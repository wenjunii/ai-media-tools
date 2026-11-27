# AI Media Scout — 2026-11-21

The edition has 96 complete guides and 21 screened discoveries. It completes 35 earlier pending guides and details 6 substantive release updates. LiveAudio documents an OBS caption overlay on Windows and Linux. CalibRaw marks subjects with device-side models for reversible RAW adjustments. The archival guides show how to correct machine-written drafts and export page layout. Music and fabrication guides describe how to keep generated work editable. SDAI documents separate iOS and Android diffusion runtimes. Open Body Tracker adds an INT8 CPU mode. OpenStitch and ZigZag update agent-assisted stitch workflows, and ComfyUI adds a deflicker route and removes DirectML. Code grants were read in full. Models, services, creative inputs and hardware or software hosts have separate requirements. This edition is based on source review and published documentation. No discovered app was installed or run. The expanded plan covered 117 fields, 1342/1342 repository-query attempts and 35 model tasks. The repository lane recorded 1342 successful, 0 partial and 0 failed queries, with 253 bounded. The model lane recorded 0 failed tasks. Metadata from 2,821 saved repository pages included 84,187 numeric identities. The complete retained backlog spans 118,555 candidates, including pilot history and 1,094 previously screened guides still pending before this edition. Creative relevance and the complete software grant were checked before including any discovery. Unreviewed and excluded records stay in local research. Live primary research yielded 578 complete usable responses from 686 distinct URL attempts, including a non-GitHub source in each of 117 fields. 14 captures reached the size bound. The ecosystem checks cover all 8 configured groups and record available findings and gaps. Evidence labels in this edition are 0 Recommended, 0 Ready to try, 107 Quality unverified, 10 Experimental. Updated evidence labels for previous entries: IgniteFuse (Quality unverified to Experimental), InvokeAI (Quality unverified to Experimental). 33 model tasks reached the configured response limit of 50 rows. A model record remains a discovery lead until code and use are verified. Model tasks with no rows: text2text-generation, zero-shot-audio-classification. The separate watchlist made 64 unsuccessful repository checks. Collection logged 4 enrichment failures. Credential-shaped material in unsealed captures was removed before sealing. The affected source origins and before-and-after hashes remain in private evidence.

Documentation reviewed today. Tools are not hands-on tested unless explicitly stated. Requirements and performance remain source-specific.

## Coverage

| Field | Finding |
| --- | --- |
| Images & design | Invoke's current creator documentation describes image generation and editing paths. Check the exact model selected for each canvas workflow before reporting rights or compute requirements. [Source 1](https://invoke.ai/) |
| Video, animation & film | OpenReelio and KoraCut provide examples of editable timeline and source-media pipelines. Follow version-specific model, workflow and export documentation when testing a handoff. 2 captures reached the size bound. [Source 1](https://openreelio.com/) [Source 2](https://koracut.org/en/docs/start/) |
| Audio, music & voice | The reviewed SCoIM material describes a piano-specific route from an accepted structure to MusicXML and MIDI. Audacity’s AI workflow uses separate effects for speech and audio processing. These are distinct authoring and cleanup tasks. 2 direct source attempts in this field did not yield usable evidence. 1 captures reached the size bound. [Source 1](https://huggingface.co/Arm/qwen3-tts-0-6b-custom-voice-mix-precision) [Source 2](https://www.ircam.fr/en/softwares) |
| 3D, reconstruction & assets | SolidCraft documents editable parametric sketches and an optional agent connection. Shape Studio separately documents local image-to-GLB or OBJ inference. Mesh export alone gives no evidence of watertightness or production print tolerances. [Source 1](https://wiro.ai/models) [Source 2](https://senacula.github.io/senacula-shapestudio/) [Source 3](https://senacula.github.io/senacula-shapestudio/mcp.html) [Source 4](https://solidcraft.io/) |
| Browser tools & web media | The browser LLM study and WebGPU documentation describe compute options. Hardware adapters, browser versions and cached weights affect any particular local creative workflow. [Source 1](https://arxiv.org/abs/2412.15803) [Source 2](https://developer.mozilla.org/en-US/docs/Web/API/WebGPU_API) |
| WebXR, VR & AR | Meta IWSDK’s development article and Google’s Three-Live project document AI-assisted construction paths. Verify the browser and headset feature before expecting the same behavior on a physical display. [Source 1](https://developers.meta.com/vr/blog/accelerate-vr-development-with-ai-and-immersive-web-sdk/) [Source 2](https://opensource.googleblog.com/2026/11/introducing-three-live-ai-generated-3d-ar-webxr.html) |
| Computational art & creative coding | FragmentTools documents live sketch controls. The MediaPipe hand-landmarker web guide describes the input and model-produced landmarks. Their creative connection needs explicit mapping and tracking tests. [Source 1](https://fragment.tools/) [Source 2](https://ai.google.dev/edge/mediapipe/solutions/vision/hand_landmarker/web_js) |
| Interactive, immersive & live media | LivePose documents an OSC bridge for pose output. Ossia’s installation guide describes mapping live data to a score. Check the selected processing model and control receiver separately. 1 direct source attempts in this field did not yield usable evidence. [Source 1](https://sat-mtl.github.io/livepose/) [Source 2](https://ossia.io/interactive-installations.html) |
| 3D printing & generative CAD | SOMA describes an agent-oriented CAD interface, while Kerfline links image redrawing to downstream path geometry. Printed or cut suitability needs measured checks of the result. [Source 1](https://somacad.app/) [Source 2](https://www.kerfline.build/) |
| Games & production pipelines | ForgeAX's documentation describes an agent-assisted game authoring workflow. The host engine, generated assets and distribution terms remain separate from editor authorization. [Source 1](https://pypi.org/project/segan-gen/) [Source 2](https://docs.godotengine.org/en/stable/classes/class_audiostreamwav.html) [Source 3](https://forgeax.github.io/docs/) [Source 4](https://segan.top/) |
| Motion capture & character animation | The primary pose-estimation and capture material distinguishes 2D observed positions from movement on a rig. Current editor and preview sources show where an animator can inspect timing before accepting an export. [Source 1](https://movens-zero.github.io/) |
| Avatars, digital humans & lip sync | The AVTR-1 repository card documents a model artifact. Evidence for capture-to-character export and downstream rig usability remains open. [Source 1](https://huggingface.co/avaturn-live/avtr-1/blob/main/README.md) |
| VFX, compositing & relighting | The Light-Aware Compositing paper provides a learned compositing method and evaluation examples. Integration and a complete eligible software release need separate checks. [Source 1](https://yaksoy.github.io/papers/SIG25p-LightAwareCompositing.pdf) [Source 2](https://arxiv.org/abs/2312.03698) |
| Spatial audio & volumetric media | SoundSpaces documents audio simulation over scenes. It provides a primary reference for spatial conditioning and acoustic results. Reproduction and output quality depend on a specific scene, model and listening system. 1 captures reached the size bound. [Source 1](https://soundspaces.org/) [Source 2](https://arxiv.org/abs/2401.14342) |
| Photogrammetry, scanning & neural rendering | The Columbia GCD project and dynamic reconstruction research address learned scene capture. Caliscope uses learned pose landmarks to check an already calibrated rig. These scopes have different hardware and evaluation requirements. 1 direct source attempts in this field did not yield usable evidence. [Source 1](https://gcd.cs.columbia.edu/) [Source 2](https://arxiv.org/abs/2512.15719) [Source 3](https://mprib.github.io/caliscope/reconstruction/) |
| Editing, captions & post-production | The Kdenlive manual documents editable captions from a selected speech track. LocalVocal supplies draft captions within OBS. Choose live or post-production translation and timing separately. 2 direct source attempts in this field did not yield usable evidence. [Source 1](https://docs.kdenlive.org/en/effects_and_filters/speech_to_text.html) [Source 2](https://obsproject.com/forum/resources/localvocal-local-live-captions-translation-on-the-go.1769/) |
| Vector graphics, illustration & textures | The SVGRender account describes learned vector rendering on the Hub. A separate vector file still needs review for editable paths, transforms and usable layer structure. [Source 1](https://huggingface.co/SVGRender) [Source 2](https://www.w3.org/TR/SVG2/) |
| Typography, fonts & layout | VecGlypher’s primary research covers generated SVG glyph outlines. A usable font still needs metrics, language coverage, consistency checks and a review of source-data rights. 1 direct source attempts in this field did not yield usable evidence. [Source 1](https://arxiv.org/abs/2602.21461) |
| Storyboarding, narrative & comics | The dramai project site describes model-driven short-drama orchestration. Check tone and continuity across the exact model endpoints and preserve an editable script or storyboard for revisions. 1 direct source attempts in this field did not yield usable evidence. [Source 1](https://hyyyyyyz.github.io/dramai/) |
| Creative publishing & presentation | eScriptorium preserves page layout and transcription as structured exports usable in a publishing pipeline. Manimvox documents examples of narrated animation. Review output format and source rights for the selected publish step. 1 direct source attempts in this field did not yield usable evidence. [Source 1](https://escriptorium-tutorial.readthedocs.io/en/latest/export/) [Source 2](https://laplacianai.github.io/manimvox/) |
| Photography, restoration & color | CalibRaw’s open-source photo editor documents device-side model masks and a download-consent path for the required weights. The photography papers provide distinct learned restoration and editing methods; check the exact RAW camera and model. 1 direct source attempts in this field did not yield usable evidence. [Source 1](https://calibraw.dueckis.de) [Source 2](https://arxiv.org/abs/2611.16236) |
| Data art & scientific visualization | The AI+VIS survey describes modeling and visual analytics research. It provides discovery context and does not verify a current source grant or accessibility of a specific authoring app. [Source 1](https://arxiv.org/abs/2204.06504) |
| Physical, robotic & kinetic installations | MIT Media Lab’s Illuminate project shows camera-responsive audience projection. A Raspberry Pi 5 inference script documents a separate low-power still-image route. Test on the final display with its own capture and compute limits. [Source 1](https://www.media.mit.edu/projects/illuminate/overview/) [Source 2](https://codeberg.org/MightyOwlbear/Raspberry-Pi-5-Diffusion/raw/branch/main/README.md) |
| Performance, projection & stage media | IRCAM’s library catalog identifies Dicy2 for corpus-driven performance. Ossia describes live routing and mapping in a separate score. Rehearse latency and a fallback input before a live piece. [Source 1](https://www.ircam.fr/en/softwares) [Source 2](https://ossia.io/recording-streaming.html) |
| Fashion, textiles & wearable media | OpenTryOn separates its registry and client from individual try-on models and services. A web workflow preview does not establish garment fit or terms of any chosen hosted model. [Source 1](https://tryonlabs.github.io/opentryon/) |
| Accessible media & assistive creation | W3C defines audio description separately from speech captions. LiveAudio documents local draft captions over OBS. Make time to check terminology and timing with intended audiences. 1 direct source attempts in this field did not yield usable evidence. [Source 1](https://w3c.github.io/wai-website/media/av/description/) [Source 2](https://liveaudio.opencohost.com/) |
| Mobile, edge & on-device creation | SDAI’s store records identify separate Android and iOS distributions for mobile diffusion. F-Droid also records source-backed builds for short offline Whisper dictation. Check each package, memory budget and model separately. [Source 1](https://f-droid.org/en/packages/com.shifthackz.aisdv1.app.foss/) [Source 2](https://apps.apple.com/us/app/sdai-ai-image-generator/id6778314183) [Source 3](https://f-droid.org/en/packages/org.woheller69.whisper/) |
| Creative learning & authoring | Manim Voiceover documents selectable speech providers and script timing controls. The Multiview-to-3D Lab presents benchmark reconstruction cases for an instructional comparison. Specific claims in a lesson still need review. 1 direct source attempts in this field did not yield usable evidence. 1 captures reached the size bound. [Source 1](https://voiceover.manim.community/en/stable/services.html) [Source 2](https://shuyaogao.github.io/multiview-to-3d-lab/) |
| Archives, media restoration & collections | NARA’s format guidance provides a source for preserving original media. Arkindex and eScriptorium show recognition layers that can become separately corrected finding aids. 2 direct source attempts in this field did not yield usable evidence. [Source 1](https://www.archives.gov/preservation/formats) [Source 2](https://doc.teklia.com/arkindex/) [Source 3](https://escriptorium.eu/about/) |
| Emerging & cross-disciplinary creative AI | Hugging Face’s task cards distinguish image-conditioned text generation from similarity embeddings. Assign creative value to the actual operation, model and retained artifact. [Source 1](https://huggingface.co/tasks/image-text-to-text) [Source 2](https://huggingface.co/tasks/sentence-similarity) |
| Tactile, vibration and haptic media | The current paper connects visual scans to the assignment of physical material feel. Its experiment does not substitute for testing the intended actuator or accessible output. [Source 1](https://arxiv.org/abs/2610.17302) |
| Neural acoustics and responsive sound spaces | NeRAF documents a radiance and acoustics field that can be queried together. Its primary project evidence describes a research rendering workflow. Room-specific playback and reconstruction still need verification. [Source 1](https://amandinebtto.github.io/NeRAF/) |
| AI agents for code-authored media production | OpenMagia documents multiple creation backends in one editor. Different providers can produce assets or modify an editable project. Their commercial, platform and service terms are separate. 1 direct source attempts in this field did not yield usable evidence. 1 captures reached the size bound. [Source 1](https://openmagia.com/) |
| AI kinetic typography and animated lettering | LyriFont documents learned audio-driven typography for performance. Validate font licensing, timing control and display export independently. [Source 1](https://mae-creative-pc.github.io/projects/2023-24/LyriFont/LyriFont.html) |
| AI choreography and dance composition | MAESTRO documents procedural sequences and scene cues. PREMIERE’s research describes a distinct AI dance-toolbox scope. Performer experimentation needs a clear distinction between generated and manually composed movement. 1 direct source attempts in this field did not yield usable evidence. [Source 1](https://midotronn.github.io/MAESTRO/) [Source 2](https://premiere-project.eu/building-an-ai-toolbox-for-dance/) |
| AI-assisted textile and computational craft | Ink Blossom and StitchFoundry materials address AI-assisted embroidery. A screen preview, generated pattern and successful sew-out on the intended material are different forms of evidence. 1 direct source attempts in this field did not yield usable evidence. [Source 1](https://inkstitch.org/) [Source 2](https://arkxlab.github.io/projects_collection/ink-blossom.html) [Source 3](https://stitchfoundry.github.io/StitchFoundry/) |
| AI music notation and score recovery | The reviewed SCoIM source shows a MusicXML and MIDI authoring route, while IRCAM’s Dicy2 report describes corpus-guided composition. Validate notation, performer directions and musical phrasing after generation. 2 direct source attempts in this field did not yield usable evidence. [Source 1](https://www.ircam.fr/en/softwares) |
| Neural relighting and material recovery | AEGIR estimates area illumination from observed views. Sapiens2 normals can provide separate compositing inputs. The task, checkpoint and lighting assumptions matter before comparing visual outputs. [Source 1](https://darkgeekms.github.io/projects/aegir/) [Source 2](https://huggingface.co/facebook/sapiens2-normal-1b) |
| Olfactory and multisensory AI media | The paper discusses AI linking smell with interactive experience. Emission hardware, materials and authoring controls remain unverified in this search. [Source 1](https://arxiv.org/abs/2604.01650) |
| AI architectural visualization and spatial design | AgenticCAD illustrates prompt-directed changes alongside constrained sketches and dimensions. A built form still needs checked units, tolerances and fabrication constraints regardless of the AI route. [Source 1](https://agenticcad.github.io/agenticcad/) |
| Neural holography and light-field media | AEGIR's primary work uses Gaussian splatting and models area emitters for indoor inverse rendering. This differs from replaying a captured volumetric scene on a specific light-field monitor. [Source 1](https://darkgeekms.github.io/projects/aegir/) |
| Neural rigging and digital puppetry | Primary image-animation research learns motion from example images. Keypoint model documentation establishes a separate landmark output that can drive a rig if the host integration is verified. [Source 1](https://arxiv.org/abs/1910.02060) [Source 2](https://huggingface.co/tasks/keypoint-detection) |
| AI ceramics and archaeological illustration | PyPotteryTrace documents the use of SAM 2 to isolate archaeological drawings and export editable SVG. Measured silhouettes and scale still require checking against the scans. [Source 1](https://lrncrd.github.io/PyPottery/pypotterytrace/index.html) |
| AI parametric design and jewelry | AgenticCAD claims model-directed actions alongside parametric constraints. Check the edit history and dimensions in the exported project before machining. [Source 1](https://agenticcad.github.io/agenticcad/) |
| AI cartography and artistic maps | MapStory’s primary paper demonstrates model-assisted scene breakdowns for map videos with editable camera and annotation steps. The production-ready release and complete software terms were not established by that evidence alone. 4 direct source attempts in this field did not yield usable evidence. 1 captures reached the size bound. [Source 1](https://arxiv.org/abs/2505.21966) [Source 2](https://uist.acm.org/2025/papers/) |
| AI robotic painting and drawing | Form's authors study using new deformable materials in robotic manipulation. The result applies to the tested material/rig conditions and does not establish desktop deployability. [Source 1](https://form-robots.github.io/) |
| AI cel animation and inbetweening | The OpenToonz lineage page documents traditional ink, paint and compositing production. This provides workflow context. A verified learned in-betweening or coloring integration still needs its own release and grant. [Source 1](https://opentoonz.github.io/e/) |
| AI Foley and sound effects | FolAI illustrates synchronized, semantically aligned sound generation. FoleyForge describes editing a source sound with a language instruction. A paper's comparison clips do not themselves establish software terms or a production integration. 1 direct source attempts in this field did not yield usable evidence. [Source 1](https://arxiv.org/abs/2611.08695) [Source 2](https://arxiv.org/html/2611.08695v1) [Source 3](https://ispamm.github.io/FolAI/) |
| Learned media codecs and neural delivery | TQCodec studies high-bitrate neural music coding. A codec paper does not establish support in the target DAW, interchange container or archive. 1 direct source attempts in this field did not yield usable evidence. [Source 1](https://arxiv.org/abs/2603.01592) |
| AI assisted sound data art and corpus instruments | Parallax documents a maker's media work combining neural imagery and sonification. It does not establish a standalone licensed tool for repeating the process. [Source 1](https://www.sonify.io/parallax-ai-art/) |
| AI biosignal art and neurointeractive media | Brain2Music combines learned music representations with fMRI-derived information in a research setting. Its findings do not establish a wearable or live studio equivalent. [Source 1](https://google-research.github.io/seanet/brain2music/) |
| Neural procedural material authoring | VideoNeuMat studies extraction of learned material properties from generated video. DCC import, repeatability and lighting calibration still need an artifact-level check. 1 captures reached the size bound. [Source 1](https://wiro.ai/docs) [Source 2](https://registry.npmjs.org/three-ntc/latest) |
| Neural cameras and unconventional image capture | Low-light capture research documents model-specific assumptions about inputs and reconstruction. Assess calibration, latency and frame-to-frame consistency on a cited sensor setup. 1 captures reached the size bound. [Source 1](https://arxiv.org/abs/2507.11931) |
| AI origami, kirigami and paper engineering | The research examines sheet folding as a physically constrained task. A generated diagram or shape does not prove buildable folds, suitable stock or a current open app release. [Source 1](https://arxiv.org/abs/2603.29585) |
| AI landscape, garden and environmental design | The OpenCADIrrigation site documents an agent-assisted design path. LibreTerrain’s source describes procedural terrain work with different assumptions. Verify physical geometry and water behavior separately. [Source 1](https://opencadirrigation.com/) [Source 2](https://gitlab.com/libreterrain/libreterrain/-/raw/main/README.md) |
| Neural mosaic and stained-glass media | Visual Anagrams documents producing multiple views of one image with a generative method. Source examples do not establish the clarity or physical material constraints of a tile mosaic. [Source 1](https://dangeng.github.io/visual_anagrams/) |
| AI optical illusions and anamorphic media | Visual Anagrams presents a generative multi-view illusion. Its intended viewing transforms should be checked separately from any gallery presentation. [Source 1](https://dangeng.github.io/visual_anagrams/) |
| AI relief engraving and learned halftoning | Imprimatur's primary site demonstrates an image-to-roller geometry pathway. The reviewed page alone did not establish a neural step, file-level licenses or a physical material test. [Source 1](https://www.imprimatur.fyi/) |
| Neural brushstroke painting and drawn media | Current primary work separates the sequence of strokes from an image of the completed painting. A generated stroke program has a different verification burden from a flattened image. [Source 1](https://arxiv.org/abs/2511.13191) |
| AI color direction and palette-based media | HueForge's Unity documentation separates grouped recoloring and masks from optional AI palette and texture generation via a configured provider. Host and service requirements differ across these routes. [Source 1](https://ragendom69.github.io/hueforge/documentation.html) |
| AI collage, cut-paper composition and layered media | The Library of Congress project's description identifies a learned image cut-out approach in a collage workflow. Source-image permissions vary across collections and need their own review. [Source 1](https://libraryofcongress.github.io/collaging-space-time/) |
| AI stereo conversion and spatial video authoring | The stereo style-transfer paper treats the left and right views together. Test corresponding edges and viewing comfort before considering a result suitable for exhibition. [Source 1](https://arxiv.org/abs/1802.10591) |
| AI semantic editing of captured 3D scenes | Semantic Gaussians attaches foundation-model features to a 3D representation for selections. Inspect whether the exported selection preserves geometry and appearance in the intended editor. 1 direct source attempts in this field did not yield usable evidence. [Source 1](https://semantic-gaussians.github.io/) [Source 2](https://sharinka0715.github.io/semantic-gaussians/) |
| AI signing avatars and expressive gesture media | PHOSA documents sign-avatar modeling. Accuracy of signing, facial expression and how deaf users assess delivered material remain distinct from photorealism. [Source 1](https://naaapi.github.io/PHOSA/) |
| AI assisted audio plugin and DSP authoring | The Faustax paper and package describe a route for audio DSP authoring and differentiable workflows. Neural models and real-time hosts have their own format and performance constraints. [Source 1](https://arxiv.org/abs/2508.09126) [Source 2](https://dbraun.github.io/faustax/) |
| AI panoramic worlds and virtual tour creation | World-Shaper describes handling the spatial structure of panoramas. Inspect seams and geometry on the intended projection or headset before relying on a generated world. [Source 1](https://world-shaper-project.github.io/) |
| Learned garment simulation and digital clothing | Learning-based cloth work and ContourCraft tackle drape and interpenetration. Fit on a rig and physical pattern cutting remain separate checks. [Source 1](https://dancasas.github.io/projects/LearningBasedVirtualTryOn/) [Source 2](https://dolorousrtur.github.io/contourcraft/) |
| AI visual dubbing and translated performance | X-Dub's developer examples report long lip-sync sequences. The clips do not establish independent performance, rights to voices or a complete reusable software package. [Source 1](https://huggingface.co/ai4bharat/IndicF5) [Source 2](https://hjrphoebus.github.io/X-Dub/) |
| Neural video reshooting and camera control | The Model Hub listing identifies a reshooting artifact. The pass did not establish a complete deployable editing package or license coverage for any input and output workflow from this listing. [Source 1](https://huggingface.co/morphic/reshoot-anything/blob/main/README.md?code=true) |
| Neural denoising for real-time creative rendering | The current Cycles manual specifies render sampling and denoiser choices. Open Image Denoise documents learned denoising separately. Check image passes and preserve fine detail in the selected render. [Source 1](https://docs.blender.org/manual/en/latest/render/cycles/render_settings/sampling.html) [Source 2](https://www.openimagedenoise.org/) |
| AI assisted media quality and take selection | A current research paper tests detectors under specific synthesis families and perturbations. Model confidence on new footage and creative utility are separate claims from benchmark performance. [Source 1](https://api.nuget.org/v3-flatcontainer/tensorstack.media/index.json) [Source 2](https://arxiv.org/abs/2610.07216) |
| AI print separation and prepress authoring | rembg’s package documents learned foreground extraction. Imprimatur describes a separate print-oriented path. An alpha matte needs separate trim, color and press checks. 1 direct source attempts in this field did not yield usable evidence. [Source 1](https://pypi.org/project/rembg/) [Source 2](https://www.imprimatur.fyi/) |
| Interactive neural game worlds | AlayaWorld presents playable generated video world research. This source establishes an experimental method and does not by itself verify a maintained game authoring package or reusable assets. [Source 1](https://alaya-lab.github.io/AlayaWorld/) |
| AI audio patching and musical dataflow | Current neural audio research separates waveform synthesis from usable patch authoring. Patches need checked sample rates, inputs and predictable routing in the target environment. [Source 1](https://www.cirmmt.org/en/funding/ice-recipient-reports/cusson2025-26) [Source 2](https://arxiv.org/abs/2111.05011) |
| Learned light shaping and caustic art | The neural photon-mapping and indirect-light research pages show different treatments of glossy effects and caustics. Their comparisons do not establish support in a specific renderer or real-time device. [Source 1](https://cseweb.ucsd.edu/~viscomp/projects/EGSR23NeRT/) [Source 2](https://justinbenoist.github.io/publications/nppm.html) |
| Fulldome and planetarium AI media | The OpenSpace paper reports a planetarium AI pilot for public science presentations. Research on scene navigation did not establish compatible playback control for a specific dome. [Source 1](https://arxiv.org/abs/2601.20466) |
| Neural embroidery and stitch design | OpenStitch and StitchFoundry document file-based embroidery authoring routes, including separate optional AI inputs. Machine constraints and stitch density remain matters for a test-sew. 1 direct source attempts in this field did not yield usable evidence. [Source 1](https://cristianonescu.github.io/OpenStitch/) [Source 2](https://stitchfoundry.app/) |
| AI printmaking, risograph and editioned art | The Imprimatur site documents generating printable roller geometry. The accessible source does not establish an AI-specific open implementation or adequate pressure and registration on press. [Source 1](https://www.imprimatur.fyi/) |
| AI museum experiences and participatory exhibition media | The Norwegian National Museum documents semantic collection search using local AI. IIIF specifies separate audiovisual and visual delivery surfaces. Artefact records need original collection context and permission metadata. [Source 1](https://beta.nasjonalmuseet.no/2026/26/semantic-search-in-the-collection-using-local-ai/) [Source 2](https://iiif.io/api/av/) [Source 3](https://doc.teklia.com/arkindex/) |
| AI-assisted stop motion and frame animation | Eagle Animation supplies direct capture and editing context. Reviewed documentation does not by itself establish a learned cleanup or in-between feature. [Source 1](https://eagle-animation.com/) |
| Neural soundscape ecology and sonic art | SoundPlot describes neural audio synthesis with acoustic feature analysis. An artistic projection of embeddings must not be treated as verified species attribution. [Source 1](https://arxiv.org/abs/2601.12752) |
| Learned anamorphoses and distorted-view art | LookingGlass proposes generative anamorphoses with Laplacian pyramid warping. Check whether the intended display angle and physical geometry appear in the source evidence before treating a generated image as installation-ready. [Source 1](https://arxiv.org/abs/2504.08902) |
| Neural multiview and glasses-free display art | The neural light-field research page documents scene comparisons and the data demands of view-dependent effects. It does not verify a chosen display's view count, calibration or input format. [Source 1](https://light-field-neural-rendering.github.io/) |
| Neural astrophotography and celestial media | AstroSURE studies removal of noise from astronomical frames without clean ground truth. Creative dark-sky editing still requires preservation of sensor originals and a way to distinguish real small features from denoising artifacts. [Source 1](https://arxiv.org/abs/2604.16793) |
| AI tactile graphics and accessible relief media | Text2TactileGraphics and AltCanvas provide first-party design research for accessible visual authoring. The actual physical and experiential result needs an accessibility and fabrication review. 1 direct source attempts in this field did not yield usable evidence. [Source 1](https://ruihangao.github.io/Text2TactileGraphics/) [Source 2](https://shljessie.github.io/AltCanvas/) |
| Neural underwater photography, film and scene restoration | UDnet's authors describe neural restoration for green/blue cast and haze. Documented results should be interpreted for the actual water, lighting and camera conditions. [Source 1](https://alzayats.github.io/UDnet/) |
| Learned acoustic holography and instrument field media | The audio proceedings paper was reachable as a primary PDF. The current page capture does not establish maintained creative authoring software, a complete grant or hardware compatibility for deployment. 2 direct source attempts in this field did not yield usable evidence. [Source 1](https://arxiv.org/abs/2205.09256) [Source 2](https://arxiv.org/abs/2508.17626) [Source 3](https://eurasip.org/Proceedings/Eusipco/Eusipco2021/pdfs/0000121.pdf) |
| Learned calligraphy and robotic brush performance | CalliRewrite documents motion planning and manipulation for strokes. Inspect the actual arm control prerequisites and the output at the chosen ink, scale and paper. [Source 1](https://luoprojectpage.github.io/callirewrite/) |
| AI comic localization, relettering and translation | ComicTL describes a custom YOLO-Nano bubble detector and a separate translation step. Match text, lettering and reading order to the source page after the detections. [Source 1](https://comictl.kiuyha.dev/index.html) [Source 2](https://chromewebstore.google.com/detail/hmigninkgibhdckiaphhmbgcghochdjc) |
| AI furniture, timber and joinery design | EPFL’s Augmented Carpentry project documents model-assisted alignment on fabrication tools. Establish the tool setup and the physical reference alignment before assessing the workflow. 1 direct source attempts in this field did not yield usable evidence. 1 captures reached the size bound. [Source 1](https://ibois-epfl.github.io/augmented-carpentry/) [Source 2](https://www.epfl.ch/labs/ibois/augmented-carpentry/) |
| AI game localization and playable translations | Taarib's own guide scopes game localization to titles the user can localize. Compare translated text and play-test context separately from licensing the tool. [Source 1](https://abdallah28r.github.io/taarib/en/) |
| AI stage lighting and show control | Ossia and QLC+ document timeline/control options. The camera model's detections and the behavior of a real console or fixture are distinct verification tasks. [Source 1](https://docs.godotengine.org/en/stable/tutorials/inputs/index.html) [Source 2](https://ossia.io/projection-mapping.html) [Source 3](https://lacylights.com/) [Source 4](https://qlcplus.org/) |
| AI photobook, album sequencing and editorial layout | The visual cover study connects generated art to music metadata. It does not verify editable book spreads, pagination or printer-ready attachments. [Source 1](https://arxiv.org/abs/2408.01651) |
| AI seamless loops, sample design and DAW-ready stems | WaivePulse describes an offline suite. A captured product page does not establish every underlying model grant or seamless playback at chosen tempos. [Source 1](https://huggingface.co/spaces/ACE-Step/Ace-Step) [Source 2](https://waivepulse.com/) |
| Neural yarn modeling and machine knitting | The inverse procedural yarn study reconstructs parameters from images down to fiber detail. A visual yarn model does not give verified physical fiber composition or production tolerances. [Source 1](https://arxiv.org/abs/2303.00154) |
| Neural watermarking for printed creative media | StegaStamp describes hiding information in imagery intended for digital display or printing. Paper, capture and lighting conditions matter when evaluating whether the decoded mark survives. [Source 1](https://www.matthewtancik.com/stegastamp) |
| Learned halftones and neural print screening | The archived deep-halftoning research describes a learned reversible binary-pixel arrangement with output examples. Exporting a monochrome image does not establish usable ink density or fidelity on the target press. 1 captures reached the size bound. [Source 1](https://nikronic.com/projects/deep-halftoning_project/) [Source 2](https://openaccess.thecvf.com/content/ICCV2021/html/Xia_Deep_Halftoning_With_Reversible_Binary_Pattern_ICCV_2021_paper.html) |
| AI brick sculpture and agent-assisted construction design | BrickGPT and BrickWright report text-directed brick planning and stability evaluation. Instructions or rendered previews do not establish a physical build with the creator's actual part inventory. [Source 1](https://avalovelace1.github.io/BrickGPT/) [Source 2](https://avalovelace1.github.io/brickwright/) |
| Neural optical holography and computational displays | Current lab pages show neural and time-multiplexed holography. Odak provides optics software context. Physical display and camera calibration terms depend on the implementation. 1 captures reached the size bound. [Source 1](https://cinescope-wkr.github.io/pado-hologram/) [Source 2](https://light.princeton.edu/publication/artifact-resilient-holography/) [Source 3](https://www.computationalimaging.org/publications/neuralholography/) [Source 4](https://www.computationalimaging.org/publications/time-multiplexed-neural-holography/) [Source 5](https://www.kaanaksit.com/odak/cgh/) [Source 6](https://www.kaanaksit.com/odak/installation/) |
| AI poetry, kinetic literature and language installations | RiTa and JHAVÉ provide procedural writing or generative text context. The application assessment still needs an actual model contribution before entry as an AI tool. [Source 1](https://jhave.com/) [Source 2](https://rednoise.org/rita/) |
| Neural hair, fur and strand-groom authoring | StrandHead, HairGPT and Digital Salon document learned approaches to 3D hair. Strand controls, rig compatibility and safe export depend on the chosen implementation. 2 direct source attempts in this field did not yield usable evidence. [Source 1](https://digital-salon.github.io/) [Source 2](https://haiminluo.github.io/hairgpt/) [Source 3](https://xiaokunsun.github.io/StrandHead.github.io/) |
| Neural smoke, fluid capture and editable VFX fields | HyFluid documents a learned scene reconstruction workflow for fluid dynamics. Verify capture and rendering constraints separately from any reusable scene or footage export. 1 direct source attempts in this field did not yield usable evidence. [Source 1](https://kovenyu.com/HyFluid/) |
| AI pattern transcription and symbolic craft verification | The StitchFoundry source and model references distinguish an assisted artwork stage from geometrically validated embroidery. Save the layout and review the result before a machine run. [Source 1](https://stitchfoundry.github.io/StitchFoundry/) [Source 2](https://huggingface.co/Qwen/Qwen3.5-4B) |
| Neural rhythm tracking and synchronized visual media | The cited primary research evaluates music-conditioned generation or regularity in movement. Reproducing projections synced to a specific audio and venue remains a separate design task. [Source 1](https://arxiv.org/abs/2108.03576) [Source 2](https://arxiv.org/abs/2407.21658) |
| Foundation-model dioramas and compositional scene assembly | The Diorama authors document single-view scene reconstruction. Hidden surfaces and unobserved dimensions remain uncertain even when the composition looks plausible. [Source 1](https://3dlg-hcvc.github.io/diorama/) |
| AI planner layouts, book arts and binding-aware publishing | Booklet publishes imposition documentation and Rosette documents the publishing workflow. Neither a generated page image nor an OCR layer guarantees readable signatures or ready-to-bind output. [Source 1](https://docs.hornpenguin.com/projects/booklet/en/latest/index.html) [Source 2](https://www.rosette.dev/docs) |
| AI shadow puppetry and hand-shadow performance | First-party CUNY and paper sources describe physical projection and shadow representations. A specific art installation requires checks for actual light geometry, interaction and stage timing. 2 direct source attempts in this field did not yield usable evidence. [Source 1](https://academicworks.cuny.edu/ny_pubs/1252/) [Source 2](https://arxiv.org/abs/2408.10360) |
| AI-agent pixel art, sprites and palette-controlled animation | Gridfab and Pixelbolt document separated authoring routes for grid-based artwork. Palette, raster scale and sprite export need an inspection after any agent edit. 1 direct source attempts in this field did not yield usable evidence. [Source 1](https://gitlab.com/azrazalea/gridfab) [Source 2](https://skulitom.github.io/Pixelbolt/) |
| Learned robotic shadow performance and inverse silhouette control | Duke's work concerns learned robotic shadow silhouettes. CUNY and Sunway document separate puppet preservation and performance research. None of those contexts by itself clears transferable production code. [Source 1](https://generalroboticslab.com/shadow) [Source 2](https://academicworks.cuny.edu/ny_pubs/1252/) [Source 3](https://arxiv.org/abs/2607.22434) [Source 4](https://sunwayuniversity.edu.my/research/centres/SCDHCH/woyae-tangae) |
| AI score transcription correction and part layout | Audiveris and current primary score research distinguish automatic music recognition from correction. Check music structure and exact export before typesetting the target edition. 3 direct source attempts in this field did not yield usable evidence. [Source 1](https://arxiv.org/abs/2611.17870) [Source 2](https://audiveris.github.io/audiveris/) |
| Archival film restoration and preservation | Current papers separate synthetic defect creation from reconstructing real film frames. Release and configuration work also showed why training data, learned weights and archival reuse rights need independent review. 1 direct source attempts in this field did not yield usable evidence. [Source 1](https://arxiv.org/abs/2607.02131) [Source 2](https://arxiv.org/abs/2607.21219) [Source 3](https://openaccess.thecvf.com/content/CVPR2025/html/Mao_Making_Old_Film_Great_Again_Degradation-aware_State_Space_Model_for_CVPR_2025_paper.html) [Source 4](https://openaccess.thecvf.com/content/WACV2024/html/Lin_Restoring_Degraded_Old_Films_With_Recursive_Recurrent_Transformer_Networks_WACV_2024_paper.html) [Source 5](https://seungjunnah.github.io/Datasets/reds.html) [Source 6](https://www.archives.gov/preservation/formats) [Source 7](https://www.kaggle.com/datasets/absolutedegradation/absolutecinema-real-scene-split-full) [Source 8](https://www.loc.gov/preservation/digital/formats/fdd/fdd000395.shtml) |
| Camera-reactive projection installations | MediaPipe’s browser Pose Landmarker returns tracked points; TrackOSC describes routing landmarks to a separate controller. Geometry and performer timing require testing on the actual surface. [Source 1](https://ai.google.dev/edge/mediapipe/solutions/vision/pose_landmarker/web_js) [Source 2](https://apps.apple.com/app/trackosc/id6795593815) |
| Learned projector compensation and exhibit color | The SIComp and projector-compensation projects study learned correction for the appearance of a projected image on a real surface. Calibrate the selected camera/projector setup and check changes in ambient light. 2 direct source attempts in this field did not yield usable evidence. [Source 1](https://hai-bo-li.github.io/SIComp/) [Source 2](https://bingyaohuang.github.io/projects/projector-compensation/) |
| Spatial audio and sound dramaturgy | AMBIT documents 44.1 kHz FOA generation and editing. PhysWave documents explicit trajectories and short 16 kHz FOA clips. SAID estimates event direction on a panoramic map. Each has a separate model or data review, and the physical or headphone decoder needs its own listening comparison. [Source 1](https://huggingface.co/api/spaces/hugging-apps/said-semantic-acoustic-imaging) [Source 2](https://huggingface.co/api/spaces/hugging-apps/said-semantic-acoustic-imaging/tree/main) [Source 3](https://huggingface.co/api/spaces/hugging-apps/said-semantic-acoustic-imaging/runtime) [Source 4](https://huggingface.co/spaces/hugging-apps/said-semantic-acoustic-imaging/raw/main/app.py) [Source 5](https://huggingface.co/spaces/hugging-apps/said-semantic-acoustic-imaging/raw/main/requirements.txt) [Source 6](https://huggingface.co/spaces/hugging-apps/said-semantic-acoustic-imaging/raw/main/README.md) [Source 7](https://huggingface.co/api/models/IN03X/SAID) [Source 8](https://huggingface.co/docs/hub/spaces-zerogpu) |
| Live production accessibility and routed captions | LiveAudio publishes an ONNX Whisper path to OBS for Windows and Linux. LocalVocal provides a separate native filter, including a Mac package matrix. StagePulse documents provider-based stage routing. Validate caption timing in the actual venue or stream. 4 direct source attempts in this field did not yield usable evidence. [Source 1](https://liveaudio.opencohost.com/) [Source 2](https://obsproject.com/forum/resources/localvocal-local-live-captions-translation-on-the-go.1769/) [Source 3](https://ossia.io/recording-streaming.html) |
| Cultural heritage layout recognition and transcription | Kraken, eScriptorium and Arkindex document separate recognition and correction workflows for scans and IIIF. Select a model appropriate for the writing and verify the reading order in PAGE or ALTO output. 10 direct source attempts in this field did not yield usable evidence. [Source 1](https://escriptorium.eu/about/) [Source 2](https://doc.teklia.com/arkindex_tutorial/export/) [Source 3](https://pypi.org/project/kraken/) |
| Learned optics and post-production lens tools | CalibRaw uses learned masks for targeted photo edits. Caliscope’s learned tracking sits alongside lens calibration and checks a multi-camera rig. Separate these uses from conventional optics calibration and verify the chosen output. 2 direct source attempts in this field did not yield usable evidence. 1 captures reached the size bound. [Source 1](https://calibraw.dueckis.de) [Source 2](https://mprib.github.io/caliscope/reconstruction/) [Source 3](https://discorpy.readthedocs.io/) |

## Search and review counts

117 creative fields; 1342/1342 repository queries attempted; 35/35 model-task queries attempted. 85033 distinct source candidates and 1490 model leads. 96 detailed profiles and 21 additional screened discoveries. Source gaps: 0 failed repository queries, 0 partial repository queries, 253 bounded repository queries, 0 failed model-task queries and 0 web ecosystem gaps. Raw search candidates include duplicates of known tools, excluded projects and projects awaiting review; they are not verified recommendations.

## Research beyond GitHub

- **gitlab** · searched: Canonical GitLab sources returned the complete eScriptorium and Arkindex Community software grants and current release lists. The public Teklia web UI returned an access challenge for some pages. Its public API provided the exact grant and release data. 5 direct attempts were unavailable, access-gated or bounded. [Source](https://gitlab.com/scripta/escriptorium/-/raw/develop/LICENSE) [Source](https://gitlab.com/api/v4/projects/scripta%2Fescriptorium/releases?per_page=5) [Source](https://gitlab.teklia.com/api/v4/projects/arkindex%2Fbackend/repository/files/LICENSE/raw?ref=develop) [Source](https://gitlab.teklia.com/api/v4/projects/arkindex%2Fbackend/releases?per_page=5)
- **codeberg** · searched: Direct project endpoints returned a Raspberry Pi 5 diffusion tool’s software grant and source. Broader topical repository search endpoints returned HTTP 429. The direct evidence does not establish comprehensive Codeberg search. 13 direct attempts were unavailable, access-gated or bounded. [Source](https://codeberg.org/MightyOwlbear/Raspberry-Pi-5-Diffusion/raw/branch/main/README.md) [Source](https://codeberg.org/MightyOwlbear/Raspberry-Pi-5-Diffusion/raw/branch/main/LICENSE) [Source](https://codeberg.org/api/v1/repos/MightyOwlbear/Raspberry-Pi-5-Diffusion)
- **sourcehut** · searched: The Diffuser project files were read directly, including the MIT license and Cargo manifest. A hard-coded local dependency path still blocks the documented portable build. Some SourceHut views returned an access error. 3 direct attempts were unavailable, access-gated or bounded. [Source](https://git.sr.ht/~rockerboo/diffuser/blob/main/LICENSE) [Source](https://git.sr.ht/~rockerboo/diffuser/blob/main/Cargo.toml) [Source](https://git.sr.ht/~rockerboo/diffuser/refs)
- **packages** · searched: Registry results identified the current Kraken OCR and Caliscope packages, plus a separate Ableton connector. The package and model terms were checked independently. One direct attempt was unavailable, access-gated or bounded. [Source](https://pypi.org/project/kraken/) [Source](https://pypi.org/project/caliscope/) [Source](https://pypi.org/project/ableton-studio-mcp/)
- **creative-plugins** · searched: The OBS resource documents how the LocalVocal audio filter writes captions to a text source or file. The release package matrix is version-specific. The reviewed Blender extension listings provide a separate source host for discovery. 6 direct attempts were unavailable, access-gated or bounded. [Source](https://obsproject.com/forum/resources/localvocal-local-live-captions-translation-on-the-go.1769/) [Source](https://extensions.blender.org/add-ons/?q=ai)
- **project-sites** · searched: LiveAudio, CalibRaw and Caliscope project sites provided separate documentation for model-backed captioning, photo masks and motion capture. These substantiate the documented routes; reproduction still needs evidence. [Source](https://liveaudio.opencohost.com/) [Source](https://calibraw.dueckis.de) [Source](https://mprib.github.io/caliscope/)
- **research-code** · searched: The DAHN historical-document paper describes actual Kraken/eScriptorium integration. Current SyncDreamer documentation and primary research provide its released code and model links. The evidence has different version and workflow scopes. 2 direct attempts were unavailable, access-gated or bounded. [Source](https://journals.openedition.org/jtei/5306) [Source](https://arxiv.org/abs/2309.03453) [Source](https://liuyuan-pal.github.io/SyncDreamer/)
- **international** · searched: The French eScriptorium and Arkindex project docs describe institution-backed IIIF workflows, and IRCAM provides corpus-based composition sources. Sinhala speech model documentation supplied an independent model-artifact reference. 7 direct attempts were unavailable, access-gated or bounded. [Source](https://escriptorium.eu/about/) [Source](https://www.teklia.com/arkindex-tutorial) [Source](https://www.ircam.fr/en/softwares) [Source](https://huggingface.co/SinhaSpeech/whisper-small-sinhala-run12-best)

## Collection limitations

- images: bounded or incomplete query: topic:diffusion is:public fork:false archived:false (1000 of 1541 matches sampled)
- images: bounded or incomplete query: AI image generation pushed:>=2026-10-22 is:public fork:false archived:false (1000 of 1715 matches sampled)
- images: bounded or incomplete query: AI image generation is:public fork:false archived:false (1000 of 16537 matches sampled)
- video: bounded or incomplete query: AI video pushed:>=2026-10-22 is:public fork:false archived:false (1000 of 17298 matches sampled)
- video: bounded or incomplete query: AI video created:>=2026-10-22 is:public fork:false archived:false (1000 of 11617 matches sampled)
- video: bounded or incomplete query: AI video is:public fork:false archived:false (1000 of 99330 matches sampled)
- video: bounded or incomplete query: topic:video-generation pushed:>=2026-10-22 is:public fork:false archived:false (999 of 2300 matches sampled)
- video: bounded or incomplete query: topic:video-generation created:>=2026-10-22 is:public fork:false archived:false (499 of 1040 matches sampled)
- video: bounded or incomplete query: topic:video-generation is:public fork:false archived:false (1000 of 5648 matches sampled)
- audio: bounded or incomplete query: topic:music-generation is:public fork:false archived:false (1000 of 1460 matches sampled)
- audio: bounded or incomplete query: AI audio pushed:>=2026-10-22 is:public fork:false archived:false (1000 of 4389 matches sampled)
- audio: bounded or incomplete query: AI audio created:>=2026-10-22 is:public fork:false archived:false (1000 of 2327 matches sampled)
- audio: bounded or incomplete query: AI audio is:public fork:false archived:false (1000 of 31102 matches sampled)
- 3d: bounded or incomplete query: 3D generation is:public fork:false archived:false (1000 of 6279 matches sampled)
- 3d: bounded or incomplete query: topic:3d-reconstruction is:public fork:false archived:false (1000 of 2186 matches sampled)
- web: bounded or incomplete query: topic:webgpu pushed:>=2026-10-22 is:public fork:false archived:false (1000 of 1503 matches sampled)
- web: bounded or incomplete query: topic:webgpu is:public fork:false archived:false (1000 of 3916 matches sampled)
- xr: bounded or incomplete query: AI WebXR is:public fork:false archived:false (199 of 203 matches sampled)
- xr: bounded or incomplete query: AI VR pushed:>=2026-10-22 is:public fork:false archived:false (299 of 419 matches sampled)
- xr: bounded or incomplete query: AI VR created:>=2026-10-22 is:public fork:false archived:false (199 of 226 matches sampled)
- xr: bounded or incomplete query: AI VR is:public fork:false archived:false (1000 of 3157 matches sampled)
- computational: bounded or incomplete query: AI creative coding is:public fork:false archived:false (1000 of 1056 matches sampled)
- computational: bounded or incomplete query: topic:generative-art pushed:>=2026-10-22 is:public fork:false archived:false (393 of 1272 matches sampled)
- computational: bounded or incomplete query: topic:generative-art created:>=2026-10-22 is:public fork:false archived:false (196 of 597 matches sampled)
- computational: bounded or incomplete query: topic:generative-art is:public fork:false archived:false (1000 of 4891 matches sampled)
- fabrication: bounded or incomplete query: AI CAD is:public fork:false archived:false (1000 of 3831 matches sampled)
- gaming: bounded or incomplete query: AI game assets is:public fork:false archived:false (800 of 801 matches sampled)
- gaming: bounded or incomplete query: AI blender is:public fork:false archived:false (1000 of 2223 matches sampled)
- motion: bounded or incomplete query: motion generation is:public fork:false archived:false (1000 of 1676 matches sampled)
- avatars: bounded or incomplete query: AI avatar is:public fork:false archived:false (1000 of 6532 matches sampled)
- avatars: bounded or incomplete query: lip sync is:public fork:false archived:false (1000 of 2792 matches sampled)
- capture: bounded or incomplete query: topic:gaussian-splatting is:public fork:false archived:false (1000 of 1186 matches sampled)
- capture: bounded or incomplete query: neural reconstruction is:public fork:false archived:false (1000 of 1391 matches sampled)
- editing: bounded or incomplete query: AI video editing pushed:>=2026-10-22 is:public fork:false archived:false (1000 of 1325 matches sampled)
- editing: bounded or incomplete query: AI video editing is:public fork:false archived:false (1000 of 4679 matches sampled)
- editing: bounded or incomplete query: AI subtitle is:public fork:false archived:false (1000 of 2567 matches sampled)
- vector: bounded or incomplete query: AI SVG is:public fork:false archived:false (1000 of 2353 matches sampled)
- storytelling: bounded or incomplete query: AI storyboard is:public fork:false archived:false (1000 of 2203 matches sampled)
- storytelling: bounded or incomplete query: AI comic is:public fork:false archived:false (1000 of 3282 matches sampled)
- publishing: bounded or incomplete query: AI presentation pushed:>=2026-10-22 is:public fork:false archived:false (1000 of 1157 matches sampled)
- publishing: bounded or incomplete query: AI presentation is:public fork:false archived:false (1000 of 9393 matches sampled)
- publishing: bounded or incomplete query: AI publishing pushed:>=2026-10-22 is:public fork:false archived:false (1000 of 1039 matches sampled)
- publishing: bounded or incomplete query: AI publishing is:public fork:false archived:false (1000 of 4718 matches sampled)
- photography: bounded or incomplete query: AI colorization is:public fork:false archived:false (1000 of 5162 matches sampled)
- visualization: bounded or incomplete query: AI visualization pushed:>=2026-10-22 is:public fork:false archived:false (1000 of 3099 matches sampled)
- visualization: bounded or incomplete query: AI visualization created:>=2026-10-22 is:public fork:false archived:false (1000 of 1759 matches sampled)
- visualization: bounded or incomplete query: AI visualization is:public fork:false archived:false (1000 of 40306 matches sampled)
- visualization: bounded or incomplete query: AI data art is:public fork:false archived:false (1000 of 1080 matches sampled)
- education: bounded or incomplete query: AI explainer pushed:>=2026-10-22 is:public fork:false archived:false (1000 of 6472 matches sampled)
- education: bounded or incomplete query: AI explainer created:>=2026-10-22 is:public fork:false archived:false (1000 of 4220 matches sampled)
- education: bounded or incomplete query: AI explainer is:public fork:false archived:false (1000 of 43571 matches sampled)
- frontier: bounded or incomplete query: AI creative tools is:public fork:false archived:false (1000 of 2186 matches sampled)
- frontier: bounded or incomplete query: AI multimedia is:public fork:false archived:false (1000 of 1242 matches sampled)
- agent-media-production: bounded or incomplete query: AI agent animation pushed:>=2026-10-22 is:public fork:false archived:false (300 of 314 matches sampled)
- procedural-materials: bounded or incomplete query: neural material is:public fork:false archived:false (1000 of 1419 matches sampled)
- underwater-media: bounded or incomplete query: underwater image enhancement is:public fork:false archived:false (1000 of 1103 matches sampled)
- generative-literature: bounded or incomplete query: AI poetry is:public fork:false archived:false (900 of 1123 matches sampled)
- book-arts: bounded or incomplete query: AI book design is:public fork:false archived:false (600 of 957 matches sampled)
- agent-pixel-art: bounded or incomplete query: AI pixel art is:public fork:false archived:false (300 of 1547 matches sampled)
- images: bounded or incomplete query: topic:diffusion is:public fork:false archived:false (1000 of 1541 matches sampled)
- cel-animation: bounded or incomplete query: animation colorization is:public fork:false archived:false (1000 of 2548 matches sampled)
- images: bounded or incomplete query: AI image generation language:TypeScript is:public fork:false archived:false (1000 of 2637 matches sampled)
- editing: bounded or incomplete query: AI video editing language:Python is:public fork:false archived:false (1000 of 1333 matches sampled)
- fabrication: bounded or incomplete query: AI CAD language:Python is:public fork:false archived:false (1000 of 1376 matches sampled)
- xr: bounded or incomplete query: AI WebXR editor is:public fork:false archived:false (4 of 5 matches sampled)
- frontier: bounded or incomplete query: AI media created:>=2026-11-02 is:public fork:false archived:false (1000 of 1398 matches sampled)
- video: bounded or incomplete query: topic:video-generation is:public fork:false archived:false (999 of 5649 matches sampled)
- capture: bounded or incomplete query: topic:gaussian-splatting is:public fork:false archived:false (1000 of 1186 matches sampled)
- cel-animation: bounded or incomplete query: animation colorization is:public fork:false archived:false (1000 of 2548 matches sampled)
- images: bounded or incomplete query: topic:diffusion created:<2025-01-01 is:public fork:false archived:false (700 of 786 matches sampled)
- images: bounded or incomplete query: topic:diffusion created:>=2025-01-01 is:public fork:false archived:false (500 of 755 matches sampled)
- images: bounded or incomplete query: AI image generation created:<2025-01-01 is:public fork:false archived:false (500 of 3077 matches sampled)
- images: bounded or incomplete query: AI image generation created:>=2025-01-01 is:public fork:false archived:false (500 of 13464 matches sampled)
- video: bounded or incomplete query: AI video created:<2025-01-01 is:public fork:false archived:false (700 of 11356 matches sampled)
- video: bounded or incomplete query: AI video created:>=2025-01-01 is:public fork:false archived:false (700 of 88003 matches sampled)
- video: bounded or incomplete query: topic:video-generation created:>=2025-01-01 is:public fork:false archived:false (700 of 5271 matches sampled)
- audio: bounded or incomplete query: topic:music-generation created:>=2025-01-01 is:public fork:false archived:false (700 of 963 matches sampled)
- audio: bounded or incomplete query: AI audio created:<2025-01-01 is:public fork:false archived:false (500 of 3932 matches sampled)
- audio: bounded or incomplete query: AI audio created:>=2025-01-01 is:public fork:false archived:false (500 of 27174 matches sampled)
- 3d: bounded or incomplete query: 3D generation created:<2025-01-01 is:public fork:false archived:false (500 of 2008 matches sampled)
- 3d: bounded or incomplete query: 3D generation created:>=2025-01-01 is:public fork:false archived:false (500 of 4271 matches sampled)
- 3d: bounded or incomplete query: topic:3d-reconstruction created:<2025-01-01 is:public fork:false archived:false (500 of 1118 matches sampled)
- 3d: bounded or incomplete query: topic:3d-reconstruction created:>=2025-01-01 is:public fork:false archived:false (500 of 1068 matches sampled)
- web: bounded or incomplete query: topic:webgpu created:<2025-01-01 is:public fork:false archived:false (700 of 751 matches sampled)
- web: bounded or incomplete query: topic:webgpu created:>=2025-01-01 is:public fork:false archived:false (500 of 3168 matches sampled)
- xr: bounded or incomplete query: AI WebXR created:>=2025-01-01 is:public fork:false archived:false (99 of 186 matches sampled)
- xr: bounded or incomplete query: AI VR created:<2025-01-01 is:public fork:false archived:false (700 of 800 matches sampled)
- xr: bounded or incomplete query: AI VR created:>=2025-01-01 is:public fork:false archived:false (299 of 2359 matches sampled)
- computational: bounded or incomplete query: AI creative coding created:>=2025-01-01 is:public fork:false archived:false (700 of 966 matches sampled)
- computational: bounded or incomplete query: topic:generative-art created:<2025-01-01 is:public fork:false archived:false (500 of 1936 matches sampled)
- computational: bounded or incomplete query: topic:generative-art created:>=2025-01-01 is:public fork:false archived:false (393 of 2956 matches sampled)
- fabrication: bounded or incomplete query: AI CAD created:>=2025-01-01 is:public fork:false archived:false (500 of 3477 matches sampled)
- gaming: bounded or incomplete query: AI blender created:>=2025-01-01 is:public fork:false archived:false (500 of 1988 matches sampled)
- motion: bounded or incomplete query: motion generation created:>=2025-01-01 is:public fork:false archived:false (700 of 1249 matches sampled)
- avatars: bounded or incomplete query: AI avatar created:<2025-01-01 is:public fork:false archived:false (700 of 705 matches sampled)
- avatars: bounded or incomplete query: AI avatar created:>=2025-01-01 is:public fork:false archived:false (500 of 5830 matches sampled)
- avatars: bounded or incomplete query: lip sync created:<2025-01-01 is:public fork:false archived:false (500 of 698 matches sampled)
- avatars: bounded or incomplete query: lip sync created:>=2025-01-01 is:public fork:false archived:false (500 of 2096 matches sampled)
- capture: bounded or incomplete query: topic:gaussian-splatting created:>=2025-01-01 is:public fork:false archived:false (900 of 933 matches sampled)
- capture: bounded or incomplete query: neural reconstruction created:>=2025-01-01 is:public fork:false archived:false (700 of 732 matches sampled)
- editing: bounded or incomplete query: AI video editing created:>=2025-01-01 is:public fork:false archived:false (700 of 4520 matches sampled)
- editing: bounded or incomplete query: AI subtitle created:>=2025-01-01 is:public fork:false archived:false (700 of 2310 matches sampled)
- vector: bounded or incomplete query: AI SVG created:>=2025-01-01 is:public fork:false archived:false (500 of 2155 matches sampled)
- typography: bounded or incomplete query: AI typography created:>=2025-01-01 is:public fork:false archived:false (700 of 823 matches sampled)
- storytelling: bounded or incomplete query: AI storyboard created:>=2025-01-01 is:public fork:false archived:false (500 of 2147 matches sampled)
- storytelling: bounded or incomplete query: AI comic created:>=2025-01-01 is:public fork:false archived:false (500 of 3125 matches sampled)
- publishing: bounded or incomplete query: AI presentation created:<2025-01-01 is:public fork:false archived:false (500 of 1358 matches sampled)
- publishing: bounded or incomplete query: AI presentation created:>=2025-01-01 is:public fork:false archived:false (500 of 8038 matches sampled)
- publishing: bounded or incomplete query: AI publishing created:>=2025-01-01 is:public fork:false archived:false (500 of 4545 matches sampled)
- photography: bounded or incomplete query: AI colorization created:<2025-01-01 is:public fork:false archived:false (500 of 1007 matches sampled)
- photography: bounded or incomplete query: AI colorization created:>=2025-01-01 is:public fork:false archived:false (500 of 4156 matches sampled)
- visualization: bounded or incomplete query: AI visualization created:<2025-01-01 is:public fork:false archived:false (500 of 5221 matches sampled)
- visualization: bounded or incomplete query: AI visualization created:>=2025-01-01 is:public fork:false archived:false (500 of 35087 matches sampled)
- visualization: bounded or incomplete query: AI data art created:>=2025-01-01 is:public fork:false archived:false (700 of 782 matches sampled)
- performance: bounded or incomplete query: AI live visuals created:>=2025-01-01 is:public fork:false archived:false (700 of 805 matches sampled)
- education: bounded or incomplete query: AI explainer created:<2025-01-01 is:public fork:false archived:false (500 of 2134 matches sampled)
- education: bounded or incomplete query: AI explainer created:>=2025-01-01 is:public fork:false archived:false (500 of 41451 matches sampled)
- frontier: bounded or incomplete query: AI creative tools created:>=2025-01-01 is:public fork:false archived:false (500 of 1788 matches sampled)
- frontier: bounded or incomplete query: AI multimedia created:>=2025-01-01 is:public fork:false archived:false (700 of 981 matches sampled)
- architectural-media: bounded or incomplete query: AI architectural visualization created:>=2025-01-01 is:public fork:false archived:false (700 of 964 matches sampled)
- procedural-materials: bounded or incomplete query: neural material created:<2025-01-01 is:public fork:false archived:false (700 of 778 matches sampled)
- procedural-materials: bounded or incomplete query: neural material created:>=2025-01-01 is:public fork:false archived:false (500 of 641 matches sampled)
- underwater-media: bounded or incomplete query: underwater image enhancement created:>=2025-01-01 is:public fork:false archived:false (500 of 602 matches sampled)
- generative-literature: bounded or incomplete query: AI poetry created:>=2025-01-01 is:public fork:false archived:false (700 of 839 matches sampled)
- book-arts: bounded or incomplete query: AI book design created:>=2025-01-01 is:public fork:false archived:false (500 of 775 matches sampled)
- cel-animation: bounded or incomplete query: animation colorization created:<2025-01-01 is:public fork:false archived:false (500 of 1093 matches sampled)
- cel-animation: bounded or incomplete query: animation colorization created:>=2025-01-01 is:public fork:false archived:false (500 of 1455 matches sampled)
- images: bounded or incomplete query: AI image generation language:TypeScript created:>=2025-01-01 is:public fork:false archived:false (500 of 2267 matches sampled)
- editing: bounded or incomplete query: AI video editing language:Python created:>=2025-01-01 is:public fork:false archived:false (700 of 1289 matches sampled)
- fabrication: bounded or incomplete query: AI CAD language:Python created:>=2025-01-01 is:public fork:false archived:false (500 of 1313 matches sampled)
- xr: bounded or incomplete query: AI WebXR editor created:>=2025-01-01 is:public fork:false archived:false (3 of 4 matches sampled)
- frontier: bounded or incomplete query: AI media created:<2025-01-01 is:public fork:false archived:false (500 of 2659 matches sampled)
- frontier: bounded or incomplete query: AI media created:>=2025-01-01 is:public fork:false archived:false (500 of 25493 matches sampled)
- 3d: bounded or incomplete query: 3D generation created:>=2025-01-01 created:<2026-01-01 is:public fork:false archived:false (300 of 6279 matches sampled)
- 3d: bounded or incomplete query: 3D generation created:>=2026-01-01 created:<2026-07-01 is:public fork:false archived:false (300 of 6279 matches sampled)
- 3d: bounded or incomplete query: 3D generation created:>=2026-07-01 created:<2026-11-18 is:public fork:false archived:false (300 of 6279 matches sampled)
- 3d: bounded or incomplete query: topic:3d-reconstruction created:>=2025-01-01 created:<2026-01-01 is:public fork:false archived:false (300 of 2187 matches sampled)
- 3d: bounded or incomplete query: topic:3d-reconstruction created:>=2026-01-01 created:<2026-07-01 is:public fork:false archived:false (300 of 2187 matches sampled)
- 3d: bounded or incomplete query: topic:3d-reconstruction created:>=2026-07-01 created:<2026-11-18 is:public fork:false archived:false (300 of 2187 matches sampled)
- audio: bounded or incomplete query: AI audio created:>=2025-01-01 created:<2026-01-01 is:public fork:false archived:false (300 of 31110 matches sampled)
- audio: bounded or incomplete query: AI audio created:>=2026-01-01 created:<2026-07-01 is:public fork:false archived:false (300 of 31110 matches sampled)
- audio: bounded or incomplete query: AI audio created:>=2026-07-01 created:<2026-11-18 is:public fork:false archived:false (300 of 31110 matches sampled)
- audio: bounded or incomplete query: topic:music-generation created:>=2025-01-01 created:<2026-01-01 is:public fork:false archived:false (300 of 1461 matches sampled)
- audio: bounded or incomplete query: topic:music-generation created:>=2026-01-01 created:<2026-07-01 is:public fork:false archived:false (300 of 1461 matches sampled)
- audio: bounded or incomplete query: topic:music-generation created:>=2026-07-01 created:<2026-11-18 is:public fork:false archived:false (300 of 1461 matches sampled)
- avatars: bounded or incomplete query: AI avatar created:>=2025-01-01 created:<2026-01-01 is:public fork:false archived:false (300 of 6535 matches sampled)
- avatars: bounded or incomplete query: AI avatar created:>=2026-01-01 created:<2026-07-01 is:public fork:false archived:false (300 of 6535 matches sampled)
- avatars: bounded or incomplete query: AI avatar created:>=2026-07-01 created:<2026-11-18 is:public fork:false archived:false (300 of 6535 matches sampled)
- avatars: bounded or incomplete query: lip sync created:>=2025-01-01 created:<2026-01-01 is:public fork:false archived:false (300 of 2794 matches sampled)
- avatars: bounded or incomplete query: lip sync created:>=2026-01-01 created:<2026-07-01 is:public fork:false archived:false (300 of 2794 matches sampled)
- avatars: bounded or incomplete query: lip sync created:>=2026-07-01 created:<2026-11-18 is:public fork:false archived:false (300 of 2794 matches sampled)
- capture: bounded or incomplete query: neural reconstruction created:>=2025-01-01 created:<2026-01-01 is:public fork:false archived:false (500 of 1391 matches sampled)
- capture: bounded or incomplete query: neural reconstruction created:>=2026-01-01 created:<2026-07-01 is:public fork:false archived:false (500 of 1391 matches sampled)
- capture: bounded or incomplete query: neural reconstruction created:>=2026-07-01 created:<2026-11-18 is:public fork:false archived:false (500 of 1391 matches sampled)
- capture: bounded or incomplete query: topic:gaussian-splatting created:>=2025-01-01 created:<2026-01-01 is:public fork:false archived:false (500 of 1186 matches sampled)
- capture: bounded or incomplete query: topic:gaussian-splatting created:>=2026-01-01 created:<2026-07-01 is:public fork:false archived:false (500 of 1186 matches sampled)
- capture: bounded or incomplete query: topic:gaussian-splatting created:>=2026-07-01 created:<2026-11-18 is:public fork:false archived:false (500 of 1186 matches sampled)
- cel-animation: bounded or incomplete query: animation colorization created:>=2025-01-01 created:<2026-01-01 is:public fork:false archived:false (300 of 2548 matches sampled)
- cel-animation: bounded or incomplete query: animation colorization created:>=2026-01-01 created:<2026-07-01 is:public fork:false archived:false (300 of 2548 matches sampled)
- cel-animation: bounded or incomplete query: animation colorization created:>=2026-07-01 created:<2026-11-18 is:public fork:false archived:false (300 of 2548 matches sampled)
- computational: bounded or incomplete query: AI creative coding created:>=2025-01-01 created:<2026-01-01 is:public fork:false archived:false (300 of 1056 matches sampled)
- computational: bounded or incomplete query: AI creative coding created:>=2026-01-01 created:<2026-07-01 is:public fork:false archived:false (300 of 1056 matches sampled)
- computational: bounded or incomplete query: AI creative coding created:>=2026-07-01 created:<2026-11-18 is:public fork:false archived:false (300 of 1056 matches sampled)
- computational: bounded or incomplete query: topic:generative-art created:>=2025-01-01 created:<2026-01-01 is:public fork:false archived:false (300 of 4892 matches sampled)
- computational: bounded or incomplete query: topic:generative-art created:>=2026-01-01 created:<2026-07-01 is:public fork:false archived:false (300 of 4892 matches sampled)
- computational: bounded or incomplete query: topic:generative-art created:>=2026-07-01 created:<2026-11-18 is:public fork:false archived:false (300 of 4892 matches sampled)
- editing: bounded or incomplete query: AI subtitle created:>=2025-01-01 created:<2026-01-01 is:public fork:false archived:false (300 of 2570 matches sampled)
- editing: bounded or incomplete query: AI subtitle created:>=2026-01-01 created:<2026-07-01 is:public fork:false archived:false (300 of 2570 matches sampled)
- editing: bounded or incomplete query: AI subtitle created:>=2026-07-01 created:<2026-11-18 is:public fork:false archived:false (300 of 2570 matches sampled)
- editing: bounded or incomplete query: AI video editing created:>=2025-01-01 created:<2026-01-01 is:public fork:false archived:false (300 of 4684 matches sampled)
- editing: bounded or incomplete query: AI video editing created:>=2026-01-01 created:<2026-07-01 is:public fork:false archived:false (300 of 4684 matches sampled)
- editing: bounded or incomplete query: AI video editing created:>=2026-07-01 created:<2026-11-18 is:public fork:false archived:false (300 of 4684 matches sampled)
- editing: bounded or incomplete query: AI video editing language:Python created:>=2025-01-01 created:<2026-01-01 is:public fork:false archived:false (300 of 1334 matches sampled)
- editing: bounded or incomplete query: AI video editing language:Python created:>=2026-01-01 created:<2026-07-01 is:public fork:false archived:false (300 of 1334 matches sampled)
- editing: bounded or incomplete query: AI video editing language:Python created:>=2026-07-01 created:<2026-11-18 is:public fork:false archived:false (300 of 1334 matches sampled)
- education: bounded or incomplete query: AI explainer created:>=2025-01-01 created:<2026-01-01 is:public fork:false archived:false (300 of 43585 matches sampled)
- education: bounded or incomplete query: AI explainer created:>=2026-01-01 created:<2026-07-01 is:public fork:false archived:false (300 of 43585 matches sampled)
- education: bounded or incomplete query: AI explainer created:>=2026-07-01 created:<2026-11-18 is:public fork:false archived:false (300 of 43585 matches sampled)
- fabrication: bounded or incomplete query: AI CAD created:>=2025-01-01 created:<2026-01-01 is:public fork:false archived:false (300 of 3833 matches sampled)
- fabrication: bounded or incomplete query: AI CAD created:>=2026-01-01 created:<2026-07-01 is:public fork:false archived:false (300 of 3833 matches sampled)
- fabrication: bounded or incomplete query: AI CAD created:>=2026-07-01 created:<2026-11-18 is:public fork:false archived:false (300 of 3833 matches sampled)
- fabrication: bounded or incomplete query: AI CAD language:Python created:>=2025-01-01 created:<2026-01-01 is:public fork:false archived:false (300 of 1377 matches sampled)
- fabrication: bounded or incomplete query: AI CAD language:Python created:>=2026-01-01 created:<2026-07-01 is:public fork:false archived:false (300 of 1377 matches sampled)
- fabrication: bounded or incomplete query: AI CAD language:Python created:>=2026-07-01 created:<2026-11-18 is:public fork:false archived:false (300 of 1377 matches sampled)
- frontier: bounded or incomplete query: AI creative tools created:>=2025-01-01 created:<2026-01-01 is:public fork:false archived:false (300 of 2186 matches sampled)
- frontier: bounded or incomplete query: AI creative tools created:>=2026-01-01 created:<2026-07-01 is:public fork:false archived:false (300 of 2186 matches sampled)
- frontier: bounded or incomplete query: AI creative tools created:>=2026-07-01 created:<2026-11-18 is:public fork:false archived:false (300 of 2186 matches sampled)
- frontier: bounded or incomplete query: AI multimedia created:>=2025-01-01 created:<2026-01-01 is:public fork:false archived:false (300 of 1242 matches sampled)
- frontier: bounded or incomplete query: AI multimedia created:>=2026-01-01 created:<2026-07-01 is:public fork:false archived:false (300 of 1242 matches sampled)
- frontier: bounded or incomplete query: AI multimedia created:>=2026-07-01 created:<2026-11-18 is:public fork:false archived:false (300 of 1242 matches sampled)
- gaming: bounded or incomplete query: AI blender created:>=2025-01-01 created:<2026-01-01 is:public fork:false archived:false (300 of 2224 matches sampled)
- gaming: bounded or incomplete query: AI blender created:>=2026-01-01 created:<2026-07-01 is:public fork:false archived:false (300 of 2224 matches sampled)
- gaming: bounded or incomplete query: AI blender created:>=2026-07-01 created:<2026-11-18 is:public fork:false archived:false (300 of 2224 matches sampled)
- images: bounded or incomplete query: AI image generation created:>=2025-01-01 created:<2026-01-01 is:public fork:false archived:false (300 of 16542 matches sampled)
- images: bounded or incomplete query: AI image generation created:>=2026-01-01 created:<2026-07-01 is:public fork:false archived:false (300 of 16542 matches sampled)
- images: bounded or incomplete query: AI image generation created:>=2026-07-01 created:<2026-11-18 is:public fork:false archived:false (300 of 16543 matches sampled)
- images: bounded or incomplete query: AI image generation language:TypeScript created:>=2025-01-01 created:<2026-01-01 is:public fork:false archived:false (300 of 2637 matches sampled)
- images: bounded or incomplete query: AI image generation language:TypeScript created:>=2026-01-01 created:<2026-07-01 is:public fork:false archived:false (300 of 2637 matches sampled)
- images: bounded or incomplete query: AI image generation language:TypeScript created:>=2026-07-01 created:<2026-11-18 is:public fork:false archived:false (300 of 2637 matches sampled)
- images: bounded or incomplete query: topic:diffusion created:>=2025-01-01 created:<2026-01-01 is:public fork:false archived:false (300 of 1541 matches sampled)
- images: bounded or incomplete query: topic:diffusion created:>=2026-01-01 created:<2026-07-01 is:public fork:false archived:false (300 of 1541 matches sampled)
- images: bounded or incomplete query: topic:diffusion created:>=2026-07-01 created:<2026-11-18 is:public fork:false archived:false (300 of 1541 matches sampled)
- motion: bounded or incomplete query: motion generation created:>=2025-01-01 created:<2026-01-01 is:public fork:false archived:false (300 of 1680 matches sampled)
- motion: bounded or incomplete query: motion generation created:>=2026-01-01 created:<2026-07-01 is:public fork:false archived:false (300 of 1680 matches sampled)
- motion: bounded or incomplete query: motion generation created:>=2026-07-01 created:<2026-11-18 is:public fork:false archived:false (300 of 1680 matches sampled)
- photography: bounded or incomplete query: AI colorization created:>=2025-01-01 created:<2026-01-01 is:public fork:false archived:false (300 of 5163 matches sampled)
- photography: bounded or incomplete query: AI colorization created:>=2026-01-01 created:<2026-07-01 is:public fork:false archived:false (300 of 5163 matches sampled)
- photography: bounded or incomplete query: AI colorization created:>=2026-07-01 created:<2026-11-18 is:public fork:false archived:false (300 of 5163 matches sampled)
- procedural-materials: bounded or incomplete query: neural material created:>=2025-01-01 created:<2026-01-01 is:public fork:false archived:false (300 of 1419 matches sampled)
- procedural-materials: bounded or incomplete query: neural material created:>=2026-01-01 created:<2026-07-01 is:public fork:false archived:false (300 of 1419 matches sampled)
- procedural-materials: bounded or incomplete query: neural material created:>=2026-07-01 created:<2026-11-18 is:public fork:false archived:false (300 of 1419 matches sampled)
- publishing: bounded or incomplete query: AI presentation created:>=2025-01-01 created:<2026-01-01 is:public fork:false archived:false (300 of 9396 matches sampled)
- publishing: bounded or incomplete query: AI presentation created:>=2026-01-01 created:<2026-07-01 is:public fork:false archived:false (300 of 9396 matches sampled)
- publishing: bounded or incomplete query: AI presentation created:>=2026-07-01 created:<2026-11-18 is:public fork:false archived:false (300 of 9396 matches sampled)
- publishing: bounded or incomplete query: AI publishing created:>=2025-01-01 created:<2026-01-01 is:public fork:false archived:false (300 of 4720 matches sampled)
- publishing: bounded or incomplete query: AI publishing created:>=2026-01-01 created:<2026-07-01 is:public fork:false archived:false (300 of 4720 matches sampled)
- publishing: bounded or incomplete query: AI publishing created:>=2026-07-01 created:<2026-11-18 is:public fork:false archived:false (300 of 4720 matches sampled)
- storytelling: bounded or incomplete query: AI comic created:>=2025-01-01 created:<2026-01-01 is:public fork:false archived:false (300 of 3282 matches sampled)
- storytelling: bounded or incomplete query: AI comic created:>=2026-01-01 created:<2026-07-01 is:public fork:false archived:false (300 of 3282 matches sampled)
- storytelling: bounded or incomplete query: AI comic created:>=2026-07-01 created:<2026-11-18 is:public fork:false archived:false (300 of 3282 matches sampled)
- storytelling: bounded or incomplete query: AI storyboard created:>=2025-01-01 created:<2026-01-01 is:public fork:false archived:false (300 of 2203 matches sampled)
- storytelling: bounded or incomplete query: AI storyboard created:>=2026-01-01 created:<2026-07-01 is:public fork:false archived:false (300 of 2203 matches sampled)
- storytelling: bounded or incomplete query: AI storyboard created:>=2026-07-01 created:<2026-11-18 is:public fork:false archived:false (300 of 2203 matches sampled)
- underwater-media: bounded or incomplete query: underwater image enhancement created:>=2025-01-01 created:<2026-01-01 is:public fork:false archived:false (300 of 1103 matches sampled)
- underwater-media: bounded or incomplete query: underwater image enhancement created:>=2026-01-01 created:<2026-07-01 is:public fork:false archived:false (300 of 1103 matches sampled)
- underwater-media: bounded or incomplete query: underwater image enhancement created:>=2026-07-01 created:<2026-11-18 is:public fork:false archived:false (300 of 1103 matches sampled)
- vector: bounded or incomplete query: AI SVG created:>=2025-01-01 created:<2026-01-01 is:public fork:false archived:false (300 of 2355 matches sampled)
- vector: bounded or incomplete query: AI SVG created:>=2026-01-01 created:<2026-07-01 is:public fork:false archived:false (300 of 2355 matches sampled)
- vector: bounded or incomplete query: AI SVG created:>=2026-07-01 created:<2026-11-18 is:public fork:false archived:false (300 of 2355 matches sampled)
- video: bounded or incomplete query: AI video created:>=2025-01-01 created:<2026-01-01 is:public fork:false archived:false (300 of 99387 matches sampled)
- video: bounded or incomplete query: AI video created:>=2026-01-01 created:<2026-07-01 is:public fork:false archived:false (300 of 99387 matches sampled)
- video: bounded or incomplete query: AI video created:>=2026-07-01 created:<2026-11-18 is:public fork:false archived:false (300 of 99387 matches sampled)
- video: bounded or incomplete query: topic:video-generation created:>=2025-01-01 created:<2026-01-01 is:public fork:false archived:false (300 of 5650 matches sampled)
- video: bounded or incomplete query: topic:video-generation created:>=2026-01-01 created:<2026-07-01 is:public fork:false archived:false (300 of 5650 matches sampled)
- video: bounded or incomplete query: topic:video-generation created:>=2026-07-01 created:<2026-11-18 is:public fork:false archived:false (300 of 5650 matches sampled)
- visualization: bounded or incomplete query: AI data art created:>=2025-01-01 created:<2026-01-01 is:public fork:false archived:false (300 of 1081 matches sampled)
- visualization: bounded or incomplete query: AI data art created:>=2026-01-01 created:<2026-07-01 is:public fork:false archived:false (300 of 1081 matches sampled)
- visualization: bounded or incomplete query: AI data art created:>=2026-07-01 created:<2026-11-18 is:public fork:false archived:false (300 of 1081 matches sampled)
- visualization: bounded or incomplete query: AI visualization created:>=2025-01-01 created:<2026-01-01 is:public fork:false archived:false (300 of 40312 matches sampled)
- visualization: bounded or incomplete query: AI visualization created:>=2026-01-01 created:<2026-07-01 is:public fork:false archived:false (300 of 40312 matches sampled)
- visualization: bounded or incomplete query: AI visualization created:>=2026-07-01 created:<2026-11-18 is:public fork:false archived:false (300 of 40312 matches sampled)
- web: bounded or incomplete query: topic:webgpu created:>=2025-01-01 created:<2026-01-01 is:public fork:false archived:false (300 of 3919 matches sampled)
- web: bounded or incomplete query: topic:webgpu created:>=2026-01-01 created:<2026-07-01 is:public fork:false archived:false (300 of 3919 matches sampled)
- web: bounded or incomplete query: topic:webgpu created:>=2026-07-01 created:<2026-11-18 is:public fork:false archived:false (300 of 3919 matches sampled)
- xr: bounded or incomplete query: AI VR created:>=2025-01-01 created:<2026-01-01 is:public fork:false archived:false (299 of 3159 matches sampled)
- xr: bounded or incomplete query: AI VR created:>=2026-01-01 created:<2026-07-01 is:public fork:false archived:false (299 of 3159 matches sampled)
- xr: bounded or incomplete query: AI VR created:>=2026-07-01 created:<2026-11-18 is:public fork:false archived:false (299 of 3159 matches sampled)
- xr: bounded or incomplete query: AI WebXR created:>=2025-01-01 created:<2026-01-01 is:public fork:false archived:false (99 of 203 matches sampled)
- xr: bounded or incomplete query: AI WebXR created:>=2026-01-01 created:<2026-07-01 is:public fork:false archived:false (99 of 203 matches sampled)
- xr: bounded or incomplete query: AI WebXR created:>=2026-07-01 created:<2026-11-18 is:public fork:false archived:false (99 of 203 matches sampled)
- xr: bounded or incomplete query: AI WebXR editor created:>=2025-01-01 created:<2026-01-01 is:public fork:false archived:false (4 of 5 matches sampled)
- xr: bounded or incomplete query: AI WebXR editor created:>=2026-01-01 created:<2026-07-01 is:public fork:false archived:false (4 of 5 matches sampled)
- xr: bounded or incomplete query: AI WebXR editor created:>=2026-07-01 created:<2026-11-18 is:public fork:false archived:false (4 of 5 matches sampled)
- Source evidence coverage. 4 source checks failed (HTTP 409).
- Tracked repository coverage. 64 source checks failed (HTTP 404).
- Tracked repository coverage. 134 reused results from earlier failed lookups (HTTP 404).

## AID Studio

Storyboarding, narrative & comics · Video, animation & film · AI agents for code-authored media production

This completes an earlier pending guide with a current source review.

### Quality assessment: Quality unverified

Creative use and the code grant are documented. Check-level gaps remain before a recommendation.

Scope: Prepare one scene with approved reference images, a shot list and editable model-generated draft panels before committing to an animation render.

Evidence checked: 2026-11-21. No local execution implied.

- **Open-source software license · verified:** Reviewed the complete project software grant and its redistribution conditions. Model, data and service terms are scoped separately. [Source](https://github.com/shijue-aid/aid-studio/blob/main/LICENSE)
- **Creative results · documented:** The bilingual source documents a first motion-comic project and specifies the deployment requirements. Shot continuity and resulting animation need their own output review. [Source](https://github.com/shijue-aid/aid-studio/blob/main/README.md) [Source](https://github.com/shijue-aid/aid-studio/blob/main/README.en.md) [Source](https://github.com/shijue-aid/aid-studio/blob/main/deploy/README.md)
- **Reproducible setup · documented:** The installation and first-use steps are in the cited documentation. Reproduction of this workflow remains unverified. [Source](https://github.com/shijue-aid/aid-studio/blob/main/README.md) [Source](https://github.com/shijue-aid/aid-studio/blob/main/README.en.md) [Source](https://github.com/shijue-aid/aid-studio/blob/main/deploy/README.md)
- **Maintenance and support · documented:** v2.2.4 is a published release. The deployment notes distinguish upgrade and rollback paths. [Source](https://github.com/shijue-aid/aid-studio/releases/tag/v2.2.4)
- **Independent use · unknown:** Independent first-hand use of the exact workflow was not established in this source review.
- **Models, services and costs · documented:** The project code is MIT. NOTICE identifies third-party components and an adapted RuoYi-Vue admin component. Backend models, generated works and user materials require independent review. Self-host compute/storage apply. Remote model, image and voice endpoints may charge for use. [Source](https://github.com/shijue-aid/aid-studio/blob/main/README.md) [Source](https://github.com/shijue-aid/aid-studio/blob/main/README.en.md) [Source](https://github.com/shijue-aid/aid-studio/blob/main/deploy/README.md)

Source and documentation review. No hands-on execution by AI Media Scout. Current release and source branch options differ. Keep backups before upgrading and verify a representative source-to-draft flow before a large project.

### How it uses AI

The self-hosted project orchestrates model-assisted scripts, character references, storyboards, images, video and voices for motion comics and short-drama preproduction. [Source](https://github.com/shijue-aid/aid-studio/blob/main/README.md) [Source](https://github.com/shijue-aid/aid-studio/blob/main/README.en.md) [Source](https://github.com/shijue-aid/aid-studio/blob/main/deploy/README.md)

### Introduction

The self-hosted project orchestrates model-assisted scripts, character references, storyboards, images, video and voices for motion comics and short-drama preproduction. [Source 1](https://github.com/shijue-aid/aid-studio/blob/main/README.md) [Source 2](https://github.com/shijue-aid/aid-studio/blob/main/README.en.md) [Source 3](https://github.com/shijue-aid/aid-studio/blob/main/deploy/README.md)

### What it is good for

Prepare one scene with approved reference images, a shot list and editable model-generated draft panels before committing to an animation render. [Source 1](https://github.com/shijue-aid/aid-studio/blob/main/README.md) [Source 2](https://github.com/shijue-aid/aid-studio/blob/main/README.en.md) [Source 3](https://github.com/shijue-aid/aid-studio/blob/main/deploy/README.md)

### Demo & examples

The bilingual source documents a first motion-comic project and specifies the deployment requirements. Shot continuity and resulting animation need their own output review. [Source 1](https://github.com/shijue-aid/aid-studio/blob/main/README.md) [Source 2](https://github.com/shijue-aid/aid-studio/blob/main/README.en.md) [Source 3](https://github.com/shijue-aid/aid-studio/blob/main/deploy/README.md)

### Install

Follow the documented route for the scoped workflow. The steps below are source references. [Source 1](https://github.com/shijue-aid/aid-studio/blob/main/README.md) [Source 2](https://github.com/shijue-aid/aid-studio/blob/main/README.en.md) [Source 3](https://github.com/shijue-aid/aid-studio/blob/main/deploy/README.md)

1. Set up the documented 64-bit Linux host and choose Docker Compose or the relevant source path. Review the official deployment configuration before initialization.
2. Start required services and configure only the selected supported model endpoints. Verify available capacity before accepting generation jobs.
### First project

A small first project makes the input, model output and handoff easy to inspect. [Source 1](https://github.com/shijue-aid/aid-studio/blob/main/README.md) [Source 2](https://github.com/shijue-aid/aid-studio/blob/main/README.en.md) [Source 3](https://github.com/shijue-aid/aid-studio/blob/main/deploy/README.md)

1. Create one motion-comic scene with authorized character assets. Draft a few shots and refine the scene prompts and sequence.
2. Generate small preview assets through the selected models, inspect consistency and keep the scene files. Review any audio/voice rights before generating lines.
3. Export or review the scene using the workflow’s supported output. Keep the storyboard, generated assets and provider settings separate.
### Hardware & software

Platform and compute constraints refer to the selected route. [Source 1](https://github.com/shijue-aid/aid-studio/blob/main/README.md) [Source 2](https://github.com/shijue-aid/aid-studio/blob/main/README.en.md) [Source 3](https://github.com/shijue-aid/aid-studio/blob/main/deploy/README.md)

- **Hardware:** The official deployment guide gives a scoped minimum of 2 cores, 4 GB RAM and 40 GB storage on one host with RocketMQ disabled. Model inference needs separate capacity.
- **Software:** 64-bit Linux server and documented deployment services. Docker Compose is the recommended container route. Connected models require compatible endpoints, credentials and their own terms.
- **Platforms:** Linux server deployment is documented. Review the client’s browser requirements separately. A native Windows/macOS server path was not verified.

### License, model weights & costs

The full software license was reviewed. Dependencies and creative assets carry their own terms. [Source 1](https://github.com/shijue-aid/aid-studio/blob/main/LICENSE) [Source 2](https://github.com/shijue-aid/aid-studio/blob/main/README.md) [Source 3](https://github.com/shijue-aid/aid-studio/blob/main/README.en.md) [Source 4](https://github.com/shijue-aid/aid-studio/blob/main/deploy/README.md)

- **Code:** MIT
- **Weights:** The project code is MIT. NOTICE identifies third-party components and an adapted RuoYi-Vue admin component. Backend models, generated works and user materials require independent review.
- **Commercial:** Project code is governed by MIT. Confirm selected model, source-media and output restrictions separately.
- **Cost:** Self-host compute/storage apply. Remote model, image and voice endpoints may charge for use.

### Why it merits attention

The creative workflow is grounded in the cited documentation. Output quality and compatibility are not hands-on verified. [Source 1](https://github.com/shijue-aid/aid-studio/blob/main/README.md) [Source 2](https://github.com/shijue-aid/aid-studio/blob/main/README.en.md) [Source 3](https://github.com/shijue-aid/aid-studio/blob/main/deploy/README.md)

### Limitations

Current release and source branch options differ. Keep backups before upgrading and verify a representative source-to-draft flow before a large project. [Source 1](https://github.com/shijue-aid/aid-studio/blob/main/README.md) [Source 2](https://github.com/shijue-aid/aid-studio/blob/main/README.en.md) [Source 3](https://github.com/shijue-aid/aid-studio/blob/main/deploy/README.md)

### Get the tool

- [Repository](https://github.com/shijue-aid/aid-studio)
- [Documentation](https://github.com/shijue-aid/aid-studio/blob/main/deploy/README.md)

## AnyAudio

Audio, music & voice · AI Foley and sound effects · AI agents for code-authored media production

The source repository was created on 2026-10-28. This is its first complete guide in the library.

### Quality assessment: Quality unverified

Creative use and the code grant are documented. Check-level gaps remain before a recommendation.

Scope: Build a small multitrack sound design sketch for a short clip, with voice, ambience, cues and a separate musical bed.

Evidence checked: 2026-11-21. No local execution implied.

- **Open-source software license · verified:** Reviewed the complete project software grant and its redistribution conditions. Model, data and service terms are scoped separately. [Source](https://github.com/cloudoyx/any-audio/blob/main/LICENSE)
- **Creative results · documented:** The project publishes an arranged bossa nova example and a short narrative sound scene. They show the intended editable tracks and export, without establishing reproducibility for every engine. [Source](https://github.com/cloudoyx/any-audio/blob/main/README.md)
- **Reproducible setup · documented:** The installation and first-use steps are in the cited documentation. Reproduction of this workflow remains unverified. [Source](https://github.com/cloudoyx/any-audio/blob/main/README.md)
- **Maintenance and support · documented:** v0.4.2 source and published version were reviewed. Compatibility with an exact host version and engine still needs independent assessment. [Source](https://github.com/cloudoyx/any-audio/releases/tag/v0.4.2)
- **Independent use · unknown:** Independent first-hand use of the exact workflow was not established in this source review.
- **Models, services and costs · documented:** MIT covers the toolkit. Its source notes identify a separate GeneralUser GS bank license and other sample or speech engines. Verify actual selected media and model rights. Local sampled rendering uses compute. Online voice calls still need service availability even when no key is documented. Optional accelerator and model downloads add storage. [Source](https://github.com/cloudoyx/any-audio/blob/main/README.md)

Source and documentation review. No hands-on execution by AI Media Scout. Packaged code does not include all sound assets. Check model use, sample terms and the generated arrangement independently before release.

### How it uses AI

A connected agent uses AnyAudio’s sound production tools to write an editable arrangement, select instrument samples and sound effects, and optionally fill narration from a speech engine. [Source](https://github.com/cloudoyx/any-audio/blob/main/README.md)

### Introduction

A connected agent uses AnyAudio’s sound production tools to write an editable arrangement, select instrument samples and sound effects, and optionally fill narration from a speech engine. [Source 1](https://github.com/cloudoyx/any-audio/blob/main/README.md)

### What it is good for

Build a small multitrack sound design sketch for a short clip, with voice, ambience, cues and a separate musical bed. [Source 1](https://github.com/cloudoyx/any-audio/blob/main/README.md)

### Demo & examples

The project publishes an arranged bossa nova example and a short narrative sound scene. They show the intended editable tracks and export, without establishing reproducibility for every engine. [Source 1](https://github.com/cloudoyx/any-audio/blob/main/README.md)

### Install

Follow the documented route for the scoped workflow. The steps below are source references. [Source 1](https://github.com/cloudoyx/any-audio/blob/main/README.md)

1. Use the documented DeepSeek Harness profile and Node version. Install and enable the plugin in that profile, then restart the host.
2. Choose a licensed SoundFont or sound library and configure the intended narration route only when needed.
### First project

A small first project makes the input, model output and handoff easy to inspect. [Source 1](https://github.com/cloudoyx/any-audio/blob/main/README.md)

1. Ask for one scene with a few cues on separate tracks. Inspect instrument bank selection, voice engine and timing.
2. Adjust the timeline and listen for clipping and continuity before muxing or exporting. Keep a record of each sample and its license.
### Hardware & software

Platform and compute constraints refer to the selected route. [Source 1](https://github.com/cloudoyx/any-audio/blob/main/README.md)

- **Hardware:** Requirement depends on chosen bank or optional speech models. Example general instrument bank is 32 MB. Minimum system RAM and VRAM are undocumented.
- **Software:** Node 22.19+ in the 22.x series or 24+, documented DSH plugin environment. FFmpeg is required for the described speech and mux paths.
- **Platforms:** The host and executable dependencies determine OS coverage. An all-platform production matrix is unverified.

### License, model weights & costs

The full software license was reviewed. Dependencies and creative assets carry their own terms. [Source 1](https://github.com/cloudoyx/any-audio/blob/main/LICENSE) [Source 2](https://github.com/cloudoyx/any-audio/blob/main/README.md)

- **Code:** MIT
- **Weights:** MIT covers the toolkit. Its source notes identify a separate GeneralUser GS bank license and other sample or speech engines. Verify actual selected media and model rights.
- **Commercial:** Project code is governed by MIT. Confirm selected model, source-media and output restrictions separately.
- **Cost:** Local sampled rendering uses compute. Online voice calls still need service availability even when no key is documented. Optional accelerator and model downloads add storage.

### Why it merits attention

The creative workflow is grounded in the cited documentation. Output quality and compatibility are not hands-on verified. [Source 1](https://github.com/cloudoyx/any-audio/blob/main/README.md)

### Limitations

Packaged code does not include all sound assets. Check model use, sample terms and the generated arrangement independently before release. [Source 1](https://github.com/cloudoyx/any-audio/blob/main/README.md)

### Get the tool

- [Repository](https://github.com/cloudoyx/any-audio)
- [Documentation](https://github.com/cloudoyx/any-audio/blob/main/README.md)

## Cutroom

Editing, captions & post-production · Video, animation & film · AI agents for code-authored media production

First complete guide in the library. The publication and documentation dates are not necessarily the project’s launch date.

### Quality assessment: Quality unverified

Creative use and the code grant are documented. Check-level gaps remain before a recommendation.

Scope: Re-cut a product walkthrough when its UI changes, preserving recorded events, caption marks and the editable storyboard.

Evidence checked: 2026-11-21. No local execution implied.

- **Open-source software license · verified:** Reviewed the complete project software grant and its redistribution conditions. Model, data and service terms are scoped separately. [Source](https://github.com/WEBGRS/cutroom/blob/main/LICENSE)
- **Creative results · documented:** The README shows the agent applying a visible annotation in the preview and describes built-in voice examples. Rerecording and render parity need testing against the actual product UI. [Source](https://github.com/WEBGRS/cutroom/blob/main/README.md)
- **Reproducible setup · documented:** The installation and first-use steps are in the cited documentation. Reproduction of this workflow remains unverified. [Source](https://github.com/WEBGRS/cutroom/blob/main/README.md)
- **Maintenance and support · documented:** Published v0.4.0 was identified, with source docs for authoring and recording. Repeatability across runtime updates is open. [Source](https://github.com/WEBGRS/cutroom/releases/tag/v0.4.0)
- **Independent use · unknown:** Independent first-hand use of the exact workflow was not established in this source review.
- **Models, services and costs · documented:** MIT covers Cutroom. Rendering uses Remotion under its own terms. Check the applicable plan and company scope, plus license notices for samples, voices and models. Local compute applies. Remotion and connected models or voice services can carry separate charges. [Source](https://github.com/WEBGRS/cutroom/blob/main/README.md)

Source and documentation review. No hands-on execution by AI Media Scout. The exact script and click routes depend on the rendered UI sequence. Confirm results and downstream use terms for the selected host.

### How it uses AI

Cutroom lets an AI assistant and an editor modify the same storyboard JSON and timeline. Its documented model route can use local speech generation and editable captions for product demonstration videos. [Source](https://github.com/WEBGRS/cutroom/blob/main/README.md)

### Introduction

Cutroom lets an AI assistant and an editor modify the same storyboard JSON and timeline. Its documented model route can use local speech generation and editable captions for product demonstration videos. [Source 1](https://github.com/WEBGRS/cutroom/blob/main/README.md)

### What it is good for

Re-cut a product walkthrough when its UI changes, preserving recorded events, caption marks and the editable storyboard. [Source 1](https://github.com/WEBGRS/cutroom/blob/main/README.md)

### Demo & examples

The README shows the agent applying a visible annotation in the preview and describes built-in voice examples. Rerecording and render parity need testing against the actual product UI. [Source 1](https://github.com/WEBGRS/cutroom/blob/main/README.md)

### Install

Follow the documented route for the scoped workflow. The steps below are source references. [Source 1](https://github.com/WEBGRS/cutroom/blob/main/README.md)

1. Use the documented project release or source setup for your OS. The packaged Windows CLI lives beside the desktop executable.
2. Configure the appropriate assistant and required rendering dependency. The editor can work manually as well.
### First project

A small first project makes the input, model output and handoff easy to inspect. [Source 1](https://github.com/WEBGRS/cutroom/blob/main/README.md)

1. Import a short recording and add a script mark around one click. Use the assistant to make one visible change.
2. Inspect and revise the same storyboard in the timeline. Generate an optional local voice track only after checking model terms.
3. Render a proof and compare caption and audio alignment after a small rerecording.
### Hardware & software

Platform and compute constraints refer to the selected route. [Source 1](https://github.com/WEBGRS/cutroom/blob/main/README.md)

- **Hardware:** The bundled speech workflow documents an approximately 147 MB model download. Total system requirements and acceleration minima remain undocumented.
- **Software:** Cutroom and its Remotion rendering route. The optional connected agent and selected voice model need their own setup.
- **Platforms:** The README describes Windows desktop/CLI use. Cross-platform source, browser and renderer support need an exact setup check.

### License, model weights & costs

The full software license was reviewed. Dependencies and creative assets carry their own terms. [Source 1](https://github.com/WEBGRS/cutroom/blob/main/LICENSE) [Source 2](https://github.com/WEBGRS/cutroom/blob/main/README.md)

- **Code:** MIT
- **Weights:** MIT covers Cutroom. Rendering uses Remotion under its own terms. Check the applicable plan and company scope, plus license notices for samples, voices and models.
- **Commercial:** Project code is governed by MIT. Confirm selected model, source-media and output restrictions separately.
- **Cost:** Local compute applies. Remotion and connected models or voice services can carry separate charges.

### Why it merits attention

The creative workflow is grounded in the cited documentation. Output quality and compatibility are not hands-on verified. [Source 1](https://github.com/WEBGRS/cutroom/blob/main/README.md)

### Limitations

The exact script and click routes depend on the rendered UI sequence. Confirm results and downstream use terms for the selected host. [Source 1](https://github.com/WEBGRS/cutroom/blob/main/README.md)

### Get the tool

- [Repository](https://github.com/WEBGRS/cutroom)
- [Documentation](https://github.com/WEBGRS/cutroom/blob/main/README.md)

## Whisper ONNX Diarization

Audio, music & voice · Editing, captions & post-production · Accessible media & assistive creation

The source repository was created on 2026-11-20. This is its first complete guide in the library.

### Quality assessment: Quality unverified

Creative use and the code grant are documented. Check-level gaps remain before a recommendation.

Scope: Produce a draft interview transcript with separable speaker labels before editorial correction.

Evidence checked: 2026-11-21. No local execution implied.

- **Open-source software license · verified:** Reviewed the complete project software grant and its redistribution conditions. Model, data and service terms are scoped separately. [Source](https://github.com/incubated-geek-cc/whisper-onnx-diarization/blob/main/LICENSE)
- **Creative results · documented:** The project presents a sample interface and names a live demo endpoint. Independent speaker-label accuracy on overlapping audio is unverified. [Source](https://github.com/incubated-geek-cc/whisper-onnx-diarization/blob/main/README.md)
- **Reproducible setup · documented:** The installation and first-use steps are in the cited documentation. Reproduction of this workflow remains unverified. [Source](https://github.com/incubated-geek-cc/whisper-onnx-diarization/blob/main/README.md)
- **Maintenance and support · documented:** The version 1.0.0 release is present. Long-term support and current model regressions remain open. [Source](https://github.com/incubated-geek-cc/whisper-onnx-diarization/releases/tag/v1.0.0)
- **Independent use · unknown:** Independent first-hand use of the exact workflow was not established in this source review.
- **Models, services and costs · documented:** MIT applies to this project. The Whisper and pyannote-derived artifacts and upstream browser components retain separate licenses. After loading model/runtime files, the project documents local inference. Hosting and model acquisition remain relevant. [Source](https://github.com/incubated-geek-cc/whisper-onnx-diarization/blob/main/README.md)

Source and documentation review. No hands-on execution by AI Media Scout. Speaker labels are estimated, particularly when voices overlap. The exact offline package and dependencies should be tested on an intended browser.

### How it uses AI

The browser app runs a Whisper ONNX recognizer with speaker-labeling support. It supplies structured transcript text from a locally processed audio or video file. [Source](https://github.com/incubated-geek-cc/whisper-onnx-diarization/blob/main/README.md)

### Introduction

The browser app runs a Whisper ONNX recognizer with speaker-labeling support. It supplies structured transcript text from a locally processed audio or video file. [Source 1](https://github.com/incubated-geek-cc/whisper-onnx-diarization/blob/main/README.md)

### What it is good for

Produce a draft interview transcript with separable speaker labels before editorial correction. [Source 1](https://github.com/incubated-geek-cc/whisper-onnx-diarization/blob/main/README.md)

### Demo & examples

The project presents a sample interface and names a live demo endpoint. Independent speaker-label accuracy on overlapping audio is unverified. [Source 1](https://github.com/incubated-geek-cc/whisper-onnx-diarization/blob/main/README.md)

### Install

Follow the documented route for the scoped workflow. The steps below are source references. [Source 1](https://github.com/incubated-geek-cc/whisper-onnx-diarization/blob/main/README.md)

1. Use the published browser demo or examine the official release’s self-hosted route. Confirm model assets, ONNX Runtime and FFmpeg are served as documented for offline use.
2. Choose the default or another documented model. Confirm the browser support required for the selected runtime.
### First project

A small first project makes the input, model output and handoff easy to inspect. [Source 1](https://github.com/incubated-geek-cc/whisper-onnx-diarization/blob/main/README.md)

1. Import a short consented recording and check the chosen transcription and speaker models.
2. Compare speech, boundaries and speaker changes against actual playback. Save the draft along with the source file and corrections.
### Hardware & software

Platform and compute constraints refer to the selected route. [Source 1](https://github.com/incubated-geek-cc/whisper-onnx-diarization/blob/main/README.md)

- **Hardware:** Minimum RAM, VRAM and disk space for the scoped workflow are undocumented.
- **Software:** Supported browser with ONNX Runtime and the documented local assets, Whisper checkpoint and diarization component. Video input may use the project’s FFmpeg path.
- **Platforms:** A browser workflow is documented. Support depends on runtime features and build. Native app support was not established.

### License, model weights & costs

The full software license was reviewed. Dependencies and creative assets carry their own terms. [Source 1](https://github.com/incubated-geek-cc/whisper-onnx-diarization/blob/main/LICENSE) [Source 2](https://github.com/incubated-geek-cc/whisper-onnx-diarization/blob/main/README.md)

- **Code:** MIT
- **Weights:** MIT applies to this project. The Whisper and pyannote-derived artifacts and upstream browser components retain separate licenses.
- **Commercial:** Project code is governed by MIT. Confirm selected model, source-media and output restrictions separately.
- **Cost:** After loading model/runtime files, the project documents local inference. Hosting and model acquisition remain relevant.

### Why it merits attention

The creative workflow is grounded in the cited documentation. Output quality and compatibility are not hands-on verified. [Source 1](https://github.com/incubated-geek-cc/whisper-onnx-diarization/blob/main/README.md)

### Limitations

Speaker labels are estimated, particularly when voices overlap. The exact offline package and dependencies should be tested on an intended browser. [Source 1](https://github.com/incubated-geek-cc/whisper-onnx-diarization/blob/main/README.md)

### Get the tool

- [Repository](https://github.com/incubated-geek-cc/whisper-onnx-diarization)
- [Documentation](https://github.com/incubated-geek-cc/whisper-onnx-diarization/blob/main/README.md)

## SRT A-roll for Jianying

Editing, captions & post-production · Video, animation & film · AI agents for code-authored media production

First complete guide in the library. The publication and documentation dates are not necessarily the project’s launch date.

### Quality assessment: Quality unverified

Creative use and the code grant are documented. Check-level gaps remain before a recommendation.

Scope: Use an approved narration with timing to draft graphic callouts for a short explainer, then revise the resulting subtitle and visual timeline.

Evidence checked: 2026-11-21. No local execution implied.

- **Open-source software license · verified:** Reviewed the complete project software grant and its redistribution conditions. Model, data and service terms are scoped separately. [Source](https://github.com/jiemianduan/srt-aroll-jianying/blob/main/LICENSE)
- **Creative results · documented:** The README documents planner density controls and a project import path. It distinguishes model-produced planning from deterministic draft assembly. [Source](https://github.com/jiemianduan/srt-aroll-jianying/blob/main/README.md)
- **Reproducible setup · documented:** The installation and first-use steps are in the cited documentation. Reproduction of this workflow remains unverified. [Source](https://github.com/jiemianduan/srt-aroll-jianying/blob/main/README.md)
- **Maintenance and support · unknown:** The reviewed sources do not establish workflow-specific support, fixes and unresolved blockers.
- **Independent use · unknown:** Independent first-hand use of the exact workflow was not established in this source review.
- **Models, services and costs · documented:** MPL-2.0 covers this repository. Jianying Pro and the selected planner/agent have separate terms. Cue assets, sound effects and fonts need their own licenses. The local assembly route requires the host and selected model access. Provider and host fees vary. [Source](https://github.com/jiemianduan/srt-aroll-jianying/blob/main/README.md)

Source and documentation review. No hands-on execution by AI Media Scout. A generated draft does not guarantee cue accuracy or import parity across host versions. Start with a short reversible edit.

### How it uses AI

The project uses a chosen model to plan callout placement and A-roll overlays from an existing SRT. It converts that plan into an editable Jianying Pro draft for correction. [Source](https://github.com/jiemianduan/srt-aroll-jianying/blob/main/README.md)

### Introduction

The project uses a chosen model to plan callout placement and A-roll overlays from an existing SRT. It converts that plan into an editable Jianying Pro draft for correction. [Source 1](https://github.com/jiemianduan/srt-aroll-jianying/blob/main/README.md)

### What it is good for

Use an approved narration with timing to draft graphic callouts for a short explainer, then revise the resulting subtitle and visual timeline. [Source 1](https://github.com/jiemianduan/srt-aroll-jianying/blob/main/README.md)

### Demo & examples

The README documents planner density controls and a project import path. It distinguishes model-produced planning from deterministic draft assembly. [Source 1](https://github.com/jiemianduan/srt-aroll-jianying/blob/main/README.md)

### Install

Follow the documented route for the scoped workflow. The steps below are source references. [Source 1](https://github.com/jiemianduan/srt-aroll-jianying/blob/main/README.md)

1. Prepare the documented macOS setup and a compatible Jianying Pro installation. Use the project’s bootstrap dependency check before approving changes.
2. Configure the selected AI planner route or the compatible agent client. Model access is separate from generating the editable draft.
### First project

A small first project makes the input, model output and handoff easy to inspect. [Source 1](https://github.com/jiemianduan/srt-aroll-jianying/blob/main/README.md)

1. Load a short, corrected SRT. Choose a density mode and inspect the model’s proposed anchors and callout duration.
2. Adjust overlays and sound cues before building the draft. Open the result in the target Jianying version and verify placement against the original audio.
### Hardware & software

Platform and compute constraints refer to the selected route. [Source 1](https://github.com/jiemianduan/srt-aroll-jianying/blob/main/README.md)

- **Hardware:** Minimum RAM, VRAM and disk space for the scoped workflow are undocumented.
- **Software:** The documented local setup requires compatible Jianying Pro, macOS source dependencies and a selected model provider or agent.
- **Platforms:** macOS is the documented bootstrap path. No native Windows or Linux support was established for the full handoff.

### License, model weights & costs

The full software license was reviewed. Dependencies and creative assets carry their own terms. [Source 1](https://github.com/jiemianduan/srt-aroll-jianying/blob/main/LICENSE) [Source 2](https://github.com/jiemianduan/srt-aroll-jianying/blob/main/README.md)

- **Code:** MPL-2.0
- **Weights:** MPL-2.0 covers this repository. Jianying Pro and the selected planner/agent have separate terms. Cue assets, sound effects and fonts need their own licenses.
- **Commercial:** Project code is governed by MPL-2.0. Confirm selected model, source-media and output restrictions separately.
- **Cost:** The local assembly route requires the host and selected model access. Provider and host fees vary.

### Why it merits attention

The creative workflow is grounded in the cited documentation. Output quality and compatibility are not hands-on verified. [Source 1](https://github.com/jiemianduan/srt-aroll-jianying/blob/main/README.md)

### Limitations

A generated draft does not guarantee cue accuracy or import parity across host versions. Start with a short reversible edit. [Source 1](https://github.com/jiemianduan/srt-aroll-jianying/blob/main/README.md)

### Get the tool

- [Repository](https://github.com/jiemianduan/srt-aroll-jianying)
- [Documentation](https://github.com/jiemianduan/srt-aroll-jianying/blob/main/README.md)

## LAREX

Cultural heritage layout recognition and transcription · Archives, media restoration & collections · Creative publishing & presentation

First complete guide in the library. The publication and documentation dates are not necessarily the project’s launch date.

### Quality assessment: Quality unverified

Creative use and the code grant are documented. Check-level gaps remain before a recommendation.

Scope: Proofread the regions and transcription for a small document corpus, then export structured data that can be reused for a digital edition or ground truth.

Evidence checked: 2026-11-21. No local execution implied.

- **Open-source software license · verified:** Reviewed the complete project software grant and its redistribution conditions. Model, data and service terms are scoped separately. [Source](https://github.com/OCR4all/LAREX/blob/main/LICENSE)
- **Creative results · documented:** The author’s project and Actions documentation describes the correction interface and the submission of default processing jobs. Exact output quality depends on the chosen processor. [Source](https://github.com/OCR4all/LAREX/blob/main/README.md) [Source](https://docs.larex.kallimachos.de/getting-started/installation) [Source](https://docs.larex.kallimachos.de)
- **Reproducible setup · documented:** The installation and first-use steps are in the cited documentation. Reproduction of this workflow remains unverified. [Source](https://github.com/OCR4all/LAREX/blob/main/README.md) [Source](https://docs.larex.kallimachos.de/getting-started/installation) [Source](https://docs.larex.kallimachos.de)
- **Maintenance and support · documented:** The release listing and documented 1.0 migration establish current version activity. Support for a particular Action remains separate. [Source](https://github.com/OCR4all/LAREX/releases/tag/v1.1.0-rc.1)
- **Independent use · unknown:** Independent first-hand use of the exact workflow was not established in this source review.
- **Models, services and costs · documented:** MIT covers the LAREX project. External processors, containers, models, annotations and imported collection media carry distinct terms. Self-host compute, storage and recognition workers apply. External processing is conditional on the chosen Action. [Source](https://github.com/OCR4all/LAREX/blob/main/README.md) [Source](https://docs.larex.kallimachos.de/getting-started/installation) [Source](https://docs.larex.kallimachos.de)

Source and documentation review. No hands-on execution by AI Media Scout. The current 1.0 rewrite and legacy LAREX 0.7 differ. Confirm model, export schema and annotation compatibility on a copy before shifting existing projects.

### How it uses AI

LAREX Actions let documented external recognition and layout processors run against document images, with correction and dataset operations kept in the same collaborative workspace. [Source](https://github.com/OCR4all/LAREX/blob/main/README.md) [Source](https://docs.larex.kallimachos.de/getting-started/installation) [Source](https://docs.larex.kallimachos.de)

### Introduction

LAREX Actions let documented external recognition and layout processors run against document images, with correction and dataset operations kept in the same collaborative workspace. [Source 1](https://github.com/OCR4all/LAREX/blob/main/README.md) [Source 2](https://docs.larex.kallimachos.de/getting-started/installation) [Source 3](https://docs.larex.kallimachos.de)

### What it is good for

Proofread the regions and transcription for a small document corpus, then export structured data that can be reused for a digital edition or ground truth. [Source 1](https://github.com/OCR4all/LAREX/blob/main/README.md) [Source 2](https://docs.larex.kallimachos.de/getting-started/installation) [Source 3](https://docs.larex.kallimachos.de)

### Demo & examples

The author’s project and Actions documentation describes the correction interface and the submission of default processing jobs. Exact output quality depends on the chosen processor. [Source 1](https://github.com/OCR4all/LAREX/blob/main/README.md) [Source 2](https://docs.larex.kallimachos.de/getting-started/installation) [Source 3](https://docs.larex.kallimachos.de)

### Install

Follow the documented route for the scoped workflow. The steps below are source references. [Source 1](https://github.com/OCR4all/LAREX/blob/main/README.md) [Source 2](https://docs.larex.kallimachos.de/getting-started/installation) [Source 3](https://docs.larex.kallimachos.de)

1. Use Docker and Docker Compose v2. Follow the installation wizard or obtain the versioned deployment ZIP from the official release.
2. Configure the documented instance and enable only the Action and external recognition service required for your project.

```sh
docker compose up -d
```

### First project

A small first project makes the input, model output and handoff easy to inspect. [Source 1](https://github.com/OCR4all/LAREX/blob/main/README.md) [Source 2](https://docs.larex.kallimachos.de/getting-started/installation) [Source 3](https://docs.larex.kallimachos.de)

1. Import a short PDF, PAGE XML or openly accessible IIIF document into a small test project.
2. Run a suitable layout or OCR Action and compare the resulting regions and text with the image. Revise errors before exporting PAGE XML or the format required by the downstream edition.
### Hardware & software

Platform and compute constraints refer to the selected route. [Source 1](https://github.com/OCR4all/LAREX/blob/main/README.md) [Source 2](https://docs.larex.kallimachos.de/getting-started/installation) [Source 3](https://docs.larex.kallimachos.de)

- **Hardware:** Minimum RAM, VRAM and disk space for the scoped workflow are undocumented.
- **Software:** Docker Compose v2 and the LAREX bundle. The selected external model processor and Docker image must also be available.
- **Platforms:** Browser-based editing with a Docker-hosted service. The installation docs establish the container path. Other native-server combinations are unverified.

### License, model weights & costs

The full software license was reviewed. Dependencies and creative assets carry their own terms. [Source 1](https://github.com/OCR4all/LAREX/blob/main/LICENSE) [Source 2](https://github.com/OCR4all/LAREX/blob/main/README.md) [Source 3](https://docs.larex.kallimachos.de/getting-started/installation) [Source 4](https://docs.larex.kallimachos.de)

- **Code:** MIT
- **Weights:** MIT covers the LAREX project. External processors, containers, models, annotations and imported collection media carry distinct terms.
- **Commercial:** Project code is governed by MIT. Confirm selected model, source-media and output restrictions separately.
- **Cost:** Self-host compute, storage and recognition workers apply. External processing is conditional on the chosen Action.

### Why it merits attention

The creative workflow is grounded in the cited documentation. Output quality and compatibility are not hands-on verified. [Source 1](https://github.com/OCR4all/LAREX/blob/main/README.md) [Source 2](https://docs.larex.kallimachos.de/getting-started/installation) [Source 3](https://docs.larex.kallimachos.de)

### Limitations

The current 1.0 rewrite and legacy LAREX 0.7 differ. Confirm model, export schema and annotation compatibility on a copy before shifting existing projects. [Source 1](https://github.com/OCR4all/LAREX/blob/main/README.md) [Source 2](https://docs.larex.kallimachos.de/getting-started/installation) [Source 3](https://docs.larex.kallimachos.de)

### Get the tool

- [Repository](https://github.com/OCR4all/LAREX)
- [Documentation](https://docs.larex.kallimachos.de)

## OM-DYCI2

AI music notation and score recovery · Audio, music & voice · Performance, projection & stage media

First complete guide in the library. The publication and documentation dates are not necessarily the project’s launch date.

### Quality assessment: Quality unverified

Creative use and the code grant are documented. Check-level gaps remain before a recommendation.

Scope: Compose a controlled run of musical phrases from a small corpus, keeping the scenario and resulting sequence editable in an OM patch.

Evidence checked: 2026-11-21. No local execution implied.

- **Open-source software license · verified:** Reviewed the complete project software grant and its redistribution conditions. Model, data and service terms are scoped separately. [Source](https://github.com/DYCI2/om-dyci2/blob/master/LICENSE)
- **Creative results · documented:** The maintained source includes tutorial patches. The IRCAM report describes an applied structured composition process using the model and OM environment. [Source](https://github.com/DYCI2/om-dyci2/blob/master/README.md) [Source](https://aimc2021.iem.at/wp-content/uploads/2021/06/AIMC_2021_Nika_Bresson.pdf) [Source](https://github.com/cac-t-u-s/om-sharp)
- **Reproducible setup · documented:** The installation and first-use steps are in the cited documentation. Reproduction of this workflow remains unverified. [Source](https://github.com/DYCI2/om-dyci2/blob/master/README.md) [Source](https://aimc2021.iem.at/wp-content/uploads/2021/06/AIMC_2021_Nika_Bresson.pdf) [Source](https://github.com/cac-t-u-s/om-sharp)
- **Maintenance and support · unknown:** The reviewed sources do not establish workflow-specific support, fixes and unresolved blockers.
- **Independent use · unknown:** Independent first-hand use of the exact workflow was not established in this source review.
- **Models, services and costs · documented:** The full GPLv3 software grant was reviewed. The host environment, Python dependencies and imported corpus have separate terms. The documented composition patch uses local compute. Corpus creation and any licensed sample material are separate. [Source](https://github.com/DYCI2/om-dyci2/blob/master/README.md) [Source](https://aimc2021.iem.at/wp-content/uploads/2021/06/AIMC_2021_Nika_Bresson.pdf) [Source](https://github.com/cac-t-u-s/om-sharp)

Source and documentation review. No hands-on execution by AI Media Scout. Compiling the wrapper and pinning a compatible Python may require additional review. Use the tutorial patch to validate your actual runtime before composing.

### How it uses AI

OM-DYCI2 combines corpus-trained generative agents with the OM composition environment. A composer can guide sequence generation with a formal scenario. [Source](https://github.com/DYCI2/om-dyci2/blob/master/README.md) [Source](https://aimc2021.iem.at/wp-content/uploads/2021/06/AIMC_2021_Nika_Bresson.pdf) [Source](https://github.com/cac-t-u-s/om-sharp)

### Introduction

OM-DYCI2 combines corpus-trained generative agents with the OM composition environment. A composer can guide sequence generation with a formal scenario. [Source 1](https://github.com/DYCI2/om-dyci2/blob/master/README.md) [Source 2](https://aimc2021.iem.at/wp-content/uploads/2021/06/AIMC_2021_Nika_Bresson.pdf) [Source 3](https://github.com/cac-t-u-s/om-sharp)

### What it is good for

Compose a controlled run of musical phrases from a small corpus, keeping the scenario and resulting sequence editable in an OM patch. [Source 1](https://github.com/DYCI2/om-dyci2/blob/master/README.md) [Source 2](https://aimc2021.iem.at/wp-content/uploads/2021/06/AIMC_2021_Nika_Bresson.pdf) [Source 3](https://github.com/cac-t-u-s/om-sharp)

### Demo & examples

The maintained source includes tutorial patches. The IRCAM report describes an applied structured composition process using the model and OM environment. [Source 1](https://github.com/DYCI2/om-dyci2/blob/master/README.md) [Source 2](https://aimc2021.iem.at/wp-content/uploads/2021/06/AIMC_2021_Nika_Bresson.pdf) [Source 3](https://github.com/cac-t-u-s/om-sharp)

### Install

Follow the documented route for the scoped workflow. The steps below are source references. [Source 1](https://github.com/DYCI2/om-dyci2/blob/master/README.md) [Source 2](https://aimc2021.iem.at/wp-content/uploads/2021/06/AIMC_2021_Nika_Bresson.pdf) [Source 3](https://github.com/cac-t-u-s/om-sharp)

1. Use the documented macOS host, Python 3 and an appropriate OM# or OM6 installation. Follow the instructions to compile the C wrapper.
2. Add the wrapper and DYCI2 Python modules to the OM library location and open one of the supplied tutorial patches.

```sh
pip install -r python-requirements.txt
```

### First project

A small first project makes the input, model output and handoff easy to inspect. [Source 1](https://github.com/DYCI2/om-dyci2/blob/master/README.md) [Source 2](https://aimc2021.iem.at/wp-content/uploads/2021/06/AIMC_2021_Nika_Bresson.pdf) [Source 3](https://github.com/cac-t-u-s/om-sharp)

1. Use a simple 4–8-bar corpus with clear labels. Adjust one scenario property in the tutorial patch.
2. Generate phrase variations and compare which material was reused. Save the patch, corpus disclosure and a separate performance reference.
### Hardware & software

Platform and compute constraints refer to the selected route. [Source 1](https://github.com/DYCI2/om-dyci2/blob/master/README.md) [Source 2](https://aimc2021.iem.at/wp-content/uploads/2021/06/AIMC_2021_Nika_Bresson.pdf) [Source 3](https://github.com/cac-t-u-s/om-sharp)

- **Hardware:** Minimum RAM, VRAM and disk space for the scoped workflow are undocumented.
- **Software:** OM# or OM6, Python 3 and the requirements from the repository. The integration contains a compiled C wrapper.
- **Platforms:** The author documents tested compilation of the wrapper on macOS. Other paths have no confirmed support here.

### License, model weights & costs

The full software license was reviewed. Dependencies and creative assets carry their own terms. [Source 1](https://github.com/DYCI2/om-dyci2/blob/master/LICENSE) [Source 2](https://github.com/DYCI2/om-dyci2/blob/master/README.md) [Source 3](https://aimc2021.iem.at/wp-content/uploads/2021/06/AIMC_2021_Nika_Bresson.pdf) [Source 4](https://github.com/cac-t-u-s/om-sharp)

- **Code:** GPL-3.0
- **Weights:** The full GPLv3 software grant was reviewed. The host environment, Python dependencies and imported corpus have separate terms.
- **Commercial:** Project code is governed by GPL-3.0. Confirm selected model, source-media and output restrictions separately.
- **Cost:** The documented composition patch uses local compute. Corpus creation and any licensed sample material are separate.

### Why it merits attention

The creative workflow is grounded in the cited documentation. Output quality and compatibility are not hands-on verified. [Source 1](https://github.com/DYCI2/om-dyci2/blob/master/README.md) [Source 2](https://aimc2021.iem.at/wp-content/uploads/2021/06/AIMC_2021_Nika_Bresson.pdf) [Source 3](https://github.com/cac-t-u-s/om-sharp)

### Limitations

Compiling the wrapper and pinning a compatible Python may require additional review. Use the tutorial patch to validate your actual runtime before composing. [Source 1](https://github.com/DYCI2/om-dyci2/blob/master/README.md) [Source 2](https://aimc2021.iem.at/wp-content/uploads/2021/06/AIMC_2021_Nika_Bresson.pdf) [Source 3](https://github.com/cac-t-u-s/om-sharp)

### Get the tool

- [Repository](https://github.com/DYCI2/om-dyci2)
- [Documentation](https://github.com/cac-t-u-s/om-sharp)

## Ableton Studio MCP

Audio, music & voice · Performance, projection & stage media · AI assisted audio plugin and DSP authoring

The source repository was created on 2026-11-19. This is its first complete guide in the library.

### Quality assessment: Quality unverified

Creative use and the code grant are documented. Check-level gaps remain before a recommendation.

Scope: Ask a connected agent to create a short rhythm pattern in a separate Live set, then inspect and adjust the editable MIDI before mixing.

Evidence checked: 2026-11-21. No local execution implied.

- **Open-source software license · verified:** Reviewed the complete project software grant and its redistribution conditions. Model, data and service terms are scoped separately. [Source](https://github.com/cedrati/ableton-studio-mcp/blob/main/LICENSE)
- **Creative results · documented:** The maintainer documents a Live 12 workflow and server/script capability checking. It reports end-to-end testing. Independent reproduction is open. [Source](https://github.com/cedrati/ableton-studio-mcp/blob/main/README.md) [Source](https://pypi.org/project/ableton-studio-mcp/) [Source](https://www.ableton.com/en/live/)
- **Reproducible setup · documented:** The installation and first-use steps are in the cited documentation. Reproduction of this workflow remains unverified. [Source](https://github.com/cedrati/ableton-studio-mcp/blob/main/README.md) [Source](https://pypi.org/project/ableton-studio-mcp/) [Source](https://www.ableton.com/en/live/)
- **Maintenance and support · unknown:** The reviewed sources do not establish workflow-specific support, fixes and unresolved blockers.
- **Independent use · unknown:** Independent first-hand use of the exact workflow was not established in this source review.
- **Models, services and costs · documented:** The connector’s code is MIT. Ableton Live, plugins, samples and model/provider access retain separate licenses. An authorized Ableton installation and a model route are required. Model, instrument and optional host upgrades may incur charges. [Source](https://github.com/cedrati/ableton-studio-mcp/blob/main/README.md) [Source](https://pypi.org/project/ableton-studio-mcp/) [Source](https://www.ableton.com/en/live/)

Source and documentation review. No hands-on execution by AI Media Scout. Server and script versions must match capabilities. A remotely applied edit needs independent listening and versioning.

### How it uses AI

The MIT bridge connects an AI assistant to Ableton Live through MCP and a Remote Script. The assisted workflow can insert or edit MIDI tracks and query track data from the project. [Source](https://github.com/cedrati/ableton-studio-mcp/blob/main/README.md) [Source](https://pypi.org/project/ableton-studio-mcp/) [Source](https://www.ableton.com/en/live/)

### Introduction

The MIT bridge connects an AI assistant to Ableton Live through MCP and a Remote Script. The assisted workflow can insert or edit MIDI tracks and query track data from the project. [Source 1](https://github.com/cedrati/ableton-studio-mcp/blob/main/README.md) [Source 2](https://pypi.org/project/ableton-studio-mcp/) [Source 3](https://www.ableton.com/en/live/)

### What it is good for

Ask a connected agent to create a short rhythm pattern in a separate Live set, then inspect and adjust the editable MIDI before mixing. [Source 1](https://github.com/cedrati/ableton-studio-mcp/blob/main/README.md) [Source 2](https://pypi.org/project/ableton-studio-mcp/) [Source 3](https://www.ableton.com/en/live/)

### Demo & examples

The maintainer documents a Live 12 workflow and server/script capability checking. It reports end-to-end testing. Independent reproduction is open. [Source 1](https://github.com/cedrati/ableton-studio-mcp/blob/main/README.md) [Source 2](https://pypi.org/project/ableton-studio-mcp/) [Source 3](https://www.ableton.com/en/live/)

### Install

Follow the documented route for the scoped workflow. The steps below are source references. [Source 1](https://github.com/cedrati/ableton-studio-mcp/blob/main/README.md) [Source 2](https://pypi.org/project/ableton-studio-mcp/) [Source 3](https://www.ableton.com/en/live/)

1. Use the documented Live 11 or 12 route and uv. Install the Remote Script through the package and select it in Live.
2. Configure the MCP client with the package’s command and verify the project connection using a new set.

```sh
uvx ableton-studio-mcp
```


```sh
uvx --from ableton-studio-mcp ableton-studio-mcp-install-script
```

### First project

A small first project makes the input, model output and handoff easy to inspect. [Source 1](https://github.com/cedrati/ableton-studio-mcp/blob/main/README.md) [Source 2](https://pypi.org/project/ableton-studio-mcp/) [Source 3](https://www.ableton.com/en/live/)

1. Create a short reference set. Request one editable MIDI track or arrangement change.
2. Review the results in Live, compare playback and save a separate revision. Use only the commands your Live version reports as supported.
### Hardware & software

Platform and compute constraints refer to the selected route. [Source 1](https://github.com/cedrati/ableton-studio-mcp/blob/main/README.md) [Source 2](https://pypi.org/project/ableton-studio-mcp/) [Source 3](https://www.ableton.com/en/live/)

- **Hardware:** Minimum RAM, VRAM and disk space for the scoped workflow are undocumented.
- **Software:** Ableton Live 11 or 12, Python 3.10+ managed with uv, a compatible Remote Script and authenticated MCP/LLM client. Live 12 is documented for song-scale features.
- **Platforms:** Native OS coverage depends on the host version and the Remote Script. The README includes a macOS installation example. Do not assume native Linux Live support.

### License, model weights & costs

The full software license was reviewed. Dependencies and creative assets carry their own terms. [Source 1](https://github.com/cedrati/ableton-studio-mcp/blob/main/LICENSE) [Source 2](https://github.com/cedrati/ableton-studio-mcp/blob/main/README.md) [Source 3](https://pypi.org/project/ableton-studio-mcp/) [Source 4](https://www.ableton.com/en/live/)

- **Code:** MIT
- **Weights:** The connector’s code is MIT. Ableton Live, plugins, samples and model/provider access retain separate licenses.
- **Commercial:** Project code is governed by MIT. Confirm selected model, source-media and output restrictions separately.
- **Cost:** An authorized Ableton installation and a model route are required. Model, instrument and optional host upgrades may incur charges.

### Why it merits attention

The creative workflow is grounded in the cited documentation. Output quality and compatibility are not hands-on verified. [Source 1](https://github.com/cedrati/ableton-studio-mcp/blob/main/README.md) [Source 2](https://pypi.org/project/ableton-studio-mcp/) [Source 3](https://www.ableton.com/en/live/)

### Limitations

Server and script versions must match capabilities. A remotely applied edit needs independent listening and versioning. [Source 1](https://github.com/cedrati/ableton-studio-mcp/blob/main/README.md) [Source 2](https://pypi.org/project/ableton-studio-mcp/) [Source 3](https://www.ableton.com/en/live/)

### Get the tool

- [Repository](https://github.com/cedrati/ableton-studio-mcp)
- [Documentation](https://www.ableton.com/en/live/)

## WolfWorld

Photogrammetry, scanning & neural rendering · Spatial audio & volumetric media · 3D, reconstruction & assets

This completes an earlier pending guide with a current source review.

### Quality assessment: Experimental

Creative use and the code grant are documented. Check-level gaps remain before a recommendation.

Scope: Evaluate a captured-scene reconstruction workflow. Start by navigating an attributed example or separately imported splat before attempting a custom clip.

Evidence checked: 2026-11-21. No local execution implied.

Why Experimental: The maintainer calls it an experimental MVP and specifically reports that real GPU reconstruction acceptance is still pending. https://github.com/quake0day/WolfWorld/blob/main/README.md

- **Open-source software license · verified:** Reviewed the complete project software grant and its redistribution conditions. Model, data and service terms are scoped separately. [Source](https://github.com/quake0day/WolfWorld/blob/main/LICENSE)
- **Creative results · documented:** The upstream presents a sample viewer path. It explicitly states that WolfWorld has no confirmed end-to-end real GPU acceptance for reconstruction. Mock tests exercise the job boundary. [Source](https://github.com/quake0day/WolfWorld/blob/main/README.md) [Source](https://github.com/quake0day/WolfWorld/blob/main/worker/README.md) [Source](https://github.com/quake0day/WolfWorld/blob/main/docs/RESEARCH.md)
- **Reproducible setup · documented:** The installation and first-use steps are in the cited documentation. Reproduction of this workflow remains unverified. [Source](https://github.com/quake0day/WolfWorld/blob/main/README.md) [Source](https://github.com/quake0day/WolfWorld/blob/main/worker/README.md) [Source](https://github.com/quake0day/WolfWorld/blob/main/docs/RESEARCH.md)
- **Maintenance and support · unknown:** The reviewed sources do not establish workflow-specific support, fixes and unresolved blockers.
- **Independent use · unknown:** Independent first-hand use of the exact workflow was not established in this source review.
- **Models, services and costs · documented:** The complete MIT project code grant was reviewed. WorldMirror model terms, display libraries and source material remain separate. Viewer-only work uses local compute. GPU inference may require hardware or hosted capacity and model storage. [Source](https://github.com/quake0day/WolfWorld/blob/main/README.md) [Source](https://github.com/quake0day/WolfWorld/blob/main/worker/README.md) [Source](https://github.com/quake0day/WolfWorld/blob/main/docs/RESEARCH.md)

Source and documentation review. No hands-on execution by AI Media Scout. Real GPU reconstruction remains unverified by the author. Browser viewing of an example does not establish a working upload-to-reconstruction workflow.

### How it uses AI

WolfWorld provides an upload and review workspace that sends video frames to a WorldMirror 2.0 worker and opens the reconstructed Gaussian scene in the browser. [Source](https://github.com/quake0day/WolfWorld/blob/main/README.md) [Source](https://github.com/quake0day/WolfWorld/blob/main/worker/README.md) [Source](https://github.com/quake0day/WolfWorld/blob/main/docs/RESEARCH.md)

### Introduction

WolfWorld provides an upload and review workspace that sends video frames to a WorldMirror 2.0 worker and opens the reconstructed Gaussian scene in the browser. [Source 1](https://github.com/quake0day/WolfWorld/blob/main/README.md) [Source 2](https://github.com/quake0day/WolfWorld/blob/main/worker/README.md) [Source 3](https://github.com/quake0day/WolfWorld/blob/main/docs/RESEARCH.md)

### What it is good for

Evaluate a captured-scene reconstruction workflow. Start by navigating an attributed example or separately imported splat before attempting a custom clip. [Source 1](https://github.com/quake0day/WolfWorld/blob/main/README.md) [Source 2](https://github.com/quake0day/WolfWorld/blob/main/worker/README.md) [Source 3](https://github.com/quake0day/WolfWorld/blob/main/docs/RESEARCH.md)

### Demo & examples

The upstream presents a sample viewer path. It explicitly states that WolfWorld has no confirmed end-to-end real GPU acceptance for reconstruction. Mock tests exercise the job boundary. [Source 1](https://github.com/quake0day/WolfWorld/blob/main/README.md) [Source 2](https://github.com/quake0day/WolfWorld/blob/main/worker/README.md) [Source 3](https://github.com/quake0day/WolfWorld/blob/main/docs/RESEARCH.md)

### Install

Follow the documented route for the scoped workflow. The steps below are source references. [Source 1](https://github.com/quake0day/WolfWorld/blob/main/README.md) [Source 2](https://github.com/quake0day/WolfWorld/blob/main/worker/README.md) [Source 3](https://github.com/quake0day/WolfWorld/blob/main/docs/RESEARCH.md)

1. Use Node.js 24 LTS and the documented pnpm version for the viewer route.
2. For video reconstruction, follow the separate NVIDIA worker guide and establish permitted model artifacts and a functioning link to that worker.
### First project

A small first project makes the input, model output and handoff easy to inspect. [Source 1](https://github.com/quake0day/WolfWorld/blob/main/README.md) [Source 2](https://github.com/quake0day/WolfWorld/blob/main/worker/README.md) [Source 3](https://github.com/quake0day/WolfWorld/blob/main/docs/RESEARCH.md)

1. Open the supplied sample splat and get familiar with the browser controls.
2. If reproducing the research path, submit one short overlapping capture and monitor the job state. Compare coverage against the source footage and annotate missing areas.
### Hardware & software

Platform and compute constraints refer to the selected route. [Source 1](https://github.com/quake0day/WolfWorld/blob/main/README.md) [Source 2](https://github.com/quake0day/WolfWorld/blob/main/worker/README.md) [Source 3](https://github.com/quake0day/WolfWorld/blob/main/docs/RESEARCH.md)

- **Hardware:** Minimum RAM, VRAM and disk space for the scoped workflow are undocumented.
- **Software:** Node.js 24 LTS and pnpm 11.19.0 in the documented web workspace. Full reconstruction requires a compatible NVIDIA GPU, WorldMirror setup and worker dependencies.
- **Platforms:** The example viewer uses a browser. The actual reconstruction route is scoped to the documented separate NVIDIA worker. Broader native support is unverified.

### License, model weights & costs

The full software license was reviewed. Dependencies and creative assets carry their own terms. [Source 1](https://github.com/quake0day/WolfWorld/blob/main/LICENSE) [Source 2](https://github.com/quake0day/WolfWorld/blob/main/README.md) [Source 3](https://github.com/quake0day/WolfWorld/blob/main/worker/README.md) [Source 4](https://github.com/quake0day/WolfWorld/blob/main/docs/RESEARCH.md)

- **Code:** MIT
- **Weights:** The complete MIT project code grant was reviewed. WorldMirror model terms, display libraries and source material remain separate.
- **Commercial:** Project code is governed by MIT. Confirm selected model, source-media and output restrictions separately.
- **Cost:** Viewer-only work uses local compute. GPU inference may require hardware or hosted capacity and model storage.

### Why it merits attention

The creative workflow is grounded in the cited documentation. Output quality and compatibility are not hands-on verified. [Source 1](https://github.com/quake0day/WolfWorld/blob/main/README.md) [Source 2](https://github.com/quake0day/WolfWorld/blob/main/worker/README.md) [Source 3](https://github.com/quake0day/WolfWorld/blob/main/docs/RESEARCH.md)

### Limitations

Real GPU reconstruction remains unverified by the author. Browser viewing of an example does not establish a working upload-to-reconstruction workflow. [Source 1](https://github.com/quake0day/WolfWorld/blob/main/README.md) [Source 2](https://github.com/quake0day/WolfWorld/blob/main/worker/README.md) [Source 3](https://github.com/quake0day/WolfWorld/blob/main/docs/RESEARCH.md)

### Get the tool

- [Repository](https://github.com/quake0day/WolfWorld)
- [Documentation](https://github.com/quake0day/WolfWorld/blob/main/docs/RESEARCH.md)

## Local Video Transcribe

Editing, captions & post-production · Accessible media & assistive creation · Video, animation & film

This completes an earlier pending guide with a current source review.

### Quality assessment: Quality unverified

Creative use and the code grant are documented. Check-level gaps remain before a recommendation.

Scope: Create a Chinese or bilingual subtitle draft from an existing recording and keep the approved SRT as a separate non-destructive deliverable.

Evidence checked: 2026-11-21. No local execution implied.

- **Open-source software license · verified:** Reviewed the complete project software grant and its redistribution conditions. Model, data and service terms are scoped separately. [Source](https://github.com/zzh-editor/video-transcribe/blob/main/LICENSE)
- **Creative results · documented:** The bilingual documentation supplies example requests, filenames and a separate 9:16 subtitle route. It does not establish recognition accuracy on a specific video. [Source](https://github.com/zzh-editor/video-transcribe/blob/main/README.md) [Source](https://github.com/zzh-editor/video-transcribe/blob/main/SKILL.md)
- **Reproducible setup · documented:** The installation and first-use steps are in the cited documentation. Reproduction of this workflow remains unverified. [Source](https://github.com/zzh-editor/video-transcribe/blob/main/README.md) [Source](https://github.com/zzh-editor/video-transcribe/blob/main/SKILL.md)
- **Maintenance and support · unknown:** The reviewed sources do not establish workflow-specific support, fixes and unresolved blockers.
- **Independent use · unknown:** Independent first-hand use of the exact workflow was not established in this source review.
- **Models, services and costs · documented:** MIT covers the skill. Local model terms and any Groq service or correction model remain independent. Local inference uses compute. Hosted Groq access and the agent host have their own terms and potential charges. [Source](https://github.com/zzh-editor/video-transcribe/blob/main/README.md) [Source](https://github.com/zzh-editor/video-transcribe/blob/main/SKILL.md)

Source and documentation review. No hands-on execution by AI Media Scout. This route only accepts local media and has separate formatting steps. Transcription and translation still require review before publishing.

### How it uses AI

The agent workflow uses Whisper-based transcription of local files to prepare an SRT, then optionally routes it through a separate language workflow for bilingual layout or revision. [Source](https://github.com/zzh-editor/video-transcribe/blob/main/README.md) [Source](https://github.com/zzh-editor/video-transcribe/blob/main/SKILL.md)

### Introduction

The agent workflow uses Whisper-based transcription of local files to prepare an SRT, then optionally routes it through a separate language workflow for bilingual layout or revision. [Source 1](https://github.com/zzh-editor/video-transcribe/blob/main/README.md) [Source 2](https://github.com/zzh-editor/video-transcribe/blob/main/SKILL.md)

### What it is good for

Create a Chinese or bilingual subtitle draft from an existing recording and keep the approved SRT as a separate non-destructive deliverable. [Source 1](https://github.com/zzh-editor/video-transcribe/blob/main/README.md) [Source 2](https://github.com/zzh-editor/video-transcribe/blob/main/SKILL.md)

### Demo & examples

The bilingual documentation supplies example requests, filenames and a separate 9:16 subtitle route. It does not establish recognition accuracy on a specific video. [Source 1](https://github.com/zzh-editor/video-transcribe/blob/main/README.md) [Source 2](https://github.com/zzh-editor/video-transcribe/blob/main/SKILL.md)

### Install

Follow the documented route for the scoped workflow. The steps below are source references. [Source 1](https://github.com/zzh-editor/video-transcribe/blob/main/README.md) [Source 2](https://github.com/zzh-editor/video-transcribe/blob/main/SKILL.md)

1. Use an agent client that supports the documented packaged skill. Follow the skill’s dependency instructions for your machine, choosing the local recognizer before you need it.
2. Check the scope of optional Srt-Enhancer and hosted Groq access separately.
### First project

A small first project makes the input, model output and handoff easy to inspect. [Source 1](https://github.com/zzh-editor/video-transcribe/blob/main/README.md) [Source 2](https://github.com/zzh-editor/video-transcribe/blob/main/SKILL.md)

1. Attach a short local clip and specify original, translated or bilingual captions and the desired language order.
2. Review semantic segmentation and cue timing. Approve edits explicitly and compare the saved SRT against the source.
3. Keep the standard subtitle file when creating a separate vertical-layout version.
### Hardware & software

Platform and compute constraints refer to the selected route. [Source 1](https://github.com/zzh-editor/video-transcribe/blob/main/README.md) [Source 2](https://github.com/zzh-editor/video-transcribe/blob/main/SKILL.md)

- **Hardware:** Minimum RAM, VRAM and disk space for the scoped workflow are undocumented.
- **Software:** A compatible agent environment and Whisper route. The skill describes MLX on suitable Macs and faster-whisper elsewhere. Optional Groq and Srt-Enhancer are separate.
- **Platforms:** The documentation distinguishes Apple silicon MLX and a general faster-whisper path. It does not establish a full per-OS support matrix.

### License, model weights & costs

The full software license was reviewed. Dependencies and creative assets carry their own terms. [Source 1](https://github.com/zzh-editor/video-transcribe/blob/main/LICENSE) [Source 2](https://github.com/zzh-editor/video-transcribe/blob/main/README.md) [Source 3](https://github.com/zzh-editor/video-transcribe/blob/main/SKILL.md)

- **Code:** MIT
- **Weights:** MIT covers the skill. Local model terms and any Groq service or correction model remain independent.
- **Commercial:** Project code is governed by MIT. Confirm selected model, source-media and output restrictions separately.
- **Cost:** Local inference uses compute. Hosted Groq access and the agent host have their own terms and potential charges.

### Why it merits attention

The creative workflow is grounded in the cited documentation. Output quality and compatibility are not hands-on verified. [Source 1](https://github.com/zzh-editor/video-transcribe/blob/main/README.md) [Source 2](https://github.com/zzh-editor/video-transcribe/blob/main/SKILL.md)

### Limitations

This route only accepts local media and has separate formatting steps. Transcription and translation still require review before publishing. [Source 1](https://github.com/zzh-editor/video-transcribe/blob/main/README.md) [Source 2](https://github.com/zzh-editor/video-transcribe/blob/main/SKILL.md)

### Get the tool

- [Repository](https://github.com/zzh-editor/video-transcribe)
- [Documentation](https://github.com/zzh-editor/video-transcribe/blob/main/SKILL.md)

## Cutlass

Video, animation & film · Editing, captions & post-production · Accessible media & assistive creation

First complete guide in the library. The publication and documentation dates are not necessarily the project’s launch date.

### Quality assessment: Quality unverified

Creative use and the code grant are documented. Check-level gaps remain before a recommendation.

Scope: Draft an English cut with a local assistant, check the edited timeline and export editable subtitles with the resulting video.

Evidence checked: 2026-11-21. No local execution implied.

- **Open-source software license · verified:** Reviewed the complete project software grant and its redistribution conditions. Model, data and service terms are scoped separately. [Source](https://github.com/1mrnewton/cutlass/blob/main/LICENSE-APACHE)
- **Creative results · documented:** The official docs describe the timeline, output commands and separately configurable assistant, including its preview-frame ability for compatible visual models. [Source](https://github.com/1mrnewton/cutlass/blob/main/README.md) [Source](https://github.com/1mrnewton/cutlass/blob/main/LICENSE-MIT)
- **Reproducible setup · documented:** The installation and first-use steps are in the cited documentation. Reproduction of this workflow remains unverified. [Source](https://github.com/1mrnewton/cutlass/blob/main/README.md) [Source](https://github.com/1mrnewton/cutlass/blob/main/LICENSE-MIT)
- **Maintenance and support · unknown:** The reviewed sources do not establish workflow-specific support, fixes and unresolved blockers.
- **Independent use · unknown:** Independent first-hand use of the exact workflow was not established in this source review.
- **Models, services and costs · documented:** The project offers either MIT or Apache-2.0. Model weights, the chosen inference runner, fonts, codecs and imported assets retain separate terms. Local app and model compute apply. No hosted assistant is documented for this local route. [Source](https://github.com/1mrnewton/cutlass/blob/main/README.md) [Source](https://github.com/1mrnewton/cutlass/blob/main/LICENSE-MIT)

Source and documentation review. No hands-on execution by AI Media Scout. The current documentation scopes captions to English and lists missing features. Inspect actual render and model edits before production use.

### How it uses AI

Cutlass uses local speech recognition for editable English captions and lets a connected local model operate the same undoable timeline commands as the editor. [Source](https://github.com/1mrnewton/cutlass/blob/main/README.md) [Source](https://github.com/1mrnewton/cutlass/blob/main/LICENSE-MIT)

### Introduction

Cutlass uses local speech recognition for editable English captions and lets a connected local model operate the same undoable timeline commands as the editor. [Source 1](https://github.com/1mrnewton/cutlass/blob/main/README.md) [Source 2](https://github.com/1mrnewton/cutlass/blob/main/LICENSE-MIT)

### What it is good for

Draft an English cut with a local assistant, check the edited timeline and export editable subtitles with the resulting video. [Source 1](https://github.com/1mrnewton/cutlass/blob/main/README.md) [Source 2](https://github.com/1mrnewton/cutlass/blob/main/LICENSE-MIT)

### Demo & examples

The official docs describe the timeline, output commands and separately configurable assistant, including its preview-frame ability for compatible visual models. [Source 1](https://github.com/1mrnewton/cutlass/blob/main/README.md) [Source 2](https://github.com/1mrnewton/cutlass/blob/main/LICENSE-MIT)

### Install

Follow the documented route for the scoped workflow. The steps below are source references. [Source 1](https://github.com/1mrnewton/cutlass/blob/main/README.md) [Source 2](https://github.com/1mrnewton/cutlass/blob/main/LICENSE-MIT)

1. Use the documented macOS, Windows or Linux desktop package and checksums for the chosen release.
2. For agent-assisted edits choose a supported local model runner such as Ollama and configure Cutlass with its local address and model. Local captions can be used separately.
### First project

A small first project makes the input, model output and handoff easy to inspect. [Source 1](https://github.com/1mrnewton/cutlass/blob/main/README.md) [Source 2](https://github.com/1mrnewton/cutlass/blob/main/LICENSE-MIT)

1. Import a short English recording and prepare a duplicate working edit.
2. Generate captions, correct the cue list and ask for one reversible timeline change. Check the undo result before a longer edit.
3. Export the captions as SRT and compare the selected range with the source recording.
### Hardware & software

Platform and compute constraints refer to the selected route. [Source 1](https://github.com/1mrnewton/cutlass/blob/main/README.md) [Source 2](https://github.com/1mrnewton/cutlass/blob/main/LICENSE-MIT)

- **Hardware:** Minimum RAM, VRAM and disk space for the scoped workflow are undocumented.
- **Software:** Cutlass desktop build and its documented local speech stack. Optional assistant needs a compatible local inference runner. Visual inspection requires a model with image inputs.
- **Platforms:** Published desktop paths cover Apple silicon macOS, Windows 64-bit and Linux x86_64. Source directories for phone clients do not establish shipped feature parity.

### License, model weights & costs

The full software license was reviewed. Dependencies and creative assets carry their own terms. [Source 1](https://github.com/1mrnewton/cutlass/blob/main/LICENSE-APACHE) [Source 2](https://github.com/1mrnewton/cutlass/blob/main/README.md) [Source 3](https://github.com/1mrnewton/cutlass/blob/main/LICENSE-MIT)

- **Code:** Apache-2.0
- **Weights:** The project offers either MIT or Apache-2.0. Model weights, the chosen inference runner, fonts, codecs and imported assets retain separate terms.
- **Commercial:** Project code is governed by Apache-2.0. Confirm selected model, source-media and output restrictions separately.
- **Cost:** Local app and model compute apply. No hosted assistant is documented for this local route.

### Why it merits attention

The creative workflow is grounded in the cited documentation. Output quality and compatibility are not hands-on verified. [Source 1](https://github.com/1mrnewton/cutlass/blob/main/README.md) [Source 2](https://github.com/1mrnewton/cutlass/blob/main/LICENSE-MIT)

### Limitations

The current documentation scopes captions to English and lists missing features. Inspect actual render and model edits before production use. [Source 1](https://github.com/1mrnewton/cutlass/blob/main/README.md) [Source 2](https://github.com/1mrnewton/cutlass/blob/main/LICENSE-MIT)

### Get the tool

- [Repository](https://github.com/1mrnewton/cutlass)
- [Documentation](https://github.com/1mrnewton/cutlass/blob/main/LICENSE-MIT)

## Tab Agent Pro

AI music notation and score recovery · Audio, music & voice

First complete guide in the library. The publication and documentation dates are not necessarily the project’s launch date.

### Quality assessment: Quality unverified

Creative use and the code grant are documented. Check-level gaps remain before a recommendation.

Scope: Transcribe a short clean riff into a draft that a musician can inspect, correct and reuse in a DAW or tablature editor.

Evidence checked: 2026-11-21. No local execution implied.

- **Open-source software license · verified:** Reviewed the complete project software grant and its redistribution conditions. Model, data and service terms are scoped separately. [Source](https://github.com/sgm-audio/tab-agent-pro/blob/main/LICENSE)
- **Creative results · documented:** The upstream shows timed tab examples and documents a CPU Basic Pitch test route. Its checks do not establish that every suggested fingering is playable. [Source](https://github.com/sgm-audio/tab-agent-pro/blob/main/README.md) [Source](https://github.com/sgm-audio/tab-agent-pro/blob/main/THIRD_PARTY_NOTICES.md) [Source](https://github.com/spotify/basic-pitch)
- **Reproducible setup · documented:** The installation and first-use steps are in the cited documentation. Reproduction of this workflow remains unverified. [Source](https://github.com/sgm-audio/tab-agent-pro/blob/main/README.md) [Source](https://github.com/sgm-audio/tab-agent-pro/blob/main/THIRD_PARTY_NOTICES.md) [Source](https://github.com/spotify/basic-pitch)
- **Maintenance and support · documented:** Release v1.0.0 and current local route documentation were reviewed. Independent verification of transcription and playability remains open. [Source](https://github.com/sgm-audio/tab-agent-pro/releases/tag/v1.0.0)
- **Independent use · unknown:** Independent first-hand use of the exact workflow was not established in this source review.
- **Models, services and costs · documented:** MIT covers project code. Basic Pitch and optional Demucs weights, REAPER and each input source have separate terms. The scoped CPU inference can operate locally. Optional model downloads and commercial DAW access have separate costs. [Source](https://github.com/sgm-audio/tab-agent-pro/blob/main/README.md) [Source](https://github.com/sgm-audio/tab-agent-pro/blob/main/THIRD_PARTY_NOTICES.md) [Source](https://github.com/spotify/basic-pitch)

Source and documentation review. No hands-on execution by AI Media Scout. The tool does not infer slides or other playing techniques merely from note times. Treat fret assignments as editable suggestions.

### How it uses AI

Tab Agent Pro uses a Basic Pitch inference route to produce notes from guitar or bass audio, then solves suggested string and fret assignments into editable tab, MIDI and JSON. [Source](https://github.com/sgm-audio/tab-agent-pro/blob/main/README.md) [Source](https://github.com/sgm-audio/tab-agent-pro/blob/main/THIRD_PARTY_NOTICES.md) [Source](https://github.com/spotify/basic-pitch)

### Introduction

Tab Agent Pro uses a Basic Pitch inference route to produce notes from guitar or bass audio, then solves suggested string and fret assignments into editable tab, MIDI and JSON. [Source 1](https://github.com/sgm-audio/tab-agent-pro/blob/main/README.md) [Source 2](https://github.com/sgm-audio/tab-agent-pro/blob/main/THIRD_PARTY_NOTICES.md) [Source 3](https://github.com/spotify/basic-pitch)

### What it is good for

Transcribe a short clean riff into a draft that a musician can inspect, correct and reuse in a DAW or tablature editor. [Source 1](https://github.com/sgm-audio/tab-agent-pro/blob/main/README.md) [Source 2](https://github.com/sgm-audio/tab-agent-pro/blob/main/THIRD_PARTY_NOTICES.md) [Source 3](https://github.com/spotify/basic-pitch)

### Demo & examples

The upstream shows timed tab examples and documents a CPU Basic Pitch test route. Its checks do not establish that every suggested fingering is playable. [Source 1](https://github.com/sgm-audio/tab-agent-pro/blob/main/README.md) [Source 2](https://github.com/sgm-audio/tab-agent-pro/blob/main/THIRD_PARTY_NOTICES.md) [Source 3](https://github.com/spotify/basic-pitch)

### Install

Follow the documented route for the scoped workflow. The steps below are source references. [Source 1](https://github.com/sgm-audio/tab-agent-pro/blob/main/README.md) [Source 2](https://github.com/sgm-audio/tab-agent-pro/blob/main/THIRD_PARTY_NOTICES.md) [Source 3](https://github.com/spotify/basic-pitch)

1. Use the documented Linux CPU setup with Python 3.11 or later, or the recorded Docker route. Install the pinned CPU PyTorch and project runtime requirements.
2. Add FFmpeg and libsndfile for the relevant codecs. Start with the source-documented local route and verify the selected provider.
### First project

A small first project makes the input, model output and handoff easy to inspect. [Source 1](https://github.com/sgm-audio/tab-agent-pro/blob/main/README.md) [Source 2](https://github.com/sgm-audio/tab-agent-pro/blob/main/THIRD_PARTY_NOTICES.md) [Source 3](https://github.com/spotify/basic-pitch)

1. Import a monophonic reference riff with known pitches and timing.
2. Run the local transcription and compare timing, fret choices and omitted notes. Inspect source separation outcomes only if testing a multitrack recording.
3. Use the tab as a draft and compare the MIDI against the source in a separate editor.
### Hardware & software

Platform and compute constraints refer to the selected route. [Source 1](https://github.com/sgm-audio/tab-agent-pro/blob/main/README.md) [Source 2](https://github.com/sgm-audio/tab-agent-pro/blob/main/THIRD_PARTY_NOTICES.md) [Source 3](https://github.com/spotify/basic-pitch)

- **Hardware:** Minimum RAM, VRAM and disk space for the scoped workflow are undocumented.
- **Software:** Python 3.11+, documented CPU PyTorch pin, Basic Pitch ONNX route, appropriate input codecs and separate optional separation runtime.
- **Platforms:** Linux CPU and Docker setup are documented. Other host and REAPER integration routes require a version-specific check.

### License, model weights & costs

The full software license was reviewed. Dependencies and creative assets carry their own terms. [Source 1](https://github.com/sgm-audio/tab-agent-pro/blob/main/LICENSE) [Source 2](https://github.com/sgm-audio/tab-agent-pro/blob/main/README.md) [Source 3](https://github.com/sgm-audio/tab-agent-pro/blob/main/THIRD_PARTY_NOTICES.md) [Source 4](https://github.com/spotify/basic-pitch)

- **Code:** MIT
- **Weights:** MIT covers project code. Basic Pitch and optional Demucs weights, REAPER and each input source have separate terms.
- **Commercial:** Project code is governed by MIT. Confirm selected model, source-media and output restrictions separately.
- **Cost:** The scoped CPU inference can operate locally. Optional model downloads and commercial DAW access have separate costs.

### Why it merits attention

The creative workflow is grounded in the cited documentation. Output quality and compatibility are not hands-on verified. [Source 1](https://github.com/sgm-audio/tab-agent-pro/blob/main/README.md) [Source 2](https://github.com/sgm-audio/tab-agent-pro/blob/main/THIRD_PARTY_NOTICES.md) [Source 3](https://github.com/spotify/basic-pitch)

### Limitations

The tool does not infer slides or other playing techniques merely from note times. Treat fret assignments as editable suggestions. [Source 1](https://github.com/sgm-audio/tab-agent-pro/blob/main/README.md) [Source 2](https://github.com/sgm-audio/tab-agent-pro/blob/main/THIRD_PARTY_NOTICES.md) [Source 3](https://github.com/spotify/basic-pitch)

### Get the tool

- [Repository](https://github.com/sgm-audio/tab-agent-pro)
- [Documentation](https://github.com/spotify/basic-pitch)

## Wunjo Make

Editing, captions & post-production · Video, animation & film · Motion capture & character animation

This completes an earlier pending guide with a current source review.

### Quality assessment: Quality unverified

Creative use and the code grant are documented. Check-level gaps remain before a recommendation.

Scope: Use a connected agent for a reversible editing action and inspect the resulting native timeline before rendering.

Evidence checked: 2026-11-21. No local execution implied.

- **Open-source software license · verified:** Reviewed the complete project software grant and its redistribution conditions. Model, data and service terms are scoped separately. [Source](https://github.com/wladradchenko/wunjo.wladradchenko.ru/blob/main/LICENSE)
- **Creative results · documented:** The maintainer documents agent operations and publishes a demonstration link. The project distinguishes the newer v3 source from earlier v2 distributions. [Source](https://github.com/wladradchenko/wunjo.wladradchenko.ru/blob/main/README.md) [Source](https://wunjo.online/product/make/download/other) [Source](https://youtu.be/bMyT8sdPXsI)
- **Reproducible setup · documented:** The installation and first-use steps are in the cited documentation. Reproduction of this workflow remains unverified. [Source](https://github.com/wladradchenko/wunjo.wladradchenko.ru/blob/main/README.md) [Source](https://wunjo.online/product/make/download/other) [Source](https://youtu.be/bMyT8sdPXsI)
- **Maintenance and support · unknown:** The reviewed sources do not establish workflow-specific support, fixes and unresolved blockers.
- **Independent use · unknown:** Independent first-hand use of the exact workflow was not established in this source review.
- **Models, services and costs · documented:** GPLv3 covers the reviewed Wunjo code. The Kdenlive base, optional model plugins, creative assets and any provider have their own applicable notices. Native editing uses local compute. The selected external or local model requires its own resources or access. [Source](https://github.com/wladradchenko/wunjo.wladradchenko.ru/blob/main/README.md) [Source](https://wunjo.online/product/make/download/other) [Source](https://youtu.be/bMyT8sdPXsI)

Source and documentation review. No hands-on execution by AI Media Scout. The v3 plugin split does not match v2 feature parity. This profile focuses on a documented agent-operated timeline, with exact platform and render reproduction open.

### How it uses AI

Wunjo Make v3’s source documents an editable Kdenlive-derived timeline with MCP operations for a connected model. Separate plugins supply optional local or provider inference. [Source](https://github.com/wladradchenko/wunjo.wladradchenko.ru/blob/main/README.md) [Source](https://wunjo.online/product/make/download/other) [Source](https://youtu.be/bMyT8sdPXsI)

### Introduction

Wunjo Make v3’s source documents an editable Kdenlive-derived timeline with MCP operations for a connected model. Separate plugins supply optional local or provider inference. [Source 1](https://github.com/wladradchenko/wunjo.wladradchenko.ru/blob/main/README.md) [Source 2](https://wunjo.online/product/make/download/other) [Source 3](https://youtu.be/bMyT8sdPXsI)

### What it is good for

Use a connected agent for a reversible editing action and inspect the resulting native timeline before rendering. [Source 1](https://github.com/wladradchenko/wunjo.wladradchenko.ru/blob/main/README.md) [Source 2](https://wunjo.online/product/make/download/other) [Source 3](https://youtu.be/bMyT8sdPXsI)

### Demo & examples

The maintainer documents agent operations and publishes a demonstration link. The project distinguishes the newer v3 source from earlier v2 distributions. [Source 1](https://github.com/wladradchenko/wunjo.wladradchenko.ru/blob/main/README.md) [Source 2](https://wunjo.online/product/make/download/other) [Source 3](https://youtu.be/bMyT8sdPXsI)

### Install

Follow the documented route for the scoped workflow. The steps below are source references. [Source 1](https://github.com/wladradchenko/wunjo.wladradchenko.ru/blob/main/README.md) [Source 2](https://wunjo.online/product/make/download/other) [Source 3](https://youtu.be/bMyT8sdPXsI)

1. Choose the v3 source instructions for the platform you intend to use. An older v2 binary has a different application and plugin layout.
2. Configure the documented Python MCP route and supported client. Use a local model plugin only if you have the documented hardware and model access.
### First project

A small first project makes the input, model output and handoff easy to inspect. [Source 1](https://github.com/wladradchenko/wunjo.wladradchenko.ru/blob/main/README.md) [Source 2](https://wunjo.online/product/make/download/other) [Source 3](https://youtu.be/bMyT8sdPXsI)

1. Create a scratch project with a consented clip. Request one timeline change and inspect the resulting project operation.
2. Compare timing and export behavior using a small proof. Keep an unmodified edit and record the model/agent route.
### Hardware & software

Platform and compute constraints refer to the selected route. [Source 1](https://github.com/wladradchenko/wunjo.wladradchenko.ru/blob/main/README.md) [Source 2](https://wunjo.online/product/make/download/other) [Source 3](https://youtu.be/bMyT8sdPXsI)

- **Hardware:** The README identifies 8 GB VRAM and CUDA 12.x for the named local model plugin route. The connected-client route has different requirements. Other system minima are undocumented.
- **Software:** The v3 editing host and its source build or matching package, Python for the documented MCP server and a separate model or capable client.
- **Platforms:** The source documents Windows, Linux and macOS for the program. Verify exact v3 build availability and optional plugin compatibility separately.

### License, model weights & costs

The full software license was reviewed. Dependencies and creative assets carry their own terms. [Source 1](https://github.com/wladradchenko/wunjo.wladradchenko.ru/blob/main/LICENSE) [Source 2](https://github.com/wladradchenko/wunjo.wladradchenko.ru/blob/main/README.md) [Source 3](https://wunjo.online/product/make/download/other) [Source 4](https://youtu.be/bMyT8sdPXsI)

- **Code:** GPL-3.0
- **Weights:** GPLv3 covers the reviewed Wunjo code. The Kdenlive base, optional model plugins, creative assets and any provider have their own applicable notices.
- **Commercial:** Project code is governed by GPL-3.0. Confirm selected model, source-media and output restrictions separately.
- **Cost:** Native editing uses local compute. The selected external or local model requires its own resources or access.

### Why it merits attention

The creative workflow is grounded in the cited documentation. Output quality and compatibility are not hands-on verified. [Source 1](https://github.com/wladradchenko/wunjo.wladradchenko.ru/blob/main/README.md) [Source 2](https://wunjo.online/product/make/download/other) [Source 3](https://youtu.be/bMyT8sdPXsI)

### Limitations

The v3 plugin split does not match v2 feature parity. This profile focuses on a documented agent-operated timeline, with exact platform and render reproduction open. [Source 1](https://github.com/wladradchenko/wunjo.wladradchenko.ru/blob/main/README.md) [Source 2](https://wunjo.online/product/make/download/other) [Source 3](https://youtu.be/bMyT8sdPXsI)

### Get the tool

- [Repository](https://github.com/wladradchenko/wunjo.wladradchenko.ru)
- [Documentation](https://youtu.be/bMyT8sdPXsI)

## video-to-3d

Photogrammetry, scanning & neural rendering · Spatial audio & volumetric media · AI architectural visualization and spatial design

The source repository was created on 2026-11-10. This is its first complete guide in the library.

### Quality assessment: Quality unverified

Creative use and the code grant are documented. Check-level gaps remain before a recommendation.

Scope: Capture an early venue reference for a set, exhibit or projection sketch. Inspect which walls are missing and note confidence before drafting a layout.

Evidence checked: 2026-11-21. No local execution implied.

- **Open-source software license · verified:** Reviewed the complete project software grant and its redistribution conditions. Model, data and service terms are scoped separately. [Source](https://github.com/Srijjit-V/video-to-3d/blob/main/LICENSE)
- **Creative results · documented:** The author publishes paired synthetic examples with and without the far wall. The verification notes compare one run per setting against a known synthetic room. Real phone capture accuracy is open. [Source](https://github.com/Srijjit-V/video-to-3d/blob/main/README.md) [Source](https://github.com/Srijjit-V/video-to-3d/blob/main/docs/VERIFICATION.md) [Source](https://srijjit-v.github.io/video-to-3d/)
- **Reproducible setup · documented:** The installation and first-use steps are in the cited documentation. Reproduction of this workflow remains unverified. [Source](https://github.com/Srijjit-V/video-to-3d/blob/main/README.md) [Source](https://github.com/Srijjit-V/video-to-3d/blob/main/docs/VERIFICATION.md) [Source](https://srijjit-v.github.io/video-to-3d/)
- **Maintenance and support · unknown:** The reviewed sources do not establish workflow-specific support, fixes and unresolved blockers.
- **Independent use · unknown:** Independent first-hand use of the exact workflow was not established in this source review.
- **Models, services and costs · documented:** MIT governs code. COLMAP, model and venue-footage permissions remain separate. Local inference and test outputs use compute and disk. A server-based hybrid route has separate hosting and data-handling considerations. [Source](https://github.com/Srijjit-V/video-to-3d/blob/main/README.md) [Source](https://github.com/Srijjit-V/video-to-3d/blob/main/docs/VERIFICATION.md) [Source](https://srijjit-v.github.io/video-to-3d/)

Source and documentation review. No hands-on execution by AI Media Scout. Synthetic tests do not establish metric accuracy in real spaces. Mirror surfaces, moving subjects, darker images and missing walls can affect reliability.

### How it uses AI

video-to-3d estimates monocular depth in frames selected from a short phone recording. It fuses the estimated shapes with COLMAP camera positions and visualizes a point cloud and approximate measurements. [Source](https://github.com/Srijjit-V/video-to-3d/blob/main/README.md) [Source](https://github.com/Srijjit-V/video-to-3d/blob/main/docs/VERIFICATION.md) [Source](https://srijjit-v.github.io/video-to-3d/)

### Introduction

video-to-3d estimates monocular depth in frames selected from a short phone recording. It fuses the estimated shapes with COLMAP camera positions and visualizes a point cloud and approximate measurements. [Source 1](https://github.com/Srijjit-V/video-to-3d/blob/main/README.md) [Source 2](https://github.com/Srijjit-V/video-to-3d/blob/main/docs/VERIFICATION.md) [Source 3](https://srijjit-v.github.io/video-to-3d/)

### What it is good for

Capture an early venue reference for a set, exhibit or projection sketch. Inspect which walls are missing and note confidence before drafting a layout. [Source 1](https://github.com/Srijjit-V/video-to-3d/blob/main/README.md) [Source 2](https://github.com/Srijjit-V/video-to-3d/blob/main/docs/VERIFICATION.md) [Source 3](https://srijjit-v.github.io/video-to-3d/)

### Demo & examples

The author publishes paired synthetic examples with and without the far wall. The verification notes compare one run per setting against a known synthetic room. Real phone capture accuracy is open. [Source 1](https://github.com/Srijjit-V/video-to-3d/blob/main/README.md) [Source 2](https://github.com/Srijjit-V/video-to-3d/blob/main/docs/VERIFICATION.md) [Source 3](https://srijjit-v.github.io/video-to-3d/)

### Install

Follow the documented route for the scoped workflow. The steps below are source references. [Source 1](https://github.com/Srijjit-V/video-to-3d/blob/main/README.md) [Source 2](https://github.com/Srijjit-V/video-to-3d/blob/main/docs/VERIFICATION.md) [Source 3](https://srijjit-v.github.io/video-to-3d/)

1. Use the documented Python 3.11 environment and prepare COLMAP and the selected depth weights. Confirm enough space for a short local run.
2. Start with the bundled example for orientation before processing an authorized venue clip. The hosted viewer and local reconstruction path differ.
### First project

A small first project makes the input, model output and handoff easy to inspect. [Source 1](https://github.com/Srijjit-V/video-to-3d/blob/main/README.md) [Source 2](https://github.com/Srijjit-V/video-to-3d/blob/main/docs/VERIFICATION.md) [Source 3](https://srijjit-v.github.io/video-to-3d/)

1. Record a short continuous walk with visible corners and floor. Keep independent reference measurements for comparison.
2. Review missing sections of the PLY cloud and compare the estimated floor plan with observations.
3. Mark the measurement confidence on exported layout references. Keep the original capture so the scene can be checked against it.
### Hardware & software

Platform and compute constraints refer to the selected route. [Source 1](https://github.com/Srijjit-V/video-to-3d/blob/main/README.md) [Source 2](https://github.com/Srijjit-V/video-to-3d/blob/main/docs/VERIFICATION.md) [Source 3](https://srijjit-v.github.io/video-to-3d/)

- **Hardware:** The local setup documents about 2 GB disk, initial model download near 100 MB, and an author test on an Apple M2. Broad RAM and VRAM minima are undocumented.
- **Software:** Python 3.11, COLMAP camera solving and selected depth model runtime. The browser route offers distinct hosted sample and hybrid paths.
- **Platforms:** Author tests on an Apple M2 MacBook are documented. Windows, Linux and CUDA performance are unverified by the project.

### License, model weights & costs

The full software license was reviewed. Dependencies and creative assets carry their own terms. [Source 1](https://github.com/Srijjit-V/video-to-3d/blob/main/LICENSE) [Source 2](https://github.com/Srijjit-V/video-to-3d/blob/main/README.md) [Source 3](https://github.com/Srijjit-V/video-to-3d/blob/main/docs/VERIFICATION.md) [Source 4](https://srijjit-v.github.io/video-to-3d/)

- **Code:** MIT
- **Weights:** MIT governs code. COLMAP, model and venue-footage permissions remain separate.
- **Commercial:** Project code is governed by MIT. Confirm selected model, source-media and output restrictions separately.
- **Cost:** Local inference and test outputs use compute and disk. A server-based hybrid route has separate hosting and data-handling considerations.

### Why it merits attention

The creative workflow is grounded in the cited documentation. Output quality and compatibility are not hands-on verified. [Source 1](https://github.com/Srijjit-V/video-to-3d/blob/main/README.md) [Source 2](https://github.com/Srijjit-V/video-to-3d/blob/main/docs/VERIFICATION.md) [Source 3](https://srijjit-v.github.io/video-to-3d/)

### Limitations

Synthetic tests do not establish metric accuracy in real spaces. Mirror surfaces, moving subjects, darker images and missing walls can affect reliability. [Source 1](https://github.com/Srijjit-V/video-to-3d/blob/main/README.md) [Source 2](https://github.com/Srijjit-V/video-to-3d/blob/main/docs/VERIFICATION.md) [Source 3](https://srijjit-v.github.io/video-to-3d/)

### Get the tool

- [Repository](https://github.com/Srijjit-V/video-to-3d)
- [Documentation](https://srijjit-v.github.io/video-to-3d/)

## DCL Motion Studio

Motion capture & character animation · Avatars, digital humans & lip sync · WebXR, VR & AR

The source repository was created on 2026-11-02. This is its first complete guide in the library.

### Quality assessment: Quality unverified

Creative use and the code grant are documented. Check-level gaps remain before a recommendation.

Scope: Draft a Decentraland avatar gesture from a short prompt or rights-cleared reference clip and export the reviewed motion as a GLB.

Evidence checked: 2026-11-21. No local execution implied.

- **Open-source software license · verified:** Reviewed the complete project software grant and its redistribution conditions. Model, data and service terms are scoped separately. [Source](https://github.com/TonyDark0/dcl-motion-studio/blob/main/LICENSE)
- **Creative results · documented:** The project publishes text- and video-derived animation examples and explains montage, retargeting and end constraints. It distinguishes the examples from benchmarks. [Source](https://github.com/TonyDark0/dcl-motion-studio/blob/main/README.md) [Source](https://github.com/TonyDark0/dcl-motion-studio/blob/main/docs/LICENSING.md) [Source](https://github.com/TonyDark0/dcl-motion-studio/blob/main/docs/MODELS_AND_RUNTIMES.md) [Source](https://github.com/TonyDark0/dcl-motion-studio/blob/main/docs/GETTING_STARTED.md)
- **Reproducible setup · documented:** The installation and first-use steps are in the cited documentation. Reproduction of this workflow remains unverified. [Source](https://github.com/TonyDark0/dcl-motion-studio/blob/main/README.md) [Source](https://github.com/TonyDark0/dcl-motion-studio/blob/main/docs/LICENSING.md) [Source](https://github.com/TonyDark0/dcl-motion-studio/blob/main/docs/MODELS_AND_RUNTIMES.md) [Source](https://github.com/TonyDark0/dcl-motion-studio/blob/main/docs/GETTING_STARTED.md)
- **Maintenance and support · unknown:** The reviewed sources do not establish workflow-specific support, fixes and unresolved blockers.
- **Independent use · unknown:** Independent first-hand use of the exact workflow was not established in this source review.
- **Models, services and costs · documented:** Application code is Apache-2.0. The motion model uses NVIDIA Open Model terms. The Llama text encoder has Meta Community terms. The avatar, RTMW3D and other models retain separate notices. Local builds require storage and compute. Pro capture requires model access approval separately. [Source](https://github.com/TonyDark0/dcl-motion-studio/blob/main/README.md) [Source](https://github.com/TonyDark0/dcl-motion-studio/blob/main/docs/LICENSING.md) [Source](https://github.com/TonyDark0/dcl-motion-studio/blob/main/docs/MODELS_AND_RUNTIMES.md) [Source](https://github.com/TonyDark0/dcl-motion-studio/blob/main/docs/GETTING_STARTED.md)

Source and documentation review. No hands-on execution by AI Media Scout. The editor targets the DCL skeleton and does not have a general animation keyframe editor. Test joint contacts and host compatibility for each export.

### How it uses AI

DCL Motion Studio generates constrained skeletal motion using Kimodo. Its Fast capture path combines browser MediaPipe pose tracking with local RTMW3D inference, followed by editable retargeting. [Source](https://github.com/TonyDark0/dcl-motion-studio/blob/main/README.md) [Source](https://github.com/TonyDark0/dcl-motion-studio/blob/main/docs/LICENSING.md) [Source](https://github.com/TonyDark0/dcl-motion-studio/blob/main/docs/MODELS_AND_RUNTIMES.md) [Source](https://github.com/TonyDark0/dcl-motion-studio/blob/main/docs/GETTING_STARTED.md)

### Introduction

DCL Motion Studio generates constrained skeletal motion using Kimodo. Its Fast capture path combines browser MediaPipe pose tracking with local RTMW3D inference, followed by editable retargeting. [Source 1](https://github.com/TonyDark0/dcl-motion-studio/blob/main/README.md) [Source 2](https://github.com/TonyDark0/dcl-motion-studio/blob/main/docs/LICENSING.md) [Source 3](https://github.com/TonyDark0/dcl-motion-studio/blob/main/docs/MODELS_AND_RUNTIMES.md) [Source 4](https://github.com/TonyDark0/dcl-motion-studio/blob/main/docs/GETTING_STARTED.md)

### What it is good for

Draft a Decentraland avatar gesture from a short prompt or rights-cleared reference clip and export the reviewed motion as a GLB. [Source 1](https://github.com/TonyDark0/dcl-motion-studio/blob/main/README.md) [Source 2](https://github.com/TonyDark0/dcl-motion-studio/blob/main/docs/LICENSING.md) [Source 3](https://github.com/TonyDark0/dcl-motion-studio/blob/main/docs/MODELS_AND_RUNTIMES.md) [Source 4](https://github.com/TonyDark0/dcl-motion-studio/blob/main/docs/GETTING_STARTED.md)

### Demo & examples

The project publishes text- and video-derived animation examples and explains montage, retargeting and end constraints. It distinguishes the examples from benchmarks. [Source 1](https://github.com/TonyDark0/dcl-motion-studio/blob/main/README.md) [Source 2](https://github.com/TonyDark0/dcl-motion-studio/blob/main/docs/LICENSING.md) [Source 3](https://github.com/TonyDark0/dcl-motion-studio/blob/main/docs/MODELS_AND_RUNTIMES.md) [Source 4](https://github.com/TonyDark0/dcl-motion-studio/blob/main/docs/GETTING_STARTED.md)

### Install

Follow the documented route for the scoped workflow. The steps below are source references. [Source 1](https://github.com/TonyDark0/dcl-motion-studio/blob/main/README.md) [Source 2](https://github.com/TonyDark0/dcl-motion-studio/blob/main/docs/LICENSING.md) [Source 3](https://github.com/TonyDark0/dcl-motion-studio/blob/main/docs/MODELS_AND_RUNTIMES.md) [Source 4](https://github.com/TonyDark0/dcl-motion-studio/blob/main/docs/GETTING_STARTED.md)

1. Follow the Windows x64 setup for Node.js 24, FFmpeg, models and the compiled Kimodo runtime. Check the documentation for the necessary build tools.
2. Keep the supplied DCL base avatar in its documented location. Use the Fast capture path initially if a separate Pro capture environment has not been provisioned.
### First project

A small first project makes the input, model output and handoff easy to inspect. [Source 1](https://github.com/TonyDark0/dcl-motion-studio/blob/main/README.md) [Source 2](https://github.com/TonyDark0/dcl-motion-studio/blob/main/docs/LICENSING.md) [Source 3](https://github.com/TonyDark0/dcl-motion-studio/blob/main/docs/MODELS_AND_RUNTIMES.md) [Source 4](https://github.com/TonyDark0/dcl-motion-studio/blob/main/docs/GETTING_STARTED.md)

1. Generate a short gesture or load an owned clip. Inspect the captured motion and joint alignment before rendering.
2. Use the hand, foot and pelvis adjustments or trim controls to correct drift and contact points.
3. Export an animated GLB for the DCL skeleton and check it in the downstream viewer. Retain the editable project.
### Hardware & software

Platform and compute constraints refer to the selected route. [Source 1](https://github.com/TonyDark0/dcl-motion-studio/blob/main/README.md) [Source 2](https://github.com/TonyDark0/dcl-motion-studio/blob/main/docs/LICENSING.md) [Source 3](https://github.com/TonyDark0/dcl-motion-studio/blob/main/docs/MODELS_AND_RUNTIMES.md) [Source 4](https://github.com/TonyDark0/dcl-motion-studio/blob/main/docs/GETTING_STARTED.md)

- **Hardware:** The documented model setup downloads roughly 6.6 GB including the text encoder. Fast capture and text generation have CPU paths. Pro capture lists a compatible NVIDIA GPU, with memory needs depending on route.
- **Software:** Node.js 24, WebGL browser, FFmpeg/FFprobe, compiled Kimodo engine and pinned models. Pro capture uses a distinct Python/PyTorch environment and additional controlled model access.
- **Platforms:** Detailed source build instructions target Windows x64 and PowerShell. The hosted demo is a separate browser route.

### License, model weights & costs

The full software license was reviewed. Dependencies and creative assets carry their own terms. [Source 1](https://github.com/TonyDark0/dcl-motion-studio/blob/main/LICENSE) [Source 2](https://github.com/TonyDark0/dcl-motion-studio/blob/main/README.md) [Source 3](https://github.com/TonyDark0/dcl-motion-studio/blob/main/docs/LICENSING.md) [Source 4](https://github.com/TonyDark0/dcl-motion-studio/blob/main/docs/MODELS_AND_RUNTIMES.md) [Source 5](https://github.com/TonyDark0/dcl-motion-studio/blob/main/docs/GETTING_STARTED.md)

- **Code:** Apache-2.0
- **Weights:** Application code is Apache-2.0. The motion model uses NVIDIA Open Model terms. The Llama text encoder has Meta Community terms. The avatar, RTMW3D and other models retain separate notices.
- **Commercial:** Project code is governed by Apache-2.0. Confirm selected model, source-media and output restrictions separately.
- **Cost:** Local builds require storage and compute. Pro capture requires model access approval separately.

### Why it merits attention

The creative workflow is grounded in the cited documentation. Output quality and compatibility are not hands-on verified. [Source 1](https://github.com/TonyDark0/dcl-motion-studio/blob/main/README.md) [Source 2](https://github.com/TonyDark0/dcl-motion-studio/blob/main/docs/LICENSING.md) [Source 3](https://github.com/TonyDark0/dcl-motion-studio/blob/main/docs/MODELS_AND_RUNTIMES.md) [Source 4](https://github.com/TonyDark0/dcl-motion-studio/blob/main/docs/GETTING_STARTED.md)

### Limitations

The editor targets the DCL skeleton and does not have a general animation keyframe editor. Test joint contacts and host compatibility for each export. [Source 1](https://github.com/TonyDark0/dcl-motion-studio/blob/main/README.md) [Source 2](https://github.com/TonyDark0/dcl-motion-studio/blob/main/docs/LICENSING.md) [Source 3](https://github.com/TonyDark0/dcl-motion-studio/blob/main/docs/MODELS_AND_RUNTIMES.md) [Source 4](https://github.com/TonyDark0/dcl-motion-studio/blob/main/docs/GETTING_STARTED.md)

### Get the tool

- [Repository](https://github.com/TonyDark0/dcl-motion-studio)
- [Documentation](https://github.com/TonyDark0/dcl-motion-studio/blob/main/docs/GETTING_STARTED.md)

## AssetRefGen

3D, reconstruction & assets · AI agents for code-authored media production · Avatars, digital humans & lip sync

The source repository was created on 2026-11-17. This is its first complete guide in the library.

### Quality assessment: Quality unverified

Creative use and the code grant are documented. Check-level gaps remain before a recommendation.

Scope: Turn an authorized character lineup into consistently named front, side and rear reference images for a 3D artist.

Evidence checked: 2026-11-21. No local execution implied.

- **Open-source software license · verified:** Reviewed the complete project software grant and its redistribution conditions. Model, data and service terms are scoped separately. [Source](https://github.com/AERIF-Dev/AssetRefGen/blob/main/LICENSE)
- **Creative results · documented:** The author supplies a lineup, an isolated master and a contact preview. The method’s generated views approximate camera angles and can vary in geometry and seams. [Source](https://github.com/AERIF-Dev/AssetRefGen/blob/main/README.md) [Source](https://github.com/AERIF-Dev/AssetRefGen/blob/main/CHANGELOG.md) [Source](https://github.com/AERIF-Dev/AssetRefGen/blob/main/THIRD_PARTY_NOTICES.md)
- **Reproducible setup · documented:** The installation and first-use steps are in the cited documentation. Reproduction of this workflow remains unverified. [Source](https://github.com/AERIF-Dev/AssetRefGen/blob/main/README.md) [Source](https://github.com/AERIF-Dev/AssetRefGen/blob/main/CHANGELOG.md) [Source](https://github.com/AERIF-Dev/AssetRefGen/blob/main/THIRD_PARTY_NOTICES.md)
- **Maintenance and support · documented:** The v0.2.0 release and changelog document the current supported skill and helper routes. [Source](https://github.com/AERIF-Dev/AssetRefGen/releases/tag/v0.2.0)
- **Independent use · unknown:** Independent first-hand use of the exact workflow was not established in this source review.
- **Models, services and costs · documented:** The complete MIT license governs the tool. Rights for reference art and for the selected image provider’s output are separate. The repository supplies no generation credits. Agent and image model access may consume usage allowance. [Source](https://github.com/AERIF-Dev/AssetRefGen/blob/main/README.md) [Source](https://github.com/AERIF-Dev/AssetRefGen/blob/main/CHANGELOG.md) [Source](https://github.com/AERIF-Dev/AssetRefGen/blob/main/THIRD_PARTY_NOTICES.md)

Source and documentation review. No hands-on execution by AI Media Scout. Generated views are visual modeling references. Inconsistent angles or details still need manual correction before modeling.

### How it uses AI

AssetRefGen orchestrates image-model calls in an agent session to produce concept-art view sets. Python helpers organize master images, PNG views, contact sheets and production notes. [Source](https://github.com/AERIF-Dev/AssetRefGen/blob/main/README.md) [Source](https://github.com/AERIF-Dev/AssetRefGen/blob/main/CHANGELOG.md) [Source](https://github.com/AERIF-Dev/AssetRefGen/blob/main/THIRD_PARTY_NOTICES.md)

### Introduction

AssetRefGen orchestrates image-model calls in an agent session to produce concept-art view sets. Python helpers organize master images, PNG views, contact sheets and production notes. [Source 1](https://github.com/AERIF-Dev/AssetRefGen/blob/main/README.md) [Source 2](https://github.com/AERIF-Dev/AssetRefGen/blob/main/CHANGELOG.md) [Source 3](https://github.com/AERIF-Dev/AssetRefGen/blob/main/THIRD_PARTY_NOTICES.md)

### What it is good for

Turn an authorized character lineup into consistently named front, side and rear reference images for a 3D artist. [Source 1](https://github.com/AERIF-Dev/AssetRefGen/blob/main/README.md) [Source 2](https://github.com/AERIF-Dev/AssetRefGen/blob/main/CHANGELOG.md) [Source 3](https://github.com/AERIF-Dev/AssetRefGen/blob/main/THIRD_PARTY_NOTICES.md)

### Demo & examples

The author supplies a lineup, an isolated master and a contact preview. The method’s generated views approximate camera angles and can vary in geometry and seams. [Source 1](https://github.com/AERIF-Dev/AssetRefGen/blob/main/README.md) [Source 2](https://github.com/AERIF-Dev/AssetRefGen/blob/main/CHANGELOG.md) [Source 3](https://github.com/AERIF-Dev/AssetRefGen/blob/main/THIRD_PARTY_NOTICES.md)

### Install

Follow the documented route for the scoped workflow. The steps below are source references. [Source 1](https://github.com/AERIF-Dev/AssetRefGen/blob/main/README.md) [Source 2](https://github.com/AERIF-Dev/AssetRefGen/blob/main/CHANGELOG.md) [Source 3](https://github.com/AERIF-Dev/AssetRefGen/blob/main/THIRD_PARTY_NOTICES.md)

1. Choose the project’s pinned skill-only distribution or source release. Set up the documented Python and Pillow helpers and a session with a supported image-generation tool.
2. Use a sandbox project folder with only the original concept images you can share with the selected model.
### First project

A small first project makes the input, model output and handoff easy to inspect. [Source 1](https://github.com/AERIF-Dev/AssetRefGen/blob/main/README.md) [Source 2](https://github.com/AERIF-Dev/AssetRefGen/blob/main/CHANGELOG.md) [Source 3](https://github.com/AERIF-Dev/AssetRefGen/blob/main/THIRD_PARTY_NOTICES.md)

1. Select one character in a test lineup and create a clean master reference. Check details with the original artist.
2. Produce a small multi-view set. Compare silhouette, garment closure and materials across views.
3. Pass the accepted PNG reference set and QA notes to modeling. Keep any unresolved pose discrepancies visible.
### Hardware & software

Platform and compute constraints refer to the selected route. [Source 1](https://github.com/AERIF-Dev/AssetRefGen/blob/main/README.md) [Source 2](https://github.com/AERIF-Dev/AssetRefGen/blob/main/CHANGELOG.md) [Source 3](https://github.com/AERIF-Dev/AssetRefGen/blob/main/THIRD_PARTY_NOTICES.md)

- **Hardware:** Minimum RAM, VRAM and disk space for the scoped workflow are undocumented.
- **Software:** AssetRefGen v0.2.0, Python 3.10+, Pillow 10.1+ and a Codex session with supported image generation. Model generation does not come with the skill.
- **Platforms:** The author reports validation of its file helpers on Windows and Linux. macOS helper compatibility is undocumented.

### License, model weights & costs

The full software license was reviewed. Dependencies and creative assets carry their own terms. [Source 1](https://github.com/AERIF-Dev/AssetRefGen/blob/main/LICENSE) [Source 2](https://github.com/AERIF-Dev/AssetRefGen/blob/main/README.md) [Source 3](https://github.com/AERIF-Dev/AssetRefGen/blob/main/CHANGELOG.md) [Source 4](https://github.com/AERIF-Dev/AssetRefGen/blob/main/THIRD_PARTY_NOTICES.md)

- **Code:** MIT
- **Weights:** The complete MIT license governs the tool. Rights for reference art and for the selected image provider’s output are separate.
- **Commercial:** Project code is governed by MIT. Confirm selected model, source-media and output restrictions separately.
- **Cost:** The repository supplies no generation credits. Agent and image model access may consume usage allowance.

### Why it merits attention

The creative workflow is grounded in the cited documentation. Output quality and compatibility are not hands-on verified. [Source 1](https://github.com/AERIF-Dev/AssetRefGen/blob/main/README.md) [Source 2](https://github.com/AERIF-Dev/AssetRefGen/blob/main/CHANGELOG.md) [Source 3](https://github.com/AERIF-Dev/AssetRefGen/blob/main/THIRD_PARTY_NOTICES.md)

### Limitations

Generated views are visual modeling references. Inconsistent angles or details still need manual correction before modeling. [Source 1](https://github.com/AERIF-Dev/AssetRefGen/blob/main/README.md) [Source 2](https://github.com/AERIF-Dev/AssetRefGen/blob/main/CHANGELOG.md) [Source 3](https://github.com/AERIF-Dev/AssetRefGen/blob/main/THIRD_PARTY_NOTICES.md)

### Get the tool

- [Repository](https://github.com/AERIF-Dev/AssetRefGen)
- [Documentation](https://github.com/AERIF-Dev/AssetRefGen/blob/main/THIRD_PARTY_NOTICES.md)

## Kiln

AI-assisted textile and computational craft · Photography, restoration & color · Creative publishing & presentation

The source repository was created on 2026-11-03. This is its first complete guide in the library.

### Quality assessment: Quality unverified

Creative use and the code grant are documented. Check-level gaps remain before a recommendation.

Scope: Prepare reviewable web product plates and labeled size or color views for a shop listing using rights-cleared reference inputs.

Evidence checked: 2026-11-21. No local execution implied.

- **Open-source software license · verified:** Reviewed the complete project software grant and its redistribution conditions. Model, data and service terms are scoped separately. [Source](https://github.com/luiscarbonel1991/kiln/blob/main/LICENSE)
- **Creative results · documented:** The author publishes a serving-board example with reported lettering checks and distinguishes its deterministic specification drawings from generated promotional scenes. [Source](https://github.com/luiscarbonel1991/kiln/blob/main/README.md) [Source](https://github.com/luiscarbonel1991/kiln/blob/main/docker-compose.yml)
- **Reproducible setup · documented:** The installation and first-use steps are in the cited documentation. Reproduction of this workflow remains unverified. [Source](https://github.com/luiscarbonel1991/kiln/blob/main/README.md) [Source](https://github.com/luiscarbonel1991/kiln/blob/main/docker-compose.yml)
- **Maintenance and support · unknown:** The reviewed sources do not establish workflow-specific support, fixes and unresolved blockers.
- **Independent use · unknown:** Independent first-hand use of the exact workflow was not established in this source review.
- **Models, services and costs · documented:** The project declares AGPL-3.0-only. Image/model providers, product designs and reference images carry separate terms. Local deterministic drawings require the server and workstation. Generative calls may be paid. The application documents per-call estimates and account spending caps. [Source](https://github.com/luiscarbonel1991/kiln/blob/main/README.md) [Source](https://github.com/luiscarbonel1991/kiln/blob/main/docker-compose.yml)

Source and documentation review. No hands-on execution by AI Media Scout. Replace inaccurate model-generated lettering or scale with reviewed artwork. Packaging lists and proof images are distinct from physical production files.

### How it uses AI

Kiln combines editable product data with provider-generated scenes and listings. The tool compares the rendered text, lettering and sizing claims against the product brief. [Source](https://github.com/luiscarbonel1991/kiln/blob/main/README.md) [Source](https://github.com/luiscarbonel1991/kiln/blob/main/docker-compose.yml)

### Introduction

Kiln combines editable product data with provider-generated scenes and listings. The tool compares the rendered text, lettering and sizing claims against the product brief. [Source 1](https://github.com/luiscarbonel1991/kiln/blob/main/README.md) [Source 2](https://github.com/luiscarbonel1991/kiln/blob/main/docker-compose.yml)

### What it is good for

Prepare reviewable web product plates and labeled size or color views for a shop listing using rights-cleared reference inputs. [Source 1](https://github.com/luiscarbonel1991/kiln/blob/main/README.md) [Source 2](https://github.com/luiscarbonel1991/kiln/blob/main/docker-compose.yml)

### Demo & examples

The author publishes a serving-board example with reported lettering checks and distinguishes its deterministic specification drawings from generated promotional scenes. [Source 1](https://github.com/luiscarbonel1991/kiln/blob/main/README.md) [Source 2](https://github.com/luiscarbonel1991/kiln/blob/main/docker-compose.yml)

### Install

Follow the documented route for the scoped workflow. The steps below are source references. [Source 1](https://github.com/luiscarbonel1991/kiln/blob/main/README.md) [Source 2](https://github.com/luiscarbonel1991/kiln/blob/main/docker-compose.yml)

1. Use the project’s Docker Compose application profile. Complete the initial local owner setup and make a small product entry.
2. For generated scenes and text, configure a supported provider under the documented settings and review cost controls before use.
### First project

A small first project makes the input, model output and handoff easy to inspect. [Source 1](https://github.com/luiscarbonel1991/kiln/blob/main/README.md) [Source 2](https://github.com/luiscarbonel1991/kiln/blob/main/docker-compose.yml)

1. Enter the product’s actual material, dimensions, finish and lettering. Confirm the deterministic plates against physical dimensions.
2. Draft a promotional scene and inspect spelling, proportions, materials and configuration against source photographs.
3. Export selected artwork for the listing. Preserve the editable specification and separate accepted and rejected render candidates.
### Hardware & software

Platform and compute constraints refer to the selected route. [Source 1](https://github.com/luiscarbonel1991/kiln/blob/main/README.md) [Source 2](https://github.com/luiscarbonel1991/kiln/blob/main/docker-compose.yml)

- **Hardware:** Minimum RAM, VRAM and disk space for the scoped workflow are undocumented.
- **Software:** Docker Compose for the documented local service. Paid generation uses a separately chosen and configured provider. Additional development uses the project’s pinned Node/pnpm and database stack.
- **Platforms:** Docker-based local server and browser use are documented. Host-specific installation validation is open.

### License, model weights & costs

The full software license was reviewed. Dependencies and creative assets carry their own terms. [Source 1](https://github.com/luiscarbonel1991/kiln/blob/main/LICENSE) [Source 2](https://github.com/luiscarbonel1991/kiln/blob/main/README.md) [Source 3](https://github.com/luiscarbonel1991/kiln/blob/main/docker-compose.yml)

- **Code:** AGPL-3.0
- **Weights:** The project declares AGPL-3.0-only. Image/model providers, product designs and reference images carry separate terms.
- **Commercial:** Project code is governed by AGPL-3.0. Confirm selected model, source-media and output restrictions separately.
- **Cost:** Local deterministic drawings require the server and workstation. Generative calls may be paid. The application documents per-call estimates and account spending caps.

### Why it merits attention

The creative workflow is grounded in the cited documentation. Output quality and compatibility are not hands-on verified. [Source 1](https://github.com/luiscarbonel1991/kiln/blob/main/README.md) [Source 2](https://github.com/luiscarbonel1991/kiln/blob/main/docker-compose.yml)

### Limitations

Replace inaccurate model-generated lettering or scale with reviewed artwork. Packaging lists and proof images are distinct from physical production files. [Source 1](https://github.com/luiscarbonel1991/kiln/blob/main/README.md) [Source 2](https://github.com/luiscarbonel1991/kiln/blob/main/docker-compose.yml)

### Get the tool

- [Repository](https://github.com/luiscarbonel1991/kiln)
- [Documentation](https://github.com/luiscarbonel1991/kiln/blob/main/docker-compose.yml)

## Frame AI

Photography, restoration & color · AI color direction and palette-based media · Images & design

The source repository was created on 2026-11-12. This is its first complete guide in the library.

### Quality assessment: Quality unverified

Creative use and the code grant are documented. Check-level gaps remain before a recommendation.

Scope: Compare provider-assisted tonal edits for a photo and approve one reversible change while preserving its original and recipe history.

Evidence checked: 2026-11-21. No local execution implied.

- **Open-source software license · verified:** Reviewed the complete project software grant and its redistribution conditions. Model, data and service terms are scoped separately. [Source](https://github.com/chillBnetley/frame-ai/blob/master/LICENSE)
- **Creative results · documented:** The project illustrates a photo workbench and explicit proposal acceptance. Its offline mock provider is useful for exploring the editor and does not establish live-model results. [Source](https://github.com/chillBnetley/frame-ai/blob/master/README.md) [Source](https://github.com/chillBnetley/frame-ai/blob/master/package.json)
- **Reproducible setup · documented:** The installation and first-use steps are in the cited documentation. Reproduction of this workflow remains unverified. [Source](https://github.com/chillBnetley/frame-ai/blob/master/README.md) [Source](https://github.com/chillBnetley/frame-ai/blob/master/package.json)
- **Maintenance and support · unknown:** The reviewed sources do not establish workflow-specific support, fixes and unresolved blockers.
- **Independent use · unknown:** Independent first-hand use of the exact workflow was not established in this source review.
- **Models, services and costs · documented:** MIT applies to the application. A remote provider receives relevant material for AI operations and has its own terms. Offline mock and manual editing use local compute. Real model requests, result variations and image storage can have costs. [Source](https://github.com/chillBnetley/frame-ai/blob/master/README.md) [Source](https://github.com/chillBnetley/frame-ai/blob/master/package.json)

Source and documentation review. No hands-on execution by AI Media Scout. Model availability and support vary. Treat natural-language grading and proposed generated changes as drafts until compared with the source.

### How it uses AI

Frame AI uses configured image-model providers for analysis and grading suggestions within an editable photo project. It offers staged changes for crop extension and selected-region generation. [Source](https://github.com/chillBnetley/frame-ai/blob/master/README.md) [Source](https://github.com/chillBnetley/frame-ai/blob/master/package.json)

### Introduction

Frame AI uses configured image-model providers for analysis and grading suggestions within an editable photo project. It offers staged changes for crop extension and selected-region generation. [Source 1](https://github.com/chillBnetley/frame-ai/blob/master/README.md) [Source 2](https://github.com/chillBnetley/frame-ai/blob/master/package.json)

### What it is good for

Compare provider-assisted tonal edits for a photo and approve one reversible change while preserving its original and recipe history. [Source 1](https://github.com/chillBnetley/frame-ai/blob/master/README.md) [Source 2](https://github.com/chillBnetley/frame-ai/blob/master/package.json)

### Demo & examples

The project illustrates a photo workbench and explicit proposal acceptance. Its offline mock provider is useful for exploring the editor and does not establish live-model results. [Source 1](https://github.com/chillBnetley/frame-ai/blob/master/README.md) [Source 2](https://github.com/chillBnetley/frame-ai/blob/master/package.json)

### Install

Follow the documented route for the scoped workflow. The steps below are source references. [Source 1](https://github.com/chillBnetley/frame-ai/blob/master/README.md) [Source 2](https://github.com/chillBnetley/frame-ai/blob/master/package.json)

1. Prepare the documented Node.js and Python versions, backend and local Web frontend. Review the Windows package separately if using a released desktop build.
2. Open a small mock session before choosing a supported image-capable provider. Check whether uploading the test photo is permitted.
### First project

A small first project makes the input, model output and handoff easy to inspect. [Source 1](https://github.com/chillBnetley/frame-ai/blob/master/README.md) [Source 2](https://github.com/chillBnetley/frame-ai/blob/master/package.json)

1. Import a rights-cleared photo and establish a neutral development. Request a bounded improvement with clear constraints.
2. Compare the proposed edit at several scales and check the recipe before approval. Save a separate proof and keep the original.
3. For generative expansion, inspect seams or altered detail and record the selected provider and output.
### Hardware & software

Platform and compute constraints refer to the selected route. [Source 1](https://github.com/chillBnetley/frame-ai/blob/master/README.md) [Source 2](https://github.com/chillBnetley/frame-ai/blob/master/package.json)

- **Hardware:** Minimum RAM, VRAM and disk space for the scoped workflow are undocumented.
- **Software:** The setup lists Node.js 24.19, Python 3.14.7 with code compatibility from 3.11, a Next.js frontend and FastAPI backend. Live inference needs a compatible provider.
- **Platforms:** The author lists Windows, macOS and Linux for source setup. The release assets and their OS are a separate check.

### License, model weights & costs

The full software license was reviewed. Dependencies and creative assets carry their own terms. [Source 1](https://github.com/chillBnetley/frame-ai/blob/master/LICENSE) [Source 2](https://github.com/chillBnetley/frame-ai/blob/master/README.md) [Source 3](https://github.com/chillBnetley/frame-ai/blob/master/package.json)

- **Code:** MIT
- **Weights:** MIT applies to the application. A remote provider receives relevant material for AI operations and has its own terms.
- **Commercial:** Project code is governed by MIT. Confirm selected model, source-media and output restrictions separately.
- **Cost:** Offline mock and manual editing use local compute. Real model requests, result variations and image storage can have costs.

### Why it merits attention

The creative workflow is grounded in the cited documentation. Output quality and compatibility are not hands-on verified. [Source 1](https://github.com/chillBnetley/frame-ai/blob/master/README.md) [Source 2](https://github.com/chillBnetley/frame-ai/blob/master/package.json)

### Limitations

Model availability and support vary. Treat natural-language grading and proposed generated changes as drafts until compared with the source. [Source 1](https://github.com/chillBnetley/frame-ai/blob/master/README.md) [Source 2](https://github.com/chillBnetley/frame-ai/blob/master/package.json)

### Get the tool

- [Repository](https://github.com/chillBnetley/frame-ai)
- [Documentation](https://github.com/chillBnetley/frame-ai/blob/master/package.json)

## Kotonoha

Creative learning & authoring · Accessible media & assistive creation · Browser tools & web media

The source repository was created on 2026-11-05. This is its first complete guide in the library.

### Quality assessment: Quality unverified

Creative use and the code grant are documented. Check-level gaps remain before a recommendation.

Scope: Create synchronized annotated reading material from a cleared short video or scan and turn selected phrases into study cards.

Evidence checked: 2026-11-21. No local execution implied.

- **Open-source software license · verified:** Reviewed the complete project software grant and its redistribution conditions. Model, data and service terms are scoped separately. [Source](https://github.com/Eliam4510/kotonoha/blob/main/LICENSE)
- **Creative results · documented:** The project shows per-word captions and OCR for rasterized pages. It distinguishes local dictionaries and transcription from optional Claude explanations. [Source](https://github.com/Eliam4510/kotonoha/blob/main/README.md) [Source](https://github.com/Eliam4510/kotonoha/blob/main/README.en.md) [Source](https://github.com/Eliam4510/kotonoha/blob/main/AVISOS.md) [Source](https://github.com/Eliam4510/kotonoha/blob/main/CHANGELOG.md)
- **Reproducible setup · documented:** The installation and first-use steps are in the cited documentation. Reproduction of this workflow remains unverified. [Source](https://github.com/Eliam4510/kotonoha/blob/main/README.md) [Source](https://github.com/Eliam4510/kotonoha/blob/main/README.en.md) [Source](https://github.com/Eliam4510/kotonoha/blob/main/AVISOS.md) [Source](https://github.com/Eliam4510/kotonoha/blob/main/CHANGELOG.md)
- **Maintenance and support · documented:** Release v0.41.0 and the changelog document the current extension route. Workflow reproduction for every language and host remains open. [Source](https://github.com/Eliam4510/kotonoha/releases/tag/v0.41.0)
- **Independent use · unknown:** Independent first-hand use of the exact workflow was not established in this source review.
- **Models, services and costs · documented:** MIT covers project code. Speech models, language corpora, book images and model providers retain separate terms. Use rights-cleared source material. Local model and dictionary downloads consume storage and compute. Claude or other explanations may use metered provider access. [Source](https://github.com/Eliam4510/kotonoha/blob/main/README.md) [Source](https://github.com/Eliam4510/kotonoha/blob/main/README.en.md) [Source](https://github.com/Eliam4510/kotonoha/blob/main/AVISOS.md) [Source](https://github.com/Eliam4510/kotonoha/blob/main/CHANGELOG.md)

Source and documentation review. No hands-on execution by AI Media Scout. Model and GPU availability affect transcription/OCR. Subtitle timing, readings and specialized vocabulary still need language review.

### How it uses AI

Kotonoha runs speech transcription and scanned-page text recognition within a Chromium extension. It adds selectable word explanations and caption overlays for language-learning media. [Source](https://github.com/Eliam4510/kotonoha/blob/main/README.md) [Source](https://github.com/Eliam4510/kotonoha/blob/main/README.en.md) [Source](https://github.com/Eliam4510/kotonoha/blob/main/AVISOS.md) [Source](https://github.com/Eliam4510/kotonoha/blob/main/CHANGELOG.md)

### Introduction

Kotonoha runs speech transcription and scanned-page text recognition within a Chromium extension. It adds selectable word explanations and caption overlays for language-learning media. [Source 1](https://github.com/Eliam4510/kotonoha/blob/main/README.md) [Source 2](https://github.com/Eliam4510/kotonoha/blob/main/README.en.md) [Source 3](https://github.com/Eliam4510/kotonoha/blob/main/AVISOS.md) [Source 4](https://github.com/Eliam4510/kotonoha/blob/main/CHANGELOG.md)

### What it is good for

Create synchronized annotated reading material from a cleared short video or scan and turn selected phrases into study cards. [Source 1](https://github.com/Eliam4510/kotonoha/blob/main/README.md) [Source 2](https://github.com/Eliam4510/kotonoha/blob/main/README.en.md) [Source 3](https://github.com/Eliam4510/kotonoha/blob/main/AVISOS.md) [Source 4](https://github.com/Eliam4510/kotonoha/blob/main/CHANGELOG.md)

### Demo & examples

The project shows per-word captions and OCR for rasterized pages. It distinguishes local dictionaries and transcription from optional Claude explanations. [Source 1](https://github.com/Eliam4510/kotonoha/blob/main/README.md) [Source 2](https://github.com/Eliam4510/kotonoha/blob/main/README.en.md) [Source 3](https://github.com/Eliam4510/kotonoha/blob/main/AVISOS.md) [Source 4](https://github.com/Eliam4510/kotonoha/blob/main/CHANGELOG.md)

### Install

Follow the documented route for the scoped workflow. The steps below are source references. [Source 1](https://github.com/Eliam4510/kotonoha/blob/main/README.md) [Source 2](https://github.com/Eliam4510/kotonoha/blob/main/README.en.md) [Source 3](https://github.com/Eliam4510/kotonoha/blob/main/AVISOS.md) [Source 4](https://github.com/Eliam4510/kotonoha/blob/main/CHANGELOG.md)

1. Use the versioned extension package and the project’s documented Chrome or Edge 120+ loading route.
2. Select the study language and the exact speech/OCR models. Start with the offline route and add a provider only for a needed feature.
### First project

A small first project makes the input, model output and handoff easy to inspect. [Source 1](https://github.com/Eliam4510/kotonoha/blob/main/README.md) [Source 2](https://github.com/Eliam4510/kotonoha/blob/main/README.en.md) [Source 3](https://github.com/Eliam4510/kotonoha/blob/main/AVISOS.md) [Source 4](https://github.com/Eliam4510/kotonoha/blob/main/CHANGELOG.md)

1. Test a short local input and compare OCR or transcribed subtitles with printed text or speech.
2. Inspect word segmentation, reading and timing. Correct what is needed before using chosen phrases in a deck.
3. Keep the original media and cleaned learning data. Review what excerpts leave the browser if enabling an optional provider.
### Hardware & software

Platform and compute constraints refer to the selected route. [Source 1](https://github.com/Eliam4510/kotonoha/blob/main/README.md) [Source 2](https://github.com/Eliam4510/kotonoha/blob/main/README.en.md) [Source 3](https://github.com/Eliam4510/kotonoha/blob/main/AVISOS.md) [Source 4](https://github.com/Eliam4510/kotonoha/blob/main/CHANGELOG.md)

- **Hardware:** Minimum RAM, VRAM and disk space for the scoped workflow are undocumented.
- **Software:** Chrome/Edge 120+, Manifest V3 extension, selected language dictionaries and local WebGPU speech/OCR models. Optional online explanation is separate.
- **Platforms:** Desktop Chrome and Edge are documented. The Windows helper is optional. Native mobile support is undocumented.

### License, model weights & costs

The full software license was reviewed. Dependencies and creative assets carry their own terms. [Source 1](https://github.com/Eliam4510/kotonoha/blob/main/LICENSE) [Source 2](https://github.com/Eliam4510/kotonoha/blob/main/README.md) [Source 3](https://github.com/Eliam4510/kotonoha/blob/main/README.en.md) [Source 4](https://github.com/Eliam4510/kotonoha/blob/main/AVISOS.md) [Source 5](https://github.com/Eliam4510/kotonoha/blob/main/CHANGELOG.md)

- **Code:** MIT
- **Weights:** MIT covers project code. Speech models, language corpora, book images and model providers retain separate terms. Use rights-cleared source material.
- **Commercial:** Project code is governed by MIT. Confirm selected model, source-media and output restrictions separately.
- **Cost:** Local model and dictionary downloads consume storage and compute. Claude or other explanations may use metered provider access.

### Why it merits attention

The creative workflow is grounded in the cited documentation. Output quality and compatibility are not hands-on verified. [Source 1](https://github.com/Eliam4510/kotonoha/blob/main/README.md) [Source 2](https://github.com/Eliam4510/kotonoha/blob/main/README.en.md) [Source 3](https://github.com/Eliam4510/kotonoha/blob/main/AVISOS.md) [Source 4](https://github.com/Eliam4510/kotonoha/blob/main/CHANGELOG.md)

### Limitations

Model and GPU availability affect transcription/OCR. Subtitle timing, readings and specialized vocabulary still need language review. [Source 1](https://github.com/Eliam4510/kotonoha/blob/main/README.md) [Source 2](https://github.com/Eliam4510/kotonoha/blob/main/README.en.md) [Source 3](https://github.com/Eliam4510/kotonoha/blob/main/AVISOS.md) [Source 4](https://github.com/Eliam4510/kotonoha/blob/main/CHANGELOG.md)

### Get the tool

- [Repository](https://github.com/Eliam4510/kotonoha)
- [Documentation](https://github.com/Eliam4510/kotonoha/blob/main/CHANGELOG.md)

## BakeDown

3D, reconstruction & assets · Games & production pipelines · Computational art & creative coding

This completes an earlier pending guide with a current source review.

### Quality assessment: Quality unverified

Creative use and the code grant are documented. Check-level gaps remain before a recommendation.

Scope: Ask an agent to prepare one generated prop for an explicit triangle budget, then inspect the manually editable result and bake outputs in Blender.

Evidence checked: 2026-11-21. No local execution implied.

- **Open-source software license · verified:** Reviewed the complete project software grant and its redistribution conditions. Model, data and service terms are scoped separately. [Source](https://github.com/keeraa/bakedown/blob/main/LICENSE)
- **Creative results · documented:** The maintainer publishes examples and an agent-facing JSON report. Its numerical before/after claims describe examples. [Source](https://github.com/keeraa/bakedown/blob/main/README.md)
- **Reproducible setup · documented:** The installation and first-use steps are in the cited documentation. Reproduction of this workflow remains unverified. [Source](https://github.com/keeraa/bakedown/blob/main/README.md)
- **Maintenance and support · documented:** Version 1.6.0 and a documented agent-facing workflow were reviewed. Engine-version compatibility and outputs require reproduction. [Source](https://github.com/keeraa/bakedown/releases/tag/v1.6.0)
- **Independent use · unknown:** Independent first-hand use of the exact workflow was not established in this source review.
- **Models, services and costs · documented:** BakeDown code is GPL-3.0-or-later in the README. Blender, external model generation and imported assets retain separate terms. Mesh work and baking require local compute. Any upstream model generation or connected agent can add independent costs. [Source](https://github.com/keeraa/bakedown/blob/main/README.md)

Source and documentation review. No hands-on execution by AI Media Scout. A lower triangle count does not guarantee good deformations or a correct normal map. Compare over the intended camera range and inspect the actual engine export.

### How it uses AI

BakeDown gives a connected AI agent a constrained Blender command-line and Python interface for inspecting and optimizing generated or scanned meshes. It returns a structured report for the agent and creator to inspect. [Source](https://github.com/keeraa/bakedown/blob/main/README.md)

### Introduction

BakeDown gives a connected AI agent a constrained Blender command-line and Python interface for inspecting and optimizing generated or scanned meshes. It returns a structured report for the agent and creator to inspect. [Source 1](https://github.com/keeraa/bakedown/blob/main/README.md)

### What it is good for

Ask an agent to prepare one generated prop for an explicit triangle budget, then inspect the manually editable result and bake outputs in Blender. [Source 1](https://github.com/keeraa/bakedown/blob/main/README.md)

### Demo & examples

The maintainer publishes examples and an agent-facing JSON report. Its numerical before/after claims describe examples. [Source 1](https://github.com/keeraa/bakedown/blob/main/README.md)

### Install

Follow the documented route for the scoped workflow. The steps below are source references. [Source 1](https://github.com/keeraa/bakedown/blob/main/README.md)

1. Use the official release’s Blender add-on file and the documented Blender Add-ons installation. Review the chosen build and upstream Blender prerequisites.
2. For the agent path use the documented CLI or Python interface, which can run within Blender. Keep an original copy of the model.
### First project

A small first project makes the input, model output and handoff easy to inspect. [Source 1](https://github.com/keeraa/bakedown/blob/main/README.md)

1. Import a representative prop. Specify target triangle count, texture size and intended engine.
2. Inspect the simplified geometry and baked maps against the original. Compare its reported distortion and missing materials before export.
3. Check scale, rigged parts and renderer import in the actual target environment.
### Hardware & software

Platform and compute constraints refer to the selected route. [Source 1](https://github.com/keeraa/bakedown/blob/main/README.md)

- **Hardware:** Minimum RAM, VRAM and disk space for the scoped workflow are undocumented.
- **Software:** Blender and the v1.6.0 BakeDown add-on. The optional agent route needs its own model/client or MCP host.
- **Platforms:** The reviewed docs use Blender. The exact compatible Blender/platform combination and headless execution should be verified on the intended system.

### License, model weights & costs

The full software license was reviewed. Dependencies and creative assets carry their own terms. [Source 1](https://github.com/keeraa/bakedown/blob/main/LICENSE) [Source 2](https://github.com/keeraa/bakedown/blob/main/README.md)

- **Code:** GPL-3.0-or-later
- **Weights:** BakeDown code is GPL-3.0-or-later in the README. Blender, external model generation and imported assets retain separate terms.
- **Commercial:** Project code is governed by GPL-3.0-or-later. Confirm selected model, source-media and output restrictions separately.
- **Cost:** Mesh work and baking require local compute. Any upstream model generation or connected agent can add independent costs.

### Why it merits attention

The creative workflow is grounded in the cited documentation. Output quality and compatibility are not hands-on verified. [Source 1](https://github.com/keeraa/bakedown/blob/main/README.md)

### Limitations

A lower triangle count does not guarantee good deformations or a correct normal map. Compare over the intended camera range and inspect the actual engine export. [Source 1](https://github.com/keeraa/bakedown/blob/main/README.md)

### Get the tool

- [Repository](https://github.com/keeraa/bakedown)
- [Documentation](https://github.com/keeraa/bakedown/blob/main/README.md)

## Motion Director

AI kinetic typography and animated lettering · Editing, captions & post-production · Computational art & creative coding

First complete guide in the library. The publication and documentation dates are not necessarily the project’s launch date.

### Quality assessment: Quality unverified

Creative use and the code grant are documented. Check-level gaps remain before a recommendation.

Scope: Make a short kinetic title for a clip and review the exact composition, timings and captured frames before export.

Evidence checked: 2026-11-21. No local execution implied.

- **Open-source software license · verified:** Reviewed the complete project software grant and its redistribution conditions. Model, data and service terms are scoped separately. [Source](https://github.com/ZZombie04/motion/blob/main/LICENSE)
- **Creative results · documented:** The repository documents preview, check, score, contact sheet and render commands. Its internal score does not independently measure creative quality. [Source](https://github.com/ZZombie04/motion/blob/main/README.md)
- **Reproducible setup · documented:** The installation and first-use steps are in the cited documentation. Reproduction of this workflow remains unverified. [Source](https://github.com/ZZombie04/motion/blob/main/README.md)
- **Maintenance and support · documented:** The v2.0.0 release was reviewed along with the command reference. Reproduction on different render backends remains open. [Source](https://github.com/ZZombie04/motion/releases/tag/v2.0.0)
- **Independent use · unknown:** Independent first-hand use of the exact workflow was not established in this source review.
- **Models, services and costs · documented:** The project code is MIT. Review fonts, sample graphics, music, input assets and model providers separately. Local rendering consumes compute. An external agent or voice workflow can require separate account/service access. [Source](https://github.com/ZZombie04/motion/blob/main/README.md)

Source and documentation review. No hands-on execution by AI Media Scout. Rendered timing depends on the browser/FFmpeg route. A versioned HTML draft, contact sheet and result should be independently reviewed.

### How it uses AI

Motion Director uses a connected coding agent and a structured engine to draft editable HTML motion graphics. It provides frame checks and contact sheets for refining the result. [Source](https://github.com/ZZombie04/motion/blob/main/README.md)

### Introduction

Motion Director uses a connected coding agent and a structured engine to draft editable HTML motion graphics. It provides frame checks and contact sheets for refining the result. [Source 1](https://github.com/ZZombie04/motion/blob/main/README.md)

### What it is good for

Make a short kinetic title for a clip and review the exact composition, timings and captured frames before export. [Source 1](https://github.com/ZZombie04/motion/blob/main/README.md)

### Demo & examples

The repository documents preview, check, score, contact sheet and render commands. Its internal score does not independently measure creative quality. [Source 1](https://github.com/ZZombie04/motion/blob/main/README.md)

### Install

Follow the documented route for the scoped workflow. The steps below are source references. [Source 1](https://github.com/ZZombie04/motion/blob/main/README.md)

1. Prepare Node.js 18+, Chrome or Edge and FFmpeg on the rendering computer. Install the repository’s documented dependencies.
2. Connect the agent only if using its MCP or skill path. Use its doctor command to identify required runtime resources.

```sh
npm install
```


```sh
node bin/motion.mjs doctor
```

### First project

A small first project makes the input, model output and handoff easy to inspect. [Source 1](https://github.com/ZZombie04/motion/blob/main/README.md)

1. Create a short composition from one template. Have the agent draft one motion or layout, then inspect the HTML and variables.
2. Preview the design, make a contact sheet and revise any clipped type or timing. Export a draft and check playback with audio.
### Hardware & software

Platform and compute constraints refer to the selected route. [Source 1](https://github.com/ZZombie04/motion/blob/main/README.md)

- **Hardware:** Minimum RAM, VRAM and disk space for the scoped workflow are undocumented.
- **Software:** Node.js 18+, compatible Chromium browser, FFmpeg and the source checkout. An authorized Claude, Codex or other agent route is optional.
- **Platforms:** Use an OS supported by the browser and FFmpeg path. Exact native package requirements and platform benchmarks are undocumented.

### License, model weights & costs

The full software license was reviewed. Dependencies and creative assets carry their own terms. [Source 1](https://github.com/ZZombie04/motion/blob/main/LICENSE) [Source 2](https://github.com/ZZombie04/motion/blob/main/README.md)

- **Code:** MIT
- **Weights:** The project code is MIT. Review fonts, sample graphics, music, input assets and model providers separately.
- **Commercial:** Project code is governed by MIT. Confirm selected model, source-media and output restrictions separately.
- **Cost:** Local rendering consumes compute. An external agent or voice workflow can require separate account/service access.

### Why it merits attention

The creative workflow is grounded in the cited documentation. Output quality and compatibility are not hands-on verified. [Source 1](https://github.com/ZZombie04/motion/blob/main/README.md)

### Limitations

Rendered timing depends on the browser/FFmpeg route. A versioned HTML draft, contact sheet and result should be independently reviewed. [Source 1](https://github.com/ZZombie04/motion/blob/main/README.md)

### Get the tool

- [Repository](https://github.com/ZZombie04/motion)
- [Documentation](https://github.com/ZZombie04/motion/blob/main/README.md)

## Deckline

Creative publishing & presentation · Storyboarding, narrative & comics · AI agents for code-authored media production

This completes an earlier pending guide with a current source review.

### Quality assessment: Quality unverified

Creative use and the code grant are documented. Check-level gaps remain before a recommendation.

Scope: Produce a first visual pitch deck with versioned page images, then revise selected pages without discarding earlier outputs.

Evidence checked: 2026-11-21. No local execution implied.

- **Open-source software license · verified:** Reviewed the complete project software grant and its redistribution conditions. Model, data and service terms are scoped separately. [Source](https://github.com/yuna78/dsh-deck-studio/blob/main/LICENSE)
- **Creative results · documented:** The bilingual docs show the workspace, slide edits and full-screen presentation. Separate editing of individual text/graphics in a downstream presentation remains to be verified. [Source](https://github.com/yuna78/dsh-deck-studio/blob/main/README.md) [Source](https://github.com/yuna78/dsh-deck-studio/blob/main/docs/install.md) [Source](https://github.com/yuna78/dsh-deck-studio/blob/main/README.en.md)
- **Reproducible setup · documented:** The installation and first-use steps are in the cited documentation. Reproduction of this workflow remains unverified. [Source](https://github.com/yuna78/dsh-deck-studio/blob/main/README.md) [Source](https://github.com/yuna78/dsh-deck-studio/blob/main/docs/install.md) [Source](https://github.com/yuna78/dsh-deck-studio/blob/main/README.en.md)
- **Maintenance and support · unknown:** The reviewed sources do not establish workflow-specific support, fixes and unresolved blockers.
- **Independent use · unknown:** Independent first-hand use of the exact workflow was not established in this source review.
- **Models, services and costs · documented:** MIT covers Deckline code. The host, exact image provider/model, user references and slide outputs carry separate terms. Local project storage is separate from image generation. Selected image providers may require accounts or incur charges. [Source](https://github.com/yuna78/dsh-deck-studio/blob/main/README.md) [Source](https://github.com/yuna78/dsh-deck-studio/blob/main/docs/install.md) [Source](https://github.com/yuna78/dsh-deck-studio/blob/main/README.en.md)

Source and documentation review. No hands-on execution by AI Media Scout. Image-based slide generation makes text and layout review essential. Preserve prompts and image versions before sharing or exporting.

### How it uses AI

Deckline calls a configured image generator inside DeepSeek Harness to produce draft slide images one page at a time while retaining prompts, edit events and version history. [Source](https://github.com/yuna78/dsh-deck-studio/blob/main/README.md) [Source](https://github.com/yuna78/dsh-deck-studio/blob/main/docs/install.md) [Source](https://github.com/yuna78/dsh-deck-studio/blob/main/README.en.md)

### Introduction

Deckline calls a configured image generator inside DeepSeek Harness to produce draft slide images one page at a time while retaining prompts, edit events and version history. [Source 1](https://github.com/yuna78/dsh-deck-studio/blob/main/README.md) [Source 2](https://github.com/yuna78/dsh-deck-studio/blob/main/docs/install.md) [Source 3](https://github.com/yuna78/dsh-deck-studio/blob/main/README.en.md)

### What it is good for

Produce a first visual pitch deck with versioned page images, then revise selected pages without discarding earlier outputs. [Source 1](https://github.com/yuna78/dsh-deck-studio/blob/main/README.md) [Source 2](https://github.com/yuna78/dsh-deck-studio/blob/main/docs/install.md) [Source 3](https://github.com/yuna78/dsh-deck-studio/blob/main/README.en.md)

### Demo & examples

The bilingual docs show the workspace, slide edits and full-screen presentation. Separate editing of individual text/graphics in a downstream presentation remains to be verified. [Source 1](https://github.com/yuna78/dsh-deck-studio/blob/main/README.md) [Source 2](https://github.com/yuna78/dsh-deck-studio/blob/main/docs/install.md) [Source 3](https://github.com/yuna78/dsh-deck-studio/blob/main/README.en.md)

### Install

Follow the documented route for the scoped workflow. The steps below are source references. [Source 1](https://github.com/yuna78/dsh-deck-studio/blob/main/README.md) [Source 2](https://github.com/yuna78/dsh-deck-studio/blob/main/docs/install.md) [Source 3](https://github.com/yuna78/dsh-deck-studio/blob/main/README.en.md)

1. Use the project’s DSH profile configuration and install the documented package into that separate profile.
2. Restart the host and select a permitted image endpoint and model. Start with a temporary two-slide project.

```sh
dsh plugin --profile deckline add dsh-plugin-deck-studio
```

### First project

A small first project makes the input, model output and handoff easy to inspect. [Source 1](https://github.com/yuna78/dsh-deck-studio/blob/main/README.md) [Source 2](https://github.com/yuna78/dsh-deck-studio/blob/main/docs/install.md) [Source 3](https://github.com/yuna78/dsh-deck-studio/blob/main/README.en.md)

1. Define audience, sequence and a slide brief. Generate one slide image and inspect text accuracy and visual hierarchy.
2. Revise a single page with its own version, then preview the deck. Confirm exactly what remains editable in the expected export.
### Hardware & software

Platform and compute constraints refer to the selected route. [Source 1](https://github.com/yuna78/dsh-deck-studio/blob/main/README.md) [Source 2](https://github.com/yuna78/dsh-deck-studio/blob/main/docs/install.md) [Source 3](https://github.com/yuna78/dsh-deck-studio/blob/main/README.en.md)

- **Hardware:** Minimum RAM, VRAM and disk space for the scoped workflow are undocumented.
- **Software:** DeepSeek Harness with the Deckline plugin and configured image service or backend. The current setup docs describe profile and data-root separation.
- **Platforms:** The project documents the plugin-host route. Do not infer native desktop or mobile support from its visual workspace.

### License, model weights & costs

The full software license was reviewed. Dependencies and creative assets carry their own terms. [Source 1](https://github.com/yuna78/dsh-deck-studio/blob/main/LICENSE) [Source 2](https://github.com/yuna78/dsh-deck-studio/blob/main/README.md) [Source 3](https://github.com/yuna78/dsh-deck-studio/blob/main/docs/install.md) [Source 4](https://github.com/yuna78/dsh-deck-studio/blob/main/README.en.md)

- **Code:** MIT
- **Weights:** MIT covers Deckline code. The host, exact image provider/model, user references and slide outputs carry separate terms.
- **Commercial:** Project code is governed by MIT. Confirm selected model, source-media and output restrictions separately.
- **Cost:** Local project storage is separate from image generation. Selected image providers may require accounts or incur charges.

### Why it merits attention

The creative workflow is grounded in the cited documentation. Output quality and compatibility are not hands-on verified. [Source 1](https://github.com/yuna78/dsh-deck-studio/blob/main/README.md) [Source 2](https://github.com/yuna78/dsh-deck-studio/blob/main/docs/install.md) [Source 3](https://github.com/yuna78/dsh-deck-studio/blob/main/README.en.md)

### Limitations

Image-based slide generation makes text and layout review essential. Preserve prompts and image versions before sharing or exporting. [Source 1](https://github.com/yuna78/dsh-deck-studio/blob/main/README.md) [Source 2](https://github.com/yuna78/dsh-deck-studio/blob/main/docs/install.md) [Source 3](https://github.com/yuna78/dsh-deck-studio/blob/main/README.en.md)

### Get the tool

- [Repository](https://github.com/yuna78/dsh-deck-studio)
- [Documentation](https://github.com/yuna78/dsh-deck-studio/blob/main/README.en.md)

## StoryCore Engine

Storyboarding, narrative & comics · Video, animation & film · AI agents for code-authored media production

First complete guide in the library. The publication and documentation dates are not necessarily the project’s launch date.

### Quality assessment: Quality unverified

Creative use and the code grant are documented. Check-level gaps remain before a recommendation.

Scope: Prepare a small short-film scene and record the model and asset choices before generating a quality-control preview.

Evidence checked: 2026-11-21. No local execution implied.

- **Open-source software license · verified:** Reviewed the complete project software grant and its redistribution conditions. Model, data and service terms are scoped separately. [Source](https://github.com/zedarvates/StoryCore-Engine/blob/main/LICENSE)
- **Creative results · documented:** The current README documents an end-to-end demo command with a mock mode. A mock workflow validates orchestration only. Result quality with actual model output remains open. [Source](https://github.com/zedarvates/StoryCore-Engine/blob/main/README.md) [Source](https://github.com/zedarvates/StoryCore-Engine/blob/main/docs/MULTI_NODE_SETUP.md)
- **Reproducible setup · documented:** The installation and first-use steps are in the cited documentation. Reproduction of this workflow remains unverified. [Source](https://github.com/zedarvates/StoryCore-Engine/blob/main/README.md) [Source](https://github.com/zedarvates/StoryCore-Engine/blob/main/docs/MULTI_NODE_SETUP.md)
- **Maintenance and support · unknown:** The reviewed sources do not establish workflow-specific support, fixes and unresolved blockers.
- **Independent use · unknown:** Independent first-hand use of the exact workflow was not established in this source review.
- **Models, services and costs · documented:** MIT applies to StoryCore source. Individual model, plugin, footage and dataset rights remain separate. Local or multi-node compute, storage and model downloads apply. Optional provider calls have their own terms. [Source](https://github.com/zedarvates/StoryCore-Engine/blob/main/README.md) [Source](https://github.com/zedarvates/StoryCore-Engine/blob/main/docs/MULTI_NODE_SETUP.md)

Source and documentation review. No hands-on execution by AI Media Scout. A mock run and production inference have separate evidence. Confirm memory allocation, the actual selected model and the rendered handoff on a small scene.

### How it uses AI

StoryCore orchestrates scripts, scene assets and video rendering through an editable project, linking local model and ComfyUI routes with distinct workflow components. [Source](https://github.com/zedarvates/StoryCore-Engine/blob/main/README.md) [Source](https://github.com/zedarvates/StoryCore-Engine/blob/main/docs/MULTI_NODE_SETUP.md)

### Introduction

StoryCore orchestrates scripts, scene assets and video rendering through an editable project, linking local model and ComfyUI routes with distinct workflow components. [Source 1](https://github.com/zedarvates/StoryCore-Engine/blob/main/README.md) [Source 2](https://github.com/zedarvates/StoryCore-Engine/blob/main/docs/MULTI_NODE_SETUP.md)

### What it is good for

Prepare a small short-film scene and record the model and asset choices before generating a quality-control preview. [Source 1](https://github.com/zedarvates/StoryCore-Engine/blob/main/README.md) [Source 2](https://github.com/zedarvates/StoryCore-Engine/blob/main/docs/MULTI_NODE_SETUP.md)

### Demo & examples

The current README documents an end-to-end demo command with a mock mode. A mock workflow validates orchestration only. Result quality with actual model output remains open. [Source 1](https://github.com/zedarvates/StoryCore-Engine/blob/main/README.md) [Source 2](https://github.com/zedarvates/StoryCore-Engine/blob/main/docs/MULTI_NODE_SETUP.md)

### Install

Follow the documented route for the scoped workflow. The steps below are source references. [Source 1](https://github.com/zedarvates/StoryCore-Engine/blob/main/README.md) [Source 2](https://github.com/zedarvates/StoryCore-Engine/blob/main/docs/MULTI_NODE_SETUP.md)

1. Use the documented Windows or Linux source path and Python dependencies. Follow the selected frontend and local backend instructions.
2. Review the model and rendering prerequisites in the multi-node setup document. Keep any renderer confined to the intended hosts.

```sh
pip install -r requirements.txt
```

### First project

A small first project makes the input, model output and handoff easy to inspect. [Source 1](https://github.com/zedarvates/StoryCore-Engine/blob/main/README.md) [Source 2](https://github.com/zedarvates/StoryCore-Engine/blob/main/docs/MULTI_NODE_SETUP.md)

1. Start with a miniature scene and approve the storyboard and asset references.
2. Follow the mock comparison to inspect the workflow states, then choose one permitted production inference route for a small actual asset.
3. Review scene and output continuity independently before a full render. Preserve original prompts and generated variants.
### Hardware & software

Platform and compute constraints refer to the selected route. [Source 1](https://github.com/zedarvates/StoryCore-Engine/blob/main/README.md) [Source 2](https://github.com/zedarvates/StoryCore-Engine/blob/main/docs/MULTI_NODE_SETUP.md)

- **Hardware:** The README lists RTX 3060 with 12 GB VRAM, 32 GB RAM and approximately 500 GB SSD, with RTX 4090+ recommended for speed. Those requirements describe the documented setup.
- **Software:** Project Python and frontend environments, with separately configured ComfyUI and local language or graphics runtime for the chosen path.
- **Platforms:** Windows 10/11 including WSL2 and Linux are documented. A native macOS workflow is undocumented.

### License, model weights & costs

The full software license was reviewed. Dependencies and creative assets carry their own terms. [Source 1](https://github.com/zedarvates/StoryCore-Engine/blob/main/LICENSE) [Source 2](https://github.com/zedarvates/StoryCore-Engine/blob/main/README.md) [Source 3](https://github.com/zedarvates/StoryCore-Engine/blob/main/docs/MULTI_NODE_SETUP.md)

- **Code:** MIT
- **Weights:** MIT applies to StoryCore source. Individual model, plugin, footage and dataset rights remain separate.
- **Commercial:** Project code is governed by MIT. Confirm selected model, source-media and output restrictions separately.
- **Cost:** Local or multi-node compute, storage and model downloads apply. Optional provider calls have their own terms.

### Why it merits attention

The creative workflow is grounded in the cited documentation. Output quality and compatibility are not hands-on verified. [Source 1](https://github.com/zedarvates/StoryCore-Engine/blob/main/README.md) [Source 2](https://github.com/zedarvates/StoryCore-Engine/blob/main/docs/MULTI_NODE_SETUP.md)

### Limitations

A mock run and production inference have separate evidence. Confirm memory allocation, the actual selected model and the rendered handoff on a small scene. [Source 1](https://github.com/zedarvates/StoryCore-Engine/blob/main/README.md) [Source 2](https://github.com/zedarvates/StoryCore-Engine/blob/main/docs/MULTI_NODE_SETUP.md)

### Get the tool

- [Repository](https://github.com/zedarvates/StoryCore-Engine)
- [Documentation](https://github.com/zedarvates/StoryCore-Engine/blob/main/docs/MULTI_NODE_SETUP.md)

## SFX Brew

Audio, music & voice · AI Foley and sound effects · Games & production pipelines

This completes an earlier pending guide with a current source review.

### Quality assessment: Quality unverified

Creative use and the code grant are documented. Check-level gaps remain before a recommendation.

Scope: Generate reusable UI sounds or game ambience with explicit agent-selected presets, inspect them and retain the seeds.

Evidence checked: 2026-11-21. No local execution implied.

- **Open-source software license · verified:** Reviewed the complete project software grant and its redistribution conditions. Model, data and service terms are scoped separately. [Source](https://github.com/2365836149-sketch/sfxbrew/blob/main/LICENSE)
- **Creative results · documented:** The source documents preset variants, an editor and export patterns for game engines. Match the sound to the intended mix by listening. [Source](https://github.com/2365836149-sketch/sfxbrew/blob/main/README.md) [Source](https://github.com/2365836149-sketch/sfxbrew/blob/main/skills/sfxbrew/SKILL.md)
- **Reproducible setup · documented:** The installation and first-use steps are in the cited documentation. Reproduction of this workflow remains unverified. [Source](https://github.com/2365836149-sketch/sfxbrew/blob/main/README.md) [Source](https://github.com/2365836149-sketch/sfxbrew/blob/main/skills/sfxbrew/SKILL.md)
- **Maintenance and support · unknown:** The reviewed sources do not establish workflow-specific support, fixes and unresolved blockers.
- **Independent use · unknown:** Independent first-hand use of the exact workflow was not established in this source review.
- **Models, services and costs · documented:** The code uses MIT. Platform integrations and any model that drives the MCP caller have separate terms. The scoped procedural synthesis runs locally. Any external agent/model access is separate. [Source](https://github.com/2365836149-sketch/sfxbrew/blob/main/README.md) [Source](https://github.com/2365836149-sketch/sfxbrew/blob/main/skills/sfxbrew/SKILL.md)

Source and documentation review. No hands-on execution by AI Media Scout. Agent selection and procedural synthesis have different evidence. Listen for loop seams, headroom and compatibility in the actual engine.

### How it uses AI

SFX Brew provides an MCP interface so a connected agent can choose and parameterize a procedural sound and export variations. The synthesis engine itself uses seeded local sound recipes. [Source](https://github.com/2365836149-sketch/sfxbrew/blob/main/README.md) [Source](https://github.com/2365836149-sketch/sfxbrew/blob/main/skills/sfxbrew/SKILL.md)

### Introduction

SFX Brew provides an MCP interface so a connected agent can choose and parameterize a procedural sound and export variations. The synthesis engine itself uses seeded local sound recipes. [Source 1](https://github.com/2365836149-sketch/sfxbrew/blob/main/README.md) [Source 2](https://github.com/2365836149-sketch/sfxbrew/blob/main/skills/sfxbrew/SKILL.md)

### What it is good for

Generate reusable UI sounds or game ambience with explicit agent-selected presets, inspect them and retain the seeds. [Source 1](https://github.com/2365836149-sketch/sfxbrew/blob/main/README.md) [Source 2](https://github.com/2365836149-sketch/sfxbrew/blob/main/skills/sfxbrew/SKILL.md)

### Demo & examples

The source documents preset variants, an editor and export patterns for game engines. Match the sound to the intended mix by listening. [Source 1](https://github.com/2365836149-sketch/sfxbrew/blob/main/README.md) [Source 2](https://github.com/2365836149-sketch/sfxbrew/blob/main/skills/sfxbrew/SKILL.md)

### Install

Follow the documented route for the scoped workflow. The steps below are source references. [Source 1](https://github.com/2365836149-sketch/sfxbrew/blob/main/README.md) [Source 2](https://github.com/2365836149-sketch/sfxbrew/blob/main/skills/sfxbrew/SKILL.md)

1. Use the project’s window or CLI documentation. Connect the documented MCP server only for an agent-run route.
2. Verify the package or source version before making a test pack with disposable output paths.
### First project

A small first project makes the input, model output and handoff easy to inspect. [Source 1](https://github.com/2365836149-sketch/sfxbrew/blob/main/README.md) [Source 2](https://github.com/2365836149-sketch/sfxbrew/blob/main/skills/sfxbrew/SKILL.md)

1. Choose one sound family, request three variations and keep their seeds. Listen in the intended mix.
2. Export a WAV or documented JavaScript snippet. For ambient loops, check the seam and dynamics using the destination engine.
### Hardware & software

Platform and compute constraints refer to the selected route. [Source 1](https://github.com/2365836149-sketch/sfxbrew/blob/main/README.md) [Source 2](https://github.com/2365836149-sketch/sfxbrew/blob/main/skills/sfxbrew/SKILL.md)

- **Hardware:** Minimum RAM, VRAM and disk space for the scoped workflow are undocumented.
- **Software:** The documented browser or Node CLI process and optional MCP client. Game-specific exports need the selected host for testing.
- **Platforms:** Browser/CLI paths are documented. Specific OS and engine integration support needs verification.

### License, model weights & costs

The full software license was reviewed. Dependencies and creative assets carry their own terms. [Source 1](https://github.com/2365836149-sketch/sfxbrew/blob/main/LICENSE) [Source 2](https://github.com/2365836149-sketch/sfxbrew/blob/main/README.md) [Source 3](https://github.com/2365836149-sketch/sfxbrew/blob/main/skills/sfxbrew/SKILL.md)

- **Code:** MIT
- **Weights:** The code uses MIT. Platform integrations and any model that drives the MCP caller have separate terms.
- **Commercial:** Project code is governed by MIT. Confirm selected model, source-media and output restrictions separately.
- **Cost:** The scoped procedural synthesis runs locally. Any external agent/model access is separate.

### Why it merits attention

The creative workflow is grounded in the cited documentation. Output quality and compatibility are not hands-on verified. [Source 1](https://github.com/2365836149-sketch/sfxbrew/blob/main/README.md) [Source 2](https://github.com/2365836149-sketch/sfxbrew/blob/main/skills/sfxbrew/SKILL.md)

### Limitations

Agent selection and procedural synthesis have different evidence. Listen for loop seams, headroom and compatibility in the actual engine. [Source 1](https://github.com/2365836149-sketch/sfxbrew/blob/main/README.md) [Source 2](https://github.com/2365836149-sketch/sfxbrew/blob/main/skills/sfxbrew/SKILL.md)

### Get the tool

- [Repository](https://github.com/2365836149-sketch/sfxbrew)
- [Documentation](https://github.com/2365836149-sketch/sfxbrew/blob/main/skills/sfxbrew/SKILL.md)

## ComfyUI

Video, animation & film · VFX, compositing & relighting · Images & design

Version 0.46.0 adds motion-aware Video Deflicker and other video-output operations and removes DirectML after the earlier v0.44.0 guide.

### Quality assessment: Quality unverified

Creative use and the code grant are documented. Check-level gaps remain before a recommendation.

Scope: Review a short generated or edited shot for temporal flicker, then deliver a separate corrected sequence and retain the node graph.

Evidence checked: 2026-11-21. No local execution implied.

- **Open-source software license · verified:** Reviewed the complete project software grant and its redistribution conditions. Model, data and service terms are scoped separately. [Source](https://github.com/Comfy-Org/ComfyUI/blob/master/LICENSE)
- **Creative results · documented:** The maintainers publish the merged deflicker implementation and release notes. Compare a reference moving edge and the unprocessed clip before judging improvement. [Source](https://github.com/Comfy-Org/ComfyUI/blob/master/README.md) [Source](https://github.com/Comfy-Org/ComfyUI/pull/17754) [Source](https://github.com/Comfy-Org/ComfyUI/pull/17711) [Source](https://docs.comfy.org/installation/system_requirements)
- **Reproducible setup · documented:** The installation and first-use steps are in the cited documentation. Reproduction of this workflow remains unverified. [Source](https://github.com/Comfy-Org/ComfyUI/blob/master/README.md) [Source](https://github.com/Comfy-Org/ComfyUI/pull/17754) [Source](https://github.com/Comfy-Org/ComfyUI/pull/17711) [Source](https://docs.comfy.org/installation/system_requirements)
- **Maintenance and support · documented:** v0.46.0 includes the merged deflicker and frame-rate features plus an explicit backend change. Compatibility on the intended setup still requires reproduction. [Source](https://github.com/Comfy-Org/ComfyUI/releases/tag/v0.46.0)
- **Independent use · unknown:** Independent first-hand use of the exact workflow was not established in this source review.
- **Models, services and costs · documented:** GPLv3 covers the reviewed core software file. RAFT weights, other graph checkpoints, partner nodes, custom nodes and input assets have independent terms. The scoped processing is a local graph route. Model downloads and device time apply. Partner nodes or another host can incur separate costs. [Source](https://github.com/Comfy-Org/ComfyUI/blob/master/README.md) [Source](https://github.com/Comfy-Org/ComfyUI/pull/17754) [Source](https://github.com/Comfy-Org/ComfyUI/pull/17711) [Source](https://docs.comfy.org/installation/system_requirements)

Source and documentation review. No hands-on execution by AI Media Scout. The release notes confirm the implementation, with no hands-on benchmark from this review. Deflicker can alter edge behavior and must be inspected. A DirectML-dependent setup needs separate migration verification.

### How it uses AI

The v0.46.0 node graph release adds a Video Deflicker node with optical flow from RAFT, allowing motion-aware correction inside a video workflow. The release also extends video concatenation normalization and single-channel PNG output. [Source](https://github.com/Comfy-Org/ComfyUI/blob/master/README.md) [Source](https://github.com/Comfy-Org/ComfyUI/pull/17754) [Source](https://github.com/Comfy-Org/ComfyUI/pull/17711) [Source](https://docs.comfy.org/installation/system_requirements)

### Introduction

The v0.46.0 node graph release adds a Video Deflicker node with optical flow from RAFT, allowing motion-aware correction inside a video workflow. The release also extends video concatenation normalization and single-channel PNG output. [Source 1](https://github.com/Comfy-Org/ComfyUI/blob/master/README.md) [Source 2](https://github.com/Comfy-Org/ComfyUI/pull/17754) [Source 3](https://github.com/Comfy-Org/ComfyUI/pull/17711) [Source 4](https://docs.comfy.org/installation/system_requirements)

### What it is good for

Review a short generated or edited shot for temporal flicker, then deliver a separate corrected sequence and retain the node graph. [Source 1](https://github.com/Comfy-Org/ComfyUI/blob/master/README.md) [Source 2](https://github.com/Comfy-Org/ComfyUI/pull/17754) [Source 3](https://github.com/Comfy-Org/ComfyUI/pull/17711) [Source 4](https://docs.comfy.org/installation/system_requirements)

### Demo & examples

The maintainers publish the merged deflicker implementation and release notes. Compare a reference moving edge and the unprocessed clip before judging improvement. [Source 1](https://github.com/Comfy-Org/ComfyUI/blob/master/README.md) [Source 2](https://github.com/Comfy-Org/ComfyUI/pull/17754) [Source 3](https://github.com/Comfy-Org/ComfyUI/pull/17711) [Source 4](https://docs.comfy.org/installation/system_requirements)

### Install

Follow the documented route for the scoped workflow. The steps below are source references. [Source 1](https://github.com/Comfy-Org/ComfyUI/blob/master/README.md) [Source 2](https://github.com/Comfy-Org/ComfyUI/pull/17754) [Source 3](https://github.com/Comfy-Org/ComfyUI/pull/17711) [Source 4](https://docs.comfy.org/installation/system_requirements)

1. Use the documented platform package or source route for v0.46.0. Check the exact torch/backend combination before updating.
2. Find the merged Video Deflicker node in the corresponding graph workflow. Consult its configuration and verify the weight/notices before using its selected flow route.
### First project

A small first project makes the input, model output and handoff easy to inspect. [Source 1](https://github.com/Comfy-Org/ComfyUI/blob/master/README.md) [Source 2](https://github.com/Comfy-Org/ComfyUI/pull/17754) [Source 3](https://github.com/Comfy-Org/ComfyUI/pull/17711) [Source 4](https://docs.comfy.org/installation/system_requirements)

1. Load one brief clip or frame batch and retain a clean input reference.
2. Apply a conservative deflicker setting, then compare changes around motion, text and thin edges.
3. Save the graph and an independently reviewable output. Verify concatenation and frame rate separately when joining clips.
### Hardware & software

Platform and compute constraints refer to the selected route. [Source 1](https://github.com/Comfy-Org/ComfyUI/blob/master/README.md) [Source 2](https://github.com/Comfy-Org/ComfyUI/pull/17754) [Source 3](https://github.com/Comfy-Org/ComfyUI/pull/17711) [Source 4](https://docs.comfy.org/installation/system_requirements)

- **Hardware:** Minimum RAM, VRAM and disk space for the scoped workflow are undocumented.
- **Software:** ComfyUI v0.46.0. Source docs describe Python 3.13 and 3.14 compatibility with caveats for custom nodes. Selected PyTorch backend and graph/model dependencies vary.
- **Platforms:** The existing project documents Windows, Linux and macOS. The v0.46.0 release explicitly removes DirectML. Verify another supported backend for the exact device.

### License, model weights & costs

The full software license was reviewed. Dependencies and creative assets carry their own terms. [Source 1](https://github.com/Comfy-Org/ComfyUI/blob/master/LICENSE) [Source 2](https://github.com/Comfy-Org/ComfyUI/blob/master/README.md) [Source 3](https://github.com/Comfy-Org/ComfyUI/pull/17754) [Source 4](https://github.com/Comfy-Org/ComfyUI/pull/17711) [Source 5](https://docs.comfy.org/installation/system_requirements)

- **Code:** GPL-3.0
- **Weights:** GPLv3 covers the reviewed core software file. RAFT weights, other graph checkpoints, partner nodes, custom nodes and input assets have independent terms.
- **Commercial:** Project code is governed by GPL-3.0. Confirm selected model, source-media and output restrictions separately.
- **Cost:** The scoped processing is a local graph route. Model downloads and device time apply. Partner nodes or another host can incur separate costs.

### Why it merits attention

The creative workflow is grounded in the cited documentation. Output quality and compatibility are not hands-on verified. [Source 1](https://github.com/Comfy-Org/ComfyUI/blob/master/README.md) [Source 2](https://github.com/Comfy-Org/ComfyUI/pull/17754) [Source 3](https://github.com/Comfy-Org/ComfyUI/pull/17711) [Source 4](https://docs.comfy.org/installation/system_requirements)

### Limitations

The release notes confirm the implementation, with no hands-on benchmark from this review. Deflicker can alter edge behavior and must be inspected. A DirectML-dependent setup needs separate migration verification. [Source 1](https://github.com/Comfy-Org/ComfyUI/blob/master/README.md) [Source 2](https://github.com/Comfy-Org/ComfyUI/pull/17754) [Source 3](https://github.com/Comfy-Org/ComfyUI/pull/17711) [Source 4](https://docs.comfy.org/installation/system_requirements)

### Get the tool

- [Repository](https://github.com/Comfy-Org/ComfyUI)
- [Documentation](https://docs.comfy.org/installation/system_requirements)

## InvokeAI

Images & design · Vector graphics, illustration & textures · Editing, captions & post-production

InvokeAI 7 beta 2 adds canvas vector and spline editing and documents a one-way data migration after the library’s v6 baseline.

### Quality assessment: Experimental

Creative use and the code grant are documented. Check-level gaps remain before a recommendation.

Scope: Create a controlled canvas study that combines a generated plate and editable vector shapes, with the beta data isolated from an existing production edit.

Evidence checked: 2026-11-21. No local execution implied.

Why Experimental: The beta 2 release states that it is beta software with one-way database migration and asks testers to start in a separate install root. https://github.com/invoke-ai/InvokeAI/releases/tag/v7.0.0-beta.2

- **Open-source software license · verified:** Reviewed the complete project software grant and its redistribution conditions. Model, data and service terms are scoped separately. [Source](https://github.com/invoke-ai/InvokeAI/blob/main/LICENSE)
- **Creative results · documented:** The beta release describes drawing shape layers and editing Bézier handles. The notes also identify fixed generation-memory cases. These release claims need project-specific verification. [Source](https://github.com/invoke-ai/InvokeAI/blob/main/README.md) [Source](https://v7.invoke.ai/start-here/installation/) [Source](https://v7.invoke.ai/start-here/upgrading/)
- **Reproducible setup · documented:** The installation and first-use steps are in the cited documentation. Reproduction of this workflow remains unverified. [Source](https://github.com/invoke-ai/InvokeAI/blob/main/README.md) [Source](https://v7.invoke.ai/start-here/installation/) [Source](https://v7.invoke.ai/start-here/upgrading/)
- **Maintenance and support · documented:** The beta 2 release notes document specific queue, memory and canvas improvements. Stability of an existing workflow is open. [Source](https://github.com/invoke-ai/InvokeAI/releases/tag/v7.0.0-beta.2)
- **Independent use · unknown:** Independent first-hand use of the exact workflow was not established in this source review.
- **Models, services and costs · documented:** The complete Apache-2.0 software file was read. The exact image model, LoRAs, content and service terms have separate scope. This guide uses local generation and canvas editing. Actual memory requirements, model downloads and compute depend on the selected route. [Source](https://github.com/invoke-ai/InvokeAI/blob/main/README.md) [Source](https://v7.invoke.ai/start-here/installation/) [Source](https://v7.invoke.ai/start-here/upgrading/)

Source and documentation review. No hands-on execution by AI Media Scout. The release explicitly warns that v7 migrations make the old database unusable by v6 and that beta 2 data is not readable by older v7 prereleases. Use an isolated root.

### How it uses AI

InvokeAI v7 beta 2 adds editable vector shapes and spline editing inside its model-backed canvas, alongside fixes to memory reuse, model loading and queues. [Source](https://github.com/invoke-ai/InvokeAI/blob/main/README.md) [Source](https://v7.invoke.ai/start-here/installation/) [Source](https://v7.invoke.ai/start-here/upgrading/)

### Introduction

InvokeAI v7 beta 2 adds editable vector shapes and spline editing inside its model-backed canvas, alongside fixes to memory reuse, model loading and queues. [Source 1](https://github.com/invoke-ai/InvokeAI/blob/main/README.md) [Source 2](https://v7.invoke.ai/start-here/installation/) [Source 3](https://v7.invoke.ai/start-here/upgrading/)

### What it is good for

Create a controlled canvas study that combines a generated plate and editable vector shapes, with the beta data isolated from an existing production edit. [Source 1](https://github.com/invoke-ai/InvokeAI/blob/main/README.md) [Source 2](https://v7.invoke.ai/start-here/installation/) [Source 3](https://v7.invoke.ai/start-here/upgrading/)

### Demo & examples

The beta release describes drawing shape layers and editing Bézier handles. The notes also identify fixed generation-memory cases. These release claims need project-specific verification. [Source 1](https://github.com/invoke-ai/InvokeAI/blob/main/README.md) [Source 2](https://v7.invoke.ai/start-here/installation/) [Source 3](https://v7.invoke.ai/start-here/upgrading/)

### Install

Follow the documented route for the scoped workflow. The steps below are source references. [Source 1](https://github.com/invoke-ai/InvokeAI/blob/main/README.md) [Source 2](https://v7.invoke.ai/start-here/installation/) [Source 3](https://v7.invoke.ai/start-here/upgrading/)

1. Follow the v7 launcher guide and select manual version v7.0.0-beta.2 in a new empty application root.
2. Keep a copy of work before trying the beta. Observe the actual path before startup because the notes describe a one-way database migration. Confirm chosen models separately.
### First project

A small first project makes the input, model output and handoff easy to inspect. [Source 1](https://github.com/invoke-ai/InvokeAI/blob/main/README.md) [Source 2](https://v7.invoke.ai/start-here/installation/) [Source 3](https://v7.invoke.ai/start-here/upgrading/)

1. Open a new project with a permitted image or checkpoint. Make an editable vector layer and adjust a curve or shape in the canvas.
2. Review that plate and layer separately. Test a small generation and compare its queue and memory behavior before using it on a larger project.
### Hardware & software

Platform and compute constraints refer to the selected route. [Source 1](https://github.com/invoke-ai/InvokeAI/blob/main/README.md) [Source 2](https://v7.invoke.ai/start-here/installation/) [Source 3](https://v7.invoke.ai/start-here/upgrading/)

- **Hardware:** Minimum RAM, VRAM and disk space for the scoped workflow are undocumented.
- **Software:** Invoke v7.0.0-beta.2 and its documented launcher/manual installation route. Selected input models, weights and codecs are separate.
- **Platforms:** The v7 platform installation guide and the specified GPU backend determine support. Consult the guide for the selected OS and model rather than assuming old-version parity.

### License, model weights & costs

The full software license was reviewed. Dependencies and creative assets carry their own terms. [Source 1](https://github.com/invoke-ai/InvokeAI/blob/main/LICENSE) [Source 2](https://github.com/invoke-ai/InvokeAI/blob/main/README.md) [Source 3](https://v7.invoke.ai/start-here/installation/) [Source 4](https://v7.invoke.ai/start-here/upgrading/)

- **Code:** Apache-2.0
- **Weights:** The complete Apache-2.0 software file was read. The exact image model, LoRAs, content and service terms have separate scope.
- **Commercial:** Project code is governed by Apache-2.0. Confirm selected model, source-media and output restrictions separately.
- **Cost:** This guide uses local generation and canvas editing. Actual memory requirements, model downloads and compute depend on the selected route.

### Why it merits attention

The creative workflow is grounded in the cited documentation. Output quality and compatibility are not hands-on verified. [Source 1](https://github.com/invoke-ai/InvokeAI/blob/main/README.md) [Source 2](https://v7.invoke.ai/start-here/installation/) [Source 3](https://v7.invoke.ai/start-here/upgrading/)

### Limitations

The release explicitly warns that v7 migrations make the old database unusable by v6 and that beta 2 data is not readable by older v7 prereleases. Use an isolated root. [Source 1](https://github.com/invoke-ai/InvokeAI/blob/main/README.md) [Source 2](https://v7.invoke.ai/start-here/installation/) [Source 3](https://v7.invoke.ai/start-here/upgrading/)

### Get the tool

- [Repository](https://github.com/invoke-ai/InvokeAI)
- [Documentation](https://v7.invoke.ai/start-here/upgrading/)

## OpenStitch

Neural embroidery and stitch design · AI-assisted textile and computational craft · Vector graphics, illustration & textures

Alpha 18 adds the browser Assistant and changes generated stitch output. The earlier reviewed release was alpha 14.

### Quality assessment: Experimental

Creative use and the code grant are documented. Check-level gaps remain before a recommendation.

Scope: Prototype a small embroidered motif with the browser Assistant, then validate the altered stitch geometry in a separate setup.

Evidence checked: 2026-11-21. No local execution implied.

Why Experimental: The alpha 18 release calls the current version an alpha for testing and details changed stitch output in existing designs. https://github.com/cristianonescu/OpenStitch/releases/tag/v0.1.0-alpha.18

- **Open-source software license · verified:** Reviewed the complete project software grant and its redistribution conditions. Model, data and service terms are scoped separately. [Source](https://github.com/cristianonescu/OpenStitch/blob/main/LICENSE-APACHE)
- **Creative results · documented:** The release documents the browser Assistant and a set of fill, net, satin and candlewick changes. It explicitly says that stitch output differs from alpha 17. [Source](https://github.com/cristianonescu/OpenStitch/blob/main/README.md) [Source](https://cristianonescu.github.io/OpenStitch/)
- **Reproducible setup · documented:** The installation and first-use steps are in the cited documentation. Reproduction of this workflow remains unverified. [Source](https://github.com/cristianonescu/OpenStitch/blob/main/README.md) [Source](https://cristianonescu.github.io/OpenStitch/)
- **Maintenance and support · documented:** The current release shows browser Assistant and stitch-engine changes on all documented OS builds. Independent sewing results remain unverified. [Source](https://github.com/cristianonescu/OpenStitch/releases/tag/v0.1.0-alpha.18)
- **Independent use · unknown:** Independent first-hand use of the exact workflow was not established in this source review.
- **Models, services and costs · documented:** The root permissive software grant and alternate license file were reviewed. Model, font and design inputs carry separate terms. Brother interoperability does not transfer rights to assets. Local editing needs compute. The optional model and hosting path may have separate subscription or network costs. [Source](https://github.com/cristianonescu/OpenStitch/blob/main/README.md) [Source](https://cristianonescu.github.io/OpenStitch/)

Source and documentation review. No hands-on execution by AI Media Scout. Alpha 18 is for testing and changes actual stitch generation. The release says the browser Assistant cannot inspect pictures or import SVG yet. Physical output needs a separate test.

### How it uses AI

OpenStitch alpha 18 adds a model-connected Assistant to its browser editor. The creator can use AI to propose editable outlines and stitch objects, then check the generated paths in the updated engine. [Source](https://github.com/cristianonescu/OpenStitch/blob/main/README.md) [Source](https://cristianonescu.github.io/OpenStitch/)

### Introduction

OpenStitch alpha 18 adds a model-connected Assistant to its browser editor. The creator can use AI to propose editable outlines and stitch objects, then check the generated paths in the updated engine. [Source 1](https://github.com/cristianonescu/OpenStitch/blob/main/README.md) [Source 2](https://cristianonescu.github.io/OpenStitch/)

### What it is good for

Prototype a small embroidered motif with the browser Assistant, then validate the altered stitch geometry in a separate setup. [Source 1](https://github.com/cristianonescu/OpenStitch/blob/main/README.md) [Source 2](https://cristianonescu.github.io/OpenStitch/)

### Demo & examples

The release documents the browser Assistant and a set of fill, net, satin and candlewick changes. It explicitly says that stitch output differs from alpha 17. [Source 1](https://github.com/cristianonescu/OpenStitch/blob/main/README.md) [Source 2](https://cristianonescu.github.io/OpenStitch/)

### Install

Follow the documented route for the scoped workflow. The steps below are source references. [Source 1](https://github.com/cristianonescu/OpenStitch/blob/main/README.md) [Source 2](https://cristianonescu.github.io/OpenStitch/)

1. Use the official browser app or the matching alpha 18 desktop artifact and checksum.
2. Set up only the Assistant backend needed for the chosen workflow and ensure you may send the relevant prompts or design data to it. Check exact browser limitations.
### First project

A small first project makes the input, model output and handoff easy to inspect. [Source 1](https://github.com/cristianonescu/OpenStitch/blob/main/README.md) [Source 2](https://cristianonescu.github.io/OpenStitch/)

1. Create a test motif with explicit thread and hoop dimensions. Ask for one small design addition, then edit the resulting object.
2. Inspect stitch order, fills and point geometry. Compare the new version against the prior reference and test-sew only on suitable sample material before production.
### Hardware & software

Platform and compute constraints refer to the selected route. [Source 1](https://github.com/cristianonescu/OpenStitch/blob/main/README.md) [Source 2](https://cristianonescu.github.io/OpenStitch/)

- **Hardware:** Minimum RAM, VRAM and disk space for the scoped workflow are undocumented.
- **Software:** Alpha 18 OpenStitch and optional approved model/agent provider. The browser setup differs from desktop and currently limits the assistant’s visual inputs.
- **Platforms:** Release lists macOS 11+ Intel and Apple silicon, Windows 10/11 x64, Linux x64 and browser. Mobile layouts do not establish machine connectivity.

### License, model weights & costs

The full software license was reviewed. Dependencies and creative assets carry their own terms. [Source 1](https://github.com/cristianonescu/OpenStitch/blob/main/LICENSE-APACHE) [Source 2](https://github.com/cristianonescu/OpenStitch/blob/main/README.md) [Source 3](https://cristianonescu.github.io/OpenStitch/)

- **Code:** Apache-2.0
- **Weights:** The root permissive software grant and alternate license file were reviewed. Model, font and design inputs carry separate terms. Brother interoperability does not transfer rights to assets.
- **Commercial:** Project code is governed by Apache-2.0. Confirm selected model, source-media and output restrictions separately.
- **Cost:** Local editing needs compute. The optional model and hosting path may have separate subscription or network costs.

### Why it merits attention

The creative workflow is grounded in the cited documentation. Output quality and compatibility are not hands-on verified. [Source 1](https://github.com/cristianonescu/OpenStitch/blob/main/README.md) [Source 2](https://cristianonescu.github.io/OpenStitch/)

### Limitations

Alpha 18 is for testing and changes actual stitch generation. The release says the browser Assistant cannot inspect pictures or import SVG yet. Physical output needs a separate test. [Source 1](https://github.com/cristianonescu/OpenStitch/blob/main/README.md) [Source 2](https://cristianonescu.github.io/OpenStitch/)

### Get the tool

- [Repository](https://github.com/cristianonescu/OpenStitch)
- [Documentation](https://cristianonescu.github.io/OpenStitch/)

## ZigZag

Neural embroidery and stitch design · AI-assisted textile and computational craft · Vector graphics, illustration & textures

Version 0.1.7 adds saved per-design chats, image prompts and an agent preflight review after the v0.1.6 guide.

### Quality assessment: Quality unverified

Creative use and the code grant are documented. Check-level gaps remain before a recommendation.

Scope: Iterate an embroidery design with an agent while preserving local conversation context, editable stitch objects and a separate preflight review.

Evidence checked: 2026-11-21. No local execution implied.

- **Open-source software license · verified:** Reviewed the complete project software grant and its redistribution conditions. Model, data and service terms are scoped separately. [Source](https://github.com/simpsoka/zigzag/blob/main/LICENSE)
- **Creative results · documented:** The current release explains agent conversation history, attached images, prompted review and conditional routing. Those checks do not establish how a particular thread, fabric and stabilizer sew. [Source](https://github.com/simpsoka/zigzag/blob/main/README.md)
- **Reproducible setup · documented:** The installation and first-use steps are in the cited documentation. Reproduction of this workflow remains unverified. [Source](https://github.com/simpsoka/zigzag/blob/main/README.md)
- **Maintenance and support · documented:** The v0.1.7 notes identify agent, stitch and crash-fix changes since v0.1.6. Device/machine-specific support is unverified. [Source](https://github.com/simpsoka/zigzag/releases/tag/v0.1.7)
- **Independent use · unknown:** Independent first-hand use of the exact workflow was not established in this source review.
- **Models, services and costs · documented:** The complete Apache-2.0 application grant was reviewed. The connected agent, fonts, drawings and source design assets retain their own terms. The editor uses local compute. External model use varies with the agent and account. Reference images may be routed to that selected provider. [Source](https://github.com/simpsoka/zigzag/blob/main/README.md)

Source and documentation review. No hands-on execution by AI Media Scout. Agent transcripts are retained on the computer per design, according to the release. This review did not independently reproduce thread routing or sew results.

### How it uses AI

ZigZag v0.1.7 keeps previous agent chats per design and supports images in prompts. Its new agent design review describes stitch cost, trims, routing, contrast and details that may be hard to sew. [Source](https://github.com/simpsoka/zigzag/blob/main/README.md)

### Introduction

ZigZag v0.1.7 keeps previous agent chats per design and supports images in prompts. Its new agent design review describes stitch cost, trims, routing, contrast and details that may be hard to sew. [Source 1](https://github.com/simpsoka/zigzag/blob/main/README.md)

### What it is good for

Iterate an embroidery design with an agent while preserving local conversation context, editable stitch objects and a separate preflight review. [Source 1](https://github.com/simpsoka/zigzag/blob/main/README.md)

### Demo & examples

The current release explains agent conversation history, attached images, prompted review and conditional routing. Those checks do not establish how a particular thread, fabric and stabilizer sew. [Source 1](https://github.com/simpsoka/zigzag/blob/main/README.md)

### Install

Follow the documented route for the scoped workflow. The steps below are source references. [Source 1](https://github.com/simpsoka/zigzag/blob/main/README.md)

1. Choose the v0.1.7 package matching your OS and use the official documentation. Set up a compatible agent connection when using the agent panel.
2. Check chosen model access and prepare a copy of the design for review. The editor route without agent use remains available.
### First project

A small first project makes the input, model output and handoff easy to inspect. [Source 1](https://github.com/simpsoka/zigzag/blob/main/README.md)

1. Open the test design. Add a permitted reference image or create one scoped edit request in the agent panel.
2. Review the design using the new agent operation and compare its suggestions with the stitch preview. Inspect points, trims, thread changes and longer traversal routes.
3. Save the editable revision and a separately reviewed export. Compare a physical test on the target material before repeating it.
### Hardware & software

Platform and compute constraints refer to the selected route. [Source 1](https://github.com/simpsoka/zigzag/blob/main/README.md)

- **Hardware:** Minimum RAM, VRAM and disk space for the scoped workflow are undocumented.
- **Software:** ZigZag v0.1.7 and optionally its documented Rust bridge or packaged MCP path. Claude Code and Codex are separately supported agent routes as noted in the release.
- **Platforms:** macOS 11+ on Intel and Apple silicon, Windows 10 1709+ x64 and Linux x64 with glibc 2.35+ are documented. Validate the exact selected artifact.

### License, model weights & costs

The full software license was reviewed. Dependencies and creative assets carry their own terms. [Source 1](https://github.com/simpsoka/zigzag/blob/main/LICENSE) [Source 2](https://github.com/simpsoka/zigzag/blob/main/README.md)

- **Code:** Apache-2.0
- **Weights:** The complete Apache-2.0 application grant was reviewed. The connected agent, fonts, drawings and source design assets retain their own terms.
- **Commercial:** Project code is governed by Apache-2.0. Confirm selected model, source-media and output restrictions separately.
- **Cost:** The editor uses local compute. External model use varies with the agent and account. Reference images may be routed to that selected provider.

### Why it merits attention

The creative workflow is grounded in the cited documentation. Output quality and compatibility are not hands-on verified. [Source 1](https://github.com/simpsoka/zigzag/blob/main/README.md)

### Limitations

Agent transcripts are retained on the computer per design, according to the release. This review did not independently reproduce thread routing or sew results. [Source 1](https://github.com/simpsoka/zigzag/blob/main/README.md)

### Get the tool

- [Repository](https://github.com/simpsoka/zigzag)
- [Documentation](https://github.com/simpsoka/zigzag/blob/main/README.md)

## Velo

Performance, projection & stage media · Physical, robotic & kinetic installations · Images & design

The compared v0.9.9-beta code adds recording with audio and macOS Syphon output after the v0.9.8-beta guide.

### Quality assessment: Quality unverified

Creative use and the code grant are documented. Check-level gaps remain before a recommendation.

Scope: Create a generated texture or visual layer in a small show graph and record a rehearsed visual plus sound output for feedback.

Evidence checked: 2026-11-21. No local execution implied.

- **Open-source software license · verified:** Reviewed the complete project software grant and its redistribution conditions. Model, data and service terms are scoped separately. [Source](https://github.com/g1lg1l/velo/blob/main/LICENSE-GPL)
- **Creative results · documented:** The code comparison identifies the recording and Syphon changes by commit. It does not establish exact output synchronization, encoder availability or stage throughput. [Source](https://github.com/g1lg1l/velo/blob/main/README.md) [Source](https://github.com/g1lg1l/velo/compare/v0.9.8-beta...v0.9.9-beta)
- **Reproducible setup · documented:** The installation and first-use steps are in the cited documentation. Reproduction of this workflow remains unverified. [Source](https://github.com/g1lg1l/velo/blob/main/README.md) [Source](https://github.com/g1lg1l/velo/compare/v0.9.8-beta...v0.9.9-beta)
- **Maintenance and support · documented:** The v0.9.8-beta-to-v0.9.9-beta compare documents audio/video recording, Syphon, autosave and UI changes. [Source](https://github.com/g1lg1l/velo/releases/tag/v0.9.9-beta)
- **Independent use · unknown:** Independent first-hand use of the exact workflow was not established in this source review.
- **Models, services and costs · documented:** The reviewed desktop app is GPL-3.0-or-later. The code libraries offer separate MIT/Apache grants. Selected image models, encoders and external technologies follow their own terms. Local shows use device compute and disk. Model and encoder downloads, any performance host and external services may add costs. [Source](https://github.com/g1lg1l/velo/blob/main/README.md) [Source](https://github.com/g1lg1l/velo/compare/v0.9.8-beta...v0.9.9-beta)

Source and documentation review. No hands-on execution by AI Media Scout. The new build is an explicitly beta-named release of the live app. Timing, frame rate and capture reliability require a rehearsal. The project’s author reports code changes, with no on-site test from this review.

### How it uses AI

Velo combines AI image-generation nodes with an editable live visual graph. The v0.9.9-beta source changes add recorded visual output with audio, a Mac Syphon path and revised live autosave behavior. [Source](https://github.com/g1lg1l/velo/blob/main/README.md) [Source](https://github.com/g1lg1l/velo/compare/v0.9.8-beta...v0.9.9-beta)

### Introduction

Velo combines AI image-generation nodes with an editable live visual graph. The v0.9.9-beta source changes add recorded visual output with audio, a Mac Syphon path and revised live autosave behavior. [Source 1](https://github.com/g1lg1l/velo/blob/main/README.md) [Source 2](https://github.com/g1lg1l/velo/compare/v0.9.8-beta...v0.9.9-beta)

### What it is good for

Create a generated texture or visual layer in a small show graph and record a rehearsed visual plus sound output for feedback. [Source 1](https://github.com/g1lg1l/velo/blob/main/README.md) [Source 2](https://github.com/g1lg1l/velo/compare/v0.9.8-beta...v0.9.9-beta)

### Demo & examples

The code comparison identifies the recording and Syphon changes by commit. It does not establish exact output synchronization, encoder availability or stage throughput. [Source 1](https://github.com/g1lg1l/velo/blob/main/README.md) [Source 2](https://github.com/g1lg1l/velo/compare/v0.9.8-beta...v0.9.9-beta)

### Install

Follow the documented route for the scoped workflow. The steps below are source references. [Source 1](https://github.com/g1lg1l/velo/blob/main/README.md) [Source 2](https://github.com/g1lg1l/velo/compare/v0.9.8-beta...v0.9.9-beta)

1. Use the corresponding Velo app release and its documented platform prerequisites. Review the exact version and audio device support.
2. Configure the local image-generation route and required model through the project’s setup. Prepare the encoder or selected Syphon host only for the intended capture path.
### First project

A small first project makes the input, model output and handoff easy to inspect. [Source 1](https://github.com/g1lg1l/velo/blob/main/README.md) [Source 2](https://github.com/g1lg1l/velo/compare/v0.9.8-beta...v0.9.9-beta)

1. Create a short show graph with a generated layer. Compare it with a reproducible source and confirm live control.
2. Make a short recording with audio and watch it back before rehearsing a long set. For Syphon, verify the Mac receiver independently.
3. Keep the editable graph, recording settings and backup. Confirm device timing on the actual rehearsal system.
### Hardware & software

Platform and compute constraints refer to the selected route. [Source 1](https://github.com/g1lg1l/velo/blob/main/README.md) [Source 2](https://github.com/g1lg1l/velo/compare/v0.9.8-beta...v0.9.9-beta)

- **Hardware:** Minimum RAM, VRAM and disk space for the scoped workflow are undocumented.
- **Software:** Velo 0.9.9-beta, the chosen AI image backend and weights. Output recording uses its documented encoder path, and Syphon is a Mac route.
- **Platforms:** Verify the release asset for the host. The current comparison documents Syphon output on macOS. No other host inherits that output capability.

### License, model weights & costs

The full software license was reviewed. Dependencies and creative assets carry their own terms. [Source 1](https://github.com/g1lg1l/velo/blob/main/LICENSE-GPL) [Source 2](https://github.com/g1lg1l/velo/blob/main/README.md) [Source 3](https://github.com/g1lg1l/velo/compare/v0.9.8-beta...v0.9.9-beta)

- **Code:** GPL-3.0-or-later
- **Weights:** The reviewed desktop app is GPL-3.0-or-later. The code libraries offer separate MIT/Apache grants. Selected image models, encoders and external technologies follow their own terms.
- **Commercial:** Project code is governed by GPL-3.0-or-later. Confirm selected model, source-media and output restrictions separately.
- **Cost:** Local shows use device compute and disk. Model and encoder downloads, any performance host and external services may add costs.

### Why it merits attention

The creative workflow is grounded in the cited documentation. Output quality and compatibility are not hands-on verified. [Source 1](https://github.com/g1lg1l/velo/blob/main/README.md) [Source 2](https://github.com/g1lg1l/velo/compare/v0.9.8-beta...v0.9.9-beta)

### Limitations

The new build is an explicitly beta-named release of the live app. Timing, frame rate and capture reliability require a rehearsal. The project’s author reports code changes, with no on-site test from this review. [Source 1](https://github.com/g1lg1l/velo/blob/main/README.md) [Source 2](https://github.com/g1lg1l/velo/compare/v0.9.8-beta...v0.9.9-beta)

### Get the tool

- [Repository](https://github.com/g1lg1l/velo)
- [Documentation](https://github.com/g1lg1l/velo/compare/v0.9.8-beta...v0.9.9-beta)

## Smashcut

Editing, captions & post-production · Motion capture & character animation · AI agents for code-authored media production

This completes an earlier pending guide with a current source review.

### Quality assessment: Quality unverified

Creative use and the code grant are documented. Check-level gaps remain before a recommendation.

Scope: Create a short product explainer with editable layers and assets that can be revised under source control.

Evidence checked: 2026-11-21. No local execution implied.

- **Open-source software license · verified:** Reviewed the complete project software grant and its redistribution conditions. Model, data and service terms are scoped separately. [Source](https://github.com/legostin/smashcut/blob/main/LICENSE)
- **Creative results · documented:** The source previews motion-technique examples and documents its local studio. The project’s own examples do not establish render parity on a different machine. [Source](https://github.com/legostin/smashcut/blob/main/README.md)
- **Reproducible setup · documented:** The installation and first-use steps are in the cited documentation. Reproduction of this workflow remains unverified. [Source](https://github.com/legostin/smashcut/blob/main/README.md)
- **Maintenance and support · unknown:** The reviewed sources do not establish workflow-specific support, fixes and unresolved blockers.
- **Independent use · unknown:** Independent first-hand use of the exact workflow was not established in this source review.
- **Models, services and costs · documented:** MIT applies to project code. Claude Code or Codex, optional voice and video services, imported assets and packaged third-party materials have separate terms. The local studio uses local compute, but the documented agent route needs authorized access. Optional external generation can add service charges. [Source](https://github.com/legostin/smashcut/blob/main/README.md)

Source and documentation review. No hands-on execution by AI Media Scout. Human review is needed for agent edits and generated visuals. Preview and export matching has not been independently verified for the selected runtime.

### How it uses AI

A connected coding agent builds editable motion graphics and video sequences as code inside a local project. Smashcut supplies a preview, scene techniques and rendering controls. [Source](https://github.com/legostin/smashcut/blob/main/README.md)

### Introduction

A connected coding agent builds editable motion graphics and video sequences as code inside a local project. Smashcut supplies a preview, scene techniques and rendering controls. [Source 1](https://github.com/legostin/smashcut/blob/main/README.md)

### What it is good for

Create a short product explainer with editable layers and assets that can be revised under source control. [Source 1](https://github.com/legostin/smashcut/blob/main/README.md)

### Demo & examples

The source previews motion-technique examples and documents its local studio. The project’s own examples do not establish render parity on a different machine. [Source 1](https://github.com/legostin/smashcut/blob/main/README.md)

### Install

Follow the documented route for the scoped workflow. The steps below are source references. [Source 1](https://github.com/legostin/smashcut/blob/main/README.md)

1. Use Node.js 20 or later on the documented macOS or Linux route and an authenticated Claude Code or Codex CLI.
2. Start the studio through the published package. Run the documented doctor command for render browser, FFmpeg and agent checks. Install optional Blender only for 3D work.

```sh
npx smashcut-studio
```


```sh
smashcut doctor
```

### First project

A small first project makes the input, model output and handoff easy to inspect. [Source 1](https://github.com/legostin/smashcut/blob/main/README.md)

1. Create a small versioned project and request a three-shot explainer with a title and one diagram.
2. Open the preview, inspect code and assets for each scene, and revise the layouts before render.
3. Export a short draft and compare it with the studio preview. Review rights on any model-generated or third-party assets.
### Hardware & software

Platform and compute constraints refer to the selected route. [Source 1](https://github.com/legostin/smashcut/blob/main/README.md)

- **Hardware:** Minimum RAM, VRAM and disk space for the scoped workflow are undocumented.
- **Software:** Node.js 20+, authorized agent CLI, render browser and FFmpeg. Blender is optional. FFmpeg fallback and one-time headless browser downloads are documented.
- **Platforms:** macOS and Linux are documented. Windows native compatibility is unverified.

### License, model weights & costs

The full software license was reviewed. Dependencies and creative assets carry their own terms. [Source 1](https://github.com/legostin/smashcut/blob/main/LICENSE) [Source 2](https://github.com/legostin/smashcut/blob/main/README.md)

- **Code:** MIT
- **Weights:** MIT applies to project code. Claude Code or Codex, optional voice and video services, imported assets and packaged third-party materials have separate terms.
- **Commercial:** Project code is governed by MIT. Confirm selected model, source-media and output restrictions separately.
- **Cost:** The local studio uses local compute, but the documented agent route needs authorized access. Optional external generation can add service charges.

### Why it merits attention

The creative workflow is grounded in the cited documentation. Output quality and compatibility are not hands-on verified. [Source 1](https://github.com/legostin/smashcut/blob/main/README.md)

### Limitations

Human review is needed for agent edits and generated visuals. Preview and export matching has not been independently verified for the selected runtime. [Source 1](https://github.com/legostin/smashcut/blob/main/README.md)

### Get the tool

- [Repository](https://github.com/legostin/smashcut)
- [Documentation](https://github.com/legostin/smashcut/blob/main/README.md)

## LexCut

Editing, captions & post-production · Video, animation & film · Accessible media & assistive creation

This completes an earlier pending guide with a current source review.

### Quality assessment: Quality unverified

Creative use and the code grant are documented. Check-level gaps remain before a recommendation.

Scope: Cut a short Sinhala or multilingual video on a Mac and keep a corrected subtitle file alongside the final video.

Evidence checked: 2026-11-21. No local execution implied.

- **Open-source software license · verified:** Reviewed the complete project software grant and its redistribution conditions. Model, data and service terms are scoped separately. [Source](https://github.com/indunissanka/lexcut/blob/main/LICENSE)
- **Creative results · documented:** The maintainer documents features and a local installer. Output quality and compatibility with a particular language or browser are unverified. [Source](https://github.com/indunissanka/lexcut/blob/main/README.md) [Source](https://huggingface.co/SinhaSpeech/whisper-small-sinhala-run12-best)
- **Reproducible setup · documented:** The installation and first-use steps are in the cited documentation. Reproduction of this workflow remains unverified. [Source](https://github.com/indunissanka/lexcut/blob/main/README.md) [Source](https://huggingface.co/SinhaSpeech/whisper-small-sinhala-run12-best)
- **Maintenance and support · unknown:** The reviewed sources do not establish workflow-specific support, fixes and unresolved blockers.
- **Independent use · unknown:** Independent first-hand use of the exact workflow was not established in this source review.
- **Models, services and costs · documented:** MIT applies to LexCut. The README identifies MIT for Whisper large-v3, Apache-2.0 for the Sinhala model, and noncommercial terms for optional Coqui XTTS-v2. The chosen asset and model versions need their own checks. Speech processing for the scoped route is local. Any optional agent/translator provider and initial downloads have separate requirements. [Source](https://github.com/indunissanka/lexcut/blob/main/README.md) [Source](https://huggingface.co/SinhaSpeech/whisper-small-sinhala-run12-best)

Source and documentation review. No hands-on execution by AI Media Scout. The current language documentation reports looping in large-v3 on some Sinhala input. Verify cue timing with the exact checkpoint and speakers. Use the audio only with appropriate consent.

### How it uses AI

LexCut serves a local browser timeline on Apple silicon and can generate editable subtitles from the audio through Whisper. It documents a separate Sinhala checkpoint for Sinhala speech. [Source](https://github.com/indunissanka/lexcut/blob/main/README.md) [Source](https://huggingface.co/SinhaSpeech/whisper-small-sinhala-run12-best)

### Introduction

LexCut serves a local browser timeline on Apple silicon and can generate editable subtitles from the audio through Whisper. It documents a separate Sinhala checkpoint for Sinhala speech. [Source 1](https://github.com/indunissanka/lexcut/blob/main/README.md) [Source 2](https://huggingface.co/SinhaSpeech/whisper-small-sinhala-run12-best)

### What it is good for

Cut a short Sinhala or multilingual video on a Mac and keep a corrected subtitle file alongside the final video. [Source 1](https://github.com/indunissanka/lexcut/blob/main/README.md) [Source 2](https://huggingface.co/SinhaSpeech/whisper-small-sinhala-run12-best)

### Demo & examples

The maintainer documents features and a local installer. Output quality and compatibility with a particular language or browser are unverified. [Source 1](https://github.com/indunissanka/lexcut/blob/main/README.md) [Source 2](https://huggingface.co/SinhaSpeech/whisper-small-sinhala-run12-best)

### Install

Follow the documented route for the scoped workflow. The steps below are source references. [Source 1](https://github.com/indunissanka/lexcut/blob/main/README.md) [Source 2](https://huggingface.co/SinhaSpeech/whisper-small-sinhala-run12-best)

1. Use the documented Apple silicon Mac with Homebrew and review the installer and required downloads. Allow the installer to set up Python 3.11, FFmpeg and the local environments, or follow the documented source steps.
2. Launch the installed app and choose the correct speech model before transcribing.
### First project

A small first project makes the input, model output and handoff easy to inspect. [Source 1](https://github.com/indunissanka/lexcut/blob/main/README.md) [Source 2](https://huggingface.co/SinhaSpeech/whisper-small-sinhala-run12-best)

1. Put a brief speaker clip on the timeline and generate a draft in the original spoken language.
2. Edit cue breaks against the source. Compare the Sinhala and generic Whisper routes on a controlled short clip if relevant.
3. Export SRT or VTT beside a video proof. Review the separate voice module’s terms before adding any generated narration.
### Hardware & software

Platform and compute constraints refer to the selected route. [Source 1](https://github.com/indunissanka/lexcut/blob/main/README.md) [Source 2](https://huggingface.co/SinhaSpeech/whisper-small-sinhala-run12-best)

- **Hardware:** Apple M1 or later documented. The optional model prefetch is roughly 4 GB for Whisper models plus OpenVoice. Minimum RAM and total disk are undocumented.
- **Software:** Homebrew, Python 3.11 and FFmpeg through the documented installer. The local editor needs a browser. Model files may be fetched at first use.
- **Platforms:** macOS on Apple silicon is documented. Windows, Linux and Intel macOS support are unverified.

### License, model weights & costs

The full software license was reviewed. Dependencies and creative assets carry their own terms. [Source 1](https://github.com/indunissanka/lexcut/blob/main/LICENSE) [Source 2](https://github.com/indunissanka/lexcut/blob/main/README.md) [Source 3](https://huggingface.co/SinhaSpeech/whisper-small-sinhala-run12-best)

- **Code:** MIT
- **Weights:** MIT applies to LexCut. The README identifies MIT for Whisper large-v3, Apache-2.0 for the Sinhala model, and noncommercial terms for optional Coqui XTTS-v2. The chosen asset and model versions need their own checks.
- **Commercial:** Project code is governed by MIT. Confirm selected model, source-media and output restrictions separately.
- **Cost:** Speech processing for the scoped route is local. Any optional agent/translator provider and initial downloads have separate requirements.

### Why it merits attention

The creative workflow is grounded in the cited documentation. Output quality and compatibility are not hands-on verified. [Source 1](https://github.com/indunissanka/lexcut/blob/main/README.md) [Source 2](https://huggingface.co/SinhaSpeech/whisper-small-sinhala-run12-best)

### Limitations

The current language documentation reports looping in large-v3 on some Sinhala input. Verify cue timing with the exact checkpoint and speakers. Use the audio only with appropriate consent. [Source 1](https://github.com/indunissanka/lexcut/blob/main/README.md) [Source 2](https://huggingface.co/SinhaSpeech/whisper-small-sinhala-run12-best)

### Get the tool

- [Repository](https://github.com/indunissanka/lexcut)
- [Documentation](https://huggingface.co/SinhaSpeech/whisper-small-sinhala-run12-best)

## Wabcut

Editing, captions & post-production · Video, animation & film · Accessible media & assistive creation

This completes an earlier pending guide with a current source review.

### Quality assessment: Experimental

Creative use and the code grant are documented. Check-level gaps remain before a recommendation.

Scope: Assemble a short edit on Windows x64 and export an independently editable caption file with the video or timeline handoff.

Evidence checked: 2026-11-21. No local execution implied.

Why Experimental: The current README identifies Wabcut 0.7.0 as an alpha. macOS, Linux and Windows ARM64 are preview builds, and transcription is still limited to Windows x64. https://github.com/sorsama/wabcut/blob/main/README.md

- **Open-source software license · verified:** Reviewed the complete project software grant and its redistribution conditions. Model, data and service terms are scoped separately. [Source](https://github.com/sorsama/wabcut/blob/main/LICENSE)
- **Creative results · documented:** The version 0.7 release notes describe the revised AI settings and editing controls. Maintainer testing is Windows-focused and the other downloads are previews. [Source](https://github.com/sorsama/wabcut/blob/main/README.md) [Source](https://github.com/sorsama/wabcut/blob/main/docs/getting-started.md) [Source](https://github.com/sorsama/wabcut/blob/main/docs/release-notes-0.7.md)
- **Reproducible setup · documented:** The installation and first-use steps are in the cited documentation. Reproduction of this workflow remains unverified. [Source](https://github.com/sorsama/wabcut/blob/main/README.md) [Source](https://github.com/sorsama/wabcut/blob/main/docs/getting-started.md) [Source](https://github.com/sorsama/wabcut/blob/main/docs/release-notes-0.7.md)
- **Maintenance and support · documented:** Release v0.7.0 describes substantive timeline and AI changes. Open blockers and platform coverage remain scoped. [Source](https://github.com/sorsama/wabcut/releases/tag/v0.7.0)
- **Independent use · unknown:** Independent first-hand use of the exact workflow was not established in this source review.
- **Models, services and costs · documented:** The complete GPLv3 code file and third-party notices were inspected. Exact speech checkpoint and any external generation service retain their own terms. Local captioning uses local compute. A selected third-party provider can introduce service costs. [Source](https://github.com/sorsama/wabcut/blob/main/README.md) [Source](https://github.com/sorsama/wabcut/blob/main/docs/getting-started.md) [Source](https://github.com/sorsama/wabcut/blob/main/docs/release-notes-0.7.md)

Source and documentation review. No hands-on execution by AI Media Scout. The maintainer explicitly describes an alpha, preview platforms and incomplete feature parity. Work on a copy and confirm whether timeline interchange retains the properties you need.

### How it uses AI

Wabcut combines a desktop timeline with locally run speech recognition on the documented Windows x64 build. The current alpha includes model management and SRT/VTT export. [Source](https://github.com/sorsama/wabcut/blob/main/README.md) [Source](https://github.com/sorsama/wabcut/blob/main/docs/getting-started.md) [Source](https://github.com/sorsama/wabcut/blob/main/docs/release-notes-0.7.md)

### Introduction

Wabcut combines a desktop timeline with locally run speech recognition on the documented Windows x64 build. The current alpha includes model management and SRT/VTT export. [Source 1](https://github.com/sorsama/wabcut/blob/main/README.md) [Source 2](https://github.com/sorsama/wabcut/blob/main/docs/getting-started.md) [Source 3](https://github.com/sorsama/wabcut/blob/main/docs/release-notes-0.7.md)

### What it is good for

Assemble a short edit on Windows x64 and export an independently editable caption file with the video or timeline handoff. [Source 1](https://github.com/sorsama/wabcut/blob/main/README.md) [Source 2](https://github.com/sorsama/wabcut/blob/main/docs/getting-started.md) [Source 3](https://github.com/sorsama/wabcut/blob/main/docs/release-notes-0.7.md)

### Demo & examples

The version 0.7 release notes describe the revised AI settings and editing controls. Maintainer testing is Windows-focused and the other downloads are previews. [Source 1](https://github.com/sorsama/wabcut/blob/main/README.md) [Source 2](https://github.com/sorsama/wabcut/blob/main/docs/getting-started.md) [Source 3](https://github.com/sorsama/wabcut/blob/main/docs/release-notes-0.7.md)

### Install

Follow the documented route for the scoped workflow. The steps below are source references. [Source 1](https://github.com/sorsama/wabcut/blob/main/README.md) [Source 2](https://github.com/sorsama/wabcut/blob/main/docs/getting-started.md) [Source 3](https://github.com/sorsama/wabcut/blob/main/docs/release-notes-0.7.md)

1. Get the current Windows x64 MSI or portable package from the official 0.7.0 release. Read the signing note before installing.
2. Open the AI settings and configure the supported local speech model. Review the getting-started guide before importing a project.
### First project

A small first project makes the input, model output and handoff easy to inspect. [Source 1](https://github.com/sorsama/wabcut/blob/main/README.md) [Source 2](https://github.com/sorsama/wabcut/blob/main/docs/getting-started.md) [Source 3](https://github.com/sorsama/wabcut/blob/main/docs/release-notes-0.7.md)

1. Import a short talking clip, trim it on the timeline and transcribe using the local x64 route.
2. Check the in/out boundaries and caption cues, then export SRT or VTT. Use a small timeline round trip to validate another NLE handoff.
### Hardware & software

Platform and compute constraints refer to the selected route. [Source 1](https://github.com/sorsama/wabcut/blob/main/README.md) [Source 2](https://github.com/sorsama/wabcut/blob/main/docs/getting-started.md) [Source 3](https://github.com/sorsama/wabcut/blob/main/docs/release-notes-0.7.md)

- **Hardware:** Minimum RAM, VRAM and disk space for the scoped workflow are undocumented.
- **Software:** Wabcut v0.7.0 and its documented local speech model. External AI providers in the app have separate authentication and terms.
- **Platforms:** Windows 10 22H2 and 11 x64 are the maintainer-tested path. Windows ARM64, Linux x64 and Apple silicon macOS downloads are previews. Local speech transcription and audio plugins are Windows x64 only.

### License, model weights & costs

The full software license was reviewed. Dependencies and creative assets carry their own terms. [Source 1](https://github.com/sorsama/wabcut/blob/main/LICENSE) [Source 2](https://github.com/sorsama/wabcut/blob/main/README.md) [Source 3](https://github.com/sorsama/wabcut/blob/main/docs/getting-started.md) [Source 4](https://github.com/sorsama/wabcut/blob/main/docs/release-notes-0.7.md)

- **Code:** GPL-3.0
- **Weights:** The complete GPLv3 code file and third-party notices were inspected. Exact speech checkpoint and any external generation service retain their own terms.
- **Commercial:** Project code is governed by GPL-3.0. Confirm selected model, source-media and output restrictions separately.
- **Cost:** Local captioning uses local compute. A selected third-party provider can introduce service costs.

### Why it merits attention

The creative workflow is grounded in the cited documentation. Output quality and compatibility are not hands-on verified. [Source 1](https://github.com/sorsama/wabcut/blob/main/README.md) [Source 2](https://github.com/sorsama/wabcut/blob/main/docs/getting-started.md) [Source 3](https://github.com/sorsama/wabcut/blob/main/docs/release-notes-0.7.md)

### Limitations

The maintainer explicitly describes an alpha, preview platforms and incomplete feature parity. Work on a copy and confirm whether timeline interchange retains the properties you need. [Source 1](https://github.com/sorsama/wabcut/blob/main/README.md) [Source 2](https://github.com/sorsama/wabcut/blob/main/docs/getting-started.md) [Source 3](https://github.com/sorsama/wabcut/blob/main/docs/release-notes-0.7.md)

### Get the tool

- [Repository](https://github.com/sorsama/wabcut)
- [Documentation](https://github.com/sorsama/wabcut/blob/main/docs/release-notes-0.7.md)

## Sabicut

Editing, captions & post-production · Video, animation & film · Live production accessibility and routed captions

This completes an earlier pending guide with a current source review.

### Quality assessment: Experimental

Creative use and the code grant are documented. Check-level gaps remain before a recommendation.

Scope: Make an auditable edit plan, caption draft and vertical short from a local recording without submitting the source clip to an API.

Evidence checked: 2026-11-21. No local execution implied.

Why Experimental: The current status documents the command-line implementation and lists creator beta as an upcoming milestone. The author’s validation is for the implemented path and creator workflow remains unfinished. https://github.com/DCT-Berinyuy/sabicut/blob/main/README.md

- **Open-source software license · verified:** Reviewed the complete project software grant and its redistribution conditions. Model, data and service terms are scoped separately. [Source](https://github.com/DCT-Berinyuy/sabicut/blob/main/LICENSE-APACHE)
- **Creative results · documented:** The repository supplies a sample plan, validator, preview and render commands. The maintainers describe creator beta as an upcoming milestone. [Source](https://github.com/DCT-Berinyuy/sabicut/blob/main/README.md) [Source](https://github.com/DCT-Berinyuy/sabicut/blob/main/docs/PRD.md)
- **Reproducible setup · documented:** The installation and first-use steps are in the cited documentation. Reproduction of this workflow remains unverified. [Source](https://github.com/DCT-Berinyuy/sabicut/blob/main/README.md) [Source](https://github.com/DCT-Berinyuy/sabicut/blob/main/docs/PRD.md)
- **Maintenance and support · unknown:** The reviewed sources do not establish workflow-specific support, fixes and unresolved blockers.
- **Independent use · unknown:** Independent first-hand use of the exact workflow was not established in this source review.
- **Models, services and costs · documented:** The repository offers Apache-2.0 or MIT for code. Whisper and Silero model files and the bundled font have separate terms. Retain their notices. The scoped workflow runs locally after manual model acquisition. No transcription API is required. [Source](https://github.com/DCT-Berinyuy/sabicut/blob/main/README.md) [Source](https://github.com/DCT-Berinyuy/sabicut/blob/main/docs/PRD.md)

Source and documentation review. No hands-on execution by AI Media Scout. The current project defines its working edit-plan and command-line routes separately from a planned creator beta. Inspect the speech recognizer in the language being edited.

### How it uses AI

A Rust workflow extracts audio, finds speech with Silero, runs whisper.cpp and saves word timestamps that can be used for captioned vertical cuts. [Source](https://github.com/DCT-Berinyuy/sabicut/blob/main/README.md) [Source](https://github.com/DCT-Berinyuy/sabicut/blob/main/docs/PRD.md)

### Introduction

A Rust workflow extracts audio, finds speech with Silero, runs whisper.cpp and saves word timestamps that can be used for captioned vertical cuts. [Source 1](https://github.com/DCT-Berinyuy/sabicut/blob/main/README.md) [Source 2](https://github.com/DCT-Berinyuy/sabicut/blob/main/docs/PRD.md)

### What it is good for

Make an auditable edit plan, caption draft and vertical short from a local recording without submitting the source clip to an API. [Source 1](https://github.com/DCT-Berinyuy/sabicut/blob/main/README.md) [Source 2](https://github.com/DCT-Berinyuy/sabicut/blob/main/docs/PRD.md)

### Demo & examples

The repository supplies a sample plan, validator, preview and render commands. The maintainers describe creator beta as an upcoming milestone. [Source 1](https://github.com/DCT-Berinyuy/sabicut/blob/main/README.md) [Source 2](https://github.com/DCT-Berinyuy/sabicut/blob/main/docs/PRD.md)

### Install

Follow the documented route for the scoped workflow. The steps below are source references. [Source 1](https://github.com/DCT-Berinyuy/sabicut/blob/main/README.md) [Source 2](https://github.com/DCT-Berinyuy/sabicut/blob/main/docs/PRD.md)

1. On the documented Linux build route use a stable Rust toolchain with the 2024 edition, CMake, a C/C++ compiler, libclang and FFmpeg 6.1 or newer with libx264.
2. Obtain exact documented Whisper and Silero files ahead of time. Verify the hashes and place them in the documented model location.
### First project

A small first project makes the input, model output and handoff easy to inspect. [Source 1](https://github.com/DCT-Berinyuy/sabicut/blob/main/README.md) [Source 2](https://github.com/DCT-Berinyuy/sabicut/blob/main/docs/PRD.md)

1. Validate the sample plan and inspect its cut timing. Run analyze on a brief talk and review the timestamps before assembling a plan.
2. Render a small preview and compare the word highlights against speech. Produce the 1080-by-1920 MP4 and separate SRT when the draft is ready.
### Hardware & software

Platform and compute constraints refer to the selected route. [Source 1](https://github.com/DCT-Berinyuy/sabicut/blob/main/README.md) [Source 2](https://github.com/DCT-Berinyuy/sabicut/blob/main/docs/PRD.md)

- **Hardware:** Manual model table lists the quantized small checkpoint at 190 MB and about 0.7 GB available memory for its small-model analysis check. Complete system minima are undocumented.
- **Software:** Rust 2024 toolchain, CMake, C/C++ compiler, libclang, FFmpeg and ffprobe, Silero and whisper.cpp GGML models.
- **Platforms:** The build example documents Debian/Ubuntu-style prerequisites. Other platform support remains to be established.

### License, model weights & costs

The full software license was reviewed. Dependencies and creative assets carry their own terms. [Source 1](https://github.com/DCT-Berinyuy/sabicut/blob/main/LICENSE-APACHE) [Source 2](https://github.com/DCT-Berinyuy/sabicut/blob/main/README.md) [Source 3](https://github.com/DCT-Berinyuy/sabicut/blob/main/docs/PRD.md)

- **Code:** Apache-2.0
- **Weights:** The repository offers Apache-2.0 or MIT for code. Whisper and Silero model files and the bundled font have separate terms. Retain their notices.
- **Commercial:** Project code is governed by Apache-2.0. Confirm selected model, source-media and output restrictions separately.
- **Cost:** The scoped workflow runs locally after manual model acquisition. No transcription API is required.

### Why it merits attention

The creative workflow is grounded in the cited documentation. Output quality and compatibility are not hands-on verified. [Source 1](https://github.com/DCT-Berinyuy/sabicut/blob/main/README.md) [Source 2](https://github.com/DCT-Berinyuy/sabicut/blob/main/docs/PRD.md)

### Limitations

The current project defines its working edit-plan and command-line routes separately from a planned creator beta. Inspect the speech recognizer in the language being edited. [Source 1](https://github.com/DCT-Berinyuy/sabicut/blob/main/README.md) [Source 2](https://github.com/DCT-Berinyuy/sabicut/blob/main/docs/PRD.md)

### Get the tool

- [Repository](https://github.com/DCT-Berinyuy/sabicut)
- [Documentation](https://github.com/DCT-Berinyuy/sabicut/blob/main/docs/PRD.md)

## AlwaysCut

Editing, captions & post-production · Video, animation & film · AI agents for code-authored media production

This completes an earlier pending guide with a current source review.

### Quality assessment: Quality unverified

Creative use and the code grant are documented. Check-level gaps remain before a recommendation.

Scope: Use word-level transcript edits and AI-assisted proposals to make a reversible rough cut of a recorded interview.

Evidence checked: 2026-11-21. No local execution implied.

- **Open-source software license · verified:** Reviewed the complete project software grant and its redistribution conditions. Model, data and service terms are scoped separately. [Source](https://github.com/ffan008/AlwaysCut/blob/main/LICENSE)
- **Creative results · documented:** The README documents timeline commands and media exports. The current GitHub release listing was empty during preflight, so this profile uses the documented source route. [Source](https://github.com/ffan008/AlwaysCut/blob/main/README.md) [Source](https://github.com/ffan008/AlwaysCut/blob/main/CHANGELOG.md)
- **Reproducible setup · documented:** The installation and first-use steps are in the cited documentation. Reproduction of this workflow remains unverified. [Source](https://github.com/ffan008/AlwaysCut/blob/main/README.md) [Source](https://github.com/ffan008/AlwaysCut/blob/main/CHANGELOG.md)
- **Maintenance and support · unknown:** The reviewed sources do not establish workflow-specific support, fixes and unresolved blockers.
- **Independent use · unknown:** Independent first-hand use of the exact workflow was not established in this source review.
- **Models, services and costs · documented:** The editor code uses AGPLv3. Official and community effect assets have separate grants. AI services and local transcription models have their own terms. The core timeline and media remain local. Connected generation, agent and transcription services can require provider access or paid calls. [Source](https://github.com/ffan008/AlwaysCut/blob/main/README.md) [Source](https://github.com/ffan008/AlwaysCut/blob/main/CHANGELOG.md)

Source and documentation review. No hands-on execution by AI Media Scout. The maintainer describes early packages and an evolving project format. Keep a backup before opening an important edit. An exact production build was not reproduced.

### How it uses AI

AlwaysCut exposes its editable timeline through model-assisted transcription and connected agent tools. Agent proposals go through its normal editor commands instead of replacing the project with a rendered clip. [Source](https://github.com/ffan008/AlwaysCut/blob/main/README.md) [Source](https://github.com/ffan008/AlwaysCut/blob/main/CHANGELOG.md)

### Introduction

AlwaysCut exposes its editable timeline through model-assisted transcription and connected agent tools. Agent proposals go through its normal editor commands instead of replacing the project with a rendered clip. [Source 1](https://github.com/ffan008/AlwaysCut/blob/main/README.md) [Source 2](https://github.com/ffan008/AlwaysCut/blob/main/CHANGELOG.md)

### What it is good for

Use word-level transcript edits and AI-assisted proposals to make a reversible rough cut of a recorded interview. [Source 1](https://github.com/ffan008/AlwaysCut/blob/main/README.md) [Source 2](https://github.com/ffan008/AlwaysCut/blob/main/CHANGELOG.md)

### Demo & examples

The README documents timeline commands and media exports. The current GitHub release listing was empty during preflight, so this profile uses the documented source route. [Source 1](https://github.com/ffan008/AlwaysCut/blob/main/README.md) [Source 2](https://github.com/ffan008/AlwaysCut/blob/main/CHANGELOG.md)

### Install

Follow the documented route for the scoped workflow. The steps below are source references. [Source 1](https://github.com/ffan008/AlwaysCut/blob/main/README.md) [Source 2](https://github.com/ffan008/AlwaysCut/blob/main/CHANGELOG.md)

1. Use the source instructions with Node.js 24.x and npm. Select the documented CPU-only install option on Linux if CUDA is unnecessary.
2. Start the development app and configure only the AI or transcription provider used by the workflow. Use the documented local dev profile.

```sh
npm run dev
```

### First project

A small first project makes the input, model output and handoff easy to inspect. [Source 1](https://github.com/ffan008/AlwaysCut/blob/main/README.md) [Source 2](https://github.com/ffan008/AlwaysCut/blob/main/CHANGELOG.md)

1. Import an interview clip into a temporary project, run a short transcription job and inspect word alignment.
2. Apply or revise a proposed trim using the native timeline, retaining an editable version.
3. Export a draft caption file or FCPXML and check how it imports into the intended editor.
### Hardware & software

Platform and compute constraints refer to the selected route. [Source 1](https://github.com/ffan008/AlwaysCut/blob/main/README.md) [Source 2](https://github.com/ffan008/AlwaysCut/blob/main/CHANGELOG.md)

- **Hardware:** Minimum RAM, VRAM and disk space for the scoped workflow are undocumented.
- **Software:** Node.js 24.x and npm. Engine/export dependencies follow the source setup. AI or caption provider settings vary by workflow.
- **Platforms:** The source docs describe macOS, Windows and Linux distributions. Their release listing did not return an installer in this check. Treat support beyond the documented source environment as unverified.

### License, model weights & costs

The full software license was reviewed. Dependencies and creative assets carry their own terms. [Source 1](https://github.com/ffan008/AlwaysCut/blob/main/LICENSE) [Source 2](https://github.com/ffan008/AlwaysCut/blob/main/README.md) [Source 3](https://github.com/ffan008/AlwaysCut/blob/main/CHANGELOG.md)

- **Code:** AGPL-3.0
- **Weights:** The editor code uses AGPLv3. Official and community effect assets have separate grants. AI services and local transcription models have their own terms.
- **Commercial:** Project code is governed by AGPL-3.0. Confirm selected model, source-media and output restrictions separately.
- **Cost:** The core timeline and media remain local. Connected generation, agent and transcription services can require provider access or paid calls.

### Why it merits attention

The creative workflow is grounded in the cited documentation. Output quality and compatibility are not hands-on verified. [Source 1](https://github.com/ffan008/AlwaysCut/blob/main/README.md) [Source 2](https://github.com/ffan008/AlwaysCut/blob/main/CHANGELOG.md)

### Limitations

The maintainer describes early packages and an evolving project format. Keep a backup before opening an important edit. An exact production build was not reproduced. [Source 1](https://github.com/ffan008/AlwaysCut/blob/main/README.md) [Source 2](https://github.com/ffan008/AlwaysCut/blob/main/CHANGELOG.md)

### Get the tool

- [Repository](https://github.com/ffan008/AlwaysCut)
- [Documentation](https://github.com/ffan008/AlwaysCut/blob/main/CHANGELOG.md)

## Auto Video Editor

Editing, captions & post-production · Video, animation & film · Accessible media & assistive creation

This completes an earlier pending guide with a current source review.

### Quality assessment: Quality unverified

Creative use and the code grant are documented. Check-level gaps remain before a recommendation.

Scope: Turn Chinese-language source clips into a short cut with draft captions and an editable handoff.

Evidence checked: 2026-11-21. No local execution implied.

- **Open-source software license · verified:** Reviewed the complete project software grant and its redistribution conditions. Model, data and service terms are scoped separately. [Source](https://github.com/WuChiRay/auto-video-editor/blob/main/LICENSE)
- **Creative results · documented:** The README contains plan-driven rendering commands and identifies platform packages. The language models and editable proprietary-host import are documented routes rather than independently tested results. [Source](https://github.com/WuChiRay/auto-video-editor/blob/main/README.md) [Source](https://github.com/WuChiRay/auto-video-editor/blob/main/docs/MACOS.md) [Source](https://github.com/WuChiRay/auto-video-editor/blob/main/THIRD_PARTY_NOTICES.md)
- **Reproducible setup · documented:** The installation and first-use steps are in the cited documentation. Reproduction of this workflow remains unverified. [Source](https://github.com/WuChiRay/auto-video-editor/blob/main/README.md) [Source](https://github.com/WuChiRay/auto-video-editor/blob/main/docs/MACOS.md) [Source](https://github.com/WuChiRay/auto-video-editor/blob/main/THIRD_PARTY_NOTICES.md)
- **Maintenance and support · documented:** Version 0.4.1 and the platform docs describe an actual package release. Independent regression checks remain open. [Source](https://github.com/WuChiRay/auto-video-editor/releases/tag/v0.4.1)
- **Independent use · unknown:** Independent first-hand use of the exact workflow was not established in this source review.
- **Models, services and costs · documented:** MIT covers application code. Whisper, FFmpeg, imported media and the proprietary Jianying host retain separate terms. The local pipeline needs compute and storage. The optional downstream host has independent access and terms. [Source](https://github.com/WuChiRay/auto-video-editor/blob/main/README.md) [Source](https://github.com/WuChiRay/auto-video-editor/blob/main/docs/MACOS.md) [Source](https://github.com/WuChiRay/auto-video-editor/blob/main/THIRD_PARTY_NOTICES.md)

Source and documentation review. No hands-on execution by AI Media Scout. The packaged Windows route and Python transcription route have different dependencies. Test captions and re-import on a small project first.

### How it uses AI

The Python version can use local Whisper transcription to drive editable subtitles in the same pipeline that produces an MP4 or a Jianying draft. [Source](https://github.com/WuChiRay/auto-video-editor/blob/main/README.md) [Source](https://github.com/WuChiRay/auto-video-editor/blob/main/docs/MACOS.md) [Source](https://github.com/WuChiRay/auto-video-editor/blob/main/THIRD_PARTY_NOTICES.md)

### Introduction

The Python version can use local Whisper transcription to drive editable subtitles in the same pipeline that produces an MP4 or a Jianying draft. [Source 1](https://github.com/WuChiRay/auto-video-editor/blob/main/README.md) [Source 2](https://github.com/WuChiRay/auto-video-editor/blob/main/docs/MACOS.md) [Source 3](https://github.com/WuChiRay/auto-video-editor/blob/main/THIRD_PARTY_NOTICES.md)

### What it is good for

Turn Chinese-language source clips into a short cut with draft captions and an editable handoff. [Source 1](https://github.com/WuChiRay/auto-video-editor/blob/main/README.md) [Source 2](https://github.com/WuChiRay/auto-video-editor/blob/main/docs/MACOS.md) [Source 3](https://github.com/WuChiRay/auto-video-editor/blob/main/THIRD_PARTY_NOTICES.md)

### Demo & examples

The README contains plan-driven rendering commands and identifies platform packages. The language models and editable proprietary-host import are documented routes rather than independently tested results. [Source 1](https://github.com/WuChiRay/auto-video-editor/blob/main/README.md) [Source 2](https://github.com/WuChiRay/auto-video-editor/blob/main/docs/MACOS.md) [Source 3](https://github.com/WuChiRay/auto-video-editor/blob/main/THIRD_PARTY_NOTICES.md)

### Install

Follow the documented route for the scoped workflow. The steps below are source references. [Source 1](https://github.com/WuChiRay/auto-video-editor/blob/main/README.md) [Source 2](https://github.com/WuChiRay/auto-video-editor/blob/main/docs/MACOS.md) [Source 3](https://github.com/WuChiRay/auto-video-editor/blob/main/THIRD_PARTY_NOTICES.md)

1. Install Python 3.11 or later and FFmpeg/ffprobe for the Python path. Use the documented package extras for the selected draft and recognition features.
2. On Windows or macOS follow the platform packaging notes. Use the Python path for automatic transcription when the Windows bundle lacks models and dependencies.

```sh
python -m pip install '.[draft,voice,visual]'
```

### First project

A small first project makes the input, model output and handoff easy to inspect. [Source 1](https://github.com/WuChiRay/auto-video-editor/blob/main/README.md) [Source 2](https://github.com/WuChiRay/auto-video-editor/blob/main/docs/MACOS.md) [Source 3](https://github.com/WuChiRay/auto-video-editor/blob/main/THIRD_PARTY_NOTICES.md)

1. Prepare a short clip set and check timing in a documented sample plan.
2. Generate or supply SRT and review the Chinese cues. Render an MP4 proof and export an editable draft when the destination supports it.
### Hardware & software

Platform and compute constraints refer to the selected route. [Source 1](https://github.com/WuChiRay/auto-video-editor/blob/main/README.md) [Source 2](https://github.com/WuChiRay/auto-video-editor/blob/main/docs/MACOS.md) [Source 3](https://github.com/WuChiRay/auto-video-editor/blob/main/THIRD_PARTY_NOTICES.md)

- **Hardware:** Minimum RAM, VRAM and disk space for the scoped workflow are undocumented.
- **Software:** Python 3.11+, FFmpeg and ffprobe. Local Whisper is optional and requires a separate model. Editable Jianying drafts need a compatible Jianying installation.
- **Platforms:** Windows x64 bundle and Intel or Apple silicon macOS 15+ DMGs documented. Source installation describes other platforms without equivalent package verification.

### License, model weights & costs

The full software license was reviewed. Dependencies and creative assets carry their own terms. [Source 1](https://github.com/WuChiRay/auto-video-editor/blob/main/LICENSE) [Source 2](https://github.com/WuChiRay/auto-video-editor/blob/main/README.md) [Source 3](https://github.com/WuChiRay/auto-video-editor/blob/main/docs/MACOS.md) [Source 4](https://github.com/WuChiRay/auto-video-editor/blob/main/THIRD_PARTY_NOTICES.md)

- **Code:** MIT
- **Weights:** MIT covers application code. Whisper, FFmpeg, imported media and the proprietary Jianying host retain separate terms.
- **Commercial:** Project code is governed by MIT. Confirm selected model, source-media and output restrictions separately.
- **Cost:** The local pipeline needs compute and storage. The optional downstream host has independent access and terms.

### Why it merits attention

The creative workflow is grounded in the cited documentation. Output quality and compatibility are not hands-on verified. [Source 1](https://github.com/WuChiRay/auto-video-editor/blob/main/README.md) [Source 2](https://github.com/WuChiRay/auto-video-editor/blob/main/docs/MACOS.md) [Source 3](https://github.com/WuChiRay/auto-video-editor/blob/main/THIRD_PARTY_NOTICES.md)

### Limitations

The packaged Windows route and Python transcription route have different dependencies. Test captions and re-import on a small project first. [Source 1](https://github.com/WuChiRay/auto-video-editor/blob/main/README.md) [Source 2](https://github.com/WuChiRay/auto-video-editor/blob/main/docs/MACOS.md) [Source 3](https://github.com/WuChiRay/auto-video-editor/blob/main/THIRD_PARTY_NOTICES.md)

### Get the tool

- [Repository](https://github.com/WuChiRay/auto-video-editor)
- [Documentation](https://github.com/WuChiRay/auto-video-editor/blob/main/THIRD_PARTY_NOTICES.md)

## Polywright

3D, reconstruction & assets · 3D printing & generative CAD · Games & production pipelines

This completes an earlier pending guide with a current source review.

### Quality assessment: Quality unverified

Creative use and the code grant are documented. Check-level gaps remain before a recommendation.

Scope: Create a prop from a reference image and validate the resulting mesh against one game or fabrication target before a separate handoff.

Evidence checked: 2026-11-21. No local execution implied.

- **Open-source software license · verified:** Reviewed the complete project software grant and its redistribution conditions. Model, data and service terms are scoped separately. [Source](https://github.com/m4bwav/polywright/blob/main/LICENSE)
- **Creative results · documented:** The README walks through a prompt to game prop and print on a 16 GB GPU. It demonstrates the intended handoff, with model and backend choices still requiring reproduction. [Source](https://github.com/m4bwav/polywright/blob/main/README.md)
- **Reproducible setup · documented:** The installation and first-use steps are in the cited documentation. Reproduction of this workflow remains unverified. [Source](https://github.com/m4bwav/polywright/blob/main/README.md)
- **Maintenance and support · documented:** Release v0.6.18 was inspected. A scoped backend support assessment remains open. [Source](https://github.com/m4bwav/polywright/releases/tag/v0.6.18)
- **Independent use · unknown:** Independent first-hand use of the exact workflow was not established in this source review.
- **Models, services and costs · documented:** MIT covers Polywright. Hunyuan3D-2 or another selected checkpoint and Blender, slicers and reference meshes retain separate terms. The CLI itself uses local compute. Explicit hosted generation, hardware and downloads may carry costs. [Source](https://github.com/m4bwav/polywright/blob/main/README.md)

Source and documentation review. No hands-on execution by AI Media Scout. Mesh validation does not certify a printable structure, topology quality or game compatibility. Model availability and cost vary independently.

### How it uses AI

Polywright gives coding agents a 3D workflow CLI that can orchestrate an image-to-mesh backend and report geometry, UVs, bounding scale and target checks. [Source](https://github.com/m4bwav/polywright/blob/main/README.md)

### Introduction

Polywright gives coding agents a 3D workflow CLI that can orchestrate an image-to-mesh backend and report geometry, UVs, bounding scale and target checks. [Source 1](https://github.com/m4bwav/polywright/blob/main/README.md)

### What it is good for

Create a prop from a reference image and validate the resulting mesh against one game or fabrication target before a separate handoff. [Source 1](https://github.com/m4bwav/polywright/blob/main/README.md)

### Demo & examples

The README walks through a prompt to game prop and print on a 16 GB GPU. It demonstrates the intended handoff, with model and backend choices still requiring reproduction. [Source 1](https://github.com/m4bwav/polywright/blob/main/README.md)

### Install

Follow the documented route for the scoped workflow. The steps below are source references. [Source 1](https://github.com/m4bwav/polywright/blob/main/README.md)

1. Use the published Python CLI and install only the chosen external tools. Run the documented doctor command to confirm Blender and the selected ComfyUI host.
2. Prepare a compatible image-to-3D workflow and review its exact model terms before generating.

```sh
python pw.py doctor
```


```sh
python pw.py inspect model.glb
```

### First project

A small first project makes the input, model output and handoff easy to inspect. [Source 1](https://github.com/m4bwav/polywright/blob/main/README.md)

1. Generate one mesh from a reference with the selected backend and save the unedited GLB.
2. Inspect scale, triangle count, UVs and watertightness. Render reference views and compare them with the intended prop.
3. Export a derivative for the selected target. Validate slicing or engine import separately.
### Hardware & software

Platform and compute constraints refer to the selected route. [Source 1](https://github.com/m4bwav/polywright/blob/main/README.md)

- **Hardware:** The maintainer example uses a 16 GB GPU. The exact total RAM, disk and VRAM needed depend on model and operation.
- **Software:** The CLI is documented for Python 3.9+. Blender and ComfyUI with the chosen workflow and checkpoints are separate. A connected agent is optional for CLI operation.
- **Platforms:** The CLI targets Python environments. Backend and DCC compatibility need their own platform check.

### License, model weights & costs

The full software license was reviewed. Dependencies and creative assets carry their own terms. [Source 1](https://github.com/m4bwav/polywright/blob/main/LICENSE) [Source 2](https://github.com/m4bwav/polywright/blob/main/README.md)

- **Code:** MIT
- **Weights:** MIT covers Polywright. Hunyuan3D-2 or another selected checkpoint and Blender, slicers and reference meshes retain separate terms.
- **Commercial:** Project code is governed by MIT. Confirm selected model, source-media and output restrictions separately.
- **Cost:** The CLI itself uses local compute. Explicit hosted generation, hardware and downloads may carry costs.

### Why it merits attention

The creative workflow is grounded in the cited documentation. Output quality and compatibility are not hands-on verified. [Source 1](https://github.com/m4bwav/polywright/blob/main/README.md)

### Limitations

Mesh validation does not certify a printable structure, topology quality or game compatibility. Model availability and cost vary independently. [Source 1](https://github.com/m4bwav/polywright/blob/main/README.md)

### Get the tool

- [Repository](https://github.com/m4bwav/polywright)
- [Documentation](https://github.com/m4bwav/polywright/blob/main/README.md)

## Multiview-to-3D Lab

3D, reconstruction & assets · Creative learning & authoring · Learned optics and post-production lens tools

This completes an earlier pending guide with a current source review.

### Quality assessment: Quality unverified

Creative use and the code grant are documented. Check-level gaps remain before a recommendation.

Scope: Compare how different reconstruction methods preserve a stylized prop’s proportions before choosing a modeling workflow.

Evidence checked: 2026-11-21. No local execution implied.

- **Open-source software license · verified:** Reviewed the complete project software grant and its redistribution conditions. Model, data and service terms are scoped separately. [Source](https://github.com/ShuyaoGao/multiview-to-3d-lab/blob/main/LICENSE)
- **Creative results · documented:** The published browser showcase explains the five routes and a 16-object synthetic benchmark. The dataset is small and does not represent arbitrary images or materials. [Source](https://github.com/ShuyaoGao/multiview-to-3d-lab/blob/main/README.md) [Source](https://github.com/ShuyaoGao/multiview-to-3d-lab/blob/main/THIRD_PARTY.md) [Source](https://shuyaogao.github.io/multiview-to-3d-lab/)
- **Reproducible setup · documented:** The installation and first-use steps are in the cited documentation. Reproduction of this workflow remains unverified. [Source](https://github.com/ShuyaoGao/multiview-to-3d-lab/blob/main/README.md) [Source](https://github.com/ShuyaoGao/multiview-to-3d-lab/blob/main/THIRD_PARTY.md) [Source](https://shuyaogao.github.io/multiview-to-3d-lab/)
- **Maintenance and support · unknown:** The reviewed sources do not establish workflow-specific support, fixes and unresolved blockers.
- **Independent use · unknown:** Independent first-hand use of the exact workflow was not established in this source review.
- **Models, services and costs · documented:** MIT covers code. Documentation and teaching materials are marked CC BY 4.0. The full third-party matrix lists separately licensed checkpoints and outputs. The showcase can be inspected without running inference. Local GPU compute and external LLM API use depend on the chosen method. [Source](https://github.com/ShuyaoGao/multiview-to-3d-lab/blob/main/README.md) [Source](https://github.com/ShuyaoGao/multiview-to-3d-lab/blob/main/THIRD_PARTY.md) [Source](https://shuyaogao.github.io/multiview-to-3d-lab/)

Source and documentation review. No hands-on execution by AI Media Scout. Synthetic benchmark results do not establish robustness for reflective, real or incomplete views. Treat it as a comparison tool and check checkpoint limitations.

### How it uses AI

The benchmark compares multiple 3D reconstruction routes from front, side and top images, including learned and LLM-assisted approaches, against known synthetic geometry. [Source](https://github.com/ShuyaoGao/multiview-to-3d-lab/blob/main/README.md) [Source](https://github.com/ShuyaoGao/multiview-to-3d-lab/blob/main/THIRD_PARTY.md) [Source](https://shuyaogao.github.io/multiview-to-3d-lab/)

### Introduction

The benchmark compares multiple 3D reconstruction routes from front, side and top images, including learned and LLM-assisted approaches, against known synthetic geometry. [Source 1](https://github.com/ShuyaoGao/multiview-to-3d-lab/blob/main/README.md) [Source 2](https://github.com/ShuyaoGao/multiview-to-3d-lab/blob/main/THIRD_PARTY.md) [Source 3](https://shuyaogao.github.io/multiview-to-3d-lab/)

### What it is good for

Compare how different reconstruction methods preserve a stylized prop’s proportions before choosing a modeling workflow. [Source 1](https://github.com/ShuyaoGao/multiview-to-3d-lab/blob/main/README.md) [Source 2](https://github.com/ShuyaoGao/multiview-to-3d-lab/blob/main/THIRD_PARTY.md) [Source 3](https://shuyaogao.github.io/multiview-to-3d-lab/)

### Demo & examples

The published browser showcase explains the five routes and a 16-object synthetic benchmark. The dataset is small and does not represent arbitrary images or materials. [Source 1](https://github.com/ShuyaoGao/multiview-to-3d-lab/blob/main/README.md) [Source 2](https://github.com/ShuyaoGao/multiview-to-3d-lab/blob/main/THIRD_PARTY.md) [Source 3](https://shuyaogao.github.io/multiview-to-3d-lab/)

### Install

Follow the documented route for the scoped workflow. The steps below are source references. [Source 1](https://github.com/ShuyaoGao/multiview-to-3d-lab/blob/main/README.md) [Source 2](https://github.com/ShuyaoGao/multiview-to-3d-lab/blob/main/THIRD_PARTY.md) [Source 3](https://shuyaogao.github.io/multiview-to-3d-lab/)

1. Start with the web showcase. For reproducing the benchmark, use the documented Windows or Linux setup, Python 3.12 and Blender 5.2.
2. Install the source requirements in an isolated environment and fetch only the weights used by the selected route under their documented terms.
### First project

A small first project makes the input, model output and handoff easy to inspect. [Source 1](https://github.com/ShuyaoGao/multiview-to-3d-lab/blob/main/README.md) [Source 2](https://github.com/ShuyaoGao/multiview-to-3d-lab/blob/main/THIRD_PARTY.md) [Source 3](https://shuyaogao.github.io/multiview-to-3d-lab/)

1. Choose one ground-truth case and inspect the paired source views and reconstruction.
2. Compare silhouette and metric differences across routes. Use the rules-based baseline with the same views before judging a learned output.
3. Keep the benchmark results tied to the selected cases. Test a production asset separately.
### Hardware & software

Platform and compute constraints refer to the selected route. [Source 1](https://github.com/ShuyaoGao/multiview-to-3d-lab/blob/main/README.md) [Source 2](https://github.com/ShuyaoGao/multiview-to-3d-lab/blob/main/THIRD_PARTY.md) [Source 3](https://shuyaogao.github.io/multiview-to-3d-lab/)

- **Hardware:** The README documents GPU use and about 40 GB of weights for routes A, B and G. The visual-hull baseline does not require a GPU. RAM and VRAM minima are undocumented.
- **Software:** Python 3.12 and Blender 5.2 for local reproduction. Learned routes use separate checkpoints. An actual Anthropic route requires provider access.
- **Platforms:** Windows and Linux local setup documented. The published showcase is a browser route, with native Mac reproduction unverified.

### License, model weights & costs

The full software license was reviewed. Dependencies and creative assets carry their own terms. [Source 1](https://github.com/ShuyaoGao/multiview-to-3d-lab/blob/main/LICENSE) [Source 2](https://github.com/ShuyaoGao/multiview-to-3d-lab/blob/main/README.md) [Source 3](https://github.com/ShuyaoGao/multiview-to-3d-lab/blob/main/THIRD_PARTY.md) [Source 4](https://shuyaogao.github.io/multiview-to-3d-lab/)

- **Code:** MIT
- **Weights:** MIT covers code. Documentation and teaching materials are marked CC BY 4.0. The full third-party matrix lists separately licensed checkpoints and outputs.
- **Commercial:** Project code is governed by MIT. Confirm selected model, source-media and output restrictions separately.
- **Cost:** The showcase can be inspected without running inference. Local GPU compute and external LLM API use depend on the chosen method.

### Why it merits attention

The creative workflow is grounded in the cited documentation. Output quality and compatibility are not hands-on verified. [Source 1](https://github.com/ShuyaoGao/multiview-to-3d-lab/blob/main/README.md) [Source 2](https://github.com/ShuyaoGao/multiview-to-3d-lab/blob/main/THIRD_PARTY.md) [Source 3](https://shuyaogao.github.io/multiview-to-3d-lab/)

### Limitations

Synthetic benchmark results do not establish robustness for reflective, real or incomplete views. Treat it as a comparison tool and check checkpoint limitations. [Source 1](https://github.com/ShuyaoGao/multiview-to-3d-lab/blob/main/README.md) [Source 2](https://github.com/ShuyaoGao/multiview-to-3d-lab/blob/main/THIRD_PARTY.md) [Source 3](https://shuyaogao.github.io/multiview-to-3d-lab/)

### Get the tool

- [Repository](https://github.com/ShuyaoGao/multiview-to-3d-lab)
- [Documentation](https://shuyaogao.github.io/multiview-to-3d-lab/)

## SyncDreamer

3D, reconstruction & assets · Photogrammetry, scanning & neural rendering · Images & design

This completes an earlier pending guide with a current source review.

### Quality assessment: Quality unverified

Creative use and the code grant are documented. Check-level gaps remain before a recommendation.

Scope: Explore a turntable-style set of generated guide images from an isolated illustration before separately fitting a production asset.

Evidence checked: 2026-11-21. No local execution implied.

- **Open-source software license · verified:** Reviewed the complete project software grant and its redistribution conditions. Model, data and service terms are scoped separately. [Source](https://github.com/liuyuan-pal/SyncDreamer/blob/main/LICENSE)
- **Creative results · documented:** The paper and project page provide views, comparison examples and evaluation methods. The authors provide a hosted demo route. Current inference availability and drawing-specific accuracy need verification. [Source](https://github.com/liuyuan-pal/SyncDreamer/blob/main/README.md) [Source](https://arxiv.org/abs/2309.03453) [Source](https://liuyuan-pal.github.io/SyncDreamer/)
- **Reproducible setup · documented:** The installation and first-use steps are in the cited documentation. Reproduction of this workflow remains unverified. [Source](https://github.com/liuyuan-pal/SyncDreamer/blob/main/README.md) [Source](https://arxiv.org/abs/2309.03453) [Source](https://liuyuan-pal.github.io/SyncDreamer/)
- **Maintenance and support · unknown:** The reviewed sources do not establish workflow-specific support, fixes and unresolved blockers.
- **Independent use · unknown:** Independent first-hand use of the exact workflow was not established in this source review.
- **Models, services and costs · documented:** MIT covers the repository software. The released checkpoint, parent weights and dataset retain separate terms. Review the selected exact artifacts before production use. Local GPU time or the hosted demo’s current capacity is required. Training has different compute and data costs. [Source](https://github.com/liuyuan-pal/SyncDreamer/blob/main/README.md) [Source](https://arxiv.org/abs/2309.03453) [Source](https://liuyuan-pal.github.io/SyncDreamer/)

Source and documentation review. No hands-on execution by AI Media Scout. Generated views are estimates, with unseen detail invented. Expected elevation and subject isolation matter. The synthetic guidance does not certify physical dimensions or mesh quality.

### How it uses AI

SyncDreamer estimates correlated rendered views from a single image with a generative model that conditions views jointly. [Source](https://github.com/liuyuan-pal/SyncDreamer/blob/main/README.md) [Source](https://arxiv.org/abs/2309.03453) [Source](https://liuyuan-pal.github.io/SyncDreamer/)

### Introduction

SyncDreamer estimates correlated rendered views from a single image with a generative model that conditions views jointly. [Source 1](https://github.com/liuyuan-pal/SyncDreamer/blob/main/README.md) [Source 2](https://arxiv.org/abs/2309.03453) [Source 3](https://liuyuan-pal.github.io/SyncDreamer/)

### What it is good for

Explore a turntable-style set of generated guide images from an isolated illustration before separately fitting a production asset. [Source 1](https://github.com/liuyuan-pal/SyncDreamer/blob/main/README.md) [Source 2](https://arxiv.org/abs/2309.03453) [Source 3](https://liuyuan-pal.github.io/SyncDreamer/)

### Demo & examples

The paper and project page provide views, comparison examples and evaluation methods. The authors provide a hosted demo route. Current inference availability and drawing-specific accuracy need verification. [Source 1](https://github.com/liuyuan-pal/SyncDreamer/blob/main/README.md) [Source 2](https://arxiv.org/abs/2309.03453) [Source 3](https://liuyuan-pal.github.io/SyncDreamer/)

### Install

Follow the documented route for the scoped workflow. The steps below are source references. [Source 1](https://github.com/liuyuan-pal/SyncDreamer/blob/main/README.md) [Source 2](https://arxiv.org/abs/2309.03453) [Source 3](https://liuyuan-pal.github.io/SyncDreamer/)

1. Use the author’s environment instructions and obtain the published checkpoint and required supporting weights under their own terms.
2. Prepare a foreground image and supply the documented elevation input. Try the low-memory inference options if needed.
### First project

A small first project makes the input, model output and handoff easy to inspect. [Source 1](https://github.com/liuyuan-pal/SyncDreamer/blob/main/README.md) [Source 2](https://arxiv.org/abs/2309.03453) [Source 3](https://liuyuan-pal.github.io/SyncDreamer/)

1. Start with a segmented object. Generate alternate views and inspect whether details around the hidden sides stay coherent.
2. Review the gallery and intermediate views before attempting the separately documented renderer or mesh route. Keep source and output versions.
### Hardware & software

Platform and compute constraints refer to the selected route. [Source 1](https://github.com/liuyuan-pal/SyncDreamer/blob/main/README.md) [Source 2](https://arxiv.org/abs/2309.03453) [Source 3](https://liuyuan-pal.github.io/SyncDreamer/)

- **Hardware:** The maintainer tested a 40 GB A100. It reports 10 GB inference and a slower reduced-batch route below that. Minimum RAM and storage are undocumented.
- **Software:** The paper implementation documents PyTorch 1.10.2 and CUDA 11.1 for its test setup. The checkpoints and optional reconstruction tooling are separate.
- **Platforms:** The cited local path is a CUDA/PyTorch research environment. Hosted demo compatibility is separate. Native Windows or macOS operation is unverified.

### License, model weights & costs

The full software license was reviewed. Dependencies and creative assets carry their own terms. [Source 1](https://github.com/liuyuan-pal/SyncDreamer/blob/main/LICENSE) [Source 2](https://github.com/liuyuan-pal/SyncDreamer/blob/main/README.md) [Source 3](https://arxiv.org/abs/2309.03453) [Source 4](https://liuyuan-pal.github.io/SyncDreamer/)

- **Code:** MIT
- **Weights:** MIT covers the repository software. The released checkpoint, parent weights and dataset retain separate terms. Review the selected exact artifacts before production use.
- **Commercial:** Project code is governed by MIT. Confirm selected model, source-media and output restrictions separately.
- **Cost:** Local GPU time or the hosted demo’s current capacity is required. Training has different compute and data costs.

### Why it merits attention

The creative workflow is grounded in the cited documentation. Output quality and compatibility are not hands-on verified. [Source 1](https://github.com/liuyuan-pal/SyncDreamer/blob/main/README.md) [Source 2](https://arxiv.org/abs/2309.03453) [Source 3](https://liuyuan-pal.github.io/SyncDreamer/)

### Limitations

Generated views are estimates, with unseen detail invented. Expected elevation and subject isolation matter. The synthetic guidance does not certify physical dimensions or mesh quality. [Source 1](https://github.com/liuyuan-pal/SyncDreamer/blob/main/README.md) [Source 2](https://arxiv.org/abs/2309.03453) [Source 3](https://liuyuan-pal.github.io/SyncDreamer/)

### Get the tool

- [Repository](https://github.com/liuyuan-pal/SyncDreamer)
- [Documentation](https://liuyuan-pal.github.io/SyncDreamer/)

## Caption Studio

Mobile, edge & on-device creation · Editing, captions & post-production · Accessible media & assistive creation

First complete guide in the library. The publication and documentation dates are not necessarily the project’s launch date.

### Quality assessment: Quality unverified

Creative use and the code grant are documented. Check-level gaps remain before a recommendation.

Scope: Correct and style draft captions on an Android phone, then export a short proof before a longer delivery.

Evidence checked: 2026-11-21. No local execution implied.

- **Open-source software license · verified:** Reviewed the complete project software grant and its redistribution conditions. Model, data and service terms are scoped separately. [Source](https://github.com/Hatsunama/Caption-Studio/blob/main/LICENSE)
- **Creative results · documented:** The current documentation explains timed captions, a preview and device-local processing. Optional translation is a distinct workflow with extra requirements. [Source](https://github.com/Hatsunama/Caption-Studio/blob/main/README.md)
- **Reproducible setup · documented:** The installation and first-use steps are in the cited documentation. Reproduction of this workflow remains unverified. [Source](https://github.com/Hatsunama/Caption-Studio/blob/main/README.md)
- **Maintenance and support · documented:** The release docs explain current APK identities and verification. Actual comparative caption accuracy remains unverified. [Source](https://github.com/Hatsunama/Caption-Studio/releases/tag/v1.4.145)
- **Independent use · unknown:** Independent first-hand use of the exact workflow was not established in this source review.
- **Models, services and costs · documented:** The full MIT software grant was reviewed. Whisper, Silero, optional Qwen translation, fonts and input media carry separate terms. The documented transcription route runs on device after model setup. The optional translation download affects storage and throughput. [Source](https://github.com/Hatsunama/Caption-Studio/blob/main/README.md)

Source and documentation review. No hands-on execution by AI Media Scout. Existing APKs may use different application IDs or change over time. Verify exact release provenance and check timings independently.

### How it uses AI

Caption Studio uses on-device Whisper recognition and Silero voice-activity detection to form editable word-timed captions for Android video. [Source](https://github.com/Hatsunama/Caption-Studio/blob/main/README.md)

### Introduction

Caption Studio uses on-device Whisper recognition and Silero voice-activity detection to form editable word-timed captions for Android video. [Source 1](https://github.com/Hatsunama/Caption-Studio/blob/main/README.md)

### What it is good for

Correct and style draft captions on an Android phone, then export a short proof before a longer delivery. [Source 1](https://github.com/Hatsunama/Caption-Studio/blob/main/README.md)

### Demo & examples

The current documentation explains timed captions, a preview and device-local processing. Optional translation is a distinct workflow with extra requirements. [Source 1](https://github.com/Hatsunama/Caption-Studio/blob/main/README.md)

### Install

Follow the documented route for the scoped workflow. The steps below are source references. [Source 1](https://github.com/Hatsunama/Caption-Studio/blob/main/README.md)

1. Select the official Android release asset and check that it uses the expected application identity and supported Android version.
2. Open the local editor and follow its initial caption model setup. Enable optional second-language processing only after reviewing its larger model.
### First project

A small first project makes the input, model output and handoff easy to inspect. [Source 1](https://github.com/Hatsunama/Caption-Studio/blob/main/README.md)

1. Import a short video and confirm the app retained access to the original file.
2. Generate draft timed captions. Check silence at the start and in the middle, edit timing and correct names.
3. Compare the exported file with the playback preview. Keep a corrected transcript separately for accessibility use.
### Hardware & software

Platform and compute constraints refer to the selected route. [Source 1](https://github.com/Hatsunama/Caption-Studio/blob/main/README.md)

- **Hardware:** The core package documents arm64-v8a, armeabi-v7a, x86 and x86_64. Translation is limited to arm64-v8a and x86_64. Minimum RAM and storage beyond model size are undocumented.
- **Software:** The universal APK requires Android 7 or newer. The extra LiteRT-LM translation route has narrower CPU architecture support and a roughly 1.6 GB Qwen download.
- **Platforms:** Android editor. A Windows helper described in the repository handles APK installation and does not run the editor.

### License, model weights & costs

The full software license was reviewed. Dependencies and creative assets carry their own terms. [Source 1](https://github.com/Hatsunama/Caption-Studio/blob/main/LICENSE) [Source 2](https://github.com/Hatsunama/Caption-Studio/blob/main/README.md)

- **Code:** MIT
- **Weights:** The full MIT software grant was reviewed. Whisper, Silero, optional Qwen translation, fonts and input media carry separate terms.
- **Commercial:** Project code is governed by MIT. Confirm selected model, source-media and output restrictions separately.
- **Cost:** The documented transcription route runs on device after model setup. The optional translation download affects storage and throughput.

### Why it merits attention

The creative workflow is grounded in the cited documentation. Output quality and compatibility are not hands-on verified. [Source 1](https://github.com/Hatsunama/Caption-Studio/blob/main/README.md)

### Limitations

Existing APKs may use different application IDs or change over time. Verify exact release provenance and check timings independently. [Source 1](https://github.com/Hatsunama/Caption-Studio/blob/main/README.md)

### Get the tool

- [Repository](https://github.com/Hatsunama/Caption-Studio)
- [Documentation](https://github.com/Hatsunama/Caption-Studio/blob/main/README.md)

## Unbagrnd

Images & design · Mobile, edge & on-device creation · Photography, restoration & color

First complete guide in the library. The publication and documentation dates are not necessarily the project’s launch date.

### Quality assessment: Quality unverified

Creative use and the code grant are documented. Check-level gaps remain before a recommendation.

Scope: Isolate a product or portrait and keep a transparent PNG for a separate composite.

Evidence checked: 2026-11-21. No local execution implied.

- **Open-source software license · verified:** Reviewed the complete project software grant and its redistribution conditions. Model, data and service terms are scoped separately. [Source](https://github.com/zidniryi/unbagrnd/blob/main/LICENSE)
- **Creative results · documented:** The upstream shows the mask and preview on supported platforms. It documents refinements and batch options. Translucent edges still need independent review. [Source](https://github.com/zidniryi/unbagrnd/blob/main/README.md)
- **Reproducible setup · documented:** The installation and first-use steps are in the cited documentation. Reproduction of this workflow remains unverified. [Source](https://github.com/zidniryi/unbagrnd/blob/main/README.md)
- **Maintenance and support · documented:** Current published release packages describe its distribution route. Independently reproduced performance remains open. [Source](https://github.com/zidniryi/unbagrnd/releases/tag/v0.6.0)
- **Independent use · unknown:** Independent first-hand use of the exact workflow was not established in this source review.
- **Models, services and costs · documented:** MIT covers the editor. The source identifies Apache-2.0 for its bundled IS-Net general-use model route. Other models and imported photos have separate terms. Local processing after acquisition avoids a required API fee. Model download and local compute still apply. [Source](https://github.com/zidniryi/unbagrnd/blob/main/README.md)

Source and documentation review. No hands-on execution by AI Media Scout. Model quality varies by subject edge and file. Unsigned package treatment and output performance vary by OS.

### How it uses AI

Unbagrnd runs neural segmentation locally through ONNX Runtime and can refine the resulting alpha mask for background removal. [Source](https://github.com/zidniryi/unbagrnd/blob/main/README.md)

### Introduction

Unbagrnd runs neural segmentation locally through ONNX Runtime and can refine the resulting alpha mask for background removal. [Source 1](https://github.com/zidniryi/unbagrnd/blob/main/README.md)

### What it is good for

Isolate a product or portrait and keep a transparent PNG for a separate composite. [Source 1](https://github.com/zidniryi/unbagrnd/blob/main/README.md)

### Demo & examples

The upstream shows the mask and preview on supported platforms. It documents refinements and batch options. Translucent edges still need independent review. [Source 1](https://github.com/zidniryi/unbagrnd/blob/main/README.md)

### Install

Follow the documented route for the scoped workflow. The steps below are source references. [Source 1](https://github.com/zidniryi/unbagrnd/blob/main/README.md)

1. Choose the matching official artifact or the documented Tauri source-build route. Check the platform’s package and signing notes.
2. Open one non-sensitive test image and select a local model, allowing only the documented one-time dependency downloads.
### First project

A small first project makes the input, model output and handoff easy to inspect. [Source 1](https://github.com/zidniryi/unbagrnd/blob/main/README.md)

1. Inspect the proposed cutout against the original. Refine around hard edges and hair with the available controls.
2. Export a transparent image and open it over light and dark backgrounds to check the compositor handoff.
### Hardware & software

Platform and compute constraints refer to the selected route. [Source 1](https://github.com/zidniryi/unbagrnd/blob/main/README.md)

- **Hardware:** Minimum RAM, VRAM and disk space for the scoped workflow are undocumented.
- **Software:** Tauri app or its source build environment, platform runtime prerequisites, ONNX Runtime and the selected compatible model.
- **Platforms:** Documentation covers macOS, Windows, Linux and Android. Check exact release artifacts and architecture requirements.

### License, model weights & costs

The full software license was reviewed. Dependencies and creative assets carry their own terms. [Source 1](https://github.com/zidniryi/unbagrnd/blob/main/LICENSE) [Source 2](https://github.com/zidniryi/unbagrnd/blob/main/README.md)

- **Code:** MIT
- **Weights:** MIT covers the editor. The source identifies Apache-2.0 for its bundled IS-Net general-use model route. Other models and imported photos have separate terms.
- **Commercial:** Project code is governed by MIT. Confirm selected model, source-media and output restrictions separately.
- **Cost:** Local processing after acquisition avoids a required API fee. Model download and local compute still apply.

### Why it merits attention

The creative workflow is grounded in the cited documentation. Output quality and compatibility are not hands-on verified. [Source 1](https://github.com/zidniryi/unbagrnd/blob/main/README.md)

### Limitations

Model quality varies by subject edge and file. Unsigned package treatment and output performance vary by OS. [Source 1](https://github.com/zidniryi/unbagrnd/blob/main/README.md)

### Get the tool

- [Repository](https://github.com/zidniryi/unbagrnd)
- [Documentation](https://github.com/zidniryi/unbagrnd/blob/main/README.md)

## Transcribe

Mobile, edge & on-device creation · Editing, captions & post-production · Audio, music & voice

First complete guide in the library. The publication and documentation dates are not necessarily the project’s launch date.

### Quality assessment: Quality unverified

Creative use and the code grant are documented. Check-level gaps remain before a recommendation.

Scope: Make a draft subtitle file from a local recording on a compatible platform and use it in a separate editor.

Evidence checked: 2026-11-21. No local execution implied.

- **Open-source software license · verified:** Reviewed the complete project software grant and its redistribution conditions. Model, data and service terms are scoped separately. [Source](https://github.com/morethancoder/transcribe/blob/main/LICENSE)
- **Creative results · documented:** The source documents a local web service as well as native Tauri packages. Mobile builds and local desktop runtimes use different setup routes. [Source](https://github.com/morethancoder/transcribe/blob/main/README.md) [Source](https://github.com/morethancoder/transcribe/blob/main/docs/MOBILE.md)
- **Reproducible setup · documented:** The installation and first-use steps are in the cited documentation. Reproduction of this workflow remains unverified. [Source](https://github.com/morethancoder/transcribe/blob/main/README.md) [Source](https://github.com/morethancoder/transcribe/blob/main/docs/MOBILE.md)
- **Maintenance and support · documented:** Published distribution and separate mobile documentation were reviewed. Cross-device transcription accuracy and setup repetition remain open. [Source](https://github.com/morethancoder/transcribe/releases/tag/v0.4.0)
- **Independent use · unknown:** Independent first-hand use of the exact workflow was not established in this source review.
- **Models, services and costs · documented:** MIT covers Transcribe. whisper.cpp, the selected weights, OS distribution tools and recording rights remain separate. The documented transcription runs on-device. Local compute and model downloads apply. No per-minute API is required for the scoped workflow. [Source](https://github.com/morethancoder/transcribe/blob/main/README.md) [Source](https://github.com/morethancoder/transcribe/blob/main/docs/MOBILE.md)

Source and documentation review. No hands-on execution by AI Media Scout. Platform paths differ in device/accelerator access and distribution. Test exact timestamps and codec support before relying on a workflow.

### How it uses AI

Transcribe runs whisper.cpp on audio from supported media and produces timestamped material for text or SRT output. [Source](https://github.com/morethancoder/transcribe/blob/main/README.md) [Source](https://github.com/morethancoder/transcribe/blob/main/docs/MOBILE.md)

### Introduction

Transcribe runs whisper.cpp on audio from supported media and produces timestamped material for text or SRT output. [Source 1](https://github.com/morethancoder/transcribe/blob/main/README.md) [Source 2](https://github.com/morethancoder/transcribe/blob/main/docs/MOBILE.md)

### What it is good for

Make a draft subtitle file from a local recording on a compatible platform and use it in a separate editor. [Source 1](https://github.com/morethancoder/transcribe/blob/main/README.md) [Source 2](https://github.com/morethancoder/transcribe/blob/main/docs/MOBILE.md)

### Demo & examples

The source documents a local web service as well as native Tauri packages. Mobile builds and local desktop runtimes use different setup routes. [Source 1](https://github.com/morethancoder/transcribe/blob/main/README.md) [Source 2](https://github.com/morethancoder/transcribe/blob/main/docs/MOBILE.md)

### Install

Follow the documented route for the scoped workflow. The steps below are source references. [Source 1](https://github.com/morethancoder/transcribe/blob/main/README.md) [Source 2](https://github.com/morethancoder/transcribe/blob/main/docs/MOBILE.md)

1. Choose a published desktop/Android package or the documented web service. For the web route prepare Node, FFmpeg, whisper-cli and the selected model using the OS-specific instructions.
2. Use the iOS source-build instructions and Apple tooling only for that route. Verify file import with the intended app build.
### First project

A small first project makes the input, model output and handoff easy to inspect. [Source 1](https://github.com/morethancoder/transcribe/blob/main/README.md) [Source 2](https://github.com/morethancoder/transcribe/blob/main/docs/MOBILE.md)

1. Open a short audio or video clip and select a model and language.
2. Listen alongside the result and adjust names and cue boundaries. Export SRT and import it into a separate editing timeline.
### Hardware & software

Platform and compute constraints refer to the selected route. [Source 1](https://github.com/morethancoder/transcribe/blob/main/README.md) [Source 2](https://github.com/morethancoder/transcribe/blob/main/docs/MOBILE.md)

- **Hardware:** Minimum RAM, VRAM and disk space for the scoped workflow are undocumented.
- **Software:** Source-based local web route uses Node, FFmpeg, whisper-cli and model files. Native apps use Tauri. The optional iOS build needs Apple provisioning and the documented source tooling.
- **Platforms:** The project documents macOS, Windows and Linux local routes, Tauri desktop and Android distribution, and a source-build path for iOS.

### License, model weights & costs

The full software license was reviewed. Dependencies and creative assets carry their own terms. [Source 1](https://github.com/morethancoder/transcribe/blob/main/LICENSE) [Source 2](https://github.com/morethancoder/transcribe/blob/main/README.md) [Source 3](https://github.com/morethancoder/transcribe/blob/main/docs/MOBILE.md)

- **Code:** MIT
- **Weights:** MIT covers Transcribe. whisper.cpp, the selected weights, OS distribution tools and recording rights remain separate.
- **Commercial:** Project code is governed by MIT. Confirm selected model, source-media and output restrictions separately.
- **Cost:** The documented transcription runs on-device. Local compute and model downloads apply. No per-minute API is required for the scoped workflow.

### Why it merits attention

The creative workflow is grounded in the cited documentation. Output quality and compatibility are not hands-on verified. [Source 1](https://github.com/morethancoder/transcribe/blob/main/README.md) [Source 2](https://github.com/morethancoder/transcribe/blob/main/docs/MOBILE.md)

### Limitations

Platform paths differ in device/accelerator access and distribution. Test exact timestamps and codec support before relying on a workflow. [Source 1](https://github.com/morethancoder/transcribe/blob/main/README.md) [Source 2](https://github.com/morethancoder/transcribe/blob/main/docs/MOBILE.md)

### Get the tool

- [Repository](https://github.com/morethancoder/transcribe)
- [Documentation](https://github.com/morethancoder/transcribe/blob/main/docs/MOBILE.md)

## Pulse Camera

Mobile, edge & on-device creation · Video, animation & film · Accessible media & assistive creation

First complete guide in the library. The publication and documentation dates are not necessarily the project’s launch date.

### Quality assessment: Quality unverified

Creative use and the code grant are documented. Check-level gaps remain before a recommendation.

Scope: Record and caption a segmented phone walkthrough, edit the cues and export or share an editable handoff.

Evidence checked: 2026-11-21. No local execution implied.

- **Open-source software license · verified:** Reviewed the complete project software grant and its redistribution conditions. Model, data and service terms are scoped separately. [Source](https://github.com/mieweb/pulse/blob/main/LICENSE)
- **Creative results · documented:** The maintainer documents the iOS and Android build paths and Android parity checks, including captioning. The scoped first workflow uses a short clip and offline captions. [Source](https://github.com/mieweb/pulse/blob/main/README.md)
- **Reproducible setup · documented:** The installation and first-use steps are in the cited documentation. Reproduction of this workflow remains unverified. [Source](https://github.com/mieweb/pulse/blob/main/README.md)
- **Maintenance and support · documented:** The current source identifies post-import, caption and upload behavior per platform. A project-specific reproduction remains open. [Source](https://github.com/mieweb/pulse/releases/tag/pulsekit-v0.1.0-rc.4)
- **Independent use · unknown:** Independent first-hand use of the exact workflow was not established in this source review.
- **Models, services and costs · documented:** MIT covers the app. The selected Whisper or other speech model, media, and any hosted server terms are separate. Authoring and the selected recognition route use device resources. Optional self-hosted upload adds server and storage costs. [Source](https://github.com/mieweb/pulse/blob/main/README.md)

Source and documentation review. No hands-on execution by AI Media Scout. Model speed, timing and stabilization differ by platform and device. Dated source checks are maintainer evidence.

### How it uses AI

Pulse uses on-device speech recognition to derive caption timing for recorded clips, then carries the caption data with trims, speeds and reorder operations in the editor. [Source](https://github.com/mieweb/pulse/blob/main/README.md)

### Introduction

Pulse uses on-device speech recognition to derive caption timing for recorded clips, then carries the caption data with trims, speeds and reorder operations in the editor. [Source 1](https://github.com/mieweb/pulse/blob/main/README.md)

### What it is good for

Record and caption a segmented phone walkthrough, edit the cues and export or share an editable handoff. [Source 1](https://github.com/mieweb/pulse/blob/main/README.md)

### Demo & examples

The maintainer documents the iOS and Android build paths and Android parity checks, including captioning. The scoped first workflow uses a short clip and offline captions. [Source 1](https://github.com/mieweb/pulse/blob/main/README.md)

### Install

Follow the documented route for the scoped workflow. The steps below are source references. [Source 1](https://github.com/mieweb/pulse/blob/main/README.md)

1. Use the official iOS or Android distribution or follow the current Expo build instructions. Choose a speech model available for the installed build.
2. Download the model in the editor’s Captions tool. Configure a self-host server only when the intended project needs upload.
### First project

A small first project makes the input, model output and handoff easy to inspect. [Source 1](https://github.com/mieweb/pulse/blob/main/README.md)

1. Record two short segments and trim/reorder them. Generate caption drafts per clip.
2. Review text and timing after the edits, correcting speaker terminology. Export a preview or a .pulse handoff and compare the result with the playback timeline.
### Hardware & software

Platform and compute constraints refer to the selected route. [Source 1](https://github.com/mieweb/pulse/blob/main/README.md)

- **Hardware:** Minimum RAM, VRAM and disk space for the scoped workflow are undocumented.
- **Software:** Documented React Native/Expo app and device speech model via whisper.rn. Published paths name differing Whisper variants and the current English route. Optional PulseVault upload needs its own server setup.
- **Platforms:** iOS and Android native clients. The repository documents Metal Whisper acceleration on iOS and CPU on Android. High cinematic stabilization is iOS-specific.

### License, model weights & costs

The full software license was reviewed. Dependencies and creative assets carry their own terms. [Source 1](https://github.com/mieweb/pulse/blob/main/LICENSE) [Source 2](https://github.com/mieweb/pulse/blob/main/README.md)

- **Code:** MIT
- **Weights:** MIT covers the app. The selected Whisper or other speech model, media, and any hosted server terms are separate.
- **Commercial:** Project code is governed by MIT. Confirm selected model, source-media and output restrictions separately.
- **Cost:** Authoring and the selected recognition route use device resources. Optional self-hosted upload adds server and storage costs.

### Why it merits attention

The creative workflow is grounded in the cited documentation. Output quality and compatibility are not hands-on verified. [Source 1](https://github.com/mieweb/pulse/blob/main/README.md)

### Limitations

Model speed, timing and stabilization differ by platform and device. Dated source checks are maintainer evidence. [Source 1](https://github.com/mieweb/pulse/blob/main/README.md)

### Get the tool

- [Repository](https://github.com/mieweb/pulse)
- [Documentation](https://github.com/mieweb/pulse/blob/main/README.md)

## Swift Speech Transcriber

Mobile, edge & on-device creation · Audio, music & voice · Editing, captions & post-production

First complete guide in the library. The publication and documentation dates are not necessarily the project’s launch date.

### Quality assessment: Quality unverified

Creative use and the code grant are documented. Check-level gaps remain before a recommendation.

Scope: Integrate editable SRT or VTT drafts into a Mac/iOS media application while keeping local recordings in the app’s workflow.

Evidence checked: 2026-11-21. No local execution implied.

- **Open-source software license · verified:** Reviewed the complete project software grant and its redistribution conditions. Model, data and service terms are scoped separately. [Source](https://github.com/arraypress/swift-speech-transcriber/blob/main/LICENSE)
- **Creative results · documented:** The developer supplies separate Apple and Whisper examples, timestamped export and locale management. A finished user-facing app or independent performance comparison is not part of this package. [Source](https://github.com/arraypress/swift-speech-transcriber/blob/main/README.md) [Source](https://developer.apple.com/documentation/speech/speechanalyzer)
- **Reproducible setup · documented:** The installation and first-use steps are in the cited documentation. Reproduction of this workflow remains unverified. [Source](https://github.com/arraypress/swift-speech-transcriber/blob/main/README.md) [Source](https://developer.apple.com/documentation/speech/speechanalyzer)
- **Maintenance and support · unknown:** The reviewed sources do not establish workflow-specific support, fixes and unresolved blockers.
- **Independent use · unknown:** Independent first-hand use of the exact workflow was not established in this source review.
- **Models, services and costs · documented:** MIT covers the package. Apple platform APIs, WhisperKit and particular model cards retain separate terms and platform conditions. Inference is documented as local after model/locale setup. Developer tooling, device and storage remain separate. [Source](https://github.com/arraypress/swift-speech-transcriber/blob/main/README.md) [Source](https://developer.apple.com/documentation/speech/speechanalyzer)

Source and documentation review. No hands-on execution by AI Media Scout. Timestamp behavior and locale coverage depend on the backend. Remote file inputs and language model acquisition have separate network paths.

### How it uses AI

The Swift package converts audio, video or microphone input to timestamped speech segments through Apple SpeechAnalyzer or an optional WhisperKit backend. [Source](https://github.com/arraypress/swift-speech-transcriber/blob/main/README.md) [Source](https://developer.apple.com/documentation/speech/speechanalyzer)

### Introduction

The Swift package converts audio, video or microphone input to timestamped speech segments through Apple SpeechAnalyzer or an optional WhisperKit backend. [Source 1](https://github.com/arraypress/swift-speech-transcriber/blob/main/README.md) [Source 2](https://developer.apple.com/documentation/speech/speechanalyzer)

### What it is good for

Integrate editable SRT or VTT drafts into a Mac/iOS media application while keeping local recordings in the app’s workflow. [Source 1](https://github.com/arraypress/swift-speech-transcriber/blob/main/README.md) [Source 2](https://developer.apple.com/documentation/speech/speechanalyzer)

### Demo & examples

The developer supplies separate Apple and Whisper examples, timestamped export and locale management. A finished user-facing app or independent performance comparison is not part of this package. [Source 1](https://github.com/arraypress/swift-speech-transcriber/blob/main/README.md) [Source 2](https://developer.apple.com/documentation/speech/speechanalyzer)

### Install

Follow the documented route for the scoped workflow. The steps below are source references. [Source 1](https://github.com/arraypress/swift-speech-transcriber/blob/main/README.md) [Source 2](https://developer.apple.com/documentation/speech/speechanalyzer)

1. Use the stated macOS 26 or iOS 26 SDK and add the package to an existing Swift project.
2. Choose Apple’s speech framework or the documented WhisperKit alternative and install the relevant locale or model.
### First project

A small first project makes the input, model output and handoff easy to inspect. [Source 1](https://github.com/arraypress/swift-speech-transcriber/blob/main/README.md) [Source 2](https://developer.apple.com/documentation/speech/speechanalyzer)

1. Start with one approved file and export structured dialogue segments. Inspect sentence or word timing using the selected engine.
2. Export a subtitle file and test it against the media timeline. Confirm the chosen language models and any speech permission behavior in the app.
### Hardware & software

Platform and compute constraints refer to the selected route. [Source 1](https://github.com/arraypress/swift-speech-transcriber/blob/main/README.md) [Source 2](https://developer.apple.com/documentation/speech/speechanalyzer)

- **Hardware:** Minimum RAM, VRAM and disk space for the scoped workflow are undocumented.
- **Software:** macOS 26/iOS 26 Swift platform framework, or optional WhisperKit and a permitted selected model. Use the SDK matching the deployment.
- **Platforms:** macOS 26+ and iOS 26+ documented. Windows and Linux are outside this Swift framework route.

### License, model weights & costs

The full software license was reviewed. Dependencies and creative assets carry their own terms. [Source 1](https://github.com/arraypress/swift-speech-transcriber/blob/main/LICENSE) [Source 2](https://github.com/arraypress/swift-speech-transcriber/blob/main/README.md) [Source 3](https://developer.apple.com/documentation/speech/speechanalyzer)

- **Code:** MIT
- **Weights:** MIT covers the package. Apple platform APIs, WhisperKit and particular model cards retain separate terms and platform conditions.
- **Commercial:** Project code is governed by MIT. Confirm selected model, source-media and output restrictions separately.
- **Cost:** Inference is documented as local after model/locale setup. Developer tooling, device and storage remain separate.

### Why it merits attention

The creative workflow is grounded in the cited documentation. Output quality and compatibility are not hands-on verified. [Source 1](https://github.com/arraypress/swift-speech-transcriber/blob/main/README.md) [Source 2](https://developer.apple.com/documentation/speech/speechanalyzer)

### Limitations

Timestamp behavior and locale coverage depend on the backend. Remote file inputs and language model acquisition have separate network paths. [Source 1](https://github.com/arraypress/swift-speech-transcriber/blob/main/README.md) [Source 2](https://developer.apple.com/documentation/speech/speechanalyzer)

### Get the tool

- [Repository](https://github.com/arraypress/swift-speech-transcriber)
- [Documentation](https://developer.apple.com/documentation/speech/speechanalyzer)

## SDAI

Mobile, edge & on-device creation · Images & design · Photography, restoration & color

First complete guide in the library. The publication and documentation dates are not necessarily the project’s launch date.

### Quality assessment: Quality unverified

Creative use and the code grant are documented. Check-level gaps remain before a recommendation.

Scope: Sketch an image reference on a mobile device, compare generation settings and export selected studies for later editing.

Evidence checked: 2026-11-21. No local execution implied.

- **Open-source software license · verified:** Reviewed the complete project software grant and its redistribution conditions. Model, data and service terms are scoped separately. [Source](https://github.com/ShiftHackZ/SDAI-KMP/blob/master/LICENSE)
- **Creative results · documented:** Store listings and the author’s platform matrix document on-device and server-backed options. The author identifies Bonsai routes with device-specific preview limitations. The scoped workflow uses the separate Core ML or Android SDXL route. [Source](https://github.com/ShiftHackZ/SDAI-KMP/blob/master/README.md) [Source](https://sdai.moroz.cc/) [Source](https://f-droid.org/en/packages/com.shifthackz.aisdv1.app.foss/) [Source](https://apps.apple.com/us/app/sdai-ai-image-generator/id6778314183)
- **Reproducible setup · documented:** The installation and first-use steps are in the cited documentation. Reproduction of this workflow remains unverified. [Source](https://github.com/ShiftHackZ/SDAI-KMP/blob/master/README.md) [Source](https://sdai.moroz.cc/) [Source](https://f-droid.org/en/packages/com.shifthackz.aisdv1.app.foss/) [Source](https://apps.apple.com/us/app/sdai-ai-image-generator/id6778314183)
- **Maintenance and support · documented:** Both stores list 1.2.0 in the captured documentation. GitHub also publishes a moving nightly, which is a separate artifact. [Source](https://github.com/ShiftHackZ/SDAI-KMP/releases/tag/nightly)
- **Independent use · unknown:** Independent first-hand use of the exact workflow was not established in this source review.
- **Models, services and costs · documented:** The project declares AGPL-3.0-only for its application. Stable Diffusion model cards, runtime components and any remote provider terms differ by route. Local generation uses a model download, device storage and compute. Remote services can have separate fees. [Source](https://github.com/ShiftHackZ/SDAI-KMP/blob/master/README.md) [Source](https://sdai.moroz.cc/) [Source](https://f-droid.org/en/packages/com.shifthackz.aisdv1.app.foss/) [Source](https://apps.apple.com/us/app/sdai-ai-image-generator/id6778314183)

Source and documentation review. No hands-on execution by AI Media Scout. Benchmark the chosen on-device provider and model size. The README distinguishes current preview states for Bonsai from other documented paths. This report uses the store edition as its scope.

### How it uses AI

SDAI brings a shared diffusion workspace to iOS and Android. The documented local paths include iOS Core ML and Android stable-diffusion.cpp SDXL. The app retains prompts, seeds and provider settings with images. [Source](https://github.com/ShiftHackZ/SDAI-KMP/blob/master/README.md) [Source](https://sdai.moroz.cc/) [Source](https://f-droid.org/en/packages/com.shifthackz.aisdv1.app.foss/) [Source](https://apps.apple.com/us/app/sdai-ai-image-generator/id6778314183)

### Introduction

SDAI brings a shared diffusion workspace to iOS and Android. The documented local paths include iOS Core ML and Android stable-diffusion.cpp SDXL. The app retains prompts, seeds and provider settings with images. [Source 1](https://github.com/ShiftHackZ/SDAI-KMP/blob/master/README.md) [Source 2](https://sdai.moroz.cc/) [Source 3](https://f-droid.org/en/packages/com.shifthackz.aisdv1.app.foss/) [Source 4](https://apps.apple.com/us/app/sdai-ai-image-generator/id6778314183)

### What it is good for

Sketch an image reference on a mobile device, compare generation settings and export selected studies for later editing. [Source 1](https://github.com/ShiftHackZ/SDAI-KMP/blob/master/README.md) [Source 2](https://sdai.moroz.cc/) [Source 3](https://f-droid.org/en/packages/com.shifthackz.aisdv1.app.foss/) [Source 4](https://apps.apple.com/us/app/sdai-ai-image-generator/id6778314183)

### Demo & examples

Store listings and the author’s platform matrix document on-device and server-backed options. The author identifies Bonsai routes with device-specific preview limitations. The scoped workflow uses the separate Core ML or Android SDXL route. [Source 1](https://github.com/ShiftHackZ/SDAI-KMP/blob/master/README.md) [Source 2](https://sdai.moroz.cc/) [Source 3](https://f-droid.org/en/packages/com.shifthackz.aisdv1.app.foss/) [Source 4](https://apps.apple.com/us/app/sdai-ai-image-generator/id6778314183)

### Install

Follow the documented route for the scoped workflow. The steps below are source references. [Source 1](https://github.com/ShiftHackZ/SDAI-KMP/blob/master/README.md) [Source 2](https://sdai.moroz.cc/) [Source 3](https://f-droid.org/en/packages/com.shifthackz.aisdv1.app.foss/) [Source 4](https://apps.apple.com/us/app/sdai-ai-image-generator/id6778314183)

1. Use the versioned iOS App Store or Android F-Droid distribution. Compare the selected platform and distribution flavor with the provider matrix.
2. For on-device use choose a compatible model for the selected runtime. Review its displayed size, terms and device benchmark before a batch.
### First project

A small first project makes the input, model output and handoff easy to inspect. [Source 1](https://github.com/ShiftHackZ/SDAI-KMP/blob/master/README.md) [Source 2](https://sdai.moroz.cc/) [Source 3](https://f-droid.org/en/packages/com.shifthackz.aisdv1.app.foss/) [Source 4](https://apps.apple.com/us/app/sdai-ai-image-generator/id6778314183)

1. Try a small generation with a clear prompt and stable seed. Compare which settings the provider actually honors.
2. Review the gallery alongside the input image or reference instructions. Save the selected image plus parameters for iteration.
3. Export the chosen studies and keep a source log of the model, runtime and file version.
### Hardware & software

Platform and compute constraints refer to the selected route. [Source 1](https://github.com/ShiftHackZ/SDAI-KMP/blob/master/README.md) [Source 2](https://sdai.moroz.cc/) [Source 3](https://f-droid.org/en/packages/com.shifthackz.aisdv1.app.foss/) [Source 4](https://apps.apple.com/us/app/sdai-ai-image-generator/id6778314183)

- **Hardware:** The F-Droid package lists Android 7.0 minimum and the App Store lists iOS 17.0 minimum. These are package requirements. The selected local model needs a separate device-fit check.
- **Software:** SDAI 1.2.0 store package. Local operation needs a compatible model archive for its Android or iOS runtime. Server-backed workflows require separate endpoints.
- **Platforms:** Android and iOS packages are documented. Local provider availability differs between the FOSS, full, Play and iOS distributions.

### License, model weights & costs

The full software license was reviewed. Dependencies and creative assets carry their own terms. [Source 1](https://github.com/ShiftHackZ/SDAI-KMP/blob/master/LICENSE) [Source 2](https://github.com/ShiftHackZ/SDAI-KMP/blob/master/README.md) [Source 3](https://sdai.moroz.cc/) [Source 4](https://f-droid.org/en/packages/com.shifthackz.aisdv1.app.foss/) [Source 5](https://apps.apple.com/us/app/sdai-ai-image-generator/id6778314183)

- **Code:** AGPL-3.0-only
- **Weights:** The project declares AGPL-3.0-only for its application. Stable Diffusion model cards, runtime components and any remote provider terms differ by route.
- **Commercial:** Project code is governed by AGPL-3.0-only. Confirm selected model, source-media and output restrictions separately.
- **Cost:** Local generation uses a model download, device storage and compute. Remote services can have separate fees.

### Why it merits attention

The creative workflow is grounded in the cited documentation. Output quality and compatibility are not hands-on verified. [Source 1](https://github.com/ShiftHackZ/SDAI-KMP/blob/master/README.md) [Source 2](https://sdai.moroz.cc/) [Source 3](https://f-droid.org/en/packages/com.shifthackz.aisdv1.app.foss/) [Source 4](https://apps.apple.com/us/app/sdai-ai-image-generator/id6778314183)

### Limitations

Benchmark the chosen on-device provider and model size. The README distinguishes current preview states for Bonsai from other documented paths. This report uses the store edition as its scope. [Source 1](https://github.com/ShiftHackZ/SDAI-KMP/blob/master/README.md) [Source 2](https://sdai.moroz.cc/) [Source 3](https://f-droid.org/en/packages/com.shifthackz.aisdv1.app.foss/) [Source 4](https://apps.apple.com/us/app/sdai-ai-image-generator/id6778314183)

### Get the tool

- [Repository](https://github.com/ShiftHackZ/SDAI-KMP)
- [Documentation](https://apps.apple.com/us/app/sdai-ai-image-generator/id6778314183)

## Open Body Tracker

Motion capture & character animation · Photogrammetry, scanning & neural rendering · Performance, projection & stage media

Compared v0.1.0 and v0.3.0 across ten upstream commits. The release adds an INT8 CPU workflow and per-model comparison and changes the maintainer’s declared terms for downloaded weights and teacher labels.

### Quality assessment: Quality unverified

Creative use and the code grant are documented. Check-level gaps remain before a recommendation.

Scope: Try CPU-based performer tracking for an interactive installation or a motion reference. Inspect confidence, timing and camera alignment before driving a cue.

Evidence checked: 2026-11-21. No local execution implied.

- **Open-source software license · verified:** Reviewed the complete project software grant and its redistribution conditions. Model, data and service terms are scoped separately. [Source](https://github.com/yuru-lab/open-body-tracker/blob/main/LICENSE)
- **Creative results · documented:** The author reports 46 ms per person for INT8 versus 103 ms for the unquantized CPU model on a Core i5-12600 with four ONNX Runtime threads. The release reports slightly different 3D benchmark errors and documents conditions. [Source](https://github.com/yuru-lab/open-body-tracker/blob/main/README.md) [Source](https://github.com/yuru-lab/open-body-tracker/releases/tag/v0.3.0) [Source](https://github.com/yuru-lab/open-body-tracker/blob/main/docs/MODELS.md) [Source](https://github.com/yuru-lab/open-body-tracker/blob/main/docs/LICENSING.md)
- **Reproducible setup · documented:** The installation and first-use steps are in the cited documentation. Reproduction of this workflow remains unverified. [Source](https://github.com/yuru-lab/open-body-tracker/blob/main/README.md) [Source](https://github.com/yuru-lab/open-body-tracker/releases/tag/v0.3.0) [Source](https://github.com/yuru-lab/open-body-tracker/blob/main/docs/MODELS.md) [Source](https://github.com/yuru-lab/open-body-tracker/blob/main/docs/LICENSING.md)
- **Maintenance and support · documented:** The archived v0.1.0-to-v0.3.0 comparison shows ten commits. The new preset and accompanying benchmarks materially change the documented CPU workflow. [Source](https://github.com/yuru-lab/open-body-tracker/releases/tag/v0.3.0)
- **Independent use · unknown:** Independent first-hand use of the exact workflow was not established in this source review.
- **Models, services and costs · documented:** The software is Apache-2.0. The maintainer declares the current model weights and teacher labels Apache-2.0 and acknowledges unresolved interpretation of the upstream SAM license. Check the precise checkpoint and labels before redistribution. The CPU route runs locally after downloading the model, subject to hardware and model storage. [Source](https://github.com/yuru-lab/open-body-tracker/blob/main/README.md) [Source](https://github.com/yuru-lab/open-body-tracker/releases/tag/v0.3.0) [Source](https://github.com/yuru-lab/open-body-tracker/blob/main/docs/MODELS.md) [Source](https://github.com/yuru-lab/open-body-tracker/blob/main/docs/LICENSING.md)

Source and documentation review. No hands-on execution by AI Media Scout. Single-person CPU timings are author measurements. Camera axis conventions and hip-relative output need conversion for a particular cue or rig. Derivative-model licensing interpretation remains open.

### How it uses AI

Open Body Tracker detects people and predicts body keypoints and hip-centered 3D coordinates from images. Version 0.3.0 adds a quantized ONNX CPU model for faster single-person tracking. [Source](https://github.com/yuru-lab/open-body-tracker/blob/main/README.md) [Source](https://github.com/yuru-lab/open-body-tracker/releases/tag/v0.3.0) [Source](https://github.com/yuru-lab/open-body-tracker/blob/main/docs/MODELS.md) [Source](https://github.com/yuru-lab/open-body-tracker/blob/main/docs/LICENSING.md)

### Introduction

Open Body Tracker detects people and predicts body keypoints and hip-centered 3D coordinates from images. Version 0.3.0 adds a quantized ONNX CPU model for faster single-person tracking. [Source 1](https://github.com/yuru-lab/open-body-tracker/blob/main/README.md) [Source 2](https://github.com/yuru-lab/open-body-tracker/releases/tag/v0.3.0) [Source 3](https://github.com/yuru-lab/open-body-tracker/blob/main/docs/MODELS.md) [Source 4](https://github.com/yuru-lab/open-body-tracker/blob/main/docs/LICENSING.md)

### What it is good for

Try CPU-based performer tracking for an interactive installation or a motion reference. Inspect confidence, timing and camera alignment before driving a cue. [Source 1](https://github.com/yuru-lab/open-body-tracker/blob/main/README.md) [Source 2](https://github.com/yuru-lab/open-body-tracker/releases/tag/v0.3.0) [Source 3](https://github.com/yuru-lab/open-body-tracker/blob/main/docs/MODELS.md) [Source 4](https://github.com/yuru-lab/open-body-tracker/blob/main/docs/LICENSING.md)

### Demo & examples

The author reports 46 ms per person for INT8 versus 103 ms for the unquantized CPU model on a Core i5-12600 with four ONNX Runtime threads. The release reports slightly different 3D benchmark errors and documents conditions. [Source 1](https://github.com/yuru-lab/open-body-tracker/blob/main/README.md) [Source 2](https://github.com/yuru-lab/open-body-tracker/releases/tag/v0.3.0) [Source 3](https://github.com/yuru-lab/open-body-tracker/blob/main/docs/MODELS.md) [Source 4](https://github.com/yuru-lab/open-body-tracker/blob/main/docs/LICENSING.md)

### Install

Follow the documented route for the scoped workflow. The steps below are source references. [Source 1](https://github.com/yuru-lab/open-body-tracker/blob/main/README.md) [Source 2](https://github.com/yuru-lab/open-body-tracker/releases/tag/v0.3.0) [Source 3](https://github.com/yuru-lab/open-body-tracker/blob/main/docs/MODELS.md) [Source 4](https://github.com/yuru-lab/open-body-tracker/blob/main/docs/LICENSING.md)

1. Use the source’s Python 3.12 and uv environment or its documented mise setup. Fetch the v0.3.0 INT8 model and supported detector through the project.
2. Use an authorized still or webcam test first. Compare the published model and library versions before adding a downstream observer.
### First project

A small first project makes the input, model output and handoff easy to inspect. [Source 1](https://github.com/yuru-lab/open-body-tracker/blob/main/README.md) [Source 2](https://github.com/yuru-lab/open-body-tracker/releases/tag/v0.3.0) [Source 3](https://github.com/yuru-lab/open-body-tracker/blob/main/docs/MODELS.md) [Source 4](https://github.com/yuru-lab/open-body-tracker/blob/main/docs/LICENSING.md)

1. Observe keypoints and confidence for a controlled movement. Check how handoff, distance and occlusion change the signal.
2. Inspect the 23 image and hip-centered joints and map only the needed values to your own cue or character test.
3. Measure update rate and lag on the actual hardware. Retain manual cue control for a performance.
### Hardware & software

Platform and compute constraints refer to the selected route. [Source 1](https://github.com/yuru-lab/open-body-tracker/blob/main/README.md) [Source 2](https://github.com/yuru-lab/open-body-tracker/releases/tag/v0.3.0) [Source 3](https://github.com/yuru-lab/open-body-tracker/blob/main/docs/MODELS.md) [Source 4](https://github.com/yuru-lab/open-body-tracker/blob/main/docs/LICENSING.md)

- **Hardware:** Minimum RAM, VRAM and disk space for the scoped workflow are undocumented.
- **Software:** The documented Python 3.12 and uv environment, ONNX Runtime and selected model/detector assets. The CUDA path is optional.
- **Platforms:** The project documents CPU, CUDA and a separate browser demo. A verified OS/device matrix was not established.

### License, model weights & costs

The full software license was reviewed. Dependencies and creative assets carry their own terms. [Source 1](https://github.com/yuru-lab/open-body-tracker/blob/main/LICENSE) [Source 2](https://github.com/yuru-lab/open-body-tracker/blob/main/README.md) [Source 3](https://github.com/yuru-lab/open-body-tracker/releases/tag/v0.3.0) [Source 4](https://github.com/yuru-lab/open-body-tracker/blob/main/docs/MODELS.md) [Source 5](https://github.com/yuru-lab/open-body-tracker/blob/main/docs/LICENSING.md)

- **Code:** Apache-2.0
- **Weights:** The software is Apache-2.0. The maintainer declares the current model weights and teacher labels Apache-2.0 and acknowledges unresolved interpretation of the upstream SAM license. Check the precise checkpoint and labels before redistribution.
- **Commercial:** Project code is governed by Apache-2.0. Confirm selected model, source-media and output restrictions separately.
- **Cost:** The CPU route runs locally after downloading the model, subject to hardware and model storage.

### Why it merits attention

The creative workflow is grounded in the cited documentation. Output quality and compatibility are not hands-on verified. [Source 1](https://github.com/yuru-lab/open-body-tracker/blob/main/README.md) [Source 2](https://github.com/yuru-lab/open-body-tracker/releases/tag/v0.3.0) [Source 3](https://github.com/yuru-lab/open-body-tracker/blob/main/docs/MODELS.md) [Source 4](https://github.com/yuru-lab/open-body-tracker/blob/main/docs/LICENSING.md)

### Limitations

Single-person CPU timings are author measurements. Camera axis conventions and hip-relative output need conversion for a particular cue or rig. Derivative-model licensing interpretation remains open. [Source 1](https://github.com/yuru-lab/open-body-tracker/blob/main/README.md) [Source 2](https://github.com/yuru-lab/open-body-tracker/releases/tag/v0.3.0) [Source 3](https://github.com/yuru-lab/open-body-tracker/blob/main/docs/MODELS.md) [Source 4](https://github.com/yuru-lab/open-body-tracker/blob/main/docs/LICENSING.md)

### Get the tool

- [Repository](https://github.com/yuru-lab/open-body-tracker)
- [Documentation](https://github.com/yuru-lab/open-body-tracker/blob/main/docs/LICENSING.md)

## Who Plays What

Audio, music & voice · Neural acoustics and responsive sound spaces · Performance, projection & stage media

The source repository was created on 2026-11-21. This is its first complete guide in the library.

### Quality assessment: Quality unverified

Creative use and the code grant are documented. Check-level gaps remain before a recommendation.

Scope: Compare a musician-isolation research workflow on an authorized noncommercial ensemble recording.

Evidence checked: 2026-11-21. No local execution implied.

- **Open-source software license · verified:** Reviewed the complete project software grant and its redistribution conditions. Model, data and service terms are scoped separately. [Source](https://github.com/AMAAI-Lab/who_plays_what/blob/main/LICENSE)
- **Creative results · documented:** The maintainers report median signal-to-distortion ratios for 58 prompted players in URMP, measured against individual reference recordings. The archived examples and evaluation scope cover overlapping instruments. [Source](https://github.com/AMAAI-Lab/who_plays_what/blob/main/README.md) [Source](https://amaai-lab.github.io/who_plays_what_demo/) [Source](https://huggingface.co/amaai-lab/who_plays_what/raw/main/README.md)
- **Reproducible setup · documented:** The installation and first-use steps are in the cited documentation. Reproduction of this workflow remains unverified. [Source](https://github.com/AMAAI-Lab/who_plays_what/blob/main/README.md) [Source](https://amaai-lab.github.io/who_plays_what_demo/) [Source](https://huggingface.co/amaai-lab/who_plays_what/raw/main/README.md)
- **Maintenance and support · unknown:** The reviewed sources do not establish workflow-specific support, fixes and unresolved blockers.
- **Independent use · unknown:** Independent first-hand use of the exact workflow was not established in this source review.
- **Models, services and costs · documented:** The code is MIT. The authors list model and data as CC BY-NC 4.0. The selected tracking and separation dependencies have independent terms. Local processing uses model downloads and compute. The documented release is intended for a rights-cleared noncommercial workflow under the scoped terms. [Source](https://github.com/AMAAI-Lab/who_plays_what/blob/main/README.md) [Source](https://amaai-lab.github.io/who_plays_what_demo/) [Source](https://huggingface.co/amaai-lab/who_plays_what/raw/main/README.md)

Source and documentation review. No hands-on execution by AI Media Scout. Primary author results have dataset and visibility constraints. Compare synchronization, occlusions and recording conditions before treating the result as a clean stem.

### How it uses AI

Who Plays What tracks a musician in a paired audio/video recording using SAM, visual embeddings and body/hand keypoints, then conditions an audio separator on the tracked player. [Source](https://github.com/AMAAI-Lab/who_plays_what/blob/main/README.md) [Source](https://amaai-lab.github.io/who_plays_what_demo/) [Source](https://huggingface.co/amaai-lab/who_plays_what/raw/main/README.md)

### Introduction

Who Plays What tracks a musician in a paired audio/video recording using SAM, visual embeddings and body/hand keypoints, then conditions an audio separator on the tracked player. [Source 1](https://github.com/AMAAI-Lab/who_plays_what/blob/main/README.md) [Source 2](https://amaai-lab.github.io/who_plays_what_demo/) [Source 3](https://huggingface.co/amaai-lab/who_plays_what/raw/main/README.md)

### What it is good for

Compare a musician-isolation research workflow on an authorized noncommercial ensemble recording. [Source 1](https://github.com/AMAAI-Lab/who_plays_what/blob/main/README.md) [Source 2](https://amaai-lab.github.io/who_plays_what_demo/) [Source 3](https://huggingface.co/amaai-lab/who_plays_what/raw/main/README.md)

### Demo & examples

The maintainers report median signal-to-distortion ratios for 58 prompted players in URMP, measured against individual reference recordings. The archived examples and evaluation scope cover overlapping instruments. [Source 1](https://github.com/AMAAI-Lab/who_plays_what/blob/main/README.md) [Source 2](https://amaai-lab.github.io/who_plays_what_demo/) [Source 3](https://huggingface.co/amaai-lab/who_plays_what/raw/main/README.md)

### Install

Follow the documented route for the scoped workflow. The steps below are source references. [Source 1](https://github.com/AMAAI-Lab/who_plays_what/blob/main/README.md) [Source 2](https://amaai-lab.github.io/who_plays_what_demo/) [Source 3](https://huggingface.co/amaai-lab/who_plays_what/raw/main/README.md)

1. Use the documented Python 3.11 environment and project dependencies. Review exact weights and permissions before loading an ensemble recording.
2. Prepare an allowed example with a visible target musician and synchronized audio. Check runtime and GPU requirements in the source.
### First project

A small first project makes the input, model output and handoff easy to inspect. [Source 1](https://github.com/AMAAI-Lab/who_plays_what/blob/main/README.md) [Source 2](https://amaai-lab.github.io/who_plays_what_demo/) [Source 3](https://huggingface.co/amaai-lab/who_plays_what/raw/main/README.md)

1. Choose an on-screen point that identifies the intended musician. Inspect whether the tracker follows the correct player.
2. Export the estimated track and compare it with the complete recording or a known isolated recording.
3. Record whether the model confuses similarly moving performers, loses a track during occlusion or preserves unwanted bleed.
### Hardware & software

Platform and compute constraints refer to the selected route. [Source 1](https://github.com/AMAAI-Lab/who_plays_what/blob/main/README.md) [Source 2](https://amaai-lab.github.io/who_plays_what_demo/) [Source 3](https://huggingface.co/amaai-lab/who_plays_what/raw/main/README.md)

- **Hardware:** Minimum RAM, VRAM and disk space for the scoped workflow are undocumented.
- **Software:** Project inference code, Python 3.11 environment and separate tracking, feature and separation models. The evaluation documents CUDA use.
- **Platforms:** Author source and GPU evaluation instructions are documented. Mac, Windows and other device compatibility for the full stack is not established.

### License, model weights & costs

The full software license was reviewed. Dependencies and creative assets carry their own terms. [Source 1](https://github.com/AMAAI-Lab/who_plays_what/blob/main/LICENSE) [Source 2](https://github.com/AMAAI-Lab/who_plays_what/blob/main/README.md) [Source 3](https://amaai-lab.github.io/who_plays_what_demo/) [Source 4](https://huggingface.co/amaai-lab/who_plays_what/raw/main/README.md)

- **Code:** MIT
- **Weights:** The code is MIT. The authors list model and data as CC BY-NC 4.0. The selected tracking and separation dependencies have independent terms.
- **Commercial:** Project code is governed by MIT. Confirm selected model, source-media and output restrictions separately.
- **Cost:** Local processing uses model downloads and compute. The documented release is intended for a rights-cleared noncommercial workflow under the scoped terms.

### Why it merits attention

The creative workflow is grounded in the cited documentation. Output quality and compatibility are not hands-on verified. [Source 1](https://github.com/AMAAI-Lab/who_plays_what/blob/main/README.md) [Source 2](https://amaai-lab.github.io/who_plays_what_demo/) [Source 3](https://huggingface.co/amaai-lab/who_plays_what/raw/main/README.md)

### Limitations

Primary author results have dataset and visibility constraints. Compare synchronization, occlusions and recording conditions before treating the result as a clean stem. [Source 1](https://github.com/AMAAI-Lab/who_plays_what/blob/main/README.md) [Source 2](https://amaai-lab.github.io/who_plays_what_demo/) [Source 3](https://huggingface.co/amaai-lab/who_plays_what/raw/main/README.md)

### Get the tool

- [Repository](https://github.com/AMAAI-Lab/who_plays_what)
- [Documentation](https://huggingface.co/amaai-lab/who_plays_what/raw/main/README.md)

## OCRmyPDF Hebrew plugin

Cultural heritage layout recognition and transcription · Archives, media restoration & collections · Creative publishing & presentation

The source repository was created on 2026-11-19. This is its first complete guide in the library.

### Quality assessment: Quality unverified

Creative use and the code grant are documented. Check-level gaps remain before a recommendation.

Scope: Create a draft searchable PDF from multilingual historical leaflets or scanned catalog pages and review their text and numeric order.

Evidence checked: 2026-11-21. No local execution implied.

- **Open-source software license · verified:** Reviewed the complete project software grant and its redistribution conditions. Model, data and service terms are scoped separately. [Source](https://github.com/RivoksLab/ocrmypdf-hebrew/blob/main/LICENSE)
- **Creative results · documented:** The maintainer documents small example and synthetic comparisons for rereading fragmented numbers. Different page layouts or historic scripts require their own check. [Source](https://github.com/RivoksLab/ocrmypdf-hebrew/blob/main/README.md) [Source](https://github.com/RivoksLab/ocrmypdf-hebrew/blob/main/pyproject.toml) [Source](https://github.com/RivoksLab/paddleocr-hebrew)
- **Reproducible setup · documented:** The installation and first-use steps are in the cited documentation. Reproduction of this workflow remains unverified. [Source](https://github.com/RivoksLab/ocrmypdf-hebrew/blob/main/README.md) [Source](https://github.com/RivoksLab/ocrmypdf-hebrew/blob/main/pyproject.toml) [Source](https://github.com/RivoksLab/paddleocr-hebrew)
- **Maintenance and support · unknown:** The reviewed sources do not establish workflow-specific support, fixes and unresolved blockers.
- **Independent use · unknown:** Independent first-hand use of the exact workflow was not established in this source review.
- **Models, services and costs · documented:** The plugin is Apache-2.0. OCR engine/model grants and any archival image rights must be checked separately. Local processing and model storage are required. The declared offline model directory avoids an inference service. [Source](https://github.com/RivoksLab/ocrmypdf-hebrew/blob/main/README.md) [Source](https://github.com/RivoksLab/ocrmypdf-hebrew/blob/main/pyproject.toml) [Source](https://github.com/RivoksLab/paddleocr-hebrew)

Source and documentation review. No hands-on execution by AI Media Scout. The selector and word-rejoin steps address specific mixed-content cases. Verify reading order and recognition against difficult original pages.

### How it uses AI

The plugin adds the paddleocr-hebrew model engine to OCRmyPDF for searchable Hebrew PDFs. It also provides a separate Tesseract reading-order correction for mixed Hebrew, English and numbers. [Source](https://github.com/RivoksLab/ocrmypdf-hebrew/blob/main/README.md) [Source](https://github.com/RivoksLab/ocrmypdf-hebrew/blob/main/pyproject.toml) [Source](https://github.com/RivoksLab/paddleocr-hebrew)

### Introduction

The plugin adds the paddleocr-hebrew model engine to OCRmyPDF for searchable Hebrew PDFs. It also provides a separate Tesseract reading-order correction for mixed Hebrew, English and numbers. [Source 1](https://github.com/RivoksLab/ocrmypdf-hebrew/blob/main/README.md) [Source 2](https://github.com/RivoksLab/ocrmypdf-hebrew/blob/main/pyproject.toml) [Source 3](https://github.com/RivoksLab/paddleocr-hebrew)

### What it is good for

Create a draft searchable PDF from multilingual historical leaflets or scanned catalog pages and review their text and numeric order. [Source 1](https://github.com/RivoksLab/ocrmypdf-hebrew/blob/main/README.md) [Source 2](https://github.com/RivoksLab/ocrmypdf-hebrew/blob/main/pyproject.toml) [Source 3](https://github.com/RivoksLab/paddleocr-hebrew)

### Demo & examples

The maintainer documents small example and synthetic comparisons for rereading fragmented numbers. Different page layouts or historic scripts require their own check. [Source 1](https://github.com/RivoksLab/ocrmypdf-hebrew/blob/main/README.md) [Source 2](https://github.com/RivoksLab/ocrmypdf-hebrew/blob/main/pyproject.toml) [Source 3](https://github.com/RivoksLab/paddleocr-hebrew)

### Install

Follow the documented route for the scoped workflow. The steps below are source references. [Source 1](https://github.com/RivoksLab/ocrmypdf-hebrew/blob/main/README.md) [Source 2](https://github.com/RivoksLab/ocrmypdf-hebrew/blob/main/pyproject.toml) [Source 3](https://github.com/RivoksLab/paddleocr-hebrew)

1. Use the documented plugin package with OCRmyPDF 17.14 or later and the selected paddleocr-hebrew dependencies.
2. Prepare one authorized scanned page that contains both Hebrew and English. Use a pinned model directory for offline processing where appropriate.
### First project

A small first project makes the input, model output and handoff easy to inspect. [Source 1](https://github.com/RivoksLab/ocrmypdf-hebrew/blob/main/README.md) [Source 2](https://github.com/RivoksLab/ocrmypdf-hebrew/blob/main/pyproject.toml) [Source 3](https://github.com/RivoksLab/paddleocr-hebrew)

1. Apply the Hebrew/English engine to a copy and retain the scanned original.
2. Inspect extracted words, punctuation and mixed numeric values. Compare awkward lines with the page image.
3. Check selection and search in the output PDF, then fix remaining reading-order or recognition errors before publication.
### Hardware & software

Platform and compute constraints refer to the selected route. [Source 1](https://github.com/RivoksLab/ocrmypdf-hebrew/blob/main/README.md) [Source 2](https://github.com/RivoksLab/ocrmypdf-hebrew/blob/main/pyproject.toml) [Source 3](https://github.com/RivoksLab/paddleocr-hebrew)

- **Hardware:** Minimum RAM, VRAM and disk space for the scoped workflow are undocumented.
- **Software:** OCRmyPDF 17.14+, ocrmypdf-hebrew and a chosen model engine. The separate Tesseract path uses the corresponding system dependencies and training data.
- **Platforms:** The plugin documents a Python package installation. Supported host details depend on OCRmyPDF and selected engines.

### License, model weights & costs

The full software license was reviewed. Dependencies and creative assets carry their own terms. [Source 1](https://github.com/RivoksLab/ocrmypdf-hebrew/blob/main/LICENSE) [Source 2](https://github.com/RivoksLab/ocrmypdf-hebrew/blob/main/README.md) [Source 3](https://github.com/RivoksLab/ocrmypdf-hebrew/blob/main/pyproject.toml) [Source 4](https://github.com/RivoksLab/paddleocr-hebrew)

- **Code:** Apache-2.0
- **Weights:** The plugin is Apache-2.0. OCR engine/model grants and any archival image rights must be checked separately.
- **Commercial:** Project code is governed by Apache-2.0. Confirm selected model, source-media and output restrictions separately.
- **Cost:** Local processing and model storage are required. The declared offline model directory avoids an inference service.

### Why it merits attention

The creative workflow is grounded in the cited documentation. Output quality and compatibility are not hands-on verified. [Source 1](https://github.com/RivoksLab/ocrmypdf-hebrew/blob/main/README.md) [Source 2](https://github.com/RivoksLab/ocrmypdf-hebrew/blob/main/pyproject.toml) [Source 3](https://github.com/RivoksLab/paddleocr-hebrew)

### Limitations

The selector and word-rejoin steps address specific mixed-content cases. Verify reading order and recognition against difficult original pages. [Source 1](https://github.com/RivoksLab/ocrmypdf-hebrew/blob/main/README.md) [Source 2](https://github.com/RivoksLab/ocrmypdf-hebrew/blob/main/pyproject.toml) [Source 3](https://github.com/RivoksLab/paddleocr-hebrew)

### Get the tool

- [Repository](https://github.com/RivoksLab/ocrmypdf-hebrew)
- [Documentation](https://github.com/RivoksLab/paddleocr-hebrew)

## tiny-voca

Audio, music & voice · Creative publishing & presentation · Accessible media & assistive creation

The source repository was created on 2026-11-14. This is its first complete guide in the library.

### Quality assessment: Quality unverified

Creative use and the code grant are documented. Check-level gaps remain before a recommendation.

Scope: Create a draft voiceover track for original text, compare emphasis and timing and keep the script editable.

Evidence checked: 2026-11-21. No local execution implied.

- **Open-source software license · verified:** Reviewed the complete project software grant and its redistribution conditions. Model, data and service terms are scoped separately. [Source](https://github.com/n4ze3m/tiny-voca/blob/main/LICENSE)
- **Creative results · documented:** The developer publishes a browser example, waveform details and source-side inference settings. Audition output for pacing and pronunciation. [Source](https://github.com/n4ze3m/tiny-voca/blob/main/README.md) [Source](https://tiny-voca.n4ze3m.com/) [Source](https://huggingface.co/n4ze3m/tiny-voca) [Source](https://github.com/n4ze3m/tiny-voca/blob/main/pyproject.toml)
- **Reproducible setup · documented:** The installation and first-use steps are in the cited documentation. Reproduction of this workflow remains unverified. [Source](https://github.com/n4ze3m/tiny-voca/blob/main/README.md) [Source](https://tiny-voca.n4ze3m.com/) [Source](https://huggingface.co/n4ze3m/tiny-voca) [Source](https://github.com/n4ze3m/tiny-voca/blob/main/pyproject.toml)
- **Maintenance and support · unknown:** The reviewed sources do not establish workflow-specific support, fixes and unresolved blockers.
- **Independent use · unknown:** Independent first-hand use of the exact workflow was not established in this source review.
- **Models, services and costs · documented:** Apache-2.0 governs the code. Review the precise weight, voice and dataset terms in their primary repositories for the planned use. Local speech generation uses device compute. Model and waveform storage remain separate. [Source](https://github.com/n4ze3m/tiny-voca/blob/main/README.md) [Source](https://tiny-voca.n4ze3m.com/) [Source](https://huggingface.co/n4ze3m/tiny-voca) [Source](https://github.com/n4ze3m/tiny-voca/blob/main/pyproject.toml)

Source and documentation review. No hands-on execution by AI Media Scout. The released voices are American English. The project describes skipping unsupported non-speech text and offers a small number of voices.

### How it uses AI

tiny-voca is a small English neural synthesizer with CPU and ONNX/browser paths. It exposes two voices, pitch and speaking-rate controls for WAV output. [Source](https://github.com/n4ze3m/tiny-voca/blob/main/README.md) [Source](https://tiny-voca.n4ze3m.com/) [Source](https://huggingface.co/n4ze3m/tiny-voca) [Source](https://github.com/n4ze3m/tiny-voca/blob/main/pyproject.toml)

### Introduction

tiny-voca is a small English neural synthesizer with CPU and ONNX/browser paths. It exposes two voices, pitch and speaking-rate controls for WAV output. [Source 1](https://github.com/n4ze3m/tiny-voca/blob/main/README.md) [Source 2](https://tiny-voca.n4ze3m.com/) [Source 3](https://huggingface.co/n4ze3m/tiny-voca) [Source 4](https://github.com/n4ze3m/tiny-voca/blob/main/pyproject.toml)

### What it is good for

Create a draft voiceover track for original text, compare emphasis and timing and keep the script editable. [Source 1](https://github.com/n4ze3m/tiny-voca/blob/main/README.md) [Source 2](https://tiny-voca.n4ze3m.com/) [Source 3](https://huggingface.co/n4ze3m/tiny-voca) [Source 4](https://github.com/n4ze3m/tiny-voca/blob/main/pyproject.toml)

### Demo & examples

The developer publishes a browser example, waveform details and source-side inference settings. Audition output for pacing and pronunciation. [Source 1](https://github.com/n4ze3m/tiny-voca/blob/main/README.md) [Source 2](https://tiny-voca.n4ze3m.com/) [Source 3](https://huggingface.co/n4ze3m/tiny-voca) [Source 4](https://github.com/n4ze3m/tiny-voca/blob/main/pyproject.toml)

### Install

Follow the documented route for the scoped workflow. The steps below are source references. [Source 1](https://github.com/n4ze3m/tiny-voca/blob/main/README.md) [Source 2](https://tiny-voca.n4ze3m.com/) [Source 3](https://huggingface.co/n4ze3m/tiny-voca) [Source 4](https://github.com/n4ze3m/tiny-voca/blob/main/pyproject.toml)

1. Follow the documented Python package and weight setup, or select the official ONNX/browser route.
2. Keep phonemizer assets and chosen model files together. Verify the archive, exact model and terms before generating speech.
### First project

A small first project makes the input, model output and handoff easy to inspect. [Source 1](https://github.com/n4ze3m/tiny-voca/blob/main/README.md) [Source 2](https://tiny-voca.n4ze3m.com/) [Source 3](https://huggingface.co/n4ze3m/tiny-voca) [Source 4](https://github.com/n4ze3m/tiny-voca/blob/main/pyproject.toml)

1. Start with a short clear American English sample script. Choose F2 or M2 and a baseline speaking rate.
2. Listen to the exported 24 kHz WAV against the text for pronunciation and volume. Compare one parameter change.
3. Retain the chosen voice and a WAV plus the original script for editing and replacement.
### Hardware & software

Platform and compute constraints refer to the selected route. [Source 1](https://github.com/n4ze3m/tiny-voca/blob/main/README.md) [Source 2](https://tiny-voca.n4ze3m.com/) [Source 3](https://huggingface.co/n4ze3m/tiny-voca) [Source 4](https://github.com/n4ze3m/tiny-voca/blob/main/pyproject.toml)

- **Hardware:** The maintainer lists an 18 MB model and reports CPU benchmarks, with separate browser runtimes. Minimum RAM and platform-specific compute constraints are undocumented.
- **Software:** Python/PyTorch or the documented ONNX Runtime route, a matching tiny-voca model and dizione phonemizer assets.
- **Platforms:** The source supports CPU and an ONNX Runtime Web workflow. Exact OS/browser compatibility needs independent confirmation.

### License, model weights & costs

The full software license was reviewed. Dependencies and creative assets carry their own terms. [Source 1](https://github.com/n4ze3m/tiny-voca/blob/main/LICENSE) [Source 2](https://github.com/n4ze3m/tiny-voca/blob/main/README.md) [Source 3](https://tiny-voca.n4ze3m.com/) [Source 4](https://huggingface.co/n4ze3m/tiny-voca) [Source 5](https://github.com/n4ze3m/tiny-voca/blob/main/pyproject.toml)

- **Code:** Apache-2.0
- **Weights:** Apache-2.0 governs the code. Review the precise weight, voice and dataset terms in their primary repositories for the planned use.
- **Commercial:** Project code is governed by Apache-2.0. Confirm selected model, source-media and output restrictions separately.
- **Cost:** Local speech generation uses device compute. Model and waveform storage remain separate.

### Why it merits attention

The creative workflow is grounded in the cited documentation. Output quality and compatibility are not hands-on verified. [Source 1](https://github.com/n4ze3m/tiny-voca/blob/main/README.md) [Source 2](https://tiny-voca.n4ze3m.com/) [Source 3](https://huggingface.co/n4ze3m/tiny-voca) [Source 4](https://github.com/n4ze3m/tiny-voca/blob/main/pyproject.toml)

### Limitations

The released voices are American English. The project describes skipping unsupported non-speech text and offers a small number of voices. [Source 1](https://github.com/n4ze3m/tiny-voca/blob/main/README.md) [Source 2](https://tiny-voca.n4ze3m.com/) [Source 3](https://huggingface.co/n4ze3m/tiny-voca) [Source 4](https://github.com/n4ze3m/tiny-voca/blob/main/pyproject.toml)

### Get the tool

- [Repository](https://github.com/n4ze3m/tiny-voca)
- [Documentation](https://github.com/n4ze3m/tiny-voca/blob/main/pyproject.toml)

## FlashVSR+

Archival film restoration and preservation · Video, animation & film · Editing, captions & post-production

First complete guide in the library. The publication and documentation dates are not necessarily the project’s launch date.

### Quality assessment: Quality unverified

Creative use and the code grant are documented. Check-level gaps remain before a recommendation.

Scope: Compare a preservation-oriented upscale of a short authorized motion shot with a conventional resize, keeping the original and model settings.

Evidence checked: 2026-11-21. No local execution implied.

- **Open-source software license · verified:** Reviewed the complete project software grant and its redistribution conditions. Model, data and service terms are scoped separately. [Source](https://github.com/OpenImagingLab/FlashVSR_Plus/blob/main/LICENSE)
- **Creative results · documented:** The authors document a single-GPU spatially untiled 4K example and publish multiple sample clips. Device, preset and scene motion determine the result. [Source](https://github.com/OpenImagingLab/FlashVSR_Plus/blob/main/README.md) [Source](https://github.com/OpenImagingLab/FlashVSR_Plus/blob/main/requirements.txt)
- **Reproducible setup · documented:** The installation and first-use steps are in the cited documentation. Reproduction of this workflow remains unverified. [Source](https://github.com/OpenImagingLab/FlashVSR_Plus/blob/main/README.md) [Source](https://github.com/OpenImagingLab/FlashVSR_Plus/blob/main/requirements.txt)
- **Maintenance and support · unknown:** The reviewed sources do not establish workflow-specific support, fixes and unresolved blockers.
- **Independent use · unknown:** Independent first-hand use of the exact workflow was not established in this source review.
- **Models, services and costs · documented:** Apache-2.0 governs the inference source. Check the selected weight terms and rights for the archival media separately. Local CUDA compute and model storage are needed, plus temporary and output video space. [Source](https://github.com/OpenImagingLab/FlashVSR_Plus/blob/main/README.md) [Source](https://github.com/OpenImagingLab/FlashVSR_Plus/blob/main/requirements.txt)

Source and documentation review. No hands-on execution by AI Media Scout. Generative upscaling can change texture and small details. The maintainer distinguishes packaged inference from separately maintained community routes.

### How it uses AI

FlashVSR+ uses a one-step diffusion model to upscale video. The official inference route offers Turbo, Base and V1 checkpoints and configurable motion and segmentation options. [Source](https://github.com/OpenImagingLab/FlashVSR_Plus/blob/main/README.md) [Source](https://github.com/OpenImagingLab/FlashVSR_Plus/blob/main/requirements.txt)

### Introduction

FlashVSR+ uses a one-step diffusion model to upscale video. The official inference route offers Turbo, Base and V1 checkpoints and configurable motion and segmentation options. [Source 1](https://github.com/OpenImagingLab/FlashVSR_Plus/blob/main/README.md) [Source 2](https://github.com/OpenImagingLab/FlashVSR_Plus/blob/main/requirements.txt)

### What it is good for

Compare a preservation-oriented upscale of a short authorized motion shot with a conventional resize, keeping the original and model settings. [Source 1](https://github.com/OpenImagingLab/FlashVSR_Plus/blob/main/README.md) [Source 2](https://github.com/OpenImagingLab/FlashVSR_Plus/blob/main/requirements.txt)

### Demo & examples

The authors document a single-GPU spatially untiled 4K example and publish multiple sample clips. Device, preset and scene motion determine the result. [Source 1](https://github.com/OpenImagingLab/FlashVSR_Plus/blob/main/README.md) [Source 2](https://github.com/OpenImagingLab/FlashVSR_Plus/blob/main/requirements.txt)

### Install

Follow the documented route for the scoped workflow. The steps below are source references. [Source 1](https://github.com/OpenImagingLab/FlashVSR_Plus/blob/main/README.md) [Source 2](https://github.com/OpenImagingLab/FlashVSR_Plus/blob/main/requirements.txt)

1. Prepare the documented Linux, CUDA and Python 3.10 environment. Select the official released preset and its model files.
2. Choose a test clip with input dimensions accepted by the chosen inference route. Check acceleration and weight terms separately.
### First project

A small first project makes the input, model output and handoff easy to inspect. [Source 1](https://github.com/OpenImagingLab/FlashVSR_Plus/blob/main/README.md) [Source 2](https://github.com/OpenImagingLab/FlashVSR_Plus/blob/main/requirements.txt)

1. Render one short sample with known detail at the native resolution, then compare it to a neutral rescale.
2. Inspect motion boundaries and written text across frames for flicker or invented detail. Adjust settings on a copy if the source motion is difficult.
3. Preserve the source, output and exact model settings for restoration review.
### Hardware & software

Platform and compute constraints refer to the selected route. [Source 1](https://github.com/OpenImagingLab/FlashVSR_Plus/blob/main/README.md) [Source 2](https://github.com/OpenImagingLab/FlashVSR_Plus/blob/main/requirements.txt)

- **Hardware:** The maintainer’s 4K example uses one RTX 4090 with 24 GB. Exact minimum VRAM is workload-dependent and undocumented for all presets.
- **Software:** Linux, Python 3.10 and NVIDIA CUDA for the official pipeline, plus checkpoint files and chosen attention backend. The source lists input divisibility by 128.
- **Platforms:** The official inference path lists Linux/NVIDIA. Separate community integrations have their own validation and requirements.

### License, model weights & costs

The full software license was reviewed. Dependencies and creative assets carry their own terms. [Source 1](https://github.com/OpenImagingLab/FlashVSR_Plus/blob/main/LICENSE) [Source 2](https://github.com/OpenImagingLab/FlashVSR_Plus/blob/main/README.md) [Source 3](https://github.com/OpenImagingLab/FlashVSR_Plus/blob/main/requirements.txt)

- **Code:** Apache-2.0
- **Weights:** Apache-2.0 governs the inference source. Check the selected weight terms and rights for the archival media separately.
- **Commercial:** Project code is governed by Apache-2.0. Confirm selected model, source-media and output restrictions separately.
- **Cost:** Local CUDA compute and model storage are needed, plus temporary and output video space.

### Why it merits attention

The creative workflow is grounded in the cited documentation. Output quality and compatibility are not hands-on verified. [Source 1](https://github.com/OpenImagingLab/FlashVSR_Plus/blob/main/README.md) [Source 2](https://github.com/OpenImagingLab/FlashVSR_Plus/blob/main/requirements.txt)

### Limitations

Generative upscaling can change texture and small details. The maintainer distinguishes packaged inference from separately maintained community routes. [Source 1](https://github.com/OpenImagingLab/FlashVSR_Plus/blob/main/README.md) [Source 2](https://github.com/OpenImagingLab/FlashVSR_Plus/blob/main/requirements.txt)

### Get the tool

- [Repository](https://github.com/OpenImagingLab/FlashVSR_Plus)
- [Documentation](https://github.com/OpenImagingLab/FlashVSR_Plus/blob/main/requirements.txt)

## Direct3D-V3

3D, reconstruction & assets · Spatial audio & volumetric media · Neural procedural material authoring

The source repository was created on 2026-11-18. This is its first complete guide in the library.

### Quality assessment: Quality unverified

Creative use and the code grant are documented. Check-level gaps remain before a recommendation.

Scope: Refine the detail of a rights-cleared coarse prop mesh and hand off the resulting geometry for topology and material review.

Evidence checked: 2026-11-21. No local execution implied.

- **Open-source software license · verified:** Reviewed the complete project software grant and its redistribution conditions. Model, data and service terms are scoped separately. [Source](https://github.com/DreamTechAI/Direct3D-V3/blob/main/LICENSE)
- **Creative results · documented:** The research project presents examples and method details with a current inference package. The released path uses aligned inputs, while the separately listed coarse-model and texture-training components are pending. [Source](https://github.com/DreamTechAI/Direct3D-V3/blob/main/README.md) [Source](https://dreamtechai.github.io/Direct3D-V3/) [Source](https://huggingface.co/wushuang98/Direct3D-V3/raw/main/README.md) [Source](https://github.com/DreamTechAI/Direct3D-V3/blob/main/requirements.txt)
- **Reproducible setup · documented:** The installation and first-use steps are in the cited documentation. Reproduction of this workflow remains unverified. [Source](https://github.com/DreamTechAI/Direct3D-V3/blob/main/README.md) [Source](https://dreamtechai.github.io/Direct3D-V3/) [Source](https://huggingface.co/wushuang98/Direct3D-V3/raw/main/README.md) [Source](https://github.com/DreamTechAI/Direct3D-V3/blob/main/requirements.txt)
- **Maintenance and support · unknown:** The reviewed sources do not establish workflow-specific support, fixes and unresolved blockers.
- **Independent use · unknown:** Independent first-hand use of the exact workflow was not established in this source review.
- **Models, services and costs · documented:** The released inference source is MIT. Model weights and optional image/coarse-mesh tools are separate. Check the exact package and source-reference rights. Local GPU compute, model weights and mesh intermediates require capacity. Optional remote image preparation can have separate costs. [Source](https://github.com/DreamTechAI/Direct3D-V3/blob/main/README.md) [Source](https://dreamtechai.github.io/Direct3D-V3/) [Source](https://huggingface.co/wushuang98/Direct3D-V3/raw/main/README.md) [Source](https://github.com/DreamTechAI/Direct3D-V3/blob/main/requirements.txt)

Source and documentation review. No hands-on execution by AI Media Scout. The inference release expects a suitable coarse mesh and aligned image. Exact detail, topology and printing readiness depend on downstream validation.

### How it uses AI

Direct3D-V3 combines a reference image and aligned coarse mesh with a voxel-domain diffusion transformer to produce refined geometry. [Source](https://github.com/DreamTechAI/Direct3D-V3/blob/main/README.md) [Source](https://dreamtechai.github.io/Direct3D-V3/) [Source](https://huggingface.co/wushuang98/Direct3D-V3/raw/main/README.md) [Source](https://github.com/DreamTechAI/Direct3D-V3/blob/main/requirements.txt)

### Introduction

Direct3D-V3 combines a reference image and aligned coarse mesh with a voxel-domain diffusion transformer to produce refined geometry. [Source 1](https://github.com/DreamTechAI/Direct3D-V3/blob/main/README.md) [Source 2](https://dreamtechai.github.io/Direct3D-V3/) [Source 3](https://huggingface.co/wushuang98/Direct3D-V3/raw/main/README.md) [Source 4](https://github.com/DreamTechAI/Direct3D-V3/blob/main/requirements.txt)

### What it is good for

Refine the detail of a rights-cleared coarse prop mesh and hand off the resulting geometry for topology and material review. [Source 1](https://github.com/DreamTechAI/Direct3D-V3/blob/main/README.md) [Source 2](https://dreamtechai.github.io/Direct3D-V3/) [Source 3](https://huggingface.co/wushuang98/Direct3D-V3/raw/main/README.md) [Source 4](https://github.com/DreamTechAI/Direct3D-V3/blob/main/requirements.txt)

### Demo & examples

The research project presents examples and method details with a current inference package. The released path uses aligned inputs, while the separately listed coarse-model and texture-training components are pending. [Source 1](https://github.com/DreamTechAI/Direct3D-V3/blob/main/README.md) [Source 2](https://dreamtechai.github.io/Direct3D-V3/) [Source 3](https://huggingface.co/wushuang98/Direct3D-V3/raw/main/README.md) [Source 4](https://github.com/DreamTechAI/Direct3D-V3/blob/main/requirements.txt)

### Install

Follow the documented route for the scoped workflow. The steps below are source references. [Source 1](https://github.com/DreamTechAI/Direct3D-V3/blob/main/README.md) [Source 2](https://dreamtechai.github.io/Direct3D-V3/) [Source 3](https://huggingface.co/wushuang98/Direct3D-V3/raw/main/README.md) [Source 4](https://github.com/DreamTechAI/Direct3D-V3/blob/main/requirements.txt)

1. Follow the Linux GPU setup and use the documented Python, Torch, CUDA and C++ compiler configuration. Obtain the matching official inference assets.
2. Prepare a small coarse OBJ, GLB or PLY and RGB/RGBA reference with matching orientation before testing.
### First project

A small first project makes the input, model output and handoff easy to inspect. [Source 1](https://github.com/DreamTechAI/Direct3D-V3/blob/main/README.md) [Source 2](https://dreamtechai.github.io/Direct3D-V3/) [Source 3](https://huggingface.co/wushuang98/Direct3D-V3/raw/main/README.md) [Source 4](https://github.com/DreamTechAI/Direct3D-V3/blob/main/requirements.txt)

1. Open the example and inspect orientation. Try one original or cleared prop using the documented inference resolution.
2. Compare silhouette and surface detail against the input, and inspect holes or disconnected faces.
3. Export GLB or another documented geometry path and review topology downstream before using it as a finished production asset.
### Hardware & software

Platform and compute constraints refer to the selected route. [Source 1](https://github.com/DreamTechAI/Direct3D-V3/blob/main/README.md) [Source 2](https://dreamtechai.github.io/Direct3D-V3/) [Source 3](https://huggingface.co/wushuang98/Direct3D-V3/raw/main/README.md) [Source 4](https://github.com/DreamTechAI/Direct3D-V3/blob/main/requirements.txt)

- **Hardware:** Minimum RAM, VRAM and disk space for the scoped workflow are undocumented.
- **Software:** The demo documents Linux with Python 3.12, PyTorch 2.14.1, CUDA Toolkit 13.0 and a C++20 compiler. FlashAttention and native extensions are workspace dependencies.
- **Platforms:** Linux CUDA is the documented reference setup. Other environments need separate verification.

### License, model weights & costs

The full software license was reviewed. Dependencies and creative assets carry their own terms. [Source 1](https://github.com/DreamTechAI/Direct3D-V3/blob/main/LICENSE) [Source 2](https://github.com/DreamTechAI/Direct3D-V3/blob/main/README.md) [Source 3](https://dreamtechai.github.io/Direct3D-V3/) [Source 4](https://huggingface.co/wushuang98/Direct3D-V3/raw/main/README.md) [Source 5](https://github.com/DreamTechAI/Direct3D-V3/blob/main/requirements.txt)

- **Code:** MIT
- **Weights:** The released inference source is MIT. Model weights and optional image/coarse-mesh tools are separate. Check the exact package and source-reference rights.
- **Commercial:** Project code is governed by MIT. Confirm selected model, source-media and output restrictions separately.
- **Cost:** Local GPU compute, model weights and mesh intermediates require capacity. Optional remote image preparation can have separate costs.

### Why it merits attention

The creative workflow is grounded in the cited documentation. Output quality and compatibility are not hands-on verified. [Source 1](https://github.com/DreamTechAI/Direct3D-V3/blob/main/README.md) [Source 2](https://dreamtechai.github.io/Direct3D-V3/) [Source 3](https://huggingface.co/wushuang98/Direct3D-V3/raw/main/README.md) [Source 4](https://github.com/DreamTechAI/Direct3D-V3/blob/main/requirements.txt)

### Limitations

The inference release expects a suitable coarse mesh and aligned image. Exact detail, topology and printing readiness depend on downstream validation. [Source 1](https://github.com/DreamTechAI/Direct3D-V3/blob/main/README.md) [Source 2](https://dreamtechai.github.io/Direct3D-V3/) [Source 3](https://huggingface.co/wushuang98/Direct3D-V3/raw/main/README.md) [Source 4](https://github.com/DreamTechAI/Direct3D-V3/blob/main/requirements.txt)

### Get the tool

- [Repository](https://github.com/DreamTechAI/Direct3D-V3)
- [Documentation](https://github.com/DreamTechAI/Direct3D-V3/blob/main/requirements.txt)

## AudiobookForge

Creative publishing & presentation · Accessible media & assistive creation · Audio, music & voice

First complete guide in the library. The publication and documentation dates are not necessarily the project’s launch date.

### Quality assessment: Quality unverified

Creative use and the code grant are documented. Check-level gaps remain before a recommendation.

Scope: Edit the chapter text of an owned zine or educational publication before synthesizing a chaptered audiobook and a representative MP3.

Evidence checked: 2026-11-21. No local execution implied.

- **Open-source software license · verified:** Reviewed the complete project software grant and its redistribution conditions. Model, data and service terms are scoped separately. [Source](https://github.com/pyMoLt/audiobookForge/blob/main/LICENSE)
- **Creative results · documented:** The creator documents a chapter review panel, a voice preview catalog and a player. Result checks would compare normalized spoken abbreviations, chapter order and figure callouts to the source. [Source](https://github.com/pyMoLt/audiobookForge/blob/main/README.md) [Source](https://github.com/pyMoLt/audiobookForge/blob/main/THIRD_PARTY.md) [Source](https://github.com/pyMoLt/audiobookForge/blob/main/CHANGELOG.md)
- **Reproducible setup · documented:** The installation and first-use steps are in the cited documentation. Reproduction of this workflow remains unverified. [Source](https://github.com/pyMoLt/audiobookForge/blob/main/README.md) [Source](https://github.com/pyMoLt/audiobookForge/blob/main/THIRD_PARTY.md) [Source](https://github.com/pyMoLt/audiobookForge/blob/main/CHANGELOG.md)
- **Maintenance and support · documented:** The v4.4.0 release and changelog describe the current engine options. Processing performance and support for a specific scan remain unverified. [Source](https://github.com/pyMoLt/audiobookForge/releases/tag/v4.4.0)
- **Independent use · unknown:** Independent first-hand use of the exact workflow was not established in this source review.
- **Models, services and costs · documented:** The app is MIT. The notices list Phonon 40m weights as CC BY-NC 4.0, Pocket TTS weights as CC BY 4.0 and voice-specific terms for Piper. Use authorized source books and obtain speaker consent for any voice cloning. Local conversion requires compute, model storage and audio output space. Optional services have their own terms and billing. [Source](https://github.com/pyMoLt/audiobookForge/blob/main/README.md) [Source](https://github.com/pyMoLt/audiobookForge/blob/main/THIRD_PARTY.md) [Source](https://github.com/pyMoLt/audiobookForge/blob/main/CHANGELOG.md)

Source and documentation review. No hands-on execution by AI Media Scout. OCR, reading order and pronunciation require editorial review. The package uses ad-hoc signing. Model, voice and book permissions vary by input and workflow.

### How it uses AI

AudiobookForge uses selectable local neural speech engines to narrate text extracted from PDFs and EPUBs. Apple Vision OCR can recover text in scanned pages. An optional configured model can summarize text or describe figures. [Source](https://github.com/pyMoLt/audiobookForge/blob/main/README.md) [Source](https://github.com/pyMoLt/audiobookForge/blob/main/THIRD_PARTY.md) [Source](https://github.com/pyMoLt/audiobookForge/blob/main/CHANGELOG.md)

### Introduction

AudiobookForge uses selectable local neural speech engines to narrate text extracted from PDFs and EPUBs. Apple Vision OCR can recover text in scanned pages. An optional configured model can summarize text or describe figures. [Source 1](https://github.com/pyMoLt/audiobookForge/blob/main/README.md) [Source 2](https://github.com/pyMoLt/audiobookForge/blob/main/THIRD_PARTY.md) [Source 3](https://github.com/pyMoLt/audiobookForge/blob/main/CHANGELOG.md)

### What it is good for

Edit the chapter text of an owned zine or educational publication before synthesizing a chaptered audiobook and a representative MP3. [Source 1](https://github.com/pyMoLt/audiobookForge/blob/main/README.md) [Source 2](https://github.com/pyMoLt/audiobookForge/blob/main/THIRD_PARTY.md) [Source 3](https://github.com/pyMoLt/audiobookForge/blob/main/CHANGELOG.md)

### Demo & examples

The creator documents a chapter review panel, a voice preview catalog and a player. Result checks would compare normalized spoken abbreviations, chapter order and figure callouts to the source. [Source 1](https://github.com/pyMoLt/audiobookForge/blob/main/README.md) [Source 2](https://github.com/pyMoLt/audiobookForge/blob/main/THIRD_PARTY.md) [Source 3](https://github.com/pyMoLt/audiobookForge/blob/main/CHANGELOG.md)

### Install

Follow the documented route for the scoped workflow. The steps below are source references. [Source 1](https://github.com/pyMoLt/audiobookForge/blob/main/README.md) [Source 2](https://github.com/pyMoLt/audiobookForge/blob/main/THIRD_PARTY.md) [Source 3](https://github.com/pyMoLt/audiobookForge/blob/main/CHANGELOG.md)

1. Choose the official Apple silicon release or follow the Xcode and Tuist source build. The project explains the ad-hoc signing status of the download.
2. Install FFmpeg for audio packaging. In Engines & Downloads, select an engine and specific voice whose use terms fit the book.
### First project

A small first project makes the input, model output and handoff easy to inspect. [Source 1](https://github.com/pyMoLt/audiobookForge/blob/main/README.md) [Source 2](https://github.com/pyMoLt/audiobookForge/blob/main/THIRD_PARTY.md) [Source 3](https://github.com/pyMoLt/audiobookForge/blob/main/CHANGELOG.md)

1. Import a small rights-cleared PDF or EPUB with a cover and two chapters. Compare extraction order and headings with the printed pages.
2. Correct line-break artifacts and add pronunciation entries. Audition one paragraph before synthesizing the rest.
3. Export the chaptered M4B or individual MP3s. Open the export in a chapter-aware player and check navigation and loudness.
### Hardware & software

Platform and compute constraints refer to the selected route. [Source 1](https://github.com/pyMoLt/audiobookForge/blob/main/README.md) [Source 2](https://github.com/pyMoLt/audiobookForge/blob/main/THIRD_PARTY.md) [Source 3](https://github.com/pyMoLt/audiobookForge/blob/main/CHANGELOG.md)

- **Hardware:** Minimum RAM, VRAM and disk space for the scoped workflow are undocumented.
- **Software:** macOS 15 or later, FFmpeg and the selected TTS engine. The source build lists Xcode 16+ and Tuist. Summaries and figure descriptions require a separately configured OpenAI-compatible service.
- **Platforms:** Apple silicon macOS on M1 or newer documented for v4.4.0.

### License, model weights & costs

The full software license was reviewed. Dependencies and creative assets carry their own terms. [Source 1](https://github.com/pyMoLt/audiobookForge/blob/main/LICENSE) [Source 2](https://github.com/pyMoLt/audiobookForge/blob/main/README.md) [Source 3](https://github.com/pyMoLt/audiobookForge/blob/main/THIRD_PARTY.md) [Source 4](https://github.com/pyMoLt/audiobookForge/blob/main/CHANGELOG.md)

- **Code:** MIT
- **Weights:** The app is MIT. The notices list Phonon 40m weights as CC BY-NC 4.0, Pocket TTS weights as CC BY 4.0 and voice-specific terms for Piper. Use authorized source books and obtain speaker consent for any voice cloning.
- **Commercial:** Project code is governed by MIT. Confirm selected model, source-media and output restrictions separately.
- **Cost:** Local conversion requires compute, model storage and audio output space. Optional services have their own terms and billing.

### Why it merits attention

The creative workflow is grounded in the cited documentation. Output quality and compatibility are not hands-on verified. [Source 1](https://github.com/pyMoLt/audiobookForge/blob/main/README.md) [Source 2](https://github.com/pyMoLt/audiobookForge/blob/main/THIRD_PARTY.md) [Source 3](https://github.com/pyMoLt/audiobookForge/blob/main/CHANGELOG.md)

### Limitations

OCR, reading order and pronunciation require editorial review. The package uses ad-hoc signing. Model, voice and book permissions vary by input and workflow. [Source 1](https://github.com/pyMoLt/audiobookForge/blob/main/README.md) [Source 2](https://github.com/pyMoLt/audiobookForge/blob/main/THIRD_PARTY.md) [Source 3](https://github.com/pyMoLt/audiobookForge/blob/main/CHANGELOG.md)

### Get the tool

- [Repository](https://github.com/pyMoLt/audiobookForge)
- [Documentation](https://github.com/pyMoLt/audiobookForge/blob/main/CHANGELOG.md)

## Sound Analyzer

Neural soundscape ecology and sonic art · Audio, music & voice · Neural acoustics and responsive sound spaces

This completes an earlier pending guide with a current source review.

### Quality assessment: Quality unverified

Creative use and the code grant are documented. Check-level gaps remain before a recommendation.

Scope: Annotate candidate sounds from a gallery, rehearsal or field recording to find possible material for a soundscape edit.

Evidence checked: 2026-11-21. No local execution implied.

- **Open-source software license · verified:** Reviewed the complete project software grant and its redistribution conditions. Model, data and service terms are scoped separately. [Source](https://github.com/LeshawnG/sound-analyzer/blob/main/LICENSE)
- **Creative results · documented:** The developer shows a time-linked spectrogram and replayable classifier events. Human review can confirm or reject a detection, and missed events require listening to the original material. [Source](https://github.com/LeshawnG/sound-analyzer/blob/main/README.md) [Source](https://github.com/LeshawnG/sound-analyzer/blob/main/THIRD_PARTY_NOTICES.md) [Source](https://github.com/LeshawnG/sound-analyzer/blob/main/CHANGELOG.md)
- **Reproducible setup · documented:** The installation and first-use steps are in the cited documentation. Reproduction of this workflow remains unverified. [Source](https://github.com/LeshawnG/sound-analyzer/blob/main/README.md) [Source](https://github.com/LeshawnG/sound-analyzer/blob/main/THIRD_PARTY_NOTICES.md) [Source](https://github.com/LeshawnG/sound-analyzer/blob/main/CHANGELOG.md)
- **Maintenance and support · documented:** The v0.1.0 release packages macOS. The README distinguishes newer source changes, including Windows, from the stable package. [Source](https://github.com/LeshawnG/sound-analyzer/releases/tag/v0.1.0)
- **Independent use · unknown:** Independent first-hand use of the exact workflow was not established in this source review.
- **Models, services and costs · documented:** The application is MIT. The ONNX EfficientAT conversion and third-party components have separate notices. Event clips derive from the input recording. CPU and local storage are required. The documented classifier does not meter API calls. [Source](https://github.com/LeshawnG/sound-analyzer/blob/main/README.md) [Source](https://github.com/LeshawnG/sound-analyzer/blob/main/THIRD_PARTY_NOTICES.md) [Source](https://github.com/LeshawnG/sound-analyzer/blob/main/CHANGELOG.md)

Source and documentation review. No hands-on execution by AI Media Scout. Field and rehearsal sound overlap can hide or mislabel events. Treat labels as edit cues and inspect which version supports the chosen OS.

### How it uses AI

Sound Analyzer uses EfficientAT with a MobileNetV3 backbone to label audio events locally. Detected events can retain an audio excerpt, a spectrogram and a reviewer decision. [Source](https://github.com/LeshawnG/sound-analyzer/blob/main/README.md) [Source](https://github.com/LeshawnG/sound-analyzer/blob/main/THIRD_PARTY_NOTICES.md) [Source](https://github.com/LeshawnG/sound-analyzer/blob/main/CHANGELOG.md)

### Introduction

Sound Analyzer uses EfficientAT with a MobileNetV3 backbone to label audio events locally. Detected events can retain an audio excerpt, a spectrogram and a reviewer decision. [Source 1](https://github.com/LeshawnG/sound-analyzer/blob/main/README.md) [Source 2](https://github.com/LeshawnG/sound-analyzer/blob/main/THIRD_PARTY_NOTICES.md) [Source 3](https://github.com/LeshawnG/sound-analyzer/blob/main/CHANGELOG.md)

### What it is good for

Annotate candidate sounds from a gallery, rehearsal or field recording to find possible material for a soundscape edit. [Source 1](https://github.com/LeshawnG/sound-analyzer/blob/main/README.md) [Source 2](https://github.com/LeshawnG/sound-analyzer/blob/main/THIRD_PARTY_NOTICES.md) [Source 3](https://github.com/LeshawnG/sound-analyzer/blob/main/CHANGELOG.md)

### Demo & examples

The developer shows a time-linked spectrogram and replayable classifier events. Human review can confirm or reject a detection, and missed events require listening to the original material. [Source 1](https://github.com/LeshawnG/sound-analyzer/blob/main/README.md) [Source 2](https://github.com/LeshawnG/sound-analyzer/blob/main/THIRD_PARTY_NOTICES.md) [Source 3](https://github.com/LeshawnG/sound-analyzer/blob/main/CHANGELOG.md)

### Install

Follow the documented route for the scoped workflow. The steps below are source references. [Source 1](https://github.com/LeshawnG/sound-analyzer/blob/main/README.md) [Source 2](https://github.com/LeshawnG/sound-analyzer/blob/main/THIRD_PARTY_NOTICES.md) [Source 3](https://github.com/LeshawnG/sound-analyzer/blob/main/CHANGELOG.md)

1. Use the published macOS package or the source setup for your OS. The project documents Python 3.10+ for source installs and PortAudio for capture.
2. Select a local file for the first session. For microphone capture, confirm the input device and OS privacy setting.
### First project

A small first project makes the input, model output and handoff easy to inspect. [Source 1](https://github.com/LeshawnG/sound-analyzer/blob/main/README.md) [Source 2](https://github.com/LeshawnG/sound-analyzer/blob/main/THIRD_PARTY_NOTICES.md) [Source 3](https://github.com/LeshawnG/sound-analyzer/blob/main/CHANGELOG.md)

1. Load a rights-cleared FLAC containing a few known sound events and a quiet reference section.
2. Play candidate events alongside the spectrogram and mark which labels match the recording.
3. Save useful events with their original time positions and use the clean original file for the production edit.
### Hardware & software

Platform and compute constraints refer to the selected route. [Source 1](https://github.com/LeshawnG/sound-analyzer/blob/main/README.md) [Source 2](https://github.com/LeshawnG/sound-analyzer/blob/main/THIRD_PARTY_NOTICES.md) [Source 3](https://github.com/LeshawnG/sound-analyzer/blob/main/CHANGELOG.md)

- **Hardware:** Minimum RAM, VRAM and disk space for the scoped workflow are undocumented.
- **Software:** Published macOS package, or Python 3.10+ source setup with documented audio and ONNX dependencies.
- **Platforms:** The sources list macOS 11+, recent Linux with PortAudio, Raspberry Pi 5 for monitoring, and a newer Windows 10/11 source route.

### License, model weights & costs

The full software license was reviewed. Dependencies and creative assets carry their own terms. [Source 1](https://github.com/LeshawnG/sound-analyzer/blob/main/LICENSE) [Source 2](https://github.com/LeshawnG/sound-analyzer/blob/main/README.md) [Source 3](https://github.com/LeshawnG/sound-analyzer/blob/main/THIRD_PARTY_NOTICES.md) [Source 4](https://github.com/LeshawnG/sound-analyzer/blob/main/CHANGELOG.md)

- **Code:** MIT
- **Weights:** The application is MIT. The ONNX EfficientAT conversion and third-party components have separate notices. Event clips derive from the input recording.
- **Commercial:** Project code is governed by MIT. Confirm selected model, source-media and output restrictions separately.
- **Cost:** CPU and local storage are required. The documented classifier does not meter API calls.

### Why it merits attention

The creative workflow is grounded in the cited documentation. Output quality and compatibility are not hands-on verified. [Source 1](https://github.com/LeshawnG/sound-analyzer/blob/main/README.md) [Source 2](https://github.com/LeshawnG/sound-analyzer/blob/main/THIRD_PARTY_NOTICES.md) [Source 3](https://github.com/LeshawnG/sound-analyzer/blob/main/CHANGELOG.md)

### Limitations

Field and rehearsal sound overlap can hide or mislabel events. Treat labels as edit cues and inspect which version supports the chosen OS. [Source 1](https://github.com/LeshawnG/sound-analyzer/blob/main/README.md) [Source 2](https://github.com/LeshawnG/sound-analyzer/blob/main/THIRD_PARTY_NOTICES.md) [Source 3](https://github.com/LeshawnG/sound-analyzer/blob/main/CHANGELOG.md)

### Get the tool

- [Repository](https://github.com/LeshawnG/sound-analyzer)
- [Documentation](https://github.com/LeshawnG/sound-analyzer/blob/main/CHANGELOG.md)

## NVCR

Learned media codecs and neural delivery · Video, animation & film · AI assisted media quality and take selection

First complete guide in the library. The publication and documentation dates are not necessarily the project’s launch date.

### Quality assessment: Quality unverified

Creative use and the code grant are documented. Check-level gaps remain before a recommendation.

Scope: Compare learned compression size, performance and image quality on a short rights-cleared motion plate before considering a media transport experiment.

Evidence checked: 2026-11-21. No local execution implied.

- **Open-source software license · verified:** Reviewed the complete project software grant and its redistribution conditions. Model, data and service terms are scoped separately. [Source](https://github.com/0elghati/nvcr/blob/main/LICENSE)
- **Creative results · documented:** The author publishes matched encode and decode measurements for RTX 4070 and Jetson Orin. The comparison measures whole runs including setup and I/O. It documents throughput, not suitability as a standard editorial exchange format. [Source](https://github.com/0elghati/nvcr/blob/main/README.md) [Source](https://github.com/0elghati/nvcr/blob/main/docs/compatibility.md) [Source](https://github.com/0elghati/nvcr/blob/main/docs/first-run.md) [Source](https://github.com/0elghati/nvcr/blob/main/results/README.md)
- **Reproducible setup · documented:** The installation and first-use steps are in the cited documentation. Reproduction of this workflow remains unverified. [Source](https://github.com/0elghati/nvcr/blob/main/README.md) [Source](https://github.com/0elghati/nvcr/blob/main/docs/compatibility.md) [Source](https://github.com/0elghati/nvcr/blob/main/docs/first-run.md) [Source](https://github.com/0elghati/nvcr/blob/main/results/README.md)
- **Maintenance and support · documented:** Release v1.6.0 and the compatibility docs provide a current map of target support. Independent post-production use and visual fidelity remain unverified. [Source](https://github.com/0elghati/nvcr/releases/tag/v1.6.0)
- **Independent use · unknown:** Independent first-hand use of the exact workflow was not established in this source review.
- **Models, services and costs · documented:** The C++ runtime has an MIT code grant. Codec, engine, model and proprietary GPU runtime terms remain separate. Validate the chosen published DCVC bundle terms before reuse. Local inference requires supported compute and storage for engines and bitstreams. Container and vendor software terms may apply. [Source](https://github.com/0elghati/nvcr/blob/main/README.md) [Source](https://github.com/0elghati/nvcr/blob/main/docs/compatibility.md) [Source](https://github.com/0elghati/nvcr/blob/main/docs/first-run.md) [Source](https://github.com/0elghati/nvcr/blob/main/results/README.md)

Source and documentation review. No hands-on execution by AI Media Scout. Some streams are tied to the encoding provider, target or numeric profile. Validate cross-target playback and archive a conventional copy for other collaborators.

### How it uses AI

NVCR packages learned DCVC-RT video compression as a native runtime with reference encode and decode flows. Codec/provider and numeric-mode identifiers govern stream compatibility. [Source](https://github.com/0elghati/nvcr/blob/main/README.md) [Source](https://github.com/0elghati/nvcr/blob/main/docs/compatibility.md) [Source](https://github.com/0elghati/nvcr/blob/main/docs/first-run.md) [Source](https://github.com/0elghati/nvcr/blob/main/results/README.md)

### Introduction

NVCR packages learned DCVC-RT video compression as a native runtime with reference encode and decode flows. Codec/provider and numeric-mode identifiers govern stream compatibility. [Source 1](https://github.com/0elghati/nvcr/blob/main/README.md) [Source 2](https://github.com/0elghati/nvcr/blob/main/docs/compatibility.md) [Source 3](https://github.com/0elghati/nvcr/blob/main/docs/first-run.md) [Source 4](https://github.com/0elghati/nvcr/blob/main/results/README.md)

### What it is good for

Compare learned compression size, performance and image quality on a short rights-cleared motion plate before considering a media transport experiment. [Source 1](https://github.com/0elghati/nvcr/blob/main/README.md) [Source 2](https://github.com/0elghati/nvcr/blob/main/docs/compatibility.md) [Source 3](https://github.com/0elghati/nvcr/blob/main/docs/first-run.md) [Source 4](https://github.com/0elghati/nvcr/blob/main/results/README.md)

### Demo & examples

The author publishes matched encode and decode measurements for RTX 4070 and Jetson Orin. The comparison measures whole runs including setup and I/O. It documents throughput, not suitability as a standard editorial exchange format. [Source 1](https://github.com/0elghati/nvcr/blob/main/README.md) [Source 2](https://github.com/0elghati/nvcr/blob/main/docs/compatibility.md) [Source 3](https://github.com/0elghati/nvcr/blob/main/docs/first-run.md) [Source 4](https://github.com/0elghati/nvcr/blob/main/results/README.md)

### Install

Follow the documented route for the scoped workflow. The steps below are source references. [Source 1](https://github.com/0elghati/nvcr/blob/main/README.md) [Source 2](https://github.com/0elghati/nvcr/blob/main/docs/compatibility.md) [Source 3](https://github.com/0elghati/nvcr/blob/main/docs/first-run.md) [Source 4](https://github.com/0elghati/nvcr/blob/main/results/README.md)

1. Review the compatibility matrix for the target, precision mode and publication tag. Choose a catalog engine for the exact GPU and runtime or the documented Jetson route.
2. Begin with a small reference clip and the first-run instructions for the selected platform. Preserve source frames and an ordinary editorial copy.
### First project

A small first project makes the input, model output and handoff easy to inspect. [Source 1](https://github.com/0elghati/nvcr/blob/main/README.md) [Source 2](https://github.com/0elghati/nvcr/blob/main/docs/compatibility.md) [Source 3](https://github.com/0elghati/nvcr/blob/main/docs/first-run.md) [Source 4](https://github.com/0elghati/nvcr/blob/main/results/README.md)

1. Encode and then decode the same short motion clip with a supported codec profile.
2. Compare decoded frames with the source and retain artifacts, engine identifiers, throughput and storage measurements together.
3. Check a receiving system against the cross-target profile before transferring a test stream.
### Hardware & software

Platform and compute constraints refer to the selected route. [Source 1](https://github.com/0elghati/nvcr/blob/main/README.md) [Source 2](https://github.com/0elghati/nvcr/blob/main/docs/compatibility.md) [Source 3](https://github.com/0elghati/nvcr/blob/main/docs/first-run.md) [Source 4](https://github.com/0elghati/nvcr/blob/main/results/README.md)

- **Hardware:** The published default requires an NVIDIA GPU present in the engine catalog. Minimum universal VRAM, RAM and disk are undocumented. The compatibility matrix specifies supported examples.
- **Software:** The documented x86_64 native route uses Ubuntu 24.04, CUDA 12.8 and TensorRT 10.9. DCVC-RT requires its compatible weights and engine. MLVC is an additional experimental integration.
- **Platforms:** Ubuntu 24.04 x86_64 with Nvidia, Jetson Orin, and documented Windows 11 Docker Desktop with WSL 2. CPU contract validation covers a separate test path.

### License, model weights & costs

The full software license was reviewed. Dependencies and creative assets carry their own terms. [Source 1](https://github.com/0elghati/nvcr/blob/main/LICENSE) [Source 2](https://github.com/0elghati/nvcr/blob/main/README.md) [Source 3](https://github.com/0elghati/nvcr/blob/main/docs/compatibility.md) [Source 4](https://github.com/0elghati/nvcr/blob/main/docs/first-run.md) [Source 5](https://github.com/0elghati/nvcr/blob/main/results/README.md)

- **Code:** MIT
- **Weights:** The C++ runtime has an MIT code grant. Codec, engine, model and proprietary GPU runtime terms remain separate. Validate the chosen published DCVC bundle terms before reuse.
- **Commercial:** Project code is governed by MIT. Confirm selected model, source-media and output restrictions separately.
- **Cost:** Local inference requires supported compute and storage for engines and bitstreams. Container and vendor software terms may apply.

### Why it merits attention

The creative workflow is grounded in the cited documentation. Output quality and compatibility are not hands-on verified. [Source 1](https://github.com/0elghati/nvcr/blob/main/README.md) [Source 2](https://github.com/0elghati/nvcr/blob/main/docs/compatibility.md) [Source 3](https://github.com/0elghati/nvcr/blob/main/docs/first-run.md) [Source 4](https://github.com/0elghati/nvcr/blob/main/results/README.md)

### Limitations

Some streams are tied to the encoding provider, target or numeric profile. Validate cross-target playback and archive a conventional copy for other collaborators. [Source 1](https://github.com/0elghati/nvcr/blob/main/README.md) [Source 2](https://github.com/0elghati/nvcr/blob/main/docs/compatibility.md) [Source 3](https://github.com/0elghati/nvcr/blob/main/docs/first-run.md) [Source 4](https://github.com/0elghati/nvcr/blob/main/results/README.md)

### Get the tool

- [Repository](https://github.com/0elghati/nvcr)
- [Documentation](https://github.com/0elghati/nvcr/blob/main/results/README.md)

## AutoMaya MCP

3D, reconstruction & assets · AI agents for code-authored media production · VFX, compositing & relighting

First complete guide in the library. The publication and documentation dates are not necessarily the project’s launch date.

### Quality assessment: Quality unverified

Creative use and the code grant are documented. Check-level gaps remain before a recommendation.

Scope: Block a small Maya shot or import an AI mesh candidate, then inspect topology, materials and the undo history in a scratch scene.

Evidence checked: 2026-11-21. No local execution implied.

- **Open-source software license · verified:** Reviewed the complete project software grant and its redistribution conditions. Model, data and service terms are scoped separately. [Source](https://github.com/CallMeParams/automaya-mcp/blob/main/LICENSE)
- **Creative results · documented:** The author documents live scene queries, captured viewport images and mesh previews. Exact supported provider behavior and mesh quality need testing with the intended scene and client. [Source](https://github.com/CallMeParams/automaya-mcp/blob/main/README.md) [Source](https://github.com/CallMeParams/automaya-mcp/blob/main/pyproject.toml)
- **Reproducible setup · documented:** The installation and first-use steps are in the cited documentation. Reproduction of this workflow remains unverified. [Source](https://github.com/CallMeParams/automaya-mcp/blob/main/README.md) [Source](https://github.com/CallMeParams/automaya-mcp/blob/main/pyproject.toml)
- **Maintenance and support · unknown:** The reviewed sources do not establish workflow-specific support, fixes and unresolved blockers.
- **Independent use · unknown:** Independent first-hand use of the exact workflow was not established in this source review.
- **Models, services and costs · documented:** The bridge code is MIT. Maya is a proprietary required host. Models, generated assets, remote asset libraries and external providers use separate terms. Maya licensing and any selected external mesh or agent service can incur charges. A provider subscription is separate from bridge code. [Source](https://github.com/CallMeParams/automaya-mcp/blob/main/README.md) [Source](https://github.com/CallMeParams/automaya-mcp/blob/main/pyproject.toml)

Source and documentation review. No hands-on execution by AI Media Scout. Agents can modify the scene and the plugin documents an enabled local bridge. Use a scratch scene and review provider/data flow, undo and complete project assets.

### How it uses AI

AutoMaya MCP exposes Maya modeling and lighting actions to an agent and documents external AI mesh-generation connections. An in-Maya change feed and undo chunks are documented for reviewing agent operations. [Source](https://github.com/CallMeParams/automaya-mcp/blob/main/README.md) [Source](https://github.com/CallMeParams/automaya-mcp/blob/main/pyproject.toml)

### Introduction

AutoMaya MCP exposes Maya modeling and lighting actions to an agent and documents external AI mesh-generation connections. An in-Maya change feed and undo chunks are documented for reviewing agent operations. [Source 1](https://github.com/CallMeParams/automaya-mcp/blob/main/README.md) [Source 2](https://github.com/CallMeParams/automaya-mcp/blob/main/pyproject.toml)

### What it is good for

Block a small Maya shot or import an AI mesh candidate, then inspect topology, materials and the undo history in a scratch scene. [Source 1](https://github.com/CallMeParams/automaya-mcp/blob/main/README.md) [Source 2](https://github.com/CallMeParams/automaya-mcp/blob/main/pyproject.toml)

### Demo & examples

The author documents live scene queries, captured viewport images and mesh previews. Exact supported provider behavior and mesh quality need testing with the intended scene and client. [Source 1](https://github.com/CallMeParams/automaya-mcp/blob/main/README.md) [Source 2](https://github.com/CallMeParams/automaya-mcp/blob/main/pyproject.toml)

### Install

Follow the documented route for the scoped workflow. The steps below are source references. [Source 1](https://github.com/CallMeParams/automaya-mcp/blob/main/README.md) [Source 2](https://github.com/CallMeParams/automaya-mcp/blob/main/pyproject.toml)

1. Use the published source setup for Maya 2024 and the documented Python route. Install the project module to the user Maya modules folder and restart the host.
2. Configure the named local MCP client connection. Review the provider setup only if the scoped workflow uses generated assets.
### First project

A small first project makes the input, model output and handoff easy to inspect. [Source 1](https://github.com/CallMeParams/automaya-mcp/blob/main/README.md) [Source 2](https://github.com/CallMeParams/automaya-mcp/blob/main/pyproject.toml)

1. Start with a duplicate test scene and request the current scene state and an isolated object edit.
2. Inspect the resulting mesh or camera view against the authoring brief and test undo on the isolated change.
3. For a generated asset, check materials, topology, files and provider terms before moving it to the production scene.
### Hardware & software

Platform and compute constraints refer to the selected route. [Source 1](https://github.com/CallMeParams/automaya-mcp/blob/main/README.md) [Source 2](https://github.com/CallMeParams/automaya-mcp/blob/main/pyproject.toml)

- **Hardware:** Minimum RAM, VRAM and disk space for the scoped workflow are undocumented.
- **Software:** Autodesk Maya 2024, the repository Python/Maya environment and a compatible MCP client. External mesh-generation services are optional routes with their own requirements.
- **Platforms:** Windows-oriented Maya module and deployment examples are documented. Confirm precise support for any different host combination.

### License, model weights & costs

The full software license was reviewed. Dependencies and creative assets carry their own terms. [Source 1](https://github.com/CallMeParams/automaya-mcp/blob/main/LICENSE) [Source 2](https://github.com/CallMeParams/automaya-mcp/blob/main/README.md) [Source 3](https://github.com/CallMeParams/automaya-mcp/blob/main/pyproject.toml)

- **Code:** MIT
- **Weights:** The bridge code is MIT. Maya is a proprietary required host. Models, generated assets, remote asset libraries and external providers use separate terms.
- **Commercial:** Project code is governed by MIT. Confirm selected model, source-media and output restrictions separately.
- **Cost:** Maya licensing and any selected external mesh or agent service can incur charges. A provider subscription is separate from bridge code.

### Why it merits attention

The creative workflow is grounded in the cited documentation. Output quality and compatibility are not hands-on verified. [Source 1](https://github.com/CallMeParams/automaya-mcp/blob/main/README.md) [Source 2](https://github.com/CallMeParams/automaya-mcp/blob/main/pyproject.toml)

### Limitations

Agents can modify the scene and the plugin documents an enabled local bridge. Use a scratch scene and review provider/data flow, undo and complete project assets. [Source 1](https://github.com/CallMeParams/automaya-mcp/blob/main/README.md) [Source 2](https://github.com/CallMeParams/automaya-mcp/blob/main/pyproject.toml)

### Get the tool

- [Repository](https://github.com/CallMeParams/automaya-mcp)
- [Documentation](https://github.com/CallMeParams/automaya-mcp/blob/main/pyproject.toml)

## ai-3d-video

Storyboarding, narrative & comics · Avatars, digital humans & lip sync · AI cel animation and inbetweening

This completes an earlier pending guide with a current source review.

### Quality assessment: Quality unverified

Creative use and the code grant are documented. Check-level gaps remain before a recommendation.

Scope: Prototype a short recurring-character sketch, export a vertical MP4 and keep an SRT for caption editing.

Evidence checked: 2026-11-21. No local execution implied.

- **Open-source software license · verified:** Reviewed the complete project software grant and its redistribution conditions. Model, data and service terms are scoped separately. [Source](https://github.com/sooooooooo101/ai-3d-video/blob/main/LICENSE)
- **Creative results · documented:** The repository supplies a staged sample and its dialogue plan. Compare the planned pauses, inferred spoken delivery and the final mouth animation against the original brief. [Source](https://github.com/sooooooooo101/ai-3d-video/blob/main/README.md) [Source](https://github.com/sooooooooo101/ai-3d-video/blob/main/templates/kikaku.md) [Source](https://github.com/sooooooooo101/ai-3d-video/blob/main/examples/uketsuke-dake/dialogue.json)
- **Reproducible setup · documented:** The installation and first-use steps are in the cited documentation. Reproduction of this workflow remains unverified. [Source](https://github.com/sooooooooo101/ai-3d-video/blob/main/README.md) [Source](https://github.com/sooooooooo101/ai-3d-video/blob/main/templates/kikaku.md) [Source](https://github.com/sooooooooo101/ai-3d-video/blob/main/examples/uketsuke-dake/dialogue.json)
- **Maintenance and support · unknown:** The reviewed sources do not establish workflow-specific support, fixes and unresolved blockers.
- **Independent use · unknown:** Independent first-hand use of the exact workflow was not established in this source review.
- **Models, services and costs · documented:** Repository code is MIT and the README identifies generated bundled background audio under MIT. VOICEVOX voices have individual usage and credit terms. Check the selected character and asset. Local rendering and synthesis use compute. A separately connected authoring model may use a metered plan. [Source](https://github.com/sooooooooo101/ai-3d-video/blob/main/README.md) [Source](https://github.com/sooooooooo101/ai-3d-video/blob/main/templates/kikaku.md) [Source](https://github.com/sooooooooo101/ai-3d-video/blob/main/examples/uketsuke-dake/dialogue.json)

Source and documentation review. No hands-on execution by AI Media Scout. English agent reference and Japanese author documentation differ in audience. Volume-driven mouth motion and the supported stage assets constrain animation detail.

### How it uses AI

This Three.js workflow uses an agent to turn a Japanese creative brief into recurring character scenes. VOICEVOX generates speech and the pipeline turns measured audio intensity into mouth motion. [Source](https://github.com/sooooooooo101/ai-3d-video/blob/main/README.md) [Source](https://github.com/sooooooooo101/ai-3d-video/blob/main/templates/kikaku.md) [Source](https://github.com/sooooooooo101/ai-3d-video/blob/main/examples/uketsuke-dake/dialogue.json)

### Introduction

This Three.js workflow uses an agent to turn a Japanese creative brief into recurring character scenes. VOICEVOX generates speech and the pipeline turns measured audio intensity into mouth motion. [Source 1](https://github.com/sooooooooo101/ai-3d-video/blob/main/README.md) [Source 2](https://github.com/sooooooooo101/ai-3d-video/blob/main/templates/kikaku.md) [Source 3](https://github.com/sooooooooo101/ai-3d-video/blob/main/examples/uketsuke-dake/dialogue.json)

### What it is good for

Prototype a short recurring-character sketch, export a vertical MP4 and keep an SRT for caption editing. [Source 1](https://github.com/sooooooooo101/ai-3d-video/blob/main/README.md) [Source 2](https://github.com/sooooooooo101/ai-3d-video/blob/main/templates/kikaku.md) [Source 3](https://github.com/sooooooooo101/ai-3d-video/blob/main/examples/uketsuke-dake/dialogue.json)

### Demo & examples

The repository supplies a staged sample and its dialogue plan. Compare the planned pauses, inferred spoken delivery and the final mouth animation against the original brief. [Source 1](https://github.com/sooooooooo101/ai-3d-video/blob/main/README.md) [Source 2](https://github.com/sooooooooo101/ai-3d-video/blob/main/templates/kikaku.md) [Source 3](https://github.com/sooooooooo101/ai-3d-video/blob/main/examples/uketsuke-dake/dialogue.json)

### Install

Follow the documented route for the scoped workflow. The steps below are source references. [Source 1](https://github.com/sooooooooo101/ai-3d-video/blob/main/README.md) [Source 2](https://github.com/sooooooooo101/ai-3d-video/blob/main/templates/kikaku.md) [Source 3](https://github.com/sooooooooo101/ai-3d-video/blob/main/examples/uketsuke-dake/dialogue.json)

1. Follow the manual workflow in the source documentation. Prepare Python 3.9+, FFmpeg, Chrome or Chromium and a running VOICEVOX engine.
2. Open the included sandbox example and copy the editable plan and permitted assets to a working folder.
### First project

A small first project makes the input, model output and handoff easy to inspect. [Source 1](https://github.com/sooooooooo101/ai-3d-video/blob/main/README.md) [Source 2](https://github.com/sooooooooo101/ai-3d-video/blob/main/templates/kikaku.md) [Source 3](https://github.com/sooooooooo101/ai-3d-video/blob/main/examples/uketsuke-dake/dialogue.json)

1. Fill out the Japanese brief with a cast, setting, timings and dialogue. Review generated actions before rendering.
2. Build the voice track and inspect the shot contact sheet for the intent of each beat.
3. Render the selected aspect ratio with separate subtitles or burn them in when that suits delivery.
### Hardware & software

Platform and compute constraints refer to the selected route. [Source 1](https://github.com/sooooooooo101/ai-3d-video/blob/main/README.md) [Source 2](https://github.com/sooooooooo101/ai-3d-video/blob/main/templates/kikaku.md) [Source 3](https://github.com/sooooooooo101/ai-3d-video/blob/main/examples/uketsuke-dake/dialogue.json)

- **Hardware:** Minimum RAM, VRAM and disk space for the scoped workflow are undocumented.
- **Software:** Python 3.9+, FFmpeg, Chrome or Chromium and VOICEVOX. An agent is an optional authoring route for script and blocking.
- **Platforms:** Author documents macOS testing and says Windows/Linux have not been tested by the project. Subtitle font paths vary by system.

### License, model weights & costs

The full software license was reviewed. Dependencies and creative assets carry their own terms. [Source 1](https://github.com/sooooooooo101/ai-3d-video/blob/main/LICENSE) [Source 2](https://github.com/sooooooooo101/ai-3d-video/blob/main/README.md) [Source 3](https://github.com/sooooooooo101/ai-3d-video/blob/main/templates/kikaku.md) [Source 4](https://github.com/sooooooooo101/ai-3d-video/blob/main/examples/uketsuke-dake/dialogue.json)

- **Code:** MIT
- **Weights:** Repository code is MIT and the README identifies generated bundled background audio under MIT. VOICEVOX voices have individual usage and credit terms. Check the selected character and asset.
- **Commercial:** Project code is governed by MIT. Confirm selected model, source-media and output restrictions separately.
- **Cost:** Local rendering and synthesis use compute. A separately connected authoring model may use a metered plan.

### Why it merits attention

The creative workflow is grounded in the cited documentation. Output quality and compatibility are not hands-on verified. [Source 1](https://github.com/sooooooooo101/ai-3d-video/blob/main/README.md) [Source 2](https://github.com/sooooooooo101/ai-3d-video/blob/main/templates/kikaku.md) [Source 3](https://github.com/sooooooooo101/ai-3d-video/blob/main/examples/uketsuke-dake/dialogue.json)

### Limitations

English agent reference and Japanese author documentation differ in audience. Volume-driven mouth motion and the supported stage assets constrain animation detail. [Source 1](https://github.com/sooooooooo101/ai-3d-video/blob/main/README.md) [Source 2](https://github.com/sooooooooo101/ai-3d-video/blob/main/templates/kikaku.md) [Source 3](https://github.com/sooooooooo101/ai-3d-video/blob/main/examples/uketsuke-dake/dialogue.json)

### Get the tool

- [Repository](https://github.com/sooooooooo101/ai-3d-video)
- [Documentation](https://github.com/sooooooooo101/ai-3d-video/blob/main/examples/uketsuke-dake/dialogue.json)

## Atlas Forge

AI cartography and artistic maps · Interactive neural game worlds · Data art & scientific visualization

The source repository was created on 2026-11-17. This is its first complete guide in the library.

### Quality assessment: Quality unverified

Creative use and the code grant are documented. Check-level gaps remain before a recommendation.

Scope: Draft a believable campaign map with settlements and rivers, compare changes for one historical period, and export vector art for later layout.

Evidence checked: 2026-11-21. No local execution implied.

- **Open-source software license · verified:** Reviewed the complete project software grant and its redistribution conditions. Model, data and service terms are scoped separately. [Source](https://github.com/UnknownGlyph/atlas-forge/blob/main/LICENSE)
- **Creative results · documented:** The authors archived two different model attempts from an empty map and documented resulting borders, settlements and validity checks. These are author trials. [Source](https://github.com/UnknownGlyph/atlas-forge/blob/main/README.md) [Source](https://github.com/UnknownGlyph/atlas-forge/blob/main/docs/STEPS.md) [Source](https://github.com/UnknownGlyph/atlas-forge/blob/main/docs/API.md) [Source](https://github.com/UnknownGlyph/atlas-forge/blob/main/docs/CREATION_WORKSPACES.md)
- **Reproducible setup · documented:** The installation and first-use steps are in the cited documentation. Reproduction of this workflow remains unverified. [Source](https://github.com/UnknownGlyph/atlas-forge/blob/main/README.md) [Source](https://github.com/UnknownGlyph/atlas-forge/blob/main/docs/STEPS.md) [Source](https://github.com/UnknownGlyph/atlas-forge/blob/main/docs/API.md) [Source](https://github.com/UnknownGlyph/atlas-forge/blob/main/docs/CREATION_WORKSPACES.md)
- **Maintenance and support · documented:** The current alpha and author trials document editing and renderer changes, with compatibility outside the Windows package unverified. [Source](https://github.com/UnknownGlyph/atlas-forge/releases/tag/v0.2.2-alpha)
- **Independent use · unknown:** Independent first-hand use of the exact workflow was not established in this source review.
- **Models, services and costs · documented:** MIT applies to Atlas Forge code. The bundled font follows the SIL Open Font License. Model endpoints and imported map data require their own terms review. The local editor uses local compute. Gemini, Anthropic, OpenAI or other connected provider costs depend on the selected endpoint. [Source](https://github.com/UnknownGlyph/atlas-forge/blob/main/README.md) [Source](https://github.com/UnknownGlyph/atlas-forge/blob/main/docs/STEPS.md) [Source](https://github.com/UnknownGlyph/atlas-forge/blob/main/docs/API.md) [Source](https://github.com/UnknownGlyph/atlas-forge/blob/main/docs/CREATION_WORKSPACES.md)

Source and documentation review. No hands-on execution by AI Media Scout. The Windows release is explicitly alpha. For multi-year edits, validate boundary topology, ownership and timeline continuity before adopting a model-generated draft.

### How it uses AI

Atlas Forge lets a language model create and edit fictional-world geometry, settlements and dated events through the same structured tools as its map interface. AI edits are staged in a reviewable draft. [Source](https://github.com/UnknownGlyph/atlas-forge/blob/main/README.md) [Source](https://github.com/UnknownGlyph/atlas-forge/blob/main/docs/STEPS.md) [Source](https://github.com/UnknownGlyph/atlas-forge/blob/main/docs/API.md) [Source](https://github.com/UnknownGlyph/atlas-forge/blob/main/docs/CREATION_WORKSPACES.md)

### Introduction

Atlas Forge lets a language model create and edit fictional-world geometry, settlements and dated events through the same structured tools as its map interface. AI edits are staged in a reviewable draft. [Source 1](https://github.com/UnknownGlyph/atlas-forge/blob/main/README.md) [Source 2](https://github.com/UnknownGlyph/atlas-forge/blob/main/docs/STEPS.md) [Source 3](https://github.com/UnknownGlyph/atlas-forge/blob/main/docs/API.md) [Source 4](https://github.com/UnknownGlyph/atlas-forge/blob/main/docs/CREATION_WORKSPACES.md)

### What it is good for

Draft a believable campaign map with settlements and rivers, compare changes for one historical period, and export vector art for later layout. [Source 1](https://github.com/UnknownGlyph/atlas-forge/blob/main/README.md) [Source 2](https://github.com/UnknownGlyph/atlas-forge/blob/main/docs/STEPS.md) [Source 3](https://github.com/UnknownGlyph/atlas-forge/blob/main/docs/API.md) [Source 4](https://github.com/UnknownGlyph/atlas-forge/blob/main/docs/CREATION_WORKSPACES.md)

### Demo & examples

The authors archived two different model attempts from an empty map and documented resulting borders, settlements and validity checks. These are author trials. [Source 1](https://github.com/UnknownGlyph/atlas-forge/blob/main/README.md) [Source 2](https://github.com/UnknownGlyph/atlas-forge/blob/main/docs/STEPS.md) [Source 3](https://github.com/UnknownGlyph/atlas-forge/blob/main/docs/API.md) [Source 4](https://github.com/UnknownGlyph/atlas-forge/blob/main/docs/CREATION_WORKSPACES.md)

### Install

Follow the documented route for the scoped workflow. The steps below are source references. [Source 1](https://github.com/UnknownGlyph/atlas-forge/blob/main/README.md) [Source 2](https://github.com/UnknownGlyph/atlas-forge/blob/main/docs/STEPS.md) [Source 3](https://github.com/UnknownGlyph/atlas-forge/blob/main/docs/API.md) [Source 4](https://github.com/UnknownGlyph/atlas-forge/blob/main/docs/CREATION_WORKSPACES.md)

1. Use the documented Windows 10/11 x64 alpha archive and a graphics device with a supported API. Launch the desktop editor.
2. If using AI, choose a documented endpoint or an existing MCP client, then prepare a separate draft world.
### First project

A small first project makes the input, model output and handoff easy to inspect. [Source 1](https://github.com/UnknownGlyph/atlas-forge/blob/main/README.md) [Source 2](https://github.com/UnknownGlyph/atlas-forge/blob/main/docs/STEPS.md) [Source 3](https://github.com/UnknownGlyph/atlas-forge/blob/main/docs/API.md) [Source 4](https://github.com/UnknownGlyph/atlas-forge/blob/main/docs/CREATION_WORKSPACES.md)

1. Open an included world or create a simple schematic. Request one specific terrain or historical change.
2. Check the before and after rendering, settlement positions, layer attributes and time range. Apply the draft after reviewing it.
3. Export SVG, PDF or PNG with the desired legend and time point. Keep the editable world draft and export record.
### Hardware & software

Platform and compute constraints refer to the selected route. [Source 1](https://github.com/UnknownGlyph/atlas-forge/blob/main/README.md) [Source 2](https://github.com/UnknownGlyph/atlas-forge/blob/main/docs/STEPS.md) [Source 3](https://github.com/UnknownGlyph/atlas-forge/blob/main/docs/API.md) [Source 4](https://github.com/UnknownGlyph/atlas-forge/blob/main/docs/CREATION_WORKSPACES.md)

- **Hardware:** The package lists DirectX 12, Vulkan or OpenGL graphics support. Reported memory or storage minima are undocumented for this workflow.
- **Software:** Windows alpha release. Source build documents Rust stable, MSVC and Visual Studio C++ tools. Model use requires a selected compatible endpoint or MCP client.
- **Platforms:** v0.2.2-alpha Windows x64 package. The author states macOS and Linux have not yet been built or tested.

### License, model weights & costs

The full software license was reviewed. Dependencies and creative assets carry their own terms. [Source 1](https://github.com/UnknownGlyph/atlas-forge/blob/main/LICENSE) [Source 2](https://github.com/UnknownGlyph/atlas-forge/blob/main/README.md) [Source 3](https://github.com/UnknownGlyph/atlas-forge/blob/main/docs/STEPS.md) [Source 4](https://github.com/UnknownGlyph/atlas-forge/blob/main/docs/API.md) [Source 5](https://github.com/UnknownGlyph/atlas-forge/blob/main/docs/CREATION_WORKSPACES.md)

- **Code:** MIT
- **Weights:** MIT applies to Atlas Forge code. The bundled font follows the SIL Open Font License. Model endpoints and imported map data require their own terms review.
- **Commercial:** Project code is governed by MIT. Confirm selected model, source-media and output restrictions separately.
- **Cost:** The local editor uses local compute. Gemini, Anthropic, OpenAI or other connected provider costs depend on the selected endpoint.

### Why it merits attention

The creative workflow is grounded in the cited documentation. Output quality and compatibility are not hands-on verified. [Source 1](https://github.com/UnknownGlyph/atlas-forge/blob/main/README.md) [Source 2](https://github.com/UnknownGlyph/atlas-forge/blob/main/docs/STEPS.md) [Source 3](https://github.com/UnknownGlyph/atlas-forge/blob/main/docs/API.md) [Source 4](https://github.com/UnknownGlyph/atlas-forge/blob/main/docs/CREATION_WORKSPACES.md)

### Limitations

The Windows release is explicitly alpha. For multi-year edits, validate boundary topology, ownership and timeline continuity before adopting a model-generated draft. [Source 1](https://github.com/UnknownGlyph/atlas-forge/blob/main/README.md) [Source 2](https://github.com/UnknownGlyph/atlas-forge/blob/main/docs/STEPS.md) [Source 3](https://github.com/UnknownGlyph/atlas-forge/blob/main/docs/API.md) [Source 4](https://github.com/UnknownGlyph/atlas-forge/blob/main/docs/CREATION_WORKSPACES.md)

### Get the tool

- [Repository](https://github.com/UnknownGlyph/atlas-forge)
- [Documentation](https://github.com/UnknownGlyph/atlas-forge/blob/main/docs/CREATION_WORKSPACES.md)

## ComfyUI Video Workflows

Video, animation & film · AI visual dubbing and translated performance · Neural relighting and material recovery

This completes an earlier pending guide with a current source review.

### Quality assessment: Quality unverified

Creative use and the code grant are documented. Check-level gaps remain before a recommendation.

Scope: Compare a selected start/end-frame dialogue graph against a short WAV before committing to a generated shot.

Evidence checked: 2026-11-21. No local execution implied.

- **Open-source software license · verified:** Reviewed the complete project software grant and its redistribution conditions. Model, data and service terms are scoped separately. [Source](https://github.com/idnn-productions/comfy-ui-video-workflows/blob/main/LICENSE)
- **Creative results · documented:** The author provides a Windows 11/RTX 4090 setup log and workflow-specific input conventions. Performance pertains to that build and model set. [Source](https://github.com/idnn-productions/comfy-ui-video-workflows/blob/main/README.md) [Source](https://github.com/idnn-productions/comfy-ui-video-workflows/blob/main/SETUP-RTX4090.md) [Source](https://github.com/idnn-productions/comfy-ui-video-workflows/blob/main/pins.json)
- **Reproducible setup · documented:** The installation and first-use steps are in the cited documentation. Reproduction of this workflow remains unverified. [Source](https://github.com/idnn-productions/comfy-ui-video-workflows/blob/main/README.md) [Source](https://github.com/idnn-productions/comfy-ui-video-workflows/blob/main/SETUP-RTX4090.md) [Source](https://github.com/idnn-productions/comfy-ui-video-workflows/blob/main/pins.json)
- **Maintenance and support · unknown:** The reviewed sources do not establish workflow-specific support, fixes and unresolved blockers.
- **Independent use · unknown:** Independent first-hand use of the exact workflow was not established in this source review.
- **Models, services and costs · documented:** MIT covers the workflow JSON and the custom ElevenLabs node code. Model weights, third-party nodes, voice recordings and optional ElevenLabs use have their own terms. Local rendering uses GPU compute and model storage. The optional external voice API has separate fees and terms. [Source](https://github.com/idnn-productions/comfy-ui-video-workflows/blob/main/README.md) [Source](https://github.com/idnn-productions/comfy-ui-video-workflows/blob/main/SETUP-RTX4090.md) [Source](https://github.com/idnn-productions/comfy-ui-video-workflows/blob/main/pins.json)

Source and documentation review. No hands-on execution by AI Media Scout. Node and Torch version drift affects some graphs. The setup documentation identifies required fixes for the LatentSync enhanced path. Independent output and exact lip sync are unverified.

### How it uses AI

This collection ships ComfyUI graphs for neural motion, talking-head sync, music-driven video and relighting. Canvas labels identify the file inputs and resulting clips. [Source](https://github.com/idnn-productions/comfy-ui-video-workflows/blob/main/README.md) [Source](https://github.com/idnn-productions/comfy-ui-video-workflows/blob/main/SETUP-RTX4090.md) [Source](https://github.com/idnn-productions/comfy-ui-video-workflows/blob/main/pins.json)

### Introduction

This collection ships ComfyUI graphs for neural motion, talking-head sync, music-driven video and relighting. Canvas labels identify the file inputs and resulting clips. [Source 1](https://github.com/idnn-productions/comfy-ui-video-workflows/blob/main/README.md) [Source 2](https://github.com/idnn-productions/comfy-ui-video-workflows/blob/main/SETUP-RTX4090.md) [Source 3](https://github.com/idnn-productions/comfy-ui-video-workflows/blob/main/pins.json)

### What it is good for

Compare a selected start/end-frame dialogue graph against a short WAV before committing to a generated shot. [Source 1](https://github.com/idnn-productions/comfy-ui-video-workflows/blob/main/README.md) [Source 2](https://github.com/idnn-productions/comfy-ui-video-workflows/blob/main/SETUP-RTX4090.md) [Source 3](https://github.com/idnn-productions/comfy-ui-video-workflows/blob/main/pins.json)

### Demo & examples

The author provides a Windows 11/RTX 4090 setup log and workflow-specific input conventions. Performance pertains to that build and model set. [Source 1](https://github.com/idnn-productions/comfy-ui-video-workflows/blob/main/README.md) [Source 2](https://github.com/idnn-productions/comfy-ui-video-workflows/blob/main/SETUP-RTX4090.md) [Source 3](https://github.com/idnn-productions/comfy-ui-video-workflows/blob/main/pins.json)

### Install

Follow the documented route for the scoped workflow. The steps below are source references. [Source 1](https://github.com/idnn-productions/comfy-ui-video-workflows/blob/main/README.md) [Source 2](https://github.com/idnn-productions/comfy-ui-video-workflows/blob/main/SETUP-RTX4090.md) [Source 3](https://github.com/idnn-productions/comfy-ui-video-workflows/blob/main/pins.json)

1. Use the declared ComfyUI version and choose one workflow. Open the file in ComfyUI and inspect the required nodes, versions and model file names.
2. Use the project’s setup notes to place required models for that graph only. Review model terms before use.
### First project

A small first project makes the input, model output and handoff easy to inspect. [Source 1](https://github.com/idnn-productions/comfy-ui-video-workflows/blob/main/README.md) [Source 2](https://github.com/idnn-productions/comfy-ui-video-workflows/blob/main/SETUP-RTX4090.md) [Source 3](https://github.com/idnn-productions/comfy-ui-video-workflows/blob/main/pins.json)

1. Set start and end images and a short rights-cleared WAV. Provide true speech duration and set lead-in and tail time.
2. Render a short clip. Compare pauses and visible mouth movement with the WAV, and inspect identity stability near the edit points.
3. Keep the graph, input identifiers, model and seed references, and the selected output clip for the next edit.
### Hardware & software

Platform and compute constraints refer to the selected route. [Source 1](https://github.com/idnn-productions/comfy-ui-video-workflows/blob/main/README.md) [Source 2](https://github.com/idnn-productions/comfy-ui-video-workflows/blob/main/SETUP-RTX4090.md) [Source 3](https://github.com/idnn-productions/comfy-ui-video-workflows/blob/main/pins.json)

- **Hardware:** The author reports RTX 4090 24 GB and workflow peaks of 22–24 GB with additional offload to system RAM. This is a setup report. Lower hardware minima are undocumented.
- **Software:** Recent ComfyUI and graph-specific models. Some graphs require extra nodes. ElevenLabs integration is optional and uses an external account.
- **Platforms:** Author’s exact configuration is Windows 11 on an RTX 4090. Other platform configurations are unverified for these workflow pins.

### License, model weights & costs

The full software license was reviewed. Dependencies and creative assets carry their own terms. [Source 1](https://github.com/idnn-productions/comfy-ui-video-workflows/blob/main/LICENSE) [Source 2](https://github.com/idnn-productions/comfy-ui-video-workflows/blob/main/README.md) [Source 3](https://github.com/idnn-productions/comfy-ui-video-workflows/blob/main/SETUP-RTX4090.md) [Source 4](https://github.com/idnn-productions/comfy-ui-video-workflows/blob/main/pins.json)

- **Code:** MIT
- **Weights:** MIT covers the workflow JSON and the custom ElevenLabs node code. Model weights, third-party nodes, voice recordings and optional ElevenLabs use have their own terms.
- **Commercial:** Project code is governed by MIT. Confirm selected model, source-media and output restrictions separately.
- **Cost:** Local rendering uses GPU compute and model storage. The optional external voice API has separate fees and terms.

### Why it merits attention

The creative workflow is grounded in the cited documentation. Output quality and compatibility are not hands-on verified. [Source 1](https://github.com/idnn-productions/comfy-ui-video-workflows/blob/main/README.md) [Source 2](https://github.com/idnn-productions/comfy-ui-video-workflows/blob/main/SETUP-RTX4090.md) [Source 3](https://github.com/idnn-productions/comfy-ui-video-workflows/blob/main/pins.json)

### Limitations

Node and Torch version drift affects some graphs. The setup documentation identifies required fixes for the LatentSync enhanced path. Independent output and exact lip sync are unverified. [Source 1](https://github.com/idnn-productions/comfy-ui-video-workflows/blob/main/README.md) [Source 2](https://github.com/idnn-productions/comfy-ui-video-workflows/blob/main/SETUP-RTX4090.md) [Source 3](https://github.com/idnn-productions/comfy-ui-video-workflows/blob/main/pins.json)

### Get the tool

- [Repository](https://github.com/idnn-productions/comfy-ui-video-workflows)
- [Documentation](https://github.com/idnn-productions/comfy-ui-video-workflows/blob/main/pins.json)

## Batchalign3

Archives, media restoration & collections · Live production accessibility and routed captions · Creative publishing & presentation

This completes an earlier pending guide with a current source review.

### Quality assessment: Quality unverified

Creative use and the code grant are documented. Check-level gaps remain before a recommendation.

Scope: Draft a transcript and timing track for a short oral-history project, then review each speaker and retain editable annotation data.

Evidence checked: 2026-11-21. No local execution implied.

- **Open-source software license · verified:** Reviewed the complete project software grant and its redistribution conditions. Model, data and service terms are scoped separately. [Source](https://github.com/FranklinChen/talkbank-tools/blob/main/LICENSE)
- **Creative results · documented:** The maintainer’s guide documents named transcription and alignment commands. It distinguishes the CLI from the experimental desktop dashboard and exposes explicit language choices. [Source](https://github.com/FranklinChen/talkbank-tools/blob/main/README.md) [Source](https://github.com/FranklinChen/talkbank-tools/blob/main/docs/PLATFORM-SUPPORT.md) [Source](https://github.com/FranklinChen/talkbank-tools/blob/main/book/src/batchalign/user-guide/quick-start.md) [Source](https://talkbank.org/)
- **Reproducible setup · documented:** The installation and first-use steps are in the cited documentation. Reproduction of this workflow remains unverified. [Source](https://github.com/FranklinChen/talkbank-tools/blob/main/README.md) [Source](https://github.com/FranklinChen/talkbank-tools/blob/main/docs/PLATFORM-SUPPORT.md) [Source](https://github.com/FranklinChen/talkbank-tools/blob/main/book/src/batchalign/user-guide/quick-start.md) [Source](https://talkbank.org/)
- **Maintenance and support · unknown:** The reviewed sources do not establish workflow-specific support, fixes and unresolved blockers.
- **Independent use · unknown:** Independent first-hand use of the exact workflow was not established in this source review.
- **Models, services and costs · documented:** The software license is BSD-3-Clause. Speech and alignment weights, any configured cloud route and corpus permissions require independent review. Local models need compute and storage. A separately selected hosted recognizer can have its own access and fees. [Source](https://github.com/FranklinChen/talkbank-tools/blob/main/README.md) [Source](https://github.com/FranklinChen/talkbank-tools/blob/main/docs/PLATFORM-SUPPORT.md) [Source](https://github.com/FranklinChen/talkbank-tools/blob/main/book/src/batchalign/user-guide/quick-start.md) [Source](https://talkbank.org/)

Source and documentation review. No hands-on execution by AI Media Scout. Keep the CLI and language/ASR choice explicit. Proper names, mixed-language passages and overlapping speech can need substantial editing.

### How it uses AI

Batchalign3 uses speech recognition, forced alignment and other learned language operations to produce time-linked CHAT transcripts from audio or enrich existing annotations. [Source](https://github.com/FranklinChen/talkbank-tools/blob/main/README.md) [Source](https://github.com/FranklinChen/talkbank-tools/blob/main/docs/PLATFORM-SUPPORT.md) [Source](https://github.com/FranklinChen/talkbank-tools/blob/main/book/src/batchalign/user-guide/quick-start.md) [Source](https://talkbank.org/)

### Introduction

Batchalign3 uses speech recognition, forced alignment and other learned language operations to produce time-linked CHAT transcripts from audio or enrich existing annotations. [Source 1](https://github.com/FranklinChen/talkbank-tools/blob/main/README.md) [Source 2](https://github.com/FranklinChen/talkbank-tools/blob/main/docs/PLATFORM-SUPPORT.md) [Source 3](https://github.com/FranklinChen/talkbank-tools/blob/main/book/src/batchalign/user-guide/quick-start.md) [Source 4](https://talkbank.org/)

### What it is good for

Draft a transcript and timing track for a short oral-history project, then review each speaker and retain editable annotation data. [Source 1](https://github.com/FranklinChen/talkbank-tools/blob/main/README.md) [Source 2](https://github.com/FranklinChen/talkbank-tools/blob/main/docs/PLATFORM-SUPPORT.md) [Source 3](https://github.com/FranklinChen/talkbank-tools/blob/main/book/src/batchalign/user-guide/quick-start.md) [Source 4](https://talkbank.org/)

### Demo & examples

The maintainer’s guide documents named transcription and alignment commands. It distinguishes the CLI from the experimental desktop dashboard and exposes explicit language choices. [Source 1](https://github.com/FranklinChen/talkbank-tools/blob/main/README.md) [Source 2](https://github.com/FranklinChen/talkbank-tools/blob/main/docs/PLATFORM-SUPPORT.md) [Source 3](https://github.com/FranklinChen/talkbank-tools/blob/main/book/src/batchalign/user-guide/quick-start.md) [Source 4](https://talkbank.org/)

### Install

Follow the documented route for the scoped workflow. The steps below are source references. [Source 1](https://github.com/FranklinChen/talkbank-tools/blob/main/README.md) [Source 2](https://github.com/FranklinChen/talkbank-tools/blob/main/docs/PLATFORM-SUPPORT.md) [Source 3](https://github.com/FranklinChen/talkbank-tools/blob/main/book/src/batchalign/user-guide/quick-start.md) [Source 4](https://talkbank.org/)

1. Choose the published CLI installer path for your OS. The official installation guide uses an isolated uv-managed Python and downloads selected speech/language models.
2. Set up one local language and an authorized test recording. Match model and output to the chosen CHAT workflow.
### First project

A small first project makes the input, model output and handoff easy to inspect. [Source 1](https://github.com/FranklinChen/talkbank-tools/blob/main/README.md) [Source 2](https://github.com/FranklinChen/talkbank-tools/blob/main/docs/PLATFORM-SUPPORT.md) [Source 3](https://github.com/FranklinChen/talkbank-tools/blob/main/book/src/batchalign/user-guide/quick-start.md) [Source 4](https://talkbank.org/)

1. Generate a draft transcript for a single sample and check the rendered language and speaker turn boundaries.
2. Use forced alignment against corrected text and compare attached timecodes with the audio.
3. Retain the CHAT files and source recording metadata for later human editing and publication.
### Hardware & software

Platform and compute constraints refer to the selected route. [Source 1](https://github.com/FranklinChen/talkbank-tools/blob/main/README.md) [Source 2](https://github.com/FranklinChen/talkbank-tools/blob/main/docs/PLATFORM-SUPPORT.md) [Source 3](https://github.com/FranklinChen/talkbank-tools/blob/main/book/src/batchalign/user-guide/quick-start.md) [Source 4](https://talkbank.org/)

- **Hardware:** The project lists 8 GB RAM minimum, 16 GB recommended and several GB for models.
- **Software:** Published Batchalign3 CLI, default uv-managed Python 3.14 and model/media dependencies. Some formats need FFmpeg. The CHAT format tools are a separate project.
- **Platforms:** The supported matrix lists Intel and Apple silicon macOS, Linux x86_64 and aarch64, and Windows x86_64.

### License, model weights & costs

The full software license was reviewed. Dependencies and creative assets carry their own terms. [Source 1](https://github.com/FranklinChen/talkbank-tools/blob/main/LICENSE) [Source 2](https://github.com/FranklinChen/talkbank-tools/blob/main/README.md) [Source 3](https://github.com/FranklinChen/talkbank-tools/blob/main/docs/PLATFORM-SUPPORT.md) [Source 4](https://github.com/FranklinChen/talkbank-tools/blob/main/book/src/batchalign/user-guide/quick-start.md) [Source 5](https://talkbank.org/)

- **Code:** BSD-3-Clause
- **Weights:** The software license is BSD-3-Clause. Speech and alignment weights, any configured cloud route and corpus permissions require independent review.
- **Commercial:** Project code is governed by BSD-3-Clause. Confirm selected model, source-media and output restrictions separately.
- **Cost:** Local models need compute and storage. A separately selected hosted recognizer can have its own access and fees.

### Why it merits attention

The creative workflow is grounded in the cited documentation. Output quality and compatibility are not hands-on verified. [Source 1](https://github.com/FranklinChen/talkbank-tools/blob/main/README.md) [Source 2](https://github.com/FranklinChen/talkbank-tools/blob/main/docs/PLATFORM-SUPPORT.md) [Source 3](https://github.com/FranklinChen/talkbank-tools/blob/main/book/src/batchalign/user-guide/quick-start.md) [Source 4](https://talkbank.org/)

### Limitations

Keep the CLI and language/ASR choice explicit. Proper names, mixed-language passages and overlapping speech can need substantial editing. [Source 1](https://github.com/FranklinChen/talkbank-tools/blob/main/README.md) [Source 2](https://github.com/FranklinChen/talkbank-tools/blob/main/docs/PLATFORM-SUPPORT.md) [Source 3](https://github.com/FranklinChen/talkbank-tools/blob/main/book/src/batchalign/user-guide/quick-start.md) [Source 4](https://talkbank.org/)

### Get the tool

- [Repository](https://github.com/FranklinChen/talkbank-tools)
- [Documentation](https://talkbank.org/)

## Local Image

Photography, restoration & color · Images & design · VFX, compositing & relighting

This completes an earlier pending guide with a current source review.

### Quality assessment: Experimental

Creative use and the code grant are documented. Check-level gaps remain before a recommendation.

Scope: Create an editable draft portrait composite by combining a subject mask, nondestructive RAW settings and a locally retained layered document.

Evidence checked: 2026-11-21. No local execution implied.

Why Experimental: The maintainer describes 0.8.0 as the first public alpha of a rebuilt app and explicitly documents that older catalogs do not migrate. https://github.com/zdbosoxfan/local-image/blob/main/README.md

- **Open-source software license · verified:** Reviewed the complete project software grant and its redistribution conditions. Model, data and service terms are scoped separately. [Source](https://github.com/zdbosoxfan/local-image/blob/main/LICENSE)
- **Creative results · documented:** The maintainer describes distinct Library, Develop, Photo and Vector workspaces and model setup by function. Library data from the prior series is incompatible with the rebuilt alpha. [Source](https://github.com/zdbosoxfan/local-image/blob/main/README.md) [Source](https://github.com/zdbosoxfan/local-image/blob/main/CHANGELOG.md) [Source](https://github.com/zdbosoxfan/local-image/blob/main/PRIVACY.md)
- **Reproducible setup · documented:** The installation and first-use steps are in the cited documentation. Reproduction of this workflow remains unverified. [Source](https://github.com/zdbosoxfan/local-image/blob/main/README.md) [Source](https://github.com/zdbosoxfan/local-image/blob/main/CHANGELOG.md) [Source](https://github.com/zdbosoxfan/local-image/blob/main/PRIVACY.md)
- **Maintenance and support · documented:** The release and changelog document this first alpha and changes to the data model. [Source](https://github.com/zdbosoxfan/local-image/releases/tag/v0.8.0-alpha)
- **Independent use · unknown:** Independent first-hand use of the exact workflow was not established in this source review.
- **Models, services and costs · documented:** The project software is GPL-3.0. Its source describes separate terms for models and optional inference services. RAW image and reference media rights remain separate. On-device work uses local compute and storage. Remote GPU or optional service usage adds separate hosting or access costs. [Source](https://github.com/zdbosoxfan/local-image/blob/main/README.md) [Source](https://github.com/zdbosoxfan/local-image/blob/main/CHANGELOG.md) [Source](https://github.com/zdbosoxfan/local-image/blob/main/PRIVACY.md)

Source and documentation review. No hands-on execution by AI Media Scout. The rebuilt alpha begins with a new Library. Preserve the earlier catalog and verify all media paths and editable assets before migration.

### How it uses AI

Local Image includes downloaded on-device photo masks and denoisers. Its generation workspace also connects to a selected ComfyUI service for generation and inpainting. [Source](https://github.com/zdbosoxfan/local-image/blob/main/README.md) [Source](https://github.com/zdbosoxfan/local-image/blob/main/CHANGELOG.md) [Source](https://github.com/zdbosoxfan/local-image/blob/main/PRIVACY.md)

### Introduction

Local Image includes downloaded on-device photo masks and denoisers. Its generation workspace also connects to a selected ComfyUI service for generation and inpainting. [Source 1](https://github.com/zdbosoxfan/local-image/blob/main/README.md) [Source 2](https://github.com/zdbosoxfan/local-image/blob/main/CHANGELOG.md) [Source 3](https://github.com/zdbosoxfan/local-image/blob/main/PRIVACY.md)

### What it is good for

Create an editable draft portrait composite by combining a subject mask, nondestructive RAW settings and a locally retained layered document. [Source 1](https://github.com/zdbosoxfan/local-image/blob/main/README.md) [Source 2](https://github.com/zdbosoxfan/local-image/blob/main/CHANGELOG.md) [Source 3](https://github.com/zdbosoxfan/local-image/blob/main/PRIVACY.md)

### Demo & examples

The maintainer describes distinct Library, Develop, Photo and Vector workspaces and model setup by function. Library data from the prior series is incompatible with the rebuilt alpha. [Source 1](https://github.com/zdbosoxfan/local-image/blob/main/README.md) [Source 2](https://github.com/zdbosoxfan/local-image/blob/main/CHANGELOG.md) [Source 3](https://github.com/zdbosoxfan/local-image/blob/main/PRIVACY.md)

### Install

Follow the documented route for the scoped workflow. The steps below are source references. [Source 1](https://github.com/zdbosoxfan/local-image/blob/main/README.md) [Source 2](https://github.com/zdbosoxfan/local-image/blob/main/CHANGELOG.md) [Source 3](https://github.com/zdbosoxfan/local-image/blob/main/PRIVACY.md)

1. Choose the 0.8.0-alpha distribution for the documented host. First use should create a new scratch Library while retaining old projects separately.
2. Select and review the on-device mask model. Configure a compatible ComfyUI server only when using a separate generative workflow.
### First project

A small first project makes the input, model output and handoff easy to inspect. [Source 1](https://github.com/zdbosoxfan/local-image/blob/main/README.md) [Source 2](https://github.com/zdbosoxfan/local-image/blob/main/CHANGELOG.md) [Source 3](https://github.com/zdbosoxfan/local-image/blob/main/PRIVACY.md)

1. Make a neutral RAW development for one test image, then generate a subject mask and inspect hair or edges manually.
2. Add an editable layer and compare the composite to the original development. Keep the original file and reversible styling.
3. Export a proof and verify that saved layers reopen under the same version before moving a larger portfolio.
### Hardware & software

Platform and compute constraints refer to the selected route. [Source 1](https://github.com/zdbosoxfan/local-image/blob/main/README.md) [Source 2](https://github.com/zdbosoxfan/local-image/blob/main/CHANGELOG.md) [Source 3](https://github.com/zdbosoxfan/local-image/blob/main/PRIVACY.md)

- **Hardware:** Minimum RAM, VRAM and disk space for the scoped workflow are undocumented.
- **Software:** Native Local Image alpha, platform graphics support and function-specific downloaded models. ComfyUI is a separate optional server for selected generative operations.
- **Platforms:** Linux x86_64 and Apple silicon macOS 13+ are documented at this release.

### License, model weights & costs

The full software license was reviewed. Dependencies and creative assets carry their own terms. [Source 1](https://github.com/zdbosoxfan/local-image/blob/main/LICENSE) [Source 2](https://github.com/zdbosoxfan/local-image/blob/main/README.md) [Source 3](https://github.com/zdbosoxfan/local-image/blob/main/CHANGELOG.md) [Source 4](https://github.com/zdbosoxfan/local-image/blob/main/PRIVACY.md)

- **Code:** GPL-3.0
- **Weights:** The project software is GPL-3.0. Its source describes separate terms for models and optional inference services. RAW image and reference media rights remain separate.
- **Commercial:** Project code is governed by GPL-3.0. Confirm selected model, source-media and output restrictions separately.
- **Cost:** On-device work uses local compute and storage. Remote GPU or optional service usage adds separate hosting or access costs.

### Why it merits attention

The creative workflow is grounded in the cited documentation. Output quality and compatibility are not hands-on verified. [Source 1](https://github.com/zdbosoxfan/local-image/blob/main/README.md) [Source 2](https://github.com/zdbosoxfan/local-image/blob/main/CHANGELOG.md) [Source 3](https://github.com/zdbosoxfan/local-image/blob/main/PRIVACY.md)

### Limitations

The rebuilt alpha begins with a new Library. Preserve the earlier catalog and verify all media paths and editable assets before migration. [Source 1](https://github.com/zdbosoxfan/local-image/blob/main/README.md) [Source 2](https://github.com/zdbosoxfan/local-image/blob/main/CHANGELOG.md) [Source 3](https://github.com/zdbosoxfan/local-image/blob/main/PRIVACY.md)

### Get the tool

- [Repository](https://github.com/zdbosoxfan/local-image)
- [Documentation](https://github.com/zdbosoxfan/local-image/blob/main/PRIVACY.md)

## CDLNet Rust inference

Learned optics and post-production lens tools · Photography, restoration & color · Images & design

This completes an earlier pending guide with a current source review.

### Quality assessment: Quality unverified

Creative use and the code grant are documented. Check-level gaps remain before a recommendation.

Scope: Compare model-based denoising against a neutral edit of a noisy still and keep the original pixels available for edge and texture review.

Evidence checked: 2026-11-21. No local execution implied.

- **Open-source software license · verified:** Reviewed the complete project software grant and its redistribution conditions. Model, data and service terms are scoped separately. [Source](https://github.com/mkranjac/cdlnet-rs/blob/main/LICENSE)
- **Creative results · documented:** The maintainer posts example images and CLI argument choices. The upstream research explains the method and evaluation of the original model. The result evidence for the Rust port remains narrower. [Source](https://github.com/mkranjac/cdlnet-rs/blob/main/Readme.md) [Source](https://github.com/mkranjac/cdlnet-rs/blob/main/Cargo.toml) [Source](https://github.com/nikopj/CDLNet-OJSP) [Source](https://arxiv.org/abs/2110.14855)
- **Reproducible setup · documented:** The installation and first-use steps are in the cited documentation. Reproduction of this workflow remains unverified. [Source](https://github.com/mkranjac/cdlnet-rs/blob/main/Readme.md) [Source](https://github.com/mkranjac/cdlnet-rs/blob/main/Cargo.toml) [Source](https://github.com/nikopj/CDLNet-OJSP) [Source](https://arxiv.org/abs/2110.14855)
- **Maintenance and support · unknown:** The reviewed sources do not establish workflow-specific support, fixes and unresolved blockers.
- **Independent use · unknown:** Independent first-hand use of the exact workflow was not established in this source review.
- **Models, services and costs · documented:** The port uses MIT. Upstream model weights, assets and data have separate provenance and usage terms. Processing runs on selected local graphics hardware. Weights and image outputs consume storage. [Source](https://github.com/mkranjac/cdlnet-rs/blob/main/Readme.md) [Source](https://github.com/mkranjac/cdlnet-rs/blob/main/Cargo.toml) [Source](https://github.com/nikopj/CDLNet-OJSP) [Source](https://arxiv.org/abs/2110.14855)

Source and documentation review. No hands-on execution by AI Media Scout. Current documentation supports inference and says training is unimplemented. The upstream evaluation does not establish identical accuracy or speed of this implementation.

### How it uses AI

This Rust port runs learned CDLNet denoising and JDD-CDLNet reconstruction through Burn/WGPU using converted weights. [Source](https://github.com/mkranjac/cdlnet-rs/blob/main/Readme.md) [Source](https://github.com/mkranjac/cdlnet-rs/blob/main/Cargo.toml) [Source](https://github.com/nikopj/CDLNet-OJSP) [Source](https://arxiv.org/abs/2110.14855)

### Introduction

This Rust port runs learned CDLNet denoising and JDD-CDLNet reconstruction through Burn/WGPU using converted weights. [Source 1](https://github.com/mkranjac/cdlnet-rs/blob/main/Readme.md) [Source 2](https://github.com/mkranjac/cdlnet-rs/blob/main/Cargo.toml) [Source 3](https://github.com/nikopj/CDLNet-OJSP) [Source 4](https://arxiv.org/abs/2110.14855)

### What it is good for

Compare model-based denoising against a neutral edit of a noisy still and keep the original pixels available for edge and texture review. [Source 1](https://github.com/mkranjac/cdlnet-rs/blob/main/Readme.md) [Source 2](https://github.com/mkranjac/cdlnet-rs/blob/main/Cargo.toml) [Source 3](https://github.com/nikopj/CDLNet-OJSP) [Source 4](https://arxiv.org/abs/2110.14855)

### Demo & examples

The maintainer posts example images and CLI argument choices. The upstream research explains the method and evaluation of the original model. The result evidence for the Rust port remains narrower. [Source 1](https://github.com/mkranjac/cdlnet-rs/blob/main/Readme.md) [Source 2](https://github.com/mkranjac/cdlnet-rs/blob/main/Cargo.toml) [Source 3](https://github.com/nikopj/CDLNet-OJSP) [Source 4](https://arxiv.org/abs/2110.14855)

### Install

Follow the documented route for the scoped workflow. The steps below are source references. [Source 1](https://github.com/mkranjac/cdlnet-rs/blob/main/Readme.md) [Source 2](https://github.com/mkranjac/cdlnet-rs/blob/main/Cargo.toml) [Source 3](https://github.com/nikopj/CDLNet-OJSP) [Source 4](https://arxiv.org/abs/2110.14855)

1. Use the documented Rust build path and a compatible WGPU graphics setup.
2. Obtain the conversion or weights through the official sources and verify the specific asset terms and method before using a personal photograph.
### First project

A small first project makes the input, model output and handoff easy to inspect. [Source 1](https://github.com/mkranjac/cdlnet-rs/blob/main/Readme.md) [Source 2](https://github.com/mkranjac/cdlnet-rs/blob/main/Cargo.toml) [Source 3](https://github.com/nikopj/CDLNet-OJSP) [Source 4](https://arxiv.org/abs/2110.14855)

1. Run the appropriate color or grayscale network on a small test image and preserve the input.
2. Compare noise, fine texture and edge appearance at the same scale. Save a separately named proof.
3. Record the chosen network and input assumptions before using the result in a production edit.
### Hardware & software

Platform and compute constraints refer to the selected route. [Source 1](https://github.com/mkranjac/cdlnet-rs/blob/main/Readme.md) [Source 2](https://github.com/mkranjac/cdlnet-rs/blob/main/Cargo.toml) [Source 3](https://github.com/nikopj/CDLNet-OJSP) [Source 4](https://arxiv.org/abs/2110.14855)

- **Hardware:** Minimum RAM, VRAM and disk space for the scoped workflow are undocumented.
- **Software:** Rust/Cargo and the documented Burn/WGPU runtime, plus compatible safetensors weights. The current project covers inference.
- **Platforms:** WGPU is documented as the backend. Supported OS/driver combinations and device minima are not documented.

### License, model weights & costs

The full software license was reviewed. Dependencies and creative assets carry their own terms. [Source 1](https://github.com/mkranjac/cdlnet-rs/blob/main/LICENSE) [Source 2](https://github.com/mkranjac/cdlnet-rs/blob/main/Readme.md) [Source 3](https://github.com/mkranjac/cdlnet-rs/blob/main/Cargo.toml) [Source 4](https://github.com/nikopj/CDLNet-OJSP) [Source 5](https://arxiv.org/abs/2110.14855)

- **Code:** MIT
- **Weights:** The port uses MIT. Upstream model weights, assets and data have separate provenance and usage terms.
- **Commercial:** Project code is governed by MIT. Confirm selected model, source-media and output restrictions separately.
- **Cost:** Processing runs on selected local graphics hardware. Weights and image outputs consume storage.

### Why it merits attention

The creative workflow is grounded in the cited documentation. Output quality and compatibility are not hands-on verified. [Source 1](https://github.com/mkranjac/cdlnet-rs/blob/main/Readme.md) [Source 2](https://github.com/mkranjac/cdlnet-rs/blob/main/Cargo.toml) [Source 3](https://github.com/nikopj/CDLNet-OJSP) [Source 4](https://arxiv.org/abs/2110.14855)

### Limitations

Current documentation supports inference and says training is unimplemented. The upstream evaluation does not establish identical accuracy or speed of this implementation. [Source 1](https://github.com/mkranjac/cdlnet-rs/blob/main/Readme.md) [Source 2](https://github.com/mkranjac/cdlnet-rs/blob/main/Cargo.toml) [Source 3](https://github.com/nikopj/CDLNet-OJSP) [Source 4](https://arxiv.org/abs/2110.14855)

### Get the tool

- [Repository](https://github.com/mkranjac/cdlnet-rs)
- [Documentation](https://arxiv.org/abs/2110.14855)

## YN Translation Workshop

AI game localization and playable translations · Creative publishing & presentation · AI poetry, kinetic literature and language installations

This completes an earlier pending guide with a current source review.

### Quality assessment: Quality unverified

Creative use and the code grant are documented. Check-level gaps remain before a recommendation.

Scope: Localize a rights-cleared chapter or game dialogue file and review the original and translation side by side with saved character-language decisions.

Evidence checked: 2026-11-21. No local execution implied.

- **Open-source software license · verified:** Reviewed the complete project software grant and its redistribution conditions. Model, data and service terms are scoped separately. [Source](https://github.com/TohmaN233/YN-translation-workshop/blob/main/LICENSE)
- **Creative results · documented:** The maintainer’s examples demonstrate authoring and localization projects. The source describes protected tokens, line checks and selective retranslation. A human language review remains important. [Source](https://github.com/TohmaN233/YN-translation-workshop/blob/main/README.md) [Source](https://github.com/TohmaN233/YN-translation-workshop/blob/main/README.en.md) [Source](https://github.com/TohmaN233/YN-translation-workshop/blob/main/docs/features.md) [Source](https://tohman233.github.io/YN-translation-workshop/)
- **Reproducible setup · documented:** The installation and first-use steps are in the cited documentation. Reproduction of this workflow remains unverified. [Source](https://github.com/TohmaN233/YN-translation-workshop/blob/main/README.md) [Source](https://github.com/TohmaN233/YN-translation-workshop/blob/main/README.en.md) [Source](https://github.com/TohmaN233/YN-translation-workshop/blob/main/docs/features.md) [Source](https://tohman233.github.io/YN-translation-workshop/)
- **Maintenance and support · unknown:** The reviewed sources do not establish workflow-specific support, fixes and unresolved blockers.
- **Independent use · unknown:** Independent first-hand use of the exact workflow was not established in this source review.
- **Models, services and costs · documented:** MIT applies to project code. Content sent to a model uses provider terms. Source game and novel materials require authorization for reuse. Manual editing is local. AI translation, auditing and retries consume selected provider quota or capacity. [Source](https://github.com/TohmaN233/YN-translation-workshop/blob/main/README.md) [Source](https://github.com/TohmaN233/YN-translation-workshop/blob/main/README.en.md) [Source](https://github.com/TohmaN233/YN-translation-workshop/blob/main/docs/features.md) [Source](https://tohman233.github.io/YN-translation-workshop/)

Source and documentation review. No hands-on execution by AI Media Scout. Scanned PDFs without a readable text layer are outside the documented ingestion route. Proofread protected variables, layout and culturally specific dialogue.

### How it uses AI

The workshop uses a chosen language model to draft and review long-form translation, while checking line structure, terminology and protected game variables or control markers. [Source](https://github.com/TohmaN233/YN-translation-workshop/blob/main/README.md) [Source](https://github.com/TohmaN233/YN-translation-workshop/blob/main/README.en.md) [Source](https://github.com/TohmaN233/YN-translation-workshop/blob/main/docs/features.md) [Source](https://tohman233.github.io/YN-translation-workshop/)

### Introduction

The workshop uses a chosen language model to draft and review long-form translation, while checking line structure, terminology and protected game variables or control markers. [Source 1](https://github.com/TohmaN233/YN-translation-workshop/blob/main/README.md) [Source 2](https://github.com/TohmaN233/YN-translation-workshop/blob/main/README.en.md) [Source 3](https://github.com/TohmaN233/YN-translation-workshop/blob/main/docs/features.md) [Source 4](https://tohman233.github.io/YN-translation-workshop/)

### What it is good for

Localize a rights-cleared chapter or game dialogue file and review the original and translation side by side with saved character-language decisions. [Source 1](https://github.com/TohmaN233/YN-translation-workshop/blob/main/README.md) [Source 2](https://github.com/TohmaN233/YN-translation-workshop/blob/main/README.en.md) [Source 3](https://github.com/TohmaN233/YN-translation-workshop/blob/main/docs/features.md) [Source 4](https://tohman233.github.io/YN-translation-workshop/)

### Demo & examples

The maintainer’s examples demonstrate authoring and localization projects. The source describes protected tokens, line checks and selective retranslation. A human language review remains important. [Source 1](https://github.com/TohmaN233/YN-translation-workshop/blob/main/README.md) [Source 2](https://github.com/TohmaN233/YN-translation-workshop/blob/main/README.en.md) [Source 3](https://github.com/TohmaN233/YN-translation-workshop/blob/main/docs/features.md) [Source 4](https://tohman233.github.io/YN-translation-workshop/)

### Install

Follow the documented route for the scoped workflow. The steps below are source references. [Source 1](https://github.com/TohmaN233/YN-translation-workshop/blob/main/README.md) [Source 2](https://github.com/TohmaN233/YN-translation-workshop/blob/main/README.en.md) [Source 3](https://github.com/TohmaN233/YN-translation-workshop/blob/main/docs/features.md) [Source 4](https://tohman233.github.io/YN-translation-workshop/)

1. Choose the current x64 Windows setup or portable package and review its published checksum.
2. Create a test project and configure the authorized provider and language direction. Use the manual workflow when media should stay local.
### First project

A small first project makes the input, model output and handoff easy to inspect. [Source 1](https://github.com/TohmaN233/YN-translation-workshop/blob/main/README.md) [Source 2](https://github.com/TohmaN233/YN-translation-workshop/blob/main/README.en.md) [Source 3](https://github.com/TohmaN233/YN-translation-workshop/blob/main/docs/features.md) [Source 4](https://tohman233.github.io/YN-translation-workshop/)

1. Import a small editable-text file and define glossary, character names and protected control placeholders.
2. Generate a first translation and inspect flagged lines. Verify line correspondence and preservation against the original.
3. Correct language and style side by side, then export a clean handoff with terminology notes and input provenance.
### Hardware & software

Platform and compute constraints refer to the selected route. [Source 1](https://github.com/TohmaN233/YN-translation-workshop/blob/main/README.md) [Source 2](https://github.com/TohmaN233/YN-translation-workshop/blob/main/README.en.md) [Source 3](https://github.com/TohmaN233/YN-translation-workshop/blob/main/docs/features.md) [Source 4](https://tohman233.github.io/YN-translation-workshop/)

- **Hardware:** Minimum RAM, VRAM and disk space for the scoped workflow are undocumented.
- **Software:** Published Windows build is self-contained. Model-enabled routes need a chosen configured provider. Text-layer PDF, EPUB and TXT are documented inputs.
- **Platforms:** The current packaged installer is for Windows x64.

### License, model weights & costs

The full software license was reviewed. Dependencies and creative assets carry their own terms. [Source 1](https://github.com/TohmaN233/YN-translation-workshop/blob/main/LICENSE) [Source 2](https://github.com/TohmaN233/YN-translation-workshop/blob/main/README.md) [Source 3](https://github.com/TohmaN233/YN-translation-workshop/blob/main/README.en.md) [Source 4](https://github.com/TohmaN233/YN-translation-workshop/blob/main/docs/features.md) [Source 5](https://tohman233.github.io/YN-translation-workshop/)

- **Code:** MIT
- **Weights:** MIT applies to project code. Content sent to a model uses provider terms. Source game and novel materials require authorization for reuse.
- **Commercial:** Project code is governed by MIT. Confirm selected model, source-media and output restrictions separately.
- **Cost:** Manual editing is local. AI translation, auditing and retries consume selected provider quota or capacity.

### Why it merits attention

The creative workflow is grounded in the cited documentation. Output quality and compatibility are not hands-on verified. [Source 1](https://github.com/TohmaN233/YN-translation-workshop/blob/main/README.md) [Source 2](https://github.com/TohmaN233/YN-translation-workshop/blob/main/README.en.md) [Source 3](https://github.com/TohmaN233/YN-translation-workshop/blob/main/docs/features.md) [Source 4](https://tohman233.github.io/YN-translation-workshop/)

### Limitations

Scanned PDFs without a readable text layer are outside the documented ingestion route. Proofread protected variables, layout and culturally specific dialogue. [Source 1](https://github.com/TohmaN233/YN-translation-workshop/blob/main/README.md) [Source 2](https://github.com/TohmaN233/YN-translation-workshop/blob/main/README.en.md) [Source 3](https://github.com/TohmaN233/YN-translation-workshop/blob/main/docs/features.md) [Source 4](https://tohman233.github.io/YN-translation-workshop/)

### Get the tool

- [Repository](https://github.com/TohmaN233/YN-translation-workshop)
- [Documentation](https://tohman233.github.io/YN-translation-workshop/)

## SpriteBrew

AI-agent pixel art, sprites and palette-controlled animation · Games & production pipelines · Avatars, digital humans & lip sync

This completes an earlier pending guide with a current source review.

### Quality assessment: Quality unverified

Creative use and the code grant are documented. Check-level gaps remain before a recommendation.

Scope: Develop a rights-cleared character sprite, verify consistent frame alignment and export selected transparent PNGs or a sheet for a game scene.

Evidence checked: 2026-11-21. No local execution implied.

- **Open-source software license · verified:** Reviewed the complete project software grant and its redistribution conditions. Model, data and service terms are scoped separately. [Source](https://github.com/GAlbanese09/spritebrew/blob/main/LICENSE)
- **Creative results · documented:** The author documents per-style examples and animation features. Performance, consistency and asset terms are dependent on the selected model and workflow. [Source](https://github.com/GAlbanese09/spritebrew/blob/main/README.md) [Source](https://spritebrew.com/) [Source](https://github.com/GAlbanese09/spritebrew/blob/main/package.json)
- **Reproducible setup · documented:** The installation and first-use steps are in the cited documentation. Reproduction of this workflow remains unverified. [Source](https://github.com/GAlbanese09/spritebrew/blob/main/README.md) [Source](https://spritebrew.com/) [Source](https://github.com/GAlbanese09/spritebrew/blob/main/package.json)
- **Maintenance and support · unknown:** The reviewed sources do not establish workflow-specific support, fixes and unresolved blockers.
- **Independent use · unknown:** Independent first-hand use of the exact workflow was not established in this source review.
- **Models, services and costs · documented:** The software uses AGPL-3.0. Retro Diffusion, account, design references and resulting art retain separate terms. Hosted features use generation tokens. Deploying the documented infrastructure and calling the provider can incur separate costs. [Source](https://github.com/GAlbanese09/spritebrew/blob/main/README.md) [Source](https://spritebrew.com/) [Source](https://github.com/GAlbanese09/spritebrew/blob/main/package.json)

Source and documentation review. No hands-on execution by AI Media Scout. Inspect a generated game sprite for palette control, pixel spacing and frame wobble before integrating. Hosted conditions can differ from self-hosting.

### How it uses AI

SpriteBrew connects model-backed pixel-art image generation, background choices and animation workflows to editable sprite sheet operations such as slicing and export. [Source](https://github.com/GAlbanese09/spritebrew/blob/main/README.md) [Source](https://spritebrew.com/) [Source](https://github.com/GAlbanese09/spritebrew/blob/main/package.json)

### Introduction

SpriteBrew connects model-backed pixel-art image generation, background choices and animation workflows to editable sprite sheet operations such as slicing and export. [Source 1](https://github.com/GAlbanese09/spritebrew/blob/main/README.md) [Source 2](https://spritebrew.com/) [Source 3](https://github.com/GAlbanese09/spritebrew/blob/main/package.json)

### What it is good for

Develop a rights-cleared character sprite, verify consistent frame alignment and export selected transparent PNGs or a sheet for a game scene. [Source 1](https://github.com/GAlbanese09/spritebrew/blob/main/README.md) [Source 2](https://spritebrew.com/) [Source 3](https://github.com/GAlbanese09/spritebrew/blob/main/package.json)

### Demo & examples

The author documents per-style examples and animation features. Performance, consistency and asset terms are dependent on the selected model and workflow. [Source 1](https://github.com/GAlbanese09/spritebrew/blob/main/README.md) [Source 2](https://spritebrew.com/) [Source 3](https://github.com/GAlbanese09/spritebrew/blob/main/package.json)

### Install

Follow the documented route for the scoped workflow. The steps below are source references. [Source 1](https://github.com/GAlbanese09/spritebrew/blob/main/README.md) [Source 2](https://spritebrew.com/) [Source 3](https://github.com/GAlbanese09/spritebrew/blob/main/package.json)

1. Use the project’s hosted route or review its complete self-host deployment. Model-backed features require an account and provider configuration.
2. Check the chosen pixel art style, sprite dimensions and account’s usage allowance before generation.
### First project

A small first project makes the input, model output and handoff easy to inspect. [Source 1](https://github.com/GAlbanese09/spritebrew/blob/main/README.md) [Source 2](https://spritebrew.com/) [Source 3](https://github.com/GAlbanese09/spritebrew/blob/main/package.json)

1. Generate or upload an owned character reference. Inspect transparency and silhouette against a true pixel grid.
2. Check the motion frames and slice a specific sheet. Review physical scale and anchors across loops.
3. Export selected sprite files and retain the prompt, model and your original art reference.
### Hardware & software

Platform and compute constraints refer to the selected route. [Source 1](https://github.com/GAlbanese09/spritebrew/blob/main/README.md) [Source 2](https://spritebrew.com/) [Source 3](https://github.com/GAlbanese09/spritebrew/blob/main/package.json)

- **Hardware:** Minimum RAM, VRAM and disk space for the scoped workflow are undocumented.
- **Software:** Web client with Next.js, image workflow and deployment configuration. AI tasks depend on Retro Diffusion. Self-host setup also documents Clerk and Cloudflare services.
- **Platforms:** Browser-based host is documented. Platform-specific app builds are undocumented.

### License, model weights & costs

The full software license was reviewed. Dependencies and creative assets carry their own terms. [Source 1](https://github.com/GAlbanese09/spritebrew/blob/main/LICENSE) [Source 2](https://github.com/GAlbanese09/spritebrew/blob/main/README.md) [Source 3](https://spritebrew.com/) [Source 4](https://github.com/GAlbanese09/spritebrew/blob/main/package.json)

- **Code:** AGPL-3.0
- **Weights:** The software uses AGPL-3.0. Retro Diffusion, account, design references and resulting art retain separate terms.
- **Commercial:** Project code is governed by AGPL-3.0. Confirm selected model, source-media and output restrictions separately.
- **Cost:** Hosted features use generation tokens. Deploying the documented infrastructure and calling the provider can incur separate costs.

### Why it merits attention

The creative workflow is grounded in the cited documentation. Output quality and compatibility are not hands-on verified. [Source 1](https://github.com/GAlbanese09/spritebrew/blob/main/README.md) [Source 2](https://spritebrew.com/) [Source 3](https://github.com/GAlbanese09/spritebrew/blob/main/package.json)

### Limitations

Inspect a generated game sprite for palette control, pixel spacing and frame wobble before integrating. Hosted conditions can differ from self-hosting. [Source 1](https://github.com/GAlbanese09/spritebrew/blob/main/README.md) [Source 2](https://spritebrew.com/) [Source 3](https://github.com/GAlbanese09/spritebrew/blob/main/package.json)

### Get the tool

- [Repository](https://github.com/GAlbanese09/spritebrew)
- [Documentation](https://github.com/GAlbanese09/spritebrew/blob/main/package.json)

## StemStudio

AI seamless loops, sample design and DAW-ready stems · AI music notation and score recovery · Audio, music & voice

This completes an earlier pending guide with a current source review.

### Quality assessment: Quality unverified

Creative use and the code grant are documented. Check-level gaps remain before a recommendation.

Scope: Prepare a personal rehearsal loop from an authorized recording, audition a stem in the mix and inspect a draft score or lyric timing against the source.

Evidence checked: 2026-11-21. No local execution implied.

- **Open-source software license · verified:** Reviewed the complete project software grant and its redistribution conditions. Model, data and service terms are scoped separately. [Source](https://github.com/RobertAgterhuis/StemStudio/blob/main/LICENSE)
- **Creative results · documented:** The maintainer documents per-stem controls, model selection and a GPU run. Piano transcription limits and model-specific restrictions are disclosed in the source. [Source](https://github.com/RobertAgterhuis/StemStudio/blob/main/README.md) [Source](https://github.com/RobertAgterhuis/StemStudio/blob/main/docs/THIRD-PARTY-LICENSES.md) [Source](https://github.com/RobertAgterhuis/StemStudio/blob/main/docker-compose.yml)
- **Reproducible setup · documented:** The installation and first-use steps are in the cited documentation. Reproduction of this workflow remains unverified. [Source](https://github.com/RobertAgterhuis/StemStudio/blob/main/README.md) [Source](https://github.com/RobertAgterhuis/StemStudio/blob/main/docs/THIRD-PARTY-LICENSES.md) [Source](https://github.com/RobertAgterhuis/StemStudio/blob/main/docker-compose.yml)
- **Maintenance and support · unknown:** The reviewed sources do not establish workflow-specific support, fixes and unresolved blockers.
- **Independent use · unknown:** Independent first-hand use of the exact workflow was not established in this source review.
- **Models, services and costs · documented:** MIT governs the project’s own source. Third-party notices distinguish separately licensed components. Some pretrained stem weights are unclear or restricted to personal noncommercial use, even when their inference code is open. Local compute and model storage are required. Optional paid providers and exact model terms are separate. [Source](https://github.com/RobertAgterhuis/StemStudio/blob/main/README.md) [Source](https://github.com/RobertAgterhuis/StemStudio/blob/main/docs/THIRD-PARTY-LICENSES.md) [Source](https://github.com/RobertAgterhuis/StemStudio/blob/main/docker-compose.yml)

Source and documentation review. No hands-on execution by AI Media Scout. Use the reviewed separation weights only within their documented scope. Separation can retain material from other instruments and draft piano transcription can omit rhythmic detail.

### How it uses AI

StemStudio separates common stems with Demucs and supplies an editable rehearsal mixer. It also documents separately installed models for draft note and lyric extraction. [Source](https://github.com/RobertAgterhuis/StemStudio/blob/main/README.md) [Source](https://github.com/RobertAgterhuis/StemStudio/blob/main/docs/THIRD-PARTY-LICENSES.md) [Source](https://github.com/RobertAgterhuis/StemStudio/blob/main/docker-compose.yml)

### Introduction

StemStudio separates common stems with Demucs and supplies an editable rehearsal mixer. It also documents separately installed models for draft note and lyric extraction. [Source 1](https://github.com/RobertAgterhuis/StemStudio/blob/main/README.md) [Source 2](https://github.com/RobertAgterhuis/StemStudio/blob/main/docs/THIRD-PARTY-LICENSES.md) [Source 3](https://github.com/RobertAgterhuis/StemStudio/blob/main/docker-compose.yml)

### What it is good for

Prepare a personal rehearsal loop from an authorized recording, audition a stem in the mix and inspect a draft score or lyric timing against the source. [Source 1](https://github.com/RobertAgterhuis/StemStudio/blob/main/README.md) [Source 2](https://github.com/RobertAgterhuis/StemStudio/blob/main/docs/THIRD-PARTY-LICENSES.md) [Source 3](https://github.com/RobertAgterhuis/StemStudio/blob/main/docker-compose.yml)

### Demo & examples

The maintainer documents per-stem controls, model selection and a GPU run. Piano transcription limits and model-specific restrictions are disclosed in the source. [Source 1](https://github.com/RobertAgterhuis/StemStudio/blob/main/README.md) [Source 2](https://github.com/RobertAgterhuis/StemStudio/blob/main/docs/THIRD-PARTY-LICENSES.md) [Source 3](https://github.com/RobertAgterhuis/StemStudio/blob/main/docker-compose.yml)

### Install

Follow the documented route for the scoped workflow. The steps below are source references. [Source 1](https://github.com/RobertAgterhuis/StemStudio/blob/main/README.md) [Source 2](https://github.com/RobertAgterhuis/StemStudio/blob/main/docs/THIRD-PARTY-LICENSES.md) [Source 3](https://github.com/RobertAgterhuis/StemStudio/blob/main/docker-compose.yml)

1. Use the documented Docker Compose v2 setup. Start with an authorized small recording and choose the model only after reviewing the complete third-party notices.
2. If using the optional GPU container, verify the exact host support and intended model before substituting it for the basic path.
### First project

A small first project makes the input, model output and handoff easy to inspect. [Source 1](https://github.com/RobertAgterhuis/StemStudio/blob/main/README.md) [Source 2](https://github.com/RobertAgterhuis/StemStudio/blob/main/docs/THIRD-PARTY-LICENSES.md) [Source 3](https://github.com/RobertAgterhuis/StemStudio/blob/main/docker-compose.yml)

1. Load one rights-cleared excerpt. Separate the documented four or six stems for personal practice and check for cross-talk.
2. Loop a difficult passage and compare the isolated part with the original mix. Correct any draft note or lyric transcription independently.
3. Keep a local rehearsal copy and the input recording reference. Review any different model or deployment separately.
### Hardware & software

Platform and compute constraints refer to the selected route. [Source 1](https://github.com/RobertAgterhuis/StemStudio/blob/main/README.md) [Source 2](https://github.com/RobertAgterhuis/StemStudio/blob/main/docs/THIRD-PARTY-LICENSES.md) [Source 3](https://github.com/RobertAgterhuis/StemStudio/blob/main/docker-compose.yml)

- **Hardware:** Minimum RAM, VRAM and disk space for the scoped workflow are undocumented.
- **Software:** Docker Compose v2, the selected model and local model storage. Some modes use NVIDIA GPU or optional outside provider access. They have separate setup.
- **Platforms:** Docker deployment documented. The maintainer reports Windows 11 with Docker Desktop/WSL2 for a named GPU configuration. Other device/driver combinations need verification.

### License, model weights & costs

The full software license was reviewed. Dependencies and creative assets carry their own terms. [Source 1](https://github.com/RobertAgterhuis/StemStudio/blob/main/LICENSE) [Source 2](https://github.com/RobertAgterhuis/StemStudio/blob/main/README.md) [Source 3](https://github.com/RobertAgterhuis/StemStudio/blob/main/docs/THIRD-PARTY-LICENSES.md) [Source 4](https://github.com/RobertAgterhuis/StemStudio/blob/main/docker-compose.yml)

- **Code:** MIT
- **Weights:** MIT governs the project’s own source. Third-party notices distinguish separately licensed components. Some pretrained stem weights are unclear or restricted to personal noncommercial use, even when their inference code is open.
- **Commercial:** Project code is governed by MIT. Confirm selected model, source-media and output restrictions separately.
- **Cost:** Local compute and model storage are required. Optional paid providers and exact model terms are separate.

### Why it merits attention

The creative workflow is grounded in the cited documentation. Output quality and compatibility are not hands-on verified. [Source 1](https://github.com/RobertAgterhuis/StemStudio/blob/main/README.md) [Source 2](https://github.com/RobertAgterhuis/StemStudio/blob/main/docs/THIRD-PARTY-LICENSES.md) [Source 3](https://github.com/RobertAgterhuis/StemStudio/blob/main/docker-compose.yml)

### Limitations

Use the reviewed separation weights only within their documented scope. Separation can retain material from other instruments and draft piano transcription can omit rhythmic detail. [Source 1](https://github.com/RobertAgterhuis/StemStudio/blob/main/README.md) [Source 2](https://github.com/RobertAgterhuis/StemStudio/blob/main/docs/THIRD-PARTY-LICENSES.md) [Source 3](https://github.com/RobertAgterhuis/StemStudio/blob/main/docker-compose.yml)

### Get the tool

- [Repository](https://github.com/RobertAgterhuis/StemStudio)
- [Documentation](https://github.com/RobertAgterhuis/StemStudio/blob/main/docker-compose.yml)

## Split Audio API

Audio, music & voice · Neural acoustics and responsive sound spaces · AI seamless loops, sample design and DAW-ready stems

First complete guide in the library. The publication and documentation dates are not necessarily the project’s launch date.

### Quality assessment: Quality unverified

Creative use and the code grant are documented. Check-level gaps remain before a recommendation.

Scope: Integrate a local stem extraction step into a sound edit or rehearsal-file pipeline while keeping raw and derived audio distinct.

Evidence checked: 2026-11-21. No local execution implied.

- **Open-source software license · verified:** Reviewed the complete project software grant and its redistribution conditions. Model, data and service terms are scoped separately. [Source](https://github.com/JozRamirez10/Split-Audio/blob/main/LICENSE)
- **Creative results · documented:** The maintainer describes distinct local inference and remote guitar routes and documents API setup. Independent audio evaluation is pending. [Source](https://github.com/JozRamirez10/Split-Audio/blob/main/README.md) [Source](https://github.com/JozRamirez10/Split-Audio/blob/main/requirements.txt) [Source](https://github.com/JozRamirez10/Split-Audio/blob/main/docker-compose.yml)
- **Reproducible setup · documented:** The installation and first-use steps are in the cited documentation. Reproduction of this workflow remains unverified. [Source](https://github.com/JozRamirez10/Split-Audio/blob/main/README.md) [Source](https://github.com/JozRamirez10/Split-Audio/blob/main/requirements.txt) [Source](https://github.com/JozRamirez10/Split-Audio/blob/main/docker-compose.yml)
- **Maintenance and support · unknown:** The reviewed sources do not establish workflow-specific support, fixes and unresolved blockers.
- **Independent use · unknown:** Independent first-hand use of the exact workflow was not established in this source review.
- **Models, services and costs · documented:** MIT applies to the worker code. Selected weights, source recording permissions and optional Music.ai cloud terms are separate. Local execution uses compute and model storage. Music.ai is a separate external access and billing path. [Source](https://github.com/JozRamirez10/Split-Audio/blob/main/README.md) [Source](https://github.com/JozRamirez10/Split-Audio/blob/main/requirements.txt) [Source](https://github.com/JozRamirez10/Split-Audio/blob/main/docker-compose.yml)

Source and documentation review. No hands-on execution by AI Media Scout. Choose the correct local endpoint to keep media on the workstation. Separation quality and model term scope vary.

### How it uses AI

The Split Audio worker uses local PyTorch and ONNX processing for vocal and instrument separation. Optional guitar-role tasks use the separately governed Music.ai service. [Source](https://github.com/JozRamirez10/Split-Audio/blob/main/README.md) [Source](https://github.com/JozRamirez10/Split-Audio/blob/main/requirements.txt) [Source](https://github.com/JozRamirez10/Split-Audio/blob/main/docker-compose.yml)

### Introduction

The Split Audio worker uses local PyTorch and ONNX processing for vocal and instrument separation. Optional guitar-role tasks use the separately governed Music.ai service. [Source 1](https://github.com/JozRamirez10/Split-Audio/blob/main/README.md) [Source 2](https://github.com/JozRamirez10/Split-Audio/blob/main/requirements.txt) [Source 3](https://github.com/JozRamirez10/Split-Audio/blob/main/docker-compose.yml)

### What it is good for

Integrate a local stem extraction step into a sound edit or rehearsal-file pipeline while keeping raw and derived audio distinct. [Source 1](https://github.com/JozRamirez10/Split-Audio/blob/main/README.md) [Source 2](https://github.com/JozRamirez10/Split-Audio/blob/main/requirements.txt) [Source 3](https://github.com/JozRamirez10/Split-Audio/blob/main/docker-compose.yml)

### Demo & examples

The maintainer describes distinct local inference and remote guitar routes and documents API setup. Independent audio evaluation is pending. [Source 1](https://github.com/JozRamirez10/Split-Audio/blob/main/README.md) [Source 2](https://github.com/JozRamirez10/Split-Audio/blob/main/requirements.txt) [Source 3](https://github.com/JozRamirez10/Split-Audio/blob/main/docker-compose.yml)

### Install

Follow the documented route for the scoped workflow. The steps below are source references. [Source 1](https://github.com/JozRamirez10/Split-Audio/blob/main/README.md) [Source 2](https://github.com/JozRamirez10/Split-Audio/blob/main/requirements.txt) [Source 3](https://github.com/JozRamirez10/Split-Audio/blob/main/docker-compose.yml)

1. Choose the documented Docker image setup or Python 3.10+ and the system audio libraries. Prepare the local model folder and exact selected weights.
2. Choose CPU or GPU dependencies as documented. Configure optional cloud access only if the specific remote separation route is required.
### First project

A small first project makes the input, model output and handoff easy to inspect. [Source 1](https://github.com/JozRamirez10/Split-Audio/blob/main/README.md) [Source 2](https://github.com/JozRamirez10/Split-Audio/blob/main/requirements.txt) [Source 3](https://github.com/JozRamirez10/Split-Audio/blob/main/docker-compose.yml)

1. Submit one rights-cleared test recording to a local separation route.
2. Compare vocals or drums with the original mix and listen for bleed at the transition between phrases.
3. Keep the recorded inputs, returned stems and model identifiers. Audition the combined result before using it in a session.
### Hardware & software

Platform and compute constraints refer to the selected route. [Source 1](https://github.com/JozRamirez10/Split-Audio/blob/main/README.md) [Source 2](https://github.com/JozRamirez10/Split-Audio/blob/main/requirements.txt) [Source 3](https://github.com/JozRamirez10/Split-Audio/blob/main/docker-compose.yml)

- **Hardware:** Minimum RAM, VRAM and disk space for the scoped workflow are undocumented.
- **Software:** Python 3.10+, FastAPI, PyTorch or ONNX and FFmpeg/libsndfile for local source deployment. Docker deployment is documented. Cloud guitar endpoints need Music.ai access.
- **Platforms:** Documented container and bare-metal service routes. Validate OS, accelerator and codec availability for the intended deployment.

### License, model weights & costs

The full software license was reviewed. Dependencies and creative assets carry their own terms. [Source 1](https://github.com/JozRamirez10/Split-Audio/blob/main/LICENSE) [Source 2](https://github.com/JozRamirez10/Split-Audio/blob/main/README.md) [Source 3](https://github.com/JozRamirez10/Split-Audio/blob/main/requirements.txt) [Source 4](https://github.com/JozRamirez10/Split-Audio/blob/main/docker-compose.yml)

- **Code:** MIT
- **Weights:** MIT applies to the worker code. Selected weights, source recording permissions and optional Music.ai cloud terms are separate.
- **Commercial:** Project code is governed by MIT. Confirm selected model, source-media and output restrictions separately.
- **Cost:** Local execution uses compute and model storage. Music.ai is a separate external access and billing path.

### Why it merits attention

The creative workflow is grounded in the cited documentation. Output quality and compatibility are not hands-on verified. [Source 1](https://github.com/JozRamirez10/Split-Audio/blob/main/README.md) [Source 2](https://github.com/JozRamirez10/Split-Audio/blob/main/requirements.txt) [Source 3](https://github.com/JozRamirez10/Split-Audio/blob/main/docker-compose.yml)

### Limitations

Choose the correct local endpoint to keep media on the workstation. Separation quality and model term scope vary. [Source 1](https://github.com/JozRamirez10/Split-Audio/blob/main/README.md) [Source 2](https://github.com/JozRamirez10/Split-Audio/blob/main/requirements.txt) [Source 3](https://github.com/JozRamirez10/Split-Audio/blob/main/docker-compose.yml)

### Get the tool

- [Repository](https://github.com/JozRamirez10/Split-Audio)
- [Documentation](https://github.com/JozRamirez10/Split-Audio/blob/main/docker-compose.yml)

## HoloGen

3D, reconstruction & assets · Photogrammetry, scanning & neural rendering · Spatial audio & volumetric media

The source repository was created on 2026-11-18. This is its first complete guide in the library.

### Quality assessment: Quality unverified

Creative use and the code grant are documented. Check-level gaps remain before a recommendation.

Scope: Build a draft object mesh from photo references, inspect uncertain surfaces and export a geometry file for later 3D cleanup.

Evidence checked: 2026-11-21. No local execution implied.

- **Open-source software license · verified:** Reviewed the complete project software grant and its redistribution conditions. Model, data and service terms are scoped separately. [Source](https://github.com/suvinsanil/HoloGen/blob/main/LICENSE)
- **Creative results · documented:** The developer describes a Three.js viewer with alternate display modes and multiple geometry exports. Quantitative capture accuracy and topology quality remain open. [Source](https://github.com/suvinsanil/HoloGen/blob/main/README.md) [Source](https://github.com/suvinsanil/HoloGen/blob/main/requirements.txt)
- **Reproducible setup · documented:** The installation and first-use steps are in the cited documentation. Reproduction of this workflow remains unverified. [Source](https://github.com/suvinsanil/HoloGen/blob/main/README.md) [Source](https://github.com/suvinsanil/HoloGen/blob/main/requirements.txt)
- **Maintenance and support · unknown:** The reviewed sources do not establish workflow-specific support, fixes and unresolved blockers.
- **Independent use · unknown:** Independent first-hand use of the exact workflow was not established in this source review.
- **Models, services and costs · documented:** The application code is MIT. Depth Anything V2 checkpoints have variant-specific terms, and selected runtimes, datasets and inputs must be checked independently. Local CPU or GPU compute and model/geometry storage are required. No hosted account is documented for the local route. [Source](https://github.com/suvinsanil/HoloGen/blob/main/README.md) [Source](https://github.com/suvinsanil/HoloGen/blob/main/requirements.txt)

Source and documentation review. No hands-on execution by AI Media Scout. Single-view reconstruction cannot observe hidden surfaces. Multi-view coverage and calibration affect the mesh. The project does not document printing readiness.

### How it uses AI

HoloGen combines Depth Anything V2 monocular depth with point and surface reconstruction. Its multi-view route uses pose recovery and TSDF fusion. [Source](https://github.com/suvinsanil/HoloGen/blob/main/README.md) [Source](https://github.com/suvinsanil/HoloGen/blob/main/requirements.txt)

### Introduction

HoloGen combines Depth Anything V2 monocular depth with point and surface reconstruction. Its multi-view route uses pose recovery and TSDF fusion. [Source 1](https://github.com/suvinsanil/HoloGen/blob/main/README.md) [Source 2](https://github.com/suvinsanil/HoloGen/blob/main/requirements.txt)

### What it is good for

Build a draft object mesh from photo references, inspect uncertain surfaces and export a geometry file for later 3D cleanup. [Source 1](https://github.com/suvinsanil/HoloGen/blob/main/README.md) [Source 2](https://github.com/suvinsanil/HoloGen/blob/main/requirements.txt)

### Demo & examples

The developer describes a Three.js viewer with alternate display modes and multiple geometry exports. Quantitative capture accuracy and topology quality remain open. [Source 1](https://github.com/suvinsanil/HoloGen/blob/main/README.md) [Source 2](https://github.com/suvinsanil/HoloGen/blob/main/requirements.txt)

### Install

Follow the documented route for the scoped workflow. The steps below are source references. [Source 1](https://github.com/suvinsanil/HoloGen/blob/main/README.md) [Source 2](https://github.com/suvinsanil/HoloGen/blob/main/requirements.txt)

1. Use the documented Python 3.10+ backend and Node 18+ frontend or the container configuration. Select the supported model and precision path.
2. Review memory and acceleration for the chosen model. Start with a small image set using the documented local CPU route or a supported NVIDIA environment.
### First project

A small first project makes the input, model output and handoff easy to inspect. [Source 1](https://github.com/suvinsanil/HoloGen/blob/main/README.md) [Source 2](https://github.com/suvinsanil/HoloGen/blob/main/requirements.txt)

1. Run single-view reconstruction on one rights-cleared image. Inspect silhouette and implied scale from side views.
2. For a test object, compare overlapping multi-view photographs and inspect the differences in holes and boundary geometry.
3. Save GLB or OBJ with the original capture assumptions. Repair normals and geometry in the downstream editor as needed.
### Hardware & software

Platform and compute constraints refer to the selected route. [Source 1](https://github.com/suvinsanil/HoloGen/blob/main/README.md) [Source 2](https://github.com/suvinsanil/HoloGen/blob/main/requirements.txt)

- **Hardware:** Minimum RAM, VRAM and disk space for the scoped workflow are undocumented.
- **Software:** Python 3.10+, Node 18+, selected Depth Anything V2 artifacts, Open3D and pycolmap for multi-view setup. CUDA is optional.
- **Platforms:** The project documents source setup including Windows environment activation and local Web frontend. Other device combinations require separate reproduction.

### License, model weights & costs

The full software license was reviewed. Dependencies and creative assets carry their own terms. [Source 1](https://github.com/suvinsanil/HoloGen/blob/main/LICENSE) [Source 2](https://github.com/suvinsanil/HoloGen/blob/main/README.md) [Source 3](https://github.com/suvinsanil/HoloGen/blob/main/requirements.txt)

- **Code:** MIT
- **Weights:** The application code is MIT. Depth Anything V2 checkpoints have variant-specific terms, and selected runtimes, datasets and inputs must be checked independently.
- **Commercial:** Project code is governed by MIT. Confirm selected model, source-media and output restrictions separately.
- **Cost:** Local CPU or GPU compute and model/geometry storage are required. No hosted account is documented for the local route.

### Why it merits attention

The creative workflow is grounded in the cited documentation. Output quality and compatibility are not hands-on verified. [Source 1](https://github.com/suvinsanil/HoloGen/blob/main/README.md) [Source 2](https://github.com/suvinsanil/HoloGen/blob/main/requirements.txt)

### Limitations

Single-view reconstruction cannot observe hidden surfaces. Multi-view coverage and calibration affect the mesh. The project does not document printing readiness. [Source 1](https://github.com/suvinsanil/HoloGen/blob/main/README.md) [Source 2](https://github.com/suvinsanil/HoloGen/blob/main/requirements.txt)

### Get the tool

- [Repository](https://github.com/suvinsanil/HoloGen)
- [Documentation](https://github.com/suvinsanil/HoloGen/blob/main/requirements.txt)

## Kinevyn

Video, animation & film · AI kinetic typography and animated lettering · Editing, captions & post-production

The source repository was created on 2026-11-21. This is its first complete guide in the library.

### Quality assessment: Quality unverified

Creative use and the code grant are documented. Check-level gaps remain before a recommendation.

Scope: Build a style reference from footage you own, draft a short original motion-graphics sequence with reusable assets and keep an editable project.

Evidence checked: 2026-11-21. No local execution implied.

- **Open-source software license · verified:** Reviewed the complete project software grant and its redistribution conditions. Model, data and service terms are scoped separately. [Source](https://github.com/minhhoit/kinevyn/blob/main/LICENSE)
- **Creative results · documented:** The source describes project templates, a Studio preview and separate generator routes. The provider wall documents integrations and their differing availability. [Source](https://github.com/minhhoit/kinevyn/blob/main/README.md) [Source](https://github.com/minhhoit/kinevyn/blob/main/docs/usage.md) [Source](https://github.com/minhhoit/kinevyn/blob/main/docs/npm-installation.md)
- **Reproducible setup · documented:** The installation and first-use steps are in the cited documentation. Reproduction of this workflow remains unverified. [Source](https://github.com/minhhoit/kinevyn/blob/main/README.md) [Source](https://github.com/minhhoit/kinevyn/blob/main/docs/usage.md) [Source](https://github.com/minhhoit/kinevyn/blob/main/docs/npm-installation.md)
- **Maintenance and support · unknown:** The reviewed sources do not establish workflow-specific support, fixes and unresolved blockers.
- **Independent use · unknown:** Independent first-hand use of the exact workflow was not established in this source review.
- **Models, services and costs · documented:** The tool source carries Apache-2.0. Template assets and reference media are separate. The selected provider terms govern model access and generated output. Local rendering uses compute. Optional model-backed asset generation is subject to provider credit or billing. [Source](https://github.com/minhhoit/kinevyn/blob/main/README.md) [Source](https://github.com/minhhoit/kinevyn/blob/main/docs/usage.md) [Source](https://github.com/minhhoit/kinevyn/blob/main/docs/npm-installation.md)

Source and documentation review. No hands-on execution by AI Media Scout. Check local agent and Studio versions against their source docs. Reference-matching examples do not establish layout fidelity or rights to reuse someone else’s asset.

### How it uses AI

Kinevyn exposes a local editable motion-video project and asset workflow to agents. It can use a reference to draft editable composition elements, then preview, revise and render the result. [Source](https://github.com/minhhoit/kinevyn/blob/main/README.md) [Source](https://github.com/minhhoit/kinevyn/blob/main/docs/usage.md) [Source](https://github.com/minhhoit/kinevyn/blob/main/docs/npm-installation.md)

### Introduction

Kinevyn exposes a local editable motion-video project and asset workflow to agents. It can use a reference to draft editable composition elements, then preview, revise and render the result. [Source 1](https://github.com/minhhoit/kinevyn/blob/main/README.md) [Source 2](https://github.com/minhhoit/kinevyn/blob/main/docs/usage.md) [Source 3](https://github.com/minhhoit/kinevyn/blob/main/docs/npm-installation.md)

### What it is good for

Build a style reference from footage you own, draft a short original motion-graphics sequence with reusable assets and keep an editable project. [Source 1](https://github.com/minhhoit/kinevyn/blob/main/README.md) [Source 2](https://github.com/minhhoit/kinevyn/blob/main/docs/usage.md) [Source 3](https://github.com/minhhoit/kinevyn/blob/main/docs/npm-installation.md)

### Demo & examples

The source describes project templates, a Studio preview and separate generator routes. The provider wall documents integrations and their differing availability. [Source 1](https://github.com/minhhoit/kinevyn/blob/main/README.md) [Source 2](https://github.com/minhhoit/kinevyn/blob/main/docs/usage.md) [Source 3](https://github.com/minhhoit/kinevyn/blob/main/docs/npm-installation.md)

### Install

Follow the documented route for the scoped workflow. The steps below are source references. [Source 1](https://github.com/minhhoit/kinevyn/blob/main/README.md) [Source 2](https://github.com/minhhoit/kinevyn/blob/main/docs/usage.md) [Source 3](https://github.com/minhhoit/kinevyn/blob/main/docs/npm-installation.md)

1. Use the documented local project setup or maintained npm package. The current source instructions list Node.js 26.11.1, npm, Chromium and FFmpeg/FFprobe.
2. Open the local Studio URL reported by the application. Connect one compatible agent if desired and confirm the selected output tools.
### First project

A small first project makes the input, model output and handoff easy to inspect. [Source 1](https://github.com/minhhoit/kinevyn/blob/main/README.md) [Source 2](https://github.com/minhhoit/kinevyn/blob/main/docs/usage.md) [Source 3](https://github.com/minhhoit/kinevyn/blob/main/docs/npm-installation.md)

1. Start with an original rights-cleared reference and a short brief. Create an editable scene with the appropriate assets and output aspect ratio.
2. Preview the render and inspect title placement, timing and asset provenance. Revise a single scene before expanding it.
3. Save the editable project and export a proof for an independent layout or caption pass.
### Hardware & software

Platform and compute constraints refer to the selected route. [Source 1](https://github.com/minhhoit/kinevyn/blob/main/README.md) [Source 2](https://github.com/minhhoit/kinevyn/blob/main/docs/usage.md) [Source 3](https://github.com/minhhoit/kinevyn/blob/main/docs/npm-installation.md)

- **Hardware:** Minimum RAM, VRAM and disk space for the scoped workflow are undocumented.
- **Software:** Git, npm and the documented source version of Node. Chrome/Chromium and FFmpeg/FFprobe for preview and export. Model providers and optional hosted routes require their own setup.
- **Platforms:** The local Web Studio and source setup are documented. Verify Chromium, encoder and agent support on the intended host.

### License, model weights & costs

The full software license was reviewed. Dependencies and creative assets carry their own terms. [Source 1](https://github.com/minhhoit/kinevyn/blob/main/LICENSE) [Source 2](https://github.com/minhhoit/kinevyn/blob/main/README.md) [Source 3](https://github.com/minhhoit/kinevyn/blob/main/docs/usage.md) [Source 4](https://github.com/minhhoit/kinevyn/blob/main/docs/npm-installation.md)

- **Code:** Apache-2.0
- **Weights:** The tool source carries Apache-2.0. Template assets and reference media are separate. The selected provider terms govern model access and generated output.
- **Commercial:** Project code is governed by Apache-2.0. Confirm selected model, source-media and output restrictions separately.
- **Cost:** Local rendering uses compute. Optional model-backed asset generation is subject to provider credit or billing.

### Why it merits attention

The creative workflow is grounded in the cited documentation. Output quality and compatibility are not hands-on verified. [Source 1](https://github.com/minhhoit/kinevyn/blob/main/README.md) [Source 2](https://github.com/minhhoit/kinevyn/blob/main/docs/usage.md) [Source 3](https://github.com/minhhoit/kinevyn/blob/main/docs/npm-installation.md)

### Limitations

Check local agent and Studio versions against their source docs. Reference-matching examples do not establish layout fidelity or rights to reuse someone else’s asset. [Source 1](https://github.com/minhhoit/kinevyn/blob/main/README.md) [Source 2](https://github.com/minhhoit/kinevyn/blob/main/docs/usage.md) [Source 3](https://github.com/minhhoit/kinevyn/blob/main/docs/npm-installation.md)

### Get the tool

- [Repository](https://github.com/minhhoit/kinevyn)
- [Documentation](https://github.com/minhhoit/kinevyn/blob/main/docs/npm-installation.md)

## VoiceType

Live production accessibility and routed captions · Editing, captions & post-production · Accessible media & assistive creation

This completes an earlier pending guide with a current source review.

### Quality assessment: Quality unverified

Creative use and the code grant are documented. Check-level gaps remain before a recommendation.

Scope: Make a first caption draft for a recorded presentation, then edit timing and speaker-specific vocabulary in the intended caption editor.

Evidence checked: 2026-11-21. No local execution implied.

- **Open-source software license · verified:** Reviewed the complete project software grant and its redistribution conditions. Model, data and service terms are scoped separately. [Source](https://github.com/quick-open/voice-type/blob/main/LICENSE)
- **Creative results · documented:** The author shows local transcription and timestamped export through the desktop app and CLI. Review how the language model handles quiet speech and specialist terms. [Source](https://github.com/quick-open/voice-type/blob/main/README.md) [Source](https://alphacephei.com/vosk/models) [Source](https://github.com/quick-open/voice-type/blob/main/requirements.txt)
- **Reproducible setup · documented:** The installation and first-use steps are in the cited documentation. Reproduction of this workflow remains unverified. [Source](https://github.com/quick-open/voice-type/blob/main/README.md) [Source](https://alphacephei.com/vosk/models) [Source](https://github.com/quick-open/voice-type/blob/main/requirements.txt)
- **Maintenance and support · unknown:** The reviewed sources do not establish workflow-specific support, fixes and unresolved blockers.
- **Independent use · unknown:** Independent first-hand use of the exact workflow was not established in this source review.
- **Models, services and costs · documented:** VoiceType and Vosk code use Apache-2.0. Vosk language model terms vary by exact download. The right to transcribe a source recording is separate. Offline inference uses device compute. Model downloads and output storage are separate resources. [Source](https://github.com/quick-open/voice-type/blob/main/README.md) [Source](https://alphacephei.com/vosk/models) [Source](https://github.com/quick-open/voice-type/blob/main/requirements.txt)

Source and documentation review. No hands-on execution by AI Media Scout. Model selection strongly affects accuracy and memory use. Vosk output needs timing and transcript review.

### How it uses AI

VoiceType uses locally downloaded Vosk speech-recognition models to convert recorded audio to text and timecodes. The project documents SRT, WebVTT and text exports. [Source](https://github.com/quick-open/voice-type/blob/main/README.md) [Source](https://alphacephei.com/vosk/models) [Source](https://github.com/quick-open/voice-type/blob/main/requirements.txt)

### Introduction

VoiceType uses locally downloaded Vosk speech-recognition models to convert recorded audio to text and timecodes. The project documents SRT, WebVTT and text exports. [Source 1](https://github.com/quick-open/voice-type/blob/main/README.md) [Source 2](https://alphacephei.com/vosk/models) [Source 3](https://github.com/quick-open/voice-type/blob/main/requirements.txt)

### What it is good for

Make a first caption draft for a recorded presentation, then edit timing and speaker-specific vocabulary in the intended caption editor. [Source 1](https://github.com/quick-open/voice-type/blob/main/README.md) [Source 2](https://alphacephei.com/vosk/models) [Source 3](https://github.com/quick-open/voice-type/blob/main/requirements.txt)

### Demo & examples

The author shows local transcription and timestamped export through the desktop app and CLI. Review how the language model handles quiet speech and specialist terms. [Source 1](https://github.com/quick-open/voice-type/blob/main/README.md) [Source 2](https://alphacephei.com/vosk/models) [Source 3](https://github.com/quick-open/voice-type/blob/main/requirements.txt)

### Install

Follow the documented route for the scoped workflow. The steps below are source references. [Source 1](https://github.com/quick-open/voice-type/blob/main/README.md) [Source 2](https://alphacephei.com/vosk/models) [Source 3](https://github.com/quick-open/voice-type/blob/main/requirements.txt)

1. Use the Windows package listed by the project or follow its Python dependencies and source launch directions.
2. Download one Vosk model for the spoken language using the model manager. Keep the model’s terms and version with the project.
### First project

A small first project makes the input, model output and handoff easy to inspect. [Source 1](https://github.com/quick-open/voice-type/blob/main/README.md) [Source 2](https://alphacephei.com/vosk/models) [Source 3](https://github.com/quick-open/voice-type/blob/main/requirements.txt)

1. Start with a short WAV or FLAC from a recording you can use. Match the language and review the transcript.
2. Export SRT for an editing timeline or WebVTT for a web player. Compare start/end times with the source audio.
3. Correct names, line length and missing speech before delivery. Retain the editable subtitle file.
### Hardware & software

Platform and compute constraints refer to the selected route. [Source 1](https://github.com/quick-open/voice-type/blob/main/README.md) [Source 2](https://alphacephei.com/vosk/models) [Source 3](https://github.com/quick-open/voice-type/blob/main/requirements.txt)

- **Hardware:** Minimum RAM, VRAM and disk space for the scoped workflow are undocumented.
- **Software:** Desktop installer or the documented Python/Tkinter source route plus a Vosk model.
- **Platforms:** Windows installer documented. The source instructions describe model paths on other hosts. Independently verified macOS and Linux packages were not established.

### License, model weights & costs

The full software license was reviewed. Dependencies and creative assets carry their own terms. [Source 1](https://github.com/quick-open/voice-type/blob/main/LICENSE) [Source 2](https://github.com/quick-open/voice-type/blob/main/README.md) [Source 3](https://alphacephei.com/vosk/models) [Source 4](https://github.com/quick-open/voice-type/blob/main/requirements.txt)

- **Code:** Apache-2.0
- **Weights:** VoiceType and Vosk code use Apache-2.0. Vosk language model terms vary by exact download. The right to transcribe a source recording is separate.
- **Commercial:** Project code is governed by Apache-2.0. Confirm selected model, source-media and output restrictions separately.
- **Cost:** Offline inference uses device compute. Model downloads and output storage are separate resources.

### Why it merits attention

The creative workflow is grounded in the cited documentation. Output quality and compatibility are not hands-on verified. [Source 1](https://github.com/quick-open/voice-type/blob/main/README.md) [Source 2](https://alphacephei.com/vosk/models) [Source 3](https://github.com/quick-open/voice-type/blob/main/requirements.txt)

### Limitations

Model selection strongly affects accuracy and memory use. Vosk output needs timing and transcript review. [Source 1](https://github.com/quick-open/voice-type/blob/main/README.md) [Source 2](https://alphacephei.com/vosk/models) [Source 3](https://github.com/quick-open/voice-type/blob/main/requirements.txt)

### Get the tool

- [Repository](https://github.com/quick-open/voice-type)
- [Documentation](https://github.com/quick-open/voice-type/blob/main/requirements.txt)

## Arabic Subtitle Maker

AI visual dubbing and translated performance · Editing, captions & post-production · Accessible media & assistive creation

This completes an earlier pending guide with a current source review.

### Quality assessment: Quality unverified

Creative use and the code grant are documented. Check-level gaps remain before a recommendation.

Scope: Generate an editable Arabic SRT from a rights-cleared interview and compare it against the spoken language before making an optional subtitled master.

Evidence checked: 2026-11-21. No local execution implied.

- **Open-source software license · verified:** Reviewed the complete project software grant and its redistribution conditions. Model, data and service terms are scoped separately. [Source](https://github.com/drcde/arabic-subtitle-maker/blob/main/LICENSE)
- **Creative results · documented:** The author documents separate SRT, burned MP4 and dual output. Correct shaping and reading order in the burned output depend on the selected FFmpeg build. [Source](https://github.com/drcde/arabic-subtitle-maker/blob/main/README.md) [Source](https://github.com/drcde/arabic-subtitle-maker/blob/main/requirements.txt) [Source](https://ai.google.dev/gemini-api/docs/pricing)
- **Reproducible setup · documented:** The installation and first-use steps are in the cited documentation. Reproduction of this workflow remains unverified. [Source](https://github.com/drcde/arabic-subtitle-maker/blob/main/README.md) [Source](https://github.com/drcde/arabic-subtitle-maker/blob/main/requirements.txt) [Source](https://ai.google.dev/gemini-api/docs/pricing)
- **Maintenance and support · unknown:** The reviewed sources do not establish workflow-specific support, fixes and unresolved blockers.
- **Independent use · unknown:** Independent first-hand use of the exact workflow was not established in this source review.
- **Models, services and costs · documented:** MIT governs this app. The chosen Whisper weights and translation service retain their own terms. Gemini receives transcript text. Local transcription requires compute and model storage. Translator access, quotas and per-model pricing are separate. [Source](https://github.com/drcde/arabic-subtitle-maker/blob/main/README.md) [Source](https://github.com/drcde/arabic-subtitle-maker/blob/main/requirements.txt) [Source](https://ai.google.dev/gemini-api/docs/pricing)

Source and documentation review. No hands-on execution by AI Media Scout. Verify the current Gemini model ID and Arabic line wrap/timing. SRT review needs someone familiar with the subject and target language.

### How it uses AI

Arabic Subtitle Maker transcribes video with faster-whisper and uses a configured Gemini endpoint to translate transcript segments into Modern Standard Arabic. [Source](https://github.com/drcde/arabic-subtitle-maker/blob/main/README.md) [Source](https://github.com/drcde/arabic-subtitle-maker/blob/main/requirements.txt) [Source](https://ai.google.dev/gemini-api/docs/pricing)

### Introduction

Arabic Subtitle Maker transcribes video with faster-whisper and uses a configured Gemini endpoint to translate transcript segments into Modern Standard Arabic. [Source 1](https://github.com/drcde/arabic-subtitle-maker/blob/main/README.md) [Source 2](https://github.com/drcde/arabic-subtitle-maker/blob/main/requirements.txt) [Source 3](https://ai.google.dev/gemini-api/docs/pricing)

### What it is good for

Generate an editable Arabic SRT from a rights-cleared interview and compare it against the spoken language before making an optional subtitled master. [Source 1](https://github.com/drcde/arabic-subtitle-maker/blob/main/README.md) [Source 2](https://github.com/drcde/arabic-subtitle-maker/blob/main/requirements.txt) [Source 3](https://ai.google.dev/gemini-api/docs/pricing)

### Demo & examples

The author documents separate SRT, burned MP4 and dual output. Correct shaping and reading order in the burned output depend on the selected FFmpeg build. [Source 1](https://github.com/drcde/arabic-subtitle-maker/blob/main/README.md) [Source 2](https://github.com/drcde/arabic-subtitle-maker/blob/main/requirements.txt) [Source 3](https://ai.google.dev/gemini-api/docs/pricing)

### Install

Follow the documented route for the scoped workflow. The steps below are source references. [Source 1](https://github.com/drcde/arabic-subtitle-maker/blob/main/README.md) [Source 2](https://github.com/drcde/arabic-subtitle-maker/blob/main/requirements.txt) [Source 3](https://ai.google.dev/gemini-api/docs/pricing)

1. Create the documented Python 3.10–3.12 environment. Use the listed dependencies and a supported Gemini API configuration.
2. For a burned output, also prepare FFmpeg with the Arabic text shaping requirements described by the project.
### First project

A small first project makes the input, model output and handoff easy to inspect. [Source 1](https://github.com/drcde/arabic-subtitle-maker/blob/main/README.md) [Source 2](https://github.com/drcde/arabic-subtitle-maker/blob/main/requirements.txt) [Source 3](https://ai.google.dev/gemini-api/docs/pricing)

1. Choose a locally held rights-cleared test clip. Review the settings and the implications of sending transcript text to Gemini.
2. Keep the generated SRT editable. Review proper nouns, timing and speaker context with an Arabic speaker.
3. Compare subtitle appearance in the destination player. If needed, render a separate MP4 with captions in the image.
### Hardware & software

Platform and compute constraints refer to the selected route. [Source 1](https://github.com/drcde/arabic-subtitle-maker/blob/main/README.md) [Source 2](https://github.com/drcde/arabic-subtitle-maker/blob/main/requirements.txt) [Source 3](https://ai.google.dev/gemini-api/docs/pricing)

- **Hardware:** The first model download can occupy several gigabytes depending on selection. Stable RAM and VRAM minima for the documented workflow are unspecified.
- **Software:** Python 3.10–3.12, project dependencies, faster-whisper model and Gemini API access. FFmpeg is required for the burned-video option.
- **Platforms:** The documentation includes Windows and Debian/Ubuntu setup. macOS validation is undocumented.

### License, model weights & costs

The full software license was reviewed. Dependencies and creative assets carry their own terms. [Source 1](https://github.com/drcde/arabic-subtitle-maker/blob/main/LICENSE) [Source 2](https://github.com/drcde/arabic-subtitle-maker/blob/main/README.md) [Source 3](https://github.com/drcde/arabic-subtitle-maker/blob/main/requirements.txt) [Source 4](https://ai.google.dev/gemini-api/docs/pricing)

- **Code:** MIT
- **Weights:** MIT governs this app. The chosen Whisper weights and translation service retain their own terms. Gemini receives transcript text.
- **Commercial:** Project code is governed by MIT. Confirm selected model, source-media and output restrictions separately.
- **Cost:** Local transcription requires compute and model storage. Translator access, quotas and per-model pricing are separate.

### Why it merits attention

The creative workflow is grounded in the cited documentation. Output quality and compatibility are not hands-on verified. [Source 1](https://github.com/drcde/arabic-subtitle-maker/blob/main/README.md) [Source 2](https://github.com/drcde/arabic-subtitle-maker/blob/main/requirements.txt) [Source 3](https://ai.google.dev/gemini-api/docs/pricing)

### Limitations

Verify the current Gemini model ID and Arabic line wrap/timing. SRT review needs someone familiar with the subject and target language. [Source 1](https://github.com/drcde/arabic-subtitle-maker/blob/main/README.md) [Source 2](https://github.com/drcde/arabic-subtitle-maker/blob/main/requirements.txt) [Source 3](https://ai.google.dev/gemini-api/docs/pricing)

### Get the tool

- [Repository](https://github.com/drcde/arabic-subtitle-maker)
- [Documentation](https://ai.google.dev/gemini-api/docs/pricing)

## XINTU

AI color direction and palette-based media · Photography, restoration & color · Images & design

This completes an earlier pending guide with a current source review.

### Quality assessment: Quality unverified

Creative use and the code grant are documented. Check-level gaps remain before a recommendation.

Scope: Explore several grading directions for a photo series while keeping control over exposure, color and the final image export.

Evidence checked: 2026-11-21. No local execution implied.

- **Open-source software license · verified:** Reviewed the complete project software grant and its redistribution conditions. Model, data and service terms are scoped separately. [Source](https://github.com/AirZhou1zz/XINTU/blob/main/LICENSE)
- **Creative results · documented:** The developer archives three Qwen cases with input context and selected grading parameters. Its local deterministic demo is a separate way to inspect controls without making a live model request. [Source](https://github.com/AirZhou1zz/XINTU/blob/main/README.md) [Source](https://github.com/AirZhou1zz/XINTU/blob/main/public/portfolio/showcase/qwen-cases.json) [Source](https://github.com/AirZhou1zz/XINTU/blob/main/docs/PROJECT_STATE.md)
- **Reproducible setup · documented:** The installation and first-use steps are in the cited documentation. Reproduction of this workflow remains unverified. [Source](https://github.com/AirZhou1zz/XINTU/blob/main/README.md) [Source](https://github.com/AirZhou1zz/XINTU/blob/main/public/portfolio/showcase/qwen-cases.json) [Source](https://github.com/AirZhou1zz/XINTU/blob/main/docs/PROJECT_STATE.md)
- **Maintenance and support · unknown:** The reviewed sources do not establish workflow-specific support, fixes and unresolved blockers.
- **Independent use · unknown:** Independent first-hand use of the exact workflow was not established in this source review.
- **Models, services and costs · documented:** The project code is MIT. The live vision/model endpoint has independent terms. Use images whose upload, grading and reuse are authorized. Canvas rendering and project mock mode run locally. A live model request consumes provider quota or may incur a charge. [Source](https://github.com/AirZhou1zz/XINTU/blob/main/README.md) [Source](https://github.com/AirZhou1zz/XINTU/blob/main/public/portfolio/showcase/qwen-cases.json) [Source](https://github.com/AirZhou1zz/XINTU/blob/main/docs/PROJECT_STATE.md)

Source and documentation review. No hands-on execution by AI Media Scout. Current examples are creator runs. Color metrics are approximate and the grading path needs calibration across more subjects and lighting.

### How it uses AI

XINTU lets a vision model propose bounded color-grading operations for a reference and target photo. Browser Canvas renders parameter-based grades and compares them with lightweight metrics. [Source](https://github.com/AirZhou1zz/XINTU/blob/main/README.md) [Source](https://github.com/AirZhou1zz/XINTU/blob/main/public/portfolio/showcase/qwen-cases.json) [Source](https://github.com/AirZhou1zz/XINTU/blob/main/docs/PROJECT_STATE.md)

### Introduction

XINTU lets a vision model propose bounded color-grading operations for a reference and target photo. Browser Canvas renders parameter-based grades and compares them with lightweight metrics. [Source 1](https://github.com/AirZhou1zz/XINTU/blob/main/README.md) [Source 2](https://github.com/AirZhou1zz/XINTU/blob/main/public/portfolio/showcase/qwen-cases.json) [Source 3](https://github.com/AirZhou1zz/XINTU/blob/main/docs/PROJECT_STATE.md)

### What it is good for

Explore several grading directions for a photo series while keeping control over exposure, color and the final image export. [Source 1](https://github.com/AirZhou1zz/XINTU/blob/main/README.md) [Source 2](https://github.com/AirZhou1zz/XINTU/blob/main/public/portfolio/showcase/qwen-cases.json) [Source 3](https://github.com/AirZhou1zz/XINTU/blob/main/docs/PROJECT_STATE.md)

### Demo & examples

The developer archives three Qwen cases with input context and selected grading parameters. Its local deterministic demo is a separate way to inspect controls without making a live model request. [Source 1](https://github.com/AirZhou1zz/XINTU/blob/main/README.md) [Source 2](https://github.com/AirZhou1zz/XINTU/blob/main/public/portfolio/showcase/qwen-cases.json) [Source 3](https://github.com/AirZhou1zz/XINTU/blob/main/docs/PROJECT_STATE.md)

### Install

Follow the documented route for the scoped workflow. The steps below are source references. [Source 1](https://github.com/AirZhou1zz/XINTU/blob/main/README.md) [Source 2](https://github.com/AirZhou1zz/XINTU/blob/main/public/portfolio/showcase/qwen-cases.json) [Source 3](https://github.com/AirZhou1zz/XINTU/blob/main/docs/PROJECT_STATE.md)

1. Use the project’s Node.js 20.9+ instructions to launch a local Web app.
2. For the live model path, configure the vision-compatible endpoint server-side. Review its media handling and ensure both images are cleared for the provider.
### First project

A small first project makes the input, model output and handoff easy to inspect. [Source 1](https://github.com/AirZhou1zz/XINTU/blob/main/README.md) [Source 2](https://github.com/AirZhou1zz/XINTU/blob/main/public/portfolio/showcase/qwen-cases.json) [Source 3](https://github.com/AirZhou1zz/XINTU/blob/main/docs/PROJECT_STATE.md)

1. Choose one reference and one test photo. Specify the mood and whether preservation of skin tones or highlight detail matters.
2. Compare candidate grades against both images. Inspect clipping and important colors before manual refinement.
3. Export the selected PNG and retain the original image and parameter choice. Check consistency before using the grade for a series.
### Hardware & software

Platform and compute constraints refer to the selected route. [Source 1](https://github.com/AirZhou1zz/XINTU/blob/main/README.md) [Source 2](https://github.com/AirZhou1zz/XINTU/blob/main/public/portfolio/showcase/qwen-cases.json) [Source 3](https://github.com/AirZhou1zz/XINTU/blob/main/docs/PROJECT_STATE.md)

- **Hardware:** Minimum RAM, VRAM and disk space for the scoped workflow are undocumented.
- **Software:** Node.js 20.9+ and the project’s browser app. The live path requires compatible image-input and structured-response support.
- **Platforms:** A local Web app setup and public demo are documented. Hardware and browser-specific minimum versions for image-size handling are undocumented.

### License, model weights & costs

The full software license was reviewed. Dependencies and creative assets carry their own terms. [Source 1](https://github.com/AirZhou1zz/XINTU/blob/main/LICENSE) [Source 2](https://github.com/AirZhou1zz/XINTU/blob/main/README.md) [Source 3](https://github.com/AirZhou1zz/XINTU/blob/main/public/portfolio/showcase/qwen-cases.json) [Source 4](https://github.com/AirZhou1zz/XINTU/blob/main/docs/PROJECT_STATE.md)

- **Code:** MIT
- **Weights:** The project code is MIT. The live vision/model endpoint has independent terms. Use images whose upload, grading and reuse are authorized.
- **Commercial:** Project code is governed by MIT. Confirm selected model, source-media and output restrictions separately.
- **Cost:** Canvas rendering and project mock mode run locally. A live model request consumes provider quota or may incur a charge.

### Why it merits attention

The creative workflow is grounded in the cited documentation. Output quality and compatibility are not hands-on verified. [Source 1](https://github.com/AirZhou1zz/XINTU/blob/main/README.md) [Source 2](https://github.com/AirZhou1zz/XINTU/blob/main/public/portfolio/showcase/qwen-cases.json) [Source 3](https://github.com/AirZhou1zz/XINTU/blob/main/docs/PROJECT_STATE.md)

### Limitations

Current examples are creator runs. Color metrics are approximate and the grading path needs calibration across more subjects and lighting. [Source 1](https://github.com/AirZhou1zz/XINTU/blob/main/README.md) [Source 2](https://github.com/AirZhou1zz/XINTU/blob/main/public/portfolio/showcase/qwen-cases.json) [Source 3](https://github.com/AirZhou1zz/XINTU/blob/main/docs/PROJECT_STATE.md)

### Get the tool

- [Repository](https://github.com/AirZhou1zz/XINTU)
- [Documentation](https://github.com/AirZhou1zz/XINTU/blob/main/docs/PROJECT_STATE.md)

## AIICUT

Video, animation & film · Editing, captions & post-production · Browser tools & web media

The source repository was created on 2026-10-22. This is its first complete guide in the library.

### Quality assessment: Experimental

Creative use and the code grant are documented. Check-level gaps remain before a recommendation.

Scope: Review an early integrated generation path for reference short shots, then assemble and caption local clips in a browser edit.

Evidence checked: 2026-11-21. No local execution implied.

Why Experimental: The current project status identifies its AI generation feature as unverified with real requests and unavailable in its public deployment. https://github.com/jcsdn/aiicut/blob/main/README.md

- **Open-source software license · verified:** Reviewed the complete project software grant and its redistribution conditions. Model, data and service terms are scoped separately. [Source](https://github.com/jcsdn/aiicut/blob/main/LICENSE)
- **Creative results · documented:** The author documents local timeline cuts, SRT and on-canvas output. The author says real Seedance generation was not verified and the public feature is unavailable. [Source](https://github.com/jcsdn/aiicut/blob/main/README.md) [Source](https://github.com/jcsdn/aiicut/blob/main/DEPLOYMENT.md)
- **Reproducible setup · documented:** The installation and first-use steps are in the cited documentation. Reproduction of this workflow remains unverified. [Source](https://github.com/jcsdn/aiicut/blob/main/README.md) [Source](https://github.com/jcsdn/aiicut/blob/main/DEPLOYMENT.md)
- **Maintenance and support · unknown:** The reviewed sources do not establish workflow-specific support, fixes and unresolved blockers.
- **Independent use · unknown:** Independent first-hand use of the exact workflow was not established in this source review.
- **Models, services and costs · documented:** The project source is MIT. Generated media uses the separately governed commercial model API and chosen input rights. Local edit uses device compute. Cloud generation requires separately configured provider access and pricing. [Source](https://github.com/jcsdn/aiicut/blob/main/README.md) [Source](https://github.com/jcsdn/aiicut/blob/main/DEPLOYMENT.md)

Source and documentation review. No hands-on execution by AI Media Scout. Native generation is unverified in the project’s own current status. Local source file and export resolution limits are documented.

### How it uses AI

AIICUT includes a Seedance text-to-video and image-to-video request path alongside a browser-based local video timeline. The project documents task polling and media import. [Source](https://github.com/jcsdn/aiicut/blob/main/README.md) [Source](https://github.com/jcsdn/aiicut/blob/main/DEPLOYMENT.md)

### Introduction

AIICUT includes a Seedance text-to-video and image-to-video request path alongside a browser-based local video timeline. The project documents task polling and media import. [Source 1](https://github.com/jcsdn/aiicut/blob/main/README.md) [Source 2](https://github.com/jcsdn/aiicut/blob/main/DEPLOYMENT.md)

### What it is good for

Review an early integrated generation path for reference short shots, then assemble and caption local clips in a browser edit. [Source 1](https://github.com/jcsdn/aiicut/blob/main/README.md) [Source 2](https://github.com/jcsdn/aiicut/blob/main/DEPLOYMENT.md)

### Demo & examples

The author documents local timeline cuts, SRT and on-canvas output. The author says real Seedance generation was not verified and the public feature is unavailable. [Source 1](https://github.com/jcsdn/aiicut/blob/main/README.md) [Source 2](https://github.com/jcsdn/aiicut/blob/main/DEPLOYMENT.md)

### Install

Follow the documented route for the scoped workflow. The steps below are source references. [Source 1](https://github.com/jcsdn/aiicut/blob/main/README.md) [Source 2](https://github.com/jcsdn/aiicut/blob/main/DEPLOYMENT.md)

1. Open the project’s browser edit interface from the documented local server source.
2. For the separate generation path, read the PHP deployment configuration and provider requirements. Use a cleared public HTTPS reference image if that path is enabled.
### First project

A small first project makes the input, model output and handoff easy to inspect. [Source 1](https://github.com/jcsdn/aiicut/blob/main/README.md) [Source 2](https://github.com/jcsdn/aiicut/blob/main/DEPLOYMENT.md)

1. Import a short local clip and add an editable SRT. Review crop and timing in the preview.
2. Where an authorized provider route is available, place a small generated draft alongside the source material. Note boundaries between generated and captured footage.
3. Export a browser-supported video format and check subtitle placement and track behavior. Keep originals and SRT separately.
### Hardware & software

Platform and compute constraints refer to the selected route. [Source 1](https://github.com/jcsdn/aiicut/blob/main/README.md) [Source 2](https://github.com/jcsdn/aiicut/blob/main/DEPLOYMENT.md)

- **Hardware:** Minimum RAM, VRAM and disk space for the scoped workflow are undocumented.
- **Software:** HTML/JavaScript browser editor. AI generation separately needs the PHP relay and Volcano Engine Ark/Seedance access.
- **Platforms:** The project suggests desktop Chrome or Edge and describes browser-dependent WebM/MP4 export. This does not establish support for every OS/browser pairing.

### License, model weights & costs

The full software license was reviewed. Dependencies and creative assets carry their own terms. [Source 1](https://github.com/jcsdn/aiicut/blob/main/LICENSE) [Source 2](https://github.com/jcsdn/aiicut/blob/main/README.md) [Source 3](https://github.com/jcsdn/aiicut/blob/main/DEPLOYMENT.md)

- **Code:** MIT
- **Weights:** The project source is MIT. Generated media uses the separately governed commercial model API and chosen input rights.
- **Commercial:** Project code is governed by MIT. Confirm selected model, source-media and output restrictions separately.
- **Cost:** Local edit uses device compute. Cloud generation requires separately configured provider access and pricing.

### Why it merits attention

The creative workflow is grounded in the cited documentation. Output quality and compatibility are not hands-on verified. [Source 1](https://github.com/jcsdn/aiicut/blob/main/README.md) [Source 2](https://github.com/jcsdn/aiicut/blob/main/DEPLOYMENT.md)

### Limitations

Native generation is unverified in the project’s own current status. Local source file and export resolution limits are documented. [Source 1](https://github.com/jcsdn/aiicut/blob/main/README.md) [Source 2](https://github.com/jcsdn/aiicut/blob/main/DEPLOYMENT.md)

### Get the tool

- [Repository](https://github.com/jcsdn/aiicut)
- [Documentation](https://github.com/jcsdn/aiicut/blob/main/DEPLOYMENT.md)

## BooruDatasetTagManager+

Images & design · Photography, restoration & color · AI agents for code-authored media production

First complete guide in the library. The publication and documentation dates are not necessarily the project’s launch date.

### Quality assessment: Quality unverified

Creative use and the code grant are documented. Check-level gaps remain before a recommendation.

Scope: Curate accurate paired caption files for an authorized LoRA dataset or an image-reference library.

Evidence checked: 2026-11-21. No local execution implied.

- **Open-source software license · verified:** Reviewed the complete project software grant and its redistribution conditions. Model, data and service terms are scoped separately. [Source](https://github.com/storyAura/BooruDatasetTagManagerPlus/blob/main/LICENSE)
- **Creative results · documented:** The project describes local model-generated tags, frequency and filter controls, and individual correction approval. Review predicted attributes for both missing and spurious tags. [Source](https://github.com/storyAura/BooruDatasetTagManagerPlus/blob/main/README.md) [Source](https://github.com/storyAura/BooruDatasetTagManagerPlus/blob/main/README_en.md) [Source](https://github.com/storyAura/BooruDatasetTagManagerPlus/blob/main/docs/FEATURES.md)
- **Reproducible setup · documented:** The installation and first-use steps are in the cited documentation. Reproduction of this workflow remains unverified. [Source](https://github.com/storyAura/BooruDatasetTagManagerPlus/blob/main/README.md) [Source](https://github.com/storyAura/BooruDatasetTagManagerPlus/blob/main/README_en.md) [Source](https://github.com/storyAura/BooruDatasetTagManagerPlus/blob/main/docs/FEATURES.md)
- **Maintenance and support · unknown:** The reviewed sources do not establish workflow-specific support, fixes and unresolved blockers.
- **Independent use · unknown:** Independent first-hand use of the exact workflow was not established in this source review.
- **Models, services and costs · documented:** MIT applies to the tag editor. Models, tag vocabularies, optional API terms and source-image permissions require separate review. Local compute and storage for image/model files. Optional remote tagging and character review can incur service cost. [Source](https://github.com/storyAura/BooruDatasetTagManagerPlus/blob/main/README.md) [Source](https://github.com/storyAura/BooruDatasetTagManagerPlus/blob/main/README_en.md) [Source](https://github.com/storyAura/BooruDatasetTagManagerPlus/blob/main/docs/FEATURES.md)

Source and documentation review. No hands-on execution by AI Media Scout. Models can misclassify visual attributes. Preserve media permissions and complete editorial review before using a dataset for training.

### How it uses AI

This dataset editor can propose tags with a local ONNX image model, supplement them with a vision endpoint, and stage character-label corrections for human acceptance. [Source](https://github.com/storyAura/BooruDatasetTagManagerPlus/blob/main/README.md) [Source](https://github.com/storyAura/BooruDatasetTagManagerPlus/blob/main/README_en.md) [Source](https://github.com/storyAura/BooruDatasetTagManagerPlus/blob/main/docs/FEATURES.md)

### Introduction

This dataset editor can propose tags with a local ONNX image model, supplement them with a vision endpoint, and stage character-label corrections for human acceptance. [Source 1](https://github.com/storyAura/BooruDatasetTagManagerPlus/blob/main/README.md) [Source 2](https://github.com/storyAura/BooruDatasetTagManagerPlus/blob/main/README_en.md) [Source 3](https://github.com/storyAura/BooruDatasetTagManagerPlus/blob/main/docs/FEATURES.md)

### What it is good for

Curate accurate paired caption files for an authorized LoRA dataset or an image-reference library. [Source 1](https://github.com/storyAura/BooruDatasetTagManagerPlus/blob/main/README.md) [Source 2](https://github.com/storyAura/BooruDatasetTagManagerPlus/blob/main/README_en.md) [Source 3](https://github.com/storyAura/BooruDatasetTagManagerPlus/blob/main/docs/FEATURES.md)

### Demo & examples

The project describes local model-generated tags, frequency and filter controls, and individual correction approval. Review predicted attributes for both missing and spurious tags. [Source 1](https://github.com/storyAura/BooruDatasetTagManagerPlus/blob/main/README.md) [Source 2](https://github.com/storyAura/BooruDatasetTagManagerPlus/blob/main/README_en.md) [Source 3](https://github.com/storyAura/BooruDatasetTagManagerPlus/blob/main/docs/FEATURES.md)

### Install

Follow the documented route for the scoped workflow. The steps below are source references. [Source 1](https://github.com/storyAura/BooruDatasetTagManagerPlus/blob/main/README.md) [Source 2](https://github.com/storyAura/BooruDatasetTagManagerPlus/blob/main/README_en.md) [Source 3](https://github.com/storyAura/BooruDatasetTagManagerPlus/blob/main/docs/FEATURES.md)

1. Choose the official self-contained Windows x64 project release and open a copy of a small rights-cleared image set.
2. Select the supported local ONNX tagging model. Use the separate vision endpoint only if needed and authorized for the images.
### First project

A small first project makes the input, model output and handoff easy to inspect. [Source 1](https://github.com/storyAura/BooruDatasetTagManagerPlus/blob/main/README.md) [Source 2](https://github.com/storyAura/BooruDatasetTagManagerPlus/blob/main/README_en.md) [Source 3](https://github.com/storyAura/BooruDatasetTagManagerPlus/blob/main/docs/FEATURES.md)

1. Load photos with paired text captions. Run a small local tag pass and check the results for repeated inappropriate labels.
2. Filter and correct tags in batches, then review model-assisted changes one at a time for important reference images.
3. Keep the mapping between images and plain-text tags intact in the reviewed output folder.
### Hardware & software

Platform and compute constraints refer to the selected route. [Source 1](https://github.com/storyAura/BooruDatasetTagManagerPlus/blob/main/README.md) [Source 2](https://github.com/storyAura/BooruDatasetTagManagerPlus/blob/main/README_en.md) [Source 3](https://github.com/storyAura/BooruDatasetTagManagerPlus/blob/main/docs/FEATURES.md)

- **Hardware:** Minimum RAM, VRAM and disk space for the scoped workflow are undocumented.
- **Software:** Windows package or the project’s documented .NET source build. ONNX model for local predictions. Some remote review paths need a compatible API.
- **Platforms:** Windows 10/11 x64. The project provides Simplified Chinese and English documentation.

### License, model weights & costs

The full software license was reviewed. Dependencies and creative assets carry their own terms. [Source 1](https://github.com/storyAura/BooruDatasetTagManagerPlus/blob/main/LICENSE) [Source 2](https://github.com/storyAura/BooruDatasetTagManagerPlus/blob/main/README.md) [Source 3](https://github.com/storyAura/BooruDatasetTagManagerPlus/blob/main/README_en.md) [Source 4](https://github.com/storyAura/BooruDatasetTagManagerPlus/blob/main/docs/FEATURES.md)

- **Code:** MIT
- **Weights:** MIT applies to the tag editor. Models, tag vocabularies, optional API terms and source-image permissions require separate review.
- **Commercial:** Project code is governed by MIT. Confirm selected model, source-media and output restrictions separately.
- **Cost:** Local compute and storage for image/model files. Optional remote tagging and character review can incur service cost.

### Why it merits attention

The creative workflow is grounded in the cited documentation. Output quality and compatibility are not hands-on verified. [Source 1](https://github.com/storyAura/BooruDatasetTagManagerPlus/blob/main/README.md) [Source 2](https://github.com/storyAura/BooruDatasetTagManagerPlus/blob/main/README_en.md) [Source 3](https://github.com/storyAura/BooruDatasetTagManagerPlus/blob/main/docs/FEATURES.md)

### Limitations

Models can misclassify visual attributes. Preserve media permissions and complete editorial review before using a dataset for training. [Source 1](https://github.com/storyAura/BooruDatasetTagManagerPlus/blob/main/README.md) [Source 2](https://github.com/storyAura/BooruDatasetTagManagerPlus/blob/main/README_en.md) [Source 3](https://github.com/storyAura/BooruDatasetTagManagerPlus/blob/main/docs/FEATURES.md)

### Get the tool

- [Repository](https://github.com/storyAura/BooruDatasetTagManagerPlus)
- [Documentation](https://github.com/storyAura/BooruDatasetTagManagerPlus/blob/main/docs/FEATURES.md)

## Ableton Live MCP

Audio, music & voice · Performance, projection & stage media · AI agents for code-authored media production

First complete guide in the library. The publication and documentation dates are not necessarily the project’s launch date.

### Quality assessment: Quality unverified

Creative use and the code grant are documented. Check-level gaps remain before a recommendation.

Scope: Ask an agent to draft an editable rhythm or accompaniment in a test Live set, inspect notes and timing, and audition it in context.

Evidence checked: 2026-11-21. No local execution implied.

- **Open-source software license · verified:** Reviewed the complete project software grant and its redistribution conditions. Model, data and service terms are scoped separately. [Source](https://github.com/CanArslanDev/ableton-live-mcp/blob/main/LICENSE)
- **Creative results · documented:** The maintainer describes rhythm/MIDI generation, set overview and section-reference examples. Real-time capture takes as long as the selected section plays. [Source](https://github.com/CanArslanDev/ableton-live-mcp/blob/main/README.md) [Source](https://github.com/CanArslanDev/ableton-live-mcp/blob/main/pyproject.toml) [Source](https://github.com/CanArslanDev/ableton-live-mcp/blob/main/CHANGELOG.md)
- **Reproducible setup · documented:** The installation and first-use steps are in the cited documentation. Reproduction of this workflow remains unverified. [Source](https://github.com/CanArslanDev/ableton-live-mcp/blob/main/README.md) [Source](https://github.com/CanArslanDev/ableton-live-mcp/blob/main/pyproject.toml) [Source](https://github.com/CanArslanDev/ableton-live-mcp/blob/main/CHANGELOG.md)
- **Maintenance and support · unknown:** The reviewed sources do not establish workflow-specific support, fixes and unresolved blockers.
- **Independent use · unknown:** Independent first-hand use of the exact workflow was not established in this source review.
- **Models, services and costs · documented:** The bridge uses MIT. Ableton Live is a separate proprietary host. Connected agent providers and external samples are governed separately. Live licensing and the selected agent plan may have their own fees. Local editing uses workstation compute. [Source](https://github.com/CanArslanDev/ableton-live-mcp/blob/main/README.md) [Source](https://github.com/CanArslanDev/ableton-live-mcp/blob/main/pyproject.toml) [Source](https://github.com/CanArslanDev/ableton-live-mcp/blob/main/CHANGELOG.md)

Source and documentation review. No hands-on execution by AI Media Scout. A connected agent can edit the set. The Live API lacks some automation and export operations, and the reference workflow can write real-time recordings.

### How it uses AI

An agent can inspect and edit an Ableton Live session through a documented MCP server and remote script. The integration exposes MIDI clips, reference-comparison tools and real-time track capture. [Source](https://github.com/CanArslanDev/ableton-live-mcp/blob/main/README.md) [Source](https://github.com/CanArslanDev/ableton-live-mcp/blob/main/pyproject.toml) [Source](https://github.com/CanArslanDev/ableton-live-mcp/blob/main/CHANGELOG.md)

### Introduction

An agent can inspect and edit an Ableton Live session through a documented MCP server and remote script. The integration exposes MIDI clips, reference-comparison tools and real-time track capture. [Source 1](https://github.com/CanArslanDev/ableton-live-mcp/blob/main/README.md) [Source 2](https://github.com/CanArslanDev/ableton-live-mcp/blob/main/pyproject.toml) [Source 3](https://github.com/CanArslanDev/ableton-live-mcp/blob/main/CHANGELOG.md)

### What it is good for

Ask an agent to draft an editable rhythm or accompaniment in a test Live set, inspect notes and timing, and audition it in context. [Source 1](https://github.com/CanArslanDev/ableton-live-mcp/blob/main/README.md) [Source 2](https://github.com/CanArslanDev/ableton-live-mcp/blob/main/pyproject.toml) [Source 3](https://github.com/CanArslanDev/ableton-live-mcp/blob/main/CHANGELOG.md)

### Demo & examples

The maintainer describes rhythm/MIDI generation, set overview and section-reference examples. Real-time capture takes as long as the selected section plays. [Source 1](https://github.com/CanArslanDev/ableton-live-mcp/blob/main/README.md) [Source 2](https://github.com/CanArslanDev/ableton-live-mcp/blob/main/pyproject.toml) [Source 3](https://github.com/CanArslanDev/ableton-live-mcp/blob/main/CHANGELOG.md)

### Install

Follow the documented route for the scoped workflow. The steps below are source references. [Source 1](https://github.com/CanArslanDev/ableton-live-mcp/blob/main/README.md) [Source 2](https://github.com/CanArslanDev/ableton-live-mcp/blob/main/pyproject.toml) [Source 3](https://github.com/CanArslanDev/ableton-live-mcp/blob/main/CHANGELOG.md)

1. Use the documented package or source path for a compatible client with uv and Python. Install the Remote Script in Live’s user library.
2. Enable the AbletonMCP control surface in Live and verify that server and script versions match. Use a separate scratch set for first use.
### First project

A small first project makes the input, model output and handoff easy to inspect. [Source 1](https://github.com/CanArslanDev/ableton-live-mcp/blob/main/README.md) [Source 2](https://github.com/CanArslanDev/ableton-live-mcp/blob/main/pyproject.toml) [Source 3](https://github.com/CanArslanDev/ableton-live-mcp/blob/main/CHANGELOG.md)

1. Open a test Live set and request its track and clip inventory. Choose one editable session clip.
2. Ask for a short MIDI idea, then inspect pitch, rhythm, velocity and instrument response. Preserve the original clip.
3. Audition a short section, correct the selection and save the editable part. Use Live’s own export route for delivery when the documented bridge has no matching operation.
### Hardware & software

Platform and compute constraints refer to the selected route. [Source 1](https://github.com/CanArslanDev/ableton-live-mcp/blob/main/README.md) [Source 2](https://github.com/CanArslanDev/ableton-live-mcp/blob/main/pyproject.toml) [Source 3](https://github.com/CanArslanDev/ableton-live-mcp/blob/main/CHANGELOG.md)

- **Hardware:** Minimum RAM, VRAM and disk space for the scoped workflow are undocumented.
- **Software:** Ableton Live 11 or 12, uv/Python 3.10+ and compatible MCP client. Some arrangement and device functions require Live 12 or 12.3.
- **Platforms:** macOS and Windows user-library paths are documented for Ableton Live. Check the specific host revision and features.

### License, model weights & costs

The full software license was reviewed. Dependencies and creative assets carry their own terms. [Source 1](https://github.com/CanArslanDev/ableton-live-mcp/blob/main/LICENSE) [Source 2](https://github.com/CanArslanDev/ableton-live-mcp/blob/main/README.md) [Source 3](https://github.com/CanArslanDev/ableton-live-mcp/blob/main/pyproject.toml) [Source 4](https://github.com/CanArslanDev/ableton-live-mcp/blob/main/CHANGELOG.md)

- **Code:** MIT
- **Weights:** The bridge uses MIT. Ableton Live is a separate proprietary host. Connected agent providers and external samples are governed separately.
- **Commercial:** Project code is governed by MIT. Confirm selected model, source-media and output restrictions separately.
- **Cost:** Live licensing and the selected agent plan may have their own fees. Local editing uses workstation compute.

### Why it merits attention

The creative workflow is grounded in the cited documentation. Output quality and compatibility are not hands-on verified. [Source 1](https://github.com/CanArslanDev/ableton-live-mcp/blob/main/README.md) [Source 2](https://github.com/CanArslanDev/ableton-live-mcp/blob/main/pyproject.toml) [Source 3](https://github.com/CanArslanDev/ableton-live-mcp/blob/main/CHANGELOG.md)

### Limitations

A connected agent can edit the set. The Live API lacks some automation and export operations, and the reference workflow can write real-time recordings. [Source 1](https://github.com/CanArslanDev/ableton-live-mcp/blob/main/README.md) [Source 2](https://github.com/CanArslanDev/ableton-live-mcp/blob/main/pyproject.toml) [Source 3](https://github.com/CanArslanDev/ableton-live-mcp/blob/main/CHANGELOG.md)

### Get the tool

- [Repository](https://github.com/CanArslanDev/ableton-live-mcp)
- [Documentation](https://github.com/CanArslanDev/ableton-live-mcp/blob/main/CHANGELOG.md)

## DA2N Light Field Rendering

Neural holography and light-field media · Neural multiview and glasses-free display art · Photogrammetry, scanning & neural rendering

First complete guide in the library. The publication and documentation dates are not necessarily the project’s launch date.

### Quality assessment: Quality unverified

Creative use and the code grant are documented. Check-level gaps remain before a recommendation.

Scope: Study whether interpolated camera views preserve edges for a multiview capture or display experiment.

Evidence checked: 2026-11-21. No local execution implied.

- **Open-source software license · verified:** Reviewed the complete project software grant and its redistribution conditions. Model, data and service terms are scoped separately. [Source](https://github.com/GaochangWu/DA2N/blob/main/LICENSE)
- **Creative results · documented:** The primary paper and project page show x16 angular upsampling comparisons on two light-field datasets. Results and reconstruction routes depend on the input baseline and materials. [Source](https://github.com/GaochangWu/DA2N/blob/main/README.md) [Source](https://gaochangwu.github.io/DA2N/DA2N.html) [Source](https://arxiv.org/abs/2104.06797)
- **Reproducible setup · documented:** The installation and first-use steps are in the cited documentation. Reproduction of this workflow remains unverified. [Source](https://github.com/GaochangWu/DA2N/blob/main/README.md) [Source](https://gaochangwu.github.io/DA2N/DA2N.html) [Source](https://arxiv.org/abs/2104.06797)
- **Maintenance and support · unknown:** The reviewed sources do not establish workflow-specific support, fixes and unresolved blockers.
- **Independent use · unknown:** Independent first-hand use of the exact workflow was not established in this source review.
- **Models, services and costs · documented:** MIT covers the project software. Light-field datasets, supplied checkpoint and input captures retain separate terms. Local inference requires compatible hardware. The environment age can increase setup effort. [Source](https://github.com/GaochangWu/DA2N/blob/main/README.md) [Source](https://gaochangwu.github.io/DA2N/DA2N.html) [Source](https://arxiv.org/abs/2104.06797)

Source and documentation review. No hands-on execution by AI Media Scout. The primary studies cover particular captures and scales. Upsampling quality, hardware compatibility and timing for a target display are unverified.

### How it uses AI

The published deep network interpolates or extrapolates views from a light field while reducing aliasing caused by wide view disparity. It supplies separate 3D and 4D light-field examples. [Source](https://github.com/GaochangWu/DA2N/blob/main/README.md) [Source](https://gaochangwu.github.io/DA2N/DA2N.html) [Source](https://arxiv.org/abs/2104.06797)

### Introduction

The published deep network interpolates or extrapolates views from a light field while reducing aliasing caused by wide view disparity. It supplies separate 3D and 4D light-field examples. [Source 1](https://github.com/GaochangWu/DA2N/blob/main/README.md) [Source 2](https://gaochangwu.github.io/DA2N/DA2N.html) [Source 3](https://arxiv.org/abs/2104.06797)

### What it is good for

Study whether interpolated camera views preserve edges for a multiview capture or display experiment. [Source 1](https://github.com/GaochangWu/DA2N/blob/main/README.md) [Source 2](https://gaochangwu.github.io/DA2N/DA2N.html) [Source 3](https://arxiv.org/abs/2104.06797)

### Demo & examples

The primary paper and project page show x16 angular upsampling comparisons on two light-field datasets. Results and reconstruction routes depend on the input baseline and materials. [Source 1](https://github.com/GaochangWu/DA2N/blob/main/README.md) [Source 2](https://gaochangwu.github.io/DA2N/DA2N.html) [Source 3](https://arxiv.org/abs/2104.06797)

### Install

Follow the documented route for the scoped workflow. The steps below are source references. [Source 1](https://github.com/GaochangWu/DA2N/blob/main/README.md) [Source 2](https://gaochangwu.github.io/DA2N/DA2N.html) [Source 3](https://arxiv.org/abs/2104.06797)

1. Recreate the source-documented Python 3.7.4 and tensorflow-gpu 1.13.1 environment separately from current tooling.
2. Acquire authorized source light fields and put the matching sample/checkpoint assets in the documented folders. Validate compatibility with the old GPU stack before a larger batch.
### First project

A small first project makes the input, model output and handoff easy to inspect. [Source 1](https://github.com/GaochangWu/DA2N/blob/main/README.md) [Source 2](https://gaochangwu.github.io/DA2N/DA2N.html) [Source 3](https://arxiv.org/abs/2104.06797)

1. Select the one-angular-axis or 4D reconstruction script. Place one example in the expected dataset layout.
2. Run interpolation at a documented scale and compare synthesized and measured views. Inspect thin edges and reflective regions before selecting a display test.
### Hardware & software

Platform and compute constraints refer to the selected route. [Source 1](https://github.com/GaochangWu/DA2N/blob/main/README.md) [Source 2](https://gaochangwu.github.io/DA2N/DA2N.html) [Source 3](https://arxiv.org/abs/2104.06797)

- **Hardware:** Minimum RAM, VRAM and disk space for the scoped workflow are undocumented.
- **Software:** Python 3.7.4, tensorflow-gpu 1.13.1 and compatible GPU runtime. Custom training data is documented in HDF5.
- **Platforms:** The archived environment specifies a historical GPU and Python stack. Current native OS and device compatibility remain unverified.

### License, model weights & costs

The full software license was reviewed. Dependencies and creative assets carry their own terms. [Source 1](https://github.com/GaochangWu/DA2N/blob/main/LICENSE) [Source 2](https://github.com/GaochangWu/DA2N/blob/main/README.md) [Source 3](https://gaochangwu.github.io/DA2N/DA2N.html) [Source 4](https://arxiv.org/abs/2104.06797)

- **Code:** MIT
- **Weights:** MIT covers the project software. Light-field datasets, supplied checkpoint and input captures retain separate terms.
- **Commercial:** Project code is governed by MIT. Confirm selected model, source-media and output restrictions separately.
- **Cost:** Local inference requires compatible hardware. The environment age can increase setup effort.

### Why it merits attention

The creative workflow is grounded in the cited documentation. Output quality and compatibility are not hands-on verified. [Source 1](https://github.com/GaochangWu/DA2N/blob/main/README.md) [Source 2](https://gaochangwu.github.io/DA2N/DA2N.html) [Source 3](https://arxiv.org/abs/2104.06797)

### Limitations

The primary studies cover particular captures and scales. Upsampling quality, hardware compatibility and timing for a target display are unverified. [Source 1](https://github.com/GaochangWu/DA2N/blob/main/README.md) [Source 2](https://gaochangwu.github.io/DA2N/DA2N.html) [Source 3](https://arxiv.org/abs/2104.06797)

### Get the tool

- [Repository](https://github.com/GaochangWu/DA2N)
- [Documentation](https://arxiv.org/abs/2104.06797)

## soundmon

Audio, music & voice · AI Foley and sound effects · AI seamless loops, sample design and DAW-ready stems

First complete guide in the library. The publication and documentation dates are not necessarily the project’s launch date.

### Quality assessment: Quality unverified

Creative use and the code grant are documented. Check-level gaps remain before a recommendation.

Scope: Generate a short set of game sound-effect candidates locally, inspect them in the editor and export selected assets with original files retained.

Evidence checked: 2026-11-21. No local execution implied.

- **Open-source software license · verified:** Reviewed the complete project software grant and its redistribution conditions. Model, data and service terms are scoped separately. [Source](https://github.com/grymmjack/soundmon/blob/main/LICENSE)
- **Creative results · documented:** The maintainer supplies a CLI and a GUI for selecting and exporting variations. The current docs distinguish the default model from the Stable Audio Open 1.0 fallback. [Source](https://github.com/grymmjack/soundmon/blob/main/README.md) [Source](https://huggingface.co/stabilityai/stable-audio-open-1.0)
- **Reproducible setup · documented:** The installation and first-use steps are in the cited documentation. Reproduction of this workflow remains unverified. [Source](https://github.com/grymmjack/soundmon/blob/main/README.md) [Source](https://huggingface.co/stabilityai/stable-audio-open-1.0)
- **Maintenance and support · unknown:** The reviewed sources do not establish workflow-specific support, fixes and unresolved blockers.
- **Independent use · unknown:** Independent first-hand use of the exact workflow was not established in this source review.
- **Models, services and costs · documented:** MIT applies to project code. Stable Audio Open 1.0, SA3 and other distinct model packs remain governed by their own terms. This workflow uses local inference after model downloads. Accelerator, storage and optional remote hosts affect costs. [Source](https://github.com/grymmjack/soundmon/blob/main/README.md) [Source](https://huggingface.co/stabilityai/stable-audio-open-1.0)

Source and documentation review. No hands-on execution by AI Media Scout. A generated take is source material for audition and cleanup. Document the model branch used and independently verify machine compatibility.

### How it uses AI

The toolkit uses local text-to-audio checkpoints behind a ComfyUI workflow to create sound effects and loops, then gives the creator editing and export options for the resulting WAV. [Source](https://github.com/grymmjack/soundmon/blob/main/README.md) [Source](https://huggingface.co/stabilityai/stable-audio-open-1.0)

### Introduction

The toolkit uses local text-to-audio checkpoints behind a ComfyUI workflow to create sound effects and loops, then gives the creator editing and export options for the resulting WAV. [Source 1](https://github.com/grymmjack/soundmon/blob/main/README.md) [Source 2](https://huggingface.co/stabilityai/stable-audio-open-1.0)

### What it is good for

Generate a short set of game sound-effect candidates locally, inspect them in the editor and export selected assets with original files retained. [Source 1](https://github.com/grymmjack/soundmon/blob/main/README.md) [Source 2](https://huggingface.co/stabilityai/stable-audio-open-1.0)

### Demo & examples

The maintainer supplies a CLI and a GUI for selecting and exporting variations. The current docs distinguish the default model from the Stable Audio Open 1.0 fallback. [Source 1](https://github.com/grymmjack/soundmon/blob/main/README.md) [Source 2](https://huggingface.co/stabilityai/stable-audio-open-1.0)

### Install

Follow the documented route for the scoped workflow. The steps below are source references. [Source 1](https://github.com/grymmjack/soundmon/blob/main/README.md) [Source 2](https://huggingface.co/stabilityai/stable-audio-open-1.0)

1. Confirm a working ComfyUI environment using the source docs. Review the supported platform path and install only the model route and node you intend to use.
2. For a focused first comparison use the documented Stable Audio Open fallback and confirm its model license and required assets.
### First project

A small first project makes the input, model output and handoff easy to inspect. [Source 1](https://github.com/grymmjack/soundmon/blob/main/README.md) [Source 2](https://huggingface.co/stabilityai/stable-audio-open-1.0)

1. Generate a few short variants from one description, retaining the prompts, seed/settings and raw WAV.
2. Compare onset, tail, noise and variation. Trim or layer a selected take, then export it separately beside the reference.
3. Check file timing and loop seams inside the target game or sound editor.
### Hardware & software

Platform and compute constraints refer to the selected route. [Source 1](https://github.com/grymmjack/soundmon/blob/main/README.md) [Source 2](https://huggingface.co/stabilityai/stable-audio-open-1.0)

- **Hardware:** The current README gives roughly 14 GB of models for the default SA3 stack. The selected fallback has distinct capacity requirements. Minimum system RAM and VRAM are undocumented for this scope.
- **Software:** A compatible ComfyUI installation and Python environment, node integration and selected weights. Soundmon documents optional alternative engines for music and narration.
- **Platforms:** The repository documents multiple accelerator routes via ComfyUI. Confirm the backend and selected model for the actual Windows, Linux or Mac host.

### License, model weights & costs

The full software license was reviewed. Dependencies and creative assets carry their own terms. [Source 1](https://github.com/grymmjack/soundmon/blob/main/LICENSE) [Source 2](https://github.com/grymmjack/soundmon/blob/main/README.md) [Source 3](https://huggingface.co/stabilityai/stable-audio-open-1.0)

- **Code:** MIT
- **Weights:** MIT applies to project code. Stable Audio Open 1.0, SA3 and other distinct model packs remain governed by their own terms.
- **Commercial:** Project code is governed by MIT. Confirm selected model, source-media and output restrictions separately.
- **Cost:** This workflow uses local inference after model downloads. Accelerator, storage and optional remote hosts affect costs.

### Why it merits attention

The creative workflow is grounded in the cited documentation. Output quality and compatibility are not hands-on verified. [Source 1](https://github.com/grymmjack/soundmon/blob/main/README.md) [Source 2](https://huggingface.co/stabilityai/stable-audio-open-1.0)

### Limitations

A generated take is source material for audition and cleanup. Document the model branch used and independently verify machine compatibility. [Source 1](https://github.com/grymmjack/soundmon/blob/main/README.md) [Source 2](https://huggingface.co/stabilityai/stable-audio-open-1.0)

### Get the tool

- [Repository](https://github.com/grymmjack/soundmon)
- [Documentation](https://huggingface.co/stabilityai/stable-audio-open-1.0)

## Tscaps

Editing, captions & post-production · Video, animation & film · Accessible media & assistive creation

First complete guide in the library. The publication and documentation dates are not necessarily the project’s launch date.

### Quality assessment: Quality unverified

Creative use and the code grant are documented. Check-level gaps remain before a recommendation.

Scope: Turn one speech recording into a vertical proof with editable timed captions and controlled cut points without uploading the source clip.

Evidence checked: 2026-11-21. No local execution implied.

- **Open-source software license · verified:** Reviewed the complete project software grant and its redistribution conditions. Model, data and service terms are scoped separately. [Source](https://github.com/francozanardi/tscaps/blob/main/LICENSE)
- **Creative results · documented:** The project documents an in-browser editor, local Whisper and word-driven editing. It explains codec and mobile constraints. A successful import for a specific camera codec needs separate verification. [Source](https://github.com/francozanardi/tscaps/blob/main/README.md) [Source](https://tscaps.io/local) [Source](https://github.com/francozanardi/tscaps/blob/main/apps/studio/mcp/README.md)
- **Reproducible setup · documented:** The installation and first-use steps are in the cited documentation. Reproduction of this workflow remains unverified. [Source](https://github.com/francozanardi/tscaps/blob/main/README.md) [Source](https://tscaps.io/local) [Source](https://github.com/francozanardi/tscaps/blob/main/apps/studio/mcp/README.md)
- **Maintenance and support · unknown:** The reviewed sources do not establish workflow-specific support, fixes and unresolved blockers.
- **Independent use · unknown:** Independent first-hand use of the exact workflow was not established in this source review.
- **Models, services and costs · documented:** The editor is AGPLv3. Engine, presets and skills have separate MIT grants. Model cards, fonts, imported clips and assets need distinct checks. Local inference and encoding use device resources. The separately offered hosted transcription route has its own terms and prices. [Source](https://github.com/francozanardi/tscaps/blob/main/README.md) [Source](https://tscaps.io/local) [Source](https://github.com/francozanardi/tscaps/blob/main/apps/studio/mcp/README.md)

Source and documentation review. No hands-on execution by AI Media Scout. The local route is constrained by browser and hardware. Older or unsupported codecs, word timing and phone speed need a small controlled check.

### How it uses AI

Tscaps uses local Whisper word timings to segment and caption short videos in a browser editor. Interactive effects and edit decisions remain represented in editable projects. [Source](https://github.com/francozanardi/tscaps/blob/main/README.md) [Source](https://tscaps.io/local) [Source](https://github.com/francozanardi/tscaps/blob/main/apps/studio/mcp/README.md)

### Introduction

Tscaps uses local Whisper word timings to segment and caption short videos in a browser editor. Interactive effects and edit decisions remain represented in editable projects. [Source 1](https://github.com/francozanardi/tscaps/blob/main/README.md) [Source 2](https://tscaps.io/local) [Source 3](https://github.com/francozanardi/tscaps/blob/main/apps/studio/mcp/README.md)

### What it is good for

Turn one speech recording into a vertical proof with editable timed captions and controlled cut points without uploading the source clip. [Source 1](https://github.com/francozanardi/tscaps/blob/main/README.md) [Source 2](https://tscaps.io/local) [Source 3](https://github.com/francozanardi/tscaps/blob/main/apps/studio/mcp/README.md)

### Demo & examples

The project documents an in-browser editor, local Whisper and word-driven editing. It explains codec and mobile constraints. A successful import for a specific camera codec needs separate verification. [Source 1](https://github.com/francozanardi/tscaps/blob/main/README.md) [Source 2](https://tscaps.io/local) [Source 3](https://github.com/francozanardi/tscaps/blob/main/apps/studio/mcp/README.md)

### Install

Follow the documented route for the scoped workflow. The steps below are source references. [Source 1](https://github.com/francozanardi/tscaps/blob/main/README.md) [Source 2](https://tscaps.io/local) [Source 3](https://github.com/francozanardi/tscaps/blob/main/apps/studio/mcp/README.md)

1. Use the documented modern Chrome/Edge/Chromium route. For self-hosting use Node.js 20 or later and the repository package setup.
2. Acquire the selected local speech model on first use. Set up the MCP tooling only if intentionally using a separate assistant.
### First project

A small first project makes the input, model output and handoff easy to inspect. [Source 1](https://github.com/francozanardi/tscaps/blob/main/README.md) [Source 2](https://tscaps.io/local) [Source 3](https://github.com/francozanardi/tscaps/blob/main/apps/studio/mcp/README.md)

1. Drop a short supported clip into the editor and let the local model draft timing. Review cuts and highlighted words against the speech.
2. Correct styling and caption text, then export a short preview. Verify codec handling and what remains editable before a longer production.
### Hardware & software

Platform and compute constraints refer to the selected route. [Source 1](https://github.com/francozanardi/tscaps/blob/main/README.md) [Source 2](https://tscaps.io/local) [Source 3](https://github.com/francozanardi/tscaps/blob/main/apps/studio/mcp/README.md)

- **Hardware:** The current README estimates about 75 MB for the default model. Device runtime and storage depend on clip length and model. It documents slow transcription on mid-range phones.
- **Software:** Modern browser with working WebCodecs for the chosen inputs. Local Whisper needs a model download. The source build requires Node.js 20 or later.
- **Platforms:** Modern Chromium-family browser route, with support dependent on installed codec and encoder. Phone access does not imply desktop performance. HEVC conversion is labeled experimental.

### License, model weights & costs

The full software license was reviewed. Dependencies and creative assets carry their own terms. [Source 1](https://github.com/francozanardi/tscaps/blob/main/LICENSE) [Source 2](https://github.com/francozanardi/tscaps/blob/main/README.md) [Source 3](https://tscaps.io/local) [Source 4](https://github.com/francozanardi/tscaps/blob/main/apps/studio/mcp/README.md)

- **Code:** AGPL-3.0
- **Weights:** The editor is AGPLv3. Engine, presets and skills have separate MIT grants. Model cards, fonts, imported clips and assets need distinct checks.
- **Commercial:** Project code is governed by AGPL-3.0. Confirm selected model, source-media and output restrictions separately.
- **Cost:** Local inference and encoding use device resources. The separately offered hosted transcription route has its own terms and prices.

### Why it merits attention

The creative workflow is grounded in the cited documentation. Output quality and compatibility are not hands-on verified. [Source 1](https://github.com/francozanardi/tscaps/blob/main/README.md) [Source 2](https://tscaps.io/local) [Source 3](https://github.com/francozanardi/tscaps/blob/main/apps/studio/mcp/README.md)

### Limitations

The local route is constrained by browser and hardware. Older or unsupported codecs, word timing and phone speed need a small controlled check. [Source 1](https://github.com/francozanardi/tscaps/blob/main/README.md) [Source 2](https://tscaps.io/local) [Source 3](https://github.com/francozanardi/tscaps/blob/main/apps/studio/mcp/README.md)

### Get the tool

- [Repository](https://github.com/francozanardi/tscaps)
- [Documentation](https://github.com/francozanardi/tscaps/blob/main/apps/studio/mcp/README.md)

## Clipframe

AI kinetic typography and animated lettering · Editing, captions & post-production · Computational art & creative coding

The source repository was created on 2026-11-21. This is its first complete guide in the library.

### Quality assessment: Quality unverified

Creative use and the code grant are documented. Check-level gaps remain before a recommendation.

Scope: Create a short data-driven title or explainer from editable JSON, reviewing exact frames and text before the final render.

Evidence checked: 2026-11-21. No local execution implied.

- **Open-source software license · verified:** Reviewed the complete project software grant and its redistribution conditions. Model, data and service terms are scoped separately. [Source](https://github.com/ferdousmikdad/clipframe/blob/main/LICENSE)
- **Creative results · documented:** The project documents example videos, template blocks, still rendering and project validation. Test whether local fonts and codecs match a representative output. [Source](https://github.com/ferdousmikdad/clipframe/blob/main/README.md) [Source](https://github.com/ferdousmikdad/clipframe/blob/main/package.json)
- **Reproducible setup · documented:** The installation and first-use steps are in the cited documentation. Reproduction of this workflow remains unverified. [Source](https://github.com/ferdousmikdad/clipframe/blob/main/README.md) [Source](https://github.com/ferdousmikdad/clipframe/blob/main/package.json)
- **Maintenance and support · unknown:** The reviewed sources do not establish workflow-specific support, fixes and unresolved blockers.
- **Independent use · unknown:** Independent first-hand use of the exact workflow was not established in this source review.
- **Models, services and costs · documented:** MIT covers project software. Fonts, source data, external imagery and separate model terms need their own review. The local rendering path requires local compute. A connected agent and outside asset sources can add access costs. [Source](https://github.com/ferdousmikdad/clipframe/blob/main/README.md) [Source](https://github.com/ferdousmikdad/clipframe/blob/main/package.json)

Source and documentation review. No hands-on execution by AI Media Scout. Output depends on installed fonts and browser version. The project describes several limitations compared with engines that render interactive embedded elements.

### How it uses AI

Clipframe supplies a JSON video engine and an MCP path that lets an AI agent assemble validated, editable compositions from supported blocks and inspect still frames before rendering. [Source](https://github.com/ferdousmikdad/clipframe/blob/main/README.md) [Source](https://github.com/ferdousmikdad/clipframe/blob/main/package.json)

### Introduction

Clipframe supplies a JSON video engine and an MCP path that lets an AI agent assemble validated, editable compositions from supported blocks and inspect still frames before rendering. [Source 1](https://github.com/ferdousmikdad/clipframe/blob/main/README.md) [Source 2](https://github.com/ferdousmikdad/clipframe/blob/main/package.json)

### What it is good for

Create a short data-driven title or explainer from editable JSON, reviewing exact frames and text before the final render. [Source 1](https://github.com/ferdousmikdad/clipframe/blob/main/README.md) [Source 2](https://github.com/ferdousmikdad/clipframe/blob/main/package.json)

### Demo & examples

The project documents example videos, template blocks, still rendering and project validation. Test whether local fonts and codecs match a representative output. [Source 1](https://github.com/ferdousmikdad/clipframe/blob/main/README.md) [Source 2](https://github.com/ferdousmikdad/clipframe/blob/main/package.json)

### Install

Follow the documented route for the scoped workflow. The steps below are source references. [Source 1](https://github.com/ferdousmikdad/clipframe/blob/main/README.md) [Source 2](https://github.com/ferdousmikdad/clipframe/blob/main/package.json)

1. Use Node.js 20 or later and installed Chrome or Edge. The documented Chromium fallback uses Playwright.
2. Clone the source, install its dependencies, build and link the CLI using the documented local route. The publisher says npm publication is pending.

```sh
npm install
```


```sh
npm run build
```


```sh
npm link
```


```sh
clipframe init my-video
```

### First project

A small first project makes the input, model output and handoff easy to inspect. [Source 1](https://github.com/ferdousmikdad/clipframe/blob/main/README.md) [Source 2](https://github.com/ferdousmikdad/clipframe/blob/main/package.json)

1. Choose a simple composition with explicit fonts and short text. Have the agent draft supported blocks or edit JSON directly.
2. Validate the project and render a still at a key moment. Correct layout and render a short final proof before scaling.
### Hardware & software

Platform and compute constraints refer to the selected route. [Source 1](https://github.com/ferdousmikdad/clipframe/blob/main/README.md) [Source 2](https://github.com/ferdousmikdad/clipframe/blob/main/package.json)

- **Hardware:** Minimum RAM, VRAM and disk space for the scoped workflow are undocumented.
- **Software:** Node.js 20+, compatible rendering browser and a locally built Clipframe checkout. Connected-agent use needs an MCP host and model access.
- **Platforms:** Browser and Node rendering prerequisites apply. Native OS-specific installer and performance guarantees were not established.

### License, model weights & costs

The full software license was reviewed. Dependencies and creative assets carry their own terms. [Source 1](https://github.com/ferdousmikdad/clipframe/blob/main/LICENSE) [Source 2](https://github.com/ferdousmikdad/clipframe/blob/main/README.md) [Source 3](https://github.com/ferdousmikdad/clipframe/blob/main/package.json)

- **Code:** MIT
- **Weights:** MIT covers project software. Fonts, source data, external imagery and separate model terms need their own review.
- **Commercial:** Project code is governed by MIT. Confirm selected model, source-media and output restrictions separately.
- **Cost:** The local rendering path requires local compute. A connected agent and outside asset sources can add access costs.

### Why it merits attention

The creative workflow is grounded in the cited documentation. Output quality and compatibility are not hands-on verified. [Source 1](https://github.com/ferdousmikdad/clipframe/blob/main/README.md) [Source 2](https://github.com/ferdousmikdad/clipframe/blob/main/package.json)

### Limitations

Output depends on installed fonts and browser version. The project describes several limitations compared with engines that render interactive embedded elements. [Source 1](https://github.com/ferdousmikdad/clipframe/blob/main/README.md) [Source 2](https://github.com/ferdousmikdad/clipframe/blob/main/package.json)

### Get the tool

- [Repository](https://github.com/ferdousmikdad/clipframe)
- [Documentation](https://github.com/ferdousmikdad/clipframe/blob/main/package.json)

## HanziFX

AI kinetic typography and animated lettering · Typography, fonts & layout · Video, animation & film

The source repository was created on 2026-11-20. This is its first complete guide in the library.

### Quality assessment: Quality unverified

Creative use and the code grant are documented. Check-level gaps remain before a recommendation.

Scope: Make a short Chinese title overlay and keep the effect’s parameters and text separate from the proof render.

Evidence checked: 2026-11-21. No local execution implied.

- **Open-source software license · verified:** Reviewed the complete project software grant and its redistribution conditions. Model, data and service terms are scoped separately. [Source](https://github.com/BitmanAlan/hanzifx/blob/main/LICENSE)
- **Creative results · documented:** The template gallery provides posters and animations. The README marks specific effects as prototype-ready and states which platform comparisons are only inferred. [Source](https://github.com/BitmanAlan/hanzifx/blob/main/README.md) [Source](https://github.com/BitmanAlan/hanzifx/blob/main/NOTICE.md)
- **Reproducible setup · documented:** The installation and first-use steps are in the cited documentation. Reproduction of this workflow remains unverified. [Source](https://github.com/BitmanAlan/hanzifx/blob/main/README.md) [Source](https://github.com/BitmanAlan/hanzifx/blob/main/NOTICE.md)
- **Maintenance and support · unknown:** The reviewed sources do not establish workflow-specific support, fixes and unresolved blockers.
- **Independent use · unknown:** Independent first-hand use of the exact workflow was not established in this source review.
- **Models, services and costs · documented:** The MIT project grant was reviewed. Individual fonts, samples and any agent model follow separate terms and notices. Local preview/encoding uses compute and initial dependency storage. Host/model access may have separate terms. [Source](https://github.com/BitmanAlan/hanzifx/blob/main/README.md) [Source](https://github.com/BitmanAlan/hanzifx/blob/main/NOTICE.md)

Source and documentation review. No hands-on execution by AI Media Scout. Some templates are marked prototype-ready and can change. Social platform suitability is a maintainer inference when explicitly labeled.

### How it uses AI

The project provides a catalog of Chinese text-motion templates and an agent-compatible scaffold that selects, parameterizes and exports a specific visual effect. [Source](https://github.com/BitmanAlan/hanzifx/blob/main/README.md) [Source](https://github.com/BitmanAlan/hanzifx/blob/main/NOTICE.md)

### Introduction

The project provides a catalog of Chinese text-motion templates and an agent-compatible scaffold that selects, parameterizes and exports a specific visual effect. [Source 1](https://github.com/BitmanAlan/hanzifx/blob/main/README.md) [Source 2](https://github.com/BitmanAlan/hanzifx/blob/main/NOTICE.md)

### What it is good for

Make a short Chinese title overlay and keep the effect’s parameters and text separate from the proof render. [Source 1](https://github.com/BitmanAlan/hanzifx/blob/main/README.md) [Source 2](https://github.com/BitmanAlan/hanzifx/blob/main/NOTICE.md)

### Demo & examples

The template gallery provides posters and animations. The README marks specific effects as prototype-ready and states which platform comparisons are only inferred. [Source 1](https://github.com/BitmanAlan/hanzifx/blob/main/README.md) [Source 2](https://github.com/BitmanAlan/hanzifx/blob/main/NOTICE.md)

### Install

Follow the documented route for the scoped workflow. The steps below are source references. [Source 1](https://github.com/BitmanAlan/hanzifx/blob/main/README.md) [Source 2](https://github.com/BitmanAlan/hanzifx/blob/main/NOTICE.md)

1. Review the selected style’s documented parameters. Prepare the documented FFmpeg/ffprobe and browser renderer, and download fonts only under their stated terms.
2. Use the documented skill installation or use the project directly. Confirm the chosen host executable before linking a skill.
### First project

A small first project makes the input, model output and handoff easy to inspect. [Source 1](https://github.com/BitmanAlan/hanzifx/blob/main/README.md) [Source 2](https://github.com/BitmanAlan/hanzifx/blob/main/NOTICE.md)

1. Select a template for a short approved Chinese headline. Adjust duration and typography without changing the source video.
2. Render a small proof, checking legibility and whether the expected transparency is supported. Preserve the editable template settings.
### Hardware & software

Platform and compute constraints refer to the selected route. [Source 1](https://github.com/BitmanAlan/hanzifx/blob/main/README.md) [Source 2](https://github.com/BitmanAlan/hanzifx/blob/main/NOTICE.md)

- **Hardware:** Pinned browser download is described as approximately 100 MB. RAM, graphics and complete disk minima are undocumented.
- **Software:** FFmpeg with codec support for the selected output, the documented browser renderer and fonts. Agent-driven use adds a compatible host.
- **Platforms:** The docs list distinct FFmpeg install examples for macOS, Windows and Linux. Overall end-to-end behavior on each combination is unverified.

### License, model weights & costs

The full software license was reviewed. Dependencies and creative assets carry their own terms. [Source 1](https://github.com/BitmanAlan/hanzifx/blob/main/LICENSE) [Source 2](https://github.com/BitmanAlan/hanzifx/blob/main/README.md) [Source 3](https://github.com/BitmanAlan/hanzifx/blob/main/NOTICE.md)

- **Code:** MIT
- **Weights:** The MIT project grant was reviewed. Individual fonts, samples and any agent model follow separate terms and notices.
- **Commercial:** Project code is governed by MIT. Confirm selected model, source-media and output restrictions separately.
- **Cost:** Local preview/encoding uses compute and initial dependency storage. Host/model access may have separate terms.

### Why it merits attention

The creative workflow is grounded in the cited documentation. Output quality and compatibility are not hands-on verified. [Source 1](https://github.com/BitmanAlan/hanzifx/blob/main/README.md) [Source 2](https://github.com/BitmanAlan/hanzifx/blob/main/NOTICE.md)

### Limitations

Some templates are marked prototype-ready and can change. Social platform suitability is a maintainer inference when explicitly labeled. [Source 1](https://github.com/BitmanAlan/hanzifx/blob/main/README.md) [Source 2](https://github.com/BitmanAlan/hanzifx/blob/main/NOTICE.md)

### Get the tool

- [Repository](https://github.com/BitmanAlan/hanzifx)
- [Documentation](https://github.com/BitmanAlan/hanzifx/blob/main/NOTICE.md)

## Argmax Open-Source SDK

Audio, music & voice · Mobile, edge & on-device creation · Accessible media & assistive creation

First complete guide in the library. The publication and documentation dates are not necessarily the project’s launch date.

### Quality assessment: Quality unverified

Creative use and the code grant are documented. Check-level gaps remain before a recommendation.

Scope: Add a timed draft transcript to a small Apple-platform audio editor or captioning prototype.

Evidence checked: 2026-11-21. No local execution implied.

- **Open-source software license · verified:** Reviewed the complete project software grant and its redistribution conditions. Model, data and service terms are scoped separately. [Source](https://github.com/argmaxinc/argmax-oss-swift/blob/main/LICENSE)
- **Creative results · documented:** The maintainer supplies Swift package examples and a CLI route. The separate Pro SDK is excluded from this scope. [Source](https://github.com/argmaxinc/argmax-oss-swift/blob/main/README.md) [Source](https://github.com/argmaxinc/argmax-oss-swift/blob/main/Package.swift) [Source](https://huggingface.co/argmaxinc/whisperkit-coreml)
- **Reproducible setup · documented:** The installation and first-use steps are in the cited documentation. Reproduction of this workflow remains unverified. [Source](https://github.com/argmaxinc/argmax-oss-swift/blob/main/README.md) [Source](https://github.com/argmaxinc/argmax-oss-swift/blob/main/Package.swift) [Source](https://huggingface.co/argmaxinc/whisperkit-coreml)
- **Maintenance and support · documented:** The v1.1.1 release and package declaration were reviewed. First-hand evidence for this app integration remains open. [Source](https://github.com/argmaxinc/argmax-oss-swift/releases/tag/v1.1.1)
- **Independent use · unknown:** Independent first-hand use of the exact workflow was not established in this source review.
- **Models, services and costs · documented:** MIT applies to the source SDK. App Store distribution, Core ML models and Argmax Pro remain separate. Review the exact downloaded checkpoint terms. Local inference uses device compute and model downloads. Additional Pro features are outside this scope. [Source](https://github.com/argmaxinc/argmax-oss-swift/blob/main/README.md) [Source](https://github.com/argmaxinc/argmax-oss-swift/blob/main/Package.swift) [Source](https://huggingface.co/argmaxinc/whisperkit-coreml)

Source and documentation review. No hands-on execution by AI Media Scout. Documentation and build-target availability do not establish latency or accuracy on a particular Apple device. Check exact product and backend.

### How it uses AI

The open-source Swift SDK includes WhisperKit for speech recognition and separate TTSKit and SpeakerKit products. A creator-facing app can select WhisperKit for local timed transcription. [Source](https://github.com/argmaxinc/argmax-oss-swift/blob/main/README.md) [Source](https://github.com/argmaxinc/argmax-oss-swift/blob/main/Package.swift) [Source](https://huggingface.co/argmaxinc/whisperkit-coreml)

### Introduction

The open-source Swift SDK includes WhisperKit for speech recognition and separate TTSKit and SpeakerKit products. A creator-facing app can select WhisperKit for local timed transcription. [Source 1](https://github.com/argmaxinc/argmax-oss-swift/blob/main/README.md) [Source 2](https://github.com/argmaxinc/argmax-oss-swift/blob/main/Package.swift) [Source 3](https://huggingface.co/argmaxinc/whisperkit-coreml)

### What it is good for

Add a timed draft transcript to a small Apple-platform audio editor or captioning prototype. [Source 1](https://github.com/argmaxinc/argmax-oss-swift/blob/main/README.md) [Source 2](https://github.com/argmaxinc/argmax-oss-swift/blob/main/Package.swift) [Source 3](https://huggingface.co/argmaxinc/whisperkit-coreml)

### Demo & examples

The maintainer supplies Swift package examples and a CLI route. The separate Pro SDK is excluded from this scope. [Source 1](https://github.com/argmaxinc/argmax-oss-swift/blob/main/README.md) [Source 2](https://github.com/argmaxinc/argmax-oss-swift/blob/main/Package.swift) [Source 3](https://huggingface.co/argmaxinc/whisperkit-coreml)

### Install

Follow the documented route for the scoped workflow. The steps below are source references. [Source 1](https://github.com/argmaxinc/argmax-oss-swift/blob/main/README.md) [Source 2](https://github.com/argmaxinc/argmax-oss-swift/blob/main/Package.swift) [Source 3](https://huggingface.co/argmaxinc/whisperkit-coreml)

1. Prepare the documented Apple developer environment with Xcode 16 or newer. Add the canonical Swift package or choose the documented Homebrew CLI.
2. Select only WhisperKit for the sample. Confirm model compatibility and obtain the exact artifact through its declared source.

```sh
brew install whisperkit-cli
```

### First project

A small first project makes the input, model output and handoff easy to inspect. [Source 1](https://github.com/argmaxinc/argmax-oss-swift/blob/main/README.md) [Source 2](https://github.com/argmaxinc/argmax-oss-swift/blob/main/Package.swift) [Source 3](https://huggingface.co/argmaxinc/whisperkit-coreml)

1. Create a test project with the official package example. Load a short authorized recording and inspect timing and language output.
2. Adapt the timed segments to your editorial tool and compare each boundary. Keep the selected model identifier with the draft.
### Hardware & software

Platform and compute constraints refer to the selected route. [Source 1](https://github.com/argmaxinc/argmax-oss-swift/blob/main/README.md) [Source 2](https://github.com/argmaxinc/argmax-oss-swift/blob/main/Package.swift) [Source 3](https://huggingface.co/argmaxinc/whisperkit-coreml)

- **Hardware:** Minimum RAM, VRAM and disk space for the scoped workflow are undocumented.
- **Software:** Xcode 16 or newer in the documented setup on macOS 14+. Swift Package Manager product WhisperKit and a compatible Core ML artifact; optional TTS and diarization products have distinct routes.
- **Platforms:** The current package declares macOS 13, iOS 16, watchOS 10 and visionOS 1 platform minima. The README for development lists macOS 14+. Feature and model performance on every declared target are unverified.

### License, model weights & costs

The full software license was reviewed. Dependencies and creative assets carry their own terms. [Source 1](https://github.com/argmaxinc/argmax-oss-swift/blob/main/LICENSE) [Source 2](https://github.com/argmaxinc/argmax-oss-swift/blob/main/README.md) [Source 3](https://github.com/argmaxinc/argmax-oss-swift/blob/main/Package.swift) [Source 4](https://huggingface.co/argmaxinc/whisperkit-coreml)

- **Code:** MIT
- **Weights:** MIT applies to the source SDK. App Store distribution, Core ML models and Argmax Pro remain separate. Review the exact downloaded checkpoint terms.
- **Commercial:** Project code is governed by MIT. Confirm selected model, source-media and output restrictions separately.
- **Cost:** Local inference uses device compute and model downloads. Additional Pro features are outside this scope.

### Why it merits attention

The creative workflow is grounded in the cited documentation. Output quality and compatibility are not hands-on verified. [Source 1](https://github.com/argmaxinc/argmax-oss-swift/blob/main/README.md) [Source 2](https://github.com/argmaxinc/argmax-oss-swift/blob/main/Package.swift) [Source 3](https://huggingface.co/argmaxinc/whisperkit-coreml)

### Limitations

Documentation and build-target availability do not establish latency or accuracy on a particular Apple device. Check exact product and backend. [Source 1](https://github.com/argmaxinc/argmax-oss-swift/blob/main/README.md) [Source 2](https://github.com/argmaxinc/argmax-oss-swift/blob/main/Package.swift) [Source 3](https://huggingface.co/argmaxinc/whisperkit-coreml)

### Get the tool

- [Repository](https://github.com/argmaxinc/argmax-oss-swift)
- [Documentation](https://huggingface.co/argmaxinc/whisperkit-coreml)

## AI Short Drama Studio

Video, animation & film · Storyboarding, narrative & comics · AI agents for code-authored media production

First complete guide in the library. The publication and documentation dates are not necessarily the project’s launch date.

### Quality assessment: Quality unverified

Creative use and the code grant are documented. Check-level gaps remain before a recommendation.

Scope: Develop one scene from a script and a character reference, then replace a single generated asset without discarding the whole draft.

Evidence checked: 2026-11-21. No local execution implied.

- **Open-source software license · verified:** Reviewed the complete project software grant and its redistribution conditions. Model, data and service terms are scoped separately. [Source](https://github.com/JerrIsTheBesta/AI-Short-Drama-Studio/blob/main/LICENSE)
- **Creative results · documented:** The source shows a canvas and genre-oriented scene generation. Model and provider choice changes the possible results and limits. [Source](https://github.com/JerrIsTheBesta/AI-Short-Drama-Studio/blob/main/README.md)
- **Reproducible setup · documented:** The installation and first-use steps are in the cited documentation. Reproduction of this workflow remains unverified. [Source](https://github.com/JerrIsTheBesta/AI-Short-Drama-Studio/blob/main/README.md)
- **Maintenance and support · documented:** Published tag v0.1.37 and current documentation were reviewed. A version-specific independent end-to-end test remains open. [Source](https://github.com/JerrIsTheBesta/AI-Short-Drama-Studio/releases/tag/v0.1.37)
- **Independent use · unknown:** Independent first-hand use of the exact workflow was not established in this source review.
- **Models, services and costs · documented:** MIT covers project code. Generative image, motion, language or voice providers and their artifacts retain their own rights and access terms. Local rendering and compute apply. Connected APIs can charge separately and may require authorized credentials. [Source](https://github.com/JerrIsTheBesta/AI-Short-Drama-Studio/blob/main/README.md)

Source and documentation review. No hands-on execution by AI Media Scout. Published Windows package signing is not established. Workflow fidelity depends on the chosen model and final export. Use a small reversible test first.

### How it uses AI

The canvas connects language, vision, image, video and speech models to editable script and scene nodes for short-form production. [Source](https://github.com/JerrIsTheBesta/AI-Short-Drama-Studio/blob/main/README.md)

### Introduction

The canvas connects language, vision, image, video and speech models to editable script and scene nodes for short-form production. [Source 1](https://github.com/JerrIsTheBesta/AI-Short-Drama-Studio/blob/main/README.md)

### What it is good for

Develop one scene from a script and a character reference, then replace a single generated asset without discarding the whole draft. [Source 1](https://github.com/JerrIsTheBesta/AI-Short-Drama-Studio/blob/main/README.md)

### Demo & examples

The source shows a canvas and genre-oriented scene generation. Model and provider choice changes the possible results and limits. [Source 1](https://github.com/JerrIsTheBesta/AI-Short-Drama-Studio/blob/main/README.md)

### Install

Follow the documented route for the scoped workflow. The steps below are source references. [Source 1](https://github.com/JerrIsTheBesta/AI-Short-Drama-Studio/blob/main/README.md)

1. Use the published Windows installer or follow the project’s documented Windows or macOS Electron source build path.
2. Open a test project and configure a supported provider or local ComfyUI endpoint for the chosen creative step. Verify that route before committing input assets.
### First project

A small first project makes the input, model output and handoff easy to inspect. [Source 1](https://github.com/JerrIsTheBesta/AI-Short-Drama-Studio/blob/main/README.md)

1. Add one scene and an approved reference image. Generate a short storyboard or frame sequence.
2. Check continuity and use the editable nodes to replace only the weakest asset. Save the original prompts and assets for comparison.
### Hardware & software

Platform and compute constraints refer to the selected route. [Source 1](https://github.com/JerrIsTheBesta/AI-Short-Drama-Studio/blob/main/README.md)

- **Hardware:** Minimum RAM, VRAM and disk space for the scoped workflow are undocumented.
- **Software:** Windows 10/11 published desktop route; documented Electron build for macOS. The model, service and local ComfyUI configuration are separate.
- **Platforms:** Windows distribution and a macOS source path documented. Equivalent native Linux setup remains unverified.

### License, model weights & costs

The full software license was reviewed. Dependencies and creative assets carry their own terms. [Source 1](https://github.com/JerrIsTheBesta/AI-Short-Drama-Studio/blob/main/LICENSE) [Source 2](https://github.com/JerrIsTheBesta/AI-Short-Drama-Studio/blob/main/README.md)

- **Code:** MIT
- **Weights:** MIT covers project code. Generative image, motion, language or voice providers and their artifacts retain their own rights and access terms.
- **Commercial:** Project code is governed by MIT. Confirm selected model, source-media and output restrictions separately.
- **Cost:** Local rendering and compute apply. Connected APIs can charge separately and may require authorized credentials.

### Why it merits attention

The creative workflow is grounded in the cited documentation. Output quality and compatibility are not hands-on verified. [Source 1](https://github.com/JerrIsTheBesta/AI-Short-Drama-Studio/blob/main/README.md)

### Limitations

Published Windows package signing is not established. Workflow fidelity depends on the chosen model and final export. Use a small reversible test first. [Source 1](https://github.com/JerrIsTheBesta/AI-Short-Drama-Studio/blob/main/README.md)

### Get the tool

- [Repository](https://github.com/JerrIsTheBesta/AI-Short-Drama-Studio)
- [Documentation](https://github.com/JerrIsTheBesta/AI-Short-Drama-Studio/blob/main/README.md)

## PolyForge

3D printing & generative CAD · 3D, reconstruction & assets · AI-assisted textile and computational craft

This completes an earlier pending guide with a current source review.

### Quality assessment: Quality unverified

Creative use and the code grant are documented. Check-level gaps remain before a recommendation.

Scope: Draft a simple dimensioned enclosure or non-load-bearing prop, inspect the generated geometry and retain the editable source for revision.

Evidence checked: 2026-11-21. No local execution implied.

- **Open-source software license · verified:** Reviewed the complete project software grant and its redistribution conditions. Model, data and service terms are scoped separately. [Source](https://github.com/rx290/polyforge/blob/main/LICENSE)
- **Creative results · documented:** The documentation shows a local model option alongside rule-based and photogrammetry paths. It lists parametric backend differences and validation steps. [Source](https://github.com/rx290/polyforge/blob/main/README.md)
- **Reproducible setup · documented:** The installation and first-use steps are in the cited documentation. Reproduction of this workflow remains unverified. [Source](https://github.com/rx290/polyforge/blob/main/README.md)
- **Maintenance and support · unknown:** The reviewed sources do not establish workflow-specific support, fixes and unresolved blockers.
- **Independent use · unknown:** Independent first-hand use of the exact workflow was not established in this source review.
- **Models, services and costs · documented:** MIT covers PolyForge. Model weights, open CAD hosts and source asset rights remain separate. The scoped model and CAD work can run locally. Model downloads, preview rendering and optional hosted execution need their own resources. [Source](https://github.com/rx290/polyforge/blob/main/README.md)

Source and documentation review. No hands-on execution by AI Media Scout. The learnable route is limited by the shape templates and constraints. A successful geometry export is not fabrication certification.

### How it uses AI

The optional local language-model route interprets a text description and fills constrained shape templates. The resulting geometry can be passed to documented CAD backends for further editing. [Source](https://github.com/rx290/polyforge/blob/main/README.md)

### Introduction

The optional local language-model route interprets a text description and fills constrained shape templates. The resulting geometry can be passed to documented CAD backends for further editing. [Source 1](https://github.com/rx290/polyforge/blob/main/README.md)

### What it is good for

Draft a simple dimensioned enclosure or non-load-bearing prop, inspect the generated geometry and retain the editable source for revision. [Source 1](https://github.com/rx290/polyforge/blob/main/README.md)

### Demo & examples

The documentation shows a local model option alongside rule-based and photogrammetry paths. It lists parametric backend differences and validation steps. [Source 1](https://github.com/rx290/polyforge/blob/main/README.md)

### Install

Follow the documented route for the scoped workflow. The steps below are source references. [Source 1](https://github.com/rx290/polyforge/blob/main/README.md)

1. Use a source-documented Linux or Windows installer, or the manual Python environment. Install the selected CAD backend separately.
2. Configure a supported local model through Ollama only for the language-assisted route. Inspect the supported templates before preparing a request.

```sh
pip install -e .
```

### First project

A small first project makes the input, model output and handoff easy to inspect. [Source 1](https://github.com/rx290/polyforge/blob/main/README.md)

1. Start with a basic object and supply exact measurements. Compare the interpreted parameters with what you intended.
2. Generate a preview and inspect scale, mesh topology and part names. Export to an editable format provided by the chosen backend.
3. Evaluate real manufacturing limits separately before a print or cut.
### Hardware & software

Platform and compute constraints refer to the selected route. [Source 1](https://github.com/rx290/polyforge/blob/main/README.md)

- **Hardware:** Minimum RAM, VRAM and disk space for the scoped workflow are undocumented.
- **Software:** Python environment and selected OpenSCAD, FreeCAD or Blender route. Optional local language model for the scoped workflow. Photogrammetry has separate COLMAP/OpenMVS requirements.
- **Platforms:** The current README describes Linux and Windows installation scripts and separate OS notes for individual backends. Full Mac, driver and device parity is unverified.

### License, model weights & costs

The full software license was reviewed. Dependencies and creative assets carry their own terms. [Source 1](https://github.com/rx290/polyforge/blob/main/LICENSE) [Source 2](https://github.com/rx290/polyforge/blob/main/README.md)

- **Code:** MIT
- **Weights:** MIT covers PolyForge. Model weights, open CAD hosts and source asset rights remain separate.
- **Commercial:** Project code is governed by MIT. Confirm selected model, source-media and output restrictions separately.
- **Cost:** The scoped model and CAD work can run locally. Model downloads, preview rendering and optional hosted execution need their own resources.

### Why it merits attention

The creative workflow is grounded in the cited documentation. Output quality and compatibility are not hands-on verified. [Source 1](https://github.com/rx290/polyforge/blob/main/README.md)

### Limitations

The learnable route is limited by the shape templates and constraints. A successful geometry export is not fabrication certification. [Source 1](https://github.com/rx290/polyforge/blob/main/README.md)

### Get the tool

- [Repository](https://github.com/rx290/polyforge)
- [Documentation](https://github.com/rx290/polyforge/blob/main/README.md)

## Creator Toolset

Editing, captions & post-production · Video, animation & film · AI agents for code-authored media production

This completes an earlier pending guide with a current source review.

### Quality assessment: Quality unverified

Creative use and the code grant are documented. Check-level gaps remain before a recommendation.

Scope: Capture a short Mac screencast or import a clip, prepare an editable caption draft, and share a reviewed proof.

Evidence checked: 2026-11-21. No local execution implied.

- **Open-source software license · verified:** Reviewed the complete project software grant and its redistribution conditions. Model, data and service terms are scoped separately. [Source](https://github.com/andripeetso/creatortoolset/blob/main/LICENSE)
- **Creative results · documented:** Current source shows the captioning and review interfaces with routes for separate creator tools. Model results and a particular share destination remain unverified. [Source](https://github.com/andripeetso/creatortoolset/blob/main/README.md) [Source](https://creatortoolset.com/docs/storage)
- **Reproducible setup · documented:** The installation and first-use steps are in the cited documentation. Reproduction of this workflow remains unverified. [Source](https://github.com/andripeetso/creatortoolset/blob/main/README.md) [Source](https://creatortoolset.com/docs/storage)
- **Maintenance and support · unknown:** The reviewed sources do not establish workflow-specific support, fixes and unresolved blockers.
- **Independent use · unknown:** Independent first-hand use of the exact workflow was not established in this source review.
- **Models, services and costs · documented:** MIT covers project code. Choice of model, app host, generated content and source media need separate terms review. Self-host operation requires compute/storage. Provider or subscription access can apply when using external AI. [Source](https://github.com/andripeetso/creatortoolset/blob/main/README.md) [Source](https://creatortoolset.com/docs/storage)

Source and documentation review. No hands-on execution by AI Media Scout. Agent and transcription roles are configured separately. Local storage, actual privacy flow and share controls vary with chosen backend.

### How it uses AI

Creator Toolset connects a selected model to a local video workflow for captions and proposed edits. The tool keeps the model connection separate from timeline operation and review links. [Source](https://github.com/andripeetso/creatortoolset/blob/main/README.md) [Source](https://creatortoolset.com/docs/storage)

### Introduction

Creator Toolset connects a selected model to a local video workflow for captions and proposed edits. The tool keeps the model connection separate from timeline operation and review links. [Source 1](https://github.com/andripeetso/creatortoolset/blob/main/README.md) [Source 2](https://creatortoolset.com/docs/storage)

### What it is good for

Capture a short Mac screencast or import a clip, prepare an editable caption draft, and share a reviewed proof. [Source 1](https://github.com/andripeetso/creatortoolset/blob/main/README.md) [Source 2](https://creatortoolset.com/docs/storage)

### Demo & examples

Current source shows the captioning and review interfaces with routes for separate creator tools. Model results and a particular share destination remain unverified. [Source 1](https://github.com/andripeetso/creatortoolset/blob/main/README.md) [Source 2](https://creatortoolset.com/docs/storage)

### Install

Follow the documented route for the scoped workflow. The steps below are source references. [Source 1](https://github.com/andripeetso/creatortoolset/blob/main/README.md) [Source 2](https://creatortoolset.com/docs/storage)

1. Use the matching documented self-hosted route or Mac recorder. Review the application setup and host prerequisites.
2. Choose an authorized local or remote model for captions/editing and check the media that the selected provider receives.
### First project

A small first project makes the input, model output and handoff easy to inspect. [Source 1](https://github.com/andripeetso/creatortoolset/blob/main/README.md) [Source 2](https://creatortoolset.com/docs/storage)

1. Record one small approved demo and review its captured source.
2. Generate editable caption cues, make a correction and preview the timing. Keep the video and edited transcript apart until the final proof.
3. If sharing, test the intended review permission and link workflow with a sample asset first.
### Hardware & software

Platform and compute constraints refer to the selected route. [Source 1](https://github.com/andripeetso/creatortoolset/blob/main/README.md) [Source 2](https://creatortoolset.com/docs/storage)

- **Hardware:** Minimum RAM, VRAM and disk space for the scoped workflow are undocumented.
- **Software:** Creator Toolset workspace and its source-documented services. Optional Mac recorder requires macOS 15+. The selected model determines local or network requirements.
- **Platforms:** Mac native recorder and self-host/browser routes documented. The documentation does not show an equivalent Windows or Android native client.

### License, model weights & costs

The full software license was reviewed. Dependencies and creative assets carry their own terms. [Source 1](https://github.com/andripeetso/creatortoolset/blob/main/LICENSE) [Source 2](https://github.com/andripeetso/creatortoolset/blob/main/README.md) [Source 3](https://creatortoolset.com/docs/storage)

- **Code:** MIT
- **Weights:** MIT covers project code. Choice of model, app host, generated content and source media need separate terms review.
- **Commercial:** Project code is governed by MIT. Confirm selected model, source-media and output restrictions separately.
- **Cost:** Self-host operation requires compute/storage. Provider or subscription access can apply when using external AI.

### Why it merits attention

The creative workflow is grounded in the cited documentation. Output quality and compatibility are not hands-on verified. [Source 1](https://github.com/andripeetso/creatortoolset/blob/main/README.md) [Source 2](https://creatortoolset.com/docs/storage)

### Limitations

Agent and transcription roles are configured separately. Local storage, actual privacy flow and share controls vary with chosen backend. [Source 1](https://github.com/andripeetso/creatortoolset/blob/main/README.md) [Source 2](https://creatortoolset.com/docs/storage)

### Get the tool

- [Repository](https://github.com/andripeetso/creatortoolset)
- [Documentation](https://creatortoolset.com/docs/storage)

## LiveAudio

Live production accessibility and routed captions · Audio, music & voice · Accessible media & assistive creation

First complete guide in the library. The publication and documentation dates are not necessarily the project’s launch date.

### Quality assessment: Quality unverified

Creative use and the code grant are documented. Check-level gaps remain before a recommendation.

Scope: Add locally decoded speech captions to a live interview, lecture, or studio stream through a separate overlay.

Evidence checked: 2026-11-21. No local execution implied.

- **Open-source software license · verified:** Reviewed the complete project software grant and its redistribution conditions. Model, data and service terms are scoped separately. [Source](https://github.com/plynte-labs/LiveAudio/blob/master/LICENSE)
- **Creative results · documented:** The team publishes a current interface screenshot and labels an older live capture as the former Python version. The OBS instructions show the overlay URL. Timing and word errors on a mixed live track need review. [Source](https://github.com/plynte-labs/LiveAudio/blob/master/README.md) [Source](https://github.com/plynte-labs/LiveAudio/blob/master/THIRD_PARTY_NOTICES.md) [Source](https://liveaudio.opencohost.com/obs-setup/)
- **Reproducible setup · documented:** The installation and first-use steps are in the cited documentation. Reproduction of this workflow remains unverified. [Source](https://github.com/plynte-labs/LiveAudio/blob/master/README.md) [Source](https://github.com/plynte-labs/LiveAudio/blob/master/THIRD_PARTY_NOTICES.md) [Source](https://liveaudio.opencohost.com/obs-setup/)
- **Maintenance and support · documented:** The published 1.6.0 release documents a native stack and updater. Caption timing and workflow-specific support remain open checks. [Source](https://github.com/plynte-labs/LiveAudio/releases/tag/v1.6.0)
- **Independent use · unknown:** Independent first-hand use of the exact workflow was not established in this source review.
- **Models, services and costs · documented:** The project notices declare Apache-2.0 for onnx-community/whisper-base and MIT for the bundled Silero VAD. Other converted Whisper cards have different or unlisted terms. DirectML and optional NVIDIA libraries have separate terms. Local CPU transcription needs no service key or metered backend. Model download, local compute and optional GPU software remain separate. [Source](https://github.com/plynte-labs/LiveAudio/blob/master/README.md) [Source](https://github.com/plynte-labs/LiveAudio/blob/master/THIRD_PARTY_NOTICES.md) [Source](https://liveaudio.opencohost.com/obs-setup/)

Source and documentation review. No hands-on execution by AI Media Scout. Loopback overlay access and captions depend on the local audio route. The maintainer’s Windows benchmark describes one hardware setup. Live transcription still needs production-level review.

### How it uses AI

LiveAudio gates an audio source with Silero voice-activity detection, decodes speech with Whisper, then supplies live text to an OBS browser overlay. Version 1.6.0 documents a native Rust and ONNX Runtime path. [Source](https://github.com/plynte-labs/LiveAudio/blob/master/README.md) [Source](https://github.com/plynte-labs/LiveAudio/blob/master/THIRD_PARTY_NOTICES.md) [Source](https://liveaudio.opencohost.com/obs-setup/)

### Introduction

LiveAudio gates an audio source with Silero voice-activity detection, decodes speech with Whisper, then supplies live text to an OBS browser overlay. Version 1.6.0 documents a native Rust and ONNX Runtime path. [Source 1](https://github.com/plynte-labs/LiveAudio/blob/master/README.md) [Source 2](https://github.com/plynte-labs/LiveAudio/blob/master/THIRD_PARTY_NOTICES.md) [Source 3](https://liveaudio.opencohost.com/obs-setup/)

### What it is good for

Add locally decoded speech captions to a live interview, lecture, or studio stream through a separate overlay. [Source 1](https://github.com/plynte-labs/LiveAudio/blob/master/README.md) [Source 2](https://github.com/plynte-labs/LiveAudio/blob/master/THIRD_PARTY_NOTICES.md) [Source 3](https://liveaudio.opencohost.com/obs-setup/)

### Demo & examples

The team publishes a current interface screenshot and labels an older live capture as the former Python version. The OBS instructions show the overlay URL. Timing and word errors on a mixed live track need review. [Source 1](https://github.com/plynte-labs/LiveAudio/blob/master/README.md) [Source 2](https://github.com/plynte-labs/LiveAudio/blob/master/THIRD_PARTY_NOTICES.md) [Source 3](https://liveaudio.opencohost.com/obs-setup/)

### Install

Follow the documented route for the scoped workflow. The steps below are source references. [Source 1](https://github.com/plynte-labs/LiveAudio/blob/master/README.md) [Source 2](https://github.com/plynte-labs/LiveAudio/blob/master/THIRD_PARTY_NOTICES.md) [Source 3](https://liveaudio.opencohost.com/obs-setup/)

1. Get the v1.6.0 Windows installer or the Linux build from the release assets. The Windows portable CLI ZIP is a different distribution.
2. Start LiveAudio and let it retrieve the selected model. Choose the ONNX base variant for the initial documented workflow. Old Windows builds require a one-time manual upgrade to v1.6.0.
### First project

A small first project makes the input, model output and handoff easy to inspect. [Source 1](https://github.com/plynte-labs/LiveAudio/blob/master/README.md) [Source 2](https://github.com/plynte-labs/LiveAudio/blob/master/THIRD_PARTY_NOTICES.md) [Source 3](https://liveaudio.opencohost.com/obs-setup/)

1. Pick a microphone input and speak a short scripted passage before connecting OBS.
2. Add the local overlay URL from the app as an OBS Browser Source. Compare partial text and final text with the source recording.
3. Check delay and font size against the actual OBS composition. Rehearse with silence and overlapping speech before a broadcast.
### Hardware & software

Platform and compute constraints refer to the selected route. [Source 1](https://github.com/plynte-labs/LiveAudio/blob/master/README.md) [Source 2](https://github.com/plynte-labs/LiveAudio/blob/master/THIRD_PARTY_NOTICES.md) [Source 3](https://liveaudio.opencohost.com/obs-setup/)

- **Hardware:** The README lists 4 GB RAM minimum, 8 GB recommended, and 250 MB for the app plus 500 MB per model cache. CPU decoding is documented. For GPU use the table lists 2 GB VRAM for tiny/base and 4 GB or more for small/turbo.
- **Software:** Version 1.6.0 includes the native stack. It needs OBS for this overlay workflow and a first model download. DirectML is optional on supported Windows GPUs. The optional NVIDIA worker is separate.
- **Platforms:** Windows 10/11 x86_64 and Linux x86_64 are documented. WASAPI system loopback and the bundled updater are Windows features. macOS support is undocumented.

### License, model weights & costs

The full software license was reviewed. Dependencies and creative assets carry their own terms. [Source 1](https://github.com/plynte-labs/LiveAudio/blob/master/LICENSE) [Source 2](https://github.com/plynte-labs/LiveAudio/blob/master/README.md) [Source 3](https://github.com/plynte-labs/LiveAudio/blob/master/THIRD_PARTY_NOTICES.md) [Source 4](https://liveaudio.opencohost.com/obs-setup/)

- **Code:** MIT
- **Weights:** The project notices declare Apache-2.0 for onnx-community/whisper-base and MIT for the bundled Silero VAD. Other converted Whisper cards have different or unlisted terms. DirectML and optional NVIDIA libraries have separate terms.
- **Commercial:** Project code is governed by MIT. Confirm selected model, source-media and output restrictions separately.
- **Cost:** Local CPU transcription needs no service key or metered backend. Model download, local compute and optional GPU software remain separate.

### Why it merits attention

The creative workflow is grounded in the cited documentation. Output quality and compatibility are not hands-on verified. [Source 1](https://github.com/plynte-labs/LiveAudio/blob/master/README.md) [Source 2](https://github.com/plynte-labs/LiveAudio/blob/master/THIRD_PARTY_NOTICES.md) [Source 3](https://liveaudio.opencohost.com/obs-setup/)

### Limitations

Loopback overlay access and captions depend on the local audio route. The maintainer’s Windows benchmark describes one hardware setup. Live transcription still needs production-level review. [Source 1](https://github.com/plynte-labs/LiveAudio/blob/master/README.md) [Source 2](https://github.com/plynte-labs/LiveAudio/blob/master/THIRD_PARTY_NOTICES.md) [Source 3](https://liveaudio.opencohost.com/obs-setup/)

### Get the tool

- [Repository](https://github.com/plynte-labs/LiveAudio)
- [Documentation](https://liveaudio.opencohost.com/obs-setup/)

## LocalVocal

Live production accessibility and routed captions · Accessible media & assistive creation · Editing, captions & post-production

First complete guide in the library. The publication and documentation dates are not necessarily the project’s launch date.

### Quality assessment: Quality unverified

Creative use and the code grant are documented. Check-level gaps remain before a recommendation.

Scope: Add draft captions to a live OBS recording and retain subtitle text for a corrected accessibility release.

Evidence checked: 2026-11-21. No local execution implied.

- **Open-source software license · verified:** Reviewed the complete project software grant and its redistribution conditions. Model, data and service terms are scoped separately. [Source](https://github.com/royshil/obs-localvocal/blob/master/LICENSE)
- **Creative results · documented:** The OBS project resource and maintainer tutorial show a LocalVocal audio filter and text source. Their examples document configuration. Word accuracy and lag on a production mix still need assessment. [Source](https://github.com/royshil/obs-localvocal/blob/master/README.md) [Source](https://obsproject.com/forum/resources/localvocal-local-live-captions-translation-on-the-go.1769/) [Source](https://www.youtube.com/watch?v=5XqTMqpui3Q) [Source](https://github.com/royshil/obs-localvocal/issues/311)
- **Reproducible setup · documented:** The installation and first-use steps are in the cited documentation. Reproduction of this workflow remains unverified. [Source](https://github.com/royshil/obs-localvocal/blob/master/README.md) [Source](https://obsproject.com/forum/resources/localvocal-local-live-captions-translation-on-the-go.1769/) [Source](https://www.youtube.com/watch?v=5XqTMqpui3Q) [Source](https://github.com/royshil/obs-localvocal/issues/311)
- **Maintenance and support · documented:** Release 0.6.2 and its package matrix establish current published binaries. Scope-specific support reports need deeper review. [Source](https://github.com/royshil/obs-localvocal/releases/tag/0.6.2)
- **Independent use · unknown:** Independent first-hand use of the exact workflow was not established in this source review.
- **Models, services and costs · documented:** The archived project file contains GPLv2. Review the selected redistributable package and exact Whisper checkpoint terms separately. Optional external translation has separate terms. The local Whisper path requires local compute and initial downloads. A hosted provider is a separate workflow. [Source](https://github.com/royshil/obs-localvocal/blob/master/README.md) [Source](https://obsproject.com/forum/resources/localvocal-local-live-captions-translation-on-the-go.1769/) [Source](https://www.youtube.com/watch?v=5XqTMqpui3Q) [Source](https://github.com/royshil/obs-localvocal/issues/311)

Source and documentation review. No hands-on execution by AI Media Scout. Caption timing depends on the encoder load, speech model and audio route. A current support report describes instability in a separate Windows stream-embedded WebVTT output path. Rehearse the selected OBS setup before delivery.

### How it uses AI

The LocalVocal OBS filter uses Whisper through whisper.cpp to transcribe or translate a selected speech input while OBS runs. It supplies onscreen text and can save an editable subtitle file. [Source](https://github.com/royshil/obs-localvocal/blob/master/README.md) [Source](https://obsproject.com/forum/resources/localvocal-local-live-captions-translation-on-the-go.1769/) [Source](https://www.youtube.com/watch?v=5XqTMqpui3Q) [Source](https://github.com/royshil/obs-localvocal/issues/311)

### Introduction

The LocalVocal OBS filter uses Whisper through whisper.cpp to transcribe or translate a selected speech input while OBS runs. It supplies onscreen text and can save an editable subtitle file. [Source 1](https://github.com/royshil/obs-localvocal/blob/master/README.md) [Source 2](https://obsproject.com/forum/resources/localvocal-local-live-captions-translation-on-the-go.1769/) [Source 3](https://www.youtube.com/watch?v=5XqTMqpui3Q) [Source 4](https://github.com/royshil/obs-localvocal/issues/311)

### What it is good for

Add draft captions to a live OBS recording and retain subtitle text for a corrected accessibility release. [Source 1](https://github.com/royshil/obs-localvocal/blob/master/README.md) [Source 2](https://obsproject.com/forum/resources/localvocal-local-live-captions-translation-on-the-go.1769/) [Source 3](https://www.youtube.com/watch?v=5XqTMqpui3Q) [Source 4](https://github.com/royshil/obs-localvocal/issues/311)

### Demo & examples

The OBS project resource and maintainer tutorial show a LocalVocal audio filter and text source. Their examples document configuration. Word accuracy and lag on a production mix still need assessment. [Source 1](https://github.com/royshil/obs-localvocal/blob/master/README.md) [Source 2](https://obsproject.com/forum/resources/localvocal-local-live-captions-translation-on-the-go.1769/) [Source 3](https://www.youtube.com/watch?v=5XqTMqpui3Q) [Source 4](https://github.com/royshil/obs-localvocal/issues/311)

### Install

Follow the documented route for the scoped workflow. The steps below are source references. [Source 1](https://github.com/royshil/obs-localvocal/blob/master/README.md) [Source 2](https://obsproject.com/forum/resources/localvocal-local-live-captions-translation-on-the-go.1769/) [Source 3](https://www.youtube.com/watch?v=5XqTMqpui3Q) [Source 4](https://github.com/royshil/obs-localvocal/issues/311)

1. Select the matching 0.6.2 OBS plugin package. Windows needs the documented MSVC runtime. Mac packages are split between Intel and Apple silicon, with OS-specific variants.
2. Install the package into the matching OBS distribution and relaunch OBS. Use the generic build for an initial CPU test.
### First project

A small first project makes the input, model output and handoff easy to inspect. [Source 1](https://github.com/royshil/obs-localvocal/blob/master/README.md) [Source 2](https://obsproject.com/forum/resources/localvocal-local-live-captions-translation-on-the-go.1769/) [Source 3](https://www.youtube.com/watch?v=5XqTMqpui3Q) [Source 4](https://github.com/royshil/obs-localvocal/issues/311)

1. Add the LocalVocal filter to a speech audio source. Pick the language, model and text output.
2. Read a recorded sample and compare names and timestamps to the original before routing live output.
3. Save captions for correction if making a recorded deliverable. Check translation quality in the actual target language.
### Hardware & software

Platform and compute constraints refer to the selected route. [Source 1](https://github.com/royshil/obs-localvocal/blob/master/README.md) [Source 2](https://obsproject.com/forum/resources/localvocal-local-live-captions-translation-on-the-go.1769/) [Source 3](https://www.youtube.com/watch?v=5XqTMqpui3Q) [Source 4](https://github.com/royshil/obs-localvocal/issues/311)

- **Hardware:** Minimum RAM, VRAM and disk space for the scoped workflow are undocumented.
- **Software:** OBS Studio, the compatible LocalVocal build and selected Whisper model. Windows generic, dedicated NVIDIA and AMD bundles differ. Model options and optional translation routes use their own terms.
- **Platforms:** Windows 10/11 x64, Ubuntu 22.04 x64 packages and Intel/Apple silicon macOS packages are documented in the release matrix.

### License, model weights & costs

The full software license was reviewed. Dependencies and creative assets carry their own terms. [Source 1](https://github.com/royshil/obs-localvocal/blob/master/LICENSE) [Source 2](https://github.com/royshil/obs-localvocal/blob/master/README.md) [Source 3](https://obsproject.com/forum/resources/localvocal-local-live-captions-translation-on-the-go.1769/) [Source 4](https://www.youtube.com/watch?v=5XqTMqpui3Q) [Source 5](https://github.com/royshil/obs-localvocal/issues/311)

- **Code:** GPL-2.0
- **Weights:** The archived project file contains GPLv2. Review the selected redistributable package and exact Whisper checkpoint terms separately. Optional external translation has separate terms.
- **Commercial:** Project code is governed by GPL-2.0. Confirm selected model, source-media and output restrictions separately.
- **Cost:** The local Whisper path requires local compute and initial downloads. A hosted provider is a separate workflow.

### Why it merits attention

The creative workflow is grounded in the cited documentation. Output quality and compatibility are not hands-on verified. [Source 1](https://github.com/royshil/obs-localvocal/blob/master/README.md) [Source 2](https://obsproject.com/forum/resources/localvocal-local-live-captions-translation-on-the-go.1769/) [Source 3](https://www.youtube.com/watch?v=5XqTMqpui3Q) [Source 4](https://github.com/royshil/obs-localvocal/issues/311)

### Limitations

Caption timing depends on the encoder load, speech model and audio route. A current support report describes instability in a separate Windows stream-embedded WebVTT output path. Rehearse the selected OBS setup before delivery. [Source 1](https://github.com/royshil/obs-localvocal/blob/master/README.md) [Source 2](https://obsproject.com/forum/resources/localvocal-local-live-captions-translation-on-the-go.1769/) [Source 3](https://www.youtube.com/watch?v=5XqTMqpui3Q) [Source 4](https://github.com/royshil/obs-localvocal/issues/311)

### Get the tool

- [Repository](https://github.com/royshil/obs-localvocal)
- [Documentation](https://github.com/royshil/obs-localvocal/issues/311)

## CalibRaw

Photography, restoration & color · Learned optics and post-production lens tools · Images & design

First complete guide in the library. The publication and documentation dates are not necessarily the project’s launch date.

### Quality assessment: Quality unverified

Creative use and the code grant are documented. Check-level gaps remain before a recommendation.

Scope: Separate a portrait subject from the background for localized tone and color adjustment while keeping the RAW source and editable adjustments.

Evidence checked: 2026-11-21. No local execution implied.

- **Open-source software license · verified:** Reviewed the complete project software grant and its redistribution conditions. Model, data and service terms are scoped separately. [Source](https://github.com/Duecki1/CalibRaw/blob/main/COPYING)
- **Creative results · documented:** The README includes the editor interface and feature examples and names the actual model artifacts. These illustrate the controls. Edge quality on a set of portraits is open. [Source](https://github.com/Duecki1/CalibRaw/blob/main/README.md) [Source](https://calibraw.dueckis.de/android/) [Source](https://github.com/Duecki1/CalibRaw/blob/main/THIRD_PARTY_NOTICES.md) [Source](https://f-droid.org/en/packages/de.duecki.calibraw/) [Source](https://calibraw.dueckis.de)
- **Reproducible setup · documented:** The installation and first-use steps are in the cited documentation. Reproduction of this workflow remains unverified. [Source](https://github.com/Duecki1/CalibRaw/blob/main/README.md) [Source](https://calibraw.dueckis.de/android/) [Source](https://github.com/Duecki1/CalibRaw/blob/main/THIRD_PARTY_NOTICES.md) [Source](https://f-droid.org/en/packages/de.duecki.calibraw/) [Source](https://calibraw.dueckis.de)
- **Maintenance and support · documented:** Version 1.5.1 is published and supplies platform-specific artifacts. The scoped model and camera compatibility still need first-hand checks. [Source](https://github.com/Duecki1/CalibRaw/releases/tag/v1.5.1)
- **Independent use · unknown:** Independent first-hand use of the exact workflow was not established in this source review.
- **Models, services and costs · documented:** Code is GPL-3.0-or-later. The notices declare MIT for the BiRefNet ONNX subject model. Big-LaMa, SAM 2.1, depth and optional people-parts modes have distinct terms, including a custom Sapiens2 grant. The documented masking workflow processes on device after downloads. Compute and storage vary with RAW size and selected artifacts. [Source](https://github.com/Duecki1/CalibRaw/blob/main/README.md) [Source](https://calibraw.dueckis.de/android/) [Source](https://github.com/Duecki1/CalibRaw/blob/main/THIRD_PARTY_NOTICES.md) [Source](https://f-droid.org/en/packages/de.duecki.calibraw/) [Source](https://calibraw.dueckis.de)

Source and documentation review. No hands-on execution by AI Media Scout. Software fallback performance and a specific camera’s RAW compatibility need a local check. Model output on translucent or weakly separated edges may need manual refinement.

### How it uses AI

CalibRaw uses locally run models for foreground, object, sky and depth masks. A mask can restrict nondestructive development to a portrait subject or a specific part of a RAW exposure. [Source](https://github.com/Duecki1/CalibRaw/blob/main/README.md) [Source](https://calibraw.dueckis.de/android/) [Source](https://github.com/Duecki1/CalibRaw/blob/main/THIRD_PARTY_NOTICES.md) [Source](https://f-droid.org/en/packages/de.duecki.calibraw/) [Source](https://calibraw.dueckis.de)

### Introduction

CalibRaw uses locally run models for foreground, object, sky and depth masks. A mask can restrict nondestructive development to a portrait subject or a specific part of a RAW exposure. [Source 1](https://github.com/Duecki1/CalibRaw/blob/main/README.md) [Source 2](https://calibraw.dueckis.de/android/) [Source 3](https://github.com/Duecki1/CalibRaw/blob/main/THIRD_PARTY_NOTICES.md) [Source 4](https://f-droid.org/en/packages/de.duecki.calibraw/) [Source 5](https://calibraw.dueckis.de)

### What it is good for

Separate a portrait subject from the background for localized tone and color adjustment while keeping the RAW source and editable adjustments. [Source 1](https://github.com/Duecki1/CalibRaw/blob/main/README.md) [Source 2](https://calibraw.dueckis.de/android/) [Source 3](https://github.com/Duecki1/CalibRaw/blob/main/THIRD_PARTY_NOTICES.md) [Source 4](https://f-droid.org/en/packages/de.duecki.calibraw/) [Source 5](https://calibraw.dueckis.de)

### Demo & examples

The README includes the editor interface and feature examples and names the actual model artifacts. These illustrate the controls. Edge quality on a set of portraits is open. [Source 1](https://github.com/Duecki1/CalibRaw/blob/main/README.md) [Source 2](https://calibraw.dueckis.de/android/) [Source 3](https://github.com/Duecki1/CalibRaw/blob/main/THIRD_PARTY_NOTICES.md) [Source 4](https://f-droid.org/en/packages/de.duecki.calibraw/) [Source 5](https://calibraw.dueckis.de)

### Install

Follow the documented route for the scoped workflow. The steps below are source references. [Source 1](https://github.com/Duecki1/CalibRaw/blob/main/README.md) [Source 2](https://calibraw.dueckis.de/android/) [Source 3](https://github.com/Duecki1/CalibRaw/blob/main/THIRD_PARTY_NOTICES.md) [Source 4](https://f-droid.org/en/packages/de.duecki.calibraw/) [Source 5](https://calibraw.dueckis.de)

1. Choose a release build for your OS. Linux also has Flathub. Android has a separate F-Droid build. Confirm graphics and the app version before opening project files.
2. Open a supported RAW and consent to the exact foreground model and ONNX runtime download for this workflow.
### First project

A small first project makes the input, model output and handoff easy to inspect. [Source 1](https://github.com/Duecki1/CalibRaw/blob/main/README.md) [Source 2](https://calibraw.dueckis.de/android/) [Source 3](https://github.com/Duecki1/CalibRaw/blob/main/THIRD_PARTY_NOTICES.md) [Source 4](https://f-droid.org/en/packages/de.duecki.calibraw/) [Source 5](https://calibraw.dueckis.de)

1. Make a neutral development of one RAW file. Create a subject mask and inspect hair and semitransparent edges against the original.
2. Apply a small exposure or contrast change using the mask. Compare the masked adjustment on and off and export a proof.
### Hardware & software

Platform and compute constraints refer to the selected route. [Source 1](https://github.com/Duecki1/CalibRaw/blob/main/README.md) [Source 2](https://calibraw.dueckis.de/android/) [Source 3](https://github.com/Duecki1/CalibRaw/blob/main/THIRD_PARTY_NOTICES.md) [Source 4](https://f-droid.org/en/packages/de.duecki.calibraw/) [Source 5](https://calibraw.dueckis.de)

- **Hardware:** The Android guide specifies Android 8.0+, 64-bit ARM and Vulkan. Desktop backends are Vulkan on Linux, Direct3D 12 or Vulkan on Windows, and Metal on macOS. The project describes slower software fallback routes on some desktop systems. Minimum RAM, VRAM and total disk for this selected mask are undocumented.
- **Software:** CalibRaw v1.5.1, a LibRaw/Rawler-supported file, platform graphics backend and the consented ONNX subject-mask artifact.
- **Platforms:** Linux x86_64/ARM64, Windows x86_64/ARM64, Intel and Apple silicon macOS, and Android are documented. The captured F-Droid Android package is 1.4.0 and differs from the reviewed 1.5.1 upstream release. Check the exact OS and driver notes.

### License, model weights & costs

The full software license was reviewed. Dependencies and creative assets carry their own terms. [Source 1](https://github.com/Duecki1/CalibRaw/blob/main/COPYING) [Source 2](https://github.com/Duecki1/CalibRaw/blob/main/README.md) [Source 3](https://calibraw.dueckis.de/android/) [Source 4](https://github.com/Duecki1/CalibRaw/blob/main/THIRD_PARTY_NOTICES.md) [Source 5](https://f-droid.org/en/packages/de.duecki.calibraw/) [Source 6](https://calibraw.dueckis.de)

- **Code:** GPL-3.0-or-later
- **Weights:** Code is GPL-3.0-or-later. The notices declare MIT for the BiRefNet ONNX subject model. Big-LaMa, SAM 2.1, depth and optional people-parts modes have distinct terms, including a custom Sapiens2 grant.
- **Commercial:** Project code is governed by GPL-3.0-or-later. Confirm selected model, source-media and output restrictions separately.
- **Cost:** The documented masking workflow processes on device after downloads. Compute and storage vary with RAW size and selected artifacts.

### Why it merits attention

The creative workflow is grounded in the cited documentation. Output quality and compatibility are not hands-on verified. [Source 1](https://github.com/Duecki1/CalibRaw/blob/main/README.md) [Source 2](https://calibraw.dueckis.de/android/) [Source 3](https://github.com/Duecki1/CalibRaw/blob/main/THIRD_PARTY_NOTICES.md) [Source 4](https://f-droid.org/en/packages/de.duecki.calibraw/) [Source 5](https://calibraw.dueckis.de)

### Limitations

Software fallback performance and a specific camera’s RAW compatibility need a local check. Model output on translucent or weakly separated edges may need manual refinement. [Source 1](https://github.com/Duecki1/CalibRaw/blob/main/README.md) [Source 2](https://calibraw.dueckis.de/android/) [Source 3](https://github.com/Duecki1/CalibRaw/blob/main/THIRD_PARTY_NOTICES.md) [Source 4](https://f-droid.org/en/packages/de.duecki.calibraw/) [Source 5](https://calibraw.dueckis.de)

### Get the tool

- [Repository](https://github.com/Duecki1/CalibRaw)
- [Documentation](https://calibraw.dueckis.de)

## Caliscope

Learned optics and post-production lens tools · Photogrammetry, scanning & neural rendering · Motion capture & character animation

First complete guide in the library. The publication and documentation dates are not necessarily the project’s launch date.

### Quality assessment: Quality unverified

Creative use and the code grant are documented. Check-level gaps remain before a recommendation.

Scope: Check a multi-camera capture setup against a short movement test, review tracking and scale, then export triangulated landmarks for inspection.

Evidence checked: 2026-11-21. No local execution implied.

- **Open-source software license · verified:** Reviewed the complete project software grant and its redistribution conditions. Model, data and service terms are scoped separately. [Source](https://github.com/mprib/caliscope/blob/main/LICENSE)
- **Creative results · documented:** The official sample project includes downloadable data. The recorded interface demo uses version 0.9.0 and differs from the current UI. Inspect exact tracking results for the current release. [Source](https://github.com/mprib/caliscope/blob/main/README.md) [Source](https://mprib.github.io/caliscope/installation/) [Source](https://mprib.github.io/caliscope/sample_project/) [Source](https://mprib.github.io/caliscope/onnx_trackers/) [Source](https://mprib.github.io/caliscope/reconstruction/)
- **Reproducible setup · documented:** The installation and first-use steps are in the cited documentation. Reproduction of this workflow remains unverified. [Source](https://github.com/mprib/caliscope/blob/main/README.md) [Source](https://mprib.github.io/caliscope/installation/) [Source](https://mprib.github.io/caliscope/sample_project/) [Source](https://mprib.github.io/caliscope/onnx_trackers/) [Source](https://mprib.github.io/caliscope/reconstruction/)
- **Maintenance and support · documented:** The source shows v0.12.0 and current tracking documentation. Accuracy and support on a particular rig still need evidence. [Source](https://github.com/mprib/caliscope/releases/tag/v0.12.0)
- **Independent use · unknown:** Independent first-hand use of the exact workflow was not established in this source review.
- **Models, services and costs · documented:** The root BSD-2-Clause grant covers Caliscope code. The official tracker docs declare Apache-2.0 for the built-in RTMPose Halpe26 cards. The optional GeoCalib route uses separate weights. The documented reconstruction check runs locally on supplied footage. It requires capture hardware as well as the runtime. [Source](https://github.com/mprib/caliscope/blob/main/README.md) [Source](https://mprib.github.io/caliscope/installation/) [Source](https://mprib.github.io/caliscope/sample_project/) [Source](https://mprib.github.io/caliscope/onnx_trackers/) [Source](https://mprib.github.io/caliscope/reconstruction/)

Source and documentation review. No hands-on execution by AI Media Scout. The maintainer positions triangulation as a calibration check. Markerless camera positioning is explicitly experimental. This guide uses the standard board calibration path.

### How it uses AI

Caliscope can run ONNX pose models on rig footage and triangulate their landmarks in 3D to check calibration. The additional GeoCalib route estimates vertical orientation from image cues. [Source](https://github.com/mprib/caliscope/blob/main/README.md) [Source](https://mprib.github.io/caliscope/installation/) [Source](https://mprib.github.io/caliscope/sample_project/) [Source](https://mprib.github.io/caliscope/onnx_trackers/) [Source](https://mprib.github.io/caliscope/reconstruction/)

### Introduction

Caliscope can run ONNX pose models on rig footage and triangulate their landmarks in 3D to check calibration. The additional GeoCalib route estimates vertical orientation from image cues. [Source 1](https://github.com/mprib/caliscope/blob/main/README.md) [Source 2](https://mprib.github.io/caliscope/installation/) [Source 3](https://mprib.github.io/caliscope/sample_project/) [Source 4](https://mprib.github.io/caliscope/onnx_trackers/) [Source 5](https://mprib.github.io/caliscope/reconstruction/)

### What it is good for

Check a multi-camera capture setup against a short movement test, review tracking and scale, then export triangulated landmarks for inspection. [Source 1](https://github.com/mprib/caliscope/blob/main/README.md) [Source 2](https://mprib.github.io/caliscope/installation/) [Source 3](https://mprib.github.io/caliscope/sample_project/) [Source 4](https://mprib.github.io/caliscope/onnx_trackers/) [Source 5](https://mprib.github.io/caliscope/reconstruction/)

### Demo & examples

The official sample project includes downloadable data. The recorded interface demo uses version 0.9.0 and differs from the current UI. Inspect exact tracking results for the current release. [Source 1](https://github.com/mprib/caliscope/blob/main/README.md) [Source 2](https://mprib.github.io/caliscope/installation/) [Source 3](https://mprib.github.io/caliscope/sample_project/) [Source 4](https://mprib.github.io/caliscope/onnx_trackers/) [Source 5](https://mprib.github.io/caliscope/reconstruction/)

### Install

Follow the documented route for the scoped workflow. The steps below are source references. [Source 1](https://github.com/mprib/caliscope/blob/main/README.md) [Source 2](https://mprib.github.io/caliscope/installation/) [Source 3](https://mprib.github.io/caliscope/sample_project/) [Source 4](https://mprib.github.io/caliscope/onnx_trackers/) [Source 5](https://mprib.github.io/caliscope/reconstruction/)

1. Create an environment supported by the current installation guide and install the GUI extra.
2. Open the sample project before testing a custom synchronized camera set.

```sh
uv pip install "caliscope[gui]"
```


```sh
caliscope
```

### First project

A small first project makes the input, model output and handoff easy to inspect. [Source 1](https://github.com/mprib/caliscope/blob/main/README.md) [Source 2](https://mprib.github.io/caliscope/installation/) [Source 3](https://mprib.github.io/caliscope/sample_project/) [Source 4](https://mprib.github.io/caliscope/onnx_trackers/) [Source 5](https://mprib.github.io/caliscope/reconstruction/)

1. Calibrate lenses and camera poses with the documented board views. Review overlap and scale for bad views first.
2. Run the tracking and triangulation check against a short movement. Inspect reprojection and occlusions, then export CSV or TRC for inspection.
### Hardware & software

Platform and compute constraints refer to the selected route. [Source 1](https://github.com/mprib/caliscope/blob/main/README.md) [Source 2](https://mprib.github.io/caliscope/installation/) [Source 3](https://mprib.github.io/caliscope/sample_project/) [Source 4](https://mprib.github.io/caliscope/onnx_trackers/) [Source 5](https://mprib.github.io/caliscope/reconstruction/)

- **Hardware:** Minimum RAM, VRAM and disk space for the scoped workflow are undocumented.
- **Software:** Caliscope v0.12.0 and Python 3.11–3.14 from its pyproject, with the GUI/tracking extras. The optional vertical estimate downloads GeoCalib ONNX weights.
- **Platforms:** Current development instructions cover Windows, macOS and Linux, including a Debian/Ubuntu GUI library prerequisite. The docs warn that PyPI and development installation extras can differ.

### License, model weights & costs

The full software license was reviewed. Dependencies and creative assets carry their own terms. [Source 1](https://github.com/mprib/caliscope/blob/main/LICENSE) [Source 2](https://github.com/mprib/caliscope/blob/main/README.md) [Source 3](https://mprib.github.io/caliscope/installation/) [Source 4](https://mprib.github.io/caliscope/sample_project/) [Source 5](https://mprib.github.io/caliscope/onnx_trackers/) [Source 6](https://mprib.github.io/caliscope/reconstruction/)

- **Code:** BSD-2-Clause
- **Weights:** The root BSD-2-Clause grant covers Caliscope code. The official tracker docs declare Apache-2.0 for the built-in RTMPose Halpe26 cards. The optional GeoCalib route uses separate weights.
- **Commercial:** Project code is governed by BSD-2-Clause. Confirm selected model, source-media and output restrictions separately.
- **Cost:** The documented reconstruction check runs locally on supplied footage. It requires capture hardware as well as the runtime.

### Why it merits attention

The creative workflow is grounded in the cited documentation. Output quality and compatibility are not hands-on verified. [Source 1](https://github.com/mprib/caliscope/blob/main/README.md) [Source 2](https://mprib.github.io/caliscope/installation/) [Source 3](https://mprib.github.io/caliscope/sample_project/) [Source 4](https://mprib.github.io/caliscope/onnx_trackers/) [Source 5](https://mprib.github.io/caliscope/reconstruction/)

### Limitations

The maintainer positions triangulation as a calibration check. Markerless camera positioning is explicitly experimental. This guide uses the standard board calibration path. [Source 1](https://github.com/mprib/caliscope/blob/main/README.md) [Source 2](https://mprib.github.io/caliscope/installation/) [Source 3](https://mprib.github.io/caliscope/sample_project/) [Source 4](https://mprib.github.io/caliscope/onnx_trackers/) [Source 5](https://mprib.github.io/caliscope/reconstruction/)

### Get the tool

- [Repository](https://github.com/mprib/caliscope)
- [Documentation](https://mprib.github.io/caliscope/reconstruction/)

## eScriptorium

Cultural heritage layout recognition and transcription · Archives, media restoration & collections · Creative publishing & presentation

First complete guide in the library. The publication and documentation dates are not necessarily the project’s launch date.

### Quality assessment: Quality unverified

Creative use and the code grant are documented. Check-level gaps remain before a recommendation.

Scope: Create a reviewed structured transcription for a small digital exhibition or scholarly edition from IIIF scans.

Evidence checked: 2026-11-21. No local execution implied.

- **Open-source software license · verified:** Reviewed the complete project software grant and its redistribution conditions. Model, data and service terms are scoped separately. [Source](https://gitlab.com/scripta/escriptorium/-/raw/develop/LICENSE)
- **Creative results · documented:** The DAHN publication pipeline documents first-hand use of Kraken and eScriptorium for historical transcription and a subsequent TEI encoding stage. That documented project used earlier versions. [Source](https://gitlab.com/api/v4/projects/scripta%2Fescriptorium/repository/files/README.md/raw?ref=develop) [Source](https://gitlab.com/api/v4/projects/scripta%2Fescriptorium/releases?per_page=5) [Source](https://journals.openedition.org/jtei/5306) [Source](https://zenodo.org/records/22879549) [Source](https://escriptorium.eu/getting_started/) [Source](https://escriptorium-tutorial.readthedocs.io/en/latest/export/)
- **Reproducible setup · documented:** The installation and first-use steps are in the cited documentation. Reproduction of this workflow remains unverified. [Source](https://gitlab.com/api/v4/projects/scripta%2Fescriptorium/repository/files/README.md/raw?ref=develop) [Source](https://gitlab.com/api/v4/projects/scripta%2Fescriptorium/releases?per_page=5) [Source](https://journals.openedition.org/jtei/5306) [Source](https://zenodo.org/records/22879549) [Source](https://escriptorium.eu/getting_started/) [Source](https://escriptorium-tutorial.readthedocs.io/en/latest/export/)
- **Maintenance and support · documented:** The canonical GitLab API lists v26.10 and v26.07 releases. The scope and open issues of the tested institution-specific deployment remain to be assessed. [Source](https://gitlab.com/scripta/escriptorium/-/releases/v26.10)
- **Independent use · verified:** The DAHN team describes producing transcriptions with eScriptorium for its scholarly edition. This is workflow-level first-hand evidence from earlier versions. [Source](https://journals.openedition.org/jtei/5306)
- **Models, services and costs · documented:** The complete MIT code license was archived. The cited Kraken general segmentation v2 record declares Apache-2.0. The chosen recognition checkpoint and ground-truth collection retain their own terms. Self-hosting requires storage and compute. Existing instances may require institutional permission. Optional training capacity is separate. [Source](https://gitlab.com/api/v4/projects/scripta%2Fescriptorium/repository/files/README.md/raw?ref=develop) [Source](https://gitlab.com/api/v4/projects/scripta%2Fescriptorium/releases?per_page=5) [Source](https://journals.openedition.org/jtei/5306) [Source](https://zenodo.org/records/22879549) [Source](https://escriptorium.eu/getting_started/) [Source](https://escriptorium-tutorial.readthedocs.io/en/latest/export/)

Source and documentation review. No hands-on execution by AI Media Scout. Layout order and accuracy depend on the collection and chosen model. Preserve corrected export and scan links. Evidence from earlier research does not establish v26.10 accuracy for new handwriting.

### How it uses AI

Kraken text recognition and layout models suggest regions, lines and text from scanned manuscripts and printed sources. eScriptorium lets editors correct both spatial segmentation and the transcript. [Source](https://gitlab.com/api/v4/projects/scripta%2Fescriptorium/repository/files/README.md/raw?ref=develop) [Source](https://gitlab.com/api/v4/projects/scripta%2Fescriptorium/releases?per_page=5) [Source](https://journals.openedition.org/jtei/5306) [Source](https://zenodo.org/records/22879549) [Source](https://escriptorium.eu/getting_started/) [Source](https://escriptorium-tutorial.readthedocs.io/en/latest/export/)

### Introduction

Kraken text recognition and layout models suggest regions, lines and text from scanned manuscripts and printed sources. eScriptorium lets editors correct both spatial segmentation and the transcript. [Source 1](https://gitlab.com/api/v4/projects/scripta%2Fescriptorium/repository/files/README.md/raw?ref=develop) [Source 2](https://gitlab.com/api/v4/projects/scripta%2Fescriptorium/releases?per_page=5) [Source 3](https://journals.openedition.org/jtei/5306) [Source 4](https://zenodo.org/records/22879549) [Source 5](https://escriptorium.eu/getting_started/) [Source 6](https://escriptorium-tutorial.readthedocs.io/en/latest/export/)

### What it is good for

Create a reviewed structured transcription for a small digital exhibition or scholarly edition from IIIF scans. [Source 1](https://gitlab.com/api/v4/projects/scripta%2Fescriptorium/repository/files/README.md/raw?ref=develop) [Source 2](https://gitlab.com/api/v4/projects/scripta%2Fescriptorium/releases?per_page=5) [Source 3](https://journals.openedition.org/jtei/5306) [Source 4](https://zenodo.org/records/22879549) [Source 5](https://escriptorium.eu/getting_started/) [Source 6](https://escriptorium-tutorial.readthedocs.io/en/latest/export/)

### Demo & examples

The DAHN publication pipeline documents first-hand use of Kraken and eScriptorium for historical transcription and a subsequent TEI encoding stage. That documented project used earlier versions. [Source 1](https://gitlab.com/api/v4/projects/scripta%2Fescriptorium/repository/files/README.md/raw?ref=develop) [Source 2](https://gitlab.com/api/v4/projects/scripta%2Fescriptorium/releases?per_page=5) [Source 3](https://journals.openedition.org/jtei/5306) [Source 4](https://zenodo.org/records/22879549) [Source 5](https://escriptorium.eu/getting_started/) [Source 6](https://escriptorium-tutorial.readthedocs.io/en/latest/export/)

### Install

Follow the documented route for the scoped workflow. The steps below are source references. [Source 1](https://gitlab.com/api/v4/projects/scripta%2Fescriptorium/repository/files/README.md/raw?ref=develop) [Source 2](https://gitlab.com/api/v4/projects/scripta%2Fescriptorium/releases?per_page=5) [Source 3](https://journals.openedition.org/jtei/5306) [Source 4](https://zenodo.org/records/22879549) [Source 5](https://escriptorium.eu/getting_started/) [Source 6](https://escriptorium-tutorial.readthedocs.io/en/latest/export/)

1. Use an available institutional instance or follow the official Docker self-hosting instructions. Confirm hosting access, model availability and rights to the document images.
2. For self-hosting, follow the configuration and worker guidance for the release. Confirm the active service before importing data.
### First project

A small first project makes the input, model output and handoff easy to inspect. [Source 1](https://gitlab.com/api/v4/projects/scripta%2Fescriptorium/repository/files/README.md/raw?ref=develop) [Source 2](https://gitlab.com/api/v4/projects/scripta%2Fescriptorium/releases?per_page=5) [Source 3](https://journals.openedition.org/jtei/5306) [Source 4](https://zenodo.org/records/22879549) [Source 5](https://escriptorium.eu/getting_started/) [Source 6](https://escriptorium-tutorial.readthedocs.io/en/latest/export/)

1. Create a document with the correct reading direction and import a small IIIF manifest or a few scanned images.
2. Choose layout and text weights for your script. The cited Kraken general segmentation release provides one layout starting point. It needs a separate recognition model. Check suggested page regions and correct text against the scan.
3. Export the selected transcription and page-layout information as PAGE or ALTO XML. Evaluate any later TEI conversion separately.
### Hardware & software

Platform and compute constraints refer to the selected route. [Source 1](https://gitlab.com/api/v4/projects/scripta%2Fescriptorium/repository/files/README.md/raw?ref=develop) [Source 2](https://gitlab.com/api/v4/projects/scripta%2Fescriptorium/releases?per_page=5) [Source 3](https://journals.openedition.org/jtei/5306) [Source 4](https://zenodo.org/records/22879549) [Source 5](https://escriptorium.eu/getting_started/) [Source 6](https://escriptorium-tutorial.readthedocs.io/en/latest/export/)

- **Hardware:** The official self-hosting guide gives 8 GB minimum RAM and 16 GB or more recommended for training. An NVIDIA GPU is optional and useful for training. VRAM and total storage requirements remain workload-dependent.
- **Software:** eScriptorium v26.10, browser, Docker for self-hosting, and selected Kraken models. The instance may need specific worker configuration.
- **Platforms:** The current getting-started page lists Linux and macOS for self-hosting. The official project presentation also documents a Windows WSL route. A hosted instance is accessed in a browser.

### License, model weights & costs

The full software license was reviewed. Dependencies and creative assets carry their own terms. [Source 1](https://gitlab.com/scripta/escriptorium/-/raw/develop/LICENSE) [Source 2](https://gitlab.com/api/v4/projects/scripta%2Fescriptorium/repository/files/README.md/raw?ref=develop) [Source 3](https://gitlab.com/api/v4/projects/scripta%2Fescriptorium/releases?per_page=5) [Source 4](https://journals.openedition.org/jtei/5306) [Source 5](https://zenodo.org/records/22879549) [Source 6](https://escriptorium.eu/getting_started/) [Source 7](https://escriptorium-tutorial.readthedocs.io/en/latest/export/)

- **Code:** MIT
- **Weights:** The complete MIT code license was archived. The cited Kraken general segmentation v2 record declares Apache-2.0. The chosen recognition checkpoint and ground-truth collection retain their own terms.
- **Commercial:** Project code is governed by MIT. Confirm selected model, source-media and output restrictions separately.
- **Cost:** Self-hosting requires storage and compute. Existing instances may require institutional permission. Optional training capacity is separate.

### Why it merits attention

The creative workflow is grounded in the cited documentation. Output quality and compatibility are not hands-on verified. [Source 1](https://gitlab.com/api/v4/projects/scripta%2Fescriptorium/repository/files/README.md/raw?ref=develop) [Source 2](https://gitlab.com/api/v4/projects/scripta%2Fescriptorium/releases?per_page=5) [Source 3](https://journals.openedition.org/jtei/5306) [Source 4](https://zenodo.org/records/22879549) [Source 5](https://escriptorium.eu/getting_started/) [Source 6](https://escriptorium-tutorial.readthedocs.io/en/latest/export/)

### Limitations

Layout order and accuracy depend on the collection and chosen model. Preserve corrected export and scan links. Evidence from earlier research does not establish v26.10 accuracy for new handwriting. [Source 1](https://gitlab.com/api/v4/projects/scripta%2Fescriptorium/repository/files/README.md/raw?ref=develop) [Source 2](https://gitlab.com/api/v4/projects/scripta%2Fescriptorium/releases?per_page=5) [Source 3](https://journals.openedition.org/jtei/5306) [Source 4](https://zenodo.org/records/22879549) [Source 5](https://escriptorium.eu/getting_started/) [Source 6](https://escriptorium-tutorial.readthedocs.io/en/latest/export/)

### Get the tool

- [Repository](https://gitlab.com/scripta/escriptorium)
- [Documentation](https://escriptorium-tutorial.readthedocs.io/en/latest/export/)

## Arkindex Community Edition

Cultural heritage layout recognition and transcription · AI museum experiences and participatory exhibition media · Archives, media restoration & collections

First complete guide in the library. The publication and documentation dates are not necessarily the project’s launch date.

### Quality assessment: Quality unverified

Creative use and the code grant are documented. Check-level gaps remain before a recommendation.

Scope: Stage a small cultural archive collection for page-level annotation, recognition and structured export under the Community Edition.

Evidence checked: 2026-11-21. No local execution implied.

- **Open-source software license · verified:** Reviewed the complete project software grant and its redistribution conditions. Model, data and service terms are scoped separately. [Source](https://gitlab.teklia.com/api/v4/projects/arkindex%2Fbackend/repository/files/LICENSE/raw?ref=develop)
- **Creative results · documented:** Teklia’s tutorial walks through importing a gallica IIIF manifest and running recognition on printed French text. The docs separately describe training and exporting model predictions. Independent current evaluation remains open. [Source](https://doc.teklia.com/arkindex/) [Source](https://doc.teklia.com/arkindex/overview/license/) [Source](https://doc.teklia.com/arkindex/deployment/) [Source](https://doc.teklia.com/arkindex/deployment/hardware/) [Source](https://doc.teklia.com/arkindex_tutorial/export/) [Source](https://www.teklia.com/arkindex-tutorial)
- **Reproducible setup · documented:** The installation and first-use steps are in the cited documentation. Reproduction of this workflow remains unverified. [Source](https://doc.teklia.com/arkindex/) [Source](https://doc.teklia.com/arkindex/overview/license/) [Source](https://doc.teklia.com/arkindex/deployment/) [Source](https://doc.teklia.com/arkindex/deployment/hardware/) [Source](https://doc.teklia.com/arkindex_tutorial/export/) [Source](https://www.teklia.com/arkindex-tutorial)
- **Maintenance and support · documented:** The canonical API lists release 1.13.2 and predecessor maintenance releases. Issue review for the selected worker and deployment remains open. [Source](https://gitlab.teklia.com/arkindex/backend/-/releases/1.13.2)
- **Independent use · unknown:** Independent first-hand use of the exact workflow was not established in this source review.
- **Models, services and costs · documented:** The complete Community Edition AGPLv3 license was archived. Commercial enterprise licensing is separate. Workers, recognition models, source images and outputs require individual terms review. Community code can be self-hosted. The Linux server, storage and processing workers require capacity. Hosted and enterprise services have separate terms. [Source](https://doc.teklia.com/arkindex/) [Source](https://doc.teklia.com/arkindex/overview/license/) [Source](https://doc.teklia.com/arkindex/deployment/) [Source](https://doc.teklia.com/arkindex/deployment/hardware/) [Source](https://doc.teklia.com/arkindex_tutorial/export/) [Source](https://www.teklia.com/arkindex-tutorial)

Source and documentation review. No hands-on execution by AI Media Scout. This is a multi-service deployment. Recognition quality on a new collection and its PAGE layout handoff need source comparison and editor review.

### How it uses AI

Arkindex orchestrates document layout, OCR and handwriting recognition workers on IIIF images and records predictions against the source pages. [Source](https://doc.teklia.com/arkindex/) [Source](https://doc.teklia.com/arkindex/overview/license/) [Source](https://doc.teklia.com/arkindex/deployment/) [Source](https://doc.teklia.com/arkindex/deployment/hardware/) [Source](https://doc.teklia.com/arkindex_tutorial/export/) [Source](https://www.teklia.com/arkindex-tutorial)

### Introduction

Arkindex orchestrates document layout, OCR and handwriting recognition workers on IIIF images and records predictions against the source pages. [Source 1](https://doc.teklia.com/arkindex/) [Source 2](https://doc.teklia.com/arkindex/overview/license/) [Source 3](https://doc.teklia.com/arkindex/deployment/) [Source 4](https://doc.teklia.com/arkindex/deployment/hardware/) [Source 5](https://doc.teklia.com/arkindex_tutorial/export/) [Source 6](https://www.teklia.com/arkindex-tutorial)

### What it is good for

Stage a small cultural archive collection for page-level annotation, recognition and structured export under the Community Edition. [Source 1](https://doc.teklia.com/arkindex/) [Source 2](https://doc.teklia.com/arkindex/overview/license/) [Source 3](https://doc.teklia.com/arkindex/deployment/) [Source 4](https://doc.teklia.com/arkindex/deployment/hardware/) [Source 5](https://doc.teklia.com/arkindex_tutorial/export/) [Source 6](https://www.teklia.com/arkindex-tutorial)

### Demo & examples

Teklia’s tutorial walks through importing a gallica IIIF manifest and running recognition on printed French text. The docs separately describe training and exporting model predictions. Independent current evaluation remains open. [Source 1](https://doc.teklia.com/arkindex/) [Source 2](https://doc.teklia.com/arkindex/overview/license/) [Source 3](https://doc.teklia.com/arkindex/deployment/) [Source 4](https://doc.teklia.com/arkindex/deployment/hardware/) [Source 5](https://doc.teklia.com/arkindex_tutorial/export/) [Source 6](https://www.teklia.com/arkindex-tutorial)

### Install

Follow the documented route for the scoped workflow. The steps below are source references. [Source 1](https://doc.teklia.com/arkindex/) [Source 2](https://doc.teklia.com/arkindex/overview/license/) [Source 3](https://doc.teklia.com/arkindex/deployment/) [Source 4](https://doc.teklia.com/arkindex/deployment/hardware/) [Source 5](https://doc.teklia.com/arkindex_tutorial/export/) [Source 6](https://www.teklia.com/arkindex-tutorial)

1. Prepare a Linux host with Docker, a domain and TLS, IIIF image access, compatible S3 storage and TLS SMTP for application notifications.
2. Follow the Community Edition deployment docs. Plan task workers for the desired recognition model and test access on one small corpus.
### First project

A small first project makes the input, model output and handoff easy to inspect. [Source 1](https://doc.teklia.com/arkindex/) [Source 2](https://doc.teklia.com/arkindex/overview/license/) [Source 3](https://doc.teklia.com/arkindex/deployment/) [Source 4](https://doc.teklia.com/arkindex/deployment/hardware/) [Source 5](https://doc.teklia.com/arkindex_tutorial/export/) [Source 6](https://www.teklia.com/arkindex-tutorial)

1. Import an authorized IIIF manifest into a test corpus. Select the appropriate OCR or HTR worker for the capture.
2. Review predicted text and regions beside source pages. Export the checked version and retain processor metadata for the publication handoff.
### Hardware & software

Platform and compute constraints refer to the selected route. [Source 1](https://doc.teklia.com/arkindex/) [Source 2](https://doc.teklia.com/arkindex/overview/license/) [Source 3](https://doc.teklia.com/arkindex/deployment/) [Source 4](https://doc.teklia.com/arkindex/deployment/hardware/) [Source 5](https://doc.teklia.com/arkindex_tutorial/export/) [Source 6](https://www.teklia.com/arkindex-tutorial)

- **Hardware:** Teklia’s production guidance lists 4 cores, 4 GB RAM and 80 GB storage per web node. Its separate database recommendation is 8–12 cores, 32 GB RAM and 500 GB storage. It recommends at least 8 cores and 16 GB RAM for machine-learning workers, with GPUs for some tasks.
- **Software:** Arkindex Community 1.13.2, Docker, Linux, IIIF, TLS, SMTP and S3-compatible storage. Match each recognition worker and model to the document type.
- **Platforms:** Self-host deployment is documented for Linux servers, preferably Ubuntu LTS. Browser operation on other platforms does not imply native server support.

### License, model weights & costs

The full software license was reviewed. Dependencies and creative assets carry their own terms. [Source 1](https://gitlab.teklia.com/api/v4/projects/arkindex%2Fbackend/repository/files/LICENSE/raw?ref=develop) [Source 2](https://doc.teklia.com/arkindex/) [Source 3](https://doc.teklia.com/arkindex/overview/license/) [Source 4](https://doc.teklia.com/arkindex/deployment/) [Source 5](https://doc.teklia.com/arkindex/deployment/hardware/) [Source 6](https://doc.teklia.com/arkindex_tutorial/export/) [Source 7](https://www.teklia.com/arkindex-tutorial)

- **Code:** AGPL-3.0
- **Weights:** The complete Community Edition AGPLv3 license was archived. Commercial enterprise licensing is separate. Workers, recognition models, source images and outputs require individual terms review.
- **Commercial:** Project code is governed by AGPL-3.0. Confirm selected model, source-media and output restrictions separately.
- **Cost:** Community code can be self-hosted. The Linux server, storage and processing workers require capacity. Hosted and enterprise services have separate terms.

### Why it merits attention

The creative workflow is grounded in the cited documentation. Output quality and compatibility are not hands-on verified. [Source 1](https://doc.teklia.com/arkindex/) [Source 2](https://doc.teklia.com/arkindex/overview/license/) [Source 3](https://doc.teklia.com/arkindex/deployment/) [Source 4](https://doc.teklia.com/arkindex/deployment/hardware/) [Source 5](https://doc.teklia.com/arkindex_tutorial/export/) [Source 6](https://www.teklia.com/arkindex-tutorial)

### Limitations

This is a multi-service deployment. Recognition quality on a new collection and its PAGE layout handoff need source comparison and editor review. [Source 1](https://doc.teklia.com/arkindex/) [Source 2](https://doc.teklia.com/arkindex/overview/license/) [Source 3](https://doc.teklia.com/arkindex/deployment/) [Source 4](https://doc.teklia.com/arkindex/deployment/hardware/) [Source 5](https://doc.teklia.com/arkindex_tutorial/export/) [Source 6](https://www.teklia.com/arkindex-tutorial)

### Get the tool

- [Repository](https://gitlab.teklia.com/arkindex/backend)
- [Documentation](https://www.teklia.com/arkindex-tutorial)

## Kraken

Cultural heritage layout recognition and transcription · Archives, media restoration & collections · Creative publishing & presentation

First complete guide in the library. The publication and documentation dates are not necessarily the project’s launch date.

### Quality assessment: Quality unverified

Creative use and the code grant are documented. Check-level gaps remain before a recommendation.

Scope: Batch-produce a draft line-linked transcription from scanned pages while retaining layout and reading order for editorial correction.

Evidence checked: 2026-11-21. No local execution implied.

- **Open-source software license · verified:** Reviewed the complete project software grant and its redistribution conditions. Model, data and service terms are scoped separately. [Source](https://github.com/mittagessen/kraken/blob/main/LICENSE)
- **Creative results · documented:** The package and author documentation describe trainable layout and recognition. DAHN reports applying this engine through eScriptorium in a historical-document publication pipeline. [Source](https://github.com/mittagessen/kraken/blob/main/README.rst) [Source](https://pypi.org/project/kraken/) [Source](https://journals.openedition.org/jtei/5306)
- **Reproducible setup · documented:** The installation and first-use steps are in the cited documentation. Reproduction of this workflow remains unverified. [Source](https://github.com/mittagessen/kraken/blob/main/README.rst) [Source](https://pypi.org/project/kraken/) [Source](https://journals.openedition.org/jtei/5306)
- **Maintenance and support · documented:** Current GitHub release 7.2 was retrieved. Review support for the target model and script before a production migration. [Source](https://github.com/mittagessen/kraken/releases/tag/7.2)
- **Independent use · verified:** DAHN describes segmentation and transcription with Kraken via eScriptorium in a scholarly publication project. It covers prior versions. [Source](https://journals.openedition.org/jtei/5306)
- **Models, services and costs · documented:** The complete Apache-2.0 software grant was archived. Each trained model and the source scan collection require a separate terms check. Local processing is possible. Model downloads and any training consume compute and storage. [Source](https://github.com/mittagessen/kraken/blob/main/README.rst) [Source](https://pypi.org/project/kraken/) [Source](https://journals.openedition.org/jtei/5306)

Source and documentation review. No hands-on execution by AI Media Scout. Historical layout, right-to-left text and uncommon scripts need model-specific comparisons. An independently used earlier pipeline does not establish accuracy of Kraken 7.2 in this project.

### How it uses AI

Kraken uses trainable reading order, layout analysis and character recognition for historical and non-Latin-script document images. [Source](https://github.com/mittagessen/kraken/blob/main/README.rst) [Source](https://pypi.org/project/kraken/) [Source](https://journals.openedition.org/jtei/5306)

### Introduction

Kraken uses trainable reading order, layout analysis and character recognition for historical and non-Latin-script document images. [Source 1](https://github.com/mittagessen/kraken/blob/main/README.rst) [Source 2](https://pypi.org/project/kraken/) [Source 3](https://journals.openedition.org/jtei/5306)

### What it is good for

Batch-produce a draft line-linked transcription from scanned pages while retaining layout and reading order for editorial correction. [Source 1](https://github.com/mittagessen/kraken/blob/main/README.rst) [Source 2](https://pypi.org/project/kraken/) [Source 3](https://journals.openedition.org/jtei/5306)

### Demo & examples

The package and author documentation describe trainable layout and recognition. DAHN reports applying this engine through eScriptorium in a historical-document publication pipeline. [Source 1](https://github.com/mittagessen/kraken/blob/main/README.rst) [Source 2](https://pypi.org/project/kraken/) [Source 3](https://journals.openedition.org/jtei/5306)

### Install

Follow the documented route for the scoped workflow. The steps below are source references. [Source 1](https://github.com/mittagessen/kraken/blob/main/README.rst) [Source 2](https://pypi.org/project/kraken/) [Source 3](https://journals.openedition.org/jtei/5306)

1. Create a compatible Python environment. Install the published Kraken package, using the PDF extra only when needed.
2. Choose a model for the script and page layout. Obtain it only through its documented source and check its terms.

```sh
pip install kraken
```

### First project

A small first project makes the input, model output and handoff easy to inspect. [Source 1](https://github.com/mittagessen/kraken/blob/main/README.rst) [Source 2](https://pypi.org/project/kraken/) [Source 3](https://journals.openedition.org/jtei/5306)

1. Try one page with known ground truth. Select models suitable for its layout and writing direction.
2. Perform segmentation and recognition and compare output with the page. Check reading order and diacritics separately before batching.
### Hardware & software

Platform and compute constraints refer to the selected route. [Source 1](https://github.com/mittagessen/kraken/blob/main/README.rst) [Source 2](https://pypi.org/project/kraken/) [Source 3](https://journals.openedition.org/jtei/5306)

- **Hardware:** Minimum RAM, VRAM and disk space for the scoped workflow are undocumented.
- **Software:** Kraken 7.2. The upstream README documents Python 3.10 through 3.13. Model and optional PDF dependencies depend on the scoped input.
- **Platforms:** Linux and macOS on x64 and ARM are documented. Native Windows support is not documented in the reviewed setup.

### License, model weights & costs

The full software license was reviewed. Dependencies and creative assets carry their own terms. [Source 1](https://github.com/mittagessen/kraken/blob/main/LICENSE) [Source 2](https://github.com/mittagessen/kraken/blob/main/README.rst) [Source 3](https://pypi.org/project/kraken/) [Source 4](https://journals.openedition.org/jtei/5306)

- **Code:** Apache-2.0
- **Weights:** The complete Apache-2.0 software grant was archived. Each trained model and the source scan collection require a separate terms check.
- **Commercial:** Project code is governed by Apache-2.0. Confirm selected model, source-media and output restrictions separately.
- **Cost:** Local processing is possible. Model downloads and any training consume compute and storage.

### Why it merits attention

The creative workflow is grounded in the cited documentation. Output quality and compatibility are not hands-on verified. [Source 1](https://github.com/mittagessen/kraken/blob/main/README.rst) [Source 2](https://pypi.org/project/kraken/) [Source 3](https://journals.openedition.org/jtei/5306)

### Limitations

Historical layout, right-to-left text and uncommon scripts need model-specific comparisons. An independently used earlier pipeline does not establish accuracy of Kraken 7.2 in this project. [Source 1](https://github.com/mittagessen/kraken/blob/main/README.rst) [Source 2](https://pypi.org/project/kraken/) [Source 3](https://journals.openedition.org/jtei/5306)

### Get the tool

- [Repository](https://github.com/mittagessen/kraken)
- [Documentation](https://journals.openedition.org/jtei/5306)

## StagePulse

Live production accessibility and routed captions · Accessible media & assistive creation · Performance, projection & stage media

First complete guide in the library. The publication and documentation dates are not necessarily the project’s launch date.

### Quality assessment: Quality unverified

Creative use and the code grant are documented. Check-level gaps remain before a recommendation.

Scope: Rehearse English and Spanish venue captions from one stage audio feed and route the same feed to both an operator console and audience display.

Evidence checked: 2026-11-21. No local execution implied.

- **Open-source software license · verified:** Reviewed the complete project software grant and its redistribution conditions. Model, data and service terms are scoped separately. [Source](https://github.com/ignaciomakara/StagePulse/blob/main/LICENSE)
- **Creative results · documented:** The README documents a test-audio route at playback speed and three client views. The challenge test files are not bundled and independently measured delay and caption quality are unavailable. [Source](https://github.com/ignaciomakara/StagePulse/blob/main/README.md) [Source](https://github.com/ignaciomakara/StagePulse/blob/main/README.es.md)
- **Reproducible setup · documented:** The installation and first-use steps are in the cited documentation. Reproduction of this workflow remains unverified. [Source](https://github.com/ignaciomakara/StagePulse/blob/main/README.md) [Source](https://github.com/ignaciomakara/StagePulse/blob/main/README.es.md)
- **Maintenance and support · unknown:** The reviewed sources do not establish workflow-specific support, fixes and unresolved blockers.
- **Independent use · unknown:** Independent first-hand use of the exact workflow was not established in this source review.
- **Models, services and costs · documented:** The project grant is Apache-2.0. The Gemini translation service is separate and requires its own access, terms and permissions for sending audio. Compute plus provider capacity and charges depend on active stage streams. The README distinguishes the stage stream from extra viewers. [Source](https://github.com/ignaciomakara/StagePulse/blob/main/README.md) [Source](https://github.com/ignaciomakara/StagePulse/blob/main/README.es.md)

Source and documentation review. No hands-on execution by AI Media Scout. This source-documented challenge implementation needs independent validation for venue latency, reconnects and multilingual terminology. Audio leaves the capture host on the Gemini route.

### How it uses AI

StagePulse uses a separate Gemini Live Translate stream for each active conference stage and repackages speech into live original and translated captions for browser displays. [Source](https://github.com/ignaciomakara/StagePulse/blob/main/README.md) [Source](https://github.com/ignaciomakara/StagePulse/blob/main/README.es.md)

### Introduction

StagePulse uses a separate Gemini Live Translate stream for each active conference stage and repackages speech into live original and translated captions for browser displays. [Source 1](https://github.com/ignaciomakara/StagePulse/blob/main/README.md) [Source 2](https://github.com/ignaciomakara/StagePulse/blob/main/README.es.md)

### What it is good for

Rehearse English and Spanish venue captions from one stage audio feed and route the same feed to both an operator console and audience display. [Source 1](https://github.com/ignaciomakara/StagePulse/blob/main/README.md) [Source 2](https://github.com/ignaciomakara/StagePulse/blob/main/README.es.md)

### Demo & examples

The README documents a test-audio route at playback speed and three client views. The challenge test files are not bundled and independently measured delay and caption quality are unavailable. [Source 1](https://github.com/ignaciomakara/StagePulse/blob/main/README.md) [Source 2](https://github.com/ignaciomakara/StagePulse/blob/main/README.es.md)

### Install

Follow the documented route for the scoped workflow. The steps below are source references. [Source 1](https://github.com/ignaciomakara/StagePulse/blob/main/README.md) [Source 2](https://github.com/ignaciomakara/StagePulse/blob/main/README.es.md)

1. On the documented Windows route prepare Python 3.10 or later, FFmpeg on PATH, a browser with AudioWorklet and a Gemini API account.
2. Configure a stage with the documented JSON format and add the key through the local environment. Follow the project’s PowerShell or manual instructions.
### First project

A small first project makes the input, model output and handoff easy to inspect. [Source 1](https://github.com/ignaciomakara/StagePulse/blob/main/README.md) [Source 2](https://github.com/ignaciomakara/StagePulse/blob/main/README.es.md)

1. Start with one test stage and audio you can send to the provider. Open the operator and display clients for that stage.
2. Play a short known passage and compare bilingual final captions with the source. Check lag and reconnect behavior before bringing in additional stages.
### Hardware & software

Platform and compute constraints refer to the selected route. [Source 1](https://github.com/ignaciomakara/StagePulse/blob/main/README.md) [Source 2](https://github.com/ignaciomakara/StagePulse/blob/main/README.es.md)

- **Hardware:** Minimum RAM, VRAM and disk space for the scoped workflow are undocumented.
- **Software:** Python 3.10 or newer, venv, FFmpeg, compatible browser and Gemini Live Translate access over a network.
- **Platforms:** Windows PowerShell is the documented path. Other OS deployment is unverified. Viewers need a suitable browser.

### License, model weights & costs

The full software license was reviewed. Dependencies and creative assets carry their own terms. [Source 1](https://github.com/ignaciomakara/StagePulse/blob/main/LICENSE) [Source 2](https://github.com/ignaciomakara/StagePulse/blob/main/README.md) [Source 3](https://github.com/ignaciomakara/StagePulse/blob/main/README.es.md)

- **Code:** Apache-2.0
- **Weights:** The project grant is Apache-2.0. The Gemini translation service is separate and requires its own access, terms and permissions for sending audio.
- **Commercial:** Project code is governed by Apache-2.0. Confirm selected model, source-media and output restrictions separately.
- **Cost:** Compute plus provider capacity and charges depend on active stage streams. The README distinguishes the stage stream from extra viewers.

### Why it merits attention

The creative workflow is grounded in the cited documentation. Output quality and compatibility are not hands-on verified. [Source 1](https://github.com/ignaciomakara/StagePulse/blob/main/README.md) [Source 2](https://github.com/ignaciomakara/StagePulse/blob/main/README.es.md)

### Limitations

This source-documented challenge implementation needs independent validation for venue latency, reconnects and multilingual terminology. Audio leaves the capture host on the Gemini route. [Source 1](https://github.com/ignaciomakara/StagePulse/blob/main/README.md) [Source 2](https://github.com/ignaciomakara/StagePulse/blob/main/README.es.md)

### Get the tool

- [Repository](https://github.com/ignaciomakara/StagePulse)
- [Documentation](https://github.com/ignaciomakara/StagePulse/blob/main/README.es.md)

## SCoIM

AI music notation and score recovery · Audio, music & voice

First complete guide in the library. The publication and documentation dates are not necessarily the project’s launch date.

### Quality assessment: Experimental

Creative use and the code grant are documented. Check-level gaps remain before a recommendation.

Scope: Develop an editable short solo-piano sketch, retaining the accepted scene outline, MusicXML score and MIDI output separately.

Evidence checked: 2026-11-21. No local execution implied.

Why Experimental: The maintainer identifies SCoIM as experimental and its current musical realization as unfinished for broader instrumentation and style fidelity. https://github.com/AllegroMoltoV/scoim/blob/main/README.md

- **Open-source software license · verified:** Reviewed the complete project software grant and its redistribution conditions. Model, data and service terms are scoped separately. [Source](https://github.com/AllegroMoltoV/scoim/blob/main/LICENSE)
- **Creative results · documented:** The project publishes a roughly three-minute piano example and a fixed-flow fixture. The v0.3.0 release records work on scene variation, pedals and resuming saved material. [Source](https://github.com/AllegroMoltoV/scoim/blob/main/README.md) [Source](https://github.com/AllegroMoltoV/scoim/blob/main/examples/public-music/bright-return/README.md)
- **Reproducible setup · documented:** The installation and first-use steps are in the cited documentation. Reproduction of this workflow remains unverified. [Source](https://github.com/AllegroMoltoV/scoim/blob/main/README.md) [Source](https://github.com/AllegroMoltoV/scoim/blob/main/examples/public-music/bright-return/README.md)
- **Maintenance and support · documented:** v0.3.0 records scene-variation and saved-attempt changes. Independent reproduction remains a gap. [Source](https://github.com/AllegroMoltoV/scoim/releases/tag/v0.3.0)
- **Independent use · unknown:** Independent first-hand use of the exact workflow was not established in this source review.
- **Models, services and costs · documented:** MIT applies to repository code. The called model service and input or generated music retain separate terms and rights. Logged-in model access is required during generation. Local replay of a saved bundle has different access requirements. [Source](https://github.com/AllegroMoltoV/scoim/blob/main/README.md) [Source](https://github.com/AllegroMoltoV/scoim/blob/main/examples/public-music/bright-return/README.md)

Source and documentation review. No hands-on execution by AI Media Scout. The public CLI currently centers on solo piano. The author explicitly describes quality as research in progress and does not promise broad instrumentation or stylistic reproduction.

### How it uses AI

SCoIM proposes a piano-piece script with an LLM, allows manual scene-level approval and realizes the approved document into harmony, melody, accompaniment and performance. [Source](https://github.com/AllegroMoltoV/scoim/blob/main/README.md) [Source](https://github.com/AllegroMoltoV/scoim/blob/main/examples/public-music/bright-return/README.md)

### Introduction

SCoIM proposes a piano-piece script with an LLM, allows manual scene-level approval and realizes the approved document into harmony, melody, accompaniment and performance. [Source 1](https://github.com/AllegroMoltoV/scoim/blob/main/README.md) [Source 2](https://github.com/AllegroMoltoV/scoim/blob/main/examples/public-music/bright-return/README.md)

### What it is good for

Develop an editable short solo-piano sketch, retaining the accepted scene outline, MusicXML score and MIDI output separately. [Source 1](https://github.com/AllegroMoltoV/scoim/blob/main/README.md) [Source 2](https://github.com/AllegroMoltoV/scoim/blob/main/examples/public-music/bright-return/README.md)

### Demo & examples

The project publishes a roughly three-minute piano example and a fixed-flow fixture. The v0.3.0 release records work on scene variation, pedals and resuming saved material. [Source 1](https://github.com/AllegroMoltoV/scoim/blob/main/README.md) [Source 2](https://github.com/AllegroMoltoV/scoim/blob/main/examples/public-music/bright-return/README.md)

### Install

Follow the documented route for the scoped workflow. The steps below are source references. [Source 1](https://github.com/AllegroMoltoV/scoim/blob/main/README.md) [Source 2](https://github.com/AllegroMoltoV/scoim/blob/main/examples/public-music/bright-return/README.md)

1. On the documented Windows route use Python 3.13 and the project PowerShell setup. Authenticate Codex CLI only for the generation workflow.
2. Inspect the fixed-flow example before making provider calls. Use the release’s documented model and profile selection.
### First project

A small first project makes the input, model output and handoff easy to inspect. [Source 1](https://github.com/AllegroMoltoV/scoim/blob/main/README.md) [Source 2](https://github.com/AllegroMoltoV/scoim/blob/main/examples/public-music/bright-return/README.md)

1. Propose a short solo-piano scene outline. Inspect a transition and revise the JSON Patch or approve the draft.
2. Realize the approved version and inspect its separate foreground and score previews.
3. Open the final MusicXML and MIDI in a score or sequence editor. Correct musical structure and listen to the performance before publishing.
### Hardware & software

Platform and compute constraints refer to the selected route. [Source 1](https://github.com/AllegroMoltoV/scoim/blob/main/README.md) [Source 2](https://github.com/AllegroMoltoV/scoim/blob/main/examples/public-music/bright-return/README.md)

- **Hardware:** Minimum RAM, VRAM and disk space for the scoped workflow are undocumented.
- **Software:** Windows, Python 3.13 and authenticated Codex CLI for model generation. Saved-bundle replay is documented without external communication.
- **Platforms:** The current README identifies Windows for its verified local source path. Other OS compatibility is undocumented.

### License, model weights & costs

The full software license was reviewed. Dependencies and creative assets carry their own terms. [Source 1](https://github.com/AllegroMoltoV/scoim/blob/main/LICENSE) [Source 2](https://github.com/AllegroMoltoV/scoim/blob/main/README.md) [Source 3](https://github.com/AllegroMoltoV/scoim/blob/main/examples/public-music/bright-return/README.md)

- **Code:** MIT
- **Weights:** MIT applies to repository code. The called model service and input or generated music retain separate terms and rights.
- **Commercial:** Project code is governed by MIT. Confirm selected model, source-media and output restrictions separately.
- **Cost:** Logged-in model access is required during generation. Local replay of a saved bundle has different access requirements.

### Why it merits attention

The creative workflow is grounded in the cited documentation. Output quality and compatibility are not hands-on verified. [Source 1](https://github.com/AllegroMoltoV/scoim/blob/main/README.md) [Source 2](https://github.com/AllegroMoltoV/scoim/blob/main/examples/public-music/bright-return/README.md)

### Limitations

The public CLI currently centers on solo piano. The author explicitly describes quality as research in progress and does not promise broad instrumentation or stylistic reproduction. [Source 1](https://github.com/AllegroMoltoV/scoim/blob/main/README.md) [Source 2](https://github.com/AllegroMoltoV/scoim/blob/main/examples/public-music/bright-return/README.md)

### Get the tool

- [Repository](https://github.com/AllegroMoltoV/scoim)
- [Documentation](https://github.com/AllegroMoltoV/scoim/blob/main/examples/public-music/bright-return/README.md)

## MusicSheet

AI music notation and score recovery · Audio, music & voice

This completes an earlier pending guide with a current source review.

### Quality assessment: Experimental

Creative use and the code grant are documented. Check-level gaps remain before a recommendation.

Scope: Inspect draft MIDI from clean piano audio in the current worker and correct its musical timing manually.

Evidence checked: 2026-11-21. No local execution implied.

Why Experimental: The current README expressly identifies source separation and full score creation as unimplemented. It scopes real-model execution to the implemented transcription worker. https://github.com/reha-design/MusicSheet/blob/main/README.md

- **Open-source software license · verified:** Reviewed the complete project software grant and its redistribution conditions. Model, data and service terms are scoped separately. [Source](https://github.com/reha-design/MusicSheet/blob/main/LICENSE)
- **Creative results · documented:** The maintainers document a Windows real-model and database verification. The architecture diagram describes future work beyond the implemented worker. [Source](https://github.com/reha-design/MusicSheet/blob/main/README.md) [Source](https://github.com/reha-design/MusicSheet/blob/main/services/ml/basic-pitch-worker/README.md)
- **Reproducible setup · documented:** The installation and first-use steps are in the cited documentation. Reproduction of this workflow remains unverified. [Source](https://github.com/reha-design/MusicSheet/blob/main/README.md) [Source](https://github.com/reha-design/MusicSheet/blob/main/services/ml/basic-pitch-worker/README.md)
- **Maintenance and support · unknown:** The reviewed sources do not establish workflow-specific support, fixes and unresolved blockers.
- **Independent use · unknown:** Independent first-hand use of the exact workflow was not established in this source review.
- **Models, services and costs · documented:** The complete MIT project license was archived. Basic Pitch weights and input audio rights require their own verification. The documented worker is local. Database runtime and compute apply. No production completeness or hosted service is assumed. [Source](https://github.com/reha-design/MusicSheet/blob/main/README.md) [Source](https://github.com/reha-design/MusicSheet/blob/main/services/ml/basic-pitch-worker/README.md)

Source and documentation review. No hands-on execution by AI Media Scout. Source separation, full video ingest and notation rendering are planned. The assessed workflow ends at Basic Pitch event/MIDI output.

### How it uses AI

The implemented opt-in transcription worker uses Basic Pitch to derive JSON and MIDI note events from WAV input. Its wider planned score-generation and source-separation flow is not yet established. [Source](https://github.com/reha-design/MusicSheet/blob/main/README.md) [Source](https://github.com/reha-design/MusicSheet/blob/main/services/ml/basic-pitch-worker/README.md)

### Introduction

The implemented opt-in transcription worker uses Basic Pitch to derive JSON and MIDI note events from WAV input. Its wider planned score-generation and source-separation flow is not yet established. [Source 1](https://github.com/reha-design/MusicSheet/blob/main/README.md) [Source 2](https://github.com/reha-design/MusicSheet/blob/main/services/ml/basic-pitch-worker/README.md)

### What it is good for

Inspect draft MIDI from clean piano audio in the current worker and correct its musical timing manually. [Source 1](https://github.com/reha-design/MusicSheet/blob/main/README.md) [Source 2](https://github.com/reha-design/MusicSheet/blob/main/services/ml/basic-pitch-worker/README.md)

### Demo & examples

The maintainers document a Windows real-model and database verification. The architecture diagram describes future work beyond the implemented worker. [Source 1](https://github.com/reha-design/MusicSheet/blob/main/README.md) [Source 2](https://github.com/reha-design/MusicSheet/blob/main/services/ml/basic-pitch-worker/README.md)

### Install

Follow the documented route for the scoped workflow. The steps below are source references. [Source 1](https://github.com/reha-design/MusicSheet/blob/main/README.md) [Source 2](https://github.com/reha-design/MusicSheet/blob/main/services/ml/basic-pitch-worker/README.md)

1. Prepare Python 3.13 and uv. Use the documented Docker Compose stack for PostgreSQL and Redis.
2. Read the API and Basic Pitch worker instructions for their separate environments. Explicitly enable the transcription provider.
### First project

A small first project makes the input, model output and handoff easy to inspect. [Source 1](https://github.com/reha-design/MusicSheet/blob/main/README.md) [Source 2](https://github.com/reha-design/MusicSheet/blob/main/services/ml/basic-pitch-worker/README.md)

1. Use a short owned piano recording and submit a supported WAV job.
2. Inspect the JSON and MIDI outputs and compare notes against a reference phrase. Open MIDI in a score tool for further correction.
### Hardware & software

Platform and compute constraints refer to the selected route. [Source 1](https://github.com/reha-design/MusicSheet/blob/main/README.md) [Source 2](https://github.com/reha-design/MusicSheet/blob/main/services/ml/basic-pitch-worker/README.md)

- **Hardware:** Minimum RAM, VRAM and disk space for the scoped workflow are undocumented.
- **Software:** Python 3.13, uv, PostgreSQL 16, Redis 7 and the worker’s CPU ONNX Runtime environment. Use Docker Compose for the documented local services.
- **Platforms:** Windows actual model execution is documented. Linux launcher/CI checks are narrower and Linux Celery real-model operation remains pending. Native macOS support is unverified.

### License, model weights & costs

The full software license was reviewed. Dependencies and creative assets carry their own terms. [Source 1](https://github.com/reha-design/MusicSheet/blob/main/LICENSE) [Source 2](https://github.com/reha-design/MusicSheet/blob/main/README.md) [Source 3](https://github.com/reha-design/MusicSheet/blob/main/services/ml/basic-pitch-worker/README.md)

- **Code:** MIT
- **Weights:** The complete MIT project license was archived. Basic Pitch weights and input audio rights require their own verification.
- **Commercial:** Project code is governed by MIT. Confirm selected model, source-media and output restrictions separately.
- **Cost:** The documented worker is local. Database runtime and compute apply. No production completeness or hosted service is assumed.

### Why it merits attention

The creative workflow is grounded in the cited documentation. Output quality and compatibility are not hands-on verified. [Source 1](https://github.com/reha-design/MusicSheet/blob/main/README.md) [Source 2](https://github.com/reha-design/MusicSheet/blob/main/services/ml/basic-pitch-worker/README.md)

### Limitations

Source separation, full video ingest and notation rendering are planned. The assessed workflow ends at Basic Pitch event/MIDI output. [Source 1](https://github.com/reha-design/MusicSheet/blob/main/README.md) [Source 2](https://github.com/reha-design/MusicSheet/blob/main/services/ml/basic-pitch-worker/README.md)

### Get the tool

- [Repository](https://github.com/reha-design/MusicSheet)
- [Documentation](https://github.com/reha-design/MusicSheet/blob/main/services/ml/basic-pitch-worker/README.md)

## Audiocast

Audio, music & voice · Creative publishing & presentation · Storyboarding, narrative & comics

This completes an earlier pending guide with a current source review.

### Quality assessment: Quality unverified

Creative use and the code grant are documented. Check-level gaps remain before a recommendation.

Scope: Make a short rights-cleared excerpt with distinct narrator and character voices and check pacing line by line.

Evidence checked: 2026-11-21. No local execution implied.

- **Open-source software license · verified:** Reviewed the complete project software grant and its redistribution conditions. Model, data and service terms are scoped separately. [Source](https://github.com/akjoshi12/Audiocast/blob/main/LICENSE)
- **Creative results · documented:** The repository includes its own promotional film and setup instructions. Independent fidelity for a specific book, language and voice set remains unknown. [Source](https://github.com/akjoshi12/Audiocast/blob/main/README.md)
- **Reproducible setup · documented:** The installation and first-use steps are in the cited documentation. Reproduction of this workflow remains unverified. [Source](https://github.com/akjoshi12/Audiocast/blob/main/README.md)
- **Maintenance and support · documented:** A v0.1.0 release is available. App-level reproduction with selected models and Android sync remains open. [Source](https://github.com/akjoshi12/Audiocast/releases/tag/v0.1.0)
- **Independent use · unknown:** Independent first-hand use of the exact workflow was not established in this source review.
- **Models, services and costs · documented:** Apache-2.0 applies to project code. Book, narrator assets, voice and language-model weights have separate terms. Local authoring needs model downloads, storage and compute. The optional lookup has network requirements. [Source](https://github.com/akjoshi12/Audiocast/blob/main/README.md)

Source and documentation review. No hands-on execution by AI Media Scout. Text extraction, casting, pronunciation and pacing need editorial review. Use only text and voice examples you have permission to transform.

### How it uses AI

Audiocast uses a local language model to label a book’s speakers and delivery cues, then builds separate synthetic voice tracks for a cast-style audiobook. [Source](https://github.com/akjoshi12/Audiocast/blob/main/README.md)

### Introduction

Audiocast uses a local language model to label a book’s speakers and delivery cues, then builds separate synthetic voice tracks for a cast-style audiobook. [Source 1](https://github.com/akjoshi12/Audiocast/blob/main/README.md)

### What it is good for

Make a short rights-cleared excerpt with distinct narrator and character voices and check pacing line by line. [Source 1](https://github.com/akjoshi12/Audiocast/blob/main/README.md)

### Demo & examples

The repository includes its own promotional film and setup instructions. Independent fidelity for a specific book, language and voice set remains unknown. [Source 1](https://github.com/akjoshi12/Audiocast/blob/main/README.md)

### Install

Follow the documented route for the scoped workflow. The steps below are source references. [Source 1](https://github.com/akjoshi12/Audiocast/blob/main/README.md)

1. Use the source setup on an Apple silicon Mac. Prepare Python 3.12, uv, FFmpeg and espeak-ng as documented.
2. Set up the local language and speech runtimes including any separate voice environment. Obtain the selected model weights under recorded terms.
### First project

A small first project makes the input, model output and handoff easy to inspect. [Source 1](https://github.com/akjoshi12/Audiocast/blob/main/README.md)

1. Load a short EPUB, PDF or text excerpt you may transform. Inspect its segmentation and speaker labels before synthesis.
2. Assign distinct authorized voices, generate the excerpt and compare dialogue attribution and pronunciations.
3. Keep the export and timing corrections alongside the source. Evaluate the optional Android playback handoff separately.
### Hardware & software

Platform and compute constraints refer to the selected route. [Source 1](https://github.com/akjoshi12/Audiocast/blob/main/README.md)

- **Hardware:** Apple silicon. The developer recommends 64 GB RAM for the documented model setup. A minimum and total disk requirement are undocumented.
- **Software:** Python 3.12 with uv, FFmpeg, espeak-ng and the documented local language/TTS models. Optional Android player or Wikipedia lookup are separate routes.
- **Platforms:** Production setup documents Apple silicon macOS. Android is a playback client in the described workflow. Other authoring environments are unverified.

### License, model weights & costs

The full software license was reviewed. Dependencies and creative assets carry their own terms. [Source 1](https://github.com/akjoshi12/Audiocast/blob/main/LICENSE) [Source 2](https://github.com/akjoshi12/Audiocast/blob/main/README.md)

- **Code:** Apache-2.0
- **Weights:** Apache-2.0 applies to project code. Book, narrator assets, voice and language-model weights have separate terms.
- **Commercial:** Project code is governed by Apache-2.0. Confirm selected model, source-media and output restrictions separately.
- **Cost:** Local authoring needs model downloads, storage and compute. The optional lookup has network requirements.

### Why it merits attention

The creative workflow is grounded in the cited documentation. Output quality and compatibility are not hands-on verified. [Source 1](https://github.com/akjoshi12/Audiocast/blob/main/README.md)

### Limitations

Text extraction, casting, pronunciation and pacing need editorial review. Use only text and voice examples you have permission to transform. [Source 1](https://github.com/akjoshi12/Audiocast/blob/main/README.md)

### Get the tool

- [Repository](https://github.com/akjoshi12/Audiocast)
- [Documentation](https://github.com/akjoshi12/Audiocast/blob/main/README.md)

## Utteran

Audio, music & voice · Editing, captions & post-production · Archives, media restoration & collections

The source repository was created on 2026-10-29. This is its first complete guide in the library.

### Quality assessment: Quality unverified

Creative use and the code grant are documented. Check-level gaps remain before a recommendation.

Scope: Produce a timestamped SRT or VTT draft and a speaker-aware transcript of a recorded interview.

Evidence checked: 2026-11-21. No local execution implied.

- **Open-source software license · verified:** Reviewed the complete project software grant and its redistribution conditions. Model, data and service terms are scoped separately. [Source](https://github.com/zawa356/Utteran/blob/main/LICENSE)
- **Creative results · documented:** The maintainer documents recorded acceptance in specific CPU/Windows configurations. It also distinguishes unmerged or unreleased interface work and GPU paths requiring more testing. [Source](https://github.com/zawa356/Utteran/blob/main/README.md) [Source](https://github.com/zawa356/Utteran/blob/main/README.en.md)
- **Reproducible setup · documented:** The installation and first-use steps are in the cited documentation. Reproduction of this workflow remains unverified. [Source](https://github.com/zawa356/Utteran/blob/main/README.md) [Source](https://github.com/zawa356/Utteran/blob/main/README.en.md)
- **Maintenance and support · documented:** The latest captured published tag is v0.1.28. The current source documents later interface experiments and their weaker verification. [Source](https://github.com/zawa356/Utteran/releases/tag/v0.1.28)
- **Independent use · unknown:** Independent first-hand use of the exact workflow was not established in this source review.
- **Models, services and costs · documented:** MIT covers Utteran source. Exact Whisper backend weights and gated pyannote components receive individual model/access checks. Local compute, storage and model downloads apply. Hosted inference is outside this workflow. [Source](https://github.com/zawa356/Utteran/blob/main/README.md) [Source](https://github.com/zawa356/Utteran/blob/main/README.en.md)

Source and documentation review. No hands-on execution by AI Media Scout. The main-branch README includes unreleased acceptance notes. Reproduce the specific released path before relying on a given GUI, GPU or diarization feature.

### How it uses AI

Utteran runs local speech recognition and can add speaker turns using pyannote. The Windows workflow exports cues and text for editing. [Source](https://github.com/zawa356/Utteran/blob/main/README.md) [Source](https://github.com/zawa356/Utteran/blob/main/README.en.md)

### Introduction

Utteran runs local speech recognition and can add speaker turns using pyannote. The Windows workflow exports cues and text for editing. [Source 1](https://github.com/zawa356/Utteran/blob/main/README.md) [Source 2](https://github.com/zawa356/Utteran/blob/main/README.en.md)

### What it is good for

Produce a timestamped SRT or VTT draft and a speaker-aware transcript of a recorded interview. [Source 1](https://github.com/zawa356/Utteran/blob/main/README.md) [Source 2](https://github.com/zawa356/Utteran/blob/main/README.en.md)

### Demo & examples

The maintainer documents recorded acceptance in specific CPU/Windows configurations. It also distinguishes unmerged or unreleased interface work and GPU paths requiring more testing. [Source 1](https://github.com/zawa356/Utteran/blob/main/README.md) [Source 2](https://github.com/zawa356/Utteran/blob/main/README.en.md)

### Install

Follow the documented route for the scoped workflow. The steps below are source references. [Source 1](https://github.com/zawa356/Utteran/blob/main/README.md) [Source 2](https://github.com/zawa356/Utteran/blob/main/README.en.md)

1. Choose the current documented Windows installer, portable package or Python route. Use the package checksums when available.
2. Follow the release-specific model setup. Access to the gated speaker model can require a Hugging Face account and approval.
### First project

A small first project makes the input, model output and handoff easy to inspect. [Source 1](https://github.com/zawa356/Utteran/blob/main/README.md) [Source 2](https://github.com/zawa356/Utteran/blob/main/README.en.md)

1. Import one recording with distinct speakers. Choose a supported inference profile and enable speaker diarization only after configuring its model.
2. Review speaker switches, names and caption timing. Export SRT or VTT with a text or JSON reference version.
### Hardware & software

Platform and compute constraints refer to the selected route. [Source 1](https://github.com/zawa356/Utteran/blob/main/README.md) [Source 2](https://github.com/zawa356/Utteran/blob/main/README.en.md)

- **Hardware:** Storage may reach several GB after models and portable environments are installed. No universal CPU, VRAM or RAM minimum is documented.
- **Software:** Documented Windows path uses Python 3.11/3.12 for source operation plus uv and FFmpeg. Current project docs name faster-whisper, whisper.cpp and pyannote.audio options. Verify exact compatibility with the installed release.
- **Platforms:** Windows 10/11 primary. Linux receives limited CI and is secondary. General GPU functions and native macOS support remain unverified in the reviewed route.

### License, model weights & costs

The full software license was reviewed. Dependencies and creative assets carry their own terms. [Source 1](https://github.com/zawa356/Utteran/blob/main/LICENSE) [Source 2](https://github.com/zawa356/Utteran/blob/main/README.md) [Source 3](https://github.com/zawa356/Utteran/blob/main/README.en.md)

- **Code:** MIT
- **Weights:** MIT covers Utteran source. Exact Whisper backend weights and gated pyannote components receive individual model/access checks.
- **Commercial:** Project code is governed by MIT. Confirm selected model, source-media and output restrictions separately.
- **Cost:** Local compute, storage and model downloads apply. Hosted inference is outside this workflow.

### Why it merits attention

The creative workflow is grounded in the cited documentation. Output quality and compatibility are not hands-on verified. [Source 1](https://github.com/zawa356/Utteran/blob/main/README.md) [Source 2](https://github.com/zawa356/Utteran/blob/main/README.en.md)

### Limitations

The main-branch README includes unreleased acceptance notes. Reproduce the specific released path before relying on a given GUI, GPU or diarization feature. [Source 1](https://github.com/zawa356/Utteran/blob/main/README.md) [Source 2](https://github.com/zawa356/Utteran/blob/main/README.en.md)

### Get the tool

- [Repository](https://github.com/zawa356/Utteran)
- [Documentation](https://github.com/zawa356/Utteran/blob/main/README.en.md)

## Synodos

Audio, music & voice · Archives, media restoration & collections · Editing, captions & post-production

This completes an earlier pending guide with a current source review.

### Quality assessment: Quality unverified

Creative use and the code grant are documented. Check-level gaps remain before a recommendation.

Scope: Create a reviewable draft transcript and speaker timeline for a small oral-history recording session.

Evidence checked: 2026-11-21. No local execution implied.

- **Open-source software license · verified:** Reviewed the complete project software grant and its redistribution conditions. Model, data and service terms are scoped separately. [Source](https://github.com/hwspen7/Synodos/blob/main/LICENSE)
- **Creative results · documented:** The source gives architecture and a getting-started recording flow. It explicitly distinguishes shared-microphone attribution and acoustic signal handling. [Source](https://github.com/hwspen7/Synodos/blob/main/README.md)
- **Reproducible setup · documented:** The installation and first-use steps are in the cited documentation. Reproduction of this workflow remains unverified. [Source](https://github.com/hwspen7/Synodos/blob/main/README.md)
- **Maintenance and support · unknown:** The reviewed sources do not establish workflow-specific support, fixes and unresolved blockers.
- **Independent use · unknown:** Independent first-hand use of the exact workflow was not established in this source review.
- **Models, services and costs · documented:** Source uses MIT. Chosen Whisper, Qwen and speaker dependencies each have their own model terms. Recording and identity data require consent handling. Local compute and model storage apply. NVIDIA CUDA is optional where documented. [Source](https://github.com/hwspen7/Synodos/blob/main/README.md)

Source and documentation review. No hands-on execution by AI Media Scout. Shared-microphone voice attribution is uncertain when speakers overlap. Validate exact speaker identity and as-used model terms before archival handoff.

### How it uses AI

Synodos windows microphone audio for speech recognition, estimates speaker attribution and exposes bounded interview transcript segments for review. [Source](https://github.com/hwspen7/Synodos/blob/main/README.md)

### Introduction

Synodos windows microphone audio for speech recognition, estimates speaker attribution and exposes bounded interview transcript segments for review. [Source 1](https://github.com/hwspen7/Synodos/blob/main/README.md)

### What it is good for

Create a reviewable draft transcript and speaker timeline for a small oral-history recording session. [Source 1](https://github.com/hwspen7/Synodos/blob/main/README.md)

### Demo & examples

The source gives architecture and a getting-started recording flow. It explicitly distinguishes shared-microphone attribution and acoustic signal handling. [Source 1](https://github.com/hwspen7/Synodos/blob/main/README.md)

### Install

Follow the documented route for the scoped workflow. The steps below are source references. [Source 1](https://github.com/hwspen7/Synodos/blob/main/README.md)

1. Set up Python 3.12 or later, uv, Node 24.12 or later and pnpm. Choose the documented optional GPU path only after confirming hardware.
2. Start its local Python speech API and the browser workspace separately. Confirm the API health before granting microphone permission.

```sh
uv sync --python 3.12
```


```sh
uv pip install -r requirements/speech-whisper.txt
```


```sh
pnpm dev
```

### First project

A small first project makes the input, model output and handoff easy to inspect. [Source 1](https://github.com/hwspen7/Synodos/blob/main/README.md)

1. Record a short session with informed participants. Check how overlapping speech and changing mic distance affect segmentation.
2. Assign speakers with caution and compare transcript timestamps against the original recording. Preserve the reviewed export and original separately.
### Hardware & software

Platform and compute constraints refer to the selected route. [Source 1](https://github.com/hwspen7/Synodos/blob/main/README.md)

- **Hardware:** Minimum RAM, VRAM and disk space for the scoped workflow are undocumented.
- **Software:** Python 3.12+, uv, Node 24.12+, pnpm, compatible microphone; selected Whisper model plus any Qwen, speaker or local LLM dependencies.
- **Platforms:** The README provides Windows PowerShell setup and launcher. Other OS support requires verification for the full stack.

### License, model weights & costs

The full software license was reviewed. Dependencies and creative assets carry their own terms. [Source 1](https://github.com/hwspen7/Synodos/blob/main/LICENSE) [Source 2](https://github.com/hwspen7/Synodos/blob/main/README.md)

- **Code:** MIT
- **Weights:** Source uses MIT. Chosen Whisper, Qwen and speaker dependencies each have their own model terms. Recording and identity data require consent handling.
- **Commercial:** Project code is governed by MIT. Confirm selected model, source-media and output restrictions separately.
- **Cost:** Local compute and model storage apply. NVIDIA CUDA is optional where documented.

### Why it merits attention

The creative workflow is grounded in the cited documentation. Output quality and compatibility are not hands-on verified. [Source 1](https://github.com/hwspen7/Synodos/blob/main/README.md)

### Limitations

Shared-microphone voice attribution is uncertain when speakers overlap. Validate exact speaker identity and as-used model terms before archival handoff. [Source 1](https://github.com/hwspen7/Synodos/blob/main/README.md)

### Get the tool

- [Repository](https://github.com/hwspen7/Synodos)
- [Documentation](https://github.com/hwspen7/Synodos/blob/main/README.md)

## TTool-AI

AI furniture, timber and joinery design · AI-assisted textile and computational craft · 3D printing & generative CAD

This completes an earlier pending guide with a current source review.

### Quality assessment: Quality unverified

Creative use and the code grant are documented. Check-level gaps remain before a recommendation.

Scope: Prepare an AR visualization of a named woodworking tool and assess how consistently it aligns in a bench demonstration.

Evidence checked: 2026-11-21. No local execution implied.

- **Open-source software license · verified:** Reviewed the complete project software grant and its redistribution conditions. Model, data and service terms are scoped separately. [Source](https://github.com/ibois-epfl/TTool-ai/blob/main/LICENSE)
- **Creative results · documented:** The lab links the project to its Augmented Carpentry work and documents a training service. Current demo availability and alignment quality need independent checks. [Source](https://github.com/ibois-epfl/TTool-ai/blob/main/README.md) [Source](https://www.epfl.ch/labs/ibois/augmented-carpentry/) [Source](https://github.com/ibois-epfl/TTool-ai/wiki)
- **Reproducible setup · documented:** The installation and first-use steps are in the cited documentation. Reproduction of this workflow remains unverified. [Source](https://github.com/ibois-epfl/TTool-ai/blob/main/README.md) [Source](https://www.epfl.ch/labs/ibois/augmented-carpentry/) [Source](https://github.com/ibois-epfl/TTool-ai/wiki)
- **Maintenance and support · documented:** The project publishes v1.0.0 and lab setup docs. Current runtime and hardware compatibility needs direct reproduction. [Source](https://github.com/ibois-epfl/TTool-ai/releases/tag/v1.0.0)
- **Independent use · unknown:** Independent first-hand use of the exact workflow was not established in this source review.
- **Models, services and costs · documented:** The complete GPLv3 project file was reviewed. The parent AR runtime, sample assets and trained checkpoints have separate terms. The self-hosted training workflow requires local GPU time or compatible compute. The lab service’s availability and access are separate. [Source](https://github.com/ibois-epfl/TTool-ai/blob/main/README.md) [Source](https://www.epfl.ch/labs/ibois/augmented-carpentry/) [Source](https://github.com/ibois-epfl/TTool-ai/wiki)

Source and documentation review. No hands-on execution by AI Media Scout. Tracking a tool for visualization does not validate mechanical accuracy, user operation or fabrication safety. Keep the initial result a supervised demonstration.

### How it uses AI

The EPFL research module trains and integrates object and pose models for woodworking tools in the Augmented Carpentry setup. [Source](https://github.com/ibois-epfl/TTool-ai/blob/main/README.md) [Source](https://www.epfl.ch/labs/ibois/augmented-carpentry/) [Source](https://github.com/ibois-epfl/TTool-ai/wiki)

### Introduction

The EPFL research module trains and integrates object and pose models for woodworking tools in the Augmented Carpentry setup. [Source 1](https://github.com/ibois-epfl/TTool-ai/blob/main/README.md) [Source 2](https://www.epfl.ch/labs/ibois/augmented-carpentry/) [Source 3](https://github.com/ibois-epfl/TTool-ai/wiki)

### What it is good for

Prepare an AR visualization of a named woodworking tool and assess how consistently it aligns in a bench demonstration. [Source 1](https://github.com/ibois-epfl/TTool-ai/blob/main/README.md) [Source 2](https://www.epfl.ch/labs/ibois/augmented-carpentry/) [Source 3](https://github.com/ibois-epfl/TTool-ai/wiki)

### Demo & examples

The lab links the project to its Augmented Carpentry work and documents a training service. Current demo availability and alignment quality need independent checks. [Source 1](https://github.com/ibois-epfl/TTool-ai/blob/main/README.md) [Source 2](https://www.epfl.ch/labs/ibois/augmented-carpentry/) [Source 3](https://github.com/ibois-epfl/TTool-ai/wiki)

### Install

Follow the documented route for the scoped workflow. The steps below are source references. [Source 1](https://github.com/ibois-epfl/TTool-ai/blob/main/README.md) [Source 2](https://www.epfl.ch/labs/ibois/augmented-carpentry/) [Source 3](https://github.com/ibois-epfl/TTool-ai/wiki)

1. For the documented server route use Ubuntu 20.04 with NVIDIA runtime, Docker and Docker Compose.
2. Follow the project’s service and dataset setup. Establish access to the separately documented Augmented Carpentry runtime before training.
### First project

A small first project makes the input, model output and handoff easy to inspect. [Source 1](https://github.com/ibois-epfl/TTool-ai/blob/main/README.md) [Source 2](https://www.epfl.ch/labs/ibois/augmented-carpentry/) [Source 3](https://github.com/ibois-epfl/TTool-ai/wiki)

1. Begin with one supported tool and a small annotated input set. Train or import only the selected detection model.
2. Compare predicted alignment against captured reference views. Review occlusion and model misses in the visualization before any real-world deployment.
### Hardware & software

Platform and compute constraints refer to the selected route. [Source 1](https://github.com/ibois-epfl/TTool-ai/blob/main/README.md) [Source 2](https://www.epfl.ch/labs/ibois/augmented-carpentry/) [Source 3](https://github.com/ibois-epfl/TTool-ai/wiki)

- **Hardware:** Minimum RAM, VRAM and disk space for the scoped workflow are undocumented.
- **Software:** FastAPI, Docker and Compose with NVIDIA runtime, PyTorch training and separate Augmented Carpentry software.
- **Platforms:** Developer-tested Linux Ubuntu 20.04 with NVIDIA GPU. No equivalent Mac or Windows training setup was confirmed.

### License, model weights & costs

The full software license was reviewed. Dependencies and creative assets carry their own terms. [Source 1](https://github.com/ibois-epfl/TTool-ai/blob/main/LICENSE) [Source 2](https://github.com/ibois-epfl/TTool-ai/blob/main/README.md) [Source 3](https://www.epfl.ch/labs/ibois/augmented-carpentry/) [Source 4](https://github.com/ibois-epfl/TTool-ai/wiki)

- **Code:** GPL-3.0
- **Weights:** The complete GPLv3 project file was reviewed. The parent AR runtime, sample assets and trained checkpoints have separate terms.
- **Commercial:** Project code is governed by GPL-3.0. Confirm selected model, source-media and output restrictions separately.
- **Cost:** The self-hosted training workflow requires local GPU time or compatible compute. The lab service’s availability and access are separate.

### Why it merits attention

The creative workflow is grounded in the cited documentation. Output quality and compatibility are not hands-on verified. [Source 1](https://github.com/ibois-epfl/TTool-ai/blob/main/README.md) [Source 2](https://www.epfl.ch/labs/ibois/augmented-carpentry/) [Source 3](https://github.com/ibois-epfl/TTool-ai/wiki)

### Limitations

Tracking a tool for visualization does not validate mechanical accuracy, user operation or fabrication safety. Keep the initial result a supervised demonstration. [Source 1](https://github.com/ibois-epfl/TTool-ai/blob/main/README.md) [Source 2](https://www.epfl.ch/labs/ibois/augmented-carpentry/) [Source 3](https://github.com/ibois-epfl/TTool-ai/wiki)

### Get the tool

- [Repository](https://github.com/ibois-epfl/TTool-ai)
- [Documentation](https://github.com/ibois-epfl/TTool-ai/wiki)

## IgniteFuse

3D printing & generative CAD · AI-assisted textile and computational craft · 3D, reconstruction & assets

This completes an earlier pending guide with a current source review.

### Quality assessment: Experimental

Creative use and the code grant are documented. Check-level gaps remain before a recommendation.

Scope: Assess an AI-assisted toolpath sketch in a local preview, using the same reproducible project files and reviewing every machine-dependent parameter.

Evidence checked: 2026-11-21. No local execution implied.

Why Experimental: The maintainer labels the current release beta and explicitly says that toolpaths, presets, project format and G-code can change and operation is not guaranteed. https://github.com/tokoshie3d/IgniteFuse/blob/main/README.md

- **Open-source software license · verified:** Reviewed the complete project software grant and its redistribution conditions. Model, data and service terms are scoped separately. [Source](https://github.com/tokoshie3d/IgniteFuse/blob/main/LICENSE)
- **Creative results · documented:** The README documents STL import, runnable stages, diagnostic output and a G-code export. It explicitly warns that beta outputs can change. [Source](https://github.com/tokoshie3d/IgniteFuse/blob/main/README.md) [Source](https://github.com/tokoshie3d/IgniteFuse/blob/main/docs/project-format.md)
- **Reproducible setup · documented:** The installation and first-use steps are in the cited documentation. Reproduction of this workflow remains unverified. [Source](https://github.com/tokoshie3d/IgniteFuse/blob/main/README.md) [Source](https://github.com/tokoshie3d/IgniteFuse/blob/main/docs/project-format.md)
- **Maintenance and support · unknown:** The reviewed sources do not establish workflow-specific support, fixes and unresolved blockers.
- **Independent use · unknown:** Independent first-hand use of the exact workflow was not established in this source review.
- **Models, services and costs · documented:** Apache-2.0 covers IgniteFuse. Host agent models, imported meshes and any third-party integration remain separate. The local studio can run without a metered call. A connected agent or external CAD service can add cost. [Source](https://github.com/tokoshie3d/IgniteFuse/blob/main/README.md) [Source](https://github.com/tokoshie3d/IgniteFuse/blob/main/docs/project-format.md)

Source and documentation review. No hands-on execution by AI Media Scout. Current beta APIs, project formats and G-code are subject to change. Simulated appearance cannot establish printer-safe output.

### How it uses AI

The local slicer exposes its active JavaScript project, scene and generated-toolpath operations through an MCP interface for an external code agent. [Source](https://github.com/tokoshie3d/IgniteFuse/blob/main/README.md) [Source](https://github.com/tokoshie3d/IgniteFuse/blob/main/docs/project-format.md)

### Introduction

The local slicer exposes its active JavaScript project, scene and generated-toolpath operations through an MCP interface for an external code agent. [Source 1](https://github.com/tokoshie3d/IgniteFuse/blob/main/README.md) [Source 2](https://github.com/tokoshie3d/IgniteFuse/blob/main/docs/project-format.md)

### What it is good for

Assess an AI-assisted toolpath sketch in a local preview, using the same reproducible project files and reviewing every machine-dependent parameter. [Source 1](https://github.com/tokoshie3d/IgniteFuse/blob/main/README.md) [Source 2](https://github.com/tokoshie3d/IgniteFuse/blob/main/docs/project-format.md)

### Demo & examples

The README documents STL import, runnable stages, diagnostic output and a G-code export. It explicitly warns that beta outputs can change. [Source 1](https://github.com/tokoshie3d/IgniteFuse/blob/main/README.md) [Source 2](https://github.com/tokoshie3d/IgniteFuse/blob/main/docs/project-format.md)

### Install

Follow the documented route for the scoped workflow. The steps below are source references. [Source 1](https://github.com/tokoshie3d/IgniteFuse/blob/main/README.md) [Source 2](https://github.com/tokoshie3d/IgniteFuse/blob/main/docs/project-format.md)

1. Use Node.js 18 or newer on a supported local environment and the published npm package.
2. Create a local project and launch its studio. Add the documented MCP connection only if you want a separate agent to access the test project.

```sh
npm install -g ignitefuse
```


```sh
ignitefuse create ./my-print
```


```sh
ignitefuse ./my-print
```

### First project

A small first project makes the input, model output and handoff easy to inspect. [Source 1](https://github.com/tokoshie3d/IgniteFuse/blob/main/README.md) [Source 2](https://github.com/tokoshie3d/IgniteFuse/blob/main/docs/project-format.md)

1. Load a test mesh and inspect the scene before generation. Ask the connected agent for a small adjustment and review its code diff.
2. Inspect the toolpath preview and diagnostic messages. Retain a copy of configuration and evaluate generated machine instructions independently.
### Hardware & software

Platform and compute constraints refer to the selected route. [Source 1](https://github.com/tokoshie3d/IgniteFuse/blob/main/README.md) [Source 2](https://github.com/tokoshie3d/IgniteFuse/blob/main/docs/project-format.md)

- **Hardware:** Minimum RAM, VRAM and disk space for the scoped workflow are undocumented.
- **Software:** Node.js 18+ and a browser. Optional creative agent needs a compatible MCP client and its own model. The separate Ignite0 service is not part of this local scope.
- **Platforms:** The native requirements are stated for Node.js and a browser. A per-OS and printer compatibility matrix was not established.

### License, model weights & costs

The full software license was reviewed. Dependencies and creative assets carry their own terms. [Source 1](https://github.com/tokoshie3d/IgniteFuse/blob/main/LICENSE) [Source 2](https://github.com/tokoshie3d/IgniteFuse/blob/main/README.md) [Source 3](https://github.com/tokoshie3d/IgniteFuse/blob/main/docs/project-format.md)

- **Code:** Apache-2.0
- **Weights:** Apache-2.0 covers IgniteFuse. Host agent models, imported meshes and any third-party integration remain separate.
- **Commercial:** Project code is governed by Apache-2.0. Confirm selected model, source-media and output restrictions separately.
- **Cost:** The local studio can run without a metered call. A connected agent or external CAD service can add cost.

### Why it merits attention

The creative workflow is grounded in the cited documentation. Output quality and compatibility are not hands-on verified. [Source 1](https://github.com/tokoshie3d/IgniteFuse/blob/main/README.md) [Source 2](https://github.com/tokoshie3d/IgniteFuse/blob/main/docs/project-format.md)

### Limitations

Current beta APIs, project formats and G-code are subject to change. Simulated appearance cannot establish printer-safe output. [Source 1](https://github.com/tokoshie3d/IgniteFuse/blob/main/README.md) [Source 2](https://github.com/tokoshie3d/IgniteFuse/blob/main/docs/project-format.md)

### Get the tool

- [Repository](https://github.com/tokoshie3d/IgniteFuse)
- [Documentation](https://github.com/tokoshie3d/IgniteFuse/blob/main/docs/project-format.md)

## Additional open-source AI discoveries

Creative AI relevance and software license screened. Full installation, requirements and quality profiles are pending.

### audio-cpp-rs · Apache-2.0

Prototype a local audio-production component with one pinned model and backend before embedding it in a creator tool.
The library binds a ggml-based local audio engine with explicit speech and sound-model families, including narration, transcription and source separation.
Complete Apache-2.0 software terms and callable pipeline were reviewed. Model-family runtime compatibility, bundled third-party components and actual outputs need a full guide.

### Quality assessment: Quality unverified

Concrete creative AI use and complete code license reviewed. Full guide and quality evidence remain pending.

Scope: Prototype a local audio-production component with one pinned model and backend before embedding it in a creator tool.

Evidence checked: 2026-11-21. No local execution implied.

- **Open-source software license · verified:** Read and archived the complete software license, including its terms and notices. [Source](https://github.com/launcher-rs/audio-cpp-rs/blob/main/LICENSE)
- **Creative results · unknown:** No sufficiently scoped result evaluation established.
- **Reproducible setup · unknown:** First-use installation and runtime checks need a complete guide.
- **Maintenance and support · unknown:** Support and open blockers need an evidence review.
- **Independent use · unknown:** Independent use or reproducible integration remains unverified.
- **Models, services and costs · documented:** Complete Apache-2.0 software terms and callable pipeline were reviewed. Model-family runtime compatibility, bundled third-party components and actual outputs need a full guide. [Source](https://github.com/launcher-rs/audio-cpp-rs/blob/main/README.md) [Source](https://github.com/launcher-rs/audio-cpp-rs/blob/main/docs/models.md)

Source review. No installation or output testing by AI Media Scout. Complete Apache-2.0 software terms and callable pipeline were reviewed. Model-family runtime compatibility, bundled third-party components and actual outputs need a full guide.

- [Official project documentation](https://github.com/launcher-rs/audio-cpp-rs/blob/main/README.md)
- [Complete software license reviewed](https://github.com/launcher-rs/audio-cpp-rs/blob/main/LICENSE)
- [Published release notes](https://github.com/launcher-rs/audio-cpp-rs/releases/tag/v0.10.0)
- [Model catalogue](https://github.com/launcher-rs/audio-cpp-rs/blob/main/docs/models.md)
### AI Texture Pipeline on Nosana · MIT

Screen a model-assisted material map produced for a game environment before DCC or engine review.
The project orchestrates generation of PBR textures for game assets using a model-backed GPU pipeline and saves the generated material maps for downstream use.
The project code license and creative task were reviewed. Exact model terms, Nosana costs and Arweave storage implications remain open. Reproduce the map-generation path before relying on benchmark claims.

### Quality assessment: Quality unverified

Concrete creative AI use and complete code license reviewed. Full guide and quality evidence remain pending.

Scope: Screen a model-assisted material map produced for a game environment before DCC or engine review.

Evidence checked: 2026-11-21. No local execution implied.

- **Open-source software license · verified:** Read and archived the complete software license, including its terms and notices. [Source](https://github.com/EachoneInformationChannel/AI-Texture-Pipeline-Nosana/blob/main/LICENSE)
- **Creative results · unknown:** No sufficiently scoped result evaluation established.
- **Reproducible setup · unknown:** First-use installation and runtime checks need a complete guide.
- **Maintenance and support · unknown:** Support and open blockers need an evidence review.
- **Independent use · unknown:** Independent use or reproducible integration remains unverified.
- **Models, services and costs · documented:** The project code license and creative task were reviewed. Exact model terms, Nosana costs and Arweave storage implications remain open. Reproduce the map-generation path before relying on benchmark claims. [Source](https://github.com/EachoneInformationChannel/AI-Texture-Pipeline-Nosana/blob/main/README.md)

Source review. No installation or output testing by AI Media Scout. The project code license and creative task were reviewed. Exact model terms, Nosana costs and Arweave storage implications remain open. Reproduce the map-generation path before relying on benchmark claims.

- [Official project documentation](https://github.com/EachoneInformationChannel/AI-Texture-Pipeline-Nosana/blob/main/README.md)
- [Complete software license reviewed](https://github.com/EachoneInformationChannel/AI-Texture-Pipeline-Nosana/blob/main/LICENSE)
### WavLM French Speech Vocoder · MIT

Compare short French reconstruction samples for a research-oriented sound and language workflow.
The project explores mapping WavLM representations back to speech audio through a learned vocoder trained for a French speech setting.
MIT code and the model, speech and reconstruction scope are documented. Complete checkpoint, dataset, licensing and export reproduction checks remain open.

### Quality assessment: Quality unverified

Concrete creative AI use and complete code license reviewed. Full guide and quality evidence remain pending.

Scope: Compare short French reconstruction samples for a research-oriented sound and language workflow.

Evidence checked: 2026-11-21. No local execution implied.

- **Open-source software license · verified:** Read and archived the complete software license, including its terms and notices. [Source](https://github.com/hi-paris/wavlm-vocoder-french/blob/main/LICENSE)
- **Creative results · unknown:** No sufficiently scoped result evaluation established.
- **Reproducible setup · unknown:** First-use installation and runtime checks need a complete guide.
- **Maintenance and support · unknown:** Support and open blockers need an evidence review.
- **Independent use · unknown:** Independent use or reproducible integration remains unverified.
- **Models, services and costs · documented:** MIT code and the model, speech and reconstruction scope are documented. Complete checkpoint, dataset, licensing and export reproduction checks remain open. [Source](https://github.com/hi-paris/wavlm-vocoder-french/blob/main/README.md)

Source review. No installation or output testing by AI Media Scout. MIT code and the model, speech and reconstruction scope are documented. Complete checkpoint, dataset, licensing and export reproduction checks remain open.

- [Official project documentation](https://github.com/hi-paris/wavlm-vocoder-french/blob/main/README.md)
- [Complete software license reviewed](https://github.com/hi-paris/wavlm-vocoder-french/blob/main/LICENSE)
### Signo · MIT

Review a constrained alphabet practice demonstration with an experienced language instructor.
Signo uses MediaPipe landmarks and TensorFlow.js classification to compare Greek Sign Language practice gestures with a browser-based guide.
The full permissive code grant was reviewed. Instructor validation, exact gesture-model training/data terms and cross-browser performance need follow-up.

### Quality assessment: Quality unverified

Concrete creative AI use and complete code license reviewed. Full guide and quality evidence remain pending.

Scope: Review a constrained alphabet practice demonstration with an experienced language instructor.

Evidence checked: 2026-11-21. No local execution implied.

- **Open-source software license · verified:** Read and archived the complete software license, including its terms and notices. [Source](https://github.com/seograth/signo/blob/main/LICENSE)
- **Creative results · documented:** The upstream shows a browser demonstration and describes a constrained letter workflow. [Source](https://github.com/seograth/signo/blob/main/README.md)
- **Reproducible setup · unknown:** First-use installation and runtime checks need a complete guide.
- **Maintenance and support · unknown:** Support and open blockers need an evidence review.
- **Independent use · unknown:** Independent use or reproducible integration remains unverified.
- **Models, services and costs · documented:** The full permissive code grant was reviewed. Instructor validation, exact gesture-model training/data terms and cross-browser performance need follow-up. [Source](https://github.com/seograth/signo/blob/main/README.md)

Source review. No installation or output testing by AI Media Scout. The full permissive code grant was reviewed. Instructor validation, exact gesture-model training/data terms and cross-browser performance need follow-up.

- [Official project documentation](https://github.com/seograth/signo/blob/main/README.md)
- [Complete software license reviewed](https://github.com/seograth/signo/blob/main/LICENSE)
### AI Subtitle Generator · MIT

Prepare a draft timed translation for a short clip before language and timing review.
The Python project documents Whisper transcription from audio/video and an optional language-model translation route for editable captions.
The MIT code grant and caption workflow were reviewed. Exact setup, selected models and provider terms need a complete guide.

### Quality assessment: Quality unverified

Concrete creative AI use and complete code license reviewed. Full guide and quality evidence remain pending.

Scope: Prepare a draft timed translation for a short clip before language and timing review.

Evidence checked: 2026-11-21. No local execution implied.

- **Open-source software license · verified:** Read and archived the complete software license, including its terms and notices. [Source](https://github.com/ZoraZora59/ai-subtitle-generator/blob/master/LICENSE)
- **Creative results · unknown:** No sufficiently scoped result evaluation established.
- **Reproducible setup · unknown:** First-use installation and runtime checks need a complete guide.
- **Maintenance and support · unknown:** Support and open blockers need an evidence review.
- **Independent use · unknown:** Independent use or reproducible integration remains unverified.
- **Models, services and costs · documented:** The MIT code grant and caption workflow were reviewed. Exact setup, selected models and provider terms need a complete guide. [Source](https://github.com/ZoraZora59/ai-subtitle-generator/blob/master/README.md)

Source review. No installation or output testing by AI Media Scout. The MIT code grant and caption workflow were reviewed. Exact setup, selected models and provider terms need a complete guide.

- [Official project documentation](https://github.com/ZoraZora59/ai-subtitle-generator/blob/master/README.md)
- [Complete software license reviewed](https://github.com/ZoraZora59/ai-subtitle-generator/blob/master/LICENSE)
- [Published release notes](https://github.com/ZoraZora59/ai-subtitle-generator/releases/tag/v1.1)
### Kaijing · LGPL-2.1

Screen a small scene generation and storyboard iteration in the self-hosted source workflow.
The project documents a model-backed short-drama workstation that creates scripts and scene assets and manages generated image/video drafts.
The complete LGPL software grant and the production-facing workflow were reviewed. Model and distribution conditions, export and runtime need a full guide.

### Quality assessment: Quality unverified

Concrete creative AI use and complete code license reviewed. Full guide and quality evidence remain pending.

Scope: Screen a small scene generation and storyboard iteration in the self-hosted source workflow.

Evidence checked: 2026-11-21. No local execution implied.

- **Open-source software license · verified:** Read and archived the complete software license, including its terms and notices. [Source](https://github.com/openroute-ai/vercelai-kaijing/blob/main/LICENSE)
- **Creative results · unknown:** No sufficiently scoped result evaluation established.
- **Reproducible setup · unknown:** First-use installation and runtime checks need a complete guide.
- **Maintenance and support · unknown:** Support and open blockers need an evidence review.
- **Independent use · unknown:** Independent use or reproducible integration remains unverified.
- **Models, services and costs · documented:** The complete LGPL software grant and the production-facing workflow were reviewed. Model and distribution conditions, export and runtime need a full guide. [Source](https://github.com/openroute-ai/vercelai-kaijing/blob/main/README.md)

Source review. No installation or output testing by AI Media Scout. The complete LGPL software grant and the production-facing workflow were reviewed. Model and distribution conditions, export and runtime need a full guide.

- [Official project documentation](https://github.com/openroute-ai/vercelai-kaijing/blob/main/README.md)
- [Complete software license reviewed](https://github.com/openroute-ai/vercelai-kaijing/blob/main/LICENSE)
### Desktop Buddy · Apache-2.0

Screen an interactive talking character as a small installation or streaming layer.
The project documents a desktop character framework with model-assisted speech processing and controls for a separate animated puppet rig.
The Apache-2.0 code grant and model-backed prototype were reviewed. Dependent TTS/ASR, rig rights and usable output capture remain to be checked.

### Quality assessment: Quality unverified

Concrete creative AI use and complete code license reviewed. Full guide and quality evidence remain pending.

Scope: Screen an interactive talking character as a small installation or streaming layer.

Evidence checked: 2026-11-21. No local execution implied.

- **Open-source software license · verified:** Read and archived the complete software license, including its terms and notices. [Source](https://github.com/dunkzinski/desktop-buddy/blob/main/LICENSE)
- **Creative results · unknown:** No sufficiently scoped result evaluation established.
- **Reproducible setup · unknown:** First-use installation and runtime checks need a complete guide.
- **Maintenance and support · unknown:** Support and open blockers need an evidence review.
- **Independent use · unknown:** Independent use or reproducible integration remains unverified.
- **Models, services and costs · documented:** The Apache-2.0 code grant and model-backed prototype were reviewed. Dependent TTS/ASR, rig rights and usable output capture remain to be checked. [Source](https://github.com/dunkzinski/desktop-buddy/blob/main/README.md)

Source review. No installation or output testing by AI Media Scout. The Apache-2.0 code grant and model-backed prototype were reviewed. Dependent TTS/ASR, rig rights and usable output capture remain to be checked.

- [Official project documentation](https://github.com/dunkzinski/desktop-buddy/blob/main/README.md)
- [Complete software license reviewed](https://github.com/dunkzinski/desktop-buddy/blob/main/LICENSE)
- [Published release notes](https://github.com/dunkzinski/desktop-buddy/releases/tag/v0.2.0)
### Arm Compute Flow Bricks · Apache-2.0

Explore a pinned mobile speech or depth component before building an offline accessibility or imaging workflow.
Arm’s Apache-licensed reference components include neural TTS and monocular depth blocks for creative-media processing pipelines.
Each brick has runtime and model dependencies. The Arm Qwen3-TTS evaluation covers one Vivo X300 configuration. A complete graph, weight terms, setup and independent integrated use remain to be reviewed.

### Quality assessment: Quality unverified

Concrete creative AI use and complete code license reviewed. Full guide and quality evidence remain pending.

Scope: Explore a pinned mobile speech or depth component before building an offline accessibility or imaging workflow.

Evidence checked: 2026-11-21. No local execution implied.

- **Open-source software license · verified:** Read and archived the complete software license, including its terms and notices. [Source](https://github.com/ARM-software/compute-flow-bricks/blob/main/LICENSE)
- **Creative results · unknown:** No sufficiently scoped result evaluation established.
- **Reproducible setup · unknown:** First-use installation and runtime checks need a complete guide.
- **Maintenance and support · unknown:** Support and open blockers need an evidence review.
- **Independent use · unknown:** Independent use or reproducible integration remains unverified.
- **Models, services and costs · documented:** Each brick has runtime and model dependencies. The Arm Qwen3-TTS evaluation covers one Vivo X300 configuration. A complete graph, weight terms, setup and independent integrated use remain to be reviewed. [Source](https://github.com/ARM-software/compute-flow-bricks/blob/main/README.md) [Source](https://huggingface.co/Arm/qwen3-tts-0-6b-custom-voice-mix-precision) [Source](https://github.com/ARM-software/compute-flow/blob/main/README.md)

Source review. No installation or output testing by AI Media Scout. Each brick has runtime and model dependencies. The Arm Qwen3-TTS evaluation covers one Vivo X300 configuration. A complete graph, weight terms, setup and independent integrated use remain to be reviewed.

- [Official project documentation](https://github.com/ARM-software/compute-flow-bricks/blob/main/README.md)
- [Complete software license reviewed](https://github.com/ARM-software/compute-flow-bricks/blob/main/LICENSE)
- [Published release notes](https://github.com/ARM-software/compute-flow-bricks/releases/tag/1.0.0)
- [Arm Qwen3-TTS model card and evaluation](https://huggingface.co/Arm/qwen3-tts-0-6b-custom-voice-mix-precision)
- [Compute Flow runtime and supported routes](https://github.com/ARM-software/compute-flow/blob/main/README.md)
### ScriptVEdit · MIT

Screen a scripted short animation or narrated picture sequence that remains editable as a timeline.
An agent can write and revise the Python timeline DSL for an editable video. The source also documents optional neural speech and separate Blender puppet rendering paths.
MIT core terms and its creative authoring scope were reviewed. The Blender worker is separately GPL-3.0-or-later. Provider, exact accessible features and runtime checks need a complete guide.

### Quality assessment: Quality unverified

Concrete creative AI use and complete code license reviewed. Full guide and quality evidence remain pending.

Scope: Screen a scripted short animation or narrated picture sequence that remains editable as a timeline.

Evidence checked: 2026-11-21. No local execution implied.

- **Open-source software license · verified:** Read and archived the complete software license, including its terms and notices. [Source](https://github.com/kojima8924/ScriptVEdit/blob/master/LICENSE)
- **Creative results · unknown:** No sufficiently scoped result evaluation established.
- **Reproducible setup · unknown:** First-use installation and runtime checks need a complete guide.
- **Maintenance and support · unknown:** Support and open blockers need an evidence review.
- **Independent use · unknown:** Independent use or reproducible integration remains unverified.
- **Models, services and costs · documented:** MIT core terms and its creative authoring scope were reviewed. The Blender worker is separately GPL-3.0-or-later. Provider, exact accessible features and runtime checks need a complete guide. [Source](https://github.com/kojima8924/ScriptVEdit/blob/master/README.md)

Source review. No installation or output testing by AI Media Scout. MIT core terms and its creative authoring scope were reviewed. The Blender worker is separately GPL-3.0-or-later. Provider, exact accessible features and runtime checks need a complete guide.

- [Official project documentation](https://github.com/kojima8924/ScriptVEdit/blob/master/README.md)
- [Complete software license reviewed](https://github.com/kojima8924/ScriptVEdit/blob/master/LICENSE)
### motion-kit · MIT

Screen an agent-driven kinetic typography or pixel-animation draft with its code retained for further editing.
The motion-kit supplies an agent-oriented authoring library and source rendering runtime for editable frames and sequences rather than only a rendered clip.
The MIT project software and actual renderer were identified. Complete runtime, model host, font/asset and render parity checks remain pending.

### Quality assessment: Quality unverified

Concrete creative AI use and complete code license reviewed. Full guide and quality evidence remain pending.

Scope: Screen an agent-driven kinetic typography or pixel-animation draft with its code retained for further editing.

Evidence checked: 2026-11-21. No local execution implied.

- **Open-source software license · verified:** Read and archived the complete software license, including its terms and notices. [Source](https://github.com/kiselas/every-frame-is-code/blob/main/LICENSE)
- **Creative results · unknown:** No sufficiently scoped result evaluation established.
- **Reproducible setup · unknown:** First-use installation and runtime checks need a complete guide.
- **Maintenance and support · unknown:** Support and open blockers need an evidence review.
- **Independent use · unknown:** Independent use or reproducible integration remains unverified.
- **Models, services and costs · documented:** The MIT project software and actual renderer were identified. Complete runtime, model host, font/asset and render parity checks remain pending. [Source](https://github.com/kiselas/every-frame-is-code/blob/main/README.md)

Source review. No installation or output testing by AI Media Scout. The MIT project software and actual renderer were identified. Complete runtime, model host, font/asset and render parity checks remain pending.

- [Official project documentation](https://github.com/kiselas/every-frame-is-code/blob/main/README.md)
- [Complete software license reviewed](https://github.com/kiselas/every-frame-is-code/blob/main/LICENSE)
- [Published release notes](https://github.com/kiselas/every-frame-is-code/releases/tag/v1.2.0)
### OCR4all · MIT

Screen a small printed-archive OCR route that keeps editorial intervention in the workflow.
OCR4all assembles OCR and page-analysis components for semi-automatic recognition of historical prints with manual correction.
The software grant and maintained interface are documented. First-use Docker bundle support, individual OCR models and independent output review need a complete guide. Upstream development moved to LAREX.

### Quality assessment: Quality unverified

Concrete creative AI use and complete code license reviewed. Full guide and quality evidence remain pending.

Scope: Screen a small printed-archive OCR route that keeps editorial intervention in the workflow.

Evidence checked: 2026-11-21. No local execution implied.

- **Open-source software license · verified:** Read and archived the complete software license, including its terms and notices. [Source](https://github.com/OCR4all/OCR4all/blob/master/LICENSE)
- **Creative results · unknown:** No sufficiently scoped result evaluation established.
- **Reproducible setup · unknown:** First-use installation and runtime checks need a complete guide.
- **Maintenance and support · unknown:** Support and open blockers need an evidence review.
- **Independent use · unknown:** Independent use or reproducible integration remains unverified.
- **Models, services and costs · documented:** The software grant and maintained interface are documented. First-use Docker bundle support, individual OCR models and independent output review need a complete guide. Upstream development moved to LAREX. [Source](https://github.com/OCR4all/OCR4all/blob/master/README.md) [Source](https://github.com/OCR4all/docker_image)

Source review. No installation or output testing by AI Media Scout. The software grant and maintained interface are documented. First-use Docker bundle support, individual OCR models and independent output review need a complete guide. Upstream development moved to LAREX.

- [Official project documentation](https://github.com/OCR4all/OCR4all/blob/master/README.md)
- [Complete software license reviewed](https://github.com/OCR4all/OCR4all/blob/master/LICENSE)
- [Published release notes](https://github.com/OCR4all/OCR4all/releases/tag/0.6.1)
- [Official Docker distribution](https://github.com/OCR4all/docker_image)
### Whisper for Android · MIT

Dictate short oral-history notes or caption corrections directly into an editable Android text field.
Whisper’s standalone app and Android keyboard use on-device speech recognition and support a separate mode for translation to English.
Recordings are limited to about 30 seconds per input. F-Droid lists Android 9 or later. Review model terms, text handling and repeated short-segment setup for an editorial guide.

### Quality assessment: Quality unverified

Concrete creative AI use and complete code license reviewed. Full guide and quality evidence remain pending.

Scope: Dictate short oral-history notes or caption corrections directly into an editable Android text field.

Evidence checked: 2026-11-21. No local execution implied.

- **Open-source software license · verified:** Read and archived the complete software license, including its terms and notices. [Source](https://github.com/woheller69/whisperIME/blob/master/LICENSE)
- **Creative results · documented:** The developer shows the editable text interface and describes its standalone translation mode. [Source](https://github.com/woheller69/whisperIME/blob/master/README.md) [Source](https://f-droid.org/en/packages/org.woheller69.whisper/)
- **Reproducible setup · documented:** The author documents an initial model download. The app has both standalone and input-method paths. [Source](https://github.com/woheller69/whisperIME/blob/master/README.md) [Source](https://f-droid.org/en/packages/org.woheller69.whisper/)
- **Maintenance and support · unknown:** Support and open blockers need an evidence review.
- **Independent use · unknown:** Independent use or reproducible integration remains unverified.
- **Models, services and costs · documented:** Recordings are limited to about 30 seconds per input. F-Droid lists Android 9 or later. Review model terms, text handling and repeated short-segment setup for an editorial guide. [Source](https://github.com/woheller69/whisperIME/blob/master/README.md) [Source](https://f-droid.org/en/packages/org.woheller69.whisper/)

Source review. No installation or output testing by AI Media Scout. Recordings are limited to about 30 seconds per input. F-Droid lists Android 9 or later. Review model terms, text handling and repeated short-segment setup for an editorial guide.

- [Official project documentation](https://github.com/woheller69/whisperIME/blob/master/README.md)
- [Complete software license reviewed](https://github.com/woheller69/whisperIME/blob/master/LICENSE)
- [Published release notes](https://github.com/woheller69/whisperIME/releases/tag/V3.8)
- [F-Droid package, release history and source mapping](https://f-droid.org/en/packages/org.woheller69.whisper/)
### Whisper+ for Android · GPL-3.0-only

Generate draft edit notes in short takes during an authorized interview or recording review.
Whisper+ uses a Whisper implementation from the RTranslator project for local short speech transcription and English draft translation.
F-Droid documents the ARM64 Android package and short recording limit. A full guide should compare model terms, timing and Android input-method differences with the sibling app.

### Quality assessment: Quality unverified

Concrete creative AI use and complete code license reviewed. Full guide and quality evidence remain pending.

Scope: Generate draft edit notes in short takes during an authorized interview or recording review.

Evidence checked: 2026-11-21. No local execution implied.

- **Open-source software license · verified:** Read and archived the complete software license, including its terms and notices. [Source](https://github.com/woheller69/whisperIMEplus/blob/master/LICENSE)
- **Creative results · documented:** The documented standalone app writes editable short snippets. Long interview transcription is outside the scoped workflow. [Source](https://github.com/woheller69/whisperIMEplus/blob/master/README.md) [Source](https://f-droid.org/en/packages/org.woheller69.whisperplus/)
- **Reproducible setup · documented:** The selected package lists Android 9 or later. First use downloads a speech model from Hugging Face. [Source](https://github.com/woheller69/whisperIMEplus/blob/master/README.md) [Source](https://f-droid.org/en/packages/org.woheller69.whisperplus/)
- **Maintenance and support · unknown:** Support and open blockers need an evidence review.
- **Independent use · unknown:** Independent use or reproducible integration remains unverified.
- **Models, services and costs · documented:** F-Droid documents the ARM64 Android package and short recording limit. A full guide should compare model terms, timing and Android input-method differences with the sibling app. [Source](https://github.com/woheller69/whisperIMEplus/blob/master/README.md) [Source](https://f-droid.org/en/packages/org.woheller69.whisperplus/)

Source review. No installation or output testing by AI Media Scout. F-Droid documents the ARM64 Android package and short recording limit. A full guide should compare model terms, timing and Android input-method differences with the sibling app.

- [Official project documentation](https://github.com/woheller69/whisperIMEplus/blob/master/README.md)
- [Complete software license reviewed](https://github.com/woheller69/whisperIMEplus/blob/master/LICENSE)
- [Published release notes](https://github.com/woheller69/whisperIMEplus/releases/tag/V2.0)
- [F-Droid package, release history and source mapping](https://f-droid.org/en/packages/org.woheller69.whisperplus/)
### StrandHead · MIT

Assess whether separate hair geometry is useful for an editable character look-development study.
The research package generates text-conditioned 3D head avatars with a separately represented hair component and geometry priors.
The MIT project grant and creator-relevant method were reviewed. FLAME, third-party models and assets have separate terms. The documented Ubuntu/CUDA reproduction and actual DCC handoff need a complete guide.

### Quality assessment: Quality unverified

Concrete creative AI use and complete code license reviewed. Full guide and quality evidence remain pending.

Scope: Assess whether separate hair geometry is useful for an editable character look-development study.

Evidence checked: 2026-11-21. No local execution implied.

- **Open-source software license · verified:** Read and archived the complete software license, including its terms and notices. [Source](https://github.com/XiaokunSun/StrandHead/blob/main/LICENSE)
- **Creative results · documented:** The authors publish generated examples and identify a tested Ubuntu 20.04, A6000 and CUDA 11.7 setup. [Source](https://github.com/XiaokunSun/StrandHead/blob/main/README.md)
- **Reproducible setup · unknown:** First-use installation and runtime checks need a complete guide.
- **Maintenance and support · unknown:** Support and open blockers need an evidence review.
- **Independent use · unknown:** Independent use or reproducible integration remains unverified.
- **Models, services and costs · documented:** The MIT project grant and creator-relevant method were reviewed. FLAME, third-party models and assets have separate terms. The documented Ubuntu/CUDA reproduction and actual DCC handoff need a complete guide. [Source](https://github.com/XiaokunSun/StrandHead/blob/main/README.md)

Source review. No installation or output testing by AI Media Scout. The MIT project grant and creator-relevant method were reviewed. FLAME, third-party models and assets have separate terms. The documented Ubuntu/CUDA reproduction and actual DCC handoff need a complete guide.

- [Official project documentation](https://github.com/XiaokunSun/StrandHead/blob/main/README.md)
- [Complete software license reviewed](https://github.com/XiaokunSun/StrandHead/blob/main/LICENSE)
### NGCC-SELD · MIT

Explore directional event metadata for an installation audio map or a retrospective stage analysis.
The audio-only DCASE submission uses learned multi-target time-difference features to locate and classify events in spatial audio.
MIT project code and the research workflow are documented. The trained model, event formats, source-audio licensing and practical playback handoff need follow-up.

### Quality assessment: Quality unverified

Concrete creative AI use and complete code license reviewed. Full guide and quality evidence remain pending.

Scope: Explore directional event metadata for an installation audio map or a retrospective stage analysis.

Evidence checked: 2026-11-21. No local execution implied.

- **Open-source software license · verified:** Read and archived the complete software license, including its terms and notices. [Source](https://github.com/axeber01/ngcc-seld/blob/main/LICENSE)
- **Creative results · unknown:** No sufficiently scoped result evaluation established.
- **Reproducible setup · unknown:** First-use installation and runtime checks need a complete guide.
- **Maintenance and support · unknown:** Support and open blockers need an evidence review.
- **Independent use · unknown:** Independent use or reproducible integration remains unverified.
- **Models, services and costs · documented:** MIT project code and the research workflow are documented. The trained model, event formats, source-audio licensing and practical playback handoff need follow-up. [Source](https://github.com/axeber01/ngcc-seld/blob/main/README.md) [Source](https://dcase.community/documents/challenge2024/technical_reports/DCASE2024_Berg_24_t3.pdf)

Source review. No installation or output testing by AI Media Scout. MIT project code and the research workflow are documented. The trained model, event formats, source-audio licensing and practical playback handoff need follow-up.

- [Official project documentation](https://github.com/axeber01/ngcc-seld/blob/main/README.md)
- [Complete software license reviewed](https://github.com/axeber01/ngcc-seld/blob/main/LICENSE)
- [Primary DCASE technical report](https://dcase.community/documents/challenge2024/technical_reports/DCASE2024_Berg_24_t3.pdf)
### PSELDNets · MIT

Screen directional event extraction as an input to an audio-visual map, with a separate visual layer for editorial review.
The project publishes learned models intended to detect and localize sound events, along with the implementation for its synthetic spatial-audio study.
The complete software grant and audio-localization scope were reviewed. Check exact dataset, checkpoint, output event representation and runtime requirements before a production prototype.

### Quality assessment: Quality unverified

Concrete creative AI use and complete code license reviewed. Full guide and quality evidence remain pending.

Scope: Screen directional event extraction as an input to an audio-visual map, with a separate visual layer for editorial review.

Evidence checked: 2026-11-21. No local execution implied.

- **Open-source software license · verified:** Read and archived the complete software license, including its terms and notices. [Source](https://github.com/Jinbo-Hu/PSELDNets/blob/main/LICENSE)
- **Creative results · unknown:** No sufficiently scoped result evaluation established.
- **Reproducible setup · unknown:** First-use installation and runtime checks need a complete guide.
- **Maintenance and support · unknown:** Support and open blockers need an evidence review.
- **Independent use · unknown:** Independent use or reproducible integration remains unverified.
- **Models, services and costs · documented:** The complete software grant and audio-localization scope were reviewed. Check exact dataset, checkpoint, output event representation and runtime requirements before a production prototype. [Source](https://github.com/Jinbo-Hu/PSELDNets/blob/main/README.md)

Source review. No installation or output testing by AI Media Scout. The complete software grant and audio-localization scope were reviewed. Check exact dataset, checkpoint, output event representation and runtime requirements before a production prototype.

- [Official project documentation](https://github.com/Jinbo-Hu/PSELDNets/blob/main/README.md)
- [Complete software license reviewed](https://github.com/Jinbo-Hu/PSELDNets/blob/main/LICENSE)
### AI Video Director H5 · MIT

Screen an authoring path for editable shot prompts and handoff material before the first visual batch.
The project turns a short-drama concept into model-oriented storyboard and shot artifacts with a ComfyUI-oriented handoff.
MIT code and the creator workflow were reviewed. The precise model/provider path and whether the handoff reproduces the storyboard need a complete guide.

### Quality assessment: Quality unverified

Concrete creative AI use and complete code license reviewed. Full guide and quality evidence remain pending.

Scope: Screen an authoring path for editable shot prompts and handoff material before the first visual batch.

Evidence checked: 2026-11-21. No local execution implied.

- **Open-source software license · verified:** Read and archived the complete software license, including its terms and notices. [Source](https://github.com/fresh-bird-No1/ai-video-director-h5/blob/main/LICENSE)
- **Creative results · unknown:** No sufficiently scoped result evaluation established.
- **Reproducible setup · unknown:** First-use installation and runtime checks need a complete guide.
- **Maintenance and support · unknown:** Support and open blockers need an evidence review.
- **Independent use · unknown:** Independent use or reproducible integration remains unverified.
- **Models, services and costs · documented:** MIT code and the creator workflow were reviewed. The precise model/provider path and whether the handoff reproduces the storyboard need a complete guide. [Source](https://github.com/fresh-bird-No1/ai-video-director-h5/blob/main/README.md)

Source review. No installation or output testing by AI Media Scout. MIT code and the creator workflow were reviewed. The precise model/provider path and whether the handoff reproduces the storyboard need a complete guide.

- [Official project documentation](https://github.com/fresh-bird-No1/ai-video-director-h5/blob/main/README.md)
- [Complete software license reviewed](https://github.com/fresh-bird-No1/ai-video-director-h5/blob/main/LICENSE)
### Holo NeRF · MIT

Screen learned volumetric sampling from calibrated views for a separate holographic visualization study.
The code uses an orthogonal neural radiance field’s density output to predict spatial point-cloud data for holography experiments.
The full software license and experimental use were reviewed. The documented dependency file was unavailable and the trained scene model, display calibration and output setup need follow-up.

### Quality assessment: Quality unverified

Concrete creative AI use and complete code license reviewed. Full guide and quality evidence remain pending.

Scope: Screen learned volumetric sampling from calibrated views for a separate holographic visualization study.

Evidence checked: 2026-11-21. No local execution implied.

- **Open-source software license · verified:** Read and archived the complete software license, including its terms and notices. [Source](https://github.com/jgfranco17/holo-nerf/blob/main/LICENSE)
- **Creative results · unknown:** No sufficiently scoped result evaluation established.
- **Reproducible setup · unknown:** First-use installation and runtime checks need a complete guide.
- **Maintenance and support · unknown:** Support and open blockers need an evidence review.
- **Independent use · unknown:** Independent use or reproducible integration remains unverified.
- **Models, services and costs · documented:** The full software license and experimental use were reviewed. The documented dependency file was unavailable and the trained scene model, display calibration and output setup need follow-up. [Source](https://github.com/jgfranco17/holo-nerf/blob/main/README.md)

Source review. No installation or output testing by AI Media Scout. The full software license and experimental use were reviewed. The documented dependency file was unavailable and the trained scene model, display calibration and output setup need follow-up.

- [Official project documentation](https://github.com/jgfranco17/holo-nerf/blob/main/README.md)
- [Complete software license reviewed](https://github.com/jgfranco17/holo-nerf/blob/main/LICENSE)
### G-SELD · GPL-3.0

Screen a way to add estimated event directions to a separate audio-installation or recording annotation map.
The project uses trained temporal convolution and gammatone features to detect and locate sound events from spatial audio.
The complete GPLv3 source file and method were reviewed. Exact datasets, weights and output mapping to the intended playback system need a full guide.

### Quality assessment: Quality unverified

Concrete creative AI use and complete code license reviewed. Full guide and quality evidence remain pending.

Scope: Screen a way to add estimated event directions to a separate audio-installation or recording annotation map.

Evidence checked: 2026-11-21. No local execution implied.

- **Open-source software license · verified:** Read and archived the complete software license, including its terms and notices. [Source](https://github.com/kgrosero/G-SELD/blob/main/LICENSE)
- **Creative results · unknown:** No sufficiently scoped result evaluation established.
- **Reproducible setup · unknown:** First-use installation and runtime checks need a complete guide.
- **Maintenance and support · unknown:** Support and open blockers need an evidence review.
- **Independent use · unknown:** Independent use or reproducible integration remains unverified.
- **Models, services and costs · documented:** The complete GPLv3 source file and method were reviewed. Exact datasets, weights and output mapping to the intended playback system need a full guide. [Source](https://github.com/kgrosero/G-SELD/blob/main/README.md)

Source review. No installation or output testing by AI Media Scout. The complete GPLv3 source file and method were reviewed. Exact datasets, weights and output mapping to the intended playback system need a full guide.

- [Official project documentation](https://github.com/kgrosero/G-SELD/blob/main/README.md)
- [Complete software license reviewed](https://github.com/kgrosero/G-SELD/blob/main/LICENSE)
### Strata · MIT

Screen a hands-free music visualization where camera landmarks can move scene controls.
The browser scene uses MediaPipe’s face and hand landmarks for optional motion interaction with a music visualization. The audio-reactive mood features are documented separately as heuristic.
The MIT code and actual landmark use were reviewed. Browser/model terms and stage performance require follow-up. The optional learned audio embedding is a future extension.

### Quality assessment: Quality unverified

Concrete creative AI use and complete code license reviewed. Full guide and quality evidence remain pending.

Scope: Screen a hands-free music visualization where camera landmarks can move scene controls.

Evidence checked: 2026-11-21. No local execution implied.

- **Open-source software license · verified:** Read and archived the complete software license, including its terms and notices. [Source](https://github.com/nikhita265/strata-spatial/blob/main/LICENSE)
- **Creative results · unknown:** No sufficiently scoped result evaluation established.
- **Reproducible setup · unknown:** First-use installation and runtime checks need a complete guide.
- **Maintenance and support · unknown:** Support and open blockers need an evidence review.
- **Independent use · unknown:** Independent use or reproducible integration remains unverified.
- **Models, services and costs · documented:** The MIT code and actual landmark use were reviewed. Browser/model terms and stage performance require follow-up. The optional learned audio embedding is a future extension. [Source](https://github.com/nikhita265/strata-spatial/blob/main/README.md)

Source review. No installation or output testing by AI Media Scout. The MIT code and actual landmark use were reviewed. Browser/model terms and stage performance require follow-up. The optional learned audio embedding is a future extension.

- [Official project documentation](https://github.com/nikhita265/strata-spatial/blob/main/README.md)
- [Complete software license reviewed](https://github.com/nikhita265/strata-spatial/blob/main/LICENSE)
### Mocap · GPL-3.0

Screen a short motion study for use as inspectable reference in a separate animation rig.
The browser project uses BlazePose and MiDaS to estimate movement and depth from video and converts the recovered motion to BVH.
The GPLv3 license and public browser entry point are documented. Current browser/model requirements, export fidelity and practical retargeting need a full review.

### Quality assessment: Quality unverified

Concrete creative AI use and complete code license reviewed. Full guide and quality evidence remain pending.

Scope: Screen a short motion study for use as inspectable reference in a separate animation rig.

Evidence checked: 2026-11-21. No local execution implied.

- **Open-source software license · verified:** Read and archived the complete software license, including its terms and notices. [Source](https://github.com/ChristianVan391/mocap/blob/main/LICENSE)
- **Creative results · unknown:** No sufficiently scoped result evaluation established.
- **Reproducible setup · unknown:** First-use installation and runtime checks need a complete guide.
- **Maintenance and support · unknown:** Support and open blockers need an evidence review.
- **Independent use · unknown:** Independent use or reproducible integration remains unverified.
- **Models, services and costs · documented:** The GPLv3 license and public browser entry point are documented. Current browser/model requirements, export fidelity and practical retargeting need a full review. [Source](https://github.com/ChristianVan391/mocap/blob/main/README.md) [Source](https://christianvan391.github.io/mocap/)

Source review. No installation or output testing by AI Media Scout. The GPLv3 license and public browser entry point are documented. Current browser/model requirements, export fidelity and practical retargeting need a full review.

- [Official project documentation](https://github.com/ChristianVan391/mocap/blob/main/README.md)
- [Complete software license reviewed](https://github.com/ChristianVan391/mocap/blob/main/LICENSE)
- [Project browser entry point](https://christianvan391.github.io/mocap/)

Source collection completed: 2026-11-21T16:33:31.821306+00:00
Search is a bounded sample. Stars and recent pushes are discovery signals, not verified quality or meaningful upgrades.
