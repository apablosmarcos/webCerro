# Landing Experience Specification

## Purpose

Define the truthful, accessible, category-led Spanish landing experience for a public preview of a possible future replacement. The preview does not replace or alter the legacy Joomla/custom-domain production site.

## Requirements

### Requirement: One-page information architecture

The system MUST present Inicio, Empresa, Productos, Servicio, and Contacto as sections of one Spanish-language landing page. Primary navigation MUST link to stable anchors for those sections, MUST identify destinations with descriptive text, and MUST preserve a logical reading order when followed or read without styling.

Proposal traceability: Target outcome 1; Scope — In scope; Business rule 1.

#### Scenario: Navigate to each section

- GIVEN the landing page is loaded
- WHEN a visitor activates each primary navigation link
- THEN the document moves to the corresponding Inicio, Empresa, Productos, Servicio, or Contacto section
- AND Inicio reaches the hero H1 while each other destination is identifiable by its section heading

#### Scenario: Read the document in source order

- GIVEN styling and scripting are unavailable
- WHEN the document is read from beginning to end
- THEN the five core sections occur in a coherent order
- AND no core content requires leaving the landing page

### Requirement: Static and truthful hero

The system MUST provide one static hero with one descriptive H1, a professional-hygiene message within the approved evidence boundary, and a direct link to a confirmed contact channel. The hero MUST NOT contain a carousel, autoplay, rotating content, or content whose availability depends on motion.

Proposal traceability: Target outcome 2; Business rules 3 and 5; Measurable success criteria.

#### Scenario: First page view

- GIVEN the landing page has loaded
- WHEN a visitor reaches the hero
- THEN one stable professional-hygiene message is present
- AND one direct confirmed contact action is available
- AND no content rotates automatically or manually

### Requirement: Verified company and service content

The system MUST state, using business-owner-approved Spanish wording, that Higienextremadura began in September 2009, supplies professional hygiene products, works with dosing systems, and provides periodic S.A.T. visits for system-related needs. It MUST distinguish company information from the Productos and Servicio sections and MUST NOT extend these facts into unverified guarantees.

Proposal traceability: Target outcome 3–4; Business rule 5; Content and business approval launch gate.

#### Scenario: Review approved business facts

- GIVEN the content owner has approved the company and service wording
- WHEN the Empresa and Servicio sections are reviewed
- THEN the September 2009 origin, professional hygiene focus, dosing systems, and periodic S.A.T. visits are represented
- AND no additional performance guarantee is implied

### Requirement: Exact category coverage

The system MUST present exactly these 12 approved product-category labels as visible, crawlable text, preserving accents and casing: Textiles y útiles de limpieza; Higiene general; Dispensadores; Automoción; Lavandería; Higiene en superficies; Celulosa; Artículos de un solo uso; Higiene personal; Higiene en cocina; Carros de limpieza; Ambientadores. The section MUST describe them as categories rather than as a complete or current SKU catalog.

Proposal traceability: Scope — In scope; Business rule 2; Measurable success criteria.

#### Scenario: Validate the category list

- GIVEN the final Productos section
- WHEN its category labels are counted and compared with the approved list
- THEN exactly 12 labels are present
- AND every label matches the approved Spanish text
- AND no SKU or product-reference list is presented

### Requirement: Direct enquiry interactions

The system MUST expose at least one client-confirmed active phone number as a descriptive telephone link and at least one client-confirmed monitored email address as a descriptive email link. Displayed contact text MUST identify the destination without relying on surrounding context. The system MUST NOT provide a contact form, form submission control, or text implying that a nonexistent form collects enquiries.

Proposal traceability: Target outcome 6; Business rules 4 and 7; Quality and operations launch gate.

#### Scenario: Contact by phone

- GIVEN a confirmed phone number is published
- WHEN a visitor activates its link on a device that supports calls
- THEN the device is offered the same displayed number as the call destination

