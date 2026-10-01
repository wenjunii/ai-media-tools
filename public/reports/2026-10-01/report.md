# AI Media Scout — 2026-10-01

The launch edition establishes 12 practical profiles across ten creative fields, separating a new release—explainroo—from current versions and established reference tools. Recent ComfyUI, InvokeAI and Velorn releases anchor image/video workflows; audio, 3D, browser AI, live visuals, XR, CAD and Blender integrations extend the toolkit. All platforms receive equal attention. Source reviews, model restrictions and unreported requirements are explicit; these tools have not been installed or benchmarked here.

Documentation reviewed today. Tools are not hands-on tested unless explicitly stated. Requirements and performance remain source-specific.

## Coverage

| Field | Finding |
| --- | --- |
| Images & design | ComfyUI and InvokeAI provide two established control/iteration workflows; both have recent September releases. Model licensing still varies. |
| Video, animation & film | explainroo is newly released; Velorn supplies an editable production timeline around generation. Early releases still need local trials. |
| Audio, music & voice | ACE-Step offers local music workflows with explicit GPU tiers. The six-pipeline model scan is a lead list; model terms are checked separately. |
| 3D, reconstruction & assets | TRELLIS.2 is a useful baseline for textured image-to-3D assets, with a significant Linux/NVIDIA hardware requirement. It is not a fresh launch. |
| Browser tools & web media | Transformers.js supports custom browser media applications; ImWeb and Tau are creator-oriented browser environments with different dependencies. |
| WebXR, VR & AR | XR Blocks has desktop and Android XR paths; Decart-XR targets Quest and uses a proprietary backend. The failed watchlist alias was resolved to official google/xrblocks. |
| Computational art & creative coding | ImWeb's AI-assisted GLSL/patch workflow and browser ML building blocks are relevant to generative systems. They require artist/developer iteration. |
| Interactive, immersive & live media | ImWeb supplies live visuals and controller mappings. Daydream Scope was evaluated but excluded from open-source profiles: its current code license is non-commercial CC BY-NC-SA 4.0. |
| 3D printing & generative CAD | Tau supports parametric CAD and export. TRELLIS.2 meshes need downstream printability checks; no new verified turnkey AI printing pipeline is claimed. |
| Games & production pipelines | MCP for Blender supports agent-assisted DCC operations; generated or retrieved assets still need topology, scale and rights checks before game use. |

## Collection limitations

- Watchlist xrblocks/xrblocks: HTTP 404 from api.github.com/repos/xrblocks/xrblocks; source not collected

## explainroo

Video, animation & film · Audio, music & voice · Computational art & creative coding

A new discovery: repository created September 25; v0.1.0 published September 30. Its first release is promising, with limited platform testing.

### Introduction

