# Selected application and terms review

Reviewed 2026-10-03 for this local draft. The dated library profile remains an
unchanged research artifact; this document records the PC execution decision.

## Selection

- Library ID: `github:xinntao/real-esrgan`, full profile in edition
  `2026-10-01-r2`. Each run saves the live library, hash, and exact selected profile.
- App: official Real-ESRGAN ncnn Vulkan Windows portable build, dated 20220424,
  distributed by the upstream author in release `v0.2.5.0`.
- Model: the bundled `realesrgan-x4plus-anime.bin` and `.param`, scale 4.
- Why this app: documented Windows/Vulkan support, portable dependency isolation,
  no account or API key, a small input, and a visible creative before/after.
  Selection is a one-app pilot, not a discovery cap.

Primary sources:

1. [Official upstream documentation](https://github.com/xinntao/Real-ESRGAN/tree/a4abfb2979a7bbff3f69f58f58ae324608821e27)
2. [Official release and Windows package](https://github.com/xinntao/Real-ESRGAN/releases/tag/v0.2.5.0)
3. [Portable implementation and CLI](https://github.com/xinntao/Real-ESRGAN-ncnn-vulkan/tree/v0.2.0)
4. [Anime model instructions](https://github.com/xinntao/Real-ESRGAN/blob/a4abfb2979a7bbff3f69f58f58ae324608821e27/docs/anime_model.md)

## Software and model terms, separately

The complete [upstream software license](https://github.com/xinntao/Real-ESRGAN/blob/a4abfb2979a7bbff3f69f58f58ae324608821e27/LICENSE)
is BSD-3-Clause. It permits source/binary use and redistribution subject to notice,
disclaimer and non-endorsement conditions. The complete [portable implementation
license](https://github.com/xinntao/Real-ESRGAN-ncnn-vulkan/blob/v0.2.0/LICENSE) is
MIT, including the realsr-ncnn-vulkan notice. These texts are archived locally.
This differs from treating the entire portable package as simply BSD-3-Clause.

The selected weights are distributed in the author's official portable bundle,
and the author's model documentation explicitly describes this model's local
inference route. The inspected bundle contains no separate model-license file;
the model documentation and release notes do not provide a distinct model-use
grant or additional restrictions. This is an explicit documentation gap, not a
claim that all model rights or training-data rights are independently cleared.
We use the documented official weights for this local test, preserve the source
evidence, and do not redistribute models or claim blanket commercial clearance.
Review exact weight/asset rights again before a commercial deployment or model
redistribution. Do not substitute GFPGAN, face models, or third-party weights under
this review.

The runtime uses ncnn and related bundled dependencies identified by upstream.
No binary, DLL, model or third-party sample is committed. The upstream sample
photos and One Piece clip are not extracted or used in the demonstration. A
future distribution of a packaged runtime would require its own complete
third-party notice review; this project only downloads for local execution.

## Supporting tools and original assets

Pillow 11.3.0 is installed from its CPython 3.10 Windows x64 wheel on PyPI, with a
pinned SHA-256. Its MIT-CMU license and third-party notices are included in the
installed wheel; see [Pillow licensing](https://pillow.readthedocs.io/en/stable/about.html#license).
It draws an original procedural illustration and assembles editorial frames.
No licensed photo or other creator's artwork is used. The input is deliberately
downsampled and compressed, and the video says so; it is not evidence of recovery
from an unknown real-world original.

FFmpeg/ffprobe are pre-existing PC tools, not installed or redistributed by this
project. Their full version/build strings and executable hashes are recorded in
`setup.json`. This PC's FFmpeg build reports GPL/version3 components. It encodes
the MP4; its build license is not represented as a license grant for model weights.

Narration uses installed Windows System.Speech with a standard system voice, not
voice cloning or an external service. It is labeled synthetic narration in the
run evidence. Windows fonts and speech binaries remain installed system assets;
they are not copied into the repository or presented as open-source software.
Real-ESRGAN is the selected open-source AI application; supporting OS services
are listed separately. The app itself produces no audio or animation.

## Provenance and integrity limits

`runtime.lock.json` pins the official ZIP URL and the SHA-256 of the bytes fetched
over HTTPS, as well as the Pillow wheel hash published by PyPI. The older GitHub
asset has no publisher digest/signature in the inspected release metadata.
The recorded ZIP hash detects later drift; it is not an independent publisher
signature or a complete security audit. No downloaded install scripts execute.
Extraction uses an explicit file allowlist; the executable, DLL and selected
model files are hashed again in the local setup receipt before each run.

The official portable README notes tile inconsistencies and potential black
images on some PCs. This run checks output dimensions and non-blank pixel range.
Visual quality and speed are observations for this one input on this PC, not
general benchmarks. Source detail is inferred; fine lines/textures can change.
