# Da eseguire nella cartella analysis/ del progetto metallarox/eload-60v, dopo "python loopz.py":
#   python eload_loop_export.py  ->  eload_loop.json (copiato in progetti/eload-60v/loop.json)
# Esporta i risultati del modello del progetto (cl.py, num.py, tsim.py) per le animazioni della pagina web.
import json, numpy as np, scipy.signal as sg, io, contextlib
with contextlib.redirect_stdout(io.StringIO()):
    from num import resp, pm, f
    import cl, tsim
REV = {"0.1": dict(C6=10e-9, C5=100e-9), "0.2": dict(C6=1e-9, C5=10e-9)}
CUR = [0.1, 0.5, 1.25, 2.5, 5.0]
out = {"I": CUR, "rev": {}}
fs = np.logspace(1, 7, 220)
for r, p in REV.items():
    R = out["rev"][r] = {"small": {}, "bode": {}, "large": {}}
    for I in CUR:
        L, _, _ = resp(I, C6=p["C6"]); fc, ph, g = pm(L)
        Li = np.interp(np.log10(fs), np.log10(f), np.abs(L)); Lp = np.interp(np.log10(fs), np.log10(f), np.unwrap(np.angle(L)) * 180 / np.pi)
        H = cl.closed(I, C5=p["C5"], C6=p["C6"])
        _, hh = sg.freqresp(H, w=2 * np.pi * fs); mag = np.abs(hh) / np.abs(hh[0])
        f3 = float(fs[np.where(mag < 0.7071)[0][0]])
        T = 2.5e-3 if r == "0.1" else 0.25e-3
        t = np.linspace(0, T, 6001); t, y = sg.step(H, T=t); y = y / y[-1] if abs(y[-1]) > 0 else y
        tr = t[np.where(y > 0.9)[0][0]] - t[np.where(y > 0.1)[0][0]]
        k = np.linspace(0, len(t) - 1, 300).astype(int)
        R["small"][str(I)] = dict(t=[round(x * 1e6, 2) for x in t[k]], y=[round(float(v), 4) for v in y[k]], tr=round(tr * 1e6, 1))
        R["bode"][str(I)] = dict(f=[round(float(x), 2) for x in fs], dB=[round(20 * np.log10(v), 2) for v in Li], ph=[round(float(v), 1) for v in Lp],
                               cl=[round(20 * np.log10(v), 2) for v in mag], pm=round(ph, 1), fc=round(fc / 1e3, 1), f3=round(f3 / 1e3, 2))
    for lab, (I0, I1) in {"on": (0, 1.0), "keep": (0.01, 1.0), "step": (1.0, 1.2)}.items():
        T = (3.2e-3 if r == "0.1" else 0.45e-3) if lab != "step" else (1.2e-3 if r == "0.1" else 0.2e-3)
        o = tsim.sim(I0, I1, p["C6"], p["C5"], T=T, dt=5e-9, tstep=20e-6)
        k = np.linspace(0, len(o) - 1, 400).astype(int)
        R["large"][lab] = dict(t=[round((o[i, 0] - 20e-6) * 1e6, 2) for i in k], y=[round(float(o[i, 1]), 4) for i in k], i0=I0, i1=I1)
json.dump(out, open("eload_loop.json", "w"), separators=(",", ":"))
for r in REV: print(r, {I: (out["rev"][r]["bode"][str(I)]["pm"], out["rev"][r]["bode"][str(I)]["f3"], out["rev"][r]["small"][str(I)]["tr"]) for I in CUR})
