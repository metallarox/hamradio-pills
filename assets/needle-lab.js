// Ham Radio Pills · animazioni del "vezzo matematico" (ago del secondo ordine).
// Stesso algoritmo di fluke_hydra_monitor.py: Euler semi-implicito a passi di 8 ms, fermi a ±(5,5 % + 1 %),
// rimbalzo con la velocità invertita e ridotta al 25 %. Nessuna libreria esterna.
(() => {
const PEG = 0.055, DT = 0.008, HI = 1 + PEG + 0.01, LO = -PEG - 0.01;
const np = (x, d = 2) => (x < 0 ? '(' + nf(x, d) + ')' : nf(x, d));
const nf = (x, d = 2) => Number.isFinite(x) ? x.toFixed(d).replace('.', ',').replace(/^-/, '−') : '—';
const clamp = (v, a, b) => Math.max(a, Math.min(b, v));
const el = (h) => { const d = document.createElement('div'); d.innerHTML = h.trim(); return d.firstElementChild; };
function theme() {
  const dk = document.documentElement.getAttribute('data-theme') === 'dark';
  return dk ? { dk, ink: '#e6eef7', mute: '#93a3b8', grid: 'rgba(255,255,255,.09)', axis: '#5a6a80', o: '#ff7a5c', b: '#4cc3f5', g: '#4fc27a', p: '#b48cf0', bez: '#0b1220', wall: '#3a4a60' }
            : { dk, ink: '#0a1a2e', mute: '#64748b', grid: 'rgba(10,26,46,.08)', axis: '#9aa5b4', o: '#e0563b', b: '#1593d1', g: '#2a9d5c', p: '#8e5bd1', bez: '#1d222b', wall: '#9aa5b4' };
}
function canvasIn(host) {
  const cv = document.createElement('canvas'); host.appendChild(cv);
  const o = { cv, ctx: cv.getContext('2d'), w: 1, h: 1 };
  const rs = () => { const r = host.getBoundingClientRect(), d = Math.min(devicePixelRatio || 1, 2);
    o.w = Math.max(1, r.width); o.h = Math.max(1, r.height);
    cv.width = Math.round(o.w * d); cv.height = Math.round(o.h * d); o.ctx.setTransform(d, 0, 0, d, 0, 0); };
  new ResizeObserver(rs).observe(host); rs(); return o;
}
function loop(root, step) {           // anima solo quando il riquadro è visibile
  let vis = false, last = 0, raf = 0;
  const tick = now => { const dt = Math.min(0.05, (now - last) / 1000); last = now; step(dt, now); raf = vis ? requestAnimationFrame(tick) : 0; };
  new IntersectionObserver(es => { vis = es[0].isIntersecting; if (vis && !raf) { last = performance.now(); raf = requestAnimationFrame(tick); } }).observe(root);
}
function rr(c, x, y, w, h, r) { c.beginPath(); c.moveTo(x + r, y); c.arcTo(x + w, y, x + w, y + h, r); c.arcTo(x + w, y + h, x, y + h, r); c.arcTo(x, y + h, x, y, r); c.arcTo(x, y, x + w, y, r); c.closePath(); }
function arrow(c, x1, y1, x2, y2, col, lw = 3) {
  const L = Math.hypot(x2 - x1, y2 - y1); if (L < 2) return;
  const a = Math.atan2(y2 - y1, x2 - x1), hl = Math.min(10, L * 0.5);
  c.strokeStyle = c.fillStyle = col; c.lineWidth = lw; c.beginPath(); c.moveTo(x1, y1); c.lineTo(x2 - hl * 0.8 * Math.cos(a), y2 - hl * 0.8 * Math.sin(a)); c.stroke();
  c.beginPath(); c.moveTo(x2, y2); c.lineTo(x2 - hl * Math.cos(a - 0.45), y2 - hl * Math.sin(a - 0.45)); c.lineTo(x2 - hl * Math.cos(a + 0.45), y2 - hl * Math.sin(a + 0.45)); c.closePath(); c.fill();
}
// cornice di un grafico: restituisce le funzioni di scala
function frame(o, T, { x0, x1, y0, y1, yt = [], yl = v => v, xt = [], xl = v => v, xlab = '', ylab = '', logx = false }) {
  const c = o.ctx, w = o.w, h = o.h, P = { l: 46, r: 12, t: 10, b: xlab ? 36 : 22 };
  const fx = logx ? v => Math.log10(v) : v => v;
  const X = v => P.l + (fx(v) - fx(x0)) / (fx(x1) - fx(x0)) * (w - P.l - P.r), Y = v => h - P.b - (v - y0) / (y1 - y0) * (h - P.t - P.b);
  c.font = '11px system-ui, sans-serif'; c.lineWidth = 1;
  for (const v of yt) { c.strokeStyle = T.grid; c.beginPath(); c.moveTo(P.l, Y(v)); c.lineTo(w - P.r, Y(v)); c.stroke(); c.fillStyle = T.mute; c.textAlign = 'right'; c.fillText(yl(v), P.l - 6, Y(v) + 4); }
  for (const v of xt) { c.strokeStyle = T.grid; c.beginPath(); c.moveTo(X(v), P.t); c.lineTo(X(v), h - P.b); c.stroke(); c.fillStyle = T.mute; c.textAlign = 'center'; c.fillText(xl(v), X(v), h - P.b + 14); }
  c.strokeStyle = T.axis; c.beginPath(); c.moveTo(P.l, P.t); c.lineTo(P.l, h - P.b); c.lineTo(w - P.r, h - P.b); c.stroke();
  if (xlab) { c.fillStyle = T.mute; c.textAlign = 'center'; c.fillText(xlab, (P.l + w - P.r) / 2, h - 6); }
  if (ylab) { c.save(); c.translate(11, (P.t + h - P.b) / 2); c.rotate(-Math.PI / 2); c.fillStyle = T.mute; c.textAlign = 'center'; c.fillText(ylab, 0, 0); c.restore(); }
  return { X, Y, P };
}
function stepResp(z, wn, t) {
  if (t <= 0) return 0;
  if (z < 0.995) { const wd = wn * Math.sqrt(1 - z * z); return 1 - Math.exp(-z * wn * t) / Math.sqrt(1 - z * z) * Math.sin(wd * t + Math.acos(z)); }
  if (z < 1.005) return 1 - (1 + wn * t) * Math.exp(-wn * t);
  const r = Math.sqrt(z * z - 1), s1 = -wn * (z - r), s2 = -wn * (z + r);
  return 1 + (s2 * Math.exp(s1 * t) - s1 * Math.exp(s2 * t)) / (s1 - s2);
}

// ---------------------------------------------------------------- simulazione dell'ago
class Needle {
  constructor() { this.x = 0; this.v = 0; this.a = 0; this.tgt = 0; this.z = 0.55; this.wn = 13; this.e = 0.25; this.ol = false; this.acc = 0; this.t = 0; this.hit = null; }
  set(v) { this.ol = v > 1; this.tgt = clamp(v, -PEG, 1 + PEG); }
  run(dt, before) { this.acc += dt; let n = 0; while (this.acc >= DT && n++ < 60) { this.acc -= DT; this.t += DT; if (before) before(this.t); this.one(); } }
  one() {
    this.a = this.wn * this.wn * (this.tgt - this.x) - 2 * this.z * this.wn * this.v;
    this.v += this.a * DT; this.x += this.v * DT;
    if (this.x > HI || this.x < LO) { const vb = this.v; this.x = clamp(this.x, LO, HI); this.v *= -this.e; this.hit = { vb, va: this.v, t: performance.now(), top: this.x > 0.5 }; }
  }
}
function drawMeter(o, n, T, label = '%') {
  const c = o.ctx, w = o.w, h = o.h; c.clearRect(0, 0, w, h);
  rr(c, 4, 4, w - 8, h - 8, 14); c.fillStyle = T.bez; c.fill();
  rr(c, 14, 14, w - 28, h - 28, 8); c.fillStyle = '#f3ecd7'; c.fill();
  const R = Math.min((w - 40) * 0.56, (h - 40) * 0.92), cx = w / 2, cy = 14 + (h - 28) * 0.5 + R * 0.62;
  const A0 = -50 * Math.PI / 180, SP = 100 * Math.PI / 180, ang = p => A0 + SP * p, pt = (p, r) => [cx + r * Math.sin(ang(p)), cy - r * Math.cos(ang(p))];
  c.lineWidth = Math.max(4, R * 0.05); c.strokeStyle = 'rgba(120,130,140,.35)'; c.beginPath(); c.arc(cx, cy, R * 0.80, ang(0) - Math.PI / 2, ang(1) - Math.PI / 2); c.stroke();
  c.strokeStyle = '#2b2b2b'; c.fillStyle = '#2b2b2b'; c.textAlign = 'center'; c.font = `${Math.max(10, R * 0.09)}px system-ui, sans-serif`;
  c.lineWidth = 1.2; c.beginPath(); c.arc(cx, cy, R * 0.90, ang(0) - Math.PI / 2, ang(1) - Math.PI / 2); c.stroke();
  for (let i = 0; i <= 50; i++) { const p = i / 50, L = i % 5 ? 0.04 : 0.08, [x1, y1] = pt(p, R * 0.90), [x2, y2] = pt(p, R * (0.90 + L)); c.lineWidth = i % 5 ? 1 : 1.8; c.beginPath(); c.moveTo(x1, y1); c.lineTo(x2, y2); c.stroke();
    if (i % 10 === 0) { const [tx, ty] = pt(p, R * 1.06); c.fillText(String(i * 2), tx, ty + 4); } }
  c.font = `${Math.max(11, R * 0.11)}px system-ui, sans-serif`; c.fillText(label, cx, cy - R * 0.35);
  for (const p of [LO - 0.012, HI + 0.012]) { const [px, py] = pt(p, R * 0.86); c.beginPath(); c.arc(px, py, Math.max(3, R * 0.025), 0, 7); c.fillStyle = '#555'; c.fill(); }
  const [gx, gy] = pt(n.tgt, R * 0.985); c.fillStyle = T.o; c.beginPath(); c.moveTo(gx, gy); const [g1x, g1y] = pt(n.tgt - 0.018, R * 1.10), [g2x, g2y] = pt(n.tgt + 0.018, R * 1.10); c.lineTo(g1x, g1y); c.lineTo(g2x, g2y); c.fill();
  const [nx, ny] = pt(n.x, R * 0.97);
  c.strokeStyle = 'rgba(0,0,0,.18)'; c.lineWidth = 2.4; c.beginPath(); c.moveTo(cx + 3, cy + 3); c.lineTo(nx + 3, ny + 4); c.stroke();
  c.strokeStyle = '#141414'; c.lineWidth = 2.2; c.beginPath(); c.moveTo(cx, cy); c.lineTo(nx, ny); c.stroke();
  c.beginPath(); c.arc(cx, cy, Math.max(6, R * 0.07), 0, 7); c.fillStyle = '#222'; c.fill();
  const lx = w - 34, ly = 30; c.beginPath(); c.arc(lx, ly, 7, 0, 7); c.fillStyle = n.ol ? '#ff3b30' : '#6d1a17'; c.fill();
  if (n.ol) { c.shadowColor = '#ff3b30'; c.shadowBlur = 12; c.fill(); c.shadowBlur = 0; }
  c.fillStyle = '#2b2b2b'; c.font = '10px system-ui, sans-serif'; c.fillText('OL', lx, ly + 20);
  if (n.hit && performance.now() - n.hit.t < 250) { const [hx, hy] = pt(n.hit.top ? HI + 0.012 : LO - 0.012, R * 0.86); c.strokeStyle = T.o; c.lineWidth = 2; c.beginPath(); c.arc(hx, hy, 10 + (performance.now() - n.hit.t) / 25, 0, 7); c.stroke(); }
}
function drawMSD(o, n, T) {
  const c = o.ctx, w = o.w, h = o.h; c.clearRect(0, 0, w, h);
  const xw = 26, mw = 54, mh = 58, base = h * 0.62, range = w - xw - mw - 70, X = v => xw + 46 + (v - LO) / (HI - LO) * range;
  c.fillStyle = T.wall; c.fillRect(xw - 12, base - mh - 26, 12, mh + 52);
  for (let y = base - mh - 26; y < base + 26; y += 9) { c.strokeStyle = T.axis; c.lineWidth = 1; c.beginPath(); c.moveTo(xw - 12, y + 9); c.lineTo(xw - 20, y + 17); c.stroke(); }
  c.strokeStyle = T.axis; c.lineWidth = 1.5; c.beginPath(); c.moveTo(xw, base + 26); c.lineTo(w - 10, base + 26); c.stroke();
  const mx = X(n.x), y1 = base - mh * 0.72, y2 = base - mh * 0.26;
  // molla
  c.strokeStyle = T.g; c.lineWidth = 2.2; c.beginPath(); c.moveTo(xw, y1); const s0 = xw + 10, s1 = mx - 8, N = 14; c.lineTo(s0, y1);
  for (let i = 1; i < N; i++) c.lineTo(s0 + (s1 - s0) * i / N, y1 + (i % 2 ? -9 : 9)); c.lineTo(s1, y1); c.lineTo(mx, y1); c.stroke();
  // smorzatore: cilindro fisso, pistone sulla massa
  const cylL = X(HI) - X(LO) + 30, cx0 = xw + 8; c.strokeStyle = T.b; c.lineWidth = 2; c.beginPath(); c.moveTo(xw, y2); c.lineTo(cx0, y2); c.stroke();
  c.beginPath(); c.moveTo(cx0 + cylL, y2 - 9); c.lineTo(cx0, y2 - 9); c.lineTo(cx0, y2 + 9); c.lineTo(cx0 + cylL, y2 + 9); c.stroke();
  c.fillStyle = T.dk ? 'rgba(76,195,245,.12)' : 'rgba(21,147,209,.10)'; c.fillRect(cx0, y2 - 9, cylL, 18);
  const px = mx - (X(HI) - cx0 - cylL + 18 + (X(HI) - X(LO))); const pist = clamp(cx0 + 12 + (n.x - LO) / (HI - LO) * (cylL - 24), cx0 + 6, cx0 + cylL - 6);
  c.lineWidth = 3; c.beginPath(); c.moveTo(pist, y2 - 7); c.lineTo(pist, y2 + 7); c.stroke(); c.lineWidth = 2; c.beginPath(); c.moveTo(pist, y2); c.lineTo(mx, y2); c.stroke(); void px;
  // massa
  rr(c, mx, base - mh, mw, mh, 6); c.fillStyle = T.ink; c.fill(); c.fillStyle = T.dk ? '#0b1220' : '#fff'; c.font = 'bold 12px system-ui, sans-serif'; c.textAlign = 'center'; c.fillText('J', mx + mw / 2, base - mh / 2 + 4);
  // obiettivo
  const gx = X(n.tgt) + mw / 2; c.setLineDash([5, 4]); c.strokeStyle = T.o; c.lineWidth = 1.5; c.beginPath(); c.moveTo(gx, 18); c.lineTo(gx, base + 26); c.stroke(); c.setLineDash([]);
  c.fillStyle = T.o; c.font = '11px system-ui, sans-serif'; c.fillText('obiettivo', gx, 13);
  // forze (scala comune)
  const k = n.wn * n.wn, s = Math.min(70, range * 0.32) / (k * 1.1), cxm = mx + mw / 2, fy = base + 46;
  const F = [[k * n.tgt, T.o, 'bobina'], [-k * n.x, T.g, 'molla'], [-2 * n.z * n.wn * n.v, T.b, 'smorz.']];
  F.forEach(([f, col, lab], i) => { const y = fy + i * 15; arrow(c, cxm, y, cxm + clamp(f * s, -range * 0.6, range * 0.6), y, col, 2.5); c.fillStyle = col; c.font = '10px system-ui, sans-serif'; c.textAlign = f >= 0 ? 'right' : 'left'; c.fillText(lab, cxm + (f >= 0 ? -6 : 6), y + 3); });
  arrow(c, cxm, base - mh - 12, cxm + clamp(n.a * s, -range * 0.6, range * 0.6), base - mh - 12, T.ink, 3);
  c.fillStyle = T.ink; c.font = '11px system-ui, sans-serif'; c.textAlign = 'left'; c.fillText("x'' (somma)", Math.min(cxm, w - 80) + 4, base - mh - 20);
}
function drawStrip(o, hist, T, win, now, opts = {}) {
  const c = o.ctx; c.clearRect(0, 0, o.w, o.h);
  const y0 = opts.y0 ?? -0.15, y1 = opts.y1 ?? 1.25;
  const { X, Y, P } = frame(o, T, { x0: now - win, x1: now, y0, y1, yt: opts.yt || [0, 0.5, 1], yl: opts.yl || (v => Math.round(v * 100) + ' %'), xlab: opts.xlab || 'tempo (scorre verso sinistra)' });
  c.save(); c.beginPath(); c.rect(P.l, 0, o.w - P.l - P.r, o.h); c.clip();
  if (opts.stops) { c.setLineDash([2, 4]); c.strokeStyle = T.mute; c.beginPath(); c.moveTo(P.l, Y(HI)); c.lineTo(o.w, Y(HI)); c.stroke(); c.setLineDash([]); c.fillStyle = T.mute; c.textAlign = 'left'; c.fillText('fermo', P.l + 4, Y(HI) - 4); }
  c.setLineDash([6, 4]); c.strokeStyle = T.o; c.lineWidth = 1.6; c.beginPath(); hist.forEach((p, i) => i ? c.lineTo(X(p[0]), Y(p[2])) : c.moveTo(X(p[0]), Y(p[2]))); c.stroke(); c.setLineDash([]);
  c.strokeStyle = T.dk ? T.b : T.ink; c.lineWidth = 2.4; c.beginPath(); hist.forEach((p, i) => i ? c.lineTo(X(p[0]), Y(p[1])) : c.moveTo(X(p[0]), Y(p[1]))); c.stroke();
  c.restore();
}

// ---------------------------------------------------------------- 1) laboratorio: ago, molla e smorzatore
function lab(root) {
  const bounce = root.dataset.w === 'bounce';
  const btns = bounce ? [['0 %', 0], ['50 %', 0.5], ['80 %', 0.8], ['94 %', 0.94], ['97 %', 0.97], ['Overload', 1.2]] : [['0 %', 0], ['25 %', 0.25], ['50 %', 0.5], ['80 %', 0.8], ['100 %', 1], ['Overload', 1.2]];
  root.append(el(`<div class="nl-row${bounce ? ' solo' : ''}"><div class="nl-cv nl-meter"></div>${bounce ? '' : '<div class="nl-cv nl-msd"></div>'}</div>`));
  if (!bounce) root.append(el(`<div class="nl-eq"></div>`));
  root.append(el(`<div class="nl-cv nl-strip"></div>`));
  root.append(el(`<div class="nl-ctl"><div class="nl-btns">${btns.map(([l, v]) => `<button data-v="${v}">${l}</button>`).join('')}<button class="nl-demo">▶ Demo</button></div>
    <div class="nl-sl">${bounce ? `<label>restituzione e <input type="range" min="0" max="0.9" step="0.05" value="0.25" data-k="e"><b data-o="e"></b></label>`
      : `<label>ζ <input type="range" min="0" max="2" step="0.01" value="0.55" data-k="z"><b data-o="z"></b></label><label>ωn <input type="range" min="3" max="30" step="0.5" value="13" data-k="wn"><b data-o="wn"></b></label><button class="nl-reset">valori del programma</button>`}</div>
    <div class="nl-read"></div></div>`));
  const n = new Needle(), M = canvasIn(root.querySelector('.nl-meter')), S = canvasIn(root.querySelector('.nl-strip')), D = bounce ? null : canvasIn(root.querySelector('.nl-msd'));
  const eq = root.querySelector('.nl-eq'), rd = root.querySelector('.nl-read'), hist = []; let t = 0, demo = false, dIdx = 0, dT = 0, lastTxt = 0, impacts = [];
  const seq = bounce ? [0.8, 0, 1.2, 0, 0.97, 0.3] : [0.25, 0.8, 0.4, 1.2, 0.1, 0.95, 0];
  const sync = () => { for (const s of root.querySelectorAll('input[data-k]')) { n[s.dataset.k] = +s.value; root.querySelector(`[data-o="${s.dataset.k}"]`).textContent = nf(+s.value, s.dataset.k === 'wn' ? 1 : 2); } info(); };
  const info = () => {
    if (bounce) return;
    const z = n.z, wn = n.wn; let s = `<span>ωn = ${nf(wn, 1)} rad/s (${nf(wn / 2 / Math.PI, 2)} Hz)</span>`;
    if (z > 0 && z < 1) { const wd = wn * Math.sqrt(1 - z * z); s += `<span>ωd = ${nf(wd, 2)} rad/s</span><span>sovraelongazione ${nf(100 * Math.exp(-Math.PI * z / Math.sqrt(1 - z * z)), 1)} %</span><span>picco a ${nf(Math.PI / wd, 2)} s</span><span>assestamento 2 % ≈ ${nf(4 / (z * wn), 2)} s</span>`; }
    else if (z === 0) s += `<span>ζ = 0: oscilla senza fermarsi</span>`;
    else s += `<span>${z === 1 ? 'smorzamento critico' : 'sovrasmorzato'}: nessuna sovraelongazione</span>`;
    rd.innerHTML = s;
  };
  root.querySelectorAll('input[data-k]').forEach(s => s.addEventListener('input', sync));
  root.querySelectorAll('.nl-btns button[data-v]').forEach(b => b.addEventListener('click', () => { demo = false; root.querySelector('.nl-demo').classList.remove('on'); n.set(+b.dataset.v); }));
  root.querySelector('.nl-demo').addEventListener('click', e => { demo = !demo; e.target.classList.toggle('on', demo); dT = 0; });
  root.querySelector('.nl-reset')?.addEventListener('click', () => { root.querySelector('[data-k="z"]').value = 0.55; root.querySelector('[data-k="wn"]').value = 13; sync(); });
  sync(); n.set(bounce ? 0.8 : 0.25); demo = true; root.querySelector('.nl-demo').classList.add('on');
  const L = (cls, s) => `<span class="${cls}">${s}</span>`;
  loop(root, (dt) => {
    const T = theme();
    if (demo) { dT -= dt; if (dT <= 0) { n.set(seq[dIdx++ % seq.length]); dT = 2.2; } }
    n.run(dt, tt => { if (bounce && n.hit && n.hit.t === -1) n.hit = null; });
    if (n.hit && n.hit !== impacts[0]) { impacts.unshift(n.hit); impacts.length = Math.min(impacts.length, 3); }
    t += dt; hist.push([t, n.x, n.tgt]); while (hist.length && hist[0][0] < t - 3.2) hist.shift();
    drawMeter(M, n, T); if (D) drawMSD(D, n, T); drawStrip(S, hist, T, 3, t, { stops: bounce, y1: 1.2 });
    if (performance.now() - lastTxt > 110) { lastTxt = performance.now();
      if (eq) { const k = n.wn * n.wn, c2 = 2 * n.z * n.wn;
        eq.innerHTML = `<div>x'' = ${L('co', 'ωn²·obiettivo')} − ${L('cg', 'ωn²·x')} − ${L('cb', "2·ζ·ωn·x'")}</div>
          <div>&nbsp;&nbsp;&nbsp;= ${L('co', nf(k, 1) + '·' + np(n.tgt, 3))} − ${L('cg', nf(k, 1) + '·' + np(n.x, 3))} − ${L('cb', nf(c2, 2) + '·' + np(n.v, 3))}</div>
          <div>&nbsp;&nbsp;&nbsp;= ${L('co', np(k * n.tgt, 1))} − ${L('cg', np(k * n.x, 1))} − ${L('cb', np(c2 * n.v, 1))} = <b>${nf(n.a, 1)}</b> 1/s²</div>`; }
      if (bounce) { const h0 = impacts[0]; rd.innerHTML = h0 ? `<span>ultimo urto: velocità ${nf(h0.vb, 2)} → ${nf(h0.va, 2)} (fondo scala al secondo)</span><span>energia rimasta e² = ${nf(100 * n.e * n.e, 0)} %</span>` : `<span>nessun urto: il salto non basta a raggiungere il fermo</span>`; }
    }
  });
}

// ---------------------------------------------------------------- 2) poli e risposta al gradino
function poles(root) {
  root.append(el(`<div class="nl-row"><div class="nl-cv nl-sq"></div><div class="nl-cv nl-wide"></div></div>`));
  root.append(el(`<div class="nl-ctl"><div class="nl-sl"><label>ζ <input type="range" min="0" max="1.6" step="0.01" value="0.55"><b></b></label><button class="nl-reset">ζ = 0,55</button></div><div class="nl-read"></div></div>`));
  const A = canvasIn(root.querySelector('.nl-sq')), B = canvasIn(root.querySelector('.nl-wide')), sl = root.querySelector('input'), out = root.querySelector('.nl-sl b'), rd = root.querySelector('.nl-read');
  const wn = 13; let z = 0.55, tau = 0, txt = '';
  const upd = () => { z = +sl.value; out.textContent = nf(z, 2);
    let s; if (z < 1) { const wd = wn * Math.sqrt(1 - z * z); s = `<span>poli: s = −${nf(z * wn, 2)} ± j·${nf(wd, 2)}</span><span>angolo arccos ζ = ${nf(Math.acos(z) * 180 / Math.PI, 1)}°</span>${z > 0 ? `<span>sovraelongazione ${nf(100 * Math.exp(-Math.PI * z / Math.sqrt(1 - z * z)), 1)} %</span>` : ''}`; }
    else { const r = Math.sqrt(z * z - 1); s = `<span>poli reali: s = −${nf(wn * (z - r), 2)} e −${nf(wn * (z + r), 2)}</span><span>nessuna oscillazione</span>`; }
    rd.innerHTML = s; };
  sl.addEventListener('input', upd); root.querySelector('.nl-reset').addEventListener('click', () => { sl.value = 0.55; upd(); }); upd();
  loop(root, dt => {
    const T = theme(); tau += dt; const Tw = 1.4, cyc = Tw + 0.6, tt = Math.min(tau % cyc, Tw);
    // piano s
    let c = A.ctx; c.clearRect(0, 0, A.w, A.h);
    const { X, Y } = frame(A, T, { x0: -16, x1: 3, y0: -16, y1: 16, yt: [-10, 0, 10], xt: [-15, -10, -5, 0], xlab: 'parte reale (1/s)', ylab: 'parte immaginaria' });
    c.strokeStyle = T.ink; c.lineWidth = 1; c.beginPath(); c.moveTo(X(-16), Y(0)); c.lineTo(X(3), Y(0)); c.moveTo(X(0), Y(-16)); c.lineTo(X(0), Y(16)); c.stroke();
    c.setLineDash([4, 4]); c.strokeStyle = T.axis; c.beginPath(); for (let a = Math.PI / 2; a <= 1.5 * Math.PI + 0.01; a += 0.05) { const px = X(wn * Math.cos(a)), py = Y(wn * Math.sin(a)); a === Math.PI / 2 ? c.moveTo(px, py) : c.lineTo(px, py); } c.stroke(); c.setLineDash([]);
    let P;
    if (z < 1) { const wd = wn * Math.sqrt(1 - z * z); P = [[-z * wn, wd], [-z * wn, -wd]];
      c.strokeStyle = T.o; c.lineWidth = 1.2; c.beginPath(); c.moveTo(X(0), Y(0)); c.lineTo(X(-z * wn), Y(wd)); c.stroke();
      c.beginPath(); c.arc(X(0), Y(0), 26, Math.PI, Math.PI + Math.acos(z), false); c.stroke();
      c.fillStyle = T.o; c.font = '11px system-ui'; c.textAlign = 'left'; c.fillText('ωn = 13', X(-z * wn / 2) + 6, Y(wd / 2));
      c.fillStyle = T.mute; c.fillText('−ζ·ωn', X(-z * wn) - 14, Y(0) + 14);
    } else { const r = Math.sqrt(z * z - 1); P = [[-wn * (z - r), 0], [-wn * (z + r), 0]]; }
    for (const [x, y] of P) { const px = X(x), py = Y(y); c.strokeStyle = T.o; c.lineWidth = 3; c.beginPath(); c.moveTo(px - 7, py - 7); c.lineTo(px + 7, py + 7); c.moveTo(px - 7, py + 7); c.lineTo(px + 7, py - 7); c.stroke(); }
    // risposta disegnata nel tempo, con l'inviluppo
    c = B.ctx; c.clearRect(0, 0, B.w, B.h);
    const F = frame(B, T, { x0: 0, x1: Tw, y0: 0, y1: 2, yt: [0, 0.5, 1, 1.5, 2], yl: v => nf(v, 1), xt: [0, 0.2, 0.4, 0.6, 0.8, 1, 1.2, 1.4], xl: v => nf(v, 1), xlab: 'tempo (s)' });
    if (z > 0 && z < 1) { const k = 1 / Math.sqrt(1 - z * z); c.setLineDash([5, 4]); c.strokeStyle = T.g; c.lineWidth = 1.3;
      for (const sg of [1, -1]) { c.beginPath(); for (let i = 0; i <= 140; i++) { const x = Tw * i / 140, y = clamp(1 + sg * k * Math.exp(-z * wn * x), -1, 3); i ? c.lineTo(F.X(x), F.Y(y)) : c.moveTo(F.X(x), F.Y(y)); } c.stroke(); }
      c.setLineDash([]); c.fillStyle = T.g; c.font = '11px system-ui'; c.textAlign = 'left'; c.fillText('inviluppo 1 ± e^(−ζ·ωn·t)/√(1−ζ²)', F.X(0.55), F.Y(1.75)); }
    c.strokeStyle = T.axis; c.setLineDash([2, 3]); c.beginPath(); c.moveTo(F.X(0), F.Y(1)); c.lineTo(F.X(Tw), F.Y(1)); c.stroke(); c.setLineDash([]);
    c.strokeStyle = T.o; c.lineWidth = 2.6; c.beginPath(); for (let i = 0; i <= 200; i++) { const x = tt * i / 200, y = clamp(stepResp(z, wn, x), -0.5, 2.5); i ? c.lineTo(F.X(x), F.Y(y)) : c.moveTo(F.X(x), F.Y(y)); } c.stroke();
    const yy = clamp(stepResp(z, wn, tt), -0.5, 2.5); c.fillStyle = T.o; c.beginPath(); c.arc(F.X(tt), F.Y(yy), 5, 0, 7); c.fill();
  });
}

// ---------------------------------------------------------------- 3) risposta in frequenza
function freq(root) {
  root.append(el(`<div class="nl-row three"><div class="nl-cv nl-meter"></div><div class="nl-cv nl-wide"></div><div class="nl-cv nl-wide"></div></div>`));
  root.append(el(`<div class="nl-ctl"><div class="nl-btns"><button data-f="0.2">0,2 Hz</button><button data-f="1">1 Hz</button><button data-f="1.3">1,3 Hz (picco)</button><button data-f="2.5">2,5 Hz</button><button data-f="6">6 Hz</button></div>
    <div class="nl-sl"><label>frequenza della lettura <input type="range" min="0" max="100" step="0.5" value="50"><b></b></label></div><div class="nl-read"></div></div>`));
  const cvs = root.querySelectorAll('.nl-cv'), M = canvasIn(cvs[0]), S = canvasIn(cvs[1]), Bd = canvasIn(cvs[2]);
  const sl = root.querySelector('input'), out = root.querySelector('.nl-sl b'), rd = root.querySelector('.nl-read');
  const n = new Needle(), z = 0.55, wn = 13, A = 0.35; let f = 1, since = 0, t = 0, hist = [], txt = 0;
  const H = w => wn * wn / Math.sqrt((wn * wn - w * w) ** 2 + (2 * z * wn * w) ** 2), ph = w => -Math.atan2(2 * z * wn * w, wn * wn - w * w) * 180 / Math.PI;
  const setF = v => { f = v; sl.value = 50 * Math.log10(f / 0.1); out.textContent = nf(f, 2) + ' Hz'; since = 0; };
  sl.addEventListener('input', () => { f = 0.1 * Math.pow(10, sl.value / 50); out.textContent = nf(f, 2) + ' Hz'; since = 0; });
  root.querySelectorAll('[data-f]').forEach(b => b.addEventListener('click', () => setF(+b.dataset.f))); setF(1);
  let ph0 = 0;
  loop(root, dt => {
    const T = theme(); since += dt; t += dt;
    n.run(dt, tt => { ph0 += 2 * Math.PI * f * DT; n.set(0.5 + A * Math.sin(ph0)); });
    hist.push([t, n.x, n.tgt]); const win = clamp(3 / f, 2, 12); while (hist.length && hist[0][0] < t - 12.5) hist.shift();
    drawMeter(M, n, T);
    drawStrip(S, hist.filter(p => p[0] > t - win - 0.1), T, win, t, { y0: 0, y1: 1, yt: [0.15, 0.5, 0.85], xlab: `ultimi ${nf(win, 1)} s` });
    let c = Bd.ctx; c.clearRect(0, 0, Bd.w, Bd.h);
    const F = frame(Bd, T, { x0: 0.1, x1: 10, y0: -30, y1: 6, yt: [-30, -20, -10, -3, 0, 6], yl: v => (v > 0 ? '+' : '') + v + ' dB', xt: [0.1, 0.3, 1, 3, 10], xl: v => nf(v, v < 1 ? 1 : 0), logx: true, xlab: 'frequenza (Hz)' });
    c.strokeStyle = T.ink; c.lineWidth = 2; c.beginPath(); for (let i = 0; i <= 200; i++) { const fr = 0.1 * Math.pow(100, i / 200), g = 20 * Math.log10(H(2 * Math.PI * fr)); i ? c.lineTo(F.X(fr), F.Y(clamp(g, -32, 8))) : c.moveTo(F.X(fr), F.Y(g)); } c.stroke();
    const g = 20 * Math.log10(H(2 * Math.PI * f)); c.fillStyle = T.o; c.beginPath(); c.arc(F.X(f), F.Y(clamp(g, -30, 6)), 6, 0, 7); c.fill();
    if (performance.now() - txt > 150) { txt = performance.now();
      let meas = '—'; if (since > Math.min(10, 4 / f + 1)) { const per = hist.filter(p => p[0] > t - 1 / f); if (per.length > 3) { const xs = per.map(p => p[1]); meas = nf(20 * Math.log10((Math.max(...xs) - Math.min(...xs)) / (2 * A)), 2) + ' dB'; } }
      rd.innerHTML = `<span>teoria: |H| = ${nf(g, 2)} dB, ritardo di fase ${nf(-ph(2 * Math.PI * f), 0)}°</span><span>misurato sulla simulazione: ${meas}</span>`; }
  });
}

// ---------------------------------------------------------------- 4) l'integratore passo per passo
function euler(root) {
  root.append(el(`<div class="nl-row"><div class="nl-code"><pre><span data-l="1">acc = wn*wn*(target - pos) - 2*zeta*wn*vel</span><span data-l="2">vel += acc * dt</span><span data-l="3">pos += vel * dt</span></pre><div class="nl-calc"></div></div><div class="nl-cv nl-wide"></div></div>`));
  root.append(el(`<div class="nl-ctl"><div class="nl-btns"><button class="e-step">Un passo</button><button class="e-run">▶ Avvia</button><button class="e-reset">Ricomincia</button>
    <label class="nl-chk"><input type="checkbox" class="e-exp"> confronta con Euler esplicito</label><label class="nl-chk"><input type="checkbox" class="e-z0"> senza smorzamento (ζ = 0)</label></div>
    <div class="nl-sl"><label>passo Δt <input type="range" min="2" max="200" step="1" value="8"><b></b></label><button class="nl-reset">8 ms</button></div><div class="nl-read"></div></div>`));
  const C = canvasIn(root.querySelector('.nl-cv')), calc = root.querySelector('.nl-calc'), rd = root.querySelector('.nl-read'), sl = root.querySelector('input[type=range]'), out = root.querySelector('.nl-sl b');
  const exp = root.querySelector('.e-exp'), z0 = root.querySelector('.e-z0'), runB = root.querySelector('.e-run'), wn = 13;
  let dt, z, S, E, k, run = false, acc = 0, hl = 0, hlT = 0, last = '';
  const reset = () => { dt = +sl.value / 1000; z = z0.checked ? 0 : 0.55; out.textContent = sl.value + ' ms'; S = { x: 0, v: 0, pts: [[0, 0]] }; E = { x: 0, v: 0, pts: [[0, 0]] }; k = 0; last = ''; info(); calc.innerHTML = '<p>Premi <b>Un passo</b>: il programma parte con l\'ago fermo a 0 e l\'obiettivo a 1.</p>'; };
  const Tmax = () => z === 0 ? 3 : 1.4;
  const info = () => { rd.innerHTML = `<span>ωn·Δt = ${nf(wn * dt, 3)} (limite di stabilità ≈ 2, cioè Δt ≈ 154 ms)</span><span>passi: ${k}</span>`; };
  const step = () => {
    if (k * dt > Tmax()) return false;
    const a = wn * wn * (1 - S.x) - 2 * z * wn * S.v, v1 = S.v + a * dt, x1 = S.x + v1 * dt;
    last = `<div class="t">passo ${k + 1} · t = ${nf((k + 1) * dt, 3)} s</div>
      <div data-l="1">acc = ${nf(wn * wn, 0)}·(1 − ${np(S.x, 4)}) − ${nf(2 * z * wn, 2)}·${np(S.v, 4)} = <b>${nf(a, 2)}</b></div>
      <div data-l="2">vel = ${nf(S.v, 4)} + ${np(a, 2)}·${nf(dt, 3)} = <b>${nf(v1, 4)}</b></div>
      <div data-l="3">pos = ${nf(S.x, 4)} + <u>${np(v1, 4)}</u>·${nf(dt, 3)} = <b>${nf(x1, 4)}</b></div>`;
    S.x = x1; S.v = v1; S.pts.push([(k + 1) * dt, x1]);
    const ae = wn * wn * (1 - E.x) - 2 * z * wn * E.v, xe = E.x + E.v * dt; if (exp.checked) last += `<div class="ex">esplicito: pos = ${nf(E.x, 4)} + <u>${np(E.v, 4)}</u>·${nf(dt, 3)} = ${nf(xe, 4)} (usa la velocità vecchia)</div>`;
    E.v += ae * dt; E.x = xe; E.pts.push([(k + 1) * dt, xe]);
    k++; calc.innerHTML = last; hl = 1; hlT = 0; info(); return true;
  };
  sl.addEventListener('input', reset); z0.addEventListener('change', reset); exp.addEventListener('change', () => { if (k === 0) reset(); });
  root.querySelector('.nl-reset').addEventListener('click', () => { sl.value = 8; reset(); });
  root.querySelector('.e-step').addEventListener('click', () => { run = false; runB.textContent = '▶ Avvia'; step(); });
  runB.addEventListener('click', () => { if (k * dt > Tmax()) reset(); run = !run; runB.textContent = run ? '⏸ Pausa' : '▶ Avvia'; });
  root.querySelector('.e-reset').addEventListener('click', () => { run = false; runB.textContent = '▶ Avvia'; reset(); });
  reset();
  loop(root, d => {
    const T = theme();
    if (run) { acc += d; const per = Math.max(0.03, Math.min(0.25, 60 * dt / 8)); while (acc > per) { acc -= per; if (!step()) { run = false; runB.textContent = '▶ Avvia'; break; } } }
    hlT += d; const lines = root.querySelectorAll('.nl-code pre span'); const cur = hl ? Math.min(3, 1 + Math.floor(hlT / 0.12)) : 0;
    lines.forEach(s => s.classList.toggle('on', +s.dataset.l === cur)); if (hlT > 0.5) hl = 0;
    const c = C.ctx; c.clearRect(0, 0, C.w, C.h); const tm = Tmax(), y1 = z === 0 ? 2.6 : 1.4, y0 = z === 0 ? -0.8 : -0.1;
    const F = frame(C, T, { x0: 0, x1: tm, y0, y1, yt: z === 0 ? [-0.5, 0, 1, 2] : [0, 0.5, 1], yl: v => nf(v, 1), xt: z === 0 ? [0, 1, 2, 3] : [0, 0.4, 0.8, 1.2], xl: v => nf(v, 1), xlab: 'tempo (s)' });
    c.save(); c.beginPath(); c.rect(F.P.l, 0, C.w - F.P.l - F.P.r, C.h - F.P.b); c.clip();
    c.strokeStyle = T.ink; c.lineWidth = 1.6; c.beginPath(); for (let i = 0; i <= 300; i++) { const x = tm * i / 300, y = z === 0 ? 1 - Math.cos(wn * x) : stepResp(z, wn, x); i ? c.lineTo(F.X(x), F.Y(y)) : c.moveTo(F.X(x), F.Y(y)); } c.stroke();
    if (exp.checked) { c.fillStyle = T.b; for (const [x, y] of E.pts) { c.beginPath(); c.arc(F.X(x), F.Y(clamp(y, y0 - 1, y1 + 1)), 2.6, 0, 7); c.fill(); } }
    c.fillStyle = T.o; for (const [x, y] of S.pts) { c.beginPath(); c.arc(F.X(x), F.Y(clamp(y, y0 - 1, y1 + 1)), 3, 0, 7); c.fill(); }
    c.restore();
    c.font = '11px system-ui'; c.textAlign = 'left'; let ly = 18; const lg = (col, s) => { c.fillStyle = col; c.fillRect(F.P.l + 10, ly - 7, 10, 3); c.fillText(s, F.P.l + 26, ly - 3); ly += 15; };
    lg(T.ink, 'soluzione esatta'); lg(T.o, 'semi-implicito (il programma)'); if (exp.checked) lg(T.b, 'Euler esplicito');
  });
}

const W = { lab, bounce: lab, poles, freq, euler };
const init = () => document.querySelectorAll('.nl[data-w]').forEach(r => { try { W[r.dataset.w](r); } catch (e) { console.warn(e); } });
document.readyState === 'loading' ? document.addEventListener('DOMContentLoaded', init) : init();
})();
