from deck import *
D=Deck("Misure inconsuete<br>e trucchi","Il ripple dei condensatori di filtro in accoppiamento AC, misure differenziali, corrente di spunto, prova componenti in XY, TDR con l'oscilloscopio, burst e PTT, inviluppo CW e altri trucchi da banco","L'oscilloscopio: misure inconsuete e trucchi")
cards=[("Ripple in AC","condensatori di filtro e alimentatori"),("ESR e invecchiamento","il ripple che cresce"),("A − B","misure differenziali con due canali"),("Corrente di spunto","shunt e trigger single"),
("Prova componenti XY","diodi, zener, condensatori in circuito"),("TDR","lunghezza e guasti dei cavi"),("PTT e burst","tempi di salita della potenza"),("Inviluppo CW","key click sotto controllo"),("Altri trucchi","line trigger, sonda-spira, persistenza")]
D.add("Cosa c'è in questa lezione",'<div class="grid3">'+"".join(f'<div class="card"><h3>{a}</h3><p>{b}</p></div>' for a,b in cards)+'</div>')
D.add("Il ripple dei condensatori di filtro",f'''<div class="fig" style="width:96%">{svg("ripple.svg")}</div><div class="two" style="align-items:start;gap:30px"><div><ul class="small">
<li>In <b>DC</b> a 5 V/div l'uscita del filtro sembra una linea piatta: 1 V di ripple è un quinto di divisione.</li>
<li>In <b>AC</b> lo strumento toglie la continua e puoi scendere a 200 mV/div o meno: il ripple occupa tutto lo schermo.</li></ul></div><div><ul class="small">
<li>Raddrizzatore a doppia semionda: ripple a <b>100 Hz</b> (due volte la rete), a dente di sega: carica rapida sui picchi e scarica lineare con la corrente del carico.</li>
<li>Nell'esempio: 1 A su 10 000 µF → circa 1 V picco-picco (formula alla slide successiva).</li></ul></div></div>''')
D.add("Ripple: come misurarlo bene e cosa dice",'''<div class="two"><div><h3>Procedura</h3><ol class="small">
<li>Sonda sui capi del <b>condensatore</b>, con la <b>molla di massa</b> sul suo negativo (non il cavetto lungo).</li>
<li>Accoppiamento <b>AC</b>, V/div fino a vedere bene il ripple, <b>limite di banda 20 MHz</b> (è la convenzione per le misure di ripple).</li>
<li>Trigger <b>line</b> (sincronizzato con la rete) per alimentatori lineari, sul canale per gli switching.</li>
<li>Misura picco-picco con cursori o misura automatica; per i segnali molto piccoli sonda 1×.</li></ol>
<div class="warn">Sul lato rete degli alimentatori valgono tutte le regole di sicurezza: misura solo sul secondario, o con una sonda differenziale.</div></div><div>
<div class="eq">ΔV ≈ I / (f<sub>ripple</sub> · C) + I · ESR</div>
<ul class="small"><li>Esempio: 1 A, 100 Hz, 10 000 µF → 1 / (100 · 0,01) = <b>1 V</b>.</li>
<li>Un condensatore elettrolitico che <b>invecchia</b> perde capacità e aumenta l'ESR: il ripple cresce. Confronta con un apparato sano o con il valore di progetto.</li>
<li>Negli switching il ripple è a decine o centinaia di kHz, con <b>spike</b> sui fronti dovuti all'ESL: misurali con la molla corta, altrimenti misuri il cavetto.</li>
<li>Dopo un regolatore lineare il ripple deve scendere a pochi mV: se no, il regolatore lavora troppo vicino alla tensione d'ingresso (dropout).</li></ul></div></div>''')
D.add("Misure differenziali con due canali (A − B)",'''<div class="two"><div><ul>
<li>Sonda A su un punto, sonda B sull'altro, masse entrambe a terra; funzione <b>math A − B</b> (o inversione di B e somma).</li>
<li>Ottieni la tensione tra due punti <b>nessuno dei quali è a massa</b>: per esempio una resistenza di sensing sul lato positivo, o un segnale bilanciato.</li></ul></div><div>
<h3>I limiti</h3><ul class="small"><li>Funziona solo se la tensione rispetto a terra (modo comune) è <b>bassa</b> ed entro i limiti degli ingressi: <b>mai</b> sulla rete o sul primario di uno switching.</li>
<li>Entrambi i canali devono restare dentro lo schermo: niente saturazione.</li>
<li>Le due sonde devono essere uguali e compensate: piccole differenze di guadagno trasformano il modo comune in un errore (reiezione di modo comune scarsa).</li>
<li>Per misure serie o ad alta tensione: sonda differenziale.</li></ul></div></div>''')
D.add("Corrente di spunto all'accensione",'''<div class="two"><div><ul>
<li>Una resistenza di shunt piccola (per esempio 0,1 Ω) sul <b>negativo</b> dell'alimentazione del carico, sonda sui suoi capi: I = V / R.</li>
<li>Trigger <b>single</b>, sul fronte di salita, livello appena sopra lo zero; base dei tempi di qualche ms.</li>
<li>Accendi: lo strumento cattura il picco di corrente che carica i condensatori dell'apparato.</li></ul></div><div>
<h3>Perché è utile</h3><ul class="small"><li>Dimensionare fusibili e alimentatori: un ricetrasmettitore da 20 A di regime può chiedere picchi molto più alti all'accensione.</li>
<li>Capire perché un alimentatore va in protezione quando accendi l'apparato.</li>
<li>Verificare un circuito di soft-start o un NTC limitatore.</li>
<li>Con una sonda di corrente a effetto Hall non serve interrompere il circuito.</li></ul></div></div>''')
D.add("Prova componenti in modalità XY",f'''<div class="fig" style="width:96%">{svg("xy.svg")}</div><div class="two" style="align-items:start;gap:30px"><div><ul class="small">
<li>Una tensione alternata di pochi volt (da un trasformatore a bassa tensione, mai la rete diretta) alimenta il componente attraverso una resistenza in serie (per esempio 1 kΩ).</li>
<li>Asse X: tensione sul componente. Asse Y: tensione sulla resistenza, cioè la corrente.</li></ul></div><div><ul class="small">
<li>Ogni componente disegna la sua "firma": linea inclinata (resistenza), ellisse (condensatore o induttanza), ginocchio (diodo), due ginocchi (zener).</li>
<li>Trucco da riparatore: confronta la firma di un punto su una scheda buona e su una guasta, a circuito spento.</li>
<li>Attenzione alle masse: le due tensioni devono avere un riferimento comune, o usa A − B.</li></ul></div></div>''')
D.add("TDR con l'oscilloscopio",f'''<div class="two"><div class="fig">{svg("tdr.svg")}</div><div><ul class="small">
<li>Un generatore di onda quadra con fronti veloci (pochi ns) e uscita a 50 Ω, un raccordo a T sull'ingresso dell'oscilloscopio (1 MΩ) e il cavo da provare sull'altra uscita del T.</li>
<li>Il fronte parte a metà ampiezza; dopo il tempo di andata e ritorno torna la riflessione: <b>sale</b> se il cavo è aperto, <b>scende</b> se è in corto, resta piatto se è chiuso su 50 Ω.</li></ul>
{eq("d = VF · c · t / 2")}
<ul class="small"><li>Esempio: 10 m con VF 0,66 → circa 101 ns di andata e ritorno.</li>
<li>Con una lunghezza nota misuri il VF; con il VF noto trovi la distanza di un guasto o di un connettore difettoso.</li>
<li>La risoluzione dipende dai fronti: con 5 ns di salita, circa mezzo metro.</li></ul></div></div>''')
D.add("PTT, burst e inviluppo CW",'''<div class="two"><div><h3>Tempo di salita della potenza al PTT</h3><ul class="small">
<li>CH1 sulla linea PTT (o sul tasto), CH2 sull'inviluppo RF: un rivelatore a diodo su un prelievo, o la RF attenuata se la banda basta.</li>
<li>Trigger sul fronte del PTT: misuri il ritardo e il tempo con cui il TX arriva a piena potenza, eventuali overshoot dell'ALC.</li>
<li>Utile per i modi digitali e per i ponti radio, dove i primi millisecondi si perdono.</li>
<li>Con i segnali TDMA (DMR, TETRA) la <b>memoria segmentata</b> salva solo i burst, con il loro istante: vedi decine di burst senza sprecare memoria.</li></ul></div><div>
<h3>Inviluppo della manipolazione CW</h3><ul class="small"><li>Fronti di salita e discesa troppo ripidi allargano lo spettro: sono i <b>key click</b> che disturbano chi ascolta vicino.</li>
<li>Guarda l'inviluppo RF mentre manipoli: fronti arrotondati di qualche millisecondo sono il comportamento corretto.</li>
<li>Fronti quasi verticali o overshoot sono un campanello d'allarme: controllali poi con l'analizzatore di spettro.</li></ul></div></div>''')
D.add("Altri trucchi da banco",'''<div class="two"><div><ul class="small">
<li><b>Trigger line</b>: sincronizza con la rete. Se un disturbo resta fermo sullo schermo, è legato ai 50 Hz (ronzio, raddrizzatori, ground loop).</li>
<li><b>Sonda come spira</b>: aggancia la clip di massa alla punta e ottieni una piccola sonda magnetica di campo vicino, per cercare da dove irradia uno switching.</li>
<li><b>Persistenza</b> o modo envelope: jitter, intermittenze, forme d'onda che cambiano nel tempo.</li>
<li><b>Trigger a larghezza d'impulso</b> per catturare il glitch raro che resetta un microcontrollore.</li></ul></div><div><ul class="small">
<li><b>Forme d'onda di riferimento</b>: salva la traccia di un apparato sano e confrontala con quella del guasto.</li>
<li><b>Funzioni math</b>: integrale della potenza per l'energia di un impulso, derivata per trovare i fronti.</li>
<li><b>Avvio di un oscillatore</b>: trigger single all'accensione per vedere quanto ci mette a partire e se parte sempre.</li>
<li>Tieni un <b>quaderno</b> con le impostazioni delle misure che fai spesso, o salvale come setup nello strumento.</li></ul></div></div>''')
rows=[("Ripple","AC, 20 MHz, molla corta; ΔV ≈ I/(f·C) + I·ESR"),("A − B","solo con modo comune basso, sonde uguali"),("Spunto","shunt sul negativo, trigger single"),("XY","firme di componenti in circuito"),
("TDR","d = VF·c·t/2 con un fronte veloce e un T"),("PTT e CW","inviluppo RF nel tempo: ALC e key click")]
D.add("Riepilogo",'<table class="sum">'+"".join(f'<tr><td class="l" style="width:180px"><b>{a}</b></td><td class="l">{b}</td></tr>' for a,b in rows)+'</table>')
D.render(); pdf("OSC_Misure_Inconsuete_Trucchi_IV3HGA.pdf")