A local renderer for coding-agent-authored explainer videos, combining narration, word timing, drawings, sound and MP4 output. [Source 1](https://github.com/vincentsch/explainroo)

### What it is good for

Educational explainers, illustrated tutorials and product walkthroughs. My suggested first experiment is a short explanation of your creative process. [Source 1](https://github.com/vincentsch/explainroo)

### Demo & examples

Published sample videos and scene images are linked in the README. They demonstrate the intended output; I have not rendered an example. [Source 1](https://github.com/vincentsch/explainroo) [Source 2](https://github.com/vincentsch/explainroo/releases/tag/v0.1.0)

### Install

Use the documented source setup after installing the prerequisites. [Source 1](https://github.com/vincentsch/explainroo)

1. Clone the repository and enter its folder.
2. Install its Node dependencies; run the doctor command to download and check the models.

```sh
git clone https://github.com/vincentsch/explainroo.git
cd explainroo
npm install
node bin/explainroo.js doctor --fetch
```

### First project

A coding agent prepares the script and scene code; the local tool produces the movie. [Source 1](https://github.com/vincentsch/explainroo)

1. Start your coding agent in the project folder and request a short explainer.
2. Review the still frames and layout/speech checks.
3. Find the resulting MP4 under videos/<name>/out/video.mp4.
### Hardware & software

The maintainer tests Linux most; macOS and Windows receive less testing. [Source 1](https://github.com/vincentsch/explainroo)

- **Hardware:** No dedicated GPU required. Initial model downloads are about 400 MB; RAM minimum and render-storage budget are unreported.
- **Software:** Node.js 20.11+, FFmpeg, Chrome/Chromium and a coding agent.
- **Platforms:** Linux; macOS/Windows are expected by the maintainer but less tested.

### License, model weights & costs

MIT applies to the tool. Dependencies retain separate licenses. [Source 1](https://github.com/vincentsch/explainroo/blob/main/LICENSE) [Source 2](https://huggingface.co/hexgrad/Kokoro-82M)

- **Code:** MIT
- **Weights:** Kokoro-82M's model card declares Apache-2.0; check any additional models separately.
- **Commercial:** MIT permits commercial software use under its conditions; asset and dependency rights remain separate.
- **Cost:** Local rendering has no required paid generation API. Your coding agent and optional image services have their own costs.

### Why it merits attention

Its sample outputs and built-in layout/speech checks offer useful evidence of a reproducible workflow. Inclusion is a documentation-based assessment of an early release. [Source 1](https://github.com/vincentsch/explainroo)

### Limitations

Early-stage software, uneven OS testing and agent-dependent results. Verify a short test render before committing to a long production. [Source 1](https://github.com/vincentsch/explainroo)

### Get the tool

- [Repository](https://github.com/vincentsch/explainroo)
- [Download](https://github.com/vincentsch/explainroo/releases/tag/v0.1.0)
- [Examples](https://github.com/vincentsch/explainroo/tree/main/examples)

## ComfyUI

Images & design · Video, animation & film · Audio, music & voice · 3D, reconstruction & assets

Initial baseline. Current observed core release: v0.38.0, published September 29; this is an existing project with a recent release.

### Introduction

A visual node-based engine for constructing and reusing AI media workflows. [Source 1](https://github.com/Comfy-Org/ComfyUI)

### What it is good for

Controlled image generation, editing, masks, upscaling and model-dependent video/audio/3D pipelines. Particularly useful when repeatability and workflow sharing matter. [Source 1](https://github.com/Comfy-Org/ComfyUI)

### Demo & examples

The README links official templates and example workflows. Begin with a small image template whose required models fit your machine. [Source 1](https://github.com/Comfy-Org/ComfyUI)

### Install

Desktop downloads simplify Windows/macOS setup. Linux and advanced GPU setups can use the documented CLI route in a virtual environment. [Source 1](https://github.com/Comfy-Org/ComfyUI) [Source 2](https://docs.comfy.org/comfy-cli/getting-started)

1. Choose the official desktop build or create a Python virtual environment.
2. For CLI installation, install comfy-cli and ComfyUI, then launch.
3. Install only the checkpoint and dependencies required by your chosen template.

```sh
pip install comfy-cli
comfy install
comfy launch
```

### First project

Start with a maintained template rather than assembling a large graph immediately. [Source 1](https://github.com/Comfy-Org/ComfyUI) [Source 2](https://docs.comfy.org/comfy-cli/getting-started)

1. Load a starter workflow and select its model.
2. Edit the prompt, fix the seed, and queue an image.
3. Save the workflow JSON with the output so the experiment can be repeated.
### Hardware & software

Compute requirements depend on model, resolution and extensions. Low-memory/offload claims are not universal performance guarantees. [Source 1](https://github.com/Comfy-Org/ComfyUI)

- **Hardware:** NVIDIA, AMD, Intel and Apple Silicon paths are documented. RAM/VRAM and disk needs are model-specific; no reliable single minimum covers all workflows.
- **Software:** Compatible Python/PyTorch, the backend appropriate to your GPU, and model files. The README recommends Python 3.13, with 3.12 as a dependency-compatibility alternative.
- **Platforms:** Windows, Linux and macOS; desktop builds for Windows/macOS; optional paid cloud service.

### License, model weights & costs

Core software is GPL-3.0; extensions and hosted partner nodes are separate components. [Source 1](https://github.com/Comfy-Org/ComfyUI/blob/master/LICENSE) [Source 2](https://github.com/Comfy-Org/ComfyUI)

- **Code:** GPL-3.0
- **Weights:** Every checkpoint has its own terms; inclusion in a template does not establish open or unrestricted weights.
- **Commercial:** Commercial use of GPL software is permitted subject to its conditions; redistribution, models and services need separate checks.
- **Cost:** Local core use is free; hardware/electricity, paid cloud and partner-node credits can add costs.

### Why it merits attention

Reusable graphs, maintained templates, model-management controls and current releases make it a strong production-workflow baseline. Output quality still depends on the chosen models. [Source 1](https://github.com/Comfy-Org/ComfyUI) [Source 2](https://github.com/Comfy-Org/ComfyUI/releases/tag/v0.38.0)

### Limitations

Custom nodes can introduce conflicts; heavy video models need substantial compute. Choose model licenses and platform instructions before downloading. [Source 1](https://github.com/Comfy-Org/ComfyUI)

### Get the tool

- [Repository](https://github.com/Comfy-Org/ComfyUI)
- [Download](https://www.comfy.org/download)
- [Documentation](https://docs.comfy.org/comfy-cli/getting-started)
- [Examples](https://comfy.org/workflows/)

## InvokeAI

Images & design · Browser tools & web media

Initial baseline. Observed release v6.14.2 was published September 27; its canvas-based approach complements node-first workflows.

### Introduction

A local AI image-creation application with a browser interface, unified canvas, model manager and reusable workflows. [Source 1](https://github.com/invoke-ai/InvokeAI)

### What it is good for

Iterative concept art, inpainting/outpainting and controlled refinement of photos, sketches and renders. [Source 1](https://github.com/invoke-ai/InvokeAI)

### Demo & examples

The official documentation links tutorials and videos. Inspect the canvas and workflow examples before choosing a model. [Source 1](https://github.com/invoke-ai/InvokeAI)

### Install

Use the official Invoke Launcher, which manages installation and updates. [Source 1](https://invoke.ai/start-here/installation/)

1. Download the platform-specific launcher.
2. Windows: run the EXE. macOS: install the DMG. Linux: make the AppImage executable.
3. Open the launcher, choose Install and follow its setup flow.
### First project

A small canvas edit is a practical first project. [Source 1](https://github.com/invoke-ai/InvokeAI)

1. Add a compatible model through the model manager.
2. Generate or import an image, then use a masked canvas region for a refinement.
3. Save the result and its settings to a board or gallery.
### Hardware & software

Choose requirements for the model family rather than assuming every supported model fits the smallest GPU. [Source 1](https://invoke.ai/start-here/system-requirements/)

- **Hardware:** Documented examples: SD1.5 4 GB VRAM/8 GB RAM; SDXL 8 GB VRAM/16 GB RAM. Apple Silicon: 16 GB+ unified memory recommended. Models and outputs need additional disk space; a universal disk minimum is not stated.
- **Software:** Launcher-managed Python; manual installation requires Python 3.11–3.12 and compatible GPU drivers.
- **Platforms:** Windows 10+, macOS 14+ and Linux. AMD GPU support is Linux-only; Intel Arc is documented for Windows/Linux x86_64.

### License, model weights & costs

Apache-2.0 covers the main application; model and incorporated-component licenses are separate. [Source 1](https://github.com/invoke-ai/InvokeAI/blob/main/LICENSE) [Source 2](https://github.com/invoke-ai/InvokeAI)

- **Code:** Apache-2.0
- **Weights:** Read each model card; some supported models and API routes have restrictive or proprietary terms.
- **Commercial:** The application license permits commercial use under its conditions; this does not grant rights for every model or input asset.
- **Cost:** Local application use is free. Optional external-model services and hardware costs are separate.

### Why it merits attention

The canvas, galleries and workflow controls address the iteration and organization needs of artists. This is a workflow assessment, not a model-quality benchmark. [Source 1](https://github.com/invoke-ai/InvokeAI)

### Limitations

Large model families need substantially more memory than SDXL. GPU backends and external API models have different support and cost constraints. [Source 1](https://invoke.ai/start-here/system-requirements/) [Source 2](https://github.com/invoke-ai/InvokeAI)

### Get the tool

- [Repository](https://github.com/invoke-ai/InvokeAI)
- [Documentation](https://invoke.ai/start-here/installation/)
- [Requirements](https://invoke.ai/start-here/system-requirements/)

## Velorn

Video, animation & film · Images & design · Audio, music & voice

Initial baseline. Observed packaged release v0.3.36 was published September 26. It offers a production layer around ComfyUI.

### Introduction

A desktop video editor combining AI generation workflows with a timeline, assets, captions and export. [Source 1](https://github.com/VelornLabs/velorn)

### What it is good for

Finishing generated clips into music videos, short films and creator videos. Its main appeal is keeping generation and editing within a project. [Source 1](https://github.com/VelornLabs/velorn)

### Demo & examples

The README contains screen captures and an agent-editing animation; these illustrate the workflow, not independently measured performance. [Source 1](https://github.com/VelornLabs/velorn)

### Install

Use a packaged release for your OS; generation additionally needs local ComfyUI. [Source 1](https://github.com/VelornLabs/velorn) [Source 2](https://github.com/VelornLabs/velorn/releases/tag/v0.3.36)

1. Download the Windows installer/portable, Mac Intel/Apple Silicon, or Linux AppImage/deb asset.
2. Install and select a projects folder.
3. For generation, configure Settings > ComfyUI Connection to the same-machine server.
### First project

Begin by editing existing media before adding a large generation pipeline. [Source 1](https://github.com/VelornLabs/velorn) [Source 2](https://github.com/VelornLabs/velorn/blob/main/docs/MCP.md)

1. Create a project and import a few clips.
2. Arrange and trim the timeline; add captions and an export preset.
3. Then test a small local generation workflow after resolving its model/node dependencies.
### Hardware & software

Editing and generation have different requirements. [Source 1](https://github.com/VelornLabs/velorn)

- **Hardware:** Editing needs space for assets, cache and exports; numerical CPU/RAM minima are unreported. Heavy local video workflows may need 24 GB+ VRAM; requirements vary by model.
- **Software:** Packaged desktop app. All current generation features require local ComfyUI, required nodes/models, and credentials for paid partner routes.
- **Platforms:** Windows, macOS Intel/Apple Silicon, Linux. The desktop ComfyUI connection is limited to localhost.

### License, model weights & costs

The editor is GPL-3.0. Workflow models, nodes and services remain independently licensed. [Source 1](https://github.com/VelornLabs/velorn/blob/main/LICENSE) [Source 2](https://github.com/VelornLabs/velorn)

- **Code:** GPL-3.0
- **Weights:** Not bundled as one unrestricted model license; inspect each workflow's model terms.
- **Commercial:** GPL permits commercial use under its conditions; generated assets and partner services need separate review.
- **Cost:** Local editor is free. Local model compute and optional cloud/partner credits add costs.

### Why it merits attention

Packaged builds, editable timelines and documented generation dependencies make it a useful creator-facing candidate. Agent tools extend workflow automation. [Source 1](https://github.com/VelornLabs/velorn) [Source 2](https://github.com/VelornLabs/velorn/releases/tag/v0.3.36) [Source 3](https://github.com/VelornLabs/velorn/blob/main/docs/MCP.md)

### Limitations

The short-film creator is explicitly beta. Downloading the editor alone does not provision a complete generation environment. [Source 1](https://github.com/VelornLabs/velorn)

### Get the tool

- [Repository](https://github.com/VelornLabs/velorn)
- [Download](https://github.com/VelornLabs/velorn/releases/tag/v0.3.36)
- [Agent Guide](https://github.com/VelornLabs/velorn/blob/main/docs/MCP.md)

## ACE-Step 1.5

Audio, music & voice

Initial baseline. Active source development was observed today; the published v0.1.8 tag is from May. Current docs also describe larger XL models, which have higher memory needs.

### Introduction

A locally runnable music-generation toolkit with a Gradio interface and API. [Source 1](https://github.com/ace-step/ACE-Step-1.5)

### What it is good for

Drafting instrumentals or vocal ideas, creating variations and editing or repainting musical segments. Treat these as sketching capabilities rather than guarantees of finished commercial audio. [Source 1](https://github.com/ace-step/ACE-Step-1.5)

### Demo & examples

The project links audio examples and a browser UI. Listening to the examples is the best first check for your genre and intended use. [Source 1](https://github.com/ace-step/ACE-Step-1.5)

### Install

Install the documented Python environment with uv, or use the project's platform package where applicable. [Source 1](https://github.com/ace-step/ACE-Step-1.5/blob/main/docs/en/INSTALL.md) [Source 2](https://github.com/ace-step/ACE-Step-1.5)

1. Install Python 3.11–3.12 and uv, then clone the repository.
2. Run uv sync and start the UI; allow its initial model downloads.
3. Use the platform-specific launch instructions for MLX, ROCm or other backends.

```sh
git clone https://github.com/ace-step/ACE-Step-1.5.git
cd ACE-Step-1.5
uv sync
uv run acestep
```

### First project

Start with a short instrumental variation so you can judge style and coherence quickly. [Source 1](https://github.com/ace-step/ACE-Step-1.5)

1. Open the local Gradio UI at localhost:7860.
2. Choose a compatible model and enter musical style, duration and optional lyrics.
3. Generate a few variations, audition them and save the useful results.
### Hardware & software

The smallest DiT configuration and XL configuration have very different memory requirements. [Source 1](https://github.com/ace-step/ACE-Step-1.5/blob/main/docs/en/INSTALL.md) [Source 2](https://github.com/ace-step/ACE-Step-1.5/blob/main/docs/en/GPU_COMPATIBILITY.md)

- **Hardware:** Install guide: ≥4 GB VRAM for DiT-only mode, ≥6 GB for LM+DiT, about 10 GB disk for core models; low-memory modes use quantization/offload. XL needs about 12 GB with aggressive offload or 20 GB without. Host RAM minimum is unreported.
- **Software:** Python 3.11–3.12, uv and platform-specific PyTorch/MLX components. Windows ROCm uses Python 3.12.
- **Platforms:** Windows, Linux and macOS Apple Silicon are documented; CUDA, MPS/MLX, ROCm, Intel XPU and CPU paths vary.

### License, model weights & costs

The application declares MIT. Verify the selected checkpoints independently before production. [Source 1](https://github.com/ace-step/ACE-Step-1.5/blob/main/LICENSE) [Source 2](https://github.com/ace-step/ACE-Step-1.5) [Source 3](https://huggingface.co/ACE-Step/Ace-Step1.5)

- **Code:** MIT
- **Weights:** The official Ace-Step1.5 turbo checkpoint card declares MIT; verify other base, SFT, XL and language-model checkpoints individually.
- **Commercial:** MIT covers the software; music originality, source-audio rights and the chosen model terms remain separate.
- **Cost:** Local inference does not require a paid generation API. Hardware and optional hosted services have separate costs.

### Why it merits attention

Practical generation/editing controls and detailed hardware-tier documentation justify a trial. Developer speed and quality claims are not independent benchmarks. [Source 1](https://github.com/ace-step/ACE-Step-1.5) [Source 2](https://github.com/ace-step/ACE-Step-1.5/blob/main/docs/en/GPU_COMPATIBILITY.md)

### Limitations

Genre fidelity, long-form structure and lyrics need listening checks. Low-memory settings trade capabilities and speed for fit. [Source 1](https://github.com/ace-step/ACE-Step-1.5) [Source 2](https://github.com/ace-step/ACE-Step-1.5/blob/main/docs/en/GPU_COMPATIBILITY.md)

### Get the tool

- [Repository](https://github.com/ace-step/ACE-Step-1.5)
- [Installation](https://github.com/ace-step/ACE-Step-1.5/blob/main/docs/en/INSTALL.md)
- [Gpu Guide](https://github.com/ace-step/ACE-Step-1.5/blob/main/docs/en/GPU_COMPATIBILITY.md)
- [Model](https://huggingface.co/ACE-Step/Ace-Step1.5)

## TRELLIS.2

3D, reconstruction & assets · Games & production pipelines · 3D printing & generative CAD

Initial baseline rather than a new launch. The repository's last observed push was July 10; official inference and model documentation remain available.

### Introduction

An image-to-3D research pipeline producing textured assets, with additional shape-conditioned texture generation. [Source 1](https://github.com/microsoft/TRELLIS.2)

### What it is good for

Prototyping game props and digital sculptural assets from reference images. Fabrication is a downstream experiment; output is not certified print-ready. [Source 1](https://github.com/microsoft/TRELLIS.2)

### Demo & examples

The official repository links a Hugging Face demo and includes a local web app and example asset exports. [Source 1](https://github.com/microsoft/TRELLIS.2) [Source 2](https://huggingface.co/microsoft/TRELLIS.2-4B)

### Install

Use the official Linux/CUDA environment and recursive clone; installation compiles several dependencies. [Source 1](https://github.com/microsoft/TRELLIS.2)

1. Prepare compatible NVIDIA drivers, CUDA Toolkit and Conda.
2. Clone recursively, run the documented setup, then activate trellis2.
3. Launch the local app after downloading the official checkpoint.

```sh
git clone -b main https://github.com/microsoft/TRELLIS.2.git --recursive
cd TRELLIS.2
. ./setup.sh --new-env --basic --flash-attn --nvdiffrast --nvdiffrec --cumesh --o-voxel --flexgemm
conda activate trellis2
python app.py
```

### First project

Use one clear object reference before trying complex scenes. [Source 1](https://github.com/microsoft/TRELLIS.2) [Source 2](https://huggingface.co/microsoft/TRELLIS.2-4B)

1. Upload an object image to the local demo.
2. Inspect the generated shape and material from multiple views.
3. Export a GLB for a DCC/game workflow; for printing, inspect and repair the mesh in a separate tool.
### Hardware & software

The official implementation is currently tested only on Linux. [Source 1](https://github.com/microsoft/TRELLIS.2)

- **Hardware:** NVIDIA GPU with at least 24 GB VRAM; tested by the authors on A100/H100. Host RAM and total disk minimum are not stated.
- **Software:** Python 3.8+, Conda recommended, CUDA Toolkit 12.4 recommended; default setup uses PyTorch 2.6/CUDA 12.4 and compiled geometry/rendering packages.
- **Platforms:** Officially tested Linux path. Native macOS and Windows support are not established by this documentation; use a suitable Linux GPU host.

### License, model weights & costs

The project states that code and its model are MIT; renderer dependencies have separate terms. [Source 1](https://github.com/microsoft/TRELLIS.2/blob/main/LICENSE) [Source 2](https://huggingface.co/microsoft/TRELLIS.2-4B) [Source 3](https://github.com/microsoft/TRELLIS.2)

- **Code:** MIT
- **Weights:** The official TRELLIS.2-4B model card declares MIT.
- **Commercial:** MIT permits commercial use under its conditions; inspect renderer dependencies and rights in the reference images.
- **Cost:** No required paid generation API for local inference; a high-memory GPU or rented host can be costly.

### Why it merits attention

Textured exports and a published example pipeline support useful asset exploration. Production topology, consistency and quality still need individual inspection. [Source 1](https://github.com/microsoft/TRELLIS.2)

### Limitations

Research installation complexity and high VRAM demand. Generated geometry may need cleanup, retopology, scaling and printability checks. [Source 1](https://github.com/microsoft/TRELLIS.2)

### Get the tool

- [Repository](https://github.com/microsoft/TRELLIS.2)
- [Model](https://huggingface.co/microsoft/TRELLIS.2-4B)
- [License](https://github.com/microsoft/TRELLIS.2/blob/main/LICENSE)

## Transformers.js

Browser tools & web media · Computational art & creative coding · Interactive, immersive & live media · Audio, music & voice · Images & design

Initial baseline. Observed version 4.3.0 was released September 16. This is a building block for custom creative applications.

### Introduction

A JavaScript library for running pretrained vision, audio and language models in browsers using ONNX Runtime. [Source 1](https://github.com/huggingface/transformers.js)

### What it is good for

Custom captioning, transcription, segmentation and responsive media interfaces. Creative-coding uses are integrations you build, rather than a finished authoring application. [Source 1](https://github.com/huggingface/transformers.js)

### Demo & examples

The official examples repository provides runnable demonstration applications and templates. [Source 1](https://github.com/huggingface/transformers.js-examples)

### Install

Install the NPM package in a JavaScript project, or use the documented ES-module/CDN path. [Source 1](https://github.com/huggingface/transformers.js)

1. Choose an example for the task you need.
2. Add the package or documented import to the project.
3. Load a supported ONNX model and check its card and download size.

```sh
npm i @huggingface/transformers
```

### First project

A useful first experiment is a small browser audio or image-analysis interface. [Source 1](https://github.com/huggingface/transformers.js) [Source 2](https://github.com/huggingface/transformers.js-examples)

1. Adapt a matching official example.
2. Start with the default WASM/CPU path; enable WebGPU only on a compatible browser.
3. Test the result with your own media and measure latency on each target device.
### Hardware & software

Memory and download size depend on the actual ONNX model. [Source 1](https://github.com/huggingface/transformers.js)

- **Hardware:** WASM inference can use the CPU; WebGPU uses compatible graphics hardware/browser support. No universal RAM/VRAM or disk minimum applies.
- **Software:** JavaScript ES modules or an NPM setup, ONNX-compatible model files and WASM runtime assets; WebGPU is optional.
- **Platforms:** Modern browsers on supported desktop/mobile systems, subject to model and backend compatibility. WebGPU support varies.

### License, model weights & costs

Apache-2.0 applies to the library, not automatically to all downloaded models. [Source 1](https://github.com/huggingface/transformers.js/blob/main/LICENSE) [Source 2](https://github.com/huggingface/transformers.js)

- **Code:** Apache-2.0
- **Weights:** Each ONNX model retains its model-card license; conversions do not remove original restrictions.
- **Commercial:** Library commercial use is allowed under Apache terms; selected models and inputs need separate checks.
- **Cost:** Local/browser inference has no compulsory paid API; hosting, bandwidth and optional external services may cost money.

### Why it merits attention

Official examples and explicit backend/quantization controls make it a strong foundation for browser experiments. You supply the creative interface and quality evaluation. [Source 1](https://github.com/huggingface/transformers.js) [Source 2](https://github.com/huggingface/transformers.js-examples)

### Limitations

Some tasks/models are unsupported. Large models strain browser memory, and WebGPU is uneven across devices. [Source 1](https://github.com/huggingface/transformers.js)

### Get the tool

- [Repository](https://github.com/huggingface/transformers.js)
- [Examples](https://github.com/huggingface/transformers.js-examples)
- [Documentation](https://huggingface.co/docs/transformers.js)

## XR Blocks

WebXR, VR & AR · Interactive, immersive & live media · Browser tools & web media

Initial baseline. Current source activity was observed today; published v0.21.1 is from August 25. The official repository is google/xrblocks.

### Introduction

A three.js-based library for interactive spatial applications, with desktop simulation, gesture handling and optional multimodal AI integration. [Source 1](https://github.com/google/xrblocks)

### What it is good for

Prototyping AI-assisted spatial interfaces and interactive installation concepts before deploying to a supported XR headset. [Source 1](https://github.com/google/xrblocks)

### Demo & examples

The Basic template responds to clicks on desktop and pinch/controller input in XR. The official sample catalog includes AI-oriented examples. [Source 1](https://xrblocks.github.io/docs/templates/Basic/) [Source 2](https://github.com/google/xrblocks)

### Install

Try the hosted starter first, then clone and serve the SDK's samples for development. [Source 1](https://github.com/google/xrblocks)

1. Open the Basic template in a supported browser.
2. For development, clone the repository, install its dependencies and serve the samples.
3. Use the local simulator before testing device-specific features.

```sh
git clone https://github.com/google/xrblocks.git
cd xrblocks
npm ci
npm run serve
```

### First project

A simple spatial object interaction is the recommended first experiment. [Source 1](https://xrblocks.github.io/docs/templates/Basic/) [Source 2](https://github.com/google/xrblocks)

1. Click the cylinder in the desktop template.
2. Modify its scene and interaction script.
3. Add the separate AI example only after configuring the required provider access.
### Hardware & software

The SDK's desktop and headset paths have different capabilities. [Source 1](https://github.com/google/xrblocks)

- **Hardware:** Desktop simulator or supported Android XR headset; RAM/VRAM/storage minima are unreported.
- **Software:** Chrome v136+ and WebXR support for targeted XR use; Node/NPM for development; provider access for Gemini AI features.
- **Platforms:** Desktop Chrome simulator and documented Android XR devices. Do not assume support for every Quest, Vision Pro or browser.

### License, model weights & costs

Apache-2.0 covers the SDK. Gemini and headset/platform services have their own terms. [Source 1](https://github.com/google/xrblocks/blob/main/LICENSE) [Source 2](https://github.com/google/xrblocks)

- **Code:** Apache-2.0
- **Weights:** Optional Gemini integration uses a proprietary service, not bundled open model weights.
- **Commercial:** SDK commercial use is allowed under Apache terms; provider and device terms remain separate.
- **Cost:** SDK is free. AI-service usage and XR hardware may add costs; a desktop simulator reduces initial hardware needs.

### Why it merits attention

Official templates, documented interactions and a desktop simulator make spatial prototyping approachable. This is a developer toolkit, with no independent headset testing here. [Source 1](https://github.com/google/xrblocks) [Source 2](https://xrblocks.github.io/docs/templates/Basic/)

### Limitations

Device APIs and browser versions constrain portability. AI functionality is optional and can depend on a proprietary provider. [Source 1](https://github.com/google/xrblocks)

### Get the tool

- [Repository](https://github.com/google/xrblocks)
- [Demo](https://xrblocks.github.io/docs/templates/Basic/)
- [Documentation](https://xrblocks.github.io/docs/)

## ImWeb

Computational art & creative coding · Interactive, immersive & live media · Browser tools & web media · Video, animation & film

Initial baseline. Observed release v0.25.0 was published September 17; source activity September 27. Its explicit AGPL declaration was checked directly.

### Introduction

A browser video-synthesis instrument combining compositing, GLSL, 3D, controllers and AI-assisted patch/shader creation. [Source 1](https://github.com/imweb-project/ImWeb)

### What it is good for

Live visuals, audio-reactive installations and iterative shader experiments. It can use hosted AI providers or a local Ollama model. [Source 1](https://github.com/imweb-project/ImWeb)

### Demo & examples

The README shows the signal flow and interfaces; the application includes a guided tour. Published documentation illustrates functionality rather than tested show reliability. [Source 1](https://github.com/imweb-project/ImWeb)

### Install

Clone the application and run its Node development server. [Source 1](https://github.com/imweb-project/ImWeb)

1. Install Node 18+ and clone the official repository.
2. Install dependencies and start the development server.
3. Open localhost:5173 in a supported browser.

```sh
git clone https://github.com/imweb-project/ImWeb.git
cd ImWeb
npm install
npm run dev
```

### First project

Start with a simple visual patch before adding AI or external control. [Source 1](https://github.com/imweb-project/ImWeb)

1. Choose a source, adjust a mix/effect and preview the canvas.
2. Connect audio or MIDI/OSC controls as needed.
3. Configure a local/hosted AI provider for patch or GLSL assistance; export a project or record WebM.
### Hardware & software

Graphics load depends on resolution, effects and sources; AI inference can be local or remote. [Source 1](https://github.com/imweb-project/ImWeb)

- **Hardware:** WebGL-capable graphics and optional camera/audio/MIDI hardware. RAM/VRAM/storage minima are unreported; a local Ollama model adds its own compute requirements.
- **Software:** Node 18+; Chrome 113+ recommended. OSC needs the bundled Node relay; AI needs Ollama or provider credentials.
- **Platforms:** Browser-based; Chrome recommended, Firefox/Safari WebGL modes have limitations. Native OS support is not separately certified.

### License, model weights & costs

The LICENSE explicitly declares AGPL-3.0-or-later; an artistic dedication explains GitHub's unclassified result. [Source 1](https://github.com/imweb-project/ImWeb/blob/main/LICENSE)

- **Code:** AGPL-3.0-or-later
- **Weights:** Local Ollama models have their own licenses; hosted AI providers are separate proprietary services.
- **Commercial:** AGPL permits commercial use, with source-sharing conditions including relevant network use; check dependent components separately.
- **Cost:** Local instrument is free. Local AI hardware and hosted-provider usage can add costs.

### Why it merits attention

Detailed signal routing, controller mappings and AI-provider options make this a relevant computational-art candidate. Included as an emerging instrument, not a proven touring setup. [Source 1](https://github.com/imweb-project/ImWeb) [Source 2](https://github.com/imweb-project/ImWeb/releases/tag/v0.25.0)

### Limitations

Small project and complex live-media surface. Browser/device differences and local-model speed need rehearsal before a performance. [Source 1](https://github.com/imweb-project/ImWeb)

### Get the tool

- [Repository](https://github.com/imweb-project/ImWeb)
- [Download](https://github.com/imweb-project/ImWeb/releases/tag/v0.25.0)
- [License](https://github.com/imweb-project/ImWeb/blob/main/LICENSE)

## Tau

3D printing & generative CAD · 3D, reconstruction & assets · Browser tools & web media · Games & production pipelines

Initial baseline. Current source activity was observed today; this is a project under heavy development, with no stable release inferred.

### Introduction

An AI-assisted browser parametric CAD environment supporting multiple geometry kernels and export formats. [Source 1](https://github.com/taucad/tau)

### What it is good for

Exploring dimension-driven forms, printable prototypes and editable CAD ideas. Suggested experiment: a small enclosure with a few adjustable parameters. [Source 1](https://github.com/taucad/tau)

### Demo & examples

The project links its hosted tau.new application and screenshots. The hosted service is a separate deployment with its own availability and AI access. [Source 1](https://github.com/taucad/tau)

### Install

The hosted version avoids installation. Self-hosted development requires infrastructure and provider configuration. [Source 1](https://github.com/taucad/tau/blob/main/contributing.md) [Source 2](https://github.com/taucad/tau)

1. For the quickest evaluation, open tau.new.
2. For local development, install Node 24+, pnpm and Docker; clone the repository.
3. Start dependencies/infrastructure, copy the UI/API example environment files, configure your provider keys and start the dev servers.

```sh
git clone https://github.com/taucad/tau.git
cd tau
pnpm install
pnpm infra:up
cp apps/ui/.env.example apps/ui/.env.local
cp apps/api/.env.example apps/api/.env.local
pnpm dev
```

### First project

Use its code/parametric workflow, then check the exported geometry in the downstream application. [Source 1](https://github.com/taucad/tau)

1. Create a simple model using an implemented CAD kernel.
2. Adjust dimensions and inspect the preview.
3. Export an appropriate mesh/solid format, then verify scale, tolerances and slicing before printing.
### Hardware & software

Hosted use and local development need different resources. [Source 1](https://github.com/taucad/tau/blob/main/contributing.md) [Source 2](https://github.com/taucad/tau)

- **Hardware:** Browser-capable device; no numerical RAM/VRAM/disk minimum is published in the reviewed setup. Local infrastructure requires additional memory/storage.
- **Software:** Local development: Node.js 24+, pnpm, Docker, PostgreSQL/Redis services and configured provider keys.
- **Platforms:** Browser use is described for desktop/mobile. Local development depends on availability of the listed tools; OS-specific certification is unreported.

### License, model weights & costs

MIT covers the core. The optional OpenSCAD component is GPL-2.0-or-later and changes obligations for a combined distribution. [Source 1](https://github.com/taucad/tau) [Source 2](https://github.com/taucad/tau/blob/main/license)

- **Code:** MIT
- **Weights:** AI models/providers are configured separately; no blanket open model-weight license is established.
- **Commercial:** Core MIT use is permitted; a distribution including the OpenSCAD kernel must meet the stated GPL conditions.
- **Cost:** Source is free. Hosting, provider calls and optional commercial kernels can have separate costs; current hosted pricing is unverified.

### Why it merits attention

Editable parametric geometry is more suitable for dimension-driven work than a purely decorative generated mesh. Multiple documented kernels and exports support experimentation. [Source 1](https://github.com/taucad/tau)

### Limitations

Heavy-development warning; planned capabilities are not implemented features. Printing and manufacturing still require geometry and tolerance checks. [Source 1](https://github.com/taucad/tau)

### Get the tool

- [Repository](https://github.com/taucad/tau)
- [Demo](https://tau.new)
- [Setup](https://github.com/taucad/tau/blob/main/contributing.md)

## MCP for Blender

Games & production pipelines · 3D, reconstruction & assets · Computational art & creative coding

Initial baseline. Current documentation uses the renamed repository/package mcp-for-blender; older blender-mcp setups retain compatibility. Source activity was observed September 30.

### Introduction

An MCP server and Blender addon enabling compatible AI clients to inspect and operate Blender scenes. [Source 1](https://github.com/ahujasid/mcp-for-blender)

### What it is good for

Agent-assisted scene blocking, materials, repetitive DCC tasks and game-asset prototyping. The language model is supplied by your client. [Source 1](https://github.com/ahujasid/mcp-for-blender)

### Demo & examples

The README links setup videos and shows example interactions. Test a small scene before trusting complex asset edits. [Source 1](https://github.com/ahujasid/mcp-for-blender)

### Install

With uv already installed, use the documented setup command and choose your client integration. [Source 1](https://github.com/ahujasid/mcp-for-blender)

1. Install Blender 3.0+, Python 3.10+ and uv.
2. Run the setup helper; choose the AI client and allow it to install/configure the addon.
3. Fully restart the AI client and open Blender.

```sh
uvx mcp-for-blender setup
```

### First project

Begin with a disposable scene so the agent's geometry choices are easy to inspect. [Source 1](https://github.com/ahujasid/mcp-for-blender)

1. Connect the configured client to the Blender addon.
2. Ask for a simple scene or repetitive modeling task.
3. Inspect topology, scale and materials in Blender before exporting to a game pipeline.
### Hardware & software

Blender's scene complexity and the selected AI backend govern compute. [Source 1](https://github.com/ahujasid/mcp-for-blender)

- **Hardware:** A machine capable of the intended Blender workload. The integration publishes no separate RAM/VRAM/storage minimum; local language models add their own requirements.
- **Software:** Blender 3.0+, Python 3.10+, uv and a compatible MCP client. External asset/generation services may need separate keys.
- **Platforms:** Documented Windows, macOS and Linux setup paths.

### License, model weights & costs

MIT covers the integration; Blender, client/model and external asset services keep their own terms. [Source 1](https://github.com/ahujasid/mcp-for-blender/blob/main/LICENSE) [Source 2](https://github.com/ahujasid/mcp-for-blender)

- **Code:** MIT
- **Weights:** No inference model is supplied as part of one universal license; use your client's chosen model.
- **Commercial:** MIT integration use is permitted; scene assets, external generation and application distribution need separate checks.
- **Cost:** Integration source is free. AI subscriptions, optional generation services and Blender rendering hardware can add costs.

### Why it merits attention

It targets real scene inspection and DCC operations, with current setup guidance and client integrations. Inclusion reflects workflow usefulness, not tested modeling skill. [Source 1](https://github.com/ahujasid/mcp-for-blender)

### Limitations

An agent can execute Python inside Blender. Keep the socket local and review work on a disposable scene; optional safe mode is documented. Final asset quality requires human inspection. [Source 1](https://github.com/ahujasid/mcp-for-blender)

### Get the tool

- [Repository](https://github.com/ahujasid/mcp-for-blender)
- [License](https://github.com/ahujasid/mcp-for-blender/blob/main/LICENSE)

## Decart-XR

WebXR, VR & AR · Interactive, immersive & live media · Video, animation & film

Initial baseline rather than a new release. Last observed source push: August 16. Included to show an immersive workflow and its important service dependency.

### Introduction

An open-source Unity/Quest application that streams passthrough camera video to Decart for AI restyling. [Source 1](https://github.com/DecartAI/Decart-XR)

### What it is good for

Researching immersive transformations of a live physical environment. This is a headset experiment rather than a self-contained open AI model. [Source 1](https://github.com/DecartAI/Decart-XR)

### Demo & examples

The README contains transformation animations and screenshots. The published latency figures are developer claims and were not measured here. [Source 1](https://github.com/DecartAI/Decart-XR)

### Install

Build the documented Unity project for the headset; provider access is a separate requirement. [Source 1](https://github.com/DecartAI/Decart-XR)

1. Clone the repository and open DecartAI-Quest-Unity in Unity Hub.
2. Use the documented Unity version, install the required XR packages and apply project settings.
3. Build an Android ARM64 APK, install it on the Quest and grant the camera permission.

```sh
git clone https://github.com/DecartAI/Decart-XR.git
cd Decart-XR/DecartAI-Quest-Unity
```

### First project

Treat this as an experimental, service-dependent prototype. [Source 1](https://github.com/DecartAI/Decart-XR)

1. Configure the required Decart access and optional voice-control provider.
2. Run the app and select a restyling mode.
3. Test network stability and the actual visual/latency experience on the headset.
### Hardware & software

The documented setup is specific to Quest, Unity and a live network. [Source 1](https://github.com/DecartAI/Decart-XR)

- **Hardware:** Meta Quest 3 with Horizon OS v74+; 8+ Mbps bidirectional internet. Desktop build-machine RAM/VRAM/storage minima are unreported.
- **Software:** Unity 6 (6000.0.34f1), Android build support, Meta XR packages and service configuration; optional Wit.ai for voice input.
- **Platforms:** Android ARM64 build targeting Quest 3. Other headsets are not established by the reviewed prerequisites.

### License, model weights & costs

MIT covers this application. Unity/Meta components and Decart AI remain separately licensed. [Source 1](https://github.com/DecartAI/Decart-XR/blob/main/LICENSE) [Source 2](https://github.com/DecartAI/Decart-XR)

- **Code:** MIT
- **Weights:** Decart inference is a proprietary hosted service; open model weights are not provided here.
- **Commercial:** Application MIT terms do not establish commercial rights to the backend, Unity/Meta SDKs or captured media.
- **Cost:** Headset and development hardware required; AI service access/pricing must be checked separately. Offline AI inference is not documented.

### Why it merits attention

The documented camera-to-WebRTC-to-headset architecture offers a concrete reference for immersive AI experiments. Inclusion is for research value, with dependencies disclosed. [Source 1](https://github.com/DecartAI/Decart-XR)

### Limitations

Proprietary-service dependence, network latency and camera permissions. Developer performance figures do not prove comfort or suitability for a public installation. [Source 1](https://github.com/DecartAI/Decart-XR)

### Get the tool

- [Repository](https://github.com/DecartAI/Decart-XR)
- [License](https://github.com/DecartAI/Decart-XR/blob/main/LICENSE)

Source collection completed: 2026-10-01T18:37:47.642762+00:00
Search is a bounded sample. Stars and recent pushes are discovery signals, not verified quality or meaningful upgrades.
