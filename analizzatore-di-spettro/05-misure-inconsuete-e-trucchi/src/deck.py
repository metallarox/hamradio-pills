"""Helper condiviso per le presentazioni Ham Radio Pills (stile IV3HGA)."""
import re, base64, os
import numpy as np
N="#0a1a2e"; C="#1593d1"; L="#e8f6fd"; G="#9aa5b4"
HERE=os.path.dirname(os.path.abspath(__file__))
LOGO='<img src="data:image/png;base64,'+base64.b64encode(open(os.path.join(HERE,"logo.png"),"rb").read()).decode()+'">'
CSS=open(os.path.join(HERE,"style.css")).read()+"""
td.l{font-family:inherit!important;text-align:left!important}.diag svg{width:100%;height:auto}
table.sum td{font-size:21px!important;padding:12px 14px!important}
.flow{display:grid;grid-template-columns:repeat(5,1fr);gap:14px}.flow .card b{display:block;font-size:34px;color:#22b8f0;line-height:1}.flow .card h3{margin-top:8px}
.warn{background:#fff4e5;border-left:5px solid #e0873b;border-radius:8px;padding:12px 16px;font-size:17px;margin:10px 0}"""
def svg(p):
    s=open(p).read(); s=re.sub(r'<\?xml.*?\?>','',s,flags=re.S); s=re.sub(r'<!DOCTYPE.*?>','',s,flags=re.S)
    return re.sub(r'(<svg[^>]*?)\swidth="[^"]*"\s+height="[^"]*"',r'\1 width="100%"',s,count=1)
def eq(x): return f'<div class="eq">{x}</div>'
def it(x,d=2): return f"{x:.{d}f}".replace(".",",")
ARW=f'<defs><marker id="ar" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0L10 5L0 10z" fill="{N}"/></marker><marker id="ac" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0L10 5L0 10z" fill="{C}"/></marker></defs>'
def box(x,y,w,h,t,fill=L,fs=15):
    lines=t.split("|"); ty=y+h/2-(len(lines)-1)*9+5
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="8" fill="{fill}" stroke="{N}" stroke-width="2"/>'+"".join(f'<text x="{x+w/2}" y="{ty+i*18}" text-anchor="middle" font-size="{fs}" fill="{N}">{l}</text>' for i,l in enumerate(lines))
def ln(x1,y1,x2,y2,c=N,dash=False):
    d='stroke-dasharray="5 4"' if dash else ""
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{c}" stroke-width="2" {d} marker-end="url(#{"ac" if c==C else "ar"})"/>'
class Deck:
    def __init__(s,title,subtitle,footer): s.S=[]; s.title=title; s.sub=subtitle; s.footer=footer
    def add(s,t,b): s.S.append((t,b))
    def render(s,path="slides.html"):
        out=[f"<!DOCTYPE html><html><head><meta charset='utf-8'><style>{CSS}</style></head><body>",
             f'<section class="slide c"><div class="cover"><div class="clogo">{LOGO}</div><div><h1>{s.title}</h1><p class="sub">{s.sub}</p><p class="by">Elia · IV3HGA</p></div></div></section>']
        n=len(s.S)+1
        for i,(t,b) in enumerate(s.S):
            out.append(f'<section class="slide"><div class="hdrlogo">{LOGO}</div><h2>{t}</h2>{b}<div class="foot"><span>{s.footer} · IV3HGA</span><span>{i+2}/{n}</span></div></section>')
        out.append("</body></html>"); open(path,"w").write("".join(out))
# --- simulazione di una traccia dell'analizzatore di spettro ---
def sa_trace(f,tones,rbw,danl_1hz=-150.0,seed=1,log_avg=True,vbw_ratio=1.0):
    """f in Hz; tones=[(freq,dBm)]; ritorna dBm visualizzati con filtro RBW gaussiano."""
    rng=np.random.default_rng(seed)
    p=np.zeros_like(f)
    sig=rbw/2.3548  # gaussiana: RBW = FWHM (-3 dB)
    for ft,pdbm in tones:
        p+=10**(pdbm/10)*np.exp(-0.5*((f-ft)/sig)**2)
    noise=10**((danl_1hz+10*np.log10(rbw))/10)
    jit=rng.exponential(1.0,f.shape)  # potenza di rumore (Rayleigh -> esponenziale)
    k=max(1,int(round(1/vbw_ratio)))
    if k>1: jit=np.convolve(jit,np.ones(k)/k,mode="same")
    tot=p+noise*jit
    return 10*np.log10(tot)
def mpl_setup():
    import matplotlib; matplotlib.use("svg"); import matplotlib.pyplot as plt
    plt.rcParams.update({"font.family":"DejaVu Sans","font.size":12,"axes.spines.top":False,"axes.spines.right":False})
    return plt
def pdf(out_pdf,html="slides.html"):
    from playwright.sync_api import sync_playwright
    with sync_playwright() as p:
        b=p.chromium.launch(); pg=b.new_page(viewport={"width":1280,"height":720})
        pg.goto("file://"+os.path.abspath(html)); pg.wait_for_timeout(300)
        pg.pdf(path=out_pdf,width="1280px",height="720px",print_background=True); b.close()
