# AI Media Scout — 2026-10-02

The expanded daily search advances 37 earlier screened discoveries into complete guides and adds 14 first-time guides plus 54 additional screened leads. It covers 32 creative fields with 201 repository queries across active/newly-created/established lanes and 13 model tasks, supplemented by live primary-source research and metadata inspection beyond the automatic README shortlist. The main themes are local voice/media generation, editable agent-driven animation and video, neural 3D/CAD workflows, and physical interactive artworks. No software was installed or run: every profile is a documentation review. All published entries have an archived complete top-level open-source software license; weights, required proprietary hosts and paid services are labeled separately. The search is bounded: 92 repository queries sampled only their first 200 matches, and Codeberg/SourceHut remained inaccessible to primary-page review. Raw candidates are not verified recommendations; older projects are first-profiled guides, not automatically new releases.

Documentation reviewed today. Tools are not hands-on tested unless explicitly stated. Requirements and performance remain source-specific.

## Coverage

| Field | Finding |
| --- | --- |
| Images & design | Full guides cover segmentation, controllable generation and model orchestration, including BiRefNet, ControlNet and DiffSynth. FireRed instruction editing is retained as a screened lead; software openness does not settle every checkpoint license. [Source 1](https://github.com/ZhengPeng7/BiRefNet) [Source 2](https://github.com/lllyasviel/ControlNet) [Source 3](https://github.com/modelscope/DiffSynth-Studio) [Source 4](https://github.com/FireRedTeam/FireRed-Image-Edit) |
| Video, animation & film | Wan2.2, LTX-Video, CogVideo and Open-Sora receive first detailed guides; VDN-H3 adds a newer experimental acceleration stack. Paid-host and community-weight terms are explicitly separated from open code, and benchmark speeds were not reproduced. [Source 1](https://github.com/Wan-Video/Wan2.2) [Source 2](https://github.com/Lightricks/LTX-Video) [Source 3](https://github.com/OpenVDN/vdn-minimax-h3) |
| Audio, music & voice | The earlier voice/audio queue is advanced into guides for F5-TTS, CosyVoice, Qwen3-TTS, Bark, stable-audio-tools and real-time speech libraries. F5 and some other weights carry restrictions; voice fidelity and latency were not tested. [Source 1](https://github.com/SWivid/F5-TTS) [Source 2](https://github.com/QwenAudio/CosyVoice) [Source 3](https://github.com/QwenLM/Qwen3-TTS) [Source 4](https://github.com/Stability-AI/stable-audio-tools) |
| 3D, reconstruction & assets | Detailed guides cover learned splat rendering, single-image mesh reconstruction and multi-tool ComfyUI pipelines. TRELLIS has an MIT core but a separately non-commercial renderer; OpenReality also has restricted reconstruction dependencies. PartCrafter and Wonder3D remain pending full review. [Source 1](https://github.com/nerfstudio-project/gsplat) [Source 2](https://github.com/microsoft/TRELLIS) [Source 3](https://github.com/reality-opened/openreality) [Source 4](https://github.com/wgsxm/PartCrafter) |
| Browser tools & web media | Browser inference guides for WebLLM and Web Stable Diffusion are joined by editable Lottie and browser spatial/CAD workflows. A browser front end is not evidence of universal OS, GPU or local inference compatibility. [Source 1](https://github.com/mlc-ai/web-llm) [Source 2](https://github.com/mlc-ai/web-stable-diffusion) [Source 3](https://github.com/diffusionstudio/lottie) [Source 4](https://github.com/pascalorg/editor) |
| WebXR, VR & AR | FoveaEngine supplies a concrete neural-scene/Godot route with experimental OpenXR/foveation. SplatKit is a screened mobile neural-asset renderer. No newly reviewed project established complete WebXR/headset compatibility; desktop captures and mobile playback were not treated as VR validation. [Source 1](https://github.com/zedarvates/FoveaCore) [Source 2](https://github.com/Xget7/splatkit) |
| Computational art & creative coding | Dynamic Typography uses a diffusion prior to optimize vector letter motion. Agent-authored canvas, shader, particle and Manim workflows are additional screened creative-coding routes; these packages supply workflow code rather than bundled AI models. [Source 1](https://github.com/zliucz/animate-your-word) [Source 2](https://github.com/iart-ai/javascript-animation-skills) [Source 3](https://github.com/iart-ai/webgl-animation-skills) [Source 4](https://github.com/iart-ai/manim-skills) |
| Interactive, immersive & live media | Two unusually concrete installations receive guides: flipdot combines local learned pose tracking with a mechanical panel; Dissolution uses diffusion/ControlNet with visitor video. Their demos document author builds, not our reproducibility or real-time measurements. [Source 1](https://github.com/mdbug/flipdot) [Source 2](https://github.com/burakkagann/dissolution) |
| 3D printing & generative CAD | CADAM and KJDraw show agent-driven CAD workflows; Blender fabrication workflows and PartCrafter are screened for follow-up. Mesh generation, DXF export and part separation do not establish watertight geometry, toolpath validity or printing readiness. [Source 1](https://github.com/Adam-CAD/CADAM) [Source 2](https://github.com/KanJieTeam/kjdraw) [Source 3](https://github.com/jangtrinh/design-os-3d-blender) [Source 4](https://github.com/wgsxm/PartCrafter) |
| Games & production pipelines | MoMask supplies a learned motion-generation guide, and ComfyUI-3D-Pack/InstantMesh support experimental asset creation. Sprite generation, reference-driven Blender motion and splat scene tools are retained as leads; usable rigs, topology and animation quality still need testing. [Source 1](https://github.com/EricGuo5513/momask-codes) [Source 2](https://github.com/MrForExample/ComfyUI-3D-Pack) [Source 3](https://github.com/TencentARC/InstantMesh) [Source 4](https://github.com/Olafs-World/sprite-animator) [Source 5](https://github.com/xbishi/mocap-skills) |
| Motion capture & character animation | Motion Video Kit, Motion Launch Videos, Text-to-Lottie and Dynamic Typography cover code-authored, vector and diffusion-driven animation. Agent-driven renderers and model-generated motion have different runtime, host and weight terms. [Source 1](https://github.com/echris6/motion-video-kit) [Source 2](https://github.com/Kimeur/motion-launch-videos) [Source 3](https://github.com/diffusionstudio/lottie) [Source 4](https://github.com/zliucz/animate-your-word) |
| Avatars, digital humans & lip sync | Qwen3-TTS, CosyVoice and Bark provide voice-character routes while MoMask provides generated 3D motion. PersonaLive portrait streaming is a screened research lead; identity fidelity, portrait permissions and live performance have not been established by this documentation run. [Source 1](https://github.com/QwenLM/Qwen3-TTS) [Source 2](https://github.com/QwenAudio/CosyVoice) [Source 3](https://github.com/EricGuo5513/momask-codes) [Source 4](https://github.com/GVCLab/PersonaLive) |
| VFX, compositing & relighting | DWPose/GroundingDINO provide control and selection signals, IC-Light provides neural relighting, and ComfyUI-3D-Pack links generation workflows. These are components or research applications, with installation and checkpoint dependencies clearly separated from the main code license. [Source 1](https://github.com/IDEA-Research/DWPose) [Source 2](https://github.com/IDEA-Research/GroundingDINO) [Source 3](https://github.com/lllyasviel/IC-Light) [Source 4](https://github.com/MrForExample/ComfyUI-3D-Pack) |
| Spatial audio & volumetric media | Gaussian reconstruction and appearance workflows connect capture to browser/Godot scene design. Guides include gsplat, OpenReality and Pascal; LichtFeld, Lyra and Efficient Gaussian Appearance remain screened follow-ups. No architectural accuracy or headset support is certified. [Source 1](https://github.com/nerfstudio-project/gsplat) [Source 2](https://github.com/reality-opened/openreality) [Source 3](https://github.com/pascalorg/editor) [Source 4](https://github.com/MrNeRF/LichtFeld-Studio) [Source 5](https://github.com/nv-tlabs/lyra) |
| Photogrammetry, scanning & neural rendering | The research covers pose extraction, learned scene fitting and dynamic Gaussian reconstruction. Camera capture assumptions and model training are separate from playback; the report does not infer a scan is dimensionally accurate from an attractive render. [Source 1](https://github.com/IDEA-Research/DWPose) [Source 2](https://github.com/nerfstudio-project/gsplat) [Source 3](https://github.com/hustvl/4DGaussians) [Source 4](https://github.com/MrNeRF/LichtFeld-Studio) |
| Editing, captions & post-production | Sprocket, H3ddle, OpenLayer and restoration tools receive guides; OpenTake, kimchi, AIMO and Lumen are screened as editing applications. AI-agent control, local inference and paid hosted generation are labeled independently. [Source 1](https://github.com/SprocketVideo/Sprocket) [Source 2](https://github.com/AlexanderIstomin/h3ddle) [Source 3](https://github.com/MehranMarxian/OpenLayer) [Source 4](https://github.com/appergb/OpenTake) [Source 5](https://github.com/ludovic111/kimchi) [Source 6](https://github.com/uxKero/aimo) |
| Vector graphics, illustration & textures | Text-to-Lottie creates editable animation JSON, Dynamic Typography saves SVG frame logs, and KJDraw retains editable CAD objects. Pixel2Motion is a pending vectorization/motion workflow; vector output alone does not establish fidelity to a source logo. [Source 1](https://github.com/diffusionstudio/lottie) [Source 2](https://github.com/zliucz/animate-your-word) [Source 3](https://github.com/KanJieTeam/kjdraw) [Source 4](https://github.com/nolangz/pixel2motion) |
| Typography, fonts & layout | The expanded typography lane found diffusion-guided letter animation and code-authored kinetic titles. Dynamic Typography receives a guide; KineTy is excluded because its software license is non-commercial, despite strong research relevance. [Source 1](https://github.com/zliucz/animate-your-word) [Source 2](https://github.com/Kimeur/motion-launch-videos) [Source 3](https://github.com/SeonmiP/KineTy) |
| Storyboarding, narrative & comics | ReelMimic and voice tools receive guides; novel-to-manga/anime, ArcReel and Jellyfish extend story planning into panels and shot generation as pending profiles. Provider costs and story/character rights are separate from workflow code. [Source 1](https://github.com/edenfunf/reelmimic) [Source 2](https://github.com/SWivid/F5-TTS) [Source 3](https://github.com/BBQ2077/novel-to-manga-anime-generator) [Source 4](https://github.com/ArcReel/ArcReel) [Source 5](https://github.com/Forget-C/Jellyfish) |
| Creative publishing & presentation | Agent motion pipelines cover announcements, overlays and captioned clips. PPT Master and specialized video packs add editable slides and publication assets as screened leads; no social posting or publication account was connected by this research run. [Source 1](https://github.com/Kimeur/motion-launch-videos) [Source 2](https://github.com/echris6/motion-video-kit) [Source 3](https://github.com/hugohe3/ppt-master) [Source 4](https://github.com/iart-ai/lower-thirds-skills) [Source 5](https://github.com/WEIFENG2333/VideoCaptioner) |
| Photography, restoration & color | BiRefNet and IC-Light provide foreground/relighting guides; Klarity and photo-restorer provide local enhancement routes. Neural restoration and colorization can synthesize plausible detail rather than recover historical facts. [Source 1](https://github.com/ZhengPeng7/BiRefNet) [Source 2](https://github.com/lllyasviel/IC-Light) [Source 3](https://github.com/HAKORADev/Klarity) [Source 4](https://github.com/reiarthur/photo-restorer) |
| Data art & scientific visualization | KJDraw has a detailed editable-drawing guide. Data, map and Manim agent packages plus Leap MCP are screened for animated explanations; these sources establish a workflow, not correctness of generated numbers or scientific explanations. [Source 1](https://github.com/KanJieTeam/kjdraw) [Source 2](https://github.com/iart-ai/data-animation-skills) [Source 3](https://github.com/iart-ai/map-animation-skills) [Source 4](https://github.com/iart-ai/manim-skills) [Source 5](https://github.com/sid-thephysicskid/leap-mcp) |
| Physical, robotic & kinetic installations | Mechanical flip-dot and diffusion-mirror works broaden the scope beyond screen-based generators. Fugleramme adds a local bird-audio classifier driving curated e-ink illustrations as a screened physical-computing lead. [Source 1](https://github.com/mdbug/flipdot) [Source 2](https://github.com/burakkagann/dissolution) [Source 3](https://github.com/arnegiacomo/fugleramme) |
| Performance, projection & stage media | Real-time STT/TTS libraries, webcam installations and PersonaLive suggest live voice/visual workflows. Their runtime and latency depend on the configured models and hardware; no public-performance timing or stream was tested. [Source 1](https://github.com/KoljaB/RealtimeSTT) [Source 2](https://github.com/KoljaB/RealtimeTTS) [Source 3](https://github.com/burakkagann/dissolution) [Source 4](https://github.com/GVCLab/PersonaLive) |
| Fashion, textiles & wearable media | FireRed editing and the OpenVTO avatar/garment/video pipeline are screened for creative try-on concepts. OpenVTO requires proprietary Vertex AI billing; neither source is evidence of garment fit or fabrication correctness. Restricted/missing-license fashion candidates were withheld. [Source 1](https://github.com/FireRedTeam/FireRed-Image-Edit) [Source 2](https://github.com/Prompt-Haus/OpenVTO) [Source 3](https://github.com/alhussein-jamil/clothes-changer) |
| Accessible media & assistive creation | PaddleOCR, speech recognition and TTS can support searchable visual text, captions and audio descriptions. VideoCaptioner and reduced-motion web workflows remain screened follow-ups; transcript accuracy and accessible presentation need human review. [Source 1](https://github.com/PaddlePaddle/PaddleOCR) [Source 2](https://github.com/KoljaB/RealtimeSTT) [Source 3](https://github.com/QwenLM/Qwen3-TTS) [Source 4](https://github.com/WEIFENG2333/VideoCaptioner) [Source 5](https://github.com/iart-ai/web-animation-skills) |
| Mobile, edge & on-device creation | Mine StableDiffusion and SplatKit document native-device AI-image/learned-scene routes as screened leads. Text-to-Lottie has mobile rendering bindings, which do not prove phone-side AI generation. Device memory/backend matrices still need dedicated review. [Source 1](https://github.com/Onion99/KMP-MineStableDiffusion) [Source 2](https://github.com/Xget7/splatkit) [Source 3](https://github.com/diffusionstudio/lottie) |
| Creative learning & authoring | Editable slide generation, mathematical animation and audio-reactive natural-history display extend creative AI into teaching. Manim/Leap/PPT/Fugleramme are screened examples; explanatory accuracy and model/platform requirements remain pending. [Source 1](https://github.com/hugohe3/ppt-master) [Source 2](https://github.com/iart-ai/manim-skills) [Source 3](https://github.com/sid-thephysicskid/leap-mcp) [Source 4](https://github.com/arnegiacomo/fugleramme) |
| Archives, media restoration & collections | Klarity and photo-restorer offer explicit local restoration guides, with full requirements where published and unknowns where absent. A claimed restoration repository with empty implementation files was excluded; attractive download-page claims are not source verification. [Source 1](https://github.com/HAKORADev/Klarity) [Source 2](https://github.com/reiarthur/photo-restorer) [Source 3](https://github.com/GridMayorTell/photo-restoration-enhancer) |
| Emerging & cross-disciplinary creative AI | VDN-H3, Lyra, part-structured meshes, dynamic splats and scene appearance models are concrete emerging/research practices. Code-license reviews do not make community/non-commercial weights unrestricted; recent commits and stars were used for discovery only. [Source 1](https://github.com/OpenVDN/vdn-minimax-h3) [Source 2](https://github.com/nv-tlabs/lyra) [Source 3](https://github.com/wgsxm/PartCrafter) [Source 4](https://github.com/hustvl/4DGaussians) [Source 5](https://github.com/nerficg-project/efficient-gaussian-appearance) |
| AI kinetic typography and animated lettering | The adaptive field yielded a full Dynamic Typography guide and kinetic-title agent tooling. New source coverage expands actual practices rather than setting a fixed daily tool count; the non-commercial KineTy code remains excluded. [Source 1](https://github.com/zliucz/animate-your-word) [Source 2](https://github.com/Kimeur/motion-launch-videos) [Source 3](https://github.com/iart-ai/kinetic-typography-skills) [Source 4](https://github.com/SeonmiP/KineTy) |
| AI agents for code-authored media production | AI-agent control of real timelines, editable Lottie/CAD/building scenes and frame-based motion production is covered with explicit host/model separation. These packages provide creative workflow software or skills; they are not themselves proof that a bundled language model is open source. [Source 1](https://github.com/SprocketVideo/Sprocket) [Source 2](https://github.com/diffusionstudio/lottie) [Source 3](https://github.com/KanJieTeam/kjdraw) [Source 4](https://github.com/pascalorg/editor) [Source 5](https://github.com/Kimeur/motion-launch-videos) |

## Search and review counts

32 creative fields; 201/201 repository queries attempted; 13/13 model-task queries attempted. 17754 distinct source candidates and 610 model leads. 51 detailed profiles and 54 additional screened discoveries. Source gaps: 0 failed repository queries, 0 partial repository queries, 92 bounded repository queries, 0 failed model-task queries and 2 web ecosystem gaps. Raw search candidates include duplicates of known tools, excluded projects and projects awaiting review; they are not verified recommendations.

## Research beyond GitHub

- **gitlab** · searched: Live primary-source research found Video2X and DiffusionBee mirrors. These were treated as upstream duplicates, not additional verified unique tools; no separately qualified new GitLab-native creative tool was established in this pass. [Source](https://gitlab.com/ai-image-and-text-processing/video-and-image-upscale/video2x) [Source](https://gitlab.com/syahdafahreza/diffusionbee-stable-diffusion-ui/-/blob/master/README.md)
- **codeberg** · gap: Live source fetching was blocked by the site robots policy. Search snippets did not provide a complete independent license/use review, so no Codeberg-hosted tool is claimed verified in this edition.
- **sourcehut** · gap: Live primary-page fetching was blocked by robots restrictions. No independently archived SourceHut license plus concrete creative-AI implementation was obtained; the ecosystem remains an explicit research gap.
- **packages** · searched: PyPI sprite-animator corresponds to the reviewed original source and its proprietary Gemini-backed workflow. Registry labels for kin3o and a Lottie creator package were not substituted for complete source-license evidence. [Source](https://pypi.org/project/sprite-animator/0.2.0/) [Source](https://www.npmjs.com/package/%40afromero/kin3o) [Source](https://www.npmjs.com/package/%40lottiefiles/creator-mcp)
- **creative-plugins** · searched: Primary plug-in sources cover local ComfyUI/Photoshop layers, Godot neural scenes and Blender AI generation. Required paid hosts/services and experimental platform support are labeled separately. [Source](https://github.com/MehranMarxian/OpenLayer) [Source](https://github.com/zedarvates/FoveaCore) [Source](https://github.com/scenario-labs/blender-plugin)
- **project-sites** · searched: Official Dynamic Typography demos and Text-to-Lottie release material supplement repository research. Developer examples establish a claimed workflow, not a hands-on quality or performance test. [Source](https://animate-your-word.github.io/demo/) [Source](https://diffusion.studio/changelog/text-to-lottie-v1/)
- **research-code** · searched: Dynamic Typography and VDN-H3 have archived open software licenses and concrete motion/video uses. KineTy uses non-commercial software terms and TransText lacked a completed source-license review, so they are not eligible library additions. [Source](https://github.com/zliucz/animate-your-word) [Source](https://github.com/OpenVDN/vdn-minimax-h3) [Source](https://github.com/SeonmiP/KineTy) [Source](https://sii-ferenas.github.io/TransText/)
- **international** · searched: Chinese/international primary material includes Qwen/FunAudioLLM model cards, PaddleOCR documentation and Chinese-language caption, Blender-motion and film-production workflows. Model terms were checked separately where available; untranslated or missing requirements were not guessed. [Source](https://huggingface.co/Qwen/Qwen3-TTS-12Hz-1.7B-VoiceDesign) [Source](https://huggingface.co/FunAudioLLM/Fun-CosyVoice3-0.5B-2512) [Source](https://github.com/PaddlePaddle/PaddleOCR) [Source](https://github.com/WEIFENG2333/VideoCaptioner) [Source](https://github.com/xbishi/mocap-skills)
- **physical-computing** · searched: Adaptive primary research adds visitor-reactive mechanical displays, a GPU portrait installation and an audio-classified e-ink illustration frame. Hardware is part of these works and not inferred from a browser interface. [Source](https://github.com/mdbug/flipdot) [Source](https://github.com/burakkagann/dissolution) [Source](https://github.com/arnegiacomo/fugleramme)

## Collection limitations

- images: bounded or incomplete query: topic:diffusion pushed:>=2026-09-02 is:public fork:false archived:false (200 of 201 matches sampled)
- images: bounded or incomplete query: topic:diffusion is:public fork:false archived:false (200 of 1417 matches sampled)
- images: bounded or incomplete query: AI image generation pushed:>=2026-09-02 is:public fork:false archived:false (200 of 1631 matches sampled)
- images: bounded or incomplete query: AI image generation created:>=2026-09-02 is:public fork:false archived:false (200 of 821 matches sampled)
- images: bounded or incomplete query: AI image generation is:public fork:false archived:false (200 of 15266 matches sampled)
- video: bounded or incomplete query: AI video pushed:>=2026-09-02 is:public fork:false archived:false (200 of 12160 matches sampled)
- video: bounded or incomplete query: AI video created:>=2026-09-02 is:public fork:false archived:false (200 of 7689 matches sampled)
- video: bounded or incomplete query: AI video is:public fork:false archived:false (200 of 81791 matches sampled)
- video: bounded or incomplete query: topic:video-generation pushed:>=2026-09-02 is:public fork:false archived:false (200 of 1455 matches sampled)
- video: bounded or incomplete query: topic:video-generation created:>=2026-09-02 is:public fork:false archived:false (200 of 548 matches sampled)
- video: bounded or incomplete query: topic:video-generation is:public fork:false archived:false (200 of 3730 matches sampled)
- audio: bounded or incomplete query: topic:music-generation pushed:>=2026-09-02 is:public fork:false archived:false (200 of 287 matches sampled)
- audio: bounded or incomplete query: topic:music-generation is:public fork:false archived:false (200 of 1161 matches sampled)
- audio: bounded or incomplete query: AI audio pushed:>=2026-09-02 is:public fork:false archived:false (200 of 3696 matches sampled)
- audio: bounded or incomplete query: AI audio created:>=2026-09-02 is:public fork:false archived:false (200 of 1980 matches sampled)
- audio: bounded or incomplete query: AI audio is:public fork:false archived:false (200 of 27328 matches sampled)
- 3d: bounded or incomplete query: 3D generation pushed:>=2026-09-02 is:public fork:false archived:false (200 of 679 matches sampled)
- 3d: bounded or incomplete query: 3D generation created:>=2026-09-02 is:public fork:false archived:false (200 of 372 matches sampled)
- 3d: bounded or incomplete query: 3D generation is:public fork:false archived:false (200 of 5731 matches sampled)
- 3d: bounded or incomplete query: topic:3d-reconstruction pushed:>=2026-09-02 is:public fork:false archived:false (200 of 250 matches sampled)
- 3d: bounded or incomplete query: topic:3d-reconstruction is:public fork:false archived:false (200 of 1893 matches sampled)
- web: bounded or incomplete query: topic:webgpu pushed:>=2026-09-02 is:public fork:false archived:false (200 of 991 matches sampled)
- web: bounded or incomplete query: topic:webgpu created:>=2026-09-02 is:public fork:false archived:false (200 of 398 matches sampled)
- web: bounded or incomplete query: topic:webgpu is:public fork:false archived:false (200 of 2727 matches sampled)
- xr: bounded or incomplete query: AI VR pushed:>=2026-09-02 is:public fork:false archived:false (200 of 323 matches sampled)
- xr: bounded or incomplete query: AI VR is:public fork:false archived:false (200 of 2819 matches sampled)
- computational: bounded or incomplete query: AI creative coding is:public fork:false archived:false (200 of 906 matches sampled)
- computational: bounded or incomplete query: topic:generative-art pushed:>=2026-09-02 is:public fork:false archived:false (200 of 755 matches sampled)
- computational: bounded or incomplete query: topic:generative-art created:>=2026-09-02 is:public fork:false archived:false (200 of 354 matches sampled)
- computational: bounded or incomplete query: topic:generative-art is:public fork:false archived:false (200 of 3768 matches sampled)
- interactive: bounded or incomplete query: AI interactive art is:public fork:false archived:false (200 of 668 matches sampled)
- fabrication: bounded or incomplete query: AI CAD pushed:>=2026-09-02 is:public fork:false archived:false (200 of 659 matches sampled)
- fabrication: bounded or incomplete query: AI CAD created:>=2026-09-02 is:public fork:false archived:false (200 of 376 matches sampled)
- fabrication: bounded or incomplete query: AI CAD is:public fork:false archived:false (200 of 2942 matches sampled)
- fabrication: bounded or incomplete query: AI 3D printing is:public fork:false archived:false (200 of 335 matches sampled)
- gaming: bounded or incomplete query: AI game assets is:public fork:false archived:false (200 of 618 matches sampled)
- gaming: bounded or incomplete query: AI blender pushed:>=2026-09-02 is:public fork:false archived:false (200 of 397 matches sampled)
- gaming: bounded or incomplete query: AI blender created:>=2026-09-02 is:public fork:false archived:false (200 of 287 matches sampled)
- gaming: bounded or incomplete query: AI blender is:public fork:false archived:false (200 of 1491 matches sampled)
- motion: bounded or incomplete query: AI motion capture is:public fork:false archived:false (200 of 228 matches sampled)
- motion: bounded or incomplete query: motion generation is:public fork:false archived:false (200 of 1482 matches sampled)
- avatars: bounded or incomplete query: AI avatar pushed:>=2026-09-02 is:public fork:false archived:false (200 of 751 matches sampled)
- avatars: bounded or incomplete query: AI avatar created:>=2026-09-02 is:public fork:false archived:false (200 of 414 matches sampled)
- avatars: bounded or incomplete query: AI avatar is:public fork:false archived:false (200 of 5799 matches sampled)
- avatars: bounded or incomplete query: lip sync pushed:>=2026-09-02 is:public fork:false archived:false (200 of 273 matches sampled)
- avatars: bounded or incomplete query: lip sync is:public fork:false archived:false (200 of 2349 matches sampled)
- vfx: bounded or incomplete query: AI visual effects is:public fork:false archived:false (200 of 411 matches sampled)
- capture: bounded or incomplete query: topic:gaussian-splatting pushed:>=2026-09-02 is:public fork:false archived:false (200 of 233 matches sampled)
- capture: bounded or incomplete query: topic:gaussian-splatting is:public fork:false archived:false (200 of 889 matches sampled)
- capture: bounded or incomplete query: neural reconstruction is:public fork:false archived:false (200 of 1309 matches sampled)
- editing: bounded or incomplete query: AI video editing pushed:>=2026-09-02 is:public fork:false archived:false (200 of 770 matches sampled)
- editing: bounded or incomplete query: AI video editing created:>=2026-09-02 is:public fork:false archived:false (200 of 476 matches sampled)
- editing: bounded or incomplete query: AI video editing is:public fork:false archived:false (200 of 3303 matches sampled)
- editing: bounded or incomplete query: AI subtitle pushed:>=2026-09-02 is:public fork:false archived:false (200 of 354 matches sampled)
- editing: bounded or incomplete query: AI subtitle is:public fork:false archived:false (200 of 2175 matches sampled)
- vector: bounded or incomplete query: AI SVG pushed:>=2026-09-02 is:public fork:false archived:false (200 of 424 matches sampled)
- vector: bounded or incomplete query: AI SVG created:>=2026-09-02 is:public fork:false archived:false (200 of 236 matches sampled)
- vector: bounded or incomplete query: AI SVG is:public fork:false archived:false (200 of 1731 matches sampled)
- typography: bounded or incomplete query: AI typography is:public fork:false archived:false (200 of 632 matches sampled)
- typography: bounded or incomplete query: font generation is:public fork:false archived:false (200 of 414 matches sampled)
- storytelling: bounded or incomplete query: AI storyboard pushed:>=2026-09-02 is:public fork:false archived:false (200 of 349 matches sampled)
- storytelling: bounded or incomplete query: AI storyboard is:public fork:false archived:false (200 of 1620 matches sampled)
- storytelling: bounded or incomplete query: AI comic pushed:>=2026-09-02 is:public fork:false archived:false (200 of 1488 matches sampled)
- storytelling: bounded or incomplete query: AI comic created:>=2026-09-02 is:public fork:false archived:false (200 of 1401 matches sampled)
- storytelling: bounded or incomplete query: AI comic is:public fork:false archived:false (200 of 2738 matches sampled)
- publishing: bounded or incomplete query: AI presentation pushed:>=2026-09-02 is:public fork:false archived:false (200 of 1096 matches sampled)
- publishing: bounded or incomplete query: AI presentation created:>=2026-09-02 is:public fork:false archived:false (200 of 670 matches sampled)
- publishing: bounded or incomplete query: AI presentation is:public fork:false archived:false (200 of 8350 matches sampled)
- publishing: bounded or incomplete query: AI publishing pushed:>=2026-09-02 is:public fork:false archived:false (200 of 1044 matches sampled)
- publishing: bounded or incomplete query: AI publishing created:>=2026-09-02 is:public fork:false archived:false (200 of 643 matches sampled)
- publishing: bounded or incomplete query: AI publishing is:public fork:false archived:false (200 of 3934 matches sampled)
- photography: bounded or incomplete query: AI colorization pushed:>=2026-09-02 is:public fork:false archived:false (200 of 439 matches sampled)
- photography: bounded or incomplete query: AI colorization created:>=2026-09-02 is:public fork:false archived:false (200 of 275 matches sampled)
- photography: bounded or incomplete query: AI colorization is:public fork:false archived:false (200 of 4666 matches sampled)
- visualization: bounded or incomplete query: AI visualization pushed:>=2026-09-02 is:public fork:false archived:false (200 of 3249 matches sampled)
- visualization: bounded or incomplete query: AI visualization created:>=2026-09-02 is:public fork:false archived:false (200 of 1882 matches sampled)
- visualization: bounded or incomplete query: AI visualization is:public fork:false archived:false (200 of 37326 matches sampled)
- visualization: bounded or incomplete query: AI data art is:public fork:false archived:false (200 of 1013 matches sampled)
- performance: bounded or incomplete query: AI live visuals is:public fork:false archived:false (200 of 694 matches sampled)
- fashion: bounded or incomplete query: AI fashion design is:public fork:false archived:false (200 of 632 matches sampled)
- fashion: bounded or incomplete query: AI textile is:public fork:false archived:false (200 of 459 matches sampled)
- accessibility: bounded or incomplete query: AI audio description is:public fork:false archived:false (200 of 251 matches sampled)
- mobile: bounded or incomplete query: AI mobile media is:public fork:false archived:false (200 of 205 matches sampled)
- education: bounded or incomplete query: AI explainer pushed:>=2026-09-02 is:public fork:false archived:false (200 of 6449 matches sampled)
- education: bounded or incomplete query: AI explainer created:>=2026-09-02 is:public fork:false archived:false (200 of 4463 matches sampled)
- education: bounded or incomplete query: AI explainer is:public fork:false archived:false (200 of 36050 matches sampled)
- frontier: bounded or incomplete query: AI creative tools pushed:>=2026-09-02 is:public fork:false archived:false (200 of 230 matches sampled)
- frontier: bounded or incomplete query: AI creative tools is:public fork:false archived:false (200 of 1926 matches sampled)
- frontier: bounded or incomplete query: AI digital art is:public fork:false archived:false (200 of 711 matches sampled)
- frontier: bounded or incomplete query: AI multimedia is:public fork:false archived:false (200 of 1158 matches sampled)
- frontier: bounded or incomplete query: AI new media is:public fork:false archived:false (200 of 500 matches sampled)
- agent-media-production: bounded or incomplete query: AI agent animation is:public fork:false archived:false (200 of 482 matches sampled)

## F5-TTS

Audio, music & voice · Storyboarding, narrative & comics · Accessible media & assistive creation

First complete guide for a previously screened discovery; documentation checked today. Repository created 2024-10-08; current source metadata is a discovery signal, not evidence of a significant product upgrade.

### How it uses AI

Flow-matching speech synthesis uses permitted reference audio/text to condition a narrated creative output. [Source](https://github.com/SWivid/F5-TTS/blob/main/README.md)

### Introduction

A flow-matching speech synthesizer with reference-audio voice conditioning and a Gradio interface. [Source 1](https://github.com/SWivid/F5-TTS/blob/main/README.md)

### What it is good for

Try a narrated exhibition introduction, audio description or multilingual voice-over using a recording you have permission to use. [Source 1](https://github.com/SWivid/F5-TTS/blob/main/README.md)

### Demo & examples

The authors publish speech examples on their project page; the local Gradio app is the reproducible demo route. [Source 1](https://github.com/SWivid/F5-TTS/blob/main/README.md) [Source 2](https://swivid.github.io/F5-TTS/)

### Install

Documentation-based setup route; commands are examples from the project and were not executed during this review. [Source 1](https://github.com/SWivid/F5-TTS/blob/main/README.md)

1. Create an isolated Python environment; install the PyTorch build matching your accelerator and FFmpeg.
2. Install the official f5-tts package, then start the inference GUI.

```sh
pip install f5-tts
```


```sh
f5-tts_infer-gradio
```

### First project

Begin with a small, permitted sample and inspect the result. [Source 1](https://github.com/SWivid/F5-TTS/blob/main/README.md)

1. Select a checkpoint and upload permitted reference audio with its transcript.
2. Enter a short narration, synthesize and listen for pronunciation and voice consistency.
3. Export the result and edit pacing in your audio editor.
### Hardware & software

Published requirements and explicit documentation gaps follow. [Source 1](https://github.com/SWivid/F5-TTS/blob/main/README.md)

- **Hardware:** CPU/GPU backends are documented. Minimum RAM, VRAM and total model storage are not documented in the inspected quickstart.
- **Software:** Python >=3.10; PyTorch, FFmpeg and checkpoint assets. The README provides CUDA, Linux ROCm, Intel XPU and Apple Silicon MPS setup alternatives.
- **Platforms:** Documented accelerator paths include NVIDIA, AMD on Linux, Intel and Apple Silicon. A matching backend is required; there is no claim of identical performance across platforms.

### License, model weights & costs

The complete top-level MIT software terms were reviewed and archived today; model/dependency/host terms remain separate. [Source 1](https://github.com/SWivid/F5-TTS/blob/main/LICENSE) [Source 2](https://github.com/SWivid/F5-TTS/blob/main/README.md)

- **Code:** MIT
- **Weights:** The README states that its distributed pretrained models are CC-BY-NC because of the Emilia training data. MIT software does not remove that non-commercial weight restriction.
- **Commercial:** The main MIT code grant permits commercial use under its notice/source and other conditions. Model, component, asset and hosted-service permission is separate. The README states that its distributed pretrained models are CC-BY-NC because of the Emilia training data. MIT software does not remove that non-commercial weight restriction.
- **Cost:** Software has no license fee; local compute or rented hardware costs apply. No paid inference service is required for the documented local route.

### Why it merits attention

Assessment: explicit reference-audio workflows, a GUI and multiple accelerator instructions make it a useful voice experimentation tool. Documentation review only; no speech was generated here. [Source 1](https://github.com/SWivid/F5-TTS/blob/main/README.md)

### Limitations

Do not use the bundled non-commercial checkpoints as an unrestricted commercial voice solution. Speech artifacts and mispronunciations require listening and correction. [Source 1](https://github.com/SWivid/F5-TTS/blob/main/README.md) [Source 2](https://github.com/SWivid/F5-TTS/blob/main/LICENSE)

### Get the tool

- [Repository](https://github.com/SWivid/F5-TTS)
- [Documentation](https://github.com/SWivid/F5-TTS/blob/main/README.md)
- [Demo](https://swivid.github.io/F5-TTS/)

## CosyVoice 3

Audio, music & voice · Accessible media & assistive creation · Avatars, digital humans & lip sync

First complete guide for a previously screened discovery; documentation checked today. Repository created 2024-07-03; current source metadata is a discovery signal, not evidence of a significant product upgrade.

### How it uses AI

Its learned speech models synthesize multilingual, speaker-conditioned narration from text and reference recordings. [Source](https://github.com/QwenAudio/CosyVoice/blob/main/README.md)

### Introduction

Multilingual neural text-to-speech with zero-shot voice conditioning, cross-lingual synthesis and a streaming-oriented deployment stack. [Source 1](https://github.com/QwenAudio/CosyVoice/blob/main/README.md)

### What it is good for

Create character dialogue, multilingual narration or interactive spoken guides; use authorized reference voices. [Source 1](https://github.com/QwenAudio/CosyVoice/blob/main/README.md)

### Demo & examples

The local web interface is the documented audition route. The README also points to author examples, but its CosyVoice3 demo URL returned 404 during today’s source check. [Source 1](https://github.com/QwenAudio/CosyVoice/blob/main/README.md)

### Install

Documentation-based setup route; commands are examples from the project and were not executed during this review. [Source 1](https://github.com/QwenAudio/CosyVoice/blob/main/README.md)

1. Clone the official repository with submodules and create its documented Python 3.10 environment.
2. Install requirements and select a matching checkpoint from the model list.
3. Follow example.py for the chosen generation mode; use the web UI instructions for a compatible checkpoint.

```sh
pip install -r requirements.txt
```


```sh
python example.py
```

### First project

Begin with a small, permitted sample and inspect the result. [Source 1](https://github.com/QwenAudio/CosyVoice/blob/main/README.md)

1. Load a checkpoint and its matching tokenizer/frontend assets.
2. Start with a short text and reference audio; compare ordinary, zero-shot and cross-lingual modes.
3. Review intelligibility before exporting speech into an edit.
### Hardware & software

Published requirements and explicit documentation gaps follow. [Source 1](https://github.com/QwenAudio/CosyVoice/blob/main/README.md)

- **Hardware:** The main examples use GPU-backed inference. Hard minimum RAM, VRAM and storage are not documented in the inspected README.
- **Software:** Python 3.10 example environment; PyTorch and requirements.txt. SoX and optional Linux x86_64 ttsfrd assets have separate installation steps; the default frontend can use wetext.
- **Platforms:** Linux and NVIDIA/Docker deployment examples are documented. Native Windows and macOS support for the full current stack is not confirmed by this review.

### License, model weights & costs

The complete top-level Apache-2.0 software terms were reviewed and archived today; model/dependency/host terms remain separate. [Source 1](https://github.com/QwenAudio/CosyVoice/blob/main/LICENSE) [Source 2](https://github.com/QwenAudio/CosyVoice/blob/main/README.md) [Source 3](https://huggingface.co/FunAudioLLM/Fun-CosyVoice3-0.5B-2512)

- **Code:** Apache-2.0
- **Weights:** The Fun-CosyVoice3-0.5B-2512 model card identifies Apache-2.0. Check the exact checkpoint rather than extending those terms to every historical CosyVoice model.
- **Commercial:** The main Apache-2.0 code grant permits commercial use under its notice/source and other conditions. Model, component, asset and hosted-service permission is separate. The Fun-CosyVoice3-0.5B-2512 model card identifies Apache-2.0. Check the exact checkpoint rather than extending those terms to every historical CosyVoice model.
- **Cost:** Local inference avoids a mandatory paid speech API; hardware and any chosen cloud deployment have their own costs.

### Why it merits attention

Assessment: published multilingual examples and separate frontend, inference and serving instructions support practical evaluation. No hands-on voice or latency testing was performed. [Source 1](https://github.com/QwenAudio/CosyVoice/blob/main/README.md)

### Limitations

The vLLM instructions distinguish supported versions; mixing versions is a compatibility risk. The web UI example uses an older 300M checkpoint and must not be assumed to load every v3 variant unchanged. The linked CosyVoice3 project-demo page was unavailable at the documentation check; this does not establish that local inference is broken. [Source 1](https://github.com/QwenAudio/CosyVoice/blob/main/README.md) [Source 2](https://github.com/QwenAudio/CosyVoice/blob/main/LICENSE) [Source 3](https://huggingface.co/FunAudioLLM/Fun-CosyVoice3-0.5B-2512)

### Get the tool

- [Repository](https://github.com/QwenAudio/CosyVoice)
- [Documentation](https://github.com/QwenAudio/CosyVoice/blob/main/README.md)

## Qwen3-TTS

Audio, music & voice · Avatars, digital humans & lip sync · Accessible media & assistive creation

First complete guide for a previously screened discovery; documentation checked today. Repository created 2026-01-21; current source metadata is a discovery signal, not evidence of a significant product upgrade.

### How it uses AI

Learned speech generation supports designed voices and reference-conditioned narration for media. [Source](https://github.com/QwenLM/Qwen3-TTS/blob/main/README.md)

### Introduction

A neural speech family offering described voice design, preset speaker control and reference-audio voice cloning in ten documented languages. [Source 1](https://github.com/QwenLM/Qwen3-TTS/blob/main/README.md)

### What it is good for

Design a fictional narrator, create localized game dialogue or test a voice interface without committing to a hosted speech API. [Source 1](https://github.com/QwenLM/Qwen3-TTS/blob/main/README.md)

### Demo & examples

qwen-tts-demo exposes the VoiceDesign, CustomVoice and Base models through a local Gradio UI; their capabilities differ. [Source 1](https://github.com/QwenLM/Qwen3-TTS/blob/main/README.md)

### Install

Documentation-based setup route; commands are examples from the project and were not executed during this review. [Source 1](https://github.com/QwenLM/Qwen3-TTS/blob/main/README.md)

1. Create the recommended clean Python 3.12 environment.
2. Install qwen-tts, then choose the model matching voice design, preset voices or cloning.
3. Use qwen-tts-demo --help and launch the corresponding local demo.

```sh
pip install -U qwen-tts
```


```sh
qwen-tts-demo --help
```

### First project

Begin with a small, permitted sample and inspect the result. [Source 1](https://github.com/QwenLM/Qwen3-TTS/blob/main/README.md)

1. For VoiceDesign, describe vocal style and enter a short script.
2. For Base, supply authorized reference audio; check the browser microphone/HTTPS notes if using a remote UI.
3. Generate, listen and save a comparison before using the speech in a project.
### Hardware & software

Published requirements and explicit documentation gaps follow. [Source 1](https://github.com/QwenLM/Qwen3-TTS/blob/main/README.md)

- **Hardware:** README examples use a CUDA device and float16/bfloat16 attention. Minimum RAM, VRAM and storage are not specified. The 96 GB figure concerns FlashAttention compilation concurrency, not an inference minimum.
- **Software:** Recommended Python 3.12, qwen-tts and model downloads. FlashAttention 2 is optional and needs compatible hardware; serving via vLLM is a separate route.
- **Platforms:** CUDA examples are documented. A web UI is a client interface and does not establish native macOS, Windows or mobile generation support for all backends.

### License, model weights & costs

The complete top-level Apache-2.0 software terms were reviewed and archived today; model/dependency/host terms remain separate. [Source 1](https://github.com/QwenLM/Qwen3-TTS/blob/main/LICENSE) [Source 2](https://github.com/QwenLM/Qwen3-TTS/blob/main/README.md) [Source 3](https://huggingface.co/Qwen/Qwen3-TTS-12Hz-1.7B-VoiceDesign)

- **Code:** Apache-2.0
- **Weights:** The inspected Qwen3-TTS-12Hz-1.7B-VoiceDesign model card lists Apache-2.0. Verify other model variants individually; DashScope is a separately governed hosted service.
- **Commercial:** The main Apache-2.0 code grant permits commercial use under its notice/source and other conditions. Model, component, asset and hosted-service permission is separate. The inspected Qwen3-TTS-12Hz-1.7B-VoiceDesign model card lists Apache-2.0. Verify other model variants individually; DashScope is a separately governed hosted service.
- **Cost:** Local code and the inspected checkpoint have no license fee. Local compute costs remain; optional DashScope API usage is separate.

### Why it merits attention

Assessment: clear separation of model modes and a packaged demo make comparison repeatable. The authors low-latency claims are not independently reproduced here. [Source 1](https://github.com/QwenLM/Qwen3-TTS/blob/main/README.md)

### Limitations

Clone only voices you are authorized to use. Do not present model-size differences or developer latency measurements as guaranteed quality or performance. [Source 1](https://github.com/QwenLM/Qwen3-TTS/blob/main/README.md) [Source 2](https://github.com/QwenLM/Qwen3-TTS/blob/main/LICENSE) [Source 3](https://huggingface.co/Qwen/Qwen3-TTS-12Hz-1.7B-VoiceDesign)

### Get the tool

- [Repository](https://github.com/QwenLM/Qwen3-TTS)
- [Documentation](https://github.com/QwenLM/Qwen3-TTS/blob/main/README.md)

## RealtimeSTT

Audio, music & voice · Interactive, immersive & live media · Accessible media & assistive creation · Physical, robotic & kinetic installations

First complete guide for a previously screened discovery; documentation checked today. Repository created 2023-08-29; current source metadata is a discovery signal, not evidence of a significant product upgrade.

### How it uses AI

Whisper-family and optional speech engines transcribe streamed audio into text for captions, performance controls and media logging. [Source](https://github.com/KoljaB/RealtimeSTT/blob/master/README.md)

### Introduction

A speech-recognition library combining neural ASR, voice activity detection, streaming callbacks and optional wake words. [Source 1](https://github.com/KoljaB/RealtimeSTT/blob/master/README.md)

### What it is good for

Drive an interactive artwork with spoken input, prototype live captions or build a voice-operated creative interface. [Source 1](https://github.com/KoljaB/RealtimeSTT/blob/master/README.md)

### Demo & examples

The README includes microphone and external PCM examples; a browser streaming reference application and production server are documented. [Source 1](https://github.com/KoljaB/RealtimeSTT/blob/master/README.md)

### Install

Documentation-based setup route; commands are examples from the project and were not executed during this review. [Source 1](https://github.com/KoljaB/RealtimeSTT/blob/master/README.md) [Source 2](https://github.com/KoljaB/RealtimeSTT/blob/master/docs/installation.md)

1. Use Python 3.11 or 3.12, the current CI targets.
2. Install the selected ASR extra and platform audio dependencies; Linux needs PortAudio headers and macOS has a PortAudio setup step.
3. Run the supplied guarded microphone example or feed a 16 kHz mono PCM stream.

```sh
pip install "RealtimeSTT[faster-whisper]"
```

### First project

Begin with a small, permitted sample and inspect the result. [Source 1](https://github.com/KoljaB/RealtimeSTT/blob/master/README.md)

1. Create an AudioToTextRecorder in a script protected by the __main__ guard.
2. Capture one utterance with text(), then connect its transcription callback to your artwork or caption display.
3. Use external-audio mode for files or streaming sources rather than opening a microphone.
### Hardware & software

Published requirements and explicit documentation gaps follow. [Source 1](https://github.com/KoljaB/RealtimeSTT/blob/master/README.md) [Source 2](https://github.com/KoljaB/RealtimeSTT/blob/master/docs/installation.md)

- **Hardware:** CPU and NVIDIA CUDA paths are documented; a microphone is needed only for microphone capture. Minimum RAM, VRAM and model storage depend on the engine and are not universally documented.
- **Software:** Python 3.11/3.12; faster-whisper or another selected engine, VAD models and audio dependencies. Python 3.13+ is not currently a release target.
- **Platforms:** Installation instructions cover Linux, Windows multiprocessing and macOS PortAudio. The recommended production CPU streaming profile is specifically Linux x86_64.

### License, model weights & costs

The complete top-level MIT software terms were reviewed and archived today; model/dependency/host terms remain separate. [Source 1](https://github.com/KoljaB/RealtimeSTT/blob/master/LICENSE) [Source 2](https://github.com/KoljaB/RealtimeSTT/blob/master/README.md) [Source 3](https://github.com/KoljaB/RealtimeSTT/blob/master/docs/licenses.md)

- **Code:** MIT
- **Weights:** MIT covers RealtimeSTT. Engine/model terms vary; the project provides a license matrix. Whisper-based paths and optional provider-licensed Porcupine must be treated separately.
- **Commercial:** The main MIT code grant permits commercial use under its notice/source and other conditions. Model, component, asset and hosted-service permission is separate. MIT covers RealtimeSTT. Engine/model terms vary; the project provides a license matrix. Whisper-based paths and optional provider-licensed Porcupine must be treated separately.
- **Cost:** Local ASR is possible without a paid speech API. Optional provider engines, wake-word services and deployment hardware may add costs.

### Why it merits attention

Assessment: explicit engine choices, external audio input and event callbacks are useful building blocks for accessible live media. Recognition accuracy and response time were not tested here. [Source 1](https://github.com/KoljaB/RealtimeSTT/blob/master/README.md)

### Limitations

Realtime partial transcripts can change before finalization. Wake-word and microphone performance need venue-specific testing; browser examples do not make every server deployment production-ready. [Source 1](https://github.com/KoljaB/RealtimeSTT/blob/master/README.md) [Source 2](https://github.com/KoljaB/RealtimeSTT/blob/master/LICENSE) [Source 3](https://github.com/KoljaB/RealtimeSTT/blob/master/docs/licenses.md)

### Get the tool

- [Repository](https://github.com/KoljaB/RealtimeSTT)
- [Documentation](https://github.com/KoljaB/RealtimeSTT/blob/master/README.md)

## RealtimeTTS

Audio, music & voice · Interactive, immersive & live media · Avatars, digital humans & lip sync · Physical, robotic & kinetic installations

First complete guide for a previously screened discovery; documentation checked today. Repository created 2023-08-26; current source metadata is a discovery signal, not evidence of a significant product upgrade.

### How it uses AI

The framework connects text to learned speech-synthesis engines for live narration or voice characters. [Source](https://github.com/KoljaB/RealtimeTTS/blob/master/README.md)

### Introduction

A streaming text-to-speech framework with selectable local and hosted engines and a current Qwen server path. [Source 1](https://github.com/KoljaB/RealtimeTTS/blob/master/README.md)

### What it is good for

Give an interactive character or installation an incremental spoken response, or prototype narration streamed as text arrives. [Source 1](https://github.com/KoljaB/RealtimeTTS/blob/master/README.md)

### Demo & examples

The README supplies Qwen server quickstarts and API usage; local playback and a headless server are different deployment modes. [Source 1](https://github.com/KoljaB/RealtimeTTS/blob/master/README.md)

### Install

Documentation-based setup route; commands are examples from the project and were not executed during this review. [Source 1](https://github.com/KoljaB/RealtimeTTS/blob/master/README.md)

1. Choose Python 3.11 or 3.12 and a Qwen GPU or CPU server extra.
2. Install the chosen extra and download its model under the model terms.
3. Start the server, then connect a client to its OpenAI-compatible speech endpoint.

```sh
python -m pip install "realtimetts[qwen-server]"
```


```sh
realtimetts-qwen-server --device gpu --clone-mode speaker_only --demo-voice
```

### First project

Begin with a small, permitted sample and inspect the result. [Source 1](https://github.com/KoljaB/RealtimeTTS/blob/master/README.md)

1. Test a short non-streaming speech request first.
2. Connect incremental text to a supported engine and inspect buffering and cancellation behavior.
3. For playback, install the platform audio libraries; a headless server can return audio without an audio device.
### Hardware & software

Published requirements and explicit documentation gaps follow. [Source 1](https://github.com/KoljaB/RealtimeTTS/blob/master/README.md)

- **Hardware:** The GPU server needs an NVIDIA driver. CPU packages require the documented CPU architecture/instructions. Minimum RAM, VRAM and storage are model-specific and not provided as one universal floor.
- **Software:** Python 3.11/3.12. Qwen server extras do not require a local Torch/CUDA toolkit or PortAudio install; local audio playback has additional dependencies.
- **Platforms:** Documented CPU wheels: Windows x86_64; Linux x86_64 glibc >=2.35; Intel macOS >=13; Apple Silicon macOS >=11. Linux ARM, Windows ARM64 and Metal are outside that server release.

### License, model weights & costs

The complete top-level MIT software terms were reviewed and archived today; model/dependency/host terms remain separate. [Source 1](https://github.com/KoljaB/RealtimeTTS/blob/master/LICENSE) [Source 2](https://github.com/KoljaB/RealtimeTTS/blob/master/README.md)

- **Code:** MIT
- **Weights:** The library is MIT; neural checkpoint, engine and cloud-provider terms remain separate. The system TTS smoke test is not itself an open-source neural model.
- **Commercial:** The main MIT code grant permits commercial use under its notice/source and other conditions. Model, component, asset and hosted-service permission is separate. The library is MIT; neural checkpoint, engine and cloud-provider terms remain separate. The system TTS smoke test is not itself an open-source neural model.
- **Cost:** Local server modes do not mandate a paid speech API. Hosted engines and their accounts are optional separate costs.

### Why it merits attention

Assessment: headless and playback separation plus explicit CPU wheel compatibility is unusually actionable documentation. Server benchmarks are author reports, not our measurements. [Source 1](https://github.com/KoljaB/RealtimeTTS/blob/master/README.md)

### Limitations

A supported CPU wheel does not imply real-time speed on that CPU. Voice cloning and any third-party cloud engine need their own asset rights and service review. [Source 1](https://github.com/KoljaB/RealtimeTTS/blob/master/README.md) [Source 2](https://github.com/KoljaB/RealtimeTTS/blob/master/LICENSE)

### Get the tool

- [Repository](https://github.com/KoljaB/RealtimeTTS)
- [Documentation](https://github.com/KoljaB/RealtimeTTS/blob/master/README.md)

## stable-audio-tools

Audio, music & voice · Computational art & creative coding · Performance, projection & stage media

First complete guide for a previously screened discovery; documentation checked today. Repository created 2023-05-23; current source metadata is a discovery signal, not evidence of a significant product upgrade.

### How it uses AI

Diffusion and audio autoencoder tools support text-conditioned sound/music experimentation and model inference/training. [Source](https://github.com/Stability-AI/stable-audio-tools/blob/main/README.md)

### Introduction

Training and inference software for neural audio generators, with configurable models and a Gradio listening interface. [Source 1](https://github.com/Stability-AI/stable-audio-tools/blob/main/README.md)

### What it is good for

Prototype ambience, sound design and generative audio studies, or fine-tune a model using audio you are entitled to train on. [Source 1](https://github.com/Stability-AI/stable-audio-tools/blob/main/README.md)

### Demo & examples

run_gradio.py provides a local text-to-audio demo for a selected pretrained model or your own unwrapped checkpoint. [Source 1](https://github.com/Stability-AI/stable-audio-tools/blob/main/README.md)

### Install

Documentation-based setup route; commands are examples from the project and were not executed during this review. [Source 1](https://github.com/Stability-AI/stable-audio-tools/blob/main/README.md)

1. Clone the repository and use the documented uv environment.
2. Enable the UI dependency group and choose a checkpoint whose terms you accept.
3. Launch run_gradio.py for that model; training is a separate installation/configuration path.

```sh
uv sync --extra ui
```


```sh
uv run python run_gradio.py --pretrained-name stabilityai/stable-audio-open-1.0
```

### First project

Begin with a small, permitted sample and inspect the result. [Source 1](https://github.com/Stability-AI/stable-audio-tools/blob/main/README.md)

1. Enter a short sound prompt and generate a listening comparison.
2. Adjust model-specific duration and sampling controls, then export the useful result.
3. For a custom trained checkpoint, unwrap the training wrapper before using inference scripts.
### Hardware & software

Published requirements and explicit documentation gaps follow. [Source 1](https://github.com/Stability-AI/stable-audio-tools/blob/main/README.md)

- **Hardware:** Memory and storage depend on the model and audio duration; the README does not publish a universal RAM/VRAM floor. Training supports multi-GPU/multi-node configurations.
- **Software:** PyTorch >=2.5; development uses Python 3.10. uv manages dependencies; FlashAttention is recommended for performance. The documented training logger uses a Weights & Biases account.
- **Platforms:** The inspected quickstart does not provide a complete native Linux/Windows/macOS support matrix. Confirm the selected model and attention backend before provisioning a host.

### License, model weights & costs

The complete top-level MIT software terms were reviewed and archived today; model/dependency/host terms remain separate. [Source 1](https://github.com/Stability-AI/stable-audio-tools/blob/main/LICENSE) [Source 2](https://github.com/Stability-AI/stable-audio-tools/blob/main/README.md) [Source 3](https://huggingface.co/stabilityai/stable-audio-open-1.0)

- **Code:** MIT
- **Weights:** MIT applies to this code. Stable Audio Open requires accepting separate model terms on Hugging Face; its gated raw model card returned 401 during this review, so current commercial weight permissions are not verified.
- **Commercial:** The main MIT code grant permits commercial use under its notice/source and other conditions. Model, component, asset and hosted-service permission is separate. MIT applies to this code. Stable Audio Open requires accepting separate model terms on Hugging Face; its gated raw model card returned 401 during this review, so current commercial weight permissions are not verified.
- **Cost:** Code has no license fee; local/rented compute, optional logging services and any separately licensed checkpoints may cost money.

### Why it merits attention

Assessment: model/dataset configuration and checkpoint unwrapping make the tool relevant beyond a prompt-only demo. Audio quality and installation were not tested. [Source 1](https://github.com/Stability-AI/stable-audio-tools/blob/main/README.md)

### Limitations

Do not treat MIT code as a license for every Stability checkpoint. Training requires a prepared dataset/config and substantially different resources from inference. [Source 1](https://github.com/Stability-AI/stable-audio-tools/blob/main/README.md) [Source 2](https://github.com/Stability-AI/stable-audio-tools/blob/main/LICENSE) [Source 3](https://huggingface.co/stabilityai/stable-audio-open-1.0)

### Get the tool

- [Repository](https://github.com/Stability-AI/stable-audio-tools)
- [Documentation](https://github.com/Stability-AI/stable-audio-tools/blob/main/README.md)

## Bark

Audio, music & voice · Storyboarding, narrative & comics · Games & production pipelines

First complete guide for a previously screened discovery; documentation checked today. Repository created 2023-04-07; current source metadata is a discovery signal, not evidence of a significant product upgrade.

### How it uses AI

Its generative audio models turn text into speech and other audio useful for experimental narration and voice-character sketches. [Source](https://github.com/suno-ai/bark/blob/main/README.md)

### Introduction

A generative text-to-audio model that can produce speech and some non-speech vocal sounds, rather than strictly reading every input word. [Source 1](https://github.com/suno-ai/bark/blob/main/README.md)

### What it is good for

Sketch expressive fictional dialogue, laughter or unusual voice textures for a game or short narrative; edit the result before publication. [Source 1](https://github.com/suno-ai/bark/blob/main/README.md)

### Demo & examples

The README links audio samples and notebooks and provides a one-line CLI that writes a WAV file. [Source 1](https://github.com/suno-ai/bark/blob/main/README.md)

### Install

Documentation-based setup route; commands are examples from the project and were not executed during this review. [Source 1](https://github.com/suno-ai/bark/blob/main/README.md)

1. Use the official GitHub package; the README warns that the PyPI package named bark is unrelated.
2. Install into an isolated environment and allow the documented model download.
3. Run the CLI or Python example, starting with a short prompt.

```sh
pip install git+https://github.com/suno-ai/bark.git
```


```sh
python -m bark --text "Hello, my name is Suno." --output_filename example.wav
```

### First project

Begin with a small, permitted sample and inspect the result. [Source 1](https://github.com/suno-ai/bark/blob/main/README.md)

1. Generate one short phrase with a preset voice.
2. Try a documented non-speech marker such as [laughter] and listen for whether it follows the script.
3. Save the WAV and assemble longer narration as edited segments.
### Hardware & software

Published requirements and explicit documentation gaps follow. [Source 1](https://github.com/suno-ai/bark/blob/main/README.md)

- **Hardware:** The authors document roughly 12 GB VRAM for all full models resident on GPU and an 8 GB small-model option; further offload settings can work on smaller cards. CPU inference is supported but slower. RAM/storage minima are not stated.
- **Software:** PyTorch >=2.0; the README reports CUDA 11.7/12.0 testing. Checkpoint downloads and optional Transformers integration are separate from the basic package.
- **Platforms:** CPU and GPU inference are documented, but the README does not certify every native operating system or Apple Silicon acceleration path.

### License, model weights & costs

The complete top-level MIT software terms were reviewed and archived today; model/dependency/host terms remain separate. [Source 1](https://github.com/suno-ai/bark/blob/main/LICENSE) [Source 2](https://github.com/suno-ai/bark/blob/main/README.md)

- **Code:** MIT
- **Weights:** The README and software license identify MIT and explicitly describe commercial availability. Dependent codec/library and any substituted weights retain their own terms.
- **Commercial:** The main MIT code grant permits commercial use under its notice/source and other conditions. Model, component, asset and hosted-service permission is separate. The README and software license identify MIT and explicitly describe commercial availability. Dependent codec/library and any substituted weights retain their own terms.
- **Cost:** No mandatory paid API for the local release; compute and downloaded model storage are the main local costs. Suno hosted products are separate.

### Why it merits attention

Assessment: published samples, short CLI output and explicit memory/offload guidance support experimentation. Generative variability is part of its appeal and a production constraint. [Source 1](https://github.com/suno-ai/bark/blob/main/README.md)

### Limitations

Outputs may deviate from the script. The FAQ describes a roughly 13–14 second generation window, so long-form speech needs additional assembly. No hands-on audio evaluation was done. [Source 1](https://github.com/suno-ai/bark/blob/main/README.md) [Source 2](https://github.com/suno-ai/bark/blob/main/LICENSE)

### Get the tool

- [Repository](https://github.com/suno-ai/bark)
- [Documentation](https://github.com/suno-ai/bark/blob/main/README.md)

## gsplat

3D, reconstruction & assets · Photogrammetry, scanning & neural rendering · Spatial audio & volumetric media · Computational art & creative coding

First complete guide for a previously screened discovery; documentation checked today. Repository created 2023-08-25; current source metadata is a discovery signal, not evidence of a significant product upgrade.

### How it uses AI

Differentiable Gaussian-splat training/rendering learns a scene representation from observations for novel-view creative work. [Source](https://github.com/nerfstudio-project/gsplat/blob/main/README.md)

### Introduction

A differentiable Gaussian-splat rasterization and optimization library with CUDA kernels and Python bindings. [Source 1](https://github.com/nerfstudio-project/gsplat/blob/main/README.md)

### What it is good for

Learn a neural scene representation from a COLMAP capture, fit an image with Gaussians or build a renderer for captured environments. [Source 1](https://github.com/nerfstudio-project/gsplat/blob/main/README.md)

### Demo & examples

The official examples cover COLMAP training, fitting a 2D image and rendering large scenes; these are developer examples rather than an end-user scan app. [Source 1](https://github.com/nerfstudio-project/gsplat/blob/main/README.md)

### Install

Documentation-based setup route; commands are examples from the project and were not executed during this review. [Source 1](https://github.com/nerfstudio-project/gsplat/blob/main/README.md)

1. Install a compatible PyTorch/CUDA environment and choose a release or current source.
2. Install gsplat; the PyPI route compiles CUDA kernels on first use.
3. Install the example dependencies and follow the COLMAP example for a small licensed capture.

```sh
pip install gsplat
```


```sh
pip install -r examples/requirements.txt --no-build-isolation
```

### First project

Begin with a small, permitted sample and inspect the result. [Source 1](https://github.com/nerfstudio-project/gsplat/blob/main/README.md)

1. Prepare images and calibrated camera poses using the documented capture example.
2. Train the Gaussian representation and inspect reconstruction errors.
3. Render a held-out view or load the generated scene in a compatible renderer.
### Hardware & software

Published requirements and explicit documentation gaps follow. [Source 1](https://github.com/nerfstudio-project/gsplat/blob/main/README.md)

- **Hardware:** A CUDA-capable NVIDIA GPU is needed for the documented acceleration paths. Scene size controls memory use; minimum RAM, VRAM and storage are not specified globally.
- **Software:** Current main requires PyTorch >=2.7 and describes CUDA 12.8/13.2 build compatibility. The README labels v1.6.0 work as not yet on PyPI: do not assume pip installs those changes.
- **Platforms:** Linux/Windows wheels exist for selected Python/PyTorch/CUDA combinations; Windows source-build instructions are linked. macOS Metal and mobile support are not documented for this CUDA library.

### License, model weights & costs

The complete top-level Apache-2.0 software terms were reviewed and archived today; model/dependency/host terms remain separate. [Source 1](https://github.com/nerfstudio-project/gsplat/blob/main/LICENSE) [Source 2](https://github.com/nerfstudio-project/gsplat/blob/main/README.md)

- **Code:** Apache-2.0
- **Weights:** Apache-2.0 covers the library. Capture datasets, imported splats and example dependencies have separate licenses; training a scene does not grant rights to its source imagery.
- **Commercial:** The main Apache-2.0 code grant permits commercial use under its notice/source and other conditions. Model, component, asset and hosted-service permission is separate. Apache-2.0 covers the library. Capture datasets, imported splats and example dependencies have separate licenses; training a scene does not grant rights to its source imagery.
- **Cost:** Local compute and optional capture tooling costs; no paid hosted renderer is required by the examples.

### Why it merits attention

Assessment: differentiable kernels and reproducible capture examples are useful infrastructure for neural media. Published speed/memory claims are author comparisons, not measurements from this review. [Source 1](https://github.com/nerfstudio-project/gsplat/blob/main/README.md)

### Limitations

This is a programmer-facing component. A splat is not automatically a watertight mesh or a 3D-printable object; XR display needs another validated application. [Source 1](https://github.com/nerfstudio-project/gsplat/blob/main/README.md) [Source 2](https://github.com/nerfstudio-project/gsplat/blob/main/LICENSE)

### Get the tool

- [Repository](https://github.com/nerfstudio-project/gsplat)
- [Documentation](https://github.com/nerfstudio-project/gsplat/blob/main/README.md)

## ComfyUI-3D-Pack

3D, reconstruction & assets · Games & production pipelines · Computational art & creative coding

First complete guide for a previously screened discovery; documentation checked today. Repository created 2024-01-05; current source metadata is a discovery signal, not evidence of a significant product upgrade.

### How it uses AI

ComfyUI nodes orchestrate neural 3D generation, reconstruction and related model workflows for creative assets. [Source](https://github.com/MrForExample/ComfyUI-3D-Pack/blob/main/README.md)

### Introduction

A ComfyUI node suite combining learned multi-view generation, reconstruction, Gaussian splats, NeRFs and mesh/texture utilities. [Source 1](https://github.com/MrForExample/ComfyUI-3D-Pack/blob/main/README.md)

### What it is good for

Assemble a visual image-to-3D asset workflow and compare InstantMesh, TripoSR or other supported models in the same node environment. [Source 1](https://github.com/MrForExample/ComfyUI-3D-Pack/blob/main/README.md)

### Demo & examples

The README embeds model-specific workflows and output clips; start with the workflow for one model rather than the entire feature set. [Source 1](https://github.com/MrForExample/ComfyUI-3D-Pack/blob/main/README.md)

### Install

Documentation-based setup route; commands are examples from the project and were not executed during this review. [Source 1](https://github.com/MrForExample/ComfyUI-3D-Pack/blob/main/README.md)

1. Set up a working ComfyUI environment first.
2. Install the pack through ComfyUI-Manager or its documented manual custom_nodes path.
3. Check the prebuild/runtime matrix and install only the model assets needed by the example.
### First project

Begin with a small, permitted sample and inspect the result. [Source 1](https://github.com/MrForExample/ComfyUI-3D-Pack/blob/main/README.md)

1. Import one documented reconstruction workflow and provide a clear object image.
2. Run its view-generation and mesh stages, splitting stages if memory is tight.
3. Inspect/export the mesh and texture; repair topology before production or fabrication.
### Hardware & software

Published requirements and explicit documentation gaps follow. [Source 1](https://github.com/MrForExample/ComfyUI-3D-Pack/blob/main/README.md)

- **Hardware:** Model-specific requirements vary. Era3D is explicitly documented as needing at least 16 GB VRAM; that figure is not a minimum for every node. Universal RAM/storage minima are not stated.
- **Software:** Published prebuilds target Python 3.12, CUDA 12.4 and torch 2.5.1+cu124. Some nodes need Windows Visual Studio Build Tools or Linux gcc/g++.
- **Platforms:** Windows 10/11 prebuilds are documented; Linux builds need compatible native toolchains. This review does not establish native macOS support for the suite.

### License, model weights & costs

The complete top-level MIT software terms were reviewed and archived today; model/dependency/host terms remain separate. [Source 1](https://github.com/MrForExample/ComfyUI-3D-Pack/blob/main/LICENSE) [Source 2](https://github.com/MrForExample/ComfyUI-3D-Pack/blob/main/README.md)

- **Code:** MIT
- **Weights:** MIT covers this node pack. Downloaded models keep separate licenses; the README flags gated Stability model terms. A node being available does not make its weights unrestricted.
- **Commercial:** The main MIT code grant permits commercial use under its notice/source and other conditions. Model, component, asset and hosted-service permission is separate. MIT covers this node pack. Downloaded models keep separate licenses; the README flags gated Stability model terms. A node being available does not make its weights unrestricted.
- **Cost:** The local route requires suitable compute and model storage; any optional hosted or provider model has its own costs.

### Why it merits attention

Assessment: reusable visual nodes expose several reconstruction methods without writing a new pipeline for each. No workflow was executed during this documentation review. [Source 1](https://github.com/MrForExample/ComfyUI-3D-Pack/blob/main/README.md)

### Limitations

Large native dependency surface and model version compatibility can complicate setup. Exported geometry still needs scale, topology and material checks. [Source 1](https://github.com/MrForExample/ComfyUI-3D-Pack/blob/main/README.md) [Source 2](https://github.com/MrForExample/ComfyUI-3D-Pack/blob/main/LICENSE)

### Get the tool

- [Repository](https://github.com/MrForExample/ComfyUI-3D-Pack)
- [Documentation](https://github.com/MrForExample/ComfyUI-3D-Pack/blob/main/README.md)

## TRELLIS — first generation

3D, reconstruction & assets · Games & production pipelines · Spatial audio & volumetric media

First complete guide for a previously screened discovery; documentation checked today. Repository created 2024-12-02; current source metadata is a discovery signal, not evidence of a significant product upgrade.

### How it uses AI

Structured-latent 3D generation uses image conditioning to produce experimental neural/mesh assets; renderer terms are separate. [Source](https://github.com/microsoft/TRELLIS/blob/main/README.md)

### Introduction

A structured-latent generative 3D model producing meshes, radiance fields and Gaussian representations from images or text. [Source 1](https://github.com/microsoft/TRELLIS/blob/main/README.md)

### What it is good for

Explore variations of a concept image and export a draft game or spatial-scene asset in GLB or Gaussian PLY form. [Source 1](https://github.com/microsoft/TRELLIS/blob/main/README.md)

### Demo & examples

The repository supplies image-to-3D examples and a Gradio app; this profile covers the original TRELLIS, separately from TRELLIS.2 already in the library. [Source 1](https://github.com/microsoft/TRELLIS/blob/main/README.md)

### Install

Documentation-based setup route; commands are examples from the project and were not executed during this review. [Source 1](https://github.com/microsoft/TRELLIS/blob/main/README.md)

1. Use the documented Linux/NVIDIA environment and clone with submodules.
2. Review the setup flags and all renderer/component licenses before installing the required dependencies.
3. Download the selected checkpoint and follow the image-conditioned example or app.py.

```sh
python app.py
```

### First project

Begin with a small, permitted sample and inspect the result. [Source 1](https://github.com/microsoft/TRELLIS/blob/main/README.md)

1. Choose the image-conditioned pipeline and supply an object image.
2. Generate the mesh, Gaussian or radiance-field representation.
3. Render multiple views and export GLB/PLY; edit defects in a 3D application.
### Hardware & software

Published requirements and explicit documentation gaps follow. [Source 1](https://github.com/microsoft/TRELLIS/blob/main/README.md)

- **Hardware:** The README requires an NVIDIA GPU with at least 16 GB memory and reports A100/A6000 verification. Minimum system RAM and total storage are not documented.
- **Software:** Python >=3.8; CUDA toolkit tested at 11.8/12.2. The default setup environment uses PyTorch 2.4.0/CUDA 11.8 and compiles native submodules.
- **Platforms:** Tested only on Linux by the authors. Windows guidance is linked but explicitly not fully tested; macOS/MPS support is not established.

### License, model weights & costs

The complete top-level MIT software terms were reviewed and archived today; model/dependency/host terms remain separate. [Source 1](https://github.com/microsoft/TRELLIS/blob/main/LICENSE) [Source 2](https://github.com/microsoft/TRELLIS/blob/main/README.md) [Source 3](https://github.com/JeffreyXiang/diffoctreerast/blob/master/LICENSE) [Source 4](https://github.com/nv-tlabs/FlexiCubes/blob/main/LICENSE.txt)

- **Code:** MIT
- **Weights:** The README identifies MIT for the models and most code. diffoctreerast and modified FlexiCubes carry separate licenses; the default dependency stack is not covered solely by the top-level MIT license. The separately reviewed diffoctreerast renderer is limited to non-commercial research/evaluation and is not an open-source component; FlexiCubes is Apache-2.0.
- **Commercial:** The main MIT code grant permits commercial use under its notice/source and other conditions. Model, component, asset and hosted-service permission is separate. The README identifies MIT for the models and most code. diffoctreerast and modified FlexiCubes carry separate licenses; the default dependency stack is not covered solely by the top-level MIT license. The separately reviewed diffoctreerast renderer is limited to non-commercial research/evaluation and is not an open-source component; FlexiCubes is Apache-2.0.
- **Cost:** Local inference needs substantial GPU compute; no paid hosted generator is mandatory. Component permissions must be resolved for commercial use.

### Why it merits attention

Assessment: explicit output formats and a documented image-first pipeline make it useful for 3D asset experiments. No generated asset or hardware claim was validated hands-on. [Source 1](https://github.com/microsoft/TRELLIS/blob/main/README.md)

### Limitations

Generated meshes may need remeshing, rigging and texture cleanup. Separate renderer terms may constrain a commercial deployment; do not infer printing readiness from GLB export. The default renderer dependency prevents describing the whole bundled stack as unrestricted open source. [Source 1](https://github.com/microsoft/TRELLIS/blob/main/README.md) [Source 2](https://github.com/microsoft/TRELLIS/blob/main/LICENSE) [Source 3](https://github.com/JeffreyXiang/diffoctreerast/blob/master/LICENSE) [Source 4](https://github.com/nv-tlabs/FlexiCubes/blob/main/LICENSE.txt)

### Get the tool

- [Repository](https://github.com/microsoft/TRELLIS)
- [Documentation](https://github.com/microsoft/TRELLIS/blob/main/README.md)

## InstantMesh

3D, reconstruction & assets · Games & production pipelines · 3D printing & generative CAD

First complete guide for a previously screened discovery; documentation checked today. Repository created 2024-04-10; current source metadata is a discovery signal, not evidence of a significant product upgrade.

### How it uses AI

A learned image-to-3D reconstruction pipeline creates multiview-derived object geometry for further creative cleanup. [Source](https://github.com/TencentARC/InstantMesh/blob/main/README.md)

### Introduction

An image-to-mesh research pipeline using generated sparse views and a large reconstruction model. [Source 1](https://github.com/TencentARC/InstantMesh/blob/main/README.md)

### What it is good for

Turn a clean product/concept image into an initial mesh and texture for later artist cleanup or shape exploration. [Source 1](https://github.com/TencentARC/InstantMesh/blob/main/README.md)

### Demo & examples

The authors provide a Hugging Face Space and a local Gradio app; the CLI can save a turntable and export a texture map. [Source 1](https://github.com/TencentARC/InstantMesh/blob/main/README.md) [Source 2](https://huggingface.co/spaces/TencentARC/InstantMesh)

### Install

Documentation-based setup route; commands are examples from the project and were not executed during this review. [Source 1](https://github.com/TencentARC/InstantMesh/blob/main/README.md)

1. Create the documented Python/CUDA environment, including Ninja and the matching xformers version.
2. Install requirements.txt and allow the selected reconstruction and Zero123++ assets to download.
3. Start app.py or use the documented run.py configuration.

```sh
pip install -r requirements.txt
```


```sh
python app.py
```

### First project

Begin with a small, permitted sample and inspect the result. [Source 1](https://github.com/TencentARC/InstantMesh/blob/main/README.md)

1. Supply a clear single-object image, using background removal only when appropriate.
2. Generate sparse views and a mesh; compare the turntable against the input.
3. Export the texture map when needed and repair unseen surfaces and topology.
### Hardware & software

Published requirements and explicit documentation gaps follow. [Source 1](https://github.com/TencentARC/InstantMesh/blob/main/README.md)

- **Hardware:** CUDA-backed inference is documented. The demo can distribute work over two GPUs or force one GPU; hard RAM/VRAM/storage minima are not published in the README.
- **Software:** Recommended Python >=3.10, PyTorch >=2.1.0 and CUDA >=12.1. The example pins torch 2.1.0/xformers 0.0.22.post7; use compatible versions.
- **Platforms:** A local CUDA stack and Docker recipe are documented. Native macOS/MPS support is not shown; Windows support is not guaranteed by a browser demo.

### License, model weights & costs

The complete top-level Apache-2.0 software terms were reviewed and archived today; model/dependency/host terms remain separate. [Source 1](https://github.com/TencentARC/InstantMesh/blob/main/LICENSE) [Source 2](https://github.com/TencentARC/InstantMesh/blob/main/README.md) [Source 3](https://huggingface.co/TencentARC/InstantMesh)

- **Code:** Apache-2.0
- **Weights:** Apache-2.0 code; the InstantMesh model card also lists Apache-2.0. The customized Zero123++ and any added dependencies/checkpoints must retain their own terms.
- **Commercial:** The main Apache-2.0 code grant permits commercial use under its notice/source and other conditions. Model, component, asset and hosted-service permission is separate. Apache-2.0 code; the InstantMesh model card also lists Apache-2.0. The customized Zero123++ and any added dependencies/checkpoints must retain their own terms.
- **Cost:** Local GPU and storage costs; a hosted demo may have availability/queue limits rather than guaranteeing free unlimited service.

### Why it merits attention

Assessment: an explicit textured-mesh export and reproducible local demo are useful starting points for asset work. This is documentation review, not an output-quality test. [Source 1](https://github.com/TencentARC/InstantMesh/blob/main/README.md)

### Limitations

A single image cannot document every surface. Generated meshes are not certified manifold, dimensionally accurate or ready for printing. [Source 1](https://github.com/TencentARC/InstantMesh/blob/main/README.md) [Source 2](https://github.com/TencentARC/InstantMesh/blob/main/LICENSE) [Source 3](https://huggingface.co/TencentARC/InstantMesh)

### Get the tool

- [Repository](https://github.com/TencentARC/InstantMesh)
- [Documentation](https://github.com/TencentARC/InstantMesh/blob/main/README.md)
- [Demo](https://huggingface.co/spaces/TencentARC/InstantMesh)

## TripoSG

3D, reconstruction & assets · Games & production pipelines · 3D printing & generative CAD

First complete guide for a previously screened discovery; documentation checked today. Repository created 2025-03-24; current source metadata is a discovery signal, not evidence of a significant product upgrade.

### How it uses AI

A rectified-flow 3D model generates candidate object geometry from images and supported guidance workflows. [Source](https://github.com/VAST-AI-Research/TripoSG/blob/main/README.md)

### Introduction

An image-to-3D rectified-flow model, with a separate scribble-and-prompt variant for shape exploration. [Source 1](https://github.com/VAST-AI-Research/TripoSG/blob/main/README.md)

### What it is good for

Generate concept geometry from an illustration or rough sketch, then edit it for a game asset or fabrication study. [Source 1](https://github.com/VAST-AI-Research/TripoSG/blob/main/README.md)

### Demo & examples

The repository links its image and scribble demos and documents GLB export and a target-face-count option. [Source 1](https://github.com/VAST-AI-Research/TripoSG/blob/main/README.md) [Source 2](https://huggingface.co/spaces/VAST-AI/TripoSG-scribble)

### Install

Documentation-based setup route; commands are examples from the project and were not executed during this review. [Source 1](https://github.com/VAST-AI-Research/TripoSG/blob/main/README.md)

1. Create the example Python 3.10 environment and install PyTorch matching your CUDA setup.
2. Install requirements.txt and place the documented TripoSG/RMBG checkpoints in their expected directories.
3. Follow the image inference command or the separate scribble configuration.

```sh
pip install -r requirements.txt
```


```sh
python -m scripts.inference_triposg --image-input assets/example_data/hjswed.png --output-path output.glb
```

### First project

Begin with a small, permitted sample and inspect the result. [Source 1](https://github.com/VAST-AI-Research/TripoSG/blob/main/README.md)

1. Start with a clear object image or the supplied example.
2. Generate a GLB and optionally set the target face count for a simpler asset.
3. Inspect thin structures, scale and topology in a modeling package before downstream use.
### Hardware & software

Published requirements and explicit documentation gaps follow. [Source 1](https://github.com/VAST-AI-Research/TripoSG/blob/main/README.md)

- **Hardware:** The README specifies a CUDA GPU with at least 8 GB VRAM. System RAM and total model/storage minimum are not documented.
- **Software:** Python 3.10 example; compatible PyTorch/CUDA and requirements.txt. The full VAE encoder additionally needs torch-cluster.
- **Platforms:** The local documented path is CUDA-based. Native Apple Silicon/MPS and mobile generation are not established; a hosted browser demo is a separate access route.

### License, model weights & costs

The complete top-level MIT software terms were reviewed and archived today; model/dependency/host terms remain separate. [Source 1](https://github.com/VAST-AI-Research/TripoSG/blob/main/LICENSE) [Source 2](https://github.com/VAST-AI-Research/TripoSG/blob/main/README.md) [Source 3](https://huggingface.co/VAST-AI/TripoSG)

- **Code:** MIT
- **Weights:** MIT code and a MIT-tagged TripoSG model card. The documented RMBG-1.4 dependency has separate terms; do not extend MIT to the background-removal model.
- **Commercial:** The main MIT code grant permits commercial use under its notice/source and other conditions. Model, component, asset and hosted-service permission is separate. MIT code and a MIT-tagged TripoSG model card. The documented RMBG-1.4 dependency has separate terms; do not extend MIT to the background-removal model.
- **Cost:** Compute/model storage costs for local use; hosted demo capacity is not guaranteed. Commercial use of every dependency is not established by the main license.

### Why it merits attention

Assessment: a stated VRAM floor, a direct GLB route and face-count control make practical exploration approachable. No mesh was generated in this review. [Source 1](https://github.com/VAST-AI-Research/TripoSG/blob/main/README.md)

### Limitations

The model focuses on shape synthesis; asset readiness and printable topology require separate checks. The scribble checkpoint and dependencies need their own license review. [Source 1](https://github.com/VAST-AI-Research/TripoSG/blob/main/README.md) [Source 2](https://github.com/VAST-AI-Research/TripoSG/blob/main/LICENSE) [Source 3](https://huggingface.co/VAST-AI/TripoSG)

### Get the tool

- [Repository](https://github.com/VAST-AI-Research/TripoSG)
- [Documentation](https://github.com/VAST-AI-Research/TripoSG/blob/main/README.md)
- [Demo](https://huggingface.co/spaces/VAST-AI/TripoSG-scribble)

## DreamGaussian

3D, reconstruction & assets · Games & production pipelines · Computational art & creative coding

First complete guide for a previously screened discovery; documentation checked today. Repository created 2023-09-27; current source metadata is a discovery signal, not evidence of a significant product upgrade.

### How it uses AI

Diffusion-guided Gaussian optimization turns text or an image into an experimental 3D representation and mesh. [Source](https://github.com/dreamgaussian/dreamgaussian/blob/main/readme.md)

### Introduction

A diffusion-guided 3D optimization pipeline that fits Gaussians, extracts a coarse mesh and refines its texture. [Source 1](https://github.com/dreamgaussian/dreamgaussian/blob/main/readme.md)

### What it is good for

Study image/text-to-3D generation or make an experimental prop draft with a visible two-stage optimization process. [Source 1](https://github.com/dreamgaussian/dreamgaussian/blob/main/readme.md)

### Demo & examples

The official project page shows examples; the README has local GUI and Gradio routes plus community notebook links. [Source 1](https://github.com/dreamgaussian/dreamgaussian/blob/main/readme.md)

### Install

Documentation-based setup route; commands are examples from the project and were not executed during this review. [Source 1](https://github.com/dreamgaussian/dreamgaussian/blob/main/readme.md)

1. Choose one of the documented CUDA/PyTorch environments and clone the source.
2. Install requirements and the specified rasterization/nearest-neighbor components, reviewing their separate licenses.
3. Preprocess an image, run the Gaussian stage, then run mesh refinement.

```sh
python process.py data/name.jpg
```


```sh
python main.py --config configs/image.yaml input=data/name_rgba.png save_path=name
```


```sh
python main2.py --config configs/image.yaml input=data/name_rgba.png save_path=name
```

### First project

Begin with a small, permitted sample and inspect the result. [Source 1](https://github.com/dreamgaussian/dreamgaussian/blob/main/readme.md)

1. Recenter and remove the background of a permitted object image.
2. Fit Gaussians and inspect the coarse mesh before refinement.
3. Export OBJ or GLB and render several viewpoints to inspect artifacts.
### Hardware & software

Published requirements and explicit documentation gaps follow. [Source 1](https://github.com/dreamgaussian/dreamgaussian/blob/main/readme.md)

- **Hardware:** The documented tests use a V100 and an RTX 3070; these are tested devices, not universal memory minima. Minimum RAM, VRAM and total storage are not specified.
- **Software:** Published combinations: Ubuntu 22/torch 1.12/CUDA 11.6 and Windows 10/torch 2.1/CUDA 12.1. Custom rasterizers, nvdiffrast and model-specific dependencies are required.
- **Platforms:** The authors report Ubuntu and Windows testing. macOS/MPS and non-CUDA inference are not documented for the full pipeline.

### License, model weights & costs

The complete top-level MIT software terms were reviewed and archived today; model/dependency/host terms remain separate. [Source 1](https://github.com/dreamgaussian/dreamgaussian/blob/main/LICENSE) [Source 2](https://github.com/dreamgaussian/dreamgaussian/blob/main/readme.md)

- **Code:** MIT
- **Weights:** MIT covers the main repository. Diffusion checkpoints and the modified Gaussian rasterizer keep separate terms; commercial rights for the complete default stack are not verified.
- **Commercial:** The main MIT code grant permits commercial use under its notice/source and other conditions. Model, component, asset and hosted-service permission is separate. MIT covers the main repository. Diffusion checkpoints and the modified Gaussian rasterizer keep separate terms; commercial rights for the complete default stack are not verified.
- **Cost:** Local GPU compute and model downloads; hosted community notebooks are optional and may incur cloud costs.

### Why it merits attention

Assessment: inspectable intermediate Gaussians, mesh refinement and explicit tested environments are useful for learning reconstruction. No runtime or output quality was tested. [Source 1](https://github.com/dreamgaussian/dreamgaussian/blob/main/readme.md)

### Limitations

The project is a research pipeline with native-build friction. Generated shape/texture can be view-dependent or distorted; export does not establish a printable or production-ready object. [Source 1](https://github.com/dreamgaussian/dreamgaussian/blob/main/readme.md) [Source 2](https://github.com/dreamgaussian/dreamgaussian/blob/main/LICENSE)

### Get the tool

- [Repository](https://github.com/dreamgaussian/dreamgaussian)
- [Documentation](https://github.com/dreamgaussian/dreamgaussian/blob/main/readme.md)

## MoMask

Motion capture & character animation · Avatars, digital humans & lip sync · Games & production pipelines · Performance, projection & stage media

First complete guide for a previously screened discovery; documentation checked today. Repository created 2023-11-29; current source metadata is a discovery signal, not evidence of a significant product upgrade.

### How it uses AI

Masked motion-model generation translates text into 3D human motion for animation prototyping. [Source](https://github.com/EricGuo5513/momask-codes/blob/main/README.md)

### Introduction

A masked generative model converting text descriptions into 3D human motion, with temporal motion inpainting. [Source 1](https://github.com/EricGuo5513/momask-codes/blob/main/README.md)

### What it is good for

Prototype a character action or fill a motion segment, then retarget the generated skeleton to a separately licensed character rig. [Source 1](https://github.com/EricGuo5513/momask-codes/blob/main/README.md)

### Demo & examples

The project page and Hugging Face demo show motions. Local output includes joint arrays, stick-figure MP4 previews and BVH files. [Source 1](https://github.com/EricGuo5513/momask-codes/blob/main/README.md) [Source 2](https://ericguo5513.github.io/momask/)

### Install

Documentation-based setup route; commands are examples from the project and were not executed during this review. [Source 1](https://github.com/EricGuo5513/momask-codes/blob/main/README.md)

1. Clone the repository and use its conda environment or Python 3.10 pip alternative.
2. Download the specified model/evaluator assets and review their own terms.
3. Run gen_t2m.py with a short action prompt on the intended GPU.

```sh
pip install -r requirements.txt
```


```sh
python gen_t2m.py --gpu_id 0 --ext first_motion --text_prompt "A person is running on a treadmill."
```

### First project

Begin with a small, permitted sample and inspect the result. [Source 1](https://github.com/EricGuo5513/momask-codes/blob/main/README.md)

1. Generate a short action and inspect the stick-figure preview.
2. Load the BVH into a 3D tool and map it to your permitted target rig.
3. Fix foot contact and joint alignment before rendering or gameplay use.
### Hardware & software

Published requirements and explicit documentation gaps follow. [Source 1](https://github.com/EricGuo5513/momask-codes/blob/main/README.md)

- **Hardware:** The examples select a GPU, but no minimum VRAM, system RAM or total storage is published in the quickstart.
- **Software:** Original tests used Python 3.7.13/PyTorch 1.7.1; the pip alternative is tested with Python 3.10. Model/evaluation assets and optional Blender retargeting tools are additional dependencies.
- **Platforms:** GPU research scripts are documented; the README does not provide a complete native Linux/Windows/macOS certification matrix.

### License, model weights & costs

The complete top-level MIT software terms were reviewed and archived today; model/dependency/host terms remain separate. [Source 1](https://github.com/EricGuo5513/momask-codes/blob/main/LICENSE) [Source 2](https://github.com/EricGuo5513/momask-codes/blob/main/README.md)

- **Code:** MIT
- **Weights:** MIT code. Downloaded model, motion-dataset, evaluation and Mixamo/character asset terms are separate and not comprehensively resolved by the software license.
- **Commercial:** The main MIT code grant permits commercial use under its notice/source and other conditions. Model, component, asset and hosted-service permission is separate. MIT code. Downloaded model, motion-dataset, evaluation and Mixamo/character asset terms are separate and not comprehensively resolved by the software license.
- **Cost:** Compute and optional character/animation software costs. Blender can be used for the documented manual rendering workflow; a proprietary character source is optional.

### Why it merits attention

Assessment: BVH export and temporal editing make it relevant to animation rather than only a paper visualization. No motion or retargeting was tested here. [Source 1](https://github.com/EricGuo5513/momask-codes/blob/main/README.md)

### Limitations

The authors note that their simple foot IK can fail and retargeting can introduce errors. It does not automatically generate a finished, rigged character. [Source 1](https://github.com/EricGuo5513/momask-codes/blob/main/README.md) [Source 2](https://github.com/EricGuo5513/momask-codes/blob/main/LICENSE)

### Get the tool

- [Repository](https://github.com/EricGuo5513/momask-codes)
- [Documentation](https://github.com/EricGuo5513/momask-codes/blob/main/README.md)
- [Demo](https://ericguo5513.github.io/momask/)

## CADAM

3D printing & generative CAD · 3D, reconstruction & assets · Browser tools & web media

First complete guide for a previously screened discovery; documentation checked today. Repository created 2025-09-01; current source metadata is a discovery signal, not evidence of a significant product upgrade.

### How it uses AI

Model-guided CAD authoring turns language/image intent into editable parametric geometry through a creative application workflow. [Source](https://github.com/Adam-CAD/CADAM/blob/master/README.md)

### Introduction

An AI-assisted parametric CAD interface that converts descriptions or images into editable OpenSCAD-style designs. [Source 1](https://github.com/Adam-CAD/CADAM/blob/master/README.md)

### What it is good for

Explore a printable bracket, enclosure or geometric art object, then change dimensions through exposed parameters and inspect the solid. [Source 1](https://github.com/Adam-CAD/CADAM/blob/master/README.md)

### Demo & examples

The project links a hosted browser demo and documents STL, SCAD and DXF exports; the hosted service is separate from local source deployment. [Source 1](https://github.com/Adam-CAD/CADAM/blob/master/README.md) [Source 2](https://adam.new/cadam)

### Install

Documentation-based setup route; commands are examples from the project and were not executed during this review. [Source 1](https://github.com/Adam-CAD/CADAM/blob/master/README.md)

1. Install the documented Node/npm and Supabase development prerequisites.
2. Clone the repository, install dependencies and configure frontend/server variables without exposing keys.
3. Start local Supabase and the development server; follow the webhook/ngrok guide only if that integration is needed.

```sh
npm install
```


```sh
npx supabase start
```


```sh
npm run dev
```

### First project

Begin with a small, permitted sample and inspect the result. [Source 1](https://github.com/Adam-CAD/CADAM/blob/master/README.md)

1. Describe a simple parametric object with dimensions and review the generated geometry.
2. Adjust parameters and inspect intersecting parts/wall thickness.
3. Export SCAD for further editing or STL/DXF for a fabrication workflow that you verify independently.
### Hardware & software

Published requirements and explicit documentation gaps follow. [Source 1](https://github.com/Adam-CAD/CADAM/blob/master/README.md)

- **Hardware:** The inspected prerequisites do not give CPU/GPU, RAM or storage minima. A local server stack is required for development despite the browser-based geometry preview.
- **Software:** Node ^20.19.0 or >=22.12.0, npm >=10 and Supabase CLI; ngrok is documented for webhook development. AI provider setup is distinct from browser rendering.
- **Platforms:** The user interface runs in a browser via WebAssembly. Native host support and the AI backend depend on the selected Node/Supabase/provider stack, not on the browser alone.

### License, model weights & costs

The complete top-level GPL-3.0 software terms were reviewed and archived today; model/dependency/host terms remain separate. [Source 1](https://github.com/Adam-CAD/CADAM/blob/master/LICENSE) [Source 2](https://github.com/Adam-CAD/CADAM/blob/master/README.md)

- **Code:** GPL-3.0
- **Weights:** GPL-3.0 software; model/provider and CAD library terms remain separate. STL export does not make a proprietary hosted AI model open source.
- **Commercial:** The main GPL-3.0 code grant permits commercial use under its notice/source and other conditions. Model, component, asset and hosted-service permission is separate. GPL-3.0 software; model/provider and CAD library terms remain separate. STL export does not make a proprietary hosted AI model open source.
- **Cost:** Self-hosted code has no license fee; AI provider calls, Supabase hosting or tunnels can have service costs. No current price is assumed.

### Why it merits attention

Assessment: editable parameters and multiple geometry exports make the AI output inspectable and useful for iteration. No generated solid was checked or printed here. [Source 1](https://github.com/Adam-CAD/CADAM/blob/master/README.md)

### Limitations

AI-generated dimensions and solids can be wrong. Validate manifold geometry, tolerances and physical suitability before printing; software operation is not fabrication safety certification. [Source 1](https://github.com/Adam-CAD/CADAM/blob/master/README.md) [Source 2](https://github.com/Adam-CAD/CADAM/blob/master/LICENSE)

### Get the tool

- [Repository](https://github.com/Adam-CAD/CADAM)
- [Documentation](https://github.com/Adam-CAD/CADAM/blob/master/README.md)
- [Demo](https://adam.new/cadam)

## BiRefNet

Images & design · Photography, restoration & color · Fashion, textiles & wearable media

First complete guide for a previously screened discovery; documentation checked today. Repository created 2022-08-17; current source metadata is a discovery signal, not evidence of a significant product upgrade.

### How it uses AI

Learned dichotomous image segmentation produces high-resolution foreground masks for compositing and asset cutouts. [Source](https://github.com/ZhengPeng7/BiRefNet/blob/main/README.md)

### Introduction

A learned high-resolution foreground/subject segmentation model that creates masks for background removal and compositing. [Source 1](https://github.com/ZhengPeng7/BiRefNet/blob/main/README.md)

### What it is good for

Prepare a photographic subject or product cutout, then refine its edges in an image editor before placing it in a new composition. [Source 1](https://github.com/ZhengPeng7/BiRefNet/blob/main/README.md)

### Demo & examples

The official Hugging Face Space and model card provide adjustable-resolution inference and a Python masking example. [Source 1](https://github.com/ZhengPeng7/BiRefNet/blob/main/README.md) [Source 2](https://huggingface.co/spaces/ZhengPeng7/BiRefNet_demo)

### Install

Documentation-based setup route; commands are examples from the project and were not executed during this review. [Source 1](https://github.com/ZhengPeng7/BiRefNet/blob/main/README.md)

1. Use the documented Python 3.11 environment and requirements for the repository, or the model-card Transformers example.
2. Download the selected BiRefNet checkpoint and inspect its remote-code/dependency requirements.
3. Start with one image and its published preprocessing/postprocessing steps.

```sh
pip install -r requirements.txt
```

### First project

Begin with a small, permitted sample and inspect the result. [Source 1](https://github.com/ZhengPeng7/BiRefNet/blob/main/README.md)

1. Load the chosen checkpoint using the model-card example.
2. Generate a foreground mask for a permitted image and apply it to alpha.
3. Inspect hair, transparent materials and fine edges before compositing.
### Hardware & software

Published requirements and explicit documentation gaps follow. [Source 1](https://github.com/ZhengPeng7/BiRefNet/blob/main/README.md)

- **Hardware:** Model-card inference uses CUDA at a documented example resolution. Minimum RAM, VRAM and model/storage requirements are not published as a universal floor.
- **Software:** The repository example uses Python 3.11; PyTorch >=2.5 is described for faster compiled training. Inference through Transformers also needs its documented transforms and model implementation.
- **Platforms:** CUDA inference and optional ONNX deployments are documented. The inspected core instructions do not confirm an end-to-end native macOS or mobile deployment.

### License, model weights & costs

The complete top-level MIT software terms were reviewed and archived today; model/dependency/host terms remain separate. [Source 1](https://github.com/ZhengPeng7/BiRefNet/blob/main/LICENSE) [Source 2](https://github.com/ZhengPeng7/BiRefNet/blob/main/README.md) [Source 3](https://huggingface.co/ZhengPeng7/BiRefNet)

- **Code:** MIT
- **Weights:** MIT code; the inspected BiRefNet model card also identifies MIT. Training datasets, third-party deployments and substituted checkpoints retain separate terms.
- **Commercial:** The main MIT code grant permits commercial use under its notice/source and other conditions. Model, component, asset and hosted-service permission is separate. MIT code; the inspected BiRefNet model card also identifies MIT. Training datasets, third-party deployments and substituted checkpoints retain separate terms.
- **Cost:** No required paid background-removal API for the local route. Compute, checkpoint downloads and any optional hosted service have separate costs/limits.

### Why it merits attention

Assessment: explicit masks, resolution controls and a local inference example suit artist-controlled compositing. This review did not test edge quality or speed. [Source 1](https://github.com/ZhengPeng7/BiRefNet/blob/main/README.md)

### Limitations

A mask is not a guarantee of accurate mattes on every image. The model-card loading example uses remote model code, so review it before installation; nothing was installed here. [Source 1](https://github.com/ZhengPeng7/BiRefNet/blob/main/README.md) [Source 2](https://github.com/ZhengPeng7/BiRefNet/blob/main/LICENSE) [Source 3](https://huggingface.co/ZhengPeng7/BiRefNet)

### Get the tool

- [Repository](https://github.com/ZhengPeng7/BiRefNet)
- [Documentation](https://github.com/ZhengPeng7/BiRefNet/blob/main/README.md)
- [Demo](https://huggingface.co/spaces/ZhengPeng7/BiRefNet_demo)

## PaddleOCR

Creative publishing & presentation · Archives, media restoration & collections · Accessible media & assistive creation · Data art & scientific visualization

First complete guide for a previously screened discovery; documentation checked today. Repository created 2020-05-08; current source metadata is a discovery signal, not evidence of a significant product upgrade.

### How it uses AI

OCR/document models extract visual text and structure for searchable media, translation and creator document workflows. [Source](https://github.com/PaddlePaddle/PaddleOCR/blob/main/README.md)

### Introduction

A neural OCR and document-parsing suite covering scene text, page structure and vision-language document understanding. [Source 1](https://github.com/PaddlePaddle/PaddleOCR/blob/main/README.md)

### What it is good for

Recover text from scanned artist books, exhibition labels and visual archives, or convert complex source pages into editable structured content. [Source 1](https://github.com/PaddlePaddle/PaddleOCR/blob/main/README.md)

### Demo & examples

The official site and README show OCR, structured document and vision-language parsing examples with Markdown/JSON output. [Source 1](https://github.com/PaddlePaddle/PaddleOCR/blob/main/README.md)

### Install

Documentation-based setup route; commands are examples from the project and were not executed during this review. [Source 1](https://github.com/PaddlePaddle/PaddleOCR/blob/main/README.md) [Source 2](https://github.com/PaddlePaddle/PaddleOCR/blob/main/docs/version3.x/installation.en.md)

1. Install the base OCR package or the optional document-parsing group required by your task.
2. Install the selected PaddlePaddle/Transformers inference engine using the current engine guide.
3. Follow the OCR pipeline example for an image before trying large PDFs or document VLMs.

```sh
python -m pip install paddleocr
```

### First project

Begin with a small, permitted sample and inspect the result. [Source 1](https://github.com/PaddlePaddle/PaddleOCR/blob/main/README.md)

1. Select OCR for text recognition or a document pipeline for layout/structure extraction.
2. Run a permitted scan and save recognized text plus coordinates/structured output.
3. Check names, punctuation, rare characters and reading order against the original before republishing.
### Hardware & software

Published requirements and explicit documentation gaps follow. [Source 1](https://github.com/PaddlePaddle/PaddleOCR/blob/main/README.md) [Source 2](https://github.com/PaddlePaddle/PaddleOCR/blob/main/docs/version3.x/installation.en.md)

- **Hardware:** CPU/GPU and model-specific backends are available; the suite does not publish a single RAM/VRAM/storage minimum for every pipeline.
- **Software:** The installation guide specifies Python >=3.8 for base OCR/doc2md and >=3.9 for other optional groups. PaddleOCR 3.5 uses separately installed configurable inference engines; training/export uses PaddlePaddle.
- **Platforms:** README and deployment notes cover Linux, Windows and macOS, with different engine/model capabilities. Linux/Windows C++ deployment and Windows RTX 50 support are explicitly mentioned; this is not equal support for every VLM backend.

### License, model weights & costs

The complete top-level Apache-2.0 software terms were reviewed and archived today; model/dependency/host terms remain separate. [Source 1](https://github.com/PaddlePaddle/PaddleOCR/blob/main/LICENSE) [Source 2](https://github.com/PaddlePaddle/PaddleOCR/blob/main/README.md)

- **Code:** Apache-2.0
- **Weights:** Apache-2.0 code. Check the exact OCR/VLM checkpoint, training data and any document-translation/provider dependency; the main repository license is not a blanket license for source documents.
- **Commercial:** The main Apache-2.0 code grant permits commercial use under its notice/source and other conditions. Model, component, asset and hosted-service permission is separate. Apache-2.0 code. Check the exact OCR/VLM checkpoint, training data and any document-translation/provider dependency; the main repository license is not a blanket license for source documents.
- **Cost:** Local inference can avoid a paid OCR API. Larger model compute, hosted services and optional provider features can incur costs.

### Why it merits attention

Assessment: distinct text/layout pipelines and inspectable structured output are useful for preservation and accessible publishing. Author benchmark claims are not independently reproduced. [Source 1](https://github.com/PaddlePaddle/PaddleOCR/blob/main/README.md)

### Limitations

OCR and generated structure can be wrong. This does not create a finished accessible document automatically; human proofreading, reading-order and layout checks remain necessary. [Source 1](https://github.com/PaddlePaddle/PaddleOCR/blob/main/README.md) [Source 2](https://github.com/PaddlePaddle/PaddleOCR/blob/main/LICENSE)

### Get the tool

- [Repository](https://github.com/PaddlePaddle/PaddleOCR)
- [Documentation](https://github.com/PaddlePaddle/PaddleOCR/blob/main/README.md)

## DWPose

Motion capture & character animation · Avatars, digital humans & lip sync · Images & design

First complete guide for a previously screened discovery; documentation checked today. Repository created 2023-07-26; current source metadata is a discovery signal, not evidence of a significant product upgrade.

### How it uses AI

A whole-body pose estimator extracts control signals useful for guided image generation, character posing and video work. [Source](https://github.com/IDEA-Research/DWPose/blob/onnx/README.md)

### Introduction

A whole-body pose estimator with learned body, face and hand keypoints and an integration route into ControlNet. [Source 1](https://github.com/IDEA-Research/DWPose/blob/onnx/README.md)

### What it is good for

Extract pose guidance from authorized photos for character illustration or frame-based animation preprocessing. [Source 1](https://github.com/IDEA-Research/DWPose/blob/onnx/README.md)

### Demo & examples

The README publishes ControlNet comparisons and a Gradio pose demo; the research model is also available through documented ONNX branches. [Source 1](https://github.com/IDEA-Research/DWPose/blob/onnx/README.md)

### Install

Documentation-based setup route; commands are examples from the project and were not executed during this review. [Source 1](https://github.com/IDEA-Research/DWPose/blob/onnx/README.md) [Source 2](https://github.com/IDEA-Research/DWPose/blob/main/INSTALL.md)

1. Choose the MMPose training/testing environment or the distinct ControlNet/ONNX inference path.
2. Download both the pose checkpoint and the required detector model.
3. Run the pose inference example or the ControlNet demo using the matching environment.

```sh
python dwpose_infer_example.py
```


```sh
python gradio_dw_open_pose.py
```

### First project

Begin with a small, permitted sample and inspect the result. [Source 1](https://github.com/IDEA-Research/DWPose/blob/onnx/README.md)

1. Run the estimator on a clearly visible person image.
2. Inspect body/hand/face landmarks and correct unsuitable guidance before generation.
3. Use the pose image as conditioning in the documented ControlNet workflow.
### Hardware & software

Published requirements and explicit documentation gaps follow. [Source 1](https://github.com/IDEA-Research/DWPose/blob/onnx/README.md) [Source 2](https://github.com/IDEA-Research/DWPose/blob/main/INSTALL.md)

- **Hardware:** The quickstart gives no universal CPU/GPU, RAM, VRAM or storage minimum. Inference resources also depend on the detector and any downstream diffusion model.
- **Software:** The MMPose environment example uses torch 1.9.1/cu111; the ControlNet route has its own environment and optional mmengine/mmcv/mmdet/mmpose versions. ONNX/OpenCV paths can avoid mmcv.
- **Platforms:** The repository distinguishes environment/backend paths but does not certify a complete native OS/headset/mobile support matrix. A pose demo is not a full motion-capture system.

### License, model weights & costs

The complete top-level Apache-2.0 software terms were reviewed and archived today; model/dependency/host terms remain separate. [Source 1](https://github.com/IDEA-Research/DWPose/blob/onnx/LICENSE) [Source 2](https://github.com/IDEA-Research/DWPose/blob/onnx/README.md)

- **Code:** Apache-2.0
- **Weights:** Apache-2.0 code, including MMPose notices. Detector/pose checkpoints, datasets and any downstream diffusion weights require independent terms review.
- **Commercial:** The main Apache-2.0 code grant permits commercial use under its notice/source and other conditions. Model, component, asset and hosted-service permission is separate. Apache-2.0 code, including MMPose notices. Detector/pose checkpoints, datasets and any downstream diffusion weights require independent terms review.
- **Cost:** Local compute and model storage; no mandatory paid pose API in the described route.

### Why it merits attention

Assessment: whole-body landmarks and direct conditioning examples make it useful in image/character workflows. No pose accuracy or downstream generation was tested. [Source 1](https://github.com/IDEA-Research/DWPose/blob/onnx/README.md)

### Limitations

Occlusion, difficult hands and missing subjects can produce bad keypoints. It estimates image pose rather than guaranteeing a metrically accurate, rigged 3D animation. [Source 1](https://github.com/IDEA-Research/DWPose/blob/onnx/README.md) [Source 2](https://github.com/IDEA-Research/DWPose/blob/onnx/LICENSE)

### Get the tool

- [Repository](https://github.com/IDEA-Research/DWPose)
- [Documentation](https://github.com/IDEA-Research/DWPose/blob/onnx/README.md)

## Grounding DINO

Images & design · Video, animation & film · Photogrammetry, scanning & neural rendering

First complete guide for a previously screened discovery; documentation checked today. Repository created 2023-03-09; current source metadata is a discovery signal, not evidence of a significant product upgrade.

### How it uses AI

Language-conditioned detection locates requested objects in images for selection, masking and visual-media processing. [Source](https://github.com/IDEA-Research/GroundingDINO/blob/main/README.md)

### Introduction

A text-conditioned open-set object detector that finds image regions described in natural language. [Source 1](https://github.com/IDEA-Research/GroundingDINO/blob/main/README.md)

### What it is good for

Locate props or subjects in a creative asset collection, and provide boxes to a separately selected segmentation/inpainting workflow. [Source 1](https://github.com/IDEA-Research/GroundingDINO/blob/main/README.md)

### Demo & examples

The repository includes annotated image examples and a CLI accepting an image, text prompt and output folder. [Source 1](https://github.com/IDEA-Research/GroundingDINO/blob/main/README.md)

### Install

Documentation-based setup route; commands are examples from the project and were not executed during this review. [Source 1](https://github.com/IDEA-Research/GroundingDINO/blob/main/README.md)

1. Clone the source and install it in editable mode.
2. Use a matching CUDA toolkit if compiling GPU support; the README also documents CPU-only compilation.
3. Download the documented checkpoint and run the image inference demo.

```sh
pip install -e .
```

### First project

Begin with a small, permitted sample and inspect the result. [Source 1](https://github.com/IDEA-Research/GroundingDINO/blob/main/README.md)

1. Provide a permitted image and an object phrase such as chair.
2. Inspect detection boxes/confidence before using them as an editing selection.
3. Combine with another explicitly licensed segmentation/editor tool only after checking that integration.
### Hardware & software

Published requirements and explicit documentation gaps follow. [Source 1](https://github.com/IDEA-Research/GroundingDINO/blob/main/README.md)

- **Hardware:** GPU and CPU-only paths are documented. The README does not specify universal system RAM, VRAM or storage minimums.
- **Software:** Python/PyTorch environment with native extension compilation and a downloaded model checkpoint; CUDA_HOME must match the actual CUDA runtime when using GPU builds. A universal Python minimum is not stated in the inspected README.
- **Platforms:** CPU/CUDA build instructions are documented, but this review does not establish native macOS/MPS or mobile support. Video editing needs additional tracking/segmentation integration.

### License, model weights & costs

The complete top-level Apache-2.0 software terms were reviewed and archived today; model/dependency/host terms remain separate. [Source 1](https://github.com/IDEA-Research/GroundingDINO/blob/main/LICENSE) [Source 2](https://github.com/IDEA-Research/GroundingDINO/blob/main/README.md)

- **Code:** Apache-2.0
- **Weights:** Apache-2.0 software. Exact checkpoint, dataset and downstream segmentation/generative model permissions must be checked separately.
- **Commercial:** The main Apache-2.0 code grant permits commercial use under its notice/source and other conditions. Model, component, asset and hosted-service permission is separate. Apache-2.0 software. Exact checkpoint, dataset and downstream segmentation/generative model permissions must be checked separately.
- **Cost:** No required paid detection API for local use. Compute and asset storage remain local costs.

### Why it merits attention

Assessment: natural-language selection and visible detection outputs make it an inspectable component for artist tooling. No detector benchmark was reproduced. [Source 1](https://github.com/IDEA-Research/GroundingDINO/blob/main/README.md)

### Limitations

It returns detections rather than finished masks, tracking or edits. Thresholds and ambiguous phrases affect results; every proposed selection needs inspection. [Source 1](https://github.com/IDEA-Research/GroundingDINO/blob/main/README.md) [Source 2](https://github.com/IDEA-Research/GroundingDINO/blob/main/LICENSE)

### Get the tool

- [Repository](https://github.com/IDEA-Research/GroundingDINO)
- [Documentation](https://github.com/IDEA-Research/GroundingDINO/blob/main/README.md)

## ControlNet — original implementation

Images & design · Computational art & creative coding · Fashion, textiles & wearable media

First complete guide for a previously screened discovery; documentation checked today. Repository created 2023-02-01; current source metadata is a discovery signal, not evidence of a significant product upgrade.

### How it uses AI

A neural control branch adds edges, pose, depth or other structured conditioning to diffusion image generation. [Source](https://github.com/lllyasviel/ControlNet/blob/main/README.md)

### Introduction

A neural conditioning architecture and demos that steer Stable Diffusion with edges, scribbles, depth, pose or other control maps. [Source 1](https://github.com/lllyasviel/ControlNet/blob/main/README.md)

### What it is good for

Keep composition or a pose while exploring illustration, material, fashion-concept or scene variants. [Source 1](https://github.com/lllyasviel/ControlNet/blob/main/README.md)

### Demo & examples

The original repository publishes nine Gradio apps and supplied control images. This profile distinguishes the original implementation from the linked 1.1/nightly work. [Source 1](https://github.com/lllyasviel/ControlNet/blob/main/README.md)

### Install

Documentation-based setup route; commands are examples from the project and were not executed during this review. [Source 1](https://github.com/lllyasviel/ControlNet/blob/main/README.md)

1. Create the environment from environment.yaml.
2. Download the selected diffusion/control checkpoint and any annotator models into the documented folders.
3. Run the demo matching your control type; the Canny app is a simple first comparison.

```sh
conda env create -f environment.yaml
```


```sh
conda activate control
```


```sh
python gradio_canny2image.py
```

### First project

Begin with a small, permitted sample and inspect the result. [Source 1](https://github.com/lllyasviel/ControlNet/blob/main/README.md)

1. Load a permitted image or draw a control map.
2. Set the prompt and control strength; generate variants while preserving the chosen structural cue.
3. Compare with and without control, then inspect anatomy, text and material details.
### Hardware & software

Published requirements and explicit documentation gaps follow. [Source 1](https://github.com/lllyasviel/ControlNet/blob/main/README.md)

- **Hardware:** The README provides a low-VRAM mode intended for 8 GB GPUs; that is a documented configuration, not a guarantee for every resolution/model. RAM and storage minima are not specified.
- **Software:** The pinned environment.yaml, diffusion/control weights and selected annotator dependencies are required. Later integrations and ControlNet 1.1 have distinct instructions.
- **Platforms:** The original CUDA-oriented environment/demo path is documented. Do not infer native Mac/mobile support from the Gradio interface; use a separately documented implementation for those targets.

### License, model weights & costs

The complete top-level Apache-2.0 software terms were reviewed and archived today; model/dependency/host terms remain separate. [Source 1](https://github.com/lllyasviel/ControlNet/blob/main/LICENSE) [Source 2](https://github.com/lllyasviel/ControlNet/blob/main/README.md)

- **Code:** Apache-2.0
- **Weights:** Apache-2.0 code. Stable Diffusion base weights, ControlNet checkpoints and annotator assets have their own terms; source openness does not remove OpenRAIL or other checkpoint restrictions.
- **Commercial:** The main Apache-2.0 code grant permits commercial use under its notice/source and other conditions. Model, component, asset and hosted-service permission is separate. Apache-2.0 code. Stable Diffusion base weights, ControlNet checkpoints and annotator assets have their own terms; source openness does not remove OpenRAIL or other checkpoint restrictions.
- **Cost:** Local GPU and model storage; optional hosted UIs/providers have separate service costs.

### Why it merits attention

Assessment: controllable structure and reproducible demo inputs provide more inspectable creative control than text prompts alone. No image generation was performed in this review. [Source 1](https://github.com/lllyasviel/ControlNet/blob/main/README.md)

### Limitations

Conditioning does not guarantee exact geometry or design feasibility. This is a foundational baseline first guide, not a claim that the 2023 implementation launched today. [Source 1](https://github.com/lllyasviel/ControlNet/blob/main/README.md) [Source 2](https://github.com/lllyasviel/ControlNet/blob/main/LICENSE)

### Get the tool

- [Repository](https://github.com/lllyasviel/ControlNet)
- [Documentation](https://github.com/lllyasviel/ControlNet/blob/main/README.md)

## IC-Light

Photography, restoration & color · Images & design · VFX, compositing & relighting

First complete guide for a previously screened discovery; documentation checked today. Repository created 2024-05-07; current source metadata is a discovery signal, not evidence of a significant product upgrade.

### How it uses AI

Image-conditioned diffusion relights a subject for new photographic/compositing concepts. [Source](https://github.com/lllyasviel/IC-Light/blob/main/README.md)

### Introduction

An image relighting system conditioned on foreground/text or a supplied background, built with diffusion models. [Source 1](https://github.com/lllyasviel/IC-Light/blob/main/README.md)

### What it is good for

Explore alternate portrait or product lighting and compare how a foreground could fit a changed environment. [Source 1](https://github.com/lllyasviel/IC-Light/blob/main/README.md)

### Demo & examples

The README shows foreground and background-conditioned examples and links an official Hugging Face Space. [Source 1](https://github.com/lllyasviel/IC-Light/blob/main/README.md) [Source 2](https://huggingface.co/spaces/lllyasviel/IC-Light)

### Install

Documentation-based setup route; commands are examples from the project and were not executed during this review. [Source 1](https://github.com/lllyasviel/IC-Light/blob/main/README.md)

1. Create the documented Python 3.10 environment and CUDA PyTorch stack.
2. Install requirements and launch the text/foreground or background-conditioned Gradio script.
3. Review downloaded model and background-remover terms before commercial work.

```sh
pip install -r requirements.txt
```


```sh
python gradio_demo.py
```


```sh
python gradio_demo_bg.py
```

### First project

Begin with a small, permitted sample and inspect the result. [Source 1](https://github.com/lllyasviel/IC-Light/blob/main/README.md)

1. Load a permitted foreground image and describe the desired light.
2. Generate several relighting variants or condition on a background.
3. Inspect identity, edges, color and consistency before compositing the selected result.
### Hardware & software

Published requirements and explicit documentation gaps follow. [Source 1](https://github.com/lllyasviel/IC-Light/blob/main/README.md)

- **Hardware:** The documented install uses CUDA 12.1 PyTorch wheels. A universal VRAM, system RAM or total model storage minimum is not stated.
- **Software:** Python 3.10; PyTorch/torchvision, requirements.txt and automatically downloaded relighting/background-removal weights.
- **Platforms:** The local guide is CUDA-oriented. Native macOS/MPS and CPU suitability for the complete current pipeline are not confirmed by the inspected instructions.

### License, model weights & costs

The complete top-level Apache-2.0 software terms were reviewed and archived today; model/dependency/host terms remain separate. [Source 1](https://github.com/lllyasviel/IC-Light/blob/main/LICENSE) [Source 2](https://github.com/lllyasviel/IC-Light/blob/main/README.md)

- **Code:** Apache-2.0
- **Weights:** Apache-2.0 code. The README explicitly says BRIA RMBG-1.4 is non-commercial and suggests replacing it with BiRefNet for commercial projects; diffusion checkpoint terms are also separate.
- **Commercial:** The main Apache-2.0 code grant permits commercial use under its notice/source and other conditions. Model, component, asset and hosted-service permission is separate. Apache-2.0 code. The README explicitly says BRIA RMBG-1.4 is non-commercial and suggests replacing it with BiRefNet for commercial projects; diffusion checkpoint terms are also separate.
- **Cost:** No mandatory paid relighting API for local execution; compute and potentially separately licensed dependency/model use may have costs.

### Why it merits attention

Assessment: explicit foreground/background modes and examples give photographers a concrete lighting study workflow. Results and installation were not tested here. [Source 1](https://github.com/lllyasviel/IC-Light/blob/main/README.md)

### Limitations

Generated lighting can change image details rather than perform physically exact relighting. A permissive main license does not permit unrestricted use of its default background-removal dependency. [Source 1](https://github.com/lllyasviel/IC-Light/blob/main/README.md) [Source 2](https://github.com/lllyasviel/IC-Light/blob/main/LICENSE)

### Get the tool

- [Repository](https://github.com/lllyasviel/IC-Light)
- [Documentation](https://github.com/lllyasviel/IC-Light/blob/main/README.md)
- [Demo](https://huggingface.co/spaces/lllyasviel/IC-Light)

## Diffusers

Images & design · Video, animation & film · Audio, music & voice · Computational art & creative coding

First complete guide for a previously screened discovery; documentation checked today. Repository created 2022-05-30; current source metadata is a discovery signal, not evidence of a significant product upgrade.

### How it uses AI

The library implements learned diffusion pipelines for generating or transforming images, video and other media. [Source](https://github.com/huggingface/diffusers/blob/main/README.md)

### Introduction

A Python framework exposing neural diffusion pipelines, schedulers and model components for media generation. [Source 1](https://github.com/huggingface/diffusers/blob/main/README.md)

### What it is good for

Build a repeatable generative image/video/audio experiment, compare model settings or add diffusion generation to a creative application. [Source 1](https://github.com/huggingface/diffusers/blob/main/README.md)

### Demo & examples

Official documentation provides pipeline examples; the README shows pretrained image generation and a lower-level scheduler/model loop. [Source 1](https://github.com/huggingface/diffusers/blob/main/README.md)

### Install

Documentation-based setup route; commands are examples from the project and were not executed during this review. [Source 1](https://github.com/huggingface/diffusers/blob/main/README.md)

1. Create an isolated environment and install PyTorch for the actual accelerator.
2. Install Diffusers with the torch extra, then choose a supported model/pipeline.
3. Read that models usage and license before downloading; use the MPS guide for compatible Apple Silicon image paths.

```sh
pip install --upgrade "diffusers[torch]"
```

### First project

Begin with a small, permitted sample and inspect the result. [Source 1](https://github.com/huggingface/diffusers/blob/main/README.md)

1. Load a pipeline using from_pretrained for the chosen model.
2. Choose a documented device and precision, generate a small output and record its seed/settings.
3. Save the asset and compare controlled changes rather than changing every setting at once.
### Hardware & software

Published requirements and explicit documentation gaps follow. [Source 1](https://github.com/huggingface/diffusers/blob/main/README.md)

- **Hardware:** Resources vary widely by checkpoint, resolution, duration and offload choices. There is no library-wide RAM, VRAM or storage floor.
- **Software:** Python, PyTorch, Diffusers and model-specific optional libraries. Exact version requirements should come from the selected release/pipeline, not one assumed version for every model.
- **Platforms:** CUDA paths and an official Apple Silicon MPS optimization guide are documented. Individual video/audio pipelines and Windows/Linux/Mac backends have their own constraints.

### License, model weights & costs

The complete top-level Apache-2.0 software terms were reviewed and archived today; model/dependency/host terms remain separate. [Source 1](https://github.com/huggingface/diffusers/blob/main/LICENSE) [Source 2](https://github.com/huggingface/diffusers/blob/main/README.md)

- **Code:** Apache-2.0
- **Weights:** Apache-2.0 software. Every pretrained checkpoint, LoRA, tokenizer and source asset keeps its own terms; the framework does not make all hosted models open source.
- **Commercial:** The main Apache-2.0 code grant permits commercial use under its notice/source and other conditions. Model, component, asset and hosted-service permission is separate. Apache-2.0 software. Every pretrained checkpoint, LoRA, tokenizer and source asset keeps its own terms; the framework does not make all hosted models open source.
- **Cost:** Local code has no license fee. GPU/cloud compute, gated models or optional provider services can incur costs.

### Why it merits attention

Assessment: common pipeline APIs and explicit component/scheduler control are strong foundations for reproducible creative code. No selected pipeline was installed or tested here. [Source 1](https://github.com/huggingface/diffusers/blob/main/README.md)

### Limitations

A framework is not an end-user editor. Model availability in a library is not evidence of high output quality, low memory demand or commercial permission. [Source 1](https://github.com/huggingface/diffusers/blob/main/README.md) [Source 2](https://github.com/huggingface/diffusers/blob/main/LICENSE)

### Get the tool

- [Repository](https://github.com/huggingface/diffusers)
- [Documentation](https://github.com/huggingface/diffusers/blob/main/README.md)

## DiffSynth-Studio

Images & design · Video, animation & film · Audio, music & voice · Computational art & creative coding

First complete guide for a previously screened discovery; documentation checked today. Repository created 2023-12-07; current source metadata is a discovery signal, not evidence of a significant product upgrade.

### How it uses AI

Its model pipelines orchestrate learned image/video and related synthesis/editing workflows with accelerator-specific setup. [Source](https://github.com/modelscope/DiffSynth-Studio/blob/main/README.md)

### Introduction

A multi-model diffusion engine for image, video and audio inference and training, with offloading and quantization options. [Source 1](https://github.com/modelscope/DiffSynth-Studio/blob/main/README.md)

### What it is good for

Prototype cross-media generators or adapt a model to a visual/audio style while controlling model loading and memory placement. [Source 1](https://github.com/modelscope/DiffSynth-Studio/blob/main/README.md)

### Demo & examples

The repository provides model-specific example scripts and linked ComfyUI/WebUI integrations; these are separate frontends rather than one guaranteed universal application. [Source 1](https://github.com/modelscope/DiffSynth-Studio/blob/main/README.md)

### Install

Documentation-based setup route; commands are examples from the project and were not executed during this review. [Source 1](https://github.com/modelscope/DiffSynth-Studio/blob/main/README.md) [Source 2](https://github.com/modelscope/DiffSynth-Studio/blob/main/docs/en/Pipeline_Usage/Setup.md)

1. Install from the current source for recent model integrations, or use the packaged release with possible feature lag.
2. Enable the audio/quant/training extra relevant to the project.
3. Choose a model-specific example and backend from the setup guide.

```sh
pip install -e .
```


```sh
pip install -e ".[audio,quant]"
```

### First project

Begin with a small, permitted sample and inspect the result. [Source 1](https://github.com/modelscope/DiffSynth-Studio/blob/main/README.md)

1. Select one supported model and inspect its example inputs and checkpoint terms.
2. Generate a small media sample with its documented inference settings.
3. Apply offloading/quantization only with an appropriate example, then compare output before starting training.
### Hardware & software

Published requirements and explicit documentation gaps follow. [Source 1](https://github.com/modelscope/DiffSynth-Studio/blob/main/README.md) [Source 2](https://github.com/modelscope/DiffSynth-Studio/blob/main/docs/en/Pipeline_Usage/Setup.md)

- **Hardware:** Model-dependent CPU RAM, GPU VRAM and disk offload are supported; a single minimum for all models is not documented.
- **Software:** Python/PyTorch and selected dependency extras. NVIDIA is the default path; the setup guide gives AMD ROCm, Apple Silicon mps/cpu and Ascend NPU variants. Model-specific version constraints still apply.
- **Platforms:** The official setup explicitly covers NVIDIA, AMD ROCm on Linux, Apple Silicon and Ascend variants. This is documented backend guidance, not hands-on certification of every model on each OS.

### License, model weights & costs

The complete top-level Apache-2.0 software terms were reviewed and archived today; model/dependency/host terms remain separate. [Source 1](https://github.com/modelscope/DiffSynth-Studio/blob/main/LICENSE) [Source 2](https://github.com/modelscope/DiffSynth-Studio/blob/main/README.md)

- **Code:** Apache-2.0
- **Weights:** Apache-2.0 engine code. All integrated base models, fine-tuned weights, LoRAs and external services retain their separate licenses; labels such as open in an update log are not enough.
- **Commercial:** The main Apache-2.0 code grant permits commercial use under its notice/source and other conditions. Model, component, asset and hosted-service permission is separate. Apache-2.0 engine code. All integrated base models, fine-tuned weights, LoRAs and external services retain their separate licenses; labels such as open in an update log are not enough.
- **Cost:** Local/rented compute and storage costs. Optional hosted ModelScope experiences or other providers have their own service terms.

### Why it merits attention

Assessment: explicit model examples and multiple accelerator setup paths help compare creative workflows with equal platform attention. No benchmark or model output was independently tested. [Source 1](https://github.com/modelscope/DiffSynth-Studio/blob/main/README.md)

### Limitations

Fast integration updates can outpace packaged versions. Offloading/quantization may change speed or output; small VRAM claims are model/configuration-specific. [Source 1](https://github.com/modelscope/DiffSynth-Studio/blob/main/README.md) [Source 2](https://github.com/modelscope/DiffSynth-Studio/blob/main/LICENSE)

### Get the tool

- [Repository](https://github.com/modelscope/DiffSynth-Studio)
- [Documentation](https://github.com/modelscope/DiffSynth-Studio/blob/main/README.md)

## Wan2.2

Video, animation & film · Storyboarding, narrative & comics · Avatars, digital humans & lip sync

First complete guide for a previously screened discovery; documentation checked today. Repository created 2025-07-28; current source metadata is a discovery signal, not evidence of a significant product upgrade.

### How it uses AI

Video diffusion models use text/image conditioning to generate motion clips for creative prototypes. [Source](https://github.com/Wan-Video/Wan2.2/blob/main/README.md)

### Introduction

A generative video family with separate text/image, hybrid 5B, speech-to-video and animation workflows. [Source 1](https://github.com/Wan-Video/Wan2.2/blob/main/README.md)

### What it is good for

Prototype a story shot from a concept image or explore motion for a fictional character; choose the model suited to the input. [Source 1](https://github.com/Wan-Video/Wan2.2/blob/main/README.md)

### Demo & examples

The official repository embeds video examples and CLI workflows for each model task. [Source 1](https://github.com/Wan-Video/Wan2.2/blob/main/README.md)

### Install

Documentation-based setup route; commands are examples from the project and were not executed during this review. [Source 1](https://github.com/Wan-Video/Wan2.2/blob/main/README.md)

1. Install torch >=2.4 and the repository requirements in an isolated environment.
2. Download the exact checkpoint matching the task; speech-to-video has additional dependencies.
3. For the lower-memory official route, follow the TI2V-5B example with the documented offload/CPU text-encoder flags.

```sh
pip install -r requirements.txt
```

### First project

Begin with a small, permitted sample and inspect the result. [Source 1](https://github.com/Wan-Video/Wan2.2/blob/main/README.md)

1. Choose text-to-video or provide a permitted image for image-to-video.
2. Set the matching task, checkpoint path, prompt and size using its generate.py example.
3. Generate a short shot, inspect temporal/anatomical artifacts and save its settings for comparison.
### Hardware & software

Published requirements and explicit documentation gaps follow. [Source 1](https://github.com/Wan-Video/Wan2.2/blob/main/README.md)

- **Hardware:** The official TI2V-5B 720p example documents >=24 GB VRAM with offloading and t5_cpu; A14B text/image and S2V examples document >=80 GB. These are task/configuration-specific floors. System RAM and total storage are not stated.
- **Software:** PyTorch >=2.4, compatible CUDA/attention dependencies, requirements.txt and selected weights. Speech synthesis via CosyVoice requires requirements_s2v.txt.
- **Platforms:** The documented local route is NVIDIA/CUDA-oriented with distributed options. Native Apple Silicon/MPS, mobile and non-CUDA support are not established by these examples.

### License, model weights & costs

The complete top-level Apache-2.0 software terms were reviewed and archived today; model/dependency/host terms remain separate. [Source 1](https://github.com/Wan-Video/Wan2.2/blob/main/LICENSE.txt) [Source 2](https://github.com/Wan-Video/Wan2.2/blob/main/README.md) [Source 3](https://huggingface.co/Wan-AI/Wan2.2-TI2V-5B)

- **Code:** Apache-2.0
- **Weights:** Apache-2.0 code; the inspected Wan2.2-TI2V-5B card also lists Apache-2.0. Other task checkpoints and speech/pose dependencies must be checked independently.
- **Commercial:** The main Apache-2.0 code grant permits commercial use under its notice/source and other conditions. Model, component, asset and hosted-service permission is separate. Apache-2.0 code; the inspected Wan2.2-TI2V-5B card also lists Apache-2.0. Other task checkpoints and speech/pose dependencies must be checked independently.
- **Cost:** No required paid video API for the local examples, but GPU resources and large checkpoint storage are substantial costs.

### Why it merits attention

Assessment: explicit task-specific commands and realistic hardware distinctions make evaluation more practical. No video or speed benchmark was generated here. [Source 1](https://github.com/Wan-Video/Wan2.2/blob/main/README.md)

### Limitations

The 5B memory figure does not apply to every Wan2.2 task. Reference identity, motion and timing may drift; generated clips need editorial and visual review. [Source 1](https://github.com/Wan-Video/Wan2.2/blob/main/README.md) [Source 2](https://github.com/Wan-Video/Wan2.2/blob/main/LICENSE.txt) [Source 3](https://huggingface.co/Wan-AI/Wan2.2-TI2V-5B)

### Get the tool

- [Repository](https://github.com/Wan-Video/Wan2.2)
- [Documentation](https://github.com/Wan-Video/Wan2.2/blob/main/README.md)

## LTX-Video — earlier generation

Video, animation & film · Storyboarding, narrative & comics

First complete guide for a previously screened discovery; documentation checked today. Repository created 2024-11-20; current source metadata is a discovery signal, not evidence of a significant product upgrade.

### How it uses AI

A diffusion video model turns text or visual conditioning into short generated video for concept development. [Source](https://github.com/Lightricks/LTX-Video/blob/main/README.md)

### Introduction

A video diffusion toolkit with image/video conditioning, extension and distilled model variants; separate from the newer LTX-2 project linked by its README. [Source 1](https://github.com/Lightricks/LTX-Video/blob/main/README.md)

### What it is good for

Animate a concept still, extend a short shot or test multiple visual/keyframe conditions for a storyboard. [Source 1](https://github.com/Lightricks/LTX-Video/blob/main/README.md)

### Demo & examples

The README publishes conditioned video examples and ComfyUI workflows, recommending ComfyUI for current output fidelity. [Source 1](https://github.com/Lightricks/LTX-Video/blob/main/README.md)

### Install

Documentation-based setup route; commands are examples from the project and were not executed during this review. [Source 1](https://github.com/Lightricks/LTX-Video/blob/main/README.md)

1. Use the documented Python/PyTorch environment and install the inference extra from source.
2. Choose the configuration/checkpoint matching the desired model version.
3. Use its ComfyUI workflow or inference.py and read the model-specific frame/resolution constraints.

```sh
python -m pip install -e ".[inference]"
```

### First project

Begin with a small, permitted sample and inspect the result. [Source 1](https://github.com/Lightricks/LTX-Video/blob/main/README.md)

1. Supply a permitted still or short video and a concise motion description.
2. Set conditioning start frames and the model configuration; generate a small clip first.
3. Inspect temporal consistency, save the seed and export a chosen draft for editing.
### Hardware & software

Published requirements and explicit documentation gaps follow. [Source 1](https://github.com/Lightricks/LTX-Video/blob/main/README.md)

- **Hardware:** VRAM demand varies by 2B/13B model, precision and offloading. The README includes configuration-specific low-memory claims, not one universal floor. System RAM and total storage minima are not documented.
- **Software:** Tested Python 3.10.5/CUDA 12.2; PyTorch >=2.1.2. macOS MPS was tested with 2.3.0 and the README specifies torch ==2.3 or >=2.6 for that path.
- **Platforms:** CUDA and explicitly documented macOS MPS paths. A universal Windows certification matrix is not provided in the inspected quickstart; ComfyUI integration is separately configured.

### License, model weights & costs

The complete top-level Apache-2.0 software terms were reviewed and archived today; model/dependency/host terms remain separate. [Source 1](https://github.com/Lightricks/LTX-Video/blob/main/LICENSE) [Source 2](https://github.com/Lightricks/LTX-Video/blob/main/README.md) [Source 3](https://huggingface.co/Lightricks/LTX-Video) [Source 4](https://huggingface.co/Lightricks/LTX-Video/blob/main/LTX-Video-Open-Weights-License-0.X.txt)

- **Code:** Apache-2.0
- **Weights:** Apache-2.0 code. Weight terms depend on checkpoint: the model card assigns a separate LTX-Video Open Weights license to the 0.9.8 variants, while earlier examples mention OpenRAIL. Review the exact weight license.
- **Commercial:** The main Apache-2.0 code grant permits commercial use under its notice/source and other conditions. Model, component, asset and hosted-service permission is separate. Apache-2.0 code. Weight terms depend on checkpoint: the model card assigns a separate LTX-Video Open Weights license to the 0.9.8 variants, while earlier examples mention OpenRAIL. Review the exact weight license.
- **Cost:** Local compute/model storage costs. LTX Studio is a distinct hosted product; its pricing/terms are not assumed to apply to the open-source code.

### Why it merits attention

Assessment: multi-condition/extension examples and an explicit MPS note make it useful for equal-platform experimentation. Developer quality/speed claims were not reproduced. [Source 1](https://github.com/Lightricks/LTX-Video/blob/main/README.md)

### Limitations

Image/video dimensions and frame counts have constraints. The authors say standalone inference.py fidelity is being brought up to the recommended ComfyUI workflow; older and newer LTX versions are not interchangeable. [Source 1](https://github.com/Lightricks/LTX-Video/blob/main/README.md) [Source 2](https://github.com/Lightricks/LTX-Video/blob/main/LICENSE) [Source 3](https://huggingface.co/Lightricks/LTX-Video) [Source 4](https://huggingface.co/Lightricks/LTX-Video/blob/main/LTX-Video-Open-Weights-License-0.X.txt)

### Get the tool

- [Repository](https://github.com/Lightricks/LTX-Video)
- [Documentation](https://github.com/Lightricks/LTX-Video/blob/main/README.md)

## Open-Sora

Video, animation & film · Computational art & creative coding

First complete guide for a previously screened discovery; documentation checked today. Repository created 2024-02-20; current source metadata is a discovery signal, not evidence of a significant product upgrade.

### How it uses AI

Its learned video-generation stack provides text/image-conditioned motion and training/inference tools for experimental media. [Source](https://github.com/hpcaitech/Open-Sora/blob/main/README.md)

### Introduction

A research video diffusion framework with image-to-video and text-to-image-to-video pipelines, training and distributed inference. [Source 1](https://github.com/hpcaitech/Open-Sora/blob/main/README.md)

### What it is good for

Study controllable clip generation or fine-tune a video pipeline as a computational media experiment. [Source 1](https://github.com/hpcaitech/Open-Sora/blob/main/README.md)

### Demo & examples

The official README has version-specific video galleries and 256px/768px inference examples; old galleries are not evidence that every current model uses the same settings. [Source 1](https://github.com/hpcaitech/Open-Sora/blob/main/README.md)

### Install

Documentation-based setup route; commands are examples from the project and were not executed during this review. [Source 1](https://github.com/hpcaitech/Open-Sora/blob/main/README.md)

1. Create the documented Python 3.10 environment and install the matching PyTorch/CUDA/xformers/attention stack.
2. Install the source package and download the Open-Sora v2 checkpoint.
3. Start with the lower-resolution inference configuration and review any image-generator/component terms.

```sh
pip install -v .
```


```sh
torchrun --nproc_per_node 1 --standalone scripts/diffusion/inference.py configs/diffusion/inference/t2i2v_256px.py --save-dir samples --prompt "raining, sea" --offload True
```

### First project

Begin with a small, permitted sample and inspect the result. [Source 1](https://github.com/hpcaitech/Open-Sora/blob/main/README.md)

1. Choose image-to-video or the staged text-to-image-to-video route.
2. Generate one short low-resolution draft and inspect motion/subject continuity.
3. Only then adjust aspect ratio, frame count or distributed settings; record the configuration.
### Hardware & software

Published requirements and explicit documentation gaps follow. [Source 1](https://github.com/hpcaitech/Open-Sora/blob/main/README.md)

- **Hardware:** The published H100/H800 256px single-GPU benchmark reports 52.5 GB peak GPU memory with offloading; that is a measured example, not a universal minimum. RAM/storage floors are not published.
- **Software:** Python 3.10 example; torch >=2.4, matching CUDA/xformers/flash-attn, and ColossalAI for distributed paths. Model and optional image-generator assets are additional requirements.
- **Platforms:** The documented shell/CUDA/distributed research path targets a compatible GPU environment. Native macOS/MPS and a complete Windows matrix are not established.

### License, model weights & costs

The complete top-level Apache-2.0 software terms were reviewed and archived today; model/dependency/host terms remain separate. [Source 1](https://github.com/hpcaitech/Open-Sora/blob/main/LICENSE) [Source 2](https://github.com/hpcaitech/Open-Sora/blob/main/README.md)

- **Code:** Apache-2.0
- **Weights:** Top-level code is Apache-2.0, but the complete LICENSE also includes third-party notices and Tencent Hunyuan community terms with geographic, use and commercial restrictions. These dependencies/weights are not all OSI-licensed.
- **Commercial:** The main Apache-2.0 code grant permits commercial use under its notice/source and other conditions. Model, component, asset and hosted-service permission is separate. Top-level code is Apache-2.0, but the complete LICENSE also includes third-party notices and Tencent Hunyuan community terms with geographic, use and commercial restrictions. These dependencies/weights are not all OSI-licensed.
- **Cost:** Large GPU/cloud compute and storage are practical costs. The main code license does not settle licensing costs or commercial rights for every model component.

### Why it merits attention

Assessment: explicit inference/training configurations and stated benchmark circumstances are useful for researchers. No quality or performance benchmark was reproduced here. [Source 1](https://github.com/hpcaitech/Open-Sora/blob/main/README.md)

### Limitations

Substantial resources and a complex model stack make this less turnkey. Do not label the entire default pipeline unrestricted open source based only on GitHub Apache metadata. [Source 1](https://github.com/hpcaitech/Open-Sora/blob/main/README.md) [Source 2](https://github.com/hpcaitech/Open-Sora/blob/main/LICENSE)

### Get the tool

- [Repository](https://github.com/hpcaitech/Open-Sora)
- [Documentation](https://github.com/hpcaitech/Open-Sora/blob/main/README.md)

## CogVideoX

Video, animation & film · Storyboarding, narrative & comics

First complete guide for a previously screened discovery; documentation checked today. Repository created 2022-05-29; current source metadata is a discovery signal, not evidence of a significant product upgrade.

### How it uses AI

CogVideoX models generate video from textual or visual guidance, supporting experimental shots and animation concepts. [Source](https://github.com/zai-org/CogVideo/blob/main/README.md)

### Introduction

A text/image-to-video model family with Diffusers and SAT implementations, downloadable checkpoints and local demos. [Source 1](https://github.com/zai-org/CogVideo/blob/main/README.md)

### What it is good for

Create short narrative/concept shots and compare prompt or conditioning choices through a reproducible model script. [Source 1](https://github.com/zai-org/CogVideo/blob/main/README.md)

### Demo & examples

The README includes versioned galleries, a CLI demo and linked local/Hugging Face Gradio demos. [Source 1](https://github.com/zai-org/CogVideo/blob/main/README.md)

### Install

Documentation-based setup route; commands are examples from the project and were not executed during this review. [Source 1](https://github.com/zai-org/CogVideo/blob/main/README.md)

1. Use Python 3.10–3.12 and install requirements for the chosen Diffusers/SAT route.
2. Select the exact model version and its license before download.
3. Follow the corresponding inference/cli_demo.py documentation and begin with a short sample.

```sh
pip install -r requirements.txt
```

### First project

Begin with a small, permitted sample and inspect the result. [Source 1](https://github.com/zai-org/CogVideo/blob/main/README.md)

1. Choose the text or image-conditioned model and supply a permitted input.
2. Generate a short draft using its documented frame count and precision.
3. Compare motion/consistency and keep the seed/settings with the selected clip.
### Hardware & software

Published requirements and explicit documentation gaps follow. [Source 1](https://github.com/zai-org/CogVideo/blob/main/README.md)

- **Hardware:** The README gives model/backend-specific GPU figures: optimized Diffusers 2B examples reach about 4 GB FP16; 1.5 variants start at higher figures. Footnoted offload/tiling/quantization settings matter. Universal RAM/storage floors are not stated.
- **Software:** Python 3.10–3.12, matching PyTorch/Diffusers or SAT dependencies and selected weights. Advanced quantization requires its separately documented torchao/CUDA compatibility.
- **Platforms:** The primary local examples are GPU-oriented. Windows/cloud community guidance is linked; native macOS/MPS or mobile support for the full stack is not established by this review.

### License, model weights & costs

The complete top-level Apache-2.0 software terms were reviewed and archived today; model/dependency/host terms remain separate. [Source 1](https://github.com/zai-org/CogVideo/blob/main/LICENSE) [Source 2](https://github.com/zai-org/CogVideo/blob/main/README.md) [Source 3](https://huggingface.co/THUDM/CogVideoX-5b/blob/main/LICENSE)

- **Code:** Apache-2.0
- **Weights:** Apache-2.0 code and explicitly Apache-2.0 CogVideoX-2B weights. 5B and other checkpoint variants use separate CogVideoX model terms; do not extend 2B permission to them.
- **Commercial:** The main Apache-2.0 code grant permits commercial use under its notice/source and other conditions. Model, component, asset and hosted-service permission is separate. Apache-2.0 code and explicitly Apache-2.0 CogVideoX-2B weights. 5B and other checkpoint variants use separate CogVideoX model terms; do not extend 2B permission to them.
- **Cost:** Local/rented GPU and storage costs; optional hosted demos/providers have their own limits and terms.

### Why it merits attention

Assessment: explicit version/precision distinctions and a permissive 2B model option make this a useful baseline comparison. No model output was tested hands-on. [Source 1](https://github.com/zai-org/CogVideo/blob/main/README.md)

### Limitations

Low-memory figures depend on specific optimizations and may be slow. Frame/resolution limits, prompt adherence and artifacts need model-specific evaluation. [Source 1](https://github.com/zai-org/CogVideo/blob/main/README.md) [Source 2](https://github.com/zai-org/CogVideo/blob/main/LICENSE) [Source 3](https://huggingface.co/THUDM/CogVideoX-5b/blob/main/LICENSE)

### Get the tool

- [Repository](https://github.com/zai-org/CogVideo)
- [Documentation](https://github.com/zai-org/CogVideo/blob/main/README.md)

## RIFE ncnn Vulkan

Video, animation & film · Editing, captions & post-production · Mobile, edge & on-device creation

First complete guide for a previously screened discovery; documentation checked today. Repository created 2020-11-22; current source metadata is a discovery signal, not evidence of a significant product upgrade.

### How it uses AI

Learned optical-flow/frame-interpolation inference creates intermediate video frames through a Vulkan-oriented desktop utility. [Source](https://github.com/nihui/rife-ncnn-vulkan/blob/master/README.md)

### Introduction

A portable neural frame-interpolation implementation using ncnn and Vulkan rather than requiring a Python/CUDA application stack. [Source 1](https://github.com/nihui/rife-ncnn-vulkan/blob/master/README.md)

### What it is good for

Create intermediate frames for a short clip, smooth an animation preview or explore retiming before final editing. [Source 1](https://github.com/nihui/rife-ncnn-vulkan/blob/master/README.md)

### Demo & examples

The README demonstrates two-frame interpolation and a complete FFmpeg extraction/interpolation/re-encoding workflow. [Source 1](https://github.com/nihui/rife-ncnn-vulkan/blob/master/README.md)

### Install

Documentation-based setup route; commands are examples from the project and were not executed during this review. [Source 1](https://github.com/nihui/rife-ncnn-vulkan/blob/master/README.md)

1. Download the official release for the host platform; binaries and model files are included.
2. Ensure compatible graphics drivers and add FFmpeg/ffprobe for a full video workflow.
3. Start with two supplied or permitted frames before processing a full sequence.

```sh
./rife-ncnn-vulkan -0 0.jpg -1 1.jpg -o 01.jpg
```

### First project

Begin with a small, permitted sample and inspect the result. [Source 1](https://github.com/nihui/rife-ncnn-vulkan/blob/master/README.md)

1. Inspect the source frame rate and preserve the source audio separately.
2. Decode to frames, interpolate and re-encode with the intended new frame rate.
3. Watch difficult motion/cuts at full resolution before using the output.
### Hardware & software

Published requirements and explicit documentation gaps follow. [Source 1](https://github.com/nihui/rife-ncnn-vulkan/blob/master/README.md)

- **Hardware:** Release notes target Intel/AMD/NVIDIA GPUs with Vulkan; CPU/multi-device options are documented. Universal RAM, VRAM and temporary-frame storage minima are not stated.
- **Software:** Portable ncnn/Vulkan runtime and included RIFE models; CUDA and PyTorch are not required. FFmpeg/ffprobe are needed for the documented whole-video example.
- **Platforms:** Windows, Linux and macOS executables are explicitly offered; macOS source builds mention MoltenVK. No mobile app/platform guarantee follows from the lightweight engine.

### License, model weights & costs

The complete top-level MIT software terms were reviewed and archived today; model/dependency/host terms remain separate. [Source 1](https://github.com/nihui/rife-ncnn-vulkan/blob/master/LICENSE) [Source 2](https://github.com/nihui/rife-ncnn-vulkan/blob/master/README.md)

- **Code:** MIT
- **Weights:** MIT software. Included model provenance and any substituted RIFE model/dependency/FFmpeg build keep their own terms; the main MIT file is not an audio/video rights grant.
- **Commercial:** The main MIT code grant permits commercial use under its notice/source and other conditions. Model, component, asset and hosted-service permission is separate. MIT software. Included model provenance and any substituted RIFE model/dependency/FFmpeg build keep their own terms; the main MIT file is not an audio/video rights grant.
- **Cost:** No required paid interpolation service; local compute and potentially large temporary frame storage are the operating costs.

### Why it merits attention

Assessment: packaged cross-platform binaries and a concrete full-video recipe lower setup friction. No interpolation artifacts or hardware performance were tested here. [Source 1](https://github.com/nihui/rife-ncnn-vulkan/blob/master/README.md)

### Limitations

Interpolation can hallucinate motion and fail on occlusion or scene cuts. Re-encoding and audio/frame-rate handling need careful checking; it does not recover authentic missing captured frames. [Source 1](https://github.com/nihui/rife-ncnn-vulkan/blob/master/README.md) [Source 2](https://github.com/nihui/rife-ncnn-vulkan/blob/master/LICENSE)

### Get the tool

- [Repository](https://github.com/nihui/rife-ncnn-vulkan)
- [Documentation](https://github.com/nihui/rife-ncnn-vulkan/blob/master/README.md)

## WebLLM

Browser tools & web media · Storyboarding, narrative & comics · Interactive, immersive & live media · Physical, robotic & kinetic installations

First complete guide for a previously screened discovery; documentation checked today. Repository created 2023-04-13; current source metadata is a discovery signal, not evidence of a significant product upgrade.

### How it uses AI

WebGPU language-model inference can run a browser-based creative-writing, story or interactive-character assistant; selected models retain their own terms. [Source](https://github.com/mlc-ai/web-llm/blob/main/README.md)

### Introduction

A WebGPU-accelerated language-model runtime that performs inference in a browser tab with an API-shaped JavaScript interface. [Source 1](https://github.com/mlc-ai/web-llm/blob/main/README.md)

### What it is good for

Build a local browser narrative character, interactive story prompt or text-driven installation using a selected appropriately licensed language model. [Source 1](https://github.com/mlc-ai/web-llm/blob/main/README.md)

### Demo & examples

WebLLM Chat and official JavaScript examples demonstrate the runtime; they do not establish that every model or browser/device combination works. [Source 1](https://github.com/mlc-ai/web-llm/blob/main/README.md) [Source 2](https://chat.webllm.ai/)

### Install

Documentation-based setup route; commands are examples from the project and were not executed during this review. [Source 1](https://github.com/mlc-ai/web-llm/blob/main/README.md)

1. Try the official browser demo on a WebGPU-capable device.
2. For your own application, install the npm runtime and follow the example engine initialization.
3. Choose a supported model with reviewed terms and show download/loading progress in your UI.

```sh
npm install @mlc-ai/web-llm
```

### First project

Begin with a small, permitted sample and inspect the result. [Source 1](https://github.com/mlc-ai/web-llm/blob/main/README.md)

1. Initialize an engine with the selected model ID and an initialization progress callback.
2. Send a short narrative prompt and stream the response into your application.
3. Test model loading, cached behavior and output on each intended browser/device.
### Hardware & software

Published requirements and explicit documentation gaps follow. [Source 1](https://github.com/mlc-ai/web-llm/blob/main/README.md)

- **Hardware:** Requires a device/browser supporting the required WebGPU features and enough memory for the selected model. There is no universal RAM, VRAM or download/storage minimum.
- **Software:** JavaScript/TypeScript web application, @mlc-ai/web-llm, WebGPU and MLC-format weights. Worker/service-worker examples are provided; source/build version requirements are model/application specific.
- **Platforms:** In-browser runtime rather than a native desktop-model installer. Windows/macOS/Linux/mobile support depends on actual browser WebGPU features, driver and model capacity; no blanket support claim is made.

### License, model weights & costs

The complete top-level Apache-2.0 software terms were reviewed and archived today; model/dependency/host terms remain separate. [Source 1](https://github.com/mlc-ai/web-llm/blob/main/LICENSE) [Source 2](https://github.com/mlc-ai/web-llm/blob/main/README.md)

- **Code:** Apache-2.0
- **Weights:** Apache-2.0 runtime. Supported model families include models with different/custom licenses; inspect the exact checkpoint. API compatibility does not require using a paid OpenAI endpoint.
- **Commercial:** The main Apache-2.0 code grant permits commercial use under its notice/source and other conditions. Model, component, asset and hosted-service permission is separate. Apache-2.0 runtime. Supported model families include models with different/custom licenses; inspect the exact checkpoint. API compatibility does not require using a paid OpenAI endpoint.
- **Cost:** The documented runtime can infer locally without a mandatory paid model API. Bandwidth, local hardware and optional application hosting are costs.

### Why it merits attention

Assessment: client-side inference and structured/streamed outputs are useful for interactive media deployment. No browser model was loaded during this review. [Source 1](https://github.com/mlc-ai/web-llm/blob/main/README.md)

### Limitations

Large downloads and browser/device memory limits affect usability. Language output can be wrong; the runtime does not itself generate images, voices or a finished narrative design. [Source 1](https://github.com/mlc-ai/web-llm/blob/main/README.md) [Source 2](https://github.com/mlc-ai/web-llm/blob/main/LICENSE)

### Get the tool

- [Repository](https://github.com/mlc-ai/web-llm)
- [Documentation](https://github.com/mlc-ai/web-llm/blob/main/README.md)
- [Demo](https://chat.webllm.ai/)

## Web Stable Diffusion

Browser tools & web media · Images & design · Interactive, immersive & live media · Creative learning & authoring

First complete guide for a previously screened discovery; documentation checked today. Repository created 2023-03-06; current source metadata is a discovery signal, not evidence of a significant product upgrade.

### How it uses AI

Browser GPU diffusion inference generates images from text without assuming a remote hosted generation API. [Source](https://github.com/mlc-ai/web-stable-diffusion/blob/main/README.md)

### Introduction

An early machine-learning-compilation prototype that runs Stable Diffusion image generation inside a WebGPU browser. [Source 1](https://github.com/mlc-ai/web-stable-diffusion/blob/main/README.md)

### What it is good for

Study client-side generative-image interfaces or prototype an installation that performs compatible inference on the viewer device. [Source 1](https://github.com/mlc-ai/web-stable-diffusion/blob/main/README.md)

### Demo & examples

The official web demo and walkthrough notebook expose a browser-generation example. This is a first detailed baseline for an older prototype, not a new 2026 release. [Source 1](https://github.com/mlc-ai/web-stable-diffusion/blob/main/README.md) [Source 2](https://websd.mlc.ai/)

### Install

Documentation-based setup route; commands are examples from the project and were not executed during this review. [Source 1](https://github.com/mlc-ai/web-stable-diffusion/blob/main/README.md)

1. Inspect the official demo first using a compatible WebGPU browser.
2. For local development, follow the walkthrough for compiling the model/runtime and building the web assets.
3. Review the historical toolchain/browser instructions against current dependencies before attempting a build.
### First project

Begin with a small, permitted sample and inspect the result. [Source 1](https://github.com/mlc-ai/web-stable-diffusion/blob/main/README.md)

1. Enter a simple prompt in the compatible demo and let the model load.
2. For an authored interface, use the published compiled-runtime flow and test one device/browser first.
3. Inspect output and loading/fallback behavior before using it in a public installation.
### Hardware & software

Published requirements and explicit documentation gaps follow. [Source 1](https://github.com/mlc-ai/web-stable-diffusion/blob/main/README.md)

- **Hardware:** WebGPU-compatible GPU/browser and capacity for model/runtime downloads. Universal RAM, VRAM and storage minima are not documented in the inspected README.
- **Software:** Advanced source deployment uses MLC/TVM, Emscripten, Rust/wasm-pack and a Jekyll site. The README includes historical Chrome Canary guidance, which is not a verified current compatibility matrix.
- **Platforms:** The README includes native and web compilation routes. Browser access alone does not confirm native macOS, Windows, mobile or headset support for this particular model build.

### License, model weights & costs

The complete top-level Apache-2.0 software terms were reviewed and archived today; model/dependency/host terms remain separate. [Source 1](https://github.com/mlc-ai/web-stable-diffusion/blob/main/LICENSE) [Source 2](https://github.com/mlc-ai/web-stable-diffusion/blob/main/README.md)

- **Code:** Apache-2.0
- **Weights:** Apache-2.0 project code. Stable Diffusion checkpoint terms are separate; compiled weights retain those terms rather than becoming Apache-licensed.
- **Commercial:** The main Apache-2.0 code grant permits commercial use under its notice/source and other conditions. Model, component, asset and hosted-service permission is separate. Apache-2.0 project code. Stable Diffusion checkpoint terms are separate; compiled weights retain those terms rather than becoming Apache-licensed.
- **Cost:** Local/client compute and model-download bandwidth, plus optional web hosting. No required paid inference API in the browser example.

### Why it merits attention

Assessment: an inspectable early example of browser diffusion is useful for creative learning. It is less turnkey than a current packaged editor and was not tested here. [Source 1](https://github.com/mlc-ai/web-stable-diffusion/blob/main/README.md)

### Limitations

Historical dependency/browser instructions can be stale. Compatibility, performance and maintenance readiness need validation before adopting it for a live show. [Source 1](https://github.com/mlc-ai/web-stable-diffusion/blob/main/README.md) [Source 2](https://github.com/mlc-ai/web-stable-diffusion/blob/main/LICENSE)

### Get the tool

- [Repository](https://github.com/mlc-ai/web-stable-diffusion)
- [Documentation](https://github.com/mlc-ai/web-stable-diffusion/blob/main/README.md)
- [Demo](https://websd.mlc.ai/)

## Mixar

3D, reconstruction & assets · Images & design · Games & production pipelines · Fashion, textiles & wearable media

First complete guide for a previously screened discovery; documentation checked today. Repository created 2026-05-18; current source metadata is a discovery signal, not evidence of a significant product upgrade.

### How it uses AI

The Blender-derived application connects AI asset generation/editing to a 3D creative workspace; its closed hosted backend is separately identified. [Source](https://github.com/Mixar-AI/mixar-app/blob/main/README.md)

### Introduction

A Blender 5.2 fork with AI scene control, integrated 3D-generation providers and layered texture painting. The desktop source is open; its hosted AI backend is closed. [Source 1](https://github.com/Mixar-AI/mixar-app/blob/main/README.md)

### What it is good for

Explore prompt-driven scene tasks, reference moodboards and texture/UV work while retaining Blender editing controls. [Source 1](https://github.com/Mixar-AI/mixar-app/blob/main/README.md)

### Demo & examples

The README describes the desktop workflow and links the official application; no live AI task was run during this review. [Source 1](https://github.com/Mixar-AI/mixar-app/blob/main/README.md)

### Install

Documentation-based setup route; commands are examples from the project and were not executed during this review. [Source 1](https://github.com/Mixar-AI/mixar-app/blob/main/README.md)

1. Follow the platform-specific Blender 5.2 build prerequisites and add Python 3.11+/rsync.
2. Clone the official repository with submodules/LFS assets and configure the provided environment template privately.
3. Build the app, then sign into Mixar for AI features or configure its documented BYOK provider route.
### First project

Begin with a small, permitted sample and inspect the result. [Source 1](https://github.com/Mixar-AI/mixar-app/blob/main/README.md)

1. Open a small scene and use the layered painting controls first.
2. With an authorized account/provider, request a bounded scene or texture task.
3. Inspect the resulting mesh, UVs/materials and export only a reviewed asset.
### Hardware & software

Published requirements and explicit documentation gaps follow. [Source 1](https://github.com/Mixar-AI/mixar-app/blob/main/README.md)

- **Hardware:** The README defers base hardware/build requirements to Blender. No Mixar-specific minimum RAM, VRAM or full build/model storage requirement is stated.
- **Software:** Blender 5.2 build toolchain, Python >=3.11, rsync, submodules/LFS and the Mixar overlay. AI features require hosted-backend authentication even though non-AI painting/Blender features can run without it.
- **Platforms:** Source build instructions cover macOS, Linux and Windows; Windows may need WSL/Cygwin for rsync. This review did not verify binaries or equal feature parity on those platforms.

### License, model weights & costs

The complete top-level GPL-3.0-or-later software terms were reviewed and archived today; model/dependency/host terms remain separate. [Source 1](https://github.com/Mixar-AI/mixar-app/blob/main/LICENSE) [Source 2](https://github.com/Mixar-AI/mixar-app/blob/main/README.md)

- **Code:** GPL-3.0-or-later
- **Weights:** Mixar original code is GPL-3.0-or-later; Blender-derived files and third-party paint code have their documented GPL notices. Brand assets have separate restrictions. AI backend/model/provider code and terms are separate.
- **Commercial:** The main GPL-3.0-or-later code grant permits commercial use under its notice/source and other conditions. Model, component, asset and hosted-service permission is separate. Mixar original code is GPL-3.0-or-later; Blender-derived files and third-party paint code have their documented GPL notices. Brand assets have separate restrictions. AI backend/model/provider code and terms are separate.
- **Cost:** Open desktop code does not make AI calls free: Mixar credits or BYOK provider usage apply. No current prices are asserted.

### Why it merits attention

Assessment: an editable Blender scene and layered materials provide substantive creative controls beyond a simple prompt wrapper. AI output quality and build/runtime behavior were not tested. [Source 1](https://github.com/Mixar-AI/mixar-app/blob/main/README.md)

### Limitations

This is not a fully open, offline AI stack. Hosted generation, provider restrictions and asset/trademark permissions must be evaluated independently of the desktop GPL license. [Source 1](https://github.com/Mixar-AI/mixar-app/blob/main/README.md) [Source 2](https://github.com/Mixar-AI/mixar-app/blob/main/LICENSE)

### Get the tool

- [Repository](https://github.com/Mixar-AI/mixar-app)
- [Documentation](https://github.com/Mixar-AI/mixar-app/blob/main/README.md)

## PotionUI

Images & design · Video, animation & film · Audio, music & voice · Browser tools & web media

First complete guide for a previously screened discovery; documentation checked today. Repository created 2026-08-24; current source metadata is a discovery signal, not evidence of a significant product upgrade.

### How it uses AI

The self-hosted studio orchestrates local learned image, video and music generation with model-specific controls, presets and optional remote GPU workers. [Source](https://github.com/PotionUI/PotionUI/blob/master/README.md)

### Introduction

An alpha multi-model creative UI for local GPU image/video/audio generation, with collections, workflows and remote workers. [Source 1](https://github.com/PotionUI/PotionUI/blob/master/README.md)

### What it is good for

Keep reusable generation presets and assets together, or let a lightweight UI dispatch work to a separate GPU machine. [Source 1](https://github.com/PotionUI/PotionUI/blob/master/README.md)

### Demo & examples

The README shows generation, collections, a video director and assistant/MCP surfaces; its doctor/start commands are the documented local on-ramp. [Source 1](https://github.com/PotionUI/PotionUI/blob/master/README.md)

### Install

Documentation-based setup route; commands are examples from the project and were not executed during this review. [Source 1](https://github.com/PotionUI/PotionUI/blob/master/README.md)

1. Choose local GPU, hybrid, remote-client or worker mode from the install table.
2. Use the tested Linux/NVIDIA prerequisites or the explicitly experimental native Windows path.
3. Run the project doctor and start command, then install a model with reviewed terms.

```sh
./potionui doctor
```


```sh
./potionui start
```

### First project

Begin with a small, permitted sample and inspect the result. [Source 1](https://github.com/PotionUI/PotionUI/blob/master/README.md)

1. Load one model/preset and generate a small permitted sample.
2. Save useful settings as a session and organize the result with tags/collections.
3. For remote mode, connect a separately configured worker; CPU-only client installation does not mean CPU generation.
### Hardware & software

Published requirements and explicit documentation gaps follow. [Source 1](https://github.com/PotionUI/PotionUI/blob/master/README.md)

- **Hardware:** Published local SDXL floor: 8 GB VRAM +16 GB RAM. Larger video/audio families need more. A single total storage minimum is not given.
- **Software:** Python 3.12; Node >=18 for most presets, with Node 20 in the native Windows prerequisites. The dependency stack is CUDA-only and has no native MPS backend.
- **Platforms:** Linux x86_64/NVIDIA is tested; native Windows is experimental. WSL2 is expected but explicitly unverified in the matrix; Docker is documented. Native macOS/AMD local generation is not supported by that stack.

### License, model weights & costs

The complete top-level GPL-3.0 software terms were reviewed and archived today; model/dependency/host terms remain separate. [Source 1](https://github.com/PotionUI/PotionUI/blob/master/LICENSE) [Source 2](https://github.com/PotionUI/PotionUI/blob/master/README.md)

- **Code:** GPL-3.0
- **Weights:** GPL-3.0 software. Each installed generator/LoRA/checkpoint and any external assistant/model provider retains its own license and service terms.
- **Commercial:** The main GPL-3.0 code grant permits commercial use under its notice/source and other conditions. Model, component, asset and hosted-service permission is separate. GPL-3.0 software. Each installed generator/LoRA/checkpoint and any external assistant/model provider retains its own license and service terms.
- **Cost:** Local GPU and model storage; remote workers can incur hardware/cloud costs. Optional external assistant providers may charge separately.

### Why it merits attention

Assessment: explicit client/worker distinction and a stated small-model floor make deployment decisions clearer. Alpha feature claims and output quality were not tested hands-on. [Source 1](https://github.com/PotionUI/PotionUI/blob/master/README.md)

### Limitations

Expect breaking changes. Equal platform consideration does not mean equal support; a browser frontend on a Mac still needs a compatible generation backend. [Source 1](https://github.com/PotionUI/PotionUI/blob/master/README.md) [Source 2](https://github.com/PotionUI/PotionUI/blob/master/LICENSE)

### Get the tool

- [Repository](https://github.com/PotionUI/PotionUI)
- [Documentation](https://github.com/PotionUI/PotionUI/blob/master/README.md)

## Generator Assets

Games & production pipelines · 3D, reconstruction & assets · Audio, music & voice · Video, animation & film

First complete guide for a previously screened discovery; documentation checked today. Repository created 2026-08-25; current source metadata is a discovery signal, not evidence of a significant product upgrade.

### How it uses AI

Local Vulkan/GGUF neural inference is orchestrated with Blender and media utilities to create images, video, music and experimental game assets without a required cloud generation service. [Source](https://github.com/laurentvv/generator-assets/blob/main/README.md)

### Introduction

A headless local media orchestrator connecting diffusion, language/audio engines and Blender to game-asset export recipes. [Source 1](https://github.com/laurentvv/generator-assets/blob/main/README.md)

### What it is good for

Prototype texture/material, mesh, environment, sound or video assets and retain a scripted generation recipe for a game project. [Source 1](https://github.com/laurentvv/generator-assets/blob/main/README.md)

### Demo & examples

The README links an author demo and documents Godot .tres/.gdshader, GLB and audio/video workflow examples. These outputs were not produced in this review. [Source 1](https://github.com/laurentvv/generator-assets/blob/main/README.md)

### Install

Documentation-based setup route; commands are examples from the project and were not executed during this review. [Source 1](https://github.com/laurentvv/generator-assets/blob/main/README.md)

1. Clone the real laurentvv/generator-assets repository; the README still contains a placeholder votre-compte clone example.
2. Use uv sync and set up the documented compatible engines/model packs for the target platform.
3. Configure actual local tool/model paths and start with one lightweight workflow rather than every advertised model.

```sh
uv sync
```

### First project

Begin with a small, permitted sample and inspect the result. [Source 1](https://github.com/laurentvv/generator-assets/blob/main/README.md)

1. Choose a small texture/image or other documented asset recipe with permitted inputs.
2. Generate and inspect the asset, then export its documented engine format.
3. Validate material, scale, looping and performance in your actual Godot/Blender project.
### Hardware & software

Published requirements and explicit documentation gaps follow. [Source 1](https://github.com/laurentvv/generator-assets/blob/main/README.md)

- **Hardware:** The README reports validation on AMD RX 6950 XT 16 GB and recommends smaller packs for 8–12 GB GPUs. Other workflows have separate memory placements. Universal RAM and total storage minima are not specified.
- **Software:** Python >=3.12/uv; selected C++ inference engines, model files, FFmpeg and optionally Blender 5.x. Vulkan is documented for Windows/Linux and Metal for macOS routes.
- **Platforms:** Windows 10/11, Linux x64 and macOS setup routes are published. Documented author validation and scripts do not establish parity for every model/platform; some configuration examples remain Windows-workstation-specific.

### License, model weights & costs

The complete top-level MIT software terms were reviewed and archived today; model/dependency/host terms remain separate. [Source 1](https://github.com/laurentvv/generator-assets/blob/main/LICENSE) [Source 2](https://github.com/laurentvv/generator-assets/blob/main/README.md)

- **Code:** MIT
- **Weights:** MIT orchestrator code. FLUX.1-dev weights are explicitly non-commercial; other weights and engines have their own terms. The authors private custom nonfree FFmpeg build is not a distributable part of the open recipe.
- **Commercial:** The main MIT code grant permits commercial use under its notice/source and other conditions. Model, component, asset and hosted-service permission is separate. MIT orchestrator code. FLUX.1-dev weights are explicitly non-commercial; other weights and engines have their own terms. The authors private custom nonfree FFmpeg build is not a distributable part of the open recipe.
- **Cost:** Local compute, large model storage and any separately licensed weights/components. No mandatory paid generation API is specified for the local recipes.

### Why it merits attention

Assessment: inspectable sequential workflows and explicit engine formats are useful for technical artists. Broad engine-ready/performance claims are author claims, not our output validation. [Source 1](https://github.com/laurentvv/generator-assets/blob/main/README.md)

### Limitations

A placeholder clone URL and workstation-specific defaults require care. Generated assets still need artistic, license and engine checks; procedural utility stages are not themselves AI generators. [Source 1](https://github.com/laurentvv/generator-assets/blob/main/README.md) [Source 2](https://github.com/laurentvv/generator-assets/blob/main/LICENSE)

### Get the tool

- [Repository](https://github.com/laurentvv/generator-assets)
- [Documentation](https://github.com/laurentvv/generator-assets/blob/main/README.md)

## Open Reality

Spatial audio & volumetric media · Photogrammetry, scanning & neural rendering · WebXR, VR & AR · Interactive, immersive & live media

First complete guide for a previously screened discovery; documentation checked today. Repository created 2026-09-01; current source metadata is a discovery signal, not evidence of a significant product upgrade.

### How it uses AI

A learned image-to-3D reconstruction backend produces spatial scenes that the open application can present or use; VGGT terms are separately restricted. [Source](https://github.com/reality-opened/openreality/blob/main/README.md)

### Introduction

An open MCP/backend workflow for turning ordinary video into AI-queryable 3D scenes with measurement, calibration and exports. [Source 1](https://github.com/reality-opened/openreality/blob/main/README.md)

### What it is good for

Prototype a spatial scene explorer or installation from a phone capture; distinguish mock/simulator demonstrations from actual reconstruction. [Source 1](https://github.com/reality-opened/openreality/blob/main/README.md)

### Demo & examples

The repository shows an offline simulator session and credits a separate VGGT-SLAM reconstruction demo. The simulator uses fixtures, not a live scan. [Source 1](https://github.com/reality-opened/openreality/blob/main/README.md)

### Install

Documentation-based setup route; commands are examples from the project and were not executed during this review. [Source 1](https://github.com/reality-opened/openreality/blob/main/README.md) [Source 2](https://github.com/reality-opened/openreality/blob/main/server/docs/self-hosting.md)

1. Use the MCP client setup for a hosted or explicitly configured self-hosted backend.
2. For local reconstruction, follow the self-host guide with its CUDA/Python stack and separately licensed VGGT dependency.
3. Use the simulator first for UI/tool integration without claiming reconstructed geometry.

```sh
npx -y openreality-mcp serve
```

### First project

Begin with a small, permitted sample and inspect the result. [Source 1](https://github.com/reality-opened/openreality/blob/main/README.md)

1. Upload a permitted room video to an actual configured reconstruction server.
2. Inspect the scene and calibrate using a known real distance before asking for measurements in metres.
3. Export a supported scene/data format and validate it in the intended application.
### Hardware & software

Published requirements and explicit documentation gaps follow. [Source 1](https://github.com/reality-opened/openreality/blob/main/README.md) [Source 2](https://github.com/reality-opened/openreality/blob/main/server/docs/self-hosting.md)

- **Hardware:** Self-hosting recommends a CUDA GPU with >=24 GB VRAM and >=48 GB host RAM. The simulator needs no reconstruction GPU. Total scan/model storage is not stated as one minimum.
- **Software:** Self-host guide: Python 3.11, torch 2.3.1/torchvision 0.18.1, server/core requirements and a pinned external VGGT backbone. The MCP client is a separate Node/npm component.
- **Platforms:** The local GPU guide is CUDA-oriented; native macOS/MPS and mobile reconstruction are not established. A phone supplies video and the browser is a client, not proof of on-device inference or WebXR output.

### License, model weights & costs

The complete top-level BSD-2-Clause software terms were reviewed and archived today; model/dependency/host terms remain separate. [Source 1](https://github.com/reality-opened/openreality/blob/main/LICENSE) [Source 2](https://github.com/reality-opened/openreality/blob/main/README.md)

- **Code:** BSD-2-Clause
- **Weights:** BSD-2-Clause application source. The README explicitly says self-hosted VGGT model/code is CC-BY-NC; that restricted dependency is excluded from any claim of an unrestricted open-source AI stack. Hosted commercial licensing is separate.
- **Commercial:** The main BSD-2-Clause code grant permits commercial use under its notice/source and other conditions. Model, component, asset and hosted-service permission is separate. BSD-2-Clause application source. The README explicitly says self-hosted VGGT model/code is CC-BY-NC; that restricted dependency is excluded from any claim of an unrestricted open-source AI stack. Hosted commercial licensing is separate.
- **Cost:** Local/rented GPU and scan storage, or separately governed hosted/Modal usage. No verified current hosted price is assumed.

### Why it merits attention

Assessment: calibration and honest relative units are useful safeguards for spatial creative experiments. Neither reconstruction nor the simulator was run here. [Source 1](https://github.com/reality-opened/openreality/blob/main/README.md)

### Limitations

Some export/live-scan lanes are explicitly outside the self-host v1 path. Scan geometry, privacy and real units need checks; source openness does not clear the non-commercial backbone license. [Source 1](https://github.com/reality-opened/openreality/blob/main/README.md) [Source 2](https://github.com/reality-opened/openreality/blob/main/LICENSE)

### Get the tool

- [Repository](https://github.com/reality-opened/openreality)
- [Documentation](https://github.com/reality-opened/openreality/blob/main/README.md)

## Logo Design Skill

Vector graphics, illustration & textures · Typography, fonts & layout · Creative publishing & presentation

First complete guide for a previously screened discovery; documentation checked today. Repository created 2026-09-26; current source metadata is a discovery signal, not evidence of a significant product upgrade.

### How it uses AI

An AI coding-agent workflow develops a logo/identity from a brief with editable vector/code outputs and visual iteration. [Source](https://github.com/kaankiziltug/logo-design-skill/blob/main/README.md)

### Introduction

An open agent workflow and Python toolset for designing, testing and delivering SVG identity concepts and brand assets. [Source 1](https://github.com/kaankiziltug/logo-design-skill/blob/main/README.md)

### What it is good for

Use an AI design assistant to explore a fictional brand mark, compare small-size/one-color behavior and export an editable identity kit. [Source 1](https://github.com/kaankiziltug/logo-design-skill/blob/main/README.md)

### Demo & examples

The repository publishes fictional example briefs and concept/kit boards. Its real-logo reference collection is for study and has separate trademark rights. [Source 1](https://github.com/kaankiziltug/logo-design-skill/blob/main/README.md)

### Install

Documentation-based setup route; commands are examples from the project and were not executed during this review. [Source 1](https://github.com/kaankiziltug/logo-design-skill/blob/main/README.md)

1. Clone the skill source and copy the logo-design folder into a compatible agents documented skills location.
2. Use Python >=3.8 for the standard-library tools.
3. Install/use an available SVG renderer only if PNG/ICO output is needed.
### First project

Begin with a small, permitted sample and inspect the result. [Source 1](https://github.com/kaankiziltug/logo-design-skill/blob/main/README.md)

1. Provide a brand brief and ask the agent for SVG concepts and comparison sheets.
2. Inspect small sizes, monochrome and visual similarity; choose a direction.
3. Request the final editable kit and review all outputs and reference-asset rights.
### Hardware & software

Published requirements and explicit documentation gaps follow. [Source 1](https://github.com/kaankiziltug/logo-design-skill/blob/main/README.md)

- **Hardware:** No minimum CPU/GPU, RAM, VRAM or storage is documented. Local Python helpers do not require running the language model on the same host.
- **Software:** Python >=3.8; PNG/ICO rendering uses an available CairoSVG/rsvg/Inkscape/Chromium or macOS Quick Look backend. A compatible image-capable AI agent is needed for the documented self-review workflow.
- **Platforms:** Agent Skills format with Python helpers and several platform renderer alternatives. Actual support depends on the chosen host/renderer; a complete OS/version certification matrix is not supplied.

### License, model weights & costs

The complete top-level MIT software terms were reviewed and archived today; model/dependency/host terms remain separate. [Source 1](https://github.com/kaankiziltug/logo-design-skill/blob/main/LICENSE) [Source 2](https://github.com/kaankiziltug/logo-design-skill/blob/main/README.md)

- **Code:** MIT
- **Weights:** MIT text/scripts/templates. Real-world reference logos are trademarks of their owners and explicitly outside MIT, for reference/education only. Model/agent service terms are separate.
- **Commercial:** The main MIT code grant permits commercial use under its notice/source and other conditions. Model, component, asset and hosted-service permission is separate. MIT text/scripts/templates. Real-world reference logos are trademarks of their owners and explicitly outside MIT, for reference/education only. Model/agent service terms are separate.
- **Cost:** No license fee for the skill. The chosen agent/model host may require a subscription/API or local-model resources; optional design tools add their own costs.

### Why it merits attention

Assessment: editable SVG and concrete small-size/monochrome checks support a useful design iteration process. Example boards are author outputs, not independently tested results. [Source 1](https://github.com/kaankiziltug/logo-design-skill/blob/main/README.md)

### Limitations

AI concepts can resemble existing marks. The workflow does not provide trademark clearance, and its reference collection is not a freely licensed logo stock library. [Source 1](https://github.com/kaankiziltug/logo-design-skill/blob/main/README.md) [Source 2](https://github.com/kaankiziltug/logo-design-skill/blob/main/LICENSE)

### Get the tool

- [Repository](https://github.com/kaankiziltug/logo-design-skill)
- [Documentation](https://github.com/kaankiziltug/logo-design-skill/blob/main/README.md)

## ReelMimic

Video, animation & film · Storyboarding, narrative & comics · Computational art & creative coding

First complete guide for a previously screened discovery; documentation checked today. Repository created 2026-09-28; current source metadata is a discovery signal, not evidence of a significant product upgrade.

### How it uses AI

An AI-agent workflow reconstructs a reference short-form style as editable code-authored media and rendered video. [Source](https://github.com/edenfunf/reelmimic/blob/main/README.md)

### Introduction

An agent-driven 2D animation production app that analyzes a reference videos style and produces a reviewed multi-shot plan and rendered animation. [Source 1](https://github.com/edenfunf/reelmimic/blob/main/README.md)

### What it is good for

Create an original short animated narrative with a permitted visual reference, storyboard review and shot-level revisions. [Source 1](https://github.com/edenfunf/reelmimic/blob/main/README.md)

### Demo & examples

The README publishes three silent preview reels and screenshots of the local production interface; seven drawing engines have differing maturity. [Source 1](https://github.com/edenfunf/reelmimic/blob/main/README.md)

### Install

Documentation-based setup route; commands are examples from the project and were not executed during this review. [Source 1](https://github.com/edenfunf/reelmimic/blob/main/README.md)

1. Install Node >=22.18, Python >=3.10, FFmpeg, Chrome and a logged-in supported AI coding agent.
2. Clone the app and follow install/start instructions for the platform.
3. Open its local interface and run the documented doctor if dependencies are missing.
### First project

Begin with a small, permitted sample and inspect the result. [Source 1](https://github.com/edenfunf/reelmimic/blob/main/README.md)

1. Provide a permitted reference and a short original brief.
2. Inspect/adjust the storyboard, characters and style frames before production.
3. Review generated shots and timed comments; export only a checked, original animation.
### Hardware & software

Published requirements and explicit documentation gaps follow. [Source 1](https://github.com/edenfunf/reelmimic/blob/main/README.md)

- **Hardware:** No hard CPU/GPU, RAM, VRAM or storage minimum is published. The README estimates 1–3.5 hours for 30–60 seconds of animation; this is an author estimate, not a tested promise.
- **Software:** Node >=22.18, Python >=3.10, FFmpeg, Chrome, and logged-in Claude Code or Codex. Account usage limits can pause production.
- **Platforms:** Mostly tested on Windows according to the authors. macOS/Linux are expected to work but have less testing; they are not equally certified.

### License, model weights & costs

The complete top-level MIT software terms were reviewed and archived today; model/dependency/host terms remain separate. [Source 1](https://github.com/edenfunf/reelmimic/blob/main/LICENSE) [Source 2](https://github.com/edenfunf/reelmimic/blob/main/README.md)

- **Code:** MIT
- **Weights:** MIT application code. Agent service, renderer/style-engine and input footage/music rights remain separate; style analysis does not grant rights to copy a references assets.
- **Commercial:** The main MIT code grant permits commercial use under its notice/source and other conditions. Model, component, asset and hosted-service permission is separate. MIT application code. Agent service, renderer/style-engine and input footage/music rights remain separate; style analysis does not grant rights to copy a references assets.
- **Cost:** Uses the selected AI account and its limits; renderer/compute and any extra generated-media providers may incur costs. No current rate is asserted.

### Why it merits attention

Assessment: plan approval, independent shot review and visible revision logs provide useful production controls. No reel was generated by this scout. [Source 1](https://github.com/edenfunf/reelmimic/blob/main/README.md)

### Limitations

2D animation only, with newer styles less field-tested. The authors say it does not make live-action footage of real people. Reference access/rights and actual output quality require review. [Source 1](https://github.com/edenfunf/reelmimic/blob/main/README.md) [Source 2](https://github.com/edenfunf/reelmimic/blob/main/LICENSE)

### Get the tool

- [Repository](https://github.com/edenfunf/reelmimic)
- [Documentation](https://github.com/edenfunf/reelmimic/blob/main/README.md)

## Motion Video Kit

Video, animation & film · Computational art & creative coding · 3D, reconstruction & assets · Storyboarding, narrative & comics

First complete guide for a previously screened discovery; documentation checked today. Repository created 2026-09-27; current source metadata is a discovery signal, not evidence of a significant product upgrade.

### How it uses AI

Agent-authored motion code and render/review utilities turn a brief into editable animation and video output. [Source](https://github.com/echris6/motion-video-kit/blob/main/README.md)

### Introduction

An open skill, templates and measurement scripts for AI-assisted business motion films built with HTML/GSAP and optional Three.js. [Source 1](https://github.com/echris6/motion-video-kit/blob/main/README.md)

### What it is good for

Create or review a short product/explainer film with deterministic motion scenes, a visual critique loop and audio checks. [Source 1](https://github.com/echris6/motion-video-kit/blob/main/README.md)

### Demo & examples

The README describes two worked sample commercials and links case-study files, including a code-built Three.js phone film. [Source 1](https://github.com/echris6/motion-video-kit/blob/main/README.md)

### Install

Documentation-based setup route; commands are examples from the project and were not executed during this review. [Source 1](https://github.com/echris6/motion-video-kit/blob/main/README.md)

1. Clone the source and add its business-motion-film skill to a compatible agent, or use the plain context route.
2. Install FFmpeg/ffprobe with the ebur128 filter for measurement scripts.
3. For the optional component lab, add Node >=22 and the documented HyperFrames setup.
### First project

Begin with a small, permitted sample and inspect the result. [Source 1](https://github.com/echris6/motion-video-kit/blob/main/README.md)

1. Start with an original brief and build a short scene from the provided templates.
2. Inspect rendered frames and use independent visual critiques plus loudness/frozen-time checks.
3. Refine the scene and verify the final export before client or social use.
### Hardware & software

Published requirements and explicit documentation gaps follow. [Source 1](https://github.com/echris6/motion-video-kit/blob/main/README.md)

- **Hardware:** No minimum GPU, RAM, VRAM or storage is documented. Renderer complexity and any separately generated footage determine resources.
- **Software:** FFmpeg/ffprobe with ebur128; optional Node >=22/HyperFrames. The agent/model and renderer are separate dependencies rather than a bundled local AI model.
- **Platforms:** Renderer-agnostic principles and command-line helpers; the README does not certify every native OS. Use a documented renderer/agent host for the target platform.

### License, model weights & costs

The complete top-level MIT software terms were reviewed and archived today; model/dependency/host terms remain separate. [Source 1](https://github.com/echris6/motion-video-kit/blob/main/LICENSE) [Source 2](https://github.com/echris6/motion-video-kit/blob/main/README.md)

- **Code:** MIT
- **Weights:** MIT text, scripts and templates. Reference films remain their owners property and are linked rather than redistributed; generated-media models/services retain separate terms.
- **Commercial:** The main MIT code grant permits commercial use under its notice/source and other conditions. Model, component, asset and hosted-service permission is separate. MIT text, scripts and templates. Reference films remain their owners property and are linked rather than redistributed; generated-media models/services retain separate terms.
- **Cost:** The skill has no license fee. Agent/model accounts, rendering hardware and optional footage/music services can cost money.

### Why it merits attention

Assessment: editable code scenes and concrete visual/audio review criteria help technical motion designers. Author examples and market claims were not independently validated. [Source 1](https://github.com/echris6/motion-video-kit/blob/main/README.md)

### Limitations

A workflow/skill cannot guarantee professional quality. Its cited market prices are a September snapshot, and references or AI imagery must not be presented as proof of real client outcomes. [Source 1](https://github.com/echris6/motion-video-kit/blob/main/README.md) [Source 2](https://github.com/echris6/motion-video-kit/blob/main/LICENSE)

### Get the tool

- [Repository](https://github.com/echris6/motion-video-kit)
- [Documentation](https://github.com/echris6/motion-video-kit/blob/main/README.md)

## Sprocket

Editing, captions & post-production · Video, animation & film · AI agents for code-authored media production

First detailed guide in this library; documentation checked today. Repository created 2026-06-26; current source metadata is a discovery signal, not evidence of a significant product upgrade.

### How it uses AI

A connected AI agent can inspect media and issue actual undoable timeline edits through the editor’s local MCP interface. [Source](https://github.com/SprocketVideo/Sprocket/blob/main/README.md)

### Introduction

A non-destructive video editor with a local MCP interface through which an AI agent can inspect and change a real timeline. [Source 1](https://github.com/SprocketVideo/Sprocket/blob/main/README.md)

### What it is good for

Assemble a vertical exhibition teaser from your own clips, then ask an agent to trim, caption and rearrange shots while retaining editor undo. [Source 1](https://github.com/SprocketVideo/Sprocket/blob/main/README.md)

### Demo & examples

The official website and README show the editor. Release packages provide the practical demo; our assessment is documentation only. [Source 1](https://github.com/SprocketVideo/Sprocket/blob/main/README.md)

### Install

Documentation-based setup route; commands are examples from the project and were not executed during this review. [Source 1](https://github.com/SprocketVideo/Sprocket/blob/main/README.md)

1. Choose the release matching Windows, Linux or macOS and your CPU architecture.
2. For a source build, install .NET 10 and follow the solution build instructions.

```sh
dotnet build Sprocket.slnx
```


```sh
dotnet run --project src/Sprocket.App
```

### First project

Begin with a small, permitted sample and inspect the result. [Source 1](https://github.com/SprocketVideo/Sprocket/blob/main/README.md)

1. Import media, choose a canvas preset and edit a short timeline.
2. Enable the opt-in loopback MCP service and connect a compatible agent if wanted.
3. Review changes and export through the editor.
### Hardware & software

Published requirements and explicit documentation gaps follow. [Source 1](https://github.com/SprocketVideo/Sprocket/blob/main/README.md)

- **Hardware:** A GPU compositing path is documented; minimum RAM, VRAM and storage are not specified.
- **Software:** .NET 10 SDK for source builds. Releases bundle FFmpeg 8 libraries; a system FFmpeg CLI is needed for media tests, not normal editor operation.
- **Platforms:** Windows 10 64-bit 1809+ and Windows 11 are supported. Linux x64/ARM64 is experimental and needs glibc >=2.35. macOS Intel/Apple Silicon packages are unsigned alpha builds.

### License, model weights & costs

The complete top-level MIT software terms were reviewed and archived today; model/dependency/host terms remain separate. [Source 1](https://github.com/SprocketVideo/Sprocket/blob/main/LICENSE) [Source 2](https://github.com/SprocketVideo/Sprocket/blob/main/README.md)

- **Code:** MIT
- **Weights:** No generative weights are bundled. The external AI agent and any model it uses retain their own terms.
- **Commercial:** The main MIT code grant permits commercial use under its notice/source and other conditions. Model, component, asset and hosted-service permission is separate. No generative weights are bundled. The external AI agent and any model it uses retain their own terms.
- **Cost:** MIT editor software has no license fee. Agent accounts, inference and compute can add costs.

### Why it merits attention

Assessment: an actual timeline and reversible editing operations make its AI integration more useful than a chat-only wrapper. Alpha platform status limits readiness; no export was tested. [Source 1](https://github.com/SprocketVideo/Sprocket/blob/main/README.md)

### Limitations

Native VST/AU/OFX plug-in hosting is not implemented. Cross-platform CI claims and project demos are author evidence, not our hardware benchmarks. [Source 1](https://github.com/SprocketVideo/Sprocket/blob/main/README.md) [Source 2](https://github.com/SprocketVideo/Sprocket/blob/main/LICENSE)

### Get the tool

- [Repository](https://github.com/SprocketVideo/Sprocket)
- [Documentation](https://github.com/SprocketVideo/Sprocket/blob/main/README.md)

## H3ddle

Video, animation & film · Images & design · Audio, music & voice · Editing, captions & post-production

First detailed guide in this library; documentation checked today. Repository created 2026-08-13; current source metadata is a discovery signal, not evidence of a significant product upgrade.

### How it uses AI

Native Metal inference generates video, images, music, sound effects and reference-conditioned speech, then combines them on a small local timeline. [Source](https://github.com/AlexanderIstomin/h3ddle/blob/main/README.md)

### Introduction

A native Apple Silicon generative-media studio combining local Metal inference with a small text, visual and audio timeline. [Source 1](https://github.com/AlexanderIstomin/h3ddle/blob/main/README.md)

### What it is good for

Draft an atmospheric short by generating stills, video, ambience and narration, then arrange them in one Mac project. [Source 1](https://github.com/AlexanderIstomin/h3ddle/blob/main/README.md)

### Demo & examples

The repository describes the studio and downloadable development builds; its model picker is the local starting point. [Source 1](https://github.com/AlexanderIstomin/h3ddle/blob/main/README.md)

### Install

Documentation-based setup route; commands are examples from the project and were not executed during this review. [Source 1](https://github.com/AlexanderIstomin/h3ddle/blob/main/README.md)

1. Download the macOS development release, or clone the repository for an Xcode build.
2. For a source build, generate the project and open it in Xcode; install a selected model through the app.

```sh
xcodegen generate
```


```sh
open H3ddle.xcodeproj
```

### First project

Begin with a small, permitted sample and inspect the result. [Source 1](https://github.com/AlexanderIstomin/h3ddle/blob/main/README.md)

1. Select an installed model and set prompt, duration and canvas.
2. Queue a short generation, inspect the result and add it to the timeline.
3. Save the project and export through the documented system media frameworks.
### Hardware & software

Published requirements and explicit documentation gaps follow. [Source 1](https://github.com/AlexanderIstomin/h3ddle/blob/main/README.md)

- **Hardware:** Apple Silicon is required. The README discusses weight streaming on 16/32 GB Macs, but does not establish a universal minimum RAM or total storage requirement.
- **Software:** macOS >=15; source builds require Xcode >=26 and XcodeGen >=2.46. FFmpeg/FFprobe are optional fallbacks for containers unsupported by system frameworks.
- **Platforms:** Native macOS Apple Silicon only in the documented route; no Intel Mac, Windows or Linux build is claimed.

### License, model weights & costs

The complete top-level Apache-2.0 software terms were reviewed and archived today; model/dependency/host terms remain separate. [Source 1](https://github.com/AlexanderIstomin/h3ddle/blob/main/LICENSE) [Source 2](https://github.com/AlexanderIstomin/h3ddle/blob/main/README.md)

- **Code:** Apache-2.0
- **Weights:** Weights are separately downloaded and licensed. YuE2-3B is explicitly CC-BY-NC 4.0; MiniMax H3, LTX and other checkpoints require independent terms review.
- **Commercial:** The main Apache-2.0 code grant permits commercial use under its notice/source and other conditions. Model, component, asset and hosted-service permission is separate. Weights are separately downloaded and licensed. YuE2-3B is explicitly CC-BY-NC 4.0; MiniMax H3, LTX and other checkpoints require independent terms review.
- **Cost:** Local inference avoids a required paid API, but compute and model-specific permissions remain separate from Apache-2.0 app code.

### Why it merits attention

Assessment: a native local generation queue and saved recipes are promising for Mac experimentation. The README distinguishes measured short runs from projected long-video speeds; neither was reproduced here. [Source 1](https://github.com/AlexanderIstomin/h3ddle/blob/main/README.md)

### Limitations

The timeline is deliberately small. Some model paths are experimental; engineering speed projections are not completed benchmarks or guarantees. [Source 1](https://github.com/AlexanderIstomin/h3ddle/blob/main/README.md) [Source 2](https://github.com/AlexanderIstomin/h3ddle/blob/main/LICENSE)

### Get the tool

- [Repository](https://github.com/AlexanderIstomin/h3ddle)
- [Documentation](https://github.com/AlexanderIstomin/h3ddle/blob/main/README.md)

## FoveaEngine / FoveaCore

3D, reconstruction & assets · Spatial audio & volumetric media · Photogrammetry, scanning & neural rendering · Games & production pipelines · WebXR, VR & AR

First detailed guide in this library; documentation checked today. Repository created 2026-04-02; current source metadata is a discovery signal, not evidence of a significant product upgrade.

### How it uses AI

The reconstruction bridge creates learned Gaussian scenes from captures, and the Godot add-on integrates those neural representations into creative scenes. [Source](https://github.com/zedarvates/FoveaCore/blob/main/README.md)

### Introduction

A Godot add-on for learned Gaussian-splat assets, with StudioTo3D reconstruction bridges and experimental OpenXR integration. [Source 1](https://github.com/zedarvates/FoveaCore/blob/main/README.md)

### What it is good for

Bring a reconstructed object or room into a Godot scene, then explore whether a splat-based exhibit or game environment fits your design. [Source 1](https://github.com/zedarvates/FoveaCore/blob/main/README.md)

### Demo & examples

The README includes desktop splat captures and a shipped demo scene. Those captures do not establish headset rendering quality. [Source 1](https://github.com/zedarvates/FoveaCore/blob/main/README.md)

### Install

Documentation-based setup route; commands are examples from the project and were not executed during this review. [Source 1](https://github.com/zedarvates/FoveaCore/blob/main/README.md) [Source 2](https://github.com/zedarvates/FoveaCore/blob/main/tutorials/reconstruction_setup.md)

1. Install the current documented Godot stable Mono baseline and clone with submodules.
2. Open project.godot and the provided drop_a_ply demo. Reconstruction requires additional FFmpeg/COLMAP setup.

```sh
git clone --recurse-submodules https://github.com/zedarvates/FoveaCore.git
```

### First project

Begin with a small, permitted sample and inspect the result. [Source 1](https://github.com/zedarvates/FoveaCore/blob/main/README.md)

1. Run demo/drop_a_ply.tscn or add a FoveaSplat3D node to a scene.
2. Assign a compatible .ply source and inspect its appearance.
3. For neural reconstruction, follow the separate StudioTo3D tutorial before importing the produced asset.
### Hardware & software

Published requirements and explicit documentation gaps follow. [Source 1](https://github.com/zedarvates/FoveaCore/blob/main/README.md) [Source 2](https://github.com/zedarvates/FoveaCore/blob/main/tutorials/reconstruction_setup.md)

- **Hardware:** A Forward+ capable GPU is required. Minimum RAM, VRAM and storage are not documented in the inspected quickstart.
- **Software:** The current README specifies Godot 4.7.2 stable Mono. FFmpeg/COLMAP and reconstruction backend dependencies are separate; they are unnecessary for viewing an existing splat.
- **Platforms:** Desktop captures are documented. Complete Windows/macOS/Linux parity and OpenXR headset support are not verified; older 4.7.dev5 screenshots are historical evidence.

### License, model weights & costs

The complete top-level MIT software terms were reviewed and archived today; model/dependency/host terms remain separate. [Source 1](https://github.com/zedarvates/FoveaCore/blob/main/LICENSE) [Source 2](https://github.com/zedarvates/FoveaCore/blob/main/README.md)

- **Code:** MIT
- **Weights:** MIT applies to the add-on; reconstruction implementations, checkpoints and scene assets have separate terms.
- **Commercial:** The main MIT code grant permits commercial use under its notice/source and other conditions. Model, component, asset and hosted-service permission is separate. MIT applies to the add-on; reconstruction implementations, checkpoints and scene assets have separate terms.
- **Cost:** No software license fee or required hosted inference service is stated. Reconstruction hardware and optional bridges add costs.

### Why it merits attention

Assessment: primary-source demo assets and explicit experimental boundaries support a focused Godot trial. Documentation review only; no scene or headset was run. [Source 1](https://github.com/zedarvates/FoveaCore/blob/main/README.md)

### Limitations

OpenXR/foveation and optional research bridges remain experimental. A splat is a learned appearance representation, not a watertight print-ready mesh. [Source 1](https://github.com/zedarvates/FoveaCore/blob/main/README.md) [Source 2](https://github.com/zedarvates/FoveaCore/blob/main/LICENSE)

### Get the tool

- [Repository](https://github.com/zedarvates/FoveaCore)
- [Documentation](https://github.com/zedarvates/FoveaCore/blob/main/README.md)

## flipdot

Physical, robotic & kinetic installations · Interactive, immersive & live media · Performance, projection & stage media · Games & production pipelines

First detailed guide in this library; documentation checked today. Repository created 2025-05-24; current source metadata is a discovery signal, not evidence of a significant product upgrade.

### How it uses AI

MediaPipe pose/face inference makes a physical artwork react to viewers; optional AI agents author and control animations. [Source](https://github.com/mdbug/flipdot/blob/master/README.md)

### Introduction

An interactive mechanical flip-dot artwork driven by learned pose/face tracking, with optional AI-agent-authored animations. [Source 1](https://github.com/mdbug/flipdot/blob/master/README.md)

### What it is good for

Build a public installation in which a visitor silhouette controls sand, games or line-art portraits on a physical 28×28 panel. [Source 1](https://github.com/mdbug/flipdot/blob/master/README.md)

### Demo & examples

The authors publish recordings of the reactive panel and agent-controlled games in the README. [Source 1](https://github.com/mdbug/flipdot/blob/master/README.md)

### Install

Documentation-based setup route; commands are examples from the project and were not executed during this review. [Source 1](https://github.com/mdbug/flipdot/blob/master/README.md) [Source 2](https://github.com/mdbug/flipdot/blob/master/docs/jetson-setup.md)

1. Follow docs/jetson-setup.md for Jetson OS, Python dependencies, the GPU MediaPipe wheel and models.
2. Configure serial hardware and webcam; launch the documented Python application. The deploy script is for an already prepared device.

```sh
python flipdot.py
```

### First project

Begin with a small, permitted sample and inspect the result. [Source 1](https://github.com/mdbug/flipdot/blob/master/README.md)

1. Begin with the pygame preview setting if hardware is not connected.
2. Connect the panel and test pose, caricature and gesture modes.
3. Use the browser console for controls; optional hosted chat or authenticated MCP adds agent-driven scripts.
### Hardware & software

Published requirements and explicit documentation gaps follow. [Source 1](https://github.com/mdbug/flipdot/blob/master/README.md) [Source 2](https://github.com/mdbug/flipdot/blob/master/docs/jetson-setup.md)

- **Hardware:** Documented build: Jetson Orin Nano, four AlfaZeta XY5 28×7 modules, USB RS485 at 57600 baud and a webcam. Gamepads are optional. Minimum memory, total disk and full bill-of-materials cost are not stated.
- **Software:** JetPack R36/Python 3.10 and a custom GPU-enabled MediaPipe build in the documented Jetson route; FastAPI browser console and Linux deployment tools. Bubblewrap is required for the optional script sandbox; the setup guide also documents a stock CPU MediaPipe fallback.
- **Platforms:** The physical installation targets Jetson Linux. A pygame preview exists; equal native Windows/macOS support is not documented.

### License, model weights & costs

The complete top-level MIT software terms were reviewed and archived today; model/dependency/host terms remain separate. [Source 1](https://github.com/mdbug/flipdot/blob/master/LICENSE) [Source 2](https://github.com/mdbug/flipdot/blob/master/README.md)

- **Code:** MIT
- **Weights:** MIT installation code does not relicense MediaPipe models, optional provider models or music used in demo recordings.
- **Commercial:** The main MIT code grant permits commercial use under its notice/source and other conditions. Model, component, asset and hosted-service permission is separate. MIT installation code does not relicense MediaPipe models, optional provider models or music used in demo recordings.
- **Cost:** Physical modules, controller and compute are paid hardware. Pose tracking is local; optional Claude/GPT/provider chat may incur service fees.

### Why it merits attention

Assessment: a concrete physical artwork and published demonstrations make this an unusually relevant installation reference. We did not assemble hardware or validate latency. [Source 1](https://github.com/mdbug/flipdot/blob/master/README.md)

### Limitations

This is a bespoke build rather than an off-the-shelf installer. Recording demo music or visitor imagery introduces asset permissions separate from the code license. [Source 1](https://github.com/mdbug/flipdot/blob/master/README.md) [Source 2](https://github.com/mdbug/flipdot/blob/master/LICENSE)

### Get the tool

- [Repository](https://github.com/mdbug/flipdot)
- [Documentation](https://github.com/mdbug/flipdot/blob/master/README.md)

## Dissolution

Physical, robotic & kinetic installations · Interactive, immersive & live media · Images & design · Performance, projection & stage media

First detailed guide in this library; documentation checked today. Repository created 2026-04-17; current source metadata is a discovery signal, not evidence of a significant product upgrade.

### How it uses AI

Stable Diffusion/ControlNet and MediaPipe combine webcam portraits with neural image generation in an interactive installation. [Source](https://github.com/burakkagann/dissolution/blob/main/README.md)

### Introduction

A webcam installation that uses Stable Diffusion, ControlNet and MediaPipe to turn a visitor portrait into an animated dissolve and generated image. [Source 1](https://github.com/burakkagann/dissolution/blob/main/README.md)

### What it is good for

Prototype a reactive portrait installation with keyboard controls, optional sound reactivity and an MP4 capture route. [Source 1](https://github.com/burakkagann/dissolution/blob/main/README.md)

### Demo & examples

The repository describes the exhibited piece and provides both live and offline scripts; the live script is the actual neural route. [Source 1](https://github.com/burakkagann/dissolution/blob/main/README.md)

### Install

Documentation-based setup route; commands are examples from the project and were not executed during this review. [Source 1](https://github.com/burakkagann/dissolution/blob/main/README.md)

1. Clone the repository and create an isolated Python >=3.11 environment.
2. Install requirements; expect first-launch downloads of models.

```sh
pip install -r requirements.txt
```


```sh
python dissolution_live.py
```


```sh
python dissolution_live.py --record out.mp4
```

### First project

Begin with a small, permitted sample and inspect the result. [Source 1](https://github.com/burakkagann/dissolution/blob/main/README.md)

1. Select a working webcam and start a short live session.
2. Adjust prompt presets and conditioning, inspecting portraits between cycles.
3. Record the display if needed and review the generated/source-image archive.
### Hardware & software

Published requirements and explicit documentation gaps follow. [Source 1](https://github.com/burakkagann/dissolution/blob/main/README.md)

- **Hardware:** A webcam and CUDA GPU are effectively required for the intended real-time neural experience. About 5 GB disk is documented for models, plus ~42 MB MediaPipe tasks. Minimum RAM and VRAM are not specified.
- **Software:** Python >=3.11, the repository requirements and a matching CUDA/PyTorch environment.
- **Platforms:** The neural path targets CUDA. OpenCV camera notes mention Linux/macOS, but Apple Silicon generation is explicitly untested; CPU fallback is a UI-only mode.

### License, model weights & costs

The complete top-level MIT software terms were reviewed and archived today; model/dependency/host terms remain separate. [Source 1](https://github.com/burakkagann/dissolution/blob/main/LICENSE) [Source 2](https://github.com/burakkagann/dissolution/blob/main/README.md)

- **Code:** MIT
- **Weights:** MIT applies to installation code. Stable Diffusion, ControlNet and MediaPipe checkpoint terms are separate and were not fully resolved here.
- **Commercial:** The main MIT code grant permits commercial use under its notice/source and other conditions. Model, component, asset and hosted-service permission is separate. MIT applies to installation code. Stable Diffusion, ControlNet and MediaPipe checkpoint terms are separate and were not fully resolved here.
- **Cost:** No required paid inference API is documented. GPU, webcam and exhibition display costs remain.

### Why it merits attention

Assessment: the documented exhibition and recording controls make it a concrete creative-AI study. Documentation review only; no portrait was generated. [Source 1](https://github.com/burakkagann/dissolution/blob/main/README.md)

### Limitations

--no-controlnet replaces neural generation with fallback images. Visitor source photos and outputs are archived locally; exhibition layout presets are monitor-specific. [Source 1](https://github.com/burakkagann/dissolution/blob/main/README.md) [Source 2](https://github.com/burakkagann/dissolution/blob/main/LICENSE)

### Get the tool

- [Repository](https://github.com/burakkagann/dissolution)
- [Documentation](https://github.com/burakkagann/dissolution/blob/main/README.md)

## Text-to-Lottie

Motion capture & character animation · Vector graphics, illustration & textures · Browser tools & web media · Mobile, edge & on-device creation · AI agents for code-authored media production

First detailed guide in this library; documentation checked today. Repository created 2026-06-04; current source metadata is a discovery signal, not evidence of a significant product upgrade.

### How it uses AI

A coding model interprets a motion brief/reference SVG and authors editable Lottie animation through the supplied skill and player. [Source](https://github.com/diffusionstudio/lottie/blob/main/README.md)

### Introduction

An open-source agent skill and animation workspace that turns prompts and reference SVGs into editable Lottie JSON. [Source 1](https://github.com/diffusionstudio/lottie/blob/main/README.md)

### What it is good for

Create a looping logo, animated interface illustration or mobile onboarding element, then refine motion in the supplied player. [Source 1](https://github.com/diffusionstudio/lottie/blob/main/README.md)

### Demo & examples

The README embeds examples; the official announcement describes the text-to-Lottie release. [Source 1](https://github.com/diffusionstudio/lottie/blob/main/README.md) [Source 2](https://diffusion.studio/changelog/text-to-lottie-v1/)

### Install

Documentation-based setup route; commands are examples from the project and were not executed during this review. [Source 1](https://github.com/diffusionstudio/lottie/blob/main/README.md)

1. Use a compatible coding agent with skill support and a Node/npm workspace.
2. Install the published skill, then ask the agent to set up its animation workspace.

```sh
npx skills add diffusionstudio/lottie
```

### First project

Begin with a small, permitted sample and inspect the result. [Source 1](https://github.com/diffusionstudio/lottie/blob/main/README.md)

1. Provide your own SVG or reference and specify timing, duration and frame rate.
2. Inspect and scrub the generated scene, requesting controls for properties you want to edit.
3. Export Lottie JSON and test it in the intended web/mobile renderer.
### Hardware & software

Published requirements and explicit documentation gaps follow. [Source 1](https://github.com/diffusionstudio/lottie/blob/main/README.md)

- **Hardware:** No RAM, VRAM, GPU or storage minimum is documented. External model inference requirements depend on the agent backend.
- **Software:** A skill-capable coding agent and the generated web workspace. Exact minimum Node version is not stated in the README.
- **Platforms:** Web authoring/player and web, iOS, Android or Flutter rendering integrations are described. Rendering an animation on a phone does not prove on-device AI inference.

### License, model weights & costs

The complete top-level MIT software terms were reviewed and archived today; model/dependency/host terms remain separate. [Source 1](https://github.com/diffusionstudio/lottie/blob/main/LICENSE) [Source 2](https://github.com/diffusionstudio/lottie/blob/main/README.md)

- **Code:** MIT
- **Weights:** MIT covers this framework; the coding-agent model and supplied SVG/font assets retain their own licenses.
- **Commercial:** The main MIT code grant permits commercial use under its notice/source and other conditions. Model, component, asset and hosted-service permission is separate. MIT covers this framework; the coding-agent model and supplied SVG/font assets retain their own licenses.
- **Cost:** The framework has no code license fee. Claude, Codex or another agent backend may require an account or inference payment.

### Why it merits attention

Assessment: editable JSON and immediate playback support practical iteration. Production-readiness is an author claim; we did not generate or render an animation. [Source 1](https://github.com/diffusionstudio/lottie/blob/main/README.md)

### Limitations

Complex effects can differ by Lottie renderer. Quality depends on the agent and the supplied references; generated output still needs visual review. [Source 1](https://github.com/diffusionstudio/lottie/blob/main/README.md) [Source 2](https://github.com/diffusionstudio/lottie/blob/main/LICENSE)

### Get the tool

- [Repository](https://github.com/diffusionstudio/lottie)
- [Documentation](https://github.com/diffusionstudio/lottie/blob/main/README.md)

## Dynamic Typography

AI kinetic typography and animated lettering · Typography, fonts & layout · Motion capture & character animation · Vector graphics, illustration & textures · Computational art & creative coding

First detailed guide in this library; documentation checked today. Repository created 2024-04-15; current source metadata is a discovery signal, not evidence of a significant product upgrade.

### How it uses AI

A video diffusion prior guides vector letter deformation and temporal motion from a semantic animation prompt. [Source](https://github.com/zliucz/animate-your-word/blob/main/README.md)

### Introduction

A diffusion-guided research system that deforms and animates vector letter shapes according to a semantic prompt. [Source 1](https://github.com/zliucz/animate-your-word/blob/main/README.md)

### What it is good for

Explore a title in which a chosen letter acts out a movement while retaining a recognizable word; useful for experimental identity and typographic art. [Source 1](https://github.com/zliucz/animate-your-word/blob/main/README.md)

### Demo & examples

The official demo page shows animated examples and the repository includes example scripts and GIFs. [Source 1](https://github.com/zliucz/animate-your-word/blob/main/README.md) [Source 2](https://animate-your-word.github.io/demo/)

### Install

Documentation-based setup route; commands are examples from the project and were not executed during this review. [Source 1](https://github.com/zliucz/animate-your-word/blob/main/README.md)

1. Create the supplied Linux conda environment and install diffvg as described by the authors.
2. Use the provided generation script with a word, selected letter and motion caption.

```sh
conda env create -f environment.yml
```


```sh
conda activate dTypo
```


```sh
python dynamicTypography.py --word "flow" --optimized_letter "f" --caption "a letter flowing in wind" --use_xformer --canonical --anneal --use_perceptual_loss --use_conformal_loss --use_transition_loss
```

### First project

Begin with a small, permitted sample and inspect the result. [Source 1](https://github.com/zliucz/animate-your-word/blob/main/README.md)

1. Choose one letter and begin with an example configuration.
2. Inspect SVG frame logs and MP4/GIF output under videos.
3. Adjust shape-preservation and transition weights when legibility or consistency drifts.
### Hardware & software

Published requirements and explicit documentation gaps follow. [Source 1](https://github.com/zliucz/animate-your-word/blob/main/README.md)

- **Hardware:** For >=20 frames, the README requires at least 24 GB VRAM; its default 24-frame run is about 28 GB. Published samples used H800 80 GB. Minimum host RAM and storage are not documented.
- **Software:** Linux-tested conda environment, CUDA/PyTorch and compiled diffvg. The environment file pins the reproducible stack.
- **Platforms:** Linux is the tested and recommended platform; Windows and macOS support are not documented.

### License, model weights & costs

The complete top-level Apache-2.0 software terms were reviewed and archived today; model/dependency/host terms remain separate. [Source 1](https://github.com/zliucz/animate-your-word/blob/main/LICENSE) [Source 2](https://github.com/zliucz/animate-your-word/blob/main/README.md)

- **Code:** Apache-2.0
- **Weights:** Apache-2.0 covers this code. Diffusion priors, diffvg, fonts and reference assets retain independent terms.
- **Commercial:** The main Apache-2.0 code grant permits commercial use under its notice/source and other conditions. Model, component, asset and hosted-service permission is separate. Apache-2.0 covers this code. Diffusion priors, diffvg, fonts and reference assets retain independent terms.
- **Cost:** No paid API is required by the research route, but substantial GPU resources may need rental.

### Why it merits attention

Assessment: vector output and explicit memory guidance distinguish it from a generic image animation demo. Documentation review only; legibility and convergence were not tested. [Source 1](https://github.com/zliucz/animate-your-word/blob/main/README.md)

### Limitations

This is an older research project first profiled here, not a new October launch. Optimization can distort letters, and the authors recommend seed/weight changes for artifacts. [Source 1](https://github.com/zliucz/animate-your-word/blob/main/README.md) [Source 2](https://github.com/zliucz/animate-your-word/blob/main/LICENSE)

### Get the tool

- [Repository](https://github.com/zliucz/animate-your-word)
- [Documentation](https://github.com/zliucz/animate-your-word/blob/main/README.md)
- [Demo](https://animate-your-word.github.io/demo/)

## OpenLayer

Images & design · Photography, restoration & color · Editing, captions & post-production · VFX, compositing & relighting

First detailed guide in this library; documentation checked today. Repository created 2026-06-21; current source metadata is a discovery signal, not evidence of a significant product upgrade.

### How it uses AI

Local ComfyUI model workflows generate or transform document content and return editable layers to Photoshop. [Source](https://github.com/MehranMarxian/OpenLayer/blob/main/README.md)

### Introduction

A Photoshop UXP panel connecting to local ComfyUI so AI generation, inpainting and other transformations return as editable Photoshop layers. [Source 1](https://github.com/MehranMarxian/OpenLayer/blob/main/README.md)

### What it is good for

Generate a background, repaint a selection or derive masks while keeping the results in a layered photographic composition. [Source 1](https://github.com/MehranMarxian/OpenLayer/blob/main/README.md)

### Demo & examples

The README links recorded Photoshop sessions and layer examples; these are developer demonstrations. [Source 1](https://github.com/MehranMarxian/OpenLayer/blob/main/README.md)

### Install

Documentation-based setup route; commands are examples from the project and were not executed during this review. [Source 1](https://github.com/MehranMarxian/OpenLayer/blob/main/README.md)

1. Install Photoshop 2024+ and Adobe Creative Cloud, plus a working local ComfyUI setup.
2. Download the .ccx release, install through Creative Cloud, then open Plugins → OpenLayer and connect to ComfyUI.
### First project

Begin with a small, permitted sample and inspect the result. [Source 1](https://github.com/MehranMarxian/OpenLayer/blob/main/README.md)

1. Check the active ComfyUI port and required models in Setup.
2. Select an image/selection and a compatible workflow, then generate a layer.
3. Inspect masks, spelling and placement before editing or exporting the composition.
### Hardware & software

Published requirements and explicit documentation gaps follow. [Source 1](https://github.com/MehranMarxian/OpenLayer/blob/main/README.md)

- **Hardware:** GPU >=8 GB VRAM is documented; 12 GB is the project target. Minimum RAM and total model storage are not stated.
- **Software:** Photoshop 2024+, Creative Cloud and local ComfyUI. Python/backend requirements follow the separately installed ComfyUI stack.
- **Platforms:** Author verification is Windows 11 with Photoshop 2025. macOS and other Photoshop versions remain unverified.

### License, model weights & costs

The complete top-level MIT software terms were reviewed and archived today; model/dependency/host terms remain separate. [Source 1](https://github.com/MehranMarxian/OpenLayer/blob/main/LICENSE) [Source 2](https://github.com/MehranMarxian/OpenLayer/blob/main/README.md)

- **Code:** MIT
- **Weights:** MIT applies to the panel. ComfyUI/checkpoint terms are separate; Qwen-Image 2.1 presets are explicitly research/evaluation-only, opt-in and not default.
- **Commercial:** The main MIT code grant permits commercial use under its notice/source and other conditions. Model, component, asset and hosted-service permission is separate. MIT applies to the panel. ComfyUI/checkpoint terms are separate; Qwen-Image 2.1 presets are explicitly research/evaluation-only, opt-in and not default.
- **Cost:** The panel has no subscription fee and local generation needs no hosted credits. Photoshop is a required paid proprietary host.

### Why it merits attention

Assessment: actual layer integration and recorded sessions support a useful trial for existing Photoshop users. We did not install the plug-in or test generated layers. [Source 1](https://github.com/MehranMarxian/OpenLayer/blob/main/README.md)

### Limitations

Public alpha, unsigned plug-in; unflattening and multi-reference tools are experimental. A free panel does not remove Photoshop or model licensing restrictions. [Source 1](https://github.com/MehranMarxian/OpenLayer/blob/main/README.md) [Source 2](https://github.com/MehranMarxian/OpenLayer/blob/main/LICENSE)

### Get the tool

- [Repository](https://github.com/MehranMarxian/OpenLayer)
- [Documentation](https://github.com/MehranMarxian/OpenLayer/blob/main/README.md)

## Motion Launch Videos

Motion capture & character animation · AI kinetic typography and animated lettering · Video, animation & film · AI agents for code-authored media production · Creative publishing & presentation

First detailed guide in this library; documentation checked today. Repository created 2026-09-27; current source metadata is a discovery signal, not evidence of a significant product upgrade.

### How it uses AI

AI coding-agent workflows write motion graphics from a brief, then use deterministic HTML/browser frames and video-export utilities. [Source](https://github.com/Kimeur/motion-launch-videos/blob/main/README.md)

### Introduction

A set of AI coding-agent workflows for deterministic, code-authored motion graphics, with browser rendering and video export helpers. [Source 1](https://github.com/Kimeur/motion-launch-videos/blob/main/README.md)

### What it is good for

Make a vertical announcement, captioned voice-over, pixel-art teaser, animated chart or transparent lower-third from your own content. [Source 1](https://github.com/Kimeur/motion-launch-videos/blob/main/README.md)

### Demo & examples

Included templates and examples can render sample films; the README shows all supported style families. [Source 1](https://github.com/Kimeur/motion-launch-videos/blob/main/README.md)

### Install

Documentation-based setup route; commands are examples from the project and were not executed during this review. [Source 1](https://github.com/Kimeur/motion-launch-videos/blob/main/README.md)

1. Install the repository marketplace plug-in in Claude Code or copy selected skills into its supported skill directory.
2. Install Node, playwright-core, Chromium and FFmpeg/FFprobe; use the included doctor command to check the render stack.

```sh
/plugin marketplace add Kimeur/motion-launch-videos
```


```sh
/plugin install motion-launch-videos@motion-launch-videos
```

### First project

Begin with a small, permitted sample and inspect the result. [Source 1](https://github.com/Kimeur/motion-launch-videos/blob/main/README.md)

1. Give the agent a sourced brief, duration, aspect ratio and permitted assets.
2. Inspect its self-contained HTML film, stills and contact sheet.
3. Render the desired formats and review decoded output and audio before use.
### Hardware & software

Published requirements and explicit documentation gaps follow. [Source 1](https://github.com/Kimeur/motion-launch-videos/blob/main/README.md)

- **Hardware:** Minimum RAM, VRAM and storage are not documented. WebGL2 may use GPU or Chromium software rendering.
- **Software:** Node >=20, playwright-core, Chromium, FFmpeg/FFprobe with libx264; AAC for sound and ProRes/VP9 for transparency. Initial font fetching needs network access.
- **Platforms:** The documented rendering components have macOS/Linux installation examples. A fully verified Windows route is not established in the inspected quickstart.

### License, model weights & costs

The complete top-level MIT software terms were reviewed and archived today; model/dependency/host terms remain separate. [Source 1](https://github.com/Kimeur/motion-launch-videos/blob/main/LICENSE) [Source 2](https://github.com/Kimeur/motion-launch-videos/blob/main/README.md)

- **Code:** MIT
- **Weights:** MIT covers these workflows and scripts; the agent model, fonts, product content and imported media have independent terms.
- **Commercial:** The main MIT code grant permits commercial use under its notice/source and other conditions. Model, component, asset and hosted-service permission is separate. MIT covers these workflows and scripts; the agent model, fonts, product content and imported media have independent terms.
- **Cost:** Local rendering needs no required paid render service, but the AI agent may require paid access.

### Why it merits attention

Assessment: deterministic frames and explicit export checks offer a practical workflow for repeatable motion drafts. Documentation review only; no MP4 was rendered. [Source 1](https://github.com/Kimeur/motion-launch-videos/blob/main/README.md)

### Limitations

Recent creation is not proof of quality. Its automated visual checks supplement human review and do not guarantee a good design or correct product claims. [Source 1](https://github.com/Kimeur/motion-launch-videos/blob/main/README.md) [Source 2](https://github.com/Kimeur/motion-launch-videos/blob/main/LICENSE)

### Get the tool

- [Repository](https://github.com/Kimeur/motion-launch-videos)
- [Documentation](https://github.com/Kimeur/motion-launch-videos/blob/main/README.md)

## VDN-H3

Video, animation & film · Audio, music & voice · Emerging & cross-disciplinary creative AI

First detailed guide in this library; documentation checked today. Repository created 2026-09-02; current source metadata is a discovery signal, not evidence of a significant product upgrade.

### How it uses AI

Learned hybrid-attention and distilled model adaptations generate video with audio through a research inference stack. [Source](https://github.com/OpenVDN/vdn-minimax-h3/blob/main/README.md)

### Introduction

A research training/inference implementation that adapts MiniMax H3 with hybrid attention and distillation for video with audio. [Source 1](https://github.com/OpenVDN/vdn-minimax-h3/blob/main/README.md)

### What it is good for

Evaluate an accelerated local text-to-video-with-audio route for a short concept clip when you have NVIDIA compute and research-engineering experience. [Source 1](https://github.com/OpenVDN/vdn-minimax-h3/blob/main/README.md)

### Demo & examples

The authors publish example videos and benchmark tables; the Diffusers script is the first local inference route. [Source 1](https://github.com/OpenVDN/vdn-minimax-h3/blob/main/README.md)

### Install

Documentation-based setup route; commands are examples from the project and were not executed during this review. [Source 1](https://github.com/OpenVDN/vdn-minimax-h3/blob/main/README.md)

1. Create the documented Python 3.12 CUDA environment and install the matched PyTorch build.
2. Install the repository and its patched Diffusers, then download the separately licensed weights.

```sh
uv pip install torch==2.13.0 --index-url https://download.pytorch.org/whl/cu129
```


```sh
uv pip install --prerelease=allow -e .
```

### First project

Begin with a small, permitted sample and inspect the result. [Source 1](https://github.com/OpenVDN/vdn-minimax-h3/blob/main/README.md)

1. Follow the authors’ patched-Diffusers setup before inference.
2. Run src/inference/infer_diffusers.py with a prompt and --out; use --offload_dit for the documented 24 GB configuration.
3. Review video and audio synchronization rather than judging quality from denoising speed alone.
### Hardware & software

Published requirements and explicit documentation gaps follow. [Source 1](https://github.com/OpenVDN/vdn-minimax-h3/blob/main/README.md)

- **Hardware:** A 24 GB card with block offload is documented for a 345-frame example, not as a universal minimum. The full repository checkpoint bundle is about 82 GB. Host RAM is not specified.
- **Software:** Python 3.12, recommended PyTorch 2.13.0+cu129 and patched Diffusers. Attention kernels vary between Hopper/datacenter Blackwell and consumer GPUs.
- **Platforms:** The inspected route is NVIDIA/CUDA-oriented; macOS, AMD and native Windows support are not established.

### License, model weights & costs

The complete top-level Apache-2.0 software terms were reviewed and archived today; model/dependency/host terms remain separate. [Source 1](https://github.com/OpenVDN/vdn-minimax-h3/blob/main/LICENSE) [Source 2](https://github.com/OpenVDN/vdn-minimax-h3/blob/main/README.md) [Source 3](https://github.com/OpenVDN/vdn-minimax-h3/blob/main/licenses/MiniMax-H3-Community-License-Agreement.txt)

- **Code:** Apache-2.0
- **Weights:** Apache-2.0 applies to training/inference code. Derivative weights use the separate MiniMax H3 Community License Agreement, not Apache-2.0.
- **Commercial:** The main Apache-2.0 code grant permits commercial use under its notice/source and other conditions. Model, component, asset and hosted-service permission is separate. Apache-2.0 applies to training/inference code. Derivative weights use the separate MiniMax H3 Community License Agreement, not Apache-2.0.
- **Cost:** Local inference does not require the hosted MiniMax API, but model permissions and GPU/rental costs still apply.

### Why it merits attention

Assessment: published inference configurations and bounded benchmark definitions make this a credible experimental lead. No benchmark or clip was reproduced. [Source 1](https://github.com/OpenVDN/vdn-minimax-h3/blob/main/README.md)

### Limitations

Headline multi-B200 speed depends on hardware, warm-up and pipeline boundaries. The fast denoising figures exclude some processing; approximate/distilled paths can change quality. [Source 1](https://github.com/OpenVDN/vdn-minimax-h3/blob/main/README.md) [Source 2](https://github.com/OpenVDN/vdn-minimax-h3/blob/main/LICENSE) [Source 3](https://github.com/OpenVDN/vdn-minimax-h3/blob/main/licenses/MiniMax-H3-Community-License-Agreement.txt)

### Get the tool

- [Repository](https://github.com/OpenVDN/vdn-minimax-h3)
- [Documentation](https://github.com/OpenVDN/vdn-minimax-h3/blob/main/README.md)

## KJDraw

Vector graphics, illustration & textures · 3D printing & generative CAD · Browser tools & web media · Data art & scientific visualization · AI agents for code-authored media production

First detailed guide in this library; documentation checked today. Repository created 2026-09-07; current source metadata is a discovery signal, not evidence of a significant product upgrade.

### How it uses AI

A language model describes drawing intent, and the software compiles supported operations into editable, reviewed CAD geometry. [Source](https://github.com/KanJieTeam/kjdraw/blob/main/README.md)

### Introduction

An editable CAD engine, workbench and agent interface that turns model-described intent into geometry and reviewed drawing changes. [Source 1](https://github.com/KanJieTeam/kjdraw/blob/main/README.md)

### What it is good for

Draft a 2D part or layout, change dimensions through conversation and retain editable objects, undo and DXF export. [Source 1](https://github.com/KanJieTeam/kjdraw/blob/main/README.md)

### Demo & examples

The official workbench shows a recorded/preset agent scenario. Its Try with AI route connects an actual model separately. [Source 1](https://github.com/KanJieTeam/kjdraw/blob/main/README.md)

### Install

Documentation-based setup route; commands are examples from the project and were not executed during this review. [Source 1](https://github.com/KanJieTeam/kjdraw/blob/main/README.md)

1. Install Node >=22 and the engine package, then add the kjdraw-cad skill to a supported agent.
2. Alternatively open the browser AI workbench and connect your chosen model provider.

```sh
npm install -g @kanjieteam/kjdraw@next
```


```sh
npx skills add KanJieTeam/kjdraw -g
```

### First project

Begin with a small, permitted sample and inspect the result. [Source 1](https://github.com/KanJieTeam/kjdraw/blob/main/README.md)

1. Ask for a simple dimensioned circle or part.
2. Review the proposal before applying it; inspect dimensions and undo/revise as needed.
3. Save/reopen the drawing and export supported DXF/KJD output.
### Hardware & software

Published requirements and explicit documentation gaps follow. [Source 1](https://github.com/KanJieTeam/kjdraw/blob/main/README.md)

- **Hardware:** No minimum RAM, VRAM or storage is documented in the inspected quickstart. Agent inference is external to the geometry engine.
- **Software:** Node >=22 for the local agent route; a compatible agent and its separately configured model. Browser workbench and TypeScript/JavaScript embedding routes are also described.
- **Platforms:** Browser and local Node routes are documented without a complete tested Windows/macOS/Linux support matrix. A web UI does not establish local inference compatibility.

### License, model weights & costs

The complete top-level Apache-2.0 software terms were reviewed and archived today; model/dependency/host terms remain separate. [Source 1](https://github.com/KanJieTeam/kjdraw/blob/main/LICENSE) [Source 2](https://github.com/KanJieTeam/kjdraw/blob/main/README.md)

- **Code:** Apache-2.0
- **Weights:** Apache-2.0 applies to the CAD engine. The connected language model, host agent and imported drawings have separate terms.
- **Commercial:** The main Apache-2.0 code grant permits commercial use under its notice/source and other conditions. Model, component, asset and hosted-service permission is separate. Apache-2.0 applies to the CAD engine. The connected language model, host agent and imported drawings have separate terms.
- **Cost:** Engine code has no license fee. Model inference and optional agent access can cost money.

### Why it merits attention

Assessment: persistent editable geometry and explicit proposal/undo steps support meaningful design iteration. Documentation review only; we did not inspect a generated CAD file. [Source 1](https://github.com/KanJieTeam/kjdraw/blob/main/README.md)

### Limitations

Not 3D solid modeling, direct DWG editing or certified plotting/print output. Generated drawings still need dimensional review; the recorded agent demo is a preset replay. [Source 1](https://github.com/KanJieTeam/kjdraw/blob/main/README.md) [Source 2](https://github.com/KanJieTeam/kjdraw/blob/main/LICENSE)

### Get the tool

- [Repository](https://github.com/KanJieTeam/kjdraw)
- [Documentation](https://github.com/KanJieTeam/kjdraw/blob/main/README.md)

## Pascal Editor

3D, reconstruction & assets · Spatial audio & volumetric media · Browser tools & web media · Interactive, immersive & live media · AI agents for code-authored media production

First detailed guide in this library; documentation checked today. Repository created 2025-10-16; current source metadata is a discovery signal, not evidence of a significant product upgrade.

### How it uses AI

An AI agent can inspect and alter real building-scene objects through MCP/CLI while a browser editor provides visual review. [Source](https://github.com/pascalorg/editor/blob/main/README.md)

### Introduction

A local-first 3D building editor with browser visualization and CLI/MCP operations for AI agents. [Source 1](https://github.com/pascalorg/editor/blob/main/README.md)

### What it is good for

Plan a room or building scene, then let an agent inspect and revise scene objects while you review the design visually. [Source 1](https://github.com/pascalorg/editor/blob/main/README.md)

### Demo & examples

The local editor is the reproducible open-source route. The attractive hosted Pascal Next preview is explicitly outside the current open-source release. [Source 1](https://github.com/pascalorg/editor/blob/main/README.md)

### Install

Documentation-based setup route; commands are examples from the project and were not executed during this review. [Source 1](https://github.com/pascalorg/editor/blob/main/README.md) [Source 2](https://editor.pascal.app/docs/developers/local-editor)

1. Install Node >=22.13 and start the local editor through the published CLI.
2. For AI operations, install/configure a compatible agent and connect pascal mcp connect using the official local-editor guide.

```sh
npx @pascal-app/cli editor
```

### First project

Begin with a small, permitted sample and inspect the result. [Source 1](https://github.com/pascalorg/editor/blob/main/README.md)

1. Create or open a local scene and inspect it in the editor.
2. Connect an agent to request bounded scene changes, then review the result.
3. Retain project data and test the supported export/render workflow for your intended use.
### Hardware & software

Published requirements and explicit documentation gaps follow. [Source 1](https://github.com/pascalorg/editor/blob/main/README.md) [Source 2](https://editor.pascal.app/docs/developers/local-editor)

- **Hardware:** A browser/GPU capable of the documented React Three Fiber/WebGPU graphics route is needed. Minimum RAM, VRAM and storage are not published in the inspected overview.
- **Software:** Node >=22.13 for CLI startup. The CLI downloads its versioned editor runtime and runs a local authenticated service; agent/model configuration is separate.
- **Platforms:** Browser and Node CLI paths are documented. A complete tested OS/browser matrix is not supplied in the overview; no on-device AI support is inferred.

### License, model weights & costs

The complete top-level MIT software terms were reviewed and archived today; model/dependency/host terms remain separate. [Source 1](https://github.com/pascalorg/editor/blob/main/LICENSE) [Source 2](https://github.com/pascalorg/editor/blob/main/README.md)

- **Code:** MIT
- **Weights:** MIT covers the released editor code; agent/model terms and imported assets are separate. Pascal Next features should not be assumed to be included in this grant/release.
- **Commercial:** The main MIT code grant permits commercial use under its notice/source and other conditions. Model, component, asset and hosted-service permission is separate. MIT covers the released editor code; agent/model terms and imported assets are separate. Pascal Next features should not be assumed to be included in this grant/release.
- **Cost:** The local editor route needs no Pascal account/API key according to the README. Agent inference or optional hosted services can add costs.

### Why it merits attention

Assessment: a real scene editor with inspectable operations is promising for spatial design. Documentation review only; no building scene was generated. [Source 1](https://github.com/pascalorg/editor/blob/main/README.md)

### Limitations

Hosted-next demos are not evidence that those capabilities ship in the open-source editor. Furniture/space checks are bounded design aids, not unsupported engineering certifications. [Source 1](https://github.com/pascalorg/editor/blob/main/README.md) [Source 2](https://github.com/pascalorg/editor/blob/main/LICENSE)

### Get the tool

- [Repository](https://github.com/pascalorg/editor)
- [Documentation](https://github.com/pascalorg/editor/blob/main/README.md)

## Klarity

Photography, restoration & color · Video, animation & film · Archives, media restoration & collections · Editing, captions & post-production

First detailed guide in this library; documentation checked today. Repository created 2026-03-29; current source metadata is a discovery signal, not evidence of a significant product upgrade.

### How it uses AI

Learned NAFNet, HAT/Real-ESRGAN and RIFE stages provide neural restoration, upscaling and video-frame interpolation. [Source](https://github.com/HAKORADev/Klarity/blob/main/README.md)

### Introduction

A local restoration GUI/CLI composing learned denoising, deblurring, super-resolution and frame interpolation models. [Source 1](https://github.com/HAKORADev/Klarity/blob/main/README.md)

### What it is good for

Prepare a better-viewing copy of a noisy scan or soft video, preserving the original while comparing heavy/light model results. [Source 1](https://github.com/HAKORADev/Klarity/blob/main/README.md)

### Demo & examples

The README links a Hugging Face Space and Colab demo plus release packages; these are developer demo routes. [Source 1](https://github.com/HAKORADev/Klarity/blob/main/README.md) [Source 2](https://huggingface.co/spaces/HAKORADev/Klarity)

### Install

Documentation-based setup route; commands are examples from the project and were not executed during this review. [Source 1](https://github.com/HAKORADev/Klarity/blob/main/README.md)

1. Choose the documented Windows/Linux CPU release, or clone for an isolated Python source installation.
2. Install requirements and FFmpeg for video processing, then start the GUI or CLI.

```sh
pip install -r requirements.txt
```


```sh
python src/klarity.py
```

### First project

Begin with a small, permitted sample and inspect the result. [Source 1](https://github.com/HAKORADev/Klarity/blob/main/README.md)

1. Load your image/video and choose restoration or interpolation mode.
2. Begin with a small light-model preview, then compare a heavier pass if useful.
3. Export a separate result and inspect faces, texture and interpolated motion against the original.
### Hardware & software

Published requirements and explicit documentation gaps follow. [Source 1](https://github.com/HAKORADev/Klarity/blob/main/README.md)

- **Hardware:** The README lists 4 GB RAM for Lite and 8–16 GB for Heavy. Model downloads are about 204/888 MB respectively, not a total disk requirement. Minimum GPU VRAM is not stated.
- **Software:** Python requirements from the repository for source builds; FFmpeg is required for video. An exact minimum Python version is not stated in the inspected quickstart.
- **Platforms:** Prebuilt CPU packages target Windows/Linux. A macOS FFmpeg install example does not prove tested Mac inference support.

### License, model weights & costs

The complete top-level MIT software terms were reviewed and archived today; model/dependency/host terms remain separate. [Source 1](https://github.com/HAKORADev/Klarity/blob/main/LICENSE) [Source 2](https://github.com/HAKORADev/Klarity/blob/main/README.md)

- **Code:** MIT
- **Weights:** MIT covers Klarity code. NAFNet, HAT/Real-ESRGAN, RIFE and individual checkpoints retain independent terms; the whole weight stack was not fully licensed here.
- **Commercial:** The main MIT code grant permits commercial use under its notice/source and other conditions. Model, component, asset and hosted-service permission is separate. MIT covers Klarity code. NAFNet, HAT/Real-ESRGAN, RIFE and individual checkpoints retain independent terms; the whole weight stack was not fully licensed here.
- **Cost:** No paid inference subscription is required by the documented local route. Compute and optional hosted demo limits remain separate.

### Why it merits attention

Assessment: selectable processing modes and local CPU packages support an accessible trial. Speed/quality multipliers are developer claims, not our measurements. [Source 1](https://github.com/HAKORADev/Klarity/blob/main/README.md)

### Limitations

Restoration can invent plausible detail and interpolation can create artifacts. Documentation review only; neither visual fidelity nor quoted performance ratios was tested. [Source 1](https://github.com/HAKORADev/Klarity/blob/main/README.md) [Source 2](https://github.com/HAKORADev/Klarity/blob/main/LICENSE)

### Get the tool

- [Repository](https://github.com/HAKORADev/Klarity)
- [Documentation](https://github.com/HAKORADev/Klarity/blob/main/README.md)
- [Demo](https://huggingface.co/spaces/HAKORADev/Klarity)

## photo-restorer

Photography, restoration & color · Archives, media restoration & collections · Images & design

First detailed guide in this library; documentation checked today. Repository created 2026-04-18; current source metadata is a discovery signal, not evidence of a significant product upgrade.

### How it uses AI

Real-ESRGAN/GFPGAN and related local model assets provide photo enhancement and optional face-restoration passes. [Source](https://github.com/reiarthur/photo-restorer/blob/main/README.md)

### Introduction

A local Python photo-enhancement library with neural super-resolution, optional face restoration and a compact batch-processing API. [Source 1](https://github.com/reiarthur/photo-restorer/blob/main/README.md)

### What it is good for

Build a repeatable restoration pass for permitted photographs, controlling face blending rather than accepting a single opaque cloud result. [Source 1](https://github.com/reiarthur/photo-restorer/blob/main/README.md)

### Demo & examples

The README gives single-image, batch and face-only Python examples. It is a developer library with no documented creator GUI. [Source 1](https://github.com/reiarthur/photo-restorer/blob/main/README.md)

### Install

Documentation-based setup route; commands are examples from the project and were not executed during this review. [Source 1](https://github.com/reiarthur/photo-restorer/blob/main/README.md)

1. Create a Python >=3.12 environment and install the published package.
2. Follow the model-management/configuration guide; the main API needs local weights but no remote API keys.

```sh
pip install photo-restorer
```

### First project

Begin with a small, permitted sample and inspect the result. [Source 1](https://github.com/reiarthur/photo-restorer/blob/main/README.md)

1. Call optimize_image or optimize_images on local source files.
2. Use restore_faces with a restrained blend or disable the face pass when it changes identity.
3. Save a separate output and compare details/color against the original.
### Hardware & software

Published requirements and explicit documentation gaps follow. [Source 1](https://github.com/reiarthur/photo-restorer/blob/main/README.md)

- **Hardware:** CPU mode is documented. Minimum RAM, GPU VRAM and total weight storage are not stated; sufficient model-cache space is required.
- **Software:** Python >=3.12 and package runtime dependencies; local Real-ESRGAN/GFPGAN and helper weights under a configurable models directory.
- **Platforms:** Local Python/CPU operation is described without a complete tested OS/accelerator matrix. Windows, macOS and Linux parity is not asserted.

### License, model weights & costs

The complete top-level MIT software terms were reviewed and archived today; model/dependency/host terms remain separate. [Source 1](https://github.com/reiarthur/photo-restorer/blob/main/LICENSE) [Source 2](https://github.com/reiarthur/photo-restorer/blob/main/README.md)

- **Code:** MIT
- **Weights:** MIT applies to this library. Real-ESRGAN/GFPGAN/helper software and checkpoint terms are separate and need model-specific review.
- **Commercial:** The main MIT code grant permits commercial use under its notice/source and other conditions. Model, component, asset and hosted-service permission is separate. MIT applies to this library. Real-ESRGAN/GFPGAN/helper software and checkpoint terms are separate and need model-specific review.
- **Cost:** No required remote API or paid subscription is documented for the main public API. Local compute costs remain.

### Why it merits attention

Assessment: a small API and controllable face pass suit an archive-processing script. Documentation review only; no image was restored or compared. [Source 1](https://github.com/reiarthur/photo-restorer/blob/main/README.md)

### Limitations

This is not evidence-preserving recovery of lost pixels. Generated facial detail and color changes can be inaccurate; full model terms and output quality remain untested. [Source 1](https://github.com/reiarthur/photo-restorer/blob/main/README.md) [Source 2](https://github.com/reiarthur/photo-restorer/blob/main/LICENSE)

### Get the tool

- [Repository](https://github.com/reiarthur/photo-restorer)
- [Documentation](https://github.com/reiarthur/photo-restorer/blob/main/README.md)

## Additional open-source AI discoveries

Creative AI relevance and software license screened. Full installation, requirements and quality profiles are pending.

### AI Video Production Editor · GPL-3.0

Develop a script, storyboard, previsualization and edited film in an Electron production workspace.
The editor integrates model-generated storyboards and image/video/audio provider jobs with its own node graph, previsualization and timeline.
GPL code is separate from paid fal/Replicate/Gemini/voice/video providers. Node versions and installer routes are documented; full platform, hardware and output review remains pending.

- [Official overview and creative AI workflow](https://github.com/LudwigKienle/ai-video-production-editor/blob/main/README.md)
- [Complete reviewed software license](https://github.com/LudwigKienle/ai-video-production-editor/blob/main/LICENSE)
### OpenTake · GPL-3.0

Use a desktop NLE with semantic media search and AI-assisted timeline operations.
Local SigLIP2 asset understanding and a Rust agent/MCP layer connect AI reasoning to editable media, rather than only returning chat text.
Beta software. Local model terms and memory/storage needs require fuller review; optional cloud agents have separate fees. Source builds and cross-platform behavior were not tested.

- [Official overview and creative AI workflow](https://github.com/appergb/OpenTake/blob/main/README.md)
- [Complete reviewed software license](https://github.com/appergb/OpenTake/blob/main/LICENSE)
### TubeViz · Apache-2.0

Build a music-driven montage from permitted video clips using a designed timeline.
OpenCLIP-assisted clip selection and AI direction produce a persistent media library and beat-synchronized timeline/video workflow.
Model licenses, native GPU configuration and output quality remain pending. Video acquisition helpers do not establish rights to third-party footage or music.

- [Official overview and creative AI workflow](https://github.com/interrupt21h/tubeviz/blob/main/README.md)
- [Complete reviewed software license](https://github.com/interrupt21h/tubeviz/blob/main/LICENSE)
### AIPLAY Studio · Apache-2.0

Experiment with AI composition in a music studio and optional ComfyUI media workflows.
The application integrates YuE2 music generation, local audio inference and optional ComfyUI-generated images/video/3D into an editing workspace.
Apache code is separate from YuE2 non-commercial weights and optional paid APIs. Windows packages and developer GPU examples are documented; full hardware/platform and model-stack review remains pending.

- [Official overview and creative AI workflow](https://github.com/Senzube4n/AIPLAY-Studio/blob/main/README.md)
- [Complete reviewed software license](https://github.com/Senzube4n/AIPLAY-Studio/blob/main/LICENSE)
### FireRed Image Edit · Apache-2.0

Try instruction-based photo changes, multi-image composition and restoration.
The released image-editing model supports neural instruction editing and specialized edit/restoration/try-on workflows with example outputs.
Apache software license reviewed. Checkpoint-specific terms, quantized-memory configurations, installation and output fidelity need a complete profile; we did not edit images.

- [Official overview and creative AI workflow](https://github.com/FireRedTeam/FireRed-Image-Edit/blob/main/README.md)
- [Complete reviewed software license](https://github.com/FireRedTeam/FireRed-Image-Edit/blob/main/LICENSE)
### OpenVTO · MIT

Prototype a consistent studio-avatar, clothing try-on and short fashion-loop application.
A compositional media pipeline combines generative avatar creation, garment substitution and image-to-video output, with a Python SDK, API and mobile playground.
MIT applies to this application pipeline. The documented inference requires Google Vertex AI setup and billing; it is not local open-model inference. Provider terms, model costs, identity fidelity and deployment requirements remain pending.

- [Official overview and creative AI workflow](https://github.com/Prompt-Haus/OpenVTO/blob/main/README.md)
- [Complete reviewed software license](https://github.com/Prompt-Haus/OpenVTO/blob/main/LICENSE)
### Vectra · GPL-3.0

Experiment with placing generated objects into a scanned Gaussian-splat environment.
Its local backend orchestrates U2-Net, SDXL-Lightning and TripoSR to generate and integrate mesh assets in a browser spatial scene.
GPL code license reviewed. The README reports an 8 GB NVIDIA/Linux design; independent verification, model terms, setup completeness and spatial-artifact review remain pending.

- [Official overview and creative AI workflow](https://github.com/parsabe/Vectra/blob/master/README.md)
- [Complete reviewed software license](https://github.com/parsabe/Vectra/blob/master/LICENSE)
### Scenario Blender Plug-in · GPL-3.0

Generate scene-aware reference images, textures or graybox concepts from Blender.
The Blender integration combines viewport/scene context with Scenario AI generation and optional agent control, then brings generated media into the creative workflow.
GPL plug-in requires Blender 5.0+ and a proprietary Scenario account/credits for hosted generation. Experimental features, model terms and exact hardware/platform behavior remain pending.

- [Official overview and creative AI workflow](https://github.com/scenario-labs/blender-plugin/blob/main/README.md)
- [Complete reviewed software license](https://github.com/scenario-labs/blender-plugin/blob/main/LICENSE)
### sprite-animator · MIT

Turn a permitted character image into a small looping pixel-art GIF for prototyping.
The workflow asks Gemini for a guided sprite sheet, optionally creates an approved base sprite first, then slices the grid and assembles animation frames.
MIT workflow code requires proprietary Gemini inference and potentially paid API usage. Frame consistency, source-image rights, provider terms and platform/hardware review remain pending; this is not an open local generative model.

- [Official overview and creative AI workflow](https://github.com/Olafs-World/sprite-animator/blob/main/README.md)
- [Complete reviewed software license](https://github.com/Olafs-World/sprite-animator/blob/main/LICENSE)
### Mine StableDiffusion · GPL-3.0

Explore local image generation with a native mobile/desktop interface and LoRA controls.
The Kotlin multiplatform client embeds stable-diffusion.cpp inference for prompt-driven images, model selection and parameter-bearing PNG exports.
GPL client license reviewed. The README shows Android/iOS and desktop routes; device-specific memory, GPU backend, build versions and individual checkpoint permissions need a complete profile.

- [Official overview and creative AI workflow](https://github.com/Onion99/KMP-MineStableDiffusion/blob/master/README.md)
- [Complete reviewed software license](https://github.com/Onion99/KMP-MineStableDiffusion/blob/master/LICENSE)
### Leap MCP · MIT

Draft a short mathematical or scientific explainer with animation and narration.
The MCP tool couples model-authored explanations with Manim-based visual rendering and narrated explainer production.
MIT code is separate from its OpenAI/provider account and charges. Rendering dependencies, language-model correctness, narration terms and hardware review remain pending.

- [Official overview and creative AI workflow](https://github.com/sid-thephysicskid/leap-mcp/blob/main/README.md)
- [Complete reviewed software license](https://github.com/sid-thephysicskid/leap-mcp/blob/main/LICENSE)
### kimchi · MIT

Generate a missing shot or bridge between clips directly in a desktop edit.
Its Rust video timeline integrates image/video model jobs, saved generation recipes and agent/MCP operations with conventional trimming and export.
New repository, not a validated production editor. Local-model versus paid-provider routes, installers, compute needs and generation/export quality remain pending.

- [Official overview and creative AI workflow](https://github.com/ludovic111/kimchi/blob/main/README.md)
- [Complete reviewed software license](https://github.com/ludovic111/kimchi/blob/main/LICENSE)
### AIMO · MIT

Revise code-authored motion graphics by selecting the visible element in an editor.
An embedded Claude/agent layer uses the selected frame and code-linked element context to revise animations, with MCP operations and optional generated images.
MIT code is separate from Claude and OpenRouter/Vercel model charges. Export reliability, code tracing, platform requirements and asset-license handling remain pending.

- [Official overview and creative AI workflow](https://github.com/uxKero/aimo/blob/main/README.md)
- [Complete reviewed software license](https://github.com/uxKero/aimo/blob/main/LICENSE)
### mocap-skills · MIT

Reconstruct a side-view character walk as Blender skeletal animation and compare its silhouette with a reference.
AI coding-agent workflows orchestrate frame measurements, inverse kinematics and Blender rendering from AI-generated or filmed references; the current method is not a trained general 3D pose estimator.
Blender 5.1+, FFmpeg and NumPy are documented. Rig mappings are specialized; published silhouette scores are author evidence. General motion, licensing of the agent/reference assets and hardware review remain pending.

- [Official overview and creative AI workflow](https://github.com/xbishi/mocap-skills/blob/main/README.md)
- [Complete reviewed software license](https://github.com/xbishi/mocap-skills/blob/main/LICENSE)
### Novel to Manga and Anime Generator · MIT

Turn a permitted chapter into manga panels, webtoon layouts or an anime production brief.
Agent workflows plan characters, consistent reference sheets, panels and shots, then provide prompts/API scripts for generated images and video.
MIT workflow code is separate from required generation providers; the README offers paid BytePlus subscription/API routes. Source-story rights, model terms, output consistency and installation review remain pending.

- [Official overview and creative AI workflow](https://github.com/BBQ2077/novel-to-manga-anime-generator/blob/main/README.md)
- [Complete reviewed software license](https://github.com/BBQ2077/novel-to-manga-anime-generator/blob/main/LICENSE)
### Recursive Visual State Video · MIT

Explore a sequence of generated frames with periodic drift checks and silent video encoding.
A coding-agent workflow feeds the previous generated image into the next generation, tracks cumulative visual drift and packages the resulting frame sequence.
Evidence is an 11-frame pilot with observed drift, not a long-video benchmark. Image-model/agent availability and fees, motion quality, dependencies and platform behavior remain pending.

- [Official overview and creative AI workflow](https://github.com/ouruocun-dotcom/recursive-visual-state-video/blob/main/README.md)
- [Complete reviewed software license](https://github.com/ouruocun-dotcom/recursive-visual-state-video/blob/main/LICENSE)
### Talking-head Video Workflow · MIT

Plan and edit spoken-word footage through explicit human review stages.
The Chinese-language agent workflow combines model-planned editing/design with transcription and editor/MCP tool calls to produce a finished spoken-video draft.
MIT applies to workflow documents/utilities. The current tool path uses ChatCut Desktop and a separate transcriber/agent; host licenses, costs and end-to-end reproducibility remain pending.

- [Official overview and creative AI workflow](https://github.com/zoushunyu144000-ui/oral-video-workflow/blob/main/README.md)
- [Complete reviewed software license](https://github.com/zoushunyu144000-ui/oral-video-workflow/blob/main/LICENSE)
### PPT Master · MIT

Create a natively editable slide deck from a topic, document or paper.
An AI-agent workflow reasons over source material and generates native PowerPoint shapes, charts, tables and animation through local authoring utilities.
MIT source includes extensive examples. Model/agent terms and fees, PowerPoint/rendering host requirements, source-grounding and installation/output review remain pending; sponsor marketing is not evidence of quality.

- [Official overview and creative AI workflow](https://github.com/hugohe3/ppt-master/blob/main/README.md)
- [Complete reviewed software license](https://github.com/hugohe3/ppt-master/blob/main/LICENSE)
### VideoCaptioner · GPL-3.0

Prepare, correct and translate subtitles for multilingual video publishing.
The application combines speech transcription with LLM-assisted subtitle segmentation, correction and translation.
GPL software terms reviewed. Local versus hosted transcription/model routes, service fees, platform/memory support and caption accuracy require a full profile.

- [Official overview and creative AI workflow](https://github.com/WEIFENG2333/VideoCaptioner/blob/master/README.md)
- [Complete reviewed software license](https://github.com/WEIFENG2333/VideoCaptioner/blob/master/LICENSE)
### SuperSplat · MIT

Edit, optimize and publish a learned Gaussian-splat scene for a web exhibition.
This is a specialized authoring tool for neural Gaussian-splat reconstructions: it manipulates the learned scene representation rather than generating text or images.
MIT editor terms reviewed. It does not train a reconstruction model itself; capture/training tools and assets are separately licensed. Browser/GPU limits, export behavior and quality remain pending.

- [Official overview and creative AI workflow](https://github.com/playcanvas/supersplat/blob/main/README.md)
- [Complete reviewed software license](https://github.com/playcanvas/supersplat/blob/main/LICENSE)
### EasyEdit · MIT

Create a montage or captioned spoken-video draft from your own media.
The local-first agent workflow analyzes media and directs captioned speech editing or music-driven shot assembly through its editing utilities.
MIT code reviewed. Model/provider routes, audio/footage permissions, installation, compute requirements and edit quality need further review.

- [Official overview and creative AI workflow](https://github.com/blixvip/easyedit/blob/main/README.md)
- [Complete reviewed software license](https://github.com/blixvip/easyedit/blob/main/LICENSE)
### Design OS 3D Blender · MIT

Use an agent to build a Blender asset with explicit render and geometry review steps.
Its AI-agent workflows translate a design brief into Blender modeling operations and evidence/render checks, including specialized fabrication-oriented validation steps.
MIT workflow license does not relicense Blender, models or assets. Stated print gates are not a certification of manufacturability; version/hardware and output review remain pending.

- [Official overview and creative AI workflow](https://github.com/jangtrinh/design-os-3d-blender/blob/main/README.md)
- [Complete reviewed software license](https://github.com/jangtrinh/design-os-3d-blender/blob/main/LICENSE)
### Pixel2Motion · MIT

Explore converting a bitmap logo into an animated SVG/HTML asset and video preview.
Agent workflows analyze a raster reference, produce vector geometry and generate motion code with rendering/QA utilities.
MIT code is separate from the AI-agent backend and any hosted service. Vector fidelity, dependencies, output compatibility and platform requirements remain pending.

- [Official overview and creative AI workflow](https://github.com/nolangz/pixel2motion/blob/main/README.md)
- [Complete reviewed software license](https://github.com/nolangz/pixel2motion/blob/main/LICENSE)
### SplatKit · MIT

Embed learned Gaussian-splat captures in a native mobile creative experience.
The SDK renders neural Gaussian-splat representations on Metal/Vulkan and packages captured worlds for mobile interaction; it is an AI-asset renderer, not a generator or training system.
MIT beta SDK. Android API/GPU constraints are documented; iOS/React Native version support, preparation dependencies, asset permissions and performance review remain pending. No headset support was verified.

- [Official overview and creative AI workflow](https://github.com/Xget7/splatkit/blob/main/README.md)
- [Complete reviewed software license](https://github.com/Xget7/splatkit/blob/main/LICENSE)
### Lumen AI Video Editor · MIT

Try agent-directed timeline editing with local captions and motion-graphics integration.
Its editing engine offers typed undoable agent/MCP operations and local Whisper transcription, with Blender/HyperFrames motion workflows.
MIT code reviewed. Windows emphasis, model/dependency terms, optional cloud routes, hardware needs and export reliability remain pending.

- [Official overview and creative AI workflow](https://github.com/Mas-inx/lumen-ai-video-editor/blob/main/README.md)
- [Complete reviewed software license](https://github.com/Mas-inx/lumen-ai-video-editor/blob/main/LICENSE)
### CVAT Community · MIT

Prepare labeled visual material for a custom creative computer-vision project.
Self-hosted AI auto-annotation connects detection, segmentation and tracking models to image/video/3D annotation and review workflows.
MIT core with separately licensed serverless/model components and distinct paid hosted products. Docker setup, unsupported Safari/WebKit, compute needs and model/annotation quality require a full profile.

- [Official overview and creative AI workflow](https://github.com/cvat-ai/cvat/blob/develop/README.md)
- [Complete reviewed software license](https://github.com/cvat-ai/cvat/blob/develop/LICENSE)
### MMagic · Apache-2.0

Build a custom image/video generation, inpainting or restoration workflow from a model toolbox.
The research/developer toolbox supplies neural generative and restoration models with training and inference utilities for visual-media tasks.
Apache core license reviewed. Individual model weights/data, supported runtime versions, GPU memory and deployment/quality remain pending; not a turnkey creator app.

- [Official overview and creative AI workflow](https://github.com/open-mmlab/mmagic/blob/main/README.md)
- [Complete reviewed software license](https://github.com/open-mmlab/mmagic/blob/main/LICENSE)
### SD.Next · Apache-2.0

Explore self-hosted generation, refinement, captioning and upscaling in a configurable media UI.
The application orchestrates diffusion/image/video inference backends and processing workflows behind a local web interface.
Apache application code reviewed. Backend/model licenses, download size, device/version support and output quality need a complete profile; a browser UI alone does not prove Mac support.

- [Official overview and creative AI workflow](https://github.com/vladmandic/sdnext/blob/master/README.md)
- [Complete reviewed software license](https://github.com/vladmandic/sdnext/blob/master/LICENSE.txt)
### Jellyfish · Apache-2.0

Prototype an AI short-drama workflow from script and storyboard to generated shots.
The production application connects story planning, character/shot consistency and image/video generation jobs with media project management and export.
Apache application license reviewed. Provider/model terms, payments, deployment, minimum memory and consistency/export quality remain pending.

- [Official overview and creative AI workflow](https://github.com/Forget-C/Jellyfish/blob/main/README.md)
- [Complete reviewed software license](https://github.com/Forget-C/Jellyfish/blob/main/LICENSE)
### Wonder3D · MIT

Reconstruct a candidate game or exhibition object from a single image.
Cross-domain diffusion produces multi-view colors and normals, which are used in its 3D mesh reconstruction pipeline.
MIT code reviewed. Model/dependency permissions, GPU requirements, mesh fidelity and installation need a full profile; generated meshes are not automatically print-ready.

- [Official overview and creative AI workflow](https://github.com/xxlong0/Wonder3D/blob/main/README.md)
- [Complete reviewed software license](https://github.com/xxlong0/Wonder3D/blob/main/LICENSE)
### ArcReel · AGPL-3.0

Develop a consistent short film from a novel, script or product brief with an editable production workflow.
Agent planning connects character assets, storyboards and multi-provider image/video generation with project management and exports.
Full AGPL-3.0 license reviewed, including source obligations for modified network services. Model/provider costs and permissions, hardware, deployment and output reliability remain pending.

- [Official overview and creative AI workflow](https://github.com/ArcReel/ArcReel/blob/main/README.md)
- [Complete reviewed software license](https://github.com/ArcReel/ArcReel/blob/main/LICENSE)
### PersonaLive · Apache-2.0

Experiment with portrait animation for a live character or streaming presentation.
The research system generates portrait motion from an identity image and driving signals, with online/offline inference routes and released training code.
Apache code license reviewed. Portrait/driver rights, checkpoint terms, live latency, exact GPU/platform requirements and artifact quality remain pending; no stream was tested.

- [Official overview and creative AI workflow](https://github.com/GVCLab/PersonaLive/blob/main/README.md)
- [Complete reviewed software license](https://github.com/GVCLab/PersonaLive/blob/main/LICENSE)
### 4D Gaussian Splatting · Apache-2.0

Reconstruct a dynamic scene for experimental volumetric playback.
The neural deformation/4D Gaussian representation learns time-varying appearance and geometry from captured observations.
Apache top-level code reviewed. Rasterizer/dependency and dataset terms, training requirements, capture assumptions and playback quality remain pending.

- [Official overview and creative AI workflow](https://github.com/hustvl/4DGaussians/blob/master/README.md)
- [Complete reviewed software license](https://github.com/hustvl/4DGaussians/blob/master/LICENSE.md)
### LichtFeld Studio · GPL-3.0

Train, inspect and edit a neural Gaussian scene in a native application.
The studio integrates learned Gaussian-splat reconstruction/training with visual editing, COLMAP inputs, plug-ins and optional MCP automation.
GPL source terms reviewed. CUDA/platform support, GPU memory, reconstruction dependencies, asset licenses and output quality require a complete profile.

- [Official overview and creative AI workflow](https://github.com/MrNeRF/LichtFeld-Studio/blob/master/README.md)
- [Complete reviewed software license](https://github.com/MrNeRF/LichtFeld-Studio/blob/master/LICENSE)
### Fugleramme · MIT

Create a living bird-illustration display reacting to species heard near a microphone.
Local BirdNET-Go audio classification selects curated bird illustrations and updates an e-ink or web display when detections change; the illustrations are not generated by the classifier.
MIT frame code is separate from BirdNET-Go/model terms and CC-BY-SA artwork. Raspberry Pi/e-ink hardware is documented; memory, setup and recognition/display quality remain pending.

- [Official overview and creative AI workflow](https://github.com/arnegiacomo/fugleramme/blob/main/README.md)
- [Complete reviewed software license](https://github.com/arnegiacomo/fugleramme/blob/main/LICENSE)
### Lyra · Apache-2.0

Explore generative 3D/4D environments and controllable scene video as a research workflow.
The released Lyra research stacks use generative world models for reconstructed/generated spatial scenes and novel-view/video workflows.
Apache code reviewed. Lyra version/checkpoint licenses, CUDA/compute requirements, GUI setup and scene consistency need a complete profile; no interactive world was generated.

- [Official overview and creative AI workflow](https://github.com/nv-tlabs/lyra/blob/main/README.md)
- [Complete reviewed software license](https://github.com/nv-tlabs/lyra/blob/main/LICENSE)
### PartCrafter · MIT

Experiment with a single-image 3D object represented as separately controllable parts.
A compositional latent-diffusion model generates structured multi-part meshes rather than only a single fused object.
MIT code reviewed. Checkpoint/dependency terms, GPU setup, part quality and topology validation remain pending; part separation does not establish printing readiness.

- [Official overview and creative AI workflow](https://github.com/wgsxm/PartCrafter/blob/main/README.md)
- [Complete reviewed software license](https://github.com/wgsxm/PartCrafter/blob/main/LICENSE)
### Efficient Gaussian Appearance · Apache-2.0

Investigate compact view-dependent appearance for a captured scene and browser display.
Its learned Gaussian appearance models fit neural scene color/appearance and include a lightweight viewing/export workflow.
Apache code reviewed. Capture data and model dependencies, fitting requirements, mobile/browser compatibility and appearance quality remain pending; research implementation, not a finished creator application.

- [Official overview and creative AI workflow](https://github.com/nerficg-project/efficient-gaussian-appearance/blob/main/README.md)
- [Complete reviewed software license](https://github.com/nerficg-project/efficient-gaussian-appearance/blob/main/LICENSE)
### TikTok Video Skills · MIT

Design vertical short-form films, timed captions and countdowns.
An AI coding-agent workflow supplies media-specific planning and implementation guidance for this task, using ordinary rendering tools rather than bundling a trained model. Design vertical short-form films, timed captions and countdowns.
MIT workflow/skill source reviewed. External coding-agent terms and fees, renderer/host licenses, exact dependencies, hardware/platform requirements and final design quality need a full profile. Marketing demos are not our tests.

- [Official overview and creative AI workflow](https://github.com/iart-ai/tiktok-video-skills/blob/main/README.md)
- [Complete reviewed software license](https://github.com/iart-ai/tiktok-video-skills/blob/main/LICENSE)
### Text Message Video Skills · MIT

Turn a scripted chat into a timed animated conversation.
An AI coding-agent workflow supplies media-specific planning and implementation guidance for this task, using ordinary rendering tools rather than bundling a trained model. Turn a scripted chat into a timed animated conversation.
MIT workflow/skill source reviewed. External coding-agent terms and fees, renderer/host licenses, exact dependencies, hardware/platform requirements and final design quality need a full profile. Marketing demos are not our tests.

- [Official overview and creative AI workflow](https://github.com/iart-ai/text-message-video-skills/blob/main/README.md)
- [Complete reviewed software license](https://github.com/iart-ai/text-message-video-skills/blob/main/LICENSE)
### YouTube Video Skills · MIT

Make a branded intro/outro or captioned podcast audiogram.
An AI coding-agent workflow supplies media-specific planning and implementation guidance for this task, using ordinary rendering tools rather than bundling a trained model. Make a branded intro/outro or captioned podcast audiogram.
MIT workflow/skill source reviewed. External coding-agent terms and fees, renderer/host licenses, exact dependencies, hardware/platform requirements and final design quality need a full profile. Marketing demos are not our tests.

- [Official overview and creative AI workflow](https://github.com/iart-ai/youtube-video-skills/blob/main/README.md)
- [Complete reviewed software license](https://github.com/iart-ai/youtube-video-skills/blob/main/LICENSE)
### E-commerce Video Skills · MIT

Animate product screenshots, sale information or a permitted photo collection.
An AI coding-agent workflow supplies media-specific planning and implementation guidance for this task, using ordinary rendering tools rather than bundling a trained model. Animate product screenshots, sale information or a permitted photo collection.
MIT workflow/skill source reviewed. External coding-agent terms and fees, renderer/host licenses, exact dependencies, hardware/platform requirements and final design quality need a full profile. Marketing demos are not our tests.

- [Official overview and creative AI workflow](https://github.com/iart-ai/ecommerce-video-skills/blob/main/README.md)
- [Complete reviewed software license](https://github.com/iart-ai/ecommerce-video-skills/blob/main/LICENSE)
### Ad Video Skills · MIT

Produce variants of a product launch, testimonial or data-driven ad film.
An AI coding-agent workflow supplies media-specific planning and implementation guidance for this task, using ordinary rendering tools rather than bundling a trained model. Produce variants of a product launch, testimonial or data-driven ad film.
MIT workflow/skill source reviewed. External coding-agent terms and fees, renderer/host licenses, exact dependencies, hardware/platform requirements and final design quality need a full profile. Marketing demos are not our tests.

- [Official overview and creative AI workflow](https://github.com/iart-ai/ad-video-skills/blob/main/README.md)
- [Complete reviewed software license](https://github.com/iart-ai/ad-video-skills/blob/main/LICENSE)
### Data Animation Skills · MIT

Animate a chart, infographic or presentation from supplied data.
An AI coding-agent workflow supplies media-specific planning and implementation guidance for this task, using ordinary rendering tools rather than bundling a trained model. Animate a chart, infographic or presentation from supplied data.
MIT workflow/skill source reviewed. External coding-agent terms and fees, renderer/host licenses, exact dependencies, hardware/platform requirements and final design quality need a full profile. Marketing demos are not our tests.

- [Official overview and creative AI workflow](https://github.com/iart-ai/data-animation-skills/blob/main/README.md)
- [Complete reviewed software license](https://github.com/iart-ai/data-animation-skills/blob/main/LICENSE)
### Explainer Video Skills · MIT

Plan and render narrated explainers, diagram reveals or recap films.
An AI coding-agent workflow supplies media-specific planning and implementation guidance for this task, using ordinary rendering tools rather than bundling a trained model. Plan and render narrated explainers, diagram reveals or recap films.
MIT workflow/skill source reviewed. External coding-agent terms and fees, renderer/host licenses, exact dependencies, hardware/platform requirements and final design quality need a full profile. Marketing demos are not our tests.

- [Official overview and creative AI workflow](https://github.com/iart-ai/explainer-video-skills/blob/main/README.md)
- [Complete reviewed software license](https://github.com/iart-ai/explainer-video-skills/blob/main/LICENSE)
### Map Animation Skills · MIT

Build an editorial map sequence with routes, camera moves and labels.
An AI coding-agent workflow supplies media-specific planning and implementation guidance for this task, using ordinary rendering tools rather than bundling a trained model. Build an editorial map sequence with routes, camera moves and labels.
MIT workflow/skill source reviewed. External coding-agent terms and fees, renderer/host licenses, exact dependencies, hardware/platform requirements and final design quality need a full profile. Marketing demos are not our tests.

- [Official overview and creative AI workflow](https://github.com/iart-ai/map-animation-skills/blob/main/README.md)
- [Complete reviewed software license](https://github.com/iart-ai/map-animation-skills/blob/main/LICENSE)
### Web Animation Skills · MIT

Design web transitions, SVG/Lottie motion and reduced-motion interaction variants.
An AI coding-agent workflow supplies media-specific planning and implementation guidance for this task, using ordinary rendering tools rather than bundling a trained model. Design web transitions, SVG/Lottie motion and reduced-motion interaction variants.
MIT workflow/skill source reviewed. External coding-agent terms and fees, renderer/host licenses, exact dependencies, hardware/platform requirements and final design quality need a full profile. Marketing demos are not our tests.

- [Official overview and creative AI workflow](https://github.com/iart-ai/web-animation-skills/blob/main/README.md)
- [Complete reviewed software license](https://github.com/iart-ai/web-animation-skills/blob/main/LICENSE)
### Motion Design Skills · MIT

Direct a branded animation with timing, composition and color workflows.
An AI coding-agent workflow supplies media-specific planning and implementation guidance for this task, using ordinary rendering tools rather than bundling a trained model. Direct a branded animation with timing, composition and color workflows.
MIT workflow/skill source reviewed. External coding-agent terms and fees, renderer/host licenses, exact dependencies, hardware/platform requirements and final design quality need a full profile. Marketing demos are not our tests.

- [Official overview and creative AI workflow](https://github.com/iart-ai/motion-design-skills/blob/main/README.md)
- [Complete reviewed software license](https://github.com/iart-ai/motion-design-skills/blob/main/LICENSE)
### Kinetic Typography Skills · MIT

Animate headlines, lyrics or title cards with code-driven timing.
An AI coding-agent workflow supplies media-specific planning and implementation guidance for this task, using ordinary rendering tools rather than bundling a trained model. Animate headlines, lyrics or title cards with code-driven timing.
MIT workflow/skill source reviewed. External coding-agent terms and fees, renderer/host licenses, exact dependencies, hardware/platform requirements and final design quality need a full profile. Marketing demos are not our tests.

- [Official overview and creative AI workflow](https://github.com/iart-ai/kinetic-typography-skills/blob/main/README.md)
- [Complete reviewed software license](https://github.com/iart-ai/kinetic-typography-skills/blob/main/LICENSE)
### Freelance Motion Skills · MIT

Structure an animation brief, revisions, delivery specification and brand-motion guide.
An AI coding-agent workflow supplies media-specific planning and implementation guidance for this task, using ordinary rendering tools rather than bundling a trained model. Structure an animation brief, revisions, delivery specification and brand-motion guide.
MIT workflow/skill source reviewed. External coding-agent terms and fees, renderer/host licenses, exact dependencies, hardware/platform requirements and final design quality need a full profile. Marketing demos are not our tests.

- [Official overview and creative AI workflow](https://github.com/iart-ai/freelance-motion-skills/blob/main/README.md)
- [Complete reviewed software license](https://github.com/iart-ai/freelance-motion-skills/blob/main/LICENSE)
### WebGL Animation Skills · MIT

Author GLSL effects, Three.js animation or particle scenes.
An AI coding-agent workflow supplies media-specific planning and implementation guidance for this task, using ordinary rendering tools rather than bundling a trained model. Author GLSL effects, Three.js animation or particle scenes.
MIT workflow/skill source reviewed. External coding-agent terms and fees, renderer/host licenses, exact dependencies, hardware/platform requirements and final design quality need a full profile. Marketing demos are not our tests.

- [Official overview and creative AI workflow](https://github.com/iart-ai/webgl-animation-skills/blob/main/README.md)
- [Complete reviewed software license](https://github.com/iart-ai/webgl-animation-skills/blob/main/LICENSE)
### Manim Skills · MIT

Build a mathematical explainer using model-authored Manim code.
An AI coding-agent workflow supplies media-specific planning and implementation guidance for this task, using ordinary rendering tools rather than bundling a trained model. Build a mathematical explainer using model-authored Manim code.
MIT workflow/skill source reviewed. External coding-agent terms and fees, renderer/host licenses, exact dependencies, hardware/platform requirements and final design quality need a full profile. Marketing demos are not our tests.

- [Official overview and creative AI workflow](https://github.com/iart-ai/manim-skills/blob/main/README.md)
- [Complete reviewed software license](https://github.com/iart-ai/manim-skills/blob/main/LICENSE)
### JavaScript Animation Skills · MIT

Create a code-drawn canvas film with synthesized Web Audio and frame-based export.
An AI coding-agent workflow supplies media-specific planning and implementation guidance for this task, using ordinary rendering tools rather than bundling a trained model. Create a code-drawn canvas film with synthesized Web Audio and frame-based export.
MIT workflow/skill source reviewed. External coding-agent terms and fees, renderer/host licenses, exact dependencies, hardware/platform requirements and final design quality need a full profile. Marketing demos are not our tests.

- [Official overview and creative AI workflow](https://github.com/iart-ai/javascript-animation-skills/blob/main/README.md)
- [Complete reviewed software license](https://github.com/iart-ai/javascript-animation-skills/blob/main/LICENSE)
### Lower Thirds Skills · MIT

Generate a transparent animated name card for a stream or edited video.
An AI coding-agent workflow supplies media-specific planning and implementation guidance for this task, using ordinary rendering tools rather than bundling a trained model. Generate a transparent animated name card for a stream or edited video.
MIT workflow/skill source reviewed. External coding-agent terms and fees, renderer/host licenses, exact dependencies, hardware/platform requirements and final design quality need a full profile. Marketing demos are not our tests.

- [Official overview and creative AI workflow](https://github.com/iart-ai/lower-thirds-skills/blob/main/README.md)
- [Complete reviewed software license](https://github.com/iart-ai/lower-thirds-skills/blob/main/LICENSE)

## Excluded and unresolved findings

Research notes only; these do not enter the eligible tool library.

- **KineTy** · excluded: Its complete software license is CC-BY-NC 4.0, with a non-commercial restriction. Strong kinetic-typography research relevance does not make that an open-source software license. [Source](https://github.com/SeonmiP/KineTy) [Source](https://github.com/SeonmiP/KineTy/blob/main/LICENSE)
- **AnimateDiff** · needs-license-review: The top-level Apache-2.0 text is archived, but the README also states academic use. That scope ambiguity and separate base/motion weights prevent promoting the earlier pending entry to an unrestricted complete recommendation today; the historical library listing remains dated. [Source](https://github.com/guoyww/AnimateDiff) [Source](https://github.com/guoyww/AnimateDiff/blob/main/LICENSE)
- **kin3o** · needs-license-review: A registry/README MIT label and a concrete 3D-design workflow were found, but a complete software license file was not obtained from the tested source paths. It remains outside eligible profiles/leads. [Source](https://github.com/affromero/kin3o) [Source](https://www.npmjs.com/package/%40afromero/kin3o)
- **clothes-changer** · needs-license-review: The fashion workflow is relevant, but no complete software license was obtained from the tested standard paths. An AI feature or a public repository does not establish redistribution permission. [Source](https://github.com/alhussein-jamil/clothes-changer)
- **3D New Era AI** · needs-license-review: GitHub metadata suggested Apache-2.0, but the complete software terms were not located in the inspected paths. Metadata alone does not satisfy this edition’s license-archive gate. [Source](https://github.com/leandrodaf/3d-new-era-ai)
- **DreamCraft3D** · needs-license-review: A research repository and MIT metadata were found, but the full software license was not obtained in this pass. No new eligible guide or lead is claimed without the complete reviewed text. [Source](https://github.com/deepseek-ai/DreamCraft3D)
- **TransText** · needs-license-review: The official research/demo page is relevant to animated typography, but released implementation and complete software-license evidence were not established. [Source](https://sii-ferenas.github.io/TransText/)
- **Generative Illustration Skills pack** · needs-license-review: The installable pack was discovered through a motion-skills directory, but a complete license for this specific repository was not found. A parent directory’s MIT claim was not applied automatically. [Source](https://github.com/iart-ai/generative-illustration-skills)
- **photo-restoration-enhancer** · excluded: The README advertises a standalone restoration app, but both main.py and Program.cs in the inspected source tree were empty. No usable open implementation was established; download-page and hardware claims alone were not enough. [Source](https://github.com/GridMayorTell/photo-restoration-enhancer)
- **Motion Graphics Skills directory** · excluded: This repository is an index of separate installable packs rather than a distinct implementation. Eligible individual packs are screened separately, avoiding a duplicate directory entry. [Source](https://github.com/iart-ai/motion-skills)
- **3D Data Materials tutorial collection** · excluded: Several kits are generic geometry or explicitly simulated model outputs, while actual Depth-Anything inference points to another repository. The collection was not counted as a newly verified AI tool; its linked implementation remains future research. [Source](https://github.com/florentPoux/3d-data-materials)
- **cutan** · excluded: The inspected overview describes cutout-animation tools but did not establish a concrete AI-model contribution in this package. Generic digital-media utility alone does not meet the AI-only scope. [Source](https://github.com/thorwhalen/cutan)

Source collection completed: 2026-10-02T12:23:59.776911+00:00
Search is a bounded sample. Stars and recent pushes are discovery signals, not verified quality or meaningful upgrades.
