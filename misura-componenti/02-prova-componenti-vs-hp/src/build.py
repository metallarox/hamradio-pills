from deck import *
O="#e0563b"; V="#2a9d5c"; B="#1593d1"
def tx(x,y,t,c=N,fs=14,a="middle",b=""): return f'<text x="{x}" y="{y}" font-size="{fs}" fill="{c}" text-anchor="{a}" {"font-weight=\"bold\"" if b else ""}>{t}</text>'
def wire(x1,y1,x2,y2,c=N,w=2.5): return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{c}" stroke-width="{w}"/>'
def res(x,y,w,t): return f'<rect x="{x}" y="{y-11}" width="{w}" height="22" rx="3" fill="#fff" stroke="{N}" stroke-width="2"/>'+tx(x+w/2,y+5,t,N,12)
D=Deck("Il prova componenti · FNIRSI LCR-P1 e un LCR meter HP","Come fa un tester da 35 euro a riconoscere un transistor e misurare condensatori e induttori con tre soli pin, cosa misura davvero, e in che cosa è diverso da un LCR meter da laboratorio come l'HP 4263B","Misurare i componenti · prova componenti")
D.add("Che cos'è un prova componenti",'''<div class="two"><div><ul>
<li>Strumenti come il <b>FNIRSI LCR-P1</b> hanno uno zoccolo con <b>tre pin</b> numerati: ci infili un componente qualsiasi e premi un tasto.</li>
<li>Lo strumento capisce da solo <b>che cosa</b> è collegato (resistenza, condensatore, induttore, diodo, zener, transistor NPN o PNP, MOSFET, JFET, IGBT, tiristore) e <b>quale pin</b> è quale, e ne mostra i parametri principali.</li>
<li>Questa famiglia di tester nasce dal progetto aperto <b>AVR Transistortester</b> di Markus Frejek, poi sviluppato a lungo da Karl-Heinz Kübbeler: un microcontrollore, poche resistenze e tanto software.</li></ul></div><div>
<h3>LCR-P1 in breve (dati del costruttore)</h3><table><tr><td class="l">Resistenze</td><td class="l">0,01 Ω – 50 MΩ</td></tr><tr><td class="l">Capacità</td><td class="l">25 pF – 100 mF, con ESR e Vloss</td></tr><tr><td class="l">Induttanze</td><td class="l">10 µH – 1000 µH, con resistenza in continua</td></tr><tr><td class="l">Transistor</td><td class="l">hFE 10–600, Ube, correnti di fuga</td></tr><tr><td class="l">Zener</td><td class="l">fino a 4,5 V sullo zoccolo, 32 V sui contatti dedicati</td></tr><tr><td class="l">Altro</td><td class="l">decodifica IR (NEC), batteria ricaricabile, USB-C</td></tr></table>
<p class="note">Prezzo indicativo: circa 35 euro.</p></div></div>''')
def pin(y,n):
    s=""
    for dy,t in [(-30,None),(0,"680 Ω"),(30,"470 kΩ")]:
        s+=tx(20,y+dy+5,"porta",N,12,"start")+wire(62,y+dy,100,y+dy)
        s+=(res(100,y+dy,80,t) if t else wire(100,y+dy,180,y+dy))+wire(180,y+dy,210,y+dy)
    s+=wire(210,y-30,210,y+30)+wire(210,y,300,y)+f'<circle cx="300" cy="{y}" r="9" fill="{O}"/>'+tx(320,y+5,f"TP{n}",O,14,"start",1)
    s+=wire(255,y,255,y+28,B,2)+tx(255,y+42,"ADC",B,12)
    return s