#### Scenario: Contact by email

- GIVEN a confirmed monitored email address is published
- WHEN a visitor activates its link
- THEN the visitor's email handler is offered the same displayed address as the destination

#### Scenario: Inspect enquiry mechanisms

- GIVEN the landing page is ready for release
- WHEN all enquiry controls and contact copy are inspected
- THEN direct phone and email links are available
- AND no form, submit control, form privacy warning, or dead form-like path is present

### Requirement: Legal navigation without obsolete content

The public preview MUST omit obsolete legacy legal/privacy URLs and copy. Because it has no forms, scripts, cookies, analytics, or personal-data collection, current legal documents MAY be deferred during preview. Before any production replacement, the system MUST provide persistent, descriptive navigation to approved current Legal Notice and Privacy Policy documents; those destinations MAY be separate documents. The system MUST NOT reproduce the legacy LO 15/1999, RD 994/1999, absent-form, or unverified legal-identity wording.

Proposal traceability: Target outcome 7; Business rules 7–8; Legal and privacy launch gate.

#### Scenario: Public preview has no reviewed legal destinations

- GIVEN current reviewed legal documents have not been supplied
- AND the preview has no form, script, cookie, analytics, or personal-data collection
- WHEN the public preview is inspected
- THEN obsolete legal/privacy links and copy are absent
- AND preview publication is not blocked

#### Scenario: Production replacement includes legal navigation

- GIVEN current reviewed legal documents and required legal identity have been approved
- WHEN a future production replacement is assessed
- THEN descriptive Legal Notice and Privacy Policy links reach the reviewed content
- AND neither destination depends on a nonexistent form

### Requirement: Unsupported claims are excluded

The system MUST exclude environmental, cost, quality, performance, perfect-operation, disinfection, bactericidal, fungicidal, H.A./hospital-registration, certification, testimonial, metric, service-area, and response-time claims unless each published claim has substantiation and explicitly approved wording. Unresolved claims MUST be omitted rather than softened into an implied promise.

Proposal traceability: Business rule 6; Content and business approval launch gate; Risks and mitigations.

#### Scenario: Claim lacks approval or evidence

- GIVEN a proposed statement makes one of the restricted claims
- AND its substantiation or approved wording is absent
- WHEN release content is reviewed
- THEN the statement is not published

#### Scenario: Claim is approved

- GIVEN a restricted claim has documented substantiation and approved wording
- WHEN it is included in release content
- THEN the published text stays within that approved wording

### Requirement: Responsive reflow and zoom

The system MUST preserve all core content and interactions without horizontal page scrolling at a viewport width of 320 CSS pixels. Text, navigation, category content, phone numbers, email addresses, contact actions, and any legal links included for a future production replacement MUST wrap or reflow without clipping or overlap. At 200% browser zoom, content and controls MUST remain readable, reachable, and operable in a meaningful reading order.

Proposal traceability: Responsive access affected capability; Quality and operations launch gate; Measurable success criteria.

#### Scenario: Narrow viewport

- GIVEN the landing page is displayed at 320 CSS pixels wide
- WHEN a visitor traverses the full page
- THEN no horizontal page scrolling is required
- AND all core content and controls remain visible and operable

#### Scenario: Two-hundred-percent zoom

- GIVEN the landing page is displayed at 200% browser zoom
- WHEN a visitor reads and operates navigation, categories, contact, and any included current legal links
- THEN content does not overlap or become clipped
- AND the reading and focus order remains meaningful

### Requirement: Semantic and keyboard accessibility

The system MUST identify the document language as Spanish, provide a descriptive page title, one descriptive H1, semantic header, navigation, main, section, and footer structure, logical heading order, and a keyboard-operable skip link to the main content. Every interactive element MUST be operable by keyboard, MUST receive focus in a meaningful order, and MUST have a clearly visible focus indicator meeting WCAG 2.2 AA contrast requirements. Required text and controls MUST meet WCAG 2.2 AA contrast, MUST NOT rely on color alone, and informative images MUST have meaningful text alternatives while redundant or decorative images MUST be ignored by assistive technology.

