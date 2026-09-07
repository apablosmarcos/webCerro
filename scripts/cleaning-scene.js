// Decorative enhancement only: the inline SVG remains usable without JS or WebGL.
const host = document.getElementById('cleaning-scene');
const toggle = document.getElementById('scene-toggle');
const motion = matchMedia('(prefers-reduced-motion: reduce)');

if (host && toggle && !motion.matches) enhance();

async function enhance() {
  let renderer, scene, resizeObserver, intersectionObserver;
  let visible = false, paused = false, suspended = false, disposed = false;
  let previous = 0, elapsed = 0;
  const events = new AbortController();
  const geometries = new Set();
  const materials = new Set();

  function dispose() {
    if (disposed) return;
    disposed = true;
    renderer?.setAnimationLoop(null);
    events.abort();
    resizeObserver?.disconnect();
    intersectionObserver?.disconnect();
    host.classList.remove('is-ready');
    toggle.hidden = true;
    geometries.forEach(geometry => geometry.dispose());
    materials.forEach(material => material.dispose());
    renderer?.dispose();
    renderer?.domElement.remove();
  }

  try {
    // Pinned, optional CDN dependency. No remote fonts, textures or models.
    const THREE = await import('https://cdn.jsdelivr.net/npm/three@0.180.0/build/three.module.js');
    if (!host.isConnected || motion.matches) return;
    renderer = new THREE.WebGLRenderer({ antialias: true, alpha: true });
    renderer.setPixelRatio(Math.min(window.devicePixelRatio || 1, 1.5));
    host.append(renderer.domElement);
    renderer.domElement.addEventListener('webglcontextlost', event => {
      event.preventDefault();
      dispose(); // Stay on the static illustration after context loss; no retry loop.
    }, { signal: events.signal });

    scene = new THREE.Scene();
    const camera = new THREE.PerspectiveCamera(35, 1, 0.1, 40);
    camera.position.set(0, 0, 11);
    scene.add(new THREE.HemisphereLight(0xf5fff6, 0x26615c, 2.6));
    const light = new THREE.DirectionalLight(0xffffff, 3);
    light.position.set(-3, 5, 6);
    scene.add(light);

    function material(options) {
      const result = new THREE.MeshStandardMaterial(options);
      materials.add(result);
      return result;
    }
    function mesh(geometry, surface, parent, x, y, z) {
      geometries.add(geometry);
      const result = new THREE.Mesh(geometry, surface);
      result.position.set(x, y, z);
      parent.add(result);
      return result;
    }
    const teal = material({ color: 0x58ada6, roughness: 0.35, metalness: 0.25 });
    const stone = material({ color: 0x58ada6, roughness: 0.9 });
    const silver = material({ color: 0xd5e6df, roughness: 0.22, metalness: 0.7 });
    const rubber = material({ color: 0x142f2c, roughness: 0.8 });
    const glass = material({ color: 0xc7ece2, transparent: true, opacity: 0.18, roughness: 0.1, metalness: 0.35, depthWrite: false });
    const water = material({ color: 0xd9fff1, transparent: true, opacity: 0.65, roughness: 0.12, metalness: 0.3 });
    const box = (w, h, d, surface, parent, x, y, z) => mesh(new THREE.BoxGeometry(w, h, d), surface, parent, x, y, z);

    // An abstract skyline, not a reconstruction of any monument.
    const skyline = new THREE.Group();
    scene.add(skyline);
    const heights = [0.8, 1.2, 0.9, 1.8, 2.5, 1.5, 1, 1.35, 0.85];
    heights.forEach((height, index) => {
      box(0.48, height, 0.3, stone, skyline, (index - 4) * 0.5, -1.7 + height / 2, -0.9);
    });
    mesh(new THREE.ConeGeometry(0.37, 0.65, 4), stone, skyline, 0, 1.12, -0.9);
    box(0.08, 0.4, 0.08, stone, skyline, 0, 1.55, -0.9);
    box(5, 0.04, 0.4, stone, skyline, 0, -1.85, -0.9);

    const pane = new THREE.Group();
    pane.rotation.set(0.04, -0.22, -0.16);
    scene.add(pane);
    box(3.1, 4, 0.055, glass, pane, 0, 0.15, 0);
    // Shared edge geometry and droplet geometry keep the scene modest.
    const vertical = new THREE.BoxGeometry(0.015, 4, 0.025);
    const horizontal = new THREE.BoxGeometry(3.1, 0.015, 0.025);
    [-1.55, 1.55].forEach(x => mesh(vertical, silver, pane, x, 0.15, 0.02));
    [-1.85, 2.15].forEach(y => mesh(horizontal, silver, pane, 0, y, 0.02));
    const dropGeometry = new THREE.SphereGeometry(0.055, 10, 8);
    const droplets = [];
    for (let i = 0; i < 16; i++) {
      const x = Math.sin(i * 13.7) * 1.3;
      const y = -1.1 + ((i * 0.71) % 2.9);
      const drop = mesh(dropGeometry, water, pane, x, y, 0.1);
      drop.scale.set(1, 1.5 + (i % 3) * 0.2, 0.5);
      droplets.push({ drop, y });
    }
    const squeegee = new THREE.Group();
    squeegee.position.set(0.35, -0.65, 0.28);
    squeegee.rotation.z = -0.3;
    pane.add(squeegee);
    box(2.25, 0.15, 0.12, silver, squeegee, 0, 0, 0);
    box(2.28, 0.055, 0.14, rubber, squeegee, 0, 0.09, 0);
    box(0.18, 0.45, 0.16, silver, squeegee, 0, -0.24, 0);
    box(0.2, 1.05, 0.2, teal, squeegee, 0, -0.94, 0);

    function frame(time) {
      if (previous) elapsed += Math.min((time - previous) / 1000, 0.05);
      previous = time;
      pane.rotation.y = -0.22 + Math.sin(elapsed * 0.22) * 0.1;
      squeegee.position.y = -0.65 + Math.sin(elapsed * 0.35) * 0.2;
      droplets.forEach(({ drop, y }, i) => { drop.position.y = y + Math.sin(elapsed * 0.3 + i) * 0.035; });
      try { renderer.render(scene, camera); } catch { dispose(); }
    }
    function sync() {
      if (disposed) return;
      previous = 0;
      const available = visible && !document.hidden && !suspended && !motion.matches;
      host.classList.toggle('is-ready', available);
      toggle.hidden = !available;
      toggle.textContent = paused ? 'Reanudar animación' : 'Pausar animación';
      toggle.setAttribute('aria-pressed', String(paused));
      renderer.setAnimationLoop(available && !paused ? frame : null);
      if (available) frame(0);
    }
    function resize() {
      if (disposed) return;
      const { width, height } = host.getBoundingClientRect();
      if (!width || !height) return;
      camera.aspect = width / height;
      // Keep the whole glass panel in view at narrow aspect ratios.
      camera.position.z = Math.max(9, 6 / camera.aspect);
      camera.updateProjectionMatrix();
      renderer.setSize(width, height, false);
      sync();
    }
    toggle.addEventListener('click', () => { paused = !paused; sync(); }, { signal: events.signal });
    document.addEventListener('visibilitychange', sync, { signal: events.signal });
    motion.addEventListener('change', sync, { signal: events.signal });
    window.addEventListener('pagehide', event => {
      if (event.persisted) { suspended = true; sync(); } else dispose();
    }, { signal: events.signal });
    window.addEventListener('pageshow', () => { suspended = false; sync(); }, { signal: events.signal });
    resizeObserver = new ResizeObserver(resize);
    resizeObserver.observe(host);
    intersectionObserver = new IntersectionObserver(entries => {
      visible = entries[0].isIntersecting;
      sync();
    }, { threshold: 0 });
    intersectionObserver.observe(host);
    resize();
  } catch {
    dispose(); // Import, WebGL or platform failure leaves the original SVG intact.
  }
}