sch=f'''<svg viewBox="0 0 380 370" width="100%">{pin(45,1)}{pin(165,2)}{pin(285,3)}</svg>'''
D.add("Dentro: tre pin e un microcontrollore",f'''<div class="two"><div>{sch}</div><div><ul class="small">
<li>Ogni pin di prova (TP1, TP2, TP3) è collegato al microcontrollore in tre modi: <b>direttamente</b>, tramite <b>680 Ω</b> o tramite <b>470 kΩ</b> (valori del progetto originale). Ogni collegamento può essere messo a Vcc, a massa o lasciato "aperto".</li>
<li>Un <b>convertitore A/D</b> legge la tensione su ciascun pin.</li>
<li>Combinando queste possibilità il software fa scorrere correnti piccole o grandi nei due versi tra qualsiasi coppia di pin, e misura le tensioni.</li>
<li>Non c'è un oscillatore sinusoidale: tutte le misure sono fatte <b>in continua</b>, con <b>impulsi</b> e <b>tempi di carica</b>.</li></ul></div></div>''')
D.add("Come riconosce il componente",'''<div class="two"><div><table><tr><th>Che cosa vede tra i pin</th><th>Conclusione</th></tr>
<tr><td class="l">Conduce uguale nei due versi, senza transitori</td><td class="l">resistenza</td></tr>
<tr><td class="l">Si carica: la tensione sale col tempo</td><td class="l">condensatore</td></tr>
<tr><td class="l">La corrente cresce col tempo, poi resistenza bassa</td><td class="l">induttore</td></tr>
<tr><td class="l">Conduce in un solo verso, con circa 0,3–0,7 V</td><td class="l">diodo</td></tr>
<tr><td class="l">Due giunzioni con un pin in comune; il terzo pin pilota la corrente</td><td class="l">transistor bipolare (NPN o PNP dal verso)</td></tr>
<tr><td class="l">Il passaggio tra due pin si apre caricando il terzo</td><td class="l">MOSFET o JFET</td></tr>
<tr><td class="l">Resta in conduzione dopo l'impulso sul gate</td><td class="l">tiristore</td></tr></table></div><div><ul>
<li>Il tester prova tutte le <b>sei combinazioni</b> di pin e versi, e per i componenti a tre terminali anche il pilotaggio del terzo pin.</li>
<li>Poi misura i parametri: per un bipolare l'<b>hFE</b> (corrente di base fornita tramite 470 kΩ e corrente di collettore misurata), la tensione base-emettitore, le correnti di fuga; per un MOSFET la soglia, la capacità di gate e il diodo interno.</li>
<li>Tutto con tensioni di pochi volt e correnti di pochi milliampere: va benissimo per identificare i componenti, meno per caratterizzarli in condizioni di lavoro.</li></ul></div></div>''')
D.add("Come misura i condensatori",f'''<div class="two"><div class="fig">{svg("charge.svg")}</div><div><ul class="small">
<li>Il condensatore viene scaricato e poi caricato attraverso una resistenza nota. Misurando il <b>tempo</b> che la tensione impiega a salire si ricava C dalla costante di tempo τ = R·C.</li>
<li>Capacità piccole: si carica con 470 kΩ per avere tempi misurabili (100 nF: 47 ms). Capacità grandi: con 680 Ω, o con brevi impulsi a corrente piena, contando quanti ne servono.</li>
<li>La caduta di tensione all'inizio dell'impulso, prima che il condensatore si carichi, dà una stima dell'<b>ESR</b>; la tensione persa dopo la carica dà la <b>Vloss</b>, indice della dispersione.</li>
<li>Sotto qualche decina di picofarad i tempi diventano troppo brevi: da qui il limite di 25 pF.</li></ul></div></div>''')
D.add("Come misura gli induttori",f'''<div class="two"><div class="fig">{svg("lrise.svg")}</div><div><ul class="small">
<li>Un induttore collegato a una tensione attraverso una resistenza fa crescere la corrente con costante di tempo τ = L/R. Il tester misura il tempo di salita e ricava L.</li>
<li>Con circa 680 Ω, 1 mH dà τ ≈ 1,5 µs: si misura bene. 10 µH dà τ ≈ 15 ns, meno di un ciclo di clock del microcontrollore: la misura diventa impossibile. È il motivo del limite inferiore di 10 µH.</li>
<li>Prima misura la resistenza in continua dell'avvolgimento, che entra nel calcolo.</li>
<li>Non c'è una frequenza di prova e quindi non c'è un <b>Q</b> alla frequenza di lavoro: per un induttore RF serve un LCR meter o il VNA.</li></ul></div></div>''')
D.add("L'altro mondo: un LCR meter HP",'''<div class="two"><div><h3>HP / Agilent / Keysight 4263B</h3><ul>
<li>Frequenze di prova <b>100 Hz, 120 Hz, 1 kHz, 10 kHz, 100 kHz</b> (20 kHz in opzione).</li>
<li>Livello AC regolabile da <b>20 mV a 1 Vrms</b>, a passi di 5 mV, con monitor di tensione e corrente effettive.</li>
<li>Accuratezza di base <b>0,1 %</b>; 11 parametri: |Z|, |Y|, θ, R, X, G, B, L, C, D, Q.</li>
<li>Polarizzazione DC interna, correzioni open, short e load, connessioni a 4 terminali per cavi e fixture.</li></ul></div><div>
<h3>Più in alto in frequenza</h3><ul><li>Lo stesso principio vettoriale arriva più in alto con strumenti come l'HP/Agilent <b>4285A</b> (da 75 kHz a 30 MHz), adatto a componenti per l'RF.</li>
<li>Oltre, si passa agli analizzatori di impedenza e al VNA.</li></ul>
<p class="note">Un 4263B usato costa oggi qualche migliaio di euro: quasi cento volte un tester. Le due cose rispondono a domande diverse.</p></div></div>''')
rows=[("Principio","tempi di carica e impulsi in continua","rapporto vettoriale V/I in AC sinusoidale"),("Frequenza di prova","nessuna dichiarata","100 Hz – 100 kHz, a scelta"),("Livello di prova","pochi volt, fisso","20 mV – 1 Vrms, regolabile, DC bias"),("Parametri","valore, ESR, Vloss, DCR","|Z|, θ, R, X, L, C, D, Q, serie o parallelo"),("Accuratezza","indicativa, qualche percento","0,1 % di base"),("Collegamenti","zoccolo o pinzette, a 2 fili","4 terminali, fixture, compensazioni"),("Componenti attivi","sì: riconosce e misura","no"),("Prezzo","circa 35 euro","qualche migliaio di euro, usato")]
D.add("Il confronto",'<table><tr><th></th><th>FNIRSI LCR-P1</th><th>LCR meter HP 4263B</th></tr>'+"".join(f'<tr><td class="l"><b>{a}</b></td><td class="l">{b}</td><td class="l">{c}</td></tr>' for a,b,c in rows)+'</table>')
D.add("Lo stesso condensatore, due letture",f'''<div class="two"><div class="fig">{svg("esrf.svg")}</div><div><ul class="small">
<li>L'ESR di un elettrolitico <b>dipende dalla frequenza</b>: alle basse frequenze pesano le perdite del dielettrico, alle alte resta la resistenza di elettrolita e terminali.</li>
<li>Nell'esempio (470 µF, modello semplificato) l'HP legge circa 108 mΩ a 100 Hz, 47 mΩ a 1 kHz, 40 mΩ a 100 kHz: tre numeri tutti giusti.</li>
<li>Il tester dà <b>un solo</b> numero, ottenuto con il suo impulso: va benissimo per scoprire un condensatore con l'ESR salito di dieci volte, non per confrontarlo con la riga "ESR a 100 kHz" del datasheet.</li>
<li>Lo stesso vale per i ceramici X7R (il tester li carica con qualche volt, l'HP misura a 1 Vrms senza bias) e per gli induttori con nucleo.</li></ul></div></div>''')
D.add("Quale usare, e quando",'''<div class="two"><div><h3>Il prova componenti</h3><ul>
<li>Riconoscere un componente sconosciuto e la sua <b>piedinatura</b>.</li><li>Controllare transistor e MOSFET recuperati, abbinare coppie per hFE.</li>
<li>Selezionare velocemente resistenze e condensatori dai cassetti.</li><li>Trovare elettrolitici con ESR alta durante una riparazione.</li></ul></div><div><h3>L'LCR meter</h3><ul>
<li>Misurare un valore con precisione e alla <b>frequenza</b> che interessa.</li><li>Q degli induttori, D e ESR dei condensatori da confrontare con i datasheet.</li>
<li>Componenti in condizioni d'uso: livello AC e polarizzazione DC.</li><li>Abbinare componenti per filtri e reti di precisione.</li></ul>
<p class="note">Per il comportamento in RF (autorisonanza, Q a 14 MHz, impedenza di una ferrite) lo strumento giusto è il VNA, capitolo 4.</p></div></div>''')
D.add("Consigli d'uso del tester",'''<div class="grid3"><div class="card"><h3>Scarica i condensatori</h3><p>Un elettrolitico carico può danneggiare gli ingressi. La protezione aiuta, ma la regola resta: scarica sempre prima di inserire.</p></div>
<div class="card"><h3>Fuori dal circuito</h3><p>In circuito le altre parti si mettono in parallelo e falsano tutto, e i semiconduttori vicini confondono il riconoscimento.</p></div>
<div class="card"><h3>Autotaratura</h3><p>Fai il self test con i tre pin in cortocircuito, come indica il manuale: corregge resistenza dei contatti e capacità a vuoto.</p></div>
<div class="card"><h3>Fili corti</h3><p>Le pinzette aggiungono resistenza e capacità: per piccole resistenze e piccole capacità usa lo zoccolo.</p></div>
<div class="card"><h3>Ai limiti</h3><p>Sotto 25 pF, sotto 10 µH o sopra 1 mH, e con zener oltre la tensione dei contatti, il risultato non è affidabile o non c'è.</p></div>
<div class="card"><h3>Leggi come una prova</h3><p>Il tester dice che cosa è e se funziona. Se il valore è critico, misuralo con l'LCR meter.</p></div></div>''')
r=[("Tester","3 pin, microcontrollore, resistenze 680 Ω e 470 kΩ"),("Riconosce","R, C, L, diodi, zener, BJT, FET, IGBT, tiristori"),("Misura","in continua: tempi di carica, impulsi, salita di corrente"),("Limiti","nessuna frequenza di prova, livello fisso, qualche %"),("HP 4263B","100 Hz–100 kHz, 20 mV–1 V, 0,1 %, 4 terminali"),("Scelta","tester per identificare, LCR meter per misurare, VNA per l'RF")]
D.add("Riepilogo",'<table class="sum">'+"".join(f'<tr><td class="l" style="width:160px"><b>{a}</b></td><td class="l">{b}</td></tr>' for a,b in r)+'</table>')
D.render(); pdf("LCR_2_Prova_componenti_vs_HP_IV3HGA.pdf")