Proposal traceability: Accessibility affected capability; Quality and operations launch gate; Measurable success criteria.

#### Scenario: Keyboard-only journey

- GIVEN a visitor uses only a keyboard
- WHEN the visitor skips to main content and traverses navigation, contact actions, and any included current legal links
- THEN every action is reachable and operable in a meaningful order
- AND focus remains clearly visible throughout

#### Scenario: Assistive-technology structure

- GIVEN a representative screen reader examines the page
- WHEN landmarks, headings, links, and images are announced
- THEN the document has coherent Spanish-language landmarks and heading order
- AND link purposes and informative image alternatives are understandable
- AND decorative or text-duplicating imagery does not add redundant announcements

#### Scenario: Contrast review

- GIVEN the final colors and interaction states
- WHEN required text, controls, and focus indicators are measured
- THEN each meets the applicable WCAG 2.2 AA contrast threshold

### Requirement: Rights-safe asset fallback

The system MUST remain complete, understandable, and usable without legacy logo, slide, editorial, category, supplier, template, or externally hosted font assets. A source asset MUST NOT ship unless its reuse rights are explicitly confirmed for that use. Reuse rights are confirmed for the four images currently referenced by the public preview; production suitability remains a separate future decision. If either applicable rights or suitability is unresolved, the system MUST use a rights-safe text or typography-led fallback and MUST preserve source evidence unchanged.

Proposal traceability: Business rule 9; Assets and brand launch gate; Assumptions.

#### Scenario: Asset rights remain unresolved

- GIVEN reuse rights or production suitability for a source asset are not confirmed
- WHEN release assets are selected
- THEN that source asset is absent from the release
- AND the page remains complete using a rights-safe fallback

#### Scenario: Source asset is approved

- GIVEN reuse rights and production suitability are confirmed
- WHEN a source asset is prepared for production
- THEN any optimized derivative is separate from the unchanged source evidence

### Requirement: SEO metadata and canonical handling

The system MUST expose `lang="es"`, one descriptive Spanish title, one unique Spanish meta description based only on approved company, category, and service content, one H1, logical headings, and all category labels as crawlable text. Canonical metadata MUST be omitted while the canonical domain is unresolved. After the domain and public landing URL are confirmed, the document MUST expose exactly one absolute canonical URL consistent with that decision. Structured organization or local-business data MUST be omitted unless legal identity, canonical URL, address, and contact facts are mutually consistent and verified.

Proposal traceability: SEO and migration affected capability; Business rules 1, 7, and 11; Quality and operations launch gate.

#### Scenario: Domain is unresolved

- GIVEN `.com` versus `.es` has not been approved
- WHEN metadata is inspected
- THEN no canonical URL or domain-dependent structured business data is published

#### Scenario: Domain is confirmed

- GIVEN the canonical domain and public landing URL are approved
- WHEN metadata is inspected
- THEN exactly one absolute canonical URL matches the approved landing URL
- AND the Spanish title and unique description contain no unsupported claim

### Requirement: Legacy URL migration map

Before a future production replacement, the system MUST maintain a reviewed migration decision for `/`, `/empresa`, `/productos`, `/contacto`, `/aviso-legal`, `/politica-de-privacidad`, and each of the 12 inventoried category paths below. Where hosting supports redirects, retired business and contact paths MUST redirect to their corresponding stable landing section, retired category paths MUST redirect to Productos or a stable anchor for their matching category, and legal paths MUST redirect to the approved legal destinations. Where hosting cannot support a redirect, the migration record MUST identify the path, intended destination, explicit no-redirect decision, owner acceptance, and resulting SEO risk.

Inventoried category paths:

