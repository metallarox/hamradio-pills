// Visualizzatore 3D di Ham Radio Pills: parti STL colorate, esploso, sezione, animazione di montaggio.
// three.js da CDN; se non si carica resta visibile l'immagine di ripiego.
const V = '0.160.0', CDN = `https://cdn.jsdelivr.net/npm/three@${V}/`;
for (const box of document.querySelectorAll('.v3d')) {
  const start = () => init(box).catch(e => { console.warn(e); box.classList.add('v3d-fail'); });
  if ('IntersectionObserver' in window) {
    const io = new IntersectionObserver(es => { if (es.some(e => e.isIntersecting)) { io.disconnect(); start(); } }, { rootMargin: '200px' });
    io.observe(box);
  } else start();
}
async function init(box) {
  const THREE = await import('three');   // dall'importmap della pagina
  const { STLLoader } = await import(CDN + 'examples/jsm/loaders/STLLoader.js');
  const { OrbitControls } = await import(CDN + 'examples/jsm/controls/OrbitControls.js');
  const parts = JSON.parse(box.dataset.parts);       // [{id, file, color, label, explode}]
  const base = box.dataset.base;
  const stage = box.querySelector('.v3d-stage');
  const renderer = new THREE.WebGLRenderer({ antialias: true, alpha: true });
  renderer.setPixelRatio(Math.min(devicePixelRatio || 1, 2));
  renderer.localClippingEnabled = true;
  stage.appendChild(renderer.domElement);
  const scene = new THREE.Scene();
  const camera = new THREE.PerspectiveCamera(35, 1, 1, 2000);
  camera.up.set(0, 0, 1);
  const home = new THREE.Vector3(95, -150, 125);
  camera.position.copy(home);
  const controls = new OrbitControls(camera, renderer.domElement);
  controls.enableDamping = true; controls.target.set(0, 0, 22); controls.update();
  scene.add(new THREE.HemisphereLight(0xffffff, 0x445566, 1.1));
  const sun = new THREE.DirectionalLight(0xffffff, 1.5); sun.position.set(60, -80, 140); scene.add(sun);
  const fill = new THREE.DirectionalLight(0xffffff, 0.5); fill.position.set(-80, 60, 40); scene.add(fill);
  const cutPlane = new THREE.Plane(new THREE.Vector3(0, 1, 0), 0);
  const loader = new STLLoader(), meshes = {};
  await Promise.all(parts.map(async p => {
    const geo = await loader.loadAsync(base + p.file);
    geo.computeVertexNormals();
    const mat = new THREE.MeshStandardMaterial({ color: p.color, roughness: .55, metalness: .05, side: THREE.DoubleSide, clippingPlanes: [] });
    const mesh = new THREE.Mesh(geo, mat); mesh.userData = p; scene.add(mesh); meshes[p.id] = mesh;
  }));
  // stato
  let t = 0, cut = false, playing = null;
  const slider = box.querySelector('.v3d-explode');
  const apply = () => {
    for (const m of Object.values(meshes)) m.position.z = (m.userData.explode || 0) * t;
    if (slider) slider.value = Math.round(t * 100);
  };
  const setCut = on => {
    cut = on; box.querySelector('.v3d-cut')?.classList.toggle('on', on);
    for (const m of Object.values(meshes)) m.material.clippingPlanes = on && !m.userData.noclip ? [cutPlane] : [];
  };
  apply();
  slider?.addEventListener('input', () => { stop(); t = slider.value / 100; apply(); });
  const stop = () => { if (playing) cancelAnimationFrame(playing); playing = null; };
  const tween = (to, ms) => { stop(); const t0 = t, s = performance.now();
    const step = now => { const k = Math.min(1, (now - s) / ms), e = k < .5 ? 2 * k * k : 1 - Math.pow(-2 * k + 2, 2) / 2;
      t = t0 + (to - t0) * e; apply(); playing = k < 1 ? requestAnimationFrame(step) : null; };
    playing = requestAnimationFrame(step); };
  box.querySelector('.v3d-mounted')?.addEventListener('click', () => tween(0, 700));
  box.querySelector('.v3d-exploded')?.addEventListener('click', () => tween(1, 700));
  box.querySelector('.v3d-play')?.addEventListener('click', () => { t = 1; apply(); setTimeout(() => tween(0, 2600), 250); });
  box.querySelector('.v3d-cut')?.addEventListener('click', () => setCut(!cut));
  box.querySelector('.v3d-home')?.addEventListener('click', () => { camera.position.copy(home); controls.target.set(0, 0, 22); controls.update(); });
  const rot = box.querySelector('.v3d-rotate');
  rot?.addEventListener('click', () => { controls.autoRotate = !controls.autoRotate; rot.classList.toggle('on', controls.autoRotate); });
  for (const cb of box.querySelectorAll('.v3d-legend input')) cb.addEventListener('change', () => { meshes[cb.value].visible = cb.checked; });
  const resize = () => { const w = stage.clientWidth, h = stage.clientHeight; renderer.setSize(w, h, false); camera.aspect = w / h; camera.updateProjectionMatrix(); };
  new ResizeObserver(resize).observe(stage); resize();
  box.classList.add('v3d-ready');
  renderer.setAnimationLoop(() => { controls.update(); renderer.render(scene, camera); });
}
