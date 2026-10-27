import math
from deck import *
D=Deck("Usare bene<br>l'analizzatore di spettro","Proteggerlo da tensione continua, sovraccarichi e spike, e impostare le misure nel modo giusto: livello di riferimento, attenuazione, RBW, rivelatori e marker","L'analizzatore di spettro: uso corretto")
chain=f'''<svg viewBox="0 0 1180 230" font-family="DejaVu Sans">{ARW}
{box(10,60,140,70,"DUT|(TX, circuito)","#fff",15)}{ln(150,95,185,95)}
{box(185,50,190,90,"Attenuatore di|potenza o|campionatore")}{ln(375,95,410,95)}
{box(410,60,140,70,"DC block")}{ln(550,95,585,95)}
{box(585,60,150,70,"Limitatore|(se serve)")}{ln(735,95,770,95)}
{box(770,60,170,70,"Attenuatore|sacrificale 10 dB")}{ln(940,95,975,95)}
{box(975,50,195,90,"Analizzatore|(attenuazione|interna ≥ 10 dB)","#fff",15)}
<g font-size="13" fill="#555"><text x="280" y="170" text-anchor="middle">riduce la potenza</text><text x="280" y="187" text-anchor="middle">a pochi dBm</text>
<text x="480" y="170" text-anchor="middle">blocca la DC</text><text x="660" y="170" text-anchor="middle">taglia gli spike</text>
<text x="855" y="170" text-anchor="middle">si rompe lui</text><text x="855" y="187" text-anchor="middle">al posto del mixer</text></g></svg>'''
D.add("Perché gli analizzatori si rompono",'''<div class="two"><div><ul>
<li>Il primo stadio è un <b>mixer</b> (o un attenuatore elettronico) progettato per pochi milliwatt. Dietro il connettore non c'è nessuna protezione robusta.</li>
<li>Le cause più comuni di guasto:</li></ul><ol class="small">
<li><b>Tensione continua</b> sull'ingresso (bias, alimentazione via cavo, uscite con DC)</li>
<li><b>Sovraccarico</b>: un trasmettitore collegato direttamente o con poca attenuazione</li>
<li><b>Transienti e spike</b>: accensioni, commutazioni, relè, carichi induttivi, linee di alimentazione</li>
<li><b>Scariche statiche</b>: antenne e cavi lunghi caricati dal vento, o le mani</li></ol></div><div>
<h3>Il danno spesso non si vede</h3><ul class="small"><li>Il mixer può non bruciarsi del tutto ma <b>perdere sensibilità</b> o diventare meno lineare: continui a misurare, ma male.</li>
<li>Per questo conviene controllare ogni tanto il livello di un segnale di riferimento noto e il rumore di fondo (vedi l'ultima parte).</li>
<li>Riparare il front-end di un analizzatore costa spesso più di un buon kit di protezioni.</li></ul></div></div>''')
D.add("Leggi l'etichetta dell'ingresso",'''<div class="two"><div><ul>
<li>Vicino al connettore d'ingresso c'è quasi sempre scritto qualcosa come <b>"+30 dBm max, 0 V DC"</b> oppure <b>"+20 dBm, 50 V DC"</b>.</li>
<li><b>0 V DC</b> significa ingresso <b>accoppiato in continua</b>: anche pochi volt possono danneggiare il mixer o l'attenuatore.</li>
<li>Un valore di DC più alto indica un condensatore di blocco interno, ma quel valore è il limite assoluto, non un margine.</li>
<li>La potenza massima vale in genere con l'attenuazione interna inserita: con 0 dB di attenuazione il limite reale è più basso.</li></ul></div><div>
<h3>Regole d'oro</h3><ol class="small"><li>Se non sei sicuro, considera l'ingresso <b>0 V DC</b>.</li>
<li>Calcola sempre la potenza che arriverà all'ingresso <b>prima</b> di collegare.</li>
<li>Usa un margine di almeno 10 dB rispetto al massimo dichiarato.</li>
<li>Non togliere mai l'attenuazione interna "per vedere meglio" senza aver controllato i livelli.</li>
<li>Connettori sempre puliti e mai forzati: anche il connettore d'ingresso si consuma.</li></ol></div></div>''')
D.add("La catena di protezione",f'<div class="diag" style="width:96%">{chain}</div>'+'''<div class="two" style="align-items:start;margin-top:4px"><div><ul class="small">
<li><b>DC block</b>: un condensatore in serie (un componente coassiale apposito). Indispensabile con preamplificatori alimentati via cavo, bias-tee, LNB, uscite di amplificatori.</li>
<li><b>Limitatore</b>: diodi che tagliano gli impulsi oltre un certo livello. Protegge dagli spike, ma è non lineare: può creare armoniche se il segnale si avvicina alla sua soglia.</li></ul></div><div><ul class="small">
<li><b>Attenuatore "sacrificale"</b> da 10 dB fisso sull'ingresso: costa poco, protegge il connettore dall'usura e assorbe parte dei transienti.</li>
<li>Ricorda di sottrarre (o impostare come <i>reference offset</i>) tutte le attenuazioni esterne.</li></ul></div></div>''')
rows=""
for w in (5,50,100,1000):
    dbm=10*math.log10(w*1000); rows+=f'<tr><td class="l">{w} W</td><td>{it(dbm,1)} dBm</td><td>{it(dbm-40,1)} dBm</td><td>{it(dbm-60,1)} dBm</td></tr>'
