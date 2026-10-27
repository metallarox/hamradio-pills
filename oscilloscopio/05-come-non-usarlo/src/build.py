from deck import *
D=Deck("Come NON usare<br>l'oscilloscopio","Gli errori più comuni, perché ingannano e come evitarli: aliasing, banda, sonde, masse, accoppiamento AC, 50 Ω, autoset e misure automatiche","L'oscilloscopio: come non usarlo")
cards=[("Fidarsi dell'immagine","aliasing e sample rate basso"),("Banda troppo stretta","il quadrato diventa un seno"),("Fattore sonda sbagliato","tensioni ×10 o ÷10"),
("Massa nel punto sbagliato","cortocircuiti e disturbi"),("Due masse su punti diversi","un corto attraverso lo strumento"),("AC dove serve DC","livelli spariti, fianchi inclinati"),
("1 MΩ al posto di 50 Ω","ampiezze doppie e riflessioni"),("Autoset e misure cieche","numeri assurdi su tracce sbagliate"),("Strumento sbagliato","voltmetro, frequenzimetro, analizzatore")]
D.add("Nove modi di sbagliare",'<div class="grid3">'+"".join(f'<div class="card"><h3>{a}</h3><p>{b}</p></div>' for a,b in cards)+'</div>')
D.add("1–2 · Immagine ingannevole e banda stretta",'''<div class="two"><div><h3>L'immagine "bella" ma falsa</h3><ul class="small">
<li>Con una base dei tempi lunga il sample rate scende: un segnale veloce può diventare un <b>alias</b> lento e stabile.</li>
<li>Gli impulsi brevi cadono tra due campioni e spariscono.</li>
<li><b>Invece</b>: guarda il sample rate sullo schermo, cambia la base dei tempi per verificare, usa peak detect per cercare glitch.</li></ul></div><div>
<h3>La banda che manca</h3><ul class="small"><li>Con poca banda un'onda quadra veloce sembra una sinusoide e i fronti sembrano lenti: misuri lo strumento, non il circuito.</li>
<li>La sonda 1× ha pochi MHz di banda anche su un oscilloscopio da 200 MHz.</li>
<li>Il limite di banda a 20 MHz dimenticato acceso fa lo stesso effetto.</li>
<li><b>Invece</b>: banda 3–5 volte il segnale, sonda 10×, limite di banda solo quando serve.</li></ul></div></div>''')
D.add("3 · Il fattore della sonda",'''<div class="two"><div><ul>
<li>Se lo strumento crede di avere una sonda 1× e la sonda è 10×, <b>tutte le tensioni sono 10 volte più basse</b> del vero; nel caso opposto, 10 volte più alte.</li>
<li>Molte sonde hanno un commutatore 1×/10× sul corpo: basta spostarlo per sbaglio.</li>
<li>Alcune sonde vengono riconosciute automaticamente, molte no.</li></ul></div><div>
<h3>Invece</h3><ul class="small"><li>Controlla l'indicazione del fattore sonda sullo schermo ogni volta che colleghi una sonda.</li>
<li>Verifica con l'uscita di calibrazione (di solito qualche volt picco-picco noto) prima di misurare.</li>
<li>Compensa la sonda sul canale dove la usi: una sonda presa da un altro strumento è quasi sempre scompensata.</li>
<li>Etichetta sonde e cavi: banda, fattore, strumento di appartenenza.</li></ul></div></div>''')
D.add("4–5 · Le masse",'''<div class="two"><div><h3>Massa nel punto sbagliato</h3><ul class="small">
<li>La clip di massa è la terra: collegata a un nodo che non è a potenziale di terra crea un cortocircuito (lezione sulla sicurezza).</li>
<li>Un cavetto di massa lungo raccoglie disturbi e crea oscillazioni finte sui fronti.</li></ul>
<h3>Due masse su punti diversi</h3><ul class="small"><li>Le masse di tutti i canali sono <b>lo stesso nodo</b> dentro lo strumento.</li>
<li>Collegare la massa del CH1 a un punto e quella del CH2 a un altro <b>cortocircuita</b> quei due punti attraverso l'oscilloscopio: per esempio la resistenza di shunt che volevi misurare, o due masse "separate" di un circuito.</li></ul></div><div>
<h3>Invece</h3><ul class="small"><li>Una sola massa di riferimento, la più vicina possibile al punto misurato, con la molla corta.</li>
<li>Per misurare tra due punti nessuno dei quali è a massa: sonda differenziale, o A − B con due canali (con i limiti visti nella lezione sui trucchi).</li>
<li>Ground loop tra strumenti (generatore, alimentatore, oscilloscopio) creano ronzii a 50 Hz: riduci i collegamenti di massa multipli, usa alimentazioni isolate dove possibile. Mai togliendo la terra di sicurezza.</li></ul></div></div>''')
D.add("6 · L'accoppiamento AC dove serve il DC",f'''<div class="fig" style="width:92%">{svg("tilt.svg")}</div><div class="two" style="align-items:start;gap:30px"><div><ul class="small">
<li>L'accoppiamento AC è un <b>passa-alto</b> (un condensatore in serie, taglio a pochi Hz): toglie la continua, ma deforma i segnali lenti.</li>
<li>Un'onda quadra a bassa frequenza diventa "inclinata"; un segnale logico perde il suo livello di riferimento.</li></ul></div><div><ul class="small">
<li>Il livello medio della traccia dipende dal duty cycle: un segnale 0–5 V appare centrato sullo zero.</li>
<li><b>Invece</b>: usa DC come default; l'AC solo per guardare piccole variazioni sopra una continua (come il ripple), sapendo cosa toglie.</li></ul></div></div>''')
D.add("7 · 1 MΩ al posto di 50 Ω",'''<div class="two"><div><ul>
<li>Un generatore con uscita a 50 Ω è tarato per un carico da 50 Ω. Se lo colleghi a un ingresso da 1 MΩ, vedi un'ampiezza <b>doppia</b> di quella impostata.</li>
<li>Un cavo coassiale lungo chiuso su 1 MΩ è una linea aperta: a frequenze alte compaiono <b>riflessioni</b> e onde stazionarie, e l'ampiezza cambia con la frequenza.</li></ul></div><div>
<h3>Invece</h3><ul class="small"><li>Segnali da sorgenti a 50 Ω (generatori, uscite RF, prelievi) su <b>ingresso a 50 Ω</b>, o su 1 MΩ con una <b>terminazione passante</b> da 50 Ω sul BNC.</li>
<li>Ricorda i limiti di potenza del 50 Ω (circa mezzo watt).</li>
<li>Con le sonde 10× usa sempre l'ingresso a 1 MΩ: a 50 Ω la sonda non funziona come previsto.</li></ul></div></div>''')
D.add("8 · Autoset e misure automatiche alla cieca",'''<div class="two"><div><ul>
<li>L'autoset sceglie da solo scale, trigger e spesso l'accoppiamento: su segnali complessi o con più componenti sceglie male.</li>
<li>Se la traccia esce dallo schermo in verticale, l'ADC satura: Vpp, Vrms e tempi diventano falsi, anche se compaiono come numeri precisi.</li>
<li>La media (average) e l'high resolution nascondono rumore e glitch: il segnale sembra più pulito di quanto sia.</li></ul></div><div>
<h3>Invece</h3><ul class="small"><li>Autoset solo per trovare il segnale, poi imposta a mano.</li>
<li>Traccia sempre tutta dentro lo schermo, con margine.</li>
<li>Guarda le statistiche delle misure: una deviazione grande indica una misura instabile.</li>
<li>Prima di salvare una misura importante, controlla: media, limite di banda, offset, fattore sonda.</li></ul></div></div>''')
D.add("9 · Lo strumento sbagliato",'''<table><tr><th>Se vuoi…</th><th>L'oscilloscopio…</th><th>Usa invece</th></tr>
<tr><td class="l">una tensione continua precisa</td><td class="l">ha qualche % di precisione</td><td class="l">un multimetro</td></tr>
<tr><td class="l">una frequenza precisa</td><td class="l">dipende dalla sua base dei tempi</td><td class="l">un frequenzimetro con buon riferimento</td></tr>
<tr><td class="l">armoniche a −60 dBc</td><td class="l">con 8 bit ha 50–60 dB di dinamica in FFT</td><td class="l">un analizzatore di spettro</td></tr>
<tr><td class="l">la potenza di un TX</td><td class="l">rischia di bruciarsi e misura male</td><td class="l">un wattmetro (con carico)</td></tr>
<tr><td class="l">l'SWR di un'antenna</td><td class="l">non separa onda diretta e riflessa</td><td class="l">un VNA o un wattmetro direzionale</td></tr></table>
<p class="note" style="margin-top:14px">L'oscilloscopio è insuperabile per vedere la <b>forma</b> e il <b>tempo</b> dei segnali. Per il resto, è un buon secondo parere.</p>''')
rows=[("Non fidarti dell'immagine","controlla sample rate e base dei tempi"),("Non usare il 1×","sonda 10× compensata"),("Non dimenticare il fattore sonda","verifica con il segnale di calibrazione"),
("Non mettere masse a caso","una massa, corta, a potenziale di terra"),("Non usare AC per i livelli","DC di default"),("Non chiudere su 1 MΩ le sorgenti a 50 Ω","ingresso 50 Ω o terminazione"),("Non fidarti dei numeri","verifica con i cursori")]
D.add("Riepilogo: non fare / fai invece",'<table class="sum">'+"".join(f'<tr><td class="l" style="width:420px"><b>{a}</b></td><td class="l">{b}</td></tr>' for a,b in rows)+'</table>')
D.render(); pdf("OSC_Come_Non_Usarlo_IV3HGA.pdf")
