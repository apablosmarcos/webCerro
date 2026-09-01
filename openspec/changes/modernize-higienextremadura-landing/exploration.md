# Exploration: modernize-higienextremadura-landing

## Goal and evidence boundary

Explore the smallest credible modernization: one Spanish-language landing page that explains Higienextremadura, exposes its 12 product categories, makes the verified service and contact paths usable, and preserves legal navigation. This is not an implementation plan or permission to reuse source assets.

Evidence reviewed:

- `openspec/config.yaml`
- `docs/reference/README.md`
- `docs/reference/content-inventory.md`
- `docs/reference/brand-audit.md`
- `assets/source-site/manifest.md`
- the four principal desktop captures, the logo, representative category imagery, and a representative slide under `assets/source-site/`

The source has no sitemap, current responsive evidence, verified asset rights, or adequate current legal identity/privacy data. Findings below distinguish verified content from recommendations and assumptions.

## Smallest viable outcome

Build a single, fast document with anchored navigation and this hierarchy:

1. **Header:** logo/wordmark, Inicio, Empresa, Productos, Servicio, Contacto; persistent but not space-heavy.
2. **Hero:** one stable thesis rather than a carousel: “Productos de higiene profesional” plus carefully qualified supporting language and one contact CTA. The four legacy messages can be condensed only after claim wording is approved.
3. **Company:** founded in September 2009, professional hygiene focus, and the short company story.
4. **Service:** dosing systems and periodic S.A.T. visits, expressed as the differentiator rather than an unsupported performance guarantee.
5. **Product categories:** all 12 canonical categories in a compact grid; each category leads to the contact action or expands only if a no-JavaScript-accessible disclosure is genuinely useful.
6. **Contact:** direct phone and email actions, then confirmed location details. Do not recreate the source’s missing form by default.
7. **Footer:** legal notice and privacy navigation, copyright, and optional “back to top.”

This replaces four shallow Joomla pages and 12 aging category pages with the information explicitly requested for the landing. It intentionally does not reproduce every legacy SKU/reference: the requested scope is a category-led landing, the inventory may be stale, code `10040` is contradictory, and a complete catalog would exceed a realistic one-PR/400-line change.

## Target users and jobs

Primary users are inferred from the professional offer rather than explicitly documented personas:

- procurement or operations staff seeking a hygiene supplier;
- facilities, cleaning, hospitality/kitchen, laundry, or automotive operators suggested by the categories;
- existing customers looking for S.A.T., dosing support, a phone number, or an email address.

Their priority jobs are: establish relevance and trust quickly, confirm that the needed category is covered, understand that service extends beyond supply, and contact a person with minimal friction. Secondary jobs are verifying location and reviewing legal/privacy information.

## Functional parity

| Current behavior/information | Landing equivalent | Decision |
|---|---|---|
| Four-item main navigation | Anchor navigation to the corresponding sections | Preserve, adding Servicio because it is a key verified value |
| Four-slide carousel | One static hero plus short value points | Replace; less motion, clearer message, less code |
| Empresa page | Compact company/story section | Preserve verified facts; qualify claims |
| 12 category cards and detail pages | 12 named category cards on-page | Preserve category coverage, not full legacy catalog |
| Dosing and periodic S.A.T. copy | Dedicated service section | Elevate verified capability |
| `tel:`/phone and `mailto:` contact | Large, descriptive click-to-call and email links | Preserve and improve once confirmed |
| Mentioned but absent contact form | No form by default | Do not reproduce broken behavior or collect personal data unnecessarily |
| Legal/privacy footer links | Persistent footer links to reviewed legal content | Preserve navigation; do not copy obsolete texts |
| Carousel controls, breadcrumbs, previous/next, Joomla internals | None | Obsolete in a one-page document |
| Supplier catalog links | Omit by default; add only if relationships, destination safety, and usefulness are confirmed | Not necessary to the requested category-led landing |

A mail link is the minimum operational enquiry path because it already exists and avoids form processing, spam protection, consent copy, retention policy, and failure-state infrastructure. If the client requires lead capture later, add a genuinely functioning form only after privacy details and delivery ownership are approved.

## Content and claim treatment

Safe to carry forward as source-published facts, pending final client confirmation:

- Higienextremadura began in September 2009.
- It supplies professional hygiene products across the 12 inventoried categories.
- It works with dosing systems.
- Its S.A.T. periodically visits installations and manages system-related needs.
- Published contact channels are `676 193 667`, `927 419 291`, and `josemiguel@higienextremadura.com`.