D.add("Misurare un trasmettitore",f'''<div class="two"><div>
{eq("P(dBm) = 10·log(P / 1 mW)")}
<table><tr><th>TX</th><th>Potenza</th><th>−40 dB</th><th>−60 dB</th></tr>{rows}</table>
<p class="note">Con 100 W e 40 dB di attenuazione arrivano +10 dBm: ancora tanti per molti analizzatori. Con 60 dB, −10 dBm: tranquillo.</p></div><div>
<h3>Due modi sicuri</h3><ul class="small"><li><b>Attenuatore di potenza</b> che regge <b>tutta</b> la potenza del TX (e il suo duty cycle), seguito da altri attenuatori fino al livello giusto.</li>
<li><b>Carico fittizio + campionatore</b> (accoppiatore direzionale o "tap" da −30…−50 dB): il TX scalda il carico, all'analizzatore arriva solo una piccola parte.</li></ul>
<div class="warn">Mai collegare un trasmettitore direttamente all'analizzatore, nemmeno "solo un attimo" o a bassa potenza: un PTT premuto per errore basta.</div>
<p class="note">Controlla anche che campionatore e attenuatori siano piatti fino alle armoniche che vuoi misurare.</p></div></div>''')
D.add("Transienti, spike e scariche statiche",'''<div class="two"><div><h3>Sequenza sicura</h3><ol class="small">
<li>Attenuazione interna al massimo e protezioni esterne collegate.</li>
<li>Accendi il DUT e aspetta che sia stabile.</li>
<li>Solo allora collega il cavo all'analizzatore.</li>
<li>Riduci l'attenuazione gradualmente, guardando i livelli.</li>
<li>Per spegnere, fai il contrario: prima scollega, poi spegni il DUT.</li></ol>
<p class="note">Alimentatori switching, relè, motori e carichi induttivi producono picchi molto più alti del segnale a regime.</p></div><div>
<h3>Antenne, cavi e linee</h3><ul class="small"><li>Prima di collegare un'antenna o un cavo lungo, <b>scaricali</b> cortocircuitando centrale e calza.</li>
<li>Mai misurare su antenne esterne con temporali in arrivo.</li>
<li>Nelle misure di emissioni condotte con LISN usa sempre un <b>limitatore di transienti</b> dedicato: l'accensione dell'apparato sotto test è la causa classica di danni.</li>
<li>Scaricati a terra (o usa un braccialetto antistatico) prima di toccare il connettore d'ingresso.</li></ul></div></div>''')
D.add("Impostare una misura: il metodo",'<div class="flow">'+"".join(f'<div class="card"><b>{i+1}</b><h3>{a}</h3><p>{b}</p></div>' for i,(a,b) in enumerate([("Frequenza","centro e span, o start e stop"),("Livello","reference level e offset esterni"),("Attenuazione","protezione contro dinamica"),("Risoluzione","RBW, VBW, sweep time"),("Lettura","rivelatore, tracce, marker")]))+'''</div>
<div class="two" style="margin-top:28px;align-items:start"><div><ul class="small"><li>Parti sempre <b>largo</b> (span ampio, impostazioni automatiche) per vedere tutto quello che c'è, poi <b>stringi</b> sul segnale che ti interessa.</li>
<li>In automatico lo strumento lega RBW, VBW e sweep time allo span: è un buon punto di partenza.</li></ul></div><div><ul class="small">
<li>Passa al manuale solo quando sai cosa vuoi ottenere: risolvere due segnali, abbassare il rumore, misurare potenza di canale.</li>
<li>Se compare <b>"UNCAL"</b> o un avviso simile, lo sweep è troppo veloce per la RBW scelta: le ampiezze lette sono sbagliate.</li></ul></div></div>''')
D.add("Livello di riferimento, scala e offset",'''<div class="two"><div><ul>
<li>Il <b>reference level</b> è il valore della riga in alto dello schermo. Metti il segnale più forte a 0–10 dB sotto: sopra il riferimento il logaritmico va in saturazione e le letture sono sbagliate.</li>
<li>Scala tipica: <b>10 dB/divisione</b> per vedere tutto, 1–2 dB/div per piccole variazioni (piattezza, ripple).</li>
<li>In molti strumenti il reference level comanda anche l'attenuazione automatica: abbassarlo può togliere attenuazione.</li></ul></div><div>
<h3>Reference offset</h3>
<div class="eq">offset = attenuatori esterni + perdita dei cavi − guadagno di eventuali preamplificatori</div>
<ul class="small"><li>Con 40 dB di campionatore + 0,5 dB di cavo imposti +40,5 dB di offset: lo strumento ti mostra direttamente la potenza al trasmettitore.</li>
<li>Scrivi l'offset sul quaderno delle misure: un offset dimenticato è un errore classico di 20–40 dB.</li></ul></div></div>''')
D.add("RBW, VBW e sweep: cosa scegliere",'''<table><tr><th>Obiettivo</th><th>RBW</th><th>VBW</th><th>Rivelatore e traccia</th></tr>
<tr><td class="l"><b>Cercare segnali</b> su una banda larga</td><td class="l">automatica</td><td class="l">= RBW</td><td class="l">peak, max hold</td></tr>
<tr><td class="l"><b>Separare</b> segnali vicini</td><td class="l">&lt; metà della loro distanza</td><td class="l">= RBW</td><td class="l">peak</td></tr>
<tr><td class="l"><b>Segnali deboli</b> vicino al rumore</td><td class="l">stretta</td><td class="l">RBW/10 o meno</td><td class="l">sample o average</td></tr>
<tr><td class="l"><b>Potenza di canale</b>, segnali digitali</td><td class="l">1–5 % del canale</td><td class="l">≥ 3·RBW</td><td class="l">RMS, average</td></tr>
<tr><td class="l"><b>Disturbi impulsivi</b> e burst</td><td class="l">larga</td><td class="l">larga</td><td class="l">peak, max hold, persistenza</td></tr>
<tr><td class="l"><b>Modulazione</b> nel tempo</td><td class="l">≥ banda del segnale</td><td class="l">larga</td><td class="l">zero span</td></tr></table>
<p class="note" style="margin-top:14px">Ogni volta che stringi la RBW di 10 volte guadagni 10 dB di rumore, ma lo sweep (analogico) diventa circa 100 volte più lento. Restringi prima lo span.</p>''')
D.add("Tracce e marker",'''<div class="two"><div><h3>Tracce</h3><table>
<tr><td class="l"><b>Clear/write</b></td><td class="l">la traccia normale, aggiornata a ogni sweep</td></tr>
<tr><td class="l"><b>Max hold</b></td><td class="l">tiene il massimo: segnali intermittenti, deriva, banda occupata</td></tr>
<tr><td class="l"><b>Min hold</b></td><td class="l">tiene il minimo: segnali continui dentro il rumore</td></tr>
<tr><td class="l"><b>Average</b></td><td class="l">media più sweep: rumore più stabile</td></tr></table></div><div>
<h3>Marker</h3><table>
<tr><td class="l"><b>Peak search</b></td><td class="l">il segnale più alto, poi next peak</td></tr>
<tr><td class="l"><b>Delta marker</b></td><td class="l">differenza in dB e Hz: armoniche in dBc, larghezze di banda</td></tr>
<tr><td class="l"><b>Noise marker</b></td><td class="l">densità di rumore in dBm/Hz, già corretta</td></tr>
<tr><td class="l"><b>Counter</b></td><td class="l">frequenza precisa, indipendente dalla risoluzione dei punti</td></tr></table>
<p class="note">La frequenza letta da un marker normale è precisa quanto il passo tra i punti (span / numero di punti): per la frequenza esatta usa il counter.</p></div></div>''')
D.add("Controllare lo strumento",'''<div class="two"><div><ul>
<li>Accendilo e aspetta che vada in temperatura: ampiezza e frequenza si assestano.</li>
<li>Prima di misure importanti, misura un <b>segnale di riferimento noto</b>: l'uscita di calibrazione interna, se c'è, o un generatore affidabile.</li>
<li>Annota livello e frequenza letti: se tra qualche mese leggi qualche dB in meno, il front-end potrebbe essere danneggiato.</li></ul></div><div><ul>
<li>Guarda anche il <b>rumore di fondo</b> a ingresso chiuso su 50 Ω, con impostazioni fisse: è il secondo indicatore di salute.</li>
<li>Usa la funzione di autocalibrazione interna, se presente, dopo il riscaldamento.</li>
<li>Tieni un tappo da 50 Ω sul connettore quando lo strumento non è in uso.</li></ul></div></div>''')
rows=["Livelli calcolati prima di collegare, con 10 dB di margine","Nessuna tensione continua: DC block dove serve","Attenuatore sacrificale e attenuazione interna ≥ 10 dB","Cavi e antenne scaricati, DUT acceso prima del collegamento","Reference level sopra il segnale più forte, offset esterni impostati","Span, RBW, VBW e rivelatore scelti per l'obiettivo","Nessun avviso UNCAL, segnale di riferimento verificato"]
D.add("Checklist",'<table class="sum">'+"".join(f'<tr><td class="l" style="width:46px;color:#22b8f0;font-weight:800">☐</td><td class="l">{r}</td></tr>' for r in rows)+'</table>')
D.render(); pdf("SA_Uso_Corretto_IV3HGA.pdf")
