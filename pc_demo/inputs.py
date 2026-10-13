"""Bounded artwork ingestion; archived originals and model inputs stay distinct."""
import hashlib
import io
import pathlib

MAX_BYTES = 20 * 1024 * 1024


def validate_size(size):
    if (not isinstance(size, (list, tuple)) or len(size) != 2
            or any(type(value) is not int or not 64 <= value <= 1024 for value in size)):
        raise ValueError('Artwork must be 64 to 1024 pixels on each side; export a smaller copy if needed')
    return tuple(size)


def input_relative(manifest):
    name = manifest.get('input_file', 'inputs/input.jpg')
    if name not in ('inputs/input.jpg', 'inputs/input.png'):
        raise ValueError('Unsupported model input path in manifest')
    return name


def source_relative(manifest):
    source = manifest.get('source_asset')
    if source is None:
        return None  # Original controlled runs predate custom artwork support.
    if not isinstance(source, dict) or source.get('file') not in ('inputs/source.png', 'inputs/source.jpg'):
        raise ValueError('Unsupported original artwork path in manifest')
    return source['file']


def provenance_hashes(manifest):
    result = {input_relative(manifest): manifest['input_sha256'],
              'outputs/actual-output.png': manifest['output_sha256']}
    original = source_relative(manifest)
    if original:
        result[original] = manifest['source_asset']['sha256']
    return result


def load_custom_input(path):
    """Validate before creating a run, downloading evidence or invoking the GPU."""
    from PIL import Image, ImageCms, ImageOps
    path = pathlib.Path(path)
    if not path.is_file():
        raise ValueError('Artwork must be an existing local PNG or JPEG file')
    with path.open('rb') as stream:
        raw = stream.read(MAX_BYTES + 1)
    if len(raw) > MAX_BYTES:
        raise ValueError('Artwork exceeds the 20 MiB input limit')
    with Image.open(io.BytesIO(raw)) as source:
        if source.format not in ('PNG', 'JPEG'):
            raise ValueError('Artwork must be PNG or JPEG')
        validate_size(source.size)
        if getattr(source, 'n_frames', 1) != 1:
            raise ValueError('Animated images are unsupported; export one still frame')
        if (source.mode not in ('RGB', 'RGBA', 'L', 'LA', 'P')
                or (source.format == 'PNG' and raw[24] > 8)):
            raise ValueError('Export an 8-bit RGB or grayscale PNG/JPEG first')
        source.load()  # Reject truncated/corrupt data before any run is created.
        if source.convert('RGBA').getchannel('A').getextrema() != (255, 255):
            raise ValueError('Transparent artwork is unsupported; export an opaque copy with your chosen background')
        orientation = source.getexif().get(274, 1)
        normalized = ImageOps.exif_transpose(source)
        profile = source.info.get('icc_profile')
        if normalized.mode in ('P', 'RGBA', 'LA'):
            normalized = normalized.convert('RGB')
        if profile:
            try:
                normalized = ImageCms.profileToProfile(normalized, ImageCms.ImageCmsProfile(io.BytesIO(profile)),
                                                       ImageCms.createProfile('sRGB'), outputMode='RGB')
            except (OSError, ValueError, ImageCms.PyCMSError) as error:
                raise ValueError('Cannot convert the embedded color profile; export an sRGB copy') from error
        else:
            normalized = normalized.convert('RGB')
        details = {'kind': 'custom', 'file': 'inputs/source.' + ('png' if source.format == 'PNG' else 'jpg'),
                   'sha256': hashlib.sha256(raw).hexdigest(), 'original_name': path.name,
                   'original_size': list(source.size), 'format': source.format, 'mode': source.mode,
                   'exif_orientation': orientation, 'input_size': list(normalized.size),
                   'color': 'converted embedded profile to sRGB' if profile else 'unprofiled pixels treated as sRGB',
                   'normalization': 'EXIF orientation applied; opaque RGB PNG; metadata removed; no resizing or JPEG recompression'}
        normalized.info.clear()
        return raw, normalized, details


def save_custom_input(run, prepared):
    raw, normalized, details = prepared
    (run / details['file']).write_bytes(raw)
    normalized.save(run / 'inputs/input.png', format='PNG')
    return {'input_file': 'inputs/input.png', 'source_asset': details,
            'source_artwork': 'User-selected local artwork; original bytes preserved. ' + details['normalization']}


def verify_custom_input(run, manifest):
    """Check that the archived original really produces the saved model input."""
    from PIL import Image
    original = source_relative(manifest)
    if original:
        _, expected, _ = load_custom_input(run / original)
        with Image.open(run / input_relative(manifest)) as actual:
            if actual.mode != 'RGB' or actual.size != expected.size or actual.tobytes() != expected.tobytes():
                raise ValueError('Model input does not match normalization of the archived original')
