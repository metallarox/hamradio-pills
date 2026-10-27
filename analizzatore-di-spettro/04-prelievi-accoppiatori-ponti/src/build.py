import json
from deck import *
v=json.load(open("vals.json"))
D=Deck("Carico con prelievo,<br>accoppiatore e ponte","Usare l'analizzatore di spettro con un carico fittizio con presa di campionamento, un accoppiatore direzionale e un ponte riflettometrico: metodi, limiti e cosa si può vedere","L'analizzatore di spettro: prelievi, accoppiatori e ponti")
coupler=f'''<svg viewBox="0 0 900 260" font-family="DejaVu Sans">{ARW}
{box(10,50,140,70,"Trasmettitore","#fff",16)}{ln(150,85,260,85)}
<rect x="260" y="40" width="340" height="150" rx="10" fill="{L}" stroke="{N}" stroke-width="2"/>
<line x1="260" y1="85" x2="600" y2="85" stroke="{N}" stroke-width="3"/><line x1="330" y1="115" x2="530" y2="115" stroke="{C}" stroke-width="3"/>
<line x1="330" y1="115" x2="330" y2="190" stroke="{C}" stroke-width="2.5"/><line x1="530" y1="115" x2="530" y2="190" stroke="{C}" stroke-width="2.5"/>
<text x="430" y="70" text-anchor="middle" font-size="14" fill="{N}">linea principale</text><text x="430" y="140" text-anchor="middle" font-size="14" fill="{C}">linea accoppiata</text>
{ln(600,85,710,85)}{box(710,50,180,70,"Carico fittizio|o antenna","#fff",16)}
<circle cx="330" cy="200" r="8" fill="#fff" stroke="{N}" stroke-width="2"/><circle cx="530" cy="200" r="8" fill="#fff" stroke="{N}" stroke-width="2"/>
<text x="330" y="230" text-anchor="middle" font-size="14" font-weight="700" fill="{N}">REF</text><text x="330" y="248" text-anchor="middle" font-size="12" fill="#555">onda riflessa</text>
<text x="530" y="230" text-anchor="middle" font-size="14" font-weight="700" fill="{N}">FWD</text><text x="530" y="248" text-anchor="middle" font-size="12" fill="#555">onda diretta</text></svg>'''
R=lambda x1,y1,x2,y2,lab,lx,ly: f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{N}" stroke-width="2.2"/><rect x="{(x1+x2)/2-22}" y="{(y1+y2)/2-9}" width="44" height="18" rx="3" fill="#fff" stroke="{N}" stroke-width="2" transform="rotate({45 if (x2-x1)*(y2-y1)>0 else -45} {(x1+x2)/2} {(y1+y2)/2})"/><text x="{lx}" y="{ly}" font-size="14" fill="{N}">{lab}</text>'
bridge=f'''<svg viewBox="0 0 560 330" font-family="DejaVu Sans">
{R(260,40,140,160,"50 Ω",150,95)}{R(260,40,380,160,"50 Ω",330,95)}{R(140,160,260,280,"50 Ω",150,235)}
<line x1="380" y1="160" x2="260" y2="280" stroke="{N}" stroke-width="2.2"/><rect x="300" y="200" width="80" height="44" rx="6" fill="{C}" opacity=".15" stroke="{C}" stroke-width="2"/><text x="340" y="227" text-anchor="middle" font-size="15" font-weight="700" fill="{C}">DUT</text>
<g fill="{N}"><circle cx="260" cy="40" r="5"/><circle cx="140" cy="160" r="5"/><circle cx="380" cy="160" r="5"/><circle cx="260" cy="280" r="5"/></g>
<line x1="260" y1="40" x2="260" y2="15" stroke="{N}" stroke-width="2"/><text x="275" y="22" font-size="14" fill="{N}">sorgente (TG)</text>
<line x1="260" y1="280" x2="260" y2="305" stroke="{N}" stroke-width="2"/><text x="275" y="318" font-size="14" fill="{N}">massa / ritorno sorgente</text>
<line x1="140" y1="160" x2="40" y2="160" stroke="{N}" stroke-width="2"/><line x1="380" y1="160" x2="480" y2="160" stroke="{N}" stroke-width="2"/>
<text x="20" y="150" font-size="14" fill="{N}">rivelatore</text><text x="20" y="190" font-size="14" fill="{N}">(→ SA, flottante)</text>
<text x="410" y="145" font-size="12" fill="#666">uscita nulla</text><text x="410" y="190" font-size="12" fill="#666">con DUT = 50 Ω</text></svg>'''
D.add("Tre accessori, tre usi",'''<div class="grid3">
<div class="card"><h3>Carico con prelievo</h3><p>Un carico fittizio che dissipa la potenza del TX e ha una presa che restituisce una piccola parte del segnale, per esempio −40 dB. Per lo <b>spettro del trasmettitore</b>.</p></div>
<div class="card"><h3>Accoppiatore direzionale</h3><p>Si inserisce tra TX e antenna e separa l'onda <b>diretta</b> da quella <b>riflessa</b>. Per lo spettro in condizioni reali e l'adattamento sotto potenza.</p></div>
<div class="card"><h3>Ponte riflettometrico</h3><p>Un ponte di Wheatstone a 50 Ω, a bassa potenza, usato con il tracking generator. Per il <b>return loss</b> di antenne, filtri e cavi.</p></div></div>
<div class="two" style="margin-top:26px;align-items:start"><div><ul class="small"><li>Tutti e tre servono a portare all'analizzatore un segnale <b>piccolo e sicuro</b>, proporzionale a quello che vuoi misurare.</li></ul></div><div><ul class="small">
<li>La chiave è conoscerne bene il <b>fattore di accoppiamento</b> e i limiti: senza questi i numeri letti sono solo indicativi.</li></ul></div></div>''')
D.add("Il carico con prelievo",f'''<div class="two"><div><ul>
<li>Dentro c'è un resistore di potenza da 50 Ω e una <b>presa</b>: un partitore resistivo, oppure una piccola capacità vicina al conduttore centrale.</li>
<li>Il TX scalda il carico; all'analizzatore arriva il segnale attenuato del fattore di accoppiamento, più eventuali attenuatori.</li>
<li>Controlla <b>potenza e durata</b> ammesse: molti carichi reggono la potenza nominale solo per pochi secondi o minuti (FM, digitale e RTTY sono al 100 % di duty cycle).</li>
<li>L'SWR del carico deve essere buono in tutta la banda, o il TX non lavora nelle condizioni normali.</li></ul></div><div>
<h3>Budget di potenza</h3><table><tr><th>TX</th><th>Prelievo −40 dB</th><th>+ 20 dB attenuatore</th></tr>
<tr><td class="l">10 W (+40 dBm)</td><td>0 dBm</td><td>−20 dBm</td></tr><tr><td class="l">100 W (+50 dBm)</td><td>+10 dBm</td><td>−10 dBm</td></tr><tr><td class="l">1 kW (+60 dBm)</td><td>+20 dBm</td><td>0 dBm</td></tr></table>
<p class="note">Imposta sull'analizzatore un reference offset pari a prelievo + attenuatori: leggerai direttamente la potenza al TX.</p></div></div>''')
D.add("Il prelievo è piatto? Attenzione alle armoniche",f'''<div class="two"><div class="fig">{svg("coupling.svg")}</div><div><ul class="small">
<li>Un prelievo <b>resistivo</b> ha un accoppiamento quasi costante fino a frequenze alte.</li>
<li>Un prelievo <b>capacitivo</b> cresce di circa <b>6 dB per ottava</b>: raddoppiando la frequenza, il segnale prelevato aumenta di 6 dB.</li>
<li>Esempio: fondamentale a 14 MHz con accoppiamento {it(v["cap14"],0)} dB. La 2ª armonica (28 MHz) passa con {it(v["cap28"],0)} dB e la 3ª (42 MHz) con {it(v["cap42"],1)} dB.</li>
<li>Senza correzione, la 2ª armonica appare <b>6 dB più alta</b> del vero e la 3ª circa <b>9,5 dB</b> più alta: un TX in regola sembra fuori norma.</li></ul>
<p class="note">Vale anche al contrario: un prelievo che cala in frequenza fa sembrare le armoniche più basse, ed è il caso più pericoloso.</p></div></div>''')
D.add("Calibrare il prelievo",'''<div class="two"><div><h3>Con un VNA o un tracking generator</h3><ol class="small">
<li>A bassa potenza: sorgente all'ingresso del carico, analizzatore (o porta 2 del VNA) sulla presa.</li>
<li>Misura |S21| dalla fondamentale fino alla 5ª–10ª armonica della banda più alta che usi.</li>
<li>Annota la curva: è il fattore di accoppiamento in funzione della frequenza.</li>
<li>Inseriscila nell'analizzatore come <b>tabella di correzione d'ampiezza</b> (transducer factor), se lo permette, o correggi a mano ogni armonica.</li></ol></div><div>
<h3>Senza strumenti di riferimento</h3><ul class="small"><li>Generatore a livello noto all'ingresso del carico, analizzatore sulla presa: un punto per ogni frequenza d'interesse.</li>
<li>Tieni gli stessi cavi e attenuatori che userai nella misura vera.</li>
<li>Ricontrolla la curva ogni tanto: connettori e resistori di potenza invecchiano.</li></ul>
<div class="warn">La calibrazione si fa a bassa potenza: mai un generatore o un VNA collegati mentre il TX trasmette.</div></div></div>''')
D.add("L'accoppiatore direzionale",f'''<div class="diag" style="width:86%;margin:auto">{coupler}</div><div class="two" style="align-items:start;gap:30px;margin-top:6px"><div>
{eq("isolamento = accoppiamento + direttività")}<ul class="small"><li><b>Accoppiamento</b> (C): quanto della onda diretta esce dalla porta FWD, per esempio −30 dB.</li></ul></div><div><ul class="small">
<li><b>Direttività</b> (D): quanto la porta FWD ignora l'onda riflessa (e viceversa). È il parametro che decide la qualità delle misure di SWR.</li>
<li>Le porte non usate vanno <b>chiuse su 50 Ω</b>: una porta aperta rovina la direttività.</li></ul></div></div>''')
D.add("Misure con l'accoppiatore",'''<div class="two"><div><h3>Spettro "in servizio"</h3><ul class="small">
<li>Con l'accoppiatore tra TX e antenna vedi lo spettro del trasmettitore nelle <b>condizioni reali</b>, con il suo carico vero e il suo SWR.</li>
<li>Porta FWD all'analizzatore (con attenuatori), REF chiusa su 50 Ω.</li></ul>
<h3>Return loss sotto potenza</h3>
<div class="eq">RL = (P<sub>FWD</sub> − C<sub>FWD</sub>) − (P<sub>REF</sub> − C<sub>REF</sub>)</div>
<ul class="small"><li>Misura le due porte in sequenza, chiudendo su 50 Ω quella non collegata. Con accoppiamenti uguali, RL è la semplice differenza in dB.</li></ul></div><div>
<h3>Segnali che arrivano dall'antenna</h3><ul class="small"><li>La porta <b>REF</b> vede anche ciò che entra dall'antenna: stazioni vicine, ripetitori, broadcast.</li>
<li>Utile per misurare quanto segnale "esterno" arriva al finale, e scoprire l'<b>intermodulazione</b> che nasce nel TX quando due trasmettitori sono vicini (siti condivisi, contest multi-stazione).</li></ul>
<p class="note">Con un accoppiatore doppio (dual directional) puoi tenere collegate entrambe le porte a due ingressi o a un commutatore.</p></div></div>''')
D.add("Quanto conta la direttività",'''<div class="two"><div><ul>
<li>La parte di onda diretta che "sfugge" nella porta REF si somma all'onda riflessa con fase qualsiasi: la lettura cade in una <b>fascia</b>.</li>
<li>Regola pratica: misuri con buona precisione return loss fino a circa <b>D − 10 dB</b>.</li></ul>
<table><tr><th>RL vero 20 dB</th><th>Letto tra</th></tr>
<tr><td class="l">direttività 20 dB</td><td>14,0 dB e "infinito"</td></tr>
<tr><td class="l">direttività 30 dB</td><td>17,6 e 23,3 dB</td></tr>
<tr><td class="l">direttività 40 dB</td><td>19,2 e 20,9 dB</td></tr></table></div><div>
<h3>Cosa aspettarsi</h3><ul class="small"><li>Molti accoppiatori e wattmetri passanti per HF hanno direttività tra 20 e 30 dB: ottimi per vedere l'SWR "a grandi linee", poco precisi sotto 1,2:1.</li>
<li>La direttività cala agli estremi della banda: controlla la scheda tecnica.</li>
<li>Cavi e adattatori dopo l'accoppiatore peggiorano la direttività effettiva.</li>
<li>Per misure di adattamento precise, a bassa potenza, usa un ponte o un VNA.</li></ul></div></div>''')
D.add("Il ponte riflettometrico",f'''<div class="two"><div class="diag" style="width:94%">{bridge}</div><div><ul class="small">
<li>Tre resistori da 50 Ω e il DUT formano un <b>ponte di Wheatstone</b>: se il DUT vale 50 Ω il ponte è bilanciato e il rivelatore non vede nulla.</li>
<li>Più il DUT si allontana da 50 Ω, più segnale esce verso l'analizzatore: l'uscita è proporzionale a |Γ|.</li>
<li>Banda larghissima, direttività tipica di 35–45 dB, ma <b>perdite di circa 6 dB</b> per lato e potenza bassa: si usa solo con il tracking generator o un generatore.</li>
<li>Nella pratica si compra o si costruisce già fatto (con un balun o un trasformatore per isolare il rivelatore).</li></ul></div></div>''')
D.add("Misure con ponte e tracking generator",f'''<div class="fig" style="width:90%;margin:-6px auto 0">{svg("ripple.svg")}</div><div class="two" style="align-items:start;gap:30px"><div><ol class="small">
<li>TG → ponte → analizzatore. Porta DUT <b>aperta</b>: normalizza (0 dB). Ripeti con la porta in <b>corto</b> e usa la media delle due: riduce l'errore del ponte.</li>
<li>Collega il DUT: la traccia (rovesciata) è il <b>return loss</b>. SWR = (1 + |Γ|) / (1 − |Γ|).</li>
<li>Verifica con un carico buono da 50 Ω: la lettura è la direttività del sistema.</li></ol></div><div>
{eq("d = VF · c / (2 · Δf)")}<p class="note" style="margin-top:2px">Cavo da 20 m (VF 0,66) chiuso su 100 Ω, con un connettore imperfetto all'inizio: le due riflessioni interferiscono e il return loss ondeggia con periodo Δf ≈ {it(v["ripple"]/1e6)} MHz. Dal periodo ricavi la distanza della discontinuità, come un TDR "dei poveri".</p></div></div>''')
D.add("Test a due toni su un TX SSB",f'''<div class="two"><div class="fig">{svg("twotone.svg")}</div><div><ul class="small">
<li>Carico con prelievo, due toni audio non armonici (per esempio 700 e 1900 Hz) di uguale livello in ingresso microfonico, regolati per la potenza voluta.</li>
<li>RBW stretta (10–30 Hz), span di qualche kHz, rivelatore peak, media o max hold.</li>
<li>Con due toni uguali, ognuno è <b>6 dB sotto la PEP</b>. I prodotti IM3 e IM5 cadono a 2f1 − f2, 2f2 − f1, e così via.</li></ul>
{eq("IMD<sub>PEP</sub> = (tono − IM3) + 6 dB")}
<p class="note">Nell'esempio IM3 a −30 dB dai toni, cioè −36 dB dalla PEP. Ripeti a diversi livelli di potenza: vedi dove il finale inizia a comprimere e se l'ALC peggiora le cose.</p></div></div>''')
D.add("Cosa si può vedere",'''<div class="two"><div><table><tr><th>Fenomeno</th><th>Come lo vedi</th></tr>
<tr><td class="l"><b>Armoniche e spurie</b></td><td class="l">span largo, delta marker in dBc (con correzione del prelievo)</td></tr>
<tr><td class="l"><b>Splatter SSB</b></td><td class="l">max hold mentre parli: la "gonna" del segnale si allarga</td></tr>
<tr><td class="l"><b>Key click in CW</b></td><td class="l">max hold e span di qualche kHz: bande laterali ai fronti</td></tr>
<tr><td class="l"><b>Overshoot dell'ALC</b></td><td class="l">zero span: il picco iniziale del burst</td></tr></table></div><div>
<table><tr><th>Fenomeno</th><th>Come lo vedi</th></tr>
<tr><td class="l"><b>Autooscillazioni</b></td><td class="l">righe strane che cambiano variando il carico (con l'accoppiatore e un'antenna o un accordatore)</td></tr>
<tr><td class="l"><b>Rumore a larga banda</b></td><td class="l">piedistallo attorno alla portante, peggiore a potenza alta</td></tr>
<tr><td class="l"><b>Instabilità del VFO</b></td><td class="l">bande laterali di rumore o righe vicine alla portante</td></tr>
<tr><td class="l"><b>Adattamento sotto potenza</b></td><td class="l">FWD e REF dell'accoppiatore</td></tr></table></div></div>''')
D.add("Errori comuni",'''<div class="two"><div><ul>
<li>Fidarsi del valore nominale del prelievo senza averne misurato l'andamento in frequenza.</li>
<li>Dimenticare l'offset (prelievo + attenuatori) e leggere livelli sbagliati di 40–60 dB.</li>
<li>Lasciare aperta una porta dell'accoppiatore non usata.</li>
<li>Montare l'accoppiatore al contrario: FWD e REF si scambiano.</li></ul></div><div><ul>
<li>Attenuatori dopo il prelievo non dimensionati per i livelli reali (anche +20 dBm scaldano un attenuatore da 0,5 W).</li>
<li>Correnti di modo comune e ground loop tra TX, carico e analizzatore: compaiono righe che non sono del TX. Usa cavi corti e una massa comune.</li>
<li>Misurare il ponte con troppa potenza, o con il TX invece che con il TG.</li>
<li>Scambiare un limite della direttività per un'antenna "perfetta".</li></ul></div></div>''')
rows=[("Carico con prelievo","spettro del TX; calibra il prelievo in frequenza"),("Prelievo capacitivo","+6 dB per ottava: armoniche sovrastimate"),("Accoppiatore direzionale","FWD e REF; porte libere su 50 Ω"),("Return loss sotto potenza","differenza FWD − REF, entro D − 10 dB"),
("Ponte riflettometrico","con TG; normalizza open/short, poi RL"),("Ripple del return loss","d = VF·c / (2·Δf)"),("Test a due toni","IMD rispetto alla PEP = Δ + 6 dB")]
D.add("Riepilogo",'<table class="sum">'+"".join(f'<tr><td class="l" style="width:320px"><b>{a}</b></td><td class="l">{b}</td></tr>' for a,b in rows)+'</table>')
D.render(); pdf("SA_Prelievi_Accoppiatori_Ponti_IV3HGA.pdf")
