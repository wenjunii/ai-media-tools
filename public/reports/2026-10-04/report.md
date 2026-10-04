# AI Media Scout — 2026-10-04

Today's full expanded search produced 25 detailed documentation-reviewed guides, including 10 completions from the earlier review queue, plus 19 additional screened discoveries. Subjects include local narration, music and dance, editable calligraphy, garment-pattern research, immersive web scenes, learned reconstruction and agent-assisted video production. LocalText2Voice's latest release adds voice-cloning/emotion controls; this is its first library guide. All 230 planned repository queries and 14 model-task queries completed across 36 fields, retaining 19,426 repository candidates including seven additional archived repositories, plus 662 model leads. Ninety-five repository searches reached result bounds; Codeberg and SourceHut have explicit research gaps. Counts are discovery observations, not quality approvals or exhaustive coverage. Full licenses were archived and reviewed for every included tool; model restrictions, proprietary dependencies and unavailable demos are identified separately. No discovered software was installed or executed.

Documentation reviewed today. Tools are not hands-on tested unless explicitly stated. Requirements and performance remain source-specific.

## Coverage

| Field | Finding |
| --- | --- |
| Images & design | ReShot prepares depth/pose controls, while SANA and imaginAIry broaden generation and image-processing options. Requirements and model permissions vary by exact checkpoint. [Source 1](https://nvlabs.github.io/Sana/docs/) [Source 2](https://brycedrennan.github.io/imaginAIry/) |
| Video, animation & film | MoneyPrinterTurbo, OpenMontage and brag connect scripts, narration, visual assets and rendering. Sources describe intended workflows; this edition did not generate or evaluate a finished film. [Source 1](https://harry0703.github.io/mpt-assets/) [Source 2](https://www.openmontage.video/) [Source 3](https://latent-spaces.github.io/brag/) |
| Audio, music & voice | VoiceStudio and LocalText2Voice offer editable narration workflows; YuE2 pairs music with symbolic scores. Open application code does not remove non-commercial conditions on some default models. [Source 1](https://voicestudio.sh/) [Source 2](https://map-yue2.github.io/) |
| 3D, reconstruction & assets | Wonder3D turns an image into multiview predictions and a mesh; GaussianGPT generates or completes Gaussian scenes. These are distinct representations, with different editing and deployment constraints. [Source 1](https://www.xxlong.site/Wonder3D/) [Source 2](https://nicolasvonluetzow.github.io/GaussianGPT/) |
| Browser tools & web media | Immersive Web SDK and AntV Infographic provide concrete AI-assisted authoring routes for browser media. Their renderers are deterministic; inference is supplied by the connected AI workflow. [Source 1](https://iwsdk.dev/) [Source 2](https://infographic.antv.vision/) |
| WebXR, VR & AR | Meta documents agent-assisted scene inspection and iteration for Immersive Web SDK. Headset testing is still necessary for interaction, comfort and performance; a desktop preview is not headset validation. [Source 1](https://developers.meta.com/vr/blog/accelerate-vr-development-with-ai-and-immersive-web-sdk/) |
| Computational art & creative coding | YuE2 exposes an editable musical representation, while GaussianGPT uses scene tokens and Shodō uses editable vector gestures. These support inspectable computational practice rather than only final-image output. [Source 1](https://map-yue2.github.io/) [Source 2](https://nicolasvonluetzow.github.io/GaussianGPT/) |
| Interactive, immersive & live media | Immersive Web SDK supports agent-driven scene workflows; JoyAI-Video-Edit is a screened live-video editing research lead. Published real-time benchmarks are hardware-specific. [Source 1](https://iwsdk.dev/) [Source 2](https://developers.meta.com/vr/blog/accelerate-vr-development-with-ai-and-immersive-web-sdk/) |
| 3D printing & generative CAD | Wonder3D examples include physical output, and Bambu Studio AI is screened for generative models and preparation checks. Neither a mesh export nor a model score establishes safe, successful printing. [Source 1](https://www.xxlong.site/Wonder3D/) [Source 2](https://github.com/heyixuan2/bambu-studio-ai) |
| Games & production pipelines | Wonder3D and GaussianGPT can supply experimental objects/environments; motion-generation leads address character staging. Runtime budgets, topology, collision and asset rights still require production review. [Source 1](https://www.xxlong.site/Wonder3D/) [Source 2](https://nicolasvonluetzow.github.io/GaussianGPT/) |
| Motion capture & character animation | AtomicDance and DiscoForcing broaden music-to-motion research, with MotionMind retained for capture/retargeting follow-up. Research examples do not establish reliable game-ready or physically executable animation. [Source 1](https://cxhcmhhh.github.io/AtomicDanceProject/) [Source 2](https://discoforcing.github.io/) |
| Avatars, digital humans & lip sync | LatentSync addresses lip synchronization; music-conditioned body motion offers a separate avatar workflow. Model/body/character licenses and preservation of identity need review independently of application code. [Source 1](https://discoforcing.github.io/) [Source 2](https://github.com/ByteDance/LatentSync) |
| VFX, compositing & relighting | ReShot provides learned control passes; Robust Video Matting and BackgroundRemover get complete guides. Subtitles-removal software was held back because its ProPainter component carries non-commercial software terms. [Source 1](https://pypi.org/project/backgroundremover/) [Source 2](https://github.com/maosika-ai/reshot/blob/main/docs/USAGE.md) |
| Spatial audio & volumetric media | Neural Acoustic Fields research describes learned room-dependent sound responses; Gaussian scene tools address visual spaces. These are separate pipelines, not a verified integrated immersive system. [Source 1](https://mitibm.mit.edu/research/blog/learning-neural-acoustic-fields/) [Source 2](https://nicolasvonluetzow.github.io/GaussianGPT/) |
| Photogrammetry, scanning & neural rendering | Spirula Studio and OOOSplat bring reconstruction into desktop workflows; Wonder3D handles single-image inference rather than measured multi-view capture. The main Spirula website was inaccessible, so its reviewed repository/releases carry the setup evidence. [Source 1](https://www.xxlong.site/Wonder3D/) [Source 2](https://github.com/harry7557558/spirula-studio) |
| Editing, captions & post-production | VideoLingo covers transcription, translation and dubbing; FireRed-OpenStoryline and Velocut add agent-assisted editing leads. Captions and synthesized audio still need human editorial review. [Source 1](https://videolingo.io/en) [Source 2](https://www.openmontage.video/) |
| Vector graphics, illustration & textures | AntV Infographic creates editable SVG structures and Shodō preserves vector brush paths. These are useful AI-authoring interfaces, without implying that every render operation itself uses AI. [Source 1](https://infographic.antv.vision/learn/getting-started) [Source 2](https://drawyourfont.com/) |
| Typography, fonts & layout | Draw Your Font has AI labeling/critique; Khatt Engine explores Arabic layouts, while Khmer Font Factory is a pending browser-inference lead. The latter demo was inaccessible and its checkpoint terms remain unresolved. [Source 1](https://drawyourfont.com/) [Source 2](https://github.com/lienghongky/cxm-kff/blob/main/src/workers/pipeline.worker.js) |
| Storyboarding, narrative & comics | OpenMontage, ViMax and Pixelle-Video address scripts, character/scene plans and generated shots. Character consistency, factual correctness and media provenance are not guaranteed by a complete pipeline. [Source 1](https://www.openmontage.video/) [Source 2](https://latent-spaces.github.io/brag/) |
| Creative publishing & presentation | Presenton and AntV Infographic add editable presentations and diagrams, while agent video tools target short explainers. Export formats and editable intermediates are emphasized over automated posting. [Source 1](https://infographic.antv.vision/) [Source 2](https://latent-spaces.github.io/brag/) |
| Photography, restoration & color | imaginAIry and BackgroundRemover offer processing routes for photographic material, alongside learned matting and depth preparation. Restoration/enhancement may alter detail and should preserve originals. [Source 1](https://brycedrennan.github.io/imaginAIry/) [Source 2](https://pypi.org/project/backgroundremover/) |
| Data art & scientific visualization | Data Formulator receives a complete guide for AI-assisted data transformation and chart authoring. AntV Infographic adds a structural SVG route; chart facts still require checking against the underlying data. [Source 1](https://pypi.org/project/data-formulator/) [Source 2](https://infographic.antv.vision/learn/getting-started) |
| Physical, robotic & kinetic installations | Ghost Arcade remains relevant to projection-based work, with no unchanged re-profile today. Spatial reconstruction and acoustic research offer building blocks, not a turnkey or safety-tested physical installation. [Source 1](https://ghostarcade.live/) [Source 2](https://mitibm.mit.edu/research/blog/learning-neural-acoustic-fields/) |
| Performance, projection & stage media | Music-to-motion and neural sound work extend performance research. Live outputs and device integration remain dependent on actual latency and hardware testing. [Source 1](https://discoforcing.github.io/) [Source 2](https://ghostarcade.live/) [Source 3](https://map-yue2.github.io/) |
| Fashion, textiles & wearable media | NeuralTailor gets a guide for point-cloud-to-garment-pattern research. SewFormer is interesting but lacks a verified complete repository license; model-produced patterns are not fit or manufacturing guarantees. [Source 1](https://sewformer.github.io/) [Source 2](https://github.com/maria-korosteleva/Garment-Pattern-Estimation) |
| Accessible media & assistive creation | VideoLingo and local narration tools can support captions and spoken media. Translation, timing, voice clarity and accessible presentation remain human-review tasks. [Source 1](https://videolingo.io/en) [Source 2](https://voicestudio.sh/) |
| Mobile, edge & on-device creation | The OnDevice LLM project site still says public sideload downloads are retired and App Store availability is forthcoming. It remains an earlier library lead; no unchanged entry is repeated as a new daily discovery. [Source 1](https://mesutcydev.github.io/ios-local-llm/) |
| Creative learning & authoring | Data Formulator, Presenton and code-authored explainers offer routes to teaching media. AI-authored text, charts and visual examples need substantive checking before use. [Source 1](https://pypi.org/project/data-formulator/) [Source 2](https://hyperframes.heygen.com/showcase) |
| Archives, media restoration & collections | Restoration, matting and local narration can support archive interpretation and presentation. Keep original scans/audio alongside derivative enhancements because models may invent or remove detail. [Source 1](https://brycedrennan.github.io/imaginAIry/) [Source 2](https://localai.io/docs/features/text-to-audio/) |
| Emerging & cross-disciplinary creative AI | The search extends into haptic media, choreography, neural acoustics and computational craft. Several projects remain watchlist entries because software is missing, non-AI, or ambiguously licensed. [Source 1](https://hapticgen.hcitech.org/) [Source 2](https://sewformer.github.io/) [Source 3](https://discoforcing.github.io/) |
| Tactile, vibration and haptic media | The HapticGen primary site was reviewed again as context; no substantive new change was established, so its existing profile is not repeated. Its software and restricted model terms remain separate. [Source 1](https://hapticgen.hcitech.org/) |
| Neural acoustics and responsive sound spaces | MIT-IBM describes Neural Acoustic Fields as learned representations of room acoustics. The old linked CMU page failed to open today; no new eligible ready-to-use acoustic application cleared review. [Source 1](https://mitibm.mit.edu/research/blog/learning-neural-acoustic-fields/) |
| AI agents for code-authored media production | brag, OpenMontage, OpenCreator and Velocut expose media generation or editing to AI agents. Agent subscriptions and generation providers remain separate from their open-source integration code. [Source 1](https://latent-spaces.github.io/brag/) [Source 2](https://www.openmontage.video/) |
| AI kinetic typography and animated lettering | HyperFrames examples and GSAP Skills demonstrate agent-authored animated lettering. The MIT skills license does not relicense the underlying GSAP engine, and examples were not re-rendered. [Source 1](https://hyperframes.heygen.com/showcase) [Source 2](https://github.com/greensock/gsap-skills) |
| AI choreography and dance composition | AtomicDance, DiscoForcing and Afford-Motion extend movement composition beyond generic video animation. Research code, checkpoints, body models and training datasets have distinct availability and permissions. [Source 1](https://cxhcmhhh.github.io/AtomicDanceProject/) [Source 2](https://discoforcing.github.io/) |
| AI-assisted textile and computational craft | NeuralTailor provides a released sewing-pattern research route; SewFormer and Threadspool remain license-review gaps. Generic embroidery/vector tools without a concrete AI contribution were not admitted. [Source 1](https://sewformer.github.io/) [Source 2](https://github.com/alexandra03/threadspool) [Source 3](https://github.com/maria-korosteleva/Garment-Pattern-Estimation) |

## Search and review counts

36 creative fields; 230/230 repository queries attempted; 14/14 model-task queries attempted. 19426 distinct source candidates and 662 model leads. 25 detailed profiles and 19 additional screened discoveries. Source gaps: 0 failed repository queries, 0 partial repository queries, 95 bounded repository queries, 0 failed model-task queries and 2 web ecosystem gaps. Raw search candidates include duplicates of known tools, excluded projects and projects awaiting review; they are not verified recommendations.

## Research beyond GitHub

- **gitlab** · searched: Reviewed MotionNet repository/site results: the inspected material is a protocol/specification, without a verified usable creative-AI implementation. No eligible GitLab tool was established today. [Source](https://gitlab.com/Roxanne_Ardary/motionnet) [Source](https://roxanneardary.com/motionnet/)
- **codeberg** · gap: Targeted live searches/pages were blocked by robots restrictions; no project and complete software license could be verified on Codeberg today.
- **sourcehut** · gap: Targeted searches were blocked or produced no inspectable relevant primary project. SourceHut creative-AI coverage remains an explicit gap.
- **packages** · searched: Read PyPI metadata and primary package descriptions for BackgroundRemover and Data Formulator; version and Python requirements were checked against the actual project/package sources. [Source](https://pypi.org/project/backgroundremover/) [Source](https://pypi.org/project/data-formulator/)
- **creative-plugins** · searched: Reviewed Dream Textures Blender setup and host-version guidance. Also inspected Pallaidium, but its README use restrictions need clarification alongside the GPL license before inclusion. [Source](https://github.com/carson-katri/dream-textures/wiki/Setup) [Source](https://github.com/tin2tin/Pallaidium)
- **project-sites** · searched: Read primary sites for VoiceStudio, Immersive Web SDK, AntV Infographic, Wonder3D, YuE2, OpenMontage and related tools. Some linked demos failed to open; no interaction or output testing is implied. [Source](https://voicestudio.sh/) [Source](https://iwsdk.dev/) [Source](https://www.openmontage.video/) [Source](https://map-yue2.github.io/)
- **research-code** · searched: Paired primary pages with released source and full software licenses for movement, geometry and music research. SewFormer is held for missing license evidence; LGM and MAtCha have non-commercial dependency concerns. [Source](https://cxhcmhhh.github.io/AtomicDanceProject/) [Source](https://discoforcing.github.io/) [Source](https://nicolasvonluetzow.github.io/GaussianGPT/) [Source](https://sewformer.github.io/)
- **international** · searched: Reviewed Chinese-language OOOSplat/Pixelle materials, Arabic Khatt Engine, Japanese/Chinese calligraphic gestures, and Khmer Font Factory source. Non-English documentation did not prevent review; unresolved weights and unavailable demos are labeled. [Source](https://infographic.antv.vision/learn/getting-started) [Source](https://github.com/ATH-MaaS/Pixelle-Video) [Source](https://github.com/dino880917/khatt-engine) [Source](https://github.com/lienghongky/cxm-kff)

## Collection limitations

- images: bounded or incomplete query: topic:diffusion pushed:>=2026-09-04 is:public fork:false archived:false (200 of 204 matches sampled)
- images: bounded or incomplete query: topic:diffusion is:public fork:false archived:false (200 of 1421 matches sampled)
- images: bounded or incomplete query: AI image generation pushed:>=2026-09-04 is:public fork:false archived:false (200 of 1632 matches sampled)
- images: bounded or incomplete query: AI image generation created:>=2026-09-04 is:public fork:false archived:false (200 of 812 matches sampled)
- images: bounded or incomplete query: AI image generation is:public fork:false archived:false (200 of 15309 matches sampled)
- video: bounded or incomplete query: AI video pushed:>=2026-09-04 is:public fork:false archived:false (200 of 12216 matches sampled)
- video: bounded or incomplete query: AI video created:>=2026-09-04 is:public fork:false archived:false (200 of 7727 matches sampled)
- video: bounded or incomplete query: AI video is:public fork:false archived:false (200 of 82345 matches sampled)
- video: bounded or incomplete query: topic:video-generation pushed:>=2026-09-04 is:public fork:false archived:false (200 of 1486 matches sampled)
- video: bounded or incomplete query: topic:video-generation created:>=2026-09-04 is:public fork:false archived:false (200 of 569 matches sampled)
- video: bounded or incomplete query: topic:video-generation is:public fork:false archived:false (200 of 3788 matches sampled)
- audio: bounded or incomplete query: topic:music-generation pushed:>=2026-09-04 is:public fork:false archived:false (200 of 289 matches sampled)
- audio: bounded or incomplete query: topic:music-generation is:public fork:false archived:false (500 of 1172 matches sampled)
- audio: bounded or incomplete query: AI audio pushed:>=2026-09-04 is:public fork:false archived:false (200 of 3733 matches sampled)
- audio: bounded or incomplete query: AI audio created:>=2026-09-04 is:public fork:false archived:false (200 of 2006 matches sampled)
- audio: bounded or incomplete query: AI audio is:public fork:false archived:false (200 of 27481 matches sampled)
- 3d: bounded or incomplete query: 3D generation pushed:>=2026-09-04 is:public fork:false archived:false (200 of 663 matches sampled)
- 3d: bounded or incomplete query: 3D generation created:>=2026-09-04 is:public fork:false archived:false (200 of 354 matches sampled)
- 3d: bounded or incomplete query: 3D generation is:public fork:false archived:false (200 of 5748 matches sampled)
- 3d: bounded or incomplete query: topic:3d-reconstruction pushed:>=2026-09-04 is:public fork:false archived:false (200 of 250 matches sampled)
- 3d: bounded or incomplete query: topic:3d-reconstruction is:public fork:false archived:false (200 of 1902 matches sampled)
- web: bounded or incomplete query: topic:webgpu pushed:>=2026-09-04 is:public fork:false archived:false (200 of 1004 matches sampled)
- web: bounded or incomplete query: topic:webgpu created:>=2026-09-04 is:public fork:false archived:false (200 of 400 matches sampled)
- web: bounded or incomplete query: topic:webgpu is:public fork:false archived:false (200 of 2766 matches sampled)
- xr: bounded or incomplete query: AI VR pushed:>=2026-09-04 is:public fork:false archived:false (200 of 328 matches sampled)
- xr: bounded or incomplete query: AI VR is:public fork:false archived:false (200 of 2838 matches sampled)
- computational: bounded or incomplete query: AI creative coding is:public fork:false archived:false (200 of 910 matches sampled)
- computational: bounded or incomplete query: topic:generative-art pushed:>=2026-09-04 is:public fork:false archived:false (200 of 801 matches sampled)
- computational: bounded or incomplete query: topic:generative-art created:>=2026-09-04 is:public fork:false archived:false (200 of 383 matches sampled)
- computational: bounded or incomplete query: topic:generative-art is:public fork:false archived:false (200 of 3827 matches sampled)
- interactive: bounded or incomplete query: AI interactive art is:public fork:false archived:false (200 of 670 matches sampled)
- fabrication: bounded or incomplete query: AI CAD pushed:>=2026-09-04 is:public fork:false archived:false (200 of 659 matches sampled)
- fabrication: bounded or incomplete query: AI CAD created:>=2026-09-04 is:public fork:false archived:false (200 of 369 matches sampled)
- fabrication: bounded or incomplete query: AI CAD is:public fork:false archived:false (200 of 2966 matches sampled)
- fabrication: bounded or incomplete query: AI 3D printing is:public fork:false archived:false (200 of 337 matches sampled)
- gaming: bounded or incomplete query: AI game assets is:public fork:false archived:false (200 of 625 matches sampled)
- gaming: bounded or incomplete query: AI blender pushed:>=2026-09-04 is:public fork:false archived:false (200 of 405 matches sampled)
- gaming: bounded or incomplete query: AI blender created:>=2026-09-04 is:public fork:false archived:false (200 of 297 matches sampled)
- gaming: bounded or incomplete query: AI blender is:public fork:false archived:false (200 of 1511 matches sampled)
- motion: bounded or incomplete query: AI motion capture is:public fork:false archived:false (200 of 230 matches sampled)
- motion: bounded or incomplete query: motion generation is:public fork:false archived:false (200 of 1487 matches sampled)
- avatars: bounded or incomplete query: AI avatar pushed:>=2026-09-04 is:public fork:false archived:false (200 of 740 matches sampled)
- avatars: bounded or incomplete query: AI avatar created:>=2026-09-04 is:public fork:false archived:false (200 of 396 matches sampled)
- avatars: bounded or incomplete query: AI avatar is:public fork:false archived:false (200 of 5824 matches sampled)
- avatars: bounded or incomplete query: lip sync pushed:>=2026-09-04 is:public fork:false archived:false (200 of 289 matches sampled)
- avatars: bounded or incomplete query: lip sync is:public fork:false archived:false (200 of 2372 matches sampled)
- vfx: bounded or incomplete query: AI visual effects is:public fork:false archived:false (200 of 413 matches sampled)
- capture: bounded or incomplete query: topic:gaussian-splatting pushed:>=2026-09-04 is:public fork:false archived:false (200 of 232 matches sampled)
- capture: bounded or incomplete query: topic:gaussian-splatting is:public fork:false archived:false (500 of 893 matches sampled)
- capture: bounded or incomplete query: neural reconstruction is:public fork:false archived:false (200 of 1312 matches sampled)
- editing: bounded or incomplete query: AI video editing pushed:>=2026-09-04 is:public fork:false archived:false (200 of 795 matches sampled)
- editing: bounded or incomplete query: AI video editing created:>=2026-09-04 is:public fork:false archived:false (200 of 495 matches sampled)
- editing: bounded or incomplete query: AI video editing is:public fork:false archived:false (200 of 3346 matches sampled)
- editing: bounded or incomplete query: AI subtitle pushed:>=2026-09-04 is:public fork:false archived:false (200 of 365 matches sampled)
- editing: bounded or incomplete query: AI subtitle is:public fork:false archived:false (200 of 2189 matches sampled)
- vector: bounded or incomplete query: AI SVG pushed:>=2026-09-04 is:public fork:false archived:false (200 of 435 matches sampled)
- vector: bounded or incomplete query: AI SVG created:>=2026-09-04 is:public fork:false archived:false (200 of 241 matches sampled)
- vector: bounded or incomplete query: AI SVG is:public fork:false archived:false (200 of 1751 matches sampled)
- typography: bounded or incomplete query: AI typography is:public fork:false archived:false (200 of 639 matches sampled)
- typography: bounded or incomplete query: font generation is:public fork:false archived:false (400 of 416 matches sampled)
- storytelling: bounded or incomplete query: AI storyboard pushed:>=2026-09-04 is:public fork:false archived:false (200 of 363 matches sampled)
- storytelling: bounded or incomplete query: AI storyboard created:>=2026-09-04 is:public fork:false archived:false (200 of 210 matches sampled)
- storytelling: bounded or incomplete query: AI storyboard is:public fork:false archived:false (200 of 1650 matches sampled)
- storytelling: bounded or incomplete query: AI comic pushed:>=2026-09-04 is:public fork:false archived:false (200 of 1571 matches sampled)
- storytelling: bounded or incomplete query: AI comic created:>=2026-09-04 is:public fork:false archived:false (200 of 1482 matches sampled)
- storytelling: bounded or incomplete query: AI comic is:public fork:false archived:false (200 of 2831 matches sampled)
- publishing: bounded or incomplete query: AI presentation pushed:>=2026-09-04 is:public fork:false archived:false (200 of 1073 matches sampled)
- publishing: bounded or incomplete query: AI presentation created:>=2026-09-04 is:public fork:false archived:false (200 of 654 matches sampled)
- publishing: bounded or incomplete query: AI presentation is:public fork:false archived:false (200 of 8377 matches sampled)
- publishing: bounded or incomplete query: AI publishing pushed:>=2026-09-04 is:public fork:false archived:false (200 of 1050 matches sampled)
- publishing: bounded or incomplete query: AI publishing created:>=2026-09-04 is:public fork:false archived:false (200 of 644 matches sampled)
- publishing: bounded or incomplete query: AI publishing is:public fork:false archived:false (200 of 3961 matches sampled)
- photography: bounded or incomplete query: AI colorization pushed:>=2026-09-04 is:public fork:false archived:false (200 of 440 matches sampled)
- photography: bounded or incomplete query: AI colorization created:>=2026-09-04 is:public fork:false archived:false (200 of 275 matches sampled)
- photography: bounded or incomplete query: AI colorization is:public fork:false archived:false (200 of 4686 matches sampled)
- visualization: bounded or incomplete query: AI visualization pushed:>=2026-09-04 is:public fork:false archived:false (200 of 3248 matches sampled)
- visualization: bounded or incomplete query: AI visualization created:>=2026-09-04 is:public fork:false archived:false (200 of 1873 matches sampled)
- visualization: bounded or incomplete query: AI visualization is:public fork:false archived:false (200 of 37442 matches sampled)
- visualization: bounded or incomplete query: AI data art is:public fork:false archived:false (200 of 1013 matches sampled)
- performance: bounded or incomplete query: AI live visuals is:public fork:false archived:false (200 of 701 matches sampled)
- fashion: bounded or incomplete query: AI fashion design is:public fork:false archived:false (200 of 632 matches sampled)
- fashion: bounded or incomplete query: AI textile is:public fork:false archived:false (200 of 459 matches sampled)
- accessibility: bounded or incomplete query: AI audio description is:public fork:false archived:false (200 of 253 matches sampled)
- mobile: bounded or incomplete query: AI mobile media is:public fork:false archived:false (200 of 206 matches sampled)
- education: bounded or incomplete query: AI explainer pushed:>=2026-09-04 is:public fork:false archived:false (200 of 6479 matches sampled)
- education: bounded or incomplete query: AI explainer created:>=2026-09-04 is:public fork:false archived:false (200 of 4491 matches sampled)
- education: bounded or incomplete query: AI explainer is:public fork:false archived:false (200 of 36379 matches sampled)
- frontier: bounded or incomplete query: AI creative tools pushed:>=2026-09-04 is:public fork:false archived:false (200 of 235 matches sampled)
- frontier: bounded or incomplete query: AI creative tools is:public fork:false archived:false (200 of 1931 matches sampled)
- frontier: bounded or incomplete query: AI digital art is:public fork:false archived:false (200 of 716 matches sampled)
- frontier: bounded or incomplete query: AI multimedia is:public fork:false archived:false (200 of 1159 matches sampled)
- frontier: bounded or incomplete query: AI new media is:public fork:false archived:false (200 of 500 matches sampled)
- neural-acoustics: bounded or incomplete query: neural acoustic is:public fork:false archived:false (200 of 341 matches sampled)
- agent-media-production: bounded or incomplete query: AI agent animation is:public fork:false archived:false (200 of 491 matches sampled)
- agent-media-production: bounded or incomplete query: AI agent video editing is:public fork:false archived:false (200 of 418 matches sampled)

## MoneyPrinterTurbo

Video, animation & film · Creative publishing & presentation · Storyboarding, narrative & comics

First detailed guide, completing an earlier screened lead. This is a documentation baseline, not a claim that the project launched today.

### How it uses AI

A short-video pipeline that combines LLM scripts, footage selection, synthesized narration, captions and final rendering. Creative use: Drafting narrated explainers from a topic or an existing script, with vertical or landscape output and local media assets. [Source](https://github.com/harry0703/MoneyPrinterTurbo) [Source](https://harry0703.github.io/mpt-assets/)

### Introduction

A short-video pipeline that combines LLM scripts, footage selection, synthesized narration, captions and final rendering. [Source 1](https://github.com/harry0703/MoneyPrinterTurbo) [Source 2](https://harry0703.github.io/mpt-assets/)

### What it is good for

Drafting narrated explainers from a topic or an existing script, with vertical or landscape output and local media assets. [Source 1](https://github.com/harry0703/MoneyPrinterTurbo) [Source 2](https://harry0703.github.io/mpt-assets/)

### Demo & examples

The official mpt-assets gallery and README contain finished examples; these demonstrate the developer workflow rather than independently measured quality. [Source 1](https://github.com/harry0703/MoneyPrinterTurbo) [Source 2](https://harry0703.github.io/mpt-assets/)

### Install

Follow the reviewed project route below; these steps are documentation guidance and were not executed. [Source 1](https://github.com/harry0703/MoneyPrinterTurbo) [Source 2](https://harry0703.github.io/mpt-assets/)

1. Download the official Windows release archive and use its start.bat, or clone the repository for the uv route.
2. For source installation select Python 3.11, run uv sync --frozen, configure the example configuration and start the platform web UI script.
3. Configure only the LLM, voice and media providers you intend to use; local Ollama is an alternative to hosted text providers.

```sh
uv sync --frozen
```


```sh
sh webui.sh
```

### First project

A small first project that exercises the documented creative workflow. [Source 1](https://github.com/harry0703/MoneyPrinterTurbo) [Source 2](https://harry0703.github.io/mpt-assets/)

1. Enter a short topic or paste a reviewed script.
2. Select voice, subtitle engine, aspect ratio and your own cleared footage/music.
3. Render a short sample, correct narration and captions, then export the full video.
### Hardware & software

Requirements are source-specific. Unreported capacities and untested platforms are not inferred. [Source 1](https://github.com/harry0703/MoneyPrinterTurbo) [Source 2](https://harry0703.github.io/mpt-assets/)

- **Hardware:** The README lists a 4-core CPU and 4 GB RAM minimum, 6–8 cores/8 GB recommended, and 8+ cores/16 GB ideal. GPU is optional; the recommended GPU tier has 4 GB VRAM. Required disk capacity is not documented as a single total.
- **Software:** Python 3.11+ (3.11 recommended), uv and the repository dependencies. Faster-Whisper adds model downloads; the default Edge subtitle timing path does not require local ASR inference.
- **Platforms:** Windows 10+, macOS 11+ and mainstream Linux are documented. Web UI normally uses port 8501; Docker is also documented.

### License, model weights & costs

The complete software license was archived and reviewed. Keep software, model weights, dependencies and hosted-service terms separate. [Source 1](https://github.com/harry0703/MoneyPrinterTurbo/blob/main/LICENSE) [Source 2](https://github.com/harry0703/MoneyPrinterTurbo) [Source 3](https://harry0703.github.io/mpt-assets/)

- **Code:** MIT
- **Weights:** LLM, TTS and recognition models have separate terms; stock footage and music are not relicensed by the MIT application.
- **Commercial:** The reviewed MIT software license permits commercial use subject to its license, notice and source-sharing obligations where applicable. This does not establish permission for every model, input, output or service.
- **Cost:** Local software has no license fee. Hosted AI, stock-media services, local compute and storage can incur costs.

### Why it merits attention

A configurable end-to-end pipeline, editable scripts and platform-specific setup make it worth assessing for repeatable explainer work. [Source 1](https://github.com/harry0703/MoneyPrinterTurbo) [Source 2](https://harry0703.github.io/mpt-assets/)

### Limitations

Automatic stock selection and factual scripts need editorial review. The repository says some bundled music came from YouTube without a clear original rights source: replace it with cleared material. No automatic social posting was enabled. This edition is a documentation review, not an installation or output-quality test. [Source 1](https://github.com/harry0703/MoneyPrinterTurbo) [Source 2](https://harry0703.github.io/mpt-assets/)

### Get the tool

- [Repository](https://github.com/harry0703/MoneyPrinterTurbo)
- [License](https://github.com/harry0703/MoneyPrinterTurbo/blob/main/LICENSE)
- [Documentation](https://harry0703.github.io/mpt-assets/)

## VideoLingo

Editing, captions & post-production · Accessible media & assistive creation · Audio, music & voice · Video, animation & film

First detailed guide, completing an earlier screened lead. This is a documentation baseline, not a claim that the project launched today.

### How it uses AI

An AI-assisted subtitle translation and dubbing application with speech recognition, alignment, segmentation and multiple speech engines. Creative use: Preparing multilingual captions or a timed dub for an existing creative video, with review between stages. [Source](https://github.com/Huanshere/VideoLingo) [Source](https://videolingo.io/en)

### Introduction

An AI-assisted subtitle translation and dubbing application with speech recognition, alignment, segmentation and multiple speech engines. [Source 1](https://github.com/Huanshere/VideoLingo) [Source 2](https://videolingo.io/en)

### What it is good for

Preparing multilingual captions or a timed dub for an existing creative video, with review between stages. [Source 1](https://github.com/Huanshere/VideoLingo) [Source 2](https://videolingo.io/en)

### Demo & examples

The official site and README publish translated/subtitled examples; no demo session or audio evaluation was run here. [Source 1](https://github.com/Huanshere/VideoLingo) [Source 2](https://videolingo.io/en)

### Install

Follow the reviewed project route below; these steps are documentation guidance and were not executed. [Source 1](https://github.com/Huanshere/VideoLingo) [Source 2](https://videolingo.io/en)

1. Windows users can use the official source ZIP and OneKeyStart.bat route.
2. For source use, clone the project and follow its uv/Python 3.12 setup, then run uv run start.py.
3. Choose recognition, translation and optional dubbing providers in the UI; Docker has a separate NVIDIA/CUDA setup.

```sh
uv run start.py
```

### First project

A small first project that exercises the documented creative workflow. [Source 1](https://github.com/Huanshere/VideoLingo) [Source 2](https://videolingo.io/en)

1. Load a short video and inspect the recognized transcript and speaker boundaries.
2. Translate and revise terminology and line breaks.
3. Generate the optional dub and review timing, pronunciation and music mixing before export.
### Hardware & software

Requirements are source-specific. Unreported capacities and untested platforms are not inferred. [Source 1](https://github.com/Huanshere/VideoLingo) [Source 2](https://videolingo.io/en)

- **Hardware:** RAM, VRAM and disk minima are not specified in the reviewed README. Apple Silicon uses an MLX recognition path; Intel Mac uses CPU. Docker documents CUDA 12.8.1/cu128 with a separate 12.6 route.
- **Software:** Python 3.12, uv, FFmpeg and engine-specific model downloads. Translation providers must support the expected structured JSON response.
- **Platforms:** Windows, macOS on Apple Silicon or Intel, and Linux are documented. A browser UI does not remove backend requirements.

### License, model weights & costs

The complete software license was archived and reviewed. Keep software, model weights, dependencies and hosted-service terms separate. [Source 1](https://github.com/Huanshere/VideoLingo/blob/main/LICENSE) [Source 2](https://github.com/Huanshere/VideoLingo) [Source 3](https://videolingo.io/en)

- **Code:** Apache-2.0
- **Weights:** Apache software licensing does not cover every ASR/TTS checkpoint or hosted translation service.
- **Commercial:** The reviewed Apache-2.0 software license permits commercial use subject to its license, notice and source-sharing obligations where applicable. This does not establish permission for every model, input, output or service.
- **Cost:** Local inference uses your hardware. Optional hosted transcription, LLM and voice APIs have separate fees.

### Why it merits attention

Explicit segmentation, pausing/resuming and alternative local recognition routes support a practical post-production review loop. [Source 1](https://github.com/Huanshere/VideoLingo) [Source 2](https://videolingo.io/en)

### Limitations

Mixed-language alignment, spoken numbers and speaker-specific voices have documented limitations. Cached stages may need deliberate regeneration after model changes; Intel Mac dubbing defaults differ for original background audio. This edition is a documentation review, not an installation or output-quality test. [Source 1](https://github.com/Huanshere/VideoLingo) [Source 2](https://videolingo.io/en)

### Get the tool

- [Repository](https://github.com/Huanshere/VideoLingo)
- [License](https://github.com/Huanshere/VideoLingo/blob/main/LICENSE)
- [Documentation](https://videolingo.io/en)

## Next AI Draw.io

Vector graphics, illustration & textures · Data art & scientific visualization · Creative learning & authoring · Browser tools & web media

First detailed guide, completing an earlier screened lead. This is a documentation baseline, not a claim that the project launched today.

### How it uses AI

An LLM-assisted Draw.io editor that creates and revises editable diagrams from text, images and PDFs. Creative use: Explaining a creative pipeline, planning an installation or turning a sketch into an editable diagram. [Source](https://github.com/DayuanJiang/next-ai-draw-io) [Source](https://next-ai-drawio.jiang.jp/)

### Introduction

An LLM-assisted Draw.io editor that creates and revises editable diagrams from text, images and PDFs. [Source 1](https://github.com/DayuanJiang/next-ai-draw-io) [Source 2](https://next-ai-drawio.jiang.jp/)

### What it is good for

Explaining a creative pipeline, planning an installation or turning a sketch into an editable diagram. [Source 1](https://github.com/DayuanJiang/next-ai-draw-io) [Source 2](https://next-ai-drawio.jiang.jp/)

### Demo & examples

An official web demo is linked at next-ai-drawio.jiang.jp, with examples and screenshots in the repository. The demo was not operated. [Source 1](https://github.com/DayuanJiang/next-ai-draw-io) [Source 2](https://next-ai-drawio.jiang.jp/)

### Install

Follow the reviewed project route below; these steps are documentation guidance and were not executed. [Source 1](https://github.com/DayuanJiang/next-ai-draw-io) [Source 2](https://next-ai-drawio.jiang.jp/)

1. Choose the official Windows, macOS or Linux desktop release, the documented Docker route, or a source checkout.
2. For source: npm install, copy env.example to .env.local and configure a supported provider.
3. Run npm run dev and open the documented port 6002.

```sh
npm install
```


```sh
npm run dev
```

### First project

A small first project that exercises the documented creative workflow. [Source 1](https://github.com/DayuanJiang/next-ai-draw-io) [Source 2](https://next-ai-drawio.jiang.jp/)

1. Describe the diagram and required relationships, or import a reference.
2. Ask for a focused change and compare it with the previous version.
3. Manually check labels, links and layout; save the editable Draw.io document.
### Hardware & software

Requirements are source-specific. Unreported capacities and untested platforms are not inferred. [Source 1](https://github.com/DayuanJiang/next-ai-draw-io) [Source 2](https://next-ai-drawio.jiang.jp/)

- **Hardware:** No universal CPU, RAM, VRAM or storage minimum is published in the reviewed README. Local-model requirements depend on the chosen Ollama model.
- **Software:** Node/npm for source development; the reviewed README does not specify a Node minimum. Supported hosted LLM credentials or a configured local endpoint are needed for AI authoring.
- **Platforms:** Desktop downloads cover Windows, macOS and Linux; browser and Docker deployment are also documented.

### License, model weights & costs

The complete software license was archived and reviewed. Keep software, model weights, dependencies and hosted-service terms separate. [Source 1](https://github.com/DayuanJiang/next-ai-draw-io/blob/main/LICENSE) [Source 2](https://github.com/DayuanJiang/next-ai-draw-io) [Source 3](https://next-ai-drawio.jiang.jp/)

- **Code:** Apache-2.0
- **Weights:** The Apache application uses separately licensed models/services. Imported logos, fonts and source documents keep their own terms.
- **Commercial:** The reviewed Apache-2.0 software license permits commercial use subject to its license, notice and source-sharing obligations where applicable. This does not establish permission for every model, input, output or service.
- **Cost:** No software license fee; hosted inference may be paid, while local inference needs suitable compute.

### Why it merits attention

Editable XML and revision history are useful advantages over a generated flat diagram image. [Source 1](https://github.com/DayuanJiang/next-ai-draw-io) [Source 2](https://next-ai-drawio.jiang.jp/)

### Limitations

Long or complex XML can fail with weaker models. A plausible-looking diagram can contain wrong connections; verify the structure. This edition is a documentation review, not an installation or output-quality test. [Source 1](https://github.com/DayuanJiang/next-ai-draw-io) [Source 2](https://next-ai-drawio.jiang.jp/)

### Get the tool

- [Repository](https://github.com/DayuanJiang/next-ai-draw-io)
- [License](https://github.com/DayuanJiang/next-ai-draw-io/blob/main/LICENSE)
- [Documentation](https://next-ai-drawio.jiang.jp/)

## Data Formulator

Data art & scientific visualization · Creative learning & authoring · Creative publishing & presentation · Browser tools & web media

First detailed guide, completing an earlier screened lead. This is a documentation baseline, not a claim that the project launched today.

### How it uses AI

A Microsoft Research application where AI agents help load, transform and visualize data on an editable canvas. Creative use: Developing data-driven art, exhibition charts and visual explanations with branchable alternatives. [Source](https://github.com/microsoft/data-formulator) [Source](https://pypi.org/project/data-formulator/) [Source](https://data-formulator.ai/)

### Introduction

A Microsoft Research application where AI agents help load, transform and visualize data on an editable canvas. [Source 1](https://github.com/microsoft/data-formulator) [Source 2](https://pypi.org/project/data-formulator/) [Source 3](https://data-formulator.ai/)

### What it is good for

Developing data-driven art, exhibition charts and visual explanations with branchable alternatives. [Source 1](https://github.com/microsoft/data-formulator) [Source 2](https://pypi.org/project/data-formulator/) [Source 3](https://data-formulator.ai/)

### Demo & examples

The official README contains workflow videos and screenshots. The hosted page requires JavaScript; no interactive session was tested. [Source 1](https://github.com/microsoft/data-formulator) [Source 2](https://pypi.org/project/data-formulator/) [Source 3](https://data-formulator.ai/)

### Install

Follow the reviewed project route below; these steps are documentation guidance and were not executed. [Source 1](https://github.com/microsoft/data-formulator) [Source 2](https://pypi.org/project/data-formulator/) [Source 3](https://data-formulator.ai/)

1. Install the Python package in a virtual environment, or use the documented uvx launcher.
2. Start the application and open localhost:5567.
3. Select a supported LLM endpoint and import a small dataset before connecting larger sources.

```sh
uvx data_formulator
```

### First project

A small first project that exercises the documented creative workflow. [Source 1](https://github.com/microsoft/data-formulator) [Source 2](https://pypi.org/project/data-formulator/) [Source 3](https://data-formulator.ai/)

1. Load CSV, spreadsheet or other supported data and inspect the inferred fields.
2. Ask a visualization question, review the transformation and refine the chart.
3. Branch the data thread to compare alternatives, then export an image or report.
### Hardware & software

Requirements are source-specific. Unreported capacities and untested platforms are not inferred. [Source 1](https://github.com/microsoft/data-formulator) [Source 2](https://pypi.org/project/data-formulator/) [Source 3](https://data-formulator.ai/)

- **Hardware:** No fixed RAM, VRAM, CPU or storage minimum is documented. Dataset size and any local model determine resource use.
- **Software:** PyPI specifies Python >=3.11. uvx, pip and Docker routes are documented; AI needs a supported provider or local model endpoint.
- **Platforms:** The Python/browser and Docker routes are documented, with Windows and macOS desktop previews also described. No comprehensive minimum-OS matrix is published.

### License, model weights & costs

The complete software license was archived and reviewed. Keep software, model weights, dependencies and hosted-service terms separate. [Source 1](https://github.com/microsoft/data-formulator/blob/main/LICENSE) [Source 2](https://github.com/microsoft/data-formulator) [Source 3](https://pypi.org/project/data-formulator/) [Source 4](https://data-formulator.ai/)

- **Code:** MIT
- **Weights:** MIT covers the application, not the connected models, datasets or database services.
- **Commercial:** The reviewed MIT software license permits commercial use subject to its license, notice and source-sharing obligations where applicable. This does not establish permission for every model, input, output or service.
- **Cost:** Local software is free; chosen hosted models and data services may charge separately.

### Why it merits attention

The combination of visible transformations, editable charts and comparison branches is useful for iterative visual storytelling. [Source 1](https://github.com/microsoft/data-formulator) [Source 2](https://pypi.org/project/data-formulator/) [Source 3](https://data-formulator.ai/)

### Limitations

Generated transformations and chart encodings need checking against the original data. A local UI may still send data to a cloud model. PyPI 0.7.0 is the stable baseline; the listed 0.8.0b1 is a prerelease, not a new release today. This edition is a documentation review, not an installation or output-quality test. [Source 1](https://github.com/microsoft/data-formulator) [Source 2](https://pypi.org/project/data-formulator/) [Source 3](https://data-formulator.ai/)

### Get the tool

- [Repository](https://github.com/microsoft/data-formulator)
- [License](https://github.com/microsoft/data-formulator/blob/main/LICENSE)
- [Documentation](https://pypi.org/project/data-formulator/)

## Robust Video Matting

VFX, compositing & relighting · Video, animation & film · Photogrammetry, scanning & neural rendering · Mobile, edge & on-device creation

First detailed guide, completing an earlier screened lead. This is a documentation baseline, not a claim that the project launched today.

### How it uses AI

A recurrent neural network that separates a human foreground and alpha matte from video without a green screen. Creative use: Compositing presenters or performers into new scenes and building interactive portrait effects. [Source](https://github.com/PeterL1n/RobustVideoMatting) [Source](https://peterl1n.github.io/RobustVideoMatting/)

### Introduction

A recurrent neural network that separates a human foreground and alpha matte from video without a green screen. [Source 1](https://github.com/PeterL1n/RobustVideoMatting) [Source 2](https://peterl1n.github.io/RobustVideoMatting/)

### What it is good for

Compositing presenters or performers into new scenes and building interactive portrait effects. [Source 1](https://github.com/PeterL1n/RobustVideoMatting) [Source 2](https://peterl1n.github.io/RobustVideoMatting/)

### Demo & examples

The official project page and repository contain compositing examples. The project page exposed only a JavaScript shell to the research reader. [Source 1](https://github.com/PeterL1n/RobustVideoMatting) [Source 2](https://peterl1n.github.io/RobustVideoMatting/)

### Install

Follow the reviewed project route below; these steps are documentation guidance and were not executed. [Source 1](https://github.com/PeterL1n/RobustVideoMatting) [Source 2](https://peterl1n.github.io/RobustVideoMatting/)

1. Clone the official repository and install requirements_inference.txt in an isolated Python environment.
2. Download the official MobileNetV3 or ResNet50 checkpoint; the authors recommend MobileNetV3 for most cases.
3. Use the supplied Python inference example or choose the separately documented ONNX, TensorFlow/TFJS or CoreML export.

```sh
pip install -r requirements_inference.txt
```

### First project

A small first project that exercises the documented creative workflow. [Source 1](https://github.com/PeterL1n/RobustVideoMatting) [Source 2](https://peterl1n.github.io/RobustVideoMatting/)

1. Start with a short single-person clip.
2. Load the matching model/checkpoint and run convert_video with the desired alpha/foreground outputs.
3. Inspect hair, motion and transparent edges over a contrasting background before compositing.
### Hardware & software

Requirements are source-specific. Unreported capacities and untested platforms are not inferred. [Source 1](https://github.com/PeterL1n/RobustVideoMatting) [Source 2](https://peterl1n.github.io/RobustVideoMatting/)

- **Hardware:** The published GPU speed table is a benchmark, not a minimum requirement, and excludes full video decoding/encoding. Minimum RAM, VRAM and disk are not documented. CPU and CUDA paths are shown.
- **Software:** Python/PyTorch inference dependencies or the chosen export runtime. ONNX opset 12 is documented; the reviewed README does not give a universal Python minimum.
- **Platforms:** ONNX supports CPU/CUDA; TFJS provides a browser option; CoreML export is documented for iOS 13+. That does not establish unrestricted macOS or arbitrary mobile support.

### License, model weights & costs

The complete software license was archived and reviewed. Keep software, model weights, dependencies and hosted-service terms separate. [Source 1](https://github.com/PeterL1n/RobustVideoMatting/blob/master/LICENSE) [Source 2](https://github.com/PeterL1n/RobustVideoMatting) [Source 3](https://peterl1n.github.io/RobustVideoMatting/)

- **Code:** GPL-3.0
- **Weights:** The source is GPL-3.0. The reviewed README does not clearly state a separate blanket grant for every checkpoint; confirm model terms for the specific distribution.
- **Commercial:** The reviewed GPL-3.0 software license permits commercial use subject to its license, notice and source-sharing obligations where applicable. This does not establish permission for every model, input, output or service.
- **Cost:** No application fee; inference hardware and integration costs remain.

### Why it merits attention

Temporal recurrence and multiple export routes make it a useful compositing component with published research comparisons. [Source 1](https://github.com/PeterL1n/RobustVideoMatting) [Source 2](https://peterl1n.github.io/RobustVideoMatting/)

### Limitations

Human matting is not general object segmentation. Hair, occlusion and fast motion can leave artifacts. CoreML models have resolution constraints and benchmark FPS must not be treated as end-to-end performance. This edition is a documentation review, not an installation or output-quality test. [Source 1](https://github.com/PeterL1n/RobustVideoMatting) [Source 2](https://peterl1n.github.io/RobustVideoMatting/)

### Get the tool

- [Repository](https://github.com/PeterL1n/RobustVideoMatting)
- [License](https://github.com/PeterL1n/RobustVideoMatting/blob/master/LICENSE)
- [Documentation](https://peterl1n.github.io/RobustVideoMatting/)

## Dream Textures

Images & design · 3D, reconstruction & assets · Vector graphics, illustration & textures · Games & production pipelines · VFX, compositing & relighting

First detailed guide, completing an earlier screened lead. This is a documentation baseline, not a claim that the project launched today.

### How it uses AI

A Blender add-on that brings diffusion texture generation, depth-guided projection and image editing into a 3D workflow. Creative use: Exploring seamless textures, painting a scene from a camera view and restyling a rendered pass. [Source](https://github.com/carson-katri/dream-textures) [Source](https://github.com/carson-katri/dream-textures/releases/tag/0.4.1) [Source](https://github.com/carson-katri/dream-textures/wiki/Setup)

### Introduction

A Blender add-on that brings diffusion texture generation, depth-guided projection and image editing into a 3D workflow. [Source 1](https://github.com/carson-katri/dream-textures) [Source 2](https://github.com/carson-katri/dream-textures/releases/tag/0.4.1) [Source 3](https://github.com/carson-katri/dream-textures/wiki/Setup)

### What it is good for

Exploring seamless textures, painting a scene from a camera view and restyling a rendered pass. [Source 1](https://github.com/carson-katri/dream-textures) [Source 2](https://github.com/carson-katri/dream-textures/releases/tag/0.4.1) [Source 3](https://github.com/carson-katri/dream-textures/wiki/Setup)

### Demo & examples

The README shows texture/projection results and links tutorials; no Blender session was run. [Source 1](https://github.com/carson-katri/dream-textures) [Source 2](https://github.com/carson-katri/dream-textures/releases/tag/0.4.1) [Source 3](https://github.com/carson-katri/dream-textures/wiki/Setup)

### Install

Follow the reviewed project route below; these steps are documentation guidance and were not executed. [Source 1](https://github.com/carson-katri/dream-textures) [Source 2](https://github.com/carson-katri/dream-textures/releases/tag/0.4.1) [Source 3](https://github.com/carson-katri/dream-textures/wiki/Setup)

1. Read release 0.4.1 and choose the archive matching your operating system, GPU and Blender version.
2. Windows CUDA packages contain a ZIP inside a 7-Zip archive; install the ZIP through Blender Add-ons preferences.
3. Enable the add-on, then download a compatible model in its preferences; depth, inpainting and upscaling use specific models.
### First project

A small first project that exercises the documented creative workflow. [Source 1](https://github.com/carson-katri/dream-textures) [Source 2](https://github.com/carson-katri/dream-textures/releases/tag/0.4.1) [Source 3](https://github.com/carson-katri/dream-textures/wiki/Setup)

1. Begin with a simple UV-mapped object or image.
2. Generate a texture or project a depth-conditioned result, keeping the seed/settings.
3. Inspect seams, surfaces and all camera angles before using the asset in a scene.
### Hardware & software

Requirements are source-specific. Unreported capacities and untested platforms are not inferred. [Source 1](https://github.com/carson-katri/dream-textures) [Source 2](https://github.com/carson-katri/dream-textures/releases/tag/0.4.1) [Source 3](https://github.com/carson-katri/dream-textures/wiki/Setup)

- **Hardware:** The README recommends over 4 GB VRAM. Setup asks for several GB of disk without a precise total; RAM minimum is not documented.
- **Software:** Blender and a matching prebuilt add-on. Release 0.4.1 separates Blender 3.6–4.0 from 4.1+ packages; this older release table is not proof of compatibility with every future Blender release.
- **Platforms:** Windows CUDA and DirectML, Apple Silicon macOS, and a manual Linux route are listed. Intel Mac support is not established by the reviewed release.

### License, model weights & costs

The complete software license was archived and reviewed. Keep software, model weights, dependencies and hosted-service terms separate. [Source 1](https://github.com/carson-katri/dream-textures/blob/main/LICENSE) [Source 2](https://github.com/carson-katri/dream-textures) [Source 3](https://github.com/carson-katri/dream-textures/releases/tag/0.4.1) [Source 4](https://github.com/carson-katri/dream-textures/wiki/Setup)

- **Code:** GPL-3.0
- **Weights:** GPL-3.0 code; Stable Diffusion checkpoints and DreamStudio services retain separate model/service terms.
- **Commercial:** The reviewed GPL-3.0 software license permits commercial use subject to its license, notice and source-sharing obligations where applicable. This does not establish permission for every model, input, output or service.
- **Cost:** Local inference uses your GPU/storage. Optional DreamStudio requires a separate account and paid service allowance.

### Why it merits attention

Direct access to scene depth and Blender render passes offers more control than transferring images between unrelated applications. [Source 1](https://github.com/carson-katri/dream-textures) [Source 2](https://github.com/carson-katri/dream-textures/releases/tag/0.4.1) [Source 3](https://github.com/carson-katri/dream-textures/wiki/Setup)

### Limitations

The latest retrieved release is from August 2024, so treat this as an established-tool baseline with compatibility risk. Generated textures do not automatically have consistent material properties or UV seams. This edition is a documentation review, not an installation or output-quality test. [Source 1](https://github.com/carson-katri/dream-textures) [Source 2](https://github.com/carson-katri/dream-textures/releases/tag/0.4.1) [Source 3](https://github.com/carson-katri/dream-textures/wiki/Setup)

### Get the tool

- [Repository](https://github.com/carson-katri/dream-textures)
- [License](https://github.com/carson-katri/dream-textures/blob/main/LICENSE)
- [Documentation](https://github.com/carson-katri/dream-textures/releases/tag/0.4.1)

## LatentSync

Avatars, digital humans & lip sync · Video, animation & film · Editing, captions & post-production

First detailed guide, completing an earlier screened lead. This is a documentation baseline, not a claim that the project launched today.

### How it uses AI

An audio-conditioned latent-diffusion tool for replacing a face video’s lip motion to match supplied speech. Creative use: Lip-sync experiments for authorized presenter footage, animation reference and dubbing research. [Source](https://github.com/bytedance/LatentSync) [Source](https://huggingface.co/ByteDance/LatentSync-1.6) [Source](https://github.com/bytedance/LatentSync/blob/main/setup_env.sh)

### Introduction

An audio-conditioned latent-diffusion tool for replacing a face video’s lip motion to match supplied speech. [Source 1](https://github.com/bytedance/LatentSync) [Source 2](https://huggingface.co/ByteDance/LatentSync-1.6) [Source 3](https://github.com/bytedance/LatentSync/blob/main/setup_env.sh)

### What it is good for

Lip-sync experiments for authorized presenter footage, animation reference and dubbing research. [Source 1](https://github.com/bytedance/LatentSync) [Source 2](https://huggingface.co/ByteDance/LatentSync-1.6) [Source 3](https://github.com/bytedance/LatentSync/blob/main/setup_env.sh)

### Demo & examples

The official repository publishes comparison videos, and the 1.6 model card explains the higher-resolution checkpoint. [Source 1](https://github.com/bytedance/LatentSync) [Source 2](https://huggingface.co/ByteDance/LatentSync-1.6) [Source 3](https://github.com/bytedance/LatentSync/blob/main/setup_env.sh)

### Install

Follow the reviewed project route below; these steps are documentation guidance and were not executed. [Source 1](https://github.com/bytedance/LatentSync) [Source 2](https://huggingface.co/ByteDance/LatentSync-1.6) [Source 3](https://github.com/bytedance/LatentSync/blob/main/setup_env.sh)

1. Clone the official repository and inspect the environment script before using it on your own machine.
2. The documented setup creates Python 3.10.13, installs FFmpeg, requirements and libgl1, and downloads the 1.6 checkpoints.
3. Start python gradio_app.py, or adapt the supplied inference.sh paths for a short video/audio pair.

```sh
python gradio_app.py
```

### First project

A small first project that exercises the documented creative workflow. [Source 1](https://github.com/bytedance/LatentSync) [Source 2](https://huggingface.co/ByteDance/LatentSync-1.6) [Source 3](https://github.com/bytedance/LatentSync/blob/main/setup_env.sh)

1. Use a short, authorized face clip and clean matching audio.
2. Select the correct model/config resolution: 1.6 uses 512×512; do not mix it with 1.5 settings.
3. Generate and inspect teeth, lips, expression and temporal stability before accepting the result.
### Hardware & software

Requirements are source-specific. Unreported capacities and untested platforms are not inferred. [Source 1](https://github.com/bytedance/LatentSync) [Source 2](https://huggingface.co/ByteDance/LatentSync-1.6) [Source 3](https://github.com/bytedance/LatentSync/blob/main/setup_env.sh)

- **Hardware:** Documented inference minima are 8 GB VRAM for 1.5 and 18 GB for 1.6. Training figures are separate and larger. RAM and total disk minimum are not documented.
- **Software:** Python 3.10.13, FFmpeg and the PyTorch/CUDA dependency stack from setup_env.sh; downloaded checkpoints are required.
- **Platforms:** The official setup uses Linux apt and a CUDA inference path. Native Mac/Windows support is not established by this setup; community wrappers are separate.

### License, model weights & costs

The complete software license was archived and reviewed. Keep software, model weights, dependencies and hosted-service terms separate. [Source 1](https://github.com/bytedance/LatentSync/blob/main/LICENSE) [Source 2](https://github.com/bytedance/LatentSync) [Source 3](https://huggingface.co/ByteDance/LatentSync-1.6) [Source 4](https://github.com/bytedance/LatentSync/blob/main/setup_env.sh)

- **Code:** Apache-2.0
- **Weights:** Apache-2.0 source; the official 1.6 model card labels weights OpenRAIL++, which has separate conditions. Borrowed components are not automatically relicensed.
- **Commercial:** The reviewed Apache-2.0 software license permits commercial use subject to its license, notice and source-sharing obligations where applicable. This does not establish permission for every model, input, output or service.
- **Cost:** No source license fee; GPU compute, storage and any hosted execution cost are separate.

### Why it merits attention

The project documents resolution-specific VRAM needs and provides a concrete audio/video workflow with comparison material. [Source 1](https://github.com/bytedance/LatentSync) [Source 2](https://huggingface.co/ByteDance/LatentSync-1.6) [Source 3](https://github.com/bytedance/LatentSync/blob/main/setup_env.sh)

### Limitations

More guidance can produce jitter/distortion; more sampling steps cost time. A successful render is not proof of natural expression or exact phoneme alignment. This edition is a documentation review, not an installation or output-quality test. [Source 1](https://github.com/bytedance/LatentSync) [Source 2](https://huggingface.co/ByteDance/LatentSync-1.6) [Source 3](https://github.com/bytedance/LatentSync/blob/main/setup_env.sh)

### Get the tool

- [Repository](https://github.com/bytedance/LatentSync)
- [License](https://github.com/bytedance/LatentSync/blob/main/LICENSE)
- [Documentation](https://huggingface.co/ByteDance/LatentSync-1.6)

## StreamDiffusion

Interactive, immersive & live media · Performance, projection & stage media · Images & design · Computational art & creative coding

First detailed guide, completing an earlier screened lead. This is a documentation baseline, not a claim that the project launched today.

### How it uses AI

A diffusion inference pipeline designed to reduce latency for continuous text-to-image and image-to-image interaction. Creative use: Live camera/screen transformations, interactive image instruments and installation prototypes. [Source](https://github.com/cumulo-autumn/StreamDiffusion) [Source](https://huggingface.co/papers/2312.12491)

### Introduction

A diffusion inference pipeline designed to reduce latency for continuous text-to-image and image-to-image interaction. [Source 1](https://github.com/cumulo-autumn/StreamDiffusion) [Source 2](https://huggingface.co/papers/2312.12491)

### What it is good for

Live camera/screen transformations, interactive image instruments and installation prototypes. [Source 1](https://github.com/cumulo-autumn/StreamDiffusion) [Source 2](https://huggingface.co/papers/2312.12491)

### Demo & examples

The repository contains real-time text and camera/screen demo folders with animated examples. [Source 1](https://github.com/cumulo-autumn/StreamDiffusion) [Source 2](https://huggingface.co/papers/2312.12491)

### Install

Follow the reviewed project route below; these steps are documentation guidance and were not executed. [Source 1](https://github.com/cumulo-autumn/StreamDiffusion) [Source 2](https://huggingface.co/papers/2312.12491)

1. Clone the repository and create the documented Python 3.10 environment.
2. Install the matching PyTorch 2.1/torchvision 0.16 CUDA 11.8 or 12.1 stack.
3. Install StreamDiffusion with the TensorRT extra and follow its TensorRT setup, or use the documented CUDA Docker route.
### First project

A small first project that exercises the documented creative workflow. [Source 1](https://github.com/cumulo-autumn/StreamDiffusion) [Source 2](https://huggingface.co/papers/2312.12491)

1. Start from the appropriate demo/example and load a compatible diffusion model.
2. Warm up the stream and try a low-resolution still before a live camera feed.
3. Adjust steps, guidance and similarity filtering while measuring actual end-to-end latency.
### Hardware & software

Requirements are source-specific. Unreported capacities and untested platforms are not inferred. [Source 1](https://github.com/cumulo-autumn/StreamDiffusion) [Source 2](https://huggingface.co/papers/2312.12491)

- **Hardware:** The published 93–106 FPS examples use an RTX 4090, i9-13900K and Ubuntu 22.04.3, and are not hardware minima or universal results. Minimum RAM, VRAM and disk are not documented.
- **Software:** Python 3.10, compatible PyTorch/CUDA/xformers, model downloads and optional TensorRT engine compilation.
- **Platforms:** Windows and Linux CUDA instructions are documented; the reviewed upstream guide does not establish native Apple Silicon or CPU performance.

### License, model weights & costs

The complete software license was archived and reviewed. Keep software, model weights, dependencies and hosted-service terms separate. [Source 1](https://github.com/cumulo-autumn/StreamDiffusion/blob/main/LICENSE) [Source 2](https://github.com/cumulo-autumn/StreamDiffusion) [Source 3](https://huggingface.co/papers/2312.12491)

- **Code:** Apache-2.0
- **Weights:** Apache-2.0 pipeline code. SD-Turbo, LCM adapters, Kohaku and other loaded checkpoints have their own licenses.
- **Commercial:** The reviewed Apache-2.0 software license permits commercial use subject to its license, notice and source-sharing obligations where applicable. This does not establish permission for every model, input, output or service.
- **Cost:** Local GPU compute and model storage; no compulsory hosted inference subscription is stated.

### Why it merits attention

Explicit streaming, batching, warm-up and frame-skipping controls are useful foundations for live-media engineering. [Source 1](https://github.com/cumulo-autumn/StreamDiffusion) [Source 2](https://huggingface.co/papers/2312.12491)

### Limitations

This is a developer pipeline, not a finished show-control application. Temporal consistency, capture/encoding overhead and latency need testing on the actual performance rig. This edition is a documentation review, not an installation or output-quality test. [Source 1](https://github.com/cumulo-autumn/StreamDiffusion) [Source 2](https://huggingface.co/papers/2312.12491)

### Get the tool

- [Repository](https://github.com/cumulo-autumn/StreamDiffusion)
- [License](https://github.com/cumulo-autumn/StreamDiffusion/blob/main/LICENSE)
- [Documentation](https://huggingface.co/papers/2312.12491)

## BackgroundRemover

Photography, restoration & color · Video, animation & film · VFX, compositing & relighting · Archives, media restoration & collections

First detailed guide, completing an earlier screened lead. This is a documentation baseline, not a claim that the project launched today.

### How it uses AI

A command-line image and video cutout tool using U²-Net segmentation, with alpha and compositing outputs. Creative use: Preparing product cutouts, portrait overlays and transparent video layers in a scripted media pipeline. [Source](https://github.com/nadermx/backgroundremover) [Source](https://pypi.org/project/backgroundremover/)

### Introduction

A command-line image and video cutout tool using U²-Net segmentation, with alpha and compositing outputs. [Source 1](https://github.com/nadermx/backgroundremover) [Source 2](https://pypi.org/project/backgroundremover/)

### What it is good for

Preparing product cutouts, portrait overlays and transparent video layers in a scripted media pipeline. [Source 1](https://github.com/nadermx/backgroundremover) [Source 2](https://pypi.org/project/backgroundremover/)

### Demo & examples

The README and PyPI page include before/after media and CLI examples; outputs were not regenerated. [Source 1](https://github.com/nadermx/backgroundremover) [Source 2](https://pypi.org/project/backgroundremover/)

### Install

Follow the reviewed project route below; these steps are documentation guidance and were not executed. [Source 1](https://github.com/nadermx/backgroundremover) [Source 2](https://pypi.org/project/backgroundremover/)

1. Install the package in an isolated environment with compatible PyTorch/torchvision and FFmpeg.
2. Allow the documented first-use U²-Net model download.
3. Start with one image, then move to the slower video workflow or the documented Docker route.

```sh
pip install backgroundremover
```


```sh
backgroundremover -i input.jpg -o output.png
```

### First project

A small first project that exercises the documented creative workflow. [Source 1](https://github.com/nadermx/backgroundremover) [Source 2](https://pypi.org/project/backgroundremover/)

1. Run a single-image cutout and inspect fine edges.
2. For video, use the transparent-video option and review every difficult transition.
3. Composite over a contrasting plate; compare against the original and retain the original archive.
### Hardware & software

Requirements are source-specific. Unreported capacities and untested platforms are not inferred. [Source 1](https://github.com/nadermx/backgroundremover) [Source 2](https://pypi.org/project/backgroundremover/)

- **Hardware:** CPU is the default fallback and CUDA is supported. RAM, VRAM and total storage minima are not specified; video length/resolution affect memory and run time.
- **Software:** The package documentation lists Python >=3.6, python-dev, PyTorch/torchvision and FFmpeg 4.4+. This older lower bound is not proof that every current dependency installs on Python 3.6.
- **Platforms:** Windows, macOS and Linux installation routes are documented. CoreML is a planned feature, not confirmed current acceleration.

### License, model weights & costs

The complete software license was archived and reviewed. Keep software, model weights, dependencies and hosted-service terms separate. [Source 1](https://github.com/nadermx/backgroundremover/blob/main/LICENSE.txt) [Source 2](https://github.com/nadermx/backgroundremover) [Source 3](https://pypi.org/project/backgroundremover/)

- **Code:** MIT
- **Weights:** MIT application code; the package identifies U²-Net models separately and credits their upstream terms. Check the exact downloaded weights and other dependencies.
- **Commercial:** The reviewed MIT software license permits commercial use subject to its license, notice and source-sharing obligations where applicable. This does not establish permission for every model, input, output or service.
- **Cost:** No software fee; local compute and disk storage are required.

### Why it merits attention

Simple repeatable commands and distinct alpha/video outputs make it useful as a pipeline component. [Source 1](https://github.com/nadermx/backgroundremover) [Source 2](https://pypi.org/project/backgroundremover/)

### Limitations

Hair, low contrast, reflections and fast motion remain difficult. Removing backgrounds can erase historically meaningful detail, so preserve original files. This edition is a documentation review, not an installation or output-quality test. [Source 1](https://github.com/nadermx/backgroundremover) [Source 2](https://pypi.org/project/backgroundremover/)

### Get the tool

- [Repository](https://github.com/nadermx/backgroundremover)
- [License](https://github.com/nadermx/backgroundremover/blob/main/LICENSE.txt)
- [Documentation](https://pypi.org/project/backgroundremover/)

## ReShot

Video, animation & film · Motion capture & character animation · VFX, compositing & relighting · Photogrammetry, scanning & neural rendering

First detailed guide in this library. The repository was created in the current discovery window; this is a documentation baseline, not a verified launch date.

### How it uses AI

A local video preprocessor that derives neural depth or body-pose control videos for downstream AI video generation; its Canny option is deterministic, not AI. Creative use: Transferring shot blocking and movement into a new video concept, or exporting pose keypoints for further editing. [Source](https://github.com/maosika-ai/reshot) [Source](https://github.com/maosika-ai/reshot/blob/main/docs/USAGE.md)

### Introduction

A local video preprocessor that derives neural depth or body-pose control videos for downstream AI video generation; its Canny option is deterministic, not AI. [Source 1](https://github.com/maosika-ai/reshot) [Source 2](https://github.com/maosika-ai/reshot/blob/main/docs/USAGE.md)

### What it is good for

Transferring shot blocking and movement into a new video concept, or exporting pose keypoints for further editing. [Source 1](https://github.com/maosika-ai/reshot) [Source 2](https://github.com/maosika-ai/reshot/blob/main/docs/USAGE.md)

### Demo & examples

The repository includes reference/depth/pose comparisons, finished takes, prompts and seeds. These are developer demonstrations, not a controlled proof that either control type is superior. [Source 1](https://github.com/maosika-ai/reshot) [Source 2](https://github.com/maosika-ai/reshot/blob/main/docs/USAGE.md)

### Install

Follow the reviewed project route below; these steps are documentation guidance and were not executed. [Source 1](https://github.com/maosika-ai/reshot) [Source 2](https://github.com/maosika-ai/reshot/blob/main/docs/USAGE.md)

1. Install the official PyPI package in a compatible Python environment; add the ffmpeg extra if FFmpeg is not already available.
2. For skeleton extraction, install the pose extra and the appropriate ONNX Runtime backend.
3. Run reshot for its local browser UI, or pass a short clip to the CLI. First use downloads the selected models.

```sh
pip install "reshot[ffmpeg]"
```


```sh
reshot
```

### First project

A small first project that exercises the documented creative workflow. [Source 1](https://github.com/maosika-ai/reshot) [Source 2](https://github.com/maosika-ai/reshot/blob/main/docs/USAGE.md)

1. Use a short authorized clip and choose depth or pose.
2. Generate a control MP4 and optionally pose JSON, checking cuts and tracked people.
3. Feed it to a compatible downstream model with an explicit description of the desired new appearance, then review the resulting motion.
### Hardware & software

Requirements are source-specific. Unreported capacities and untested platforms are not inferred. [Source 1](https://github.com/maosika-ai/reshot) [Source 2](https://github.com/maosika-ai/reshot/blob/main/docs/USAGE.md)

- **Hardware:** The README lists NVIDIA 8 GB+ for fast mode, with about 3 GB measured use, and 12 GB+ for full mode, with about 11 GB use. Apple Silicon and slower CPU paths are documented. It reports 16 GB host RAM covering roughly 27 seconds at 720p; depth weights are 111 MB and pose weights about 340 MB. These are workload-specific figures, not universal guarantees.
- **Software:** Python 3.10 or newer, PyTorch 2.1 or newer, and FFmpeg. Optional pose support requires ONNX Runtime; use its GPU build only with a compatible NVIDIA setup. The guide recommends a recent PyTorch build for Apple MPS performance.
- **Platforms:** CUDA, Apple Silicon and CPU routes are documented. Mac pose inference uses CPU in the cited benchmark; the README warns that no official Windows EXE installer exists.

### License, model weights & costs

The complete software license was archived and reviewed. Keep software, model weights, dependencies and hosted-service terms separate. [Source 1](https://github.com/maosika-ai/reshot/blob/main/LICENSE) [Source 2](https://github.com/maosika-ai/reshot) [Source 3](https://github.com/maosika-ai/reshot/blob/main/docs/USAGE.md)

- **Code:** Apache-2.0
- **Weights:** Apache-2.0 code; the README identifies default Small depth and DWPose models as Apache. Larger optional depth models are CC-BY-NC. Downstream generators have independent licenses/services.
- **Commercial:** The reviewed Apache-2.0 software license permits commercial use subject to its license, notice and source-sharing obligations where applicable. This does not establish permission for every model, input, output or service.
- **Cost:** Local preprocessing has no software fee; video-generation APIs or hosted GPUs can cost separately.

### Why it merits attention

Documented control exports, retained prompts and per-run metrics make the workflow inspectable. [Source 1](https://github.com/maosika-ai/reshot) [Source 2](https://github.com/maosika-ai/reshot/blob/main/docs/USAGE.md)

### Limitations

Pose can invent off-screen joints in close-ups; Canny preserves identity-bearing outlines. The README contains differing Mac timing examples, so measure your selected version/mode. Control videos do not ensure precise reproduction. The README and usage guide give different Apple Silicon timing examples, so neither is a reliable speed promise for a new machine. This edition is a documentation review, not an installation or output-quality test. [Source 1](https://github.com/maosika-ai/reshot) [Source 2](https://github.com/maosika-ai/reshot/blob/main/docs/USAGE.md)

### Get the tool

- [Repository](https://github.com/maosika-ai/reshot)
- [License](https://github.com/maosika-ai/reshot/blob/main/LICENSE)
- [Documentation](https://github.com/maosika-ai/reshot/blob/main/docs/USAGE.md)

## Draw Your Font

Typography, fonts & layout · Vector graphics, illustration & textures · Creative publishing & presentation · Computational art & creative coding

First detailed guide in this library. This is a documentation baseline, not a claim that the project launched today.

### How it uses AI

A font-building CLI with an AI-agent workflow: vision labels photographed handwriting and critiques the result, while deterministic code traces and builds the glyphs. Creative use: Turning your own hand lettering into a usable TTF or web font and iterating on weight, smoothing and problem glyphs. [Source](https://github.com/danilo-znamerovszkij/draw-your-font) [Source](https://drawyourfont.com/)

### Introduction

A font-building CLI with an AI-agent workflow: vision labels photographed handwriting and critiques the result, while deterministic code traces and builds the glyphs. [Source 1](https://github.com/danilo-znamerovszkij/draw-your-font) [Source 2](https://drawyourfont.com/)

### What it is good for

Turning your own hand lettering into a usable TTF or web font and iterating on weight, smoothing and problem glyphs. [Source 1](https://github.com/danilo-znamerovszkij/draw-your-font) [Source 2](https://drawyourfont.com/)

### Demo & examples

The official site shows a photographed alphabet and its resulting font, plus a browser conversion demo. The browser/CLI-only path itself does not require AI. [Source 1](https://github.com/danilo-znamerovszkij/draw-your-font) [Source 2](https://drawyourfont.com/)

### Install

Follow the reviewed project route below; these steps are documentation guidance and were not executed. [Source 1](https://github.com/danilo-znamerovszkij/draw-your-font) [Source 2](https://drawyourfont.com/)

1. Use Node 18+ and the documented npm CLI.
2. For AI-assisted labeling/refinement, add the repository’s draw-your-font skill to a compatible agent such as Claude Code.
3. Start with the printable alphabet template or a well-lit photo of separated letters.

```sh
npx draw-your-font template -o template.pdf
```


```sh
npx draw-your-font make photo.jpg --chars "ABCabc" --name "My Hand"
```

### First project

A small first project that exercises the documented creative workflow. [Source 1](https://github.com/danilo-znamerovszkij/draw-your-font) [Source 2](https://drawyourfont.com/)

1. Give the agent the image and identify the intended alphabet, or provide --chars manually.
2. Generate the font and inspect a preview of ordinary words and troublesome pairs.
3. Correct mislabeled glyphs and export the requested TTF/WOFF/WOFF2 formats.
### Hardware & software

Requirements are source-specific. Unreported capacities and untested platforms are not inferred. [Source 1](https://github.com/danilo-znamerovszkij/draw-your-font) [Source 2](https://drawyourfont.com/)

- **Hardware:** No RAM, VRAM, CPU or storage minimum is documented; no local GPU requirement is stated for the deterministic CLI.
- **Software:** Node >=18; the CLI is described as pure npm without system FontForge/ImageMagick/Potrace binaries. The AI route requires a separately available vision-capable agent.
- **Platforms:** macOS, Linux and Windows wherever the documented Node version runs. The browser demo is a separate local deterministic path.

### License, model weights & costs

The complete software license was archived and reviewed. Keep software, model weights, dependencies and hosted-service terms separate. [Source 1](https://github.com/danilo-znamerovszkij/draw-your-font/blob/main/LICENSE) [Source 2](https://github.com/danilo-znamerovszkij/draw-your-font) [Source 3](https://drawyourfont.com/)

- **Code:** MIT
- **Weights:** MIT tool/skill code; the chosen agent/model has separate terms. Use your own or appropriately licensed handwriting/artwork.
- **Commercial:** The reviewed MIT software license permits commercial use subject to its license, notice and source-sharing obligations where applicable. This does not establish permission for every model, input, output or service.
- **Cost:** CLI has no fee; a hosted vision agent can require a subscription or inference charges.

### Why it merits attention

Keeping glyph geometry tied to the source handwriting and exporting editable font files gives the creator useful control. [Source 1](https://github.com/danilo-znamerovszkij/draw-your-font) [Source 2](https://drawyourfont.com/)

### Limitations

Kerning, ligatures and glyph randomization are described as planned. Do not extend the site’s no-upload claim to a cloud vision-agent workflow: the agent’s handling of submitted images determines that. This edition is a documentation review, not an installation or output-quality test. [Source 1](https://github.com/danilo-znamerovszkij/draw-your-font) [Source 2](https://drawyourfont.com/)

### Get the tool

- [Repository](https://github.com/danilo-znamerovszkij/draw-your-font)
- [License](https://github.com/danilo-znamerovszkij/draw-your-font/blob/main/LICENSE)
- [Documentation](https://drawyourfont.com/)

## Khatt Engine

Typography, fonts & layout · Images & design · Vector graphics, illustration & textures

First detailed guide in this library. This is a documentation baseline, not a claim that the project launched today.

### How it uses AI

An Arabic calligraphy prototype that shapes text with HarfBuzz/FreeType, then uses an AI image service for surface styling and OCR for a limited check. Creative use: Exploring ink, paper and color treatments while retaining a font-derived Arabic text skeleton. [Source](https://github.com/dino880917/khatt-engine) [Source](https://khatt-engine.onrender.com/)

### Introduction

An Arabic calligraphy prototype that shapes text with HarfBuzz/FreeType, then uses an AI image service for surface styling and OCR for a limited check. [Source 1](https://github.com/dino880917/khatt-engine) [Source 2](https://khatt-engine.onrender.com/)

### What it is good for

Exploring ink, paper and color treatments while retaining a font-derived Arabic text skeleton. [Source 1](https://github.com/dino880917/khatt-engine) [Source 2](https://khatt-engine.onrender.com/)

### Demo & examples

The README links a hosted demo, but that endpoint was inaccessible during this review. No live-output validation is claimed. [Source 1](https://github.com/dino880917/khatt-engine) [Source 2](https://khatt-engine.onrender.com/)

### Install

Follow the reviewed project route below; these steps are documentation guidance and were not executed. [Source 1](https://github.com/dino880917/khatt-engine) [Source 2](https://khatt-engine.onrender.com/)

1. Clone dino880917/khatt-engine; the README’s your-username clone address is a placeholder.
2. Create a Python 3.11+ virtual environment and install the project with uv pip install -e .
3. Place the documented Arabic fonts in assets/fonts and configure the Stability API credential locally.

```sh
uv pip install -e .
```


```sh
python -m khatt "بسم الله" --style thuluth
```

### First project

A small first project that exercises the documented creative workflow. [Source 1](https://github.com/dino880917/khatt-engine) [Source 2](https://khatt-engine.onrender.com/)

1. Enter a short Arabic phrase and choose a supported style.
2. Compare the shaped skeleton with the original text before stylization.
3. Inspect the final image manually for dots, diacritics and letter order; export only after a fluent reader checks it.
### Hardware & software

Requirements are source-specific. Unreported capacities and untested platforms are not inferred. [Source 1](https://github.com/dino880917/khatt-engine) [Source 2](https://khatt-engine.onrender.com/)

- **Hardware:** No RAM, VRAM, CPU or disk minimum is documented. Stylization uses a remote API; local font processing/OCR still needs its dependencies.
- **Software:** Python 3.11+, uv, HarfBuzz/FreeType, EasyOCR models, the specified fonts and a Stability AI API key/internet connection.
- **Platforms:** The README lists Windows, macOS and Linux; the optional FastAPI browser interface normally uses port 8000.

### License, model weights & costs

The complete software license was archived and reviewed. Keep software, model weights, dependencies and hosted-service terms separate. [Source 1](https://github.com/dino880917/khatt-engine/blob/main/LICENSE) [Source 2](https://github.com/dino880917/khatt-engine) [Source 3](https://khatt-engine.onrender.com/)

- **Code:** MIT
- **Weights:** MIT application. Stability services, OCR models and downloaded fonts retain their own terms.
- **Commercial:** The reviewed MIT software license permits commercial use subject to its license, notice and source-sharing obligations where applicable. This does not establish permission for every model, input, output or service.
- **Cost:** Local code is free; API usage may be billed. No current free-tier allowance was independently confirmed.

### Why it merits attention

Separating shaping from styling is a concrete, inspectable approach to a language-specific creative problem. [Source 1](https://github.com/dino880917/khatt-engine) [Source 2](https://khatt-engine.onrender.com/)

### Limitations

Despite stronger marketing language, OCR currently checks the skeleton, not the final stylized image. Thuluth, Naskh and Diwani share Amiri geometry and differ only by styling prompts; linguistic correctness is not guaranteed. This edition is a documentation review, not an installation or output-quality test. [Source 1](https://github.com/dino880917/khatt-engine) [Source 2](https://khatt-engine.onrender.com/)

### Get the tool

- [Repository](https://github.com/dino880917/khatt-engine)
- [License](https://github.com/dino880917/khatt-engine/blob/main/LICENSE)
- [Documentation](https://khatt-engine.onrender.com/)

## Immersive Web SDK

WebXR, VR & AR · Browser tools & web media · Interactive, immersive & live media · 3D, reconstruction & assets · Games & production pipelines

First detailed guide in this library. This is a documentation baseline, not a claim that the project launched today.

### How it uses AI

A WebXR development framework with an AI-agent integration that lets an assistant inspect scenes, take screenshots and exercise emulated interactions. Creative use: Building interactive browser-based 3D/VR scenes with agent-assisted coding and visual debugging. [Source](https://github.com/facebook/immersive-web-sdk) [Source](https://iwsdk.dev/) [Source](https://developers.meta.com/vr/blog/accelerate-vr-development-with-ai-and-immersive-web-sdk/)

### Introduction

A WebXR development framework with an AI-agent integration that lets an assistant inspect scenes, take screenshots and exercise emulated interactions. [Source 1](https://github.com/facebook/immersive-web-sdk) [Source 2](https://iwsdk.dev/) [Source 3](https://developers.meta.com/vr/blog/accelerate-vr-development-with-ai-and-immersive-web-sdk/)

### What it is good for

Building interactive browser-based 3D/VR scenes with agent-assisted coding and visual debugging. [Source 1](https://github.com/facebook/immersive-web-sdk) [Source 2](https://iwsdk.dev/) [Source 3](https://developers.meta.com/vr/blog/accelerate-vr-development-with-ai-and-immersive-web-sdk/)

### Demo & examples

The official documentation includes examples, while Meta’s primary article describes the scene-inspection and agent workflow. No headset or browser runtime was tested. [Source 1](https://github.com/facebook/immersive-web-sdk) [Source 2](https://iwsdk.dev/) [Source 3](https://developers.meta.com/vr/blog/accelerate-vr-development-with-ai-and-immersive-web-sdk/)

### Install

Follow the reviewed project route below; these steps are documentation guidance and were not executed. [Source 1](https://github.com/facebook/immersive-web-sdk) [Source 2](https://iwsdk.dev/) [Source 3](https://developers.meta.com/vr/blog/accelerate-vr-development-with-ai-and-immersive-web-sdk/)

1. Install the documented Node 20+ prerequisite and scaffold a project with npm create @iwsdk@latest.
2. Choose the offered AI integration and follow the generated project’s development instructions.
3. For an existing app, follow the current README’s exact Three.js alias/override requirement to avoid duplicate runtimes.

```sh
npm create @iwsdk@latest
```

### First project

A small first project that exercises the documented creative workflow. [Source 1](https://github.com/facebook/immersive-web-sdk) [Source 2](https://iwsdk.dev/) [Source 3](https://developers.meta.com/vr/blog/accelerate-vr-development-with-ai-and-immersive-web-sdk/)

1. Start from a small scene and request one concrete interaction.
2. Use the agent tooling to inspect the scene and emulate input, then review the code and screenshots.
3. Test the actual immersive behavior on the target browser/headset before deployment.
### Hardware & software

Requirements are source-specific. Unreported capacities and untested platforms are not inferred. [Source 1](https://github.com/facebook/immersive-web-sdk) [Source 2](https://iwsdk.dev/) [Source 3](https://developers.meta.com/vr/blog/accelerate-vr-development-with-ai-and-immersive-web-sdk/)

- **Hardware:** A development laptop and compatible browser are documented; numeric CPU, RAM, VRAM and disk minima are not published. Quest 3/3S/Pro are recommended test devices, not a prerequisite for desktop authoring.
- **Software:** Node 20+ per Meta’s setup article, npm and the SDK’s pinned dependencies; source-repository development also has its own pinned Node/pnpm toolchain. AI requires a compatible external agent.
- **Platforms:** Desktop emulation and WebXR-capable browser/headset operation are distinct. Meta names Chrome/Edge for development; headset/browser support must be checked for the deployed experience.

### License, model weights & costs

The complete software license was archived and reviewed. Keep software, model weights, dependencies and hosted-service terms separate. [Source 1](https://github.com/facebook/immersive-web-sdk/blob/main/LICENSE) [Source 2](https://github.com/facebook/immersive-web-sdk) [Source 3](https://iwsdk.dev/) [Source 4](https://developers.meta.com/vr/blog/accelerate-vr-development-with-ai-and-immersive-web-sdk/)

- **Code:** MIT
- **Weights:** MIT SDK. AI providers, optional models, assets and platform services retain their own terms.
- **Commercial:** The reviewed MIT software license permits commercial use subject to its license, notice and source-sharing obligations where applicable. This does not establish permission for every model, input, output or service.
- **Cost:** No SDK fee; agent inference, hosting and headset hardware can cost separately.

### Why it merits attention

Scene-aware inspection and emulated input offer a concrete AI contribution beyond a generic graphics framework. [Source 1](https://github.com/facebook/immersive-web-sdk) [Source 2](https://iwsdk.dev/) [Source 3](https://developers.meta.com/vr/blog/accelerate-vr-development-with-ai-and-immersive-web-sdk/)

### Limitations

Agent-generated code still needs review, and desktop emulation does not establish comfort, performance or tracking quality in a headset. This edition is a documentation review, not an installation or output-quality test. [Source 1](https://github.com/facebook/immersive-web-sdk) [Source 2](https://iwsdk.dev/) [Source 3](https://developers.meta.com/vr/blog/accelerate-vr-development-with-ai-and-immersive-web-sdk/)

### Get the tool

- [Repository](https://github.com/facebook/immersive-web-sdk)
- [License](https://github.com/facebook/immersive-web-sdk/blob/main/LICENSE)
- [Documentation](https://iwsdk.dev/)

## VoiceStudio (open-source edition)

Audio, music & voice · Accessible media & assistive creation · Editing, captions & post-production · Storyboarding, narrative & comics

First detailed guide in this library. This is a documentation baseline, not a claim that the project launched today.

### How it uses AI

An Electron/FastAPI studio for model-based voice generation, cloning, transcription, dubbing and audiobooks, with multiple selectable engines. Creative use: Creating authorized narration and experimenting with timed multilingual dialogue or audiobook chapters. [Source](https://github.com/debpalash/VoiceStudio) [Source](https://voicestudio.sh/) [Source](https://github.com/debpalash/VoiceStudio/blob/main/LICENSE-NOTICE.md) [Source](https://github.com/debpalash/VoiceStudio/blob/main/docs/performance.md) [Source](https://github.com/debpalash/VoiceStudio/releases/tag/v0.5.6)

### Introduction

An Electron/FastAPI studio for model-based voice generation, cloning, transcription, dubbing and audiobooks, with multiple selectable engines. [Source 1](https://github.com/debpalash/VoiceStudio) [Source 2](https://voicestudio.sh/) [Source 3](https://github.com/debpalash/VoiceStudio/blob/main/LICENSE-NOTICE.md) [Source 4](https://github.com/debpalash/VoiceStudio/blob/main/docs/performance.md) [Source 5](https://github.com/debpalash/VoiceStudio/releases/tag/v0.5.6)

### What it is good for

Creating authorized narration and experimenting with timed multilingual dialogue or audiobook chapters. [Source 1](https://github.com/debpalash/VoiceStudio) [Source 2](https://voicestudio.sh/) [Source 3](https://github.com/debpalash/VoiceStudio/blob/main/LICENSE-NOTICE.md) [Source 4](https://github.com/debpalash/VoiceStudio/blob/main/docs/performance.md) [Source 5](https://github.com/debpalash/VoiceStudio/releases/tag/v0.5.6)

### Demo & examples

The official site and repository show the cloning, dubbing and model-management workspaces. Language counts are developer claims and depend on the engine. [Source 1](https://github.com/debpalash/VoiceStudio) [Source 2](https://voicestudio.sh/) [Source 3](https://github.com/debpalash/VoiceStudio/blob/main/LICENSE-NOTICE.md) [Source 4](https://github.com/debpalash/VoiceStudio/blob/main/docs/performance.md) [Source 5](https://github.com/debpalash/VoiceStudio/releases/tag/v0.5.6)

### Install

Follow the reviewed project route below; these steps are documentation guidance and were not executed. [Source 1](https://github.com/debpalash/VoiceStudio) [Source 2](https://voicestudio.sh/) [Source 3](https://github.com/debpalash/VoiceStudio/blob/main/LICENSE-NOTICE.md) [Source 4](https://github.com/debpalash/VoiceStudio/blob/main/docs/performance.md) [Source 5](https://github.com/debpalash/VoiceStudio/releases/tag/v0.5.6)

1. Download the open-source Electron release for your platform from the official GitHub release page.
2. Install its local runtime and select an engine whose model terms fit your project.
3. Install the required model, then check the reported compute device before generating. Intel Mac users need a remote backend.
### First project

A small first project that exercises the documented creative workflow. [Source 1](https://github.com/debpalash/VoiceStudio) [Source 2](https://voicestudio.sh/) [Source 3](https://github.com/debpalash/VoiceStudio/blob/main/LICENSE-NOTICE.md) [Source 4](https://github.com/debpalash/VoiceStudio/blob/main/docs/performance.md) [Source 5](https://github.com/debpalash/VoiceStudio/releases/tag/v0.5.6)

1. Use a built-in voice or a clean reference recording you have permission to use.
2. Generate a short passage, revise pronunciation and timing, then try a longer story or dub.
3. Review each chapter/segment and export approved audio or video.
### Hardware & software

Requirements are source-specific. Unreported capacities and untested platforms are not inferred. [Source 1](https://github.com/debpalash/VoiceStudio) [Source 2](https://voicestudio.sh/) [Source 3](https://github.com/debpalash/VoiceStudio/blob/main/LICENSE-NOTICE.md) [Source 4](https://github.com/debpalash/VoiceStudio/blob/main/docs/performance.md) [Source 5](https://github.com/debpalash/VoiceStudio/releases/tag/v0.5.6)

- **Hardware:** The site says about 8 GB RAM is enough to start; this is not a guarantee for all engines. The README notes roughly 5 GB free disk for the small CPU PyTorch setup, plus separate model storage. GPU needs vary; the release describes 8 GB GPU audiobook fixes.
- **Software:** Packaged Electron app with managed Python/PyTorch backend and downloaded models. Source development requires Node 22+, Bun, Rust/Cargo and build tools.
- **Platforms:** NVIDIA CUDA on Windows/Linux; Apple Silicon MPS; slower CPU routes. Intel Mac is UI plus remote backend. Windows ARM is experimental and the website/README differ on native packaging, so verify the exact release asset.

### License, model weights & costs

The complete software license was archived and reviewed. Keep software, model weights, dependencies and hosted-service terms separate. [Source 1](https://github.com/debpalash/VoiceStudio/blob/main/LICENSE) [Source 2](https://github.com/debpalash/VoiceStudio) [Source 3](https://voicestudio.sh/) [Source 4](https://github.com/debpalash/VoiceStudio/blob/main/LICENSE-NOTICE.md) [Source 5](https://github.com/debpalash/VoiceStudio/blob/main/docs/performance.md) [Source 6](https://github.com/debpalash/VoiceStudio/releases/tag/v0.5.6)

- **Code:** AGPL-3.0
- **Weights:** AGPL-3.0 application permits commercial use under its terms. The default OmniVoice weights are CC-BY-NC, and its tokenizer has Boson Higgs/Meta Llama terms; paid VoiceStudio code licensing does not replace model permissions. Other engines differ.
- **Commercial:** The reviewed AGPL-3.0 software license permits commercial use subject to its license, notice and source-sharing obligations where applicable. This does not establish permission for every model, input, output or service.
- **Cost:** The open-source app has no license fee. Pro/Cloud are separate offerings; model permissions, remote compute and optional translation APIs can add cost.

### Why it merits attention

Explicit engine/device reporting and platform documentation help choose a realistic local workflow. [Source 1](https://github.com/debpalash/VoiceStudio) [Source 2](https://voicestudio.sh/) [Source 3](https://github.com/debpalash/VoiceStudio/blob/main/LICENSE-NOTICE.md) [Source 4](https://github.com/debpalash/VoiceStudio/blob/main/docs/performance.md) [Source 5](https://github.com/debpalash/VoiceStudio/releases/tag/v0.5.6)

### Limitations

The current release notes describe unsigned/ad-hoc-signed, non-notarized installers and manual Mac updates. Quality and memory vary by engine. Do not equate a local interface with local processing when remote providers are configured. This edition is a documentation review, not an installation or output-quality test. [Source 1](https://github.com/debpalash/VoiceStudio) [Source 2](https://voicestudio.sh/) [Source 3](https://github.com/debpalash/VoiceStudio/blob/main/LICENSE-NOTICE.md) [Source 4](https://github.com/debpalash/VoiceStudio/blob/main/docs/performance.md) [Source 5](https://github.com/debpalash/VoiceStudio/releases/tag/v0.5.6)

### Get the tool

- [Repository](https://github.com/debpalash/VoiceStudio)
- [License](https://github.com/debpalash/VoiceStudio/blob/main/LICENSE)
- [Documentation](https://voicestudio.sh/)

## NeuralTailor

Fashion, textiles & wearable media · AI-assisted textile and computational craft · 3D printing & generative CAD · 3D, reconstruction & assets

First detailed guide in this library. This is a documentation baseline, not a claim that the project launched today.

### How it uses AI

A research implementation that predicts sewing-panel shapes and stitch relationships from 3D garment point clouds. Creative use: Studying garment reconstruction and computational pattern design, with inspectable predicted panels rather than only a rendered garment. [Source](https://github.com/maria-korosteleva/Garment-Pattern-Estimation) [Source](https://github.com/maria-korosteleva/Garment-Pattern-Estimation/blob/master/docs/Installation.md) [Source](https://github.com/maria-korosteleva/Garment-Pattern-Estimation/blob/master/docs/Running.md) [Source](https://zenodo.org/records/5267549)

### Introduction

A research implementation that predicts sewing-panel shapes and stitch relationships from 3D garment point clouds. [Source 1](https://github.com/maria-korosteleva/Garment-Pattern-Estimation) [Source 2](https://github.com/maria-korosteleva/Garment-Pattern-Estimation/blob/master/docs/Installation.md) [Source 3](https://github.com/maria-korosteleva/Garment-Pattern-Estimation/blob/master/docs/Running.md) [Source 4](https://zenodo.org/records/5267549)

### What it is good for

Studying garment reconstruction and computational pattern design, with inspectable predicted panels rather than only a rendered garment. [Source 1](https://github.com/maria-korosteleva/Garment-Pattern-Estimation) [Source 2](https://github.com/maria-korosteleva/Garment-Pattern-Estimation/blob/master/docs/Installation.md) [Source 3](https://github.com/maria-korosteleva/Garment-Pattern-Estimation/blob/master/docs/Running.md) [Source 4](https://zenodo.org/records/5267549)

### Demo & examples

The repository includes an overview and pretrained-model evaluation route; the authors link their garment/pattern dataset on Zenodo. [Source 1](https://github.com/maria-korosteleva/Garment-Pattern-Estimation) [Source 2](https://github.com/maria-korosteleva/Garment-Pattern-Estimation/blob/master/docs/Installation.md) [Source 3](https://github.com/maria-korosteleva/Garment-Pattern-Estimation/blob/master/docs/Running.md) [Source 4](https://zenodo.org/records/5267549)

### Install

Follow the reviewed project route below; these steps are documentation guidance and were not executed. [Source 1](https://github.com/maria-korosteleva/Garment-Pattern-Estimation) [Source 2](https://github.com/maria-korosteleva/Garment-Pattern-Estimation/blob/master/docs/Installation.md) [Source 3](https://github.com/maria-korosteleva/Garment-Pattern-Estimation/blob/master/docs/Running.md) [Source 4](https://zenodo.org/records/5267549)

1. Follow the documented Windows or Ubuntu Conda setup, using Python 3.9 and compatible PyTorch/PyG/libigl packages.
2. Download the needed dataset split and Garment-Pattern-Generator dependency, then set the local paths in system.json.
3. Use the provided models/configs for evaluation before considering retraining.

```sh
python nn/evaluation_scripts/on_test_set.py -sh models/att/att.yaml -st models/att/stitch_model.yaml --unseen --predict
```

### First project

A small first project that exercises the documented creative workflow. [Source 1](https://github.com/maria-korosteleva/Garment-Pattern-Estimation) [Source 2](https://github.com/maria-korosteleva/Garment-Pattern-Estimation/blob/master/docs/Installation.md) [Source 3](https://github.com/maria-korosteleva/Garment-Pattern-Estimation/blob/master/docs/Running.md) [Source 4](https://zenodo.org/records/5267549)

1. Run the full shape-and-stitch evaluation example on the prepared test data.
2. Inspect the separate shape and stitch prediction folders and compare with the reference patterns.
3. Treat a new pattern as a research output requiring drape, scale, seam and fit checks before physical fabrication.
### Hardware & software

Requirements are source-specific. Unreported capacities and untested platforms are not inferred. [Source 1](https://github.com/maria-korosteleva/Garment-Pattern-Estimation) [Source 2](https://github.com/maria-korosteleva/Garment-Pattern-Estimation/blob/master/docs/Installation.md) [Source 3](https://github.com/maria-korosteleva/Garment-Pattern-Estimation/blob/master/docs/Running.md) [Source 4](https://zenodo.org/records/5267549)

- **Hardware:** Numeric CPU, RAM, VRAM and storage minima are not published in the reviewed setup. Dataset and model downloads add storage; CUDA is used by documented accelerated setups.
- **Software:** Python 3.9, PyTorch, PyTorch Geometric, libigl and requirements.txt. The Windows example pins PyTorch 1.12/CUDA 11.6; Ubuntu gives a separate CUDA 12.1 route. Optional W&B tracking and Maya visualization are separate.
- **Platforms:** Developed on Windows 10/11 and Ubuntu. Other OS support, including macOS, is not confirmed.

### License, model weights & costs

The complete software license was archived and reviewed. Keep software, model weights, dependencies and hosted-service terms separate. [Source 1](https://github.com/maria-korosteleva/Garment-Pattern-Estimation/blob/master/LICENSE) [Source 2](https://github.com/maria-korosteleva/Garment-Pattern-Estimation) [Source 3](https://github.com/maria-korosteleva/Garment-Pattern-Estimation/blob/master/docs/Installation.md) [Source 4](https://github.com/maria-korosteleva/Garment-Pattern-Estimation/blob/master/docs/Running.md) [Source 5](https://zenodo.org/records/5267549)

- **Code:** MIT
- **Weights:** MIT repository source. Dataset, pretrained weights and dependency terms must be checked separately; Autodesk Maya is a proprietary optional visualization host.
- **Commercial:** The reviewed MIT software license permits commercial use subject to its license, notice and source-sharing obligations where applicable. This does not establish permission for every model, input, output or service.
- **Cost:** No source license fee; compute/storage and optional proprietary tools or hosted tracking may cost separately.

### Why it merits attention

Separating panel geometry and stitch prediction provides a useful research interface for fashion and craft workflows. [Source 1](https://github.com/maria-korosteleva/Garment-Pattern-Estimation) [Source 2](https://github.com/maria-korosteleva/Garment-Pattern-Estimation/blob/master/docs/Installation.md) [Source 3](https://github.com/maria-korosteleva/Garment-Pattern-Estimation/blob/master/docs/Running.md) [Source 4](https://zenodo.org/records/5267549)

### Limitations

Some shape-only evaluation outputs copy ground-truth stitches for comparison; use the full stitch model when assessing actual reconstruction. It does not establish production-ready fit or manufacturing tolerances. This edition is a documentation review, not an installation or output-quality test. [Source 1](https://github.com/maria-korosteleva/Garment-Pattern-Estimation) [Source 2](https://github.com/maria-korosteleva/Garment-Pattern-Estimation/blob/master/docs/Installation.md) [Source 3](https://github.com/maria-korosteleva/Garment-Pattern-Estimation/blob/master/docs/Running.md) [Source 4](https://zenodo.org/records/5267549)

### Get the tool

- [Repository](https://github.com/maria-korosteleva/Garment-Pattern-Estimation)
- [License](https://github.com/maria-korosteleva/Garment-Pattern-Estimation/blob/master/LICENSE)
- [Documentation](https://github.com/maria-korosteleva/Garment-Pattern-Estimation/blob/master/docs/Installation.md)

## AtomicDance

AI choreography and dance composition · Motion capture & character animation · Performance, projection & stage media · Avatars, digital humans & lip sync

First detailed guide in this library. This is a documentation baseline, not a claim that the project launched today.

### How it uses AI

A music-to-dance research system that plans editable atomic movements and uses diffusion to complete motion and transitions. Creative use: Studying choreography structure, replacing movement types and adjusting movement timing without working only frame by frame. [Source](https://github.com/oceanflowlab/AtomicDance) [Source](https://cxhcmhhh.github.io/AtomicDanceProject/)

### Introduction

A music-to-dance research system that plans editable atomic movements and uses diffusion to complete motion and transitions. [Source 1](https://github.com/oceanflowlab/AtomicDance) [Source 2](https://cxhcmhhh.github.io/AtomicDanceProject/)

### What it is good for

Studying choreography structure, replacing movement types and adjusting movement timing without working only frame by frame. [Source 1](https://github.com/oceanflowlab/AtomicDance) [Source 2](https://cxhcmhhh.github.io/AtomicDanceProject/)

### Demo & examples

The official project page presents movement, generation and editing examples with the paper; these were documentation examples, not reproduced experiments. [Source 1](https://github.com/oceanflowlab/AtomicDance) [Source 2](https://cxhcmhhh.github.io/AtomicDanceProject/)

### Install

Follow the reviewed project route below; these steps are documentation guidance and were not executed. [Source 1](https://github.com/oceanflowlab/AtomicDance) [Source 2](https://cxhcmhhh.github.io/AtomicDanceProject/)

1. Use the validated Linux environment: Python 3.7.12, PyTorch 1.12.1 and CUDA 11.6.
2. Install the requirements plus the pinned music-feature/PyTorch3D dependencies; prepare the released atomic dataset.
3. Obtain the separately licensed SMPL model and required planner/completion checkpoints, or train them using the documented stages.
### First project

A small first project that exercises the documented creative workflow. [Source 1](https://github.com/oceanflowlab/AtomicDance) [Source 2](https://cxhcmhhh.github.io/AtomicDanceProject/)

1. Prepare a small music/test sequence and the matching model/config paths.
2. Run the planner-plus-completion evaluator and inspect generated motions.
3. Edit an atomic movement plan and compare the resulting transitions and beat alignment.
### Hardware & software

Requirements are source-specific. Unreported capacities and untested platforms are not inferred. [Source 1](https://github.com/oceanflowlab/AtomicDance) [Source 2](https://cxhcmhhh.github.io/AtomicDanceProject/)

- **Hardware:** The README recommends a CUDA GPU with at least 16 GB memory for training and inference. Host RAM and total disk needs are not documented.
- **Software:** The validated legacy Python/PyTorch/CUDA stack, PyTorch3D 0.7.1, music-feature dependencies, atomic dataset and checkpoints.
- **Platforms:** Linux is the validated platform. Native Windows/macOS support is not documented.

### License, model weights & costs

The complete software license was archived and reviewed. Keep software, model weights, dependencies and hosted-service terms separate. [Source 1](https://github.com/oceanflowlab/AtomicDance/blob/main/LICENSE) [Source 2](https://github.com/oceanflowlab/AtomicDance) [Source 3](https://cxhcmhhh.github.io/AtomicDanceProject/)

- **Code:** MIT
- **Weights:** MIT code; SMPL, AIST++, pretrained checkpoints and other assets have separate licenses and access requirements.
- **Commercial:** The reviewed MIT software license permits commercial use subject to its license, notice and source-sharing obligations where applicable. This does not establish permission for every model, input, output or service.
- **Cost:** No source license fee; training/inference compute and dataset storage are required.

### Why it merits attention

An explicit symbolic plan gives a concrete editing mechanism for research choreography. [Source 1](https://github.com/oceanflowlab/AtomicDance) [Source 2](https://cxhcmhhh.github.io/AtomicDanceProject/)

### Limitations

The README says pretrained checkpoints will be released; their availability was not confirmed. This is not a ready-to-run consumer app, and the old dependency stack may complicate installation. This edition is a documentation review, not an installation or output-quality test. [Source 1](https://github.com/oceanflowlab/AtomicDance) [Source 2](https://cxhcmhhh.github.io/AtomicDanceProject/)

### Get the tool

- [Repository](https://github.com/oceanflowlab/AtomicDance)
- [License](https://github.com/oceanflowlab/AtomicDance/blob/main/LICENSE)
- [Documentation](https://cxhcmhhh.github.io/AtomicDanceProject/)

## DiscoForcing

AI choreography and dance composition · Motion capture & character animation · Interactive, immersive & live media · Avatars, digital humans & lip sync

First detailed guide in this library. This is a documentation baseline, not a claim that the project launched today.

### How it uses AI

An audio-conditioned diffusion framework for streaming dance motion, with a browser avatar demo and a separate ROS2 integration. Creative use: Researching music-responsive characters and interactive dance systems that react to changing audio. [Source](https://github.com/CurMack/DiscoForcing) [Source](https://discoforcing.github.io/) [Source](https://github.com/CurMack/DiscoForcing/blob/main/web_demo/README.md)

### Introduction

An audio-conditioned diffusion framework for streaming dance motion, with a browser avatar demo and a separate ROS2 integration. [Source 1](https://github.com/CurMack/DiscoForcing) [Source 2](https://discoforcing.github.io/) [Source 3](https://github.com/CurMack/DiscoForcing/blob/main/web_demo/README.md)

### What it is good for

Researching music-responsive characters and interactive dance systems that react to changing audio. [Source 1](https://github.com/CurMack/DiscoForcing) [Source 2](https://discoforcing.github.io/) [Source 3](https://github.com/CurMack/DiscoForcing/blob/main/web_demo/README.md)

### Demo & examples

The ICML 2026 project page shows streaming motion and describes avatar/robot demonstrations. Performance is author-reported. [Source 1](https://github.com/CurMack/DiscoForcing) [Source 2](https://discoforcing.github.io/) [Source 3](https://github.com/CurMack/DiscoForcing/blob/main/web_demo/README.md)

### Install

Follow the reviewed project route below; these steps are documentation guidance and were not executed. [Source 1](https://github.com/CurMack/DiscoForcing) [Source 2](https://discoforcing.github.io/) [Source 3](https://github.com/CurMack/DiscoForcing/blob/main/web_demo/README.md)

1. Create the Python 3.10 environment and install the repository requirements plus a compatible Flash Attention build.
2. Prepare the dataset, SMPL asset, configuration paths and model checkpoints described in the README.
3. For the browser route, use the web_demo setup and start its Flask server on port 5000.
### First project

A small first project that exercises the documented creative workflow. [Source 1](https://github.com/CurMack/DiscoForcing) [Source 2](https://discoforcing.github.io/) [Source 3](https://github.com/CurMack/DiscoForcing/blob/main/web_demo/README.md)

1. Validate generation from a short WAV file before trying live input.
2. Open the local web demo, grant microphone access and compare motion across music changes.
3. Inspect continuity and latency; robot deployment is a separate specialist engineering task.
### Hardware & software

Requirements are source-specific. Unreported capacities and untested platforms are not inferred. [Source 1](https://github.com/CurMack/DiscoForcing) [Source 2](https://discoforcing.github.io/) [Source 3](https://github.com/CurMack/DiscoForcing/blob/main/web_demo/README.md)

- **Hardware:** Numeric RAM, VRAM, CPU and disk minima are not documented. The selected VQ-PAE path runs model inference on GPU; published demo timing is not a universal guarantee.
- **Software:** Python 3.10+, model/dependency stack, FFmpeg and matching checkpoints; a modern Web Audio browser for the client.
- **Platforms:** The setup is Linux-oriented. Chrome/Firefox/Edge clients and remote access are documented, but that does not establish native inference support on every client OS.

### License, model weights & costs

The complete software license was archived and reviewed. Keep software, model weights, dependencies and hosted-service terms separate. [Source 1](https://github.com/CurMack/DiscoForcing/blob/main/LICENSE) [Source 2](https://github.com/CurMack/DiscoForcing) [Source 3](https://discoforcing.github.io/) [Source 4](https://github.com/CurMack/DiscoForcing/blob/main/web_demo/README.md)

- **Code:** MIT
- **Weights:** MIT code. SMPL, AIST++, FineDance and pretrained components keep their own terms; a robot platform is outside the software grant.
- **Commercial:** The reviewed MIT software license permits commercial use subject to its license, notice and source-sharing obligations where applicable. This does not establish permission for every model, input, output or service.
- **Cost:** Local or hosted GPU compute and separate physical hardware if used.

### Why it merits attention

Released generation scripts and a specific audio-to-joint browser workflow provide concrete research value. [Source 1](https://github.com/CurMack/DiscoForcing) [Source 2](https://discoforcing.github.io/) [Source 3](https://github.com/CurMack/DiscoForcing/blob/main/web_demo/README.md)

### Limitations

Checkpoint paths require preparation. Browser documentation contains inconsistent claims about system-audio capture; microphone input is the clearer documented baseline. No safety or live-show reliability was tested. This edition is a documentation review, not an installation or output-quality test. [Source 1](https://github.com/CurMack/DiscoForcing) [Source 2](https://discoforcing.github.io/) [Source 3](https://github.com/CurMack/DiscoForcing/blob/main/web_demo/README.md)

### Get the tool

- [Repository](https://github.com/CurMack/DiscoForcing)
- [License](https://github.com/CurMack/DiscoForcing/blob/main/LICENSE)
- [Documentation](https://discoforcing.github.io/)

## brag

AI agents for code-authored media production · Video, animation & film · Creative publishing & presentation · AI kinetic typography and animated lettering

First detailed guide in this library. This is a documentation baseline, not a claim that the project launched today.

### How it uses AI

An agent skill that turns a project into a short launch/demo video, using an AI assistant for the story and composition workflow. Creative use: Prototyping a short tool showcase with motion, soundtrack and draft share copy. [Source](https://github.com/latent-spaces/brag) [Source](https://latent-spaces.github.io/brag/)

### Introduction

An agent skill that turns a project into a short launch/demo video, using an AI assistant for the story and composition workflow. [Source 1](https://github.com/latent-spaces/brag) [Source 2](https://latent-spaces.github.io/brag/)

### What it is good for

Prototyping a short tool showcase with motion, soundtrack and draft share copy. [Source 1](https://github.com/latent-spaces/brag) [Source 2](https://latent-spaces.github.io/brag/)

### Demo & examples

The official launch site presents several finished example videos and the project’s own launch clip. [Source 1](https://github.com/latent-spaces/brag) [Source 2](https://latent-spaces.github.io/brag/)

### Install

Follow the reviewed project route below; these steps are documentation guidance and were not executed. [Source 1](https://github.com/latent-spaces/brag) [Source 2](https://latent-spaces.github.io/brag/)

1. Use a compatible agent and install the documented brag skill from its official repository.
2. The classic workflow needs Node 22+, FFmpeg on PATH and Hyperframes; check that renderer’s setup separately.
3. Choose the classic workflow explicitly if needed; the newer slim path has different dependencies and a model-specific design.
### First project

A small first project that exercises the documented creative workflow. [Source 1](https://github.com/latent-spaces/brag) [Source 2](https://latent-spaces.github.io/brag/)

1. Run the skill inside a project you can truthfully demonstrate and state the intended tone.
2. Review the proposed story and on-screen claims before rendering.
3. Inspect brag-output/brag.mp4, captions, audio and share copy; posting to social accounts is a separate action.
### Hardware & software

Requirements are source-specific. Unreported capacities and untested platforms are not inferred. [Source 1](https://github.com/latent-spaces/brag) [Source 2](https://latent-spaces.github.io/brag/)

- **Hardware:** No CPU, RAM, VRAM or storage minimum is documented. Rendering and any local inference depend on the selected workflow.
- **Software:** Agent with skill support; classic route Node 22+, FFmpeg and Hyperframes. Narration is optional and uses Kokoro through that renderer.
- **Platforms:** The README includes Windows symlink caveats and portable agent-directory installation; it does not publish a complete minimum-OS compatibility matrix.

### License, model weights & costs

The complete software license was archived and reviewed. Keep software, model weights, dependencies and hosted-service terms separate. [Source 1](https://github.com/latent-spaces/brag/blob/main/LICENSE) [Source 2](https://github.com/latent-spaces/brag) [Source 3](https://latent-spaces.github.io/brag/)

- **Code:** MIT
- **Weights:** MIT skill code. Agent/model/renderer terms and bundled music/SFX rights remain separate; credit alone is not proof of every downstream use right.
- **Commercial:** The reviewed MIT software license permits commercial use subject to its license, notice and source-sharing obligations where applicable. This does not establish permission for every model, input, output or service.
- **Cost:** Skill is free; agent inference and the optional hosted letsbrag service can cost separately.

### Why it merits attention

The output bundle includes a plan, composition brief, rendered video and share copy, which fits a reviewable creator workflow. [Source 1](https://github.com/latent-spaces/brag) [Source 2](https://latent-spaces.github.io/brag/)

### Limitations

A polished launch clip is not a benchmark or proof that the demonstrated app was exercised correctly. Verify every capability claim and asset right before publication. This edition is a documentation review, not an installation or output-quality test. [Source 1](https://github.com/latent-spaces/brag) [Source 2](https://latent-spaces.github.io/brag/)

### Get the tool

- [Repository](https://github.com/latent-spaces/brag)
- [License](https://github.com/latent-spaces/brag/blob/main/LICENSE)
- [Documentation](https://latent-spaces.github.io/brag/)

## AntV Infographic

Data art & scientific visualization · Vector graphics, illustration & textures · Creative publishing & presentation · Creative learning & authoring

First detailed guide in this library. This is a documentation baseline, not a claim that the project launched today.

### How it uses AI

A declarative SVG infographic engine with supplied AI-agent skills for turning descriptions into editable visual compositions. Creative use: Creating explainers, process diagrams and structured infographic layouts with a text-to-design workflow. [Source](https://github.com/antvis/Infographic) [Source](https://infographic.antv.vision/) [Source](https://infographic.antv.vision/learn/getting-started)

### Introduction

A declarative SVG infographic engine with supplied AI-agent skills for turning descriptions into editable visual compositions. [Source 1](https://github.com/antvis/Infographic) [Source 2](https://infographic.antv.vision/) [Source 3](https://infographic.antv.vision/learn/getting-started)

### What it is good for

Creating explainers, process diagrams and structured infographic layouts with a text-to-design workflow. [Source 1](https://github.com/antvis/Infographic) [Source 2](https://infographic.antv.vision/) [Source 3](https://infographic.antv.vision/learn/getting-started)

### Demo & examples

The official site has an AI generator and gallery; the documentation illustrates editable layouts and streaming generation. [Source 1](https://github.com/antvis/Infographic) [Source 2](https://infographic.antv.vision/) [Source 3](https://infographic.antv.vision/learn/getting-started)

### Install

Follow the reviewed project route below; these steps are documentation guidance and were not executed. [Source 1](https://github.com/antvis/Infographic) [Source 2](https://infographic.antv.vision/) [Source 3](https://infographic.antv.vision/learn/getting-started)

1. Add @antv/infographic to a JavaScript project with npm.
2. Create a page container and initialize Infographic with editable enabled.
3. For the AI workflow, install the appropriate official creator/syntax skill in a supported agent and connect the chosen model separately.

```sh
npm install @antv/infographic
```

### First project

A small first project that exercises the documented creative workflow. [Source 1](https://github.com/antvis/Infographic) [Source 2](https://infographic.antv.vision/) [Source 3](https://infographic.antv.vision/learn/getting-started)

1. Provide a small set of verified facts and ask the agent for a suitable infographic syntax/template.
2. Render, then revise labels, hierarchy, color and spacing in the editable view.
3. Export or incorporate the SVG after checking readability and data accuracy.
### Hardware & software

Requirements are source-specific. Unreported capacities and untested platforms are not inferred. [Source 1](https://github.com/antvis/Infographic) [Source 2](https://infographic.antv.vision/) [Source 3](https://infographic.antv.vision/learn/getting-started)

- **Hardware:** No numeric RAM, VRAM, CPU or disk minimum is documented; a browser renders the infographic. A local LLM, if chosen, has separate needs.
- **Software:** JavaScript/npm project and browser; no specific Node minimum is stated in the reviewed quick start. AI authoring requires an external agent/model.
- **Platforms:** Browser-focused library; host/OS support follows the chosen development and agent stack, not a published native-app matrix.

### License, model weights & costs

The complete software license was archived and reviewed. Keep software, model weights, dependencies and hosted-service terms separate. [Source 1](https://github.com/antvis/Infographic/blob/main/LICENSE) [Source 2](https://github.com/antvis/Infographic) [Source 3](https://infographic.antv.vision/) [Source 4](https://infographic.antv.vision/learn/getting-started)

- **Code:** MIT
- **Weights:** MIT engine and skills. Fonts, icons, input data and model/provider terms remain separate.
- **Commercial:** The reviewed MIT software license permits commercial use subject to its license, notice and source-sharing obligations where applicable. This does not establish permission for every model, input, output or service.
- **Cost:** No library fee; chosen AI services and hosting may cost separately.

### Why it merits attention

Structured syntax, editable output and SVG rendering make iteration and inspection easier than a flat generated image. [Source 1](https://github.com/antvis/Infographic) [Source 2](https://infographic.antv.vision/) [Source 3](https://infographic.antv.vision/learn/getting-started)

### Limitations

The renderer itself is deterministic; the supplied agent integration is the AI component. Template counts and marketing quality claims are not independent evaluation. This edition is a documentation review, not an installation or output-quality test. [Source 1](https://github.com/antvis/Infographic) [Source 2](https://infographic.antv.vision/) [Source 3](https://infographic.antv.vision/learn/getting-started)

### Get the tool

- [Repository](https://github.com/antvis/Infographic)
- [License](https://github.com/antvis/Infographic/blob/main/LICENSE)
- [Documentation](https://infographic.antv.vision/)

## LocalAI

Images & design · Audio, music & voice · Video, animation & film · Browser tools & web media · Emerging & cross-disciplinary creative AI

First detailed guide in this library. This is a documentation baseline, not a claim that the project launched today.

### How it uses AI

A local model-serving platform with concrete image-generation, speech and other media backends exposed through a browser UI and APIs. Creative use: Building a reusable local service for image experiments, narration or media applications that need a stable inference interface. [Source](https://github.com/mudler/LocalAI) [Source](https://localai.io/) [Source](https://localai.io/docs/features/image-generation/) [Source](https://localai.io/docs/features/text-to-audio/)

### Introduction

A local model-serving platform with concrete image-generation, speech and other media backends exposed through a browser UI and APIs. [Source 1](https://github.com/mudler/LocalAI) [Source 2](https://localai.io/) [Source 3](https://localai.io/docs/features/image-generation/) [Source 4](https://localai.io/docs/features/text-to-audio/)

### What it is good for

Building a reusable local service for image experiments, narration or media applications that need a stable inference interface. [Source 1](https://github.com/mudler/LocalAI) [Source 2](https://localai.io/) [Source 3](https://localai.io/docs/features/image-generation/) [Source 4](https://localai.io/docs/features/text-to-audio/)

### Demo & examples

The official image and TTS documentation contains executable client examples and configuration recipes; no backend was installed or benchmarked here. [Source 1](https://github.com/mudler/LocalAI) [Source 2](https://localai.io/) [Source 3](https://localai.io/docs/features/image-generation/) [Source 4](https://localai.io/docs/features/text-to-audio/)

### Install

Follow the reviewed project route below; these steps are documentation guidance and were not executed. [Source 1](https://github.com/mudler/LocalAI) [Source 2](https://localai.io/) [Source 3](https://localai.io/docs/features/image-generation/) [Source 4](https://localai.io/docs/features/text-to-audio/)

1. Choose the official container/binary route that matches your hardware and required backend.
2. Start the service with persistent model/data storage following the setup guide.
3. Install a gallery model and inspect its license, model files and backend requirements before using the corresponding media endpoint.
### First project

A small first project that exercises the documented creative workflow. [Source 1](https://github.com/mudler/LocalAI) [Source 2](https://localai.io/) [Source 3](https://localai.io/docs/features/image-generation/) [Source 4](https://localai.io/docs/features/text-to-audio/)

1. Begin with one small, supported image or speech model.
2. Generate a single image through /v1/images/generations or a speech sample through the TTS UI/API.
3. Record model/settings and inspect output before integrating the service into a larger creative workflow.
### Hardware & software

Requirements are source-specific. Unreported capacities and untested platforms are not inferred. [Source 1](https://github.com/mudler/LocalAI) [Source 2](https://localai.io/) [Source 3](https://localai.io/docs/features/image-generation/) [Source 4](https://localai.io/docs/features/text-to-audio/)

- **Hardware:** Some image and speech backends run on CPU, while others need a supported GPU. There is no universal RAM/VRAM/disk requirement across all models. The image guide documents tiling/offloading and warns that high-resolution VAE decoding can require large buffers.
- **Software:** Docker or a supported native build, selected backend/runtime and downloaded model assets. GPU containers require the corresponding driver/runtime.
- **Platforms:** CPU and hardware-specific NVIDIA/AMD/Intel/Vulkan routes are documented, with separate Apple/Metal/MLX paths. Backend support varies; do not assume every model works on every platform.

### License, model weights & costs

The complete software license was archived and reviewed. Keep software, model weights, dependencies and hosted-service terms separate. [Source 1](https://github.com/mudler/LocalAI/blob/master/LICENSE) [Source 2](https://github.com/mudler/LocalAI) [Source 3](https://localai.io/) [Source 4](https://localai.io/docs/features/image-generation/) [Source 5](https://localai.io/docs/features/text-to-audio/)

- **Code:** MIT
- **Weights:** MIT serving software. Each model/backend retains its own license: inclusion in the gallery does not establish unrestricted commercial use.
- **Commercial:** The reviewed MIT software license permits commercial use subject to its license, notice and source-sharing obligations where applicable. This does not establish permission for every model, input, output or service.
- **Cost:** No compulsory hosted API subscription for local models; hardware, storage, electricity and optional remote services are separate.

### Why it merits attention

Specific media endpoints and backend configuration make it useful infrastructure for repeatable creator tools. [Source 1](https://github.com/mudler/LocalAI) [Source 2](https://localai.io/) [Source 3](https://localai.io/docs/features/image-generation/) [Source 4](https://localai.io/docs/features/text-to-audio/)

### Limitations

A model-serving platform is not a finished editor. CPU capability does not promise useful speed for large video/diffusion models, and some upscaling configurations fall back to ordinary resizing rather than AI. This edition is a documentation review, not an installation or output-quality test. [Source 1](https://github.com/mudler/LocalAI) [Source 2](https://localai.io/) [Source 3](https://localai.io/docs/features/image-generation/) [Source 4](https://localai.io/docs/features/text-to-audio/)

### Get the tool

- [Repository](https://github.com/mudler/LocalAI)
- [License](https://github.com/mudler/LocalAI/blob/master/LICENSE)
- [Documentation](https://localai.io/)

## YuE2

Audio, music & voice · Computational art & creative coding · AI agents for code-authored media production · Performance, projection & stage media

First detailed guide in this library. This is a documentation baseline, not a claim that the project launched today.

### How it uses AI

A music-generation system that creates an editable melody/chord score before synthesizing a full song, with related cover and score-editing workflows. Creative use: Comparing arrangements, developing original song ideas and experimenting with score-controlled instrumental or vocal music. [Source](https://github.com/multimodal-art-projection/YuE) [Source](https://map-yue2.github.io/) [Source](https://github.com/multimodal-art-projection/YuE/blob/main/MODEL_LICENSE) [Source](https://github.com/multimodal-art-projection/YuE/releases/tag/yue2-music-v1.2.0)

### Introduction

A music-generation system that creates an editable melody/chord score before synthesizing a full song, with related cover and score-editing workflows. [Source 1](https://github.com/multimodal-art-projection/YuE) [Source 2](https://map-yue2.github.io/) [Source 3](https://github.com/multimodal-art-projection/YuE/blob/main/MODEL_LICENSE) [Source 4](https://github.com/multimodal-art-projection/YuE/releases/tag/yue2-music-v1.2.0)

### What it is good for

Comparing arrangements, developing original song ideas and experimenting with score-controlled instrumental or vocal music. [Source 1](https://github.com/multimodal-art-projection/YuE) [Source 2](https://map-yue2.github.io/) [Source 3](https://github.com/multimodal-art-projection/YuE/blob/main/MODEL_LICENSE) [Source 4](https://github.com/multimodal-art-projection/YuE/releases/tag/yue2-music-v1.2.0)

### Demo & examples

The official demo site pairs songs with symbolic scores and shows editing/cover examples. Its comparative rankings use a particular benchmark and different selection budgets, not a universal quality verdict. [Source 1](https://github.com/multimodal-art-projection/YuE) [Source 2](https://map-yue2.github.io/) [Source 3](https://github.com/multimodal-art-projection/YuE/blob/main/MODEL_LICENSE) [Source 4](https://github.com/multimodal-art-projection/YuE/releases/tag/yue2-music-v1.2.0)

### Install

Follow the reviewed project route below; these steps are documentation guidance and were not executed. [Source 1](https://github.com/multimodal-art-projection/YuE) [Source 2](https://map-yue2.github.io/) [Source 3](https://github.com/multimodal-art-projection/YuE/blob/main/MODEL_LICENSE) [Source 4](https://github.com/multimodal-art-projection/YuE/releases/tag/yue2-music-v1.2.0)

1. Use the documented Linux/Python 3.12 environment on a suitable NVIDIA GPU.
2. Clone the official YuE repository, create a virtual environment and install the local package.
3. Run the supplied generation example; first use downloads the required model files. Review model terms first.

```sh
python -m pip install .
```


```sh
python examples/generate.py --output outputs/first-song
```

### First project

A small first project that exercises the documented creative workflow. [Source 1](https://github.com/multimodal-art-projection/YuE) [Source 2](https://map-yue2.github.io/) [Source 3](https://github.com/multimodal-art-projection/YuE/blob/main/MODEL_LICENSE) [Source 4](https://github.com/multimodal-art-projection/YuE/releases/tag/yue2-music-v1.2.0)

1. Create a short original lyric/style request and generate its score and audio.
2. Inspect audio.flac and the retained score/settings, then edit the ABC score if needed.
3. Render a second version and listen for musical fidelity, unwanted vocals, clipping and truncation.
### Hardware & software

Requirements are source-specific. Unreported capacities and untested platforms are not inferred. [Source 1](https://github.com/multimodal-art-projection/YuE) [Source 2](https://map-yue2.github.io/) [Source 3](https://github.com/multimodal-art-projection/YuE/blob/main/MODEL_LICENSE) [Source 4](https://github.com/multimodal-art-projection/YuE/releases/tag/yue2-music-v1.2.0)

- **Hardware:** The quick start specifies a BF16-capable NVIDIA GPU with 24 GB VRAM. Host RAM and total disk minimum are not stated; model/artifact storage is additional.
- **Software:** Linux, Python 3.12, compatible NVIDIA inference stack and downloaded checkpoints. SheetSage2 transcription uses a separate environment when making covers from audio.
- **Platforms:** The official local quick start is Linux/NVIDIA. A hosted browser demo and separate ComfyUI integration exist; native macOS/Windows support is not established by this guide.

### License, model weights & costs

The complete software license was archived and reviewed. Keep software, model weights, dependencies and hosted-service terms separate. [Source 1](https://github.com/multimodal-art-projection/YuE/blob/main/LICENSE) [Source 2](https://github.com/multimodal-art-projection/YuE) [Source 3](https://map-yue2.github.io/) [Source 4](https://github.com/multimodal-art-projection/YuE/blob/main/MODEL_LICENSE) [Source 5](https://github.com/multimodal-art-projection/YuE/releases/tag/yue2-music-v1.2.0)

- **Code:** Apache-2.0
- **Weights:** Apache-2.0 source/skill/documentation; model weights use CC-BY-NC 4.0 with an additional individual-creator permission for monetized outputs under stated conditions. Companies need separate commercial-weight permission. This is not an unrestricted open-source weight license.
- **Commercial:** The reviewed Apache-2.0 software license permits commercial use subject to its license, notice and source-sharing obligations where applicable. This does not establish permission for every model, input, output or service.
- **Cost:** No code fee; GPU compute/storage and optional agent services are separate. The individual permission does not cover commercial resale of weights or third-party music rights.

### Why it merits attention

Retained score, intermediate artifacts and model identities support inspectable musical iteration. [Source 1](https://github.com/multimodal-art-projection/YuE) [Source 2](https://map-yue2.github.io/) [Source 3](https://github.com/multimodal-art-projection/YuE/blob/main/MODEL_LICENSE) [Source 4](https://github.com/multimodal-art-projection/YuE/releases/tag/yue2-music-v1.2.0)

### Limitations

Editing produces an entirely new recording rather than preserving untouched waveform segments. Best-of-eight benchmark selection differs from ordinary generation. The September skill update and October 2 transcription report are dated context, not claims of a new release today. This edition is a documentation review, not an installation or output-quality test. [Source 1](https://github.com/multimodal-art-projection/YuE) [Source 2](https://map-yue2.github.io/) [Source 3](https://github.com/multimodal-art-projection/YuE/blob/main/MODEL_LICENSE) [Source 4](https://github.com/multimodal-art-projection/YuE/releases/tag/yue2-music-v1.2.0)

### Get the tool

- [Repository](https://github.com/multimodal-art-projection/YuE)
- [License](https://github.com/multimodal-art-projection/YuE/blob/main/LICENSE)
- [Documentation](https://map-yue2.github.io/)

## Wonder3D

3D, reconstruction & assets · Games & production pipelines · 3D printing & generative CAD · Photogrammetry, scanning & neural rendering

First detailed guide, completing an earlier screened lead. This is a documentation baseline, not a claim that the project launched today.

### How it uses AI

A cross-domain diffusion system that predicts multiple color/normal views from one image, then reconstructs a textured mesh. Creative use: Exploring a 2D concept as a game prop or 3D study before manual retopology and material work. [Source](https://github.com/xxlong0/Wonder3D) [Source](https://www.xxlong.site/Wonder3D/)

### Introduction

A cross-domain diffusion system that predicts multiple color/normal views from one image, then reconstructs a textured mesh. [Source 1](https://github.com/xxlong0/Wonder3D) [Source 2](https://www.xxlong.site/Wonder3D/)

### What it is good for

Exploring a 2D concept as a game prop or 3D study before manual retopology and material work. [Source 1](https://github.com/xxlong0/Wonder3D) [Source 2](https://www.xxlong.site/Wonder3D/)

### Demo & examples

The official project page shows asset, Houdini and printing examples; these examples do not prove arbitrary generated meshes are printable. [Source 1](https://github.com/xxlong0/Wonder3D) [Source 2](https://www.xxlong.site/Wonder3D/)

### Install

Follow the reviewed project route below; these steps are documentation guidance and were not executed. [Source 1](https://github.com/xxlong0/Wonder3D) [Source 2](https://www.xxlong.site/Wonder3D/)

1. Follow the Linux Conda/requirements and tiny-cuda-nn setup, or the dedicated main-windows branch instructions.
2. Download the official diffusion checkpoint and required masking model; prepare a centered input with clean foreground masking.
3. Use the reconstruction Gradio application or the separate multiview and mesh-extraction scripts.

```sh
python gradio_app_recon.py
```

### First project

A small first project that exercises the documented creative workflow. [Source 1](https://github.com/xxlong0/Wonder3D) [Source 2](https://www.xxlong.site/Wonder3D/)

1. Start with a clear front-facing object image with limited occlusion.
2. Generate the six color/normal views, inspect consistency, then reconstruct the mesh.
3. Check geometry, scale, texture and topology in a 3D editor before game or fabrication use.
### Hardware & software

Requirements are source-specific. Unreported capacities and untested platforms are not inferred. [Source 1](https://github.com/xxlong0/Wonder3D) [Source 2](https://www.xxlong.site/Wonder3D/)

- **Hardware:** The reviewed README does not publish numeric RAM, VRAM or storage minima. CUDA dependencies are part of the main route; NeuS is described as a slower, lower-memory reconstruction alternative.
- **Software:** Conda/Python, PyTorch, CUDA components and model downloads. The example was tested on diffusers 0.19.3 and warns about newer-version conflicts; no universal Python minimum is given.
- **Platforms:** Linux setup, separate Windows branch and Docker documentation are provided. Native macOS support is not verified.

### License, model weights & costs

The complete software license was archived and reviewed. Keep software, model weights, dependencies and hosted-service terms separate. [Source 1](https://github.com/xxlong0/Wonder3D/blob/main/LICENSE) [Source 2](https://github.com/xxlong0/Wonder3D) [Source 3](https://www.xxlong.site/Wonder3D/)

- **Code:** MIT
- **Weights:** MIT source; diffusion checkpoints, SAM and borrowed components keep separate terms. Do not infer all-model permission from the repository license.
- **Commercial:** The reviewed MIT software license permits commercial use subject to its license, notice and source-sharing obligations where applicable. This does not establish permission for every model, input, output or service.
- **Cost:** No source fee; GPU compute/storage and any chosen proprietary downstream tools are separate.

### Why it merits attention

Inspectable normal/color intermediates and alternative reconstruction methods are useful for understanding failure cases. [Source 1](https://github.com/xxlong0/Wonder3D) [Source 2](https://www.xxlong.site/Wonder3D/)

### Limitations

The documented baseline uses six 256×256 views and an orthographic assumption. Occlusion and camera distortion can harm geometry; exported meshes still need watertightness and fabrication checks. This is an older research baseline, not a new launch. This edition is a documentation review, not an installation or output-quality test. [Source 1](https://github.com/xxlong0/Wonder3D) [Source 2](https://www.xxlong.site/Wonder3D/)

### Get the tool

- [Repository](https://github.com/xxlong0/Wonder3D)
- [License](https://github.com/xxlong0/Wonder3D/blob/main/LICENSE)
- [Documentation](https://www.xxlong.site/Wonder3D/)

## Spirula Studio

Photogrammetry, scanning & neural rendering · 3D, reconstruction & assets · Spatial audio & volumetric media · WebXR, VR & AR · 3D printing & generative CAD

First detailed guide in this library. This is a documentation baseline, not a claim that the project launched today.

### How it uses AI

A desktop reconstruction application that trains Gaussian scene representations from photographs or video, with learned masking and feature matching, editing, and textured-mesh export. Creative use: Capturing objects, exhibition spaces and locations for interactive scenes or visual studies, then inspecting and editing the learned reconstruction. [Source](https://github.com/harry7557558/spirula-studio) [Source](https://github.com/harry7557558/spirula-studio/releases/)

### Introduction

A desktop reconstruction application that trains Gaussian scene representations from photographs or video, with learned masking and feature matching, editing, and textured-mesh export. [Source 1](https://github.com/harry7557558/spirula-studio) [Source 2](https://github.com/harry7557558/spirula-studio/releases/)

### What it is good for

Capturing objects, exhibition spaces and locations for interactive scenes or visual studies, then inspecting and editing the learned reconstruction. [Source 1](https://github.com/harry7557558/spirula-studio) [Source 2](https://github.com/harry7557558/spirula-studio/releases/)

### Demo & examples

The README includes capture/render examples and links a browser viewer and gallery. The main website could not be opened by the research browser today; no reconstruction or viewer interaction was tested. [Source 1](https://github.com/harry7557558/spirula-studio) [Source 2](https://github.com/harry7557558/spirula-studio/releases/)

### Install

Follow the reviewed project route below; these steps are documentation guidance and were not executed. [Source 1](https://github.com/harry7557558/spirula-studio) [Source 2](https://github.com/harry7557558/spirula-studio/releases/)

1. Choose the official Windows, Linux or Apple Silicon release archive, extract it and open the GUI.
2. Create a small project from overlapping photographs or a short orbit video. Download an optional masking checkpoint only after reviewing its terms.
3. For source builds follow the documented Vulkan/CMake/Ninja route; CUDA is a separate Windows/Linux alternative.
### First project

A small first project that exercises the documented creative workflow. [Source 1](https://github.com/harry7557558/spirula-studio) [Source 2](https://github.com/harry7557558/spirula-studio/releases/)

1. Inspect the recovered cameras, masks and reconstruction coverage before training.
2. Train a small scene, inspect floaters and missing surfaces, then use the edit/render controls.
3. Export a scene or textured mesh and check geometry, scale and holes in a downstream editor; mesh export is not proof of printability.
### Hardware & software

Requirements are source-specific. Unreported capacities and untested platforms are not inferred. [Source 1](https://github.com/harry7557558/spirula-studio) [Source 2](https://github.com/harry7557558/spirula-studio/releases/)

- **Hardware:** The developer reports training 10 million full-SH Gaussians in 8 GB VRAM; this is a workload claim, not a universal minimum. Host RAM, minimum GPU memory, total disk space and minimum OS versions are not stated in the reviewed overview.
- **Software:** The packaged application avoids a separate Python/PyTorch or COLMAP installation. Source builds use a C++ build toolchain and Vulkan; macOS uses MoltenVK. Optional AI masking downloads models on first use.
- **Platforms:** Windows, Linux and macOS/Apple Silicon releases are documented. Vulkan supports NVIDIA, AMD, Intel and Apple GPUs; actual support depends on the driver and machine. CUDA is documented for Windows/Linux only.

### License, model weights & costs

The complete software license was archived and reviewed. Keep software, model weights, dependencies and hosted-service terms separate. [Source 1](https://github.com/harry7557558/spirula-studio/blob/master/LICENSE) [Source 2](https://github.com/harry7557558/spirula-studio) [Source 3](https://github.com/harry7557558/spirula-studio/releases/)

- **Code:** GPL-3.0
- **Weights:** GPL-3.0 software. Optional SAM 2.1 masks use Apache-2.0 checkpoints; SAM 3 uses separate non-standard Meta terms. Datasets retain their licenses. The optional GPU video-decoding build flags have codec patent considerations.
- **Commercial:** The reviewed GPL-3.0 software license permits commercial use subject to its license, notice and source-sharing obligations where applicable. This does not establish permission for every model, input, output or service.
- **Cost:** No application license fee; local GPU compute, storage and any external assets are separate.

### Why it merits attention

A packaged workflow and documented cross-vendor path make this a useful candidate for creators without an NVIDIA-only setup. Editable masks, cameras, meshes and renders make problems inspectable. [Source 1](https://github.com/harry7557558/spirula-studio) [Source 2](https://github.com/harry7557558/spirula-studio/releases/)

### Limitations

September release notes describe editing/rendering, scale recovery and macOS support; this is the library baseline, not a claim of an October 4 launch. Difficult captures can still fail, and marketing speed/quality claims were not independently reproduced. This edition is a documentation review, not an installation or output-quality test. [Source 1](https://github.com/harry7557558/spirula-studio) [Source 2](https://github.com/harry7557558/spirula-studio/releases/)

### Get the tool

- [Repository](https://github.com/harry7557558/spirula-studio)
- [License](https://github.com/harry7557558/spirula-studio/blob/master/LICENSE)
- [Documentation](https://github.com/harry7557558/spirula-studio/releases/)

## LocalText2Voice

Audio, music & voice · Video, animation & film · Creative publishing & presentation · Accessible media & assistive creation · Storyboarding, narrative & comics

First detailed guide in this library. This is a documentation baseline, not a claim that the project launched today.

### How it uses AI

A desktop application for segmented AI narration, audiobooks, podcasts and an editable audio-to-video storyboard workflow. Creative use: Producing long-form narration with corrections at segment level, timed subtitles, a music mix and optional scene-by-scene generated visuals. [Source](https://github.com/estebanstifli/LocalText2Voice) [Source](https://github.com/estebanstifli/LocalText2Voice/releases/tag/v2.2.0)

### Introduction

A desktop application for segmented AI narration, audiobooks, podcasts and an editable audio-to-video storyboard workflow. [Source 1](https://github.com/estebanstifli/LocalText2Voice) [Source 2](https://github.com/estebanstifli/LocalText2Voice/releases/tag/v2.2.0)

### What it is good for

Producing long-form narration with corrections at segment level, timed subtitles, a music mix and optional scene-by-scene generated visuals. [Source 1](https://github.com/estebanstifli/LocalText2Voice) [Source 2](https://github.com/estebanstifli/LocalText2Voice/releases/tag/v2.2.0)

### Demo & examples

The README links author-made documentary and animated-story tutorials. They illustrate the intended workflow; this review did not listen to or reproduce a full production. [Source 1](https://github.com/estebanstifli/LocalText2Voice) [Source 2](https://github.com/estebanstifli/LocalText2Voice/releases/tag/v2.2.0)

### Install

Follow the reviewed project route below; these steps are documentation guidance and were not executed. [Source 1](https://github.com/estebanstifli/LocalText2Voice) [Source 2](https://github.com/estebanstifli/LocalText2Voice/releases/tag/v2.2.0)

1. Windows 10/11 users can download LocalText2Voice-Setup.exe from the official release and choose a storage folder and CPU-light or GPU profile.
2. In Settings > TTS Engines, select an engine and review its model license; download a suitable voice.
3. Linux users need Python 3.10+, virtual-environment support, Git and FFmpeg, then follow the documented source launcher; macOS is not officially supported.
### First project

A small first project that exercises the documented creative workflow. [Source 1](https://github.com/estebanstifli/LocalText2Voice) [Source 2](https://github.com/estebanstifli/LocalText2Voice/releases/tag/v2.2.0)

1. Import a short TXT/Markdown/DOCX/EPUB passage, select a voice and generate a few segments.
2. Listen and correct pronunciation or timing; optionally run Whisper review, regenerate selected segments and approve them.
3. Export audio/subtitles, or continue into the beta Video Storyboard to add scenes, review continuity and render MP4.
### Hardware & software

Requirements are source-specific. Unreported capacities and untested platforms are not inferred. [Source 1](https://github.com/estebanstifli/LocalText2Voice) [Source 2](https://github.com/estebanstifli/LocalText2Voice/releases/tag/v2.2.0)

- **Hardware:** Developer guidance: basic 4-core 64-bit CPU, 8 GB RAM and 5 GB free disk; recommended 6 cores, 16 GB RAM, 20–30 GB SSD space and NVIDIA 8 GB VRAM; larger workflows 32 GB RAM/50+ GB disk/12+ GB VRAM. These are guidance profiles, not guarantees for every engine. Assets and exports need additional storage.
- **Software:** Packaged Windows installer; Linux source requires Python 3.10+, FFmpeg and desktop dependencies. Optional engines download their own models and isolated runtimes. GPU acceleration primarily targets NVIDIA CUDA.
- **Platforms:** Windows 10/11 64-bit is the packaged route. Linux 64-bit is source-based, with Arch/CachyOS KDE/Wayland documented as tested upstream. macOS is explicitly untested and unsupported.

### License, model weights & costs

The complete software license was archived and reviewed. Keep software, model weights, dependencies and hosted-service terms separate. [Source 1](https://github.com/estebanstifli/LocalText2Voice/blob/main/LICENSE) [Source 2](https://github.com/estebanstifli/LocalText2Voice) [Source 3](https://github.com/estebanstifli/LocalText2Voice/releases/tag/v2.2.0)

- **Code:** MIT
- **Weights:** MIT application, with separate engine/model/voice and FFmpeg/Qt terms. OmniVoice and F5-TTS Russian weights are non-commercial. IndexTTS-2.5 has its own conditional Bilibili model license; do not treat MIT as permission for all output workflows.
- **Commercial:** The reviewed MIT software license permits commercial use subject to its license, notice and source-sharing obligations where applicable. This does not establish permission for every model, input, output or service.
- **Cost:** Local software is free to run; models, GPU/storage and optional cloud providers are separate. No cloud account is needed for the supported local narration route.

### Why it merits attention

Segment review, regeneration and retained project data give creators more control than a single opaque generation. The v2.2.0 release was published October 4 UTC (October 3 Eastern) and documents voice-cloning/emotion controls. [Source 1](https://github.com/estebanstifli/LocalText2Voice) [Source 2](https://github.com/estebanstifli/LocalText2Voice/releases/tag/v2.2.0)

### Limitations

Video Storyboard remains beta and needs continuity/timing review. Local engine fallback can be slow; optional cloud modes send content to providers. Early Windows builds may be unsigned. The new release is described in a first-library profile, without claiming it was installed. This edition is a documentation review, not an installation or output-quality test. [Source 1](https://github.com/estebanstifli/LocalText2Voice) [Source 2](https://github.com/estebanstifli/LocalText2Voice/releases/tag/v2.2.0)

### Get the tool

- [Repository](https://github.com/estebanstifli/LocalText2Voice)
- [License](https://github.com/estebanstifli/LocalText2Voice/blob/main/LICENSE)
- [Documentation](https://github.com/estebanstifli/LocalText2Voice/releases/tag/v2.2.0)

## Shodō — Ink & Gesture

Typography, fonts & layout · Vector graphics, illustration & textures · Images & design · Computational art & creative coding

First detailed guide in this library. The repository was created in the current discovery window; this is a documentation baseline, not a verified launch date.

### How it uses AI

An experimental calligraphy workbench where an AI proposes ordered brush gestures, an SVG renderer paints them and the user edits each stroke. Vision can critique selected characters against a reference. Creative use: Making editable calligraphic studies and expressive lettering, then refining paths, pressure, brush texture and multi-character composition before SVG or PNG export. [Source](https://github.com/hayden1126/shodo) [Source](https://github.com/hayden1126/shodo/blob/main/THIRD_PARTY.md)

### Introduction

An experimental calligraphy workbench where an AI proposes ordered brush gestures, an SVG renderer paints them and the user edits each stroke. Vision can critique selected characters against a reference. [Source 1](https://github.com/hayden1126/shodo) [Source 2](https://github.com/hayden1126/shodo/blob/main/THIRD_PARTY.md)

### What it is good for

Making editable calligraphic studies and expressive lettering, then refining paths, pressure, brush texture and multi-character composition before SVG or PNG export. [Source 1](https://github.com/hayden1126/shodo) [Source 2](https://github.com/hayden1126/shodo/blob/main/THIRD_PARTY.md)

### Demo & examples

Recorded AI studies for 愛 and 森羅万象 are included and can be edited without a new API request. The hosted prototype is private, and the repository contains a demo script rather than a finished demo video. [Source 1](https://github.com/hayden1126/shodo) [Source 2](https://github.com/hayden1126/shodo/blob/main/THIRD_PARTY.md)

### Install

Follow the reviewed project route below; these steps are documentation guidance and were not executed. [Source 1](https://github.com/hayden1126/shodo) [Source 2](https://github.com/hayden1126/shodo/blob/main/THIRD_PARTY.md)

1. Install Node.js 22.13+ and npm, clone the official repository and install its locked dependencies with npm ci.
2. Start the local development server with npm run dev and open localhost:5180.
3. For new AI generation, copy the example environment file to the ignored local environment file and configure the provider key. Prepared/recorded studies work without a key.

```sh
npm ci
```


```sh
npm run dev
```

### First project

A small first project that exercises the documented creative workflow. [Source 1](https://github.com/hayden1126/shodo) [Source 2](https://github.com/hayden1126/shodo/blob/main/THIRD_PARTY.md)

1. Open a recorded study, select a stroke and change a curve handle or pressure point.
2. For a new work, enter a short phrase and inspect character identity/order before accepting an optional critique.
3. Arrange the composition and export SVG/PNG plus Study JSON to preserve editable paths and brush settings.
### Hardware & software

Requirements are source-specific. Unreported capacities and untested platforms are not inferred. [Source 1](https://github.com/hayden1126/shodo) [Source 2](https://github.com/hayden1126/shodo/blob/main/THIRD_PARTY.md)

- **Hardware:** Minimum RAM, GPU/VRAM and disk capacities are not documented. Generation uses a remote AI provider; this does not establish a universal minimum for the local browser/server.
- **Software:** Node.js 22.13+, npm and a desktop browser. Windows ARM64 needs x64 Node for the documented Worker runtime. New generations require network access and a configured provider account.
- **Platforms:** Desktop-oriented web application; Windows ARM64 setup is described. General macOS/Linux compatibility and mobile support were not independently established from the reviewed documentation.

### License, model weights & costs

The complete software license was archived and reviewed. Keep software, model weights, dependencies and hosted-service terms separate. [Source 1](https://github.com/hayden1126/shodo/blob/main/LICENSE) [Source 2](https://github.com/hayden1126/shodo) [Source 3](https://github.com/hayden1126/shodo/blob/main/THIRD_PARTY.md)

- **Code:** MIT
- **Weights:** MIT application with retained scaffold/dependency notices. The bundled Yuji Syuku font uses SIL OFL 1.1; uploaded reference images and provider terms remain separate.
- **Commercial:** The reviewed MIT software license permits commercial use subject to its license, notice and source-sharing obligations where applicable. This does not establish permission for every model, input, output or service.
- **Cost:** Recorded studies and editing need no model account. New generation and vision critique may incur provider charges.

### Why it merits attention

The output is editable vector geometry, and the documentation distinguishes generated studies from deterministic prepared paths and acknowledges character/style limits. [Source 1](https://github.com/hayden1126/shodo) [Source 2](https://github.com/hayden1126/shodo/blob/main/THIRD_PARTY.md)

### Limitations

Hackathon prototype: approximate procedural brush rendering, subjective AI critiques, no guaranteed stroke-order correctness, and no typographic kerning for Latin text. Uploaded visual references are sent with generation; no external artwork was submitted in this review. This edition is a documentation review, not an installation or output-quality test. [Source 1](https://github.com/hayden1126/shodo) [Source 2](https://github.com/hayden1126/shodo/blob/main/THIRD_PARTY.md)

### Get the tool

- [Repository](https://github.com/hayden1126/shodo)
- [License](https://github.com/hayden1126/shodo/blob/main/LICENSE)
- [Documentation](https://github.com/hayden1126/shodo/blob/main/THIRD_PARTY.md)

## Additional open-source AI discoveries

Creative AI relevance and software license screened. Full installation, requirements and quality profiles are pending.

### MotionMind · MIT

Translating captured body movement into avatar animation and an interactive movement-coaching study.
The documented pipeline combines learned pose/body estimation, motion retargeting and LLM/vision interpretation.
MIT applies to the original application; the license appendix preserves third-party asset terms. SMPL/body models, checkpoints, avatars and hosted coaching providers have separate restrictions. Physical-accuracy claims and setup are not verified. Software license reviewed; full profile and hands-on output testing remain pending.

- [Official project documentation](https://github.com/rohitacharyams/MotionMind)
- [Complete reviewed software license](https://github.com/rohitacharyams/MotionMind/blob/main/LICENSE)
### OpenMontage · AGPL-3.0

Organizing a brief, script, storyboard, generated assets and rendered video with a reviewable production plan.
AI agents plan and generate narration/visuals, then compose scenes using supported video renderers.
AGPL application; agent subscriptions, generation services, music and renderer terms remain separate. The Studio landing page also advertises a waitlist, so source availability is not proof of hosted access. Software license reviewed; full profile and hands-on output testing remain pending.

- [Official project documentation](https://github.com/calesthio/OpenMontage)
- [Complete reviewed software license](https://github.com/calesthio/OpenMontage/blob/main/LICENSE)
- [Official project documentation](https://www.openmontage.video/)
### Pixelle-Video · Apache-2.0

Producing short narrated videos from an AI-written script, generated visuals and TTS.
The workflow supports LLM scripting and model-generated image/video/audio assets, including local Ollama/ComfyUI integrations.
Apache software; provider/model terms and generation costs vary. The older project-site link failed during web research; install reliability and output quality remain pending. Software license reviewed; full profile and hands-on output testing remain pending.

- [Official project documentation](https://github.com/ATH-MaaS/Pixelle-Video)
- [Complete reviewed software license](https://github.com/ATH-MaaS/Pixelle-Video/blob/main/LICENSE)
### GSAP Skills · MIT

Helping an AI coding agent author kinetic text, SVG movement and scroll-linked web animation.
The skill package supplies animation-specific instructions and examples to an external AI agent that writes GSAP code.
MIT covers this skill package, not the separately licensed GSAP engine or agent service. This is an AI-authoring integration, not a standalone trained model. Software license reviewed; full profile and hands-on output testing remain pending.

- [Official project documentation](https://github.com/greensock/gsap-skills)
- [Complete reviewed software license](https://github.com/greensock/gsap-skills/blob/main/LICENSE)
### OpenCreator · Apache-2.0

Managing media projects with transcription, subtitles, translation and generated assets in a creator workspace.
A connected AI agent orchestrates media-specific tools and generation providers.
Apache application. Agent runtime, optional cloud APIs and model licenses are separate; local storage does not mean all computation stays offline. Software license reviewed; full profile and hands-on output testing remain pending.

- [Official project documentation](https://github.com/krillinai/OpenCreator)
- [Complete reviewed software license](https://github.com/krillinai/OpenCreator/blob/master/LICENSE)
### ViMax · MIT

Turning a narrative brief into character descriptions, storyboards and assembled video shots.
A multi-agent pipeline coordinates script planning, image references and model-based video generation.
MIT framework; provider accounts, model terms and generated-character consistency need further review. Treat it as an experimental production pipeline. Software license reviewed; full profile and hands-on output testing remain pending.

- [Official project documentation](https://github.com/HKUDS/ViMax)
- [Complete reviewed software license](https://github.com/HKUDS/ViMax/blob/main/LICENSE)
### Presenton · Apache-2.0

Creating editable presentation drafts from text or source documents, with PPTX/PDF export.
LLMs generate slide structure and content; local Ollama or hosted models can supply inference.
Apache application. Generated text/layout need review, and image providers, fonts, model terms and exact platform resource needs vary. Software license reviewed; full profile and hands-on output testing remain pending.

- [Official project documentation](https://github.com/presenton/presenton)
- [Complete reviewed software license](https://github.com/presenton/presenton/blob/main/LICENSE)
### SANA · Apache-2.0

Exploring efficient image generation and newer video-model experiments.
The project implements trained diffusion architectures and inference/training code for generated visual media.
Apache code; checkpoint terms and hardware differ by model. Image-model low-memory claims must not be transferred to every video model. Software license reviewed; full profile and hands-on output testing remain pending.

- [Official project documentation](https://github.com/NVlabs/Sana)
- [Complete reviewed software license](https://github.com/NVlabs/Sana/blob/main/LICENSE)
- [Official project documentation](https://nvlabs.github.io/Sana/docs/)
### X-AnyLabeling · GPL-3.0

Preparing and correcting labeled visual datasets for creative-media experiments.
AI-assisted detection, segmentation, OCR and pose models propose annotations for human review.
GPL application with Windows/macOS/Linux guidance. Each downloaded detector/segmenter has separate terms; accuracy and packaging still require a detailed profile. Software license reviewed; full profile and hands-on output testing remain pending.

- [Official project documentation](https://github.com/CVHub520/X-AnyLabeling)
- [Complete reviewed software license](https://github.com/CVHub520/X-AnyLabeling/blob/main/LICENSE)
### imaginAIry · MIT

Scriptable image generation, editing, restoration and controlled visual experiments.
The Python CLI integrates diffusion and learned image-processing models rather than only deterministic filters.
MIT code; model licenses differ. Documentation has older Python/version constraints, so current installation and compatibility need follow-up. Enhancement can invent detail. Software license reviewed; full profile and hands-on output testing remain pending.

- [Official project documentation](https://github.com/brycedrennan/imaginAIry)
- [Complete reviewed software license](https://github.com/brycedrennan/imaginAIry/blob/master/LICENSE)
- [Official project documentation](https://brycedrennan.github.io/imaginAIry/)
### FireRed-OpenStoryline · Apache-2.0

Conversational rough cuts, narration, beat-aware music selection and repeatable editing workflows.
LLM planning and media understanding choose and refine sequences; optional AI transitions generate new connecting footage.
Apache code; hosted inference and media rights are separate. The authors warn that generated transitions can be costly and unpredictable; not a tested quality endorsement. Software license reviewed; full profile and hands-on output testing remain pending.

- [Official project documentation](https://github.com/FireRedTeam/FireRed-OpenStoryline)
- [Complete reviewed software license](https://github.com/FireRedTeam/FireRed-OpenStoryline/blob/main/LICENSE)
### 3DGRUT · Apache-2.0

Reconstructing and rendering learned Gaussian scenes with distorted-camera support and secondary light effects.
Scene training and Neural Harmonic Textures learn appearance; the hybrid pipeline combines Gaussian rasterization and ray tracing.
Apache code. Ray-tracing paths need suitable hardware and are research-oriented; detailed dependency, data and resource review remains pending. Software license reviewed; full profile and hands-on output testing remain pending.

- [Official project documentation](https://github.com/nv-tlabs/3dgrut)
- [Complete reviewed software license](https://github.com/nv-tlabs/3dgrut/blob/main/LICENSE)
### JoyAI-Video-Edit · Apache-2.0

Instruction-guided edits to a live or uploaded video stream.
A multimodal condition encoder and autoregressive diffusion transformer generate edited frames causally.
Apache software; model/deployment terms need separate review. Published consumer-GPU examples use an RTX 5090 with 32 GB VRAM; real-time performance is not established for ordinary laptops. Software license reviewed; full profile and hands-on output testing remain pending.

- [Official project documentation](https://github.com/jd-opensource/JoyAI-Video-Edit)
- [Complete reviewed software license](https://github.com/jd-opensource/JoyAI-Video-Edit/blob/main/LICENSE)
### OOOSplat · Apache-2.0

Turning overlapping photos or orbit video into an editable local Gaussian scene.
The application orchestrates reconstruction and Brush-based optimization of a learned Gaussian representation, then previews and exports it.
Apache application with separately licensed FFmpeg/COLMAP/Brush. macOS Apple Silicon and Ubuntu builds are labeled Alpha; exact packaging and GPU compatibility need follow-up. Software license reviewed; full profile and hands-on output testing remain pending.

- [Official project documentation](https://github.com/ooolabdev/ooosplat)
- [Complete reviewed software license](https://github.com/ooolabdev/ooosplat/blob/main/LICENSE)
### GaussianGPT · MIT

Generating, completing or outpainting experimental 3D Gaussian environments.
A sparse VQ autoencoder and autoregressive transformer predict scene tokens, which decode into renderable Gaussian primitives.
MIT research code with released checkpoints. CUDA/source-compiled dependencies, dataset permissions and model reuse terms still need full profile review. Software license reviewed; full profile and hands-on output testing remain pending.

- [Official project documentation](https://github.com/nicolasvonluetzow/GaussianGPT)
- [Complete reviewed software license](https://github.com/nicolasvonluetzow/GaussianGPT/blob/main/LICENSE)
- [Official project documentation](https://nicolasvonluetzow.github.io/GaussianGPT/)
### Bambu Studio AI · MIT

Assisting with model search, generative figurines, measured CAD, mesh checks and preparation for Bambu Studio.
An external AI agent drives documented text/image-to-3D providers and Python preparation tools; deterministic CAD is separately identified.
MIT skill/tool code; copied Bambu profiles retain AGPL, and model-generation APIs have separate costs/terms. The documented flow leaves slicing and starting the printer to the user; printability has not been tested. Software license reviewed; full profile and hands-on output testing remain pending.

- [Official project documentation](https://github.com/heyixuan2/bambu-studio-ai)
- [Complete reviewed software license](https://github.com/heyixuan2/bambu-studio-ai/blob/main/LICENSE)
### Khmer Font Factory · MIT

Exploring few-shot Khmer glyph generation and browser-side vector/font compilation.
The README and released worker code load ONNX style encoders, an MXFont generator and refinement sessions, followed by vectorization.
MIT application. The linked hosted demo was inaccessible during research; checkpoint provenance/licensing, availability and actual glyph quality remain unresolved parts of a full profile. Software license reviewed; full profile and hands-on output testing remain pending.

- [Official project documentation](https://github.com/lienghongky/cxm-kff)
- [Complete reviewed software license](https://github.com/lienghongky/cxm-kff/blob/main/LICENSE)
- [Official project documentation](https://github.com/lienghongky/cxm-kff/blob/main/src/workers/pipeline.worker.js)
### Afford-Motion · MIT

Researching character movement that follows text while taking a 3D scene into account.
An affordance diffusion model predicts interaction regions and a second diffusion model generates human motion conditioned on them.
MIT research source; body models, datasets and checkpoints retain separate terms. Legacy Python/CUDA reproduction and animation export suitability need review. Software license reviewed; full profile and hands-on output testing remain pending.

- [Official project documentation](https://github.com/afford-motion/afford-motion)
- [Complete reviewed software license](https://github.com/afford-motion/afford-motion/blob/main/LICENSE)
### Velocut · MIT

Letting a creator and an AI agent edit the same timeline and 3D scene with inspectable history.
MCP tools expose scene creation, camera control and media edits to an external AI model; the editor does not secretly run a second local LLM.
MIT code with separate asset/dependency terms. The documented full editor requires Node 22.6+ and Chrome/Edge WebGPU/WebCodecs; Safari/Firefox are not supported for the full editor. Software license reviewed; full profile and hands-on output testing remain pending.

- [Official project documentation](https://github.com/open-ribbi/velocut)
- [Complete reviewed software license](https://github.com/open-ribbi/velocut/blob/main/LICENSE)

## Excluded and unresolved findings

Research notes only; these do not enter the eligible tool library.

- **Palmier current releases** · excluded: The inspected license keeps GPL coverage for the historical source through v0.7.6/last-gpl-source but says newer distributed releases are proprietary. Current releases do not qualify; the old tag was not separately profiled. [Source](https://github.com/palmier-io/palmier-pro)
- **OfficeCLI** · needs-license-review: The full file labeled Apache-2.0 changes clause 4(d) from the canonical notice wording. It is held for clarification instead of treating the SPDX label as a completed software review. [Source](https://github.com/iOfficeAI/OfficeCLI)
- **SewFormer** · needs-license-review: A primary research page and code repository exist, but the license endpoint returned 404 and no complete software grant was verified. [Source](https://sewformer.github.io/) [Source](https://github.com/sail-sg/sewformer)
- **Threadspool** · needs-license-review: An LLM-assisted embroidery workflow is described, but no complete repository software license was available. Embroidery import examples also do not prove stitch-out quality. [Source](https://github.com/alexandra03/threadspool)
- **MAESTRO** · needs-license-review: No complete repository software license was available from the inspected endpoint; creative potential alone is insufficient for eligibility. [Source](https://github.com/midotronn/MAESTRO)
- **Aether Companion** · needs-license-review: The inspected repository did not expose a complete software license at its license endpoint. It remains outside eligible additions. [Source](https://github.com/ibrews/aether-companion)
- **Video Subtitle Remover** · needs-license-review: The application has an Apache license, but its documented ProPainter path incorporates software offered under non-commercial S-Lab terms. Component and distribution permissions need clarification before an unrestricted-software profile. [Source](https://github.com/YaoFANGUK/video-subtitle-remover) [Source](https://github.com/sczhou/ProPainter/blob/main/LICENSE)
- **LGM** · needs-license-review: The main code is MIT, but the required modified Gaussian rasterizer uses research/non-commercial Gaussian-Splatting terms. The integrated installation cannot be represented as wholly open-source software without resolving that dependency. [Source](https://github.com/3DTopia/LGM) [Source](https://github.com/ashawkey/diff-gaussian-rasterization/blob/main/LICENSE.md)
- **MAtCha** · needs-license-review: The main license is MIT, but the documented reconstruction stack depends on 2D Gaussian Splatting with research/non-commercial terms. A component-level permission review remains necessary. [Source](https://github.com/Anttwo/MAtCha) [Source](https://github.com/hbb1/2d-gaussian-splatting/blob/main/LICENSE.md)
- **Pallaidium** · needs-license-review: The GPL software file coexists with README use prohibitions including false-information generation and commercial misuse. The scope of those restrictions needs clarification before eligible inclusion; model licenses also differ. [Source](https://github.com/tin2tin/Pallaidium)

Source collection completed: 2026-10-04T12:25:10.772582+00:00
Search is a bounded sample. Stars and recent pushes are discovery signals, not verified quality or meaningful upgrades.
