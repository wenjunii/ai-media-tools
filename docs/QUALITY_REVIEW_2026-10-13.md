# Quality evidence review — October 13, 2026

The library now has **3 Recommended, 4 Ready to try, 512 Quality unverified and
31 Experimental tools**. This pass updated 50 record-bound assessments and closed
26 individual evidence gaps. The library still contains 550 tools and 13 editions.

## Labels changed

| Tool and assessed workflow | Previous label | Current label | Evidence and limits |
| --- | --- | --- | --- |
| Depth Anything V2 Small — still-image relative-depth guidance | Ready to try | Recommended | Reviewed Small-model depth-order evaluation and its limitations; independent Transformers and ComfyUI implementations support setup/use. Dense reconstruction, metric variants and video consistency are excluded. |
| Whisper small/small.en — human-corrected draft English transcription | Ready to try | Recommended | Reviewed long-form transcription evaluation, decoding context and hallucination/error limits; independent Small-model reproduction supports the local route. Final captions require listening and correction. |
| SAM 2.1 Large — prompted masks and short-shot propagation | Quality unverified | Recommended | The revised paper explicitly evaluates SAM 2.1, with corrective prompts and tracking limitations. Independent predictor integration and checkpoint terms were reviewed. Shot changes and unattended long videos are excluded. |
| rembg — CPU inference with BiRefNet general-epoch_244 | Quality unverified | Ready to try | Inspected DiffSplat's actual rembg integration and resolved the selected model's terms. Exact-checkpoint cutout quality remains pending. |
| ComfyUI — built-in local SDXL Base 1.0 workflow | Quality unverified | Ready to try | Inspected Krita's implemented ComfyUI client, current fixes, setup and the complete SDXL model license. Other models, custom nodes and paid APIs are outside scope. |
| Chatterbox Turbo — English draft narration | Quality unverified | Ready to try | Inspected independent model loading, reference-audio handling and generation code; reviewed official Turbo terms and support limits. Listening quality remains pending. |
| Excalimate — browser animation/MCP authoring | Experimental | Quality unverified | Ongoing cleanup and bug fixing alone do not substantiate a prototype or unstable whole application. The other missing checks remain open. |
| FerroCut — current source-only editing engine | Quality unverified | Experimental | Current documentation identifies early software with changing interfaces, no release and unfinished operations. |
| Dralo Studio — R3 source-test build | Quality unverified | Experimental | The maintainer explicitly identifies an internal testing build with incomplete model/platform acceptance and a required upgrade path. |

These are workflow-specific judgments under the existing [quality policy](QUALITY_POLICY.md).
No star threshold, own-demo requirement or tier shortcut was introduced.

## What closed the result checks

