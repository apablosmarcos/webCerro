# Technical Design: modernize-higienextremadura-landing

## 1. Design summary

Build one dependency-free static document and one stylesheet. There is no existing application, build system, or requested framework, and every launch-critical behavior is native HTML, so a framework, package manager, component layer, client-side JavaScript, and runtime configuration would add cost without capability.

The public-preview slice uses verified teal cues, a 12-item category matrix, a supply → dosing → periodic S.A.T. sequence, and four source images with confirmed public reuse rights. Literal approved contact values are inserted into HTML; obsolete legal/privacy values are omitted rather than represented by guessed placeholders. Production suitability and current reviewed legal documents remain future production-replacement gates.

### Frontend design plan

- **Subject and audience:** a practical professional-hygiene supplier for procurement, operations, and existing customers who need range and human support quickly.
- **Palette:** verified `#58ADA6` as rules and spacious accents; verified dark teal `#26615C` for high-contrast surfaces and primary actions; white, `#F4F8F7`, and near-black `#172B29` as neutral support.
- **Typography:** one local/system stack: `"Open Sans", ui-sans-serif, system-ui, sans-serif`. This preserves the only evidenced family when installed without fetching Google Fonts. No font file or external request is added.
- **Structural device:** the product taxonomy is the main visual grid; service is a short ordered sequence rather than generic feature cards.
- **Signature element:** paired 3 px teal rules, derived from the verified logo line treatment, sit beside key headings and connect the service sequence. They are CSS decoration, not meaningful content.
- **Critique:** omit gradients, stock hero photography, glass cards, decorative blobs, icon packs, carousel behavior, and animation. Those treatments do not explain this business and would either repeat template residue or depend on unverified assets.

## 2. System boundary and files

Implementation is centered at the repository root because no application directory or deployment convention exists yet:

| File | Purpose | Forecast |
|---|---|---:|
| `index.html` | Complete Spanish landing, metadata, semantic content, approved links | 130–155 lines |
| `styles.css` | Palette, type scale, layout, states, responsive behavior | 130–155 lines |
| `tests/validate_landing.py` | Standard-library structural contract check | 45–60 lines |
| `redirects.md` | Host-neutral reviewed legacy-path map and ownership status | 20–25 lines |
| Host redirect adapter, once hosting is known | `_redirects`, `.htaccess`, or equivalent generated from the map | 0–25 lines |

Target: **325–395 changed implementation lines**. Binary assets, a JS file, package metadata, build config, component scaffolding, and embedded legal documents are excluded. If reviewed legal documents must be added to this repository rather than linked as supplied destinations, reforecast before implementation; do not squeeze them into the 400-line budget.

No application data is collected or transmitted. Browser flows are only document navigation, `tel:`, `mailto:`, and legal links. The preview server only serves static files; redirects belong to future production migration.

## 3. Document structure and stable contracts

Use this source order, which remains coherent without CSS:

1. `a.skip-link[href="#contenido-principal"]`
2. `header`: text brand treatment (or approved logo), primary `nav[aria-label="Navegación principal"]`
3. `main#contenido-principal`
   - hero `#inicio` with the only `h1` and a direct confirmed contact link
   - `section#empresa`
   - `section#productos`, 12-item category list, and enquiry link
   - `section#servicio`, ordered supply/dosing/S.A.T. sequence
   - `section#contacto`, confirmed call and email actions and optional confirmed public location
4. `footer`: `href="#inicio"`; add approved current Legal Notice and Privacy Policy links only before a future production replacement

Primary navigation contracts are exactly:

| Label | Target |
|---|---|
| Inicio | `#inicio` |
| Empresa | `#empresa` |
| Productos | `#productos` |
| Servicio | `#servicio` |
| Contacto | `#contacto` |

Category nodes receive stable IDs so old category URLs can preserve intent even though the cards are not product-detail links:

| Approved visible label | Stable ID |
|---|---|
| Textiles y útiles de limpieza | `categoria-textiles-utiles-limpieza` |
| Higiene general | `categoria-higiene-general` |
| Dispensadores | `categoria-dispensadores` |
| Automoción | `categoria-automocion` |
| Lavandería | `categoria-lavanderia` |
| Higiene en superficies | `categoria-higiene-superficies` |
| Celulosa | `categoria-celulosa` |
| Artículos de un solo uso | `categoria-articulos-un-solo-uso` |
| Higiene personal | `categoria-higiene-personal` |
| Higiene en cocina | `categoria-higiene-cocina` |
| Carros de limpieza | `categoria-carros-limpieza` |
| Ambientadores | `categoria-ambientadores` |

