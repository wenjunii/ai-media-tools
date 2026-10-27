# AI Media Scout — 2026-10-27

Expanded research covers 72 creative fields with 582 repository queries and 18 model tasks, including new rendering-denoising, media-quality-analysis and print-prepress searches. This edition provides 52 detailed profiles (37 first additions, 14 completed earlier leads and one substantive update) plus two additional screened leads, adding 39 library entries. The localized SolidCraft derivative is explicitly distinguished from its existing upstream entry. Highlights include new local/browser/Android tools, fuller guides for earlier screened entries, and Audio Studio MCP 1.0’s substantive browser-UI update. Code licensing is reviewed separately from weights, services and assets. The weekly review covered all 1,197 entries present at the start of this run; today’s records also receive fresh six-check assessments. Quality gaps remain explicit, with no popularity-based promotion. No discovered tool was installed or run. All 582 repository queries were attempted: 293 succeeded, 198 failed and 91 were partial, with 89 bounded/truncated results. All 18 model-task queries completed. GitHub HTTP 403 failures and blocked Codeberg/SourceHut access leave coverage gaps; this is broad bounded research, not an exhaustive inventory.

Documentation reviewed today. Tools are not hands-on tested unless explicitly stated. Requirements and performance remain source-specific.

## Coverage

| Field | Finding |
| --- | --- |
| Images & design | OpenFill adds local editor inpainting; OpenPixels supplies a GitLab-hosted browser restoration workflow. Code and model rights are assessed separately. [Source 1](https://github.com/beckettharriman/openfill) [Source 2](https://openpixels.app/) |
| Video, animation & film | Repo2Reels and SubGenPlayer cover narrated short-form output and editable subtitles. Video-editor searches also revisited existing tools without recycling unchanged guides. [Source 1](https://github.com/sravinp-art/Repo2Reels) [Source 2](https://openfilm.dev/) |
| Audio, music & voice | Audio Studio MCP 1.0 receives a concrete browser-UI update. Sonicproof and Voiceolator cover selection/QC and voice isolation, not interchangeable generation tasks. [Source 1](https://github.com/kanaworksai-hue/audio-studio-mcp/releases/tag/v1.0.0) [Source 2](https://pypi.org/project/sonicproof/) |
| 3D, reconstruction & assets | New and completed guides cover image-to-CAD, reconstruction, asset selection and toon looks; editable geometry does not establish manufacturing suitability. [Source 1](https://arxiv.org/abs/2505.14646) [Source 2](https://fastgs.github.io/) |
| Browser tools & web media | Added two neural WebGPU denoisers and browser photo/CAD interfaces, with device support kept specific to the documented runtime. [Source 1](https://pmndrs.github.io/denoiser/docs/) [Source 2](https://hush.tokyoaivisuals.club) |
| WebXR, VR & AR | Albie adds a Quest voice-driven spatial CAD workspace with paid service/asset dependencies and a fresh-clone asset gap. No headset testing was performed by the scout. [Source 1](https://github.com/builtbyd3v/Albie) [Source 2](https://github.com/builtbyd3v/Albie/blob/main/docs/SETUP.md) |
| Computational art & creative coding | SciSketch and Lumen connect AI to editable visual structures and data-driven media; generated structures still require human inspection. [Source 1](https://aclanthology.org/2025.emnlp-demos.28/) [Source 2](https://lumen.holoviz.org/) |
| Interactive, immersive & live media | AirMIDI and Robo-Flower provide gesture-controlled sound and physical interaction. Local timing and mechanical behavior remain untested by the scout. [Source 1](https://github.com/kesharishaurya007/Airwave) [Source 2](https://github.com/SamuelAlexander/robo-flower) |
| 3D printing & generative CAD | CAD-Coder and Paloan Jewelry CAD support concept/CAD workflows. Exported STL/STEP does not prove fit, strength or castability. [Source 1](https://arxiv.org/abs/2505.14646) [Source 2](https://rubelpublic.github.io/paloan-jewelry-cad/) |
| Games & production pipelines | Reviewed audio generation/cleaning and source-attributed 3D asset retrieval for game work; no popularity threshold is used as quality proof. [Source 1](https://github.com/Schockgeber/voiceolator) [Source 2](https://github.com/jeak01/3d-asset-agent-skills) |
| Motion capture & character animation | anymove adds AI-video-driven creature capture with documented multi-leg/lying-down failures. G1 dance covers a separate human-to-robot simulation workflow. [Source 1](https://github.com/patch-gg/anymove) [Source 2](https://github.com/guoshuhao066-code/g1-dance-pipeline) |
| Avatars, digital humans & lip sync | Completed VRM conversation and agent-assisted avatar-build guides, separating neural services, conventional shaders and proprietary host requirements. [Source 1](https://github.com/dexvdev/svelte-vrm-live) [Source 2](https://github.com/hrabanazviking/Seidr-Smidja) |
| VFX, compositing & relighting | Neural denoising and dynamic Gaussian capture are included. UniRelight surfaced as adjacent research, without inferring its checkpoint terms from a listing. [Source 1](https://pmndrs.github.io/denoiser/) [Source 2](https://huggingface.co/nvidia/UniRelight) |
| Spatial audio & volumetric media | FastGS and the 4D capture scaffold now have fuller guides. CPU staging, trained reconstruction and a production spatial experience are separate outcomes. [Source 1](https://fastgs.github.io/) [Source 2](https://github.com/backblaze-b2-samples/4d-gaussian-splatting-volumetric-capture) |
| Photogrammetry, scanning & neural rendering | Reviewed calibrated capture-to-splat processing and neural camera research; hardware minima remain unknown where authors do not state them. [Source 1](https://github.com/backblaze-b2-samples/4d-gaussian-splatting-volumetric-capture) [Source 2](https://iilab.io/IFIN/) |
| Editing, captions & post-production | OpenFill, OpenPixels and the Audio Studio browser update add concrete editing workflows with original-preserving or comparison controls. [Source 1](https://github.com/beckettharriman/openfill) [Source 2](https://openpixels.app/) |
| Vector graphics, illustration & textures | SciSketch exposes diagram composition with SVG assets; no claim is made that every generated figure is a semantically correct editable CAD/vector object. [Source 1](https://github.com/yale-nlp/SciSketch) [Source 2](https://aclanthology.org/2025.emnlp-demos.28/) |
| Typography, fonts & layout | Repo2Reels combines generated speech with timed word captions. Conventional kinetic-type tools surfaced but were not admitted without an AI contribution. [Source 1](https://github.com/sravinp-art/Repo2Reels) [Source 2](https://www.hinzandkunz.com/moving-typo/) |
| Storyboarding, narrative & comics | Lumen narrative-report mode and local dictation support visual/story drafting; existing story-writing sites were researched without re-listing unchanged tools. [Source 1](https://lumen.holoviz.org/getting_started/using_lumen_ai/) [Source 2](https://docs.storyforge-lab.com/en/) |
| Creative publishing & presentation | Added short-reel generation and report exports; none of these findings authorizes or performs social publication. [Source 1](https://github.com/sravinp-art/Repo2Reels) [Source 2](https://lumen.holoviz.org/getting_started/using_lumen_ai/) |
| Photography, restoration & color | OpenPixels and Mitsuke cover enhancement and local visual retrieval. Enhancement can invent detail; search relevance and restoration fidelity need different checks. [Source 1](https://openpixels.app/) [Source 2](https://github.com/kanaworksai-hue/mitsuke) |
| Data art & scientific visualization | Lumen and SciSketch receive detailed guides. Charts and scientific figures must still be checked against their input evidence. [Source 1](https://lumen.holoviz.org/) [Source 2](https://aclanthology.org/2025.emnlp-demos.28/) |
| Physical, robotic & kinetic installations | Kinetic sculpture and a heritage-guide prototype broaden the installation workflow coverage. A source demo does not establish unattended venue readiness. [Source 1](https://github.com/SamuelAlexander/robo-flower) [Source 2](https://github.com/thanhnhan04/champa-vision-rag) |
| Performance, projection & stage media | Gesture MIDI, robot-dance simulation and kinetic sculpture were reviewed as distinct creative-performance routes with different hardware responsibilities. [Source 1](https://github.com/kesharishaurya007/Airwave) [Source 2](https://github.com/guoshuhao066-code/g1-dance-pipeline) |
| Fashion, textiles & wearable media | Avatar look development and neural garment research were revisited; a simulation paper does not establish pattern-making or fit accuracy. [Source 1](https://github.com/kanaworksai-hue/mochitoon) [Source 2](https://4dqv.mpi-inf.mpg.de/NeuralGarSim/) |
| Accessible media & assistive creation | SubGenPlayer, Tsuzuri and XiaoFu support transcription/caption workflows. Cloud ASR and on-device recognition are explicitly distinguished. [Source 1](https://github.com/megatih/SubGenPlayer) [Source 2](https://github.com/Jolly-J/XiaoFu) |
| Mobile, edge & on-device creation | XiaoFu adds an Android workflow, while browser/native OpenPixels capabilities are kept separate; phone support is never inferred solely from a web UI. [Source 1](https://github.com/Jolly-J/XiaoFu) [Source 2](https://gitlab.com/openpixelsapp/OpenPixels/-/blob/main/MODELS.md) |
| Creative learning & authoring | Scientific diagrams and Champa visual retrieval provide educational use cases. Neither generated explanation nor a polished demo proves factual accuracy. [Source 1](https://github.com/yale-nlp/SciSketch) [Source 2](https://github.com/thanhnhan04/champa-vision-rag) |
| Archives, media restoration & collections | Heritage-image retrieval and photograph enhancement were reviewed with dataset attribution and invented-detail limits retained. [Source 1](https://github.com/thanhnhan04/champa-vision-rag) [Source 2](https://openpixels.app/) |
| Emerging & cross-disciplinary creative AI | Adjacent searches included scientific diagramming, neural rendering, biosignal reconstruction and new local applications. Boundaries are creative AI relevance and licensing, not the starter categories. [Source 1](https://aclanthology.org/2025.emnlp-demos.28/) [Source 2](https://arxiv.org/abs/2507.09747) |
| Tactile, vibration and haptic media | HapticGen primary research was searched. No new haptic application with a completed code-license and hardware review cleared this pass. [Source 1](https://hapticgen.hcitech.org/) |
| Neural acoustics and responsive sound spaces | Image2Reverb remains a concrete neural-acoustics research direction; no new eligible release was established from the bounded primary-source search. [Source 1](https://jeffmentch.com/projects/image2reverb/) |
| AI agents for code-authored media production | MochiToon, Seidr-Smidja and 3D Asset Agent Skills document agent-assisted creative operations. The scout reads these instructions as evidence and does not execute them. [Source 1](https://github.com/kanaworksai-hue/mochitoon) [Source 2](https://github.com/jeak01/3d-asset-agent-skills) |
| AI kinetic typography and animated lettering | Repo2Reels supplies timed captions and motion-graphic scenes driven by generated speech. It is currently English-only. [Source 1](https://github.com/sravinp-art/Repo2Reels) |
| AI choreography and dance composition | Completed the G1 dance-pipeline guide around retargeting, learned policies and simulation. Hardware deployment remains a separate supervised validation step. [Source 1](https://github.com/guoshuhao066-code/g1-dance-pipeline) |
| AI-assisted textile and computational craft | Jewelry and ceramic-design code were inspected. The ceramic repository’s sparse instructions do not yet support a complete practical guide, so its existing pending entry is preserved. [Source 1](https://github.com/rubelpublic/paloan-jewelry-cad) [Source 2](https://github.com/ali-Eskandarian/Ceramic-Design-Generative-AI) |
| AI music notation and score recovery | Ruach Studio’s score/piano-roll route and optical music-recognition sources were reviewed; notation editing is distinct from neural audio generation. [Source 1](https://github.com/igrbible/Ruach_Studio) [Source 2](https://symphoniaio.github.io/) |
| Neural relighting and material recovery | Neural-PBIR and UniRelight surfaced in primary research; HoloLab’s optical shader effect is not mislabeled as learned relighting. [Source 1](https://neural-pbir.github.io/) [Source 2](https://huggingface.co/nvidia/UniRelight) |
| Olfactory and multisensory AI media | Anemoia research/artwork was located, but an accessible artwork description did not establish an eligible reusable software release. [Source 1](https://www.media.mit.edu/projects/anemoia-device/overview/) |
| AI architectural visualization and spatial design | RoomSmith and BIM-oriented projects were searched. No additional fully screened architecture tool was inferred from promotional capability claims. [Source 1](https://rumeasiyan.github.io/roomsmith/) [Source 2](https://www.bimtex.dev/) |
| Neural holography and light-field media | Neural holography research remains relevant; HoloLab’s browser card effect is not presented as a light-field or physical holographic display. [Source 1](https://research.nvidia.com/publication/2020-08_neural-holography) [Source 2](https://github.com/Elijah-Lin-Dancer/Holo-Card-Studio) |
| Neural rigging and digital puppetry | VRM speech/animation and gesture systems were examined as digital-puppetry building blocks, with no claim of ready stage operation. [Source 1](https://github.com/dexvdev/svelte-vrm-live) [Source 2](https://github.com/kesharishaurya007/Airwave) |
| AI ceramics and archaeological illustration | PyPottery research and the retained ceramic GAN candidate were inspected. No supported manufacturing-ready ceramic workflow was established today. [Source 1](https://lrncrd.github.io/PyPottery/) [Source 2](https://github.com/ali-Eskandarian/Ceramic-Design-Generative-AI) |
| AI parametric design and jewelry | CAD-Coder and Paloan Jewelry CAD have detailed guides; generated construction code still needs geometry and fabrication review. [Source 1](https://arxiv.org/abs/2505.14646) [Source 2](https://rubelpublic.github.io/paloan-jewelry-cad/) |
| AI cartography and artistic maps | Lumen and Mundi primary documentation were researched for AI-assisted geospatial visualization; no map’s factual accuracy is inferred from successful rendering. [Source 1](https://lumen.holoviz.org/) [Source 2](https://docs.mundi.ai/) |
| AI robotic painting and drawing | Robo-Flower and G1 dance workflows extend physical-art coverage, with explicit prototype/simulation boundaries. [Source 1](https://github.com/SamuelAlexander/robo-flower) [Source 2](https://github.com/guoshuhao066-code/g1-dance-pipeline) |
| AI cel animation and inbetweening | MochiToon provides agent-assisted Blender toon look development. MotionCel surfaced but its complete software grant was not established in this pass. [Source 1](https://github.com/kanaworksai-hue/mochitoon) [Source 2](https://motioncel.com/) |
| AI Foley and sound effects | Sonicproof and the Audio Studio update address effect selection and generation; FoleyCrafter and ControlFoley remain adjacent primary research. [Source 1](https://github.com/kanaworksai-hue/sonicproof) [Source 2](https://foleycrafter.github.io/) [Source 3](https://huggingface.co/YJX-Xiaomi/ControlFoley) |
| Learned media codecs and neural delivery | Current compression research was searched; no new codec was promoted from a paper or package listing without its complete license review. [Source 1](https://machinelearning.apple.com/research/compression) |
| AI assisted sound data art and corpus instruments | YOLO sonification code and generative-performance research were inspected. The existing YOLO lead remains pending because practical setup/runtime documentation is sparse. [Source 1](https://github.com/filip-dobrocky/YOLO-sonification) [Source 2](https://www.media.mit.edu/projects/jordan-rudess-genai/overview/) |
| AI biosignal art and neurointeractive media | BrainFLORA now has a full dataset-oriented guide; live EEG artworks and BrainArt were also inspected without inferring a complete live neural pipeline from a title. [Source 1](https://arxiv.org/abs/2507.09747) [Source 2](https://www.amykarle.com/project/cortical_echoes/) |
| Neural procedural material authoring | Loom adds an explicit AI-agent PBR-material authoring and preview-feedback workflow; its procedural renderer is distinguished from neural texture inference. [Source 1](https://research.nvidia.com/labs/rtr/publication/yu2026toward/) [Source 2](https://github.com/uilianks/loom) |
| Neural cameras and unconventional image capture | IFIN and lensless-learning sources were researched; no new camera system was admitted solely from reconstruction illustrations. [Source 1](https://iilab.io/IFIN/) [Source 2](https://waller-lab.github.io/LenslessLearning/index.html) |
| AI origami, kirigami and paper engineering | COrigami and a robotic-origami benchmark were searched. Benchmark or paper availability does not establish an installable licensed folding tool. [Source 1](https://arxiv.org/abs/2606.26299) [Source 2](https://bitrobot.ai/grand-challenges/robotic-origami) |
| AI landscape, garden and environmental design | Landscape-design services and research surfaced, but an eligible released codebase was not established from the reviewed primary pages. [Source 1](https://ailandscape.garden/about) [Source 2](https://ieeexplore.ieee.org/abstract/document/11142324) |
| Neural mosaic and stained-glass media | The mosaic-specific query did not establish a newly eligible application. Adjacent pixel-pattern/halftoning code remains under review and is not assumed to solve mosaic assembly. [Source 1](https://github.com/Nikronic/Deep-Halftoning) |
| AI optical illusions and anamorphic media | Diffusion Illusions, LookingGlass and PTDiffusion were searched as illusion-generation directions; viewing-condition robustness remains separate from a demo. [Source 1](https://diffusionillusions.com/) [Source 2](https://lookingglass-lpw.github.io/) [Source 3](https://xianggao1102.github.io/PTDiffusion_webpage/) |
| AI relief engraving and learned halftoning | Deep-Halftoning’s current README explicitly says the paper numbers are not reproducible. It remains a pending research lead, not a production engraving recommendation. [Source 1](https://nikronic.com/projects/deep-halftoning_project/) [Source 2](https://github.com/Nikronic/Deep-Halftoning) |
| Neural brushstroke painting and drawn media | PaintCopilot primary research was found, but this pass did not establish a complete installable code-and-license package for admission. [Source 1](https://paintcopilot.github.io/) |
| AI color direction and palette-based media | Chromary supplies agent color skills and a runnable MCP example. Its educational links, deterministic playground and AI-assisted workflow are distinguished, and accessibility/print guarantees are not inferred. [Source 1](https://github.com/izynu/chromary) [Source 2](https://rampa.design/) |
| AI collage, cut-paper composition and layered media | The collage-specific search did not produce a new fully reviewed licensed application. OpenFill’s layer-based edits are adjacent functionality, not a claim of automatic collage composition. [Source 1](https://github.com/beckettharriman/openfill) |
| AI stereo conversion and spatial video authoring | Spatial Video Studio and stereo-generation sources were searched. A commercial demo or a stereo pair alone does not satisfy the open-source boundary or prove comfortable VR viewing. [Source 1](https://www.spatial-video-studio.com/en) |
| AI semantic editing of captured 3D scenes | ArtisanGS, Semantic Gaussians and ManifoldSplat were researched. Semantic selection/editing results remain specific to their published scene and model conditions. [Source 1](https://research.nvidia.com/labs/sil/projects/ArtisanGS/) [Source 2](https://semantic-gaussians.github.io/) [Source 3](https://arxiv.org/abs/2610.03599) |
| AI signing avatars and expressive gesture media | SignFlow and sign-avatar research were searched; language/community validation and complete implementation terms remain requirements, not assumed capabilities. [Source 1](https://github.com/Leander-bai/SignFlow) [Source 2](https://aclanthology.org/2022.sltat-1.pdf) |
| AI assisted audio plugin and DSP authoring | Ruse and UL-UNAS cover agent-authored DSP and learned speech cleanup respectively. A source package does not prove real-time reliability in a chosen host. [Source 1](https://www.symbia-labs.com/ruse/) [Source 2](https://xiaobin-rong.github.io/ul-unas_demo/) |
| AI panoramic worlds and virtual tour creation | World/scene-generation research was searched alongside reconstruction tools. No new complete panoramic/VR application cleared additional review in this pass. [Source 1](https://github.com/backblaze-b2-samples/4d-gaussian-splatting-volumetric-capture) [Source 2](https://fastgs.github.io/) |
| Learned garment simulation and digital clothing | NeuralGarSim and related garment-simulation sources were searched. Rendering or simulated drape is not physical fit validation. [Source 1](https://4dqv.mpi-inf.mpg.de/NeuralGarSim/) [Source 2](https://dumoulina.github.io/dit-garment/) |
| AI visual dubbing and translated performance | TBDub and distinct OpenDub projects surfaced. Their code/model licenses and actual local/cloud behavior require separate review before new admission. [Source 1](https://taoliveaigc.github.io/TBDub/) [Source 2](https://opendub.app/) |
| Neural video reshooting and camera control | CameraAnything and camera-control research were searched; no unreviewed checkpoint was added solely because a demo looked compelling. [Source 1](https://yixuanli98.github.io/cameraanything/) |
| Neural denoising for real-time creative rendering | New adaptive field: Hush and pmndrs Denoiser receive guides with current prototype/alpha evidence, model scope and device-validation limits. [Source 1](https://hush.tokyoaivisuals.club) [Source 2](https://pmndrs.github.io/denoiser/docs/) |
| AI assisted media quality and take selection | New adaptive field: Sonicproof scores/selects audio and Mitsuke retrieves visual references. Automated scores and nearest neighbors do not establish artistic quality. [Source 1](https://pypi.org/project/sonicproof/) [Source 2](https://github.com/kanaworksai-hue/mitsuke) |
| AI print separation and prepress authoring | New adaptive field: learned halftoning was reviewed; ordinary PDF/print utilities do not qualify as AI, and the retained neural code has unresolved reproducibility. [Source 1](https://nikronic.com/projects/deep-halftoning_project/) [Source 2](https://github.com/Nikronic/Deep-Halftoning) |

## Search and review counts

72 creative fields; 582/582 repository queries attempted; 18/18 model-task queries attempted. 15772 distinct source candidates and 856 model leads. 52 detailed profiles and 2 additional screened discoveries. Source gaps: 198 failed repository queries, 91 partial repository queries, 89 bounded repository queries, 0 failed model-task queries and 2 web ecosystem gaps. Raw search candidates include duplicates of known tools, excluded projects and projects awaiting review; they are not verified recommendations.

## Research beyond GitHub

- **gitlab** · searched: Archived the official OpenPixels README, complete MIT/Apache license files and model provenance; added a full browser-workflow guide with explicit native-platform and account-documentation limits. [Source](https://gitlab.com/openpixelsapp/OpenPixels)
- **codeberg** · gap: Live source-group searches encountered robots/access restrictions; coverage remains incomplete. No absence of eligible tools is inferred and no restriction was bypassed.
- **sourcehut** · gap: Live source-group searches encountered robots/access restrictions; the source group remains a documented coverage gap.
- **packages** · searched: Read Sonicproof and Lumen package/release information and followed original project/model documentation; package publication is not a quality endorsement. [Source](https://pypi.org/project/sonicproof/) [Source](https://pypi.org/project/lumen/)
- **creative-plugins** · searched: Reviewed current OpenFill editor integrations and MochiToon agent-assisted Blender workflow, including host requirements and explicit testing-stage evidence. [Source](https://github.com/beckettharriman/openfill) [Source](https://github.com/kanaworksai-hue/mochitoon)
- **project-sites** · searched: Followed official Tokyo AI Visuals, Hush, OpenPixels, FastGS and other creative/research sites; conventional non-AI releases were not admitted just because the publisher also makes AI tools. [Source](https://www.tokyoaivisuals.com/en/open-source-week) [Source](https://hush.tokyoaivisuals.club) [Source](https://openpixels.app/)
- **research-code** · searched: Followed SciSketch, CAD-Coder, BrainFLORA and neural rendering research to released source. Model access/terms and research hardware remain separate from code licensing. [Source](https://aclanthology.org/2025.emnlp-demos.28/) [Source](https://arxiv.org/abs/2505.14646) [Source](https://arxiv.org/abs/2507.09747)
- **international** · searched: Read Japanese MochiToon, Chinese XiaoFu/GANCalligraphy and Vietnamese Champa documentation using the same licensing and evidence standards; cloud-ASR and model-rights caveats are explicit. [Source](https://github.com/kanaworksai-hue/mochitoon) [Source](https://github.com/Jolly-J/XiaoFu) [Source](https://github.com/thanhnhan04/champa-vision-rag)

## Collection limitations

- images: bounded or incomplete query: topic:diffusion pushed:>=2026-09-27 is:public fork:false archived:false (100 of 54 matches sampled)
- images: bounded or incomplete query: topic:diffusion is:public fork:false archived:false (200 of 1485 matches sampled)
- images: bounded or incomplete query: AI image generation pushed:>=2026-09-27 is:public fork:false archived:false (200 of 1695 matches sampled)
- images: bounded or incomplete query: AI image generation created:>=2026-09-27 is:public fork:false archived:false (96 of 856 matches sampled)
- images: bounded or incomplete query: AI image generation is:public fork:false archived:false (200 of 15940 matches sampled)
- video: bounded or incomplete query: AI video pushed:>=2026-09-27 is:public fork:false archived:false (200 of 14825 matches sampled)
- video: bounded or incomplete query: AI video created:>=2026-09-27 is:public fork:false archived:false (9 of 9810 matches sampled)
- video: HTTP 403 from api.github.com/search/repositories; source not collected
- video: HTTP 403 from api.github.com/search/repositories; source not collected
- video: HTTP 403 from api.github.com/search/repositories; source not collected
- video: HTTP 403 from api.github.com/search/repositories; source not collected
- audio: HTTP 403 from api.github.com/search/repositories; source not collected
- audio: HTTP 403 from api.github.com/search/repositories; source not collected
- audio: HTTP 403 from api.github.com/search/repositories; source not collected
- audio: HTTP 403 from api.github.com/search/repositories; source not collected
- audio: bounded or incomplete query: AI audio created:>=2026-09-27 is:public fork:false archived:false (200 of 2199 matches sampled)
- audio: bounded or incomplete query: AI audio is:public fork:false archived:false (200 of 29187 matches sampled)
- 3d: bounded or incomplete query: 3D generation pushed:>=2026-09-27 is:public fork:false archived:false (200 of 674 matches sampled)
- 3d: bounded or incomplete query: 3D generation created:>=2026-09-27 is:public fork:false archived:false (95 of 317 matches sampled)
- 3d: bounded or incomplete query: 3D generation is:public fork:false archived:false (200 of 5996 matches sampled)
- 3d: bounded or incomplete query: topic:3d-reconstruction pushed:>=2026-09-27 is:public fork:false archived:false (161 of 198 matches sampled)
- 3d: bounded or incomplete query: topic:3d-reconstruction created:>=2026-09-27 is:public fork:false archived:false (8 of 47 matches sampled)
- 3d: HTTP 403 from api.github.com/search/repositories; source not collected
- 3d: bounded or incomplete query: topic:3d-reconstruction is:public fork:false archived:false (100 of 2044 matches sampled)
- web: HTTP 403 from api.github.com/search/repositories; source not collected
- web: HTTP 403 from api.github.com/search/repositories; source not collected
- web: HTTP 403 from api.github.com/search/repositories; source not collected
- web: HTTP 403 from api.github.com/search/repositories; source not collected
- web: HTTP 403 from api.github.com/search/repositories; source not collected
- web: HTTP 403 from api.github.com/search/repositories; source not collected
- xr: bounded or incomplete query: AI WebXR pushed:>=2026-09-27 is:public fork:false archived:false (44 of 45 matches sampled)
- xr: bounded or incomplete query: AI WebXR created:>=2026-09-27 is:public fork:false archived:false (27 of 28 matches sampled)
- xr: bounded or incomplete query: AI WebXR is:public fork:false archived:false (149 of 150 matches sampled)
- xr: bounded or incomplete query: AI VR pushed:>=2026-09-27 is:public fork:false archived:false (200 of 375 matches sampled)
- xr: bounded or incomplete query: AI VR created:>=2026-09-27 is:public fork:false archived:false (200 of 212 matches sampled)
- xr: bounded or incomplete query: AI VR is:public fork:false archived:false (200 of 2989 matches sampled)
- computational: bounded or incomplete query: AI creative coding pushed:>=2026-09-27 is:public fork:false archived:false (100 of 86 matches sampled)
- computational: bounded or incomplete query: AI creative coding is:public fork:false archived:false (200 of 973 matches sampled)
- computational: bounded or incomplete query: topic:generative-art pushed:>=2026-09-27 is:public fork:false archived:false (53 of 1112 matches sampled)
- computational: HTTP 403 from api.github.com/search/repositories; source not collected
- computational: bounded or incomplete query: topic:generative-art created:>=2026-09-27 is:public fork:false archived:false (100 of 573 matches sampled)
- computational: bounded or incomplete query: topic:generative-art is:public fork:false archived:false (200 of 4340 matches sampled)
- interactive: bounded or incomplete query: StreamDiffusion pushed:>=2026-09-27 is:public fork:false archived:false (9 of 9 matches sampled)
- interactive: bounded or incomplete query: StreamDiffusion is:public fork:false archived:false (13 of 55 matches sampled)
- interactive: bounded or incomplete query: AI interactive art pushed:>=2026-09-27 is:public fork:false archived:false (7 of 26 matches sampled)
- interactive: bounded or incomplete query: AI interactive art created:>=2026-09-27 is:public fork:false archived:false (14 of 14 matches sampled)
- interactive: bounded or incomplete query: AI interactive art is:public fork:false archived:false (200 of 702 matches sampled)
- fabrication: bounded or incomplete query: AI CAD pushed:>=2026-09-27 is:public fork:false archived:false (200 of 888 matches sampled)
- fabrication: HTTP 403 from api.github.com/search/repositories; source not collected
- fabrication: HTTP 403 from api.github.com/search/repositories; source not collected
- fabrication: HTTP 403 from api.github.com/search/repositories; source not collected
- fabrication: HTTP 403 from api.github.com/search/repositories; source not collected
- fabrication: HTTP 403 from api.github.com/search/repositories; source not collected
- gaming: HTTP 403 from api.github.com/search/repositories; source not collected
- gaming: HTTP 403 from api.github.com/search/repositories; source not collected
- gaming: HTTP 403 from api.github.com/search/repositories; source not collected
- gaming: HTTP 403 from api.github.com/search/repositories; source not collected
- gaming: HTTP 403 from api.github.com/search/repositories; source not collected
- gaming: HTTP 403 from api.github.com/search/repositories; source not collected
- motion: HTTP 403 from api.github.com/search/repositories; source not collected
- motion: HTTP 403 from api.github.com/search/repositories; source not collected
- motion: bounded or incomplete query: AI motion capture is:public fork:false archived:false (200 of 244 matches sampled)
- motion: bounded or incomplete query: motion generation pushed:>=2026-09-27 is:public fork:false archived:false (61 of 116 matches sampled)
- motion: bounded or incomplete query: motion generation created:>=2026-09-27 is:public fork:false archived:false (35 of 66 matches sampled)
- motion: bounded or incomplete query: motion generation is:public fork:false archived:false (55 of 1576 matches sampled)
- avatars: bounded or incomplete query: AI avatar pushed:>=2026-09-27 is:public fork:false archived:false (200 of 854 matches sampled)
- avatars: bounded or incomplete query: AI avatar created:>=2026-09-27 is:public fork:false archived:false (200 of 481 matches sampled)
- avatars: bounded or incomplete query: AI avatar is:public fork:false archived:false (200 of 6188 matches sampled)
- avatars: HTTP 403 from api.github.com/search/repositories; source not collected
- avatars: bounded or incomplete query: lip sync pushed:>=2026-09-27 is:public fork:false archived:false (100 of 379 matches sampled)
- avatars: HTTP 403 from api.github.com/search/repositories; source not collected
- avatars: HTTP 403 from api.github.com/search/repositories; source not collected
- vfx: HTTP 403 from api.github.com/search/repositories; source not collected
- vfx: HTTP 403 from api.github.com/search/repositories; source not collected
- vfx: HTTP 403 from api.github.com/search/repositories; source not collected
- vfx: HTTP 403 from api.github.com/search/repositories; source not collected
- vfx: HTTP 403 from api.github.com/search/repositories; source not collected
- vfx: HTTP 403 from api.github.com/search/repositories; source not collected
- spatial: HTTP 403 from api.github.com/search/repositories; source not collected
- spatial: bounded or incomplete query: AI spatial audio is:public fork:false archived:false (100 of 81 matches sampled)
- spatial: bounded or incomplete query: volumetric neural rendering pushed:>=2026-09-27 is:public fork:false archived:false (0 of 0 matches sampled)
- capture: bounded or incomplete query: topic:gaussian-splatting pushed:>=2026-09-27 is:public fork:false archived:false (200 of 302 matches sampled)
- capture: bounded or incomplete query: topic:gaussian-splatting created:>=2026-09-27 is:public fork:false archived:false (122 of 122 matches sampled)
- capture: bounded or incomplete query: topic:gaussian-splatting is:public fork:false archived:false (500 of 714 matches sampled)
- capture: bounded or incomplete query: neural reconstruction is:public fork:false archived:false (200 of 1355 matches sampled)
- editing: bounded or incomplete query: AI video editing pushed:>=2026-09-27 is:public fork:false archived:false (200 of 1018 matches sampled)
- editing: bounded or incomplete query: AI video editing created:>=2026-09-27 is:public fork:false archived:false (200 of 671 matches sampled)
- editing: bounded or incomplete query: AI video editing is:public fork:false archived:false (142 of 1083 matches sampled)
- editing: bounded or incomplete query: AI subtitle pushed:>=2026-09-27 is:public fork:false archived:false (200 of 420 matches sampled)
- editing: bounded or incomplete query: AI subtitle created:>=2026-09-27 is:public fork:false archived:false (200 of 217 matches sampled)
- editing: bounded or incomplete query: AI subtitle is:public fork:false archived:false (113 of 750 matches sampled)
- vector: HTTP 403 from api.github.com/search/repositories; source not collected
- vector: HTTP 403 from api.github.com/search/repositories; source not collected
- vector: HTTP 403 from api.github.com/search/repositories; source not collected
- vector: HTTP 403 from api.github.com/search/repositories; source not collected
- vector: HTTP 403 from api.github.com/search/repositories; source not collected
- vector: HTTP 403 from api.github.com/search/repositories; source not collected
- typography: HTTP 403 from api.github.com/search/repositories; source not collected
- typography: HTTP 403 from api.github.com/search/repositories; source not collected
- typography: HTTP 403 from api.github.com/search/repositories; source not collected
- typography: bounded or incomplete query: font generation is:public fork:false archived:false (300 of 214 matches sampled)
- storytelling: bounded or incomplete query: AI storyboard pushed:>=2026-09-27 is:public fork:false archived:false (200 of 512 matches sampled)
- storytelling: bounded or incomplete query: AI storyboard created:>=2026-09-27 is:public fork:false archived:false (200 of 333 matches sampled)
- storytelling: bounded or incomplete query: AI storyboard is:public fork:false archived:false (158 of 466 matches sampled)
- storytelling: bounded or incomplete query: AI comic pushed:>=2026-09-27 is:public fork:false archived:false (175 of 1024 matches sampled)
- storytelling: HTTP 403 from api.github.com/search/repositories; source not collected
- storytelling: HTTP 403 from api.github.com/search/repositories; source not collected
- publishing: HTTP 403 from api.github.com/search/repositories; source not collected
- publishing: HTTP 403 from api.github.com/search/repositories; source not collected
- publishing: HTTP 403 from api.github.com/search/repositories; source not collected
- publishing: HTTP 403 from api.github.com/search/repositories; source not collected
- publishing: HTTP 403 from api.github.com/search/repositories; source not collected
- publishing: bounded or incomplete query: AI publishing is:public fork:false archived:false (200 of 4327 matches sampled)
- photography: bounded or incomplete query: AI photo restoration is:public fork:false archived:false (68 of 210 matches sampled)
- photography: bounded or incomplete query: AI colorization created:>=2026-09-27 is:public fork:false archived:false (200 of 304 matches sampled)
- photography: bounded or incomplete query: AI colorization is:public fork:false archived:false (200 of 4934 matches sampled)
- visualization: bounded or incomplete query: AI visualization pushed:>=2026-09-27 is:public fork:false archived:false (200 of 3458 matches sampled)
- visualization: bounded or incomplete query: AI visualization created:>=2026-09-27 is:public fork:false archived:false (68 of 1671 matches sampled)
- visualization: bounded or incomplete query: AI visualization is:public fork:false archived:false (115 of 38965 matches sampled)
- visualization: HTTP 403 from api.github.com/search/repositories; source not collected
- visualization: HTTP 403 from api.github.com/search/repositories; source not collected
- visualization: HTTP 403 from api.github.com/search/repositories; source not collected
- installation: HTTP 403 from api.github.com/search/repositories; source not collected
- installation: HTTP 403 from api.github.com/search/repositories; source not collected
- performance: bounded or incomplete query: AI live visuals pushed:>=2026-09-27 is:public fork:false archived:false (3 of 8 matches sampled)
- performance: bounded or incomplete query: AI live visuals is:public fork:false archived:false (200 of 350 matches sampled)
- fashion: HTTP 403 from api.github.com/search/repositories; source not collected
- fashion: bounded or incomplete query: AI fashion design is:public fork:false archived:false (100 of 658 matches sampled)
- fashion: HTTP 403 from api.github.com/search/repositories; source not collected
- fashion: HTTP 403 from api.github.com/search/repositories; source not collected
- fashion: HTTP 403 from api.github.com/search/repositories; source not collected
- accessibility: HTTP 403 from api.github.com/search/repositories; source not collected
- accessibility: HTTP 403 from api.github.com/search/repositories; source not collected
- accessibility: HTTP 403 from api.github.com/search/repositories; source not collected
- accessibility: HTTP 403 from api.github.com/search/repositories; source not collected
- accessibility: HTTP 403 from api.github.com/search/repositories; source not collected
- accessibility: HTTP 403 from api.github.com/search/repositories; source not collected
- mobile: bounded or incomplete query: AI mobile media is:public fork:false archived:false (80 of 229 matches sampled)
- education: bounded or incomplete query: AI explainer pushed:>=2026-09-27 is:public fork:false archived:false (200 of 6868 matches sampled)
- education: bounded or incomplete query: AI explainer created:>=2026-09-27 is:public fork:false archived:false (200 of 4759 matches sampled)
- education: bounded or incomplete query: AI explainer is:public fork:false archived:false (200 of 28790 matches sampled)
- preservation: HTTP 403 from api.github.com/search/repositories; source not collected
- preservation: HTTP 403 from api.github.com/search/repositories; source not collected
- preservation: HTTP 403 from api.github.com/search/repositories; source not collected
- preservation: HTTP 403 from api.github.com/search/repositories; source not collected
- preservation: HTTP 403 from api.github.com/search/repositories; source not collected
- preservation: HTTP 403 from api.github.com/search/repositories; source not collected
- frontier: bounded or incomplete query: AI creative tools pushed:>=2026-09-27 is:public fork:false archived:false (200 of 272 matches sampled)
- frontier: bounded or incomplete query: AI creative tools created:>=2026-09-27 is:public fork:false archived:false (100 of 42 matches sampled)
- frontier: bounded or incomplete query: AI creative tools is:public fork:false archived:false (200 of 2042 matches sampled)
- frontier: bounded or incomplete query: AI digital art is:public fork:false archived:false (200 of 745 matches sampled)
- frontier: bounded or incomplete query: AI multimedia pushed:>=2026-09-27 is:public fork:false archived:false (39 of 118 matches sampled)
- frontier: bounded or incomplete query: AI multimedia is:public fork:false archived:false (200 of 1200 matches sampled)
- frontier: HTTP 403 from api.github.com/search/repositories; source not collected
- frontier: HTTP 403 from api.github.com/search/repositories; source not collected
- frontier: HTTP 403 from api.github.com/search/repositories; source not collected
- frontier: HTTP 403 from api.github.com/search/repositories; source not collected
- frontier: HTTP 403 from api.github.com/search/repositories; source not collected
- haptics: bounded or incomplete query: AI haptic created:>=2026-09-27 is:public fork:false archived:false (0 of 3 matches sampled)
- haptics: bounded or incomplete query: AI haptic is:public fork:false archived:false (200 of 64 matches sampled)
- neural-acoustics: bounded or incomplete query: neural acoustic is:public fork:false archived:false (165 of 165 matches sampled)
- neural-acoustics: bounded or incomplete query: audio visual acoustics created:>=2026-09-27 is:public fork:false archived:false (1 of 2 matches sampled)
- neural-acoustics: HTTP 403 from api.github.com/search/repositories; source not collected
- agent-media-production: HTTP 403 from api.github.com/search/repositories; source not collected
- agent-media-production: HTTP 403 from api.github.com/search/repositories; source not collected
- agent-media-production: HTTP 403 from api.github.com/search/repositories; source not collected
- agent-media-production: HTTP 403 from api.github.com/search/repositories; source not collected
- agent-media-production: HTTP 403 from api.github.com/search/repositories; source not collected
- agent-media-production: HTTP 403 from api.github.com/search/repositories; source not collected
- motion-typography: HTTP 403 from api.github.com/search/repositories; source not collected
- motion-typography: HTTP 403 from api.github.com/search/repositories; source not collected
- motion-typography: HTTP 403 from api.github.com/search/repositories; source not collected
- computational-craft: bounded or incomplete query: neural knitting created:>=2026-09-27 is:public fork:false archived:false (0 of 0 matches sampled)
- computational-craft: bounded or incomplete query: neural knitting is:public fork:false archived:false (2 of 3 matches sampled)
- music-notation: bounded or incomplete query: optical music recognition is:public fork:false archived:false (229 of 270 matches sampled)
- music-notation: HTTP 403 from api.github.com/search/repositories; source not collected
- music-notation: HTTP 403 from api.github.com/search/repositories; source not collected
- music-notation: HTTP 403 from api.github.com/search/repositories; source not collected
- relighting: HTTP 403 from api.github.com/search/repositories; source not collected
- architectural-media: bounded or incomplete query: AI architectural visualization pushed:>=2026-09-27 is:public fork:false archived:false (100 of 75 matches sampled)
- architectural-media: bounded or incomplete query: AI architectural visualization is:public fork:false archived:false (200 of 940 matches sampled)
- architectural-media: bounded or incomplete query: AI floor plan pushed:>=2026-09-27 is:public fork:false archived:false (9 of 56 matches sampled)
- architectural-media: HTTP 403 from api.github.com/search/repositories; source not collected
- light-field: HTTP 403 from api.github.com/search/repositories; source not collected
- light-field: HTTP 403 from api.github.com/search/repositories; source not collected
- light-field: HTTP 403 from api.github.com/search/repositories; source not collected
- light-field: HTTP 403 from api.github.com/search/repositories; source not collected
- light-field: HTTP 403 from api.github.com/search/repositories; source not collected
- light-field: bounded or incomplete query: AI hologram pushed:>=2026-09-27 is:public fork:false archived:false (34 of 34 matches sampled)
- light-field: bounded or incomplete query: AI hologram is:public fork:false archived:false (94 of 100 matches sampled)
- puppetry: bounded or incomplete query: AI puppet animation is:public fork:false archived:false (3 of 5 matches sampled)
- puppetry: HTTP 403 from api.github.com/search/repositories; source not collected
- puppetry: HTTP 403 from api.github.com/search/repositories; source not collected
- puppetry: HTTP 403 from api.github.com/search/repositories; source not collected
- ceramics: HTTP 403 from api.github.com/search/repositories; source not collected
- ceramics: HTTP 403 from api.github.com/search/repositories; source not collected
- ceramics: HTTP 403 from api.github.com/search/repositories; source not collected
- ceramics: HTTP 403 from api.github.com/search/repositories; source not collected
- ceramics: HTTP 403 from api.github.com/search/repositories; source not collected
- ceramics: HTTP 403 from api.github.com/search/repositories; source not collected
- parametric-design: HTTP 403 from api.github.com/search/repositories; source not collected
- parametric-design: HTTP 403 from api.github.com/search/repositories; source not collected
- parametric-design: HTTP 403 from api.github.com/search/repositories; source not collected
- parametric-design: HTTP 403 from api.github.com/search/repositories; source not collected
- parametric-design: HTTP 403 from api.github.com/search/repositories; source not collected
- parametric-design: HTTP 403 from api.github.com/search/repositories; source not collected
- cartography: HTTP 403 from api.github.com/search/repositories; source not collected
- cartography: HTTP 403 from api.github.com/search/repositories; source not collected
- cartography: bounded or incomplete query: diffusion map generation pushed:>=2026-09-27 is:public fork:false archived:false (2 of 2 matches sampled)
- robotic-art: bounded or incomplete query: AI robot painting is:public fork:false archived:false (6 of 6 matches sampled)
- robotic-art: bounded or incomplete query: neural robotic drawing is:public fork:false archived:false (0 of 1 matches sampled)
- cel-animation: bounded or incomplete query: AI cel animation pushed:>=2026-09-27 is:public fork:false archived:false (4 of 4 matches sampled)
- cel-animation: bounded or incomplete query: sketch inbetweening is:public fork:false archived:false (2 of 2 matches sampled)
- foley: HTTP 403 from api.github.com/search/repositories; source not collected
- foley: HTTP 403 from api.github.com/search/repositories; source not collected
- foley: HTTP 403 from api.github.com/search/repositories; source not collected
- foley: HTTP 403 from api.github.com/search/repositories; source not collected
- foley: HTTP 403 from api.github.com/search/repositories; source not collected
- foley: HTTP 403 from api.github.com/search/repositories; source not collected
- neural-media-codecs: HTTP 403 from api.github.com/search/repositories; source not collected
- neural-media-codecs: HTTP 403 from api.github.com/search/repositories; source not collected
- neural-media-codecs: HTTP 403 from api.github.com/search/repositories; source not collected
- neural-media-codecs: HTTP 403 from api.github.com/search/repositories; source not collected
- neural-media-codecs: HTTP 403 from api.github.com/search/repositories; source not collected
- neural-media-codecs: HTTP 403 from api.github.com/search/repositories; source not collected
- sonic-data-art: HTTP 403 from api.github.com/search/repositories; source not collected
- biosignal-art: bounded or incomplete query: EEG AI art created:>=2026-09-27 is:public fork:false archived:false (0 of 0 matches sampled)
- procedural-materials: bounded or incomplete query: neural material is:public fork:false archived:false (200 of 1398 matches sampled)
- procedural-materials: HTTP 403 from api.github.com/search/repositories; source not collected
- neural-camera: HTTP 403 from api.github.com/search/repositories; source not collected
- neural-camera: HTTP 403 from api.github.com/search/repositories; source not collected
- neural-camera: HTTP 403 from api.github.com/search/repositories; source not collected
- neural-camera: HTTP 403 from api.github.com/search/repositories; source not collected
- neural-camera: HTTP 403 from api.github.com/search/repositories; source not collected
- neural-camera: HTTP 403 from api.github.com/search/repositories; source not collected
- paper-engineering: bounded or incomplete query: neural kirigami created:>=2026-09-27 is:public fork:false archived:false (0 of 0 matches sampled)
- landscape-design: bounded or incomplete query: AI landscape design is:public fork:false archived:false (158 of 158 matches sampled)
- mosaic-art: HTTP 403 from api.github.com/search/repositories; source not collected
- mosaic-art: HTTP 403 from api.github.com/search/repositories; source not collected
- perceptual-art: HTTP 403 from api.github.com/search/repositories; source not collected
- perceptual-art: HTTP 403 from api.github.com/search/repositories; source not collected
- perceptual-art: HTTP 403 from api.github.com/search/repositories; source not collected
- perceptual-art: HTTP 403 from api.github.com/search/repositories; source not collected
- engraving: bounded or incomplete query: AI laser engraving pushed:>=2026-09-27 is:public fork:false archived:false (0 of 0 matches sampled)
- engraving: bounded or incomplete query: AI laser engraving is:public fork:false archived:false (2 of 2 matches sampled)
- brushstroke-art: bounded or incomplete query: neural painting is:public fork:false archived:false (200 of 287 matches sampled)
- color-direction: bounded or incomplete query: AI palette generation pushed:>=2026-09-27 is:public fork:false archived:false (2 of 3 matches sampled)
- color-direction: bounded or incomplete query: AI palette generation created:>=2026-09-27 is:public fork:false archived:false (3 of 3 matches sampled)
- color-direction: HTTP 403 from api.github.com/search/repositories; source not collected
- collage: HTTP 403 from api.github.com/search/repositories; source not collected
- collage: HTTP 403 from api.github.com/search/repositories; source not collected
- collage: HTTP 403 from api.github.com/search/repositories; source not collected
- collage: HTTP 403 from api.github.com/search/repositories; source not collected
- collage: bounded or incomplete query: AI collage composition created:>=2026-09-27 is:public fork:false archived:false (0 of 0 matches sampled)
- stereoscopic-media: bounded or incomplete query: 2D 3D depth conversion created:>=2026-09-27 is:public fork:false archived:false (1 of 1 matches sampled)
- stereoscopic-media: bounded or incomplete query: 2D 3D depth conversion is:public fork:false archived:false (2 of 8 matches sampled)
- signing-avatars: bounded or incomplete query: AI sign language avatar pushed:>=2026-09-27 is:public fork:false archived:false (0 of 7 matches sampled)
- signing-avatars: HTTP 403 from api.github.com/search/repositories; source not collected
- signing-avatars: HTTP 403 from api.github.com/search/repositories; source not collected
- signing-avatars: HTTP 403 from api.github.com/search/repositories; source not collected
- signing-avatars: HTTP 403 from api.github.com/search/repositories; source not collected
- signing-avatars: HTTP 403 from api.github.com/search/repositories; source not collected
- neural-dsp-authoring: HTTP 403 from api.github.com/search/repositories; source not collected
- neural-dsp-authoring: HTTP 403 from api.github.com/search/repositories; source not collected
- neural-dsp-authoring: HTTP 403 from api.github.com/search/repositories; source not collected
- neural-dsp-authoring: HTTP 403 from api.github.com/search/repositories; source not collected
- neural-dsp-authoring: HTTP 403 from api.github.com/search/repositories; source not collected
- neural-dsp-authoring: HTTP 403 from api.github.com/search/repositories; source not collected
- panoramic-worlds: HTTP 403 from api.github.com/search/repositories; source not collected
- panoramic-worlds: HTTP 403 from api.github.com/search/repositories; source not collected
- visual-dubbing: bounded or incomplete query: AI visual dubbing is:public fork:false archived:false (7 of 8 matches sampled)
- visual-dubbing: bounded or incomplete query: neural lip sync translation created:>=2026-09-27 is:public fork:false archived:false (0 of 0 matches sampled)
- neural-reshooting: HTTP 403 from api.github.com/search/repositories; source not collected
- neural-reshooting: HTTP 403 from api.github.com/search/repositories; source not collected
- neural-reshooting: HTTP 403 from api.github.com/search/repositories; source not collected
- render-denoising: HTTP 403 from api.github.com/search/repositories; source not collected
- render-denoising: HTTP 403 from api.github.com/search/repositories; source not collected
- render-denoising: HTTP 403 from api.github.com/search/repositories; source not collected
- render-denoising: HTTP 403 from api.github.com/search/repositories; source not collected
- render-denoising: HTTP 403 from api.github.com/search/repositories; source not collected
- render-denoising: HTTP 403 from api.github.com/search/repositories; source not collected
- media-quality-analysis: bounded or incomplete query: AI generative audio quality created:>=2026-09-27 is:public fork:false archived:false (1 of 1 matches sampled)
- media-quality-analysis: bounded or incomplete query: multimodal creative asset search created:>=2026-09-27 is:public fork:false archived:false (0 of 0 matches sampled)
- print-prepress: bounded or incomplete query: learned halftone printing is:public fork:false archived:false (0 of 0 matches sampled)
- fashion: HTTP 403 from api.github.com/search/repositories; source not collected
- capture: HTTP 403 from api.github.com/search/repositories; source not collected
- performance: HTTP 403 from api.github.com/search/repositories; source not collected
- fashion: HTTP 403 from api.github.com/search/repositories; source not collected
- preservation: HTTP 403 from api.github.com/search/repositories; source not collected
- fabrication: HTTP 403 from api.github.com/search/repositories; source not collected
- vector: HTTP 403 from api.github.com/search/repositories; source not collected
- audio: HTTP 403 from api.github.com/search/repositories; source not collected
- mobile: HTTP 403 from api.github.com/search/repositories; source not collected
- architectural-media: HTTP 403 from api.github.com/search/repositories; source not collected
- audio: HTTP 403 from api.github.com/search/repositories; source not collected
- education: HTTP 403 from api.github.com/search/repositories; source not collected
- images: bounded or incomplete query: topic:diffusion is:public fork:false archived:false (4 of 568 matches sampled)
- ceramics: bounded or incomplete query: PyPottery is:public fork:false archived:false (2 of 2 matches sampled)
- parametric-design: bounded or incomplete query: text-to-cad is:public fork:false archived:false (300 of 259 matches sampled)
- spatial: HTTP 403 from api.github.com/search/repositories; source not collected
- vector: HTTP 403 from api.github.com/search/repositories; source not collected
- preservation: HTTP 403 from api.github.com/search/repositories; source not collected
- cartography: HTTP 403 from api.github.com/search/repositories; source not collected
- robotic-art: HTTP 403 from api.github.com/search/repositories; source not collected
- computational-craft: HTTP 403 from api.github.com/search/repositories; source not collected
- images: bounded or incomplete query: AI painting editor local created:>=2026-09-27 is:public fork:false archived:false (0 of 0 matches sampled)
- xr: bounded or incomplete query: AI WebXR spatial creation is:public fork:false archived:false (0 of 0 matches sampled)
- cel-animation: bounded or incomplete query: animation colorization is:public fork:false archived:false (500 of 2499 matches sampled)
- storytelling: HTTP 403 from api.github.com/search/repositories; source not collected
- cel-animation: HTTP 403 from api.github.com/search/repositories; source not collected
- sonic-data-art: bounded or incomplete query: AI corpus sound design is:public fork:false archived:false (0 of 0 matches sampled)
- procedural-materials: bounded or incomplete query: neural procedural material is:public fork:false archived:false (0 of 0 matches sampled)
- collage: bounded or incomplete query: collage reinforcement learning is:public fork:false archived:false (0 of 0 matches sampled)
- photography: bounded or incomplete query: AI photograph culling local created:>=2026-09-27 is:public fork:false archived:false (0 of 0 matches sampled)
- typography: HTTP 403 from api.github.com/search/repositories; source not collected
- signing-avatars: HTTP 403 from api.github.com/search/repositories; source not collected
- light-field: bounded or incomplete query: learned light field editing is:public fork:false archived:false (0 of 0 matches sampled)
- neural-dsp-authoring: bounded or incomplete query: AI agent Rust DSP is:public fork:false archived:false (0 of 8 matches sampled)
- stereoscopic-media: bounded or incomplete query: neural stereo video conversion WebGPU is:public fork:false archived:false (0 of 0 matches sampled)
- panoramic-worlds: bounded or incomplete query: panorama world generation is:public fork:false archived:false (0 of 1 matches sampled)
- procedural-materials: HTTP 403 from api.github.com/search/repositories; source not collected
- xr: HTTP 403 from api.github.com/search/repositories; source not collected
- audio: HTTP 403 from api.github.com/search/repositories; source not collected
- images: HTTP 403 from api.github.com/search/repositories; source not collected
- puppetry: HTTP 403 from api.github.com/search/repositories; source not collected
- neural-clothing: HTTP 403 from api.github.com/search/repositories; source not collected
- visual-dubbing: HTTP 403 from api.github.com/search/repositories; source not collected
- light-field: HTTP 403 from api.github.com/search/repositories; source not collected
- neural-reshooting: HTTP 403 from api.github.com/search/repositories; source not collected
- audio: bounded or incomplete query: Audio Studio MCP is:public fork:false archived:false (69 of 69 matches sampled)
- media-quality-analysis: bounded or incomplete query: Sonicproof is:public fork:false archived:false (0 of 1 matches sampled)
- video: bounded or incomplete query: AI creative editor created:>=2026-10-20 is:public fork:false archived:false (0 of 0 matches sampled)
- images: bounded or incomplete query: AI image tool created:>=2026-10-20 is:public fork:false archived:false (12 of 91 matches sampled)
- Watchlist wdfewwdev-web/tileweaver: HTTP 404 from api.github.com/repos/wdfewwdev-web/tileweaver; source not collected
- Watchlist gtwatts/ferrocut: HTTP 404 from api.github.com/repos/gtwatts/ferrocut; source not collected
- Watchlist justynberk/reel-kit: HTTP 404 from api.github.com/repos/justynberk/reel-kit; source not collected
- Watchlist ludovic111/kimchi: HTTP 404 from api.github.com/repos/ludovic111/kimchi; source not collected
- Watchlist lukemun/dreamcut: HTTP 404 from api.github.com/repos/lukemun/dreamcut; source not collected
- Watchlist voughtboysjj-rgb/ai-subtitle-generator: HTTP 404 from api.github.com/repos/voughtboysjj-rgb/ai-subtitle-generator; source not collected
- Watchlist bigeye0x0/bigeye-sticker-video: HTTP 404 from api.github.com/repos/bigeye0x0/bigeye-sticker-video; source not collected
- Watchlist kwebby/cutscript: HTTP 404 from api.github.com/repos/kwebby/cutscript; source not collected
- Watchlist amitbaz/music-production-ai-mentor: HTTP 404 from api.github.com/repos/amitbaz/music-production-ai-mentor; source not collected
- Watchlist barnine/barnine: HTTP 404 from api.github.com/repos/barnine/barnine; source not collected
- Watchlist licincan/blender-ai-mcp-addon: HTTP 404 from api.github.com/repos/licincan/blender-ai-mcp-addon; source not collected
- Watchlist wdfewwdev-web/tileweaver: HTTP 404 from api.github.com/repos/wdfewwdev-web/tileweaver; source not collected (earlier attempt in this observation)
- Watchlist licincan/blender-ai-mcp-addon: HTTP 404 from api.github.com/repos/licincan/blender-ai-mcp-addon; source not collected (earlier attempt in this observation)
- Watchlist lukemun/dreamcut: HTTP 404 from api.github.com/repos/lukemun/dreamcut; source not collected (earlier attempt in this observation)
- Watchlist ludovic111/kimchi: HTTP 404 from api.github.com/repos/ludovic111/kimchi; source not collected (earlier attempt in this observation)
- Watchlist gtwatts/ferrocut: HTTP 404 from api.github.com/repos/gtwatts/ferrocut; source not collected (earlier attempt in this observation)
- Watchlist justynberk/reel-kit: HTTP 404 from api.github.com/repos/justynberk/reel-kit; source not collected (earlier attempt in this observation)
- Watchlist ludovic111/kimchi: HTTP 404 from api.github.com/repos/ludovic111/kimchi; source not collected (earlier attempt in this observation)
- Watchlist wdfewwdev-web/tileweaver: HTTP 404 from api.github.com/repos/wdfewwdev-web/tileweaver; source not collected (earlier attempt in this observation)
- Watchlist lukemun/dreamcut: HTTP 404 from api.github.com/repos/lukemun/dreamcut; source not collected (earlier attempt in this observation)
- Watchlist barnine/barnine: HTTP 404 from api.github.com/repos/barnine/barnine; source not collected (earlier attempt in this observation)
- Watchlist kwebby/cutscript: HTTP 404 from api.github.com/repos/kwebby/cutscript; source not collected (earlier attempt in this observation)
- Watchlist amitbaz/music-production-ai-mentor: HTTP 404 from api.github.com/repos/amitbaz/music-production-ai-mentor; source not collected (earlier attempt in this observation)
- Watchlist voughtboysjj-rgb/ai-subtitle-generator: HTTP 404 from api.github.com/repos/voughtboysjj-rgb/ai-subtitle-generator; source not collected (earlier attempt in this observation)
- Watchlist amitbaz/music-production-ai-mentor: HTTP 404 from api.github.com/repos/amitbaz/music-production-ai-mentor; source not collected (earlier attempt in this observation)
- Watchlist barnine/barnine: HTTP 404 from api.github.com/repos/barnine/barnine; source not collected (earlier attempt in this observation)
- Watchlist gtwatts/ferrocut: HTTP 404 from api.github.com/repos/gtwatts/ferrocut; source not collected (earlier attempt in this observation)
- Watchlist ludovic111/kimchi: HTTP 404 from api.github.com/repos/ludovic111/kimchi; source not collected (earlier attempt in this observation)
- Watchlist licincan/blender-ai-mcp-addon: HTTP 404 from api.github.com/repos/licincan/blender-ai-mcp-addon; source not collected (earlier attempt in this observation)
- Watchlist bigeye0x0/bigeye-sticker-video: HTTP 404 from api.github.com/repos/bigeye0x0/bigeye-sticker-video; source not collected (earlier attempt in this observation)
- Watchlist justynberk/reel-kit: HTTP 404 from api.github.com/repos/justynberk/reel-kit; source not collected (earlier attempt in this observation)
- Watchlist ludovic111/kimchi: HTTP 404 from api.github.com/repos/ludovic111/kimchi; source not collected (earlier attempt in this observation)
- Watchlist bigeye0x0/bigeye-sticker-video: HTTP 404 from api.github.com/repos/bigeye0x0/bigeye-sticker-video; source not collected (earlier attempt in this observation)
- Evidence hamzaskhan/Room-Tile-Visualizer: HTTP 409 from api.github.com/repos/hamzaskhan/Room-Tile-Visualizer/commits; source not collected

## Sonicproof

Audio, music & voice · AI assisted media quality and take selection · AI Foley and sound effects

A recently created project receiving its first full library guide; its creation is not proof of production readiness.

### Quality assessment: Quality unverified

Software licensing and a concrete creative AI use are supported. The remaining checks do not establish a recommendation.

Scope: Choosing sound-design takes, finding effects by description and catching technical problems before auditioning a larger batch.

Evidence checked: 2026-10-27. No local execution implied.

- **Open-source software license · verified:** The complete root software license was read and archived. The grant covers this project code; unresolved model, service and asset terms are disclosed separately. [Source](https://github.com/kanaworksai-hue/sonicproof/blob/main/LICENSE)
- **Creative results · documented:** The README shows the local browser workbench and CLI examples for prompt matching, ranking, QC and picture fit. These are maintainer examples; listening quality has not been independently established. [Source](https://github.com/kanaworksai-hue/sonicproof/blob/main/README.md) [Source](https://huggingface.co/google/embeddinggemma-2) [Source](https://pypi.org/project/sonicproof/)
- **Reproducible setup · documented:** Install the model extra with uv, load the model using doctor, and start the local workbench on port 7788. On Windows, install a matching CUDA torch and torchvision pair first if GPU acceleration is wanted; the default PyPI torch can be CPU-only. Independent reproduction has not been established in this review. [Source](https://github.com/kanaworksai-hue/sonicproof/blob/main/README.md) [Source](https://huggingface.co/google/embeddinggemma-2) [Source](https://pypi.org/project/sonicproof/)
- **Maintenance and support · documented:** Live review archived 10 recent commits, 3 published release records and 8 recent support/PR records. Latest sampled commit: 2026-10-19. The bounded support sample did not establish third-party resolution history. This is documented activity, not proof of sustained support or a complete blocker survey. [Source](https://github.com/kanaworksai-hue/sonicproof/commits/main) [Source](https://github.com/kanaworksai-hue/sonicproof/issues)
- **Independent use · unknown:** Reviewed official examples, the current support sample and bounded live web findings. Independent first-hand reproduction of this exact creative workflow was not established; author demonstrations are not treated as independent evidence.
- **Models, services and costs · documented:** EmbeddingGemma 2 is downloaded separately; the current Google model card declares Apache-2.0. Its model documentation and any applicable usage policy should be checked separately. Project branding and the Kana character are excluded from the software grant. Local compute; no inference API key required. An optional agent client can have separate charges. [Source](https://github.com/kanaworksai-hue/sonicproof/blob/main/README.md) [Source](https://huggingface.co/google/embeddinggemma-2) [Source](https://pypi.org/project/sonicproof/)

Documentation review only; AI Media Scout did not install or run this software. Short transients, long musical mixtures and difficult prompts can mislead embedding scores. Picture fit samples frames rather than understanding every moment. No independent reproduction was established.

### How it uses AI

An audio workbench that uses multimodal EmbeddingGemma 2 embeddings to compare generated sounds with prompts, rank takes and search a local sound library. Technical loudness, clipping and loop checks complement the AI scores. [Source](https://github.com/kanaworksai-hue/sonicproof/blob/main/README.md) [Source](https://huggingface.co/google/embeddinggemma-2) [Source](https://pypi.org/project/sonicproof/)

### Introduction

An audio workbench that uses multimodal EmbeddingGemma 2 embeddings to compare generated sounds with prompts, rank takes and search a local sound library. Technical loudness, clipping and loop checks complement the AI scores. [Source 1](https://github.com/kanaworksai-hue/sonicproof/blob/main/README.md) [Source 2](https://huggingface.co/google/embeddinggemma-2) [Source 3](https://pypi.org/project/sonicproof/)

### What it is good for

Choosing sound-design takes, finding effects by description and catching technical problems before auditioning a larger batch. [Source 1](https://github.com/kanaworksai-hue/sonicproof/blob/main/README.md) [Source 2](https://huggingface.co/google/embeddinggemma-2) [Source 3](https://pypi.org/project/sonicproof/)

### Demo & examples

The README shows the local browser workbench and CLI examples for prompt matching, ranking, QC and picture fit. These are maintainer examples; listening quality has not been independently established. [Source 1](https://github.com/kanaworksai-hue/sonicproof/blob/main/README.md) [Source 2](https://huggingface.co/google/embeddinggemma-2) [Source 3](https://pypi.org/project/sonicproof/)

### Install

Install the model extra with uv, load the model using doctor, and start the local workbench on port 7788. On Windows, install a matching CUDA torch and torchvision pair first if GPU acceleration is wanted; the default PyPI torch can be CPU-only. [Source 1](https://github.com/kanaworksai-hue/sonicproof/blob/main/README.md) [Source 2](https://huggingface.co/google/embeddinggemma-2) [Source 3](https://pypi.org/project/sonicproof/)

1. Obtain the official source or release linked below.
2. Install the model extra with uv, load the model using doctor, and start the local workbench on port 7788. On Windows, install a matching CUDA torch and torchvision pair first if GPU acceleration is wanted; the default PyPI torch can be CPU-only.

```sh
uv tool install "sonicproof[model]"
```


```sh
sonicproof doctor --load
```


```sh
sonicproof serve
```

### First project

Start with a short, representative project and inspect the result before a larger batch. [Source 1](https://github.com/kanaworksai-hue/sonicproof/blob/main/README.md) [Source 2](https://huggingface.co/google/embeddinggemma-2) [Source 3](https://pypi.org/project/sonicproof/)

1. Load a short sound and describe the intended effect.
2. Compare several takes with the same prompt, then inspect clipping, loudness and loop diagnostics.
3. Listen to the shortlisted takes; semantic similarity is a triage aid, not an artistic verdict.
### Hardware & software

Requirements below are documented for this workflow. Unspecified limits are not inferred. [Source 1](https://github.com/kanaworksai-hue/sonicproof/blob/main/README.md) [Source 2](https://huggingface.co/google/embeddinggemma-2) [Source 3](https://pypi.org/project/sonicproof/)

- **Hardware:** About 1.5 GB of model download is documented. Minimum RAM and VRAM are not documented.
- **Software:** Python 3.11+; CI versions documented as 3.11–3.13. ffmpeg is needed for AAC/M4A/MP4 and video input, not ordinary WAV/FLAC/OGG/MP3.
- **Platforms:** macOS MPS, Linux/Windows CUDA, and CPU execution are documented.

### License, model weights & costs

The full software license was reviewed. Model weights, assets and services remain separate. [Source 1](https://github.com/kanaworksai-hue/sonicproof/blob/main/LICENSE) [Source 2](https://github.com/kanaworksai-hue/sonicproof/blob/main/README.md) [Source 3](https://huggingface.co/google/embeddinggemma-2) [Source 4](https://pypi.org/project/sonicproof/)

- **Code:** MIT
- **Weights:** EmbeddingGemma 2 is downloaded separately; the current Google model card declares Apache-2.0. Its model documentation and any applicable usage policy should be checked separately. Project branding and the Kana character are excluded from the software grant.
- **Commercial:** Software use follows MIT. EmbeddingGemma 2 is downloaded separately; the current Google model card declares Apache-2.0. Its model documentation and any applicable usage policy should be checked separately. Project branding and the Kana character are excluded from the software grant.
- **Cost:** Local compute; no inference API key required. An optional agent client can have separate charges.

### Why it merits attention

Included for the documented creative workflow. A complete guide and popularity do not establish output reliability. [Source 1](https://github.com/kanaworksai-hue/sonicproof/blob/main/README.md) [Source 2](https://huggingface.co/google/embeddinggemma-2) [Source 3](https://pypi.org/project/sonicproof/)

### Limitations

Short transients, long musical mixtures and difficult prompts can mislead embedding scores. Picture fit samples frames rather than understanding every moment. No independent reproduction was established. [Source 1](https://github.com/kanaworksai-hue/sonicproof/blob/main/README.md) [Source 2](https://huggingface.co/google/embeddinggemma-2) [Source 3](https://pypi.org/project/sonicproof/)

### Get the tool

- [Repository](https://github.com/kanaworksai-hue/sonicproof)
- [Documentation](https://github.com/kanaworksai-hue/sonicproof/blob/main/README.md)

## Hush

Neural denoising for real-time creative rendering · Browser tools & web media · 3D, reconstruction & assets · VFX, compositing & relighting

A recently created project receiving its first full library guide; its creation is not proof of production readiness.

### Quality assessment: Experimental

Software licensing and a concrete creative AI use are supported. The remaining checks do not establish a recommendation.

Scope: Experiments with responsive, low-sample interactive 3D rendering in a browser.

Evidence checked: 2026-10-27. No local execution implied.

Why Experimental: The current README explicitly identifies a research prototype, with a neural filter trained on only three example scenes and unfinished generalization/training support. https://github.com/kanaworksai-hue/hush/blob/main/README.md https://hush.tokyoaivisuals.club

- **Open-source software license · verified:** The complete root software license was read and archived. The grant covers this project code; unresolved model, service and asset terms are disclosed separately. [Source](https://github.com/kanaworksai-hue/hush/blob/main/LICENSE)
- **Creative results · documented:** The official Hush site and README provide comparative noisy/SVGF/Hush render views. The cited timings are author measurements, not universal performance guarantees. [Source](https://github.com/kanaworksai-hue/hush/blob/main/README.md) [Source](https://hush.tokyoaivisuals.club)
- **Reproducible setup · documented:** For the demo, clone the repository, install its npm dependencies, fetch the documented scene assets and start Vite. The library can also be installed directly from its GitHub repository; the unrelated npm package named hush is not this project. Independent reproduction has not been established in this review. [Source](https://github.com/kanaworksai-hue/hush/blob/main/README.md) [Source](https://hush.tokyoaivisuals.club)
- **Maintenance and support · documented:** Live review archived 3 recent commits, 0 published release records and 0 recent support/PR records. Latest sampled commit: 2026-10-20. The bounded support sample did not establish third-party resolution history. This is documented activity, not proof of sustained support or a complete blocker survey. [Source](https://github.com/kanaworksai-hue/hush/commits/main) [Source](https://github.com/kanaworksai-hue/hush/issues)
- **Independent use · unknown:** Reviewed official examples, the current support sample and bounded live web findings. Independent first-hand reproduction of this exact creative workflow was not established; author demonstrations are not treated as independent evidence.
- **Models, services and costs · documented:** The repository includes its small trained parameter network. Demo assets retain separate terms; the README identifies CC0 assets and third-party credits. Brand assets are excluded from MIT. Local compute plus any chosen external model or service; provider access and charges are separate. [Source](https://github.com/kanaworksai-hue/hush/blob/main/README.md) [Source](https://hush.tokyoaivisuals.club)

Documentation review only; AI Media Scout did not install or run this software. The README explicitly calls the current work a research prototype. The weights were trained on only three example scenes; training code is not released. Broad walls, glass and some object-ID cases are known limitations.

### How it uses AI

A WebGPU path-tracing denoiser whose small neural network predicts filter parameters, combined with temporal accumulation and spatial filtering. [Source](https://github.com/kanaworksai-hue/hush/blob/main/README.md) [Source](https://hush.tokyoaivisuals.club)

### Introduction

A WebGPU path-tracing denoiser whose small neural network predicts filter parameters, combined with temporal accumulation and spatial filtering. [Source 1](https://github.com/kanaworksai-hue/hush/blob/main/README.md) [Source 2](https://hush.tokyoaivisuals.club)

### What it is good for

Experiments with responsive, low-sample interactive 3D rendering in a browser. [Source 1](https://github.com/kanaworksai-hue/hush/blob/main/README.md) [Source 2](https://hush.tokyoaivisuals.club)

### Demo & examples

The official Hush site and README provide comparative noisy/SVGF/Hush render views. The cited timings are author measurements, not universal performance guarantees. [Source 1](https://github.com/kanaworksai-hue/hush/blob/main/README.md) [Source 2](https://hush.tokyoaivisuals.club)

### Install

For the demo, clone the repository, install its npm dependencies, fetch the documented scene assets and start Vite. The library can also be installed directly from its GitHub repository; the unrelated npm package named hush is not this project. [Source 1](https://github.com/kanaworksai-hue/hush/blob/main/README.md) [Source 2](https://hush.tokyoaivisuals.club)

1. Obtain the official source or release linked below.
2. For the demo, clone the repository, install its npm dependencies, fetch the documented scene assets and start Vite. The library can also be installed directly from its GitHub repository; the unrelated npm package named hush is not this project.

```sh
git clone https://github.com/kanaworksai-hue/hush.git
```


```sh
cd hush
```


```sh
npm install
```


```sh
python tools/fetch_assets.py
```


```sh
npm run dev
```

### First project

Start with a short, representative project and inspect the result before a larger batch. [Source 1](https://github.com/kanaworksai-hue/hush/blob/main/README.md) [Source 2](https://hush.tokyoaivisuals.club)

1. Open the demo in a WebGPU-capable browser.
2. Compare the same scene at the same sample count with denoising disabled and enabled.
3. Inspect motion, thin edges, glass and flat walls before adopting the filter.
### Hardware & software

Requirements below are documented for this workflow. Unspecified limits are not inferred. [Source 1](https://github.com/kanaworksai-hue/hush/blob/main/README.md) [Source 2](https://hush.tokyoaivisuals.club)

- **Hardware:** A WebGPU device meeting Hush.requiredLimits is required. Minimum system RAM/VRAM are not stated; an RTX 3060 timing is a benchmark rather than a minimum.
- **Software:** Node 20.19+, Python 3 for asset retrieval; Chrome/Edge 113+ or Safari 26+ documented. WebGPU and a secure browser context are required.
- **Platforms:** Browser WebGPU is required; a complete OS/device support matrix is not documented.

### License, model weights & costs

The full software license was reviewed. Model weights, assets and services remain separate. [Source 1](https://github.com/kanaworksai-hue/hush/blob/main/LICENSE) [Source 2](https://github.com/kanaworksai-hue/hush/blob/main/README.md) [Source 3](https://hush.tokyoaivisuals.club)

- **Code:** MIT
- **Weights:** The repository includes its small trained parameter network. Demo assets retain separate terms; the README identifies CC0 assets and third-party credits. Brand assets are excluded from MIT.
- **Commercial:** Software use follows MIT. The repository includes its small trained parameter network. Demo assets retain separate terms; the README identifies CC0 assets and third-party credits. Brand assets are excluded from MIT.
- **Cost:** Local compute plus any chosen external model or service; provider access and charges are separate.

### Why it merits attention

Included for the documented creative workflow. A complete guide and popularity do not establish output reliability. [Source 1](https://github.com/kanaworksai-hue/hush/blob/main/README.md) [Source 2](https://hush.tokyoaivisuals.club)

### Limitations

The README explicitly calls the current work a research prototype. The weights were trained on only three example scenes; training code is not released. Broad walls, glass and some object-ID cases are known limitations. [Source 1](https://github.com/kanaworksai-hue/hush/blob/main/README.md) [Source 2](https://hush.tokyoaivisuals.club)

### Get the tool

- [Repository](https://github.com/kanaworksai-hue/hush)
- [Documentation](https://github.com/kanaworksai-hue/hush/blob/main/README.md)

## Mitsuke

Images & design · Video, animation & film · AI assisted media quality and take selection · Photography, restoration & color

A recently created project receiving its first full library guide; its creation is not proof of production readiness.

### Quality assessment: Quality unverified

Software licensing and a concrete creative AI use are supported. The remaining checks do not establish a recommendation.

Scope: Finding visual references in personal image collections and locating visually similar shots without uploading the collection.

Evidence checked: 2026-10-27. No local execution implied.

- **Open-source software license · verified:** The complete root software license was read and archived. The grant covers this project code; unresolved model, service and asset terms are disclosed separately. [Source](https://github.com/kanaworksai-hue/mitsuke/blob/main/LICENSE)
- **Creative results · documented:** The README illustrates the local search gallery, image queries and collections. These are published maintainer examples, not an independent search-quality benchmark. [Source](https://github.com/kanaworksai-hue/mitsuke/blob/main/README.md) [Source](https://huggingface.co/google/embeddinggemma-2)
- **Reproducible setup · documented:** Install using uv on Apple silicon, download the model with doctor and open the local server on port 8737. Independent reproduction has not been established in this review. [Source](https://github.com/kanaworksai-hue/mitsuke/blob/main/README.md) [Source](https://huggingface.co/google/embeddinggemma-2)
- **Maintenance and support · documented:** Live review archived 10 recent commits, 1 published release records and 0 recent support/PR records. Latest sampled commit: 2026-10-22. The bounded support sample did not establish third-party resolution history. This is documented activity, not proof of sustained support or a complete blocker survey. [Source](https://github.com/kanaworksai-hue/mitsuke/commits/main) [Source](https://github.com/kanaworksai-hue/mitsuke/issues)
- **Independent use · unknown:** Reviewed official examples, the current support sample and bounded live web findings. Independent first-hand reproduction of this exact creative workflow was not established; author demonstrations are not treated as independent evidence.
- **Models, services and costs · documented:** The separately downloaded EmbeddingGemma 2 model is declared Apache-2.0; the MLX conversion retains separate upstream terms. Branding is excluded from the MIT code license. Local computation and storage; no hosted inference API required. [Source](https://github.com/kanaworksai-hue/mitsuke/blob/main/README.md) [Source](https://huggingface.co/google/embeddinggemma-2)

Documentation review only; AI Media Scout did not install or run this software. Video search indexes visual shots, not audio or dialogue. Some color filtering and mood-board export features are roadmap items. Search relevance has not been independently reproduced.

### How it uses AI

Local semantic search for images and video shots using an MLX conversion of EmbeddingGemma 2; queries can combine words, a reference image and mood-board context. [Source](https://github.com/kanaworksai-hue/mitsuke/blob/main/README.md) [Source](https://huggingface.co/google/embeddinggemma-2)

### Introduction

Local semantic search for images and video shots using an MLX conversion of EmbeddingGemma 2; queries can combine words, a reference image and mood-board context. [Source 1](https://github.com/kanaworksai-hue/mitsuke/blob/main/README.md) [Source 2](https://huggingface.co/google/embeddinggemma-2)

### What it is good for

Finding visual references in personal image collections and locating visually similar shots without uploading the collection. [Source 1](https://github.com/kanaworksai-hue/mitsuke/blob/main/README.md) [Source 2](https://huggingface.co/google/embeddinggemma-2)

### Demo & examples

The README illustrates the local search gallery, image queries and collections. These are published maintainer examples, not an independent search-quality benchmark. [Source 1](https://github.com/kanaworksai-hue/mitsuke/blob/main/README.md) [Source 2](https://huggingface.co/google/embeddinggemma-2)

### Install

Install using uv on Apple silicon, download the model with doctor and open the local server on port 8737. [Source 1](https://github.com/kanaworksai-hue/mitsuke/blob/main/README.md) [Source 2](https://huggingface.co/google/embeddinggemma-2)

1. Obtain the official source or release linked below.
2. Install using uv on Apple silicon, download the model with doctor and open the local server on port 8737.

```sh
uv tool install "mitsuke @ git+https://github.com/kanaworksai-hue/mitsuke"
```


```sh
mitsuke doctor --download
```


```sh
mitsuke serve --open
```

### First project

Start with a short, representative project and inspect the result before a larger batch. [Source 1](https://github.com/kanaworksai-hue/mitsuke/blob/main/README.md) [Source 2](https://huggingface.co/google/embeddinggemma-2)

1. Add a folder of references and allow indexing to finish.
2. Search with a visual description or an example image.
3. Review the returned images or video shots and save useful references into a collection.
### Hardware & software

Requirements below are documented for this workflow. Unspecified limits are not inferred. [Source 1](https://github.com/kanaworksai-hue/mitsuke/blob/main/README.md) [Source 2](https://huggingface.co/google/embeddinggemma-2)

- **Hardware:** Approximately 4 GB free disk space, including about 1.5 GB for the model; minimum RAM is not specified.
- **Software:** Python 3.12+, uv and MLX; optional MCP integration is available.
- **Platforms:** Apple silicon Mac M1 or later. Intel Mac, Windows and Linux are not supported by this MLX application.

### License, model weights & costs

The full software license was reviewed. Model weights, assets and services remain separate. [Source 1](https://github.com/kanaworksai-hue/mitsuke/blob/main/LICENSE) [Source 2](https://github.com/kanaworksai-hue/mitsuke/blob/main/README.md) [Source 3](https://huggingface.co/google/embeddinggemma-2)

- **Code:** MIT
- **Weights:** The separately downloaded EmbeddingGemma 2 model is declared Apache-2.0; the MLX conversion retains separate upstream terms. Branding is excluded from the MIT code license.
- **Commercial:** Software use follows MIT. The separately downloaded EmbeddingGemma 2 model is declared Apache-2.0; the MLX conversion retains separate upstream terms. Branding is excluded from the MIT code license.
- **Cost:** Local computation and storage; no hosted inference API required.

### Why it merits attention

Included for the documented creative workflow. A complete guide and popularity do not establish output reliability. [Source 1](https://github.com/kanaworksai-hue/mitsuke/blob/main/README.md) [Source 2](https://huggingface.co/google/embeddinggemma-2)

### Limitations

Video search indexes visual shots, not audio or dialogue. Some color filtering and mood-board export features are roadmap items. Search relevance has not been independently reproduced. [Source 1](https://github.com/kanaworksai-hue/mitsuke/blob/main/README.md) [Source 2](https://huggingface.co/google/embeddinggemma-2)

### Get the tool

- [Repository](https://github.com/kanaworksai-hue/mitsuke)
- [Documentation](https://github.com/kanaworksai-hue/mitsuke/blob/main/README.md)

## Tsuzuri

Audio, music & voice · Accessible media & assistive creation · Storyboarding, narrative & comics

A recently created project receiving its first full library guide; its creation is not proof of production readiness.

### Quality assessment: Quality unverified

Software licensing and a concrete creative AI use are supported. The remaining checks do not establish a recommendation.

Scope: Dictating scripts, captions, notes and creative briefs directly into a text field.

Evidence checked: 2026-10-27. No local execution implied.

- **Open-source software license · verified:** The complete root software license was read and archived. The grant covers this project code; unresolved model, service and asset terms are disclosed separately. [Source](https://github.com/kanaworksai-hue/tsuzuri/blob/main/LICENSE)
- **Creative results · documented:** The README shows the menu-bar workflow and language support. Speech accuracy claims remain maintainer documentation; mixed-language performance is explicitly limited. [Source](https://github.com/kanaworksai-hue/tsuzuri/blob/main/README.md) [Source](https://github.com/kanaworksai-hue/tsuzuri/releases)
- **Reproducible setup · documented:** Download the DMG from the official releases, drag the app into Applications, grant microphone/accessibility permissions and let it fetch its models. A source build requires Xcode 26+, Swift 6.3+ and the Metal toolchain. Independent reproduction has not been established in this review. [Source](https://github.com/kanaworksai-hue/tsuzuri/blob/main/README.md) [Source](https://github.com/kanaworksai-hue/tsuzuri/releases)
- **Maintenance and support · documented:** Live review archived 10 recent commits, 3 published release records and 0 recent support/PR records. Latest sampled commit: 2026-10-22. The bounded support sample did not establish third-party resolution history. This is documented activity, not proof of sustained support or a complete blocker survey. [Source](https://github.com/kanaworksai-hue/tsuzuri/commits/main) [Source](https://github.com/kanaworksai-hue/tsuzuri/issues)
- **Independent use · unknown:** Reviewed official examples, the current support sample and bounded live web findings. Independent first-hand reproduction of this exact creative workflow was not established; author demonstrations are not treated as independent evidence.
- **Models, services and costs · documented:** Qwen3-ASR, the optional cleanup model and Silero VAD are separate components with their own notices; the README identifies Apache-2.0 and MIT terms. Branding is excluded from the code grant. Runs locally after downloads; no cloud transcription account required. [Source](https://github.com/kanaworksai-hue/tsuzuri/blob/main/README.md) [Source](https://github.com/kanaworksai-hue/tsuzuri/releases)

Documentation review only; AI Media Scout did not install or run this software. Short mixed Japanese/Chinese speech and sound-alike words can be mistranscribed. Cleanup language coverage is narrower than recognition. The paste shortcut assumes the documented keyboard behavior.

### How it uses AI

An offline macOS dictation app using Qwen3-ASR through MLX, with optional local text cleanup for punctuation and short spoken drafts. [Source](https://github.com/kanaworksai-hue/tsuzuri/blob/main/README.md) [Source](https://github.com/kanaworksai-hue/tsuzuri/releases)

### Introduction

An offline macOS dictation app using Qwen3-ASR through MLX, with optional local text cleanup for punctuation and short spoken drafts. [Source 1](https://github.com/kanaworksai-hue/tsuzuri/blob/main/README.md) [Source 2](https://github.com/kanaworksai-hue/tsuzuri/releases)

### What it is good for

Dictating scripts, captions, notes and creative briefs directly into a text field. [Source 1](https://github.com/kanaworksai-hue/tsuzuri/blob/main/README.md) [Source 2](https://github.com/kanaworksai-hue/tsuzuri/releases)

### Demo & examples

The README shows the menu-bar workflow and language support. Speech accuracy claims remain maintainer documentation; mixed-language performance is explicitly limited. [Source 1](https://github.com/kanaworksai-hue/tsuzuri/blob/main/README.md) [Source 2](https://github.com/kanaworksai-hue/tsuzuri/releases)

### Install

Download the DMG from the official releases, drag the app into Applications, grant microphone/accessibility permissions and let it fetch its models. A source build requires Xcode 26+, Swift 6.3+ and the Metal toolchain. [Source 1](https://github.com/kanaworksai-hue/tsuzuri/blob/main/README.md) [Source 2](https://github.com/kanaworksai-hue/tsuzuri/releases)

1. Obtain the official source or release linked below.
2. Download the DMG from the official releases, drag the app into Applications, grant microphone/accessibility permissions and let it fetch its models. A source build requires Xcode 26+, Swift 6.3+ and the Metal toolchain.
### First project

Start with a short, representative project and inspect the result before a larger batch. [Source 1](https://github.com/kanaworksai-hue/tsuzuri/blob/main/README.md) [Source 2](https://github.com/kanaworksai-hue/tsuzuri/releases)

1. Select a supported recognition language and a destination text field.
2. Hold the right Option key, speak, then release to transcribe and paste.
3. Proofread names and mixed-language phrases; enable the optional cleanup model only when useful.
### Hardware & software

Requirements below are documented for this workflow. Unspecified limits are not inferred. [Source 1](https://github.com/kanaworksai-hue/tsuzuri/blob/main/README.md) [Source 2](https://github.com/kanaworksai-hue/tsuzuri/releases)

- **Hardware:** About 2 GB free memory while active; default ASR download about 1.6 GB. Optional cleanup adds about 1.19 GB disk and 0.35 GB memory.
- **Software:** macOS 14+; source build requires Xcode 26+ and Swift 6.3+. Microphone and accessibility access are documented.
- **Platforms:** Apple silicon M1 or newer; Windows, Linux and Intel Mac support is not documented.

### License, model weights & costs

The full software license was reviewed. Model weights, assets and services remain separate. [Source 1](https://github.com/kanaworksai-hue/tsuzuri/blob/main/LICENSE) [Source 2](https://github.com/kanaworksai-hue/tsuzuri/blob/main/README.md) [Source 3](https://github.com/kanaworksai-hue/tsuzuri/releases)

- **Code:** MIT
- **Weights:** Qwen3-ASR, the optional cleanup model and Silero VAD are separate components with their own notices; the README identifies Apache-2.0 and MIT terms. Branding is excluded from the code grant.
- **Commercial:** Software use follows MIT. Qwen3-ASR, the optional cleanup model and Silero VAD are separate components with their own notices; the README identifies Apache-2.0 and MIT terms. Branding is excluded from the code grant.
- **Cost:** Runs locally after downloads; no cloud transcription account required.

### Why it merits attention

Included for the documented creative workflow. A complete guide and popularity do not establish output reliability. [Source 1](https://github.com/kanaworksai-hue/tsuzuri/blob/main/README.md) [Source 2](https://github.com/kanaworksai-hue/tsuzuri/releases)

### Limitations

Short mixed Japanese/Chinese speech and sound-alike words can be mistranscribed. Cleanup language coverage is narrower than recognition. The paste shortcut assumes the documented keyboard behavior. [Source 1](https://github.com/kanaworksai-hue/tsuzuri/blob/main/README.md) [Source 2](https://github.com/kanaworksai-hue/tsuzuri/releases)

### Get the tool

- [Repository](https://github.com/kanaworksai-hue/tsuzuri)
- [Documentation](https://github.com/kanaworksai-hue/tsuzuri/blob/main/README.md)

## MochiToon

3D, reconstruction & assets · AI cel animation and inbetweening · AI agents for code-authored media production

A recently created project receiving its first full library guide; its creation is not proof of production readiness.

### Quality assessment: Quality unverified

Software licensing and a concrete creative AI use are supported. The remaining checks do not establish a recommendation.

Scope: AI-assisted toon look development, palette exploration and stylized character previews.

Evidence checked: 2026-10-27. No local execution implied.

- **Open-source software license · verified:** The complete root software license was read and archived. The grant covers this project code; unresolved model, service and asset terms are disclosed separately. [Source](https://github.com/kanaworksai-hue/mochitoon/blob/main/LICENSE)
- **Creative results · documented:** The README includes layered shader, palette and before/after examples. Agent automation is documented through agent/mochitoon_agent.py; no independent end-to-end agent reproduction was established. [Source](https://github.com/kanaworksai-hue/mochitoon/blob/main/README.md) [Source](https://github.com/kanaworksai-hue/mochitoon/releases)
- **Reproducible setup · documented:** Download the official mochitoon ZIP release and install it from disk in Blender preferences. For AI-assisted control, connect a compatible coding agent to the documented Python wrapper; the manual add-on remains usable without an LLM. Independent reproduction has not been established in this review. [Source](https://github.com/kanaworksai-hue/mochitoon/blob/main/README.md) [Source](https://github.com/kanaworksai-hue/mochitoon/releases)
- **Maintenance and support · documented:** Live review archived 5 recent commits, 4 published release records and 0 recent support/PR records. Latest sampled commit: 2026-10-23. The bounded support sample did not establish third-party resolution history. This is documented activity, not proof of sustained support or a complete blocker survey. [Source](https://github.com/kanaworksai-hue/mochitoon/commits/main) [Source](https://github.com/kanaworksai-hue/mochitoon/issues)
- **Independent use · unknown:** Reviewed official examples, the current support sample and bounded live web findings. Independent first-hand reproduction of this exact creative workflow was not established; author demonstrations are not treated as independent evidence.
- **Models, services and costs · documented:** GPL-3.0 software; the README specifies GPL-3.0-or-later. An optional external AI agent has its own model/service terms. Kana branding and sample assets are separate from the code license. Local compute plus any chosen external model or service; provider access and charges are separate. [Source](https://github.com/kanaworksai-hue/mochitoon/blob/main/README.md) [Source](https://github.com/kanaworksai-hue/mochitoon/releases)

Documentation review only; AI Media Scout did not install or run this software. Cycles and orthographic cameras are not supported. Setup can replace materials and change scene settings, so work on a project copy. Optional missing features do not alone establish a prototype verdict.

### How it uses AI

A Blender EEVEE toon-material add-on with an agent-facing Python wrapper, allowing an AI coding agent to select and tune the same material presets and scene setup used in its manual UI. The shader itself is not a neural renderer. [Source](https://github.com/kanaworksai-hue/mochitoon/blob/main/README.md) [Source](https://github.com/kanaworksai-hue/mochitoon/releases)

### Introduction

A Blender EEVEE toon-material add-on with an agent-facing Python wrapper, allowing an AI coding agent to select and tune the same material presets and scene setup used in its manual UI. The shader itself is not a neural renderer. [Source 1](https://github.com/kanaworksai-hue/mochitoon/blob/main/README.md) [Source 2](https://github.com/kanaworksai-hue/mochitoon/releases)

### What it is good for

AI-assisted toon look development, palette exploration and stylized character previews. [Source 1](https://github.com/kanaworksai-hue/mochitoon/blob/main/README.md) [Source 2](https://github.com/kanaworksai-hue/mochitoon/releases)

### Demo & examples

The README includes layered shader, palette and before/after examples. Agent automation is documented through agent/mochitoon_agent.py; no independent end-to-end agent reproduction was established. [Source 1](https://github.com/kanaworksai-hue/mochitoon/blob/main/README.md) [Source 2](https://github.com/kanaworksai-hue/mochitoon/releases)

### Install

Download the official mochitoon ZIP release and install it from disk in Blender preferences. For AI-assisted control, connect a compatible coding agent to the documented Python wrapper; the manual add-on remains usable without an LLM. [Source 1](https://github.com/kanaworksai-hue/mochitoon/blob/main/README.md) [Source 2](https://github.com/kanaworksai-hue/mochitoon/releases)

1. Obtain the official source or release linked below.
2. Download the official mochitoon ZIP release and install it from disk in Blender preferences. For AI-assisted control, connect a compatible coding agent to the documented Python wrapper; the manual add-on remains usable without an LLM.
### First project

Start with a short, representative project and inspect the result before a larger batch. [Source 1](https://github.com/kanaworksai-hue/mochitoon/blob/main/README.md) [Source 2](https://github.com/kanaworksai-hue/mochitoon/releases)

1. Select an object in an EEVEE scene and open the MochiToon panel.
2. Choose a palette and Make It Cute, then optionally set up the demonstration lighting.
3. Use the documented agent wrapper for material adjustments and inspect the rendered result.
### Hardware & software

Requirements below are documented for this workflow. Unspecified limits are not inferred. [Source 1](https://github.com/kanaworksai-hue/mochitoon/blob/main/README.md) [Source 2](https://github.com/kanaworksai-hue/mochitoon/releases)

- **Hardware:** Minimum system RAM, VRAM and total disk space are not documented in the reviewed instructions.
- **Software:** Blender 4.2+ with EEVEE; tested versions cited as 5.1/5.2. Some bloom behavior needs Blender 5.0+.
- **Platforms:** Blender add-on; a separate tested OS matrix is not documented.

### License, model weights & costs

The full software license was reviewed. Model weights, assets and services remain separate. [Source 1](https://github.com/kanaworksai-hue/mochitoon/blob/main/LICENSE) [Source 2](https://github.com/kanaworksai-hue/mochitoon/blob/main/README.md) [Source 3](https://github.com/kanaworksai-hue/mochitoon/releases)

- **Code:** GPL-3.0
- **Weights:** GPL-3.0 software; the README specifies GPL-3.0-or-later. An optional external AI agent has its own model/service terms. Kana branding and sample assets are separate from the code license.
- **Commercial:** Software use follows GPL-3.0. GPL-3.0 software; the README specifies GPL-3.0-or-later. An optional external AI agent has its own model/service terms. Kana branding and sample assets are separate from the code license.
- **Cost:** Local compute plus any chosen external model or service; provider access and charges are separate.

### Why it merits attention

Included for the documented creative workflow. A complete guide and popularity do not establish output reliability. [Source 1](https://github.com/kanaworksai-hue/mochitoon/blob/main/README.md) [Source 2](https://github.com/kanaworksai-hue/mochitoon/releases)

### Limitations

Cycles and orthographic cameras are not supported. Setup can replace materials and change scene settings, so work on a project copy. Optional missing features do not alone establish a prototype verdict. [Source 1](https://github.com/kanaworksai-hue/mochitoon/blob/main/README.md) [Source 2](https://github.com/kanaworksai-hue/mochitoon/releases)

### Get the tool

- [Repository](https://github.com/kanaworksai-hue/mochitoon)
- [Documentation](https://github.com/kanaworksai-hue/mochitoon/blob/main/README.md)

## Voiceolator

Audio, music & voice · Editing, captions & post-production · Games & production pipelines

A recently created project receiving its first full library guide; its creation is not proof of production readiness.

### Quality assessment: Quality unverified

Software licensing and a concrete creative AI use are supported. The remaining checks do not establish a recommendation.

Scope: Cleaning commentary and podcast/VOD recordings, and monitoring spoken audio while preserving other applications’ sound.

Evidence checked: 2026-10-27. No local execution implied.

- **Open-source software license · verified:** The complete root software license was read and archived. The grant covers this project code; unresolved model, service and asset terms are disclosed separately. [Source](https://github.com/Schockgeber/voiceolator/blob/main/LICENSE-APACHE)
- **Creative results · documented:** The README provides screenshots and a seven-scenario evaluation, including failures with singing and other voices. These are maintainer measurements rather than independent quality confirmation. [Source](https://github.com/Schockgeber/voiceolator/blob/main/README.md) [Source](https://huggingface.co/Ceva-IP/DPDFNet) [Source](https://github.com/Schockgeber/voiceolator/releases)
- **Reproducible setup · documented:** Use the official Windows installer/portable archive or Linux x86_64 AppImage. Review release checksums and the unsigned-build notice. The Quality engine on Windows needs the x64 Microsoft Visual C++ Redistributable; the Light engine is a fallback. Independent reproduction has not been established in this review. [Source](https://github.com/Schockgeber/voiceolator/blob/main/README.md) [Source](https://huggingface.co/Ceva-IP/DPDFNet) [Source](https://github.com/Schockgeber/voiceolator/releases)
- **Maintenance and support · documented:** Live review archived 10 recent commits, 2 published release records and 0 recent support/PR records. Latest sampled commit: 2026-10-27. The bounded support sample did not establish third-party resolution history. This is documented activity, not proof of sustained support or a complete blocker survey. [Source](https://github.com/Schockgeber/voiceolator/commits/main) [Source](https://github.com/Schockgeber/voiceolator/issues)
- **Independent use · unknown:** Reviewed official examples, the current support sample and bounded live web findings. Independent first-hand reproduction of this exact creative workflow was not established; author demonstrations are not treated as independent evidence.
- **Models, services and costs · documented:** The full Apache-2.0 license was reviewed; the project also offers MIT. DPDFNet’s model card declares Apache-2.0; DeepFilterNet, ONNX Runtime and multimedia libraries retain their notices. Local processing without an account or inference fee; optional ffmpeg retrieval is a network download. [Source](https://github.com/Schockgeber/voiceolator/blob/main/README.md) [Source](https://huggingface.co/Ceva-IP/DPDFNet) [Source](https://github.com/Schockgeber/voiceolator/releases)

Documentation review only; AI Media Scout did not install or run this software. It does not identify one specific speaker: singing, co-hosts and game-character voices can remain. Capture covers an entire application, not one browser tab. Latency and suppression figures vary with source and hardware.

### How it uses AI

A desktop audio cleaner using DPDFNet or DeepFilterNet3 to isolate speech from a selected application or a saved recording, with local CPU inference. [Source](https://github.com/Schockgeber/voiceolator/blob/main/README.md) [Source](https://huggingface.co/Ceva-IP/DPDFNet) [Source](https://github.com/Schockgeber/voiceolator/releases)

### Introduction

A desktop audio cleaner using DPDFNet or DeepFilterNet3 to isolate speech from a selected application or a saved recording, with local CPU inference. [Source 1](https://github.com/Schockgeber/voiceolator/blob/main/README.md) [Source 2](https://huggingface.co/Ceva-IP/DPDFNet) [Source 3](https://github.com/Schockgeber/voiceolator/releases)

### What it is good for

Cleaning commentary and podcast/VOD recordings, and monitoring spoken audio while preserving other applications’ sound. [Source 1](https://github.com/Schockgeber/voiceolator/blob/main/README.md) [Source 2](https://huggingface.co/Ceva-IP/DPDFNet) [Source 3](https://github.com/Schockgeber/voiceolator/releases)

### Demo & examples

The README provides screenshots and a seven-scenario evaluation, including failures with singing and other voices. These are maintainer measurements rather than independent quality confirmation. [Source 1](https://github.com/Schockgeber/voiceolator/blob/main/README.md) [Source 2](https://huggingface.co/Ceva-IP/DPDFNet) [Source 3](https://github.com/Schockgeber/voiceolator/releases)

### Install

Use the official Windows installer/portable archive or Linux x86_64 AppImage. Review release checksums and the unsigned-build notice. The Quality engine on Windows needs the x64 Microsoft Visual C++ Redistributable; the Light engine is a fallback. [Source 1](https://github.com/Schockgeber/voiceolator/blob/main/README.md) [Source 2](https://huggingface.co/Ceva-IP/DPDFNet) [Source 3](https://github.com/Schockgeber/voiceolator/releases)

1. Obtain the official source or release linked below.
2. Use the official Windows installer/portable archive or Linux x86_64 AppImage. Review release checksums and the unsigned-build notice. The Quality engine on Windows needs the x64 Microsoft Visual C++ Redistributable; the Light engine is a fallback.
### First project

Start with a short, representative project and inspect the result before a larger batch. [Source 1](https://github.com/Schockgeber/voiceolator/blob/main/README.md) [Source 2](https://huggingface.co/Ceva-IP/DPDFNet) [Source 3](https://github.com/Schockgeber/voiceolator/releases)

1. For files, drop a recording into the Files tab and select Isolate voice.
2. Review the generated voice track alongside the original; the video image is copied unchanged.
3. For live use, select the source application and output device, then measure latency on the actual machine.
### Hardware & software

Requirements below are documented for this workflow. Unspecified limits are not inferred. [Source 1](https://github.com/Schockgeber/voiceolator/blob/main/README.md) [Source 2](https://huggingface.co/Ceva-IP/DPDFNet) [Source 3](https://github.com/Schockgeber/voiceolator/releases)

- **Hardware:** Any modern CPU is the stated requirement; no GPU is needed. Minimum RAM and disk space are not specified.
- **Software:** Windows 10 version 2004+ or Windows 11 x64; Linux glibc 2.31+, PipeWire with pipewire-pulse or PulseAudio, X11 or Wayland/XWayland. ffmpeg is needed for video-file processing.
- **Platforms:** Windows and Linux x86_64 releases are documented. macOS support is not documented.

### License, model weights & costs

The full software license was reviewed. Model weights, assets and services remain separate. [Source 1](https://github.com/Schockgeber/voiceolator/blob/main/LICENSE-APACHE) [Source 2](https://github.com/Schockgeber/voiceolator/blob/main/README.md) [Source 3](https://huggingface.co/Ceva-IP/DPDFNet) [Source 4](https://github.com/Schockgeber/voiceolator/releases)

- **Code:** Apache-2.0
- **Weights:** The full Apache-2.0 license was reviewed; the project also offers MIT. DPDFNet’s model card declares Apache-2.0; DeepFilterNet, ONNX Runtime and multimedia libraries retain their notices.
- **Commercial:** Software use follows Apache-2.0. The full Apache-2.0 license was reviewed; the project also offers MIT. DPDFNet’s model card declares Apache-2.0; DeepFilterNet, ONNX Runtime and multimedia libraries retain their notices.
- **Cost:** Local processing without an account or inference fee; optional ffmpeg retrieval is a network download.

### Why it merits attention

Included for the documented creative workflow. A complete guide and popularity do not establish output reliability. [Source 1](https://github.com/Schockgeber/voiceolator/blob/main/README.md) [Source 2](https://huggingface.co/Ceva-IP/DPDFNet) [Source 3](https://github.com/Schockgeber/voiceolator/releases)

### Limitations

It does not identify one specific speaker: singing, co-hosts and game-character voices can remain. Capture covers an entire application, not one browser tab. Latency and suppression figures vary with source and hardware. [Source 1](https://github.com/Schockgeber/voiceolator/blob/main/README.md) [Source 2](https://huggingface.co/Ceva-IP/DPDFNet) [Source 3](https://github.com/Schockgeber/voiceolator/releases)

### Get the tool

- [Repository](https://github.com/Schockgeber/voiceolator)
- [Documentation](https://github.com/Schockgeber/voiceolator/blob/main/README.md)

## SubGenPlayer

Video, animation & film · Accessible media & assistive creation · Editing, captions & post-production

A recently created project receiving its first full library guide; its creation is not proof of production readiness.

### Quality assessment: Quality unverified

Software licensing and a concrete creative AI use are supported. The remaining checks do not establish a recommendation.

Scope: Previewing foreign-language footage and exporting editable original, English or bilingual subtitle files.

Evidence checked: 2026-10-27. No local execution implied.

- **Open-source software license · verified:** The complete root software license was read and archived. The grant covers this project code; unresolved model, service and asset terms are disclosed separately. [Source](https://github.com/megatih/SubGenPlayer/blob/main/LICENSE)
- **Creative results · documented:** The README includes player, model-management and subtitle-export screenshots attributed to UI tests. Real-time subtitle reliability has not been independently checked. [Source](https://github.com/megatih/SubGenPlayer/blob/main/README.md)
- **Reproducible setup · documented:** Use the official release or build the Xcode project after retrieving its pinned MPVKit frameworks. The release is not notarized; inspect the project and release provenance before opening. Download the selected speech and translation models within the app. Independent reproduction has not been established in this review. [Source](https://github.com/megatih/SubGenPlayer/blob/main/README.md)
- **Maintenance and support · documented:** Live review archived 6 recent commits, 1 published release records and 0 recent support/PR records. Latest sampled commit: 2026-10-26. The bounded support sample did not establish third-party resolution history. This is documented activity, not proof of sustained support or a complete blocker survey. [Source](https://github.com/megatih/SubGenPlayer/commits/main) [Source](https://github.com/megatih/SubGenPlayer/issues)
- **Independent use · unknown:** Reviewed official examples, the current support sample and bounded live web findings. Independent first-hand reproduction of this exact creative workflow was not established; author demonstrations are not treated as independent evidence.
- **Models, services and costs · documented:** GPL-3.0 software, declared GPL-3.0-or-later in the README; MPVKit/FFmpeg, WhisperKit, Qwen3 and Apple framework terms are separate. Model licenses need component-specific confirmation. Local inference after downloads; optional update checks and model retrieval use the network. [Source](https://github.com/megatih/SubGenPlayer/blob/main/README.md)

Documentation review only; AI Media Scout did not install or run this software. The available release is v1.0.0-rc.1. Model download tiers are not minimum whole-system RAM guarantees. Only the documented English/Japanese/Chinese dialogue to English workflow is described.

### How it uses AI

A native macOS player that generates English subtitles for English, Japanese and Chinese dialogue using local WhisperKit/Apple Speech and Qwen3/Apple Translation models. [Source](https://github.com/megatih/SubGenPlayer/blob/main/README.md)

### Introduction

A native macOS player that generates English subtitles for English, Japanese and Chinese dialogue using local WhisperKit/Apple Speech and Qwen3/Apple Translation models. [Source 1](https://github.com/megatih/SubGenPlayer/blob/main/README.md)

### What it is good for

Previewing foreign-language footage and exporting editable original, English or bilingual subtitle files. [Source 1](https://github.com/megatih/SubGenPlayer/blob/main/README.md)

### Demo & examples

The README includes player, model-management and subtitle-export screenshots attributed to UI tests. Real-time subtitle reliability has not been independently checked. [Source 1](https://github.com/megatih/SubGenPlayer/blob/main/README.md)

### Install

Use the official release or build the Xcode project after retrieving its pinned MPVKit frameworks. The release is not notarized; inspect the project and release provenance before opening. Download the selected speech and translation models within the app. [Source 1](https://github.com/megatih/SubGenPlayer/blob/main/README.md)

1. Obtain the official source or release linked below.
2. Use the official release or build the Xcode project after retrieving its pinned MPVKit frameworks. The release is not notarized; inspect the project and release provenance before opening. Download the selected speech and translation models within the app.

```sh
python3 Scripts/fetch-mpvkit.py
```


```sh
xcodebuild -scheme SubGenPlayer -destination "platform=macOS,arch=arm64" -skipMacroValidation CODE_SIGN_IDENTITY=- build
```

### First project

Start with a short, representative project and inspect the result before a larger batch. [Source 1](https://github.com/megatih/SubGenPlayer/blob/main/README.md)

1. Open a video; existing English embedded or sidecar subtitles take priority.
2. Choose the local transcription/translation models for the machine’s memory tier.
3. Review and export SRT, VTT or ASS, including bilingual output when needed.
### Hardware & software

Requirements below are documented for this workflow. Unspecified limits are not inferred. [Source 1](https://github.com/megatih/SubGenPlayer/blob/main/README.md)

- **Hardware:** The smallest documented model bundle is about 0.65 GB speech plus 1.0 GB translator for the below-24-GiB tier; larger tiers use up to 3.1 GB plus 18.5 GB. No minimum RAM threshold is explicitly stated.
- **Software:** macOS 27+ on Apple silicon; source build uses Xcode, Swift packages, Python 3 and pinned libmpv/FFmpeg frameworks.
- **Platforms:** Apple silicon macOS only; Windows and Linux support is not documented.

### License, model weights & costs

The full software license was reviewed. Model weights, assets and services remain separate. [Source 1](https://github.com/megatih/SubGenPlayer/blob/main/LICENSE) [Source 2](https://github.com/megatih/SubGenPlayer/blob/main/README.md)

- **Code:** GPL-3.0
- **Weights:** GPL-3.0 software, declared GPL-3.0-or-later in the README; MPVKit/FFmpeg, WhisperKit, Qwen3 and Apple framework terms are separate. Model licenses need component-specific confirmation.
- **Commercial:** Software use follows GPL-3.0. GPL-3.0 software, declared GPL-3.0-or-later in the README; MPVKit/FFmpeg, WhisperKit, Qwen3 and Apple framework terms are separate. Model licenses need component-specific confirmation.
- **Cost:** Local inference after downloads; optional update checks and model retrieval use the network.

### Why it merits attention

Included for the documented creative workflow. A complete guide and popularity do not establish output reliability. [Source 1](https://github.com/megatih/SubGenPlayer/blob/main/README.md)

### Limitations

The available release is v1.0.0-rc.1. Model download tiers are not minimum whole-system RAM guarantees. Only the documented English/Japanese/Chinese dialogue to English workflow is described. [Source 1](https://github.com/megatih/SubGenPlayer/blob/main/README.md)

### Get the tool

- [Repository](https://github.com/megatih/SubGenPlayer)
- [Documentation](https://github.com/megatih/SubGenPlayer/blob/main/README.md)

## XiaoFu

Mobile, edge & on-device creation · Audio, music & voice · Accessible media & assistive creation

A recently created project receiving its first full library guide; its creation is not proof of production readiness.

### Quality assessment: Quality unverified

Software licensing and a concrete creative AI use are supported. The remaining checks do not establish a recommendation.

Scope: Turning phone video dialogue into reusable audio and editable transcript drafts.

Evidence checked: 2026-10-27. No local execution implied.

- **Open-source software license · verified:** The complete root software license was read and archived. The grant covers this project code; unresolved model, service and asset terms are disclosed separately. [Source](https://github.com/Jolly-J/XiaoFu/blob/main/LICENSE)
- **Creative results · documented:** The Chinese README shows extraction, provider selection and transcript screenshots. Its local-processing claim applies to extraction, not the cloud transcription requests. [Source](https://github.com/Jolly-J/XiaoFu/blob/main/README.md)
- **Reproducible setup · documented:** Install the APK from the official GitHub release. For a source build, use JDK 17 and Android SDK 35 with the included Gradle wrapper. Configure a personal provider API key in the app for transcription. Independent reproduction has not been established in this review. [Source](https://github.com/Jolly-J/XiaoFu/blob/main/README.md)
- **Maintenance and support · documented:** Live review archived 4 recent commits, 1 published release records and 0 recent support/PR records. Latest sampled commit: 2026-10-26. The bounded support sample did not establish third-party resolution history. This is documented activity, not proof of sustained support or a complete blocker survey. [Source](https://github.com/Jolly-J/XiaoFu/commits/main) [Source](https://github.com/Jolly-J/XiaoFu/issues)
- **Independent use · unknown:** Reviewed official examples, the current support sample and bounded live web findings. Independent first-hand reproduction of this exact creative workflow was not established; author demonstrations are not treated as independent evidence.
- **Models, services and costs · documented:** MIT application code. Hosted SenseVoiceSmall/MiniMax inference, account access and provider data terms are separate; this app does not supply an offline local ASR model. Local extraction plus external ASR usage; verify current provider pricing instead of relying on the README’s quoted rate. [Source](https://github.com/Jolly-J/XiaoFu/blob/main/README.md)

Documentation review only; AI Media Scout did not install or run this software. The README’s blanket local/privacy language must not be applied to ASR: audio is uploaded to the provider. Source claims about free or paid rates were not independently confirmed today. AAC extraction and transcoding behavior should be checked for the source format.

### How it uses AI

An Android video-audio extractor with an AI transcription route using SenseVoiceSmall through SiliconFlow or a MiniMax ASR service. Extraction is local; AI transcription is sent directly to the chosen provider. [Source](https://github.com/Jolly-J/XiaoFu/blob/main/README.md)

### Introduction

An Android video-audio extractor with an AI transcription route using SenseVoiceSmall through SiliconFlow or a MiniMax ASR service. Extraction is local; AI transcription is sent directly to the chosen provider. [Source 1](https://github.com/Jolly-J/XiaoFu/blob/main/README.md)

### What it is good for

Turning phone video dialogue into reusable audio and editable transcript drafts. [Source 1](https://github.com/Jolly-J/XiaoFu/blob/main/README.md)

### Demo & examples

The Chinese README shows extraction, provider selection and transcript screenshots. Its local-processing claim applies to extraction, not the cloud transcription requests. [Source 1](https://github.com/Jolly-J/XiaoFu/blob/main/README.md)

### Install

Install the APK from the official GitHub release. For a source build, use JDK 17 and Android SDK 35 with the included Gradle wrapper. Configure a personal provider API key in the app for transcription. [Source 1](https://github.com/Jolly-J/XiaoFu/blob/main/README.md)

1. Obtain the official source or release linked below.
2. Install the APK from the official GitHub release. For a source build, use JDK 17 and Android SDK 35 with the included Gradle wrapper. Configure a personal provider API key in the app for transcription.

```sh
git clone https://github.com/Jolly-J/XiaoFu.git
```


```sh
cd XiaoFu
```


```sh
./gradlew assembleDebug
```

### First project

Start with a short, representative project and inspect the result before a larger batch. [Source 1](https://github.com/Jolly-J/XiaoFu/blob/main/README.md)

1. Choose a locally stored video and extract M4A or WAV.
2. If transcription is needed, select SiliconFlow or MiniMax and explicitly send the audio to that service.
3. Proofread the returned transcript and export or copy the text.
### Hardware & software

Requirements below are documented for this workflow. Unspecified limits are not inferred. [Source 1](https://github.com/Jolly-J/XiaoFu/blob/main/README.md)

- **Hardware:** Minimum RAM, free disk and supported chipset requirements are not stated.
- **Software:** Android 8.0/API 26+; Android 14+ recommended for the richer UI. Source toolchain: JDK 17, SDK 35, Kotlin 2.0 and Jetpack Compose.
- **Platforms:** Android; desktop and iOS builds are not documented.

### License, model weights & costs

The full software license was reviewed. Model weights, assets and services remain separate. [Source 1](https://github.com/Jolly-J/XiaoFu/blob/main/LICENSE) [Source 2](https://github.com/Jolly-J/XiaoFu/blob/main/README.md)

- **Code:** MIT
- **Weights:** MIT application code. Hosted SenseVoiceSmall/MiniMax inference, account access and provider data terms are separate; this app does not supply an offline local ASR model.
- **Commercial:** Software use follows MIT. MIT application code. Hosted SenseVoiceSmall/MiniMax inference, account access and provider data terms are separate; this app does not supply an offline local ASR model.
- **Cost:** Local extraction plus external ASR usage; verify current provider pricing instead of relying on the README’s quoted rate.

### Why it merits attention

Included for the documented creative workflow. A complete guide and popularity do not establish output reliability. [Source 1](https://github.com/Jolly-J/XiaoFu/blob/main/README.md)

### Limitations

The README’s blanket local/privacy language must not be applied to ASR: audio is uploaded to the provider. Source claims about free or paid rates were not independently confirmed today. AAC extraction and transcoding behavior should be checked for the source format. [Source 1](https://github.com/Jolly-J/XiaoFu/blob/main/README.md)

### Get the tool

- [Repository](https://github.com/Jolly-J/XiaoFu)
- [Documentation](https://github.com/Jolly-J/XiaoFu/blob/main/README.md)

## Repo2Reels

Video, animation & film · Audio, music & voice · AI kinetic typography and animated lettering · Creative publishing & presentation

A recently created project receiving its first full library guide; its creation is not proof of production readiness.

### Quality assessment: Quality unverified

Software licensing and a concrete creative AI use are supported. The remaining checks do not establish a recommendation.

Scope: Producing short vertical product explainers with editable scripts, consistent branding, voice-over and caption timing.

Evidence checked: 2026-10-27. No local execution implied.

- **Open-source software license · verified:** The complete root software license was read and archived. The grant covers this project code; unresolved model, service and asset terms are disclosed separately. [Source](https://github.com/sravinp-art/Repo2Reels/blob/main/LICENSE)
- **Creative results · documented:** The README embeds three product reels, a starter reel and contact sheets. They show the author’s workflow; they do not establish independent reproduction. [Source](https://github.com/sravinp-art/Repo2Reels/blob/main/README.md) [Source](https://huggingface.co/hexgrad/Kokoro-82M)
- **Reproducible setup · documented:** Clone the project and use its documented setup script to prepare the Python environment, headless Chromium and voice models, then render the starter project. These are instructions for a future user; the scout did not execute them. Independent reproduction has not been established in this review. [Source](https://github.com/sravinp-art/Repo2Reels/blob/main/README.md) [Source](https://huggingface.co/hexgrad/Kokoro-82M)
- **Maintenance and support · documented:** Live review archived 10 recent commits, 0 published release records and 0 recent support/PR records. Latest sampled commit: 2026-10-26. The bounded support sample did not establish third-party resolution history. This is documented activity, not proof of sustained support or a complete blocker survey. [Source](https://github.com/sravinp-art/Repo2Reels/commits/main) [Source](https://github.com/sravinp-art/Repo2Reels/issues)
- **Independent use · unknown:** Reviewed official examples, the current support sample and bounded live web findings. Independent first-hand reproduction of this exact creative workflow was not established; author demonstrations are not treated as independent evidence.
- **Models, services and costs · documented:** MIT code and starter. Kokoro weights are Apache-2.0, fonts SIL OFL, and Whisper/runtime dependencies have separate notices. The Keyva name, logo and example reels are excluded branded material. Local inference with no API key; an optional Claude Code plugin has its own service requirements. [Source](https://github.com/sravinp-art/Repo2Reels/blob/main/README.md) [Source](https://huggingface.co/hexgrad/Kokoro-82M)

Documentation review only; AI Media Scout did not install or run this software. English only; digits must be written as spoken words in voice lines, and unfamiliar names can need pronunciation edits. Custom music import is not supported. Rendering a reel does not publish it to social platforms.

### How it uses AI

A local short-video pipeline combining Kokoro text-to-speech, optional Whisper read-back checks, timed captions, HTML motion graphics and generated musical cues. [Source](https://github.com/sravinp-art/Repo2Reels/blob/main/README.md) [Source](https://huggingface.co/hexgrad/Kokoro-82M)

### Introduction

A local short-video pipeline combining Kokoro text-to-speech, optional Whisper read-back checks, timed captions, HTML motion graphics and generated musical cues. [Source 1](https://github.com/sravinp-art/Repo2Reels/blob/main/README.md) [Source 2](https://huggingface.co/hexgrad/Kokoro-82M)

### What it is good for

Producing short vertical product explainers with editable scripts, consistent branding, voice-over and caption timing. [Source 1](https://github.com/sravinp-art/Repo2Reels/blob/main/README.md) [Source 2](https://huggingface.co/hexgrad/Kokoro-82M)

### Demo & examples

The README embeds three product reels, a starter reel and contact sheets. They show the author’s workflow; they do not establish independent reproduction. [Source 1](https://github.com/sravinp-art/Repo2Reels/blob/main/README.md) [Source 2](https://huggingface.co/hexgrad/Kokoro-82M)

### Install

Clone the project and use its documented setup script to prepare the Python environment, headless Chromium and voice models, then render the starter project. These are instructions for a future user; the scout did not execute them. [Source 1](https://github.com/sravinp-art/Repo2Reels/blob/main/README.md) [Source 2](https://huggingface.co/hexgrad/Kokoro-82M)

1. Obtain the official source or release linked below.
2. Clone the project and use its documented setup script to prepare the Python environment, headless Chromium and voice models, then render the starter project. These are instructions for a future user; the scout did not execute them.

```sh
git clone https://github.com/sravinp-art/Repo2Reels
```


```sh
cd Repo2Reels
```


```sh
./setup.sh
```


```sh
python3 make.py projects/starter
```

### First project

Start with a short, representative project and inspect the result before a larger batch. [Source 1](https://github.com/sravinp-art/Repo2Reels/blob/main/README.md) [Source 2](https://huggingface.co/hexgrad/Kokoro-82M)

1. Create a project with python3 make.py new acme.
2. Edit project.json for five spoken lines and branding; edit scenes.js for the visual content.
3. Render, inspect the contact sheet, listen to the voice and use the optional --listen check before sharing.
### Hardware & software

Requirements below are documented for this workflow. Unspecified limits are not inferred. [Source 1](https://github.com/sravinp-art/Repo2Reels/blob/main/README.md) [Source 2](https://huggingface.co/hexgrad/Kokoro-82M)

- **Hardware:** CPU execution without a GPU; setup describes about 350 MB of voice assets, excluding runtime/render outputs. Whole-system RAM and total disk minimum are not stated.
- **Software:** Python 3.10+, ffmpeg and git; setup downloads a headless Chromium and models. No Node/React toolchain is required for the renderer.
- **Platforms:** macOS and Linux; Windows through WSL is documented.

### License, model weights & costs

The full software license was reviewed. Model weights, assets and services remain separate. [Source 1](https://github.com/sravinp-art/Repo2Reels/blob/main/LICENSE) [Source 2](https://github.com/sravinp-art/Repo2Reels/blob/main/README.md) [Source 3](https://huggingface.co/hexgrad/Kokoro-82M)

- **Code:** MIT
- **Weights:** MIT code and starter. Kokoro weights are Apache-2.0, fonts SIL OFL, and Whisper/runtime dependencies have separate notices. The Keyva name, logo and example reels are excluded branded material.
- **Commercial:** Software use follows MIT. MIT code and starter. Kokoro weights are Apache-2.0, fonts SIL OFL, and Whisper/runtime dependencies have separate notices. The Keyva name, logo and example reels are excluded branded material.
- **Cost:** Local inference with no API key; an optional Claude Code plugin has its own service requirements.

### Why it merits attention

Included for the documented creative workflow. A complete guide and popularity do not establish output reliability. [Source 1](https://github.com/sravinp-art/Repo2Reels/blob/main/README.md) [Source 2](https://huggingface.co/hexgrad/Kokoro-82M)

### Limitations

English only; digits must be written as spoken words in voice lines, and unfamiliar names can need pronunciation edits. Custom music import is not supported. Rendering a reel does not publish it to social platforms. [Source 1](https://github.com/sravinp-art/Repo2Reels/blob/main/README.md) [Source 2](https://huggingface.co/hexgrad/Kokoro-82M)

### Get the tool

- [Repository](https://github.com/sravinp-art/Repo2Reels)
- [Documentation](https://github.com/sravinp-art/Repo2Reels/blob/main/README.md)

## 3D Asset Agent Skills

3D, reconstruction & assets · AI agents for code-authored media production · Games & production pipelines

A recently created project receiving its first full library guide; its creation is not proof of production readiness.

### Quality assessment: Quality unverified

Software licensing and a concrete creative AI use are supported. The remaining checks do not establish a recommendation.

Scope: Building an attributed reference/asset shortlist for Blender scenes, games and simulation prototypes before modeling from scratch.

Evidence checked: 2026-10-27. No local execution implied.

- **Open-source software license · verified:** The complete root software license was read and archived. The grant covers this project code; unresolved model, service and asset terms are disclosed separately. [Source](https://github.com/jeak01/3d-asset-agent-skills/blob/main/LICENSE)
- **Creative results · documented:** The README shows twelve source-attributed catalog previews and a generated comparison-gallery workflow. Download tests do not prove successful Blender import or editing. [Source](https://github.com/jeak01/3d-asset-agent-skills/blob/main/README.md)
- **Reproducible setup · documented:** Clone the repository and place its simready-3d-assistant folder in a compatible agent’s skill directory, after reviewing its instructions. The standalone search helper only requires Python’s standard library. Independent reproduction has not been established in this review. [Source](https://github.com/jeak01/3d-asset-agent-skills/blob/main/README.md)
- **Maintenance and support · documented:** Live review archived 4 recent commits, 0 published release records and 0 recent support/PR records. Latest sampled commit: 2026-10-26. The bounded support sample did not establish third-party resolution history. This is documented activity, not proof of sustained support or a complete blocker survey. [Source](https://github.com/jeak01/3d-asset-agent-skills/commits/main) [Source](https://github.com/jeak01/3d-asset-agent-skills/issues)
- **Independent use · unknown:** Reviewed official examples, the current support sample and bounded live web findings. Independent first-hand reproduction of this exact creative workflow was not established; author demonstrations are not treated as independent evidence.
- **Models, services and costs · documented:** MIT code. Models retain their own terms; the default filter admits declared CC-BY-4.0 or CC0-1.0 with a license file. Scenario attribution and possible third-party rights remain relevant. Public catalog reads do not require added API keys; the optional agent/model and editing application can have separate costs. [Source](https://github.com/jeak01/3d-asset-agent-skills/blob/main/README.md)

Documentation review only; AI Media Scout did not install or run this software. Scenario keyword coverage excludes records without useful prompt metadata. The helper does not edit or render models, and successful download does not certify import, physics, printability or rights clearance.

### How it uses AI

An AI-agent skill and Python helper for finding reusable 3D assets, inspecting real previews and licensing, then preparing a modeling handoff. Agent reasoning and catalog vector search assist selection; the helper does not generate geometry itself. [Source](https://github.com/jeak01/3d-asset-agent-skills/blob/main/README.md)

### Introduction

An AI-agent skill and Python helper for finding reusable 3D assets, inspecting real previews and licensing, then preparing a modeling handoff. Agent reasoning and catalog vector search assist selection; the helper does not generate geometry itself. [Source 1](https://github.com/jeak01/3d-asset-agent-skills/blob/main/README.md)

### What it is good for

Building an attributed reference/asset shortlist for Blender scenes, games and simulation prototypes before modeling from scratch. [Source 1](https://github.com/jeak01/3d-asset-agent-skills/blob/main/README.md)

### Demo & examples

The README shows twelve source-attributed catalog previews and a generated comparison-gallery workflow. Download tests do not prove successful Blender import or editing. [Source 1](https://github.com/jeak01/3d-asset-agent-skills/blob/main/README.md)

### Install

Clone the repository and place its simready-3d-assistant folder in a compatible agent’s skill directory, after reviewing its instructions. The standalone search helper only requires Python’s standard library. [Source 1](https://github.com/jeak01/3d-asset-agent-skills/blob/main/README.md)

1. Obtain the official source or release linked below.
2. Clone the repository and place its simready-3d-assistant folder in a compatible agent’s skill directory, after reviewing its instructions. The standalone search helper only requires Python’s standard library.

```sh
git clone https://github.com/jeak01/3d-asset-agent-skills.git
```


```sh
cd 3d-asset-agent-skills
```


```sh
python simready-3d-assistant/scripts/simready.py search --query "mobile cart" --intent "A sci-fi maintenance cart" --limit 5 --out ./candidates
```

### First project

Start with a short, representative project and inspect the result before a larger batch. [Source 1](https://github.com/jeak01/3d-asset-agent-skills/blob/main/README.md)

1. Describe the intended object and compare returned previews, source URLs and licenses.
2. Select a model before downloading its pinned package and attribution record.
3. Prepare a modeling handoff and validate the package in a compatible 3D application.
### Hardware & software

Requirements below are documented for this workflow. Unspecified limits are not inferred. [Source 1](https://github.com/jeak01/3d-asset-agent-skills/blob/main/README.md)

- **Hardware:** Minimum RAM/VRAM are not documented. The default 512 MiB download budget is a retrieval limit, not the application’s hardware requirement.
- **Software:** Python 3.10+ for discovery/download; a compatible AI agent for the assisted workflow and Blender or another suitable application for actual editing.
- **Platforms:** An explicit tested OS matrix is not provided; Python compatibility alone is not a platform test.

### License, model weights & costs

The full software license was reviewed. Model weights, assets and services remain separate. [Source 1](https://github.com/jeak01/3d-asset-agent-skills/blob/main/LICENSE) [Source 2](https://github.com/jeak01/3d-asset-agent-skills/blob/main/README.md)

- **Code:** MIT
- **Weights:** MIT code. Models retain their own terms; the default filter admits declared CC-BY-4.0 or CC0-1.0 with a license file. Scenario attribution and possible third-party rights remain relevant.
- **Commercial:** Software use follows MIT. MIT code. Models retain their own terms; the default filter admits declared CC-BY-4.0 or CC0-1.0 with a license file. Scenario attribution and possible third-party rights remain relevant.
- **Cost:** Public catalog reads do not require added API keys; the optional agent/model and editing application can have separate costs.

### Why it merits attention

Included for the documented creative workflow. A complete guide and popularity do not establish output reliability. [Source 1](https://github.com/jeak01/3d-asset-agent-skills/blob/main/README.md)

### Limitations

Scenario keyword coverage excludes records without useful prompt metadata. The helper does not edit or render models, and successful download does not certify import, physics, printability or rights clearance. [Source 1](https://github.com/jeak01/3d-asset-agent-skills/blob/main/README.md)

### Get the tool

- [Repository](https://github.com/jeak01/3d-asset-agent-skills)
- [Documentation](https://github.com/jeak01/3d-asset-agent-skills/blob/main/README.md)

## Lumen

Data art & scientific visualization · AI cartography and artistic maps · Creative publishing & presentation

First full guide in this library. This is a newly reviewed discovery, not a claim that the software launched today.

### Quality assessment: Quality unverified

Software licensing and a concrete creative AI use are supported. The remaining checks do not establish a recommendation.

Scope: Data-driven storytelling, exhibition dashboards, explanatory charts and editable visual research reports.

Evidence checked: 2026-10-27. No local execution implied.

- **Open-source software license · verified:** The complete root software license was read and archived. The grant covers this project code; unresolved model, service and asset terms are disclosed separately. [Source](https://github.com/holoviz/lumen/blob/main/LICENSE)
- **Creative results · documented:** Official documentation demonstrates chart generation, annotations, report/story mode and notebook/HTML/Word exports. Release v1.4.0 was published October 26; a release alone is not a quality verdict. [Source](https://github.com/holoviz/lumen/blob/main/README.md) [Source](https://lumen.holoviz.org/getting_started/using_lumen_ai/) [Source](https://github.com/holoviz/lumen/releases/tag/v1.4.0)
- **Reproducible setup · documented:** Install Lumen with pip or conda-forge using Python 3.11+, then start the Explorer against a CSV or another supported data source. Configure the chosen LLM provider in the interface; local and hosted providers have different resource and account requirements. Independent reproduction has not been established in this review. [Source](https://github.com/holoviz/lumen/blob/main/README.md) [Source](https://lumen.holoviz.org/getting_started/using_lumen_ai/) [Source](https://github.com/holoviz/lumen/releases/tag/v1.4.0)
- **Maintenance and support · documented:** Live review archived 10 recent commits, 5 published release records and 10 recent support/PR records. Latest sampled commit: 2026-10-26. Current sampled topics include Loading a big CSV is slow; Allow users to select charts to keep / discard in exported Report. This is documented activity, not proof of sustained support or a complete blocker survey. [Source](https://github.com/holoviz/lumen/commits/main) [Source](https://github.com/holoviz/lumen/issues)
- **Independent use · unknown:** Reviewed official examples, the current support sample and bounded live web findings. Independent first-hand reproduction of this exact creative workflow was not established; author demonstrations are not treated as independent evidence.
- **Models, services and costs · documented:** BSD-3-Clause code. Selected LLMs, hosted providers, local weights and external data sources retain their own licenses and service terms. Local models use local compute; hosted models or authenticated agent providers can incur charges. A keyless provider route does not establish unrestricted or permanent free service. [Source](https://github.com/holoviz/lumen/blob/main/README.md) [Source](https://lumen.holoviz.org/getting_started/using_lumen_ai/) [Source](https://github.com/holoviz/lumen/releases/tag/v1.4.0)

Documentation review only; AI Media Scout did not install or run this software. Generated SQL, narratives and visualization specifications require human checking. The current issue sample includes large-CSV loading and validation concerns. Exportable reusable report templates are still described as planned.

### How it uses AI

An extensible LLM-agent framework that turns questions about datasets into inspectable SQL pipelines, interactive charts, tables, dashboards and narrative reports. [Source](https://github.com/holoviz/lumen/blob/main/README.md) [Source](https://lumen.holoviz.org/getting_started/using_lumen_ai/) [Source](https://github.com/holoviz/lumen/releases/tag/v1.4.0)

### Introduction

An extensible LLM-agent framework that turns questions about datasets into inspectable SQL pipelines, interactive charts, tables, dashboards and narrative reports. [Source 1](https://github.com/holoviz/lumen/blob/main/README.md) [Source 2](https://lumen.holoviz.org/getting_started/using_lumen_ai/) [Source 3](https://github.com/holoviz/lumen/releases/tag/v1.4.0)

### What it is good for

Data-driven storytelling, exhibition dashboards, explanatory charts and editable visual research reports. [Source 1](https://github.com/holoviz/lumen/blob/main/README.md) [Source 2](https://lumen.holoviz.org/getting_started/using_lumen_ai/) [Source 3](https://github.com/holoviz/lumen/releases/tag/v1.4.0)

### Demo & examples

Official documentation demonstrates chart generation, annotations, report/story mode and notebook/HTML/Word exports. Release v1.4.0 was published October 26; a release alone is not a quality verdict. [Source 1](https://github.com/holoviz/lumen/blob/main/README.md) [Source 2](https://lumen.holoviz.org/getting_started/using_lumen_ai/) [Source 3](https://github.com/holoviz/lumen/releases/tag/v1.4.0)

### Install

Install Lumen with pip or conda-forge using Python 3.11+, then start the Explorer against a CSV or another supported data source. Configure the chosen LLM provider in the interface; local and hosted providers have different resource and account requirements. [Source 1](https://github.com/holoviz/lumen/blob/main/README.md) [Source 2](https://lumen.holoviz.org/getting_started/using_lumen_ai/) [Source 3](https://github.com/holoviz/lumen/releases/tag/v1.4.0)

1. Obtain the official source or release linked below.
2. Install Lumen with pip or conda-forge using Python 3.11+, then start the Explorer against a CSV or another supported data source. Configure the chosen LLM provider in the interface; local and hosted providers have different resource and account requirements.

```sh
pip install lumen
```


```sh
lumen-ai serve data.csv
```

### First project

Start with a short, representative project and inspect the result before a larger batch. [Source 1](https://github.com/holoviz/lumen/blob/main/README.md) [Source 2](https://lumen.holoviz.org/getting_started/using_lumen_ai/) [Source 3](https://github.com/holoviz/lumen/releases/tag/v1.4.0)

1. Load a small dataset and ask for a specific chart or comparison.
2. Inspect the generated query, labels and values, then manually edit or ask for a refinement.
3. Use Report mode to arrange the story and export the notebook or HTML; Word export additionally needs python-docx.
### Hardware & software

Requirements below are documented for this workflow. Unspecified limits are not inferred. [Source 1](https://github.com/holoviz/lumen/blob/main/README.md) [Source 2](https://lumen.holoviz.org/getting_started/using_lumen_ai/) [Source 3](https://github.com/holoviz/lumen/releases/tag/v1.4.0)

- **Hardware:** Minimum system RAM, VRAM and total disk space are not documented in the reviewed instructions.
- **Software:** Python 3.11+; Panel-based UI and provider-specific model access. Word export uses optional python-docx.
- **Platforms:** Linux, Windows and macOS are explicitly documented.

### License, model weights & costs

The full software license was reviewed. Model weights, assets and services remain separate. [Source 1](https://github.com/holoviz/lumen/blob/main/LICENSE) [Source 2](https://github.com/holoviz/lumen/blob/main/README.md) [Source 3](https://lumen.holoviz.org/getting_started/using_lumen_ai/) [Source 4](https://github.com/holoviz/lumen/releases/tag/v1.4.0)

- **Code:** BSD-3-Clause
- **Weights:** BSD-3-Clause code. Selected LLMs, hosted providers, local weights and external data sources retain their own licenses and service terms.
- **Commercial:** Software use follows BSD-3-Clause. BSD-3-Clause code. Selected LLMs, hosted providers, local weights and external data sources retain their own licenses and service terms.
- **Cost:** Local models use local compute; hosted models or authenticated agent providers can incur charges. A keyless provider route does not establish unrestricted or permanent free service.

### Why it merits attention

Included for the documented creative workflow. A complete guide and popularity do not establish output reliability. [Source 1](https://github.com/holoviz/lumen/blob/main/README.md) [Source 2](https://lumen.holoviz.org/getting_started/using_lumen_ai/) [Source 3](https://github.com/holoviz/lumen/releases/tag/v1.4.0)

### Limitations

Generated SQL, narratives and visualization specifications require human checking. The current issue sample includes large-CSV loading and validation concerns. Exportable reusable report templates are still described as planned. [Source 1](https://github.com/holoviz/lumen/blob/main/README.md) [Source 2](https://lumen.holoviz.org/getting_started/using_lumen_ai/) [Source 3](https://github.com/holoviz/lumen/releases/tag/v1.4.0)

### Get the tool

- [Repository](https://github.com/holoviz/lumen)
- [Documentation](https://github.com/holoviz/lumen/blob/main/README.md)

## SciSketch

Data art & scientific visualization · Creative learning & authoring · Vector graphics, illustration & textures

First full guide in this library. This is a newly reviewed discovery, not a claim that the software launched today.

### Quality assessment: Quality unverified

Software licensing and a concrete creative AI use are supported. The remaining checks do not establish a recommendation.

Scope: Drafting research illustrations and explanatory diagrams from parsed scientific papers.

Evidence checked: 2026-10-27. No local execution implied.

- **Open-source software license · verified:** The complete root software license was read and archived. The grant covers this project code; unresolved model, service and asset terms are disclosed separately. [Source](https://github.com/yale-nlp/SciSketch/blob/main/LICENSE)
- **Creative results · documented:** The official EMNLP demonstration paper and linked Hugging Face Space describe the paper-to-diagram workflow. Output accuracy and layout quality have not been independently reproduced here. [Source](https://github.com/yale-nlp/SciSketch/blob/main/README.md) [Source](https://aclanthology.org/2025.emnlp-demos.28/) [Source](https://huggingface.co/spaces/zihang93/SCISKETCH)
- **Reproducible setup · documented:** Clone the repository, create a Python 3.10+ environment, install requirements and configure the foundation-model endpoint/key in the documented local environment file. Prepare a parsed paper and its input images before running the generation script. Independent reproduction has not been established in this review. [Source](https://github.com/yale-nlp/SciSketch/blob/main/README.md) [Source](https://aclanthology.org/2025.emnlp-demos.28/) [Source](https://huggingface.co/spaces/zihang93/SCISKETCH)
- **Maintenance and support · documented:** Live review archived 2 recent commits, 0 published release records and 0 recent support/PR records. Latest sampled commit: 2025-04-24. The bounded support sample did not establish third-party resolution history. This is documented activity, not proof of sustained support or a complete blocker survey. [Source](https://github.com/yale-nlp/SciSketch/commits/main) [Source](https://github.com/yale-nlp/SciSketch/issues)
- **Independent use · unknown:** Reviewed official examples, the current support sample and bounded live web findings. Independent first-hand reproduction of this exact creative workflow was not established; author demonstrations are not treated as independent evidence.
- **Models, services and costs · documented:** MIT repository code. External models, API access, icons, paper figures and other inputs retain separate terms. Local compute plus any chosen external model or service; provider access and charges are separate. [Source](https://github.com/yale-nlp/SciSketch/blob/main/README.md) [Source](https://aclanthology.org/2025.emnlp-demos.28/) [Source](https://huggingface.co/spaces/zihang93/SCISKETCH)

Documentation review only; AI Media Scout did not install or run this software. Not an evidence verifier: a plausible figure can misrepresent the source paper. Endpoint compatibility and hardware minima are not fully specified. The sampled repository history is small and no independent reproduction was established.

### How it uses AI

A scientific-diagram pipeline that uses language models to plan and refine a paper’s visual structure, then composes diagram content with SVG icons and empirical images. [Source](https://github.com/yale-nlp/SciSketch/blob/main/README.md) [Source](https://aclanthology.org/2025.emnlp-demos.28/) [Source](https://huggingface.co/spaces/zihang93/SCISKETCH)

### Introduction

A scientific-diagram pipeline that uses language models to plan and refine a paper’s visual structure, then composes diagram content with SVG icons and empirical images. [Source 1](https://github.com/yale-nlp/SciSketch/blob/main/README.md) [Source 2](https://aclanthology.org/2025.emnlp-demos.28/) [Source 3](https://huggingface.co/spaces/zihang93/SCISKETCH)

### What it is good for

Drafting research illustrations and explanatory diagrams from parsed scientific papers. [Source 1](https://github.com/yale-nlp/SciSketch/blob/main/README.md) [Source 2](https://aclanthology.org/2025.emnlp-demos.28/) [Source 3](https://huggingface.co/spaces/zihang93/SCISKETCH)

### Demo & examples

The official EMNLP demonstration paper and linked Hugging Face Space describe the paper-to-diagram workflow. Output accuracy and layout quality have not been independently reproduced here. [Source 1](https://github.com/yale-nlp/SciSketch/blob/main/README.md) [Source 2](https://aclanthology.org/2025.emnlp-demos.28/) [Source 3](https://huggingface.co/spaces/zihang93/SCISKETCH)

### Install

Clone the repository, create a Python 3.10+ environment, install requirements and configure the foundation-model endpoint/key in the documented local environment file. Prepare a parsed paper and its input images before running the generation script. [Source 1](https://github.com/yale-nlp/SciSketch/blob/main/README.md) [Source 2](https://aclanthology.org/2025.emnlp-demos.28/) [Source 3](https://huggingface.co/spaces/zihang93/SCISKETCH)

1. Obtain the official source or release linked below.
2. Clone the repository, create a Python 3.10+ environment, install requirements and configure the foundation-model endpoint/key in the documented local environment file. Prepare a parsed paper and its input images before running the generation script.

```sh
git clone https://github.com/yale-nlp/SciSketch.git
```


```sh
cd SciSketch
```


```sh
pip install -r requirements.txt
```


```sh
bash bin/generate_diagrams.sh --sample_id paper_name
```

### First project

Start with a short, representative project and inspect the result before a larger batch. [Source 1](https://github.com/yale-nlp/SciSketch/blob/main/README.md) [Source 2](https://aclanthology.org/2025.emnlp-demos.28/) [Source 3](https://huggingface.co/spaces/zihang93/SCISKETCH)

1. Place the parsed paper under the documented samples/parsed_papers layout.
2. Supply any empirical images required for the figure and run the sample-ID workflow.
3. Check the diagram against the paper, correct scientific labels and inspect icon/image rights before publication.
### Hardware & software

Requirements below are documented for this workflow. Unspecified limits are not inferred. [Source 1](https://github.com/yale-nlp/SciSketch/blob/main/README.md) [Source 2](https://aclanthology.org/2025.emnlp-demos.28/) [Source 3](https://huggingface.co/spaces/zihang93/SCISKETCH)

- **Hardware:** Minimum system RAM, VRAM and total disk space are not documented in the reviewed instructions.
- **Software:** Python 3.10+ and requirements.txt; a configured language-model API or compatible endpoint.
- **Platforms:** An explicit tested OS matrix is not documented. A hosted demo is linked separately from local execution.

### License, model weights & costs

The full software license was reviewed. Model weights, assets and services remain separate. [Source 1](https://github.com/yale-nlp/SciSketch/blob/main/LICENSE) [Source 2](https://github.com/yale-nlp/SciSketch/blob/main/README.md) [Source 3](https://aclanthology.org/2025.emnlp-demos.28/) [Source 4](https://huggingface.co/spaces/zihang93/SCISKETCH)

- **Code:** MIT
- **Weights:** MIT repository code. External models, API access, icons, paper figures and other inputs retain separate terms.
- **Commercial:** Software use follows MIT. MIT repository code. External models, API access, icons, paper figures and other inputs retain separate terms.
- **Cost:** Local compute plus any chosen external model or service; provider access and charges are separate.

### Why it merits attention

Included for the documented creative workflow. A complete guide and popularity do not establish output reliability. [Source 1](https://github.com/yale-nlp/SciSketch/blob/main/README.md) [Source 2](https://aclanthology.org/2025.emnlp-demos.28/) [Source 3](https://huggingface.co/spaces/zihang93/SCISKETCH)

### Limitations

Not an evidence verifier: a plausible figure can misrepresent the source paper. Endpoint compatibility and hardware minima are not fully specified. The sampled repository history is small and no independent reproduction was established. [Source 1](https://github.com/yale-nlp/SciSketch/blob/main/README.md) [Source 2](https://aclanthology.org/2025.emnlp-demos.28/) [Source 3](https://huggingface.co/spaces/zihang93/SCISKETCH)

### Get the tool

- [Repository](https://github.com/yale-nlp/SciSketch)
- [Documentation](https://github.com/yale-nlp/SciSketch/blob/main/README.md)

## CAD-Coder

3D, reconstruction & assets · AI parametric design and jewelry · 3D printing & generative CAD

First full guide in this library. This is a newly reviewed discovery, not a claim that the software launched today.

### Quality assessment: Quality unverified

Software licensing and a concrete creative AI use are supported. The remaining checks do not establish a recommendation.

Scope: Image-conditioned parametric CAD experiments and studying how generated construction code relates to the final shape.

Evidence checked: 2026-10-27. No local execution implied.

- **Open-source software license · verified:** The complete root software license was read and archived. The grant covers this project code; unresolved model, service and asset terms are disclosed separately. [Source](https://github.com/anniedoris/CAD-Coder/blob/main/LICENSE)
- **Creative results · documented:** The paper and repository show image-to-code examples. The documented workflow is batch inference; the planned interactive chat route is not presented as available. [Source](https://github.com/anniedoris/CAD-Coder/blob/main/README.md) [Source](https://arxiv.org/abs/2505.14646) [Source](https://huggingface.co/CADCODER/CAD-Coder/tree/main)
- **Reproducible setup · documented:** Use the documented Python 3.10 llava environment for inference and a separate cad_iou environment for geometry reconstruction because their dependencies conflict. Install the project and matching training/inference dependencies, obtain the model and test inputs, then run the batch evaluation script. Independent reproduction has not been established in this review. [Source](https://github.com/anniedoris/CAD-Coder/blob/main/README.md) [Source](https://arxiv.org/abs/2505.14646) [Source](https://huggingface.co/CADCODER/CAD-Coder/tree/main)
- **Maintenance and support · documented:** Live review archived 8 recent commits, 0 published release records and 6 recent support/PR records. Latest sampled commit: 2025-07-17. Current sampled topics include how to convert cadquery to point cloud in order to compute cd and iou?; CAD Drafter Willing to Participate in Testing & Feedback. This is documented activity, not proof of sustained support or a complete blocker survey. [Source](https://github.com/anniedoris/CAD-Coder/commits/main) [Source](https://github.com/anniedoris/CAD-Coder/issues)
- **Independent use · unknown:** Reviewed official examples, the current support sample and bounded live web findings. Independent first-hand reproduction of this exact creative workflow was not established; author demonstrations are not treated as independent evidence.
- **Models, services and costs · documented:** Apache-2.0 code. The attempted current Hugging Face model README returned 404, so checkpoint/base-model licensing and access remain unresolved rather than being inferred from the code license. Local compute plus any chosen external model or service; provider access and charges are separate. [Source](https://github.com/anniedoris/CAD-Coder/blob/main/README.md) [Source](https://arxiv.org/abs/2505.14646) [Source](https://huggingface.co/CADCODER/CAD-Coder/tree/main)

Documentation review only; AI Media Scout did not install or run this software. The four-H100 training configuration and training-data download size are not inference minimum requirements. Geometry and manufacturability need separate validation. Open issues include evaluation and serving questions.

### How it uses AI

A vision-language model workflow that converts an object image into editable CadQuery program text and reconstructs CAD geometry from that program. [Source](https://github.com/anniedoris/CAD-Coder/blob/main/README.md) [Source](https://arxiv.org/abs/2505.14646) [Source](https://huggingface.co/CADCODER/CAD-Coder/tree/main)

### Introduction

A vision-language model workflow that converts an object image into editable CadQuery program text and reconstructs CAD geometry from that program. [Source 1](https://github.com/anniedoris/CAD-Coder/blob/main/README.md) [Source 2](https://arxiv.org/abs/2505.14646) [Source 3](https://huggingface.co/CADCODER/CAD-Coder/tree/main)

### What it is good for

Image-conditioned parametric CAD experiments and studying how generated construction code relates to the final shape. [Source 1](https://github.com/anniedoris/CAD-Coder/blob/main/README.md) [Source 2](https://arxiv.org/abs/2505.14646) [Source 3](https://huggingface.co/CADCODER/CAD-Coder/tree/main)

### Demo & examples

The paper and repository show image-to-code examples. The documented workflow is batch inference; the planned interactive chat route is not presented as available. [Source 1](https://github.com/anniedoris/CAD-Coder/blob/main/README.md) [Source 2](https://arxiv.org/abs/2505.14646) [Source 3](https://huggingface.co/CADCODER/CAD-Coder/tree/main)

### Install

Use the documented Python 3.10 llava environment for inference and a separate cad_iou environment for geometry reconstruction because their dependencies conflict. Install the project and matching training/inference dependencies, obtain the model and test inputs, then run the batch evaluation script. [Source 1](https://github.com/anniedoris/CAD-Coder/blob/main/README.md) [Source 2](https://arxiv.org/abs/2505.14646) [Source 3](https://huggingface.co/CADCODER/CAD-Coder/tree/main)

1. Obtain the official source or release linked below.
2. Use the documented Python 3.10 llava environment for inference and a separate cad_iou environment for geometry reconstruction because their dependencies conflict. Install the project and matching training/inference dependencies, obtain the model and test inputs, then run the batch evaluation script.

```sh
conda create -n llava python=3.10 -y
```


```sh
conda activate llava
```


```sh
pip install -e .
```


```sh
bash scripts/v1_5/eval/test_gencadcode.sh "CADCODER/CAD-Coder" "cadquery_test_data_subset100"
```

### First project

Start with a short, representative project and inspect the result before a larger batch. [Source 1](https://github.com/anniedoris/CAD-Coder/blob/main/README.md) [Source 2](https://arxiv.org/abs/2505.14646) [Source 3](https://huggingface.co/CADCODER/CAD-Coder/tree/main)

1. Prepare the documented image test-data subset and model checkpoint.
2. Generate CadQuery program outputs using the evaluation script.
3. In the separate geometry environment, reconstruct models with scripts/generate_model_cad.py and inspect the STEP geometry before editing or fabrication.
### Hardware & software

Requirements below are documented for this workflow. Unspecified limits are not inferred. [Source 1](https://github.com/anniedoris/CAD-Coder/blob/main/README.md) [Source 2](https://arxiv.org/abs/2505.14646) [Source 3](https://huggingface.co/CADCODER/CAD-Coder/tree/main)

- **Hardware:** Inference RAM, VRAM and total disk minimum are not documented in the reviewed guide. Published training hardware is not a minimum for inference.
- **Software:** Python 3.10, LLaVA-derived inference dependencies and a separate CadQuery environment. Flash-attention wheels must match the documented Linux/CUDA/PyTorch stack.
- **Platforms:** The documented workflow targets a CUDA/Linux software stack. Native Windows/macOS support is not confirmed.

### License, model weights & costs

The full software license was reviewed. Model weights, assets and services remain separate. [Source 1](https://github.com/anniedoris/CAD-Coder/blob/main/LICENSE) [Source 2](https://github.com/anniedoris/CAD-Coder/blob/main/README.md) [Source 3](https://arxiv.org/abs/2505.14646) [Source 4](https://huggingface.co/CADCODER/CAD-Coder/tree/main)

- **Code:** Apache-2.0
- **Weights:** Apache-2.0 code. The attempted current Hugging Face model README returned 404, so checkpoint/base-model licensing and access remain unresolved rather than being inferred from the code license.
- **Commercial:** Software use follows Apache-2.0. Apache-2.0 code. The attempted current Hugging Face model README returned 404, so checkpoint/base-model licensing and access remain unresolved rather than being inferred from the code license.
- **Cost:** Local compute plus any chosen external model or service; provider access and charges are separate.

### Why it merits attention

Included for the documented creative workflow. A complete guide and popularity do not establish output reliability. [Source 1](https://github.com/anniedoris/CAD-Coder/blob/main/README.md) [Source 2](https://arxiv.org/abs/2505.14646) [Source 3](https://huggingface.co/CADCODER/CAD-Coder/tree/main)

### Limitations

The four-H100 training configuration and training-data download size are not inference minimum requirements. Geometry and manufacturability need separate validation. Open issues include evaluation and serving questions. [Source 1](https://github.com/anniedoris/CAD-Coder/blob/main/README.md) [Source 2](https://arxiv.org/abs/2505.14646) [Source 3](https://huggingface.co/CADCODER/CAD-Coder/tree/main)

### Get the tool

- [Repository](https://github.com/anniedoris/CAD-Coder)
- [Documentation](https://github.com/anniedoris/CAD-Coder/blob/main/README.md)

## FastGS

3D, reconstruction & assets · Spatial audio & volumetric media · Photogrammetry, scanning & neural rendering

First complete guide for an earlier screened library entry, with installation, first-use, requirements and six-check evidence review. This is fuller coverage, not a claim of a new launch today.

### Quality assessment: Quality unverified

Software licensing and a concrete creative AI use are supported. The remaining checks do not establish a recommendation.

Scope: Creating navigable scene captures and comparing fast training configurations for spatial media.

Evidence checked: 2026-10-27. No local execution implied.

- **Open-source software license · verified:** The complete root software license was read and archived. The grant covers this project code; unresolved model, service and asset terms are disclosed separately. [Source](https://github.com/fastgs/FastGS/blob/main/LICENSE)
- **Creative results · documented:** The official project page, paper and repository show reconstruction results and training benchmarks. These are author results; the optional dynamic branch has a current issue about treating scenes as static. [Source](https://github.com/fastgs/FastGS/blob/main/README.md) [Source](https://fastgs.github.io/) [Source](https://arxiv.org/abs/2511.04283)
- **Reproducible setup · documented:** Clone with submodules, create the supplied Conda environment and prepare a COLMAP dataset. Start with the documented base training script, then inspect the exported splats in a compatible viewer. Independent reproduction has not been established in this review. [Source](https://github.com/fastgs/FastGS/blob/main/README.md) [Source](https://fastgs.github.io/) [Source](https://arxiv.org/abs/2511.04283)
- **Maintenance and support · documented:** Live review archived 10 recent commits, 0 published release records and 10 recent support/PR records. Latest sampled commit: 2026-03-03. Current sampled topics include fast-d3dgs branch still treats the scene as static; Verify evals on Papers with Code. This is documented activity, not proof of sustained support or a complete blocker survey. [Source](https://github.com/fastgs/FastGS/commits/main) [Source](https://github.com/fastgs/FastGS/issues)
- **Independent use · unknown:** Reviewed official examples, the current support sample and bounded live web findings. Independent first-hand reproduction of this exact creative workflow was not established; author demonstrations are not treated as independent evidence.
- **Models, services and costs · documented:** MIT root code; upstream 3DGS components, submodules, datasets and model artifacts retain separate terms, which can differ from MIT. Local compute plus any chosen external model or service; provider access and charges are separate. [Source](https://github.com/fastgs/FastGS/blob/main/README.md) [Source](https://fastgs.github.io/) [Source](https://arxiv.org/abs/2511.04283)

Documentation review only; AI Media Scout did not install or run this software. Paper-quality hardware is expensive and timings depend on dataset/settings. The dynamic branch is not covered by a reliable static-scene result. Reconstruction does not certify watertight fabrication geometry.

### How it uses AI

An accelerated 3D Gaussian Splatting training workflow for reconstructing view-dependent scenes from calibrated photographs. [Source](https://github.com/fastgs/FastGS/blob/main/README.md) [Source](https://fastgs.github.io/) [Source](https://arxiv.org/abs/2511.04283)

### Introduction

An accelerated 3D Gaussian Splatting training workflow for reconstructing view-dependent scenes from calibrated photographs. [Source 1](https://github.com/fastgs/FastGS/blob/main/README.md) [Source 2](https://fastgs.github.io/) [Source 3](https://arxiv.org/abs/2511.04283)

### What it is good for

Creating navigable scene captures and comparing fast training configurations for spatial media. [Source 1](https://github.com/fastgs/FastGS/blob/main/README.md) [Source 2](https://fastgs.github.io/) [Source 3](https://arxiv.org/abs/2511.04283)

### Demo & examples

The official project page, paper and repository show reconstruction results and training benchmarks. These are author results; the optional dynamic branch has a current issue about treating scenes as static. [Source 1](https://github.com/fastgs/FastGS/blob/main/README.md) [Source 2](https://fastgs.github.io/) [Source 3](https://arxiv.org/abs/2511.04283)

### Install

Clone with submodules, create the supplied Conda environment and prepare a COLMAP dataset. Start with the documented base training script, then inspect the exported splats in a compatible viewer. [Source 1](https://github.com/fastgs/FastGS/blob/main/README.md) [Source 2](https://fastgs.github.io/) [Source 3](https://arxiv.org/abs/2511.04283)

1. Obtain the official source or release linked below.
2. Clone with submodules, create the supplied Conda environment and prepare a COLMAP dataset. Start with the documented base training script, then inspect the exported splats in a compatible viewer.

```sh
git clone --recursive https://github.com/fastgs/FastGS.git
```


```sh
cd FastGS
```


```sh
conda env create --file environment.yml
```


```sh
conda activate fastgs
```


```sh
bash train_base.sh
```

### First project

Start with a short, representative project and inspect the result before a larger batch. [Source 1](https://github.com/fastgs/FastGS/blob/main/README.md) [Source 2](https://fastgs.github.io/) [Source 3](https://arxiv.org/abs/2511.04283)

1. Prepare calibrated images and the COLMAP scene expected by the training scripts.
2. Adjust dataset/output paths and train the base static scene.
3. Inspect held-out views and exported splats rather than relying solely on training speed.
### Hardware & software

Requirements below are documented for this workflow. Unspecified limits are not inferred. [Source 1](https://github.com/fastgs/FastGS/blob/main/README.md) [Source 2](https://fastgs.github.io/) [Source 3](https://arxiv.org/abs/2511.04283)

- **Hardware:** NVIDIA compute capability 7+; 24 GB VRAM is the documented paper-quality target and RTX 4090 is recommended. Minimum system RAM/disk are not stated.
- **Software:** Conda/PyTorch, a C++ compiler and CUDA 11 SDK; nvcc 11.8 and Ubuntu are described. Windows-specific compiler setup is mentioned.
- **Platforms:** CUDA/NVIDIA workflow; Ubuntu is documented and Windows build guidance exists. macOS/MPS support is not documented.

### License, model weights & costs

The full software license was reviewed. Model weights, assets and services remain separate. [Source 1](https://github.com/fastgs/FastGS/blob/main/LICENSE) [Source 2](https://github.com/fastgs/FastGS/blob/main/README.md) [Source 3](https://fastgs.github.io/) [Source 4](https://arxiv.org/abs/2511.04283)

- **Code:** MIT
- **Weights:** MIT root code; upstream 3DGS components, submodules, datasets and model artifacts retain separate terms, which can differ from MIT.
- **Commercial:** Software use follows MIT. MIT root code; upstream 3DGS components, submodules, datasets and model artifacts retain separate terms, which can differ from MIT.
- **Cost:** Local compute plus any chosen external model or service; provider access and charges are separate.

### Why it merits attention

Included for the documented creative workflow. A complete guide and popularity do not establish output reliability. [Source 1](https://github.com/fastgs/FastGS/blob/main/README.md) [Source 2](https://fastgs.github.io/) [Source 3](https://arxiv.org/abs/2511.04283)

### Limitations

Paper-quality hardware is expensive and timings depend on dataset/settings. The dynamic branch is not covered by a reliable static-scene result. Reconstruction does not certify watertight fabrication geometry. [Source 1](https://github.com/fastgs/FastGS/blob/main/README.md) [Source 2](https://fastgs.github.io/) [Source 3](https://arxiv.org/abs/2511.04283)

### Get the tool

- [Repository](https://github.com/fastgs/FastGS)
- [Documentation](https://github.com/fastgs/FastGS/blob/main/README.md)

## Svelte VRM Live

Avatars, digital humans & lip sync · Browser tools & web media · Interactive, immersive & live media

First complete guide for an earlier screened library entry, with installation, first-use, requirements and six-check evidence review. This is fuller coverage, not a claim of a new launch today.

### Quality assessment: Quality unverified

Software licensing and a concrete creative AI use are supported. The remaining checks do not establish a recommendation.

Scope: Prototyping conversational virtual characters and web-based avatar performances.

Evidence checked: 2026-10-27. No local execution implied.

- **Open-source software license · verified:** The complete root software license was read and archived. The grant covers this project code; unresolved model, service and asset terms are disclosed separately. [Source](https://github.com/dexvdev/svelte-vrm-live/blob/main/LICENSE)
- **Creative results · documented:** The repository links a showcase video and describes the chat-to-speech-to-animation chain. End-to-end behavior was not independently reproduced. [Source](https://github.com/dexvdev/svelte-vrm-live/blob/main/README.md)
- **Reproducible setup · documented:** Clone the current canonical repository, install using pnpm, configure Google Generative AI and ElevenLabs credentials in a private .env and start the development server. Independent reproduction has not been established in this review. [Source](https://github.com/dexvdev/svelte-vrm-live/blob/main/README.md)
- **Maintenance and support · documented:** Live review archived 9 recent commits, 0 published release records and 3 recent support/PR records. Latest sampled commit: 2025-08-18. The bounded support sample did not establish third-party resolution history. This is documented activity, not proof of sustained support or a complete blocker survey. [Source](https://github.com/dexvdev/svelte-vrm-live/commits/main) [Source](https://github.com/dexvdev/svelte-vrm-live/issues)
- **Independent use · unknown:** Reviewed official examples, the current support sample and bounded live web findings. Independent first-hand reproduction of this exact creative workflow was not established; author demonstrations are not treated as independent evidence.
- **Models, services and costs · documented:** AGPL-3.0 code. Google/ElevenLabs services and VRM/Mixamo assets retain their own terms and can require accounts or payment. Local compute plus any chosen external model or service; provider access and charges are separate. [Source](https://github.com/dexvdev/svelte-vrm-live/blob/main/README.md)

Documentation review only; AI Media Scout did not install or run this software. External services can change, and their latency affects interaction. A browser UI does not prove all-platform local inference; speech and language generation rely on the configured providers.

### How it uses AI

A browser VRM-avatar interface combining a generative-AI conversation service, ElevenLabs speech and phoneme-driven lip animation. [Source](https://github.com/dexvdev/svelte-vrm-live/blob/main/README.md)

### Introduction

A browser VRM-avatar interface combining a generative-AI conversation service, ElevenLabs speech and phoneme-driven lip animation. [Source 1](https://github.com/dexvdev/svelte-vrm-live/blob/main/README.md)

### What it is good for

Prototyping conversational virtual characters and web-based avatar performances. [Source 1](https://github.com/dexvdev/svelte-vrm-live/blob/main/README.md)

### Demo & examples

The repository links a showcase video and describes the chat-to-speech-to-animation chain. End-to-end behavior was not independently reproduced. [Source 1](https://github.com/dexvdev/svelte-vrm-live/blob/main/README.md)

### Install

Clone the current canonical repository, install using pnpm, configure Google Generative AI and ElevenLabs credentials in a private .env and start the development server. [Source 1](https://github.com/dexvdev/svelte-vrm-live/blob/main/README.md)

1. Obtain the official source or release linked below.
2. Clone the current canonical repository, install using pnpm, configure Google Generative AI and ElevenLabs credentials in a private .env and start the development server.

```sh
git clone https://github.com/dexvdev/svelte-vrm-live.git
```


```sh
cd svelte-vrm-live
```


```sh
pnpm install
```


```sh
pnpm dev
```

### First project

Start with a short, representative project and inspect the result before a larger batch. [Source 1](https://github.com/dexvdev/svelte-vrm-live/blob/main/README.md)

1. Provide the required model/voice service credentials and a permitted VRM asset.
2. Open the local interface and send a short character prompt.
3. Inspect speech timing, phoneme motion and animation before developing a public experience.
### Hardware & software

Requirements below are documented for this workflow. Unspecified limits are not inferred. [Source 1](https://github.com/dexvdev/svelte-vrm-live/blob/main/README.md)

- **Hardware:** Minimum system RAM, VRAM and total disk space are not documented in the reviewed instructions.
- **Software:** Node.js 18+, pnpm, Svelte/Threlte/Three.js and provider API access.
- **Platforms:** Browser frontend; a full tested operating-system matrix is not documented.

### License, model weights & costs

The full software license was reviewed. Model weights, assets and services remain separate. [Source 1](https://github.com/dexvdev/svelte-vrm-live/blob/main/LICENSE) [Source 2](https://github.com/dexvdev/svelte-vrm-live/blob/main/README.md)

- **Code:** AGPL-3.0
- **Weights:** AGPL-3.0 code. Google/ElevenLabs services and VRM/Mixamo assets retain their own terms and can require accounts or payment.
- **Commercial:** Software use follows AGPL-3.0. AGPL-3.0 code. Google/ElevenLabs services and VRM/Mixamo assets retain their own terms and can require accounts or payment.
- **Cost:** Local compute plus any chosen external model or service; provider access and charges are separate.

### Why it merits attention

Included for the documented creative workflow. A complete guide and popularity do not establish output reliability. [Source 1](https://github.com/dexvdev/svelte-vrm-live/blob/main/README.md)

### Limitations

External services can change, and their latency affects interaction. A browser UI does not prove all-platform local inference; speech and language generation rely on the configured providers. [Source 1](https://github.com/dexvdev/svelte-vrm-live/blob/main/README.md)

### Get the tool

- [Repository](https://github.com/dexvdev/svelte-vrm-live)
- [Documentation](https://github.com/dexvdev/svelte-vrm-live/blob/main/README.md)

## AirMIDI (Airwave)

Audio, music & voice · Interactive, immersive & live media · Performance, projection & stage media

First complete guide for an earlier screened library entry, with installation, first-use, requirements and six-check evidence review. This is fuller coverage, not a claim of a new launch today.

### Quality assessment: Quality unverified

Software licensing and a concrete creative AI use are supported. The remaining checks do not establish a recommendation.

Scope: Gesture-driven composition, expressive performance prototypes and interactive music installations.

Evidence checked: 2026-10-27. No local execution implied.

- **Open-source software license · verified:** The complete root software license was read and archived. The grant covers this project code; unresolved model, service and asset terms are disclosed separately. [Source](https://github.com/kesharishaurya007/Airwave/blob/main/LICENSE)
- **Creative results · documented:** The README maps pinch, hand position, depth and wrist rotation to musical controls and links archived research material. Claimed latency has not been independently measured. [Source](https://github.com/kesharishaurya007/Airwave/blob/main/README.md) [Source](https://doi.org/10.17605/OSF.IO/FTMY7)
- **Reproducible setup · documented:** Install the listed Python packages, enable an IAC Driver MIDI bus in macOS Audio MIDI Setup and run the documented test9.py entry point. Route the MIDI bus to a synthesizer or DAW. Independent reproduction has not been established in this review. [Source](https://github.com/kesharishaurya007/Airwave/blob/main/README.md) [Source](https://doi.org/10.17605/OSF.IO/FTMY7)
- **Maintenance and support · documented:** Live review archived 10 recent commits, 0 published release records and 0 recent support/PR records. Latest sampled commit: 2026-10-25. The bounded support sample did not establish third-party resolution history. This is documented activity, not proof of sustained support or a complete blocker survey. [Source](https://github.com/kesharishaurya007/Airwave/commits/main) [Source](https://github.com/kesharishaurya007/Airwave/issues)
- **Independent use · unknown:** Reviewed official examples, the current support sample and bounded live web findings. Independent first-hand reproduction of this exact creative workflow was not established; author demonstrations are not treated as independent evidence.
- **Models, services and costs · documented:** MIT project code. MediaPipe/model components and the chosen DAW/instrument have their own terms; no hosted model is required by the described workflow. Local compute plus any chosen external model or service; provider access and charges are separate. [Source](https://github.com/kesharishaurya007/Airwave/blob/main/README.md) [Source](https://doi.org/10.17605/OSF.IO/FTMY7)

Documentation review only; AI Media Scout did not install or run this software. Occlusion, lighting and camera framing can affect gesture tracking. No zero-latency or stage-reliability claim is established.

### How it uses AI

A webcam instrument that uses MediaPipe hand tracking to map gestures to MIDI notes and continuous musical controls. [Source](https://github.com/kesharishaurya007/Airwave/blob/main/README.md) [Source](https://doi.org/10.17605/OSF.IO/FTMY7)

### Introduction

A webcam instrument that uses MediaPipe hand tracking to map gestures to MIDI notes and continuous musical controls. [Source 1](https://github.com/kesharishaurya007/Airwave/blob/main/README.md) [Source 2](https://doi.org/10.17605/OSF.IO/FTMY7)

### What it is good for

Gesture-driven composition, expressive performance prototypes and interactive music installations. [Source 1](https://github.com/kesharishaurya007/Airwave/blob/main/README.md) [Source 2](https://doi.org/10.17605/OSF.IO/FTMY7)

### Demo & examples

The README maps pinch, hand position, depth and wrist rotation to musical controls and links archived research material. Claimed latency has not been independently measured. [Source 1](https://github.com/kesharishaurya007/Airwave/blob/main/README.md) [Source 2](https://doi.org/10.17605/OSF.IO/FTMY7)

### Install

Install the listed Python packages, enable an IAC Driver MIDI bus in macOS Audio MIDI Setup and run the documented test9.py entry point. Route the MIDI bus to a synthesizer or DAW. [Source 1](https://github.com/kesharishaurya007/Airwave/blob/main/README.md) [Source 2](https://doi.org/10.17605/OSF.IO/FTMY7)

1. Obtain the official source or release linked below.
2. Install the listed Python packages, enable an IAC Driver MIDI bus in macOS Audio MIDI Setup and run the documented test9.py entry point. Route the MIDI bus to a synthesizer or DAW.

```sh
pip install opencv-python mediapipe mido python-rtmidi numpy
```


```sh
python test9.py
```

### First project

Start with a short, representative project and inspect the result before a larger batch. [Source 1](https://github.com/kesharishaurya007/Airwave/blob/main/README.md) [Source 2](https://doi.org/10.17605/OSF.IO/FTMY7)

1. Set up the webcam in stable lighting and route MIDI to an instrument.
2. Try a pinch for note control, then adjust position/rotation for expression.
3. Tune the mapping while monitoring false triggers and perceived latency.
### Hardware & software

Requirements below are documented for this workflow. Unspecified limits are not inferred. [Source 1](https://github.com/kesharishaurya007/Airwave/blob/main/README.md) [Source 2](https://doi.org/10.17605/OSF.IO/FTMY7)

- **Hardware:** A webcam and suitable lighting are required; minimum CPU, RAM, VRAM and Python version are not documented.
- **Software:** Python with OpenCV, MediaPipe, mido, python-rtmidi and NumPy; an IAC MIDI bus and a receiving instrument/DAW.
- **Platforms:** Apple silicon/macOS workflow documented; Windows/Linux routing has not been verified in this review.

### License, model weights & costs

The full software license was reviewed. Model weights, assets and services remain separate. [Source 1](https://github.com/kesharishaurya007/Airwave/blob/main/LICENSE) [Source 2](https://github.com/kesharishaurya007/Airwave/blob/main/README.md) [Source 3](https://doi.org/10.17605/OSF.IO/FTMY7)

- **Code:** MIT
- **Weights:** MIT project code. MediaPipe/model components and the chosen DAW/instrument have their own terms; no hosted model is required by the described workflow.
- **Commercial:** Software use follows MIT. MIT project code. MediaPipe/model components and the chosen DAW/instrument have their own terms; no hosted model is required by the described workflow.
- **Cost:** Local compute plus any chosen external model or service; provider access and charges are separate.

### Why it merits attention

Included for the documented creative workflow. A complete guide and popularity do not establish output reliability. [Source 1](https://github.com/kesharishaurya007/Airwave/blob/main/README.md) [Source 2](https://doi.org/10.17605/OSF.IO/FTMY7)

### Limitations

Occlusion, lighting and camera framing can affect gesture tracking. No zero-latency or stage-reliability claim is established. [Source 1](https://github.com/kesharishaurya007/Airwave/blob/main/README.md) [Source 2](https://doi.org/10.17605/OSF.IO/FTMY7)

### Get the tool

- [Repository](https://github.com/kesharishaurya007/Airwave)
- [Documentation](https://github.com/kesharishaurya007/Airwave/blob/main/README.md)

## HoloLab Studio

3D, reconstruction & assets · Browser tools & web media · Neural relighting and material recovery

First complete guide for an earlier screened library entry, with installation, first-use, requirements and six-check evidence review. This is fuller coverage, not a claim of a new launch today.

### Quality assessment: Quality unverified

Software licensing and a concrete creative AI use are supported. The remaining checks do not establish a recommendation.

Scope: Interactive digital cards, layered illustration and shader-based promotional art.

Evidence checked: 2026-10-27. No local execution implied.

- **Open-source software license · verified:** The complete root software license was read and archived. The grant covers this project code; unresolved model, service and asset terms are disclosed separately. [Source](https://github.com/Elijah-Lin-Dancer/Holo-Card-Studio/blob/main/LICENSE)
- **Creative results · documented:** The official gallery and turntable examples show the layered card effect. This is a visual shader effect, not a physical holographic display. [Source](https://github.com/Elijah-Lin-Dancer/Holo-Card-Studio/blob/main/README.md) [Source](https://Elijah-Lin-Dancer.github.io/Holo-Card-Studio/)
- **Reproducible setup · documented:** Use make setup to prepare the documented Python tooling, configure an ARK API key for the image service and install Blender 4.5 for rendering. Start the local preview, then generate a card from a short sentence. Independent reproduction has not been established in this review. [Source](https://github.com/Elijah-Lin-Dancer/Holo-Card-Studio/blob/main/README.md) [Source](https://Elijah-Lin-Dancer.github.io/Holo-Card-Studio/)
- **Maintenance and support · documented:** Live review archived 10 recent commits, 0 published release records and 2 recent support/PR records. Latest sampled commit: 2026-10-14. Current sampled topics include [Remove] nonexistent-card-id; [Submission] A glowing blue whale flying above a midnight ocean. This is documented activity, not proof of sustained support or a complete blocker survey. [Source](https://github.com/Elijah-Lin-Dancer/Holo-Card-Studio/commits/main) [Source](https://github.com/Elijah-Lin-Dancer/Holo-Card-Studio/issues)
- **Independent use · unknown:** Reviewed official examples, the current support sample and bounded live web findings. Independent first-hand reproduction of this exact creative workflow was not established; author demonstrations are not treated as independent evidence.
- **Models, services and costs · documented:** The complete root license is MIT with retained upstream attribution, despite GitHub reporting NOASSERTION. Image-service terms, U2Net/model assets and generated content rights are separate. Local compute plus any chosen external model or service; provider access and charges are separate. [Source](https://github.com/Elijah-Lin-Dancer/Holo-Card-Studio/blob/main/README.md) [Source](https://Elijah-Lin-Dancer.github.io/Holo-Card-Studio/)

Documentation review only; AI Media Scout did not install or run this software. Cards depend on a hosted image service and can need manual layer correction. Physical holography and print readiness are not established.

### How it uses AI

A pipeline from a text idea through generated layered artwork, neural background removal and Blender geometry to a browser-rendered holographic-style collectible card. [Source](https://github.com/Elijah-Lin-Dancer/Holo-Card-Studio/blob/main/README.md) [Source](https://Elijah-Lin-Dancer.github.io/Holo-Card-Studio/)

### Introduction

A pipeline from a text idea through generated layered artwork, neural background removal and Blender geometry to a browser-rendered holographic-style collectible card. [Source 1](https://github.com/Elijah-Lin-Dancer/Holo-Card-Studio/blob/main/README.md) [Source 2](https://Elijah-Lin-Dancer.github.io/Holo-Card-Studio/)

### What it is good for

Interactive digital cards, layered illustration and shader-based promotional art. [Source 1](https://github.com/Elijah-Lin-Dancer/Holo-Card-Studio/blob/main/README.md) [Source 2](https://Elijah-Lin-Dancer.github.io/Holo-Card-Studio/)

### Demo & examples

The official gallery and turntable examples show the layered card effect. This is a visual shader effect, not a physical holographic display. [Source 1](https://github.com/Elijah-Lin-Dancer/Holo-Card-Studio/blob/main/README.md) [Source 2](https://Elijah-Lin-Dancer.github.io/Holo-Card-Studio/)

### Install

Use make setup to prepare the documented Python tooling, configure an ARK API key for the image service and install Blender 4.5 for rendering. Start the local preview, then generate a card from a short sentence. [Source 1](https://github.com/Elijah-Lin-Dancer/Holo-Card-Studio/blob/main/README.md) [Source 2](https://Elijah-Lin-Dancer.github.io/Holo-Card-Studio/)

1. Obtain the official source or release linked below.
2. Use make setup to prepare the documented Python tooling, configure an ARK API key for the image service and install Blender 4.5 for rendering. Start the local preview, then generate a card from a short sentence.

```sh
make setup
```


```sh
make preview
```


```sh
make card SENTENCE="A luminous garden at night" SLUG=garden
```

### First project

Start with a short, representative project and inspect the result before a larger batch. [Source 1](https://github.com/Elijah-Lin-Dancer/Holo-Card-Studio/blob/main/README.md) [Source 2](https://Elijah-Lin-Dancer.github.io/Holo-Card-Studio/)

1. Generate and review the four artwork layers.
2. Inspect background removal and card geometry in the rendering pipeline.
3. Preview the GLB/card in the local browser gallery and check shader appearance from several angles.
### Hardware & software

Requirements below are documented for this workflow. Unspecified limits are not inferred. [Source 1](https://github.com/Elijah-Lin-Dancer/Holo-Card-Studio/blob/main/README.md) [Source 2](https://Elijah-Lin-Dancer.github.io/Holo-Card-Studio/)

- **Hardware:** Minimum system RAM, VRAM and total disk space are not documented in the reviewed instructions.
- **Software:** Python project dependencies, Blender 4.5/Cycles, rembg/U2Net and Three.js 0.180; Doubao/ARK service access for the described image route.
- **Platforms:** Browser viewing is documented; the complete supported local-generation OS/version matrix is not specified.

### License, model weights & costs

The full software license was reviewed. Model weights, assets and services remain separate. [Source 1](https://github.com/Elijah-Lin-Dancer/Holo-Card-Studio/blob/main/LICENSE) [Source 2](https://github.com/Elijah-Lin-Dancer/Holo-Card-Studio/blob/main/README.md) [Source 3](https://Elijah-Lin-Dancer.github.io/Holo-Card-Studio/)

- **Code:** MIT
- **Weights:** The complete root license is MIT with retained upstream attribution, despite GitHub reporting NOASSERTION. Image-service terms, U2Net/model assets and generated content rights are separate.
- **Commercial:** Software use follows MIT. The complete root license is MIT with retained upstream attribution, despite GitHub reporting NOASSERTION. Image-service terms, U2Net/model assets and generated content rights are separate.
- **Cost:** Local compute plus any chosen external model or service; provider access and charges are separate.

### Why it merits attention

Included for the documented creative workflow. A complete guide and popularity do not establish output reliability. [Source 1](https://github.com/Elijah-Lin-Dancer/Holo-Card-Studio/blob/main/README.md) [Source 2](https://Elijah-Lin-Dancer.github.io/Holo-Card-Studio/)

### Limitations

Cards depend on a hosted image service and can need manual layer correction. Physical holography and print readiness are not established. [Source 1](https://github.com/Elijah-Lin-Dancer/Holo-Card-Studio/blob/main/README.md) [Source 2](https://Elijah-Lin-Dancer.github.io/Holo-Card-Studio/)

### Get the tool

- [Repository](https://github.com/Elijah-Lin-Dancer/Holo-Card-Studio)
- [Documentation](https://github.com/Elijah-Lin-Dancer/Holo-Card-Studio/blob/main/README.md)

## 3DCellForge / 3D Model Studio

3D, reconstruction & assets · Browser tools & web media · Interactive, immersive & live media

First complete guide for an earlier screened library entry, with installation, first-use, requirements and six-check evidence review. This is fuller coverage, not a claim of a new launch today.

### Quality assessment: Experimental

Software licensing and a concrete creative AI use are supported. The remaining checks do not establish a recommendation.

Scope: Trying image-to-3D services in a common interface and comparing resulting assets before export.

Evidence checked: 2026-10-27. No local execution implied.

Why Experimental: The current project description explicitly identifies this React/Three.js model workspace as a prototype with provider and fallback paths still being developed. https://github.com/huangserva/3DCellForge/blob/main/README.md

- **Open-source software license · verified:** The complete root software license was read and archived. The grant covers this project code; unresolved model, service and asset terms are disclosed separately. [Source](https://github.com/huangserva/3DCellForge/blob/main/LICENSE)
- **Creative results · documented:** The README links a workspace demo video and local GLB examples. Its deterministic local depth/mesh fallback is not equivalent to AI model generation. [Source](https://github.com/huangserva/3DCellForge/blob/main/README.md)
- **Reproducible setup · documented:** Install npm dependencies and start the Vite frontend. To call generation providers, configure the documented server-side keys in .env.local and start the API process separately. Independent reproduction has not been established in this review. [Source](https://github.com/huangserva/3DCellForge/blob/main/README.md)
- **Maintenance and support · documented:** Live review archived 10 recent commits, 0 published release records and 8 recent support/PR records. Latest sampled commit: 2026-05-14. Current sampled topics include sistema circulatorio; Virtual Factory for Smart Hybrid Materials with AI Optimization Layer. This is documented activity, not proof of sustained support or a complete blocker survey. [Source](https://github.com/huangserva/3DCellForge/commits/main) [Source](https://github.com/huangserva/3DCellForge/issues)
- **Independent use · unknown:** Reviewed official examples, the current support sample and bounded live web findings. Independent first-hand reproduction of this exact creative workflow was not established; author demonstrations are not treated as independent evidence.
- **Models, services and costs · documented:** MIT code. Hyper3D, Tripo, Fal/Hunyuan, optional OpenAI and local checkpoint terms are separate. Sample GLBs require their own CC0/CC-BY attribution review. Local compute plus any chosen external model or service; provider access and charges are separate. [Source](https://github.com/huangserva/3DCellForge/blob/main/README.md)

Documentation review only; AI Media Scout did not install or run this software. The current README explicitly describes a prototype. Local fallback geometry is not an AI substitute and export does not certify production topology or printability.

### How it uses AI

A React/Three.js workspace for image-conditioned 3D generation through external providers, with model inspection, queue controls and optional local Hunyuan integration. [Source](https://github.com/huangserva/3DCellForge/blob/main/README.md)

### Introduction

A React/Three.js workspace for image-conditioned 3D generation through external providers, with model inspection, queue controls and optional local Hunyuan integration. [Source 1](https://github.com/huangserva/3DCellForge/blob/main/README.md)

### What it is good for

Trying image-to-3D services in a common interface and comparing resulting assets before export. [Source 1](https://github.com/huangserva/3DCellForge/blob/main/README.md)

### Demo & examples

The README links a workspace demo video and local GLB examples. Its deterministic local depth/mesh fallback is not equivalent to AI model generation. [Source 1](https://github.com/huangserva/3DCellForge/blob/main/README.md)

### Install

Install npm dependencies and start the Vite frontend. To call generation providers, configure the documented server-side keys in .env.local and start the API process separately. [Source 1](https://github.com/huangserva/3DCellForge/blob/main/README.md)

1. Obtain the official source or release linked below.
2. Install npm dependencies and start the Vite frontend. To call generation providers, configure the documented server-side keys in .env.local and start the API process separately.

```sh
npm install
```


```sh
npm run dev
```


```sh
npm run dev:api
```

### First project

Start with a short, representative project and inspect the result before a larger batch. [Source 1](https://github.com/huangserva/3DCellForge/blob/main/README.md)

1. Select a provider and upload a permitted reference image.
2. Review the generation queue, model viewer and asset information.
3. Export a GLB and inspect geometry/materials in the target application.
### Hardware & software

Requirements below are documented for this workflow. Unspecified limits are not inferred. [Source 1](https://github.com/huangserva/3DCellForge/blob/main/README.md)

- **Hardware:** Minimum system RAM, VRAM and total disk space are not documented in the reviewed instructions.
- **Software:** React/Vite/Three.js and Node/npm; optional backend on port 8787 with provider credentials. A minimum Node version is not documented.
- **Platforms:** Browser application; a full tested local OS matrix is not documented.

### License, model weights & costs

The full software license was reviewed. Model weights, assets and services remain separate. [Source 1](https://github.com/huangserva/3DCellForge/blob/main/LICENSE) [Source 2](https://github.com/huangserva/3DCellForge/blob/main/README.md)

- **Code:** MIT
- **Weights:** MIT code. Hyper3D, Tripo, Fal/Hunyuan, optional OpenAI and local checkpoint terms are separate. Sample GLBs require their own CC0/CC-BY attribution review.
- **Commercial:** Software use follows MIT. MIT code. Hyper3D, Tripo, Fal/Hunyuan, optional OpenAI and local checkpoint terms are separate. Sample GLBs require their own CC0/CC-BY attribution review.
- **Cost:** Local compute plus any chosen external model or service; provider access and charges are separate.

### Why it merits attention

Included for the documented creative workflow. A complete guide and popularity do not establish output reliability. [Source 1](https://github.com/huangserva/3DCellForge/blob/main/README.md)

### Limitations

The current README explicitly describes a prototype. Local fallback geometry is not an AI substitute and export does not certify production topology or printability. [Source 1](https://github.com/huangserva/3DCellForge/blob/main/README.md)

### Get the tool

- [Repository](https://github.com/huangserva/3DCellForge)
- [Documentation](https://github.com/huangserva/3DCellForge/blob/main/README.md)

## Seidr-Smidja

Avatars, digital humans & lip sync · 3D, reconstruction & assets · AI agents for code-authored media production

First complete guide for an earlier screened library entry, with installation, first-use, requirements and six-check evidence review. This is fuller coverage, not a claim of a new launch today.

### Quality assessment: Quality unverified

Software licensing and a concrete creative AI use are supported. The remaining checks do not establish a recommendation.

Scope: Automating repeatable avatar edits and turning a character brief into inspectable VRM previews.

Evidence checked: 2026-10-27. No local execution implied.

- **Open-source software license · verified:** The complete root software license was read and archived. The grant covers this project code; unresolved model, service and asset terms are disclosed separately. [Source](https://github.com/hrabanazviking/Seidr-Smidja/blob/development/LICENSE)
- **Creative results · documented:** The README documents minimal-spec builds, validation and rendered-preview feedback. Reported non-Blender tests do not prove the actual Blender or VRoid host path. [Source](https://github.com/hrabanazviking/Seidr-Smidja/blob/development/README.md)
- **Reproducible setup · documented:** Use the documented development branch and Python 3.10+ environment, install editable dependencies, verify installation and bootstrap the asset hoard. Install Blender and its VRM add-on for the actual build route. Independent reproduction has not been established in this review. [Source](https://github.com/hrabanazviking/Seidr-Smidja/blob/development/README.md)
- **Maintenance and support · documented:** Live review archived 10 recent commits, 0 published release records and 0 recent support/PR records. Latest sampled commit: 2026-10-22. The bounded support sample did not establish third-party resolution history. This is documented activity, not proof of sustained support or a complete blocker survey. [Source](https://github.com/hrabanazviking/Seidr-Smidja/commits/development) [Source](https://github.com/hrabanazviking/Seidr-Smidja/issues)
- **Independent use · unknown:** Reviewed official examples, the current support sample and bounded live web findings. Independent first-hand reproduction of this exact creative workflow was not established; author demonstrations are not treated as independent evidence.
- **Models, services and costs · documented:** Apache-2.0 toolkit. Avatar/hoard assets, VRoid Studio, external agent services and any model weights retain separate permissions. Local compute plus any chosen external model or service; provider access and charges are separate. [Source](https://github.com/hrabanazviking/Seidr-Smidja/blob/development/README.md)

Documentation review only; AI Media Scout did not install or run this software. The current docs acknowledge real-host smoke checks still pending. Historical phase names and optional unfinished integrations do not by themselves label the main workflow Experimental.

### How it uses AI

An agent-oriented VRM character toolkit using structured specifications, Blender/VRM operations and rendered feedback to help a language-model agent refine avatar designs. [Source](https://github.com/hrabanazviking/Seidr-Smidja/blob/development/README.md)

### Introduction

An agent-oriented VRM character toolkit using structured specifications, Blender/VRM operations and rendered feedback to help a language-model agent refine avatar designs. [Source 1](https://github.com/hrabanazviking/Seidr-Smidja/blob/development/README.md)

### What it is good for

Automating repeatable avatar edits and turning a character brief into inspectable VRM previews. [Source 1](https://github.com/hrabanazviking/Seidr-Smidja/blob/development/README.md)

### Demo & examples

The README documents minimal-spec builds, validation and rendered-preview feedback. Reported non-Blender tests do not prove the actual Blender or VRoid host path. [Source 1](https://github.com/hrabanazviking/Seidr-Smidja/blob/development/README.md)

### Install

Use the documented development branch and Python 3.10+ environment, install editable dependencies, verify installation and bootstrap the asset hoard. Install Blender and its VRM add-on for the actual build route. [Source 1](https://github.com/hrabanazviking/Seidr-Smidja/blob/development/README.md)

1. Obtain the official source or release linked below.
2. Use the documented development branch and Python 3.10+ environment, install editable dependencies, verify installation and bootstrap the asset hoard. Install Blender and its VRM add-on for the actual build route.

```sh
pip install -e .
```


```sh
python tools/verify_install.py
```


```sh
seidr bootstrap-hoard
```


```sh
seidr build examples/spec_minimal.yaml --out ./out/
```

### First project

Start with a short, representative project and inspect the result before a larger batch. [Source 1](https://github.com/hrabanazviking/Seidr-Smidja/blob/development/README.md)

1. Write or adapt a permitted avatar specification and select licensed seed assets.
2. Build and inspect validation output and preview images.
3. Have the agent propose focused edits, then recheck the actual exported VRM in the target host.
### Hardware & software

Requirements below are documented for this workflow. Unspecified limits are not inferred. [Source 1](https://github.com/hrabanazviking/Seidr-Smidja/blob/development/README.md)

- **Hardware:** Minimum system RAM, VRAM and total disk space are not documented in the reviewed instructions.
- **Software:** Python 3.10+, Blender and the VRM add-on; CLI/MCP/REST interfaces. VRoid Studio and remote-control components are optional routes.
- **Platforms:** Headless Blender route and optional Windows/macOS VRoid automation are described; a complete validated OS matrix is not established.

### License, model weights & costs

The full software license was reviewed. Model weights, assets and services remain separate. [Source 1](https://github.com/hrabanazviking/Seidr-Smidja/blob/development/LICENSE) [Source 2](https://github.com/hrabanazviking/Seidr-Smidja/blob/development/README.md)

- **Code:** Apache-2.0
- **Weights:** Apache-2.0 toolkit. Avatar/hoard assets, VRoid Studio, external agent services and any model weights retain separate permissions.
- **Commercial:** Software use follows Apache-2.0. Apache-2.0 toolkit. Avatar/hoard assets, VRoid Studio, external agent services and any model weights retain separate permissions.
- **Cost:** Local compute plus any chosen external model or service; provider access and charges are separate.

### Why it merits attention

Included for the documented creative workflow. A complete guide and popularity do not establish output reliability. [Source 1](https://github.com/hrabanazviking/Seidr-Smidja/blob/development/README.md)

### Limitations

The current docs acknowledge real-host smoke checks still pending. Historical phase names and optional unfinished integrations do not by themselves label the main workflow Experimental. [Source 1](https://github.com/hrabanazviking/Seidr-Smidja/blob/development/README.md)

### Get the tool

- [Repository](https://github.com/hrabanazviking/Seidr-Smidja)
- [Documentation](https://github.com/hrabanazviking/Seidr-Smidja/blob/development/README.md)

## Paloan Jewelry CAD

3D printing & generative CAD · AI parametric design and jewelry · 3D, reconstruction & assets

First complete guide for an earlier screened library entry, with installation, first-use, requirements and six-check evidence review. This is fuller coverage, not a claim of a new launch today.

### Quality assessment: Quality unverified

Software licensing and a concrete creative AI use are supported. The remaining checks do not establish a recommendation.

Scope: Exploring ring and setting concepts and preparing designs for further review in Rhino or another CAD environment.

Evidence checked: 2026-10-27. No local execution implied.

- **Open-source software license · verified:** The complete root software license was read and archived. The grant covers this project code; unresolved model, service and asset terms are disclosed separately. [Source](https://github.com/rubelpublic/paloan-jewelry-cad/blob/main/LICENSE)
- **Creative results · documented:** The hosted application and README demonstrate settings, materials and model exports. Internal manufacturing checks are not a certified assessment by a jeweler or caster. [Source](https://github.com/rubelpublic/paloan-jewelry-cad/blob/main/README.md) [Source](https://rubelpublic.github.io/paloan-jewelry-cad/)
- **Reproducible setup · documented:** Open the hosted static app or serve the repository with the supplied Python server. Configure a chosen AI provider when using brief/photo interpretation; Rhino is optional for its corresponding export workflow. Independent reproduction has not been established in this review. [Source](https://github.com/rubelpublic/paloan-jewelry-cad/blob/main/README.md) [Source](https://rubelpublic.github.io/paloan-jewelry-cad/)
- **Maintenance and support · documented:** Live review archived 5 recent commits, 0 published release records and 0 recent support/PR records. Latest sampled commit: 2026-10-12. The bounded support sample did not establish third-party resolution history. This is documented activity, not proof of sustained support or a complete blocker survey. [Source](https://github.com/rubelpublic/paloan-jewelry-cad/commits/main) [Source](https://github.com/rubelpublic/paloan-jewelry-cad/issues)
- **Independent use · unknown:** Reviewed official examples, the current support sample and bounded live web findings. Independent first-hand reproduction of this exact creative workflow was not established; author demonstrations are not treated as independent evidence.
- **Models, services and costs · documented:** MIT code. Puter or optional model-provider services and Rhino have separate terms and costs; source code licensing does not cover submitted reference-image rights. Local/static viewing plus any selected AI-provider charges and optional Rhino license; README free-service language is not a permanent pricing guarantee. [Source](https://github.com/rubelpublic/paloan-jewelry-cad/blob/main/README.md) [Source](https://rubelpublic.github.io/paloan-jewelry-cad/)

Documentation review only; AI Media Scout did not install or run this software. Rhino smoke tests described in the repository use mocked APIs rather than proving execution inside Rhino. STL output and built-in checks do not establish castability, fit or strength.

### How it uses AI

A browser jewelry-design workspace with AI-assisted interpretation of photographs and design briefs into editable parametric forms, plus CAD/export helpers. [Source](https://github.com/rubelpublic/paloan-jewelry-cad/blob/main/README.md) [Source](https://rubelpublic.github.io/paloan-jewelry-cad/)

### Introduction

A browser jewelry-design workspace with AI-assisted interpretation of photographs and design briefs into editable parametric forms, plus CAD/export helpers. [Source 1](https://github.com/rubelpublic/paloan-jewelry-cad/blob/main/README.md) [Source 2](https://rubelpublic.github.io/paloan-jewelry-cad/)

### What it is good for

Exploring ring and setting concepts and preparing designs for further review in Rhino or another CAD environment. [Source 1](https://github.com/rubelpublic/paloan-jewelry-cad/blob/main/README.md) [Source 2](https://rubelpublic.github.io/paloan-jewelry-cad/)

### Demo & examples

The hosted application and README demonstrate settings, materials and model exports. Internal manufacturing checks are not a certified assessment by a jeweler or caster. [Source 1](https://github.com/rubelpublic/paloan-jewelry-cad/blob/main/README.md) [Source 2](https://rubelpublic.github.io/paloan-jewelry-cad/)

### Install

Open the hosted static app or serve the repository with the supplied Python server. Configure a chosen AI provider when using brief/photo interpretation; Rhino is optional for its corresponding export workflow. [Source 1](https://github.com/rubelpublic/paloan-jewelry-cad/blob/main/README.md) [Source 2](https://rubelpublic.github.io/paloan-jewelry-cad/)

1. Obtain the official source or release linked below.
2. Open the hosted static app or serve the repository with the supplied Python server. Configure a chosen AI provider when using brief/photo interpretation; Rhino is optional for its corresponding export workflow.

```sh
python tools/serve.py
```

### First project

Start with a short, representative project and inspect the result before a larger batch. [Source 1](https://github.com/rubelpublic/paloan-jewelry-cad/blob/main/README.md) [Source 2](https://rubelpublic.github.io/paloan-jewelry-cad/)

1. Enter a design brief or reference image through the AI route.
2. Inspect and adjust dimensions, stones, spacing and setting geometry.
3. Export Rhino Python, STL or GLB as appropriate and obtain application/manufacturing validation before fabrication.
### Hardware & software

Requirements below are documented for this workflow. Unspecified limits are not inferred. [Source 1](https://github.com/rubelpublic/paloan-jewelry-cad/blob/main/README.md) [Source 2](https://rubelpublic.github.io/paloan-jewelry-cad/)

- **Hardware:** Minimum system RAM, VRAM and total disk space are not documented in the reviewed instructions.
- **Software:** Browser/Three.js; Python 3.8+ for local tools, optional Pillow for relief work. Rhino 7/8 or Grasshopper for the documented proprietary CAD route.
- **Platforms:** Browser interface; a complete tested browser/OS matrix is not documented.

### License, model weights & costs

The full software license was reviewed. Model weights, assets and services remain separate. [Source 1](https://github.com/rubelpublic/paloan-jewelry-cad/blob/main/LICENSE) [Source 2](https://github.com/rubelpublic/paloan-jewelry-cad/blob/main/README.md) [Source 3](https://rubelpublic.github.io/paloan-jewelry-cad/)

- **Code:** MIT
- **Weights:** MIT code. Puter or optional model-provider services and Rhino have separate terms and costs; source code licensing does not cover submitted reference-image rights.
- **Commercial:** Software use follows MIT. MIT code. Puter or optional model-provider services and Rhino have separate terms and costs; source code licensing does not cover submitted reference-image rights.
- **Cost:** Local/static viewing plus any selected AI-provider charges and optional Rhino license; README free-service language is not a permanent pricing guarantee.

### Why it merits attention

Included for the documented creative workflow. A complete guide and popularity do not establish output reliability. [Source 1](https://github.com/rubelpublic/paloan-jewelry-cad/blob/main/README.md) [Source 2](https://rubelpublic.github.io/paloan-jewelry-cad/)

### Limitations

Rhino smoke tests described in the repository use mocked APIs rather than proving execution inside Rhino. STL output and built-in checks do not establish castability, fit or strength. [Source 1](https://github.com/rubelpublic/paloan-jewelry-cad/blob/main/README.md) [Source 2](https://rubelpublic.github.io/paloan-jewelry-cad/)

### Get the tool

- [Repository](https://github.com/rubelpublic/paloan-jewelry-cad)
- [Documentation](https://github.com/rubelpublic/paloan-jewelry-cad/blob/main/README.md)

## Champa Vision RAG

Archives, media restoration & collections · Creative learning & authoring · Physical, robotic & kinetic installations

First complete guide for an earlier screened library entry, with installation, first-use, requirements and six-check evidence review. This is fuller coverage, not a claim of a new launch today.

### Quality assessment: Quality unverified

Software licensing and a concrete creative AI use are supported. The remaining checks do not establish a recommendation.

Scope: Prototyping museum interpretation, visual artifact lookup and educational audio guides.

Evidence checked: 2026-10-27. No local execution implied.

- **Open-source software license · verified:** The complete root software license was read and archived. The grant covers this project code; unresolved model, service and asset terms are disclosed separately. [Source](https://github.com/thanhnhan04/champa-vision-rag/blob/main/LICENSE)
- **Creative results · documented:** The Vietnamese README provides artifact examples, retrieval comparisons and a Streamlit workflow. Narrow author benchmarks do not establish zero hallucination or museum-level factual accuracy. [Source](https://github.com/thanhnhan04/champa-vision-rag/blob/main/README.md)
- **Reproducible setup · documented:** Create a Python 3.10 or 3.11 environment, install requirements and start the Streamlit application. Fetch the documented embedding/voice assets and preserve their separate notices. Independent reproduction has not been established in this review. [Source](https://github.com/thanhnhan04/champa-vision-rag/blob/main/README.md)
- **Maintenance and support · documented:** Live review archived 4 recent commits, 0 published release records and 0 recent support/PR records. Latest sampled commit: 2026-10-21. The bounded support sample did not establish third-party resolution history. This is documented activity, not proof of sustained support or a complete blocker survey. [Source](https://github.com/thanhnhan04/champa-vision-rag/commits/main) [Source](https://github.com/thanhnhan04/champa-vision-rag/issues)
- **Independent use · unknown:** Reviewed official examples, the current support sample and bounded live web findings. Independent first-hand reproduction of this exact creative workflow was not established; author demonstrations are not treated as independent evidence.
- **Models, services and costs · documented:** MIT application code. Piper/MMS voice models, image datasets and heritage-source material retain separate terms; MMS can have non-commercial restrictions, and image attributions must be retained. Local compute plus any chosen external model or service; provider access and charges are separate. [Source](https://github.com/thanhnhan04/champa-vision-rag/blob/main/README.md)

Documentation review only; AI Media Scout did not install or run this software. The collection is narrow and visually similar artifacts can be confused. Historical claims require source checking; model and dataset rights are not automatically covered by MIT.

### How it uses AI

A visual heritage assistant combining CLIP/DINOv2/SigLIP image retrieval with a curated Champa artifact knowledge base and optional Vietnamese speech output. [Source](https://github.com/thanhnhan04/champa-vision-rag/blob/main/README.md)

### Introduction

A visual heritage assistant combining CLIP/DINOv2/SigLIP image retrieval with a curated Champa artifact knowledge base and optional Vietnamese speech output. [Source 1](https://github.com/thanhnhan04/champa-vision-rag/blob/main/README.md)

### What it is good for

Prototyping museum interpretation, visual artifact lookup and educational audio guides. [Source 1](https://github.com/thanhnhan04/champa-vision-rag/blob/main/README.md)

### Demo & examples

The Vietnamese README provides artifact examples, retrieval comparisons and a Streamlit workflow. Narrow author benchmarks do not establish zero hallucination or museum-level factual accuracy. [Source 1](https://github.com/thanhnhan04/champa-vision-rag/blob/main/README.md)

### Install

Create a Python 3.10 or 3.11 environment, install requirements and start the Streamlit application. Fetch the documented embedding/voice assets and preserve their separate notices. [Source 1](https://github.com/thanhnhan04/champa-vision-rag/blob/main/README.md)

1. Obtain the official source or release linked below.
2. Create a Python 3.10 or 3.11 environment, install requirements and start the Streamlit application. Fetch the documented embedding/voice assets and preserve their separate notices.

```sh
python -m venv .venv
```


```sh
pip install -r requirements.txt
```


```sh
streamlit run app.py
```

### First project

Start with a short, representative project and inspect the result before a larger batch. [Source 1](https://github.com/thanhnhan04/champa-vision-rag/blob/main/README.md)

1. Upload a permitted artifact image and inspect the top matching references.
2. Compare retrieval variants and read the cited cultural information.
3. Review any generated text with subject expertise before using optional speech output in an exhibition.
### Hardware & software

Requirements below are documented for this workflow. Unspecified limits are not inferred. [Source 1](https://github.com/thanhnhan04/champa-vision-rag/blob/main/README.md)

- **Hardware:** 8 GB RAM is recommended; CPU execution is described. VRAM is not required for that route; total disk minimum is not documented.
- **Software:** Python 3.10/3.11, PyTorch 2+, Streamlit and model dependencies.
- **Platforms:** Windows, Linux and macOS are explicitly documented; CPU use is supported.

### License, model weights & costs

The full software license was reviewed. Model weights, assets and services remain separate. [Source 1](https://github.com/thanhnhan04/champa-vision-rag/blob/main/LICENSE) [Source 2](https://github.com/thanhnhan04/champa-vision-rag/blob/main/README.md)

- **Code:** MIT
- **Weights:** MIT application code. Piper/MMS voice models, image datasets and heritage-source material retain separate terms; MMS can have non-commercial restrictions, and image attributions must be retained.
- **Commercial:** Software use follows MIT. MIT application code. Piper/MMS voice models, image datasets and heritage-source material retain separate terms; MMS can have non-commercial restrictions, and image attributions must be retained.
- **Cost:** Local compute plus any chosen external model or service; provider access and charges are separate.

### Why it merits attention

Included for the documented creative workflow. A complete guide and popularity do not establish output reliability. [Source 1](https://github.com/thanhnhan04/champa-vision-rag/blob/main/README.md)

### Limitations

The collection is narrow and visually similar artifacts can be confused. Historical claims require source checking; model and dataset rights are not automatically covered by MIT. [Source 1](https://github.com/thanhnhan04/champa-vision-rag/blob/main/README.md)

### Get the tool

- [Repository](https://github.com/thanhnhan04/champa-vision-rag)
- [Documentation](https://github.com/thanhnhan04/champa-vision-rag/blob/main/README.md)

## G1 Dance Pipeline

AI choreography and dance composition · AI robotic painting and drawing · Performance, projection & stage media

First complete guide for an earlier screened library entry, with installation, first-use, requirements and six-check evidence review. This is fuller coverage, not a claim of a new launch today.

### Quality assessment: Quality unverified

Software licensing and a concrete creative AI use are supported. The remaining checks do not establish a recommendation.

Scope: Studying embodied choreography and comparing motion retargeting, learned control and simulated performance.

Evidence checked: 2026-10-27. No local execution implied.

- **Open-source software license · verified:** The complete root software license was read and archived. The grant covers this project code; unresolved model, service and asset terms are disclosed separately. [Source](https://github.com/guoshuhao066-code/g1-dance-pipeline/blob/main/LICENSE)
- **Creative results · documented:** The README shows original motion, retargeted motion, trained policy and MuJoCo simulation clips. The author explicitly suspended further hardware validation; simulations do not establish safe physical performance. [Source](https://github.com/guoshuhao066-code/g1-dance-pipeline/blob/main/README.md)
- **Reproducible setup · documented:** Clone recursively, configure the documented pipeline environment and run its bootstrap and doctor commands on a suitable simulation workstation. Start with the documented CMU BVH example in simulation. Independent reproduction has not been established in this review. [Source](https://github.com/guoshuhao066-code/g1-dance-pipeline/blob/main/README.md)
- **Maintenance and support · documented:** Live review archived 5 recent commits, 0 published release records and 0 recent support/PR records. Latest sampled commit: 2026-07-26. The bounded support sample did not establish third-party resolution history. This is documented activity, not proof of sustained support or a complete blocker survey. [Source](https://github.com/guoshuhao066-code/g1-dance-pipeline/commits/main) [Source](https://github.com/guoshuhao066-code/g1-dance-pipeline/issues)
- **Independent use · unknown:** Reviewed official examples, the current support sample and bounded live web findings. Independent first-hand reproduction of this exact creative workflow was not established; author demonstrations are not treated as independent evidence.
- **Models, services and costs · documented:** Apache-2.0 project code. CMU/SMPL-X motion and body assets, simulation software and robot SDKs retain their own terms. Local compute plus any chosen external model or service; provider access and charges are separate. [Source](https://github.com/guoshuhao066-code/g1-dance-pipeline/blob/main/README.md)

Documentation review only; AI Media Scout did not install or run this software. Training, retargeting and hardware behavior are different validation stages. The robot variant is G1 EDU 29-DoF; an animation clip is not proof of physical safety or portability.

### How it uses AI

A human-motion-to-robot pipeline combining retargeting with learned control policies to reproduce dance motion on a Unitree G1 simulation and a separately validated hardware route. [Source](https://github.com/guoshuhao066-code/g1-dance-pipeline/blob/main/README.md)

### Introduction

A human-motion-to-robot pipeline combining retargeting with learned control policies to reproduce dance motion on a Unitree G1 simulation and a separately validated hardware route. [Source 1](https://github.com/guoshuhao066-code/g1-dance-pipeline/blob/main/README.md)

### What it is good for

Studying embodied choreography and comparing motion retargeting, learned control and simulated performance. [Source 1](https://github.com/guoshuhao066-code/g1-dance-pipeline/blob/main/README.md)

### Demo & examples

The README shows original motion, retargeted motion, trained policy and MuJoCo simulation clips. The author explicitly suspended further hardware validation; simulations do not establish safe physical performance. [Source 1](https://github.com/guoshuhao066-code/g1-dance-pipeline/blob/main/README.md)

### Install

Clone recursively, configure the documented pipeline environment and run its bootstrap and doctor commands on a suitable simulation workstation. Start with the documented CMU BVH example in simulation. [Source 1](https://github.com/guoshuhao066-code/g1-dance-pipeline/blob/main/README.md)

1. Obtain the official source or release linked below.
2. Clone recursively, configure the documented pipeline environment and run its bootstrap and doctor commands on a suitable simulation workstation. Start with the documented CMU BVH example in simulation.

```sh
git clone --recursive https://github.com/guoshuhao066-code/g1-dance-pipeline.git
```


```sh
cd g1-dance-pipeline
```


```sh
./pipeline.sh bootstrap
```


```sh
./pipeline.sh doctor
```

### First project

Start with a short, representative project and inspect the result before a larger batch. [Source 1](https://github.com/guoshuhao066-code/g1-dance-pipeline/blob/main/README.md)

1. Prepare licensed motion data and inspect the retargeted G1 trajectory.
2. Use the documented Isaac Lab training/export route and evaluate the ONNX policy in MuJoCo.
3. Treat deployment to a physical robot as a separate supervised engineering step, not a consequence of successful simulation.
### Hardware & software

Requirements below are documented for this workflow. Unspecified limits are not inferred. [Source 1](https://github.com/guoshuhao066-code/g1-dance-pipeline/blob/main/README.md)

- **Hardware:** A suitable simulation/training GPU and, only for physical deployment, the specified G1 EDU robot are needed. Minimum RAM, VRAM and disk are not documented in the reviewed README.
- **Software:** GMR, Isaac Lab, MuJoCo, ONNX and the project’s configured environments; refer to the repository environment/provenance docs for pinned components.
- **Platforms:** The documented simulation stack is the supported route; a complete macOS/Windows/Linux compatibility matrix is not given in the README.

### License, model weights & costs

The full software license was reviewed. Model weights, assets and services remain separate. [Source 1](https://github.com/guoshuhao066-code/g1-dance-pipeline/blob/main/LICENSE) [Source 2](https://github.com/guoshuhao066-code/g1-dance-pipeline/blob/main/README.md)

- **Code:** Apache-2.0
- **Weights:** Apache-2.0 project code. CMU/SMPL-X motion and body assets, simulation software and robot SDKs retain their own terms.
- **Commercial:** Software use follows Apache-2.0. Apache-2.0 project code. CMU/SMPL-X motion and body assets, simulation software and robot SDKs retain their own terms.
- **Cost:** Local compute plus any chosen external model or service; provider access and charges are separate.

### Why it merits attention

Included for the documented creative workflow. A complete guide and popularity do not establish output reliability. [Source 1](https://github.com/guoshuhao066-code/g1-dance-pipeline/blob/main/README.md)

### Limitations

Training, retargeting and hardware behavior are different validation stages. The robot variant is G1 EDU 29-DoF; an animation clip is not proof of physical safety or portability. [Source 1](https://github.com/guoshuhao066-code/g1-dance-pipeline/blob/main/README.md)

### Get the tool

- [Repository](https://github.com/guoshuhao066-code/g1-dance-pipeline)
- [Documentation](https://github.com/guoshuhao066-code/g1-dance-pipeline/blob/main/README.md)

## 4D Gaussian Splatting Volumetric Capture

Photogrammetry, scanning & neural rendering · Spatial audio & volumetric media · Video, animation & film

First complete guide for an earlier screened library entry, with installation, first-use, requirements and six-check evidence review. This is fuller coverage, not a claim of a new launch today.

### Quality assessment: Quality unverified

Software licensing and a concrete creative AI use are supported. The remaining checks do not establish a recommendation.

Scope: Building a volumetric-capture or VFX research workflow with traceable intermediate files and storage accounting.

Evidence checked: 2026-10-27. No local execution implied.

- **Open-source software license · verified:** The complete root software license was read and archived. The grant covers this project code; unresolved model, service and asset terms are disclosed separately. [Source](https://github.com/backblaze-b2-samples/4d-gaussian-splatting-volumetric-capture/blob/main/LICENSE)
- **Creative results · documented:** The README shows session dashboards, multi-view contact sheets and stage status. Non-CUDA demonstrations explicitly skip training; a staged dataset is not a completed neural reconstruction. [Source](https://github.com/backblaze-b2-samples/4d-gaussian-splatting-volumetric-capture/blob/main/README.md)
- **Reproducible setup · documented:** Clone the repository, run pnpm run setup, add private B2 credentials to the local environment file and start pnpm dev. Install the separate 4DGaussians engine only on a CUDA host when actual neural training is required. Independent reproduction has not been established in this review. [Source](https://github.com/backblaze-b2-samples/4d-gaussian-splatting-volumetric-capture/blob/main/README.md)
- **Maintenance and support · documented:** Live review archived 7 recent commits, 0 published release records and 10 recent support/PR records. Latest sampled commit: 2026-08-17. The bounded support sample did not establish third-party resolution history. This is documented activity, not proof of sustained support or a complete blocker survey. [Source](https://github.com/backblaze-b2-samples/4d-gaussian-splatting-volumetric-capture/commits/main) [Source](https://github.com/backblaze-b2-samples/4d-gaussian-splatting-volumetric-capture/issues)
- **Independent use · unknown:** Reviewed official examples, the current support sample and bounded live web findings. Independent first-hand reproduction of this exact creative workflow was not established; author demonstrations are not treated as independent evidence.
- **Models, services and costs · documented:** MIT orchestration code; upstream 4DGaussians and its CUDA submodules retain separate terms. Backblaze is a proprietary storage service, and source footage retains its own rights. Local processing/GPU compute plus Backblaze storage and transfer charges under its current service terms. [Source](https://github.com/backblaze-b2-samples/4d-gaussian-splatting-volumetric-capture/blob/main/README.md)

Documentation review only; AI Media Scout did not install or run this software. A development scaffold without managed production authentication/operations. CPU preprocessing and a cloud deployment do not prove neural training. Large intermediate files can amplify storage costs.

### How it uses AI

A multi-camera capture pipeline that prepares a 4DGaussians dataset and runs neural dynamic-scene reconstruction on CUDA, while versioning source videos and derived artifacts in Backblaze B2. [Source](https://github.com/backblaze-b2-samples/4d-gaussian-splatting-volumetric-capture/blob/main/README.md)

### Introduction

A multi-camera capture pipeline that prepares a 4DGaussians dataset and runs neural dynamic-scene reconstruction on CUDA, while versioning source videos and derived artifacts in Backblaze B2. [Source 1](https://github.com/backblaze-b2-samples/4d-gaussian-splatting-volumetric-capture/blob/main/README.md)

### What it is good for

Building a volumetric-capture or VFX research workflow with traceable intermediate files and storage accounting. [Source 1](https://github.com/backblaze-b2-samples/4d-gaussian-splatting-volumetric-capture/blob/main/README.md)

### Demo & examples

The README shows session dashboards, multi-view contact sheets and stage status. Non-CUDA demonstrations explicitly skip training; a staged dataset is not a completed neural reconstruction. [Source 1](https://github.com/backblaze-b2-samples/4d-gaussian-splatting-volumetric-capture/blob/main/README.md)

### Install

Clone the repository, run pnpm run setup, add private B2 credentials to the local environment file and start pnpm dev. Install the separate 4DGaussians engine only on a CUDA host when actual neural training is required. [Source 1](https://github.com/backblaze-b2-samples/4d-gaussian-splatting-volumetric-capture/blob/main/README.md)

1. Obtain the official source or release linked below.
2. Clone the repository, run pnpm run setup, add private B2 credentials to the local environment file and start pnpm dev. Install the separate 4DGaussians engine only on a CUDA host when actual neural training is required.

```sh
git clone https://github.com/backblaze-b2-samples/4d-gaussian-splatting-volumetric-capture.git
```


```sh
cd 4d-gaussian-splatting-volumetric-capture
```


```sh
pnpm run setup
```


```sh
pnpm dev
```

### First project

Start with a short, representative project and inspect the result before a larger batch. [Source 1](https://github.com/backblaze-b2-samples/4d-gaussian-splatting-volumetric-capture/blob/main/README.md)

1. Create a session with synchronized camera videos or the documented synthetic example.
2. Inspect frame extraction, calibration and staged multipleview data.
3. Run the separate CUDA training stage, then review held-out views and exported splats alongside storage costs.
### Hardware & software

Requirements below are documented for this workflow. Unspecified limits are not inferred. [Source 1](https://github.com/backblaze-b2-samples/4d-gaussian-splatting-volumetric-capture/blob/main/README.md)

- **Hardware:** CPU can run ingest/calibration/staging. CUDA GPU is required for training; minimum VRAM/RAM are not specified and captures/checkpoints can occupy many GB.
- **Software:** Node.js 20+, pnpm 9+, Python 3.12+, Backblaze B2 account/keys; CUDA and build dependencies for the separate neural engine.
- **Platforms:** macOS, Linux and WSL2 for local base scripts; native Windows is not supported. Actual 4D training requires CUDA and has no CPU/MPS kernels.

### License, model weights & costs

The full software license was reviewed. Model weights, assets and services remain separate. [Source 1](https://github.com/backblaze-b2-samples/4d-gaussian-splatting-volumetric-capture/blob/main/LICENSE) [Source 2](https://github.com/backblaze-b2-samples/4d-gaussian-splatting-volumetric-capture/blob/main/README.md)

- **Code:** MIT
- **Weights:** MIT orchestration code; upstream 4DGaussians and its CUDA submodules retain separate terms. Backblaze is a proprietary storage service, and source footage retains its own rights.
- **Commercial:** Software use follows MIT. MIT orchestration code; upstream 4DGaussians and its CUDA submodules retain separate terms. Backblaze is a proprietary storage service, and source footage retains its own rights.
- **Cost:** Local processing/GPU compute plus Backblaze storage and transfer charges under its current service terms.

### Why it merits attention

Included for the documented creative workflow. A complete guide and popularity do not establish output reliability. [Source 1](https://github.com/backblaze-b2-samples/4d-gaussian-splatting-volumetric-capture/blob/main/README.md)

### Limitations

A development scaffold without managed production authentication/operations. CPU preprocessing and a cloud deployment do not prove neural training. Large intermediate files can amplify storage costs. [Source 1](https://github.com/backblaze-b2-samples/4d-gaussian-splatting-volumetric-capture/blob/main/README.md)

### Get the tool

- [Repository](https://github.com/backblaze-b2-samples/4d-gaussian-splatting-volumetric-capture)
- [Documentation](https://github.com/backblaze-b2-samples/4d-gaussian-splatting-volumetric-capture/blob/main/README.md)

## BrainFLORA

AI biosignal art and neurointeractive media · Images & design · Data art & scientific visualization

First complete guide for an earlier screened library entry, with installation, first-use, requirements and six-check evidence review. This is fuller coverage, not a claim of a new launch today.

### Quality assessment: Quality unverified

Software licensing and a concrete creative AI use are supported. The remaining checks do not establish a recommendation.

Scope: Exploring research datasets for brain-to-image visualizations and concept-representation experiments relevant to biosignal art.

Evidence checked: 2026-10-27. No local execution implied.

- **Open-source software license · verified:** The complete root software license was read and archived. The grant covers this project code; unresolved model, service and asset terms are disclosed separately. [Source](https://github.com/ncclab-sustech/BrainFLORA/blob/main/LICENSE)
- **Creative results · documented:** The repository and ACM MM paper show the framework and reconstruction/captioning evaluations. This is not a validated real-time consumer EEG art interface. [Source](https://github.com/ncclab-sustech/BrainFLORA/blob/main/README.md) [Source](https://arxiv.org/abs/2507.09747) [Source](https://huggingface.co/datasets/LidongYang/BrainFLORA)
- **Reproducible setup · documented:** Clone the repository, create the provided BrainFLORA Conda environment and install it editable. Download the preprocessed datasets/checkpoints and the separately required SDXL/IP-Adapter or Shikra assets for the chosen task. Independent reproduction has not been established in this review. [Source](https://github.com/ncclab-sustech/BrainFLORA/blob/main/README.md) [Source](https://arxiv.org/abs/2507.09747) [Source](https://huggingface.co/datasets/LidongYang/BrainFLORA)
- **Maintenance and support · documented:** Live review archived 10 recent commits, 0 published release records and 6 recent support/PR records. Latest sampled commit: 2026-06-19. Current sampled topics include Question about fMRI Visualization in BrainFLORA; Questions about environment dependencies and a few possible code issues during reproduction. This is documented activity, not proof of sustained support or a complete blocker survey. [Source](https://github.com/ncclab-sustech/BrainFLORA/commits/main) [Source](https://github.com/ncclab-sustech/BrainFLORA/issues)
- **Independent use · unknown:** Reviewed official examples, the current support sample and bounded live web findings. Independent first-hand reproduction of this exact creative workflow was not established; author demonstrations are not treated as independent evidence.
- **Models, services and costs · documented:** MIT repository code. Brain datasets, THINGS images, SDXL/IP-Adapter and Shikra/base-model weights retain their separate licenses and access conditions. Local compute plus any chosen external model or service; provider access and charges are separate. [Source](https://github.com/ncclab-sustech/BrainFLORA/blob/main/README.md) [Source](https://arxiv.org/abs/2507.09747) [Source](https://huggingface.co/datasets/LidongYang/BrainFLORA)

Documentation review only; AI Media Scout did not install or run this software. Open issue evidence includes reproduction/environment questions and fMRI visualization concerns. Offline dataset evaluation does not establish live biosignal capture or generalization to a new person.

### How it uses AI

A multimodal neural-embedding framework for EEG, MEG and fMRI, with visual retrieval, SDXL/IP-Adapter image reconstruction and Shikra-based captioning workflows. [Source](https://github.com/ncclab-sustech/BrainFLORA/blob/main/README.md) [Source](https://arxiv.org/abs/2507.09747) [Source](https://huggingface.co/datasets/LidongYang/BrainFLORA)

### Introduction

A multimodal neural-embedding framework for EEG, MEG and fMRI, with visual retrieval, SDXL/IP-Adapter image reconstruction and Shikra-based captioning workflows. [Source 1](https://github.com/ncclab-sustech/BrainFLORA/blob/main/README.md) [Source 2](https://arxiv.org/abs/2507.09747) [Source 3](https://huggingface.co/datasets/LidongYang/BrainFLORA)

### What it is good for

Exploring research datasets for brain-to-image visualizations and concept-representation experiments relevant to biosignal art. [Source 1](https://github.com/ncclab-sustech/BrainFLORA/blob/main/README.md) [Source 2](https://arxiv.org/abs/2507.09747) [Source 3](https://huggingface.co/datasets/LidongYang/BrainFLORA)

### Demo & examples

The repository and ACM MM paper show the framework and reconstruction/captioning evaluations. This is not a validated real-time consumer EEG art interface. [Source 1](https://github.com/ncclab-sustech/BrainFLORA/blob/main/README.md) [Source 2](https://arxiv.org/abs/2507.09747) [Source 3](https://huggingface.co/datasets/LidongYang/BrainFLORA)

### Install

Clone the repository, create the provided BrainFLORA Conda environment and install it editable. Download the preprocessed datasets/checkpoints and the separately required SDXL/IP-Adapter or Shikra assets for the chosen task. [Source 1](https://github.com/ncclab-sustech/BrainFLORA/blob/main/README.md) [Source 2](https://arxiv.org/abs/2507.09747) [Source 3](https://huggingface.co/datasets/LidongYang/BrainFLORA)

1. Obtain the official source or release linked below.
2. Clone the repository, create the provided BrainFLORA Conda environment and install it editable. Download the preprocessed datasets/checkpoints and the separately required SDXL/IP-Adapter or Shikra assets for the chosen task.

```sh
git clone https://github.com/ncclab-sustech/BrainFLORA.git
```


```sh
cd BrainFLORA
```


```sh
conda env create -f environment.yml
```


```sh
conda activate BrainFLORA
```


```sh
pip install -e .
```

### First project

Start with a short, representative project and inspect the result before a larger batch. [Source 1](https://github.com/ncclab-sustech/BrainFLORA/blob/main/README.md) [Source 2](https://arxiv.org/abs/2507.09747) [Source 3](https://huggingface.co/datasets/LidongYang/BrainFLORA)

1. Start with the supplied visual-retrieval evaluation and documented dataset layout.
2. For reconstruction, cache the required image-model assets and use eval/FLORA_inference_reconst.py.
3. Compare generated images and metrics against the dataset references; do not interpret them as literal mind reading.
### Hardware & software

Requirements below are documented for this workflow. Unspecified limits are not inferred. [Source 1](https://github.com/ncclab-sustech/BrainFLORA/blob/main/README.md) [Source 2](https://arxiv.org/abs/2507.09747) [Source 3](https://huggingface.co/datasets/LidongYang/BrainFLORA)

- **Hardware:** Minimum VRAM, RAM and total disk are not stated. The documented full reconstruction example generates 3,100 images, which is a workload description rather than a minimum.
- **Software:** Conda/PyTorch environment, CUDA-oriented scripts and task-specific checkpoints; optional caption metrics and Shikra assets are separate.
- **Platforms:** The documented examples use cuda:0. Explicit native macOS/Windows support is not established.

### License, model weights & costs

The full software license was reviewed. Model weights, assets and services remain separate. [Source 1](https://github.com/ncclab-sustech/BrainFLORA/blob/main/LICENSE) [Source 2](https://github.com/ncclab-sustech/BrainFLORA/blob/main/README.md) [Source 3](https://arxiv.org/abs/2507.09747) [Source 4](https://huggingface.co/datasets/LidongYang/BrainFLORA)

- **Code:** MIT
- **Weights:** MIT repository code. Brain datasets, THINGS images, SDXL/IP-Adapter and Shikra/base-model weights retain their separate licenses and access conditions.
- **Commercial:** Software use follows MIT. MIT repository code. Brain datasets, THINGS images, SDXL/IP-Adapter and Shikra/base-model weights retain their separate licenses and access conditions.
- **Cost:** Local compute plus any chosen external model or service; provider access and charges are separate.

### Why it merits attention

Included for the documented creative workflow. A complete guide and popularity do not establish output reliability. [Source 1](https://github.com/ncclab-sustech/BrainFLORA/blob/main/README.md) [Source 2](https://arxiv.org/abs/2507.09747) [Source 3](https://huggingface.co/datasets/LidongYang/BrainFLORA)

### Limitations

Open issue evidence includes reproduction/environment questions and fMRI visualization concerns. Offline dataset evaluation does not establish live biosignal capture or generalization to a new person. [Source 1](https://github.com/ncclab-sustech/BrainFLORA/blob/main/README.md) [Source 2](https://arxiv.org/abs/2507.09747) [Source 3](https://huggingface.co/datasets/LidongYang/BrainFLORA)

### Get the tool

- [Repository](https://github.com/ncclab-sustech/BrainFLORA)
- [Documentation](https://github.com/ncclab-sustech/BrainFLORA/blob/main/README.md)

## Ruach Studio

Audio, music & voice · AI music notation and score recovery · Editing, captions & post-production

First complete guide for an earlier screened library entry, with installation, first-use, requirements and six-check evidence review. This is fuller coverage, not a claim of a new launch today.

### Quality assessment: Quality unverified

Software licensing and a concrete creative AI use are supported. The remaining checks do not establish a recommendation.

Scope: Iterating on AI-generated songs and moving selected material toward a music-editing workflow.

Evidence checked: 2026-10-27. No local execution implied.

- **Open-source software license · verified:** The complete root software license was read and archived. The grant covers this project code; unresolved model, service and asset terms are disclosed separately. [Source](https://github.com/igrbible/Ruach_Studio/blob/main/LICENSE)
- **Creative results · documented:** The repository links music examples, workspaces and measured comparisons. These are maintainer results; DAW integration and the Intel Arc engine are separately marked experimental/beta. [Source](https://github.com/igrbible/Ruach_Studio/blob/main/README.md) [Source](https://github.com/igrbible/Ruach_Studio/blob/main/INSTALL.md)
- **Reproducible setup · documented:** Follow INSTALL.md on Linux with NVIDIA/CUDA: create its Python environments, fetch pinned models, build the server and start the lab and studio. Pinokio is a documented Linux alternative. Windows 11 uses the separate WSL2 instructions. Independent reproduction has not been established in this review. [Source](https://github.com/igrbible/Ruach_Studio/blob/main/README.md) [Source](https://github.com/igrbible/Ruach_Studio/blob/main/INSTALL.md)
- **Maintenance and support · documented:** Live review archived 10 recent commits, 5 published release records and 2 recent support/PR records. Latest sampled commit: 2026-10-27. Current sampled topics include Vocal Stem Only Model; Feature Request: Windows Support or Pinokio Script for Ruach_Studio. This is documented activity, not proof of sustained support or a complete blocker survey. [Source](https://github.com/igrbible/Ruach_Studio/commits/main) [Source](https://github.com/igrbible/Ruach_Studio/issues)
- **Independent use · unknown:** Reviewed official examples, the current support sample and bounded live web findings. Independent first-hand reproduction of this exact creative workflow was not established; author demonstrations are not treated as independent evidence.
- **Models, services and costs · documented:** AGPL-3.0 code, declared or-later; bundled upstream components retain their notices. YuE2 checkpoint weights and several audio datasets/models are non-commercial. Published project logo/audio/artwork use CC-BY-NC-ND terms. No commercial permission is inferred for generated songs. Local compute/storage; optional OpenRouter/other services have separate fees. [Source](https://github.com/igrbible/Ruach_Studio/blob/main/README.md) [Source](https://github.com/igrbible/Ruach_Studio/blob/main/INSTALL.md)

Documentation review only; AI Media Scout did not install or run this software. Model-weight and asset restrictions are material. Optional DAW and Intel paths have documented limitations; those do not automatically label the supported NVIDIA song workflow Experimental. Independent reproduction is unresolved.

### How it uses AI

A local YuE2-based music studio for song generation, continuation, editing and refinement, with optional lyric-writing services, stem processing and cover-art tools. [Source](https://github.com/igrbible/Ruach_Studio/blob/main/README.md) [Source](https://github.com/igrbible/Ruach_Studio/blob/main/INSTALL.md)

### Introduction

A local YuE2-based music studio for song generation, continuation, editing and refinement, with optional lyric-writing services, stem processing and cover-art tools. [Source 1](https://github.com/igrbible/Ruach_Studio/blob/main/README.md) [Source 2](https://github.com/igrbible/Ruach_Studio/blob/main/INSTALL.md)

### What it is good for

Iterating on AI-generated songs and moving selected material toward a music-editing workflow. [Source 1](https://github.com/igrbible/Ruach_Studio/blob/main/README.md) [Source 2](https://github.com/igrbible/Ruach_Studio/blob/main/INSTALL.md)

### Demo & examples

The repository links music examples, workspaces and measured comparisons. These are maintainer results; DAW integration and the Intel Arc engine are separately marked experimental/beta. [Source 1](https://github.com/igrbible/Ruach_Studio/blob/main/README.md) [Source 2](https://github.com/igrbible/Ruach_Studio/blob/main/INSTALL.md)

### Install

Follow INSTALL.md on Linux with NVIDIA/CUDA: create its Python environments, fetch pinned models, build the server and start the lab and studio. Pinokio is a documented Linux alternative. Windows 11 uses the separate WSL2 instructions. [Source 1](https://github.com/igrbible/Ruach_Studio/blob/main/README.md) [Source 2](https://github.com/igrbible/Ruach_Studio/blob/main/INSTALL.md)

1. Obtain the official source or release linked below.
2. Follow INSTALL.md on Linux with NVIDIA/CUDA: create its Python environments, fetch pinned models, build the server and start the lab and studio. Pinokio is a documented Linux alternative. Windows 11 uses the separate WSL2 instructions.

```sh
git clone https://github.com/igrbible/Ruach_Studio.git
```


```sh
cd Ruach_Studio
```


```sh
./lab/install-venv.sh
```


```sh
./fetch-models.sh
```


```sh
./build.sh --server
```


```sh
./lab/start-lab.sh
```


```sh
./start.sh
```

### First project

Start with a short, representative project and inspect the result before a larger batch. [Source 1](https://github.com/igrbible/Ruach_Studio/blob/main/README.md) [Source 2](https://github.com/igrbible/Ruach_Studio/blob/main/INSTALL.md)

1. Open the local studio on port 7777 and choose a model that fits the GPU.
2. Generate a short song from a prompt/lyrics, audition variations and keep a selected take.
3. Use editing, extension or refinement carefully, and verify the rights of every selected model before commercial use.
### Hardware & software

Requirements below are documented for this workflow. Unspecified limits are not inferred. [Source 1](https://github.com/igrbible/Ruach_Studio/blob/main/README.md) [Source 2](https://github.com/igrbible/Ruach_Studio/blob/main/INSTALL.md)

- **Hardware:** 24 GB NVIDIA VRAM is documented for the full path; smaller 8–16 GB cards use Q8_0 and 6 GB can use shorter songs/smaller copies. About 33 GB base disk is stated, with model/Artist extras adding many GB; allow additional space because version-specific README totals differ. Minimum RAM is not stated.
- **Software:** Linux x86_64, CUDA toolkit 12.8, gcc/g++ 13, CMake 3.24+, Python 3.12, ffmpeg, git and curl. Optional model servers or OpenRouter for the Writer.
- **Platforms:** Ubuntu 24.04 is the documented tested host; Windows 11 via WSL2. Intel Arc/oneAPI has a beta engine route with feature limits. macOS local generation is not documented.

### License, model weights & costs

The full software license was reviewed. Model weights, assets and services remain separate. [Source 1](https://github.com/igrbible/Ruach_Studio/blob/main/LICENSE) [Source 2](https://github.com/igrbible/Ruach_Studio/blob/main/README.md) [Source 3](https://github.com/igrbible/Ruach_Studio/blob/main/INSTALL.md)

- **Code:** AGPL-3.0
- **Weights:** AGPL-3.0 code, declared or-later; bundled upstream components retain their notices. YuE2 checkpoint weights and several audio datasets/models are non-commercial. Published project logo/audio/artwork use CC-BY-NC-ND terms. No commercial permission is inferred for generated songs.
- **Commercial:** Software use follows AGPL-3.0. AGPL-3.0 code, declared or-later; bundled upstream components retain their notices. YuE2 checkpoint weights and several audio datasets/models are non-commercial. Published project logo/audio/artwork use CC-BY-NC-ND terms. No commercial permission is inferred for generated songs.
- **Cost:** Local compute/storage; optional OpenRouter/other services have separate fees.

### Why it merits attention

Included for the documented creative workflow. A complete guide and popularity do not establish output reliability. [Source 1](https://github.com/igrbible/Ruach_Studio/blob/main/README.md) [Source 2](https://github.com/igrbible/Ruach_Studio/blob/main/INSTALL.md)

### Limitations

Model-weight and asset restrictions are material. Optional DAW and Intel paths have documented limitations; those do not automatically label the supported NVIDIA song workflow Experimental. Independent reproduction is unresolved. [Source 1](https://github.com/igrbible/Ruach_Studio/blob/main/README.md) [Source 2](https://github.com/igrbible/Ruach_Studio/blob/main/INSTALL.md)

### Get the tool

- [Repository](https://github.com/igrbible/Ruach_Studio)
- [Documentation](https://github.com/igrbible/Ruach_Studio/blob/main/README.md)

## Blooming Polygons / Robo-Flower

AI robotic painting and drawing · Physical, robotic & kinetic installations · Interactive, immersive & live media

First complete guide for an earlier screened library entry, with installation, first-use, requirements and six-check evidence review. This is fuller coverage, not a claim of a new launch today.

### Quality assessment: Experimental

Software licensing and a concrete creative AI use are supported. The remaining checks do not establish a recommendation.

Scope: Building supervised experiments in responsive sculpture, embodied interaction and kinetic installation design.

Evidence checked: 2026-10-27. No local execution implied.

Why Experimental: The current documentation explicitly scopes the kinetic installation as a small six-node proof of concept, with mechanical and real-world integration work required before broader deployment. https://github.com/SamuelAlexander/robo-flower/blob/main/README.md

- **Open-source software license · verified:** The complete root software license was read and archived. The grant covers this project code; unresolved model, service and asset terms are disclosed separately. [Source](https://github.com/SamuelAlexander/robo-flower/blob/main/LICENSE)
- **Creative results · documented:** The README provides staged computer-vision, serial and Arduino/ESP32 control examples and describes a six-node proof of concept. No independent installation reliability review was established. [Source](https://github.com/SamuelAlexander/robo-flower/blob/main/README.md)
- **Reproducible setup · documented:** Create a Python environment with the documented vision/serial packages, prepare or train the hand-gesture model and configure the microcontroller sketch for the actual wiring. A separate guide covers deployment to Jetson Orin Nano. Independent reproduction has not been established in this review. [Source](https://github.com/SamuelAlexander/robo-flower/blob/main/README.md)
- **Maintenance and support · documented:** Live review archived 4 recent commits, 0 published release records and 0 recent support/PR records. Latest sampled commit: 2026-05-25. The bounded support sample did not establish third-party resolution history. This is documented activity, not proof of sustained support or a complete blocker survey. [Source](https://github.com/SamuelAlexander/robo-flower/commits/main) [Source](https://github.com/SamuelAlexander/robo-flower/issues)
- **Independent use · unknown:** Reviewed official examples, the current support sample and bounded live web findings. Independent first-hand reproduction of this exact creative workflow was not established; author demonstrations are not treated as independent evidence.
- **Models, services and costs · documented:** Apache-2.0 project code. Ultralytics/model weights, Roboflow, Colab, Arduino libraries and dataset assets retain their own licenses and service terms. Local compute plus any chosen external model or service; provider access and charges are separate. [Source](https://github.com/SamuelAlexander/robo-flower/blob/main/README.md)

Documentation review only; AI Media Scout did not install or run this software. The source describes a physical proof of concept. Gesture mistakes can move hardware unexpectedly; limit switches, wiring and pinch-point controls need actual engineering validation. It is not a turnkey venue installation.

### How it uses AI

A kinetic-sculpture project where a trained YOLOv8 hand detector sends gesture-driven serial commands to motorized flower-like structures. [Source](https://github.com/SamuelAlexander/robo-flower/blob/main/README.md)

### Introduction

A kinetic-sculpture project where a trained YOLOv8 hand detector sends gesture-driven serial commands to motorized flower-like structures. [Source 1](https://github.com/SamuelAlexander/robo-flower/blob/main/README.md)

### What it is good for

Building supervised experiments in responsive sculpture, embodied interaction and kinetic installation design. [Source 1](https://github.com/SamuelAlexander/robo-flower/blob/main/README.md)

### Demo & examples

The README provides staged computer-vision, serial and Arduino/ESP32 control examples and describes a six-node proof of concept. No independent installation reliability review was established. [Source 1](https://github.com/SamuelAlexander/robo-flower/blob/main/README.md)

### Install

Create a Python environment with the documented vision/serial packages, prepare or train the hand-gesture model and configure the microcontroller sketch for the actual wiring. A separate guide covers deployment to Jetson Orin Nano. [Source 1](https://github.com/SamuelAlexander/robo-flower/blob/main/README.md)

1. Obtain the official source or release linked below.
2. Create a Python environment with the documented vision/serial packages, prepare or train the hand-gesture model and configure the microcontroller sketch for the actual wiring. A separate guide covers deployment to Jetson Orin Nano.

```sh
python -m venv roboflower_env
```


```sh
pip install opencv-python torch ultralytics pyserial
```

### First project

Start with a short, representative project and inspect the result before a larger batch. [Source 1](https://github.com/SamuelAlexander/robo-flower/blob/main/README.md)

1. Validate camera detection without connected motors.
2. Configure serial ports, limit switches and the microcontroller’s motor mapping.
3. Test one mechanism at a time under supervision before composing the six-node interaction.
### Hardware & software

Requirements below are documented for this workflow. Unspecified limits are not inferred. [Source 1](https://github.com/SamuelAlexander/robo-flower/blob/main/README.md)

- **Hardware:** Webcam; ESP32-S3 board/carrier, six stepper motors/drivers, six limit switches and a 12 V 5 A motor supply are listed. Jetson Orin Nano is an optional deployment host. RAM/VRAM/storage minima are not given.
- **Software:** Python 3.7+ stated by the tutorial, OpenCV, PyTorch, Ultralytics, pyserial and Arduino IDE. Actual current dependency compatibility is not independently verified; the Jetson guide specifies JetPack 5.1.2.
- **Platforms:** Mac development and Jetson deployment are described; Windows environment activation is shown. This is not a complete tested platform matrix.

### License, model weights & costs

The full software license was reviewed. Model weights, assets and services remain separate. [Source 1](https://github.com/SamuelAlexander/robo-flower/blob/main/LICENSE) [Source 2](https://github.com/SamuelAlexander/robo-flower/blob/main/README.md)

- **Code:** Apache-2.0
- **Weights:** Apache-2.0 project code. Ultralytics/model weights, Roboflow, Colab, Arduino libraries and dataset assets retain their own licenses and service terms.
- **Commercial:** Software use follows Apache-2.0. Apache-2.0 project code. Ultralytics/model weights, Roboflow, Colab, Arduino libraries and dataset assets retain their own licenses and service terms.
- **Cost:** Local compute plus any chosen external model or service; provider access and charges are separate.

### Why it merits attention

Included for the documented creative workflow. A complete guide and popularity do not establish output reliability. [Source 1](https://github.com/SamuelAlexander/robo-flower/blob/main/README.md)

### Limitations

The source describes a physical proof of concept. Gesture mistakes can move hardware unexpectedly; limit switches, wiring and pinch-point controls need actual engineering validation. It is not a turnkey venue installation. [Source 1](https://github.com/SamuelAlexander/robo-flower/blob/main/README.md)

### Get the tool

- [Repository](https://github.com/SamuelAlexander/robo-flower)
- [Documentation](https://github.com/SamuelAlexander/robo-flower/blob/main/README.md)

## UL-UNAS

Audio, music & voice · Accessible media & assistive creation · AI assisted audio plugin and DSP authoring

First complete guide for an earlier screened library entry, with installation, first-use, requirements and six-check evidence review. This is fuller coverage, not a claim of a new launch today.

### Quality assessment: Quality unverified

Software licensing and a concrete creative AI use are supported. The remaining checks do not establish a recommendation.

Scope: Cleaning recorded dialogue and studying lightweight denoising blocks for real-time audio tools.

Evidence checked: 2026-10-27. No local execution implied.

- **Open-source software license · verified:** The complete root software license was read and archived. The grant covers this project code; unresolved model, service and asset terms are disclosed separately. [Source](https://github.com/Xiaobin-Rong/ul-unas/blob/main/LICENSE)
- **Creative results · documented:** The official audio-demo page and paper provide speech enhancement comparisons. Results were not independently auditioned or benchmarked in this review. [Source](https://github.com/Xiaobin-Rong/ul-unas/blob/main/README.md) [Source](https://xiaobin-rong.github.io/ul-unas_demo/) [Source](https://github.com/Xiaobin-Rong/ul-unas/blob/main/inference.py)
- **Reproducible setup · documented:** Obtain the source and supplied checkpoint, then prepare a Python/PyTorch environment with soundfile and tqdm. The repository does not publish a complete pinned installation environment. Source inspection confirms inference.py is the runnable file, correcting the README example that omits .py. Independent reproduction has not been established in this review. [Source](https://github.com/Xiaobin-Rong/ul-unas/blob/main/README.md) [Source](https://xiaobin-rong.github.io/ul-unas_demo/) [Source](https://github.com/Xiaobin-Rong/ul-unas/blob/main/inference.py)
- **Maintenance and support · documented:** Live review archived 10 recent commits, 0 published release records and 10 recent support/PR records. Latest sampled commit: 2026-06-17. Current sampled topics include how to fine-tune?; Release UL-UNAS on Hugging Face. This is documented activity, not proof of sustained support or a complete blocker survey. [Source](https://github.com/Xiaobin-Rong/ul-unas/commits/main) [Source](https://github.com/Xiaobin-Rong/ul-unas/issues)
- **Independent use · unknown:** Reviewed official examples, the current support sample and bounded live web findings. Independent first-hand reproduction of this exact creative workflow was not established; author demonstrations are not treated as independent evidence.
- **Models, services and costs · documented:** MIT software. Checkpoint and DNS dataset terms need separate confirmation; the root code license is not assumed to cover every training asset. Local compute plus any chosen external model or service; provider access and charges are separate. [Source](https://github.com/Xiaobin-Rong/ul-unas/blob/main/README.md) [Source](https://xiaobin-rong.github.io/ul-unas_demo/) [Source](https://github.com/Xiaobin-Rong/ul-unas/blob/main/inference.py)

Documentation review only; AI Media Scout did not install or run this software. The supplied script processes files, not a live microphone stream. It does not document a complete environment lock or universal audio-format/sample-rate handling. An open fine-tuning question remains.

### How it uses AI

Ultralight U-Net architectures for speech enhancement, with pretrained batch inference and a separately released streaming ONNX route. [Source](https://github.com/Xiaobin-Rong/ul-unas/blob/main/README.md) [Source](https://xiaobin-rong.github.io/ul-unas_demo/) [Source](https://github.com/Xiaobin-Rong/ul-unas/blob/main/inference.py)

### Introduction

Ultralight U-Net architectures for speech enhancement, with pretrained batch inference and a separately released streaming ONNX route. [Source 1](https://github.com/Xiaobin-Rong/ul-unas/blob/main/README.md) [Source 2](https://xiaobin-rong.github.io/ul-unas_demo/) [Source 3](https://github.com/Xiaobin-Rong/ul-unas/blob/main/inference.py)

### What it is good for

Cleaning recorded dialogue and studying lightweight denoising blocks for real-time audio tools. [Source 1](https://github.com/Xiaobin-Rong/ul-unas/blob/main/README.md) [Source 2](https://xiaobin-rong.github.io/ul-unas_demo/) [Source 3](https://github.com/Xiaobin-Rong/ul-unas/blob/main/inference.py)

### Demo & examples

The official audio-demo page and paper provide speech enhancement comparisons. Results were not independently auditioned or benchmarked in this review. [Source 1](https://github.com/Xiaobin-Rong/ul-unas/blob/main/README.md) [Source 2](https://xiaobin-rong.github.io/ul-unas_demo/) [Source 3](https://github.com/Xiaobin-Rong/ul-unas/blob/main/inference.py)

### Install

Obtain the source and supplied checkpoint, then prepare a Python/PyTorch environment with soundfile and tqdm. The repository does not publish a complete pinned installation environment. Source inspection confirms inference.py is the runnable file, correcting the README example that omits .py. [Source 1](https://github.com/Xiaobin-Rong/ul-unas/blob/main/README.md) [Source 2](https://xiaobin-rong.github.io/ul-unas_demo/) [Source 3](https://github.com/Xiaobin-Rong/ul-unas/blob/main/inference.py)

1. Obtain the official source or release linked below.
2. Obtain the source and supplied checkpoint, then prepare a Python/PyTorch environment with soundfile and tqdm. The repository does not publish a complete pinned installation environment. Source inspection confirms inference.py is the runnable file, correcting the README example that omits .py.

```sh
python inference.py --input_dir input_wavs --output_dir enhanced_wavs --device cpu
```

### First project

Start with a short, representative project and inspect the result before a larger batch. [Source 1](https://github.com/Xiaobin-Rong/ul-unas/blob/main/README.md) [Source 2](https://xiaobin-rong.github.io/ul-unas_demo/) [Source 3](https://github.com/Xiaobin-Rong/ul-unas/blob/main/inference.py)

1. Place suitable WAV files in a test input folder and retain the originals.
2. Run inference with the supplied DNS3-trained checkpoint and the chosen torch device.
3. Audition speech, residual noise and distortions; consult the separate ONNX route for streaming integration.
### Hardware & software

Requirements below are documented for this workflow. Unspecified limits are not inferred. [Source 1](https://github.com/Xiaobin-Rong/ul-unas/blob/main/README.md) [Source 2](https://xiaobin-rong.github.io/ul-unas_demo/) [Source 3](https://github.com/Xiaobin-Rong/ul-unas/blob/main/inference.py)

- **Hardware:** Minimum system RAM, VRAM and total disk space are not documented in the reviewed instructions.
- **Software:** Python, PyTorch, soundfile and tqdm are imported by the reviewed inference code; exact supported versions are not documented.
- **Platforms:** The script explicitly supports a torch device argument including CPU and cuda:0. A complete tested OS matrix is not documented.

### License, model weights & costs

The full software license was reviewed. Model weights, assets and services remain separate. [Source 1](https://github.com/Xiaobin-Rong/ul-unas/blob/main/LICENSE) [Source 2](https://github.com/Xiaobin-Rong/ul-unas/blob/main/README.md) [Source 3](https://xiaobin-rong.github.io/ul-unas_demo/) [Source 4](https://github.com/Xiaobin-Rong/ul-unas/blob/main/inference.py)

- **Code:** MIT
- **Weights:** MIT software. Checkpoint and DNS dataset terms need separate confirmation; the root code license is not assumed to cover every training asset.
- **Commercial:** Software use follows MIT. MIT software. Checkpoint and DNS dataset terms need separate confirmation; the root code license is not assumed to cover every training asset.
- **Cost:** Local compute plus any chosen external model or service; provider access and charges are separate.

### Why it merits attention

Included for the documented creative workflow. A complete guide and popularity do not establish output reliability. [Source 1](https://github.com/Xiaobin-Rong/ul-unas/blob/main/README.md) [Source 2](https://xiaobin-rong.github.io/ul-unas_demo/) [Source 3](https://github.com/Xiaobin-Rong/ul-unas/blob/main/inference.py)

### Limitations

The supplied script processes files, not a live microphone stream. It does not document a complete environment lock or universal audio-format/sample-rate handling. An open fine-tuning question remains. [Source 1](https://github.com/Xiaobin-Rong/ul-unas/blob/main/README.md) [Source 2](https://xiaobin-rong.github.io/ul-unas_demo/) [Source 3](https://github.com/Xiaobin-Rong/ul-unas/blob/main/inference.py)

### Get the tool

- [Repository](https://github.com/Xiaobin-Rong/ul-unas)
- [Documentation](https://github.com/Xiaobin-Rong/ul-unas/blob/main/README.md)

## pmndrs Denoiser

Neural denoising for real-time creative rendering · Browser tools & web media · 3D, reconstruction & assets

First full guide in this library. This is a newly reviewed discovery, not a claim that the software launched today.

### Quality assessment: Experimental

Software licensing and a concrete creative AI use are supported. The remaining checks do not establish a recommendation.

Scope: Interactive path-tracing previews, progressive render cleanup and browser-based graphics experiments.

Evidence checked: 2026-10-27. No local execution implied.

Why Experimental: The current API is explicitly alpha with breaking runtime/import changes, limited validated hardware and unfinished temporal-model support; scope is the evolving neural WebGPU integration. https://github.com/pmndrs/denoiser/blob/main/README.md https://pmndrs.github.io/denoiser/

- **Open-source software license · verified:** The complete root software license was read and archived. The grant covers this project code; unresolved model, service and asset terms are disclosed separately. [Source](https://github.com/pmndrs/denoiser/blob/main/LICENSE)
- **Creative results · documented:** The official examples show path-tracer integration, comparisons and runtime benchmarks. The README says validation has so far focused on Apple GPUs; numbers are not cross-vendor guarantees. [Source](https://github.com/pmndrs/denoiser/blob/main/README.md) [Source](https://pmndrs.github.io/denoiser/)
- **Reproducible setup · documented:** Build the repository with its Yarn workspace, then run a supplied example. Use the current package documentation for runtime/model setup: AutoRuntime is now the default and ONNX Runtime is a separate optional import. Do not assume an older npm release has this API. Independent reproduction has not been established in this review. [Source](https://github.com/pmndrs/denoiser/blob/main/README.md) [Source](https://pmndrs.github.io/denoiser/)
- **Maintenance and support · documented:** Live review archived 10 recent commits, 0 published release records and 10 recent support/PR records. Latest sampled commit: 2026-10-24. Current sampled topics include three r186: compileAsync lights back faces of transparent DoubleSide materials with the wrong normal; v2.0.0 launch checklist. This is documented activity, not proof of sustained support or a complete blocker survey. [Source](https://github.com/pmndrs/denoiser/commits/main) [Source](https://github.com/pmndrs/denoiser/issues)
- **Independent use · unknown:** Reviewed official examples, the current support sample and bounded live web findings. Independent first-hand reproduction of this exact creative workflow was not established; author demonstrations are not treated as independent evidence.
- **Models, services and costs · documented:** MIT library; Intel OIDN weights retain Apache-2.0 notices and other runtime components retain their own terms. Pretrained weights are downloaded separately. Local compute plus any chosen external model or service; provider access and charges are separate. [Source](https://github.com/pmndrs/denoiser/blob/main/README.md) [Source](https://pmndrs.github.io/denoiser/)

Documentation review only; AI Media Scout did not install or run this software. The current README explicitly marks breaking alpha API changes. OIDN 3 temporal models are planned, not implemented, and source issues include device-memory and Three.js integration concerns.

### How it uses AI

A WebGPU rendering library that runs pretrained Intel OIDN neural denoisers on path-traced images, with Three.js shared-device integrations and separate non-neural FidelityFX temporal filters. [Source](https://github.com/pmndrs/denoiser/blob/main/README.md) [Source](https://pmndrs.github.io/denoiser/)

### Introduction

A WebGPU rendering library that runs pretrained Intel OIDN neural denoisers on path-traced images, with Three.js shared-device integrations and separate non-neural FidelityFX temporal filters. [Source 1](https://github.com/pmndrs/denoiser/blob/main/README.md) [Source 2](https://pmndrs.github.io/denoiser/)

### What it is good for

Interactive path-tracing previews, progressive render cleanup and browser-based graphics experiments. [Source 1](https://github.com/pmndrs/denoiser/blob/main/README.md) [Source 2](https://pmndrs.github.io/denoiser/)

### Demo & examples

The official examples show path-tracer integration, comparisons and runtime benchmarks. The README says validation has so far focused on Apple GPUs; numbers are not cross-vendor guarantees. [Source 1](https://github.com/pmndrs/denoiser/blob/main/README.md) [Source 2](https://pmndrs.github.io/denoiser/)

### Install

Build the repository with its Yarn workspace, then run a supplied example. Use the current package documentation for runtime/model setup: AutoRuntime is now the default and ONNX Runtime is a separate optional import. Do not assume an older npm release has this API. [Source 1](https://github.com/pmndrs/denoiser/blob/main/README.md) [Source 2](https://pmndrs.github.io/denoiser/)

1. Obtain the official source or release linked below.
2. Build the repository with its Yarn workspace, then run a supplied example. Use the current package documentation for runtime/model setup: AutoRuntime is now the default and ONNX Runtime is a separate optional import. Do not assume an older npm release has this API.

```sh
corepack yarn install
```


```sh
yarn workspace denoiser build
```


```sh
yarn examples --list
```


```sh
yarn examples three-pathtracer
```

### First project

Start with a short, representative project and inspect the result before a larger batch. [Source 1](https://github.com/pmndrs/denoiser/blob/main/README.md) [Source 2](https://pmndrs.github.io/denoiser/)

1. Run a sample path-tracing scene and compare one frozen noisy frame before and after denoising.
2. When embedding, share the renderer’s GPUDevice and provide correctly encoded color/albedo/normal textures.
3. Check memory use, orientation and runtime compatibility on the actual target device.
### Hardware & software

Requirements below are documented for this workflow. Unspecified limits are not inferred. [Source 1](https://github.com/pmndrs/denoiser/blob/main/README.md) [Source 2](https://pmndrs.github.io/denoiser/)

- **Hardware:** WebGPU-capable hardware is required; minimum RAM/VRAM is not stated. Runtime-specific allocation limits must be checked, especially alongside an active path tracer.
- **Software:** WebGPU, a compatible browser, JavaScript/TypeScript and the project’s Yarn toolchain. Optional onnxruntime-web runtime uses its own model configuration.
- **Platforms:** Author validation is stated as Apple-GPU only. Linux/NVIDIA issue reports exist but do not establish broad platform support.

### License, model weights & costs

The full software license was reviewed. Model weights, assets and services remain separate. [Source 1](https://github.com/pmndrs/denoiser/blob/main/LICENSE) [Source 2](https://github.com/pmndrs/denoiser/blob/main/README.md) [Source 3](https://pmndrs.github.io/denoiser/)

- **Code:** MIT
- **Weights:** MIT library; Intel OIDN weights retain Apache-2.0 notices and other runtime components retain their own terms. Pretrained weights are downloaded separately.
- **Commercial:** Software use follows MIT. MIT library; Intel OIDN weights retain Apache-2.0 notices and other runtime components retain their own terms. Pretrained weights are downloaded separately.
- **Cost:** Local compute plus any chosen external model or service; provider access and charges are separate.

### Why it merits attention

Included for the documented creative workflow. A complete guide and popularity do not establish output reliability. [Source 1](https://github.com/pmndrs/denoiser/blob/main/README.md) [Source 2](https://pmndrs.github.io/denoiser/)

### Limitations

The current README explicitly marks breaking alpha API changes. OIDN 3 temporal models are planned, not implemented, and source issues include device-memory and Three.js integration concerns. [Source 1](https://github.com/pmndrs/denoiser/blob/main/README.md) [Source 2](https://pmndrs.github.io/denoiser/)

### Get the tool

- [Repository](https://github.com/pmndrs/denoiser)
- [Documentation](https://github.com/pmndrs/denoiser/blob/main/README.md)

## OpenFill

Images & design · Editing, captions & post-production

A recently created project receiving its first full library guide; its creation is not proof of production readiness.

### Quality assessment: Experimental

Software licensing and a concrete creative AI use are supported. The remaining checks do not establish a recommendation.

Scope: Non-destructive image editing with local diffusion/inpainting models inside an existing creative editor.

Evidence checked: 2026-10-27. No local execution implied.

Why Experimental: The current source explicitly labels both editor integrations beta, with unresolved model-output softness/prompt-adherence limits and newly introduced AMD support documented on one tested card. https://github.com/beckettharriman/openfill/blob/main/README.md https://github.com/beckettharriman/openfill/issues/3 https://github.com/beckettharriman/openfill/releases

- **Open-source software license · verified:** The complete root software license was read and archived. The grant covers this project code; unresolved model, service and asset terms are disclosed separately. [Source](https://github.com/beckettharriman/openfill/blob/main/LICENSE)
- **Creative results · documented:** The README shows a PhotoCraft editing GIF. A detailed third-party RX 7800 XT report documents functional Create/Fill/Remove/Expand tests and visual imperfections; this is bounded evidence, not certification of every model/device. [Source](https://github.com/beckettharriman/openfill/blob/main/README.md) [Source](https://github.com/beckettharriman/openfill/issues/3) [Source](https://github.com/beckettharriman/openfill/releases)
- **Reproducible setup · documented:** Use the official PhotoCraft or GIMP release ZIP. Install the plugin for the chosen editor, select or download ComfyUI, and fetch an appropriate model through its manager. Follow the platform-specific guide for Mac/AMD setup. Independent reproduction has not been established in this review. [Source](https://github.com/beckettharriman/openfill/blob/main/README.md) [Source](https://github.com/beckettharriman/openfill/issues/3) [Source](https://github.com/beckettharriman/openfill/releases)
- **Maintenance and support · documented:** Live review archived 10 recent commits, 5 published release records and 4 recent support/PR records. Latest sampled commit: 2026-10-26. Current sampled topics include Additional Models; AMD test report: RX 7800 XT on Windows — PhotoCraft 0.2.2 Create/Fill/Remove/Expand working. This is documented activity, not proof of sustained support or a complete blocker survey. [Source](https://github.com/beckettharriman/openfill/commits/main) [Source](https://github.com/beckettharriman/openfill/issues)
- **Independent use · verified:** A third-party first-hand issue report dated October 26 documents PhotoCraft 0.2.2 on an RX 7800 XT with LaMa/SD1.5, detailed inputs, functional checks and failures. Its evidence is limited to that version and workflow, not every current model/platform. [Source](https://github.com/beckettharriman/openfill/issues/3)
- **Models, services and costs · documented:** Apache-2.0 plugin. ComfyUI, the host editor and each downloaded model have separate terms. MAT and FLUX.1 Fill are identified as non-commercial model options; no model ships with the plugin. Local computation and model downloads; verify separate host and model terms. [Source](https://github.com/beckettharriman/openfill/blob/main/README.md) [Source](https://github.com/beckettharriman/openfill/issues/3) [Source](https://github.com/beckettharriman/openfill/releases)

Documentation review only; AI Media Scout did not install or run this software. Current PhotoCraft 0.2.4/GIMP 2.0.0-beta.6 paths are explicitly beta. Some operations render around 1024 pixels then upscale; SD 1.5 can ignore small/flat-region prompts, and FLUX is slow on 8 GB. The independent report tests earlier PhotoCraft plugin 0.2.2, SD1.5 and LaMa only.

### How it uses AI

A local ComfyUI-backed plugin for PhotoCraft and GIMP 3 that adds AI fill, object removal, canvas expansion and image creation as editable layers. [Source](https://github.com/beckettharriman/openfill/blob/main/README.md) [Source](https://github.com/beckettharriman/openfill/issues/3) [Source](https://github.com/beckettharriman/openfill/releases)

### Introduction

A local ComfyUI-backed plugin for PhotoCraft and GIMP 3 that adds AI fill, object removal, canvas expansion and image creation as editable layers. [Source 1](https://github.com/beckettharriman/openfill/blob/main/README.md) [Source 2](https://github.com/beckettharriman/openfill/issues/3) [Source 3](https://github.com/beckettharriman/openfill/releases)

### What it is good for

Non-destructive image editing with local diffusion/inpainting models inside an existing creative editor. [Source 1](https://github.com/beckettharriman/openfill/blob/main/README.md) [Source 2](https://github.com/beckettharriman/openfill/issues/3) [Source 3](https://github.com/beckettharriman/openfill/releases)

### Demo & examples

The README shows a PhotoCraft editing GIF. A detailed third-party RX 7800 XT report documents functional Create/Fill/Remove/Expand tests and visual imperfections; this is bounded evidence, not certification of every model/device. [Source 1](https://github.com/beckettharriman/openfill/blob/main/README.md) [Source 2](https://github.com/beckettharriman/openfill/issues/3) [Source 3](https://github.com/beckettharriman/openfill/releases)

### Install

Use the official PhotoCraft or GIMP release ZIP. Install the plugin for the chosen editor, select or download ComfyUI, and fetch an appropriate model through its manager. Follow the platform-specific guide for Mac/AMD setup. [Source 1](https://github.com/beckettharriman/openfill/blob/main/README.md) [Source 2](https://github.com/beckettharriman/openfill/issues/3) [Source 3](https://github.com/beckettharriman/openfill/releases)

1. Obtain the official source or release linked below.
2. Use the official PhotoCraft or GIMP release ZIP. Install the plugin for the chosen editor, select or download ComfyUI, and fetch an appropriate model through its manager. Follow the platform-specific guide for Mac/AMD setup.
### First project

Start with a short, representative project and inspect the result before a larger batch. [Source 1](https://github.com/beckettharriman/openfill/blob/main/README.md) [Source 2](https://github.com/beckettharriman/openfill/issues/3) [Source 3](https://github.com/beckettharriman/openfill/releases)

1. Select an image region and choose Fill or Remove; use Expand for canvas borders.
2. Choose a model whose memory requirements and license fit the project.
3. Inspect the new layer, mask, prompt adherence and edge detail; retain the original and use Undo when needed.
### Hardware & software

Requirements below are documented for this workflow. Unspecified limits are not inferred. [Source 1](https://github.com/beckettharriman/openfill/blob/main/README.md) [Source 2](https://github.com/beckettharriman/openfill/issues/3) [Source 3](https://github.com/beckettharriman/openfill/releases)

- **Hardware:** Documented model-specific VRAM: about 2 GB for LaMa removal, 4 GB SD1.5 fill, 8 GB SDXL-quality fill. Initial LaMa/DreamShaper downloads are about 0.2/2 GB; whole-system RAM/storage limits are not supplied.
- **Software:** PhotoCraft 0.12–0.16 or GIMP 3.2; Python and ComfyUI. Windows, Linux and Apple-silicon setup routes are documented.
- **Platforms:** Windows 10/11 and Linux; Apple silicon Mac support is documented. AMD RX 7000+ support has a limited RX 7800 XT user test.

### License, model weights & costs

The full software license was reviewed. Model weights, assets and services remain separate. [Source 1](https://github.com/beckettharriman/openfill/blob/main/LICENSE) [Source 2](https://github.com/beckettharriman/openfill/blob/main/README.md) [Source 3](https://github.com/beckettharriman/openfill/issues/3) [Source 4](https://github.com/beckettharriman/openfill/releases)

- **Code:** Apache-2.0
- **Weights:** Apache-2.0 plugin. ComfyUI, the host editor and each downloaded model have separate terms. MAT and FLUX.1 Fill are identified as non-commercial model options; no model ships with the plugin.
- **Commercial:** Software use follows Apache-2.0. Apache-2.0 plugin. ComfyUI, the host editor and each downloaded model have separate terms. MAT and FLUX.1 Fill are identified as non-commercial model options; no model ships with the plugin.
- **Cost:** Local computation and model downloads; verify separate host and model terms.

### Why it merits attention

Included for the documented creative workflow. A complete guide and popularity do not establish output reliability. [Source 1](https://github.com/beckettharriman/openfill/blob/main/README.md) [Source 2](https://github.com/beckettharriman/openfill/issues/3) [Source 3](https://github.com/beckettharriman/openfill/releases)

### Limitations

Current PhotoCraft 0.2.4/GIMP 2.0.0-beta.6 paths are explicitly beta. Some operations render around 1024 pixels then upscale; SD 1.5 can ignore small/flat-region prompts, and FLUX is slow on 8 GB. The independent report tests earlier PhotoCraft plugin 0.2.2, SD1.5 and LaMa only. [Source 1](https://github.com/beckettharriman/openfill/blob/main/README.md) [Source 2](https://github.com/beckettharriman/openfill/issues/3) [Source 3](https://github.com/beckettharriman/openfill/releases)

### Get the tool

- [Repository](https://github.com/beckettharriman/openfill)
- [Documentation](https://github.com/beckettharriman/openfill/blob/main/README.md)

## Audio Studio MCP 1.0

Audio, music & voice · AI Foley and sound effects · Games & production pipelines

Release 1.0.0 on October 24 adds a local browser UI with queued generation, synchronized candidate comparisons, waveform AI edits and export/library controls. This is a concrete update to the October 23 MCP-only library guide; existing MCP parameters remain compatible.

### Quality assessment: Quality unverified

Software licensing and a concrete creative AI use are supported. The remaining checks do not establish a recommendation.

Scope: Generating music beds and sound effects, comparing several takes and preparing loops or video-ready audio exports.

Evidence checked: 2026-10-27. No local execution implied.

- **Open-source software license · verified:** The complete root software license was read and archived. The grant covers this project code; unresolved model, service and asset terms are disclosed separately. [Source](https://github.com/kanaworksai-hue/audio-studio-mcp/blob/main/LICENSE)
- **Creative results · documented:** The official sample page and 1.0 screenshots show sound generation and waveform editing. The October 24 release adds a browser workflow; its audio quality has not been independently auditioned here. [Source](https://github.com/kanaworksai-hue/audio-studio-mcp/blob/main/README.md) [Source](https://github.com/kanaworksai-hue/audio-studio-mcp/releases/tag/v1.0.0) [Source](https://kanaworksai-hue.github.io/audio-studio-mcp/)
- **Reproducible setup · documented:** Use the documented Mac or Windows installer to prepare the runtime/model. Existing installations can update to 1.0 and restart the server; the release documents an added editable-install package. Start the local browser interface on port 8765. Independent reproduction has not been established in this review. [Source](https://github.com/kanaworksai-hue/audio-studio-mcp/blob/main/README.md) [Source](https://github.com/kanaworksai-hue/audio-studio-mcp/releases/tag/v1.0.0) [Source](https://kanaworksai-hue.github.io/audio-studio-mcp/)
- **Maintenance and support · documented:** Live review archived 10 recent commits, 5 published release records and 10 recent support/PR records. Latest sampled commit: 2026-10-24. Current sampled topics include Windows: process_audio with format=ogg crashes the server (0xC00000FD stack overflow in libsndfile Vorbis encoder); Fix: add validation_alias for duration_seconds parameter. This is documented activity, not proof of sustained support or a complete blocker survey. [Source](https://github.com/kanaworksai-hue/audio-studio-mcp/commits/main) [Source](https://github.com/kanaworksai-hue/audio-studio-mcp/issues)
- **Independent use · unknown:** Reviewed official examples, the current support sample and bounded live web findings. Independent first-hand reproduction of this exact creative workflow was not established; author demonstrations are not treated as independent evidence.
- **Models, services and costs · documented:** MIT source. Stable Audio 3 weights use the separate Stability AI Community License. IBM Plex Sans is SIL OFL; Kana branding is excluded from MIT. Commercial eligibility depends on the separate weight terms. Local generation after downloads; model/license eligibility and optional assistant access remain separate. [Source](https://github.com/kanaworksai-hue/audio-studio-mcp/blob/main/README.md) [Source](https://github.com/kanaworksai-hue/audio-studio-mcp/releases/tag/v1.0.0) [Source](https://kanaworksai-hue.github.io/audio-studio-mcp/)

Documentation review only; AI Media Scout did not install or run this software. This is an instrumental music/SFX workflow, not reliable intelligible singing. The browser server binds to loopback and has no login; it is not a hosted multi-user service. Model generation and listening quality remain separate checks.

### How it uses AI

A local Stable Audio 3 sound studio accessible through MCP and, in release 1.0, a shared browser interface for generation, comparison, waveform editing and export. [Source](https://github.com/kanaworksai-hue/audio-studio-mcp/blob/main/README.md) [Source](https://github.com/kanaworksai-hue/audio-studio-mcp/releases/tag/v1.0.0) [Source](https://kanaworksai-hue.github.io/audio-studio-mcp/)

### Introduction

A local Stable Audio 3 sound studio accessible through MCP and, in release 1.0, a shared browser interface for generation, comparison, waveform editing and export. [Source 1](https://github.com/kanaworksai-hue/audio-studio-mcp/blob/main/README.md) [Source 2](https://github.com/kanaworksai-hue/audio-studio-mcp/releases/tag/v1.0.0) [Source 3](https://kanaworksai-hue.github.io/audio-studio-mcp/)

### What it is good for

Generating music beds and sound effects, comparing several takes and preparing loops or video-ready audio exports. [Source 1](https://github.com/kanaworksai-hue/audio-studio-mcp/blob/main/README.md) [Source 2](https://github.com/kanaworksai-hue/audio-studio-mcp/releases/tag/v1.0.0) [Source 3](https://kanaworksai-hue.github.io/audio-studio-mcp/)

### Demo & examples

The official sample page and 1.0 screenshots show sound generation and waveform editing. The October 24 release adds a browser workflow; its audio quality has not been independently auditioned here. [Source 1](https://github.com/kanaworksai-hue/audio-studio-mcp/blob/main/README.md) [Source 2](https://github.com/kanaworksai-hue/audio-studio-mcp/releases/tag/v1.0.0) [Source 3](https://kanaworksai-hue.github.io/audio-studio-mcp/)

### Install

Use the documented Mac or Windows installer to prepare the runtime/model. Existing installations can update to 1.0 and restart the server; the release documents an added editable-install package. Start the local browser interface on port 8765. [Source 1](https://github.com/kanaworksai-hue/audio-studio-mcp/blob/main/README.md) [Source 2](https://github.com/kanaworksai-hue/audio-studio-mcp/releases/tag/v1.0.0) [Source 3](https://kanaworksai-hue.github.io/audio-studio-mcp/)

1. Obtain the official source or release linked below.
2. Use the documented Mac or Windows installer to prepare the runtime/model. Existing installations can update to 1.0 and restart the server; the release documents an added editable-install package. Start the local browser interface on port 8765.

```sh
git clone --branch v1.0.0 https://github.com/kanaworksai-hue/audio-studio-mcp.git
```


```sh
cd audio-studio-mcp
```


```sh
.venv/bin/audio-studio-mcp --web 8765
```

### First project

Start with a short, representative project and inspect the result before a larger batch. [Source 1](https://github.com/kanaworksai-hue/audio-studio-mcp/blob/main/README.md) [Source 2](https://github.com/kanaworksai-hue/audio-studio-mcp/releases/tag/v1.0.0) [Source 3](https://kanaworksai-hue.github.io/audio-studio-mcp/)

1. Complete the platform installer and required model access first.
2. Generate up to four variations in the browser and compare them at the same play position.
3. Use waveform selection for inpainting/extension, then export WAV/OGG/FLAC with suitable trim, loudness and loop settings.
### Hardware & software

Requirements below are documented for this workflow. Unspecified limits are not inferred. [Source 1](https://github.com/kanaworksai-hue/audio-studio-mcp/blob/main/README.md) [Source 2](https://github.com/kanaworksai-hue/audio-studio-mcp/releases/tag/v1.0.0) [Source 3](https://kanaworksai-hue.github.io/audio-studio-mcp/)

- **Hardware:** Mac M1+ with 16 GB RAM recommended and about 6 GB model storage; Windows NVIDIA 8 GB+ VRAM and about 14 GB for model/PyTorch documented. These are backend-specific figures.
- **Software:** Git, ffmpeg and the supplied Python environment. Windows uses .venv/Scripts/audio-studio-mcp.exe; gated model access requires accepting the upstream terms.
- **Platforms:** Apple silicon macOS and NVIDIA Windows backends are documented. Linux remains untested in the application’s support statement; Intel Mac/AMD are not supported by these installers.

### License, model weights & costs

The full software license was reviewed. Model weights, assets and services remain separate. [Source 1](https://github.com/kanaworksai-hue/audio-studio-mcp/blob/main/LICENSE) [Source 2](https://github.com/kanaworksai-hue/audio-studio-mcp/blob/main/README.md) [Source 3](https://github.com/kanaworksai-hue/audio-studio-mcp/releases/tag/v1.0.0) [Source 4](https://kanaworksai-hue.github.io/audio-studio-mcp/)

- **Code:** MIT
- **Weights:** MIT source. Stable Audio 3 weights use the separate Stability AI Community License. IBM Plex Sans is SIL OFL; Kana branding is excluded from MIT. Commercial eligibility depends on the separate weight terms.
- **Commercial:** Software use follows MIT. MIT source. Stable Audio 3 weights use the separate Stability AI Community License. IBM Plex Sans is SIL OFL; Kana branding is excluded from MIT. Commercial eligibility depends on the separate weight terms.
- **Cost:** Local generation after downloads; model/license eligibility and optional assistant access remain separate.

### Why it merits attention

Included for the documented creative workflow. A complete guide and popularity do not establish output reliability. [Source 1](https://github.com/kanaworksai-hue/audio-studio-mcp/blob/main/README.md) [Source 2](https://github.com/kanaworksai-hue/audio-studio-mcp/releases/tag/v1.0.0) [Source 3](https://kanaworksai-hue.github.io/audio-studio-mcp/)

### Limitations

This is an instrumental music/SFX workflow, not reliable intelligible singing. The browser server binds to loopback and has no login; it is not a hosted multi-user service. Model generation and listening quality remain separate checks. [Source 1](https://github.com/kanaworksai-hue/audio-studio-mcp/blob/main/README.md) [Source 2](https://github.com/kanaworksai-hue/audio-studio-mcp/releases/tag/v1.0.0) [Source 3](https://kanaworksai-hue.github.io/audio-studio-mcp/)

### Get the tool

- [Repository](https://github.com/kanaworksai-hue/audio-studio-mcp)
- [Documentation](https://github.com/kanaworksai-hue/audio-studio-mcp/blob/main/README.md)

## OpenPixels

Images & design · Photography, restoration & color · Browser tools & web media · Archives, media restoration & collections

First full guide in this library. This is a newly reviewed discovery, not a claim that the software launched today.

### Quality assessment: Quality unverified

Code licensing is verified; model-specific rights, setup reproduction and output fidelity remain incomplete.

Scope: Restoring and upscaling creative reference images, cleaning compression artifacts and preparing visual drafts without uploading photo pixels for inference.

Evidence checked: 2026-10-27. No local execution implied.

- **Open-source software license · verified:** Read the complete MIT grant, copyright notice, conditions and warranty disclaimer; alternative Apache file was archived separately. [Source](https://gitlab.com/openpixelsapp/OpenPixels/-/blob/main/LICENSE-MIT)
- **Creative results · documented:** The official site provides a before/after slider and recorded workflow. Internal sharpness/SSIM numbers describe the author’s test, not historical accuracy or independent restoration fidelity. [Source](https://gitlab.com/openpixelsapp/OpenPixels/-/blob/main/README.md) [Source](https://gitlab.com/openpixelsapp/OpenPixels/-/blob/main/MODELS.md) [Source](https://openpixels.app/)
- **Reproducible setup · documented:** Use the browser application or build apps/web from the GitLab repository. The source build needs the JavaScript/Rust toolchains and first downloads/converts models; it is more involved than opening the site. Independent local build reproduction was not established. [Source](https://gitlab.com/openpixelsapp/OpenPixels/-/blob/main/README.md) [Source](https://gitlab.com/openpixelsapp/OpenPixels/-/blob/main/MODELS.md) [Source](https://openpixels.app/)
- **Maintenance and support · documented:** Current model notes describe October 23–24 fixes, including removal of a faulty WebGPU fp16 face model and retained compatibility files. Sustained support is not independently established. [Source](https://gitlab.com/openpixelsapp/OpenPixels/-/blob/main/MODELS.md)
- **Independent use · unknown:** Primary-site and bounded web searches did not establish independent first-hand reproduction for this assessed browser workflow.
- **Models, services and costs · documented:** Models have individual BSD-3-Clause, Apache-2.0 and MIT notices in MODELS.md. GFPGAN’s upstream license also lists NVIDIA non-commercial third-party code; the manifest discusses that boundary, so commercial rights for that component are not assumed verified. [Source](https://gitlab.com/openpixelsapp/OpenPixels/-/blob/main/MODELS.md)

Source review only; not installed or run. Neural restoration and colorization can invent plausible detail. The hosted page asks for a free account to save while the README claims no account is needed, an unresolved documentation discrepancy. Native phone builds lack several browser features, and cross-compilation is not proof of Windows execution.

### How it uses AI

A browser photo enhancer using locally executed neural upscaling, restoration, matting and colorization models, with before/after comparisons and batch export. [Source](https://gitlab.com/openpixelsapp/OpenPixels/-/blob/main/README.md) [Source](https://gitlab.com/openpixelsapp/OpenPixels/-/blob/main/MODELS.md) [Source](https://openpixels.app/)

### Introduction

OpenPixels combines a Svelte browser UI, ONNX inference and Rust/WASM image operations to enhance photographs on the user’s device. [Source 1](https://gitlab.com/openpixelsapp/OpenPixels/-/blob/main/README.md) [Source 2](https://gitlab.com/openpixelsapp/OpenPixels/-/blob/main/MODELS.md) [Source 3](https://openpixels.app/)

### What it is good for

Restoring and upscaling creative reference images, cleaning compression artifacts and preparing visual drafts without uploading photo pixels for inference. [Source 1](https://gitlab.com/openpixelsapp/OpenPixels/-/blob/main/README.md) [Source 2](https://gitlab.com/openpixelsapp/OpenPixels/-/blob/main/MODELS.md) [Source 3](https://openpixels.app/)

### Demo & examples

The official site provides a before/after slider and recorded workflow. Internal sharpness/SSIM numbers describe the author’s test, not historical accuracy or independent restoration fidelity. [Source 1](https://gitlab.com/openpixelsapp/OpenPixels/-/blob/main/README.md) [Source 2](https://gitlab.com/openpixelsapp/OpenPixels/-/blob/main/MODELS.md) [Source 3](https://openpixels.app/)

### Install

Use the browser application or build apps/web from the GitLab repository. The source build needs the JavaScript/Rust toolchains and first downloads/converts models; it is more involved than opening the site. [Source 1](https://gitlab.com/openpixelsapp/OpenPixels/-/blob/main/README.md) [Source 2](https://gitlab.com/openpixelsapp/OpenPixels/-/blob/main/MODELS.md) [Source 3](https://openpixels.app/)

1. Open the official browser app and review its current account/download behavior.
2. For self-hosting, follow the repository build instructions and fetch the pinned model assets.

```sh
npm --prefix apps/web install
```


```sh
npm --prefix apps/web run build
```


```sh
npm --prefix apps/web run preview
```

### First project

Start with a copy of a small image, choose the operation and compare the output carefully. [Source 1](https://gitlab.com/openpixelsapp/OpenPixels/-/blob/main/README.md) [Source 2](https://gitlab.com/openpixelsapp/OpenPixels/-/blob/main/MODELS.md) [Source 3](https://openpixels.app/)

1. Choose a photo and an upscale/restoration/background operation.
2. Let the required model download, then inspect the before/after result.
3. Export only after checking invented detail, edge artifacts and applicable asset/model rights.
### Hardware & software

Browser and native backends have distinct capabilities; source-build requirements do not establish native runtime support. [Source 1](https://gitlab.com/openpixelsapp/OpenPixels/-/blob/main/README.md) [Source 2](https://gitlab.com/openpixelsapp/OpenPixels/-/blob/main/MODELS.md) [Source 3](https://openpixels.app/)

- **Hardware:** WebGPU acceleration when available and CPU fallback otherwise. Minimum RAM/VRAM/disk are not stated; individual model downloads range from small MB to hundreds of MB.
- **Software:** Svelte 5/Vite, Rust/WASM and onnxruntime-web for the web build; PyTorch conversion tools are used by the model-build step. Exact Node/Rust minimum versions are not specified in the reviewed README.
- **Platforms:** Browser app plus Chrome/Edge/Firefox extension paths. Native desktop/mobile builds are separate; the model manifest explicitly lists missing phone features and unproven cross-built Windows execution.

### License, model weights & costs

The complete MIT software grant was reviewed; Apache-2.0 is an alternative offered by the project. [Source 1](https://gitlab.com/openpixelsapp/OpenPixels/-/blob/main/LICENSE-MIT) [Source 2](https://gitlab.com/openpixelsapp/OpenPixels/-/blob/main/README.md) [Source 3](https://gitlab.com/openpixelsapp/OpenPixels/-/blob/main/MODELS.md) [Source 4](https://openpixels.app/)

- **Code:** MIT
- **Weights:** Models have individual BSD-3-Clause, Apache-2.0 and MIT notices in MODELS.md. GFPGAN’s upstream license also lists NVIDIA non-commercial third-party code; the manifest discusses that boundary, so commercial rights for that component are not assumed verified.
- **Commercial:** MIT software permits commercial use subject to its notice; model, brand and input-image rights remain separate.
- **Cost:** Local compute and downloads; the public site describes a free service but its save/account requirements conflict with the README.

### Why it merits attention

Included for a concrete local photo workflow and archived code license; neither a metric badge nor source availability establishes faithful restoration. [Source 1](https://gitlab.com/openpixelsapp/OpenPixels/-/blob/main/README.md) [Source 2](https://gitlab.com/openpixelsapp/OpenPixels/-/blob/main/MODELS.md) [Source 3](https://openpixels.app/)

### Limitations

Neural restoration and colorization can invent plausible detail. The hosted page asks for a free account to save while the README claims no account is needed, an unresolved documentation discrepancy. Native phone builds lack several browser features, and cross-compilation is not proof of Windows execution. [Source 1](https://gitlab.com/openpixelsapp/OpenPixels/-/blob/main/README.md) [Source 2](https://gitlab.com/openpixelsapp/OpenPixels/-/blob/main/MODELS.md) [Source 3](https://openpixels.app/)

### Get the tool

- [Repository](https://gitlab.com/openpixelsapp/OpenPixels)
- [Documentation](https://gitlab.com/openpixelsapp/OpenPixels/-/blob/main/README.md)
- [Demo](https://openpixels.app/)

## anymove

Motion capture & character animation · Games & production pipelines · 3D, reconstruction & assets

A recently created project receiving its first full library guide; its creation is not proof of production readiness.

### Quality assessment: Quality unverified

Software licensing and a concrete creative AI use are supported. The remaining checks do not establish a recommendation.

Scope: Prototyping nonhuman character gestures for game creatures with wings, tails or multiple legs, then exporting GLB animation.

Evidence checked: 2026-10-27. No local execution implied.

- **Open-source software license · verified:** The complete root software license was read and archived. The grant covers this project code; unresolved model, service and asset terms are disclosed separately. [Source](https://github.com/patch-gg/anymove/blob/main/LICENSE)
- **Creative results · documented:** The official GIF and examples release show dragon, wolf, spider and demon captures. The table reports author measurements, not independent capture accuracy. [Source](https://github.com/patch-gg/anymove/blob/main/README.md) [Source](https://github.com/patch-gg/anymove/releases/tag/examples-v1)
- **Reproducible setup · documented:** Clone the source, create a Python 3.11 environment, install the documented PyTorch CUDA wheel and requirements, and supply Blender 5.x for the full pipeline. The included joint-detection example can be fitted on CPU without Blender or model downloads. Independent reproduction has not been established in this review. [Source](https://github.com/patch-gg/anymove/blob/main/README.md) [Source](https://github.com/patch-gg/anymove/releases/tag/examples-v1)
- **Maintenance and support · documented:** Live review archived 4 recent commits, 1 published release records and 0 recent support/PR records. Latest sampled commit: 2026-10-27. The bounded support sample did not establish third-party resolution history. This is documented activity, not proof of sustained support or a complete blocker survey. [Source](https://github.com/patch-gg/anymove/commits/main) [Source](https://github.com/patch-gg/anymove/issues)
- **Independent use · unknown:** Reviewed official examples, the current support sample and bounded live web findings. Independent first-hand reproduction of this exact creative workflow was not established; author demonstrations are not treated as independent evidence.
- **Models, services and costs · documented:** Apache-2.0 project code; DINOv2 has its own Apache-2.0 terms. MiniMax H3 weights/LoRA use a separate community license, fal is a hosted service and source meshes/assets need their own rights. Local GPU compute plus fal generation charges. Author examples quote October 2026 per-clip costs; current account prices must be checked. [Source](https://github.com/patch-gg/anymove/blob/main/README.md) [Source](https://github.com/patch-gg/anymove/releases/tag/examples-v1)

Documentation review only; AI Media Scout did not install or run this software. Eight-legged walking and lying-down motions currently fail in documented examples. Rigs are placed manually; video-view timing, limb colors and ground-contact assumptions can fail. No production animation guarantee.

### How it uses AI

Turns an AI-generated front-and-side creature video into a rigged animation using a DINOv2 joint reader and a two-view 3D fitting stage. [Source](https://github.com/patch-gg/anymove/blob/main/README.md) [Source](https://github.com/patch-gg/anymove/releases/tag/examples-v1)

### Introduction

Turns an AI-generated front-and-side creature video into a rigged animation using a DINOv2 joint reader and a two-view 3D fitting stage. [Source 1](https://github.com/patch-gg/anymove/blob/main/README.md) [Source 2](https://github.com/patch-gg/anymove/releases/tag/examples-v1)

### What it is good for

Prototyping nonhuman character gestures for game creatures with wings, tails or multiple legs, then exporting GLB animation. [Source 1](https://github.com/patch-gg/anymove/blob/main/README.md) [Source 2](https://github.com/patch-gg/anymove/releases/tag/examples-v1)

### Demo & examples

The official GIF and examples release show dragon, wolf, spider and demon captures. The table reports author measurements, not independent capture accuracy. [Source 1](https://github.com/patch-gg/anymove/blob/main/README.md) [Source 2](https://github.com/patch-gg/anymove/releases/tag/examples-v1)

### Install

Clone the source, create a Python 3.11 environment, install the documented PyTorch CUDA wheel and requirements, and supply Blender 5.x for the full pipeline. The included joint-detection example can be fitted on CPU without Blender or model downloads. [Source 1](https://github.com/patch-gg/anymove/blob/main/README.md) [Source 2](https://github.com/patch-gg/anymove/releases/tag/examples-v1)

1. Obtain the official source or release linked below.
2. Clone the source, create a Python 3.11 environment, install the documented PyTorch CUDA wheel and requirements, and supply Blender 5.x for the full pipeline. The included joint-detection example can be fitted on CPU without Blender or model downloads.

```sh
python3.11 -m venv .venv
```


```sh
.venv/bin/pip install torch==2.11.0 --index-url https://download.pytorch.org/whl/cu128
```


```sh
.venv/bin/pip install -r requirements.txt
```


```sh
MOCAP_CREATURE=assets/dragon .venv/bin/python -m mocap.solve examples/dragon_roar/det.npz assets/dragon/rigged/rig_info.json motion.json
```

### First project

Start with a short, representative project and inspect the result before a larger batch. [Source 1](https://github.com/patch-gg/anymove/blob/main/README.md) [Source 2](https://github.com/patch-gg/anymove/releases/tag/examples-v1)

1. Fit the supplied roar example and inspect its two-view agreement.
2. For a new creature, prepare the mesh, place joints by hand, render poses and train its reader.
3. Generate synchronized two-view clips through fal, fit the rig and inspect foot contact and limb identity before exporting.
### Hardware & software

Requirements below are documented for this workflow. Unspecified limits are not inferred. [Source 1](https://github.com/patch-gg/anymove/blob/main/README.md) [Source 2](https://github.com/patch-gg/anymove/releases/tag/examples-v1)

- **Hardware:** The quick start requests 24 GB NVIDIA VRAM to train a reader; a separate run reports 12 GB, so that measurement is not substituted for the stated setup requirement. Reading/fitting need less but no minimum is documented. Example assets include a 355 MB reader; total RAM/disk minimum is unspecified.
- **Software:** Python 3.11, PyTorch 2.11.0/cu128, Blender 5.x and NVIDIA CUDA for the full training/capture route.
- **Platforms:** The source documents a shell-based CUDA workflow and a CPU-only fitting example; it does not publish a complete tested Windows/macOS/Linux matrix.

### License, model weights & costs

The full software license was reviewed. Model weights, assets and services remain separate. [Source 1](https://github.com/patch-gg/anymove/blob/main/LICENSE) [Source 2](https://github.com/patch-gg/anymove/blob/main/README.md) [Source 3](https://github.com/patch-gg/anymove/releases/tag/examples-v1)

- **Code:** Apache-2.0
- **Weights:** Apache-2.0 project code; DINOv2 has its own Apache-2.0 terms. MiniMax H3 weights/LoRA use a separate community license, fal is a hosted service and source meshes/assets need their own rights.
- **Commercial:** Software use follows Apache-2.0. Apache-2.0 project code; DINOv2 has its own Apache-2.0 terms. MiniMax H3 weights/LoRA use a separate community license, fal is a hosted service and source meshes/assets need their own rights.
- **Cost:** Local GPU compute plus fal generation charges. Author examples quote October 2026 per-clip costs; current account prices must be checked.

### Why it merits attention

Included for the documented creative workflow. A complete guide and popularity do not establish output reliability. [Source 1](https://github.com/patch-gg/anymove/blob/main/README.md) [Source 2](https://github.com/patch-gg/anymove/releases/tag/examples-v1)

### Limitations

Eight-legged walking and lying-down motions currently fail in documented examples. Rigs are placed manually; video-view timing, limb colors and ground-contact assumptions can fail. No production animation guarantee. [Source 1](https://github.com/patch-gg/anymove/blob/main/README.md) [Source 2](https://github.com/patch-gg/anymove/releases/tag/examples-v1)

### Get the tool

- [Repository](https://github.com/patch-gg/anymove)
- [Documentation](https://github.com/patch-gg/anymove/blob/main/README.md)

## Loom textures

Neural procedural material authoring · Games & production pipelines · 3D, reconstruction & assets

A recently created project receiving its first full library guide; its creation is not proof of production readiness.

### Quality assessment: Quality unverified

Software licensing and a concrete creative AI use are supported. The remaining checks do not establish a recommendation.

Scope: Creating inspectable seamless game materials with albedo, normals, height, roughness, metallic, AO, ORM and emissive outputs.

Evidence checked: 2026-10-27. No local execution implied.

- **Open-source software license · verified:** The complete root software license was read and archived. The grant covers this project code; unresolved model, service and asset terms are disclosed separately. [Source](https://github.com/uilianks/loom/blob/main/LICENSE)
- **Creative results · documented:** Official sphere/tile galleries and the Dragon’s Hoard Blender scene show materials from the supplied source file. A seam check does not establish artistic realism. [Source](https://github.com/uilianks/loom/blob/main/README.md)
- **Reproducible setup · documented:** Clone the repository, install its Node dependencies, and build or serve the example material file. Its optional skill integrates the same tools into an AI coding agent. Independent reproduction has not been established in this review. [Source](https://github.com/uilianks/loom/blob/main/README.md)
- **Maintenance and support · documented:** Live review archived 3 recent commits, 0 published release records and 0 recent support/PR records. Latest sampled commit: 2026-10-22. The bounded support sample did not establish third-party resolution history. This is documented activity, not proof of sustained support or a complete blocker survey. [Source](https://github.com/uilianks/loom/commits/main) [Source](https://github.com/uilianks/loom/issues)
- **Independent use · unknown:** Reviewed official examples, the current support sample and bounded live web findings. Independent first-hand reproduction of this exact creative workflow was not established; author demonstrations are not treated as independent evidence.
- **Models, services and costs · documented:** MIT code with upstream claude-pxl attribution/NOTICE. AI assistant access and any imported texture/image rights are separate. Local Node compute plus the chosen AI agent’s access or subscription; imported assets retain their own terms. [Source](https://github.com/uilianks/loom/blob/main/README.md)

Documentation review only; AI Media Scout did not install or run this software. This is an agent-driven procedural workflow, not text-to-texture inference built into the package. Seamlessness does not prove that every map is physically meaningful or suitable for a target renderer.

### How it uses AI

An AI-agent texture-authoring toolkit: an agent writes procedural material code, builds PBR maps and preview sheets, then uses annotated visual feedback to revise it. The renderer itself is deterministic, not a generative neural model. [Source](https://github.com/uilianks/loom/blob/main/README.md)

### Introduction

An AI-agent texture-authoring toolkit: an agent writes procedural material code, builds PBR maps and preview sheets, then uses annotated visual feedback to revise it. The renderer itself is deterministic, not a generative neural model. [Source 1](https://github.com/uilianks/loom/blob/main/README.md)

### What it is good for

Creating inspectable seamless game materials with albedo, normals, height, roughness, metallic, AO, ORM and emissive outputs. [Source 1](https://github.com/uilianks/loom/blob/main/README.md)

### Demo & examples

Official sphere/tile galleries and the Dragon’s Hoard Blender scene show materials from the supplied source file. A seam check does not establish artistic realism. [Source 1](https://github.com/uilianks/loom/blob/main/README.md)

### Install

Clone the repository, install its Node dependencies, and build or serve the example material file. Its optional skill integrates the same tools into an AI coding agent. [Source 1](https://github.com/uilianks/loom/blob/main/README.md)

1. Obtain the official source or release linked below.
2. Clone the repository, install its Node dependencies, and build or serve the example material file. Its optional skill integrates the same tools into an AI coding agent.

```sh
npm install
```


```sh
node bin/loom.js build showcase/materials.tx.js
```


```sh
node bin/loom.js serve showcase/materials.tx.js
```

### First project

Start with a short, representative project and inspect the result before a larger batch. [Source 1](https://github.com/uilianks/loom/blob/main/README.md)

1. Build the example and inspect the tiled, sphere and cube previews.
2. Ask an agent to write a small .tx.js material using the documented generators.
3. Annotate the preview and revise maps; inspect scale, color space and normals inside the target engine.
### Hardware & software

Requirements below are documented for this workflow. Unspecified limits are not inferred. [Source 1](https://github.com/uilianks/loom/blob/main/README.md)

- **Hardware:** Minimum system RAM, VRAM and total disk space are not documented in the reviewed instructions.
- **Software:** Node.js 22.18 or newer; npm and a browser for the live viewer. An external AI coding agent is required for the AI-directed workflow.
- **Platforms:** No complete tested operating-system matrix or GPU requirement is documented.

### License, model weights & costs

The full software license was reviewed. Model weights, assets and services remain separate. [Source 1](https://github.com/uilianks/loom/blob/main/LICENSE) [Source 2](https://github.com/uilianks/loom/blob/main/README.md)

- **Code:** MIT
- **Weights:** MIT code with upstream claude-pxl attribution/NOTICE. AI assistant access and any imported texture/image rights are separate.
- **Commercial:** Software use follows MIT. MIT code with upstream claude-pxl attribution/NOTICE. AI assistant access and any imported texture/image rights are separate.
- **Cost:** Local Node compute plus the chosen AI agent’s access or subscription; imported assets retain their own terms.

### Why it merits attention

Included for the documented creative workflow. A complete guide and popularity do not establish output reliability. [Source 1](https://github.com/uilianks/loom/blob/main/README.md)

### Limitations

This is an agent-driven procedural workflow, not text-to-texture inference built into the package. Seamlessness does not prove that every map is physically meaningful or suitable for a target renderer. [Source 1](https://github.com/uilianks/loom/blob/main/README.md)

### Get the tool

- [Repository](https://github.com/uilianks/loom)
- [Documentation](https://github.com/uilianks/loom/blob/main/README.md)

## Imagen CLI/TUI

Images & design · Editing, captions & post-production · Photography, restoration & color

A recently created project receiving its first full library guide; its creation is not proof of production readiness.

### Quality assessment: Quality unverified

Software licensing and a concrete creative AI use are supported. The remaining checks do not establish a recommendation.

Scope: Managing image variations, comparing contact sheets and preserving image-generation provenance across CLI and terminal UI sessions.

Evidence checked: 2026-10-27. No local execution implied.

- **Open-source software license · verified:** The complete root software license was read and archived. The grant covers this project code; unresolved model, service and asset terms are disclosed separately. [Source](https://github.com/NekoCCN/ImagenCli/blob/main/LICENSE)
- **Creative results · documented:** Official screenshots show session previews, generation controls and model-license listings. They do not independently establish image quality or provider reliability. [Source](https://github.com/NekoCCN/ImagenCli/blob/main/README.md)
- **Reproducible setup · documented:** Install the published Python tool through uv or pipx. Configure a supported image endpoint and a credential reference, create a session, then generate, approve and execute a plan. Model discovery does not prove that a provider supports every requested operation. Independent reproduction has not been established in this review. [Source](https://github.com/NekoCCN/ImagenCli/blob/main/README.md)
- **Maintenance and support · documented:** Live review archived 10 recent commits, 5 published release records and 1 recent support/PR records. Latest sampled commit: 2026-10-27. The bounded support sample did not establish third-party resolution history. This is documented activity, not proof of sustained support or a complete blocker survey. [Source](https://github.com/NekoCCN/ImagenCli/commits/main) [Source](https://github.com/NekoCCN/ImagenCli/issues)
- **Independent use · unknown:** Reviewed official examples, the current support sample and bounded live web findings. Independent first-hand reproduction of this exact creative workflow was not established; author demonstrations are not treated as independent evidence.
- **Models, services and costs · documented:** MIT source. Provider services and model weights have separate terms; listed restoration/upscaling models include distinct attribution or public-domain declarations and community ONNX conversions. Generation/edit calls can incur provider fees; local processing uses the user’s hardware. No universal free provider or zero-cost inference is implied. [Source](https://github.com/NekoCCN/ImagenCli/blob/main/README.md)

Documentation review only; AI Media Scout did not install or run this software. Postprocessing is explicitly experimental, while the assessed main workflow is provider/session orchestration. Some remote asynchronous jobs and TUI feature parity remain planned. Restored texture may be invented; memory limits are not a complete sandbox.

### How it uses AI

A persistent image-generation workbench shared by people and AI agents, with provider-backed generation/editing, reviewable plans, local postprocessing and optional neural upscaling. [Source](https://github.com/NekoCCN/ImagenCli/blob/main/README.md)

### Introduction

A persistent image-generation workbench shared by people and AI agents, with provider-backed generation/editing, reviewable plans, local postprocessing and optional neural upscaling. [Source 1](https://github.com/NekoCCN/ImagenCli/blob/main/README.md)

### What it is good for

Managing image variations, comparing contact sheets and preserving image-generation provenance across CLI and terminal UI sessions. [Source 1](https://github.com/NekoCCN/ImagenCli/blob/main/README.md)

### Demo & examples

Official screenshots show session previews, generation controls and model-license listings. They do not independently establish image quality or provider reliability. [Source 1](https://github.com/NekoCCN/ImagenCli/blob/main/README.md)

### Install

Install the published Python tool through uv or pipx. Configure a supported image endpoint and a credential reference, create a session, then generate, approve and execute a plan. Model discovery does not prove that a provider supports every requested operation. [Source 1](https://github.com/NekoCCN/ImagenCli/blob/main/README.md)

1. Obtain the official source or release linked below.
2. Install the published Python tool through uv or pipx. Configure a supported image endpoint and a credential reference, create a session, then generate, approve and execute a plan. Model discovery does not prove that a provider supports every requested operation.

```sh
uv tool install "imagen-cli[tui,postprocess]"
```


```sh
imagen tui
```


```sh
imagen help generate
```


```sh
imagen superres models
```

### First project

Start with a short, representative project and inspect the result before a larger batch. [Source 1](https://github.com/NekoCCN/ImagenCli/blob/main/README.md)

1. Configure the actual provider/model and create a named session.
2. Create a generation/edit plan, review its content and costs, then approve its digest and execute it.
3. Inspect artifacts before local transforms or upscaling; preserve unknown provider outcomes for reconciliation rather than blindly generating again.
### Hardware & software

Requirements below are documented for this workflow. Unspecified limits are not inferred. [Source 1](https://github.com/NekoCCN/ImagenCli/blob/main/README.md)

- **Hardware:** Minimum system RAM, VRAM and total disk space are not documented in the reviewed instructions.
- **Software:** Python 3.12+; optional Textual and image-processing extras. Neural upscaling needs separately accepted runtime and model downloads.
- **Platforms:** Linux/macOS paths are documented; physical Windows verification is explicitly unfinished. No full validated OS matrix is established.

### License, model weights & costs

The full software license was reviewed. Model weights, assets and services remain separate. [Source 1](https://github.com/NekoCCN/ImagenCli/blob/main/LICENSE) [Source 2](https://github.com/NekoCCN/ImagenCli/blob/main/README.md)

- **Code:** MIT
- **Weights:** MIT source. Provider services and model weights have separate terms; listed restoration/upscaling models include distinct attribution or public-domain declarations and community ONNX conversions.
- **Commercial:** Software use follows MIT. MIT source. Provider services and model weights have separate terms; listed restoration/upscaling models include distinct attribution or public-domain declarations and community ONNX conversions.
- **Cost:** Generation/edit calls can incur provider fees; local processing uses the user’s hardware. No universal free provider or zero-cost inference is implied.

### Why it merits attention

Included for the documented creative workflow. A complete guide and popularity do not establish output reliability. [Source 1](https://github.com/NekoCCN/ImagenCli/blob/main/README.md)

### Limitations

Postprocessing is explicitly experimental, while the assessed main workflow is provider/session orchestration. Some remote asynchronous jobs and TUI feature parity remain planned. Restored texture may be invented; memory limits are not a complete sandbox. [Source 1](https://github.com/NekoCCN/ImagenCli/blob/main/README.md)

### Get the tool

- [Repository](https://github.com/NekoCCN/ImagenCli)
- [Documentation](https://github.com/NekoCCN/ImagenCli/blob/main/README.md)

## Mosamem

Images & design · Typography, fonts & layout · Editing, captions & post-production

A recently created project receiving its first full library guide; its creation is not proof of production readiness.

### Quality assessment: Experimental

Software licensing and a concrete creative AI use are supported. The remaining checks do not establish a recommendation.

Scope: Preparing Arabic social graphics, masking photos and editing layered PSD-based design drafts.

Evidence checked: 2026-10-27. No local execution implied.

Why Experimental: The current 0.1 README explicitly calls this a first beta with unfinished features; PSD fidelity and Windows validation remain limited for the assessed layered-image workflow. https://github.com/motalim-ai/mosamem/blob/main/README.md https://github.com/motalim-ai/mosamem/blob/main/docs/status.md https://github.com/motalim-ai/mosamem/blob/main/THIRD-PARTY-NOTICES.md

- **Open-source software license · verified:** The complete root software license was read and archived. The grant covers this project code; unresolved model, service and asset terms are disclosed separately. [Source](https://github.com/motalim-ai/mosamem/blob/main/LICENSE)
- **Creative results · documented:** Official interface captures and a feature-tour report show editing and AI operations. The Windows report is from an ARM virtual machine running x64, not a physical Windows graphics-card validation. [Source](https://github.com/motalim-ai/mosamem/blob/main/README.md) [Source](https://github.com/motalim-ai/mosamem/blob/main/docs/status.md) [Source](https://github.com/motalim-ai/mosamem/blob/main/THIRD-PARTY-NOTICES.md)
- **Reproducible setup · documented:** Obtain the official macOS or Windows installer, or build with Rust, Node 20+ and Tauri. The published installers are unsigned; inspect release checksums and current platform guidance. Models are downloaded individually on first use. Independent reproduction has not been established in this review. [Source](https://github.com/motalim-ai/mosamem/blob/main/README.md) [Source](https://github.com/motalim-ai/mosamem/blob/main/docs/status.md) [Source](https://github.com/motalim-ai/mosamem/blob/main/THIRD-PARTY-NOTICES.md)
- **Maintenance and support · documented:** Live review archived 10 recent commits, 1 published release records and 1 recent support/PR records. Latest sampled commit: 2026-10-21. Current sampled topics include اختيار اتجاه القوائم. This is documented activity, not proof of sustained support or a complete blocker survey. [Source](https://github.com/motalim-ai/mosamem/commits/main) [Source](https://github.com/motalim-ai/mosamem/issues)
- **Independent use · unknown:** Reviewed official examples, the current support sample and bounded live web findings. Independent first-hand reproduction of this exact creative workflow was not established; author demonstrations are not treated as independent evidence.
- **Models, services and costs · documented:** GPL-3.0 project code; downloaded BiRefNet-lite and MI-GAN are listed as MIT, SAM 2.1 as Apache-2.0, with separate runtime/font notices. Project name/icon rights are separate. Local compute plus any chosen external model or service; provider access and charges are separate. [Source](https://github.com/motalim-ai/mosamem/blob/main/README.md) [Source](https://github.com/motalim-ai/mosamem/blob/main/docs/status.md) [Source](https://github.com/motalim-ai/mosamem/blob/main/THIRD-PARTY-NOTICES.md)

Documentation review only; AI Media Scout did not install or run this software. The current 0.1 release is explicitly an early beta with unfinished work. PSD support is partial: non-RGB modes, smart-object contents and several Photoshop effects do not round-trip as editable equivalents.

### How it uses AI

An Arabic-first layered photo editor with local neural subject selection, background removal, object masks and inpainting alongside editable Arabic typography. [Source](https://github.com/motalim-ai/mosamem/blob/main/README.md) [Source](https://github.com/motalim-ai/mosamem/blob/main/docs/status.md) [Source](https://github.com/motalim-ai/mosamem/blob/main/THIRD-PARTY-NOTICES.md)

### Introduction

An Arabic-first layered photo editor with local neural subject selection, background removal, object masks and inpainting alongside editable Arabic typography. [Source 1](https://github.com/motalim-ai/mosamem/blob/main/README.md) [Source 2](https://github.com/motalim-ai/mosamem/blob/main/docs/status.md) [Source 3](https://github.com/motalim-ai/mosamem/blob/main/THIRD-PARTY-NOTICES.md)

### What it is good for

Preparing Arabic social graphics, masking photos and editing layered PSD-based design drafts. [Source 1](https://github.com/motalim-ai/mosamem/blob/main/README.md) [Source 2](https://github.com/motalim-ai/mosamem/blob/main/docs/status.md) [Source 3](https://github.com/motalim-ai/mosamem/blob/main/THIRD-PARTY-NOTICES.md)

### Demo & examples

Official interface captures and a feature-tour report show editing and AI operations. The Windows report is from an ARM virtual machine running x64, not a physical Windows graphics-card validation. [Source 1](https://github.com/motalim-ai/mosamem/blob/main/README.md) [Source 2](https://github.com/motalim-ai/mosamem/blob/main/docs/status.md) [Source 3](https://github.com/motalim-ai/mosamem/blob/main/THIRD-PARTY-NOTICES.md)

### Install

Obtain the official macOS or Windows installer, or build with Rust, Node 20+ and Tauri. The published installers are unsigned; inspect release checksums and current platform guidance. Models are downloaded individually on first use. [Source 1](https://github.com/motalim-ai/mosamem/blob/main/README.md) [Source 2](https://github.com/motalim-ai/mosamem/blob/main/docs/status.md) [Source 3](https://github.com/motalim-ai/mosamem/blob/main/THIRD-PARTY-NOTICES.md)

1. Obtain the official source or release linked below.
2. Obtain the official macOS or Windows installer, or build with Rust, Node 20+ and Tauri. The published installers are unsigned; inspect release checksums and current platform guidance. Models are downloaded individually on first use.

```sh
npm install
```


```sh
npx tauri dev
```


```sh
npx tauri build
```

### First project

Start with a short, representative project and inspect the result before a larger batch. [Source 1](https://github.com/motalim-ai/mosamem/blob/main/README.md) [Source 2](https://github.com/motalim-ai/mosamem/blob/main/docs/status.md) [Source 3](https://github.com/motalim-ai/mosamem/blob/main/THIRD-PARTY-NOTICES.md)

1. Open a copy of an image or PSD and choose the Arabic or English interface.
2. Use subject selection, background removal or smart fill and inspect edges and invented content.
3. Keep the layered .mosamem project and compare exported PSD/raster output, especially unsupported Photoshop features.
### Hardware & software

Requirements below are documented for this workflow. Unspecified limits are not inferred. [Source 1](https://github.com/motalim-ai/mosamem/blob/main/README.md) [Source 2](https://github.com/motalim-ai/mosamem/blob/main/docs/status.md) [Source 3](https://github.com/motalim-ai/mosamem/blob/main/THIRD-PARTY-NOTICES.md)

- **Hardware:** Models are documented at roughly 28–115 MB each; minimum system RAM/VRAM and whole-install storage are not stated. Large layered images can use substantial memory.
- **Software:** macOS 13.4+ on Apple silicon, or Windows 10/11 x64 with WebView2. Source builds need Rust and Node 20+; Windows also needs Visual Studio C++ tools.
- **Platforms:** Mac Apple silicon and Windows x64 installers; Windows ARM uses x64 emulation. Physical Windows performance and GPU paths are not fully verified. Linux support is not documented.

### License, model weights & costs

The full software license was reviewed. Model weights, assets and services remain separate. [Source 1](https://github.com/motalim-ai/mosamem/blob/main/LICENSE) [Source 2](https://github.com/motalim-ai/mosamem/blob/main/README.md) [Source 3](https://github.com/motalim-ai/mosamem/blob/main/docs/status.md) [Source 4](https://github.com/motalim-ai/mosamem/blob/main/THIRD-PARTY-NOTICES.md)

- **Code:** GPL-3.0
- **Weights:** GPL-3.0 project code; downloaded BiRefNet-lite and MI-GAN are listed as MIT, SAM 2.1 as Apache-2.0, with separate runtime/font notices. Project name/icon rights are separate.
- **Commercial:** Software use follows GPL-3.0. GPL-3.0 project code; downloaded BiRefNet-lite and MI-GAN are listed as MIT, SAM 2.1 as Apache-2.0, with separate runtime/font notices. Project name/icon rights are separate.
- **Cost:** Local compute plus any chosen external model or service; provider access and charges are separate.

### Why it merits attention

Included for the documented creative workflow. A complete guide and popularity do not establish output reliability. [Source 1](https://github.com/motalim-ai/mosamem/blob/main/README.md) [Source 2](https://github.com/motalim-ai/mosamem/blob/main/docs/status.md) [Source 3](https://github.com/motalim-ai/mosamem/blob/main/THIRD-PARTY-NOTICES.md)

### Limitations

The current 0.1 release is explicitly an early beta with unfinished work. PSD support is partial: non-RGB modes, smart-object contents and several Photoshop effects do not round-trip as editable equivalents. [Source 1](https://github.com/motalim-ai/mosamem/blob/main/README.md) [Source 2](https://github.com/motalim-ai/mosamem/blob/main/docs/status.md) [Source 3](https://github.com/motalim-ai/mosamem/blob/main/THIRD-PARTY-NOTICES.md)

### Get the tool

- [Repository](https://github.com/motalim-ai/mosamem)
- [Documentation](https://github.com/motalim-ai/mosamem/blob/main/README.md)

## Albie mixed-reality workspace

WebXR, VR & AR · Interactive, immersive & live media · AI parametric design and jewelry

A recently created project receiving its first full library guide; its creation is not proof of production readiness.

### Quality assessment: Quality unverified

Software licensing and a concrete creative AI use are supported. The remaining checks do not establish a recommendation.

Scope: Exploring voice-driven spatial design interfaces and interactive CAD/visualization prototypes on Quest.

Evidence checked: 2026-10-27. No local execution implied.

- **Open-source software license · verified:** The complete root software license was read and archived. The grant covers this project code; unresolved model, service and asset terms are disclosed separately. [Source](https://github.com/builtbyd3v/Albie/blob/main/LICENSE)
- **Creative results · documented:** The team supplies a three-minute headset demo and a device-readiness screenshot. The readiness check and author ML accuracy examples do not establish reproducible creative quality. [Source](https://github.com/builtbyd3v/Albie/blob/main/README.md) [Source](https://youtu.be/28D1QIcsdzI) [Source](https://github.com/builtbyd3v/Albie/blob/main/docs/SETUP.md) [Source](https://github.com/builtbyd3v/Albie/blob/main/docs/DISCLOSURE.md)
- **Reproducible setup · documented:** Follow the official setup guide: configure the Python hub and service credentials, import the required licensed character assets, open Unity 6000.6.7f1, build an Android APK and connect a Quest in developer mode. The full documented setup is macOS Apple silicon. Independent reproduction has not been established in this review. [Source](https://github.com/builtbyd3v/Albie/blob/main/README.md) [Source](https://youtu.be/28D1QIcsdzI) [Source](https://github.com/builtbyd3v/Albie/blob/main/docs/SETUP.md) [Source](https://github.com/builtbyd3v/Albie/blob/main/docs/DISCLOSURE.md)
- **Maintenance and support · documented:** Live review archived 10 recent commits, 0 published release records and 10 recent support/PR records. Latest sampled commit: 2026-10-25. The bounded support sample did not establish third-party resolution history. This is documented activity, not proof of sustained support or a complete blocker survey. [Source](https://github.com/builtbyd3v/Albie/commits/main) [Source](https://github.com/builtbyd3v/Albie/issues)
- **Independent use · unknown:** Reviewed official examples, the current support sample and bounded live web findings. Independent first-hand reproduction of this exact creative workflow was not established; author demonstrations are not treated as independent evidence.
- **Models, services and costs · documented:** MIT project code. Unity/Meta SDK terms, Grok/Claude/TypeSafe services and a paid Unity Asset Store alligator remain separate. Modified character mesh files are omitted and the guide asks for them from a teammate, leaving a fresh-clone reproduction gap. Headset, possible Unity/asset costs and paid model/API access; no universal free runtime. [Source](https://github.com/builtbyd3v/Albie/blob/main/README.md) [Source](https://youtu.be/28D1QIcsdzI) [Source](https://github.com/builtbyd3v/Albie/blob/main/docs/SETUP.md) [Source](https://github.com/builtbyd3v/Albie/blob/main/docs/DISCLOSURE.md)

Documentation review only; AI Media Scout did not install or run this software. Public source does not include all character assets. The hub and screen bridge lack authentication. Headset readiness is not proof of performance, agent reliability or engineering safety.

### How it uses AI

A Quest mixed-reality workspace whose conversational AI agent changes parametric CAD, presents ML experiments and coordinates a spatial desktop through a laptop hub. [Source](https://github.com/builtbyd3v/Albie/blob/main/README.md) [Source](https://youtu.be/28D1QIcsdzI) [Source](https://github.com/builtbyd3v/Albie/blob/main/docs/SETUP.md) [Source](https://github.com/builtbyd3v/Albie/blob/main/docs/DISCLOSURE.md)

### Introduction

A Quest mixed-reality workspace whose conversational AI agent changes parametric CAD, presents ML experiments and coordinates a spatial desktop through a laptop hub. [Source 1](https://github.com/builtbyd3v/Albie/blob/main/README.md) [Source 2](https://youtu.be/28D1QIcsdzI) [Source 3](https://github.com/builtbyd3v/Albie/blob/main/docs/SETUP.md) [Source 4](https://github.com/builtbyd3v/Albie/blob/main/docs/DISCLOSURE.md)

### What it is good for

Exploring voice-driven spatial design interfaces and interactive CAD/visualization prototypes on Quest. [Source 1](https://github.com/builtbyd3v/Albie/blob/main/README.md) [Source 2](https://youtu.be/28D1QIcsdzI) [Source 3](https://github.com/builtbyd3v/Albie/blob/main/docs/SETUP.md) [Source 4](https://github.com/builtbyd3v/Albie/blob/main/docs/DISCLOSURE.md)

### Demo & examples

The team supplies a three-minute headset demo and a device-readiness screenshot. The readiness check and author ML accuracy examples do not establish reproducible creative quality. [Source 1](https://github.com/builtbyd3v/Albie/blob/main/README.md) [Source 2](https://youtu.be/28D1QIcsdzI) [Source 3](https://github.com/builtbyd3v/Albie/blob/main/docs/SETUP.md) [Source 4](https://github.com/builtbyd3v/Albie/blob/main/docs/DISCLOSURE.md)

### Install

Follow the official setup guide: configure the Python hub and service credentials, import the required licensed character assets, open Unity 6000.6.7f1, build an Android APK and connect a Quest in developer mode. The full documented setup is macOS Apple silicon. [Source 1](https://github.com/builtbyd3v/Albie/blob/main/README.md) [Source 2](https://youtu.be/28D1QIcsdzI) [Source 3](https://github.com/builtbyd3v/Albie/blob/main/docs/SETUP.md) [Source 4](https://github.com/builtbyd3v/Albie/blob/main/docs/DISCLOSURE.md)

1. Obtain the official source or release linked below.
2. Follow the official setup guide: configure the Python hub and service credentials, import the required licensed character assets, open Unity 6000.6.7f1, build an Android APK and connect a Quest in developer mode. The full documented setup is macOS Apple silicon.

```sh
sh dev-setup.sh <env-file>
```


```sh
sh run-demo.sh
```

### First project

Start with a short, representative project and inspect the result before a larger batch. [Source 1](https://github.com/builtbyd3v/Albie/blob/main/README.md) [Source 2](https://youtu.be/28D1QIcsdzI) [Source 3](https://github.com/builtbyd3v/Albie/blob/main/docs/SETUP.md) [Source 4](https://github.com/builtbyd3v/Albie/blob/main/docs/DISCLOSURE.md)

1. Prepare the hub and inspect a small parametric CAD example before enabling agent edits.
2. Build and connect the Quest application, then request a bounded voice edit and inspect the resulting part.
3. Keep the unauthenticated hub/bridge on a private network and verify any generated engineering result separately.
### Hardware & software

Requirements below are documented for this workflow. Unspecified limits are not inferred. [Source 1](https://github.com/builtbyd3v/Albie/blob/main/README.md) [Source 2](https://youtu.be/28D1QIcsdzI) [Source 3](https://github.com/builtbyd3v/Albie/blob/main/docs/SETUP.md) [Source 4](https://github.com/builtbyd3v/Albie/blob/main/docs/DISCLOSURE.md)

- **Hardware:** Quest 3 or 3S and a connected development computer; Apple silicon for the complete host workflow. Minimum RAM/VRAM/storage are not documented.
- **Software:** Unity 6000.6.7f1 with Android build support, Meta XR SDK 207, Python 3.11+, Node 20+, Chrome/Playwright and optional VS Code bridge.
- **Platforms:** Quest 3/3S headset. Full host setup requires macOS Apple silicon; Windows/Linux instructions omit screen capture and iMessage. No claim of full cross-platform parity.

### License, model weights & costs

The full software license was reviewed. Model weights, assets and services remain separate. [Source 1](https://github.com/builtbyd3v/Albie/blob/main/LICENSE) [Source 2](https://github.com/builtbyd3v/Albie/blob/main/README.md) [Source 3](https://youtu.be/28D1QIcsdzI) [Source 4](https://github.com/builtbyd3v/Albie/blob/main/docs/SETUP.md) [Source 5](https://github.com/builtbyd3v/Albie/blob/main/docs/DISCLOSURE.md)

- **Code:** MIT
- **Weights:** MIT project code. Unity/Meta SDK terms, Grok/Claude/TypeSafe services and a paid Unity Asset Store alligator remain separate. Modified character mesh files are omitted and the guide asks for them from a teammate, leaving a fresh-clone reproduction gap.
- **Commercial:** Software use follows MIT. MIT project code. Unity/Meta SDK terms, Grok/Claude/TypeSafe services and a paid Unity Asset Store alligator remain separate. Modified character mesh files are omitted and the guide asks for them from a teammate, leaving a fresh-clone reproduction gap.
- **Cost:** Headset, possible Unity/asset costs and paid model/API access; no universal free runtime.

### Why it merits attention

Included for the documented creative workflow. A complete guide and popularity do not establish output reliability. [Source 1](https://github.com/builtbyd3v/Albie/blob/main/README.md) [Source 2](https://youtu.be/28D1QIcsdzI) [Source 3](https://github.com/builtbyd3v/Albie/blob/main/docs/SETUP.md) [Source 4](https://github.com/builtbyd3v/Albie/blob/main/docs/DISCLOSURE.md)

### Limitations

Public source does not include all character assets. The hub and screen bridge lack authentication. Headset readiness is not proof of performance, agent reliability or engineering safety. [Source 1](https://github.com/builtbyd3v/Albie/blob/main/README.md) [Source 2](https://youtu.be/28D1QIcsdzI) [Source 3](https://github.com/builtbyd3v/Albie/blob/main/docs/SETUP.md) [Source 4](https://github.com/builtbyd3v/Albie/blob/main/docs/DISCLOSURE.md)

### Get the tool

- [Repository](https://github.com/builtbyd3v/Albie)
- [Documentation](https://github.com/builtbyd3v/Albie/blob/main/README.md)

## Voice Foundry Local

Audio, music & voice · Storyboarding, narrative & comics · Accessible media & assistive creation

A recently created project receiving its first full library guide; its creation is not proof of production readiness.

### Quality assessment: Quality unverified

Software licensing and a concrete creative AI use are supported. The remaining checks do not establish a recommendation.

Scope: Creating character dialogue, video narration and chapter-based audiobook drafts with audition-and-approve controls.

Evidence checked: 2026-10-27. No local execution implied.

- **Open-source software license · verified:** The complete root software license was read and archived. The grant covers this project code; unresolved model, service and asset terms are disclosed separately. [Source](https://github.com/Xpink1999/voice-foundry-local/blob/main/LICENSE)
- **Creative results · documented:** Official screenshots and workflow documentation show generation, reference preparation and chapter review. A successful long-text import is explicitly not proof that a full audiobook was generated. [Source](https://github.com/Xpink1999/voice-foundry-local/blob/main/README.md) [Source](https://github.com/Xpink1999/voice-foundry-local/blob/main/docs/INSTALL.md) [Source](https://github.com/Xpink1999/voice-foundry-local/blob/main/THIRD_PARTY_NOTICES.md)
- **Reproducible setup · documented:** On Windows 11 x64 install Git, uv, an NVIDIA driver and FFmpeg, then obtain the source ZIP and launch install-voice.cmd. The installer creates a pinned Python/CUDA environment and downloads the model set. Independent reproduction has not been established in this review. [Source](https://github.com/Xpink1999/voice-foundry-local/blob/main/README.md) [Source](https://github.com/Xpink1999/voice-foundry-local/blob/main/docs/INSTALL.md) [Source](https://github.com/Xpink1999/voice-foundry-local/blob/main/THIRD_PARTY_NOTICES.md)
- **Maintenance and support · documented:** Live review archived 10 recent commits, 0 published release records and 0 recent support/PR records. Latest sampled commit: 2026-10-27. The bounded support sample did not establish third-party resolution history. This is documented activity, not proof of sustained support or a complete blocker survey. [Source](https://github.com/Xpink1999/voice-foundry-local/commits/main) [Source](https://github.com/Xpink1999/voice-foundry-local/issues)
- **Independent use · unknown:** Reviewed official examples, the current support sample and bounded live web findings. Independent first-hand reproduction of this exact creative workflow was not established; author demonstrations are not treated as independent evidence.
- **Models, services and costs · documented:** Apache-2.0 platform. Third-party notice lists VoxCPM2, Whisper, AST, Resemblyzer, MossFormer and source-separation models separately; MelBandRoformer uses a pinned model-card MIT declaration without a separate full weight license. Voice/text permissions are separate. Local inference after downloads; no required hosted generation service documented. [Source](https://github.com/Xpink1999/voice-foundry-local/blob/main/README.md) [Source](https://github.com/Xpink1999/voice-foundry-local/blob/main/docs/INSTALL.md) [Source](https://github.com/Xpink1999/voice-foundry-local/blob/main/THIRD_PARTY_NOTICES.md)

Documentation review only; AI Media Scout did not install or run this software. Voice emotion/speed descriptions are approximate. Denoising/separation can distort or leak voices. CoreOnly mode can open the UI but cannot synthesize or process recordings.

### How it uses AI

A local VoxCPM2 voice-design, cloning and long-form narration platform sharing one model/voice library across a Web UI, CLI, REST API and MCP. [Source](https://github.com/Xpink1999/voice-foundry-local/blob/main/README.md) [Source](https://github.com/Xpink1999/voice-foundry-local/blob/main/docs/INSTALL.md) [Source](https://github.com/Xpink1999/voice-foundry-local/blob/main/THIRD_PARTY_NOTICES.md)

### Introduction

A local VoxCPM2 voice-design, cloning and long-form narration platform sharing one model/voice library across a Web UI, CLI, REST API and MCP. [Source 1](https://github.com/Xpink1999/voice-foundry-local/blob/main/README.md) [Source 2](https://github.com/Xpink1999/voice-foundry-local/blob/main/docs/INSTALL.md) [Source 3](https://github.com/Xpink1999/voice-foundry-local/blob/main/THIRD_PARTY_NOTICES.md)

### What it is good for

Creating character dialogue, video narration and chapter-based audiobook drafts with audition-and-approve controls. [Source 1](https://github.com/Xpink1999/voice-foundry-local/blob/main/README.md) [Source 2](https://github.com/Xpink1999/voice-foundry-local/blob/main/docs/INSTALL.md) [Source 3](https://github.com/Xpink1999/voice-foundry-local/blob/main/THIRD_PARTY_NOTICES.md)

### Demo & examples

Official screenshots and workflow documentation show generation, reference preparation and chapter review. A successful long-text import is explicitly not proof that a full audiobook was generated. [Source 1](https://github.com/Xpink1999/voice-foundry-local/blob/main/README.md) [Source 2](https://github.com/Xpink1999/voice-foundry-local/blob/main/docs/INSTALL.md) [Source 3](https://github.com/Xpink1999/voice-foundry-local/blob/main/THIRD_PARTY_NOTICES.md)

### Install

On Windows 11 x64 install Git, uv, an NVIDIA driver and FFmpeg, then obtain the source ZIP and launch install-voice.cmd. The installer creates a pinned Python/CUDA environment and downloads the model set. [Source 1](https://github.com/Xpink1999/voice-foundry-local/blob/main/README.md) [Source 2](https://github.com/Xpink1999/voice-foundry-local/blob/main/docs/INSTALL.md) [Source 3](https://github.com/Xpink1999/voice-foundry-local/blob/main/THIRD_PARTY_NOTICES.md)

1. Obtain the official source or release linked below.
2. On Windows 11 x64 install Git, uv, an NVIDIA driver and FFmpeg, then obtain the source ZIP and launch install-voice.cmd. The installer creates a pinned Python/CUDA environment and downloads the model set.

```sh
install-voice.cmd
```


```sh
start-voice.cmd
```


```sh
bin\voice.cmd health
```

### First project

Start with a short, representative project and inspect the result before a larger batch. [Source 1](https://github.com/Xpink1999/voice-foundry-local/blob/main/README.md) [Source 2](https://github.com/Xpink1999/voice-foundry-local/blob/main/docs/INSTALL.md) [Source 3](https://github.com/Xpink1999/voice-foundry-local/blob/main/THIRD_PARTY_NOTICES.md)

1. Open the local Web UI at port 8961 and generate a short line from a voice description.
2. Audition candidates before approving/exporting; proofread reference transcripts for cloning.
3. Import a short chapter first, review every segment, and keep original reference recordings.
### Hardware & software

Requirements below are documented for this workflow. Unspecified limits are not inferred. [Source 1](https://github.com/Xpink1999/voice-foundry-local/blob/main/README.md) [Source 2](https://github.com/Xpink1999/voice-foundry-local/blob/main/docs/INSTALL.md) [Source 3](https://github.com/Xpink1999/voice-foundry-local/blob/main/THIRD_PARTY_NOTICES.md)

- **Hardware:** At least 30 GiB free disk recommended: models about 7.1 GiB and PyTorch download about 3.2 GiB plus environment/cache. RTX 4090 is the tested device, not a documented minimum; minimum RAM/VRAM is unspecified.
- **Software:** Python 3.11.16 and PyTorch/torchaudio 2.8.0 cu128 are installed by the platform; FFmpeg for recording conversion and postprocessing. Visual C++ v14 runtime may be needed for DLL loading.
- **Platforms:** Windows 11 x64; principally tested by the author on RTX 4090. CPU and other GPU configurations have not received equivalent validation; Mac/Linux inference is not established.

### License, model weights & costs

The full software license was reviewed. Model weights, assets and services remain separate. [Source 1](https://github.com/Xpink1999/voice-foundry-local/blob/main/LICENSE) [Source 2](https://github.com/Xpink1999/voice-foundry-local/blob/main/README.md) [Source 3](https://github.com/Xpink1999/voice-foundry-local/blob/main/docs/INSTALL.md) [Source 4](https://github.com/Xpink1999/voice-foundry-local/blob/main/THIRD_PARTY_NOTICES.md)

- **Code:** Apache-2.0
- **Weights:** Apache-2.0 platform. Third-party notice lists VoxCPM2, Whisper, AST, Resemblyzer, MossFormer and source-separation models separately; MelBandRoformer uses a pinned model-card MIT declaration without a separate full weight license. Voice/text permissions are separate.
- **Commercial:** Software use follows Apache-2.0. Apache-2.0 platform. Third-party notice lists VoxCPM2, Whisper, AST, Resemblyzer, MossFormer and source-separation models separately; MelBandRoformer uses a pinned model-card MIT declaration without a separate full weight license. Voice/text permissions are separate.
- **Cost:** Local inference after downloads; no required hosted generation service documented.

### Why it merits attention

Included for the documented creative workflow. A complete guide and popularity do not establish output reliability. [Source 1](https://github.com/Xpink1999/voice-foundry-local/blob/main/README.md) [Source 2](https://github.com/Xpink1999/voice-foundry-local/blob/main/docs/INSTALL.md) [Source 3](https://github.com/Xpink1999/voice-foundry-local/blob/main/THIRD_PARTY_NOTICES.md)

### Limitations

Voice emotion/speed descriptions are approximate. Denoising/separation can distort or leak voices. CoreOnly mode can open the UI but cannot synthesize or process recordings. [Source 1](https://github.com/Xpink1999/voice-foundry-local/blob/main/README.md) [Source 2](https://github.com/Xpink1999/voice-foundry-local/blob/main/docs/INSTALL.md) [Source 3](https://github.com/Xpink1999/voice-foundry-local/blob/main/THIRD_PARTY_NOTICES.md)

### Get the tool

- [Repository](https://github.com/Xpink1999/voice-foundry-local)
- [Documentation](https://github.com/Xpink1999/voice-foundry-local/blob/main/README.md)

## 3D-Assisted Illustration

Images & design · 3D, reconstruction & assets · Computational art & creative coding

A recently created project receiving its first full library guide; its creation is not proof of production readiness.

### Quality assessment: Quality unverified

Software licensing and a concrete creative AI use are supported. The remaining checks do not establish a recommendation.

Scope: Making editable concept-art bases with perspective, lighting, masks and atmospheric passes before manual painting.

Evidence checked: 2026-10-27. No local execution implied.

- **Open-source software license · verified:** The complete root software license was read and archived. The grant covers this project code; unresolved model, service and asset terms are disclosed separately. [Source](https://github.com/starryark/3d-assisted-illustration/blob/main/LICENSE)
- **Creative results · documented:** The official rooftop case study includes five checkpoint renders, a final image and layered paintover outputs. Numeric checks catch selected failures but do not establish artistic success. [Source](https://github.com/starryark/3d-assisted-illustration/blob/main/README.md)
- **Reproducible setup · documented:** Install Blender 5.2+ and Python 3.9+, clone the source and run the supplied scene through tools/run.py. GPU rendering is optional; the documented workflow can fall back to CPU. Independent reproduction has not been established in this review. [Source](https://github.com/starryark/3d-assisted-illustration/blob/main/README.md)
- **Maintenance and support · documented:** Live review archived 4 recent commits, 1 published release records and 0 recent support/PR records. Latest sampled commit: 2026-10-25. The bounded support sample did not establish third-party resolution history. This is documented activity, not proof of sustained support or a complete blocker survey. [Source](https://github.com/starryark/3d-assisted-illustration/commits/main) [Source](https://github.com/starryark/3d-assisted-illustration/issues)
- **Independent use · unknown:** Reviewed official examples, the current support sample and bounded live web findings. Independent first-hand reproduction of this exact creative workflow was not established; author demonstrations are not treated as independent evidence.
- **Models, services and costs · documented:** MIT toolkit and original procedural example. Blender, optional painting applications, AI assistant access and imported asset rights are separate. Local rendering and chosen AI agent access; optional creative hosts/assets may have separate costs. [Source](https://github.com/starryark/3d-assisted-illustration/blob/main/README.md)

Documentation review only; AI Media Scout did not install or run this software. The toolkit is a deterministic staging/checking system used by AI agents, not a built-in text-to-image model. Some visual judgments remain outside its numeric gates; rendering a valid PSD does not prove a good illustration.

### How it uses AI

An AI-agent authoring workflow that builds Blender scenes in staged Python functions, checks geometric/visual constraints and exports layered PSD/ORA paintover kits. [Source](https://github.com/starryark/3d-assisted-illustration/blob/main/README.md)

### Introduction

An AI-agent authoring workflow that builds Blender scenes in staged Python functions, checks geometric/visual constraints and exports layered PSD/ORA paintover kits. [Source 1](https://github.com/starryark/3d-assisted-illustration/blob/main/README.md)

### What it is good for

Making editable concept-art bases with perspective, lighting, masks and atmospheric passes before manual painting. [Source 1](https://github.com/starryark/3d-assisted-illustration/blob/main/README.md)

### Demo & examples

The official rooftop case study includes five checkpoint renders, a final image and layered paintover outputs. Numeric checks catch selected failures but do not establish artistic success. [Source 1](https://github.com/starryark/3d-assisted-illustration/blob/main/README.md)

### Install

Install Blender 5.2+ and Python 3.9+, clone the source and run the supplied scene through tools/run.py. GPU rendering is optional; the documented workflow can fall back to CPU. [Source 1](https://github.com/starryark/3d-assisted-illustration/blob/main/README.md)

1. Obtain the official source or release linked below.
2. Install Blender 5.2+ and Python 3.9+, clone the source and run the supplied scene through tools/run.py. GPU rendering is optional; the documented workflow can fall back to CPU.

```sh
python tools/run.py scenes/rooftop_city --quality draft
```


```sh
python tools/new_scene.py harbor_dawn "Harbor at Dawn"
```


```sh
python tools/run.py scenes/harbor_dawn --until blockout
```

### First project

Start with a short, representative project and inspect the result before a larger batch. [Source 1](https://github.com/starryark/3d-assisted-illustration/blob/main/README.md)

1. Render the example and inspect contact, visibility, exposure and grayscale reports.
2. Have an AI coding agent write one scene stage at a time, reviewing each image and numeric check.
3. Export the final layered PSD/ORA and complete the illustration manually in a compatible painting editor.
### Hardware & software

Requirements below are documented for this workflow. Unspecified limits are not inferred. [Source 1](https://github.com/starryark/3d-assisted-illustration/blob/main/README.md)

- **Hardware:** GPU optional; minimum RAM/VRAM and storage are not documented. Published render timings are author examples, not hardware-independent promises.
- **Software:** Blender 5.2+, Python 3.9+; optional psd-tools, Pillow and numpy for external PSD read-back. An AI coding agent supplies the AI authoring role.
- **Platforms:** Headless Blender with CPU/GPU rendering; a complete tested OS support matrix is not documented.

### License, model weights & costs

The full software license was reviewed. Model weights, assets and services remain separate. [Source 1](https://github.com/starryark/3d-assisted-illustration/blob/main/LICENSE) [Source 2](https://github.com/starryark/3d-assisted-illustration/blob/main/README.md)

- **Code:** MIT
- **Weights:** MIT toolkit and original procedural example. Blender, optional painting applications, AI assistant access and imported asset rights are separate.
- **Commercial:** Software use follows MIT. MIT toolkit and original procedural example. Blender, optional painting applications, AI assistant access and imported asset rights are separate.
- **Cost:** Local rendering and chosen AI agent access; optional creative hosts/assets may have separate costs.

### Why it merits attention

Included for the documented creative workflow. A complete guide and popularity do not establish output reliability. [Source 1](https://github.com/starryark/3d-assisted-illustration/blob/main/README.md)

### Limitations

The toolkit is a deterministic staging/checking system used by AI agents, not a built-in text-to-image model. Some visual judgments remain outside its numeric gates; rendering a valid PSD does not prove a good illustration. [Source 1](https://github.com/starryark/3d-assisted-illustration/blob/main/README.md)

### Get the tool

- [Repository](https://github.com/starryark/3d-assisted-illustration)
- [Documentation](https://github.com/starryark/3d-assisted-illustration/blob/main/README.md)

## GenSfM

3D, reconstruction & assets · Photogrammetry, scanning & neural rendering · Spatial audio & volumetric media

A recently created project receiving its first full library guide; its creation is not proof of production readiness.

### Quality assessment: Quality unverified

Software licensing and a concrete creative AI use are supported. The remaining checks do not establish a recommendation.

Scope: Reconstructing object references for 3D scenes and inspecting recovered cameras alongside textured GLB and Gaussian outputs.

Evidence checked: 2026-10-27. No local execution implied.

- **Open-source software license · verified:** The complete root software license was read and archived. The grant covers this project code; unresolved model, service and asset terms are disclosed separately. [Source](https://github.com/dotb1ue/GenSfm/blob/main/LICENSE)
- **Creative results · documented:** The official project video/gallery and included masked objects show reconstruction and camera recovery. These are author examples, not independent metrology or manufacturing validation. [Source](https://github.com/dotb1ue/GenSfm/blob/main/README.md) [Source](https://dotb1ue.github.io/GenSfm/) [Source](https://huggingface.co/dotblue/GenSfm)
- **Reproducible setup · documented:** Use Linux with NVIDIA CUDA/nvcc, initialize Conda/Mamba and install the repository’s rendering extensions. The documented environment uses Python 3.12, PyTorch 2.9.1 and CUDA 12.8. Independent reproduction has not been established in this review. [Source](https://github.com/dotb1ue/GenSfm/blob/main/README.md) [Source](https://dotb1ue.github.io/GenSfm/) [Source](https://huggingface.co/dotblue/GenSfm)
- **Maintenance and support · documented:** Live review archived 3 recent commits, 0 published release records and 0 recent support/PR records. Latest sampled commit: 2026-10-27. The bounded support sample did not establish third-party resolution history. This is documented activity, not proof of sustained support or a complete blocker survey. [Source](https://github.com/dotb1ue/GenSfm/commits/main) [Source](https://github.com/dotb1ue/GenSfm/issues)
- **Independent use · unknown:** Reviewed official examples, the current support sample and bounded live web findings. Independent first-hand reproduction of this exact creative workflow was not established; author demonstrations are not treated as independent evidence.
- **Models, services and costs · documented:** MIT code and model bundle according to its current model card, with preserved TRELLIS notices. DINOv2 and optional rembg weights download separately; example images retain their source terms. Local GPU compute and downloads. [Source](https://github.com/dotb1ue/GenSfm/blob/main/README.md) [Source](https://dotb1ue.github.io/GenSfm/) [Source](https://huggingface.co/dotblue/GenSfm)

Documentation review only; AI Media Scout did not install or run this software. Inputs must show the same rigid object with usable masks. Training UV encoder/resume state is separate from the inference bundle. Reconstruction does not establish dimensional accuracy, watertightness or printability.

### How it uses AI

A native 3D diffusion pipeline that jointly predicts a rigid object’s geometry, texture and camera poses from two to four uncalibrated images. [Source](https://github.com/dotb1ue/GenSfm/blob/main/README.md) [Source](https://dotb1ue.github.io/GenSfm/) [Source](https://huggingface.co/dotblue/GenSfm)

### Introduction

A native 3D diffusion pipeline that jointly predicts a rigid object’s geometry, texture and camera poses from two to four uncalibrated images. [Source 1](https://github.com/dotb1ue/GenSfm/blob/main/README.md) [Source 2](https://dotb1ue.github.io/GenSfm/) [Source 3](https://huggingface.co/dotblue/GenSfm)

### What it is good for

Reconstructing object references for 3D scenes and inspecting recovered cameras alongside textured GLB and Gaussian outputs. [Source 1](https://github.com/dotb1ue/GenSfm/blob/main/README.md) [Source 2](https://dotb1ue.github.io/GenSfm/) [Source 3](https://huggingface.co/dotblue/GenSfm)

### Demo & examples

The official project video/gallery and included masked objects show reconstruction and camera recovery. These are author examples, not independent metrology or manufacturing validation. [Source 1](https://github.com/dotb1ue/GenSfm/blob/main/README.md) [Source 2](https://dotb1ue.github.io/GenSfm/) [Source 3](https://huggingface.co/dotblue/GenSfm)

### Install

Use Linux with NVIDIA CUDA/nvcc, initialize Conda/Mamba and install the repository’s rendering extensions. The documented environment uses Python 3.12, PyTorch 2.9.1 and CUDA 12.8. [Source 1](https://github.com/dotb1ue/GenSfm/blob/main/README.md) [Source 2](https://dotb1ue.github.io/GenSfm/) [Source 3](https://huggingface.co/dotblue/GenSfm)

1. Obtain the official source or release linked below.
2. Use Linux with NVIDIA CUDA/nvcc, initialize Conda/Mamba and install the repository’s rendering extensions. The documented environment uses Python 3.12, PyTorch 2.9.1 and CUDA 12.8.

```sh
. ./setup.sh --new-env --basic --spconv --mipgaussian --nvdiffrast
```


```sh
mamba activate gensfm
```


```sh
python example_multi_image.py --input-dir assets/example/wagon --pretrained dotblue/GenSfm --output-dir outputs/wagon
```

### First project

Start with a short, representative project and inspect the result before a larger batch. [Source 1](https://github.com/dotb1ue/GenSfm/blob/main/README.md) [Source 2](https://dotb1ue.github.io/GenSfm/) [Source 3](https://huggingface.co/dotblue/GenSfm)

1. Start with the included masked wagon example and inspect saved reprojected images.
2. Supply two to four masked views of one rigid object; four well-spread views are recommended.
3. Compare GLB geometry and texture against all views, respecting the documented camera-coordinate transform.
### Hardware & software

Requirements below are documented for this workflow. Unspecified limits are not inferred. [Source 1](https://github.com/dotb1ue/GenSfm/blob/main/README.md) [Source 2](https://dotb1ue.github.io/GenSfm/) [Source 3](https://huggingface.co/dotblue/GenSfm)

- **Hardware:** NVIDIA CUDA GPU required; minimum VRAM/RAM is not documented. Inference bundle is approximately 5.8 GB plus DINOv2, optional masking weights and environment storage.
- **Software:** Linux, Python 3.12, PyTorch 2.9.1, CUDA 12.8 toolkit and native rendering extensions. SDPA avoids optional attention packages.
- **Platforms:** Linux/NVIDIA CUDA is documented. Windows/macOS runtime support is not established.

### License, model weights & costs

The full software license was reviewed. Model weights, assets and services remain separate. [Source 1](https://github.com/dotb1ue/GenSfm/blob/main/LICENSE) [Source 2](https://github.com/dotb1ue/GenSfm/blob/main/README.md) [Source 3](https://dotb1ue.github.io/GenSfm/) [Source 4](https://huggingface.co/dotblue/GenSfm)

- **Code:** MIT
- **Weights:** MIT code and model bundle according to its current model card, with preserved TRELLIS notices. DINOv2 and optional rembg weights download separately; example images retain their source terms.
- **Commercial:** Software use follows MIT. MIT code and model bundle according to its current model card, with preserved TRELLIS notices. DINOv2 and optional rembg weights download separately; example images retain their source terms.
- **Cost:** Local GPU compute and downloads.

### Why it merits attention

Included for the documented creative workflow. A complete guide and popularity do not establish output reliability. [Source 1](https://github.com/dotb1ue/GenSfm/blob/main/README.md) [Source 2](https://dotb1ue.github.io/GenSfm/) [Source 3](https://huggingface.co/dotblue/GenSfm)

### Limitations

Inputs must show the same rigid object with usable masks. Training UV encoder/resume state is separate from the inference bundle. Reconstruction does not establish dimensional accuracy, watertightness or printability. [Source 1](https://github.com/dotb1ue/GenSfm/blob/main/README.md) [Source 2](https://dotb1ue.github.io/GenSfm/) [Source 3](https://huggingface.co/dotblue/GenSfm)

### Get the tool

- [Repository](https://github.com/dotb1ue/GenSfm)
- [Documentation](https://github.com/dotb1ue/GenSfm/blob/main/README.md)

## Digital Human Koubo

Avatars, digital humans & lip sync · Video, animation & film · AI visual dubbing and translated performance

A recently created project receiving its first full library guide; its creation is not proof of production readiness.

### Quality assessment: Quality unverified

Software licensing and a concrete creative AI use are supported. The remaining checks do not establish a recommendation.

Scope: Drafting narrated explainers and short presenter videos with reviewable generation costs and reusable editing templates.

Evidence checked: 2026-10-27. No local execution implied.

- **Open-source software license · verified:** The complete root software license was read and archived. The grant covers this project code; unresolved model, service and asset terms are disclosed separately. [Source](https://github.com/andyhuo520/digital-human-koubo/blob/main/LICENSE)
- **Creative results · documented:** The current release API lists all eight documented MP4 demo/gallery assets after a closed broken-link report. The videos remain author demonstrations; an independent Linux contact-sheet test covers only that utility, not the complete pipeline. [Source](https://github.com/andyhuo520/digital-human-koubo/blob/main/README.md) [Source](https://github.com/andyhuo520/digital-human-koubo/issues/3) [Source](https://github.com/andyhuo520/digital-human-koubo/releases/tag/v1.0.0)
- **Reproducible setup · documented:** Clone the project and register its two agent skills in a compatible local agent. Connect the separately billed Renoise service, then install ffmpeg, Python dependencies, Node and whisper.cpp/model as documented. Independent reproduction has not been established in this review. [Source](https://github.com/andyhuo520/digital-human-koubo/blob/main/README.md) [Source](https://github.com/andyhuo520/digital-human-koubo/issues/3) [Source](https://github.com/andyhuo520/digital-human-koubo/releases/tag/v1.0.0)
- **Maintenance and support · documented:** Live review archived 4 recent commits, 1 published release records and 3 recent support/PR records. Latest sampled commit: 2026-10-26. Current sampled topics include 收录通知：digital-human-koubo 已收录于 Awesome Social Media Skills; All README demo video links return 404 / Not Found. This is documented activity, not proof of sustained support or a complete blocker survey. [Source](https://github.com/andyhuo520/digital-human-koubo/commits/main) [Source](https://github.com/andyhuo520/digital-human-koubo/issues)
- **Independent use · unknown:** Reviewed official examples, the current support sample and bounded live web findings. Independent first-hand reproduction of this exact creative workflow was not established; author demonstrations are not treated as independent evidence.
- **Models, services and costs · documented:** MIT project code. Renoise/model generation is a separate paid service, Remotion has separate licensing, and optional MiMo TTS/voice/portrait inputs require their own terms and permissions. Renoise credits plus AI agent access and any optional TTS or Remotion licensing. Demo credit totals are examples, not current price guarantees. [Source](https://github.com/andyhuo520/digital-human-koubo/blob/main/README.md) [Source](https://github.com/andyhuo520/digital-human-koubo/issues/3) [Source](https://github.com/andyhuo520/digital-human-koubo/releases/tag/v1.0.0)

Documentation review only; AI Media Scout did not install or run this software. The full pipeline depends on hosted proprietary generation. Lip sync, voice matching and 15-second segment continuity can fail; author persona IDs do not work in a new account. One helper’s Linux test does not verify the full workflow.

### How it uses AI

An AI-agent pipeline that turns a reference portrait and script into talking-head clips through Renoise MCP, then performs speech checks, audio matching, captions and Remotion editing. [Source](https://github.com/andyhuo520/digital-human-koubo/blob/main/README.md) [Source](https://github.com/andyhuo520/digital-human-koubo/issues/3) [Source](https://github.com/andyhuo520/digital-human-koubo/releases/tag/v1.0.0)

### Introduction

An AI-agent pipeline that turns a reference portrait and script into talking-head clips through Renoise MCP, then performs speech checks, audio matching, captions and Remotion editing. [Source 1](https://github.com/andyhuo520/digital-human-koubo/blob/main/README.md) [Source 2](https://github.com/andyhuo520/digital-human-koubo/issues/3) [Source 3](https://github.com/andyhuo520/digital-human-koubo/releases/tag/v1.0.0)

### What it is good for

Drafting narrated explainers and short presenter videos with reviewable generation costs and reusable editing templates. [Source 1](https://github.com/andyhuo520/digital-human-koubo/blob/main/README.md) [Source 2](https://github.com/andyhuo520/digital-human-koubo/issues/3) [Source 3](https://github.com/andyhuo520/digital-human-koubo/releases/tag/v1.0.0)

### Demo & examples

The current release API lists all eight documented MP4 demo/gallery assets after a closed broken-link report. The videos remain author demonstrations; an independent Linux contact-sheet test covers only that utility, not the complete pipeline. [Source 1](https://github.com/andyhuo520/digital-human-koubo/blob/main/README.md) [Source 2](https://github.com/andyhuo520/digital-human-koubo/issues/3) [Source 3](https://github.com/andyhuo520/digital-human-koubo/releases/tag/v1.0.0)

### Install

Clone the project and register its two agent skills in a compatible local agent. Connect the separately billed Renoise service, then install ffmpeg, Python dependencies, Node and whisper.cpp/model as documented. [Source 1](https://github.com/andyhuo520/digital-human-koubo/blob/main/README.md) [Source 2](https://github.com/andyhuo520/digital-human-koubo/issues/3) [Source 3](https://github.com/andyhuo520/digital-human-koubo/releases/tag/v1.0.0)

1. Obtain the official source or release linked below.
2. Clone the project and register its two agent skills in a compatible local agent. Connect the separately billed Renoise service, then install ffmpeg, Python dependencies, Node and whisper.cpp/model as documented.

```sh
git clone https://github.com/andyhuo520/digital-human-koubo.git
```


```sh
python3 -m pip install numpy pillow
```

### First project

Start with a short, representative project and inspect the result before a larger batch. [Source 1](https://github.com/andyhuo520/digital-human-koubo/blob/main/README.md) [Source 2](https://github.com/andyhuo520/digital-human-koubo/issues/3) [Source 3](https://github.com/andyhuo520/digital-human-koubo/releases/tag/v1.0.0)

1. Create an authorized presenter reference and choose a script, format and editing style.
2. Review the service’s credit quote and one generated segment before a longer batch.
3. Inspect transcriptions, lip sync, identity, captions and transition frames before exporting.
### Hardware & software

Requirements below are documented for this workflow. Unspecified limits are not inferred. [Source 1](https://github.com/andyhuo520/digital-human-koubo/blob/main/README.md) [Source 2](https://github.com/andyhuo520/digital-human-koubo/issues/3) [Source 3](https://github.com/andyhuo520/digital-human-koubo/releases/tag/v1.0.0)

- **Hardware:** Minimum system RAM, VRAM and total disk space are not documented in the reviewed instructions.
- **Software:** An agent that supports skills, remote MCP and local commands; Python 3 with numpy/Pillow, Node 18+, ffmpeg, whisper.cpp and a downloaded speech model; Remotion 4 for editing.
- **Platforms:** macOS/Windows/Linux setup instructions are provided, but full-platform reproduction is not established. Text-behind-presenter uses Apple Vision and is macOS-specific; an open PR addresses a macOS-only font path.

### License, model weights & costs

The full software license was reviewed. Model weights, assets and services remain separate. [Source 1](https://github.com/andyhuo520/digital-human-koubo/blob/main/LICENSE) [Source 2](https://github.com/andyhuo520/digital-human-koubo/blob/main/README.md) [Source 3](https://github.com/andyhuo520/digital-human-koubo/issues/3) [Source 4](https://github.com/andyhuo520/digital-human-koubo/releases/tag/v1.0.0)

- **Code:** MIT
- **Weights:** MIT project code. Renoise/model generation is a separate paid service, Remotion has separate licensing, and optional MiMo TTS/voice/portrait inputs require their own terms and permissions.
- **Commercial:** Software use follows MIT. MIT project code. Renoise/model generation is a separate paid service, Remotion has separate licensing, and optional MiMo TTS/voice/portrait inputs require their own terms and permissions.
- **Cost:** Renoise credits plus AI agent access and any optional TTS or Remotion licensing. Demo credit totals are examples, not current price guarantees.

### Why it merits attention

Included for the documented creative workflow. A complete guide and popularity do not establish output reliability. [Source 1](https://github.com/andyhuo520/digital-human-koubo/blob/main/README.md) [Source 2](https://github.com/andyhuo520/digital-human-koubo/issues/3) [Source 3](https://github.com/andyhuo520/digital-human-koubo/releases/tag/v1.0.0)

### Limitations

The full pipeline depends on hosted proprietary generation. Lip sync, voice matching and 15-second segment continuity can fail; author persona IDs do not work in a new account. One helper’s Linux test does not verify the full workflow. The open Linux contact-sheet PR is a proposed fix, not confirmed merged behavior. [Source 1](https://github.com/andyhuo520/digital-human-koubo/blob/main/README.md) [Source 2](https://github.com/andyhuo520/digital-human-koubo/issues/3) [Source 3](https://github.com/andyhuo520/digital-human-koubo/releases/tag/v1.0.0)

### Get the tool

- [Repository](https://github.com/andyhuo520/digital-human-koubo)
- [Documentation](https://github.com/andyhuo520/digital-human-koubo/blob/main/README.md)

## Agentic Edition Studio

Video, animation & film · Editing, captions & post-production · Computational art & creative coding

A recently created project receiving its first full library guide; its creation is not proof of production readiness.

### Quality assessment: Quality unverified

Software licensing and a concrete creative AI use are supported. The remaining checks do not establish a recommendation.

Scope: Prototyping short-form edits with explicit beat tables, timestamps, per-project decisions and frame-level revision feedback.

Evidence checked: 2026-10-27. No local execution implied.

- **Open-source software license · verified:** The complete root software license was read and archived. The grant covers this project code; unresolved model, service and asset terms are disclosed separately. [Source](https://github.com/RoderickGrc/agentic-edition-studio/blob/main/LICENSE)
- **Creative results · unknown:** The project explicitly ships an empty studio and an Example composition; a completed creative edit and its quality are not established by the reviewed sources. [Source](https://github.com/RoderickGrc/agentic-edition-studio/blob/main/README.md)
- **Reproducible setup · documented:** Install Node dependencies, prepare Python for the bundled sureshot tools and follow the guided setup plan for ffmpeg, speech and OCR. Gemini is optional for timeline summaries, not required for every analysis step. Independent reproduction has not been established in this review. [Source](https://github.com/RoderickGrc/agentic-edition-studio/blob/main/README.md)
- **Maintenance and support · documented:** Live review archived 2 recent commits, 0 published release records and 0 recent support/PR records. Latest sampled commit: 2026-10-24. The bounded support sample did not establish third-party resolution history. This is documented activity, not proof of sustained support or a complete blocker survey. [Source](https://github.com/RoderickGrc/agentic-edition-studio/commits/main) [Source](https://github.com/RoderickGrc/agentic-edition-studio/issues)
- **Independent use · unknown:** Reviewed official examples, the current support sample and bounded live web findings. Independent first-hand reproduction of this exact creative workflow was not established; author demonstrations are not treated as independent evidence.
- **Models, services and costs · documented:** MIT starter code. Remotion, speech/OCR models, external coding agents and optional Gemini retain separate terms. No third-party sound assets are included. Local processing plus chosen AI-agent/model access and any applicable Remotion license; optional API charges depend on account. [Source](https://github.com/RoderickGrc/agentic-edition-studio/blob/main/README.md)

Documentation review only; AI Media Scout did not install or run this software. An intentionally empty starter is not a ready-made film pipeline: project judgment/wiki material and sound assets must be supplied. Automated render completion does not prove editing quality or synchronization.

### How it uses AI

A starter workspace for AI-agent video editing that turns speech, OCR, cuts and motion into a timed evidence map, then creates reviewable Remotion compositions. [Source](https://github.com/RoderickGrc/agentic-edition-studio/blob/main/README.md)

### Introduction

A starter workspace for AI-agent video editing that turns speech, OCR, cuts and motion into a timed evidence map, then creates reviewable Remotion compositions. [Source 1](https://github.com/RoderickGrc/agentic-edition-studio/blob/main/README.md)

### What it is good for

Prototyping short-form edits with explicit beat tables, timestamps, per-project decisions and frame-level revision feedback. [Source 1](https://github.com/RoderickGrc/agentic-edition-studio/blob/main/README.md)

### Demo & examples

The starter includes an Example composition at 1080×1920, 30 fps and 150 frames. It explicitly contains no finished creative videos or sound library, so it does not demonstrate a complete successful edit. [Source 1](https://github.com/RoderickGrc/agentic-edition-studio/blob/main/README.md)

### Install

Install Node dependencies, prepare Python for the bundled sureshot tools and follow the guided setup plan for ffmpeg, speech and OCR. Gemini is optional for timeline summaries, not required for every analysis step. [Source 1](https://github.com/RoderickGrc/agentic-edition-studio/blob/main/README.md)

1. Obtain the official source or release linked below.
2. Install Node dependencies, prepare Python for the bundled sureshot tools and follow the guided setup plan for ffmpeg, speech and OCR. Gemini is optional for timeline summaries, not required for every analysis step.

```sh
npm install
```


```sh
npm run dev
```


```sh
python .agents/skills/sureshot/scripts/sureshot.py setup --plan
```


```sh
npm run new -- my-reel --width 1080 --height 1920 --fps 30 --frames 150
```

### First project

Start with a short, representative project and inspect the result before a larger batch. [Source 1](https://github.com/RoderickGrc/agentic-edition-studio/blob/main/README.md)

1. Create a project and add source media with known rights.
2. Analyze speech/OCR/cuts, have the agent create an edit and record its decisions.
3. Review the render for pacing, missing footage and sync; feed back frame-specific corrections.
### Hardware & software

Requirements below are documented for this workflow. Unspecified limits are not inferred. [Source 1](https://github.com/RoderickGrc/agentic-edition-studio/blob/main/README.md)

- **Hardware:** Minimum system RAM, VRAM and total disk space are not documented in the reviewed instructions.
- **Software:** Node 18+ and Windows with Python 3.10–3.13. ffmpeg, speech tools, Tesseract by default and optional PaddleOCR; numpy for sound utilities.
- **Platforms:** Windows is the documented target. Mac/Linux equivalence and GPU minima are not established.

### License, model weights & costs

The full software license was reviewed. Model weights, assets and services remain separate. [Source 1](https://github.com/RoderickGrc/agentic-edition-studio/blob/main/LICENSE) [Source 2](https://github.com/RoderickGrc/agentic-edition-studio/blob/main/README.md)

- **Code:** MIT
- **Weights:** MIT starter code. Remotion, speech/OCR models, external coding agents and optional Gemini retain separate terms. No third-party sound assets are included.
- **Commercial:** Software use follows MIT. MIT starter code. Remotion, speech/OCR models, external coding agents and optional Gemini retain separate terms. No third-party sound assets are included.
- **Cost:** Local processing plus chosen AI-agent/model access and any applicable Remotion license; optional API charges depend on account.

### Why it merits attention

Included for the documented creative workflow. A complete guide and popularity do not establish output reliability. [Source 1](https://github.com/RoderickGrc/agentic-edition-studio/blob/main/README.md)

### Limitations

An intentionally empty starter is not a ready-made film pipeline: project judgment/wiki material and sound assets must be supplied. Automated render completion does not prove editing quality or synchronization. [Source 1](https://github.com/RoderickGrc/agentic-edition-studio/blob/main/README.md)

### Get the tool

- [Repository](https://github.com/RoderickGrc/agentic-edition-studio)
- [Documentation](https://github.com/RoderickGrc/agentic-edition-studio/blob/main/README.md)

## Chromary

AI color direction and palette-based media · Browser tools & web media · Data art & scientific visualization

A recently created project receiving its first full library guide; its creation is not proof of production readiness.

### Quality assessment: Quality unverified

Software licensing and a concrete creative AI use are supported. The remaining checks do not establish a recommendation.

Scope: Helping an AI assistant construct color themes, inspect contrast and choose palettes for web interfaces, charts and game art.

Evidence checked: 2026-10-27. No local execution implied.

- **Open-source software license · verified:** The complete root software license was read and archived. The grant covers this project code; unresolved model, service and asset terms are disclosed separately. [Source](https://github.com/izynu/chromary/blob/main/LICENSE)
- **Creative results · documented:** The official Chroma Lab and screenshot examples demonstrate palette/contrast controls. They do not independently validate every guide, accessibility claim or agent-generated theme. [Source](https://github.com/izynu/chromary/blob/main/README.md)
- **Reproducible setup · documented:** Clone the repository, add the selected skill folders to a compatible AI agent, or install the Bun dependencies in mcp/example-color-server and configure that server in the agent. The static playground opens locally without a build. Independent reproduction has not been established in this review. [Source](https://github.com/izynu/chromary/blob/main/README.md)
- **Maintenance and support · documented:** Live review archived 10 recent commits, 0 published release records and 0 recent support/PR records. Latest sampled commit: 2026-10-25. The bounded support sample did not establish third-party resolution history. This is documented activity, not proof of sustained support or a complete blocker survey. [Source](https://github.com/izynu/chromary/commits/main) [Source](https://github.com/izynu/chromary/issues)
- **Independent use · unknown:** Reviewed official examples, the current support sample and bounded live web findings. Independent first-hand reproduction of this exact creative workflow was not established; author demonstrations are not treated as independent evidence.
- **Models, services and costs · documented:** MIT toolkit. The Color API and any other linked services, external models, color standards and third-party recipe libraries keep their own terms. Local playground/recipes plus the chosen agent and any called external services; no guaranteed free service availability. [Source](https://github.com/izynu/chromary/blob/main/README.md)

Documentation review only; AI Media Scout did not install or run this software. Much of the package is educational/reference material; the concrete AI role is agent skills plus callable color tools. APCA experiments are not interchangeable with current WCAG conformance, and print/cultural palette tools listed on the roadmap are future work.

### How it uses AI

A color-engineering toolkit with AI-agent skills and a runnable MCP server for computing palettes and color information, plus deterministic design recipes and an offline playground. [Source](https://github.com/izynu/chromary/blob/main/README.md)

### Introduction

A color-engineering toolkit with AI-agent skills and a runnable MCP server for computing palettes and color information, plus deterministic design recipes and an offline playground. [Source 1](https://github.com/izynu/chromary/blob/main/README.md)

### What it is good for

Helping an AI assistant construct color themes, inspect contrast and choose palettes for web interfaces, charts and game art. [Source 1](https://github.com/izynu/chromary/blob/main/README.md)

### Demo & examples

The official Chroma Lab and screenshot examples demonstrate palette/contrast controls. They do not independently validate every guide, accessibility claim or agent-generated theme. [Source 1](https://github.com/izynu/chromary/blob/main/README.md)

### Install

Clone the repository, add the selected skill folders to a compatible AI agent, or install the Bun dependencies in mcp/example-color-server and configure that server in the agent. The static playground opens locally without a build. [Source 1](https://github.com/izynu/chromary/blob/main/README.md)

1. Obtain the official source or release linked below.
2. Clone the repository, add the selected skill folders to a compatible AI agent, or install the Bun dependencies in mcp/example-color-server and configure that server in the agent. The static playground opens locally without a build.

```sh
bun install
```


```sh
bun run index.ts
```

### First project

Start with a short, representative project and inspect the result before a larger batch. [Source 1](https://github.com/izynu/chromary/blob/main/README.md)

1. Start with a small brand palette or chart and select the relevant agent skill.
2. Use computed color/contrast results rather than relying on names alone.
3. Check generated colors in the actual layout and viewing conditions; print matching and newer roadmap skills are not shipped guarantees.
### Hardware & software

Requirements below are documented for this workflow. Unspecified limits are not inferred. [Source 1](https://github.com/izynu/chromary/blob/main/README.md)

- **Hardware:** Minimum system RAM, VRAM and total disk space are not documented in the reviewed instructions.
- **Software:** Bun for the example TypeScript MCP server; a compatible AI agent for the AI workflow. The static HTML playground needs only a browser. Minimum Bun/OS versions are not stated.
- **Platforms:** Browser playground and agent integrations; no complete tested desktop OS matrix is provided.

### License, model weights & costs

The full software license was reviewed. Model weights, assets and services remain separate. [Source 1](https://github.com/izynu/chromary/blob/main/LICENSE) [Source 2](https://github.com/izynu/chromary/blob/main/README.md)

- **Code:** MIT
- **Weights:** MIT toolkit. The Color API and any other linked services, external models, color standards and third-party recipe libraries keep their own terms.
- **Commercial:** Software use follows MIT. MIT toolkit. The Color API and any other linked services, external models, color standards and third-party recipe libraries keep their own terms.
- **Cost:** Local playground/recipes plus the chosen agent and any called external services; no guaranteed free service availability.

### Why it merits attention

Included for the documented creative workflow. A complete guide and popularity do not establish output reliability. [Source 1](https://github.com/izynu/chromary/blob/main/README.md)

### Limitations

Much of the package is educational/reference material; the concrete AI role is agent skills plus callable color tools. APCA experiments are not interchangeable with current WCAG conformance, and print/cultural palette tools listed on the roadmap are future work. [Source 1](https://github.com/izynu/chromary/blob/main/README.md)

### Get the tool

- [Repository](https://github.com/izynu/chromary)
- [Documentation](https://github.com/izynu/chromary/blob/main/README.md)

## LTSeries

Storyboarding, narrative & comics · Video, animation & film · Images & design

A recently created project receiving its first full library guide; its creation is not proof of production readiness.

### Quality assessment: Experimental

Software licensing and a concrete creative AI use are supported. The remaining checks do not establish a recommendation.

Scope: Managing short-drama or comic-series preproduction and inspecting shot-by-shot generation histories.

Evidence checked: 2026-10-27. No local execution implied.

Why Experimental: The current source identifies early-stage software with unfinished media archival, approval states and team controls for its production workflow. https://github.com/eust-w/ltseries/blob/main/README.md

- **Open-source software license · verified:** The complete root software license was read and archived. The grant covers this project code; unresolved model, service and asset terms are disclosed separately. [Source](https://github.com/eust-w/ltseries/blob/main/LICENSE)
- **Creative results · documented:** Official narrated walkthroughs show real application captures and provider outputs. The walkthrough is edited, its TTS narration is postproduction, and the older six-shot film is separate from current screenshots. [Source](https://github.com/eust-w/ltseries/blob/main/README.md)
- **Reproducible setup · documented:** Clone, configure the root environment with provider credentials, a strong admin password and session secret, retain authentication, then start Docker Compose. The stack includes MongoDB, Go API/FFmpeg and React UI. Independent reproduction has not been established in this review. [Source](https://github.com/eust-w/ltseries/blob/main/README.md)
- **Maintenance and support · documented:** Live review archived 3 recent commits, 1 published release records and 0 recent support/PR records. Latest sampled commit: 2026-10-24. The bounded support sample did not establish third-party resolution history. This is documented activity, not proof of sustained support or a complete blocker survey. [Source](https://github.com/eust-w/ltseries/commits/main) [Source](https://github.com/eust-w/ltseries/issues)
- **Independent use · unknown:** Reviewed official examples, the current support sample and bounded live web findings. Independent first-hand reproduction of this exact creative workflow was not established; author demonstrations are not treated as independent evidence.
- **Models, services and costs · documented:** MIT project software. MongoDB, provider APIs and generated-media conditions are separate. DashScope/model access is required for the documented cloud workflow; audio needs its own configured endpoint. Local hosting plus paid external model/API usage; self-hosting does not make inference free. [Source](https://github.com/eust-w/ltseries/blob/main/README.md)

Documentation review only; AI Media Scout did not install or run this software. Current documentation calls this early-stage software for trusted teams. Approve/reject states, permanent media archival, English UI and richer audio are roadmap items. Metadata scores do not measure visual consistency, and cloud providers cannot fetch private localhost reference URLs.

### How it uses AI

A self-hosted AI production workspace that uses an LLM and image/video providers to turn scripts into art direction, reusable references, storyboards, shot variants and assembled videos. [Source](https://github.com/eust-w/ltseries/blob/main/README.md)

### Introduction

A self-hosted AI production workspace that uses an LLM and image/video providers to turn scripts into art direction, reusable references, storyboards, shot variants and assembled videos. [Source 1](https://github.com/eust-w/ltseries/blob/main/README.md)

### What it is good for

Managing short-drama or comic-series preproduction and inspecting shot-by-shot generation histories. [Source 1](https://github.com/eust-w/ltseries/blob/main/README.md)

### Demo & examples

Official narrated walkthroughs show real application captures and provider outputs. The walkthrough is edited, its TTS narration is postproduction, and the older six-shot film is separate from current screenshots. [Source 1](https://github.com/eust-w/ltseries/blob/main/README.md)

### Install

Clone, configure the root environment with provider credentials, a strong admin password and session secret, retain authentication, then start Docker Compose. The stack includes MongoDB, Go API/FFmpeg and React UI. [Source 1](https://github.com/eust-w/ltseries/blob/main/README.md)

1. Obtain the official source or release linked below.
2. Clone, configure the root environment with provider credentials, a strong admin password and session secret, retain authentication, then start Docker Compose. The stack includes MongoDB, Go API/FFmpeg and React UI.

```sh
cp .env.example .env
```


```sh
docker compose up -d --build
```


```sh
docker compose ps
```

### First project

Start with a short, representative project and inspect the result before a larger batch. [Source 1](https://github.com/eust-w/ltseries/blob/main/README.md)

1. Open the local UI on port 3108 and analyze a short script.
2. Review art direction and references, generate first frames and a few shot takes, checking each billable request.
3. Assemble selected clips after checking continuity and media-link availability.
### Hardware & software

Requirements below are documented for this workflow. Unspecified limits are not inferred. [Source 1](https://github.com/eust-w/ltseries/blob/main/README.md)

- **Hardware:** Minimum system RAM, VRAM and total disk space are not documented in the reviewed instructions.
- **Software:** Docker with Compose and enabled provider models; source development uses Go 1.24+, Node 22.12+, MongoDB 7 and FFmpeg.
- **Platforms:** Self-hosted browser UI; no complete tested Mac/Windows/Linux deployment matrix is documented. Primarily Chinese interface.

### License, model weights & costs

The full software license was reviewed. Model weights, assets and services remain separate. [Source 1](https://github.com/eust-w/ltseries/blob/main/LICENSE) [Source 2](https://github.com/eust-w/ltseries/blob/main/README.md)

- **Code:** MIT
- **Weights:** MIT project software. MongoDB, provider APIs and generated-media conditions are separate. DashScope/model access is required for the documented cloud workflow; audio needs its own configured endpoint.
- **Commercial:** Software use follows MIT. MIT project software. MongoDB, provider APIs and generated-media conditions are separate. DashScope/model access is required for the documented cloud workflow; audio needs its own configured endpoint.
- **Cost:** Local hosting plus paid external model/API usage; self-hosting does not make inference free.

### Why it merits attention

Included for the documented creative workflow. A complete guide and popularity do not establish output reliability. [Source 1](https://github.com/eust-w/ltseries/blob/main/README.md)

### Limitations

Current documentation calls this early-stage software for trusted teams. Approve/reject states, permanent media archival, English UI and richer audio are roadmap items. Metadata scores do not measure visual consistency, and cloud providers cannot fetch private localhost reference URLs. [Source 1](https://github.com/eust-w/ltseries/blob/main/README.md)

### Get the tool

- [Repository](https://github.com/eust-w/ltseries)
- [Documentation](https://github.com/eust-w/ltseries/blob/main/README.md)

## CutVii

Video, animation & film · Editing, captions & post-production · Accessible media & assistive creation

A recently created project receiving its first full library guide; its creation is not proof of production readiness.

### Quality assessment: Quality unverified

Software licensing and a concrete creative AI use are supported. The remaining checks do not establish a recommendation.

Scope: Preparing short captioned videos while retaining local media and reviewing suggested clips manually.

Evidence checked: 2026-10-27. No local execution implied.

- **Open-source software license · verified:** The complete root software license was read and archived. The grant covers this project code; unresolved model, service and asset terms are disclosed separately. [Source](https://github.com/zidniryi/cutvii/blob/main/LICENSE)
- **Creative results · documented:** Official 1.0.3 screenshots show a pumpkin-video edit with captions, voice-over, upscale and auto clips. The separate smoke-test document records earlier macOS live exports but says Windows/Linux human runs were not completed. [Source](https://github.com/zidniryi/cutvii/blob/main/README.md) [Source](https://github.com/zidniryi/cutvii/blob/main/docs/smoke-tests.md) [Source](https://github.com/zidniryi/cutvii/blob/main/docs/licensing.md)
- **Reproducible setup · documented:** Use the official platform release or build with Node 22+, pnpm 10+, Rust 1.85+ and the Tauri prerequisites. Installers describe bundled FFmpeg; source builds require an appropriate FFmpeg/FFprobe. Independent reproduction has not been established in this review. [Source](https://github.com/zidniryi/cutvii/blob/main/README.md) [Source](https://github.com/zidniryi/cutvii/blob/main/docs/smoke-tests.md) [Source](https://github.com/zidniryi/cutvii/blob/main/docs/licensing.md)
- **Maintenance and support · documented:** Live review archived 10 recent commits, 4 published release records and 0 recent support/PR records. Latest sampled commit: 2026-10-23. The bounded support sample did not establish third-party resolution history. This is documented activity, not proof of sustained support or a complete blocker survey. [Source](https://github.com/zidniryi/cutvii/commits/main) [Source](https://github.com/zidniryi/cutvii/issues)
- **Independent use · unknown:** Reviewed official examples, the current support sample and bounded live web findings. Independent first-hand reproduction of this exact creative workflow was not established; author demonstrations are not treated as independent evidence.
- **Models, services and costs · documented:** MIT editor code, separate GPL FFmpeg binaries and OFL/Apache font notices. The reviewed licensing page does not comprehensively settle every current AI weight/runtime, so those terms remain an evidence gap. Local computation and model downloads; no required paid cloud account is documented. [Source](https://github.com/zidniryi/cutvii/blob/main/README.md) [Source](https://github.com/zidniryi/cutvii/blob/main/docs/smoke-tests.md) [Source](https://github.com/zidniryi/cutvii/blob/main/docs/licensing.md)

Documentation review only; AI Media Scout did not install or run this software. README claims and older smoke/licensing notes are not fully aligned about packaged testing. Caption accuracy, upscale fidelity and clip selection need actual output review; source badges alone do not prove platform usability.

### How it uses AI

A local desktop video editor with on-device speech-based subtitles and documented voice-over, AI upscaling and clip-selection workflows alongside a multitrack timeline. [Source](https://github.com/zidniryi/cutvii/blob/main/README.md) [Source](https://github.com/zidniryi/cutvii/blob/main/docs/smoke-tests.md) [Source](https://github.com/zidniryi/cutvii/blob/main/docs/licensing.md)

### Introduction

A local desktop video editor with on-device speech-based subtitles and documented voice-over, AI upscaling and clip-selection workflows alongside a multitrack timeline. [Source 1](https://github.com/zidniryi/cutvii/blob/main/README.md) [Source 2](https://github.com/zidniryi/cutvii/blob/main/docs/smoke-tests.md) [Source 3](https://github.com/zidniryi/cutvii/blob/main/docs/licensing.md)

### What it is good for

Preparing short captioned videos while retaining local media and reviewing suggested clips manually. [Source 1](https://github.com/zidniryi/cutvii/blob/main/README.md) [Source 2](https://github.com/zidniryi/cutvii/blob/main/docs/smoke-tests.md) [Source 3](https://github.com/zidniryi/cutvii/blob/main/docs/licensing.md)

### Demo & examples

Official 1.0.3 screenshots show a pumpkin-video edit with captions, voice-over, upscale and auto clips. The separate smoke-test document records earlier macOS live exports but says Windows/Linux human runs were not completed. [Source 1](https://github.com/zidniryi/cutvii/blob/main/README.md) [Source 2](https://github.com/zidniryi/cutvii/blob/main/docs/smoke-tests.md) [Source 3](https://github.com/zidniryi/cutvii/blob/main/docs/licensing.md)

### Install

Use the official platform release or build with Node 22+, pnpm 10+, Rust 1.85+ and the Tauri prerequisites. Installers describe bundled FFmpeg; source builds require an appropriate FFmpeg/FFprobe. [Source 1](https://github.com/zidniryi/cutvii/blob/main/README.md) [Source 2](https://github.com/zidniryi/cutvii/blob/main/docs/smoke-tests.md) [Source 3](https://github.com/zidniryi/cutvii/blob/main/docs/licensing.md)

1. Obtain the official source or release linked below.
2. Use the official platform release or build with Node 22+, pnpm 10+, Rust 1.85+ and the Tauri prerequisites. Installers describe bundled FFmpeg; source builds require an appropriate FFmpeg/FFprobe.

```sh
pnpm install
```


```sh
pnpm tauri dev
```

### First project

Start with a short, representative project and inspect the result before a larger batch. [Source 1](https://github.com/zidniryi/cutvii/blob/main/README.md) [Source 2](https://github.com/zidniryi/cutvii/blob/main/docs/smoke-tests.md) [Source 3](https://github.com/zidniryi/cutvii/blob/main/docs/licensing.md)

1. Import a short clip and check playback before editing.
2. Generate and proofread subtitles; review any upscale or auto-clip suggestion against the source.
3. Export a short MP4 and inspect sync, transitions and missing media in a separate player.
### Hardware & software

Requirements below are documented for this workflow. Unspecified limits are not inferred. [Source 1](https://github.com/zidniryi/cutvii/blob/main/README.md) [Source 2](https://github.com/zidniryi/cutvii/blob/main/docs/smoke-tests.md) [Source 3](https://github.com/zidniryi/cutvii/blob/main/docs/licensing.md)

- **Hardware:** Minimum system RAM, VRAM and total disk space are not documented in the reviewed instructions.
- **Software:** Node 22+, pnpm 10+, Rust 1.85+, FFmpeg/FFprobe 6+ for development and OS-specific Tauri dependencies. Neural features require additional model/runtime assets.
- **Platforms:** macOS Apple-silicon packages; Windows/Linux packages are advertised but the smoke-test document still lists their human runtime validation as incomplete. Intel Mac has no packaged build; Linux preview depends on GStreamer codecs.

### License, model weights & costs

The full software license was reviewed. Model weights, assets and services remain separate. [Source 1](https://github.com/zidniryi/cutvii/blob/main/LICENSE) [Source 2](https://github.com/zidniryi/cutvii/blob/main/README.md) [Source 3](https://github.com/zidniryi/cutvii/blob/main/docs/smoke-tests.md) [Source 4](https://github.com/zidniryi/cutvii/blob/main/docs/licensing.md)

- **Code:** MIT
- **Weights:** MIT editor code, separate GPL FFmpeg binaries and OFL/Apache font notices. The reviewed licensing page does not comprehensively settle every current AI weight/runtime, so those terms remain an evidence gap.
- **Commercial:** Software use follows MIT. MIT editor code, separate GPL FFmpeg binaries and OFL/Apache font notices. The reviewed licensing page does not comprehensively settle every current AI weight/runtime, so those terms remain an evidence gap.
- **Cost:** Local computation and model downloads; no required paid cloud account is documented.

### Why it merits attention

Included for the documented creative workflow. A complete guide and popularity do not establish output reliability. [Source 1](https://github.com/zidniryi/cutvii/blob/main/README.md) [Source 2](https://github.com/zidniryi/cutvii/blob/main/docs/smoke-tests.md) [Source 3](https://github.com/zidniryi/cutvii/blob/main/docs/licensing.md)

### Limitations

README claims and older smoke/licensing notes are not fully aligned about packaged testing. Caption accuracy, upscale fidelity and clip selection need actual output review; source badges alone do not prove platform usability. [Source 1](https://github.com/zidniryi/cutvii/blob/main/README.md) [Source 2](https://github.com/zidniryi/cutvii/blob/main/docs/smoke-tests.md) [Source 3](https://github.com/zidniryi/cutvii/blob/main/docs/licensing.md)

### Get the tool

- [Repository](https://github.com/zidniryi/cutvii)
- [Documentation](https://github.com/zidniryi/cutvii/blob/main/README.md)

## Remiqora Video

Video, animation & film · Storyboarding, narrative & comics · Editing, captions & post-production

A recently created project receiving its first full library guide; its creation is not proof of production readiness.

### Quality assessment: Experimental

Software licensing and a concrete creative AI use are supported. The remaining checks do not establish a recommendation.

Scope: Experimenting with multi-scene films, music-video drafts and alternative story branches without a hosted generation service.

Evidence checked: 2026-10-27. No local execution implied.

Why Experimental: The current 0.1.0 is explicitly not stable and warns of breaking changes, bugs and rough edges throughout the local film workflow. https://github.com/inikolax/remiqora-video/blob/master/README.md

- **Open-source software license · verified:** The complete root software license was read and archived. The grant covers this project code; unresolved model, service and asset terms are disclosed separately. [Source](https://github.com/inikolax/remiqora-video/blob/master/LICENSE)
- **Creative results · documented:** The official screenshots show idea, storyboard, montage, graph and installer flows. Author timings are measured on an RTX 4080 16 GB and do not establish general runtime or film quality. [Source](https://github.com/inikolax/remiqora-video/blob/master/README.md)
- **Reproducible setup · documented:** Use the official 0.1.0 prerelease installer or clone and run install.bat. Choose model sets, verify their terms and prepare adequate disk space; the source route also needs a local llama-server for the writer. Independent reproduction has not been established in this review. [Source](https://github.com/inikolax/remiqora-video/blob/master/README.md)
- **Maintenance and support · documented:** Live review archived 1 recent commits, 1 published release records and 0 recent support/PR records. Latest sampled commit: 2026-10-26. The bounded support sample did not establish third-party resolution history. This is documented activity, not proof of sustained support or a complete blocker survey. [Source](https://github.com/inikolax/remiqora-video/commits/master) [Source](https://github.com/inikolax/remiqora-video/issues)
- **Independent use · unknown:** Reviewed official examples, the current support sample and bounded live web findings. Independent first-hand reproduction of this exact creative workflow was not established; author demonstrations are not treated as independent evidence.
- **Models, services and costs · documented:** GPL-3.0 project code. MiniMax H3, LTX and Krea weights have separate community licenses; WAN’s listed Apache-2.0 terms do not transfer to the other models. NVIDIA SDK files and any chosen GGUF weights retain their own conditions. Local GPU compute and large downloads; gated model acceptance and model-specific commercial terms still apply. [Source](https://github.com/inikolax/remiqora-video/blob/master/README.md)

Documentation review only; AI Media Scout did not install or run this software. The current release explicitly warns of breaking changes, bugs and rough edges. Models share the GPU sequentially; character identity drifts over long chains, music may vary by scene, and unsigned packaging has compatibility limits.

### How it uses AI

A local Windows/NVIDIA studio that uses a local language model for storyboards and ComfyUI-core video models for scene generation, continuation, montage and finishing. [Source](https://github.com/inikolax/remiqora-video/blob/master/README.md)

### Introduction

A local Windows/NVIDIA studio that uses a local language model for storyboards and ComfyUI-core video models for scene generation, continuation, montage and finishing. [Source 1](https://github.com/inikolax/remiqora-video/blob/master/README.md)

### What it is good for

Experimenting with multi-scene films, music-video drafts and alternative story branches without a hosted generation service. [Source 1](https://github.com/inikolax/remiqora-video/blob/master/README.md)

### Demo & examples

The official screenshots show idea, storyboard, montage, graph and installer flows. Author timings are measured on an RTX 4080 16 GB and do not establish general runtime or film quality. [Source 1](https://github.com/inikolax/remiqora-video/blob/master/README.md)

### Install

Use the official 0.1.0 prerelease installer or clone and run install.bat. Choose model sets, verify their terms and prepare adequate disk space; the source route also needs a local llama-server for the writer. [Source 1](https://github.com/inikolax/remiqora-video/blob/master/README.md)

1. Obtain the official source or release linked below.
2. Use the official 0.1.0 prerelease installer or clone and run install.bat. Choose model sets, verify their terms and prepare adequate disk space; the source route also needs a local llama-server for the writer.

```sh
install.bat
```


```sh
dev.bat
```

### First project

Start with a short, representative project and inspect the result before a larger batch. [Source 1](https://github.com/inikolax/remiqora-video/blob/master/README.md)

1. Install a single model set and generate one short scene from an editable storyboard.
2. Inspect face drift, continuity, sound and generated text before chaining scenes.
3. Use montage edits or FCPXML export, then review the final output independently of automatic quality checks.
### Hardware & software

Requirements below are documented for this workflow. Unspecified limits are not inferred. [Source 1](https://github.com/inikolax/remiqora-video/blob/master/README.md)

- **Hardware:** Targets 16 GB NVIDIA VRAM; author test was RTX 4080 with 62 GB RAM, not a stated minimum RAM requirement. H3+writer about 53 GB of weights, all sets about 196 GB, plus roughly 6 GB engine and other assets.
- **Software:** Windows 11, NVIDIA driver 580+ per installer; source prerequisites include Python 3.13, uv, Node, FFmpeg and pinned ComfyUI core. NVIDIA RTX Video SDK is separate for some finishing routes.
- **Platforms:** Windows/NVIDIA only in the current documentation. Mac, AMD and Linux inference support are not established.

### License, model weights & costs

The full software license was reviewed. Model weights, assets and services remain separate. [Source 1](https://github.com/inikolax/remiqora-video/blob/master/LICENSE) [Source 2](https://github.com/inikolax/remiqora-video/blob/master/README.md)

- **Code:** GPL-3.0
- **Weights:** GPL-3.0 project code. MiniMax H3, LTX and Krea weights have separate community licenses; WAN’s listed Apache-2.0 terms do not transfer to the other models. NVIDIA SDK files and any chosen GGUF weights retain their own conditions.
- **Commercial:** Software use follows GPL-3.0. GPL-3.0 project code. MiniMax H3, LTX and Krea weights have separate community licenses; WAN’s listed Apache-2.0 terms do not transfer to the other models. NVIDIA SDK files and any chosen GGUF weights retain their own conditions.
- **Cost:** Local GPU compute and large downloads; gated model acceptance and model-specific commercial terms still apply.

### Why it merits attention

Included for the documented creative workflow. A complete guide and popularity do not establish output reliability. [Source 1](https://github.com/inikolax/remiqora-video/blob/master/README.md)

### Limitations

The current release explicitly warns of breaking changes, bugs and rough edges. Models share the GPU sequentially; character identity drifts over long chains, music may vary by scene, and unsigned packaging has compatibility limits. [Source 1](https://github.com/inikolax/remiqora-video/blob/master/README.md)

### Get the tool

- [Repository](https://github.com/inikolax/remiqora-video)
- [Documentation](https://github.com/inikolax/remiqora-video/blob/master/README.md)

## Pulsar music language

Audio, music & voice · Computational art & creative coding · AI assisted audio plugin and DSP authoring

A recently created project receiving its first full library guide; its creation is not proof of production readiness.

### Quality assessment: Quality unverified

Software licensing and a concrete creative AI use are supported. The remaining checks do not establish a recommendation.

Scope: Composing electronic-music sketches with inspectable notes, automation and stems, and iterating on measurable mix problems.

Evidence checked: 2026-10-27. No local execution implied.

- **Open-source software license · verified:** The complete root software license was read and archived. The grant covers this project code; unresolved model, service and asset terms are disclosed separately. [Source](https://github.com/ronreiter/pulsar/blob/main/LICENSE)
- **Creative results · documented:** The official listening page links agent-written deep-house/techno examples and their .pulse sources. Mix reports describe signal properties; they cannot replace human judgment of musical quality. [Source](https://github.com/ronreiter/pulsar/blob/main/README.md) [Source](https://ronreiter.github.io/pulsar/#listen)
- **Reproducible setup · documented:** On macOS or Linux, clone the repository and create the documented Python environment with MCP/voice extras. ffmpeg is needed for MP3 export; the voice model downloads on first use. Independent reproduction has not been established in this review. [Source](https://github.com/ronreiter/pulsar/blob/main/README.md) [Source](https://ronreiter.github.io/pulsar/#listen)
- **Maintenance and support · documented:** Live review archived 10 recent commits, 0 published release records and 0 recent support/PR records. Latest sampled commit: 2026-10-25. The bounded support sample did not establish third-party resolution history. This is documented activity, not proof of sustained support or a complete blocker survey. [Source](https://github.com/ronreiter/pulsar/commits/main) [Source](https://github.com/ronreiter/pulsar/issues)
- **Independent use · unknown:** Reviewed official examples, the current support sample and bounded live web findings. Independent first-hand reproduction of this exact creative workflow was not established; author demonstrations are not treated as independent evidence.
- **Models, services and costs · documented:** GPL-3.0 software with DawDreamer and Faust dependency terms. Kokoro weights/voices, reference recordings and the external AI composer have separate terms. Local rendering plus chosen AI-agent access; no required paid music-generation endpoint is documented. [Source](https://github.com/ronreiter/pulsar/blob/main/README.md) [Source](https://ronreiter.github.io/pulsar/#listen)

Documentation review only; AI Media Scout did not install or run this software. Numerical tonal balance or masking feedback does not prove a satisfying composition. Neural singing repitches word-level speech and needs audition; it is not a guarantee of natural singing.

### How it uses AI

A music-as-code system designed for AI agents to write arrangements, render audio and revise against mix measurements; an optional Kokoro neural-voice path adds speaking or pitched vocal lines. [Source](https://github.com/ronreiter/pulsar/blob/main/README.md) [Source](https://ronreiter.github.io/pulsar/#listen)

### Introduction

A music-as-code system designed for AI agents to write arrangements, render audio and revise against mix measurements; an optional Kokoro neural-voice path adds speaking or pitched vocal lines. [Source 1](https://github.com/ronreiter/pulsar/blob/main/README.md) [Source 2](https://ronreiter.github.io/pulsar/#listen)

### What it is good for

Composing electronic-music sketches with inspectable notes, automation and stems, and iterating on measurable mix problems. [Source 1](https://github.com/ronreiter/pulsar/blob/main/README.md) [Source 2](https://ronreiter.github.io/pulsar/#listen)

### Demo & examples

The official listening page links agent-written deep-house/techno examples and their .pulse sources. Mix reports describe signal properties; they cannot replace human judgment of musical quality. [Source 1](https://github.com/ronreiter/pulsar/blob/main/README.md) [Source 2](https://ronreiter.github.io/pulsar/#listen)

### Install

On macOS or Linux, clone the repository and create the documented Python environment with MCP/voice extras. ffmpeg is needed for MP3 export; the voice model downloads on first use. [Source 1](https://github.com/ronreiter/pulsar/blob/main/README.md) [Source 2](https://ronreiter.github.io/pulsar/#listen)

1. Obtain the official source or release linked below.
2. On macOS or Linux, clone the repository and create the documented Python environment with MCP/voice extras. ffmpeg is needed for MP3 export; the voice model downloads on first use.

```sh
uv venv --python 3.12 .venv
```


```sh
uv pip install --python .venv/bin/python -e ".[mcp,voice,dev]"
```


```sh
.venv/bin/pulsar check examples/deep_house_agent.pulse
```


```sh
.venv/bin/pulsar render examples/deep_house_agent.pulse -o demo.mp3
```

### First project

Start with a short, representative project and inspect the result before a larger batch. [Source 1](https://github.com/ronreiter/pulsar/blob/main/README.md) [Source 2](https://ronreiter.github.io/pulsar/#listen)

1. Render a supplied arrangement and listen while comparing the mix report.
2. Ask an agent to change one section, instrument or automation curve, then render again.
3. Inspect stems, loudness and vocal intelligibility before using a piece in a creative production.
### Hardware & software

Requirements below are documented for this workflow. Unspecified limits are not inferred. [Source 1](https://github.com/ronreiter/pulsar/blob/main/README.md) [Source 2](https://ronreiter.github.io/pulsar/#listen)

- **Hardware:** The optional voice model is about 350 MB. Minimum system RAM, VRAM and total disk space are not documented.
- **Software:** Python 3.10+; example install uses Python 3.12/uv. DawDreamer/Faust synthesis, ffmpeg for MP3 and optional Kokoro voice dependencies. Native Studio requires Xcode command-line tools.
- **Platforms:** macOS and Linux for the CLI; native Pulsar Studio is macOS-specific. Windows support is not documented.

### License, model weights & costs

The full software license was reviewed. Model weights, assets and services remain separate. [Source 1](https://github.com/ronreiter/pulsar/blob/main/LICENSE) [Source 2](https://github.com/ronreiter/pulsar/blob/main/README.md) [Source 3](https://ronreiter.github.io/pulsar/#listen)

- **Code:** GPL-3.0
- **Weights:** GPL-3.0 software with DawDreamer and Faust dependency terms. Kokoro weights/voices, reference recordings and the external AI composer have separate terms.
- **Commercial:** Software use follows GPL-3.0. GPL-3.0 software with DawDreamer and Faust dependency terms. Kokoro weights/voices, reference recordings and the external AI composer have separate terms.
- **Cost:** Local rendering plus chosen AI-agent access; no required paid music-generation endpoint is documented.

### Why it merits attention

Included for the documented creative workflow. A complete guide and popularity do not establish output reliability. [Source 1](https://github.com/ronreiter/pulsar/blob/main/README.md) [Source 2](https://ronreiter.github.io/pulsar/#listen)

### Limitations

Numerical tonal balance or masking feedback does not prove a satisfying composition. Neural singing repitches word-level speech and needs audition; it is not a guarantee of natural singing. [Source 1](https://github.com/ronreiter/pulsar/blob/main/README.md) [Source 2](https://ronreiter.github.io/pulsar/#listen)

### Get the tool

- [Repository](https://github.com/ronreiter/pulsar)
- [Documentation](https://github.com/ronreiter/pulsar/blob/main/README.md)

## Dawkey

Audio, music & voice · Performance, projection & stage media · Interactive, immersive & live media

A recently created project receiving its first full library guide; its creation is not proof of production readiness.

### Quality assessment: Experimental

Software licensing and a concrete creative AI use are supported. The remaining checks do not establish a recommendation.

Scope: Exploring inspectable AI-assisted music arrangement and mixing on a Linux creative workstation.

Evidence checked: 2026-10-27. No local execution implied.

Why Experimental: The current README explicitly marks early development and warns of rough edges and missing features in the recording/editing workflow. https://github.com/quonic/dawkey/blob/main/README.md

- **Open-source software license · verified:** The complete root software license was read and archived. The grant covers this project code; unresolved model, service and asset terms are disclosed separately. [Source](https://github.com/quonic/dawkey/blob/main/LICENSE)
- **Creative results · documented:** Official arrangement/mixer screenshots and an automation WebM show author workflows. They do not establish real-time stability with every audio device or plugin. [Source](https://github.com/quonic/dawkey/blob/main/README.md)
- **Reproducible setup · documented:** Use a documented distro package or build with Rust 1.88+ and the listed system libraries. The live app requires Wayland, PipeWire/WirePlumber and a Vulkan driver; attach the AI client to its local MCP socket. Independent reproduction has not been established in this review. [Source](https://github.com/quonic/dawkey/blob/main/README.md)
- **Maintenance and support · documented:** Live review archived 10 recent commits, 5 published release records and 10 recent support/PR records. Latest sampled commit: 2026-10-26. Current sampled topics include import_midi at position_bar or position_beats lands on the wrong bar when it adopts the file's tempo; A plugin file that prints anything to stdout while it's scanned disappears from the catalog. This is documented activity, not proof of sustained support or a complete blocker survey. [Source](https://github.com/quonic/dawkey/commits/main) [Source](https://github.com/quonic/dawkey/issues)
- **Independent use · unknown:** Reviewed official examples, the current support sample and bounded live web findings. Independent first-hand reproduction of this exact creative workflow was not established; author demonstrations are not treated as independent evidence.
- **Models, services and costs · documented:** AGPL-3.0-or-later software, separate OFL fonts and plugin licenses. AI assistant service access and third-party instruments are separate. Local DAW use plus optional instruments and AI assistant access. [Source](https://github.com/quonic/dawkey/blob/main/README.md)

Documentation review only; AI Media Scout did not install or run this software. The current project explicitly describes early development with rough edges and missing features. Plugin isolation and deterministic tests do not establish glitch-free venue or recording use.

### How it uses AI

A Linux DAW with a built-in MCP interface that lets AI assistants manipulate audio/MIDI arrangements, recording, instruments, automation and exports. [Source](https://github.com/quonic/dawkey/blob/main/README.md)

### Introduction

A Linux DAW with a built-in MCP interface that lets AI assistants manipulate audio/MIDI arrangements, recording, instruments, automation and exports. [Source 1](https://github.com/quonic/dawkey/blob/main/README.md)

### What it is good for

Exploring inspectable AI-assisted music arrangement and mixing on a Linux creative workstation. [Source 1](https://github.com/quonic/dawkey/blob/main/README.md)

### Demo & examples

Official arrangement/mixer screenshots and an automation WebM show author workflows. They do not establish real-time stability with every audio device or plugin. [Source 1](https://github.com/quonic/dawkey/blob/main/README.md)

### Install

Use a documented distro package or build with Rust 1.88+ and the listed system libraries. The live app requires Wayland, PipeWire/WirePlumber and a Vulkan driver; attach the AI client to its local MCP socket. [Source 1](https://github.com/quonic/dawkey/blob/main/README.md)

1. Obtain the official source or release linked below.
2. Use a documented distro package or build with Rust 1.88+ and the listed system libraries. The live app requires Wayland, PipeWire/WirePlumber and a Vulkan driver; attach the AI client to its local MCP socket.

```sh
cargo build --release
```


```sh
./target/release/dawkey
```


```sh
dawkey mcp --attach
```

### First project

Start with a short, representative project and inspect the result before a larger batch. [Source 1](https://github.com/quonic/dawkey/blob/main/README.md)

1. Import a small audio/MIDI project and confirm device routing.
2. Attach an AI assistant, request a bounded arrangement edit and inspect it in the timeline.
3. Audition plugin processing and exported WAV/FLAC; headless virtual-clock tests do not prove live audio performance.
### Hardware & software

Requirements below are documented for this workflow. Unspecified limits are not inferred. [Source 1](https://github.com/quonic/dawkey/blob/main/README.md)

- **Hardware:** A Vulkan-capable driver is required; Mesa software rendering is documented as an option. Minimum RAM/VRAM, audio-interface requirements and storage are not stated.
- **Software:** Rust 1.88+ for building; Wayland, PipeWire, WirePlumber, Vulkan, lilv and documented build libraries. XWayland and optional GTK/Qt libraries for plugin GUIs.
- **Platforms:** Linux only: packages are documented for Fedora 44, Debian 13, Ubuntu 26.04 and Arch. No X11 app, JACK or ALSA backend; headless virtual audio has different requirements.

### License, model weights & costs

The full software license was reviewed. Model weights, assets and services remain separate. [Source 1](https://github.com/quonic/dawkey/blob/main/LICENSE) [Source 2](https://github.com/quonic/dawkey/blob/main/README.md)

- **Code:** AGPL-3.0
- **Weights:** AGPL-3.0-or-later software, separate OFL fonts and plugin licenses. AI assistant service access and third-party instruments are separate.
- **Commercial:** Software use follows AGPL-3.0. AGPL-3.0-or-later software, separate OFL fonts and plugin licenses. AI assistant service access and third-party instruments are separate.
- **Cost:** Local DAW use plus optional instruments and AI assistant access.

### Why it merits attention

Included for the documented creative workflow. A complete guide and popularity do not establish output reliability. [Source 1](https://github.com/quonic/dawkey/blob/main/README.md)

### Limitations

The current project explicitly describes early development with rough edges and missing features. Plugin isolation and deterministic tests do not establish glitch-free venue or recording use. [Source 1](https://github.com/quonic/dawkey/blob/main/README.md)

### Get the tool

- [Repository](https://github.com/quonic/dawkey)
- [Documentation](https://github.com/quonic/dawkey/blob/main/README.md)

## Goxel MCP Server

3D, reconstruction & assets · Games & production pipelines · Computational art & creative coding

A recently created project receiving its first full library guide; its creation is not proof of production readiness.

### Quality assessment: Quality unverified

Software licensing and a concrete creative AI use are supported. The remaining checks do not establish a recommendation.

Scope: Drafting voxel game assets and reviewing agent-generated geometry in the same editor before exporting.

Evidence checked: 2026-10-27. No local execution implied.

- **Open-source software license · verified:** The complete root software license was read and archived. The grant covers this project code; unresolved model, service and asset terms are disclosed separately. [Source](https://github.com/al3x-d3v357/goxel-mcp/blob/main/LICENSE)
- **Creative results · documented:** The official preview shows a procedural cyberpunk archer generated through MCP and opened in Goxel. It is an author example, not evidence that arbitrary prompts produce usable assets. [Source](https://github.com/al3x-d3v357/goxel-mcp/blob/main/README.md)
- **Reproducible setup · documented:** Install Node 18+ and Goxel 0.15+, clone the source, then configure an MCP client to launch node with the absolute server.js path. Set the Goxel binary and output directory explicitly. Independent reproduction has not been established in this review. [Source](https://github.com/al3x-d3v357/goxel-mcp/blob/main/README.md)
- **Maintenance and support · documented:** Live review archived 3 recent commits, 1 published release records and 0 recent support/PR records. Latest sampled commit: 2026-10-24. The bounded support sample did not establish third-party resolution history. This is documented activity, not proof of sustained support or a complete blocker survey. [Source](https://github.com/al3x-d3v357/goxel-mcp/commits/main) [Source](https://github.com/al3x-d3v357/goxel-mcp/issues)
- **Independent use · unknown:** Reviewed official examples, the current support sample and bounded live web findings. Independent first-hand reproduction of this exact creative workflow was not established; author demonstrations are not treated as independent evidence.
- **Models, services and costs · documented:** MIT bridge code; Goxel’s own license, external model/agent access and any imported assets are separate. Local Goxel/Node compute plus whichever AI assistant is connected. [Source](https://github.com/al3x-d3v357/goxel-mcp/blob/main/README.md)

Documentation review only; AI Media Scout did not install or run this software. Character/object presets and QuickJS scripts provide the geometry; the AI role is tool orchestration. Output export does not guarantee engine readiness, rigging or printability.

### How it uses AI

An MCP bridge exposing Goxel’s procedural voxel characters, props, scripts, format conversion and GUI inspection to AI agents. [Source](https://github.com/al3x-d3v357/goxel-mcp/blob/main/README.md)

### Introduction

An MCP bridge exposing Goxel’s procedural voxel characters, props, scripts, format conversion and GUI inspection to AI agents. [Source 1](https://github.com/al3x-d3v357/goxel-mcp/blob/main/README.md)

### What it is good for

Drafting voxel game assets and reviewing agent-generated geometry in the same editor before exporting. [Source 1](https://github.com/al3x-d3v357/goxel-mcp/blob/main/README.md)

### Demo & examples

The official preview shows a procedural cyberpunk archer generated through MCP and opened in Goxel. It is an author example, not evidence that arbitrary prompts produce usable assets. [Source 1](https://github.com/al3x-d3v357/goxel-mcp/blob/main/README.md)

### Install

Install Node 18+ and Goxel 0.15+, clone the source, then configure an MCP client to launch node with the absolute server.js path. Set the Goxel binary and output directory explicitly. [Source 1](https://github.com/al3x-d3v357/goxel-mcp/blob/main/README.md)

1. Obtain the official source or release linked below.
2. Install Node 18+ and Goxel 0.15+, clone the source, then configure an MCP client to launch node with the absolute server.js path. Set the Goxel binary and output directory explicitly.

```sh
node /absolute/path/to/goxel-mcp/server.js
```

### First project

Start with a short, representative project and inspect the result before a larger batch. [Source 1](https://github.com/al3x-d3v357/goxel-mcp/blob/main/README.md)

1. Connect the agent and request one supplied character or object preset.
2. Open the generated .vox model in Goxel and inspect scale, topology and palette.
3. Try a bounded procedural modification, then validate OBJ/glTF or PNG exports in the destination application.
### Hardware & software

Requirements below are documented for this workflow. Unspecified limits are not inferred. [Source 1](https://github.com/al3x-d3v357/goxel-mcp/blob/main/README.md)

- **Hardware:** Minimum system RAM, VRAM and total disk space are not documented in the reviewed instructions.
- **Software:** Node.js 18+, Goxel 0.15+ and a local MCP-capable AI client; GUI interaction needs a working display session.
- **Platforms:** Linux, macOS and Windows Goxel paths are documented. The review did not establish equivalent end-to-end tests on all three.

### License, model weights & costs

The full software license was reviewed. Model weights, assets and services remain separate. [Source 1](https://github.com/al3x-d3v357/goxel-mcp/blob/main/LICENSE) [Source 2](https://github.com/al3x-d3v357/goxel-mcp/blob/main/README.md)

- **Code:** MIT
- **Weights:** MIT bridge code; Goxel’s own license, external model/agent access and any imported assets are separate.
- **Commercial:** Software use follows MIT. MIT bridge code; Goxel’s own license, external model/agent access and any imported assets are separate.
- **Cost:** Local Goxel/Node compute plus whichever AI assistant is connected.

### Why it merits attention

Included for the documented creative workflow. A complete guide and popularity do not establish output reliability. [Source 1](https://github.com/al3x-d3v357/goxel-mcp/blob/main/README.md)

### Limitations

Character/object presets and QuickJS scripts provide the geometry; the AI role is tool orchestration. Output export does not guarantee engine readiness, rigging or printability. [Source 1](https://github.com/al3x-d3v357/goxel-mcp/blob/main/README.md)

### Get the tool

- [Repository](https://github.com/al3x-d3v357/goxel-mcp)
- [Documentation](https://github.com/al3x-d3v357/goxel-mcp/blob/main/README.md)

## ShiGuang photo grading

Photography, restoration & color · AI color direction and palette-based media · Mobile, edge & on-device creation

A recently created project receiving its first full library guide; its creation is not proof of production readiness.

### Quality assessment: Quality unverified

Software licensing and a concrete creative AI use are supported. The remaining checks do not establish a recommendation.

Scope: Making conversational exposure/color adjustments and reusable photo recipes without using generative repainting in the main edit history.

Evidence checked: 2026-10-27. No local execution implied.

- **Open-source software license · verified:** The complete root software license was read and archived. The grant covers this project code; unresolved model, service and asset terms are disclosed separately. [Source](https://github.com/Pyc718672103/shiguang-photo/blob/main/LICENSE)
- **Creative results · documented:** The source describes parameter controls, histogram/clipping checks and evaluation scaffolding. Machine aesthetic scores are explicitly proxy measurements, not proof of human preference. [Source](https://github.com/Pyc718672103/shiguang-photo/blob/main/README.md)
- **Reproducible setup · documented:** Clone, create a Python environment and install the locked requirements. Configure the documented DashScope endpoint and credentials, then run the Gradio desktop UI or FastAPI backend for the WeChat mini program. Independent reproduction has not been established in this review. [Source](https://github.com/Pyc718672103/shiguang-photo/blob/main/README.md)
- **Maintenance and support · documented:** Live review archived 2 recent commits, 0 published release records and 0 recent support/PR records. Latest sampled commit: 2026-10-22. The bounded support sample did not establish third-party resolution history. This is documented activity, not proof of sustained support or a complete blocker survey. [Source](https://github.com/Pyc718672103/shiguang-photo/commits/main) [Source](https://github.com/Pyc718672103/shiguang-photo/issues)
- **Independent use · unknown:** Reviewed official examples, the current support sample and bounded live web findings. Independent first-hand reproduction of this exact creative workflow was not established; author demonstrations are not treated as independent evidence.
- **Models, services and costs · documented:** MIT software. DashScope/Qwen service terms and optional Real-ESRGAN/GFPGAN/YuNet weight terms remain separate; input photographs and evaluation assets retain their rights. Hosted VLM calls are separately billed; manual controls and applying a saved parameter recipe do not require another AI call. [Source](https://github.com/Pyc718672103/shiguang-photo/blob/main/README.md)

Documentation review only; AI Media Scout did not install or run this software. Only 8-bit single-frame JPEG/PNG up to 24 MP/30 MB are documented; no RAW/HDR, masks or batches. Only one model provider has been integrated. Optional restoration can invent detail and is outside the exact-undo chain.

### How it uses AI

A visual-language-model photo grader that proposes nine global edit parameters, then re-renders deterministically from the original image with an undoable version chain. [Source](https://github.com/Pyc718672103/shiguang-photo/blob/main/README.md)

### Introduction

A visual-language-model photo grader that proposes nine global edit parameters, then re-renders deterministically from the original image with an undoable version chain. [Source 1](https://github.com/Pyc718672103/shiguang-photo/blob/main/README.md)

### What it is good for

Making conversational exposure/color adjustments and reusable photo recipes without using generative repainting in the main edit history. [Source 1](https://github.com/Pyc718672103/shiguang-photo/blob/main/README.md)

### Demo & examples

The source describes parameter controls, histogram/clipping checks and evaluation scaffolding. Machine aesthetic scores are explicitly proxy measurements, not proof of human preference. [Source 1](https://github.com/Pyc718672103/shiguang-photo/blob/main/README.md)

### Install

Clone, create a Python environment and install the locked requirements. Configure the documented DashScope endpoint and credentials, then run the Gradio desktop UI or FastAPI backend for the WeChat mini program. [Source 1](https://github.com/Pyc718672103/shiguang-photo/blob/main/README.md)

1. Obtain the official source or release linked below.
2. Clone, create a Python environment and install the locked requirements. Configure the documented DashScope endpoint and credentials, then run the Gradio desktop UI or FastAPI backend for the WeChat mini program.

```sh
python -m venv .venv
```


```sh
.venv/bin/python -m pip install -r requirements.lock.txt
```


```sh
python ui/app.py
```

### First project

Start with a short, representative project and inspect the result before a larger batch. [Source 1](https://github.com/Pyc718672103/shiguang-photo/blob/main/README.md)

1. Open a copy of a supported JPEG/PNG and request a mild color/exposure adjustment.
2. Inspect clipping and the nine parameters, compare history versions and adjust manually.
3. Save a recipe or export, keeping optional upscaling/face restoration separate from the deterministic edit history.
### Hardware & software

Requirements below are documented for this workflow. Unspecified limits are not inferred. [Source 1](https://github.com/Pyc718672103/shiguang-photo/blob/main/README.md)

- **Hardware:** Input limit is 24 megapixels/30 MB; minimum system RAM, local GPU and total disk requirements are not documented. Main VLM analysis uses a hosted API.
- **Software:** Python 3.12 is the documented version; FastAPI, Gradio, Pillow and locked dependencies. WeChat Developer Tools and a user-owned AppID for mini-program development.
- **Platforms:** Windows/macOS/Linux Python setup variants plus WeChat and Gradio interfaces are documented; a complete tested physical-device matrix is not provided.

### License, model weights & costs

The full software license was reviewed. Model weights, assets and services remain separate. [Source 1](https://github.com/Pyc718672103/shiguang-photo/blob/main/LICENSE) [Source 2](https://github.com/Pyc718672103/shiguang-photo/blob/main/README.md)

- **Code:** MIT
- **Weights:** MIT software. DashScope/Qwen service terms and optional Real-ESRGAN/GFPGAN/YuNet weight terms remain separate; input photographs and evaluation assets retain their rights.
- **Commercial:** Software use follows MIT. MIT software. DashScope/Qwen service terms and optional Real-ESRGAN/GFPGAN/YuNet weight terms remain separate; input photographs and evaluation assets retain their rights.
- **Cost:** Hosted VLM calls are separately billed; manual controls and applying a saved parameter recipe do not require another AI call.

### Why it merits attention

Included for the documented creative workflow. A complete guide and popularity do not establish output reliability. [Source 1](https://github.com/Pyc718672103/shiguang-photo/blob/main/README.md)

### Limitations

Only 8-bit single-frame JPEG/PNG up to 24 MP/30 MB are documented; no RAW/HDR, masks or batches. Only one model provider has been integrated. Optional restoration can invent detail and is outside the exact-undo chain. [Source 1](https://github.com/Pyc718672103/shiguang-photo/blob/main/README.md)

### Get the tool

- [Repository](https://github.com/Pyc718672103/shiguang-photo)
- [Documentation](https://github.com/Pyc718672103/shiguang-photo/blob/main/README.md)

## Pergel

Vector graphics, illustration & textures · Browser tools & web media · Interactive, immersive & live media

A recently created project receiving its first full library guide; its creation is not proof of production readiness.

### Quality assessment: Experimental

Software licensing and a concrete creative AI use are supported. The remaining checks do not establish a recommendation.

Scope: Prototyping a design-to-code loop with real local assets and visible agent changes.

Evidence checked: 2026-10-27. No local execution implied.

Why Experimental: The current editor is explicitly early-development 0.1 with rough edges, incomplete plugin/import parity and untested Mac/Linux builds. https://github.com/Burqk1/Pergel/blob/main/README.md

- **Open-source software license · verified:** The complete root software license was read and archived. The grant covers this project code; unresolved model, service and asset terms are disclosed separately. [Source](https://github.com/Burqk1/Pergel/blob/main/LICENSE)
- **Creative results · documented:** Official documentation gives design-context and pixel-diff examples plus Windows performance measurements. Those examples are not independently verified fidelity benchmarks. [Source](https://github.com/Burqk1/Pergel/blob/main/README.md)
- **Reproducible setup · documented:** Use the current desktop release or build the Rust/WASM engine and Tauri shell with the documented toolchain. Keep the desktop app open and connect an MCP client to its loopback server on port 3855. Independent reproduction has not been established in this review. [Source](https://github.com/Burqk1/Pergel/blob/main/README.md)
- **Maintenance and support · documented:** Live review archived 3 recent commits, 2 published release records and 0 recent support/PR records. Latest sampled commit: 2026-10-24. The bounded support sample did not establish third-party resolution history. This is documented activity, not proof of sustained support or a complete blocker survey. [Source](https://github.com/Burqk1/Pergel/commits/main) [Source](https://github.com/Burqk1/Pergel/issues)
- **Independent use · unknown:** Reviewed official examples, the current support sample and bounded live web findings. Independent first-hand reproduction of this exact creative workflow was not established; author demonstrations are not treated as independent evidence.
- **Models, services and costs · documented:** MIT project code. Skia/Tauri/fonts/icons and any imported Figma assets keep separate terms. Figma imports need an authorized account/API token; an external AI agent supplies model inference. Local editing plus chosen AI agent and any Figma/asset access; no cloud-storage service is included. [Source](https://github.com/Burqk1/Pergel/blob/main/README.md)

Documentation review only; AI Media Scout did not install or run this software. Current 0.1 documentation identifies early development. Plugin compatibility is partial, Figma REST imports omit local variables/plugins, and collaboration merges at whole-frame granularity.

### How it uses AI

A local vector/interface design editor whose MCP server lets AI coding agents inspect assets, create or edit designs, generate reference code and compare implementations to the canvas. [Source](https://github.com/Burqk1/Pergel/blob/main/README.md)

### Introduction

A local vector/interface design editor whose MCP server lets AI coding agents inspect assets, create or edit designs, generate reference code and compare implementations to the canvas. [Source 1](https://github.com/Burqk1/Pergel/blob/main/README.md)

### What it is good for

Prototyping a design-to-code loop with real local assets and visible agent changes. [Source 1](https://github.com/Burqk1/Pergel/blob/main/README.md)

### Demo & examples

Official documentation gives design-context and pixel-diff examples plus Windows performance measurements. Those examples are not independently verified fidelity benchmarks. [Source 1](https://github.com/Burqk1/Pergel/blob/main/README.md)

### Install

Use the current desktop release or build the Rust/WASM engine and Tauri shell with the documented toolchain. Keep the desktop app open and connect an MCP client to its loopback server on port 3855. [Source 1](https://github.com/Burqk1/Pergel/blob/main/README.md)

1. Obtain the official source or release linked below.
2. Use the current desktop release or build the Rust/WASM engine and Tauri shell with the documented toolchain. Keep the desktop app open and connect an MCP client to its loopback server on port 3855.

```sh
npm install
```


```sh
npm run wasm
```


```sh
npm run tauri dev
```

### First project

Start with a short, representative project and inspect the result before a larger batch. [Source 1](https://github.com/Burqk1/Pergel/blob/main/README.md)

1. Create or import a small design with assets you can use.
2. Connect an AI agent and request a scoped canvas or implementation change.
3. Inspect real asset reuse, text/layout and pixel differences; review before accepting further changes.
### Hardware & software

Requirements below are documented for this workflow. Unspecified limits are not inferred. [Source 1](https://github.com/Burqk1/Pergel/blob/main/README.md)

- **Hardware:** Published benchmark used RTX 3080 and eight logical CPU cores; these are not minimum requirements. A small-file memory measurement and 4 GB WASM ceiling do not define required system RAM.
- **Software:** Documented build toolchain: Rust 1.99, Emscripten 6.0.12, Node 20+ and Tauri 2 prerequisites. Windows needs WebView2/MSVC tools.
- **Platforms:** Developed/tested by the author on Windows 11. Mac/Linux builds are explicitly untested. Browser-only mode has no MCP server or native file access.

### License, model weights & costs

The full software license was reviewed. Model weights, assets and services remain separate. [Source 1](https://github.com/Burqk1/Pergel/blob/main/LICENSE) [Source 2](https://github.com/Burqk1/Pergel/blob/main/README.md)

- **Code:** MIT
- **Weights:** MIT project code. Skia/Tauri/fonts/icons and any imported Figma assets keep separate terms. Figma imports need an authorized account/API token; an external AI agent supplies model inference.
- **Commercial:** Software use follows MIT. MIT project code. Skia/Tauri/fonts/icons and any imported Figma assets keep separate terms. Figma imports need an authorized account/API token; an external AI agent supplies model inference.
- **Cost:** Local editing plus chosen AI agent and any Figma/asset access; no cloud-storage service is included.

### Why it merits attention

Included for the documented creative workflow. A complete guide and popularity do not establish output reliability. [Source 1](https://github.com/Burqk1/Pergel/blob/main/README.md)

### Limitations

Current 0.1 documentation identifies early development. Plugin compatibility is partial, Figma REST imports omit local variables/plugins, and collaboration merges at whole-frame granularity. [Source 1](https://github.com/Burqk1/Pergel/blob/main/README.md)

### Get the tool

- [Repository](https://github.com/Burqk1/Pergel)
- [Documentation](https://github.com/Burqk1/Pergel/blob/main/README.md)

## Sequence browser editor

Video, animation & film · Browser tools & web media · Editing, captions & post-production

A recently created project receiving its first full library guide; its creation is not proof of production readiness.

### Quality assessment: Quality unverified

Software licensing and a concrete creative AI use are supported. The remaining checks do not establish a recommendation.

Scope: Creating small local video edits with agent-assisted trims, titles, fades and music while retaining manual timeline control.

Evidence checked: 2026-10-27. No local execution implied.

- **Open-source software license · verified:** The complete root software license was read and archived. The grant covers this project code; unresolved model, service and asset terms are disclosed separately. [Source](https://github.com/alamkanak/sequence/blob/main/LICENSE)
- **Creative results · documented:** The official hosted editor and screenshot show the multitrack workflow. Browser/codec compatibility and the quality of an AI edit remain unverified by this scout. [Source](https://github.com/alamkanak/sequence/blob/main/README.md) [Source](https://alamkanak.github.io/sequence/) [Source](https://alamkanak.github.io/sequence/docs/mcp/)
- **Reproducible setup · documented:** For manual editing open the official site in desktop Chrome/Edge. For AI editing install Node 24+ and follow the companion pairing guide. Self-hosting uses npm ci and npm run dev. Independent reproduction has not been established in this review. [Source](https://github.com/alamkanak/sequence/blob/main/README.md) [Source](https://alamkanak.github.io/sequence/) [Source](https://alamkanak.github.io/sequence/docs/mcp/)
- **Maintenance and support · documented:** Live review archived 10 recent commits, 0 published release records and 0 recent support/PR records. Latest sampled commit: 2026-10-24. The bounded support sample did not establish third-party resolution history. This is documented activity, not proof of sustained support or a complete blocker survey. [Source](https://github.com/alamkanak/sequence/commits/main) [Source](https://github.com/alamkanak/sequence/issues)
- **Independent use · unknown:** Reviewed official examples, the current support sample and bounded live web findings. Independent first-hand reproduction of this exact creative workflow was not established; author demonstrations are not treated as independent evidence.
- **Models, services and costs · documented:** AGPL-3.0-only project code. Browser codecs, imported media and AI-agent/model services have separate terms. The agent can receive project data and requested previews even though browser rendering stays local. Local rendering; chosen AI assistant access may cost money. [Source](https://github.com/alamkanak/sequence/blob/main/README.md) [Source](https://alamkanak.github.io/sequence/) [Source](https://alamkanak.github.io/sequence/docs/mcp/)

Documentation review only; AI Media Scout did not install or run this software. Browser data clearing deletes autosaved copies. Project JSON omits media, so originals are needed for reopening elsewhere. Export is SDR and does not preserve HDR; local browser processing is not a blanket guarantee that an external agent receives no data.

### How it uses AI

A browser video editor paired with a local MCP companion so AI agents can edit the same visible multitrack timeline that a person reviews and adjusts. [Source](https://github.com/alamkanak/sequence/blob/main/README.md) [Source](https://alamkanak.github.io/sequence/) [Source](https://alamkanak.github.io/sequence/docs/mcp/)

### Introduction

A browser video editor paired with a local MCP companion so AI agents can edit the same visible multitrack timeline that a person reviews and adjusts. [Source 1](https://github.com/alamkanak/sequence/blob/main/README.md) [Source 2](https://alamkanak.github.io/sequence/) [Source 3](https://alamkanak.github.io/sequence/docs/mcp/)

### What it is good for

Creating small local video edits with agent-assisted trims, titles, fades and music while retaining manual timeline control. [Source 1](https://github.com/alamkanak/sequence/blob/main/README.md) [Source 2](https://alamkanak.github.io/sequence/) [Source 3](https://alamkanak.github.io/sequence/docs/mcp/)

### Demo & examples

The official hosted editor and screenshot show the multitrack workflow. Browser/codec compatibility and the quality of an AI edit remain unverified by this scout. [Source 1](https://github.com/alamkanak/sequence/blob/main/README.md) [Source 2](https://alamkanak.github.io/sequence/) [Source 3](https://alamkanak.github.io/sequence/docs/mcp/)

### Install

For manual editing open the official site in desktop Chrome/Edge. For AI editing install Node 24+ and follow the companion pairing guide. Self-hosting uses npm ci and npm run dev. [Source 1](https://github.com/alamkanak/sequence/blob/main/README.md) [Source 2](https://alamkanak.github.io/sequence/) [Source 3](https://alamkanak.github.io/sequence/docs/mcp/)

1. Obtain the official source or release linked below.
2. For manual editing open the official site in desktop Chrome/Edge. For AI editing install Node 24+ and follow the companion pairing guide. Self-hosting uses npm ci and npm run dev.

```sh
npm ci
```


```sh
npm run dev
```

### First project

Start with a short, representative project and inspect the result before a larger batch. [Source 1](https://github.com/alamkanak/sequence/blob/main/README.md) [Source 2](https://alamkanak.github.io/sequence/) [Source 3](https://alamkanak.github.io/sequence/docs/mcp/)

1. Import original media and keep backup copies outside browser storage.
2. Pair the local agent with the editor, granting only the media folders needed for the project.
3. Review requested edits and export a short MP4/WebM when the browser supports it; inspect audio sync and codec output.
### Hardware & software

Requirements below are documented for this workflow. Unspecified limits are not inferred. [Source 1](https://github.com/alamkanak/sequence/blob/main/README.md) [Source 2](https://alamkanak.github.io/sequence/) [Source 3](https://alamkanak.github.io/sequence/docs/mcp/)

- **Hardware:** Minimum system RAM, VRAM and total disk space are not documented in the reviewed instructions.
- **Software:** Desktop Chrome or Edge recommended, browser media APIs and Node 24+ for MCP/self-hosting. A local MCP-capable AI client is required for AI edits.
- **Platforms:** Browser-based; codec/export support depends on browser and device. No complete hardware/OS support matrix is documented.

### License, model weights & costs

The full software license was reviewed. Model weights, assets and services remain separate. [Source 1](https://github.com/alamkanak/sequence/blob/main/LICENSE) [Source 2](https://github.com/alamkanak/sequence/blob/main/README.md) [Source 3](https://alamkanak.github.io/sequence/) [Source 4](https://alamkanak.github.io/sequence/docs/mcp/)

- **Code:** AGPL-3.0
- **Weights:** AGPL-3.0-only project code. Browser codecs, imported media and AI-agent/model services have separate terms. The agent can receive project data and requested previews even though browser rendering stays local.
- **Commercial:** Software use follows AGPL-3.0. AGPL-3.0-only project code. Browser codecs, imported media and AI-agent/model services have separate terms. The agent can receive project data and requested previews even though browser rendering stays local.
- **Cost:** Local rendering; chosen AI assistant access may cost money.

### Why it merits attention

Included for the documented creative workflow. A complete guide and popularity do not establish output reliability. [Source 1](https://github.com/alamkanak/sequence/blob/main/README.md) [Source 2](https://alamkanak.github.io/sequence/) [Source 3](https://alamkanak.github.io/sequence/docs/mcp/)

### Limitations

Browser data clearing deletes autosaved copies. Project JSON omits media, so originals are needed for reopening elsewhere. Export is SDR and does not preserve HDR; local browser processing is not a blanket guarantee that an external agent receives no data. [Source 1](https://github.com/alamkanak/sequence/blob/main/README.md) [Source 2](https://alamkanak.github.io/sequence/) [Source 3](https://alamkanak.github.io/sequence/docs/mcp/)

### Get the tool

- [Repository](https://github.com/alamkanak/sequence)
- [Documentation](https://github.com/alamkanak/sequence/blob/main/README.md)

## reel-studio

Video, animation & film · Motion capture & character animation · Neural rigging and digital puppetry

A recently created project receiving its first full library guide; its creation is not proof of production readiness.

### Quality assessment: Quality unverified

Software licensing and a concrete creative AI use are supported. The remaining checks do not establish a recommendation.

Scope: Making short repeatable animated explainers with inspectable staging and two procedural characters.

Evidence checked: 2026-10-27. No local execution implied.

- **Open-source software license · verified:** The complete root software license was read and archived. The grant covers this project code; unresolved model, service and asset terms are disclosed separately. [Source](https://github.com/NaxFur/reel-studio/blob/main/LICENSE)
- **Creative results · documented:** The README links two example episodes and the creator’s published .env sketch with beat stills. These are maintainer outputs, not independent reproduction evidence. [Source](https://github.com/NaxFur/reel-studio/blob/main/README.md) [Source](https://www.instagram.com/reel/De-JRqviF1z/)
- **Reproducible setup · documented:** On the documented Apple-silicon Mac setup, install Blender 5.x, ffmpeg, whisper.cpp and Python, then use the reviewed project’s installer and render example stills before a full episode. Independent reproduction has not been established in this review. [Source](https://github.com/NaxFur/reel-studio/blob/main/README.md) [Source](https://www.instagram.com/reel/De-JRqviF1z/)
- **Maintenance and support · documented:** Live review archived 4 recent commits, 1 published release records and 0 recent support/PR records. Latest sampled commit: 2026-10-27. The bounded support sample did not establish third-party resolution history. This is documented activity, not proof of sustained support or a complete blocker survey. [Source](https://github.com/NaxFur/reel-studio/commits/main) [Source](https://github.com/NaxFur/reel-studio/issues)
- **Independent use · unknown:** Reviewed official examples, the current support sample and bounded live web findings. Independent first-hand reproduction of this exact creative workflow was not established; author demonstrations are not treated as independent evidence.
- **Models, services and costs · documented:** MIT project code and procedural characters. Blender, speech-model weights, any ElevenLabs service and source audio retain separate terms; the fan character does not confer trademark affiliation. Local rendering plus chosen AI-agent access and optional paid TTS; recording your own voice avoids that TTS service fee. [Source](https://github.com/NaxFur/reel-studio/blob/main/README.md) [Source](https://www.instagram.com/reel/De-JRqviF1z/)

Documentation review only; AI Media Scout did not install or run this software. Full renders are substantially slower than draft stills. Final voice timing can change layout, camera shake can clip through geometry, and speech checks do not replace listening. No social publishing is performed by this research.

### How it uses AI

An AI coding-agent workflow that turns a storyboard into procedural Blender character sketches, captions, voices, sound effects and a vertical video; the visuals are scripted, not diffusion-generated. [Source](https://github.com/NaxFur/reel-studio/blob/main/README.md) [Source](https://www.instagram.com/reel/De-JRqviF1z/)

### Introduction

An AI coding-agent workflow that turns a storyboard into procedural Blender character sketches, captions, voices, sound effects and a vertical video; the visuals are scripted, not diffusion-generated. [Source 1](https://github.com/NaxFur/reel-studio/blob/main/README.md) [Source 2](https://www.instagram.com/reel/De-JRqviF1z/)

### What it is good for

Making short repeatable animated explainers with inspectable staging and two procedural characters. [Source 1](https://github.com/NaxFur/reel-studio/blob/main/README.md) [Source 2](https://www.instagram.com/reel/De-JRqviF1z/)

### Demo & examples

The README links two example episodes and the creator’s published .env sketch with beat stills. These are maintainer outputs, not independent reproduction evidence. [Source 1](https://github.com/NaxFur/reel-studio/blob/main/README.md) [Source 2](https://www.instagram.com/reel/De-JRqviF1z/)

### Install

On the documented Apple-silicon Mac setup, install Blender 5.x, ffmpeg, whisper.cpp and Python, then use the reviewed project’s installer and render example stills before a full episode. [Source 1](https://github.com/NaxFur/reel-studio/blob/main/README.md) [Source 2](https://www.instagram.com/reel/De-JRqviF1z/)

1. Obtain the official source or release linked below.
2. On the documented Apple-silicon Mac setup, install Blender 5.x, ffmpeg, whisper.cpp and Python, then use the reviewed project’s installer and render example stills before a full episode.

```sh
./setup/install.sh --model
```


```sh
skills/duo-sketch-reel/pipeline.sh examples/env-rotate --say stills
```

### First project

Start with a short, representative project and inspect the result before a larger batch. [Source 1](https://github.com/NaxFur/reel-studio/blob/main/README.md) [Source 2](https://www.instagram.com/reel/De-JRqviF1z/)

1. Inspect the example storyboard and render draft stills at every beat.
2. Use an AI coding agent to adapt the script, character acting and camera plan.
3. Add authorized recordings or chosen TTS, re-check timing and stills, then render and inspect the exported reel.
### Hardware & software

Requirements below are documented for this workflow. Unspecified limits are not inferred. [Source 1](https://github.com/NaxFur/reel-studio/blob/main/README.md) [Source 2](https://www.instagram.com/reel/De-JRqviF1z/)

- **Hardware:** Author example: roughly an hour for a 40-second reel on an M-series Mac with three workers. Exact minimum RAM, storage and GPU/unified memory are not documented.
- **Software:** macOS Apple silicon; Blender 5.x (author developed on 5.4), Python 3, ffmpeg, whisper.cpp/whisper-cli and an AI coding agent.
- **Platforms:** Apple-silicon macOS is tested by the author. Linux is explicitly untested and the free say-based draft is Mac-only; Windows support is not documented.

### License, model weights & costs

The full software license was reviewed. Model weights, assets and services remain separate. [Source 1](https://github.com/NaxFur/reel-studio/blob/main/LICENSE) [Source 2](https://github.com/NaxFur/reel-studio/blob/main/README.md) [Source 3](https://www.instagram.com/reel/De-JRqviF1z/)

- **Code:** MIT
- **Weights:** MIT project code and procedural characters. Blender, speech-model weights, any ElevenLabs service and source audio retain separate terms; the fan character does not confer trademark affiliation.
- **Commercial:** Software use follows MIT. MIT project code and procedural characters. Blender, speech-model weights, any ElevenLabs service and source audio retain separate terms; the fan character does not confer trademark affiliation.
- **Cost:** Local rendering plus chosen AI-agent access and optional paid TTS; recording your own voice avoids that TTS service fee.

### Why it merits attention

Included for the documented creative workflow. A complete guide and popularity do not establish output reliability. [Source 1](https://github.com/NaxFur/reel-studio/blob/main/README.md) [Source 2](https://www.instagram.com/reel/De-JRqviF1z/)

### Limitations

Full renders are substantially slower than draft stills. Final voice timing can change layout, camera shake can clip through geometry, and speech checks do not replace listening. No social publishing is performed by this research. [Source 1](https://github.com/NaxFur/reel-studio/blob/main/README.md) [Source 2](https://www.instagram.com/reel/De-JRqviF1z/)

### Get the tool

- [Repository](https://github.com/NaxFur/reel-studio)
- [Documentation](https://github.com/NaxFur/reel-studio/blob/main/README.md)

## Additional open-source AI discoveries

Creative AI relevance and software license screened. Full installation, requirements and quality profiles are pending.

### ChakraA sound-to-light · Apache-2.0

Prototyping room lighting driven by singing bowls, gongs and other sustained tones, starting with the desktop simulator.
A sound-to-light installation tool with an optional local EfficientAT neural sound gate that distinguishes bowl-like sounds and modulates light responses. Ordinary pitch-to-color detection also works without AI.
Full setup, hardware, model-term and output-quality review pending. The C pitch detector is separate from the AI gate. The gate source uses a separately prepared PyTorch/EfficientAT environment and author-local head paths; complete portable AI setup and weight terms remain pending. macOS/Linux simulator needs Python 3 and ffmpeg. ESP32-S31 board execution and its proposed ESP-DL AI port are untested; quoted on-board latency is an estimate. Color/chakra mappings are artistic conventions, not health measurements.

### Quality assessment: Quality unverified

Software license and creative AI relevance screened; full guide and quality checks remain pending.

Scope: Prototyping room lighting driven by singing bowls, gongs and other sustained tones, starting with the desktop simulator.

Evidence checked: 2026-10-27. No local execution implied.

- **Open-source software license · verified:** Complete software license read and archived; this grant does not cover separate models, services or assets. [Source](https://github.com/leopardcodeai/chakraa/blob/main/LICENSE)
- **Creative results · unknown:** Published creative results have not received a substantive independent quality review.
- **Reproducible setup · unknown:** A complete installation and reproducibility review is pending.
- **Maintenance and support · documented:** Live review archived 10 recent commits, 0 published release records and 0 recent support/PR records. Latest sampled commit: 2026-10-27. The bounded support sample did not establish third-party resolution history. This is documented activity, not proof of sustained support or a complete blocker survey. [Source](https://github.com/leopardcodeai/chakraa/commits/main) [Source](https://github.com/leopardcodeai/chakraa/issues)
- **Independent use · unknown:** Reviewed official examples, the current support sample and bounded live web findings. Independent first-hand reproduction of this exact creative workflow was not established; author demonstrations are not treated as independent evidence.
- **Models, services and costs · documented:** The C pitch detector is separate from the AI gate. The gate source uses a separately prepared PyTorch/EfficientAT environment and author-local head paths; complete portable AI setup and weight terms remain pending. macOS/Linux simulator needs Python 3 and ffmpeg. ESP32-S31 board execution and its proposed ESP-DL AI port are untested; quoted on-board latency is an estimate. Color/chakra mappings are artistic conventions, not health measurements. [Source](https://github.com/leopardcodeai/chakraa/blob/main/README.md) [Source](https://github.com/leopardcodeai/chakraa/blob/main/tools/ai_gate.py)

Source review only; not installed or run. The C pitch detector is separate from the AI gate. The gate source uses a separately prepared PyTorch/EfficientAT environment and author-local head paths; complete portable AI setup and weight terms remain pending. macOS/Linux simulator needs Python 3 and ffmpeg. ESP32-S31 board execution and its proposed ESP-DL AI port are untested; quoted on-board latency is an estimate. Color/chakra mappings are artistic conventions, not health measurements.

- [Official documentation](https://github.com/leopardcodeai/chakraa/blob/main/README.md)
- [Complete software license reviewed](https://github.com/leopardcodeai/chakraa/blob/main/LICENSE)
- [Additional primary documentation](https://github.com/leopardcodeai/chakraa/blob/main/tools/ai_gate.py)
- [Current maintenance and support evidence](https://github.com/leopardcodeai/chakraa/commits/main)
- [Current maintenance and support evidence](https://github.com/leopardcodeai/chakraa/issues)
### SolidCraft Traditional Chinese edition · Apache-2.0

Exploring localized AI-assisted parametric modeling while preserving upstream attribution.
A Traditional Chinese localization and Windows packaging of the SolidCraft parametric CAD application, retaining the upstream MCP route for AI agents to create and modify parts.
Full profile pending, especially localized Windows setup, model/service dependencies and physical-output validation. The complete Apache-2.0 software grant was reviewed; MIT is an alternative. This is a localized derivative of the SolidCraft already in the library, with a separate Traditional Chinese interface and Windows installer/portable release, not a new CAD kernel. Release assets were confirmed from metadata without downloading or running them. Most README demo links remain upstream. Localization-specific reproducibility, model/service costs and hardware minima need further review. The release advertises Bambu integration, but printed fit and tolerances are unverified.

### Quality assessment: Quality unverified

Software license and creative AI relevance screened; full guide and quality checks remain pending.

Scope: Exploring localized AI-assisted parametric modeling while preserving upstream attribution.

Evidence checked: 2026-10-27. No local execution implied.

- **Open-source software license · verified:** Complete software license read and archived; this grant does not cover separate models, services or assets. [Source](https://github.com/vincentchiou/solidcraft/blob/main/LICENSE-APACHE)
- **Creative results · unknown:** Published creative results have not received a substantive independent quality review.
- **Reproducible setup · documented:** The localized release lists a Windows setup executable and portable ZIP; its metadata confirms both assets. A full localized install and MCP reproducibility review remains pending; no binary was executed. [Source](https://github.com/vincentchiou/solidcraft/releases/tag/v0.22.1-zh-TW)
- **Maintenance and support · documented:** Live review archived 10 recent commits, 2 published release records and 0 recent support/PR records. Latest sampled commit: 2026-10-26. The bounded support sample did not establish third-party resolution history. This is documented activity, not proof of sustained support or a complete blocker survey. [Source](https://github.com/vincentchiou/solidcraft/commits/main) [Source](https://github.com/vincentchiou/solidcraft/issues)
- **Independent use · unknown:** Reviewed official examples, the current support sample and bounded live web findings. Independent first-hand reproduction of this exact creative workflow was not established; author demonstrations are not treated as independent evidence.
- **Models, services and costs · documented:** The complete Apache-2.0 software grant was reviewed; MIT is an alternative. This is a localized derivative of the SolidCraft already in the library, with a separate Traditional Chinese interface and Windows installer/portable release, not a new CAD kernel. Release assets were confirmed from metadata without downloading or running them. Most README demo links remain upstream. Localization-specific reproducibility, model/service costs and hardware minima need further review. The release advertises Bambu integration, but printed fit and tolerances are unverified. [Source](https://github.com/vincentchiou/solidcraft/blob/main/README.md) [Source](https://github.com/vincentchiou/solidcraft/releases/tag/v0.22.1-zh-TW)

Source review only; not installed or run. The complete Apache-2.0 software grant was reviewed; MIT is an alternative. This is a localized derivative of the SolidCraft already in the library, with a separate Traditional Chinese interface and Windows installer/portable release, not a new CAD kernel. Release assets were confirmed from metadata without downloading or running them. Most README demo links remain upstream. Localization-specific reproducibility, model/service costs and hardware minima need further review. The release advertises Bambu integration, but printed fit and tolerances are unverified.

- [Official documentation](https://github.com/vincentchiou/solidcraft/blob/main/README.md)
- [Complete software license reviewed](https://github.com/vincentchiou/solidcraft/blob/main/LICENSE-APACHE)
- [Current maintenance and support evidence](https://github.com/vincentchiou/solidcraft/commits/main)
- [Current maintenance and support evidence](https://github.com/vincentchiou/solidcraft/issues)
- [Localized Windows release and published asset inventory](https://github.com/vincentchiou/solidcraft/releases/tag/v0.22.1-zh-TW)

## Excluded and unresolved findings

Research notes only; these do not enter the eligible tool library.

- **Divya Drusti** · excluded: The complete grant is a modified MIT text that adds prominent author-link attribution to public deployments, modifications and derivatives. It is not the unmodified MIT license; eligibility under the project’s verified-OSI rule is not established. [Source](https://github.com/razeltech/divya-drusti/blob/main/LICENSE)
- **MatrixPrism** · excluded: The reviewed current workflow uses conventional audio analysis and generative shaders. An agent-development guide alone does not establish an AI feature in the creative application, so it is excluded from this AI-only edition. [Source](https://github.com/AnjinMeili/matrixprism)
- **Hi3D v1.0 MLX port** · excluded: The archived custom Hi3D software grant includes scale-triggered separate licensing and mandatory use/branding conditions. Public code and model downloads do not meet this library’s verified open-source software boundary. [Source](https://github.com/devin-lai/Hi3Dv1.0-mlx/blob/main/LICENSE)
- **Animated Design Previews** · needs-license-review: The previously observed repository now returns 404 for metadata, README and full-license reads. Historical metadata alone cannot establish current eligibility. [Source](https://github.com/yashansco/animated-design-previews)
- **REALMOTION-AI** · needs-license-review: The current repository lacks a readable README; metadata advertising talking portraits is insufficient to verify an implemented creative AI workflow. [Source](https://github.com/Nsjja7uaj/REALMOTION-AI)
- **Sparse older research guides** · needs-license-review: GANCalligraphy, Ceramic Design GANs, YOLO sonification, Collaborative Comic Generation, BrainArt, Vectra and Deep-Halftoning were revisited. Their existing screened records remain in the queue where setup, implementation or dependency evidence is incomplete; unchanged leads are not republished as discoveries. [Source](https://github.com/Nikronic/Deep-Halftoning)

Source collection completed: 2026-10-27T13:05:50.418706+00:00
Search is a bounded sample. Stars and recent pushes are discovery signals, not verified quality or meaningful upgrades.
