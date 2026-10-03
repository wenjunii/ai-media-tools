# AI Media Scout — 2026-10-03

Today's expanded edition contains 32 detailed guides, including three meaningful release updates and 16 completions from the earlier review queue, plus 51 additional screened discoveries. New baseline guides range from tactile synthesis and robotic painting to local audio, neural scenes, accessible media and agent-authored animation. Krita's new prerelease changes host requirements and warns of poor macOS performance. All 215 planned repository queries and 14 model-task queries ran across 34 fields; 95 repository searches remain bounded, and Codeberg/SourceHut have explicit web-access gaps. Raw candidates are not approved tools. Every featured software license was reviewed; restricted model weights and paid/proprietary dependencies are called out separately. No discovered software was installed or executed.

Documentation reviewed today. Tools are not hands-on tested unless explicitly stated. Requirements and performance remain source-specific.

## Coverage

| Field | Finding |
| --- | --- |
| Images & design | Krita has a consequential Krita 6/Qt6 prerelease and an explicit macOS performance warning. OpenPencil and SD.Next add distinct editable-design and local-generation routes; no tool was installed. [Source 1](https://docs.interstice.cloud/installation/) [Source 2](https://openpencil.dev/) |
| Video, animation & film | PotionUI adds hosted image/video options and reusable presets; HyperFrames offers code-authored video, while ArcReel/Jellyfish organize multi-shot production. Hosted models retain separate terms. [Source 1](https://potionui.com/docs) [Source 2](https://hyperframes.heygen.com/quickstart) |
| Audio, music & voice | MLX Audio provides an Apple Silicon route, Resonant supplies a separate desktop workflow, and YuE2-Turbo is retained as a lead with non-commercial weight terms clearly separated from its software license. [Source 1](https://pypi.org/project/mlx-audio/) [Source 2](https://github.com/NoizAI/YuE2-Turbo) |
| 3D, reconstruction & assets | PartCrafter produces decomposable mesh parts; LichtFeld and Efficient Gaussian Appearance cover neural scene training/viewing. CAD, meshes and Gaussian splats have different downstream uses. [Source 1](https://wgsxm.github.io/projects/partcrafter/) [Source 2](https://fhahlbohm.github.io/efficient-gaussian-appearance/) |
| Browser tools & web media | OpenPencil, OpenSubs and browser scene/viewer tools broaden browser-based creation. A web interface does not establish CPU-only inference or native support on every operating system. [Source 1](https://openpencil.dev/) [Source 2](https://opensubs.app/) |
| WebXR, VR & AR | XRBlocks primary research and HapticGen extend the search to spatial interaction and tactile authoring. No new general-purpose WebXR runtime was sufficiently verified for a full profile today. [Source 1](https://www.duruofei.com/papers/Li_XRBlocks-AcceleratingHuman-centeredAI%2BXRInnovation_2025.pdf) [Source 2](https://hapticgen.hcitech.org/) |
| Computational art & creative coding | HyperFrames, Neural Fourier Shift and Ghost Arcade connect AI authoring to programmable motion, audio or shaders. Their deterministic rendering steps should not be confused with neural inference. [Source 1](https://hyperframes.heygen.com/showcase) [Source 2](https://ghostarcade.live/) |
| Interactive, immersive & live media | Ghost Arcade and OpenVJ support live visual creation; Riso Windowseat is retained for its agent-assisted interactive scene workflow. Show reliability remains untested. [Source 1](https://ghostarcade.live/) [Source 2](https://github.com/sevenevesai/riso-windowseat) |
| 3D printing & generative CAD | PartCrafter and KimCAD merit follow-up for editable parts and CAD scripting. Mesh export alone does not establish watertightness, manufacturing tolerances or printing readiness. [Source 1](https://wgsxm.github.io/projects/partcrafter/) [Source 2](https://github.com/scottconverse/KimCadClaude) |
| Games & production pipelines | Sprite Studio and part-aware 3D tools offer distinct character and prop pipelines. Small game-asset and agent tools were inspected beyond the automatic README shortlist. [Source 1](https://wgsxm.github.io/projects/partcrafter/) [Source 2](https://github.com/JohnKinyanjui/sprite-maker) |
| Motion capture & character animation | Motion-transfer scripts, Pixel2Motion and the FloodDiffusion 2 dance lead span body motion and graphic animation. The FloodDiffusion project site was inaccessible; its released README remains the concrete lead evidence. [Source 1](https://nolangz.github.io/pixel2motion/) [Source 2](https://github.com/AlayaLab/FloodDiffusion2) |
| Avatars, digital humans & lip sync | LatentSync remains a newly screened lip-sync lead; its 1.6 model card specifies OpenRAIL++ weights, separate from Apache software. PersonaLive is held for conflicting academic-use wording. [Source 1](https://huggingface.co/ByteDance/LatentSync-1.6) |
| VFX, compositing & relighting | MMagic and Robust Video Matting cover restoration, synthesis and foreground extraction. Model-specific setup, temporal artifacts and checkpoints still need individual scrutiny. [Source 1](https://mmagic.readthedocs.io/en/latest/) |
| Spatial audio & volumetric media | Neural Acoustic Fields models room impulse responses; Gaussian appearance research supplies a separate volumetric visual route. Neither implies a ready-made immersive authoring suite. [Source 1](https://www.andrew.cmu.edu/user/afluo/Neural_Acoustic_Fields/) [Source 2](https://fhahlbohm.github.io/efficient-gaussian-appearance/) |
| Photogrammetry, scanning & neural rendering | LichtFeld and Efficient Gaussian Appearance provide neural reconstruction workflows; CVAT adds reviewed model-assisted annotation for footage and point clouds. [Source 1](https://fhahlbohm.github.io/efficient-gaussian-appearance/) [Source 2](https://docs.cvat.ai/docs/administration/community/basics/installation/) |
| Editing, captions & post-production | VideoCaptioner receives a detailed guide; OpenSubs and several transcription/dubbing projects enter the pending queue. Local recognition and hosted translation paths are distinguished. [Source 1](https://weifeng2333.github.io/VideoCaptioner/) [Source 2](https://opensubs.app/) |
| Vector graphics, illustration & textures | Pixel2Motion makes editable animated SVG from reference logos; OpenPencil supports editable design nodes. VecFusion is held because a complete software license was not found. [Source 1](https://nolangz.github.io/pixel2motion/) [Source 2](https://openpencil.dev/) |
| Typography, fonts & layout | Koharu covers translated text placement in images; Pixel2Motion and HyperFrames extend the scope to animated lettering. No new font-generation package cleared a complete profile today. [Source 1](https://koharu.rs/en/installation) [Source 2](https://hyperframes.heygen.com/showcase) |
| Storyboarding, narrative & comics | ArcReel, Jellyfish and BeefTV offer shot/asset organization, while narrative and comic tools are retained as screened leads. Generated character consistency has not been hands-on verified. [Source 1](https://arc-reel.com/en/) [Source 2](https://docs.arc-reel.com/guide/getting-started/) |
| Creative publishing & presentation | HyperFrames provides reusable explainer/presentation compositions, and AI-assisted writing/story tools broaden the pending library. Exported media and fonts keep their own rights. [Source 1](https://hyperframes.heygen.com/showcase) [Source 2](https://openpencil.dev/) |
| Photography, restoration & color | SD.Next and Krita provide established image-editing routes. OmaStudio is a provisional lead: reviewed code uses a remote AI decision client with a heuristic offline fallback, so the advertised offline AI should not be read as neural inference. [Source 1](https://vladmandic.github.io/sdnext-docs/Installation/) [Source 2](https://github.com/ozdil/omarchy-omastudio/blob/master/src/ai/jev.rs) |
| Data art & scientific visualization | Data Formulator is screened for model-assisted visual data transformation, while HyperFrames provides animated chart/explainer output. Generic dashboards without concrete creative AI were not admitted. [Source 1](https://hyperframes.heygen.com/showcase) [Source 2](https://github.com/microsoft/data-formulator) |
| Physical, robotic & kinetic installations | FRIDA/CoFRIDA adds physical human-robot painting to the library; Ghost Arcade addresses projection-based installation. Robot simulation and safe hardware integration are separate from reading the documentation. [Source 1](https://pschaldenbrand.github.io/cofrida/) [Source 2](https://ghostarcade.live/) |
| Performance, projection & stage media | Ghost Arcade, OpenVJ and Neural Fourier Shift broaden live visual and sound performance. Native output integrations and hardware requirements vary by platform and version. [Source 1](https://ghostarcade.live/download) [Source 2](https://github.com/jin-woo-lee/nfs-binaural) |
| Fashion, textiles & wearable media | FASHN VTON 1.5 and OpenTryOn were inspected through primary sources. Neither enters the eligible additions today: FASHN needs license-text clarification, and OpenTryOn software is non-commercial. [Source 1](https://fashn.ai/blog/fashn-vton-1-5-open-source-release) [Source 2](https://github.com/tryonlabs/opentryon) |
| Accessible media & assistive creation | Microsoft AI Audio Descriptions supplies a detailed guide, and OpenSubs/EmDash AI Alt Text add captioning and image-description leads. Accessibility output still needs human review. [Source 1](https://opensubs.app/) [Source 2](https://github.com/DavidPivert/emdash-plugin-ai-alt-text) |
| Mobile, edge & on-device creation | OnDevice LLM documents iPhone vision, speech and image-generation surfaces. Its current site says public sideload downloads have retired and App Store availability is forthcoming; source access is not a currently available store release. [Source 1](https://mesutcydev.github.io/ios-local-llm/) |
| Creative learning & authoring | HyperFrames and vistep support AI-authored visual explanations; CVAT can help prepare media datasets. Published example scenes may be deterministic even when their authoring workflow uses an agent. [Source 1](https://hyperframes.heygen.com/quickstart) [Source 2](https://github.com/int64ago/vistep) |
| Archives, media restoration & collections | MMagic, restoration interfaces and transcription leads cover media restoration and searchable records. Enhancement may invent detail; archival originals should be retained. [Source 1](https://mmagic.readthedocs.io/en/latest/) |
| Emerging & cross-disciplinary creative AI | The added haptic, acoustic, agent-media and kinetic-type fields surface creative practices beyond image/video generators. Research prototypes, installable applications and agent toolkits are labeled separately. [Source 1](https://hapticgen.hcitech.org/) [Source 2](https://pschaldenbrand.github.io/cofrida/) |
| Tactile, vibration and haptic media | HapticGen supplies text-to-vibration research and a study application. Its MIT code and non-commercial model weights are distinct; placeholder deployment paths prevent a turnkey install claim. [Source 1](https://hapticgen.hcitech.org/) |
| Neural acoustics and responsive sound spaces | Neural Acoustic Fields offers source and datasets for learned spatial sound response. Its older environment and experimental integrations need deliberate reproduction work. [Source 1](https://www.andrew.cmu.edu/user/afluo/Neural_Acoustic_Fields/) |
| AI agents for code-authored media production | HyperFrames, AIMO, LEAP and multiple scene/video toolkits let an AI coding agent manipulate editable media structures. The agent service and any proprietary host remain separate dependencies. [Source 1](https://hyperframes.heygen.com/quickstart) [Source 2](https://arc-reel.com/en/) |
| AI kinetic typography and animated lettering | HyperFrames and Pixel2Motion provide reusable kinetic text/logo workflows. Their published examples are evidence of intended capability, not an independent assessment of output quality. [Source 1](https://hyperframes.heygen.com/showcase) [Source 2](https://nolangz.github.io/pixel2motion/) |

## Search and review counts

34 creative fields; 215/215 repository queries attempted; 14/14 model-task queries attempted. 19218 distinct source candidates and 660 model leads. 32 detailed profiles and 51 additional screened discoveries. Source gaps: 0 failed repository queries, 0 partial repository queries, 95 bounded repository queries, 0 failed model-task queries and 2 web ecosystem gaps. Raw search candidates include duplicates of known tools, excluded projects and projects awaiting review; they are not verified recommendations.

## Research beyond GitHub

- **gitlab** · searched: Reviewed Sonic Visions on GitLab: its AI-created artwork-to-MIDI workflow is interesting, but the converter itself does not establish concrete AI functionality, so it was not added as an AI tool. [Source](https://gitlab.com/mellotanica/sonic_visions)
- **codeberg** · gap: Live Codeberg searches/pages were blocked by robots restrictions. No candidate or license was verified there; this is an explicit ecosystem gap.
- **sourcehut** · gap: Targeted SourceHut searches were blocked or returned no inspectable relevant primary project. A generic host homepage would not establish creative-AI coverage.
- **packages** · searched: Checked the MLX Audio PyPI package and project documentation. Also inspected neural-tilde; its non-commercial software license prevents eligible inclusion. [Source](https://pypi.org/project/mlx-audio/) [Source](https://pypi.org/project/neural-tilde/)
- **creative-plugins** · searched: Reviewed Krita installation and the new host-version-specific release, Blender Dream Textures and ComfyUI extensions. Proprietary host and model terms remain separate. [Source](https://docs.interstice.cloud/installation/) [Source](https://github.com/carson-katri/dream-textures)
- **project-sites** · searched: Read primary demos and setup pages for HapticGen, Ghost Arcade, PartCrafter, Koharu, HyperFrames and others, supplementing repository results. [Source](https://hapticgen.hcitech.org/) [Source](https://ghostarcade.live/download) [Source](https://wgsxm.github.io/projects/partcrafter/)
- **research-code** · searched: Paired FRIDA/CoFRIDA and Neural Acoustic Fields research pages with released code and complete software licenses. A paper or demo alone was insufficient for inclusion. [Source](https://pschaldenbrand.github.io/cofrida/) [Source](https://www.andrew.cmu.edu/user/afluo/Neural_Acoustic_Fields/)
- **international** · searched: Reviewed Chinese ArcReel and VideoCaptioner documentation, multilingual Koharu, and Chinese short-drama/agent toolkits. Installation/platform claims were taken from the actual sources. [Source](https://docs.arc-reel.com/guide/getting-started/) [Source](https://weifeng2333.github.io/VideoCaptioner/) [Source](https://koharu.rs/en/installation)

## Collection limitations

- images: bounded or incomplete query: topic:diffusion pushed:>=2026-09-03 is:public fork:false archived:false (200 of 204 matches sampled)
- images: bounded or incomplete query: topic:diffusion is:public fork:false archived:false (200 of 1419 matches sampled)
- images: bounded or incomplete query: AI image generation pushed:>=2026-09-03 is:public fork:false archived:false (200 of 1619 matches sampled)
- images: bounded or incomplete query: AI image generation created:>=2026-09-03 is:public fork:false archived:false (200 of 805 matches sampled)
- images: bounded or incomplete query: AI image generation is:public fork:false archived:false (200 of 15275 matches sampled)
- video: bounded or incomplete query: AI video pushed:>=2026-09-03 is:public fork:false archived:false (200 of 12182 matches sampled)
- video: bounded or incomplete query: AI video created:>=2026-09-03 is:public fork:false archived:false (200 of 7708 matches sampled)
- video: bounded or incomplete query: AI video is:public fork:false archived:false (200 of 82067 matches sampled)
- video: bounded or incomplete query: topic:video-generation pushed:>=2026-09-03 is:public fork:false archived:false (200 of 1473 matches sampled)
- video: bounded or incomplete query: topic:video-generation created:>=2026-09-03 is:public fork:false archived:false (200 of 563 matches sampled)
- video: bounded or incomplete query: topic:video-generation is:public fork:false archived:false (200 of 3763 matches sampled)
- audio: bounded or incomplete query: topic:music-generation pushed:>=2026-09-03 is:public fork:false archived:false (200 of 289 matches sampled)
- audio: bounded or incomplete query: topic:music-generation is:public fork:false archived:false (500 of 1168 matches sampled)
- audio: bounded or incomplete query: AI audio pushed:>=2026-09-03 is:public fork:false archived:false (200 of 3706 matches sampled)
- audio: bounded or incomplete query: AI audio created:>=2026-09-03 is:public fork:false archived:false (200 of 1997 matches sampled)
- audio: bounded or incomplete query: AI audio is:public fork:false archived:false (200 of 27407 matches sampled)
- 3d: bounded or incomplete query: 3D generation pushed:>=2026-09-03 is:public fork:false archived:false (200 of 667 matches sampled)
- 3d: bounded or incomplete query: 3D generation created:>=2026-09-03 is:public fork:false archived:false (200 of 363 matches sampled)
- 3d: bounded or incomplete query: 3D generation is:public fork:false archived:false (200 of 5736 matches sampled)
- 3d: bounded or incomplete query: topic:3d-reconstruction pushed:>=2026-09-03 is:public fork:false archived:false (200 of 252 matches sampled)
- 3d: bounded or incomplete query: topic:3d-reconstruction is:public fork:false archived:false (200 of 1899 matches sampled)
- web: bounded or incomplete query: topic:webgpu pushed:>=2026-09-03 is:public fork:false archived:false (200 of 1002 matches sampled)
- web: bounded or incomplete query: topic:webgpu created:>=2026-09-03 is:public fork:false archived:false (200 of 402 matches sampled)
- web: bounded or incomplete query: topic:webgpu is:public fork:false archived:false (200 of 2752 matches sampled)
- xr: bounded or incomplete query: AI VR pushed:>=2026-09-03 is:public fork:false archived:false (200 of 326 matches sampled)
- xr: bounded or incomplete query: AI VR is:public fork:false archived:false (200 of 2828 matches sampled)
- computational: bounded or incomplete query: AI creative coding is:public fork:false archived:false (200 of 910 matches sampled)
- computational: bounded or incomplete query: topic:generative-art pushed:>=2026-09-03 is:public fork:false archived:false (200 of 779 matches sampled)
- computational: bounded or incomplete query: topic:generative-art created:>=2026-09-03 is:public fork:false archived:false (200 of 365 matches sampled)
- computational: bounded or incomplete query: topic:generative-art is:public fork:false archived:false (200 of 3798 matches sampled)
- interactive: bounded or incomplete query: AI interactive art is:public fork:false archived:false (200 of 668 matches sampled)
- fabrication: bounded or incomplete query: AI CAD pushed:>=2026-09-03 is:public fork:false archived:false (200 of 657 matches sampled)
- fabrication: bounded or incomplete query: AI CAD created:>=2026-09-03 is:public fork:false archived:false (200 of 367 matches sampled)
- fabrication: bounded or incomplete query: AI CAD is:public fork:false archived:false (200 of 2953 matches sampled)
- fabrication: bounded or incomplete query: AI 3D printing is:public fork:false archived:false (200 of 337 matches sampled)
- gaming: bounded or incomplete query: AI game assets is:public fork:false archived:false (200 of 625 matches sampled)
- gaming: bounded or incomplete query: AI blender pushed:>=2026-09-03 is:public fork:false archived:false (200 of 397 matches sampled)
- gaming: bounded or incomplete query: AI blender created:>=2026-09-03 is:public fork:false archived:false (200 of 287 matches sampled)
- gaming: bounded or incomplete query: AI blender is:public fork:false archived:false (200 of 1497 matches sampled)
- motion: bounded or incomplete query: AI motion capture is:public fork:false archived:false (200 of 229 matches sampled)
- motion: bounded or incomplete query: motion generation is:public fork:false archived:false (200 of 1482 matches sampled)
- avatars: bounded or incomplete query: AI avatar pushed:>=2026-09-03 is:public fork:false archived:false (200 of 736 matches sampled)
- avatars: bounded or incomplete query: AI avatar created:>=2026-09-03 is:public fork:false archived:false (200 of 396 matches sampled)
- avatars: bounded or incomplete query: AI avatar is:public fork:false archived:false (200 of 5809 matches sampled)
- avatars: bounded or incomplete query: lip sync pushed:>=2026-09-03 is:public fork:false archived:false (200 of 278 matches sampled)
- avatars: bounded or incomplete query: lip sync is:public fork:false archived:false (200 of 2359 matches sampled)
- vfx: bounded or incomplete query: AI visual effects is:public fork:false archived:false (200 of 411 matches sampled)
- capture: bounded or incomplete query: topic:gaussian-splatting pushed:>=2026-09-03 is:public fork:false archived:false (200 of 232 matches sampled)
- capture: bounded or incomplete query: topic:gaussian-splatting is:public fork:false archived:false (500 of 892 matches sampled)
- capture: bounded or incomplete query: neural reconstruction is:public fork:false archived:false (200 of 1309 matches sampled)
- editing: bounded or incomplete query: AI video editing pushed:>=2026-09-03 is:public fork:false archived:false (200 of 791 matches sampled)
- editing: bounded or incomplete query: AI video editing created:>=2026-09-03 is:public fork:false archived:false (200 of 492 matches sampled)
- editing: bounded or incomplete query: AI video editing is:public fork:false archived:false (200 of 3331 matches sampled)
- editing: bounded or incomplete query: AI subtitle pushed:>=2026-09-03 is:public fork:false archived:false (200 of 364 matches sampled)
- editing: bounded or incomplete query: AI subtitle is:public fork:false archived:false (200 of 2182 matches sampled)
- vector: bounded or incomplete query: AI SVG pushed:>=2026-09-03 is:public fork:false archived:false (200 of 426 matches sampled)
- vector: bounded or incomplete query: AI SVG created:>=2026-09-03 is:public fork:false archived:false (200 of 236 matches sampled)
- vector: bounded or incomplete query: AI SVG is:public fork:false archived:false (200 of 1738 matches sampled)
- typography: bounded or incomplete query: AI typography is:public fork:false archived:false (200 of 637 matches sampled)
- typography: bounded or incomplete query: font generation is:public fork:false archived:false (400 of 415 matches sampled)
- storytelling: bounded or incomplete query: AI storyboard pushed:>=2026-09-03 is:public fork:false archived:false (200 of 355 matches sampled)
- storytelling: bounded or incomplete query: AI storyboard created:>=2026-09-03 is:public fork:false archived:false (200 of 203 matches sampled)
- storytelling: bounded or incomplete query: AI storyboard is:public fork:false archived:false (200 of 1635 matches sampled)
- storytelling: bounded or incomplete query: AI comic pushed:>=2026-09-03 is:public fork:false archived:false (200 of 1537 matches sampled)
- storytelling: bounded or incomplete query: AI comic created:>=2026-09-03 is:public fork:false archived:false (200 of 1452 matches sampled)
- storytelling: bounded or incomplete query: AI comic is:public fork:false archived:false (200 of 2794 matches sampled)
- publishing: bounded or incomplete query: AI presentation pushed:>=2026-09-03 is:public fork:false archived:false (200 of 1083 matches sampled)
- publishing: bounded or incomplete query: AI presentation created:>=2026-09-03 is:public fork:false archived:false (200 of 669 matches sampled)
- publishing: bounded or incomplete query: AI presentation is:public fork:false archived:false (200 of 8362 matches sampled)
- publishing: bounded or incomplete query: AI publishing pushed:>=2026-09-03 is:public fork:false archived:false (200 of 1047 matches sampled)
- publishing: bounded or incomplete query: AI publishing created:>=2026-09-03 is:public fork:false archived:false (200 of 642 matches sampled)
- publishing: bounded or incomplete query: AI publishing is:public fork:false archived:false (200 of 3951 matches sampled)
- photography: bounded or incomplete query: AI colorization pushed:>=2026-09-03 is:public fork:false archived:false (200 of 433 matches sampled)
- photography: bounded or incomplete query: AI colorization created:>=2026-09-03 is:public fork:false archived:false (200 of 271 matches sampled)
- photography: bounded or incomplete query: AI colorization is:public fork:false archived:false (200 of 4675 matches sampled)
- visualization: bounded or incomplete query: AI visualization pushed:>=2026-09-03 is:public fork:false archived:false (200 of 3247 matches sampled)
- visualization: bounded or incomplete query: AI visualization created:>=2026-09-03 is:public fork:false archived:false (200 of 1869 matches sampled)
- visualization: bounded or incomplete query: AI visualization is:public fork:false archived:false (200 of 37383 matches sampled)
- visualization: bounded or incomplete query: AI data art is:public fork:false archived:false (200 of 1013 matches sampled)
- performance: bounded or incomplete query: AI live visuals is:public fork:false archived:false (200 of 696 matches sampled)
- fashion: bounded or incomplete query: AI fashion design is:public fork:false archived:false (200 of 632 matches sampled)
- fashion: bounded or incomplete query: AI textile is:public fork:false archived:false (200 of 458 matches sampled)
- accessibility: bounded or incomplete query: AI audio description is:public fork:false archived:false (200 of 251 matches sampled)
- mobile: bounded or incomplete query: AI mobile media is:public fork:false archived:false (200 of 206 matches sampled)
- education: bounded or incomplete query: AI explainer pushed:>=2026-09-03 is:public fork:false archived:false (200 of 6466 matches sampled)
- education: bounded or incomplete query: AI explainer created:>=2026-09-03 is:public fork:false archived:false (200 of 4470 matches sampled)
- education: bounded or incomplete query: AI explainer is:public fork:false archived:false (200 of 36205 matches sampled)
- frontier: bounded or incomplete query: AI creative tools pushed:>=2026-09-03 is:public fork:false archived:false (200 of 232 matches sampled)
- frontier: bounded or incomplete query: AI creative tools is:public fork:false archived:false (200 of 1927 matches sampled)
- frontier: bounded or incomplete query: AI digital art is:public fork:false archived:false (200 of 714 matches sampled)
- frontier: bounded or incomplete query: AI multimedia is:public fork:false archived:false (200 of 1159 matches sampled)
- frontier: bounded or incomplete query: AI new media is:public fork:false archived:false (200 of 500 matches sampled)
- neural-acoustics: bounded or incomplete query: neural acoustic is:public fork:false archived:false (200 of 340 matches sampled)
- agent-media-production: bounded or incomplete query: AI agent animation is:public fork:false archived:false (200 of 492 matches sampled)
- agent-media-production: bounded or incomplete query: AI agent video editing is:public fork:false archived:false (200 of 416 matches sampled)

## Generative AI for Krita

Images & design · Photography, restoration & color · Vector graphics, illustration & textures

v1.54.0-pre, published October 3, migrates to Krita 6/Qt6 and adds Qwen Image 2.1 support. It no longer supports Krita 5.x, is not extensively tested and is explicitly reported to perform poorly on macOS.

### How it uses AI

A Krita plugin integrates diffusion generation and guided editing with painting layers, masks and selections. Creative use: Revise selected areas of an illustration while retaining manual painting control. [Source](https://github.com/Acly/krita-ai-diffusion) [Source](https://docs.interstice.cloud/installation/) [Source](https://github.com/Acly/krita-ai-diffusion/releases/tag/v1.54.0-pre)

### Introduction

A Krita plugin integrates diffusion generation and guided editing with painting layers, masks and selections. [Source 1](https://github.com/Acly/krita-ai-diffusion) [Source 2](https://docs.interstice.cloud/installation/) [Source 3](https://github.com/Acly/krita-ai-diffusion/releases/tag/v1.54.0-pre)

### What it is good for

Revise selected areas of an illustration while retaining manual painting control. [Source 1](https://github.com/Acly/krita-ai-diffusion) [Source 2](https://docs.interstice.cloud/installation/) [Source 3](https://github.com/Acly/krita-ai-diffusion/releases/tag/v1.54.0-pre)

### Demo & examples

The official handbook and README link installation, live-painting videos and a gallery. [Source 1](https://github.com/Acly/krita-ai-diffusion) [Source 2](https://docs.interstice.cloud/installation/) [Source 3](https://github.com/Acly/krita-ai-diffusion/releases/tag/v1.54.0-pre)

### Install

Follow the reviewed project route below; these steps are documentation guidance and were not executed. [Source 1](https://github.com/Acly/krita-ai-diffusion) [Source 2](https://docs.interstice.cloud/installation/) [Source 3](https://github.com/Acly/krita-ai-diffusion/releases/tag/v1.54.0-pre)

1. Choose a plugin release compatible with your Krita major version. Today's v1.54.0-pre explicitly requires Krita 6; its notes recommend 6.0.4.
2. Import the official plugin ZIP through Krita's Python Plugin menu and restart.
3. Enable AI Image Generation, then configure a managed local, custom ComfyUI or optional online backend.
### First project

A small first project that exercises the documented creative workflow. [Source 1](https://github.com/Acly/krita-ai-diffusion) [Source 2](https://docs.interstice.cloud/installation/) [Source 3](https://github.com/Acly/krita-ai-diffusion/releases/tag/v1.54.0-pre)

1. Duplicate a small sketch layer and select one region.
2. Generate a controlled variation and inspect edges/composition.
3. Accept useful layers selectively, keeping the original painting available.
### Hardware & software

Requirements are source-specific. Unreported capacities and untested platforms are not inferred. [Source 1](https://github.com/Acly/krita-ai-diffusion) [Source 2](https://docs.interstice.cloud/installation/) [Source 3](https://github.com/Acly/krita-ai-diffusion/releases/tag/v1.54.0-pre)

- **Hardware:** README recommends at least 6 GB NVIDIA VRAM for local generation; official docs list Intel Arc 8 GB+, ROCm-compatible AMD and Apple Silicon. Model storage starts at 10 GB and can exceed 50 GB. System RAM minimum is undocumented.
- **Software:** For v1.54.0-pre: Krita 6/Qt6 and a compatible ComfyUI backend; macOS MPS route needs macOS 14+. Older stable documentation still names Krita 5.2+.
- **Platforms:** Windows/Linux GPU routes and macOS Apple Silicon are documented, but the new prerelease has a specific macOS performance warning. CPU inference is very slow.

### License, model weights & costs

The complete software license was archived and reviewed. Keep software, model weights, dependencies and hosted-service terms separate. [Source 1](https://github.com/Acly/krita-ai-diffusion/blob/main/LICENSE) [Source 2](https://github.com/Acly/krita-ai-diffusion) [Source 3](https://docs.interstice.cloud/installation/) [Source 4](https://github.com/Acly/krita-ai-diffusion/releases/tag/v1.54.0-pre)

- **Code:** GPL-3.0
- **Weights:** GPL-3.0 plugin; checkpoints, LoRAs and auxiliary models retain their own terms.
- **Commercial:** The reviewed GPL-3.0 software license permits commercial use subject to its license, notice and source-sharing obligations where applicable. This does not establish permission for every model, input, output or service.
- **Cost:** Local compute/storage or optional paid cloud generation.

### Why it merits attention

The update adds a concrete model and host-version migration, making compatibility review more useful than a generic upgrade recommendation. [Source 1](https://github.com/Acly/krita-ai-diffusion) [Source 2](https://docs.interstice.cloud/installation/) [Source 3](https://github.com/Acly/krita-ai-diffusion/releases/tag/v1.54.0-pre)

### Limitations

Do not infer compatibility from the generic install guide: it still says Krita 6 support comes with 2.x, while this prerelease is named 1.54.0-pre. Follow release-specific requirements. This edition is a documentation review, not an installation or output-quality test. [Source 1](https://github.com/Acly/krita-ai-diffusion) [Source 2](https://docs.interstice.cloud/installation/) [Source 3](https://github.com/Acly/krita-ai-diffusion/releases/tag/v1.54.0-pre)

### Get the tool

- [Repository](https://github.com/Acly/krita-ai-diffusion)
- [License](https://github.com/Acly/krita-ai-diffusion/blob/main/LICENSE)
- [Documentation](https://docs.interstice.cloud/installation/)

## PotionUI

Images & design · Video, animation & film · Audio, music & voice · Editing, captions & post-production

v0.0.14, published October 2 after the prior observation, adds OpenRouter image/video backends, a layered image editor, reusable preset formulas and Qwen-Image 2.1 control/inpainting workflows.

### How it uses AI

A self-hosted AI studio gives multiple users model-specific forms, presets, generation history and media organization. Creative use: Share a local GPU or configured worker while keeping creator-facing controls simpler than node graphs. [Source](https://github.com/PotionUI/PotionUI) [Source](https://potionui.com/docs) [Source](https://github.com/PotionUI/PotionUI/releases/tag/v0.0.14)

### Introduction

A self-hosted AI studio gives multiple users model-specific forms, presets, generation history and media organization. [Source 1](https://github.com/PotionUI/PotionUI) [Source 2](https://potionui.com/docs) [Source 3](https://github.com/PotionUI/PotionUI/releases/tag/v0.0.14)

### What it is good for

Share a local GPU or configured worker while keeping creator-facing controls simpler than node graphs. [Source 1](https://github.com/PotionUI/PotionUI) [Source 2](https://potionui.com/docs) [Source 3](https://github.com/PotionUI/PotionUI/releases/tag/v0.0.14)

### Demo & examples

The official documentation includes a worked product study and the README links a 60-second tour. [Source 1](https://github.com/PotionUI/PotionUI) [Source 2](https://potionui.com/docs) [Source 3](https://github.com/PotionUI/PotionUI/releases/tag/v0.0.14)

### Install

Follow the reviewed project route below; these steps are documentation guidance and were not executed. [Source 1](https://github.com/PotionUI/PotionUI) [Source 2](https://potionui.com/docs) [Source 3](https://github.com/PotionUI/PotionUI/releases/tag/v0.0.14)

1. Back up existing alpha workspace data, then select the documented local, hybrid, remote-client or worker install profile.
2. Prepare Python 3.12 and Node 18+ (Node 20 for the native Windows route).
3. Run the project doctor/start commands. For the new hosted route, enable OpenRouter in Admin → Plugins and configure its API access.

```sh
./potionui doctor
```


```sh
./potionui start
```

### First project

A small first project that exercises the documented creative workflow. [Source 1](https://github.com/PotionUI/PotionUI) [Source 2](https://potionui.com/docs) [Source 3](https://github.com/PotionUI/PotionUI/releases/tag/v0.0.14)

1. Choose a permitted model/preset and generate a small sample.
2. Use the new image editor or reusable formula to revise the result.
3. For multi-shot video, review each shot and its possible provider cost before retrying.
### Hardware & software

Requirements are source-specific. Unreported capacities and untested platforms are not inferred. [Source 1](https://github.com/PotionUI/PotionUI) [Source 2](https://potionui.com/docs) [Source 3](https://github.com/PotionUI/PotionUI/releases/tag/v0.0.14)

- **Hardware:** Local SDXL floor: 8 GB VRAM and 16 GB RAM; larger families need more. Total model storage is not given universally. A remote CPU-only client is not CPU generation.
- **Software:** Python 3.12, Node 18+/20, CUDA stack for local generation; native Windows GPU route lists driver 580+. Hosted generation needs its selected provider.
- **Platforms:** Tested Linux x86_64/NVIDIA; native Windows experimental, WSL2 listed as expected but unverified, Docker documented. Native MPS/AMD local generation is unsupported.

### License, model weights & costs

The complete software license was archived and reviewed. Keep software, model weights, dependencies and hosted-service terms separate. [Source 1](https://github.com/PotionUI/PotionUI/blob/master/LICENSE) [Source 2](https://github.com/PotionUI/PotionUI) [Source 3](https://potionui.com/docs) [Source 4](https://github.com/PotionUI/PotionUI/releases/tag/v0.0.14)

- **Code:** GPL-3.0
- **Weights:** GPL-3.0 application; installed local weights and new hosted models/services have independent terms.
- **Commercial:** The reviewed GPL-3.0 software license permits commercial use subject to its license, notice and source-sharing obligations where applicable. This does not establish permission for every model, input, output or service.
- **Cost:** Local/worker GPU costs; OpenRouter and other hosted generation can bill separately, including requests that finish after cancellation.

### Why it merits attention

Layered editing and reusable settings are concrete workflow additions; model-access controls remain useful for shared hardware. [Source 1](https://github.com/PotionUI/PotionUI) [Source 2](https://potionui.com/docs) [Source 3](https://github.com/PotionUI/PotionUI/releases/tag/v0.0.14)

### Limitations

Alpha releases can break plugins/configuration. This release changes accepted plugin categories and Docker storage guidance; read its upgrade notes. This edition is a documentation review, not an installation or output-quality test. [Source 1](https://github.com/PotionUI/PotionUI) [Source 2](https://potionui.com/docs) [Source 3](https://github.com/PotionUI/PotionUI/releases/tag/v0.0.14)

### Get the tool

- [Repository](https://github.com/PotionUI/PotionUI)
- [License](https://github.com/PotionUI/PotionUI/blob/master/LICENSE)
- [Documentation](https://potionui.com/docs)

## BeefTV

Video, animation & film · Storyboarding, narrative & comics · Images & design · AI agents for code-authored media production

v1.7.2, published October 3, restores the Windows MCP CLI, fixes duplicate-window/runtime discovery issues and repairs assistant connections through custom model channels.

### How it uses AI

A local canvas workspace organizes model-driven text, images, video and audio as connected creative assets. Creative use: Develop and revise a storyboard or short-video concept while preserving references and generated assets. [Source](https://github.com/glanderness/BeefTV) [Source](https://github.com/glanderness/BeefTV/blob/main/QUICKSTART.md) [Source](https://github.com/glanderness/BeefTV/blob/main/NOTICE) [Source](https://github.com/glanderness/BeefTV/releases/tag/v1.7.2)

### Introduction

A local canvas workspace organizes model-driven text, images, video and audio as connected creative assets. [Source 1](https://github.com/glanderness/BeefTV) [Source 2](https://github.com/glanderness/BeefTV/blob/main/QUICKSTART.md) [Source 3](https://github.com/glanderness/BeefTV/blob/main/NOTICE) [Source 4](https://github.com/glanderness/BeefTV/releases/tag/v1.7.2)

### What it is good for

Develop and revise a storyboard or short-video concept while preserving references and generated assets. [Source 1](https://github.com/glanderness/BeefTV) [Source 2](https://github.com/glanderness/BeefTV/blob/main/QUICKSTART.md) [Source 3](https://github.com/glanderness/BeefTV/blob/main/NOTICE) [Source 4](https://github.com/glanderness/BeefTV/releases/tag/v1.7.2)

### Demo & examples

The README links a product walkthrough and the official site presents the desktop workflow. [Source 1](https://github.com/glanderness/BeefTV) [Source 2](https://github.com/glanderness/BeefTV/blob/main/QUICKSTART.md) [Source 3](https://github.com/glanderness/BeefTV/blob/main/NOTICE) [Source 4](https://github.com/glanderness/BeefTV/releases/tag/v1.7.2)

### Install

Follow the reviewed project route below; these steps are documentation guidance and were not executed. [Source 1](https://github.com/glanderness/BeefTV) [Source 2](https://github.com/glanderness/BeefTV/blob/main/QUICKSTART.md) [Source 3](https://github.com/glanderness/BeefTV/blob/main/NOTICE) [Source 4](https://github.com/glanderness/BeefTV/releases/tag/v1.7.2)

1. Download the official macOS or Windows release for the correct processor.
2. Follow QUICKSTART.md and create/open a local workspace.
3. Configure the chosen model channel. For source builds, provide Go 1.25, Bun and Wails platform components.
### First project

A small first project that exercises the documented creative workflow. [Source 1](https://github.com/glanderness/BeefTV) [Source 2](https://github.com/glanderness/BeefTV/blob/main/QUICKSTART.md) [Source 3](https://github.com/glanderness/BeefTV/blob/main/NOTICE) [Source 4](https://github.com/glanderness/BeefTV/releases/tag/v1.7.2)

1. Create several storyboard nodes and connect their references.
2. Generate or import one asset and revise that node.
3. Save the project and verify its local assets; test the corrected MCP connection if using an agent.
### Hardware & software

Requirements are source-specific. Unreported capacities and untested platforms are not inferred. [Source 1](https://github.com/glanderness/BeefTV) [Source 2](https://github.com/glanderness/BeefTV/blob/main/QUICKSTART.md) [Source 3](https://github.com/glanderness/BeefTV/blob/main/NOTICE) [Source 4](https://github.com/glanderness/BeefTV/releases/tag/v1.7.2)

- **Hardware:** RAM, VRAM and disk minimums are not documented. A local workspace does not imply that model inference runs locally.
- **Software:** Official desktop package plus configured provider access. Source builds use Go 1.25/Bun/Wails; Windows builds also require the documented GCC setup.
- **Platforms:** macOS Apple Silicon/Intel and Windows desktop packages; native Linux release support is not established in the reviewed overview.

### License, model weights & costs

The complete software license was archived and reviewed. Keep software, model weights, dependencies and hosted-service terms separate. [Source 1](https://github.com/glanderness/BeefTV/blob/main/LICENSE) [Source 2](https://github.com/glanderness/BeefTV) [Source 3](https://github.com/glanderness/BeefTV/blob/main/QUICKSTART.md) [Source 4](https://github.com/glanderness/BeefTV/blob/main/NOTICE) [Source 5](https://github.com/glanderness/BeefTV/releases/tag/v1.7.2)

- **Code:** MIT
- **Weights:** MIT workspace with retained upstream notices. Providers and bundled third-party components have separate terms.
- **Commercial:** The reviewed MIT software license permits commercial use subject to its license, notice and source-sharing obligations where applicable. This does not establish permission for every model, input, output or service.
- **Cost:** Local storage and optional model-provider charges.

### Why it merits attention

This release addresses concrete Windows agent-integration failures rather than merely changing a timestamp. [Source 1](https://github.com/glanderness/BeefTV) [Source 2](https://github.com/glanderness/BeefTV/blob/main/QUICKSTART.md) [Source 3](https://github.com/glanderness/BeefTV/blob/main/NOTICE) [Source 4](https://github.com/glanderness/BeefTV/releases/tag/v1.7.2)

### Limitations

The fixes are release-note claims, not hands-on validation. macOS packages remain unnotarized according to the quick start; provider connectivity is a separate dependency. This edition is a documentation review, not an installation or output-quality test. [Source 1](https://github.com/glanderness/BeefTV) [Source 2](https://github.com/glanderness/BeefTV/blob/main/QUICKSTART.md) [Source 3](https://github.com/glanderness/BeefTV/blob/main/NOTICE) [Source 4](https://github.com/glanderness/BeefTV/releases/tag/v1.7.2)

### Get the tool

- [Repository](https://github.com/glanderness/BeefTV)
- [License](https://github.com/glanderness/BeefTV/blob/main/LICENSE)
- [Documentation](https://github.com/glanderness/BeefTV/blob/main/QUICKSTART.md)

## LEAP MCP

Creative learning & authoring · Data art & scientific visualization · Video, animation & film · AI agents for code-authored media production

First detailed guide, completing an earlier screened lead. This is a documentation baseline, not a claim that the project launched today.

### How it uses AI

An MCP workflow that combines an AI-written lesson, OpenAI narration and Manim animations into a short educational video. Creative use: Draft a narrated science or art explainer with a hook, explanation and closing synthesis. [Source](https://github.com/sid-thephysicskid/leap-mcp)

### Introduction

An MCP workflow that combines an AI-written lesson, OpenAI narration and Manim animations into a short educational video. [Source 1](https://github.com/sid-thephysicskid/leap-mcp)

### What it is good for

Draft a narrated science or art explainer with a hook, explanation and closing synthesis. [Source 1](https://github.com/sid-thephysicskid/leap-mcp)

### Demo & examples

The README includes an animated demonstration and example lesson prompts; this review did not render a lesson. [Source 1](https://github.com/sid-thephysicskid/leap-mcp)

### Install

Follow the reviewed project route below; these steps are documentation guidance and were not executed. [Source 1](https://github.com/sid-thephysicskid/leap-mcp)

1. Use the documented Python 3.8–3.11 environment and install/sign in to Claude Code.
2. Clone the repository, review its setup.py, then follow the documented setup and configure an OpenAI API key locally.
3. Start Claude Code and confirm the leap-mcp connection through its MCP list.
### First project

A small first project that exercises the documented creative workflow. [Source 1](https://github.com/sid-thephysicskid/leap-mcp)

1. Request an explainer about a specific topic and audience.
2. Review the script and animation for factual accuracy before rendering.
3. Review the narration and final video before sharing.
### Hardware & software

Requirements are source-specific. Unreported capacities and untested platforms are not inferred. [Source 1](https://github.com/sid-thephysicskid/leap-mcp)

- **Hardware:** RAM, GPU/VRAM and disk minimums are not documented.
- **Software:** Python 3.8–3.11, Manim, FastMCP, Claude Code and an OpenAI API key. The README warns against Python 3.13+.
- **Platforms:** The README does not provide a tested Windows/macOS/Linux matrix; only Claude Code is currently supported as the client.

### License, model weights & costs

The complete software license was archived and reviewed. Keep software, model weights, dependencies and hosted-service terms separate. [Source 1](https://github.com/sid-thephysicskid/leap-mcp/blob/main/LICENSE) [Source 2](https://github.com/sid-thephysicskid/leap-mcp)

- **Code:** MIT
- **Weights:** No standalone model weights are supplied; narration and reasoning depend on external services.
- **Commercial:** The reviewed MIT software license permits commercial use subject to its license, notice and source-sharing obligations where applicable. This does not establish permission for every model, input, output or service.
- **Cost:** The source is MIT; Claude access and OpenAI API usage are separate costs.

### Why it merits attention

A concrete script-to-animation-to-narration pipeline and a published demo make this assessable as an experimental education workflow. [Source 1](https://github.com/sid-thephysicskid/leap-mcp)

### Limitations

Provider-dependent and not a self-contained local model. Other MCP clients and video-quality controls are listed as future work. This edition is a documentation review, not an installation or output-quality test. [Source 1](https://github.com/sid-thephysicskid/leap-mcp)

### Get the tool

- [Repository](https://github.com/sid-thephysicskid/leap-mcp)
- [License](https://github.com/sid-thephysicskid/leap-mcp/blob/main/LICENSE)

## Recursive Visual State Video

Video, animation & film · Computational art & creative coding · AI agents for code-authored media production

First detailed guide, completing an earlier screened lead. The repository was created in the current discovery window; this is a documentation baseline, not a verified launch date.

### How it uses AI

An agent workflow generates each image from the preceding frame, periodically reviews visual drift, and packages the sequence into a silent video. Creative use: Short fixed-camera motion studies and experiments in visual continuity from a natural-language brief. [Source](https://github.com/ouruocun-dotcom/recursive-visual-state-video)

### Introduction

An agent workflow generates each image from the preceding frame, periodically reviews visual drift, and packages the sequence into a silent video. [Source 1](https://github.com/ouruocun-dotcom/recursive-visual-state-video)

### What it is good for

Short fixed-camera motion studies and experiments in visual continuity from a natural-language brief. [Source 1](https://github.com/ouruocun-dotcom/recursive-visual-state-video)

### Demo & examples

The repository documents an 11-frame pilot, including softness, color and pose drift; this is a qualitative example, not a benchmark. [Source 1](https://github.com/ouruocun-dotcom/recursive-visual-state-video)

### Install

Follow the reviewed project route below; these steps are documentation guidance and were not executed. [Source 1](https://github.com/ouruocun-dotcom/recursive-visual-state-video)

1. Clone or download the repository and install the skills/recursive-visual-state-video folder in a compatible agent's skill mechanism.
2. Install Python 3 and Pillow; add FFmpeg if MP4 output is wanted.
3. Confirm that the agent's actual image tool accepts a prior local frame and produces real output files.
### First project

A small first project that exercises the documented creative workflow. [Source 1](https://github.com/ouruocun-dotcom/recursive-visual-state-video)

1. Specify scene, action, duration and frame rate.
2. Generate a recursive sequence, inspect periodic continuity checks and retain originals when repairing frames.
3. Validate frames, inspect the contact sheet and encode the optional silent MP4.
### Hardware & software

Requirements are source-specific. Unreported capacities and untested platforms are not inferred. [Source 1](https://github.com/ouruocun-dotcom/recursive-visual-state-video)

- **Hardware:** RAM, VRAM, disk and GPU minimums are not documented; image generation depends on the selected tool.
- **Software:** Compatible Codex/image tooling, Python 3, Pillow; FFmpeg is optional for video encoding.
- **Platforms:** No tested OS support matrix is published. Local utilities and the image-tool capability must be checked separately.

### License, model weights & costs

The complete software license was archived and reviewed. Keep software, model weights, dependencies and hosted-service terms separate. [Source 1](https://github.com/ouruocun-dotcom/recursive-visual-state-video/blob/main/LICENSE) [Source 2](https://github.com/ouruocun-dotcom/recursive-visual-state-video)

- **Code:** MIT
- **Weights:** No model weights are bundled. Image-tool terms apply independently.
- **Commercial:** The reviewed MIT software license permits commercial use subject to its license, notice and source-sharing obligations where applicable. This does not establish permission for every model, input, output or service.
- **Cost:** MIT workflow and scripts; image generation and agent access may incur service costs.

### Why it merits attention

The example explicitly records failed pose adherence and cumulative drift, making the workflow's limits inspectable. [Source 1](https://github.com/ouruocun-dotcom/recursive-visual-state-video)

### Limitations

Not a trained video model; repair can sharpen a wrong pose without correcting it. Long sequences can accumulate drift. This edition is a documentation review, not an installation or output-quality test. [Source 1](https://github.com/ouruocun-dotcom/recursive-visual-state-video)

### Get the tool

- [Repository](https://github.com/ouruocun-dotcom/recursive-visual-state-video)
- [License](https://github.com/ouruocun-dotcom/recursive-visual-state-video/blob/main/LICENSE)

## Oral Video Workflow

Editing, captions & post-production · Video, animation & film · Accessible media & assistive creation · AI agents for code-authored media production

First detailed guide, completing an earlier screened lead. The repository was created in the current discovery window; this is a documentation baseline, not a verified launch date.

### How it uses AI

An AI agent organizes a talking-head edit through planning, rough cut, visual design, production and delivery, with human review points. Creative use: Turn spoken-word footage into a designed short video while reviewing cuts, captions and supporting visuals. [Source](https://github.com/zoushunyu144000-ui/oral-video-workflow)

### Introduction

An AI agent organizes a talking-head edit through planning, rough cut, visual design, production and delivery, with human review points. [Source 1](https://github.com/zoushunyu144000-ui/oral-video-workflow)

### What it is good for

Turn spoken-word footage into a designed short video while reviewing cuts, captions and supporting visuals. [Source 1](https://github.com/zoushunyu144000-ui/oral-video-workflow)

### Demo & examples

The README supplies the workflow and workspace structure; it does not establish a tested public end-to-end demo. [Source 1](https://github.com/zoushunyu144000-ui/oral-video-workflow)

### Install

Follow the reviewed project route below; these steps are documentation guidance and were not executed. [Source 1](https://github.com/zoushunyu144000-ui/oral-video-workflow)

1. Download the repository and place skills/oral-video-workflow in the chosen agent's supported skill location.
2. Provide FFmpeg and a local or online transcription tool.
3. Configure the documented ChatCut Desktop MCP connection, or implement the editing-tool substitutions described by the author.
### First project

A small first project that exercises the documented creative workflow. [Source 1](https://github.com/zoushunyu144000-ui/oral-video-workflow)

1. Supply one source recording and the intended platform.
2. Review the proposed rough cut and visual treatment at the workflow's checkpoints.
3. Inspect captions, timing and the exported video before publishing.
### Hardware & software

Requirements are source-specific. Unreported capacities and untested platforms are not inferred. [Source 1](https://github.com/zoushunyu144000-ui/oral-video-workflow)

- **Hardware:** CPU, RAM, VRAM and storage requirements are not documented.
- **Software:** A file/command-capable AI agent, FFmpeg, transcription and an editing/export tool. Current examples use ChatCut Desktop MCP.
- **Platforms:** OS support is not specified and depends on the chosen agent and editor.

### License, model weights & costs

The complete software license was archived and reviewed. Keep software, model weights, dependencies and hosted-service terms separate. [Source 1](https://github.com/zoushunyu144000-ui/oral-video-workflow/blob/main/LICENSE) [Source 2](https://github.com/zoushunyu144000-ui/oral-video-workflow)

- **Code:** MIT
- **Weights:** No trained weights are included; transcription and agent-model terms are separate.
- **Commercial:** The reviewed MIT software license permits commercial use subject to its license, notice and source-sharing obligations where applicable. This does not establish permission for every model, input, output or service.
- **Cost:** MIT workflow; agent, transcription and editor services may require separate accounts or payment.

### Why it merits attention

Explicit review gates and reusable project/style records provide a useful production structure. [Source 1](https://github.com/zoushunyu144000-ui/oral-video-workflow)

### Limitations

This is an orchestration recipe, not an autonomous video editor. Chinese documentation and editor-specific integration need adaptation. This edition is a documentation review, not an installation or output-quality test. [Source 1](https://github.com/zoushunyu144000-ui/oral-video-workflow)

### Get the tool

- [Repository](https://github.com/zoushunyu144000-ui/oral-video-workflow)
- [License](https://github.com/zoushunyu144000-ui/oral-video-workflow/blob/main/LICENSE)

## mocap-skills

Motion capture & character animation · Avatars, digital humans & lip sync · Games & production pipelines · AI agents for code-authored media production

First detailed guide, completing an earlier screened lead. The repository was created in the current discovery window; this is a documentation baseline, not a verified launch date.

### How it uses AI

An AI coding assistant uses silhouette measurements and inverse kinematics to transfer side-view reference motion into a Blender rig; a separate utility scores alignment. Creative use: Reconstruct and compare a stylized character walk cycle from a reference clip. [Source](https://github.com/xbishi/mocap-skills)

### Introduction

An AI coding assistant uses silhouette measurements and inverse kinematics to transfer side-view reference motion into a Blender rig; a separate utility scores alignment. [Source 1](https://github.com/xbishi/mocap-skills)

### What it is good for

Reconstruct and compare a stylized character walk cycle from a reference clip. [Source 1](https://github.com/xbishi/mocap-skills)

### Demo & examples

The README describes a cartoon-wolf development example with overlay/IoU checks; its reported score is author evidence, not an independent evaluation. [Source 1](https://github.com/xbishi/mocap-skills)

### Install

Follow the reviewed project route below; these steps are documentation guidance and were not executed. [Source 1](https://github.com/xbishi/mocap-skills)

1. Copy the h3-to-blender-mocap and rg-mocap-score folders into the chosen agent's skills directory.
2. Provide Blender 5.1+, BlenderMCP, FFmpeg/ffprobe and NumPy.
3. Adapt the rig configuration and reference paths using the supplied workflow documentation.
### First project

A small first project that exercises the documented creative workflow. [Source 1](https://github.com/xbishi/mocap-skills)

1. Prepare a side-view clip and compatible Rigify-style character.
2. Measure the silhouette, drive the rig, then compare rendered frames using red/green overlays.
3. Inspect hidden limbs manually and choose/repair a looping window.
### Hardware & software

Requirements are source-specific. Unreported capacities and untested platforms are not inferred. [Source 1](https://github.com/xbishi/mocap-skills)

- **Hardware:** The method does not train a pose model. No numeric CPU, RAM, VRAM or disk minimum is documented.
- **Software:** Blender 5.1+, BlenderMCP (documented port 9876), FFmpeg/ffprobe, NumPy and an AI coding assistant.
- **Platforms:** A tested operating-system matrix is not published.

### License, model weights & costs

The complete software license was archived and reviewed. Keep software, model weights, dependencies and hosted-service terms separate. [Source 1](https://github.com/xbishi/mocap-skills/blob/main/LICENSE) [Source 2](https://github.com/xbishi/mocap-skills)

- **Code:** MIT
- **Weights:** The motion-transfer scripts use image measurements and IK, not bundled neural weights; AI comes from the authoring agent and optional generated references.
- **Commercial:** The reviewed MIT software license permits commercial use subject to its license, notice and source-sharing obligations where applicable. This does not establish permission for every model, input, output or service.
- **Cost:** MIT scripts; Blender and local rendering resources plus any chosen agent/image service costs.

### Why it merits attention

Per-frame overlays and a separate scoring tool expose errors instead of relying only on a polished demonstration. [Source 1](https://github.com/xbishi/mocap-skills)

### Limitations

Best suited to monocular side views and a configured rig. High silhouette IoU does not prove correct hidden-limb placement. This edition is a documentation review, not an installation or output-quality test. [Source 1](https://github.com/xbishi/mocap-skills)

### Get the tool

- [Repository](https://github.com/xbishi/mocap-skills)
- [License](https://github.com/xbishi/mocap-skills/blob/main/LICENSE)

## AIMO

Editing, captions & post-production · Motion capture & character animation · Video, animation & film · AI agents for code-authored media production

First detailed guide, completing an earlier screened lead. The repository was created in the current discovery window; this is a documentation baseline, not a verified launch date.

### How it uses AI

A timeline and visual inspector for code-authored videos, with an integrated AI assistant that can edit the element visible in the current frame. Creative use: Adjust generated titles, shapes, timing and sound without repeatedly locating the drawing code by hand. [Source](https://github.com/uxKero/aimo)

### Introduction

A timeline and visual inspector for code-authored videos, with an integrated AI assistant that can edit the element visible in the current frame. [Source 1](https://github.com/uxKero/aimo)

### What it is good for

Adjust generated titles, shapes, timing and sound without repeatedly locating the drawing code by hand. [Source 1](https://github.com/uxKero/aimo)

### Demo & examples

The README shows the visual inspector, text controls and timeline, and describes an included example/tour. [Source 1](https://github.com/uxKero/aimo)

### Install

Follow the reviewed project route below; these steps are documentation guidance and were not executed. [Source 1](https://github.com/uxKero/aimo)

1. Install Node.js 20+, Python 3.10+, FFmpeg and an authenticated Claude Code client.
2. Clone uxKero/aimo and start its prebuilt server with node aimo/server/aimo-server.js.
3. Open the local address on port 4870 and complete the dependency check and example tour.
### First project

A small first project that exercises the documented creative workflow. [Source 1](https://github.com/uxKero/aimo)

1. Open a code-authored video or its included example.
2. Select a visible element to edit values, or ask the assistant to change it.
3. Preview the affected frames and audio, then export MP4, WebM, GIF or PNG.
### Hardware & software

Requirements are source-specific. Unreported capacities and untested platforms are not inferred. [Source 1](https://github.com/uxKero/aimo)

- **Hardware:** Numeric CPU, RAM, VRAM and storage minimums are not documented.
- **Software:** Node.js 20+, Python 3.10+, FFmpeg and Claude Code. Optional image generation uses OpenRouter or Vercel AI Gateway.
- **Platforms:** Windows is tested by the author; macOS and Linux are described as expected to work but untested.

### License, model weights & costs

The complete software license was archived and reviewed. Keep software, model weights, dependencies and hosted-service terms separate. [Source 1](https://github.com/uxKero/aimo/blob/main/LICENSE) [Source 2](https://github.com/uxKero/aimo)

- **Code:** MIT
- **Weights:** No model weights are supplied; Claude and optional image providers remain separate.
- **Commercial:** The reviewed MIT software license permits commercial use subject to its license, notice and source-sharing obligations where applicable. This does not establish permission for every model, input, output or service.
- **Cost:** MIT application; agent access and optional generation APIs may cost money.

### Why it merits attention

Direct selection-to-code inspection, undo grouping and per-track sound controls address concrete editing problems. [Source 1](https://github.com/uxKero/aimo)

### Limitations

Not every video format is editable as code. Cross-platform support and export quality were not tested in this review. This edition is a documentation review, not an installation or output-quality test. [Source 1](https://github.com/uxKero/aimo)

### Get the tool

- [Repository](https://github.com/uxKero/aimo)
- [License](https://github.com/uxKero/aimo/blob/main/LICENSE)

## Pixel2Motion

Vector graphics, illustration & textures · Motion capture & character animation · Browser tools & web media · Typography, fonts & layout · AI agents for code-authored media production

First detailed guide, completing an earlier screened lead. This is a documentation baseline, not a claim that the project launched today.

### How it uses AI

A coding agent reconstructs a raster logo as structured SVG, authors animation and uses local scripts to inspect geometry and frame continuity. Creative use: Produce a reusable animated brand mark with an editable SVG and a browser-based motion showcase. [Source](https://github.com/nolangz/pixel2motion) [Source](https://nolangz.github.io/pixel2motion/)

### Introduction

A coding agent reconstructs a raster logo as structured SVG, authors animation and uses local scripts to inspect geometry and frame continuity. [Source 1](https://github.com/nolangz/pixel2motion) [Source 2](https://nolangz.github.io/pixel2motion/)

### What it is good for

Produce a reusable animated brand mark with an editable SVG and a browser-based motion showcase. [Source 1](https://github.com/nolangz/pixel2motion) [Source 2](https://nolangz.github.io/pixel2motion/)

### Demo & examples

The official GitHub Pages gallery shows source/logo-motion pairs and fitting evidence with replay and speed controls. [Source 1](https://github.com/nolangz/pixel2motion) [Source 2](https://nolangz.github.io/pixel2motion/)

### Install

Follow the reviewed project route below; these steps are documentation guidance and were not executed. [Source 1](https://github.com/nolangz/pixel2motion) [Source 2](https://nolangz.github.io/pixel2motion/)

1. Download the repository and configure its workflow in a compatible Codex or Claude skill environment.
2. Create a Python 3.10+ environment and install Pillow, NumPy and Playwright.
3. Install/configure Chrome or Chromium for the rendering and frame-capture helpers.
### First project

A small first project that exercises the documented creative workflow. [Source 1](https://github.com/nolangz/pixel2motion) [Source 2](https://nolangz.github.io/pixel2motion/)

1. Supply a logo and write a motion brief.
2. Fit the static vector and review overlays before choreographing semantic SVG parts.
3. Generate the HTML showcase, capture frames and compare the final frame with the approved static logo.
### Hardware & software

Requirements are source-specific. Unreported capacities and untested platforms are not inferred. [Source 1](https://github.com/nolangz/pixel2motion) [Source 2](https://nolangz.github.io/pixel2motion/)

- **Hardware:** RAM, GPU/VRAM and disk minimums are not documented.
- **Software:** Python 3.10+, Pillow, NumPy, Playwright, Chrome/Chromium and an AI coding assistant.
- **Platforms:** A macOS Chrome path is illustrated, but there is no complete tested OS matrix. Browser playback does not establish installation support.

### License, model weights & costs

The complete software license was archived and reviewed. Keep software, model weights, dependencies and hosted-service terms separate. [Source 1](https://github.com/nolangz/pixel2motion/blob/main/LICENSE) [Source 2](https://github.com/nolangz/pixel2motion) [Source 3](https://nolangz.github.io/pixel2motion/)

- **Code:** MIT
- **Weights:** No bundled model weights; the chosen agent's terms apply.
- **Commercial:** The reviewed MIT software license permits commercial use subject to its license, notice and source-sharing obligations where applicable. This does not establish permission for every model, input, output or service.
- **Cost:** MIT source; optional commercial Pixel2Motion services are separate from the open workflow.

### Why it merits attention

Geometry overlays, path audits and deterministic frame capture provide inspectable design QA. [Source 1](https://github.com/nolangz/pixel2motion) [Source 2](https://nolangz.github.io/pixel2motion/)

### Limitations

An agent still authors and reviews the result. High geometric overlap alone does not establish good typography or motion. This edition is a documentation review, not an installation or output-quality test. [Source 1](https://github.com/nolangz/pixel2motion) [Source 2](https://nolangz.github.io/pixel2motion/)

### Get the tool

- [Repository](https://github.com/nolangz/pixel2motion)
- [License](https://github.com/nolangz/pixel2motion/blob/main/LICENSE)
- [Documentation](https://nolangz.github.io/pixel2motion/)

## Jellyfish

Storyboarding, narrative & comics · Video, animation & film · Images & design

First detailed guide, completing an earlier screened lead. This is a documentation baseline, not a claim that the project launched today.

### How it uses AI

An AI short-drama workspace organizes scripts, shot breakdowns, character/prop assets and image/video generation jobs. Creative use: Manage a multi-shot story while reusing approved references and tracking generation, cancellation and recovery. [Source](https://github.com/Forget-C/Jellyfish)

### Introduction

An AI short-drama workspace organizes scripts, shot breakdowns, character/prop assets and image/video generation jobs. [Source 1](https://github.com/Forget-C/Jellyfish)

### What it is good for

Manage a multi-shot story while reusing approved references and tracking generation, cancellation and recovery. [Source 1](https://github.com/Forget-C/Jellyfish)

### Demo & examples

The README includes project and asset-management screenshots; no live production test was performed. [Source 1](https://github.com/Forget-C/Jellyfish)

### Install

Follow the reviewed project route below; these steps are documentation guidance and were not executed. [Source 1](https://github.com/Forget-C/Jellyfish)

1. Clone the repository and install Docker with Compose.
2. Copy deploy/compose/.env.example to deploy/compose/.env and set local configuration.
3. Launch the documented Compose file; open the frontend on port 7788 and configure model providers.
### First project

A small first project that exercises the documented creative workflow. [Source 1](https://github.com/Forget-C/Jellyfish)

1. Create a project/chapter and supply the script.
2. Review extracted shots, dialogue and candidate assets; confirm shot readiness.
3. Generate approved shot media, monitor task status and review exports.
### Hardware & software

Requirements are source-specific. Unreported capacities and untested platforms are not inferred. [Source 1](https://github.com/Forget-C/Jellyfish)

- **Hardware:** CPU, RAM, VRAM and disk minimums are not specified. Provider-side generation has its own requirements.
- **Software:** Docker/Compose stack including backend, frontend, MySQL, Redis and RustFS; manual development uses uv and pnpm.
- **Platforms:** Container and local-development routes are documented, but there is no tested desktop OS matrix.

### License, model weights & costs

The complete software license was archived and reviewed. Keep software, model weights, dependencies and hosted-service terms separate. [Source 1](https://github.com/Forget-C/Jellyfish/blob/main/LICENSE) [Source 2](https://github.com/Forget-C/Jellyfish)

- **Code:** Apache-2.0
- **Weights:** No common weight license covers the workspace's configurable providers; check each selected model.
- **Commercial:** The reviewed Apache-2.0 software license permits commercial use subject to its license, notice and source-sharing obligations where applicable. This does not establish permission for every model, input, output or service.
- **Cost:** Apache-2.0 workspace; compute, storage and external generation services may cost money.

### Why it merits attention

Explicit readiness states and reusable character/scene assets make this more than a single prompt box. [Source 1](https://github.com/Forget-C/Jellyfish)

### Limitations

Identity consistency and provider reliability are not proven by the screenshots. Deployment is a multi-service setup. This edition is a documentation review, not an installation or output-quality test. [Source 1](https://github.com/Forget-C/Jellyfish)

### Get the tool

- [Repository](https://github.com/Forget-C/Jellyfish)
- [License](https://github.com/Forget-C/Jellyfish/blob/main/LICENSE)

## ArcReel

Storyboarding, narrative & comics · Video, animation & film · Images & design · AI agents for code-authored media production

First detailed guide, completing an earlier screened lead. This is a documentation baseline, not a claim that the project launched today.

### How it uses AI

A self-hosted AI workbench turns novels, scripts or product materials into reviewed assets, storyboards, generated shots and editable short videos. Creative use: Create episodic or product narratives with reusable character references and generation-cost tracking. [Source](https://github.com/ArcReel/ArcReel) [Source](https://docs.arc-reel.com/guide/getting-started/) [Source](https://github.com/ArcReel/ArcReel/blob/main/NOTICE) [Source](https://arc-reel.com/en/)

### Introduction

A self-hosted AI workbench turns novels, scripts or product materials into reviewed assets, storyboards, generated shots and editable short videos. [Source 1](https://github.com/ArcReel/ArcReel) [Source 2](https://docs.arc-reel.com/guide/getting-started/) [Source 3](https://github.com/ArcReel/ArcReel/blob/main/NOTICE) [Source 4](https://arc-reel.com/en/)

### What it is good for

Create episodic or product narratives with reusable character references and generation-cost tracking. [Source 1](https://github.com/ArcReel/ArcReel) [Source 2](https://docs.arc-reel.com/guide/getting-started/) [Source 3](https://github.com/ArcReel/ArcReel/blob/main/NOTICE) [Source 4](https://arc-reel.com/en/)

### Demo & examples

The README includes three short-drama examples and interface screenshots; the project site describes the production stages. [Source 1](https://github.com/ArcReel/ArcReel) [Source 2](https://docs.arc-reel.com/guide/getting-started/) [Source 3](https://github.com/ArcReel/ArcReel/blob/main/NOTICE) [Source 4](https://arc-reel.com/en/)

### Install

Follow the reviewed project route below; these steps are documentation guidance and were not executed. [Source 1](https://github.com/ArcReel/ArcReel) [Source 2](https://docs.arc-reel.com/guide/getting-started/) [Source 3](https://github.com/ArcReel/ArcReel/blob/main/NOTICE) [Source 4](https://arc-reel.com/en/)

1. Install Docker and Docker Compose, then clone ArcReel.
2. Enter deploy, copy .env.example to .env and review authentication/network settings.
3. Launch docker compose up -d; open port 1241, sign in and configure the agent and generation providers.
### First project

A small first project that exercises the documented creative workflow. [Source 1](https://github.com/ArcReel/ArcReel) [Source 2](https://docs.arc-reel.com/guide/getting-started/) [Source 3](https://github.com/ArcReel/ArcReel/blob/main/NOTICE) [Source 4](https://arc-reel.com/en/)

1. Create a project from a novel, finished script or creative concept.
2. Approve assets and shot plans, then generate and revise selected media.
3. Assemble a video or export a Jianying draft for further editing.
### Hardware & software

Requirements are source-specific. Unreported capacities and untested platforms are not inferred. [Source 1](https://github.com/ArcReel/ArcReel) [Source 2](https://docs.arc-reel.com/guide/getting-started/) [Source 3](https://github.com/ArcReel/ArcReel/blob/main/NOTICE) [Source 4](https://arc-reel.com/en/)

- **Hardware:** Minimum RAM, VRAM, CPU and disk capacity are not specified in the reviewed quick start.
- **Software:** Docker/Compose, configured text/image/video/TTS providers; media processing uses bundled FFmpeg.
- **Platforms:** Project documentation describes Docker, macOS and Windows through WSL2. Provider inference is a separate environment.

### License, model weights & costs

The complete software license was archived and reviewed. Keep software, model weights, dependencies and hosted-service terms separate. [Source 1](https://github.com/ArcReel/ArcReel/blob/main/LICENSE) [Source 2](https://github.com/ArcReel/ArcReel) [Source 3](https://docs.arc-reel.com/guide/getting-started/) [Source 4](https://github.com/ArcReel/ArcReel/blob/main/NOTICE) [Source 5](https://arc-reel.com/en/)

- **Code:** AGPL-3.0
- **Weights:** Generation-provider models retain their own licenses; AGPL does not license their weights.
- **Commercial:** The reviewed AGPL-3.0 software license permits commercial use subject to its license, notice and source-sharing obligations where applicable. This does not establish permission for every model, input, output or service.
- **Cost:** AGPL-3.0 application; provider usage and hosting are separate. Alternative commercial licensing is offered.

### Why it merits attention

Reviewable stages, asset reuse, regeneration and editing export address practical multi-shot production. [Source 1](https://github.com/ArcReel/ArcReel) [Source 2](https://docs.arc-reel.com/guide/getting-started/) [Source 3](https://github.com/ArcReel/ArcReel/blob/main/NOTICE) [Source 4](https://arc-reel.com/en/)

### Limitations

Jianying export targets the mainland-China application; CapCut compatibility is unverified. NOTICE requires visible attribution/origin notices; trademark rights are separate. This edition is a documentation review, not an installation or output-quality test. [Source 1](https://github.com/ArcReel/ArcReel) [Source 2](https://docs.arc-reel.com/guide/getting-started/) [Source 3](https://github.com/ArcReel/ArcReel/blob/main/NOTICE) [Source 4](https://arc-reel.com/en/)

### Get the tool

- [Repository](https://github.com/ArcReel/ArcReel)
- [License](https://github.com/ArcReel/ArcReel/blob/main/LICENSE)
- [Documentation](https://docs.arc-reel.com/guide/getting-started/)

## CVAT Community

Photogrammetry, scanning & neural rendering · Images & design · Video, animation & film · 3D, reconstruction & assets · Creative learning & authoring

First detailed guide, completing an earlier screened lead. This is a documentation baseline, not a claim that the project launched today.

### How it uses AI

A visual-data annotation workspace with model-assisted segmentation, detection and tracking for images, video and point clouds. Creative use: Build and correct masks, tracking labels or training sets for creative vision, capture and restoration workflows. [Source](https://github.com/cvat-ai/cvat) [Source](https://docs.cvat.ai/docs/administration/community/basics/installation/)

### Introduction

A visual-data annotation workspace with model-assisted segmentation, detection and tracking for images, video and point clouds. [Source 1](https://github.com/cvat-ai/cvat) [Source 2](https://docs.cvat.ai/docs/administration/community/basics/installation/)

### What it is good for

Build and correct masks, tracking labels or training sets for creative vision, capture and restoration workflows. [Source 1](https://github.com/cvat-ai/cvat) [Source 2](https://docs.cvat.ai/docs/administration/community/basics/installation/)

### Demo & examples

The official tutorials and hosted CVAT Online provide demonstrations; hosted feature availability differs from Community. [Source 1](https://github.com/cvat-ai/cvat) [Source 2](https://docs.cvat.ai/docs/administration/community/basics/installation/)

### Install

Follow the reviewed project route below; these steps are documentation guidance and were not executed. [Source 1](https://github.com/cvat-ai/cvat) [Source 2](https://docs.cvat.ai/docs/administration/community/basics/installation/)

1. Install Git, Docker Engine and Compose; clone cvat-ai/cvat.
2. Start the default Compose stack and create the documented administrator account.
3. For AI annotation, enable the serverless Compose component and deploy chosen Nuclio model functions.
### First project

A small first project that exercises the documented creative workflow. [Source 1](https://github.com/cvat-ai/cvat) [Source 2](https://docs.cvat.ai/docs/administration/community/basics/installation/)

1. Create a project/task, upload a short clip or image set and define labels.
2. Run a selected auto-annotation model and manually correct its output.
3. Review annotations and export a supported dataset format.
### Hardware & software

Requirements are source-specific. Unreported capacities and untested platforms are not inferred. [Source 1](https://github.com/cvat-ai/cvat) [Source 2](https://docs.cvat.ai/docs/administration/community/basics/installation/)

- **Hardware:** Numeric RAM, VRAM and storage minimums are not established by the reviewed README; model functions have separate compute needs.
- **Software:** Docker/Compose and Git; Nuclio/nuctl plus model-specific dependencies for serverless AI annotation.
- **Platforms:** Official installation docs cover Ubuntu, Windows and macOS. Chromium browsers are primarily tested; Safari/WebKit is unsupported.

### License, model weights & costs

The complete software license was archived and reviewed. Keep software, model weights, dependencies and hosted-service terms separate. [Source 1](https://github.com/cvat-ai/cvat/blob/develop/LICENSE) [Source 2](https://github.com/cvat-ai/cvat) [Source 3](https://docs.cvat.ai/docs/administration/community/basics/installation/)

- **Code:** MIT
- **Weights:** Core/serverless code is MIT, but some third-party model assets are non-commercial or separately licensed.
- **Commercial:** The reviewed MIT software license permits commercial use subject to its license, notice and source-sharing obligations where applicable. This does not establish permission for every model, input, output or service.
- **Cost:** Community source is MIT and self-hosted; Online and Enterprise plans and their extra features are separate.

### Why it merits attention

Manual correction, dataset export and task review make model output auditable for real production datasets. [Source 1](https://github.com/cvat-ai/cvat) [Source 2](https://docs.cvat.ai/docs/administration/community/basics/installation/)

### Limitations

This prepares/labels media; it is not an image generator. Paid hosted SAM/agent features must not be assumed included in Community. This edition is a documentation review, not an installation or output-quality test. [Source 1](https://github.com/cvat-ai/cvat) [Source 2](https://docs.cvat.ai/docs/administration/community/basics/installation/)

### Get the tool

- [Repository](https://github.com/cvat-ai/cvat)
- [License](https://github.com/cvat-ai/cvat/blob/develop/LICENSE)
- [Documentation](https://docs.cvat.ai/docs/administration/community/basics/installation/)

## SD.Next

Images & design · Video, animation & film · Photography, restoration & color · Editing, captions & post-production

First detailed guide, completing an earlier screened lead. This is a documentation baseline, not a claim that the project launched today.

### How it uses AI

A local server and WebUI for diffusion image/video generation, guided editing, captioning and post-processing. Creative use: Explore model-specific image generation, inpainting, LoRA/control workflows and image enhancement from one interface. [Source](https://github.com/vladmandic/sdnext) [Source](https://vladmandic.github.io/sdnext-docs/Installation/)

### Introduction

A local server and WebUI for diffusion image/video generation, guided editing, captioning and post-processing. [Source 1](https://github.com/vladmandic/sdnext) [Source 2](https://vladmandic.github.io/sdnext-docs/Installation/)

### What it is good for

Explore model-specific image generation, inpainting, LoRA/control workflows and image enhancement from one interface. [Source 1](https://github.com/vladmandic/sdnext) [Source 2](https://vladmandic.github.io/sdnext-docs/Installation/)

### Demo & examples

Official desktop/mobile screenshots and an installation walkthrough are linked from the README. [Source 1](https://github.com/vladmandic/sdnext) [Source 2](https://vladmandic.github.io/sdnext-docs/Installation/)

### Install

Follow the reviewed project route below; these steps are documentation guidance and were not executed. [Source 1](https://github.com/vladmandic/sdnext) [Source 2](https://vladmandic.github.io/sdnext-docs/Installation/)

1. Install supported Git/Python versions and choose the documented compute backend.
2. Clone vladmandic/sdnext into a writable directory and run the OS-specific launcher.
3. Wait for dependency setup, open the displayed local URL and configure model/cache paths.

```sh
git clone https://github.com/vladmandic/sdnext
```


```sh
./webui.sh  # from sdnext on Linux/macOS; Windows uses webui.bat
```

### First project

A small first project that exercises the documented creative workflow. [Source 1](https://github.com/vladmandic/sdnext) [Source 2](https://vladmandic.github.io/sdnext-docs/Installation/)

1. Download or select a compatible model and review its terms.
2. Try a small text-to-image job, then test an editing or control workflow.
3. Inspect the result and save the image and settings.
### Hardware & software

Requirements are source-specific. Unreported capacities and untested platforms are not inferred. [Source 1](https://github.com/vladmandic/sdnext) [Source 2](https://vladmandic.github.io/sdnext-docs/Installation/)

- **Hardware:** Multiple GPU backends and CPU execution are documented. There is no universal RAM, VRAM or disk minimum across supported models.
- **Software:** Git, Python, selected Torch/backend dependencies and downloaded model files; the launcher manages its environment.
- **Platforms:** Windows/Linux NVIDIA, AMD and Intel routes; Apple Silicon MPS on macOS; backend-specific Docker recipes. Support varies by model.

### License, model weights & costs

The complete software license was archived and reviewed. Keep software, model weights, dependencies and hosted-service terms separate. [Source 1](https://github.com/vladmandic/sdnext/blob/master/LICENSE.txt) [Source 2](https://github.com/vladmandic/sdnext) [Source 3](https://vladmandic.github.io/sdnext-docs/Installation/)

- **Code:** Apache-2.0
- **Weights:** Each downloaded model, LoRA and extension has its own license; the server's Apache-2.0 terms do not cover all weights.
- **Commercial:** The reviewed Apache-2.0 software license permits commercial use subject to its license, notice and source-sharing obligations where applicable. This does not establish permission for every model, input, output or service.
- **Cost:** Apache-2.0 source; local compute/storage and optional remote services are separate.

### Why it merits attention

Documented cross-platform backends and model-specific controls make it useful beyond a single vendor's GPU stack. [Source 1](https://github.com/vladmandic/sdnext) [Source 2](https://vladmandic.github.io/sdnext-docs/Installation/)

### Limitations

Quantization/offloading claims are developer claims; this review did not benchmark them. Mobile WebUI access is not on-device inference. This edition is a documentation review, not an installation or output-quality test. [Source 1](https://github.com/vladmandic/sdnext) [Source 2](https://vladmandic.github.io/sdnext-docs/Installation/)

### Get the tool

- [Repository](https://github.com/vladmandic/sdnext)
- [License](https://github.com/vladmandic/sdnext/blob/master/LICENSE.txt)
- [Documentation](https://vladmandic.github.io/sdnext-docs/Installation/)

## PartCrafter

3D, reconstruction & assets · Games & production pipelines · 3D printing & generative CAD

First detailed guide, completing an earlier screened lead. This is a documentation baseline, not a claim that the project launched today.

### How it uses AI

A compositional diffusion model generates multiple semantically distinct 3D mesh parts from one RGB image. Creative use: Prototype decomposable props or scene objects for further editing; fabrication needs separate geometric validation. [Source](https://github.com/wgsxm/PartCrafter) [Source](https://wgsxm.github.io/projects/partcrafter/)

### Introduction

A compositional diffusion model generates multiple semantically distinct 3D mesh parts from one RGB image. [Source 1](https://github.com/wgsxm/PartCrafter) [Source 2](https://wgsxm.github.io/projects/partcrafter/)

### What it is good for

Prototype decomposable props or scene objects for further editing; fabrication needs separate geometric validation. [Source 1](https://github.com/wgsxm/PartCrafter) [Source 2](https://wgsxm.github.io/projects/partcrafter/)

### Demo & examples

The project page shows part-separated objects, scenes and real-photo experiments and links a community-hosted demo. [Source 1](https://github.com/wgsxm/PartCrafter) [Source 2](https://wgsxm.github.io/projects/partcrafter/)

### Install

Follow the reviewed project route below; these steps are documentation guidance and were not executed. [Source 1](https://github.com/wgsxm/PartCrafter) [Source 2](https://wgsxm.github.io/projects/partcrafter/)

1. Set up the documented Python 3.11 and PyTorch 2.5.1/CUDA 12.4 environment.
2. Clone PartCrafter and follow settings/setup.sh and graphics-library instructions after reviewing them.
3. Run a supplied image example; the inference scripts download required checkpoints.

```sh
python scripts/inference_partcrafter.py --image_path assets/images/np3_2f6ab901c5a84ed6bbdf85a67b22a2ee.png --num_parts 3 --tag robot --render
```

### First project

A small first project that exercises the documented creative workflow. [Source 1](https://github.com/wgsxm/PartCrafter) [Source 2](https://wgsxm.github.io/projects/partcrafter/)

1. Start with the robot example and its suggested three-part count.
2. Inspect generated parts in results/robot; vary the count or use background removal for your own image.
3. Check geometry and topology in a 3D editor before using it in a game or print workflow.
### Hardware & software

Requirements are source-specific. Unreported capacities and untested platforms are not inferred. [Source 1](https://github.com/wgsxm/PartCrafter) [Source 2](https://wgsxm.github.io/projects/partcrafter/)

- **Hardware:** A CUDA GPU with at least 8GB VRAM is documented for inference; part/token counts increase demand. RAM and total storage are not specified. Training example uses 8×H20 96GB.
- **Software:** Python 3.11, Torch 2.5.1+cu124, graphics libraries and checkpoints. Optional VLM assistance uses separate API credentials.
- **Platforms:** Tested Debian 12/NVIDIA H20; upstream links community Windows instructions. macOS, AMD and CPU inference are not documented.

### License, model weights & costs

The complete software license was archived and reviewed. Keep software, model weights, dependencies and hosted-service terms separate. [Source 1](https://github.com/wgsxm/PartCrafter/blob/main/LICENSE) [Source 2](https://github.com/wgsxm/PartCrafter) [Source 3](https://wgsxm.github.io/projects/partcrafter/)

- **Code:** MIT
- **Weights:** PartCrafter, scene, TripoSG and optional RMBG checkpoints require their respective model terms; MIT code does not establish a blanket weight grant.
- **Commercial:** The reviewed MIT software license permits commercial use subject to its license, notice and source-sharing obligations where applicable. This does not establish permission for every model, input, output or service.
- **Cost:** MIT software; local GPU resources, optional hosted demo and optional Gemini assistance have separate costs/terms.

### Why it merits attention

Part-aware outputs and explicit part-count control are concrete advantages for editable asset experiments. [Source 1](https://github.com/wgsxm/PartCrafter) [Source 2](https://wgsxm.github.io/projects/partcrafter/)

### Limitations

Real photos have a domain gap; stylization may help but changes the input. Mesh output does not guarantee watertightness, scale or print readiness. This edition is a documentation review, not an installation or output-quality test. [Source 1](https://github.com/wgsxm/PartCrafter) [Source 2](https://wgsxm.github.io/projects/partcrafter/)

### Get the tool

- [Repository](https://github.com/wgsxm/PartCrafter)
- [License](https://github.com/wgsxm/PartCrafter/blob/main/LICENSE)
- [Documentation](https://wgsxm.github.io/projects/partcrafter/)

## Efficient Gaussian Appearance

3D, reconstruction & assets · Photogrammetry, scanning & neural rendering · Spatial audio & volumetric media · Browser tools & web media

First detailed guide, completing an earlier screened lead. The repository was created in the current discovery window; this is a documentation baseline, not a verified launch date.

### How it uses AI

A Gaussian-splatting pipeline compares view-dependent appearance models and adds compact per-splat features decoded by a small neural network. Creative use: Research smaller neural scene representations and inspect the rendered results in a portable browser viewer. [Source](https://github.com/nerficg-project/efficient-gaussian-appearance) [Source](https://fhahlbohm.github.io/efficient-gaussian-appearance/) [Source](https://fhahlbohm.github.io/efficient-gaussian-appearance/viewer/)

### Introduction

A Gaussian-splatting pipeline compares view-dependent appearance models and adds compact per-splat features decoded by a small neural network. [Source 1](https://github.com/nerficg-project/efficient-gaussian-appearance) [Source 2](https://fhahlbohm.github.io/efficient-gaussian-appearance/) [Source 3](https://fhahlbohm.github.io/efficient-gaussian-appearance/viewer/)

### What it is good for

Research smaller neural scene representations and inspect the rendered results in a portable browser viewer. [Source 1](https://github.com/nerficg-project/efficient-gaussian-appearance) [Source 2](https://fhahlbohm.github.io/efficient-gaussian-appearance/) [Source 3](https://fhahlbohm.github.io/efficient-gaussian-appearance/viewer/)

### Demo & examples

The official WebGL viewer publishes benchmark-scene checkpoints for the compared appearance models. [Source 1](https://github.com/nerficg-project/efficient-gaussian-appearance) [Source 2](https://fhahlbohm.github.io/efficient-gaussian-appearance/) [Source 3](https://fhahlbohm.github.io/efficient-gaussian-appearance/viewer/)

### Install

Follow the reviewed project route below; these steps are documentation guidance and were not executed. [Source 1](https://github.com/nerficg-project/efficient-gaussian-appearance) [Source 2](https://fhahlbohm.github.io/efficient-gaussian-appearance/) [Source 3](https://fhahlbohm.github.io/efficient-gaussian-appearance/viewer/)

1. Set up the NeRFICG framework and its compatible Conda environment.
2. Clone this repository recursively into src/Methods/FasterGSVDA.
3. Install method dependencies with the documented NeRFICG installer and select an appearance configuration.
### First project

A small first project that exercises the documented creative workflow. [Source 1](https://github.com/nerficg-project/efficient-gaussian-appearance) [Source 2](https://fhahlbohm.github.io/efficient-gaussian-appearance/) [Source 3](https://fhahlbohm.github.io/efficient-gaussian-appearance/viewer/)

1. Prepare a supported posed-image scene.
2. Train the supplied neural-appearance configuration and inspect reconstruction quality.
3. Export the trained run with export_ngsplat.py and open it in the WebGL viewer.
### Hardware & software

Requirements are source-specific. Unreported capacities and untested platforms are not inferred. [Source 1](https://github.com/nerficg-project/efficient-gaussian-appearance) [Source 2](https://fhahlbohm.github.io/efficient-gaussian-appearance/) [Source 3](https://fhahlbohm.github.io/efficient-gaussian-appearance/viewer/)

- **Hardware:** NVIDIA GPU required for training; no numeric RAM, VRAM or disk minimum is documented. Browser viewing has different requirements.
- **Software:** Conda, compatible C++ compiler and recent CUDA SDK; CUDA 12.8 is recommended. Uses NeRFICG and tiny-cuda-nn.
- **Platforms:** Linux preferred; Windows supported for the CUDA pipeline. WebGL viewing is separate and includes laptop/mobile examples; no macOS training claim.

### License, model weights & costs

The complete software license was archived and reviewed. Keep software, model weights, dependencies and hosted-service terms separate. [Source 1](https://github.com/nerficg-project/efficient-gaussian-appearance/blob/main/LICENSE) [Source 2](https://github.com/nerficg-project/efficient-gaussian-appearance) [Source 3](https://fhahlbohm.github.io/efficient-gaussian-appearance/) [Source 4](https://fhahlbohm.github.io/efficient-gaussian-appearance/viewer/)

- **Code:** Apache-2.0
- **Weights:** Scene checkpoints and third-party components need their own terms checked; source code is Apache-2.0.
- **Commercial:** The reviewed Apache-2.0 software license permits commercial use subject to its license, notice and source-sharing obligations where applicable. This does not establish permission for every model, input, output or service.
- **Cost:** No source license fee; GPU training resources and storage are user supplied.

### Why it merits attention

One pipeline and a shared viewer make appearance alternatives inspectable under comparable configurations. [Source 1](https://github.com/nerficg-project/efficient-gaussian-appearance) [Source 2](https://fhahlbohm.github.io/efficient-gaussian-appearance/) [Source 3](https://fhahlbohm.github.io/efficient-gaussian-appearance/viewer/)

### Limitations

Research results are not a universal speed/size guarantee. Neural appearance requires a compatible decoder; generic PLY viewers may lose that behavior. This edition is a documentation review, not an installation or output-quality test. [Source 1](https://github.com/nerficg-project/efficient-gaussian-appearance) [Source 2](https://fhahlbohm.github.io/efficient-gaussian-appearance/) [Source 3](https://fhahlbohm.github.io/efficient-gaussian-appearance/viewer/)

### Get the tool

- [Repository](https://github.com/nerficg-project/efficient-gaussian-appearance)
- [License](https://github.com/nerficg-project/efficient-gaussian-appearance/blob/main/LICENSE)
- [Documentation](https://fhahlbohm.github.io/efficient-gaussian-appearance/)

## HapticGen

Tactile, vibration and haptic media · WebXR, VR & AR · Interactive, immersive & live media · Physical, robotic & kinetic installations

First detailed guide in this library. This is a documentation baseline, not a claim that the project launched today.

### How it uses AI

A text-conditioned generative model produces vibration waveforms for haptic-design experiments. Creative use: Prototype tactile effects for interactive installations, XR and game feedback before testing them on a suitable actuator. [Source](https://github.com/HapticGen/HapticGen) [Source](https://hapticgen.hcitech.org/) [Source](https://huggingface.co/HapticGen/HapticGen-Weights) [Source](https://github.com/HapticGen/HapticGen/blob/main/requirements.txt) [Source](https://github.com/HapticGen/HapticGen/blob/main/audiogen-beam-serve.py) [Source](https://github.com/HapticGen/HapticGen/blob/main/README-audiocraft.md) [Source](https://github.com/HapticGen/HapticGen/blob/main/LICENSE_weights)

### Introduction

A text-conditioned generative model produces vibration waveforms for haptic-design experiments. [Source 1](https://github.com/HapticGen/HapticGen) [Source 2](https://hapticgen.hcitech.org/) [Source 3](https://huggingface.co/HapticGen/HapticGen-Weights) [Source 4](https://github.com/HapticGen/HapticGen/blob/main/requirements.txt) [Source 5](https://github.com/HapticGen/HapticGen/blob/main/audiogen-beam-serve.py) [Source 6](https://github.com/HapticGen/HapticGen/blob/main/README-audiocraft.md) [Source 7](https://github.com/HapticGen/HapticGen/blob/main/LICENSE_weights)

### What it is good for

Prototype tactile effects for interactive installations, XR and game feedback before testing them on a suitable actuator. [Source 1](https://github.com/HapticGen/HapticGen) [Source 2](https://hapticgen.hcitech.org/) [Source 3](https://huggingface.co/HapticGen/HapticGen-Weights) [Source 4](https://github.com/HapticGen/HapticGen/blob/main/requirements.txt) [Source 5](https://github.com/HapticGen/HapticGen/blob/main/audiogen-beam-serve.py) [Source 6](https://github.com/HapticGen/HapticGen/blob/main/README-audiocraft.md) [Source 7](https://github.com/HapticGen/HapticGen/blob/main/LICENSE_weights)

### Demo & examples

The CHI 2025 project page publishes examples and study material; no hardware demo was run here. [Source 1](https://github.com/HapticGen/HapticGen) [Source 2](https://hapticgen.hcitech.org/) [Source 3](https://huggingface.co/HapticGen/HapticGen-Weights) [Source 4](https://github.com/HapticGen/HapticGen/blob/main/requirements.txt) [Source 5](https://github.com/HapticGen/HapticGen/blob/main/audiogen-beam-serve.py) [Source 6](https://github.com/HapticGen/HapticGen/blob/main/README-audiocraft.md) [Source 7](https://github.com/HapticGen/HapticGen/blob/main/LICENSE_weights)

### Install

Follow the reviewed project route below; these steps are documentation guidance and were not executed. [Source 1](https://github.com/HapticGen/HapticGen) [Source 2](https://hapticgen.hcitech.org/) [Source 3](https://huggingface.co/HapticGen/HapticGen-Weights) [Source 4](https://github.com/HapticGen/HapticGen/blob/main/requirements.txt) [Source 5](https://github.com/HapticGen/HapticGen/blob/main/audiogen-beam-serve.py) [Source 6](https://github.com/HapticGen/HapticGen/blob/main/README-audiocraft.md) [Source 7](https://github.com/HapticGen/HapticGen/blob/main/LICENSE_weights)

1. Clone the code and follow README-audiocraft.md in an isolated Python environment.
2. Resolve the documented version mismatch: requirements.txt pins Torch 2.1.2, while older AudioCraft instructions name other Torch versions.
3. Download the separate HapticGen weights. Adapt audiogen-beam-serve.py model paths and provider configuration: it contains a placeholder file host and study-specific model IDs.
### First project

A small first project that exercises the documented creative workflow. [Source 1](https://github.com/HapticGen/HapticGen) [Source 2](https://hapticgen.hcitech.org/) [Source 3](https://huggingface.co/HapticGen/HapticGen-Weights) [Source 4](https://github.com/HapticGen/HapticGen/blob/main/requirements.txt) [Source 5](https://github.com/HapticGen/HapticGen/blob/main/audiogen-beam-serve.py) [Source 6](https://github.com/HapticGen/HapticGen/blob/main/README-audiocraft.md) [Source 7](https://github.com/HapticGen/HapticGen/blob/main/LICENSE_weights)

1. Choose a short tactile-event description.
2. Configure the matching checkpoint and review the script's local test path before generation.
3. Inspect the waveform, then evaluate sensation using documented actuator controls; this repository does not supply a universal device driver.
### Hardware & software

Requirements are source-specific. Unreported capacities and untested platforms are not inferred. [Source 1](https://github.com/HapticGen/HapticGen) [Source 2](https://hapticgen.hcitech.org/) [Source 3](https://huggingface.co/HapticGen/HapticGen-Weights) [Source 4](https://github.com/HapticGen/HapticGen/blob/main/requirements.txt) [Source 5](https://github.com/HapticGen/HapticGen/blob/main/audiogen-beam-serve.py) [Source 6](https://github.com/HapticGen/HapticGen/blob/main/README-audiocraft.md) [Source 7](https://github.com/HapticGen/HapticGen/blob/main/LICENSE_weights)

- **Hardware:** The study-serving example requests a T4 GPU and 16 GiB host memory; these are example settings, not minimum requirements. Minimum VRAM, disk and actuator compatibility are not documented.
- **Software:** Python 3.9 in the serving example, CUDA-enabled Torch, AudioCraft dependencies, Beam and OpenAI imports. The unchanged study script initializes an OpenAI client.
- **Platforms:** No tested Windows/macOS/Linux support matrix is published. A cloud endpoint example is not proof of local Mac support.

### License, model weights & costs

The complete software license was archived and reviewed. Keep software, model weights, dependencies and hosted-service terms separate. [Source 1](https://github.com/HapticGen/HapticGen/blob/main/LICENSE) [Source 2](https://github.com/HapticGen/HapticGen) [Source 3](https://hapticgen.hcitech.org/) [Source 4](https://huggingface.co/HapticGen/HapticGen-Weights) [Source 5](https://github.com/HapticGen/HapticGen/blob/main/requirements.txt) [Source 6](https://github.com/HapticGen/HapticGen/blob/main/audiogen-beam-serve.py) [Source 7](https://github.com/HapticGen/HapticGen/blob/main/README-audiocraft.md) [Source 8](https://github.com/HapticGen/HapticGen/blob/main/LICENSE_weights)

- **Code:** MIT
- **Weights:** Published HapticGen weights are CC-BY-NC-4.0; they are non-commercial despite MIT software.
- **Commercial:** The reviewed MIT software license permits commercial use subject to its license, notice and source-sharing obligations where applicable. This does not establish permission for every model, input, output or service.
- **Cost:** Local/cloud compute, a haptic actuator and optional OpenAI prompt variations are separate costs.

### Why it merits attention

A research publication, released checkpoints and explicit waveform workflow make this a useful frontier experiment. [Source 1](https://github.com/HapticGen/HapticGen) [Source 2](https://hapticgen.hcitech.org/) [Source 3](https://huggingface.co/HapticGen/HapticGen-Weights) [Source 4](https://github.com/HapticGen/HapticGen/blob/main/requirements.txt) [Source 5](https://github.com/HapticGen/HapticGen/blob/main/audiogen-beam-serve.py) [Source 6](https://github.com/HapticGen/HapticGen/blob/main/README-audiocraft.md) [Source 7](https://github.com/HapticGen/HapticGen/blob/main/LICENSE_weights)

### Limitations

Not a ready-to-use consumer application. The sample server needs adaptation, and non-commercial weights restrict deployment. This edition is a documentation review, not an installation or output-quality test. [Source 1](https://github.com/HapticGen/HapticGen) [Source 2](https://hapticgen.hcitech.org/) [Source 3](https://huggingface.co/HapticGen/HapticGen-Weights) [Source 4](https://github.com/HapticGen/HapticGen/blob/main/requirements.txt) [Source 5](https://github.com/HapticGen/HapticGen/blob/main/audiogen-beam-serve.py) [Source 6](https://github.com/HapticGen/HapticGen/blob/main/README-audiocraft.md) [Source 7](https://github.com/HapticGen/HapticGen/blob/main/LICENSE_weights)

### Get the tool

- [Repository](https://github.com/HapticGen/HapticGen)
- [License](https://github.com/HapticGen/HapticGen/blob/main/LICENSE)
- [Documentation](https://hapticgen.hcitech.org/)

## Neural Acoustic Fields

Neural acoustics and responsive sound spaces · Spatial audio & volumetric media · Audio, music & voice · WebXR, VR & AR

First detailed guide in this library. This is a documentation baseline, not a claim that the project launched today.

### How it uses AI

A neural field predicts room impulse responses for emitter/listener positions, allowing arbitrary audio to inherit spatial acoustics. Creative use: Explore position-dependent reverberation and sound propagation for virtual environments. [Source](https://github.com/aluo-x/Learning_Neural_Acoustic_Fields) [Source](https://www.andrew.cmu.edu/user/afluo/Neural_Acoustic_Fields/) [Source](https://arxiv.org/abs/2204.00628)

### Introduction

A neural field predicts room impulse responses for emitter/listener positions, allowing arbitrary audio to inherit spatial acoustics. [Source 1](https://github.com/aluo-x/Learning_Neural_Acoustic_Fields) [Source 2](https://www.andrew.cmu.edu/user/afluo/Neural_Acoustic_Fields/) [Source 3](https://arxiv.org/abs/2204.00628)

### What it is good for

Explore position-dependent reverberation and sound propagation for virtual environments. [Source 1](https://github.com/aluo-x/Learning_Neural_Acoustic_Fields) [Source 2](https://www.andrew.cmu.edu/user/afluo/Neural_Acoustic_Fields/) [Source 3](https://arxiv.org/abs/2204.00628)

### Demo & examples

The primary project page and README include a spatial-audio video and a Colab link. [Source 1](https://github.com/aluo-x/Learning_Neural_Acoustic_Fields) [Source 2](https://www.andrew.cmu.edu/user/afluo/Neural_Acoustic_Fields/) [Source 3](https://arxiv.org/abs/2204.00628)

### Install

Follow the reviewed project route below; these steps are documentation guidance and were not executed. [Source 1](https://github.com/aluo-x/Learning_Neural_Acoustic_Fields) [Source 2](https://www.andrew.cmu.edu/user/afluo/Neural_Acoustic_Fields/) [Source 3](https://arxiv.org/abs/2204.00628)

1. Clone the repository and install the documented PyTorch/scientific Python dependencies.
2. Download the linked checkpoints and metadata, and extract them into the documented project structure.
3. Begin with an existing apartment scene; new-scene preparation requires additional SoundSpaces/Habitat tooling.
### First project

A small first project that exercises the documented creative workflow. [Source 1](https://github.com/aluo-x/Learning_Neural_Acoustic_Fields) [Source 2](https://www.andrew.cmu.edu/user/afluo/Neural_Acoustic_Fields/) [Source 3](https://arxiv.org/abs/2204.00628)

1. Run testing/cache_test_NAF.py on the supplied scene/checkpoint.
2. Run testing/compute_spectral_NAF.py to inspect reconstruction error.
3. Explore loudness or feature visualization before adapting the research pipeline to your own environment.
### Hardware & software

Requirements are source-specific. Unreported capacities and untested platforms are not inferred. [Source 1](https://github.com/aluo-x/Learning_Neural_Acoustic_Fields) [Source 2](https://www.andrew.cmu.edu/user/afluo/Neural_Acoustic_Fields/) [Source 3](https://arxiv.org/abs/2204.00628)

- **Hardware:** Testing is documented on one GPU; a training example uses four. GPU model, minimum VRAM, RAM and total disk requirements are not documented.
- **Software:** PyTorch 1.9, h5py, NumPy, SciPy, Matplotlib and librosa; scikit-learn for probes. FFmpeg 5 and Opus tools apply only to codec baselines.
- **Platforms:** Tested Ubuntu 20.04 and 21.10; other operating systems are not verified in the README.

### License, model weights & costs

The complete software license was archived and reviewed. Keep software, model weights, dependencies and hosted-service terms separate. [Source 1](https://github.com/aluo-x/Learning_Neural_Acoustic_Fields/blob/master/LICENSE) [Source 2](https://github.com/aluo-x/Learning_Neural_Acoustic_Fields) [Source 3](https://www.andrew.cmu.edu/user/afluo/Neural_Acoustic_Fields/) [Source 4](https://arxiv.org/abs/2204.00628)

- **Code:** Apache-2.0
- **Weights:** The Apache-2.0 source license does not establish separate checkpoint, scene-data or demo-music rights.
- **Commercial:** The reviewed Apache-2.0 software license permits commercial use subject to its license, notice and source-sharing obligations where applicable. This does not establish permission for every model, input, output or service.
- **Cost:** Local compute and data storage; no required paid inference API is documented.

### Why it merits attention

Released scene checkpoints and quantitative evaluation scripts support reproducible research. [Source 1](https://github.com/aluo-x/Learning_Neural_Acoustic_Fields) [Source 2](https://www.andrew.cmu.edu/user/afluo/Neural_Acoustic_Fields/) [Source 3](https://arxiv.org/abs/2204.00628)

### Limitations

The released implementation uses random phase, unlike a fully phase-aware acoustic simulator. Advanced scene/video tooling is described as work in progress. This edition is a documentation review, not an installation or output-quality test. [Source 1](https://github.com/aluo-x/Learning_Neural_Acoustic_Fields) [Source 2](https://www.andrew.cmu.edu/user/afluo/Neural_Acoustic_Fields/) [Source 3](https://arxiv.org/abs/2204.00628)

### Get the tool

- [Repository](https://github.com/aluo-x/Learning_Neural_Acoustic_Fields)
- [License](https://github.com/aluo-x/Learning_Neural_Acoustic_Fields/blob/master/LICENSE)
- [Documentation](https://www.andrew.cmu.edu/user/afluo/Neural_Acoustic_Fields/)

## MLX-Audio

Audio, music & voice · Accessible media & assistive creation · Mobile, edge & on-device creation

First detailed guide in this library. This is a documentation baseline, not a claim that the project launched today.

### How it uses AI

An Apple MLX toolkit runs speech generation, recognition and speech/audio transformation models on Apple Silicon. Creative use: Create local narration and transcriptions, or experiment with voice conversion and separation using a supported model. [Source](https://github.com/Blaizzy/mlx-audio) [Source](https://pypi.org/project/mlx-audio/)

### Introduction

An Apple MLX toolkit runs speech generation, recognition and speech/audio transformation models on Apple Silicon. [Source 1](https://github.com/Blaizzy/mlx-audio) [Source 2](https://pypi.org/project/mlx-audio/)

### What it is good for

Create local narration and transcriptions, or experiment with voice conversion and separation using a supported model. [Source 1](https://github.com/Blaizzy/mlx-audio) [Source 2](https://pypi.org/project/mlx-audio/)

### Demo & examples

The README provides model-specific examples and links a web interface; these examples were documentation-reviewed. [Source 1](https://github.com/Blaizzy/mlx-audio) [Source 2](https://pypi.org/project/mlx-audio/)

### Install

Follow the reviewed project route below; these steps are documentation guidance and were not executed. [Source 1](https://github.com/Blaizzy/mlx-audio) [Source 2](https://pypi.org/project/mlx-audio/)

1. Install Python 3.10+ and pip install mlx-audio on a supported Apple Silicon Mac.
2. Install FFmpeg when working with MP3, FLAC, OGG or Opus; WAV handling does not require it.
3. Choose a supported model and review its own model card before the first download.

```sh
pip install mlx-audio
```


```sh
mlx_audio.tts.generate --model mlx-community/Qwen3-TTS-12Hz-0.6B-CustomVoice-8bit --text 'A short narration test.' --voice Vivian
```

### First project

A small first project that exercises the documented creative workflow. [Source 1](https://github.com/Blaizzy/mlx-audio) [Source 2](https://pypi.org/project/mlx-audio/)

1. Generate a short narration with the documented mlx_audio.tts.generate command.
2. Listen to the output and adjust the selected model's voice or generation settings.
3. Use --save when streaming if an output file is required.
### Hardware & software

Requirements are source-specific. Unreported capacities and untested platforms are not inferred. [Source 1](https://github.com/Blaizzy/mlx-audio) [Source 2](https://pypi.org/project/mlx-audio/)

- **Hardware:** Apple Silicon is the documented target. Minimum unified memory and free disk depend on the model and are not specified universally.
- **Software:** Python 3.10+, MLX and model dependencies; optional FFmpeg and server extras.
- **Platforms:** Apple Silicon macOS; the separate Swift integration has its own setup. Windows/Linux inference support is not established by this README.

### License, model weights & costs

The complete software license was archived and reviewed. Keep software, model weights, dependencies and hosted-service terms separate. [Source 1](https://github.com/Blaizzy/mlx-audio/blob/main/LICENSE) [Source 2](https://github.com/Blaizzy/mlx-audio) [Source 3](https://pypi.org/project/mlx-audio/)

- **Code:** MIT
- **Weights:** Every downloaded speech/music model has independent terms; MIT applies to the toolkit.
- **Commercial:** The reviewed MIT software license permits commercial use subject to its license, notice and source-sharing obligations where applicable. This does not establish permission for every model, input, output or service.
- **Cost:** Local compute/storage; no paid inference service is required for the documented local model path.

### Why it merits attention

Model-specific CLI/API examples and Apple-native execution address a concrete non-CUDA workflow. [Source 1](https://github.com/Blaizzy/mlx-audio) [Source 2](https://pypi.org/project/mlx-audio/)

### Limitations

Support and memory needs vary by model. Voice quality and latency were not benchmarked. This edition is a documentation review, not an installation or output-quality test. [Source 1](https://github.com/Blaizzy/mlx-audio) [Source 2](https://pypi.org/project/mlx-audio/)

### Get the tool

- [Repository](https://github.com/Blaizzy/mlx-audio)
- [License](https://github.com/Blaizzy/mlx-audio/blob/main/LICENSE)
- [Documentation](https://pypi.org/project/mlx-audio/)

## Resonant

Audio, music & voice · Editing, captions & post-production · Performance, projection & stage media

First detailed guide in this library. This is a documentation baseline, not a claim that the project launched today.

### How it uses AI

A music workstation combines arrangement and mixing with local ACE-Step song generation and optional Seed-VC voice conversion. Creative use: Generate song ideas, arrange clips and export a reviewed WAV mix. [Source](https://github.com/calesthio/Resonant) [Source](https://github.com/calesthio/Resonant/blob/main/THIRD_PARTY_NOTICES.md)

### Introduction

A music workstation combines arrangement and mixing with local ACE-Step song generation and optional Seed-VC voice conversion. [Source 1](https://github.com/calesthio/Resonant) [Source 2](https://github.com/calesthio/Resonant/blob/main/THIRD_PARTY_NOTICES.md)

### What it is good for

Generate song ideas, arrange clips and export a reviewed WAV mix. [Source 1](https://github.com/calesthio/Resonant) [Source 2](https://github.com/calesthio/Resonant/blob/main/THIRD_PARTY_NOTICES.md)

### Demo & examples

The README includes three music examples and workstation screenshots. [Source 1](https://github.com/calesthio/Resonant) [Source 2](https://github.com/calesthio/Resonant/blob/main/THIRD_PARTY_NOTICES.md)

### Install

Follow the reviewed project route below; these steps are documentation guidance and were not executed. [Source 1](https://github.com/calesthio/Resonant) [Source 2](https://github.com/calesthio/Resonant/blob/main/THIRD_PARTY_NOTICES.md)

1. Download the official Windows installer or portable release.
2. Use the AI Song controls to install the optional ACE-Step runtime and model files.
3. For source development, use Node.js 22+, npm ci and the documented development/build scripts.
### First project

A small first project that exercises the documented creative workflow. [Source 1](https://github.com/calesthio/Resonant) [Source 2](https://github.com/calesthio/Resonant/blob/main/THIRD_PARTY_NOTICES.md)

1. Generate a short song from lyrics, style and duration controls.
2. Arrange and edit the result in the timeline or clip launcher.
3. Balance tracks and export WAV; inspect voice-conversion output separately if enabled.
### Hardware & software

Requirements are source-specific. Unreported capacities and untested platforms are not inferred. [Source 1](https://github.com/calesthio/Resonant) [Source 2](https://github.com/calesthio/Resonant/blob/main/THIRD_PARTY_NOTICES.md)

- **Hardware:** Multicore CPU and audio output for the workstation. ACE-Step recommends 6–8 GB VRAM; Seed-VC lists 6 GB minimum/8 GB recommended. Its AI runtime is about 5 GB before weights; total RAM and storage minimums are not specified.
- **Software:** Windows 10/11 x64; optional downloaded AI runtimes. Node.js 22+ is for building from source.
- **Platforms:** Current packaged support is Windows x64. macOS/Linux packages are not established by the reviewed documentation.

### License, model weights & costs

The complete software license was archived and reviewed. Keep software, model weights, dependencies and hosted-service terms separate. [Source 1](https://github.com/calesthio/Resonant/blob/main/LICENSE) [Source 2](https://github.com/calesthio/Resonant) [Source 3](https://github.com/calesthio/Resonant/blob/main/THIRD_PARTY_NOTICES.md)

- **Code:** AGPL-3.0
- **Weights:** ACE-Step, Seed-VC checkpoints, instrument packs and imported samples retain independent terms. Seed-VC source is GPL-3.0.
- **Commercial:** The reviewed AGPL-3.0 software license permits commercial use subject to its license, notice and source-sharing obligations where applicable. This does not establish permission for every model, input, output or service.
- **Cost:** AGPL-3.0 software; local hardware and optional external agent/model services are separate.

### Why it merits attention

A complete arrangement/export surface and optional local generation are more useful than a stand-alone generation form. [Source 1](https://github.com/calesthio/Resonant) [Source 2](https://github.com/calesthio/Resonant/blob/main/THIRD_PARTY_NOTICES.md)

### Limitations

Unsigned emerging releases; performance and musical quality have not been tested here. Sample and weight rights are not covered by the app license. This edition is a documentation review, not an installation or output-quality test. [Source 1](https://github.com/calesthio/Resonant) [Source 2](https://github.com/calesthio/Resonant/blob/main/THIRD_PARTY_NOTICES.md)

### Get the tool

- [Repository](https://github.com/calesthio/Resonant)
- [License](https://github.com/calesthio/Resonant/blob/main/LICENSE)
- [Documentation](https://github.com/calesthio/Resonant/blob/main/THIRD_PARTY_NOTICES.md)

## AI Audio Descriptions

Accessible media & assistive creation · Video, animation & film · Audio, music & voice · Editing, captions & post-production

First detailed guide in this library. This is a documentation baseline, not a claim that the project launched today.

### How it uses AI

An AI-assisted pipeline drafts editable video descriptions, synthesizes narration and mixes it into an MP4 with audio ducking. Creative use: Create a reviewed audio-description track for an exhibition film, tutorial or short video. [Source](https://github.com/microsoft/ai-audio-descriptions)

### Introduction

An AI-assisted pipeline drafts editable video descriptions, synthesizes narration and mixes it into an MP4 with audio ducking. [Source 1](https://github.com/microsoft/ai-audio-descriptions)

### What it is good for

Create a reviewed audio-description track for an exhibition film, tutorial or short video. [Source 1](https://github.com/microsoft/ai-audio-descriptions)

### Demo & examples

The README links sample MP4 outputs and shows its description-editing Studio. [Source 1](https://github.com/microsoft/ai-audio-descriptions)

### Install

Follow the reviewed project route below; these steps are documentation guidance and were not executed. [Source 1](https://github.com/microsoft/ai-audio-descriptions)

1. Install Python, Node.js 20.19+, FFmpeg/ffprobe and Azure Developer CLI.
2. Provision the documented Azure Foundry/Speech resources and configure credentials locally; provisioning may incur charges.
3. Install Python and Studio dependencies, then start the documented development server.

```sh
python -m cli.generate_ad input.mp4 output.vtt
```


```sh
python -m cli.render_ad input.mp4 output.vtt output.mp4
```

### First project

A small first project that exercises the documented creative workflow. [Source 1](https://github.com/microsoft/ai-audio-descriptions)

1. Generate a WebVTT description draft with cli.generate_ad.
2. Review accuracy, omissions and narration windows in Studio.
3. Render the approved VTT with cli.render_ad, then listen to the complete mixed result.
### Hardware & software

Requirements are source-specific. Unreported capacities and untested platforms are not inferred. [Source 1](https://github.com/microsoft/ai-audio-descriptions)

- **Hardware:** CPU, GPU, RAM, VRAM and disk minimums are not documented. Model inference uses configured Azure services.
- **Software:** Python (version not specified in the reviewed README), Node.js 20.19+, FFmpeg/ffprobe and Azure services.
- **Platforms:** Windows-style setup examples are provided; a tested OS matrix is not published. The browser UI does not establish host compatibility.

### License, model weights & costs

The complete software license was archived and reviewed. Keep software, model weights, dependencies and hosted-service terms separate. [Source 1](https://github.com/microsoft/ai-audio-descriptions/blob/main/license.md) [Source 2](https://github.com/microsoft/ai-audio-descriptions)

- **Code:** MIT
- **Weights:** No bundled open model weights; Azure model/service terms apply independently.
- **Commercial:** The reviewed MIT software license permits commercial use subject to its license, notice and source-sharing obligations where applicable. This does not establish permission for every model, input, output or service.
- **Cost:** MIT source; Azure hosting, language-model and speech usage can cost money.

### Why it merits attention

Human-editable timing and text plus a separate render stage support meaningful accessibility review. [Source 1](https://github.com/microsoft/ai-audio-descriptions)

### Limitations

Generated descriptions can miss or misdescribe important action. The optional description-isolation workflow is approximate. This edition is a documentation review, not an installation or output-quality test. [Source 1](https://github.com/microsoft/ai-audio-descriptions)

### Get the tool

- [Repository](https://github.com/microsoft/ai-audio-descriptions)
- [License](https://github.com/microsoft/ai-audio-descriptions/blob/main/license.md)

## Sprite Studio

Games & production pipelines · Images & design · Motion capture & character animation · AI agents for code-authored media production

First detailed guide in this library. This is a documentation baseline, not a claim that the project launched today.

### How it uses AI

An AI-assisted desktop workspace generates sprites, proposes rigs, tests animation loops and exports sprite sheets with metadata. Creative use: Develop a coherent character pack and a usable animation loop while retaining editable source assets. [Source](https://github.com/JohnKinyanjui/sprite-maker)

### Introduction

An AI-assisted desktop workspace generates sprites, proposes rigs, tests animation loops and exports sprite sheets with metadata. [Source 1](https://github.com/JohnKinyanjui/sprite-maker)

### What it is good for

Develop a coherent character pack and a usable animation loop while retaining editable source assets. [Source 1](https://github.com/JohnKinyanjui/sprite-maker)

### Demo & examples

The README shows rabbit, dragon and centipede animations plus a coordinated asset pack. [Source 1](https://github.com/JohnKinyanjui/sprite-maker)

### Install

Follow the reviewed project route below; these steps are documentation guidance and were not executed. [Source 1](https://github.com/JohnKinyanjui/sprite-maker)

1. Choose the official desktop package for your OS and processor.
2. Install and authenticate a supported Codex, Cursor or Antigravity CLI for AI features.
3. For a source build, install Bun, stable Rust and Tauri 2 platform dependencies; use bun install and bun tauri dev.
### First project

A small first project that exercises the documented creative workflow. [Source 1](https://github.com/JohnKinyanjui/sprite-maker)

1. Generate or import a character and approve a master identity anchor.
2. Ask for a rig or animation; use the deterministic native rig renderer when appropriate.
3. Normalize and align frames, test the loop, accept it and export PNG sheets plus metadata.
### Hardware & software

Requirements are source-specific. Unreported capacities and untested platforms are not inferred. [Source 1](https://github.com/JohnKinyanjui/sprite-maker)

- **Hardware:** Minimum RAM, VRAM, GPU and disk capacity are not documented; local rig rendering and external image inference have separate costs.
- **Software:** Desktop release plus an authenticated supported agent CLI. Source builds require Bun, Rust and Tauri dependencies.
- **Platforms:** macOS Intel/Apple Silicon, Windows and Linux build routes are documented. Android/iOS are explicitly outside scope.

### License, model weights & costs

The complete software license was archived and reviewed. Keep software, model weights, dependencies and hosted-service terms separate. [Source 1](https://github.com/JohnKinyanjui/sprite-maker/blob/main/LICENSE) [Source 2](https://github.com/JohnKinyanjui/sprite-maker)

- **Code:** MIT
- **Weights:** The workbench does not grant rights to the selected agent/image model or reference assets.
- **Commercial:** The reviewed MIT software license permits commercial use subject to its license, notice and source-sharing obligations where applicable. This does not establish permission for every model, input, output or service.
- **Cost:** MIT software; external agent/image services may cost money. Native rig frames do not invoke image generation.

### Why it merits attention

Identity anchors, alignment checks and loop testing address the gap between attractive images and reusable game assets. [Source 1](https://github.com/JohnKinyanjui/sprite-maker)

### Limitations

Agent output still needs art direction. Native IK rendering is deterministic animation, not a learned motion model. This edition is a documentation review, not an installation or output-quality test. [Source 1](https://github.com/JohnKinyanjui/sprite-maker)

### Get the tool

- [Repository](https://github.com/JohnKinyanjui/sprite-maker)
- [License](https://github.com/JohnKinyanjui/sprite-maker/blob/main/LICENSE)

## OpenVJ

Performance, projection & stage media · Physical, robotic & kinetic installations · Interactive, immersive & live media · Browser tools & web media · Computational art & creative coding

First detailed guide in this library. This is a documentation baseline, not a claim that the project launched today.

### How it uses AI

A projection-mapping and live-visuals workspace includes AI-assisted GLSL shader generation alongside audio/MIDI controls. Creative use: Prototype audio-reactive stage visuals and map generated shaders onto surfaces. [Source](https://github.com/kniessner/openvj)

### Introduction

A projection-mapping and live-visuals workspace includes AI-assisted GLSL shader generation alongside audio/MIDI controls. [Source 1](https://github.com/kniessner/openvj)

### What it is good for

Prototype audio-reactive stage visuals and map generated shaders onto surfaces. [Source 1](https://github.com/kniessner/openvj)

### Demo & examples

The local quick start opens a bundled demo scene; no live projector test was performed. [Source 1](https://github.com/kniessner/openvj)

### Install

Follow the reviewed project route below; these steps are documentation guidance and were not executed. [Source 1](https://github.com/kniessner/openvj)

1. Install Node.js 18+ and clone the repository.
2. Run npm install, then npm run dev.
3. Open the displayed local address (documented port 5173); configure an Anthropic API key only if using AI shader generation.
### First project

A small first project that exercises the documented creative workflow. [Source 1](https://github.com/kniessner/openvj)

1. Add a surface and adjust its projection corners.
2. Describe a shader, inspect the generated code/preview and connect audio or MIDI modulation.
3. Save the project JSON and test fullscreen output on the intended display.
### Hardware & software

Requirements are source-specific. Unreported capacities and untested platforms are not inferred. [Source 1](https://github.com/kniessner/openvj)

- **Hardware:** A compatible browser/GPU and optional projector/MIDI controller; numeric RAM, VRAM and disk minimums are not documented.
- **Software:** Node.js 18+ for local development. Browser support is claimed for Chrome, Firefox, Edge and Safari, but WebMIDI and GPU features vary.
- **Platforms:** Browser-based; no tested desktop OS/hardware matrix is published.

### License, model weights & costs

The complete software license was archived and reviewed. Keep software, model weights, dependencies and hosted-service terms separate. [Source 1](https://github.com/kniessner/openvj/blob/main/LICENSE) [Source 2](https://github.com/kniessner/openvj)

- **Code:** MIT
- **Weights:** No local AI weights are supplied; AI shader generation uses Anthropic's service.
- **Commercial:** The reviewed MIT software license permits commercial use subject to its license, notice and source-sharing obligations where applicable. This does not establish permission for every model, input, output or service.
- **Cost:** MIT application; API usage and show hardware are separate costs.

### Why it merits attention

Direct shader editing and surface/audio controls connect AI generation to an actual live-media workflow. [Source 1](https://github.com/kniessner/openvj)

### Limitations

Beta software; browser feature claims and show reliability need device testing. Built-in procedural presets are not themselves AI. This edition is a documentation review, not an installation or output-quality test. [Source 1](https://github.com/kniessner/openvj)

### Get the tool

- [Repository](https://github.com/kniessner/openvj)
- [License](https://github.com/kniessner/openvj/blob/main/LICENSE)

## Neural Fourier Shift

Neural acoustics and responsive sound spaces · Spatial audio & volumetric media · Audio, music & voice · WebXR, VR & AR

First detailed guide in this library. This is a documentation baseline, not a claim that the project launched today.

### How it uses AI

A neural rendering model converts mono speech into binaural audio conditioned on source positions. Creative use: Prototype a moving spatial voice for headphones, virtual scenes or an immersive audio piece. [Source](https://github.com/jin-woo-lee/nfs-binaural) [Source](https://arxiv.org/abs/2211.00878)

### Introduction

A neural rendering model converts mono speech into binaural audio conditioned on source positions. [Source 1](https://github.com/jin-woo-lee/nfs-binaural) [Source 2](https://arxiv.org/abs/2211.00878)

### What it is good for

Prototype a moving spatial voice for headphones, virtual scenes or an immersive audio piece. [Source 1](https://github.com/jin-woo-lee/nfs-binaural) [Source 2](https://arxiv.org/abs/2211.00878)

### Demo & examples

The repository supplies a demo-video script and a released pretrained model. [Source 1](https://github.com/jin-woo-lee/nfs-binaural) [Source 2](https://arxiv.org/abs/2211.00878)

### Install

Follow the reviewed project route below; these steps are documentation guidance and were not executed. [Source 1](https://github.com/jin-woo-lee/nfs-binaural) [Source 2](https://arxiv.org/abs/2211.00878)

1. Clone the repository and install requirements.txt in an isolated environment.
2. Download the official v1.0.0 checkpoint.
3. Prepare mono WAV inputs and optional position text files; dataset preparation is needed for training/evaluation, not every custom render.

```sh
python render.py --gpu 0 --ckpt path/to/model.pt --root_dir path/to/mono --save_dir path/to/output
```

### First project

A small first project that exercises the documented creative workflow. [Source 1](https://github.com/jin-woo-lee/nfs-binaural) [Source 2](https://arxiv.org/abs/2211.00878)

1. Run render.py with checkpoint, input directory and output directory.
2. Provide a position path, or use its documented circular-motion example.
3. Listen on headphones and compare with the mono original before using the result.
### Hardware & software

Requirements are source-specific. Unreported capacities and untested platforms are not inferred. [Source 1](https://github.com/jin-woo-lee/nfs-binaural) [Source 2](https://arxiv.org/abs/2211.00878)

- **Hardware:** The authors tested RTX 2080 with CUDA 11.2. That is a tested setup, not a stated minimum. RAM, VRAM and disk requirements are otherwise undocumented.
- **Software:** Python dependencies from requirements.txt and CUDA-capable PyTorch; Python version is not stated in the README.
- **Platforms:** CUDA GPU path documented; no verified macOS/Windows/Linux support matrix.

### License, model weights & costs

The complete software license was archived and reviewed. Keep software, model weights, dependencies and hosted-service terms separate. [Source 1](https://github.com/jin-woo-lee/nfs-binaural/blob/main/LICENSE) [Source 2](https://github.com/jin-woo-lee/nfs-binaural) [Source 3](https://arxiv.org/abs/2211.00878)

- **Code:** MIT
- **Weights:** MIT code; the separately released checkpoint and external binaural dataset require their own terms reviewed before redistribution.
- **Commercial:** The reviewed MIT software license permits commercial use subject to its license, notice and source-sharing obligations where applicable. This does not establish permission for every model, input, output or service.
- **Cost:** Local compute and storage; no paid inference API is documented.

### Why it merits attention

A concrete arbitrary-WAV rendering entry point makes the research practical to inspect. [Source 1](https://github.com/jin-woo-lee/nfs-binaural) [Source 2](https://arxiv.org/abs/2211.00878)

### Limitations

Designed around binaural speech; performance on music and arbitrary room acoustics is not established. This edition is a documentation review, not an installation or output-quality test. [Source 1](https://github.com/jin-woo-lee/nfs-binaural) [Source 2](https://arxiv.org/abs/2211.00878)

### Get the tool

- [Repository](https://github.com/jin-woo-lee/nfs-binaural)
- [License](https://github.com/jin-woo-lee/nfs-binaural/blob/main/LICENSE)
- [Documentation](https://arxiv.org/abs/2211.00878)

## MMagic

Images & design · Video, animation & film · VFX, compositing & relighting · Photography, restoration & color · Archives, media restoration & collections

First detailed guide, completing an earlier screened lead. This is a documentation baseline, not a claim that the project launched today.

### How it uses AI

A PyTorch toolbox provides model inference and training workflows for generation, restoration, super-resolution, matting and other image/video tasks. Creative use: Compare restoration methods or build a reproducible media-processing experiment. [Source](https://github.com/open-mmlab/mmagic) [Source](https://mmagic.readthedocs.io/en/latest/) [Source](https://github.com/open-mmlab/mmagic/blob/main/docs/en/get_started/install.md) [Source](https://github.com/open-mmlab/mmagic/blob/main/docs/en/get_started/quick_run.md)

### Introduction

A PyTorch toolbox provides model inference and training workflows for generation, restoration, super-resolution, matting and other image/video tasks. [Source 1](https://github.com/open-mmlab/mmagic) [Source 2](https://mmagic.readthedocs.io/en/latest/) [Source 3](https://github.com/open-mmlab/mmagic/blob/main/docs/en/get_started/install.md) [Source 4](https://github.com/open-mmlab/mmagic/blob/main/docs/en/get_started/quick_run.md)

### What it is good for

Compare restoration methods or build a reproducible media-processing experiment. [Source 1](https://github.com/open-mmlab/mmagic) [Source 2](https://mmagic.readthedocs.io/en/latest/) [Source 3](https://github.com/open-mmlab/mmagic/blob/main/docs/en/get_started/install.md) [Source 4](https://github.com/open-mmlab/mmagic/blob/main/docs/en/get_started/quick_run.md)

### Demo & examples

Official documentation includes text-to-image and ESRGAN examples; model-specific documentation supplies further demonstrations. [Source 1](https://github.com/open-mmlab/mmagic) [Source 2](https://mmagic.readthedocs.io/en/latest/) [Source 3](https://github.com/open-mmlab/mmagic/blob/main/docs/en/get_started/install.md) [Source 4](https://github.com/open-mmlab/mmagic/blob/main/docs/en/get_started/quick_run.md)

### Install

Follow the reviewed project route below; these steps are documentation guidance and were not executed. [Source 1](https://github.com/open-mmlab/mmagic) [Source 2](https://mmagic.readthedocs.io/en/latest/) [Source 3](https://github.com/open-mmlab/mmagic/blob/main/docs/en/get_started/install.md) [Source 4](https://github.com/open-mmlab/mmagic/blob/main/docs/en/get_started/quick_run.md)

1. Prepare a compatible Python/PyTorch environment.
2. Install OpenMIM, MMCV 2.0+ and MMEngine, then install mmagic.
3. Check the selected model's configuration, checkpoint and dependency compatibility before inference.

```sh
pip install -U openmim
```


```sh
mim install 'mmcv>=2.0.0'
```


```sh
mim install mmengine
```


```sh
mim install mmagic
```

### First project

A small first project that exercises the documented creative workflow. [Source 1](https://github.com/open-mmlab/mmagic) [Source 2](https://mmagic.readthedocs.io/en/latest/) [Source 3](https://github.com/open-mmlab/mmagic/blob/main/docs/en/get_started/install.md) [Source 4](https://github.com/open-mmlab/mmagic/blob/main/docs/en/get_started/quick_run.md)

1. Start with the documented MMagicInferencer example.
2. Choose a restoration or generation model and supply a small test input.
3. Save the result and compare fine detail, temporal behavior and artifacts against the original.
### Hardware & software

Requirements are source-specific. Unreported capacities and untested platforms are not inferred. [Source 1](https://github.com/open-mmlab/mmagic) [Source 2](https://mmagic.readthedocs.io/en/latest/) [Source 3](https://github.com/open-mmlab/mmagic/blob/main/docs/en/get_started/install.md) [Source 4](https://github.com/open-mmlab/mmagic/blob/main/docs/en/get_started/quick_run.md)

- **Hardware:** CPU and GPU setup paths are documented. No universal RAM, VRAM or disk minimum covers the different models.
- **Software:** Published prerequisites: Python 3.7+, PyTorch 1.8+, MMCV 2.0+ and MMEngine. The install examples include older pinned stacks; current package compatibility must be checked.
- **Platforms:** Official documentation lists Linux, Windows and macOS. Availability of a particular CUDA operator/model is separate.

### License, model weights & costs

The complete software license was archived and reviewed. Keep software, model weights, dependencies and hosted-service terms separate. [Source 1](https://github.com/open-mmlab/mmagic/blob/main/LICENSE) [Source 2](https://github.com/open-mmlab/mmagic) [Source 3](https://mmagic.readthedocs.io/en/latest/) [Source 4](https://github.com/open-mmlab/mmagic/blob/main/docs/en/get_started/install.md) [Source 5](https://github.com/open-mmlab/mmagic/blob/main/docs/en/get_started/quick_run.md)

- **Code:** Apache-2.0
- **Weights:** Apache-2.0 toolbox; each checkpoint, dataset and third-party dependency retains its own terms.
- **Commercial:** The reviewed Apache-2.0 software license permits commercial use subject to its license, notice and source-sharing obligations where applicable. This does not establish permission for every model, input, output or service.
- **Cost:** Local compute/storage; optional external model downloads/services are separate.

### Why it merits attention

Configuration-driven models and published inference examples support repeatable comparisons. [Source 1](https://github.com/open-mmlab/mmagic) [Source 2](https://mmagic.readthedocs.io/en/latest/) [Source 3](https://github.com/open-mmlab/mmagic/blob/main/docs/en/get_started/install.md) [Source 4](https://github.com/open-mmlab/mmagic/blob/main/docs/en/get_started/quick_run.md)

### Limitations

A research toolkit rather than a universal one-click editor. Enhancement can invent details; archival fidelity requires comparison. This edition is a documentation review, not an installation or output-quality test. [Source 1](https://github.com/open-mmlab/mmagic) [Source 2](https://mmagic.readthedocs.io/en/latest/) [Source 3](https://github.com/open-mmlab/mmagic/blob/main/docs/en/get_started/install.md) [Source 4](https://github.com/open-mmlab/mmagic/blob/main/docs/en/get_started/quick_run.md)

### Get the tool

- [Repository](https://github.com/open-mmlab/mmagic)
- [License](https://github.com/open-mmlab/mmagic/blob/main/LICENSE)
- [Documentation](https://mmagic.readthedocs.io/en/latest/)

## LichtFeld Studio

3D, reconstruction & assets · Photogrammetry, scanning & neural rendering · Spatial audio & volumetric media · Editing, captions & post-production

First detailed guide, completing an earlier screened lead. This is a documentation baseline, not a claim that the project launched today.

### How it uses AI

A CUDA application trains and edits Gaussian scene reconstructions, with neural preprocessing and multiple scene-export formats. Creative use: Turn a posed photo set into a spatial asset and clean it up for viewing or later production. [Source](https://github.com/MrNeRF/LichtFeld-Studio) [Source](https://github.com/MrNeRF/LichtFeld-Studio/blob/master/docs/building_and_distribution.md)

### Introduction

A CUDA application trains and edits Gaussian scene reconstructions, with neural preprocessing and multiple scene-export formats. [Source 1](https://github.com/MrNeRF/LichtFeld-Studio) [Source 2](https://github.com/MrNeRF/LichtFeld-Studio/blob/master/docs/building_and_distribution.md)

### What it is good for

Turn a posed photo set into a spatial asset and clean it up for viewing or later production. [Source 1](https://github.com/MrNeRF/LichtFeld-Studio) [Source 2](https://github.com/MrNeRF/LichtFeld-Studio/blob/master/docs/building_and_distribution.md)

### Demo & examples

The README shows training/editing workflows and published scene examples. [Source 1](https://github.com/MrNeRF/LichtFeld-Studio) [Source 2](https://github.com/MrNeRF/LichtFeld-Studio/blob/master/docs/building_and_distribution.md)

### Install

Follow the reviewed project route below; these steps are documentation guidance and were not executed. [Source 1](https://github.com/MrNeRF/LichtFeld-Studio) [Source 2](https://github.com/MrNeRF/LichtFeld-Studio/blob/master/docs/building_and_distribution.md)

1. For a packaged Windows build, use the project's portal and review its access terms.
2. For a free source build, clone the project and install CUDA 12.8+, CMake 3.30+, vcpkg and the documented compiler.
3. Build with CMake; Linux also needs a working X11 or Wayland GUI stack.

```sh
cmake -B build
```


```sh
cmake --build build -j 16
```


```sh
./build/LichtFeld-Studio -d /path/to/data -o /path/to/output
```

### First project

A small first project that exercises the documented creative workflow. [Source 1](https://github.com/MrNeRF/LichtFeld-Studio) [Source 2](https://github.com/MrNeRF/LichtFeld-Studio/blob/master/docs/building_and_distribution.md)

1. Load a supported COLMAP dataset and choose an output project.
2. Train the scene, inspect weak areas and use selection/editing controls.
3. Export a supported scene format and verify it in the intended viewer.
### Hardware & software

Requirements are source-specific. Unreported capacities and untested platforms are not inferred. [Source 1](https://github.com/MrNeRF/LichtFeld-Studio) [Source 2](https://github.com/MrNeRF/LichtFeld-Studio/blob/master/docs/building_and_distribution.md)

- **Hardware:** NVIDIA compute capability 7.5+ (Turing-class) and driver 570+ are documented. AMD/Intel GPUs and GTX 10-series are not supported by the default build. Numeric RAM/VRAM minimums are not specified.
- **Software:** CUDA 12.8+, CMake 3.30+, vcpkg; GCC 14+ on Linux or Visual Studio 2022 v17.10+ with the documented Clang component on Windows.
- **Platforms:** Windows and Linux. No macOS training support is documented.

### License, model weights & costs

The complete software license was archived and reviewed. Keep software, model weights, dependencies and hosted-service terms separate. [Source 1](https://github.com/MrNeRF/LichtFeld-Studio/blob/master/LICENSE) [Source 2](https://github.com/MrNeRF/LichtFeld-Studio) [Source 3](https://github.com/MrNeRF/LichtFeld-Studio/blob/master/docs/building_and_distribution.md)

- **Code:** GPL-3.0
- **Weights:** GPL-3.0 source; optional MoGe-2 preprocessing weights and scene data retain separate terms.
- **Commercial:** The reviewed GPL-3.0 software license permits commercial use subject to its license, notice and source-sharing obligations where applicable. This does not establish permission for every model, input, output or service.
- **Cost:** Source builds are free of license fees; Windows prebuilt access through the project portal requires a donation. GPU hardware is separate.

### Why it merits attention

Training, editing and export in one native interface can reduce scene-preparation friction. [Source 1](https://github.com/MrNeRF/LichtFeld-Studio) [Source 2](https://github.com/MrNeRF/LichtFeld-Studio/blob/master/docs/building_and_distribution.md)

### Limitations

A Gaussian scene is not a watertight printing mesh. Browser export compatibility and reconstruction quality need project-specific testing. This edition is a documentation review, not an installation or output-quality test. [Source 1](https://github.com/MrNeRF/LichtFeld-Studio) [Source 2](https://github.com/MrNeRF/LichtFeld-Studio/blob/master/docs/building_and_distribution.md)

### Get the tool

- [Repository](https://github.com/MrNeRF/LichtFeld-Studio)
- [License](https://github.com/MrNeRF/LichtFeld-Studio/blob/master/LICENSE)
- [Documentation](https://github.com/MrNeRF/LichtFeld-Studio/blob/master/docs/building_and_distribution.md)

## Lyra 2

3D, reconstruction & assets · Video, animation & film · Photogrammetry, scanning & neural rendering · WebXR, VR & AR

First detailed guide, completing an earlier screened lead. This is a documentation baseline, not a claim that the project launched today.

### How it uses AI

A camera-controlled video-generation and reconstruction pipeline creates explorable scene representations from an image. Creative use: Experiment with imagined spaces and camera paths for previsualization. [Source](https://github.com/nv-tlabs/lyra) [Source](https://github.com/nv-tlabs/lyra/blob/main/Lyra-2/README.md) [Source](https://github.com/nv-tlabs/lyra/blob/main/Lyra-2/INSTALL.md) [Source](https://github.com/nv-tlabs/lyra/blob/main/Lyra-2/gui/README.md)

### Introduction

A camera-controlled video-generation and reconstruction pipeline creates explorable scene representations from an image. [Source 1](https://github.com/nv-tlabs/lyra) [Source 2](https://github.com/nv-tlabs/lyra/blob/main/Lyra-2/README.md) [Source 3](https://github.com/nv-tlabs/lyra/blob/main/Lyra-2/INSTALL.md) [Source 4](https://github.com/nv-tlabs/lyra/blob/main/Lyra-2/gui/README.md)

### What it is good for

Experiment with imagined spaces and camera paths for previsualization. [Source 1](https://github.com/nv-tlabs/lyra) [Source 2](https://github.com/nv-tlabs/lyra/blob/main/Lyra-2/README.md) [Source 3](https://github.com/nv-tlabs/lyra/blob/main/Lyra-2/INSTALL.md) [Source 4](https://github.com/nv-tlabs/lyra/blob/main/Lyra-2/gui/README.md)

### Demo & examples

The repository links project demonstrations and a GUI for authoring camera paths; the project site's new address was inaccessible during this check. [Source 1](https://github.com/nv-tlabs/lyra) [Source 2](https://github.com/nv-tlabs/lyra/blob/main/Lyra-2/README.md) [Source 3](https://github.com/nv-tlabs/lyra/blob/main/Lyra-2/INSTALL.md) [Source 4](https://github.com/nv-tlabs/lyra/blob/main/Lyra-2/gui/README.md)

### Install

Follow the reviewed project route below; these steps are documentation guidance and were not executed. [Source 1](https://github.com/nv-tlabs/lyra) [Source 2](https://github.com/nv-tlabs/lyra/blob/main/Lyra-2/README.md) [Source 3](https://github.com/nv-tlabs/lyra/blob/main/Lyra-2/INSTALL.md) [Source 4](https://github.com/nv-tlabs/lyra/blob/main/Lyra-2/gui/README.md)

1. Clone recursively and follow Lyra-2/INSTALL.md in its Conda environment.
2. Use the documented Python 3.10, Torch 2.7.1 and CUDA 12.8 stack and build required extensions.
3. Download the separate NVIDIA checkpoints after reviewing their research-only model terms.
### First project

A small first project that exercises the documented creative workflow. [Source 1](https://github.com/nv-tlabs/lyra) [Source 2](https://github.com/nv-tlabs/lyra/blob/main/Lyra-2/README.md) [Source 3](https://github.com/nv-tlabs/lyra/blob/main/Lyra-2/INSTALL.md) [Source 4](https://github.com/nv-tlabs/lyra/blob/main/Lyra-2/gui/README.md)

1. Load an image and author camera keyframes in the supplied GUI.
2. Generate a short video and inspect consistency.
3. Export the video and run the documented reconstruction path; inspect geometry before reuse.
### Hardware & software

Requirements are source-specific. Unreported capacities and untested platforms are not inferred. [Source 1](https://github.com/nv-tlabs/lyra) [Source 2](https://github.com/nv-tlabs/lyra/blob/main/Lyra-2/README.md) [Source 3](https://github.com/nv-tlabs/lyra/blob/main/Lyra-2/INSTALL.md) [Source 4](https://github.com/nv-tlabs/lyra/blob/main/Lyra-2/gui/README.md)

- **Hardware:** Tested on NVIDIA H100 GPUs. The README's 80 GB H100 timing example is not a minimum specification. RAM, minimum VRAM and disk capacity are not established.
- **Software:** Ubuntu 22.04 test environment, Python 3.10, Torch 2.7.1, CUDA 12.8, Flash Attention and compiled reconstruction dependencies.
- **Platforms:** Linux/NVIDIA. Other Linux/CUDA 12.4+ setups are described as expected but unverified. The GUI also requires Linux/CUDA; no Mac/Windows support claim.

### License, model weights & costs

The complete software license was archived and reviewed. Keep software, model weights, dependencies and hosted-service terms separate. [Source 1](https://github.com/nv-tlabs/lyra/blob/main/LICENSE) [Source 2](https://github.com/nv-tlabs/lyra) [Source 3](https://github.com/nv-tlabs/lyra/blob/main/Lyra-2/README.md) [Source 4](https://github.com/nv-tlabs/lyra/blob/main/Lyra-2/INSTALL.md) [Source 5](https://github.com/nv-tlabs/lyra/blob/main/Lyra-2/gui/README.md)

- **Code:** Apache-2.0
- **Weights:** NVIDIA Internal Scientific Research and Development Model License applies to released Lyra weights; Apache-2.0 code does not grant commercial model use.
- **Commercial:** The reviewed Apache-2.0 software license permits commercial use subject to its license, notice and source-sharing obligations where applicable. This does not establish permission for every model, input, output or service.
- **Cost:** Substantial GPU resources and storage; no source license fee.

### Why it merits attention

Camera authoring plus reconstruction forms a concrete scene-exploration experiment. [Source 1](https://github.com/nv-tlabs/lyra) [Source 2](https://github.com/nv-tlabs/lyra/blob/main/Lyra-2/README.md) [Source 3](https://github.com/nv-tlabs/lyra/blob/main/Lyra-2/INSTALL.md) [Source 4](https://github.com/nv-tlabs/lyra/blob/main/Lyra-2/gui/README.md)

### Limitations

Generated geometry can hallucinate; long sequences and accelerated generation trade quality for speed. Research-only weights constrain production deployment. This edition is a documentation review, not an installation or output-quality test. [Source 1](https://github.com/nv-tlabs/lyra) [Source 2](https://github.com/nv-tlabs/lyra/blob/main/Lyra-2/README.md) [Source 3](https://github.com/nv-tlabs/lyra/blob/main/Lyra-2/INSTALL.md) [Source 4](https://github.com/nv-tlabs/lyra/blob/main/Lyra-2/gui/README.md)

### Get the tool

- [Repository](https://github.com/nv-tlabs/lyra)
- [License](https://github.com/nv-tlabs/lyra/blob/main/LICENSE)
- [Documentation](https://github.com/nv-tlabs/lyra/blob/main/Lyra-2/README.md)

## VideoCaptioner

Editing, captions & post-production · Accessible media & assistive creation · Video, animation & film · Audio, music & voice

First detailed guide, completing an earlier screened lead. This is a documentation baseline, not a claim that the project launched today.

### How it uses AI

A desktop/CLI workflow transcribes, segments, translates and burns subtitles into video using local or hosted speech and language models. Creative use: Make reviewed multilingual captions for a tutorial, performance recording or social clip. [Source](https://github.com/WEIFENG2333/VideoCaptioner) [Source](https://weifeng2333.github.io/VideoCaptioner/)

### Introduction

A desktop/CLI workflow transcribes, segments, translates and burns subtitles into video using local or hosted speech and language models. [Source 1](https://github.com/WEIFENG2333/VideoCaptioner) [Source 2](https://weifeng2333.github.io/VideoCaptioner/)

### What it is good for

Make reviewed multilingual captions for a tutorial, performance recording or social clip. [Source 1](https://github.com/WEIFENG2333/VideoCaptioner) [Source 2](https://weifeng2333.github.io/VideoCaptioner/)

### Demo & examples

The README and Chinese documentation show the editor and subtitle workflow. [Source 1](https://github.com/WEIFENG2333/VideoCaptioner) [Source 2](https://weifeng2333.github.io/VideoCaptioner/)

### Install

Follow the reviewed project route below; these steps are documentation guidance and were not executed. [Source 1](https://github.com/WEIFENG2333/VideoCaptioner) [Source 2](https://weifeng2333.github.io/VideoCaptioner/)

1. Use an official release or the documented pip package.
2. Select and configure a speech-recognition backend; download local model files when required.
3. Configure translation/LLM providers only for the features that need them.

```sh
pip install videocaptioner
```


```sh
videocaptioner-gui
```

### First project

A small first project that exercises the documented creative workflow. [Source 1](https://github.com/WEIFENG2333/VideoCaptioner) [Source 2](https://weifeng2333.github.io/VideoCaptioner/)

1. Transcribe a short video with the selected backend.
2. Correct recognition errors and caption timing; optionally translate and proofread.
3. Export subtitle files or synthesize the captioned video.
### Hardware & software

Requirements are source-specific. Unreported capacities and untested platforms are not inferred. [Source 1](https://github.com/WEIFENG2333/VideoCaptioner) [Source 2](https://weifeng2333.github.io/VideoCaptioner/)

- **Hardware:** No numeric RAM, VRAM or storage minimum is stated in the reviewed README; local models vary.
- **Software:** Python for the pip route, selected ASR/LLM dependencies and media-processing tools. The README does not specify a universal Python version.
- **Platforms:** Windows releases and macOS setup instructions are documented. Other platform/backend combinations need separate verification.

### License, model weights & costs

The complete software license was archived and reviewed. Keep software, model weights, dependencies and hosted-service terms separate. [Source 1](https://github.com/WEIFENG2333/VideoCaptioner/blob/master/LICENSE) [Source 2](https://github.com/WEIFENG2333/VideoCaptioner) [Source 3](https://weifeng2333.github.io/VideoCaptioner/)

- **Code:** GPL-3.0
- **Weights:** GPL-3.0 application; downloaded ASR models and hosted translators have their own terms.
- **Commercial:** The reviewed GPL-3.0 software license permits commercial use subject to its license, notice and source-sharing obligations where applicable. This does not establish permission for every model, input, output or service.
- **Cost:** Local inference uses local resources; some hosted translation/recognition routes and LLM features may cost money.

### Why it merits attention

Editable subtitles and independent CLI stages support human review and repeatable processing. [Source 1](https://github.com/WEIFENG2333/VideoCaptioner) [Source 2](https://weifeng2333.github.io/VideoCaptioner/)

### Limitations

Automatic translation and segmentation require proofreading. A free hosted service is not local inference. This edition is a documentation review, not an installation or output-quality test. [Source 1](https://github.com/WEIFENG2333/VideoCaptioner) [Source 2](https://weifeng2333.github.io/VideoCaptioner/)

### Get the tool

- [Repository](https://github.com/WEIFENG2333/VideoCaptioner)
- [License](https://github.com/WEIFENG2333/VideoCaptioner/blob/master/LICENSE)
- [Documentation](https://weifeng2333.github.io/VideoCaptioner/)

## Koharu

Storyboarding, narrative & comics · Typography, fonts & layout · Images & design · Creative publishing & presentation

First detailed guide in this library. This is a documentation baseline, not a claim that the project launched today.

### How it uses AI

A manga workspace combines ML detection, OCR, translation and generative cleanup with manual typesetting and layered export. Creative use: Localize a comic while correcting OCR and preserving editable page layers. [Source](https://github.com/koharu-rs/koharu) [Source](https://koharu.rs/en/installation) [Source](https://koharu.rs/en/hardware)

### Introduction

A manga workspace combines ML detection, OCR, translation and generative cleanup with manual typesetting and layered export. [Source 1](https://github.com/koharu-rs/koharu) [Source 2](https://koharu.rs/en/installation) [Source 3](https://koharu.rs/en/hardware)

### What it is good for

Localize a comic while correcting OCR and preserving editable page layers. [Source 1](https://github.com/koharu-rs/koharu) [Source 2](https://koharu.rs/en/installation) [Source 3](https://koharu.rs/en/hardware)

### Demo & examples

The README shows the interface and official guides walk through a first translated page. [Source 1](https://github.com/koharu-rs/koharu) [Source 2](https://koharu.rs/en/installation) [Source 3](https://koharu.rs/en/hardware)

### Install

Follow the reviewed project route below; these steps are documentation guidance and were not executed. [Source 1](https://github.com/koharu-rs/koharu) [Source 2](https://koharu.rs/en/installation) [Source 3](https://koharu.rs/en/hardware)

1. Download the release matching Windows, Apple-silicon macOS or your Linux distribution.
2. Let its native runtimes initialize; selected models download on first use.
3. Create a project from one readable page before importing a longer work.
### First project

A small first project that exercises the documented creative workflow. [Source 1](https://github.com/koharu-rs/koharu) [Source 2](https://koharu.rs/en/installation) [Source 3](https://koharu.rs/en/hardware)

1. Run detection/OCR, then review the extracted text.
2. Translate with a selected local or hosted model and proofread.
3. Clean source lettering, adjust multilingual typography and export PNG or layered PSD.
### Hardware & software

Requirements are source-specific. Unreported capacities and untested platforms are not inferred. [Source 1](https://github.com/koharu-rs/koharu) [Source 2](https://koharu.rs/en/installation) [Source 3](https://koharu.rs/en/hardware)

- **Hardware:** A working WebGPU adapter is required for the canvas even when inference uses CPU. No universal numeric RAM/VRAM/disk minimum is published.
- **Software:** Managed native runtimes; a full CUDA/ROCm SDK is not required for releases. CUDA 13.3 backend requires Turing-class or newer NVIDIA GPU and R610+ driver according to project docs.
- **Platforms:** Windows/Linux CUDA or ROCm where supported, Apple Silicon Metal, and partial Vulkan/CPU fallback. Some vision models remain CPU-only on a Vulkan-only system.

### License, model weights & costs

The complete software license was archived and reviewed. Keep software, model weights, dependencies and hosted-service terms separate. [Source 1](https://github.com/koharu-rs/koharu/blob/main/LICENSE-APACHE) [Source 2](https://github.com/koharu-rs/koharu) [Source 3](https://koharu.rs/en/installation) [Source 4](https://koharu.rs/en/hardware)

- **Code:** Apache-2.0
- **Weights:** Dual MIT/Apache-2.0 source; the archived review covers Apache-2.0. OCR, inpainting and translation models keep their own terms.
- **Commercial:** The reviewed Apache-2.0 software license permits commercial use subject to its license, notice and source-sharing obligations where applicable. This does not establish permission for every model, input, output or service.
- **Cost:** Local computation and model storage; optional hosted translation is separate.

### Why it merits attention

Proofreading, editable lettering and PSD export provide a practical review loop. [Source 1](https://github.com/koharu-rs/koharu) [Source 2](https://koharu.rs/en/installation) [Source 3](https://koharu.rs/en/hardware)

### Limitations

Automatic cleanup can damage artwork and translation can be wrong. Model residency can exceed device memory. This edition is a documentation review, not an installation or output-quality test. [Source 1](https://github.com/koharu-rs/koharu) [Source 2](https://koharu.rs/en/installation) [Source 3](https://koharu.rs/en/hardware)

### Get the tool

- [Repository](https://github.com/koharu-rs/koharu)
- [License](https://github.com/koharu-rs/koharu/blob/main/LICENSE-APACHE)
- [Documentation](https://koharu.rs/en/installation)

## OpenPencil

Images & design · Vector graphics, illustration & textures · Browser tools & web media · Typography, fonts & layout · Creative publishing & presentation

First detailed guide in this library. This is a documentation baseline, not a claim that the project launched today.

### How it uses AI

A visual design editor uses AI chat to create and modify editable design nodes, with file interchange and programmable export. Creative use: Draft layouts, revise components and export visual assets or code while retaining an editable document. [Source](https://github.com/open-pencil/open-pencil) [Source](https://openpencil.dev) [Source](https://app.openpencil.dev/demo)

### Introduction

A visual design editor uses AI chat to create and modify editable design nodes, with file interchange and programmable export. [Source 1](https://github.com/open-pencil/open-pencil) [Source 2](https://openpencil.dev) [Source 3](https://app.openpencil.dev/demo)

### What it is good for

Draft layouts, revise components and export visual assets or code while retaining an editable document. [Source 1](https://github.com/open-pencil/open-pencil) [Source 2](https://openpencil.dev) [Source 3](https://app.openpencil.dev/demo)

### Demo & examples

The official web demo and README screenshots show the editor; the demo was not operated in this review. [Source 1](https://github.com/open-pencil/open-pencil) [Source 2](https://openpencil.dev) [Source 3](https://app.openpencil.dev/demo)

### Install

Follow the reviewed project route below; these steps are documentation guidance and were not executed. [Source 1](https://github.com/open-pencil/open-pencil) [Source 2](https://openpencil.dev) [Source 3](https://app.openpencil.dev/demo)

1. Use the official browser app or download the matching desktop release.
2. Connect a supported model provider for AI creation; local file editing does not itself imply local AI inference.
3. Optionally install @open-pencil/cli for scripted inspection/export.
### First project

A small first project that exercises the documented creative workflow. [Source 1](https://github.com/open-pencil/open-pencil) [Source 2](https://openpencil.dev) [Source 3](https://app.openpencil.dev/demo)

1. Open a supported .fig/.pen document or start a new design.
2. Ask the integrated assistant to change a specific frame and inspect typography/layout.
3. Save the editable file and export the required image, vector, document or code format.
### Hardware & software

Requirements are source-specific. Unreported capacities and untested platforms are not inferred. [Source 1](https://github.com/open-pencil/open-pencil) [Source 2](https://openpencil.dev) [Source 3](https://app.openpencil.dev/demo)

- **Hardware:** The README states an approximately 15 MB desktop app size, not a total disk requirement. RAM, GPU and VRAM minimums are undocumented.
- **Software:** macOS 13+ with current Safari updates; Windows 10+; Linux WebKitGTK 2.40+. Web app: Chrome/Edge 111+, Firefox 128+ or Safari 16.4+.
- **Platforms:** Desktop macOS/Windows/Linux and web. AI provider support is separate from editor platform support.

### License, model weights & costs

The complete software license was archived and reviewed. Keep software, model weights, dependencies and hosted-service terms separate. [Source 1](https://github.com/open-pencil/open-pencil/blob/master/LICENSE) [Source 2](https://github.com/open-pencil/open-pencil) [Source 3](https://openpencil.dev) [Source 4](https://app.openpencil.dev/demo)

- **Code:** MIT
- **Weights:** MIT editor; external text/image/vectorization providers retain their own terms.
- **Commercial:** The reviewed MIT software license permits commercial use subject to its license, notice and source-sharing obligations where applicable. This does not establish permission for every model, input, output or service.
- **Cost:** No editor source license fee. Optional model APIs such as Recraft/fal.ai vectorization may cost money.

### Why it merits attention

Editable nodes, design-token inspection and export make AI suggestions reviewable and reusable. [Source 1](https://github.com/open-pencil/open-pencil) [Source 2](https://openpencil.dev) [Source 3](https://app.openpencil.dev/demo)

### Limitations

The project describes remaining rough edges. File-format fidelity, font availability and generated code need inspection. This edition is a documentation review, not an installation or output-quality test. [Source 1](https://github.com/open-pencil/open-pencil) [Source 2](https://openpencil.dev) [Source 3](https://app.openpencil.dev/demo)

### Get the tool

- [Repository](https://github.com/open-pencil/open-pencil)
- [License](https://github.com/open-pencil/open-pencil/blob/master/LICENSE)
- [Documentation](https://openpencil.dev)

## HyperFrames

Video, animation & film · AI kinetic typography and animated lettering · Creative publishing & presentation · Data art & scientific visualization · AI agents for code-authored media production

First detailed guide in this library. This is a documentation baseline, not a claim that the project launched today.

### How it uses AI

An AI coding agent authors an editable HTML/CSS video composition, which HyperFrames previews and renders frame by frame into MP4. Creative use: Make short explainers, product demonstrations, animated charts and kinetic captions with reusable layouts. [Source](https://github.com/heygen-com/hyperframes) [Source](https://hyperframes.heygen.com/quickstart) [Source](https://hyperframes.heygen.com/showcase)

### Introduction

An AI coding agent authors an editable HTML/CSS video composition, which HyperFrames previews and renders frame by frame into MP4. [Source 1](https://github.com/heygen-com/hyperframes) [Source 2](https://hyperframes.heygen.com/quickstart) [Source 3](https://hyperframes.heygen.com/showcase)

### What it is good for

Make short explainers, product demonstrations, animated charts and kinetic captions with reusable layouts. [Source 1](https://github.com/heygen-com/hyperframes) [Source 2](https://hyperframes.heygen.com/quickstart) [Source 3](https://hyperframes.heygen.com/showcase)

### Demo & examples

The official showcase provides finished videos; the quickstart describes a ten-second product intro. [Source 1](https://github.com/heygen-com/hyperframes) [Source 2](https://hyperframes.heygen.com/quickstart) [Source 3](https://hyperframes.heygen.com/showcase)

### Install

Follow the reviewed project route below; these steps are documentation guidance and were not executed. [Source 1](https://github.com/heygen-com/hyperframes) [Source 2](https://hyperframes.heygen.com/quickstart) [Source 3](https://hyperframes.heygen.com/showcase)

1. Install Node.js 22+ and FFmpeg.
2. Create a project with npx hyperframes init my-video.
3. For AI authoring, install the documented agent plugin or core skills in your own production environment; the renderer also works directly from the CLI.

```sh
npx hyperframes init my-video
```


```sh
npx hyperframes preview
```


```sh
npx hyperframes render
```

### First project

A small first project that exercises the documented creative workflow. [Source 1](https://github.com/heygen-com/hyperframes) [Source 2](https://hyperframes.heygen.com/quickstart) [Source 3](https://hyperframes.heygen.com/showcase)

1. Describe the desired sequence or edit its HTML composition.
2. Preview locally and inspect timing, text, narration and generated assets.
3. Render an MP4 after review, retaining the source composition for revisions.
### Hardware & software

Requirements are source-specific. Unreported capacities and untested platforms are not inferred. [Source 1](https://github.com/heygen-com/hyperframes) [Source 2](https://hyperframes.heygen.com/quickstart) [Source 3](https://hyperframes.heygen.com/showcase)

- **Hardware:** Headless Chrome and FFmpeg perform rendering. Numeric CPU/RAM/VRAM and disk minimums are not specified.
- **Software:** Node.js 22+, FFmpeg and the supplied browser/rendering dependencies; a compatible coding agent for AI authoring.
- **Platforms:** Documentation includes macOS, Windows and Linux development setup. Browser preview and local rendering are distinct from optional hosted production.

### License, model weights & costs

The complete software license was archived and reviewed. Keep software, model weights, dependencies and hosted-service terms separate. [Source 1](https://github.com/heygen-com/hyperframes/blob/main/LICENSE) [Source 2](https://github.com/heygen-com/hyperframes) [Source 3](https://hyperframes.heygen.com/quickstart) [Source 4](https://hyperframes.heygen.com/showcase)

- **Code:** Apache-2.0
- **Weights:** No required bundled model weights; the coding agent and optional media/voice/avatar services have independent terms.
- **Commercial:** The reviewed Apache-2.0 software license permits commercial use subject to its license, notice and source-sharing obligations where applicable. This does not establish permission for every model, input, output or service.
- **Cost:** Apache-2.0 renderer with no per-render license fee; agent access, hosted services and compute remain separate.

### Why it merits attention

Source compositions and deterministic frame seeking make revisions easier to inspect than a flattened generated clip. [Source 1](https://github.com/heygen-com/hyperframes) [Source 2](https://hyperframes.heygen.com/quickstart) [Source 3](https://hyperframes.heygen.com/showcase)

### Limitations

AI-written layouts still need editorial review. Animation libraries, fonts and imported/generated media have separate rights. This edition is a documentation review, not an installation or output-quality test. [Source 1](https://github.com/heygen-com/hyperframes) [Source 2](https://hyperframes.heygen.com/quickstart) [Source 3](https://hyperframes.heygen.com/showcase)

### Get the tool

- [Repository](https://github.com/heygen-com/hyperframes)
- [License](https://github.com/heygen-com/hyperframes/blob/main/LICENSE)
- [Documentation](https://hyperframes.heygen.com/quickstart)

## Ghost Arcade

Performance, projection & stage media · Physical, robotic & kinetic installations · Interactive, immersive & live media · Computational art & creative coding

First detailed guide in this library. This is a documentation baseline, not a claim that the project launched today.

### How it uses AI

A VJ/projection-mapping application includes prompt-assisted shader creation, audio-reactive mixing and stage-output controls. Creative use: Create and perform generative shaders on mapped surfaces, then capture a live-visual sequence. [Source](https://github.com/riskcapital/ghost-arcade) [Source](https://ghostarcade.live/) [Source](https://ghostarcade.live/download)

### Introduction

A VJ/projection-mapping application includes prompt-assisted shader creation, audio-reactive mixing and stage-output controls. [Source 1](https://github.com/riskcapital/ghost-arcade) [Source 2](https://ghostarcade.live/) [Source 3](https://ghostarcade.live/download)

### What it is good for

Create and perform generative shaders on mapped surfaces, then capture a live-visual sequence. [Source 1](https://github.com/riskcapital/ghost-arcade) [Source 2](https://ghostarcade.live/) [Source 3](https://ghostarcade.live/download)

### Demo & examples

The official site publishes interface and performance examples; no projector, NDI, Syphon or Spout testing was performed. [Source 1](https://github.com/riskcapital/ghost-arcade) [Source 2](https://ghostarcade.live/) [Source 3](https://ghostarcade.live/download)

### Install

Follow the reviewed project route below; these steps are documentation guidance and were not executed. [Source 1](https://github.com/riskcapital/ghost-arcade) [Source 2](https://ghostarcade.live/) [Source 3](https://ghostarcade.live/download)

1. Use the official download page for the current packaged release. The 2.x download form requires email consent; legacy 1.9.995 downloads do not.
2. For the default-branch legacy source, install Node.js 20+ and npm 10+, clone and run npm install.
3. Start legacy desktop with npm run desktop or browser mode with npm start. The 2.x source is on the branch explicitly linked in the README.
### First project

A small first project that exercises the documented creative workflow. [Source 1](https://github.com/riskcapital/ghost-arcade) [Source 2](https://ghostarcade.live/) [Source 3](https://ghostarcade.live/download)

1. Create a surface/scene and add a shader or video layer.
2. Use the documented AI provider connection for shader generation, then inspect its output.
3. Map to the target display, test audio/control routing and record a short rehearsal.
### Hardware & software

Requirements are source-specific. Unreported capacities and untested platforms are not inferred. [Source 1](https://github.com/riskcapital/ghost-arcade) [Source 2](https://ghostarcade.live/) [Source 3](https://ghostarcade.live/download)

- **Hardware:** Native 2.0.16: Direct3D 12 (Windows) or Metal (Mac), 8 GB RAM (16 GB for multi-output/long shows), 1080p display and 1 GB disk. Legacy 1.9.995: WebGL 2, 4 GB RAM, 720p display and 500 MB disk. No numeric VRAM minimum is stated.
- **Software:** Legacy source: Node.js 20+, npm 10+, Electron/browser dependencies. The 2.x native renderer uses Rust/wgpu; do not apply legacy build instructions to it.
- **Platforms:** Native packages: Windows 10+ 64-bit or macOS 12+. Linux uses the legacy browser-renderer build; native Linux output is unsupported. Output integrations vary by platform.

### License, model weights & costs

The complete software license was archived and reviewed. Keep software, model weights, dependencies and hosted-service terms separate. [Source 1](https://github.com/riskcapital/ghost-arcade/blob/main/LICENSE) [Source 2](https://github.com/riskcapital/ghost-arcade) [Source 3](https://ghostarcade.live/) [Source 4](https://ghostarcade.live/download)

- **Code:** AGPL-3.0
- **Weights:** AGPL-3.0-only application; AI shader/media providers and imported assets keep independent terms.
- **Commercial:** The reviewed AGPL-3.0 software license permits commercial use subject to its license, notice and source-sharing obligations where applicable. This does not establish permission for every model, input, output or service.
- **Cost:** The desktop app is described as free/open-source; connected AI services and show hardware can cost money.

### Why it merits attention

AI-generated code feeds directly into mapping, modulation and capture workflows. [Source 1](https://github.com/riskcapital/ghost-arcade) [Source 2](https://ghostarcade.live/) [Source 3](https://ghostarcade.live/download)

### Limitations

Version drift is visible: website 2.0.16, README highlights 2.0.13, and default source remains legacy 1.9. Verify the exact source/release pair before deployment. This edition is a documentation review, not an installation or output-quality test. [Source 1](https://github.com/riskcapital/ghost-arcade) [Source 2](https://ghostarcade.live/) [Source 3](https://ghostarcade.live/download)

### Get the tool

- [Repository](https://github.com/riskcapital/ghost-arcade)
- [License](https://github.com/riskcapital/ghost-arcade/blob/main/LICENSE)
- [Documentation](https://ghostarcade.live/)

## FRIDA / CoFRIDA

Physical, robotic & kinetic installations · Computational art & creative coding · Images & design · Interactive, immersive & live media

First detailed guide in this library. This is a documentation baseline, not a claim that the project launched today.

### How it uses AI

A learned, differentiable painting model plans brush strokes from images/text; CoFRIDA extends it to respond to a human's partially painted canvas. Creative use: Explore human–robot co-painting and physical brush-based installations, beginning in simulation. [Source](https://github.com/cmubig/Frida) [Source](https://arxiv.org/abs/2402.13442) [Source](https://arxiv.org/abs/2210.00664) [Source](https://pschaldenbrand.github.io/cofrida/)

### Introduction

A learned, differentiable painting model plans brush strokes from images/text; CoFRIDA extends it to respond to a human's partially painted canvas. [Source 1](https://github.com/cmubig/Frida) [Source 2](https://arxiv.org/abs/2402.13442) [Source 3](https://arxiv.org/abs/2210.00664) [Source 4](https://pschaldenbrand.github.io/cofrida/)

### What it is good for

Explore human–robot co-painting and physical brush-based installations, beginning in simulation. [Source 1](https://github.com/cmubig/Frida) [Source 2](https://arxiv.org/abs/2402.13442) [Source 3](https://arxiv.org/abs/2210.00664) [Source 4](https://pschaldenbrand.github.io/cofrida/)

### Demo & examples

The authors publish painting videos, a Colab notebook and research project pages. [Source 1](https://github.com/cmubig/Frida) [Source 2](https://arxiv.org/abs/2402.13442) [Source 3](https://arxiv.org/abs/2210.00664) [Source 4](https://pschaldenbrand.github.io/cofrida/)

### Install

Follow the reviewed project route below; these steps are documentation guidance and were not executed. [Source 1](https://github.com/cmubig/Frida) [Source 2](https://arxiv.org/abs/2402.13442) [Source 3](https://arxiv.org/abs/2210.00664) [Source 4](https://pschaldenbrand.github.io/cofrida/)

1. Clone the canonical repository and prepare its Python 3.8/Ubuntu environment.
2. Use the provided Conda environment or requirements file and a compatible CUDA/PyTorch stack.
3. Start with simulation and supplied calibration data. Physical operation additionally requires robot, camera, materials layout and calibration setup.
### First project

A small first project that exercises the documented creative workflow. [Source 1](https://github.com/cmubig/Frida) [Source 2](https://arxiv.org/abs/2402.13442) [Source 3](https://arxiv.org/abs/2210.00664) [Source 4](https://pschaldenbrand.github.io/cofrida/)

1. Choose a text/image/style objective and inspect a simulated painting plan.
2. Review the planned strokes and intermediate canvas before changing parameters.
3. For a physical setup, follow the robot-specific calibration and material-position documentation; the research code is not an unattended appliance.
### Hardware & software

Requirements are source-specific. Unreported capacities and untested platforms are not inferred. [Source 1](https://github.com/cmubig/Frida) [Source 2](https://arxiv.org/abs/2402.13442) [Source 3](https://arxiv.org/abs/2210.00664) [Source 4](https://pschaldenbrand.github.io/cofrida/)

- **Hardware:** Recommended NVIDIA VRAM: 8+ GB for core FRIDA, 12+ GB for CoFRIDA inference, 16+ GB for training. RAM and storage minimums are unspecified. Physical setup uses a supported robot, camera and painting materials.
- **Software:** Python 3.8, CUDA/PyTorch, supplied dependencies; gphoto2 for the documented camera workflow.
- **Platforms:** Ubuntu 20.04 is the authors' environment. UFactory XArm/Franka are currently supported; Sawyer requires the older ICRA 2023 tag. No Mac/Windows host validation is documented.

### License, model weights & costs

The complete software license was archived and reviewed. Keep software, model weights, dependencies and hosted-service terms separate. [Source 1](https://github.com/cmubig/Frida/blob/master/LICENSE) [Source 2](https://github.com/cmubig/Frida) [Source 3](https://arxiv.org/abs/2402.13442) [Source 4](https://arxiv.org/abs/2210.00664) [Source 5](https://pschaldenbrand.github.io/cofrida/)

- **Code:** GPL-3.0
- **Weights:** GPL-3.0 code; Stable Diffusion, CLIP and other model/data assets retain independent terms.
- **Commercial:** The reviewed GPL-3.0 software license permits commercial use subject to its license, notice and source-sharing obligations where applicable. This does not establish permission for every model, input, output or service.
- **Cost:** Local GPU computation; robot/camera/material costs are separate and not estimated here.

### Why it merits attention

Released simulation, physical setup documentation and human co-painting examples support a concrete creative research workflow. [Source 1](https://github.com/cmubig/Frida) [Source 2](https://arxiv.org/abs/2402.13442) [Source 3](https://arxiv.org/abs/2210.00664) [Source 4](https://pschaldenbrand.github.io/cofrida/)

### Limitations

Physical calibration and robot integration are substantial. A simulated plan does not establish a safe or accurate physical execution. This edition is a documentation review, not an installation or output-quality test. [Source 1](https://github.com/cmubig/Frida) [Source 2](https://arxiv.org/abs/2402.13442) [Source 3](https://arxiv.org/abs/2210.00664) [Source 4](https://pschaldenbrand.github.io/cofrida/)

### Get the tool

- [Repository](https://github.com/cmubig/Frida)
- [License](https://github.com/cmubig/Frida/blob/master/LICENSE)
- [Documentation](https://arxiv.org/abs/2402.13442)

## Additional open-source AI discoveries

Creative AI relevance and software license screened. Full installation, requirements and quality profiles are pending.

### Stable Diffusion WebUI · AGPL-3.0

Local diffusion image generation, inpainting/outpainting and controlled texture experiments.
The application runs diffusion models with image-to-image, masks, LoRA and tiled generation controls.
Model/extension terms and current platform setup need a detailed follow-up; reported low-VRAM support is model-specific. Software license reviewed; full profile and hands-on output testing remain pending.

- [Official project documentation](https://github.com/AUTOMATIC1111/stable-diffusion-webui)
- [Complete reviewed software license](https://github.com/AUTOMATIC1111/stable-diffusion-webui/blob/master/LICENSE.txt)
### MoneyPrinterTurbo · MIT

Assemble scripted short videos with narration, captions and chosen media.
LLMs generate/rewrite scripts and choose media keywords; configurable TTS and image/video providers feed a compositing pipeline.
Provider costs, stock-media rights and posting integrations require review; no automated posting was used. Software license reviewed; full profile and hands-on output testing remain pending.

- [Official project documentation](https://github.com/harry0703/MoneyPrinterTurbo)
- [Complete reviewed software license](https://github.com/harry0703/MoneyPrinterTurbo/blob/main/LICENSE)
### Next AI Draw.io · Apache-2.0

Create editable explanatory diagrams from text, documents or reference images.
An LLM generates and revises draw.io XML while the editor retains diagram history.
Model formatting reliability, local/hosted provider setup and exact hardware requirements remain pending. Software license reviewed; full profile and hands-on output testing remain pending.

- [Official project documentation](https://github.com/DayuanJiang/next-ai-draw-io)
- [Complete reviewed software license](https://github.com/DayuanJiang/next-ai-draw-io/blob/main/LICENSE)
### VideoLingo · Apache-2.0

Translate, retime and dub video with editable subtitles.
Speech recognition/alignment and LLM-assisted segmentation/translation feed configurable voice-synthesis backends.
Detailed platform/model requirements and voice quality review pending; timing and speaker separation are not guaranteed. Software license reviewed; full profile and hands-on output testing remain pending.

- [Official project documentation](https://github.com/Huanshere/VideoLingo)
- [Complete reviewed software license](https://github.com/Huanshere/VideoLingo/blob/main/LICENSE)
### Data Formulator · MIT

Explore data through editable visualizations and branching analysis paths.
AI agents transform connected data and generate chart specifications for visual exploration.
Chart/data accuracy and stable-versus-beta installation need detailed follow-up; hosted model costs are separate. Software license reviewed; full profile and hands-on output testing remain pending.

- [Official project documentation](https://github.com/microsoft/data-formulator)
- [Complete reviewed software license](https://github.com/microsoft/data-formulator/blob/main/LICENSE)
### Toonflow · MIT

Organize short-drama scripts, characters and generated shots on a visual production canvas.
AI script, image and video services are integrated with asset management and shot production.
Installation, provider licensing and quality review pending. Current README explicitly removes former commercial addenda; archived code license is MIT. Software license reviewed; full profile and hands-on output testing remain pending.

- [Official project documentation](https://github.com/HBAI-Ltd/Toonflow-app)
- [Complete reviewed software license](https://github.com/HBAI-Ltd/Toonflow-app/blob/master/LICENSE)
### Robust Video Matting · GPL-3.0

Extract human foreground mattes for compositing and virtual backgrounds.
A recurrent neural network uses temporal memory to estimate video alpha mattes.
Detailed inference/framework and checkpoint terms review pending; developer FPS figures are not verified here. Software license reviewed; full profile and hands-on output testing remain pending.

- [Official project documentation](https://github.com/PeterL1n/RobustVideoMatting)
- [Complete reviewed software license](https://github.com/PeterL1n/RobustVideoMatting/blob/master/LICENSE)
### Dream Textures · GPL-3.0

Generate textures and restyle Blender scenes with diffusion.
The Blender add-on uses diffusion for text-to-texture, depth-conditioned projection, inpainting and render-pass stylization.
Current Blender/platform compatibility and model license review pending; proprietary host assumptions do not apply because Blender is separate open software. Software license reviewed; full profile and hands-on output testing remain pending.

- [Official project documentation](https://github.com/carson-katri/dream-textures)
- [Complete reviewed software license](https://github.com/carson-katri/dream-textures/blob/main/LICENSE)
### Inpaint-web · GPL-3.0

Remove unwanted image regions and upscale images in a browser.
MI-GAN inference and neural upscaling run through browser WebGPU/WASM paths.
Browser/GPU support and weight terms need detailed review; SAM and Stable Diffusion items shown in the roadmap are not treated as implemented. Software license reviewed; full profile and hands-on output testing remain pending.

- [Official project documentation](https://github.com/lxfater/inpaint-web)
- [Complete reviewed software license](https://github.com/lxfater/inpaint-web/blob/main/LICENSE)
### SmartSub · MIT

Transcribe, translate, proofread, voice and burn captions from a desktop workspace.
Local whisper.cpp/sherpa-onnx recognition, configurable TTS and an AI assistant support an end-to-end subtitle workflow.
Detailed backend requirements and checkpoint/service terms pending; free hosted translation is distinct from offline processing. Software license reviewed; full profile and hands-on output testing remain pending.

- [Official project documentation](https://github.com/buxuku/SmartSub)
- [Complete reviewed software license](https://github.com/buxuku/SmartSub/blob/main/LICENSE)
### LatentSync · Apache-2.0

Adapt lip motion in a video to supplied speech for reviewed dubbing experiments.
Audio-conditioned latent diffusion and Whisper embeddings model the relationship between speech and mouth motion.
Hardware/version/model rights and artifact review pending. The documented 1.6 release is an older baseline, not today's launch. The official LatentSync 1.6 model card labels weights OpenRAIL++, separate from Apache-2.0 code. Software license reviewed; full profile and hands-on output testing remain pending.

- [Official project documentation](https://github.com/bytedance/LatentSync)
- [Complete reviewed software license](https://github.com/bytedance/LatentSync/blob/main/LICENSE)
- [Official project documentation](https://huggingface.co/ByteDance/LatentSync-1.6)
### Amphion · MIT

Research speech generation, voice conversion and singing-voice pipelines.
The toolkit implements neural TTS, singing synthesis, conversion and vocoder workflows.
Individual models have different requirements/terms; Emilia data includes non-commercial material. Do not treat the entire dataset/model ecosystem as MIT. Software license reviewed; full profile and hands-on output testing remain pending.

- [Official project documentation](https://github.com/open-mmlab/Amphion)
- [Complete reviewed software license](https://github.com/open-mmlab/Amphion/blob/main/LICENSE)
### StreamDiffusion · Apache-2.0

Build interactive image transformation or real-time visual experiments.
A diffusion inference pipeline batches denoising and filters similar inputs to reduce interactive processing overhead.
Exact GPU/model setup and latency review pending; published RTX 4090 measurements are not universal minimums or guarantees. Software license reviewed; full profile and hands-on output testing remain pending.

- [Official project documentation](https://github.com/cumulo-autumn/StreamDiffusion)
- [Complete reviewed software license](https://github.com/cumulo-autumn/StreamDiffusion/blob/main/LICENSE)
### BackgroundRemover · MIT

Batch-remove backgrounds from images and clips through a CLI.
U2Net-based segmentation produces foreground masks and alpha video outputs.
Install/platform and edge-quality review pending. README identifies separate Apache-2.0 model terms, which need checkpoint-specific confirmation. Software license reviewed; full profile and hands-on output testing remain pending.

- [Official project documentation](https://github.com/nadermx/backgroundremover)
- [Complete reviewed software license](https://github.com/nadermx/backgroundremover/blob/main/LICENSE.txt)
### InkOS · AGPL-3.0

Draft and revise long fiction, screenplays and branching narrative projects.
LLM agents use structured story memory, retrieval and review actions to generate and revise narrative artifacts.
Detailed setup, model costs and writing-quality review pending; AGPL terms cover software, not model-provider terms. Software license reviewed; full profile and hands-on output testing remain pending.

- [Official project documentation](https://github.com/Narcooo/inkos)
- [Complete reviewed software license](https://github.com/Narcooo/inkos/blob/master/LICENSE)
### threestudio · Apache-2.0

Experiment with text/image-conditioned 3D asset generation.
The framework lifts 2D generative-model guidance into optimized 3D representations across multiple research methods.
Method-specific GPU requirements and model licenses pending; generated geometry is not automatically game-optimized or printable. Software license reviewed; full profile and hands-on output testing remain pending.

- [Official project documentation](https://github.com/threestudio-project/threestudio)
- [Complete reviewed software license](https://github.com/threestudio-project/threestudio/blob/main/LICENSE)
### Game Asset MCP · MIT

Route AI-assisted 2D/3D asset prototypes into local project files.
An MCP workflow combines a Flux game-asset image model with InstantMesh or Hunyuan3D image-to-mesh Spaces.
Service availability, duplicated Space setup and all weight terms pending; README installation contains a placeholder repository URL. Software license reviewed; full profile and hands-on output testing remain pending.

- [Official project documentation](https://github.com/sato942/game-asset-mcp)
- [Complete reviewed software license](https://github.com/sato942/game-asset-mcp/blob/main/LICENSE)
### theDAW · MIT

Generate music, edit/mix it and explore linked performance/visual workflows.
Documented Stable Audio and Magenta generation paths connect to arrangement, stem processing and audio-to-score tools.
Large feature surface needs validation. Software MIT does not cover Stable Audio, other weights, plugins or optional cloud services. Software license reviewed; full profile and hands-on output testing remain pending.

- [Official project documentation](https://github.com/gantasmo/theDAW)
- [Complete reviewed software license](https://github.com/gantasmo/theDAW/blob/main/LICENSE)
### KimCad · Apache-2.0

Turn a described/sketched functional part into editable parametric CAD and a reviewed slicing workflow.
Local Ollama language/vision models translate a brief into a design plan; deterministic templates construct geometry.
Beta hardware/printing validation pending; the author distinguishes mock-protocol tests from physical printer tests. No print-readiness guarantee is made here. Software license reviewed; full profile and hands-on output testing remain pending.

- [Official project documentation](https://github.com/scottconverse/KimCadClaude)
- [Complete reviewed software license](https://github.com/scottconverse/KimCadClaude/blob/main/LICENSE)
### Inkstone · MIT

Turn a novel into lettered comic pages, PDF or webtoon strips.
A multimodal API extracts story/character information and generates reference-conditioned page art; local typography overlays readable lettering.
Cloud-only default inference; advertised free service availability and output rights require separate review. Consistency is explicitly limited. Software license reviewed; full profile and hands-on output testing remain pending.

- [Official project documentation](https://github.com/phaethix/inkstone)
- [Complete reviewed software license](https://github.com/phaethix/inkstone/blob/main/LICENSE)
### OnDevice LLM · MIT

Explore on-device speech, vision and image-generation workflows on iPhone or Apple Silicon.
The workbench combines MLX, llama.cpp, whisper.cpp and Core ML for local multimodal generation and recognition.
Model/device memory, iOS/macCatalyst setup and individual weights still need detailed review; generic chat alone is not the creative basis for inclusion. The current project site says public sideload downloads have retired and the App Store release is coming soon; source and previews remain available. Software license reviewed; full profile and hands-on output testing remain pending.

- [Official project documentation](https://github.com/Mesutcydev/ios-local-llm)
- [Complete reviewed software license](https://github.com/Mesutcydev/ios-local-llm/blob/main/LICENSE)
- [Official project documentation](https://mesutcydev.github.io/ios-local-llm/)
### Comic Drama Workflow · MIT

Organize a script into characters, storyboard media, dialogue audio and an editable production timeline.
AI scene extraction and pluggable ComfyUI/TTS/video providers feed a dynamic-comic rendering workflow.
Explicit early prototype. Provider integration maturity, installation and hardware review pending; deterministic fallback frames are not AI generation. Software license reviewed; full profile and hands-on output testing remain pending.

- [Official project documentation](https://github.com/tccnnd/Comic-drama)
- [Complete reviewed software license](https://github.com/tccnnd/Comic-drama/blob/main/LICENSE)
### Wind Comic · MIT

Coordinate reusable characters, storyboards, voices and a short-drama timeline.
A multi-agent workflow connects configurable LLM and media-generation providers to editable production stages.
Large claims and test-count badges were not independently verified. Provider costs, hardware and deployment details need follow-up. Software license reviewed; full profile and hands-on output testing remain pending.

- [Official project documentation](https://github.com/ChrisChen667788/wind-comic)
- [Complete reviewed software license](https://github.com/ChrisChen667788/wind-comic/blob/main/LICENSE)
### RestoraX · MIT

Explore a configurable restoration pipeline for old photographs and video.
The project documents neural restoration adapters including a Real-ESRGAN example and a graph-based processing interface.
Prototype/stub-first: many advertised adapters are stubs and some benchmark figures are extrapolations. Real implementation, weight licenses and output quality require verification before use. Software license reviewed; full profile and hands-on output testing remain pending.

- [Official project documentation](https://github.com/karailker/restorax)
- [Complete reviewed software license](https://github.com/karailker/restorax/blob/main/LICENSE)
### anidoodle · Apache-2.0

Author code-drawn illustrations, scored films and interactive artwork.
Its reusable agent skills direct a coding model to construct artwork and music through a deterministic rendering toolkit.
Detailed installation and output review pending; the rendering engine itself is procedural, while AI is the authoring agent. Software license reviewed; full profile and hands-on output testing remain pending.

- [Official project documentation](https://github.com/alexgreensh/anidoodle)
- [Complete reviewed software license](https://github.com/alexgreensh/anidoodle/blob/main/LICENSE)
### Riso Windowseat toolkit · MIT

Create risograph-style HTML films and print series.
Reusable Claude Code skills and a render harness support AI-assisted composition of Canvas/Web Audio films.
Agent setup, rendering requirements and embedded piano-recording terms need further review; existing films are examples, not a model. Software license reviewed; full profile and hands-on output testing remain pending.

- [Official project documentation](https://github.com/sevenevesai/riso-windowseat)
- [Complete reviewed software license](https://github.com/sevenevesai/riso-windowseat/blob/main/LICENSE)
### BrewReel · Apache-2.0

Turn a product brief into a structured vertical promotional video.
An LLM selects shots and writes copy for constrained video templates before local rendering.
Apache-2.0 code; required Remotion has separate source-available/commercial terms. Dependency, cost and hardware review pending. Software license reviewed; full profile and hands-on output testing remain pending.

- [Official project documentation](https://github.com/Finderchangchang/brewreel)
- [Complete reviewed software license](https://github.com/Finderchangchang/brewreel/blob/main/LICENSE)
- [Official project documentation](https://github.com/Finderchangchang/brewreel/blob/main/NOTICE)
### OpenHouse 3D · MIT

Prototype a modeled property walkthrough from listing photos and measured dimensions.
A coding agent interprets reference images and builds procedural Blender scenes using the toolkit's camera-solving and comparison utilities.
This is agent-assisted reconstruction, not guaranteed photogrammetric truth. Installation and reference-image rights review pending. Software license reviewed; full profile and hands-on output testing remain pending.

- [Official project documentation](https://github.com/yunfanye/openhouse-3d)
- [Complete reviewed software license](https://github.com/yunfanye/openhouse-3d/blob/main/LICENSE)
### OpenRive · MIT

Let an AI assistant edit vector animations and state-machine projects.
An MCP interface exposes animation/project operations to an external AI agent while the editor handles .riv files.
Runtime/file compatibility, agent setup and dependency terms need detailed review; the editor contains no bundled generative model. Software license reviewed; full profile and hands-on output testing remain pending.

- [Official project documentation](https://github.com/UpstandPlatform/OpenRive)
- [Complete reviewed software license](https://github.com/UpstandPlatform/OpenRive/blob/main/LICENSE)
### Yengi · AGPL-3.0

Develop Blender scenes or Unity content with a Windows AI copilot.
Local/cloud LLMs propose scene blueprints and generate Blender Python or Unity code, with viewport-image feedback.
Claims of bug-free code are not accepted as evidence. Installation, model requirements and proprietary Unity terms need separate review. Software license reviewed; full profile and hands-on output testing remain pending.

- [Official project documentation](https://github.com/mdaiWorks/yengi)
- [Complete reviewed software license](https://github.com/mdaiWorks/yengi/blob/main/LICENSE)
### 3D New Era AI · Apache-2.0

Co-design floor plans, furnishings and rendered interiors.
An MCP-connected AI agent manipulates live scene geometry and design properties in the Rust editor.
Dual MIT/Apache-2.0; this review archives Apache. Building-standard/ergonomic claims, platform setup and hosted-connector limits remain unverified. Software license reviewed; full profile and hands-on output testing remain pending.

- [Official project documentation](https://github.com/leandrodaf/3d-new-era-ai)
- [Complete reviewed software license](https://github.com/leandrodaf/3d-new-era-ai/blob/main/LICENSE-APACHE)
### CapShorts · MIT

Prepare captioned short clips and remove pauses from longer recordings.
Whisper/Faster-Whisper transcription drives word-timed subtitles; the stack also supports a hosted Groq path.
MIT app; verify bundled dependencies, local fallback behavior and export quality. Claimed three-second transcription is not a measured result here. Software license reviewed; full profile and hands-on output testing remain pending.

- [Official project documentation](https://github.com/thealiraza2/CapShorts)
- [Complete reviewed software license](https://github.com/thealiraza2/CapShorts/blob/main/LICENSE)
### Beyondwords · MIT

Organize manuscript research, editing, book production and publishing preparation.
An AI assistant uses reusable authoring skills and local evidence/manuscript tools to produce reviewed book artifacts.
Assistant/service dependencies and output-format checks pending. No account access or publication action was performed. Software license reviewed; full profile and hands-on output testing remain pending.

- [Official project documentation](https://github.com/beyondtahir/beyondwords)
- [Complete reviewed software license](https://github.com/beyondtahir/beyondwords/blob/main/LICENSE)
### OpenSpatial · GPL-3.0

Experiment with headphone spatial playback and AI-assisted stereo upmix on Mac.
A Core ML voice-separation path places dialogue in the center of a spatial sound field, alongside head tracking.
Detailed runtime/device review pending; GPL code, model assets and CC-BY-SA room responses have distinct terms. Not a universal spatial-mastering guarantee. Software license reviewed; full profile and hands-on output testing remain pending.

- [Official project documentation](https://github.com/dortanes/openspatial)
- [Complete reviewed software license](https://github.com/dortanes/openspatial/blob/main/LICENSE)
### vistep scene-authoring toolkit · MIT

Produce bilingual interactive explainers with narration and inspectable calculations.
The repository provides a vistep-scene authoring skill for an AI coding assistant to create new educational scenes.
Published scenes run without live AI. Inclusion concerns the reusable AI authoring workflow; dependencies, instructional accuracy and setup remain pending. Software license reviewed; full profile and hands-on output testing remain pending.

- [Official project documentation](https://github.com/int64ago/vistep)
- [Complete reviewed software license](https://github.com/int64ago/vistep/blob/main/LICENSE)
### Qwen Image Studio · MIT

Run text-to-image and multi-image editing on Apple Silicon.
A local Diffusers Qwen-Image-2.1 pipeline optionally uses a separate 9B prompt enhancer, unloading it before generation.
Detailed memory/model terms review pending. CLI is standalone, but the web studio requires helmstudio; browser access is not generic platform support. Software license reviewed; full profile and hands-on output testing remain pending.

- [Official project documentation](https://github.com/janishar/qwen-image-2.1-studio)
- [Complete reviewed software license](https://github.com/janishar/qwen-image-2.1-studio/blob/main/LICENSE)
### FloodDiffusion 2 · MIT

Generate continuous body motion with changing text and controlled paths.
A streaming diffusion model uses cached attention and root-path conditioning to synthesize motion.
Python/model/hardware and third-party body-model terms need detailed review; MIT code does not cover every dataset or weight. Software license reviewed; full profile and hands-on output testing remain pending.

- [Official project documentation](https://github.com/AlayaLab/FloodDiffusion2)
- [Complete reviewed software license](https://github.com/AlayaLab/FloodDiffusion2/blob/main/LICENSE)
### OmaStudio · MIT

Explore RAW photo editing with AI-assisted scene/preset decisions on Linux.
The Rust Jev client sends photographic metrics and EXIF state to a configured AI decision service and applies returned preset/tone recommendations to a RAW editing recipe.
The README advertises offline AI, but the reviewed implementation separates a keyed remote model client from a deterministic offline expert fallback. Availability/accuracy of the remote endpoint, setup and hardware need verification; do not assume on-device neural inference. Software license reviewed; full profile and hands-on output testing remain pending.

- [Official project documentation](https://github.com/ozdil/omarchy-omastudio)
- [Complete reviewed software license](https://github.com/ozdil/omarchy-omastudio/blob/master/LICENSE)
- [Official project documentation](https://github.com/ozdil/omarchy-omastudio/blob/master/src/ai/jev.rs)
### SandKit · MIT

Turn reference art into interactive sand-particle experiences.
An agent workflow creates line art and estimated depth maps, then integrates them with a WebGL2 particle renderer.
AI is in authoring/assets, not the particle simulation. Detailed setup and generated-asset/trademark rights review pending. Software license reviewed; full profile and hands-on output testing remain pending.

- [Official project documentation](https://github.com/LinklyAI/SandKit)
- [Complete reviewed software license](https://github.com/LinklyAI/SandKit/blob/main/LICENSE)
### Remiqora · MIT

Generate songs and arrange them in a local multitrack music workspace.
ACE-Step and YuE2 generation combine with stem separation, transcription and optional LoRA training.
Actively developing software. YuE2-3B weights remain CC-BY-NC-4.0; platform/model memory and other component terms need review. Software license reviewed; full profile and hands-on output testing remain pending.

- [Official project documentation](https://github.com/inikolax/remiqora)
- [Complete reviewed software license](https://github.com/inikolax/remiqora/blob/master/LICENSE)
### EmDash AI Alt Text · MIT

Draft and translate image descriptions while preserving human-written alt text.
Claude vision/text generation describes public images in each page's language within the CMS workflow.
Requires EmDash sandbox support and Anthropic API access; Cloudflare's runner path needs a paid plan. Accuracy and accessibility conformance require human review. Software license reviewed; full profile and hands-on output testing remain pending.

- [Official project documentation](https://github.com/DavidPivert/emdash-plugin-ai-alt-text)
- [Complete reviewed software license](https://github.com/DavidPivert/emdash-plugin-ai-alt-text/blob/main/LICENSE)
### YuE2-Turbo · Apache-2.0

Serve concurrent YuE2 song-generation jobs through a browser studio/API.
The inference layer uses vLLM, resident weights and batched synthesis to execute YuE2 music generation.
Apache-2.0 software but CC-BY-NC-4.0 model weights. Claimed speedups are limited to the author's benchmark setup; detailed deployment review pending. Software license reviewed; full profile and hands-on output testing remain pending.

- [Official project documentation](https://github.com/NoizAI/YuE2-Turbo)
- [Complete reviewed software license](https://github.com/NoizAI/YuE2-Turbo/blob/main/LICENSE)
### OpenSubs · AGPL-3.0

Transcribe, translate, style and burn captions through browser, desktop or CLI workflows.
Local speech recognition and translation models feed a shared Rust/WASM subtitle engine.
AGPL software; verify each runtime's models, browser memory and optional network paths. 'Local' claims have not been traffic-tested here. Software license reviewed; full profile and hands-on output testing remain pending.

- [Official project documentation](https://github.com/open-subs/opensubs)
- [Complete reviewed software license](https://github.com/open-subs/opensubs/blob/main/LICENSE)
### ALIGN · MIT

Create editable code-based illustrations and films through iterative visual review.
An AI coding agent writes drawing/rendering programs and revises them against reference images and independent visual feedback.
Model/agent and rendering setup review pending; no diffusion model is required by this authoring approach. Software license reviewed; full profile and hands-on output testing remain pending.

- [Official project documentation](https://github.com/wanshuiyin/ALIGN-Agentic-Loop-Image-GeneratioN)
- [Complete reviewed software license](https://github.com/wanshuiyin/ALIGN-Agentic-Loop-Image-GeneratioN/blob/main/LICENSE)
### SVG AITuber Chat · MIT

Prototype a speaking animated SVG host for a livestream.
An LLM generates replies and TTS audio drives lip motion, expressions and reactions.
MIT source excludes the Miko character assets, which have separate redistribution limits. Provider costs, streaming setup and output review pending. Software license reviewed; full profile and hands-on output testing remain pending.

- [Official project documentation](https://github.com/shinshin86/svg-aituber-chat)
- [Complete reviewed software license](https://github.com/shinshin86/svg-aituber-chat/blob/main/LICENSE)
### ComfyUI H3 Latent Relay · MIT

Experiment with continuity across generated H3 video segments.
ComfyUI nodes transfer a prior segment's audio/video latents into subsequent model conditioning without the stated decode/re-encode step.
Requires compatible ComfyUI/H3 support and separate model terms; seamless continuity and hardware claims need validation. Software license reviewed; full profile and hands-on output testing remain pending.

- [Official project documentation](https://github.com/ZenHG/ComfyUI-H3-Latent-Relay)
- [Complete reviewed software license](https://github.com/ZenHG/ComfyUI-H3-Latent-Relay/blob/main/LICENSE)
### HEISS UI · MIT

Use a simplified prompt/gallery interface with existing ComfyUI workflows.
The frontend exposes model-specific controls and routes diffusion image/video generation to ComfyUI.
Derived from J-AI Studio with retained MIT notices; workflow support, LAN setup and underlying model requirements remain pending. Software license reviewed; full profile and hands-on output testing remain pending.

- [Official project documentation](https://github.com/tristmeister/HEISS-UI)
- [Complete reviewed software license](https://github.com/tristmeister/HEISS-UI/blob/main/LICENSE)
### showtime · MIT

Build short edited videos through a coding agent and local rendering tools.
The agent directs scenes and uses the toolkit's media/rendering helpers to assemble a film.
Early release. Optional MusicGen and CrisperWhisper weights are non-commercial; other downloaded tools/models retain separate terms. Software license reviewed; full profile and hands-on output testing remain pending.

- [Official project documentation](https://github.com/FavioVazquez/showtime)
- [Complete reviewed software license](https://github.com/FavioVazquez/showtime/blob/main/LICENSE)
### opus-js-animations · MIT

Author an audio-led short film as editable JavaScript.
A Claude Code workflow develops a treatment, writes animation code and iteratively inspects rendered frames.
MIT workflow; proprietary agent access and third-party audio terms are separate. Model superiority claims and rendering requirements remain unverified. Software license reviewed; full profile and hands-on output testing remain pending.

- [Official project documentation](https://github.com/klsoen/opus-js-animations)
- [Complete reviewed software license](https://github.com/klsoen/opus-js-animations/blob/main/LICENSE)
### html-anime · MIT

Create a constrained anime-style short from an editable shot sheet.
A coding agent interprets the shot sheet and draws HTML scenes rendered by HyperFrames.
No trained video model is supplied. Agent access, font terms and output quality need further review. Software license reviewed; full profile and hands-on output testing remain pending.

- [Official project documentation](https://github.com/blixvip/html-anime)
- [Complete reviewed software license](https://github.com/blixvip/html-anime/blob/main/LICENSE)
### Infinite Canvas for ComfyUI · MIT

Organize generated media and references in a visual ComfyUI workspace.
Workflow-defined inputs drive text/image/video generation, with an assistant working from selected canvas context.
MIT source; current generation routing is ComfyUI-only. Detailed setup, model rights and local browser-storage behavior need review. Software license reviewed; full profile and hands-on output testing remain pending.

- [Official project documentation](https://github.com/ZhuYichuan/infinite-canvas)
- [Complete reviewed software license](https://github.com/ZhuYichuan/infinite-canvas/blob/main/LICENSE)

## Excluded and unresolved findings

Research notes only; these do not enter the eligible tool library.

- **OpenTryOn** · excluded: Software is offered under CC-BY-NC-4.0, which does not meet this library's open-source software requirement. [Source](https://github.com/tryonlabs/opentryon)
- **neural-tilde** · excluded: The package identifies non-commercial software terms; it is not admitted as an eligible open-source AI audio tool. [Source](https://pypi.org/project/neural-tilde/)
- **FASHN VTON 1.5** · needs-license-review: The project advertises Apache licensing, but the inspected license differs from standard text and GitHub did not classify it. The discrepancy needs clarification before eligibility is asserted. [Source](https://github.com/fashn-AI/fashn-vton-1.5) [Source](https://fashn.ai/blog/fashn-vton-1-5-open-source-release)
- **Bailando** · needs-license-review: The inspected software uses custom NTU S-Lab terms. A recognized unrestricted software grant has not been established. [Source](https://github.com/lisiyao21/Bailando)
- **AnimateDiff** · needs-license-review: An Apache license file coexists with academic-use-only wording in the README. This conflict prevents promotion to a detailed guide; prior historical entries are preserved. [Source](https://github.com/guoyww/AnimateDiff)
- **PersonaLive** · needs-license-review: Academic-use restrictions in the README conflict with the apparent Apache software grant. A complete component/permission clarification is needed before promotion. [Source](https://github.com/GVCLab/PersonaLive)
- **fugleramme** · needs-license-review: The visualization code is MIT, but its BirdNETGo AI dependency carries non-commercial/share-alike conditions. The integrated operating path needs a clearer component review. [Source](https://github.com/arnegiacomo/fugleramme)
- **VecFusion** · needs-license-review: The research README is available, but the license endpoint returned 404 and no complete software grant was verified. [Source](https://github.com/vikasTmz/VecFusion_CVPR24)
- **Sensus AI Hub** · needs-license-review: The hub's Apache license does not settle its vendored rPPG-Toolbox component, which carries Responsible AI License 1.1. Component restrictions need resolution. [Source](https://github.com/Sensus-AI-pt/sensus-ai-hub)
- **PAMI** · excluded: The repository contains a license and project description, but the inspected release checklist says code/weights are not yet released. It is a research announcement rather than usable released software today. [Source](https://github.com/Coral79/PAMI-Code)

Source collection completed: 2026-10-03T12:23:28.978965+00:00
Search is a bounded sample. Stars and recent pushes are discovery signals, not verified quality or meaningful upgrades.
