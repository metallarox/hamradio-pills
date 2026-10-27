import re,json,base64
v=json.load(open("vals.json"))
def svg(p):
    s=open(p).read(); s=re.sub(r'<\?xml.*?\?>','',s,flags=re.S); s=re.sub(r'<!DOCTYPE.*?>','',s,flags=re.S)
    return re.sub(r'(<svg[^>]*?)\swidth="[^"]*"\s+height="[^"]*"',r'\1 width="100%"',s,count=1)
logo='<img src="data:image/png;base64,'+base64.b64encode(open("logo.png","rb").read()).decode()+'">'
css=open("style.css").read()
S=[]
def add(t,b): S.append((t,b))
def eq(x): return f'<div class="eq">{x}</div>'
add("",f'''<div class="cover"><div class="clogo">{logo}</div><div>
<h1>Misure inconsuete<br>con il VNA</h1>
<p class="sub">Ferriti, componenti, linee, materiali, misure senza contatto e sistemi: 12 cose che il VNA sa fare oltre a SWR e filtri</p>
<p class="by">Elia · IV3HGA</p></div></div>''')
cards=[("Ferriti","μ' e μ'' di un toroide sconosciuto"),("SRF, ESR, Q","il limite reale di L e C"),("Choke in modo comune","quanta impedenza blocca davvero"),
("Shunt-through","milliohm: PDN ed ESR"),("Risonatori e group delay","ceramici, SAW, cavità"),("TDR","guasti e fattore di velocità"),
("εr e tan δ del PCB","risonatore ad anello"),("Umidità","la εr dell'acqua è circa 80"),("Grid-dip e NFC","risonanze senza contatto"),
("Accoppiamento k","due picchi, un numero"),("Isolamento e schermatura","S21 tra antenne e contenitori"),("Time-gating","antenne misurate in stanza")]
add("Panoramica",'<div class="grid3">'+"".join(f'<div class="card"><h3>{a}</h3><p>{b}</p></div>' for a,b in cards)+'</div>')
add("1 · Ferriti: identificare un toroide sconosciuto",f'''<div class="two"><div class="fig">{svg("ferrite.svg")}<p class="cap">Andamento tipico (modello simulato a rilassamento).</p></div><div><ul class="small">
<li>Avvolgi poche spire N sul toroide (anche una sola) e misura <b>S11 → Z = R + jX</b>, con calibrazione ai capi del filo.</li>
<li>Dalle dimensioni ricavi l'induttanza "in aria" per spira:</li></ul>
{eq("L0 = μ0·h·ln(OD/ID) / 2π")}
{eq("μ' = X / (ω·N²·L0) &nbsp; μ'' = R / (ω·N²·L0)")}
<p class="note">Confronta le curve con i datasheet (Fair-Rite e simili): il punto di incrocio μ' = μ'' e il valore iniziale identificano il mix. Usa poche spire, perché la capacità tra le spire falsa le misure alle frequenze alte.</p></div></div>''')
add("2 · SRF, ESR e Q dei componenti",f'''<div class="two"><div class="fig">{svg("srf.svg")}<p class="cap">Condensatore da 100 nF con ESL 1 nH ed ESR 20 mΩ.</p></div><div><ul class="small">
<li>Oltre la <b>SRF</b> un condensatore si comporta da induttore, e un induttore da condensatore.</li>
<li>Dal minimo di |Z| ricavi ESR e SRF, e da questi l'induttanza parassita:</li></ul>
{eq("ESL = 1 / ((2π·SRF)²·C)")}
{eq("Q<sub>L</sub> = X / R &nbsp;(induttori)")}
<p class="note">Per condensatori grandi, con |Z| di pochi mΩ, S11 non basta: serve lo shunt-through (slide 4). Gli induttori si misurano bene in S11 o in serie in S21. Un SMD va saldato su un fixture con piste cortissime e calibrato.</p></div></div>''')
add("3 · Choke in modo comune e balun 1:1",f'''<div class="two"><div><ul>
<li>Il choke va <b>in serie</b> tra porta 1 e porta 2, con i conduttori del cavo (o la coppia bifilare) cortocircuitati ai due capi: così vedi solo il modo comune.</li>
<li>L'impedenza si ricava da S21 complesso:</li></ul>
{eq("Z = 2·Z0 · (1 − S21) / S21")}
<table><tr><th>|Z| choke</th><th>|S21|</th></tr><tr><td>500 Ω</td><td>≈ −15.6 dB</td></tr><tr><td>1 kΩ</td><td>≈ −20.8 dB</td></tr><tr><td>5 kΩ</td><td>≈ −34.2 dB</td></tr></table></div><div>
<ul><li>Conta la parte <b>resistiva</b>: un choke molto reattivo può risuonare con il cavo e peggiorare le cose.</li>
<li>Misura su tutta la banda d'uso, non solo a una frequenza.</li>
<li>Collega il choke con collegamenti corti e lontano da piani metallici: la capacità verso massa abbassa le letture alle frequenze alte.</li>
<li>Con lo stesso metodo verifichi i <b>balun</b> 1:1 e le ferriti a clip sui cavi di alimentazione.</li></ul></div></div>''')
add("4 · Shunt-through: misurare i milliohm",f'''<div class="two"><div><ul>
<li>Il DUT va <b>in parallelo</b> alla linea tra porta 1 e porta 2, nello stesso punto.</li>
<li>Un'impedenza piccolissima diventa un S21 piccolo ma ben misurabile:</li></ul>
{eq("Z = (Z0/2) · S21 / (1 − S21) &nbsp;≈ 25 Ω · S21")}
<table><tr><th>Z DUT</th><th>|S21|</th></tr><tr><td>1 Ω</td><td>≈ −28.3 dB</td></tr><tr><td>100 mΩ</td><td>≈ −48.0 dB</td></tr><tr><td>10 mΩ</td><td>≈ −68.0 dB</td></tr></table></div><div>
<h3>Per cosa usarlo</h3><ul><li>Impedenza della rete di alimentazione (PDN) di una scheda</li><li>ESR di condensatori elettrolitici e di bulk</li><li>Impedenza di trasferimento di schermi e cavi</li></ul>
<h3>Attenzione</h3><ul><li>Alle basse frequenze la calza dei cavi crea un <b>ground loop</b> che si somma al DUT: metti un isolatore di massa o molte ferriti sul cavo della porta 2.</li>
<li>Calibrazione <i>through</i> e cavi rigidi, con collegamenti con la minima induttanza possibile.</li></ul></div></div>''')
add("5 · Risonatori, SAW e cavità: group delay",f'''<div class="two"><div><ul>
<li>Si misurano come il quarzo: fs, fp e modello equivalente per i risonatori ceramici; S21 e S11 per filtri SAW e cavità.</li>
<li>Il <b>group delay</b> è la derivata della fase, e quasi tutti i VNA lo mostrano direttamente:</li></ul>
{eq("τg = − dφ/dω = − (1/360°)·dφ/df")}
{eq("Q<sub>L</sub> ≈ π·f0·τg &nbsp;(risonatore singolo, al centro)")}</div><div>
<ul><li>Nei duplexer e nei combiner a cavità il ripple del group delay in banda indica la taratura: risonatori "storti" danno picchi asimmetrici.</li>
<li>Nei filtri SAW verifichi la piattezza del delay, che è importante per le modulazioni digitali.</li>
<li>Usa un'apertura di smoothing ridotta: troppa media appiattisce i dettagli, troppo poca rende il delay rumoroso.</li></ul></div></div>''')
add("6 · TDR: guasti nei cavi e fattore di velocità",f'''<div class="fig" style="width:92%">{svg("tdr.svg")}</div><div class="two" style="align-items:start;gap:30px"><div>
{eq("d = VF·c·t / 2")}
{eq("d<sub>max</sub> = VF·c / (2·Δf<sub>step</sub>)")}</div><div><p class="note" style="margin-top:4px">Simulazione: span 1 GHz con 2001 punti (passo 0,5 MHz), quindi d<sub>max</sub> ≈ {v["dmax"]:.0f} m con VF 0,66 e risoluzione di circa 10–20 cm. Con la modalità <i>lowpass step</i> il tipo di discontinuità diventa leggibile: un gradino in su è una Z più alta (schiacciatura, aperto), uno in giù una Z più bassa (acqua, corto). Se conosci la lunghezza, dal picco dell'aperto ricavi il VF.</p></div></div>''')
add("7 · εr e tan δ di un substrato PCB",f'''<div class="two"><div><ul>
<li>Realizza un <b>risonatore ad anello</b> in microstriscia, debolmente accoppiato da due gap, e misura S21.</li>
<li>Al picco n-esimo la circonferenza media vale n lunghezze d'onda guidate:</li></ul>
{eq("εeff = ( n·c / (2π·r·f<sub>n</sub>) )²")}
<p class="note">Poi ricavi εr invertendo la formula della microstriscia (Hammerstad):</p>
{eq("εeff = (εr+1)/2 + (εr−1)/2 · (1 + 12h/W)<sup>−½</sup>")}</div><div>
<ul class="small"><li>Il Q caricato si legge dalla banda a −3 dB. Con accoppiamento simmetrico: Q<sub>u</sub> = Q<sub>L</sub> / (1 − |S21|<sub>pk</sub>).</li>
<li>Si separano le perdite: 1/Q<sub>u</sub> = 1/Q<sub>c</sub> + 1/Q<sub>d</sub> + 1/Q<sub>r</sub>. Da Q<sub>d</sub>:</li></ul>
{eq("tan δ = εeff(εr−1) / (εr(εeff−1)·Q<sub>d</sub>)")}
<p class="note">Più picchi n = 1, 2, 3 ti danno εr in funzione della frequenza. In alternativa basta uno stub λ/2 aperto, meno preciso perché risente degli effetti di bordo.</p></div></div>''')
add("8 · Umidità di terreno, legno e materiali",f'''<div class="two"><div><ul>
<li>L'acqua ha <b>εr ≈ 80</b>, mentre il terreno secco sta tra 3 e 5 e il legno secco tra 2 e 4: piccole quantità d'acqua spostano molto la εr apparente.</li>
<li><b>Sonda TDR</b>: due aste parallele di lunghezza L infilate nel materiale. Misuri il tempo t di andata e ritorno lungo le aste:</li></ul>
{eq("Ka = ( c·t / (2L) )²")}
<p class="note">Equazione di Topp (1980) per i terreni minerali, contenuto volumetrico d'acqua θv:</p>
{eq("θv = −0.053 + 0.0292·Ka − 5.5·10⁻⁴·Ka² + 4.3·10⁻⁶·Ka³")}</div><div>
<ul><li><b>Sonda capacitiva / risonante</b>: un LC o una linea aperta a contatto con il materiale. Lo spostamento della risonanza (o la variazione di S11) segue l'umidità.</li>
<li>Calibra sempre su campioni noti (secco e pesato dopo bagnatura): la relazione dipende dal materiale.</li>
<li>Alle frequenze basse sale la conducibilità (sali disciolti), quindi conviene lavorare a centinaia di MHz.</li></ul></div></div>''')
add("9 · Grid-dip moderno e antenne NFC",f'''<div class="two"><div><h3>Risonanze senza contatto</h3><ul>
<li>Collega una piccola <b>spira</b> (1–2 spire, qualche cm) alla porta 1 e avvicinala al circuito risonante.</li>
<li>Alla risonanza compare un <b>dip in |S11|</b> (o un picco in Re Z): è il grid-dip meter, con la frequenza letta direttamente.</li>
<li>Allontana la spira finché il dip resta appena visibile: con un accoppiamento stretto la risonanza si sposta.</li>
<li>Funziona su trappole, circuiti LC, bobine di antenne, cavità e linee.</li></ul></div><div>
<h3>Tag NFC e RFID (13,56 MHz)</h3><ul><li>Con lo stesso metodo vedi dove risuona l'antenna di un tag o di un lettore, e il suo Q.</li>
<li>Il metallo vicino crea correnti parassite: <b>L diminuisce</b>, la risonanza sale e il Q crolla. Per questo esistono i fogli di ferrite sotto i tag "on-metal".</li>
<li>Utile per capire perché un tag non funziona su una superficie specifica.</li></ul></div></div>''')
add("10 · Coefficiente di accoppiamento k",f'''<div class="two"><div class="fig">{svg("coupling.svg")}<p class="cap">Due risonatori identici a 10 MHz, Q ≈ 80, accoppiati debolmente alle porte.</p></div><div><ul class="small">
<li>Due risonatori accoppiati (bobine di ricarica wireless, link induttivi, filtri a più poli) danno <b>due picchi</b> f1 e f2 in S21.</li>
<li>Per accoppiamento magnetico:</li></ul>
{eq("k = (f2² − f1²) / (f2² + f1²)")}
<ul class="small"><li>Nella simulazione con k = 0,10 i picchi a {v["f1"]/1e6:.2f} e {v["f2"]/1e6:.2f} MHz danno k ≈ {v["k_est"]:.3f}.</li>
<li>Sotto l'accoppiamento critico (k &lt; circa 1/Q) i picchi non si separano, come per la curva k = 0,02.</li>
<li>Le porte devono essere accoppiate debolmente ai risonatori, altrimenti lo caricano e spostano i picchi.</li></ul></div></div>''')
add("11 · Isolamento tra antenne e schermatura",f'''<div class="two"><div><h3>Isolamento tra antenne</h3><ul>
<li>Le due antenne montate vanno su porta 1 e porta 2: <b>isolamento = −|S21|</b>, con calibrazione <i>through</i> ai connettori delle antenne.</li>
<li>Per un ripetitore l'isolamento deve superare il guadagno di almeno 10–15 dB, altrimenti si innesca.</li>
<li>Cambiando distanza verticale o orizzontale e polarizzazione trovi la configurazione migliore prima di salire sul traliccio.</li></ul></div><div>
<h3>Efficacia di schermatura</h3><ul><li>Un'antenna dentro e una fuori dal contenitore, dalla gabbia o dalla busta:</li></ul>
{eq("SE (dB) = |S21|<sub>senza</sub> − |S21|<sub>con</sub>")}
<ul class="small"><li>La misura è limitata dalla <b>dinamica</b> del VNA: se SE si avvicina al rumore di fondo il risultato è solo un minimo.</li>
<li>Il cavo che entra nel contenitore è esso stesso una perdita: mettici ferriti o un passante.</li></ul></div></div>''')
add("12 · Time-gating: antenne misurate in stanza",f'''<div class="two"><div><ul>
<li>Trasformi S11 (o S21) nel dominio del tempo e vedi la risposta dell'antenna separata dalle riflessioni di pareti, soffitto e oggetti.</li>
<li>Metti un <b>gate</b> attorno alla risposta principale e torni in frequenza: ottieni un S11 "come in camera anecoica".</li>
<li>La risoluzione temporale dipende dallo span: circa 1/span, cioè 1 ns ≈ 30 cm in aria con 1 GHz di span.</li></ul></div><div>
<h3>Regole pratiche</h3><ul><li>Le riflessioni da escludere devono arrivare più tardi della risoluzione (oggetti a distanze maggiori di qualche decina di cm).</li>
<li>Il gate deformerà i bordi della banda: misura uno span più largo e scarta gli estremi.</li>
<li>Usa la modalità <i>bandpass</i> se non parti da frequenze vicine a DC.</li>
<li>Con lo stesso trucco togli l'effetto di un connettore o di un adattatore in un fixture.</li></ul></div></div>''')
rows=[("Ferriti","S11","spire sul toroide","μ', μ'', mix"),("SRF / ESR / Q","S11 o S21","fixture SMD","SRF, ESL, ESR, Q"),
("Choke CM","S21 serie","conduttori in corto","Z in modo comune"),("Shunt-through","S21 parallelo","DUT tra le linee","mΩ, PDN, ESR"),
("Risonatori, SAW","S21","fixture dedicato","τg, Q, ripple"),("TDR","S11 → tempo","cavo","distanza, Z, VF"),
("εr PCB","S21","anello in microstriscia","εr, tan δ"),("Umidità","S11","sonda TDR/capacitiva","Ka, θv"),
("Grid-dip / NFC","S11","spira di accoppiamento","f risonanza, Q"),("Accoppiamento","S21","due risonatori","k"),
("Isolamento / SE","S21","due antenne","dB di isolamento"),("Time-gating","S11/S21 → tempo","antenna in stanza","S11 depurato")]
add("Riepilogo",'<table class="sum"><tr><th>Misura</th><th>Parametro</th><th>Setup</th><th>Cosa ricavi</th></tr>'+"".join(f"<tr><td><b>{a}</b></td><td>{b}</td><td>{c}</td><td>{d}</td></tr>" for a,b,c,d in rows)+'</table>')
out=[f"<!DOCTYPE html><html><head><meta charset='utf-8'><style>{css}</style></head><body>"]
for i,(t,b) in enumerate(S):
    if not t: out.append(f'<section class="slide c">{b}</section>');continue
    out.append(f'<section class="slide"><div class="hdrlogo">{logo}</div><h2>{t}</h2>{b}<div class="foot"><span>Misure inconsuete con il VNA · IV3HGA</span><span>{i+1}/{len(S)}</span></div></section>')
out.append("</body></html>"); open("slides.html","w").write("".join(out))
