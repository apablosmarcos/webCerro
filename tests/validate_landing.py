from html.parser import HTMLParser
from pathlib import Path
import re
import subprocess

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
        if tag not in {"meta", "link", "img", "br", "hr", "input", "source"}:
            self.stack.append((tag, values))

    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)
        self.handle_endtag(tag)

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


def check_scene_lifecycle(root):
    # Run the actual module against small browser/Three doubles; no GPU or network.
    harness = r"""
import assert from 'node:assert/strict';
import { readFileSync } from 'node:fs';
const source = readFileSync('scripts/cleaning-scene.js', 'utf8').replace(
  /import\('https:\/\/cdn\.jsdelivr\.net\/npm\/three@0\.180\.0\/build\/three\.module\.js'\)/,
  'globalThis.loadThree()');
class Target extends EventTarget {
  hidden = true;
  isConnected = true;
  classes = new Set();
  classList = { add: x => this.classes.add(x), remove: x => this.classes.delete(x),
    toggle: (x, on) => on ? this.classes.add(x) : this.classes.delete(x) };
  setAttribute() {}
  append() {}
  remove() { this.removed = true; }
  getBoundingClientRect() { return { width: 440, height: 540 }; }
}
const vector = () => ({ set() {} });
class Object3D {
  position = vector(); rotation = vector(); scale = vector();
  add() {} updateProjectionMatrix() {} dispose() { this.disposed = true; }
}
let renderer, io, ro, imports;
class Renderer extends Object3D {
  domElement = new Target();
  constructor() { super(); renderer = this; }
  setPixelRatio(n) { assert.ok(n <= 1.5); }
  setSize(w, h, css) { assert.equal(css, false); }
  setAnimationLoop(fn) { this.loop = fn; }
  render() { this.renders = (this.renders || 0) + 1; }
}
const THREE = new Proxy({ WebGLRenderer: Renderer }, { get: (o, key) => key === 'then' ? undefined : o[key] || Object3D });
globalThis.ResizeObserver = class { constructor(fn) { ro = this; this.fn = fn; } observe() {} disconnect() { this.disconnected = true; } };
globalThis.IntersectionObserver = class { constructor(fn) { io = this; this.fn = fn; } observe() {} disconnect() { this.disconnected = true; } };
async function boot(reduced = false, fail = false) {
  const host = new Target(), toggle = new Target(), motion = new Target();
  motion.matches = reduced;
  globalThis.document = new Target(); document.hidden = false;
  document.getElementById = id => id === 'cleaning-scene' ? host : toggle;
  globalThis.window = new Target(); window.devicePixelRatio = 3;
  globalThis.matchMedia = () => motion;
  imports = 0;
  globalThis.loadThree = () => {
    imports++;
    if (fail === true) return Promise.reject(Error('offline'));
    return Promise.resolve(fail === 'webgl' ? new Proxy(THREE, {
      get: (o, key) => key === 'WebGLRenderer' ? class { constructor() { throw Error('No WebGL'); } } : o[key]
    }) : THREE);
  };
  new Function(source)();
  await new Promise(resolve => setImmediate(resolve));
  return { host, toggle, motion };
}
await boot(true); assert.equal(imports, 0);
let state = await boot(false, true);
assert.equal(state.toggle.hidden, true); assert.equal(state.host.classes.has('is-ready'), false);
state = await boot(false, 'webgl');
assert.equal(state.toggle.hidden, true); assert.equal(state.host.classes.has('is-ready'), false);
state = await boot();
assert.equal(renderer.loop, null); // Offscreen initially.
io.fn([{ isIntersecting: true }]); assert.equal(typeof renderer.loop, 'function');
state.toggle.dispatchEvent(new Event('click')); assert.equal(renderer.loop, null);
state.toggle.dispatchEvent(new Event('click')); assert.equal(typeof renderer.loop, 'function');
document.hidden = true; document.dispatchEvent(new Event('visibilitychange')); assert.equal(renderer.loop, null);
document.hidden = false; document.dispatchEvent(new Event('visibilitychange')); assert.equal(typeof renderer.loop, 'function');
io.fn([{ isIntersecting: false }]); assert.equal(renderer.loop, null);
io.fn([{ isIntersecting: true }]);
state.motion.matches = true; state.motion.dispatchEvent(new Event('change'));
assert.equal(renderer.loop, null); assert.equal(state.host.classes.has('is-ready'), false);
state.motion.matches = false; state.motion.dispatchEvent(new Event('change'));
const hide = new Event('pagehide'); hide.persisted = true; window.dispatchEvent(hide); assert.equal(renderer.loop, null);
window.dispatchEvent(new Event('pageshow')); assert.equal(typeof renderer.loop, 'function');
ro.fn(); assert.ok(renderer.renders > 0);
renderer.domElement.dispatchEvent(new Event('webglcontextlost', { cancelable: true }));
assert.equal(renderer.loop, null); assert.equal(renderer.disposed, true);
assert.equal(ro.disconnected, true); assert.equal(io.disconnected, true);
assert.equal(state.host.classes.has('is-ready'), false); assert.equal(state.toggle.hidden, true);
state = await boot(); window.dispatchEvent(new Event('pagehide')); assert.equal(renderer.disposed, true);
console.log('PASS: scene lifecycle doubles (reduced motion, offline, pause, visibility, resize, bfcache, context loss, disposal)');
"""
    subprocess.run(["node", "--input-type=module", "-e", harness], cwd=root, check=True)


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
        display = re.sub(r"\D", "", " ".join(text_inside(doc, "section", id="contacto")))
        check(digits in display, "informational phone " + digits)
    check(EMAIL in " ".join(text_inside(doc, "section", id="contacto")), "informational email")
    check(all(x.get("href", "").startswith("#") for x in links), "internal links only; no contact actions")
    check("Plasencia · Extremadura" in source, "visible regional context")
    images = attrs(doc, "img")
    check(all("alt" in image for image in images), "explicit alt on every image")
    check(bool(images) and all(image.get("src") in IMAGES and image.get("alt") == IMAGES[image["src"]] for image in images), "only approved local images and alternatives")
    check(all((root / image.get("src", "")).is_file() for image in images), "every local image exists")
    check(IMAGES["assets/source-site/slides/slide1.jpg"] == "", "empty decorative hero alt")
    check(all(IMAGES[path] for path in list(IMAGES)[1:]), "non-empty informative image alts")
    ids = {values["id"] for _, values in doc.attrs if values.get("id")}
    fragments = [x.get("href", "") for x in links if x.get("href", "").startswith("#")]
    check(all(fragment[1:] in ids for fragment in fragments), "every fragment link resolves")
    check(not any(x.get("href", "").rstrip("/") in ("/aviso-legal", "/politica-de-privacidad") for x in links), "obsolete legal URLs absent")
    check(not any(x.get("rel") == "canonical" for x in attrs(doc, "link")), "canonical absent from preview")
    check("form" not in doc.tags, "no forms")
    check(attrs(doc, "script") == [{"type": "module", "src": "scripts/cleaning-scene.js"}], "one local scene module")
    check(any(x.get("id") == "cleaning-scene" and x.get("aria-hidden") == "true" for _, x in doc.attrs), "decorative scene hidden from assistive technology")
    check(any(x.get("id") == "scene-toggle" and "hidden" in x for x in attrs(doc, "button")), "progressively enhanced pause control")
    check(bool(attrs(doc, "svg")), "inline static scene fallback")
    scene_path = root / "scripts/cleaning-scene.js"
    check(scene_path.is_file(), "scene module exists")
    styles = [x.get("href", "") for x in attrs(doc, "link") if x.get("rel") == "stylesheet"]
    check(styles == ["styles.css"], "one required local stylesheet")
    check(all((root / style).is_file() for style in styles), "every local stylesheet exists")
    css = (root / "styles.css").read_text(encoding="utf-8").lower()
    check(all(color in css for color in ("#58ada6", "#26615c")), "brand palette retained")
    check("prefers-reduced-motion: reduce" in css and ":focus-visible" in css, "reduced-motion fallback and keyboard focus styles")
    check(not re.search(r"(?:url\(|@import)", css), "no additional CSS asset dependencies")
    check(not re.search(r"carousel|slider|lorem|todo|placeholder", source, re.I), "no carousel or placeholders")
    check(not RESTRICTED.search(" ".join(text for _, text in doc.text)), "no restricted claims")
    if failures:
        print("FAIL: " + "\nFAIL: ".join(failures))
        raise SystemExit(1)
    check_scene_lifecycle(root)
    print("PASS: metadata, landmarks, navigation, fragments, local resources, informational contacts, scene contract, and exclusions")


if __name__ == "__main__":
    main()
