// Ham Radio Pills · animazioni della pagina eload-60v.
// "eloop": risposte dell'anello di corrente calcolate con il modello del progetto (analysis/ di metallarox/eload-60v).
// "etherm": bilancio termico e SOA con i numeri delle slide del progetto.
(() => {
const nf = (x, d = 1) => Number.isFinite(x) ? x.toFixed(d).replace('.', ',').replace(/^-/, '−') : '—';
const clamp = (v, a, b) => Math.max(a, Math.min(b, v));
const el = h => { const d = document.createElement('div'); d.innerHTML = h.trim(); return d.firstElementChild; };
const theme = () => { const dk = document.documentElement.getAttribute('data-theme') === 'dark';
  return dk ? { dk, ink: '#e6eef7', mute: '#93a3b8', grid: 'rgba(255,255,255,.09)', axis: '#5a6a80', o: '#ff7a5c', b: '#4cc3f5', g: '#4fc27a', r: '#ff5c5c', faint: 'rgba(230,238,247,.28)' }
            : { dk, ink: '#0a1a2e', mute: '#64748b', grid: 'rgba(10,26,46,.08)', axis: '#9aa5b4', o: '#e0563b', b: '#1593d1', g: '#2a9d5c', r: '#d62f2f', faint: 'rgba(10,26,46,.25)' }; };
function canvasIn(host) { const cv = document.createElement('canvas'); host.appendChild(cv); const o = { cv, ctx: cv.getContext('2d'), w: 1, h: 1 };
  const rs = () => { const r = host.getBoundingClientRect(), d = Math.min(devicePixelRatio || 1, 2); o.w = Math.max(1, r.width); o.h = Math.max(1, r.height); cv.width = Math.round(o.w * d); cv.height = Math.round(o.h * d); o.ctx.setTransform(d, 0, 0, d, 0, 0); o.dirty = true; };
  new ResizeObserver(rs).observe(host); rs(); return o; }
function loop(root, step) { let vis = false, last = 0, raf = 0;
  const tick = now => { const dt = Math.min(0.05, (now - last) / 1000); last = now; step(dt); raf = vis ? requestAnimationFrame(tick) : 0; };
  new IntersectionObserver(es => { vis = es[0].isIntersecting; if (vis && !raf) { last = performance.now(); raf = requestAnimationFrame(tick); } }).observe(root); }
function frame(o, T, { x0, x1, y0, y1, yt = [], yl = v => v, xt = [], xl = v => v, xlab = '', ylab = '', logx = false, pb = 0 }) {
  const c = o.ctx, w = o.w, h = o.h, P = { l: 52, r: 14, t: 12, b: pb || (xlab ? 38 : 24) };
  const fx = logx ? v => Math.log10(v) : v => v;
  const X = v => P.l + (fx(v) - fx(x0)) / (fx(x1) - fx(x0)) * (w - P.l - P.r), Y = v => h - P.b - (v - y0) / (y1 - y0) * (h - P.t - P.b);
  c.font = '11px system-ui, sans-serif'; c.lineWidth = 1;
  for (const v of yt) { c.strokeStyle = T.grid; c.beginPath(); c.moveTo(P.l, Y(v)); c.lineTo(w - P.r, Y(v)); c.stroke(); c.fillStyle = T.mute; c.textAlign = 'right'; c.fillText(yl(v), P.l - 6, Y(v) + 4); }
  for (const v of xt) { c.strokeStyle = T.grid; c.beginPath(); c.moveTo(X(v), P.t); c.lineTo(X(v), h - P.b); c.stroke(); c.fillStyle = T.mute; c.textAlign = 'center'; c.fillText(xl(v), X(v), h - P.b + 14); }
  c.strokeStyle = T.axis; c.beginPath(); c.moveTo(P.l, P.t); c.lineTo(P.l, h - P.b); c.lineTo(w - P.r, h - P.b); c.stroke();
  if (xlab) { c.fillStyle = T.mute; c.textAlign = 'center'; c.fillText(xlab, (P.l + w - P.r) / 2, h - 6); }
  if (ylab) { c.save(); c.translate(12, (P.t + h - P.b) / 2); c.rotate(-Math.PI / 2); c.fillStyle = T.mute; c.textAlign = 'center'; c.fillText(ylab, 0, 0); c.restore(); }
  return { X, Y, P };
}
const niceTicks = (a, b, n = 5) => { const span = b - a, st = Math.pow(10, Math.floor(Math.log10(span / n))), m = [1, 2, 5, 10].find(k => span / (st * k) <= n) * st; const out = []; for (let v = Math.ceil(a / m) * m; v <= b + 1e-9; v += m) out.push(+v.toFixed(6)); return out; };
function seg(root, name, opts, val, on) {
  const g = el(`<div class="nl-seg"><span>${name}</span>${opts.map(([v, l]) => `<button data-v="${v}">${l}</button>`).join('')}</div>`);
  const set = v => { g.querySelectorAll('button').forEach(b => b.classList.toggle('on', b.dataset.v === String(v))); };
  g.querySelectorAll('button').forEach(b => b.addEventListener('click', () => { set(b.dataset.v); on(b.dataset.v); })); set(val); return g;
}

// ---------------------------------------------------------------- anello di corrente
async function eloop(root) {
  const D = await (await fetch(root.dataset.src)).json();
  let rev = '0.2', cas = 'step', I = '1.25', prog = 0;
  const CASES = { step: 'Passo 1,0 → 1,2 A', keep: 'Accensione con keep-alive 10 mA', on: 'Accensione da 0 A', small: 'Piccolo segnale (modello lineare)' };
  const ctl = el('<div class="nl-ctl"></div>');
  root.append(el('<div class="nl-row"><div class="nl-cv nl-wide eo-t"></div><div class="nl-cv nl-wide eo-b"></div></div>'), ctl);
  const rd = el('<div class="nl-read"></div>');
  const redo = () => { prog = 0; };
  ctl.append(seg(root, 'revisione', [['0.1', 'rev 0.1 · C6 10 nF'], ['0.2', 'rev 0.2 · C6 1 nF']], rev, v => { rev = v; redo(); }),
    seg(root, 'prova', Object.entries(CASES), cas, v => { cas = v; redo(); }),
    seg(root, 'corrente (Bode e piccolo segnale)', Object.keys(D.rev['0.2'].bode).map(k => [k, String(+k).replace('.', ',') + ' A']), I, v => { I = v; redo(); }), rd);
  const A = canvasIn(root.querySelector('.eo-t')), B = canvasIn(root.querySelector('.eo-b'));
  const trace = (r) => { if (cas === 'small') { const s = D.rev[r].small[I]; return { t: s.t, y: s.y, i0: 0, i1: 1, norm: true }; } return D.rev[r].large[cas]; };
  const metrics = tr => { const { t, y, i0, i1 } = tr, a = i0 + 0.1 * (i1 - i0), b = i0 + 0.9 * (i1 - i0);
    const t10 = t[y.findIndex(v => v >= a)], t90 = t[y.findIndex(v => v >= b)], os = (Math.max(...y) - i1) / (i1 - i0) * 100; return { t10, t90, os }; };
  let txt = 0;
  loop(root, dt => {
    const T = theme(); prog = Math.min(1, prog + dt / 1.6);
    const tr = trace(rev), other = trace(rev === '0.1' ? '0.2' : '0.1');
    const tmax = tr.t[tr.t.length - 1], tmin = Math.min(0, tr.t[0]);
    const unit = tmax > 1500 ? 'ms' : 'µs', k = unit === 'ms' ? 1e-3 : 1;
    let c = A.ctx; c.clearRect(0, 0, A.w, A.h);
    const ytop = tr.norm ? 1.2 : Math.max(tr.i1 * 1.15, 1.3), ybot = tr.norm ? -0.05 : (cas === 'step' ? 0.9 : -0.05);
    const F = frame(A, T, { x0: tmin * k, x1: tmax * k, y0: ybot, y1: ytop, yt: niceTicks(ybot, ytop, 5), yl: v => nf(v, tr.norm ? 1 : 2) + (tr.norm ? '' : ' A'), xt: niceTicks(tmin * k, tmax * k, 6), xl: v => nf(v, v % 1 ? 1 : 0), xlab: `tempo dal comando (${unit})`, ylab: tr.norm ? 'corrente / passo' : 'corrente nel canale' });
    c.save(); c.beginPath(); c.rect(F.P.l, 0, A.w - F.P.l - F.P.r, A.h - F.P.b); c.clip();
    // riferimento: il comando
    c.strokeStyle = T.g; c.setLineDash([5, 4]); c.lineWidth = 1.5; c.beginPath(); c.moveTo(F.X(tmin * k), F.Y(tr.i0)); c.lineTo(F.X(0), F.Y(tr.i0)); c.lineTo(F.X(0), F.Y(tr.i1)); c.lineTo(F.X(tmax * k), F.Y(tr.i1)); c.stroke(); c.setLineDash([]);
    c.strokeStyle = T.faint; c.lineWidth = 1.6; c.beginPath(); other.t.forEach((t, i) => { const x = F.X(t * k), y = F.Y(other.y[i]); i ? c.lineTo(x, y) : c.moveTo(x, y); }); c.stroke();
    const n = Math.max(2, Math.round(tr.t.length * prog));
    c.strokeStyle = T.o; c.lineWidth = 2.8; c.beginPath(); for (let i = 0; i < n; i++) { const x = F.X(tr.t[i] * k), y = F.Y(tr.y[i]); i ? c.lineTo(x, y) : c.moveTo(x, y); } c.stroke();
    c.fillStyle = T.o; c.beginPath(); c.arc(F.X(tr.t[n - 1] * k), F.Y(tr.y[n - 1]), 5, 0, 7); c.fill();
    const m = metrics(tr); if (prog > 0.98 && Number.isFinite(m.t10) && Number.isFinite(m.t90)) {
      c.strokeStyle = T.ink; c.lineWidth = 1; c.setLineDash([2, 3]);
      for (const tt of [m.t10, m.t90]) { c.beginPath(); c.moveTo(F.X(tt * k), F.P.t); c.lineTo(F.X(tt * k), A.h - F.P.b); c.stroke(); }
      c.setLineDash([]); c.fillStyle = T.ink; c.font = '11px system-ui'; c.textAlign = 'left'; c.fillText('10 %', F.X(m.t10 * k) + 3, F.P.t + 11); c.fillText('90 %', F.X(m.t90 * k) + 3, F.P.t + 24); }
    c.restore();
    c.font = '11px system-ui'; c.textAlign = 'right'; const lx = A.w - F.P.r - 8, ly = A.h - F.P.b - 10; c.fillStyle = T.g; c.fillText('- - comando', lx, ly - 28); c.fillStyle = T.o; c.fillText('rev ' + rev.replace('.', ','), lx, ly - 14); c.fillStyle = T.mute; c.fillText('rev ' + (rev === '0.1' ? '0,2' : '0,1') + ' (confronto)', lx, ly);
    // Bode
    const bd = D.rev[rev].bode[I]; c = B.ctx; c.clearRect(0, 0, B.w, B.h);
    const G = frame(B, T, { x0: 10, x1: 1e7, y0: -60, y1: 140, yt: [-60, -20, 0, 20, 60, 100, 140], yl: v => v + ' dB', xt: [10, 100, 1e3, 1e4, 1e5, 1e6, 1e7], xl: v => v >= 1e6 ? v / 1e6 + ' M' : v >= 1e3 ? v / 1e3 + ' k' : String(v), logx: true, xlab: 'frequenza (Hz)' });
    c.strokeStyle = T.ink; c.lineWidth = 2; c.beginPath(); bd.f.forEach((f, i) => { const x = G.X(f), y = G.Y(clamp(bd.dB[i], -70, 150)); i ? c.lineTo(x, y) : c.moveTo(x, y); }); c.stroke();
    c.strokeStyle = T.b; c.lineWidth = 2; c.beginPath(); bd.f.forEach((f, i) => { const x = G.X(f), y = G.Y(clamp(bd.cl[i], -70, 150)); i ? c.lineTo(x, y) : c.moveTo(x, y); }); c.stroke();
    c.strokeStyle = T.axis; c.setLineDash([3, 3]); c.beginPath(); c.moveTo(G.X(10), G.Y(0)); c.lineTo(G.X(1e7), G.Y(0)); c.stroke(); c.setLineDash([]);
    const fc = bd.fc * 1e3; c.fillStyle = T.o; c.beginPath(); c.arc(G.X(fc), G.Y(0), 6, 0, 7); c.fill();
    const f3 = bd.f3 * 1e3; c.fillStyle = T.b; c.beginPath(); c.arc(G.X(f3), G.Y(-3), 5, 0, 7); c.fill();
    c.font = '11px system-ui'; c.textAlign = 'left'; c.fillStyle = T.ink; c.fillText('guadagno d\'anello |L|', G.X(15), G.Y(125)); c.fillStyle = T.b; c.fillText('anello chiuso I / I_set', G.X(15), G.Y(108));
    c.fillStyle = T.o; c.textAlign = 'right'; c.fillText(`|L| = 1 a ${nf(bd.fc / 1e3, 2)} MHz · margine di fase ${nf(bd.pm, 1)}°`, B.w - 16, G.Y(40)); c.fillStyle = T.b; c.textAlign = 'left'; c.fillText(`−3 dB: ${nf(bd.f3, 1)} kHz`, G.X(f3) - 20, G.Y(-3) + 18);
    if (performance.now() - txt > 200) { txt = performance.now(); const mm = metrics(tr);
      const td = cas === 'on' ? `<span>ritardo di accensione ≈ V<sub>G</sub>·R14·C6 / (I·R<sub>s</sub>) = 3,8 V·1 kΩ·${rev === '0.1' ? '10' : '1'} nF / 20 mV ≈ <b>${rev === '0.1' ? '1,9 ms' : '190 µs'}</b></span>` : '';
      rd.innerHTML = `<span>10–90 %: <b>${nf(mm.t90 - mm.t10, 1)} µs</b></span><span>al 90 % dopo <b>${nf(mm.t90, 0)} µs</b> dal comando</span><span>sovraelongazione ${nf(Math.max(0, mm.os), 1)} %</span><span>banda ad anello chiuso a ${I.replace('.', ',')} A: <b>${nf(bd.f3, 2)} kHz</b></span>${td}`; }
  });
}

// ---------------------------------------------------------------- calore e SOA
function etherm(root) {
  const S = { V: 60, I: 5, n: 4, Ta: 35, Rsa: 0.12 };
  const RJC = 0.31, RCS = 0.21, RPAD = 0.03, OTP = 100, TJMAX = 150;
  root.append(el('<div class="nl-row"><div class="nl-cv nl-wide et-soa"></div><div class="nl-cv nl-wide et-temp"></div></div>'));
  const ctl = el(`<div class="nl-ctl"><div class="nl-sl">
    <label>tensione <input type="range" min="1" max="60" step="0.5" data-k="V"><b data-o="V"></b></label>
    <label>corrente totale <input type="range" min="0" max="20" step="0.05" data-k="I"><b data-o="I"></b></label>
    <label>canali <input type="range" min="1" max="4" step="1" data-k="n"><b data-o="n"></b></label></div><div class="nl-sl">
    <label>ambiente <input type="range" min="15" max="45" step="1" data-k="Ta"><b data-o="Ta"></b></label>
    <label>dissipatore R<sub>sa</sub> <input type="range" min="0.06" max="0.4" step="0.01" data-k="Rsa"><b data-o="Rsa"></b></label>
    <button class="nl-reset">caso delle slide: 60 V, 5 A</button></div><div class="nl-read"></div></div>`);
  root.append(ctl);
  const U = { V: v => nf(v, 1) + ' V', I: v => nf(v, 2) + ' A', n: v => String(v), Ta: v => nf(v, 0) + ' °C', Rsa: v => nf(v, 2) + ' K/W' };
  const inputs = ctl.querySelectorAll('input'), rd = ctl.querySelector('.nl-read');
  const sync = () => { inputs.forEach(i => { S[i.dataset.k] = +i.value; ctl.querySelector(`[data-o="${i.dataset.k}"]`).textContent = U[i.dataset.k](+i.value); }); };
  const put = () => inputs.forEach(i => { i.value = S[i.dataset.k]; });
  inputs.forEach(i => i.addEventListener('input', sync)); ctl.querySelector('.nl-reset').addEventListener('click', () => { Object.assign(S, { V: 60, I: 5, n: 4, Ta: 35, Rsa: 0.12 }); put(); sync(); });
  put(); sync();
  const A = canvasIn(root.querySelector('.et-soa')), B = canvasIn(root.querySelector('.et-temp'));
  const shown = { base: 35, spr: 35, case: 35, j: 35 }; let txt = 0;
  loop(root, dt => {
    const T = theme();
    const req = S.I / S.n, lim = Math.min(5, 75 / S.V), Ich = Math.min(req, lim), Pf = S.V * Ich, Pt = Pf * S.n;
    const Tb = S.Ta + S.Rsa * Pt, Ts = Tb + RPAD * Pt, Tc = Ts + RCS * Pf, Tj = Tc + RJC * Pf;
    const target = { base: Tb, spr: Ts, case: Tc, j: Tj }; for (const k in shown) shown[k] += (target[k] - shown[k]) * Math.min(1, dt * 6);
    // SOA per MOSFET
    let c = A.ctx; c.clearRect(0, 0, A.w, A.h);
    const F = frame(A, T, { x0: 0, x1: 80, y0: 0, y1: 6, yt: [0, 1, 2, 3, 4, 5, 6], yl: v => v + ' A', xt: [0, 10, 20, 30, 40, 50, 60, 70, 80], xlab: 'tensione sul MOSFET (V)', ylab: 'corrente per canale' });
    const curve = (Pw, col, dash, lw) => { c.strokeStyle = col; c.lineWidth = lw; c.setLineDash(dash); c.beginPath(); let first = true; for (let v = 1; v <= 80; v += 0.5) { const i = Pw / v; if (i > 6.2) continue; const x = F.X(v), y = F.Y(i); first ? c.moveTo(x, y) : c.lineTo(x, y); first = false; } c.stroke(); c.setLineDash([]); };
    const Psoa = 240 * (150 - Tc) / (150 - 75);
    c.fillStyle = T.dk ? 'rgba(79,194,122,.10)' : 'rgba(42,157,92,.10)'; c.beginPath(); c.moveTo(F.X(0), F.Y(0)); c.lineTo(F.X(0), F.Y(5)); for (let v = 15; v <= 60; v += 0.5) c.lineTo(F.X(v), F.Y(Math.min(5, 75 / v))); c.lineTo(F.X(60), F.Y(0)); c.closePath(); c.fill();
    curve(Math.max(0, Psoa), T.r, [6, 4], 2); curve(75, T.g, [], 2.4);
    c.strokeStyle = T.g; c.lineWidth = 2.4; c.beginPath(); c.moveTo(F.X(0), F.Y(5)); c.lineTo(F.X(15), F.Y(5)); c.stroke();
    c.strokeStyle = T.axis; c.setLineDash([3, 3]); c.beginPath(); c.moveTo(F.X(60), F.P.t); c.lineTo(F.X(60), A.h - F.P.b); c.stroke(); c.setLineDash([]);
    c.font = '11px system-ui'; c.textAlign = 'left'; c.fillStyle = T.g; c.fillText('limite del firmware: 5 A e 75 W', F.X(17), F.Y(5.55));
    c.fillStyle = T.r; c.fillText(`FBSOA garantita, ridotta a T_case ${nf(Tc, 0)} °C: ${nf(Psoa, 0)} W`, F.X(22), F.Y(Math.min(5.9, Psoa / 22) ) - 6);
    c.fillStyle = T.mute; c.fillText('OVP 64,7 V', F.X(61), F.P.t + 12);
    if (req > Ich + 1e-6) { c.strokeStyle = T.mute; c.setLineDash([2, 3]); c.beginPath(); c.moveTo(F.X(S.V), F.Y(Math.min(req, 6))); c.lineTo(F.X(S.V), F.Y(Ich)); c.stroke(); c.setLineDash([]); c.fillStyle = T.mute; c.beginPath(); c.arc(F.X(S.V), F.Y(Math.min(req, 6)), 4, 0, 7); c.fill(); }
    c.fillStyle = T.o; c.beginPath(); c.arc(F.X(S.V), F.Y(Ich), 7, 0, 7); c.fill();
    // catena termica
    c = B.ctx; c.clearRect(0, 0, B.w, B.h);
    const nodes = [['ambiente', S.Ta], ['base del dissipatore', shown.base], ['spreader di rame (NTC)', shown.spr], ['case del MOSFET', shown.case], ['giunzione', shown.j]];
    const G = frame(B, T, { x0: 0, x1: 1, y0: 0, y1: 180, yt: [0, 30, 60, 90, 120, 150, 180], yl: v => v + ' °C', ylab: 'temperatura', pb: 44 });
    const bw = (B.w - G.P.l - G.P.r) / nodes.length;
    nodes.forEach(([lab, t], i) => { const x = G.P.l + bw * i + bw * 0.18, w = bw * 0.64, hot = clamp((t - 25) / 125, 0, 1);
      c.fillStyle = `hsl(${(1 - hot) * 210}, 75%, ${T.dk ? 55 : 50}%)`; c.fillRect(x, G.Y(t), w, G.Y(0) - G.Y(t));
      c.fillStyle = T.ink; c.textAlign = 'center'; c.font = 'bold 12px system-ui'; c.fillText(nf(t, 0) + ' °C', x + w / 2, G.Y(t) - 6);
      c.font = '10px system-ui'; c.fillStyle = T.mute; const words = lab.split(' '); words.reduce((acc, wd) => { const ln = acc[acc.length - 1]; (ln + ' ' + wd).length > 12 ? acc.push(wd) : acc[acc.length - 1] = (ln ? ln + ' ' : '') + wd; return acc; }, ['']).forEach((ln, j) => c.fillText(ln, x + w / 2, G.Y(0) + 13 + j * 12)); });
    c.strokeStyle = T.r; c.setLineDash([6, 4]); c.lineWidth = 1.5; c.beginPath(); c.moveTo(G.P.l, G.Y(TJMAX)); c.lineTo(B.w - G.P.r, G.Y(TJMAX)); c.stroke();
    c.strokeStyle = T.o; c.beginPath(); c.moveTo(G.P.l, G.Y(OTP)); c.lineTo(B.w - G.P.r, G.Y(OTP)); c.stroke(); c.setLineDash([]);
    c.font = '11px system-ui'; c.textAlign = 'left'; c.fillStyle = T.r; c.fillText('T_j massima 150 °C', G.P.l + 6, G.Y(TJMAX) - 5); c.fillStyle = T.o; c.fillText('OTP sullo spreader ≈ 100 °C', G.P.l + 6, G.Y(OTP) - 5);
    if (performance.now() - txt > 150) { txt = performance.now();
      const st = Ts >= OTP ? '<b class="bad">l\'OTP interviene: lo spreader supera 100 °C</b>' : Tj >= TJMAX ? '<b class="bad">giunzione oltre 150 °C</b>' : '<b class="ok">dentro i limiti</b>';
      rd.innerHTML = `<span>per canale: ${nf(Ich, 2)} A × ${nf(S.V, 1)} V = <b>${nf(Pf, 1)} W</b>${req > Ich + 1e-6 ? ` (chiesti ${nf(req, 2)} A: limitati dal firmware)` : ''}</span><span>totale ${nf(Pt, 0)} W</span>
        <span>T<sub>j</sub> = ${nf(S.Ta, 0)} + ${nf(S.Rsa, 2)}·${nf(Pt, 0)} + 0,03·${nf(Pt, 0)} + (0,21 + 0,31)·${nf(Pf, 1)} = <b>${nf(Tj, 0)} °C</b></span>
        <span>margine SOA ${nf(Psoa / Math.max(Pf, 0.01), 1)}×</span><span>${st}</span>`; }
  });
}
const W = { eloop, etherm };
const init = () => document.querySelectorAll('.nl[data-w]').forEach(r => { if (W[r.dataset.w]) Promise.resolve(W[r.dataset.w](r)).catch(e => console.warn(e)); });
document.readyState === 'loading' ? document.addEventListener('DOMContentLoaded', init) : init();
})();
