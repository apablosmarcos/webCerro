# Brand audit

This audit separates the few verified identity signals from site content and generic Joomla presentation. Use it as evidence, not as permission to reuse an asset.

## Verified palette

| Color | Verified use | Confidence | Design status |
|---|---|---:|---|
| `#58ADA6` (`rgb(88, 173, 166)`) | 3 px top border, links, active navigation, primary buttons | High: repeated CSS declaration on the four principal pages | Primary identity candidate |
| `#26615C` (`rgb(38, 97, 92)`) | Site background | High: repeated `body.site` CSS declaration | Dark identity candidate |
| `#333333` (`rgb(51, 51, 51)`) | Inline color around legacy Empresa content | Medium | Editorial residue; do not promote to brand color without approval |

White, greys, gradients, button treatments, carousel controls, and Bootstrap states are not verified brand colors. Most belong to Joomla Protostar, Bootstrap, or Slideshow CK.

## Typography

| Use | Evidence | Classification |
|---|---|---|
| Headings `h1`–`h6` and `.site-title` | Global `font-family: 'Open Sans', sans-serif`; Google Fonts request for Open Sans | Only verified site-configured family |
| Empresa legacy fragment | Inline `Tahoma, Helvetica, Arial, sans-serif`, `12.16px`, `line-height: 15.808px` | Legacy editorial formatting, not a reliable brand rule |
| General body copy | Primarily inherited from Protostar `template.css` | Template typography, not verified identity |

Open Sans may be retained as continuity, but the client should confirm whether it is intentional. Do not reproduce the undersized legacy text styles.

## Asset classification

| Class | Assets | Reuse position |
|---|---|---|
| Brand | `assets/source-site/brand/logo-1.png` | The only verified primary brand asset. No SVG, monochrome, inverse, symbol-only, mobile, or alternate lockup was found. Request original artwork before production use. |
| Content | Four slides and thumbnails; `Foto5.jpg`, `Foto8.jpg`, `numero6.jpg`; 12 category images | Commercial/editorial evidence. They illustrate current messaging and catalog structure but are not identity assets. |
| Template | Protostar favicon, breadcrumb arrow, chevrons/icon font, Bootstrap controls, Slideshow CK controls and styles | Generic Joomla/plugin presentation. Not downloaded and should not be carried into the redesign. |
| Reference capture | Full-page screenshots for `/`, `/empresa`, `/productos`, `/contacto` | Historical layout evidence only; not a production asset. |

The Protostar favicon was not downloaded: its path identifies it as a generic template resource and it adds no useful brand evidence.

## Reuse and licensing cautions

- The owner confirmed public-preview reuse rights for the four images currently referenced: `slides/slide1.jpg`, `categories/textiles.jpg`, `categories/dispensadores.jpg`, and `categories/carros.jpg`. This does not approve production suitability or any other source asset.
- Hosting alone does **not** establish rights for the logo, remaining slides, editorial images, or remaining category images; those need separate approval before reuse.
- Other slides may contain stock or third-party photography, and other category images may originate from manufacturers or external catalogs (`losdi.com`, `quimituria.com`, `talleresgalindo.com`).
- The source legal notice attributes materials to Higienextremadura **or third parties**; this prevents blanket reuse assumptions.
- Category and editorial images have missing/non-descriptive alternative text on the source site. Write meaningful alternatives only after confirming what each image depicts and whether it remains in the new design.
- Preserve downloaded files unchanged as source evidence. Any optimization, cropping, metadata removal, or format conversion should create a separate production derivative after rights approval.

## Layout boundary

The current centered container, left `span3` navigation, right `span9` content, vertical pills, breadcrumbs, and four-column catalog grid are Bootstrap 2/Protostar patterns. They document the current information architecture but are not brand requirements for the modernization.
