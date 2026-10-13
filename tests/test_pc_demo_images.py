"""Real image ingestion checks, using the already reviewed Pillow dependency."""
import pathlib
import tempfile
import unittest
from unittest.mock import patch
from pc_demo.inputs import load_custom_input, save_custom_input, verify_custom_input

try:
    from PIL import Image, ImageCms
except ImportError:
    Image = None


@unittest.skipIf(Image is None, 'Run with the PC venv; Windows CI installs the pinned Pillow wheel')
class ArtworkInputTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = pathlib.Path(self.temporary.name)
        self.source = self.root / 'my artwork.png'

    def test_original_bytes_and_non_square_pixels_are_preserved(self):
        original = Image.new('RGB', (320, 192), '#347a56')
        original.putpixel((40, 40), (255, 0, 0))
        original.save(self.source)
        raw = self.source.read_bytes()
        prepared = load_custom_input(self.source)
        run = self.root / 'run'
        (run / 'inputs').mkdir(parents=True)
        manifest = save_custom_input(run, prepared)
        self.assertEqual(self.source.read_bytes(), raw)
        self.assertEqual((run / 'inputs/source.png').read_bytes(), raw)
        with Image.open(run / 'inputs/input.png') as image:
            self.assertEqual(image.size, (320, 192))
            self.assertEqual(image.tobytes(), original.tobytes())
        verify_custom_input(run, manifest)
        Image.new('RGB', (320, 192), 'red').save(run / 'inputs/input.png')
        with self.assertRaisesRegex(ValueError, 'archived original'):
            verify_custom_input(run, manifest)

    def test_jpeg_orientation_is_applied_once_and_metadata_is_removed(self):
        self.source = self.root / 'camera export.jpg'
        original = Image.new('RGB', (96, 64), 'red')
        original.paste('blue', (0, 0, 48, 64))
        exif = Image.Exif()
        exif[274] = 6
        original.save(self.source, exif=exif)
        _, result, details = load_custom_input(self.source)
        self.assertEqual(details['original_size'], [96, 64])
        self.assertEqual(details['input_size'], [64, 96])
        self.assertEqual(result.size, (64, 96))
        self.assertEqual(result.info, {})
        self.assertEqual(details['exif_orientation'], 6)
        self.assertGreater(result.getpixel((30, 10))[2], 200)
        self.assertGreater(result.getpixel((30, 80))[0], 200)

    def test_embedded_srgb_profile_is_converted_and_recorded(self):
        profile = ImageCms.ImageCmsProfile(ImageCms.createProfile('sRGB')).tobytes()
        Image.new('RGB', (64, 64), '#238f42').save(self.source, icc_profile=profile)
        _, image, details = load_custom_input(self.source)
        self.assertEqual(image.getpixel((10, 10)), (35, 143, 66))
        self.assertEqual(details['color'], 'converted embedded profile to sRGB')
        self.assertEqual(image.info, {})

    def test_invalid_profile_is_not_silently_discarded(self):
        Image.new('RGB', (64, 64)).save(self.source, icc_profile=b'not a profile')
        with self.assertRaisesRegex(ValueError, 'color profile'):
            load_custom_input(self.source)

    def test_transparency_is_rejected_but_opaque_rgba_is_supported(self):
        Image.new('RGBA', (64, 64), (1, 2, 3, 0)).save(self.source)
        with self.assertRaisesRegex(ValueError, 'Transparent'):
            load_custom_input(self.source)
        Image.new('RGBA', (64, 64), (1, 2, 3, 255)).save(self.source)
        self.assertEqual(load_custom_input(self.source)[1].mode, 'RGB')

    def test_animated_and_unsupported_formats_are_rejected(self):
        one, two = Image.new('RGB', (64, 64), 'red'), Image.new('RGB', (64, 64), 'blue')
        one.save(self.source, save_all=True, append_images=[two], duration=100, loop=0)
        with self.assertRaisesRegex(ValueError, 'Animated'):
            load_custom_input(self.source)
        one.save(self.source, format='BMP')
        with self.assertRaisesRegex(ValueError, 'PNG or JPEG'):
            load_custom_input(self.source)

    def test_large_dimensions_and_high_bit_depth_are_rejected(self):
        Image.new('RGB', (1025, 64)).save(self.source)
        with self.assertRaisesRegex(ValueError, '64 to 1024'):
            load_custom_input(self.source)
        Image.new('I;16', (64, 64)).save(self.source)
        with self.assertRaisesRegex(ValueError, '8-bit'):
            load_custom_input(self.source)

    def test_bounded_file_read_and_corrupt_input_do_not_start_a_run(self):
        self.source.write_bytes(b'x' * 41)
        with patch('pc_demo.inputs.MAX_BYTES', 40), self.assertRaisesRegex(ValueError, '20 MiB'):
            load_custom_input(self.source)
        with patch('pc_demo.pipeline.verified_runtime', side_effect=AssertionError('must validate first')):
            from pc_demo.pipeline import run_demo
            with self.assertRaises(OSError):
                run_demo(input_image=self.source)

    def test_contain_keeps_portrait_and_landscape_aspect_ratios(self):
        from pc_demo.render import contain
        for size in ((64, 128), (128, 64)):
            with self.subTest(size=size):
                result = contain(Image.new('RGB', size, 'red'), (256, 256), 'black')
                box = result.getbbox()
                self.assertEqual((box[2]-box[0])/(box[3]-box[1]), size[0]/size[1])
                self.assertEqual(result.getpixel((128, 128)), (255, 0, 0))
