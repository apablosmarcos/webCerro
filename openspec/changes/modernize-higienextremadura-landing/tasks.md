# Tasks: modernize-higienextremadura-landing

## Review Workload Forecast

| Field | Value |
|-------|-------|
| Estimated changed lines | 325–395 additions + deletions |
| 400-line budget risk | Medium |
| Chained PRs recommended | No |
| Suggested split | Single PR: landing contract/page → migration readiness |
| Delivery strategy | single-pr |
| Chain strategy | single-pr-default |

Decision needed before apply: No
Chained PRs recommended: No
Chain strategy: single-pr-default
400-line budget risk: Medium

The single PR contains two independently reviewable work units. After every task, measure `git diff --numstat`. Stop and reforecast **before** adding more changes if the current diff plus the minimum forecast for unfinished required work would reach 400 lines, or if the diff reaches 380 lines. Remove optional visual CSS first; never compress accessibility, validation, truthful-content, legal, contact, or redirect checks to fit. Repository-hosted legal documents, a larger host adapter, imagery, or any scope addition requires a new forecast before implementation continues.

## Dependencies and client-supplied launch-gate inputs

These facts are inputs, not implementation guesses. Record approved values and decisions in the apply/release evidence. The GitHub Pages public preview does not depend on production legal documents, canonical cutover, hosting migration, DNS/CNAME, redirects, monitoring/SLO, or production rollback. Those remain blocked future production work; no task may guess missing values or copy obsolete legal text.

| Gate | Client-supplied input | Required by |
|---|---|---|
| G1 | Final approved Spanish company, September 2009, professional-hygiene, dosing, periodic S.A.T., hero, CTA, title, and description wording | T2 onward |
| G2 | Approval that the exact 12 named categories remain current and category-only discovery is acceptable | T2 onward |
| G3 | Approved primary CTA, active phone number(s), monitored email, plus whether an address/location and public visits may be stated | T1–T2 and release |
| G4 | Current reviewed legal identity/documents; obsolete legacy URLs stay omitted | Future production replacement, not preview |
| G5 | GitHub Pages approved as public preview only; existing production canonical/custom domain remains unchanged | Preview now; canonical migration only for future production |
| G6 | Public reuse rights confirmed for the four referenced preview images; production suitability separate | T2–T6 preview; suitability before production |
| G7 | GitHub Pages preview needs no redirects; production hosting/redirect decisions remain unapproved | T7–T8 future production only |
| G8 | Evidence and exact approved wording for any restricted claim; absent approval means complete omission | T1–T2 and release |

No task may resolve contradictory phone, email, address, legal, or `.com`/`.es` facts by inference. If G5 is temporarily unresolved during a non-release preview, the validator and page must assert/implement canonical omission; release still waits for G5.

## Work unit 1 — Landing contract and accessible page

**Start:** G1–G3/G8 are recorded; G4 is explicitly deferred with obsolete URLs omitted; G5 records preview-only Pages hosting; G6 confirms reuse rights for the four referenced preview images.
**Finish:** the dependency-free landing passes the standard-library validator and manual page checks.
**Verification:** `python3 tests/validate_landing.py` plus T6 evidence.
**Rollback:** remove `index.html`, `styles.css`, and `tests/validate_landing.py` together.
**Forecast:** `tests/validate_landing.py` 45–60; `index.html` 130–155; `styles.css` 130–155; unit total 305–370 changed lines.

### Strict TDD sequence for `tests/validate_landing.py`

- [x] **T1 — RED:** Create `tests/validate_landing.py` using only `html.parser`, `pathlib`, and `re`; encode the approved-values block and assertions for `lang="es"`, title/description, exactly one H1, core landmarks/IDs, five exact nav targets, the exact ordered 12 labels and stable category IDs, confirmed matching `tel:`/`mailto:` display and URI values, omission of obsolete legal destinations, canonical behavior consistent with preview-only hosting, and exclusion of scripts, forms, external fonts/stylesheets, carousel markers, placeholders, and restricted claims. Run `python3 tests/validate_landing.py` before `index.html` exists and retain the non-zero output identifying missing contracts as RED evidence. Depends on G1–G5 and G8; acceptance evidence is the command, exit code, and representative failed assertions in the apply report. <!-- sdd-owner: implementation -->

- [x] **T2 — GREEN:** Add the minimum semantic `index.html` that makes `python3 tests/validate_landing.py` pass: first-child skip link to `#contenido-principal`; `header`, labelled primary nav, hero/Inicio content at `#inicio`, `main#contenido-principal`, Empresa/Productos/Servicio/Contacto sections, footer back-to-start navigation, one static hero/H1 and direct approved CTA, approved literal company/service/contact values and preview-safe legal/canonical handling, and no JavaScript/form/structured data. Use the exact 12 labels and stable IDs from `design.md`; describe them as categories, not a complete SKU catalog. Acceptance evidence is a zero exit code and validator output naming all checked contracts. Depends on T1 and G1–G5/G8. <!-- sdd-owner: implementation -->

