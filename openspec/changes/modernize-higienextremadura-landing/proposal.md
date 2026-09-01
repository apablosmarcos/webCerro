# Proposal: modernize-higienextremadura-landing

## Intent

Replace the aging multi-page Joomla presentation with a simple Spanish one-page experience that preserves Higienextremadura’s verified business information and real contact paths. The page will remain category-led and enquiry-first: visitors should quickly understand the offer, find one of the 12 product categories, recognize the dosing and S.A.T. service, and contact the company directly.

This proposal defines product requirements and launch conditions only. It does not select an implementation stack or authorize unverified content or asset reuse.

## Problem

The current site spreads a small amount of useful information across shallow pages and aging category entries, leads with a carousel that has no direct conversion action, and provides weak responsive and accessibility evidence. Its most useful outcomes—understanding category coverage and contacting the company—are harder to reach than necessary.

Modernization also carries material content risk: contact, address, domain, and legal details conflict; privacy text is obsolete; several commercial and regulatory claims lack substantiation; the catalog may be stale; and rights to source imagery are unverified. A direct migration would reproduce ambiguity and operational risk rather than solve it.

## Target users and situations

- Procurement and operations staff evaluating a professional hygiene supplier.
- Facilities, cleaning, hospitality/kitchen, laundry, and automotive operators looking for relevant product coverage.
- Existing customers seeking dosing support, S.A.T., a phone number, or an email address.
- Visitors verifying company history, location, privacy, or legal information.

The priority moment is a quick supplier check or support/enquiry need, often on a mobile device. Users need relevance, trust, category coverage, and a working human contact path without navigating a full catalog.

## Target outcome

Deliver one responsive, accessible, operational, SEO-conscious Spanish landing page with:

1. concise anchored navigation;
2. a static hero with a verified professional-hygiene message and direct contact CTA;
3. the company story, including the verified September 2009 origin;
4. a clear section for dosing systems and periodic S.A.T. support;
5. all 12 canonical product categories in crawlable text;
6. prominent, descriptive phone and email actions;
7. for a future production replacement, persistent navigation to approved legal and privacy content.

The result should feel modern through hierarchy, spacing, typography, restrained verified color cues, and responsive structure—not through motion, template chrome, or new dependencies.

## Scope

### In scope

- A single Spanish-language page with sections for Inicio, Empresa, Productos, Servicio, and Contacto.
- Replacement of the four-slide carousel with one static hero.
- Preservation of these 12 category labels:
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
- Verified company history and carefully worded dosing/S.A.T. capability.
- Direct `tel:` and `mailto:` enquiry paths using client-confirmed details.
- Future production Legal Notice and Privacy Policy navigation to reviewed content.
- Semantic content, keyboard usability, visible focus, contrast, zoom/reflow resilience, and no required motion or JavaScript interaction.
- Responsive behavior down to 320 CSS px without horizontal page scrolling.
- Basic on-page SEO: Spanish language metadata, descriptive title and meta description, one H1, logical headings, crawlable category text, and canonical metadata only after the domain is confirmed.
- For a future production replacement, a redirect map for important existing company, product, contact, legal, and category URLs where hosting supports redirects.
- Pre-launch functional, accessibility, responsive, content, and metadata checks.

### Non-goals

- Full SKU/reference migration, product-detail pages, or correction of the legacy catalog.
- E-commerce, pricing, checkout, accounts, stock, search, filters, or order management.
- CMS, database, API, supplier synchronization, or downloadable catalog infrastructure.
- A contact form unless separately approved with delivery ownership, privacy wording, retention, spam protection, and failure handling.
- WhatsApp, maps, analytics, cookies, embeds, social channels, testimonials, reviews, metrics, certifications, service areas, or response-time promises without separate verification and approval.
- Supplier catalog links unless destinations, relationships, and usefulness are confirmed.
- New legal drafting, logo redesign, broad design-system work, or production reuse of source assets without rights confirmation.
- Reproduction of Joomla layout, carousel, breadcrumbs, pagination, template icons, or obsolete privacy/form language.
- Any implementation-stack decision in this phase.

## Affected capabilities

