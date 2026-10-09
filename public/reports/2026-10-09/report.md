# AI Media Scout — 2026-10-09

Today’s expanded edition covers 44 creative fields, including newly added ceramics and parametric design. All 306 planned repository queries and 16 model searches ran; 100 repository searches hit configured result limits, with no failed or partial queries. The search is broad, not exhaustive. 48 detailed guides and 18 additional screened discoveries cover practical media workflows and specialist research. Many guides complete earlier queued reviews or establish an older tool’s first baseline; they are not all new launches. Recent documented changes include Remiqora’s AI arranger and DAW export, OpenSubs desktop compatibility checks, and Toonflow’s canvas-paste fix. Every featured software license was read in full. Optional model restrictions, restricted dependencies and uncertain documentation remain explicit; FastGS/4C4D license conflicts, missing FAST-RIR artifacts and unresolved software releases are watchlisted. GitLab, package registries, creative plugins, international projects and primary research were checked; Codeberg/SourceHut access gaps remain visible. All platforms receive source-backed advice. No discovered tool was installed or executed.

Documentation reviewed today. Tools are not hands-on tested unless explicitly stated. Requirements and performance remain source-specific.

## Coverage

| Field | Finding |
| --- | --- |
| Images & design | Local generation frontends and StableGen broaden image workflows; Qwen Image Studio documents a high-memory Apple Silicon setup, while ComfyUI frontends depend on their selected backend. A browser UI alone does not establish local inference support. [Source 1](https://heiss-ui.vercel.app/) [Source 2](https://github.com/janishar/qwen-image-2.1-studio) |
| Video, animation & film | TurboDiffusion receives a detailed research guide, and StreamDiffusionV2 is screened for interactive video. Their acceleration claims depend on the model, GPU and measured pipeline stages; no performance was reproduced. [Source 1](https://streamdiffusionv2.github.io/) [Source 2](https://github.com/thu-ml/TurboDiffusion) |
| Audio, music & voice | Remiqora, Audio WebUI, MuseGAN and the historical Riffusion code provide different sound-generation routes. Mature-looking interfaces do not remove model-specific license or memory constraints. [Source 1](https://salu133445.github.io/musegan/) [Source 2](https://github.com/inikolax/Remiqora) |
| 3D, reconstruction & assets | Blender neural-radiance caching, StableGen and pose-free dynamic reconstruction broaden the 3D set. Geometry quality, baked texture quality and manufacturing fitness remain separate checks. [Source 1](https://bralani.github.io/nopo4d_html/) [Source 2](https://github.com/sakalond/StableGen) |
| Browser tools & web media | OpenSubs provides browser/local subtitle workflows; HEISS exposes ComfyUI generation controls. Published websites were inspected as documentation, without submitting media or testing inference. [Source 1](https://opensubs.app/) [Source 2](https://heiss-ui.vercel.app/) |
| WebXR, VR & AR | Primary Meta and Google XR development material supplements OpenGestureXR and a screened browser AR studio. Headset support, phone handoff and desktop orientation previews differ; free XR products without verified open code were not admitted. [Source 1](https://developers.meta.com/vr/blog/accelerate-vr-development-with-ai-and-immersive-web-sdk/) [Source 2](https://research.google/blog/vibe-coding-xr-accelerating-ai-xr-prototyping-with-xr-blocks-and-gemini/) [Source 3](https://nirholas.github.io/3D-AR-Studio/) |
| Computational art & creative coding | Complex-valued learned Gaussian holography, a PINN beam-shaping method and neural reconstruction support computational imaging experiments. They are research components with optical/training assumptions, not ready-made exhibition hardware. [Source 1](https://complightlab.com/publications/complex_valued_2d_gaussians/) [Source 2](https://arxiv.org/abs/2607.18012) |
| Interactive, immersive & live media | Streaming diffusion and conversational-avatar frameworks are screened for interactive media. Keyword-based scene selection in SoundVisualizer is deterministic; its documented AI contribution comes from an external agent controlling the creative workflow. [Source 1](https://streamdiffusionv2.github.io/) [Source 2](https://github.com/cayatur/SoundVisualizer) [Source 3](https://github.com/uezo/aiavatarkit) |
| 3D printing & generative CAD | text-to-cad and StableGen add editable-geometry and mesh/texture routes. cadgen has a recent v0.7.19 package release; that fact does not validate generated tolerances, supports or material behavior. [Source 1](https://pypi.org/project/cadgen/) [Source 2](https://www.texttocad.dev/) [Source 3](https://github.com/sakalond/StableGen) |
| Games & production pipelines | Agent-authored 2D rigs, pixel assets and reconstructed scenes supply possible game-production inputs. A preview renderer or automatic export does not establish production-ready topology, animation or collision behavior. [Source 1](https://github.com/RevStudio/Rev2D) [Source 2](https://github.com/gfargo/pixelkiln) [Source 3](https://bralani.github.io/nopo4d_html/) |
| Motion capture & character animation | CHAMP and FollowYourPose receive first detailed baseline reviews; ReactDance adds a reaction-conditioned dance research direction. Older model baselines are explicitly distinguished from new releases. [Source 1](https://follow-your-pose.github.io/) [Source 2](https://github.com/fudan-generative-vision/champ) [Source 3](https://github.com/RipeMangoBox/ReactDance) |
| Avatars, digital humans & lip sync | RelightableAvatar, AvatarScript and the screened Neural Face Rigging code address different representation, speech and animation stages. Model, voice, body-data and mesh-preparation restrictions remain separate from source licenses. [Source 1](https://wenbin-lin.github.io/RelightableAvatar-page/) [Source 2](https://dafei-qin.github.io/NFR/) [Source 3](https://github.com/receptron/avatarscript) |
| VFX, compositing & relighting | Blender NRP, relightable avatars and the Radiance nodes offer rendering and compositing experiments. Radiance explicitly separates its GPL code from non-commercial RUDRA weights; generated passes are estimates. [Source 1](https://wenbin-lin.github.io/RelightableAvatar-page/) [Source 2](https://github.com/bgyss/Blender-NRP) [Source 3](https://github.com/FXTD-Studios/radiance) |
| Spatial audio & volumetric media | The neural-acoustics sweep revisited FAST-RIR and found a current missing-data/checkpoint notice. Previously profiled HRTF work remains available in the library; no newly reproducible complete spatial-audio application was established today. [Source 1](https://github.com/anton-jeran/FAST-RIR) [Source 2](https://anton-jeran.github.io/FRIR/) |
| Photogrammetry, scanning & neural rendering | movie2threejs is now documented in detail and NoPo4D is screened for dynamic reconstruction. NoPo4D’s website uses a reduced input setting for browser rendering, so that viewer is not the paper benchmark. [Source 1](https://bralani.github.io/nopo4d_html/) [Source 2](https://github.com/rsasaki0109/movie2threejs) |
| Editing, captions & post-production | OpenSubs and VidBee combine practical media acquisition/caption workflows with AI. Timeline Studio was researched but held out because its MIT license and research-only README language need clarification. [Source 1](https://opensubs.app/) [Source 2](https://vidbee.org/download/) [Source 3](https://github.com/MartinDelophy/ai-video-editor) |
| Vector graphics, illustration & textures | PyPotteryTrace and TechPack AI Builder cover learned drawing-vectorization and AI-assisted technical-sheet inputs. SVG export alone is not an AI capability; the model contribution is identified separately in each entry. [Source 1](https://lrncrd.github.io/PyPottery/) [Source 2](https://github.com/morfemartin/techpack-ai-builder) |
| Typography, fonts & layout | Khmer font workflows are documented with their specific AI role. Current modal kinetic typography research remains a watchlist finding because released-code licensing was not established. [Source 1](https://github.com/lienghongky/CXM-KFF) [Source 2](https://arxiv.org/abs/2609.38325) |
| Storyboarding, narrative & comics | ToonFlow and Troupe receive workflow-level guides covering scripts, narration and scene assembly. Generated still-card videos are distinguished from animated character performances. [Source 1](https://github.com/HBAI-Ltd/Toonflow-app) [Source 2](https://github.com/maxgfr/troupe) |
| Creative publishing & presentation | Inkos, OfficeCLI and Morningprint expose writing, document and small-print workflows. Cloud credentials, optional proprietary services and incomplete bridge packaging are described in their guides; this research run created no extra publishing automation. [Source 1](https://github.com/Narcooo/inkos) [Source 2](https://github.com/iOfficeAI/OfficeCLI) [Source 3](https://github.com/matt-w-horn/morningprint) |
| Photography, restoration & color | Neural Gaffer is screened for target-lighting edits and RelightableAvatar receives a detailed guide. A diffusion relighting result should be treated as a generated interpretation, not recovery of documented scene illumination. [Source 1](https://neural-gaffer.github.io/) [Source 2](https://wenbin-lin.github.io/RelightableAvatar-page/) |
| Data art & scientific visualization | Holographic phase workbenches and learned light-field representations extend scientific visualization. Their possible use in media installations is an editorial application idea; no medical or calibrated-measurement claim is made. [Source 1](https://complightlab.com/publications/complex_valued_2d_gaussians/) [Source 2](https://github.com/emircbngl/dhm-hybrid) |
| Physical, robotic & kinetic installations | Soma maps EEG spectrograms through pix2pix, while ArtAI uses audience input for generated projection imagery. Both are screened experimental implementations with hardware, checkpoint or legacy-service work still pending. [Source 1](https://github.com/Timamamu/Soma-EEG-to-Art-Feedback-Loop) [Source 2](https://github.com/SilentByte/artai) |
| Performance, projection & stage media | SoundVisualizer provides an agent-accessible live visual environment, and streaming diffusion suggests camera-driven performance workflows. Claimed real-time speed is configuration-dependent; no rehearsal or latency test was performed. [Source 1](https://streamdiffusionv2.github.io/) [Source 2](https://github.com/cayatur/SoundVisualizer) |
| Fashion, textiles & wearable media | TechPack AI Builder gets a full guide; a minimal SDXL-Turbo fashion notebook is screened as an educational template. The reviewed notebook did not substantiate its README’s richer multi-angle/recommendation claims. [Source 1](https://github.com/morfemartin/techpack-ai-builder) [Source 2](https://github.com/RDreamStudios/FashionAIStudio/blob/main/FashionAIStudio.ipynb) |
| Accessible media & assistive creation | OpenSubs, Whisper-WebUI and an EmDash alt-text plugin offer useful media-access building blocks. Captions, translations and image descriptions still require review and do not establish accessibility compliance. [Source 1](https://opensubs.app/) [Source 2](https://github.com/jhj0517/Whisper-WebUI) [Source 3](https://github.com/davidpivert/emdash-plugin-ai-alt-text) |
| Mobile, edge & on-device creation | The iOS Local AI Service receives a guide with explicit Apple development requirements. It is a service component rather than a complete assistant UI; browser/AR clients do not imply that every generation model runs on-device. [Source 1](https://github.com/MesutCyDev/ios-local-llm) [Source 2](https://nirholas.github.io/3D-AR-Studio/) |
| Creative learning & authoring | MuseGAN, optical-music recognition and PyPottery offer documented learning/research routes. Legacy TensorFlow environments are called out rather than presented as current easy installs. [Source 1](https://salu133445.github.io/musegan/) [Source 2](https://grfia.dlsi.ua.es/primus/) [Source 3](https://lrncrd.github.io/PyPottery/) |
| Archives, media restoration & collections | PyPottery’s four distinct applications cover extraction, drawing transformation and collection workflows; OMR supports notation transcription. Generated reconstructions and OCR must be checked against original records. [Source 1](https://lrncrd.github.io/PyPottery/) [Source 2](https://grfia.dlsi.ua.es/primus/) |
| Emerging & cross-disciplinary creative AI | The live sweep includes olfactory interfaces, holography, haptics and dynamic 4D reconstruction. Papers without verified released software/terms remain outside the eligible library. [Source 1](https://arxiv.org/abs/2604.01650) [Source 2](https://hapticgen.hcitech.org/static/pdfs/paper.pdf) [Source 3](https://bralani.github.io/nopo4d_html/) |
| Tactile, vibration and haptic media | HapticGen’s primary paper was reviewed as a text-to-vibration research lead. No additional complete software release with a fully reviewed open-source license was established today. [Source 1](https://hapticgen.hcitech.org/static/pdfs/paper.pdf) |
| Neural acoustics and responsive sound spaces | FAST-RIR provides neural room-response code, but its maintainer reports losing access to the shared model and data. A cached model card does not resolve current artifact availability, so it is watchlisted. [Source 1](https://github.com/anton-jeran/FAST-RIR) [Source 2](https://anton-jeran.github.io/FRIR/) |
| AI agents for code-authored media production | text-to-cad, OfficeCLI, SandKit and anidoodle expose concrete creative authoring to external AI agents. Deterministic renderers remain distinct from the model that writes or edits their inputs. [Source 1](https://www.texttocad.dev/) [Source 2](https://github.com/iOfficeAI/OfficeCLI) [Source 3](https://github.com/linklyai/sandkit) |
| AI kinetic typography and animated lettering | Modal Kinetic Typography remains unresolved as released software, while agent-controlled motion/scene authoring offers a documented practical route. An AI-generated repository description or ordinary CSS animation is not enough for eligibility. [Source 1](https://arxiv.org/abs/2609.38325) [Source 2](https://github.com/alexgreensh/anidoodle) |
| AI choreography and dance composition | ReactDance receives a research guide, while InfiniteDance and XRMoGen remain outside the cleared set because of non-commercial terms. GitLab MotionNet contained specification documents rather than a runnable implementation. [Source 1](https://github.com/RipeMangoBox/ReactDance) [Source 2](https://huzhongyyuan.github.io/InfiniteDance/) [Source 3](https://gitlab.com/Roxanne_Ardary/motionnet) |
| AI-assisted textile and computational craft | Voice-guided Kolam and AI-assisted garment specifications broaden craft workflows. Kolam’s speech recognition is AI, while its pattern renderer is procedural; machine-ready embroidery was not established from the thin SewSynth overview. [Source 1](https://github.com/adarshoff/kolam-studio) [Source 2](https://github.com/morfemartin/techpack-ai-builder) [Source 3](https://github.com/agrow/sewsynth) |
| AI music notation and score recovery | Zeus, the PrIMuS end-to-end OMR baseline and MoChord receive detailed guides. They address score recognition and harmonic workflows, with different model assets and legacy dependencies. [Source 1](https://grfia.dlsi.ua.es/primus/) [Source 2](https://github.com/omniomr/zeus) [Source 3](https://github.com/mocha-yuan/mochord) |
| Neural relighting and material recovery | RelightableAvatar is documented in detail and Neural Gaffer is screened for image/object relighting. Neither source establishes automatic accurate relighting of every scene. [Source 1](https://wenbin-lin.github.io/RelightableAvatar-page/) [Source 2](https://neural-gaffer.github.io/) |
| Olfactory and multisensory AI media | AromaGen describes a generative scent interface in primary research, but released software, hardware availability and a complete open license were not established. This remains an explicit field gap. [Source 1](https://arxiv.org/abs/2604.01650) |
| AI architectural visualization and spatial design | LayoutSculpt and movie2threejs receive detailed reviews for interpreting layouts and constructing interactive scenes. Inferred structure, metric scale and legal model use require independent checks. [Source 1](https://github.com/Li-Rui-Zhe/LayoutSculpt) [Source 2](https://github.com/rsasaki0109/movie2threejs) [Source 3](https://bralani.github.io/nopo4d_html/) |
| Neural holography and light-field media | Learned complex-valued Gaussian holography receives a guide; EPINET and NoPo4D are screened for depth/dynamic-view research. Optical hardware, captured light fields and ordinary video inputs are not interchangeable. [Source 1](https://complightlab.com/publications/complex_valued_2d_gaussians/) [Source 2](https://github.com/chshin10/epinet) [Source 3](https://bralani.github.io/nopo4d_html/) |
| Neural rigging and digital puppetry | Rev2D and AvatarScript complete earlier reviews; Neural Face Rigging adds a screened facial-animation route. Rig cleanup and expression transfer still need inspection on the actual character. [Source 1](https://github.com/RevStudio/Rev2D) [Source 2](https://github.com/receptron/avatarscript) [Source 3](https://dafei-qin.github.io/NFR/) |
| AI ceramics and archaeological illustration | This newly added field found four separately documented PyPottery applications for archaeological pottery records. They support extraction, drawing processing and analysis, not proof of ceramic fabrication or kiln-ready designs. [Source 1](https://lrncrd.github.io/PyPottery/) [Source 2](https://lrncrd.github.io/PyPottery/pypotteryscan/usage.html) |
| AI parametric design and jewelry | This new field found text-to-cad, MAC and Forgent3D workflows linking agents to editable CAD and geometric feedback. Package/repository recency does not validate physical dimensions or the quality of every generated assembly. [Source 1](https://www.texttocad.dev/) [Source 2](https://pypi.org/project/cadgen/) [Source 3](https://github.com/Pan-Chera/Multi-Agent-CAD) |

## Search and review counts

44 creative fields; 306/306 repository queries attempted; 16/16 model-task queries attempted. 21797 distinct source candidates and 755 model leads. 48 detailed profiles and 18 additional screened discoveries. Source gaps: 0 failed repository queries, 0 partial repository queries, 100 bounded repository queries, 0 failed model-task queries and 2 web ecosystem gaps. Raw search candidates include duplicates of known tools, excluded projects and projects awaiting review; they are not verified recommendations.

## Research beyond GitHub

- **gitlab** · searched: MotionNet was inspected through its live project page and archived source metadata/README. The repository contained specification documents, not an implemented creator tool, so it was excluded. [Source](https://gitlab.com/Roxanne_Ardary/motionnet)
- **codeberg** · gap: Live access was blocked by robots/access restrictions. No newly cleared Codeberg software was established; this is a source-coverage gap.
- **sourcehut** · gap: Live access was blocked by robots/access restrictions. No newly cleared SourceHut software was established; this is a source-coverage gap.
- **packages** · searched: PyPI cadgen was inspected live and lists version 0.7.19. Its GitHub release timestamp is October 9 UTC (October 8 in New York); this is a recent release, not a claim of a local-date launch today. [Source](https://pypi.org/project/cadgen/)
- **creative-plugins** · searched: Blender NRP, AI Texture tools, StableGen and Radiance were reviewed through their primary documentation and complete licenses. Separate model restrictions and required hosts are recorded, including non-commercial RUDRA weights. [Source](https://github.com/bgyss/Blender-NRP) [Source](https://github.com/sakalond/StableGen) [Source](https://github.com/FXTD-Studios/radiance)
- **project-sites** · searched: Live official PyPottery, OpenSubs, HEISS, VidBee, Neural Gaffer and NoPo4D pages supplemented repository review. Troupe/TechPack demo retrieval failed; a linked demo is not claimed as a successful test. [Source](https://lrncrd.github.io/PyPottery/) [Source](https://opensubs.app/) [Source](https://heiss-ui.vercel.app/) [Source](https://neural-gaffer.github.io/) [Source](https://bralani.github.io/nopo4d_html/)
- **research-code** · searched: UCL holography, avatar relighting, music recognition and streaming diffusion were followed from primary research to released code. Haptic, olfactory and typography papers without cleared releases remain watchlist/gap findings. [Source](https://complightlab.com/publications/complex_valued_2d_gaussians/) [Source](https://wenbin-lin.github.io/RelightableAvatar-page/) [Source](https://grfia.dlsi.ua.es/primus/) [Source](https://streamdiffusionv2.github.io/)
- **international** · searched: Chinese JoyAI documentation, Khmer typography, Japanese avatar workflows and Tamil voice controls broadened the sweep. Language support and platform support are recorded independently. [Source](https://joyai-vl-video-future-academy-jd.github.io/JoyAI-VL-Interaction/) [Source](https://github.com/lienghongky/CXM-KFF) [Source](https://github.com/receptron/avatarscript) [Source](https://github.com/adarshoff/kolam-studio)

## Collection limitations

- images: bounded or incomplete query: topic:diffusion pushed:>=2026-09-09 is:public fork:false archived:false (200 of 204 matches sampled)
- images: bounded or incomplete query: topic:diffusion is:public fork:false archived:false (200 of 1433 matches sampled)
- images: bounded or incomplete query: AI image generation pushed:>=2026-09-09 is:public fork:false archived:false (200 of 1648 matches sampled)
- images: bounded or incomplete query: AI image generation created:>=2026-09-09 is:public fork:false archived:false (200 of 821 matches sampled)
- images: bounded or incomplete query: AI image generation is:public fork:false archived:false (200 of 15459 matches sampled)
- video: bounded or incomplete query: AI video pushed:>=2026-09-09 is:public fork:false archived:false (200 of 12509 matches sampled)
- video: bounded or incomplete query: AI video created:>=2026-09-09 is:public fork:false archived:false (200 of 7915 matches sampled)
- video: bounded or incomplete query: AI video is:public fork:false archived:false (200 of 83817 matches sampled)
- video: bounded or incomplete query: topic:video-generation pushed:>=2026-09-09 is:public fork:false archived:false (200 of 1590 matches sampled)
- video: bounded or incomplete query: topic:video-generation created:>=2026-09-09 is:public fork:false archived:false (200 of 666 matches sampled)
- video: bounded or incomplete query: topic:video-generation is:public fork:false archived:false (200 of 3976 matches sampled)
- audio: bounded or incomplete query: topic:music-generation pushed:>=2026-09-09 is:public fork:false archived:false (200 of 312 matches sampled)
- audio: bounded or incomplete query: topic:music-generation is:public fork:false archived:false (500 of 1200 matches sampled)
- audio: bounded or incomplete query: AI audio pushed:>=2026-09-09 is:public fork:false archived:false (200 of 3777 matches sampled)
- audio: bounded or incomplete query: AI audio created:>=2026-09-09 is:public fork:false archived:false (200 of 2014 matches sampled)
- audio: bounded or incomplete query: AI audio is:public fork:false archived:false (200 of 27838 matches sampled)
- 3d: bounded or incomplete query: 3D generation pushed:>=2026-09-09 is:public fork:false archived:false (200 of 678 matches sampled)
- 3d: bounded or incomplete query: 3D generation created:>=2026-09-09 is:public fork:false archived:false (200 of 341 matches sampled)
- 3d: bounded or incomplete query: 3D generation is:public fork:false archived:false (200 of 5806 matches sampled)
- 3d: bounded or incomplete query: topic:3d-reconstruction pushed:>=2026-09-09 is:public fork:false archived:false (200 of 262 matches sampled)
- 3d: bounded or incomplete query: topic:3d-reconstruction is:public fork:false archived:false (200 of 1920 matches sampled)
- web: bounded or incomplete query: topic:webgpu pushed:>=2026-09-09 is:public fork:false archived:false (200 of 1070 matches sampled)
- web: bounded or incomplete query: topic:webgpu created:>=2026-09-09 is:public fork:false archived:false (200 of 453 matches sampled)
- web: bounded or incomplete query: topic:webgpu is:public fork:false archived:false (200 of 2886 matches sampled)
- xr: bounded or incomplete query: AI VR pushed:>=2026-09-09 is:public fork:false archived:false (200 of 337 matches sampled)
- xr: bounded or incomplete query: AI VR is:public fork:false archived:false (200 of 2863 matches sampled)
- computational: bounded or incomplete query: AI creative coding is:public fork:false archived:false (200 of 922 matches sampled)
- computational: bounded or incomplete query: topic:generative-art pushed:>=2026-09-09 is:public fork:false archived:false (200 of 881 matches sampled)
- computational: bounded or incomplete query: topic:generative-art created:>=2026-09-09 is:public fork:false archived:false (200 of 437 matches sampled)
- computational: bounded or incomplete query: topic:generative-art is:public fork:false archived:false (200 of 3951 matches sampled)
- interactive: bounded or incomplete query: AI interactive art is:public fork:false archived:false (200 of 676 matches sampled)
- fabrication: bounded or incomplete query: AI CAD pushed:>=2026-09-09 is:public fork:false archived:false (200 of 691 matches sampled)
- fabrication: bounded or incomplete query: AI CAD created:>=2026-09-09 is:public fork:false archived:false (200 of 377 matches sampled)
- fabrication: bounded or incomplete query: AI CAD is:public fork:false archived:false (200 of 3041 matches sampled)
- fabrication: bounded or incomplete query: AI 3D printing is:public fork:false archived:false (200 of 345 matches sampled)
- gaming: bounded or incomplete query: AI game assets is:public fork:false archived:false (200 of 634 matches sampled)
- gaming: bounded or incomplete query: AI blender pushed:>=2026-09-09 is:public fork:false archived:false (200 of 415 matches sampled)
- gaming: bounded or incomplete query: AI blender created:>=2026-09-09 is:public fork:false archived:false (200 of 290 matches sampled)
- gaming: bounded or incomplete query: AI blender is:public fork:false archived:false (200 of 1566 matches sampled)
- motion: bounded or incomplete query: AI motion capture is:public fork:false archived:false (200 of 232 matches sampled)
- motion: bounded or incomplete query: motion generation is:public fork:false archived:false (200 of 1510 matches sampled)
- avatars: bounded or incomplete query: AI avatar pushed:>=2026-09-09 is:public fork:false archived:false (200 of 747 matches sampled)
- avatars: bounded or incomplete query: AI avatar created:>=2026-09-09 is:public fork:false archived:false (200 of 400 matches sampled)
- avatars: bounded or incomplete query: AI avatar is:public fork:false archived:false (200 of 5902 matches sampled)
- avatars: bounded or incomplete query: lip sync pushed:>=2026-09-09 is:public fork:false archived:false (200 of 306 matches sampled)
- avatars: bounded or incomplete query: lip sync is:public fork:false archived:false (200 of 2410 matches sampled)
- vfx: bounded or incomplete query: AI visual effects is:public fork:false archived:false (200 of 419 matches sampled)
- capture: bounded or incomplete query: topic:gaussian-splatting pushed:>=2026-09-09 is:public fork:false archived:false (200 of 249 matches sampled)
- capture: bounded or incomplete query: topic:gaussian-splatting is:public fork:false archived:false (500 of 924 matches sampled)
- capture: bounded or incomplete query: neural reconstruction is:public fork:false archived:false (200 of 1318 matches sampled)
- editing: bounded or incomplete query: AI video editing pushed:>=2026-09-09 is:public fork:false archived:false (200 of 819 matches sampled)
- editing: bounded or incomplete query: AI video editing created:>=2026-09-09 is:public fork:false archived:false (200 of 514 matches sampled)
- editing: bounded or incomplete query: AI video editing is:public fork:false archived:false (200 of 3450 matches sampled)
- editing: bounded or incomplete query: AI subtitle pushed:>=2026-09-09 is:public fork:false archived:false (200 of 359 matches sampled)
- editing: bounded or incomplete query: AI subtitle is:public fork:false archived:false (200 of 2223 matches sampled)
- vector: bounded or incomplete query: AI SVG pushed:>=2026-09-09 is:public fork:false archived:false (200 of 435 matches sampled)
- vector: bounded or incomplete query: AI SVG created:>=2026-09-09 is:public fork:false archived:false (200 of 247 matches sampled)
- vector: bounded or incomplete query: AI SVG is:public fork:false archived:false (200 of 1798 matches sampled)
- typography: bounded or incomplete query: AI typography is:public fork:false archived:false (200 of 654 matches sampled)
- typography: bounded or incomplete query: font generation is:public fork:false archived:false (400 of 416 matches sampled)
- storytelling: bounded or incomplete query: AI storyboard pushed:>=2026-09-09 is:public fork:false archived:false (200 of 390 matches sampled)
- storytelling: bounded or incomplete query: AI storyboard created:>=2026-09-09 is:public fork:false archived:false (200 of 233 matches sampled)
- storytelling: bounded or incomplete query: AI storyboard is:public fork:false archived:false (200 of 1705 matches sampled)
- storytelling: bounded or incomplete query: AI comic pushed:>=2026-09-09 is:public fork:false archived:false (200 of 1711 matches sampled)
- storytelling: bounded or incomplete query: AI comic created:>=2026-09-09 is:public fork:false archived:false (200 of 1636 matches sampled)
- storytelling: bounded or incomplete query: AI comic is:public fork:false archived:false (200 of 2996 matches sampled)
- publishing: bounded or incomplete query: AI presentation pushed:>=2026-09-09 is:public fork:false archived:false (200 of 1127 matches sampled)
- publishing: bounded or incomplete query: AI presentation created:>=2026-09-09 is:public fork:false archived:false (200 of 680 matches sampled)
- publishing: bounded or incomplete query: AI presentation is:public fork:false archived:false (200 of 8505 matches sampled)
- publishing: bounded or incomplete query: AI publishing pushed:>=2026-09-09 is:public fork:false archived:false (200 of 1057 matches sampled)
- publishing: bounded or incomplete query: AI publishing created:>=2026-09-09 is:public fork:false archived:false (200 of 644 matches sampled)
- publishing: bounded or incomplete query: AI publishing is:public fork:false archived:false (200 of 4037 matches sampled)
- photography: bounded or incomplete query: AI photo restoration is:public fork:false archived:false (200 of 202 matches sampled)
- photography: bounded or incomplete query: AI colorization pushed:>=2026-09-09 is:public fork:false archived:false (200 of 438 matches sampled)
- photography: bounded or incomplete query: AI colorization created:>=2026-09-09 is:public fork:false archived:false (200 of 277 matches sampled)
- photography: bounded or incomplete query: AI colorization is:public fork:false archived:false (200 of 4734 matches sampled)
- visualization: bounded or incomplete query: AI visualization pushed:>=2026-09-09 is:public fork:false archived:false (200 of 3203 matches sampled)
- visualization: bounded or incomplete query: AI visualization created:>=2026-09-09 is:public fork:false archived:false (200 of 1860 matches sampled)
- visualization: bounded or incomplete query: AI visualization is:public fork:false archived:false (200 of 37703 matches sampled)
- visualization: bounded or incomplete query: AI data art is:public fork:false archived:false (200 of 1021 matches sampled)
- performance: bounded or incomplete query: AI live visuals is:public fork:false archived:false (200 of 710 matches sampled)
- fashion: bounded or incomplete query: AI fashion design is:public fork:false archived:false (200 of 637 matches sampled)
- fashion: bounded or incomplete query: AI textile is:public fork:false archived:false (200 of 470 matches sampled)
- accessibility: bounded or incomplete query: AI audio description is:public fork:false archived:false (200 of 254 matches sampled)
- mobile: bounded or incomplete query: AI mobile media is:public fork:false archived:false (200 of 210 matches sampled)
- education: bounded or incomplete query: AI explainer pushed:>=2026-09-09 is:public fork:false archived:false (200 of 6472 matches sampled)
- education: bounded or incomplete query: AI explainer created:>=2026-09-09 is:public fork:false archived:false (200 of 4440 matches sampled)
- education: bounded or incomplete query: AI explainer is:public fork:false archived:false (200 of 37233 matches sampled)
- frontier: bounded or incomplete query: AI creative tools pushed:>=2026-09-09 is:public fork:false archived:false (200 of 249 matches sampled)
- frontier: bounded or incomplete query: AI creative tools is:public fork:false archived:false (200 of 1955 matches sampled)
- frontier: bounded or incomplete query: AI digital art is:public fork:false archived:false (200 of 720 matches sampled)
- frontier: bounded or incomplete query: AI multimedia is:public fork:false archived:false (200 of 1175 matches sampled)
- frontier: bounded or incomplete query: AI new media is:public fork:false archived:false (200 of 502 matches sampled)
- neural-acoustics: bounded or incomplete query: neural acoustic is:public fork:false archived:false (200 of 345 matches sampled)
- agent-media-production: bounded or incomplete query: AI agent animation is:public fork:false archived:false (200 of 507 matches sampled)
- agent-media-production: bounded or incomplete query: AI agent video editing is:public fork:false archived:false (200 of 439 matches sampled)
- architectural-media: bounded or incomplete query: AI architectural visualization is:public fork:false archived:false (200 of 909 matches sampled)
- architectural-media: bounded or incomplete query: AI floor plan is:public fork:false archived:false (200 of 636 matches sampled)
- light-field: bounded or incomplete query: AI hologram is:public fork:false archived:false (200 of 206 matches sampled)
- images: bounded or incomplete query: topic:diffusion is:public fork:false archived:false (500 of 1433 matches sampled)

## PyPotteryInk

Images & design · Archives, media restoration & collections · AI ceramics and archaeological illustration · AI-assisted textile and computational craft

First detailed documentation review; this is a baseline, not a claim that the project launched today.

### How it uses AI

A local application that uses one-step diffusion to translate pencil drawings of pottery into inked illustrations, with patches for large sheets and batch processing. Preparing archaeological or museum illustration drafts while retaining an editable review stage; compare stippling and outlines against the original drawing. [Source](https://github.com/lrncrd/PyPotteryInk/blob/main/README.md) [Source](https://lrncrd.github.io/PyPottery/) [Source](https://huggingface.co/lrncrd/PyPotteryInk)

### Introduction

A local application that uses one-step diffusion to translate pencil drawings of pottery into inked illustrations, with patches for large sheets and batch processing. [Source 1](https://github.com/lrncrd/PyPotteryInk/blob/main/README.md) [Source 2](https://lrncrd.github.io/PyPottery/) [Source 3](https://huggingface.co/lrncrd/PyPotteryInk)

### What it is good for

Preparing archaeological or museum illustration drafts while retaining an editable review stage; compare stippling and outlines against the original drawing. [Source 1](https://github.com/lrncrd/PyPotteryInk/blob/main/README.md) [Source 2](https://lrncrd.github.io/PyPottery/) [Source 3](https://huggingface.co/lrncrd/PyPotteryInk)

### Demo & examples

The PyPottery project site presents the suite and illustrated workflows; these are published examples, not a live inference session tested here. [Source 1](https://github.com/lrncrd/PyPotteryInk/blob/main/README.md) [Source 2](https://lrncrd.github.io/PyPottery/) [Source 3](https://huggingface.co/lrncrd/PyPotteryInk)

### Install

Use the documented route for your platform. These reference steps and commands were not executed in this review. [Source 1](https://github.com/lrncrd/PyPotteryInk/blob/main/README.md) [Source 2](https://lrncrd.github.io/PyPottery/) [Source 3](https://huggingface.co/lrncrd/PyPotteryInk)

1. Use the PyPottery launcher for the documented Windows or macOS route, or clone PyPotteryInk into a Python 3.12 environment.
2. For source setup install requirements.txt and start app.py; open the local interface on port 5003.
3. Run Hardware Check, download the selected model in Model Management, and run Model Diagnostics before a batch.

```sh
pip install -r requirements.txt
```


```sh
python app.py
```

### First project

Preparing archaeological or museum illustration drafts while retaining an editable review stage; compare stippling and outlines against the original drawing. [Source 1](https://github.com/lrncrd/PyPotteryInk/blob/main/README.md) [Source 2](https://lrncrd.github.io/PyPottery/) [Source 3](https://huggingface.co/lrncrd/PyPotteryInk)

1. Start with one clean pencil drawing.
2. Choose preprocessing, model and patch settings, then produce an inked draft.
3. Compare fine marks and vessel contours with the source; export only after review, then apply the same settings to a batch.
### Hardware & software

Requirements below come from the cited documentation. Undocumented limits are left unknown, and benchmarks are not universal minimums. [Source 1](https://github.com/lrncrd/PyPotteryInk/blob/main/README.md) [Source 2](https://lrncrd.github.io/PyPottery/) [Source 3](https://huggingface.co/lrncrd/PyPotteryInk)

- **Hardware:** 4+ CPU cores; 8 GB RAM minimum and 16 GB recommended. Documentation lists NVIDIA GTX 1060 with 6 GB VRAM or newer for CUDA, and M1/M2/M3 with 8 GB unified memory for MPS. CPU inference is slower. Allow at least 5 GB disk; individual LoRA downloads are additional.
- **Software:** Python 3.12 is the suite recommendation; the app states Python 3.11+. Flask, PyTorch and its listed requirements; CUDA uses FP16 and MPS uses FP32.
- **Platforms:** Windows 10/11, macOS 11+ and Ubuntu 20.04+ are documented. MPS support is specific to this app, not a promise for every PyPottery component.

### License, model weights & costs

Application code is Apache-2.0. The PyPotteryInk model card is labeled Apache-2.0, but the base diffusion model has separate terms. The README asks researchers to disclose AI assistance, model/version and drawing counts; this is distinct from the reviewed code license. [Source 1](https://github.com/lrncrd/PyPotteryInk/blob/main/LICENSE) [Source 2](https://github.com/lrncrd/PyPotteryInk/blob/main/README.md) [Source 3](https://lrncrd.github.io/PyPottery/) [Source 4](https://huggingface.co/lrncrd/PyPotteryInk)

- **Code:** Apache-2.0
- **Weights:** Application code is Apache-2.0. The PyPotteryInk model card is labeled Apache-2.0, but the base diffusion model has separate terms. The README asks researchers to disclose AI assistance, model/version and drawing counts; this is distinct from the reviewed code license.
- **Commercial:** The reviewed Apache-2.0 application-code license permits commercial activity subject to its conditions. This does not clear separate model weights, datasets, voices, dependency code, services or proprietary hosts; unrestricted end-to-end commercial use is not established.
- **Cost:** No purchase requirement was identified for the reviewed source code. Hardware, storage and any selected paid provider or proprietary host can incur costs; current service prices were not verified.

### Why it merits attention

A concrete illustration task, model diagnostics and single-image-to-batch workflow make the project useful for specialist illustration review. Documentation/source review only; the application was not installed or run. [Source 1](https://github.com/lrncrd/PyPotteryInk/blob/main/README.md) [Source 2](https://lrncrd.github.io/PyPottery/) [Source 3](https://huggingface.co/lrncrd/PyPotteryInk)

### Limitations

Generated marks can alter evidence in a drawing. Published examples do not prove archaeological fidelity. Documentation differs between older Gradio pages and the current Flask application. [Source 1](https://github.com/lrncrd/PyPotteryInk/blob/main/README.md) [Source 2](https://lrncrd.github.io/PyPottery/) [Source 3](https://huggingface.co/lrncrd/PyPotteryInk)

### Get the tool

- [Repository](https://github.com/lrncrd/PyPotteryInk)
- [Documentation](https://github.com/lrncrd/PyPotteryInk/blob/main/README.md)

## PyPotteryScan

Archives, media restoration & collections · AI ceramics and archaeological illustration · Images & design · Creative publishing & presentation

First detailed documentation review; this is a baseline, not a claim that the project launched today.

### How it uses AI

A local plate-digitization workspace combining manual vessel/text annotation with GLM-OCR or OlmOCR and optional language-model parsing. Turning illustrated catalog pages into reviewed image crops, text and structured metadata for an archive or exhibition database. [Source](https://github.com/lrncrd/PyPotteryScan/blob/main/README.md) [Source](https://lrncrd.github.io/PyPottery/pypotteryscan/usage.html)

### Introduction

A local plate-digitization workspace combining manual vessel/text annotation with GLM-OCR or OlmOCR and optional language-model parsing. [Source 1](https://github.com/lrncrd/PyPotteryScan/blob/main/README.md) [Source 2](https://lrncrd.github.io/PyPottery/pypotteryscan/usage.html)

### What it is good for

Turning illustrated catalog pages into reviewed image crops, text and structured metadata for an archive or exhibition database. [Source 1](https://github.com/lrncrd/PyPotteryScan/blob/main/README.md) [Source 2](https://lrncrd.github.io/PyPottery/pypotteryscan/usage.html)

### Demo & examples

The official usage guide describes the interface; its screenshot/animation section is still marked as forthcoming. [Source 1](https://github.com/lrncrd/PyPotteryScan/blob/main/README.md) [Source 2](https://lrncrd.github.io/PyPottery/pypotteryscan/usage.html)

### Install

Use the documented route for your platform. These reference steps and commands were not executed in this review. [Source 1](https://github.com/lrncrd/PyPotteryScan/blob/main/README.md) [Source 2](https://lrncrd.github.io/PyPottery/pypotteryscan/usage.html)

1. Install through the PyPottery launcher, or create the documented Python 3.12 source environment.
2. Install requirements.txt, start app.py and open localhost:5002.
3. Select an OCR route and download its models; the application also attempts the Qwen3.5-2B parser download.

```sh
pip install -r requirements.txt
```


```sh
python app.py
```

### First project

Turning illustrated catalog pages into reviewed image crops, text and structured metadata for an archive or exhibition database. [Source 1](https://github.com/lrncrd/PyPotteryScan/blob/main/README.md) [Source 2](https://lrncrd.github.io/PyPottery/pypotteryscan/usage.html)

1. Create a project and load plate images.
2. Mark vessel and text boxes, run OCR and correct the transcription and crop boundaries.
3. Export the reviewed images and CSV/Excel metadata or the machine-learning coordinate package.
### Hardware & software

Requirements below come from the cited documentation. Undocumented limits are left unknown, and benchmarks are not universal minimums. [Source 1](https://github.com/lrncrd/PyPotteryScan/blob/main/README.md) [Source 2](https://lrncrd.github.io/PyPottery/pypotteryscan/usage.html)

- **Hardware:** 16 GB RAM minimum; 32 GB recommended for OCR. GLM-OCR offers CPU/GPU paths. OlmOCR-7B-FP4 requires NVIDIA and roughly a 5 GB model download; a universal VRAM or total disk minimum is not documented.
- **Software:** Python 3.12 tested, Flask and listed dependencies; GLM-OCR or OlmOCR plus the optional Qwen parser have separate runtimes/model files.
- **Platforms:** Windows, macOS and Linux are documented; the NVIDIA-only OCR option does not establish Mac acceleration.

### License, model weights & costs

Apache-2.0 application code. OCR and Qwen model terms must be checked independently; the application license does not cover every downloaded checkpoint. [Source 1](https://github.com/lrncrd/PyPotteryScan/blob/main/LICENSE) [Source 2](https://github.com/lrncrd/PyPotteryScan/blob/main/README.md) [Source 3](https://lrncrd.github.io/PyPottery/pypotteryscan/usage.html)

- **Code:** Apache-2.0
- **Weights:** Apache-2.0 application code. OCR and Qwen model terms must be checked independently; the application license does not cover every downloaded checkpoint.
- **Commercial:** The reviewed Apache-2.0 application-code license permits commercial activity subject to its conditions. This does not clear separate model weights, datasets, voices, dependency code, services or proprietary hosts; unrestricted end-to-end commercial use is not established.
- **Cost:** No purchase requirement was identified for the reviewed source code. Hardware, storage and any selected paid provider or proprietary host can incur costs; current service prices were not verified.

### Why it merits attention

Manual annotation, correction and structured exports provide a useful audit trail for plate digitization. Documentation/source review only; the application was not installed or run. [Source 1](https://github.com/lrncrd/PyPotteryScan/blob/main/README.md) [Source 2](https://lrncrd.github.io/PyPottery/pypotteryscan/usage.html)

### Limitations

OCR and text-to-field parsing can misread labels. Human crop selection and verification remain necessary; no accuracy benchmark was reproduced. [Source 1](https://github.com/lrncrd/PyPotteryScan/blob/main/README.md) [Source 2](https://lrncrd.github.io/PyPottery/pypotteryscan/usage.html)

### Get the tool

- [Repository](https://github.com/lrncrd/PyPotteryScan)
- [Documentation](https://github.com/lrncrd/PyPotteryScan/blob/main/README.md)

## PyPotteryTrace

AI ceramics and archaeological illustration · Vector graphics, illustration & textures · Archives, media restoration & collections · AI-assisted textile and computational craft

First detailed documentation review; this is a baseline, not a claim that the project launched today.

### How it uses AI

An alpha application using SAM 2 segmentation to isolate pottery drawings and convert reviewed contours into layered SVG illustrations. Separating vessel profiles, decorations and sections from scanned drawings, with mirroring around a chosen axis for illustration work. [Source](https://github.com/lrncrd/PyPotteryTrace/blob/main/README.md) [Source](https://lrncrd.github.io/PyPottery/)

### Introduction

An alpha application using SAM 2 segmentation to isolate pottery drawings and convert reviewed contours into layered SVG illustrations. [Source 1](https://github.com/lrncrd/PyPotteryTrace/blob/main/README.md) [Source 2](https://lrncrd.github.io/PyPottery/)

### What it is good for

Separating vessel profiles, decorations and sections from scanned drawings, with mirroring around a chosen axis for illustration work. [Source 1](https://github.com/lrncrd/PyPotteryTrace/blob/main/README.md) [Source 2](https://lrncrd.github.io/PyPottery/)

### Demo & examples

The repository shows the segmentation/vectorization workflow. The linked technical-reference page could not be retrieved in this review. [Source 1](https://github.com/lrncrd/PyPotteryTrace/blob/main/README.md) [Source 2](https://lrncrd.github.io/PyPottery/)

### Install

Use the documented route for your platform. These reference steps and commands were not executed in this review. [Source 1](https://github.com/lrncrd/PyPotteryTrace/blob/main/README.md) [Source 2](https://lrncrd.github.io/PyPottery/)

1. Install with the PyPottery launcher or clone the application into Python 3.12.
2. Install its requirements and launch app.py on local port 5004.
3. Download a SAM 2 checkpoint; start with the default base model unless the documented model choices better suit the machine.

```sh
pip install -r requirements.txt
```


```sh
python app.py
```

### First project

Separating vessel profiles, decorations and sections from scanned drawings, with mirroring around a chosen axis for illustration work. [Source 1](https://github.com/lrncrd/PyPotteryTrace/blob/main/README.md) [Source 2](https://lrncrd.github.io/PyPottery/)

1. Upload a drawing and use positive/negative clicks to refine the mask.
2. Assign the drawing category, confirm the contour and choose the rotation/mirror axis.
3. Vectorize and inspect the SVG groups; save the project and export reviewed SVG or masks.
### Hardware & software

Requirements below come from the cited documentation. Undocumented limits are left unknown, and benchmarks are not universal minimums. [Source 1](https://github.com/lrncrd/PyPotteryTrace/blob/main/README.md) [Source 2](https://lrncrd.github.io/PyPottery/)

- **Hardware:** NVIDIA CUDA is recommended; CPU operation is documented. SAM 2 downloads range from about 156 MB (tiny) to 898 MB (large), with base about 323 MB. RAM/VRAM and total disk minimums are not published.
- **Software:** Python 3.12, SAM 2, PyTorch and the repository requirements.
- **Platforms:** Windows, Linux and macOS; the current documentation uses CPU on Apple Silicon, not the MPS path documented for PyPotteryInk.

### License, model weights & costs

Apache-2.0 code. SAM 2/checkpoint terms are separate; do not apply the app license to unrelated imported assets. [Source 1](https://github.com/lrncrd/PyPotteryTrace/blob/main/LICENSE) [Source 2](https://github.com/lrncrd/PyPotteryTrace/blob/main/README.md) [Source 3](https://lrncrd.github.io/PyPottery/)

- **Code:** Apache-2.0
- **Weights:** Apache-2.0 code. SAM 2/checkpoint terms are separate; do not apply the app license to unrelated imported assets.
- **Commercial:** The reviewed Apache-2.0 application-code license permits commercial activity subject to its conditions. This does not clear separate model weights, datasets, voices, dependency code, services or proprietary hosts; unrestricted end-to-end commercial use is not established.
- **Cost:** No purchase requirement was identified for the reviewed source code. Hardware, storage and any selected paid provider or proprietary host can incur costs; current service prices were not verified.

### Why it merits attention

Interactive mask correction and layered vector output give illustrators useful control over an otherwise automatic segmentation step. Documentation/source review only; the application was not installed or run. [Source 1](https://github.com/lrncrd/PyPotteryTrace/blob/main/README.md) [Source 2](https://lrncrd.github.io/PyPottery/)

### Limitations

Alpha status; segmentation errors can become misleading contours. SVG export is not evidence of dimensional accuracy or manufacturing readiness. [Source 1](https://github.com/lrncrd/PyPotteryTrace/blob/main/README.md) [Source 2](https://lrncrd.github.io/PyPottery/)

### Get the tool

- [Repository](https://github.com/lrncrd/PyPotteryTrace)
- [Documentation](https://github.com/lrncrd/PyPotteryTrace/blob/main/README.md)

## PyPotteryLens

AI ceramics and archaeological illustration · Archives, media restoration & collections · Images & design

First detailed documentation review; this is a baseline, not a claim that the project launched today.

### How it uses AI

A YOLO-assisted local application that detects pottery drawings in PDF plates, then lets the researcher refine annotations, masks and metadata. Preparing an image collection from illustrated archaeological publications for a digital collection or comparative visual study. [Source](https://github.com/lrncrd/PyPotteryLens/blob/main/README.md) [Source](https://lrncrd.github.io/PyPottery/)

### Introduction

A YOLO-assisted local application that detects pottery drawings in PDF plates, then lets the researcher refine annotations, masks and metadata. [Source 1](https://github.com/lrncrd/PyPotteryLens/blob/main/README.md) [Source 2](https://lrncrd.github.io/PyPottery/)

### What it is good for

Preparing an image collection from illustrated archaeological publications for a digital collection or comparative visual study. [Source 1](https://github.com/lrncrd/PyPotteryLens/blob/main/README.md) [Source 2](https://lrncrd.github.io/PyPottery/)

### Demo & examples

The suite site and repository show detection and annotation examples; no PDF was processed during this review. [Source 1](https://github.com/lrncrd/PyPotteryLens/blob/main/README.md) [Source 2](https://lrncrd.github.io/PyPottery/)

### Install

Use the documented route for your platform. These reference steps and commands were not executed in this review. [Source 1](https://github.com/lrncrd/PyPotteryLens/blob/main/README.md) [Source 2](https://lrncrd.github.io/PyPottery/)

1. Use the PyPottery launcher or a source environment with Python 3.12, within the documented 3.10–3.12 range.
2. Install requirements, start app.py and open local port 5001.
3. Allow the documented model downloads and check the detector on a small PDF first.

```sh
pip install -r requirements.txt
```


```sh
python app.py
```

### First project

Preparing an image collection from illustrated archaeological publications for a digital collection or comparative visual study. [Source 1](https://github.com/lrncrd/PyPotteryLens/blob/main/README.md) [Source 2](https://lrncrd.github.io/PyPottery/)

1. Import a PDF and run detection.
2. Correct boxes, nested objects, masks, orientation and ENT/FRAG labels.
3. Review publication metadata and export image crops plus tabular data.
### Hardware & software

Requirements below come from the cited documentation. Undocumented limits are left unknown, and benchmarks are not universal minimums. [Source 1](https://github.com/lrncrd/PyPotteryLens/blob/main/README.md) [Source 2](https://lrncrd.github.io/PyPottery/)

- **Hardware:** 8 GB RAM minimum, 16 GB recommended. NVIDIA CUDA and Apple MPS are optional; CPU is described for small/medium jobs. VRAM and total storage minimums are not documented.
- **Software:** Python 3.10–3.12, with 3.12 tested; YOLO and the listed Python/PDF dependencies. Model download access is needed initially.
- **Platforms:** The documentation lists Windows 11, Ubuntu 24.10 and macOS Sonoma 14+.

### License, model weights & costs

GPL-3.0 code: redistribution obligations differ from permissive licenses. Detector weights and source publications have independent terms; their blanket commercial availability was not established. [Source 1](https://github.com/lrncrd/PyPotteryLens/blob/main/LICENSE) [Source 2](https://github.com/lrncrd/PyPotteryLens/blob/main/README.md) [Source 3](https://lrncrd.github.io/PyPottery/)

- **Code:** GPL-3.0
- **Weights:** GPL-3.0 code: redistribution obligations differ from permissive licenses. Detector weights and source publications have independent terms; their blanket commercial availability was not established.
- **Commercial:** The reviewed GPL-3.0 application-code license permits commercial activity subject to its conditions. This does not clear separate model weights, datasets, voices, dependency code, services or proprietary hosts; unrestricted end-to-end commercial use is not established.
- **Cost:** No purchase requirement was identified for the reviewed source code. Hardware, storage and any selected paid provider or proprietary host can incur costs; current service prices were not verified.

### Why it merits attention

Detection followed by editable annotation and metadata export is a clear specialist workflow. Documentation/source review only; the application was not installed or run. [Source 1](https://github.com/lrncrd/PyPotteryLens/blob/main/README.md) [Source 2](https://lrncrd.github.io/PyPottery/)

### Limitations

Automatic boxes can miss or split drawings. Scanned publication rights and faithful attribution remain separate from software licensing. [Source 1](https://github.com/lrncrd/PyPotteryLens/blob/main/README.md) [Source 2](https://lrncrd.github.io/PyPottery/)

### Get the tool

- [Repository](https://github.com/lrncrd/PyPotteryLens)
- [Documentation](https://github.com/lrncrd/PyPotteryLens/blob/main/README.md)

## text-to-cad / cadgen

AI parametric design and jewelry · 3D printing & generative CAD · 3D, reconstruction & assets · AI architectural visualization and spatial design · AI agents for code-authored media production

First detailed documentation review; this is a baseline, not a claim that the project launched today. Recent v0.7.19 release notes describe fixes to Windows mesh export, file/screenshot failures and error reporting. Its release was October 8 in New York (October 9 UTC).

### How it uses AI

An agent-oriented CAD toolkit in which an external language model authors and revises parametric geometry through a local CAD runtime and viewer. Iterating dimensioned objects, enclosures or sculptural components, inspecting geometry and exporting STEP, GLB, STL or 3MF for downstream review. [Source](https://github.com/earthtojake/text-to-cad/blob/main/README.md) [Source](https://www.texttocad.dev/) [Source](https://pypi.org/project/cadgen/) [Source](https://github.com/earthtojake/text-to-cad/releases/tag/v0.7.19)

### Introduction

An agent-oriented CAD toolkit in which an external language model authors and revises parametric geometry through a local CAD runtime and viewer. [Source 1](https://github.com/earthtojake/text-to-cad/blob/main/README.md) [Source 2](https://www.texttocad.dev/) [Source 3](https://pypi.org/project/cadgen/) [Source 4](https://github.com/earthtojake/text-to-cad/releases/tag/v0.7.19)

### What it is good for

Iterating dimensioned objects, enclosures or sculptural components, inspecting geometry and exporting STEP, GLB, STL or 3MF for downstream review. [Source 1](https://github.com/earthtojake/text-to-cad/blob/main/README.md) [Source 2](https://www.texttocad.dev/) [Source 3](https://pypi.org/project/cadgen/) [Source 4](https://github.com/earthtojake/text-to-cad/releases/tag/v0.7.19)

### Demo & examples

The official site shows CAD/viewer examples; PyPI lists cadgen 0.7.19 on October 9. This is the first detailed library guide, not proof that the project launched today. [Source 1](https://github.com/earthtojake/text-to-cad/blob/main/README.md) [Source 2](https://www.texttocad.dev/) [Source 3](https://pypi.org/project/cadgen/) [Source 4](https://github.com/earthtojake/text-to-cad/releases/tag/v0.7.19)

### Install

Use the documented route for your platform. These reference steps and commands were not executed in this review. [Source 1](https://github.com/earthtojake/text-to-cad/blob/main/README.md) [Source 2](https://www.texttocad.dev/) [Source 3](https://pypi.org/project/cadgen/) [Source 4](https://github.com/earthtojake/text-to-cad/releases/tag/v0.7.19)

1. Choose the documented agent plugin from the latest branch; its released skills and CAD server use a matching cadgen version.
2. Install uv for the local runtime and use an existing supported agent account. Claude Code has the two plugin commands below; other agent routes are described in the README.
3. On first use allow the runtime download, then open the CAD viewer card or its local browser link.

```sh
claude plugin marketplace add earthtojake/text-to-cad#latest
```


```sh
claude plugin install text-to-cad@earthtojake
```


```sh
uvx cadgen telemetry off
```

### First project

Iterating dimensioned objects, enclosures or sculptural components, inspecting geometry and exporting STEP, GLB, STL or 3MF for downstream review. [Source 1](https://github.com/earthtojake/text-to-cad/blob/main/README.md) [Source 2](https://www.texttocad.dev/) [Source 3](https://pypi.org/project/cadgen/) [Source 4](https://github.com/earthtojake/text-to-cad/releases/tag/v0.7.19)

1. Describe a simple object with explicit dimensions and units.
2. Inspect the model, choose a face or feature in the viewer and request one controlled revision.
3. Export a neutral format and check dimensions, clearances and manufacturability in the intended downstream application.
### Hardware & software

Requirements below come from the cited documentation. Undocumented limits are left unknown, and benchmarks are not universal minimums. [Source 1](https://github.com/earthtojake/text-to-cad/blob/main/README.md) [Source 2](https://www.texttocad.dev/) [Source 3](https://pypi.org/project/cadgen/) [Source 4](https://github.com/earthtojake/text-to-cad/releases/tag/v0.7.19)

- **Hardware:** A machine able to run the chosen agent and CAD runtime; RAM, VRAM and total storage minimums are not documented. A printer is optional and separately configured.
- **Software:** uv; cadgen PyPI metadata requires Python 3.11+ and the documented desktop server command uses managed Python 3.13. Some skill installation routes also use Node/npm.
- **Platforms:** Several desktop/terminal agent integrations are documented. A fully tested Windows/macOS/Linux matrix was not established; browser viewing is not proof of backend compatibility.

### License, model weights & costs

MIT toolkit code. The external agent, manufacturing services and any printer software retain their own terms. No bundled model license is implied. [Source 1](https://github.com/earthtojake/text-to-cad/blob/main/LICENSE) [Source 2](https://github.com/earthtojake/text-to-cad/blob/main/README.md) [Source 3](https://www.texttocad.dev/) [Source 4](https://pypi.org/project/cadgen/) [Source 5](https://github.com/earthtojake/text-to-cad/releases/tag/v0.7.19)

- **Code:** MIT
- **Weights:** MIT toolkit code. The external agent, manufacturing services and any printer software retain their own terms. No bundled model license is implied.
- **Commercial:** The reviewed MIT application-code license permits commercial activity subject to its conditions. This does not clear separate model weights, datasets, voices, dependency code, services or proprietary hosts; unrestricted end-to-end commercial use is not established.
- **Cost:** No purchase requirement was identified for the reviewed source code. Hardware, storage and any selected paid provider or proprietary host can incur costs; current service prices were not verified.

### Why it merits attention

Editable CAD operations, a viewer and engineering-oriented exports offer more control than a one-shot mesh generator. Documentation/source review only; the application was not installed or run. [Source 1](https://github.com/earthtojake/text-to-cad/blob/main/README.md) [Source 2](https://www.texttocad.dev/) [Source 3](https://pypi.org/project/cadgen/) [Source 4](https://github.com/earthtojake/text-to-cad/releases/tag/v0.7.19)

### Limitations

Model output needs dimensional review. DFM suggestions and STL export do not certify a printable or safe part. Anonymous usage/crash telemetry is documented; the runtime provides a telemetry-off command. [Source 1](https://github.com/earthtojake/text-to-cad/blob/main/README.md) [Source 2](https://www.texttocad.dev/) [Source 3](https://pypi.org/project/cadgen/) [Source 4](https://github.com/earthtojake/text-to-cad/releases/tag/v0.7.19)

### Get the tool

- [Repository](https://github.com/earthtojake/text-to-cad)
- [Documentation](https://github.com/earthtojake/text-to-cad/blob/main/README.md)

## Complex-Valued 2D Gaussian Holography

Neural holography and light-field media · Computational art & creative coding · Data art & scientific visualization · Physical, robotic & kinetic installations

First detailed documentation review; this is a baseline, not a claim that the project launched today.

### How it uses AI

Research code learning compact complex-valued Gaussian holograms from RGB/depth targets through differentiable wave optics, with SIREN/MLP neural representation baselines. Studying holographic imagery, depth-plane reconstructions and phase/amplitude outputs for experimental display work; the neural baseline is explicitly available alongside the Gaussian method. [Source](https://github.com/complight/Complex-Valued_2D_Gaussian_Representation/blob/main/README.md) [Source](https://complightlab.com/publications/complex_valued_2d_gaussians/)

### Introduction

Research code learning compact complex-valued Gaussian holograms from RGB/depth targets through differentiable wave optics, with SIREN/MLP neural representation baselines. [Source 1](https://github.com/complight/Complex-Valued_2D_Gaussian_Representation/blob/main/README.md) [Source 2](https://complightlab.com/publications/complex_valued_2d_gaussians/)

### What it is good for

Studying holographic imagery, depth-plane reconstructions and phase/amplitude outputs for experimental display work; the neural baseline is explicitly available alongside the Gaussian method. [Source 1](https://github.com/complight/Complex-Valued_2D_Gaussian_Representation/blob/main/README.md) [Source 2](https://complightlab.com/publications/complex_valued_2d_gaussians/)

### Demo & examples

The Computational Light Laboratory page presents reconstruction comparisons and links the released code. Numerical reconstructions are not evidence of a ready-to-use physical display. [Source 1](https://github.com/complight/Complex-Valued_2D_Gaussian_Representation/blob/main/README.md) [Source 2](https://complightlab.com/publications/complex_valued_2d_gaussians/)

### Install

Use the documented route for your platform. These reference steps and commands were not executed in this review. [Source 1](https://github.com/complight/Complex-Valued_2D_Gaussian_Representation/blob/main/README.md) [Source 2](https://complightlab.com/publications/complex_valued_2d_gaussians/)

1. Create the documented Python 3.10 conda environment and install requirements.txt.
2. Use the pinned PyTorch 2.9.1 / torchvision 0.24.1 CUDA 12.8 build and compile both documented CUDA extensions.
3. Check the GPU architecture flags and begin with one supplied RGB/depth example.

```sh
conda create -n gholo python=3.10
```


```sh
pip install -r requirements.txt
```

### First project

Studying holographic imagery, depth-plane reconstructions and phase/amplitude outputs for experimental display work; the neural baseline is explicitly available alongside the Gaussian method. [Source 1](https://github.com/complight/Complex-Valued_2D_Gaussian_Representation/blob/main/README.md) [Source 2](https://complightlab.com/publications/complex_valued_2d_gaussians/)

1. Select an RGB image and matching depth map; without depth, only a single plane is supervised.
2. Set wavelength, pixel pitch and depth parameters to match the intended experiment, then run the supplied training example.
3. Inspect reconstructed planes and phase/amplitude maps in result_2d; compare against the SIREN/MLP baseline where relevant.
### Hardware & software

Requirements below come from the cited documentation. Undocumented limits are left unknown, and benchmarks are not universal minimums. [Source 1](https://github.com/complight/Complex-Valued_2D_Gaussian_Representation/blob/main/README.md) [Source 2](https://complightlab.com/publications/complex_valued_2d_gaussians/)

- **Hardware:** NVIDIA CUDA is required by the documented extensions. Default compilation targets A100 and RTX 3090/A6000; other targets require flag changes. RAM/VRAM minimums and full disk use are not documented.
- **Software:** Python 3.10, PyTorch 2.9.1, torchvision 0.24.1, CUDA compilation tools, odak and requirements.txt. LPIPS downloads VGG weights on first use.
- **Platforms:** CUDA source workflow; native macOS/MPS support and a tested Windows matrix are not documented.

### License, model weights & costs

MIT source. LPIPS/VGG, input imagery and other dependencies retain separate terms; no unrestricted license is inferred for arbitrary input assets. [Source 1](https://github.com/complight/Complex-Valued_2D_Gaussian_Representation/blob/main/LICENSE) [Source 2](https://github.com/complight/Complex-Valued_2D_Gaussian_Representation/blob/main/README.md) [Source 3](https://complightlab.com/publications/complex_valued_2d_gaussians/)

- **Code:** MIT
- **Weights:** MIT source. LPIPS/VGG, input imagery and other dependencies retain separate terms; no unrestricted license is inferred for arbitrary input assets.
- **Commercial:** The reviewed MIT application-code license permits commercial activity subject to its conditions. This does not clear separate model weights, datasets, voices, dependency code, services or proprietary hosts; unrestricted end-to-end commercial use is not established.
- **Cost:** No purchase requirement was identified for the reviewed source code. Hardware, storage and any selected paid provider or proprietary host can incur costs; current service prices were not verified.

### Why it merits attention

The project publishes input examples, optical parameters, baseline scripts and explicit output paths. Documentation/source review only; the application was not installed or run. [Source 1](https://github.com/complight/Complex-Valued_2D_Gaussian_Representation/blob/main/README.md) [Source 2](https://complightlab.com/publications/complex_valued_2d_gaussians/)

### Limitations

Research prototype requiring optics/CUDA knowledge. Performance claims belong to the authors. Physical SLM calibration and a display hardware recipe are additional work. [Source 1](https://github.com/complight/Complex-Valued_2D_Gaussian_Representation/blob/main/README.md) [Source 2](https://complightlab.com/publications/complex_valued_2d_gaussians/)

### Get the tool

- [Repository](https://github.com/complight/Complex-Valued_2D_Gaussian_Representation)
- [Documentation](https://github.com/complight/Complex-Valued_2D_Gaussian_Representation/blob/main/README.md)

## ReactDance

AI choreography and dance composition · Motion capture & character animation · Performance, projection & stage media · Avatars, digital humans & lip sync

First detailed documentation review; this is a baseline, not a claim that the project launched today.

### How it uses AI

An ICLR 2026 research implementation that learns long-form reactive dance conditioned on music and a partner dancer, using hierarchical motion representations. Researching duet choreography and exporting generated motion arrays/videos for evaluation before any character retargeting. [Source](https://github.com/RipeMangoBox/ReactDance/blob/main/README.md)

### Introduction

An ICLR 2026 research implementation that learns long-form reactive dance conditioned on music and a partner dancer, using hierarchical motion representations. [Source 1](https://github.com/RipeMangoBox/ReactDance/blob/main/README.md)

### What it is good for

Researching duet choreography and exporting generated motion arrays/videos for evaluation before any character retargeting. [Source 1](https://github.com/RipeMangoBox/ReactDance/blob/main/README.md)

### Demo & examples

The README contains a poster and links a project page; that page was inaccessible to the browser research tool today. The source documents ground-truth and generated-video outputs. [Source 1](https://github.com/RipeMangoBox/ReactDance/blob/main/README.md)

### Install

Use the documented route for your platform. These reference steps and commands were not executed in this review. [Source 1](https://github.com/RipeMangoBox/ReactDance/blob/main/README.md)

1. Clone the repository and create the environment from environment.yml.
2. Use the recommended Python 3.8 and PyTorch 2.1.0 with CUDA 12.1; install FFmpeg and MoviePy 1.0.3 for videos.
3. Download the documented dataset into data_lazy. Train the HFSQ stage and then ReactDance, or supply compatible checkpoints; a turnkey pretrained download was not established.

```sh
conda env create -f environment.yml
```


```sh
python vis_gt.py
```


```sh
python hfsq.py --config ./configs/hfsq128_512_q2.yaml --mode train
```


```sh
python reactdance.py --config ./configs/reactdance.yaml --mode train
```

### First project

Researching duet choreography and exporting generated motion arrays/videos for evaluation before any character retargeting. [Source 1](https://github.com/RipeMangoBox/ReactDance/blob/main/README.md)

1. Run ground-truth visualization to verify the dataset layout.
2. Train/configure the two stages and set checkpoint paths in the saved YAML configuration.
3. Sample reactive dance, then inspect pos3d_npy and video outputs and evaluate solo/duet metrics before retargeting.
### Hardware & software

Requirements below come from the cited documentation. Undocumented limits are left unknown, and benchmarks are not universal minimums. [Source 1](https://github.com/RipeMangoBox/ReactDance/blob/main/README.md)

- **Hardware:** The documented route uses an NVIDIA CUDA environment. RAM, minimum VRAM, disk capacity and training duration are not specified.
- **Software:** Python 3.8, PyTorch 2.1.0/CUDA 12.1, tested matplotlib 3.1.1, FFmpeg, MoviePy 1.0.3 and environment.yml.
- **Platforms:** A conda/CUDA research workflow is documented; supported OS versions, Mac support and CPU inference are not established.

### License, model weights & costs

MIT source code. Duolando-derived data, motion assets and any supplied checkpoints need independent permission; MIT is not a license for every dance dataset. [Source 1](https://github.com/RipeMangoBox/ReactDance/blob/main/LICENSE) [Source 2](https://github.com/RipeMangoBox/ReactDance/blob/main/README.md)

- **Code:** MIT
- **Weights:** MIT source code. Duolando-derived data, motion assets and any supplied checkpoints need independent permission; MIT is not a license for every dance dataset.
- **Commercial:** The reviewed MIT application-code license permits commercial activity subject to its conditions. This does not clear separate model weights, datasets, voices, dependency code, services or proprietary hosts; unrestricted end-to-end commercial use is not established.
- **Cost:** No purchase requirement was identified for the reviewed source code. Hardware, storage and any selected paid provider or proprietary host can incur costs; current service prices were not verified.

### Why it merits attention

Separate training, sampling and duet-specific evaluation scripts make the research procedure inspectable. Documentation/source review only; the application was not installed or run. [Source 1](https://github.com/RipeMangoBox/ReactDance/blob/main/README.md)

### Limitations

Not a live dance partner or finished animation application. The README inference examples contain formatting quirks; use the actual saved configuration path rather than shell backticks. Output contact and motion artifacts need review. [Source 1](https://github.com/RipeMangoBox/ReactDance/blob/main/README.md)

### Get the tool

- [Repository](https://github.com/RipeMangoBox/ReactDance)
- [Documentation](https://github.com/RipeMangoBox/ReactDance/blob/main/README.md)

## OpenSubs

Video, animation & film · Editing, captions & post-production · Accessible media & assistive creation · Creative publishing & presentation · Browser tools & web media

Repository is within the observed recent-creation window; this first detailed guide does not establish production maturity. The October 9 v1.0.3 release publishes instruction-decoding checks for Windows/Linux binaries and states an AVX2 baseline outside runtime-dispatched code. These are developer checks, not tests performed here.

### How it uses AI

A subtitle application using Whisper speech recognition, optional translation and styled caption rendering in a browser, with desktop and CLI variants. Producing corrected captions and social-video subtitle treatments, then exporting SRT/VTT/ASS or a captioned MP4. [Source](https://github.com/open-subs/opensubs/blob/main/README.md) [Source](https://opensubs.app/) [Source](https://github.com/open-subs/opensubs/blob/main/docs/install.md) [Source](https://github.com/open-subs/opensubs/releases/tag/v1.0.3)

### Introduction

A subtitle application using Whisper speech recognition, optional translation and styled caption rendering in a browser, with desktop and CLI variants. [Source 1](https://github.com/open-subs/opensubs/blob/main/README.md) [Source 2](https://opensubs.app/) [Source 3](https://github.com/open-subs/opensubs/blob/main/docs/install.md) [Source 4](https://github.com/open-subs/opensubs/releases/tag/v1.0.3)

### What it is good for

Producing corrected captions and social-video subtitle treatments, then exporting SRT/VTT/ASS or a captioned MP4. [Source 1](https://github.com/open-subs/opensubs/blob/main/README.md) [Source 2](https://opensubs.app/) [Source 3](https://github.com/open-subs/opensubs/blob/main/docs/install.md) [Source 4](https://github.com/open-subs/opensubs/releases/tag/v1.0.3)

### Demo & examples

The live site offers a sample clip and published Tears of Steel caption examples. No transcription or export was run here. [Source 1](https://github.com/open-subs/opensubs/blob/main/README.md) [Source 2](https://opensubs.app/) [Source 3](https://github.com/open-subs/opensubs/blob/main/docs/install.md) [Source 4](https://github.com/open-subs/opensubs/releases/tag/v1.0.3)

### Install

Use the documented route for your platform. These reference steps and commands were not executed in this review. [Source 1](https://github.com/open-subs/opensubs/blob/main/README.md) [Source 2](https://opensubs.app/) [Source 3](https://github.com/open-subs/opensubs/blob/main/docs/install.md) [Source 4](https://github.com/open-subs/opensubs/releases/tag/v1.0.3)

1. For the simplest route open opensubs.app in a WebAssembly-capable browser; WebGPU accelerates supported devices.
2. Choose a speech model and let it download into the browser cache.
3. For long-file desktop work use the appropriate release candidate and verify that FFmpeg has both ass and whisper filters. The installation guide documents unsigned builds and platform-specific setup.
### First project

Producing corrected captions and social-video subtitle treatments, then exporting SRT/VTT/ASS or a captioned MP4. [Source 1](https://github.com/open-subs/opensubs/blob/main/README.md) [Source 2](https://opensubs.app/) [Source 3](https://github.com/open-subs/opensubs/blob/main/docs/install.md) [Source 4](https://github.com/open-subs/opensubs/releases/tag/v1.0.3)

1. Load a short video or the sample, choose the language/model and transcribe.
2. Listen to uncertain cues and correct text; choose local or explicitly selected cloud translation.
3. Preview caption styling and export sidecar subtitles or a burned-in MP4.
### Hardware & software

Requirements below come from the cited documentation. Undocumented limits are left unknown, and benchmarks are not universal minimums. [Source 1](https://github.com/open-subs/opensubs/blob/main/README.md) [Source 2](https://opensubs.app/) [Source 3](https://github.com/open-subs/opensubs/blob/main/docs/install.md) [Source 4](https://github.com/open-subs/opensubs/releases/tag/v1.0.3)

- **Hardware:** Browser models are about 40–250 MB. Desktop models range from about 78 MB to 1.6 GB. A universal RAM/VRAM minimum is not documented; file size and browser limits matter. The v1.0.3 Windows/Linux desktop release states an x86-64-v3/AVX2 baseline outside runtime-dispatched libraries; it is not suitable evidence of compatibility with every old x86 CPU.
- **Software:** Browser: WebAssembly, optional WebGPU and WebCodecs for export. Desktop/CLI: FFmpeg with ass/whisper; source CLI pins Rust 1.97.1.
- **Platforms:** Web plus documented Windows x64, Apple Silicon macOS and Linux packages. Mobile native projects are not released. The website and install guide disagree on extension store availability; check the actual listing before relying on it.

### License, model weights & costs

Core code is AGPL-3.0; optional backend crates have separate permissive terms. Model licenses and paid translation/transcription services are independent. [Source 1](https://github.com/open-subs/opensubs/blob/main/LICENSE) [Source 2](https://github.com/open-subs/opensubs/blob/main/README.md) [Source 3](https://opensubs.app/) [Source 4](https://github.com/open-subs/opensubs/blob/main/docs/install.md) [Source 5](https://github.com/open-subs/opensubs/releases/tag/v1.0.3)

- **Code:** AGPL-3.0
- **Weights:** Core code is AGPL-3.0; optional backend crates have separate permissive terms. Model licenses and paid translation/transcription services are independent.
- **Commercial:** The reviewed AGPL-3.0 application-code license permits commercial activity subject to its conditions. This does not clear separate model weights, datasets, voices, dependency code, services or proprietary hosts; unrestricted end-to-end commercial use is not established.
- **Cost:** No purchase requirement was identified for the reviewed source code. Hardware, storage and any selected paid provider or proprietary host can incur costs; current service prices were not verified.

### Why it merits attention

An explicit correction stage, portable caption formats and local processing options make the workflow practical. Documentation/source review only; the application was not installed or run. [Source 1](https://github.com/open-subs/opensubs/blob/main/README.md) [Source 2](https://opensubs.app/) [Source 3](https://github.com/open-subs/opensubs/blob/main/docs/install.md) [Source 4](https://github.com/open-subs/opensubs/releases/tag/v1.0.3)

### Limitations

Cue wording is editable but timing is fixed and cues cannot be added, deleted or merged in the web editor. Cloud translation sends text; optional cloud transcription sends the selected audio. Current builds are release candidates. [Source 1](https://github.com/open-subs/opensubs/blob/main/README.md) [Source 2](https://opensubs.app/) [Source 3](https://github.com/open-subs/opensubs/blob/main/docs/install.md) [Source 4](https://github.com/open-subs/opensubs/releases/tag/v1.0.3)

### Get the tool

- [Repository](https://github.com/open-subs/opensubs)
- [Documentation](https://github.com/open-subs/opensubs/blob/main/README.md)

## Remiqora

Audio, music & voice · Editing, captions & post-production · AI music notation and score recovery · Performance, projection & stage media

Repository is within the observed recent-creation window; this first detailed guide does not establish production maturity. The October 9 v0.3.0 prerelease adds part-by-part AI arranging, DAWproject/Reaper export and selectable first-run model downloads. Desktop installers remain experimental.

### How it uses AI

A local music workspace combining ACE-Step and YuE2 generation with stem separation, score/MIDI tools and a multitrack editor. Developing song sketches into arrangements: generate variants, separate stems, add a part and export a mix or a project for another DAW. [Source](https://github.com/inikolax/remiqora/blob/master/README.md) [Source](https://github.com/inikolax/remiqora/releases/tag/v0.3.0)

### Introduction

A local music workspace combining ACE-Step and YuE2 generation with stem separation, score/MIDI tools and a multitrack editor. [Source 1](https://github.com/inikolax/remiqora/blob/master/README.md) [Source 2](https://github.com/inikolax/remiqora/releases/tag/v0.3.0)

### What it is good for

Developing song sketches into arrangements: generate variants, separate stems, add a part and export a mix or a project for another DAW. [Source 1](https://github.com/inikolax/remiqora/blob/master/README.md) [Source 2](https://github.com/inikolax/remiqora/releases/tag/v0.3.0)

### Demo & examples

The repository publishes desktop setup and editor screenshots; the documented installation tests are maintainer reports, not tests performed here. [Source 1](https://github.com/inikolax/remiqora/blob/master/README.md) [Source 2](https://github.com/inikolax/remiqora/releases/tag/v0.3.0)

### Install

Use the documented route for your platform. These reference steps and commands were not executed in this review. [Source 1](https://github.com/inikolax/remiqora/blob/master/README.md) [Source 2](https://github.com/inikolax/remiqora/releases/tag/v0.3.0)

1. Choose an experimental Windows or Apple Silicon installer, or follow the source scripts for your platform.
2. On first launch choose the model/project location and install only the desired engines; the location is not safely movable later because database paths are absolute.
3. Start with ACE-Step and the editor, then add Demucs, YuE2 or arranger base models when needed.
### First project

Developing song sketches into arrangements: generate variants, separate stems, add a part and export a mix or a project for another DAW. [Source 1](https://github.com/inikolax/remiqora/blob/master/README.md) [Source 2](https://github.com/inikolax/remiqora/releases/tag/v0.3.0)

1. Generate a short custom or instrumental sketch and compare variants.
2. Open it in the editor, separate stems or add a complementary part with the base arranger model.
3. Review the mix and export WAV/MP3, stems with a Reaper project, or DAWproject.
### Hardware & software

Requirements below come from the cited documentation. Undocumented limits are left unknown, and benchmarks are not universal minimums. [Source 1](https://github.com/inikolax/remiqora/blob/master/README.md) [Source 2](https://github.com/inikolax/remiqora/releases/tag/v0.3.0)

- **Hardware:** Windows installer: NVIDIA RTX 20-series+ and driver 580+. Initial ACE-Step setup is about 18 GB; all optional components approach 60 GB. YuE2 q8_0 is described at about 9 GB VRAM; q4_0 targets cards with 8 GB or less. XL arranger recommends 16 GB+; these are component-specific, not universal guarantees.
- **Software:** Desktop setup provisions runtimes. Linux source needs Python 3.11/3.12, uv, Node 20.19+ or 22.12+, CMake, FFmpeg and a CUDA development toolkit.
- **Platforms:** Windows/NVIDIA and macOS/Apple Silicon installers; Linux x86_64 source route was verified by maintainers on Ubuntu 24.04 through WSL2. Bare-metal Linux variants and Intel Macs are not established.

### License, model weights & costs

MIT application. ACE-Step and YuE2 terms differ: the README identifies YuE2 weights as CC-BY-NC-4.0 and warns against commercial use of that lane. Other engines/models/data retain their own terms. [Source 1](https://github.com/inikolax/remiqora/blob/master/LICENSE) [Source 2](https://github.com/inikolax/remiqora/blob/master/README.md) [Source 3](https://github.com/inikolax/remiqora/releases/tag/v0.3.0)

- **Code:** MIT
- **Weights:** MIT application. ACE-Step and YuE2 terms differ: the README identifies YuE2 weights as CC-BY-NC-4.0 and warns against commercial use of that lane. Other engines/models/data retain their own terms.
- **Commercial:** The reviewed MIT application-code license permits commercial activity subject to its conditions. This does not clear separate model weights, datasets, voices, dependency code, services or proprietary hosts; unrestricted end-to-end commercial use is not established.
- **Cost:** No purchase requirement was identified for the reviewed source code. Hardware, storage and any selected paid provider or proprietary host can incur costs; current service prices were not verified.

### Why it merits attention

A shared media library and editable DAW timeline let users build on outputs instead of only regenerating whole songs. Documentation/source review only; the application was not installed or run. [Source 1](https://github.com/inikolax/remiqora/blob/master/README.md) [Source 2](https://github.com/inikolax/remiqora/releases/tag/v0.3.0)

### Limitations

Experimental unsigned installers, large downloads and engine switching constraints. MuScriptor needs YuE2 active. The local web service has no built-in authentication; the Mac route is newer and less exercised. [Source 1](https://github.com/inikolax/remiqora/blob/master/README.md) [Source 2](https://github.com/inikolax/remiqora/releases/tag/v0.3.0)

### Get the tool

- [Repository](https://github.com/inikolax/remiqora)
- [Documentation](https://github.com/inikolax/remiqora/blob/master/README.md)

## Portable AI Studio

Images & design · Audio, music & voice · Accessible media & assistive creation · Browser tools & web media

Completed a previously screened discovery with its first detailed guide; this is not a new-launch claim.

### How it uses AI

A portable local interface for stable-diffusion.cpp image generation, llama.cpp chat, Whisper transcription and Kokoro speech synthesis. Keeping image, narration and transcription experiments in one local workspace with model management and an output gallery. [Source](https://github.com/techjarves/Portable-Local-Studio/blob/main/README.md) [Source](https://github.com/techjarves/portable-local-studio/releases)

### Introduction

A portable local interface for stable-diffusion.cpp image generation, llama.cpp chat, Whisper transcription and Kokoro speech synthesis. [Source 1](https://github.com/techjarves/Portable-Local-Studio/blob/main/README.md) [Source 2](https://github.com/techjarves/portable-local-studio/releases)

### What it is good for

Keeping image, narration and transcription experiments in one local workspace with model management and an output gallery. [Source 1](https://github.com/techjarves/Portable-Local-Studio/blob/main/README.md) [Source 2](https://github.com/techjarves/portable-local-studio/releases)

### Demo & examples

The README links a maintainer setup video and screenshots. Its portability and acceleration claims were not exercised here. [Source 1](https://github.com/techjarves/Portable-Local-Studio/blob/main/README.md) [Source 2](https://github.com/techjarves/portable-local-studio/releases)

### Install

Use the documented route for your platform. These reference steps and commands were not executed in this review. [Source 1](https://github.com/techjarves/Portable-Local-Studio/blob/main/README.md) [Source 2](https://github.com/techjarves/portable-local-studio/releases)

1. Download or clone the project and select windows.bat, linux.sh or mac.sh for the documented platform.
2. First launch downloads the portable runtime/backends; add a supported complete model in the correct workspace or use Model Manager.
3. Open localhost:1420, select the model and verify a small job before adding larger checkpoints.
### First project

Keeping image, narration and transcription experiments in one local workspace with model management and an output gallery. [Source 1](https://github.com/techjarves/Portable-Local-Studio/blob/main/README.md) [Source 2](https://github.com/techjarves/portable-local-studio/releases)

1. Start with a documented small SD 1.5 image model or a speech model.
2. Generate an image or transcribe a short recording and inspect the saved result/metadata.
3. Switch workspaces deliberately; image and text engines are mutually exclusive by default.
### Hardware & software

Requirements below come from the cited documentation. Undocumented limits are left unknown, and benchmarks are not universal minimums. [Source 1](https://github.com/techjarves/Portable-Local-Studio/blob/main/README.md) [Source 2](https://github.com/techjarves/portable-local-studio/releases)

- **Hardware:** No universal RAM/VRAM minimum is published. Listed image downloads range from roughly 2 GB SD 1.5 to 6.6 GB SDXL; backends and speech models add storage. Hardware acceleration depends on the selected backend/driver.
- **Software:** Portable Node 22 on Windows; model-specific backends. Linux prebuilt binaries require glibc 2.38+, GLIBCXX_3.4.32+ and libgomp; Vulkan also needs its loader/driver. Optional OpenVINO NPU setup has additional Python/driver requirements.
- **Platforms:** 64-bit Windows 10/11, modern Linux and Apple Silicon macOS are documented. Intel Macs are explicitly unsupported. CUDA, Vulkan, ROCm, Metal and OpenVINO routes have different requirements.

### License, model weights & costs

MIT application code. Stable Diffusion/SDXL derivatives, GGUF models and speech models have separate licenses; the model manager is not a blanket commercial permission grant. [Source 1](https://github.com/techjarves/Portable-Local-Studio/blob/main/LICENSE) [Source 2](https://github.com/techjarves/Portable-Local-Studio/blob/main/README.md) [Source 3](https://github.com/techjarves/portable-local-studio/releases)

- **Code:** MIT
- **Weights:** MIT application code. Stable Diffusion/SDXL derivatives, GGUF models and speech models have separate licenses; the model manager is not a blanket commercial permission grant.
- **Commercial:** The reviewed MIT application-code license permits commercial activity subject to its conditions. This does not clear separate model weights, datasets, voices, dependency code, services or proprietary hosts; unrestricted end-to-end commercial use is not established.
- **Cost:** No purchase requirement was identified for the reviewed source code. Hardware, storage and any selected paid provider or proprietary host can incur costs; current service prices were not verified.

### Why it merits attention

The documentation identifies supported file types, backend failure modes and platform-specific launch paths. Documentation/source review only; the application was not installed or run. [Source 1](https://github.com/techjarves/Portable-Local-Studio/blob/main/README.md) [Source 2](https://github.com/techjarves/portable-local-studio/releases)

### Limitations

Offline inference follows initial downloads. LoRA, ControlNet, VAE-only and text-encoder-only files are not standalone supported image checkpoints. A broad hardware badge does not guarantee every device. [Source 1](https://github.com/techjarves/Portable-Local-Studio/blob/main/README.md) [Source 2](https://github.com/techjarves/portable-local-studio/releases)

### Get the tool

- [Repository](https://github.com/techjarves/Portable-Local-Studio)
- [Documentation](https://github.com/techjarves/Portable-Local-Studio/blob/main/README.md)

## HEISS UI

Images & design · Video, animation & film · Photography, restoration & color · Editing, captions & post-production · Mobile, edge & on-device creation · Browser tools & web media

Repository is within the observed recent-creation window; this first detailed guide does not establish production maturity.

### How it uses AI

A local prompt/gallery frontend that drives an existing ComfyUI installation, including image generation, reference editing, upscaling and beta video workflows. Repeated prompt–compare–adjust work without editing a graph every time, while retaining access to custom ComfyUI workflows. [Source](https://github.com/tristmeister/HEISS-UI/blob/main/README.md) [Source](https://heiss-ui.vercel.app/)

### Introduction

A local prompt/gallery frontend that drives an existing ComfyUI installation, including image generation, reference editing, upscaling and beta video workflows. [Source 1](https://github.com/tristmeister/HEISS-UI/blob/main/README.md) [Source 2](https://heiss-ui.vercel.app/)

### What it is good for

Repeated prompt–compare–adjust work without editing a graph every time, while retaining access to custom ComfyUI workflows. [Source 1](https://github.com/tristmeister/HEISS-UI/blob/main/README.md) [Source 2](https://heiss-ui.vercel.app/)

### Demo & examples

The website and README show real-time generation recordings; demo mode explicitly uses placeholders and is not evidence of inference quality. [Source 1](https://github.com/tristmeister/HEISS-UI/blob/main/README.md) [Source 2](https://heiss-ui.vercel.app/)

### Install

Use the documented route for your platform. These reference steps and commands were not executed in this review. [Source 1](https://github.com/tristmeister/HEISS-UI/blob/main/README.md) [Source 2](https://heiss-ui.vercel.app/)

1. Download the Windows x64, macOS arm64 or Linux x64 release ZIP and unpack it fully.
2. Launch Start HEISS UI; packaged releases include Node and dependencies. Source users need Node 20.9+ and npm install/npm start.
3. Run ComfyUI separately and connect on port 8188 or 8000, or set its address in Settings > Connection.

```sh
npm install
```


```sh
npm start
```

### First project

Repeated prompt–compare–adjust work without editing a graph every time, while retaining access to custom ComfyUI workflows. [Source 1](https://github.com/tristmeister/HEISS-UI/blob/main/README.md) [Source 2](https://heiss-ui.vercel.app/)

1. Select a model and resolve the required weights/nodes shown by the UI.
2. Prompt or supply reference images, compare results and reuse settings from the gallery.
3. Import a reviewed custom workflow or enable LAN access only when you want another device to control the same render host.
### Hardware & software

Requirements below come from the cited documentation. Undocumented limits are left unknown, and benchmarks are not universal minimums. [Source 1](https://github.com/tristmeister/HEISS-UI/blob/main/README.md) [Source 2](https://heiss-ui.vercel.app/)

- **Hardware:** No frontend-wide RAM/VRAM/storage minimum is documented. ComfyUI and chosen models determine inference needs; a phone is a client, not the rendering machine.
- **Software:** Existing ComfyUI and its model/node dependencies. Packaged Node runtime; source Node 20.9+ with 22+ recommended. FFmpeg is included for video previews under separate terms.
- **Platforms:** Release launchers for Windows x64, Apple Silicon macOS and Linux x64. Mobile/laptop browsers can connect to a configured host over LAN.

### License, model weights & costs

MIT frontend, with retained upstream copyright; bundled FFmpeg is separately GPL licensed. Every ComfyUI node, model and weight license remains independent. [Source 1](https://github.com/tristmeister/HEISS-UI/blob/main/LICENSE) [Source 2](https://github.com/tristmeister/HEISS-UI/blob/main/README.md) [Source 3](https://heiss-ui.vercel.app/)

- **Code:** MIT
- **Weights:** MIT frontend, with retained upstream copyright; bundled FFmpeg is separately GPL licensed. Every ComfyUI node, model and weight license remains independent.
- **Commercial:** The reviewed MIT application-code license permits commercial activity subject to its conditions. This does not clear separate model weights, datasets, voices, dependency code, services or proprietary hosts; unrestricted end-to-end commercial use is not established.
- **Cost:** No purchase requirement was identified for the reviewed source code. Hardware, storage and any selected paid provider or proprietary host can incur costs; current service prices were not verified.

### Why it merits attention

Model-specific controls, workflow import and clear missing-dependency feedback support practical daily iteration. Documentation/source review only; the application was not installed or run. [Source 1](https://github.com/tristmeister/HEISS-UI/blob/main/README.md) [Source 2](https://heiss-ui.vercel.app/)

### Limitations

Video remains beta. The frontend cannot make an unsupported ComfyUI model run; gated model access and VRAM limits remain. LAN controls and private gallery storage need deliberate configuration. [Source 1](https://github.com/tristmeister/HEISS-UI/blob/main/README.md) [Source 2](https://heiss-ui.vercel.app/)

### Get the tool

- [Repository](https://github.com/tristmeister/HEISS-UI)
- [Documentation](https://github.com/tristmeister/HEISS-UI/blob/main/README.md)

## kimchi

Video, animation & film · Editing, captions & post-production · VFX, compositing & relighting · AI kinetic typography and animated lettering · AI agents for code-authored media production

Repository is within the observed recent-creation window; this first detailed guide does not establish production maturity.

### How it uses AI

A beta video editor integrating generated shots, local Whisper captions, motion graphics and agent-controlled timeline operations in a native Rust application. Prompting a shot into an editable cut, extending or bridging clips and finishing with captions, audio and conventional exports. [Source](https://github.com/ludovic111/kimchi/blob/main/README.md) [Source](https://lsuite.xyz/launcher)

### Introduction

A beta video editor integrating generated shots, local Whisper captions, motion graphics and agent-controlled timeline operations in a native Rust application. [Source 1](https://github.com/ludovic111/kimchi/blob/main/README.md) [Source 2](https://lsuite.xyz/launcher)

### What it is good for

Prompting a shot into an editable cut, extending or bridging clips and finishing with captions, audio and conventional exports. [Source 1](https://github.com/ludovic111/kimchi/blob/main/README.md) [Source 2](https://lsuite.xyz/launcher)

### Demo & examples

The repository contains timeline, motion and document examples. The public product-page fetch failed during this review. [Source 1](https://github.com/ludovic111/kimchi/blob/main/README.md) [Source 2](https://lsuite.xyz/launcher)

### Install

Use the documented route for your platform. These reference steps and commands were not executed in this review. [Source 1](https://github.com/ludovic111/kimchi/blob/main/README.md) [Source 2](https://lsuite.xyz/launcher)

1. Use the lsuite launcher and its free account for the documented Linux AppImage/deb beta, or build from source.
2. Source builds require Rust 1.92+ and the listed GPUI/audio/system development libraries.
3. Configure a chosen generation provider or a local ComfyUI workflow; download the Whisper model for local captions.
### First project

Prompting a shot into an editable cut, extending or bridging clips and finishing with captions, audio and conventional exports. [Source 1](https://github.com/ludovic111/kimchi/blob/main/README.md) [Source 2](https://lsuite.xyz/launcher)

1. Import a small set of footage and create a rough cut.
2. Generate into a gap or extend a clip, then trim and review the result on the timeline.
3. Correct captions, check motion/audio and export a preset or a chosen codec.
### Hardware & software

Requirements below come from the cited documentation. Undocumented limits are left unknown, and benchmarks are not universal minimums. [Source 1](https://github.com/ludovic111/kimchi/blob/main/README.md) [Source 2](https://lsuite.xyz/launcher)

- **Hardware:** Web/GPU rendering and inference needs depend on the workflow. Numeric RAM, VRAM and disk minimums are not published.
- **Software:** Linux beta application with bundled media components; Rust 1.92+ for source. External AI accounts/keys or local ComfyUI/Ollama are optional paths with their own dependencies.
- **Platforms:** Released beta is Linux x86-64. macOS and Windows are marked coming soon despite cross-platform rendering code and build scripts; do not treat those scripts as released support.

### License, model weights & costs

MIT editor; bundled FFmpeg is separately GPL, fonts have OFL terms and external models/providers retain their own conditions. [Source 1](https://github.com/ludovic111/kimchi/blob/main/LICENSE) [Source 2](https://github.com/ludovic111/kimchi/blob/main/README.md) [Source 3](https://lsuite.xyz/launcher)

- **Code:** MIT
- **Weights:** MIT editor; bundled FFmpeg is separately GPL, fonts have OFL terms and external models/providers retain their own conditions.
- **Commercial:** The reviewed MIT application-code license permits commercial activity subject to its conditions. This does not clear separate model weights, datasets, voices, dependency code, services or proprietary hosts; unrestricted end-to-end commercial use is not established.
- **Cost:** No purchase requirement was identified for the reviewed source code. Hardware, storage and any selected paid provider or proprietary host can incur costs; current service prices were not verified.

### Why it merits attention

Generated media remains on a real editable timeline with saved prompt/model provenance and conventional media exports. Documentation/source review only; the application was not installed or run. [Source 1](https://github.com/ludovic111/kimchi/blob/main/README.md) [Source 2](https://lsuite.xyz/launcher)

### Limitations

Beta application. Broad feature descriptions and test counts do not establish production parity with established editors. Provider costs, latency and model availability vary. [Source 1](https://github.com/ludovic111/kimchi/blob/main/README.md) [Source 2](https://lsuite.xyz/launcher)

### Get the tool

- [Repository](https://github.com/ludovic111/kimchi)
- [Documentation](https://github.com/ludovic111/kimchi/blob/main/README.md)

## Toonflow

Video, animation & film · Storyboarding, narrative & comics · Avatars, digital humans & lip sync · AI agents for code-authored media production

Completed a previously screened discovery with its first detailed guide; this is not a new-launch claim. The October 9 v2.0.5 release fixes pasting clipboard images into the canvas and moves asset-height validation to the provider layer.

### How it uses AI

A short-drama production workspace linking AI-assisted scripts, storyboards, character/scene assets and generated media through a node-based workflow. Organizing an illustrated or animated story from text and reusable character references into shots for review and assembly. [Source](https://github.com/HBAI-Ltd/Toonflow-app/blob/master/README.md) [Source](https://github.com/HBAI-Ltd/Toonflow-app/releases) [Source](https://github.com/HBAI-Ltd/Toonflow-app/releases/tag/v2.0.5)

### Introduction

A short-drama production workspace linking AI-assisted scripts, storyboards, character/scene assets and generated media through a node-based workflow. [Source 1](https://github.com/HBAI-Ltd/Toonflow-app/blob/master/README.md) [Source 2](https://github.com/HBAI-Ltd/Toonflow-app/releases) [Source 3](https://github.com/HBAI-Ltd/Toonflow-app/releases/tag/v2.0.5)

### What it is good for

Organizing an illustrated or animated story from text and reusable character references into shots for review and assembly. [Source 1](https://github.com/HBAI-Ltd/Toonflow-app/blob/master/README.md) [Source 2](https://github.com/HBAI-Ltd/Toonflow-app/releases) [Source 3](https://github.com/HBAI-Ltd/Toonflow-app/releases/tag/v2.0.5)

### Demo & examples

The README provides interface screenshots and a work-example section; these are published demonstrations, not a verified end-to-end run here. [Source 1](https://github.com/HBAI-Ltd/Toonflow-app/blob/master/README.md) [Source 2](https://github.com/HBAI-Ltd/Toonflow-app/releases) [Source 3](https://github.com/HBAI-Ltd/Toonflow-app/releases/tag/v2.0.5)

### Install

Use the documented route for your platform. These reference steps and commands were not executed in this review. [Source 1](https://github.com/HBAI-Ltd/Toonflow-app/blob/master/README.md) [Source 2](https://github.com/HBAI-Ltd/Toonflow-app/releases) [Source 3](https://github.com/HBAI-Ltd/Toonflow-app/releases/tag/v2.0.5)

1. Download the Windows or Apple Silicon macOS desktop release, or use the documented Docker Compose route.
2. Windows needs WebView2; the installer checks for it. Linux server/source setup uses the pinned Bun 1.3.14 and FFmpeg.
3. Configure the selected model services and their keys in the application before trying generation.
4. Android users have a documented ARM64 APK route in v2.0.5, with either the embedded backend or a shared backend connection; provider credentials and model services are still separate.
### First project

Organizing an illustrated or animated story from text and reusable character references into shots for review and assembly. [Source 1](https://github.com/HBAI-Ltd/Toonflow-app/blob/master/README.md) [Source 2](https://github.com/HBAI-Ltd/Toonflow-app/releases) [Source 3](https://github.com/HBAI-Ltd/Toonflow-app/releases/tag/v2.0.5)

1. Create a project and establish the script and characters.
2. Break the story into shots and generate/revise assets with the selected providers.
3. Inspect character continuity, dialogue and shot outputs before assembling the final story.
### Hardware & software

Requirements below come from the cited documentation. Undocumented limits are left unknown, and benchmarks are not universal minimums. [Source 1](https://github.com/HBAI-Ltd/Toonflow-app/blob/master/README.md) [Source 2](https://github.com/HBAI-Ltd/Toonflow-app/releases) [Source 3](https://github.com/HBAI-Ltd/Toonflow-app/releases/tag/v2.0.5)

- **Hardware:** RAM, VRAM and total disk minimums are not documented. Hosted models reduce local inference needs but incur their own costs; local model routes depend on their models.
- **Software:** Desktop runtimes or Docker Engine/Compose; direct server source uses Bun 1.3.14 and FFmpeg. Generation services require separate setup.
- **Platforms:** Windows, Apple Silicon macOS and Docker/Linux server routes are documented; this does not establish a native Linux desktop package. The newly observed v2.0.5 release also supplies Android 8+ ARM64 APKs; its current README describes an embedded Bun backend or a connection to a shared remote backend. That is not a claim that all generation models run on the phone.

### License, model weights & costs

The current complete source license is MIT. The README states that the refactor removed earlier commercial addenda; provider, model and asset terms remain separate. [Source 1](https://github.com/HBAI-Ltd/Toonflow-app/blob/master/LICENSE) [Source 2](https://github.com/HBAI-Ltd/Toonflow-app/blob/master/README.md) [Source 3](https://github.com/HBAI-Ltd/Toonflow-app/releases) [Source 4](https://github.com/HBAI-Ltd/Toonflow-app/releases/tag/v2.0.5)

- **Code:** MIT
- **Weights:** The current complete source license is MIT. The README states that the refactor removed earlier commercial addenda; provider, model and asset terms remain separate.
- **Commercial:** The reviewed MIT application-code license permits commercial activity subject to its conditions. This does not clear separate model weights, datasets, voices, dependency code, services or proprietary hosts; unrestricted end-to-end commercial use is not established.
- **Cost:** No purchase requirement was identified for the reviewed source code. Hardware, storage and any selected paid provider or proprietary host can incur costs; current service prices were not verified.

### Why it merits attention

A project-level story/asset workflow offers more organization than a single prompt-to-video wrapper. Documentation/source review only; the application was not installed or run. [Source 1](https://github.com/HBAI-Ltd/Toonflow-app/blob/master/README.md) [Source 2](https://github.com/HBAI-Ltd/Toonflow-app/releases) [Source 3](https://github.com/HBAI-Ltd/Toonflow-app/releases/tag/v2.0.5)

### Limitations

Generation quality and cross-shot consistency are model-dependent. Sponsorship offers and advertised API prices were not treated as independently verified value claims. [Source 1](https://github.com/HBAI-Ltd/Toonflow-app/blob/master/README.md) [Source 2](https://github.com/HBAI-Ltd/Toonflow-app/releases) [Source 3](https://github.com/HBAI-Ltd/Toonflow-app/releases/tag/v2.0.5)

### Get the tool

- [Repository](https://github.com/HBAI-Ltd/Toonflow-app)
- [Documentation](https://github.com/HBAI-Ltd/Toonflow-app/blob/master/README.md)

## VidBee

Video, animation & film · Archives, media restoration & collections · Editing, captions & post-production · Accessible media & assistive creation

Completed a previously screened discovery with its first detailed guide; this is not a new-launch claim.

### How it uses AI

A desktop media library combining downloads/imports with local speech recognition, speaker-aware transcripts, timecode search and optional AI transformations. Finding a spoken moment in a recorded interview, building transcripts and preparing text/caption material for editing. [Source](https://github.com/nexmoe/VidBee/blob/main/README.md) [Source](https://vidbee.org/download/) [Source](https://vidbee.org/)

### Introduction

A desktop media library combining downloads/imports with local speech recognition, speaker-aware transcripts, timecode search and optional AI transformations. [Source 1](https://github.com/nexmoe/VidBee/blob/main/README.md) [Source 2](https://vidbee.org/download/) [Source 3](https://vidbee.org/)

### What it is good for

Finding a spoken moment in a recorded interview, building transcripts and preparing text/caption material for editing. [Source 1](https://github.com/nexmoe/VidBee/blob/main/README.md) [Source 2](https://vidbee.org/download/) [Source 3](https://vidbee.org/)

### Demo & examples

The official site presents transcript and download workflows; the project README documents the current local ASR options. [Source 1](https://github.com/nexmoe/VidBee/blob/main/README.md) [Source 2](https://vidbee.org/download/) [Source 3](https://vidbee.org/)

### Install

Use the documented route for your platform. These reference steps and commands were not executed in this review. [Source 1](https://github.com/nexmoe/VidBee/blob/main/README.md) [Source 2](https://vidbee.org/download/) [Source 3](https://vidbee.org/)

1. Use the official installer for the supported desktop platform.
2. In Settings select and download an ASR model such as Whisper, SenseVoice, Parakeet or Qwen3-ASR.
3. If using AI skills, configure the chosen cloud provider or a local Ollama/LM Studio endpoint separately.
### First project

Finding a spoken moment in a recorded interview, building transcripts and preparing text/caption material for editing. [Source 1](https://github.com/nexmoe/VidBee/blob/main/README.md) [Source 2](https://vidbee.org/download/) [Source 3](https://vidbee.org/)

1. Import a clip you are authorized to use.
2. Transcribe it, correct names and speaker labels, and use a transcript result to jump to the timecode.
3. Export reviewed text/captions; enable a cloud AI task only with an appropriate data-sharing choice.
### Hardware & software

Requirements below come from the cited documentation. Undocumented limits are left unknown, and benchmarks are not universal minimums. [Source 1](https://github.com/nexmoe/VidBee/blob/main/README.md) [Source 2](https://vidbee.org/download/) [Source 3](https://vidbee.org/)

- **Hardware:** The app does not publish a universal RAM, VRAM or disk minimum; model files and media dominate storage.
- **Software:** Desktop application and chosen ASR model; optional local model server or provider key for AI tasks. Exact minimum OS versions should be checked on the download page.
- **Platforms:** Official downloads cover Windows, macOS and Linux. A web/Docker interface still processes files on its server host, not necessarily on the viewing phone/browser.

### License, model weights & costs

MIT application; speech-model licenses, optional provider terms and source-media rights are independent. [Source 1](https://github.com/nexmoe/VidBee/blob/main/LICENSE) [Source 2](https://github.com/nexmoe/VidBee/blob/main/README.md) [Source 3](https://vidbee.org/download/) [Source 4](https://vidbee.org/)

- **Code:** MIT
- **Weights:** MIT application; speech-model licenses, optional provider terms and source-media rights are independent.
- **Commercial:** The reviewed MIT application-code license permits commercial activity subject to its conditions. This does not clear separate model weights, datasets, voices, dependency code, services or proprietary hosts; unrestricted end-to-end commercial use is not established.
- **Cost:** No purchase requirement was identified for the reviewed source code. Hardware, storage and any selected paid provider or proprietary host can incur costs; current service prices were not verified.

### Why it merits attention

Time-linked transcripts and a shared library are directly useful for searching and reusing recorded media. Documentation/source review only; the application was not installed or run. [Source 1](https://github.com/nexmoe/VidBee/blob/main/README.md) [Source 2](https://vidbee.org/download/) [Source 3](https://vidbee.org/)

### Limitations

Speech recognition still needs correction; cloud AI operations can send transcript content to the selected provider. Download capability does not grant rights to source media. [Source 1](https://github.com/nexmoe/VidBee/blob/main/README.md) [Source 2](https://vidbee.org/download/) [Source 3](https://vidbee.org/)

### Get the tool

- [Repository](https://github.com/nexmoe/VidBee)
- [Documentation](https://github.com/nexmoe/VidBee/blob/main/README.md)

## Audio WebUI

Audio, music & voice · Editing, captions & post-production · Performance, projection & stage media

Completed a previously screened discovery with its first detailed guide; this is not a new-launch claim.

### How it uses AI

A local web interface collecting neural audio workflows including Bark speech, AudioLDM/AudioCraft generation, RVC voice conversion and Whisper transcription. Trying speech, sound generation, voice conversion and transcription through one interface while keeping model-specific settings visible. [Source](https://github.com/gitmylo/audio-webui/blob/master/readme.md) [Source](https://github.com/gitmylo/audio-webui/blob/master/readme/features.md)

### Introduction

A local web interface collecting neural audio workflows including Bark speech, AudioLDM/AudioCraft generation, RVC voice conversion and Whisper transcription. [Source 1](https://github.com/gitmylo/audio-webui/blob/master/readme.md) [Source 2](https://github.com/gitmylo/audio-webui/blob/master/readme/features.md)

### What it is good for

Trying speech, sound generation, voice conversion and transcription through one interface while keeping model-specific settings visible. [Source 1](https://github.com/gitmylo/audio-webui/blob/master/readme.md) [Source 2](https://github.com/gitmylo/audio-webui/blob/master/readme/features.md)

### Demo & examples

The README links interface examples and a Colab notebook; availability and model output were not tested here. [Source 1](https://github.com/gitmylo/audio-webui/blob/master/readme.md) [Source 2](https://github.com/gitmylo/audio-webui/blob/master/readme/features.md)

### Install

Use the documented route for your platform. These reference steps and commands were not executed in this review. [Source 1](https://github.com/gitmylo/audio-webui/blob/master/readme.md) [Source 2](https://github.com/gitmylo/audio-webui/blob/master/readme/features.md)

1. Clone the repository and prepare Python 3.10, Git and FFmpeg for formats that need it.
2. Windows users follow run.bat and the documented C++ build-tool prerequisite; Linux/macOS use run.sh.
3. Select a feature and install/download only its required models and extensions.
### First project

Trying speech, sound generation, voice conversion and transcription through one interface while keeping model-specific settings visible. [Source 1](https://github.com/gitmylo/audio-webui/blob/master/readme.md) [Source 2](https://github.com/gitmylo/audio-webui/blob/master/readme/features.md)

1. Begin with a short speech or sound-effect prompt.
2. Select the appropriate neural engine, generate and listen to the complete output.
3. Use the transcription or conversion tab only with its own configured model; export the reviewed audio.
### Hardware & software

Requirements below come from the cited documentation. Undocumented limits are left unknown, and benchmarks are not universal minimums. [Source 1](https://github.com/gitmylo/audio-webui/blob/master/readme.md) [Source 2](https://github.com/gitmylo/audio-webui/blob/master/readme/features.md)

- **Hardware:** No single RAM/VRAM/storage minimum covers the bundled engines. GPU needs vary by Bark, AudioLDM, AudioCraft and RVC; model storage is additional.
- **Software:** Python 3.10, Git, feature-specific requirements and FFmpeg. Windows builds may need Microsoft C++ build tools.
- **Platforms:** Windows, Linux and macOS launch scripts are documented. A launcher does not establish acceleration or compatibility for every included model on every platform.

### License, model weights & costs

MIT interface. Each integrated engine, checkpoint and voice dataset retains its own terms; some audio-model weights have non-commercial restrictions. [Source 1](https://github.com/gitmylo/audio-webui/blob/master/LICENSE) [Source 2](https://github.com/gitmylo/audio-webui/blob/master/readme.md) [Source 3](https://github.com/gitmylo/audio-webui/blob/master/readme/features.md)

- **Code:** MIT
- **Weights:** MIT interface. Each integrated engine, checkpoint and voice dataset retains its own terms; some audio-model weights have non-commercial restrictions.
- **Commercial:** The reviewed MIT application-code license permits commercial activity subject to its conditions. This does not clear separate model weights, datasets, voices, dependency code, services or proprietary hosts; unrestricted end-to-end commercial use is not established.
- **Cost:** No purchase requirement was identified for the reviewed source code. Hardware, storage and any selected paid provider or proprietary host can incur costs; current service prices were not verified.

### Why it merits attention

The feature list identifies actual implemented engines and conversion/transcription tasks rather than only a generic AI label. Documentation/source review only; the application was not installed or run. [Source 1](https://github.com/gitmylo/audio-webui/blob/master/readme.md) [Source 2](https://github.com/gitmylo/audio-webui/blob/master/readme/features.md)

### Limitations

A broad multi-engine research interface can have dependency conflicts and uneven maintenance. Voice consent and model permissions remain necessary; no output was evaluated hands-on. [Source 1](https://github.com/gitmylo/audio-webui/blob/master/readme.md) [Source 2](https://github.com/gitmylo/audio-webui/blob/master/readme/features.md)

### Get the tool

- [Repository](https://github.com/gitmylo/audio-webui)
- [Documentation](https://github.com/gitmylo/audio-webui/blob/master/readme.md)

## MuseGAN / Binary MuseGAN

Audio, music & voice · AI music notation and score recovery · Creative learning & authoring · Computational art & creative coding

Completed a previously screened discovery with its first detailed guide; this is not a new-launch claim.

### How it uses AI

A legacy GAN research implementation for polyphonic multitrack piano-roll generation, including the later Binary MuseGAN approach. Exploring generated bass, drums, guitar, piano and string phrases as symbolic material for composition studies. [Source](https://github.com/salu133445/musegan/blob/main/README.md) [Source](https://hermandong.com/musegan/) [Source](https://github.com/salu133445/musegan/blob/main/requirements.txt)

### Introduction

A legacy GAN research implementation for polyphonic multitrack piano-roll generation, including the later Binary MuseGAN approach. [Source 1](https://github.com/salu133445/musegan/blob/main/README.md) [Source 2](https://hermandong.com/musegan/) [Source 3](https://github.com/salu133445/musegan/blob/main/requirements.txt)

### What it is good for

Exploring generated bass, drums, guitar, piano and string phrases as symbolic material for composition studies. [Source 1](https://github.com/salu133445/musegan/blob/main/README.md) [Source 2](https://hermandong.com/musegan/) [Source 3](https://github.com/salu133445/musegan/blob/main/requirements.txt)

### Demo & examples

The official MuseGAN site publishes audio examples. They demonstrate the research, not a new 2026 release or a modern turnkey music application. [Source 1](https://github.com/salu133445/musegan/blob/main/README.md) [Source 2](https://hermandong.com/musegan/) [Source 3](https://github.com/salu133445/musegan/blob/main/requirements.txt)

### Install

Use the documented route for your platform. These reference steps and commands were not executed in this review. [Source 1](https://github.com/salu133445/musegan/blob/main/README.md) [Source 2](https://hermandong.com/musegan/) [Source 3](https://github.com/salu133445/musegan/blob/main/requirements.txt)

1. Clone the repository and create an isolated environment compatible with its historical dependencies.
2. Inspect requirements.txt: it pins tensorflow-gpu 1.10.1, NumPy 1.14.5 and pypianoroll 0.4.6 among other old packages; a modern Python environment is not a supported substitute.
3. Download the documented pretrained experiment data/models and use the provided inference scripts.
### First project

Exploring generated bass, drums, guitar, piano and string phrases as symbolic material for composition studies. [Source 1](https://github.com/salu133445/musegan/blob/main/README.md) [Source 2](https://hermandong.com/musegan/) [Source 3](https://github.com/salu133445/musegan/blob/main/requirements.txt)

1. Run the default pretrained inference experiment first.
2. Inspect the generated piano rolls and compare interpolation examples.
3. Use the documented Pypianoroll workflow to turn suitable symbolic results into MIDI for a DAW, then edit the musical structure.
### Hardware & software

Requirements below come from the cited documentation. Undocumented limits are left unknown, and benchmarks are not universal minimums. [Source 1](https://github.com/salu133445/musegan/blob/main/README.md) [Source 2](https://hermandong.com/musegan/) [Source 3](https://github.com/salu133445/musegan/blob/main/requirements.txt)

- **Hardware:** Historical TensorFlow GPU workflow; RAM, VRAM and storage minimums are not published.
- **Software:** Pinned TensorFlow-GPU 1.10.1-era dependencies, MIDI/piano-roll packages and shell inference scripts. A currently working Python/driver combination was not established.
- **Platforms:** Research source workflow; current Windows/macOS/Linux compatibility is not documented. No native modern Apple Silicon support is claimed.

### License, model weights & costs

MIT code. Lakh Pianoroll data, source MIDI and pretrained model permissions are separate and were not established as universally commercial. [Source 1](https://github.com/salu133445/musegan/blob/main/LICENSE) [Source 2](https://github.com/salu133445/musegan/blob/main/README.md) [Source 3](https://hermandong.com/musegan/) [Source 4](https://github.com/salu133445/musegan/blob/main/requirements.txt)

- **Code:** MIT
- **Weights:** MIT code. Lakh Pianoroll data, source MIDI and pretrained model permissions are separate and were not established as universally commercial.
- **Commercial:** The reviewed MIT application-code license permits commercial activity subject to its conditions. This does not clear separate model weights, datasets, voices, dependency code, services or proprietary hosts; unrestricted end-to-end commercial use is not established.
- **Cost:** No purchase requirement was identified for the reviewed source code. Hardware, storage and any selected paid provider or proprietary host can incur costs; current service prices were not verified.

### Why it merits attention

Published samples, training/inference structure and symbolic output make it a useful historical music-generation baseline. Documentation/source review only; the application was not installed or run. [Source 1](https://github.com/salu133445/musegan/blob/main/README.md) [Source 2](https://hermandong.com/musegan/) [Source 3](https://github.com/salu133445/musegan/blob/main/requirements.txt)

### Limitations

Legacy environment with substantial setup risk. The current branch differs from original MuseGAN variants; accompaniment/control claims from the original paper do not automatically describe every current script. [Source 1](https://github.com/salu133445/musegan/blob/main/README.md) [Source 2](https://hermandong.com/musegan/) [Source 3](https://github.com/salu133445/musegan/blob/main/requirements.txt)

### Get the tool

- [Repository](https://github.com/salu133445/musegan)
- [Documentation](https://github.com/salu133445/musegan/blob/main/README.md)

## Riffusion hobby

Audio, music & voice · Computational art & creative coding · Creative learning & authoring

Completed a previously screened discovery with its first detailed guide; this is not a new-launch claim.

### How it uses AI

The original hobby research code converts diffusion-generated spectrogram imagery into audio and supports prompt interpolation through CLI, Streamlit and server interfaces. Studying image-to-sound generation and creating short experimental sonic textures from visual/audio representations. [Source](https://github.com/riffusion/riffusion-hobby/blob/main/README.md) [Source](https://huggingface.co/riffusion/riffusion-model-v1)

### Introduction

The original hobby research code converts diffusion-generated spectrogram imagery into audio and supports prompt interpolation through CLI, Streamlit and server interfaces. [Source 1](https://github.com/riffusion/riffusion-hobby/blob/main/README.md) [Source 2](https://huggingface.co/riffusion/riffusion-model-v1)

### What it is good for

Studying image-to-sound generation and creating short experimental sonic textures from visual/audio representations. [Source 1](https://github.com/riffusion/riffusion-hobby/blob/main/README.md) [Source 2](https://huggingface.co/riffusion/riffusion-model-v1)

### Demo & examples

The repository documents the Streamlit playground; the model card includes research context. This is the discontinued hobby code, distinct from later commercial Riffusion products. [Source 1](https://github.com/riffusion/riffusion-hobby/blob/main/README.md) [Source 2](https://huggingface.co/riffusion/riffusion-model-v1)

### Install

Use the documented route for your platform. These reference steps and commands were not executed in this review. [Source 1](https://github.com/riffusion/riffusion-hobby/blob/main/README.md) [Source 2](https://huggingface.co/riffusion/riffusion-model-v1)

1. Use an isolated Python 3.9/3.10 environment with the repository requirements.
2. Install FFmpeg when using formats other than WAV and download the specified model.
3. Start the Streamlit playground or use the documented image-to-audio CLI.

```sh
python -m riffusion.streamlit.playground
```

### First project

Studying image-to-sound generation and creating short experimental sonic textures from visual/audio representations. [Source 1](https://github.com/riffusion/riffusion-hobby/blob/main/README.md) [Source 2](https://huggingface.co/riffusion/riffusion-model-v1)

1. Create a short prompt and compare generated spectrogram/audio pairs.
2. Adjust interpolation or reconstruction settings while listening for artifacts.
3. Export a short sample and retain its prompt/model information for further editing.
### Hardware & software

Requirements below come from the cited documentation. Undocumented limits are left unknown, and benchmarks are not universal minimums. [Source 1](https://github.com/riffusion/riffusion-hobby/blob/main/README.md) [Source 2](https://huggingface.co/riffusion/riffusion-model-v1)

- **Hardware:** NVIDIA is preferred for fast inference; the README uses RTX 3090/A10G as examples. CPU is slower and MPS has CPU fallbacks. RAM, minimum VRAM and disk capacity are not specified.
- **Software:** Python 3.9/3.10; historical diffusers 0.9–0.11-era compatibility and FFmpeg as needed.
- **Platforms:** CUDA, CPU and a qualified MPS path are described; no current supported OS-version matrix is published.

### License, model weights & costs

MIT code. riffusion-model-v1 is labeled CreativeML OpenRAIL-M and has use restrictions/research context; it is not MIT merely because the application is. [Source 1](https://github.com/riffusion/riffusion-hobby/blob/main/LICENSE) [Source 2](https://github.com/riffusion/riffusion-hobby/blob/main/README.md) [Source 3](https://huggingface.co/riffusion/riffusion-model-v1)

- **Code:** MIT
- **Weights:** MIT code. riffusion-model-v1 is labeled CreativeML OpenRAIL-M and has use restrictions/research context; it is not MIT merely because the application is.
- **Commercial:** The reviewed MIT application-code license permits commercial activity subject to its conditions. This does not clear separate model weights, datasets, voices, dependency code, services or proprietary hosts; unrestricted end-to-end commercial use is not established.
- **Cost:** No purchase requirement was identified for the reviewed source code. Hardware, storage and any selected paid provider or proprietary host can incur costs; current service prices were not verified.

### Why it merits attention

Inspectable spectrogram generation and reconstruction expose the mechanics of a distinctive sound-making approach. Documentation/source review only; the application was not installed or run. [Source 1](https://github.com/riffusion/riffusion-hobby/blob/main/README.md) [Source 2](https://huggingface.co/riffusion/riffusion-model-v1)

### Limitations

No longer maintained, with old dependency assumptions and noisy/short-form outputs. A documented MPS path is not a performance guarantee on current Macs. [Source 1](https://github.com/riffusion/riffusion-hobby/blob/main/README.md) [Source 2](https://huggingface.co/riffusion/riffusion-model-v1)

### Get the tool

- [Repository](https://github.com/riffusion/riffusion-hobby)
- [Documentation](https://github.com/riffusion/riffusion-hobby/blob/main/README.md)

## Zeus optical music recognition

AI music notation and score recovery · Archives, media restoration & collections · Audio, music & voice

Completed a previously screened discovery with its first detailed guide; this is not a new-launch claim.

### How it uses AI

A neural optical-music-recognition CLI that converts cropped staff or grand-staff images into symbolic notation including MusicXML and LMX. Recovering editable notation from scanned music for an archive, performance edition or composition study. [Source](https://github.com/OmniOMR/zeus/blob/main/README.md) [Source](https://github.com/OmniOMR/zeus/blob/main/docs/using-the-cli.md)

### Introduction

A neural optical-music-recognition CLI that converts cropped staff or grand-staff images into symbolic notation including MusicXML and LMX. [Source 1](https://github.com/OmniOMR/zeus/blob/main/README.md) [Source 2](https://github.com/OmniOMR/zeus/blob/main/docs/using-the-cli.md)

### What it is good for

Recovering editable notation from scanned music for an archive, performance edition or composition study. [Source 1](https://github.com/OmniOMR/zeus/blob/main/README.md) [Source 2](https://github.com/OmniOMR/zeus/blob/main/docs/using-the-cli.md)

### Demo & examples

The README and CLI guide include sample images, model snapshots and expected output files; no score was transcribed here. [Source 1](https://github.com/OmniOMR/zeus/blob/main/README.md) [Source 2](https://github.com/OmniOMR/zeus/blob/main/docs/using-the-cli.md)

### Install

Use the documented route for your platform. These reference steps and commands were not executed in this review. [Source 1](https://github.com/OmniOMR/zeus/blob/main/README.md) [Source 2](https://github.com/OmniOMR/zeus/blob/main/docs/using-the-cli.md)

1. Create the project-recommended Python 3.10 environment and install the tagged package.
2. Download a compatible model snapshot separately and extract its .model directory.
3. Choose the snapshot for the type of staff image and verify the CLI help before batch work.

```sh
pip install "zeus @ git+https://github.com/OmniOMR/zeus.git@v1.0.0"
```


```sh
zeus predict --model-snapshot models/zeus-olimpic-1.0-2024-02-12.model --quiet-tf scans/grandstaff-1.jpg
```

### First project

Recovering editable notation from scanned music for an archive, performance edition or composition study. [Source 1](https://github.com/OmniOMR/zeus/blob/main/README.md) [Source 2](https://github.com/OmniOMR/zeus/blob/main/docs/using-the-cli.md)

1. Crop and deskew a single staff/grand staff rather than submitting a whole page.
2. Run predict with the model-snapshot path and one or more image paths.
3. Open the resulting MusicXML and check pitches, rhythm, voices and barlines against the scan.
### Hardware & software

Requirements below come from the cited documentation. Undocumented limits are left unknown, and benchmarks are not universal minimums. [Source 1](https://github.com/OmniOMR/zeus/blob/main/README.md) [Source 2](https://github.com/OmniOMR/zeus/blob/main/docs/using-the-cli.md)

- **Hardware:** RAM, VRAM and total disk minimums are not documented. Model snapshots require additional storage.
- **Software:** Python 3.10 is the project-pinned route with TensorFlow 2.12 dependencies; this is not a claim that TensorFlow universally lacks newer-Python builds.
- **Platforms:** Python CLI; a tested Windows/macOS/Linux matrix and Apple GPU acceleration are not documented.

### License, model weights & costs

MIT software. The documented 2026 solo-staff snapshot has CC-BY-NC-SA terms, while the 2024 grand-staff snapshot uses CC-BY-SA; choose and review the exact model before reuse. [Source 1](https://github.com/OmniOMR/zeus/blob/main/LICENSE) [Source 2](https://github.com/OmniOMR/zeus/blob/main/README.md) [Source 3](https://github.com/OmniOMR/zeus/blob/main/docs/using-the-cli.md)

- **Code:** MIT
- **Weights:** MIT software. The documented 2026 solo-staff snapshot has CC-BY-NC-SA terms, while the 2024 grand-staff snapshot uses CC-BY-SA; choose and review the exact model before reuse.
- **Commercial:** The reviewed MIT application-code license permits commercial activity subject to its conditions. This does not clear separate model weights, datasets, voices, dependency code, services or proprietary hosts; unrestricted end-to-end commercial use is not established.
- **Cost:** No purchase requirement was identified for the reviewed source code. Hardware, storage and any selected paid provider or proprietary host can incur costs; current service prices were not verified.

### Why it merits attention

Explicit crop assumptions and standard notation export make the research usable for supervised transcription. Documentation/source review only; the application was not installed or run. [Source 1](https://github.com/OmniOMR/zeus/blob/main/README.md) [Source 2](https://github.com/OmniOMR/zeus/blob/main/docs/using-the-cli.md)

### Limitations

Model fit matters: full-page layout and arbitrary handwriting are not guaranteed. Printed music and model permissions are separate from code openness. [Source 1](https://github.com/OmniOMR/zeus/blob/main/README.md) [Source 2](https://github.com/OmniOMR/zeus/blob/main/docs/using-the-cli.md)

### Get the tool

- [Repository](https://github.com/OmniOMR/zeus)
- [Documentation](https://github.com/OmniOMR/zeus/blob/main/README.md)

## tf-deep-omr

AI music notation and score recovery · Archives, media restoration & collections · Creative learning & authoring

Completed a previously screened discovery with its first detailed guide; this is not a new-launch claim.

### How it uses AI

A 2018 TensorFlow convolutional/recurrent CTC model for end-to-end recognition of monophonic printed music staves. Learning or reproducing neural score-to-symbol transcription on the PrIMuS dataset, with semantic and agnostic notation variants. [Source](https://github.com/OMR-Research/tf-end-to-end/blob/master/README.md) [Source](https://grfia.dlsi.ua.es/primus/)

### Introduction

A 2018 TensorFlow convolutional/recurrent CTC model for end-to-end recognition of monophonic printed music staves. [Source 1](https://github.com/OMR-Research/tf-end-to-end/blob/master/README.md) [Source 2](https://grfia.dlsi.ua.es/primus/)

### What it is good for

Learning or reproducing neural score-to-symbol transcription on the PrIMuS dataset, with semantic and agnostic notation variants. [Source 1](https://github.com/OMR-Research/tf-end-to-end/blob/master/README.md) [Source 2](https://grfia.dlsi.ua.es/primus/)

### Demo & examples

The README includes a test image and predicted token sequence; the official PrIMuS page provides the research dataset and model links. [Source 1](https://github.com/OMR-Research/tf-end-to-end/blob/master/README.md) [Source 2](https://grfia.dlsi.ua.es/primus/)

### Install

Use the documented route for your platform. These reference steps and commands were not executed in this review. [Source 1](https://github.com/OMR-Research/tf-end-to-end/blob/master/README.md) [Source 2](https://grfia.dlsi.ua.es/primus/)

1. Clone the repository into a separate legacy research environment.
2. Download a semantic or agnostic pretrained model from the official PrIMuS links and match it with the corresponding vocabulary.
3. The README does not publish a complete dependency lock or exact Python/TensorFlow version; resolving that environment is required before inference.

```sh
python ctc_predict.py -image Data/Example/000051652-1_2_1.png -model Models/semantic_model.meta -vocabulary Data/vocabulary_semantic.txt
```

### First project

Learning or reproducing neural score-to-symbol transcription on the PrIMuS dataset, with semantic and agnostic notation variants. [Source 1](https://github.com/OMR-Research/tf-end-to-end/blob/master/README.md) [Source 2](https://grfia.dlsi.ua.es/primus/)

1. Start with the included Data/Example staff image.
2. Run ctc_predict.py with the matching model and vocabulary.
3. Compare the output tokens with the supplied ground truth before attempting an unseen staff.
### Hardware & software

Requirements below come from the cited documentation. Undocumented limits are left unknown, and benchmarks are not universal minimums. [Source 1](https://github.com/OMR-Research/tf-end-to-end/blob/master/README.md) [Source 2](https://grfia.dlsi.ua.es/primus/)

- **Hardware:** RAM, GPU/VRAM and storage minimums are not documented.
- **Software:** TensorFlow-era Python code, CTC model/checkpoint and vocabulary. Exact dependency versions and modern compatibility are not documented.
- **Platforms:** No current OS support matrix or Apple Silicon route is established.

### License, model weights & costs

MIT software. PrIMuS data and downloaded trained models retain separate terms; commercial permissions were not established in this review. [Source 1](https://github.com/OMR-Research/tf-end-to-end/blob/master/LICENSE) [Source 2](https://github.com/OMR-Research/tf-end-to-end/blob/master/README.md) [Source 3](https://grfia.dlsi.ua.es/primus/)

- **Code:** MIT
- **Weights:** MIT software. PrIMuS data and downloaded trained models retain separate terms; commercial permissions were not established in this review.
- **Commercial:** The reviewed MIT application-code license permits commercial activity subject to its conditions. This does not clear separate model weights, datasets, voices, dependency code, services or proprietary hosts; unrestricted end-to-end commercial use is not established.
- **Cost:** No purchase requirement was identified for the reviewed source code. Hardware, storage and any selected paid provider or proprietary host can incur costs; current service prices were not verified.

### Why it merits attention

A supplied test image, ground truth and separate semantic/agnostic outputs make its intended task concrete. Documentation/source review only; the application was not installed or run. [Source 1](https://github.com/OMR-Research/tf-end-to-end/blob/master/README.md) [Source 2](https://grfia.dlsi.ua.es/primus/)

### Limitations

Legacy research, not a full score editor or polyphonic page recognizer. The agnostic example misses the final barline; environment setup remains incomplete in the README. [Source 1](https://github.com/OMR-Research/tf-end-to-end/blob/master/README.md) [Source 2](https://grfia.dlsi.ua.es/primus/)

### Get the tool

- [Repository](https://github.com/OMR-Research/tf-end-to-end)
- [Documentation](https://github.com/OMR-Research/tf-end-to-end/blob/master/README.md)

## MoChord

Audio, music & voice · AI music notation and score recovery · Creative learning & authoring · Performance, projection & stage media

Completed a previously screened discovery with its first detailed guide; this is not a new-launch claim.

### How it uses AI

A guitar composition/practice workspace using DeepSeek to propose chord progressions, song structures and practice plans, with a deterministic fallback when AI is unavailable. Turning a key/mode or musical idea into playable voicings, a heard progression and a structured practice loop. [Source](https://github.com/Mocha-Yuan/MoChord/blob/main/README.md)

### Introduction

A guitar composition/practice workspace using DeepSeek to propose chord progressions, song structures and practice plans, with a deterministic fallback when AI is unavailable. [Source 1](https://github.com/Mocha-Yuan/MoChord/blob/main/README.md)

### What it is good for

Turning a key/mode or musical idea into playable voicings, a heard progression and a structured practice loop. [Source 1](https://github.com/Mocha-Yuan/MoChord/blob/main/README.md)

### Demo & examples

The bilingual README shows the chord workspace and product interaction image; no generated music or tuner accuracy was tested. [Source 1](https://github.com/Mocha-Yuan/MoChord/blob/main/README.md)

### Install

Use the documented route for your platform. These reference steps and commands were not executed in this review. [Source 1](https://github.com/Mocha-Yuan/MoChord/blob/main/README.md)

1. Clone and run npm install, then npm run dev for the web workspace.
2. Use npm run desktop:dev for the Tauri desktop route and configure its DeepSeek key through the documented UI or local environment.
3. Set up Supabase only if cloud accounts/sync are needed; guest progress can remain local.

```sh
npm install
```


```sh
npm run desktop:dev
```

### First project

Turning a key/mode or musical idea into playable voicings, a heard progression and a structured practice loop. [Source 1](https://github.com/Mocha-Yuan/MoChord/blob/main/README.md)

1. Enter a key and progression idea and compare beginner/advanced suggestions.
2. Listen to voicings, edit awkward choices and send a selected progression into practice mode.
3. Set BPM/bars, follow the practice coach and save the progression or song draft.
### Hardware & software

Requirements below come from the cited documentation. Undocumented limits are left unknown, and benchmarks are not universal minimums. [Source 1](https://github.com/Mocha-Yuan/MoChord/blob/main/README.md)

- **Hardware:** Microphone is needed for tuning. Numeric RAM, VRAM and disk requirements are not documented; AI calls use the selected service.
- **Software:** Node/npm, React/Vite and Tauri/Rust for desktop builds. Android has a documented development workflow; exact SDK versions are not specified in the overview.
- **Platforms:** Web, Tauri desktop and Android development paths. A validated desktop OS-version matrix and released mobile store package were not established.

### License, model weights & costs

MIT application. DeepSeek service terms and optional Supabase hosting are separate; no local model weights are bundled by this description. [Source 1](https://github.com/Mocha-Yuan/MoChord/blob/main/LICENSE) [Source 2](https://github.com/Mocha-Yuan/MoChord/blob/main/README.md)

- **Code:** MIT
- **Weights:** MIT application. DeepSeek service terms and optional Supabase hosting are separate; no local model weights are bundled by this description.
- **Commercial:** The reviewed MIT application-code license permits commercial activity subject to its conditions. This does not clear separate model weights, datasets, voices, dependency code, services or proprietary hosts; unrestricted end-to-end commercial use is not established.
- **Cost:** No purchase requirement was identified for the reviewed source code. Hardware, storage and any selected paid provider or proprietary host can incur costs; current service prices were not verified.

### Why it merits attention

Structured progression validation, audible voicings and practice controls connect AI suggestions to an actionable musical exercise. Documentation/source review only; the application was not installed or run. [Source 1](https://github.com/Mocha-Yuan/MoChord/blob/main/README.md)

### Limitations

Offline chord fallback and YIN-style tuning are not neural generation. LLM harmony and fingering suggestions need musician review; browser mode does not expose the desktop API key. [Source 1](https://github.com/Mocha-Yuan/MoChord/blob/main/README.md)

### Get the tool

- [Repository](https://github.com/Mocha-Yuan/MoChord)
- [Documentation](https://github.com/Mocha-Yuan/MoChord/blob/main/README.md)

## Blender Neural Render Proxies

Neural relighting and material recovery · 3D, reconstruction & assets · VFX, compositing & relighting · Computational art & creative coding

Completed a previously screened discovery with its first detailed guide; this is not a new-launch claim.

### How it uses AI

An experimental Blender implementation that learns a neural proxy from a fixed-view path cache for interactive relighting and inverse light fitting. Exploring light-rig variations and differentiable lighting studies on a static scene without retracing the full scene for every trial. [Source](https://github.com/bgyss/Blender-NRP/blob/main/README.md) [Source](https://github.com/bgyss/Blender-NRP/blob/main/docs/USER_GUIDE.md) [Source](https://studios.disneyresearch.com/2026/07/01/neural-render-proxies-for-interactive-and-differentiable-lighting/)

### Introduction

An experimental Blender implementation that learns a neural proxy from a fixed-view path cache for interactive relighting and inverse light fitting. [Source 1](https://github.com/bgyss/Blender-NRP/blob/main/README.md) [Source 2](https://github.com/bgyss/Blender-NRP/blob/main/docs/USER_GUIDE.md) [Source 3](https://studios.disneyresearch.com/2026/07/01/neural-render-proxies-for-interactive-and-differentiable-lighting/)

### What it is good for

Exploring light-rig variations and differentiable lighting studies on a static scene without retracing the full scene for every trial. [Source 1](https://github.com/bgyss/Blender-NRP/blob/main/README.md) [Source 2](https://github.com/bgyss/Blender-NRP/blob/main/docs/USER_GUIDE.md) [Source 3](https://studios.disneyresearch.com/2026/07/01/neural-render-proxies-for-interactive-and-differentiable-lighting/)

### Demo & examples

The user guide gives a small-room bake/train/preview procedure. It is an independent implementation inspired by Disney research, not Disney’s official production plugin. [Source 1](https://github.com/bgyss/Blender-NRP/blob/main/README.md) [Source 2](https://github.com/bgyss/Blender-NRP/blob/main/docs/USER_GUIDE.md) [Source 3](https://studios.disneyresearch.com/2026/07/01/neural-render-proxies-for-interactive-and-differentiable-lighting/)

### Install

Use the documented route for your platform. These reference steps and commands were not executed in this review. [Source 1](https://github.com/bgyss/Blender-NRP/blob/main/README.md) [Source 2](https://github.com/bgyss/Blender-NRP/blob/main/docs/USER_GUIDE.md) [Source 3](https://studios.disneyresearch.com/2026/07/01/neural-render-proxies-for-interactive-and-differentiable-lighting/)

1. Package the addon with scripts/package_addon.py and install the resulting ZIP in Blender Preferences.
2. Use Blender 4.2+; the maintainer tested 5.1. Install PyTorch in Blender’s bundled Python for neural training.
3. Begin with the documented small 64×64 scene and a modest path/bounce count.

```sh
python scripts/package_addon.py
```

### First project

Exploring light-rig variations and differentiable lighting studies on a static scene without retracing the full scene for every trial. [Source 1](https://github.com/bgyss/Blender-NRP/blob/main/README.md) [Source 2](https://github.com/bgyss/Blender-NRP/blob/main/docs/USER_GUIDE.md) [Source 3](https://studios.disneyresearch.com/2026/07/01/neural-render-proxies-for-interactive-and-differentiable-lighting/)

1. Fix the scene/camera, bake the path cache and train the proxy.
2. Adjust a sphere/quad light and compare the preview with a reference render.
3. Optionally solve for lighting and export the light-rig data; rebake when geometry or camera changes.
### Hardware & software

Requirements below come from the cited documentation. Undocumented limits are left unknown, and benchmarks are not universal minimums. [Source 1](https://github.com/bgyss/Blender-NRP/blob/main/README.md) [Source 2](https://github.com/bgyss/Blender-NRP/blob/main/docs/USER_GUIDE.md) [Source 3](https://studios.disneyresearch.com/2026/07/01/neural-render-proxies-for-interactive-and-differentiable-lighting/)

- **Hardware:** No numeric RAM/VRAM minimum is published. CUDA or Apple MPS is selected where supported; cache/training size scales with the scene.
- **Software:** Blender 4.2+, Python 3.11+ for fixtures, NumPy and PyTorch in Blender’s actual Python environment.
- **Platforms:** Blender-based CUDA/MPS paths are documented; a complete tested Windows/macOS/Linux matrix is not supplied.

### License, model weights & costs

MIT addon code; Blender, PyTorch and any selected external model/ComfyUI integration retain independent terms. [Source 1](https://github.com/bgyss/Blender-NRP/blob/main/LICENSE) [Source 2](https://github.com/bgyss/Blender-NRP/blob/main/README.md) [Source 3](https://github.com/bgyss/Blender-NRP/blob/main/docs/USER_GUIDE.md) [Source 4](https://studios.disneyresearch.com/2026/07/01/neural-render-proxies-for-interactive-and-differentiable-lighting/)

- **Code:** MIT
- **Weights:** MIT addon code; Blender, PyTorch and any selected external model/ComfyUI integration retain independent terms.
- **Commercial:** The reviewed MIT application-code license permits commercial activity subject to its conditions. This does not clear separate model weights, datasets, voices, dependency code, services or proprietary hosts; unrestricted end-to-end commercial use is not established.
- **Cost:** No purchase requirement was identified for the reviewed source code. Hardware, storage and any selected paid provider or proprietary host can incur costs; current service prices were not verified.

### Why it merits attention

Explicit bake, training and reference-comparison steps make the approximation inspectable. Documentation/source review only; the application was not installed or run. [Source 1](https://github.com/bgyss/Blender-NRP/blob/main/README.md) [Source 2](https://github.com/bgyss/Blender-NRP/blob/main/docs/USER_GUIDE.md) [Source 3](https://studios.disneyresearch.com/2026/07/01/neural-render-proxies-for-interactive-and-differentiable-lighting/)

### Limitations

Static-view cache, approximate Lambertian transport and incomplete correspondence with Cycles. Without PyTorch, available fallback operations are non-neural. Responsiveness claims are not frame-rate guarantees. [Source 1](https://github.com/bgyss/Blender-NRP/blob/main/README.md) [Source 2](https://github.com/bgyss/Blender-NRP/blob/main/docs/USER_GUIDE.md) [Source 3](https://studios.disneyresearch.com/2026/07/01/neural-render-proxies-for-interactive-and-differentiable-lighting/)

### Get the tool

- [Repository](https://github.com/bgyss/Blender-NRP)
- [Documentation](https://github.com/bgyss/Blender-NRP/blob/main/README.md)

## RelightableAvatar

Avatars, digital humans & lip sync · Neural relighting and material recovery · 3D, reconstruction & assets · Performance, projection & stage media

Completed a previously screened discovery with its first detailed guide; this is not a new-launch claim.

### How it uses AI

An AAAI 2024 research system learning a relightable human avatar from monocular or sparse views through deformation, visibility and material models. Studying novel-pose and novel-light human rendering from a recorded subject, with explicit body-model and data prerequisites. [Source](https://github.com/wenbin-lin/RelightableAvatar/blob/main/README.md) [Source](https://wenbin-lin.github.io/RelightableAvatar-page/)

### Introduction

An AAAI 2024 research system learning a relightable human avatar from monocular or sparse views through deformation, visibility and material models. [Source 1](https://github.com/wenbin-lin/RelightableAvatar/blob/main/README.md) [Source 2](https://wenbin-lin.github.io/RelightableAvatar-page/)

### What it is good for

Studying novel-pose and novel-light human rendering from a recorded subject, with explicit body-model and data prerequisites. [Source 1](https://github.com/wenbin-lin/RelightableAvatar/blob/main/README.md) [Source 2](https://wenbin-lin.github.io/RelightableAvatar-page/)

### Demo & examples

The official project page publishes pipeline and rendered-video demonstrations; these were documentation evidence, not a reproduced capture session. [Source 1](https://github.com/wenbin-lin/RelightableAvatar/blob/main/README.md) [Source 2](https://wenbin-lin.github.io/RelightableAvatar-page/)

### Install

Use the documented route for your platform. These reference steps and commands were not executed in this review. [Source 1](https://github.com/wenbin-lin/RelightableAvatar/blob/main/README.md) [Source 2](https://wenbin-lin.github.io/RelightableAvatar-page/)

1. Follow the RAvatar conda environment and documented CUDA/PyTorch/PyTorch3D setup.
2. Obtain the required SMPL neutral body files under their own agreement and download the provided data/checkpoints.
3. Use the material visualization configuration before considering the multi-stage training workflow.

```sh
python run_material.py --type visualize --cfg_file configs/material_ps_m3c.yaml exp_name material_ps_m3c novel_light True vis_pose_sequence True
```

### First project

Studying novel-pose and novel-light human rendering from a recorded subject, with explicit body-model and data prerequisites. [Source 1](https://github.com/wenbin-lin/RelightableAvatar/blob/main/README.md) [Source 2](https://wenbin-lin.github.io/RelightableAvatar-page/)

1. Prepare a compatible subject dataset and configuration.
2. Render a supplied checkpoint under a novel light/pose sequence.
3. Inspect silhouette, shading and temporal artifacts before training on new capture material.
### Hardware & software

Requirements below come from the cited documentation. Undocumented limits are left unknown, and benchmarks are not universal minimums. [Source 1](https://github.com/wenbin-lin/RelightableAvatar/blob/main/README.md) [Source 2](https://wenbin-lin.github.io/RelightableAvatar-page/)

- **Hardware:** RTX 3090 is the reported GPU example, not a verified minimum. RAM, minimum VRAM and full storage requirements are not published.
- **Software:** Tested Ubuntu 22.04, Python 3.8, PyTorch 1.10.1, CUDA 11.3 and PyTorch3D 0.4.0; SMPL assets and trained checkpoints are separate downloads.
- **Platforms:** Ubuntu/CUDA is documented. Native Windows, macOS/MPS and CPU execution are not established.

### License, model weights & costs

Apache-2.0 source. SMPL has separate non-commercial conditions in the documented route; checkpoints and capture data are not automatically Apache licensed. [Source 1](https://github.com/wenbin-lin/RelightableAvatar/blob/main/LICENSE) [Source 2](https://github.com/wenbin-lin/RelightableAvatar/blob/main/README.md) [Source 3](https://wenbin-lin.github.io/RelightableAvatar-page/)

- **Code:** Apache-2.0
- **Weights:** Apache-2.0 source. SMPL has separate non-commercial conditions in the documented route; checkpoints and capture data are not automatically Apache licensed.
- **Commercial:** The reviewed Apache-2.0 application-code license permits commercial activity subject to its conditions. This does not clear separate model weights, datasets, voices, dependency code, services or proprietary hosts; unrestricted end-to-end commercial use is not established.
- **Cost:** No purchase requirement was identified for the reviewed source code. Hardware, storage and any selected paid provider or proprietary host can incur costs; current service prices were not verified.

### Why it merits attention

Pose, visibility and material stages expose the assumptions behind relighting rather than treating it as an unexplained image filter. Documentation/source review only; the application was not installed or run. [Source 1](https://github.com/wenbin-lin/RelightableAvatar/blob/main/README.md) [Source 2](https://wenbin-lin.github.io/RelightableAvatar-page/)

### Limitations

Research prototype with substantial data preparation; body-model permissions and appearance artifacts constrain reuse. A generated avatar is not a measured digital double. [Source 1](https://github.com/wenbin-lin/RelightableAvatar/blob/main/README.md) [Source 2](https://wenbin-lin.github.io/RelightableAvatar-page/)

### Get the tool

- [Repository](https://github.com/wenbin-lin/RelightableAvatar)
- [Documentation](https://github.com/wenbin-lin/RelightableAvatar/blob/main/README.md)

## PINN-shaper

Neural holography and light-field media · Computational art & creative coding · Physical, robotic & kinetic installations · Data art & scientific visualization

Completed a previously screened discovery with its first detailed guide; this is not a new-launch claim.

### How it uses AI

A physics-informed neural-network experiment for optical beam shaping, learning phase functions through a wave-optics/PDE formulation. Exploring shaped illumination and phase-map designs for computational optics or experimental light-art research. [Source](https://github.com/rafael-fuente/pinn-shaper/blob/main/README.md) [Source](https://arxiv.org/abs/2607.18012)

### Introduction

A physics-informed neural-network experiment for optical beam shaping, learning phase functions through a wave-optics/PDE formulation. [Source 1](https://github.com/rafael-fuente/pinn-shaper/blob/main/README.md) [Source 2](https://arxiv.org/abs/2607.18012)

### What it is good for

Exploring shaped illumination and phase-map designs for computational optics or experimental light-art research. [Source 1](https://github.com/rafael-fuente/pinn-shaper/blob/main/README.md) [Source 2](https://arxiv.org/abs/2607.18012)

### Demo & examples

The repository offers star/letter-pattern notebooks and numerical diffraction examples; no optical bench was tested. [Source 1](https://github.com/rafael-fuente/pinn-shaper/blob/main/README.md) [Source 2](https://arxiv.org/abs/2607.18012)

### Install

Use the documented route for your platform. These reference steps and commands were not executed in this review. [Source 1](https://github.com/rafael-fuente/pinn-shaper/blob/main/README.md) [Source 2](https://arxiv.org/abs/2607.18012)

1. Clone the repository and use an isolated Python environment.
2. Install PyTorch and the documented diffractsim dependencies; choose a compatible CUDA build only if using that acceleration path.
3. Open the supplied notebook example before substituting a new target pattern.
### First project

Exploring shaped illumination and phase-map designs for computational optics or experimental light-art research. [Source 1](https://github.com/rafael-fuente/pinn-shaper/blob/main/README.md) [Source 2](https://arxiv.org/abs/2607.18012)

1. Choose a demonstrated target intensity pattern.
2. Train the phase representation with the example settings.
3. Compare propagation with diffractsim and inspect the phase/result images before considering hardware use.
### Hardware & software

Requirements below come from the cited documentation. Undocumented limits are left unknown, and benchmarks are not universal minimums. [Source 1](https://github.com/rafael-fuente/pinn-shaper/blob/main/README.md) [Source 2](https://arxiv.org/abs/2607.18012)

- **Hardware:** No minimum RAM, VRAM, GPU model or storage requirement is documented. Physical experiments additionally require compatible optics/SLM hardware.
- **Software:** PyTorch, diffractsim and the repository notebook dependencies; exact Python/OS version support is not published.
- **Platforms:** Python research workflow. No tested Windows/macOS/Linux matrix or guaranteed Apple GPU support is established.

### License, model weights & costs

MPL-2.0 code, with file-level copyleft obligations. Dependencies, example imagery and any optical hardware software have their own terms. [Source 1](https://github.com/rafael-fuente/pinn-shaper/blob/main/LICENSE) [Source 2](https://github.com/rafael-fuente/pinn-shaper/blob/main/README.md) [Source 3](https://arxiv.org/abs/2607.18012)

- **Code:** MPL-2.0
- **Weights:** MPL-2.0 code, with file-level copyleft obligations. Dependencies, example imagery and any optical hardware software have their own terms.
- **Commercial:** The reviewed MPL-2.0 application-code license permits commercial activity subject to its conditions. This does not clear separate model weights, datasets, voices, dependency code, services or proprietary hosts; unrestricted end-to-end commercial use is not established.
- **Cost:** No purchase requirement was identified for the reviewed source code. Hardware, storage and any selected paid provider or proprietary host can incur costs; current service prices were not verified.

### Why it merits attention

A concrete phase-design objective and numerical propagation comparison make the neural contribution identifiable. Documentation/source review only; the application was not installed or run. [Source 1](https://github.com/rafael-fuente/pinn-shaper/blob/main/README.md) [Source 2](https://arxiv.org/abs/2607.18012)

### Limitations

Numerical beam-shaping research, not a plug-and-play holographic display. Physical calibration, illumination limits and measured optical performance remain outside this review. [Source 1](https://github.com/rafael-fuente/pinn-shaper/blob/main/README.md) [Source 2](https://arxiv.org/abs/2607.18012)

### Get the tool

- [Repository](https://github.com/rafael-fuente/pinn-shaper)
- [Documentation](https://github.com/rafael-fuente/pinn-shaper/blob/main/README.md)

## LayoutSculpt

AI architectural visualization and spatial design · Spatial audio & volumetric media · 3D, reconstruction & assets · AI agents for code-authored media production

Repository is within the observed recent-creation window; this first detailed guide does not establish production maturity.

### How it uses AI

A local floorplan workspace using an image-capable Codex model to identify structure, followed by human confirmation and deterministic GLB construction. Turning a 2D plan into an editable spatial concept with furniture, materials and lighting for design discussions or previsualization. [Source](https://github.com/Li-Rui-Zhe/LayoutSculpt/blob/main/README.md)

### Introduction

A local floorplan workspace using an image-capable Codex model to identify structure, followed by human confirmation and deterministic GLB construction. [Source 1](https://github.com/Li-Rui-Zhe/LayoutSculpt/blob/main/README.md)

### What it is good for

Turning a 2D plan into an editable spatial concept with furniture, materials and lighting for design discussions or previsualization. [Source 1](https://github.com/Li-Rui-Zhe/LayoutSculpt/blob/main/README.md)

### Demo & examples

The README shows a real Three.js recording of an original example room. It does not establish recognition accuracy on arbitrary uploaded plans. [Source 1](https://github.com/Li-Rui-Zhe/LayoutSculpt/blob/main/README.md)

### Install

Use the documented route for your platform. These reference steps and commands were not executed in this review. [Source 1](https://github.com/Li-Rui-Zhe/LayoutSculpt/blob/main/README.md)

1. Prepare Node 22+, pnpm, Python 3.11+ and an already installed/signed-in image-capable Codex CLI.
2. Follow the Windows source instructions: install frontend and backend dependencies, then build and start the app.
3. Open localhost:8000 and keep one backend process per data directory.

```sh
pnpm install --frozen-lockfile
```


```sh
python -m venv .venv
```


```sh
.venv\Scripts\python.exe -m pip install -r backend/requirements-dev.txt
```


```sh
pnpm build
```


```sh
pnpm start
```

### First project

Turning a 2D plan into an editable spatial concept with furniture, materials and lighting for design discussions or previsualization. [Source 1](https://github.com/Li-Rui-Zhe/LayoutSculpt/blob/main/README.md)

1. Upload a PNG/JPEG/WebP floorplan and inspect the recognized walls, openings and rooms against the original.
2. Confirm or correct the structure before AI furniture planning and local placement checks.
3. Adjust materials/lights, save a version and export GLB plus structure/consistency reports.
### Hardware & software

Requirements below come from the cited documentation. Undocumented limits are left unknown, and benchmarks are not universal minimums. [Source 1](https://github.com/Li-Rui-Zhe/LayoutSculpt/blob/main/README.md)

- **Hardware:** No numeric RAM/VRAM/storage minimum is documented. Input limit is 20 MB; the browser must support WebGL.
- **Software:** Node 22+, pnpm, Python 3.11+; backend dependencies were tested on Windows with Python 3.13.5. A model/account supporting image input is required.
- **Platforms:** Documented and tested setup is Windows PowerShell. Other source environments are not established as tested; a browser UI does not prove native Mac/Linux support.

### License, model weights & costs

Apache-2.0 application. Codex/model account and service terms are separate; furniture/model assets should retain their own notices. [Source 1](https://github.com/Li-Rui-Zhe/LayoutSculpt/blob/main/LICENSE) [Source 2](https://github.com/Li-Rui-Zhe/LayoutSculpt/blob/main/README.md)

- **Code:** Apache-2.0
- **Weights:** Apache-2.0 application. Codex/model account and service terms are separate; furniture/model assets should retain their own notices.
- **Commercial:** The reviewed Apache-2.0 application-code license permits commercial activity subject to its conditions. This does not clear separate model weights, datasets, voices, dependency code, services or proprietary hosts; unrestricted end-to-end commercial use is not established.
- **Cost:** No purchase requirement was identified for the reviewed source code. Hardware, storage and any selected paid provider or proprietary host can incur costs; current service prices were not verified.

### Why it merits attention

Human structure confirmation and actual GLB consistency checks offer useful controls around AI recognition. Documentation/source review only; the application was not installed or run. [Source 1](https://github.com/Li-Rui-Zhe/LayoutSculpt/blob/main/README.md)

### Limitations

Missing dimensions are estimated. Geometric consistency is not recognition correctness; the output is a concept preview, not a surveyed model or approved construction drawing. [Source 1](https://github.com/Li-Rui-Zhe/LayoutSculpt/blob/main/README.md)

### Get the tool

- [Repository](https://github.com/Li-Rui-Zhe/LayoutSculpt)
- [Documentation](https://github.com/Li-Rui-Zhe/LayoutSculpt/blob/main/README.md)

## playworld / movie2threejs

Photogrammetry, scanning & neural rendering · 3D, reconstruction & assets · Games & production pipelines · Spatial audio & volumetric media · Interactive, immersive & live media

Repository is within the observed recent-creation window; this first detailed guide does not establish production maturity.

### How it uses AI

A research pipeline combining learned camera estimation, Gaussian splatting and SAM 3 masks with a Three.js physics viewer for walkable captured spaces. Prototyping interactive scene captures where users can walk, push a reviewed object or throw a ball inside reconstructed imagery. [Source](https://github.com/rsasaki0109/movie2threejs/blob/master/README.md) [Source](https://rsasaki0109.github.io/movie2threejs/)

### Introduction

A research pipeline combining learned camera estimation, Gaussian splatting and SAM 3 masks with a Three.js physics viewer for walkable captured spaces. [Source 1](https://github.com/rsasaki0109/movie2threejs/blob/master/README.md) [Source 2](https://rsasaki0109.github.io/movie2threejs/)

### What it is good for

Prototyping interactive scene captures where users can walk, push a reviewed object or throw a ball inside reconstructed imagery. [Source 1](https://github.com/rsasaki0109/movie2threejs/blob/master/README.md) [Source 2](https://rsasaki0109.github.io/movie2threejs/)

### Demo & examples

Five live demos use public capture-rig photographs. Three use supplied calibration rather than VGGT; the demos are not proof of a phone-video workflow. [Source 1](https://github.com/rsasaki0109/movie2threejs/blob/master/README.md) [Source 2](https://rsasaki0109.github.io/movie2threejs/)

### Install

Use the documented route for your platform. These reference steps and commands were not executed in this review. [Source 1](https://github.com/rsasaki0109/movie2threejs/blob/master/README.md) [Source 2](https://rsasaki0109.github.io/movie2threejs/)

1. Try the documented synthetic demo through the pip package and a local HTTP server.
2. For real capture use the linked Colab notebook with L4/A100 and approved SAM 3 access, or follow the isolated GPU environments.
3. Keep VGGT, gsplat and SAM 3 dependencies separate as the recipe specifies.

```sh
pip install "playworld @ git+https://github.com/rsasaki0109/movie2threejs.git"
```


```sh
playworld demo --out demo_world
```


```sh
python -m http.server -d demo_world 8000
```

### First project

Prototyping interactive scene captures where users can walk, push a reviewed object or throw a ball inside reconstructed imagery. [Source 1](https://github.com/rsasaki0109/movie2threejs/blob/master/README.md) [Source 2](https://rsasaki0109.github.io/movie2threejs/)

1. Explore the synthetic sample with WASD, jump, push, throw and reset.
2. For real data prepare upright, well-covered capture material and run poses, training, segmentation and world-building stages.
3. Review scale, masks, colliders and unseen surfaces before recording a walkthrough.
### Hardware & software

Requirements below come from the cited documentation. Undocumented limits are left unknown, and benchmarks are not universal minimums. [Source 1](https://github.com/rsasaki0109/movie2threejs/blob/master/README.md) [Source 2](https://rsasaki0109.github.io/movie2threejs/)

- **Hardware:** Real processing was documented on Colab L4; the SAM 3 recipe needs native bf16 and T4 compatibility is unverified. Universal RAM/VRAM/storage minimums are not published; captures and splats can be large.
- **Software:** Python package, separate model environments and browser viewer. Optional scripted recording uses Playwright and media tools; Hugging Face access is needed for gated weights.
- **Platforms:** Browser demos with desktop/touch controls; Colab GPU and a documented Windows client workflow. Native Mac reconstruction is not established.

### License, model weights & costs

MIT application and attributed example capture data. Default VGGT weights are non-commercial; SAM 3 access and terms are independent. [Source 1](https://github.com/rsasaki0109/movie2threejs/blob/master/LICENSE) [Source 2](https://github.com/rsasaki0109/movie2threejs/blob/master/README.md) [Source 3](https://rsasaki0109.github.io/movie2threejs/)

- **Code:** MIT
- **Weights:** MIT application and attributed example capture data. Default VGGT weights are non-commercial; SAM 3 access and terms are independent.
- **Commercial:** The reviewed MIT application-code license permits commercial activity subject to its conditions. This does not clear separate model weights, datasets, voices, dependency code, services or proprietary hosts; unrestricted end-to-end commercial use is not established.
- **Cost:** No purchase requirement was identified for the reviewed source code. Hardware, storage and any selected paid provider or proprietary host can incur costs; current service prices were not verified.

### Why it merits attention

The source distinguishes measured capture demos, synthetic tests and unverified phone input, with visible output artifacts acknowledged. Documentation/source review only; the application was not installed or run. [Source 1](https://github.com/rsasaki0109/movie2threejs/blob/master/README.md) [Source 2](https://rsasaki0109.github.io/movie2threejs/)

### Limitations

Scale assumes camera height; physics and masks are estimates. Unseen surfaces use approximations. Phone-video capture remains unvalidated and visual blur/streaks persist. [Source 1](https://github.com/rsasaki0109/movie2threejs/blob/master/README.md) [Source 2](https://rsasaki0109.github.io/movie2threejs/)

### Get the tool

- [Repository](https://github.com/rsasaki0109/movie2threejs)
- [Documentation](https://github.com/rsasaki0109/movie2threejs/blob/master/README.md)

## Rev2D

Neural rigging and digital puppetry · Avatars, digital humans & lip sync · Motion capture & character animation · Interactive, immersive & live media · AI agents for code-authored media production

Repository is within the observed recent-creation window; this first detailed guide does not establish production maturity.

### How it uses AI

An editable 2D rig/animation toolkit with a local editor and AI-agent bridge for proposing landmarks, rig changes and animation operations in a structured JSON format. Building a small illustrated puppet, inspecting deformations and iterating motion with an external agent while keeping a readable rig. [Source](https://github.com/RevStudio/Rev2D/blob/main/README.md)

### Introduction

An editable 2D rig/animation toolkit with a local editor and AI-agent bridge for proposing landmarks, rig changes and animation operations in a structured JSON format. [Source 1](https://github.com/RevStudio/Rev2D/blob/main/README.md)

### What it is good for

Building a small illustrated puppet, inspecting deformations and iterating motion with an external agent while keeping a readable rig. [Source 1](https://github.com/RevStudio/Rev2D/blob/main/README.md)

### Demo & examples

The README publishes template renders, parameter contact sheets and editor recordings generated by its own tools. [Source 1](https://github.com/RevStudio/Rev2D/blob/main/README.md)

### Install

Use the documented route for your platform. These reference steps and commands were not executed in this review. [Source 1](https://github.com/RevStudio/Rev2D/blob/main/README.md)

1. Clone the source checkout, install dependencies and use Node 22+; no npm release is currently promised.
2. Create a template model and open it with the local edit command.
3. Connect an already configured Codex or Claude Code provider only when AI assistance is desired.

```sh
npm install
```


```sh
node bin/rev2d.js new hero.r2d.json --template hana
```


```sh
node bin/rev2d.js validate hero.r2d.json
```


```sh
node bin/rev2d.js edit hero.r2d.json
```

### First project

Building a small illustrated puppet, inspecting deformations and iterating motion with an external agent while keeping a readable rig. [Source 1](https://github.com/RevStudio/Rev2D/blob/main/README.md)

1. Start with the hana or minimal template and inspect the neutral pose.
2. Request a small rig/motion change, validate the model and review a parameter contact sheet.
3. Preview the animation and export supported data with its conversion report.
### Hardware & software

Requirements below come from the cited documentation. Undocumented limits are left unknown, and benchmarks are not universal minimums. [Source 1](https://github.com/RevStudio/Rev2D/blob/main/README.md)

- **Hardware:** No documented RAM/VRAM/storage minimum. Browser rendering needs the appropriate graphics support; local rendering is distinct from external-model inference.
- **Software:** Node 22+, Git and npm dependencies; editor/agent bridge and chosen model client. Chrome/FFmpeg are needed for the documented demo capture tools, not every edit.
- **Platforms:** Source Node/browser workflow; a complete tested OS matrix is not documented. Windows-specific media-tool configuration is described.

### License, model weights & costs

MIT code. External agent services and imported Spine/Live2D assets/runtimes have separate terms; format interchange does not transfer their licenses. [Source 1](https://github.com/RevStudio/Rev2D/blob/main/LICENSE) [Source 2](https://github.com/RevStudio/Rev2D/blob/main/README.md)

- **Code:** MIT
- **Weights:** MIT code. External agent services and imported Spine/Live2D assets/runtimes have separate terms; format interchange does not transfer their licenses.
- **Commercial:** The reviewed MIT application-code license permits commercial activity subject to its conditions. This does not clear separate model weights, datasets, voices, dependency code, services or proprietary hosts; unrestricted end-to-end commercial use is not established.
- **Cost:** No purchase requirement was identified for the reviewed source code. Hardware, storage and any selected paid provider or proprietary host can incur costs; current service prices were not verified.

### Why it merits attention

Validation, contact sheets and explicit approximation reports make agent-authored rig changes reviewable. Documentation/source review only; the application was not installed or run. [Source 1](https://github.com/RevStudio/Rev2D/blob/main/README.md)

### Limitations

v0.1 experiment. Live2D .moc3 art/deformers are unsupported; JSON motion interchange is narrower. Front-facing busts are the best-documented avatar input, and conversions can lose features. [Source 1](https://github.com/RevStudio/Rev2D/blob/main/README.md)

### Get the tool

- [Repository](https://github.com/RevStudio/Rev2D)
- [Documentation](https://github.com/RevStudio/Rev2D/blob/main/README.md)

## AvatarScript

Avatars, digital humans & lip sync · Video, animation & film · Neural rigging and digital puppetry · Creative publishing & presentation

Repository is within the observed recent-creation window; this first detailed guide does not establish production maturity.

### How it uses AI

A script/compiler/rendering pipeline that combines neural TTS or speech alignment with mesh-avatar visemes, emotions and gestures to produce a video. Creating a narrated illustrated presenter from a short Japanese or English script and an existing avatar package. [Source](https://github.com/receptron/avatarscript/blob/main/README.md)

### Introduction

A script/compiler/rendering pipeline that combines neural TTS or speech alignment with mesh-avatar visemes, emotions and gestures to produce a video. [Source 1](https://github.com/receptron/avatarscript/blob/main/README.md)

### What it is good for

Creating a narrated illustrated presenter from a short Japanese or English script and an existing avatar package. [Source 1](https://github.com/receptron/avatarscript/blob/main/README.md)

### Demo & examples

The repository supplies a sample avatar and script. Source CI smoke runs are maintainer evidence, not a rendered demonstration performed here. [Source 1](https://github.com/receptron/avatarscript/blob/main/README.md)

### Install

Use the documented route for your platform. These reference steps and commands were not executed in this review. [Source 1](https://github.com/receptron/avatarscript/blob/main/README.md)

1. Install avatarscript with Node 22.18+ and FFmpeg available.
2. Configure a chosen TTS provider through a private environment or .env file; OpenAI/Gemini alignment also needs onnxruntime-node and its model download.
3. Use a repository sample avatar or the documented remote avatar package; it is not bundled in the npm package.

```sh
npm install avatarscript
```


```sh
npm install onnxruntime-node
```


```sh
npx avatarscript make --avatar avatars/ani --script examples/hello-ja.avs --tts elevenlabs -o out/hello-ja.mp4
```

### First project

Creating a narrated illustrated presenter from a short Japanese or English script and an existing avatar package. [Source 1](https://github.com/receptron/avatarscript/blob/main/README.md)

1. Write a short .avs file with language, emotion, pauses and motion tags.
2. Render with the selected voice and inspect WAV, score JSON and MP4 outputs.
3. Correct pronunciation/timing and use WebM or ProRes 4444 when alpha is needed.
### Hardware & software

Requirements below come from the cited documentation. Undocumented limits are left unknown, and benchmarks are not universal minimums. [Source 1](https://github.com/receptron/avatarscript/blob/main/README.md)

- **Hardware:** Optional forced-alignment model is about 290 MB. Numeric RAM/VRAM and total storage minimums are not documented.
- **Software:** Node 22.18+, FFmpeg, headless browser rendering and a configured TTS provider. ONNX runtime is optional for specific provider alignment paths.
- **Platforms:** Source/package tests are documented on Ubuntu and macOS. A fully verified Windows matrix is not established.

### License, model weights & costs

MIT application, bundled mesh engine and documented sample avatar. TTS APIs, voice rights and alignment-model terms are separate. [Source 1](https://github.com/receptron/avatarscript/blob/main/LICENSE) [Source 2](https://github.com/receptron/avatarscript/blob/main/README.md)

- **Code:** MIT
- **Weights:** MIT application, bundled mesh engine and documented sample avatar. TTS APIs, voice rights and alignment-model terms are separate.
- **Commercial:** The reviewed MIT application-code license permits commercial activity subject to its conditions. This does not clear separate model weights, datasets, voices, dependency code, services or proprietary hosts; unrestricted end-to-end commercial use is not established.
- **Cost:** No purchase requirement was identified for the reviewed source code. Hardware, storage and any selected paid provider or proprietary host can incur costs; current service prices were not verified.

### Why it merits attention

A structured script and segment cache allow precise revisions without resynthesizing the whole narration. Documentation/source review only; the application was not installed or run. [Source 1](https://github.com/receptron/avatarscript/blob/main/README.md)

### Limitations

Early release. Automatic LLM scriptwriting, gaze and emphasis rendering are not implemented; the offline mock produces a buzz, not neural speech. Other languages use less specific viseme handling. [Source 1](https://github.com/receptron/avatarscript/blob/main/README.md)

### Get the tool

- [Repository](https://github.com/receptron/avatarscript)
- [Documentation](https://github.com/receptron/avatarscript/blob/main/README.md)

## Troupe

Storyboarding, narrative & comics · Video, animation & film · Audio, music & voice · Browser tools & web media

Repository is within the observed recent-creation window; this first detailed guide does not establish production maturity.

### How it uses AI

A short-video studio combining scripts, cast cards, neural Kokoro narration and optional language/image/video models in browser or self-hosted editions. Producing voiced, captioned story drafts on CPU, then optionally replacing still imagery with generated media from local or cloud providers. [Source](https://github.com/maxgfr/troupe/blob/main/README.md) [Source](https://maxgfr.github.io/troupe/)

### Introduction

A short-video studio combining scripts, cast cards, neural Kokoro narration and optional language/image/video models in browser or self-hosted editions. [Source 1](https://github.com/maxgfr/troupe/blob/main/README.md) [Source 2](https://maxgfr.github.io/troupe/)

### What it is good for

Producing voiced, captioned story drafts on CPU, then optionally replacing still imagery with generated media from local or cloud providers. [Source 1](https://github.com/maxgfr/troupe/blob/main/README.md) [Source 2](https://maxgfr.github.io/troupe/)

### Demo & examples

The live browser edition and a recorded tour show a short script-to-download workflow; the tour accelerates marked waits. [Source 1](https://github.com/maxgfr/troupe/blob/main/README.md) [Source 2](https://maxgfr.github.io/troupe/)

### Install

Use the documented route for your platform. These reference steps and commands were not executed in this review. [Source 1](https://github.com/maxgfr/troupe/blob/main/README.md) [Source 2](https://maxgfr.github.io/troupe/)

1. Open the browser edition in recent Chrome/Edge for the smallest setup.
2. For local/cloud model servers clone the repository and start the Docker Compose studio.
3. The Docker route downloads qwen3:4b and Kokoro voices; retrieve the generated access code from the app logs.

```sh
docker compose up -d --wait
```

### First project

Producing voiced, captioned story drafts on CPU, then optionally replacing still imagery with generated media from local or cloud providers. [Source 1](https://github.com/maxgfr/troupe/blob/main/README.md) [Source 2](https://maxgfr.github.io/troupe/)

1. Create a short project, cast a character and write a few lines.
2. Use script chat if a supported model is configured, then render with Kokoro.
3. Review voice/captions and export MP4; select a separate image/video backend only when desired.
### Hardware & software

Requirements below come from the cited documentation. Undocumented limits are left unknown, and benchmarks are not universal minimums. [Source 1](https://github.com/maxgfr/troupe/blob/main/README.md) [Source 2](https://maxgfr.github.io/troupe/)

- **Hardware:** CPU narration/rendering is documented. Docker downloads include roughly 2.5 GB chat weights and 90 MB voices; total RAM/VRAM/disk minimums are not stated. Browser chat needs WebGPU.
- **Software:** Recent Chrome/Edge for browser rendering; Docker/Compose for the full studio. Optional Ollama, ComfyUI or paid provider integrations have additional requirements.
- **Platforms:** Static browser edition plus Docker self-hosting. Specific tested host OS versions are not published; web access is distinct from local inference support.

### License, model weights & costs

MIT studio; Kokoro, chat/video models, cast assets and providers retain their own terms. Cloud generation can cost money despite the studio having no subscription. [Source 1](https://github.com/maxgfr/troupe/blob/main/LICENSE) [Source 2](https://github.com/maxgfr/troupe/blob/main/README.md) [Source 3](https://maxgfr.github.io/troupe/)

- **Code:** MIT
- **Weights:** MIT studio; Kokoro, chat/video models, cast assets and providers retain their own terms. Cloud generation can cost money despite the studio having no subscription.
- **Commercial:** The reviewed MIT application-code license permits commercial activity subject to its conditions. This does not clear separate model weights, datasets, voices, dependency code, services or proprietary hosts; unrestricted end-to-end commercial use is not established.
- **Cost:** No purchase requirement was identified for the reviewed source code. Hardware, storage and any selected paid provider or proprietary host can incur costs; current service prices were not verified.

### Why it merits attention

A documented CPU first-run route and an explicit separation between browser and self-hosted capabilities reduce setup ambiguity. Documentation/source review only; the application was not installed or run. [Source 1](https://github.com/maxgfr/troupe/blob/main/README.md) [Source 2](https://maxgfr.github.io/troupe/)

### Limitations

The local renderer creates narrated/captioned still-card videos, not animated acting. Browser storage can be lost without backups; cloud/local server integrations require the self-hosted edition. [Source 1](https://github.com/maxgfr/troupe/blob/main/README.md) [Source 2](https://maxgfr.github.io/troupe/)

### Get the tool

- [Repository](https://github.com/maxgfr/troupe)
- [Documentation](https://github.com/maxgfr/troupe/blob/main/README.md)

## OpenGestureXR

WebXR, VR & AR · Interactive, immersive & live media · Neural rigging and digital puppetry · Accessible media & assistive creation

Completed a previously screened discovery with its first detailed guide; this is not a new-launch claim.

### How it uses AI

A webcam hand-interaction prototype using MediaPipe landmarks, rule-based gestures or a trainable ONNX classifier, and a Unity client. Prototyping grab, pinch, point and release interactions for an installation or puppet/object control study before headset integration. [Source](https://github.com/raechao93/OpenGestureXR/blob/main/README.md)

### Introduction

A webcam hand-interaction prototype using MediaPipe landmarks, rule-based gestures or a trainable ONNX classifier, and a Unity client. [Source 1](https://github.com/raechao93/OpenGestureXR/blob/main/README.md)

### What it is good for

Prototyping grab, pinch, point and release interactions for an installation or puppet/object control study before headset integration. [Source 1](https://github.com/raechao93/OpenGestureXR/blob/main/README.md)

### Demo & examples

The README describes a Unity demo and the webcam pipeline; native Quest/Pico/HoloLens support is a roadmap goal. [Source 1](https://github.com/raechao93/OpenGestureXR/blob/main/README.md)

### Install

Use the documented route for your platform. These reference steps and commands were not executed in this review. [Source 1](https://github.com/raechao93/OpenGestureXR/blob/main/README.md)

1. Use the current repository URL rather than the stale ARMAX clone example in its README.
2. Prepare Python 3.10+, install requirements.txt and start the FastAPI service.
3. Copy the documented Unity scripts into a project and configure the client/interactor components.

```sh
pip install -r requirements.txt
```


```sh
uvicorn gesture_api.server.main:app --reload
```

### First project

Prototyping grab, pinch, point and release interactions for an installation or puppet/object control study before headset integration. [Source 1](https://github.com/raechao93/OpenGestureXR/blob/main/README.md)

1. Check hand landmarks and gesture output with a webcam.
2. Connect one Unity object and tune smoothing/confidence thresholds.
3. Collect labeled gesture samples and train/export an ONNX model if the rule-based classifier is insufficient.
### Hardware & software

Requirements below come from the cited documentation. Undocumented limits are left unknown, and benchmarks are not universal minimums. [Source 1](https://github.com/raechao93/OpenGestureXR/blob/main/README.md)

- **Hardware:** A webcam is the established input. RAM, GPU/VRAM, storage and headset hardware minimums are not documented.
- **Software:** Python 3.10+, MediaPipe, FastAPI, optional PyTorch/ONNX training and Unity. A Unity version requirement is not published.
- **Platforms:** Webcam/Python/Unity prototype. OpenXR abstraction is present, but native Quest, Pico, HoloLens and other device support is not verified.

### License, model weights & costs

MIT code; MediaPipe models, Unity host terms and trained-model/data permissions are independent. [Source 1](https://github.com/raechao93/OpenGestureXR/blob/main/LICENSE) [Source 2](https://github.com/raechao93/OpenGestureXR/blob/main/README.md)

- **Code:** MIT
- **Weights:** MIT code; MediaPipe models, Unity host terms and trained-model/data permissions are independent.
- **Commercial:** The reviewed MIT application-code license permits commercial activity subject to its conditions. This does not clear separate model weights, datasets, voices, dependency code, services or proprietary hosts; unrestricted end-to-end commercial use is not established.
- **Cost:** No purchase requirement was identified for the reviewed source code. Hardware, storage and any selected paid provider or proprietary host can incur costs; current service prices were not verified.

### Why it merits attention

The actual hand landmark pipeline and a train/export route give it a concrete AI contribution despite rule-based default gesture labels. Documentation/source review only; the application was not installed or run. [Source 1](https://github.com/raechao93/OpenGestureXR/blob/main/README.md)

### Limitations

Prototype with stale clone instructions. Unity’s named WebSocket mode currently uses fast HTTP polling unless a separate WebSocket client is added. Reported frame rates were not reproduced. [Source 1](https://github.com/raechao93/OpenGestureXR/blob/main/README.md)

### Get the tool

- [Repository](https://github.com/raechao93/OpenGestureXR)
- [Documentation](https://github.com/raechao93/OpenGestureXR/blob/main/README.md)

## KhmerFontFactory

Typography, fonts & layout · Vector graphics, illustration & textures · Browser tools & web media

Completed a previously screened discovery with its first detailed guide; this is not a new-launch claim.

### How it uses AI

A browser font-design experiment using a few-shot MXFont-style ONNX model to synthesize Khmer glyphs from style references, then vectorize and package them. Exploring a coherent Khmer type style from limited examples and reviewing generated outlines before font production. [Source](https://github.com/lienghongky/cxm-kff/blob/main/README.md)

### Introduction

A browser font-design experiment using a few-shot MXFont-style ONNX model to synthesize Khmer glyphs from style references, then vectorize and package them. [Source 1](https://github.com/lienghongky/cxm-kff/blob/main/README.md)

### What it is good for

Exploring a coherent Khmer type style from limited examples and reviewing generated outlines before font production. [Source 1](https://github.com/lienghongky/cxm-kff/blob/main/README.md)

### Demo & examples

The README provides the interface/workflow and links a hosted demo; that demo could not be fetched by the research browser today. [Source 1](https://github.com/lienghongky/cxm-kff/blob/main/README.md)

### Install

Use the documented route for your platform. These reference steps and commands were not executed in this review. [Source 1](https://github.com/lienghongky/cxm-kff/blob/main/README.md)

1. Clone the project and install its Node/npm dependencies.
2. Run the development server or build the browser application.
3. Prepare the documented model/assets and reference glyphs; no particular Node version or full resource budget is published in the overview.

```sh
npm install
```


```sh
npm run dev
```


```sh
npm run build
```

### First project

Exploring a coherent Khmer type style from limited examples and reviewing generated outlines before font production. [Source 1](https://github.com/lienghongky/cxm-kff/blob/main/README.md)

1. Supply style references and generate a small glyph set.
2. Inspect Khmer marks, spacing and shapes, then vectorize with the supplied VTracer path.
3. Review outlines/metrics before exporting the OpenType/WOFF2 font.
### Hardware & software

Requirements below come from the cited documentation. Undocumented limits are left unknown, and benchmarks are not universal minimums. [Source 1](https://github.com/lienghongky/cxm-kff/blob/main/README.md)

- **Hardware:** RAM/VRAM and disk minimums are not documented. Browser WASM/thread support and model memory affect usability.
- **Software:** Node/npm for source, ONNX browser inference, VTracer and Pyodide workers for font tooling.
- **Platforms:** Browser application; exact tested browsers/OS versions are not documented. Browser operation does not establish identical performance on mobile.

### License, model weights & costs

MIT code. The model-weight license was not established from the README; source glyphs and generated font rights require separate review. [Source 1](https://github.com/lienghongky/cxm-kff/blob/main/LICENSE) [Source 2](https://github.com/lienghongky/cxm-kff/blob/main/README.md)

- **Code:** MIT
- **Weights:** MIT code. The model-weight license was not established from the README; source glyphs and generated font rights require separate review.
- **Commercial:** The reviewed MIT application-code license permits commercial activity subject to its conditions. This does not clear separate model weights, datasets, voices, dependency code, services or proprietary hosts; unrestricted end-to-end commercial use is not established.
- **Cost:** No purchase requirement was identified for the reviewed source code. Hardware, storage and any selected paid provider or proprietary host can incur costs; current service prices were not verified.

### Why it merits attention

The chain from learned style transfer to editable vectors and a font container is directly relevant to typography work. Documentation/source review only; the application was not installed or run. [Source 1](https://github.com/lienghongky/cxm-kff/blob/main/README.md)

### Limitations

An exported font is not evidence of Khmer linguistic correctness or high-quality shaping. Model permissions and glyph quality remain unresolved beyond the source-code review. [Source 1](https://github.com/lienghongky/cxm-kff/blob/main/README.md)

### Get the tool

- [Repository](https://github.com/lienghongky/cxm-kff)
- [Documentation](https://github.com/lienghongky/cxm-kff/blob/main/README.md)

## AI Texture for Substance 3D Painter

3D, reconstruction & assets · VFX, compositing & relighting · Images & design

Repository is within the observed recent-creation window; this first detailed guide does not establish production maturity.

### How it uses AI

A Painter plugin that sends depth-conditioned views through an SDXL/ControlNet ComfyUI workflow and projects generated textures back onto a mesh. Rapid texture/material studies on a 3D asset while preserving Painter’s layer-based editing workflow. [Source](https://github.com/baileychen-dot/ai-texture-sp-tools/blob/main/README.md)

### Introduction

A Painter plugin that sends depth-conditioned views through an SDXL/ControlNet ComfyUI workflow and projects generated textures back onto a mesh. [Source 1](https://github.com/baileychen-dot/ai-texture-sp-tools/blob/main/README.md)

### What it is good for

Rapid texture/material studies on a 3D asset while preserving Painter’s layer-based editing workflow. [Source 1](https://github.com/baileychen-dot/ai-texture-sp-tools/blob/main/README.md)

### Demo & examples

The README shows workflow screenshots and links an artist portfolio; the portfolio page was inaccessible during this review. [Source 1](https://github.com/baileychen-dot/ai-texture-sp-tools/blob/main/README.md)

### Install

Use the documented route for your platform. These reference steps and commands were not executed in this review. [Source 1](https://github.com/baileychen-dot/ai-texture-sp-tools/blob/main/README.md)

1. Use the documented Substance 3D Painter 11.1.2/PySide6 setup and copy the plugin into its Python plugins folder.
2. Prepare ComfyUI with the documented Hunyuan3DWrapper-related nodes, SDXL checkpoint and ControlNet/depth components.
3. Reload/enable the plugin and connect it to the running ComfyUI service.
### First project

Rapid texture/material studies on a 3D asset while preserving Painter’s layer-based editing workflow. [Source 1](https://github.com/baileychen-dot/ai-texture-sp-tools/blob/main/README.md)

1. Open a mesh and choose the documented multi-view camera set.
2. Enter a material prompt and generate depth-guided views.
3. Project to layers, inspect seams/occluded areas and paint corrections before export.
### Hardware & software

Requirements below come from the cited documentation. Undocumented limits are left unknown, and benchmarks are not universal minimums. [Source 1](https://github.com/baileychen-dot/ai-texture-sp-tools/blob/main/README.md)

- **Hardware:** No plugin-specific RAM/VRAM/storage minimum is published; Painter and the ComfyUI models determine needs.
- **Software:** Paid Adobe Substance 3D Painter, tested 11.1.2, PySide6 plugin API, ComfyUI and the selected SDXL/ControlNet workflow.
- **Platforms:** Painter host workflow; the README does not establish a tested Windows/macOS matrix or Mac inference performance.

### License, model weights & costs

MIT plugin. Adobe’s proprietary host, SDXL/ControlNet model terms and custom-node licenses are separate; MIT does not include a Painter license. [Source 1](https://github.com/baileychen-dot/ai-texture-sp-tools/blob/main/LICENSE) [Source 2](https://github.com/baileychen-dot/ai-texture-sp-tools/blob/main/README.md)

- **Code:** MIT
- **Weights:** MIT plugin. Adobe’s proprietary host, SDXL/ControlNet model terms and custom-node licenses are separate; MIT does not include a Painter license.
- **Commercial:** The reviewed MIT application-code license permits commercial activity subject to its conditions. This does not clear separate model weights, datasets, voices, dependency code, services or proprietary hosts; unrestricted end-to-end commercial use is not established.
- **Cost:** No purchase requirement was identified for the reviewed source code. Hardware, storage and any selected paid provider or proprietary host can incur costs; current service prices were not verified.

### Why it merits attention

Depth conditioning and retained projection layers give an artist concrete handles for fixing generated texture errors. Documentation/source review only; the application was not installed or run. [Source 1](https://github.com/baileychen-dot/ai-texture-sp-tools/blob/main/README.md)

### Limitations

Seams, view inconsistency and hidden surfaces need manual cleanup. Manual image projection is not itself AI; the neural path requires the configured backend. [Source 1](https://github.com/baileychen-dot/ai-texture-sp-tools/blob/main/README.md)

### Get the tool

- [Repository](https://github.com/baileychen-dot/ai-texture-sp-tools)
- [Documentation](https://github.com/baileychen-dot/ai-texture-sp-tools/blob/main/README.md)

## Qwen Image Studio

Images & design · Photography, restoration & color · Editing, captions & post-production

Repository is within the observed recent-creation window; this first detailed guide does not establish production maturity.

### How it uses AI

A Qwen Image 2.1 CLI and local studio for generation, reference-image editing and optional prompt enhancement, designed around Apple Silicon MPS. Running controlled local image/edit experiments while keeping prompts, references and generated takes in a local session. [Source](https://github.com/janishar/qwen-image-2.1-studio/blob/main/README.md)

### Introduction

A Qwen Image 2.1 CLI and local studio for generation, reference-image editing and optional prompt enhancement, designed around Apple Silicon MPS. [Source 1](https://github.com/janishar/qwen-image-2.1-studio/blob/main/README.md)

### What it is good for

Running controlled local image/edit experiments while keeping prompts, references and generated takes in a local session. [Source 1](https://github.com/janishar/qwen-image-2.1-studio/blob/main/README.md)

### Demo & examples

The README documents the studio and CLI controls. No model was downloaded or image generated in this review. [Source 1](https://github.com/janishar/qwen-image-2.1-studio/blob/main/README.md)

### Install

Use the documented route for your platform. These reference steps and commands were not executed in this review. [Source 1](https://github.com/janishar/qwen-image-2.1-studio/blob/main/README.md)

1. For the complete UI use the documented helmstudio launcher and install the studio from its library.
2. For a checkout, use uv sync and the documented helm-backed web/run.sh route; the UI requires helmstudio.
3. Download or point to the Qwen image weights. Prompt-enhancer weights are optional for CLI use and are loaded separately.

```sh
uv sync
```


```sh
uv run qwen-image-2-1 "A neon shop sign that reads QWEN" -m ~/models/Qwen-Image-2.1
```

### First project

Running controlled local image/edit experiments while keeping prompts, references and generated takes in a local session. [Source 1](https://github.com/janishar/qwen-image-2.1-studio/blob/main/README.md)

1. Start with a short CLI prompt or open the studio and select the model path.
2. Add references or enable the matching text/image prompt enhancer if needed.
3. Generate, inspect the PNG and save the prompt/seed/settings with the chosen take.
### Hardware & software

Requirements below come from the cited documentation. Undocumented limits are left unknown, and benchmarks are not universal minimums. [Source 1](https://github.com/janishar/qwen-image-2.1-studio/blob/main/README.md)

- **Hardware:** Built and tested on a 64 GB Apple Silicon Mac. Image bf16 weights total about 30 GB; each optional enhancer about 18 GB, roughly 67 GB for all launcher downloads. Enhancer memory is freed before the image model loads; 64 GB is the documented test setup, not a proved universal minimum.
- **Software:** Python 3.12+, uv, Git-pinned diffusers and model files; helmstudio is required for the web studio, not the standalone generation CLI.
- **Platforms:** macOS/Apple Silicon is the tested route. CUDA and CPU flags exist but are explicitly untested; no Windows/Linux support guarantee follows from them.

### License, model weights & costs

MIT application. Qwen Image 2.1 and prompt-enhancer weights have separate terms; the source license does not make those weights unrestricted. [Source 1](https://github.com/janishar/qwen-image-2.1-studio/blob/main/LICENSE) [Source 2](https://github.com/janishar/qwen-image-2.1-studio/blob/main/README.md)

- **Code:** MIT
- **Weights:** MIT application. Qwen Image 2.1 and prompt-enhancer weights have separate terms; the source license does not make those weights unrestricted.
- **Commercial:** The reviewed MIT application-code license permits commercial activity subject to its conditions. This does not clear separate model weights, datasets, voices, dependency code, services or proprietary hosts; unrestricted end-to-end commercial use is not established.
- **Cost:** No purchase requirement was identified for the reviewed source code. Hardware, storage and any selected paid provider or proprietary host can incur costs; current service prices were not verified.

### Why it merits attention

The documentation quantifies weight sizes and distinguishes the launcher/UI route from direct CLI inference. Documentation/source review only; the application was not installed or run. [Source 1](https://github.com/janishar/qwen-image-2.1-studio/blob/main/README.md)

### Limitations

Large memory/storage footprint and a fresh model load per render. RGBA file output does not by itself mean the image has meaningful transparency. Published peak-RAM configuration is an estimate. [Source 1](https://github.com/janishar/qwen-image-2.1-studio/blob/main/README.md)

### Get the tool

- [Repository](https://github.com/janishar/qwen-image-2.1-studio)
- [Documentation](https://github.com/janishar/qwen-image-2.1-studio/blob/main/README.md)

## TurboDiffusion

Video, animation & film · Computational art & creative coding · VFX, compositing & relighting

Completed a previously screened discovery with its first detailed guide; this is not a new-launch claim.

### How it uses AI

A research framework accelerating Wan diffusion-video generation with sparse attention, distillation and quantized checkpoint options. Reducing iteration time for technically managed text-to-video or image-to-video experiments on supported NVIDIA hardware. [Source](https://github.com/thu-ml/TurboDiffusion/blob/main/README.md) [Source](https://arxiv.org/abs/2512.16093)

### Introduction

A research framework accelerating Wan diffusion-video generation with sparse attention, distillation and quantized checkpoint options. [Source 1](https://github.com/thu-ml/TurboDiffusion/blob/main/README.md) [Source 2](https://arxiv.org/abs/2512.16093)

### What it is good for

Reducing iteration time for technically managed text-to-video or image-to-video experiments on supported NVIDIA hardware. [Source 1](https://github.com/thu-ml/TurboDiffusion/blob/main/README.md) [Source 2](https://arxiv.org/abs/2512.16093)

### Demo & examples

The README shows a five-second generated example and benchmark tables. Its advertised speedups exclude text encoding and VAE decoding in the stated E2E comparison. [Source 1](https://github.com/thu-ml/TurboDiffusion/blob/main/README.md) [Source 2](https://arxiv.org/abs/2512.16093)

### Install

Use the documented route for your platform. These reference steps and commands were not executed in this review. [Source 1](https://github.com/thu-ml/TurboDiffusion/blob/main/README.md) [Source 2](https://arxiv.org/abs/2512.16093)

1. Create the documented environment, with Python 3.12 as the example and PyTorch 2.8 recommended.
2. Install turbodiffusion without build isolation and the optional SpargeAttn component for SageSLA.
3. Download the appropriate Wan text encoder/VAE and Turbo checkpoint; choose quantized versus unquantized files according to the documented GPU route.

```sh
pip install turbodiffusion --no-build-isolation
```

### First project

Reducing iteration time for technically managed text-to-video or image-to-video experiments on supported NVIDIA hardware. [Source 1](https://github.com/thu-ml/TurboDiffusion/blob/main/README.md) [Source 2](https://arxiv.org/abs/2512.16093)

1. Begin with the 1.3B 480p text-to-video example and a detailed English prompt.
2. Set checkpoint paths and generation parameters in the provided inference command.
3. Compare the output and total workflow time, including loading/encoding/decoding, before scaling resolution or model size.
### Hardware & software

Requirements below come from the cited documentation. Undocumented limits are left unknown, and benchmarks are not universal minimums. [Source 1](https://github.com/thu-ml/TurboDiffusion/blob/main/README.md) [Source 2](https://arxiv.org/abs/2512.16093)

- **Hardware:** Benchmarks use RTX 5090; quantized instructions also name RTX 4090-class GPUs. Unquantized examples target more than 40 GB GPU memory. A universal RAM/VRAM minimum or total storage budget is not stated.
- **Software:** Python >=3.9, PyTorch >=2.7 with 2.8 recommended, CUDA-compatible custom components and separate checkpoint files.
- **Platforms:** NVIDIA/CUDA research workflow. Native Mac/MPS and a tested Windows version matrix are not established.

### License, model weights & costs

Apache-2.0 source. Wan/Turbo checkpoints and any optional LTX-related branch have independent model terms; check the exact selected checkpoint. [Source 1](https://github.com/thu-ml/TurboDiffusion/blob/main/LICENSE) [Source 2](https://github.com/thu-ml/TurboDiffusion/blob/main/README.md) [Source 3](https://arxiv.org/abs/2512.16093)

- **Code:** Apache-2.0
- **Weights:** Apache-2.0 source. Wan/Turbo checkpoints and any optional LTX-related branch have independent model terms; check the exact selected checkpoint.
- **Commercial:** The reviewed Apache-2.0 application-code license permits commercial activity subject to its conditions. This does not clear separate model weights, datasets, voices, dependency code, services or proprietary hosts; unrestricted end-to-end commercial use is not established.
- **Cost:** No purchase requirement was identified for the reviewed source code. Hardware, storage and any selected paid provider or proprietary host can incur costs; current service prices were not verified.

### Why it merits attention

Public scripts, explicit quantization routes and disclosed benchmark scope make the acceleration claim inspectable. Documentation/source review only; the application was not installed or run. [Source 1](https://github.com/thu-ml/TurboDiffusion/blob/main/README.md) [Source 2](https://arxiv.org/abs/2512.16093)

### Limitations

Models were trained on long English prompts; other prompt styles may need adaptation. Fast denoising does not prove equal end-to-end speed or output quality on another GPU. [Source 1](https://github.com/thu-ml/TurboDiffusion/blob/main/README.md) [Source 2](https://arxiv.org/abs/2512.16093)

### Get the tool

- [Repository](https://github.com/thu-ml/TurboDiffusion)
- [Documentation](https://github.com/thu-ml/TurboDiffusion/blob/main/README.md)

## JoyAI-VL-Interaction

Interactive, immersive & live media · Physical, robotic & kinetic installations · Video, animation & film · Performance, projection & stage media

Completed a previously screened discovery with its first detailed guide; this is not a new-launch claim.

### How it uses AI

An 8B video-language research system that watches a stream and learns when to speak, remain silent or delegate a task, with optional speech input/output. Prototyping responsive video commentary or a scene-aware installation that reacts to changing visual events. [Source](https://github.com/jd-opensource/JoyAI-VL-Interaction/blob/main/README.md) [Source](https://github.com/jd-opensource/JoyAI-VL-Interaction/blob/main/doc/getting_started.md) [Source](https://joyai-vl-video-future-academy-jd.github.io/JoyAI-VL-Interaction/)

### Introduction

An 8B video-language research system that watches a stream and learns when to speak, remain silent or delegate a task, with optional speech input/output. [Source 1](https://github.com/jd-opensource/JoyAI-VL-Interaction/blob/main/README.md) [Source 2](https://github.com/jd-opensource/JoyAI-VL-Interaction/blob/main/doc/getting_started.md) [Source 3](https://joyai-vl-video-future-academy-jd.github.io/JoyAI-VL-Interaction/)

### What it is good for

Prototyping responsive video commentary or a scene-aware installation that reacts to changing visual events. [Source 1](https://github.com/jd-opensource/JoyAI-VL-Interaction/blob/main/README.md) [Source 2](https://github.com/jd-opensource/JoyAI-VL-Interaction/blob/main/doc/getting_started.md) [Source 3](https://joyai-vl-video-future-academy-jd.github.io/JoyAI-VL-Interaction/)

### Demo & examples

The official project site publishes live-commentary examples, including pet streams. These are author demonstrations, not evidence of dependable real-world monitoring. [Source 1](https://github.com/jd-opensource/JoyAI-VL-Interaction/blob/main/README.md) [Source 2](https://github.com/jd-opensource/JoyAI-VL-Interaction/blob/main/doc/getting_started.md) [Source 3](https://joyai-vl-video-future-academy-jd.github.io/JoyAI-VL-Interaction/)

### Install

Use the documented route for your platform. These reference steps and commands were not executed in this review. [Source 1](https://github.com/jd-opensource/JoyAI-VL-Interaction/blob/main/README.md) [Source 2](https://github.com/jd-opensource/JoyAI-VL-Interaction/blob/main/doc/getting_started.md) [Source 3](https://joyai-vl-video-future-academy-jd.github.io/JoyAI-VL-Interaction/)

1. Use the documented Linux/NVIDIA environment and install the core dependencies.
2. Download the main interaction and summary models; install ASR/TTS only if the project needs spoken interaction.
3. Start the minimal two-service route and open the local HTTPS web UI on port 8099 before considering optional background-agent delegation.

```sh
./install/install.sh --with-all
```


```sh
./install/download-models.sh --all
```


```sh
./services/scripts/run.sh minimal
```

### First project

Prototyping responsive video commentary or a scene-aware installation that reacts to changing visual events. [Source 1](https://github.com/jd-opensource/JoyAI-VL-Interaction/blob/main/README.md) [Source 2](https://github.com/jd-opensource/JoyAI-VL-Interaction/blob/main/doc/getting_started.md) [Source 3](https://joyai-vl-video-future-academy-jd.github.io/JoyAI-VL-Interaction/)

1. Select a short controlled camera/video input and define the desired commentary style.
2. Observe whether the model responds at useful moments and inspect mistakes/silences.
3. Enable speech services separately and keep sensitive or consequential environments outside an unvalidated prototype.
### Hardware & software

Requirements below come from the cited documentation. Undocumented limits are left unknown, and benchmarks are not universal minimums. [Source 1](https://github.com/jd-opensource/JoyAI-VL-Interaction/blob/main/README.md) [Source 2](https://github.com/jd-opensource/JoyAI-VL-Interaction/blob/main/doc/getting_started.md) [Source 3](https://joyai-vl-video-future-academy-jd.github.io/JoyAI-VL-Interaction/)

- **Hardware:** Linux with NVIDIA GPUs, with Hopper tested; the README also points to tuned 3090/5090 configurations. CUDA 12.x and driver 535+ are documented. RAM, minimum VRAM and disk totals are not specified in the getting-started guide.
- **Software:** Python 3.12 recommended, uv/pip, main/summary model files and optional Qwen ASR/TTS runtimes.
- **Platforms:** Linux/NVIDIA is the documented deployment route. Windows and macOS native inference are not established; the browser is a client.

### License, model weights & costs

Apache-2.0 source. Main and auxiliary model/data terms are separate; optional JD Cloud and external-agent service usage has its own conditions/costs. [Source 1](https://github.com/jd-opensource/JoyAI-VL-Interaction/blob/main/LICENSE) [Source 2](https://github.com/jd-opensource/JoyAI-VL-Interaction/blob/main/README.md) [Source 3](https://github.com/jd-opensource/JoyAI-VL-Interaction/blob/main/doc/getting_started.md) [Source 4](https://joyai-vl-video-future-academy-jd.github.io/JoyAI-VL-Interaction/)

- **Code:** Apache-2.0
- **Weights:** Apache-2.0 source. Main and auxiliary model/data terms are separate; optional JD Cloud and external-agent service usage has its own conditions/costs.
- **Commercial:** The reviewed Apache-2.0 application-code license permits commercial activity subject to its conditions. This does not clear separate model weights, datasets, voices, dependency code, services or proprietary hosts; unrestricted end-to-end commercial use is not established.
- **Cost:** No purchase requirement was identified for the reviewed source code. Hardware, storage and any selected paid provider or proprietary host can incur costs; current service prices were not verified.

### Why it merits attention

A minimal deployment path and explicit speak/silence/delegate behavior make the interactive-media use concrete. Documentation/source review only; the application was not installed or run. [Source 1](https://github.com/jd-opensource/JoyAI-VL-Interaction/blob/main/README.md) [Source 2](https://github.com/jd-opensource/JoyAI-VL-Interaction/blob/main/doc/getting_started.md) [Source 3](https://joyai-vl-video-future-academy-jd.github.io/JoyAI-VL-Interaction/)

### Limitations

Research system with uncertain timing/recognition outside demonstrations. The AdaCodec variant is still on the README TODO list, so its described token savings are not assumed in the released default route. [Source 1](https://github.com/jd-opensource/JoyAI-VL-Interaction/blob/main/README.md) [Source 2](https://github.com/jd-opensource/JoyAI-VL-Interaction/blob/main/doc/getting_started.md) [Source 3](https://joyai-vl-video-future-academy-jd.github.io/JoyAI-VL-Interaction/)

### Get the tool

- [Repository](https://github.com/jd-opensource/JoyAI-VL-Interaction)
- [Documentation](https://github.com/jd-opensource/JoyAI-VL-Interaction/blob/main/README.md)

## anidoodle

Computational art & creative coding · Images & design · Video, animation & film · AI kinetic typography and animated lettering · Audio, music & voice · Browser tools & web media

Repository is within the observed recent-creation window; this first detailed guide does not establish production maturity.

### How it uses AI

An agent-driven illustration/animation toolkit: an external language model writes deterministic drawing and music programs, then a local engine renders them. Creating coherent explainer art, animated diagrams, social loops and launch films that can be revised as code and exported in multiple formats. [Source](https://github.com/alexgreensh/anidoodle/blob/main/README.md)

### Introduction

An agent-driven illustration/animation toolkit: an external language model writes deterministic drawing and music programs, then a local engine renders them. [Source 1](https://github.com/alexgreensh/anidoodle/blob/main/README.md)

### What it is good for

Creating coherent explainer art, animated diagrams, social loops and launch films that can be revised as code and exported in multiple formats. [Source 1](https://github.com/alexgreensh/anidoodle/blob/main/README.md)

### Demo & examples

The README includes a launch film and a 47-second Mechanical Lepidoptera example made with the engine; they are published examples, not reproduced here. [Source 1](https://github.com/alexgreensh/anidoodle/blob/main/README.md)

### Install

Use the documented route for your platform. These reference steps and commands were not executed in this review. [Source 1](https://github.com/alexgreensh/anidoodle/blob/main/README.md)

1. Install the documented skill/plugin in a compatible existing agent, or inspect/copy its standard skill folder.
2. Use Node 20+ and the scaffold command to create a separate artwork project.
3. Install its project dependencies and Chromium; FFmpeg is needed for moving-image exports.

```sh
node <anidoodle>/engine/tools/scaffold.mjs ./art --still hero --film intro --format 9x16 --duration 60
```


```sh
node tools/still.mjs hero --out out/hero.png --scale 2
```


```sh
node tools/render.mjs intro --out out/intro.mp4
```

### First project

Creating coherent explainer art, animated diagrams, social loops and launch films that can be revised as code and exported in multiple formats. [Source 1](https://github.com/alexgreensh/anidoodle/blob/main/README.md)

1. Ask the agent for one small illustration and review the resulting source/render.
2. Change timing, palette or a drawing feature and rerender deterministically.
3. Use the provided output checks and export PNG, video/animation or self-contained HTML.
### Hardware & software

Requirements below come from the cited documentation. Undocumented limits are left unknown, and benchmarks are not universal minimums. [Source 1](https://github.com/alexgreensh/anidoodle/blob/main/README.md)

- **Hardware:** No minimum RAM/VRAM/storage budget is published. Local rendering uses a browser; the selected external model and optional instrument sample pack have separate resource needs.
- **Software:** Node 20+, Chromium/Playwright tooling and FFmpeg for animation; a compatible agent/model account for AI authoring.
- **Platforms:** Node/browser/FFmpeg workflow. The README does not establish a tested OS-version matrix, despite describing portable outputs.

### License, model weights & costs

Apache-2.0 toolkit. External model services and optional sound-pack/instrument assets require separate terms; code rendering is not a bundled open-weight image model. [Source 1](https://github.com/alexgreensh/anidoodle/blob/main/LICENSE) [Source 2](https://github.com/alexgreensh/anidoodle/blob/main/README.md)

- **Code:** Apache-2.0
- **Weights:** Apache-2.0 toolkit. External model services and optional sound-pack/instrument assets require separate terms; code rendering is not a bundled open-weight image model.
- **Commercial:** The reviewed Apache-2.0 application-code license permits commercial activity subject to its conditions. This does not clear separate model weights, datasets, voices, dependency code, services or proprietary hosts; unrestricted end-to-end commercial use is not established.
- **Cost:** No purchase requirement was identified for the reviewed source code. Hardware, storage and any selected paid provider or proprietary host can incur costs; current service prices were not verified.

### Why it merits attention

Source-based deterministic outputs, format checks and editable music/art structure can make revisions more predictable. Documentation/source review only; the application was not installed or run. [Source 1](https://github.com/alexgreensh/anidoodle/blob/main/README.md)

### Limitations

AI is used during authoring; the finished renderer is deterministic. High-quality examples still require prompting and source review. No universal speed or zero-cost first-generation promise is inferred. [Source 1](https://github.com/alexgreensh/anidoodle/blob/main/README.md)

### Get the tool

- [Repository](https://github.com/alexgreensh/anidoodle)
- [Documentation](https://github.com/alexgreensh/anidoodle/blob/main/README.md)

## SandKit

Browser tools & web media · Computational art & creative coding · Interactive, immersive & live media · Images & design

Repository is within the observed recent-creation window; this first detailed guide does not establish production maturity.

### How it uses AI

An AI-assisted sand-art workflow pairing agent-created line art/estimated depth maps with a deterministic WebGL2 particle renderer and visual editor. Building an interactive illustration or website hero that scatters and reforms, with editable grain, depth and animation controls. [Source](https://github.com/LinklyAI/SandKit/blob/main/README.md) [Source](https://linkly.ai/sandkit)

### Introduction

An AI-assisted sand-art workflow pairing agent-created line art/estimated depth maps with a deterministic WebGL2 particle renderer and visual editor. [Source 1](https://github.com/LinklyAI/SandKit/blob/main/README.md) [Source 2](https://linkly.ai/sandkit)

### What it is good for

Building an interactive illustration or website hero that scatters and reforms, with editable grain, depth and animation controls. [Source 1](https://github.com/LinklyAI/SandKit/blob/main/README.md) [Source 2](https://linkly.ai/sandkit)

### Demo & examples

The official demo presents sample artwork and text experiments. The included sample assets work without running an AI model. [Source 1](https://github.com/LinklyAI/SandKit/blob/main/README.md) [Source 2](https://linkly.ai/sandkit)

### Install

Use the documented route for your platform. These reference steps and commands were not executed in this review. [Source 1](https://github.com/LinklyAI/SandKit/blob/main/README.md) [Source 2](https://linkly.ai/sandkit)

1. Clone the repository and use Node 22+.
2. Start scripts/serve.mjs; the core, showcase and editor do not require dependency installation.
3. For custom AI art use the documented compatible image-capable agent workflow, then bring the produced maps into the renderer.

```sh
node scripts/serve.mjs
```

### First project

Building an interactive illustration or website hero that scatters and reforms, with editable grain, depth and animation controls. [Source 1](https://github.com/LinklyAI/SandKit/blob/main/README.md) [Source 2](https://linkly.ai/sandkit)

1. Open the showcase or editor and explore an included sample.
2. Create or supply matching line/depth images, then tune grain budget, scatter timing and parallax.
3. Export editor settings or integrate the unchanged source/worker files into a web page.
### Hardware & software

Requirements below come from the cited documentation. Undocumented limits are left unknown, and benchmarks are not universal minimums. [Source 1](https://github.com/LinklyAI/SandKit/blob/main/README.md) [Source 2](https://linkly.ai/sandkit)

- **Hardware:** WebGL2-capable graphics; numeric RAM/VRAM/storage minimums are not published. Adaptive grain budget and reduced-motion output are provided.
- **Software:** Node 22+ for the local server; browser WebGL2 and HTTP hosting. Optional React adapter targets React 18+; custom AI images require an external model session.
- **Platforms:** Browser renderer with Node source tooling. Specific tested desktop/mobile OS versions are not documented.

### License, model weights & costs

MIT source and included generated assets to the extent rights are held; trademarks and external image-model terms are separate. [Source 1](https://github.com/LinklyAI/SandKit/blob/main/LICENSE) [Source 2](https://github.com/LinklyAI/SandKit/blob/main/README.md) [Source 3](https://linkly.ai/sandkit)

- **Code:** MIT
- **Weights:** MIT source and included generated assets to the extent rights are held; trademarks and external image-model terms are separate.
- **Commercial:** The reviewed MIT application-code license permits commercial activity subject to its conditions. This does not clear separate model weights, datasets, voices, dependency code, services or proprietary hosts; unrestricted end-to-end commercial use is not established.
- **Cost:** No purchase requirement was identified for the reviewed source code. Hardware, storage and any selected paid provider or proprietary host can incur costs; current service prices were not verified.

### Why it merits attention

A working visual editor, matching image/depth inputs and a documented lightweight integration make the creative output controllable. Documentation/source review only; the application was not installed or run. [Source 1](https://github.com/LinklyAI/SandKit/blob/main/README.md) [Source 2](https://linkly.ai/sandkit)

### Limitations

The particle simulation is not itself AI. The public editor is not a cloud image-generation/upload service; custom art is produced in the external agent workflow. Depth is estimated rather than measured. [Source 1](https://github.com/LinklyAI/SandKit/blob/main/README.md) [Source 2](https://linkly.ai/sandkit)

### Get the tool

- [Repository](https://github.com/LinklyAI/SandKit)
- [Documentation](https://github.com/LinklyAI/SandKit/blob/main/README.md)

## PixelKiln

Games & production pipelines · Images & design · Editing, captions & post-production · Creative publishing & presentation

Completed a previously screened discovery with its first detailed guide; this is not a new-launch claim. Recent v0.87.0 adds the PixelLab Image-to-Pixel-Art Pro Flash route and updates provider pricing integration; no current service price is independently quoted here.

### How it uses AI

A manifest-driven pipeline for AI pixel-art generation, human candidate selection, recovery and engine-ready asset packaging across hosted providers or self-hosted ComfyUI. Managing consistent game sprites, tile sets and animation frames with provenance and deliberate spending controls. [Source](https://github.com/gfargo/pixelkiln/blob/main/README.md) [Source](https://github.com/gfargo/pixelkiln/blob/main/PROVIDERS.md) [Source](https://github.com/gfargo/pixelkiln/releases/tag/v0.87.0)

### Introduction

A manifest-driven pipeline for AI pixel-art generation, human candidate selection, recovery and engine-ready asset packaging across hosted providers or self-hosted ComfyUI. [Source 1](https://github.com/gfargo/pixelkiln/blob/main/README.md) [Source 2](https://github.com/gfargo/pixelkiln/blob/main/PROVIDERS.md) [Source 3](https://github.com/gfargo/pixelkiln/releases/tag/v0.87.0)

### What it is good for

Managing consistent game sprites, tile sets and animation frames with provenance and deliberate spending controls. [Source 1](https://github.com/gfargo/pixelkiln/blob/main/README.md) [Source 2](https://github.com/gfargo/pixelkiln/blob/main/PROVIDERS.md) [Source 3](https://github.com/gfargo/pixelkiln/releases/tag/v0.87.0)

### Demo & examples

The README describes the local gallery, pinned Pixelorama editing route and provider comparison; no provider job was submitted here. [Source 1](https://github.com/gfargo/pixelkiln/blob/main/README.md) [Source 2](https://github.com/gfargo/pixelkiln/blob/main/PROVIDERS.md) [Source 3](https://github.com/gfargo/pixelkiln/releases/tag/v0.87.0)

### Install

Use the documented route for your platform. These reference steps and commands were not executed in this review. [Source 1](https://github.com/gfargo/pixelkiln/blob/main/README.md) [Source 2](https://github.com/gfargo/pixelkiln/blob/main/PROVIDERS.md) [Source 3](https://github.com/gfargo/pixelkiln/releases/tag/v0.87.0)

1. Install pixelkiln in a Node 22+ project and copy a minimal manifest.
2. Configure one chosen provider privately or point to an existing local ComfyUI server.
3. Run the offline doctor and plan commands before authorizing a generation budget.

```sh
npm install --save-dev pixelkiln
```


```sh
npx pixelkiln doctor --dry-run
```


```sh
npx pixelkiln plan
```

### First project

Managing consistent game sprites, tile sets and animation frames with provenance and deliberate spending controls. [Source 1](https://github.com/gfargo/pixelkiln/blob/main/README.md) [Source 2](https://github.com/gfargo/pixelkiln/blob/main/PROVIDERS.md) [Source 3](https://github.com/gfargo/pixelkiln/releases/tag/v0.87.0)

1. Declare the intended assets/style/output paths and inspect the proposed work.
2. Generate only a selected slice with the provider-specific budget ceiling and choose candidates in the gallery.
3. Touch up the art and pack/export to Aseprite, Godot or Tiled as appropriate, retaining the manifest and lock/provenance files.
### Hardware & software

Requirements below come from the cited documentation. Undocumented limits are left unknown, and benchmarks are not universal minimums. [Source 1](https://github.com/gfargo/pixelkiln/blob/main/README.md) [Source 2](https://github.com/gfargo/pixelkiln/blob/main/PROVIDERS.md) [Source 3](https://github.com/gfargo/pixelkiln/releases/tag/v0.87.0)

- **Hardware:** No universal RAM/VRAM/storage minimum. Hosted routes mostly need client/storage resources; ComfyUI requires the selected local model hardware.
- **Software:** Node 22+; development recommends Node 24. Provider credentials or compatible ComfyUI workflow; optional Pixelorama build for browser edits.
- **Platforms:** Node CLI/local browser gallery; no fully tested OS-version matrix is published in the overview.

### License, model weights & costs

MIT application. PixelLab, Retro Diffusion, Scenario and ComfyUI models/workflows have separate costs, asset rights and license terms. [Source 1](https://github.com/gfargo/pixelkiln/blob/main/LICENSE) [Source 2](https://github.com/gfargo/pixelkiln/blob/main/README.md) [Source 3](https://github.com/gfargo/pixelkiln/blob/main/PROVIDERS.md) [Source 4](https://github.com/gfargo/pixelkiln/releases/tag/v0.87.0)

- **Code:** MIT
- **Weights:** MIT application. PixelLab, Retro Diffusion, Scenario and ComfyUI models/workflows have separate costs, asset rights and license terms.
- **Commercial:** The reviewed MIT application-code license permits commercial activity subject to its conditions. This does not clear separate model weights, datasets, voices, dependency code, services or proprietary hosts; unrestricted end-to-end commercial use is not established.
- **Cost:** No purchase requirement was identified for the reviewed source code. Hardware, storage and any selected paid provider or proprietary host can incur costs; current service prices were not verified.

### Why it merits attention

Explicit planning, human selection, recovery and export provenance address practical asset-production concerns. Documentation/source review only; the application was not installed or run. [Source 1](https://github.com/gfargo/pixelkiln/blob/main/README.md) [Source 2](https://github.com/gfargo/pixelkiln/blob/main/PROVIDERS.md) [Source 3](https://github.com/gfargo/pixelkiln/releases/tag/v0.87.0)

### Limitations

Provider feature support differs. ComfyUI frame sets and composition do not guarantee good pixel-art animation; quality gates and artist cleanup still matter. A numeric budget is in provider units, not a universal currency amount. [Source 1](https://github.com/gfargo/pixelkiln/blob/main/README.md) [Source 2](https://github.com/gfargo/pixelkiln/blob/main/PROVIDERS.md) [Source 3](https://github.com/gfargo/pixelkiln/releases/tag/v0.87.0)

### Get the tool

- [Repository](https://github.com/gfargo/pixelkiln)
- [Documentation](https://github.com/gfargo/pixelkiln/blob/main/README.md)

## InkOS

Storyboarding, narrative & comics · Creative publishing & presentation · Games & production pipelines · AI agents for code-authored media production

Completed a previously screened discovery with its first detailed guide; this is not a new-launch claim.

### How it uses AI

A story-creation agent workspace using configurable language models to manage planning, characters, continuity, drafting, review, revision and multilingual delivery. Developing serialized fiction, scripts or interactive narrative while preserving project memory and reviewing proposed changes. [Source](https://github.com/Narcooo/inkos/blob/master/README.md)

### Introduction

A story-creation agent workspace using configurable language models to manage planning, characters, continuity, drafting, review, revision and multilingual delivery. [Source 1](https://github.com/Narcooo/inkos/blob/master/README.md)

### What it is good for

Developing serialized fiction, scripts or interactive narrative while preserving project memory and reviewing proposed changes. [Source 1](https://github.com/Narcooo/inkos/blob/master/README.md)

### Demo & examples

The repository shows the Studio interface and links a hosted edition; the local source workflow is the reviewed installation route. [Source 1](https://github.com/Narcooo/inkos/blob/master/README.md)

### Install

Use the documented route for your platform. These reference steps and commands were not executed in this review. [Source 1](https://github.com/Narcooo/inkos/blob/master/README.md)

1. Install the npm package with Node 22.16+.
2. Initialize a separate story project and start the local Studio.
3. In model settings select a supported provider/protocol, test the connection and save the model configuration; optional local endpoints have their own setup.

```sh
npm i -g @actalk/inkos
```


```sh
inkos init my-novel
```


```sh
inkos
```

### First project

Developing serialized fiction, scripts or interactive narrative while preserving project memory and reviewing proposed changes. [Source 1](https://github.com/Narcooo/inkos/blob/master/README.md)

1. Create a story brief and establish characters, setting and constraints.
2. Ask for a plan or short scene, then inspect the saved draft and audit findings.
3. Revise continuity/style and review translations or interactive state before exporting/publishing.
### Hardware & software

Requirements below come from the cited documentation. Undocumented limits are left unknown, and benchmarks are not universal minimums. [Source 1](https://github.com/Narcooo/inkos/blob/master/README.md)

- **Hardware:** No numeric RAM/VRAM/storage minimum. Local-model inference, if selected, has separate requirements; cloud routes need network access.
- **Software:** Node 22.16+ and a compatible model provider or endpoint. Studio secrets/configuration and CLI environment overrides are intentionally separate.
- **Platforms:** Node CLI/TUI/local web workspace. A verified OS-version matrix and native mobile application were not established.

### License, model weights & costs

AGPL-3.0 code. Model services, generated covers, source texts and translation rights are separate; hosted deployments must respect applicable source-sharing obligations. [Source 1](https://github.com/Narcooo/inkos/blob/master/LICENSE) [Source 2](https://github.com/Narcooo/inkos/blob/master/README.md)

- **Code:** AGPL-3.0
- **Weights:** AGPL-3.0 code. Model services, generated covers, source texts and translation rights are separate; hosted deployments must respect applicable source-sharing obligations.
- **Commercial:** The reviewed AGPL-3.0 application-code license permits commercial activity subject to its conditions. This does not clear separate model weights, datasets, voices, dependency code, services or proprietary hosts; unrestricted end-to-end commercial use is not established.
- **Cost:** No purchase requirement was identified for the reviewed source code. Hardware, storage and any selected paid provider or proprietary host can incur costs; current service prices were not verified.

### Why it merits attention

A shared project memory, structured review/revision and explicit configuration paths offer useful support for long-form work. Documentation/source review only; the application was not installed or run. [Source 1](https://github.com/Narcooo/inkos/blob/master/README.md)

### Limitations

An agent’s statement that it finished is not proof of saved output; inspect the actual files. Narrative consistency and translation quality require editorial review, and hosted models may incur substantial usage. [Source 1](https://github.com/Narcooo/inkos/blob/master/README.md)

### Get the tool

- [Repository](https://github.com/Narcooo/inkos)
- [Documentation](https://github.com/Narcooo/inkos/blob/master/README.md)

## OfficeCLI

Creative publishing & presentation · Data art & scientific visualization · AI agents for code-authored media production

Completed a previously screened discovery with its first detailed guide; this is not a new-launch claim.

### How it uses AI

A document-authoring toolkit designed for an external AI agent to create/edit Office files and render previews for a visual check-and-revise loop. Building presentation decks, illustrated reports and document layouts with inspectable structure and rendered feedback. [Source](https://github.com/iOfficeAI/OfficeCLI/blob/main/README.md)

### Introduction

A document-authoring toolkit designed for an external AI agent to create/edit Office files and render previews for a visual check-and-revise loop. [Source 1](https://github.com/iOfficeAI/OfficeCLI/blob/main/README.md)

### What it is good for

Building presentation decks, illustrated reports and document layouts with inspectable structure and rendered feedback. [Source 1](https://github.com/iOfficeAI/OfficeCLI/blob/main/README.md)

### Demo & examples

The README publishes deck/document creation examples. The official website could not be fetched during this review; no Office file was generated here. [Source 1](https://github.com/iOfficeAI/OfficeCLI/blob/main/README.md)

### Install

Use the documented route for your platform. These reference steps and commands were not executed in this review. [Source 1](https://github.com/iOfficeAI/OfficeCLI/blob/main/README.md)

1. Download the self-contained binary for the documented OS/architecture, or use the documented npm/Homebrew/Scoop route.
2. Check officecli --version; a separate .NET runtime or Microsoft Office installation is not required by the packaged binary.
3. Connect it to the chosen external agent workflow and start with a disposable document.

```sh
npm install -g @officecli/officecli
```


```sh
officecli --version
```


```sh
officecli create deck.pptx
```


```sh
officecli view deck.pptx html
```


```sh
officecli close deck.pptx
```

### First project

Building presentation decks, illustrated reports and document layouts with inspectable structure and rendered feedback. [Source 1](https://github.com/iOfficeAI/OfficeCLI/blob/main/README.md)

1. Create a small presentation/document and add one structured content element.
2. Render/view it as HTML or PNG and let the agent inspect the result.
3. Correct layout, validate the actual file and close the resident document session to flush changes.
### Hardware & software

Requirements below come from the cited documentation. Undocumented limits are left unknown, and benchmarks are not universal minimums. [Source 1](https://github.com/iOfficeAI/OfficeCLI/blob/main/README.md)

- **Hardware:** Numeric RAM/VRAM/storage minimums are not published. Image preview/rendering and any external model add their own resource needs.
- **Software:** Self-contained native binary with embedded .NET; npm route is only a binary installer. An external AI agent/model is needed for AI-authored content.
- **Platforms:** Published binaries cover Windows x64/ARM64, macOS Intel/Apple Silicon and Linux x64/ARM64.

### License, model weights & costs

Apache-2.0 code. External model services, fonts, templates and input media retain their own terms; Office-file support does not license proprietary assets. [Source 1](https://github.com/iOfficeAI/OfficeCLI/blob/main/LICENSE) [Source 2](https://github.com/iOfficeAI/OfficeCLI/blob/main/README.md)

- **Code:** Apache-2.0
- **Weights:** Apache-2.0 code. External model services, fonts, templates and input media retain their own terms; Office-file support does not license proprietary assets.
- **Commercial:** The reviewed Apache-2.0 application-code license permits commercial activity subject to its conditions. This does not clear separate model weights, datasets, voices, dependency code, services or proprietary hosts; unrestricted end-to-end commercial use is not established.
- **Cost:** No purchase requirement was identified for the reviewed source code. Hardware, storage and any selected paid provider or proprietary host can incur costs; current service prices were not verified.

### Why it merits attention

Structured inspection plus rendered previews provide concrete feedback for agent-authored layout work. Documentation/source review only; the application was not installed or run. [Source 1](https://github.com/iOfficeAI/OfficeCLI/blob/main/README.md)

### Limitations

The CLI is not a standalone model. Rendering fidelity and final layout must be checked in the intended viewer; the repository’s superlative marketing claims were not treated as evidence. [Source 1](https://github.com/iOfficeAI/OfficeCLI/blob/main/README.md)

### Get the tool

- [Repository](https://github.com/iOfficeAI/OfficeCLI)
- [Documentation](https://github.com/iOfficeAI/OfficeCLI/blob/main/README.md)

## CAYADEV Visualizer

Performance, projection & stage media · Physical, robotic & kinetic installations · Interactive, immersive & live media · Data art & scientific visualization · AI agents for code-authored media production

Completed a previously screened discovery with its first detailed guide; this is not a new-launch claim.

### How it uses AI

A cross-platform VJ/audio-reactive application with an MCP interface that lets an external AI agent inspect previews and configure scenes, shaders, layers and show controls. Building and revising live visual looks for music, projection or OBS output with an agent, while preserving conventional performance controls. [Source](https://github.com/CaYatur/SoundVisualizer/blob/main/README.md)

### Introduction

A cross-platform VJ/audio-reactive application with an MCP interface that lets an external AI agent inspect previews and configure scenes, shaders, layers and show controls. [Source 1](https://github.com/CaYatur/SoundVisualizer/blob/main/README.md)

### What it is good for

Building and revising live visual looks for music, projection or OBS output with an agent, while preserving conventional performance controls. [Source 1](https://github.com/CaYatur/SoundVisualizer/blob/main/README.md)

### Demo & examples

The README contains visual galleries and documented output routes. The built-in keyword Scene Generator is explicitly non-neural; the AI workflow is the external-agent control path. [Source 1](https://github.com/CaYatur/SoundVisualizer/blob/main/README.md)

### Install

Use the documented route for your platform. These reference steps and commands were not executed in this review. [Source 1](https://github.com/CaYatur/SoundVisualizer/blob/main/README.md)

1. Install the release for Windows, Apple Silicon macOS or Linux, or build the source with Node 20+.
2. Choose an audio source/display and confirm one normal visualizer scene first.
3. Install Node LTS for the optional MCP bridge, enable it on the Control card and connect the shown local command to a chosen agent.

```sh
npm install
```


```sh
npm start
```

### First project

Building and revising live visual looks for music, projection or OBS output with an agent, while preserving conventional performance controls. [Source 1](https://github.com/CaYatur/SoundVisualizer/blob/main/README.md)

1. Start with a template and inspect its audio response.
2. Let the agent read the scene and preview, then grant only the application mode needed for the edits you want.
3. Review the resulting layers/effects and route to a display, OBS or the recorded-video output.
### Hardware & software

Requirements below come from the cited documentation. Undocumented limits are left unknown, and benchmarks are not universal minimums. [Source 1](https://github.com/CaYatur/SoundVisualizer/blob/main/README.md)

- **Hardware:** GPU with WebGL2 required; numeric RAM/VRAM/disk minima are not published. Multiple displays and high-resolution effects increase load.
- **Software:** Packaged Electron app. Node LTS is needed for MCP, Node 20+ for source. macOS system audio needs a virtual device such as BlackHole; Linux needs PulseAudio/PipeWire.
- **Platforms:** Windows 10/11, Apple Silicon macOS (build notes specify macOS 15+) and Linux x64. Spout/Syphon and lighting features remain platform-specific.

### License, model weights & costs

MIT application. Imported MilkDrop presets, shaders, music and external agent/model services retain their own terms. [Source 1](https://github.com/CaYatur/SoundVisualizer/blob/main/LICENSE) [Source 2](https://github.com/CaYatur/SoundVisualizer/blob/main/README.md)

- **Code:** MIT
- **Weights:** MIT application. Imported MilkDrop presets, shaders, music and external agent/model services retain their own terms.
- **Commercial:** The reviewed MIT application-code license permits commercial activity subject to its conditions. This does not clear separate model weights, datasets, voices, dependency code, services or proprietary hosts; unrestricted end-to-end commercial use is not established.
- **Cost:** No purchase requirement was identified for the reviewed source code. Hardware, storage and any selected paid provider or proprietary host can incur costs; current service prices were not verified.

### Why it merits attention

Preview-reading tools, scoped control modes and deterministic output controls make AI assistance verifiable within an actual VJ workflow. Documentation/source review only; the application was not installed or run. [Source 1](https://github.com/CaYatur/SoundVisualizer/blob/main/README.md)

### Limitations

Audio reactivity and procedural graphics are not themselves neural generation. Agent/model setup is separate, live performance needs rehearsal, and no advertised test/performance count was independently reproduced. [Source 1](https://github.com/CaYatur/SoundVisualizer/blob/main/README.md)

### Get the tool

- [Repository](https://github.com/CaYatur/SoundVisualizer)
- [Documentation](https://github.com/CaYatur/SoundVisualizer/blob/main/README.md)

## morningprint

AI-assisted textile and computational craft · Physical, robotic & kinetic installations · Creative publishing & presentation

Completed a previously screened discovery with its first detailed guide; this is not a new-launch claim.

### How it uses AI

A small physical-art workflow in which an external language model creates a constrained declarative CP437 art specification and a renderer sends it to an ESC/POS receipt printer. Exploring daily generative text/graphic prints as an installation or artist-book experiment. [Source](https://github.com/matt-w-horn/morningprint/blob/main/README.md)

### Introduction

A small physical-art workflow in which an external language model creates a constrained declarative CP437 art specification and a renderer sends it to an ESC/POS receipt printer. [Source 1](https://github.com/matt-w-horn/morningprint/blob/main/README.md)

### What it is good for

Exploring daily generative text/graphic prints as an installation or artist-book experiment. [Source 1](https://github.com/matt-w-horn/morningprint/blob/main/README.md)

### Demo & examples

The README shows a physical example print and provides a fixed golden art plate for renderer testing. [Source 1](https://github.com/matt-w-horn/morningprint/blob/main/README.md)

### Install

Use the documented route for your platform. These reference steps and commands were not executed in this review. [Source 1](https://github.com/matt-w-horn/morningprint/blob/main/README.md)

1. Prepare the documented ESC/POS printer and USB bridge setup; the author uses an Epson TM-T20III and Raspberry Pi Zero W.
2. Build the TypeScript Apps Script bundle with Node/npm and create your own Apps Script project before any push; the committed clasp binding belongs to the author.
3. Configure the printer bridge/tunnel and model access privately, then test a non-AI golden plate before an AI print.

```sh
npm install
```


```sh
npm run build
```


```sh
node test-print.mjs art --dry
```

### First project

Exploring daily generative text/graphic prints as an installation or artist-book experiment. [Source 1](https://github.com/matt-w-horn/morningprint/blob/main/README.md)

1. Calibrate columns and byte output on the selected printer.
2. Inspect a dry-run art specification and compare a fixed test plate.
3. Generate one reviewed piece and print it; recurring scheduling is optional user setup, not something performed in this research run.
### Hardware & software

Requirements below come from the cited documentation. Undocumented limits are left unknown, and benchmarks are not universal minimums. [Source 1](https://github.com/matt-w-horn/morningprint/blob/main/README.md)

- **Hardware:** Documented Epson TM-T20III 80 mm ESC/POS printer and Pi Zero W; other CP437 ESC/POS devices need calibration. RAM/VRAM/storage minima are not published.
- **Software:** Node build tools, Google Apps Script/clasp, Python USB bridge, ngrok endpoint and Anthropic service. Weather enrichment is optional.
- **Platforms:** Cloud script plus a Linux/Pi print bridge. The build-host OS matrix is not documented; no native Windows/Mac printer compatibility is inferred.

### License, model weights & costs

MIT source and notices. Model service, tunnel/hosting and physical hardware have separate terms/costs. [Source 1](https://github.com/matt-w-horn/morningprint/blob/main/LICENSE) [Source 2](https://github.com/matt-w-horn/morningprint/blob/main/README.md)

- **Code:** MIT
- **Weights:** MIT source and notices. Model service, tunnel/hosting and physical hardware have separate terms/costs.
- **Commercial:** The reviewed MIT application-code license permits commercial activity subject to its conditions. This does not clear separate model weights, datasets, voices, dependency code, services or proprietary hosts; unrestricted end-to-end commercial use is not established.
- **Cost:** No purchase requirement was identified for the reviewed source code. Hardware, storage and any selected paid provider or proprietary host can incur costs; current service prices were not verified.

### Why it merits attention

A constrained art grammar, byte-level protocol and printed examples connect the AI step to a specific physical medium. Documentation/source review only; the application was not installed or run. [Source 1](https://github.com/matt-w-horn/morningprint/blob/main/README.md)

### Limitations

The author’s Pi bridge script is not committed; adapting the runbook is required. Not a turnkey printer app, and the exact service model identifier must be checked against the chosen account. [Source 1](https://github.com/matt-w-horn/morningprint/blob/main/README.md)

### Get the tool

- [Repository](https://github.com/matt-w-horn/morningprint)
- [Documentation](https://github.com/matt-w-horn/morningprint/blob/main/README.md)

## Kolam Studio

AI-assisted textile and computational craft · Interactive, immersive & live media · Accessible media & assistive creation · Browser tools & web media

Repository is within the observed recent-creation window; this first detailed guide does not establish production maturity.

### How it uses AI

A browser kolam/rangoli studio using speech recognition for English or Tamil commands that control a procedural mirror-curve drawing system. Hands-free exploration of patterns, grid size and themes, followed by a high-resolution PNG for visual study or digital artwork. [Source](https://github.com/adarshoff/kolam-studio/blob/main/README.md)

### Introduction

A browser kolam/rangoli studio using speech recognition for English or Tamil commands that control a procedural mirror-curve drawing system. [Source 1](https://github.com/adarshoff/kolam-studio/blob/main/README.md)

### What it is good for

Hands-free exploration of patterns, grid size and themes, followed by a high-resolution PNG for visual study or digital artwork. [Source 1](https://github.com/adarshoff/kolam-studio/blob/main/README.md)

### Demo & examples

The README shows the drawing workflow and links a live studio, but the live-page fetch failed today. [Source 1](https://github.com/adarshoff/kolam-studio/blob/main/README.md)

### Install

Use the documented route for your platform. These reference steps and commands were not executed in this review. [Source 1](https://github.com/adarshoff/kolam-studio/blob/main/README.md)

1. Clone the single-file application and serve it over local HTTP or HTTPS.
2. Use Chrome or Edge with internet access for Web Speech API recognition.
3. Choose EN or Tamil and grant microphone access only if using voice; every command also has a button/pill.

```sh
python -m http.server
```

### First project

Hands-free exploration of patterns, grid size and themes, followed by a high-resolution PNG for visual study or digital artwork. [Source 1](https://github.com/adarshoff/kolam-studio/blob/main/README.md)

1. Choose a small pattern/grid and generate a design.
2. Speak a grid/theme command or use its visible equivalent, then inspect the resulting loops.
3. Save the 3000 px PNG and a gallery entry for later comparison.
### Hardware & software

Requirements below come from the cited documentation. Undocumented limits are left unknown, and benchmarks are not universal minimums. [Source 1](https://github.com/adarshoff/kolam-studio/blob/main/README.md)

- **Hardware:** Microphone for voice input; RAM/VRAM/storage minima are not documented.
- **Software:** Single HTML/JavaScript Canvas app; local HTTP server or HTTPS. Voice needs the browser speech service and network access.
- **Platforms:** Chrome/Edge for voice; other modern browsers for manual controls. No exact browser/OS versions or offline speech support are documented.

### License, model weights & costs

MIT code. Browser speech-service terms and any external use of cultural/source imagery remain separate. [Source 1](https://github.com/adarshoff/kolam-studio/blob/main/LICENSE) [Source 2](https://github.com/adarshoff/kolam-studio/blob/main/README.md)

- **Code:** MIT
- **Weights:** MIT code. Browser speech-service terms and any external use of cultural/source imagery remain separate.
- **Commercial:** The reviewed MIT application-code license permits commercial activity subject to its conditions. This does not clear separate model weights, datasets, voices, dependency code, services or proprietary hosts; unrestricted end-to-end commercial use is not established.
- **Cost:** No purchase requirement was identified for the reviewed source code. Hardware, storage and any selected paid provider or proprietary host can incur costs; current service prices were not verified.

### Why it merits attention

A concrete speech-to-creative-control workflow and manual equivalents make the accessibility contribution clear. Documentation/source review only; the application was not installed or run. [Source 1](https://github.com/adarshoff/kolam-studio/blob/main/README.md)

### Limitations

The pattern generator is procedural, not a neural image model; being built with AI is not the reason for inclusion. Speech recognition can mishear commands, and documented symmetry constraints differ for odd/even grids. [Source 1](https://github.com/adarshoff/kolam-studio/blob/main/README.md)

### Get the tool

- [Repository](https://github.com/adarshoff/kolam-studio)
- [Documentation](https://github.com/adarshoff/kolam-studio/blob/main/README.md)

## OnDeviceLLM / OnDeviceLAS

Mobile, edge & on-device creation · Images & design · Audio, music & voice · Interactive, immersive & live media

Completed a previously screened discovery with its first detailed guide; this is not a new-launch claim.

### How it uses AI

An Apple-platform developer workbench integrating local language, vision, speech and image-generation runtimes, with an on-device server build. Prototyping private mobile creative interfaces or supplying local speech/vision/model services to a separately built client. [Source](https://github.com/Mesutcydev/ios-local-llm/blob/main/README.md)

### Introduction

An Apple-platform developer workbench integrating local language, vision, speech and image-generation runtimes, with an on-device server build. [Source 1](https://github.com/Mesutcydev/ios-local-llm/blob/main/README.md)

### What it is good for

Prototyping private mobile creative interfaces or supplying local speech/vision/model services to a separately built client. [Source 1](https://github.com/Mesutcydev/ios-local-llm/blob/main/README.md)

### Demo & examples

The README describes multiple source modules, but the current generated OnDeviceLAS scheme is server-only; full assistant/lens/voice screens are not promised in that build. [Source 1](https://github.com/Mesutcydev/ios-local-llm/blob/main/README.md)

### Install

Use the documented route for your platform. These reference steps and commands were not executed in this review. [Source 1](https://github.com/Mesutcydev/ios-local-llm/blob/main/README.md)

1. Use an Apple Silicon Mac with the documented Xcode/native build toolchain and clone recursively.
2. Build the required native frameworks, generate the project and install pods as described.
3. Open the OnDeviceLAS workspace and select a simulator or provisioned device; obtain model weights separately.
### First project

Prototyping private mobile creative interfaces or supplying local speech/vision/model services to a separately built client. [Source 1](https://github.com/Mesutcydev/ios-local-llm/blob/main/README.md)

1. Start the server build with a small compatible model.
2. Connect a local client through its authenticated API and try one short speech/vision/image request.
3. Inspect resource use and generated results; add a custom UI from the source modules only as a separate development task.
### Hardware & software

Requirements below come from the cited documentation. Undocumented limits are left unknown, and benchmarks are not universal minimums. [Source 1](https://github.com/Mesutcydev/ios-local-llm/blob/main/README.md)

- **Hardware:** Apple Silicon development host and a compatible iOS device/simulator. RAM and storage depend on models; numeric universal limits are not documented.
- **Software:** Xcode 26+, iOS 18+, XcodeGen, CocoaPods, CMake and native MLX/llama.cpp/whisper.cpp-related components. Physical devices require signing configuration.
- **Platforms:** Apple/iOS source workflow with an optional Mac Catalyst path. Windows/Linux/Android native builds are not provided by this route.

### License, model weights & costs

MIT application source. Model weights are separate; Apple FastVLM is identified as research-only. No bundled-weight commercial permission is implied. [Source 1](https://github.com/Mesutcydev/ios-local-llm/blob/main/LICENSE) [Source 2](https://github.com/Mesutcydev/ios-local-llm/blob/main/README.md)

- **Code:** MIT
- **Weights:** MIT application source. Model weights are separate; Apple FastVLM is identified as research-only. No bundled-weight commercial permission is implied.
- **Commercial:** The reviewed MIT application-code license permits commercial activity subject to its conditions. This does not clear separate model weights, datasets, voices, dependency code, services or proprietary hosts; unrestricted end-to-end commercial use is not established.
- **Cost:** No purchase requirement was identified for the reviewed source code. Hardware, storage and any selected paid provider or proprietary host can incur costs; current service prices were not verified.

### Why it merits attention

Local API boundaries and several runtime adapters offer useful building blocks for mobile creative prototypes. Documentation/source review only; the application was not installed or run. [Source 1](https://github.com/Mesutcydev/ios-local-llm/blob/main/README.md)

### Limitations

Developer setup, not an App Store-ready studio. App Store is coming soon and older IPA routes are retired. Background iOS execution is limited; simulator success is not device inference performance. [Source 1](https://github.com/Mesutcydev/ios-local-llm/blob/main/README.md)

### Get the tool

- [Repository](https://github.com/Mesutcydev/ios-local-llm)
- [Documentation](https://github.com/Mesutcydev/ios-local-llm/blob/main/README.md)

## EmDash AI Alt Text

Accessible media & assistive creation · Creative publishing & presentation · Browser tools & web media

Repository is within the observed recent-creation window; this first detailed guide does not establish production maturity.

### How it uses AI

An EmDash plugin using an external vision-language model to generate or translate image alternative text in the entry’s language while preserving human-written text. Preparing first-draft accessible descriptions for image-heavy portfolios or multilingual media publishing. [Source](https://github.com/DavidPivert/emdash-plugin-ai-alt-text/blob/main/README.md)

### Introduction

An EmDash plugin using an external vision-language model to generate or translate image alternative text in the entry’s language while preserving human-written text. [Source 1](https://github.com/DavidPivert/emdash-plugin-ai-alt-text/blob/main/README.md)

### What it is good for

Preparing first-draft accessible descriptions for image-heavy portfolios or multilingual media publishing. [Source 1](https://github.com/DavidPivert/emdash-plugin-ai-alt-text/blob/main/README.md)

### Demo & examples

The repository documents media-library inheritance and editor behavior. No content was submitted to a vision API in this review. [Source 1](https://github.com/DavidPivert/emdash-plugin-ai-alt-text/blob/main/README.md)

### Install

Use the documented route for your platform. These reference steps and commands were not executed in this review. [Source 1](https://github.com/DavidPivert/emdash-plugin-ai-alt-text/blob/main/README.md)

1. Use EmDash 1.0+ with its sandbox plugin runner.
2. Build/install the plugin through the documented package workflow and configure the Cloudflare LOADER binding and Anthropic key privately.
3. Test on a public JPEG/PNG/GIF/WebP image in a draft entry before wider use.
### First project

Preparing first-draft accessible descriptions for image-heavy portfolios or multilingual media publishing. [Source 1](https://github.com/DavidPivert/emdash-plugin-ai-alt-text/blob/main/README.md)

1. Save a draft entry with a supported image and descriptive context.
2. Review the generated alt text for visible facts, language and names.
3. Edit the description manually as needed; retain intentional human alt text rather than overwriting it.
### Hardware & software

Requirements below come from the cited documentation. Undocumented limits are left unknown, and benchmarks are not universal minimums. [Source 1](https://github.com/DavidPivert/emdash-plugin-ai-alt-text/blob/main/README.md)

- **Hardware:** No local RAM/VRAM requirement is documented; inference uses a hosted service. Hosting resources and image size limits depend on the chosen platform.
- **Software:** EmDash 1.0+, plugin sandbox runner, paid Cloudflare Workers LOADER capability and Anthropic API access; pnpm for source builds.
- **Platforms:** CMS/Workers deployment; a tested local Windows/macOS/Linux installation matrix is not documented.

### License, model weights & costs

MIT plugin. Cloudflare and Anthropic are paid/proprietary services with independent terms; the code license does not include those services. [Source 1](https://github.com/DavidPivert/emdash-plugin-ai-alt-text/blob/main/LICENSE) [Source 2](https://github.com/DavidPivert/emdash-plugin-ai-alt-text/blob/main/README.md)

- **Code:** MIT
- **Weights:** MIT plugin. Cloudflare and Anthropic are paid/proprietary services with independent terms; the code license does not include those services.
- **Commercial:** The reviewed MIT application-code license permits commercial activity subject to its conditions. This does not clear separate model weights, datasets, voices, dependency code, services or proprietary hosts; unrestricted end-to-end commercial use is not established.
- **Cost:** No purchase requirement was identified for the reviewed source code. Hardware, storage and any selected paid provider or proprietary host can incur costs; current service prices were not verified.

### Why it merits attention

Language-aware descriptions and preservation of human text support a useful editorial accessibility workflow. Documentation/source review only; the application was not installed or run. [Source 1](https://github.com/DavidPivert/emdash-plugin-ai-alt-text/blob/main/README.md)

### Limitations

SVG and some other formats/rich-text image paths are unsupported. Provider failure leaves the save path working but may leave alt text missing. Image URLs/context are sent to the service; generated descriptions can hallucinate and do not establish accessibility compliance. [Source 1](https://github.com/DavidPivert/emdash-plugin-ai-alt-text/blob/main/README.md)

### Get the tool

- [Repository](https://github.com/DavidPivert/emdash-plugin-ai-alt-text)
- [Documentation](https://github.com/DavidPivert/emdash-plugin-ai-alt-text/blob/main/README.md)

## Champ

Avatars, digital humans & lip sync · Motion capture & character animation · Video, animation & film

Completed a previously screened discovery with its first detailed guide; this is not a new-launch claim.

### How it uses AI

A research human-image animation system using 3D parametric guidance, pose, depth, normals and semantic maps to condition neural video generation. Animating a reference person image with prepared motion guidance for character-animation studies. [Source](https://github.com/fudan-generative-vision/champ/blob/master/README.md) [Source](https://fudan-generative-vision.github.io/champ/)

### Introduction

A research human-image animation system using 3D parametric guidance, pose, depth, normals and semantic maps to condition neural video generation. [Source 1](https://github.com/fudan-generative-vision/champ/blob/master/README.md) [Source 2](https://fudan-generative-vision.github.io/champ/)

### What it is good for

Animating a reference person image with prepared motion guidance for character-animation studies. [Source 1](https://github.com/fudan-generative-vision/champ/blob/master/README.md) [Source 2](https://fudan-generative-vision.github.io/champ/)

### Demo & examples

The README and project page present animation examples; the linked hosted demos were not run. [Source 1](https://github.com/fudan-generative-vision/champ/blob/master/README.md) [Source 2](https://fudan-generative-vision.github.io/champ/)

### Install

Use the documented route for your platform. These reference steps and commands were not executed in this review. [Source 1](https://github.com/fudan-generative-vision/champ/blob/master/README.md) [Source 2](https://fudan-generative-vision.github.io/champ/)

1. Use the documented Python 3.10 environment with CUDA 12.1 and install requirements, or the recommended Poetry route on Windows.
2. Download the pretrained model collection and prepared SMPL/rendered guidance motions.
3. Set the reference image and guidance paths in the inference YAML.

```sh
python inference.py --config configs/inference/inference.yaml
```

### First project

Animating a reference person image with prepared motion guidance for character-animation studies. [Source 1](https://github.com/fudan-generative-vision/champ/blob/master/README.md) [Source 2](https://fudan-generative-vision.github.io/champ/)

1. Start with one supplied motion sequence and reference image.
2. Run the inference configuration and inspect results frame by frame.
3. Shorten the frame range if necessary and review identity, clothing and limb artifacts before reuse.
### Hardware & software

Requirements below come from the cited documentation. Undocumented limits are left unknown, and benchmarks are not universal minimums. [Source 1](https://github.com/fudan-generative-vision/champ/blob/master/README.md) [Source 2](https://fudan-generative-vision.github.io/champ/)

- **Hardware:** Tested A100 and RTX 3090. The default roughly 250-frame motion needs about 20 GB VRAM; shorter clips can reduce demand. RAM and total disk minimums are not specified.
- **Software:** Python 3.10, CUDA 12.1, repository pip/Poetry dependencies, pretrained weights and rendered SMPL-based guidance.
- **Platforms:** Ubuntu 20.04 and Windows 11 are documented. Native macOS/MPS support is not established.

### License, model weights & costs

MIT code. Stable Diffusion/animation checkpoints, SMPL assets and source images/motions have independent terms. [Source 1](https://github.com/fudan-generative-vision/champ/blob/master/LICENSE) [Source 2](https://github.com/fudan-generative-vision/champ/blob/master/README.md) [Source 3](https://fudan-generative-vision.github.io/champ/)

- **Code:** MIT
- **Weights:** MIT code. Stable Diffusion/animation checkpoints, SMPL assets and source images/motions have independent terms.
- **Commercial:** The reviewed MIT application-code license permits commercial activity subject to its conditions. This does not clear separate model weights, datasets, voices, dependency code, services or proprietary hosts; unrestricted end-to-end commercial use is not established.
- **Cost:** No purchase requirement was identified for the reviewed source code. Hardware, storage and any selected paid provider or proprietary host can incur costs; current service prices were not verified.

### Why it merits attention

Published guidance channels and a clear inference/configuration route expose useful animation controls. Documentation/source review only; the application was not installed or run. [Source 1](https://github.com/fudan-generative-vision/champ/blob/master/README.md) [Source 2](https://fudan-generative-vision.github.io/champ/)

### Limitations

Older research baseline, not a new release today. Preparing new motion guidance is additional work; VRAM demand and temporal/identity artifacts can limit practical use. [Source 1](https://github.com/fudan-generative-vision/champ/blob/master/README.md) [Source 2](https://fudan-generative-vision.github.io/champ/)

### Get the tool

- [Repository](https://github.com/fudan-generative-vision/champ)
- [Documentation](https://github.com/fudan-generative-vision/champ/blob/master/README.md)

## FollowYourPose

Motion capture & character animation · Avatars, digital humans & lip sync · Video, animation & film · Creative learning & authoring

Completed a previously screened discovery with its first detailed guide; this is not a new-launch claim.

### How it uses AI

A pose-conditioned text-to-video research model adapting Stable Diffusion with learned pose encoding and temporal attention. Exploring how a character’s textual appearance can be varied while following a skeleton-motion sequence. [Source](https://github.com/mayuelala/FollowYourPose/blob/main/README.md) [Source](https://follow-your-pose.github.io/)

### Introduction

A pose-conditioned text-to-video research model adapting Stable Diffusion with learned pose encoding and temporal attention. [Source 1](https://github.com/mayuelala/FollowYourPose/blob/main/README.md) [Source 2](https://follow-your-pose.github.io/)

### What it is good for

Exploring how a character’s textual appearance can be varied while following a skeleton-motion sequence. [Source 1](https://github.com/mayuelala/FollowYourPose/blob/main/README.md) [Source 2](https://follow-your-pose.github.io/)

### Demo & examples

The official site and README show pose/video examples and link hosted notebook/Gradio routes; their availability was not tested by running inference. [Source 1](https://github.com/mayuelala/FollowYourPose/blob/main/README.md) [Source 2](https://follow-your-pose.github.io/)

### Install

Use the documented route for your platform. These reference steps and commands were not executed in this review. [Source 1](https://github.com/mayuelala/FollowYourPose/blob/main/README.md) [Source 2](https://follow-your-pose.github.io/)

1. Create the documented Python 3.8 environment and install requirements.txt.
2. Download the FollowYourPose checkpoint and required Stable Diffusion model into the documented layout.
3. Use a prepared skeleton clip or generate one with the documented MMPose/HRNet workflow; start app.py for the local Gradio interface.

```sh
python app.py
```

### First project

Exploring how a character’s textual appearance can be varied while following a skeleton-motion sequence. [Source 1](https://github.com/mayuelala/FollowYourPose/blob/main/README.md) [Source 2](https://follow-your-pose.github.io/)

1. Load a short supplied skeleton video and enter an appearance prompt.
2. Generate a clip and compare movement against the skeleton.
3. Adjust prompt/pose input and inspect temporal artifacts before using the result in a larger edit.
### Hardware & software

Requirements below come from the cited documentation. Undocumented limits are left unknown, and benchmarks are not universal minimums. [Source 1](https://github.com/mayuelala/FollowYourPose/blob/main/README.md) [Source 2](https://follow-your-pose.github.io/)

- **Hardware:** The local demo documentation names A100/RTX 3090. Training used eight A100s; that is not an inference minimum. RAM, minimum VRAM and total storage are not specified.
- **Software:** Python 3.8, CUDA 11-era dependencies, optional old xformers wheel, model checkpoints and MMPose if creating poses.
- **Platforms:** Legacy CUDA research workflow with notebook/Gradio options. A tested modern Windows/macOS matrix is not documented.

### License, model weights & costs

MIT source. Stable Diffusion and FollowYourPose weights, pose datasets and input footage have independent terms. [Source 1](https://github.com/mayuelala/FollowYourPose/blob/main/LICENSE) [Source 2](https://github.com/mayuelala/FollowYourPose/blob/main/README.md) [Source 3](https://follow-your-pose.github.io/)

- **Code:** MIT
- **Weights:** MIT source. Stable Diffusion and FollowYourPose weights, pose datasets and input footage have independent terms.
- **Commercial:** The reviewed MIT application-code license permits commercial activity subject to its conditions. This does not clear separate model weights, datasets, voices, dependency code, services or proprietary hosts; unrestricted end-to-end commercial use is not established.
- **Cost:** No purchase requirement was identified for the reviewed source code. Hardware, storage and any selected paid provider or proprietary host can incur costs; current service prices were not verified.

### Why it merits attention

Pose examples and a local demonstration route make it a useful historical baseline for motion-conditioned generation. Documentation/source review only; the application was not installed or run. [Source 1](https://github.com/mayuelala/FollowYourPose/blob/main/README.md) [Source 2](https://follow-your-pose.github.io/)

### Limitations

Legacy dependencies and an explicitly unstable xformers installation path. Public examples do not prove modern GPU/driver compatibility or production temporal consistency. [Source 1](https://github.com/mayuelala/FollowYourPose/blob/main/README.md) [Source 2](https://follow-your-pose.github.io/)

### Get the tool

- [Repository](https://github.com/mayuelala/FollowYourPose)
- [Documentation](https://github.com/mayuelala/FollowYourPose/blob/main/README.md)

## TechPack AI Builder

Fashion, textiles & wearable media · Vector graphics, illustration & textures · Creative publishing & presentation · AI-assisted textile and computational craft

First detailed documentation review; this is a baseline, not a claim that the project launched today.

### How it uses AI

DeepSeek/NVIDIA services assist translation, PDF extraction and garment-from-photo tasks; an optional Qwen/MLX bridge supports local studio reasoning. The SVG layout engine itself is deterministic. [Source](https://github.com/morfemartin/techpack-ai-builder/blob/main/README.md) [Source](https://github.com/morfemartin/techpack-ai-builder)

### Introduction

A garment-specification wizard that exports editable multilingual SVG tech packs, with optional AI extraction, translation and garment drafting. [Source 1](https://github.com/morfemartin/techpack-ai-builder/blob/main/README.md) [Source 2](https://github.com/morfemartin/techpack-ai-builder)

### What it is good for

Prepare cap construction sheets, embroidery specifications and designer handoff pages in Spanish, English and Chinese. [Source 1](https://github.com/morfemartin/techpack-ai-builder/blob/main/README.md) [Source 2](https://github.com/morfemartin/techpack-ai-builder)

### Demo & examples

The README shows wizard and multi-artboard export examples. The linked GitHub Pages demo disables AI features because it has no server proxy; its live page could not be retrieved in this review. [Source 1](https://github.com/morfemartin/techpack-ai-builder/blob/main/README.md) [Source 2](https://github.com/morfemartin/techpack-ai-builder)

### Install

Use the documented route for your platform. These reference steps and commands were not executed in this review. [Source 1](https://github.com/morfemartin/techpack-ai-builder/blob/main/README.md) [Source 2](https://github.com/morfemartin/techpack-ai-builder)

1. Clone the official source, install its npm dependencies and start the Vite development server.
2. For AI features, copy the documented environment example into local configuration and supply the required NVIDIA service key to the server proxy.
3. The separate private-studio path uses a local Qwen/MLX bridge on a Mac; follow its dedicated studio documentation before enabling it.

```sh
git clone https://github.com/morfemartin/techpack-ai-builder.git
```


```sh
cd techpack-ai-builder
```


```sh
npm install
```


```sh
npm run dev
```

### First project

Prepare cap construction sheets, embroidery specifications and designer handoff pages in Spanish, English and Chinese. [Source 1](https://github.com/morfemartin/techpack-ai-builder/blob/main/README.md) [Source 2](https://github.com/morfemartin/techpack-ai-builder)

1. Start with the fully supported Cap template and enter brand, construction parts, placements and colors.
2. Use an optional AI extraction or translation action, then compare the output with the original specification.
3. Preview and export the SVG pages or illustration handoff; complete missing technical drawings before production.
### Hardware & software

Requirements below come from the cited documentation. Undocumented limits are left unknown, and benchmarks are not universal minimums. [Source 1](https://github.com/morfemartin/techpack-ai-builder/blob/main/README.md) [Source 2](https://github.com/morfemartin/techpack-ai-builder)

- **Hardware:** RAM, GPU/VRAM and storage minimums are not documented for the web app. The optional local Qwen model has separate memory requirements that are not established here.
- **Software:** Node.js 18+, npm, React/Vite and a browser. AI actions need the documented backend proxy and provider key; the local studio alternative uses MLX.
- **Platforms:** Browser UI with a local Node development route; an explicit local Qwen route is documented for Mac. A tested Windows/Linux matrix is not supplied, and the public static demo does not perform AI inference.

### License, model weights & costs

MIT application source. Qwen model terms and NVIDIA/DeepSeek service conditions are separate; Adobe Illustrator is an optional proprietary destination, while SVG remains usable independently. [Source 1](https://github.com/morfemartin/techpack-ai-builder/blob/main/LICENSE) [Source 2](https://github.com/morfemartin/techpack-ai-builder/blob/main/README.md) [Source 3](https://github.com/morfemartin/techpack-ai-builder)

- **Code:** MIT
- **Weights:** MIT application source. Qwen model terms and NVIDIA/DeepSeek service conditions are separate; Adobe Illustrator is an optional proprietary destination, while SVG remains usable independently.
- **Commercial:** The reviewed MIT application-code license permits commercial activity subject to its conditions. This does not clear separate model weights, datasets, voices, dependency code, services or proprietary hosts; unrestricted end-to-end commercial use is not established.
- **Cost:** No purchase requirement was identified for the reviewed source code. Hardware, storage and any selected paid provider or proprietary host can incur costs; current service prices were not verified.

### Why it merits attention

The separation of editable data, SVG export and explicit missing-illustration handoff makes this more useful than a fashion-image generator for production documentation. Documentation/source review only; the application was not installed or run. [Source 1](https://github.com/morfemartin/techpack-ai-builder/blob/main/README.md) [Source 2](https://github.com/morfemartin/techpack-ai-builder)

### Limitations

Only Cap is fully supported; other garment types and PDF export are roadmap items. AI-derived dimensions and construction details require a designer check. No garment was manufactured or export opened in Illustrator during this review. [Source 1](https://github.com/morfemartin/techpack-ai-builder/blob/main/README.md) [Source 2](https://github.com/morfemartin/techpack-ai-builder)

### Get the tool

- [Repository](https://github.com/morfemartin/techpack-ai-builder)
- [Documentation](https://github.com/morfemartin/techpack-ai-builder/blob/main/README.md)

## StableGen

3D, reconstruction & assets · Images & design · Games & production pipelines · 3D printing & generative CAD

First detailed documentation review; this is a baseline, not a claim that the project launched today.

### How it uses AI

ComfyUI runs SDXL, FLUX or Qwen diffusion workflows guided by camera/depth/normal inputs; an optional TRELLIS.2 path predicts textured meshes from images or prompts. [Source](https://github.com/sakalond/StableGen/blob/main/README.md) [Source](https://github.com/sakalond/stablegen)

### Introduction

A Blender add-on connecting scene-aware diffusion texturing and TRELLIS.2 mesh generation to a ComfyUI backend. [Source 1](https://github.com/sakalond/StableGen/blob/main/README.md) [Source 2](https://github.com/sakalond/stablegen)

### What it is good for

Develop coordinated textures across multiple objects, generate preliminary 3D assets, refine selected surfaces and bake textures for downstream engines. [Source 1](https://github.com/sakalond/StableGen/blob/main/README.md) [Source 2](https://github.com/sakalond/stablegen)

### Demo & examples

The README publishes multi-view examples, original input meshes, texture variations and generated-mesh galleries; these are developer demonstrations, not success-rate measurements. [Source 1](https://github.com/sakalond/StableGen/blob/main/README.md) [Source 2](https://github.com/sakalond/stablegen)

### Install

Use the documented route for your platform. These reference steps and commands were not executed in this review. [Source 1](https://github.com/sakalond/StableGen/blob/main/README.md) [Source 2](https://github.com/sakalond/stablegen)

1. Install and verify a supported ComfyUI backend, locally or on a separate machine.
2. For the introductory existing-mesh workflow, follow the SDXL/ComfyUI dependency route. The optional TRELLIS.2 Native texture mode pulls separately restricted NVIDIA libraries; do not assume the add-on license covers that mode.
3. Download StableGen.zip from official Releases, install and enable it in Blender, then configure the output directory, server address and ControlNet mappings.
4. Allow Blender network access for communication with ComfyUI, including when the server is local.
### First project

Develop coordinated textures across multiple objects, generate preliminary 3D assets, refine selected surfaces and bake textures for downstream engines. [Source 1](https://github.com/sakalond/StableGen/blob/main/README.md) [Source 2](https://github.com/sakalond/stablegen)

1. Open a simple mesh, start ComfyUI and open the StableGen panel in the Blender sidebar.
2. Add viewpoints, choose a matching diffusion architecture/checkpoint and enter a texture prompt.
3. Generate, inspect seams and hidden surfaces, then use local edits or alternate camera prompts to refine.
4. Bake/unwrap textures for engine export; inspect scale, topology and manufacturing constraints separately before any printing.
### Hardware & software

Requirements below come from the cited documentation. Undocumented limits are left unknown, and benchmarks are not universal minimums. [Source 1](https://github.com/sakalond/StableGen/blob/main/README.md) [Source 2](https://github.com/sakalond/stablegen)

- **Hardware:** The developer states at least 8 GB VRAM for usable SDXL speed and 16 GB or more for FLUX.1-dev or Qwen-Image-Edit. NVIDIA CUDA is recommended. Models can occupy 10–50 GB or more; total RAM and TRELLIS.2-specific minimums are not established in this guide.
- **Software:** Blender 4.2–4.5 or 5.1+; Blender 5.0 is explicitly unsupported. A working ComfyUI backend, Python 3 and Git are needed for the documented setup; dependency families vary by model.
- **Platforms:** The README lists Windows 10/11, Linux and Apple Silicon macOS. This does not establish parity for every model or CUDA extension. A remote backend is documented.

### License, model weights & costs

GPL-3.0 add-on code, reviewed in full. ComfyUI, custom nodes and SDXL/FLUX/Qwen/TRELLIS model weights retain their own terms; GPL permission for the add-on does not clear all model outputs or assets. The README identifies optional TRELLIS.2 Native texture-mode dependencies nvdiffrast/nvdiffrec as research/evaluation-only software. Use of that mode needs separate permission; it is not covered by the add-on’s GPL. The documented SDXL/Qwen projection routes do not use those two components, but their model terms still apply. [Source 1](https://github.com/sakalond/StableGen/blob/main/LICENSE) [Source 2](https://github.com/sakalond/StableGen/blob/main/README.md) [Source 3](https://github.com/sakalond/stablegen)

- **Code:** GPL-3.0
- **Weights:** GPL-3.0 add-on code, reviewed in full. ComfyUI, custom nodes and SDXL/FLUX/Qwen/TRELLIS model weights retain their own terms; GPL permission for the add-on does not clear all model outputs or assets. The README identifies optional TRELLIS.2 Native texture-mode dependencies nvdiffrast/nvdiffrec as research/evaluation-only software. Use of that mode needs separate permission; it is not covered by the add-on’s GPL. The documented SDXL/Qwen projection routes do not use those two components, but their model terms still apply.
- **Commercial:** The reviewed GPL-3.0 application-code license permits commercial activity subject to its conditions. This does not clear separate model weights, datasets, voices, dependency code, services or proprietary hosts; unrestricted end-to-end commercial use is not established.
- **Cost:** No purchase requirement was identified for the reviewed source code. Hardware, storage and any selected paid provider or proprietary host can incur costs; current service prices were not verified.

### Why it merits attention

Multi-view masking, scene-wide controls, local refinement and baking address practical asset-workflow stages beyond one-shot image generation. Documentation/source review only; the application was not installed or run. [Source 1](https://github.com/sakalond/StableGen/blob/main/README.md) [Source 2](https://github.com/sakalond/stablegen)

### Limitations

Generated topology, texture seams and unseen surfaces still need review. The print exporter and color-mixing features do not prove that a generated object is printable or mechanically safe. Hardware figures are author guidance, not measurements from this run. The optional Native TRELLIS.2 texture mode includes non-commercial dependencies; this guide’s introductory workflow uses projection-based texturing of an existing mesh. [Source 1](https://github.com/sakalond/StableGen/blob/main/README.md) [Source 2](https://github.com/sakalond/stablegen)

### Get the tool

- [Repository](https://github.com/sakalond/StableGen)
- [Documentation](https://github.com/sakalond/StableGen/blob/main/README.md)

## Additional open-source AI discoveries

Creative AI relevance and software license screened. Full installation, requirements and quality profiles are pending.

### Avorythm · MIT

Prepare translated captions and dubbed versions of recorded or browser media.
Translate and dub browser or uploaded media using Gemini speech/translation and optional Whisper transcription, with synchronized source and translated captions.
MIT source with substantive capture, synchronization and export workflows. Cloud keys and service terms apply; the Windows package also bundles GPL FFmpeg. Full routing, privacy, hardware and unsigned-installer review remains pending. Documentation screening only; not installed or tested.

- [Official overview](https://github.com/msmahdinejad/avorythm/blob/main/README.md)
- [Complete reviewed software license](https://github.com/msmahdinejad/avorythm/blob/main/LICENSE)
### Orange for ComfyUI · MIT

Give collaborators a simpler interface to curated creative-generation workflows.
Expose ComfyUI diffusion workflows through simplified creator controls, with model/node preflight, backend routing and optional LLM prompt enhancement.
MIT frontend; ComfyUI and downloadable models have independent terms. Backend-specific hardware and full installation review are pending. Documentation screening only; not installed or tested.

- [Official overview](https://github.com/saintbrodie/Orange/blob/main/README.md)
- [Complete reviewed software license](https://github.com/saintbrodie/Orange/blob/main/LICENSE)
### Whisper-WebUI · Apache-2.0

Create draft subtitles and translations from recordings or microphone input.
Use Whisper speech recognition to produce subtitle files, with optional NLLB translation, speech activity filtering, source separation and speaker diarization.
Apache-2.0 interface; model terms and optional DeepL/pyannote access are separate. Full device/backend compatibility review is pending; example memory benchmarks are not universal minimums. Documentation screening only; not installed or tested.

- [Official overview](https://github.com/jhj0517/Whisper-WebUI/blob/master/README.md)
- [Complete reviewed software license](https://github.com/jhj0517/Whisper-WebUI/blob/master/LICENSE)
### AI Render for Blender · MIT

Explore stylized Blender renders and animation frames.
Turn Blender scene renders and prompts into Stable Diffusion images or animation-frame experiments, including a documented local AUTOMATIC1111 backend route.
MIT add-on with published demos and Windows/Mac/Linux documentation. Current Blender/backend compatibility and model terms need deeper review; temporal coherence is not established. Documentation screening only; not installed or tested.

- [Official overview](https://github.com/benrugg/AI-Render/blob/main/README.md)
- [Complete reviewed software license](https://github.com/benrugg/AI-Render/blob/main/LICENSE)
### ArtAI audience installation · MIT

Build an audience-driven projection-art prototype.
Convert audience-submitted titles into VQGAN+CLIP imagery and curate the generated images in an audio-reactive Godot projection display.
MIT hackathon implementation. Its historical Twitter API integration and cloud GPU setup need modernization/availability checks; no current turnkey deployment was verified. Documentation screening only; not installed or tested.

- [Official overview](https://github.com/SilentByte/artai/blob/master/README.md)
- [Complete reviewed software license](https://github.com/SilentByte/artai/blob/master/LICENSE.txt)
### Soma EEG-to-Art · MIT

Prototype a biofeedback visual installation with a Muse headset.
Transform Muse EEG spectrograms into abstract images with trained pix2pix models for a documented participatory installation.
MIT source; external weights/data and Muse hardware need separate checks. The visual mapping is an artistic experiment, not evidence of thought-reading or a validated neurological interpretation. Detailed deployment review is pending. Documentation screening only; not installed or tested.

- [Official overview](https://github.com/Timamamu/Soma-EEG-to-Art-Feedback-Loop/blob/main/README.md)
- [Complete reviewed software license](https://github.com/Timamamu/Soma-EEG-to-Art-Feedback-Loop/blob/main/LICENSE)
### EPINET · MIT

Study depth-aware imagery from light-field captures.
Estimate depth from light-field images with a convolutional network using epipolar geometry, as a building block for depth-aware media and computational imaging.
MIT 2018 research baseline. The documented Python 3.5/TensorFlow 1.x environment is old; dataset, weights and modern reproduction review are pending. Documentation screening only; not installed or tested.

- [Official overview](https://github.com/chshin10/epinet/blob/master/README.md)
- [Complete reviewed software license](https://github.com/chshin10/epinet/blob/master/LICENSE)
### MAC Multi-Agent CAD · MIT

Draft editable objects and experimental assemblies for design exploration.
Use language-model planning, code generation and visual/geometric checks to build editable CAD parts and experimental multi-part assemblies.
MIT source; paid model access may apply. Assemblies are a technology preview, curated examples are not general success rates, and dimensions/joints need manual checks. Full dependency and hardware review is pending. Documentation screening only; not installed or tested.

- [Official overview](https://github.com/Pan-Chera/Multi-Agent-CAD/blob/main/README.md)
- [Complete reviewed software license](https://github.com/Pan-Chera/Multi-Agent-CAD/blob/main/LICENSE)
### Forgent3D · MIT

Inspect and iterate on agent-authored parametric geometry.
Give coding agents a local parametric CAD rebuild, screenshot and geometry-feedback loop around editable parts and assemblies.
MIT desktop source. The README points release downloads to a differently named repository; packaging, supported platforms and external agent requirements need verification before an installation recommendation. Documentation screening only; not installed or tested.

- [Official overview](https://github.com/forgent3d/forgent3d-desktop/blob/main/README.md)
- [Complete reviewed software license](https://github.com/forgent3d/forgent3d-desktop/blob/main/LICENSE)
### Radiance for ComfyUI · GPL-3.0

Prototype estimated HDR and VFX delivery workflows inside ComfyUI.
Use learned RUDRA SDR-to-HDR recovery alongside ComfyUI color-management, image-review and VFX delivery nodes.
GPL-3.0 software reviewed in full; RUDRA weights are explicitly non-commercial. Full node/model compatibility and hardware review are pending, and estimated HDR content is not a measurement of the original scene. Documentation screening only; not installed or tested.

- [Official overview](https://github.com/FXTD-Studios/radiance/blob/main/README.md)
- [Complete reviewed software license](https://github.com/FXTD-Studios/radiance/blob/main/LICENSE)
### Neural Gaffer · MIT

Explore alternate illumination for object photographs and radiance fields.
Condition a diffusion model on target environment lighting to relight object photographs, with a separate radiance-field relighting research path.
MIT code with released inference/training scripts and checkpoint links. CUDA installation, weights/dataset permissions and reproducibility need a full profile; demonstrations were not reproduced. Documentation screening only; not installed or tested.

- [Official overview](https://github.com/Haian-Jin/Neural_Gaffer/blob/main/README.md)
- [Complete reviewed software license](https://github.com/Haian-Jin/Neural_Gaffer/blob/main/LICENSE)
### Neural Face Rigging · MIT

Retarget facial expressions onto a custom character mesh.
Use a learned face-rig representation to transfer facial animation onto custom meshes with different topology.
MIT research code. Ubuntu/CUDA is the documented tested setup; Windows needs a manual PyTorch3D path. Mesh preparation, training assets and weight terms remain under review. Documentation screening only; not installed or tested.

- [Official overview](https://github.com/dafei-qin/NFR_pytorch/blob/master/readme.md)
- [Complete reviewed software license](https://github.com/dafei-qin/NFR_pytorch/blob/master/LICENSE)
### NoPo4D · MIT

Study dynamic scene reconstruction from multiple video views.
Reconstruct dynamic Gaussian scenes from multi-view video with a learned depth/camera backbone and motion encoder, without supplied camera poses.
MIT inference code and a linked checkpoint; training code remains unreleased. CUDA/model requirements and model-weight terms need a detailed review. Browser examples use a smaller input setting than paper benchmarks. Documentation screening only; not installed or tested.

- [Official overview](https://github.com/bralani/NoPo4D/blob/main/README.md)
- [Complete reviewed software license](https://github.com/bralani/NoPo4D/blob/main/LICENSE)
### FashionAIStudio notebook · MIT

Create preliminary garment concept images in an educational notebook.
Generate clothing concept images with an SDXL-Turbo notebook that turns garment and accessory inputs into prompts.
MIT notebook, inspected directly. This is a small CUDA/Colab educational template; README claims of multi-angle viewing and personalized recommendations were not established in the notebook. Model terms and device requirements remain pending. Documentation screening only; not installed or tested.

- [Official overview](https://github.com/RDreamStudios/FashionAIStudio/blob/main/README.md)
- [Complete reviewed software license](https://github.com/RDreamStudios/FashionAIStudio/blob/main/LICENSE)
- [Reviewed implementation notebook](https://github.com/RDreamStudios/FashionAIStudio/blob/main/FashionAIStudio.ipynb)
### AIAvatarKit · Apache-2.0

Develop voiced characters, interactive signage and conversational installations.
Combine speech recognition, language-model dialogue and speech synthesis with expressions and animation for conversational characters and installations.
Apache-2.0 framework. Default setup uses an OpenAI key and VOICEVOX-compatible server; hosts, voices and services have separate terms. Latency claims and deployment requirements need deeper review. Documentation screening only; not installed or tested.

- [Official overview](https://github.com/uezo/aiavatarkit/blob/main/README.md)
- [Complete reviewed software license](https://github.com/uezo/aiavatarkit/blob/main/LICENSE)
### StreamDiffusionV2 · Apache-2.0

Prototype camera-driven video stylization for performance or streaming.
Apply video diffusion to live video streams with rolling attention caches and motion-aware scheduling for interactive visual transformations.
Apache-2.0 software; Linux/NVIDIA is the documented route. The headline frame-rate figures use multiple H100 GPUs, not a generic personal computer. Full model licensing and setup review is pending. Documentation screening only; not installed or tested.

- [Official overview](https://github.com/chenfengxu714/StreamDiffusionV2/blob/master/README.md)
- [Complete reviewed software license](https://github.com/chenfengxu714/StreamDiffusionV2/blob/master/LICENSE)
### 3D AR Studio · Apache-2.0

Assemble and share generated or imported objects in a browser AR scene.
Combine a documented external text-to-3D service with editable browser scenes and WebXR/phone AR handoff.
Apache-2.0 studio source. The model-generation service has separate availability and terms; its keyless default is not evidence of an open backend. Camera/orientation preview is not universal world-tracked AR. Full hardware/platform review is pending. Documentation screening only; not installed or tested.

- [Official overview](https://github.com/nirholas/3D-AR-Studio/blob/main/README.md)
- [Complete reviewed software license](https://github.com/nirholas/3D-AR-Studio/blob/main/LICENSE)
### DHM Hybrid · Apache-2.0

Explore holographic phase imagery and three-dimensional surface visualization.
Use an optional residual U-Net correction path in a holographic phase-reconstruction and 3D-surface visualization workbench; using those scientific images in an installation is an editorial application idea.
Apache-2.0 source. Classical reconstruction alone is not AI, and no laboratory data or trained model ships with the project; the neural route requires independent training. Full practical review is pending; no medical or measurement accuracy claim is made. Documentation screening only; not installed or tested.

- [Official overview](https://github.com/emircbngl/dhm-hybrid/blob/main/README.md)
- [Complete reviewed software license](https://github.com/emircbngl/dhm-hybrid/blob/main/LICENSE)

## Excluded and unresolved findings

Research notes only; these do not enter the eligible tool library.

- **FastGS and 4C4D** · excluded: MIT labels at repository level do not resolve the non-commercial Inria notices retained in rendering source files. These versions are not cleared as wholly open-source software recommendations. Historical editions are preserved. [Source](https://github.com/fastgs/FastGS/blob/main/scene/gaussian_model.py) [Source](https://github.com/yangzf-1023/4C4D/blob/main/scene/gaussian_model.py)
- **XRMoGen** · excluded: The complete combined license includes Apache terms alongside non-commercial S-Lab/Jukebox-derived software provisions. The combined tool does not meet this library’s open-source software requirement. [Source](https://github.com/openxrlab/xrmogen/blob/main/LICENSE)
- **Fugleramme** · needs-license-review: Its MIT application depends on a separate BirdNET-Go component whose README states a non-commercial code license. End-to-end software eligibility needs clarification before promotion to a full guide. [Source](https://github.com/arnegiacomo/fugleramme) [Source](https://github.com/tphakala/birdnet-go)
- **InfiniteDance** · excluded: The official release describes non-commercial academic terms; it is research context rather than an eligible open-source tool. [Source](https://huzhongyyuan.github.io/InfiniteDance/)
- **Timeline Studio** · needs-license-review: The full license is MIT, but the README separately says the tool is intended solely for technical research and learning. That mixed message needs clarification before this strict open-source library treats the whole tool as cleared. [Source](https://github.com/MartinDelophy/ai-video-editor) [Source](https://github.com/MartinDelophy/ai-video-editor/blob/main/LICENSE)
- **FAST-RIR** · excluded: The maintainer reports losing access to shared training data and model artifacts. The code license is open, but a reliable current pretrained installation route was not established. [Source](https://github.com/anton-jeran/FAST-RIR)
- **AI Clothing Fashion Design Generator** · needs-license-review: The wrapper has an MIT license but includes a multi-model IDM-VTON workflow whose bundled/dependency permissions were not fully resolved in this review. It is held for a dependency-license audit. [Source](https://github.com/nuwandda/ai-clothing-fashion-design-generator)
- **Graspable** · needs-license-review: The live XR product site did not establish released source and a complete open-source software license. Free access alone is insufficient. [Source](https://graspable.dev/)
- **AromaGen** · needs-license-review: The primary paper presents a generative olfactory interface, but accessible released code and a complete software license were not established. [Source](https://arxiv.org/abs/2604.01650)
- **Strike a Chord! Modal Kinetic Typography** · needs-license-review: The September 29 primary preprint describes diffusion-supervised glyph motion; released implementation and license remain unresolved. [Source](https://arxiv.org/abs/2609.38325)
- **Jewelry-generation prototypes** · needs-license-review: Three promising jewelry repositories did not expose a complete software license in their collected snapshots. [Source](https://github.com/CMPN-CODECELL/Syrus2026_JAIS) [Source](https://github.com/advaiTtTtTt/jewelry-ai) [Source](https://github.com/sidd707/Aurigen-AI-Powered-Jewelry-Design-Studio)
- **MotionNet on GitLab** · excluded: Source inspection found a specification repository, without a runnable AI choreography implementation. [Source](https://gitlab.com/Roxanne_Ardary/motionnet)
- **MiMoType, DepthAITestbed and SewSynth** · excluded: MiMoType did not establish an AI runtime or full license; DepthAITestbed documents stereo depth only; SewSynth’s short overview did not identify a concrete implemented AI contribution. These were not admitted solely from names or metadata. [Source](https://github.com/gyoomei/mimotype) [Source](https://github.com/keijiro/DepthAITestbed) [Source](https://github.com/agrow/sewsynth)
- **Local AI Apps (local-ai-service)** · needs-license-review: The complete root license is Apache-2.0, while the audio sub-application README still calls the project learning/research-licensed. This inconsistent software documentation needs clarification before promotion to a full guide; separate model restrictions also apply. [Source](https://github.com/capricorncd/local-ai-service) [Source](https://github.com/capricorncd/local-ai-service/blob/main/apps/audio/README.md)

Source collection completed: 2026-10-09T12:44:23.975913+00:00
Search is a bounded sample. Stars and recent pushes are discovery signals, not verified quality or meaningful upgrades.