- [x] **T3 — TRIANGULATE:** Prove the validator detects independent regressions by temporarily testing controlled broken copies of `index.html`: remove/rename one category or stable ID, mismatch a displayed contact from its URI, add a second H1, add a prohibited form/script/restricted claim, add an obsolete legal URL, add a production canonical contrary to G5, and break a fragment target. Capture a non-zero result for each mutation, restore the passing page, and rerun the command successfully; no broken fixture or mutation remains in production files. Depends on T2; acceptance evidence is the mutation/result matrix plus the final passing run. <!-- sdd-owner: implementation -->

- [x] **T4 — REFACTOR:** Simplify duplicated parser/assertion logic and HTML markup without broadening scope or adding dependencies; keep approved values explicit and reviewable. Run `python3 tests/validate_landing.py` unchanged in behavior. Acceptance evidence is the passing command, unchanged contract list, and `git diff --numstat` confirming the unit still fits the forecast. Depends on T3. <!-- sdd-owner: implementation -->

### Presentation and behavior

- [x] **T5 — Implement `styles.css` and link it locally from `index.html`:** use the verified teal/dark-teal/ink/paper/wash palette, system font stack, visible 3 px focus, underlined or bordered links, fluid type/spacing, wrapping non-sticky navigation, auto-fit category grid, ordered service sequence, and responsive hero/contact layout. Use only the four rights-confirmed preview images plus the text wordmark; add no other images, external fonts, fixed heights, hidden content, required motion, or JavaScript; ensure 44 px effective contact targets, `overflow-wrap`, and anchor `scroll-margin`. Acceptance evidence is a local-network inspection showing no unexpected external requests and screenshots/check notes at desktop, 320 CSS px, and 200% zoom with no clipping, overlap, or horizontal page scroll. Depends on T4 and G6. <!-- sdd-owner: implementation -->

- [ ] **T6 — Validate the complete page manually:** check unstyled/source order; HTML validity and console/network cleanliness; keyboard skip/nav/contact journey and focus order/visibility; one H1 and coherent landmarks/headings/lists in VoiceOver or NVDA; WCAG 2.2 AA computed contrast for normal/hover/focus/visited states; 320 px reflow and 200% zoom; exact Spanish accents/casing and all 12 categories/anchors; no unsupported claim, unapproved image, form, motion, tracking, cookie, embed, or dead control; real mobile call offer and desktop/mobile mail-handler offer; confirm obsolete legal/privacy URLs remain absent. Re-run `python3 tests/validate_landing.py`. Acceptance evidence is a dated device/browser/assistive-technology matrix with pass/fail results and the final command output. Depends on T5 and approved operational values from G1–G6/G8. <!-- sdd-owner: implementation -->

## Work unit 2 — Future production migration readiness

This work unit is not required for the GitHub Pages public preview and remains blocked until a production replacement is separately approved.

**Start:** Work unit 1 passes; production G5 and G7 decisions are recorded.
**Finish:** every inventoried path has a reviewed outcome and every supported redirect is validated.
**Verification:** HTTP status/one-hop matrix plus browser fragment checks.
**Rollback:** remove/disable the host adapter independently while retaining `redirects.md` as the migration record.
**Forecast:** `redirects.md` 20–25; host-native adapter (`_redirects`, `.htaccess`, or operator config reference) 0–25; unit total 20–50 changed lines. The adapter may proceed only if the measured PR remains below 400 lines.

- [ ] **T7 — Create `redirects.md`:** inventory `/`, `/empresa`, `/productos`, `/contacto`, `/aviso-legal`, `/politica-de-privacidad`, and all 12 category paths from `spec.md`; map them to the final canonical landing, five stable section anchors, 12 stable category anchors, or exact approved legal destinations. For unsupported paths record intended destination, explicit no-redirect decision, accepting owner/date, and SEO risk; preserve query strings where supported and target final HTTPS destinations to avoid chains. Acceptance evidence is a 19-path review table with no silent omissions and owner review recorded. Depends on T6, G5, and G7. <!-- sdd-owner: implementation -->

- [ ] **T8 — Add the smallest host-native redirect adapter only after G7 identifies a future production platform:** use `_redirects`, narrowly scoped `.htaccess`, or an operator-ready server configuration reference; never use JavaScript or meta-refresh. For each supported legacy URL, verify permanent status, one hop, correct final canonical path, no loop, and then verify the fragment target in a browser. If hosting has no redirect support, add no fake adapter and complete the accepted-risk fields in `redirects.md`. Acceptance evidence is the HTTP/browser matrix for every mapped path and a passing `python3 tests/validate_landing.py`. Depends on T7 and the budget stop condition. <!-- sdd-owner: implementation -->

## Parent-owned release gate

The 400-line protection is a parent approval stop condition only: apply must stop and obtain a reforecast/delivery decision before 400 changed lines. It creates zero review actors, starts no review transaction, and grants no review authority.

- [ ] **R2 — Verify future production-cutover evidence only:** as a zero-actor lifecycle gate—not a review transaction or grant of review authority—confirm production approvals, current legal documents, production hosting/canonical decisions, passing redirect evidence, monitoring/SLO decisions, and a recoverable Joomla deployment with independently reversible redirects. This is not required for the public Pages preview; unresolved items block only a future production replacement. <!-- sdd-owner: parent -->
