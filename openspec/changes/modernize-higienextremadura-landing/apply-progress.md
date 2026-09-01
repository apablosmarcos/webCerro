# Apply progress: modernize-higienextremadura-landing

## Approved inputs

Approval owner: project owner (user in this Pi session)
Approval date: 2026-09-01
Use: public GitHub Pages preview only. The existing Joomla/custom-domain production deployment remains unchanged; production replacement remains blocked until every production release gate is complete.

| Gate | Recorded decision |
|---|---|
| G1 | Approved title: `Productos de higiene profesional | Higienextremadura`. Approved description:`Productos de higiene profesional, sistemas de dosificación y servicio técnico periódico en Plasencia.` Approved hero/H1: `Productos de higiene profesional`. Approved company fact:`Higienextremadura nace en septiembre de 2009.` Approved service terms: `sistemas de dosificación` and `servicio técnico periódico`. Approved CTA:`Solicitar información`. |
| G2 | Approved category-only discovery using the exact ordered 12 category labels and stable IDs in `design.md`. |
| G3 | Approved primary email CTA: `josemiguel@higienextremadura.com`. Approved visible contacts: `676 193 667`, `927 419 291`, and `josemiguel@higienextremadura.com`. Approved location: `Plasencia (Cáceres)`. Public visits and opening hours are not approved and must not be stated. |
| G4 | The public preview has no forms, scripts, cookies, analytics, or personal-data collection. Obsolete legacy legal/privacy URLs and copy are omitted. Current reviewed legal documents may be added later and remain a production-replacement gate. |
| G5 | GitHub Pages is approved only as a public preview host, not as the canonical production host or a cutover. The existing Joomla site and custom domain remain unchanged; no DNS, CNAME, redirect, or domain migration is authorized. |
| G6 | Public reuse rights are confirmed for the four images referenced by `index.html`: `slide1.jpg`, `textiles.jpg`, `dispensadores.jpg`, and `carros.jpg`. Production suitability remains a separate future release decision. |
| G7 | GitHub Pages is the preview platform. Preview publication requires no redirect adapter, unsupported-path migration handling, monitoring/SLO, or production rollback. T7–T8 remain blocked future production-cutover work until that separate deployment is approved. |
| G8 | No restricted claim is approved. Omit unsubstantiated results, savings, quality, environmental, perfect-operation, disinfection, antimicrobial, registration, certification, testimonial, metric, service-area, and response-time claims. |

## Strict TDD evidence

| Cycle | Task | Evidence | Result |
|---|---|---|---|
| RED | T1 | `python3 tests/validate_landing.py` before `index.html` existed | Historical exit 1; failures included `lang="es"`, approved title/description, one H1, landmarks, navigation, categories, both phones, email, the then-proposed legal destinations, and canonical. The legal-link contract is superseded for preview. |
| GREEN | T2 | `python3 tests/validate_landing.py` after adding semantic HTML | Historical exit 0 under the then-current contract. The preview now intentionally omits obsolete legal destinations. |
| TRIANGULATE | T3 | Controlled mutations against a restored copy of `index.html` | Each mutation exited 1: removed category/stable ID → category contract; changed phone display → phone contract; second H1 → H1 contract; form plus restricted phrase → form contract; broken legal URL → legal contract; absent, wrong, and duplicate canonical → canonical contract. Restored page exited 0. |
| REFACTOR | T4 | Simplified phone-link comparison and retained shared parser/text helpers; reran validator | Exit 0 with unchanged PASS contract. `git diff --numstat` then: `99 0 index.html`, `113 0 tests/validate_landing.py` (212 lines). |
| RED | T5 image correction | Extended `tests/validate_landing.py` first to require the four approved exact local paths, explicit `alt` on every image, empty hero alt, and non-empty exact informative alts; ran against the image-free page | Exit 1: `FAIL: four approved local images and alternatives`. |
| GREEN | T5 image correction | Added the decorative hero and compact three-image Productos row, using source assets in place with intrinsic dimensions and responsive aspect-ratio-preserving CSS | Exit 0: `PASS: metadata, landmarks, navigation, 12 categories, four local images, contacts, legal, canonical, and exclusions`. |
| TRIANGULATE | T5 image correction | Temporarily changed the hero alternative from empty to `Baño` | Exit 1: `FAIL: four approved local images and alternatives`; restored immediately. |
| REFACTOR | T5 image correction | Kept one shared responsive image rule and no new abstraction, dependency, copied asset, background image, or crop | Final validator exit 0; `git diff --check` exit 0. |

