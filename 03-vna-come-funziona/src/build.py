import re,json,base64
v=json.load(open("vals.json"))
def svg(p):
    s=open(p).read(); s=re.sub(r'<\?xml.*?\?>','',s,flags=re.S); s=re.sub(r'<!DOCTYPE.*?>','',s,flags=re.S)
    return re.sub(r'(<svg[^>]*?)\swidth="[^"]*"\s+height="[^"]*"',r'\1 width="100%"',s,count=1)
logo='<img src="data:image/png;base64,'+base64.b64encode(open("logo.png","rb").read()).decode()+'">'
css=open("style.css").read()+".diag svg{width:100%;height:auto}"
N="#0a1a2e"; C="#1593d1"; L="#e8f6fd"
def eq(x): return f'<div class="eq">{x}</div>'
ARW=f'<defs><marker id="ar" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0L10 5L0 10z" fill="{N}"/></marker><marker id="ac" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0L10 5L0 10z" fill="{C}"/></marker></defs>'
waves=f'''<svg viewBox="0 0 560 250" font-family="DejaVu Sans" font-size="18">{ARW}
<rect x="210" y="60" width="140" height="130" rx="10" fill="{L}" stroke="{N}" stroke-width="2.5"/>
<text x="280" y="132" text-anchor="middle" font-weight="700" fill="{N}">DUT</text>
<g stroke="{N}" stroke-width="2.5"><line x1="40" y1="95" x2="200" y2="95" marker-end="url(#ar)"/><line x1="360" y1="95" x2="520" y2="95" marker-end="url(#ar)"/></g>
<g stroke="{C}" stroke-width="2.5"><line x1="200" y1="155" x2="40" y2="155" marker-end="url(#ac)"/><line x1="520" y1="155" x2="360" y2="155" marker-end="url(#ac)"/></g>
<g font-weight="700"><text x="110" y="85" fill="{N}">a1</text><text x="110" y="185" fill="{C}">b1</text><text x="430" y="85" fill="{N}">b2</text><text x="430" y="185" fill="{C}">a2</text></g>
<g fill="#666" font-size="14"><text x="40" y="40">Porta 1</text><text x="470" y="40">Porta 2</text><text x="40" y="230">a = onda incidente · b = onda uscente</text></g></svg>'''
def box(x,y,w,h,t,fill=L,fs=15):
    lines=t.split("|"); ty=y+h/2-(len(lines)-1)*9+5
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="8" fill="{fill}" stroke="{N}" stroke-width="2"/>'+"".join(f'<text x="{x+w/2}" y="{ty+i*18}" text-anchor="middle" font-size="{fs}" fill="{N}">{l}</text>' for i,l in enumerate(lines))
def ln(x1,y1,x2,y2,c=N,dash=""): return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{c}" stroke-width="2" {"stroke-dasharray=\"5 4\"" if dash else ""} marker-end="url(#{"ac" if c==C else "ar"})"/>'
blk=f'''<svg viewBox="0 0 1140 400" font-family="DejaVu Sans">{ARW}
{box(10,40,150,70,"Sorgente|(sintetizzatore|PLL)",L,14)}
{ln(160,75,205,75)}{box(205,45,110,60,"Splitter")}
{ln(315,75,375,75)}{box(375,35,190,80,"Ponte o|accoppiatore|direzionale")}
{ln(565,75,640,75)}<circle cx="650" cy="75" r="9" fill="#fff" stroke="{N}" stroke-width="2"/><text x="650" y="25" text-anchor="middle" font-size="14" fill="{N}">Porta 1</text>
<line x1="659" y1="75" x2="700" y2="75" stroke="{N}" stroke-width="2"/>{box(700,45,130,60,"DUT","#fff",17)}<line x1="830" y1="75" x2="871" y2="75" stroke="{N}" stroke-width="2"/>
<circle cx="880" cy="75" r="9" fill="#fff" stroke="{N}" stroke-width="2"/><text x="880" y="25" text-anchor="middle" font-size="14" fill="{N}">Porta 2</text>
{ln(889,75,960,75)}{box(960,45,170,60,"Carico 50 Ω|+ campionamento")}
{ln(260,105,260,170,C)}{ln(470,115,470,170,C)}{ln(1045,105,1045,170,C)}
{box(195,170,130,60,"Ricevitore R|(riferimento)","#fff")}{box(405,170,130,60,"Ricevitore A|(riflessa)","#fff")}{box(980,170,130,60,"Ricevitore B|(trasmessa)","#fff")}
<g stroke="{N}" stroke-width="1.6" stroke-dasharray="5 4" fill="none"><path d="M225 262 H1010"/><path d="M225 262 V232"/><path d="M435 262 V232"/><path d="M1010 262 V232"/></g>
{box(620,246,190,32,"LO (oscillatore locale)",L,14)}
{ln(260,230,260,300)}{ln(470,230,470,300)}{ln(1045,230,1045,300)}
{box(195,300,915,56,"IF → ADC → DSP: ampiezza e fase complesse di R, A, B  →  S11 = A/R,  S21 = B/R")}
<text x="12" y="390" font-size="13" fill="#666">Schema semplificato di un VNA "T/R" a una via (come i NanoVNA). Un VNA completo ha uno switch e ricevitori anche sulla porta 2.</text></svg>'''
flow=f'''<svg viewBox="0 0 560 260" font-family="DejaVu Sans" font-size="17">{ARW}
<rect x="18" y="20" width="350" height="200" rx="10" fill="{L}" stroke="#9aa5b4" stroke-dasharray="6 5"/>
<text x="193" y="245" text-anchor="middle" font-size="14" fill="#666">"adattatore d'errore" (VNA + cavi + connettori)</text>
<g fill="{N}"><circle cx="60" cy="60" r="6"/><circle cx="60" cy="180" r="6"/><circle cx="330" cy="60" r="6"/><circle cx="330" cy="180" r="6"/></g>
{ln(66,60,322,60)}{ln(322,180,68,180)}{ln(60,66,60,172,C)}{ln(330,66,330,172,C)}
<text x="195" y="48" text-anchor="middle" fill="{N}">e10</text><text x="195" y="205" text-anchor="middle" fill="{N}">e01</text>
<text x="72" y="125" fill="{C}" font-weight="700">e00 = Ed</text><text x="242" y="125" fill="{C}" font-weight="700">Es</text><text x="242" y="145" fill="{C}" font-size="14">= e11</text>
<line x1="330" y1="60" x2="440" y2="60" stroke="{N}" stroke-width="2"/><line x1="440" y1="180" x2="336" y2="180" stroke="{N}" stroke-width="2"/>
<rect x="440" y="45" width="100" height="150" rx="8" fill="#fff" stroke="{N}" stroke-width="2"/><text x="490" y="125" text-anchor="middle" font-weight="700" fill="{N}">DUT Γa</text>
<text x="20" y="14" font-size="13" fill="#666">a (sorgente) in alto · b (misura) in basso</text></svg>'''
S=[]
def add(t,b): S.append((t,b))
add("",f'''<div class="cover"><div class="clogo">{logo}</div><div>
<h1>Come funziona<br>un VNA</h1>
<p class="sub">Onde, parametri S, ricevitori, modello d'errore e calibrazione: cosa succede davvero dentro un analizzatore di reti vettoriale</p>
<p class="by">Elia · IV3HGA</p></div></div>''')
add("Cos'è un VNA",f'''<div class="two"><div><ul>
<li>Un <b>analizzatore di reti</b> invia un segnale noto al dispositivo (DUT) e misura cosa torna indietro e cosa passa.</li>
<li><b>Vettoriale</b> significa che misura <b>ampiezza e fase</b>, cioè numeri complessi, non solo potenze.</li>
<li>Non misura potenze assolute ma <b>rapporti</b> tra onde: per questo è così preciso.</li></ul></div><div>
<h3>Rispetto ad altri strumenti</h3><table>
<tr><th>Strumento</th><th>Cosa vede</th></tr>
<tr><td>Rosmetro</td><td style="font-family:inherit;text-align:left">solo |Γ| (SWR)</td></tr>
<tr><td>SNA / tracking gen.</td><td style="font-family:inherit;text-align:left">|S21|, |S11| scalari</td></tr>
<tr><td>VNA</td><td style="font-family:inherit;text-align:left">S11, S21… complessi</td></tr></table>
<p class="note">Con la fase arrivano impedenze, carta di Smith, group delay, dominio del tempo e soprattutto la <b>correzione degli errori</b>, che con un analizzatore scalare non si può fare in modo completo.</p></div></div>''')
add("Onde e parametri S",f'''<div class="two"><div class="diag">{waves}</div><div>
{eq("b1 = S11·a1 + S12·a2")}{eq("b2 = S21·a1 + S22·a2")}
<ul class="small"><li><b>S11 = b1/a1</b> con a2 = 0 (porta 2 chiusa su 50 Ω): riflessione all'ingresso.</li>
<li><b>S21 = b2/a1</b> con a2 = 0: trasmissione, cioè guadagno o attenuazione.</li>
<li>S22 e S12 sono gli stessi visti dalla porta 2.</li></ul>
<p class="note">Si usano le onde e non tensioni e correnti perché in RF le onde si misurano bene su 50 Ω, mentre cortocircuiti e aperti ideali, necessari per i parametri Z e Y, non esistono.</p></div></div>''')
add("Architettura a blocchi",f'''<div class="diag" style="width:96%">{blk}</div><div class="grid3" style="margin-top:4px">
<div class="card"><h3>R: riferimento</h3><p>Campiona l'onda incidente a1, cioè quello che la sorgente sta davvero mandando.</p></div>
<div class="card"><h3>A: riflessa</h3><p>Riceve dal ponte l'onda b1 che torna dal DUT sulla porta 1.</p></div>
<div class="card"><h3>B: trasmessa</h3><p>Riceve l'onda b2 che esce dal DUT sulla porta 2.</p></div></div>''')
add("Separare le onde: ponte e accoppiatore",f'''<div class="two"><div><h3>Il problema</h3><ul>
<li>Sullo stesso cavo viaggiano l'onda incidente e quella riflessa: per misurare S11 bisogna <b>separarle</b>.</li>
<li><b>Ponte resistivo</b> (Wheatstone): banda larghissima, fino a pochi kHz, ma con perdite di 6 dB o più. È la scelta dei VNA economici.</li>
<li><b>Accoppiatore direzionale</b>: perdite basse, ma funziona solo in una banda limitata, soprattutto verso il basso.</li></ul></div><div>
<h3>La direttività</h3><ul><li>Un separatore reale lascia passare un po' di onda incidente nel ramo "riflessa".</li>
<li>La <b>direttività</b> è quanto questa perdita è sotto il segnale riflesso vero: con 30 dB non distingui bene carichi con return loss vicino a 30 dB.</li>
<li>Si tratta di un errore sistematico (Ed), e la calibrazione lo sottrae: la direttività <b>effettiva</b> dopo la calibrazione dipende dalla qualità del carico usato.</li></ul></div></div>''')
add("Il ricevitore",f'''<div class="two"><div><ul>
<li>Ogni ricevitore (R, A, B) <b>converte</b> il segnale RF a una frequenza intermedia fissa: f<sub>IF</sub> = |f<sub>RF</sub> − f<sub>LO</sub>|.</li>
<li>Un <b>ADC</b> campiona l'IF e il DSP ne estrae parte reale e immaginaria (I/Q), cioè ampiezza e fase.</li>
<li>Siccome tutti i ricevitori usano lo stesso LO, i loro <b>rapporti</b> sono coerenti in fase: il rumore di fase della sorgente si cancella.</li>
<li>Nei VNA economici si sfruttano le <b>armoniche</b> della sorgente e del LO per salire in frequenza: nelle bande alte la dinamica cala.</li></ul></div><div>
<h3>IF bandwidth: rumore contro velocità</h3><table><tr><th>IF BW</th><th>Rumore di fondo</th></tr>
<tr><td>10 kHz</td><td>riferimento</td></tr><tr><td>1 kHz</td><td>−10 dB</td></tr><tr><td>100 Hz</td><td>−20 dB</td></tr><tr><td>10 Hz</td><td>−30 dB</td></tr></table>
<p class="note">Il rumore scala con 10·log(IF BW), mentre il tempo per punto cresce circa come 1/IF BW. <b>Dinamica</b> = potenza massima in ingresso al ricevitore − rumore di fondo, a una IF BW data.</p></div></div>''')
add("Dalle onde ai parametri S",f'''<div class="two"><div>
{eq("S11<sub>grezzo</sub> = A / R")}{eq("S21<sub>grezzo</sub> = B / R")}
<ul><li>Dividendo per R si eliminano le variazioni di ampiezza e fase della sorgente con la frequenza.</li>
<li>Restano però gli errori del <b>percorso</b>: cavi, connettori, ponte, adattamenti non perfetti. Per questo il dato è ancora "grezzo".</li></ul></div><div>
<h3>T/R oppure set completo di parametri S</h3><ul>
<li><b>T/R (una via)</b>: la sorgente sta solo sulla porta 1. Misura S11 e S21; per S22 e S12 devi girare il DUT. È il caso di NanoVNA e simili.</li>
<li><b>Set completo</b>: uno switch manda la sorgente alternativamente sulle due porte e misura tutti e quattro i parametri senza toccare il DUT.</li>
<li>Solo con il set completo è possibile la correzione a <b>12 termini</b>; con il T/R si usa una correzione ridotta (<i>enhanced response</i>).</li></ul></div></div>''')
add("Errori sistematici: il modello a 3 termini",f'''<div class="two"><div class="diag">{flow}</div><div>
{eq("Γm = Ed + Er·Γa / (1 − Es·Γa)")}
<ul class="small"><li><b>Ed</b> (direttività): segnale che arriva al ricevitore anche senza DUT.</li>
<li><b>Es</b> (adattamento della sorgente): la porta non è 50 Ω perfetti e rimanda indietro parte dell'onda riflessa.</li>
<li><b>Er = e10·e01</b> (tracking in riflessione): attenuazione e ritardo del percorso, cavo compreso.</li></ul>
<p class="note">Sono errori ripetibili: se li conosci, li togli. Restano gli errori casuali (rumore, connettori, cavi che si muovono) e la deriva.</p></div></div>''')
r1,r2=v["rl20_d30"]
add("Quanto pesa la direttività",f'''<div class="two"><div class="fig">{svg("directivity.svg")}</div><div><ul>
<li>L'onda dovuta a Ed si somma al riflesso vero con fase qualsiasi, quindi il valore misurato può cadere ovunque in una fascia.</li>
<li>Esempio: un carico con <b>RL vero 20 dB</b> e direttività 30 dB viene letto tra <b>{r1:.1f} e {r2:.1f} dB</b>.</li>
<li>Quando RL vero si avvicina alla direttività, l'errore esplode: il valore misurato può essere quasi qualsiasi.</li>
<li>Per questo ha senso misurare un buon carico a 50 Ω <b>dopo</b> la calibrazione: il suo RL ti dice la direttività effettiva del tuo setup.</li></ul></div></div>''')
add("Calibrazione SOL (Short, Open, Load)",f'''<div class="two"><div><ul>
<li>Tre incognite complesse (Ed, Es, Er) per ogni frequenza: servono <b>tre standard noti</b>.</li>
<li>Misuri Γm con il Load (Γ = 0), lo Short (Γ = −1) e l'Open (Γ = +1):</li></ul>
{eq("Ed = Γm<sub>L</sub>")}
<p class="note">Con s = Γm<sub>S</sub> − Ed e o = Γm<sub>O</sub> − Ed:</p>
{eq("Es = (o + s) / (o − s)")}{eq("Er = o·(1 − Es)")}</div><div>
<h3>Correzione di ogni misura</h3>
{eq("Γa = (Γm − Ed) / (Er + Es·(Γm − Ed))")}
<ul class="small"><li>Il VNA applica questa formula punto per punto, in tempo reale.</li>
<li>Gli standard reali non sono ideali: l'open ha una capacità di bordo, lo short un'induttanza e un ritardo. Il VNA usa i <b>coefficienti del kit</b> (C0…C3, L0…L3, offset delay) per sapere il loro Γ vero.</li>
<li>Il <b>piano di riferimento</b> cade dove colleghi gli standard: tutto ciò che sta prima viene tolto.</li></ul></div></div>''')
add("La calibrazione in azione (simulazione)",f'''<div class="two"><div><div class="fig">{svg("cal_mag.svg")}</div>
<p class="cap">Antenna simulata, risonante a 145 MHz con R = 40 Ω, misurata attraverso 1 m di cavo e un ponte imperfetto.</p></div><div><div class="fig" style="width:80%;margin:auto">{svg("cal_smith.svg")}</div>
<p class="note">Senza calibrazione il cavo fa ruotare la traccia sulla carta di Smith (ritardo) e la rimpicciolisce (perdita), mentre direttività e adattamento della sorgente la deformano. Dopo la SOL la curva torna identica a quella vera: lo scarto nella simulazione è ~10⁻¹⁶, cioè zero numerico.</p></div></div>''')
add("Calibrazione a due porte",f'''<div class="two"><div><h3>Il modello a 12 termini</h3>
<p class="note" style="margin-top:0">Per ogni direzione (avanti e indietro) ci sono 6 termini:</p>
<table><tr><td>Ed</td><td style="font-family:inherit;text-align:left">direttività</td></tr><tr><td>Es</td><td style="font-family:inherit;text-align:left">adattamento della sorgente</td></tr>
<tr><td>Er</td><td style="font-family:inherit;text-align:left">tracking in riflessione</td></tr><tr><td>El</td><td style="font-family:inherit;text-align:left">adattamento del carico (porta 2)</td></tr>
<tr><td>Et</td><td style="font-family:inherit;text-align:left">tracking in trasmissione</td></tr><tr><td>Ex</td><td style="font-family:inherit;text-align:left">isolamento (crosstalk)</td></tr></table></div><div>
<h3>Metodi</h3><ul class="small"><li><b>SOLT</b>: SOL su entrambe le porte + un Thru. È il più comune e richiede standard ben caratterizzati.</li>
<li><b>TRL</b> (Thru, Reflect, Line): usa linee di trasmissione invece degli standard noti. È ottimo per i fixture su PCB e in microstriscia.</li>
<li><b>Unknown thru / SOLR</b>: il thru non deve essere noto, basta che sia reciproco. Serve quando le porte hanno connettori diversi.</li>
<li><b>Port extension</b>: sposta il piano di riferimento compensando solo ritardo (e perdita). È veloce ma non corregge disadattamenti.</li></ul></div></div>''')
add("Errori casuali e buone pratiche",f'''<div class="two"><div><h3>Cosa la calibrazione non toglie</h3><ul>
<li><b>Rumore</b>: si riduce con IF BW più stretta o con la media.</li>
<li><b>Ripetibilità dei connettori</b>: ogni volta che colleghi qualcosa il contatto cambia leggermente. Serve una chiave dinamometrica per gli SMA.</li>
<li><b>Cavi che si muovono</b>: un cavo piegato dopo la calibrazione cambia fase e perdita.</li>
<li><b>Deriva termica</b>: lascia scaldare lo strumento prima di calibrare.</li></ul></div><div>
<h3>Checklist</h3><ol class="small"><li>Accendi e aspetta che lo strumento sia in temperatura</li><li>Imposta span, punti, potenza e IF BW <b>prima</b> di calibrare</li>
<li>Calibra esattamente dove colleghi il DUT</li><li>Verifica: misura il carico (RL alto) e l'open/short (|Γ| ≈ 1)</li>
<li>Non muovere i cavi; ricalibra se cambi impostazioni</li><li>Usa potenza adatta al DUT (amplificatori: attenua!)</li></ol></div></div>''')
add("Formati di visualizzazione",f'''<div class="two"><div><table>
<tr><th>Formato</th><th>Formula</th></tr>
<tr><td>Return loss</td><td>RL = −20·log|Γ|</td></tr>
<tr><td>SWR</td><td>(1 + |Γ|) / (1 − |Γ|)</td></tr>
<tr><td>Impedenza</td><td>Z = Z0·(1 + Γ)/(1 − Γ)</td></tr>
<tr><td>Mismatch loss</td><td>−10·log(1 − |Γ|²)</td></tr>
<tr><td>Insertion loss</td><td>−20·log|S21|</td></tr>
<tr><td>Group delay</td><td>−dφ/dω</td></tr></table></div><div><ul>
<li><b>Log mag e fase</b>: il formato di base, utile per filtri e amplificatori.</li>
<li><b>Carta di Smith</b>: la più espressiva per l'adattamento, perché vedi subito se il carico è induttivo o capacitivo e come adattarlo.</li>
<li><b>Polare</b>: Γ come vettore, utile per vedere il ritardo.</li>
<li><b>Dominio del tempo</b>: con l'IFFT dei dati in frequenza ottieni TDR e time-gating (vedi la presentazione sulle misure inconsuete).</li></ul></div></div>''')
add("Le specifiche che contano",f'''<div class="two"><div><ul>
<li><b>Gamma di frequenza</b>, e se agli estremi la dinamica è ancora utile.</li>
<li><b>Dinamica</b> in S21, a una IF BW indicata: decide quanto in basso puoi misurare un filtro o un isolamento.</li>
<li><b>Trace noise</b>: quanto è "stabile" la traccia in dB e gradi.</li>
<li><b>Direttività e adattamento della sorgente</b> grezzi, e soprattutto quelli effettivi dopo la calibrazione.</li></ul></div><div><ul>
<li><b>Potenza regolabile</b>: serve per non saturare gli amplificatori e per i quarzi.</li>
<li><b>Numero di punti e velocità</b>: contano per i risonatori ad alto Q e per la taratura dal vivo.</li>
<li><b>Architettura</b>: T/R o set completo, numero di ricevitori, armoniche.</li>
<li><b>Kit di calibrazione</b>: un VNA è preciso quanto i suoi standard.</li></ul></div></div>''')
out=[f"<!DOCTYPE html><html><head><meta charset='utf-8'><style>{css}</style></head><body>"]
for i,(t,b) in enumerate(S):
    if not t: out.append(f'<section class="slide c">{b}</section>');continue
    out.append(f'<section class="slide"><div class="hdrlogo">{logo}</div><h2>{t}</h2>{b}<div class="foot"><span>Come funziona un VNA · IV3HGA</span><span>{i+1}/{len(S)}</span></div></section>')
out.append("</body></html>"); open("slides.html","w").write("".join(out))