IDs are lowercase ASCII, unambiguous, and treated as migration API: visual or copy changes must not rename them. `scroll-margin-block-start` prevents anchored headings/cards touching the viewport edge; smooth scrolling is not enabled.

## 4. Content mapping

| Destination | Evidence-backed content | Production handling |
|---|---|---|
| Brand/header | Business name; verified teal treatment | Default to styled text `higienextremadura`. Replace with an approved production logo only when both rights and quality pass. |
| Hero | “Productos de higiene profesional” | One H1. Supporting sentence and direct contact label use final owner-approved wording/value. No legacy slide claims. |
| Empresa | Began in September 2009; professional hygiene focus | Short paragraph, approved verbatim before release. No geography, customer count, or quality claim. |
| Productos | The exact 12 specified labels | Semantic `ul`; one label per `li`, no images, descriptions, counts, SKUs, or “complete catalog” implication. Introduce explicitly as categories. |
| Servicio | Dosing systems; periodic S.A.T. visits for system-related needs | An `ol` with three concise stages: product supply, dosing systems, periodic S.A.T. support. Final Spanish wording requires owner approval and cannot imply a guarantee or response time. |
| Contacto | Confirmed active phone and monitored email | Separate descriptive links such as `Llamar al …` and `Escribir a …`; visible and URI values must represent the same approved destination. Publish location only if address and public-visit status are confirmed. |
| Footer/legal | No reviewed current documents for preview | Omit obsolete URLs/copy in preview. Add descriptive links to supplied reviewed destinations before any production replacement. |

The hero CTA points directly to the approved primary `tel:` or `mailto:` destination, not merely `#contacto`, because that is a specification contract. A secondary text link may point to `#productos`. Category cards are informational, not fake controls; the single post-grid enquiry link supplies the next action.

## 5. Visual and responsive system

### Palette and contrast

Define CSS custom properties only for repeated tokens:

- `--teal: #58ADA6` — rules, borders, large non-text accents; never small white text.
- `--teal-dark: #26615C` — primary action/background. White against it is approximately **7.13:1**.
- `--ink: #172B29` — body/headings. Against light teal it is approximately **5.62:1**.
- `--paper: #FFFFFF`; `--wash: #F4F8F7` — alternating surfaces.

All ordinary text uses `--ink` on paper/wash. Links are underlined except where a bordered primary navigation/action treatment already communicates interactivity. Focus uses a 3 px high-contrast outline with 3 px offset; it is not replaced with a color-only state. Re-measure every final foreground/background/state combination rather than relying only on these base ratios.

### Type and spacing

- Body: `clamp(1rem, .96rem + .2vw, 1.125rem)`, line-height about 1.6.
- H1: `clamp(2.25rem, 7vw, 4.75rem)`, short line length; section headings use a smaller fluid step.
- Copy measure: about `65ch`; page width: about `70rem` with fluid 1–2rem gutters.
- Section spacing uses `clamp()`; no fixed heights and no text over images.

### Layout

- Header is not sticky: this avoids covering anchors and consuming the viewport at 200% zoom. Navigation is a wrapping flex row; no hamburger or disclosure is needed.
- Hero is a two-area CSS grid at available widths: thesis/content beside a restrained teal rule field. The decorative field collapses below the content on narrow widths and is `aria-hidden` only if represented by an HTML node; prefer pseudo-elements.
- Product list uses `grid-template-columns: repeat(auto-fit, minmax(min(100%, 14rem), 1fr))`. It naturally reflows from several columns to one without device-specific breakpoints. Cards use number + label as taxonomy, not generic icons.
- Service uses an ordered list with connecting paired rules; DOM order remains supply, dosing, S.A.T.
- Contact is a two-column grid when space permits and one column otherwise. Links use at least 44 px effective block size and `overflow-wrap: anywhere` for long addresses.
- A single media query around `48rem` may refine hero/contact alignment. At 320 CSS px all grids are one column and navigation wraps. Do not hide content at any width.

No transitions are required. If a tiny hover transition is introduced during implementation, disable it under `prefers-reduced-motion: reduce`; deletion is preferred.

## 6. Accessibility mechanics