## Completed implementation tasks

- T1, T2, T3, T4, and T5 are complete and visibly checked in `tasks.md`.
- Added `tests/validate_landing.py`, `index.html`, and `styles.css`.
- Corrected T5 at the user's request so the public preview visibly uses the rights-confirmed hero plus three category images from their existing source paths. T5 remains checked because the responsive, local, no-JavaScript presentation acceptance remains satisfied.
- T6 remains unchecked because representative VoiceOver/NVDA and real device call/mail-handler checks were not available. No unsupported claim of that evidence is made. Its earlier prohibition on all images contradicted completed T5 and is corrected below to prohibit only unapproved images.

## Browser and manual evidence — 2026-09-01

| Environment/check | Result | Evidence / limitation |
|---|---|---|
| Chromium headless, 1440 × 1000 | Pass | Screenshot inspected; no clipping/overlap in captured viewport. DOM had one H1. |
| Chromium CDP, 320 CSS px | Pass | Screenshot inspected; `scrollWidth=305`, `clientWidth=305`; navigation and cards wrap without horizontal page overflow. |
| Chromium CDP, 200% effective scale (320 CSS px at device scale 2) | Pass | 640 × 2000 screenshot inspected; `scrollWidth=305`, `clientWidth=305`; visible content remains reflowed. |
| Focus/keyboard spot check | Partial pass | Programmatically focused first-child skip link; computed outline was 3 px. Full physical keyboard journey was not run. |
| Network (before image correction) | Historical pass, superseded for image inventory | Local server received only `/`, `/styles.css`, and Chromium's default `/favicon.ico` request (404). The corrected page now intentionally references four approved local images; a new full network/manual pass belongs to pending T6. |
| Legal destinations | Not applicable to preview | Obsolete legacy URLs remain omitted. Current reviewed documents are deferred to any future production replacement. |
| Contrast calculation | Pass | ink/paper 14.85:1; ink/wash 13.87:1; dark-teal/paper 7.13:1; visited/paper 9.02:1; white/dark-teal 7.13:1; focus ink/wash 13.87:1. |
| Source/DOM/content | Pass before correction; automated contract updated after correction | Semantic source order, exact Spanish category text, one H1, no script/form/motion/tracking/embed, and contact URI equality remain covered. The updated validator additionally requires four exact local images and their decorative/informative alt contracts. |
| VoiceOver/NVDA; real mobile call; desktop/mobile mail handler | Not run | No representative screen reader or physical/mobile handler was available; blocks T6 completion. |

Screenshots were generated as temporary review evidence at `/tmp/webcerro-desktop.png`, `/tmp/webcerro-320px.png`, and `/tmp/webcerro-200pct.png`; they are not product artifacts.

## Commands and final verification

- RED: `python3 tests/validate_landing.py` after extending the image contract and before adding markup — exit 1; `FAIL: four approved local images and alternatives`.
- Historical GREEN: `python3 tests/validate_landing.py` exited 0 under the then-current legal-link contract. That contract is superseded: the public preview intentionally omits obsolete legal destinations.
- Mutation: temporarily changed the required empty hero alt to `Baño`; validator exited 1 with `FAIL: four approved local images and alternatives`; restored before the final pass.
- `git diff --check -- index.html styles.css tests/validate_landing.py` — exit 0.
- Final implementation numstat: `106 0 index.html`, `108 0 styles.css`, `127 0 tests/validate_landing.py`; total **341 added, 0 deleted**.
- `git diff --cached --name-only` — empty. Intent-to-add is used only for the three implementation files, so content is not staged.

## Deviations and scope boundary