- `/productos/19-textiles-y-utiles-de-limpieza`
- `/productos/12-higiene-general`
- `/productos/9-dispensadores`
- `/productos/4-automocion`
- `/productos/14-lavanderia`
- `/productos/11-higiene-en-superficies`
- `/productos/7-celulosa`
- `/productos/3-articulos-de-un-solo-uso`
- `/productos/13-higiene-personal`
- `/productos/10-higiene-en-cocina`
- `/productos/6-carros-de-limpieza`
- `/productos/2-ambientadores`

Proposal traceability: SEO and migration affected capability; Scope — In scope; Measurable success criteria; Assumptions.

#### Scenario: Supported redirect path

- GIVEN hosting supports redirects and a legacy path has an agreed destination
- WHEN that legacy path is requested
- THEN the visitor is redirected to the documented landing section, category anchor, or approved legal destination
- AND the destination corresponds to the legacy intent

#### Scenario: Redirect is unsupported

- GIVEN hosting cannot redirect an inventoried legacy path
- WHEN migration readiness is reviewed
- THEN the map records the intended destination, explicit decision, owner acceptance, and SEO risk
- AND the path is not silently omitted

### Requirement: Core experience without JavaScript

The system MUST make primary navigation, all five core sections, all 12 category labels, and direct phone and email actions available and operable when JavaScript is unavailable. When current legal navigation is added for a future production replacement, it MUST also work without JavaScript. No launch-critical content or action MAY depend on client-side scripting.

Proposal traceability: Scope — In scope; Assumptions; Review workload forecast.

#### Scenario: JavaScript is unavailable

- GIVEN JavaScript is disabled or fails to load
- WHEN a visitor uses the landing page
- THEN the core sections, category labels, and phone and email actions remain present and operable
- AND any current legal links included for production remain operable

### Requirement: Publication gates

The public GitHub Pages preview MUST NOT change Joomla production, the custom domain, DNS/CNAME, or redirects, and MUST NOT add forms, scripts, cookies, analytics, or personal-data collection. Preview publication requires approved displayed content/contact values, rights for its four referenced images, and validated accessibility/responsive behavior. Legal identity/documents, production canonical migration, redirect coverage, monitoring/SLO, and rollback evidence remain blocked gates for a separately approved production replacement.

Proposal traceability: All Launch gates; Business rules 7 and 10; Decision summary.

#### Scenario: A required gate fails

- GIVEN at least one gate applicable to the requested preview or production release is unresolved
- WHEN that release approval is requested
- THEN that release is blocked
- AND a production-only blocker does not block the public preview or get replaced by a guessed value or copied legacy content

#### Scenario: All required gates pass

- GIVEN every applicable launch gate has recorded approval or validation
- WHEN release readiness is assessed
- THEN the landing page is eligible for release

### Requirement: Explicit scope boundaries

The system MUST NOT include SKU/reference migration, product-detail pages, e-commerce, pricing, checkout, accounts, stock, search, filters, order management, CMS, database, API, supplier synchronization, downloadable catalogs, an unapproved contact form, WhatsApp, maps, analytics, cookies, embeds, social channels, testimonials, reviews, metrics, certifications, service-area or response-time promises, unverified supplier links, new legal drafting, logo redesign, a broad design system, Joomla layout, carousel, breadcrumbs, pagination, template icons, or obsolete privacy/form language. Adding any excluded capability SHALL require a separately approved scope change and its applicable evidence, privacy, legal, accessibility, and operational requirements.

Proposal traceability: Scope — Non-goals; Business rules 4, 6, 8–9.

#### Scenario: Review release scope

- GIVEN the release candidate is complete
- WHEN its content, controls, dependencies, data flows, and destinations are compared with the non-goals
- THEN none of the excluded capabilities is present

#### Scenario: Stakeholder requests an excluded capability

- GIVEN a stakeholder requests a listed non-goal
- WHEN the request is evaluated for this change
- THEN it is excluded unless a separate scope change is approved