Do not state as proven facts without evidence: excellent results, minimum application cost, maximum quality, environmentally respectful/non-aggressive formulations, perfect operation, bactericidal/fungicidal status, or H.A./hospital registration. Keep such language out of the initial landing or visibly qualify it only with approved substantiation.

Canonical category labels:

1. Textiles y útiles de limpieza
2. Higiene general
3. Dispensadores
4. Automoción
5. Lavandería
6. Higiene en superficies
7. Celulosa
8. Artículos de un solo uso
9. Higiene personal
10. Higiene en cocina
11. Carros de limpieza
12. Ambientadores

No new product counts, sectors served, delivery areas, opening hours, response times, certifications, testimonials, social channels, prices, or sustainability claims should be invented.

## Design direction

### Pass 1 — deliberate plan

- **Subject/audience:** a practical regional professional-hygiene supplier for buyers and operators who value product coverage and support, not a lifestyle cleaning brand.
- **Palette:** use verified teal `#58ADA6` for controlled accents and dark teal `#26615C` for high-contrast anchors, balanced by white and neutral surfaces. Contrast must be measured; the light teal should not carry small white text.
- **Typography:** Open Sans is the only verified configured family. Use it alone (with a system sans fallback) in a disciplined scale rather than inventing a new brand pairing or reproducing undersized legacy text.
- **Structural device:** a clear 12-cell category matrix paired with a short supply → dosing → S.A.T. service sequence. Structure communicates range and ongoing support.
- **Signature element:** thin paired teal rules derived from the logo’s verified line treatment can connect headings and service steps. This is brand-specific without copying Joomla chrome.

### Pass 2 — critique

Avoid generic gradients, floating glass cards, decorative blobs, stock-photo hero conventions, and gratuitous animation. The current centered panel, left sidebar, breadcrumbs, Bootstrap buttons, slideshow controls, and four-column desktop grid are template residue, not identity. The modernization should feel specific through the teal linework, restrained cleanliness, category taxonomy, and service sequence—not through more UI.

## Accessibility

Target WCAG 2.2 AA fundamentals:

- semantic landmarks, one descriptive `h1`, ordered headings, skip link, and useful page title;
- native links/buttons and keyboard-operable navigation; visible focus with sufficient contrast;
- no automatic carousel; no content that depends on hover, motion, or JavaScript;
- minimum comfortable touch targets and spacing; do not rely on color alone;
- meaningful link labels such as “Llamar al 676 193 667” and displayed email text;
- logo alternative “Higienextremadura”; category images get contextual alternatives only if informative, otherwise empty `alt` when adjacent text duplicates them;
- readable line lengths, scalable text, and layouts resilient at 200% zoom and narrow widths;
- respect reduced-motion preferences if any optional transition is introduced.

Spanish language metadata (`lang="es"`) and correct accents/casing are required. Accessibility validation should cover keyboard, focus order, zoom/reflow, contrast, and a representative screen-reader pass.

## Responsive behavior

Use content-driven breakpoints rather than device-specific layouts:

- header navigation wraps or becomes a native, accessible disclosure only if wrapping is insufficient;
- hero becomes single-column without text over critical image content;
- category matrix moves from several columns to two and then one as space demands;
- contact actions become full-width, easy tap targets on narrow screens;
- phone numbers and long email/address strings wrap safely;
- no horizontal scrolling at 320 CSS px, and meaningful reading order is unchanged across sizes.

The source screenshots prove desktop presentation only and should not be treated as responsive requirements.

## Contact, privacy, and legal constraints

Recommended initial interaction is direct call/email, not a form. It is lower-risk and replaces the only actually working contact behavior with clearer equivalents. Before launch, confirm:

- preferred primary CTA and whether both phone numbers remain active;
- which address is public: Avda. Acacias 3, Pol. Ind. SEPES warehouse, or another location;
- whether the named email remains appropriate and monitored;
- legal entity, NIF/CIF, registered address, domain owner, privacy controller/contact, and current RGPD/LOPDGDD wording;
- canonical `.com` versus `.es` domain.

Legal Notice and Privacy Policy must remain navigable, but the obsolete LO 15/1999 / RD 994/1999 text must not be silently migrated. A legal review/content handoff is a launch dependency. Avoid analytics, cookies, embeds, maps, external fonts, and forms in the smallest version; this reduces privacy surface. If any are later added, assess consent and disclosure obligations first.