The [Depth Anything V2 paper](https://arxiv.org/html/2406.09414v2) evaluates the
selected Small model using manually checked relative-depth pairs. Its sparse
ordering test is useful evidence for depth guidance, with explicit limits on
dense reconstruction accuracy.

The [Whisper paper](https://cdn.openai.com/papers/whisper.pdf) supplies long-form
English evaluation for small and small.en, with substantial dataset-dependent
errors. This supports human-reviewed draft transcription, not automatic final
caption acceptance.

The [revised SAM 2 paper](https://arxiv.org/html/2408.00714v2) identifies the
evaluated checkpoints as SAM 2.1 and documents interactive mask correction and
tracking failures. The assessment is scoped to that workflow.

BiRefNet remains **Ready to try**. Its [paper](https://arxiv.org/html/2401.03407v5)
evaluates task-specific training/checkpoints; the reviewed general-epoch_244
integration is a different checkpoint. Those scores do not close the exact-model
output gap. Neither paper links nor attractive sample links automatically pass
the results check.

## Other useful evidence and unresolved gaps

- **Nerfstudio:** the [NerfBaselines adapter](https://github.com/nerfbaselines/nerfbaselines/blob/main/nerfbaselines/methods/nerfstudio.py)
  and [pinned environment](https://github.com/nerfbaselines/nerfbaselines/blob/main/nerfbaselines/methods/nerfstudio_spec.py)
  establish independent implementation/reproduction. The
  [Nerfacto evaluation](https://arxiv.org/html/2302.04264v4) supports bounded
  novel-view studies. Current stack compatibility and exact dependency terms
  remain unresolved, so the overall label stays Quality unverified.
- **Krita AI Diffusion:** first-hand inpainting and outpainting reports support
  independent creative use. Stable/prerelease host versions, queue behavior and
  the complete selected model pack still need a matched review.
- **Upscayl, RIFE and RIFE NCNN:** concrete user reports establish independent
  creative use, while backend, output-save, model-version or support gaps remain.
  Those reports were not treated as universal successful setup or output tests.
- **Real-ESRGAN:** [issue 677](https://github.com/xinntao/Real-ESRGAN/issues/677)
  still has no maintainer clarification of the official checkpoint terms in the
  returned discussion. The BSD software license does not resolve that open question.
- **NeuralNote v2:** current documentation distinguishes Apache software from
  [non-commercial MuScriptor weights](https://github.com/DamRsn/NeuralNote#license).
  Windows crash/model-load reports remain. Basic Pitch evidence from older
  versions was not transferred to the new model.
- **Inkscape MCP adapter:** the complete updated license keeps the code MIT but
  [excludes Night Atlas artwork](https://github.com/dcc-mcp/dcc-mcp-inkscape/blob/main/tests/fixtures/night_atlas/LICENSES.md).
  The assessment now calls out that boundary.
- **Embedded Amp Model:** GitLab history is now readable. Synthetic amp error and
  modeled compute budgets do not establish a physically tested pedal.
- **AudioStellar:** fresh GitLab history shows concrete save/open and portability
  fixes; the current JUCE/Python setup is incomplete. The musical description
  “experimental sampler” does not determine the software label.
- **3D AR Studio:** added promotion links provide no independent implementation,
  output assessment or resolved hosted-service terms. It remains Quality unverified.

The 18 deeper follow-ups were Depth Anything V2, Whisper, BiRefNet, rembg, SAM 2,
Nerfstudio, ComfyUI, Chatterbox, the Inkscape adapter, Krita AI Diffusion,
NeuralNote, Upscayl, RIFE, RIFE NCNN, Real-ESRGAN, 3D AR Studio, Embedded Amp Model
and AudioStellar. Each retains all six checks with individual evidence statuses.

All 30 previous Experimental decisions received a current stage review. Twenty-nine
retained that label, with PeerBrush and Flameblade version descriptions corrected
to 0.25 and 0.3.0 respectively. Excalimate changed as described above. Those stage
reviews preserve the existing six-check findings and explicitly disclose their
limited scope. FerroCut and Dralo add two newly supported Experimental decisions.

## Coverage and remaining work

Source snapshots were refreshed for all 550 existing entries:

- 548 GitHub repositories: metadata, README, complete software license, up to
  five releases, ten commits and twenty recently updated issue-endpoint items.
  Pull requests share that endpoint; this is a bounded support sample.
- Two GitLab projects: current README/license and up to ten commits.
- All 550 complete license files were compared with preserved full-text reviews.
  549 were byte-identical; the Inkscape adapter's changed license and linked asset
  exclusion received a full-text review.
- Selected follow-ups also archived primary papers, model cards, independent
  implementation code, complete selected-model terms and specific discussions.
  Initial raw-source URL failures remain recorded locally; a wrong Chatterbox
  branch URL was resolved against the repository's actual default branch.

This combines a library-wide source refresh with 50 scoped reassessments. The
remaining 500 entries retain their prior assessment dates and findings. It is
not 550 exhaustive output, dependency or independent-use evaluations.

| Missing evidence | Before | After |
| --- | ---: | ---: |
| Creative results | 550 | 546 |
| Reproducible setup | 547 | 542 |
| Substantive maintenance | 546 | 542 |
| Independent use | 547 | 538 |
| Dependencies and costs | 547 | 543 |
| Complete software license | 0 | 0 |

There are **547 pending tools**, including four with only a result review left.
The prioritized queue preserves the remaining work:

```sh
python3 -m media_scout quality-backlog --full
python3 -m media_scout quality-backlog --full --check independent_use
```

No discovered software was installed or executed. Current curation is stored in
`config/quality_reviews.json`, bound to the exact latest published record, and
rendered in the [searchable library](https://wenjunii.github.io/ai-media-tools/).
The dated editions, delivery receipts and scheduler are preserved.
