import re,json,base64
v=json.load(open("vals.txt"))
def svg(p): 
    s=open(p).read(); s=re.sub(r'<\?xml.*?\?>','',s,flags=re.S); s=re.sub(r'<!DOCTYPE.*?>','',s,flags=re.S)
    return re.sub(r'(<svg[^>]*?)\swidth="[^"]*"\s+height="[^"]*"',r'\1 width="100%"',s,count=1)
logo='<img src="data:image/png;base64,'+base64.b64encode(open("logo.png","rb").read()).decode()+'">'
bvd='''<svg viewBox="0 0 520 260" width="100%" font-family="DejaVu Sans" font-size="16" fill="none" stroke="#0a1a2e" stroke-width="2.5">
<line x1="20" y1="70" x2="80" y2="70"/><line x1="440" y1="70" x2="500" y2="70"/>
<circle cx="20" cy="70" r="5" fill="#0a1a2e"/><circle cx="500" cy="70" r="5" fill="#0a1a2e"/>
<path d="M80 70 l10 -12 l15 24 l15 -24 l15 24 l15 -24 l10 12"/>
<path d="M160 70 h10 c0 -22 20 -22 20 0 c0 -22 20 -22 20 0 c0 -22 20 -22 20 0 c0 -22 20 -22 20 0 h10"/>
<line x1="280" y1="70" x2="330" y2="70"/><line x1="330" y1="48" x2="330" y2="92"/><line x1="344" y1="48" x2="344" y2="92"/><line x1="344" y1="70" x2="440" y2="70"/>
<line x1="60" y1="70" x2="60" y2="190"/><line x1="460" y1="70" x2="460" y2="190"/>
<line x1="60" y1="190" x2="253" y2="190"/><line x1="253" y1="168" x2="253" y2="212"/><line x1="267" y1="168" x2="267" y2="212"/><line x1="267" y1="190" x2="460" y2="190"/>
<g stroke="none" fill="#1593d1" font-weight="700"><text x="98" y="112">Rm</text><text x="208" y="112">Lm</text><text x="326" y="118">Cm</text><text x="248" y="238">C0</text></g>
<g stroke="none" fill="#666" font-size="13"><text x="200" y="30">ramo mozionale (serie)</text><text x="300" y="182">capacità statica</text></g>
</svg>'''
fix='''<svg viewBox="0 0 560 230" width="100%" font-family="DejaVu Sans" font-size="15" stroke="#0a1a2e" stroke-width="2.5" fill="none">
<rect x="20" y="60" width="110" height="110" rx="10" fill="#e8f6fd"/><rect x="430" y="60" width="110" height="110" rx="10" fill="#e8f6fd"/>
<line x1="130" y1="115" x2="230" y2="115"/><line x1="330" y1="115" x2="430" y2="115"/>
<rect x="240" y="95" width="80" height="40" rx="4" fill="#fff"/><line x1="230" y1="115" x2="240" y2="115"/><line x1="320" y1="115" x2="330" y2="115"/>
<line x1="252" y1="100" x2="252" y2="130"/><line x1="308" y1="100" x2="308" y2="130"/>
<g stroke="none" fill="#0a1a2e"><text x="44" y="110" font-weight="700">Porta 1</text><text x="50" y="132">50 Ω</text>
<text x="454" y="110" font-weight="700">Porta 2</text><text x="460" y="132">50 Ω</text>
<text x="262" y="85" font-weight="700" fill="#1593d1">XTAL</text>
<text x="150" y="200" fill="#666" font-size="13">piano di calibrazione = pin del quarzo</text></g>
<line x1="230" y1="150" x2="230" y2="185" stroke="#1593d1" stroke-dasharray="4 4"/><line x1="330" y1="150" x2="330" y2="185" stroke="#1593d1" stroke-dasharray="4 4"/>
</svg>'''
def F(x,d=1): return f"{x:,.{d}f}".replace(","," ")
slides=[]
def S(title,body,num=True):
    slides.append((title,body))
