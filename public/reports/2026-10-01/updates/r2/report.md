# AI Media Scout — 2026-10-01 · Update 1

Requested expanded-search update: 27 additional detailed guides and 38 further software-license/creative-AI screened discoveries, with no fixed count quota. Together with the preserved original 12 guides, these add 65 tools to the searchable library. New September projects include BeefTV, YuE2 Studio and BridgeClip; established tools are first coverage, not new-launch claims. All 189 repository queries and 13 model tasks ran; 92 broad queries were bounded, so this is not an exhaustive inventory. Code, model weights, proprietary AI hosts and missing hardware requirements are separated. Documentation was reviewed; no tool was installed or benchmarked. The original sent report and email receipt remain unchanged.

Documentation reviewed today. Tools are not hands-on tested unless explicitly stated. Requirements and performance remain source-specific.

## Coverage

| Field | Finding |
| --- | --- |
| Images & design | Krita AI, SwarmUI and other local interfaces add control, painting and environment choices absent from the original edition. Model terms and backend compatibility differ. [Source 1](https://github.com/Acly/krita-ai-diffusion) [Source 2](https://github.com/mcmonkeyprojects/SwarmUI) |
| Video, animation & film | Recent BeefTV and BridgeClip offer canvas and clipping workflows. Wan2.2 and other generators enter the pending appendix; output consistency still needs testing. [Source 1](https://github.com/glanderness/BeefTV) [Source 2](https://github.com/bridge-mind/bridgeclip) [Source 3](https://github.com/Wan-Video/Wan2.2) |
| Audio, music & voice | New YuE2 Studio adds an editable musical score. Chatterbox, OpenVoice and KittenTTS cover speech; AudioCraft and F5-TTS have non-commercial published weights. [Source 1](https://github.com/timoncool/YuE2-Studio) [Source 2](https://github.com/facebookresearch/audiocraft) [Source 3](https://github.com/SWivid/F5-TTS) |
| 3D, reconstruction & assets | TripoSR provides a detailed image-to-mesh starting point; TripoSG, InstantMesh, DreamGaussian and ComfyUI-3D-Pack remain screened leads with geometry and setup review pending. [Source 1](https://github.com/VAST-AI-Research/TripoSR) [Source 2](https://github.com/VAST-AI-Research/TripoSG) |
| Browser tools & web media | WebLLM and Web Stable Diffusion expose WebGPU paths for creative browser applications. Browser compatibility, model memory and weight terms require device-specific review. [Source 1](https://github.com/mlc-ai/web-llm) [Source 2](https://github.com/mlc-ai/web-stable-diffusion) |
| WebXR, VR & AR | Nerfstudio and Open Reality are adjacent learned-scene components for XR experimentation, not newly verified headset applications. Existing XR guides remain in the original edition. [Source 1](https://github.com/nerfstudio-project/nerfstudio) [Source 2](https://github.com/reality-opened/openreality) |
| Computational art & creative coding | C/C++ diffusion runtimes, Diffusers, SVGRender and code-based agent workflows broaden custom generative systems beyond standalone image editors. [Source 1](https://github.com/leejet/stable-diffusion.cpp) [Source 2](https://github.com/ximinng/PyTorch-SVGRender) [Source 3](https://github.com/edenfunf/reelmimic) |
| Interactive, immersive & live media | RealtimeSTT/TTS and WebLLM can supply learned voice/language interaction to artist-built systems. Realtime latency and installation behavior are not independently tested. [Source 1](https://github.com/KoljaB/RealtimeSTT) [Source 2](https://github.com/KoljaB/RealtimeTTS) [Source 3](https://github.com/mlc-ai/web-llm) |
| 3D printing & generative CAD | CADAM is a screened AI-to-parametric-CAD lead; image-to-mesh tools offer proxies. STL export alone proves neither watertightness, fit nor printing readiness. [Source 1](https://github.com/Adam-CAD/CADAM) [Source 2](https://github.com/VAST-AI-Research/TripoSR) |
| Games & production pipelines | Mesh generators, text-to-motion models and the Generator Assets pipeline are relevant to game prototypes. Retopology, rigging, collision, scale and engine import remain downstream checks. [Source 1](https://github.com/VAST-AI-Research/TripoSR) [Source 2](https://github.com/EricGuo5513/momask-codes) [Source 3](https://github.com/laurentvv/generator-assets) |
| Motion capture & character animation | MotionGPT and MoMask support text-driven motion experiments; DWPose supplies whole-body conditions. Body-model/dataset licenses and retargeting need separate review. [Source 1](https://github.com/OpenMotionLab/MotionGPT) [Source 2](https://github.com/EricGuo5513/momask-codes) [Source 3](https://github.com/IDEA-Research/DWPose) |
| Avatars, digital humans & lip sync | LivePortrait and local voice tools add portrait and vocal performance routes. LivePortrait default InsightFace detector weights have non-commercial terms; commercial deployments must replace them. [Source 1](https://github.com/KlingTeam/LivePortrait) [Source 2](https://github.com/myshell-ai/OpenVoice) |
| VFX, compositing & relighting | SAM 2 masks, depth estimates and IC-Light relighting can become compositing inputs. IC-Light documents a non-commercial default background-removal component to replace for commercial use. [Source 1](https://github.com/facebookresearch/sam2) [Source 2](https://github.com/DepthAnything/Depth-Anything-V2) [Source 3](https://github.com/lllyasviel/IC-Light) |
| Spatial audio & volumetric media | Nerfstudio, gsplat and Open Reality connect learned capture with scene inspection. Open Reality distinguishes its simulator from actual reconstruction and relative units from calibrated metres. [Source 1](https://github.com/nerfstudio-project/nerfstudio) [Source 2](https://github.com/nerfstudio-project/gsplat) [Source 3](https://github.com/reality-opened/openreality) |
| Photogrammetry, scanning & neural rendering | Neural scene reconstruction and monocular depth are useful adjacent capture tools. A phone-video or depth-map result is not automatically accurate metric scanning. [Source 1](https://github.com/reality-opened/openreality) [Source 2](https://github.com/DepthAnything/Depth-Anything-V2) |
| Editing, captions & post-production | WhisperX word timing, SAM 2 masks, RIFE interpolation and BridgeClip editing cover distinct post-production tasks. Captions, occlusions and interpolated frames require manual review. [Source 1](https://github.com/m-bain/whisperX) [Source 2](https://github.com/facebookresearch/sam2) [Source 3](https://github.com/hzwer/ECCV2022-RIFE) [Source 4](https://github.com/bridge-mind/bridgeclip) |
| Vector graphics, illustration & textures | PyTorch-SVGRender and an agent logo-design extension add vector-specific experiments. Generated SVG paths may need substantial simplification and originality review. [Source 1](https://github.com/ximinng/PyTorch-SVGRender) [Source 2](https://github.com/kaankiziltug/logo-design-skill) |
| Typography, fonts & layout | SVGRender contains letterform-oriented research methods and the logo extension includes SVG/type workflows. No new turnkey, production-tested AI typeface system is claimed. [Source 1](https://github.com/ximinng/PyTorch-SVGRender) [Source 2](https://github.com/kaankiziltug/logo-design-skill) |
| Storyboarding, narrative & comics | Speech tools, ReelMimic reference analysis and motion-video agent templates can support narrative prototypes. Required agent accounts and rendering stacks remain separate from MIT source terms. [Source 1](https://github.com/myshell-ai/OpenVoice) [Source 2](https://github.com/edenfunf/reelmimic) [Source 3](https://github.com/echris6/motion-video-kit) |
| Creative publishing & presentation | PaddleOCR document extraction and BridgeClip captioned exports address searchable/editable material and short-form preparation. Automated publishing and API providers have separate terms. [Source 1](https://github.com/PaddlePaddle/PaddleOCR) [Source 2](https://github.com/bridge-mind/bridgeclip) |
| Photography, restoration & color | rembg, Upscayl, Real-ESRGAN and relighting tools add masking/restoration routes. AI detail is synthesized and should not be presented as recovered original information. [Source 1](https://github.com/danielgatis/rembg) [Source 2](https://github.com/upscayl/upscayl) [Source 3](https://github.com/xinntao/Real-ESRGAN) |
| Data art & scientific visualization | Depth maps, learned 3D scenes and document-layout extraction are useful source material for visualizations. No newly tested dedicated AI data-art application is established in this review. [Source 1](https://github.com/DepthAnything/Depth-Anything-V2) [Source 2](https://github.com/nerfstudio-project/nerfstudio) [Source 3](https://github.com/PaddlePaddle/PaddleOCR) |
| Physical, robotic & kinetic installations | Streaming speech and in-browser model inference can become components in interactive installations. Continuous operation, acoustics and device latency remain untested. [Source 1](https://github.com/KoljaB/RealtimeSTT) [Source 2](https://github.com/KoljaB/RealtimeTTS) [Source 3](https://github.com/mlc-ai/web-llm) |
| Performance, projection & stage media | RVC and MusicGen are relevant to voice/music experiments, subject to model terms. RAVE and nn_tilde are excluded because their current code licenses are non-commercial. [Source 1](https://github.com/RVC-Project/Retrieval-based-Voice-Conversion-WebUI) [Source 2](https://github.com/acids-ircam/RAVE/blob/master/LICENSE) [Source 3](https://github.com/acids-ircam/nn_tilde/blob/master/LICENSE) |
| Fashion, textiles & wearable media | Krita painting, neural cutouts and Mixar texture workflows are adjacent tools for fashion image and material exploration. Garment fitting, simulation and manufacturability are not verified. [Source 1](https://github.com/Acly/krita-ai-diffusion) [Source 2](https://github.com/danielgatis/rembg) [Source 3](https://github.com/Mixar-AI/mixar-app) |
| Accessible media & assistive creation | Whisper/WhisperX captions, text-to-speech and OCR can assist accessible creative drafts. Human correction is necessary; no compliance or universal language-accuracy claim is made. [Source 1](https://github.com/openai/whisper) [Source 2](https://github.com/m-bain/whisperX) [Source 3](https://github.com/PaddlePaddle/PaddleOCR) |
| Mobile, edge & on-device creation | stable-diffusion.cpp documents Android/Termux deployment. CPU-first speech and browser inference are adjacent possibilities, not verified phone applications or performance guarantees. [Source 1](https://github.com/leejet/stable-diffusion.cpp) [Source 2](https://github.com/KittenML/KittenTTS) [Source 3](https://github.com/mlc-ai/web-llm) |
| Creative learning & authoring | Supplied small datasets and example workflows offer reproducible learning starts: a Nerfstudio capture, a TripoSR object, or a short Whisper transcript. Nothing was installed in this documentation review. [Source 1](https://github.com/nerfstudio-project/nerfstudio) [Source 2](https://github.com/VAST-AI-Research/TripoSR) [Source 3](https://github.com/openai/whisper) |
| Archives, media restoration & collections | OCR and speech transcription help make archives searchable; restoration can alter evidence. Preserve original scans/photos/audio alongside derived material. [Source 1](https://github.com/PaddlePaddle/PaddleOCR) [Source 2](https://github.com/openai/whisper) [Source 3](https://github.com/xinntao/Real-ESRGAN) |
| Emerging & cross-disciplinary creative AI | Recent agent-assisted logo, motion-video and reference-animation projects extend the search to new authoring practices. Their open source is distinct from required external AI agents; custom-license LTX-2 remains excluded. [Source 1](https://github.com/kaankiziltug/logo-design-skill) [Source 2](https://github.com/echris6/motion-video-kit) [Source 3](https://github.com/edenfunf/reelmimic) [Source 4](https://github.com/Lightricks/LTX-2/blob/main/LICENSE-2_x) |

## Search and review counts

30 creative fields; 189/189 repository queries attempted; 13/13 model-task queries attempted. 17434 distinct source candidates and 609 model leads. 27 detailed profiles and 38 additional screened discoveries. Source gaps: 0 failed repository queries, 0 partial repository queries, 92 bounded repository queries, 0 failed model-task queries and 3 web ecosystem gaps. Raw search candidates include duplicates of known tools, excluded projects and projects awaiting review; they are not verified recommendations.

## Research beyond GitHub

- **gitlab** · gap: Live search identified the official GPG2A aerial-image diffusion release, but the source view did not expose complete documentation/license evidence in this session. It is not promoted as an eligible tool. [Source](https://gitlab.com/vail-uvm/GPG2A/-/tree/main)
- **codeberg** · gap: Live searches and source access were attempted, but source access was blocked and no complete primary documentation/license review was possible. No Codeberg project is promoted. 
- **sourcehut** · gap: Live searches/source access were attempted; robots/access restrictions prevented a complete primary-source review. No SourceHut project is promoted. 
- **packages** · searched: Read the current rembg package documentation and Python support range; followed package/source evidence for creator-oriented background removal. [Source](https://pypi.org/project/rembg/)
- **creative-plugins** · searched: Reviewed the official Krita AI installation and the Mixar Blender-fork overview, distinguishing local backend options from a required closed hosted AI service. [Source](https://docs.interstice.cloud/installation/) [Source](https://github.com/Mixar-AI/mixar-app)
- **project-sites** · searched: Read official Krita installation, Upscayl documentation and SVGRender project documentation alongside their actual source licenses. [Source](https://docs.interstice.cloud/installation/) [Source](https://docs.upscayl.org/introduction) [Source](https://pytorch-svgrender.readthedocs.io/en/latest/)
- **research-code** · searched: Read released image-to-3D, neural capture, motion and audio code/setup. Restricted software is excluded; non-commercial weights on otherwise open code are separately labeled. [Source](https://github.com/VAST-AI-Research/TripoSR) [Source](https://github.com/nerfstudio-project/nerfstudio) [Source](https://github.com/OpenMotionLab/MotionGPT) [Source](https://github.com/facebookresearch/audiocraft)
- **international** · searched: Reviewed Chinese-language RVC and BeefTV setup and multilingual source projects including CosyVoice/Qwen speech tools. Platform instructions and software terms were checked rather than inferred from English popularity. [Source](https://github.com/RVC-Project/Retrieval-based-Voice-Conversion-WebUI) [Source](https://github.com/glanderness/BeefTV) [Source](https://github.com/FunAudioLLM/CosyVoice) [Source](https://github.com/QwenLM/Qwen3-TTS)

## Collection limitations

- images: bounded or incomplete query: topic:diffusion pushed:>=2026-09-01 is:public fork:false archived:false (200 of 203 matches sampled)
- images: bounded or incomplete query: topic:diffusion is:public fork:false archived:false (200 of 1414 matches sampled)
- images: bounded or incomplete query: AI image generation pushed:>=2026-09-01 is:public fork:false archived:false (200 of 1633 matches sampled)
- images: bounded or incomplete query: AI image generation created:>=2026-09-01 is:public fork:false archived:false (200 of 832 matches sampled)
- images: bounded or incomplete query: AI image generation is:public fork:false archived:false (200 of 15252 matches sampled)
- video: bounded or incomplete query: AI video pushed:>=2026-09-01 is:public fork:false archived:false (200 of 12335 matches sampled)
- video: bounded or incomplete query: AI video created:>=2026-09-01 is:public fork:false archived:false (200 of 7838 matches sampled)
- video: bounded or incomplete query: AI video is:public fork:false archived:false (200 of 81647 matches sampled)
- video: bounded or incomplete query: topic:video-generation pushed:>=2026-09-01 is:public fork:false archived:false (200 of 1465 matches sampled)
- video: bounded or incomplete query: topic:video-generation created:>=2026-09-01 is:public fork:false archived:false (200 of 558 matches sampled)
- video: bounded or incomplete query: topic:video-generation is:public fork:false archived:false (200 of 3719 matches sampled)
- audio: bounded or incomplete query: topic:music-generation pushed:>=2026-09-01 is:public fork:false archived:false (200 of 286 matches sampled)
- audio: bounded or incomplete query: topic:music-generation is:public fork:false archived:false (200 of 1158 matches sampled)
- audio: bounded or incomplete query: AI audio pushed:>=2026-09-01 is:public fork:false archived:false (200 of 3752 matches sampled)
- audio: bounded or incomplete query: AI audio created:>=2026-09-01 is:public fork:false archived:false (200 of 2011 matches sampled)
- audio: bounded or incomplete query: AI audio is:public fork:false archived:false (200 of 27304 matches sampled)
- 3d: bounded or incomplete query: 3D generation pushed:>=2026-09-01 is:public fork:false archived:false (200 of 693 matches sampled)
- 3d: bounded or incomplete query: 3D generation created:>=2026-09-01 is:public fork:false archived:false (200 of 380 matches sampled)
- 3d: bounded or incomplete query: 3D generation is:public fork:false archived:false (200 of 5727 matches sampled)
- 3d: bounded or incomplete query: topic:3d-reconstruction pushed:>=2026-09-01 is:public fork:false archived:false (200 of 255 matches sampled)
- 3d: bounded or incomplete query: topic:3d-reconstruction is:public fork:false archived:false (200 of 1893 matches sampled)
- web: bounded or incomplete query: topic:webgpu pushed:>=2026-09-01 is:public fork:false archived:false (200 of 993 matches sampled)
- web: bounded or incomplete query: topic:webgpu created:>=2026-09-01 is:public fork:false archived:false (200 of 400 matches sampled)
- web: bounded or incomplete query: topic:webgpu is:public fork:false archived:false (200 of 2715 matches sampled)
- xr: bounded or incomplete query: AI VR pushed:>=2026-09-01 is:public fork:false archived:false (200 of 323 matches sampled)
- xr: bounded or incomplete query: AI VR is:public fork:false archived:false (200 of 2815 matches sampled)
- computational: bounded or incomplete query: AI creative coding is:public fork:false archived:false (200 of 902 matches sampled)
- computational: bounded or incomplete query: topic:generative-art pushed:>=2026-09-01 is:public fork:false archived:false (200 of 752 matches sampled)
- computational: bounded or incomplete query: topic:generative-art created:>=2026-09-01 is:public fork:false archived:false (200 of 353 matches sampled)
- computational: bounded or incomplete query: topic:generative-art is:public fork:false archived:false (200 of 3757 matches sampled)
- interactive: bounded or incomplete query: AI interactive art is:public fork:false archived:false (200 of 668 matches sampled)
- fabrication: bounded or incomplete query: AI CAD pushed:>=2026-09-01 is:public fork:false archived:false (200 of 665 matches sampled)
- fabrication: bounded or incomplete query: AI CAD created:>=2026-09-01 is:public fork:false archived:false (200 of 381 matches sampled)
- fabrication: bounded or incomplete query: AI CAD is:public fork:false archived:false (200 of 2939 matches sampled)
- fabrication: bounded or incomplete query: AI 3D printing is:public fork:false archived:false (200 of 335 matches sampled)
- gaming: bounded or incomplete query: AI game assets is:public fork:false archived:false (200 of 617 matches sampled)
- gaming: bounded or incomplete query: AI blender pushed:>=2026-09-01 is:public fork:false archived:false (200 of 398 matches sampled)
- gaming: bounded or incomplete query: AI blender created:>=2026-09-01 is:public fork:false archived:false (200 of 287 matches sampled)
- gaming: bounded or incomplete query: AI blender is:public fork:false archived:false (200 of 1485 matches sampled)
- motion: bounded or incomplete query: AI motion capture is:public fork:false archived:false (200 of 227 matches sampled)
- motion: bounded or incomplete query: motion generation is:public fork:false archived:false (200 of 1480 matches sampled)
- avatars: bounded or incomplete query: AI avatar pushed:>=2026-09-01 is:public fork:false archived:false (200 of 761 matches sampled)
- avatars: bounded or incomplete query: AI avatar created:>=2026-09-01 is:public fork:false archived:false (200 of 425 matches sampled)
- avatars: bounded or incomplete query: AI avatar is:public fork:false archived:false (200 of 5790 matches sampled)
- avatars: bounded or incomplete query: lip sync pushed:>=2026-09-01 is:public fork:false archived:false (200 of 274 matches sampled)
- avatars: bounded or incomplete query: lip sync is:public fork:false archived:false (200 of 2345 matches sampled)
- vfx: bounded or incomplete query: AI visual effects is:public fork:false archived:false (200 of 412 matches sampled)
- capture: bounded or incomplete query: topic:gaussian-splatting pushed:>=2026-09-01 is:public fork:false archived:false (200 of 234 matches sampled)
- capture: bounded or incomplete query: topic:gaussian-splatting is:public fork:false archived:false (200 of 889 matches sampled)
- capture: bounded or incomplete query: neural reconstruction is:public fork:false archived:false (200 of 1309 matches sampled)
- editing: bounded or incomplete query: AI video editing pushed:>=2026-09-01 is:public fork:false archived:false (200 of 789 matches sampled)
- editing: bounded or incomplete query: AI video editing created:>=2026-09-01 is:public fork:false archived:false (200 of 492 matches sampled)
- editing: bounded or incomplete query: AI video editing is:public fork:false archived:false (200 of 3301 matches sampled)
- editing: bounded or incomplete query: AI subtitle pushed:>=2026-09-01 is:public fork:false archived:false (200 of 359 matches sampled)
- editing: bounded or incomplete query: AI subtitle is:public fork:false archived:false (200 of 2172 matches sampled)
- vector: bounded or incomplete query: AI SVG pushed:>=2026-09-01 is:public fork:false archived:false (200 of 424 matches sampled)
- vector: bounded or incomplete query: AI SVG created:>=2026-09-01 is:public fork:false archived:false (200 of 233 matches sampled)
- vector: bounded or incomplete query: AI SVG is:public fork:false archived:false (200 of 1721 matches sampled)
- typography: bounded or incomplete query: AI typography is:public fork:false archived:false (200 of 630 matches sampled)
- typography: bounded or incomplete query: font generation is:public fork:false archived:false (200 of 413 matches sampled)
- storytelling: bounded or incomplete query: AI storyboard pushed:>=2026-09-01 is:public fork:false archived:false (200 of 354 matches sampled)
- storytelling: bounded or incomplete query: AI storyboard created:>=2026-09-01 is:public fork:false archived:false (200 of 201 matches sampled)
- storytelling: bounded or incomplete query: AI storyboard is:public fork:false archived:false (200 of 1619 matches sampled)
- storytelling: bounded or incomplete query: AI comic pushed:>=2026-09-01 is:public fork:false archived:false (200 of 1465 matches sampled)
- storytelling: bounded or incomplete query: AI comic created:>=2026-09-01 is:public fork:false archived:false (200 of 1385 matches sampled)
- storytelling: bounded or incomplete query: AI comic is:public fork:false archived:false (200 of 2716 matches sampled)
- publishing: bounded or incomplete query: AI presentation pushed:>=2026-09-01 is:public fork:false archived:false (200 of 1116 matches sampled)
- publishing: bounded or incomplete query: AI presentation created:>=2026-09-01 is:public fork:false archived:false (200 of 687 matches sampled)
- publishing: bounded or incomplete query: AI presentation is:public fork:false archived:false (200 of 8341 matches sampled)
- publishing: bounded or incomplete query: AI publishing pushed:>=2026-09-01 is:public fork:false archived:false (200 of 1060 matches sampled)
- publishing: bounded or incomplete query: AI publishing created:>=2026-09-01 is:public fork:false archived:false (200 of 661 matches sampled)
- publishing: bounded or incomplete query: AI publishing is:public fork:false archived:false (200 of 3931 matches sampled)
- photography: bounded or incomplete query: AI colorization pushed:>=2026-09-01 is:public fork:false archived:false (200 of 440 matches sampled)
- photography: bounded or incomplete query: AI colorization created:>=2026-09-01 is:public fork:false archived:false (200 of 277 matches sampled)
- photography: bounded or incomplete query: AI colorization is:public fork:false archived:false (200 of 4662 matches sampled)
- visualization: bounded or incomplete query: AI visualization pushed:>=2026-09-01 is:public fork:false archived:false (200 of 3294 matches sampled)
- visualization: bounded or incomplete query: AI visualization created:>=2026-09-01 is:public fork:false archived:false (200 of 1920 matches sampled)
- visualization: bounded or incomplete query: AI visualization is:public fork:false archived:false (200 of 37297 matches sampled)
- visualization: bounded or incomplete query: AI data art is:public fork:false archived:false (200 of 1010 matches sampled)
- performance: bounded or incomplete query: AI live visuals is:public fork:false archived:false (200 of 694 matches sampled)
- fashion: bounded or incomplete query: AI fashion design is:public fork:false archived:false (200 of 632 matches sampled)
- fashion: bounded or incomplete query: AI textile is:public fork:false archived:false (200 of 459 matches sampled)
- accessibility: bounded or incomplete query: AI audio description is:public fork:false archived:false (200 of 251 matches sampled)
- mobile: bounded or incomplete query: AI mobile media is:public fork:false archived:false (200 of 205 matches sampled)
- education: bounded or incomplete query: AI explainer pushed:>=2026-09-01 is:public fork:false archived:false (200 of 6550 matches sampled)
- education: bounded or incomplete query: AI explainer created:>=2026-09-01 is:public fork:false archived:false (200 of 4569 matches sampled)
- education: bounded or incomplete query: AI explainer is:public fork:false archived:false (200 of 35971 matches sampled)
- frontier: bounded or incomplete query: AI creative tools pushed:>=2026-09-01 is:public fork:false archived:false (200 of 234 matches sampled)
- frontier: bounded or incomplete query: AI creative tools is:public fork:false archived:false (200 of 1924 matches sampled)
- frontier: bounded or incomplete query: AI digital art is:public fork:false archived:false (200 of 711 matches sampled)
- frontier: bounded or incomplete query: AI multimedia is:public fork:false archived:false (200 of 1157 matches sampled)
- frontier: bounded or incomplete query: AI new media is:public fork:false archived:false (200 of 500 matches sampled)

## BeefTV

Video, animation & film · Images & design · Audio, music & voice · Storyboarding, narrative & comics · Browser tools & web media

Repository created 2026-09-24. New to this library; young-project claims still need hands-on validation.

### How it uses AI

A local project canvas for AI media generation, organization and iterative editing. Creative use: Connecting references, generated images, clips, audio and storyboards within one reusable project. [Source](https://github.com/glanderness/BeefTV)

### Introduction

A local project canvas for AI media generation, organization and iterative editing. [Source 1](https://github.com/glanderness/BeefTV)

### What it is good for

Connecting references, generated images, clips, audio and storyboards within one reusable project. [Source 1](https://github.com/glanderness/BeefTV)

### Demo & examples

The README provides a product video and canvas examples; the release download links a demonstration video. [Source 1](https://github.com/glanderness/BeefTV) [Source 2](https://github.com/glanderness/BeefTV/blob/main/QUICKSTART.md)

### Install

Documented installation route; commands below are reference text and were not executed. [Source 1](https://github.com/glanderness/BeefTV/blob/main/QUICKSTART.md) [Source 2](https://github.com/glanderness/BeefTV)

1. Download the official macOS or Windows desktop release.
2. Follow QUICKSTART.md for installation and first launch; configure a supported model channel.
3. Create a small canvas project and add your own source media.
### First project

Suggested first project, based on the documented controls; an untested trial plan. [Source 1](https://github.com/glanderness/BeefTV)

1. My suggested trial: create three storyboard nodes and connect their references.
2. Generate or import one result, then revise only that node.
3. Save the project and check whether all needed assets remain available locally.
### Hardware & software

Configuration-specific requirements; missing minimums are stated explicitly. [Source 1](https://github.com/glanderness/BeefTV/blob/main/QUICKSTART.md) [Source 2](https://github.com/glanderness/BeefTV)

- **Hardware:** The local workspace does not imply local model inference. RAM, VRAM and storage minimums are not documented in the reviewed README; requirements depend on the chosen model channel.
- **Software:** Official macOS/Windows desktop package and configured model-provider access. Source builds require Go 1.25, Bun and Wails platform components.
- **Platforms:** macOS and Windows desktop downloads are documented. Native Linux release support is not established in the reviewed overview.

### License, model weights & costs

Reviewed MIT project software; model and service terms are separate. [Source 1](https://github.com/glanderness/BeefTV/blob/main/LICENSE) [Source 2](https://github.com/glanderness/BeefTV)

- **Code:** MIT
- **Weights:** Each configured model/provider has separate terms; the MIT workspace does not license those models.
- **Commercial:** Software terms reviewed; permission for a complete commercial deployment depends on the chosen models and dependencies and is not fully verified.
- **Cost:** Local storage plus any required model-provider charges; no current price claim.

### Why it merits attention

Assessment: a visible canvas/demo and editable asset relationships distinguish it from a bare API wrapper. Documentation reviewed; no desktop package run. [Source 1](https://github.com/glanderness/BeefTV)

### Limitations

Very young project. The current Mac app is not Apple signed/notarized; follow the official first-launch guidance. Local project storage is distinct from external model inference. [Source 1](https://github.com/glanderness/BeefTV)

### Get the tool

- [Repository](https://github.com/glanderness/BeefTV)
- [Documentation](https://github.com/glanderness/BeefTV/blob/main/QUICKSTART.md)
- [Download](https://github.com/glanderness/BeefTV/releases)

## YuE2 Studio

Audio, music & voice · Performance, projection & stage media · Storyboarding, narrative & comics

Repository created 2026-09-22. New to this library; young-project claims still need hands-on validation.

### How it uses AI

A Windows song-generation studio with an editable score and local YuE2 inference. Creative use: Song sketches with lyrics, melodies and score edits that can be rendered again. [Source](https://github.com/timoncool/YuE2-Studio)

### Introduction

A Windows song-generation studio with an editable score and local YuE2 inference. [Source 1](https://github.com/timoncool/YuE2-Studio)

### What it is good for

Song sketches with lyrics, melodies and score edits that can be rendered again. [Source 1](https://github.com/timoncool/YuE2-Studio)

### Demo & examples

The README and project page show the score, player and generation interface; developer speed claims were not reproduced. [Source 1](https://github.com/timoncool/YuE2-Studio) [Source 2](https://timoncool.github.io/YuE2-Studio/)

### Install

Documented installation route; commands below are reference text and were not executed. [Source 1](https://timoncool.github.io/YuE2-Studio/) [Source 2](https://github.com/timoncool/YuE2-Studio)

1. Download the official Windows x64 installer or portable release.
2. Follow first-launch instructions to obtain a compatible YuE2 model set.
3. Select the GPU backend and verify the model terms before generation.
### First project

Suggested first project, based on the documented controls; an untested trial plan. [Source 1](https://github.com/timoncool/YuE2-Studio)

1. My suggested trial: write a short style brief and a small lyric segment.
2. Generate a draft, then change one score or tempo element and render again.
3. Compare phrasing and keep the score, seed and model settings with the audio.
### Hardware & software

Configuration-specific requirements; missing minimums are stated explicitly. [Source 1](https://timoncool.github.io/YuE2-Studio/) [Source 2](https://github.com/timoncool/YuE2-Studio)

- **Hardware:** NVIDIA 6 GB+ VRAM; AMD/Intel Vulkan is experimental. One model set uses about 4–10 GB disk. Optional LoRA training needs RTX 30-series or newer with 11 GB VRAM and extra storage. RAM minimum is not documented.
- **Software:** Windows release bundles a Rust/React/Tauri application with yue2.cpp; the runtime does not require Python or Node. Model files are separate.
- **Platforms:** Windows 10/11 x64; Microsoft Edge WebView2 is required and may be installed on first launch. macOS/Linux releases are not documented.

### License, model weights & costs

MIT studio; bundled components include AGPL-3.0 visualization, Apache-2.0 score code and GPL-2.0 SoundFonts. Model permissions are narrower. [Source 1](https://github.com/timoncool/YuE2-Studio/blob/main/LICENSE) [Source 2](https://github.com/timoncool/YuE2-Studio) [Source 3](https://github.com/multimodal-art-projection/YuE/blob/main/MODEL_LICENSE)

- **Code:** MIT
- **Weights:** YuE2 backbone/VAE: CC-BY-NC-4.0 plus a conditional individual-creator permission. SheetSage2 and decoder companion remain CC-BY-NC without that exception.
- **Commercial:** The upstream terms permit individuals to monetize generated outputs under responsible-use conditions, while company commercial model use needs a separate license. That exception does not license every companion model.
- **Cost:** Local compute and storage; optional external services have separate charges. Current prices are not verified.

### Why it merits attention

Assessment: score editing makes the creative control more concrete than a single music prompt. Documentation reviewed; no song rendered. [Source 1](https://github.com/timoncool/YuE2-Studio)

### Limitations

Young project; non-NVIDIA paths are experimental. Commercial permission for the selected weight set is not verified here. [Source 1](https://github.com/timoncool/YuE2-Studio)

### Get the tool

- [Repository](https://github.com/timoncool/YuE2-Studio)
- [Documentation](https://timoncool.github.io/YuE2-Studio/)
- [Download](https://github.com/timoncool/YuE2-Studio/releases)

## BridgeClip

Video, animation & film · Editing, captions & post-production · Creative publishing & presentation · Accessible media & assistive creation

Repository created 2026-09-24. New to this library; young-project claims still need hands-on validation.

### How it uses AI

A desktop clip editor that combines transcript-based AI selection with local video rendering. Creative use: Finding and refining short clips from interviews, streams and podcasts, with captions and framing. [Source](https://github.com/bridge-mind/bridgeclip)

### Introduction

A desktop clip editor that combines transcript-based AI selection with local video rendering. [Source 1](https://github.com/bridge-mind/bridgeclip)

### What it is good for

Finding and refining short clips from interviews, streams and podcasts, with captions and framing. [Source 1](https://github.com/bridge-mind/bridgeclip)

### Demo & examples

The README shows the candidate/edit/export workflow and caption previews; no clip was processed here. [Source 1](https://github.com/bridge-mind/bridgeclip) [Source 2](https://github.com/bridge-mind/bridgeclip/blob/main/docs/usage.md)

### Install

Documented installation route; commands below are reference text and were not executed. [Source 1](https://github.com/bridge-mind/bridgeclip/blob/main/docs/usage.md) [Source 2](https://github.com/bridge-mind/bridgeclip)

1. Download the official package matching your operating system and architecture.
2. Install it; packaged releases include Python, FFmpeg and yt-dlp.
3. Provide your own OpenRouter key with credit, then add a local video for a small trial.
### First project

Suggested first project, based on the documented controls; an untested trial plan. [Source 1](https://github.com/bridge-mind/bridgeclip)

1. My suggested trial: use a short interview file in Review & edit.
2. Check that a proposed clip preserves context, then correct cuts, framing and captions.
3. Export one clip and review it fully before publishing.
### Hardware & software

Configuration-specific requirements; missing minimums are stated explicitly. [Source 1](https://github.com/bridge-mind/bridgeclip/blob/main/docs/usage.md) [Source 2](https://github.com/bridge-mind/bridgeclip)

- **Hardware:** Rendering is local; AI processing uses OpenRouter. Universal RAM/VRAM/storage minimums are not documented in the reviewed overview.
- **Software:** Release bundles Python, FFmpeg and yt-dlp. A funded OpenRouter API key is required; Linux needs an unlocked desktop secret service for key storage.
- **Platforms:** macOS Apple Silicon/Intel, Windows x64 and Linux x64 DEB/AppImage are documented.

### License, model weights & costs

Reviewed MIT project software; model and service terms are separate. [Source 1](https://github.com/bridge-mind/bridgeclip/blob/main/LICENSE) [Source 2](https://github.com/bridge-mind/bridgeclip)

- **Code:** MIT
- **Weights:** AI models run through OpenRouter/provider terms; MIT desktop code does not make those services open source.
- **Commercial:** MIT code permits commercial use subject to notices; AI-provider and source-video terms are independent.
- **Cost:** OpenRouter credits plus local rendering/storage; optional publishing integrations have separate terms.

### Why it merits attention

Assessment: synchronized editing, captions and local rendering are substantial creative functions. Documentation reviewed; no install or API call. [Source 1](https://github.com/bridge-mind/bridgeclip)

### Limitations

Requires funded OpenRouter access. The guide limits supported linked sources to six hours/20 GB and excludes live/private Twitch material. Source features can differ from a downloaded release. [Source 1](https://github.com/bridge-mind/bridgeclip)

### Get the tool

- [Repository](https://github.com/bridge-mind/bridgeclip)
- [Documentation](https://github.com/bridge-mind/bridgeclip/blob/main/docs/usage.md)
- [Download](https://github.com/bridge-mind/bridgeclip/releases)

## Krita AI Diffusion

Images & design · Editing, captions & post-production · Photography, restoration & color · Fashion, textiles & wearable media

First detailed review in this library. An established baseline newly covered by the expanded search, not a claim that it launched or significantly changed today.

### How it uses AI

A painting plugin that brings diffusion generation, inpainting and image guidance into Krita. Creative use: Concept painting, masked retouching, sketch-guided variations and extending a canvas while retaining editable layers. [Source](https://github.com/Acly/krita-ai-diffusion)

### Introduction

A painting plugin that brings diffusion generation, inpainting and image guidance into Krita. [Source 1](https://github.com/Acly/krita-ai-diffusion)

### What it is good for

Concept painting, masked retouching, sketch-guided variations and extending a canvas while retaining editable layers. [Source 1](https://github.com/Acly/krita-ai-diffusion)

### Demo & examples

The official installation guide and repository contain illustrated painting workflows; no example was run here. [Source 1](https://github.com/Acly/krita-ai-diffusion) [Source 2](https://docs.interstice.cloud/installation/)

### Install

Documented installation route; commands below are reference text and were not executed. [Source 1](https://docs.interstice.cloud/installation/) [Source 2](https://github.com/Acly/krita-ai-diffusion)

1. Install Krita 5.2 or newer; check the plugin version compatible with your Krita major release.
2. Download the official plugin ZIP; use Tools → Scripts → Import Python Plugin, then restart Krita.
3. Enable the AI Image Generation docker, open Configure and choose managed local ComfyUI or an existing server.
### First project

Suggested first project, based on the documented controls; an untested trial plan. [Source 1](https://github.com/Acly/krita-ai-diffusion)

1. My suggested trial: duplicate a small sketch layer and select one region.
2. Generate a variation from that selection and a short description; retain the original layer.
3. Compare edges and brush character before accepting the generated layer.
### Hardware & software

Configuration-specific requirements; missing minimums are stated explicitly. [Source 1](https://docs.interstice.cloud/installation/) [Source 2](https://github.com/Acly/krita-ai-diffusion)

- **Hardware:** Local NVIDIA: at least 6 GB VRAM recommended. AMD ROCm and Intel Arc/XPU paths are documented. Storage: at least 10 GB; many packages can exceed 50 GB. System RAM minimum is not documented.
- **Software:** Krita 5.2+; a compatible plugin and ComfyUI backend. Managed setup downloads models. Apple Silicon MPS requires macOS 14+ in the documented local route.
- **Platforms:** Windows, Linux and macOS have documented routes. CPU-only inference is very slow. Online generation is an optional alternative.

### License, model weights & costs

Reviewed GPL-3.0 project software; model and service terms are separate. [Source 1](https://github.com/Acly/krita-ai-diffusion/blob/main/LICENSE) [Source 2](https://github.com/Acly/krita-ai-diffusion)

- **Code:** GPL-3.0
- **Weights:** Each diffusion checkpoint, LoRA and auxiliary model retains its own terms.
- **Commercial:** Software terms reviewed; permission for a complete commercial deployment depends on the chosen models and dependencies and is not fully verified.
- **Cost:** Local compute and model storage; optional paid online service.

### Why it merits attention

Assessment: its selection and layer integration makes a small, reversible painting trial practical. Documentation reviewed; no installation or output test. [Source 1](https://github.com/Acly/krita-ai-diffusion)

### Limitations

Backend/model compatibility matters. Generated detail can change the painting; published examples are developer demonstrations. [Source 1](https://github.com/Acly/krita-ai-diffusion)

### Get the tool

- [Repository](https://github.com/Acly/krita-ai-diffusion)
- [Documentation](https://docs.interstice.cloud/installation/)
- [Download](https://github.com/Acly/krita-ai-diffusion/releases)

## Stability Matrix

Images & design · Video, animation & film · Audio, music & voice · Editing, captions & post-production

First detailed review in this library. An established baseline newly covered by the expanded search, not a claim that it launched or significantly changed today.

### How it uses AI

A desktop package and model manager with a built-in diffusion inference interface. Creative use: Managing several creative AI backends and sharing downloaded checkpoints without rebuilding each environment manually. [Source](https://github.com/LykosAI/StabilityMatrix)

### Introduction

A desktop package and model manager with a built-in diffusion inference interface. [Source 1](https://github.com/LykosAI/StabilityMatrix)

### What it is good for

Managing several creative AI backends and sharing downloaded checkpoints without rebuilding each environment manually. [Source 1](https://github.com/LykosAI/StabilityMatrix)

### Demo & examples

The repository shows the package manager and inference UI; the first-image guide gives a concrete ComfyUI-backed workflow. [Source 1](https://github.com/LykosAI/StabilityMatrix) [Source 2](https://github.com/LykosAI/StabilityMatrix/blob/main/docs/inference/text-to-image.md)

### Install

Documented installation route; commands below are reference text and were not executed. [Source 1](https://github.com/LykosAI/StabilityMatrix/blob/main/docs/inference/text-to-image.md) [Source 2](https://github.com/LykosAI/StabilityMatrix)

1. Download the release matching Windows, Linux or Apple Silicon macOS.
2. Choose a data folder with room for environments and models; install a supported backend such as ComfyUI.
3. Import a compatible full checkpoint and select the backend in Inference.
### First project

Suggested first project, based on the documented controls; an untested trial plan. [Source 1](https://github.com/LykosAI/StabilityMatrix)

1. My suggested trial: select one full checkpoint and generate a single small image.
2. Keep high-resolution fixes and extra modules off until the basic backend works.
3. Save the image and its settings, then change only the prompt for comparison.
### Hardware & software

Configuration-specific requirements; missing minimums are stated explicitly. [Source 1](https://github.com/LykosAI/StabilityMatrix/blob/main/docs/inference/text-to-image.md) [Source 2](https://github.com/LykosAI/StabilityMatrix)

- **Hardware:** Requirements depend on the installed backend and model. A universal CPU, RAM, VRAM or storage minimum is not documented.
- **Software:** Release packages embed Git and Python; installed backends add their own dependencies and checkpoints.
- **Platforms:** Windows, Linux and Apple Silicon macOS releases are documented; individual packages may support fewer platforms.

### License, model weights & costs

Reviewed AGPL-3.0 project software; model and service terms are separate. [Source 1](https://github.com/LykosAI/StabilityMatrix/blob/main/LICENSE) [Source 2](https://github.com/LykosAI/StabilityMatrix)

- **Code:** AGPL-3.0
- **Weights:** Downloaded models and backend packages retain independent licenses.
- **Commercial:** Software terms reviewed; permission for a complete commercial deployment depends on the chosen models and dependencies and is not fully verified.
- **Cost:** Local hardware, storage and any separately selected services.

### Why it merits attention

Assessment: useful environment organization and a documented first-image path. Documentation reviewed; no backend installed. [Source 1](https://github.com/LykosAI/StabilityMatrix)

### Limitations

A manager cannot make an unsupported backend or model work on every device. Troubleshoot the selected package first. [Source 1](https://github.com/LykosAI/StabilityMatrix)

### Get the tool

- [Repository](https://github.com/LykosAI/StabilityMatrix)
- [Documentation](https://github.com/LykosAI/StabilityMatrix/blob/main/docs/inference/text-to-image.md)
- [Download](https://github.com/LykosAI/StabilityMatrix/releases)

## SwarmUI

Images & design · Video, animation & film · Audio, music & voice · Browser tools & web media

First detailed review in this library. An established baseline newly covered by the expanded search, not a claim that it launched or significantly changed today.

### How it uses AI

A modular browser interface for diffusion backends and multimodal generation. Creative use: A shared generation workstation, advanced image controls and image/video/audio experiments around supported backends. [Source](https://github.com/mcmonkeyprojects/SwarmUI)

### Introduction

A modular browser interface for diffusion backends and multimodal generation. [Source 1](https://github.com/mcmonkeyprojects/SwarmUI)

### What it is good for

A shared generation workstation, advanced image controls and image/video/audio experiments around supported backends. [Source 1](https://github.com/mcmonkeyprojects/SwarmUI)

### Demo & examples

The README links screenshots, tutorials and the project documentation; the current source identifies a beta release. [Source 1](https://github.com/mcmonkeyprojects/SwarmUI)

### Install

Documented installation route; commands below are reference text and were not executed. [Source 1](https://github.com/mcmonkeyprojects/SwarmUI)

1. Use the official Windows installer or the Linux source-install guide linked in the repository.
2. Follow the platform prerequisites and choose a supported backend during first-run setup.
3. Download a compatible model, start the local server and open its printed address.
### First project

Suggested first project, based on the documented controls; an untested trial plan. [Source 1](https://github.com/mcmonkeyprojects/SwarmUI)

1. My suggested trial: choose one image backend and its matching model.
2. Generate a small batch, inspect the history and save one result.
3. Try video or audio only after the corresponding backend and model requirements are checked.
### Hardware & software

Configuration-specific requirements; missing minimums are stated explicitly. [Source 1](https://github.com/mcmonkeyprojects/SwarmUI)

- **Hardware:** RAM, VRAM and storage depend on the backend and model; a universal minimum is not documented.
- **Software:** Windows automated route targets Windows 11; manual setup uses Git and a suitable .NET SDK. Linux guide recommends Python 3.11/3.12 for common backends.
- **Platforms:** Windows and Linux setup is documented. A browser frontend alone does not establish native macOS backend support; a remote GPU server is an alternative.

### License, model weights & costs

Reviewed MIT project software; model and service terms are separate. [Source 1](https://github.com/mcmonkeyprojects/SwarmUI/blob/master/LICENSE.txt) [Source 2](https://github.com/mcmonkeyprojects/SwarmUI)

- **Code:** MIT
- **Weights:** Each selected model and backend has separate terms.
- **Commercial:** Software terms reviewed; permission for a complete commercial deployment depends on the chosen models and dependencies and is not fully verified.
- **Cost:** Local compute and storage; optional external services have separate charges. Current prices are not verified.

### Why it merits attention

Assessment: modular backends and visible generation history support repeatable creative experiments. Documentation reviewed; no server run. [Source 1](https://github.com/mcmonkeyprojects/SwarmUI)

### Limitations

Beta interface and backend compatibility can change. Do not assume every model supports every control. [Source 1](https://github.com/mcmonkeyprojects/SwarmUI)

### Get the tool

- [Repository](https://github.com/mcmonkeyprojects/SwarmUI)
- [Documentation](https://github.com/mcmonkeyprojects/SwarmUI)
- [Download](https://github.com/mcmonkeyprojects/SwarmUI/releases)

## stable-diffusion.cpp

Images & design · Video, animation & film · Mobile, edge & on-device creation · Computational art & creative coding

First detailed review in this library. An established baseline newly covered by the expanded search, not a claim that it launched or significantly changed today.

### How it uses AI

A C/C++ inference runtime for diffusion models, including quantized model workflows. Creative use: Building local image/video generation into scripts and experimenting with CPU, Vulkan or Metal hardware paths. [Source](https://github.com/leejet/stable-diffusion.cpp)

### Introduction

A C/C++ inference runtime for diffusion models, including quantized model workflows. [Source 1](https://github.com/leejet/stable-diffusion.cpp)

### What it is good for

Building local image/video generation into scripts and experimenting with CPU, Vulkan or Metal hardware paths. [Source 1](https://github.com/leejet/stable-diffusion.cpp)

### Demo & examples

The repository provides generated examples and a CLI quick start; these are developer examples, not our benchmarks. [Source 1](https://github.com/leejet/stable-diffusion.cpp) [Source 2](https://github.com/leejet/stable-diffusion.cpp/blob/master/docs/build.md)

### Install

Documented installation route; commands below are reference text and were not executed. [Source 1](https://github.com/leejet/stable-diffusion.cpp/blob/master/docs/build.md) [Source 2](https://github.com/leejet/stable-diffusion.cpp)

1. Download the matching official binary or build from source with CMake and the chosen hardware backend.
2. Obtain a model supported by that build and separately check its license.
3. Use the documented CLI with the model path and a short prompt.

```sh
./bin/sd-cli -m ../models/v1-5-pruned-emaonly.safetensors -p "a lovely cat"
```

### First project

Suggested first project, based on the documented controls; an untested trial plan. [Source 1](https://github.com/leejet/stable-diffusion.cpp)

1. My suggested trial: keep the model and seed fixed and render two short prompts.
2. Compare speed and artifacts before changing quantization, tiling or resolution.
3. Keep the model filename and runtime version with the output.
### Hardware & software

Configuration-specific requirements; missing minimums are stated explicitly. [Source 1](https://github.com/leejet/stable-diffusion.cpp/blob/master/docs/build.md) [Source 2](https://github.com/leejet/stable-diffusion.cpp)

- **Hardware:** CPU, CUDA, Vulkan, Metal, OpenCL and SYCL paths are documented. RAM/VRAM and storage depend on model, quantization and resolution; no universal minimum is published.
- **Software:** A compatible model file; CMake/toolchain if building. Backend-specific drivers and SDKs apply.
- **Platforms:** Windows, Linux, macOS and Android/Termux routes are documented; check individual backend support.

### License, model weights & costs

Reviewed MIT project software; model and service terms are separate. [Source 1](https://github.com/leejet/stable-diffusion.cpp/blob/master/LICENSE) [Source 2](https://github.com/leejet/stable-diffusion.cpp)

- **Code:** MIT
- **Weights:** The MIT runtime does not license downloaded diffusion checkpoints.
- **Commercial:** Software terms reviewed; permission for a complete commercial deployment depends on the chosen models and dependencies and is not fully verified.
- **Cost:** Local compute and storage; optional external services have separate charges. Current prices are not verified.

### Why it merits attention

Assessment: explicit backend choices make this useful for portable creative experiments. Documentation reviewed; no binary run. [Source 1](https://github.com/leejet/stable-diffusion.cpp)

### Limitations

Model support varies by build; quantization and tiling can affect results. Cross-backend performance has not been tested here. [Source 1](https://github.com/leejet/stable-diffusion.cpp)

### Get the tool

- [Repository](https://github.com/leejet/stable-diffusion.cpp)
- [Documentation](https://github.com/leejet/stable-diffusion.cpp/blob/master/docs/build.md)
- [Download](https://github.com/leejet/stable-diffusion.cpp/releases)

## Upscayl

Images & design · Photography, restoration & color · Archives, media restoration & collections

First detailed review in this library. An established baseline newly covered by the expanded search, not a claim that it launched or significantly changed today.

### How it uses AI

A desktop application for neural image enlargement. Creative use: Preparing small illustrations and photographs for layouts or larger digital presentation. [Source](https://github.com/upscayl/upscayl)

### Introduction

A desktop application for neural image enlargement. [Source 1](https://github.com/upscayl/upscayl)

### What it is good for

Preparing small illustrations and photographs for layouts or larger digital presentation. [Source 1](https://github.com/upscayl/upscayl)

### Demo & examples

The README includes interface examples and comparisons; the official documentation describes the workflow. [Source 1](https://github.com/upscayl/upscayl) [Source 2](https://docs.upscayl.org/introduction)

### Install

Documented installation route; commands below are reference text and were not executed. [Source 1](https://docs.upscayl.org/introduction) [Source 2](https://github.com/upscayl/upscayl)

1. Download the official release for your operating system.
2. Install or open the platform package and check GPU compatibility.
3. Choose a small test image, an upscaling model and an output folder.
### First project

Suggested first project, based on the documented controls; an untested trial plan. [Source 1](https://github.com/upscayl/upscayl)

1. My suggested trial: enlarge a copy of a small photograph.
2. Compare faces, fine text and edges at 100% against the original.
3. Keep the source alongside the upscale; use the result only when the added detail helps.
### Hardware & software

Configuration-specific requirements; missing minimums are stated explicitly. [Source 1](https://docs.upscayl.org/introduction) [Source 2](https://github.com/upscayl/upscayl)

- **Hardware:** A compatible Vulkan GPU is the normal desktop route. A universal RAM/VRAM or storage minimum is not documented in the reviewed setup.
- **Software:** Official platform package and compatible graphics drivers; included and custom models have separate terms.
- **Platforms:** Linux, Windows 10+ and macOS 12+ are documented. GPU/backend compatibility still applies.

### License, model weights & costs

Reviewed AGPL-3.0 project software; model and service terms are separate. [Source 1](https://github.com/upscayl/upscayl/blob/main/LICENSE) [Source 2](https://github.com/upscayl/upscayl)

- **Code:** AGPL-3.0
- **Weights:** Check the particular upscaler model; AGPL software terms do not cover all external weights.
- **Commercial:** Software terms reviewed; permission for a complete commercial deployment depends on the chosen models and dependencies and is not fully verified.
- **Cost:** Local compute and storage; optional external services have separate charges. Current prices are not verified.

### Why it merits attention

Assessment: an approachable native interface for comparison-based enlargement. Documentation reviewed; no image processed. [Source 1](https://github.com/upscayl/upscayl)

### Limitations

Upscaling synthesizes detail and may distort faces or lettering. CPU workarounds do not establish universal CPU support. [Source 1](https://github.com/upscayl/upscayl)

### Get the tool

- [Repository](https://github.com/upscayl/upscayl)
- [Documentation](https://docs.upscayl.org/introduction)
- [Download](https://github.com/upscayl/upscayl/releases)

## chaiNNer

Images & design · Video, animation & film · Computational art & creative coding · Editing, captions & post-production

First detailed review in this library. An established baseline newly covered by the expanded search, not a claim that it launched or significantly changed today.

### How it uses AI

A node-based desktop image-processing application with neural model inference. Creative use: Batch upscaling and reusable processing chains that combine AI models with ordinary image operations. [Source](https://github.com/chaiNNer-org/chaiNNer)

### Introduction

A node-based desktop image-processing application with neural model inference. [Source 1](https://github.com/chaiNNer-org/chaiNNer)

### What it is good for

Batch upscaling and reusable processing chains that combine AI models with ordinary image operations. [Source 1](https://github.com/chaiNNer-org/chaiNNer)

### Demo & examples

The README shows node graphs and describes model/runtime compatibility; no live output was tested. [Source 1](https://github.com/chaiNNer-org/chaiNNer)

### Install

Documented installation route; commands below are reference text and were not executed. [Source 1](https://github.com/chaiNNer-org/chaiNNer)

1. Download the official desktop release for your platform.
2. Select an inference package compatible with your GPU or CPU and obtain a supported model.
3. Build a minimal chain with an image loader, model loader, upscale operation and image saver.
### First project

Suggested first project, based on the documented controls; an untested trial plan. [Source 1](https://github.com/chaiNNer-org/chaiNNer)

1. My suggested trial: run one small input through the simplest chain.
2. Compare the saved result, then add a batch loader for copies of several inputs.
3. Keep the graph with the models and test tiles when memory is limited.
### Hardware & software

Configuration-specific requirements; missing minimums are stated explicitly. [Source 1](https://github.com/chaiNNer-org/chaiNNer)

- **Hardware:** NVIDIA/CUDA, AMD ROCm or NCNN, Intel NCNN and CPU routes vary by runtime. Apple Silicon can use PyTorch MPS; ONNX there is CPU-only. Universal RAM/VRAM/storage minimums are not documented.
- **Software:** Desktop release, selected inference dependencies and a supported model architecture.
- **Platforms:** Windows, Linux and macOS routes are documented; Windows 8.1 and below and macOS 10.x are unsupported.

### License, model weights & costs

Reviewed GPL-3.0 project software; model and service terms are separate. [Source 1](https://github.com/chaiNNer-org/chaiNNer/blob/main/LICENSE) [Source 2](https://github.com/chaiNNer-org/chaiNNer)

- **Code:** GPL-3.0
- **Weights:** External model checkpoints retain their own licenses.
- **Commercial:** Software terms reviewed; permission for a complete commercial deployment depends on the chosen models and dependencies and is not fully verified.
- **Cost:** Local compute and storage; optional external services have separate charges. Current prices are not verified.

### Why it merits attention

Assessment: saved node graphs suit repeatable batch creative work. Documentation reviewed; no graph executed. [Source 1](https://github.com/chaiNNer-org/chaiNNer)

### Limitations

Unsupported architectures and low-memory settings can fail or introduce artifacts; compatibility must be checked per runtime. [Source 1](https://github.com/chaiNNer-org/chaiNNer)

### Get the tool

- [Repository](https://github.com/chaiNNer-org/chaiNNer)
- [Documentation](https://github.com/chaiNNer-org/chaiNNer)
- [Download](https://github.com/chaiNNer-org/chaiNNer/releases)

## rembg

Images & design · Photography, restoration & color · Fashion, textiles & wearable media · Editing, captions & post-production

First detailed review in this library. An established baseline newly covered by the expanded search, not a claim that it launched or significantly changed today.

### How it uses AI

A Python library and CLI for AI background removal. Creative use: Cutout preparation for product photographs, collages, fashion layouts and compositing. [Source](https://github.com/danielgatis/rembg)

### Introduction

A Python library and CLI for AI background removal. [Source 1](https://github.com/danielgatis/rembg)

### What it is good for

Cutout preparation for product photographs, collages, fashion layouts and compositing. [Source 1](https://github.com/danielgatis/rembg)

### Demo & examples

The README contains input/output examples and CLI usage; no cutout was generated here. [Source 1](https://github.com/danielgatis/rembg) [Source 2](https://pypi.org/project/rembg/)

### Install

Documented installation route; commands below are reference text and were not executed. [Source 1](https://pypi.org/project/rembg/) [Source 2](https://github.com/danielgatis/rembg)

1. Create a Python environment in the documented supported version range.
2. Install the CPU/CLI extras first; choose GPU extras only after checking the ONNX runtime requirements.
3. Run the image command on a copy of one file.

```sh
pip install "rembg[cpu,cli]"
```


```sh
rembg i input.png output.png
```

### First project

Suggested first project, based on the documented controls; an untested trial plan. [Source 1](https://github.com/danielgatis/rembg)

1. My suggested trial: use a photograph with hair, transparent edges or a complex background.
2. Inspect the alpha boundary over both light and dark backgrounds.
3. Retouch the mask manually if the cutout is intended for final artwork.
### Hardware & software

Configuration-specific requirements; missing minimums are stated explicitly. [Source 1](https://pypi.org/project/rembg/) [Source 2](https://github.com/danielgatis/rembg)

- **Hardware:** CPU ONNX inference is supported. NVIDIA CUDA and AMD ROCm routes need compatible runtimes; RAM, VRAM and storage minimums are not documented.
- **Software:** Current documentation: Python >=3.11,<3.14; ONNX Runtime and selected model downloads.
- **Platforms:** Use supported Python/ONNX environments. The reviewed package does not publish a complete certified OS/version matrix.

### License, model weights & costs

Reviewed MIT project software; model and service terms are separate. [Source 1](https://github.com/danielgatis/rembg/blob/main/LICENSE.txt) [Source 2](https://github.com/danielgatis/rembg)

- **Code:** MIT
- **Weights:** Each downloaded segmentation model has independent terms; optional hosted APIs are separate.
- **Commercial:** Software terms reviewed; permission for a complete commercial deployment depends on the chosen models and dependencies and is not fully verified.
- **Cost:** Local compute and storage; optional external services have separate charges. Current prices are not verified.

### Why it merits attention

Assessment: a small scriptable first task and reusable batch interface. Documentation reviewed; no segmentation test. [Source 1](https://github.com/danielgatis/rembg)

### Limitations

Fine hair, transparency and unusual objects can need manual masking. GPU installation is runtime-specific. [Source 1](https://github.com/danielgatis/rembg)

### Get the tool

- [Repository](https://github.com/danielgatis/rembg)
- [Documentation](https://pypi.org/project/rembg/)
- [Download](https://github.com/danielgatis/rembg/releases)

## Whisper

Audio, music & voice · Video, animation & film · Accessible media & assistive creation · Creative publishing & presentation · Archives, media restoration & collections

First detailed review in this library. An established baseline newly covered by the expanded search, not a claim that it launched or significantly changed today.

### How it uses AI

A speech-recognition model and CLI for transcription, translation and language identification. Creative use: Draft transcripts, subtitles and searchable spoken-word archives. [Source](https://github.com/openai/whisper)

### Introduction

A speech-recognition model and CLI for transcription, translation and language identification. [Source 1](https://github.com/openai/whisper)

### What it is good for

Draft transcripts, subtitles and searchable spoken-word archives. [Source 1](https://github.com/openai/whisper)

### Demo & examples

The repository supplies CLI and Python examples; no recording was transcribed here. [Source 1](https://github.com/openai/whisper)

### Install

Documented installation route; commands below are reference text and were not executed. [Source 1](https://github.com/openai/whisper)

1. Install the package in a compatible Python environment.
2. Install FFmpeg using the documented route for your operating system.
3. Choose a model size that fits your device and first test a short recording.

```sh
pip install -U openai-whisper
```


```sh
whisper audio.wav --model turbo
```

### First project

Suggested first project, based on the documented controls; an untested trial plan. [Source 1](https://github.com/openai/whisper)

1. My suggested trial: transcribe a one-minute clip with clearly audible speech.
2. Proofread names, punctuation and silence segments against the audio.
3. Use the subtitle outputs as drafts and check timing before publication.
### Hardware & software

Configuration-specific requirements; missing minimums are stated explicitly. [Source 1](https://github.com/openai/whisper)

- **Hardware:** Approximate documented GPU memory: tiny/base 1 GB, small 2 GB, medium 5 GB, large 10 GB, turbo 6 GB. These are model-specific estimates; CPU is possible. RAM and total storage minimums are not documented.
- **Software:** FFmpeg and PyTorch; README expects compatibility with Python 3.8–3.11 rather than establishing a new universal requirement.
- **Platforms:** Windows, Linux and macOS FFmpeg/setup paths are documented; performance depends on the inference device.

### License, model weights & costs

Reviewed MIT project software; model and service terms are separate. [Source 1](https://github.com/openai/whisper/blob/main/LICENSE) [Source 2](https://github.com/openai/whisper)

- **Code:** MIT
- **Weights:** The repository states code and model weights are MIT licensed.
- **Commercial:** MIT permits commercial software use subject to its notices; transcription output still needs accuracy and content-rights review.
- **Cost:** Local compute and storage; optional external services have separate charges. Current prices are not verified.

### Why it merits attention

Assessment: explicit model sizes and multiple subtitle outputs make a controlled captioning trial practical. Documentation reviewed; no accuracy benchmark. [Source 1](https://github.com/openai/whisper)

### Limitations

Recognition can hallucinate or mishear, especially around noise and silence; turbo is not the translation-oriented model. [Source 1](https://github.com/openai/whisper)

### Get the tool

- [Repository](https://github.com/openai/whisper)
- [Documentation](https://github.com/openai/whisper)
- [Download](https://github.com/openai/whisper/releases)

## WhisperX

Audio, music & voice · Video, animation & film · Accessible media & assistive creation · Editing, captions & post-production

First detailed review in this library. An established baseline newly covered by the expanded search, not a claim that it launched or significantly changed today.

### How it uses AI

A transcription pipeline that adds word alignment and optional speaker diarization. Creative use: Word-timed caption drafts and multi-speaker editing transcripts. [Source](https://github.com/m-bain/whisperX)

### Introduction

A transcription pipeline that adds word alignment and optional speaker diarization. [Source 1](https://github.com/m-bain/whisperX)

### What it is good for

Word-timed caption drafts and multi-speaker editing transcripts. [Source 1](https://github.com/m-bain/whisperX)

### Demo & examples

The README includes timed transcription examples and command-line usage; no alignment was tested. [Source 1](https://github.com/m-bain/whisperX)

### Install

Documented installation route; commands below are reference text and were not executed. [Source 1](https://github.com/m-bain/whisperX)

1. Install WhisperX in an isolated Python environment.
2. For GPU inference follow the documented CUDA 12.8 setup; CPU is a separate supported route.
3. Enable optional diarization only after checking and accepting the selected gated model terms.

```sh
pip install whisperx
```


```sh
whisperx path/to/audio.wav --compute_type int8 --device cpu
```

### First project

Suggested first project, based on the documented controls; an untested trial plan. [Source 1](https://github.com/m-bain/whisperX)

1. My suggested trial: transcribe a short interview with two known speakers.
2. Compare word boundaries and speaker changes against playback.
3. Correct names and timing before exporting subtitles or edit notes.
### Hardware & software

Configuration-specific requirements; missing minimums are stated explicitly. [Source 1](https://github.com/m-bain/whisperX)

- **Hardware:** The project reports under 8 GB GPU memory for a particular large-v2/beam-5 setup, not a universal minimum. CPU is available; RAM and storage minimums are not documented.
- **Software:** Python environment, inference/alignment models and CUDA 12.8 for the documented GPU path. Optional pyannote diarization may require gated Hugging Face access.
- **Platforms:** CPU usage explicitly includes macOS; NVIDIA GPU setup needs compatible CUDA. A complete OS/version certification matrix is not published.

### License, model weights & costs

Reviewed BSD-2-Clause project software; model and service terms are separate. [Source 1](https://github.com/m-bain/whisperX/blob/main/LICENSE) [Source 2](https://github.com/m-bain/whisperX)

- **Code:** BSD-2-Clause
- **Weights:** Whisper, alignment and diarization weights each retain their own terms; gated access is separate from the BSD-2-Clause code.
- **Commercial:** Software terms reviewed; permission for a complete commercial deployment depends on the chosen models and dependencies and is not fully verified.
- **Cost:** Local compute and storage; optional external services have separate charges. Current prices are not verified.

### Why it merits attention

Assessment: word-level alignment is useful for caption editing beyond plain transcript generation. Documentation reviewed; no recording processed. [Source 1](https://github.com/m-bain/whisperX)

### Limitations

Overlap and alignment errors require manual review. Diarization setup adds model access and dependencies. [Source 1](https://github.com/m-bain/whisperX)

### Get the tool

- [Repository](https://github.com/m-bain/whisperX)
- [Documentation](https://github.com/m-bain/whisperX)
- [Download](https://github.com/m-bain/whisperX/releases)

## Chatterbox

Audio, music & voice · Storyboarding, narrative & comics · Games & production pipelines · Accessible media & assistive creation

First detailed review in this library. An established baseline newly covered by the expanded search, not a claim that it launched or significantly changed today.

### How it uses AI

A local text-to-speech family with expressive speech and reference-voice conditioning. Creative use: Narration drafts, character-voice prototypes and short interactive voice responses. [Source](https://github.com/resemble-ai/chatterbox)

### Introduction

A local text-to-speech family with expressive speech and reference-voice conditioning. [Source 1](https://github.com/resemble-ai/chatterbox)

### What it is good for

Narration drafts, character-voice prototypes and short interactive voice responses. [Source 1](https://github.com/resemble-ai/chatterbox)

### Demo & examples

The README links sample audio and Python examples; samples are developer demonstrations. [Source 1](https://github.com/resemble-ai/chatterbox)

### Install

Documented installation route; commands below are reference text and were not executed. [Source 1](https://github.com/resemble-ai/chatterbox)

1. Use an isolated environment; the project reports testing Python 3.11 on Debian 11.
2. Install chatterbox-tts and select the documented example for the desired model variant.
3. Choose a supported inference device and let that variant download its models.

```sh
pip install chatterbox-tts
```

### First project

Suggested first project, based on the documented controls; an untested trial plan. [Source 1](https://github.com/resemble-ai/chatterbox)

1. My suggested trial: render a short narration in the default example.
2. Adjust one expression or voice-reference setting and listen for pronunciation changes.
3. Review the complete recording before using it in a prototype.
### Hardware & software

Configuration-specific requirements; missing minimums are stated explicitly. [Source 1](https://github.com/resemble-ai/chatterbox)

- **Hardware:** CUDA, CPU and MPS examples are present; variant and input length change memory needs. Universal RAM/VRAM/storage minimums are not documented.
- **Software:** Python 3.11 is the tested setup; package dependencies and model files are variant-specific.
- **Platforms:** Debian is the published test environment; CPU/MPS examples do not establish a complete Windows/macOS version support matrix.

### License, model weights & costs

Reviewed MIT project software; model and service terms are separate. [Source 1](https://github.com/resemble-ai/chatterbox/blob/master/LICENSE) [Source 2](https://github.com/resemble-ai/chatterbox)

- **Code:** MIT
- **Weights:** Check the selected Chatterbox variant and checkpoint terms separately; the reviewed repository code is MIT.
- **Commercial:** Software terms reviewed; permission for a complete commercial deployment depends on the chosen models and dependencies and is not fully verified.
- **Cost:** Local compute and storage; optional external services have separate charges. Current prices are not verified.

### Why it merits attention

Assessment: reference conditioning and explicit model variants offer useful narration experiments. Documentation reviewed; no synthesis run. [Source 1](https://github.com/resemble-ai/chatterbox)

### Limitations

Voice similarity and pronunciation are not guaranteed. A reference voice must be appropriate for the intended use. [Source 1](https://github.com/resemble-ai/chatterbox)

### Get the tool

- [Repository](https://github.com/resemble-ai/chatterbox)
- [Documentation](https://github.com/resemble-ai/chatterbox)
- [Download](https://github.com/resemble-ai/chatterbox/releases)

## KittenTTS

Audio, music & voice · Interactive, immersive & live media · Mobile, edge & on-device creation · Accessible media & assistive creation

First detailed review in this library. An established baseline newly covered by the expanded search, not a claim that it launched or significantly changed today.

### How it uses AI

A compact ONNX text-to-speech toolkit designed for CPU inference. Creative use: Short local narration and voices for lightweight interactive prototypes. [Source](https://github.com/KittenML/KittenTTS)

### Introduction

A compact ONNX text-to-speech toolkit designed for CPU inference. [Source 1](https://github.com/KittenML/KittenTTS)

### What it is good for

Short local narration and voices for lightweight interactive prototypes. [Source 1](https://github.com/KittenML/KittenTTS)

### Demo & examples

The repository includes example usage and voice samples; we did not synthesize them. [Source 1](https://github.com/KittenML/KittenTTS)

### Install

Documented installation route; commands below are reference text and were not executed. [Source 1](https://github.com/KittenML/KittenTTS)

1. Use Python 3.8 or newer with an isolated environment.
2. Install the documented 0.8.1 package wheel, then select a matching model.
3. Run the README Python example with one of its named voices and save the audio.

```sh
pip install https://github.com/KittenML/KittenTTS/releases/download/0.8.1/kittentts-0.8.1-py3-none-any.whl
```

### First project

Suggested first project, based on the documented controls; an untested trial plan. [Source 1](https://github.com/KittenML/KittenTTS)

1. My suggested trial: generate one short sentence with Jasper and then Bella.
2. Listen for articulation and adjust speed conservatively.
3. Keep the model and voice names with the saved narration.
### Hardware & software

Configuration-specific requirements; missing minimums are stated explicitly. [Source 1](https://github.com/KittenML/KittenTTS)

- **Hardware:** CPU inference requires no GPU. Documented models span roughly 15M–80M parameters and 25–80 MB of model files; that excludes environment size. RAM minimum is not documented.
- **Software:** Python >=3.8, ONNX Runtime and a matching model; optional GPU dependencies are separate.
- **Platforms:** Linux, macOS and Windows are documented; no mobile package/device certification is established here.

### License, model weights & costs

Reviewed Apache-2.0 project software; model and service terms are separate. [Source 1](https://github.com/KittenML/KittenTTS/blob/main/LICENSE) [Source 2](https://github.com/KittenML/KittenTTS)

- **Code:** Apache-2.0
- **Weights:** Confirm the exact downloaded checkpoint terms independently of the Apache-2.0 package.
- **Commercial:** Software terms reviewed; permission for a complete commercial deployment depends on the chosen models and dependencies and is not fully verified.
- **Cost:** Local compute and storage; optional external services have separate charges. Current prices are not verified.

### Why it merits attention

Assessment: CPU-first setup is useful when a discrete GPU is unavailable. Documentation reviewed; no latency or quality benchmark. [Source 1](https://github.com/KittenML/KittenTTS)

### Limitations

Compact size is not proof of production speech quality. Pronunciation and long-form narration need listening tests. [Source 1](https://github.com/KittenML/KittenTTS)

### Get the tool

- [Repository](https://github.com/KittenML/KittenTTS)
- [Documentation](https://github.com/KittenML/KittenTTS)
- [Download](https://github.com/KittenML/KittenTTS/releases)

## TripoSR

3D, reconstruction & assets · Games & production pipelines · 3D printing & generative CAD

First detailed review in this library. An established baseline newly covered by the expanded search, not a claim that it launched or significantly changed today.

### How it uses AI

An image-to-3D reconstruction release that turns a single picture into a mesh. Creative use: Rapid object proxies and early game or visualization asset blockouts. [Source](https://github.com/VAST-AI-Research/TripoSR)

### Introduction

An image-to-3D reconstruction release that turns a single picture into a mesh. [Source 1](https://github.com/VAST-AI-Research/TripoSR)

### What it is good for

Rapid object proxies and early game or visualization asset blockouts. [Source 1](https://github.com/VAST-AI-Research/TripoSR)

### Demo & examples

The README links a public Gradio demo and supplied chair example; neither was executed here. [Source 1](https://github.com/VAST-AI-Research/TripoSR)

### Install

Documented installation route; commands below are reference text and were not executed. [Source 1](https://github.com/VAST-AI-Research/TripoSR)

1. Create a Python >=3.8 environment and install PyTorch matching the intended CUDA version.
2. Clone the official repository and install requirements.txt, including the mesh dependency.
3. Run the supplied example first or launch gradio_app.py.

```sh
python run.py examples/chair.png --output-dir output/
```


```sh
python gradio_app.py
```

### First project

Suggested first project, based on the documented controls; an untested trial plan. [Source 1](https://github.com/VAST-AI-Research/TripoSR)

1. My suggested trial: use one isolated object with a simple silhouette.
2. Open the exported mesh in your DCC tool and inspect hidden surfaces.
3. Check scale, normals and topology before adapting it for a game or fabrication.
### Hardware & software

Configuration-specific requirements; missing minimums are stated explicitly. [Source 1](https://github.com/VAST-AI-Research/TripoSR)

- **Hardware:** The default single-image path is documented at about 6 GB VRAM. RAM and storage minimums are not documented; CPU-related fallback notes are not a general performance guarantee.
- **Software:** Python >=3.8, PyTorch, matching CUDA and requirements.txt; torchmcubes setup can require a compatible build environment.
- **Platforms:** Documented setup centers on PyTorch/CUDA. Complete Windows/macOS support and version minimums are not established by the reviewed guide.

### License, model weights & costs

Reviewed MIT project software; model and service terms are separate. [Source 1](https://github.com/VAST-AI-Research/TripoSR/blob/main/LICENSE) [Source 2](https://github.com/VAST-AI-Research/TripoSR)

- **Code:** MIT
- **Weights:** The developers expressly release code, pretrained models and the interactive demo under MIT.
- **Commercial:** MIT permits commercial use subject to notices; input-image rights and downstream asset checks still apply.
- **Cost:** Local compute and storage; optional external services have separate charges. Current prices are not verified.

### Why it merits attention

Assessment: supplied examples and a simple image-to-mesh entry point make it a useful prototype candidate. Documentation reviewed; no reconstruction or print test. [Source 1](https://github.com/VAST-AI-Research/TripoSR)

### Limitations

A plausible mesh is not necessarily watertight, dimensionally accurate or print-ready. [Source 1](https://github.com/VAST-AI-Research/TripoSR)

### Get the tool

- [Repository](https://github.com/VAST-AI-Research/TripoSR)
- [Documentation](https://github.com/VAST-AI-Research/TripoSR)
- [Download](https://github.com/VAST-AI-Research/TripoSR/releases)

## Segment Anything 2 (SAM 2)

Images & design · Video, animation & film · VFX, compositing & relighting · Editing, captions & post-production · Photogrammetry, scanning & neural rendering

First detailed review in this library. An established baseline newly covered by the expanded search, not a claim that it launched or significantly changed today.

### How it uses AI

A promptable AI segmentation model for images and tracked video masks. Creative use: Rotoscoping starts, object isolation and mask preparation for compositing. [Source](https://github.com/facebookresearch/sam2)

### Introduction

A promptable AI segmentation model for images and tracked video masks. [Source 1](https://github.com/facebookresearch/sam2)

### What it is good for

Rotoscoping starts, object isolation and mask preparation for compositing. [Source 1](https://github.com/facebookresearch/sam2)

### Demo & examples

The repository links image/video notebooks, Colab examples and an official interactive demo. [Source 1](https://github.com/facebookresearch/sam2)

### Install

Documented installation route; commands below are reference text and were not executed. [Source 1](https://github.com/facebookresearch/sam2)

1. Use Python >=3.10 with PyTorch >=2.5.1 and torchvision >=0.20.1.
2. Install the repository package and download a matching SAM 2 checkpoint.
3. Add notebook dependencies if needed and start with a supplied image or video notebook.
### First project

Suggested first project, based on the documented controls; an untested trial plan. [Source 1](https://github.com/facebookresearch/sam2)

1. My suggested trial: select one object with a point prompt in a short clip.
2. Inspect the resulting masks frame by frame at occlusions.
3. Refine prompts before taking masks into a compositor.
### Hardware & software

Configuration-specific requirements; missing minimums are stated explicitly. [Source 1](https://github.com/facebookresearch/sam2)

- **Hardware:** CUDA extension builds need a compatible NVIDIA toolchain; some main inference works without optional postprocessing. RAM/VRAM/storage minimums are not documented.
- **Software:** Python >=3.10, PyTorch >=2.5.1, torchvision >=0.20.1 and checkpoint files; nvcc for the optional CUDA extension.
- **Platforms:** Linux-style setup; Windows users are advised to use WSL/Ubuntu. Native macOS support is not verified in the reviewed instructions.

### License, model weights & costs

Reviewed Apache-2.0 project software; model and service terms are separate. [Source 1](https://github.com/facebookresearch/sam2/blob/main/LICENSE) [Source 2](https://github.com/facebookresearch/sam2)

- **Code:** Apache-2.0
- **Weights:** The repository states Apache-2.0 for SAM 2 code and checkpoints; dependency and example-asset terms remain separate.
- **Commercial:** Software terms reviewed; permission for a complete commercial deployment depends on the chosen models and dependencies and is not fully verified.
- **Cost:** Local compute and storage; optional external services have separate charges. Current prices are not verified.

### Why it merits attention

Assessment: promptable video masks connect directly to editorial and VFX preparation. Documentation reviewed; no mask-quality test. [Source 1](https://github.com/facebookresearch/sam2)

### Limitations

Tracking can need correction after occlusion or object changes. Published benchmark results were not reproduced here. [Source 1](https://github.com/facebookresearch/sam2)

### Get the tool

- [Repository](https://github.com/facebookresearch/sam2)
- [Documentation](https://github.com/facebookresearch/sam2)
- [Download](https://github.com/facebookresearch/sam2/releases)

## Depth Anything V2

VFX, compositing & relighting · Spatial audio & volumetric media · Photography, restoration & color · Photogrammetry, scanning & neural rendering

First detailed review in this library. An established baseline newly covered by the expanded search, not a claim that it launched or significantly changed today.

### How it uses AI

A monocular AI depth-estimation toolkit. Creative use: Depth-reference passes for compositing, parallax experiments and generation controls. [Source](https://github.com/DepthAnything/Depth-Anything-V2)

### Introduction

A monocular AI depth-estimation toolkit. [Source 1](https://github.com/DepthAnything/Depth-Anything-V2)

### What it is good for

Depth-reference passes for compositing, parallax experiments and generation controls. [Source 1](https://github.com/DepthAnything/Depth-Anything-V2)

### Demo & examples

The README includes example depth maps and a Gradio app; no output was generated here. [Source 1](https://github.com/DepthAnything/Depth-Anything-V2)

### Install

Documented installation route; commands below are reference text and were not executed. [Source 1](https://github.com/DepthAnything/Depth-Anything-V2)

1. Clone the official repository and install its requirements.
2. Choose and download the Small checkpoint if an Apache-2.0 weight license is needed.
3. Use the vits encoder with that checkpoint, or start the supplied Gradio app.

```sh
python run.py --encoder vits --img-path assets/examples --outdir depth_vis
```


```sh
python app.py
```

### First project

Suggested first project, based on the documented controls; an untested trial plan. [Source 1](https://github.com/DepthAnything/Depth-Anything-V2)

1. My suggested trial: derive depth from a photograph with foreground and background layers.
2. Compare the relative ordering against the original, especially reflections and thin structures.
3. Use the map as an artistic control reference rather than a measured scan.
### Hardware & software

Configuration-specific requirements; missing minimums are stated explicitly. [Source 1](https://github.com/DepthAnything/Depth-Anything-V2)

- **Hardware:** CUDA, Apple MPS and CPU device selection are documented. RAM, VRAM and storage minimums are not documented.
- **Software:** Python/PyTorch dependencies in requirements.txt and a matching encoder/checkpoint. Exact Python minimum is not stated in the reviewed setup.
- **Platforms:** CUDA, MPS and CPU routes are shown; this does not establish a complete OS/version compatibility matrix.

### License, model weights & costs

Reviewed Apache-2.0 project software; model and service terms are separate. [Source 1](https://github.com/DepthAnything/Depth-Anything-V2/blob/main/LICENSE) [Source 2](https://github.com/DepthAnything/Depth-Anything-V2)

- **Code:** Apache-2.0
- **Weights:** Small: Apache-2.0. Base, Large and Giant: CC-BY-NC-4.0, according to the README.
- **Commercial:** Apache-2.0 code and Small weights allow commercial use subject to terms; larger published checkpoints are non-commercial.
- **Cost:** Local compute and storage; optional external services have separate charges. Current prices are not verified.

### Why it merits attention

Assessment: an explicit lightweight license option and documented device selection support a useful depth-pass trial. Documentation reviewed; no accuracy test. [Source 1](https://github.com/DepthAnything/Depth-Anything-V2)

### Limitations

Relative depth can be wrong and is not calibrated measurement. Larger model terms differ from Small. [Source 1](https://github.com/DepthAnything/Depth-Anything-V2)

### Get the tool

- [Repository](https://github.com/DepthAnything/Depth-Anything-V2)
- [Documentation](https://github.com/DepthAnything/Depth-Anything-V2)
- [Download](https://github.com/DepthAnything/Depth-Anything-V2/releases)

## Nerfstudio

3D, reconstruction & assets · Spatial audio & volumetric media · Photogrammetry, scanning & neural rendering · WebXR, VR & AR

First detailed review in this library. An established baseline newly covered by the expanded search, not a claim that it launched or significantly changed today.

### How it uses AI

A modular studio for neural radiance-field training, viewing and export. Creative use: Turning captured photographs into explorable scenes and novel camera views for spatial-media experiments. [Source](https://github.com/nerfstudio-project/nerfstudio)

### Introduction

A modular studio for neural radiance-field training, viewing and export. [Source 1](https://github.com/nerfstudio-project/nerfstudio)

### What it is good for

Turning captured photographs into explorable scenes and novel camera views for spatial-media experiments. [Source 1](https://github.com/nerfstudio-project/nerfstudio)

### Demo & examples

The repository links interactive viewers and the provided poster dataset workflow. [Source 1](https://github.com/nerfstudio-project/nerfstudio)

### Install

Documented installation route; commands below are reference text and were not executed. [Source 1](https://github.com/nerfstudio-project/nerfstudio)

1. Follow the NVIDIA/CUDA and PyTorch prerequisites, including tiny-cuda-nn where required.
2. Install Nerfstudio and download the small official poster dataset.
3. Train the nerfacto example and open the viewer URL printed by the process.

```sh
pip install nerfstudio
```


```sh
ns-download-data nerfstudio --capture-name=poster
```


```sh
ns-train nerfacto --data data/nerfstudio/poster
```

### First project

Suggested first project, based on the documented controls; an untested trial plan. [Source 1](https://github.com/nerfstudio-project/nerfstudio)

1. My suggested trial: inspect the supplied capture before using your own images.
2. Move the virtual camera within the observed views and inspect floaters or missing surfaces.
3. Capture a small static object with consistent lighting for a second trial.
### Hardware & software

Configuration-specific requirements; missing minimums are stated explicitly. [Source 1](https://github.com/nerfstudio-project/nerfstudio)

- **Hardware:** The documented training setup uses NVIDIA CUDA. Memory and storage scale with method and capture; universal RAM/VRAM/storage minimums are not documented.
- **Software:** Python >=3.8; the guide gives CUDA 11.7/11.8 and PyTorch 2.1.2/cu118 setup examples. Methods add their own build dependencies.
- **Platforms:** The CUDA training guide is not native macOS support. The browser viewer may run separately from a compatible GPU training host.

### License, model weights & costs

Reviewed Apache-2.0 project software; model and service terms are separate. [Source 1](https://github.com/nerfstudio-project/nerfstudio/blob/main/LICENSE) [Source 2](https://github.com/nerfstudio-project/nerfstudio)

- **Code:** Apache-2.0
- **Weights:** Methods, pretrained components and captured datasets retain their own terms.
- **Commercial:** Software terms reviewed; permission for a complete commercial deployment depends on the chosen models and dependencies and is not fully verified.
- **Cost:** Local compute and storage; optional external services have separate charges. Current prices are not verified.

### Why it merits attention

Assessment: a small supplied dataset and visible training/viewer loop make results inspectable. Documentation reviewed; no scene trained. [Source 1](https://github.com/nerfstudio-project/nerfstudio)

### Limitations

Capture coverage, motion and lighting affect reconstruction. A neural scene is not automatically a watertight fabrication mesh. [Source 1](https://github.com/nerfstudio-project/nerfstudio)

### Get the tool

- [Repository](https://github.com/nerfstudio-project/nerfstudio)
- [Documentation](https://github.com/nerfstudio-project/nerfstudio)
- [Download](https://github.com/nerfstudio-project/nerfstudio/releases)

## Real-ESRGAN

Images & design · Video, animation & film · Archives, media restoration & collections · Photography, restoration & color

First detailed review in this library. An established baseline newly covered by the expanded search, not a claim that it launched or significantly changed today.

### How it uses AI

A neural image and video restoration toolkit with upscaling models. Creative use: Preparing low-resolution creative assets and testing restoration on archival material. [Source](https://github.com/xinntao/Real-ESRGAN)

### Introduction

A neural image and video restoration toolkit with upscaling models. [Source 1](https://github.com/xinntao/Real-ESRGAN)

### What it is good for

Preparing low-resolution creative assets and testing restoration on archival material. [Source 1](https://github.com/xinntao/Real-ESRGAN)

### Demo & examples

The README provides restoration comparisons, sample inputs and portable/Python routes. [Source 1](https://github.com/xinntao/Real-ESRGAN)

### Install

Documented installation route; commands below are reference text and were not executed. [Source 1](https://github.com/xinntao/Real-ESRGAN)

1. For Python, use Python >=3.7 and PyTorch >=1.7 and follow the official dependency instructions.
2. Install BasicSR and the listed dependencies, then the repository package.
3. Use a documented model and start with a copied input; the portable NCNN route has different capabilities.

```sh
python inference_realesrgan.py -n RealESRGAN_x4plus -i inputs
```

### First project

Suggested first project, based on the documented controls; an untested trial plan. [Source 1](https://github.com/xinntao/Real-ESRGAN)

1. My suggested trial: compare a small illustration and a photograph separately.
2. Inspect text, skin and repeated textures at full resolution.
3. Keep the original and avoid treating invented detail as recovered evidence.
### Hardware & software

Configuration-specific requirements; missing minimums are stated explicitly. [Source 1](https://github.com/xinntao/Real-ESRGAN)

- **Hardware:** Python inference depends on its model/runtime; tiling is supported. RAM/VRAM/storage minimums are not documented. The separate NCNN binary route avoids a CUDA/PyTorch environment.
- **Software:** Python >=3.7, PyTorch >=1.7, BasicSR and requirements.txt for the Python path; optional face enhancement adds GFPGAN.
- **Platforms:** The repository documents Python and portable Windows/Linux/macOS alternatives. Verify the chosen binary and GPU backend; these were not tested here.

### License, model weights & costs

Reviewed BSD-3-Clause project software; model and service terms are separate. [Source 1](https://github.com/xinntao/Real-ESRGAN/blob/master/LICENSE) [Source 2](https://github.com/xinntao/Real-ESRGAN)

- **Code:** BSD-3-Clause
- **Weights:** Code is BSD-3-Clause; model checkpoints and optional GFPGAN dependencies need separate terms checks.
- **Commercial:** Software terms reviewed; permission for a complete commercial deployment depends on the chosen models and dependencies and is not fully verified.
- **Cost:** Local compute and storage; optional external services have separate charges. Current prices are not verified.

### Why it merits attention

Assessment: visible comparisons, tiling and multiple inference routes make this useful for controlled restoration experiments. Documentation reviewed; no restoration benchmark. [Source 1](https://github.com/xinntao/Real-ESRGAN)

### Limitations

Synthesized detail, tile inconsistencies and face changes can harm faithful restoration. [Source 1](https://github.com/xinntao/Real-ESRGAN)

### Get the tool

- [Repository](https://github.com/xinntao/Real-ESRGAN)
- [Documentation](https://github.com/xinntao/Real-ESRGAN)
- [Download](https://github.com/xinntao/Real-ESRGAN/releases)

## RIFE

Video, animation & film · Editing, captions & post-production · VFX, compositing & relighting

First detailed review in this library. An established baseline newly covered by the expanded search, not a claim that it launched or significantly changed today.

### How it uses AI

A neural frame-interpolation toolkit that estimates intermediate frames. Creative use: Slow-motion experiments and converting footage to a higher frame rate. [Source](https://github.com/hzwer/ECCV2022-RIFE)

### Introduction

A neural frame-interpolation toolkit that estimates intermediate frames. [Source 1](https://github.com/hzwer/ECCV2022-RIFE)

### What it is good for

Slow-motion experiments and converting footage to a higher frame rate. [Source 1](https://github.com/hzwer/ECCV2022-RIFE)

### Demo & examples

The repository links video examples and command-line inference instructions. [Source 1](https://github.com/hzwer/ECCV2022-RIFE)

### Install

Documented installation route; commands below are reference text and were not executed. [Source 1](https://github.com/hzwer/ECCV2022-RIFE)

1. Clone the official repository and install requirements.txt in a compatible PyTorch environment.
2. Download the documented HD model into train_log.
3. Run the supplied video command on a copy of a short clip.

```sh
python3 inference_video.py --exp=1 --video=video.mp4
```

### First project

Suggested first project, based on the documented controls; an untested trial plan. [Source 1](https://github.com/hzwer/ECCV2022-RIFE)

1. My suggested trial: interpolate a short clip with both simple motion and an occlusion.
2. Inspect the inserted frames at cuts and crossing edges.
3. Compare timing and motion character before using it in an edit.
### Hardware & software

Configuration-specific requirements; missing minimums are stated explicitly. [Source 1](https://github.com/hzwer/ECCV2022-RIFE)

- **Hardware:** Developer GPU speed examples are configuration-specific, not minimums. RAM, VRAM and storage minimums are not documented.
- **Software:** Python/PyTorch requirements and HD model files; exact universal version requirements are not established in the reviewed guide.
- **Platforms:** Main setup is Python/PyTorch-oriented. A referenced Mac contribution does not certify native Mac support; the separate NCNN implementation is another route.

### License, model weights & costs

Reviewed MIT project software; model and service terms are separate. [Source 1](https://github.com/hzwer/ECCV2022-RIFE/blob/main/LICENSE) [Source 2](https://github.com/hzwer/ECCV2022-RIFE)

- **Code:** MIT
- **Weights:** Check the downloaded RIFE checkpoint terms separately from MIT code.
- **Commercial:** Software terms reviewed; permission for a complete commercial deployment depends on the chosen models and dependencies and is not fully verified.
- **Cost:** Local compute and storage; optional external services have separate charges. Current prices are not verified.

### Why it merits attention

Assessment: a small CLI trial gives directly inspectable editing results. Documentation reviewed; no speed or frame-quality test. [Source 1](https://github.com/hzwer/ECCV2022-RIFE)

### Limitations

Cuts, occlusions and fast motion can generate incorrect intermediate frames. [Source 1](https://github.com/hzwer/ECCV2022-RIFE)

### Get the tool

- [Repository](https://github.com/hzwer/ECCV2022-RIFE)
- [Documentation](https://github.com/hzwer/ECCV2022-RIFE)
- [Download](https://github.com/hzwer/ECCV2022-RIFE/releases)

## AudioCraft / MusicGen

Audio, music & voice · Performance, projection & stage media · Storyboarding, narrative & comics

First detailed review in this library. An established baseline newly covered by the expanded search, not a claim that it launched or significantly changed today.

### How it uses AI

A neural audio toolkit including text- and melody-conditioned music generation. Creative use: Non-commercial soundtrack sketches and research on controllable music or sound generation. [Source](https://github.com/facebookresearch/audiocraft)

### Introduction

A neural audio toolkit including text- and melody-conditioned music generation. [Source 1](https://github.com/facebookresearch/audiocraft)

### What it is good for

Non-commercial soundtrack sketches and research on controllable music or sound generation. [Source 1](https://github.com/facebookresearch/audiocraft)

### Demo & examples

The repository and MusicGen guide link audio examples and an official Hugging Face demo. [Source 1](https://github.com/facebookresearch/audiocraft) [Source 2](https://github.com/facebookresearch/audiocraft/blob/main/docs/MUSICGEN.md)

### Install

Documented installation route; commands below are reference text and were not executed. [Source 1](https://github.com/facebookresearch/audiocraft/blob/main/docs/MUSICGEN.md) [Source 2](https://github.com/facebookresearch/audiocraft)

1. Use the documented Python 3.9/PyTorch 2.1.0 setup and install FFmpeg.
2. Install AudioCraft and choose a model after reviewing its weight terms.
3. Follow the MusicGen example or its Gradio application instructions.

```sh
pip install -U audiocraft
```

### First project

Suggested first project, based on the documented controls; an untested trial plan. [Source 1](https://github.com/facebookresearch/audiocraft)

1. My suggested trial: generate a short instrumental cue from a simple mood prompt.
2. Compare two prompts while retaining their model and settings.
3. Keep it as a research sketch unless the selected model license permits the intended use.
### Hardware & software

Configuration-specific requirements; missing minimums are stated explicitly. [Source 1](https://github.com/facebookresearch/audiocraft/blob/main/docs/MUSICGEN.md) [Source 2](https://github.com/facebookresearch/audiocraft)

- **Hardware:** The MusicGen guide recommends a GPU with at least 16 GB memory for medium/1.5B models. Smaller short-sequence setups differ. RAM and storage minimums are not documented.
- **Software:** Python 3.9, PyTorch 2.1.0, FFmpeg and downloaded model checkpoints in the documented route.
- **Platforms:** The main route is GPU/PyTorch-oriented; a complete OS/version support matrix is not documented. A web demo is a separate hosted route.

### License, model weights & costs

Reviewed MIT project software; model and service terms are separate. [Source 1](https://github.com/facebookresearch/audiocraft/blob/main/LICENSE) [Source 2](https://github.com/facebookresearch/audiocraft)

- **Code:** MIT
- **Weights:** Published AudioCraft/MusicGen weights are CC-BY-NC-4.0; the software is MIT.
- **Commercial:** MIT software can be used commercially; the supplied non-commercial weights do not authorize commercial music generation.
- **Cost:** Local compute and storage; optional external services have separate charges. Current prices are not verified.

### Why it merits attention

Assessment: melody/text conditioning is useful for sound-design research, with the weight restriction made explicit. Documentation reviewed; no audio synthesized. [Source 1](https://github.com/facebookresearch/audiocraft)

### Limitations

Non-commercial weights are a material restriction. Musical coherence and adherence are not independently evaluated here. [Source 1](https://github.com/facebookresearch/audiocraft)

### Get the tool

- [Repository](https://github.com/facebookresearch/audiocraft)
- [Documentation](https://github.com/facebookresearch/audiocraft/blob/main/docs/MUSICGEN.md)
- [Download](https://github.com/facebookresearch/audiocraft/releases)

## MotionGPT

Motion capture & character animation · Avatars, digital humans & lip sync · Games & production pipelines · Performance, projection & stage media

First detailed review in this library. An established baseline newly covered by the expanded search, not a claim that it launched or significantly changed today.

### How it uses AI

A motion-language research release for text-driven human-motion generation. Creative use: Early character-action prototypes and exploring language as a motion authoring interface. [Source](https://github.com/OpenMotionLab/MotionGPT)

### Introduction

A motion-language research release for text-driven human-motion generation. [Source 1](https://github.com/OpenMotionLab/MotionGPT)

### What it is good for

Early character-action prototypes and exploring language as a motion authoring interface. [Source 1](https://github.com/OpenMotionLab/MotionGPT)

### Demo & examples

The repository links motion examples and a Gradio application. [Source 1](https://github.com/OpenMotionLab/MotionGPT)

### Install

Documented installation route; commands below are reference text and were not executed. [Source 1](https://github.com/OpenMotionLab/MotionGPT)

1. Use the tested Python 3.10.6/PyTorch 2.0.0 environment and install requirements.txt.
2. Obtain the documented checkpoints and necessary motion-data assets; review their independent terms.
3. Launch app.py or use the supplied text-to-motion demo configuration.

```sh
python app.py
```


```sh
python demo.py --cfg ./configs/config_h3d_stage3.yaml --example ./demos/t2m.txt
```

### First project

Suggested first project, based on the documented controls; an untested trial plan. [Source 1](https://github.com/OpenMotionLab/MotionGPT)

1. My suggested trial: generate a simple walking or gesturing action.
2. Inspect the skeleton and motion timing before importing it into a character pipeline.
3. Retarget and edit the result as a prototype, not a finished performance.
### Hardware & software

Configuration-specific requirements; missing minimums are stated explicitly. [Source 1](https://github.com/OpenMotionLab/MotionGPT)

- **Hardware:** GPU examples do not establish a minimum. RAM, VRAM and storage requirements are not documented in the reviewed setup.
- **Software:** Tested Python 3.10.6/PyTorch 2.0.0; requirements, spaCy language model, checkpoints and motion assets.
- **Platforms:** Research Python/PyTorch setup; a complete native Windows/macOS support matrix is not documented.

### License, model weights & costs

Reviewed MIT project software; model and service terms are separate. [Source 1](https://github.com/OpenMotionLab/MotionGPT/blob/main/LICENSE) [Source 2](https://github.com/OpenMotionLab/MotionGPT)

- **Code:** MIT
- **Weights:** Check checkpoint, HumanML3D and body-model/data terms independently of the MIT code.
- **Commercial:** Software terms reviewed; permission for a complete commercial deployment depends on the chosen models and dependencies and is not fully verified.
- **Cost:** Local compute and storage; optional external services have separate charges. Current prices are not verified.

### Why it merits attention

Assessment: text-to-motion examples reveal a concrete creative use beyond image generation. Documentation reviewed; no animation generated. [Source 1](https://github.com/OpenMotionLab/MotionGPT)

### Limitations

Research output requires skeleton, retargeting and motion-quality review. Dataset/body-model licensing can constrain use. [Source 1](https://github.com/OpenMotionLab/MotionGPT)

### Get the tool

- [Repository](https://github.com/OpenMotionLab/MotionGPT)
- [Documentation](https://github.com/OpenMotionLab/MotionGPT)
- [Download](https://github.com/OpenMotionLab/MotionGPT/releases)

## PyTorch-SVGRender

Vector graphics, illustration & textures · Typography, fonts & layout · Computational art & creative coding

First detailed review in this library. An established baseline newly covered by the expanded search, not a claim that it launched or significantly changed today.

### How it uses AI

A research toolkit for AI-assisted vector graphics and differentiable SVG rendering. Creative use: Text-guided SVG experiments, image-to-vector studies and exploratory letterform work. [Source](https://github.com/ximinng/PyTorch-SVGRender)

### Introduction

A research toolkit for AI-assisted vector graphics and differentiable SVG rendering. [Source 1](https://github.com/ximinng/PyTorch-SVGRender)

### What it is good for

Text-guided SVG experiments, image-to-vector studies and exploratory letterform work. [Source 1](https://github.com/ximinng/PyTorch-SVGRender)

### Demo & examples

The repository and official documentation show multiple methods and example render commands. [Source 1](https://github.com/ximinng/PyTorch-SVGRender) [Source 2](https://pytorch-svgrender.readthedocs.io/en/latest/)

### Install

Documented installation route; commands below are reference text and were not executed. [Source 1](https://pytorch-svgrender.readthedocs.io/en/latest/) [Source 2](https://github.com/ximinng/PyTorch-SVGRender) [Source 3](https://github.com/ximinng/PyTorch-SVGRender/blob/main/script/install.sh)

1. Read the official installation guide and its script dependencies before choosing a supported environment.
2. Install the required PyTorch/CUDA and method-specific components as documented.
3. Start with a supplied method example and its required model/assets.

```sh
python svg_render.py x=clipdraw "prompt='a photo of a cat'"
```

### First project

Suggested first project, based on the documented controls; an untested trial plan. [Source 1](https://github.com/ximinng/PyTorch-SVGRender)

1. My suggested trial: generate a simple symbol from a short prompt.
2. Open the SVG in a vector editor and inspect path complexity and editability.
3. For lettering, verify legibility independently of visual resemblance.
### Hardware & software

Configuration-specific requirements; missing minimums are stated explicitly. [Source 1](https://pytorch-svgrender.readthedocs.io/en/latest/) [Source 2](https://github.com/ximinng/PyTorch-SVGRender) [Source 3](https://github.com/ximinng/PyTorch-SVGRender/blob/main/script/install.sh)

- **Hardware:** Methods use different differentiable-rendering/ML dependencies. A universal RAM/VRAM/storage minimum is not documented.
- **Software:** The provided install script pins Python 3.10, PyTorch 1.12.1, torchvision 0.13.1, CUDA toolkit 11.3 and diffusers 0.20.2, plus DiffVG/build dependencies. This older stack needs compatibility review.
- **Platforms:** The provided setup includes Ubuntu package commands and CUDA components. Native Windows/macOS support is not verified.

### License, model weights & costs

Reviewed MPL-2.0 project software; model and service terms are separate. [Source 1](https://github.com/ximinng/PyTorch-SVGRender/blob/main/LICENSE) [Source 2](https://github.com/ximinng/PyTorch-SVGRender)

- **Code:** MPL-2.0
- **Weights:** Each CLIP, diffusion or other pretrained component has separate terms.
- **Commercial:** Software terms reviewed; permission for a complete commercial deployment depends on the chosen models and dependencies and is not fully verified.
- **Cost:** Local compute and storage; optional external services have separate charges. Current prices are not verified.

### Why it merits attention

Assessment: released code and several vector-specific methods warrant an experimental trial. Documentation reviewed; no SVG rendered. [Source 1](https://github.com/ximinng/PyTorch-SVGRender)

### Limitations

Work in progress with an older pinned setup; generated paths can be complex and lettering need not remain clean editable type. [Source 1](https://github.com/ximinng/PyTorch-SVGRender)

### Get the tool

- [Repository](https://github.com/ximinng/PyTorch-SVGRender)
- [Documentation](https://pytorch-svgrender.readthedocs.io/en/latest/)
- [Download](https://github.com/ximinng/PyTorch-SVGRender/releases)

## RVC WebUI

Audio, music & voice · Avatars, digital humans & lip sync · Performance, projection & stage media · Games & production pipelines

First detailed review in this library. An established baseline newly covered by the expanded search, not a claim that it launched or significantly changed today.

### How it uses AI

A local voice-conversion interface with retrieval-based model training and inference. Creative use: Vocal-timbre experiments and prototype character-voice transformations. [Source](https://github.com/RVC-Project/Retrieval-based-Voice-Conversion-WebUI)

### Introduction

A local voice-conversion interface with retrieval-based model training and inference. [Source 1](https://github.com/RVC-Project/Retrieval-based-Voice-Conversion-WebUI)

### What it is good for

Vocal-timbre experiments and prototype character-voice transformations. [Source 1](https://github.com/RVC-Project/Retrieval-based-Voice-Conversion-WebUI)

### Demo & examples

The official Chinese-language README provides updated setup and interface routes; no conversion was run. [Source 1](https://github.com/RVC-Project/Retrieval-based-Voice-Conversion-WebUI)

### Install

Documented installation route; commands below are reference text and were not executed. [Source 1](https://github.com/RVC-Project/Retrieval-based-Voice-Conversion-WebUI)

1. Create a Python 3.12 x64 environment and install the documented FFmpeg/audio system dependencies.
2. Choose the CPU/AMD/Intel or NVIDIA requirements file matching the device; the filenames intentionally spell requirments.
3. Download the required inference assets, then start webui.py.

```sh
python -m pip install -r requirments_cpu_py312.txt
```


```sh
python webui.py
```

### First project

Suggested first project, based on the documented controls; an untested trial plan. [Source 1](https://github.com/RVC-Project/Retrieval-based-Voice-Conversion-WebUI)

1. My suggested trial: use a short clean recording and a voice model you are entitled to use.
2. Convert a copy and compare articulation and noise against the source.
3. Tune conservatively and retain the input, model and parameters.
### Hardware & software

Configuration-specific requirements; missing minimums are stated explicitly. [Source 1](https://github.com/RVC-Project/Retrieval-based-Voice-Conversion-WebUI)

- **Hardware:** CPU, Windows DirectML and NVIDIA routes are documented. No universal RAM/VRAM/storage minimum is published in the reviewed setup.
- **Software:** Python 3.12 x64, FFmpeg and model assets. Current NVIDIA routes use Torch 2.7.1 with CUDA 12.8 for RTX 50-series or CUDA 11.8 for earlier GPUs.
- **Platforms:** Windows and Ubuntu 24.04 x86_64 setup is documented. Current native macOS support is not verified in these instructions.

### License, model weights & costs

Reviewed MIT project software; model and service terms are separate. [Source 1](https://github.com/RVC-Project/Retrieval-based-Voice-Conversion-WebUI/blob/main/LICENSE) [Source 2](https://github.com/RVC-Project/Retrieval-based-Voice-Conversion-WebUI)

- **Code:** MIT
- **Weights:** Every downloaded or trained voice model and source dataset has separate terms.
- **Commercial:** Software terms reviewed; permission for a complete commercial deployment depends on the chosen models and dependencies and is not fully verified.
- **Cost:** Local compute and storage; optional external services have separate charges. Current prices are not verified.

### Why it merits attention

Assessment: explicit contemporary setup branches and local conversion address a concrete creative audio task. Documentation reviewed; no training or inference. [Source 1](https://github.com/RVC-Project/Retrieval-based-Voice-Conversion-WebUI)

### Limitations

Model/source-voice rights and artifacts need review; training claims are not quality guarantees. [Source 1](https://github.com/RVC-Project/Retrieval-based-Voice-Conversion-WebUI)

### Get the tool

- [Repository](https://github.com/RVC-Project/Retrieval-based-Voice-Conversion-WebUI)
- [Documentation](https://github.com/RVC-Project/Retrieval-based-Voice-Conversion-WebUI)
- [Download](https://github.com/RVC-Project/Retrieval-based-Voice-Conversion-WebUI/releases)

## LivePortrait

Avatars, digital humans & lip sync · Video, animation & film · Motion capture & character animation · Storyboarding, narrative & comics

First detailed review in this library. An established baseline newly covered by the expanded search, not a claim that it launched or significantly changed today.

### How it uses AI

A portrait-animation toolkit driven by motion from a reference performance. Creative use: Short character and portrait animation prototypes with expression and pose control. [Source](https://github.com/KlingAIResearch/LivePortrait)

### Introduction

A portrait-animation toolkit driven by motion from a reference performance. [Source 1](https://github.com/KlingAIResearch/LivePortrait)

### What it is good for

Short character and portrait animation prototypes with expression and pose control. [Source 1](https://github.com/KlingAIResearch/LivePortrait)

### Demo & examples

The official README links human/animal examples and project demos; they were not reproduced here. [Source 1](https://github.com/KlingAIResearch/LivePortrait)

### Install

Documented installation route; commands below are reference text and were not executed. [Source 1](https://github.com/KlingAIResearch/LivePortrait)

1. Use the official Python 3.10/FFmpeg setup and the appropriate PyTorch route.
2. Download the listed pretrained components, checking InsightFace model restrictions.
3. Run inference.py with a source portrait and driving clip; use the documented MPS fallback on Apple Silicon.

```sh
python inference.py -s source.jpg -d driving.mp4
```

### First project

Suggested first project, based on the documented controls; an untested trial plan. [Source 1](https://github.com/KlingAIResearch/LivePortrait)

1. My suggested trial: animate an original portrait from a short, simple driving clip.
2. Inspect eyes, mouth and silhouette for unstable motion.
3. Keep the animation as a prototype and review model permissions before commercial delivery.
### Hardware & software

Configuration-specific requirements; missing minimums are stated explicitly. [Source 1](https://github.com/KlingAIResearch/LivePortrait)

- **Hardware:** Hardware benchmarks are configuration-specific; universal RAM, VRAM and storage minimums are not documented.
- **Software:** Python 3.10, FFmpeg, PyTorch and pretrained components; macOS has requirements_macOS.txt and MPS fallback instructions.
- **Platforms:** Windows/Linux routes cover human and animal modes. Apple Silicon macOS supports the documented human route; animal mode is unsupported there and Intel Macs are not verified.

### License, model weights & costs

Reviewed MIT project software; model and service terms are separate. [Source 1](https://github.com/KlingAIResearch/LivePortrait/blob/main/LICENSE) [Source 2](https://github.com/KlingAIResearch/LivePortrait)

- **Code:** MIT
- **Weights:** InsightFace face-detection models are non-commercial/research-only; other components have individual terms.
- **Commercial:** MIT project code permits commercial use; the developers require replacing restricted InsightFace detection models for commercial projects.
- **Cost:** Local compute and storage; optional external services have separate charges. Current prices are not verified.

### Why it merits attention

Assessment: explicit driving inputs and platform caveats make an inspectable avatar trial possible. Documentation reviewed; no face animation run. [Source 1](https://github.com/KlingAIResearch/LivePortrait)

### Limitations

Default dependencies constrain commercial deployment. Portrait likeness and temporal stability were not tested. [Source 1](https://github.com/KlingAIResearch/LivePortrait)

### Get the tool

- [Repository](https://github.com/KlingAIResearch/LivePortrait)
- [Documentation](https://github.com/KlingAIResearch/LivePortrait)
- [Download](https://github.com/KlingAIResearch/LivePortrait/releases)

## OpenVoice

Audio, music & voice · Storyboarding, narrative & comics · Avatars, digital humans & lip sync · Accessible media & assistive creation

First detailed review in this library. An established baseline newly covered by the expanded search, not a claim that it launched or significantly changed today.

### How it uses AI

A voice-cloning toolkit with speaker-style controls and multilingual synthesis. Creative use: Narration prototypes and multilingual character-voice experiments from reference speech. [Source](https://github.com/myshell-ai/OpenVoice)

### Introduction

A voice-cloning toolkit with speaker-style controls and multilingual synthesis. [Source 1](https://github.com/myshell-ai/OpenVoice)

### What it is good for

Narration prototypes and multilingual character-voice experiments from reference speech. [Source 1](https://github.com/myshell-ai/OpenVoice)

### Demo & examples

The repository links voice examples and V2 usage notebooks; no voice was cloned here. [Source 1](https://github.com/myshell-ai/OpenVoice) [Source 2](https://github.com/myshell-ai/OpenVoice/blob/main/docs/USAGE.md)

### Install

Documented installation route; commands below are reference text and were not executed. [Source 1](https://github.com/myshell-ai/OpenVoice/blob/main/docs/USAGE.md) [Source 2](https://github.com/myshell-ai/OpenVoice)

1. Follow the developer Linux environment instructions; the usage guide creates a Python 3.9 environment.
2. Install the repository package and download V2 checkpoints into checkpoints_v2.
3. For V2, install the documented MeloTTS dependency and follow demo_part3.ipynb.
### First project

Suggested first project, based on the documented controls; an untested trial plan. [Source 1](https://github.com/myshell-ai/OpenVoice)

1. My suggested trial: use reference speech recorded for this purpose.
2. Render one short line and compare articulation and timbre.
3. Check each target language and retain the reference and model version with the output.
### Hardware & software

Configuration-specific requirements; missing minimums are stated explicitly. [Source 1](https://github.com/myshell-ai/OpenVoice/blob/main/docs/USAGE.md) [Source 2](https://github.com/myshell-ai/OpenVoice)

- **Hardware:** The reviewed guide does not publish a RAM, VRAM or total storage minimum.
- **Software:** Python 3.9 in the supplied environment example, PyTorch, V2 checkpoints and MeloTTS dependencies.
- **Platforms:** The developer usage route is Linux-oriented; native Windows/macOS support is not documented in that guide.

### License, model weights & costs

Reviewed MIT project software; model and service terms are separate. [Source 1](https://github.com/myshell-ai/OpenVoice/blob/main/LICENSE) [Source 2](https://github.com/myshell-ai/OpenVoice)

- **Code:** MIT
- **Weights:** The README expressly releases OpenVoice V1/V2 checkpoints under MIT; MeloTTS and other dependencies retain their own terms.
- **Commercial:** The developers expressly permit commercial use of OpenVoice code and V1/V2 checkpoints under MIT; reference-voice rights and dependencies remain separate.
- **Cost:** Local compute and storage; optional external services have separate charges. Current prices are not verified.

### Why it merits attention

Assessment: explicit V2 notebooks and disclosed checkpoint terms support a useful multilingual voice experiment. Documentation reviewed; no synthesis. [Source 1](https://github.com/myshell-ai/OpenVoice)

### Limitations

Cross-language voice quality and similarity need listening tests; environment setup includes multiple components. [Source 1](https://github.com/myshell-ai/OpenVoice)

### Get the tool

- [Repository](https://github.com/myshell-ai/OpenVoice)
- [Documentation](https://github.com/myshell-ai/OpenVoice/blob/main/docs/USAGE.md)
- [Download](https://github.com/myshell-ai/OpenVoice/releases)

## Fooocus

Images & design · Photography, restoration & color · Storyboarding, narrative & comics

First detailed review in this library. An established baseline newly covered by the expanded search, not a claim that it launched or significantly changed today.

### How it uses AI

An SDXL image-generation interface focused on prompts and input-image variations. Creative use: Low-control concept exploration, inpainting and prompt-based image iterations. [Source](https://github.com/lllyasviel/Fooocus)

### Introduction

An SDXL image-generation interface focused on prompts and input-image variations. [Source 1](https://github.com/lllyasviel/Fooocus)

### What it is good for

Low-control concept exploration, inpainting and prompt-based image iterations. [Source 1](https://github.com/lllyasviel/Fooocus)

### Demo & examples

The README provides image comparisons and UI examples; these are developer demonstrations. [Source 1](https://github.com/lllyasviel/Fooocus)

### Install

Documented installation route; commands below are reference text and were not executed. [Source 1](https://github.com/lllyasviel/Fooocus)

1. On Windows, download and extract the official package and start run.bat.
2. On Linux, follow the Python 3.10 environment route and install requirements_versions.txt.
3. On Apple Silicon, follow the explicitly unofficial MPS guide; start entry_with_update.py and allow model downloads.

```sh
python entry_with_update.py
```

### First project

Suggested first project, based on the documented controls; an untested trial plan. [Source 1](https://github.com/lllyasviel/Fooocus)

1. My suggested trial: use the default SDXL preset and a simple composition prompt.
2. Compare one variation and one masked edit while keeping originals.
3. Save settings and verify the downloaded preset model terms before final work.
### Hardware & software

Configuration-specific requirements; missing minimums are stated explicitly. [Source 1](https://github.com/lllyasviel/Fooocus)

- **Hardware:** RTX Windows/Linux guide: 4 GB VRAM and 8 GB RAM with swap; older/AMD routes differ, and CPU-only guide lists 32 GB RAM. Apple Silicon uses shared memory. Total storage minimum is not documented.
- **Software:** Linux guide uses Python 3.10; release/environment dependencies and SDXL models. First-use inpainting can download a 1.28 GB control file.
- **Platforms:** Windows and Linux routes are documented; AMD is beta. Apple Silicon Mac instructions are explicitly unofficial and lightly tested.

### License, model weights & costs

Reviewed GPL-3.0 project software; model and service terms are separate. [Source 1](https://github.com/lllyasviel/Fooocus/blob/main/LICENSE) [Source 2](https://github.com/lllyasviel/Fooocus)

- **Code:** GPL-3.0
- **Weights:** Default and alternative SDXL checkpoints, presets and inpaint models retain independent terms.
- **Commercial:** Software terms reviewed; permission for a complete commercial deployment depends on the chosen models and dependencies and is not fully verified.
- **Cost:** Local compute and storage; optional external services have separate charges. Current prices are not verified.

### Why it merits attention

Assessment: an accessible SDXL baseline, with its LTS status disclosed rather than presented as a new launch. Documentation reviewed; no generation run. [Source 1](https://github.com/lllyasviel/Fooocus)

### Limitations

The project is in limited LTS with bug fixes only and has no current plan to adopt newer model architectures. [Source 1](https://github.com/lllyasviel/Fooocus)

### Get the tool

- [Repository](https://github.com/lllyasviel/Fooocus)
- [Documentation](https://github.com/lllyasviel/Fooocus)
- [Download](https://github.com/lllyasviel/Fooocus/releases)

## Additional open-source AI discoveries

Creative AI relevance and software license screened. Full installation, requirements and quality profiles are pending.

### F5-TTS · MIT

Flow-matching speech generation for narration and character-voice research.
Flow-matching speech generation for narration and character-voice research.
Software license and creative AI use screened; complete installation, hardware, dependent-model terms and output-quality review pending. Published pretrained weights are CC-BY-NC because of training-data terms; MIT code does not authorize commercial use of those weights.

- [Official README and creative workflow](https://github.com/SWivid/F5-TTS)
- [Reviewed software license](https://github.com/SWivid/F5-TTS/blob/main/LICENSE)
### CosyVoice · Apache-2.0

Multilingual, controllable speech synthesis for narration and interactive character prototypes.
Multilingual, controllable speech synthesis for narration and interactive character prototypes.
Software license and creative AI use screened; complete installation, hardware, dependent-model terms and output-quality review pending. Check the chosen checkpoint, text-front-end and streaming dependencies individually.

- [Official README and creative workflow](https://github.com/QwenAudio/CosyVoice)
- [Reviewed software license](https://github.com/QwenAudio/CosyVoice/blob/main/LICENSE)
### RIFE ncnn Vulkan · MIT

Neural frame interpolation through a portable Vulkan implementation.
Neural frame interpolation through a portable Vulkan implementation.
Software license and creative AI use screened; complete installation, hardware, dependent-model terms and output-quality review pending. Official binaries cover Windows/Linux/macOS and Intel/AMD/NVIDIA GPUs; model terms and device performance need a full profile.

- [Official README and creative workflow](https://github.com/nihui/rife-ncnn-vulkan)
- [Reviewed software license](https://github.com/nihui/rife-ncnn-vulkan/blob/master/LICENSE)
### BiRefNet · MIT

High-resolution neural foreground segmentation for cutout and composite workflows.
High-resolution neural foreground segmentation for cutout and composite workflows.
Software license and creative AI use screened; complete installation, hardware, dependent-model terms and output-quality review pending. Do not confuse this MIT code with BRIA RMBG-2.0 weights, which the README describes as non-commercial.

- [Official README and creative workflow](https://github.com/ZhengPeng7/BiRefNet)
- [Reviewed software license](https://github.com/ZhengPeng7/BiRefNet/blob/main/LICENSE)
### Wan2.2 · Apache-2.0

Text/image-driven video generation for shot and motion prototypes.
Text/image-driven video generation for shot and motion prototypes.
Software license and creative AI use screened; complete installation, hardware, dependent-model terms and output-quality review pending. The README identifies Apache-2.0 model terms; hardware tiers, checkpoint selection and output consistency still need detailed review.

- [Official README and creative workflow](https://github.com/Wan-Video/Wan2.2)
- [Reviewed software license](https://github.com/Wan-Video/Wan2.2/blob/main/LICENSE.txt)
### LTX-Video (earlier generation) · Apache-2.0

Diffusion video generation from text and image/keyframe inputs.
Diffusion video generation from text and image/keyframe inputs.
Software license and creative AI use screened; complete installation, hardware, dependent-model terms and output-quality review pending. This repository now directs current development to LTX-2. Earlier LTX-Video weights have version-specific OpenRail terms; do not treat this as the newest LTX release.

- [Official README and creative workflow](https://github.com/Lightricks/LTX-Video)
- [Reviewed software license](https://github.com/Lightricks/LTX-Video/blob/main/LICENSE)
### Open-Sora · Apache-2.0

Released video-generation and training software for experimental film workflows.
Released video-generation and training software for experimental film workflows.
Software license and creative AI use screened; complete installation, hardware, dependent-model terms and output-quality review pending. Research setup and model-specific hardware, checkpoint terms and reproducibility need a full review.

- [Official README and creative workflow](https://github.com/hpcaitech/Open-Sora)
- [Reviewed software license](https://github.com/hpcaitech/Open-Sora/blob/main/LICENSE)
### CogVideoX · Apache-2.0

Text/image-to-video generation with released inference code and demos.
Text/image-to-video generation with released inference code and demos.
Software license and creative AI use screened; complete installation, hardware, dependent-model terms and output-quality review pending. CogVideoX-2B is documented under Apache-2.0; other versions have separate model terms. Select a version before commercial or hardware advice.

- [Official README and creative workflow](https://github.com/zai-org/CogVideo)
- [Reviewed software license](https://github.com/zai-org/CogVideo/blob/main/LICENSE)
### PaddleOCR · Apache-2.0

OCR and document vision models convert scans, images and PDFs into editable text and structured Markdown/JSON.
OCR and document vision models convert scans, images and PDFs into editable text and structured Markdown/JSON.
Software license and creative AI use screened; complete installation, hardware, dependent-model terms and output-quality review pending. Model/version selection, language coverage, layout fidelity and local installation remain to be profiled.

- [Official README and creative workflow](https://github.com/PaddlePaddle/PaddleOCR)
- [Reviewed software license](https://github.com/PaddlePaddle/PaddleOCR/blob/main/LICENSE)
### gsplat · Apache-2.0

CUDA Gaussian-splatting components for training/rendering learned scenes and custom spatial-media tools.
CUDA Gaussian-splatting components for training/rendering learned scenes and custom spatial-media tools.
Software license and creative AI use screened; complete installation, hardware, dependent-model terms and output-quality review pending. A developer component, not a ready-made editor. README main-branch features can precede a PyPI release; exact version and CUDA setup need review.

- [Official README and creative workflow](https://github.com/nerfstudio-project/gsplat)
- [Reviewed software license](https://github.com/nerfstudio-project/gsplat/blob/main/LICENSE)
### ComfyUI-3D-Pack · MIT

ComfyUI nodes connect learned reconstruction/generation models with meshes and UV workflows.
ComfyUI nodes connect learned reconstruction/generation models with meshes and UV workflows.
Software license and creative AI use screened; complete installation, hardware, dependent-model terms and output-quality review pending. Every bundled model, third-party component and automatic build dependency needs separate compatibility and terms checks.

- [Official README and creative workflow](https://github.com/MrForExample/ComfyUI-3D-Pack)
- [Reviewed software license](https://github.com/MrForExample/ComfyUI-3D-Pack/blob/main/LICENSE)
### TRELLIS (first generation) · MIT

Structured 3D generation from images/text into meshes, Gaussians or radiance fields.
Structured 3D generation from images/text into meshes, Gaussians or radiance fields.
Software license and creative AI use screened; complete installation, hardware, dependent-model terms and output-quality review pending. Distinct from TRELLIS.2 in the original edition; compare generations and checkpoint terms rather than assume the first is newer.

- [Official README and creative workflow](https://github.com/microsoft/TRELLIS)
- [Reviewed software license](https://github.com/microsoft/TRELLIS/blob/main/LICENSE)
### InstantMesh · Apache-2.0

Image-conditioned multi-view generation and reconstruction of 3D asset meshes.
Image-conditioned multi-view generation and reconstruction of 3D asset meshes.
Software license and creative AI use screened; complete installation, hardware, dependent-model terms and output-quality review pending. Research output needs topology, hidden-surface and printability checks; no fabrication readiness is inferred.

- [Official README and creative workflow](https://github.com/TencentARC/InstantMesh)
- [Reviewed software license](https://github.com/TencentARC/InstantMesh/blob/main/LICENSE)
### TripoSG · MIT

Image-to-3D shape generation, including a scribble-and-prompt prototype path.
Image-to-3D shape generation, including a scribble-and-prompt prototype path.
Software license and creative AI use screened; complete installation, hardware, dependent-model terms and output-quality review pending. Checkpoint/model dependencies, environment builds and mesh quality remain pending; export does not guarantee printable geometry.

- [Official README and creative workflow](https://github.com/VAST-AI-Research/TripoSG)
- [Reviewed software license](https://github.com/VAST-AI-Research/TripoSG/blob/main/LICENSE)
### MoMask · MIT

Text-conditioned 3D human-motion generation, with a linked Blender integration.
Text-conditioned 3D human-motion generation, with a linked Blender integration.
Software license and creative AI use screened; complete installation, hardware, dependent-model terms and output-quality review pending. SMPL/SMPL-X, datasets and supporting libraries have independent terms; retargeting and motion quality need a full review.

- [Official README and creative workflow](https://github.com/EricGuo5513/momask-codes)
- [Reviewed software license](https://github.com/EricGuo5513/momask-codes/blob/main/LICENSE)
### RealtimeSTT · MIT

Streaming speech recognition and voice-activity/wake-word inputs for interactive media prototypes.
Streaming speech recognition and voice-activity/wake-word inputs for interactive media prototypes.
Software license and creative AI use screened; complete installation, hardware, dependent-model terms and output-quality review pending. Engine choices include different local and commercial model terms; choose and profile one engine/device route.

- [Official README and creative workflow](https://github.com/KoljaB/RealtimeSTT)
- [Reviewed software license](https://github.com/KoljaB/RealtimeSTT/blob/master/LICENSE)
### RealtimeTTS · MIT

Streaming neural speech output for interactive characters and spoken interfaces.
Streaming neural speech output for interactive characters and spoken interfaces.
Software license and creative AI use screened; complete installation, hardware, dependent-model terms and output-quality review pending. Local neural engines, system voices and paid cloud engines are distinct; optional non-commercial audio samples and model terms need review.

- [Official README and creative workflow](https://github.com/KoljaB/RealtimeTTS)
- [Reviewed software license](https://github.com/KoljaB/RealtimeTTS/blob/master/LICENSE)
### stable-audio-tools · MIT

Training and inference software for diffusion-based music and sound experiments.
Training and inference software for diffusion-based music and sound experiments.
Software license and creative AI use screened; complete installation, hardware, dependent-model terms and output-quality review pending. MIT code is separate from Stable Audio checkpoint licenses; hardware and model permissions need a model-specific profile.

- [Official README and creative workflow](https://github.com/Stability-AI/stable-audio-tools)
- [Reviewed software license](https://github.com/Stability-AI/stable-audio-tools/blob/main/LICENSE)
### Bark · MIT

Generative speech, nonverbal sounds and short audio effects from text.
Generative speech, nonverbal sounds and short audio effects from text.
Software license and creative AI use screened; complete installation, hardware, dependent-model terms and output-quality review pending. The README describes MIT code/models and research limitations; pronunciation, duration and controllability still need a listening test.

- [Official README and creative workflow](https://github.com/suno-ai/bark)
- [Reviewed software license](https://github.com/suno-ai/bark/blob/main/LICENSE)
### Diffusers · Apache-2.0

Composable diffusion pipelines for custom creative generation, adapters and fine-tuning.
Composable diffusion pipelines for custom creative generation, adapters and fine-tuning.
Software license and creative AI use screened; complete installation, hardware, dependent-model terms and output-quality review pending. Apache-2.0 library terms do not license all models; select a concrete pipeline before installation/hardware recommendations.

- [Official README and creative workflow](https://github.com/huggingface/diffusers)
- [Reviewed software license](https://github.com/huggingface/diffusers/blob/main/LICENSE)
### DiffSynth-Studio · Apache-2.0

Diffusion inference/training with VRAM scheduling and quantization for custom media workflows.
Diffusion inference/training with VRAM scheduling and quantization for custom media workflows.
Software license and creative AI use screened; complete installation, hardware, dependent-model terms and output-quality review pending. Supported model families, offloading and checkpoint terms differ; memory claims require a particular configuration.

- [Official README and creative workflow](https://github.com/modelscope/DiffSynth-Studio)
- [Reviewed software license](https://github.com/modelscope/DiffSynth-Studio/blob/main/LICENSE)
### DWPose · Apache-2.0

Whole-body pose estimation supplies motion/pose conditions for image and animation generation.
Whole-body pose estimation supplies motion/pose conditions for image and animation generation.
Software license and creative AI use screened; complete installation, hardware, dependent-model terms and output-quality review pending. Base pose estimates are not finished animation; checkpoint, dependency and downstream generator terms need separate review.

- [Official README and creative workflow](https://github.com/IDEA-Research/DWPose)
- [Reviewed software license](https://github.com/IDEA-Research/DWPose/blob/onnx/LICENSE)
### Grounding DINO · Apache-2.0

Text-conditioned object detection supplies object selections and conditioning for creative editing pipelines.
Text-conditioned object detection supplies object selections and conditioning for creative editing pipelines.
Software license and creative AI use screened; complete installation, hardware, dependent-model terms and output-quality review pending. Detector output still needs segmentation/editing components; exact model and integration requirements remain pending.

- [Official README and creative workflow](https://github.com/IDEA-Research/GroundingDINO)
- [Reviewed software license](https://github.com/IDEA-Research/GroundingDINO/blob/main/LICENSE)
### ControlNet · Apache-2.0

Adds learned structural conditions such as edges, poses and depth to diffusion image generation.
Adds learned structural conditions such as edges, poses and depth to diffusion image generation.
Software license and creative AI use screened; complete installation, hardware, dependent-model terms and output-quality review pending. This is the original implementation; newer variants and UI integrations are separate. Base models and condition extractors retain their own terms.

- [Official README and creative workflow](https://github.com/lllyasviel/ControlNet)
- [Reviewed software license](https://github.com/lllyasviel/ControlNet/blob/main/LICENSE)
### IC-Light · Apache-2.0

AI relighting from foreground images with text or background conditions.
AI relighting from foreground images with text or background conditions.
Software license and creative AI use screened; complete installation, hardware, dependent-model terms and output-quality review pending. The README identifies BRIA RMBG-1.4 as non-commercial and suggests replacing it for commercial workflows; full dependency/model review remains pending.

- [Official README and creative workflow](https://github.com/lllyasviel/IC-Light)
- [Reviewed software license](https://github.com/lllyasviel/IC-Light/blob/main/LICENSE)
### AnimateDiff · Apache-2.0

Motion modules turn supported personalized diffusion-image models into animation generators.
Motion modules turn supported personalized diffusion-image models into animation generators.
Software license and creative AI use screened; complete installation, hardware, dependent-model terms and output-quality review pending. Main and SDXL-beta branches differ. Motion/base-model terms, GPU needs and temporal artifacts remain pending.

- [Official README and creative workflow](https://github.com/guoyww/AnimateDiff)
- [Reviewed software license](https://github.com/guoyww/AnimateDiff/blob/main/LICENSE.txt)
### CADAM · GPL-3.0

AI-assisted natural-language/image inputs generate editable parametric OpenSCAD geometry.
AI-assisted natural-language/image inputs generate editable parametric OpenSCAD geometry.
Software license and creative AI use screened; complete installation, hardware, dependent-model terms and output-quality review pending. STL/SCAD/DXF export is documented; dimension accuracy, provider setup, mechanical suitability and printability still need testing.

- [Official README and creative workflow](https://github.com/Adam-CAD/CADAM)
- [Reviewed software license](https://github.com/Adam-CAD/CADAM/blob/master/LICENSE)
### Web Stable Diffusion · Apache-2.0

WebGPU diffusion inference enables browser-native image-generation experiments.
WebGPU diffusion inference enables browser-native image-generation experiments.
Software license and creative AI use screened; complete installation, hardware, dependent-model terms and output-quality review pending. A browser demo and deployment notebook are available; browser/device compatibility, model cache and weight terms need review.

- [Official README and creative workflow](https://github.com/mlc-ai/web-stable-diffusion)
- [Reviewed software license](https://github.com/mlc-ai/web-stable-diffusion/blob/main/LICENSE)
### WebLLM · Apache-2.0

In-browser language-model inference can power local interactive narratives and creative assistants.
In-browser language-model inference can power local interactive narratives and creative assistants.
Software license and creative AI use screened; complete installation, hardware, dependent-model terms and output-quality review pending. Concrete creative use is an assessment of its documented streaming/JSON interface. Model terms and WebGPU/browser memory remain model-specific.

- [Official README and creative workflow](https://github.com/mlc-ai/web-llm)
- [Reviewed software license](https://github.com/mlc-ai/web-llm/blob/main/LICENSE)
### Qwen3-TTS · Apache-2.0

Voice design, cloning and natural-language voice control for multilingual narration prototypes.
Voice design, cloning and natural-language voice control for multilingual narration prototypes.
Software license and creative AI use screened; complete installation, hardware, dependent-model terms and output-quality review pending. The released 0.6B/1.7B variants and hosted APIs are different routes; checkpoint terms, hardware and output quality need a full profile.

- [Official README and creative workflow](https://github.com/QwenLM/Qwen3-TTS)
- [Reviewed software license](https://github.com/QwenLM/Qwen3-TTS/blob/main/LICENSE)
### Mixar · GPL-3.0

A Blender 5.2 fork adds an AI scene agent, layered texture painting, neural asset search and generation connections.
A Blender 5.2 fork adds an AI scene agent, layered texture painting, neural asset search and generation connections.
Software license and creative AI use screened; complete installation, hardware, dependent-model terms and output-quality review pending. GPL-3.0 desktop client; its AI backend is explicitly closed source and hosted. AI use needs an account/provider access; BYOK does not make the backend open source.

- [Official README and creative workflow](https://github.com/Mixar-AI/mixar-app)
- [Reviewed software license](https://github.com/Mixar-AI/mixar-app/blob/main/LICENSE)
### PotionUI · GPL-3.0

A self-hosted multimodal diffusion studio with generation forms, user accounts and video-shot sections.
A self-hosted multimodal diffusion studio with generation forms, user accounts and video-shot sections.
Software license and creative AI use screened; complete installation, hardware, dependent-model terms and output-quality review pending. Alpha; Linux NVIDIA setup and experimental Windows routes. The SDXL floor is stated as 8 GB VRAM/16 GB RAM; other models and their terms differ.

- [Official README and creative workflow](https://github.com/PotionUI/PotionUI)
- [Reviewed software license](https://github.com/PotionUI/PotionUI/blob/master/LICENSE)
### Generator Assets · MIT

A headless pipeline orchestrates local AI generation for Godot/Blender assets, music and video.
A headless pipeline orchestrates local AI generation for Godot/Blender assets, music and video.
Software license and creative AI use screened; complete installation, hardware, dependent-model terms and output-quality review pending. Vulkan/GGUF and engine-ready export are developer claims; model-specific licenses, builds and actual engine import need verification.

- [Official README and creative workflow](https://github.com/laurentvv/generator-assets)
- [Reviewed software license](https://github.com/laurentvv/generator-assets/blob/main/LICENSE)
### DreamGaussian · MIT

Generative Gaussian splatting builds 3D object prototypes from an image.
Generative Gaussian splatting builds 3D object prototypes from an image.
Software license and creative AI use screened; complete installation, hardware, dependent-model terms and output-quality review pending. Research quality, mesh conversion, geometry cleanup and all pretrained component terms remain pending.

- [Official README and creative workflow](https://github.com/dreamgaussian/dreamgaussian)
- [Reviewed software license](https://github.com/dreamgaussian/dreamgaussian/blob/main/LICENSE)
### Open Reality · BSD-2-Clause

A learned reconstruction core turns phone videos into queryable 3D scenes exposed to AI agents through MCP.
A learned reconstruction core turns phone videos into queryable 3D scenes exposed to AI agents through MCP.
Software license and creative AI use screened; complete installation, hardware, dependent-model terms and output-quality review pending. The offline demo is a simulator, not proof of reconstruction. BSD client/server code, VGGT-related components/weights, GPU deployment and hosted exports need separate review; scale is relative until calibrated.

- [Official README and creative workflow](https://github.com/reality-opened/openreality)
- [Reviewed software license](https://github.com/reality-opened/openreality/blob/main/LICENSE)
### ReelMimic · MIT

Agent orchestration analyzes a reference video and builds/reviews a new 2D animation with code-based drawing engines.
Agent orchestration analyzes a reference video and builds/reviews a new 2D animation with code-based drawing engines.
Software license and creative AI use screened; complete installation, hardware, dependent-model terms and output-quality review pending. Very young application; requires the user's Claude Code/Codex account and usage allowance. Engine dependencies, renderer requirements and long production times need a full profile.

- [Official README and creative workflow](https://github.com/edenfunf/reelmimic)
- [Reviewed software license](https://github.com/edenfunf/reelmimic/blob/main/LICENSE)
### Logo Design Skill · MIT

An agent workflow plus Python SVG audit/render/export tools supports AI-assisted identity design.
An agent workflow plus Python SVG audit/render/export tools supports AI-assisted identity design.
Software license and creative AI use screened; complete installation, hardware, dependent-model terms and output-quality review pending. An agent extension, not a standalone trained model. Required agent/service costs, reference-logo rights and generated-mark originality need review.

- [Official README and creative workflow](https://github.com/kaankiziltug/logo-design-skill)
- [Reviewed software license](https://github.com/kaankiziltug/logo-design-skill/blob/main/LICENSE)
### Motion Video Kit · MIT

An agent workflow combines AI-directed footage/motion design with code templates and render/audio quality-check scripts.
An agent workflow combines AI-directed footage/motion design with code templates and render/audio quality-check scripts.
Software license and creative AI use screened; complete installation, hardware, dependent-model terms and output-quality review pending. A skill/toolkit with an external AI agent, not autonomous local inference. Rendering stack, agent costs and original reference-film rights remain separate.

- [Official README and creative workflow](https://github.com/echris6/motion-video-kit)
- [Reviewed software license](https://github.com/echris6/motion-video-kit/blob/main/LICENSE)

## Excluded and unresolved findings

Research notes only; these do not enter the eligible tool library.

- **acids-ircam/RAVE** · excluded: Complete software license specifies CC-BY-NC-4.0; non-commercial code is outside the confirmed open-source-only eligibility rule. [Source](https://github.com/acids-ircam/RAVE/blob/master/LICENSE)
- **acids-ircam/nn_tilde** · excluded: Complete software license specifies CC-BY-NC-4.0; non-commercial code is outside the confirmed open-source-only eligibility rule. [Source](https://github.com/acids-ircam/nn_tilde/blob/master/LICENSE)
- **facebookresearch/co-tracker** · excluded: Complete software license specifies CC-BY-NC-4.0; non-commercial code is outside the confirmed open-source-only eligibility rule. [Source](https://github.com/facebookresearch/co-tracker/blob/main/LICENSE.md)
- **fishaudio/fish-speech** · excluded: Fish Audio Research License has custom research/commercial conditions; software is not approved under a recognized open-source license. [Source](https://github.com/fishaudio/fish-speech/blob/main/LICENSE)
- **Lightricks/LTX-2** · excluded: The current root and LTX-2.x licenses are custom Community License Agreements. This latest LTX home is not featured as OSI-licensed software. [Source](https://github.com/Lightricks/LTX-2/blob/main/LICENSE)
- **Sanster/IOPaint** · excluded: Repository is archived; retained for context rather than promoted as a maintained recommendation. [Source](https://github.com/Sanster/IOPaint/blob/main/LICENSE)
- **TencentARC/GFPGAN** · needs-license-review: GitHub classification is ambiguous/custom or the file contains multiple component terms. A complete software/dependency license determination is still pending; not an eligible screened lead. [Source](https://github.com/TencentARC/GFPGAN/blob/master/LICENSE)
- **TencentARC/BrushNet** · needs-license-review: GitHub classification is ambiguous/custom or the file contains multiple component terms. A complete software/dependency license determination is still pending; not an eligible screened lead. [Source](https://github.com/TencentARC/BrushNet/blob/main/LICENSE)
- **TMElyralab/MuseTalk** · needs-license-review: GitHub classification is ambiguous/custom or the file contains multiple component terms. A complete software/dependency license determination is still pending; not an eligible screened lead. [Source](https://github.com/TMElyralab/MuseTalk/blob/main/LICENSE)
- **w-okada/voice-changer** · needs-license-review: GitHub classification is ambiguous/custom or the file contains multiple component terms. A complete software/dependency license determination is still pending; not an eligible screened lead. [Source](https://github.com/w-okada/voice-changer/blob/master/LICENSE)
- **mmlab-cv/BlendAnything** · needs-license-review: GitHub classification is ambiguous/custom or the file contains multiple component terms. A complete software/dependency license determination is still pending; not an eligible screened lead. [Source](https://github.com/mmlab-cv/BlendAnything/blob/main/LICENSE)
- **Anjok07/ultimatevocalremovergui** · needs-license-review: GitHub metadata labels MIT, but the complete license endpoint was unavailable in the snapshot. Metadata alone does not satisfy the complete-license evidence requirement. [Source](https://github.com/Anjok07/ultimatevocalremovergui)
- **ashawkey/LGM** · needs-license-review: Supplementary primary-source fetch failed; software license and complete creative workflow could not be verified. It stays outside the public tool library. [Source](https://github.com/ashawkey/LGM)
- **nihui/realesrgan-ncnn-vulkan** · needs-license-review: Supplementary primary-source fetch failed; software license and complete creative workflow could not be verified. It stays outside the public tool library. [Source](https://github.com/nihui/realesrgan-ncnn-vulkan)
- **tintwotin/blender_ai** · needs-license-review: Supplementary primary-source fetch failed; software license and complete creative workflow could not be verified. It stays outside the public tool library. [Source](https://github.com/tintwotin/blender_ai)
- **KyaniteLabs/liminal** · needs-license-review: Supplementary primary-source fetch failed; software license and complete creative workflow could not be verified. It stays outside the public tool library. [Source](https://github.com/KyaniteLabs/liminal)

Source collection completed: 2026-10-01T21:42:59.319882+00:00
Search is a bounded sample. Stars and recent pushes are discovery signals, not verified quality or meaningful upgrades.