## SEO and discoverability

- descriptive Spanish title and unique meta description based on verified professional-hygiene/category/service information;
- one H1 and crawlable HTML section copy; category names as real text, not baked into images;
- canonical URL only after `.com`/`.es` is decided;
- preserve or redirect important current paths (`/empresa`, `/productos`, `/contacto`, legal paths, and category URLs) to relevant landing anchors where hosting permits;
- meaningful contact links and location only after confirmation;
- Organization/LocalBusiness structured data only after legal identity, canonical URL, address, and contact facts are verified; omit rather than publish contradictory schema;
- no meta keywords, hidden catalog copy, speculative location pages, or unsupported claim markup.

Redirect coverage matters more than recreating breadcrumbs or a large sitemap for this one-page scope.

## Asset reuse strategy

- Preserve everything under `assets/source-site/` unchanged as evidence.
- **Logo:** the only verified brand asset, but rights are unproven and the 883×119 PNG includes substantial whitespace. Request original vector/transparent artwork; use the source PNG only if the client confirms rights and quality is acceptable.
- **Category/editorial/slide images:** treat as optional, not required. They are low-resolution legacy composites/stock-like imagery with embedded script text and possible supplier rights. A typography-led category matrix is safer and lighter.
- Do not reuse Joomla favicon, breadcrumb arrows, icon font, Bootstrap controls, or slideshow resources.
- If rights are confirmed and an image materially improves comprehension, create a separate optimized derivative and retain the original. Never upscale or overwrite evidence.
- Avoid adding a new icon or carousel dependency; text and CSS structure cover the need.

## Non-goals

- full e-commerce, checkout, account area, stock, pricing, search, filtering, or order management;
- complete SKU/reference migration or new product-detail pages;
- CMS, database, API, supplier synchronization, or downloadable catalogs;
- unsupported WhatsApp, maps, social media, reviews, certifications, metrics, or service-area claims;
- redesigning/certifying the logo or creating a broad design system;
- reproducing Joomla’s layout, carousel, breadcrumbs, pagination, or broken form copy;
- drafting definitive legal language without qualified client/legal input.

## Risks and mitigations

| Risk | Impact | Smallest mitigation |
|---|---|---|
| Contradictory contact/address/domain data | High | Treat confirmation as launch gate; do not guess |
| Obsolete/incomplete legal and privacy text | High | Legal review and new approved copy; keep collection-free page |
| Unsupported product/environment/performance claims | High | Remove or qualify until evidence and wording are approved |
| Unclear image/logo rights | High | Typography-first page; reuse only after explicit confirmation |
| Category-only view disappoints users expecting SKUs | Medium | Set clear “categorías” language and enquiry CTA; add catalog later only from validated data |
| Redirects omitted during one-page migration | Medium | Inventory legacy paths and map them to stable anchors before release |
| Contact email/phone fails operationally | High | Client confirmation plus pre-launch click/call/mail checks |
| 400-line budget encourages excessive visual compression | Medium | Prefer semantic static page, CSS-only layout, no dependencies or form |
| SEO loses category-page depth | Medium | Keep all 12 names and concise verified context in crawlable HTML; redirect old URLs |

## Open decisions and assumptions

### Blocking before implementation content is finalized

1. Confirm legal identity, current legal/privacy copy, canonical domain, and which legal routes/documents will host it.
2. Confirm current phone(s), preferred CTA, email, address/location, and whether public visiting is intended.
3. Confirm approval/evidence for environmental, cost, quality, performance, disinfection, and registration claims.
4. Confirm rights to logo and images; request original logo artwork.
5. Confirm that a category-only, enquiry-led catalog is acceptable and that all 12 categories remain current.

### Default assumptions for the smallest proposal

- Spanish-only, static, one-page experience.
- `676 193 667` and the published email are provisional primary contact channels pending confirmation.
- No contact form, cookies, analytics, external font, map embed, social links, or supplier links.
- All 12 category names appear; no SKU lists appear.
- Static hero, no carousel and no substantive motion.
- Legal navigation is present, but approved legal documents are supplied outside the design process.

## Recommendation

Proceed to proposal with the single-document, category-led, enquiry-first approach. It best preserves the site’s real value while deleting obsolete Joomla behavior and avoiding new privacy/backend scope. The proposal should make the five client confirmations explicit acceptance dependencies and reserve the 400-line budget for semantic content, responsive CSS, and essential validation—not catalog or form infrastructure.
