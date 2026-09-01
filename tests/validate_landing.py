from html.parser import HTMLParser
from pathlib import Path
import re

TITLE = "Productos de higiene profesional | Higienextremadura"
DESCRIPTION = "Productos de higiene profesional, sistemas de dosificación y servicio técnico periódico en Plasencia."
NAV = ["#inicio", "#empresa", "#productos", "#servicio", "#contacto"]
CATEGORIES = [
    ("Textiles y útiles de limpieza", "categoria-textiles-utiles-limpieza"),
    ("Higiene general", "categoria-higiene-general"),
    ("Dispensadores", "categoria-dispensadores"),
    ("Automoción", "categoria-automocion"),
    ("Lavandería", "categoria-lavanderia"),
    ("Higiene en superficies", "categoria-higiene-superficies"),
    ("Celulosa", "categoria-celulosa"),
    ("Artículos de un solo uso", "categoria-articulos-un-solo-uso"),
    ("Higiene personal", "categoria-higiene-personal"),
    ("Higiene en cocina", "categoria-higiene-cocina"),
    ("Carros de limpieza", "categoria-carros-limpieza"),
    ("Ambientadores", "categoria-ambientadores"),
]
PHONES = {"+34676193667": "676193667", "+34927419291": "927419291"}
EMAIL = "josemiguel@higienextremadura.com"
IMAGES = {
    "assets/source-site/slides/slide1.jpg": "",
    "assets/source-site/categories/textiles.jpg": "Limpieza de cristales con una rasqueta",
    "assets/source-site/categories/dispensadores.jpg": "Dos secamanos murales en un espacio público",
    "assets/source-site/categories/carros.jpg": "Profesional con carro de limpieza en un edificio",
}
RESTRICTED = re.compile(
    r"ahorro|ecológic|calidad|garantiz|perfecto funcionamiento|desinfect|bactericida|fungicida|hospitalari|certificad|testimoni|respuesta en",
    re.I,
)


class Document(HTMLParser):
    def __init__(self):
        super().__init__()
        self.tags, self.attrs, self.text, self.stack, self.links, self.elements = [], [], [], [], [], []

    def handle_starttag(self, tag, attrs):
        values = dict(attrs)
        self.tags.append(tag)
        self.attrs.append((tag, values))
        self.elements.append((list(self.stack), tag, values))
        if tag == "a":
            self.links.append((list(self.stack), values))
        self.stack.append((tag, values))

    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)
        self.stack.pop()

    def handle_endtag(self, tag):
        for index in range(len(self.stack) - 1, -1, -1):
            if self.stack[index][0] == tag:
                del self.stack[index:]
                break

    def handle_data(self, data):
        value = " ".join(data.split())
        if value:
            self.text.append((list(self.stack), value))


def attrs(doc, tag):
    return [values for name, values in doc.attrs if name == tag]


def text_inside(doc, tag, **wanted):
    return [text for stack, text in doc.text if any(name == tag and all(values.get(k) == v for k, v in wanted.items()) for name, values in stack)]


def main():
    root = Path(__file__).parents[1]
    path = root / "index.html"
    failures = []
    check = lambda condition, message: failures.append(message) if not condition else None
    source = path.read_text(encoding="utf-8") if path.exists() else ""
    doc = Document()
    doc.feed(source)
    html = attrs(doc, "html")
    check(html and html[0].get("lang") == "es", 'lang="es"')
    check(" ".join(text_inside(doc, "title")) == TITLE, "approved title")
    metas = attrs(doc, "meta")
    check(any(x.get("name") == "description" and x.get("content") == DESCRIPTION for x in metas), "approved description")
    check(len(attrs(doc, "h1")) == 1, "exactly one H1")
    required = [("div", "inicio"), ("main", "contenido-principal"), ("section", "empresa"), ("section", "productos"), ("section", "servicio"), ("section", "contacto")]
    check(all(any(tag == wanted_tag and values.get("id") == wanted_id for tag, values in doc.attrs) for wanted_tag, wanted_id in required) and bool(attrs(doc, "footer")), "core semantic landmarks and IDs")
    body_children = [(tag, values) for stack, tag, values in doc.elements if stack and stack[-1][0] == "body"]
    check(bool(body_children) and body_children[0][0] == "a" and body_children[0][1].get("href") == "#contenido-principal", "first-child skip link")
    nav_links = [link.get("href") for stack, link in doc.links if any(tag == "nav" and values.get("aria-label") == "Navegación principal" for tag, values in stack)]
    check(nav_links == NAV, "five exact ordered navigation targets")
    observed = [(" ".join(text_inside(doc, "li", id=category_id)), category_id) for _, category_id in CATEGORIES]
    check(observed == CATEGORIES, "exact ordered category labels and stable IDs")
    links = attrs(doc, "a")
    for uri, digits in PHONES.items():
        href = "tel:" + uri
        display = re.sub(r"\D", "", " ".join(text_inside(doc, "a", href=href)))
        check(any(x.get("href") == href for x in links) and display == digits, "matching phone " + digits)
    email_links = [x for x in links if x.get("href") == "mailto:" + EMAIL]
    check(bool(email_links) and EMAIL in " ".join(text_inside(doc, "a", href="mailto:" + EMAIL)), "matching email")
    images = attrs(doc, "img")
    check(all("alt" in image for image in images), "explicit alt on every image")
    check([(image.get("src"), image.get("alt")) for image in images] == list(IMAGES.items()), "four approved local images and alternatives")
    check(all((root / image.get("src", "")).is_file() for image in images), "every local image exists")
    check(IMAGES["assets/source-site/slides/slide1.jpg"] == "", "empty decorative hero alt")
    check(all(IMAGES[path] for path in list(IMAGES)[1:]), "non-empty informative image alts")
    ids = {values["id"] for _, values in doc.attrs if values.get("id")}
    fragments = [x.get("href", "") for x in links if x.get("href", "").startswith("#")]
    check(all(fragment[1:] in ids for fragment in fragments), "every fragment link resolves")
    check(not any(x.get("href", "").rstrip("/") in ("/aviso-legal", "/politica-de-privacidad") for x in links), "obsolete legal URLs absent")
    check(not any(x.get("rel") == "canonical" for x in attrs(doc, "link")), "canonical absent from preview")
    check(not any(tag in doc.tags for tag in ("script", "form")), "no scripts or forms")
    styles = [x.get("href", "") for x in attrs(doc, "link") if x.get("rel") == "stylesheet"]
    check(styles == ["styles.css"], "one required local stylesheet")
    check(all((root / style).is_file() for style in styles), "every local stylesheet exists")
    check(not re.search(r"carousel|slider|lorem|todo|placeholder", source, re.I), "no carousel or placeholders")
    check(not RESTRICTED.search(" ".join(text for _, text in doc.text)), "no restricted claims")
    if failures:
        print("FAIL: " + "\nFAIL: ".join(failures))
        raise SystemExit(1)
    print("PASS: metadata, landmarks, navigation, fragments, local resources, contacts, preview omissions, and exclusions")


if __name__ == "__main__":
    main()