S("", f'''<div class="cover"><div class="clogo">{logo}</div><div>
<h1>Misurare un quarzo<br>con il VNA</h1>
<p class="sub">Dalla misura di S21 al modello Butterworth–Van Dyke: fs, fp, Rm, Lm, Cm, C0 e Q</p>
<p class="by">Elia · IV3HGA</p></div></div>''')
S("Il modello equivalente (BVD)", f'''<div class="two"><div>{bvd}</div><div>
<ul><li><b>Ramo mozionale</b> Rm–Lm–Cm: rappresenta la risonanza meccanica del cristallo.</li>
<li><b>C0</b>: capacità statica fra gli elettrodi e il contenitore.</li>
<li>Sono due le risonanze da cercare:</li></ul>
<div class="eq">fs = 1 / (2π √(Lm·Cm))</div>
<div class="eq">fp ≈ fs · (1 + Cm / 2C0)</div>
<p class="note">Cm vale pochi fF e C0 qualche pF, quindi fp sta solo pochi kHz sopra fs.</p></div></div>''')
S("Setup di misura: quarzo in serie, S21", f'''<div class="two"><div>{fix}</div><div><ul>
<li>Il quarzo va <b>in serie</b> tra le due porte, con collegamenti cortissimi.</li>
<li><b>Calibra sul fixture</b> (almeno <i>through</i>, meglio 2 porte completa) in modo che il piano di riferimento cada ai pin del quarzo.</li>
<li><b>Potenza bassa</b>, tra −10 e −20 dBm: i quarzi sono sensibili al drive level.</li>
<li><b>Span stretto</b> (pochi kHz per fs, decine di kHz per vedere anche fp), molti punti e IF BW basso.</li>
<li>Con il NanoVNA conviene usare segmenti o scan software con migliaia di punti.</li></ul></div></div>''')
S("Cosa si vede: la risposta S21", f'''<div class="fig">{svg("wide.svg")}</div>
<p class="cap">Simulazione di un quarzo da 10 MHz (Rm = 10 Ω, Lm = 10 mH, C0 = 5 pF). <b>fs</b> è il picco di |S21|, dove la fase passa per 0°. <b>fp</b> è il notch profondo a circa {F((v["fp"]-v["fs"])/1e3)} kHz sopra.</p>''')
S("Estrazione dei parametri", f'''<div class="two"><div class="fig">{svg("zoom.svg")}</div><div>
<div class="eq"><b>Rm</b> = 2·Z0 · (1/|S21|<sub>pk</sub> − 1)</div>
<div class="eq"><b>Lm</b> = (Rm + 2·Z0) / (2π·Δf)</div>
<div class="eq"><b>Cm</b> = 1 / ((2π·fs)² · Lm)</div>
<div class="eq"><b>C0</b> ≈ Cm · fs / (2·(fp − fs))</div>
<div class="eq"><b>Q</b> = 2π·fs·Lm / Rm</div>
<p class="note">Δf è la distanza fra i punti di fase a <b>±45°</b>, dove la reattanza del ramo uguaglia la resistenza totale della maglia (Rm + 2·Z0). Sono più precisi dei punti a −3 dB.</p></div></div>''')
S("Esempio numerico (dati simulati)", f'''<div class="two"><div><table>
<tr><th>Lettura dal VNA</th><th></th></tr>
<tr><td>fs (picco |S21|)</td><td>{F(v["fs"])} Hz</td></tr>
<tr><td>|S21| al picco</td><td>{v["spk"]:.4f} ({v["spkdb"]:.2f} dB)</td></tr>
<tr><td>f₁ (+45°)</td><td>{F(v["fm"])} Hz</td></tr>
<tr><td>f₂ (−45°)</td><td>{F(v["fpl"])} Hz</td></tr>
<tr><td>Δf</td><td>{F(v["df"])} Hz</td></tr>
<tr><td>fp (notch)</td><td>{F(v["fp"])} Hz</td></tr></table></div><div><table>
<tr><th>Risultato</th><th></th></tr>
<tr><td>Rm</td><td>{v["Rm"]:.2f} Ω</td></tr>
<tr><td>Lm</td><td>{v["Lm"]*1e3:.3f} mH</td></tr>
<tr><td>Cm</td><td>{v["Cm"]*1e15:.2f} fF</td></tr>
<tr><td>C0</td><td>{v["C0"]*1e12:.2f} pF</td></tr>
<tr><td>Q a vuoto</td><td>{F(v["Q"],0)}</td></tr></table>
<p class="note">I valori estratti coincidono con quelli del modello (10 Ω · 10 mH · 25,33 fF · 5 pF) entro lo 0,1 %.</p></div></div>''')
v11=json.load(open("vals11.json"))
fix11='''<svg viewBox="0 0 420 230" width="100%" font-family="DejaVu Sans" font-size="15" stroke="#0a1a2e" stroke-width="2.5" fill="none">
<rect x="20" y="50" width="110" height="110" rx="10" fill="#e8f6fd"/>
<line x1="130" y1="105" x2="260" y2="105"/><line x1="260" y1="105" x2="260" y2="120"/>
<rect x="240" y="120" width="40" height="70" rx="4" fill="#fff"/><line x1="245" y1="132" x2="275" y2="132"/><line x1="245" y1="178" x2="275" y2="178"/>
<line x1="260" y1="190" x2="260" y2="205"/><line x1="240" y1="205" x2="280" y2="205"/><line x1="248" y1="212" x2="272" y2="212"/><line x1="255" y1="219" x2="265" y2="219"/>
<g stroke="none" fill="#0a1a2e"><text x="44" y="100" font-weight="700">Porta 1</text><text x="50" y="122">S11</text>
<text x="292" y="160" font-weight="700" fill="#1593d1">XTAL</text><text x="292" y="180" fill="#666" font-size="13">verso massa</text>
<text x="150" y="40" fill="#666" font-size="13">OSL ai pin del quarzo</text></g>
</svg>'''
S("Alternativa: misura in S11 (quarzo verso massa)", f'''<div class="two"><div style="display:flex;flex-direction:column;align-items:center"><div style="width:300px">{fix11}</div><div class="fig" style="width:310px">{svg("smith.svg")}</div></div><div><ul>
<li>Il quarzo va tra <b>porta 1 e massa</b>: il VNA lavora come analizzatore d'impedenza.</li>
<li>Calibrazione <b>OSL</b> (open-short-load) direttamente ai pin del quarzo.</li>
<li>Dal coefficiente di riflessione ricavi l'impedenza:</li></ul>
<div class="eq">Z = Z0 · (1 + S11) / (1 − S11)</div>
<ul><li><b>fs</b>: X = 0 con |Z| minimo, dove sulla carta di Smith il cerchio di risonanza taglia l'asse reale vicino al centro.</li>
<li><b>fp</b>: X = 0 con |Z| massimo, sul bordo destro della carta (Γ ≈ 1).</li></ul></div></div>''')
S("S11: estrazione dei parametri", f'''<div class="two"><div class="fig">{svg("zph.svg")}
<div class="eq"><b>Rm</b> = R(fs) &nbsp;&nbsp; <b>Lm</b> = Rm / (2π·Δf)</div>
<div class="eq"><b>Q</b> = fs / Δf &nbsp;&nbsp; <b>Cm</b> = 1 / ((2π·fs)²·Lm)</div></div><div>
<p class="note" style="margin-top:0">Δf è la distanza fra i punti dove la fase di Z vale ±45° (|X| = R). Il quarzo non è caricato da 2·Z0, quindi Q è <b>già quello a vuoto</b>. Nell'esempio: Δf = {v11["df"]:.0f} Hz, Rm = {v11["Rm"]:.2f} Ω, Lm = {v11["Lm"]*1e3:.3f} mH, <span style="white-space:nowrap">Q = {F(v11["Q"],0)}</span>.</p>
<h3>Vantaggi</h3><ul><li>Lettura diretta di Rm e Q a vuoto</li><li>Rm (pochi Ω – decine di Ω) è vicina a 50 Ω, dove S11 è più accurato</li></ul>
<h3>Limiti</h3><ul><li>A fp |Z| ≈ {v11["Zfp"]/1e6:.1f} MΩ e |S11| ≈ 1: meglio calcolarla da Cm e C0 o misurarla in S21</li>
<li>C0 lontano dalla risonanza è poco precisa (≈ 3 kΩ a 10 MHz): meglio usare un LCR meter</li>
<li>Le capacità parassite verso massa finiscono in parallelo a C0</li><li>Serve uno span stretto: Δf è di poche centinaia di Hz</li></ul></div></div>''')
S("Migliorare la precisione", '''<div class="two"><div><h3>Abbassare l'impedenza vista dal quarzo</h3><ul>
<li>I 2·50 Ω in serie abbassano il <b>Q caricato</b> (circa 5 700 nell'esempio, contro 63 000 a vuoto): la curva si allarga e Lm diventa meno preciso, soprattutto se Rm è piccola.</li>
<li>La norma <b>IEC 60444</b> usa un <b>pi-network da 12,5 Ω</b>. Una versione casalinga: attenuatori o trasformatori 4:1 su entrambe le porte (con Z0 = 12,5 Ω nelle formule).</li></ul></div><div>
<h3>Parassiti e alternative</h3><ul>
<li>Le capacità del fixture si sommano a C0 e spostano fp: calibra il più vicino possibile ai pin, oppure misura e sottrai la capacità del fixture vuoto.</li>
<li>Combina i due metodi: <b>S11</b> per fs, Rm, Lm e Q, <b>S21</b> (o il calcolo) per fp e C0.</li>
<li>C0 si può anche misurare lontano dalla risonanza, dove il quarzo si comporta da condensatore.</li></ul></div></div>''')
S("Frequenza con capacità di carico e checklist", '''<div class="two"><div><h3>Oscillatore parallelo con CL</h3>
<div class="eq">fL ≈ fs · (1 + Cm / (2·(C0 + CL)))</div>
<p class="note">Con i valori dell'esempio e CL = 20 pF: fL ≈ fs + 5,1 kHz. Il <i>pulling</i> del quarzo dipende soprattutto dal rapporto Cm/(C0+CL).</p></div><div>
<h3>Checklist</h3><ol>
<li>Fixture corto, calibrazione ai pin</li><li>Potenza −10…−20 dBm, IF BW basso</li>
<li>Span stretto, molti punti</li><li>Leggi fs, |S21|pk, f₁ e f₂ a ±45°, fp</li>
<li>Calcola Rm → Lm → Cm → C0 → Q</li><li>Ripeti a potenze diverse per verificare il drive level</li></ol></div></div>''')
css='''@page{size:1280px 720px;margin:0}*{box-sizing:border-box}body{margin:0;font-family:"DejaVu Sans",Arial,sans-serif;color:#1b2430}
.slide{width:1280px;height:720px;position:relative;overflow:hidden;page-break-after:always;padding:56px 70px 60px;background:#fff}
.slide h2{margin:0 0 28px;padding-right:120px;font-size:36px;color:#0a1a2e;border-left:8px solid #22b8f0;padding-left:18px}
.hdrlogo{position:absolute;top:22px;right:44px}.hdrlogo img{width:92px;height:92px}
.foot{position:absolute;bottom:22px;left:70px;right:70px;font-size:13px;color:#8a94a3;display:flex;justify-content:space-between}
.two{display:grid;grid-template-columns:1fr 1fr;gap:44px;align-items:center}
ul,ol{font-size:19px;line-height:1.5;padding-left:24px;margin:6px 0}li{margin-bottom:8px}
h3{color:#1593d1;font-size:22px;margin:0 0 10px}
.eq{background:#e8f6fd;border-radius:8px;padding:10px 16px;margin:8px 0;font-size:20px;font-family:"DejaVu Sans Mono",monospace}
.note{font-size:16px;color:#4a5566;line-height:1.45}.cap{font-size:17px;color:#4a5566;margin-top:6px;line-height:1.45}
.fig svg{width:100%;height:auto}
table{border-collapse:collapse;width:100%;font-size:18px}th{text-align:left;color:#1593d1;border-bottom:2px solid #1593d1;padding:8px}td{padding:8px;border-bottom:1px solid #e1e6ee}td:last-child{text-align:right;font-family:"DejaVu Sans Mono",monospace}
.cover{height:100%;display:flex;flex-direction:column;justify-content:center}.cover h1{font-size:64px;color:#0a1a2e;margin:28px 0 18px;line-height:1.1}
.cover .sub{font-size:24px;color:#4a5566;max-width:900px}.cover .by{font-size:20px;color:#1593d1;font-weight:700;margin-top:30px}
.clogo img{width:260px;height:260px}.cover{padding-left:20px}.slide.c{background:linear-gradient(135deg,#fff 55%,#e8f6fd)}.cover{flex-direction:row!important;align-items:center;gap:60px;justify-content:flex-start!important}'''
out=[f"<!DOCTYPE html><html><head><meta charset='utf-8'><style>{css}</style></head><body>"]
for i,(t,b) in enumerate(slides):
    if not t: out.append(f'<section class="slide c">{b}</section>');continue
    out.append(f'<section class="slide"><div class="hdrlogo">{logo}</div><h2>{t}</h2>{b}<div class="foot"><span>Misurare un quarzo con il VNA · IV3HGA</span><span>{i+1}/{len(slides)}</span></div></section>')
out.append("</body></html>")
open("slides.html","w").write("".join(out))