- Set `<html lang="es">`, UTF-8, viewport metadata, one useful `<title>`, one H1, ordered H2/H3 structure, and native landmarks.
- The skip link is first in DOM, visually concealed only until focus, and targets the focusable main (`tabindex="-1"` only if browser testing shows it is needed for reliable focus transfer).
- Use only `<a>` for navigation/contact/legal actions. Do not add ARIA roles to native landmarks or links. `aria-current` is not used because a static one-page page cannot update it without script.
- Cards are a list. Their visible text is the accessible name; decorative numerals/rules are hidden from assistive technology when separate from the label.
- Text-brand fallback needs no image alternative. If approved logo is used, its `alt` is `Higienextremadura`; adjacent duplicate brand text is then visually hidden or removed to prevent duplicate announcements.
- There are no keyboard traps, hover-only content, custom controls, autoplay, or motion-dependent information.
- Validate DOM/source order, keyboard order, 320 px reflow, 200% zoom, contrast, and representative screen-reader output. Native phone/email behavior is tested on a supporting mobile device as well as by URI inspection.

## 7. Metadata rules

Implementation-ready rules:

- Title pattern: `Productos de higiene profesional | Higienextremadura` after owner approval.
- Description: one unique Spanish sentence assembled only from approved professional-hygiene, category, dosing, S.A.T., and contact wording; aim for roughly 140–160 characters but truth outranks length.
- Exactly one H1; all 12 category labels remain HTML text.
- No `meta keywords`, Open Graph image, favicon copied from Joomla, geo metadata, or structured business data in this slice.
- Omit `<link rel="canonical">` while `.com` versus `.es` or the public landing URL is unresolved. Once approved, insert exactly one absolute HTTPS URL with the chosen preferred host/path.
- Omit Organization/LocalBusiness JSON-LD until legal identity, domain, address, and contacts are consistent and verified. This is omission, not a TODO script or empty schema.

## 8. Contact and legal behavior

HTML contains literal approved values; no environment variables, JSON config, templating, or runtime substitution is justified for one static page.

- Normalize phone URI values to `tel:+34…` when the client confirms Spanish numbers; display the owner-approved human-readable format. The validator compares normalized digits.
- Use a plain `mailto:` address with no prefilled subject/body unless explicitly approved. No obfuscation script.
- Do not show either source address, either provisional phone, the named email, opening hours, visit invitation, or a map merely because it appeared on the legacy site.
- The public preview omits obsolete legacy legal/privacy URLs and copy. It has no forms, scripts, cookies, analytics, or personal-data collection.
- Current reviewed legal links/documents are deferred until before any production replacement. If supplied as repository files, that is a scope/reforecast decision because this design does not draft or budget them.

## 9. Rights-safe assets

Public reuse rights are confirmed for the four preview images referenced in place: `assets/source-site/slides/slide1.jpg`, `assets/source-site/categories/textiles.jpg`, `assets/source-site/categories/dispensadores.jpg`, and `assets/source-site/categories/carros.jpg`. Preserve source evidence unchanged. This rights decision does not establish production suitability.

The text wordmark remains the fallback. Any future production logo or optimized image derivative requires a separate suitability decision and separate production path; never modify the evidence files.

## 10. Legacy redirect strategy

`redirects.md` is the reviewed source of truth until hosting is identified. Intended decisions are:

- `/` → serve the landing (no redirect).
- `/empresa` → `/#empresa`; `/productos` → `/#productos`; `/contacto` → `/#contacto`.
- Each inventoried category path → its matching `/#categoria-…` ID from section 3.
- `/aviso-legal` and `/politica-de-privacidad` → serve approved content at those paths, or redirect to the exact reviewed destinations.

Use permanent redirects only after production destinations and canonical domain are approved. Preserve query strings unless the chosen host requires an explicit rule. Prevent chains by targeting the final canonical HTTPS URL directly when host rules require absolute locations.

Hosting adapter options, selected only after the platform is known:

1. Netlify-compatible host: a small `_redirects` file.
2. Apache: narrowly scoped `.htaccess` `Redirect 301` rules.
3. Nginx/managed hosting: provide the reviewed map to the operator as server config; keep the acceptance record in `redirects.md`.
4. Host with no redirect support: record, per path, intended destination, explicit no-redirect decision, accepting owner, date, and SEO risk. Do not add JavaScript or meta-refresh redirect pages as a workaround.

Validate each configured path with an HTTP client: expected permanent status, one hop, correct final path/fragment, no loop. Fragment navigation is then verified in a browser because URL fragments are not sent to the server.

## 11. Validation strategy

`tests/validate_landing.py` uses only Python's standard library (`html.parser`, `pathlib`, `re`) and is written before/with the markup. It exits non-zero unless all machine-checkable contracts hold:

- `lang="es"`, title, description, exactly one H1, and required landmark/section IDs;
- exact ordered set of 12 visible category labels and all stable category IDs;
- five primary anchor destinations;
- no `script`, `form`, external stylesheet/font, carousel marker, provisional placeholder token, or restricted-claim phrase;
- at least one literal confirmed `tel:` and one literal confirmed `mailto:`, with displayed destinations matching normalized URI values;
- for future production, two non-placeholder legal destinations;
- canonical absent when the launch record says unresolved, or exactly one approved absolute canonical when resolved.