- Four rights-confirmed existing source-site images are referenced in place for the public preview. The hero is decorative (`alt=""`); the category images have concise Spanish alternatives and visible captions. Production suitability remains a separate future decision.
- No JavaScript, dependency, copied/derived asset, background image, crop, tracking, cookie, analytics, form, or personal-data collection was added.
- GitHub Pages is preview-only. No DNS, CNAME, redirect, monitoring/SLO, production rollback, or Joomla/custom-domain change is in scope. T7, T8, R2, and production cutover remain blocked future work.
- Workload boundary: corrected T1–T5 slice only, **341/400 changed implementation lines**; below the 380-line hard stop, leaving **39 lines to 380** and **59 lines to 400**.

## Remaining tasks

- [ ] **T6 — Validate the complete page manually:** check unstyled/source order; HTML validity and console/network cleanliness; keyboard skip/nav/contact journey and focus order/visibility; one H1 and coherent landmarks/headings/lists in VoiceOver or NVDA; WCAG 2.2 AA computed contrast for normal/hover/focus/visited states; 320 px reflow and 200% zoom; exact Spanish accents/casing and all 12 categories/anchors; no unsupported claim, unapproved image, form, motion, tracking, cookie, embed, or dead control; real mobile call offer and desktop/mobile mail-handler offer. Confirm obsolete legal/privacy URLs remain absent; resolving reviewed legal destinations is deferred to a future production replacement. Re-run `python3 tests/validate_landing.py`. Acceptance evidence is a dated device/browser/assistive-technology matrix with pass/fail results and the final command output. Depends on T5 and approved operational values from G1–G6/G8. <!-- sdd-owner: implementation -->
- [ ] **T7 — Create `redirects.md`:** inventory `/`, `/empresa`, `/productos`, `/contacto`, `/aviso-legal`, `/politica-de-privacidad`, and all 12 category paths from `spec.md`; map them to the final canonical landing, five stable section anchors, 12 stable category anchors, or exact approved legal destinations. For unsupported paths record intended destination, explicit no-redirect decision, accepting owner/date, and SEO risk; preserve query strings where supported and target final HTTPS destinations to avoid chains. Acceptance evidence is a 19-path review table with no silent omissions and owner review recorded. Depends on T6, G5, and G7. <!-- sdd-owner: implementation -->
- [ ] **T8 — Add the smallest host-native redirect adapter only after G7 identifies a future production platform:** use `_redirects`, narrowly scoped `.htaccess`, or an operator-ready server configuration reference; never use JavaScript or meta-refresh. For each supported legacy URL, verify permanent status, one hop, correct final canonical path, no loop, and then verify the fragment target in a browser. If hosting has no redirect support, add no fake adapter and complete the accepted-risk fields in `redirects.md`. Acceptance evidence is the HTTP/browser matrix for every mapped path and a passing `python3 tests/validate_landing.py`. Depends on T7 and the budget stop condition. <!-- sdd-owner: implementation -->
- [ ] **R2 — Verify future production-cutover evidence only:** as a zero-actor lifecycle gate—not a review transaction or grant of review authority—confirm all production approvals and passing content/contact/legal/accessibility/responsive/metadata/redirect evidence, with a recoverable Joomla deployment and independently reversible redirects. This gate is not required for the GitHub Pages public preview; any unresolved production gate blocks only a future replacement. <!-- sdd-owner: parent -->

## Structured status consumed

- Change: `modernize-higienextremadura-landing`; authoritative store: openspec; apply state: source candidate ready for commit, with Pages activation pending T6 post-deploy/manual verification.
- `actionContext.mode=repo-local`; workspace and only allowed edit root: `/home/alvaro_pablos/miscosas/webCerro`; no warnings.
- Authorized preview scope: T1–T6. Actual completed scope: T1–T5; T6 post-deploy/manual verification remains pending and unchecked; no manual completion is claimed. Future production-only blockers: current reviewed legal documents, final production asset suitability, production hosting/cutover approval, DNS/canonical migration decisions, redirects, monitoring/SLO decisions, rollback evidence, T7, T8, and R2.
