from deck import *
O="#e0563b"
D=Deck("Funzioni nascoste<br>e trucchi da esperti","REL, MIN/MAX, peak, hold, bargraph e logging; resistenza interna di batterie e alimentatori, caduta di tensione sotto carico, fusibili in circuito, sonda RF a diodo e altri trucchi da stazione","Il multimetro: funzioni nascoste e trucchi")
probe=f'''<svg viewBox="0 0 760 230" font-family="DejaVu Sans">{ARW}
<circle cx="30" cy="70" r="7" fill="#fff" stroke="{N}" stroke-width="2"/><text x="10" y="45" font-size="13" fill="{N}">punta RF</text>
<path d="M37 70 H100" stroke="{N}" stroke-width="2"/><line x1="100" y1="50" x2="100" y2="90" stroke="{N}" stroke-width="2.5"/><line x1="112" y1="50" x2="112" y2="90" stroke="{N}" stroke-width="2.5"/><text x="80" y="115" font-size="12" fill="#555">1–10 nF</text>
<path d="M112 70 H230" stroke="{N}" stroke-width="2"/><circle cx="230" cy="70" r="4" fill="{N}"/>
<path d="M230 70 V110" stroke="{N}" stroke-width="2"/><polygon points="218,110 242,110 230,130" fill="#fff" stroke="{N}" stroke-width="2"/><line x1="218" y1="132" x2="242" y2="132" stroke="{N}" stroke-width="2.5"/>
<path d="M230 132 V180" stroke="{N}" stroke-width="2"/><text x="250" y="128" font-size="12" fill="#555">diodo Schottky</text><text x="250" y="144" font-size="12" fill="#555">o al germanio</text>
<path d="M230 70 H330" stroke="{N}" stroke-width="2"/><rect x="330" y="58" width="90" height="24" rx="3" fill="#fff" stroke="{N}" stroke-width="2"/><text x="375" y="50" text-anchor="middle" font-size="12" fill="#555">~4,1 MΩ</text>
<path d="M420 70 H520" stroke="{N}" stroke-width="2"/><path d="M470 70 V110" stroke="{N}" stroke-width="2"/><line x1="450" y1="110" x2="490" y2="110" stroke="{N}" stroke-width="2.5"/><line x1="450" y1="122" x2="490" y2="122" stroke="{N}" stroke-width="2.5"/><path d="M470 122 V180" stroke="{N}" stroke-width="2"/><text x="498" y="120" font-size="12" fill="#555">1–10 nF</text>
{box(520,40,200,60,"Multimetro V DC|10 MΩ","#fff",14)}<path d="M20 180 H620 V100" stroke="{N}" stroke-width="2" fill="none"/><text x="20" y="205" font-size="13" fill="#555">massa (clip corta)</text></svg>'''
cards=[("REL / Δ","differenze e confronti"),("MIN / MAX / AVG","picchi e cadute nel tempo"),("Peak 1 ms","eventi rapidissimi"),("Bargraph e hold","tarare e leggere al buio"),("Resistenza interna","batterie e alimentatori"),("Caduta sotto carico","cavi, connettori, fusibili"),("Fusibile in circuito","senza smontarlo"),("Sonda RF","la RF con il multimetro"),("E altri trucchi","rapporti spire, masse, RF in stazione")]
D.add("In questa lezione",'<div class="grid3">'+"".join(f'<div class="card"><h3>{a}</h3><p>{b}</p></div>' for a,b in cards)+'</div>')
D.add("REL (Δ): misure relative",'''<div class="two"><div><ul>
<li>REL memorizza la lettura attuale e da quel momento mostra la <b>differenza</b> rispetto a essa.</li>
<li>Uso classico: azzerare i puntali in Ω o la capacità dei puntali in pF.</li></ul>
<h3>Usi meno ovvi</h3><ul class="small"><li><b>Appaiare componenti</b>: misura una resistenza di riferimento, premi REL, poi misura le altre: leggi direttamente lo scarto. Alcuni modelli lo mostrano in %.</li>
<li><b>Deriva</b>: tensione di un alimentatore appena acceso, premi REL, guarda di quanto si sposta mentre scalda.</li>
<li><b>Variazioni piccole</b> su valori grandi: 13,800 V che diventano 13,794 V si leggono come −6 mV.</li></ul></div><div>
<div class="note">Con REL attivo la portata spesso resta bloccata: se cambi tipo di misura, disattivalo per non leggere differenze senza accorgertene.</div>
<p class="note" style="margin-top:14px">Molti strumenti mostrano il simbolo Δ o REL sul display: controllalo sempre prima di annotare un valore.</p></div></div>''')
D.add("MIN / MAX / AVG",'''<div class="two"><div><ul>
<li>Lo strumento registra il <b>minimo</b>, il <b>massimo</b> e spesso la <b>media</b> di una grandezza nel tempo, finché non lo fermi.</li>
<li>La velocità di cattura è quella normale di misura (decimi di secondo); alcuni modelli hanno una modalità <b>peak</b> da 1 ms o meno.</li></ul>
<h3>In stazione</h3><ul class="small"><li>Puntali ai morsetti del ricetrasmettitore, MIN/MAX attivo, trasmetti in SSB: il <b>minimo</b> è la tensione durante i picchi di voce. Se scende troppo, la radio distorce o si spegne.</li>
<li>Batteria in portatile: tensione minima durante un QSO lungo.</li>
<li>Rete elettrica: buchi di tensione quando parte un elettrodomestico.</li></ul></div><div>
<h3>Altri usi</h3><ul class="small"><li>Temperatura massima di un dissipatore durante una sessione di modi digitali.</li>
<li>Corrente media di un dispositivo che alterna sleep e trasmissione.</li>
<li>Guasti intermittenti: lasci lo strumento collegato per ore e guardi se c'è stato un "buco".</li>
<li>La media di un valore che oscilla è più significativa di una lettura "a occhio".</li></ul></div></div>''')
D.add("Peak, hold, bargraph e logging",'''<div class="two"><div><ul class="small">
<li><b>Peak (1 ms)</b>: cattura i valori di picco istantanei, non efficaci. Utile per spike, corrente di spunto, sovratensioni brevi.</li>
<li><b>Hold</b>: congela il display. <b>AutoHold</b>: congela da solo quando la lettura è stabile, e avvisa con un bip. Perfetto quando i puntali sono in un punto scomodo e non puoi guardare lo strumento.</li>
<li><b>Inrush</b> (sulle pinze): misura la corrente di spunto di motori e alimentatori all'accensione.</li></ul></div><div><ul class="small">
<li><b>Bargraph</b>: veloce, segue le variazioni. Per tarare un nucleo "al massimo" (per esempio la tensione AGC o il livello di un rivelatore) guarda il bargraph, non le cifre.</li>
<li><b>Logging</b> e interfaccia PC (USB, infrarossi, Bluetooth): registri lunghe serie di misure. Curva di scarica di una batteria, stabilità di un alimentatore in una notte.</li>
<li><b>Smoothing</b>: media mobile delle letture, per valori rumorosi.</li></ul>
<p class="note">Non tutti i modelli hanno tutte queste funzioni: vale la pena rileggere il manuale del proprio strumento, spesso nasconde funzioni attivabili tenendo premuto un tasto all'accensione.</p></div></div>''')
D.add("Resistenza interna di batterie e alimentatori",f'''<div class="two"><div class="fig">{svg("rint.svg")}</div><div>
{eq("R<sub>int</sub> = (V<sub>1</sub> − V<sub>2</sub>) / (I<sub>2</sub> − I<sub>1</sub>)")}
<ul class="small"><li>Misura la tensione ai morsetti con due correnti diverse (per esempio ricezione e trasmissione), e le due correnti.</li>
<li>Esempio: 12,60 V a 1 A, 12,20 V a 21 A → R = 0,40 V / 20 A = <b>20 mΩ</b>.</li>
<li>Una batteria che invecchia ha una resistenza interna che cresce: confronta nel tempo con lo stesso metodo.</li>
<li>Vale anche per un alimentatore (regolazione) e per l'insieme alimentatore + cavi: misura ai morsetti della radio.</li></ul></div></div>''')
D.add("Caduta di tensione sotto carico",'''<div class="two"><div><ul>
<li>Il modo migliore per controllare cavi, connettori, interruttori e portafusibili non è misurarli in Ω a vuoto, ma misurare la <b>tensione ai loro capi mentre passa la corrente</b>.</li>
<li>Un connettore "buono" in Ω può avere un contatto che, a 20 A, perde decine di mV e scalda.</li></ul>
<h3>Procedura</h3><ol class="small"><li>Ricetrasmettitore in trasmissione su carico fittizio (corrente alta e costante).</li>
<li>Portata mV, puntali ai due lati di ogni elemento: cavo positivo, cavo negativo, fusibile, connettore.</li>
<li>Somma le cadute: devono spiegare la differenza tra alimentatore e radio.</li></ol></div><div>
<h3>Esempio: 13,8 V all'alimentatore, 12,9 V alla radio a 20 A</h3>
<table><tr><th>Elemento</th><th>Caduta</th></tr><tr><td class="l">cavo positivo</td><td>0,30 V</td></tr><tr><td class="l">cavo negativo</td><td>0,30 V</td></tr><tr><td class="l">portafusibile</td><td>0,15 V</td></tr><tr><td class="l">connettore</td><td>0,15 V</td></tr><tr><td class="l"><b>Totale</b></td><td><b>0,90 V</b></td></tr></table>
<p class="note">Il portafusibile e il connettore "sprecano" quanto un metro di cavo: sono loro da sistemare. Dove c'è caduta c'è anche calore (P = V·I: 0,15 V × 20 A = 3 W).</p></div></div>''')
D.add("Un fusibile in circuito, senza smontarlo",'''<div class="two"><div><ul>
<li>Con il circuito <b>alimentato</b> e il carico collegato, misura la tensione <b>ai capi del fusibile</b>.</li>
<li><b>Circa 0 V</b> (pochi mV): il fusibile è integro.</li>
<li><b>Tutta la tensione di alimentazione</b>: il fusibile è interrotto, perché ai suoi capi si ritrova la differenza tra alimentazione e carico.</li></ul></div><div>
<h3>Attenzione</h3><ul class="small"><li>Funziona solo se il carico è collegato: senza carico anche un fusibile aperto può leggere pochi volt (attraverso l'impedenza del multimetro).</li>
<li>Sulla rete valgono le regole di sicurezza: categoria adatta, una mano sola.</li>
<li>Con la portata mV puoi anche stimare la corrente: un fusibile ha una piccola resistenza, e la caduta cresce con la corrente (solo come indicazione).</li></ul></div></div>''')
D.add("La sonda RF a diodo",f'''<div class="diag" style="width:84%;margin:-6px auto 0">{probe}</div><div class="two" style="align-items:start;gap:30px"><div><ul class="small">
<li>Il diodo raddrizza la RF e il condensatore si carica al <b>valore di picco</b>. La resistenza in serie da circa 4,1 MΩ, con i 10 MΩ del multimetro, fa un partitore da 0,707: lo strumento mostra direttamente il <b>valore efficace</b> di una sinusoide.</li></ul></div><div><ul class="small">
<li>Sotto 1 V circa la caduta del diodo introduce un errore grande: la sonda è una misura relativa, ottima per tarare e confrontare.</li>
<li>Su 50 Ω: P = V<sub>eff</sub>² / 50. Con 7,07 V leggi 1 W.</li>
<li>Con il diodo in parallelo come nello schema la lettura è negativa: conta il valore assoluto (o inverti il diodo).</li><li>Limita la tensione inversa del diodo: mai su uscite di potenza senza attenuatore.</li></ul></div></div>''')
D.add("Altri trucchi da stazione",'''<div class="two"><div><ul class="small">
<li><b>Rapporto spire di un trasformatore</b>: applica una tensione alternata bassa e sicura (da un trasformatorino o un generatore) a un avvolgimento e misura l'altro: N1/N2 = V1/V2.</li>
<li><b>Riconoscere i conduttori di un cavo multipolare</b>: collega in corto due fili all'altro capo e cerca con la continuità quali sono.</li>
<li><b>Ground loop</b>: misura in mV AC tra le masse di due apparati collegati: decine di mV a 50 Hz spiegano il ronzio in audio.</li></ul></div><div><ul class="small">
<li><b>RF in stazione</b>: se le letture del multimetro "saltano" quando trasmetti, c'è RF sui cavi e in casa. È un indizio di correnti di modo comune da curare con choke.</li>
<li><b>Due multimetri insieme</b>: tensione e corrente contemporanee per calcolare potenza e efficienza (lezione sul wattmetro).</li>
<li><b>Tensione AGC o S-meter</b>: un riferimento comodo per tarare filtri e trappole "al massimo".</li>
<li>Annota le letture di un apparato <b>quando funziona</b> (tensioni dei punti di test): in caso di guasto avrai un riferimento.</li></ul></div></div>''')
rows=[("REL","differenze, appaiamento, deriva"),("MIN/MAX","cadute in trasmissione, guasti intermittenti"),("R interna","(V<sub>1</sub> − V<sub>2</sub>)/(I<sub>2</sub> − I<sub>1</sub>)"),("Caduta sotto carico","mV ai capi di cavi e connettori a corrente piena"),
("Fusibile","0 V ai capi = integro; tensione piena = interrotto"),("Sonda RF","picco × 0,707 con 4,1 MΩ in serie")]
D.add("Riepilogo",'<table class="sum">'+"".join(f'<tr><td class="l" style="width:250px"><b>{a}</b></td><td class="l">{b}</td></tr>' for a,b in rows)+'</table>')
D.render(); pdf("MM_Funzioni_Nascoste_Trucchi_IV3HGA.pdf")
