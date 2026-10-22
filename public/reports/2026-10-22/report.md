# AI Media Scout — 2026-10-22

Today’s expanded research adds 50 detailed guides and 37 additional screened discoveries across creative AI. Seventeen guides complete earlier screened entries; 70 tools are new to the library. All 500 configured repository queries and 18 model tasks across 64 fields were attempted: one repository query failed and 112 were bounded, so this is broad, disclosed coverage rather than an exhaustive search. Software licenses were reviewed in full for all 87 entries; model, service, asset and proprietary-host terms remain separate. Sixteen unresolved or excluded findings are explained, and Codeberg/SourceHut remain explicit access gaps. These are source reviews, not installations or hands-on demonstrations. Missing independent-use and quality evidence stays visible in the labels. Weekly whole-library review starts October 26 and is not due today.

Documentation reviewed today. Tools are not hands-on tested unless explicitly stated. Requirements and performance remain source-specific.

## Coverage

| Field | Finding |
| --- | --- |
| Images & design | Image generation, colorization and inpainting were researched alongside editable design tools. OpenPencil’s official site documents AI edits to real layers; today’s detailed guides include Inpaint Anything and watercolor/colorization workflows. Model terms remain separate. [Source 1](https://openpencil.dev/) |
| Video, animation & film | Video Dancer’s project site shows current artist-facing generative-video work. This edition adds multiple production workflows, with setup limits and service dependencies; these are first library guides, not claims that each app launched today. [Source 1](https://www.shdw.work/) |
| Audio, music & voice | Package research found phonepod’s local speech-restoration chain. The current Arm ULUNAS model card led to a newly screened MIT upstream speech-enhancement tool; the separate mobile inference package has an early-access dependency and unevaluated accuracy. YoVoice and other audio workflows receive full guides. [Source 1](https://pypi.org/project/phonepod/) [Source 2](https://huggingface.co/Arm/ulunas-speech-enhancement-fp32-litert) |
| 3D, reconstruction & assets | Neural rendering, avatar animation, CAD and model inspection remain in scope. Visionary links a hosted editor, but the page could not be opened in this pass; documentation and hardware guidance were reviewed in the source repository. Live primary-paper research on ManifoldSplat supplemented scene-editing discovery. Geometry export is not treated as measured accuracy or fabrication readiness. [Source 1](https://visionary.openxlab.org.cn/) [Source 2](https://arxiv.org/abs/2610.03599) |
| Browser tools & web media | Browser authoring and local browser front ends were checked, including OpenPencil’s programmable design surface. A web interface alone is not treated as proof of Mac/Linux support or offline AI inference. [Source 1](https://openpencil.dev/user-guide/) |
| WebXR, VR & AR | ImmersiveX’s project site describes an AI-assisted Unity/OpenXR route; it remains a research finding pending full software review. The older Inside Music experiment gets a guide with explicit legacy WebVR compatibility limits. [Source 1](https://www.genxr.co/immersivex) |
| Computational art & creative coding | Learned painting, procedural shaders and generated typography were covered. The NeuralType author describes a small neural font with important unseen-word failures; this is a finding, not an eligible release claim. [Source 1](https://elih.net/blog/nastaliq-distilled/) |
| Interactive, immersive & live media | Interactive scene and design authoring were checked through live project documentation, including collaborative agent edits in OpenPencil. Runtime compatibility and output reliability remain workflow-specific. [Source 1](https://openpencil.dev/) |
| 3D printing & generative CAD | Text-to-CAD and AI-assisted object design were researched, including CadZero’s official site. Full guides for Fabricator and CAD bridges retain proprietary-host requirements and do not equate STL output with a successful print. [Source 1](https://cadzero.dev/) |
| Games & production pipelines | The official Hayao site and playable-example listing document agent-authored 2D games, solver checks and human playtesting. They supplement neural game-model and Three.js authoring research. We reviewed documentation without running the examples; general game quality remains unverified. [Source 1](https://hayao.dev/) [Source 2](https://hayao.dev/play/) |
| Motion capture & character animation | The DancingBox paper describes motion capture for digital puppetry; today’s guides add several video-to-motion routes with model and rig limitations. Research origin alone does not produce an Experimental label. [Source 1](https://arxiv.org/abs/2603.17704) |
| Avatars, digital humans & lip sync | FantasyTalking’s official project page supplements portrait-animation research. Avatar samples, sign dictionaries and motion outputs are described as documented results, not verified communication accuracy or identity preservation. [Source 1](https://fantasy-amap.github.io/fantasy-talking/) |
| VFX, compositing & relighting | Current primary model research includes Lightricks’ water-effect IC-LoRA and NVIDIA UniRelight. The water adapter documents reference-conditioned edits but warns about identity drift and uses separate community weight terms with gated access. These model findings are not counted as new eligible software or verified physical simulation. [Source 1](https://huggingface.co/Lightricks/LTX-2.5-22b-IC-LoRA-Water-Simulation) [Source 2](https://huggingface.co/nvidia/UniRelight) |
| Spatial audio & volumetric media | The SonoWorld primary paper extends image-to-scene research into spatial audio. Acoustic Agent’s full guide distinguishes its simulation code from restricted floorplan/material/audio resources. [Source 1](https://openaccess.thecvf.com/content/CVPR2026/papers/Jin_SonoWorld_From_One_Image_to_a_3D_Audio-Visual_Scene_CVPR_2026_paper.pdf) |
| Photogrammetry, scanning & neural rendering | Captured-scene and Gaussian workflows were researched through LichtFeld’s project site and neural geometry repositories. New geometry leads need model, calibration and hardware review before any accuracy recommendation. [Source 1](https://lichtfeld.io/) |
| Editing, captions & post-production | Subtitld’s project documentation supplements caption/editing searches. Arya, ToneRelay and other guides distinguish local, hosted and proprietary-host features instead of assuming feature parity. [Source 1](https://subtitld.org/) |
| Vector graphics, illustration & textures | Editable vector and diagram workflows were researched through OpenPencil and repository documentation. Full guides cover SVG Animator and architecture diagrams; structural validity is not visual-quality verification. [Source 1](https://openpencil.dev/user-guide/) |
| Typography, fonts & layout | Neural font generation and agent-assisted typography remain covered. The NeuralType author’s documented limitations illustrate why font/glyph examples cannot establish robust shaping or reusable font-file quality. [Source 1](https://elih.net/blog/nastaliq-distilled/) |
| Storyboarding, narrative & comics | OpenNolan’s project site supplements story and shot-planning research. Today’s library additions include screenplay/shot agents and visual interpretation tools, with source-story and generation-service terms kept distinct. [Source 1](https://www.opennolan.com/) |
| Creative publishing & presentation | Agent-driven design and presentation exports were researched through OpenPencil’s official guide and diagram authoring projects. Publication/export capability is not evidence of factual accuracy or cleared source content. [Source 1](https://openpencil.dev/user-guide/) |
| Photography, restoration & color | The Adaptive Color Grading primary paper supplements photographic editing research. ToneRelay receives a guide based on its README and platform instructions; its reproduced editing captures are historical, and the linked portal could not be opened today. Adobe host requirements and source-preview limits remain explicit. [Source 1](https://arxiv.org/abs/2609.21169) [Source 2](https://reefruan.github.io/tonerelay-portal/#experience) |
| Data art & scientific visualization | SoundPlot’s primary paper describes learned organization of birdsong representations. Neural geometry, diagrams and biosignal visualization add adjacent creative directions; new leads remain pending detailed review. [Source 1](https://arxiv.org/abs/2601.12752) |
| Physical, robotic & kinetic installations | IRCAM’s installation article documents an EEG-driven sound-art practice. Hardware acquisition and artistic prototypes are researched without treating a project description as a released, licensed application. [Source 1](https://forum.ircam.fr/article/detail/mind-rain-bamboo-whisper-real-time-eeg-interactive-installation/) |
| Performance, projection & stage media | Live audiovisual work was researched alongside IRCAM’s EEG performance example. HVFT VISION receives a source-based guide that separates matting/depth code, noncommercial optional weights and restricted visual assets. [Source 1](https://forum.ircam.fr/article/detail/mind-rain-bamboo-whisper-real-time-eeg-interactive-installation/) |
| Fashion, textiles & wearable media | FabricTryon’s official project page documents fabric retexturing. Clothing-design and knitting searches also found research/proposal material; no production sewing or fabric behavior is inferred from a rendered garment. [Source 1](https://style3d.github.io/fabric_tryon/) |
| Accessible media & assistive creation | OpenEar’s project site and caption/audio-description sources were checked. Signing avatars receive cautious workflow descriptions; independent signer/user validation remains a specific evidence gap. [Source 1](https://www.openearproject.org/) |
| Mobile, edge & on-device creation | Mobile searches included on-device generative galleries and tactile prototypes. HapticGen’s official material helps frame multimodal interaction; device-specific requirements are retained and general phone support is not inferred. [Source 1](https://hapticgen.hcitech.org/) |
| Creative learning & authoring | Aalto’s textile-design research connects AI with pattern-design education. Today’s guides also cover music-production learning and creative coding, without claiming unverified teaching outcomes. [Source 1](https://www.aalto.fi/en/research-art/textile-design-meets-ai) |
| Archives, media restoration & collections | Kraken’s current documentation describes trainable recognition for historical and non-Latin documents. The root redirect initially yielded no readable content, so the current documentation path was researched directly; new archival-tool eligibility is still reviewed individually. [Source 1](https://kraken.re/main/index.html) |
| Emerging & cross-disciplinary creative AI | Emerging multisensory and cross-disciplinary practices were researched beyond the starter fields. MIT’s Anemoia page describes AI-linked scent work, but a fully reviewed open-source software release was not established. [Source 1](https://www.media.mit.edu/projects/anemoia-device/overview/) |
| Tactile, vibration and haptic media | HapticGen’s official project describes text-to-vibration research. Additional screened leads include mobile texture-to-haptics and agent-authored tactile patterns; accessibility validation and device behavior remain unresolved. [Source 1](https://hapticgen.hcitech.org/) |
| Neural acoustics and responsive sound spaces | SonoWorld’s primary paper was checked alongside Acoustic Agent’s current documentation. The latter uses AI-assisted scene/material information around physical simulation; it is not presented as a wholly neural acoustic renderer. [Source 1](https://openaccess.thecvf.com/content/CVPR2026/papers/Jin_SonoWorld_From_One_Image_to_a_3D_Audio-Visual_Scene_CVPR_2026_paper.pdf) |
| AI agents for code-authored media production | Anymotion’s project site supplements terminal-agent motion research. Shaderera and several studio guides show different production approaches; external model services and quality claims are checked separately. [Source 1](https://anymotion.art) |
| AI kinetic typography and animated lettering | The ICCV Dynamic Typography paper provides a primary research trail for animated lettering. Agent motion skills and SVG workflows are also covered, with typography legibility left as an unverified quality check. [Source 1](https://www.openaccess.thecvf.com/content/ICCV2025/papers/Liu_Dynamic_Typography_Bringing_Text_to_Life_via_Video_Diffusion_Prior_ICCV_2025_paper.pdf) |
| AI choreography and dance composition | DanceCrafter’s author project page documents controllable dance research; GitLab also surfaced a MotionNet project. Released code, model rights and dance quality require further review before new eligibility claims. [Source 1](https://faustrazor.github.io/) |
| AI-assisted textile and computational craft | Aalto’s current knitting research was checked alongside weaving searches. Knit-by-Command’s README still contains a usage placeholder and goals, so it is not treated as an implemented AI tool. [Source 1](https://www.aalto.fi/en/research-art/textile-design-meets-ai) |
| AI music notation and score recovery | Kyutai’s Muscriptor project and other notation sites were researched. YoVoice’s guide includes score-related workflows while keeping transcription models and music-model terms separate. [Source 1](https://muscriptor.kyutai.org/) |
| Neural relighting and material recovery | UniRelight’s model page and material-generation projects were checked. Albedolizer’s learned color correction is distinguished from procedural PBR maps and from measured inverse rendering. [Source 1](https://huggingface.co/nvidia/UniRelight) |
| Olfactory and multisensory AI media | MIT’s Anemoia page and the iPheromone artist project were examined. AI-linked scent installations were found, but no additional fully licensed, reproducible software package was established in this pass. [Source 1](https://www.media.mit.edu/projects/anemoia-device/overview/) |
| AI architectural visualization and spatial design | ClayScape’s primary paper links generated form to a physical creative workflow; architectural and room-simulation searches broadened that trail. Open Garden Planner and Acoustic Agent have separate guides with practical limits. [Source 1](https://arxiv.org/abs/2604.25657) |
| Neural holography and light-field media | Neural Light Spheres and learned light-field editing research were checked. HFG Neural Holography is preserved as an unfinished screened implementation because its own checkpoints and a required source link are still missing. [Source 1](https://arxiv.org/abs/2409.17924) |
| Neural rigging and digital puppetry | DancingBox’s paper provides a current digital-puppetry research source. Vid2anim and Blender motion guides retain retargeting, host-version and separate character-asset constraints. [Source 1](https://arxiv.org/abs/2603.17704) |
| AI ceramics and archaeological illustration | ClayScape’s author paper was checked for AI-assisted ceramics and printed forms. A paper or demo alone does not establish an eligible code release; existing ceramic-code leads still need fuller setup evidence. [Source 1](https://arxiv.org/abs/2604.25657) |
| AI parametric design and jewelry | CadZero’s project site and AI-to-CAD implementations were researched. Full guides distinguish open-source bridges from required proprietary CAD hosts and unverified fabrication results. [Source 1](https://cadzero.dev/) |
| AI cartography and artistic maps | LibreTerrain’s official site documents agent-accessible terrain graphs and export formats. This is a source finding pending a complete license/workflow review; ordinary non-AI cartography is not admitted just for matching a search term. Trazo receives a full guide for its implemented AI-assisted geospatial authoring, with optional ArcGIS services and separately licensed bundled assets disclosed. [Source 1](https://libreterrain.org/) |
| AI robotic painting and drawing | The Artistic Style in Robotic Painting paper and artist-authored brushstroke project were examined. BrushOS lacks a collected license grant and stays outside the eligible library. [Source 1](https://arxiv.org/abs/2007.03647) |
| AI cel animation and inbetweening | Primary animation research on sparse-input inbetweening/colorization was checked. Today’s colorization guide is scoped to draft page colors, without promising animation continuity. [Source 1](https://openreview.net/pdf/c124ef4c12ad5e1cf5d1d3271bd3dcd05e46544d.pdf) |
| AI Foley and sound effects | FolAI’s official project site provides a synchronized-Foley research trail. Sound-effects generation in broader studios remains subject to its selected model terms and full output review. [Source 1](https://ispamm.github.io/FolAI/) |
| Learned media codecs and neural delivery | Kyutai’s primary codec explainer was supplemented with original software documentation across speech, general sound and developer ports. This edition adds full SemantiCodec, HILCodec and DisCoder guides plus screened codecs; model/data terms, unfinished packages and independent listening gaps remain explicit. [Source 1](https://kyutai.org/codec-explainer/) |
| AI assisted sound data art and corpus instruments | SoundPlot’s primary paper connects learned sound organization with birdsong representations. It remains a research lead until software and dataset terms are reviewed. [Source 1](https://arxiv.org/abs/2601.12752) |
| AI biosignal art and neurointeractive media | IRCAM’s EEG installation article and BrainFLORA source were reviewed. The screened framework uses recorded datasets; it is not described as a validated live thought-to-art product. [Source 1](https://forum.ircam.fr/article/detail/mind-rain-bamboo-whisper-real-time-eeg-interactive-installation/) |
| Neural procedural material authoring | FabricTryon’s project page provides a material-appearance research source. Shader Architect and Albedolizer cover separate code/material workflows, with visual correctness and physical material fidelity unverified. [Source 1](https://style3d.github.io/fabric_tryon/) |
| Neural cameras and unconventional image capture | The imaging lab’s research page surfaced learned unconventional-camera reconstruction. No newly verified deployable camera tool or hardware requirements were established; ordinary camera hardware is not relabeled as AI. [Source 1](https://iilab.io/research.html) |
| AI origami, kirigami and paper engineering | COrigami’s primary paper and a newly found Papercraft-KI workflow were researched. The latter explicitly remains documentation-stage with a non-AI cube example and placeholder projects; neither source establishes an additional fully reviewed AI fabrication application here. [Source 1](https://arxiv.org/abs/2606.26299) |
| AI landscape, garden and environmental design | LibreTerrain’s official site supplements landscape/terrain searches, and Open Garden Planner receives a full guide for its agent-accessible plan. Plant outcomes and physical-site accuracy remain distinct from drawing features. [Source 1](https://libreterrain.org/) |
| Neural mosaic and stained-glass media | The CVF art project page surfaced an AI/code-based mosaic practice. No additional released, fully licensed mosaic tool was established; ordinary average-color mosaic algorithms alone do not satisfy AI relevance. [Source 1](https://www.thecvf-art.com/project.php?artist=ashwin-nedungadi&id=933&year=2026) |
| AI optical illusions and anamorphic media | Visual Anagrams’ official page documents diffusion-generated transformed-view illusions. It supplements this field’s research without recycling an unchanged earlier library entry. [Source 1](https://dangeng.github.io/visual_anagrams/) |
| AI relief engraving and learned halftoning | Deep Halftoning’s author project page and repository were rechecked. Its current README says paper numbers are not reproducible; it remains a pending review rather than a completed production guide. [Source 1](https://nikronic.com/projects/deep-halftoning_project/) |
| Neural brushstroke painting and drawn media | The artist-authored imag_stroke_ai project and learned painting repositories were researched. Full guides cover coordinate-based neural painting and a legacy sketch-to-watercolor experiment, with actual testing explicitly absent. [Source 1](https://www.pouyanasgharian.com/projects/imag_stroke_ai/) |
| AI color direction and palette-based media | The Adaptive Color Grading primary paper supplements current color-workflow searches. ToneRelay’s practical guide distinguishes documented editing sessions from new benchmarks or independent output checks. [Source 1](https://arxiv.org/abs/2609.21169) |
| AI collage, cut-paper composition and layered media | The Collage Diffusion author page was located after two guessed project URLs failed. Additional agent-driven paper-collage workflows were screened; their external video services and factual-script accuracy remain separate checks. [Source 1](https://vsanimator.github.io/collage_diffusion/) |
| AI stereo conversion and spatial video authoring | Neural/display-radiance research and stereo conversion queries were checked. Existing stereo candidates remain in the cumulative backlog; this edition does not claim a new fully verified stereo authoring tool. [Source 1](https://arxiv.org/abs/2510.03356) |
| AI semantic editing of captured 3D scenes | The October ManifoldSplat paper describes language-guided head-avatar editing. Its project page failed to open, so code/license eligibility was not established from the paper alone. [Source 1](https://arxiv.org/abs/2610.03599) |
| AI signing avatars and expressive gesture media | BhashaSetu’s primary project site and sign-avatar implementations were researched. SignFlow and a MediaPipe-to-Blender capture workflow receive guides; linguistic accuracy and expressive signing remain unverified, and two no-license repositories stay excluded. [Source 1](https://www.bhashasetuisl.in/) |

## Search and review counts

64 creative fields; 500/500 repository queries attempted; 18/18 model-task queries attempted. 25750 distinct source candidates and 852 model leads. 50 detailed profiles and 37 additional screened discoveries. Source gaps: 1 failed repository queries, 0 partial repository queries, 112 bounded repository queries, 0 failed model-task queries and 2 web ecosystem gaps. Raw search candidates include duplicates of known tools, excluded projects and projects awaiting review; they are not verified recommendations.

## Research beyond GitHub

- **gitlab** · searched: Researched MotionNet’s music-to-ballroom choreography project and an image-API contract. Metadata and declared licensing are not a complete reviewed software grant; neither is added as an eligible tool today. [Source](https://gitlab.com/Roxanne_Ardary/motionnet) [Source](https://gitlab.com/a.adach/ai-image-contract/-/blob/main/README.md)
- **codeberg** · gap: The live site-scoped search was blocked by robots restrictions; no Codeberg-wide coverage or eligible new finding is claimed.
- **sourcehut** · gap: The live git.sr.ht search was blocked by robots restrictions; this ecosystem remains an explicit coverage gap.
- **packages** · searched: PyPI research led to phonepod, whose software license was separately reviewed. Neural-tilde explicitly reuses noncommercial nn~ code and is excluded despite its creative audio use. [Source](https://pypi.org/project/phonepod/) [Source](https://pypi.org/project/neural-tilde/)
- **creative-plugins** · searched: Reviewed source documentation for Lightroom Classic, Blender, Ableton and CAD integrations. ToneRelay’s README reproduces prior editing captures; the separate portal could not be opened in this pass. Required host licenses and model services remain separate. [Source](https://reefruan.github.io/tonerelay-portal/#experience) [Source](https://github.com/Larenju-Rai/open-mocap-blender)
- **project-sites** · searched: Checked current official design, rendering, motion, audio and multisensory project sites. Some pages failed to open and some promising claims lack a reviewed software release; those are disclosed rather than counted as eligible. [Source](https://openpencil.dev/) [Source](https://hapticgen.hcitech.org/) [Source](https://www.media.mit.edu/projects/anemoia-device/overview/)
- **research-code** · searched: Followed primary papers and official implementations for motion, holography, scene editing, typography and codecs. No-license code and unreleased checkpoints remain explicit gaps. [Source](https://arxiv.org/abs/2610.03599) [Source](https://arxiv.org/abs/2603.17704) [Source](https://github.com/IGL-HKUST/DiffusionAsShader)
- **international** · searched: Reviewed Chinese/English voice, design and photo workflows, Korean/English video-workbench docs, Spanish reconstruction tooling and Indonesian performance documentation; platform advice is not restricted to one country or OS. [Source](https://github.com/leemysw/yovoice) [Source](https://github.com/raonolje/AIMovieStorage) [Source](https://github.com/rellytechgame/Reverse3D-tool) [Source](https://github.com/rezjadwi/hvft-vision)

## Collection limitations

- images: bounded or incomplete query: topic:diffusion pushed:>=2026-09-22 is:public fork:false archived:false (200 of 230 matches sampled)
- images: bounded or incomplete query: topic:diffusion is:public fork:false archived:false (200 of 1475 matches sampled)
- images: bounded or incomplete query: AI image generation pushed:>=2026-09-22 is:public fork:false archived:false (200 of 1719 matches sampled)
- images: bounded or incomplete query: AI image generation created:>=2026-09-22 is:public fork:false archived:false (200 of 879 matches sampled)
- images: bounded or incomplete query: AI image generation is:public fork:false archived:false (200 of 15834 matches sampled)
- video: bounded or incomplete query: AI video pushed:>=2026-09-22 is:public fork:false archived:false (200 of 13997 matches sampled)
- video: bounded or incomplete query: AI video created:>=2026-09-22 is:public fork:false archived:false (200 of 9155 matches sampled)
- video: bounded or incomplete query: AI video is:public fork:false archived:false (200 of 88070 matches sampled)
- video: bounded or incomplete query: topic:video-generation pushed:>=2026-09-22 is:public fork:false archived:false (200 of 1898 matches sampled)
- video: bounded or incomplete query: topic:video-generation created:>=2026-09-22 is:public fork:false archived:false (200 of 893 matches sampled)
- video: bounded or incomplete query: topic:video-generation is:public fork:false archived:false (200 of 4472 matches sampled)
- audio: bounded or incomplete query: topic:music-generation pushed:>=2026-09-22 is:public fork:false archived:false (200 of 362 matches sampled)
- audio: bounded or incomplete query: topic:music-generation is:public fork:false archived:false (500 of 1284 matches sampled)
- audio: bounded or incomplete query: AI audio pushed:>=2026-09-22 is:public fork:false archived:false (200 of 4061 matches sampled)
- audio: bounded or incomplete query: AI audio created:>=2026-09-22 is:public fork:false archived:false (200 of 2161 matches sampled)
- audio: bounded or incomplete query: AI audio is:public fork:false archived:false (200 of 28803 matches sampled)
- 3d: bounded or incomplete query: 3D generation pushed:>=2026-09-22 is:public fork:false archived:false (200 of 660 matches sampled)
- 3d: bounded or incomplete query: 3D generation created:>=2026-09-22 is:public fork:false archived:false (200 of 301 matches sampled)
- 3d: bounded or incomplete query: 3D generation is:public fork:false archived:false (200 of 5936 matches sampled)
- 3d: bounded or incomplete query: topic:3d-reconstruction pushed:>=2026-09-22 is:public fork:false archived:false (200 of 308 matches sampled)
- 3d: bounded or incomplete query: topic:3d-reconstruction is:public fork:false archived:false (200 of 2011 matches sampled)
- web: bounded or incomplete query: topic:webgpu pushed:>=2026-09-22 is:public fork:false archived:false (200 of 1312 matches sampled)
- web: bounded or incomplete query: topic:webgpu created:>=2026-09-22 is:public fork:false archived:false (200 of 572 matches sampled)
- web: bounded or incomplete query: topic:webgpu is:public fork:false archived:false (200 of 3219 matches sampled)
- xr: bounded or incomplete query: AI WebXR pushed:>=2026-09-22 is:public fork:false archived:false (47 of 48 matches sampled)
- xr: bounded or incomplete query: AI WebXR created:>=2026-09-22 is:public fork:false archived:false (28 of 29 matches sampled)
- xr: bounded or incomplete query: AI WebXR is:public fork:false archived:false (146 of 147 matches sampled)
- xr: bounded or incomplete query: AI VR pushed:>=2026-09-22 is:public fork:false archived:false (200 of 363 matches sampled)
- xr: bounded or incomplete query: AI VR is:public fork:false archived:false (200 of 2939 matches sampled)
- computational: bounded or incomplete query: AI creative coding is:public fork:false archived:false (200 of 960 matches sampled)
- computational: bounded or incomplete query: topic:generative-art pushed:>=2026-09-22 is:public fork:false archived:false (200 of 1077 matches sampled)
- computational: bounded or incomplete query: topic:generative-art created:>=2026-09-22 is:public fork:false archived:false (200 of 583 matches sampled)
- computational: bounded or incomplete query: topic:generative-art is:public fork:false archived:false (200 of 4243 matches sampled)
- interactive: bounded or incomplete query: AI interactive art is:public fork:false archived:false (200 of 700 matches sampled)
- fabrication: bounded or incomplete query: AI CAD pushed:>=2026-09-22 is:public fork:false archived:false (200 of 834 matches sampled)
- fabrication: bounded or incomplete query: AI CAD created:>=2026-09-22 is:public fork:false archived:false (200 of 475 matches sampled)
- fabrication: bounded or incomplete query: AI CAD is:public fork:false archived:false (200 of 3313 matches sampled)
- fabrication: bounded or incomplete query: AI 3D printing is:public fork:false archived:false (200 of 363 matches sampled)
- gaming: bounded or incomplete query: AI game assets is:public fork:false archived:false (200 of 680 matches sampled)
- gaming: bounded or incomplete query: AI blender pushed:>=2026-09-22 is:public fork:false archived:false (200 of 507 matches sampled)
- gaming: bounded or incomplete query: AI blender created:>=2026-09-22 is:public fork:false archived:false (200 of 335 matches sampled)
- gaming: bounded or incomplete query: AI blender is:public fork:false archived:false (200 of 1733 matches sampled)
- motion: bounded or incomplete query: AI motion capture is:public fork:false archived:false (200 of 241 matches sampled)
- motion: bounded or incomplete query: motion generation pushed:>=2026-09-22 is:public fork:false archived:false (200 of 236 matches sampled)
- motion: bounded or incomplete query: motion generation is:public fork:false archived:false (200 of 1570 matches sampled)
- avatars: bounded or incomplete query: AI avatar pushed:>=2026-09-22 is:public fork:false archived:false (200 of 820 matches sampled)
- avatars: bounded or incomplete query: AI avatar created:>=2026-09-22 is:public fork:false archived:false (200 of 455 matches sampled)
- avatars: bounded or incomplete query: AI avatar is:public fork:false archived:false (200 of 6107 matches sampled)
- avatars: bounded or incomplete query: lip sync pushed:>=2026-09-22 is:public fork:false archived:false (200 of 354 matches sampled)
- avatars: bounded or incomplete query: lip sync created:>=2026-09-22 is:public fork:false archived:false (200 of 236 matches sampled)
- avatars: bounded or incomplete query: lip sync is:public fork:false archived:false (200 of 2518 matches sampled)
- vfx: bounded or incomplete query: AI visual effects is:public fork:false archived:false (200 of 428 matches sampled)
- capture: bounded or incomplete query: topic:gaussian-splatting pushed:>=2026-09-22 is:public fork:false archived:false (200 of 265 matches sampled)
- capture: bounded or incomplete query: topic:gaussian-splatting is:public fork:false archived:false (500 of 986 matches sampled)
- capture: bounded or incomplete query: neural reconstruction is:public fork:false archived:false (200 of 1341 matches sampled)
- editing: bounded or incomplete query: AI video editing pushed:>=2026-09-22 is:public fork:false archived:false (200 of 974 matches sampled)
- editing: bounded or incomplete query: AI video editing created:>=2026-09-22 is:public fork:false archived:false (200 of 638 matches sampled)
- editing: bounded or incomplete query: AI video editing is:public fork:false archived:false (200 of 3793 matches sampled)
- editing: bounded or incomplete query: AI subtitle pushed:>=2026-09-22 is:public fork:false archived:false (200 of 394 matches sampled)
- editing: bounded or incomplete query: AI subtitle created:>=2026-09-22 is:public fork:false archived:false (200 of 212 matches sampled)
- editing: bounded or incomplete query: AI subtitle is:public fork:false archived:false (200 of 2326 matches sampled)
- vector: bounded or incomplete query: AI SVG pushed:>=2026-09-22 is:public fork:false archived:false (200 of 527 matches sampled)
- vector: bounded or incomplete query: AI SVG created:>=2026-09-22 is:public fork:false archived:false (200 of 294 matches sampled)
- vector: bounded or incomplete query: AI SVG is:public fork:false archived:false (200 of 1960 matches sampled)
- typography: bounded or incomplete query: AI typography is:public fork:false archived:false (200 of 710 matches sampled)
- typography: bounded or incomplete query: font generation is:public fork:false archived:false (400 of 417 matches sampled)
- storytelling: bounded or incomplete query: AI storyboard pushed:>=2026-09-22 is:public fork:false archived:false (200 of 463 matches sampled)
- storytelling: bounded or incomplete query: AI storyboard created:>=2026-09-22 is:public fork:false archived:false (200 of 300 matches sampled)
- storytelling: bounded or incomplete query: AI storyboard is:public fork:false archived:false (200 of 1866 matches sampled)
- storytelling: bounded or incomplete query: AI comic pushed:>=2026-09-22 is:public fork:false archived:false (200 of 1804 matches sampled)
- storytelling: bounded or incomplete query: AI comic created:>=2026-09-22 is:public fork:false archived:false (200 of 1706 matches sampled)
- storytelling: bounded or incomplete query: AI comic is:public fork:false archived:false (200 of 3111 matches sampled)
- publishing: bounded or incomplete query: AI presentation pushed:>=2026-09-22 is:public fork:false archived:false (200 of 1148 matches sampled)
- publishing: bounded or incomplete query: AI presentation created:>=2026-09-22 is:public fork:false archived:false (200 of 671 matches sampled)
- publishing: bounded or incomplete query: AI presentation is:public fork:false archived:false (200 of 8788 matches sampled)
- publishing: bounded or incomplete query: AI publishing pushed:>=2026-09-22 is:public fork:false archived:false (200 of 1067 matches sampled)
- publishing: bounded or incomplete query: AI publishing created:>=2026-09-22 is:public fork:false archived:false (200 of 597 matches sampled)
- publishing: bounded or incomplete query: AI publishing is:public fork:false archived:false (200 of 4221 matches sampled)
- photography: bounded or incomplete query: AI photo restoration is:public fork:false archived:false (200 of 209 matches sampled)
- photography: bounded or incomplete query: AI colorization pushed:>=2026-09-22 is:public fork:false archived:false (200 of 465 matches sampled)
- photography: bounded or incomplete query: AI colorization created:>=2026-09-22 is:public fork:false archived:false (200 of 284 matches sampled)
- photography: bounded or incomplete query: AI colorization is:public fork:false archived:false (200 of 4883 matches sampled)
- visualization: bounded or incomplete query: AI visualization pushed:>=2026-09-22 is:public fork:false archived:false (200 of 3450 matches sampled)
- visualization: bounded or incomplete query: AI visualization created:>=2026-09-22 is:public fork:false archived:false (200 of 2034 matches sampled)
- visualization: bounded or incomplete query: AI visualization is:public fork:false archived:false (200 of 38646 matches sampled)
- visualization: bounded or incomplete query: AI data art is:public fork:false archived:false (200 of 1039 matches sampled)
- performance: bounded or incomplete query: AI live visuals is:public fork:false archived:false (200 of 746 matches sampled)
- fashion: bounded or incomplete query: AI fashion design is:public fork:false archived:false (200 of 653 matches sampled)
- fashion: bounded or incomplete query: AI textile is:public fork:false archived:false (200 of 491 matches sampled)
- accessibility: bounded or incomplete query: AI audio description is:public fork:false archived:false (200 of 266 matches sampled)
- mobile: bounded or incomplete query: AI mobile media is:public fork:false archived:false (200 of 226 matches sampled)
- education: bounded or incomplete query: AI explainer pushed:>=2026-09-22 is:public fork:false archived:false (200 of 6760 matches sampled)
- education: bounded or incomplete query: AI explainer created:>=2026-09-22 is:public fork:false archived:false (200 of 4694 matches sampled)
- education: bounded or incomplete query: AI explainer is:public fork:false archived:false (200 of 39249 matches sampled)
- frontier: bounded or incomplete query: AI creative tools pushed:>=2026-09-22 is:public fork:false archived:false (200 of 272 matches sampled)
- frontier: bounded or incomplete query: AI creative tools is:public fork:false archived:false (200 of 2018 matches sampled)
- frontier: bounded or incomplete query: AI digital art is:public fork:false archived:false (200 of 739 matches sampled)
- frontier: bounded or incomplete query: AI multimedia is:public fork:false archived:false (200 of 1193 matches sampled)
- frontier: bounded or incomplete query: AI new media is:public fork:false archived:false (200 of 511 matches sampled)
- haptics: bounded or incomplete query: AI haptic is:public fork:false archived:false (300 of 301 matches sampled)
- neural-acoustics: bounded or incomplete query: neural acoustic is:public fork:false archived:false (200 of 352 matches sampled)
- agent-media-production: bounded or incomplete query: AI agent animation pushed:>=2026-09-22 is:public fork:false archived:false (200 of 213 matches sampled)
- agent-media-production: bounded or incomplete query: AI agent animation is:public fork:false archived:false (200 of 587 matches sampled)
- agent-media-production: bounded or incomplete query: AI agent video editing is:public fork:false archived:false (200 of 501 matches sampled)
- architectural-media: bounded or incomplete query: AI architectural visualization is:public fork:false archived:false (200 of 936 matches sampled)
- architectural-media: bounded or incomplete query: AI floor plan is:public fork:false archived:false (200 of 683 matches sampled)
- light-field: bounded or incomplete query: AI hologram is:public fork:false archived:false (200 of 224 matches sampled)
- neural-media-codecs: bounded or incomplete query: neural image compression is:public fork:false archived:false (200 of 297 matches sampled)
- procedural-materials: bounded or incomplete query: neural material is:public fork:false archived:false (200 of 1385 matches sampled)
- landscape-design: HTTP 502 from api.github.com/search/repositories; source not collected
- brushstroke-art: bounded or incomplete query: neural painting is:public fork:false archived:false (200 of 286 matches sampled)
- images: bounded or incomplete query: topic:diffusion is:public fork:false archived:false (500 of 1475 matches sampled)
- cel-animation: bounded or incomplete query: animation colorization is:public fork:false archived:false (500 of 2488 matches sampled)
- Watchlist wdfewwdev-web/tileweaver: HTTP 404 from api.github.com/repos/wdfewwdev-web/tileweaver; source not collected
- Watchlist gtwatts/ferrocut: HTTP 404 from api.github.com/repos/gtwatts/ferrocut; source not collected
- Watchlist justynberk/reel-kit: HTTP 404 from api.github.com/repos/justynberk/reel-kit; source not collected
- Watchlist ludovic111/kimchi: HTTP 404 from api.github.com/repos/ludovic111/kimchi; source not collected
- Watchlist voughtboysjj-rgb/ai-subtitle-generator: HTTP 404 from api.github.com/repos/voughtboysjj-rgb/ai-subtitle-generator; source not collected
- Watchlist bigeye0x0/bigeye-sticker-video: HTTP 404 from api.github.com/repos/bigeye0x0/bigeye-sticker-video; source not collected
- Watchlist licincan/blender-ai-mcp-addon: HTTP 404 from api.github.com/repos/licincan/blender-ai-mcp-addon; source not collected
- Watchlist wdfewwdev-web/tileweaver: HTTP 404 from api.github.com/repos/wdfewwdev-web/tileweaver; source not collected (earlier attempt in this observation)
- Watchlist licincan/blender-ai-mcp-addon: HTTP 404 from api.github.com/repos/licincan/blender-ai-mcp-addon; source not collected (earlier attempt in this observation)
- Watchlist ludovic111/kimchi: HTTP 404 from api.github.com/repos/ludovic111/kimchi; source not collected (earlier attempt in this observation)
- Watchlist gtwatts/ferrocut: HTTP 404 from api.github.com/repos/gtwatts/ferrocut; source not collected (earlier attempt in this observation)
- Watchlist justynberk/reel-kit: HTTP 404 from api.github.com/repos/justynberk/reel-kit; source not collected (earlier attempt in this observation)
- Watchlist ludovic111/kimchi: HTTP 404 from api.github.com/repos/ludovic111/kimchi; source not collected (earlier attempt in this observation)
- Watchlist wdfewwdev-web/tileweaver: HTTP 404 from api.github.com/repos/wdfewwdev-web/tileweaver; source not collected (earlier attempt in this observation)
- Watchlist voughtboysjj-rgb/ai-subtitle-generator: HTTP 404 from api.github.com/repos/voughtboysjj-rgb/ai-subtitle-generator; source not collected (earlier attempt in this observation)
- Watchlist gtwatts/ferrocut: HTTP 404 from api.github.com/repos/gtwatts/ferrocut; source not collected (earlier attempt in this observation)
- Watchlist ludovic111/kimchi: HTTP 404 from api.github.com/repos/ludovic111/kimchi; source not collected (earlier attempt in this observation)
- Watchlist licincan/blender-ai-mcp-addon: HTTP 404 from api.github.com/repos/licincan/blender-ai-mcp-addon; source not collected (earlier attempt in this observation)
- Watchlist bigeye0x0/bigeye-sticker-video: HTTP 404 from api.github.com/repos/bigeye0x0/bigeye-sticker-video; source not collected (earlier attempt in this observation)
- Watchlist justynberk/reel-kit: HTTP 404 from api.github.com/repos/justynberk/reel-kit; source not collected (earlier attempt in this observation)
- Watchlist ludovic111/kimchi: HTTP 404 from api.github.com/repos/ludovic111/kimchi; source not collected (earlier attempt in this observation)
- Watchlist bigeye0x0/bigeye-sticker-video: HTTP 404 from api.github.com/repos/bigeye0x0/bigeye-sticker-video; source not collected (earlier attempt in this observation)

## Style Glyph Generator

Typography, fonts & layout · Images & design · Computational art & creative coding

First full guide, completing an earlier screened library entry with installation, use and documented requirements. This is a review-depth improvement, not a verified new software release.

### Quality assessment: Quality unverified

Software licensing and a concrete creative AI use are supported. The remaining checks do not establish a recommendation.

Scope: Exploring display-letter shapes and texture treatments for posters or type studies.

Evidence checked: 2026-10-22. No local execution implied.

- **Open-source software license · verified:** The complete root software license was read and archived. The grant covers this project code; unresolved model, service and asset terms are disclosed separately. [Source](https://github.com/dx199771/font_generation/blob/main/LICENSE)
- **Creative results · documented:** README examples show generated glyph images and the two-network architecture; the linked Colab is the documented playground. [Source](https://github.com/dx199771/font_generation/blob/main/README.md)
- **Reproducible setup · documented:** Use the linked Colab or the repository playground.ipynb; install PyTorch and Beautiful Soup in a compatible environment. The README package spelling "pytorch" should be checked against current official PyTorch installation guidance. Independent reproduction has not been established in this review. [Source](https://github.com/dx199771/font_generation/blob/main/README.md)
- **Maintenance and support · unknown:** A release or active repository alone does not establish sustained support. Workflow-specific support and unresolved blockers need a deeper review.
- **Independent use · unknown:** Independent first-hand use or a working third-party integration was not established for this selected workflow.
- **Models, services and costs · documented:** Font datasets, pretrained glyph models and VGG16 files are separate downloads; their complete redistribution/commercial terms remain unresolved. Local compute plus any chosen external model or service; provider access and charges are separate. [Source](https://github.com/dx199771/font_generation/blob/main/README.md)

Documentation review only; AI Media Scout did not install or run this software. The output is glyph imagery, not a documented complete installable font. Legacy dependencies and dataset availability need reproduction.

### How it uses AI

Combines a GAN glyph generator with a CNN texture synthesizer to create textured character images. [Source](https://github.com/dx199771/font_generation/blob/main/README.md)

### Introduction

Combines a GAN glyph generator with a CNN texture synthesizer to create textured character images. [Source 1](https://github.com/dx199771/font_generation/blob/main/README.md)

### What it is good for

Exploring display-letter shapes and texture treatments for posters or type studies. [Source 1](https://github.com/dx199771/font_generation/blob/main/README.md)

### Demo & examples

README examples show generated glyph images and the two-network architecture; the linked Colab is the documented playground. [Source 1](https://github.com/dx199771/font_generation/blob/main/README.md)

### Install

Use the linked Colab or the repository playground.ipynb; install PyTorch and Beautiful Soup in a compatible environment. The README package spelling "pytorch" should be checked against current official PyTorch installation guidance. [Source 1](https://github.com/dx199771/font_generation/blob/main/README.md)

1. Obtain the official source or release linked below.
2. Use the linked Colab or the repository playground.ipynb; install PyTorch and Beautiful Soup in a compatible environment. The README package spelling "pytorch" should be checked against current official PyTorch installation guidance.
### First project

Start with a short, representative project and inspect the result before a larger batch. [Source 1](https://github.com/dx199771/font_generation/blob/main/README.md)

1. Open playground.ipynb and obtain the provided glyph data.
2. Choose or train a glyph model; for texture synthesis obtain vgg16.npy and place it in nets.
3. Inspect generated glyph images in results before using them in a composition.
### Hardware & software

Requirements below are documented for this workflow. Unspecified limits are not inferred. [Source 1](https://github.com/dx199771/font_generation/blob/main/README.md)

- **Hardware:** A GPU is explicitly required for testing and training. GPU type, VRAM, RAM and disk minimums are not documented.
- **Software:** PyTorch, Beautiful Soup, Jupyter/Colab; version pins are not documented.
- **Platforms:** The documented route is a GPU notebook. Native Windows, macOS and Linux compatibility is not established by the README.

### License, model weights & costs

The full software license was reviewed. Model weights, assets and services remain separate. [Source 1](https://github.com/dx199771/font_generation/blob/main/LICENSE) [Source 2](https://github.com/dx199771/font_generation/blob/main/README.md)

- **Code:** MIT
- **Weights:** Font datasets, pretrained glyph models and VGG16 files are separate downloads; their complete redistribution/commercial terms remain unresolved.
- **Commercial:** Software use follows MIT. Font datasets, pretrained glyph models and VGG16 files are separate downloads; their complete redistribution/commercial terms remain unresolved.
- **Cost:** Local compute plus any chosen external model or service; provider access and charges are separate.

### Why it merits attention

Included for the documented creative workflow. A complete guide and popularity do not establish output reliability. [Source 1](https://github.com/dx199771/font_generation/blob/main/README.md)

### Limitations

The output is glyph imagery, not a documented complete installable font. Legacy dependencies and dataset availability need reproduction. [Source 1](https://github.com/dx199771/font_generation/blob/main/README.md)

### Get the tool

- [Repository](https://github.com/dx199771/font_generation)
- [Documentation](https://github.com/dx199771/font_generation/blob/main/README.md)

## Hayao.js

Games & production pipelines · Interactive, immersive & live media · Computational art & creative coding · Creative learning & authoring

First full guide, completing an earlier screened library entry with installation, use and documented requirements. This is a review-depth improvement, not a verified new software release.

### Quality assessment: Quality unverified

Software licensing and a concrete creative AI use are supported. The remaining checks do not establish a recommendation.

Scope: Making small browser games and iterating on rules with an AI coding agent.

Evidence checked: 2026-10-22. No local execution implied.

- **Open-source software license · verified:** The complete root software license was read and archived. The grant covers this project code; unresolved model, service and asset terms are disclosed separately. [Source](https://github.com/hellojanpacan/hayao-js/blob/main/LICENSE)
- **Creative results · documented:** The official hayao.dev/play gallery contains playable examples; maintainer solver and determinism checks are not proof of enjoyable gameplay. [Source](https://github.com/hellojanpacan/hayao-js/blob/main/README.md) [Source](https://hayao.dev/play/)
- **Reproducible setup · documented:** Create a project with the documented scaffold, install its npm dependencies, then run the verification and development commands. Connect the optional coding-agent plugin or MCP bridge only for the AI authoring workflow. Independent reproduction has not been established in this review. [Source](https://github.com/hellojanpacan/hayao-js/blob/main/README.md) [Source](https://hayao.dev/play/)
- **Maintenance and support · unknown:** A release or active repository alone does not establish sustained support. Workflow-specific support and unresolved blockers need a deeper review.
- **Independent use · unknown:** Independent first-hand use or a working third-party integration was not established for this selected workflow.
- **Models, services and costs · documented:** The engine does not bundle an LLM. Agent/model access and imported art, fonts and audio have separate terms. Local compute plus any chosen external model or service; provider access and charges are separate. [Source](https://github.com/hellojanpacan/hayao-js/blob/main/README.md) [Source](https://hayao.dev/play/)

Documentation review only; AI Media Scout did not install or run this software. Winnability and deterministic replay do not establish fun, accessibility or polished output; human playtesting remains necessary.

### How it uses AI

An agent-oriented 2D game engine exposes deterministic simulation, solver checks and an MCP playtest bridge so an LLM can author and inspect playable games. [Source](https://github.com/hellojanpacan/hayao-js/blob/main/README.md) [Source](https://hayao.dev/play/)

### Introduction

An agent-oriented 2D game engine exposes deterministic simulation, solver checks and an MCP playtest bridge so an LLM can author and inspect playable games. [Source 1](https://github.com/hellojanpacan/hayao-js/blob/main/README.md) [Source 2](https://hayao.dev/play/)

### What it is good for

Making small browser games and iterating on rules with an AI coding agent. [Source 1](https://github.com/hellojanpacan/hayao-js/blob/main/README.md) [Source 2](https://hayao.dev/play/)

### Demo & examples

The official hayao.dev/play gallery contains playable examples; maintainer solver and determinism checks are not proof of enjoyable gameplay. [Source 1](https://github.com/hellojanpacan/hayao-js/blob/main/README.md) [Source 2](https://hayao.dev/play/)

### Install

Create a project with the documented scaffold, install its npm dependencies, then run the verification and development commands. Connect the optional coding-agent plugin or MCP bridge only for the AI authoring workflow. [Source 1](https://github.com/hellojanpacan/hayao-js/blob/main/README.md) [Source 2](https://hayao.dev/play/)

1. Obtain the official source or release linked below.
2. Create a project with the documented scaffold, install its npm dependencies, then run the verification and development commands. Connect the optional coding-agent plugin or MCP bridge only for the AI authoring workflow.

```sh
npx hayao@latest create my-game
```


```sh
cd my-game
```


```sh
npm install
```


```sh
npm run verify
```


```sh
npm run dev
```

### First project

Start with a short, representative project and inspect the result before a larger batch. [Source 1](https://github.com/hellojanpacan/hayao-js/blob/main/README.md) [Source 2](https://hayao.dev/play/)

1. Describe a small game to a compatible coding agent and edit its defineGame implementation.
2. Run the supplied verifier and inspect its actual scope.
3. Play the result and use Workshop feedback to adjust pacing and controls.
### Hardware & software

Requirements below are documented for this workflow. Unspecified limits are not inferred. [Source 1](https://github.com/hellojanpacan/hayao-js/blob/main/README.md) [Source 2](https://hayao.dev/play/)

- **Hardware:** Minimum system RAM, VRAM and total disk space are not documented in the reviewed instructions.
- **Software:** Node.js, npm, ESM/TypeScript and a modern browser; exact Node minimum is not specified in the reviewed README.
- **Platforms:** Headless simulation runs in Node; browser rendering uses SVG/Canvas/Web Audio. No native OS certification or VR support is claimed.

### License, model weights & costs

The full software license was reviewed. Model weights, assets and services remain separate. [Source 1](https://github.com/hellojanpacan/hayao-js/blob/main/LICENSE) [Source 2](https://github.com/hellojanpacan/hayao-js/blob/main/README.md) [Source 3](https://hayao.dev/play/)

- **Code:** MIT
- **Weights:** The engine does not bundle an LLM. Agent/model access and imported art, fonts and audio have separate terms.
- **Commercial:** Software use follows MIT. The engine does not bundle an LLM. Agent/model access and imported art, fonts and audio have separate terms.
- **Cost:** Local compute plus any chosen external model or service; provider access and charges are separate.

### Why it merits attention

Included for the documented creative workflow. A complete guide and popularity do not establish output reliability. [Source 1](https://github.com/hellojanpacan/hayao-js/blob/main/README.md) [Source 2](https://hayao.dev/play/)

### Limitations

Winnability and deterministic replay do not establish fun, accessibility or polished output; human playtesting remains necessary. [Source 1](https://github.com/hellojanpacan/hayao-js/blob/main/README.md) [Source 2](https://hayao.dev/play/)

### Get the tool

- [Repository](https://github.com/hellojanpacan/hayao-js)
- [Documentation](https://github.com/hellojanpacan/hayao-js/blob/main/README.md)

## Image Painting Neural Network

Neural brushstroke painting and drawn media · Images & design · Computational art & creative coding · Creative learning & authoring

First full guide, completing an earlier screened library entry with installation, use and documented requirements. This is a review-depth improvement, not a verified new software release.

### Quality assessment: Quality unverified

Software licensing and a concrete creative AI use are supported. The remaining checks do not establish a recommendation.

Scope: Showing the learning process as an abstract animation or teaching neural image representations.

Evidence checked: 2026-10-22. No local execution implied.

- **Open-source software license · verified:** The complete root software license was read and archived. The grant covers this project code; unresolved model, service and asset terms are disclosed separately. [Source](https://github.com/guiferviz/nn_painting_tensorflow/blob/master/LICENSE)
- **Creative results · documented:** The README includes rainbow and Rubik-cube training GIFs. [Source](https://github.com/guiferviz/nn_painting_tensorflow/blob/master/README.md)
- **Reproducible setup · documented:** Obtain the source and a compatible legacy TensorFlow/Python environment. FFmpeg is needed for the optional video/GIF helper scripts; the README does not provide a pinned installation environment. Independent reproduction has not been established in this review. [Source](https://github.com/guiferviz/nn_painting_tensorflow/blob/master/README.md)
- **Maintenance and support · unknown:** A release or active repository alone does not establish sustained support. Workflow-specific support and unresolved blockers need a deeper review.
- **Independent use · unknown:** Independent first-hand use or a working third-party integration was not established for this selected workflow.
- **Models, services and costs · documented:** No separate model download is specified for coordinate fitting. Sample images and borrowed course components retain their own rights and attributions. Local compute plus any chosen external model or service; provider access and charges are separate. [Source](https://github.com/guiferviz/nn_painting_tensorflow/blob/master/README.md)

Documentation review only; AI Media Scout did not install or run this software. This is an older code workflow with no reproducibility confirmation in this review; its pixel fitting is not a physical brush or robotic painting system.

### How it uses AI

Trains a neural network to map pixel coordinates to RGB values and saves the evolving reconstruction as a sequence of images. [Source](https://github.com/guiferviz/nn_painting_tensorflow/blob/master/README.md)

### Introduction

Trains a neural network to map pixel coordinates to RGB values and saves the evolving reconstruction as a sequence of images. [Source 1](https://github.com/guiferviz/nn_painting_tensorflow/blob/master/README.md)

### What it is good for

Showing the learning process as an abstract animation or teaching neural image representations. [Source 1](https://github.com/guiferviz/nn_painting_tensorflow/blob/master/README.md)

### Demo & examples

The README includes rainbow and Rubik-cube training GIFs. [Source 1](https://github.com/guiferviz/nn_painting_tensorflow/blob/master/README.md)

### Install

Obtain the source and a compatible legacy TensorFlow/Python environment. FFmpeg is needed for the optional video/GIF helper scripts; the README does not provide a pinned installation environment. [Source 1](https://github.com/guiferviz/nn_painting_tensorflow/blob/master/README.md)

1. Obtain the official source or release linked below.
2. Obtain the source and a compatible legacy TensorFlow/Python environment. FFmpeg is needed for the optional video/GIF helper scripts; the README does not provide a pinned installation environment.

```sh
python main.py input/my-image.png
```


```sh
python main.py -h
```

### First project

Start with a short, representative project and inspect the result before a larger batch. [Source 1](https://github.com/guiferviz/nn_painting_tensorflow/blob/master/README.md)

1. Choose an image you are entitled to use.
2. Run main.py with that image and inspect the iteration frames created under output.
3. Stop training at a useful visual stage; optionally assemble frames with the documented make_video.sh helper.
### Hardware & software

Requirements below are documented for this workflow. Unspecified limits are not inferred. [Source 1](https://github.com/guiferviz/nn_painting_tensorflow/blob/master/README.md)

- **Hardware:** Minimum system RAM, VRAM and total disk space are not documented in the reviewed instructions.
- **Software:** Python, TensorFlow and FFmpeg for movie conversion; exact versions are not documented.
- **Platforms:** The examples use Python and shell helpers; a complete Windows/macOS/Linux support matrix is not documented.

### License, model weights & costs

The full software license was reviewed. Model weights, assets and services remain separate. [Source 1](https://github.com/guiferviz/nn_painting_tensorflow/blob/master/LICENSE) [Source 2](https://github.com/guiferviz/nn_painting_tensorflow/blob/master/README.md)

- **Code:** MIT
- **Weights:** No separate model download is specified for coordinate fitting. Sample images and borrowed course components retain their own rights and attributions.
- **Commercial:** Software use follows MIT. No separate model download is specified for coordinate fitting. Sample images and borrowed course components retain their own rights and attributions.
- **Cost:** Local compute plus any chosen external model or service; provider access and charges are separate.

### Why it merits attention

Included for the documented creative workflow. A complete guide and popularity do not establish output reliability. [Source 1](https://github.com/guiferviz/nn_painting_tensorflow/blob/master/README.md)

### Limitations

This is an older code workflow with no reproducibility confirmation in this review; its pixel fitting is not a physical brush or robotic painting system. [Source 1](https://github.com/guiferviz/nn_painting_tensorflow/blob/master/README.md)

### Get the tool

- [Repository](https://github.com/guiferviz/nn_painting_tensorflow)
- [Documentation](https://github.com/guiferviz/nn_painting_tensorflow/blob/master/README.md)

## Architecture Diagram Generator

Vector graphics, illustration & textures · Data art & scientific visualization · Creative publishing & presentation · Creative learning & authoring

First full guide, completing an earlier screened library entry with installation, use and documented requirements. This is a review-depth improvement, not a verified new software release.

### Quality assessment: Quality unverified

Software licensing and a concrete creative AI use are supported. The remaining checks do not establish a recommendation.

Scope: Explaining creative software pipelines, installations and production systems in presentations.

Evidence checked: 2026-10-22. No local execution implied.

- **Open-source software license · verified:** The complete root software license was read and archived. The grant covers this project code; unresolved model, service and asset terms are disclosed separately. [Source](https://github.com/Cocoon-AI/architecture-diagram-generator/blob/main/LICENSE)
- **Creative results · documented:** The README shows web-app, serverless and microservice diagram examples, with PNG/PDF export controls. [Source](https://github.com/Cocoon-AI/architecture-diagram-generator/blob/main/README.md)
- **Reproducible setup · documented:** Download the provided architecture-diagram.zip and install it as a custom Claude skill, or make its SKILL.md and template available to a supported agent. Follow the current host instructions for enabling skills. Independent reproduction has not been established in this review. [Source](https://github.com/Cocoon-AI/architecture-diagram-generator/blob/main/README.md)
- **Maintenance and support · unknown:** A release or active repository alone does not establish sustained support. Workflow-specific support and unresolved blockers need a deeper review.
- **Independent use · unknown:** Independent first-hand use or a working third-party integration was not established for this selected workflow.
- **Models, services and costs · documented:** The MIT template/skill is separate from the proprietary AI host. Google Fonts may be loaded by the generated template. The skill is MIT licensed; AI-host access and usage limits are separate. No current price is asserted. [Source](https://github.com/Cocoon-AI/architecture-diagram-generator/blob/main/README.md)

Documentation review only; AI Media Scout did not install or run this software. Diagram accuracy and visual quality require review; do not treat an AI-generated connection as verified system documentation.

### How it uses AI

Provides an AI-agent skill and HTML/SVG template that turn a system description into editable architecture diagrams. [Source](https://github.com/Cocoon-AI/architecture-diagram-generator/blob/main/README.md)

### Introduction

Provides an AI-agent skill and HTML/SVG template that turn a system description into editable architecture diagrams. [Source 1](https://github.com/Cocoon-AI/architecture-diagram-generator/blob/main/README.md)

### What it is good for

Explaining creative software pipelines, installations and production systems in presentations. [Source 1](https://github.com/Cocoon-AI/architecture-diagram-generator/blob/main/README.md)

### Demo & examples

The README shows web-app, serverless and microservice diagram examples, with PNG/PDF export controls. [Source 1](https://github.com/Cocoon-AI/architecture-diagram-generator/blob/main/README.md)

### Install

Download the provided architecture-diagram.zip and install it as a custom Claude skill, or make its SKILL.md and template available to a supported agent. Follow the current host instructions for enabling skills. [Source 1](https://github.com/Cocoon-AI/architecture-diagram-generator/blob/main/README.md)

1. Obtain the official source or release linked below.
2. Download the provided architecture-diagram.zip and install it as a custom Claude skill, or make its SKILL.md and template available to a supported agent. Follow the current host instructions for enabling skills.
### First project

Start with a short, representative project and inspect the result before a larger batch. [Source 1](https://github.com/Cocoon-AI/architecture-diagram-generator/blob/main/README.md)

1. Write a short description of components and connections.
2. Ask the agent to create an architecture diagram using the template.
3. Open the resulting HTML, correct labels and connections, then use its PNG or PDF export.
### Hardware & software

Requirements below are documented for this workflow. Unspecified limits are not inferred. [Source 1](https://github.com/Cocoon-AI/architecture-diagram-generator/blob/main/README.md)

- **Hardware:** Minimum system RAM, VRAM and total disk space are not documented in the reviewed instructions.
- **Software:** A supported AI-agent host and a modern browser. No Python environment or model download is specified for the template workflow.
- **Platforms:** The output is browser-readable HTML/SVG. The README documents Claude web and CLI routes; it does not certify all operating systems.

### License, model weights & costs

The full software license was reviewed. Model weights, assets and services remain separate. [Source 1](https://github.com/Cocoon-AI/architecture-diagram-generator/blob/main/LICENSE) [Source 2](https://github.com/Cocoon-AI/architecture-diagram-generator/blob/main/README.md)

- **Code:** MIT
- **Weights:** The MIT template/skill is separate from the proprietary AI host. Google Fonts may be loaded by the generated template.
- **Commercial:** Software use follows MIT. The MIT template/skill is separate from the proprietary AI host. Google Fonts may be loaded by the generated template.
- **Cost:** The skill is MIT licensed; AI-host access and usage limits are separate. No current price is asserted.

### Why it merits attention

Included for the documented creative workflow. A complete guide and popularity do not establish output reliability. [Source 1](https://github.com/Cocoon-AI/architecture-diagram-generator/blob/main/README.md)

### Limitations

Diagram accuracy and visual quality require review; do not treat an AI-generated connection as verified system documentation. [Source 1](https://github.com/Cocoon-AI/architecture-diagram-generator/blob/main/README.md)

### Get the tool

- [Repository](https://github.com/Cocoon-AI/architecture-diagram-generator)
- [Documentation](https://github.com/Cocoon-AI/architecture-diagram-generator/blob/main/README.md)

## Shader Architect

Neural procedural material authoring · Computational art & creative coding · Browser tools & web media · Images & design

First full guide, completing an earlier screened library entry with installation, use and documented requirements. This is a review-depth improvement, not a verified new software release.

### Quality assessment: Quality unverified

Software licensing and a concrete creative AI use are supported. The remaining checks do not establish a recommendation.

Scope: Prototyping glass, chrome, holographic surfaces or animated noise for interface and motion concepts.

Evidence checked: 2026-10-22. No local execution implied.

- **Open-source software license · verified:** The complete root software license was read and archived. The grant covers this project code; unresolved model, service and asset terms are disclosed separately. [Source](https://github.com/alessiamatteucci/Shader-Architect/blob/main/LICENSE)
- **Creative results · documented:** The repository supplies five design recipes; it explicitly says they are not already compiled or visually verified shaders. [Source](https://github.com/alessiamatteucci/Shader-Architect/blob/main/README.md)
- **Reproducible setup · documented:** Copy the shader-architect folder to the supported agent skill directory, connect the official Figma MCP server and install the required figma-shaders capability. Without that connection the documented output is a technical brief only. Independent reproduction has not been established in this review. [Source](https://github.com/alessiamatteucci/Shader-Architect/blob/main/README.md)
- **Maintenance and support · unknown:** A release or active repository alone does not establish sustained support. Workflow-specific support and unresolved blockers need a deeper review.
- **Independent use · unknown:** Independent first-hand use or a working third-party integration was not established for this selected workflow.
- **Models, services and costs · documented:** The MIT skill does not include the AI model, Figma service or shader runtime permissions; those hosts retain their terms. AI-agent and Figma plan costs/access are separate from the MIT skill. [Source](https://github.com/alessiamatteucci/Shader-Architect/blob/main/README.md)

Documentation review only; AI Media Scout did not install or run this software. Examples are recipes, not verified results. A successful compile and a successful visual review are distinct, and Figma APIs may change.

### How it uses AI

An agent skill translates material references into parameterized Figma WebGPU/WGSL shaders through Figma MCP. [Source](https://github.com/alessiamatteucci/Shader-Architect/blob/main/README.md)

### Introduction

An agent skill translates material references into parameterized Figma WebGPU/WGSL shaders through Figma MCP. [Source 1](https://github.com/alessiamatteucci/Shader-Architect/blob/main/README.md)

### What it is good for

Prototyping glass, chrome, holographic surfaces or animated noise for interface and motion concepts. [Source 1](https://github.com/alessiamatteucci/Shader-Architect/blob/main/README.md)

### Demo & examples

The repository supplies five design recipes; it explicitly says they are not already compiled or visually verified shaders. [Source 1](https://github.com/alessiamatteucci/Shader-Architect/blob/main/README.md)

### Install

Copy the shader-architect folder to the supported agent skill directory, connect the official Figma MCP server and install the required figma-shaders capability. Without that connection the documented output is a technical brief only. [Source 1](https://github.com/alessiamatteucci/Shader-Architect/blob/main/README.md)

1. Obtain the official source or release linked below.
2. Copy the shader-architect folder to the supported agent skill directory, connect the official Figma MCP server and install the required figma-shaders capability. Without that connection the documented output is a technical brief only.
### First project

Start with a short, representative project and inspect the result before a larger batch. [Source 1](https://github.com/alessiamatteucci/Shader-Architect/blob/main/README.md)

1. Use ANALYZE to describe a reference and intended controls.
2. Use CREATE for a new shader in the connected Figma account.
3. Inspect the resulting shader and use REFINE for a narrowly described adjustment.
### Hardware & software

Requirements below are documented for this workflow. Unspecified limits are not inferred. [Source 1](https://github.com/alessiamatteucci/Shader-Architect/blob/main/README.md)

- **Hardware:** Minimum system RAM, VRAM and total disk space are not documented in the reviewed instructions.
- **Software:** A skill-capable agent, Figma account, official Figma MCP shader tools and figma-shaders skill.
- **Platforms:** Figma and agent host support determines compatibility; local OS, RAM and GPU minima are not documented here.

### License, model weights & costs

The full software license was reviewed. Model weights, assets and services remain separate. [Source 1](https://github.com/alessiamatteucci/Shader-Architect/blob/main/LICENSE) [Source 2](https://github.com/alessiamatteucci/Shader-Architect/blob/main/README.md)

- **Code:** MIT
- **Weights:** The MIT skill does not include the AI model, Figma service or shader runtime permissions; those hosts retain their terms.
- **Commercial:** Software use follows MIT. The MIT skill does not include the AI model, Figma service or shader runtime permissions; those hosts retain their terms.
- **Cost:** AI-agent and Figma plan costs/access are separate from the MIT skill.

### Why it merits attention

Included for the documented creative workflow. A complete guide and popularity do not establish output reliability. [Source 1](https://github.com/alessiamatteucci/Shader-Architect/blob/main/README.md)

### Limitations

Examples are recipes, not verified results. A successful compile and a successful visual review are distinct, and Figma APIs may change. [Source 1](https://github.com/alessiamatteucci/Shader-Architect/blob/main/README.md)

### Get the tool

- [Repository](https://github.com/alessiamatteucci/Shader-Architect)
- [Documentation](https://github.com/alessiamatteucci/Shader-Architect/blob/main/README.md)

## SVG Animator

Vector graphics, illustration & textures · AI kinetic typography and animated lettering · Data art & scientific visualization · Creative publishing & presentation

First full guide, completing an earlier screened library entry with installation, use and documented requirements. This is a review-depth improvement, not a verified new software release.

### Quality assessment: Quality unverified

Software licensing and a concrete creative AI use are supported. The remaining checks do not establish a recommendation.

Scope: Creating animated flow diagrams, explainer graphics and simple looping SVG artwork.

Evidence checked: 2026-10-22. No local execution implied.

- **Open-source software license · verified:** The complete root software license was read and archived. The grant covers this project code; unresolved model, service and asset terms are disclosed separately. [Source](https://github.com/takimdigital/svg-animator/blob/main/LICENSE)
- **Creative results · documented:** The repository includes animated example SVGs and a gallery. Structural validation does not establish visual quality. [Source](https://github.com/takimdigital/svg-animator/blob/main/README.md)
- **Reproducible setup · documented:** Obtain the repository and optionally install it as an agent skill. Use Python for the pipeline; Playwright plus Chromium is required to render review frames but not to generate or lint SVG. Independent reproduction has not been established in this review. [Source](https://github.com/takimdigital/svg-animator/blob/main/README.md)
- **Maintenance and support · unknown:** A release or active repository alone does not establish sustained support. Workflow-specific support and unresolved blockers need a deeper review.
- **Independent use · unknown:** Independent first-hand use or a working third-party integration was not established for this selected workflow.
- **Models, services and costs · documented:** AI authoring requires a separate agent/model. The deterministic generator can operate without an AI call. Local compute plus any chosen external model or service; provider access and charges are separate. [Source](https://github.com/takimdigital/svg-animator/blob/main/README.md)

Documentation review only; AI Media Scout did not install or run this software. The fallback first frame must be complete. Automated lint passes cannot establish readable text, good motion or an attractive composition.

### How it uses AI

Combines an AI-agent authoring skill with JSON-driven SVG generators, linting and frame rendering for animated diagrams and illustrations. [Source](https://github.com/takimdigital/svg-animator/blob/main/README.md)

### Introduction

Combines an AI-agent authoring skill with JSON-driven SVG generators, linting and frame rendering for animated diagrams and illustrations. [Source 1](https://github.com/takimdigital/svg-animator/blob/main/README.md)

### What it is good for

Creating animated flow diagrams, explainer graphics and simple looping SVG artwork. [Source 1](https://github.com/takimdigital/svg-animator/blob/main/README.md)

### Demo & examples

The repository includes animated example SVGs and a gallery. Structural validation does not establish visual quality. [Source 1](https://github.com/takimdigital/svg-animator/blob/main/README.md)

### Install

Obtain the repository and optionally install it as an agent skill. Use Python for the pipeline; Playwright plus Chromium is required to render review frames but not to generate or lint SVG. [Source 1](https://github.com/takimdigital/svg-animator/blob/main/README.md)

1. Obtain the official source or release linked below.
2. Obtain the repository and optionally install it as an agent skill. Use Python for the pipeline; Playwright plus Chromium is required to render review frames but not to generate or lint SVG.

```sh
python scripts/run_pipeline.py assets/specs/flow-with-feedback.json --out-dir run --name my-diagram
```

### First project

Start with a short, representative project and inspect the result before a larger batch. [Source 1](https://github.com/takimdigital/svg-animator/blob/main/README.md)

1. Choose a diagram specification or ask the agent to write one.
2. Run the pipeline and inspect rendered PNG frames at several times.
3. Refine labels and timing, then embed or export the resulting SVG.
### Hardware & software

Requirements below are documented for this workflow. Unspecified limits are not inferred. [Source 1](https://github.com/takimdigital/svg-animator/blob/main/README.md)

- **Hardware:** Minimum system RAM, VRAM and total disk space are not documented in the reviewed instructions.
- **Software:** Python; Playwright and Chromium for rendering. Exact Python version and OS support are not documented in the reviewed quickstart.
- **Platforms:** Generated SVG is intended for browser/image embedding; hover and JavaScript do not run when embedded as an img.

### License, model weights & costs

The full software license was reviewed. Model weights, assets and services remain separate. [Source 1](https://github.com/takimdigital/svg-animator/blob/main/LICENSE) [Source 2](https://github.com/takimdigital/svg-animator/blob/main/README.md)

- **Code:** MIT
- **Weights:** AI authoring requires a separate agent/model. The deterministic generator can operate without an AI call.
- **Commercial:** Software use follows MIT. AI authoring requires a separate agent/model. The deterministic generator can operate without an AI call.
- **Cost:** Local compute plus any chosen external model or service; provider access and charges are separate.

### Why it merits attention

Included for the documented creative workflow. A complete guide and popularity do not establish output reliability. [Source 1](https://github.com/takimdigital/svg-animator/blob/main/README.md)

### Limitations

The fallback first frame must be complete. Automated lint passes cannot establish readable text, good motion or an attractive composition. [Source 1](https://github.com/takimdigital/svg-animator/blob/main/README.md)

### Get the tool

- [Repository](https://github.com/takimdigital/svg-animator)
- [Documentation](https://github.com/takimdigital/svg-animator/blob/main/README.md)

## TianGong

Typography, fonts & layout · Browser tools & web media · Images & design · Creative publishing & presentation

First full guide, completing an earlier screened library entry with installation, use and documented requirements. This is a review-depth improvement, not a verified new software release.

### Quality assessment: Quality unverified

Software licensing and a concrete creative AI use are supported. The remaining checks do not establish a recommendation.

Scope: Developing interface concepts or visual briefs informed by calligraphy, ink painting, porcelain and garden composition.

Evidence checked: 2026-10-22. No local execution implied.

- **Open-source software license · verified:** The complete root software license was read and archived. The grant covers this project code; unresolved model, service and asset terms are disclosed separately. [Source](https://github.com/wuji-labs/tiangong/blob/main/LICENSE)
- **Creative results · documented:** The repository contains landing-page, palette and design-review examples; its benchmark scenarios have not been run. [Source](https://github.com/wuji-labs/tiangong/blob/main/README.md)
- **Reproducible setup · documented:** Copy the appropriate skill directory into a supported agent, or use the documented Cursor/Kiro configuration route. This is an agent reference workflow, not a standalone generative model. Independent reproduction has not been established in this review. [Source](https://github.com/wuji-labs/tiangong/blob/main/README.md)
- **Maintenance and support · unknown:** A release or active repository alone does not establish sustained support. Workflow-specific support and unresolved blockers need a deeper review.
- **Independent use · unknown:** Independent first-hand use or a working third-party integration was not established for this selected workflow.
- **Models, services and costs · documented:** The MIT skill does not include a model; host terms and any generated/used assets are separate. Local compute plus any chosen external model or service; provider access and charges are separate. [Source](https://github.com/wuji-labs/tiangong/blob/main/README.md)

Documentation review only; AI Media Scout did not install or run this software. Aesthetic claims are the author’s framing, not measured superiority. The unrun benchmark cannot support a recommendation.

### How it uses AI

An AI design skill provides Chinese aesthetic references and a structured design method for language-model-assisted layouts, palettes and reviews. [Source](https://github.com/wuji-labs/tiangong/blob/main/README.md)

### Introduction

An AI design skill provides Chinese aesthetic references and a structured design method for language-model-assisted layouts, palettes and reviews. [Source 1](https://github.com/wuji-labs/tiangong/blob/main/README.md)

### What it is good for

Developing interface concepts or visual briefs informed by calligraphy, ink painting, porcelain and garden composition. [Source 1](https://github.com/wuji-labs/tiangong/blob/main/README.md)

### Demo & examples

The repository contains landing-page, palette and design-review examples; its benchmark scenarios have not been run. [Source 1](https://github.com/wuji-labs/tiangong/blob/main/README.md)

### Install

Copy the appropriate skill directory into a supported agent, or use the documented Cursor/Kiro configuration route. This is an agent reference workflow, not a standalone generative model. [Source 1](https://github.com/wuji-labs/tiangong/blob/main/README.md)

1. Obtain the official source or release linked below.
2. Copy the appropriate skill directory into a supported agent, or use the documented Cursor/Kiro configuration route. This is an agent reference workflow, not a standalone generative model.
### First project

Start with a short, representative project and inspect the result before a larger batch. [Source 1](https://github.com/wuji-labs/tiangong/blob/main/README.md)

1. Give the agent a concrete design brief and audience.
2. Ask it to apply the skill to a layout or palette and explain the design choices.
3. Review the result for readability, cultural context and practical fit.
### Hardware & software

Requirements below are documented for this workflow. Unspecified limits are not inferred. [Source 1](https://github.com/wuji-labs/tiangong/blob/main/README.md)

- **Hardware:** Minimum system RAM, VRAM and total disk space are not documented in the reviewed instructions.
- **Software:** A compatible skills/rules-based AI agent; no separate runtime or model version is specified.
- **Platforms:** The README lists Claude Code, Codex, OpenClaw, Cursor and Kiro routes. OS support is inherited from the chosen host, not verified here.

### License, model weights & costs

The full software license was reviewed. Model weights, assets and services remain separate. [Source 1](https://github.com/wuji-labs/tiangong/blob/main/LICENSE) [Source 2](https://github.com/wuji-labs/tiangong/blob/main/README.md)

- **Code:** MIT
- **Weights:** The MIT skill does not include a model; host terms and any generated/used assets are separate.
- **Commercial:** Software use follows MIT. The MIT skill does not include a model; host terms and any generated/used assets are separate.
- **Cost:** Local compute plus any chosen external model or service; provider access and charges are separate.

### Why it merits attention

Included for the documented creative workflow. A complete guide and popularity do not establish output reliability. [Source 1](https://github.com/wuji-labs/tiangong/blob/main/README.md)

### Limitations

Aesthetic claims are the author’s framing, not measured superiority. The unrun benchmark cannot support a recommendation. [Source 1](https://github.com/wuji-labs/tiangong/blob/main/README.md)

### Get the tool

- [Repository](https://github.com/wuji-labs/tiangong)
- [Documentation](https://github.com/wuji-labs/tiangong/blob/main/README.md)

## Inpaint Anything for Stable Diffusion Web UI

Images & design · Photography, restoration & color · VFX, compositing & relighting · Editing, captions & post-production

First full guide in this library, establishing a documentation baseline; not a claim of a launch or significant update today.

### Quality assessment: Quality unverified

Software licensing and a concrete creative AI use are supported. The remaining checks do not establish a recommendation.

Scope: Replacing an object, repairing a background or exporting a detailed mask for a compositing task.

Evidence checked: 2026-10-22. No local execution implied.

- **Open-source software license · verified:** The complete root software license was read and archived. The grant covers this project code; unresolved model, service and asset terms are disclosed separately. [Source](https://github.com/Uminosachi/sd-webui-inpaint-anything/blob/main/LICENSE)
- **Creative results · documented:** The README shows the browser interface and documents mask, inpainting, cleaner and ControlNet workflows. [Source](https://github.com/Uminosachi/sd-webui-inpaint-anything/blob/main/README.md)
- **Reproducible setup · documented:** In AUTOMATIC1111 Web UI 1.3.0 or newer, install the repository URL through Extensions, restart, and download a compatible segmentation checkpoint from the Inpaint Anything tab. Independent reproduction has not been established in this review. [Source](https://github.com/Uminosachi/sd-webui-inpaint-anything/blob/main/README.md)
- **Maintenance and support · unknown:** A release or active repository alone does not establish sustained support. Workflow-specific support and unresolved blockers need a deeper review.
- **Independent use · unknown:** Independent first-hand use or a working third-party integration was not established for this selected workflow.
- **Models, services and costs · documented:** Apache-2.0 extension code is separate from SAM variants, inpainting checkpoints, optional ControlNet and cleaner dependencies; selected model terms need review. Local compute plus any chosen external model or service; provider access and charges are separate. [Source](https://github.com/Uminosachi/sd-webui-inpaint-anything/blob/main/README.md)

Documentation review only; AI Media Scout did not install or run this software. Larger SAM models consume more VRAM; no numeric minimum is given. Browser privacy extensions can interfere with sketch-mask retrieval, and older Gradio can display a small mask.

### How it uses AI

Uses Segment Anything-family masks to select image regions for Stable Diffusion inpainting, outpainting or cleaner workflows. [Source](https://github.com/Uminosachi/sd-webui-inpaint-anything/blob/main/README.md)

### Introduction

Uses Segment Anything-family masks to select image regions for Stable Diffusion inpainting, outpainting or cleaner workflows. [Source 1](https://github.com/Uminosachi/sd-webui-inpaint-anything/blob/main/README.md)

### What it is good for

Replacing an object, repairing a background or exporting a detailed mask for a compositing task. [Source 1](https://github.com/Uminosachi/sd-webui-inpaint-anything/blob/main/README.md)

### Demo & examples

The README shows the browser interface and documents mask, inpainting, cleaner and ControlNet workflows. [Source 1](https://github.com/Uminosachi/sd-webui-inpaint-anything/blob/main/README.md)

### Install

In AUTOMATIC1111 Web UI 1.3.0 or newer, install the repository URL through Extensions, restart, and download a compatible segmentation checkpoint from the Inpaint Anything tab. [Source 1](https://github.com/Uminosachi/sd-webui-inpaint-anything/blob/main/README.md)

1. Obtain the official source or release linked below.
2. In AUTOMATIC1111 Web UI 1.3.0 or newer, install the repository URL through Extensions, restart, and download a compatible segmentation checkpoint from the Inpaint Anything tab.
### First project

Start with a short, representative project and inspect the result before a larger batch. [Source 1](https://github.com/Uminosachi/sd-webui-inpaint-anything/blob/main/README.md)

1. Load an image and run segmentation.
2. Select the desired region, create the mask and adjust its boundary.
3. Choose an inpainting checkpoint and prompt, generate a small test, then inspect seams and preserved content.
### Hardware & software

Requirements below are documented for this workflow. Unspecified limits are not inferred. [Source 1](https://github.com/Uminosachi/sd-webui-inpaint-anything/blob/main/README.md)

- **Hardware:** VRAM use varies with SAM size and the inpainting model. Minimum GPU, VRAM, RAM and storage are not documented by this extension.
- **Software:** AUTOMATIC1111 Web UI >=1.3.0; segmentation and inpainting models; optional ControlNet extension/models and xformers.
- **Platforms:** Windows batch and Linux/macOS Python paths are documented. Actual acceleration depends on the host Web UI, PyTorch and selected models; browser access does not establish universal backend support.

### License, model weights & costs

The full software license was reviewed. Model weights, assets and services remain separate. [Source 1](https://github.com/Uminosachi/sd-webui-inpaint-anything/blob/main/LICENSE) [Source 2](https://github.com/Uminosachi/sd-webui-inpaint-anything/blob/main/README.md)

- **Code:** Apache-2.0
- **Weights:** Apache-2.0 extension code is separate from SAM variants, inpainting checkpoints, optional ControlNet and cleaner dependencies; selected model terms need review.
- **Commercial:** Software use follows Apache-2.0. Apache-2.0 extension code is separate from SAM variants, inpainting checkpoints, optional ControlNet and cleaner dependencies; selected model terms need review.
- **Cost:** Local compute plus any chosen external model or service; provider access and charges are separate.

### Why it merits attention

Included for the documented creative workflow. A complete guide and popularity do not establish output reliability. [Source 1](https://github.com/Uminosachi/sd-webui-inpaint-anything/blob/main/README.md)

### Limitations

Larger SAM models consume more VRAM; no numeric minimum is given. Browser privacy extensions can interfere with sketch-mask retrieval, and older Gradio can display a small mask. [Source 1](https://github.com/Uminosachi/sd-webui-inpaint-anything/blob/main/README.md)

### Get the tool

- [Repository](https://github.com/Uminosachi/sd-webui-inpaint-anything)
- [Documentation](https://github.com/Uminosachi/sd-webui-inpaint-anything/blob/main/README.md)

## BlenderLLM

3D, reconstruction & assets · AI parametric design and jewelry · 3D printing & generative CAD

First full guide in this library, establishing a documentation baseline; not a claim of a launch or significant update today.

### Quality assessment: Quality unverified

Software licensing and a concrete creative AI use are supported. The remaining checks do not establish a recommendation.

Scope: Drafting simple 3D object concepts and studying text-to-CAD scripting.

Evidence checked: 2026-10-22. No local execution implied.

- **Open-source software license · verified:** The complete root software license was read and archived. The grant covers this project code; unresolved model, service and asset terms are disclosed separately. [Source](https://github.com/FreedomIntelligence/BlenderLLM/blob/main/LICENSE)
- **Creative results · documented:** The README and paper show model examples and CADBench evaluations; benchmark claims have not been independently reproduced here. [Source](https://github.com/FreedomIntelligence/BlenderLLM/blob/main/README.md) [Source](https://huggingface.co/FreedomIntelligence/BlenderLLM)
- **Reproducible setup · documented:** Install the repository requirements, download BlenderLLM weights, and make a Blender executable available for the rendering route. Use chat.py first to inspect generated code before considering modeling.py. Independent reproduction has not been established in this review. [Source](https://github.com/FreedomIntelligence/BlenderLLM/blob/main/README.md) [Source](https://huggingface.co/FreedomIntelligence/BlenderLLM)
- **Maintenance and support · unknown:** A release or active repository alone does not establish sustained support. Workflow-specific support and unresolved blockers need a deeper review.
- **Independent use · unknown:** Independent first-hand use or a working third-party integration was not established for this selected workflow.
- **Models, services and costs · documented:** Apache-2.0 repository code; BlenderLLM, its Qwen backbone and datasets have separate model/data terms that require their own check. Local compute plus any chosen external model or service; provider access and charges are separate. [Source](https://github.com/FreedomIntelligence/BlenderLLM/blob/main/README.md) [Source](https://huggingface.co/FreedomIntelligence/BlenderLLM)

Documentation review only; AI Media Scout did not install or run this software. The authors state limitations in advanced materials/structural detail, multimodal input and multi-turn interaction. Generated geometry is not certified printable or mechanically valid.

### How it uses AI

A Qwen2.5-Coder-7B-derived model generates Blender Python scripts from text instructions and can render the resulting geometry. [Source](https://github.com/FreedomIntelligence/BlenderLLM/blob/main/README.md) [Source](https://huggingface.co/FreedomIntelligence/BlenderLLM)

### Introduction

A Qwen2.5-Coder-7B-derived model generates Blender Python scripts from text instructions and can render the resulting geometry. [Source 1](https://github.com/FreedomIntelligence/BlenderLLM/blob/main/README.md) [Source 2](https://huggingface.co/FreedomIntelligence/BlenderLLM)

### What it is good for

Drafting simple 3D object concepts and studying text-to-CAD scripting. [Source 1](https://github.com/FreedomIntelligence/BlenderLLM/blob/main/README.md) [Source 2](https://huggingface.co/FreedomIntelligence/BlenderLLM)

### Demo & examples

The README and paper show model examples and CADBench evaluations; benchmark claims have not been independently reproduced here. [Source 1](https://github.com/FreedomIntelligence/BlenderLLM/blob/main/README.md) [Source 2](https://huggingface.co/FreedomIntelligence/BlenderLLM)

### Install

Install the repository requirements, download BlenderLLM weights, and make a Blender executable available for the rendering route. Use chat.py first to inspect generated code before considering modeling.py. [Source 1](https://github.com/FreedomIntelligence/BlenderLLM/blob/main/README.md) [Source 2](https://huggingface.co/FreedomIntelligence/BlenderLLM)

1. Obtain the official source or release linked below.
2. Install the repository requirements, download BlenderLLM weights, and make a Blender executable available for the rendering route. Use chat.py first to inspect generated code before considering modeling.py.

```sh
pip install -r requirements.txt
```


```sh
python chat.py --model_name FreedomIntelligence/BlenderLLM --prompt "Create a simple table"
```

### First project

Start with a short, representative project and inspect the result before a larger batch. [Source 1](https://github.com/FreedomIntelligence/BlenderLLM/blob/main/README.md) [Source 2](https://huggingface.co/FreedomIntelligence/BlenderLLM)

1. Describe a simple object with clear dimensions and parts.
2. Inspect the generated bpy script.
3. If using the rendering workflow, configure Blender and an output folder, then inspect geometry and render results before downstream use.
### Hardware & software

Requirements below are documented for this workflow. Unspecified limits are not inferred. [Source 1](https://github.com/FreedomIntelligence/BlenderLLM/blob/main/README.md) [Source 2](https://huggingface.co/FreedomIntelligence/BlenderLLM)

- **Hardware:** Minimum system RAM, VRAM and total disk space are not documented in the reviewed instructions.
- **Software:** Python dependencies in requirements.txt, downloaded model weights, and Blender for script execution/rendering. Exact Blender minimum is not specified.
- **Platforms:** The README gives executable-path examples for Windows, macOS and Linux; supported model-inference hardware per OS is not established.

### License, model weights & costs

The full software license was reviewed. Model weights, assets and services remain separate. [Source 1](https://github.com/FreedomIntelligence/BlenderLLM/blob/main/LICENSE) [Source 2](https://github.com/FreedomIntelligence/BlenderLLM/blob/main/README.md) [Source 3](https://huggingface.co/FreedomIntelligence/BlenderLLM)

- **Code:** Apache-2.0
- **Weights:** Apache-2.0 repository code; BlenderLLM, its Qwen backbone and datasets have separate model/data terms that require their own check.
- **Commercial:** Software use follows Apache-2.0. Apache-2.0 repository code; BlenderLLM, its Qwen backbone and datasets have separate model/data terms that require their own check.
- **Cost:** Local compute plus any chosen external model or service; provider access and charges are separate.

### Why it merits attention

Included for the documented creative workflow. A complete guide and popularity do not establish output reliability. [Source 1](https://github.com/FreedomIntelligence/BlenderLLM/blob/main/README.md) [Source 2](https://huggingface.co/FreedomIntelligence/BlenderLLM)

### Limitations

The authors state limitations in advanced materials/structural detail, multimodal input and multi-turn interaction. Generated geometry is not certified printable or mechanically valid. [Source 1](https://github.com/FreedomIntelligence/BlenderLLM/blob/main/README.md) [Source 2](https://huggingface.co/FreedomIntelligence/BlenderLLM)

### Get the tool

- [Repository](https://github.com/FreedomIntelligence/BlenderLLM)
- [Documentation](https://github.com/FreedomIntelligence/BlenderLLM/blob/main/README.md)

## Diffusion as Shader

Video, animation & film · VFX, compositing & relighting · Motion capture & character animation · 3D, reconstruction & assets

First full guide in this library, establishing a documentation baseline; not a claim of a launch or significant update today.

### Quality assessment: Quality unverified

Software licensing and a concrete creative AI use are supported. The remaining checks do not establish a recommendation.

Scope: Exploring controlled camera moves and motion-conditioned visual effects from images, video or a Blender scene.

Evidence checked: 2026-10-22. No local execution implied.

- **Open-source software license · verified:** The complete root software license was read and archived. The grant covers this project code; unresolved model, service and asset terms are disclosed separately. [Source](https://github.com/IGL-HKUST/DiffusionAsShader/blob/main/LICENSE)
- **Creative results · documented:** The official project and README show four task families; some demonstrated replacements use FLUX.1 Kontext assistance. [Source](https://github.com/IGL-HKUST/DiffusionAsShader/blob/main/README.md) [Source](https://igl-hkust.github.io/das/) [Source](https://huggingface.co/EXCAI/Diffusion-As-Shader)
- **Reproducible setup · documented:** Create the documented Python 3.10 environment, install PyTorch 2.5.1/CUDA 11.8 and repository requirements, initialize MoGe/VGGT submodules, and download the named tracking and diffusion checkpoints. Independent reproduction has not been established in this review. [Source](https://github.com/IGL-HKUST/DiffusionAsShader/blob/main/README.md) [Source](https://igl-hkust.github.io/das/) [Source](https://huggingface.co/EXCAI/Diffusion-As-Shader)
- **Maintenance and support · unknown:** A release or active repository alone does not establish sustained support. Workflow-specific support and unresolved blockers need a deeper review.
- **Independent use · unknown:** Independent first-hand use or a working third-party integration was not established for this selected workflow.
- **Models, services and costs · documented:** Apache-2.0 project code does not grant all tracker, diffusion, FLUX or dataset rights. Model/dependency terms remain separately scoped and unresolved in this guide. Local compute plus any chosen external model or service; provider access and charges are separate. [Source](https://github.com/IGL-HKUST/DiffusionAsShader/blob/main/README.md) [Source](https://igl-hkust.github.io/das/) [Source](https://huggingface.co/EXCAI/Diffusion-As-Shader)

Documentation review only; AI Media Scout did not install or run this software. Camera controls operate over the documented 49-frame sequence; tracker scale can require adjustment. Results and benchmark quality are not verified here.

### How it uses AI

Controls a video diffusion model with 3D tracking for motion transfer, camera movement, object manipulation and mesh-driven animation. [Source](https://github.com/IGL-HKUST/DiffusionAsShader/blob/main/README.md) [Source](https://igl-hkust.github.io/das/) [Source](https://huggingface.co/EXCAI/Diffusion-As-Shader)

### Introduction

Controls a video diffusion model with 3D tracking for motion transfer, camera movement, object manipulation and mesh-driven animation. [Source 1](https://github.com/IGL-HKUST/DiffusionAsShader/blob/main/README.md) [Source 2](https://igl-hkust.github.io/das/) [Source 3](https://huggingface.co/EXCAI/Diffusion-As-Shader)

### What it is good for

Exploring controlled camera moves and motion-conditioned visual effects from images, video or a Blender scene. [Source 1](https://github.com/IGL-HKUST/DiffusionAsShader/blob/main/README.md) [Source 2](https://igl-hkust.github.io/das/) [Source 3](https://huggingface.co/EXCAI/Diffusion-As-Shader)

### Demo & examples

The official project and README show four task families; some demonstrated replacements use FLUX.1 Kontext assistance. [Source 1](https://github.com/IGL-HKUST/DiffusionAsShader/blob/main/README.md) [Source 2](https://igl-hkust.github.io/das/) [Source 3](https://huggingface.co/EXCAI/Diffusion-As-Shader)

### Install

Create the documented Python 3.10 environment, install PyTorch 2.5.1/CUDA 11.8 and repository requirements, initialize MoGe/VGGT submodules, and download the named tracking and diffusion checkpoints. [Source 1](https://github.com/IGL-HKUST/DiffusionAsShader/blob/main/README.md) [Source 2](https://igl-hkust.github.io/das/) [Source 3](https://huggingface.co/EXCAI/Diffusion-As-Shader)

1. Obtain the official source or release linked below.
2. Create the documented Python 3.10 environment, install PyTorch 2.5.1/CUDA 11.8 and repository requirements, initialize MoGe/VGGT submodules, and download the named tracking and diffusion checkpoints.

```sh
pip install -r requirements.txt
```


```sh
python webui.py --gpu 0
```

### First project

Start with a short, representative project and inspect the result before a larger batch. [Source 1](https://github.com/IGL-HKUST/DiffusionAsShader/blob/main/README.md) [Source 2](https://igl-hkust.github.io/das/) [Source 3](https://huggingface.co/EXCAI/Diffusion-As-Shader)

1. Start with one provided example and the matching checkpoints.
2. Choose camera control or motion transfer and supply a short input.
3. Inspect temporal consistency and geometry; Blender mesh workflows require generated tracking video.
### Hardware & software

Requirements below are documented for this workflow. Unspecified limits are not inferred. [Source 1](https://github.com/IGL-HKUST/DiffusionAsShader/blob/main/README.md) [Source 2](https://igl-hkust.github.io/das/) [Source 3](https://huggingface.co/EXCAI/Diffusion-As-Shader)

- **Hardware:** The authors state 32 GB GPU memory is sufficient for their inference code and tested an H800. This is not a universal minimum; RAM and storage are not documented.
- **Software:** Python 3.10, PyTorch 2.5.1, CUDA 11.8, MoGe/VGGT and tracking checkpoints. Blender >4.0 for the documented mesh-to-video route.
- **Platforms:** Maintainer-tested inference environment is Ubuntu 20.04 with an NVIDIA H800; Windows/macOS/CPU support is not documented.

### License, model weights & costs

The full software license was reviewed. Model weights, assets and services remain separate. [Source 1](https://github.com/IGL-HKUST/DiffusionAsShader/blob/main/LICENSE) [Source 2](https://github.com/IGL-HKUST/DiffusionAsShader/blob/main/README.md) [Source 3](https://igl-hkust.github.io/das/) [Source 4](https://huggingface.co/EXCAI/Diffusion-As-Shader)

- **Code:** Apache-2.0
- **Weights:** Apache-2.0 project code does not grant all tracker, diffusion, FLUX or dataset rights. Model/dependency terms remain separately scoped and unresolved in this guide.
- **Commercial:** Software use follows Apache-2.0. Apache-2.0 project code does not grant all tracker, diffusion, FLUX or dataset rights. Model/dependency terms remain separately scoped and unresolved in this guide.
- **Cost:** Local compute plus any chosen external model or service; provider access and charges are separate.

### Why it merits attention

Included for the documented creative workflow. A complete guide and popularity do not establish output reliability. [Source 1](https://github.com/IGL-HKUST/DiffusionAsShader/blob/main/README.md) [Source 2](https://igl-hkust.github.io/das/) [Source 3](https://huggingface.co/EXCAI/Diffusion-As-Shader)

### Limitations

Camera controls operate over the documented 49-frame sequence; tracker scale can require adjustment. Results and benchmark quality are not verified here. [Source 1](https://github.com/IGL-HKUST/DiffusionAsShader/blob/main/README.md) [Source 2](https://igl-hkust.github.io/das/) [Source 3](https://huggingface.co/EXCAI/Diffusion-As-Shader)

### Get the tool

- [Repository](https://github.com/IGL-HKUST/DiffusionAsShader)
- [Documentation](https://github.com/IGL-HKUST/DiffusionAsShader/blob/main/README.md)

## Sign-language motion capture for Blender

AI signing avatars and expressive gesture media · Motion capture & character animation · Avatars, digital humans & lip sync · Accessible media & assistive creation

First full guide in this library, establishing a documentation baseline; not a claim of a launch or significant update today.

### Quality assessment: Quality unverified

Software licensing and a concrete creative AI use are supported. The remaining checks do not establish a recommendation.

Scope: Studying signing motion capture and avatar animation from recorded gesture examples.

Evidence checked: 2026-10-22. No local execution implied.

- **Open-source software license · verified:** The complete root software license was read and archived. The grant covers this project code; unresolved model, service and asset terms are disclosed separately. [Source](https://github.com/lanthaon/sl-animation-blender/blob/main/LICENSE)
- **Creative results · documented:** Prepared .blend files, BVH motion and an FBX export are included as examples. [Source](https://github.com/lanthaon/sl-animation-blender/blob/main/README.md)
- **Reproducible setup · documented:** Use the versions named in the project and open the prepared Blender files; the attached scripts contain the workflow instructions for landmark capture and bone-rotation transfer. Independent reproduction has not been established in this review. [Source](https://github.com/lanthaon/sl-animation-blender/blob/main/README.md)
- **Maintenance and support · unknown:** A release or active repository alone does not establish sustained support. Workflow-specific support and unresolved blockers need a deeper review.
- **Independent use · unknown:** Independent first-hand use or a working third-party integration was not established for this selected workflow.
- **Models, services and costs · documented:** MIT project code; MediaPipe, Daz Studio/character assets, bridge and recorded signing clips retain separate terms. Local compute plus any chosen external model or service; provider access and charges are separate. [Source](https://github.com/lanthaon/sl-animation-blender/blob/main/README.md)

Documentation review only; AI Media Scout did not install or run this software. Motion capture is not linguistic validation. The project does not establish that generated signing is intelligible or suitable for accessibility delivery without qualified review.

### How it uses AI

Uses MediaPipe Holistic to extract body/hand landmarks from RGB video and transfer motion to a prepared Daz character in Blender. [Source](https://github.com/lanthaon/sl-animation-blender/blob/main/README.md)

### Introduction

Uses MediaPipe Holistic to extract body/hand landmarks from RGB video and transfer motion to a prepared Daz character in Blender. [Source 1](https://github.com/lanthaon/sl-animation-blender/blob/main/README.md)

### What it is good for

Studying signing motion capture and avatar animation from recorded gesture examples. [Source 1](https://github.com/lanthaon/sl-animation-blender/blob/main/README.md)

### Demo & examples

Prepared .blend files, BVH motion and an FBX export are included as examples. [Source 1](https://github.com/lanthaon/sl-animation-blender/blob/main/README.md)

### Install

Use the versions named in the project and open the prepared Blender files; the attached scripts contain the workflow instructions for landmark capture and bone-rotation transfer. [Source 1](https://github.com/lanthaon/sl-animation-blender/blob/main/README.md)

1. Obtain the official source or release linked below.
2. Use the versions named in the project and open the prepared Blender files; the attached scripts contain the workflow instructions for landmark capture and bone-rotation transfer.
### First project

Start with a short, representative project and inspect the result before a larger batch. [Source 1](https://github.com/lanthaon/sl-animation-blender/blob/main/README.md)

1. Start with make_bvh_files.blend and a short consented source video.
2. Follow the attached landmark script to produce capture data.
3. Open animate_avatar.blend, apply the recorded motion and inspect hands, face and body alignment.
### Hardware & software

Requirements below are documented for this workflow. Unspecified limits are not inferred. [Source 1](https://github.com/lanthaon/sl-animation-blender/blob/main/README.md)

- **Hardware:** Minimum system RAM, VRAM and total disk space are not documented in the reviewed instructions.
- **Software:** Blender 2.91.2, Python 3.7/3.8, MediaPipe 0.8.3.1 and opencv-python 4.5.1.48 were used by the author.
- **Platforms:** No complete operating-system compatibility matrix is documented. Do not infer current Blender compatibility from the older tested versions.

### License, model weights & costs

The full software license was reviewed. Model weights, assets and services remain separate. [Source 1](https://github.com/lanthaon/sl-animation-blender/blob/main/LICENSE) [Source 2](https://github.com/lanthaon/sl-animation-blender/blob/main/README.md)

- **Code:** MIT
- **Weights:** MIT project code; MediaPipe, Daz Studio/character assets, bridge and recorded signing clips retain separate terms.
- **Commercial:** Software use follows MIT. MIT project code; MediaPipe, Daz Studio/character assets, bridge and recorded signing clips retain separate terms.
- **Cost:** Local compute plus any chosen external model or service; provider access and charges are separate.

### Why it merits attention

Included for the documented creative workflow. A complete guide and popularity do not establish output reliability. [Source 1](https://github.com/lanthaon/sl-animation-blender/blob/main/README.md)

### Limitations

Motion capture is not linguistic validation. The project does not establish that generated signing is intelligible or suitable for accessibility delivery without qualified review. [Source 1](https://github.com/lanthaon/sl-animation-blender/blob/main/README.md)

### Get the tool

- [Repository](https://github.com/lanthaon/sl-animation-blender)
- [Documentation](https://github.com/lanthaon/sl-animation-blender/blob/main/README.md)

## YoVoice

Audio, music & voice · Accessible media & assistive creation · AI music notation and score recovery

First full guide, completing an earlier screened library entry with installation, use and documented requirements. This is a review-depth improvement, not a verified new software release.

### Quality assessment: Quality unverified

Software licensing and a concrete creative AI use are supported. The remaining checks do not establish a recommendation.

Scope: Drafting narration, character voices, songs and editable melody scores, starting with a lightweight built-in voice.

Evidence checked: 2026-10-22. No local execution implied.

- **Open-source software license · verified:** The complete root software license was read and archived. The grant covers this project code; unresolved model, service and asset terms are disclosed separately. [Source](https://github.com/leemysw/yovoice/blob/main/LICENSE)
- **Creative results · documented:** The README shows the project interface and model workflows; the model guide describes voice and song generation. These are maintainer examples, not independently tested listening results. [Source](https://github.com/leemysw/yovoice/blob/main/README.md) [Source](https://github.com/leemysw/yovoice/blob/main/docs/models.md) [Source](https://github.com/leemysw/yovoice/blob/main/THIRD_PARTY_NOTICES.md)
- **Reproducible setup · documented:** Choose the official platform release, open Settings, download an engine and model, then create a Speech, Story, Music or Score project. CLI packages are also supplied. Independent reproduction has not been established in this review. [Source](https://github.com/leemysw/yovoice/blob/main/README.md) [Source](https://github.com/leemysw/yovoice/blob/main/docs/models.md) [Source](https://github.com/leemysw/yovoice/blob/main/THIRD_PARTY_NOTICES.md)
- **Maintenance and support · unknown:** A release or active repository alone does not establish sustained support. Workflow-specific support and unresolved blockers need a deeper review.
- **Independent use · unknown:** Independent first-hand use or a working third-party integration was not established for this selected workflow.
- **Models, services and costs · documented:** The root app is Apache-2.0. Kokoro and Qwen3-TTS are identified as Apache-2.0; ACE-Step as MIT. OmniVoice, YuE2 and Breeze TTS 2 have noncommercial weight terms; IndexTTS has separate model terms. The bundled ocho helper is binary-only despite its stated Apache license; a complete source build of every bundled helper is not established. Local compute plus any chosen external model or service; provider access and charges are separate. [Source](https://github.com/leemysw/yovoice/blob/main/README.md) [Source](https://github.com/leemysw/yovoice/blob/main/docs/models.md) [Source](https://github.com/leemysw/yovoice/blob/main/THIRD_PARTY_NOTICES.md)

Documentation review only; AI Media Scout did not install or run this software. Long text can drift or repeat, especially with model-specific chunking and precision choices. Model download size is not peak memory. Optional AI assistants use separate providers. No single app license covers every model or voice recording.

### How it uses AI

A desktop workspace runs speech, voice-design and music models locally through audio.cpp, with editable narration projects and optional AI score assistance. [Source](https://github.com/leemysw/yovoice/blob/main/README.md) [Source](https://github.com/leemysw/yovoice/blob/main/docs/models.md) [Source](https://github.com/leemysw/yovoice/blob/main/THIRD_PARTY_NOTICES.md)

### Introduction

A desktop workspace runs speech, voice-design and music models locally through audio.cpp, with editable narration projects and optional AI score assistance. [Source 1](https://github.com/leemysw/yovoice/blob/main/README.md) [Source 2](https://github.com/leemysw/yovoice/blob/main/docs/models.md) [Source 3](https://github.com/leemysw/yovoice/blob/main/THIRD_PARTY_NOTICES.md)

### What it is good for

Drafting narration, character voices, songs and editable melody scores, starting with a lightweight built-in voice. [Source 1](https://github.com/leemysw/yovoice/blob/main/README.md) [Source 2](https://github.com/leemysw/yovoice/blob/main/docs/models.md) [Source 3](https://github.com/leemysw/yovoice/blob/main/THIRD_PARTY_NOTICES.md)

### Demo & examples

The README shows the project interface and model workflows; the model guide describes voice and song generation. These are maintainer examples, not independently tested listening results. [Source 1](https://github.com/leemysw/yovoice/blob/main/README.md) [Source 2](https://github.com/leemysw/yovoice/blob/main/docs/models.md) [Source 3](https://github.com/leemysw/yovoice/blob/main/THIRD_PARTY_NOTICES.md)

### Install

Choose the official platform release, open Settings, download an engine and model, then create a Speech, Story, Music or Score project. CLI packages are also supplied. [Source 1](https://github.com/leemysw/yovoice/blob/main/README.md) [Source 2](https://github.com/leemysw/yovoice/blob/main/docs/models.md) [Source 3](https://github.com/leemysw/yovoice/blob/main/THIRD_PARTY_NOTICES.md)

1. Obtain the official source or release linked below.
2. Choose the official platform release, open Settings, download an engine and model, then create a Speech, Story, Music or Score project. CLI packages are also supplied.

```sh
yovoice models download kokoro-82m-q8
```


```sh
yovoice generate --model kokoro-82m-q8 --speaker af_heart --text "Hello, welcome." --output hello.wav
```

### First project

Start with a short, representative project and inspect the result before a larger batch. [Source 1](https://github.com/leemysw/yovoice/blob/main/README.md) [Source 2](https://github.com/leemysw/yovoice/blob/main/docs/models.md) [Source 3](https://github.com/leemysw/yovoice/blob/main/THIRD_PARTY_NOTICES.md)

1. Download Kokoro in Settings for a small first narration task.
2. Enter a short script, choose a built-in speaker and generate.
3. Listen for pronunciation and chunk boundaries; export the accepted take.
### Hardware & software

Requirements below are documented for this workflow. Unspecified limits are not inferred. [Source 1](https://github.com/leemysw/yovoice/blob/main/README.md) [Source 2](https://github.com/leemysw/yovoice/blob/main/docs/models.md) [Source 3](https://github.com/leemysw/yovoice/blob/main/THIRD_PARTY_NOTICES.md)

- **Hardware:** Maintainer recommendations: Kokoro CPU with 4 GB+ RAM; voice cloning 4–6 GB VRAM or 8 GB+ Apple Silicon memory; music 12 GB+ VRAM or 16 GB+ Apple Silicon. Kokoro Q8 is about 190 MB; larger music models span roughly 6–15 GB. These are workflow recommendations, not independently measured minima.
- **Software:** The desktop distribution uses a C++ audio.cpp engine; users do not need a separate Python installation. Windows uses WebView2; Linux packages need WebKitGTK 4.1. Music and newer models require engine v0.9.1.
- **Platforms:** Documented releases: macOS 14+ on Apple Silicon, Windows 10/11 x64, Linux x64. CPU, Metal and selected CUDA/Vulkan engine routes differ by platform.

### License, model weights & costs

The full software license was reviewed. Model weights, assets and services remain separate. [Source 1](https://github.com/leemysw/yovoice/blob/main/LICENSE) [Source 2](https://github.com/leemysw/yovoice/blob/main/README.md) [Source 3](https://github.com/leemysw/yovoice/blob/main/docs/models.md) [Source 4](https://github.com/leemysw/yovoice/blob/main/THIRD_PARTY_NOTICES.md)

- **Code:** Apache-2.0
- **Weights:** The root app is Apache-2.0. Kokoro and Qwen3-TTS are identified as Apache-2.0; ACE-Step as MIT. OmniVoice, YuE2 and Breeze TTS 2 have noncommercial weight terms; IndexTTS has separate model terms. The bundled ocho helper is binary-only despite its stated Apache license; a complete source build of every bundled helper is not established.
- **Commercial:** Software use follows Apache-2.0. The root app is Apache-2.0. Kokoro and Qwen3-TTS are identified as Apache-2.0; ACE-Step as MIT. OmniVoice, YuE2 and Breeze TTS 2 have noncommercial weight terms; IndexTTS has separate model terms. The bundled ocho helper is binary-only despite its stated Apache license; a complete source build of every bundled helper is not established.
- **Cost:** Local compute plus any chosen external model or service; provider access and charges are separate.

### Why it merits attention

Included for the documented creative workflow. A complete guide and popularity do not establish output reliability. [Source 1](https://github.com/leemysw/yovoice/blob/main/README.md) [Source 2](https://github.com/leemysw/yovoice/blob/main/docs/models.md) [Source 3](https://github.com/leemysw/yovoice/blob/main/THIRD_PARTY_NOTICES.md)

### Limitations

Long text can drift or repeat, especially with model-specific chunking and precision choices. Model download size is not peak memory. Optional AI assistants use separate providers. No single app license covers every model or voice recording. [Source 1](https://github.com/leemysw/yovoice/blob/main/README.md) [Source 2](https://github.com/leemysw/yovoice/blob/main/docs/models.md) [Source 3](https://github.com/leemysw/yovoice/blob/main/THIRD_PARTY_NOTICES.md)

### Get the tool

- [Repository](https://github.com/leemysw/yovoice)
- [Documentation](https://github.com/leemysw/yovoice/blob/main/README.md)

## Acoustic Agent

Audio, music & voice · Spatial audio & volumetric media · Neural acoustics and responsive sound spaces · AI architectural visualization and spatial design

First full guide, completing an earlier screened library entry with installation, use and documented requirements. This is a review-depth improvement, not a verified new software release.

### Quality assessment: Experimental

Software licensing and a concrete creative AI use are supported. The remaining checks do not establish a recommendation.

Scope: Exploring room impulse responses, moving sound sources and binaural auralization for spatial sound design and installation prototypes.

Evidence checked: 2026-10-22. No local execution implied.

Why Experimental: The current README explicitly describes the software as research alpha; the assessed room-simulation workflow remains under development. https://github.com/aizhiqi-work/acoustic-agent/blob/main/README.md https://github.com/aizhiqi-work/acoustic-agent/blob/main/docs/INSTALLATION.md https://github.com/aizhiqi-work/acoustic-agent/blob/main/THIRD_PARTY_NOTICES.md

- **Open-source software license · verified:** The complete root software license was read and archived. The grant covers this project code; unresolved model, service and asset terms are disclosed separately. [Source](https://github.com/aizhiqi-work/acoustic-agent/blob/main/LICENSE)
- **Creative results · documented:** The project publishes room examples, acoustic benchmarks and a local web auralization interface. The physical renderer itself is not a generative AI model. [Source](https://github.com/aizhiqi-work/acoustic-agent/blob/main/README.md) [Source](https://github.com/aizhiqi-work/acoustic-agent/blob/main/docs/INSTALLATION.md) [Source](https://github.com/aizhiqi-work/acoustic-agent/blob/main/THIRD_PARTY_NOTICES.md)
- **Reproducible setup · documented:** Use Python 3.10+, obtain the repository and its Git LFS resources, install the development extras, then follow the installation guide to verify resources and start the local web interface. Independent reproduction has not been established in this review. [Source](https://github.com/aizhiqi-work/acoustic-agent/blob/main/README.md) [Source](https://github.com/aizhiqi-work/acoustic-agent/blob/main/docs/INSTALLATION.md) [Source](https://github.com/aizhiqi-work/acoustic-agent/blob/main/THIRD_PARTY_NOTICES.md)
- **Maintenance and support · unknown:** A release or active repository alone does not establish sustained support. Workflow-specific support and unresolved blockers need a deeper review.
- **Independent use · unknown:** Independent first-hand use or a working third-party integration was not established for this selected workflow.
- **Models, services and costs · documented:** Apache-2.0 covers project code. ResPlan-derived floorplans are CC BY-NC-SA 4.0. The material database is NOASSERTION with mixed terms, including subsets requiring redistribution permission. Demo audio provenance is unresolved. HRTF files have their own terms. Local compute plus any chosen external model or service; provider access and charges are separate. [Source](https://github.com/aizhiqi-work/acoustic-agent/blob/main/README.md) [Source](https://github.com/aizhiqi-work/acoustic-agent/blob/main/docs/INSTALLATION.md) [Source](https://github.com/aizhiqi-work/acoustic-agent/blob/main/THIRD_PARTY_NOTICES.md)

Documentation review only; AI Media Scout did not install or run this software. Research alpha. Dataset-driven workflows are not uniformly open or commercially cleared. VLM mappings do not generate physical absorption coefficients. CPU/GPU accuracy and speed claims are maintainer benchmarks.

### How it uses AI

An AI-assisted room-acoustics workflow uses VLM-derived material mappings and optional language-model scene descriptions around a physical acoustic simulator. [Source](https://github.com/aizhiqi-work/acoustic-agent/blob/main/README.md) [Source](https://github.com/aizhiqi-work/acoustic-agent/blob/main/docs/INSTALLATION.md) [Source](https://github.com/aizhiqi-work/acoustic-agent/blob/main/THIRD_PARTY_NOTICES.md)

### Introduction

An AI-assisted room-acoustics workflow uses VLM-derived material mappings and optional language-model scene descriptions around a physical acoustic simulator. [Source 1](https://github.com/aizhiqi-work/acoustic-agent/blob/main/README.md) [Source 2](https://github.com/aizhiqi-work/acoustic-agent/blob/main/docs/INSTALLATION.md) [Source 3](https://github.com/aizhiqi-work/acoustic-agent/blob/main/THIRD_PARTY_NOTICES.md)

### What it is good for

Exploring room impulse responses, moving sound sources and binaural auralization for spatial sound design and installation prototypes. [Source 1](https://github.com/aizhiqi-work/acoustic-agent/blob/main/README.md) [Source 2](https://github.com/aizhiqi-work/acoustic-agent/blob/main/docs/INSTALLATION.md) [Source 3](https://github.com/aizhiqi-work/acoustic-agent/blob/main/THIRD_PARTY_NOTICES.md)

### Demo & examples

The project publishes room examples, acoustic benchmarks and a local web auralization interface. The physical renderer itself is not a generative AI model. [Source 1](https://github.com/aizhiqi-work/acoustic-agent/blob/main/README.md) [Source 2](https://github.com/aizhiqi-work/acoustic-agent/blob/main/docs/INSTALLATION.md) [Source 3](https://github.com/aizhiqi-work/acoustic-agent/blob/main/THIRD_PARTY_NOTICES.md)

### Install

Use Python 3.10+, obtain the repository and its Git LFS resources, install the development extras, then follow the installation guide to verify resources and start the local web interface. [Source 1](https://github.com/aizhiqi-work/acoustic-agent/blob/main/README.md) [Source 2](https://github.com/aizhiqi-work/acoustic-agent/blob/main/docs/INSTALLATION.md) [Source 3](https://github.com/aizhiqi-work/acoustic-agent/blob/main/THIRD_PARTY_NOTICES.md)

1. Obtain the official source or release linked below.
2. Use Python 3.10+, obtain the repository and its Git LFS resources, install the development extras, then follow the installation guide to verify resources and start the local web interface.

```sh
pip install -e ".[dev]"
```

### First project

Start with a short, representative project and inspect the result before a larger batch. [Source 1](https://github.com/aizhiqi-work/acoustic-agent/blob/main/README.md) [Source 2](https://github.com/aizhiqi-work/acoustic-agent/blob/main/docs/INSTALLATION.md) [Source 3](https://github.com/aizhiqi-work/acoustic-agent/blob/main/THIRD_PARTY_NOTICES.md)

1. Verify the downloaded resources using the documented resource check.
2. Start with a parametric room, source and listener placement.
3. Render an impulse response or binaural example, then compare materials and motion using audio you have rights to use.
### Hardware & software

Requirements below are documented for this workflow. Unspecified limits are not inferred. [Source 1](https://github.com/aizhiqi-work/acoustic-agent/blob/main/README.md) [Source 2](https://github.com/aizhiqi-work/acoustic-agent/blob/main/docs/INSTALLATION.md) [Source 3](https://github.com/aizhiqi-work/acoustic-agent/blob/main/THIRD_PARTY_NOTICES.md)

- **Hardware:** CPU mode is documented; CUDA acceleration is optional. Minimum RAM, VRAM and disk are not specified. M4, RTX 4090 and A6000 benchmarks are examples, not minimum requirements.
- **Software:** Python 3.10+, NumPy/Numba and project dependencies; Git LFS for bundled resources. Optional NVIDIA CUDA path differs numerically from the CPU path.
- **Platforms:** The reviewed guide documents CPU execution and optional NVIDIA CUDA. Example benchmarks include Apple M4 CPU and NVIDIA GPUs; a comprehensive OS support matrix is not documented.

### License, model weights & costs

The full software license was reviewed. Model weights, assets and services remain separate. [Source 1](https://github.com/aizhiqi-work/acoustic-agent/blob/main/LICENSE) [Source 2](https://github.com/aizhiqi-work/acoustic-agent/blob/main/README.md) [Source 3](https://github.com/aizhiqi-work/acoustic-agent/blob/main/docs/INSTALLATION.md) [Source 4](https://github.com/aizhiqi-work/acoustic-agent/blob/main/THIRD_PARTY_NOTICES.md)

- **Code:** Apache-2.0
- **Weights:** Apache-2.0 covers project code. ResPlan-derived floorplans are CC BY-NC-SA 4.0. The material database is NOASSERTION with mixed terms, including subsets requiring redistribution permission. Demo audio provenance is unresolved. HRTF files have their own terms.
- **Commercial:** Software use follows Apache-2.0. Apache-2.0 covers project code. ResPlan-derived floorplans are CC BY-NC-SA 4.0. The material database is NOASSERTION with mixed terms, including subsets requiring redistribution permission. Demo audio provenance is unresolved. HRTF files have their own terms.
- **Cost:** Local compute plus any chosen external model or service; provider access and charges are separate.

### Why it merits attention

Included for the documented creative workflow. A complete guide and popularity do not establish output reliability. [Source 1](https://github.com/aizhiqi-work/acoustic-agent/blob/main/README.md) [Source 2](https://github.com/aizhiqi-work/acoustic-agent/blob/main/docs/INSTALLATION.md) [Source 3](https://github.com/aizhiqi-work/acoustic-agent/blob/main/THIRD_PARTY_NOTICES.md)

### Limitations

Research alpha. Dataset-driven workflows are not uniformly open or commercially cleared. VLM mappings do not generate physical absorption coefficients. CPU/GPU accuracy and speed claims are maintainer benchmarks. [Source 1](https://github.com/aizhiqi-work/acoustic-agent/blob/main/README.md) [Source 2](https://github.com/aizhiqi-work/acoustic-agent/blob/main/docs/INSTALLATION.md) [Source 3](https://github.com/aizhiqi-work/acoustic-agent/blob/main/THIRD_PARTY_NOTICES.md)

### Get the tool

- [Repository](https://github.com/aizhiqi-work/acoustic-agent)
- [Documentation](https://github.com/aizhiqi-work/acoustic-agent/blob/main/README.md)

## Google AI Edge Gallery

Mobile, edge & on-device creation · Video, animation & film · Images & design · Audio, music & voice · Accessible media & assistive creation

First full guide, completing an earlier screened library entry with installation, use and documented requirements. This is a review-depth improvement, not a verified new software release.

### Quality assessment: Experimental

Software licensing and a concrete creative AI use are supported. The remaining checks do not establish a recommendation.

Scope: Finding and trimming a moment in a video, transcribing a recording, and exploring local multimodal models on a phone.

Evidence checked: 2026-10-22. No local execution implied.

Why Experimental: The current application README explicitly labels the release experimental Beta, including the on-device gallery workflow. https://github.com/google-ai-edge/gallery/blob/main/README.md

- **Open-source software license · verified:** The complete root software license was read and archived. The grant covers this project code; unresolved model, service and asset terms are disclosed separately. [Source](https://github.com/google-ai-edge/gallery/blob/main/LICENSE)
- **Creative results · documented:** The README documents Video Moment Finder, Ask Image and Audio Scribe with interface examples and official application downloads. [Source](https://github.com/google-ai-edge/gallery/blob/main/README.md)
- **Reproducible setup · documented:** Install the official Android or iOS app, or use the documented Android release package; choose a supported model and complete its initial download and any publisher acceptance. Independent reproduction has not been established in this review. [Source](https://github.com/google-ai-edge/gallery/blob/main/README.md)
- **Maintenance and support · unknown:** A release or active repository alone does not establish sustained support. Workflow-specific support and unresolved blockers need a deeper review.
- **Independent use · unknown:** Independent first-hand use or a working third-party integration was not established for this selected workflow.
- **Models, services and costs · documented:** Apache-2.0 application source; Gemma and other downloaded weights retain publisher-specific terms and any gated access conditions. Local compute plus any chosen external model or service; provider access and charges are separate. [Source](https://github.com/google-ai-edge/gallery/blob/main/README.md)

Documentation review only; AI Media Scout did not install or run this software. The app is explicitly an experimental beta. On-device speed, memory limits and model capability depend on the selected phone and model; a generic minimum RAM/VRAM/storage is not published.

### How it uses AI

A mobile gallery runs on-device generative models for image questions, audio transcription and semantic video moments. [Source](https://github.com/google-ai-edge/gallery/blob/main/README.md)

### Introduction

A mobile gallery runs on-device generative models for image questions, audio transcription and semantic video moments. [Source 1](https://github.com/google-ai-edge/gallery/blob/main/README.md)

### What it is good for

Finding and trimming a moment in a video, transcribing a recording, and exploring local multimodal models on a phone. [Source 1](https://github.com/google-ai-edge/gallery/blob/main/README.md)

### Demo & examples

The README documents Video Moment Finder, Ask Image and Audio Scribe with interface examples and official application downloads. [Source 1](https://github.com/google-ai-edge/gallery/blob/main/README.md)

### Install

Install the official Android or iOS app, or use the documented Android release package; choose a supported model and complete its initial download and any publisher acceptance. [Source 1](https://github.com/google-ai-edge/gallery/blob/main/README.md)

1. Obtain the official source or release linked below.
2. Install the official Android or iOS app, or use the documented Android release package; choose a supported model and complete its initial download and any publisher acceptance.
### First project

Start with a short, representative project and inspect the result before a larger batch. [Source 1](https://github.com/google-ai-edge/gallery/blob/main/README.md)

1. Choose a model and finish its download.
2. Open Video Moment Finder with a short clip and ask for a visible event.
3. Inspect the returned segment before trimming and exporting it.
### Hardware & software

Requirements below are documented for this workflow. Unspecified limits are not inferred. [Source 1](https://github.com/google-ai-edge/gallery/blob/main/README.md)

- **Hardware:** Minimum system RAM, VRAM and total disk space are not documented in the reviewed instructions.
- **Software:** Android 12+ or iOS 17+ for the documented mobile routes. Model downloads and their runtime compatibility vary.
- **Platforms:** Android and iOS are documented. A macOS download is linked, but a minimum macOS version was not established in the reviewed README. Windows/Linux desktop support is not established.

### License, model weights & costs

The full software license was reviewed. Model weights, assets and services remain separate. [Source 1](https://github.com/google-ai-edge/gallery/blob/main/LICENSE) [Source 2](https://github.com/google-ai-edge/gallery/blob/main/README.md)

- **Code:** Apache-2.0
- **Weights:** Apache-2.0 application source; Gemma and other downloaded weights retain publisher-specific terms and any gated access conditions.
- **Commercial:** Software use follows Apache-2.0. Apache-2.0 application source; Gemma and other downloaded weights retain publisher-specific terms and any gated access conditions.
- **Cost:** Local compute plus any chosen external model or service; provider access and charges are separate.

### Why it merits attention

Included for the documented creative workflow. A complete guide and popularity do not establish output reliability. [Source 1](https://github.com/google-ai-edge/gallery/blob/main/README.md)

### Limitations

The app is explicitly an experimental beta. On-device speed, memory limits and model capability depend on the selected phone and model; a generic minimum RAM/VRAM/storage is not published. [Source 1](https://github.com/google-ai-edge/gallery/blob/main/README.md)

### Get the tool

- [Repository](https://github.com/google-ai-edge/gallery)
- [Documentation](https://github.com/google-ai-edge/gallery/blob/main/README.md)

## FantasyTalking

Video, animation & film · Avatars, digital humans & lip sync · Audio, music & voice · Motion capture & character animation

First full guide in this library, establishing a documentation baseline; not a claim of a launch or significant update today.

### Quality assessment: Quality unverified

Software licensing and a concrete creative AI use are supported. The remaining checks do not establish a recommendation.

Scope: Short character dialogue and portrait animation from a still image plus a voice recording.

Evidence checked: 2026-10-22. No local execution implied.

- **Open-source software license · verified:** The complete root software license was read and archived. The grant covers this project code; unresolved model, service and asset terms are disclosed separately. [Source](https://github.com/Fantasy-AMAP/fantasy-talking/blob/main/LICENSE)
- **Creative results · documented:** The official project page and linked demo show generated portrait videos. These are published examples; no local render was tested. [Source](https://github.com/Fantasy-AMAP/fantasy-talking/blob/main/README.md) [Source](https://fantasy-amap.github.io/fantasy-talking/)
- **Reproducible setup · documented:** Clone the project, install its requirements with PyTorch 2+, and download the documented Wan2.1 I2V 14B 720P, wav2vec2 and FantasyTalking checkpoints. Use infer.py or the optional Gradio app. Independent reproduction has not been established in this review. [Source](https://github.com/Fantasy-AMAP/fantasy-talking/blob/main/README.md) [Source](https://fantasy-amap.github.io/fantasy-talking/)
- **Maintenance and support · unknown:** A release or active repository alone does not establish sustained support. Workflow-specific support and unresolved blockers need a deeper review.
- **Independent use · unknown:** Independent first-hand use or a working third-party integration was not established for this selected workflow.
- **Models, services and costs · documented:** Apache-2.0 project code. Wan, wav2vec2 and FantasyTalking checkpoints must be obtained separately; the complete terms for every weight were not established in this review. Local compute plus any chosen external model or service; provider access and charges are separate. [Source](https://github.com/Fantasy-AMAP/fantasy-talking/blob/main/README.md) [Source](https://fantasy-amap.github.io/fantasy-talking/)

Documentation review only; AI Media Scout did not install or run this software. The A100 measurements are configuration-specific: about 40 GB, 20 GB or 5 GB VRAM for different persistence settings at 512×512 and 81 frames, with substantial speed differences. They do not establish a universal 5 GB minimum.

### How it uses AI

An audio-conditioned video model animates a reference portrait into a speaking character using a Wan image-to-video backbone. [Source](https://github.com/Fantasy-AMAP/fantasy-talking/blob/main/README.md) [Source](https://fantasy-amap.github.io/fantasy-talking/)

### Introduction

An audio-conditioned video model animates a reference portrait into a speaking character using a Wan image-to-video backbone. [Source 1](https://github.com/Fantasy-AMAP/fantasy-talking/blob/main/README.md) [Source 2](https://fantasy-amap.github.io/fantasy-talking/)

### What it is good for

Short character dialogue and portrait animation from a still image plus a voice recording. [Source 1](https://github.com/Fantasy-AMAP/fantasy-talking/blob/main/README.md) [Source 2](https://fantasy-amap.github.io/fantasy-talking/)

### Demo & examples

The official project page and linked demo show generated portrait videos. These are published examples; no local render was tested. [Source 1](https://github.com/Fantasy-AMAP/fantasy-talking/blob/main/README.md) [Source 2](https://fantasy-amap.github.io/fantasy-talking/)

### Install

Clone the project, install its requirements with PyTorch 2+, and download the documented Wan2.1 I2V 14B 720P, wav2vec2 and FantasyTalking checkpoints. Use infer.py or the optional Gradio app. [Source 1](https://github.com/Fantasy-AMAP/fantasy-talking/blob/main/README.md) [Source 2](https://fantasy-amap.github.io/fantasy-talking/)

1. Obtain the official source or release linked below.
2. Clone the project, install its requirements with PyTorch 2+, and download the documented Wan2.1 I2V 14B 720P, wav2vec2 and FantasyTalking checkpoints. Use infer.py or the optional Gradio app.

```sh
pip install -r requirements.txt
```


```sh
python infer.py --image_path assets/images/woman.png --audio_path assets/audios/woman.wav
```

### First project

Start with a short, representative project and inspect the result before a larger batch. [Source 1](https://github.com/Fantasy-AMAP/fantasy-talking/blob/main/README.md) [Source 2](https://fantasy-amap.github.io/fantasy-talking/)

1. Place an authorized portrait and speech clip in the input paths.
2. Run a short inference with the documented settings.
3. Compare lip motion, identity and temporal consistency before a longer render.
### Hardware & software

Requirements below are documented for this workflow. Unspecified limits are not inferred. [Source 1](https://github.com/Fantasy-AMAP/fantasy-talking/blob/main/README.md) [Source 2](https://fantasy-amap.github.io/fantasy-talking/)

- **Hardware:** Published A100 tests report 40/20/5 GB VRAM configurations for a specified 512×512, 81-frame task. Minimum system RAM and total disk are not documented.
- **Software:** Python environment with project requirements and PyTorch 2+; optional FlashAttention. Gradio/spaces are additional dependencies for app.py.
- **Platforms:** NVIDIA GPU workflow is documented; a full Windows/macOS/Linux support matrix is not provided.

### License, model weights & costs

The full software license was reviewed. Model weights, assets and services remain separate. [Source 1](https://github.com/Fantasy-AMAP/fantasy-talking/blob/main/LICENSE) [Source 2](https://github.com/Fantasy-AMAP/fantasy-talking/blob/main/README.md) [Source 3](https://fantasy-amap.github.io/fantasy-talking/)

- **Code:** Apache-2.0
- **Weights:** Apache-2.0 project code. Wan, wav2vec2 and FantasyTalking checkpoints must be obtained separately; the complete terms for every weight were not established in this review.
- **Commercial:** Software use follows Apache-2.0. Apache-2.0 project code. Wan, wav2vec2 and FantasyTalking checkpoints must be obtained separately; the complete terms for every weight were not established in this review.
- **Cost:** Local compute plus any chosen external model or service; provider access and charges are separate.

### Why it merits attention

Included for the documented creative workflow. A complete guide and popularity do not establish output reliability. [Source 1](https://github.com/Fantasy-AMAP/fantasy-talking/blob/main/README.md) [Source 2](https://fantasy-amap.github.io/fantasy-talking/)

### Limitations

The A100 measurements are configuration-specific: about 40 GB, 20 GB or 5 GB VRAM for different persistence settings at 512×512 and 81 frames, with substantial speed differences. They do not establish a universal 5 GB minimum. [Source 1](https://github.com/Fantasy-AMAP/fantasy-talking/blob/main/README.md) [Source 2](https://fantasy-amap.github.io/fantasy-talking/)

### Get the tool

- [Repository](https://github.com/Fantasy-AMAP/fantasy-talking)
- [Documentation](https://github.com/Fantasy-AMAP/fantasy-talking/blob/main/README.md)

## Visionary

3D, reconstruction & assets · Browser tools & web media · Avatars, digital humans & lip sync · Photogrammetry, scanning & neural rendering · Interactive, immersive & live media

First full guide in this library, establishing a documentation baseline; not a claim of a launch or significant update today.

### Quality assessment: Quality unverified

Software licensing and a concrete creative AI use are supported. The remaining checks do not establish a recommendation.

Scope: Interactive neural-character and captured-scene viewers, with programmable post-processing and conventional 3D content.

Evidence checked: 2026-10-22. No local execution implied.

- **Open-source software license · verified:** The complete root software license was read and archived. The grant covers this project code; unresolved model, service and asset terms are disclosed separately. [Source](https://github.com/Visionary-Laboratory/visionary/blob/main/LICENSE)
- **Creative results · documented:** The README presents avatar, Gaussian and hybrid-rendering examples and links an editor/demo. The hosted editor could not be opened in this pass, so current live availability is unverified. [Source](https://github.com/Visionary-Laboratory/visionary/blob/main/README.md) [Source](https://visionary.openxlab.org.cn/)
- **Reproducible setup · documented:** Use the hosted editor for an initial look, or install Node.js 18+ as recommended, install npm dependencies and start the development server. Independent reproduction has not been established in this review. [Source](https://github.com/Visionary-Laboratory/visionary/blob/main/README.md) [Source](https://visionary.openxlab.org.cn/)
- **Maintenance and support · unknown:** A release or active repository alone does not establish sustained support. Workflow-specific support and unresolved blockers need a deeper review.
- **Independent use · unknown:** Independent first-hand use or a working third-party integration was not established for this selected workflow.
- **Models, services and costs · documented:** Apache-2.0 framework code. Neural models, avatar weights and sample scenes retain separate licenses and are not all cleared by the framework license. Local compute plus any chosen external model or service; provider access and charges are separate. [Source](https://github.com/Visionary-Laboratory/visionary/blob/main/README.md) [Source](https://visionary.openxlab.org.cn/)

Documentation review only; AI Media Scout did not install or run this software. This is a developer rendering/inference framework. A live viewer is not evidence that every model or browser works, and the reviewed documentation identifies meaningful platform constraints.

### How it uses AI

A browser framework combines WebGPU rendering and ONNX inference for neural avatars, Gaussian scenes and hybrid mesh effects. [Source](https://github.com/Visionary-Laboratory/visionary/blob/main/README.md) [Source](https://visionary.openxlab.org.cn/)

### Introduction

A browser framework combines WebGPU rendering and ONNX inference for neural avatars, Gaussian scenes and hybrid mesh effects. [Source 1](https://github.com/Visionary-Laboratory/visionary/blob/main/README.md) [Source 2](https://visionary.openxlab.org.cn/)

### What it is good for

Interactive neural-character and captured-scene viewers, with programmable post-processing and conventional 3D content. [Source 1](https://github.com/Visionary-Laboratory/visionary/blob/main/README.md) [Source 2](https://visionary.openxlab.org.cn/)

### Demo & examples

The README presents avatar, Gaussian and hybrid-rendering examples and links an editor/demo. The hosted editor could not be opened in this pass, so current live availability is unverified. [Source 1](https://github.com/Visionary-Laboratory/visionary/blob/main/README.md) [Source 2](https://visionary.openxlab.org.cn/)

### Install

Use the hosted editor for an initial look, or install Node.js 18+ as recommended, install npm dependencies and start the development server. [Source 1](https://github.com/Visionary-Laboratory/visionary/blob/main/README.md) [Source 2](https://visionary.openxlab.org.cn/)

1. Obtain the official source or release linked below.
2. Use the hosted editor for an initial look, or install Node.js 18+ as recommended, install npm dependencies and start the development server.

```sh
npm install
```


```sh
npm run dev
```

### First project

Start with a short, representative project and inspect the result before a larger batch. [Source 1](https://github.com/Visionary-Laboratory/visionary/blob/main/README.md) [Source 2](https://visionary.openxlab.org.cn/)

1. Open the simple demo on the local server.
2. Load a documented sample scene or neural avatar.
3. Check browser/GPU support and frame behavior before integrating your own assets.
### Hardware & software

Requirements below are documented for this workflow. Unspecified limits are not inferred. [Source 1](https://github.com/Visionary-Laboratory/visionary/blob/main/README.md) [Source 2](https://visionary.openxlab.org.cn/)

- **Hardware:** Discrete GPU recommended on Windows; M4 Max or better advised by the maintainer for heavy Mac workloads. Numeric RAM/VRAM/disk minima are not documented.
- **Software:** Recent Chrome with WebGPU, Node.js 18+ recommended for source development, project npm dependencies and compatible ONNX assets.
- **Platforms:** The maintainer recommends Windows 10/11 with a discrete GPU. Ubuntu has a documented fp16 issue. macOS heavy workloads are described as slow, with M4 Max or better advised for those cases; universal browser portability is not claimed.

### License, model weights & costs

The full software license was reviewed. Model weights, assets and services remain separate. [Source 1](https://github.com/Visionary-Laboratory/visionary/blob/main/LICENSE) [Source 2](https://github.com/Visionary-Laboratory/visionary/blob/main/README.md) [Source 3](https://visionary.openxlab.org.cn/)

- **Code:** Apache-2.0
- **Weights:** Apache-2.0 framework code. Neural models, avatar weights and sample scenes retain separate licenses and are not all cleared by the framework license.
- **Commercial:** Software use follows Apache-2.0. Apache-2.0 framework code. Neural models, avatar weights and sample scenes retain separate licenses and are not all cleared by the framework license.
- **Cost:** Local compute plus any chosen external model or service; provider access and charges are separate.

### Why it merits attention

Included for the documented creative workflow. A complete guide and popularity do not establish output reliability. [Source 1](https://github.com/Visionary-Laboratory/visionary/blob/main/README.md) [Source 2](https://visionary.openxlab.org.cn/)

### Limitations

This is a developer rendering/inference framework. A live viewer is not evidence that every model or browser works, and the reviewed documentation identifies meaningful platform constraints. [Source 1](https://github.com/Visionary-Laboratory/visionary/blob/main/README.md) [Source 2](https://visionary.openxlab.org.cn/)

### Get the tool

- [Repository](https://github.com/Visionary-Laboratory/visionary)
- [Documentation](https://github.com/Visionary-Laboratory/visionary/blob/main/README.md)

## vid2anim

Motion capture & character animation · Neural rigging and digital puppetry · 3D, reconstruction & assets · Games & production pipelines

First full guide in this library. The repository was created 2026-10-13, within the discovery window; that date does not establish a product launch or output quality.

### Quality assessment: Quality unverified

Software licensing and a concrete creative AI use are supported. The remaining checks do not establish a recommendation.

Scope: Creating rough character animation from a movement clip, with GLB/BVH output and a Blender route.

Evidence checked: 2026-10-22. No local execution implied.

- **Open-source software license · verified:** The complete root software license was read and archived. The grant covers this project code; unresolved model, service and asset terms are disclosed separately. [Source](https://github.com/mehulcode12/vid2anim/blob/main/LICENSE)
- **Creative results · documented:** The README shows the multi-engine workflow and retargeting examples. Reported frame rates are maintainer claims, not this review’s measurements. [Source](https://github.com/mehulcode12/vid2anim/blob/main/README.md)
- **Reproducible setup · documented:** Use Python 3.10–3.12, install the package from the source checkout, run its doctor and start the optional web interface. Begin with the CPU-capable MediaPipe engine. Independent reproduction has not been established in this review. [Source](https://github.com/mehulcode12/vid2anim/blob/main/README.md)
- **Maintenance and support · unknown:** A release or active repository alone does not establish sustained support. Workflow-specific support and unresolved blockers need a deeper review.
- **Independent use · unknown:** Independent first-hand use or a working third-party integration was not established for this selected workflow.
- **Models, services and costs · documented:** MIT pipeline code. Engine weights, SMPL-X body models, sample characters and Mixamo/Daz content have separate terms; model access does not clear character assets. Local compute plus any chosen external model or service; provider access and charges are separate. [Source](https://github.com/mehulcode12/vid2anim/blob/main/README.md)

Documentation review only; AI Media Scout did not install or run this software. 2D pose and monocular motion recovery can fail under occlusion. Retargeted motion is a starting point for cleanup. The larger GVHMR route is not equivalent to the lightweight CPU path.

### How it uses AI

Video-to-motion tooling extracts learned body pose with MediaPipe, DWPose or GVHMR and retargets it to animated character files. [Source](https://github.com/mehulcode12/vid2anim/blob/main/README.md)

### Introduction

Video-to-motion tooling extracts learned body pose with MediaPipe, DWPose or GVHMR and retargets it to animated character files. [Source 1](https://github.com/mehulcode12/vid2anim/blob/main/README.md)

### What it is good for

Creating rough character animation from a movement clip, with GLB/BVH output and a Blender route. [Source 1](https://github.com/mehulcode12/vid2anim/blob/main/README.md)

### Demo & examples

The README shows the multi-engine workflow and retargeting examples. Reported frame rates are maintainer claims, not this review’s measurements. [Source 1](https://github.com/mehulcode12/vid2anim/blob/main/README.md)

### Install

Use Python 3.10–3.12, install the package from the source checkout, run its doctor and start the optional web interface. Begin with the CPU-capable MediaPipe engine. [Source 1](https://github.com/mehulcode12/vid2anim/blob/main/README.md)

1. Obtain the official source or release linked below.
2. Use Python 3.10–3.12, install the package from the source checkout, run its doctor and start the optional web interface. Begin with the CPU-capable MediaPipe engine.

```sh
pip install -e .
```


```sh
vid2anim doctor
```


```sh
vid2anim serve
```

### First project

Start with a short, representative project and inspect the result before a larger batch. [Source 1](https://github.com/mehulcode12/vid2anim/blob/main/README.md)

1. Upload a short, clearly visible body-motion clip.
2. Choose an engine and compatible target rig, then extract and retarget.
3. Inspect feet, hands and occluded joints before exporting or editing the animation in Blender.
### Hardware & software

Requirements below are documented for this workflow. Unspecified limits are not inferred. [Source 1](https://github.com/mehulcode12/vid2anim/blob/main/README.md)

- **Hardware:** README model downloads are roughly 28 MB for MediaPipe, 150 MB for DWPose and 5.3 GB for GVHMR assets. These are download sizes, not memory minima; RAM/VRAM requirements are not specified.
- **Software:** Python 3.10–3.12; engine-specific model downloads. A documented Blender addon covers Blender 3.0 through 4.2+.
- **Platforms:** Windows, macOS and Linux setup instructions are supplied. MediaPipe supports the documented CPU route; CUDA and SMPL-X routes add separate constraints.

### License, model weights & costs

The full software license was reviewed. Model weights, assets and services remain separate. [Source 1](https://github.com/mehulcode12/vid2anim/blob/main/LICENSE) [Source 2](https://github.com/mehulcode12/vid2anim/blob/main/README.md)

- **Code:** MIT
- **Weights:** MIT pipeline code. Engine weights, SMPL-X body models, sample characters and Mixamo/Daz content have separate terms; model access does not clear character assets.
- **Commercial:** Software use follows MIT. MIT pipeline code. Engine weights, SMPL-X body models, sample characters and Mixamo/Daz content have separate terms; model access does not clear character assets.
- **Cost:** Local compute plus any chosen external model or service; provider access and charges are separate.

### Why it merits attention

Included for the documented creative workflow. A complete guide and popularity do not establish output reliability. [Source 1](https://github.com/mehulcode12/vid2anim/blob/main/README.md)

### Limitations

2D pose and monocular motion recovery can fail under occlusion. Retargeted motion is a starting point for cleanup. The larger GVHMR route is not equivalent to the lightweight CPU path. [Source 1](https://github.com/mehulcode12/vid2anim/blob/main/README.md)

### Get the tool

- [Repository](https://github.com/mehulcode12/vid2anim)
- [Documentation](https://github.com/mehulcode12/vid2anim/blob/main/README.md)

## Open Mocap Blender

Motion capture & character animation · Neural rigging and digital puppetry · 3D, reconstruction & assets · Interactive, immersive & live media

First full guide in this library, establishing a documentation baseline; not a claim of a launch or significant update today.

### Quality assessment: Quality unverified

Software licensing and a concrete creative AI use are supported. The remaining checks do not establish a recommendation.

Scope: Body-motion experiments and hand-driven character controls inside an older Blender workflow.

Evidence checked: 2026-10-22. No local execution implied.

- **Open-source software license · verified:** The complete root software license was read and archived. The grant covers this project code; unresolved model, service and asset terms are disclosed separately. [Source](https://github.com/Larenju-Rai/open-mocap-blender/blob/main/LICENSE.txt)
- **Creative results · documented:** The maintainer provides a linked video tutorial and example animation assets; they were reviewed as documentation, not reproduced. [Source](https://github.com/Larenju-Rai/open-mocap-blender/blob/main/README.md)
- **Reproducible setup · documented:** Download the official addon, follow the installation tutorial for the supported Blender version, and install its pinned tracking dependencies through the documented addon setup. Independent reproduction has not been established in this review. [Source](https://github.com/Larenju-Rai/open-mocap-blender/blob/main/README.md)
- **Maintenance and support · unknown:** A release or active repository alone does not establish sustained support. Workflow-specific support and unresolved blockers need a deeper review.
- **Independent use · unknown:** Independent first-hand use or a working third-party integration was not established for this selected workflow.
- **Models, services and costs · documented:** MIT addon code. MediaPipe and other dependencies keep their licenses. Example clips and character assets have separate permissions; a sample asset license does not grant unrelated character/IP rights. Local compute plus any chosen external model or service; provider access and charges are separate. [Source](https://github.com/Larenju-Rai/open-mocap-blender/blob/main/README.md)

Documentation review only; AI Media Scout did not install or run this software. Old-host compatibility is a practical constraint, not by itself proof of experimental quality. Independent installation and retargeting reproduction remain unverified.

### How it uses AI

A Blender addon uses MediaPipe pose and hand tracking to turn recorded movement or a live hand feed into animation data. [Source](https://github.com/Larenju-Rai/open-mocap-blender/blob/main/README.md)

### Introduction

A Blender addon uses MediaPipe pose and hand tracking to turn recorded movement or a live hand feed into animation data. [Source 1](https://github.com/Larenju-Rai/open-mocap-blender/blob/main/README.md)

### What it is good for

Body-motion experiments and hand-driven character controls inside an older Blender workflow. [Source 1](https://github.com/Larenju-Rai/open-mocap-blender/blob/main/README.md)

### Demo & examples

The maintainer provides a linked video tutorial and example animation assets; they were reviewed as documentation, not reproduced. [Source 1](https://github.com/Larenju-Rai/open-mocap-blender/blob/main/README.md)

### Install

Download the official addon, follow the installation tutorial for the supported Blender version, and install its pinned tracking dependencies through the documented addon setup. [Source 1](https://github.com/Larenju-Rai/open-mocap-blender/blob/main/README.md)

1. Obtain the official source or release linked below.
2. Download the official addon, follow the installation tutorial for the supported Blender version, and install its pinned tracking dependencies through the documented addon setup.
### First project

Start with a short, representative project and inspect the result before a larger batch. [Source 1](https://github.com/Larenju-Rai/open-mocap-blender/blob/main/README.md)

1. Open the addon in a supported Blender installation.
2. Use a short body clip or the documented live hand input.
3. Retarget to the sample rig and inspect the animation before adapting a character.
### Hardware & software

Requirements below are documented for this workflow. Unspecified limits are not inferred. [Source 1](https://github.com/Larenju-Rai/open-mocap-blender/blob/main/README.md)

- **Hardware:** Minimum system RAM, VRAM and total disk space are not documented in the reviewed instructions.
- **Software:** README restricts support to Blender 4.0.0 or earlier and names Python 3.10, MediaPipe 0.10.14, OpenCV 4.11.0.86 and CVZone 1.6.1; the exact Blender/Python pairing needs compatibility confirmation.
- **Platforms:** Blender host workflow; the README does not establish a tested OS matrix or support for later Blender releases.

### License, model weights & costs

The full software license was reviewed. Model weights, assets and services remain separate. [Source 1](https://github.com/Larenju-Rai/open-mocap-blender/blob/main/LICENSE.txt) [Source 2](https://github.com/Larenju-Rai/open-mocap-blender/blob/main/README.md)

- **Code:** MIT
- **Weights:** MIT addon code. MediaPipe and other dependencies keep their licenses. Example clips and character assets have separate permissions; a sample asset license does not grant unrelated character/IP rights.
- **Commercial:** Software use follows MIT. MIT addon code. MediaPipe and other dependencies keep their licenses. Example clips and character assets have separate permissions; a sample asset license does not grant unrelated character/IP rights.
- **Cost:** Local compute plus any chosen external model or service; provider access and charges are separate.

### Why it merits attention

Included for the documented creative workflow. A complete guide and popularity do not establish output reliability. [Source 1](https://github.com/Larenju-Rai/open-mocap-blender/blob/main/README.md)

### Limitations

Old-host compatibility is a practical constraint, not by itself proof of experimental quality. Independent installation and retargeting reproduction remain unverified. [Source 1](https://github.com/Larenju-Rai/open-mocap-blender/blob/main/README.md)

### Get the tool

- [Repository](https://github.com/Larenju-Rai/open-mocap-blender)
- [Documentation](https://github.com/Larenju-Rai/open-mocap-blender/blob/main/README.md)

## IrisEcho

Images & design · Video, animation & film · Audio, music & voice · 3D, reconstruction & assets · 3D printing & generative CAD

First full guide in this library. The repository was created 2026-09-30, within the discovery window; that date does not establish a product launch or output quality.

### Quality assessment: Quality unverified

Software licensing and a concrete creative AI use are supported. The remaining checks do not establish a recommendation.

Scope: Producing multiple media assets on one Windows workstation while reusing downloaded models and inspecting per-model licenses.

Evidence checked: 2026-10-22. No local execution implied.

- **Open-source software license · verified:** The complete root software license was read and archived. The grant covers this project code; unresolved model, service and asset terms are disclosed separately. [Source](https://github.com/ribbiteer/irisecho/blob/main/LICENSE)
- **Creative results · documented:** The README includes workflow imagery and a workstation demo; the demonstrated machine is an example rather than a requirement. [Source](https://github.com/ribbiteer/irisecho/blob/main/README.md) [Source](https://github.com/ribbiteer/irisecho/blob/main/MODELS.md) [Source](https://github.com/ribbiteer/irisecho/blob/main/THIRD_PARTY_NOTICES.md)
- **Reproducible setup · documented:** Install the Windows release, allow it to prepare its private runtime, select a studio and download a compatible model. Existing model folders can be linked and hash-checked. Independent reproduction has not been established in this review. [Source](https://github.com/ribbiteer/irisecho/blob/main/README.md) [Source](https://github.com/ribbiteer/irisecho/blob/main/MODELS.md) [Source](https://github.com/ribbiteer/irisecho/blob/main/THIRD_PARTY_NOTICES.md)
- **Maintenance and support · unknown:** A release or active repository alone does not establish sustained support. Workflow-specific support and unresolved blockers need a deeper review.
- **Independent use · unknown:** Independent first-hand use or a working third-party integration was not established for this selected workflow.
- **Models, services and costs · documented:** AGPL-3.0-or-later application source. Engines and weights are separate; some are permissive, while FLUX dev, gated audio models, LTX and other options have noncommercial, revenue, access or territory conditions. Review MODELS.md for the selected route. Local compute plus any chosen external model or service; provider access and charges are separate. [Source](https://github.com/ribbiteer/irisecho/blob/main/README.md) [Source](https://github.com/ribbiteer/irisecho/blob/main/MODELS.md) [Source](https://github.com/ribbiteer/irisecho/blob/main/THIRD_PARTY_NOTICES.md)

Documentation review only; AI Media Scout did not install or run this software. A shared queue loads one GPU engine at a time but does not make every model fit the same memory. The unsigned installer and untested platforms are disclosed. STL export does not establish watertight or printable geometry.

### How it uses AI

A desktop media studio orchestrates local image, speech, music, video and 3D engines behind a shared queue and model library. [Source](https://github.com/ribbiteer/irisecho/blob/main/README.md) [Source](https://github.com/ribbiteer/irisecho/blob/main/MODELS.md) [Source](https://github.com/ribbiteer/irisecho/blob/main/THIRD_PARTY_NOTICES.md)

### Introduction

A desktop media studio orchestrates local image, speech, music, video and 3D engines behind a shared queue and model library. [Source 1](https://github.com/ribbiteer/irisecho/blob/main/README.md) [Source 2](https://github.com/ribbiteer/irisecho/blob/main/MODELS.md) [Source 3](https://github.com/ribbiteer/irisecho/blob/main/THIRD_PARTY_NOTICES.md)

### What it is good for

Producing multiple media assets on one Windows workstation while reusing downloaded models and inspecting per-model licenses. [Source 1](https://github.com/ribbiteer/irisecho/blob/main/README.md) [Source 2](https://github.com/ribbiteer/irisecho/blob/main/MODELS.md) [Source 3](https://github.com/ribbiteer/irisecho/blob/main/THIRD_PARTY_NOTICES.md)

### Demo & examples

The README includes workflow imagery and a workstation demo; the demonstrated machine is an example rather than a requirement. [Source 1](https://github.com/ribbiteer/irisecho/blob/main/README.md) [Source 2](https://github.com/ribbiteer/irisecho/blob/main/MODELS.md) [Source 3](https://github.com/ribbiteer/irisecho/blob/main/THIRD_PARTY_NOTICES.md)

### Install

Install the Windows release, allow it to prepare its private runtime, select a studio and download a compatible model. Existing model folders can be linked and hash-checked. [Source 1](https://github.com/ribbiteer/irisecho/blob/main/README.md) [Source 2](https://github.com/ribbiteer/irisecho/blob/main/MODELS.md) [Source 3](https://github.com/ribbiteer/irisecho/blob/main/THIRD_PARTY_NOTICES.md)

1. Obtain the official source or release linked below.
2. Install the Windows release, allow it to prepare its private runtime, select a studio and download a compatible model. Existing model folders can be linked and hash-checked.
### First project

Start with a short, representative project and inspect the result before a larger batch. [Source 1](https://github.com/ribbiteer/irisecho/blob/main/README.md) [Source 2](https://github.com/ribbiteer/irisecho/blob/main/MODELS.md) [Source 3](https://github.com/ribbiteer/irisecho/blob/main/THIRD_PARTY_NOTICES.md)

1. Choose a small supported model in one studio.
2. Generate a short asset and inspect its result and model license.
3. Save or export the accepted result; validate meshes separately before any fabrication.
### Hardware & software

Requirements below are documented for this workflow. Unspecified limits are not inferred. [Source 1](https://github.com/ribbiteer/irisecho/blob/main/README.md) [Source 2](https://github.com/ribbiteer/irisecho/blob/main/MODELS.md) [Source 3](https://github.com/ribbiteer/irisecho/blob/main/THIRD_PARTY_NOTICES.md)

- **Hardware:** Documented Windows baseline: 8 GB VRAM minimum, 12 GB recommended, NVIDIA RTX 20-series or newer. System RAM and complete disk minimum are not specified; downloads vary by model.
- **Software:** The installer creates its own Python environment. Source builds require uv, Node.js 20+ and Rust for the desktop shell; model-specific private engines are downloaded separately.
- **Platforms:** Windows 11 with NVIDIA RTX 20-series or newer is supported. RTX 50 builds are not yet tested. Apple Silicon and Linux are explicitly coming soon, not supported by this assessment.

### License, model weights & costs

The full software license was reviewed. Model weights, assets and services remain separate. [Source 1](https://github.com/ribbiteer/irisecho/blob/main/LICENSE) [Source 2](https://github.com/ribbiteer/irisecho/blob/main/README.md) [Source 3](https://github.com/ribbiteer/irisecho/blob/main/MODELS.md) [Source 4](https://github.com/ribbiteer/irisecho/blob/main/THIRD_PARTY_NOTICES.md)

- **Code:** AGPL-3.0
- **Weights:** AGPL-3.0-or-later application source. Engines and weights are separate; some are permissive, while FLUX dev, gated audio models, LTX and other options have noncommercial, revenue, access or territory conditions. Review MODELS.md for the selected route.
- **Commercial:** Software use follows AGPL-3.0. AGPL-3.0-or-later application source. Engines and weights are separate; some are permissive, while FLUX dev, gated audio models, LTX and other options have noncommercial, revenue, access or territory conditions. Review MODELS.md for the selected route.
- **Cost:** Local compute plus any chosen external model or service; provider access and charges are separate.

### Why it merits attention

Included for the documented creative workflow. A complete guide and popularity do not establish output reliability. [Source 1](https://github.com/ribbiteer/irisecho/blob/main/README.md) [Source 2](https://github.com/ribbiteer/irisecho/blob/main/MODELS.md) [Source 3](https://github.com/ribbiteer/irisecho/blob/main/THIRD_PARTY_NOTICES.md)

### Limitations

A shared queue loads one GPU engine at a time but does not make every model fit the same memory. The unsigned installer and untested platforms are disclosed. STL export does not establish watertight or printable geometry. [Source 1](https://github.com/ribbiteer/irisecho/blob/main/README.md) [Source 2](https://github.com/ribbiteer/irisecho/blob/main/MODELS.md) [Source 3](https://github.com/ribbiteer/irisecho/blob/main/THIRD_PARTY_NOTICES.md)

### Get the tool

- [Repository](https://github.com/ribbiteer/irisecho)
- [Documentation](https://github.com/ribbiteer/irisecho/blob/main/README.md)

## CozyClay

3D, reconstruction & assets · Video, animation & film · Storyboarding, narrative & comics · AI agents for code-authored media production

First full guide in this library, establishing a documentation baseline; not a claim of a launch or significant update today.

### Quality assessment: Quality unverified

Software licensing and a concrete creative AI use are supported. The remaining checks do not establish a recommendation.

Scope: Blocking a scene and camera move, checking a graybox sequence, then exporting guide frames or depth/normal passes for a separate video generator.

Evidence checked: 2026-10-22. No local execution implied.

- **Open-source software license · verified:** The complete root software license was read and archived. The grant covers this project code; unresolved model, service and asset terms are disclosed separately. [Source](https://github.com/NomaDamas/CozyClay/blob/main/LICENSE)
- **Creative results · documented:** The official site and README show the browser studio and exported previs examples; third-party generation and physical plausibility were not tested. [Source](https://github.com/NomaDamas/CozyClay/blob/main/README.md) [Source](https://github.com/NomaDamas/CozyClay/blob/main/LICENSING.md) [Source](https://github.com/NomaDamas/CozyClay/blob/main/THIRD_PARTY_NOTICES.md) [Source](https://cozyclay.org/)
- **Reproducible setup · documented:** Use Node.js 22.19+ and Chromium, then launch the npm package or open the hosted studio. Add a chosen AI provider or MCP-capable agent for language-driven editing. Independent reproduction has not been established in this review. [Source](https://github.com/NomaDamas/CozyClay/blob/main/README.md) [Source](https://github.com/NomaDamas/CozyClay/blob/main/LICENSING.md) [Source](https://github.com/NomaDamas/CozyClay/blob/main/THIRD_PARTY_NOTICES.md) [Source](https://cozyclay.org/)
- **Maintenance and support · unknown:** A release or active repository alone does not establish sustained support. Workflow-specific support and unresolved blockers need a deeper review.
- **Independent use · unknown:** Independent first-hand use or a working third-party integration was not established for this selected workflow.
- **Models, services and costs · documented:** Combined project is AGPL-3.0-or-later, with older GPL-3.0-or-later contributions explained in LICENSING.md. Optional ARDY/Llama models have separate terms. Bundled Mixamo X/Y-bot raw character files are explicitly outside the grant and have unresolved redistribution; use separately cleared assets. Local compute plus any chosen external model or service; provider access and charges are separate. [Source](https://github.com/NomaDamas/CozyClay/blob/main/README.md) [Source](https://github.com/NomaDamas/CozyClay/blob/main/LICENSING.md) [Source](https://github.com/NomaDamas/CozyClay/blob/main/THIRD_PARTY_NOTICES.md) [Source](https://cozyclay.org/)

Documentation review only; AI Media Scout did not install or run this software. Previs is not final AI video. Third-party character redistribution is unresolved, and external generation/agent services have separate costs. No dedicated model GPU is needed for the basic previs route, but browser graphics resources still matter.

### How it uses AI

An agent-accessible browser studio makes editable 3D previs and motion plans, with camera and scene exports for AI video workflows. [Source](https://github.com/NomaDamas/CozyClay/blob/main/README.md) [Source](https://github.com/NomaDamas/CozyClay/blob/main/LICENSING.md) [Source](https://github.com/NomaDamas/CozyClay/blob/main/THIRD_PARTY_NOTICES.md) [Source](https://cozyclay.org/)

### Introduction

An agent-accessible browser studio makes editable 3D previs and motion plans, with camera and scene exports for AI video workflows. [Source 1](https://github.com/NomaDamas/CozyClay/blob/main/README.md) [Source 2](https://github.com/NomaDamas/CozyClay/blob/main/LICENSING.md) [Source 3](https://github.com/NomaDamas/CozyClay/blob/main/THIRD_PARTY_NOTICES.md) [Source 4](https://cozyclay.org/)

### What it is good for

Blocking a scene and camera move, checking a graybox sequence, then exporting guide frames or depth/normal passes for a separate video generator. [Source 1](https://github.com/NomaDamas/CozyClay/blob/main/README.md) [Source 2](https://github.com/NomaDamas/CozyClay/blob/main/LICENSING.md) [Source 3](https://github.com/NomaDamas/CozyClay/blob/main/THIRD_PARTY_NOTICES.md) [Source 4](https://cozyclay.org/)

### Demo & examples

The official site and README show the browser studio and exported previs examples; third-party generation and physical plausibility were not tested. [Source 1](https://github.com/NomaDamas/CozyClay/blob/main/README.md) [Source 2](https://github.com/NomaDamas/CozyClay/blob/main/LICENSING.md) [Source 3](https://github.com/NomaDamas/CozyClay/blob/main/THIRD_PARTY_NOTICES.md) [Source 4](https://cozyclay.org/)

### Install

Use Node.js 22.19+ and Chromium, then launch the npm package or open the hosted studio. Add a chosen AI provider or MCP-capable agent for language-driven editing. [Source 1](https://github.com/NomaDamas/CozyClay/blob/main/README.md) [Source 2](https://github.com/NomaDamas/CozyClay/blob/main/LICENSING.md) [Source 3](https://github.com/NomaDamas/CozyClay/blob/main/THIRD_PARTY_NOTICES.md) [Source 4](https://cozyclay.org/)

1. Obtain the official source or release linked below.
2. Use Node.js 22.19+ and Chromium, then launch the npm package or open the hosted studio. Add a chosen AI provider or MCP-capable agent for language-driven editing.

```sh
npx cozyclay
```

### First project

Start with a short, representative project and inspect the result before a larger batch. [Source 1](https://github.com/NomaDamas/CozyClay/blob/main/README.md) [Source 2](https://github.com/NomaDamas/CozyClay/blob/main/LICENSING.md) [Source 3](https://github.com/NomaDamas/CozyClay/blob/main/THIRD_PARTY_NOTICES.md) [Source 4](https://cozyclay.org/)

1. Block a small scene and describe a camera or object action to the agent.
2. Inspect the preview and motion plan.
3. Export guide frames, a graybox video or other supported passes for a separate generation workflow.
### Hardware & software

Requirements below are documented for this workflow. Unspecified limits are not inferred. [Source 1](https://github.com/NomaDamas/CozyClay/blob/main/README.md) [Source 2](https://github.com/NomaDamas/CozyClay/blob/main/LICENSING.md) [Source 3](https://github.com/NomaDamas/CozyClay/blob/main/THIRD_PARTY_NOTICES.md) [Source 4](https://cozyclay.org/)

- **Hardware:** Minimum system RAM, VRAM and total disk space are not documented in the reviewed instructions.
- **Software:** Node.js 22.19+ and Chromium for the local launcher; browser 3D rendering. AI agent credentials or a supported host are separate.
- **Platforms:** Browser-based local/hosted workflow; a complete tested Windows/macOS/Linux hardware matrix is not documented.

### License, model weights & costs

The full software license was reviewed. Model weights, assets and services remain separate. [Source 1](https://github.com/NomaDamas/CozyClay/blob/main/LICENSE) [Source 2](https://github.com/NomaDamas/CozyClay/blob/main/README.md) [Source 3](https://github.com/NomaDamas/CozyClay/blob/main/LICENSING.md) [Source 4](https://github.com/NomaDamas/CozyClay/blob/main/THIRD_PARTY_NOTICES.md) [Source 5](https://cozyclay.org/)

- **Code:** AGPL-3.0
- **Weights:** Combined project is AGPL-3.0-or-later, with older GPL-3.0-or-later contributions explained in LICENSING.md. Optional ARDY/Llama models have separate terms. Bundled Mixamo X/Y-bot raw character files are explicitly outside the grant and have unresolved redistribution; use separately cleared assets.
- **Commercial:** Software use follows AGPL-3.0. Combined project is AGPL-3.0-or-later, with older GPL-3.0-or-later contributions explained in LICENSING.md. Optional ARDY/Llama models have separate terms. Bundled Mixamo X/Y-bot raw character files are explicitly outside the grant and have unresolved redistribution; use separately cleared assets.
- **Cost:** Local compute plus any chosen external model or service; provider access and charges are separate.

### Why it merits attention

Included for the documented creative workflow. A complete guide and popularity do not establish output reliability. [Source 1](https://github.com/NomaDamas/CozyClay/blob/main/README.md) [Source 2](https://github.com/NomaDamas/CozyClay/blob/main/LICENSING.md) [Source 3](https://github.com/NomaDamas/CozyClay/blob/main/THIRD_PARTY_NOTICES.md) [Source 4](https://cozyclay.org/)

### Limitations

Previs is not final AI video. Third-party character redistribution is unresolved, and external generation/agent services have separate costs. No dedicated model GPU is needed for the basic previs route, but browser graphics resources still matter. [Source 1](https://github.com/NomaDamas/CozyClay/blob/main/README.md) [Source 2](https://github.com/NomaDamas/CozyClay/blob/main/LICENSING.md) [Source 3](https://github.com/NomaDamas/CozyClay/blob/main/THIRD_PARTY_NOTICES.md) [Source 4](https://cozyclay.org/)

### Get the tool

- [Repository](https://github.com/NomaDamas/CozyClay)
- [Documentation](https://github.com/NomaDamas/CozyClay/blob/main/README.md)

## VibeMotion

Video, animation & film · AI kinetic typography and animated lettering · AI agents for code-authored media production

First full guide in this library, establishing a documentation baseline; not a claim of a launch or significant update today.

### Quality assessment: Experimental

Software licensing and a concrete creative AI use are supported. The remaining checks do not establish a recommendation.

Scope: Trying natural-language edits and motion blocks on a short local video project on Windows.

Evidence checked: 2026-10-22. No local execution implied.

Why Experimental: The current README and notice describe a pre-alpha local editing prototype whose UI, API and workflows can change or break. https://github.com/amirmushichge/VibeMotion/blob/main/README.md https://github.com/amirmushichge/VibeMotion/blob/main/THIRD_PARTY_NOTICES.md

- **Open-source software license · verified:** The complete root software license was read and archived. The grant covers this project code; unresolved model, service and asset terms are disclosed separately. [Source](https://github.com/amirmushichge/VibeMotion/blob/main/LICENSE)
- **Creative results · documented:** The README shows workflow previews and QA/render paths. A working independent reproduction has not been established. [Source](https://github.com/amirmushichge/VibeMotion/blob/main/README.md) [Source](https://github.com/amirmushichge/VibeMotion/blob/main/THIRD_PARTY_NOTICES.md)
- **Reproducible setup · documented:** Follow the Windows launcher guide from the official checkout. Its bootstrap prepares Python, FFmpeg and optional inference tools; review the chosen LTX/Gemma model terms before downloading. Independent reproduction has not been established in this review. [Source](https://github.com/amirmushichge/VibeMotion/blob/main/README.md) [Source](https://github.com/amirmushichge/VibeMotion/blob/main/THIRD_PARTY_NOTICES.md)
- **Maintenance and support · unknown:** A release or active repository alone does not establish sustained support. Workflow-specific support and unresolved blockers need a deeper review.
- **Independent use · unknown:** Independent first-hand use or a working third-party integration was not established for this selected workflow.
- **Models, services and costs · documented:** Apache-2.0 app source. LTX package/weights have community terms, Gemma has its own terms, and generated previews use GSAP under its separate no-charge license. A repacked model fallback has unresolved terms. Local compute plus any chosen external model or service; provider access and charges are separate. [Source](https://github.com/amirmushichge/VibeMotion/blob/main/README.md) [Source](https://github.com/amirmushichge/VibeMotion/blob/main/THIRD_PARTY_NOTICES.md)

Documentation review only; AI Media Scout did not install or run this software. The current project is explicitly pre-alpha with unstable UI/API/workflows. Basic editing and the much heavier NVIDIA generation path should be assessed separately.

### How it uses AI

A local video-editing prototype combines an LLM editing agent, transcription, motion graphics and optional LTX video generation. [Source](https://github.com/amirmushichge/VibeMotion/blob/main/README.md) [Source](https://github.com/amirmushichge/VibeMotion/blob/main/THIRD_PARTY_NOTICES.md)

### Introduction

A local video-editing prototype combines an LLM editing agent, transcription, motion graphics and optional LTX video generation. [Source 1](https://github.com/amirmushichge/VibeMotion/blob/main/README.md) [Source 2](https://github.com/amirmushichge/VibeMotion/blob/main/THIRD_PARTY_NOTICES.md)

### What it is good for

Trying natural-language edits and motion blocks on a short local video project on Windows. [Source 1](https://github.com/amirmushichge/VibeMotion/blob/main/README.md) [Source 2](https://github.com/amirmushichge/VibeMotion/blob/main/THIRD_PARTY_NOTICES.md)

### Demo & examples

The README shows workflow previews and QA/render paths. A working independent reproduction has not been established. [Source 1](https://github.com/amirmushichge/VibeMotion/blob/main/README.md) [Source 2](https://github.com/amirmushichge/VibeMotion/blob/main/THIRD_PARTY_NOTICES.md)

### Install

Follow the Windows launcher guide from the official checkout. Its bootstrap prepares Python, FFmpeg and optional inference tools; review the chosen LTX/Gemma model terms before downloading. [Source 1](https://github.com/amirmushichge/VibeMotion/blob/main/README.md) [Source 2](https://github.com/amirmushichge/VibeMotion/blob/main/THIRD_PARTY_NOTICES.md)

1. Obtain the official source or release linked below.
2. Follow the Windows launcher guide from the official checkout. Its bootstrap prepares Python, FFmpeg and optional inference tools; review the chosen LTX/Gemma model terms before downloading.
### First project

Start with a short, representative project and inspect the result before a larger batch. [Source 1](https://github.com/amirmushichge/VibeMotion/blob/main/README.md) [Source 2](https://github.com/amirmushichge/VibeMotion/blob/main/THIRD_PARTY_NOTICES.md)

1. Create a local project with a short clip.
2. Ask the agent for a small edit or motion block and inspect its preview.
3. Use the documented QA and render controls to export a test MP4.
### Hardware & software

Requirements below are documented for this workflow. Unspecified limits are not inferred. [Source 1](https://github.com/amirmushichge/VibeMotion/blob/main/README.md) [Source 2](https://github.com/amirmushichge/VibeMotion/blob/main/THIRD_PARTY_NOTICES.md)

- **Hardware:** Basic editing has a CPU route; local LTX generation needs NVIDIA GPU support. A reliable RAM/VRAM/disk minimum is not documented in the reviewed instructions.
- **Software:** Windows launch scripts, Python 3.11+, FFmpeg/ffprobe and an Ollama or configured model route. Optional GPU generation adds PyTorch, LTX and Gemma dependencies; automated provisioning uses winget.
- **Platforms:** Windows 10/11 is the documented path. Other operating systems are not established by the reviewed installation guide.

### License, model weights & costs

The full software license was reviewed. Model weights, assets and services remain separate. [Source 1](https://github.com/amirmushichge/VibeMotion/blob/main/LICENSE) [Source 2](https://github.com/amirmushichge/VibeMotion/blob/main/README.md) [Source 3](https://github.com/amirmushichge/VibeMotion/blob/main/THIRD_PARTY_NOTICES.md)

- **Code:** Apache-2.0
- **Weights:** Apache-2.0 app source. LTX package/weights have community terms, Gemma has its own terms, and generated previews use GSAP under its separate no-charge license. A repacked model fallback has unresolved terms.
- **Commercial:** Software use follows Apache-2.0. Apache-2.0 app source. LTX package/weights have community terms, Gemma has its own terms, and generated previews use GSAP under its separate no-charge license. A repacked model fallback has unresolved terms.
- **Cost:** Local compute plus any chosen external model or service; provider access and charges are separate.

### Why it merits attention

Included for the documented creative workflow. A complete guide and popularity do not establish output reliability. [Source 1](https://github.com/amirmushichge/VibeMotion/blob/main/README.md) [Source 2](https://github.com/amirmushichge/VibeMotion/blob/main/THIRD_PARTY_NOTICES.md)

### Limitations

The current project is explicitly pre-alpha with unstable UI/API/workflows. Basic editing and the much heavier NVIDIA generation path should be assessed separately. [Source 1](https://github.com/amirmushichge/VibeMotion/blob/main/README.md) [Source 2](https://github.com/amirmushichge/VibeMotion/blob/main/THIRD_PARTY_NOTICES.md)

### Get the tool

- [Repository](https://github.com/amirmushichge/VibeMotion)
- [Documentation](https://github.com/amirmushichge/VibeMotion/blob/main/README.md)

## OpenFlowKit

Vector graphics, illustration & textures · Data art & scientific visualization · Browser tools & web media · Creative learning & authoring

First full guide, completing an earlier screened library entry with installation, use and documented requirements. This is a review-depth improvement, not a verified new software release.

### Quality assessment: Quality unverified

Software licensing and a concrete creative AI use are supported. The remaining checks do not establish a recommendation.

Scope: Explaining systems with AI-assisted flowcharts, architecture maps and animated diagram sequences that remain editable.

Evidence checked: 2026-10-22. No local execution implied.

- **Open-source software license · verified:** The complete root software license was read and archived. The grant covers this project code; unresolved model, service and asset terms are disclosed separately. [Source](https://github.com/openflowkit/openflowkit/blob/main/LICENSE)
- **Creative results · documented:** The public browser app and README demonstrate generated diagrams, live canvas edits and export formats. [Source](https://github.com/openflowkit/openflowkit/blob/main/README.md) [Source](https://app.openflowkit.com) [Source](https://docs.openflowkit.com/self-hosting/)
- **Reproducible setup · documented:** Open the hosted app or self-host its static Docker build. Configure an AI provider or the documented MCP bridge for agent editing; ordinary drawing works without AI. Independent reproduction has not been established in this review. [Source](https://github.com/openflowkit/openflowkit/blob/main/README.md) [Source](https://app.openflowkit.com) [Source](https://docs.openflowkit.com/self-hosting/)
- **Maintenance and support · unknown:** A release or active repository alone does not establish sustained support. Workflow-specific support and unresolved blockers need a deeper review.
- **Independent use · unknown:** Independent first-hand use or a working third-party integration was not established for this selected workflow.
- **Models, services and costs · documented:** MIT project code. AI-provider services and any imported icon/content licenses are separate; the model service is not bundled under MIT. Local compute plus any chosen external model or service; provider access and charges are separate. [Source](https://github.com/openflowkit/openflowkit/blob/main/README.md) [Source](https://app.openflowkit.com) [Source](https://docs.openflowkit.com/self-hosting/)

Documentation review only; AI Media Scout did not install or run this software. No real-time collaborative editing. AI calls, share links and repository maps use the network. Diagrams stay in browser storage unless exported; back them up. Usage analytics can be disabled.

### How it uses AI

An editable diagram canvas connects language-model assistants to a diagram DSL, direct canvas operations and animated exports. [Source](https://github.com/openflowkit/openflowkit/blob/main/README.md) [Source](https://app.openflowkit.com) [Source](https://docs.openflowkit.com/self-hosting/)

### Introduction

An editable diagram canvas connects language-model assistants to a diagram DSL, direct canvas operations and animated exports. [Source 1](https://github.com/openflowkit/openflowkit/blob/main/README.md) [Source 2](https://app.openflowkit.com) [Source 3](https://docs.openflowkit.com/self-hosting/)

### What it is good for

Explaining systems with AI-assisted flowcharts, architecture maps and animated diagram sequences that remain editable. [Source 1](https://github.com/openflowkit/openflowkit/blob/main/README.md) [Source 2](https://app.openflowkit.com) [Source 3](https://docs.openflowkit.com/self-hosting/)

### Demo & examples

The public browser app and README demonstrate generated diagrams, live canvas edits and export formats. [Source 1](https://github.com/openflowkit/openflowkit/blob/main/README.md) [Source 2](https://app.openflowkit.com) [Source 3](https://docs.openflowkit.com/self-hosting/)

### Install

Open the hosted app or self-host its static Docker build. Configure an AI provider or the documented MCP bridge for agent editing; ordinary drawing works without AI. [Source 1](https://github.com/openflowkit/openflowkit/blob/main/README.md) [Source 2](https://app.openflowkit.com) [Source 3](https://docs.openflowkit.com/self-hosting/)

1. Obtain the official source or release linked below.
2. Open the hosted app or self-host its static Docker build. Configure an AI provider or the documented MCP bridge for agent editing; ordinary drawing works without AI.

```sh
docker build -t openflowkit .
```


```sh
docker run --rm -p 3045:3045 openflowkit
```

### First project

Start with a short, representative project and inspect the result before a larger batch. [Source 1](https://github.com/openflowkit/openflowkit/blob/main/README.md) [Source 2](https://app.openflowkit.com) [Source 3](https://docs.openflowkit.com/self-hosting/)

1. Start a diagram and describe its structure to a configured AI assistant.
2. Inspect labels and connections on the canvas.
3. Export SVG/PDF or an animated format, and save JSON for later editing.
### Hardware & software

Requirements below are documented for this workflow. Unspecified limits are not inferred. [Source 1](https://github.com/openflowkit/openflowkit/blob/main/README.md) [Source 2](https://app.openflowkit.com) [Source 3](https://docs.openflowkit.com/self-hosting/)

- **Hardware:** Minimum system RAM, VRAM and total disk space are not documented in the reviewed instructions.
- **Software:** Current desktop browser with WebGL; Chromium is the automated-test target. Self-hosting needs Docker; CLI/MCP Node requirements differ from the source development environment.
- **Platforms:** Desktop browser workflow with Windows/Linux keyboard variants documented. A browser interface is not evidence of every platform/GPU combination.

### License, model weights & costs

The full software license was reviewed. Model weights, assets and services remain separate. [Source 1](https://github.com/openflowkit/openflowkit/blob/main/LICENSE) [Source 2](https://github.com/openflowkit/openflowkit/blob/main/README.md) [Source 3](https://app.openflowkit.com) [Source 4](https://docs.openflowkit.com/self-hosting/)

- **Code:** MIT
- **Weights:** MIT project code. AI-provider services and any imported icon/content licenses are separate; the model service is not bundled under MIT.
- **Commercial:** Software use follows MIT. MIT project code. AI-provider services and any imported icon/content licenses are separate; the model service is not bundled under MIT.
- **Cost:** Local compute plus any chosen external model or service; provider access and charges are separate.

### Why it merits attention

Included for the documented creative workflow. A complete guide and popularity do not establish output reliability. [Source 1](https://github.com/openflowkit/openflowkit/blob/main/README.md) [Source 2](https://app.openflowkit.com) [Source 3](https://docs.openflowkit.com/self-hosting/)

### Limitations

No real-time collaborative editing. AI calls, share links and repository maps use the network. Diagrams stay in browser storage unless exported; back them up. Usage analytics can be disabled. [Source 1](https://github.com/openflowkit/openflowkit/blob/main/README.md) [Source 2](https://app.openflowkit.com) [Source 3](https://docs.openflowkit.com/self-hosting/)

### Get the tool

- [Repository](https://github.com/openflowkit/openflowkit)
- [Documentation](https://github.com/openflowkit/openflowkit/blob/main/README.md)

## Shaderera

Video, animation & film · Computational art & creative coding · AI kinetic typography and animated lettering · AI agents for code-authored media production

First full guide, completing an earlier screened library entry with installation, use and documented requirements. This is a review-depth improvement, not a verified new software release.

### Quality assessment: Quality unverified

Software licensing and a concrete creative AI use are supported. The remaining checks do not establish a recommendation.

Scope: Editable title sequences, shader films and campaign variations rendered from a time-based scene program.

Evidence checked: 2026-10-22. No local execution implied.

- **Open-source software license · verified:** The complete root software license was read and archived. The grant covers this project code; unresolved model, service and asset terms are disclosed separately. [Source](https://github.com/shaderera/shaderera/blob/main/LICENSE)
- **Creative results · documented:** The README demonstrates frame inspection, contact sheets and rendered films; technical checks do not by themselves judge visual taste. [Source](https://github.com/shaderera/shaderera/blob/main/README.md) [Source](https://github.com/shaderera/shaderera/blob/main/INSTALL.md)
- **Reproducible setup · documented:** Use Node.js 24+ and FFmpeg, scaffold a project, install its dependencies, then run doctor and check. Configure its optional MCP server in a chosen coding agent. Independent reproduction has not been established in this review. [Source](https://github.com/shaderera/shaderera/blob/main/README.md) [Source](https://github.com/shaderera/shaderera/blob/main/INSTALL.md)
- **Maintenance and support · unknown:** A release or active repository alone does not establish sustained support. Workflow-specific support and unresolved blockers need a deeper review.
- **Independent use · unknown:** Independent first-hand use or a working third-party integration was not established for this selected workflow.
- **Models, services and costs · documented:** MIT engine, plugins and skills. Font plugins use SIL OFL; name/logo are separately reserved. Coding-agent/model services and imported assets have separate terms. Local compute plus any chosen external model or service; provider access and charges are separate. [Source](https://github.com/shaderera/shaderera/blob/main/README.md) [Source](https://github.com/shaderera/shaderera/blob/main/INSTALL.md)

Documentation review only; AI Media Scout did not install or run this software. This is an agent-oriented programming workflow, not a prompt-only video model. Deterministic frame checks do not prove creative quality; rendering requirements vary by scene.

### How it uses AI

A code-based film engine gives AI coding agents deterministic rendering, inspection and delivery tools for procedural motion graphics. [Source](https://github.com/shaderera/shaderera/blob/main/README.md) [Source](https://github.com/shaderera/shaderera/blob/main/INSTALL.md)

### Introduction

A code-based film engine gives AI coding agents deterministic rendering, inspection and delivery tools for procedural motion graphics. [Source 1](https://github.com/shaderera/shaderera/blob/main/README.md) [Source 2](https://github.com/shaderera/shaderera/blob/main/INSTALL.md)

### What it is good for

Editable title sequences, shader films and campaign variations rendered from a time-based scene program. [Source 1](https://github.com/shaderera/shaderera/blob/main/README.md) [Source 2](https://github.com/shaderera/shaderera/blob/main/INSTALL.md)

### Demo & examples

The README demonstrates frame inspection, contact sheets and rendered films; technical checks do not by themselves judge visual taste. [Source 1](https://github.com/shaderera/shaderera/blob/main/README.md) [Source 2](https://github.com/shaderera/shaderera/blob/main/INSTALL.md)

### Install

Use Node.js 24+ and FFmpeg, scaffold a project, install its dependencies, then run doctor and check. Configure its optional MCP server in a chosen coding agent. [Source 1](https://github.com/shaderera/shaderera/blob/main/README.md) [Source 2](https://github.com/shaderera/shaderera/blob/main/INSTALL.md)

1. Obtain the official source or release linked below.
2. Use Node.js 24+ and FFmpeg, scaffold a project, install its dependencies, then run doctor and check. Configure its optional MCP server in a chosen coding agent.

```sh
npx create-shaderera@latest my-film
```


```sh
cd my-film
```


```sh
npm install
```


```sh
npx shaderera doctor
```


```sh
npx shaderera check
```

### First project

Start with a short, representative project and inspect the result before a larger batch. [Source 1](https://github.com/shaderera/shaderera/blob/main/README.md) [Source 2](https://github.com/shaderera/shaderera/blob/main/INSTALL.md)

1. Describe a short film and edit its render(t) scene with the agent.
2. Generate stills/contact sheets and inspect timing and text.
3. Render a video only after the project checks pass.
### Hardware & software

Requirements below are documented for this workflow. Unspecified limits are not inferred. [Source 1](https://github.com/shaderera/shaderera/blob/main/README.md) [Source 2](https://github.com/shaderera/shaderera/blob/main/INSTALL.md)

- **Hardware:** Minimum system RAM, VRAM and total disk space are not documented in the reviewed instructions.
- **Software:** Node.js 24+, FFmpeg; Chrome is additionally needed for browser-host films. GPU/WebGPU requirements depend on the selected renderer.
- **Platforms:** Installation guidance covers macOS, Windows and Linux. Browser and GPU hosts still need compatible local graphics support.

### License, model weights & costs

The full software license was reviewed. Model weights, assets and services remain separate. [Source 1](https://github.com/shaderera/shaderera/blob/main/LICENSE) [Source 2](https://github.com/shaderera/shaderera/blob/main/README.md) [Source 3](https://github.com/shaderera/shaderera/blob/main/INSTALL.md)

- **Code:** MIT
- **Weights:** MIT engine, plugins and skills. Font plugins use SIL OFL; name/logo are separately reserved. Coding-agent/model services and imported assets have separate terms.
- **Commercial:** Software use follows MIT. MIT engine, plugins and skills. Font plugins use SIL OFL; name/logo are separately reserved. Coding-agent/model services and imported assets have separate terms.
- **Cost:** Local compute plus any chosen external model or service; provider access and charges are separate.

### Why it merits attention

Included for the documented creative workflow. A complete guide and popularity do not establish output reliability. [Source 1](https://github.com/shaderera/shaderera/blob/main/README.md) [Source 2](https://github.com/shaderera/shaderera/blob/main/INSTALL.md)

### Limitations

This is an agent-oriented programming workflow, not a prompt-only video model. Deterministic frame checks do not prove creative quality; rendering requirements vary by scene. [Source 1](https://github.com/shaderera/shaderera/blob/main/README.md) [Source 2](https://github.com/shaderera/shaderera/blob/main/INSTALL.md)

### Get the tool

- [Repository](https://github.com/shaderera/shaderera)
- [Documentation](https://github.com/shaderera/shaderera/blob/main/README.md)

## phonepod

Audio, music & voice · Editing, captions & post-production · Archives, media restoration & collections

First full guide in this library, establishing a documentation baseline; not a claim of a launch or significant update today.

### Quality assessment: Quality unverified

Software licensing and a concrete creative AI use are supported. The remaining checks do not establish a recommendation.

Scope: Cleaning noisy spoken voice memos into a mono podcast draft without a cloud upload.

Evidence checked: 2026-10-22. No local execution implied.

- **Open-source software license · verified:** The complete root software license was read and archived. The grant covers this project code; unresolved model, service and asset terms are disclosed separately. [Source](https://github.com/vedantggwp/phonepod/blob/main/LICENSE)
- **Creative results · documented:** The README says before/after audio demos are still coming; its quality and speed descriptions are author claims, not verified listening evidence. [Source](https://github.com/vedantggwp/phonepod/blob/main/README.md)
- **Reproducible setup · documented:** Install Python 3.11+ and FFmpeg, then the phonepod package. The optional UI extra exposes a local browser interface. Independent reproduction has not been established in this review. [Source](https://github.com/vedantggwp/phonepod/blob/main/README.md)
- **Maintenance and support · unknown:** A release or active repository alone does not establish sustained support. Workflow-specific support and unresolved blockers need a deeper review.
- **Independent use · unknown:** Independent first-hand use or a working third-party integration was not established for this selected workflow.
- **Models, services and costs · documented:** MIT application code; DeepFilterNet, MossFormer and DSP dependencies retain separate licenses. A complete review of all downloaded model terms remains pending. Local compute plus any chosen external model or service; provider access and charges are separate. [Source](https://github.com/vedantggwp/phonepod/blob/main/README.md)

Documentation review only; AI Media Scout did not install or run this software. The beta API may change. No hosted before/after demo is available yet, and enhancement can alter voice detail. The author’s seven-second timing for a two-minute file is not an independently reproduced benchmark.

### How it uses AI

A local speech-restoration pipeline combines DeepFilterNet3 and MossFormer2 neural enhancement with a conventional mastering chain. [Source](https://github.com/vedantggwp/phonepod/blob/main/README.md)

### Introduction

A local speech-restoration pipeline combines DeepFilterNet3 and MossFormer2 neural enhancement with a conventional mastering chain. [Source 1](https://github.com/vedantggwp/phonepod/blob/main/README.md)

### What it is good for

Cleaning noisy spoken voice memos into a mono podcast draft without a cloud upload. [Source 1](https://github.com/vedantggwp/phonepod/blob/main/README.md)

### Demo & examples

The README says before/after audio demos are still coming; its quality and speed descriptions are author claims, not verified listening evidence. [Source 1](https://github.com/vedantggwp/phonepod/blob/main/README.md)

### Install

Install Python 3.11+ and FFmpeg, then the phonepod package. The optional UI extra exposes a local browser interface. [Source 1](https://github.com/vedantggwp/phonepod/blob/main/README.md)

1. Obtain the official source or release linked below.
2. Install Python 3.11+ and FFmpeg, then the phonepod package. The optional UI extra exposes a local browser interface.

```sh
pip install phonepod
```


```sh
phonepod recording.m4a podcast.wav
```


```sh
pip install "phonepod[ui]"
```


```sh
python -m phonepod.app
```

### First project

Start with a short, representative project and inspect the result before a larger batch. [Source 1](https://github.com/vedantggwp/phonepod/blob/main/README.md)

1. Choose a short speech recording.
2. Run the CLI or local UI to produce a 48 kHz mono WAV.
3. Compare intelligibility, noise and artifacts against the untouched recording.
### Hardware & software

Requirements below are documented for this workflow. Unspecified limits are not inferred. [Source 1](https://github.com/vedantggwp/phonepod/blob/main/README.md)

- **Hardware:** CPU inference is documented. Minimum RAM, model-download total and disk requirements are not specified.
- **Software:** Python 3.11+, FFmpeg and the package dependencies; optional UI dependencies for port 7860.
- **Platforms:** CPU operation is documented, with an Apple Silicon timing example and macOS/Linux package classifiers. A Windows support claim was not established.

### License, model weights & costs

The full software license was reviewed. Model weights, assets and services remain separate. [Source 1](https://github.com/vedantggwp/phonepod/blob/main/LICENSE) [Source 2](https://github.com/vedantggwp/phonepod/blob/main/README.md)

- **Code:** MIT
- **Weights:** MIT application code; DeepFilterNet, MossFormer and DSP dependencies retain separate licenses. A complete review of all downloaded model terms remains pending.
- **Commercial:** Software use follows MIT. MIT application code; DeepFilterNet, MossFormer and DSP dependencies retain separate licenses. A complete review of all downloaded model terms remains pending.
- **Cost:** Local compute plus any chosen external model or service; provider access and charges are separate.

### Why it merits attention

Included for the documented creative workflow. A complete guide and popularity do not establish output reliability. [Source 1](https://github.com/vedantggwp/phonepod/blob/main/README.md)

### Limitations

The beta API may change. No hosted before/after demo is available yet, and enhancement can alter voice detail. The author’s seven-second timing for a two-minute file is not an independently reproduced benchmark. [Source 1](https://github.com/vedantggwp/phonepod/blob/main/README.md)

### Get the tool

- [Repository](https://github.com/vedantggwp/phonepod)
- [Documentation](https://github.com/vedantggwp/phonepod/blob/main/README.md)

## SignFlow

AI signing avatars and expressive gesture media · Avatars, digital humans & lip sync · Accessible media & assistive creation · Interactive, immersive & live media

First full guide in this library, establishing a documentation baseline; not a claim of a launch or significant update today.

### Quality assessment: Quality unverified

Software licensing and a concrete creative AI use are supported. The remaining checks do not establish a recommendation.

Scope: Exploring camera-driven gesture recognition and a spoken-word-to-signing-avatar interface for accessible-media prototypes.

Evidence checked: 2026-10-22. No local execution implied.

- **Open-source software license · verified:** The complete root software license was read and archived. The grant covers this project code; unresolved model, service and asset terms are disclosed separately. [Source](https://github.com/Leander-bai/SignFlow/blob/main/LICENSE)
- **Creative results · documented:** The README describes the avatar and recognition architecture. No independent Deaf-user evaluation or reliable continuous-ASL translation result was established. [Source](https://github.com/Leander-bai/SignFlow/blob/main/README.md)
- **Reproducible setup · documented:** Prepare Node.js 20+, PostgreSQL and the documented speech/LLM/TTS provider configuration; install dependencies, initialize the application schema and start its local server. Independent reproduction has not been established in this review. [Source](https://github.com/Leander-bai/SignFlow/blob/main/README.md)
- **Maintenance and support · unknown:** A release or active repository alone does not establish sustained support. Workflow-specific support and unresolved blockers need a deeper review.
- **Independent use · unknown:** Independent first-hand use or a working third-party integration was not established for this selected workflow.
- **Models, services and costs · documented:** MIT app code. Ready Player Me/Mixamo avatar and motion assets, MediaPipe models and external speech/LLM/TTS services have separate terms. Local compute plus any chosen external model or service; provider access and charges are separate. [Source](https://github.com/Leander-bai/SignFlow/blob/main/README.md)

Documentation review only; AI Media Scout did not install or run this software. The 500+ pose dictionary is not a proven general-ASL translator. Word-level animation and a small FBX set can lose grammar or nonmanual meaning. Cloud speech/LLM/TTS paths contradict any assumption that all processing stays local.

### How it uses AI

A browser application combines learned hand/body/face tracking, speech services and a 3D pose dictionary for bidirectional sign-avatar experiments. [Source](https://github.com/Leander-bai/SignFlow/blob/main/README.md)

### Introduction

A browser application combines learned hand/body/face tracking, speech services and a 3D pose dictionary for bidirectional sign-avatar experiments. [Source 1](https://github.com/Leander-bai/SignFlow/blob/main/README.md)

### What it is good for

Exploring camera-driven gesture recognition and a spoken-word-to-signing-avatar interface for accessible-media prototypes. [Source 1](https://github.com/Leander-bai/SignFlow/blob/main/README.md)

### Demo & examples

The README describes the avatar and recognition architecture. No independent Deaf-user evaluation or reliable continuous-ASL translation result was established. [Source 1](https://github.com/Leander-bai/SignFlow/blob/main/README.md)

### Install

Prepare Node.js 20+, PostgreSQL and the documented speech/LLM/TTS provider configuration; install dependencies, initialize the application schema and start its local server. [Source 1](https://github.com/Leander-bai/SignFlow/blob/main/README.md)

1. Obtain the official source or release linked below.
2. Prepare Node.js 20+, PostgreSQL and the documented speech/LLM/TTS provider configuration; install dependencies, initialize the application schema and start its local server.

```sh
npm install
```


```sh
npm run db:push
```


```sh
npm run dev
```

### First project

Start with a short, representative project and inspect the result before a larger batch. [Source 1](https://github.com/Leander-bai/SignFlow/blob/main/README.md)

1. Start the app and grant camera/microphone access.
2. Try a small known dictionary sign or short spoken phrase.
3. Inspect handshape, facial expression and meaning with a competent signer; do not treat the output as validated interpretation.
### Hardware & software

Requirements below are documented for this workflow. Unspecified limits are not inferred. [Source 1](https://github.com/Leander-bai/SignFlow/blob/main/README.md)

- **Hardware:** Webcam, microphone and WebGL-capable graphics are used. Minimum system RAM, GPU memory and storage are not documented.
- **Software:** Node.js 20+, PostgreSQL, React/Three.js, MediaPipe Tasks Vision; Deepgram, DeepSeek and configured OpenAI/Replit TTS service access.
- **Platforms:** Browser workflow using WebGL-accelerated tracking; the README does not establish a tested OS/browser matrix.

### License, model weights & costs

The full software license was reviewed. Model weights, assets and services remain separate. [Source 1](https://github.com/Leander-bai/SignFlow/blob/main/LICENSE) [Source 2](https://github.com/Leander-bai/SignFlow/blob/main/README.md)

- **Code:** MIT
- **Weights:** MIT app code. Ready Player Me/Mixamo avatar and motion assets, MediaPipe models and external speech/LLM/TTS services have separate terms.
- **Commercial:** Software use follows MIT. MIT app code. Ready Player Me/Mixamo avatar and motion assets, MediaPipe models and external speech/LLM/TTS services have separate terms.
- **Cost:** Local compute plus any chosen external model or service; provider access and charges are separate.

### Why it merits attention

Included for the documented creative workflow. A complete guide and popularity do not establish output reliability. [Source 1](https://github.com/Leander-bai/SignFlow/blob/main/README.md)

### Limitations

The 500+ pose dictionary is not a proven general-ASL translator. Word-level animation and a small FBX set can lose grammar or nonmanual meaning. Cloud speech/LLM/TTS paths contradict any assumption that all processing stays local. [Source 1](https://github.com/Leander-bai/SignFlow/blob/main/README.md)

### Get the tool

- [Repository](https://github.com/Leander-bai/SignFlow)
- [Documentation](https://github.com/Leander-bai/SignFlow/blob/main/README.md)

## Open Garden Planner

AI landscape, garden and environmental design · AI architectural visualization and spatial design · Vector graphics, illustration & textures · 3D printing & generative CAD

First full guide, completing an earlier screened library entry with installation, use and documented requirements. This is a review-depth improvement, not a verified new software release.

### Quality assessment: Quality unverified

Software licensing and a concrete creative AI use are supported. The remaining checks do not establish a recommendation.

Scope: AI-assisted garden layout, calibrated site diagrams and editable plant/structure plans with drawing exports.

Evidence checked: 2026-10-22. No local execution implied.

- **Open-source software license · verified:** The complete root software license was read and archived. The grant covers this project code; unresolved model, service and asset terms are disclosed separately. [Source](https://github.com/cofade/open-garden-planner/blob/master/LICENSE)
- **Creative results · documented:** The README shows the desktop planner and describes the linked 2D/3D plan workflow. Agent-driven plan quality and horticultural outcomes were not independently validated. [Source](https://github.com/cofade/open-garden-planner/blob/master/README.md)
- **Reproducible setup · documented:** Use the official Windows installer, checking the supplied checksum/provenance, or install from source with Python 3.11+. Enable and configure the embedded agent integration for the AI-assisted route. Independent reproduction has not been established in this review. [Source](https://github.com/cofade/open-garden-planner/blob/master/README.md)
- **Maintenance and support · unknown:** A release or active repository alone does not establish sustained support. Workflow-specific support and unresolved blockers need a deeper review.
- **Independent use · unknown:** Independent first-hand use or a working third-party integration was not established for this selected workflow.
- **Models, services and costs · documented:** GPL-3.0 software. External AI providers, plant databases and imported images retain their own terms and access requirements. Local compute plus any chosen external model or service; provider access and charges are separate. [Source](https://github.com/cofade/open-garden-planner/blob/master/README.md)

Documentation review only; AI Media Scout did not install or run this software. The current 3D workflow assumes flat ground. Unmeasured RAM limits and ongoing 3D development are disclosed; a precise drawing or plant trait record does not prove structural or growing suitability.

### How it uses AI

A metric garden-design application exposes its live plan to AI agents through an embedded MCP server for inspection, visualization and optional editing. [Source](https://github.com/cofade/open-garden-planner/blob/master/README.md)

### Introduction

A metric garden-design application exposes its live plan to AI agents through an embedded MCP server for inspection, visualization and optional editing. [Source 1](https://github.com/cofade/open-garden-planner/blob/master/README.md)

### What it is good for

AI-assisted garden layout, calibrated site diagrams and editable plant/structure plans with drawing exports. [Source 1](https://github.com/cofade/open-garden-planner/blob/master/README.md)

### Demo & examples

The README shows the desktop planner and describes the linked 2D/3D plan workflow. Agent-driven plan quality and horticultural outcomes were not independently validated. [Source 1](https://github.com/cofade/open-garden-planner/blob/master/README.md)

### Install

Use the official Windows installer, checking the supplied checksum/provenance, or install from source with Python 3.11+. Enable and configure the embedded agent integration for the AI-assisted route. [Source 1](https://github.com/cofade/open-garden-planner/blob/master/README.md)

1. Obtain the official source or release linked below.
2. Use the official Windows installer, checking the supplied checksum/provenance, or install from source with Python 3.11+. Enable and configure the embedded agent integration for the AI-assisted route.

```sh
pip install -e .
```


```sh
python -m open_garden_planner
```

### First project

Start with a short, representative project and inspect the result before a larger batch. [Source 1](https://github.com/cofade/open-garden-planner/blob/master/README.md)

1. Import and calibrate a site image or create a metric plan.
2. Use the agent integration to inspect the plan and request a bounded edit.
3. Review dimensions and layers, then export SVG, PDF, DXF or a plant list.
### Hardware & software

Requirements below are documented for this workflow. Unspecified limits are not inferred. [Source 1](https://github.com/cofade/open-garden-planner/blob/master/README.md)

- **Hardware:** Maintainer measures about 611 MiB for the installed v1.29.6 app and advises at least 1 GiB plus download/temp/plan storage. Minimum RAM is explicitly unmeasured. 3D frame rate depends on graphics; software fallback exists.
- **Software:** Python 3.11+, PyQt6 for source builds. Optional plant databases require their own API access; AI use requires an MCP-capable agent.
- **Platforms:** Windows 10/11 64-bit installer. Source instructions also show Linux/Mac environment activation, but equivalent platform testing was not established.

### License, model weights & costs

The full software license was reviewed. Model weights, assets and services remain separate. [Source 1](https://github.com/cofade/open-garden-planner/blob/master/LICENSE) [Source 2](https://github.com/cofade/open-garden-planner/blob/master/README.md)

- **Code:** GPL-3.0
- **Weights:** GPL-3.0 software. External AI providers, plant databases and imported images retain their own terms and access requirements.
- **Commercial:** Software use follows GPL-3.0. GPL-3.0 software. External AI providers, plant databases and imported images retain their own terms and access requirements.
- **Cost:** Local compute plus any chosen external model or service; provider access and charges are separate.

### Why it merits attention

Included for the documented creative workflow. A complete guide and popularity do not establish output reliability. [Source 1](https://github.com/cofade/open-garden-planner/blob/master/README.md)

### Limitations

The current 3D workflow assumes flat ground. Unmeasured RAM limits and ongoing 3D development are disclosed; a precise drawing or plant trait record does not prove structural or growing suitability. [Source 1](https://github.com/cofade/open-garden-planner/blob/master/README.md)

### Get the tool

- [Repository](https://github.com/cofade/open-garden-planner)
- [Documentation](https://github.com/cofade/open-garden-planner/blob/master/README.md)

## ToneRelay for Lightroom Classic

Photography, restoration & color · AI color direction and palette-based media · Editing, captions & post-production

First full guide, completing an earlier screened library entry with installation, use and documented requirements. This is a review-depth improvement, not a verified new software release.

### Quality assessment: Quality unverified

Software licensing and a concrete creative AI use are supported. The remaining checks do not establish a recommendation.

Scope: Reference-guided color edits, subject/exposure adjustments and reviewed catalog selection tasks inside Lightroom Classic.

Evidence checked: 2026-10-22. No local execution implied.

- **Open-source software license · verified:** The complete root software license was read and archived. The grant covers this project code; unresolved model, service and asset terms are disclosed separately. [Source](https://github.com/ReefRuan/tonerelay-lightroom-mcp/blob/main/LICENSE)
- **Creative results · documented:** The README reproduces earlier Lightroom/agent editing captures and says they are historical workflow records, not newly repeated edits or speed/token benchmarks. The linked portal could not be opened in this pass; its current interactive availability is unverified. [Source](https://github.com/ReefRuan/tonerelay-lightroom-mcp/blob/main/README.md) [Source](https://github.com/ReefRuan/tonerelay-lightroom-mcp/blob/main/INSTALL.md) [Source](https://reefruan.github.io/tonerelay-portal/#experience)
- **Reproducible setup · documented:** Use a verified fixed source revision, Python 3.10+ and the platform bootstrap guide. Install the Lightroom plugin, start the bridge, restart Lightroom, then connect the MCP server and matching client skill. Independent reproduction has not been established in this review. [Source](https://github.com/ReefRuan/tonerelay-lightroom-mcp/blob/main/README.md) [Source](https://github.com/ReefRuan/tonerelay-lightroom-mcp/blob/main/INSTALL.md) [Source](https://reefruan.github.io/tonerelay-portal/#experience)
- **Maintenance and support · unknown:** A release or active repository alone does not establish sustained support. Workflow-specific support and unresolved blockers need a deeper review.
- **Independent use · unknown:** Independent first-hand use or a working third-party integration was not established for this selected workflow.
- **Models, services and costs · documented:** AGPL-3.0-only original code and runtime prompts. Adobe software, AI client/provider access and photos/reference images are separate; the software license does not grant Adobe access. Local compute plus any chosen external model or service; provider access and charges are separate. [Source](https://github.com/ReefRuan/tonerelay-lightroom-mcp/blob/main/README.md) [Source](https://github.com/ReefRuan/tonerelay-lightroom-mcp/blob/main/INSTALL.md) [Source](https://reefruan.github.io/tonerelay-portal/#experience)

Documentation review only; AI Media Scout did not install or run this software. Currently a source preview with no stable installer or completed all-platform acceptance. Catalog ratings/flags can modify the catalog; review scope and virtual-copy behavior. Platform installer features differ.

### How it uses AI

A local MCP bridge lets an AI agent inspect Lightroom Classic previews and adjust development settings through an iterative photo-editing conversation. [Source](https://github.com/ReefRuan/tonerelay-lightroom-mcp/blob/main/README.md) [Source](https://github.com/ReefRuan/tonerelay-lightroom-mcp/blob/main/INSTALL.md) [Source](https://reefruan.github.io/tonerelay-portal/#experience)

### Introduction

A local MCP bridge lets an AI agent inspect Lightroom Classic previews and adjust development settings through an iterative photo-editing conversation. [Source 1](https://github.com/ReefRuan/tonerelay-lightroom-mcp/blob/main/README.md) [Source 2](https://github.com/ReefRuan/tonerelay-lightroom-mcp/blob/main/INSTALL.md) [Source 3](https://reefruan.github.io/tonerelay-portal/#experience)

### What it is good for

Reference-guided color edits, subject/exposure adjustments and reviewed catalog selection tasks inside Lightroom Classic. [Source 1](https://github.com/ReefRuan/tonerelay-lightroom-mcp/blob/main/README.md) [Source 2](https://github.com/ReefRuan/tonerelay-lightroom-mcp/blob/main/INSTALL.md) [Source 3](https://reefruan.github.io/tonerelay-portal/#experience)

### Demo & examples

The README reproduces earlier Lightroom/agent editing captures and says they are historical workflow records, not newly repeated edits or speed/token benchmarks. The linked portal could not be opened in this pass; its current interactive availability is unverified. [Source 1](https://github.com/ReefRuan/tonerelay-lightroom-mcp/blob/main/README.md) [Source 2](https://github.com/ReefRuan/tonerelay-lightroom-mcp/blob/main/INSTALL.md) [Source 3](https://reefruan.github.io/tonerelay-portal/#experience)

### Install

Use a verified fixed source revision, Python 3.10+ and the platform bootstrap guide. Install the Lightroom plugin, start the bridge, restart Lightroom, then connect the MCP server and matching client skill. [Source 1](https://github.com/ReefRuan/tonerelay-lightroom-mcp/blob/main/README.md) [Source 2](https://github.com/ReefRuan/tonerelay-lightroom-mcp/blob/main/INSTALL.md) [Source 3](https://reefruan.github.io/tonerelay-portal/#experience)

1. Obtain the official source or release linked below.
2. Use a verified fixed source revision, Python 3.10+ and the platform bootstrap guide. Install the Lightroom plugin, start the bridge, restart Lightroom, then connect the MCP server and matching client skill.
### First project

Start with a short, representative project and inspect the result before a larger batch. [Source 1](https://github.com/ReefRuan/tonerelay-lightroom-mcp/blob/main/README.md) [Source 2](https://github.com/ReefRuan/tonerelay-lightroom-mcp/blob/main/INSTALL.md) [Source 3](https://reefruan.github.io/tonerelay-portal/#experience)

1. Open the intended Lightroom catalog and select a photograph.
2. Confirm the connection can read the selected image, then request a small edit on a virtual copy.
3. Inspect the actual Lightroom preview and continue adjusting before export.
### Hardware & software

Requirements below are documented for this workflow. Unspecified limits are not inferred. [Source 1](https://github.com/ReefRuan/tonerelay-lightroom-mcp/blob/main/README.md) [Source 2](https://github.com/ReefRuan/tonerelay-lightroom-mcp/blob/main/INSTALL.md) [Source 3](https://reefruan.github.io/tonerelay-portal/#experience)

- **Hardware:** Minimum system RAM, VRAM and total disk space are not documented in the reviewed instructions.
- **Software:** Adobe Lightroom Classic, Python 3.10+, a local MCP-capable AI client and the matching plugin/bridge components. TOML configuration checking needs Python 3.11+.
- **Platforms:** Separate macOS and Windows installers/instructions. Cloud Lightroom, Photoshop and Linux support are not claimed.

### License, model weights & costs

The full software license was reviewed. Model weights, assets and services remain separate. [Source 1](https://github.com/ReefRuan/tonerelay-lightroom-mcp/blob/main/LICENSE) [Source 2](https://github.com/ReefRuan/tonerelay-lightroom-mcp/blob/main/README.md) [Source 3](https://github.com/ReefRuan/tonerelay-lightroom-mcp/blob/main/INSTALL.md) [Source 4](https://reefruan.github.io/tonerelay-portal/#experience)

- **Code:** AGPL-3.0
- **Weights:** AGPL-3.0-only original code and runtime prompts. Adobe software, AI client/provider access and photos/reference images are separate; the software license does not grant Adobe access.
- **Commercial:** Software use follows AGPL-3.0. AGPL-3.0-only original code and runtime prompts. Adobe software, AI client/provider access and photos/reference images are separate; the software license does not grant Adobe access.
- **Cost:** Local compute plus any chosen external model or service; provider access and charges are separate.

### Why it merits attention

Included for the documented creative workflow. A complete guide and popularity do not establish output reliability. [Source 1](https://github.com/ReefRuan/tonerelay-lightroom-mcp/blob/main/README.md) [Source 2](https://github.com/ReefRuan/tonerelay-lightroom-mcp/blob/main/INSTALL.md) [Source 3](https://reefruan.github.io/tonerelay-portal/#experience)

### Limitations

Currently a source preview with no stable installer or completed all-platform acceptance. Catalog ratings/flags can modify the catalog; review scope and virtual-copy behavior. Platform installer features differ. [Source 1](https://github.com/ReefRuan/tonerelay-lightroom-mcp/blob/main/README.md) [Source 2](https://github.com/ReefRuan/tonerelay-lightroom-mcp/blob/main/INSTALL.md) [Source 3](https://reefruan.github.io/tonerelay-portal/#experience)

### Get the tool

- [Repository](https://github.com/ReefRuan/tonerelay-lightroom-mcp)
- [Documentation](https://github.com/ReefRuan/tonerelay-lightroom-mcp/blob/main/README.md)

## pix2pix Watercolor

Images & design · Neural brushstroke painting and drawn media · Computational art & creative coding

First full guide, completing an earlier screened library entry with installation, use and documented requirements. This is a review-depth improvement, not a verified new software release.

### Quality assessment: Quality unverified

Software licensing and a concrete creative AI use are supported. The remaining checks do not establish a recommendation.

Scope: Studying a learned sketch-to-watercolor style on a small, controlled paired image collection.

Evidence checked: 2026-10-22. No local execution implied.

- **Open-source software license · verified:** The complete root software license was read and archived. The grant covers this project code; unresolved model, service and asset terms are disclosed separately. [Source](https://github.com/yingzwang/pix2pix-watercolor/blob/master/LICENSE.txt)
- **Creative results · documented:** The README provides example watercolor outputs and training imagery; generalization beyond those samples is unverified. [Source](https://github.com/yingzwang/pix2pix-watercolor/blob/master/README.md) [Source](https://github.com/yingzwang/pix2pix-watercolor/blob/master/pix2pix.py)
- **Reproducible setup · documented:** Recreate the documented legacy TensorFlow 1.9 environment, preferably the author’s Linux GPU/cuDNN route, prepare paired data and use pix2pix.py training/test modes. Independent reproduction has not been established in this review. [Source](https://github.com/yingzwang/pix2pix-watercolor/blob/master/README.md) [Source](https://github.com/yingzwang/pix2pix-watercolor/blob/master/pix2pix.py)
- **Maintenance and support · unknown:** A release or active repository alone does not establish sustained support. Workflow-specific support and unresolved blockers need a deeper review.
- **Independent use · unknown:** Independent first-hand use or a working third-party integration was not established for this selected workflow.
- **Models, services and costs · documented:** MIT code. Training artwork and any checkpoints retain separate rights; a reusable pre-trained model license was not established. Local compute plus any chosen external model or service; provider access and charges are separate. [Source](https://github.com/yingzwang/pix2pix-watercolor/blob/master/README.md) [Source](https://github.com/yingzwang/pix2pix-watercolor/blob/master/pix2pix.py)

Documentation review only; AI Media Scout did not install or run this software. This is a training-oriented legacy workflow, not a current packaged painting app. Very small training sets and author examples do not demonstrate broad stylistic generalization.

### How it uses AI

A modified pix2pix neural image-translation project learns to turn paired pencil sketches into watercolor-like images. [Source](https://github.com/yingzwang/pix2pix-watercolor/blob/master/README.md) [Source](https://github.com/yingzwang/pix2pix-watercolor/blob/master/pix2pix.py)

### Introduction

A modified pix2pix neural image-translation project learns to turn paired pencil sketches into watercolor-like images. [Source 1](https://github.com/yingzwang/pix2pix-watercolor/blob/master/README.md) [Source 2](https://github.com/yingzwang/pix2pix-watercolor/blob/master/pix2pix.py)

### What it is good for

Studying a learned sketch-to-watercolor style on a small, controlled paired image collection. [Source 1](https://github.com/yingzwang/pix2pix-watercolor/blob/master/README.md) [Source 2](https://github.com/yingzwang/pix2pix-watercolor/blob/master/pix2pix.py)

### Demo & examples

The README provides example watercolor outputs and training imagery; generalization beyond those samples is unverified. [Source 1](https://github.com/yingzwang/pix2pix-watercolor/blob/master/README.md) [Source 2](https://github.com/yingzwang/pix2pix-watercolor/blob/master/pix2pix.py)

### Install

Recreate the documented legacy TensorFlow 1.9 environment, preferably the author’s Linux GPU/cuDNN route, prepare paired data and use pix2pix.py training/test modes. [Source 1](https://github.com/yingzwang/pix2pix-watercolor/blob/master/README.md) [Source 2](https://github.com/yingzwang/pix2pix-watercolor/blob/master/pix2pix.py)

1. Obtain the official source or release linked below.
2. Recreate the documented legacy TensorFlow 1.9 environment, preferably the author’s Linux GPU/cuDNN route, prepare paired data and use pix2pix.py training/test modes.

```sh
python pix2pix.py --mode train --max_epochs 2 --display_freq 1 --output_dir results/v/train --input_dir photos
```

### First project

Start with a short, representative project and inspect the result before a larger batch. [Source 1](https://github.com/yingzwang/pix2pix-watercolor/blob/master/README.md) [Source 2](https://github.com/yingzwang/pix2pix-watercolor/blob/master/pix2pix.py)

1. Prepare aligned sketch/watercolor pairs in the expected input layout.
2. Train a small experiment and inspect saved sample images.
3. Use the checkpoint with test/export mode and compare unseen sketches before expanding the dataset.
### Hardware & software

Requirements below are documented for this workflow. Unspecified limits are not inferred. [Source 1](https://github.com/yingzwang/pix2pix-watercolor/blob/master/README.md) [Source 2](https://github.com/yingzwang/pix2pix-watercolor/blob/master/pix2pix.py)

- **Hardware:** Minimum system RAM, VRAM and total disk space are not documented in the reviewed instructions.
- **Software:** Legacy TensorFlow 1.9, NumPy and project scripts; GPU/cuDNN recommended in the README. Current Python/CUDA compatibility is not established.
- **Platforms:** Linux GPU workflow recommended by the author; other platforms and contemporary environments are not verified.

### License, model weights & costs

The full software license was reviewed. Model weights, assets and services remain separate. [Source 1](https://github.com/yingzwang/pix2pix-watercolor/blob/master/LICENSE.txt) [Source 2](https://github.com/yingzwang/pix2pix-watercolor/blob/master/README.md) [Source 3](https://github.com/yingzwang/pix2pix-watercolor/blob/master/pix2pix.py)

- **Code:** MIT
- **Weights:** MIT code. Training artwork and any checkpoints retain separate rights; a reusable pre-trained model license was not established.
- **Commercial:** Software use follows MIT. MIT code. Training artwork and any checkpoints retain separate rights; a reusable pre-trained model license was not established.
- **Cost:** Local compute plus any chosen external model or service; provider access and charges are separate.

### Why it merits attention

Included for the documented creative workflow. A complete guide and popularity do not establish output reliability. [Source 1](https://github.com/yingzwang/pix2pix-watercolor/blob/master/README.md) [Source 2](https://github.com/yingzwang/pix2pix-watercolor/blob/master/pix2pix.py)

### Limitations

This is a training-oriented legacy workflow, not a current packaged painting app. Very small training sets and author examples do not demonstrate broad stylistic generalization. [Source 1](https://github.com/yingzwang/pix2pix-watercolor/blob/master/README.md) [Source 2](https://github.com/yingzwang/pix2pix-watercolor/blob/master/pix2pix.py)

### Get the tool

- [Repository](https://github.com/yingzwang/pix2pix-watercolor)
- [Documentation](https://github.com/yingzwang/pix2pix-watercolor/blob/master/README.md)

## Albedolizer

Neural procedural material authoring · Images & design · 3D, reconstruction & assets · Neural relighting and material recovery

First full guide in this library, establishing a documentation baseline; not a claim of a launch or significant update today.

### Quality assessment: Quality unverified

Software licensing and a concrete creative AI use are supported. The remaining checks do not establish a recommendation.

Scope: Preparing albedo variations and rough texture-map drafts for a game or visualization material.

Evidence checked: 2026-10-22. No local execution implied.

- **Open-source software license · verified:** The complete root software license was read and archived. The grant covers this project code; unresolved model, service and asset terms are disclosed separately. [Source](https://github.com/invisiblelevel/Albedolizer/blob/main/LICENSE)
- **Creative results · documented:** The README documents before/after textures, map generation and a material preview. Procedural maps are not measured physical-material recovery. [Source](https://github.com/invisiblelevel/Albedolizer/blob/main/README.md) [Source](https://github.com/invisiblelevel/Albedolizer/blob/main/THIRD_PARTY_NOTICES.md)
- **Reproducible setup · documented:** Use the official Windows installer, or create the documented Python 3.10 source environment, install requirements and launch main.py. Independent reproduction has not been established in this review. [Source](https://github.com/invisiblelevel/Albedolizer/blob/main/README.md) [Source](https://github.com/invisiblelevel/Albedolizer/blob/main/THIRD_PARTY_NOTICES.md)
- **Maintenance and support · unknown:** A release or active repository alone does not establish sustained support. Workflow-specific support and unresolved blockers need a deeper review.
- **Independent use · unknown:** Independent first-hand use or a working third-party integration was not established for this selected workflow.
- **Models, services and costs · documented:** MIT main project; LUTwithBGrid is separately Apache-2.0. The README attributes a seamless-texture algorithm to GPL GIMP code, so redistribution needs component-level review; the root MIT label is not a complete grant for every component. Local compute plus any chosen external model or service; provider access and charges are separate. [Source](https://github.com/invisiblelevel/Albedolizer/blob/main/README.md) [Source](https://github.com/invisiblelevel/Albedolizer/blob/main/THIRD_PARTY_NOTICES.md)

Documentation review only; AI Media Scout did not install or run this software. Sobel-derived and other procedural maps do not recover true material properties. Component licensing, independent quality and source-build portability need further review.

### How it uses AI

A desktop texture utility combines learned color correction through an ONNX LUT model with material presets and procedural PBR-map generation. [Source](https://github.com/invisiblelevel/Albedolizer/blob/main/README.md) [Source](https://github.com/invisiblelevel/Albedolizer/blob/main/THIRD_PARTY_NOTICES.md)

### Introduction

A desktop texture utility combines learned color correction through an ONNX LUT model with material presets and procedural PBR-map generation. [Source 1](https://github.com/invisiblelevel/Albedolizer/blob/main/README.md) [Source 2](https://github.com/invisiblelevel/Albedolizer/blob/main/THIRD_PARTY_NOTICES.md)

### What it is good for

Preparing albedo variations and rough texture-map drafts for a game or visualization material. [Source 1](https://github.com/invisiblelevel/Albedolizer/blob/main/README.md) [Source 2](https://github.com/invisiblelevel/Albedolizer/blob/main/THIRD_PARTY_NOTICES.md)

### Demo & examples

The README documents before/after textures, map generation and a material preview. Procedural maps are not measured physical-material recovery. [Source 1](https://github.com/invisiblelevel/Albedolizer/blob/main/README.md) [Source 2](https://github.com/invisiblelevel/Albedolizer/blob/main/THIRD_PARTY_NOTICES.md)

### Install

Use the official Windows installer, or create the documented Python 3.10 source environment, install requirements and launch main.py. [Source 1](https://github.com/invisiblelevel/Albedolizer/blob/main/README.md) [Source 2](https://github.com/invisiblelevel/Albedolizer/blob/main/THIRD_PARTY_NOTICES.md)

1. Obtain the official source or release linked below.
2. Use the official Windows installer, or create the documented Python 3.10 source environment, install requirements and launch main.py.

```sh
pip install -r requirements.txt
```


```sh
python main.py
```

### First project

Start with a short, representative project and inspect the result before a larger batch. [Source 1](https://github.com/invisiblelevel/Albedolizer/blob/main/README.md) [Source 2](https://github.com/invisiblelevel/Albedolizer/blob/main/THIRD_PARTY_NOTICES.md)

1. Load an albedo image and select a material preset.
2. Inspect an automatic correction against the source image.
3. Generate preview maps in the PBR tab and export the needed engine pack, then validate it in the target renderer.
### Hardware & software

Requirements below are documented for this workflow. Unspecified limits are not inferred. [Source 1](https://github.com/invisiblelevel/Albedolizer/blob/main/README.md) [Source 2](https://github.com/invisiblelevel/Albedolizer/blob/main/THIRD_PARTY_NOTICES.md)

- **Hardware:** README: 16 GB RAM minimum/32 GB recommended, four CPU cores minimum/eight recommended, 2 GB disk minimum/5+ GB SSD recommended. Dedicated GPU not required; NVIDIA recommended for viewer workloads. 8K batches may need 32 GB RAM.
- **Software:** Windows release, or Python 3.10 source environment with ONNX runtime and project dependencies.
- **Platforms:** Windows 10 x64 minimum and Windows 11 recommended. Source portability to other systems was not established.

### License, model weights & costs

The full software license was reviewed. Model weights, assets and services remain separate. [Source 1](https://github.com/invisiblelevel/Albedolizer/blob/main/LICENSE) [Source 2](https://github.com/invisiblelevel/Albedolizer/blob/main/README.md) [Source 3](https://github.com/invisiblelevel/Albedolizer/blob/main/THIRD_PARTY_NOTICES.md)

- **Code:** MIT
- **Weights:** MIT main project; LUTwithBGrid is separately Apache-2.0. The README attributes a seamless-texture algorithm to GPL GIMP code, so redistribution needs component-level review; the root MIT label is not a complete grant for every component.
- **Commercial:** Software use follows MIT. MIT main project; LUTwithBGrid is separately Apache-2.0. The README attributes a seamless-texture algorithm to GPL GIMP code, so redistribution needs component-level review; the root MIT label is not a complete grant for every component.
- **Cost:** Local compute plus any chosen external model or service; provider access and charges are separate.

### Why it merits attention

Included for the documented creative workflow. A complete guide and popularity do not establish output reliability. [Source 1](https://github.com/invisiblelevel/Albedolizer/blob/main/README.md) [Source 2](https://github.com/invisiblelevel/Albedolizer/blob/main/THIRD_PARTY_NOTICES.md)

### Limitations

Sobel-derived and other procedural maps do not recover true material properties. Component licensing, independent quality and source-build portability need further review. [Source 1](https://github.com/invisiblelevel/Albedolizer/blob/main/README.md) [Source 2](https://github.com/invisiblelevel/Albedolizer/blob/main/THIRD_PARTY_NOTICES.md)

### Get the tool

- [Repository](https://github.com/invisiblelevel/Albedolizer)
- [Documentation](https://github.com/invisiblelevel/Albedolizer/blob/main/README.md)

## Fabricator

3D printing & generative CAD · AI parametric design and jewelry · 3D, reconstruction & assets

First full guide, completing an earlier screened library entry with installation, use and documented requirements. This is a review-depth improvement, not a verified new software release.

### Quality assessment: Quality unverified

Software licensing and a concrete creative AI use are supported. The remaining checks do not establish a recommendation.

Scope: Designing small functional objects iteratively with a coding agent, including split parts and fit adjustments.

Evidence checked: 2026-10-22. No local execution implied.

- **Open-source software license · verified:** The complete root software license was read and archived. The grant covers this project code; unresolved model, service and asset terms are disclosed separately. [Source](https://github.com/Amuniare/ai-fabricator/blob/main/LICENSE)
- **Creative results · documented:** Four documented example designs include brackets, a battery holder, a split shelf and a drill-bit box, with rendered previews. Their real-world strength and fit were not independently checked. [Source](https://github.com/Amuniare/ai-fabricator/blob/main/README.md)
- **Reproducible setup · documented:** On Windows 11, install Bambu Studio and obtain the official repository. Follow setup.bat instructions to provision the supported tools, then open the Fabricator desktop shortcut and sign into Claude. Independent reproduction has not been established in this review. [Source](https://github.com/Amuniare/ai-fabricator/blob/main/README.md)
- **Maintenance and support · unknown:** A release or active repository alone does not establish sustained support. Workflow-specific support and unresolved blockers need a deeper review.
- **Independent use · unknown:** Independent first-hand use or a working third-party integration was not established for this selected workflow.
- **Models, services and costs · documented:** MIT project code. Claude subscription/service and Bambu host/printer tooling are separate; design/source asset rights remain the creator’s responsibility. Claude subscription, local compute, printer/filament and any host costs; no current price is inferred. [Source](https://github.com/Amuniare/ai-fabricator/blob/main/README.md)

Documentation review only; AI Media Scout did not install or run this software. Automated design/slicing checks and pictures do not establish mechanical safety, tolerances or print success. The documented route requires commercial AI access and specific printer tooling.

### How it uses AI

An AI-assisted build123d workflow turns an object description into editable CAD, rendered previews and Bambu Studio slicing outputs. [Source](https://github.com/Amuniare/ai-fabricator/blob/main/README.md)

### Introduction

An AI-assisted build123d workflow turns an object description into editable CAD, rendered previews and Bambu Studio slicing outputs. [Source 1](https://github.com/Amuniare/ai-fabricator/blob/main/README.md)

### What it is good for

Designing small functional objects iteratively with a coding agent, including split parts and fit adjustments. [Source 1](https://github.com/Amuniare/ai-fabricator/blob/main/README.md)

### Demo & examples

Four documented example designs include brackets, a battery holder, a split shelf and a drill-bit box, with rendered previews. Their real-world strength and fit were not independently checked. [Source 1](https://github.com/Amuniare/ai-fabricator/blob/main/README.md)

### Install

On Windows 11, install Bambu Studio and obtain the official repository. Follow setup.bat instructions to provision the supported tools, then open the Fabricator desktop shortcut and sign into Claude. [Source 1](https://github.com/Amuniare/ai-fabricator/blob/main/README.md)

1. Obtain the official source or release linked below.
2. On Windows 11, install Bambu Studio and obtain the official repository. Follow setup.bat instructions to provision the supported tools, then open the Fabricator desktop shortcut and sign into Claude.

```sh
uv run fabricator doctor
```

### First project

Start with a short, representative project and inspect the result before a larger batch. [Source 1](https://github.com/Amuniare/ai-fabricator/blob/main/README.md)

1. Describe a small object with dimensions and printer constraints.
2. Review the multi-angle design previews and requested changes.
3. Inspect the generated parts and slicing estimates in Bambu Studio; validate a small fit test before a larger functional print.
### Hardware & software

Requirements below are documented for this workflow. Unspecified limits are not inferred. [Source 1](https://github.com/Amuniare/ai-fabricator/blob/main/README.md)

- **Hardware:** Bambu Lab printer for the documented output workflow, tested on A1 mini. PC RAM, GPU and disk minima are not documented.
- **Software:** Windows 11, Bambu Studio, Python tools/build123d and VS Code with Claude. The bootstrap installs supporting developer tools.
- **Platforms:** Windows 11; the maintainer reports testing with a Bambu A1 mini. Other printers/platforms are not established.

### License, model weights & costs

The full software license was reviewed. Model weights, assets and services remain separate. [Source 1](https://github.com/Amuniare/ai-fabricator/blob/main/LICENSE) [Source 2](https://github.com/Amuniare/ai-fabricator/blob/main/README.md)

- **Code:** MIT
- **Weights:** MIT project code. Claude subscription/service and Bambu host/printer tooling are separate; design/source asset rights remain the creator’s responsibility.
- **Commercial:** Software use follows MIT. MIT project code. Claude subscription/service and Bambu host/printer tooling are separate; design/source asset rights remain the creator’s responsibility.
- **Cost:** Claude subscription, local compute, printer/filament and any host costs; no current price is inferred.

### Why it merits attention

Included for the documented creative workflow. A complete guide and popularity do not establish output reliability. [Source 1](https://github.com/Amuniare/ai-fabricator/blob/main/README.md)

### Limitations

Automated design/slicing checks and pictures do not establish mechanical safety, tolerances or print success. The documented route requires commercial AI access and specific printer tooling. [Source 1](https://github.com/Amuniare/ai-fabricator/blob/main/README.md)

### Get the tool

- [Repository](https://github.com/Amuniare/ai-fabricator)
- [Documentation](https://github.com/Amuniare/ai-fabricator/blob/main/README.md)

## Bar Nine

Audio, music & voice · Creative learning & authoring · Editing, captions & post-production

First full guide in this library. The repository was created 2026-10-12, within the discovery window; that date does not establish a product launch or output quality.

### Quality assessment: Experimental

Software licensing and a concrete creative AI use are supported. The remaining checks do not establish a recommendation.

Scope: Learning from track/device/MIDI structure and making small reviewed arrangement or mixer edits in Ableton.

Evidence checked: 2026-10-22. No local execution implied.

Why Experimental: The current README labels the Mac application early, warns of rough edges and says the first tester build is still pending. https://github.com/barnine/barnine/blob/main/README.md

- **Open-source software license · verified:** The complete root software license was read and archived. The grant covers this project code; unresolved model, service and asset terms are disclosed separately. [Source](https://github.com/barnine/barnine/blob/main/LICENSE)
- **Creative results · documented:** The README shows a shortened settings-based session and before/after parameter changes; it explicitly states that the assistant cannot hear the track. [Source](https://github.com/barnine/barnine/blob/main/README.md)
- **Reproducible setup · documented:** On macOS with Ableton Live 12.4+, install Node.js 22.18+ and pnpm, obtain the source, start the Mac app, configure an Anthropic API key and pair its remote script with Live. Independent reproduction has not been established in this review. [Source](https://github.com/barnine/barnine/blob/main/README.md)
- **Maintenance and support · unknown:** A release or active repository alone does not establish sustained support. Workflow-specific support and unresolved blockers need a deeper review.
- **Independent use · unknown:** Independent first-hand use or a working third-party integration was not established for this selected workflow.
- **Models, services and costs · documented:** MIT integration code. Ableton, third-party plug-ins, samples and Anthropic services have separate terms and costs. Local compute plus any chosen external model or service; provider access and charges are separate. [Source](https://github.com/barnine/barnine/blob/main/README.md)

Documentation review only; AI Media Scout did not install or run this software. The assistant currently reasons from settings rather than listening. Automation, freezing and clip splitting are not supported; the first tester build and additional app features are still pending.

### How it uses AI

An AI production mentor reads and edits an Ableton Live Set through a desktop integration, explaining musical settings and changes. [Source](https://github.com/barnine/barnine/blob/main/README.md)

### Introduction

An AI production mentor reads and edits an Ableton Live Set through a desktop integration, explaining musical settings and changes. [Source 1](https://github.com/barnine/barnine/blob/main/README.md)

### What it is good for

Learning from track/device/MIDI structure and making small reviewed arrangement or mixer edits in Ableton. [Source 1](https://github.com/barnine/barnine/blob/main/README.md)

### Demo & examples

The README shows a shortened settings-based session and before/after parameter changes; it explicitly states that the assistant cannot hear the track. [Source 1](https://github.com/barnine/barnine/blob/main/README.md)

### Install

On macOS with Ableton Live 12.4+, install Node.js 22.18+ and pnpm, obtain the source, start the Mac app, configure an Anthropic API key and pair its remote script with Live. [Source 1](https://github.com/barnine/barnine/blob/main/README.md)

1. Obtain the official source or release linked below.
2. On macOS with Ableton Live 12.4+, install Node.js 22.18+ and pnpm, obtain the source, start the Mac app, configure an Anthropic API key and pair its remote script with Live.

```sh
pnpm install
```


```sh
pnpm --filter @mentor/mac start
```

### First project

Start with a short, representative project and inspect the result before a larger batch. [Source 1](https://github.com/barnine/barnine/blob/main/README.md)

1. Pair the app, restart Live and choose Bar Nine as a control surface.
2. Open a copied Live Set and ask about a small track or device issue.
3. Review a proposed parameter change and listen to the result yourself.
### Hardware & software

Requirements below are documented for this workflow. Unspecified limits are not inferred. [Source 1](https://github.com/barnine/barnine/blob/main/README.md)

- **Hardware:** Minimum system RAM, VRAM and total disk space are not documented in the reviewed instructions.
- **Software:** Ableton Live 12.4+, macOS, Node.js 22.18+, pnpm and Anthropic API access.
- **Platforms:** macOS only in the current documented implementation; Windows support is explicitly absent.

### License, model weights & costs

The full software license was reviewed. Model weights, assets and services remain separate. [Source 1](https://github.com/barnine/barnine/blob/main/LICENSE) [Source 2](https://github.com/barnine/barnine/blob/main/README.md)

- **Code:** MIT
- **Weights:** MIT integration code. Ableton, third-party plug-ins, samples and Anthropic services have separate terms and costs.
- **Commercial:** Software use follows MIT. MIT integration code. Ableton, third-party plug-ins, samples and Anthropic services have separate terms and costs.
- **Cost:** Local compute plus any chosen external model or service; provider access and charges are separate.

### Why it merits attention

Included for the documented creative workflow. A complete guide and popularity do not establish output reliability. [Source 1](https://github.com/barnine/barnine/blob/main/README.md)

### Limitations

The assistant currently reasons from settings rather than listening. Automation, freezing and clip splitting are not supported; the first tester build and additional app features are still pending. [Source 1](https://github.com/barnine/barnine/blob/main/README.md)

### Get the tool

- [Repository](https://github.com/barnine/barnine)
- [Documentation](https://github.com/barnine/barnine/blob/main/README.md)

## HVFT VISION

Performance, projection & stage media · Interactive, immersive & live media · Physical, robotic & kinetic installations · Video, animation & film

First full guide, completing an earlier screened library entry with installation, use and documented requirements. This is a review-depth improvement, not a verified new software release.

### Quality assessment: Quality unverified

Software licensing and a concrete creative AI use are supported. The remaining checks do not establish a recommendation.

Scope: Harsh-noise performance visuals, camera/depth composites and mapped multi-channel projector output.

Evidence checked: 2026-10-22. No local execution implied.

- **Open-source software license · verified:** The complete root software license was read and archived. The grant covers this project code; unresolved model, service and asset terms are disclosed separately. [Source](https://github.com/Rezjadwi/hvft-vision/blob/main/LICENSE)
- **Creative results · documented:** The maintainer shows control-window and kinetic-text screenshots and describes use in their own performance practice. Independent live-show reliability was not verified. [Source](https://github.com/Rezjadwi/hvft-vision/blob/main/README.md) [Source](https://github.com/rezjadwi/hvft-vision/blob/main/THIRD_PARTY_NOTICES.md)
- **Reproducible setup · documented:** On an Apple Silicon Mac with Node.js 20+, obtain the source, install npm dependencies and start the app. Optional local AI GEN needs Python 3.11+ and its documented PyTorch/diffusers environment. Independent reproduction has not been established in this review. [Source](https://github.com/Rezjadwi/hvft-vision/blob/main/README.md) [Source](https://github.com/rezjadwi/hvft-vision/blob/main/THIRD_PARTY_NOTICES.md)
- **Maintenance and support · unknown:** A release or active repository alone does not establish sustained support. Workflow-specific support and unresolved blockers need a deeper review.
- **Independent use · unknown:** Independent first-hand use or a working third-party integration was not established for this selected workflow.
- **Models, services and costs · documented:** GPL-3.0 app; third-party matting, depth and shader components retain their terms. Local SD-Turbo is explicitly noncommercial under the notice; Gemini is a separate cloud service. Some bundled fonts/assets are personal-use-only and need replacement or clearance for redistribution. Local compute plus any chosen external model or service; provider access and charges are separate. [Source](https://github.com/Rezjadwi/hvft-vision/blob/main/README.md) [Source](https://github.com/rezjadwi/hvft-vision/blob/main/THIRD_PARTY_NOTICES.md)

Documentation review only; AI Media Scout did not install or run this software. Source-stage application with planned packaged release. Projector stability and latency are not independently tested. The app’s source license does not clear every bundled visual asset or optional model.

### How it uses AI

A live visual mixer combines learned person matting, monocular depth and optional diffusion restyling with sound-texture-reactive projection effects. [Source](https://github.com/Rezjadwi/hvft-vision/blob/main/README.md) [Source](https://github.com/rezjadwi/hvft-vision/blob/main/THIRD_PARTY_NOTICES.md)

### Introduction

A live visual mixer combines learned person matting, monocular depth and optional diffusion restyling with sound-texture-reactive projection effects. [Source 1](https://github.com/Rezjadwi/hvft-vision/blob/main/README.md) [Source 2](https://github.com/rezjadwi/hvft-vision/blob/main/THIRD_PARTY_NOTICES.md)

### What it is good for

Harsh-noise performance visuals, camera/depth composites and mapped multi-channel projector output. [Source 1](https://github.com/Rezjadwi/hvft-vision/blob/main/README.md) [Source 2](https://github.com/rezjadwi/hvft-vision/blob/main/THIRD_PARTY_NOTICES.md)

### Demo & examples

The maintainer shows control-window and kinetic-text screenshots and describes use in their own performance practice. Independent live-show reliability was not verified. [Source 1](https://github.com/Rezjadwi/hvft-vision/blob/main/README.md) [Source 2](https://github.com/rezjadwi/hvft-vision/blob/main/THIRD_PARTY_NOTICES.md)

### Install

On an Apple Silicon Mac with Node.js 20+, obtain the source, install npm dependencies and start the app. Optional local AI GEN needs Python 3.11+ and its documented PyTorch/diffusers environment. [Source 1](https://github.com/Rezjadwi/hvft-vision/blob/main/README.md) [Source 2](https://github.com/rezjadwi/hvft-vision/blob/main/THIRD_PARTY_NOTICES.md)

1. Obtain the official source or release linked below.
2. On an Apple Silicon Mac with Node.js 20+, obtain the source, install npm dependencies and start the app. Optional local AI GEN needs Python 3.11+ and its documented PyTorch/diffusers environment.

```sh
npm install
```


```sh
npm start
```

### First project

Start with a short, representative project and inspect the result before a larger batch. [Source 1](https://github.com/Rezjadwi/hvft-vision/blob/main/README.md) [Source 2](https://github.com/rezjadwi/hvft-vision/blob/main/THIRD_PARTY_NOTICES.md)

1. Allow camera and microphone access and select an audio input.
2. Enable a camera/depth channel and adjust the sound-reactivity level.
3. Open projector output, fit the four mapping corners and save a preset after testing the display.
### Hardware & software

Requirements below are documented for this workflow. Unspecified limits are not inferred. [Source 1](https://github.com/Rezjadwi/hvft-vision/blob/main/README.md) [Source 2](https://github.com/rezjadwi/hvft-vision/blob/main/THIRD_PARTY_NOTICES.md)

- **Hardware:** Developed on an M1 Mac with 16 GB RAM, an example configuration rather than a tested minimum. Optional local model download is about 2.6 GB; projector/audio/camera hardware depends on the performance.
- **Software:** macOS Apple Silicon, Node.js 20+; optional Python 3.11+, PyTorch MPS and diffusers for local SD-Turbo. Kinect, Android camera, MIDI and Syphon are optional paths.
- **Platforms:** macOS Apple Silicon. A downloadable DMG is planned; the current documented installation is from source.

### License, model weights & costs

The full software license was reviewed. Model weights, assets and services remain separate. [Source 1](https://github.com/Rezjadwi/hvft-vision/blob/main/LICENSE) [Source 2](https://github.com/Rezjadwi/hvft-vision/blob/main/README.md) [Source 3](https://github.com/rezjadwi/hvft-vision/blob/main/THIRD_PARTY_NOTICES.md)

- **Code:** GPL-3.0
- **Weights:** GPL-3.0 app; third-party matting, depth and shader components retain their terms. Local SD-Turbo is explicitly noncommercial under the notice; Gemini is a separate cloud service. Some bundled fonts/assets are personal-use-only and need replacement or clearance for redistribution.
- **Commercial:** Software use follows GPL-3.0. GPL-3.0 app; third-party matting, depth and shader components retain their terms. Local SD-Turbo is explicitly noncommercial under the notice; Gemini is a separate cloud service. Some bundled fonts/assets are personal-use-only and need replacement or clearance for redistribution.
- **Cost:** Local compute plus any chosen external model or service; provider access and charges are separate.

### Why it merits attention

Included for the documented creative workflow. A complete guide and popularity do not establish output reliability. [Source 1](https://github.com/Rezjadwi/hvft-vision/blob/main/README.md) [Source 2](https://github.com/rezjadwi/hvft-vision/blob/main/THIRD_PARTY_NOTICES.md)

### Limitations

Source-stage application with planned packaged release. Projector stability and latency are not independently tested. The app’s source license does not clear every bundled visual asset or optional model. [Source 1](https://github.com/Rezjadwi/hvft-vision/blob/main/README.md) [Source 2](https://github.com/rezjadwi/hvft-vision/blob/main/THIRD_PARTY_NOTICES.md)

### Get the tool

- [Repository](https://github.com/Rezjadwi/hvft-vision)
- [Documentation](https://github.com/Rezjadwi/hvft-vision/blob/main/README.md)

## Nomi

Video, animation & film · Storyboarding, narrative & comics · 3D, reconstruction & assets · AI agents for code-authored media production

First full guide in this library, establishing a documentation baseline; not a claim of a launch or significant update today.

### Quality assessment: Quality unverified

Software licensing and a concrete creative AI use are supported. The remaining checks do not establish a recommendation.

Scope: Keeping character references, shot prompts, generated takes and final edits together across different model providers.

Evidence checked: 2026-10-22. No local execution implied.

- **Open-source software license · verified:** The complete root software license was read and archived. The grant covers this project code; unresolved model, service and asset terms are disclosed separately. [Source](https://github.com/aqm857886159/Nomi/blob/main/LICENSE)
- **Creative results · documented:** The README links a 90-second film of the interface and generated media. It is a maintainer demonstration, not independent evidence of consistent identity or shot control. [Source](https://github.com/aqm857886159/Nomi/blob/main/README.md) [Source](https://nomiaqm.com/en/quickstart)
- **Reproducible setup · documented:** Download the matching official macOS or Windows release, create a local project and connect a chosen model provider or local ComfyUI. Source development needs Node.js 20+ and pnpm. Independent reproduction has not been established in this review. [Source](https://github.com/aqm857886159/Nomi/blob/main/README.md) [Source](https://nomiaqm.com/en/quickstart)
- **Maintenance and support · unknown:** A release or active repository alone does not establish sustained support. Workflow-specific support and unresolved blockers need a deeper review.
- **Independent use · unknown:** Independent first-hand use or a working third-party integration was not established for this selected workflow.
- **Models, services and costs · documented:** AGPL-3.0-only current source; historical Apache releases retain their terms. Connected models, relays, ComfyUI weights and commercial AI services are separate. Local compute plus any chosen external model or service; provider access and charges are separate. [Source](https://github.com/aqm857886159/Nomi/blob/main/README.md) [Source](https://nomiaqm.com/en/quickstart)

Documentation review only; AI Media Scout did not install or run this software. Local project storage does not make API inference local. Installers currently lack platform signing/notarization. Minimum RAM/VRAM is not documented and local model requirements are separate; AI editing remains on the roadmap.

### How it uses AI

A local-first video studio connects an AI planning agent to storyboards, image/video generation providers and an editable timeline. [Source](https://github.com/aqm857886159/Nomi/blob/main/README.md) [Source](https://nomiaqm.com/en/quickstart)

### Introduction

A local-first video studio connects an AI planning agent to storyboards, image/video generation providers and an editable timeline. [Source 1](https://github.com/aqm857886159/Nomi/blob/main/README.md) [Source 2](https://nomiaqm.com/en/quickstart)

### What it is good for

Keeping character references, shot prompts, generated takes and final edits together across different model providers. [Source 1](https://github.com/aqm857886159/Nomi/blob/main/README.md) [Source 2](https://nomiaqm.com/en/quickstart)

### Demo & examples

The README links a 90-second film of the interface and generated media. It is a maintainer demonstration, not independent evidence of consistent identity or shot control. [Source 1](https://github.com/aqm857886159/Nomi/blob/main/README.md) [Source 2](https://nomiaqm.com/en/quickstart)

### Install

Download the matching official macOS or Windows release, create a local project and connect a chosen model provider or local ComfyUI. Source development needs Node.js 20+ and pnpm. [Source 1](https://github.com/aqm857886159/Nomi/blob/main/README.md) [Source 2](https://nomiaqm.com/en/quickstart)

1. Obtain the official source or release linked below.
2. Download the matching official macOS or Windows release, create a local project and connect a chosen model provider or local ComfyUI. Source development needs Node.js 20+ and pnpm.
### First project

Start with a short, representative project and inspect the result before a larger batch. [Source 1](https://github.com/aqm857886159/Nomi/blob/main/README.md) [Source 2](https://nomiaqm.com/en/quickstart)

1. Connect one model route and inspect its terms and cost.
2. Describe a short sequence, review the storyboard and generate a small number of takes.
3. Arrange accepted takes on the timeline and export MP4.
### Hardware & software

Requirements below are documented for this workflow. Unspecified limits are not inferred. [Source 1](https://github.com/aqm857886159/Nomi/blob/main/README.md) [Source 2](https://nomiaqm.com/en/quickstart)

- **Hardware:** Minimum system RAM, VRAM and total disk space are not documented in the reviewed instructions.
- **Software:** Packaged desktop app; source builds use Node.js 20+ and pnpm. Generation requires external APIs or a separately configured local ComfyUI runtime.
- **Platforms:** macOS Apple Silicon/Intel and Windows 10/11 x64 installers. Linux, Windows ARM and a universal Mac installer are not currently published.

### License, model weights & costs

The full software license was reviewed. Model weights, assets and services remain separate. [Source 1](https://github.com/aqm857886159/Nomi/blob/main/LICENSE) [Source 2](https://github.com/aqm857886159/Nomi/blob/main/README.md) [Source 3](https://nomiaqm.com/en/quickstart)

- **Code:** AGPL-3.0
- **Weights:** AGPL-3.0-only current source; historical Apache releases retain their terms. Connected models, relays, ComfyUI weights and commercial AI services are separate.
- **Commercial:** Software use follows AGPL-3.0. AGPL-3.0-only current source; historical Apache releases retain their terms. Connected models, relays, ComfyUI weights and commercial AI services are separate.
- **Cost:** Local compute plus any chosen external model or service; provider access and charges are separate.

### Why it merits attention

Included for the documented creative workflow. A complete guide and popularity do not establish output reliability. [Source 1](https://github.com/aqm857886159/Nomi/blob/main/README.md) [Source 2](https://nomiaqm.com/en/quickstart)

### Limitations

Local project storage does not make API inference local. Installers currently lack platform signing/notarization. Minimum RAM/VRAM is not documented and local model requirements are separate; AI editing remains on the roadmap. [Source 1](https://github.com/aqm857886159/Nomi/blob/main/README.md) [Source 2](https://nomiaqm.com/en/quickstart)

### Get the tool

- [Repository](https://github.com/aqm857886159/Nomi)
- [Documentation](https://github.com/aqm857886159/Nomi/blob/main/README.md)

## Arya

Video, animation & film · Editing, captions & post-production · AI kinetic typography and animated lettering · AI color direction and palette-based media

First full guide in this library. The repository was created 2026-10-19, within the discovery window; that date does not establish a product launch or output quality.

### Quality assessment: Quality unverified

Software licensing and a concrete creative AI use are supported. The remaining checks do not establish a recommendation.

Scope: AI-assisted clip editing, captions/shorts, titles, color work and audio cleanup in a locally stored project.

Evidence checked: 2026-10-22. No local execution implied.

- **Open-source software license · verified:** The complete root software license was read and archived. The grant covers this project code; unresolved model, service and asset terms are disclosed separately. [Source](https://github.com/rubix-labs-hq/arya/blob/main/LICENSE)
- **Creative results · documented:** README screenshots show edits using Tears of Steel footage, with separate native/local/hosted feature tables. These examples do not prove every export path. [Source](https://github.com/rubix-labs-hq/arya/blob/main/README.md) [Source](https://github.com/rubix-labs-hq/arya/blob/main/THIRD_PARTY_NOTICES.md)
- **Reproducible setup · documented:** Use the official macOS DMG for the native app. For the full local browser editor, follow the macOS developer setup, prepare its persistence helper and start the local media server. Independent reproduction has not been established in this review. [Source](https://github.com/rubix-labs-hq/arya/blob/main/README.md) [Source](https://github.com/rubix-labs-hq/arya/blob/main/THIRD_PARTY_NOTICES.md)
- **Maintenance and support · unknown:** A release or active repository alone does not establish sustained support. Workflow-specific support and unresolved blockers need a deeper review.
- **Independent use · unknown:** Independent first-hand use or a working third-party integration was not established for this selected workflow.
- **Models, services and costs · documented:** MIT editor code; MPL-2.0 media muxing, OFL fonts and separately licensed sample footage. Apple frameworks, assistant accounts/CLIs and optional speech models retain their terms. Local compute plus any chosen external model or service; provider access and charges are separate. [Source](https://github.com/rubix-labs-hq/arya/blob/main/README.md) [Source](https://github.com/rubix-labs-hq/arya/blob/main/THIRD_PARTY_NOTICES.md)

Documentation review only; AI Media Scout did not install or run this software. Hosted and local versions have different capabilities. Hosted export is limited to five minutes, and iPhone/iPad distribution is forthcoming. Shorts scores describe structure, not predicted audience performance.

### How it uses AI

A video and motion editor lets an AI assistant inspect project state or rendered frames and apply ordinary undoable timeline edits. [Source](https://github.com/rubix-labs-hq/arya/blob/main/README.md) [Source](https://github.com/rubix-labs-hq/arya/blob/main/THIRD_PARTY_NOTICES.md)

### Introduction

A video and motion editor lets an AI assistant inspect project state or rendered frames and apply ordinary undoable timeline edits. [Source 1](https://github.com/rubix-labs-hq/arya/blob/main/README.md) [Source 2](https://github.com/rubix-labs-hq/arya/blob/main/THIRD_PARTY_NOTICES.md)

### What it is good for

AI-assisted clip editing, captions/shorts, titles, color work and audio cleanup in a locally stored project. [Source 1](https://github.com/rubix-labs-hq/arya/blob/main/README.md) [Source 2](https://github.com/rubix-labs-hq/arya/blob/main/THIRD_PARTY_NOTICES.md)

### Demo & examples

README screenshots show edits using Tears of Steel footage, with separate native/local/hosted feature tables. These examples do not prove every export path. [Source 1](https://github.com/rubix-labs-hq/arya/blob/main/README.md) [Source 2](https://github.com/rubix-labs-hq/arya/blob/main/THIRD_PARTY_NOTICES.md)

### Install

Use the official macOS DMG for the native app. For the full local browser editor, follow the macOS developer setup, prepare its persistence helper and start the local media server. [Source 1](https://github.com/rubix-labs-hq/arya/blob/main/README.md) [Source 2](https://github.com/rubix-labs-hq/arya/blob/main/THIRD_PARTY_NOTICES.md)

1. Obtain the official source or release linked below.
2. Use the official macOS DMG for the native app. For the full local browser editor, follow the macOS developer setup, prepare its persistence helper and start the local media server.

```sh
npm ci --prefix editor
```


```sh
npm run --prefix editor prepare:persistence
```


```sh
npm run --prefix editor check:persistence
```

### First project

Start with a short, representative project and inspect the result before a larger batch. [Source 1](https://github.com/rubix-labs-hq/arya/blob/main/README.md) [Source 2](https://github.com/rubix-labs-hq/arya/blob/main/THIRD_PARTY_NOTICES.md)

1. Create a project and import a short clip.
2. Connect an optional supported AI assistant and request a bounded timeline edit.
3. Review and undo as needed, then export using the formats supported by that edition.
### Hardware & software

Requirements below are documented for this workflow. Unspecified limits are not inferred. [Source 1](https://github.com/rubix-labs-hq/arya/blob/main/README.md) [Source 2](https://github.com/rubix-labs-hq/arya/blob/main/THIRD_PARTY_NOTICES.md)

- **Hardware:** Minimum system RAM, VRAM and total disk space are not documented in the reviewed instructions.
- **Software:** macOS 14+ native app. Local browser development requires Node.js 22+, FFmpeg/ffprobe, Chrome and Xcode Command Line Tools; native compilation needs Xcode 26.4.1+. Browser transcription optionally uses whisper.cpp.
- **Platforms:** Native releases support Apple Silicon and Intel macOS 14+. The full local browser route also depends on a macOS-only persistence helper. Hosted Chrome/Edge editing omits AI assistant, transcription and other server features.

### License, model weights & costs

The full software license was reviewed. Model weights, assets and services remain separate. [Source 1](https://github.com/rubix-labs-hq/arya/blob/main/LICENSE) [Source 2](https://github.com/rubix-labs-hq/arya/blob/main/README.md) [Source 3](https://github.com/rubix-labs-hq/arya/blob/main/THIRD_PARTY_NOTICES.md)

- **Code:** MIT
- **Weights:** MIT editor code; MPL-2.0 media muxing, OFL fonts and separately licensed sample footage. Apple frameworks, assistant accounts/CLIs and optional speech models retain their terms.
- **Commercial:** Software use follows MIT. MIT editor code; MPL-2.0 media muxing, OFL fonts and separately licensed sample footage. Apple frameworks, assistant accounts/CLIs and optional speech models retain their terms.
- **Cost:** Local compute plus any chosen external model or service; provider access and charges are separate.

### Why it merits attention

Included for the documented creative workflow. A complete guide and popularity do not establish output reliability. [Source 1](https://github.com/rubix-labs-hq/arya/blob/main/README.md) [Source 2](https://github.com/rubix-labs-hq/arya/blob/main/THIRD_PARTY_NOTICES.md)

### Limitations

Hosted and local versions have different capabilities. Hosted export is limited to five minutes, and iPhone/iPad distribution is forthcoming. Shorts scores describe structure, not predicted audience performance. [Source 1](https://github.com/rubix-labs-hq/arya/blob/main/README.md) [Source 2](https://github.com/rubix-labs-hq/arya/blob/main/THIRD_PARTY_NOTICES.md)

### Get the tool

- [Repository](https://github.com/rubix-labs-hq/arya)
- [Documentation](https://github.com/rubix-labs-hq/arya/blob/main/README.md)

## Anymotion

Video, animation & film · AI kinetic typography and animated lettering · AI agents for code-authored media production

First full guide in this library, establishing a documentation baseline; not a claim of a launch or significant update today.

### Quality assessment: Quality unverified

Software licensing and a concrete creative AI use are supported. The remaining checks do not establish a recommendation.

Scope: Short explainers, titles and brand motion experiments with editable code and screenshot-based revision.

Evidence checked: 2026-10-22. No local execution implied.

- **Open-source software license · verified:** The complete root software license was read and archived. The grant covers this project code; unresolved model, service and asset terms are disclosed separately. [Source](https://github.com/anymotion-agent/anymotion/blob/main/LICENSE)
- **Creative results · documented:** The README demonstrates planning, frame previews and composition checks. Claims of zero-bug first passes are marketing claims, not verified outcomes. [Source](https://github.com/anymotion-agent/anymotion/blob/main/README.md) [Source](https://anymotion.art)
- **Reproducible setup · documented:** Install Node.js 18+ and the npm package; run the provider setup wizard. FFmpeg is additionally required for MP4 export. Independent reproduction has not been established in this review. [Source](https://github.com/anymotion-agent/anymotion/blob/main/README.md) [Source](https://anymotion.art)
- **Maintenance and support · unknown:** A release or active repository alone does not establish sustained support. Workflow-specific support and unresolved blockers need a deeper review.
- **Independent use · unknown:** Independent first-hand use or a working third-party integration was not established for this selected workflow.
- **Models, services and costs · documented:** MIT agent code. Model-provider terms, API charges, local-model weights and imported brand assets are separate. Local compute plus any chosen external model or service; provider access and charges are separate. [Source](https://github.com/anymotion-agent/anymotion/blob/main/README.md) [Source](https://anymotion.art)

Documentation review only; AI Media Scout did not install or run this software. A passing structural/composition audit does not guarantee attractive motion, correct content or a bug-free render. Provider defaults and capabilities may vary; no independent reproduction was established.

### How it uses AI

A terminal agent writes HTML/CSS/JavaScript motion graphics, inspects frames through a headless browser and renders video. [Source](https://github.com/anymotion-agent/anymotion/blob/main/README.md) [Source](https://anymotion.art)

### Introduction

A terminal agent writes HTML/CSS/JavaScript motion graphics, inspects frames through a headless browser and renders video. [Source 1](https://github.com/anymotion-agent/anymotion/blob/main/README.md) [Source 2](https://anymotion.art)

### What it is good for

Short explainers, titles and brand motion experiments with editable code and screenshot-based revision. [Source 1](https://github.com/anymotion-agent/anymotion/blob/main/README.md) [Source 2](https://anymotion.art)

### Demo & examples

The README demonstrates planning, frame previews and composition checks. Claims of zero-bug first passes are marketing claims, not verified outcomes. [Source 1](https://github.com/anymotion-agent/anymotion/blob/main/README.md) [Source 2](https://anymotion.art)

### Install

Install Node.js 18+ and the npm package; run the provider setup wizard. FFmpeg is additionally required for MP4 export. [Source 1](https://github.com/anymotion-agent/anymotion/blob/main/README.md) [Source 2](https://anymotion.art)

1. Obtain the official source or release linked below.
2. Install Node.js 18+ and the npm package; run the provider setup wizard. FFmpeg is additionally required for MP4 export.

```sh
npm install -g @anymotion-agent/anymotion
```


```sh
anymotion setup
```


```sh
anymotion doctor
```

### First project

Start with a short, representative project and inspect the result before a larger batch. [Source 1](https://github.com/anymotion-agent/anymotion/blob/main/README.md) [Source 2](https://anymotion.art)

1. Describe a short animation and its duration/format.
2. Review sampled frames and composition findings, then revise.
3. Render a test MP4 and inspect it at full playback speed.
### Hardware & software

Requirements below are documented for this workflow. Unspecified limits are not inferred. [Source 1](https://github.com/anymotion-agent/anymotion/blob/main/README.md) [Source 2](https://anymotion.art)

- **Hardware:** Minimum system RAM, VRAM and total disk space are not documented in the reviewed instructions.
- **Software:** Node.js 18+, headless-browser dependencies and FFmpeg for video export. A configured cloud or local language-model endpoint is required.
- **Platforms:** Windows, macOS and Linux FFmpeg setup routes are documented; a comprehensive tested hardware/browser matrix is not supplied.

### License, model weights & costs

The full software license was reviewed. Model weights, assets and services remain separate. [Source 1](https://github.com/anymotion-agent/anymotion/blob/main/LICENSE) [Source 2](https://github.com/anymotion-agent/anymotion/blob/main/README.md) [Source 3](https://anymotion.art)

- **Code:** MIT
- **Weights:** MIT agent code. Model-provider terms, API charges, local-model weights and imported brand assets are separate.
- **Commercial:** Software use follows MIT. MIT agent code. Model-provider terms, API charges, local-model weights and imported brand assets are separate.
- **Cost:** Local compute plus any chosen external model or service; provider access and charges are separate.

### Why it merits attention

Included for the documented creative workflow. A complete guide and popularity do not establish output reliability. [Source 1](https://github.com/anymotion-agent/anymotion/blob/main/README.md) [Source 2](https://anymotion.art)

### Limitations

A passing structural/composition audit does not guarantee attractive motion, correct content or a bug-free render. Provider defaults and capabilities may vary; no independent reproduction was established. [Source 1](https://github.com/anymotion-agent/anymotion/blob/main/README.md) [Source 2](https://anymotion.art)

### Get the tool

- [Repository](https://github.com/anymotion-agent/anymotion)
- [Documentation](https://github.com/anymotion-agent/anymotion/blob/main/README.md)

## Lyrictor

Audio, music & voice · Video, animation & film · Typography, fonts & layout · Storyboarding, narrative & comics

First full guide in this library, establishing a documentation baseline; not a claim of a launch or significant update today.

### Quality assessment: Quality unverified

Software licensing and a concrete creative AI use are supported. The remaining checks do not establish a recommendation.

Scope: Creating a personal visual interpretation of a song, with synchronized lyrics and portrait or landscape video output.

Evidence checked: 2026-10-22. No local execution implied.

- **Open-source software license · verified:** The complete root software license was read and archived. The grant covers this project code; unresolved model, service and asset terms are disclosed separately. [Source](https://github.com/jtCodes/lyrictor/blob/master/LICENSE)
- **Creative results · documented:** Two linked video demonstrations show the editor and AI preview. They are author demonstrations and do not grant rights to the music shown. [Source](https://github.com/jtCodes/lyrictor/blob/master/docs/README.md)
- **Reproducible setup · documented:** Choose a desktop release or use Node.js 20.19+ in the 20.x line, or 22.12+, with Yarn 4. Install the locked dependencies and launch the web or desktop development app. Independent reproduction has not been established in this review. [Source](https://github.com/jtCodes/lyrictor/blob/master/docs/README.md)
- **Maintenance and support · unknown:** A release or active repository alone does not establish sustained support. Workflow-specific support and unresolved blockers need a deeper review.
- **Independent use · unknown:** Independent first-hand use or a working third-party integration was not established for this selected workflow.
- **Models, services and costs · documented:** GPL-3.0 app code. AI services/models, Firebase access and music/image rights are separate; importing a URL does not authorize publishing its media. Local compute plus any chosen external model or service; provider access and charges are separate. [Source](https://github.com/jtCodes/lyrictor/blob/master/docs/README.md)

Documentation review only; AI Media Scout did not install or run this software. AI image generation and export depend on the selected service/runtime. Independent synchronization, export and cross-platform reproduction remain unverified.

### How it uses AI

A lyric-visualization editor combines an editable song timeline with AI-generated background images and audio-reactive graphics. [Source](https://github.com/jtCodes/lyrictor/blob/master/docs/README.md)

### Introduction

A lyric-visualization editor combines an editable song timeline with AI-generated background images and audio-reactive graphics. [Source 1](https://github.com/jtCodes/lyrictor/blob/master/docs/README.md)

### What it is good for

Creating a personal visual interpretation of a song, with synchronized lyrics and portrait or landscape video output. [Source 1](https://github.com/jtCodes/lyrictor/blob/master/docs/README.md)

### Demo & examples

Two linked video demonstrations show the editor and AI preview. They are author demonstrations and do not grant rights to the music shown. [Source 1](https://github.com/jtCodes/lyrictor/blob/master/docs/README.md)

### Install

Choose a desktop release or use Node.js 20.19+ in the 20.x line, or 22.12+, with Yarn 4. Install the locked dependencies and launch the web or desktop development app. [Source 1](https://github.com/jtCodes/lyrictor/blob/master/docs/README.md)

1. Obtain the official source or release linked below.
2. Choose a desktop release or use Node.js 20.19+ in the 20.x line, or 22.12+, with Yarn 4. Install the locked dependencies and launch the web or desktop development app.

```sh
corepack enable
```


```sh
yarn install --immutable
```


```sh
yarn dev
```

### First project

Start with a short, representative project and inspect the result before a larger batch. [Source 1](https://github.com/jtCodes/lyrictor/blob/master/docs/README.md)

1. Import audio you have permission to use.
2. Place lyric, image and visualizer layers on the timeline; configure an AI image provider if desired.
3. Review synchronization and export the chosen orientation.
### Hardware & software

Requirements below are documented for this workflow. Unspecified limits are not inferred. [Source 1](https://github.com/jtCodes/lyrictor/blob/master/docs/README.md)

- **Hardware:** Minimum system RAM, VRAM and total disk space are not documented in the reviewed instructions.
- **Software:** Node.js/Vite/Yarn source stack, React and Firebase services; desktop uses Electron. OpenRouter image models or optional local Stable Diffusion are separate.
- **Platforms:** Browser and Electron routes are documented; a Mac desktop build is mentioned as not notarized. Complete OS support and minimum memory requirements are not specified.

### License, model weights & costs

The full software license was reviewed. Model weights, assets and services remain separate. [Source 1](https://github.com/jtCodes/lyrictor/blob/master/LICENSE) [Source 2](https://github.com/jtCodes/lyrictor/blob/master/docs/README.md)

- **Code:** GPL-3.0
- **Weights:** GPL-3.0 app code. AI services/models, Firebase access and music/image rights are separate; importing a URL does not authorize publishing its media.
- **Commercial:** Software use follows GPL-3.0. GPL-3.0 app code. AI services/models, Firebase access and music/image rights are separate; importing a URL does not authorize publishing its media.
- **Cost:** Local compute plus any chosen external model or service; provider access and charges are separate.

### Why it merits attention

Included for the documented creative workflow. A complete guide and popularity do not establish output reliability. [Source 1](https://github.com/jtCodes/lyrictor/blob/master/docs/README.md)

### Limitations

AI image generation and export depend on the selected service/runtime. Independent synchronization, export and cross-platform reproduction remain unverified. [Source 1](https://github.com/jtCodes/lyrictor/blob/master/docs/README.md)

### Get the tool

- [Repository](https://github.com/jtCodes/lyrictor)
- [Documentation](https://github.com/jtCodes/lyrictor/blob/master/docs/README.md)

## Inventor MCP

3D printing & generative CAD · AI parametric design and jewelry · 3D, reconstruction & assets

First full guide in this library, establishing a documentation baseline; not a claim of a launch or significant update today.

### Quality assessment: Quality unverified

Software licensing and a concrete creative AI use are supported. The remaining checks do not establish a recommendation.

Scope: Iterating dimensioned brackets, shafts, sheet-metal parts and other editable CAD geometry in an existing Inventor workflow.

Evidence checked: 2026-10-22. No local execution implied.

- **Open-source software license · verified:** The complete root software license was read and archived. The grant covers this project code; unresolved model, service and asset terms are disclosed separately. [Source](https://github.com/NeonGlay/inventor-mcp/blob/main/LICENSE)
- **Creative results · documented:** The README gives a parametric nut example and operation reports with geometry deltas; this does not establish manufactured-part fitness. [Source](https://github.com/NeonGlay/inventor-mcp/blob/main/README.md)
- **Reproducible setup · documented:** On Windows with Inventor, install Python 3.12+ and the MCP/pywin32 dependencies, then register the repository’s src.server entry in an MCP client and start Inventor. Independent reproduction has not been established in this review. [Source](https://github.com/NeonGlay/inventor-mcp/blob/main/README.md)
- **Maintenance and support · unknown:** A release or active repository alone does not establish sustained support. Workflow-specific support and unresolved blockers need a deeper review.
- **Independent use · unknown:** Independent first-hand use or a working third-party integration was not established for this selected workflow.
- **Models, services and costs · documented:** MIT bridge source. Autodesk Inventor is a separate proprietary host; the AI client/model and any engineering standards/assets have separate terms. Local compute plus any chosen external model or service; provider access and charges are separate. [Source](https://github.com/NeonGlay/inventor-mcp/blob/main/README.md)

Documentation review only; AI Media Scout did not install or run this software. Geometry delta reports do not prove structural safety or manufacturability. A broad arbitrary-Python tool exists; the full behavior and independent usage checks are pending.

### How it uses AI

An MCP server lets a language-model assistant construct parameterized parts through Autodesk Inventor’s COM API. [Source](https://github.com/NeonGlay/inventor-mcp/blob/main/README.md)

### Introduction

An MCP server lets a language-model assistant construct parameterized parts through Autodesk Inventor’s COM API. [Source 1](https://github.com/NeonGlay/inventor-mcp/blob/main/README.md)

### What it is good for

Iterating dimensioned brackets, shafts, sheet-metal parts and other editable CAD geometry in an existing Inventor workflow. [Source 1](https://github.com/NeonGlay/inventor-mcp/blob/main/README.md)

### Demo & examples

The README gives a parametric nut example and operation reports with geometry deltas; this does not establish manufactured-part fitness. [Source 1](https://github.com/NeonGlay/inventor-mcp/blob/main/README.md)

### Install

On Windows with Inventor, install Python 3.12+ and the MCP/pywin32 dependencies, then register the repository’s src.server entry in an MCP client and start Inventor. [Source 1](https://github.com/NeonGlay/inventor-mcp/blob/main/README.md)

1. Obtain the official source or release linked below.
2. On Windows with Inventor, install Python 3.12+ and the MCP/pywin32 dependencies, then register the repository’s src.server entry in an MCP client and start Inventor.

```sh
pip install "mcp[cli]" pywin32
```

### First project

Start with a short, representative project and inspect the result before a larger batch. [Source 1](https://github.com/NeonGlay/inventor-mcp/blob/main/README.md)

1. Open an Inventor working document and connect the MCP client.
2. Ask for a small dimensioned part using bounded operations.
3. Review dimensions, feature history and topology before exporting or fabrication.
### Hardware & software

Requirements below are documented for this workflow. Unspecified limits are not inferred. [Source 1](https://github.com/NeonGlay/inventor-mcp/blob/main/README.md)

- **Hardware:** Minimum system RAM, VRAM and total disk space are not documented in the reviewed instructions.
- **Software:** Windows, Autodesk Inventor, Python 3.12+, pywin32 and mcp[cli]. Developed/tested by the maintainer with Inventor 2026.
- **Platforms:** Windows COM integration. Older Inventor releases may need API adjustments; macOS/Linux are not documented as supported.

### License, model weights & costs

The full software license was reviewed. Model weights, assets and services remain separate. [Source 1](https://github.com/NeonGlay/inventor-mcp/blob/main/LICENSE) [Source 2](https://github.com/NeonGlay/inventor-mcp/blob/main/README.md)

- **Code:** MIT
- **Weights:** MIT bridge source. Autodesk Inventor is a separate proprietary host; the AI client/model and any engineering standards/assets have separate terms.
- **Commercial:** Software use follows MIT. MIT bridge source. Autodesk Inventor is a separate proprietary host; the AI client/model and any engineering standards/assets have separate terms.
- **Cost:** Local compute plus any chosen external model or service; provider access and charges are separate.

### Why it merits attention

Included for the documented creative workflow. A complete guide and popularity do not establish output reliability. [Source 1](https://github.com/NeonGlay/inventor-mcp/blob/main/README.md)

### Limitations

Geometry delta reports do not prove structural safety or manufacturability. A broad arbitrary-Python tool exists; the full behavior and independent usage checks are pending. [Source 1](https://github.com/NeonGlay/inventor-mcp/blob/main/README.md)

### Get the tool

- [Repository](https://github.com/NeonGlay/inventor-mcp)
- [Documentation](https://github.com/NeonGlay/inventor-mcp/blob/main/README.md)

## OpenAI to FreeCAD Workflow

3D printing & generative CAD · AI parametric design and jewelry · 3D, reconstruction & assets · Creative learning & authoring

First full guide in this library, establishing a documentation baseline; not a claim of a launch or significant update today.

### Quality assessment: Quality unverified

Software licensing and a concrete creative AI use are supported. The remaining checks do not establish a recommendation.

Scope: Learning and prototyping text-to-CAD workflows, with a rendered multi-view check of generated geometry.

Evidence checked: 2026-10-22. No local execution implied.

- **Open-source software license · verified:** The complete root software license was read and archived. The grant covers this project code; unresolved model, service and asset terms are disclosed separately. [Source](https://github.com/giuliano-t/openAI-to-freeCAD-workflow/blob/main/LICENSE)
- **Creative results · documented:** The README links a Colab notebook and describes interactive and six-view model visualization; independent geometry or print validation was not established. [Source](https://github.com/giuliano-t/openAI-to-freeCAD-workflow/blob/main/README.md)
- **Reproducible setup · documented:** Open the official notebook in Colab and configure its OpenAI access through the notebook’s documented secret mechanism. Its setup cells install headless FreeCAD and supporting Python packages. Independent reproduction has not been established in this review. [Source](https://github.com/giuliano-t/openAI-to-freeCAD-workflow/blob/main/README.md)
- **Maintenance and support · unknown:** A release or active repository alone does not establish sustained support. Workflow-specific support and unresolved blockers need a deeper review.
- **Independent use · unknown:** Independent first-hand use or a working third-party integration was not established for this selected workflow.
- **Models, services and costs · documented:** MIT pipeline code. OpenAI API/service access, FreeCAD dependencies and reference data retain separate terms. Local compute plus any chosen external model or service; provider access and charges are separate. [Source](https://github.com/giuliano-t/openAI-to-freeCAD-workflow/blob/main/README.md)

Documentation review only; AI Media Scout did not install or run this software. The notebook runs model-generated code. An STL and a plausible rendering do not prove valid solids, dimensions or printable geometry. API costs and model availability are separate.

### How it uses AI

A notebook uses prompt refinement and retrieval examples to generate FreeCAD Python code from a plain-language object description. [Source](https://github.com/giuliano-t/openAI-to-freeCAD-workflow/blob/main/README.md)

### Introduction

A notebook uses prompt refinement and retrieval examples to generate FreeCAD Python code from a plain-language object description. [Source 1](https://github.com/giuliano-t/openAI-to-freeCAD-workflow/blob/main/README.md)

### What it is good for

Learning and prototyping text-to-CAD workflows, with a rendered multi-view check of generated geometry. [Source 1](https://github.com/giuliano-t/openAI-to-freeCAD-workflow/blob/main/README.md)

### Demo & examples

The README links a Colab notebook and describes interactive and six-view model visualization; independent geometry or print validation was not established. [Source 1](https://github.com/giuliano-t/openAI-to-freeCAD-workflow/blob/main/README.md)

### Install

Open the official notebook in Colab and configure its OpenAI access through the notebook’s documented secret mechanism. Its setup cells install headless FreeCAD and supporting Python packages. [Source 1](https://github.com/giuliano-t/openAI-to-freeCAD-workflow/blob/main/README.md)

1. Obtain the official source or release linked below.
2. Open the official notebook in Colab and configure its OpenAI access through the notebook’s documented secret mechanism. Its setup cells install headless FreeCAD and supporting Python packages.
### First project

Start with a short, representative project and inspect the result before a larger batch. [Source 1](https://github.com/giuliano-t/openAI-to-freeCAD-workflow/blob/main/README.md)

1. Use a simple object description with explicit dimensions.
2. Inspect the generated FreeCAD script before running it in your own environment.
3. Check the resulting multi-view geometry and STL separately before fabrication.
### Hardware & software

Requirements below are documented for this workflow. Unspecified limits are not inferred. [Source 1](https://github.com/giuliano-t/openAI-to-freeCAD-workflow/blob/main/README.md)

- **Hardware:** Minimum system RAM, VRAM and total disk space are not documented in the reviewed instructions.
- **Software:** Colab/Python notebook, headless FreeCAD, OpenAI API and visualization dependencies such as trimesh. A complete pinned local-version matrix is not documented in the overview.
- **Platforms:** Google Colab is the documented primary route. Local use is mentioned but equivalent Windows/macOS/Linux setup was not established.

### License, model weights & costs

The full software license was reviewed. Model weights, assets and services remain separate. [Source 1](https://github.com/giuliano-t/openAI-to-freeCAD-workflow/blob/main/LICENSE) [Source 2](https://github.com/giuliano-t/openAI-to-freeCAD-workflow/blob/main/README.md)

- **Code:** MIT
- **Weights:** MIT pipeline code. OpenAI API/service access, FreeCAD dependencies and reference data retain separate terms.
- **Commercial:** Software use follows MIT. MIT pipeline code. OpenAI API/service access, FreeCAD dependencies and reference data retain separate terms.
- **Cost:** Local compute plus any chosen external model or service; provider access and charges are separate.

### Why it merits attention

Included for the documented creative workflow. A complete guide and popularity do not establish output reliability. [Source 1](https://github.com/giuliano-t/openAI-to-freeCAD-workflow/blob/main/README.md)

### Limitations

The notebook runs model-generated code. An STL and a plausible rendering do not prove valid solids, dimensions or printable geometry. API costs and model availability are separate. [Source 1](https://github.com/giuliano-t/openAI-to-freeCAD-workflow/blob/main/README.md)

### Get the tool

- [Repository](https://github.com/giuliano-t/openAI-to-freeCAD-workflow)
- [Documentation](https://github.com/giuliano-t/openAI-to-freeCAD-workflow/blob/main/README.md)

## Inside Music YouTube Edition

WebXR, VR & AR · Spatial audio & volumetric media · Audio, music & voice · Interactive, immersive & live media

First full guide in this library, establishing a documentation baseline; not a claim of a launch or significant update today.

### Quality assessment: Quality unverified

Software licensing and a concrete creative AI use are supported. The remaining checks do not establish a recommendation.

Scope: Exploring a song’s layers as an immersive educational or exhibition-style audio experience.

Evidence checked: 2026-10-22. No local execution implied.

- **Open-source software license · verified:** The complete root software license was read and archived. The grant covers this project code; unresolved model, service and asset terms are disclosed separately. [Source](https://github.com/toxtli/webvr-360-music/blob/master/LICENSE)
- **Creative results · documented:** The README links a historic online experiment and describes spherical instrument controls. Current availability and headset operation were not established. [Source](https://github.com/toxtli/webvr-360-music/blob/master/README.md)
- **Reproducible setup · documented:** Install the frontend’s legacy Node/webpack dependencies and Python backend requirements, configure the local audio directory, then run the backend and a local frontend server. Independent reproduction has not been established in this review. [Source](https://github.com/toxtli/webvr-360-music/blob/master/README.md)
- **Maintenance and support · unknown:** A release or active repository alone does not establish sustained support. Workflow-specific support and unresolved blockers need a deeper review.
- **Independent use · unknown:** Independent first-hand use or a working third-party integration was not established for this selected workflow.
- **Models, services and costs · documented:** Apache-2.0 code. Spleeter dependencies/weights and song rights are separate; audio is not included and a source URL does not clear reuse rights. Local compute plus any chosen external model or service; provider access and charges are separate. [Source](https://github.com/toxtli/webvr-360-music/blob/master/README.md)

Documentation review only; AI Media Scout did not install or run this software. The README retains the original experiment framing. That historical description is not treated as a current instability verdict. Legacy WebVR/build dependencies, source downloads and modern headset compatibility need fresh testing.

### How it uses AI

A Spleeter-based stem-separation backend feeds a browser/VR sound room where individual instruments can be toggled in space. [Source](https://github.com/toxtli/webvr-360-music/blob/master/README.md)

### Introduction

A Spleeter-based stem-separation backend feeds a browser/VR sound room where individual instruments can be toggled in space. [Source 1](https://github.com/toxtli/webvr-360-music/blob/master/README.md)

### What it is good for

Exploring a song’s layers as an immersive educational or exhibition-style audio experience. [Source 1](https://github.com/toxtli/webvr-360-music/blob/master/README.md)

### Demo & examples

The README links a historic online experiment and describes spherical instrument controls. Current availability and headset operation were not established. [Source 1](https://github.com/toxtli/webvr-360-music/blob/master/README.md)

### Install

Install the frontend’s legacy Node/webpack dependencies and Python backend requirements, configure the local audio directory, then run the backend and a local frontend server. [Source 1](https://github.com/toxtli/webvr-360-music/blob/master/README.md)

1. Obtain the official source or release linked below.
2. Install the frontend’s legacy Node/webpack dependencies and Python backend requirements, configure the local audio directory, then run the backend and a local frontend server.

```sh
npm install
```


```sh
webpack -p
```


```sh
pip install -r requirements.txt
```


```sh
python app.py --web
```

### First project

Start with a short, representative project and inspect the result before a larger batch. [Source 1](https://github.com/toxtli/webvr-360-music/blob/master/README.md)

1. Process an authorized audio source through the documented backend.
2. Open the corresponding song in the browser scene.
3. Toggle separated stems and inspect separation artifacts; verify any target headset independently.
### Hardware & software

Requirements below are documented for this workflow. Unspecified limits are not inferred. [Source 1](https://github.com/toxtli/webvr-360-music/blob/master/README.md)

- **Hardware:** Minimum system RAM, VRAM and total disk space are not documented in the reviewed instructions.
- **Software:** Legacy webpack below 4, Node.js, A-Frame/Three.js/Tone.js, Python and Spleeter. Exact modern Python/browser compatibility is not specified.
- **Platforms:** Browser, historical WebVR controllers and Google Cardboard are described. Modern WebXR/headset compatibility and desktop OS testing are not established.

### License, model weights & costs

The full software license was reviewed. Model weights, assets and services remain separate. [Source 1](https://github.com/toxtli/webvr-360-music/blob/master/LICENSE) [Source 2](https://github.com/toxtli/webvr-360-music/blob/master/README.md)

- **Code:** Apache-2.0
- **Weights:** Apache-2.0 code. Spleeter dependencies/weights and song rights are separate; audio is not included and a source URL does not clear reuse rights.
- **Commercial:** Software use follows Apache-2.0. Apache-2.0 code. Spleeter dependencies/weights and song rights are separate; audio is not included and a source URL does not clear reuse rights.
- **Cost:** Local compute plus any chosen external model or service; provider access and charges are separate.

### Why it merits attention

Included for the documented creative workflow. A complete guide and popularity do not establish output reliability. [Source 1](https://github.com/toxtli/webvr-360-music/blob/master/README.md)

### Limitations

The README retains the original experiment framing. That historical description is not treated as a current instability verdict. Legacy WebVR/build dependencies, source downloads and modern headset compatibility need fresh testing. [Source 1](https://github.com/toxtli/webvr-360-music/blob/master/README.md)

### Get the tool

- [Repository](https://github.com/toxtli/webvr-360-music)
- [Documentation](https://github.com/toxtli/webvr-360-music/blob/master/README.md)

## Manga Colorization FJ

Images & design · Storyboarding, narrative & comics · AI cel animation and inbetweening

First full guide in this library, establishing a documentation baseline; not a claim of a launch or significant update today.

### Quality assessment: Quality unverified

Software licensing and a concrete creative AI use are supported. The remaining checks do not establish a recommendation.

Scope: Draft color studies for line art and testing batch colorization on pages the creator is authorized to transform.

Evidence checked: 2026-10-22. No local execution implied.

- **Open-source software license · verified:** The complete root software license was read and archived. The grant covers this project code; unresolved model, service and asset terms are disclosed separately. [Source](https://github.com/xiaogdgenuine/Manga-Colorization-FJ/blob/main/LICENSE)
- **Creative results · documented:** The README provides paired sample images. They are documented examples, not evidence of consistent character palettes across a comic. [Source](https://github.com/xiaogdgenuine/Manga-Colorization-FJ/blob/main/README.md)
- **Reproducible setup · documented:** Use the repository’s Python dependencies, download the linked generator.pt into networks, and place a small sample in input. Choose CPU or the optional GPU flag. Independent reproduction has not been established in this review. [Source](https://github.com/xiaogdgenuine/Manga-Colorization-FJ/blob/main/README.md)
- **Maintenance and support · unknown:** A release or active repository alone does not establish sustained support. Workflow-specific support and unresolved blockers need a deeper review.
- **Independent use · unknown:** Independent first-hand use or a working third-party integration was not established for this selected workflow.
- **Models, services and costs · documented:** GPL-3.0 project code. The linked generator weights, Real-ESRGAN model and original artwork require separate license/rights review. Local compute plus any chosen external model or service; provider access and charges are separate. [Source](https://github.com/xiaogdgenuine/Manga-Colorization-FJ/blob/main/README.md)

Documentation review only; AI Media Scout did not install or run this software. Minimum RAM/VRAM and total storage are undocumented; tiling does not establish a universal low-memory minimum. Color continuity, text preservation and model-download reliability remain unverified.

### How it uses AI

A learned manga-colorization pipeline converts line-art pages to color, with optional tiled Real-ESRGAN upscaling. [Source](https://github.com/xiaogdgenuine/Manga-Colorization-FJ/blob/main/README.md)

### Introduction

A learned manga-colorization pipeline converts line-art pages to color, with optional tiled Real-ESRGAN upscaling. [Source 1](https://github.com/xiaogdgenuine/Manga-Colorization-FJ/blob/main/README.md)

### What it is good for

Draft color studies for line art and testing batch colorization on pages the creator is authorized to transform. [Source 1](https://github.com/xiaogdgenuine/Manga-Colorization-FJ/blob/main/README.md)

### Demo & examples

The README provides paired sample images. They are documented examples, not evidence of consistent character palettes across a comic. [Source 1](https://github.com/xiaogdgenuine/Manga-Colorization-FJ/blob/main/README.md)

### Install

Use the repository’s Python dependencies, download the linked generator.pt into networks, and place a small sample in input. Choose CPU or the optional GPU flag. [Source 1](https://github.com/xiaogdgenuine/Manga-Colorization-FJ/blob/main/README.md)

1. Obtain the official source or release linked below.
2. Use the repository’s Python dependencies, download the linked generator.pt into networks, and place a small sample in input. Choose CPU or the optional GPU flag.

```sh
python inference.py
```


```sh
python inference.py -g
```

### First project

Start with a short, representative project and inspect the result before a larger batch. [Source 1](https://github.com/xiaogdgenuine/Manga-Colorization-FJ/blob/main/README.md)

1. Place a permitted line-art image in the input folder.
2. Run a small colorization and inspect the output.
3. Adjust tile/size settings or optional upscaling, then correct character colors manually as needed.
### Hardware & software

Requirements below are documented for this workflow. Unspecified limits are not inferred. [Source 1](https://github.com/xiaogdgenuine/Manga-Colorization-FJ/blob/main/README.md)

- **Hardware:** Minimum system RAM, VRAM and total disk space are not documented in the reviewed instructions.
- **Software:** Python and PyTorch; the README says the checkpoint format supports PyTorch 1.0+. Exact current dependency compatibility and model-host availability require validation.
- **Platforms:** CPU and GPU modes are documented; an OS-specific supported-platform matrix is absent.

### License, model weights & costs

The full software license was reviewed. Model weights, assets and services remain separate. [Source 1](https://github.com/xiaogdgenuine/Manga-Colorization-FJ/blob/main/LICENSE) [Source 2](https://github.com/xiaogdgenuine/Manga-Colorization-FJ/blob/main/README.md)

- **Code:** GPL-3.0
- **Weights:** GPL-3.0 project code. The linked generator weights, Real-ESRGAN model and original artwork require separate license/rights review.
- **Commercial:** Software use follows GPL-3.0. GPL-3.0 project code. The linked generator weights, Real-ESRGAN model and original artwork require separate license/rights review.
- **Cost:** Local compute plus any chosen external model or service; provider access and charges are separate.

### Why it merits attention

Included for the documented creative workflow. A complete guide and popularity do not establish output reliability. [Source 1](https://github.com/xiaogdgenuine/Manga-Colorization-FJ/blob/main/README.md)

### Limitations

Minimum RAM/VRAM and total storage are undocumented; tiling does not establish a universal low-memory minimum. Color continuity, text preservation and model-download reliability remain unverified. [Source 1](https://github.com/xiaogdgenuine/Manga-Colorization-FJ/blob/main/README.md)

### Get the tool

- [Repository](https://github.com/xiaogdgenuine/Manga-Colorization-FJ)
- [Documentation](https://github.com/xiaogdgenuine/Manga-Colorization-FJ/blob/main/README.md)

## SemantiCodec

Audio, music & voice · Learned media codecs and neural delivery

First full guide in this library, establishing a documentation baseline; not a claim of a launch or significant update today.

### Quality assessment: Quality unverified

Software licensing and a concrete creative AI use are supported. The remaining checks do not establish a recommendation.

Scope: Exploring low-bitrate sound representations for audio art, speech and generative-audio pipelines.

Evidence checked: 2026-10-22. No local execution implied.

- **Open-source software license · verified:** The complete root software license was read and archived. The grant covers this project code; unresolved model, service and asset terms are disclosed separately. [Source](https://github.com/haoheliu/SemantiCodec-inference/blob/main/LICENSE)
- **Creative results · documented:** The README links the author’s audio-sample page and reports bitrate/token-rate settings. We did not listen to or reproduce the comparisons. [Source](https://github.com/haoheliu/SemantiCodec-inference/blob/main/README.md)
- **Reproducible setup · documented:** Install the source package in a Python environment. Initializing SemantiCodec downloads checkpoints; select a supported compute device and review those model terms before reuse. Independent reproduction has not been established in this review. [Source](https://github.com/haoheliu/SemantiCodec-inference/blob/main/README.md)
- **Maintenance and support · unknown:** A release or active repository alone does not establish sustained support. Workflow-specific support and unresolved blockers need a deeper review.
- **Independent use · unknown:** Independent first-hand use or a working third-party integration was not established for this selected workflow.
- **Models, services and costs · documented:** Automatically downloaded checkpoints and evaluation datasets are separate from the MIT software grant; their complete downstream-use terms remain unresolved. Local compute plus any chosen external model or service; provider access and charges are separate. [Source](https://github.com/haoheliu/SemantiCodec-inference/blob/main/README.md)

Documentation review only; AI Media Scout did not install or run this software. This is a developer codec, not a music-production GUI. Claimed bitrate and perceptual advantages need independent review; low bitrate does not imply lossless preservation.

### How it uses AI

A learned audio encoder and decoder turn general sound into compact semantic tokens and reconstruct a waveform. [Source](https://github.com/haoheliu/SemantiCodec-inference/blob/main/README.md)

### Introduction

A learned audio encoder and decoder turn general sound into compact semantic tokens and reconstruct a waveform. [Source 1](https://github.com/haoheliu/SemantiCodec-inference/blob/main/README.md)

### What it is good for

Exploring low-bitrate sound representations for audio art, speech and generative-audio pipelines. [Source 1](https://github.com/haoheliu/SemantiCodec-inference/blob/main/README.md)

### Demo & examples

The README links the author’s audio-sample page and reports bitrate/token-rate settings. We did not listen to or reproduce the comparisons. [Source 1](https://github.com/haoheliu/SemantiCodec-inference/blob/main/README.md)

### Install

Install the source package in a Python environment. Initializing SemantiCodec downloads checkpoints; select a supported compute device and review those model terms before reuse. [Source 1](https://github.com/haoheliu/SemantiCodec-inference/blob/main/README.md)

1. Obtain the official source or release linked below.
2. Install the source package in a Python environment. Initializing SemantiCodec downloads checkpoints; select a supported compute device and review those model terms before reuse.

```sh
pip install git+https://github.com/haoheliu/SemantiCodec-inference.git
```

### First project

Start with a short, representative project and inspect the result before a larger batch. [Source 1](https://github.com/haoheliu/SemantiCodec-inference/blob/main/README.md)

1. Instantiate SemantiCodec with token_rate=100 and semantic_vocab_size=16384, following the official example.
2. Encode a short WAV with semanticodec.encode(filepath), then reconstruct with semanticodec.decode(tokens).
3. Save waveform[0,0] at 16000 Hz using soundfile and compare it with the original; inspect artifacts before reducing the token rate.
### Hardware & software

Requirements below are documented for this workflow. Unspecified limits are not inferred. [Source 1](https://github.com/haoheliu/SemantiCodec-inference/blob/main/README.md)

- **Hardware:** Minimum system RAM, VRAM and total disk space are not documented in the reviewed instructions.
- **Software:** Python, the package dependencies and soundfile. Exact Python/PyTorch minimums are not specified in the reviewed quickstart.
- **Platforms:** CPU, CUDA and Apple MPS backends are explicitly documented; a complete OS/version compatibility matrix is not published.

### License, model weights & costs

The full software license was reviewed. Model weights, assets and services remain separate. [Source 1](https://github.com/haoheliu/SemantiCodec-inference/blob/main/LICENSE) [Source 2](https://github.com/haoheliu/SemantiCodec-inference/blob/main/README.md)

- **Code:** MIT
- **Weights:** Automatically downloaded checkpoints and evaluation datasets are separate from the MIT software grant; their complete downstream-use terms remain unresolved.
- **Commercial:** Software use follows MIT. Automatically downloaded checkpoints and evaluation datasets are separate from the MIT software grant; their complete downstream-use terms remain unresolved.
- **Cost:** Local compute plus any chosen external model or service; provider access and charges are separate.

### Why it merits attention

Included for the documented creative workflow. A complete guide and popularity do not establish output reliability. [Source 1](https://github.com/haoheliu/SemantiCodec-inference/blob/main/README.md)

### Limitations

This is a developer codec, not a music-production GUI. Claimed bitrate and perceptual advantages need independent review; low bitrate does not imply lossless preservation. [Source 1](https://github.com/haoheliu/SemantiCodec-inference/blob/main/README.md)

### Get the tool

- [Repository](https://github.com/haoheliu/SemantiCodec-inference)
- [Documentation](https://github.com/haoheliu/SemantiCodec-inference/blob/main/README.md)

## HILCodec

Audio, music & voice · Learned media codecs and neural delivery

First full guide in this library, establishing a documentation baseline; not a claim of a launch or significant update today.

### Quality assessment: Quality unverified

Software licensing and a concrete creative AI use are supported. The remaining checks do not establish a recommendation.

Scope: Comparing compressed dialogue, ambience and music for interactive or networked media.

Evidence checked: 2026-10-22. No local execution implied.

- **Open-source software license · verified:** The complete root software license was read and archived. The grant covers this project code; unresolved model, service and asset terms are disclosed separately. [Source](https://github.com/aask1357/hilcodec/blob/master/LICENSE)
- **Creative results · documented:** The author links audio samples and supplies hil_music and hil_speech ONNX models. Objective and listening results were not reproduced. [Source](https://github.com/aask1357/hilcodec/blob/master/README.md)
- **Reproducible setup · documented:** For inference, obtain the source and install ONNXRuntime, librosa and soundfile. The training route has a separate PyTorch/CUDA environment; start with the supplied ONNX test script. Independent reproduction has not been established in this review. [Source](https://github.com/aask1357/hilcodec/blob/master/README.md)
- **Maintenance and support · unknown:** A release or active repository alone does not establish sustained support. Workflow-specific support and unresolved blockers need a deeper review.
- **Independent use · unknown:** Independent first-hand use or a working third-party integration was not established for this selected workflow.
- **Models, services and costs · documented:** The root software grant is MIT. Pretrained checkpoints and VCTK, DNS, Jamendo and other comparison data retain separate terms; the grant is not generalized to every dataset. Local compute plus any chosen external model or service; provider access and charges are separate. [Source](https://github.com/aask1357/hilcodec/blob/master/README.md)

Documentation review only; AI Media Scout did not install or run this software. Some optional evaluation metrics reportedly crash on the author’s server. That limitation is scoped to evaluation; output quality and other environments remain unverified.

### How it uses AI

A learned streaming audio codec encodes and reconstructs speech or general audio using separate pretrained model variants. [Source](https://github.com/aask1357/hilcodec/blob/master/README.md)

### Introduction

A learned streaming audio codec encodes and reconstructs speech or general audio using separate pretrained model variants. [Source 1](https://github.com/aask1357/hilcodec/blob/master/README.md)

### What it is good for

Comparing compressed dialogue, ambience and music for interactive or networked media. [Source 1](https://github.com/aask1357/hilcodec/blob/master/README.md)

### Demo & examples

The author links audio samples and supplies hil_music and hil_speech ONNX models. Objective and listening results were not reproduced. [Source 1](https://github.com/aask1357/hilcodec/blob/master/README.md)

### Install

For inference, obtain the source and install ONNXRuntime, librosa and soundfile. The training route has a separate PyTorch/CUDA environment; start with the supplied ONNX test script. [Source 1](https://github.com/aask1357/hilcodec/blob/master/README.md)

1. Obtain the official source or release linked below.
2. For inference, obtain the source and install ONNXRuntime, librosa and soundfile. The training route has a separate PyTorch/CUDA environment; start with the supplied ONNX test script.

```sh
pip install onnxruntime librosa soundfile
```


```sh
python test_onnx.py -n hil_speech --enc --dec
```

### First project

Start with a short, representative project and inspect the result before a larger batch. [Source 1](https://github.com/aask1357/hilcodec/blob/master/README.md)

1. Set PATH in test_onnx.py to a short input as the README directs.
2. Choose hil_speech for clean speech or hil_music for the broader audio model, and encode/decode it.
3. Inspect onnx/hil_speech_output.wav and compare quality before integrating the codec; use the script help for sample-rate and frame settings.
### Hardware & software

Requirements below are documented for this workflow. Unspecified limits are not inferred. [Source 1](https://github.com/aask1357/hilcodec/blob/master/README.md)

- **Hardware:** Minimum system RAM, VRAM and total disk space are not documented in the reviewed instructions.
- **Software:** Inference: ONNXRuntime, librosa, soundfile. Maintainer-tested training pairs include CUDA 10.2/PyTorch 1.12, CUDA 11.7/PyTorch 1.13 and CUDA 11.8/PyTorch 2.5.
- **Platforms:** CPU ONNX inference is documented. Training uses CUDA; no complete Windows/macOS/Linux support matrix is stated.

### License, model weights & costs

The full software license was reviewed. Model weights, assets and services remain separate. [Source 1](https://github.com/aask1357/hilcodec/blob/master/LICENSE) [Source 2](https://github.com/aask1357/hilcodec/blob/master/README.md)

- **Code:** MIT
- **Weights:** The root software grant is MIT. Pretrained checkpoints and VCTK, DNS, Jamendo and other comparison data retain separate terms; the grant is not generalized to every dataset.
- **Commercial:** Software use follows MIT. The root software grant is MIT. Pretrained checkpoints and VCTK, DNS, Jamendo and other comparison data retain separate terms; the grant is not generalized to every dataset.
- **Cost:** Local compute plus any chosen external model or service; provider access and charges are separate.

### Why it merits attention

Included for the documented creative workflow. A complete guide and popularity do not establish output reliability. [Source 1](https://github.com/aask1357/hilcodec/blob/master/README.md)

### Limitations

Some optional evaluation metrics reportedly crash on the author’s server. That limitation is scoped to evaluation; output quality and other environments remain unverified. [Source 1](https://github.com/aask1357/hilcodec/blob/master/README.md)

### Get the tool

- [Repository](https://github.com/aask1357/hilcodec)
- [Documentation](https://github.com/aask1357/hilcodec/blob/master/README.md)

## DisCoder

Audio, music & voice · Learned media codecs and neural delivery

First full guide in this library, establishing a documentation baseline; not a claim of a launch or significant update today.

### Quality assessment: Quality unverified

Software licensing and a concrete creative AI use are supported. The remaining checks do not establish a recommendation.

Scope: Developer experiments with music resynthesis and the decoder stage of generative-audio systems.

Evidence checked: 2026-10-22. No local execution implied.

- **Open-source software license · verified:** The complete root software license was read and archived. The grant covers this project code; unresolved model, service and asset terms are disclosed separately. [Source](https://github.com/ETH-DISCO/discoder/blob/main/LICENSE)
- **Creative results · documented:** The project links author samples and a pretrained Hugging Face model, and includes an original-versus-reconstructed audio notebook example. [Source](https://github.com/ETH-DISCO/discoder/blob/main/README.md)
- **Reproducible setup · documented:** Clone the repository, create a Python 3.11 environment, and install requirements.txt. Obtain the documented model and use its matching configuration; training and ViSQOL setup are separate. Independent reproduction has not been established in this review. [Source](https://github.com/ETH-DISCO/discoder/blob/main/README.md)
- **Maintenance and support · unknown:** A release or active repository alone does not establish sustained support. Workflow-specific support and unresolved blockers need a deeper review.
- **Independent use · unknown:** Independent first-hand use or a working third-party integration was not established for this selected workflow.
- **Models, services and costs · documented:** MIT covers the repository software. The DisCoder checkpoint, upstream DAC weights and training audio need their own terms; no blanket commercial-model permission is inferred. Local compute plus any chosen external model or service; provider access and charges are separate. [Source](https://github.com/ETH-DISCO/discoder/blob/main/README.md)

Documentation review only; AI Media Scout did not install or run this software. It is a vocoder component rather than text-to-music software. Spectrogram fidelity and generalization beyond the published examples remain unverified.

### How it uses AI

A neural vocoder reconstructs 44.1 kHz sound from mel spectrograms through a learned representation aligned with a fine-tuned DAC decoder. [Source](https://github.com/ETH-DISCO/discoder/blob/main/README.md)

### Introduction

A neural vocoder reconstructs 44.1 kHz sound from mel spectrograms through a learned representation aligned with a fine-tuned DAC decoder. [Source 1](https://github.com/ETH-DISCO/discoder/blob/main/README.md)

### What it is good for

Developer experiments with music resynthesis and the decoder stage of generative-audio systems. [Source 1](https://github.com/ETH-DISCO/discoder/blob/main/README.md)

### Demo & examples

The project links author samples and a pretrained Hugging Face model, and includes an original-versus-reconstructed audio notebook example. [Source 1](https://github.com/ETH-DISCO/discoder/blob/main/README.md)

### Install

Clone the repository, create a Python 3.11 environment, and install requirements.txt. Obtain the documented model and use its matching configuration; training and ViSQOL setup are separate. [Source 1](https://github.com/ETH-DISCO/discoder/blob/main/README.md)

1. Obtain the official source or release linked below.
2. Clone the repository, create a Python 3.11 environment, and install requirements.txt. Obtain the documented model and use its matching configuration; training and ViSQOL setup are separate.

```sh
conda create -n discoder python=3.11
```


```sh
conda activate discoder
```


```sh
python -m pip install -r requirements.txt
```

### First project

Start with a short, representative project and inspect the result before a larger batch. [Source 1](https://github.com/ETH-DISCO/discoder/blob/main/README.md)

1. Follow the README’s DisCoder.from_pretrained("disco-eth/discoder") example with a short clip.
2. Load/resample the clip to the model sample rate, pad it, and obtain the configured mel spectrogram.
3. Reconstruct with the model, remove padding, and compare the two waveforms; the supplied batch inference script accepts input/output directories.
### Hardware & software

Requirements below are documented for this workflow. Unspecified limits are not inferred. [Source 1](https://github.com/ETH-DISCO/discoder/blob/main/README.md)

- **Hardware:** Minimum system RAM, VRAM and total disk space are not documented in the reviewed instructions.
- **Software:** Python 3.11 was tested; project PyTorch dependencies and a compatible model/configuration are required.
- **Platforms:** The documented pretrained example uses CUDA. CPU, Apple MPS and a complete native OS matrix are not established by the reviewed instructions.

### License, model weights & costs

The full software license was reviewed. Model weights, assets and services remain separate. [Source 1](https://github.com/ETH-DISCO/discoder/blob/main/LICENSE) [Source 2](https://github.com/ETH-DISCO/discoder/blob/main/README.md)

- **Code:** MIT
- **Weights:** MIT covers the repository software. The DisCoder checkpoint, upstream DAC weights and training audio need their own terms; no blanket commercial-model permission is inferred.
- **Commercial:** Software use follows MIT. MIT covers the repository software. The DisCoder checkpoint, upstream DAC weights and training audio need their own terms; no blanket commercial-model permission is inferred.
- **Cost:** Local compute plus any chosen external model or service; provider access and charges are separate.

### Why it merits attention

Included for the documented creative workflow. A complete guide and popularity do not establish output reliability. [Source 1](https://github.com/ETH-DISCO/discoder/blob/main/README.md)

### Limitations

It is a vocoder component rather than text-to-music software. Spectrogram fidelity and generalization beyond the published examples remain unverified. [Source 1](https://github.com/ETH-DISCO/discoder/blob/main/README.md)

### Get the tool

- [Repository](https://github.com/ETH-DISCO/discoder)
- [Documentation](https://github.com/ETH-DISCO/discoder/blob/main/README.md)

## Trazo

Vector graphics, illustration & textures · Video, animation & film · Data art & scientific visualization · Browser tools & web media

First full guide in this library. The repository was created 2026-10-02, within the discovery window; that date does not establish a product launch or output quality.

### Quality assessment: Quality unverified

Software licensing and a concrete creative AI use are supported. The remaining checks do not establish a recommendation.

Scope: Editable hand-drawn diagrams and narrated slide-to-video explainers.

Evidence checked: 2026-10-22. No local execution implied.

- **Open-source software license · verified:** The complete root software license was read and archived. The grant covers this project code; unresolved model, service and asset terms are disclosed separately. [Source](https://github.com/balalex12/trazo/blob/main/LICENSE)
- **Creative results · documented:** The README includes an exported GIF and a UI tour showing diagram creation, agent edits and animated output; these are maintainer examples. [Source](https://github.com/balalex12/trazo/blob/main/README.md) [Source](https://github.com/balalex12/trazo/blob/main/THIRD_PARTY_NOTICES.md)
- **Reproducible setup · documented:** Choose a desktop release or Docker Compose v2. For a source Docker install, clone the repository and build the compose project, then open localhost:3000. Configure a model in AI assistant settings for AI features. Independent reproduction has not been established in this review. [Source](https://github.com/balalex12/trazo/blob/main/README.md) [Source](https://github.com/balalex12/trazo/blob/main/THIRD_PARTY_NOTICES.md)
- **Maintenance and support · unknown:** A release or active repository alone does not establish sustained support. Workflow-specific support and unresolved blockers need a deeper review.
- **Independent use · unknown:** Independent first-hand use or a working third-party integration was not established for this selected workflow.
- **Models, services and costs · documented:** The core is MIT; fonts and community assets have their own terms. The reviewed notices identify bundled Calcite icons under Esri terms and an optional proprietary ArcGIS SDK loaded at runtime. Local model weights and cloud APIs remain separate. Local compute plus any chosen external model or service; provider access and charges are separate. [Source](https://github.com/balalex12/trazo/blob/main/README.md) [Source](https://github.com/balalex12/trazo/blob/main/THIRD_PARTY_NOTICES.md)

Documentation review only; AI Media Scout did not install or run this software. AI is optional and off initially; non-AI imports are not described as model inference. The optional CLI bridge is experimental, and Utility Network tracing is unvalidated; neither is used as an automatic verdict on the diagram workflow.

### How it uses AI

An optional local or remote language model generates and edits diagrams, and can propose captions, timing and narration for animated explainers. [Source](https://github.com/balalex12/trazo/blob/main/README.md) [Source](https://github.com/balalex12/trazo/blob/main/THIRD_PARTY_NOTICES.md)

### Introduction

An optional local or remote language model generates and edits diagrams, and can propose captions, timing and narration for animated explainers. [Source 1](https://github.com/balalex12/trazo/blob/main/README.md) [Source 2](https://github.com/balalex12/trazo/blob/main/THIRD_PARTY_NOTICES.md)

### What it is good for

Editable hand-drawn diagrams and narrated slide-to-video explainers. [Source 1](https://github.com/balalex12/trazo/blob/main/README.md) [Source 2](https://github.com/balalex12/trazo/blob/main/THIRD_PARTY_NOTICES.md)

### Demo & examples

The README includes an exported GIF and a UI tour showing diagram creation, agent edits and animated output; these are maintainer examples. [Source 1](https://github.com/balalex12/trazo/blob/main/README.md) [Source 2](https://github.com/balalex12/trazo/blob/main/THIRD_PARTY_NOTICES.md)

### Install

Choose a desktop release or Docker Compose v2. For a source Docker install, clone the repository and build the compose project, then open localhost:3000. Configure a model in AI assistant settings for AI features. [Source 1](https://github.com/balalex12/trazo/blob/main/README.md) [Source 2](https://github.com/balalex12/trazo/blob/main/THIRD_PARTY_NOTICES.md)

1. Obtain the official source or release linked below.
2. Choose a desktop release or Docker Compose v2. For a source Docker install, clone the repository and build the compose project, then open localhost:3000. Configure a model in AI assistant settings for AI features.

```sh
docker compose up -d --build
```

### First project

Start with a short, representative project and inspect the result before a larger batch. [Source 1](https://github.com/balalex12/trazo/blob/main/README.md) [Source 2](https://github.com/balalex12/trazo/blob/main/THIRD_PARTY_NOTICES.md)

1. Create or import a diagram and connect the intended local model or remote provider in AI assistant settings.
2. Ask for a small diagram or edit, inspect the editable shapes and undo unwanted changes.
3. Duplicate frames, set timing/transitions and captions, preview the animation, then export MP4/GIF; narration and optional integrations have separate setup.
### Hardware & software

Requirements below are documented for this workflow. Unspecified limits are not inferred. [Source 1](https://github.com/balalex12/trazo/blob/main/README.md) [Source 2](https://github.com/balalex12/trazo/blob/main/THIRD_PARTY_NOTICES.md)

- **Hardware:** Minimum system RAM, VRAM and total disk space are not documented in the reviewed instructions.
- **Software:** Desktop release or Docker with Compose v2. The optional CLI bridge needs Node.js 18+; model runtimes, Jupyter and ArcGIS are separate integrations.
- **Platforms:** Desktop downloads are documented for Windows, macOS and Linux; Docker/browser operation is another route. Detailed minimum OS versions are not stated in the reviewed overview.

### License, model weights & costs

The full software license was reviewed. Model weights, assets and services remain separate. [Source 1](https://github.com/balalex12/trazo/blob/main/LICENSE) [Source 2](https://github.com/balalex12/trazo/blob/main/README.md) [Source 3](https://github.com/balalex12/trazo/blob/main/THIRD_PARTY_NOTICES.md)

- **Code:** MIT
- **Weights:** The core is MIT; fonts and community assets have their own terms. The reviewed notices identify bundled Calcite icons under Esri terms and an optional proprietary ArcGIS SDK loaded at runtime. Local model weights and cloud APIs remain separate.
- **Commercial:** Software use follows MIT. The core is MIT; fonts and community assets have their own terms. The reviewed notices identify bundled Calcite icons under Esri terms and an optional proprietary ArcGIS SDK loaded at runtime. Local model weights and cloud APIs remain separate.
- **Cost:** Local compute plus any chosen external model or service; provider access and charges are separate.

### Why it merits attention

Included for the documented creative workflow. A complete guide and popularity do not establish output reliability. [Source 1](https://github.com/balalex12/trazo/blob/main/README.md) [Source 2](https://github.com/balalex12/trazo/blob/main/THIRD_PARTY_NOTICES.md)

### Limitations

AI is optional and off initially; non-AI imports are not described as model inference. The optional CLI bridge is experimental, and Utility Network tracing is unvalidated; neither is used as an automatic verdict on the diagram workflow. [Source 1](https://github.com/balalex12/trazo/blob/main/README.md) [Source 2](https://github.com/balalex12/trazo/blob/main/THIRD_PARTY_NOTICES.md)

### Get the tool

- [Repository](https://github.com/balalex12/trazo)
- [Documentation](https://github.com/balalex12/trazo/blob/main/README.md)

## OpenBand

Audio, music & voice · Browser tools & web media · Interactive, immersive & live media

First full guide in this library. The repository was created 2026-10-18, within the discovery window; that date does not establish a product launch or output quality.

### Quality assessment: Quality unverified

Software licensing and a concrete creative AI use are supported. The remaining checks do not establish a recommendation.

Scope: Editable MIDI arrangements, loop sketches and small collaborative music projects.

Evidence checked: 2026-10-22. No local execution implied.

- **Open-source software license · verified:** The complete root software license was read and archived. The grant covers this project code; unresolved model, service and asset terms are disclosed separately. [Source](https://github.com/iltempe/openband/blob/main/LICENSE)
- **Creative results · documented:** The README links a live studio and shows piano-roll, mixer and model-chat examples. The page was not played or benchmarked in this review. [Source](https://github.com/iltempe/openband/blob/main/README.md)
- **Reproducible setup · documented:** Use the linked browser demo or an official desktop release. For AI, configure the built-in model panel or follow the MCP connection guide. The README warns that the npm name openband belongs to a different project. Independent reproduction has not been established in this review. [Source](https://github.com/iltempe/openband/blob/main/README.md)
- **Maintenance and support · unknown:** A release or active repository alone does not establish sustained support. Workflow-specific support and unresolved blockers need a deeper review.
- **Independent use · unknown:** Independent first-hand use or a working third-party integration was not established for this selected workflow.
- **Models, services and costs · documented:** MIT covers the studio. AI service charges, local model weights, imported samples/SoundFonts and WAM plugins retain separate terms. The project says its built-in instruments are synthesized and not Apple assets. Local compute plus any chosen external model or service; provider access and charges are separate. [Source](https://github.com/iltempe/openband/blob/main/README.md)

Documentation review only; AI Media Scout did not install or run this software. Maintainer feature claims and tool counts are not independent quality evidence. Browser storage, device audio/MIDI behavior and exported-project interoperability need practical validation.

### How it uses AI

A browser music studio lets connected language-model agents compose, arrange, mix and export through its AI panel or MCP tools. [Source](https://github.com/iltempe/openband/blob/main/README.md)

### Introduction

A browser music studio lets connected language-model agents compose, arrange, mix and export through its AI panel or MCP tools. [Source 1](https://github.com/iltempe/openband/blob/main/README.md)

### What it is good for

Editable MIDI arrangements, loop sketches and small collaborative music projects. [Source 1](https://github.com/iltempe/openband/blob/main/README.md)

### Demo & examples

The README links a live studio and shows piano-roll, mixer and model-chat examples. The page was not played or benchmarked in this review. [Source 1](https://github.com/iltempe/openband/blob/main/README.md)

### Install

Use the linked browser demo or an official desktop release. For AI, configure the built-in model panel or follow the MCP connection guide. The README warns that the npm name openband belongs to a different project. [Source 1](https://github.com/iltempe/openband/blob/main/README.md)

1. Obtain the official source or release linked below.
2. Use the linked browser demo or an official desktop release. For AI, configure the built-in model panel or follow the MCP connection guide. The README warns that the npm name openband belongs to a different project.
### First project

Start with a short, representative project and inspect the result before a larger batch. [Source 1](https://github.com/iltempe/openband/blob/main/README.md)

1. Open an example song or make a short loop; the random-loop starter itself does not need AI.
2. Connect the chosen provider or local Ollama model and ask for a small change to notes, instruments or arrangement.
3. Inspect and edit the piano roll/mixer, undo unwanted edits, then export WAV, MIDI, dawproject or the native project format.
### Hardware & software

Requirements below are documented for this workflow. Unspecified limits are not inferred. [Source 1](https://github.com/iltempe/openband/blob/main/README.md)

- **Hardware:** Minimum system RAM, VRAM and total disk space are not documented in the reviewed instructions.
- **Software:** Modern browser or desktop distribution. The CLI/MCP route documents Node.js 18+; an AI provider or local model runtime is separate.
- **Platforms:** Browser operation and macOS, Windows and Linux desktop downloads are documented. Offline editing after installation does not mean cloud models run offline.

### License, model weights & costs

The full software license was reviewed. Model weights, assets and services remain separate. [Source 1](https://github.com/iltempe/openband/blob/main/LICENSE) [Source 2](https://github.com/iltempe/openband/blob/main/README.md)

- **Code:** MIT
- **Weights:** MIT covers the studio. AI service charges, local model weights, imported samples/SoundFonts and WAM plugins retain separate terms. The project says its built-in instruments are synthesized and not Apple assets.
- **Commercial:** Software use follows MIT. MIT covers the studio. AI service charges, local model weights, imported samples/SoundFonts and WAM plugins retain separate terms. The project says its built-in instruments are synthesized and not Apple assets.
- **Cost:** Local compute plus any chosen external model or service; provider access and charges are separate.

### Why it merits attention

Included for the documented creative workflow. A complete guide and popularity do not establish output reliability. [Source 1](https://github.com/iltempe/openband/blob/main/README.md)

### Limitations

Maintainer feature claims and tool counts are not independent quality evidence. Browser storage, device audio/MIDI behavior and exported-project interoperability need practical validation. [Source 1](https://github.com/iltempe/openband/blob/main/README.md)

### Get the tool

- [Repository](https://github.com/iltempe/openband)
- [Documentation](https://github.com/iltempe/openband/blob/main/README.md)

## AI Builder for Minecraft

Games & production pipelines · 3D, reconstruction & assets · Interactive, immersive & live media

First full guide in this library. The repository was created 2026-09-29, within the discovery window; that date does not establish a product launch or output quality.

### Quality assessment: Quality unverified

Software licensing and a concrete creative AI use are supported. The remaining checks do not establish a recommendation.

Scope: Prototyping game-world structures and stylized block sculptures from text or reference images.

Evidence checked: 2026-10-22. No local execution implied.

- **Open-source software license · verified:** The complete root software license was read and archived. The grant covers this project code; unresolved model, service and asset terms are disclosed separately. [Source](https://github.com/AugustZhang1/AI-Builder-Minecraft/blob/main/LICENSE)
- **Creative results · documented:** The README embeds ship, statue and revision examples from the maintainer; output fidelity and server performance were not independently checked. [Source](https://github.com/AugustZhang1/AI-Builder-Minecraft/blob/main/README.md)
- **Reproducible setup · documented:** Install alongside a Minecraft Java server, create a Python environment, install requirements, configure OpenSCAD’s Manifold backend and authenticate a supported AI CLI. Enable local RCON as documented and set the server directory. Independent reproduction has not been established in this review. [Source](https://github.com/AugustZhang1/AI-Builder-Minecraft/blob/main/README.md)
- **Maintenance and support · unknown:** A release or active repository alone does not establish sustained support. Workflow-specific support and unresolved blockers need a deeper review.
- **Independent use · unknown:** Independent first-hand use or a working third-party integration was not established for this selected workflow.
- **Models, services and costs · documented:** MIT covers the bridge; Minecraft is a separate proprietary host. AI subscriptions and optional image-to-3D model/asset terms are separate; Hugging Face access is needed for the image statue route. Local compute plus any chosen external model or service; provider access and charges are separate. [Source](https://github.com/AugustZhang1/AI-Builder-Minecraft/blob/main/README.md)

Documentation review only; AI Media Scout did not install or run this software. Build commands modify the world and require operator access. Mesh-to-block conversion does not guarantee accurate, efficient or safe placement; use a backed-up test world.

### How it uses AI

A language model writes OpenSCAD designs, which are rendered, voxelized and placed in a Minecraft Java world; a separate image-to-3D path creates statues. [Source](https://github.com/AugustZhang1/AI-Builder-Minecraft/blob/main/README.md)

### Introduction

A language model writes OpenSCAD designs, which are rendered, voxelized and placed in a Minecraft Java world; a separate image-to-3D path creates statues. [Source 1](https://github.com/AugustZhang1/AI-Builder-Minecraft/blob/main/README.md)

### What it is good for

Prototyping game-world structures and stylized block sculptures from text or reference images. [Source 1](https://github.com/AugustZhang1/AI-Builder-Minecraft/blob/main/README.md)

### Demo & examples

The README embeds ship, statue and revision examples from the maintainer; output fidelity and server performance were not independently checked. [Source 1](https://github.com/AugustZhang1/AI-Builder-Minecraft/blob/main/README.md)

### Install

Install alongside a Minecraft Java server, create a Python environment, install requirements, configure OpenSCAD’s Manifold backend and authenticate a supported AI CLI. Enable local RCON as documented and set the server directory. [Source 1](https://github.com/AugustZhang1/AI-Builder-Minecraft/blob/main/README.md)

1. Obtain the official source or release linked below.
2. Install alongside a Minecraft Java server, create a Python environment, install requirements, configure OpenSCAD’s Manifold backend and authenticate a supported AI CLI. Enable local RCON as documented and set the server directory.

```sh
python3 -m venv venv
```


```sh
venv/bin/pip install -r requirements.txt
```

### First project

Start with a short, representative project and inspect the result before a larger batch. [Source 1](https://github.com/AugustZhang1/AI-Builder-Minecraft/blob/main/README.md)

1. Use the documented --once mode for a small design preview before placing blocks in a world.
2. In a test world, an operator enters !design followed by a short structure description and inspects the preview.
3. Revise with !designfix; use !place only after reviewing the proposed structure. Pixel-art conversion is a separate non-AI operation.
### Hardware & software

Requirements below are documented for this workflow. Unspecified limits are not inferred. [Source 1](https://github.com/AugustZhang1/AI-Builder-Minecraft/blob/main/README.md)

- **Hardware:** Minimum system RAM, VRAM and total disk space are not documented in the reviewed instructions.
- **Software:** Minecraft Java 1.21.x server on the same machine, Python 3.12+, OpenSCAD with Manifold, and authenticated Claude Code or the documented Gemini CLI route.
- **Platforms:** Linux setup and a manual Windows route are documented. macOS support and numerical CPU/GPU/RAM/storage minimums are not established.

### License, model weights & costs

The full software license was reviewed. Model weights, assets and services remain separate. [Source 1](https://github.com/AugustZhang1/AI-Builder-Minecraft/blob/main/LICENSE) [Source 2](https://github.com/AugustZhang1/AI-Builder-Minecraft/blob/main/README.md)

- **Code:** MIT
- **Weights:** MIT covers the bridge; Minecraft is a separate proprietary host. AI subscriptions and optional image-to-3D model/asset terms are separate; Hugging Face access is needed for the image statue route.
- **Commercial:** Software use follows MIT. MIT covers the bridge; Minecraft is a separate proprietary host. AI subscriptions and optional image-to-3D model/asset terms are separate; Hugging Face access is needed for the image statue route.
- **Cost:** Local compute plus any chosen external model or service; provider access and charges are separate.

### Why it merits attention

Included for the documented creative workflow. A complete guide and popularity do not establish output reliability. [Source 1](https://github.com/AugustZhang1/AI-Builder-Minecraft/blob/main/README.md)

### Limitations

Build commands modify the world and require operator access. Mesh-to-block conversion does not guarantee accurate, efficient or safe placement; use a backed-up test world. [Source 1](https://github.com/AugustZhang1/AI-Builder-Minecraft/blob/main/README.md)

### Get the tool

- [Repository](https://github.com/AugustZhang1/AI-Builder-Minecraft)
- [Documentation](https://github.com/AugustZhang1/AI-Builder-Minecraft/blob/main/README.md)

## Sprite Studio

Games & production pipelines · Images & design · Motion capture & character animation · VFX, compositing & relighting

First full guide in this library. The repository was created 2026-10-13, within the discovery window; that date does not establish a product launch or output quality.

### Quality assessment: Quality unverified

Software licensing and a concrete creative AI use are supported. The remaining checks do not establish a recommendation.

Scope: Editable game sprites, layered raster rigs and VFX packs exported to multiple engines.

Evidence checked: 2026-10-22. No local execution implied.

- **Open-source software license · verified:** The complete root software license was read and archived. The grant covers this project code; unresolved model, service and asset terms are disclosed separately. [Source](https://github.com/lenhonbp/sprite-studio/blob/main/LICENSE)
- **Creative results · documented:** The README describes a combat-VFX sample and field-test records, while explicitly labeling the sample art unreviewed. No engine integration was executed here. [Source](https://github.com/lenhonbp/sprite-studio/blob/main/README.md)
- **Reproducible setup · documented:** Open the official offline HTML release, or clone the source and run the Node local server. The agent art toolkit additionally needs Python and Pillow; connect a compatible agent separately. Independent reproduction has not been established in this review. [Source](https://github.com/lenhonbp/sprite-studio/blob/main/README.md)
- **Maintenance and support · unknown:** A release or active repository alone does not establish sustained support. Workflow-specific support and unresolved blockers need a deeper review.
- **Independent use · unknown:** Independent first-hand use or a working third-party integration was not established for this selected workflow.
- **Models, services and costs · documented:** MIT covers the project. AI-agent access, any external image model, imported art and target engine licenses are separate; sample art is not certified production-ready. Local compute plus any chosen external model or service; provider access and charges are separate. [Source](https://github.com/lenhonbp/sprite-studio/blob/main/README.md)

Documentation review only; AI Media Scout did not install or run this software. Automated pack checks establish file/contract properties, not artistic quality or universal engine parity. Much of the deeper documentation is in Vietnamese.

### How it uses AI

An agent-facing production skill and MCP/CLI workflow coordinate sprite creation, rig edits, VFX authoring and asset checks. [Source](https://github.com/lenhonbp/sprite-studio/blob/main/README.md)

### Introduction

An agent-facing production skill and MCP/CLI workflow coordinate sprite creation, rig edits, VFX authoring and asset checks. [Source 1](https://github.com/lenhonbp/sprite-studio/blob/main/README.md)

### What it is good for

Editable game sprites, layered raster rigs and VFX packs exported to multiple engines. [Source 1](https://github.com/lenhonbp/sprite-studio/blob/main/README.md)

### Demo & examples

The README describes a combat-VFX sample and field-test records, while explicitly labeling the sample art unreviewed. No engine integration was executed here. [Source 1](https://github.com/lenhonbp/sprite-studio/blob/main/README.md)

### Install

Open the official offline HTML release, or clone the source and run the Node local server. The agent art toolkit additionally needs Python and Pillow; connect a compatible agent separately. [Source 1](https://github.com/lenhonbp/sprite-studio/blob/main/README.md)

1. Obtain the official source or release linked below.
2. Open the official offline HTML release, or clone the source and run the Node local server. The agent art toolkit additionally needs Python and Pillow; connect a compatible agent separately.

```sh
npm start
```

### First project

Start with a short, representative project and inspect the result before a larger batch. [Source 1](https://github.com/lenhonbp/sprite-studio/blob/main/README.md)

1. Open the sample project or import your own PNG layers, then inspect the rig and pivots.
2. Use the agent workflow or manual editor to make a small animation/VFX change and preview timing and transparency.
3. Select the intended engine adapter, export the pack, and check it in that engine before production use.
### Hardware & software

Requirements below are documented for this workflow. Unspecified limits are not inferred. [Source 1](https://github.com/lenhonbp/sprite-studio/blob/main/README.md)

- **Hardware:** Minimum system RAM, VRAM and total disk space are not documented in the reviewed instructions.
- **Software:** Offline HTML needs a desktop browser. Local server: Node.js 22+; selected adapter checks use 22.13+. Agent toolkit: Python 3.10+ and Pillow.
- **Platforms:** The offline editor names desktop Chrome, Edge, Firefox and Safari. Native OS version requirements and individual engine compatibility need the adapter guide.

### License, model weights & costs

The full software license was reviewed. Model weights, assets and services remain separate. [Source 1](https://github.com/lenhonbp/sprite-studio/blob/main/LICENSE) [Source 2](https://github.com/lenhonbp/sprite-studio/blob/main/README.md)

- **Code:** MIT
- **Weights:** MIT covers the project. AI-agent access, any external image model, imported art and target engine licenses are separate; sample art is not certified production-ready.
- **Commercial:** Software use follows MIT. MIT covers the project. AI-agent access, any external image model, imported art and target engine licenses are separate; sample art is not certified production-ready.
- **Cost:** Local compute plus any chosen external model or service; provider access and charges are separate.

### Why it merits attention

Included for the documented creative workflow. A complete guide and popularity do not establish output reliability. [Source 1](https://github.com/lenhonbp/sprite-studio/blob/main/README.md)

### Limitations

Automated pack checks establish file/contract properties, not artistic quality or universal engine parity. Much of the deeper documentation is in Vietnamese. [Source 1](https://github.com/lenhonbp/sprite-studio/blob/main/README.md)

### Get the tool

- [Repository](https://github.com/lenhonbp/sprite-studio)
- [Documentation](https://github.com/lenhonbp/sprite-studio/blob/main/README.md)

## Nuzky

Video, animation & film · Editing, captions & post-production · Accessible media & assistive creation

First full guide in this library. The repository was created 2026-10-06, within the discovery window; that date does not establish a product launch or output quality.

### Quality assessment: Experimental

Software licensing and a concrete creative AI use are supported. The remaining checks do not establish a recommendation.

Scope: Captioned talking-head shorts and transcript-driven editing experiments.

Evidence checked: 2026-10-22. No local execution implied.

Why Experimental: The current README explicitly labels Nuzky alpha, warns of rough edges and documents incomplete platform validation and disabled Windows AI editing. https://github.com/nuzkyapp/nuzky/blob/main/README.md

- **Open-source software license · verified:** The complete root software license was read and archived. The grant covers this project code; unresolved model, service and asset terms are disclosed separately. [Source](https://github.com/nuzkyapp/nuzky/blob/main/LICENSE)
- **Creative results · documented:** The README warns that its editor illustration differs from the alpha. Maintainer tests are strongest on macOS; no hands-on evaluation was performed here. [Source](https://github.com/nuzkyapp/nuzky/blob/main/README.md)
- **Reproducible setup · documented:** Download the appropriate official installer and review its platform status. The first transcript downloads a speech model. Source builds require the documented Rust/Node/FFmpeg toolchain; AI editing needs a separate authenticated agent. Independent reproduction has not been established in this review. [Source](https://github.com/nuzkyapp/nuzky/blob/main/README.md)
- **Maintenance and support · unknown:** A release or active repository alone does not establish sustained support. Workflow-specific support and unresolved blockers need a deeper review.
- **Independent use · unknown:** Independent first-hand use or a working third-party integration was not established for this selected workflow.
- **Models, services and costs · documented:** GPL-3.0-or-later code, separate FFmpeg/component terms, CC0 sounds/stickers and a CC BY 3.0 sample clip are documented. Speech models and external agent providers have separate terms; connected agents may send project context to their provider. Local compute plus any chosen external model or service; provider access and charges are separate. [Source](https://github.com/nuzkyapp/nuzky/blob/main/README.md)

Documentation review only; AI Media Scout did not install or run this software. The release is explicitly alpha with rough edges and material platform limitations. Export is MP4-only; there is no phone app or template library.

### How it uses AI

Local Whisper transcription drives text-based video cuts and captions, while connected agents can edit the timeline through the same project interface. [Source](https://github.com/nuzkyapp/nuzky/blob/main/README.md)

### Introduction

Local Whisper transcription drives text-based video cuts and captions, while connected agents can edit the timeline through the same project interface. [Source 1](https://github.com/nuzkyapp/nuzky/blob/main/README.md)

### What it is good for

Captioned talking-head shorts and transcript-driven editing experiments. [Source 1](https://github.com/nuzkyapp/nuzky/blob/main/README.md)

### Demo & examples

The README warns that its editor illustration differs from the alpha. Maintainer tests are strongest on macOS; no hands-on evaluation was performed here. [Source 1](https://github.com/nuzkyapp/nuzky/blob/main/README.md)

### Install

Download the appropriate official installer and review its platform status. The first transcript downloads a speech model. Source builds require the documented Rust/Node/FFmpeg toolchain; AI editing needs a separate authenticated agent. [Source 1](https://github.com/nuzkyapp/nuzky/blob/main/README.md)

1. Obtain the official source or release linked below.
2. Download the appropriate official installer and review its platform status. The first transcript downloads a speech model. Source builds require the documented Rust/Node/FFmpeg toolchain; AI editing needs a separate authenticated agent.
### First project

Start with a short, representative project and inspect the result before a larger batch. [Source 1](https://github.com/nuzkyapp/nuzky/blob/main/README.md)

1. Create a test project, import a short talking clip, and download the speech model when prompted.
2. Generate a transcript, inspect recognition, then remove a small pause or word range and check the corresponding edit.
3. Review captions and audio, then export an MP4 using the appropriate portrait/landscape preset. Connect AI editing only on a supported route.
### Hardware & software

Requirements below are documented for this workflow. Unspecified limits are not inferred. [Source 1](https://github.com/nuzkyapp/nuzky/blob/main/README.md)

- **Hardware:** Minimum system RAM, VRAM and total disk space are not documented in the reviewed instructions.
- **Software:** Packaged app; source development requires Rust >=1.94, Node.js 22.12+, FFmpeg headers/libraries, clang and cmake; Linux adds ALSA and WebKitGTK 4.1.
- **Platforms:** macOS 14+ Apple Silicon is maintainer-tested; Linux x86_64 is partly tested, with Ubuntu 24.04+/glibc 2.39+ documented. Windows 10/11 x64 is untested, AI editing is disabled there and transcription uses CPU. Intel Mac and ARM Linux/Windows are unsupported.

### License, model weights & costs

The full software license was reviewed. Model weights, assets and services remain separate. [Source 1](https://github.com/nuzkyapp/nuzky/blob/main/LICENSE) [Source 2](https://github.com/nuzkyapp/nuzky/blob/main/README.md)

- **Code:** GPL-3.0
- **Weights:** GPL-3.0-or-later code, separate FFmpeg/component terms, CC0 sounds/stickers and a CC BY 3.0 sample clip are documented. Speech models and external agent providers have separate terms; connected agents may send project context to their provider.
- **Commercial:** Software use follows GPL-3.0. GPL-3.0-or-later code, separate FFmpeg/component terms, CC0 sounds/stickers and a CC BY 3.0 sample clip are documented. Speech models and external agent providers have separate terms; connected agents may send project context to their provider.
- **Cost:** Local compute plus any chosen external model or service; provider access and charges are separate.

### Why it merits attention

Included for the documented creative workflow. A complete guide and popularity do not establish output reliability. [Source 1](https://github.com/nuzkyapp/nuzky/blob/main/README.md)

### Limitations

The release is explicitly alpha with rough edges and material platform limitations. Export is MP4-only; there is no phone app or template library. [Source 1](https://github.com/nuzkyapp/nuzky/blob/main/README.md)

### Get the tool

- [Repository](https://github.com/nuzkyapp/nuzky)
- [Documentation](https://github.com/nuzkyapp/nuzky/blob/main/README.md)

## Stable Illusion

Images & design

First full guide in this library, establishing a documentation baseline; not a claim of a launch or significant update today.

### Quality assessment: Quality unverified

Software licensing and a concrete creative AI use are supported. The remaining checks do not establish a recommendation.

Scope: Local prompt-to-image experiments in a native Windows interface.

Evidence checked: 2026-10-22. No local execution implied.

- **Open-source software license · verified:** The complete root software license was read and archived. The grant covers this project code; unresolved model, service and asset terms are disclosed separately. [Source](https://github.com/tslothorst/StableIllusion/blob/master/LICENSE)
- **Creative results · unknown:** The README describes generation controls and saving/copying the result; a current representative output gallery was not established in this review. [Source](https://github.com/tslothorst/StableIllusion/blob/master/README.md)
- **Reproducible setup · documented:** Install the appropriate .NET runtime/SDK, build the solution, obtain compatible ONNX-format Stable Diffusion components, and point appsettings.json at their paths. Check the current upstream model locations; the README’s clone example contains a duplicated git token. Independent reproduction has not been established in this review. [Source](https://github.com/tslothorst/StableIllusion/blob/master/README.md)
- **Maintenance and support · unknown:** A release or active repository alone does not establish sustained support. Workflow-specific support and unresolved blockers need a deeper review.
- **Independent use · unknown:** Independent first-hand use or a working third-party integration was not established for this selected workflow.
- **Models, services and costs · documented:** The app is MIT. Stable Diffusion weights retain their own license and use restrictions; model downloads and CUDA components are separate from the app grant. Local compute plus any chosen external model or service; provider access and charges are separate. [Source](https://github.com/tslothorst/StableIllusion/blob/master/README.md)

Documentation review only; AI Media Scout did not install or run this software. This is an older workflow with unverified current dependency/model-host compatibility. Tested hardware is not a minimum specification, and generation quality was not verified.

### How it uses AI

A Windows WPF interface runs Stable Diffusion through ONNX Runtime to generate images from prompts. [Source](https://github.com/tslothorst/StableIllusion/blob/master/README.md)

### Introduction

A Windows WPF interface runs Stable Diffusion through ONNX Runtime to generate images from prompts. [Source 1](https://github.com/tslothorst/StableIllusion/blob/master/README.md)

### What it is good for

Local prompt-to-image experiments in a native Windows interface. [Source 1](https://github.com/tslothorst/StableIllusion/blob/master/README.md)

### Demo & examples

The README describes generation controls and saving/copying the result; a current representative output gallery was not established in this review. [Source 1](https://github.com/tslothorst/StableIllusion/blob/master/README.md)

### Install

Install the appropriate .NET runtime/SDK, build the solution, obtain compatible ONNX-format Stable Diffusion components, and point appsettings.json at their paths. Check the current upstream model locations; the README’s clone example contains a duplicated git token. [Source 1](https://github.com/tslothorst/StableIllusion/blob/master/README.md)

1. Obtain the official source or release linked below.
2. Install the appropriate .NET runtime/SDK, build the solution, obtain compatible ONNX-format Stable Diffusion components, and point appsettings.json at their paths. Check the current upstream model locations; the README’s clone example contains a duplicated git token.

```sh
dotnet build --configuration Release
```

### First project

Start with a short, representative project and inspect the result before a larger batch. [Source 1](https://github.com/tslothorst/StableIllusion/blob/master/README.md)

1. Configure paths for the text encoder, UNet, VAE and safety model.
2. Launch the built executable, choose the available execution provider, enter a short prompt and generate an image.
3. Compare step/guidance settings and save the result; the CPU route is explicitly untested by the maintainer.
### Hardware & software

Requirements below are documented for this workflow. Unspecified limits are not inferred. [Source 1](https://github.com/tslothorst/StableIllusion/blob/master/README.md)

- **Hardware:** Maintainer testing used an RTX 3080 with 12 GB VRAM. The README reports roughly 16 GB RAM during generation and recommends 32 GB; it does not guarantee operation below that test setup or document total disk needs.
- **Software:** .NET 6 runtime or SDK and compatible ONNX Runtime; optional NVIDIA CUDA/cuDNN; Stable Diffusion 1.4/1.5 ONNX models.
- **Platforms:** Windows is documented. macOS and Linux support are not established for this WPF application.

### License, model weights & costs

The full software license was reviewed. Model weights, assets and services remain separate. [Source 1](https://github.com/tslothorst/StableIllusion/blob/master/LICENSE) [Source 2](https://github.com/tslothorst/StableIllusion/blob/master/README.md)

- **Code:** MIT
- **Weights:** The app is MIT. Stable Diffusion weights retain their own license and use restrictions; model downloads and CUDA components are separate from the app grant.
- **Commercial:** Software use follows MIT. The app is MIT. Stable Diffusion weights retain their own license and use restrictions; model downloads and CUDA components are separate from the app grant.
- **Cost:** Local compute plus any chosen external model or service; provider access and charges are separate.

### Why it merits attention

Included for the documented creative workflow. A complete guide and popularity do not establish output reliability. [Source 1](https://github.com/tslothorst/StableIllusion/blob/master/README.md)

### Limitations

This is an older workflow with unverified current dependency/model-host compatibility. Tested hardware is not a minimum specification, and generation quality was not verified. [Source 1](https://github.com/tslothorst/StableIllusion/blob/master/README.md)

### Get the tool

- [Repository](https://github.com/tslothorst/StableIllusion)
- [Documentation](https://github.com/tslothorst/StableIllusion/blob/master/README.md)

## HO[LO] Desk

Audio, music & voice · Browser tools & web media · Interactive, immersive & live media

First full guide in this library. The repository was created 2026-10-17, within the discovery window; that date does not establish a product launch or output quality.

### Quality assessment: Quality unverified

Software licensing and a concrete creative AI use are supported. The remaining checks do not establish a recommendation.

Scope: Browser-based music composition, recording and editable AI-assisted arrangements.

Evidence checked: 2026-10-22. No local execution implied.

- **Open-source software license · verified:** The complete root software license was read and archived. The grant covers this project code; unresolved model, service and asset terms are disclosed separately. [Source](https://github.com/shooter-git/holo-desk/blob/main/LICENSE)
- **Creative results · documented:** The README shows the studio, mobile layout and remote controller; latency and sound quality claims are maintainer descriptions, not independently tested results. [Source](https://github.com/shooter-git/holo-desk/blob/main/README.md)
- **Reproducible setup · documented:** Install Node.js 24+ and pnpm 10, clone the source, install dependencies, copy the example configuration and fetch desired sample packs. Build/start the studio, then install the optional AI integration only if needed. Independent reproduction has not been established in this review. [Source](https://github.com/shooter-git/holo-desk/blob/main/README.md)
- **Maintenance and support · unknown:** A release or active repository alone does not establish sustained support. Workflow-specific support and unresolved blockers need a deeper review.
- **Independent use · unknown:** Independent first-hand use or a working third-party integration was not established for this selected workflow.
- **Models, services and costs · documented:** MIT covers studio code. The project identifies its sample packs as CC0 but imported packs retain their own terms. Claude service access and optional Tailscale networking are separate dependencies. Local compute plus any chosen external model or service; provider access and charges are separate. [Source](https://github.com/shooter-git/holo-desk/blob/main/README.md)

Documentation review only; AI Media Scout did not install or run this software. Low-latency figures vary by device and are not generalized guarantees. Windows exclusive audio can silence other applications; remote-device use has separate networking and MIDI setup.

### How it uses AI

A Claude Code integration reads an open music session and makes undoable arrangement, harmony and mixing changes through the studio’s tools. [Source](https://github.com/shooter-git/holo-desk/blob/main/README.md)

### Introduction

A Claude Code integration reads an open music session and makes undoable arrangement, harmony and mixing changes through the studio’s tools. [Source 1](https://github.com/shooter-git/holo-desk/blob/main/README.md)

### What it is good for

Browser-based music composition, recording and editable AI-assisted arrangements. [Source 1](https://github.com/shooter-git/holo-desk/blob/main/README.md)

### Demo & examples

The README shows the studio, mobile layout and remote controller; latency and sound quality claims are maintainer descriptions, not independently tested results. [Source 1](https://github.com/shooter-git/holo-desk/blob/main/README.md)

### Install

Install Node.js 24+ and pnpm 10, clone the source, install dependencies, copy the example configuration and fetch desired sample packs. Build/start the studio, then install the optional AI integration only if needed. [Source 1](https://github.com/shooter-git/holo-desk/blob/main/README.md)

1. Obtain the official source or release linked below.
2. Install Node.js 24+ and pnpm 10, clone the source, install dependencies, copy the example configuration and fetch desired sample packs. Build/start the studio, then install the optional AI integration only if needed.

```sh
pnpm install
```


```sh
cp .env.example .env
```


```sh
pnpm packs install
```


```sh
pnpm build
```


```sh
pnpm start
```

### First project

Start with a short, representative project and inspect the result before a larger batch. [Source 1](https://github.com/shooter-git/holo-desk/blob/main/README.md)

1. Open localhost:47800, start the studio and create a short instrument part or import audio.
2. Connect the documented AI skill, ask for a bounded harmony/arrangement change and inspect the resulting notes and undo step.
3. Adjust the mix and bounce a WAV; verify it before moving the song to another project or device.
### Hardware & software

Requirements below are documented for this workflow. Unspecified limits are not inferred. [Source 1](https://github.com/shooter-git/holo-desk/blob/main/README.md)

- **Hardware:** Sample-library installation can consume several GB. Minimum RAM, VRAM, processor and total disk capacity are not documented; microphones/MIDI/audio interfaces are optional workflow hardware.
- **Software:** Node.js 24+, pnpm 10 or the Docker route. Browser audio/MIDI features need a secure context; AI use needs a configured Claude Code account. Native companion builds require Zig 0.16 or an appropriate C compiler.
- **Platforms:** Browser/tablet/phone use is documented, with separate Windows x64, macOS ARM64/x64 and Linux x64 native audio companions. Device MIDI paths differ, including a separate iOS network-MIDI route.

### License, model weights & costs

The full software license was reviewed. Model weights, assets and services remain separate. [Source 1](https://github.com/shooter-git/holo-desk/blob/main/LICENSE) [Source 2](https://github.com/shooter-git/holo-desk/blob/main/README.md)

- **Code:** MIT
- **Weights:** MIT covers studio code. The project identifies its sample packs as CC0 but imported packs retain their own terms. Claude service access and optional Tailscale networking are separate dependencies.
- **Commercial:** Software use follows MIT. MIT covers studio code. The project identifies its sample packs as CC0 but imported packs retain their own terms. Claude service access and optional Tailscale networking are separate dependencies.
- **Cost:** Local compute plus any chosen external model or service; provider access and charges are separate.

### Why it merits attention

Included for the documented creative workflow. A complete guide and popularity do not establish output reliability. [Source 1](https://github.com/shooter-git/holo-desk/blob/main/README.md)

### Limitations

Low-latency figures vary by device and are not generalized guarantees. Windows exclusive audio can silence other applications; remote-device use has separate networking and MIDI setup. [Source 1](https://github.com/shooter-git/holo-desk/blob/main/README.md)

### Get the tool

- [Repository](https://github.com/shooter-git/holo-desk)
- [Documentation](https://github.com/shooter-git/holo-desk/blob/main/README.md)

## Additional open-source AI discoveries

Creative AI relevance and software license screened. Full installation, requirements and quality profiles are pending.

### Threlte Live · AGPL-3.0

Interactive voiced VRM character experiments.
A VRM streaming interface connects Google generative chat to ElevenLabs speech and phoneme-driven avatar lip sync.
Full setup, hardware, model-term and output-quality review pending. AGPL app; Google/ElevenLabs services, avatar assets and Mixamo animation rights are separate. Node 18+/pnpm are documented; hardware and independent lip-sync review remain pending.

### Quality assessment: Quality unverified

Software license and creative AI relevance screened; full guide and quality checks remain pending.

Scope: Interactive voiced VRM character experiments.

Evidence checked: 2026-10-22. No local execution implied.

- **Open-source software license · verified:** Complete software license read and archived; this grant does not cover separate models, services or assets. [Source](https://github.com/dexvdev/svelte-vrm-live/blob/main/LICENSE)
- **Creative results · unknown:** Published creative results have not received a substantive independent quality review.
- **Reproducible setup · unknown:** A complete installation and reproducibility review is pending.
- **Maintenance and support · unknown:** Workflow-specific maintenance and blocker review remains incomplete.
- **Independent use · unknown:** Independent first-hand use has not been established in this review.
- **Models, services and costs · documented:** AGPL app; Google/ElevenLabs services, avatar assets and Mixamo animation rights are separate. Node 18+/pnpm are documented; hardware and independent lip-sync review remain pending. [Source](https://github.com/dexvdev/svelte-vrm-live/blob/main/README.md)

Source review only; not installed or run. AGPL app; Google/ElevenLabs services, avatar assets and Mixamo animation rights are separate. Node 18+/pnpm are documented; hardware and independent lip-sync review remain pending.

- [Official documentation](https://github.com/dexvdev/svelte-vrm-live/blob/main/README.md)
- [Complete software license reviewed](https://github.com/dexvdev/svelte-vrm-live/blob/main/LICENSE)
### Native Media AI Studio · MIT

Organizing AI-assisted music-video drafts and beat-based visual edits.
A local pipeline combines Demucs/Whisper analysis and ComfyUI generation with music-video editing and audio-reactive scenes.
Full setup, hardware, model-term and output-quality review pending. MIT original code; Remotion is explicitly source-available with paid company conditions, madmom weights are noncommercial, and Unity/models/assets retain separate terms. The 8 GB GPU and 32 GB RAM machine is a target, not a verified universal minimum.

### Quality assessment: Quality unverified

Software license and creative AI relevance screened; full guide and quality checks remain pending.

Scope: Organizing AI-assisted music-video drafts and beat-based visual edits.

Evidence checked: 2026-10-22. No local execution implied.

- **Open-source software license · verified:** Complete software license read and archived; this grant does not cover separate models, services or assets. [Source](https://github.com/ogneocortext/Native-Media-AI-Studio/blob/main/LICENSE)
- **Creative results · unknown:** Published creative results have not received a substantive independent quality review.
- **Reproducible setup · unknown:** A complete installation and reproducibility review is pending.
- **Maintenance and support · unknown:** Workflow-specific maintenance and blocker review remains incomplete.
- **Independent use · unknown:** Independent first-hand use has not been established in this review.
- **Models, services and costs · documented:** MIT original code; Remotion is explicitly source-available with paid company conditions, madmom weights are noncommercial, and Unity/models/assets retain separate terms. The 8 GB GPU and 32 GB RAM machine is a target, not a verified universal minimum. [Source](https://github.com/ogneocortext/Native-Media-AI-Studio/blob/main/README.md)

Source review only; not installed or run. MIT original code; Remotion is explicitly source-available with paid company conditions, madmom weights are noncommercial, and Unity/models/assets retain separate terms. The 8 GB GPU and 32 GB RAM machine is a target, not a verified universal minimum.

- [Official documentation](https://github.com/ogneocortext/Native-Media-AI-Studio/blob/main/README.md)
- [Complete software license reviewed](https://github.com/ogneocortext/Native-Media-AI-Studio/blob/main/LICENSE)
### AIMovieStorage · MIT

Planning shots and keeping generated takes attached to character and scene references.
A Windows workbench combines AI screenplay/reference analysis with local image/video/music engines and 3D shot blocking.
Full setup, hardware, model-term and output-quality review pending. Windows 10/11 x64, WebView2 and engine-specific NVIDIA CUDA requirements. Models have separate licenses, API assistance is optional and paid separately. Real-output validation of local generation remains unfinished.

### Quality assessment: Experimental

Software license and creative AI relevance screened; full guide and quality checks remain pending.

Scope: Planning shots and keeping generated takes attached to character and scene references.

Evidence checked: 2026-10-22. No local execution implied.

Why Experimental: The current beta notice explicitly says local model generation is still being checked against real output and not every path has been exercised end to end. https://github.com/raonolje/AIMovieStorage/blob/main/README.md

- **Open-source software license · verified:** Complete software license read and archived; this grant does not cover separate models, services or assets. [Source](https://github.com/raonolje/AIMovieStorage/blob/main/LICENSE)
- **Creative results · unknown:** Published creative results have not received a substantive independent quality review.
- **Reproducible setup · unknown:** A complete installation and reproducibility review is pending.
- **Maintenance and support · unknown:** Workflow-specific maintenance and blocker review remains incomplete.
- **Independent use · unknown:** Independent first-hand use has not been established in this review.
- **Models, services and costs · documented:** Windows 10/11 x64, WebView2 and engine-specific NVIDIA CUDA requirements. Models have separate licenses, API assistance is optional and paid separately. Real-output validation of local generation remains unfinished. [Source](https://github.com/raonolje/AIMovieStorage/blob/main/README.md)

Source review only; not installed or run. Windows 10/11 x64, WebView2 and engine-specific NVIDIA CUDA requirements. Models have separate licenses, API assistance is optional and paid separately. Real-output validation of local generation remains unfinished.

- [Official documentation](https://github.com/raonolje/AIMovieStorage/blob/main/README.md)
- [Complete software license reviewed](https://github.com/raonolje/AIMovieStorage/blob/main/LICENSE)
### reverse3d · Apache-2.0

Exploring photo-to-relief, measured model reconstruction and editable CAD drafts.
An AI-agent CAD/reconstruction toolkit combines learned image depth with mesh, photogrammetry and parametric modeling operations.
Full setup, hardware, model-term and output-quality review pending. Apache-2.0 core; external Blender/COLMAP and model weights differ. The notice distinguishes permissive Depth Anything V2 Small from noncommercial Base/Large. Broad setup scripts can alter multiple agent configurations; full setup review remains pending. Geometry output is not fabrication validation.

### Quality assessment: Quality unverified

Software license and creative AI relevance screened; full guide and quality checks remain pending.

Scope: Exploring photo-to-relief, measured model reconstruction and editable CAD drafts.

Evidence checked: 2026-10-22. No local execution implied.

- **Open-source software license · verified:** Complete software license read and archived; this grant does not cover separate models, services or assets. [Source](https://github.com/rellytechgame/Reverse3D-tool/blob/main/LICENSE)
- **Creative results · unknown:** Published creative results have not received a substantive independent quality review.
- **Reproducible setup · unknown:** A complete installation and reproducibility review is pending.
- **Maintenance and support · unknown:** Workflow-specific maintenance and blocker review remains incomplete.
- **Independent use · unknown:** Independent first-hand use has not been established in this review.
- **Models, services and costs · documented:** Apache-2.0 core; external Blender/COLMAP and model weights differ. The notice distinguishes permissive Depth Anything V2 Small from noncommercial Base/Large. Broad setup scripts can alter multiple agent configurations; full setup review remains pending. Geometry output is not fabrication validation. [Source](https://github.com/rellytechgame/Reverse3D-tool/blob/main/README.md)

Source review only; not installed or run. Apache-2.0 core; external Blender/COLMAP and model weights differ. The notice distinguishes permissive Depth Anything V2 Small from noncommercial Base/Large. Broad setup scripts can alter multiple agent configurations; full setup review remains pending. Geometry output is not fabrication validation.

- [Official documentation](https://github.com/rellytechgame/Reverse3D-tool/blob/main/README.md)
- [Complete software license reviewed](https://github.com/rellytechgame/Reverse3D-tool/blob/main/LICENSE)
### Seiðr-Smiðja · Apache-2.0

Programmatic VRM character variations and reviewed avatar assembly.
An agent-facing avatar pipeline builds from YAML specifications, renders previews and supports an AI visual critique/revision loop.
Full setup, hardware, model-term and output-quality review pending. Apache-2.0 current code, despite a historical TBD badge. Blender, VRoid host, base meshes and model/agent services have separate requirements and terms. Historical unfinished notes are not treated as a current Experimental verdict; live Blender/VRoid integration evidence remains incomplete.

### Quality assessment: Quality unverified

Software license and creative AI relevance screened; full guide and quality checks remain pending.

Scope: Programmatic VRM character variations and reviewed avatar assembly.

Evidence checked: 2026-10-22. No local execution implied.

- **Open-source software license · verified:** Complete software license read and archived; this grant does not cover separate models, services or assets. [Source](https://github.com/hrabanazviking/Seidr-Smidja/blob/development/LICENSE)
- **Creative results · unknown:** Published creative results have not received a substantive independent quality review.
- **Reproducible setup · unknown:** A complete installation and reproducibility review is pending.
- **Maintenance and support · unknown:** Workflow-specific maintenance and blocker review remains incomplete.
- **Independent use · unknown:** Independent first-hand use has not been established in this review.
- **Models, services and costs · documented:** Apache-2.0 current code, despite a historical TBD badge. Blender, VRoid host, base meshes and model/agent services have separate requirements and terms. Historical unfinished notes are not treated as a current Experimental verdict; live Blender/VRoid integration evidence remains incomplete. [Source](https://github.com/hrabanazviking/Seidr-Smidja/blob/development/README.md)

Source review only; not installed or run. Apache-2.0 current code, despite a historical TBD badge. Blender, VRoid host, base meshes and model/agent services have separate requirements and terms. Historical unfinished notes are not treated as a current Experimental verdict; live Blender/VRoid integration evidence remains incomplete.

- [Official documentation](https://github.com/hrabanazviking/Seidr-Smidja/blob/development/README.md)
- [Complete software license reviewed](https://github.com/hrabanazviking/Seidr-Smidja/blob/development/LICENSE)
### Kaolin · Apache-2.0

Building research-backed 3D asset, Gaussian and neural-rendering prototypes.
A PyTorch library provides neural 3D representations, differentiable rendering and learned representation-based simulation modules.
Full setup, hardware, model-term and output-quality review pending. Apache-2.0 default library. Legacy non_commercial import paths retain different terms; use the current permissive modules. GPU/PyTorch compatibility and sample-model terms need a complete workflow review. An optional experimental Newton coupling does not label the entire library Experimental.

### Quality assessment: Quality unverified

Software license and creative AI relevance screened; full guide and quality checks remain pending.

Scope: Building research-backed 3D asset, Gaussian and neural-rendering prototypes.

Evidence checked: 2026-10-22. No local execution implied.

- **Open-source software license · verified:** Complete software license read and archived; this grant does not cover separate models, services or assets. [Source](https://github.com/NVIDIAGameWorks/kaolin/blob/master/LICENSE)
- **Creative results · unknown:** Published creative results have not received a substantive independent quality review.
- **Reproducible setup · unknown:** A complete installation and reproducibility review is pending.
- **Maintenance and support · unknown:** Workflow-specific maintenance and blocker review remains incomplete.
- **Independent use · unknown:** Independent first-hand use has not been established in this review.
- **Models, services and costs · documented:** Apache-2.0 default library. Legacy non_commercial import paths retain different terms; use the current permissive modules. GPU/PyTorch compatibility and sample-model terms need a complete workflow review. An optional experimental Newton coupling does not label the entire library Experimental. [Source](https://github.com/NVIDIAGameWorks/kaolin/blob/master/README.md)

Source review only; not installed or run. Apache-2.0 default library. Legacy non_commercial import paths retain different terms; use the current permissive modules. GPU/PyTorch compatibility and sample-model terms need a complete workflow review. An optional experimental Newton coupling does not label the entire library Experimental.

- [Official documentation](https://github.com/NVIDIAGameWorks/kaolin/blob/master/README.md)
- [Complete software license reviewed](https://github.com/NVIDIAGameWorks/kaolin/blob/master/LICENSE)
### LongLive · Apache-2.0

Exploring longer AI video sequences and controllable generative scene experiments.
A collection of long-context video-generation implementations provides autoregressive generation, distillation and related world-model infrastructure.
Full setup, hardware, model-term and output-quality review pending. Apache-2.0 root code; each subproject has its own environment, model weights and documentation. The creative scope here is video generation, not a claim of deployable robotics. Memory and model-term review remains pending.

### Quality assessment: Quality unverified

Software license and creative AI relevance screened; full guide and quality checks remain pending.

Scope: Exploring longer AI video sequences and controllable generative scene experiments.

Evidence checked: 2026-10-22. No local execution implied.

- **Open-source software license · verified:** Complete software license read and archived; this grant does not cover separate models, services or assets. [Source](https://github.com/NVlabs/LongLive/blob/main/LICENSE)
- **Creative results · unknown:** Published creative results have not received a substantive independent quality review.
- **Reproducible setup · unknown:** A complete installation and reproducibility review is pending.
- **Maintenance and support · unknown:** Workflow-specific maintenance and blocker review remains incomplete.
- **Independent use · unknown:** Independent first-hand use has not been established in this review.
- **Models, services and costs · documented:** Apache-2.0 root code; each subproject has its own environment, model weights and documentation. The creative scope here is video generation, not a claim of deployable robotics. Memory and model-term review remains pending. [Source](https://github.com/NVlabs/LongLive/blob/main/README.md)

Source review only; not installed or run. Apache-2.0 root code; each subproject has its own environment, model weights and documentation. The creative scope here is video generation, not a claim of deployable robotics. Memory and model-term review remains pending.

- [Official documentation](https://github.com/NVlabs/LongLive/blob/main/README.md)
- [Complete software license reviewed](https://github.com/NVlabs/LongLive/blob/main/LICENSE)
### Matrix-Game · MIT

Testing neural visual treatments for playable game environments.
Interactive world models combine game-engine state and player input with learned streaming video rendering.
Full setup, hardware, model-term and output-quality review pending. The root MIT license covers earlier versions; version 4 has a separately reviewed Apache-2.0 license. Model weights and game assets retain their terms. Advertised FPS excludes video I/O and depends on exact hardware/settings; full setup and independent gameplay review remain pending.

### Quality assessment: Quality unverified

Software license and creative AI relevance screened; full guide and quality checks remain pending.

Scope: Testing neural visual treatments for playable game environments.

Evidence checked: 2026-10-22. No local execution implied.

- **Open-source software license · verified:** Complete MIT root license and complete Apache-2.0 version 4 license were reviewed and archived; the grants apply to different version directories. Models and game assets remain separate. [Source](https://github.com/SkyworkAI/Matrix-Game/blob/main/LICENSE) [Source](https://github.com/SkyworkAI/Matrix-Game/blob/main/Matrix-Game-4/LICENSE)
- **Creative results · unknown:** Published creative results have not received a substantive independent quality review.
- **Reproducible setup · unknown:** A complete installation and reproducibility review is pending.
- **Maintenance and support · unknown:** Workflow-specific maintenance and blocker review remains incomplete.
- **Independent use · unknown:** Independent first-hand use has not been established in this review.
- **Models, services and costs · documented:** The root MIT license covers earlier versions; version 4 has a separately reviewed Apache-2.0 license. Model weights and game assets retain their terms. Advertised FPS excludes video I/O and depends on exact hardware/settings; full setup and independent gameplay review remain pending. [Source](https://github.com/SkyworkAI/Matrix-Game/blob/main/README.md)

Source review only; not installed or run. The root MIT license covers earlier versions; version 4 has a separately reviewed Apache-2.0 license. Model weights and game assets retain their terms. Advertised FPS excludes video I/O and depends on exact hardware/settings; full setup and independent gameplay review remain pending.

- [Official documentation](https://github.com/SkyworkAI/Matrix-Game/blob/main/README.md)
- [Complete software license reviewed](https://github.com/SkyworkAI/Matrix-Game/blob/main/LICENSE)
- [Complete version 4 software license reviewed](https://github.com/SkyworkAI/Matrix-Game/blob/main/Matrix-Game-4/LICENSE)
- [Version 4 software license](https://github.com/SkyworkAI/Matrix-Game/blob/main/Matrix-Game-4/LICENSE)
### 3D Model Studio · MIT

Comparing generated GLBs and staging interactive object presentations.
A React/Three.js workspace connects image-to-3D providers to model inspection, generation queues and presentation views.
Full setup, hardware, model-term and output-quality review pending. MIT application; external Hyper3D/Tripo/Fal/Hunyuan providers, weights and demo assets have separate terms. Its internal model score is structural metadata, not independent artistic or fabrication validation.

### Quality assessment: Experimental

Software license and creative AI relevance screened; full guide and quality checks remain pending.

Scope: Comparing generated GLBs and staging interactive object presentations.

Evidence checked: 2026-10-22. No local execution implied.

Why Experimental: The current README explicitly describes the application as a React/Three.js prototype. https://github.com/huangserva/3DCellForge/blob/main/README.md

- **Open-source software license · verified:** Complete software license read and archived; this grant does not cover separate models, services or assets. [Source](https://github.com/huangserva/3DCellForge/blob/main/LICENSE)
- **Creative results · unknown:** Published creative results have not received a substantive independent quality review.
- **Reproducible setup · unknown:** A complete installation and reproducibility review is pending.
- **Maintenance and support · unknown:** Workflow-specific maintenance and blocker review remains incomplete.
- **Independent use · unknown:** Independent first-hand use has not been established in this review.
- **Models, services and costs · documented:** MIT application; external Hyper3D/Tripo/Fal/Hunyuan providers, weights and demo assets have separate terms. Its internal model score is structural metadata, not independent artistic or fabrication validation. [Source](https://github.com/huangserva/3DCellForge/blob/main/README.md)

Source review only; not installed or run. MIT application; external Hyper3D/Tripo/Fal/Hunyuan providers, weights and demo assets have separate terms. Its internal model score is structural metadata, not independent artistic or fabrication validation.

- [Official documentation](https://github.com/huangserva/3DCellForge/blob/main/README.md)
- [Complete software license reviewed](https://github.com/huangserva/3DCellForge/blob/main/LICENSE)
### Motion Design Skill · MIT

Prompting more deliberate easing, transitions and interface choreography.
An agent skill supplies motion-direction guidance and recipes that AI coding agents use to create and revise UI animation.
Full setup, hardware, model-term and output-quality review pending. MIT skill content; an agent/model and the chosen animation runtime are separate. It is guidance for AI-assisted authoring, not a trained motion model or a guarantee of animation quality.

### Quality assessment: Quality unverified

Software license and creative AI relevance screened; full guide and quality checks remain pending.

Scope: Prompting more deliberate easing, transitions and interface choreography.

Evidence checked: 2026-10-22. No local execution implied.

- **Open-source software license · verified:** Complete software license read and archived; this grant does not cover separate models, services or assets. [Source](https://github.com/LottieFiles/motion-design-skill/blob/main/LICENSE)
- **Creative results · unknown:** Published creative results have not received a substantive independent quality review.
- **Reproducible setup · unknown:** A complete installation and reproducibility review is pending.
- **Maintenance and support · unknown:** Workflow-specific maintenance and blocker review remains incomplete.
- **Independent use · unknown:** Independent first-hand use has not been established in this review.
- **Models, services and costs · documented:** MIT skill content; an agent/model and the chosen animation runtime are separate. It is guidance for AI-assisted authoring, not a trained motion model or a guarantee of animation quality. [Source](https://github.com/LottieFiles/motion-design-skill/blob/main/README.md)

Source review only; not installed or run. MIT skill content; an agent/model and the chosen animation runtime are separate. It is guidance for AI-assisted authoring, not a trained motion model or a guarantee of animation quality.

- [Official documentation](https://github.com/LottieFiles/motion-design-skill/blob/main/README.md)
- [Complete software license reviewed](https://github.com/LottieFiles/motion-design-skill/blob/main/LICENSE)
### Vox Director · MIT

Paper-collage-style explainers and short video drafts.
An AI-agent workflow generates script, collage keyframes, voice and video through Atlas Cloud and assembles the results with FFmpeg.
Full setup, hardware, model-term and output-quality review pending. MIT workflow code; Atlas Cloud inference, voice/video models and source media have separate charges and terms. Published examples are author demonstrations; factual accuracy and clip consistency need review.

### Quality assessment: Quality unverified

Software license and creative AI relevance screened; full guide and quality checks remain pending.

Scope: Paper-collage-style explainers and short video drafts.

Evidence checked: 2026-10-22. No local execution implied.

- **Open-source software license · verified:** Complete software license read and archived; this grant does not cover separate models, services or assets. [Source](https://github.com/Alisa0808/vox-director/blob/main/LICENSE)
- **Creative results · unknown:** Published creative results have not received a substantive independent quality review.
- **Reproducible setup · unknown:** A complete installation and reproducibility review is pending.
- **Maintenance and support · unknown:** Workflow-specific maintenance and blocker review remains incomplete.
- **Independent use · unknown:** Independent first-hand use has not been established in this review.
- **Models, services and costs · documented:** MIT workflow code; Atlas Cloud inference, voice/video models and source media have separate charges and terms. Published examples are author demonstrations; factual accuracy and clip consistency need review. [Source](https://github.com/Alisa0808/vox-director/blob/main/README.md)

Source review only; not installed or run. MIT workflow code; Atlas Cloud inference, voice/video models and source media have separate charges and terms. Published examples are author demonstrations; factual accuracy and clip consistency need review.

- [Official documentation](https://github.com/Alisa0808/vox-director/blob/main/README.md)
- [Complete software license reviewed](https://github.com/Alisa0808/vox-director/blob/main/LICENSE)
### Metric3D · BSD-2-Clause

Preparing geometry/depth inputs for neural scene and compositing experiments.
A learned monocular geometry model estimates metric depth and surface normals from a single image.
Full setup, hardware, model-term and output-quality review pending. BSD-2-Clause software reviewed in full; checkpoint/data terms and camera assumptions require further review. Predicted depth is not a measured scan or guaranteed physical scale.

### Quality assessment: Quality unverified

Software license and creative AI relevance screened; full guide and quality checks remain pending.

Scope: Preparing geometry/depth inputs for neural scene and compositing experiments.

Evidence checked: 2026-10-22. No local execution implied.

- **Open-source software license · verified:** Complete software license read and archived; this grant does not cover separate models, services or assets. [Source](https://github.com/YvanYin/Metric3D/blob/main/LICENSE)
- **Creative results · unknown:** Published creative results have not received a substantive independent quality review.
- **Reproducible setup · unknown:** A complete installation and reproducibility review is pending.
- **Maintenance and support · unknown:** Workflow-specific maintenance and blocker review remains incomplete.
- **Independent use · unknown:** Independent first-hand use has not been established in this review.
- **Models, services and costs · documented:** BSD-2-Clause software reviewed in full; checkpoint/data terms and camera assumptions require further review. Predicted depth is not a measured scan or guaranteed physical scale. [Source](https://github.com/YvanYin/Metric3D/blob/main/README.md)

Source review only; not installed or run. BSD-2-Clause software reviewed in full; checkpoint/data terms and camera assumptions require further review. Predicted depth is not a measured scan or guaranteed physical scale.

- [Official documentation](https://github.com/YvanYin/Metric3D/blob/main/README.md)
- [Complete software license reviewed](https://github.com/YvanYin/Metric3D/blob/main/LICENSE)
### Helios · Apache-2.0

Exploring extended generated video and lower-memory offloaded render experiments.
A long-video generation implementation provides text/video generation and memory-saving inference configurations.
Full setup, hardware, model-term and output-quality review pending. Apache-2.0 project code. The H100 real-time and roughly 6 GB offload claims refer to different configurations and cannot be combined into one requirement. Complete weight terms, RAM/storage and independent workflow reproduction remain pending.

### Quality assessment: Quality unverified

Software license and creative AI relevance screened; full guide and quality checks remain pending.

Scope: Exploring extended generated video and lower-memory offloaded render experiments.

Evidence checked: 2026-10-22. No local execution implied.

- **Open-source software license · verified:** Complete software license read and archived; this grant does not cover separate models, services or assets. [Source](https://github.com/PKU-YuanGroup/Helios/blob/main/LICENSE.txt)
- **Creative results · unknown:** Published creative results have not received a substantive independent quality review.
- **Reproducible setup · unknown:** A complete installation and reproducibility review is pending.
- **Maintenance and support · unknown:** Workflow-specific maintenance and blocker review remains incomplete.
- **Independent use · unknown:** Independent first-hand use has not been established in this review.
- **Models, services and costs · documented:** Apache-2.0 project code. The H100 real-time and roughly 6 GB offload claims refer to different configurations and cannot be combined into one requirement. Complete weight terms, RAM/storage and independent workflow reproduction remain pending. [Source](https://github.com/PKU-YuanGroup/Helios/blob/main/README.md)

Source review only; not installed or run. Apache-2.0 project code. The H100 real-time and roughly 6 GB offload claims refer to different configurations and cannot be combined into one requirement. Complete weight terms, RAM/storage and independent workflow reproduction remain pending.

- [Official documentation](https://github.com/PKU-YuanGroup/Helios/blob/main/README.md)
- [Complete software license reviewed](https://github.com/PKU-YuanGroup/Helios/blob/main/LICENSE.txt)
### AI Comic Builder · Apache-2.0

Managing AI-assisted comic or short-drama production from a script.
A script-to-animation workflow uses language/image/video providers to extract characters, plan shots, generate keyframes and assemble clips.
Full setup, hardware, model-term and output-quality review pending. Apache-2.0 app; OpenAI/Gemini/Kling/Seedance/Veo services have separate costs and terms. Character consistency is a workflow goal, not verified evidence. The documented Node baseline must be checked against the actual Next.js version during a full setup review.

### Quality assessment: Quality unverified

Software license and creative AI relevance screened; full guide and quality checks remain pending.

Scope: Managing AI-assisted comic or short-drama production from a script.

Evidence checked: 2026-10-22. No local execution implied.

- **Open-source software license · verified:** Complete software license read and archived; this grant does not cover separate models, services or assets. [Source](https://github.com/LingyiChen-AI/AIComicBuilder/blob/main/LICENSE)
- **Creative results · unknown:** Published creative results have not received a substantive independent quality review.
- **Reproducible setup · unknown:** A complete installation and reproducibility review is pending.
- **Maintenance and support · unknown:** Workflow-specific maintenance and blocker review remains incomplete.
- **Independent use · unknown:** Independent first-hand use has not been established in this review.
- **Models, services and costs · documented:** Apache-2.0 app; OpenAI/Gemini/Kling/Seedance/Veo services have separate costs and terms. Character consistency is a workflow goal, not verified evidence. The documented Node baseline must be checked against the actual Next.js version during a full setup review. [Source](https://github.com/LingyiChen-AI/AIComicBuilder/blob/main/README.md)

Source review only; not installed or run. Apache-2.0 app; OpenAI/Gemini/Kling/Seedance/Veo services have separate costs and terms. Character consistency is a workflow goal, not verified evidence. The documented Node baseline must be checked against the actual Next.js version during a full setup review.

- [Official documentation](https://github.com/LingyiChen-AI/AIComicBuilder/blob/main/README.md)
- [Complete software license reviewed](https://github.com/LingyiChen-AI/AIComicBuilder/blob/main/LICENSE)
### MiniMax MCP · MIT

Creating media assets from an agent conversation using MiniMax services.
An official MCP bridge exposes text-to-speech, voice design and cloning, image generation and video generation to an AI client.
Full setup, hardware, model-term and output-quality review pending. MIT bridge code; model inference is a separate MiniMax API service, not local open-source weights. Region/host must match account credentials and calls may incur costs. The maintainer now points to a newer CLI option as well.

### Quality assessment: Quality unverified

Software license and creative AI relevance screened; full guide and quality checks remain pending.

Scope: Creating media assets from an agent conversation using MiniMax services.

Evidence checked: 2026-10-22. No local execution implied.

- **Open-source software license · verified:** Complete software license read and archived; this grant does not cover separate models, services or assets. [Source](https://github.com/MiniMax-AI/MiniMax-MCP/blob/main/LICENSE)
- **Creative results · unknown:** Published creative results have not received a substantive independent quality review.
- **Reproducible setup · unknown:** A complete installation and reproducibility review is pending.
- **Maintenance and support · unknown:** Workflow-specific maintenance and blocker review remains incomplete.
- **Independent use · unknown:** Independent first-hand use has not been established in this review.
- **Models, services and costs · documented:** MIT bridge code; model inference is a separate MiniMax API service, not local open-source weights. Region/host must match account credentials and calls may incur costs. The maintainer now points to a newer CLI option as well. [Source](https://github.com/MiniMax-AI/MiniMax-MCP/blob/main/README.md)

Source review only; not installed or run. MIT bridge code; model inference is a separate MiniMax API service, not local open-source weights. Region/host must match account credentials and calls may incur costs. The maintainer now points to a newer CLI option as well.

- [Official documentation](https://github.com/MiniMax-AI/MiniMax-MCP/blob/main/README.md)
- [Complete software license reviewed](https://github.com/MiniMax-AI/MiniMax-MCP/blob/main/LICENSE)
### MIMO · Apache-2.0

Character-animation and scene-compositing experiments.
A video-synthesis model separates character, motion and scene controls for animating a reference character with 3D motion or a driving video.
Full setup, hardware, model-term and output-quality review pending. Apache-2.0 code; model/backbone/body-model terms and sample assets need further review. The released code is a simplified implementation; A100/L20 CUDA tests are examples, not universal minimum requirements.

### Quality assessment: Quality unverified

Software license and creative AI relevance screened; full guide and quality checks remain pending.

Scope: Character-animation and scene-compositing experiments.

Evidence checked: 2026-10-22. No local execution implied.

- **Open-source software license · verified:** Complete software license read and archived; this grant does not cover separate models, services or assets. [Source](https://github.com/menyifang/MIMO/blob/main/LICENSE)
- **Creative results · unknown:** Published creative results have not received a substantive independent quality review.
- **Reproducible setup · unknown:** A complete installation and reproducibility review is pending.
- **Maintenance and support · unknown:** Workflow-specific maintenance and blocker review remains incomplete.
- **Independent use · unknown:** Independent first-hand use has not been established in this review.
- **Models, services and costs · documented:** Apache-2.0 code; model/backbone/body-model terms and sample assets need further review. The released code is a simplified implementation; A100/L20 CUDA tests are examples, not universal minimum requirements. [Source](https://github.com/menyifang/MIMO/blob/main/README.md)

Source review only; not installed or run. Apache-2.0 code; model/backbone/body-model terms and sample assets need further review. The released code is a simplified implementation; A100/L20 CUDA tests are examples, not universal minimum requirements.

- [Official documentation](https://github.com/menyifang/MIMO/blob/main/README.md)
- [Complete software license reviewed](https://github.com/menyifang/MIMO/blob/main/LICENSE)
### MagicTime · Apache-2.0

Concept sequences involving gradual transformation and time-lapse-style imagery.
A prompt-conditioned video pipeline learns metamorphic/time-lapse transformations rather than only short rigid motion.
Full setup, hardware, model-term and output-quality review pending. Apache-2.0 code. Datasets, backbone models and checkpoints retain separate terms; a complete environment/hardware and output review remains pending. Inclusion is new to this library, not a new software release claim.

### Quality assessment: Quality unverified

Software license and creative AI relevance screened; full guide and quality checks remain pending.

Scope: Concept sequences involving gradual transformation and time-lapse-style imagery.

Evidence checked: 2026-10-22. No local execution implied.

- **Open-source software license · verified:** Complete software license read and archived; this grant does not cover separate models, services or assets. [Source](https://github.com/PKU-YuanGroup/MagicTime/blob/main/LICENSE)
- **Creative results · unknown:** Published creative results have not received a substantive independent quality review.
- **Reproducible setup · unknown:** A complete installation and reproducibility review is pending.
- **Maintenance and support · unknown:** Workflow-specific maintenance and blocker review remains incomplete.
- **Independent use · unknown:** Independent first-hand use has not been established in this review.
- **Models, services and costs · documented:** Apache-2.0 code. Datasets, backbone models and checkpoints retain separate terms; a complete environment/hardware and output review remains pending. Inclusion is new to this library, not a new software release claim. [Source](https://github.com/PKU-YuanGroup/MagicTime/blob/main/README.md)

Source review only; not installed or run. Apache-2.0 code. Datasets, backbone models and checkpoints retain separate terms; a complete environment/hardware and output review remains pending. Inclusion is new to this library, not a new software release claim.

- [Official documentation](https://github.com/PKU-YuanGroup/MagicTime/blob/main/README.md)
- [Complete software license reviewed](https://github.com/PKU-YuanGroup/MagicTime/blob/main/LICENSE)
### Cosmos Predict 2.5 · Apache-2.0

Researching generative scene continuation for media prototyping.
A world-prediction implementation generates future video states from textual or visual context.
Full setup, hardware, model-term and output-quality review pending. Apache-2.0 software with separately licensed NVIDIA model weights. The README says active development has moved to Cosmos 3 and this version receives limited maintenance; full creative workflow and hardware review remain pending.

### Quality assessment: Quality unverified

Software license and creative AI relevance screened; full guide and quality checks remain pending.

Scope: Researching generative scene continuation for media prototyping.

Evidence checked: 2026-10-22. No local execution implied.

- **Open-source software license · verified:** Complete software license read and archived; this grant does not cover separate models, services or assets. [Source](https://github.com/nvidia-cosmos/cosmos-predict2.5/blob/main/LICENSE)
- **Creative results · unknown:** Published creative results have not received a substantive independent quality review.
- **Reproducible setup · unknown:** A complete installation and reproducibility review is pending.
- **Maintenance and support · documented:** The maintainer explicitly states limited maintenance and a migration of active development to Cosmos 3; ongoing support for this selected older version is not verified. [Source](https://github.com/nvidia-cosmos/cosmos-predict2.5/blob/main/README.md)
- **Independent use · unknown:** Independent first-hand use has not been established in this review.
- **Models, services and costs · documented:** Apache-2.0 software with separately licensed NVIDIA model weights. The README says active development has moved to Cosmos 3 and this version receives limited maintenance; full creative workflow and hardware review remain pending. [Source](https://github.com/nvidia-cosmos/cosmos-predict2.5/blob/main/README.md)

Source review only; not installed or run. Apache-2.0 software with separately licensed NVIDIA model weights. The README says active development has moved to Cosmos 3 and this version receives limited maintenance; full creative workflow and hardware review remain pending.

- [Official documentation](https://github.com/nvidia-cosmos/cosmos-predict2.5/blob/main/README.md)
- [Complete software license reviewed](https://github.com/nvidia-cosmos/cosmos-predict2.5/blob/main/LICENSE)
### Lance · Apache-2.0

Exploring multimodal edit-and-generate workflows with an openly licensed implementation.
A unified multimodal implementation supports image/video generation, understanding and iterative editing in one model family.
Full setup, hardware, model-term and output-quality review pending. Apache-2.0 code. The README requires Python 3.10+, CUDA 12.4+ and at least 40 GB GPU memory for inference; checkpoints and other model terms still need review. Capability demos do not establish independent edit reliability.

### Quality assessment: Quality unverified

Software license and creative AI relevance screened; full guide and quality checks remain pending.

Scope: Exploring multimodal edit-and-generate workflows with an openly licensed implementation.

Evidence checked: 2026-10-22. No local execution implied.

- **Open-source software license · verified:** Complete software license read and archived; this grant does not cover separate models, services or assets. [Source](https://github.com/bytedance/Lance/blob/main/LICENSE)
- **Creative results · unknown:** Published creative results have not received a substantive independent quality review.
- **Reproducible setup · unknown:** A complete installation and reproducibility review is pending.
- **Maintenance and support · unknown:** Workflow-specific maintenance and blocker review remains incomplete.
- **Independent use · unknown:** Independent first-hand use has not been established in this review.
- **Models, services and costs · documented:** Apache-2.0 code. The README requires Python 3.10+, CUDA 12.4+ and at least 40 GB GPU memory for inference; checkpoints and other model terms still need review. Capability demos do not establish independent edit reliability. [Source](https://github.com/bytedance/Lance/blob/main/README.md)

Source review only; not installed or run. Apache-2.0 code. The README requires Python 3.10+, CUDA 12.4+ and at least 40 GB GPU memory for inference; checkpoints and other model terms still need review. Capability demos do not establish independent edit reliability.

- [Official documentation](https://github.com/bytedance/Lance/blob/main/README.md)
- [Complete software license reviewed](https://github.com/bytedance/Lance/blob/main/LICENSE)
### Drama Skills · MIT

Maintaining continuity and reviewable production plans across episodic AI drama or motion comics.
An AI-agent skill set organizes script adaptation, visual assets, storyboards, production prompts and editing into explicit creative project documents.
Full setup, hardware, model-term and output-quality review pending. MIT skills; coding-agent services, generation adapters, model fees and source-story rights are separate. Python 3.9+ and FFmpeg are documented for helper/editing paths; model quality and claimed studio experience are not independently verified.

### Quality assessment: Quality unverified

Software license and creative AI relevance screened; full guide and quality checks remain pending.

Scope: Maintaining continuity and reviewable production plans across episodic AI drama or motion comics.

Evidence checked: 2026-10-22. No local execution implied.

- **Open-source software license · verified:** Complete software license read and archived; this grant does not cover separate models, services or assets. [Source](https://github.com/zenstory-ai/drama-skills/blob/main/LICENSE)
- **Creative results · unknown:** Published creative results have not received a substantive independent quality review.
- **Reproducible setup · unknown:** A complete installation and reproducibility review is pending.
- **Maintenance and support · unknown:** Workflow-specific maintenance and blocker review remains incomplete.
- **Independent use · unknown:** Independent first-hand use has not been established in this review.
- **Models, services and costs · documented:** MIT skills; coding-agent services, generation adapters, model fees and source-story rights are separate. Python 3.9+ and FFmpeg are documented for helper/editing paths; model quality and claimed studio experience are not independently verified. [Source](https://github.com/zenstory-ai/drama-skills/blob/main/README.md)

Source review only; not installed or run. MIT skills; coding-agent services, generation adapters, model fees and source-story rights are separate. Python 3.9+ and FFmpeg are documented for helper/editing paths; model quality and claimed studio experience are not independently verified.

- [Official documentation](https://github.com/zenstory-ai/drama-skills/blob/main/README.md)
- [Complete software license reviewed](https://github.com/zenstory-ai/drama-skills/blob/main/LICENSE)
### Three.js Game Skills · MIT

Prototyping browser games with an AI coding agent and inspectable runtime output.
Agent skills coordinate gameplay, graphics, UI and optional generated media around a Three.js scaffold and test hooks.
Full setup, hardware, model-term and output-quality review pending. MIT skill/scaffold code; agent/model services and generated asset rights are separate. Playable author demos and test templates do not prove all generated games are polished or reliable.

### Quality assessment: Quality unverified

Software license and creative AI relevance screened; full guide and quality checks remain pending.

Scope: Prototyping browser games with an AI coding agent and inspectable runtime output.

Evidence checked: 2026-10-22. No local execution implied.

- **Open-source software license · verified:** Complete software license read and archived; this grant does not cover separate models, services or assets. [Source](https://github.com/majidmanzarpour/threejs-game-skills/blob/main/LICENSE)
- **Creative results · unknown:** Published creative results have not received a substantive independent quality review.
- **Reproducible setup · unknown:** A complete installation and reproducibility review is pending.
- **Maintenance and support · unknown:** Workflow-specific maintenance and blocker review remains incomplete.
- **Independent use · unknown:** Independent first-hand use has not been established in this review.
- **Models, services and costs · documented:** MIT skill/scaffold code; agent/model services and generated asset rights are separate. Playable author demos and test templates do not prove all generated games are polished or reliable. [Source](https://github.com/majidmanzarpour/threejs-game-skills/blob/main/README.md)

Source review only; not installed or run. MIT skill/scaffold code; agent/model services and generated asset rights are separate. Playable author demos and test templates do not prove all generated games are polished or reliable.

- [Official documentation](https://github.com/majidmanzarpour/threejs-game-skills/blob/main/README.md)
- [Complete software license reviewed](https://github.com/majidmanzarpour/threejs-game-skills/blob/main/LICENSE)
### BrainFLORA · MIT

Researching biosignal-to-image representations for experimental visualization and media art.
A multimodal neural-embedding framework reconstructs, retrieves and captions images from recorded EEG/MEG/fMRI datasets.
Full setup, hardware, model-term and output-quality review pending. MIT code; datasets, checkpoints and Shikra/model assets have separate terms. This is a dataset-based research workflow, not a proven live mind-reading interface; acquisition hardware, training and generalization need specialist review.

### Quality assessment: Quality unverified

Software license and creative AI relevance screened; full guide and quality checks remain pending.

Scope: Researching biosignal-to-image representations for experimental visualization and media art.

Evidence checked: 2026-10-22. No local execution implied.

- **Open-source software license · verified:** Complete software license read and archived; this grant does not cover separate models, services or assets. [Source](https://github.com/ncclab-sustech/BrainFLORA/blob/main/LICENSE)
- **Creative results · unknown:** Published creative results have not received a substantive independent quality review.
- **Reproducible setup · unknown:** A complete installation and reproducibility review is pending.
- **Maintenance and support · unknown:** Workflow-specific maintenance and blocker review remains incomplete.
- **Independent use · unknown:** Independent first-hand use has not been established in this review.
- **Models, services and costs · documented:** MIT code; datasets, checkpoints and Shikra/model assets have separate terms. This is a dataset-based research workflow, not a proven live mind-reading interface; acquisition hardware, training and generalization need specialist review. [Source](https://github.com/ncclab-sustech/BrainFLORA/blob/main/README.md)

Source review only; not installed or run. MIT code; datasets, checkpoints and Shikra/model assets have separate terms. This is a dataset-based research workflow, not a proven live mind-reading interface; acquisition hardware, training and generalization need specialist review.

- [Official documentation](https://github.com/ncclab-sustech/BrainFLORA/blob/main/README.md)
- [Complete software license reviewed](https://github.com/ncclab-sustech/BrainFLORA/blob/main/LICENSE)
### TactileLens · MIT

Prototyping camera-to-tactile texture experiences on supported Android hardware.
On-device neural texture analysis and segmentation drive Android vibration and synchronized synthetic audio.
Full setup, hardware, model-term and output-quality review pending. MIT code; a full model-asset and build review is pending. Android Studio Ladybug+, API 35 and Snapdragon/Hexagon hardware are documented; Galaxy S25 Ultra is the target. Sub-20ms and accessibility claims are not independently verified or validated for navigation safety.

### Quality assessment: Quality unverified

Software license and creative AI relevance screened; full guide and quality checks remain pending.

Scope: Prototyping camera-to-tactile texture experiences on supported Android hardware.

Evidence checked: 2026-10-22. No local execution implied.

- **Open-source software license · verified:** Complete software license read and archived; this grant does not cover separate models, services or assets. [Source](https://github.com/chisomogugu/TactileLens---Vision-to-Haptics-AI-Application/blob/main/LICENSE)
- **Creative results · unknown:** Published creative results have not received a substantive independent quality review.
- **Reproducible setup · unknown:** A complete installation and reproducibility review is pending.
- **Maintenance and support · unknown:** Workflow-specific maintenance and blocker review remains incomplete.
- **Independent use · unknown:** Independent first-hand use has not been established in this review.
- **Models, services and costs · documented:** MIT code; a full model-asset and build review is pending. Android Studio Ladybug+, API 35 and Snapdragon/Hexagon hardware are documented; Galaxy S25 Ultra is the target. Sub-20ms and accessibility claims are not independently verified or validated for navigation safety. [Source](https://github.com/chisomogugu/TactileLens---Vision-to-Haptics-AI-Application/blob/main/README.md)

Source review only; not installed or run. MIT code; a full model-asset and build review is pending. Android Studio Ladybug+, API 35 and Snapdragon/Hexagon hardware are documented; Galaxy S25 Ultra is the target. Sub-20ms and accessibility claims are not independently verified or validated for navigation safety.

- [Official documentation](https://github.com/chisomogugu/TactileLens---Vision-to-Haptics-AI-Application/blob/main/README.md)
- [Complete software license reviewed](https://github.com/chisomogugu/TactileLens---Vision-to-Haptics-AI-Application/blob/main/LICENSE)
### HFG Neural Holography · MIT

Exploring learned hologram reconstruction and ringing reduction.
A neural holography training pipeline uses high-frequency-guided generative priors and learned depth-derived data.
Full setup, hardware, model-term and output-quality review pending. MIT project code; Stable Diffusion, ControlNet, VAE and rendered datasets have separate terms. Proposed-method checkpoints are not yet released, and some referenced weight sources are placeholders.

### Quality assessment: Experimental

Software license and creative AI relevance screened; full guide and quality checks remain pending.

Scope: Exploring learned hologram reconstruction and ringing reduction.

Evidence checked: 2026-10-22. No local execution implied.

Why Experimental: The current README says the proposed checkpoints will be released after acceptance and leaves a required VAE source as a placeholder, so the documented reconstruction workflow is unfinished. https://github.com/HannahZhang1926/HFG-Neural-Holo/blob/main/README.md

- **Open-source software license · verified:** Complete software license read and archived; this grant does not cover separate models, services or assets. [Source](https://github.com/HannahZhang1926/HFG-Neural-Holo/blob/main/LICENSE)
- **Creative results · unknown:** Published creative results have not received a substantive independent quality review.
- **Reproducible setup · unknown:** A complete installation and reproducibility review is pending.
- **Maintenance and support · unknown:** Workflow-specific maintenance and blocker review remains incomplete.
- **Independent use · unknown:** Independent first-hand use has not been established in this review.
- **Models, services and costs · documented:** MIT project code; Stable Diffusion, ControlNet, VAE and rendered datasets have separate terms. Proposed-method checkpoints are not yet released, and some referenced weight sources are placeholders. [Source](https://github.com/HannahZhang1926/HFG-Neural-Holo/blob/main/README.md)

Source review only; not installed or run. MIT project code; Stable Diffusion, ControlNet, VAE and rendered datasets have separate terms. Proposed-method checkpoints are not yet released, and some referenced weight sources are placeholders.

- [Official documentation](https://github.com/HannahZhang1926/HFG-Neural-Holo/blob/main/README.md)
- [Complete software license reviewed](https://github.com/HannahZhang1926/HFG-Neural-Holo/blob/main/LICENSE)
### Vox Explainer Method · AGPL-3.0

Drafting paper-collage explainer or advertising sequences with an AI assistant.
An AI skill uses MaxFusion MCP generation to create collage references, animated clips and continuous explainer sequences from a script.
Full setup, hardware, model-term and output-quality review pending. AGPL-3.0 code/skill; Claude, MaxFusion and Google generation services, upload destinations and charges are separate. Clip continuity and researched factual claims require human review; no independent end-to-end reproduction was established.

### Quality assessment: Quality unverified

Software license and creative AI relevance screened; full guide and quality checks remain pending.

Scope: Drafting paper-collage explainer or advertising sequences with an AI assistant.

Evidence checked: 2026-10-22. No local execution implied.

- **Open-source software license · verified:** Complete software license read and archived; this grant does not cover separate models, services or assets. [Source](https://github.com/holy-templar/vox-animated-ad-mcp/blob/main/LICENSE)
- **Creative results · unknown:** Published creative results have not received a substantive independent quality review.
- **Reproducible setup · unknown:** A complete installation and reproducibility review is pending.
- **Maintenance and support · unknown:** Workflow-specific maintenance and blocker review remains incomplete.
- **Independent use · unknown:** Independent first-hand use has not been established in this review.
- **Models, services and costs · documented:** AGPL-3.0 code/skill; Claude, MaxFusion and Google generation services, upload destinations and charges are separate. Clip continuity and researched factual claims require human review; no independent end-to-end reproduction was established. [Source](https://github.com/holy-templar/vox-animated-ad-mcp/blob/main/README.md)

Source review only; not installed or run. AGPL-3.0 code/skill; Claude, MaxFusion and Google generation services, upload destinations and charges are separate. Clip continuity and researched factual claims require human review; no independent end-to-end reproduction was established.

- [Official documentation](https://github.com/holy-templar/vox-animated-ad-mcp/blob/main/README.md)
- [Complete software license reviewed](https://github.com/holy-templar/vox-animated-ad-mcp/blob/main/LICENSE)
### haptics.md · Apache-2.0

Adding explicitly specified haptic feedback to AI-authored interfaces.
An agent-oriented descriptor/compiler workflow lets AI coding agents author portable tactile feedback patterns and map them to native or web APIs.
Full setup, hardware, model-term and output-quality review pending. Apache-2.0 tooling. The web route is duration-only Android Chrome and a no-op on iPhone Safari/desktop. The separate braille proposal is explicitly not co-designed or recommended; do not treat it as validated assistive communication. Core pattern compilation and AI-agent use need a full review.

### Quality assessment: Quality unverified

Software license and creative AI relevance screened; full guide and quality checks remain pending.

Scope: Adding explicitly specified haptic feedback to AI-authored interfaces.

Evidence checked: 2026-10-22. No local execution implied.

- **Open-source software license · verified:** Complete software license read and archived; this grant does not cover separate models, services or assets. [Source](https://github.com/Bimbi-Dev/haptics.md/blob/main/LICENSE)
- **Creative results · unknown:** Published creative results have not received a substantive independent quality review.
- **Reproducible setup · unknown:** A complete installation and reproducibility review is pending.
- **Maintenance and support · unknown:** Workflow-specific maintenance and blocker review remains incomplete.
- **Independent use · unknown:** Independent first-hand use has not been established in this review.
- **Models, services and costs · documented:** Apache-2.0 tooling. The web route is duration-only Android Chrome and a no-op on iPhone Safari/desktop. The separate braille proposal is explicitly not co-designed or recommended; do not treat it as validated assistive communication. Core pattern compilation and AI-agent use need a full review. [Source](https://github.com/Bimbi-Dev/haptics.md/blob/main/README.md)

Source review only; not installed or run. Apache-2.0 tooling. The web route is duration-only Android Chrome and a no-op on iPhone Safari/desktop. The separate braille proposal is explicitly not co-designed or recommended; do not treat it as validated assistive communication. Core pattern compilation and AI-agent use need a full review.

- [Official documentation](https://github.com/Bimbi-Dev/haptics.md/blob/main/README.md)
- [Complete software license reviewed](https://github.com/Bimbi-Dev/haptics.md/blob/main/LICENSE)
### UL-UNAS · MIT

Dialogue and voice-recording cleanup in compact audio tools.
A learned ultra-lightweight U-Net removes noise from recorded speech; the released software offers file inference and streaming ONNX code.
Full setup, hardware, model-term and output-quality review pending. The full MIT code license was reviewed. Checkpoint/dataset terms, dependency versions and hardware limits still need a full guide. Arm separately packages a 16 kHz mono LiteRT variant, but its offered inference engine requires early-access approval and its card says accuracy was not evaluated; that package is not equated with the freely available upstream runtime.

### Quality assessment: Quality unverified

Software license and creative AI relevance screened; full guide and quality checks remain pending.

Scope: Dialogue and voice-recording cleanup in compact audio tools.

Evidence checked: 2026-10-22. No local execution implied.

- **Open-source software license · verified:** Complete software license read and archived; this grant does not cover separate models, services or assets. [Source](https://github.com/Xiaobin-Rong/ul-unas/blob/main/LICENSE)
- **Creative results · unknown:** Published creative results have not received a substantive independent quality review.
- **Reproducible setup · unknown:** A complete installation and reproducibility review is pending.
- **Maintenance and support · unknown:** Workflow-specific maintenance and blocker review remains incomplete.
- **Independent use · documented:** Arm documents a separately packaged LiteRT port and its measured Android timing. This is an external integration trail; accuracy, public inference access and broad independent reproduction remain unresolved. [Source](https://huggingface.co/Arm/ulunas-speech-enhancement-fp32-litert)
- **Models, services and costs · documented:** The full MIT code license was reviewed. Checkpoint/dataset terms, dependency versions and hardware limits still need a full guide. Arm separately packages a 16 kHz mono LiteRT variant, but its offered inference engine requires early-access approval and its card says accuracy was not evaluated; that package is not equated with the freely available upstream runtime. [Source](https://github.com/Xiaobin-Rong/ul-unas/blob/main/README.md) [Source](https://huggingface.co/Arm/ulunas-speech-enhancement-fp32-litert)

Source review only; not installed or run. The full MIT code license was reviewed. Checkpoint/dataset terms, dependency versions and hardware limits still need a full guide. Arm separately packages a 16 kHz mono LiteRT variant, but its offered inference engine requires early-access approval and its card says accuracy was not evaluated; that package is not equated with the freely available upstream runtime.

- [Official documentation](https://github.com/Xiaobin-Rong/ul-unas/blob/main/README.md)
- [Complete software license reviewed](https://github.com/Xiaobin-Rong/ul-unas/blob/main/LICENSE)
- [Arm downstream model package and limitations](https://huggingface.co/Arm/ulunas-speech-enhancement-fp32-litert)
- [Arm downstream model package and limitations](https://huggingface.co/Arm/ulunas-speech-enhancement-fp32-litert)
### NDVQ · MIT

Exploratory speech-codec and synthetic-dialogue research.
Distribution-based learned vector quantization compresses and reconstructs speech, with code for training and evaluation.
Full setup, hardware, model-term and output-quality review pending. MIT code; Python 3.9, old pinned PyTorch/CUDA/fairseq/Apex paths and dependent codec/model/data terms need careful review. The study is speech-focused and does not establish music or ambient-sound quality.

### Quality assessment: Experimental

Software license and creative AI relevance screened; full guide and quality checks remain pending.

Scope: Exploratory speech-codec and synthetic-dialogue research.

Evidence checked: 2026-10-22. No local execution implied.

Why Experimental: The current README explicitly describes the distributed implementation as experimental, uncleaned research code. https://github.com/ZhikangNiu/NDVQ/blob/main/README.md

- **Open-source software license · verified:** Complete software license read and archived; this grant does not cover separate models, services or assets. [Source](https://github.com/ZhikangNiu/NDVQ/blob/main/LICENSE)
- **Creative results · unknown:** Published creative results have not received a substantive independent quality review.
- **Reproducible setup · unknown:** A complete installation and reproducibility review is pending.
- **Maintenance and support · unknown:** Workflow-specific maintenance and blocker review remains incomplete.
- **Independent use · unknown:** Independent first-hand use has not been established in this review.
- **Models, services and costs · documented:** MIT code; Python 3.9, old pinned PyTorch/CUDA/fairseq/Apex paths and dependent codec/model/data terms need careful review. The study is speech-focused and does not establish music or ambient-sound quality. [Source](https://github.com/ZhikangNiu/NDVQ/blob/main/README.md)

Source review only; not installed or run. MIT code; Python 3.9, old pinned PyTorch/CUDA/fairseq/Apex paths and dependent codec/model/data terms need careful review. The study is speech-focused and does not establish music or ambient-sound quality.

- [Official documentation](https://github.com/ZhikangNiu/NDVQ/blob/main/README.md)
- [Complete software license reviewed](https://github.com/ZhikangNiu/NDVQ/blob/main/LICENSE)
### Oobleck · MIT

Developing custom neural sound representations.
An audio autoencoder implementation produces learned latent representations intended for downstream sound diffusion and token-based synthesis.
Full setup, hardware, model-term and output-quality review pending. MIT code. The README still awaits initial trained models and proposes future validation; it does not provide a production-ready pretrained audio workflow.

### Quality assessment: Experimental

Software license and creative AI relevance screened; full guide and quality checks remain pending.

Scope: Developing custom neural sound representations.

Evidence checked: 2026-10-22. No local execution implied.

Why Experimental: The current README says it is waiting for the first models to be trained and describes model variants and listening validation as future work. https://github.com/Harmonai-org/oobleck/blob/main/README.md

- **Open-source software license · verified:** Complete software license read and archived; this grant does not cover separate models, services or assets. [Source](https://github.com/Harmonai-org/oobleck/blob/main/LICENSE)
- **Creative results · unknown:** Published creative results have not received a substantive independent quality review.
- **Reproducible setup · unknown:** A complete installation and reproducibility review is pending.
- **Maintenance and support · unknown:** Workflow-specific maintenance and blocker review remains incomplete.
- **Independent use · unknown:** Independent first-hand use has not been established in this review.
- **Models, services and costs · documented:** MIT code. The README still awaits initial trained models and proposes future validation; it does not provide a production-ready pretrained audio workflow. [Source](https://github.com/Harmonai-org/oobleck/blob/main/README.md)

Source review only; not installed or run. MIT code. The README still awaits initial trained models and proposes future validation; it does not provide a production-ready pretrained audio workflow.

- [Official documentation](https://github.com/Harmonai-org/oobleck/blob/main/README.md)
- [Complete software license reviewed](https://github.com/Harmonai-org/oobleck/blob/main/LICENSE)
### SNAC-Go · Apache-2.0

Embedding neural speech decoding in Go applications.
A Go implementation decodes hierarchical SNAC neural tokens into 24 kHz speech waveforms for TTS applications.
Full setup, hardware, model-term and output-quality review pending. Apache-2.0 software; SNAC and TTS model weights retain separate terms. The quickstart includes application-defined WAV output and needs an integration guide. Maintainer numerical-equivalence claims are not independent listening tests; pre-1.0 API changes remain possible.

### Quality assessment: Quality unverified

Software license and creative AI relevance screened; full guide and quality checks remain pending.

Scope: Embedding neural speech decoding in Go applications.

Evidence checked: 2026-10-22. No local execution implied.

- **Open-source software license · verified:** Complete software license read and archived; this grant does not cover separate models, services or assets. [Source](https://github.com/tcpipuk/snac-go/blob/main/LICENSE)
- **Creative results · unknown:** Published creative results have not received a substantive independent quality review.
- **Reproducible setup · unknown:** A complete installation and reproducibility review is pending.
- **Maintenance and support · unknown:** Workflow-specific maintenance and blocker review remains incomplete.
- **Independent use · unknown:** Independent first-hand use has not been established in this review.
- **Models, services and costs · documented:** Apache-2.0 software; SNAC and TTS model weights retain separate terms. The quickstart includes application-defined WAV output and needs an integration guide. Maintainer numerical-equivalence claims are not independent listening tests; pre-1.0 API changes remain possible. [Source](https://github.com/tcpipuk/snac-go/blob/main/README.md)

Source review only; not installed or run. Apache-2.0 software; SNAC and TTS model weights retain separate terms. The quickstart includes application-defined WAV output and needs an integration guide. Maintainer numerical-equivalence claims are not independent listening tests; pre-1.0 API changes remain possible.

- [Official documentation](https://github.com/tcpipuk/snac-go/blob/main/README.md)
- [Complete software license reviewed](https://github.com/tcpipuk/snac-go/blob/main/LICENSE)
### NeuralCodecs for .NET · Apache-2.0

Integrating neural audio and TTS into .NET creative tools.
C# implementations encode/decode neural audio representations and support model-driven dialogue generation.
Full setup, hardware, model-term and output-quality review pending. Apache-2.0 root code and separately reviewed third-party notices. Requires .NET 8+, TorchSharp/libTorch and model-specific dependencies. Code notices do not settle model-weight permissions, especially EnCodec and other downloaded checkpoints; some model links and examples need correction before a complete guide.

### Quality assessment: Quality unverified

Software license and creative AI relevance screened; full guide and quality checks remain pending.

Scope: Integrating neural audio and TTS into .NET creative tools.

Evidence checked: 2026-10-22. No local execution implied.

- **Open-source software license · verified:** Complete software license read and archived; this grant does not cover separate models, services or assets. [Source](https://github.com/DillionLowry/NeuralCodecs/blob/main/LICENSE.md)
- **Creative results · unknown:** Published creative results have not received a substantive independent quality review.
- **Reproducible setup · unknown:** A complete installation and reproducibility review is pending.
- **Maintenance and support · unknown:** Workflow-specific maintenance and blocker review remains incomplete.
- **Independent use · unknown:** Independent first-hand use has not been established in this review.
- **Models, services and costs · documented:** Apache-2.0 root code and separately reviewed third-party notices. Requires .NET 8+, TorchSharp/libTorch and model-specific dependencies. Code notices do not settle model-weight permissions, especially EnCodec and other downloaded checkpoints; some model links and examples need correction before a complete guide. [Source](https://github.com/DillionLowry/NeuralCodecs/blob/main/README.md) [Source](https://github.com/DillionLowry/NeuralCodecs/blob/main/THIRD-PARTY-NOTICES.md)

Source review only; not installed or run. Apache-2.0 root code and separately reviewed third-party notices. Requires .NET 8+, TorchSharp/libTorch and model-specific dependencies. Code notices do not settle model-weight permissions, especially EnCodec and other downloaded checkpoints; some model links and examples need correction before a complete guide.

- [Official documentation](https://github.com/DillionLowry/NeuralCodecs/blob/main/README.md)
- [Complete software license reviewed](https://github.com/DillionLowry/NeuralCodecs/blob/main/LICENSE.md)
- [Third-party software notices](https://github.com/DillionLowry/NeuralCodecs/blob/main/THIRD-PARTY-NOTICES.md)
- [Third-party software notices](https://github.com/DillionLowry/NeuralCodecs/blob/main/THIRD-PARTY-NOTICES.md)
### SD-Codec · MIT

Research on editable source-aware audio representations.
A learned codec separates source representations for speech, music and sound while compressing/reconstructing audio.
Full setup, hardware, model-term and output-quality review pending. MIT repository software; downloaded weights, AudioCraft/DAC-derived parts and DnR/DNS/Jamendo/MUSAN/WHAM data require separate terms. The documented eight A100 80 GB training setup is not an inference minimum; inference requirements remain unresolved.

### Quality assessment: Quality unverified

Software license and creative AI relevance screened; full guide and quality checks remain pending.

Scope: Research on editable source-aware audio representations.

Evidence checked: 2026-10-22. No local execution implied.

- **Open-source software license · verified:** Complete software license read and archived; this grant does not cover separate models, services or assets. [Source](https://github.com/XiaoyuBIE1994/SDCodec/blob/main/LICENSE)
- **Creative results · unknown:** Published creative results have not received a substantive independent quality review.
- **Reproducible setup · unknown:** A complete installation and reproducibility review is pending.
- **Maintenance and support · unknown:** Workflow-specific maintenance and blocker review remains incomplete.
- **Independent use · unknown:** Independent first-hand use has not been established in this review.
- **Models, services and costs · documented:** MIT repository software; downloaded weights, AudioCraft/DAC-derived parts and DnR/DNS/Jamendo/MUSAN/WHAM data require separate terms. The documented eight A100 80 GB training setup is not an inference minimum; inference requirements remain unresolved. [Source](https://github.com/XiaoyuBIE1994/SDCodec/blob/main/README.md)

Source review only; not installed or run. MIT repository software; downloaded weights, AudioCraft/DAC-derived parts and DnR/DNS/Jamendo/MUSAN/WHAM data require separate terms. The documented eight A100 80 GB training setup is not an inference minimum; inference requirements remain unresolved.

- [Official documentation](https://github.com/XiaoyuBIE1994/SDCodec/blob/main/README.md)
- [Complete software license reviewed](https://github.com/XiaoyuBIE1994/SDCodec/blob/main/LICENSE)
### lyra-js · MIT

Low-bitrate voice transport experiments for interactive web media.
A WebAssembly/JavaScript port exposes learned Lyra speech encoding and decoding in a browser.
Full setup, hardware, model-term and output-quality review pending. MIT wrapper with upstream Lyra code/model obligations separate. npm package is lyra-codec; browser compatibility, current build provenance and listening quality need a full review.

### Quality assessment: Quality unverified

Software license and creative AI relevance screened; full guide and quality checks remain pending.

Scope: Low-bitrate voice transport experiments for interactive web media.

Evidence checked: 2026-10-22. No local execution implied.

- **Open-source software license · verified:** Complete software license read and archived; this grant does not cover separate models, services or assets. [Source](https://github.com/neuvideo/lyra-js/blob/main/LICENSE)
- **Creative results · unknown:** Published creative results have not received a substantive independent quality review.
- **Reproducible setup · unknown:** A complete installation and reproducibility review is pending.
- **Maintenance and support · unknown:** Workflow-specific maintenance and blocker review remains incomplete.
- **Independent use · unknown:** Independent first-hand use has not been established in this review.
- **Models, services and costs · documented:** MIT wrapper with upstream Lyra code/model obligations separate. npm package is lyra-codec; browser compatibility, current build provenance and listening quality need a full review. [Source](https://github.com/neuvideo/lyra-js/blob/main/README.md)

Source review only; not installed or run. MIT wrapper with upstream Lyra code/model obligations separate. npm package is lyra-codec; browser compatibility, current build provenance and listening quality need a full review.

- [Official documentation](https://github.com/neuvideo/lyra-js/blob/main/README.md)
- [Complete software license reviewed](https://github.com/neuvideo/lyra-js/blob/main/LICENSE)
### AudioCodec-Hub · MIT

Comparing neural codecs or preparing audio representations for creative model workflows.
A Python interface encodes and reconstructs audio with learned EnCodec, DAC and AudioDec models, including directory encoding.
Full setup, hardware, model-term and output-quality review pending. MIT wrapper; each pretrained model keeps its own terms. Batch decoding, multichannel handling and packaging remain incomplete; the author warns batch-code equivalence has not been carefully checked. Scope and current API examples need verification.

### Quality assessment: Quality unverified

Software license and creative AI relevance screened; full guide and quality checks remain pending.

Scope: Comparing neural codecs or preparing audio representations for creative model workflows.

Evidence checked: 2026-10-22. No local execution implied.

- **Open-source software license · verified:** Complete software license read and archived; this grant does not cover separate models, services or assets. [Source](https://github.com/ga642381/AudioCodec-Hub/blob/main/LICENSE)
- **Creative results · unknown:** Published creative results have not received a substantive independent quality review.
- **Reproducible setup · unknown:** A complete installation and reproducibility review is pending.
- **Maintenance and support · unknown:** Workflow-specific maintenance and blocker review remains incomplete.
- **Independent use · unknown:** Independent first-hand use has not been established in this review.
- **Models, services and costs · documented:** MIT wrapper; each pretrained model keeps its own terms. Batch decoding, multichannel handling and packaging remain incomplete; the author warns batch-code equivalence has not been carefully checked. Scope and current API examples need verification. [Source](https://github.com/ga642381/AudioCodec-Hub/blob/main/README.md)

Source review only; not installed or run. MIT wrapper; each pretrained model keeps its own terms. Batch decoding, multichannel handling and packaging remain incomplete; the author warns batch-code equivalence has not been carefully checked. Scope and current API examples need verification.

- [Official documentation](https://github.com/ga642381/AudioCodec-Hub/blob/main/README.md)
- [Complete software license reviewed](https://github.com/ga642381/AudioCodec-Hub/blob/main/LICENSE)
### LINNE · MIT

Exploring compact learned representations for WAV audio.
A linear-predictive neural network encoder implements forward/backward propagation and training for an audio compression workflow.
Full setup, hardware, model-term and output-quality review pending. MIT code, CMake >=3.15 and a native compiler build. Hardware, current platform support and lossless round-trip/bitstream guarantees require a full source and output review; a beta description alone is not a quality verdict.

### Quality assessment: Quality unverified

Software license and creative AI relevance screened; full guide and quality checks remain pending.

Scope: Exploring compact learned representations for WAV audio.

Evidence checked: 2026-10-22. No local execution implied.

- **Open-source software license · verified:** Complete software license read and archived; this grant does not cover separate models, services or assets. [Source](https://github.com/aikiriao/LINNE/blob/main/COPYING)
- **Creative results · unknown:** Published creative results have not received a substantive independent quality review.
- **Reproducible setup · unknown:** A complete installation and reproducibility review is pending.
- **Maintenance and support · unknown:** Workflow-specific maintenance and blocker review remains incomplete.
- **Independent use · unknown:** Independent first-hand use has not been established in this review.
- **Models, services and costs · documented:** MIT code, CMake >=3.15 and a native compiler build. Hardware, current platform support and lossless round-trip/bitstream guarantees require a full source and output review; a beta description alone is not a quality verdict. [Source](https://github.com/aikiriao/LINNE/blob/main/README.md)

Source review only; not installed or run. MIT code, CMake >=3.15 and a native compiler build. Hardware, current platform support and lossless round-trip/bitstream guarantees require a full source and output review; a beta description alone is not a quality verdict.

- [Official documentation](https://github.com/aikiriao/LINNE/blob/main/README.md)
- [Complete software license reviewed](https://github.com/aikiriao/LINNE/blob/main/COPYING)
- [Neural predictor and trainer implementation](https://github.com/aikiriao/LINNE/blob/main/libs/linne_network/src/linne_network.c)
- [Neural predictor and trainer implementation](https://github.com/aikiriao/LINNE/blob/main/libs/linne_network/src/linne_network.c)
### VieNeu Audio Studio · Apache-2.0

Vietnamese narration and dialogue drafts.
A local Vietnamese speech application combines text-to-speech, voice conditioning and multi-character dialogue with API/MCP access.
Full setup, hardware, model-term and output-quality review pending. Apache-2.0 software, with separate VieNeu and optional global-model/voice-asset terms. The README documents Windows, macOS and Linux installers, 4 GB minimum/8 GB recommended RAM and about 5 GB disk, but complete release, model and output review remains pending. Its optional global mode cites Higgs and Llama community terms; unsigned installers and automatic-start choices need review.

### Quality assessment: Quality unverified

Software license and creative AI relevance screened; full guide and quality checks remain pending.

Scope: Vietnamese narration and dialogue drafts.

Evidence checked: 2026-10-22. No local execution implied.

- **Open-source software license · verified:** Complete software license read and archived; this grant does not cover separate models, services or assets. [Source](https://github.com/sonlovinbot-team/vieneu-audio-studio/blob/main/LICENSE)
- **Creative results · unknown:** Published creative results have not received a substantive independent quality review.
- **Reproducible setup · unknown:** A complete installation and reproducibility review is pending.
- **Maintenance and support · unknown:** Workflow-specific maintenance and blocker review remains incomplete.
- **Independent use · unknown:** Independent first-hand use has not been established in this review.
- **Models, services and costs · documented:** Apache-2.0 software, with separate VieNeu and optional global-model/voice-asset terms. The README documents Windows, macOS and Linux installers, 4 GB minimum/8 GB recommended RAM and about 5 GB disk, but complete release, model and output review remains pending. Its optional global mode cites Higgs and Llama community terms; unsigned installers and automatic-start choices need review. [Source](https://github.com/sonlovinbot-team/vieneu-audio-studio/blob/main/README.md)

Source review only; not installed or run. Apache-2.0 software, with separate VieNeu and optional global-model/voice-asset terms. The README documents Windows, macOS and Linux installers, 4 GB minimum/8 GB recommended RAM and about 5 GB disk, but complete release, model and output review remains pending. Its optional global mode cites Higgs and Llama community terms; unsigned installers and automatic-start choices need review.

- [Official documentation](https://github.com/sonlovinbot-team/vieneu-audio-studio/blob/main/README.md)
- [Complete software license reviewed](https://github.com/sonlovinbot-team/vieneu-audio-studio/blob/main/LICENSE)
### ThothPad · GPL-3.0

Writer-controlled draft comparison and model-assisted revision.
Optional language-model revision and agent tools operate alongside local prose diagnostics for manuscripts and creative writing.
Full setup, hardware, model-term and output-quality review pending. GPL-3.0-or-later derivative of Ghostwriter; Qt, Python 3.11+, grammar components and optional cloud/local model terms are separate. Most prose metrics are deterministic; they are not authorship detection. Native setup, component notices and quality evidence remain pending.

### Quality assessment: Quality unverified

Software license and creative AI relevance screened; full guide and quality checks remain pending.

Scope: Writer-controlled draft comparison and model-assisted revision.

Evidence checked: 2026-10-22. No local execution implied.

- **Open-source software license · verified:** Complete software license read and archived; this grant does not cover separate models, services or assets. [Source](https://github.com/anoracleofra-code/Thothpad/blob/main/COPYING)
- **Creative results · unknown:** Published creative results have not received a substantive independent quality review.
- **Reproducible setup · unknown:** A complete installation and reproducibility review is pending.
- **Maintenance and support · unknown:** Workflow-specific maintenance and blocker review remains incomplete.
- **Independent use · unknown:** Independent first-hand use has not been established in this review.
- **Models, services and costs · documented:** GPL-3.0-or-later derivative of Ghostwriter; Qt, Python 3.11+, grammar components and optional cloud/local model terms are separate. Most prose metrics are deterministic; they are not authorship detection. Native setup, component notices and quality evidence remain pending. [Source](https://github.com/anoracleofra-code/Thothpad/blob/main/README.md)

Source review only; not installed or run. GPL-3.0-or-later derivative of Ghostwriter; Qt, Python 3.11+, grammar components and optional cloud/local model terms are separate. Most prose metrics are deterministic; they are not authorship detection. Native setup, component notices and quality evidence remain pending.

- [Official documentation](https://github.com/anoracleofra-code/Thothpad/blob/main/README.md)
- [Complete software license reviewed](https://github.com/anoracleofra-code/Thothpad/blob/main/COPYING)

## Excluded and unresolved findings

Research notes only; these do not enter the eligible tool library.

- **SLRT** · needs-license-review: No complete software license was found in the collected repository license endpoint/root evidence. A sign-language paper and public code are insufficient to establish eligibility. [Source](https://github.com/FangyunWei/SLRT)
- **avatar-pose** · needs-license-review: The collected license endpoint returned 404 and no root license was established. Not counted as an eligible avatar tool. [Source](https://github.com/fhswf/avatar-pose)
- **DeepCalliFont** · needs-license-review: The official repository was located from the paper, but a complete software license could not be collected. [Source](https://github.com/lsflyt-pku/DeepCalliFont)
- **BrushOS** · needs-license-review: A concrete robotic-painting description was found, but the repository license endpoint returned 404; code-license review remains unresolved. [Source](https://github.com/Legedith/BrushOS-Robotic-painting-in-action)
- **Neural-tilde** · excluded: The package documentation explicitly describes extensive reuse of nn~ code under CC BY-NC 4.0. Noncommercial software terms do not meet this library’s open-source-only rule. [Source](https://pypi.org/project/neural-tilde/)
- **MaterialSearch** · needs-license-review: The current README says source is intentionally obfuscated and the API implementation is not open source. A root GPL label does not establish complete corresponding source for the assessed search application. [Source](https://github.com/chn-lee-yumi/MaterialSearch)
- **Timeline Studio** · needs-license-review: The root license is MIT, but the README describes use as solely technical research and learning. The scope of that additional wording needs clarification before an unrestricted software eligibility claim. [Source](https://github.com/MartinDelophy/ai-video-editor)
- **Knit-by-Command** · excluded: The reviewed README has project goals and a placeholder for usage instructions; an implemented generative-AI knitting workflow was not established. [Source](https://github.com/HiDefTextiles/Knit-By-Command)
- **OmniCue** · excluded: The current source describes a concept/reference design and defensive publication, not a verified released application. Hardware and AI capability claims remain proposals. [Source](https://github.com/yargnad/OmniCue)
- **Agent Robot Avatar** · excluded: The reviewed component supplies programmed SVG states and interactions for agent interfaces. A concrete AI inference or AI-driven creative-authoring workflow was not established for the component itself. [Source](https://github.com/CX-ArtLab/agent-robot-avatar)
- **Open Design (nexu-io)** · needs-license-review: The root file is labeled Apache-2.0, but comparison of the complete text with the Apache Software Foundation original found changes to the operative trademark and warranty/liability wording. The grant is not treated as an unchanged standard Apache license solely from its SPDX label; license clarification is pending. [Source](https://github.com/nexu-io/open-design/blob/main/README.md) [Source](https://github.com/nexu-io/open-design/blob/main/LICENSE) [Source](https://www.apache.org/licenses/LICENSE-2.0.txt)
- **Fast-DACVAE** · needs-license-review: The collected root license is MIT while the README names Apache-2.0 for the project. Upstream codec and model rights need scope clarification before assigning one verified software label. [Source](https://github.com/kadirnar/fast-dacvae)
- **Story Systems Template** · needs-license-review: The root MIT grant is accompanied by a NOTICE requiring a specific prominent branded attribution. The relationship of this additional mandatory condition to the standard MIT grant needs clarification. [Source](https://github.com/bybren-llc/story-systems-template) [Source](https://github.com/bybren-llc/story-systems-template/blob/main/NOTICE)
- **NeRC** · excluded: The current repository root contains only README and license, and the README still says code will be released. A paper/demo is not a released application. [Source](https://github.com/JiaxiongQ/NeRC)
- **manifoldsplat (a-canela)** · excluded: The README is only a project title. A concrete usable creative AI workflow and its relationship to the similarly named paper could not be established. [Source](https://github.com/a-canela/manifoldsplat)
- **Papercraft-KI** · excluded: The repository describes a documentation-stage workflow; its completed cube example is not an AI-generation demonstration, and other examples/templates are placeholders. Kept as a workflow research resource rather than a released AI application. [Source](https://github.com/malkreide/papercraft-ki)

Source collection completed: 2026-10-22T13:13:35.366288+00:00
Search is a bounded sample. Stars and recent pushes are discovery signals, not verified quality or meaningful upgrades.