The test must consume a small explicit approved-values block in its own source or a concise checked-in launch record; it must not make network calls or become a content-management system. Final values are committed with their assertions so accidental regression is visible in review.

Manual release checks cover what parsing cannot:

1. HTML validation and browser console/network review (no unexpected requests).
2. Keyboard-only skip/nav/contact journey and visible focus; include legal links only in future production checks.
3. 320 px viewport, long-content wrapping, and 200% zoom without horizontal page scroll/overlap.
4. Computed contrast for normal, hover, focus, and visited states.
5. VoiceOver or NVDA landmark/heading/list/link pass.
6. Real mobile call offer and desktop/mobile email-handler offer; for future production, legal destinations resolve.
7. Exact Spanish copy/category comparison and restricted-claim review.
8. Redirect status/one-hop/browser-fragment matrix for every inventoried path.

Testing is configured as `enabled: false` only because no runner currently exists; the standard-library command is `python3 tests/validate_landing.py`. No dependency installation is introduced.

## 12. Unresolved launch-gate data: exact handling

### Implementation-ready decisions

The static stack, file boundary, source order, anchor IDs, exact category labels, CSS system, text-brand fallback, no-JS/no-form behavior, accessibility mechanics, metadata omission rules, redirect intent, and validation contracts can be implemented without further product decisions.

### Client-supplied blockers

| Required decision/data | Until supplied | On approval |
|---|---|---|
| Final company, dosing, and S.A.T. Spanish wording | Do not invent or expand copy; implementation branch may not be released. | Insert approved literal wording and snapshot it in validation expectations. |
| All 12 categories/current category-only approval | Keep exact specified list only as a review candidate; release blocked. | Record owner/date and validate exact list. |
| Primary CTA, active phone(s), monitored email | Do not publish provisional `676 193 667`, `927 419 291`, or `josemiguel@…`; no dummy `tel:`/`mailto:` or dead CTA. | Insert literal displayed links, normalized URIs, and validator expectations; test operationally. |
| Public address and whether visits are intended | Omit the entire location block, not merely its label. | Add only the approved address/visit wording; no map. |
| Legal identity, privacy controller/contact, reviewed legal destinations | Never copy legacy legal/privacy text; release blocked even if footer styling is complete. | Link the two exact reviewed destinations and verify they resolve. |
| Canonical `.com`/`.es` and public URL | Omit canonical, domain-dependent Open Graph URLs, and structured data. | Add one absolute HTTPS canonical and update direct redirect targets. |
| Logo/image rights and suitability | Ship-design remains text/CSS only; no source binary enters production. | Logo may be optimized separately if it improves the result; other imagery remains out of scope by default. |
| Hosting/redirect capability | Maintain `redirects.md`; do not pretend client-side redirects satisfy migration. | Add the smallest host-native adapter or record accepted no-redirect risk per path. |
| Restricted-claim evidence/wording | Omit every unresolved claim completely. | Add only separately substantiated and approved literal wording; otherwise no change. |

There are no production placeholder strings (`TODO`, fake phone/email, `#` legal links), hidden unresolved data, commented-out claims, or build-time defaults. A release candidate is ineligible while any required row lacks recorded approval and validation.

## 13. Preview deployment and future production rollback

Deploy the static files to GitHub Pages as a public preview only. This is not a production cutover: keep the Joomla/custom-domain deployment unchanged and do not configure DNS, CNAME, redirects, monitoring/SLO, or a production rollback for the preview. Preview rollback is simply disabling/removing the Pages publication; production remains unaffected.

Migration readiness, current reviewed legal documents, production hosting, redirect validation, monitoring/SLO decisions, and a recoverable production rollback plan remain blocked future work. Reforecast them only if the owner separately approves replacing production.

## 14. Decision record

- Chosen: native static HTML/CSS, zero client JavaScript and zero dependencies.
- Chosen: typography-first, verified teal identity, CSS line motif, system font fallback.
- Chosen: stable section and per-category anchors; semantic list rather than interactive cards.
- Chosen: direct call/email only; legal documents remain approved external/separate destinations by default.
- Chosen: four rights-confirmed source images for public preview; production suitability remains undecided and text branding remains the fallback.
- Chosen: GitHub Pages as public preview only; no production hosting, custom-domain, DNS/CNAME, redirect, monitoring/SLO, or rollback change.
- Rejected: framework/build system, hamburger menu, carousel, form/backend, external fonts, analytics, maps, structured data, and client-side redirect shims.