| Capability | Proposed change |
|---|---|
| Site navigation | Consolidate core destinations into stable on-page sections; add reviewed legal navigation for future production. |
| Business presentation | Preserve verified history and professional hygiene positioning while removing unsupported claims. |
| Product discovery | Replace aging category/detail navigation with a compact overview of all 12 categories. |
| Service discovery | Elevate dosing systems and periodic S.A.T. as a distinct, verified capability. |
| Enquiries | Make confirmed phone and email paths prominent and descriptive; do not introduce a form. |
| Responsive access | Provide content-driven reflow, usable targets, and safe wrapping on narrow screens. |
| Accessibility | Establish semantic landmarks/headings, skip navigation, keyboard/focus support, contrast, readable sizing, and reduced-motion-safe behavior. |
| SEO and migration | Provide crawlable Spanish content and metadata; map important legacy URLs for future production. |
| Legal/privacy | Require approved current documents and discoverable destinations before future production replacement. |
| Brand presentation | Use verified identity cues cautiously; exclude template styling and unlicensed assets. |

## Business rules

1. The page is Spanish-only for the first release and must use correct Spanish accents, casing, and `lang="es"`.
2. The experience remains category-led and enquiry-first. All 12 categories appear; no SKU list is implied or migrated.
3. The hero is static. No carousel, autoplay, or content dependent on motion is permitted.
4. Direct call and email are the only default enquiry mechanisms. A form requires a later explicit product and privacy decision.
5. Company history, dosing systems, and periodic S.A.T. may be stated only within the evidence boundary of the reference material and client approval.
6. No environmental, cost, quality, performance, disinfection, bactericidal/fungicidal, H.A./hospital-registration, certification, or similar claim may ship without substantiation and approved wording.
7. Phone numbers, email, address, legal identity, domain, and legal/privacy text must be explicitly confirmed; contradictions must never be resolved by guessing.
8. Legal Notice and Privacy Policy must be navigable in a future production replacement, but obsolete source texts must not be copied.
9. Source files remain evidence. Logo, photography, category images, supplier media, and fonts may be used only when rights and production suitability are confirmed; the initial design must work without optional imagery or externally hosted fonts.
10. Accessibility and operational contact behavior are launch requirements, not later enhancements.
11. Structured data is omitted unless legal identity, canonical domain, address, and contact facts are internally consistent and verified.

## Launch gates

Release is blocked until all applicable gates pass:

### Content and business approval

- Confirm all 12 categories remain current and that category-only discovery is acceptable.
- Approve the company, dosing, and S.A.T. wording.
- Confirm the preferred primary CTA, active phone number(s), monitored email, public address/location, and whether public visits are intended.
- Remove every unsupported claim or provide evidence and approved wording.

### Legal and privacy

- Confirm legal entity, NIF/CIF, registered/public address, domain owner, privacy controller/contact, and canonical `.com` or `.es` domain.
- Supply or approve current Legal Notice and Privacy Policy destinations/content under RGPD/LOPDGDD review.
- Confirm that no unapproved tracking, cookies, embeds, or personal-data collection has entered scope.

### Assets and brand

- Confirm rights before any source logo or image is reused; otherwise launch with a rights-safe text/typography-led treatment.
- Ensure no Joomla/template or unverified supplier asset is carried forward.

### Quality and operations

- Verify every displayed phone number and email action on representative mobile and desktop environments.
- Validate keyboard navigation, focus order/visibility, heading structure, contrast, 200% zoom, representative screen-reader output, and reflow at 320 CSS px.
- Confirm title, description, language, canonical handling, crawlable category text, and redirect coverage for agreed legacy paths.
- Obtain business/content owner sign-off on the final Spanish page.

## Measurable success criteria

