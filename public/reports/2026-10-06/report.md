# AI Media Scout — 2026-10-06

Today adds 33 complete guides and 45 additional screened discoveries across 40 creative fields, including architecture, physical drawing, haptics, music notation and neural scene capture. Eighteen earlier pending entries now have practical guides; these are first detailed baselines, not claims that the tools launched today. All 262 repository queries and 15 model-task queries completed; 97 repository searches were bounded and two web ecosystems could not be accessed. Model-task results are also bounded samples of up to 50 per task. The search is broad but not exhaustive. Every published entry has a reviewed complete open-source software license; model, dataset and service restrictions are reported separately. Hardware advice covers documented options across platforms, and no discovered app was installed or tested.

Documentation reviewed today. Tools are not hands-on tested unless explicitly stated. Requirements and performance remain source-specific.

## Coverage

| Field | Finding |
| --- | --- |
| Images & design | Image editing and local inference remain productive areas: FireRed Image Edit, Turbo MLX and ImageGen Mac receive guides. Model terms differ substantially; open application code does not make every weight commercially usable. [Source 1](https://huggingface.co/FireRedTeam/FireRed-Image-Edit-1.1) [Source 2](https://github.com/rinste/turbo-mlx) |
| Video, animation & film | JoyAI Video Edit and AnimateDiff now have practical guides; additional video models remain screened leads. The high-end GPU demonstration for live editing is reported as an author result, not a universal real-time promise. [Source 1](https://huggingface.co/spaces/wxDai/joyai-video-edit) [Source 2](https://animatediff.github.io/) |
| Audio, music & voice | YuE2 Turbo, OpenSpatial and symbolic-music tooling broaden this edition beyond speech generation. The primary YuE2 project documents its music research; the server profile separately flags non-commercial weights. [Source 1](https://map-yue2.github.io/) [Source 2](https://github.com/noizai/YuE2-Turbo) |
| 3D, reconstruction & assets | New guides cover image-to-mesh generation, Gaussian training/editing and indoor scene composition. Primary demos provide examples, while printability and mesh quality remain unverified. [Source 1](https://ldyang694.github.io/projects/pixal3d/) [Source 2](https://chenguolin.github.io/projects/InstructScene/) |
| Browser tools & web media | Browser AI and agent-authored visual tools were checked alongside local applications. WebGPU documentation helps distinguish browser inference support from a web frontend that depends on a separate GPU server. [Source 1](https://huggingface.co/docs/transformers.js/guides/webgpu) [Source 2](https://superspl.at/editor) |
| WebXR, VR & AR | Research on AI-assisted XR interaction and neural scene assets was reviewed. LDraw Nova documents Quest 3 viewing, while the unlicensed Abra candidate is held outside the eligible library. [Source 1](https://edwardlu2018.github.io/assets/pubs/genassist_ieeevr_26.pdf) [Source 2](https://github.com/anteloc/ldraw-nova) |
| Computational art & creative coding | Creative coding, symbolic music and neural scene optimization all remain in scope. ml5.js documentation was checked for accessible browser-based learning workflows; unchanged known tools are not repeated as new profiles. [Source 1](https://ml5js.org/) [Source 2](https://miditok.readthedocs.io/en/latest/) |
| Interactive, immersive & live media | Interactive AI includes scene-editing agents, vision/voice installations and tactile signals. Browser-learning documentation and the Haptic Neural Fields project supplement repository discovery. [Source 1](https://ml5js.org/) [Source 2](https://mmlab-cv.github.io/HapticNeuralFields/) |
| 3D printing & generative CAD | PartCAD, MCP build123d and Line-us MCP connect AI authoring to parametric or physical output; LDraw Nova adds brick-model workflows. An export or collision check does not establish a safe physical build. [Source 1](https://partcad.readthedocs.io/en/latest/) [Source 2](https://www.ldraw.org/docs-main.html) |
| Games & production pipelines | Godot reinforcement-learning agents and AI-assisted mesh editing extend game coverage beyond image assets. Official research and editor documentation were reviewed; runtime integration still needs project-specific testing. [Source 1](https://arxiv.org/abs/2112.03636) [Source 2](https://editor.qtmesh.dev/docs.html) |
| Motion capture & character animation | AnimateDiff and FloodDiffusion2 now have guides; pose control and kinematic generation also appear as screened discoveries. Dance research project sites were checked to extend the search beyond video diffusion alone. [Source 1](https://animatediff.github.io/) [Source 2](https://faustrazor.github.io/) |
| Avatars, digital humans & lip sync | PuppetStudio adds a documented route from illustrations and recordings to speaking clips. Its Windows-first neural-rendering path and public-alpha limits are explicit; image-animation research provides adjacent techniques. [Source 1](https://github.com/Well-Noted/PuppetStudio) [Source 2](https://animatediff.github.io/) |
| VFX, compositing & relighting | Marigold provides depth, normals and intrinsic-image estimates; 3DGRUT explores neural scene rendering. Relighting project sites were researched without treating every paper demo as verified reusable software. [Source 1](https://marigoldcomputervision.github.io/) [Source 2](https://nrhints.github.io/) |
| Spatial audio & volumetric media | Spatial media includes Gaussian scenes and headphone audio. OpenSpatial is profiled, neural HRTF projects are retained as leads, and primary acoustic-field research was checked for adjacent workflows. [Source 1](https://www.cs.unc.edu/~cpk/data/papers/Neural_acoustic_fields.pdf) [Source 2](https://research.nvidia.com/labs/toronto-ai/3DGRT) |
| Photogrammetry, scanning & neural rendering | Brush, 4D Gaussians and 3DGRUT cover static/dynamic neural capture. Public examples were inspected as developer evidence; they do not validate reconstruction from arbitrary personal footage. [Source 1](https://arthurbrussee.github.io/brush-demo) [Source 2](https://guanjunwu.github.io/4dgs/index.html) |
| Editing, captions & post-production | Editing coverage includes masks/annotation, neural capture cleanup and conversational video assembly. FireRed OpenStoryline provides a primary workflow demo; model/provider and source-media terms stay separate. [Source 1](https://fireredteam.github.io/demos/firered_openstoryline/) [Source 2](https://superspl.at/editor) |
| Vector graphics, illustration & textures | ArchLang adds AI-assisted plan-to-vector authoring; NeuralSVG is a screened generative-vector lead. The NeuralSVG paper and ArchLang playground supplement source-code review. [Source 1](https://arxiv.org/abs/2501.03992) [Source 2](https://playground.archlang.uk) |
| Typography, fonts & layout | Font-generation papers were checked, alongside agent-authored text/layout and SVG workflows. No newly verified standalone font application was promoted solely from a paper or attractive demo. [Source 1](https://arxiv.org/abs/2212.05895) [Source 2](https://arxiv.org/abs/2312.12142) |
| Storyboarding, narrative & comics | Narrated puppet clips, conversational video editing, comic translation and dubbing all support storytelling. Completed guides distinguish local processing from external model calls. [Source 1](https://fireredteam.github.io/demos/firered_openstoryline/) [Source 2](https://github.com/Well-Noted/PuppetStudio) |
| Creative publishing & presentation | AI chart authoring, comics and media-to-text workflows extend publication coverage. Microsoft primary material on AI visualization was reviewed; new Flint Chart and Comic Translate entries remain pending detailed guides. [Source 1](https://www.microsoft.com/en-us/research/blog/data-formulator-a-concept-driven-ai-powered-approach-to-data-visualization/) [Source 2](https://github.com/microsoft/flint-chart) |
| Photography, restoration & color | Image analysis, local edits and semantic collection search were screened. Marigold adds a full guide, while media-library and upscaling applications await practical reviews. [Source 1](https://marigoldcomputervision.github.io/) [Source 2](https://diffusionbee.com) |
| Data art & scientific visualization | Primary AI visualization research was checked, and Flint Chart adds an agent-oriented chart-specification lead. Generated charts still require checking against the source data. [Source 1](https://labs.ai.azure.com/innovations/data-formulator/) [Source 2](https://github.com/microsoft/flint-chart) |
| Physical, robotic & kinetic installations | Live visual generation, vision-aware interaction and tactile output remain within scope. StreamDiffusionV2 and Haptic Neural Fields project sites provide adjacent primary examples; hardware performance remains untested. [Source 1](https://streamdiffusionv2.github.io/) [Source 2](https://mmlab-cv.github.io/HapticNeuralFields/) |
| Performance, projection & stage media | Music-generation servers, audio analysis and motion control were reviewed. The Cypher DJ project page was also checked for live-performance context; a project-page claim alone does not complete license/setup review. [Source 1](https://www.infinimind-creations.com/instruments/cypher-dj/) [Source 2](https://map-yue2.github.io/) |
| Fashion, textiles & wearable media | Virtual try-on and AI textile practice were investigated. OpenTryOn software is excluded for its non-commercial license; textile research without verified released software remains a gap, not an eligible recommendation. [Source 1](https://prompthaus.pl/open-source) [Source 2](https://www.aalto.fi/en/research-art/textile-design-meets-ai) [Source 3](https://github.com/tryonlabs/opentryon) |
| Accessible media & assistive creation | Transcription, score recognition, tactile graphics and haptic media broaden accessibility coverage. The Text2TactileGraphics project was reviewed as a research lead, without asserting complete software licensing or guaranteed print readiness. [Source 1](https://ruihangao.github.io/Text2TactileGraphics/) [Source 2](https://pypi.org/project/oemer/) |
| Mobile, edge & on-device creation | Android speech input and Brush mobile builds were screened. WebGPU primary documentation was checked, but browser access to a desktop service is not labeled on-device inference. [Source 1](https://huggingface.co/docs/transformers.js/guides/webgpu) [Source 2](https://github.com/EdiBianco/OpenWhispr) |
| Creative learning & authoring | Executable neural HRTF tutorials, ml5.js examples and music tokenization support creative learning. Tutorial code is distinguished from finished artist-facing software. [Source 1](https://ml5js.org/) [Source 2](https://miditok.readthedocs.io/en/latest/) |
| Archives, media restoration & collections | Printed score recovery, recorded-speech transcription and collection search were reviewed. Recognition and restoration can introduce errors; outputs should be checked against the original material. [Source 1](https://pypi.org/project/oemer/) [Source 2](https://marigoldcomputervision.github.io/) |
| Emerging & cross-disciplinary creative AI | Emerging directions include architecture, local spatial models, tactile synthesis and new music inference. YuE2 primary research was checked; recently modified repositories and model listings are discovery signals rather than quality proof. [Source 1](https://arxiv.org/abs/2609.33757) [Source 2](https://hapticgen.hcitech.org/) |
| Tactile, vibration and haptic media | Haptic Neural Fields receives a guide. HapticGen and tactile-graphics project pages broadened the search; each released model, dataset and physical device integration needs its own review. [Source 1](https://mmlab-cv.github.io/HapticNeuralFields/) [Source 2](https://hapticgen.hcitech.org/) [Source 3](https://ruihangao.github.io/Text2TactileGraphics/) |
| Neural acoustics and responsive sound spaces | Neural HRTF code and a hands-on tutorial are screened leads, while acoustic-field primary research provides context. No claim is made that inferred acoustics replace measured room or listener validation. [Source 1](https://www.cs.unc.edu/~cpk/data/papers/Neural_acoustic_fields.pdf) [Source 2](https://github.com/yzyouzhang/hrtf_field) |
| AI agents for code-authored media production | Agent workflows now span video editing, architectural plans, CAD and mesh operations. The detailed profiles describe the actual media operation and identify the external model dependence. [Source 1](https://fireredteam.github.io/demos/firered_openstoryline/) [Source 2](https://archlang.uk) |
| AI kinetic typography and animated lettering | Agent-authored HTML animation and visual coding notebooks were screened. Typography-generation research and browser AI documentation were also searched; these do not establish native motion-design-host compatibility. [Source 1](https://arxiv.org/abs/2312.12142) [Source 2](https://huggingface.co/docs/transformers.js/guides/webgpu) [Source 3](https://github.com/nexu-io/html-video) |
| AI choreography and dance composition | CustomDance, Kimodo and pose-guided video broaden motion discovery. DanceCrafter/DanceFusion primary sites were checked; motion generation still needs contact, retargeting and performance review. [Source 1](https://faustrazor.github.io/) [Source 2](https://th-mlab.github.io/DanceFusion/) [Source 3](https://github.com/XulongT/CustomDance) |
| AI-assisted textile and computational craft | AI-assisted CAD, pen plotting and brick assemblies are covered by full guides. AI textile research was checked, but craft-sounding names were not treated as knitting/manufacturing tools without concrete evidence. [Source 1](https://partcad.readthedocs.io/en/latest/) [Source 2](https://www.aalto.fi/en/research-art/textile-design-meets-ai) |
| AI music notation and score recovery | ScanScore, oemer, Polyphonic TrOMR and MidiTok now have detailed entries spanning recognition and model-ready score representation. Package documentation supplements repository sources; recognized notation needs proofreading. [Source 1](https://pypi.org/project/oemer/) [Source 2](https://pypi.org/project/miditok/) |
| Neural relighting and material recovery | Marigold intrinsic-image analysis is profiled; neural relighting project sites were researched for additional directions. No unreviewed model or dependency license was assumed permissive. [Source 1](https://marigoldcomputervision.github.io/) [Source 2](https://neural-gaffer.github.io/) [Source 3](https://near-project.github.io/) |
| Olfactory and multisensory AI media | Image-to-scent narrative research and a prompt-to-fragrance repository were found. No new fully licensed creative application was established: Sniff AI has no verified software license, and the MIT Media Lab project page alone does not grant a software license. [Source 1](https://www.media.mit.edu/projects/anemoia-device/overview/) [Source 2](https://github.com/ksek87/sniff_ai) |
| AI architectural visualization and spatial design | This newly added field produced three guides: Aedifex for editable scenes, ArchLang for structured plans and InstructScene for learned interior layouts. Primary project/playground evidence was reviewed; drawings are not engineering certification. [Source 1](https://archlang.uk) [Source 2](https://chenguolin.github.io/projects/InstructScene/) [Source 3](https://github.com/TangSY/aedifex) |

## Search and review counts

40 creative fields; 262/262 repository queries attempted; 15/15 model-task queries attempted. 20547 distinct source candidates and 711 model leads. 33 detailed profiles and 45 additional screened discoveries. Source gaps: 0 failed repository queries, 0 partial repository queries, 97 bounded repository queries, 0 failed model-task queries and 2 web ecosystem gaps. Raw search candidates include duplicates of known tools, excluded projects and projects awaiting review; they are not verified recommendations.

## Research beyond GitHub

- **gitlab** · searched: Official ComfyUI toolkit tags and a ballroom-motion repository were inspected. These are researched findings; label-only licensing was insufficient to add them as new eligible tools today. [Source](https://gitlab.com/UmeAiRT-Studio/comfyui-umeairt-toolkit/-/tags) [Source](https://gitlab.com/Roxanne_Ardary/motionnet)
- **codeberg** · gap: Live research could not inspect Codeberg content because access was blocked by robots restrictions. This is an access gap, not a claim that no relevant tools exist.
- **sourcehut** · gap: Live research could not inspect SourceHut content because access was blocked by robots restrictions. No unverified SourceHut candidate is promoted.
- **packages** · searched: Official oemer and MidiTok package pages and PartCAD documentation supplement source snapshots, covering score recognition, symbolic-model data and CAD tooling. [Source](https://pypi.org/project/oemer/) [Source](https://pypi.org/project/miditok/) [Source](https://partcad.readthedocs.io/en/latest/)
- **creative-plugins** · searched: Krita AI Diffusion model/setup documentation was checked, and Blender/ComfyUI plugin sources were screened. Host, model and plugin licenses remain separate. [Source](https://docs.interstice.cloud/base-models/) [Source](https://docs.interstice.cloud/common-issues/) [Source](https://github.com/AIGODLIKE/ComfyUI-BlenderAI-node)
- **project-sites** · searched: Primary architecture, neural capture, image analysis, video-editing and tactile project sites/demos were reviewed. Attractive examples alone were not counted as license verification. [Source](https://chenguolin.github.io/projects/InstructScene/) [Source](https://marigoldcomputervision.github.io/) [Source](https://hapticgen.hcitech.org/)
- **research-code** · searched: Primary papers and released repositories were checked across neural SVG, Gaussian reconstruction, dance, haptic and music work. Research prototypes are labeled and model/data limits remain visible. [Source](https://arxiv.org/abs/2501.03992) [Source](https://research.nvidia.com/labs/toronto-ai/3DGRT) [Source](https://mmlab-cv.github.io/HapticNeuralFields/)
- **international** · searched: Chinese and English official documentation was reviewed for FireRed workflows, AutoClip and YouDub, alongside international research projects. Translation of a README does not validate local installation. [Source](https://github.com/FireRedTeam/FireRed-OpenStoryline) [Source](https://github.com/zhouxiaoka/autoclip) [Source](https://github.com/liuzhao1225/YouDub-webui)

## Collection limitations

- images: bounded or incomplete query: topic:diffusion pushed:>=2026-09-06 is:public fork:false archived:false (200 of 206 matches sampled)
- images: bounded or incomplete query: topic:diffusion is:public fork:false archived:false (200 of 1426 matches sampled)
- images: bounded or incomplete query: AI image generation pushed:>=2026-09-06 is:public fork:false archived:false (200 of 1656 matches sampled)
- images: bounded or incomplete query: AI image generation created:>=2026-09-06 is:public fork:false archived:false (200 of 820 matches sampled)
- images: bounded or incomplete query: AI image generation is:public fork:false archived:false (200 of 15380 matches sampled)
- video: bounded or incomplete query: AI video pushed:>=2026-09-06 is:public fork:false archived:false (200 of 12347 matches sampled)
- video: bounded or incomplete query: AI video created:>=2026-09-06 is:public fork:false archived:false (200 of 7788 matches sampled)
- video: bounded or incomplete query: AI video is:public fork:false archived:false (200 of 82936 matches sampled)
- video: bounded or incomplete query: topic:video-generation pushed:>=2026-09-06 is:public fork:false archived:false (200 of 1539 matches sampled)
- video: bounded or incomplete query: topic:video-generation created:>=2026-09-06 is:public fork:false archived:false (200 of 614 matches sampled)
- video: bounded or incomplete query: topic:video-generation is:public fork:false archived:false (200 of 3870 matches sampled)
- audio: bounded or incomplete query: topic:music-generation pushed:>=2026-09-06 is:public fork:false archived:false (200 of 303 matches sampled)
- audio: bounded or incomplete query: topic:music-generation is:public fork:false archived:false (500 of 1185 matches sampled)
- audio: bounded or incomplete query: AI audio pushed:>=2026-09-06 is:public fork:false archived:false (200 of 3774 matches sampled)
- audio: bounded or incomplete query: AI audio created:>=2026-09-06 is:public fork:false archived:false (200 of 2032 matches sampled)
- audio: bounded or incomplete query: AI audio is:public fork:false archived:false (200 of 27653 matches sampled)
- 3d: bounded or incomplete query: 3D generation pushed:>=2026-09-06 is:public fork:false archived:false (200 of 667 matches sampled)
- 3d: bounded or incomplete query: 3D generation created:>=2026-09-06 is:public fork:false archived:false (200 of 344 matches sampled)
- 3d: bounded or incomplete query: 3D generation is:public fork:false archived:false (200 of 5778 matches sampled)
- 3d: bounded or incomplete query: topic:3d-reconstruction pushed:>=2026-09-06 is:public fork:false archived:false (200 of 251 matches sampled)
- 3d: bounded or incomplete query: topic:3d-reconstruction is:public fork:false archived:false (200 of 1904 matches sampled)
- web: bounded or incomplete query: topic:webgpu pushed:>=2026-09-06 is:public fork:false archived:false (200 of 1032 matches sampled)
- web: bounded or incomplete query: topic:webgpu created:>=2026-09-06 is:public fork:false archived:false (200 of 431 matches sampled)
- web: bounded or incomplete query: topic:webgpu is:public fork:false archived:false (200 of 2816 matches sampled)
- xr: bounded or incomplete query: AI VR pushed:>=2026-09-06 is:public fork:false archived:false (200 of 332 matches sampled)
- xr: bounded or incomplete query: AI VR is:public fork:false archived:false (200 of 2854 matches sampled)
- computational: bounded or incomplete query: AI creative coding is:public fork:false archived:false (200 of 914 matches sampled)
- computational: bounded or incomplete query: topic:generative-art pushed:>=2026-09-06 is:public fork:false archived:false (200 of 845 matches sampled)
- computational: bounded or incomplete query: topic:generative-art created:>=2026-09-06 is:public fork:false archived:false (200 of 414 matches sampled)
- computational: bounded or incomplete query: topic:generative-art is:public fork:false archived:false (200 of 3887 matches sampled)
- interactive: bounded or incomplete query: AI interactive art is:public fork:false archived:false (200 of 673 matches sampled)
- fabrication: bounded or incomplete query: AI CAD pushed:>=2026-09-06 is:public fork:false archived:false (200 of 667 matches sampled)
- fabrication: bounded or incomplete query: AI CAD created:>=2026-09-06 is:public fork:false archived:false (200 of 368 matches sampled)
- fabrication: bounded or incomplete query: AI CAD is:public fork:false archived:false (200 of 2990 matches sampled)
- fabrication: bounded or incomplete query: AI 3D printing is:public fork:false archived:false (200 of 342 matches sampled)
- gaming: bounded or incomplete query: AI game assets is:public fork:false archived:false (200 of 633 matches sampled)
- gaming: bounded or incomplete query: AI blender pushed:>=2026-09-06 is:public fork:false archived:false (200 of 417 matches sampled)
- gaming: bounded or incomplete query: AI blender created:>=2026-09-06 is:public fork:false archived:false (200 of 308 matches sampled)
- gaming: bounded or incomplete query: AI blender is:public fork:false archived:false (200 of 1536 matches sampled)
- motion: bounded or incomplete query: AI motion capture is:public fork:false archived:false (200 of 231 matches sampled)
- motion: bounded or incomplete query: motion generation is:public fork:false archived:false (200 of 1497 matches sampled)
- avatars: bounded or incomplete query: AI avatar pushed:>=2026-09-06 is:public fork:false archived:false (200 of 738 matches sampled)
- avatars: bounded or incomplete query: AI avatar created:>=2026-09-06 is:public fork:false archived:false (200 of 393 matches sampled)
- avatars: bounded or incomplete query: AI avatar is:public fork:false archived:false (200 of 5855 matches sampled)
- avatars: bounded or incomplete query: lip sync pushed:>=2026-09-06 is:public fork:false archived:false (200 of 286 matches sampled)
- avatars: bounded or incomplete query: lip sync is:public fork:false archived:false (200 of 2381 matches sampled)
- vfx: bounded or incomplete query: AI visual effects is:public fork:false archived:false (200 of 416 matches sampled)
- capture: bounded or incomplete query: topic:gaussian-splatting pushed:>=2026-09-06 is:public fork:false archived:false (200 of 240 matches sampled)
- capture: bounded or incomplete query: topic:gaussian-splatting is:public fork:false archived:false (500 of 903 matches sampled)
- capture: bounded or incomplete query: neural reconstruction is:public fork:false archived:false (200 of 1315 matches sampled)
- editing: bounded or incomplete query: AI video editing pushed:>=2026-09-06 is:public fork:false archived:false (200 of 814 matches sampled)
- editing: bounded or incomplete query: AI video editing created:>=2026-09-06 is:public fork:false archived:false (200 of 513 matches sampled)
- editing: bounded or incomplete query: AI video editing is:public fork:false archived:false (200 of 3392 matches sampled)
- editing: bounded or incomplete query: AI subtitle pushed:>=2026-09-06 is:public fork:false archived:false (200 of 367 matches sampled)
- editing: bounded or incomplete query: AI subtitle is:public fork:false archived:false (200 of 2203 matches sampled)
- vector: bounded or incomplete query: AI SVG pushed:>=2026-09-06 is:public fork:false archived:false (200 of 421 matches sampled)
- vector: bounded or incomplete query: AI SVG created:>=2026-09-06 is:public fork:false archived:false (200 of 233 matches sampled)
- vector: bounded or incomplete query: AI SVG is:public fork:false archived:false (200 of 1761 matches sampled)
- typography: bounded or incomplete query: AI typography is:public fork:false archived:false (200 of 647 matches sampled)
- typography: bounded or incomplete query: font generation is:public fork:false archived:false (400 of 416 matches sampled)
- storytelling: bounded or incomplete query: AI storyboard pushed:>=2026-09-06 is:public fork:false archived:false (200 of 371 matches sampled)
- storytelling: bounded or incomplete query: AI storyboard created:>=2026-09-06 is:public fork:false archived:false (200 of 214 matches sampled)
- storytelling: bounded or incomplete query: AI storyboard is:public fork:false archived:false (200 of 1670 matches sampled)
- storytelling: bounded or incomplete query: AI comic pushed:>=2026-09-06 is:public fork:false archived:false (200 of 1664 matches sampled)
- storytelling: bounded or incomplete query: AI comic created:>=2026-09-06 is:public fork:false archived:false (200 of 1581 matches sampled)
- storytelling: bounded or incomplete query: AI comic is:public fork:false archived:false (200 of 2936 matches sampled)
- publishing: bounded or incomplete query: AI presentation pushed:>=2026-09-06 is:public fork:false archived:false (200 of 1102 matches sampled)
- publishing: bounded or incomplete query: AI presentation created:>=2026-09-06 is:public fork:false archived:false (200 of 675 matches sampled)
- publishing: bounded or incomplete query: AI presentation is:public fork:false archived:false (200 of 8436 matches sampled)
- publishing: bounded or incomplete query: AI publishing pushed:>=2026-09-06 is:public fork:false archived:false (200 of 1071 matches sampled)
- publishing: bounded or incomplete query: AI publishing created:>=2026-09-06 is:public fork:false archived:false (200 of 654 matches sampled)
- publishing: bounded or incomplete query: AI publishing is:public fork:false archived:false (200 of 4000 matches sampled)
- photography: bounded or incomplete query: AI colorization pushed:>=2026-09-06 is:public fork:false archived:false (200 of 441 matches sampled)
- photography: bounded or incomplete query: AI colorization created:>=2026-09-06 is:public fork:false archived:false (200 of 281 matches sampled)
- photography: bounded or incomplete query: AI colorization is:public fork:false archived:false (200 of 4708 matches sampled)
- visualization: bounded or incomplete query: AI visualization pushed:>=2026-09-06 is:public fork:false archived:false (200 of 3245 matches sampled)
- visualization: bounded or incomplete query: AI visualization created:>=2026-09-06 is:public fork:false archived:false (200 of 1882 matches sampled)
- visualization: bounded or incomplete query: AI visualization is:public fork:false archived:false (200 of 37534 matches sampled)
- visualization: bounded or incomplete query: AI data art is:public fork:false archived:false (200 of 1015 matches sampled)
- performance: bounded or incomplete query: AI live visuals is:public fork:false archived:false (200 of 703 matches sampled)
- fashion: bounded or incomplete query: AI fashion design is:public fork:false archived:false (200 of 635 matches sampled)
- fashion: bounded or incomplete query: AI textile is:public fork:false archived:false (200 of 463 matches sampled)
- accessibility: bounded or incomplete query: AI audio description is:public fork:false archived:false (200 of 253 matches sampled)
- mobile: bounded or incomplete query: AI mobile media is:public fork:false archived:false (200 of 207 matches sampled)
- education: bounded or incomplete query: AI explainer pushed:>=2026-09-06 is:public fork:false archived:false (200 of 6370 matches sampled)
- education: bounded or incomplete query: AI explainer created:>=2026-09-06 is:public fork:false archived:false (200 of 4362 matches sampled)
- education: bounded or incomplete query: AI explainer is:public fork:false archived:false (200 of 36714 matches sampled)
- frontier: bounded or incomplete query: AI creative tools pushed:>=2026-09-06 is:public fork:false archived:false (200 of 235 matches sampled)
- frontier: bounded or incomplete query: AI creative tools is:public fork:false archived:false (200 of 1936 matches sampled)
- frontier: bounded or incomplete query: AI digital art is:public fork:false archived:false (200 of 718 matches sampled)
- frontier: bounded or incomplete query: AI multimedia is:public fork:false archived:false (200 of 1167 matches sampled)
- frontier: bounded or incomplete query: AI new media is:public fork:false archived:false (200 of 500 matches sampled)
- neural-acoustics: bounded or incomplete query: neural acoustic is:public fork:false archived:false (200 of 341 matches sampled)
- agent-media-production: bounded or incomplete query: AI agent animation is:public fork:false archived:false (200 of 497 matches sampled)
- agent-media-production: bounded or incomplete query: AI agent video editing is:public fork:false archived:false (200 of 425 matches sampled)
- architectural-media: bounded or incomplete query: AI architectural visualization is:public fork:false archived:false (200 of 900 matches sampled)
- architectural-media: bounded or incomplete query: AI floor plan is:public fork:false archived:false (200 of 628 matches sampled)

## Aedifex

AI architectural visualization and spatial design · 3D, reconstruction & assets · Interactive, immersive & live media

First detailed library baseline. Documentation and complete software license checked on 2026-10-06; no claim of a new release today.

### How it uses AI

An AI agent invokes scene-editing tools for walls, openings and furnishings; ghost previews and confirmation expose proposed changes. [Source](https://github.com/TangSY/aedifex/blob/main/README.md)

### Introduction

A browser-based architectural editor that turns natural-language requests into editable building geometry. [Source 1](https://github.com/TangSY/aedifex/blob/main/README.md)

### What it is good for

Blocking out interiors, rearranging furniture, reviewing floor plans and exporting a scene for further design work. [Source 1](https://github.com/TangSY/aedifex/blob/main/README.md)

### Demo & examples

The official README includes a recorded editor demonstration. [Source 1](https://github.com/TangSY/aedifex/blob/main/README.md)

### Install

Use the official route below; commands are documented instructions, not commands run during this review. [Source 1](https://github.com/TangSY/aedifex/blob/main/README.md)

1. Clone the repository and install Node.js 20+ and pnpm 9+.
2. Install dependencies; configure the editor environment with a supported model endpoint and keep API keys private.
3. Start the development server and open localhost:3002.

```sh
pnpm install
```


```sh
pnpm dev
```

### First project

Begin with a small example and review the result before expanding the project. [Source 1](https://github.com/TangSY/aedifex/blob/main/README.md)

1. Create a small room and request one furniture-layout change.
2. Inspect the preview, confirm the edit, and export GLB/OBJ or the documented fabrication formats.
### Hardware & software

Requirements below reflect the cited documentation. Unreported minimums remain unknown. [Source 1](https://github.com/TangSY/aedifex/blob/main/README.md)

- **Hardware:** A WebGPU-capable computer is required; minimum RAM, VRAM and free storage are not documented.
- **Software:** Node.js 20+, pnpm 9+; an OpenAI-compatible service or the documented local-model option.
- **Platforms:** README names Chrome 113+, Edge 113+ and Firefox Nightly with WebGPU. Native OS-specific support is not separately validated.

### License, model weights & costs

The complete top-level MIT software license was reviewed and archived. Keep dependent components and model terms separate. [Source 1](https://github.com/TangSY/aedifex/blob/main/LICENSE) [Source 2](https://github.com/TangSY/aedifex/blob/main/README.md)

- **Code:** MIT
- **Weights:** No bundled model grants are implied by the MIT editor. Local-model weights or hosted API terms apply independently.
- **Commercial:** The reviewed software license permits commercial software use subject to its obligations; it does not clear independent weights, data, assets, services or dependencies.
- **Cost:** Source code is available under the stated license. Hardware, electricity, storage and any optional or required hosted model/API services may add costs; no current service-price quote is asserted.

### Why it merits attention

Its documented workflow is relevant to blocking out interiors, rearranging furniture, reviewing floor plans and exporting a scene for further design work. The sources provide a concrete implementation and setup path. This assessment is based on documentation and developer examples, not independent output or performance testing. [Source 1](https://github.com/TangSY/aedifex/blob/main/README.md)

### Limitations

Geometry exports, including STL/3MF, are not evidence of structural safety or print readiness. Browser support and provider integration were reviewed in documentation only. [Source 1](https://github.com/TangSY/aedifex/blob/main/README.md)

### Get the tool

- [Repository](https://github.com/TangSY/aedifex)
- [Documentation](https://github.com/TangSY/aedifex/blob/main/README.md)
- [License](https://github.com/TangSY/aedifex/blob/main/LICENSE)

## ArchLang

AI architectural visualization and spatial design · Vector graphics, illustration & textures · AI agents for code-authored media production

First detailed library baseline. Documentation and complete software license checked on 2026-10-06; no claim of a new release today.

### How it uses AI

An external language-model agent writes the .arch DSL and responds to structured validation errors; the compiler itself is deterministic. [Source](https://github.com/ChanMeng666/archlang/blob/main/README.md) [Source](https://github.com/ChanMeng666/archlang/blob/main/package.json)

### Introduction

A floor-plan language and compiler that gives AI agents a structured way to author drawings. [Source 1](https://github.com/ChanMeng666/archlang/blob/main/README.md) [Source 2](https://github.com/ChanMeng666/archlang/blob/main/package.json)

### What it is good for

Producing dimensioned plans, iterating room layouts and exporting SVG, DXF, PDF, PNG or plain-text previews. [Source 1](https://github.com/ChanMeng666/archlang/blob/main/README.md) [Source 2](https://github.com/ChanMeng666/archlang/blob/main/package.json)

### Demo & examples

The project links an interactive playground at https://playground.archlang.uk. [Source 1](https://archlang.uk)

### Install

Use the official route below; commands are documented instructions, not commands run during this review. [Source 1](https://github.com/ChanMeng666/archlang/blob/main/README.md) [Source 2](https://github.com/ChanMeng666/archlang/blob/main/package.json)

1. Install Node.js 18 or newer.
2. Use the published npx CLI to create a starter plan.
3. Compile to SVG; PDF/PNG routes have separately documented optional dependencies.

```sh
npx @chanmeng666/archlang new -o plan.arch
```


```sh
npx @chanmeng666/archlang compile plan.arch -o plan.svg
```

### First project

Begin with a small example and review the result before expanding the project. [Source 1](https://github.com/ChanMeng666/archlang/blob/main/README.md) [Source 2](https://github.com/ChanMeng666/archlang/blob/main/package.json)

1. Edit the starter room dimensions or ask an AI coding agent to do so.
2. Compile, inspect the plan and correct validation errors before using the export.
### Hardware & software

Requirements below reflect the cited documentation. Unreported minimums remain unknown. [Source 1](https://github.com/ChanMeng666/archlang/blob/main/README.md) [Source 2](https://github.com/ChanMeng666/archlang/blob/main/package.json)

- **Hardware:** RAM, VRAM and storage minimums are not documented; no bundled inference GPU requirement is specified.
- **Software:** Node.js >=18; optional rendering dependencies for some export formats; an external AI client for assisted authoring.
- **Platforms:** Node-based CLI and browser playground are documented; an OS-by-OS support matrix is not provided.

### License, model weights & costs

The complete top-level MIT software license was reviewed and archived. Keep dependent components and model terms separate. [Source 1](https://github.com/ChanMeng666/archlang/blob/main/LICENSE) [Source 2](https://github.com/ChanMeng666/archlang/blob/main/README.md) [Source 3](https://github.com/ChanMeng666/archlang/blob/main/package.json)

- **Code:** MIT
- **Weights:** The compiler is MIT; any connected model or agent has separate terms and possible service costs.
- **Commercial:** The reviewed software license permits commercial software use subject to its obligations; it does not clear independent weights, data, assets, services or dependencies.
- **Cost:** Source code is available under the stated license. Hardware, electricity, storage and any optional or required hosted model/API services may add costs; no current service-price quote is asserted.

### Why it merits attention

Its documented workflow is relevant to producing dimensioned plans, iterating room layouts and exporting SVG, DXF, PDF, PNG or plain-text previews. The sources provide a concrete implementation and setup path. This assessment is based on documentation and developer examples, not independent output or performance testing. [Source 1](https://github.com/ChanMeng666/archlang/blob/main/README.md) [Source 2](https://github.com/ChanMeng666/archlang/blob/main/package.json)

### Limitations

This is a design-authoring tool, not a building-code or engineering certification system. AI assistance depends on an external agent. [Source 1](https://github.com/ChanMeng666/archlang/blob/main/README.md) [Source 2](https://github.com/ChanMeng666/archlang/blob/main/package.json)

### Get the tool

- [Repository](https://github.com/ChanMeng666/archlang)
- [Documentation](https://archlang.uk)
- [License](https://github.com/ChanMeng666/archlang/blob/main/LICENSE)

## InstructScene

AI architectural visualization and spatial design · 3D, reconstruction & assets · Spatial audio & volumetric media

First detailed library baseline. Documentation and complete software license checked on 2026-10-06; no claim of a new release today.

### How it uses AI

Learned semantic and geometric models arrange objects into 3D scenes from instructions. [Source](https://github.com/chenguolin/InstructScene/blob/main/README.md)

### Introduction

A research system for generating indoor scenes using a semantic graph prior and a layout decoder. [Source 1](https://github.com/chenguolin/InstructScene/blob/main/README.md)

### What it is good for

Text-conditioned interior scene composition, rearrangement and completion experiments. [Source 1](https://github.com/chenguolin/InstructScene/blob/main/README.md)

### Demo & examples

The official project page presents scene generation and editing examples. [Source 1](https://chenguolin.github.io/projects/InstructScene/)

### Install

Use the official route below; commands are documented instructions, not commands run during this review. [Source 1](https://github.com/chenguolin/InstructScene/blob/main/README.md)

1. Clone the official repository and follow settings/setup.sh as documented.
2. Obtain the required 3D-FRONT/3D-FUTURE assets under their own terms.
3. Download matching object-feature, semantic-prior and decoder checkpoints before running the example.

```sh
bash settings/setup.sh
```

### First project

Begin with a small example and review the result before expanding the project. [Source 1](https://github.com/chenguolin/InstructScene/blob/main/README.md)

1. Start with the documented bedroom example and matching checkpoints.
2. Run the inference script, then render the resulting scene using the documented Blender route.
### Hardware & software

Requirements below reflect the cited documentation. Unreported minimums remain unknown. [Source 1](https://github.com/chenguolin/InstructScene/blob/main/README.md)

- **Hardware:** Single-GPU training is described; A40 training times are examples rather than a minimum. RAM, minimum VRAM and disk capacity are not specified.
- **Software:** Python/PyTorch/CUDA environment from the setup script; the README provides Blender 3.3.1 for Linux x64.
- **Platforms:** The documented rendering route targets Linux; native Windows and macOS support is not established.

### License, model weights & costs

The complete top-level MIT software license was reviewed and archived. Keep dependent components and model terms separate. [Source 1](https://github.com/chenguolin/InstructScene/blob/main/LICENSE) [Source 2](https://github.com/chenguolin/InstructScene/blob/main/README.md)

- **Code:** MIT
- **Weights:** MIT code. Dataset access and checkpoint terms are separate; some shared prior/decoder checkpoints are community-provided.
- **Commercial:** The reviewed software license permits commercial software use subject to its obligations; it does not clear independent weights, data, assets, services or dependencies.
- **Cost:** Source code is available under the stated license. Hardware, electricity, storage and any optional or required hosted model/API services may add costs; no current service-price quote is asserted.

### Why it merits attention

Its documented workflow is relevant to text-conditioned interior scene composition, rearrangement and completion experiments. The sources provide a concrete implementation and setup path. This assessment is based on documentation and developer examples, not independent output or performance testing. [Source 1](https://github.com/chenguolin/InstructScene/blob/main/README.md)

### Limitations

Research reproduction requires compatible datasets and checkpoints. Published illustrations are author results, not our tests. [Source 1](https://github.com/chenguolin/InstructScene/blob/main/README.md)

### Get the tool

- [Repository](https://github.com/chenguolin/InstructScene)
- [Documentation](https://chenguolin.github.io/projects/InstructScene/)
- [License](https://github.com/chenguolin/InstructScene/blob/main/LICENSE)

## LDraw Nova

3D printing & generative CAD · AI-assisted textile and computational craft · WebXR, VR & AR

First detailed library baseline. The repository falls within the discovery window, but this is not independent evidence of its launch date. Documentation and complete software license checked on 2026-10-06; no claim of a new release today.

### How it uses AI

A connected agent calls Python CAD and part-search tools to build and revise assemblies; optional semantic reranking supplements text search. [Source](https://github.com/anteloc/ldraw-nova/blob/master/README.md) [Source](https://github.com/anteloc/ldraw-nova/blob/master/ATTRIBUTION.md)

### Introduction

An AI-agent-oriented CAD environment for constructing and inspecting virtual brick models. [Source 1](https://github.com/anteloc/ldraw-nova/blob/master/README.md) [Source 2](https://github.com/anteloc/ldraw-nova/blob/master/ATTRIBUTION.md)

### What it is good for

Planning LDraw assemblies, searching parts, inspecting gaps/collisions and viewing designs in a browser or Quest 3. [Source 1](https://github.com/anteloc/ldraw-nova/blob/master/README.md) [Source 2](https://github.com/anteloc/ldraw-nova/blob/master/ATTRIBUTION.md)

### Demo & examples

The README links a workflow video and Quest-oriented 3D/VR viewer. [Source 1](https://github.com/anteloc/ldraw-nova/blob/master/README.md)

### Install

Use the official route below; commands are documented instructions, not commands run during this review. [Source 1](https://github.com/anteloc/ldraw-nova/blob/master/README.md) [Source 2](https://github.com/anteloc/ldraw-nova/blob/master/ATTRIBUTION.md)

1. Install Git and Docker with Compose.
2. Clone ldraw-nova and its companion Docker repository as sibling directories at the matching documented v0.6.0 versions.
3. Build and start the documented Compose stack; use the local viewer and configure an agent separately.
### First project

Begin with a small example and review the result before expanding the project. [Source 1](https://github.com/anteloc/ldraw-nova/blob/master/README.md) [Source 2](https://github.com/anteloc/ldraw-nova/blob/master/ATTRIBUTION.md)

1. Ask the connected agent to assemble a small model and render a preview.
2. Review geometry and part availability, then inspect or export the virtual assembly.
### Hardware & software

Requirements below reflect the cited documentation. Unreported minimums remain unknown. [Source 1](https://github.com/anteloc/ldraw-nova/blob/master/README.md) [Source 2](https://github.com/anteloc/ldraw-nova/blob/master/ATTRIBUTION.md)

- **Hardware:** The first Docker build is documented at roughly 5 GB. RAM and VRAM minimums are not stated; Quest 3 is optional for VR.
- **Software:** Git, Docker/Compose, the matching companion project and an AI agent; semantic reranking can use a separate API key.
- **Platforms:** Container/browser workflow; Quest 3 viewing is described. The README does not establish equal native support on every desktop OS.

### License, model weights & costs

The complete top-level AGPL-3.0 software license was reviewed and archived. Keep dependent components and model terms separate. [Source 1](https://github.com/anteloc/ldraw-nova/blob/master/LICENSE) [Source 2](https://github.com/anteloc/ldraw-nova/blob/master/README.md) [Source 3](https://github.com/anteloc/ldraw-nova/blob/master/ATTRIBUTION.md)

- **Code:** AGPL-3.0
- **Weights:** AGPL-3.0 application code; project documentation uses CC-BY-SA-4.0. LDraw assets, companion components and external model terms require separate attention.
- **Commercial:** The reviewed software license permits commercial software use subject to its obligations; it does not clear independent weights, data, assets, services or dependencies. AGPL obligations can apply when modified software is made available over a network.
- **Cost:** Source code is available under the stated license. Hardware, electricity, storage and any optional or required hosted model/API services may add costs; no current service-price quote is asserted.

### Why it merits attention

Its documented workflow is relevant to planning LDraw assemblies, searching parts, inspecting gaps/collisions and viewing designs in a browser or Quest 3. The sources provide a concrete implementation and setup path. This assessment is based on documentation and developer examples, not independent output or performance testing. [Source 1](https://github.com/anteloc/ldraw-nova/blob/master/README.md) [Source 2](https://github.com/anteloc/ldraw-nova/blob/master/ATTRIBUTION.md)

### Limitations

The local service has no authentication and is intended for a trusted network. VR performance and generation speed have known limits; a virtual assembly is not proof of physical buildability. [Source 1](https://github.com/anteloc/ldraw-nova/blob/master/README.md) [Source 2](https://github.com/anteloc/ldraw-nova/blob/master/ATTRIBUTION.md)

### Get the tool

- [Repository](https://github.com/anteloc/ldraw-nova)
- [Documentation](https://github.com/anteloc/ldraw-nova/blob/master/README.md)
- [License](https://github.com/anteloc/ldraw-nova/blob/master/LICENSE)

## Brush

Photogrammetry, scanning & neural rendering · 3D, reconstruction & assets · Browser tools & web media · Mobile, edge & on-device creation

First detailed library baseline. Documentation and complete software license checked on 2026-10-06; no claim of a new release today.

### How it uses AI

Optimizes Gaussian scene representations from calibrated photographs rather than merely displaying conventional geometry. [Source](https://github.com/ArthurBrussee/brush/blob/main/README.md)

### Introduction

A Gaussian-splat training and viewing application built around Burn and WebGPU. [Source 1](https://github.com/ArthurBrussee/brush/blob/main/README.md)

### What it is good for

Reconstructing photographed scenes as neural 3D assets and comparing training results interactively. [Source 1](https://github.com/ArthurBrussee/brush/blob/main/README.md)

### Demo & examples

The project provides a browser demo and example splat assets. [Source 1](https://arthurbrussee.github.io/brush-demo)

### Install

Use the official route below; commands are documented instructions, not commands run during this review. [Source 1](https://github.com/ArthurBrussee/brush/blob/main/README.md)

1. Prefer an official release for a supported desktop.
2. For a source build, install Rust 1.88+ and clone the repository.
3. Android builds additionally require the documented SDK/NDK toolchain.

```sh
cargo run --release
```

### First project

Begin with a small example and review the result before expanding the project. [Source 1](https://github.com/ArthurBrussee/brush/blob/main/README.md)

1. Load a documented COLMAP or Nerfstudio dataset.
2. Train while inspecting the reconstruction, then save or open the supported PLY/splat formats.
### Hardware & software

Requirements below reflect the cited documentation. Unreported minimums remain unknown. [Source 1](https://github.com/ArthurBrussee/brush/blob/main/README.md)

- **Hardware:** A compatible GPU/WebGPU backend is needed; RAM, VRAM and disk needs depend on the scene and no universal minimum is given.
- **Software:** Rust 1.88+ for source builds; calibrated training data; browser WebGPU for the web demo.
- **Platforms:** Native Windows, macOS and Linux plus an Android build route are documented. Web instructions identify Chrome/Edge; do not assume Safari/Firefox support.

### License, model weights & costs

The complete top-level Apache-2.0 software license was reviewed and archived. Keep dependent components and model terms separate. [Source 1](https://github.com/ArthurBrussee/brush/blob/main/LICENSE) [Source 2](https://github.com/ArthurBrussee/brush/blob/main/README.md)

- **Code:** Apache-2.0
- **Weights:** Apache-2.0 code. Source photographs and any imported datasets remain subject to their own rights.
- **Commercial:** The reviewed software license permits commercial software use subject to its obligations; it does not clear independent weights, data, assets, services or dependencies.
- **Cost:** Source code is available under the stated license. Hardware, electricity, storage and any optional or required hosted model/API services may add costs; no current service-price quote is asserted.

### Why it merits attention

Its documented workflow is relevant to reconstructing photographed scenes as neural 3D assets and comparing training results interactively. The sources provide a concrete implementation and setup path. This assessment is based on documentation and developer examples, not independent output or performance testing. [Source 1](https://github.com/ArthurBrussee/brush/blob/main/README.md)

### Limitations

The browser route has narrower compatibility than native builds. Reconstruction quality depends on capture coverage; published performance is not independently tested. [Source 1](https://github.com/ArthurBrussee/brush/blob/main/README.md)

### Get the tool

- [Repository](https://github.com/ArthurBrussee/brush)
- [Documentation](https://arthurbrussee.github.io/brush-demo)
- [License](https://github.com/ArthurBrussee/brush/blob/main/LICENSE)

## Marigold

Photography, restoration & color · VFX, compositing & relighting · Neural relighting and material recovery

First detailed library baseline. Documentation and complete software license checked on 2026-10-06; no claim of a new release today.

### How it uses AI

Pretrained diffusion models infer geometric and appearance information from RGB images. [Source](https://github.com/prs-eth/Marigold/blob/main/README.md)

### Introduction

Diffusion-based image analysis for depth, surface normals and intrinsic appearance/lighting estimates. [Source 1](https://github.com/prs-eth/Marigold/blob/main/README.md)

### What it is good for

Preparing depth-driven composites, relighting studies and material/normal references from photographs. [Source 1](https://github.com/prs-eth/Marigold/blob/main/README.md)

### Demo & examples

The official project site links interactive depth, normals and intrinsic-image demos. [Source 1](https://marigoldcomputervision.github.io/)

### Install

Use the official route below; commands are documented instructions, not commands run during this review. [Source 1](https://github.com/prs-eth/Marigold/blob/main/README.md)

1. Clone the repository and create the documented Python environment.
2. Install requirements and select the checkpoint for the desired task.
3. Run the task-specific inference script; initial use downloads model files.

```sh
pip install -r requirements.txt
```


```sh
python script/depth/run.py --checkpoint prs-eth/marigold-depth-v1-1 --input_rgb_dir input/in-the-wild_example --output_dir output/in-the-wild_example --fp16
```

### First project

Begin with a small example and review the result before expanding the project. [Source 1](https://github.com/prs-eth/Marigold/blob/main/README.md)

1. Test one well-exposed photo using depth inference.
2. Inspect the output and confidence/ensemble settings before bringing it into a compositor.
### Hardware & software

Requirements below reflect the cited documentation. Unreported minimums remain unknown. [Source 1](https://github.com/prs-eth/Marigold/blob/main/README.md)

- **Hardware:** Ubuntu/CUDA testing used an RTX 3090, which is not stated as a minimum. RAM, VRAM and storage minimums are not documented.
- **Software:** Reference environment: Ubuntu 22.04, Python 3.10.12, CUDA 11.7. Checkpoint choice and inference settings affect memory.
- **Platforms:** Linux is documented; Windows via WSL2 and an Apple Silicon MPS flag are described. These are documentation claims, not local tests.

### License, model weights & costs

The complete top-level Apache-2.0 software license was reviewed and archived. Keep dependent components and model terms separate. [Source 1](https://github.com/prs-eth/Marigold/blob/main/LICENSE.txt) [Source 2](https://github.com/prs-eth/Marigold/blob/main/README.md)

- **Code:** Apache-2.0
- **Weights:** Apache-2.0 software; verify each selected model card separately before commercial use.
- **Commercial:** The reviewed software license permits commercial software use subject to its obligations; it does not clear independent weights, data, assets, services or dependencies.
- **Cost:** Source code is available under the stated license. Hardware, electricity, storage and any optional or required hosted model/API services may add costs; no current service-price quote is asserted.

### Why it merits attention

Its documented workflow is relevant to preparing depth-driven composites, relighting studies and material/normal references from photographs. The sources provide a concrete implementation and setup path. This assessment is based on documentation and developer examples, not independent output or performance testing. [Source 1](https://github.com/prs-eth/Marigold/blob/main/README.md)

### Limitations

Depth and appearance maps are estimates rather than measured ground truth. Ensemble size and resolution trade speed for quality. [Source 1](https://github.com/prs-eth/Marigold/blob/main/README.md)

### Get the tool

- [Repository](https://github.com/prs-eth/Marigold)
- [Documentation](https://marigoldcomputervision.github.io/)
- [License](https://github.com/prs-eth/Marigold/blob/main/LICENSE.txt)

## Pixal3D

3D, reconstruction & assets · 3D printing & generative CAD

First detailed library baseline. Documentation and complete software license checked on 2026-10-06; no claim of a new release today.

### How it uses AI

A learned 3D generation pipeline reconstructs geometry and appearance from visual conditioning. [Source](https://github.com/TencentARC/Pixal3D/blob/master/README.md) [Source](https://github.com/TencentARC/Pixal3D/blob/master/NOTICE) [Source](https://github.com/microsoft/TRELLIS.2/blob/main/README.md)

### Introduction

Pixel-aligned image-to-3D generation with single-view and multi-view inference. [Source 1](https://github.com/TencentARC/Pixal3D/blob/master/README.md) [Source 2](https://github.com/TencentARC/Pixal3D/blob/master/NOTICE) [Source 3](https://github.com/microsoft/TRELLIS.2/blob/main/README.md)

### What it is good for

Building a textured 3D starting asset from an image for subsequent artist cleanup. [Source 1](https://github.com/TencentARC/Pixal3D/blob/master/README.md) [Source 2](https://github.com/TencentARC/Pixal3D/blob/master/NOTICE) [Source 3](https://github.com/microsoft/TRELLIS.2/blob/main/README.md)

### Demo & examples

The official project page and Hugging Face demo show image-to-mesh results. [Source 1](https://ldyang694.github.io/projects/pixal3d/)

### Install

Use the official route below; commands are documented instructions, not commands run during this review. [Source 1](https://github.com/TencentARC/Pixal3D/blob/master/README.md) [Source 2](https://github.com/TencentARC/Pixal3D/blob/master/NOTICE) [Source 3](https://github.com/microsoft/TRELLIS.2/blob/main/README.md)

1. Follow the current Pixal3D branch instructions together with its TRELLIS.2 base environment.
2. Install the additional requirements and architecture-specific attention dependencies.
3. Download the required weights and try the documented low-VRAM example.

```sh
python inference.py --image assets/images/0_img.png --output ./output.glb --low_vram
```


```sh
python app.py --low_vram
```

### First project

Begin with a small example and review the result before expanding the project. [Source 1](https://github.com/TencentARC/Pixal3D/blob/master/README.md) [Source 2](https://github.com/TencentARC/Pixal3D/blob/master/NOTICE) [Source 3](https://github.com/microsoft/TRELLIS.2/blob/main/README.md)

1. Use a clearly framed object photo.
2. Generate a GLB and inspect mesh, texture and unseen surfaces in a 3D editor.
### Hardware & software

Requirements below reflect the cited documentation. Unreported minimums remain unknown. [Source 1](https://github.com/TencentARC/Pixal3D/blob/master/README.md) [Source 2](https://github.com/TencentARC/Pixal3D/blob/master/NOTICE) [Source 3](https://github.com/microsoft/TRELLIS.2/blob/main/README.md)

- **Hardware:** The upstream TRELLIS.2 setup documents an NVIDIA GPU with at least 24 GB VRAM. Pixal3D offers lower-resolution low-VRAM mode but does not quantify a new guaranteed minimum; RAM/storage minimums are not stated.
- **Software:** Linux/CUDA-oriented setup; upstream CUDA 12.4 and Python >=3.8, with PyTorch and attention-extension versions needing to match.
- **Platforms:** Linux is the documented core route. Community Windows/WSL wrappers are linked; native macOS inference is not documented.

### License, model weights & costs

The complete top-level MIT software license was reviewed and archived. Keep dependent components and model terms separate. [Source 1](https://github.com/TencentARC/Pixal3D/blob/master/LICENSE) [Source 2](https://github.com/TencentARC/Pixal3D/blob/master/README.md) [Source 3](https://github.com/TencentARC/Pixal3D/blob/master/NOTICE) [Source 4](https://github.com/microsoft/TRELLIS.2/blob/main/README.md)

- **Code:** MIT
- **Weights:** The reviewed NOTICE states MIT for Pixal3D code and parameters; listed third-party components retain their respective MIT/Apache terms.
- **Commercial:** The reviewed software license permits commercial software use subject to its obligations; it does not clear independent weights, data, assets, services or dependencies.
- **Cost:** Source code is available under the stated license. Hardware, electricity, storage and any optional or required hosted model/API services may add costs; no current service-price quote is asserted.

### Why it merits attention

Its documented workflow is relevant to building a textured 3D starting asset from an image for subsequent artist cleanup. The sources provide a concrete implementation and setup path. This assessment is based on documentation and developer examples, not independent output or performance testing. [Source 1](https://github.com/TencentARC/Pixal3D/blob/master/README.md) [Source 2](https://github.com/TencentARC/Pixal3D/blob/master/NOTICE) [Source 3](https://github.com/microsoft/TRELLIS.2/blob/main/README.md)

### Limitations

Low-VRAM mode reduces resolution and does not prove support on small GPUs. Mesh export does not establish watertightness or print readiness. [Source 1](https://github.com/TencentARC/Pixal3D/blob/master/README.md) [Source 2](https://github.com/TencentARC/Pixal3D/blob/master/NOTICE) [Source 3](https://github.com/microsoft/TRELLIS.2/blob/main/README.md)

### Get the tool

- [Repository](https://github.com/TencentARC/Pixal3D)
- [Documentation](https://ldyang694.github.io/projects/pixal3d/)
- [License](https://github.com/TencentARC/Pixal3D/blob/master/LICENSE)

## Turbo MLX

Images & design · Video, animation & film · Audio, music & voice · Mobile, edge & on-device creation

First detailed library baseline. The repository falls within the discovery window, but this is not independent evidence of its launch date. Documentation and complete software license checked on 2026-10-06; no claim of a new release today.

### How it uses AI

Runs supported diffusion and audiovisual model families locally with quantized MLX implementations. [Source](https://github.com/rinste/turbo-mlx/blob/main/README.md)

### Introduction

A native Apple Silicon studio for local image and audiovisual generation using MLX. [Source 1](https://github.com/rinste/turbo-mlx/blob/main/README.md)

### What it is good for

Trying locally hosted image models, image edits, video generation and upscaling in one Mac interface. [Source 1](https://github.com/rinste/turbo-mlx/blob/main/README.md)

### Demo & examples

The official README links a recorded application walkthrough. [Source 1](https://github.com/rinste/turbo-mlx/blob/main/README.md)

### Install

Use the official route below; commands are documented instructions, not commands run during this review. [Source 1](https://github.com/rinste/turbo-mlx/blob/main/README.md)

1. Download the official Mac application release.
2. Choose a model compatible with available unified memory.
3. Download that model inside the app and complete any model-specific access requirements.
### First project

Begin with a small example and review the result before expanding the project. [Source 1](https://github.com/rinste/turbo-mlx/blob/main/README.md)

1. Start with a smaller supported image model.
2. Enter a prompt or reference image, generate, and export from the history view.
### Hardware & software

Requirements below reflect the cited documentation. Unreported minimums remain unknown. [Source 1](https://github.com/rinste/turbo-mlx/blob/main/README.md)

- **Hardware:** Apple Silicon M1 or newer; application minimum 16 GB unified memory. Documented model needs range roughly 16–64 GB and downloads about 5–38 GB, depending on model.
- **Software:** macOS 15+; MLX model packages and any gated-model authorization required by the chosen family.
- **Platforms:** Apple Silicon macOS. Native Windows, Linux and Intel Mac builds are not documented.

### License, model weights & costs

The complete top-level MIT software license was reviewed and archived. Keep dependent components and model terms separate. [Source 1](https://github.com/rinste/turbo-mlx/blob/main/LICENSE) [Source 2](https://github.com/rinste/turbo-mlx/blob/main/README.md)

- **Code:** MIT
- **Weights:** MIT application. Model families have different terms, including permissive models and LTX community/gated terms; inspect the exact model before commercial work.
- **Commercial:** The reviewed software license permits commercial software use subject to its obligations; it does not clear independent weights, data, assets, services or dependencies.
- **Cost:** Source code is available under the stated license. Hardware, electricity, storage and any optional or required hosted model/API services may add costs; no current service-price quote is asserted.

### Why it merits attention

Its documented workflow is relevant to trying locally hosted image models, image edits, video generation and upscaling in one Mac interface. The sources provide a concrete implementation and setup path. This assessment is based on documentation and developer examples, not independent output or performance testing. [Source 1](https://github.com/rinste/turbo-mlx/blob/main/README.md)

### Limitations

A model appearing in the menu does not mean it fits every Mac. Author speed examples are device-specific and were not reproduced. [Source 1](https://github.com/rinste/turbo-mlx/blob/main/README.md)

### Get the tool

- [Repository](https://github.com/rinste/turbo-mlx)
- [Documentation](https://github.com/rinste/turbo-mlx/blob/main/README.md)
- [License](https://github.com/rinste/turbo-mlx/blob/main/LICENSE)

## ImageGen Mac

Images & design · Photography, restoration & color

First detailed library baseline. The repository falls within the discovery window, but this is not independent evidence of its launch date. Documentation and complete software license checked on 2026-10-06; no claim of a new release today.

### How it uses AI

Runs a large image-generation/editing model through a local Apple Silicon backend. [Source](https://github.com/ph1lb4/imagegen-mac/blob/main/README.md) [Source](https://github.com/ph1lb4/imagegen-mac/blob/main/THIRD_PARTY_NOTICES.md)

### Introduction

A local Mac application for Qwen Image 2.1 generation and reference-image editing, with an MCP interface. [Source 1](https://github.com/ph1lb4/imagegen-mac/blob/main/README.md) [Source 2](https://github.com/ph1lb4/imagegen-mac/blob/main/THIRD_PARTY_NOTICES.md)

### What it is good for

Researching multi-reference edits, local image variations and transparent-background generation. [Source 1](https://github.com/ph1lb4/imagegen-mac/blob/main/README.md) [Source 2](https://github.com/ph1lb4/imagegen-mac/blob/main/THIRD_PARTY_NOTICES.md)

### Demo & examples

The official README contains application examples and media. [Source 1](https://github.com/ph1lb4/imagegen-mac/blob/main/README.md)

### Install

Use the official route below; commands are documented instructions, not commands run during this review. [Source 1](https://github.com/ph1lb4/imagegen-mac/blob/main/README.md) [Source 2](https://github.com/ph1lb4/imagegen-mac/blob/main/THIRD_PARTY_NOTICES.md)

1. Install Xcode Command Line Tools and uv on a supported Mac.
2. Clone the repository and build the application.
3. Move the built app into place and download its model assets.

```sh
./scripts/build-app.sh
```

### First project

Begin with a small example and review the result before expanding the project. [Source 1](https://github.com/ph1lb4/imagegen-mac/blob/main/README.md) [Source 2](https://github.com/ph1lb4/imagegen-mac/blob/main/THIRD_PARTY_NOTICES.md)

1. Load one reference image and make a small edit.
2. Compare the result with the original and export only within the model license permissions.
### Hardware & software

Requirements below reflect the cited documentation. Unreported minimums remain unknown. [Source 1](https://github.com/ph1lb4/imagegen-mac/blob/main/README.md) [Source 2](https://github.com/ph1lb4/imagegen-mac/blob/main/THIRD_PARTY_NOTICES.md)

- **Hardware:** Apple Silicon; 64 GB unified memory recommended, with 48 GB described as limited to smaller work. About 33 GB of weights, roughly 35 GB storage plus around 1 GB Python runtime.
- **Software:** macOS 14+, Xcode Command Line Tools and uv for the source build.
- **Platforms:** Apple Silicon macOS. Intel Mac, Windows and Linux are not documented targets.

### License, model weights & costs

The complete top-level MIT software license was reviewed and archived. Keep dependent components and model terms separate. [Source 1](https://github.com/ph1lb4/imagegen-mac/blob/main/LICENSE) [Source 2](https://github.com/ph1lb4/imagegen-mac/blob/main/README.md) [Source 3](https://github.com/ph1lb4/imagegen-mac/blob/main/THIRD_PARTY_NOTICES.md)

- **Code:** MIT
- **Weights:** MIT application code, but the reviewed third-party notice identifies Qwen Image 2.1 weights as non-commercial research licensed.
- **Commercial:** The application is open source, but the documented model restriction is non-commercial; do not treat this workflow as cleared for commercial/client work.
- **Cost:** Source code is available under the stated license. Hardware, electricity, storage and any optional or required hosted model/API services may add costs; no current service-price quote is asserted.

### Why it merits attention

Its documented workflow is relevant to researching multi-reference edits, local image variations and transparent-background generation. The sources provide a concrete implementation and setup path. This assessment is based on documentation and developer examples, not independent output or performance testing. [Source 1](https://github.com/ph1lb4/imagegen-mac/blob/main/README.md) [Source 2](https://github.com/ph1lb4/imagegen-mac/blob/main/THIRD_PARTY_NOTICES.md)

### Limitations

The software license does not authorize commercial use of the bundled model. High memory needs and untested output fidelity limit casual adoption. [Source 1](https://github.com/ph1lb4/imagegen-mac/blob/main/README.md) [Source 2](https://github.com/ph1lb4/imagegen-mac/blob/main/THIRD_PARTY_NOTICES.md)

### Get the tool

- [Repository](https://github.com/ph1lb4/imagegen-mac)
- [Documentation](https://github.com/ph1lb4/imagegen-mac/blob/main/README.md)
- [License](https://github.com/ph1lb4/imagegen-mac/blob/main/LICENSE)

## AMD AI Linux GenAI Platform

Images & design · Video, animation & film · Audio, music & voice

First detailed library baseline. The repository falls within the discovery window, but this is not independent evidence of its launch date. Documentation and complete software license checked on 2026-10-06; no claim of a new release today.

### How it uses AI

Coordinates supported generative models over Mesa/RADV Vulkan; the project does not claim to use the Ryzen NPU for this route. [Source](https://github.com/Octanium91/amd-ai-linux-genai-platform/blob/main/README.md) [Source](https://github.com/Octanium91/amd-ai-linux-genai-platform/blob/main/docs/models.md)

### Introduction

A local generative-media stack targeting AMD Ryzen AI integrated graphics through Vulkan. [Source 1](https://github.com/Octanium91/amd-ai-linux-genai-platform/blob/main/README.md) [Source 2](https://github.com/Octanium91/amd-ai-linux-genai-platform/blob/main/docs/models.md)

### What it is good for

Running image, video and audio workflows on selected AMD APU systems without a CUDA GPU. [Source 1](https://github.com/Octanium91/amd-ai-linux-genai-platform/blob/main/README.md) [Source 2](https://github.com/Octanium91/amd-ai-linux-genai-platform/blob/main/docs/models.md)

### Demo & examples

The repository documents the web interface and model-pack workflow. [Source 1](https://github.com/Octanium91/amd-ai-linux-genai-platform/blob/main/README.md)

### Install

Use the official route below; commands are documented instructions, not commands run during this review. [Source 1](https://github.com/Octanium91/amd-ai-linux-genai-platform/blob/main/README.md) [Source 2](https://github.com/Octanium91/amd-ai-linux-genai-platform/blob/main/docs/models.md)

1. Use a supported Linux host with Docker Compose and current Mesa/RADV.
2. Follow the repository setup and GPU checks, then build/start its containers.
3. Create the local administrator account and install a compatible model pack.

```sh
./scripts/setup.sh --install
```


```sh
docker compose up --build
```

### First project

Begin with a small example and review the result before expanding the project. [Source 1](https://github.com/Octanium91/amd-ai-linux-genai-platform/blob/main/README.md) [Source 2](https://github.com/Octanium91/amd-ai-linux-genai-platform/blob/main/docs/models.md)

1. Verify the Vulkan GPU is detected before loading models.
2. Start with an image pack, generate a small example and monitor shared-memory use.
### Hardware & software

Requirements below reflect the cited documentation. Unreported minimums remain unknown. [Source 1](https://github.com/Octanium91/amd-ai-linux-genai-platform/blob/main/README.md) [Source 2](https://github.com/Octanium91/amd-ai-linux-genai-platform/blob/main/docs/models.md)

- **Hardware:** Reference system: Ryzen AI HX 370/890M with 32 GB RAM and 24 GB GTT, not a universal minimum. Model storage is documented around 20–40 GB; tuning varies by APU.
- **Software:** Linux kernel 6.10+, Mesa RADV, Docker/Compose; optional Ollama prompt assistance.
- **Platforms:** Debian 13 is tested by the author and Ubuntu 24.04 is mentioned. Browser access from other devices does not mean those devices run inference.

### License, model weights & costs

The complete top-level MIT software license was reviewed and archived. Keep dependent components and model terms separate. [Source 1](https://github.com/Octanium91/amd-ai-linux-genai-platform/blob/main/LICENSE) [Source 2](https://github.com/Octanium91/amd-ai-linux-genai-platform/blob/main/README.md) [Source 3](https://github.com/Octanium91/amd-ai-linux-genai-platform/blob/main/docs/models.md)

- **Code:** MIT
- **Weights:** MIT orchestration code; model packs include different licenses such as Apache/MIT and OpenRAIL. Verify each pack separately.
- **Commercial:** The reviewed software license permits commercial software use subject to its obligations; it does not clear independent weights, data, assets, services or dependencies.
- **Cost:** Source code is available under the stated license. Hardware, electricity, storage and any optional or required hosted model/API services may add costs; no current service-price quote is asserted.

### Why it merits attention

Its documented workflow is relevant to running image, video and audio workflows on selected AMD APU systems without a CUDA GPU. The sources provide a concrete implementation and setup path. This assessment is based on documentation and developer examples, not independent output or performance testing. [Source 1](https://github.com/Octanium91/amd-ai-linux-genai-platform/blob/main/README.md) [Source 2](https://github.com/Octanium91/amd-ai-linux-genai-platform/blob/main/docs/models.md)

### Limitations

Tuned for particular Strix Point/Halo/Krackan systems. Native macOS/Windows operation and universal APU compatibility are not established. [Source 1](https://github.com/Octanium91/amd-ai-linux-genai-platform/blob/main/README.md) [Source 2](https://github.com/Octanium91/amd-ai-linux-genai-platform/blob/main/docs/models.md)

### Get the tool

- [Repository](https://github.com/Octanium91/amd-ai-linux-genai-platform)
- [Documentation](https://github.com/Octanium91/amd-ai-linux-genai-platform/blob/main/README.md)
- [License](https://github.com/Octanium91/amd-ai-linux-genai-platform/blob/main/LICENSE)

## DiffusionBee

Images & design · Photography, restoration & color · Editing, captions & post-production

First detailed library baseline. Documentation and complete software license checked on 2026-10-06; no claim of a new release today.

### How it uses AI

Runs diffusion image-generation models locally through a packaged GUI. [Source](https://github.com/divamgupta/diffusionbee-stable-diffusion-ui/blob/master/README.md)

### Introduction

A desktop interface for running Stable Diffusion image workflows locally on a Mac. [Source 1](https://github.com/divamgupta/diffusionbee-stable-diffusion-ui/blob/master/README.md)

### What it is good for

Text-to-image, image variations, inpainting/outpainting and supported ControlNet/LoRA workflows. [Source 1](https://github.com/divamgupta/diffusionbee-stable-diffusion-ui/blob/master/README.md)

### Demo & examples

The official product site presents application screenshots and generated examples. [Source 1](https://diffusionbee.com)

### Install

Use the official route below; commands are documented instructions, not commands run during this review. [Source 1](https://github.com/divamgupta/diffusionbee-stable-diffusion-ui/blob/master/README.md)

1. Download the appropriate official Mac release.
2. Install and launch the application, then obtain a compatible model through the documented workflow.
### First project

Begin with a small example and review the result before expanding the project. [Source 1](https://github.com/divamgupta/diffusionbee-stable-diffusion-ui/blob/master/README.md)

1. Generate a small image from a prompt.
2. Try a masked edit or reference-based variation and save the selected output.
### Hardware & software

Requirements below reflect the cited documentation. Unreported minimums remain unknown. [Source 1](https://github.com/divamgupta/diffusionbee-stable-diffusion-ui/blob/master/README.md)

- **Hardware:** The README does not publish universal RAM, VRAM or free-storage minimums; model size matters.
- **Software:** README lists macOS 12.3.1+ for Intel and macOS 11+ for M1/M2. Check the selected release and model compatibility.
- **Platforms:** macOS with Intel or supported Apple Silicon builds. Native Windows/Linux releases are not established in the reviewed documentation.

### License, model weights & costs

The complete top-level AGPL-3.0 software license was reviewed and archived. Keep dependent components and model terms separate. [Source 1](https://github.com/divamgupta/diffusionbee-stable-diffusion-ui/blob/master/LICENSE) [Source 2](https://github.com/divamgupta/diffusionbee-stable-diffusion-ui/blob/master/README.md)

- **Code:** AGPL-3.0
- **Weights:** AGPL-3.0 application code; Stable Diffusion and other model weights have separate, model-specific conditions.
- **Commercial:** The reviewed software license permits commercial software use subject to its obligations; it does not clear independent weights, data, assets, services or dependencies. AGPL obligations can apply when modified software is made available over a network.
- **Cost:** Source code is available under the stated license. Hardware, electricity, storage and any optional or required hosted model/API services may add costs; no current service-price quote is asserted.

### Why it merits attention

Its documented workflow is relevant to text-to-image, image variations, inpainting/outpainting and supported ControlNet/LoRA workflows. The sources provide a concrete implementation and setup path. This assessment is based on documentation and developer examples, not independent output or performance testing. [Source 1](https://github.com/divamgupta/diffusionbee-stable-diffusion-ui/blob/master/README.md)

### Limitations

A convenient GUI does not remove model licensing or resource constraints. Output quality and current release compatibility were not hands-on tested. [Source 1](https://github.com/divamgupta/diffusionbee-stable-diffusion-ui/blob/master/README.md)

### Get the tool

- [Repository](https://github.com/divamgupta/diffusionbee-stable-diffusion-ui)
- [Documentation](https://diffusionbee.com)
- [License](https://github.com/divamgupta/diffusionbee-stable-diffusion-ui/blob/master/LICENSE)

## PartCAD

3D printing & generative CAD · AI-assisted textile and computational craft · 3D, reconstruction & assets

First detailed library baseline. Documentation and complete software license checked on 2026-10-06; no claim of a new release today.

### How it uses AI

A connected agent can generate CAD code, render results and use geometric feedback to revise a part. [Source](https://github.com/partcad/partcad/blob/devel/README.md)

### Introduction

A CAD-as-code package system with CLI, IDE and agent-assisted design workflows. [Source 1](https://github.com/partcad/partcad/blob/devel/README.md)

### What it is good for

Organizing reusable parametric parts and assemblies, producing engineering-format exports and iterating with an AI coding agent. [Source 1](https://github.com/partcad/partcad/blob/devel/README.md)

### Demo & examples

Official documentation includes tutorials and CLI examples; platform IDE releases are linked. [Source 1](https://partcad.readthedocs.io/en/latest/)

### Install

Use the official route below; commands are documented instructions, not commands run during this review. [Source 1](https://github.com/partcad/partcad/blob/devel/README.md)

1. Choose the official IDE/extension or install the Python CLI in a suitable environment.
2. Follow platform prerequisites such as Windows long paths/Miniforge, Mac command-line tools or Linux graphics dependencies.

```sh
pip install -U partcad
```

### First project

Begin with a small example and review the result before expanding the project. [Source 1](https://github.com/partcad/partcad/blob/devel/README.md)

1. Open a documented sample package and inspect a part.
2. Ask a compatible AI agent for a dimensional change, review the rendered geometry and export using the documented CLI/IDE route.
### Hardware & software

Requirements below reflect the cited documentation. Unreported minimums remain unknown. [Source 1](https://github.com/partcad/partcad/blob/devel/README.md)

- **Hardware:** RAM, VRAM and disk minimums are not specified; local or remote AI model resources are additional.
- **Software:** Python/Conda environment for CLI use; CAD dependencies and optional VS Code extension or desktop IDE.
- **Platforms:** Windows, macOS and Linux routes are documented.

### License, model weights & costs

The complete top-level Apache-2.0 software license was reviewed and archived. Keep dependent components and model terms separate. [Source 1](https://github.com/partcad/partcad/blob/devel/LICENSE.txt) [Source 2](https://github.com/partcad/partcad/blob/devel/README.md)

- **Code:** Apache-2.0
- **Weights:** Apache-2.0 code. Connected agent/model services and imported CAD assets retain separate terms.
- **Commercial:** The reviewed software license permits commercial software use subject to its obligations; it does not clear independent weights, data, assets, services or dependencies.
- **Cost:** Source code is available under the stated license. Hardware, electricity, storage and any optional or required hosted model/API services may add costs; no current service-price quote is asserted.

### Why it merits attention

Its documented workflow is relevant to organizing reusable parametric parts and assemblies, producing engineering-format exports and iterating with an AI coding agent. The sources provide a concrete implementation and setup path. This assessment is based on documentation and developer examples, not independent output or performance testing. [Source 1](https://github.com/partcad/partcad/blob/devel/README.md)

### Limitations

AI-generated geometry needs dimensional and manufacturing review. A successful export is not a safety or fabrication certificate. [Source 1](https://github.com/partcad/partcad/blob/devel/README.md)

### Get the tool

- [Repository](https://github.com/partcad/partcad)
- [Documentation](https://partcad.readthedocs.io/en/latest/)
- [License](https://github.com/partcad/partcad/blob/devel/LICENSE.txt)

## QtMeshEditor

3D, reconstruction & assets · Games & production pipelines · AI agents for code-authored media production

First detailed library baseline. Documentation and complete software license checked on 2026-10-06; no claim of a new release today.

### How it uses AI

Its documented agent interface and AI-assisted material workflow let an AI client manipulate assets through editor operations. [Source](https://github.com/fernandotonon/QtMeshEditor/blob/master/README.md)

### Introduction

A mesh editor and command-line tool with an MCP interface for agent-controlled 3D asset work. [Source 1](https://github.com/fernandotonon/QtMeshEditor/blob/master/README.md)

### What it is good for

Inspecting/converting meshes, editing materials and preparing game assets with assisted operations. [Source 1](https://github.com/fernandotonon/QtMeshEditor/blob/master/README.md)

### Demo & examples

The official site and README include editor screenshots and workflow documentation. [Source 1](https://editor.qtmesh.dev/docs.html)

### Install

Use the official route below; commands are documented instructions, not commands run during this review. [Source 1](https://github.com/fernandotonon/QtMeshEditor/blob/master/README.md)

1. Choose an official release or the documented platform package route.
2. On Windows use the published winget package; on Mac use the documented Homebrew tap; Linux packages are also listed.
3. Configure an AI client separately if using MCP assistance.

```sh
winget install FernandoTonon.QtMeshEditor
```

### First project

Begin with a small example and review the result before expanding the project. [Source 1](https://github.com/fernandotonon/QtMeshEditor/blob/master/README.md)

1. Open a sample mesh and inspect materials and animation.
2. Ask the connected agent for a limited edit, review the result and export to the required asset format.
### Hardware & software

Requirements below reflect the cited documentation. Unreported minimums remain unknown. [Source 1](https://github.com/fernandotonon/QtMeshEditor/blob/master/README.md)

- **Hardware:** Minimum RAM, VRAM and storage are not documented as a universal requirement; AI model workloads can require additional hardware.
- **Software:** The packaged editor or its documented Qt build environment; an external AI client for agent control.
- **Platforms:** Windows, macOS and Linux package routes are documented.

### License, model weights & costs

The complete top-level MIT software license was reviewed and archived. Keep dependent components and model terms separate. [Source 1](https://github.com/fernandotonon/QtMeshEditor/blob/master/License) [Source 2](https://github.com/fernandotonon/QtMeshEditor/blob/master/README.md)

- **Code:** MIT
- **Weights:** MIT editor code. AI model/runtime components and any hosted services must be checked separately.
- **Commercial:** The reviewed software license permits commercial software use subject to its obligations; it does not clear independent weights, data, assets, services or dependencies.
- **Cost:** Source code is available under the stated license. Hardware, electricity, storage and any optional or required hosted model/API services may add costs; no current service-price quote is asserted.

### Why it merits attention

Its documented workflow is relevant to inspecting/converting meshes, editing materials and preparing game assets with assisted operations. The sources provide a concrete implementation and setup path. This assessment is based on documentation and developer examples, not independent output or performance testing. [Source 1](https://github.com/fernandotonon/QtMeshEditor/blob/master/README.md)

### Limitations

The reviewed evidence supports assisted asset operations, not a guarantee that every model-generation backend works on every platform. [Source 1](https://github.com/fernandotonon/QtMeshEditor/blob/master/README.md)

### Get the tool

- [Repository](https://github.com/fernandotonon/QtMeshEditor)
- [Documentation](https://editor.qtmesh.dev/docs.html)
- [License](https://github.com/fernandotonon/QtMeshEditor/blob/master/License)

## MidiTok

Audio, music & voice · AI music notation and score recovery · Computational art & creative coding

First detailed library baseline. Documentation and complete software license checked on 2026-10-06; no claim of a new release today.

### How it uses AI

Converts structured music into model-ready token vocabularies and datasets; learned language models can then generate or analyze those sequences. [Source](https://github.com/Natooz/MidiTok/blob/main/README.md)

### Introduction

A symbolic-music tokenization library for training and using music models. [Source 1](https://github.com/Natooz/MidiTok/blob/main/README.md)

### What it is good for

Preparing MIDI/ABC corpora for Transformer composition or transcription research and converting token sequences back to scores. [Source 1](https://github.com/Natooz/MidiTok/blob/main/README.md)

### Demo & examples

Official documentation includes tokenization examples and model-training notebooks. [Source 1](https://miditok.readthedocs.io/en/latest/)

### Install

Use the official route below; commands are documented instructions, not commands run during this review. [Source 1](https://github.com/Natooz/MidiTok/blob/main/README.md)

1. Install Python 3.9+ and the package.
2. Select a tokenizer such as REMI and follow the documentation configuration example.

```sh
pip install miditok
```

### First project

Begin with a small example and review the result before expanding the project. [Source 1](https://github.com/Natooz/MidiTok/blob/main/README.md)

1. Tokenize a small MIDI file and decode it to check the round trip.
2. Use the documented dataset/model notebook when ready to train or sample a music model.
### Hardware & software

Requirements below reflect the cited documentation. Unreported minimums remain unknown. [Source 1](https://github.com/Natooz/MidiTok/blob/main/README.md)

- **Hardware:** No universal RAM, VRAM or disk minimum is published; model training is a separate workload.
- **Software:** Python >=3.9 and package dependencies; PyTorch/model tooling when following the learning examples.
- **Platforms:** Python library; the reviewed documentation does not provide a complete tested desktop OS matrix.

### License, model weights & costs

The complete top-level MIT software license was reviewed and archived. Keep dependent components and model terms separate. [Source 1](https://github.com/Natooz/MidiTok/blob/main/LICENSE) [Source 2](https://github.com/Natooz/MidiTok/blob/main/README.md)

- **Code:** MIT
- **Weights:** MIT library. Training music rights and downstream model/checkpoint licenses remain separate.
- **Commercial:** The reviewed software license permits commercial software use subject to its obligations; it does not clear independent weights, data, assets, services or dependencies.
- **Cost:** Source code is available under the stated license. Hardware, electricity, storage and any optional or required hosted model/API services may add costs; no current service-price quote is asserted.

### Why it merits attention

Its documented workflow is relevant to preparing MIDI/ABC corpora for Transformer composition or transcription research and converting token sequences back to scores. The sources provide a concrete implementation and setup path. This assessment is based on documentation and developer examples, not independent output or performance testing. [Source 1](https://github.com/Natooz/MidiTok/blob/main/README.md)

### Limitations

This is developer infrastructure, not a standalone song generator. Representation choices can change musical detail. [Source 1](https://github.com/Natooz/MidiTok/blob/main/README.md)

### Get the tool

- [Repository](https://github.com/Natooz/MidiTok)
- [Documentation](https://miditok.readthedocs.io/en/latest/)
- [License](https://github.com/Natooz/MidiTok/blob/main/LICENSE)

## AnimateDiff

Video, animation & film · Motion capture & character animation · Images & design

Completed the detailed guide for an earlier screened discovery. Documentation and complete software license checked on 2026-10-06; no claim of a new release today.

### How it uses AI

Learned temporal modules add motion to a diffusion image backbone. [Source](https://github.com/guoyww/AnimateDiff/blob/main/README.md)

### Introduction

Motion modules that extend compatible text-to-image diffusion models into short animations. [Source 1](https://github.com/guoyww/AnimateDiff/blob/main/README.md)

### What it is good for

Animating a visual style, experimenting with motion adapters and conditioning video with supported control inputs. [Source 1](https://github.com/guoyww/AnimateDiff/blob/main/README.md)

### Demo & examples

The official project page provides clips and links a Hugging Face demo. [Source 1](https://animatediff.github.io/)

### Install

Use the official route below; commands are documented instructions, not commands run during this review. [Source 1](https://github.com/guoyww/AnimateDiff/blob/main/README.md)

1. Clone the repository and install the documented environment and requirements.
2. Choose the matching SD1.5 or SDXL route and obtain its base model and motion components.
3. Launch the documented Gradio interface or YAML-driven generation script.

```sh
pip install -r requirements.txt
```


```sh
python -u app.py
```

### First project

Begin with a small example and review the result before expanding the project. [Source 1](https://github.com/guoyww/AnimateDiff/blob/main/README.md)

1. Begin with an official sample configuration.
2. Change one prompt, inspect temporal consistency and export a short clip before increasing complexity.
### Hardware & software

Requirements below reflect the cited documentation. Unreported minimums remain unknown. [Source 1](https://github.com/guoyww/AnimateDiff/blob/main/README.md)

- **Hardware:** An SDXL example reports roughly 13 GB VRAM, not a universal minimum. The v3 motion module is about 1.56 GB plus adapter/base-model files; RAM and complete disk minimums are not stated.
- **Software:** Python/PyTorch/CUDA-oriented dependencies and compatible diffusion, motion and optional control checkpoints.
- **Platforms:** The reviewed setup does not establish a full native Windows/macOS/Linux compatibility matrix; a hosted demo is linked.

### License, model weights & costs

The complete top-level Apache-2.0 software license was reviewed and archived. Keep dependent components and model terms separate. [Source 1](https://github.com/guoyww/AnimateDiff/blob/main/LICENSE.txt) [Source 2](https://github.com/guoyww/AnimateDiff/blob/main/README.md)

- **Code:** Apache-2.0
- **Weights:** Apache-2.0 code; base image models and all downloaded motion/control weights need their own terms checked.
- **Commercial:** The reviewed software license permits commercial software use subject to its obligations; it does not clear independent weights, data, assets, services or dependencies.
- **Cost:** Source code is available under the stated license. Hardware, electricity, storage and any optional or required hosted model/API services may add costs; no current service-price quote is asserted.

### Why it merits attention

Its documented workflow is relevant to animating a visual style, experimenting with motion adapters and conditioning video with supported control inputs. The sources provide a concrete implementation and setup path. This assessment is based on documentation and developer examples, not independent output or performance testing. [Source 1](https://github.com/guoyww/AnimateDiff/blob/main/README.md)

### Limitations

Short clips can flicker or lose identity. Motion modules, adapters and backbone versions must match. [Source 1](https://github.com/guoyww/AnimateDiff/blob/main/README.md)

### Get the tool

- [Repository](https://github.com/guoyww/AnimateDiff)
- [Documentation](https://animatediff.github.io/)
- [License](https://github.com/guoyww/AnimateDiff/blob/main/LICENSE.txt)

## FireRed Image Edit

Images & design · Editing, captions & post-production · Photography, restoration & color

Completed the detailed guide for an earlier screened discovery. Documentation and complete software license checked on 2026-10-06; no claim of a new release today.

### How it uses AI

A generative editing model interprets text instructions together with one or more images. [Source](https://github.com/FireRedTeam/FireRed-Image-Edit/blob/main/README.md)

### Introduction

An image-editing model family with multi-reference composition and portrait-oriented controls. [Source 1](https://github.com/FireRedTeam/FireRed-Image-Edit/blob/main/README.md)

### What it is good for

Trying identity-preserving portrait changes, stylized text and composite edits from visual references. [Source 1](https://github.com/FireRedTeam/FireRed-Image-Edit/blob/main/README.md)

### Demo & examples

The README links official Hugging Face/ModelScope models and interactive examples for version 1.1. [Source 1](https://github.com/FireRedTeam/FireRed-Image-Edit/blob/main/README.md)

### Install

Use the official route below; commands are documented instructions, not commands run during this review. [Source 1](https://github.com/FireRedTeam/FireRed-Image-Edit/blob/main/README.md)

1. Clone the repository and install its requirements in the documented Python environment.
2. Obtain the matching model weights and run the supplied image-editing example.

```sh
pip install -r requirements.txt
```


```sh
python inference.py --input_image ./examples/edit_example.png --prompt "Change the background to a studio backdrop" --output_image output_edit.png --seed 43
```

### First project

Begin with a small example and review the result before expanding the project. [Source 1](https://github.com/FireRedTeam/FireRed-Image-Edit/blob/main/README.md)

1. Use one permitted portrait/reference image.
2. Make a single controlled change, compare identity and text details, then save the result.
### Hardware & software

Requirements below reflect the cited documentation. Unreported minimums remain unknown. [Source 1](https://github.com/FireRedTeam/FireRed-Image-Edit/blob/main/README.md)

- **Hardware:** An optimized author example uses around 30 GB VRAM; it is not a universal minimum or speed guarantee. RAM and disk minimums are not documented.
- **Software:** Repository Python/PyTorch requirements and the corresponding weights; optimization flags must match the documented setup.
- **Platforms:** GPU inference setup is documented; native macOS and Windows compatibility are not established. Hosted demos offer another route.

### License, model weights & costs

The complete top-level Apache-2.0 software license was reviewed and archived. Keep dependent components and model terms separate. [Source 1](https://github.com/FireRedTeam/FireRed-Image-Edit/blob/main/LICENSE) [Source 2](https://github.com/FireRedTeam/FireRed-Image-Edit/blob/main/README.md)

- **Code:** Apache-2.0
- **Weights:** The official README states Apache-2.0 for code and released model weights; check any added dependencies or assets separately.
- **Commercial:** The reviewed software license permits commercial software use subject to its obligations; it does not clear independent weights, data, assets, services or dependencies.
- **Cost:** Source code is available under the stated license. Hardware, electricity, storage and any optional or required hosted model/API services may add costs; no current service-price quote is asserted.

### Why it merits attention

Its documented workflow is relevant to trying identity-preserving portrait changes, stylized text and composite edits from visual references. The sources provide a concrete implementation and setup path. This assessment is based on documentation and developer examples, not independent output or performance testing. [Source 1](https://github.com/FireRedTeam/FireRed-Image-Edit/blob/main/README.md)

### Limitations

Documentation and demos were reviewed only. Portrait fidelity, spelling and multi-image consistency still need project-specific checking. [Source 1](https://github.com/FireRedTeam/FireRed-Image-Edit/blob/main/README.md)

### Get the tool

- [Repository](https://github.com/FireRedTeam/FireRed-Image-Edit)
- [Documentation](https://github.com/FireRedTeam/FireRed-Image-Edit/blob/main/README.md)
- [License](https://github.com/FireRedTeam/FireRed-Image-Edit/blob/main/LICENSE)

## threestudio

3D, reconstruction & assets · Computational art & creative coding

Completed the detailed guide for an earlier screened discovery. Documentation and complete software license checked on 2026-10-06; no claim of a new release today.

### How it uses AI

Uses pretrained generative models as guidance to optimize 3D representations. [Source](https://github.com/threestudio-project/threestudio/blob/main/README.md)

### Introduction

A configurable research framework for text/image-guided 3D generation. [Source 1](https://github.com/threestudio-project/threestudio/blob/main/README.md)

### What it is good for

Comparing DreamFusion-style optimization methods, representations and guidance models. [Source 1](https://github.com/threestudio-project/threestudio/blob/main/README.md)

### Demo & examples

The README includes example outputs and method-specific configurations. [Source 1](https://github.com/threestudio-project/threestudio/blob/main/README.md)

### Install

Use the official route below; commands are documented instructions, not commands run during this review. [Source 1](https://github.com/threestudio-project/threestudio/blob/main/README.md)

1. Clone the project and use its documented CUDA/Python environment.
2. Install requirements and accept/download the selected guidance model under its own terms.
3. Start with a lightweight documented configuration.

```sh
pip install -r requirements.txt
```


```sh
python launch.py --config configs/dreamfusion-sd.yaml --train --gpu 0 system.prompt_processor.prompt="a small ceramic teapot"
```

### First project

Begin with a small example and review the result before expanding the project. [Source 1](https://github.com/threestudio-project/threestudio/blob/main/README.md)

1. Run the sample optimization and inspect intermediate views.
2. Review the completed turntable/asset before trying a different guidance model.
### Hardware & software

Requirements below reflect the cited documentation. Unreported minimums remain unknown. [Source 1](https://github.com/threestudio-project/threestudio/blob/main/README.md)

- **Hardware:** The SD example is documented around 6 GB VRAM; DeepFloyd IF examples need over 20 GB. These are configuration-specific. RAM/storage minima are not stated.
- **Software:** Reference setup: Ubuntu 20.04, Python >=3.8, PyTorch >=1.12 and CUDA; model-specific extras may apply.
- **Platforms:** Linux is the documented reference. Native Windows/macOS operation is not established by the reviewed setup.

### License, model weights & costs

The complete top-level Apache-2.0 software license was reviewed and archived. Keep dependent components and model terms separate. [Source 1](https://github.com/threestudio-project/threestudio/blob/main/LICENSE) [Source 2](https://github.com/threestudio-project/threestudio/blob/main/README.md)

- **Code:** Apache-2.0
- **Weights:** Apache-2.0 framework; guidance weights, including gated models, have independent terms.
- **Commercial:** The reviewed software license permits commercial software use subject to its obligations; it does not clear independent weights, data, assets, services or dependencies.
- **Cost:** Source code is available under the stated license. Hardware, electricity, storage and any optional or required hosted model/API services may add costs; no current service-price quote is asserted.

### Why it merits attention

Its documented workflow is relevant to comparing DreamFusion-style optimization methods, representations and guidance models. The sources provide a concrete implementation and setup path. This assessment is based on documentation and developer examples, not independent output or performance testing. [Source 1](https://github.com/threestudio-project/threestudio/blob/main/README.md)

### Limitations

A research framework with substantial setup and optimization cost. Results can have inconsistent geometry or unseen surfaces. [Source 1](https://github.com/threestudio-project/threestudio/blob/main/README.md)

### Get the tool

- [Repository](https://github.com/threestudio-project/threestudio)
- [Documentation](https://github.com/threestudio-project/threestudio/blob/main/README.md)
- [License](https://github.com/threestudio-project/threestudio/blob/main/LICENSE)

## SuperSplat

3D, reconstruction & assets · Editing, captions & post-production · Browser tools & web media

Completed the detailed guide for an earlier screened discovery. Documentation and complete software license checked on 2026-10-06; no claim of a new release today.

### How it uses AI

Works specifically on learned Gaussian scene assets; it is the editing stage of an AI reconstruction workflow, not a trainer. [Source](https://github.com/playcanvas/supersplat/blob/main/README.md)

### Introduction

A browser editor for trained Gaussian-splat scenes. [Source 1](https://github.com/playcanvas/supersplat/blob/main/README.md)

### What it is good for

Cleaning up neural captures, selecting/removing unwanted splats and preparing interactive presentations. [Source 1](https://github.com/playcanvas/supersplat/blob/main/README.md)

### Demo & examples

A live editor is available at https://superspl.at/editor. [Source 1](https://superspl.at/editor)

### Install

Use the official route below; commands are documented instructions, not commands run during this review. [Source 1](https://github.com/playcanvas/supersplat/blob/main/README.md)

1. Open the official hosted editor for the simplest route.
2. For local development, install Node.js 20.19+ and clone the repository.
3. Install dependencies and start the development server.

```sh
npm install
```


```sh
npm run develop
```

### First project

Begin with a small example and review the result before expanding the project. [Source 1](https://github.com/playcanvas/supersplat/blob/main/README.md)

1. Import a supported Gaussian scene.
2. Trim unwanted regions, inspect viewpoints and export or publish through the documented workflow.
### Hardware & software

Requirements below reflect the cited documentation. Unreported minimums remain unknown. [Source 1](https://github.com/playcanvas/supersplat/blob/main/README.md)

- **Hardware:** Scene complexity determines memory pressure; no universal RAM, VRAM or disk minimum is documented.
- **Software:** A compatible browser; Node.js 20.19+ only for the local source route.
- **Platforms:** Browser-based editor. Do not infer support for every mobile browser or headset from that fact alone.

### License, model weights & costs

The complete top-level MIT software license was reviewed and archived. Keep dependent components and model terms separate. [Source 1](https://github.com/playcanvas/supersplat/blob/main/LICENSE) [Source 2](https://github.com/playcanvas/supersplat/blob/main/README.md)

- **Code:** MIT
- **Weights:** MIT editor; imported captures and model-derived assets retain their own rights.
- **Commercial:** The reviewed software license permits commercial software use subject to its obligations; it does not clear independent weights, data, assets, services or dependencies.
- **Cost:** Source code is available under the stated license. Hardware, electricity, storage and any optional or required hosted model/API services may add costs; no current service-price quote is asserted.

### Why it merits attention

Its documented workflow is relevant to cleaning up neural captures, selecting/removing unwanted splats and preparing interactive presentations. The sources provide a concrete implementation and setup path. This assessment is based on documentation and developer examples, not independent output or performance testing. [Source 1](https://github.com/playcanvas/supersplat/blob/main/README.md)

### Limitations

Does not reconstruct a scene from photos. Large captures can exceed browser/GPU limits. [Source 1](https://github.com/playcanvas/supersplat/blob/main/README.md)

### Get the tool

- [Repository](https://github.com/playcanvas/supersplat)
- [Documentation](https://superspl.at/editor)
- [License](https://github.com/playcanvas/supersplat/blob/main/LICENSE)

## 4D Gaussian Splatting

Photogrammetry, scanning & neural rendering · 3D, reconstruction & assets · Motion capture & character animation

Completed the detailed guide for an earlier screened discovery. Documentation and complete software license checked on 2026-10-06; no claim of a new release today.

### How it uses AI

Learns a dynamic neural scene representation rather than simply interpolating a conventional animation. [Source](https://github.com/hustvl/4DGaussians/blob/master/README.md) [Source](https://github.com/hustvl/4DGaussians/blob/master/.gitmodules)

### Introduction

A research implementation of dynamic Gaussian scene reconstruction. [Source 1](https://github.com/hustvl/4DGaussians/blob/master/README.md) [Source 2](https://github.com/hustvl/4DGaussians/blob/master/.gitmodules)

### What it is good for

Reconstructing time-varying captured scenes and rendering them from new viewpoints. [Source 1](https://github.com/hustvl/4DGaussians/blob/master/README.md) [Source 2](https://github.com/hustvl/4DGaussians/blob/master/.gitmodules)

### Demo & examples

The official 4DGS project page presents dynamic-scene renderings. [Source 1](https://guanjunwu.github.io/4dgs/index.html)

### Install

Use the official route below; commands are documented instructions, not commands run during this review. [Source 1](https://github.com/hustvl/4DGaussians/blob/master/README.md) [Source 2](https://github.com/hustvl/4DGaussians/blob/master/.gitmodules)

1. Clone the repository with its required submodules.
2. Follow the Python 3.7/PyTorch 1.13.1 CUDA environment and install the documented extensions.
3. Prepare a supported dataset and use its matching training configuration.
### First project

Begin with a small example and review the result before expanding the project. [Source 1](https://github.com/hustvl/4DGaussians/blob/master/README.md) [Source 2](https://github.com/hustvl/4DGaussians/blob/master/.gitmodules)

1. Start with the documented D-NeRF example.
2. Train, render the time sequence and inspect the supported per-frame export outputs.
### Hardware & software

Requirements below reflect the cited documentation. Unreported minimums remain unknown. [Source 1](https://github.com/hustvl/4DGaussians/blob/master/README.md) [Source 2](https://github.com/hustvl/4DGaussians/blob/master/.gitmodules)

- **Hardware:** No universal RAM, VRAM or storage minimum is documented; dataset and training configuration determine demand.
- **Software:** Legacy Python 3.7/PyTorch 1.13.1 with CUDA 11.6-oriented dependencies and compiled submodules.
- **Platforms:** Linux/CUDA-style setup is documented; native Mac/Windows support is not established.

### License, model weights & costs

The complete top-level Apache-2.0 software license was reviewed and archived. Keep dependent components and model terms separate. [Source 1](https://github.com/hustvl/4DGaussians/blob/master/LICENSE.md) [Source 2](https://github.com/hustvl/4DGaussians/blob/master/README.md) [Source 3](https://github.com/hustvl/4DGaussians/blob/master/.gitmodules)

- **Code:** Apache-2.0
- **Weights:** Apache-2.0 top-level code. INRIA-derived rasterization and other submodules have separate terms that must be reviewed before commercial deployment.
- **Commercial:** The reviewed software license permits commercial software use subject to its obligations; it does not clear independent weights, data, assets, services or dependencies.
- **Cost:** Source code is available under the stated license. Hardware, electricity, storage and any optional or required hosted model/API services may add costs; no current service-price quote is asserted.

### Why it merits attention

Its documented workflow is relevant to reconstructing time-varying captured scenes and rendering them from new viewpoints. The sources provide a concrete implementation and setup path. This assessment is based on documentation and developer examples, not independent output or performance testing. [Source 1](https://github.com/hustvl/4DGaussians/blob/master/README.md) [Source 2](https://github.com/hustvl/4DGaussians/blob/master/.gitmodules)

### Limitations

Top-level Apache licensing does not settle dependency rights. Reproduction involves an older compiled environment and author examples were not tested. [Source 1](https://github.com/hustvl/4DGaussians/blob/master/README.md) [Source 2](https://github.com/hustvl/4DGaussians/blob/master/.gitmodules)

### Get the tool

- [Repository](https://github.com/hustvl/4DGaussians)
- [Documentation](https://guanjunwu.github.io/4dgs/index.html)
- [License](https://github.com/hustvl/4DGaussians/blob/master/LICENSE.md)

## 3DGRUT

Photogrammetry, scanning & neural rendering · Spatial audio & volumetric media · VFX, compositing & relighting

Completed the detailed guide for an earlier screened discovery. Documentation and complete software license checked on 2026-10-06; no claim of a new release today.

### How it uses AI

Learns Gaussian scene representations and renders them with techniques designed for flexible camera/ray models. [Source](https://github.com/nv-tlabs/3dgrut/blob/main/README.md)

### Introduction

Gaussian rendering and training tools supporting ray-tracing and rasterization-oriented approaches. [Source 1](https://github.com/nv-tlabs/3dgrut/blob/main/README.md)

### What it is good for

Researching neural captures with distorted cameras, rolling shutter and richer rendering effects. [Source 1](https://github.com/nv-tlabs/3dgrut/blob/main/README.md)

### Demo & examples

NVIDIA Research publishes project examples for 3DGRT and related methods. [Source 1](https://research.nvidia.com/labs/toronto-ai/3DGRT)

### Install

Use the official route below; commands are documented instructions, not commands run during this review. [Source 1](https://github.com/nv-tlabs/3dgrut/blob/main/README.md)

1. Clone the repository recursively.
2. Use the documented uv environment script for Linux or Windows.
3. Install matching CUDA/build prerequisites and download a supported sample dataset.

```sh
./install_env_uv.sh
```


```sh
python train.py --config-name apps/nerf_synthetic_3dgut.yaml path=data/nerf_synthetic/lego out_dir=runs experiment_name=lego_3dgut
```

### First project

Begin with a small example and review the result before expanding the project. [Source 1](https://github.com/nv-tlabs/3dgrut/blob/main/README.md)

1. Train the provided Lego configuration.
2. Inspect the rendered views before switching camera models or more complex captures.
### Hardware & software

Requirements below reflect the cited documentation. Unreported minimums remain unknown. [Source 1](https://github.com/nv-tlabs/3dgrut/blob/main/README.md)

- **Hardware:** NVIDIA CUDA GPU required; RT cores are recommended for ray tracing. RAM/VRAM/storage minima are not published as universal values.
- **Software:** Documented CUDA versions include 11.8 and 12.x, with 12.8 needed for RTX 50-series; Windows build tools or Linux graphics headers apply.
- **Platforms:** Linux and Windows setup scripts are documented. Native macOS is not a documented inference/training route.

### License, model weights & costs

The complete top-level Apache-2.0 software license was reviewed and archived. Keep dependent components and model terms separate. [Source 1](https://github.com/nv-tlabs/3dgrut/blob/main/LICENSE) [Source 2](https://github.com/nv-tlabs/3dgrut/blob/main/README.md)

- **Code:** Apache-2.0
- **Weights:** Apache-2.0 project code; datasets, drivers and dependent packages retain separate terms.
- **Commercial:** The reviewed software license permits commercial software use subject to its obligations; it does not clear independent weights, data, assets, services or dependencies.
- **Cost:** Source code is available under the stated license. Hardware, electricity, storage and any optional or required hosted model/API services may add costs; no current service-price quote is asserted.

### Why it merits attention

Its documented workflow is relevant to researching neural captures with distorted cameras, rolling shutter and richer rendering effects. The sources provide a concrete implementation and setup path. This assessment is based on documentation and developer examples, not independent output or performance testing. [Source 1](https://github.com/nv-tlabs/3dgrut/blob/main/README.md)

### Limitations

Different rendering modes have different hardware/performance tradeoffs. Advanced effects in research examples are not a guarantee for arbitrary captures. [Source 1](https://github.com/nv-tlabs/3dgrut/blob/main/README.md)

### Get the tool

- [Repository](https://github.com/nv-tlabs/3dgrut)
- [Documentation](https://research.nvidia.com/labs/toronto-ai/3DGRT)
- [License](https://github.com/nv-tlabs/3dgrut/blob/main/LICENSE)

## JoyAI Video Edit

Video, animation & film · Editing, captions & post-production · Interactive, immersive & live media

Completed the detailed guide for an earlier screened discovery. Documentation and complete software license checked on 2026-10-06; no claim of a new release today.

### How it uses AI

A 16B causal video model transforms frames according to text instructions and accompanying control components. [Source](https://github.com/jd-opensource/JoyAI-Video-Edit/blob/main/README.md) [Source](https://github.com/jd-opensource/JoyAI-Video-Edit/blob/main/DEPLOYMENT.md)

### Introduction

A large instruction-guided video editing system with a streaming inference pipeline. [Source 1](https://github.com/jd-opensource/JoyAI-Video-Edit/blob/main/README.md) [Source 2](https://github.com/jd-opensource/JoyAI-Video-Edit/blob/main/DEPLOYMENT.md)

### What it is good for

Experimenting with prompt-directed live/video transformations on high-end NVIDIA hardware. [Source 1](https://github.com/jd-opensource/JoyAI-Video-Edit/blob/main/README.md) [Source 2](https://github.com/jd-opensource/JoyAI-Video-Edit/blob/main/DEPLOYMENT.md)

### Demo & examples

The official README links its Hugging Face demonstration and recorded examples. [Source 1](https://github.com/jd-opensource/JoyAI-Video-Edit/blob/main/README.md)

### Install

Use the official route below; commands are documented instructions, not commands run during this review. [Source 1](https://github.com/jd-opensource/JoyAI-Video-Edit/blob/main/README.md) [Source 2](https://github.com/jd-opensource/JoyAI-Video-Edit/blob/main/DEPLOYMENT.md)

1. Follow DEPLOYMENT.md in a Python 3.10 environment.
2. Install the GPU-specific attention and custom operation builds; RTX 5090 and B200 instructions differ.
3. Download the checkpoints and configure required vision-language components before launching the documented server.
### First project

Begin with a small example and review the result before expanding the project. [Source 1](https://github.com/jd-opensource/JoyAI-Video-Edit/blob/main/README.md) [Source 2](https://github.com/jd-opensource/JoyAI-Video-Edit/blob/main/DEPLOYMENT.md)

1. Begin with the official launch configuration and short input.
2. Measure frame rate/latency and inspect temporal artifacts before attempting a live performance.
### Hardware & software

Requirements below reflect the cited documentation. Unreported minimums remain unknown. [Source 1](https://github.com/jd-opensource/JoyAI-Video-Edit/blob/main/README.md) [Source 2](https://github.com/jd-opensource/JoyAI-Video-Edit/blob/main/DEPLOYMENT.md)

- **Hardware:** Author demonstration: RTX 5090 with 32 GB VRAM at 840×480 and around 24 FPS. Checkpoint directory is roughly 51 GB, plus build/cache space; RAM minimum is not stated.
- **Software:** Python 3.10, CUDA >=12.8 for the documented 5090 route, custom CUDA extensions and required MiMo-VL component; optional detector files affect gating features.
- **Platforms:** Linux/CUDA deployment is documented. Native macOS/Windows support is not established.

### License, model weights & costs

The complete top-level Apache-2.0 software license was reviewed and archived. Keep dependent components and model terms separate. [Source 1](https://github.com/jd-opensource/JoyAI-Video-Edit/blob/main/LICENSE) [Source 2](https://github.com/jd-opensource/JoyAI-Video-Edit/blob/main/README.md) [Source 3](https://github.com/jd-opensource/JoyAI-Video-Edit/blob/main/DEPLOYMENT.md)

- **Code:** Apache-2.0
- **Weights:** Apache-2.0 application code. Model and auxiliary-component terms must be assessed separately before production use.
- **Commercial:** The reviewed software license permits commercial software use subject to its obligations; it does not clear independent weights, data, assets, services or dependencies.
- **Cost:** Source code is available under the stated license. Hardware, electricity, storage and any optional or required hosted model/API services may add costs; no current service-price quote is asserted.

### Why it merits attention

Its documented workflow is relevant to experimenting with prompt-directed live/video transformations on high-end NVIDIA hardware. The sources provide a concrete implementation and setup path. This assessment is based on documentation and developer examples, not independent output or performance testing. [Source 1](https://github.com/jd-opensource/JoyAI-Video-Edit/blob/main/README.md) [Source 2](https://github.com/jd-opensource/JoyAI-Video-Edit/blob/main/DEPLOYMENT.md)

### Limitations

The published GPU demonstration is not a universal real-time guarantee. Missing optional detector assets change behavior; installation requires careful version matching. [Source 1](https://github.com/jd-opensource/JoyAI-Video-Edit/blob/main/README.md) [Source 2](https://github.com/jd-opensource/JoyAI-Video-Edit/blob/main/DEPLOYMENT.md)

### Get the tool

- [Repository](https://github.com/jd-opensource/JoyAI-Video-Edit)
- [Documentation](https://github.com/jd-opensource/JoyAI-Video-Edit/blob/main/README.md)
- [License](https://github.com/jd-opensource/JoyAI-Video-Edit/blob/main/LICENSE)

## X-AnyLabeling

Editing, captions & post-production · Video, animation & film · Images & design · Photogrammetry, scanning & neural rendering

Completed the detailed guide for an earlier screened discovery. Documentation and complete software license checked on 2026-10-06; no claim of a new release today.

### How it uses AI

Integrates learned detection, segmentation, tracking and recognition models into an editable annotation workflow. [Source](https://github.com/CVHub520/X-AnyLabeling/blob/main/README.md) [Source](https://github.com/CVHub520/X-AnyLabeling/blob/main/docs/en/get_started.md)

### Introduction

A desktop annotation environment with AI-assisted masks, tracking, OCR and multimodal tools. [Source 1](https://github.com/CVHub520/X-AnyLabeling/blob/main/README.md) [Source 2](https://github.com/CVHub520/X-AnyLabeling/blob/main/docs/en/get_started.md)

### What it is good for

Preparing creative datasets, extracting object regions, annotating footage and correcting machine-proposed labels. [Source 1](https://github.com/CVHub520/X-AnyLabeling/blob/main/README.md) [Source 2](https://github.com/CVHub520/X-AnyLabeling/blob/main/docs/en/get_started.md)

### Demo & examples

The official README and user guide show image/video and newer point-cloud tools. [Source 1](https://github.com/CVHub520/X-AnyLabeling/blob/main/README.md)

### Install

Use the official route below; commands are documented instructions, not commands run during this review. [Source 1](https://github.com/CVHub520/X-AnyLabeling/blob/main/README.md) [Source 2](https://github.com/CVHub520/X-AnyLabeling/blob/main/docs/en/get_started.md)

1. Choose an official packaged release or use the documented Python installation.
2. Select CPU or the matching CUDA extra; some advanced capabilities require source installation.
3. Run the documented dependency check before loading a model.

```sh
pip install "x-anylabeling-cvhub[cpu]"
```


```sh
xanylabeling checks
```

### First project

Begin with a small example and review the result before expanding the project. [Source 1](https://github.com/CVHub520/X-AnyLabeling/blob/main/README.md) [Source 2](https://github.com/CVHub520/X-AnyLabeling/blob/main/docs/en/get_started.md)

1. Open a small image set and select a supported segmentation model.
2. Generate masks, manually correct boundaries and export the chosen annotation format.
### Hardware & software

Requirements below reflect the cited documentation. Unreported minimums remain unknown. [Source 1](https://github.com/CVHub520/X-AnyLabeling/blob/main/README.md) [Source 2](https://github.com/CVHub520/X-AnyLabeling/blob/main/docs/en/get_started.md)

- **Hardware:** CPU and GPU options exist; minimum RAM/VRAM/storage depends on the selected model and is not universally specified.
- **Software:** Python 3.11–3.13 for the source/package route, with 3.12 recommended; use matching CUDA 11/12/13 dependencies when applicable.
- **Platforms:** Windows, macOS and Linux CPU routes; Windows/Linux CUDA routes are documented.

### License, model weights & costs

The complete top-level GPL-3.0 software license was reviewed and archived. Keep dependent components and model terms separate. [Source 1](https://github.com/CVHub520/X-AnyLabeling/blob/main/LICENSE) [Source 2](https://github.com/CVHub520/X-AnyLabeling/blob/main/README.md) [Source 3](https://github.com/CVHub520/X-AnyLabeling/blob/main/docs/en/get_started.md)

- **Code:** GPL-3.0
- **Weights:** GPL-3.0 software. Downloaded model weights and optional external providers have separate terms.
- **Commercial:** The reviewed software license permits commercial software use subject to its obligations; it does not clear independent weights, data, assets, services or dependencies.
- **Cost:** Source code is available under the stated license. Hardware, electricity, storage and any optional or required hosted model/API services may add costs; no current service-price quote is asserted.

### Why it merits attention

Its documented workflow is relevant to preparing creative datasets, extracting object regions, annotating footage and correcting machine-proposed labels. The sources provide a concrete implementation and setup path. This assessment is based on documentation and developer examples, not independent output or performance testing. [Source 1](https://github.com/CVHub520/X-AnyLabeling/blob/main/README.md) [Source 2](https://github.com/CVHub520/X-AnyLabeling/blob/main/docs/en/get_started.md)

### Limitations

Packaged releases can lag source-only features. AI-generated masks and labels require human review. [Source 1](https://github.com/CVHub520/X-AnyLabeling/blob/main/README.md) [Source 2](https://github.com/CVHub520/X-AnyLabeling/blob/main/docs/en/get_started.md)

### Get the tool

- [Repository](https://github.com/CVHub520/X-AnyLabeling)
- [Documentation](https://github.com/CVHub520/X-AnyLabeling/blob/main/README.md)
- [License](https://github.com/CVHub520/X-AnyLabeling/blob/main/LICENSE)

## ScanScore

AI music notation and score recovery · Audio, music & voice · Archives, media restoration & collections

Completed the detailed guide for an earlier screened discovery. Documentation and complete software license checked on 2026-10-06; no claim of a new release today.

### How it uses AI

Combines optical music recognition, neural RapidOCR text recognition and optional Ollama instrument-name interpretation. [Source](https://github.com/Rockman6/ScanScore/blob/master/README.md)

### Introduction

An Audiveris-based score-recognition application with newer OCR and optional language-model assistance. [Source 1](https://github.com/Rockman6/ScanScore/blob/master/README.md)

### What it is good for

Turning printed sheet music into editable MusicXML/MIDI while correcting multilingual labels. [Source 1](https://github.com/Rockman6/ScanScore/blob/master/README.md)

### Demo & examples

The official README describes score import, correction and export; no independently tested demo is claimed. [Source 1](https://github.com/Rockman6/ScanScore/blob/master/README.md)

### Install

Use the official route below; commands are documented instructions, not commands run during this review. [Source 1](https://github.com/Rockman6/ScanScore/blob/master/README.md)

1. Clone the canonical Rockman6/ScanScore repository; the README clone example contains a placeholder owner.
2. Install Java 21+ and use its Gradle wrapper.
3. Add Python/RapidOCR and a local Ollama model only for the optional enhanced features.

```sh
./gradlew :app:run
```

### First project

Begin with a small example and review the result before expanding the project. [Source 1](https://github.com/Rockman6/ScanScore/blob/master/README.md)

1. Import one clean score page.
2. Check notes and instrument names, correct errors and export MusicXML or MIDI.
### Hardware & software

Requirements below reflect the cited documentation. Unreported minimums remain unknown. [Source 1](https://github.com/Rockman6/ScanScore/blob/master/README.md)

- **Hardware:** RapidOCR resources are described at roughly 300 MB. RAM/VRAM/disk minima for the whole application and optional LLM are not documented.
- **Software:** Java 21+, Gradle wrapper; optional Python 3.11/RapidOCR and Ollama qwen2.5:7B.
- **Platforms:** Windows, macOS and Linux are documented.

### License, model weights & costs

The complete top-level AGPL-3.0 software license was reviewed and archived. Keep dependent components and model terms separate. [Source 1](https://github.com/Rockman6/ScanScore/blob/master/LICENSE) [Source 2](https://github.com/Rockman6/ScanScore/blob/master/README.md)

- **Code:** AGPL-3.0
- **Weights:** AGPL-3.0 application; OCR and language-model packages/weights remain separately licensed.
- **Commercial:** The reviewed software license permits commercial software use subject to its obligations; it does not clear independent weights, data, assets, services or dependencies. AGPL obligations can apply when modified software is made available over a network.
- **Cost:** Source code is available under the stated license. Hardware, electricity, storage and any optional or required hosted model/API services may add costs; no current service-price quote is asserted.

### Why it merits attention

Its documented workflow is relevant to turning printed sheet music into editable MusicXML/MIDI while correcting multilingual labels. The sources provide a concrete implementation and setup path. This assessment is based on documentation and developer examples, not independent output or performance testing. [Source 1](https://github.com/Rockman6/ScanScore/blob/master/README.md)

### Limitations

An evolving fork; score interpretation is not guaranteed and requires proofreading. The placeholder clone instruction needs the canonical repository substituted. [Source 1](https://github.com/Rockman6/ScanScore/blob/master/README.md)

### Get the tool

- [Repository](https://github.com/Rockman6/ScanScore)
- [Documentation](https://github.com/Rockman6/ScanScore/blob/master/README.md)
- [License](https://github.com/Rockman6/ScanScore/blob/master/LICENSE)

## oemer

AI music notation and score recovery · Audio, music & voice · Archives, media restoration & collections

Completed the detailed guide for an earlier screened discovery. Documentation and complete software license checked on 2026-10-06; no claim of a new release today.

### How it uses AI

Neural segmentation and recognition stages extract musical symbols and reconstruct score structure. [Source](https://github.com/BreezeWhite/oemer/blob/main/README.md)

### Introduction

A neural optical-music-recognition pipeline for printed score images. [Source 1](https://github.com/BreezeWhite/oemer/blob/main/README.md)

### What it is good for

Recovering editable MusicXML from photographed or scanned Western sheet music. [Source 1](https://github.com/BreezeWhite/oemer/blob/main/README.md)

### Demo & examples

The official README includes sample inputs/outputs and a Colab route. [Source 1](https://pypi.org/project/oemer/)

### Install

Use the official route below; commands are documented instructions, not commands run during this review. [Source 1](https://github.com/BreezeWhite/oemer/blob/main/README.md)

1. Install the Python package.
2. Allow the documented first-run model download.
3. Use the default ONNX Runtime backend or the separately documented TensorFlow option.

```sh
pip install oemer
```


```sh
oemer score.png
```

### First project

Begin with a small example and review the result before expanding the project. [Source 1](https://github.com/BreezeWhite/oemer/blob/main/README.md)

1. Try a single clear printed score image.
2. Inspect the annotated result and MusicXML in notation software, correcting recognition errors.
### Hardware & software

Requirements below reflect the cited documentation. Unreported minimums remain unknown. [Source 1](https://github.com/BreezeWhite/oemer/blob/main/README.md)

- **Hardware:** RAM, VRAM and storage minimums are not published. Author runtime examples are not universal guarantees.
- **Software:** Python package with ONNX Runtime by default; optional TensorFlow backend and image-processing dependencies.
- **Platforms:** A Python/Colab route is documented; a complete tested desktop OS matrix is not provided.

### License, model weights & costs

The complete top-level MIT software license was reviewed and archived. Keep dependent components and model terms separate. [Source 1](https://github.com/BreezeWhite/oemer/blob/main/LICENSE) [Source 2](https://github.com/BreezeWhite/oemer/blob/main/README.md)

- **Code:** MIT
- **Weights:** MIT source code; downloaded model assets require their own terms to be verified for the intended use.
- **Commercial:** The reviewed software license permits commercial software use subject to its obligations; it does not clear independent weights, data, assets, services or dependencies.
- **Cost:** Source code is available under the stated license. Hardware, electricity, storage and any optional or required hosted model/API services may add costs; no current service-price quote is asserted.

### Why it merits attention

Its documented workflow is relevant to recovering editable MusicXML from photographed or scanned Western sheet music. The sources provide a concrete implementation and setup path. This assessment is based on documentation and developer examples, not independent output or performance testing. [Source 1](https://github.com/BreezeWhite/oemer/blob/main/README.md)

### Limitations

Handwritten and non-Western notation are outside the stated scope. Deskewing can fail and a documented bypass may be needed. [Source 1](https://github.com/BreezeWhite/oemer/blob/main/README.md)

### Get the tool

- [Repository](https://github.com/BreezeWhite/oemer)
- [Documentation](https://pypi.org/project/oemer/)
- [License](https://github.com/BreezeWhite/oemer/blob/main/LICENSE)

## Polyphonic TrOMR

AI music notation and score recovery · Audio, music & voice · Computational art & creative coding

Completed the detailed guide for an earlier screened discovery. Documentation and complete software license checked on 2026-10-06; no claim of a new release today.

### How it uses AI

An optical-music-recognition Transformer predicts structured score content from image inputs. [Source](https://github.com/NetEase/Polyphonic-TrOMR/blob/master/README.md)

### Introduction

A Transformer-based research implementation for recognizing polyphonic sheet music. [Source 1](https://github.com/NetEase/Polyphonic-TrOMR/blob/master/README.md)

### What it is good for

Studying how photographed score images can become symbolic musical representations. [Source 1](https://github.com/NetEase/Polyphonic-TrOMR/blob/master/README.md)

### Demo & examples

The README provides example photographs and recognition outputs. [Source 1](https://github.com/NetEase/Polyphonic-TrOMR/blob/master/README.md)

### Install

Use the official route below; commands are documented instructions, not commands run during this review. [Source 1](https://github.com/NetEase/Polyphonic-TrOMR/blob/master/README.md)

1. Clone the official repository and install its listed requirements.
2. Obtain the documented inference resources and start with a bundled example.

```sh
pip install -r requirements.txt
```


```sh
python ./tromr/inference.py ./examples/photo4.jpg
```

### First project

Begin with a small example and review the result before expanding the project. [Source 1](https://github.com/NetEase/Polyphonic-TrOMR/blob/master/README.md)

1. Run the provided photograph example.
2. Compare the recognized content against the page before trying a personal score image.
### Hardware & software

Requirements below reflect the cited documentation. Unreported minimums remain unknown. [Source 1](https://github.com/NetEase/Polyphonic-TrOMR/blob/master/README.md)

- **Hardware:** Minimum RAM, VRAM and free disk space are not documented.
- **Software:** Python and repository requirements; exact supported Python/OS versions are not fully specified in the reviewed overview.
- **Platforms:** No complete tested Windows/macOS/Linux support matrix is provided.

### License, model weights & costs

The complete top-level Apache-2.0 software license was reviewed and archived. Keep dependent components and model terms separate. [Source 1](https://github.com/NetEase/Polyphonic-TrOMR/blob/master/LICENSE) [Source 2](https://github.com/NetEase/Polyphonic-TrOMR/blob/master/README.md)

- **Code:** Apache-2.0
- **Weights:** Apache-2.0 code; model and training-data terms are not fully established by the top-level software license.
- **Commercial:** The reviewed software license permits commercial software use subject to its obligations; it does not clear independent weights, data, assets, services or dependencies.
- **Cost:** Source code is available under the stated license. Hardware, electricity, storage and any optional or required hosted model/API services may add costs; no current service-price quote is asserted.

### Why it merits attention

Its documented workflow is relevant to studying how photographed score images can become symbolic musical representations. The sources provide a concrete implementation and setup path. This assessment is based on documentation and developer examples, not independent output or performance testing. [Source 1](https://github.com/NetEase/Polyphonic-TrOMR/blob/master/README.md)

### Limitations

Research inference code, not a finished notation editor. Training availability and real-world score coverage require further evaluation. [Source 1](https://github.com/NetEase/Polyphonic-TrOMR/blob/master/README.md)

### Get the tool

- [Repository](https://github.com/NetEase/Polyphonic-TrOMR)
- [Documentation](https://github.com/NetEase/Polyphonic-TrOMR/blob/master/README.md)
- [License](https://github.com/NetEase/Polyphonic-TrOMR/blob/master/LICENSE)

## PuppetStudio

Avatars, digital humans & lip sync · Video, animation & film · Storyboarding, narrative & comics

Completed the detailed guide for an earlier screened discovery. The repository falls within the discovery window, but this is not independent evidence of its launch date. Documentation and complete software license checked on 2026-10-06; no claim of a new release today.

### How it uses AI

Combines speech transcription, image/anatomy analysis and SadTalker-based facial animation. [Source](https://github.com/well-noted/PuppetStudio/blob/main/README.md) [Source](https://github.com/well-noted/PuppetStudio/blob/main/docs/DEPENDENCIES.md)

### Introduction

A public-alpha workflow that turns recordings and illustrated characters into short speaking clips. [Source 1](https://github.com/well-noted/PuppetStudio/blob/main/README.md) [Source 2](https://github.com/well-noted/PuppetStudio/blob/main/docs/DEPENDENCIES.md)

### What it is good for

Building simple narrated puppet videos with transcription, character anatomy and lip-sync rendering. [Source 1](https://github.com/well-noted/PuppetStudio/blob/main/README.md) [Source 2](https://github.com/well-noted/PuppetStudio/blob/main/docs/DEPENDENCIES.md)

### Demo & examples

The official README links a short rendered example and setup documentation. [Source 1](https://github.com/well-noted/PuppetStudio/blob/main/README.md)

### Install

Use the official route below; commands are documented instructions, not commands run during this review. [Source 1](https://github.com/well-noted/PuppetStudio/blob/main/README.md) [Source 2](https://github.com/well-noted/PuppetStudio/blob/main/docs/DEPENDENCIES.md)

1. Use the documented Windows release/launcher route.
2. Allow its local runtime setup and obtain the separately listed model assets.
3. Check disk space and NVIDIA driver compatibility before enabling neural rendering.

```sh
launch.cmd
```

### First project

Begin with a small example and review the result before expanding the project. [Source 1](https://github.com/well-noted/PuppetStudio/blob/main/README.md) [Source 2](https://github.com/well-noted/PuppetStudio/blob/main/docs/DEPENDENCIES.md)

1. Import audio and transcribe it, then select a short passage.
2. Import character artwork, approve anatomy and render a short speaking preview before a full clip.
### Hardware & software

Requirements below reflect the cited documentation. Unreported minimums remain unknown. [Source 1](https://github.com/well-noted/PuppetStudio/blob/main/README.md) [Source 2](https://github.com/well-noted/PuppetStudio/blob/main/docs/DEPENDENCIES.md)

- **Hardware:** At least 15 GiB free storage is documented. A low-memory NVIDIA path targets 4 GB VRAM with 256-pixel/batch-1 settings; it is not a guarantee for all scenes. System RAM minimum is not stated.
- **Software:** Python 3.10–3.12 or the managed bootstrap; transcription, MediaPipe/SadTalker and media dependencies.
- **Platforms:** Windows x64 is the primary route. Manual macOS/Linux Studio setup exists, but neural rendering there is not validated in the documentation.

### License, model weights & costs

The complete top-level MIT software license was reviewed and archived. Keep dependent components and model terms separate. [Source 1](https://github.com/well-noted/PuppetStudio/blob/main/LICENSE) [Source 2](https://github.com/well-noted/PuppetStudio/blob/main/README.md) [Source 3](https://github.com/well-noted/PuppetStudio/blob/main/docs/DEPENDENCIES.md)

- **Code:** MIT
- **Weights:** MIT application; SadTalker, model weights and media components have separate notices. Optional external services have their own terms/costs.
- **Commercial:** The reviewed software license permits commercial software use subject to its obligations; it does not clear independent weights, data, assets, services or dependencies.
- **Cost:** Source code is available under the stated license. Hardware, electricity, storage and any optional or required hosted model/API services may add costs; no current service-price quote is asserted.

### Why it merits attention

Its documented workflow is relevant to building simple narrated puppet videos with transcription, character anatomy and lip-sync rendering. The sources provide a concrete implementation and setup path. This assessment is based on documentation and developer examples, not independent output or performance testing. [Source 1](https://github.com/well-noted/PuppetStudio/blob/main/README.md) [Source 2](https://github.com/well-noted/PuppetStudio/blob/main/docs/DEPENDENCIES.md)

### Limitations

Fresh-machine end-to-end installation is not fully validated by the project. CPU lip-sync is not provided; non-GPU operation is limited to other parts of the workflow. [Source 1](https://github.com/well-noted/PuppetStudio/blob/main/README.md) [Source 2](https://github.com/well-noted/PuppetStudio/blob/main/docs/DEPENDENCIES.md)

### Get the tool

- [Repository](https://github.com/well-noted/PuppetStudio)
- [Documentation](https://github.com/well-noted/PuppetStudio/blob/main/README.md)
- [License](https://github.com/well-noted/PuppetStudio/blob/main/LICENSE)

## FireRed OpenStoryline

Editing, captions & post-production · Video, animation & film · Storyboarding, narrative & comics · AI agents for code-authored media production

Completed the detailed guide for an earlier screened discovery. Documentation and complete software license checked on 2026-10-06; no claim of a new release today.

### How it uses AI

Language/vision models interpret source media and instructions while agent tools assemble and revise the edit. [Source](https://github.com/FireRedTeam/FireRed-OpenStoryline/blob/main/README.md)

### Introduction

A conversational video-production workflow for organizing media, drafting narration and revising edits. [Source 1](https://github.com/FireRedTeam/FireRed-OpenStoryline/blob/main/README.md)

### What it is good for

Building a short themed video, aligning music and voiceover, then reusing an editing style with different footage. [Source 1](https://github.com/FireRedTeam/FireRed-OpenStoryline/blob/main/README.md)

### Demo & examples

The official project demo page shows example workflows and links hosted demonstrations. [Source 1](https://fireredteam.github.io/demos/firered_openstoryline/)

### Install

Use the official route below; commands are documented instructions, not commands run during this review. [Source 1](https://github.com/FireRedTeam/FireRed-OpenStoryline/blob/main/README.md)

1. Create the documented Python 3.11 environment.
2. Follow the platform build instructions and configure model providers in private local settings.
3. Start the tool server and CLI or web interface as documented.

```sh
PYTHONPATH=src python -m open_storyline.mcp.server
```


```sh
uvicorn agent_fastapi:app --host 127.0.0.1 --port 8005
```

### First project

Begin with a small example and review the result before expanding the project. [Source 1](https://github.com/FireRedTeam/FireRed-OpenStoryline/blob/main/README.md)

1. Provide a small set of media you can use and a clear story brief.
2. Review the suggested script, media choices and timing; refine the edit conversationally before export.
### Hardware & software

Requirements below reflect the cited documentation. Unreported minimums remain unknown. [Source 1](https://github.com/FireRedTeam/FireRed-OpenStoryline/blob/main/README.md)

- **Hardware:** RAM, VRAM and disk minimums are not documented; local models and media rendering add separate resource needs.
- **Software:** Python 3.11, media/build dependencies and configured AI provider credentials; source instructions include a Windows-specific route.
- **Platforms:** macOS/Linux setup and separate Windows instructions are provided.

### License, model weights & costs

The complete top-level Apache-2.0 software license was reviewed and archived. Keep dependent components and model terms separate. [Source 1](https://github.com/FireRedTeam/FireRed-OpenStoryline/blob/main/LICENSE) [Source 2](https://github.com/FireRedTeam/FireRed-OpenStoryline/blob/main/README.md)

- **Code:** Apache-2.0
- **Weights:** Apache-2.0 code. Hosted models, retrieved media, music and fonts have independent rights and potentially paid usage.
- **Commercial:** The reviewed software license permits commercial software use subject to its obligations; it does not clear independent weights, data, assets, services or dependencies.
- **Cost:** Source code is available under the stated license. Hardware, electricity, storage and any optional or required hosted model/API services may add costs; no current service-price quote is asserted.

### Why it merits attention

Its documented workflow is relevant to building a short themed video, aligning music and voiceover, then reusing an editing style with different footage. The sources provide a concrete implementation and setup path. This assessment is based on documentation and developer examples, not independent output or performance testing. [Source 1](https://github.com/FireRedTeam/FireRed-OpenStoryline/blob/main/README.md)

### Limitations

Provider calls can accumulate cost. Suggested or downloaded media is not automatically cleared for publication; every generated edit needs review. [Source 1](https://github.com/FireRedTeam/FireRed-OpenStoryline/blob/main/README.md)

### Get the tool

- [Repository](https://github.com/FireRedTeam/FireRed-OpenStoryline)
- [Documentation](https://fireredteam.github.io/demos/firered_openstoryline/)
- [License](https://github.com/FireRedTeam/FireRed-OpenStoryline/blob/main/LICENSE)

## OpenSpatial

Audio, music & voice · Spatial audio & volumetric media · Accessible media & assistive creation

Completed the detailed guide for an earlier screened discovery. The repository falls within the discovery window, but this is not independent evidence of its launch date. Documentation and complete software license checked on 2026-10-06; no claim of a new release today.

### How it uses AI

A Core ML HTDemucs component separates source content for the AI surround workflow. [Source](https://github.com/dortanes/openspatial/blob/main/README.md)

### Introduction

A Mac audio application for headphone surround processing, including AI-assisted source separation. [Source 1](https://github.com/dortanes/openspatial/blob/main/README.md)

### What it is good for

Listening to or prototyping spatial audio with a centered vocal channel and optional camera-based head tracking. [Source 1](https://github.com/dortanes/openspatial/blob/main/README.md)

### Demo & examples

The official README shows the application and explains the surround/head-tracking modes. [Source 1](https://github.com/dortanes/openspatial/blob/main/README.md)

### Install

Use the official route below; commands are documented instructions, not commands run during this review. [Source 1](https://github.com/dortanes/openspatial/blob/main/README.md)

1. Download the official Apple Silicon release and move it to Applications.
2. Follow the audio-driver installation flow and required local permissions.
3. Select headphones and download the AI model when choosing the AI surround mode.
### First project

Begin with a small example and review the result before expanding the project. [Source 1](https://github.com/dortanes/openspatial/blob/main/README.md)

1. Choose a headphone output and test a familiar audio track.
2. Compare processing modes and enable camera head tracking only if needed.
### Hardware & software

Requirements below reflect the cited documentation. Unreported minimums remain unknown. [Source 1](https://github.com/dortanes/openspatial/blob/main/README.md)

- **Hardware:** Apple Silicon required. RAM, VRAM and storage minimums are not specified; a camera is needed only for visual head tracking.
- **Software:** macOS 15+ and the audio driver; Xcode 26+ and uv are listed for source building.
- **Platforms:** Apple Silicon macOS. Windows/Linux native operation is not documented.

### License, model weights & costs

The complete top-level GPL-3.0 software license was reviewed and archived. Keep dependent components and model terms separate. [Source 1](https://github.com/dortanes/openspatial/blob/main/LICENSE) [Source 2](https://github.com/dortanes/openspatial/blob/main/README.md)

- **Code:** GPL-3.0
- **Weights:** GPL-3.0 application; notices list HTDemucs MIT, BlackHole GPL-3.0 and room impulses CC-BY-SA-3.0.
- **Commercial:** The reviewed software license permits commercial software use subject to its obligations; it does not clear independent weights, data, assets, services or dependencies.
- **Cost:** Source code is available under the stated license. Hardware, electricity, storage and any optional or required hosted model/API services may add costs; no current service-price quote is asserted.

### Why it merits attention

Its documented workflow is relevant to listening to or prototyping spatial audio with a centered vocal channel and optional camera-based head tracking. The sources provide a concrete implementation and setup path. This assessment is based on documentation and developer examples, not independent output or performance testing. [Source 1](https://github.com/dortanes/openspatial/blob/main/README.md)

### Limitations

Spatial rendering and source separation can introduce artifacts. Support for games through Mac compatibility layers is not a Windows release. [Source 1](https://github.com/dortanes/openspatial/blob/main/README.md)

### Get the tool

- [Repository](https://github.com/dortanes/openspatial)
- [Documentation](https://github.com/dortanes/openspatial/blob/main/README.md)
- [License](https://github.com/dortanes/openspatial/blob/main/LICENSE)

## YuE2 Turbo

Audio, music & voice · Performance, projection & stage media · Emerging & cross-disciplinary creative AI

Completed the detailed guide for an earlier screened discovery. The repository falls within the discovery window, but this is not independent evidence of its launch date. Documentation and complete software license checked on 2026-10-06; no claim of a new release today.

### How it uses AI

Keeps the YuE2 model resident and uses a batched inference stack to generate music from structured prompts. [Source](https://github.com/NoizAI/YuE2-Turbo/blob/main/README.md) [Source](https://github.com/NoizAI/YuE2-Turbo/blob/main/MODEL_LICENSE)

### Introduction

An inference server and browser studio for accelerated YuE2 music generation. [Source 1](https://github.com/NoizAI/YuE2-Turbo/blob/main/README.md) [Source 2](https://github.com/NoizAI/YuE2-Turbo/blob/main/MODEL_LICENSE)

### What it is good for

Non-commercial research into lyric-conditioned songs, musical styles and supported cover/notation workflows. [Source 1](https://github.com/NoizAI/YuE2-Turbo/blob/main/README.md) [Source 2](https://github.com/NoizAI/YuE2-Turbo/blob/main/MODEL_LICENSE)

### Demo & examples

The official repository documents the browser studio and links YuE2 examples. [Source 1](https://github.com/NoizAI/YuE2-Turbo/blob/main/README.md)

### Install

Use the official route below; commands are documented instructions, not commands run during this review. [Source 1](https://github.com/NoizAI/YuE2-Turbo/blob/main/README.md) [Source 2](https://github.com/NoizAI/YuE2-Turbo/blob/main/MODEL_LICENSE)

1. Use the documented Linux Python/CUDA environment and pinned inference dependencies.
2. Install the server extra and obtain model weights under the MODEL_LICENSE.
3. Set the documented private service key, start the backend, then the browser frontend.

```sh
yue2-serve
```


```sh
YUE2_UPSTREAM=http://127.0.0.1:8000 yue2-web
```

### First project

Begin with a small example and review the result before expanding the project. [Source 1](https://github.com/NoizAI/YuE2-Turbo/blob/main/README.md) [Source 2](https://github.com/NoizAI/YuE2-Turbo/blob/main/MODEL_LICENSE)

1. Begin with a short lyrics/style example and low concurrency.
2. Listen for clipping, lyric errors and continuity before increasing duration.
### Hardware & software

Requirements below reflect the cited documentation. Unreported minimums remain unknown. [Source 1](https://github.com/NoizAI/YuE2-Turbo/blob/main/README.md) [Source 2](https://github.com/NoizAI/YuE2-Turbo/blob/main/MODEL_LICENSE)

- **Hardware:** Tuned on RTX 5090 32 GB; 24 GB operation requires reduced concurrency and is not universally guaranteed. About 8 GB weights plus cache; author reports around 18 GB idle/25 GB peak GPU use.
- **Software:** Linux x86_64, Python 3.11/3.12, PyTorch 2.10/CUDA 12.8, vLLM 0.19 and matching Triton; optional tools add dependencies.
- **Platforms:** Linux/NVIDIA is the documented route; native macOS/Windows operation is not validated.

### License, model weights & costs

The complete top-level Apache-2.0 software license was reviewed and archived. Keep dependent components and model terms separate. [Source 1](https://github.com/NoizAI/YuE2-Turbo/blob/main/LICENSE) [Source 2](https://github.com/NoizAI/YuE2-Turbo/blob/main/README.md) [Source 3](https://github.com/NoizAI/YuE2-Turbo/blob/main/MODEL_LICENSE)

- **Code:** Apache-2.0
- **Weights:** Apache-2.0 server code, but YuE2 weights are CC-BY-NC-4.0 according to the reviewed MODEL_LICENSE. The open-source server does not remove that non-commercial restriction.
- **Commercial:** The application is open source, but the documented model restriction is non-commercial; do not treat this workflow as cleared for commercial/client work.
- **Cost:** Source code is available under the stated license. Hardware, electricity, storage and any optional or required hosted model/API services may add costs; no current service-price quote is asserted.

### Why it merits attention

Its documented workflow is relevant to non-commercial research into lyric-conditioned songs, musical styles and supported cover/notation workflows. The sources provide a concrete implementation and setup path. This assessment is based on documentation and developer examples, not independent output or performance testing. [Source 1](https://github.com/NoizAI/YuE2-Turbo/blob/main/README.md) [Source 2](https://github.com/NoizAI/YuE2-Turbo/blob/main/MODEL_LICENSE)

### Limitations

Author throughput figures were not reproduced. Model licensing limits client/commercial music production; source music and voice rights also matter. [Source 1](https://github.com/NoizAI/YuE2-Turbo/blob/main/README.md) [Source 2](https://github.com/NoizAI/YuE2-Turbo/blob/main/MODEL_LICENSE)

### Get the tool

- [Repository](https://github.com/NoizAI/YuE2-Turbo)
- [Documentation](https://github.com/NoizAI/YuE2-Turbo/blob/main/README.md)
- [License](https://github.com/NoizAI/YuE2-Turbo/blob/main/LICENSE)

## FloodDiffusion2

Motion capture & character animation · AI choreography and dance composition · Interactive, immersive & live media

Completed the detailed guide for an earlier screened discovery. The repository falls within the discovery window, but this is not independent evidence of its launch date. Documentation and complete software license checked on 2026-10-06; no claim of a new release today.

### How it uses AI

A diffusion model generates human-motion sequences under streaming constraints and multiple controls. [Source](https://github.com/AlayaLab/FloodDiffusion2/blob/main/README.md) [Source](https://github.com/AlayaLab/FloodDiffusion2/blob/main/THIRD_PARTY_LICENSES.md)

### Introduction

A streaming diffusion research system for controllable human motion. [Source 1](https://github.com/AlayaLab/FloodDiffusion2/blob/main/README.md) [Source 2](https://github.com/AlayaLab/FloodDiffusion2/blob/main/THIRD_PARTY_LICENSES.md)

### What it is good for

Experimenting with text, trajectory and root-motion conditioning for animated characters. [Source 1](https://github.com/AlayaLab/FloodDiffusion2/blob/main/README.md) [Source 2](https://github.com/AlayaLab/FloodDiffusion2/blob/main/THIRD_PARTY_LICENSES.md)

### Demo & examples

The repository links project examples and provides evaluation/rendering configurations. [Source 1](https://github.com/AlayaLab/FloodDiffusion2/blob/main/README.md)

### Install

Use the official route below; commands are documented instructions, not commands run during this review. [Source 1](https://github.com/AlayaLab/FloodDiffusion2/blob/main/README.md) [Source 2](https://github.com/AlayaLab/FloodDiffusion2/blob/main/THIRD_PARTY_LICENSES.md)

1. Use the documented Python/CUDA environment.
2. Follow setup_project.py to install dependencies and download the specified checkpoints.
3. Obtain separately licensed body-model/data resources when required for mesh rendering.

```sh
python setup_project.py
```


```sh
python evaluate.py --config configs/df_humanml3d_263.yaml metrics.t2m=null
```

### First project

Begin with a small example and review the result before expanding the project. [Source 1](https://github.com/AlayaLab/FloodDiffusion2/blob/main/README.md) [Source 2](https://github.com/AlayaLab/FloodDiffusion2/blob/main/THIRD_PARTY_LICENSES.md)

1. Run the documented example and inspect the motion render.
2. Adjust a single prompt or trajectory control and compare body/contact consistency.
### Hardware & software

Requirements below reflect the cited documentation. Unreported minimums remain unknown. [Source 1](https://github.com/AlayaLab/FloodDiffusion2/blob/main/README.md) [Source 2](https://github.com/AlayaLab/FloodDiffusion2/blob/main/THIRD_PARTY_LICENSES.md)

- **Hardware:** Author examples use RTX 4090 for inference and H200 for training, not universal minima. RAM, minimum VRAM and disk requirements are not specified.
- **Software:** Python 3.10+, documented PyTorch 2.9.1/CUDA 12.8 stack; OpenGL/EGL and SMPL-H resources for relevant rendering paths.
- **Platforms:** Linux is documented, with Windows via WSL2 described. Native macOS support is not established.

### License, model weights & costs

The complete top-level MIT software license was reviewed and archived. Keep dependent components and model terms separate. [Source 1](https://github.com/AlayaLab/FloodDiffusion2/blob/main/LICENSE) [Source 2](https://github.com/AlayaLab/FloodDiffusion2/blob/main/README.md) [Source 3](https://github.com/AlayaLab/FloodDiffusion2/blob/main/THIRD_PARTY_LICENSES.md)

- **Code:** MIT
- **Weights:** MIT code; checkpoint/data licenses remain separate. SMPL-H requires its own licensed access and is not granted by this repository.
- **Commercial:** The reviewed software license permits commercial software use subject to its obligations; it does not clear independent weights, data, assets, services or dependencies.
- **Cost:** Source code is available under the stated license. Hardware, electricity, storage and any optional or required hosted model/API services may add costs; no current service-price quote is asserted.

### Why it merits attention

Its documented workflow is relevant to experimenting with text, trajectory and root-motion conditioning for animated characters. The sources provide a concrete implementation and setup path. This assessment is based on documentation and developer examples, not independent output or performance testing. [Source 1](https://github.com/AlayaLab/FloodDiffusion2/blob/main/README.md) [Source 2](https://github.com/AlayaLab/FloodDiffusion2/blob/main/THIRD_PARTY_LICENSES.md)

### Limitations

Research motion needs checking for contact, anatomy and retargeting quality. Body-model permissions can affect redistribution. [Source 1](https://github.com/AlayaLab/FloodDiffusion2/blob/main/README.md) [Source 2](https://github.com/AlayaLab/FloodDiffusion2/blob/main/THIRD_PARTY_LICENSES.md)

### Get the tool

- [Repository](https://github.com/AlayaLab/FloodDiffusion2)
- [Documentation](https://github.com/AlayaLab/FloodDiffusion2/blob/main/README.md)
- [License](https://github.com/AlayaLab/FloodDiffusion2/blob/main/LICENSE)

## MCP build123d

3D printing & generative CAD · AI-assisted textile and computational craft · AI agents for code-authored media production

Completed the detailed guide for an earlier screened discovery. Documentation and complete software license checked on 2026-10-06; no claim of a new release today.

### How it uses AI

An external AI agent writes build123d code, renders it and uses OCCT-derived feedback to revise geometry. [Source](https://github.com/superWorldSavior/mcp-build123d/blob/main/README.md)

### Introduction

An MCP server connecting AI agents to parametric Python CAD and geometric inspection. [Source 1](https://github.com/superWorldSavior/mcp-build123d/blob/main/README.md)

### What it is good for

Drafting parameterized parts, checking dimensions and exporting STEP/STL/GLB for further review. [Source 1](https://github.com/superWorldSavior/mcp-build123d/blob/main/README.md)

### Demo & examples

The README includes example workflows and the documented MCP connection route. [Source 1](https://github.com/superWorldSavior/mcp-build123d/blob/main/README.md)

### Install

Use the official route below; commands are documented instructions, not commands run during this review. [Source 1](https://github.com/superWorldSavior/mcp-build123d/blob/main/README.md)

1. Install Deno 2.9.6 and Python 3.10+ for the source route.
2. Create the project virtual environment and install pinned runtime dependencies.
3. Start the local MCP service and connect a compatible AI client.

```sh
pip install -r requirements/runtime.txt -c requirements/constraints.txt
```


```sh
BUILD123D_PYTHON_BIN="$PWD/.venv/bin/python" deno task serve
```

### First project

Begin with a small example and review the result before expanding the project. [Source 1](https://github.com/superWorldSavior/mcp-build123d/blob/main/README.md)

1. Request a small bracket with explicit dimensions.
2. Inspect the preview and measurements, revise the design, then export for CAD/manufacturing review.
### Hardware & software

Requirements below reflect the cited documentation. Unreported minimums remain unknown. [Source 1](https://github.com/superWorldSavior/mcp-build123d/blob/main/README.md)

- **Hardware:** RAM, VRAM and storage minimums are not documented; external AI inference is separate.
- **Software:** Deno 2.9.6, Python >=3.10, pinned build123d 0.11.1 and OCCT dependencies; external MCP-capable AI client.
- **Platforms:** Documented promotion/setup targets macOS/Linux POSIX environments; the documented Windows path is refused rather than validated.

### License, model weights & costs

The complete top-level MIT software license was reviewed and archived. Keep dependent components and model terms separate. [Source 1](https://github.com/superWorldSavior/mcp-build123d/blob/main/LICENSE) [Source 2](https://github.com/superWorldSavior/mcp-build123d/blob/main/README.md)

- **Code:** MIT
- **Weights:** MIT server; CAD dependencies and external model terms remain independent.
- **Commercial:** The reviewed software license permits commercial software use subject to its obligations; it does not clear independent weights, data, assets, services or dependencies.
- **Cost:** Source code is available under the stated license. Hardware, electricity, storage and any optional or required hosted model/API services may add costs; no current service-price quote is asserted.

### Why it merits attention

Its documented workflow is relevant to drafting parameterized parts, checking dimensions and exporting STEP/STL/GLB for further review. The sources provide a concrete implementation and setup path. This assessment is based on documentation and developer examples, not independent output or performance testing. [Source 1](https://github.com/superWorldSavior/mcp-build123d/blob/main/README.md)

### Limitations

Runs arbitrary Python and is not a sandbox. Use a controlled local environment; geometry checks do not certify manufacturing safety. [Source 1](https://github.com/superWorldSavior/mcp-build123d/blob/main/README.md)

### Get the tool

- [Repository](https://github.com/superWorldSavior/mcp-build123d)
- [Documentation](https://github.com/superWorldSavior/mcp-build123d/blob/main/README.md)
- [License](https://github.com/superWorldSavior/mcp-build123d/blob/main/LICENSE)

## Line-us MCP

3D printing & generative CAD · AI-assisted textile and computational craft · Interactive, immersive & live media

Completed the detailed guide for an earlier screened discovery. The repository falls within the discovery window, but this is not independent evidence of its launch date. Documentation and complete software license checked on 2026-10-06; no claim of a new release today.

### How it uses AI

A connected language-model agent uses scene-building, preview and robot tools to plan and execute drawings. [Source](https://github.com/BenTeoNeb/lineus-mcp/blob/main/README.md)

### Introduction

An AI-agent interface for planning drawings and controlling a Line-us pen robot. [Source 1](https://github.com/BenTeoNeb/lineus-mcp/blob/main/README.md)

### What it is good for

Turning text, SVG and hatched compositions into reviewed physical drawing commands. [Source 1](https://github.com/BenTeoNeb/lineus-mcp/blob/main/README.md)

### Demo & examples

The official README documents a mock mode and physical-robot workflow. [Source 1](https://github.com/BenTeoNeb/lineus-mcp/blob/main/README.md)

### Install

Use the official route below; commands are documented instructions, not commands run during this review. [Source 1](https://github.com/BenTeoNeb/lineus-mcp/blob/main/README.md)

1. Install uv and a compatible MCP client.
2. Use the documented package-from-repository route and configure LINEUS_HOST for the local robot.
3. Start with LINEUS_MOCK=1 to inspect plans without moving hardware.

```sh
uvx --from git+https://github.com/BenTeoNeb/lineus-mcp lineus-mcp
```

### First project

Begin with a small example and review the result before expanding the project. [Source 1](https://github.com/BenTeoNeb/lineus-mcp/blob/main/README.md)

1. Create a simple drawing in mock mode and inspect its preview.
2. Check the page/reach limits, then run a supervised short plot with pen and paper.
### Hardware & software

Requirements below reflect the cited documentation. Unreported minimums remain unknown. [Source 1](https://github.com/BenTeoNeb/lineus-mcp/blob/main/README.md)

- **Hardware:** A Line-us robot is needed for physical output, but mock mode does not need hardware. RAM, VRAM and disk minima are not stated.
- **Software:** uv, an MCP client and a documented Python 3.10–3.13 environment; local TCP connection to the robot.
- **Platforms:** Python-based local workflow; a complete desktop OS validation matrix is not provided.

### License, model weights & costs

The complete top-level MIT software license was reviewed and archived. Keep dependent components and model terms separate. [Source 1](https://github.com/BenTeoNeb/lineus-mcp/blob/main/LICENSE) [Source 2](https://github.com/BenTeoNeb/lineus-mcp/blob/main/README.md)

- **Code:** MIT
- **Weights:** MIT tool code; bundled font notices include OFL and external agent/model terms remain separate.
- **Commercial:** The reviewed software license permits commercial software use subject to its obligations; it does not clear independent weights, data, assets, services or dependencies.
- **Cost:** Source code is available under the stated license. Hardware, electricity, storage and any optional or required hosted model/API services may add costs; no current service-price quote is asserted.

### Why it merits attention

Its documented workflow is relevant to turning text, SVG and hatched compositions into reviewed physical drawing commands. The sources provide a concrete implementation and setup path. This assessment is based on documentation and developer examples, not independent output or performance testing. [Source 1](https://github.com/BenTeoNeb/lineus-mcp/blob/main/README.md)

### Limitations

The robot connection is unauthenticated on the local network. Default page size is not a guaranteed physical reach limit; preview and supervise motion. [Source 1](https://github.com/BenTeoNeb/lineus-mcp/blob/main/README.md)

### Get the tool

- [Repository](https://github.com/BenTeoNeb/lineus-mcp)
- [Documentation](https://github.com/BenTeoNeb/lineus-mcp/blob/main/README.md)
- [License](https://github.com/BenTeoNeb/lineus-mcp/blob/main/LICENSE)

## Haptic Neural Fields

Tactile, vibration and haptic media · Accessible media & assistive creation · Physical, robotic & kinetic installations

First detailed library baseline. Documentation and complete software license checked on 2026-10-06; no claim of a new release today.

### How it uses AI

A learned material/action representation predicts tactile output for a novel action rather than replaying a fixed vibration file. [Source](https://github.com/mmlab-cv/HapticNeuralFields/blob/main/README.md)

### Introduction

A neural-field research implementation for synthesizing tactile signals from materials and actions. [Source 1](https://github.com/mmlab-cv/HapticNeuralFields/blob/main/README.md)

### What it is good for

Exploring haptic material experiences and generating signals for new interaction trajectories. [Source 1](https://github.com/mmlab-cv/HapticNeuralFields/blob/main/README.md)

### Demo & examples

The official project page presents research examples and the repository provides a CPU smoke example. [Source 1](https://mmlab-cv.github.io/HapticNeuralFields/)

### Install

Use the official route below; commands are documented instructions, not commands run during this review. [Source 1](https://github.com/mmlab-cv/HapticNeuralFields/blob/main/README.md)

1. Clone the repository, create a Python environment and install requirements.
2. Download the documented ResNet encoder and arrange the sample data.
3. Run the small CPU training example before scaling the experiment.

```sh
pip install -r requirements.txt
```


```sh
python main.py --device=cpu --num_of_materials=1 --num_epochs=1 --validation_interval=1 --checkpoint_interval=1 --batch_size=8 --num_workers=0
```


```sh
python generate_novel_action.py --action=Scratch_LeftRight_Strong --image=Digit/BubbleEnvelope/00487.jpg
```

### First project

Begin with a small example and review the result before expanding the project. [Source 1](https://github.com/mmlab-cv/HapticNeuralFields/blob/main/README.md)

1. Train the small documented material example.
2. Generate a new action from the latest checkpoint and inspect the signal before integrating any physical haptic device.
### Hardware & software

Requirements below reflect the cited documentation. Unreported minimums remain unknown. [Source 1](https://github.com/mmlab-cv/HapticNeuralFields/blob/main/README.md)

- **Hardware:** A CPU smoke route and automatic CUDA selection are documented. RAM, VRAM, storage minima and universal actuator requirements are not specified.
- **Software:** Python requirements, encoder weights and example tactile/image data; use documented paths and checkpoints.
- **Platforms:** Python CPU/CUDA routes are described; tested Windows/macOS/Linux versions are not comprehensively specified.

### License, model weights & costs

The complete top-level MIT software license was reviewed and archived. Keep dependent components and model terms separate. [Source 1](https://github.com/mmlab-cv/HapticNeuralFields/blob/main/LICENSE) [Source 2](https://github.com/mmlab-cv/HapticNeuralFields/blob/main/README.md)

- **Code:** MIT
- **Weights:** MIT code. Encoder weights, datasets and any physical-device integration have separate terms/requirements.
- **Commercial:** The reviewed software license permits commercial software use subject to its obligations; it does not clear independent weights, data, assets, services or dependencies.
- **Cost:** Source code is available under the stated license. Hardware, electricity, storage and any optional or required hosted model/API services may add costs; no current service-price quote is asserted.

### Why it merits attention

Its documented workflow is relevant to exploring haptic material experiences and generating signals for new interaction trajectories. The sources provide a concrete implementation and setup path. This assessment is based on documentation and developer examples, not independent output or performance testing. [Source 1](https://github.com/mmlab-cv/HapticNeuralFields/blob/main/README.md)

### Limitations

A research signal generator, not a validated universal haptic driver. Perceptual results and safe device playback were not tested here. [Source 1](https://github.com/mmlab-cv/HapticNeuralFields/blob/main/README.md)

### Get the tool

- [Repository](https://github.com/mmlab-cv/HapticNeuralFields)
- [Documentation](https://mmlab-cv.github.io/HapticNeuralFields/)
- [License](https://github.com/mmlab-cv/HapticNeuralFields/blob/main/LICENSE)

## Additional open-source AI discoveries

Creative AI relevance and software license screened. Full installation, requirements and quality profiles are pending.

### MFLUX · MIT

Local image generation and editing on Apple Silicon.
MLX implementations run supported diffusion model families with quantization.
Full workflow/hardware review pending; each supported model has independent weight terms. Documentation screened; not installed or tested.

- [Official README](https://github.com/mflux-community/mflux/blob/main/README.md)
- [Reviewed complete software license](https://github.com/mflux-community/mflux/blob/main/LICENSE)
### QualityScaler · MIT

Upscaling and denoising photographs or video.
Neural super-resolution models run through ONNX/DirectML with tiling.
Full hardware review pending; paid packaged binaries and model terms are separate from MIT source. Restoration can invent detail. Documentation screened; not installed or tested.

- [Official README](https://github.com/Djdefrag/QualityScaler/blob/main/README.md)
- [Reviewed complete software license](https://github.com/Djdefrag/QualityScaler/blob/main/LICENSE)
### Comic Translate · Apache-2.0

Translating comics while preserving bubble layout.
Combines learned detection/OCR, translation, inpainting and text replacement.
Local versus API-dependent routes, model terms and layout accuracy still need detailed review. Documentation screened; not installed or tested.

- [Official README](https://github.com/ogkalu2/comic-translate/blob/main/README.md)
- [Reviewed complete software license](https://github.com/ogkalu2/comic-translate/blob/main/LICENSE)
### noScribe · GPL-3.0

Transcribing recorded speech with speaker-aware editing.
Uses Whisper/faster-whisper and diarization components for speech and speaker analysis.
Native platform installers and model requirements need full review. The official project is associated with noscribe.de, not similarly named commercial sites. Documentation screened; not installed or tested.

- [Official README](https://github.com/kaixxx/noScribe/blob/main/README.md)
- [Reviewed complete software license](https://github.com/kaixxx/noScribe/blob/main/LICENSE.txt)
### Godot RL Agents · MIT

Training game agents and experimental interactive behaviors inside Godot.
Connects Godot simulations to reinforcement-learning libraries including Stable Baselines3 and other training backends.
Installation, hardware, dependent model terms and output quality still need a full practical review. Documentation screened; not installed or tested.

- [Official README](https://github.com/edbeeching/godot_rl_agents/blob/main/README.md)
- [Reviewed complete software license](https://github.com/edbeeching/godot_rl_agents/blob/main/LICENSE)
### Pallaidium · GPL-3.0

Generating media inside Blender Video Sequence Editor workflows.
Integrates generative image, audio and video models into Blender editing.
GPL source reviewed. Model-specific restrictions, including non-commercial options identified by the README, and GPU/setup requirements need full review. Documentation screened; not installed or tested.

- [Official README](https://github.com/tin2tin/Pallaidium/blob/main/README.md)
- [Reviewed complete software license](https://github.com/tin2tin/Pallaidium/blob/main/LICENSE.txt)
### ComfyUI BlenderAI Node · GPL-3.0

Connecting Blender renders and assets to ComfyUI generation.
A Blender addon exchanges scene/render inputs with diffusion workflows for image and texture tasks.
Blender/ComfyUI version compatibility, memory needs and model licenses remain pending. Documentation screened; not installed or tested.

- [Official README](https://github.com/AIGODLIKE/ComfyUI-BlenderAI-node/blob/main/README.md)
- [Reviewed complete software license](https://github.com/AIGODLIKE/ComfyUI-BlenderAI-node/blob/main/LICENSE)
### AudioMuse AI · AGPL-3.0

Analyzing and navigating a music collection by sonic character.
Neural audio analysis and CLAP-style embeddings support similarity and playlist workflows.
AGPL application and additional model/asset notices reviewed separately; end-to-end requirements and library quality remain pending. Documentation screened; not installed or tested.

- [Official README](https://github.com/NeptuneHub/AudioMuse-AI/blob/main/README.md)
- [Reviewed complete software license](https://github.com/NeptuneHub/AudioMuse-AI/blob/main/LICENSE)
### Home Gallery · MIT

Searching a personal media collection by visual similarity.
Uses learned image features for reverse-image and similarity search.
The default configuration can use an external analysis API; a local route is configurable. Offline behavior and requirements still need practical review. Documentation screened; not installed or tested.

- [Official README](https://github.com/xemle/home-gallery/blob/master/README.md)
- [Reviewed complete software license](https://github.com/xemle/home-gallery/blob/master/LICENSE)
### Infinite Image Browsing · MIT

Finding and organizing generated-image collections.
Documented embeddings-based clustering/search and AI folder naming go beyond reading image metadata.
Full setup pending; some AI functions require an OpenAI-compatible endpoint and independent model terms. Documentation screened; not installed or tested.

- [Official README](https://github.com/zanllp/infinite-image-browsing/blob/main/README.md)
- [Reviewed complete software license](https://github.com/zanllp/infinite-image-browsing/blob/main/LICENSE)
### Flint Chart · MIT

Creating charts with AI agents and exporting to familiar chart backends.
Agents author a compact chart specification that compiles to supported visualization formats.
AI authoring depends on an external agent; backend and Python-port maturity need further review. Documentation screened; not installed or tested.

- [Official README](https://github.com/microsoft/flint-chart/blob/main/README.md)
- [Reviewed complete software license](https://github.com/microsoft/flint-chart/blob/main/LICENSE)
### Kimodo · Apache-2.0

Generating character or robot motion under text, pose and path controls.
Kinematic motion diffusion synthesizes sequences from multiple conditioning signals.
Code is Apache-2.0; model weights, retargeting constraints and hardware requirements need separate full review. Documentation screened; not installed or tested.

- [Official README](https://github.com/nv-tlabs/kimodo/blob/main/README.md)
- [Reviewed complete software license](https://github.com/nv-tlabs/kimodo/blob/main/LICENSE)
### img2img Turbo · MIT

Fast sketch-to-image and image-translation experiments.
One-step diffusion translation builds on pretrained image model components.
MIT code does not replace Stable Diffusion Turbo weight terms; platform and resource review pending. Documentation screened; not installed or tested.

- [Official README](https://github.com/GaParmar/img2img-turbo/blob/main/README.md)
- [Reviewed complete software license](https://github.com/GaParmar/img2img-turbo/blob/main/LICENSE)
### DreamCraft3D · MIT

Creating 3D assets from image guidance.
Diffusion-guided geometry and texture optimization form a staged 3D generation pipeline.
Separate guidance models such as Stable Zero123 have independent terms; full installation and hardware review pending. Documentation screened; not installed or tested.

- [Official README](https://github.com/deepseek-ai/DreamCraft3D/blob/main/README.md)
- [Reviewed complete software license](https://github.com/deepseek-ai/DreamCraft3D/blob/main/LICENSE-CODE)
### DynamiCrafter · Apache-2.0

Animating still images and experimenting with loops/interpolation.
Diffusion video generation uses image and text conditioning.
Research prototype; model terms, resolution-specific memory and temporal consistency need full review. Documentation screened; not installed or tested.

- [Official README](https://github.com/Doubiiu/DynamiCrafter/blob/main/README.md)
- [Reviewed complete software license](https://github.com/Doubiiu/DynamiCrafter/blob/main/LICENSE)
### Pyramid Flow · MIT

Text- and image-conditioned video-generation experiments.
Autoregressive flow matching generates video across resolution stages.
Code licensing is verified; weights, 384p/768p hardware demands and setup remain pending. Documentation screened; not installed or tested.

- [Official README](https://github.com/jy0205/Pyramid-Flow/blob/main/README.md)
- [Reviewed complete software license](https://github.com/jy0205/Pyramid-Flow/blob/main/LICENSE)
### FastGS · MIT

Accelerating Gaussian-splat reconstruction experiments.
Optimizes learned Gaussian scene representations with a training approach designed for faster reconstruction.
MIT top-level code; rasterizer and inherited 3DGS/Taming/Speedy components have separate terms. Full dependency and hardware review pending. Documentation screened; not installed or tested.

- [Official README](https://github.com/fastgs/FastGS/blob/main/README.md)
- [Reviewed complete software license](https://github.com/fastgs/FastGS/blob/main/LICENSE)
### LGM · MIT

Generating Gaussian 3D content from multiview image conditioning.
A large reconstruction model predicts neural 3D scene representations.
MIT top-level code; INRIA-derived rasterizer and model terms must be checked separately before deployment. Documentation screened; not installed or tested.

- [Official README](https://github.com/3DTopia/LGM/blob/main/readme.md)
- [Reviewed complete software license](https://github.com/3DTopia/LGM/blob/main/LICENSE)
### Follow Your Pose · MIT

Conditioning character video generation on pose sequences and text.
A diffusion video pipeline follows pose controls to synthesize movement.
Stable Diffusion weights and other resources have separate terms; setup and motion fidelity remain pending. Documentation screened; not installed or tested.

- [Official README](https://github.com/mayuelala/FollowYourPose/blob/main/README.md)
- [Reviewed complete software license](https://github.com/mayuelala/FollowYourPose/blob/main/LICENSE)
### ReCamMaster · MIT

Changing camera motion/viewpoint in generated video.
A learned camera-conditioned video model re-renders scenes under new camera trajectories.
The public implementation uses a Wan2.1-based route; the paper backbone is not fully released, so research demo parity must not be assumed. Documentation screened; not installed or tested.

- [Official README](https://github.com/KlingAIResearch/ReCamMaster/blob/main/README.md)
- [Reviewed complete software license](https://github.com/KlingAIResearch/ReCamMaster/blob/main/LICENSE)
### Bernini · Apache-2.0

Planning and generating edited videos from multimodal instructions.
Combines a multimodal semantic planner with a diffusion-transformer renderer.
Full and renderer-only routes have different requirements; model permissions, resources and output quality remain pending. Documentation screened; not installed or tested.

- [Official README](https://github.com/bytedance/Bernini/blob/main/README.md)
- [Reviewed complete software license](https://github.com/bytedance/Bernini/blob/main/LICENSE)
### JoyAI Image · Apache-2.0

Unified image understanding, generation and editing research.
Connects an 8B multimodal language component with a 16B diffusion transformer.
Large-model setup, hardware and weight terms require a full review despite Apache-2.0 source. Documentation screened; not installed or tested.

- [Official README](https://github.com/jd-opensource/JoyAI-Image/blob/main/README.md)
- [Reviewed complete software license](https://github.com/jd-opensource/JoyAI-Image/blob/main/LICENSE)
### JoyAI VL Interaction · Apache-2.0

Building vision-aware spoken interfaces for installations or interactive experiences.
A vision-first multimodal model interprets visual input and supports spoken interaction.
This is an interaction model, not a video editor. Device access, latency, hardware and weight terms need further review. Documentation screened; not installed or tested.

- [Official README](https://github.com/jd-opensource/JoyAI-VL-Interaction/blob/main/README.md)
- [Reviewed complete software license](https://github.com/jd-opensource/JoyAI-VL-Interaction/blob/main/LICENSE)
### MuseGAN · MIT

Researching multi-track symbolic music generation.
Generative adversarial models produce coordinated musical tracks.
An older research baseline, not a new release; legacy dependencies, dataset rights and checkpoint availability need full review. Documentation screened; not installed or tested.

- [Official README](https://github.com/salu133445/musegan/blob/main/README.md)
- [Reviewed complete software license](https://github.com/salu133445/musegan/blob/main/LICENSE)
### SplaTAM · BSD-3-Clause

Reconstructing neural scenes from RGB-D captures.
Gaussian-based simultaneous localization and mapping learns a scene while estimating camera motion.
BSD-3-Clause top-level code reviewed; dependent rasterizer/model/data terms and hardware remain pending. Documentation screened; not installed or tested.

- [Official README](https://github.com/spla-tam/SplaTAM/blob/main/README.md)
- [Reviewed complete software license](https://github.com/spla-tam/SplaTAM/blob/main/LICENSE)
### NeuralRecon · Apache-2.0

Reconstructing geometry from monocular video for spatial content workflows.
A learned multi-view reconstruction network estimates 3D geometry across frames.
Legacy research setup and ARKit example are not proof of current mobile deployment; full setup and terms pending. Documentation screened; not installed or tested.

- [Official README](https://github.com/zju3dv/NeuralRecon/blob/master/README.md)
- [Reviewed complete software license](https://github.com/zju3dv/NeuralRecon/blob/master/LICENSE)
### Riffusion Hobby · MIT

Experimenting with spectrogram-based prompt-conditioned audio.
Diffusion-generated spectrograms are converted into sound and interpolated across prompts.
This is the older hobby codebase, not the present commercial service. Model terms, audio quality and dependencies need further review. Documentation screened; not installed or tested.

- [Official README](https://github.com/riffusion/riffusion-hobby/blob/main/README.md)
- [Reviewed complete software license](https://github.com/riffusion/riffusion-hobby/blob/main/LICENSE)
### NeuralSVG · MIT

Generating editable vector artwork from text.
Diffusion-guided optimization learns ordered SVG shapes with palette controls.
Research code; model licenses, optimization cost and export editability need practical evaluation. Documentation screened; not installed or tested.

- [Official README](https://github.com/SagiPolaczek/NeuralSVG/blob/main/README.md)
- [Reviewed complete software license](https://github.com/SagiPolaczek/NeuralSVG/blob/main/LICENSE)
### Metal Gauss · MIT

Training Gaussian-splat captures on Apple Silicon.
Uses a Metal-based Gaussian optimization path instead of requiring CUDA.
MIT source reviewed; exact chip/memory limits, dependency terms and capture quality remain pending. Documentation screened; not installed or tested.

- [Official README](https://github.com/nandometzger/metal-gauss/blob/main/README.md)
- [Reviewed complete software license](https://github.com/nandometzger/metal-gauss/blob/main/LICENSE)
### MLX Spatial · MIT

Running supported image-to-spatial models on Apple Silicon.
MLX ports support model families for 3D Gaussians and camera/depth prediction.
Do not assume all outputs are Gaussians: the documented HY-World-Mirror route covers camera/depth. Upstream weight access and hardware review pending. Documentation screened; not installed or tested.

- [Official README](https://github.com/appautomaton/mlx-spatial/blob/main/README.md)
- [Reviewed complete software license](https://github.com/appautomaton/mlx-spatial/blob/main/LICENSE)
### Gaido · MIT

Iterating on creative browser code with visual feedback.
An agent notebook cycles through code, rendering and critique with branching revisions.
External model costs and client/runtime requirements need review; generated interactive output is not hands-on tested. Documentation screened; not installed or tested.

- [Official README](https://github.com/vlobanov/gaido/blob/main/README.md)
- [Reviewed complete software license](https://github.com/vlobanov/gaido/blob/main/LICENSE)
### CustomDance · MIT

Generating dance with text intent, reference movement and controlled edits.
Multimodal intent analysis/retrieval and motion inpainting guide dance synthesis.
Research CUDA environment, FineDance/SMPL resources and optional hosted language-model costs need full review. Documentation screened; not installed or tested.

- [Official README](https://github.com/XulongT/CustomDance/blob/main/README.md)
- [Reviewed complete software license](https://github.com/XulongT/CustomDance/blob/main/LICENSE)
### Neural HRTF Tutorial · MIT

Learning neural head-related transfer-function modeling through executable notebooks.
The tutorial implements learned HRTF models for spatial-audio experiments.
MIT teaching code is distinct from included/referenced data terms, including CC-BY-SA material; hardware and perceptual validation pending. Documentation screened; not installed or tested.

- [Official README](https://github.com/yzyouzhang/dafx2026-hrtf-tutorial/blob/main/README.md)
- [Reviewed complete software license](https://github.com/yzyouzhang/dafx2026-hrtf-tutorial/blob/main/LICENSE.md)
### HRTF Field · MIT

Modeling directional headphone audio responses continuously.
A neural field represents HRTFs across spatial directions.
Research prototype; dataset rights, inference setup and listener-specific quality remain pending. Documentation screened; not installed or tested.

- [Official README](https://github.com/yzyouzhang/hrtf_field/blob/main/README.md)
- [Reviewed complete software license](https://github.com/yzyouzhang/hrtf_field/blob/main/LICENSE)
### OpenWhispr Android · Apache-2.0

Dictating creative notes and drafts on Android.
Local sherpa-ONNX recognition or optional hosted Whisper turns speech into text; optional language-model cleanup is supported.
Apache-2.0 app reviewed; local model/device compatibility and optional provider terms/costs need full review. Documentation screened; not installed or tested.

- [Official README](https://github.com/EdiBianco/OpenWhispr/blob/main/README.md)
- [Reviewed complete software license](https://github.com/EdiBianco/OpenWhispr/blob/main/LICENSE)
### HTML Video · Apache-2.0

Turning agent-authored HTML motion designs into video.
An AI coding-agent workflow authors animated HTML templates; optional AI soundtrack features extend the rendered output.
Apache-2.0 tooling; external AI clients, soundtrack terms and render requirements remain pending. Documentation screened; not installed or tested.

- [Official README](https://github.com/nexu-io/html-video/blob/main/README.md)
- [Reviewed complete software license](https://github.com/nexu-io/html-video/blob/main/LICENSE)
### AutoClip · MIT

Finding highlights and preparing shorter versions of long videos.
Speech recognition and language-model analysis select segments and assist subtitles/covers.
Chinese primary docs reviewed. Local/hosted model choices, hardware and any publishing integrations need separate evaluation; no social posting was enabled. Documentation screened; not installed or tested.

- [Official README](https://github.com/zhouxiaoka/autoclip/blob/main/README.md)
- [Reviewed complete software license](https://github.com/zhouxiaoka/autoclip/blob/main/LICENSE)
### YouDub WebUI · Apache-2.0

Translating and dubbing videos with aligned speech.
Combines recognition, translation and voice-generation/cloning stages, with optional subtitle-driven input.
Model/provider terms, voice permissions and language-specific quality require detailed review. Documentation screened; not installed or tested.

- [Official README](https://github.com/liuzhao1225/YouDub-webui/blob/main/README.md)
- [Reviewed complete software license](https://github.com/liuzhao1225/YouDub-webui/blob/main/LICENSE)
### Scriberr · MIT

Transcribing media locally and asking questions about transcripts.
Speech models generate transcripts and optional language models support transcript analysis.
Full installation, supported diarization behavior, hardware and optional provider terms remain pending. Documentation screened; not installed or tested.

- [Official README](https://github.com/rishikanthc/Scriberr/blob/main/README.md)
- [Reviewed complete software license](https://github.com/rishikanthc/Scriberr/blob/main/LICENSE)
### diart · MIT

Adding live speaker segmentation to recordings or interactive audio systems.
Neural streaming diarization estimates who is speaking over time.
Transcription is listed as future work in the reviewed README; do not treat this as an existing full ASR application. Model terms and latency still need review. Documentation screened; not installed or tested.

- [Official README](https://github.com/juanmc2005/diart/blob/main/README.md)
- [Reviewed complete software license](https://github.com/juanmc2005/diart/blob/main/LICENSE)
### Portable Local Studio · MIT

Using local image, speech and text tools through a shared desktop interface.
Integrates Stable Diffusion, Whisper, Kokoro and llama.cpp-oriented workflows.
Cross-platform claims and model-specific requirements are untested; MIT application licensing does not cover every bundled weight. Documentation screened; not installed or tested.

- [Official README](https://github.com/techjarves/Portable-Local-Studio/blob/main/README.md)
- [Reviewed complete software license](https://github.com/techjarves/Portable-Local-Studio/blob/main/LICENSE)
### AI Cover Gen · MIT

Experimenting with voice-converted song covers.
RVC-based voice conversion transforms vocal recordings within a cover-generation pipeline.
Voice/source-music permissions, weight terms, separation quality and hardware need full review. Documentation screened; not installed or tested.

- [Official README](https://github.com/SociallyIneptWeeb/AICoverGen/blob/main/README.md)
- [Reviewed complete software license](https://github.com/SociallyIneptWeeb/AICoverGen/blob/main/LICENSE)
### Audio WebUI · MIT

Trying speech, sound, music and voice-conversion models in one extensible interface.
Its feature documentation lists Bark, AudioLDM/AudioCraft, RVC, TTS and Whisper model integrations.
Older evolving integration stack; each model license and its dependency/hardware compatibility require full review. Documentation screened; not installed or tested.

- [Official README](https://github.com/gitmylo/audio-webui/blob/master/readme.md)
- [Reviewed complete software license](https://github.com/gitmylo/audio-webui/blob/master/LICENSE)
- [Official feature list](https://github.com/gitmylo/audio-webui/blob/master/readme/features.md)
### GauStudio · MIT

Experimenting with Gaussian scene reconstruction and processing pipelines.
Provides tooling around learned Gaussian representations for neural rendering workflows.
MIT top-level code with separately licensed rasterization components; full dependency, setup and export review pending. Documentation screened; not installed or tested.

- [Official README](https://github.com/GAP-LAB-CUHK-SZ/gaustudio/blob/master/README.md)
- [Reviewed complete software license](https://github.com/GAP-LAB-CUHK-SZ/gaustudio/blob/master/LICENSE)
### MVSplat · MIT

Reconstructing Gaussian scenes from sparse multiview images.
A feed-forward multiview model predicts a neural scene representation.
MIT source reviewed; dataset/checkpoint terms, GPU memory and sparse-view quality need detailed review. Documentation screened; not installed or tested.

- [Official README](https://github.com/donydchen/mvsplat/blob/main/README.md)
- [Reviewed complete software license](https://github.com/donydchen/mvsplat/blob/main/LICENSE)

## Excluded and unresolved findings

Research notes only; these do not enter the eligible tool library.

- **OpenTryOn** · excluded: The complete software license is CC-BY-NC-4.0, with a non-commercial restriction. This does not meet the open-source software eligibility rule. [Source](https://github.com/tryonlabs/opentryon)
- **Sniff AI** · needs-license-review: A creative fragrance-generation use is described, but no complete software license was found in the inspected repository. Remains outside the eligible library. [Source](https://github.com/ksek87/sniff_ai)
- **Abra** · needs-license-review: Potentially relevant AI/XR work, but no complete software license was available in the inspected repository. Not an eligible open-source recommendation yet. [Source](https://github.com/Brandi-Kinard/abra)

Source collection completed: 2026-10-06T12:30:43.842117+00:00
Search is a bounded sample. Stars and recent pushes are discovery signals, not verified quality or meaningful upgrades.
