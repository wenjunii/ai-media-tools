# AI Media Scout — 2026-10-07

Today completes 38 detailed guides and adds 28 further screened discoveries across 41 creative fields, including the newly added holography/light-field field. Twenty-seven guides complete earlier pending reviews; eleven are first detailed baselines. This is not a claim that these tools launched today. All 275 repository queries and 16 model-task queries succeeded. Collection and supplemental research archived 20,875 repository candidates and 752 model listings; 97 repository queries reached their configured result bounds. Model-task lists are bounded samples of up to 50 results per task. Two web ecosystems could not be inspected because of access restrictions. The full catalog and retained pilot backlog informed screening, including metadata beyond the automatic README shortlist; raw unreviewed candidates remain local. Every published entry has a reviewed complete open-source software license, with weights, services, hosts and setup limitations separated. No discovered application was installed or tested, and the search is broad rather than exhaustive.

Documentation reviewed today. Tools are not hands-on tested unless explicitly stated. Requirements and performance remain source-specific.

## Coverage

| Field | Finding |
| --- | --- |
| Images & design | MFLUX and the established Stable Diffusion WebUI receive practical guides; PotionUI was checked but has no newly verified release or creator-facing change beyond its earlier entry. Primary Krita model documentation was also checked; different model architectures and licenses prevent treating all local image tools as interchangeable. [Source 1](https://docs.interstice.cloud/models/) [Source 2](https://docs.interstice.cloud/base-models/) |
| Video, animation & film | AutoSubs, Video Subtitle Remover and HTML animation tooling extend coverage beyond video generation. Neural inpainting and subtitle recognition need output review; current official demonstrations are not independent quality tests. [Source 1](https://modelscope.cn/models/iic/ClearerVoice-Studio) [Source 2](https://antgroup.github.io/ai/echomimic_v2/) |
| Audio, music & voice | New guides span speech cleanup, transcription, music analysis, composition and live performance. Package sources for Audio as Code and sense-music were checked to distinguish external-agent authoring from embedded neural analysis. [Source 1](https://pypi.org/project/audio-as-code/) [Source 2](https://pypi.org/project/sense-music/) |
| 3D, reconstruction & assets | metal-gauss and mlx-spatial add Apple Silicon routes; Unique3D and MapAnything remain screened for fuller review. Neural reconstruction examples do not prove correct unseen geometry or production-ready meshes. [Source 1](https://research.nvidia.com/labs/dir/neuralangelo/) [Source 2](https://github.com/facebookresearch/map-anything) |
| Browser tools & web media | Local web studios and browser AI libraries were investigated. Transformers.js documentation distinguishes browser WebGPU inference from a browser interface controlling a remote GPU. [Source 1](https://huggingface.co/docs/transformers.js/guides/webgpu) [Source 2](https://ml5js.org/learn/) |
| WebXR, VR & AR | Haptic generation and holographic display synthesis widen XR coverage beyond headsets and 3D viewers. Their specialist hardware and research setup should not be confused with turnkey WebXR applications. [Source 1](https://hapticgen.hcitech.org/) [Source 2](https://www.computationalimaging.org/publications/time-multiplexed-neural-holography/) |
| Computational art & creative coding | Neural vector optimization, code-based music composition and learned optical propagation provide distinct computational-art directions. ml5.js primary learning material was also checked for accessible model-driven sketches. [Source 1](https://ml5js.org/learn/) [Source 2](https://www.computationalimaging.org/publications/time-multiplexed-neural-holography/) |
| Interactive, immersive & live media | Godot reinforcement learning, webcam-conditioned installations and tactile generation were screened. Primary educational and haptic sources supplement repositories; latency and installation reliability remain untested. [Source 1](https://ml5js.org/community/) [Source 2](https://hapticgen.hcitech.org/) |
| 3D printing & generative CAD | Tactile graphics and physical flip-dot displays were researched. Text2TactileGraphics has a concrete research demonstration, but its inspected code lacked a verified software license and remains outside the eligible library. [Source 1](https://ruihangao.github.io/Text2TactileGraphics/) [Source 2](https://github.com/mdbug/flipdot) |
| Games & production pipelines | Godot RL Agents now has a setup guide for learned game behavior. World-model discovery found an unmaintained earlier LingBot repository and a non-commercially licensed successor; neither is presented as a new unrestricted creator recommendation. [Source 1](https://github.com/edbeeching/godot_rl_agents) [Source 2](https://technology.robbyant.com/lingbot-world-v2) |
| Motion capture & character animation | Kimodo now has a guide covering motion constraints, checkpoints and export preparation. Its primary documentation separates model families and installation options; learned contact/motion still requires review. [Source 1](https://research.nvidia.com/labs/sil/projects/kimodo/docs/) [Source 2](https://research.nvidia.com/labs/sil/projects/kimodo/docs/user_guide/motion_convert.html) |
| Avatars, digital humans & lip sync | PersonaLive receives a detailed research guide, while EchoMimicV2, Champ and Linly-Talker remain screened leads. Official half-body animation examples were checked without accepting benchmark claims as local performance proof. [Source 1](https://antgroup.github.io/ai/echomimic_v2/) [Source 2](https://github.com/GVCLab/PersonaLive) |
| VFX, compositing & relighting | Blender/ComfyUI integration, portrait animation and restoration frameworks expand the VFX set. Neural relighting project sites were researched; a paper showcase alone is insufficient to certify complete reusable software. [Source 1](https://research.nvidia.com/labs/toronto-ai/DiffusionRenderer/) [Source 2](https://research.nvidia.com/labs/toronto-ai/fegr/) |
| Spatial audio & volumetric media | Mac neural-scene tooling, reconstruction and spatial-audio research were reviewed. Geometric output and inferred acoustics remain estimates requiring comparison with the original capture or measurements. [Source 1](https://research.nvidia.com/labs/toronto-ai/adaptive-shells/) [Source 2](https://arxiv.org/abs/2210.15196) |
| Photogrammetry, scanning & neural rendering | metal-gauss and MapAnything offer different learned reconstruction routes; official Neuralangelo material supplies adjacent primary context. MapAnything defaults to non-commercial weights and separately documents an Apache alternative. [Source 1](https://research.nvidia.com/labs/dir/neuralangelo/) [Source 2](https://github.com/facebookresearch/map-anything) |
| Editing, captions & post-production | Caption correction, subtitle-region inpainting and dialogue enhancement now have fuller guides. ClearerVoice primary demos were checked; restoration must be compared with the original rather than judged from a higher resolution alone. [Source 1](https://modelscope.cn/studios/iic/ClearerVoice-Studio) [Source 2](https://github.com/YaoFANGUK/video-subtitle-remover) |
| Vector graphics, illustration & textures | NeuralSVG and an Inkscape agent bridge now have detailed entries. The former optimizes generative vector art; the latter depends on an external model and a native drawing application. [Source 1](https://sagipolaczek.github.io/NeuralSVG/) [Source 2](https://www.openaccess.thecvf.com/content/ICCV2025/papers/Polaczek_NeuralSVG_An_Implicit_Representation_for_Text-to-Vector_Generation_ICCV_2025_paper.pdf) |
| Typography, fonts & layout | FontDiffuser research and neural vector work were checked alongside animated text authoring. No new standalone font application was certified from a paper alone, and known unchanged tools were not reissued as new. [Source 1](https://arxiv.org/abs/2312.12142) [Source 2](https://sagipolaczek.github.io/NeuralSVG/) |
| Storyboarding, narrative & comics | Comic translation, portrait animation, expressive audio and agent-authored videos broaden narrative workflows. The report distinguishes source-code licensing from voice/model and source-media conditions. [Source 1](https://antgroup.github.io/ai/echomimic_v2/) [Source 2](https://noscribe.de/en/docs/usage/) |
| Creative publishing & presentation | Flint Chart, PPT Master, Comic Translate and transcript tools now have practical guides. Editable output is useful, but generated chart data, translation and slide claims need review. [Source 1](https://microsoft.github.io/flint-chart/) [Source 2](https://hugohe3.github.io/ppt-master-examples/) |
| Photography, restoration & color | QualityScaler, MFLUX and collection-search tools cover restoration, generation and retrieval. Primary model documentation was checked; HomeGallery’s default preview transmission is explicitly disclosed in its guide. [Source 1](https://docs.interstice.cloud/selections/) [Source 2](https://demo.home-gallery.org) |
| Data art & scientific visualization | AI-agent chart and slide authoring is joined by semantic SVG diagram tooling. Microsoft’s live project gallery was checked; external-agent dependence is separated from deterministic rendering. [Source 1](https://microsoft.github.io/flint-chart/) [Source 2](https://github.com/yizhiyanhua-ai/fireworks-tech-graph) |
| Physical, robotic & kinetic installations | Interactive portrait generation, flip-dot vision and vibrotactile signals broaden installation discovery. HapticGen has useful research code but incomplete turnkey setup and non-commercial weights. [Source 1](https://hapticgen.hcitech.org/) [Source 2](https://github.com/burakkagann/dissolution) |
| Performance, projection & stage media | Cypher DJ, music-library analysis and neural amplifier effects support performance experiments. The Cypher DJ project and archived DDSP-VST work were checked; beta/archived status is retained instead of implying production reliability. [Source 1](https://www.infinimind-creations.com/instruments/cypher-dj/) [Source 2](https://magenta.tensorflow.org/ddsp-vst) [Source 3](https://arxiv.org/abs/2508.09126) |
| Fashion, textiles & wearable media | Garment generation and reconstruction research were investigated. GarmentDiffusion and Garment-GPT lacked verified software licenses in the inspected repositories; SwiftTailor’s announced code path did not establish an eligible released application. [Source 1](https://arxiv.org/abs/2609.18483) [Source 2](https://proceedings.iclr.cc/paper_files/paper/2026/hash/34b70ece5f8d273fd670a17e2248d034-Abstract-Conference.html) [Source 3](https://qualcomm-ai-research.github.io/SwiftTailor/) |
| Accessible media & assistive creation | noScribe, AutoSubs, Android dictation, score recognition and tactile research cover multiple access needs. Platform/version differences and optional non-commercial model components are visible in the profiles. [Source 1](https://noscribe.de/en/docs/download-installation/) [Source 2](https://ruihangao.github.io/Text2TactileGraphics/) |
| Mobile, edge & on-device creation | OpenWispr for Android now has a guide with its actual Android minimum and local/cloud distinction. Maintainer mobile speech material and browser WebGPU documentation were also checked; browser access does not establish local inference. [Source 1](https://huggingface.co/blog/aufklarer/offline-voice-agent-android) [Source 2](https://huggingface.co/docs/transformers.js/guides/webgpu) |
| Creative learning & authoring | Godot RL, Amphion recipes, ml5.js tutorials and editable music code support learning-by-modification. These are documented educational/developer routes rather than uniform beginner-ready applications. [Source 1](https://ml5js.org/learn/) [Source 2](https://ml5js.org/community/) [Source 3](https://pypi.org/project/audio-as-code/) |
| Archives, media restoration & collections | Transcription, score recovery, collection search and restoration were researched alongside CLAMS audiovisual-archive work. Non-commercial film-restoration material and unlicensed Nuke examples were kept outside the eligible set. [Source 1](https://clams.ai/) [Source 2](https://noscribe.de/en/docs/usage/) |
| Emerging & cross-disciplinary creative AI | Light-field/holographic media is a newly added field, alongside existing tactile, olfactory and neural-acoustic directions. Newness of an idea or repository is not evidence of an open license or production quality. [Source 1](https://www.computationalimaging.org/publications/time-multiplexed-neural-holography/) [Source 2](https://hapticgen.hcitech.org/) |
| Tactile, vibration and haptic media | HapticGen was revisited, including setup gaps and separate CC-BY-NC model terms; its unchanged existing guide is not repeated in this edition. Text2TactileGraphics remains unresolved on software licensing, despite a concrete physical-output demonstration. [Source 1](https://hapticgen.hcitech.org/) [Source 2](https://ruihangao.github.io/Text2TactileGraphics/) |
| Neural acoustics and responsive sound spaces | Neural HRTF and acoustic-filter research was checked for personalized spatial audio. Existing pending candidates remain in the queue; the papers alone do not establish a new ready-to-install creator application. [Source 1](https://arxiv.org/abs/2210.15196) [Source 2](https://arxiv.org/abs/2501.13017) [Source 3](https://arxiv.org/abs/2402.17907) |
| AI agents for code-authored media production | Detailed guides now cover agent-driven charts, vector documents, presentations, videos and editable music. External models make the creative decisions; deterministic media engines are identified as such. [Source 1](https://microsoft.github.io/flint-chart/) [Source 2](https://hugohe3.github.io/ppt-master-examples/) [Source 3](https://pypi.org/project/audio-as-code/) |
| AI kinetic typography and animated lettering | HTML video and AI-authored browser slides provide code-based text-animation routes. Font-generation research was also checked; this does not establish native compatibility with every motion-design host. [Source 1](https://arxiv.org/abs/2312.12142) [Source 2](https://github.com/nexu-io/html-video) |
| AI choreography and dance composition | Kimodo’s path/keyframe/contact controls broaden movement authoring, while pose-driven avatar projects offer adjacent visualizations. Exported motion still needs retargeting, contact and timing review. [Source 1](https://research.nvidia.com/labs/sil/projects/kimodo/) [Source 2](https://research.nvidia.com/labs/sil/projects/kimodo/docs/user_guide/motion_convert.html) |
| AI-assisted textile and computational craft | Learned knitting/inverse-design research and physical-media controllers were investigated. Announcements and studies without a verified released software license remain gaps; no fabrication readiness is inferred from an export. [Source 1](https://arxiv.org/abs/2504.14007) [Source 2](https://purlwiselabs.com/) [Source 3](https://ruihangao.github.io/Text2TactileGraphics/) |
| AI music notation and score recovery | HOMR GUI now has a score-recognition guide and Audio as Code adds editable symbolic composition. Recognition and MIDI playback require musical proofreading; agent composition is separate from neural audio synthesis. [Source 1](https://pypi.org/project/audio-as-code/) [Source 2](https://github.com/quackone/HOMR_GUI) |
| Neural relighting and material recovery | NVIDIA TRON, DiffusionRenderer and FEGR project material was researched. These are primary research findings; none was newly promoted solely because an impressive relighting demo exists. [Source 1](https://research.nvidia.com/labs/sil/projects/tron/) [Source 2](https://research.nvidia.com/labs/toronto-ai/DiffusionRenderer/) [Source 3](https://research.nvidia.com/labs/toronto-ai/fegr/) |
| Olfactory and multisensory AI media | AI-assisted image-to-scent narrative research was revisited through MIT Media Lab primary pages. No newly verified open-source application was established, so this remains an explicit software-availability/license gap. [Source 1](https://www.media.mit.edu/projects/anemoia-device/overview/) [Source 2](https://tangible.media.mit.edu/project/the-anemoia-device/) |
| AI architectural visualization and spatial design | Learned indoor scene composition and spatial reconstruction remain relevant. InstructScene primary examples were checked; its already-published unchanged entry was not recycled as a new daily guide. [Source 1](https://chenguolin.github.io/projects/InstructScene/) [Source 2](https://research.nvidia.com/labs/toronto-ai/adaptive-shells/) |
| Neural holography and light-field media | The added holography/light-field field produced detailed guides for Time-multiplexed Neural Holography, Neural 3D Holography, NeLF-Pro and SIGNET, plus a screened PINN-shaper lead. The older Neural Holography code has non-commercial academic terms and is excluded; light-field-stitching research remains a further lead. [Source 1](https://www.computationalimaging.org/publications/time-multiplexed-neural-holography/) [Source 2](https://www.computationalimaging.org/publications/neuralholography/) [Source 3](https://light.princeton.edu/wp-content/uploads/2024/09/neuls_paper.pdf) |

## Search and review counts

41 creative fields; 275/275 repository queries attempted; 16/16 model-task queries attempted. 20875 distinct source candidates and 752 model leads. 38 detailed profiles and 28 additional screened discoveries. Source gaps: 0 failed repository queries, 0 partial repository queries, 97 bounded repository queries, 0 failed model-task queries and 2 web ecosystem gaps. Raw search candidates include duplicates of known tools, excluded projects and projects awaiting review; they are not verified recommendations.

## Research beyond GitHub

- **gitlab** · searched: Official UmeAiRT ComfyUI toolkit tags were reviewed, including video-workflow fixes. Complete software-license eligibility was not established for an additional published entry. [Source](https://gitlab.com/UmeAiRT-Studio/comfyui-umeairt-toolkit/-/tags)
- **codeberg** · gap: Live research was blocked by robots restrictions, so Codeberg content could not be inspected. This is an access gap, not evidence that no relevant tools exist.
- **sourcehut** · gap: Live research was blocked by robots restrictions, so SourceHut content could not be inspected. No unverified candidate is promoted from that source group.
- **packages** · searched: Audio as Code and sense-music package pages were inspected alongside their source repositories, covering agent composition and optional neural audio analysis. [Source](https://pypi.org/project/audio-as-code/) [Source](https://pypi.org/project/sense-music/)
- **creative-plugins** · searched: Primary Krita AI model/install/selection documentation, Blender integration sources and neural-audio plug-in research were checked. Host and model conditions remain separate. [Source](https://docs.interstice.cloud/installation/) [Source](https://docs.interstice.cloud/models/) [Source](https://magenta.tensorflow.org/ddsp-vst) [Source](https://arxiv.org/abs/2508.09126)
- **project-sites** · searched: Official noScribe, Kimodo, NeuralSVG, HapticGen and computational-imaging sites were reviewed for actual workflows, demonstrations and setup constraints. [Source](https://noscribe.de/en/docs/download-installation/) [Source](https://research.nvidia.com/labs/sil/projects/kimodo/docs/) [Source](https://sagipolaczek.github.io/NeuralSVG/) [Source](https://hapticgen.hcitech.org/)
- **research-code** · searched: Primary papers/project pages were traced to released code for motion, neural SVG, haptics, tactile graphics and holography. Missing and non-commercial software licenses remain explicit exclusions. [Source](https://research.nvidia.com/labs/sil/projects/kimodo/) [Source](https://www.computationalimaging.org/publications/time-multiplexed-neural-holography/) [Source](https://ruihangao.github.io/Text2TactileGraphics/)
- **international** · searched: ModelScope ClearerVoice demos, Chinese/English subtitle-removal documentation and international avatar research were checked. Published demos do not establish tested local installation. [Source](https://modelscope.cn/models/iic/ClearerVoice-Studio) [Source](https://modelscope.cn/studios/iic/ClearerVoice-Studio) [Source](https://antgroup.github.io/ai/echomimic_v2/)

## Collection limitations

- images: bounded or incomplete query: topic:diffusion is:public fork:false archived:false (200 of 1427 matches sampled)
- images: bounded or incomplete query: AI image generation pushed:>=2026-09-07 is:public fork:false archived:false (200 of 1636 matches sampled)
- images: bounded or incomplete query: AI image generation created:>=2026-09-07 is:public fork:false archived:false (200 of 815 matches sampled)
- images: bounded or incomplete query: AI image generation is:public fork:false archived:false (200 of 15405 matches sampled)
- video: bounded or incomplete query: AI video pushed:>=2026-09-07 is:public fork:false archived:false (200 of 12414 matches sampled)
- video: bounded or incomplete query: AI video created:>=2026-09-07 is:public fork:false archived:false (200 of 7830 matches sampled)
- video: bounded or incomplete query: AI video is:public fork:false archived:false (200 of 83211 matches sampled)
- video: bounded or incomplete query: topic:video-generation pushed:>=2026-09-07 is:public fork:false archived:false (200 of 1558 matches sampled)
- video: bounded or incomplete query: topic:video-generation created:>=2026-09-07 is:public fork:false archived:false (200 of 628 matches sampled)
- video: bounded or incomplete query: topic:video-generation is:public fork:false archived:false (200 of 3900 matches sampled)
- audio: bounded or incomplete query: topic:music-generation pushed:>=2026-09-07 is:public fork:false archived:false (200 of 301 matches sampled)
- audio: bounded or incomplete query: topic:music-generation is:public fork:false archived:false (500 of 1191 matches sampled)
- audio: bounded or incomplete query: AI audio pushed:>=2026-09-07 is:public fork:false archived:false (200 of 3779 matches sampled)
- audio: bounded or incomplete query: AI audio created:>=2026-09-07 is:public fork:false archived:false (200 of 2033 matches sampled)
- audio: bounded or incomplete query: AI audio is:public fork:false archived:false (200 of 27714 matches sampled)
- 3d: bounded or incomplete query: 3D generation pushed:>=2026-09-07 is:public fork:false archived:false (200 of 665 matches sampled)
- 3d: bounded or incomplete query: 3D generation created:>=2026-09-07 is:public fork:false archived:false (200 of 341 matches sampled)
- 3d: bounded or incomplete query: 3D generation is:public fork:false archived:false (200 of 5786 matches sampled)
- 3d: bounded or incomplete query: topic:3d-reconstruction pushed:>=2026-09-07 is:public fork:false archived:false (200 of 252 matches sampled)
- 3d: bounded or incomplete query: topic:3d-reconstruction is:public fork:false archived:false (200 of 1908 matches sampled)
- web: bounded or incomplete query: topic:webgpu pushed:>=2026-09-07 is:public fork:false archived:false (200 of 1043 matches sampled)
- web: bounded or incomplete query: topic:webgpu created:>=2026-09-07 is:public fork:false archived:false (200 of 432 matches sampled)
- web: bounded or incomplete query: topic:webgpu is:public fork:false archived:false (200 of 2834 matches sampled)
- xr: bounded or incomplete query: AI VR pushed:>=2026-09-07 is:public fork:false archived:false (200 of 329 matches sampled)
- xr: bounded or incomplete query: AI VR is:public fork:false archived:false (200 of 2851 matches sampled)
- computational: bounded or incomplete query: AI creative coding is:public fork:false archived:false (200 of 915 matches sampled)
- computational: bounded or incomplete query: topic:generative-art pushed:>=2026-09-07 is:public fork:false archived:false (200 of 862 matches sampled)
- computational: bounded or incomplete query: topic:generative-art created:>=2026-09-07 is:public fork:false archived:false (200 of 422 matches sampled)
- computational: bounded or incomplete query: topic:generative-art is:public fork:false archived:false (200 of 3909 matches sampled)
- interactive: bounded or incomplete query: AI interactive art is:public fork:false archived:false (200 of 674 matches sampled)
- fabrication: bounded or incomplete query: AI CAD pushed:>=2026-09-07 is:public fork:false archived:false (200 of 673 matches sampled)
- fabrication: bounded or incomplete query: AI CAD created:>=2026-09-07 is:public fork:false archived:false (200 of 369 matches sampled)
- fabrication: bounded or incomplete query: AI CAD is:public fork:false archived:false (200 of 3005 matches sampled)
- fabrication: bounded or incomplete query: AI 3D printing is:public fork:false archived:false (200 of 344 matches sampled)
- gaming: bounded or incomplete query: AI game assets is:public fork:false archived:false (200 of 634 matches sampled)
- gaming: bounded or incomplete query: AI blender pushed:>=2026-09-07 is:public fork:false archived:false (200 of 415 matches sampled)
- gaming: bounded or incomplete query: AI blender created:>=2026-09-07 is:public fork:false archived:false (200 of 298 matches sampled)
- gaming: bounded or incomplete query: AI blender is:public fork:false archived:false (200 of 1547 matches sampled)
- motion: bounded or incomplete query: AI motion capture is:public fork:false archived:false (200 of 231 matches sampled)
- motion: bounded or incomplete query: motion generation is:public fork:false archived:false (200 of 1497 matches sampled)
- avatars: bounded or incomplete query: AI avatar pushed:>=2026-09-07 is:public fork:false archived:false (200 of 743 matches sampled)
- avatars: bounded or incomplete query: AI avatar created:>=2026-09-07 is:public fork:false archived:false (200 of 398 matches sampled)
- avatars: bounded or incomplete query: AI avatar is:public fork:false archived:false (200 of 5874 matches sampled)
- avatars: bounded or incomplete query: lip sync pushed:>=2026-09-07 is:public fork:false archived:false (200 of 295 matches sampled)
- avatars: bounded or incomplete query: lip sync is:public fork:false archived:false (200 of 2394 matches sampled)
- vfx: bounded or incomplete query: AI visual effects is:public fork:false archived:false (200 of 418 matches sampled)
- capture: bounded or incomplete query: topic:gaussian-splatting pushed:>=2026-09-07 is:public fork:false archived:false (200 of 240 matches sampled)
- capture: bounded or incomplete query: topic:gaussian-splatting is:public fork:false archived:false (500 of 907 matches sampled)
- capture: bounded or incomplete query: neural reconstruction is:public fork:false archived:false (200 of 1318 matches sampled)
- editing: bounded or incomplete query: AI video editing pushed:>=2026-09-07 is:public fork:false archived:false (200 of 813 matches sampled)
- editing: bounded or incomplete query: AI video editing created:>=2026-09-07 is:public fork:false archived:false (200 of 515 matches sampled)
- editing: bounded or incomplete query: AI video editing is:public fork:false archived:false (200 of 3409 matches sampled)
- editing: bounded or incomplete query: AI subtitle pushed:>=2026-09-07 is:public fork:false archived:false (200 of 362 matches sampled)
- editing: bounded or incomplete query: AI subtitle is:public fork:false archived:false (200 of 2207 matches sampled)
- vector: bounded or incomplete query: AI SVG pushed:>=2026-09-07 is:public fork:false archived:false (200 of 428 matches sampled)
- vector: bounded or incomplete query: AI SVG created:>=2026-09-07 is:public fork:false archived:false (200 of 236 matches sampled)
- vector: bounded or incomplete query: AI SVG is:public fork:false archived:false (200 of 1776 matches sampled)
- typography: bounded or incomplete query: AI typography is:public fork:false archived:false (200 of 648 matches sampled)
- typography: bounded or incomplete query: font generation is:public fork:false archived:false (400 of 417 matches sampled)
- storytelling: bounded or incomplete query: AI storyboard pushed:>=2026-09-07 is:public fork:false archived:false (200 of 373 matches sampled)
- storytelling: bounded or incomplete query: AI storyboard created:>=2026-09-07 is:public fork:false archived:false (200 of 217 matches sampled)
- storytelling: bounded or incomplete query: AI storyboard is:public fork:false archived:false (200 of 1679 matches sampled)
- storytelling: bounded or incomplete query: AI comic pushed:>=2026-09-07 is:public fork:false archived:false (200 of 1688 matches sampled)
- storytelling: bounded or incomplete query: AI comic created:>=2026-09-07 is:public fork:false archived:false (200 of 1611 matches sampled)
- storytelling: bounded or incomplete query: AI comic is:public fork:false archived:false (200 of 2966 matches sampled)
- publishing: bounded or incomplete query: AI presentation pushed:>=2026-09-07 is:public fork:false archived:false (200 of 1123 matches sampled)
- publishing: bounded or incomplete query: AI presentation created:>=2026-09-07 is:public fork:false archived:false (200 of 680 matches sampled)
- publishing: bounded or incomplete query: AI presentation is:public fork:false archived:false (200 of 8456 matches sampled)
- publishing: bounded or incomplete query: AI publishing pushed:>=2026-09-07 is:public fork:false archived:false (200 of 1063 matches sampled)
- publishing: bounded or incomplete query: AI publishing created:>=2026-09-07 is:public fork:false archived:false (200 of 647 matches sampled)
- publishing: bounded or incomplete query: AI publishing is:public fork:false archived:false (200 of 4005 matches sampled)
- photography: bounded or incomplete query: AI colorization pushed:>=2026-09-07 is:public fork:false archived:false (200 of 438 matches sampled)
- photography: bounded or incomplete query: AI colorization created:>=2026-09-07 is:public fork:false archived:false (200 of 275 matches sampled)
- photography: bounded or incomplete query: AI colorization is:public fork:false archived:false (200 of 4715 matches sampled)
- visualization: bounded or incomplete query: AI visualization pushed:>=2026-09-07 is:public fork:false archived:false (200 of 3216 matches sampled)
- visualization: bounded or incomplete query: AI visualization created:>=2026-09-07 is:public fork:false archived:false (200 of 1860 matches sampled)
- visualization: bounded or incomplete query: AI visualization is:public fork:false archived:false (200 of 37577 matches sampled)
- visualization: bounded or incomplete query: AI data art is:public fork:false archived:false (200 of 1016 matches sampled)
- performance: bounded or incomplete query: AI live visuals is:public fork:false archived:false (200 of 704 matches sampled)
- fashion: bounded or incomplete query: AI fashion design is:public fork:false archived:false (200 of 636 matches sampled)
- fashion: bounded or incomplete query: AI textile is:public fork:false archived:false (200 of 466 matches sampled)
- accessibility: bounded or incomplete query: AI audio description is:public fork:false archived:false (200 of 254 matches sampled)
- mobile: bounded or incomplete query: AI mobile media is:public fork:false archived:false (200 of 207 matches sampled)
- education: bounded or incomplete query: AI explainer pushed:>=2026-09-07 is:public fork:false archived:false (200 of 6435 matches sampled)
- education: bounded or incomplete query: AI explainer created:>=2026-09-07 is:public fork:false archived:false (200 of 4395 matches sampled)
- education: bounded or incomplete query: AI explainer is:public fork:false archived:false (200 of 36889 matches sampled)
- frontier: bounded or incomplete query: AI creative tools pushed:>=2026-09-07 is:public fork:false archived:false (200 of 235 matches sampled)
- frontier: bounded or incomplete query: AI creative tools is:public fork:false archived:false (200 of 1941 matches sampled)
- frontier: bounded or incomplete query: AI digital art is:public fork:false archived:false (200 of 718 matches sampled)
- frontier: bounded or incomplete query: AI multimedia is:public fork:false archived:false (200 of 1169 matches sampled)
- frontier: bounded or incomplete query: AI new media is:public fork:false archived:false (200 of 501 matches sampled)
- neural-acoustics: bounded or incomplete query: neural acoustic is:public fork:false archived:false (200 of 345 matches sampled)
- agent-media-production: bounded or incomplete query: AI agent animation is:public fork:false archived:false (200 of 502 matches sampled)
- agent-media-production: bounded or incomplete query: AI agent video editing is:public fork:false archived:false (200 of 430 matches sampled)
- architectural-media: bounded or incomplete query: AI architectural visualization is:public fork:false archived:false (200 of 902 matches sampled)
- architectural-media: bounded or incomplete query: AI floor plan is:public fork:false archived:false (200 of 628 matches sampled)
- light-field: bounded or incomplete query: AI hologram is:public fork:false archived:false (200 of 203 matches sampled)

## MFLUX

Images & design · Photography, restoration & color · Computational art & creative coding

Completed the detailed guide for an earlier screened discovery. Documentation and complete software license checked on 2026-10-07; no claim of a new release today.

### How it uses AI

Runs pretrained generative image models, with quantization and model-specific controls rather than a hosted image API wrapper. [Source](https://github.com/mflux-community/mflux/blob/main/README.md) [Source](https://github.com/mflux-community/mflux/blob/main/src/mflux/models/z_image/README.md) [Source](https://github.com/mflux-community/mflux/blob/main/pyproject.toml)

### Introduction

A Python and command-line image-generation toolkit built around MLX, with model-specific editing, conditioning and LoRA workflows. [Source 1](https://github.com/mflux-community/mflux/blob/main/README.md) [Source 2](https://github.com/mflux-community/mflux/blob/main/src/mflux/models/z_image/README.md) [Source 3](https://github.com/mflux-community/mflux/blob/main/pyproject.toml)

### What it is good for

Developing image variations and locally reproducible visual experiments on supported hardware. [Source 1](https://github.com/mflux-community/mflux/blob/main/README.md) [Source 2](https://github.com/mflux-community/mflux/blob/main/src/mflux/models/z_image/README.md) [Source 3](https://github.com/mflux-community/mflux/blob/main/pyproject.toml)

### Demo & examples

The README and model guides show developer-generated examples and reproducible prompts. [Source 1](https://github.com/mflux-community/mflux/blob/main/README.md)

### Install

Documented setup guidance; these commands were not executed during this review. [Source 1](https://github.com/mflux-community/mflux/blob/main/README.md) [Source 2](https://github.com/mflux-community/mflux/blob/main/src/mflux/models/z_image/README.md) [Source 3](https://github.com/mflux-community/mflux/blob/main/pyproject.toml)

1. Install uv and the package on a documented platform.
2. Choose a supported model and review its weight license; initial use downloads model files.
3. Start with the documented quantized Z-Image Turbo example.

```sh
uv tool install --upgrade mflux
```


```sh
mflux-generate-z-image-turbo --prompt "A puffin standing on a cliff" --seed 42 -q 8
```

### First project

Begin with a small example and inspect the result before using it in production. [Source 1](https://github.com/mflux-community/mflux/blob/main/README.md) [Source 2](https://github.com/mflux-community/mflux/blob/main/src/mflux/models/z_image/README.md) [Source 3](https://github.com/mflux-community/mflux/blob/main/pyproject.toml)

1. Generate a small batch with a fixed seed.
2. Change one prompt or conditioning input at a time and retain parameters with the output.
### Hardware & software

Source-backed requirements; unreported minimums remain unknown. [Source 1](https://github.com/mflux-community/mflux/blob/main/README.md) [Source 2](https://github.com/mflux-community/mflux/blob/main/src/mflux/models/z_image/README.md) [Source 3](https://github.com/mflux-community/mflux/blob/main/pyproject.toml)

- **Hardware:** Apple Silicon is the main documented route; no universal RAM minimum is given. Z-Image documentation describes roughly 31 GB of unquantized weights; quantization reduces storage/memory needs. Other models differ.
- **Software:** Published package requires Python >=3.10; developer tooling uses >=3.13. uv, MLX and selected model files are required.
- **Platforms:** macOS on Apple Silicon is documented. A separate NVIDIA DGX installation route is also documented; this does not establish general Windows/Linux GPU support.

### License, model weights & costs

The complete top-level MIT software license was reviewed and archived. Dependent models and components retain their own terms. [Source 1](https://github.com/mflux-community/mflux/blob/main/LICENSE) [Source 2](https://github.com/mflux-community/mflux/blob/main/README.md) [Source 3](https://github.com/mflux-community/mflux/blob/main/src/mflux/models/z_image/README.md) [Source 4](https://github.com/mflux-community/mflux/blob/main/pyproject.toml)

- **Code:** MIT
- **Weights:** MIT application code; each model and LoRA retains independent terms, including restrictions or gated access where applicable.
- **Commercial:** The reviewed software license permits commercial software use subject to its obligations; it does not clear independent weights, data, assets, services or dependencies.
- **Cost:** Source code is available under the stated license. Compute, storage, optional hardware and any hosted model/API services can add costs; no current service-price quote is asserted.

### Why it merits attention

Included for its concrete documented creative workflow: Developing image variations and locally reproducible visual experiments on supported hardware. The documentation and developer examples support relevance; output quality, setup success and performance were not independently tested. [Source 1](https://github.com/mflux-community/mflux/blob/main/README.md) [Source 2](https://github.com/mflux-community/mflux/blob/main/src/mflux/models/z_image/README.md) [Source 3](https://github.com/mflux-community/mflux/blob/main/pyproject.toml)

### Limitations

Model support, memory and controls differ across pipelines. Documentation and examples were reviewed; generation speed and image quality were not tested. [Source 1](https://github.com/mflux-community/mflux/blob/main/README.md) [Source 2](https://github.com/mflux-community/mflux/blob/main/src/mflux/models/z_image/README.md) [Source 3](https://github.com/mflux-community/mflux/blob/main/pyproject.toml)

### Get the tool

- [Repository](https://github.com/mflux-community/mflux)
- [Documentation](https://github.com/mflux-community/mflux/blob/main/README.md)
- [License](https://github.com/mflux-community/mflux/blob/main/LICENSE)

## QualityScaler

Images & design · Video, animation & film · Archives, media restoration & collections

Completed the detailed guide for an earlier screened discovery. Documentation and complete software license checked on 2026-10-07; no claim of a new release today.

### How it uses AI

AI super-resolution models reconstruct detail; tiled processing accommodates supported GPUs. [Source](https://github.com/Djdefrag/QualityScaler/blob/main/README.md)

### Introduction

A Windows desktop application for neural image/video upscaling and denoising using ONNX models. [Source 1](https://github.com/Djdefrag/QualityScaler/blob/main/README.md)

### What it is good for

Preparing low-resolution photographs or clips for closer visual review and higher-resolution delivery. [Source 1](https://github.com/Djdefrag/QualityScaler/blob/main/README.md)

### Demo & examples

The README contains interface images and author before/after demonstrations. [Source 1](https://github.com/Djdefrag/QualityScaler/blob/main/README.md)

### Install

Documented setup guidance; these commands were not executed during this review. [Source 1](https://github.com/Djdefrag/QualityScaler/blob/main/README.md)

1. Use the official Windows distribution or build the MIT source.
2. For source use, install Python requirements and obtain the documented AI models and FFmpeg executable in the prescribed folders.
3. Launch QualityScaler.py and check that the intended DirectML device is selected.

```sh
pip install -r requirements.txt
```


```sh
python QualityScaler.py
```

### First project

Begin with a small example and inspect the result before using it in production. [Source 1](https://github.com/Djdefrag/QualityScaler/blob/main/README.md)

1. Load one image or short clip and select a model and scale.
2. Preview fine edges and faces, then process the full input after choosing suitable tiling.
### Hardware & software

Source-backed requirements; unreported minimums remain unknown. [Source 1](https://github.com/Djdefrag/QualityScaler/blob/main/README.md)

- **Hardware:** README specifies 8 GB RAM and a DirectX 12 GPU with at least 4 GB VRAM. Free-storage minimum is not documented.
- **Software:** Windows 10/11, Python source environment, ONNX/DirectML and FFmpeg; consult the current requirements file for dependency versions.
- **Platforms:** Windows; compatible AMD, Intel and NVIDIA GPUs are described. Native macOS/Linux support is not established.

### License, model weights & costs

The complete top-level MIT software license was reviewed and archived. Dependent models and components retain their own terms. [Source 1](https://github.com/Djdefrag/QualityScaler/blob/main/LICENSE) [Source 2](https://github.com/Djdefrag/QualityScaler/blob/main/README.md)

- **Code:** MIT
- **Weights:** MIT source; downloaded model terms and FFmpeg licensing remain separate.
- **Commercial:** The reviewed software license permits commercial software use subject to its obligations; it does not clear independent weights, data, assets, services or dependencies.
- **Cost:** MIT source is available without a software license fee. Packaged Steam/itch.io releases are paid options; current prices were not verified.

### Why it merits attention

Included for its concrete documented creative workflow: Preparing low-resolution photographs or clips for closer visual review and higher-resolution delivery. The documentation and developer examples support relevance; output quality, setup success and performance were not independently tested. [Source 1](https://github.com/Djdefrag/QualityScaler/blob/main/README.md)

### Limitations

Invented detail and temporal inconsistency remain possible. Paid packaged builds and free source are different distribution routes. [Source 1](https://github.com/Djdefrag/QualityScaler/blob/main/README.md)

### Get the tool

- [Repository](https://github.com/Djdefrag/QualityScaler)
- [Documentation](https://github.com/Djdefrag/QualityScaler/blob/main/README.md)
- [License](https://github.com/Djdefrag/QualityScaler/blob/main/LICENSE)

## Comic Translate

Images & design · Storyboarding, narrative & comics · Creative publishing & presentation · Accessible media & assistive creation

Completed the detailed guide for an earlier screened discovery. Documentation and complete software license checked on 2026-10-07; no claim of a new release today.

### How it uses AI

Neural OCR/inpainting and selected translation models automate detection, cleanup and language conversion. [Source](https://github.com/ogkalu2/comic-translate/blob/main/README.md)

### Introduction

A comic-localization interface combining text recognition, translation, inpainting and replacement lettering. [Source 1](https://github.com/ogkalu2/comic-translate/blob/main/README.md)

### What it is good for

Translating comics or illustrated narratives while retaining editable text and manual correction. [Source 1](https://github.com/ogkalu2/comic-translate/blob/main/README.md)

### Demo & examples

The official README shows the editor and translated page examples. [Source 1](https://github.com/ogkalu2/comic-translate/blob/main/README.md)

### Install

Documented setup guidance; these commands were not executed during this review. [Source 1](https://github.com/ogkalu2/comic-translate/blob/main/README.md)

1. Choose an official Windows/macOS desktop build or clone the source.
2. The source route documents Python 3.12, Git and uv; install requirements and optional NVIDIA ONNX acceleration.
3. Configure the chosen translation service/model and suitable fonts before importing pages.

```sh
uv init --python 3.12
```


```sh
uv add -r requirements.txt --compile-bytecode
```


```sh
uv run comic.py
```

### First project

Begin with a small example and inspect the result before using it in production. [Source 1](https://github.com/ogkalu2/comic-translate/blob/main/README.md)

1. Import a page, set source/target languages and review detected text regions.
2. Correct OCR and translation, inspect repaired backgrounds, adjust lettering and export.
### Hardware & software

Source-backed requirements; unreported minimums remain unknown. [Source 1](https://github.com/ogkalu2/comic-translate/blob/main/README.md)

- **Hardware:** RAM, VRAM and storage minimums are not documented. NVIDIA acceleration is optional in the source route.
- **Software:** Python 3.12/uv for source; translation credentials depend on provider. CBR/RAR input needs UnRAR, Unar or 7-Zip; fonts must cover the target language.
- **Platforms:** Windows and macOS desktop apps and a Chromium extension are documented. The inspected instructions do not establish a complete Linux support matrix.

### License, model weights & costs

The complete top-level Apache-2.0 software license was reviewed and archived. Dependent models and components retain their own terms. [Source 1](https://github.com/ogkalu2/comic-translate/blob/main/LICENSE) [Source 2](https://github.com/ogkalu2/comic-translate/blob/main/README.md)

- **Code:** Apache-2.0
- **Weights:** Apache-2.0 code; translation APIs, OCR/inpainting weights and fonts have independent terms.
- **Commercial:** The reviewed software license permits commercial software use subject to its obligations; it does not clear independent weights, data, assets, services or dependencies.
- **Cost:** Source code is available under the stated license. Compute, storage, optional hardware and any hosted model/API services can add costs; no current service-price quote is asserted.

### Why it merits attention

Included for its concrete documented creative workflow: Translating comics or illustrated narratives while retaining editable text and manual correction. The documentation and developer examples support relevance; output quality, setup success and performance were not independently tested. [Source 1](https://github.com/ogkalu2/comic-translate/blob/main/README.md)

### Limitations

OCR, context and lettering still need editorial review. Hosted translation may transmit page text/images and add charges; service pricing was not verified. [Source 1](https://github.com/ogkalu2/comic-translate/blob/main/README.md)

### Get the tool

- [Repository](https://github.com/ogkalu2/comic-translate)
- [Documentation](https://github.com/ogkalu2/comic-translate/blob/main/README.md)
- [License](https://github.com/ogkalu2/comic-translate/blob/main/LICENSE)

## noScribe

Audio, music & voice · Accessible media & assistive creation · Archives, media restoration & collections

Completed the detailed guide for an earlier screened discovery. Documentation and complete software license checked on 2026-10-07; no claim of a new release today.

### How it uses AI

Whisper-based speech recognition and neural diarization produce editable, speaker-aware transcripts. [Source](https://github.com/kaixxx/noScribe/blob/main/README.md) [Source](https://noscribe.de/en/docs/download-installation/) [Source](https://noscribe.de/en/docs/usage/) [Source](https://noscribe.de/en/docs/faq/)

### Introduction

A local interview-transcription application with speaker detection and a companion transcript editor. [Source 1](https://github.com/kaixxx/noScribe/blob/main/README.md) [Source 2](https://noscribe.de/en/docs/download-installation/) [Source 3](https://noscribe.de/en/docs/usage/) [Source 4](https://noscribe.de/en/docs/faq/)

### What it is good for

Preparing oral histories, artist interviews, documentary transcripts and searchable research recordings. [Source 1](https://github.com/kaixxx/noScribe/blob/main/README.md) [Source 2](https://noscribe.de/en/docs/download-installation/) [Source 3](https://noscribe.de/en/docs/usage/) [Source 4](https://noscribe.de/en/docs/faq/)

### Demo & examples

The official site includes usage documentation and the transcript-editor workflow. [Source 1](https://noscribe.de/en/docs/download-installation/)

### Install

Documented setup guidance; these commands were not executed during this review. [Source 1](https://github.com/kaixxx/noScribe/blob/main/README.md) [Source 2](https://noscribe.de/en/docs/download-installation/) [Source 3](https://noscribe.de/en/docs/usage/) [Source 4](https://noscribe.de/en/docs/faq/)

1. Download the official installer matching your CPU, GPU and OS.
2. Current 0.8 installers cover Windows and Apple Silicon; follow the separate CUDA instructions only for a supported NVIDIA setup.
3. Open the application, select a recording and configure language/speaker options.
### First project

Begin with a small example and inspect the result before using it in production. [Source 1](https://github.com/kaixxx/noScribe/blob/main/README.md) [Source 2](https://noscribe.de/en/docs/download-installation/) [Source 3](https://noscribe.de/en/docs/usage/) [Source 4](https://noscribe.de/en/docs/faq/)

1. Transcribe a short representative excerpt first.
2. Listen while correcting names, speaker boundaries and overlaps; export HTML, text or WebVTT as appropriate.
### Hardware & software

Source-backed requirements; unreported minimums remain unknown. [Source 1](https://github.com/kaixxx/noScribe/blob/main/README.md) [Source 2](https://noscribe.de/en/docs/download-installation/) [Source 3](https://noscribe.de/en/docs/usage/) [Source 4](https://noscribe.de/en/docs/faq/)

- **Hardware:** CPU processing is available. The documented Windows CUDA route requires RTX 20xx or newer with at least 6 GB VRAM. Universal RAM/storage minimums are not specified in the inspected pages.
- **Software:** CUDA route documents driver >=570.65 and a matching toolkit. Bundled releases avoid a manual Python environment.
- **Platforms:** Apple Silicon 0.8 requires macOS 14+. Windows CPU/CUDA builds are offered. Intel Mac remains on official 0.6; Linux binary remains 0.7, with a source route also available.

### License, model weights & costs

The complete top-level GPL-3.0 software license was reviewed and archived. Dependent models and components retain their own terms. [Source 1](https://github.com/kaixxx/noScribe/blob/main/LICENSE.txt) [Source 2](https://github.com/kaixxx/noScribe/blob/main/README.md) [Source 3](https://noscribe.de/en/docs/download-installation/) [Source 4](https://noscribe.de/en/docs/usage/) [Source 5](https://noscribe.de/en/docs/faq/)

- **Code:** GPL-3.0
- **Weights:** GPL-3.0 software; bundled recognition and speaker-model components retain their own terms. The FAQ separately discusses commercial transcript use.
- **Commercial:** The reviewed software license permits commercial software use subject to its obligations; it does not clear independent weights, data, assets, services or dependencies.
- **Cost:** Source code is available under the stated license. Compute, storage, optional hardware and any hosted model/API services can add costs; no current service-price quote is asserted.

### Why it merits attention

Included for its concrete documented creative workflow: Preparing oral histories, artist interviews, documentary transcripts and searchable research recordings. The documentation and developer examples support relevance; output quality, setup success and performance were not independently tested. [Source 1](https://github.com/kaixxx/noScribe/blob/main/README.md) [Source 2](https://noscribe.de/en/docs/download-installation/) [Source 3](https://noscribe.de/en/docs/usage/) [Source 4](https://noscribe.de/en/docs/faq/)

### Limitations

Do not infer that all platforms have the same current version. Overlapping speech, names and difficult audio require listening and correction; accuracy was not tested. [Source 1](https://github.com/kaixxx/noScribe/blob/main/README.md) [Source 2](https://noscribe.de/en/docs/download-installation/) [Source 3](https://noscribe.de/en/docs/usage/) [Source 4](https://noscribe.de/en/docs/faq/)

### Get the tool

- [Repository](https://github.com/kaixxx/noScribe)
- [Documentation](https://noscribe.de/en/docs/download-installation/)
- [License](https://github.com/kaixxx/noScribe/blob/main/LICENSE.txt)

## Godot RL Agents

Games & production pipelines · Interactive, immersive & live media · Creative learning & authoring

Completed the detailed guide for an earlier screened discovery. Documentation and complete software license checked on 2026-10-07; no claim of a new release today.

### How it uses AI

Learning algorithms optimize an agent from observations, actions and rewards supplied by the game. [Source](https://github.com/edbeeching/godot_rl_agents/blob/main/README.md)

### Introduction

A bridge between Godot games and Python reinforcement-learning algorithms. [Source 1](https://github.com/edbeeching/godot_rl_agents/blob/main/README.md)

### What it is good for

Training game characters, experimenting with emergent behavior and testing interactive environments. [Source 1](https://github.com/edbeeching/godot_rl_agents/blob/main/README.md)

### Demo & examples

Official examples and a linked video tutorial demonstrate the JumperHard environment and training. [Source 1](https://github.com/edbeeching/godot_rl_agents/blob/main/README.md)

### Install

Documented setup guidance; these commands were not executed during this review. [Source 1](https://github.com/edbeeching/godot_rl_agents/blob/main/README.md)

1. Create a Python virtual environment and install godot-rl.
2. Clone/download the documented examples.
3. Install Godot 4 .NET and import the JumperHard project for editor-based training.

```sh
pip install godot-rl
```


```sh
python examples/stable_baselines3_example.py
```

### First project

Begin with a small example and inspect the result before using it in production. [Source 1](https://github.com/edbeeching/godot_rl_agents/blob/main/README.md)

1. Run the example and inspect how observation, action and reward signals are defined.
2. Change one behavior objective, retrain and evaluate the resulting agent in the game.
### Hardware & software

Source-backed requirements; unreported minimums remain unknown. [Source 1](https://github.com/edbeeching/godot_rl_agents/blob/main/README.md)

- **Hardware:** No universal CPU/GPU, RAM, VRAM or storage minimum is documented; training cost depends on environment and algorithm.
- **Software:** Godot 4 .NET, Python environment and a supported learning backend such as Stable Baselines3.
- **Platforms:** Windows, Linux and macOS workflows are described. Distributed example binaries cover Windows/Linux; macOS can use the editor route.

### License, model weights & costs

The complete top-level MIT software license was reviewed and archived. Dependent models and components retain their own terms. [Source 1](https://github.com/edbeeching/godot_rl_agents/blob/main/LICENSE) [Source 2](https://github.com/edbeeching/godot_rl_agents/blob/main/README.md)

- **Code:** MIT
- **Weights:** MIT software; bundled example assets may use separate terms such as CC-BY, and learned models/data need project-specific review.
- **Commercial:** The reviewed software license permits commercial software use subject to its obligations; it does not clear independent weights, data, assets, services or dependencies.
- **Cost:** Source code is available under the stated license. Compute, storage, optional hardware and any hosted model/API services can add costs; no current service-price quote is asserted.

### Why it merits attention

Included for its concrete documented creative workflow: Training game characters, experimenting with emergent behavior and testing interactive environments. The documentation and developer examples support relevance; output quality, setup success and performance were not independently tested. [Source 1](https://github.com/edbeeching/godot_rl_agents/blob/main/README.md)

### Limitations

This learns behavior rather than generating dialogue or game art. Reward design and generalization need experimentation; export paths have additional limitations. [Source 1](https://github.com/edbeeching/godot_rl_agents/blob/main/README.md)

### Get the tool

- [Repository](https://github.com/edbeeching/godot_rl_agents)
- [Documentation](https://github.com/edbeeching/godot_rl_agents/blob/main/README.md)
- [License](https://github.com/edbeeching/godot_rl_agents/blob/main/LICENSE)

## Pallaidium

Video, animation & film · Images & design · Audio, music & voice · VFX, compositing & relighting

Completed the detailed guide for an earlier screened discovery. Documentation and complete software license checked on 2026-10-07; no claim of a new release today.

### How it uses AI

Model-specific diffusion and audio-generation pipelines turn prompts and selected strips into new media. [Source](https://github.com/tin2tin/Pallaidium/blob/main/README.md)

### Introduction

A Blender Video Sequence Editor add-on connecting generative media models directly to a timeline. [Source 1](https://github.com/tin2tin/Pallaidium/blob/main/README.md)

### What it is good for

Creating image, video, speech or music elements in the context of an edit. [Source 1](https://github.com/tin2tin/Pallaidium/blob/main/README.md)

### Demo & examples

The README includes timeline screenshots and examples of generated strips. [Source 1](https://github.com/tin2tin/Pallaidium/blob/main/README.md)

### Install

Documented setup guidance; these commands were not executed during this review. [Source 1](https://github.com/tin2tin/Pallaidium/blob/main/README.md)

1. Install the documented Blender version and Git, then install the add-on ZIP.
2. Use the add-on preferences to install dependencies and restart Blender.
3. Choose a supported model in the Sequencer sidebar and review its download/license requirements.
### First project

Begin with a small example and inspect the result before using it in production. [Source 1](https://github.com/tin2tin/Pallaidium/blob/main/README.md)

1. Start with one short strip or a still and a simple prompt.
2. Generate, inspect the result in the timeline and preserve source media before iterating.
### Hardware & software

Source-backed requirements; unreported minimums remain unknown. [Source 1](https://github.com/tin2tin/Pallaidium/blob/main/README.md)

- **Hardware:** Documentation describes NVIDIA GPUs with 6–16 GB VRAM depending on model, not a universal 6 GB minimum. It lists 20+ GB disk space and initial model downloads of roughly 5–30 GB. RAM minimum is not documented.
- **Software:** README specifies Blender 5.2+, Git and CUDA 12.8 for the documented NVIDIA route; dependencies/models are installed through the add-on.
- **Platforms:** Windows is the primary documented route; Linux support is limited. Native macOS inference is not established.

### License, model weights & costs

The complete top-level GPL-3.0 software license was reviewed and archived. Dependent models and components retain their own terms. [Source 1](https://github.com/tin2tin/Pallaidium/blob/main/LICENSE.txt) [Source 2](https://github.com/tin2tin/Pallaidium/blob/main/README.md)

- **Code:** GPL-3.0
- **Weights:** GPL-3.0 add-on code. Every generation model and optional remote API retains its own license and possible charges.
- **Commercial:** The reviewed software license permits commercial software use subject to its obligations; it does not clear independent weights, data, assets, services or dependencies.
- **Cost:** Source code is available under the stated license. Compute, storage, optional hardware and any hosted model/API services can add costs; no current service-price quote is asserted.

### Why it merits attention

Included for its concrete documented creative workflow: Creating image, video, speech or music elements in the context of an edit. The documentation and developer examples support relevance; output quality, setup success and performance were not independently tested. [Source 1](https://github.com/tin2tin/Pallaidium/blob/main/README.md)

### Limitations

Version requirements are unusually specific and can change with model dependencies. Model availability, quality and memory were not tested; timeline integration does not make all model weights unrestricted. [Source 1](https://github.com/tin2tin/Pallaidium/blob/main/README.md)

### Get the tool

- [Repository](https://github.com/tin2tin/Pallaidium)
- [Documentation](https://github.com/tin2tin/Pallaidium/blob/main/README.md)
- [License](https://github.com/tin2tin/Pallaidium/blob/main/LICENSE.txt)

## ComfyUI BlenderAI Node

3D, reconstruction & assets · Images & design · VFX, compositing & relighting · Interactive, immersive & live media

Completed the detailed guide for an earlier screened discovery. Documentation and complete software license checked on 2026-10-07; no claim of a new release today.

### How it uses AI

Routes Blender inputs through actual ComfyUI generative/conditioning models and returns their outputs. [Source](https://github.com/AIGODLIKE/ComfyUI-BlenderAI-node/blob/main/README.md)

### Introduction

A Blender add-on exposing ComfyUI workflows through Blender nodes and image/render inputs. [Source 1](https://github.com/AIGODLIKE/ComfyUI-BlenderAI-node/blob/main/README.md)

### What it is good for

AI-assisted material experiments, render restyling and controlled image generation within a 3D workflow. [Source 1](https://github.com/AIGODLIKE/ComfyUI-BlenderAI-node/blob/main/README.md)

### Demo & examples

The README provides node/interface examples and workflow demonstrations. [Source 1](https://github.com/AIGODLIKE/ComfyUI-BlenderAI-node/blob/main/README.md)

### Install

Documented setup guidance; these commands were not executed during this review. [Source 1](https://github.com/AIGODLIKE/ComfyUI-BlenderAI-node/blob/main/README.md)

1. Prepare a working ComfyUI installation with the needed models.
2. Install the project ZIP as a Blender add-on, using its documented add-on route rather than assuming extension compatibility.
3. Set the ComfyUI/Python paths, connect the backend and import a supported graph.
### First project

Begin with a small example and inspect the result before using it in production. [Source 1](https://github.com/AIGODLIKE/ComfyUI-BlenderAI-node/blob/main/README.md)

1. Feed one render or viewport image into a simple generation workflow.
2. Review the returned image before applying it to materials or a larger scene.
### Hardware & software

Source-backed requirements; unreported minimums remain unknown. [Source 1](https://github.com/AIGODLIKE/ComfyUI-BlenderAI-node/blob/main/README.md)

- **Hardware:** No numeric RAM, VRAM or storage minimum is documented; requirements follow the selected ComfyUI backend and models.
- **Software:** README recommends Blender 3.5/3.6/4.0 and Windows 10/11. Particular workflows also require EasyBakeNode or ControlNet auxiliary nodes.
- **Platforms:** Windows is the primary route. Manual Linux setup is discussed; macOS support is not established by the inspected documentation.

### License, model weights & costs

The complete top-level GPL-3.0 software license was reviewed and archived. Dependent models and components retain their own terms. [Source 1](https://github.com/AIGODLIKE/ComfyUI-BlenderAI-node/blob/main/LICENSE) [Source 2](https://github.com/AIGODLIKE/ComfyUI-BlenderAI-node/blob/main/README.md)

- **Code:** GPL-3.0
- **Weights:** GPL-3.0 add-on; ComfyUI nodes, model weights and companion add-ons have separate terms.
- **Commercial:** The reviewed software license permits commercial software use subject to its obligations; it does not clear independent weights, data, assets, services or dependencies.
- **Cost:** Source code is available under the stated license. Compute, storage, optional hardware and any hosted model/API services can add costs; no current service-price quote is asserted.

### Why it merits attention

Included for its concrete documented creative workflow: AI-assisted material experiments, render restyling and controlled image generation within a 3D workflow. The documentation and developer examples support relevance; output quality, setup success and performance were not independently tested. [Source 1](https://github.com/AIGODLIKE/ComfyUI-BlenderAI-node/blob/main/README.md)

### Limitations

Not every ComfyUI graph/node is compatible. Installation and host-version compatibility were reviewed only in documentation. [Source 1](https://github.com/AIGODLIKE/ComfyUI-BlenderAI-node/blob/main/README.md)

### Get the tool

- [Repository](https://github.com/AIGODLIKE/ComfyUI-BlenderAI-node)
- [Documentation](https://github.com/AIGODLIKE/ComfyUI-BlenderAI-node/blob/main/README.md)
- [License](https://github.com/AIGODLIKE/ComfyUI-BlenderAI-node/blob/main/LICENSE)

## AudioMuse-AI

Audio, music & voice · Performance, projection & stage media · Creative publishing & presentation

Completed the detailed guide for an earlier screened discovery. Documentation and complete software license checked on 2026-10-07; no claim of a new release today.

### How it uses AI

MusicNN, CLAP-family embeddings and related models analyze audio similarity, with optional speech/text features. [Source](https://github.com/NeptuneHub/AudioMuse-AI/blob/main/README.md) [Source](https://github.com/NeptuneHub/AudioMuse-AI/blob/main/docs/GPU.md) [Source](https://github.com/NeptuneHub/AudioMuse-AI/blob/main/docs/ALGORITHM.md)

### Introduction

A self-hosted music-analysis and playlist system that attaches neural sonic information to an existing library. [Source 1](https://github.com/NeptuneHub/AudioMuse-AI/blob/main/README.md) [Source 2](https://github.com/NeptuneHub/AudioMuse-AI/blob/main/docs/GPU.md) [Source 3](https://github.com/NeptuneHub/AudioMuse-AI/blob/main/docs/ALGORITHM.md)

### What it is good for

Finding similar tracks, exploring musical mood and building playlists from a personal media collection. [Source 1](https://github.com/NeptuneHub/AudioMuse-AI/blob/main/README.md) [Source 2](https://github.com/NeptuneHub/AudioMuse-AI/blob/main/docs/GPU.md) [Source 3](https://github.com/NeptuneHub/AudioMuse-AI/blob/main/docs/ALGORITHM.md)

### Demo & examples

The README and algorithm documentation illustrate analysis and playlist workflows. [Source 1](https://github.com/NeptuneHub/AudioMuse-AI/blob/main/README.md)

### Install

Documented setup guidance; these commands were not executed during this review. [Source 1](https://github.com/NeptuneHub/AudioMuse-AI/blob/main/README.md) [Source 2](https://github.com/NeptuneHub/AudioMuse-AI/blob/main/docs/GPU.md) [Source 3](https://github.com/NeptuneHub/AudioMuse-AI/blob/main/docs/ALGORITHM.md)

1. Choose a native application or the documented container deployment.
2. Open the setup wizard at localhost:8000 and connect a supported library server.
3. Analyze a small collection before enabling larger jobs or optional GPU workers.
### First project

Begin with a small example and inspect the result before using it in production. [Source 1](https://github.com/NeptuneHub/AudioMuse-AI/blob/main/README.md) [Source 2](https://github.com/NeptuneHub/AudioMuse-AI/blob/main/docs/GPU.md) [Source 3](https://github.com/NeptuneHub/AudioMuse-AI/blob/main/docs/ALGORITHM.md)

1. Select reference tracks and inspect similarity results.
2. Refine playlist criteria and check the output against the actual recordings.
### Hardware & software

Source-backed requirements; unreported minimums remain unknown. [Source 1](https://github.com/NeptuneHub/AudioMuse-AI/blob/main/README.md) [Source 2](https://github.com/NeptuneHub/AudioMuse-AI/blob/main/docs/GPU.md) [Source 3](https://github.com/NeptuneHub/AudioMuse-AI/blob/main/docs/ALGORITHM.md)

- **Hardware:** Documented baseline: four CPU cores with AVX2 on Intel or ARM, 8 GB RAM and an NVMe SSD; capacity is not specified. Optional NVIDIA GPU guidance recommends 8 GB VRAM.
- **Software:** GPU containers document CUDA 13, driver >=580 and NVIDIA Container Toolkit. Supported library integrations include Navidrome, Jellyfin, LMS/Lyrion, Emby and Plex.
- **Platforms:** Native Windows 10/11 x64, Apple Silicon macOS (tested on 15.3.1) and Linux deb/rpm options; containers cover amd64/arm64. Check release-specific compatibility.

### License, model weights & costs

The complete top-level AGPL-3.0 software license was reviewed and archived. Dependent models and components retain their own terms. [Source 1](https://github.com/NeptuneHub/AudioMuse-AI/blob/main/LICENSE) [Source 2](https://github.com/NeptuneHub/AudioMuse-AI/blob/main/README.md) [Source 3](https://github.com/NeptuneHub/AudioMuse-AI/blob/main/docs/GPU.md) [Source 4](https://github.com/NeptuneHub/AudioMuse-AI/blob/main/docs/ALGORITHM.md)

- **Code:** AGPL-3.0
- **Weights:** AGPL-3.0 application. The full license notice separately lists MusicNN ISC, CLAP components, neural fingerprints, Whisper/Silero and tokenizer/model terms; one blanket model license does not cover the stack.
- **Commercial:** The reviewed software license permits commercial software use subject to its obligations; it does not clear independent weights, data, assets, services or dependencies. AGPL obligations can apply when modified software is made available over a network.
- **Cost:** Source code is available under the stated license. Compute, storage, optional hardware and any hosted model/API services can add costs; no current service-price quote is asserted.

### Why it merits attention

Included for its concrete documented creative workflow: Finding similar tracks, exploring musical mood and building playlists from a personal media collection. The documentation and developer examples support relevance; output quality, setup success and performance were not independently tested. [Source 1](https://github.com/NeptuneHub/AudioMuse-AI/blob/main/README.md) [Source 2](https://github.com/NeptuneHub/AudioMuse-AI/blob/main/docs/GPU.md) [Source 3](https://github.com/NeptuneHub/AudioMuse-AI/blob/main/docs/ALGORITHM.md)

### Limitations

Similarity is model-dependent and may miss artistic intent. Optional server products may have paid features. The documented GPU setup is not a CPU requirement. [Source 1](https://github.com/NeptuneHub/AudioMuse-AI/blob/main/README.md) [Source 2](https://github.com/NeptuneHub/AudioMuse-AI/blob/main/docs/GPU.md) [Source 3](https://github.com/NeptuneHub/AudioMuse-AI/blob/main/docs/ALGORITHM.md)

### Get the tool

- [Repository](https://github.com/NeptuneHub/AudioMuse-AI)
- [Documentation](https://github.com/NeptuneHub/AudioMuse-AI/blob/main/README.md)
- [License](https://github.com/NeptuneHub/AudioMuse-AI/blob/main/LICENSE)

## HomeGallery

Photography, restoration & color · Video, animation & film · Archives, media restoration & collections

Completed the detailed guide for an earlier screened discovery. Documentation and complete software license checked on 2026-10-07; no claim of a new release today.

### How it uses AI

Neural recognition and image similarity enrich search beyond filenames and conventional metadata. [Source](https://github.com/xemle/home-gallery/blob/master/README.md) [Source](https://demo.home-gallery.org)

### Introduction

A self-hosted photo/video gallery with machine-assisted similarity, object and face search. [Source 1](https://github.com/xemle/home-gallery/blob/master/README.md) [Source 2](https://demo.home-gallery.org)

### What it is good for

Rediscovering visual material in a personal archive and browsing related images across a large collection. [Source 1](https://github.com/xemle/home-gallery/blob/master/README.md) [Source 2](https://demo.home-gallery.org)

### Demo & examples

An official public demo shows the gallery interface and search experience. [Source 1](https://demo.home-gallery.org)

### Install

Documented setup guidance; these commands were not executed during this review. [Source 1](https://github.com/xemle/home-gallery/blob/master/README.md) [Source 2](https://demo.home-gallery.org)

1. Download a documented OS binary, or build with Node.js.
2. Initialize a source directory and start the server.
3. Before processing private media, review the API configuration: previews go to the public API by default; a local API server is available.

```sh
./gallery init --source ~/Pictures
```


```sh
./gallery run server
```

### First project

Begin with a small example and inspect the result before using it in production. [Source 1](https://github.com/xemle/home-gallery/blob/master/README.md) [Source 2](https://demo.home-gallery.org)

1. Index a small folder and check how similar-image and face results behave.
2. Configure local inference if desired and then expand indexing to the collection.
### Hardware & software

Source-backed requirements; unreported minimums remain unknown. [Source 1](https://github.com/xemle/home-gallery/blob/master/README.md) [Source 2](https://demo.home-gallery.org)

- **Hardware:** Numeric RAM, VRAM and disk minimums are not documented. Low-powered devices, including Raspberry Pi, can use the remote API route.
- **Software:** Prebuilt binaries or Node.js 20 LTS/18 old LTS as named in the README; customized Linux builds may require Perl and build tools.
- **Platforms:** Windows, macOS and Linux are documented, with additional Raspberry Pi support. Specific binary architectures should be checked before download.

### License, model weights & costs

The complete top-level MIT software license was reviewed and archived. Dependent models and components retain their own terms. [Source 1](https://github.com/xemle/home-gallery/blob/master/LICENSE) [Source 2](https://github.com/xemle/home-gallery/blob/master/README.md) [Source 3](https://demo.home-gallery.org)

- **Code:** MIT
- **Weights:** MIT code; API implementations, model weights and map services have separate terms.
- **Commercial:** The reviewed software license permits commercial software use subject to its obligations; it does not clear independent weights, data, assets, services or dependencies.
- **Cost:** Source code is available under the stated license. Compute, storage, optional hardware and any hosted model/API services can add costs; no current service-price quote is asserted.

### Why it merits attention

Included for its concrete documented creative workflow: Rediscovering visual material in a personal archive and browsing related images across a large collection. The documentation and developer examples support relevance; output quality, setup success and performance were not independently tested. [Source 1](https://github.com/xemle/home-gallery/blob/master/README.md) [Source 2](https://demo.home-gallery.org)

### Limitations

Default image previews are transmitted to api.home-gallery.org; reverse geocoding sends coordinates to Nominatim. Self-hosting the gallery alone does not make all processing local. [Source 1](https://github.com/xemle/home-gallery/blob/master/README.md) [Source 2](https://demo.home-gallery.org)

### Get the tool

- [Repository](https://github.com/xemle/home-gallery)
- [Documentation](https://demo.home-gallery.org)
- [License](https://github.com/xemle/home-gallery/blob/master/LICENSE)

## Infinite Image Browsing

Images & design · Photography, restoration & color · Creative publishing & presentation

Completed the detailed guide for an earlier screened discovery. Documentation and complete software license checked on 2026-10-07; no claim of a new release today.

### How it uses AI

Optional embeddings and language-model topic generation add semantic search/clustering to conventional image metadata browsing. [Source](https://github.com/zanllp/infinite-image-browsing/blob/main/README.md)

### Introduction

An image-browser and metadata tool for AI-generated collections, with optional semantic search and AI categorization. [Source 1](https://github.com/zanllp/infinite-image-browsing/blob/main/README.md)

### What it is good for

Finding images by prompt history or meaning and organizing large generation archives. [Source 1](https://github.com/zanllp/infinite-image-browsing/blob/main/README.md)

### Demo & examples

The README illustrates gallery, metadata and natural-language categorization views. [Source 1](https://github.com/zanllp/infinite-image-browsing/blob/main/README.md)

### Install

Documented setup guidance; these commands were not executed during this review. [Source 1](https://github.com/zanllp/infinite-image-browsing/blob/main/README.md)

1. Choose a standalone desktop release, a Stable Diffusion WebUI extension or the documented Python route.
2. Index a small image directory first.
3. Enable semantic features only after configuring the documented OpenAI-compatible endpoint and dependencies.
### First project

Begin with a small example and inspect the result before using it in production. [Source 1](https://github.com/zanllp/infinite-image-browsing/blob/main/README.md)

1. Search generation metadata to find a known image.
2. Try semantic grouping, review the proposed categories and confirm before moving any files.
### Hardware & software

Source-backed requirements; unreported minimums remain unknown. [Source 1](https://github.com/zanllp/infinite-image-browsing/blob/main/README.md)

- **Hardware:** Minimum RAM, VRAM and storage are not documented. Semantic-index size grows with the collection; remote inference does not imply a local GPU requirement.
- **Software:** Semantic categorization documents numpy, hnswlib and an OpenAI-compatible endpoint/key. Python/host requirements depend on the selected distribution.
- **Platforms:** Standalone and extension routes are documented, including Windows builds. The inspected README does not establish a complete native OS support matrix.

### License, model weights & costs

The complete top-level MIT software license was reviewed and archived. Dependent models and components retain their own terms. [Source 1](https://github.com/zanllp/infinite-image-browsing/blob/main/LICENSE) [Source 2](https://github.com/zanllp/infinite-image-browsing/blob/main/README.md)

- **Code:** MIT
- **Weights:** MIT software; external embedding/chat models and providers have independent licenses and costs.
- **Commercial:** The reviewed software license permits commercial software use subject to its obligations; it does not clear independent weights, data, assets, services or dependencies.
- **Cost:** Source code is available under the stated license. Compute, storage, optional hardware and any hosted model/API services can add costs; no current service-price quote is asserted.

### Why it merits attention

Included for its concrete documented creative workflow: Finding images by prompt history or meaning and organizing large generation archives. The documentation and developer examples support relevance; output quality, setup success and performance were not independently tested. [Source 1](https://github.com/zanllp/infinite-image-browsing/blob/main/README.md)

### Limitations

Natural-language categorization is experimental and ComfyUI metadata coverage is partial. Endpoint configuration determines what data leaves the machine; browser access is not proof of on-device inference. [Source 1](https://github.com/zanllp/infinite-image-browsing/blob/main/README.md)

### Get the tool

- [Repository](https://github.com/zanllp/infinite-image-browsing)
- [Documentation](https://github.com/zanllp/infinite-image-browsing/blob/main/README.md)
- [License](https://github.com/zanllp/infinite-image-browsing/blob/main/LICENSE)

## Flint Chart

Data art & scientific visualization · Creative publishing & presentation · AI agents for code-authored media production

Completed the detailed guide for an earlier screened discovery. Documentation and complete software license checked on 2026-10-07; no claim of a new release today.

### How it uses AI

An external language-model agent authors a compact chart specification through the MCP tools; deterministic compilers render it to Vega-Lite, ECharts, Chart.js, Plotly or Excel-oriented outputs. [Source](https://github.com/microsoft/flint-chart/blob/main/README.md) [Source](https://microsoft.github.io/flint-chart/)

### Introduction

A chart-specification compiler and agent interface producing editable charts across multiple rendering backends. [Source 1](https://github.com/microsoft/flint-chart/blob/main/README.md) [Source 2](https://microsoft.github.io/flint-chart/)

### What it is good for

Drafting data visualizations for publications, presentations and web projects while keeping source data inspectable. [Source 1](https://github.com/microsoft/flint-chart/blob/main/README.md) [Source 2](https://microsoft.github.io/flint-chart/)

### Demo & examples

The official site offers a chart gallery and interactive editor. [Source 1](https://microsoft.github.io/flint-chart/)

### Install

Documented setup guidance; these commands were not executed during this review. [Source 1](https://github.com/microsoft/flint-chart/blob/main/README.md) [Source 2](https://microsoft.github.io/flint-chart/)

1. Install Node.js 18 or newer.
2. Add the library to a project or configure the documented MCP server in an AI client.
3. Choose a rendering backend and supply a small known dataset.

```sh
npm install flint-chart
```


```sh
npx -y flint-chart-mcp
```

### First project

Begin with a small example and inspect the result before using it in production. [Source 1](https://github.com/microsoft/flint-chart/blob/main/README.md) [Source 2](https://microsoft.github.io/flint-chart/)

1. Ask the connected agent for a chart with an explicit metric, grouping and units.
2. Validate values, labels and scales against the data before exporting or embedding.
### Hardware & software

Source-backed requirements; unreported minimums remain unknown. [Source 1](https://github.com/microsoft/flint-chart/blob/main/README.md) [Source 2](https://microsoft.github.io/flint-chart/)

- **Hardware:** No numeric RAM, VRAM or storage minimum is documented; the compiler does not bundle an inference model.
- **Software:** Node.js >=18; renderer dependencies and an external AI client/model for assisted authoring.
- **Platforms:** Node and browser workflows are documented; no separate OS-by-OS certification is claimed.

### License, model weights & costs

The complete top-level MIT software license was reviewed and archived. Dependent models and components retain their own terms. [Source 1](https://github.com/microsoft/flint-chart/blob/main/LICENSE) [Source 2](https://github.com/microsoft/flint-chart/blob/main/README.md) [Source 3](https://microsoft.github.io/flint-chart/)

- **Code:** MIT
- **Weights:** MIT compiler. Model/provider terms, spreadsheet hosts and renderer dependencies remain independent.
- **Commercial:** The reviewed software license permits commercial software use subject to its obligations; it does not clear independent weights, data, assets, services or dependencies.
- **Cost:** Source code is available under the stated license. Compute, storage, optional hardware and any hosted model/API services can add costs; no current service-price quote is asserted.

### Why it merits attention

Included for its concrete documented creative workflow: Drafting data visualizations for publications, presentations and web projects while keeping source data inspectable. The documentation and developer examples support relevance; output quality, setup success and performance were not independently tested. [Source 1](https://github.com/microsoft/flint-chart/blob/main/README.md) [Source 2](https://microsoft.github.io/flint-chart/)

### Limitations

AI authoring depends on an external model. Python work is a source preview rather than an equivalent published package; generated charts require data verification. [Source 1](https://github.com/microsoft/flint-chart/blob/main/README.md) [Source 2](https://microsoft.github.io/flint-chart/)

### Get the tool

- [Repository](https://github.com/microsoft/flint-chart)
- [Documentation](https://microsoft.github.io/flint-chart/)
- [License](https://github.com/microsoft/flint-chart/blob/main/LICENSE)

## Kimodo

Motion capture & character animation · AI choreography and dance composition · Avatars, digital humans & lip sync · Games & production pipelines

Completed the detailed guide for an earlier screened discovery. Documentation and complete software license checked on 2026-10-07; no claim of a new release today.

### How it uses AI

Pretrained motion models synthesize sequences under text and geometric conditioning. [Source](https://github.com/nv-tlabs/kimodo/blob/main/README.md) [Source](https://research.nvidia.com/labs/sil/projects/kimodo/docs/) [Source](https://research.nvidia.com/labs/sil/projects/kimodo/docs/getting_started/installation.html) [Source](https://research.nvidia.com/labs/sil/projects/kimodo/docs/getting_started/quick_start.html) [Source](https://research.nvidia.com/labs/sil/projects/kimodo/docs/user_guide/motion_convert.html)

### Introduction

A kinematic motion-diffusion system for generating and constraining human or robot movement. [Source 1](https://github.com/nv-tlabs/kimodo/blob/main/README.md) [Source 2](https://research.nvidia.com/labs/sil/projects/kimodo/docs/) [Source 3](https://research.nvidia.com/labs/sil/projects/kimodo/docs/getting_started/installation.html) [Source 4](https://research.nvidia.com/labs/sil/projects/kimodo/docs/getting_started/quick_start.html) [Source 5](https://research.nvidia.com/labs/sil/projects/kimodo/docs/user_guide/motion_convert.html)

### What it is good for

Prototyping character motion from text, paths, keyframes and hand/foot constraints. [Source 1](https://github.com/nv-tlabs/kimodo/blob/main/README.md) [Source 2](https://research.nvidia.com/labs/sil/projects/kimodo/docs/) [Source 3](https://research.nvidia.com/labs/sil/projects/kimodo/docs/getting_started/installation.html) [Source 4](https://research.nvidia.com/labs/sil/projects/kimodo/docs/getting_started/quick_start.html) [Source 5](https://research.nvidia.com/labs/sil/projects/kimodo/docs/user_guide/motion_convert.html)

### Demo & examples

NVIDIA provides an official project showcase and local interactive demo documentation. [Source 1](https://research.nvidia.com/labs/sil/projects/kimodo/docs/)

### Install

Documented setup guidance; these commands were not executed during this review. [Source 1](https://github.com/nv-tlabs/kimodo/blob/main/README.md) [Source 2](https://research.nvidia.com/labs/sil/projects/kimodo/docs/) [Source 3](https://research.nvidia.com/labs/sil/projects/kimodo/docs/getting_started/installation.html) [Source 4](https://research.nvidia.com/labs/sil/projects/kimodo/docs/getting_started/quick_start.html) [Source 5](https://research.nvidia.com/labs/sil/projects/kimodo/docs/user_guide/motion_convert.html)

1. Create the documented Python 3.10 environment and install a matching PyTorch/CUDA build.
2. Obtain authorized access to the required gated Llama model and the chosen Kimodo checkpoint.
3. Install the all-features package and start the demo at localhost:7860.

```sh
pip install "kimodo[all] @ git+https://github.com/nv-tlabs/kimodo.git"
```


```sh
kimodo_demo
```

### First project

Begin with a small example and inspect the result before using it in production. [Source 1](https://github.com/nv-tlabs/kimodo/blob/main/README.md) [Source 2](https://research.nvidia.com/labs/sil/projects/kimodo/docs/) [Source 3](https://research.nvidia.com/labs/sil/projects/kimodo/docs/getting_started/installation.html) [Source 4](https://research.nvidia.com/labs/sil/projects/kimodo/docs/getting_started/quick_start.html) [Source 5](https://research.nvidia.com/labs/sil/projects/kimodo/docs/user_guide/motion_convert.html)

1. Choose a checkpoint such as the documented SOMA route and enter a simple motion prompt.
2. Add one constraint, inspect contacts and timing, then export through the documented motion-conversion tools.
### Hardware & software

Source-backed requirements; unreported minimums remain unknown. [Source 1](https://github.com/nv-tlabs/kimodo/blob/main/README.md) [Source 2](https://research.nvidia.com/labs/sil/projects/kimodo/docs/) [Source 3](https://research.nvidia.com/labs/sil/projects/kimodo/docs/getting_started/installation.html) [Source 4](https://research.nvidia.com/labs/sil/projects/kimodo/docs/getting_started/quick_start.html) [Source 5](https://research.nvidia.com/labs/sil/projects/kimodo/docs/user_guide/motion_convert.html)

- **Hardware:** Documentation estimates about 17 GB VRAM with all components on GPU; CPU text-encoder offload can reduce GPU use below 3 GB in the described configuration. These are configuration examples, not universal guarantees. RAM/disk minima are not specified.
- **Software:** Python 3.10, PyTorch >2.0, compatible CUDA, checkpoint files and Hugging Face access to Meta-Llama-3-8B-Instruct.
- **Platforms:** Linux development/testing is documented on RTX 3090/4090 and A100. Windows Docker is expected; native Windows/macOS support is not verified.

### License, model weights & costs

The complete top-level Apache-2.0 software license was reviewed and archived. Dependent models and components retain their own terms. [Source 1](https://github.com/nv-tlabs/kimodo/blob/main/LICENSE) [Source 2](https://github.com/nv-tlabs/kimodo/blob/main/README.md) [Source 3](https://research.nvidia.com/labs/sil/projects/kimodo/docs/) [Source 4](https://research.nvidia.com/labs/sil/projects/kimodo/docs/getting_started/installation.html) [Source 5](https://research.nvidia.com/labs/sil/projects/kimodo/docs/getting_started/quick_start.html) [Source 6](https://research.nvidia.com/labs/sil/projects/kimodo/docs/user_guide/motion_convert.html)

- **Code:** Apache-2.0
- **Weights:** Apache-2.0 code. SOMA/G1 weights use NVIDIA Open Model terms; SMPL-X variants use NVIDIA research/development terms. Llama and body-model licenses are additional.
- **Commercial:** The reviewed software license permits commercial software use subject to its obligations; it does not clear independent weights, data, assets, services or dependencies.
- **Cost:** Source code is available under the stated license. Compute, storage, optional hardware and any hosted model/API services can add costs; no current service-price quote is asserted.

### Why it merits attention

Included for its concrete documented creative workflow: Prototyping character motion from text, paths, keyframes and hand/foot constraints. The documentation and developer examples support relevance; output quality, setup success and performance were not independently tested. [Source 1](https://github.com/nv-tlabs/kimodo/blob/main/README.md) [Source 2](https://research.nvidia.com/labs/sil/projects/kimodo/docs/) [Source 3](https://research.nvidia.com/labs/sil/projects/kimodo/docs/getting_started/installation.html) [Source 4](https://research.nvidia.com/labs/sil/projects/kimodo/docs/getting_started/quick_start.html) [Source 5](https://research.nvidia.com/labs/sil/projects/kimodo/docs/user_guide/motion_convert.html)

### Limitations

Retargeting, ground contact and motion quality need artist review. The software license does not grant unrestricted use of all checkpoint families. [Source 1](https://github.com/nv-tlabs/kimodo/blob/main/README.md) [Source 2](https://research.nvidia.com/labs/sil/projects/kimodo/docs/) [Source 3](https://research.nvidia.com/labs/sil/projects/kimodo/docs/getting_started/installation.html) [Source 4](https://research.nvidia.com/labs/sil/projects/kimodo/docs/getting_started/quick_start.html) [Source 5](https://research.nvidia.com/labs/sil/projects/kimodo/docs/user_guide/motion_convert.html)

### Get the tool

- [Repository](https://github.com/nv-tlabs/kimodo)
- [Documentation](https://research.nvidia.com/labs/sil/projects/kimodo/docs/)
- [License](https://github.com/nv-tlabs/kimodo/blob/main/LICENSE)

## NeuralSVG

Vector graphics, illustration & textures · Typography, fonts & layout · Computational art & creative coding

Completed the detailed guide for an earlier screened discovery. Documentation and complete software license checked on 2026-10-07; no claim of a new release today.

### How it uses AI

A neural representation is optimized using diffusion-model guidance, then converted into vector elements. [Source](https://github.com/SagiPolaczek/NeuralSVG/blob/main/README.md) [Source](https://sagipolaczek.github.io/NeuralSVG/)

### Introduction

A research method that optimizes an implicit representation into layered, editable SVG artwork from text. [Source 1](https://github.com/SagiPolaczek/NeuralSVG/blob/main/README.md) [Source 2](https://sagipolaczek.github.io/NeuralSVG/)

### What it is good for

Exploring generated vector compositions and color-conditioned design variations. [Source 1](https://github.com/SagiPolaczek/NeuralSVG/blob/main/README.md) [Source 2](https://sagipolaczek.github.io/NeuralSVG/)

### Demo & examples

The official project page presents vector results and variations. [Source 1](https://sagipolaczek.github.io/NeuralSVG/)

### Install

Documented setup guidance; these commands were not executed during this review. [Source 1](https://github.com/SagiPolaczek/NeuralSVG/blob/main/README.md) [Source 2](https://sagipolaczek.github.io/NeuralSVG/)

1. Create the documented Python 3.10 Conda environment.
2. Build/install diffvg, install requirements and download the matching diffusion/LoRA assets.
3. Run the provided sketching configuration with a short prompt.

```sh
python scripts/train.py --config_path config_files/run_sketching.yaml --data.text_prompt="minimal 2d line drawing of a rose. on a white background."
```

### First project

Begin with a small example and inspect the result before using it in production. [Source 1](https://github.com/SagiPolaczek/NeuralSVG/blob/main/README.md) [Source 2](https://sagipolaczek.github.io/NeuralSVG/)

1. Start with one simple subject and the published configuration.
2. Inspect layer structure and curves in a vector editor before adapting colors or composition.
### Hardware & software

Source-backed requirements; unreported minimums remain unknown. [Source 1](https://github.com/SagiPolaczek/NeuralSVG/blob/main/README.md) [Source 2](https://sagipolaczek.github.io/NeuralSVG/)

- **Hardware:** Minimum RAM, VRAM and storage are not documented; optimization requires the PyTorch/diffvg/diffusion environment.
- **Software:** Python 3.10, PyTorch, diffvg and matching pretrained/LoRA files. Building diffvg adds a native-toolchain dependency.
- **Platforms:** The inspected instructions do not provide a complete supported-OS matrix or a validated macOS/Windows route.

### License, model weights & costs

The complete top-level MIT software license was reviewed and archived. Dependent models and components retain their own terms. [Source 1](https://github.com/SagiPolaczek/NeuralSVG/blob/main/LICENSE) [Source 2](https://github.com/SagiPolaczek/NeuralSVG/blob/main/README.md) [Source 3](https://sagipolaczek.github.io/NeuralSVG/)

- **Code:** MIT
- **Weights:** MIT source; Stable Diffusion and LoRA weights retain independent terms.
- **Commercial:** The reviewed software license permits commercial software use subject to its obligations; it does not clear independent weights, data, assets, services or dependencies.
- **Cost:** Source code is available under the stated license. Compute, storage, optional hardware and any hosted model/API services can add costs; no current service-price quote is asserted.

### Why it merits attention

Included for its concrete documented creative workflow: Exploring generated vector compositions and color-conditioned design variations. The documentation and developer examples support relevance; output quality, setup success and performance were not independently tested. [Source 1](https://github.com/SagiPolaczek/NeuralSVG/blob/main/README.md) [Source 2](https://sagipolaczek.github.io/NeuralSVG/)

### Limitations

This performs optimization for a prompt rather than instant generic image vectorization. Some aspect-ratio documentation remains incomplete; results were not tested. [Source 1](https://github.com/SagiPolaczek/NeuralSVG/blob/main/README.md) [Source 2](https://sagipolaczek.github.io/NeuralSVG/)

### Get the tool

- [Repository](https://github.com/SagiPolaczek/NeuralSVG)
- [Documentation](https://sagipolaczek.github.io/NeuralSVG/)
- [License](https://github.com/SagiPolaczek/NeuralSVG/blob/main/LICENSE)

## metal-gauss

3D, reconstruction & assets · Photogrammetry, scanning & neural rendering · Spatial audio & volumetric media

Completed the detailed guide for an earlier screened discovery. Documentation and complete software license checked on 2026-10-07; no claim of a new release today.

### How it uses AI

Optimizes Gaussian scene representations from calibrated imagery and renders novel viewpoints. [Source](https://github.com/nandometzger/metal-gauss/blob/main/README.md)

### Introduction

A Gaussian-splat training and rendering toolkit using Apple Silicon Metal and PyTorch MPS. [Source 1](https://github.com/nandometzger/metal-gauss/blob/main/README.md)

### What it is good for

Building and inspecting neural scene assets on a Mac, and rendering scene images or orbit videos. [Source 1](https://github.com/nandometzger/metal-gauss/blob/main/README.md)

### Demo & examples

The README presents reconstruction examples, viewer instructions and author benchmarks. [Source 1](https://github.com/nandometzger/metal-gauss/blob/main/README.md)

### Install

Documented setup guidance; these commands were not executed during this review. [Source 1](https://github.com/nandometzger/metal-gauss/blob/main/README.md)

1. Install Python >=3.10, PyTorch >=2.5 and Apple Command Line Tools.
2. Install the viewer extra and obtain a compatible scene or documented training dataset.
3. Add FFmpeg when MP4 export is needed.

```sh
pip install "metal-gauss[viewer]"
```


```sh
metal-gauss-view scene.ply --up +z
```

### First project

Begin with a small example and inspect the result before using it in production. [Source 1](https://github.com/nandometzger/metal-gauss/blob/main/README.md)

1. Open a small PLY scene and inspect its orientation and coverage.
2. Follow the training dataset recipe for your photographs, then inspect geometry before exporting frames/video.
### Hardware & software

Source-backed requirements; unreported minimums remain unknown. [Source 1](https://github.com/nandometzger/metal-gauss/blob/main/README.md)

- **Hardware:** Apple Silicon is required for the documented accelerated route. RAM/storage minimums are not given and depend on scene size; published M5 measurements are author benchmarks, not a minimum.
- **Software:** macOS, Python >=3.10, PyTorch >=2.5, Command Line Tools; FFmpeg for MP4. Full Xcode is not required by the documentation.
- **Platforms:** Apple Silicon macOS. The browser viewer displays a scene rendered by the Mac service; it does not establish browser-only training on other operating systems.

### License, model weights & costs

The complete top-level MIT software license was reviewed and archived. Dependent models and components retain their own terms. [Source 1](https://github.com/nandometzger/metal-gauss/blob/main/LICENSE) [Source 2](https://github.com/nandometzger/metal-gauss/blob/main/README.md)

- **Code:** MIT
- **Weights:** MIT code; input photographs and imported scene/dataset rights remain separate.
- **Commercial:** The reviewed software license permits commercial software use subject to its obligations; it does not clear independent weights, data, assets, services or dependencies.
- **Cost:** Source code is available under the stated license. Compute, storage, optional hardware and any hosted model/API services can add costs; no current service-price quote is asserted.

### Why it merits attention

Included for its concrete documented creative workflow: Building and inspecting neural scene assets on a Mac, and rendering scene images or orbit videos. The documentation and developer examples support relevance; output quality, setup success and performance were not independently tested. [Source 1](https://github.com/nandometzger/metal-gauss/blob/main/README.md)

### Limitations

Sparse capture and large viewpoint changes can reveal artifacts or unsupported surfaces. Numerical speed and quality claims were not independently tested. [Source 1](https://github.com/nandometzger/metal-gauss/blob/main/README.md)

### Get the tool

- [Repository](https://github.com/nandometzger/metal-gauss)
- [Documentation](https://github.com/nandometzger/metal-gauss/blob/main/README.md)
- [License](https://github.com/nandometzger/metal-gauss/blob/main/LICENSE)

## mlx-spatial

3D, reconstruction & assets · Photogrammetry, scanning & neural rendering · Spatial audio & volumetric media

Completed the detailed guide for an earlier screened discovery. Documentation and complete software license checked on 2026-10-07; no claim of a new release today.

### How it uses AI

Implements pretrained spatial-model inference, including documented SAM3D, TRELLIS.2, HY-World Mirror, LiTo and MapAnything routes. [Source](https://github.com/appautomaton/mlx-spatial/blob/main/README.md)

### Introduction

An MLX implementation layer for several spatial and image-to-3D model pipelines on Apple Silicon. [Source 1](https://github.com/appautomaton/mlx-spatial/blob/main/README.md)

### What it is good for

Experimenting locally with learned scene geometry, textured assets and multi-view reconstruction. [Source 1](https://github.com/appautomaton/mlx-spatial/blob/main/README.md)

### Demo & examples

The README supplies model-specific examples and generated-asset illustrations. [Source 1](https://github.com/appautomaton/mlx-spatial/blob/main/README.md)

### Install

Documented setup guidance; these commands were not executed during this review. [Source 1](https://github.com/appautomaton/mlx-spatial/blob/main/README.md)

1. Install the documented Python 3.13/MLX environment on Apple Silicon.
2. Install the package, or clone the source when using repository wrapper scripts.
3. Download the model-specific weights and choose an example matching that model.

```sh
pip install mlx-spatial
```


```sh
uv run python scripts/trellis2/generate_textured.py inputs/trellis2/cup-of-tea.jpg --output-dir outputs/trellis2/cup-of-tea-script
```

### First project

Begin with a small example and inspect the result before using it in production. [Source 1](https://github.com/appautomaton/mlx-spatial/blob/main/README.md)

1. For the wrapper example, work from the source checkout with its sample input.
2. Inspect the generated asset in a 3D editor and compare shape, texture and unseen regions with the input.
### Hardware & software

Source-backed requirements; unreported minimums remain unknown. [Source 1](https://github.com/appautomaton/mlx-spatial/blob/main/README.md)

- **Hardware:** Apple Silicon; universal RAM/storage requirements are not documented. Weights are downloaded separately and pipeline memory varies substantially.
- **Software:** Python 3.13, MLX and the selected model assets. The wheel does not include every source wrapper or checkpoint.
- **Platforms:** Apple Silicon macOS is documented; native Windows/Linux support is not established.

### License, model weights & costs

The complete top-level MIT software license was reviewed and archived. Dependent models and components retain their own terms. [Source 1](https://github.com/appautomaton/mlx-spatial/blob/main/LICENSE) [Source 2](https://github.com/appautomaton/mlx-spatial/blob/main/README.md)

- **Code:** MIT
- **Weights:** MIT implementation code; every upstream checkpoint retains its own terms, potentially including gates or non-commercial restrictions.
- **Commercial:** The reviewed software license permits commercial software use subject to its obligations; it does not clear independent weights, data, assets, services or dependencies.
- **Cost:** Source code is available under the stated license. Compute, storage, optional hardware and any hosted model/API services can add costs; no current service-price quote is asserted.

### Why it merits attention

Included for its concrete documented creative workflow: Experimenting locally with learned scene geometry, textured assets and multi-view reconstruction. The documentation and developer examples support relevance; output quality, setup success and performance were not independently tested. [Source 1](https://github.com/appautomaton/mlx-spatial/blob/main/README.md)

### Limitations

Model maturity varies; Pixal3D work is described as in development. A GLB export is not evidence that a mesh is watertight or ready for printing. [Source 1](https://github.com/appautomaton/mlx-spatial/blob/main/README.md)

### Get the tool

- [Repository](https://github.com/appautomaton/mlx-spatial)
- [Documentation](https://github.com/appautomaton/mlx-spatial/blob/main/README.md)
- [License](https://github.com/appautomaton/mlx-spatial/blob/main/LICENSE)

## OpenWispr for Android

Mobile, edge & on-device creation · Audio, music & voice · Accessible media & assistive creation

Completed the detailed guide for an earlier screened discovery. Documentation and complete software license checked on 2026-10-07; no claim of a new release today.

### How it uses AI

Local sherpa-onnx speech models or optional Groq Whisper convert speech to text; an optional language model rewrites the result. [Source](https://github.com/EdiBianco/OpenWhispr/blob/main/README.md) [Source](https://github.com/EdiBianco/OpenWhispr/blob/main/app/build.gradle.kts)

### Introduction

An Android voice-input application combining local speech recognition with optional cloud transcription and cleanup. [Source 1](https://github.com/EdiBianco/OpenWhispr/blob/main/README.md) [Source 2](https://github.com/EdiBianco/OpenWhispr/blob/main/app/build.gradle.kts)

### What it is good for

Dictating artist notes, rough captions and text directly into other mobile apps. [Source 1](https://github.com/EdiBianco/OpenWhispr/blob/main/README.md) [Source 2](https://github.com/EdiBianco/OpenWhispr/blob/main/app/build.gradle.kts)

### Demo & examples

The README illustrates the floating microphone and Android workflow. [Source 1](https://github.com/EdiBianco/OpenWhispr/blob/main/README.md)

### Install

Documented setup guidance; these commands were not executed during this review. [Source 1](https://github.com/EdiBianco/OpenWhispr/blob/main/README.md) [Source 2](https://github.com/EdiBianco/OpenWhispr/blob/main/app/build.gradle.kts)

1. Download the official Android release or build the source using its Android toolchain.
2. Grant the documented microphone/accessibility/overlay permissions and download a local model.
3. Keep cloud transcription or cleanup disabled unless the selected provider and data handling suit the workflow.
### First project

Begin with a small example and inspect the result before using it in production. [Source 1](https://github.com/EdiBianco/OpenWhispr/blob/main/README.md) [Source 2](https://github.com/EdiBianco/OpenWhispr/blob/main/app/build.gradle.kts)

1. Test a short dictation in a notes app.
2. Compare the text with the recording and correct names before using it as a caption or script.
### Hardware & software

Source-backed requirements; unreported minimums remain unknown. [Source 1](https://github.com/EdiBianco/OpenWhispr/blob/main/README.md) [Source 2](https://github.com/EdiBianco/OpenWhispr/blob/main/app/build.gradle.kts)

- **Hardware:** Model downloads and runtime need available storage/memory, but numeric minima are not documented.
- **Software:** The build declares Android minSdk 30 (Android 11). Source builds use JDK 17 and the Android SDK; optional cloud functions need provider credentials.
- **Platforms:** Android; this is a phone application, not a macOS/Windows desktop build. Release packaging includes debug builds.

### License, model weights & costs

The complete top-level Apache-2.0 software license was reviewed and archived. Dependent models and components retain their own terms. [Source 1](https://github.com/EdiBianco/OpenWhispr/blob/main/LICENSE) [Source 2](https://github.com/EdiBianco/OpenWhispr/blob/main/README.md) [Source 3](https://github.com/EdiBianco/OpenWhispr/blob/main/app/build.gradle.kts)

- **Code:** Apache-2.0
- **Weights:** Apache-2.0 application; recognition models and optional Groq/LLM services retain independent terms.
- **Commercial:** The reviewed software license permits commercial software use subject to its obligations; it does not clear independent weights, data, assets, services or dependencies.
- **Cost:** Source code is available under the stated license. Compute, storage, optional hardware and any hosted model/API services can add costs; no current service-price quote is asserted.

### Why it merits attention

Included for its concrete documented creative workflow: Dictating artist notes, rough captions and text directly into other mobile apps. The documentation and developer examples support relevance; output quality, setup success and performance were not independently tested. [Source 1](https://github.com/EdiBianco/OpenWhispr/blob/main/README.md) [Source 2](https://github.com/EdiBianco/OpenWhispr/blob/main/app/build.gradle.kts)

### Limitations

Local speech mode and cloud cleanup have different privacy properties. This is the EdiBianco Android project, with its own lineage and packaging; desktop projects sharing similar names are separate. [Source 1](https://github.com/EdiBianco/OpenWhispr/blob/main/README.md) [Source 2](https://github.com/EdiBianco/OpenWhispr/blob/main/app/build.gradle.kts)

### Get the tool

- [Repository](https://github.com/EdiBianco/OpenWhispr)
- [Documentation](https://github.com/EdiBianco/OpenWhispr/blob/main/README.md)
- [License](https://github.com/EdiBianco/OpenWhispr/blob/main/LICENSE)

## html-video

Video, animation & film · AI kinetic typography and animated lettering · AI agents for code-authored media production

Completed the detailed guide for an earlier screened discovery. Documentation and complete software license checked on 2026-10-07; no claim of a new release today.

### How it uses AI

An external coding/model agent turns a brief or source material into animated scene code; a local renderer exports it. [Source](https://github.com/nexu-io/html-video/blob/main/README.md)

### Introduction

A local studio for AI-agent-authored HTML/CSS motion scenes and video rendering. [Source 1](https://github.com/nexu-io/html-video/blob/main/README.md)

### What it is good for

Creating animated explainers, product clips and motion typography with editable web-based scene code. [Source 1](https://github.com/nexu-io/html-video/blob/main/README.md)

### Demo & examples

The README shows templates, studio controls and example animation workflows. [Source 1](https://github.com/nexu-io/html-video/blob/main/README.md)

### Install

Documented setup guidance; these commands were not executed during this review. [Source 1](https://github.com/nexu-io/html-video/blob/main/README.md)

1. Install Node.js 20+, pnpm 9+, FFmpeg and the documented Chromium/Playwright dependencies.
2. Clone the source, install dependencies and build the workspace.
3. Start the studio and configure the external agent or supported model provider.

```sh
pnpm install
```


```sh
pnpm -r build
```


```sh
node packages/cli/dist/bin.js studio
```

### First project

Begin with a small example and inspect the result before using it in production. [Source 1](https://github.com/nexu-io/html-video/blob/main/README.md)

1. Open localhost:3071 and choose one template.
2. Draft a brief clip, edit scene timing/text, inspect frames and render an MP4.
### Hardware & software

Source-backed requirements; unreported minimums remain unknown. [Source 1](https://github.com/nexu-io/html-video/blob/main/README.md)

- **Hardware:** RAM, VRAM and disk minimums are not documented; rendering and any local model have separate requirements.
- **Software:** Node >=20, pnpm >=9, FFmpeg and Chromium/Playwright. AI authoring needs an external agent or configured API.
- **Platforms:** Local browser studio; the inspected documentation does not establish a complete native OS matrix or mobile rendering support.

### License, model weights & costs

The complete top-level Apache-2.0 software license was reviewed and archived. Dependent models and components retain their own terms. [Source 1](https://github.com/nexu-io/html-video/blob/main/LICENSE) [Source 2](https://github.com/nexu-io/html-video/blob/main/README.md)

- **Code:** Apache-2.0
- **Weights:** Apache-2.0 source; external agents, optional MiniMax narration/music, fonts and media assets have separate terms.
- **Commercial:** The reviewed software license permits commercial software use subject to its obligations; it does not clear independent weights, data, assets, services or dependencies.
- **Cost:** Source code is available under the stated license. Compute, storage, optional hardware and any hosted model/API services can add costs; no current service-price quote is asserted.

### Why it merits attention

Included for its concrete documented creative workflow: Creating animated explainers, product clips and motion typography with editable web-based scene code. The documentation and developer examples support relevance; output quality, setup success and performance were not independently tested. [Source 1](https://github.com/nexu-io/html-video/blob/main/README.md)

### Limitations

Hyperframes is the currently shipped renderer. Remotion, Motion Canvas and Manim are planned integrations, not verified current capabilities. Optional APIs may add cost. [Source 1](https://github.com/nexu-io/html-video/blob/main/README.md)

### Get the tool

- [Repository](https://github.com/nexu-io/html-video)
- [Documentation](https://github.com/nexu-io/html-video/blob/main/README.md)
- [License](https://github.com/nexu-io/html-video/blob/main/LICENSE)

## Scriberr

Audio, music & voice · Video, animation & film · Accessible media & assistive creation · Archives, media restoration & collections

Completed the detailed guide for an earlier screened discovery. Documentation and complete software license checked on 2026-10-07; no claim of a new release today.

### How it uses AI

Whisper/NeMo and related neural engines recognize speech; optional Pyannote models identify speaker segments. [Source](https://github.com/rishikanthc/Scriberr/blob/main/README.md)

### Introduction

A self-hosted transcription application with several recognition engines and optional speaker diarization. [Source 1](https://github.com/rishikanthc/Scriberr/blob/main/README.md)

### What it is good for

Turning recordings into editable transcripts for documentary work, interviews and media archives. [Source 1](https://github.com/rishikanthc/Scriberr/blob/main/README.md)

### Demo & examples

The README presents the upload/transcription interface and deployment examples. [Source 1](https://github.com/rishikanthc/Scriberr/blob/main/README.md)

### Install

Documented setup guidance; these commands were not executed during this review. [Source 1](https://github.com/rishikanthc/Scriberr/blob/main/README.md)

1. Use the documented macOS/Linux Homebrew route or a suitable Docker image.
2. Start the application and allow the first model downloads.
3. For containers, retain both application data and the documented model/environment volumes.

```sh
brew tap rishikanthc/scriberr
```


```sh
brew install scriberr
```


```sh
scriberr
```

### First project

Begin with a small example and inspect the result before using it in production. [Source 1](https://github.com/rishikanthc/Scriberr/blob/main/README.md)

1. Upload a short recording and choose a recognition model.
2. Review transcript/speaker boundaries before exporting; enable optional chat only after selecting a provider.
### Hardware & software

Source-backed requirements; unreported minimums remain unknown. [Source 1](https://github.com/rishikanthc/Scriberr/blob/main/README.md)

- **Hardware:** CPU and NVIDIA GPU routes exist; numeric minimum RAM/VRAM/storage are not documented. RTX 50-series Blackwell cards need the dedicated documented image.
- **Software:** Homebrew or Docker; model files download on first use. Diarization and optional chat can introduce separate model-access/API requirements.
- **Platforms:** macOS/Linux native package and CPU/CUDA container routes. The PWA is a client interface, not proof of on-phone inference.

### License, model weights & costs

The complete top-level MIT software license was reviewed and archived. Dependent models and components retain their own terms. [Source 1](https://github.com/rishikanthc/Scriberr/blob/main/LICENSE) [Source 2](https://github.com/rishikanthc/Scriberr/blob/main/README.md)

- **Code:** MIT
- **Weights:** MIT software; Whisper, NeMo, Pyannote checkpoints and optional chat providers have independent conditions.
- **Commercial:** The reviewed software license permits commercial software use subject to its obligations; it does not clear independent weights, data, assets, services or dependencies.
- **Cost:** Source code is available under the stated license. Compute, storage, optional hardware and any hosted model/API services can add costs; no current service-price quote is asserted.

### Why it merits attention

Included for its concrete documented creative workflow: Turning recordings into editable transcripts for documentary work, interviews and media archives. The documentation and developer examples support relevance; output quality, setup success and performance were not independently tested. [Source 1](https://github.com/rishikanthc/Scriberr/blob/main/README.md)

### Limitations

Hardware-specific Docker images are not interchangeable. Speaker labels and recognition need correction; optional cloud chat changes where transcript data is processed. [Source 1](https://github.com/rishikanthc/Scriberr/blob/main/README.md)

### Get the tool

- [Repository](https://github.com/rishikanthc/Scriberr)
- [Documentation](https://github.com/rishikanthc/Scriberr/blob/main/README.md)
- [License](https://github.com/rishikanthc/Scriberr/blob/main/LICENSE)

## Diart

Audio, music & voice · Interactive, immersive & live media · Accessible media & assistive creation

Completed the detailed guide for an earlier screened discovery. Documentation and complete software license checked on 2026-10-07; no claim of a new release today.

### How it uses AI

Neural segmentation and speaker embeddings feed incremental clustering to label who is speaking over time. [Source](https://github.com/juanmc2005/diart/blob/main/README.md)

### Introduction

A Python framework for incremental, real-time speaker diarization from live audio. [Source 1](https://github.com/juanmc2005/diart/blob/main/README.md)

### What it is good for

Adding speaker-aware timing to interactive audio prototypes, recorded discussions or caption pipelines. [Source 1](https://github.com/juanmc2005/diart/blob/main/README.md)

### Demo & examples

The README provides microphone-stream examples and author latency/accuracy measurements. [Source 1](https://github.com/juanmc2005/diart/blob/main/README.md)

### Install

Documented setup guidance; these commands were not executed during this review. [Source 1](https://github.com/juanmc2005/diart/blob/main/README.md)

1. Create a supported Python environment and install the documented audio system libraries.
2. Install diart and accept/access any required Pyannote model terms on Hugging Face.
3. Run the microphone example with an appropriate input device.

```sh
pip install diart
```


```sh
diart.stream microphone
```

### First project

Begin with a small example and inspect the result before using it in production. [Source 1](https://github.com/juanmc2005/diart/blob/main/README.md)

1. Record a short two-speaker exchange and inspect the generated RTTM speaker timings.
2. Tune the streaming parameters before connecting a separate transcription/rendering system.
### Hardware & software

Source-backed requirements; unreported minimums remain unknown. [Source 1](https://github.com/juanmc2005/diart/blob/main/README.md)

- **Hardware:** CPU/GPU benchmark examples are documented, but universal RAM, VRAM and disk minima are not specified.
- **Software:** Python 3.10/3.11/3.12; documentation specifies FFmpeg <4.4, PortAudio 19.6.x and libsndfile >=1.2.2. Some pretrained models require account acceptance/authentication.
- **Platforms:** The inspected documentation does not provide a validated OS-by-OS matrix; audio-device and native-library setup is platform-specific.

### License, model weights & costs

The complete top-level MIT software license was reviewed and archived. Dependent models and components retain their own terms. [Source 1](https://github.com/juanmc2005/diart/blob/main/LICENSE) [Source 2](https://github.com/juanmc2005/diart/blob/main/README.md)

- **Code:** MIT
- **Weights:** MIT software; Pyannote and other pretrained model terms are separate.
- **Commercial:** The reviewed software license permits commercial software use subject to its obligations; it does not clear independent weights, data, assets, services or dependencies.
- **Cost:** Source code is available under the stated license. Compute, storage, optional hardware and any hosted model/API services can add costs; no current service-price quote is asserted.

### Why it merits attention

Included for its concrete documented creative workflow: Adding speaker-aware timing to interactive audio prototypes, recorded discussions or caption pipelines. The documentation and developer examples support relevance; output quality, setup success and performance were not independently tested. [Source 1](https://github.com/juanmc2005/diart/blob/main/README.md)

### Limitations

The project produces diarization, not a complete speech-to-text caption application. Transcription is listed as future work; old dependency constraints need careful environment planning. [Source 1](https://github.com/juanmc2005/diart/blob/main/README.md)

### Get the tool

- [Repository](https://github.com/juanmc2005/diart)
- [Documentation](https://github.com/juanmc2005/diart/blob/main/README.md)
- [License](https://github.com/juanmc2005/diart/blob/main/LICENSE)

## Amphion

Audio, music & voice · Performance, projection & stage media · Creative learning & authoring

Completed the detailed guide for an earlier screened discovery. Documentation and complete software license checked on 2026-10-07; no claim of a new release today.

### How it uses AI

Neural generative models, codecs and diffusion recipes synthesize or transform sound from text and reference audio. [Source](https://github.com/open-mmlab/Amphion/blob/main/README.md) [Source](https://github.com/open-mmlab/Amphion/blob/main/egs/tta/README.md) [Source](https://github.com/open-mmlab/Amphion/blob/main/egs/tta/RECIPE.md) [Source](https://huggingface.co/spaces/amphion/Text-to-Audio)

### Introduction

A research toolkit for speech, singing and general audio generation, with model recipes and visualization tools. [Source 1](https://github.com/open-mmlab/Amphion/blob/main/README.md) [Source 2](https://github.com/open-mmlab/Amphion/blob/main/egs/tta/README.md) [Source 3](https://github.com/open-mmlab/Amphion/blob/main/egs/tta/RECIPE.md) [Source 4](https://huggingface.co/spaces/amphion/Text-to-Audio)

### What it is good for

Studying or adapting text-to-audio, voice conversion and expressive speech pipelines. [Source 1](https://github.com/open-mmlab/Amphion/blob/main/README.md) [Source 2](https://github.com/open-mmlab/Amphion/blob/main/egs/tta/README.md) [Source 3](https://github.com/open-mmlab/Amphion/blob/main/egs/tta/RECIPE.md) [Source 4](https://huggingface.co/spaces/amphion/Text-to-Audio)

### Demo & examples

The text-to-audio recipe links an official demo and pretrained model; other recipes have separate demonstrations. [Source 1](https://huggingface.co/spaces/amphion/Text-to-Audio)

### Install

Documented setup guidance; these commands were not executed during this review. [Source 1](https://github.com/open-mmlab/Amphion/blob/main/README.md) [Source 2](https://github.com/open-mmlab/Amphion/blob/main/egs/tta/README.md) [Source 3](https://github.com/open-mmlab/Amphion/blob/main/egs/tta/RECIPE.md) [Source 4](https://huggingface.co/spaces/amphion/Text-to-Audio)

1. Clone the source and choose a specific recipe rather than installing every model family at once.
2. The general setup documents Conda Python 3.9.15 and env.sh; a CUDA Docker route is also provided.
3. For text-to-audio, obtain the matching pretrained checkpoint and configure its paths as described in the recipe.

```sh
conda create --name amphion python=3.9.15
```


```sh
conda activate amphion
```


```sh
sh env.sh
```


```sh
sh egs/tta/audioldm/run_inference.sh --text "A man is whistling"
```

### First project

Begin with a small example and inspect the result before using it in production. [Source 1](https://github.com/open-mmlab/Amphion/blob/main/README.md) [Source 2](https://github.com/open-mmlab/Amphion/blob/main/egs/tta/README.md) [Source 3](https://github.com/open-mmlab/Amphion/blob/main/egs/tta/RECIPE.md) [Source 4](https://huggingface.co/spaces/amphion/Text-to-Audio)

1. Run one short text-to-audio example from the repository root after configuring the checkpoint.
2. Listen for prompt adherence and artifacts before modifying parameters or considering training.
### Hardware & software

Source-backed requirements; unreported minimums remain unknown. [Source 1](https://github.com/open-mmlab/Amphion/blob/main/README.md) [Source 2](https://github.com/open-mmlab/Amphion/blob/main/egs/tta/README.md) [Source 3](https://github.com/open-mmlab/Amphion/blob/main/egs/tta/RECIPE.md) [Source 4](https://huggingface.co/spaces/amphion/Text-to-Audio)

- **Hardware:** GPU requirements depend on the chosen model. The inspected general and text-to-audio guides do not specify universal RAM/VRAM/storage minimums.
- **Software:** Recipe-specific Python/PyTorch environment; the general installer uses Python 3.9.15. NVIDIA Docker additionally needs driver, CUDA and Container Toolkit.
- **Platforms:** Shell/CUDA-oriented research setup; native macOS/Windows parity is not established by the inspected guides.

### License, model weights & costs

The complete top-level MIT software license was reviewed and archived. Dependent models and components retain their own terms. [Source 1](https://github.com/open-mmlab/Amphion/blob/main/LICENSE) [Source 2](https://github.com/open-mmlab/Amphion/blob/main/README.md) [Source 3](https://github.com/open-mmlab/Amphion/blob/main/egs/tta/README.md) [Source 4](https://github.com/open-mmlab/Amphion/blob/main/egs/tta/RECIPE.md) [Source 5](https://huggingface.co/spaces/amphion/Text-to-Audio)

- **Code:** MIT
- **Weights:** MIT code. Model and dataset terms differ: original Emilia is CC-BY-NC-4.0 while Emilia-YODAS is CC-BY-4.0; these are not interchangeable commercial permissions.
- **Commercial:** The reviewed software license permits commercial software use subject to its obligations; it does not clear independent weights, data, assets, services or dependencies.
- **Cost:** Source code is available under the stated license. Compute, storage, optional hardware and any hosted model/API services can add costs; no current service-price quote is asserted.

### Why it merits attention

Included for its concrete documented creative workflow: Studying or adapting text-to-audio, voice conversion and expressive speech pipelines. The documentation and developer examples support relevance; output quality, setup success and performance were not independently tested. [Source 1](https://github.com/open-mmlab/Amphion/blob/main/README.md) [Source 2](https://github.com/open-mmlab/Amphion/blob/main/egs/tta/README.md) [Source 3](https://github.com/open-mmlab/Amphion/blob/main/egs/tta/RECIPE.md) [Source 4](https://huggingface.co/spaces/amphion/Text-to-Audio)

### Limitations

Recipes have different environments and maturity. Training instructions require separate datasets; a toolkit license does not clear all training material or voice models. [Source 1](https://github.com/open-mmlab/Amphion/blob/main/README.md) [Source 2](https://github.com/open-mmlab/Amphion/blob/main/egs/tta/README.md) [Source 3](https://github.com/open-mmlab/Amphion/blob/main/egs/tta/RECIPE.md) [Source 4](https://huggingface.co/spaces/amphion/Text-to-Audio)

### Get the tool

- [Repository](https://github.com/open-mmlab/Amphion)
- [Documentation](https://huggingface.co/spaces/amphion/Text-to-Audio)
- [License](https://github.com/open-mmlab/Amphion/blob/main/LICENSE)

## dcc-mcp-inkscape

Vector graphics, illustration & textures · Creative publishing & presentation · AI agents for code-authored media production

Completed the detailed guide for an earlier screened discovery. Documentation and complete software license checked on 2026-10-07; no claim of a new release today.

### How it uses AI

An external language-model agent supplies structured drawing plans to a deterministic Inkscape bridge. [Source](https://github.com/dcc-mcp/dcc-mcp-inkscape/blob/main/README.md) [Source](https://github.com/dcc-mcp/dcc-mcp-inkscape/blob/main/install.md)

### Introduction

An agent-control bridge that executes typed vector-document operations in native Inkscape. [Source 1](https://github.com/dcc-mcp/dcc-mcp-inkscape/blob/main/README.md) [Source 2](https://github.com/dcc-mcp/dcc-mcp-inkscape/blob/main/install.md)

### What it is good for

Creating editable SVG layouts, manipulating paths/text/layers and exporting PNG/SVG through an AI client. [Source 1](https://github.com/dcc-mcp/dcc-mcp-inkscape/blob/main/README.md) [Source 2](https://github.com/dcc-mcp/dcc-mcp-inkscape/blob/main/install.md)

### Demo & examples

The repository documents native execution proof and example vector plans; no public live demo was verified. [Source 1](https://github.com/dcc-mcp/dcc-mcp-inkscape/blob/main/README.md)

### Install

Documented setup guidance; these commands were not executed during this review. [Source 1](https://github.com/dcc-mcp/dcc-mcp-inkscape/blob/main/README.md) [Source 2](https://github.com/dcc-mcp/dcc-mcp-inkscape/blob/main/install.md)

1. Prepare Inkscape and the Python controller plus the matching dcc-mcp-core dependency.
2. Use the documented source/wheel installation route; this version is not a published PyPI release.
3. Configure executable, workspace, private profile and MCP gateway paths, run the installation plan and connect an agent.
### First project

Begin with a small example and inspect the result before using it in production. [Source 1](https://github.com/dcc-mcp/dcc-mcp-inkscape/blob/main/README.md) [Source 2](https://github.com/dcc-mcp/dcc-mcp-inkscape/blob/main/install.md)

1. Ask the agent to make one small SVG with editable text and a simple shape.
2. Open it in Inkscape, inspect native objects and export a preview before expanding the plan.
### Hardware & software

Source-backed requirements; unreported minimums remain unknown. [Source 1](https://github.com/dcc-mcp/dcc-mcp-inkscape/blob/main/README.md) [Source 2](https://github.com/dcc-mcp/dcc-mcp-inkscape/blob/main/install.md)

- **Hardware:** RAM, VRAM and storage minima are not documented; no inference model is bundled in the bridge.
- **Software:** Python >=3.7 controller, dcc-mcp-core >=0.20.36,<1 and Inkscape 1.4. The documented native proof uses Windows portable Inkscape 1.4.4.
- **Platforms:** Installation/version-probe support is explicitly Windows-focused. Linux runtime provenance exists, but equivalent Linux/macOS installation preflight is not established.

### License, model weights & costs

The complete top-level MIT software license was reviewed and archived. Dependent models and components retain their own terms. [Source 1](https://github.com/dcc-mcp/dcc-mcp-inkscape/blob/main/LICENSE) [Source 2](https://github.com/dcc-mcp/dcc-mcp-inkscape/blob/main/README.md) [Source 3](https://github.com/dcc-mcp/dcc-mcp-inkscape/blob/main/install.md)

- **Code:** MIT
- **Weights:** MIT bridge; Inkscape, fonts, gateway/client components and any external model retain separate terms.
- **Commercial:** The reviewed software license permits commercial software use subject to its obligations; it does not clear independent weights, data, assets, services or dependencies.
- **Cost:** Source code is available under the stated license. Compute, storage, optional hardware and any hosted model/API services can add costs; no current service-price quote is asserted.

### Why it merits attention

Included for its concrete documented creative workflow: Creating editable SVG layouts, manipulating paths/text/layers and exporting PNG/SVG through an AI client. The documentation and developer examples support relevance; output quality, setup success and performance were not independently tested. [Source 1](https://github.com/dcc-mcp/dcc-mcp-inkscape/blob/main/README.md) [Source 2](https://github.com/dcc-mcp/dcc-mcp-inkscape/blob/main/install.md)

### Limitations

This early source-only release requires integration work. It does not bundle an AI model or fonts, and cannot be assumed to cover every Inkscape operation. [Source 1](https://github.com/dcc-mcp/dcc-mcp-inkscape/blob/main/README.md) [Source 2](https://github.com/dcc-mcp/dcc-mcp-inkscape/blob/main/install.md)

### Get the tool

- [Repository](https://github.com/dcc-mcp/dcc-mcp-inkscape)
- [Documentation](https://github.com/dcc-mcp/dcc-mcp-inkscape/blob/main/README.md)
- [License](https://github.com/dcc-mcp/dcc-mcp-inkscape/blob/main/LICENSE)

## PPT Master

Creative publishing & presentation · Storyboarding, narrative & comics · AI agents for code-authored media production

Completed the detailed guide for an earlier screened discovery. Documentation and complete software license checked on 2026-10-07; no claim of a new release today.

### How it uses AI

A connected language-model agent uses the repository tools and source materials to draft slide content and structure. [Source](https://github.com/hugohe3/ppt-master/blob/main/README.md) [Source](https://github.com/hugohe3/ppt-master/blob/main/docs/getting-started.md) [Source](https://hugohe3.github.io/ppt-master-examples/)

### Introduction

An AI-agent-oriented workflow for building editable PowerPoint presentations from documents, briefs and templates. [Source 1](https://github.com/hugohe3/ppt-master/blob/main/README.md) [Source 2](https://github.com/hugohe3/ppt-master/blob/main/docs/getting-started.md) [Source 3](https://hugohe3.github.io/ppt-master-examples/)

### What it is good for

Turning research or a visual narrative into a slide deck, then reviewing layout and exported results. [Source 1](https://github.com/hugohe3/ppt-master/blob/main/README.md) [Source 2](https://github.com/hugohe3/ppt-master/blob/main/docs/getting-started.md) [Source 3](https://hugohe3.github.io/ppt-master-examples/)

### Demo & examples

The project links a public examples gallery with generated presentations. [Source 1](https://hugohe3.github.io/ppt-master-examples/)

### Install

Documented setup guidance; these commands were not executed during this review. [Source 1](https://github.com/hugohe3/ppt-master/blob/main/README.md) [Source 2](https://github.com/hugohe3/ppt-master/blob/main/docs/getting-started.md) [Source 3](https://hugohe3.github.io/ppt-master-examples/)

1. Install Python 3.10+ and the documented requirements in the source checkout.
2. Open the project with a supported filesystem-capable AI coding agent.
3. Supply source material, audience and template constraints, then follow the getting-started workflow.

```sh
pip install -r requirements.txt
```

### First project

Begin with a small example and inspect the result before using it in production. [Source 1](https://github.com/hugohe3/ppt-master/blob/main/README.md) [Source 2](https://github.com/hugohe3/ppt-master/blob/main/docs/getting-started.md) [Source 3](https://hugohe3.github.io/ppt-master-examples/)

1. Start with a short deck and review its proposed narrative.
2. Inspect every slide, correct layout/text and export the editable PPTX and available previews.
### Hardware & software

Source-backed requirements; unreported minimums remain unknown. [Source 1](https://github.com/hugohe3/ppt-master/blob/main/README.md) [Source 2](https://github.com/hugohe3/ppt-master/blob/main/docs/getting-started.md) [Source 3](https://hugohe3.github.io/ppt-master-examples/)

- **Hardware:** Minimum RAM, VRAM and storage are not documented; local or hosted model requirements are separate.
- **Software:** Python >=3.10 and an external AI agent. Pandoc is needed only for certain older document formats; optional image/narration services need their own setup.
- **Platforms:** Windows, macOS and Linux guidance is provided. PowerPoint can be used for review but is a separate proprietary product.

### License, model weights & costs

The complete top-level MIT software license was reviewed and archived. Dependent models and components retain their own terms. [Source 1](https://github.com/hugohe3/ppt-master/blob/main/LICENSE) [Source 2](https://github.com/hugohe3/ppt-master/blob/main/README.md) [Source 3](https://github.com/hugohe3/ppt-master/blob/main/docs/getting-started.md) [Source 4](https://hugohe3.github.io/ppt-master-examples/)

- **Code:** MIT
- **Weights:** MIT code; agent/model services, input documents, templates, fonts and generated-image providers have separate terms.
- **Commercial:** The reviewed software license permits commercial software use subject to its obligations; it does not clear independent weights, data, assets, services or dependencies.
- **Cost:** Source code is available under the stated license. Compute, storage, optional hardware and any hosted model/API services can add costs; no current service-price quote is asserted.

### Why it merits attention

Included for its concrete documented creative workflow: Turning research or a visual narrative into a slide deck, then reviewing layout and exported results. The documentation and developer examples support relevance; output quality, setup success and performance were not independently tested. [Source 1](https://github.com/hugohe3/ppt-master/blob/main/README.md) [Source 2](https://github.com/hugohe3/ppt-master/blob/main/docs/getting-started.md) [Source 3](https://hugohe3.github.io/ppt-master-examples/)

### Limitations

This is an agent-assisted workflow, not guaranteed one-click publication quality. External model calls may transmit source material; text and visual claims need human review. [Source 1](https://github.com/hugohe3/ppt-master/blob/main/README.md) [Source 2](https://github.com/hugohe3/ppt-master/blob/main/docs/getting-started.md) [Source 3](https://hugohe3.github.io/ppt-master-examples/)

### Get the tool

- [Repository](https://github.com/hugohe3/ppt-master)
- [Documentation](https://hugohe3.github.io/ppt-master-examples/)
- [License](https://github.com/hugohe3/ppt-master/blob/main/LICENSE)

## Stable Diffusion WebUI (AUTOMATIC1111)

Images & design · Photography, restoration & color · VFX, compositing & relighting

Completed the detailed guide for an earlier screened discovery. Documentation and complete software license checked on 2026-10-07; no claim of a new release today.

### How it uses AI

Runs diffusion models and compatible extensions such as conditioning/upscaling components. [Source](https://github.com/AUTOMATIC1111/stable-diffusion-webui/blob/master/README.md)

### Introduction

An established local web interface for Stable Diffusion image generation, editing and extensions. [Source 1](https://github.com/AUTOMATIC1111/stable-diffusion-webui/blob/master/README.md)

### What it is good for

Iterating text-to-image, image-to-image, inpainting and model-specific image workflows with reusable parameters. [Source 1](https://github.com/AUTOMATIC1111/stable-diffusion-webui/blob/master/README.md)

### Demo & examples

The README includes interface examples and links to the official feature and installation wiki. [Source 1](https://github.com/AUTOMATIC1111/stable-diffusion-webui/blob/master/README.md)

### Install

Documented setup guidance; these commands were not executed during this review. [Source 1](https://github.com/AUTOMATIC1111/stable-diffusion-webui/blob/master/README.md)

1. Choose the official installation guide for your OS/GPU.
2. Windows NVIDIA instructions use Python 3.10.6 and Git; clone the repository and obtain an appropriate checkpoint.
3. Launch webui-user.bat on Windows or follow webui.sh/Linux and the separate Apple Silicon guide.

```sh
git clone https://github.com/AUTOMATIC1111/stable-diffusion-webui.git
```

### First project

Begin with a small example and inspect the result before using it in production. [Source 1](https://github.com/AUTOMATIC1111/stable-diffusion-webui/blob/master/README.md)

1. Select a checkpoint, enter a prompt and record the seed/settings.
2. Inspect the image, use a small inpainting region and retain metadata for reproducibility.
### Hardware & software

Source-backed requirements; unreported minimums remain unknown. [Source 1](https://github.com/AUTOMATIC1111/stable-diffusion-webui/blob/master/README.md)

- **Hardware:** The README describes 4 GB VRAM operation and reports of 2 GB configurations; neither guarantees all models/extensions. RAM and free-storage minimums are not universal/documented.
- **Software:** OS/GPU-specific Python/PyTorch setup; Windows reference uses Python 3.10.6. Checkpoint and optional extension downloads add storage/dependencies.
- **Platforms:** Windows and Linux installation routes plus an Apple Silicon wiki are provided. GPU/model compatibility must be checked for each route.

### License, model weights & costs

The complete top-level AGPL-3.0 software license was reviewed and archived. Dependent models and components retain their own terms. [Source 1](https://github.com/AUTOMATIC1111/stable-diffusion-webui/blob/master/LICENSE.txt) [Source 2](https://github.com/AUTOMATIC1111/stable-diffusion-webui/blob/master/README.md)

- **Code:** AGPL-3.0
- **Weights:** AGPL-3.0 application; models, extensions and reused components have distinct licenses.
- **Commercial:** The reviewed software license permits commercial software use subject to its obligations; it does not clear independent weights, data, assets, services or dependencies. AGPL obligations can apply when modified software is made available over a network.
- **Cost:** Source code is available under the stated license. Compute, storage, optional hardware and any hosted model/API services can add costs; no current service-price quote is asserted.

### Why it merits attention

Included for its concrete documented creative workflow: Iterating text-to-image, image-to-image, inpainting and model-specific image workflows with reusable parameters. The documentation and developer examples support relevance; output quality, setup success and performance were not independently tested. [Source 1](https://github.com/AUTOMATIC1111/stable-diffusion-webui/blob/master/README.md)

### Limitations

Established does not mean every new model or GPU is supported. Extensions can change the environment substantially; no installation or output test was performed. [Source 1](https://github.com/AUTOMATIC1111/stable-diffusion-webui/blob/master/README.md)

### Get the tool

- [Repository](https://github.com/AUTOMATIC1111/stable-diffusion-webui)
- [Documentation](https://github.com/AUTOMATIC1111/stable-diffusion-webui/blob/master/README.md)
- [License](https://github.com/AUTOMATIC1111/stable-diffusion-webui/blob/master/LICENSE.txt)

## PersonaLive

Avatars, digital humans & lip sync · Motion capture & character animation · Video, animation & film

Completed the detailed guide for an earlier screened discovery. Documentation and complete software license checked on 2026-10-07; no claim of a new release today.

### How it uses AI

Neural animation transfers motion from a driving sequence or webcam to an appearance-conditioned portrait. [Source](https://github.com/GVCLab/PersonaLive/blob/main/README.md)

### Introduction

A diffusion-based portrait-animation system driven by recorded or live motion input. [Source 1](https://github.com/GVCLab/PersonaLive/blob/main/README.md)

### What it is good for

Exploring animated portrait clips and character-performance prototypes from a reference image. [Source 1](https://github.com/GVCLab/PersonaLive/blob/main/README.md)

### Demo & examples

The README shows developer videos and offline/online workflow examples. [Source 1](https://github.com/GVCLab/PersonaLive/blob/main/README.md)

### Install

Documented setup guidance; these commands were not executed during this review. [Source 1](https://github.com/GVCLab/PersonaLive/blob/main/README.md)

1. Create Python 3.10 and install requirements_base.txt.
2. Obtain the documented model files and configure the reference/driving input.
3. Begin with offline inference before attempting the separate web/realtime acceleration setup.

```sh
pip install -r requirements_base.txt
```


```sh
python inference_offline.py
```

### First project

Begin with a small example and inspect the result before using it in production. [Source 1](https://github.com/GVCLab/PersonaLive/blob/main/README.md)

1. Use an authorized portrait and a short driving clip.
2. Inspect expression, identity consistency and frame transitions before trying a longer sequence.
### Hardware & software

Source-backed requirements; unreported minimums remain unknown. [Source 1](https://github.com/GVCLab/PersonaLive/blob/main/README.md)

- **Hardware:** The documented long-stream offline route lists 12 GB VRAM. A universal real-time minimum, RAM minimum and storage minimum are not published.
- **Software:** Python 3.10 and model dependencies; the online UI uses Node.js >=18. TensorRT engines may need rebuilding for the actual GPU.
- **Platforms:** Linux-centered setup with community Windows/Blackwell guidance. Native macOS support is not established.

### License, model weights & costs

The complete top-level Apache-2.0 software license was reviewed and archived. Dependent models and components retain their own terms. [Source 1](https://github.com/GVCLab/PersonaLive/blob/main/LICENSE) [Source 2](https://github.com/GVCLab/PersonaLive/blob/main/README.md)

- **Code:** Apache-2.0
- **Weights:** Apache-2.0 code; diffusion base models and other checkpoint terms are separate.
- **Commercial:** The reviewed software license permits commercial software use subject to its obligations; it does not clear independent weights, data, assets, services or dependencies.
- **Cost:** Source code is available under the stated license. Compute, storage, optional hardware and any hosted model/API services can add costs; no current service-price quote is asserted.

### Why it merits attention

Included for its concrete documented creative workflow: Exploring animated portrait clips and character-performance prototypes from a reference image. The documentation and developer examples support relevance; output quality, setup success and performance were not independently tested. [Source 1](https://github.com/GVCLab/PersonaLive/blob/main/README.md)

### Limitations

Developer performance examples are not local test results. H100-specific acceleration files are not portable guarantees; the README also points to the later EditaLive project. [Source 1](https://github.com/GVCLab/PersonaLive/blob/main/README.md)

### Get the tool

- [Repository](https://github.com/GVCLab/PersonaLive)
- [Documentation](https://github.com/GVCLab/PersonaLive/blob/main/README.md)
- [License](https://github.com/GVCLab/PersonaLive/blob/main/LICENSE)

## RestoraX

Video, animation & film · Images & design · Audio, music & voice · Archives, media restoration & collections

Completed the detailed guide for an earlier screened discovery. Documentation and complete software license checked on 2026-10-07; no claim of a new release today.

### How it uses AI

Supports integrations such as Real-ESRGAN, DDColor, RIFE, Demucs and VoiceFixer for learned restoration tasks. [Source](https://github.com/karailker/restorax/blob/main/README.md)

### Introduction

A modular restoration research framework connecting image, frame-interpolation and audio stages in a processing graph. [Source 1](https://github.com/karailker/restorax/blob/main/README.md)

### What it is good for

Prototyping restoration chains and comparing intermediate outputs from old films or recordings. [Source 1](https://github.com/karailker/restorax/blob/main/README.md)

### Demo & examples

The README includes author examples and a benchmark table; the latter explicitly approximates stubs on CPU and is not proof of real-model throughput. [Source 1](https://github.com/karailker/restorax/blob/main/README.md)

### Install

Documented setup guidance; these commands were not executed during this review. [Source 1](https://github.com/karailker/restorax/blob/main/README.md)

1. Clone the project and prepare Python 3.11, PyTorch and FFmpeg.
2. Install requirements and the editable package; obtain the actual weights for each intended stage.
3. Begin with a documented CLI pipeline before considering the Redis/Celery/web stack.

```sh
pip install -r requirements.txt
```


```sh
pip install -e .
```


```sh
restorax run --input old_film.mp4 --pipeline sr_x4
```

### First project

Begin with a small example and inspect the result before using it in production. [Source 1](https://github.com/karailker/restorax/blob/main/README.md)

1. Process a short expendable copy and check which stages use real models versus stubs.
2. Compare source and output frames/audio, then retain the original alongside the result.
### Hardware & software

Source-backed requirements; unreported minimums remain unknown. [Source 1](https://github.com/karailker/restorax/blob/main/README.md)

- **Hardware:** README lists 8 GB RAM minimum/16 GB recommended and 5 GB disk minimum/20+ GB with models. GPU recommendation is 8 GB VRAM; CPU operation is described.
- **Software:** Python 3.11, PyTorch >=2.3 and FFmpeg; CUDA 12.1 for the documented NVIDIA setup. The web stack adds services and frontend dependencies.
- **Platforms:** CPU/CUDA routes are described, but a complete supported-OS matrix is not provided.

### License, model weights & costs

The complete top-level MIT software license was reviewed and archived. Dependent models and components retain their own terms. [Source 1](https://github.com/karailker/restorax/blob/main/LICENSE) [Source 2](https://github.com/karailker/restorax/blob/main/README.md)

- **Code:** MIT
- **Weights:** MIT framework. Integrated models/components such as ProPainter or CodeFormer can have additional restrictions; not all pipeline choices are cleared for commercial use.
- **Commercial:** The reviewed software license permits commercial software use subject to its obligations; it does not clear independent weights, data, assets, services or dependencies.
- **Cost:** Source code is available under the stated license. Compute, storage, optional hardware and any hosted model/API services can add costs; no current service-price quote is asserted.

### Why it merits attention

Included for its concrete documented creative workflow: Prototyping restoration chains and comparing intermediate outputs from old films or recordings. The documentation and developer examples support relevance; output quality, setup success and performance were not independently tested. [Source 1](https://github.com/karailker/restorax/blob/main/README.md)

### Limitations

This is a stub-first prototype. Do not interpret the model list or illustrative benchmarks as a validated production restoration application. [Source 1](https://github.com/karailker/restorax/blob/main/README.md)

### Get the tool

- [Repository](https://github.com/karailker/restorax)
- [Documentation](https://github.com/karailker/restorax/blob/main/README.md)
- [License](https://github.com/karailker/restorax/blob/main/LICENSE)

## HOMR GUI

AI music notation and score recovery · Audio, music & voice · Accessible media & assistive creation · Archives, media restoration & collections

Completed the detailed guide for an earlier screened discovery. Documentation and complete software license checked on 2026-10-07; no claim of a new release today.

### How it uses AI

A vision-transformer-based recognition pipeline detects notation and predicts symbolic score content. [Source](https://github.com/Quackone/homr_gui/blob/main/README.md)

### Introduction

A desktop interface for optical music recognition, converting score images into editable symbolic music. [Source 1](https://github.com/Quackone/homr_gui/blob/main/README.md)

### What it is good for

Recovering sheet music into MusicXML/MIDI for proofreading, arrangement or accessible playback. [Source 1](https://github.com/Quackone/homr_gui/blob/main/README.md)

### Demo & examples

The README shows the GUI and example recognition workflow. [Source 1](https://github.com/Quackone/homr_gui/blob/main/README.md)

### Install

Documented setup guidance; these commands were not executed during this review. [Source 1](https://github.com/Quackone/homr_gui/blob/main/README.md)

1. Create the documented Python environment and install requirements.
2. Choose the CPU ONNX runtime or the separately documented CUDA runtime and obtain required model files.
3. Launch the appropriate GUI script.

```sh
pip install -r requirements.txt
```


```sh
python homr_gui_cpu.py
```

### First project

Begin with a small example and inspect the result before using it in production. [Source 1](https://github.com/Quackone/homr_gui/blob/main/README.md)

1. Load a clear score image and crop/prepare it before recognition.
2. Inspect notes, rhythms, voices and measures in notation software before exporting a final score.
### Hardware & software

Source-backed requirements; unreported minimums remain unknown. [Source 1](https://github.com/Quackone/homr_gui/blob/main/README.md)

- **Hardware:** RAM, VRAM and storage minima are not documented; CPU inference is available and GPU runtime is optional.
- **Software:** README lists Python 3.11–3.15, PyQt6 and ONNX Runtime; CUDA builds require matching GPU dependencies.
- **Platforms:** Windows launchers are documented. Equivalent native macOS/Linux release support is not established by the inspected guide.

### License, model weights & costs

The complete top-level AGPL-3.0 software license was reviewed and archived. Dependent models and components retain their own terms. [Source 1](https://github.com/Quackone/homr_gui/blob/main/LICENSE) [Source 2](https://github.com/Quackone/homr_gui/blob/main/README.md)

- **Code:** AGPL-3.0
- **Weights:** AGPL-3.0 GUI source; underlying recognition models and any mirrored weights retain independent terms.
- **Commercial:** The reviewed software license permits commercial software use subject to its obligations; it does not clear independent weights, data, assets, services or dependencies. AGPL obligations can apply when modified software is made available over a network.
- **Cost:** Source code is available under the stated license. Compute, storage, optional hardware and any hosted model/API services can add costs; no current service-price quote is asserted.

### Why it merits attention

Included for its concrete documented creative workflow: Recovering sheet music into MusicXML/MIDI for proofreading, arrangement or accessible playback. The documentation and developer examples support relevance; output quality, setup success and performance were not independently tested. [Source 1](https://github.com/Quackone/homr_gui/blob/main/README.md)

### Limitations

Recognition can misread notation and layout. A successful MusicXML export is not evidence that the score is musically correct. [Source 1](https://github.com/Quackone/homr_gui/blob/main/README.md)

### Get the tool

- [Repository](https://github.com/Quackone/homr_gui)
- [Documentation](https://github.com/Quackone/homr_gui/blob/main/README.md)
- [License](https://github.com/Quackone/homr_gui/blob/main/LICENSE)

## Cypher DJ

Audio, music & voice · Performance, projection & stage media · Interactive, immersive & live media · AI agents for code-authored media production

Completed the detailed guide for an earlier screened discovery. Documentation and complete software license checked on 2026-10-07; no claim of a new release today.

### How it uses AI

A connected language-model agent invokes MCP tools to inspect and control audio operations; the playback engine itself is conventional signal processing. [Source](https://github.com/CytrexSGR/cypher-dj/blob/main/README.md) [Source](https://github.com/CytrexSGR/cypher-dj/blob/main/INSTALL.md) [Source](https://www.infinimind-creations.com/instruments/cypher-dj/)

### Introduction

A public-beta music-performance system combining decks, loop boxes, live coding and AI-agent controls. [Source 1](https://github.com/CytrexSGR/cypher-dj/blob/main/README.md) [Source 2](https://github.com/CytrexSGR/cypher-dj/blob/main/INSTALL.md) [Source 3](https://www.infinimind-creations.com/instruments/cypher-dj/)

### What it is good for

Exploring human/agent co-performance, transitions and timed changes in a local DJ setup. [Source 1](https://github.com/CytrexSGR/cypher-dj/blob/main/README.md) [Source 2](https://github.com/CytrexSGR/cypher-dj/blob/main/INSTALL.md) [Source 3](https://www.infinimind-creations.com/instruments/cypher-dj/)

### Demo & examples

The README and project page present the performance interface and routing approach. [Source 1](https://www.infinimind-creations.com/instruments/cypher-dj/)

### Install

Documented setup guidance; these commands were not executed during this review. [Source 1](https://github.com/CytrexSGR/cypher-dj/blob/main/README.md) [Source 2](https://github.com/CytrexSGR/cypher-dj/blob/main/INSTALL.md) [Source 3](https://www.infinimind-creations.com/instruments/cypher-dj/)

1. Follow INSTALL.md on the documented Ubuntu/PipeWire setup.
2. Build the three native binaries, install Python/Node dependencies and configure music paths.
3. Start the system on its default silent test sink; configure output routing explicitly before a performance.

```sh
djk/start/djk-start
```

### First project

Begin with a small example and inspect the result before using it in production. [Source 1](https://github.com/CytrexSGR/cypher-dj/blob/main/README.md) [Source 2](https://github.com/CytrexSGR/cypher-dj/blob/main/INSTALL.md) [Source 3](https://www.infinimind-creations.com/instruments/cypher-dj/)

1. Load a small local collection and test deck/cue controls.
2. Connect an agent, request one timed transition and listen/inspect timing before enabling more autonomy.
### Hardware & software

Source-backed requirements; unreported minimums remain unknown. [Source 1](https://github.com/CytrexSGR/cypher-dj/blob/main/README.md) [Source 2](https://github.com/CytrexSGR/cypher-dj/blob/main/INSTALL.md) [Source 3](https://www.infinimind-creations.com/instruments/cypher-dj/)

- **Hardware:** The core locks 4 GiB RAM and uses additional shared memory; a complete machine minimum and disk minimum are not published. Audio-interface needs depend on routing.
- **Software:** Ubuntu 24.04 x64, PipeWire/JACK, Node >=22.18, Python, C++/CMake/Ninja, FFmpeg and Rubber Band. Strudel/Carla/Surge are optional routes.
- **Platforms:** Documented Linux setup only; macOS/Windows parity is not established.

### License, model weights & costs

The complete top-level AGPL-3.0 software license was reviewed and archived. Dependent models and components retain their own terms. [Source 1](https://github.com/CytrexSGR/cypher-dj/blob/main/LICENSE) [Source 2](https://github.com/CytrexSGR/cypher-dj/blob/main/README.md) [Source 3](https://github.com/CytrexSGR/cypher-dj/blob/main/INSTALL.md) [Source 4](https://www.infinimind-creations.com/instruments/cypher-dj/)

- **Code:** AGPL-3.0
- **Weights:** AGPL-3.0 source; optional instruments, external agents/models and music assets have separate terms.
- **Commercial:** The reviewed software license permits commercial software use subject to its obligations; it does not clear independent weights, data, assets, services or dependencies. AGPL obligations can apply when modified software is made available over a network.
- **Cost:** Source code is available under the stated license. Compute, storage, optional hardware and any hosted model/API services can add costs; no current service-price quote is asserted.

### Why it merits attention

Included for its concrete documented creative workflow: Exploring human/agent co-performance, transitions and timed changes in a local DJ setup. The documentation and developer examples support relevance; output quality, setup success and performance were not independently tested. [Source 1](https://github.com/CytrexSGR/cypher-dj/blob/main/README.md) [Source 2](https://github.com/CytrexSGR/cypher-dj/blob/main/INSTALL.md) [Source 3](https://www.infinimind-creations.com/instruments/cypher-dj/)

### Limitations

Public beta. Physical headphone-path latency is not measured, roughly 11 ms round-trip is uncompensated in the described setup, and a private catalog database is not supplied. Not tested for live reliability. [Source 1](https://github.com/CytrexSGR/cypher-dj/blob/main/README.md) [Source 2](https://github.com/CytrexSGR/cypher-dj/blob/main/INSTALL.md) [Source 3](https://www.infinimind-creations.com/instruments/cypher-dj/)

### Get the tool

- [Repository](https://github.com/CytrexSGR/cypher-dj)
- [Documentation](https://www.infinimind-creations.com/instruments/cypher-dj/)
- [License](https://github.com/CytrexSGR/cypher-dj/blob/main/LICENSE)

## AutoSubs

Video, animation & film · Audio, music & voice · Accessible media & assistive creation · Editing, captions & post-production

First detailed library baseline. Documentation and complete software license checked on 2026-10-07; no claim of a new release today.

### How it uses AI

Local speech-recognition models, voice-activity detection and optional diarization/alignment produce timed text. [Source](https://github.com/tmoroney/auto-subs/blob/main/README.md)

### Introduction

A local transcription and subtitle application with optional editing-host integrations. [Source 1](https://github.com/tmoroney/auto-subs/blob/main/README.md)

### What it is good for

Captioning short films, interviews and social clips, either standalone or alongside a video editor. [Source 1](https://github.com/tmoroney/auto-subs/blob/main/README.md)

### Demo & examples

The official README illustrates the subtitle editor and DaVinci Resolve/Adobe integrations. [Source 1](https://github.com/tmoroney/auto-subs/blob/main/README.md)

### Install

Documented setup guidance; these commands were not executed during this review. [Source 1](https://github.com/tmoroney/auto-subs/blob/main/README.md)

1. Download the official installer matching your OS, or use the documented macOS Homebrew cask.
2. Download a recognition model in the Model Manager.
3. Import a small media file; configure an editing-host connection only if needed.

```sh
brew install --cask auto-subs
```

### First project

Begin with a small example and inspect the result before using it in production. [Source 1](https://github.com/tmoroney/auto-subs/blob/main/README.md)

1. Transcribe, correct names and timing, and review speaker segmentation.
2. Export SRT/text or copy text; test the captions in the target editor.
### Hardware & software

Source-backed requirements; unreported minimums remain unknown. [Source 1](https://github.com/tmoroney/auto-subs/blob/main/README.md)

- **Hardware:** Author estimates for Whisper range from tiny (~80 MB weights/~1 GB RAM) to large (~3.1 GB/~10 GB RAM). These are approximate model figures, not total application minima. Optional alignment adds ~320 MB.
- **Software:** Packaged app plus downloaded recognition/VAD/diarization assets. Editing integrations have separate host-version requirements.
- **Platforms:** Windows x64, macOS Apple Silicon/Intel, and Linux deb/rpm distributions are documented.

### License, model weights & costs

The complete top-level MIT software license was reviewed and archived. Dependent models and components retain their own terms. [Source 1](https://github.com/tmoroney/auto-subs/blob/main/LICENSE) [Source 2](https://github.com/tmoroney/auto-subs/blob/main/README.md)

- **Code:** MIT
- **Weights:** MIT app. Models have separate terms; optional MMS forced alignment is CC-BY-NC-4.0 and must not be treated as cleared for commercial work.
- **Commercial:** The reviewed software license permits commercial software use subject to its obligations; it does not clear independent weights, data, assets, services or dependencies.
- **Cost:** Source code is available under the stated license. Compute, storage, optional hardware and any hosted model/API services can add costs; no current service-price quote is asserted.

### Why it merits attention

Included for its concrete documented creative workflow: Captioning short films, interviews and social clips, either standalone or alongside a video editor. The documentation and developer examples support relevance; output quality, setup success and performance were not independently tested. [Source 1](https://github.com/tmoroney/auto-subs/blob/main/README.md)

### Limitations

Author accuracy rankings are relative claims, not independent evaluation. Proprietary Resolve/Adobe hosts are optional and separately licensed; subtitle timing and text require review. [Source 1](https://github.com/tmoroney/auto-subs/blob/main/README.md)

### Get the tool

- [Repository](https://github.com/tmoroney/auto-subs)
- [Documentation](https://github.com/tmoroney/auto-subs/blob/main/README.md)
- [License](https://github.com/tmoroney/auto-subs/blob/main/LICENSE)

## ClearerVoice-Studio

Audio, music & voice · Video, animation & film · Archives, media restoration & collections

First detailed library baseline. Documentation and complete software license checked on 2026-10-07; no claim of a new release today.

### How it uses AI

Pretrained neural models, including MossFormer variants, estimate enhanced or separated speech waveforms. [Source](https://github.com/modelscope/ClearerVoice-Studio/blob/main/README.md) [Source](https://github.com/modelscope/ClearerVoice-Studio/blob/main/clearvoice/README.md) [Source](https://huggingface.co/spaces/alibabasglab/ClearVoice) [Source](https://modelscope.cn/models/iic/ClearerVoice-Studio) [Source](https://modelscope.cn/studios/iic/ClearerVoice-Studio)

### Introduction

A speech-processing toolkit for enhancement, source separation, super-resolution and audio-visual target extraction. [Source 1](https://github.com/modelscope/ClearerVoice-Studio/blob/main/README.md) [Source 2](https://github.com/modelscope/ClearerVoice-Studio/blob/main/clearvoice/README.md) [Source 3](https://huggingface.co/spaces/alibabasglab/ClearVoice) [Source 4](https://modelscope.cn/models/iic/ClearerVoice-Studio) [Source 5](https://modelscope.cn/studios/iic/ClearerVoice-Studio)

### What it is good for

Improving intelligibility in recorded dialogue and exploring speech cleanup before an edit. [Source 1](https://github.com/modelscope/ClearerVoice-Studio/blob/main/README.md) [Source 2](https://github.com/modelscope/ClearerVoice-Studio/blob/main/clearvoice/README.md) [Source 3](https://huggingface.co/spaces/alibabasglab/ClearVoice) [Source 4](https://modelscope.cn/models/iic/ClearerVoice-Studio) [Source 5](https://modelscope.cn/studios/iic/ClearerVoice-Studio)

### Demo & examples

Official Hugging Face and ModelScope spaces provide speech-processing demonstrations. [Source 1](https://huggingface.co/spaces/alibabasglab/ClearVoice)

### Install

Documented setup guidance; these commands were not executed during this review. [Source 1](https://github.com/modelscope/ClearerVoice-Studio/blob/main/README.md) [Source 2](https://github.com/modelscope/ClearerVoice-Studio/blob/main/clearvoice/README.md) [Source 3](https://huggingface.co/spaces/alibabasglab/ClearVoice) [Source 4](https://modelscope.cn/models/iic/ClearerVoice-Studio) [Source 5](https://modelscope.cn/studios/iic/ClearerVoice-Studio)

1. Install the clearvoice package in a compatible Python environment.
2. Install FFmpeg for non-WAV formats.
3. Select the model/task in the documented Python API; weights download from the supported model hosts.

```sh
pip install clearvoice
```

### First project

Begin with a small example and inspect the result before using it in production. [Source 1](https://github.com/modelscope/ClearerVoice-Studio/blob/main/README.md) [Source 2](https://github.com/modelscope/ClearerVoice-Studio/blob/main/clearvoice/README.md) [Source 3](https://huggingface.co/spaces/alibabasglab/ClearVoice) [Source 4](https://modelscope.cn/models/iic/ClearerVoice-Studio) [Source 5](https://modelscope.cn/studios/iic/ClearerVoice-Studio)

1. Use the documented ClearVoice(task="speech_enhancement", model_names=["MossFormer2_SE_48K"]) example on one short recording.
2. Write the returned waveform and listen against the original for artifacts and lost consonants.
### Hardware & software

Source-backed requirements; unreported minimums remain unknown. [Source 1](https://github.com/modelscope/ClearerVoice-Studio/blob/main/README.md) [Source 2](https://github.com/modelscope/ClearerVoice-Studio/blob/main/clearvoice/README.md) [Source 3](https://huggingface.co/spaces/alibabasglab/ClearVoice) [Source 4](https://modelscope.cn/models/iic/ClearerVoice-Studio) [Source 5](https://modelscope.cn/studios/iic/ClearerVoice-Studio)

- **Hardware:** Minimum RAM, VRAM and storage are not documented in the inspected guide; model choice and input duration affect requirements.
- **Software:** Python package and model dependencies; FFmpeg for broader format support. An exact universal Python/backend version is not established in the inspected guide.
- **Platforms:** FFmpeg setup instructions cover Linux, macOS and Windows, but do not themselves verify every inference model on each OS/GPU.

### License, model weights & costs

The complete top-level Apache-2.0 software license was reviewed and archived. Dependent models and components retain their own terms. [Source 1](https://github.com/modelscope/ClearerVoice-Studio/blob/main/LICENSE) [Source 2](https://github.com/modelscope/ClearerVoice-Studio/blob/main/README.md) [Source 3](https://github.com/modelscope/ClearerVoice-Studio/blob/main/clearvoice/README.md) [Source 4](https://huggingface.co/spaces/alibabasglab/ClearVoice) [Source 5](https://modelscope.cn/models/iic/ClearerVoice-Studio) [Source 6](https://modelscope.cn/studios/iic/ClearerVoice-Studio)

- **Code:** Apache-2.0
- **Weights:** Apache-2.0 code. Individual pretrained model cards and dependency terms should be checked separately; a blanket weight license is not established here.
- **Commercial:** The reviewed software license permits commercial software use subject to its obligations; it does not clear independent weights, data, assets, services or dependencies.
- **Cost:** Source code is available under the stated license. Compute, storage, optional hardware and any hosted model/API services can add costs; no current service-price quote is asserted.

### Why it merits attention

Included for its concrete documented creative workflow: Improving intelligibility in recorded dialogue and exploring speech cleanup before an edit. The documentation and developer examples support relevance; output quality, setup success and performance were not independently tested. [Source 1](https://github.com/modelscope/ClearerVoice-Studio/blob/main/README.md) [Source 2](https://github.com/modelscope/ClearerVoice-Studio/blob/main/clearvoice/README.md) [Source 3](https://huggingface.co/spaces/alibabasglab/ClearVoice) [Source 4](https://modelscope.cn/models/iic/ClearerVoice-Studio) [Source 5](https://modelscope.cn/studios/iic/ClearerVoice-Studio)

### Limitations

Focused on speech, not guaranteed general music restoration. Developer metrics and demonstrations were reviewed, but no independent listening/performance test was performed. [Source 1](https://github.com/modelscope/ClearerVoice-Studio/blob/main/README.md) [Source 2](https://github.com/modelscope/ClearerVoice-Studio/blob/main/clearvoice/README.md) [Source 3](https://huggingface.co/spaces/alibabasglab/ClearVoice) [Source 4](https://modelscope.cn/models/iic/ClearerVoice-Studio) [Source 5](https://modelscope.cn/studios/iic/ClearerVoice-Studio)

### Get the tool

- [Repository](https://github.com/modelscope/ClearerVoice-Studio)
- [Documentation](https://huggingface.co/spaces/alibabasglab/ClearVoice)
- [License](https://github.com/modelscope/ClearerVoice-Studio/blob/main/LICENSE)

## Video Subtitle Remover

Video, animation & film · Editing, captions & post-production · Archives, media restoration & collections

First detailed library baseline. Documentation and complete software license checked on 2026-10-07; no claim of a new release today.

### How it uses AI

OCR/region detection identifies text and learned temporal/image inpainting estimates replacement pixels. [Source](https://github.com/YaoFANGUK/video-subtitle-remover/blob/main/README.md)

### Introduction

A local application that detects and fills burned-in subtitle regions with neural inpainting. [Source 1](https://github.com/YaoFANGUK/video-subtitle-remover/blob/main/README.md)

### What it is good for

Preparing authorized footage for relocalization or removing obsolete text from a clean edit copy. [Source 1](https://github.com/YaoFANGUK/video-subtitle-remover/blob/main/README.md)

### Demo & examples

The README includes before/after clips and GUI screenshots. [Source 1](https://github.com/YaoFANGUK/video-subtitle-remover/blob/main/README.md)

### Install

Documented setup guidance; these commands were not executed during this review. [Source 1](https://github.com/YaoFANGUK/video-subtitle-remover/blob/main/README.md)

1. Choose the Windows CPU, DirectML or matching NVIDIA package, or use the documented source route.
2. For source, set up the platform-specific Python/Paddle/PyTorch backend before installing requirements.
3. Launch the GUI and select a short clip plus the intended subtitle region.

```sh
pip install -r requirements.txt
```


```sh
python gui.py
```

### First project

Begin with a small example and inspect the result before using it in production. [Source 1](https://github.com/YaoFANGUK/video-subtitle-remover/blob/main/README.md)

1. Set the text region carefully and process a short segment.
2. Check temporal consistency and restored detail before processing the full authorized source.
### Hardware & software

Source-backed requirements; unreported minimums remain unknown. [Source 1](https://github.com/YaoFANGUK/video-subtitle-remover/blob/main/README.md)

- **Hardware:** Minimum RAM, VRAM and storage are not documented. CUDA package selection varies by GPU generation; CPU/DirectML alternatives are documented.
- **Software:** Source instructions use Python 3.12+ with Paddle 3/PyTorch 2.7 routes; macOS examples include Python 3.13. CUDA 11.8/12.6/12.8 distributions are not interchangeable.
- **Platforms:** Windows packages; source instructions for Windows, Linux and macOS. Intel Mac CPU and Apple Silicon routes have distinct guidance and OCR caveats.

### License, model weights & costs

The complete top-level Apache-2.0 software license was reviewed and archived. Dependent models and components retain their own terms. [Source 1](https://github.com/YaoFANGUK/video-subtitle-remover/blob/main/LICENSE) [Source 2](https://github.com/YaoFANGUK/video-subtitle-remover/blob/main/README.md)

- **Code:** Apache-2.0
- **Weights:** Apache-2.0 code; STTN/LaMa and other dependent models retain independent terms.
- **Commercial:** The reviewed software license permits commercial software use subject to its obligations; it does not clear independent weights, data, assets, services or dependencies.
- **Cost:** Source code is available under the stated license. Compute, storage, optional hardware and any hosted model/API services can add costs; no current service-price quote is asserted.

### Why it merits attention

Included for its concrete documented creative workflow: Preparing authorized footage for relocalization or removing obsolete text from a clean edit copy. The documentation and developer examples support relevance; output quality, setup success and performance were not independently tested. [Source 1](https://github.com/YaoFANGUK/video-subtitle-remover/blob/main/README.md)

### Limitations

Inpainting invents replacement pixels and can damage moving textures. Keeping resolution does not mean lossless visual restoration. Inspect OCR/model-specific platform warnings. [Source 1](https://github.com/YaoFANGUK/video-subtitle-remover/blob/main/README.md)

### Get the tool

- [Repository](https://github.com/YaoFANGUK/video-subtitle-remover)
- [Documentation](https://github.com/YaoFANGUK/video-subtitle-remover/blob/main/README.md)
- [License](https://github.com/YaoFANGUK/video-subtitle-remover/blob/main/LICENSE)

## Audio as Code

Audio, music & voice · AI music notation and score recovery · Games & production pipelines · AI agents for code-authored media production

First detailed library baseline. Documentation and complete software license checked on 2026-10-07; no claim of a new release today.

### How it uses AI

An external creative agent makes musical decisions in a structured score; synthesis/rendering is deterministic and does not bundle or call a neural model. [Source](https://github.com/joaoCarvalho1000/audio-as-code/blob/main/README.md) [Source](https://audioascode.com)

### Introduction

A music framework for AI-agent-authored, editable scores with local WAV, stems and MIDI rendering. [Source 1](https://github.com/joaoCarvalho1000/audio-as-code/blob/main/README.md) [Source 2](https://audioascode.com)

### What it is good for

Composing reproducible soundtracks, game loops, audio logos and presentation cues that remain editable as code or JSON. [Source 1](https://github.com/joaoCarvalho1000/audio-as-code/blob/main/README.md) [Source 2](https://audioascode.com)

### Demo & examples

The official site offers listening examples and editable-score demonstrations. [Source 1](https://audioascode.com)

### Install

Documented setup guidance; these commands were not executed during this review. [Source 1](https://github.com/joaoCarvalho1000/audio-as-code/blob/main/README.md) [Source 2](https://audioascode.com)

1. Install Python >=3.10 and uv.
2. Initialize a composition workspace with the documented pinned package.
3. Sync dependencies, run the doctor and render the starter composer.

```sh
uvx --from audio-as-code==0.4.0 aac init my-soundtrack
```


```sh
cd my-soundtrack
```


```sh
uv sync
```


```sh
uv run aac doctor
```


```sh
uv run python compose.py
```

### First project

Begin with a small example and inspect the result before using it in production. [Source 1](https://github.com/joaoCarvalho1000/audio-as-code/blob/main/README.md) [Source 2](https://audioascode.com)

1. Ask an external agent to draft a brief, timed composition or edit the starter manually.
2. Listen to the WAV, revise score/mix parameters, and retain MIDI, stems and source alongside the final cue.
### Hardware & software

Source-backed requirements; unreported minimums remain unknown. [Source 1](https://github.com/joaoCarvalho1000/audio-as-code/blob/main/README.md) [Source 2](https://audioascode.com)

- **Hardware:** No API key, model weights, audio device or DAW is required for local rendering. Numeric RAM/storage minima are not documented; an external agent has separate requirements.
- **Software:** Python >=3.10 and uv or a Python virtual environment. Version 0.4.0 is an alpha with procedural instrument prototypes.
- **Platforms:** Windows, macOS and Linux instructions are provided.

### License, model weights & costs

The complete top-level MIT software license was reviewed and archived. Dependent models and components retain their own terms. [Source 1](https://github.com/joaoCarvalho1000/audio-as-code/blob/main/LICENSE) [Source 2](https://github.com/joaoCarvalho1000/audio-as-code/blob/main/README.md) [Source 3](https://audioascode.com)

- **Code:** MIT
- **Weights:** MIT software; external AI-agent terms and any imported score/material rights remain separate.
- **Commercial:** The reviewed software license permits commercial software use subject to its obligations; it does not clear independent weights, data, assets, services or dependencies.
- **Cost:** Source code is available under the stated license. Compute, storage, optional hardware and any hosted model/API services can add costs; no current service-price quote is asserted.

### Why it merits attention

Included for its concrete documented creative workflow: Composing reproducible soundtracks, game loops, audio logos and presentation cues that remain editable as code or JSON. The documentation and developer examples support relevance; output quality, setup success and performance were not independently tested. [Source 1](https://github.com/joaoCarvalho1000/audio-as-code/blob/main/README.md) [Source 2](https://audioascode.com)

### Limitations

Procedural voices are prototypes, and numerical measurements do not prove musical realism. MIDI playback depends on the receiving synth; the renderer does not autonomously turn a prompt into music. [Source 1](https://github.com/joaoCarvalho1000/audio-as-code/blob/main/README.md) [Source 2](https://audioascode.com)

### Get the tool

- [Repository](https://github.com/joaoCarvalho1000/audio-as-code)
- [Documentation](https://audioascode.com)
- [License](https://github.com/joaoCarvalho1000/audio-as-code/blob/main/LICENSE)

## sense-music

Audio, music & voice · Editing, captions & post-production · Data art & scientific visualization · Performance, projection & stage media

First detailed library baseline. Documentation and complete software license checked on 2026-10-07; no claim of a new release today.

### How it uses AI

Optional CLAP embeddings/tags, Demucs stems, Whisper lyrics and Qwen2-Audio captions provide concrete AI analysis beyond the conventional signal-processing core. [Source](https://github.com/HumanjavaEnterprises/huje.sensemusic.OC-python.src/blob/main/README.md) [Source](https://github.com/HumanjavaEnterprises/huje.sensemusic.OC-python.src/blob/main/pyproject.toml) [Source](https://pypi.org/project/sense-music/)

### Introduction

A Python music-analysis toolkit producing timing, structure and visual reports, with optional neural perception layers. [Source 1](https://github.com/HumanjavaEnterprises/huje.sensemusic.OC-python.src/blob/main/README.md) [Source 2](https://github.com/HumanjavaEnterprises/huje.sensemusic.OC-python.src/blob/main/pyproject.toml) [Source 3](https://pypi.org/project/sense-music/)

### What it is good for

Finding edit points, comparing references and inspecting arrangement or sonic character before a media edit. [Source 1](https://github.com/HumanjavaEnterprises/huje.sensemusic.OC-python.src/blob/main/README.md) [Source 2](https://github.com/HumanjavaEnterprises/huje.sensemusic.OC-python.src/blob/main/pyproject.toml) [Source 3](https://pypi.org/project/sense-music/)

### Demo & examples

The README shows analysis objects, report exports and edit-point examples. [Source 1](https://pypi.org/project/sense-music/)

### Install

Documented setup guidance; these commands were not executed during this review. [Source 1](https://github.com/HumanjavaEnterprises/huje.sensemusic.OC-python.src/blob/main/README.md) [Source 2](https://github.com/HumanjavaEnterprises/huje.sensemusic.OC-python.src/blob/main/pyproject.toml) [Source 3](https://pypi.org/project/sense-music/)

1. Install Python >=3.10 and the desired extras.
2. The full extra includes heavier perception dependencies; Python 3.12 needs the documented Git build of madmom.
3. Enable only the neural layers needed for the first analysis.

```sh
pip install "sense-music[full]"
```

### First project

Begin with a small example and inspect the result before using it in production. [Source 1](https://github.com/HumanjavaEnterprises/huje.sensemusic.OC-python.src/blob/main/README.md) [Source 2](https://github.com/HumanjavaEnterprises/huje.sensemusic.OC-python.src/blob/main/pyproject.toml) [Source 3](https://pypi.org/project/sense-music/)

1. Call analyze("song.mp3", rhythm=True, embedding=True, clap_tags=True, stems=True, caption=False).
2. Save the result to an output directory and inspect the HTML/images; use edit_points(result, snap=True) to review proposed bar-aligned cuts.
### Hardware & software

Source-backed requirements; unreported minimums remain unknown. [Source 1](https://github.com/HumanjavaEnterprises/huje.sensemusic.OC-python.src/blob/main/README.md) [Source 2](https://github.com/HumanjavaEnterprises/huje.sensemusic.OC-python.src/blob/main/pyproject.toml) [Source 3](https://pypi.org/project/sense-music/)

- **Hardware:** Numeric RAM, VRAM and disk minima are not documented. Optional Qwen2-Audio captions load a 7B model and are substantially heavier than the basic analysis.
- **Software:** Python >=3.10; optional transformers, madmom, Demucs and other extras. Model assets/dependencies vary by enabled layer.
- **Platforms:** The inspected documentation does not provide a validated OS-by-OS support matrix.

### License, model weights & costs

The complete top-level MIT software license was reviewed and archived. Dependent models and components retain their own terms. [Source 1](https://github.com/HumanjavaEnterprises/huje.sensemusic.OC-python.src/blob/main/LICENSE) [Source 2](https://github.com/HumanjavaEnterprises/huje.sensemusic.OC-python.src/blob/main/README.md) [Source 3](https://github.com/HumanjavaEnterprises/huje.sensemusic.OC-python.src/blob/main/pyproject.toml) [Source 4](https://pypi.org/project/sense-music/)

- **Code:** MIT
- **Weights:** MIT package; optional neural models, source audio and hosted-service terms are independent.
- **Commercial:** The reviewed software license permits commercial software use subject to its obligations; it does not clear independent weights, data, assets, services or dependencies.
- **Cost:** Source code is available under the stated license. Compute, storage, optional hardware and any hosted model/API services can add costs; no current service-price quote is asserted.

### Why it merits attention

Included for its concrete documented creative workflow: Finding edit points, comparing references and inspecting arrangement or sonic character before a media edit. The documentation and developer examples support relevance; output quality, setup success and performance were not independently tested. [Source 1](https://github.com/HumanjavaEnterprises/huje.sensemusic.OC-python.src/blob/main/README.md) [Source 2](https://github.com/HumanjavaEnterprises/huje.sensemusic.OC-python.src/blob/main/pyproject.toml) [Source 3](https://pypi.org/project/sense-music/)

### Limitations

Missing optional dependencies can cause graceful feature omission, so inspect which outputs were actually produced. Musical tags and suggested cut points need listening-based review. [Source 1](https://github.com/HumanjavaEnterprises/huje.sensemusic.OC-python.src/blob/main/README.md) [Source 2](https://github.com/HumanjavaEnterprises/huje.sensemusic.OC-python.src/blob/main/pyproject.toml) [Source 3](https://pypi.org/project/sense-music/)

### Get the tool

- [Repository](https://github.com/HumanjavaEnterprises/huje.sensemusic.OC-python.src)
- [Documentation](https://pypi.org/project/sense-music/)
- [License](https://github.com/HumanjavaEnterprises/huje.sensemusic.OC-python.src/blob/main/LICENSE)

## Time-multiplexed Neural Holography

Neural holography and light-field media · Computational art & creative coding · Physical, robotic & kinetic installations · WebXR, VR & AR

First detailed library baseline. Documentation and complete software license checked on 2026-10-07; no claim of a new release today.

### How it uses AI

Learned propagation models and optimization produce time-multiplexed phase patterns matched to a calibrated optical system. [Source](https://github.com/computational-imaging/time-multiplexed-neural-holography/blob/main/README.md) [Source](https://github.com/computational-imaging/time-multiplexed-neural-holography/blob/main/env.yml) [Source](https://www.computationalimaging.org/publications/time-multiplexed-neural-holography/)

### Introduction

A SIGGRAPH 2022 research implementation for learned holographic display synthesis using fast spatial light modulators. [Source 1](https://github.com/computational-imaging/time-multiplexed-neural-holography/blob/main/README.md) [Source 2](https://github.com/computational-imaging/time-multiplexed-neural-holography/blob/main/env.yml) [Source 3](https://www.computationalimaging.org/publications/time-multiplexed-neural-holography/)

### What it is good for

Exploring holographic display pipelines from 2D, RGB-D or light-field content in an optics research setup. [Source 1](https://github.com/computational-imaging/time-multiplexed-neural-holography/blob/main/README.md) [Source 2](https://github.com/computational-imaging/time-multiplexed-neural-holography/blob/main/env.yml) [Source 3](https://www.computationalimaging.org/publications/time-multiplexed-neural-holography/)

### Demo & examples

The official Stanford computational-imaging project page contains the paper and display demonstrations. [Source 1](https://www.computationalimaging.org/publications/time-multiplexed-neural-holography/)

### Install

Documented setup guidance; these commands were not executed during this review. [Source 1](https://github.com/computational-imaging/time-multiplexed-neural-holography/blob/main/README.md) [Source 2](https://github.com/computational-imaging/time-multiplexed-neural-holography/blob/main/env.yml) [Source 3](https://www.computationalimaging.org/publications/time-multiplexed-neural-holography/)

1. Clone the source and create the environment from env.yml.
2. Obtain the linked models/data and edit parameters for the intended optical setup.
3. Begin with the documented simulated 2D example before any camera-in-the-loop or display experiment.

```sh
conda env create -f env.yml
```


```sh
conda activate tmnh
```


```sh
python main.py -c=configs_2d.txt --channel=0
```

### First project

Begin with a small example and inspect the result before using it in production. [Source 1](https://github.com/computational-imaging/time-multiplexed-neural-holography/blob/main/README.md) [Source 2](https://github.com/computational-imaging/time-multiplexed-neural-holography/blob/main/env.yml) [Source 3](https://www.computationalimaging.org/publications/time-multiplexed-neural-holography/)

1. Generate a single-channel phase sequence using the example configuration.
2. Review simulated reconstruction, repeat the documented RGB channel process, and calibrate physical playback separately if appropriate hardware is available.
### Hardware & software

Source-backed requirements; unreported minimums remain unknown. [Source 1](https://github.com/computational-imaging/time-multiplexed-neural-holography/blob/main/README.md) [Source 2](https://github.com/computational-imaging/time-multiplexed-neural-holography/blob/main/env.yml) [Source 3](https://www.computationalimaging.org/publications/time-multiplexed-neural-holography/)

- **Hardware:** Physical playback requires a compatible fast quantized spatial light modulator and calibrated optics/camera setup. Universal GPU, RAM, VRAM and storage minima are not documented.
- **Software:** Conda environment uses Python 3.10 with PyTorch/Lightning and optical-model dependencies. Configuration and calibration are project-specific.
- **Platforms:** The inspected research guide does not establish a complete supported desktop-OS matrix. This is not a standard VR-headset plug-in.

### License, model weights & costs

The complete top-level MIT software license was reviewed and archived. Dependent models and components retain their own terms. [Source 1](https://github.com/computational-imaging/time-multiplexed-neural-holography/blob/main/LICENSE) [Source 2](https://github.com/computational-imaging/time-multiplexed-neural-holography/blob/main/README.md) [Source 3](https://github.com/computational-imaging/time-multiplexed-neural-holography/blob/main/env.yml) [Source 4](https://www.computationalimaging.org/publications/time-multiplexed-neural-holography/)

- **Code:** MIT
- **Weights:** MIT software. Linked datasets, pretrained assets and physical hardware have independent conditions.
- **Commercial:** The reviewed software license permits commercial software use subject to its obligations; it does not clear independent weights, data, assets, services or dependencies.
- **Cost:** Source code is available under the stated license. Compute, storage, optional hardware and any hosted model/API services can add costs; no current service-price quote is asserted.

### Why it merits attention

Included for its concrete documented creative workflow: Exploring holographic display pipelines from 2D, RGB-D or light-field content in an optics research setup. The documentation and developer examples support relevance; output quality, setup success and performance were not independently tested. [Source 1](https://github.com/computational-imaging/time-multiplexed-neural-holography/blob/main/README.md) [Source 2](https://github.com/computational-imaging/time-multiplexed-neural-holography/blob/main/env.yml) [Source 3](https://www.computationalimaging.org/publications/time-multiplexed-neural-holography/)

### Limitations

An established research baseline newly documented in this library, not a newly launched 2026 tool. Reproducing optical results requires specialist equipment; no hardware experiment was performed. [Source 1](https://github.com/computational-imaging/time-multiplexed-neural-holography/blob/main/README.md) [Source 2](https://github.com/computational-imaging/time-multiplexed-neural-holography/blob/main/env.yml) [Source 3](https://www.computationalimaging.org/publications/time-multiplexed-neural-holography/)

### Get the tool

- [Repository](https://github.com/computational-imaging/time-multiplexed-neural-holography)
- [Documentation](https://www.computationalimaging.org/publications/time-multiplexed-neural-holography/)
- [License](https://github.com/computational-imaging/time-multiplexed-neural-holography/blob/main/LICENSE)

## NeuralNote

Audio, music & voice · AI music notation and score recovery · Performance, projection & stage media

First detailed library baseline. Documentation and complete software license checked on 2026-10-07; no claim of a new release today.

### How it uses AI

Version 2 uses MuScriptor neural transcription models to infer notes and instrument groups from an audio mix. [Source](https://github.com/DamRsn/NeuralNote/blob/main/README.md)

### Introduction

A local audio-to-MIDI application and DAW plug-in with multi-instrument transcription and built-in audition synthesis. [Source 1](https://github.com/DamRsn/NeuralNote/blob/main/README.md)

### What it is good for

Recovering editable note ideas from recordings, sketching arrangements and comparing a transcript with its source audio. [Source 1](https://github.com/DamRsn/NeuralNote/blob/main/README.md)

### Demo & examples

The official README shows the piano-roll interface and playback/transcription workflow. [Source 1](https://github.com/DamRsn/NeuralNote/blob/main/README.md)

### Install

Documented setup guidance; these commands were not executed during this review. [Source 1](https://github.com/DamRsn/NeuralNote/blob/main/README.md)

1. Choose the official Apple Silicon macOS or Windows x64 installer; other documented platforms currently require source builds.
2. Download a model from inside the application.
3. Open the standalone app or insert the VST3/AU in a compatible DAW.
### First project

Begin with a small example and inspect the result before using it in production. [Source 1](https://github.com/DamRsn/NeuralNote/blob/main/README.md)

1. Drop an audio file or record a short track excerpt.
2. Choose instruments or Automatic, transcribe, audition against the source, then drag/save MIDI and correct mistakes.
### Hardware & software

Source-backed requirements; unreported minimums remain unknown. [Source 1](https://github.com/DamRsn/NeuralNote/blob/main/README.md)

- **Hardware:** Model downloads are approximately 210 MB small, 620 MB medium and 2.7 GB large. A GPU is strongly recommended for medium/large; universal RAM/VRAM minima are not given. Published M1 Pro speeds are author measurements.
- **Software:** Metal on macOS, Vulkan on Windows/Linux, or CPU. Source builds require Git/submodules, CMake, a C++23 compiler and Python 3; additional platform SDK dependencies apply.
- **Platforms:** Packaged Apple Silicon macOS and Windows x64. Intel Mac and Linux installers are planned; source instructions include Ubuntu 24.04/Clang 20. Only a few machines/GPUs have been tested by the authors.

### License, model weights & costs

The complete top-level Apache-2.0 software license was reviewed and archived. Dependent models and components retain their own terms. [Source 1](https://github.com/DamRsn/NeuralNote/blob/main/LICENSE) [Source 2](https://github.com/DamRsn/NeuralNote/blob/main/README.md)

- **Code:** Apache-2.0
- **Weights:** Apache-2.0 application code. MuScriptor/GGUF weights use CC-BY-NC-4.0. JUCE, ASIO, fonts and soundfonts have separate notices; Windows ASIO redistribution has an additional agreement.
- **Commercial:** Apache-2.0 covers the application code only. The supplied MuScriptor weights may be used only non-commercially, so this workflow is not cleared for commercial/client production.
- **Cost:** Source code is available under the stated license. Compute, storage, optional hardware and any hosted model/API services can add costs; no current service-price quote is asserted.

### Why it merits attention

Included for its concrete documented creative workflow: Recovering editable note ideas from recordings, sketching arrangements and comparing a transcript with its source audio. The documentation and developer examples support relevance; output quality, setup success and performance were not independently tested. [Source 1](https://github.com/DamRsn/NeuralNote/blob/main/README.md)

### Limitations

The v2 model is non-commercial despite open application code. Instrument identification and notes require proofreading; MIDI-out and CLI are roadmap items, not current confirmed features. [Source 1](https://github.com/DamRsn/NeuralNote/blob/main/README.md)

### Get the tool

- [Repository](https://github.com/DamRsn/NeuralNote)
- [Documentation](https://github.com/DamRsn/NeuralNote/blob/main/README.md)
- [License](https://github.com/DamRsn/NeuralNote/blob/main/LICENSE)

## Neural Resonator VST

Audio, music & voice · Computational art & creative coding · Performance, projection & stage media

First detailed library baseline. Documentation and complete software license checked on 2026-10-07; no claim of a new release today.

### How it uses AI

A LibTorch neural network predicts filter behavior from an arbitrary 2D shape/material representation. [Source](https://github.com/rodrigodzf/NeuralResonatorVST/blob/main/README.md)

### Introduction

A neural sound-design plug-in that turns drawn shapes and material choices into resonant filters. [Source 1](https://github.com/rodrigodzf/NeuralResonatorVST/blob/main/README.md)

### What it is good for

Exploring imagined objects and sculptural timbres by exciting a modelled resonator with MIDI impulses or incoming audio. [Source 1](https://github.com/rodrigodzf/NeuralResonatorVST/blob/main/README.md)

### Demo & examples

The README links a developer demonstration video with the plug-in workflow. [Source 1](https://github.com/rodrigodzf/NeuralResonatorVST/blob/main/README.md)

### Install

Documented setup guidance; these commands were not executed during this review. [Source 1](https://github.com/rodrigodzf/NeuralResonatorVST/blob/main/README.md)

1. Download the documented Mac or Linux VST3 release and place it in the platform’s VST3 folder.
2. Rescan plug-ins in a compatible host.
3. For source builds, clone with submodules and follow bin/build.sh; LibTorch downloads and JUCE dependencies are additional.

```sh
git clone --recurse-submodules https://github.com/rodrigodzf/NeuralResonatorVST.git
```


```sh
bash ./bin/build.sh
```

### First project

Begin with a small example and inspect the result before using it in production. [Source 1](https://github.com/rodrigodzf/NeuralResonatorVST/blob/main/README.md)

1. Select/draw a shape and material, then excite the resonator with a quiet MIDI impulse.
2. Compare the response with an incoming sound and adjust parameters before using it in a mix.
### Hardware & software

Source-backed requirements; unreported minimums remain unknown. [Source 1](https://github.com/rodrigodzf/NeuralResonatorVST/blob/main/README.md)

- **Hardware:** RAM, VRAM, CPU and storage minima are not documented; a compatible audio host/output device is needed for plug-in use.
- **Software:** VST3 host, LibTorch and JUCE. Source builds need the documented native toolchain; the web GUI adds React/TypeScript dependencies, with a traditional C++ GUI option.
- **Platforms:** Mac and Linux releases are documented. Windows support is not established; Linux defaults to the C++ interface.

### License, model weights & costs

The complete top-level MIT software license was reviewed and archived. Dependent models and components retain their own terms. [Source 1](https://github.com/rodrigodzf/NeuralResonatorVST/blob/main/LICENSE) [Source 2](https://github.com/rodrigodzf/NeuralResonatorVST/blob/main/README.md)

- **Code:** MIT
- **Weights:** MIT project code. JUCE, LibTorch, borrowed UI/network code and model assets retain separate terms requiring attention for redistribution.
- **Commercial:** The reviewed software license permits commercial software use subject to its obligations; it does not clear independent weights, data, assets, services or dependencies.
- **Cost:** Source code is available under the stated license. Compute, storage, optional hardware and any hosted model/API services can add costs; no current service-price quote is asserted.

### Why it merits attention

Included for its concrete documented creative workflow: Exploring imagined objects and sculptural timbres by exciting a modelled resonator with MIDI impulses or incoming audio. The documentation and developer examples support relevance; output quality, setup success and performance were not independently tested. [Source 1](https://github.com/rodrigodzf/NeuralResonatorVST/blob/main/README.md)

### Limitations

This is an experimental neural-filter instrument, not a measurement of a real physical object. Audio stability, compatibility and sound quality were not tested. [Source 1](https://github.com/rodrigodzf/NeuralResonatorVST/blob/main/README.md)

### Get the tool

- [Repository](https://github.com/rodrigodzf/NeuralResonatorVST)
- [Documentation](https://github.com/rodrigodzf/NeuralResonatorVST/blob/main/README.md)
- [License](https://github.com/rodrigodzf/NeuralResonatorVST/blob/main/LICENSE)

## NeLF-Pro

Neural holography and light-field media · 3D, reconstruction & assets · Photogrammetry, scanning & neural rendering · Spatial audio & volumetric media

First detailed library baseline. Documentation and complete software license checked on 2026-10-07; no claim of a new release today.

### How it uses AI

Learned probe factors estimate scene density/radiance for neural view synthesis. [Source](https://github.com/sinoyou/nelf-pro/blob/main/README.md) [Source](https://sinoyou.github.io/nelf-pro/)

### Introduction

A CVPR 2024 research implementation representing scenes with learnable local light-field probes. [Source 1](https://github.com/sinoyou/nelf-pro/blob/main/README.md) [Source 2](https://sinoyou.github.io/nelf-pro/)

### What it is good for

Reconstructing captured scenes, exploring novel views and rendering camera paths at multiple scene scales. [Source 1](https://github.com/sinoyou/nelf-pro/blob/main/README.md) [Source 2](https://sinoyou.github.io/nelf-pro/)

### Demo & examples

The official project page shows small- and large-scene render comparisons and a video. [Source 1](https://sinoyou.github.io/nelf-pro/)

### Install

Documented setup guidance; these commands were not executed during this review. [Source 1](https://github.com/sinoyou/nelf-pro/blob/main/README.md) [Source 2](https://sinoyou.github.io/nelf-pro/)

1. Create an isolated environment; the guide recommends Python 3.8 and a CUDA 11.3/PyTorch 1.12.1 stack.
2. Install the simplified SDFStudio-derived source package.
3. Prepare a documented dataset and set its path in a complete YAML configuration.

```sh
pip install -e .
```


```sh
ns-train nelf-pro-small --trainer.load-config ./conf/small/free.yaml
```

### First project

Begin with a small example and inspect the result before using it in production. [Source 1](https://github.com/sinoyou/nelf-pro/blob/main/README.md) [Source 2](https://sinoyou.github.io/nelf-pro/)

1. Start with the documented stair scene.
2. Point the YAML at the resulting checkpoint, inspect the viewer and export a camera-path render or depth-derived point cloud.
### Hardware & software

Source-backed requirements; unreported minimums remain unknown. [Source 1](https://github.com/sinoyou/nelf-pro/blob/main/README.md) [Source 2](https://sinoyou.github.io/nelf-pro/)

- **Hardware:** CUDA is required by the documented setup. Minimum RAM/VRAM and storage are not specified; scene scale and dataset size affect needs.
- **Software:** Python >=3.7, recommended 3.8; tested CUDA 11.3, torch 1.12.1+cu113 and torchvision 0.13.1+cu113. This is an older research dependency stack.
- **Platforms:** CUDA-oriented research setup; a complete native Windows/macOS/Linux support matrix is not given.

### License, model weights & costs

The complete top-level Apache-2.0 software license was reviewed and archived. Dependent models and components retain their own terms. [Source 1](https://github.com/sinoyou/nelf-pro/blob/main/LICENSE) [Source 2](https://github.com/sinoyou/nelf-pro/blob/main/README.md) [Source 3](https://sinoyou.github.io/nelf-pro/)

- **Code:** Apache-2.0
- **Weights:** Apache-2.0 source; scene datasets, photographs and inherited framework components have their own terms.
- **Commercial:** The reviewed software license permits commercial software use subject to its obligations; it does not clear independent weights, data, assets, services or dependencies.
- **Cost:** Source code is available under the stated license. Compute, storage, optional hardware and any hosted model/API services can add costs; no current service-price quote is asserted.

### Why it merits attention

Included for its concrete documented creative workflow: Reconstructing captured scenes, exploring novel views and rendering camera paths at multiple scene scales. The documentation and developer examples support relevance; output quality, setup success and performance were not independently tested. [Source 1](https://github.com/sinoyou/nelf-pro/blob/main/README.md) [Source 2](https://sinoyou.github.io/nelf-pro/)

### Limitations

Use complete YAML configurations: mixed CLI overrides can be overwritten by the YAML. This framework version starts its viewer through training rather than a standalone viewer command; reconstruction quality was not tested. [Source 1](https://github.com/sinoyou/nelf-pro/blob/main/README.md) [Source 2](https://sinoyou.github.io/nelf-pro/)

### Get the tool

- [Repository](https://github.com/sinoyou/nelf-pro)
- [Documentation](https://sinoyou.github.io/nelf-pro/)
- [License](https://github.com/sinoyou/nelf-pro/blob/main/LICENSE)

## SIGNET

Neural holography and light-field media · Computational art & creative coding · Spatial audio & volumetric media

First detailed library baseline. Documentation and complete software license checked on 2026-10-07; no claim of a new release today.

### How it uses AI

A neural network with Gegenbauer embedding encodes and decodes views from a light field. [Source](https://github.com/AugmentariumLab/SIGNET/blob/main/README.md)

### Introduction

An ICCV 2021 demonstration of compact neural representations for light-field views. [Source 1](https://github.com/AugmentariumLab/SIGNET/blob/main/README.md)

### What it is good for

Studying viewpoint-indexed image decoding and light-field representation for spatial-media experiments. [Source 1](https://github.com/AugmentariumLab/SIGNET/blob/main/README.md)

### Demo & examples

The repository supplies pretrained lego and tarot scenes and links the research project. [Source 1](https://github.com/AugmentariumLab/SIGNET/blob/main/README.md)

### Install

Documented setup guidance; these commands were not executed during this review. [Source 1](https://github.com/AugmentariumLab/SIGNET/blob/main/README.md)

1. Clone the source and prepare CUDA, PyTorch, NumPy and PIL.
2. Use the provided encoded scene weights.
3. Run the demo decoder for an allowed view coordinate.

```sh
python demo_decode.py -u 8 -v 8 --scene lego
```

### First project

Begin with a small example and inspect the result before using it in production. [Source 1](https://github.com/AugmentariumLab/SIGNET/blob/main/README.md)

1. Decode several views with integer u/v coordinates between 0 and 16.
2. Compare the image changes and review the paper before adapting the representation to a different dataset.
### Hardware & software

Source-backed requirements; unreported minimums remain unknown. [Source 1](https://github.com/AugmentariumLab/SIGNET/blob/main/README.md)

- **Hardware:** CUDA is required by the listed environment. Minimum RAM, VRAM and storage are not documented.
- **Software:** Python with PyTorch, NumPy and PIL; exact supported versions are not specified in the short guide.
- **Platforms:** No validated OS-by-OS matrix is published in the inspected README.

### License, model weights & costs

The complete top-level MIT software license was reviewed and archived. Dependent models and components retain their own terms. [Source 1](https://github.com/AugmentariumLab/SIGNET/blob/main/LICENSE) [Source 2](https://github.com/AugmentariumLab/SIGNET/blob/main/README.md)

- **Code:** MIT
- **Weights:** MIT code. The included scene weights/data do not have a separately verified blanket grant in this review; check source-data terms before reuse.
- **Commercial:** The reviewed software license permits commercial software use subject to its obligations; it does not clear independent weights, data, assets, services or dependencies.
- **Cost:** Source code is available under the stated license. Compute, storage, optional hardware and any hosted model/API services can add costs; no current service-price quote is asserted.

### Why it merits attention

Included for its concrete documented creative workflow: Studying viewpoint-indexed image decoding and light-field representation for spatial-media experiments. The documentation and developer examples support relevance; output quality, setup success and performance were not independently tested. [Source 1](https://github.com/AugmentariumLab/SIGNET/blob/main/README.md)

### Limitations

A small research decoder demonstration, not a complete capture or display application. It does not demonstrate arbitrary-scene training or real-time headset playback. [Source 1](https://github.com/AugmentariumLab/SIGNET/blob/main/README.md)

### Get the tool

- [Repository](https://github.com/AugmentariumLab/SIGNET)
- [Documentation](https://github.com/AugmentariumLab/SIGNET/blob/main/README.md)
- [License](https://github.com/AugmentariumLab/SIGNET/blob/main/LICENSE)

## Neural 3D Holography

Neural holography and light-field media · WebXR, VR & AR · Computational art & creative coding · Physical, robotic & kinetic installations

First detailed library baseline. Documentation and complete software license checked on 2026-10-07; no claim of a new release today.

### How it uses AI

Camera-supervised neural propagation models reduce mismatch between simulated optics and a physical display. [Source](https://github.com/computational-imaging/neural-3d-holography/blob/main/README.md) [Source](https://www.computationalimaging.org/publications/neuralholography3d/)

### Introduction

A SIGGRAPH Asia 2021 implementation of learned wave propagation for holographic AR/VR display research. [Source 1](https://github.com/computational-imaging/neural-3d-holography/blob/main/README.md) [Source 2](https://www.computationalimaging.org/publications/neuralholography3d/)

### What it is good for

Generating SLM phase patterns from RGB/RGB-D targets and calibrating multi-plane holographic displays. [Source 1](https://github.com/computational-imaging/neural-3d-holography/blob/main/README.md) [Source 2](https://www.computationalimaging.org/publications/neuralholography3d/)

### Demo & examples

The official project presents video, AR/VR prototype results and research comparisons. [Source 1](https://www.computationalimaging.org/publications/neuralholography3d/)

### Install

Documented setup guidance; these commands were not executed during this review. [Source 1](https://github.com/computational-imaging/neural-3d-holography/blob/main/README.md) [Source 2](https://www.computationalimaging.org/publications/neuralholography3d/)

1. Clone the project and create its neural3d Conda environment.
2. For physical work, install compatible camera/SLM SDKs and adjust optical parameters to the real setup.
3. Begin with the supplied simulation/phase-generation example before camera-in-the-loop calibration.

```sh
conda env create -f env.yml
```


```sh
conda activate neural3d
```


```sh
python main.py --data_path=./data/test --out_path=./results_first --channel=1 --target=rgbd --loss_func=l2 --lr=0.01 --num_iters=1000
```

### First project

Begin with a small example and inspect the result before using it in production. [Source 1](https://github.com/computational-imaging/neural-3d-holography/blob/main/README.md) [Source 2](https://www.computationalimaging.org/publications/neuralholography3d/)

1. Inspect the generated phase and simulated reconstruction.
2. If using physical equipment, follow per-plane homography calibration and training instructions; repeat with the actual optical parameters.
### Hardware & software

Source-backed requirements; unreported minimums remain unknown. [Source 1](https://github.com/computational-imaging/neural-3d-holography/blob/main/README.md) [Source 2](https://www.computationalimaging.org/publications/neuralholography3d/)

- **Hardware:** Physical work needs an SLM, camera and optical illumination system. Numeric RAM/VRAM minima are not documented; optional released training datasets are approximately 60 GB or 220 GB.
- **Software:** PyTorch >=1.10 with complex operations, PyTorch Lightning and env.yml dependencies. PyCapture2 and HOLOEYE SDK or slmPy are documented hardware routes.
- **Platforms:** Research Python/optics workflow; a complete desktop-OS support matrix is not stated. Not a plug-in for ordinary consumer headsets.

### License, model weights & costs

The complete top-level MIT software license was reviewed and archived. Dependent models and components retain their own terms. [Source 1](https://github.com/computational-imaging/neural-3d-holography/blob/main/LICENSE) [Source 2](https://github.com/computational-imaging/neural-3d-holography/blob/main/README.md) [Source 3](https://www.computationalimaging.org/publications/neuralholography3d/)

- **Code:** MIT
- **Weights:** MIT source for this 3D implementation. Vendor SDKs, datasets and trained assets have independent terms; the older 2020 Neural Holography repository has different licensing.
- **Commercial:** The reviewed software license permits commercial software use subject to its obligations; it does not clear independent weights, data, assets, services or dependencies.
- **Cost:** Source code is available under the stated license. Compute, storage, optional hardware and any hosted model/API services can add costs; no current service-price quote is asserted.

### Why it merits attention

Included for its concrete documented creative workflow: Generating SLM phase patterns from RGB/RGB-D targets and calibrating multi-plane holographic displays. The documentation and developer examples support relevance; output quality, setup success and performance were not independently tested. [Source 1](https://github.com/computational-imaging/neural-3d-holography/blob/main/README.md) [Source 2](https://www.computationalimaging.org/publications/neuralholography3d/)

### Limitations

Specialist calibration is central to reproduction. Project comparisons are author experiments, and the site notes limits in its DPAC comparison. No optical apparatus was installed or tested. [Source 1](https://github.com/computational-imaging/neural-3d-holography/blob/main/README.md) [Source 2](https://www.computationalimaging.org/publications/neuralholography3d/)

### Get the tool

- [Repository](https://github.com/computational-imaging/neural-3d-holography)
- [Documentation](https://www.computationalimaging.org/publications/neuralholography3d/)
- [License](https://github.com/computational-imaging/neural-3d-holography/blob/main/LICENSE)

## Additional open-source AI discoveries

Creative AI relevance and software license screened. Full installation, requirements and quality profiles are pending.

### Unique3D · MIT

Creating an initial 3D asset from one image.
Diffusion-based multiview generation and reconstruction predict geometry/appearance from a visual reference.
Detailed setup/quality review pending. Ubuntu/CUDA is the primary route with community Windows options; unseen geometry and print readiness are unverified. Model/component terms are separate. Documentation screened; not installed or tested.

- [Official README](https://github.com/AiuniAI/Unique3D/blob/main/README.md)
- [Reviewed complete software license](https://github.com/AiuniAI/Unique3D/blob/main/LICENSE)
### Linly-Talker · MIT

Prototyping a talking digital character with speech input and a generated response.
Combines ASR, language models, voice generation and neural talking-head components.
Full installation/hardware review pending. Component licenses vary, including potentially restricted avatar models and optional paid services; the top-level software license does not clear the entire stack. Documentation screened; not installed or tested.

- [Official README](https://github.com/Kedreamix/Linly-Talker/blob/main/README.md)
- [Reviewed complete software license](https://github.com/Kedreamix/Linly-Talker/blob/main/LICENSE)
### MAGI-1 · Apache-2.0

Experimenting with chunked video generation and temporal control.
An autoregressive diffusion model generates video in successive chunks.
Detailed guide pending. The documented 4.5B and 24B routes have very different GPU needs; model terms and practical quality require separate review. Documentation screened; not installed or tested.

- [Official README](https://github.com/SandAI-org/MAGI-1/blob/main/README.md)
- [Reviewed complete software license](https://github.com/SandAI-org/MAGI-1/blob/main/LICENSE)
### OmniGen · MIT

Generating or editing images from mixed text and image instructions.
A multimodal generative model uses visual references and language conditioning in one pipeline.
Full model-license, GPU, platform and workflow review pending; attractive examples are developer results. Documentation screened; not installed or tested.

- [Official README](https://github.com/VectorSpaceLab/OmniGen/blob/main/README.md)
- [Reviewed complete software license](https://github.com/VectorSpaceLab/OmniGen/blob/main/LICENSE)
### Video Shotcraft · Apache-2.0

Building cinematic product-video drafts from shot recipes and editable scene code.
An external creative agent develops storyboard and shot instructions that drive a Remotion-based video workflow.
Full setup review pending. Apache source is separate from Remotion team/commercial terms, agent services and audio/media asset rights. Documentation screened; not installed or tested.

- [Official README](https://github.com/Vincentwei1021/video-shotcraft/blob/main/README.md)
- [Reviewed complete software license](https://github.com/Vincentwei1021/video-shotcraft/blob/main/LICENSE)
### VACE · Apache-2.0

Controlled video generation and editing with varied visual conditions.
A learned video-creation/editing framework conditions generation on inputs such as masks and source video.
Detailed model/hardware review pending. Wan and LTX model families have different terms; LTX 0.9 RAIL-M should not be treated as the same license as Apache code. Documentation screened; not installed or tested.

- [Official README](https://github.com/ali-vilab/VACE/blob/main/README.md)
- [Reviewed complete software license](https://github.com/ali-vilab/VACE/blob/main/LICENSE.txt)
### EchoMimicV2 · Apache-2.0

Creating audio-driven half-body character performances.
Neural animation combines audio and pose conditioning to synthesize expressive human motion/video.
Full installation, checkpoint-license and hardware review pending. Published A100 speed measurements are author results and do not predict a consumer machine. Documentation screened; not installed or tested.

- [Official README](https://github.com/antgroup/echomimic_v2/blob/main/README.md)
- [Reviewed complete software license](https://github.com/antgroup/echomimic_v2/blob/main/LICENSE)
### Higgs Audio v2/v2.5 source · Apache-2.0

Exploring expressive narration and multi-speaker audio generation from the retained v2-family implementation.
The archived v2 guide describes an audio foundation model for speech, prosody and voice-conditioned generation.
Legacy implementation: v3 no longer uses this repository and has separate research/non-commercial terms. The v2 source is Apache-2.0, but each checkpoint license, setup and hardware requirement still needs a full review; this entry is not an endorsement of v3. Documentation screened; not installed or tested.

- [Official README](https://github.com/boson-ai/higgs-audio/blob/main/README.md)
- [Reviewed complete software license](https://github.com/boson-ai/higgs-audio/blob/main/LICENSE)
- [README_V2.md](https://github.com/boson-ai/higgs-audio/blob/main/README_V2.md)
### MapAnything · Apache-2.0

Reconstructing scene geometry from images with optional geometric inputs.
A learned transformer estimates multiview geometry, with image/pose/depth-conditioned workflows.
Full practical guide pending. Default weights use CC-BY-NC-4.0; facebook/map-anything-apache is the separately documented Apache-2.0 alternative. Code licensing alone does not choose the checkpoint. Documentation screened; not installed or tested.

- [Official README](https://github.com/facebookresearch/map-anything/blob/main/README.md)
- [Reviewed complete software license](https://github.com/facebookresearch/map-anything/blob/main/LICENSE)
### Champ · MIT

Animating a reference character with 3D human-motion guidance.
A diffusion animation pipeline uses SMPL-style geometric conditioning to control generated motion.
Detailed setup/license review pending. The default 250-frame example documents about 20 GB VRAM; SMPL and pretrained model terms remain separate from the code. Documentation screened; not installed or tested.

- [Official README](https://github.com/fudan-generative-vision/champ/blob/master/README.md)
- [Reviewed complete software license](https://github.com/fudan-generative-vision/champ/blob/master/LICENSE)
### Deep-Live-Cam · AGPL-3.0

Exploring authorized face-replacement character effects in live or recorded video.
Neural face analysis and swapping models synthesize a replacement face within a video pipeline.
AGPL source verified; InsightFace weights are restricted to non-commercial research in the documented route. Paid prebuilt offerings, model permissions, platform requirements and output quality need separate review. Documentation screened; not installed or tested.

- [Official README](https://github.com/hacksider/Deep-Live-Cam/blob/main/README.md)
- [Reviewed complete software license](https://github.com/hacksider/Deep-Live-Cam/blob/main/LICENSE)
### FastVideo · Apache-2.0

Developing faster video-model inference and post-training pipelines.
Implements learned video-model training/distillation and optimized inference paths, including documented GPU and MLX routes.
Developer framework rather than a universal creator app. Full backend/platform setup, weight licensing and performance reproduction are pending. Documentation screened; not installed or tested.

- [Official README](https://github.com/hao-ai-lab/FastVideo/blob/main/README.md)
- [Reviewed complete software license](https://github.com/hao-ai-lab/FastVideo/blob/main/LICENSE)
### OfficeCLI · Apache-2.0

Authoring editable presentation/document content with an AI agent and visual feedback.
An external language model invokes document tools and uses rendered previews to iteratively revise Office content.
The document engine is deterministic and requires an external agent for AI authoring. Full runtime, renderer, font and model-service review remains pending. Documentation screened; not installed or tested.

- [Official README](https://github.com/iOfficeAI/OfficeCLI/blob/main/README.md)
- [Reviewed complete software license](https://github.com/iOfficeAI/OfficeCLI/blob/main/LICENSE)
### VidBee · MIT

Indexing and searching a personal media collection through transcripts and AI-assisted analysis.
Local ASR generates searchable text; configured models can summarize or query transcripts, with local endpoint options.
Full installation/platform review pending. AI functions are distinct from the downloader; provider configuration determines privacy and costs, and media permissions remain separate. Documentation screened; not installed or tested.

- [Official README](https://github.com/nexmoe/VidBee/blob/main/README.md)
- [Reviewed complete software license](https://github.com/nexmoe/VidBee/blob/main/LICENSE)
### Guizang PPT · AGPL-3.0

Creating AI-authored HTML presentations with presenter and rehearsal views.
An external agent generates slide structure, content and visual code through the supplied authoring workflow.
AGPL source verified; model services, optional image-generation APIs, fonts and source material have independent terms. Full setup/output review pending. Documentation screened; not installed or tested.

- [Official README](https://github.com/op7418/guizang-ppt-skill/blob/main/README.md)
- [Reviewed complete software license](https://github.com/op7418/guizang-ppt-skill/blob/main/LICENSE)
### Palmier Pro published source · GPL-3.0

Studying an AI-assisted native Mac video editor and its agent-control workflow.
The documented MCP/agent interface exposes editing operations for model-directed media assembly.
This entry covers the GPL-published source only. Distributed binaries after v0.7.6 are proprietary; the latest download must not be described as GPL. Source build, dependency licenses and hardware review remain pending. Documentation screened; not installed or tested.

- [Official README](https://github.com/palmier-io/palmier-pro/blob/main/README.md)
- [Reviewed complete software license](https://github.com/palmier-io/palmier-pro/blob/main/LICENSE)
### PPTist · AGPL-3.0

Building editable slide experiences with optional AI drafting and rewriting.
The web editor integrates model-assisted slide/content generation around its structured presentation data.
AGPL source verified. AI provider/backend configuration is separate; this is not a turnkey free hosted AI service. Full setup, privacy and export-fidelity review pending. Documentation screened; not installed or tested.

- [Official README](https://github.com/pipipi-pikachu/PPTist/blob/master/README.md)
- [Reviewed complete software license](https://github.com/pipipi-pikachu/PPTist/blob/master/LICENSE)
### TTS WebUI · MIT

Comparing speech, voice-conversion and music-generation models from one interface.
Integrates multiple neural speech/audio-generation backends and their controls.
MIT interface source does not clear all included model families. Detailed installation, memory, checkpoint restrictions and output quality remain pending. Documentation screened; not installed or tested.

- [Official README](https://github.com/rsxdalv/TTS-WebUI/blob/main/README.md)
- [Reviewed complete software license](https://github.com/rsxdalv/TTS-WebUI/blob/main/LICENSE)
### TurboDiffusion · Apache-2.0

Researching accelerated diffusion-video generation.
Attention and distillation techniques reduce sampling cost in compatible video-model pipelines.
Apache source verified; full model/dependency-license and GPU setup review pending. RTX 5090 demonstrations are author measurements, not a universal speed promise. Documentation screened; not installed or tested.

- [Official README](https://github.com/thu-ml/TurboDiffusion/blob/main/README.md)
- [Reviewed complete software license](https://github.com/thu-ml/TurboDiffusion/blob/main/LICENSE)
### Timbro · MIT

Exploring a compact neural-amplifier effect for guitar or other sound-design inputs.
WaveNet/LSTM-style learned amplifier profiles can be blended through the plug-in controls.
MIT source reviewed. Model, JUCE and distribution terms need a full dependency review; documented VST3/AU/standalone routes across desktop platforms have not been tested. Documentation screened; not installed or tested.

- [Official README](https://github.com/tondo-audio/timbro/blob/main/README.md)
- [Reviewed complete software license](https://github.com/tondo-audio/timbro/blob/main/LICENSE)
### ArtLine · MIT

Converting photographs into line-art references.
A FastAI-based learned image-translation model predicts a stylized line rendering.
MIT source verified; legacy dependencies, weights/training-material rights and platform setup require detailed review. Output is raster line art, not automatically editable vector geometry. Documentation screened; not installed or tested.

- [Official README](https://github.com/vijishmadhavan/ArtLine/blob/main/README.md)
- [Reviewed complete software license](https://github.com/vijishmadhavan/ArtLine/blob/main/LICENSE)
### AI Video Transcriber · Apache-2.0

Preparing transcripts, summaries and translations from long-form media.
Speech recognition and language-model processing convert audio/video into structured text.
Apache source verified. Local-versus-cloud dependencies, provider data handling, language accuracy and hardware requirements remain pending; do not assume all processing stays local. Documentation screened; not installed or tested.

- [Official README](https://github.com/wendy7756/AI-Video-Transcriber/blob/main/README.md)
- [Reviewed complete software license](https://github.com/wendy7756/AI-Video-Transcriber/blob/main/LICENSE)
### Fireworks Tech Graph · MIT

Drafting technical diagrams with SVG and animated/web export options.
An external AI agent authors semantic diagram specifications and uses generator/validation tools to refine the visual output.
MIT source verified; the renderer is deterministic and AI assistance requires an external agent. Full setup, fonts/assets, model terms and diagram correctness remain pending. Documentation screened; not installed or tested.

- [Official README](https://github.com/yizhiyanhua-ai/fireworks-tech-graph/blob/main/README.md)
- [Reviewed complete software license](https://github.com/yizhiyanhua-ai/fireworks-tech-graph/blob/main/LICENSE)
### AutoMovie · MIT

Producing code-authored scenes, camera motion and deterministic film renders.
An external coding agent authors scripts, typed scene contracts and TypeScript performances; the engine validates and renders them without an internal language model.
MIT source reviewed. Node 22+/pnpm 10 development route and external-agent dependence are documented; full production/render setup and output review remain pending. Documentation screened; not installed or tested.

- [Official README](https://github.com/samchon/automovie/blob/master/README.md)
- [Reviewed complete software license](https://github.com/samchon/automovie/blob/master/LICENSE)
### CAYADEV Visualizer source · MIT

Building audio-reactive visual scenes and controlling a VJ/show setup through an AI agent.
A local MCP interface gives an external model scene/output controls; the visual and audio-analysis engines themselves are conventional.
MIT source reviewed. MCP controls are marked for 3.1.5 on main and are not in the current 3.1.4 binary release. Full native integration, dependency licensing and live-performance review remain pending. Documentation screened; not installed or tested.

- [Official README](https://github.com/CaYatur/SoundVisualizer/blob/main/README.md)
- [Reviewed complete software license](https://github.com/CaYatur/SoundVisualizer/blob/main/LICENSE)
### Geomotion · MIT

Creating editable hand-drawn-style morphing animations and exporting SVG, Lottie or HTML.
An external agent writes structured animation specifications and uses MCP validation/render tools; animation interpolation is deterministic.
MIT source reviewed. Full setup, format fidelity, embedding compatibility and external-agent/provider review remain pending; a renderer does not itself contain a generative model. Documentation screened; not installed or tested.

- [Official README](https://github.com/hacimertgokhan/geomotion/blob/main/README.md)
- [Reviewed complete software license](https://github.com/hacimertgokhan/geomotion/blob/main/LICENSE)
### Phosmith · AGPL-3.0

Exploring browser photo editing with AI selection/masking and optional agent-driven edits.
SlimSAM/CLIPSeg browser inference supports learned selections; optional local services and a Gemini agent handle other editing tasks.
AGPL source reviewed. Documentation mixes browser-local, local-server and hosted-provider paths; actual privacy/backend requirements must be resolved per feature. Full installation and output review pending. Documentation screened; not installed or tested.

- [Official README](https://github.com/ArAnirudh2901/Phosmith/blob/main/README.md)
- [Reviewed complete software license](https://github.com/ArAnirudh2901/Phosmith/blob/main/LICENSE)
### PINN-shaper · MPL-2.0

Designing shaped light patterns for spatial-light-modulator or flat-optics experiments.
Physics-informed neural networks solve a beam-shaping PDE to generate phase profiles for target intensity patterns.
Complete MPL-2.0 software license reviewed. PyTorch/diffractsim notebooks are research code; hardware calibration, model/data terms and optical output validation remain pending. Documentation screened; not installed or tested.

- [Official README](https://github.com/rafael-fuente/pinn-shaper/blob/main/README.md)
- [Reviewed complete software license](https://github.com/rafael-fuente/pinn-shaper/blob/main/LICENSE)

## Excluded and unresolved findings

Research notes only; these do not enter the eligible tool library.

- **Raveler** · excluded: Neural timbre plug-in for Wwise, but its software license is CC-BY-NC-4.0. Excluded from open-source software eligibility; Wwise is also a separate proprietary host. [Source](https://github.com/usdivad/Raveler)
- **Neural Holography (original implementation)** · excluded: The inspected software license limits use to academic/non-commercial purposes. This is separate from the MIT-licensed time-multiplexed implementation featured today. [Source](https://github.com/computational-imaging/neural-holography)
- **8.75mm AI-assisted film-restoration workflow** · excluded: The repository uses CC-BY-NC-ND-4.0, so it does not qualify as open-source software. [Source](https://github.com/hw4090-create/8.75mm-AI-Assisted-Film-Restoration-Workflow)
- **LingBot-World v2** · excluded: The newer implementation uses CC-BY-NC-SA-4.0 software terms. The earlier Apache repository says it is no longer maintained; neither is promoted as a new unrestricted application. [Source](https://github.com/Robbyant/lingbot-world-v2)
- **GarmentDiffusion** · needs-license-review: Potential creative garment workflow, but no complete software license was available in the inspected repository. [Source](https://github.com/Shenfu-Research/GarmentDiffusion)
- **Garment-GPT** · needs-license-review: Relevant garment research, but the inspected repository did not establish a complete software license. [Source](https://github.com/ChimerAI-MMLab/Garment-GPT)
- **Custom machine learning for film restoration** · needs-license-review: No complete software license was found; the examples also depend on proprietary NukeX CopyCat. [Source](https://github.com/fabiocolor/custom-machine-learning-for-film-restoration)
- **Text2TactileGraphics** · needs-license-review: The primary project demonstrates tactile graphics, but the inspected code lacked a verified complete software license. A physical-output demo does not establish print readiness. [Source](https://github.com/alex4727/Text2TactileGraphics)

Source collection completed: 2026-10-07T12:33:57.253397+00:00
Search is a bounded sample. Stars and recent pushes are discovery signals, not verified quality or meaningful upgrades.