- Exactly 12 approved category labels are visible as real, crawlable text.
- The company origin, dosing systems, and periodic S.A.T. are represented with approved wording.
- At least one confirmed phone action and one confirmed email action are visible and function correctly; no form-like dead end is present.
- For a future production replacement, Legal Notice and Privacy Policy are reachable from the landing page and use approved destinations/content.
- No carousel, autoplay, unapproved form, SKU catalog, unsupported claim, or unlicensed/unapproved source asset ships.
- All primary navigation and contact actions are operable by keyboard with visible focus.
- The page has no horizontal page scroll at 320 CSS px and remains readable/usable at 200% zoom.
- Automated/manual contrast review finds no WCAG 2.2 AA contrast failure in required text and controls; representative screen-reader review finds a coherent landmark and heading order.
- The rendered document has Spanish language metadata, one descriptive H1, an approved title and meta description, and canonical metadata consistent with the confirmed domain.
- Before future production replacement, every agreed priority legacy URL has a documented destination or an explicit decision not to redirect.
- Stakeholder acceptance confirms that a visitor can identify a relevant category and reach a working contact channel without leaving the one-page journey.

## Assumptions

- The first release is a static-content, one-page Spanish experience.
- `676 193 667` and `josemiguel@higienextremadura.com` are provisional evidence only until client confirmation; `927 419 291` and all address variants remain unresolved.
- All 12 category names remain in scope, but no individual product data is reliable enough for this slice.
- No form, analytics, cookies, external font, map embed, social link, supplier link, or substantive motion is necessary for launch.
- Approved legal documents may remain separate destinations rather than being embedded in the landing.
- Hosting can support redirects; if it cannot, the migration owner must explicitly accept the resulting SEO risk.
- A typography-first presentation is acceptable if asset rights or quality are unresolved.

## Risks and mitigations

| Risk | Impact | Mitigation |
|---|---|---|
| Contradictory contact, address, or domain data | Users cannot reach the business; misleading publication | Make confirmation a hard launch gate and test final actions. |
| Obsolete/incomplete legal and privacy content | Compliance and trust exposure | Require reviewed current content; keep the page collection- and tracking-free. |
| Unsupported commercial or regulated claims | Legal, reputational, and customer risk | Omit by default; include only with evidence and approved wording. |
| Unclear logo/image rights | IP exposure or launch delay | Design to work without imagery; use assets only after explicit rights approval. |
| Category-only view is mistaken for a full catalog | User disappointment or extra support enquiries | Label the section clearly as categories and pair it with a direct enquiry CTA. |
| Lost authority from retired category URLs | SEO traffic loss | Map priority paths to relevant stable anchors and validate redirects before release. |
| Contact channels are unmonitored or invalid | Landing is visually complete but operationally broken | Confirm ownership and run pre-launch call/mail checks. |
| One-page consolidation weakens detailed search coverage | Reduced long-tail visibility | Keep concise category context crawlable; defer detail pages until validated demand and data exist. |
| 400-line budget drives inaccessible shortcuts | Quality regression | Keep interactions native and scope static; protect accessibility and validation before decoration. |

## Future production rollback

For a separately approved production replacement, keep the current production site available until all production gates pass. Deployment must be reversible to the prior site/version without losing source evidence or approved content. Preserve the legacy URL inventory and redirect map so redirects can be disabled or reverted independently if they cause routing problems. Because this release adds no form, database, CMS, or data migration, rollback should require no user-data restoration.

## Review workload forecast

**Delivery shape:** one PR, provided the approved scope remains static and no form, CMS, full catalog, bespoke legal drafting, or unverified asset remediation is added.

**Changed-line target:** approximately 300–380 hand-authored lines across the minimum page content, styling, metadata/configuration, redirect rules or mapping, and a small validation checklist/check. The 400-line review budget is feasible only with:

- one page and a compact stylesheet rather than reusable component infrastructure;
- native links and layout behavior rather than JavaScript widgets;
- category names rather than SKU/detail content;
- no new dependency, backend, analytics, map, or form;
- concise redirects/configuration limited to priority legacy paths.

The forecast should be revisited before implementation once the existing delivery structure and hosting constraints are known. If required production changes exceed 400 reviewed lines, reduce optional visual treatment or split migration configuration from the page only with explicit approval; do not compress away accessibility, legal, or operational checks.

## Decision summary

Proceed with the smallest credible modernization: a one-page, Spanish, category-led and enquiry-first landing that preserves verified business value while removing obsolete interaction and avoiding new privacy/backend scope. Implementation may begin only after the content/contact/legal/asset decisions needed for truthful publication are assigned, and launch remains blocked until they are resolved.
