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
D.add("Da dove viene",'''<div class="two"><div><ul>
<li>Il progetto nasce come <b>AVR Transistortester</b> di Markus Frejek: un microcontrollore ATmega, qualche resistenza e un display, per capire che transistor si ha in mano e come sono i pin.</li>
<li>Karl-Heinz Kübbeler lo ha poi sviluppato per anni, soprattutto nel software, aggiungendo misure di condensatori, ESR, induttori, zener, autotaratura e molto altro. Il suo manuale descrive in dettaglio ogni metodo di misura.</li>
<li>Pieter-Tjerk de Boer, PA3FWM, ha aggiunto un metodo a campionamento per piccole capacità e induttanze.</li></ul></div><div>
<h3>La famiglia</h3><ul><li>Dal progetto aperto sono nati moltissimi strumenti commerciali economici, con nomi come GM328 o LCR-T4, display diversi e qualche funzione in più.</li>
<li>L'<b>LCR-P1</b> è una versione recente: display a colori, zoccolo rimovibile, batteria ricaricabile, contatti separati per gli zener e decodifica IR.</li></ul>
<p class="note">Il costruttore non pubblica il firmware né il microcontrollore usati: qui si descrive il principio del progetto aperto, comune a tutta la famiglia.</p></div></div>''')
blk=f'''<svg viewBox="0 0 600 300" width="100%">{ARW}
{box(20,30,140,50,"batteria|e USB-C")}{box(20,120,140,50,"regolatore|5 V")}{box(230,90,150,110,"microcontrollore||con ADC")}
{box(450,30,130,50,"display")}{box(450,120,130,50,"rete di|resistenze")}{box(450,210,130,50,"zoccolo|TP1 TP2 TP3",fill="#fde8e3")}
{box(230,230,150,50,"DC-DC per|zener fino a 32 V")}{box(20,230,140,50,"ricevitore IR")}
{ln(90,80,90,120)}{ln(160,145,230,145)}{ln(380,110,450,60)}{ln(380,145,450,145)}{ln(515,170,515,210)}{ln(160,255,230,170)}{ln(305,200,305,230)}</svg>'''
D.add("Lo schema a blocchi",f"""<div class="two"><div>{blk}</div><div><ul class="small">
<li>Il <b>microcontrollore</b> fa tutto: comanda le uscite verso la rete di resistenze, legge le tensioni con l'ADC, misura i tempi con i suoi timer, calcola e mostra il risultato.</li>
<li>La <b>rete di resistenze</b> collega ogni pin di prova al microcontrollore in modo diretto, tramite 680 Ω o tramite 470 kΩ.</li>
<li>Un <b>convertitore DC-DC</b> genera una tensione più alta per misurare gli zener sui contatti dedicati.</li>
<li>Il riferimento di tensione dell'ADC e la precisione delle resistenze determinano l'accuratezza finale.</li></ul></div></div>""")
D.add("Misurare una resistenza",f"""<div class="two"><div class="fig">{svg("rerr.svg")}</div><div><ul class="small">
<li>Il resistore incognito e una resistenza nota formano un <b>partitore</b>: un pin a Vcc tramite la resistenza nota, l'altro a massa. Dalla tensione letta:</li></ul>
{eq("R<sub>x</sub> = R<sub>rif</sub> · V / (V<sub>cc</sub> − V)")}
<ul class="small"><li>Esempio: con 680 Ω e 5 V, l'ADC legge 2,5 V → R<sub>x</sub> = 680 Ω.</li>
<li>Con un ADC a 10 bit un passo vale 5 V / 1024 ≈ 4,9 mV. L'errore è minimo quando R<sub>x</sub> è vicina alla resistenza di riferimento e cresce molto agli estremi.</li>
<li>Per questo il tester usa 680 Ω per le resistenze piccole e 470 kΩ per quelle grandi, e fa la media di molte letture.</li>
<li>Sotto pochi ohm entrano in gioco la resistenza interna dei pin del microcontrollore e quella dei contatti: servono autotaratura e un metodo dedicato.</li></ul></div></div>""")
D.add("Il diodo",'''<div class="two"><div><ul>
<li>Il tester trova un diodo quando una coppia di pin conduce in un verso e non nell'altro.</li>
<li>Misura la tensione diretta con due correnti diverse:</li></ul>
<table><tr><th>Percorso</th><th>Corrente circa</th><th>Che cosa vedi</th></tr><tr><td class="l">via 680 Ω</td><td>(5 − 0,65) / 680 ≈ 6,4 mA</td><td class="l">Vf "di lavoro"</td></tr><tr><td class="l">via 470 kΩ</td><td>(5 − 0,65) / 470 k ≈ 9 µA</td><td class="l">Vf a corrente minima, più bassa</td></tr></table>
<ul class="small"><li>Nel verso inverso misura la <b>capacità di giunzione</b> e la corrente di fuga.</li></ul></div><div>
<h3>Che cosa ci si fa</h3><ul><li>Distinguere un diodo al silicio (0,6–0,7 V), uno Schottky (0,2–0,4 V), un germanio (0,2–0,3 V) e un LED (oltre 1,5 V, e spesso si accende).</li>
<li>Riconoscere un diodo varicap dalla capacità inversa, utile per gli oscillatori.</li>
<li>Trovare i diodi interni dei MOSFET e i diodi di protezione dei transistor.</li></ul>
<p class="note">Un diodo che conduce in entrambi i versi o in nessuno viene segnalato come guasto o come "nessun componente".</p></div></div>''')
D.add("Il transistor bipolare passo per passo",f"""<div class="two"><div><h3>Riconoscimento</h3><ol class="small">
<li>Trova due giunzioni che conducono con un pin in comune: quel pin è la <b>base</b>.</li>
<li>Il verso di conduzione dice se è <b>NPN</b> (la base è l'anodo comune) o <b>PNP</b>.</li>
<li>Prova i due pin rimasti come collettore ed emettitore: il collegamento con il guadagno più alto è quello giusto.</li></ol>
<h3>Esempio di calcolo dell'hFE (NPN)</h3><ul class="small"><li>Base alimentata da 5 V tramite 470 kΩ: Ib ≈ (5 − 0,65) / 470 k ≈ <b>9,3 µA</b>.</li>
<li>Collettore a 5 V tramite 680 Ω: l'ADC misura una caduta di 1,9 V → Ic = 1,9 / 680 ≈ <b>2,8 mA</b>.</li></ul>
{eq("hFE = Ic / Ib ≈ 2,8 mA / 9,3 µA ≈ 300")}</div><div>
<h3>Che cosa mostra</h3><ul class="small"><li>hFE, Ube (tensione base-emettitore), correnti di fuga Iceo e Ices, presenza di un diodo di protezione.</li>
<li>L'hFE è misurato a pochi milliampere: in un finale di potenza a 1 A sarà diverso. Va bene per confrontare e abbinare transistor dello stesso tipo, non come dato di progetto.</li>
<li>I Darlington si riconoscono dall'hFE molto alto e dalla Ube intorno a 1,2 V.</li></ul></div></div>""")
D.add("MOSFET e JFET",'''<div class="grid3"><div class="card"><h3>MOSFET ad arricchimento</h3><p>Il gate non conduce. Il tester carica lentamente il gate tramite 470 kΩ finché tra drain e source inizia a passare corrente: la tensione a quel punto è la <b>soglia Vt</b>.</p></div>
<div class="card"><h3>Capacità di gate</h3><p>Dal tempo di carica del gate ricava la capacità Cg, utile per confrontare MOSFET e capire quanto sarà facile pilotarli.</p></div>
<div class="card"><h3>Diodo interno</h3><p>Tra source e drain c'è il diodo intrinseco: il tester ne misura la Vf e lo usa per capire la polarità (canale N o P).</p></div>
<div class="card"><h3>Rds(on)</h3><p>Con il gate carico misura una resistenza drain-source, ma a correnti di milliampere e con Vgs di pochi volt: per i MOSFET a soglia alta non è il valore del datasheet.</p></div>
<div class="card"><h3>JFET</h3><p>Conduce già senza tensione sul gate; il tester misura la corrente di drain e la capacità di gate, e riconosce canale N o P.</p></div>
<div class="card"><h3>Attenzione</h3><p>I MOSFET sono sensibili alle cariche elettrostatiche: maneggiali per il corpo, e cortocircuita i pin prima di inserirli se il tester li legge in modo strano.</p></div></div>''')
D.add("Zener e tensioni più alte",'''<div class="two"><div><ul>
<li>Dallo zoccolo principale il microcontrollore arriva al massimo alla sua alimentazione: uno zener si vede solo fino a circa 4,5 V.</li>
<li>Per gli zener più alti l'LCR-P1 ha <b>contatti dedicati</b> (K-A-A) alimentati da un convertitore DC-DC, che misurano fino a circa <b>32 V</b>.</li>
<li>La corrente di prova è piccola: la tensione letta è quella "di ginocchio" a bassa corrente, che può essere un po' più bassa del valore nominale a 5 mA del datasheet.</li></ul></div><div>
<h3>Altri usi dei contatti alti</h3><ul><li>Verificare LED bianchi e blu e piccole stringhe di LED.</li>
<li>Controllare la tensione di scarica di un TVS o di un piccolo varistore a bassa tensione.</li></ul>
<p class="note">Il tester non sostituisce un alimentatore regolabile con limitazione di corrente per caratterizzare uno zener: è un controllo rapido.</p></div></div>''')
D.add("L'ESR: come lo stima",f"""<div class="two"><div class="fig">{svg("esrpulse.svg")}</div><div><ul class="small">
<li>Si fa passare nel condensatore un breve impulso di corrente nota, tramite 680 Ω o direttamente dal pin.</li>
<li>All'inizio dell'impulso la tensione salta subito di I·ESR, prima ancora che il condensatore abbia accumulato carica; poi sale lentamente con pendenza I/C. Alla fine dell'impulso ricade dello stesso salto.</li>
<li>Misurando il salto, e conoscendo la corrente, si ricava l'ESR. Nell'esempio: 5 mA e 10 mV di salto → ESR = <b>2 Ω</b>.</li>
<li>Il salto è di pochi millivolt: servono molte misure mediate e un ADC usato al limite. Per questo l'ESR del tester è indicativa e si misura solo su capacità non troppo piccole.</li></ul></div></div>""")
D.add("Da dove vengono gli errori",'''<div class="grid3"><div class="card"><h3>Risoluzione dell'ADC</h3><p>Nel progetto originale l'ADC è a 10 bit: 4,9 mV per passo con riferimento a 5 V. Le misure ai limiti delle portate ne risentono.</p></div>
<div class="card"><h3>Riferimento di tensione</h3><p>Tutte le misure dipendono dal riferimento dell'ADC: se varia dell'1 %, variano dell'1 % i risultati. L'autotaratura ne corregge una parte.</p></div>
<div class="card"><h3>Resistenze di riferimento</h3><p>La tolleranza delle 680 Ω e 470 kΩ entra direttamente nelle misure di R e di C.</p></div>
<div class="card"><h3>Pin del microcontrollore</h3><p>Le uscite hanno una resistenza interna di qualche decina di ohm che cambia con temperatura e corrente: pesa sulle piccole resistenze e sull'ESR.</p></div>
<div class="card"><h3>Contatti e cavi</h3><p>Lo zoccolo e le pinzette aggiungono resistenza e capacità: pochi pF falsano i piccoli condensatori.</p></div>
<div class="card"><h3>Componente stesso</h3><p>Un elettrolitico con dispersione alta, un induttore con nucleo che satura o un ceramico X7R danno letture che dipendono dal metodo di prova.</p></div></div>''')
D.add("HP 4263B: come si usa",'''<div class="two"><div><h3>Impostazioni principali</h3><ul>
<li><b>Frequenza</b>: 100 Hz, 120 Hz, 1 kHz, 10 kHz, 100 kHz.</li>
<li><b>Livello</b>: tensione di prova da 20 mV a 1 Vrms; il monitor mostra tensione e corrente effettive sul componente.</li>
<li><b>Parametro primario e secondario</b>: per esempio Cs e D, Ls e Q, |Z| e θ, R e X.</li>
<li><b>Tempo di misura</b>: corto, medio o lungo, cioè velocità contro rumore.</li></ul></div><div><h3>Prima di misurare</h3><ul>
<li>Dichiara la lunghezza dei cavi (0, 1, 2 o 4 m), che lo strumento corregge.</li>
<li>Esegui le correzioni <b>open e short</b>, ed eventualmente <b>load</b> con un componente di riferimento.</li>
<li>Usa una fixture o le pinze Kelvin: i terminali sono a 4 coppie (Hcur, Hpot, Lpot, Lcur).</li>
<li>Per gli elettrolitici attiva la <b>polarizzazione DC</b> interna, rispettando la polarità.</li></ul>
<p class="note">Con l'opzione per trasformatori misura anche rapporto spire, mutua induttanza e resistenza in continua.</p></div></div>''')
D.add("Sei componenti, due strumenti",'''<table><tr><th>Componente</th><th>Prova componenti</th><th>LCR meter HP</th></tr>
<tr><td class="l">Resistenza 100 Ω</td><td class="l">valore corretto entro pochi percento</td><td class="l">valore allo 0,1 %, e con X si vede se è a filo avvolto</td></tr>
<tr><td class="l">Film 100 nF</td><td class="l">capacità corretta; ESR troppo piccola per essere letta</td><td class="l">Cs e D (circa 0,001), a frequenza scelta</td></tr>
<tr><td class="l">Ceramico X7R 10 µF 0805</td><td class="l">un valore misurato col suo metodo e i suoi volt</td><td class="l">valore a 1 kHz e 1 V; con DC bias si vede la perdita di capacità in esercizio</td></tr>
<tr><td class="l">Elettrolitico 470 µF</td><td class="l">capacità, ESR indicativa, Vloss: ottimo per scovare quelli esauriti</td><td class="l">Cs e ESR a 120 Hz e a 100 kHz, da confrontare col datasheet</td></tr>
<tr><td class="l">Induttore 100 µH su ferrite</td><td class="l">induttanza e resistenza in continua</td><td class="l">Ls e Q a 100 kHz; con DC bias la saturazione</td></tr>
<tr><td class="l">Transistor sconosciuto</td><td class="l">tipo, piedinatura, hFE, Ube</td><td class="l">non è il suo lavoro</td></tr></table>
<p class="note">Descrizioni qualitative: la lettura esatta dipende dal componente e dall'esemplare di strumento.</p>''')
D.add("Un flusso di lavoro in riparazione",'''<div class="two"><div><ol>
<li><b>Ispezione</b>: componenti gonfi, bruciati, saldature rotte.</li>
<li><b>In circuito</b>, a scheda spenta e scarica: un misuratore di ESR in circuito o l'LCR meter a 100 kHz per una prima idea sugli elettrolitici.</li>
<li><b>Fuori dal circuito</b>: il prova componenti per identificare semiconduttori sospetti, controllare piedinature e trovare transistor in corto o aperti.</li>
<li><b>Ricambio</b>: il prova componenti per scegliere tra i pezzi del cassetto, abbinare hFE, verificare la polarità di un MOSFET.</li>
<li><b>Valori critici</b>: l'LCR meter per induttori di filtro, condensatori di temporizzazione, componenti di oscillatori e filtri.</li>
<li><b>RF</b>: il VNA per tutto quello che lavora sopra il centinaio di kHz.</li></ol></div><div>
<p class="note">I due strumenti non sono in competizione: il tester risponde a "che cos'è e funziona?", l'LCR meter a "quanto vale esattamente, a questa frequenza e a questo livello?".</p></div></div>''')
ORDER=["Che cos'è un prova componenti","Da dove viene","Lo schema a blocchi","Dentro: tre pin e un microcontrollore","Come riconosce il componente","Misurare una resistenza","Il diodo","Il transistor bipolare passo per passo","MOSFET e JFET","Zener e tensioni più alte","Come misura i condensatori","L'ESR: come lo stima","Come misura gli induttori","Da dove vengono gli errori","L'altro mondo: un LCR meter HP","HP 4263B: come si usa","Il confronto","Lo stesso condensatore, due letture","Sei componenti, due strumenti","Quale usare, e quando","Un flusso di lavoro in riparazione","Consigli d'uso del tester","Riepilogo"]
_d={t:b for t,b in D.S}; assert set(_d)==set(ORDER), set(_d)^set(ORDER)
D.S=[(t,_d[t]) for t in ORDER]
D.render(); pdf("LCR_2_Prova_componenti_vs_HP_IV3HGA.pdf")
