from deck import *
D=Deck("Accesso multiplo:<br>FDMA, TDMA, CDMA","Come tanti utenti condividono lo stesso spettro: dividere in frequenza, in tempo, con codici o con tutte e tre le cose insieme. Duplex FDD e TDD, accesso casuale ed esempi dai ponti radio alla telefonia","Accesso multiplo")
D.add("Il problema",'''<div class="two"><div><ul>
<li>Lo spettro è una risorsa limitata, e tutti vogliono parlare. Come si fa a far comunicare tanti utenti senza che si disturbino?</li>
<li>Un segnale occupa un pezzo di <b>frequenza</b> per un certo <b>tempo</b>. Si può dividere la frequenza, il tempo, o distinguere gli utenti con un <b>codice</b>.</li></ul></div><div>
<table><tr><th>Tecnica</th><th>Si divide…</th><th>Esempi</th></tr>
<tr><td class="l"><b>FDMA</b></td><td class="l">la frequenza</td><td class="l">ponti FM, broadcast, D-STAR, FT8 nel waterfall</td></tr>
<tr><td class="l"><b>TDMA</b></td><td class="l">il tempo</td><td class="l">DMR, TETRA, GSM</td></tr>
<tr><td class="l"><b>CDMA</b></td><td class="l">il codice</td><td class="l">UMTS/WCDMA, GPS</td></tr>
<tr><td class="l"><b>OFDMA</b></td><td class="l">frequenza e tempo a blocchi</td><td class="l">LTE, 5G, Wi-Fi moderno</td></tr></table></div></div>''')
D.add("Quattro modi di dividere lo spettro",f'''<div class="fig" style="width:96%">{svg("grids.svg")}</div><div class="two" style="align-items:start;gap:30px"><div><ul class="small">
<li>Ogni colore è un utente. In <b>FDMA</b> ognuno ha la sua striscia di frequenza per tutto il tempo; in <b>TDMA</b> tutta la banda per una frazione del tempo.</li></ul></div><div><ul class="small">
<li>In <b>CDMA</b> tutti trasmettono insieme sulla stessa banda e si distinguono per il codice. In <b>OFDMA</b> la rete assegna a ciascuno blocchi di tempo e frequenza secondo le necessità.</li></ul></div></div>''')
D.add("FDMA",'''<div class="two"><div><ul>
<li>Ogni utente o servizio ha il suo <b>canale</b>: è il modo più antico e naturale, quello dei ponti radio FM e delle stazioni broadcast.</li>
<li>Servono <b>bande di guardia</b> tra i canali e filtri selettivi nei ricevitori (la selettività del capitolo sul generatore).</li></ul></div><div>
<h3>Pregi e limiti</h3><ul class="small"><li>Semplice: il trasmettitore lavora in continuo, nessuna sincronizzazione tra utenti.</li>
<li>Ogni canale richiede la sua catena RF: in un ponte con 4 canali servono 4 trasmettitori e un combinatore.</li>
<li>Canali più stretti (da 25 a 12,5 e 6,25 kHz) aumentano gli utenti, ma richiedono oscillatori più stabili e filtri migliori.</li>
<li>Anche FT8 nel waterfall è un FDMA "spontaneo": ognuno sceglie la sua frequenza audio.</li></ul></div></div>''')
D.add("TDMA",'''<div class="two"><div><ul>
<li>Un canale viene diviso in <b>intervalli di tempo</b> (slot) che si ripetono in una trama. Ogni utente trasmette a <b>burst</b> nel suo slot.</li>
<li>Tra gli slot servono <b>tempi di guardia</b>: i segnali arrivano con ritardi diversi a seconda della distanza.</li></ul>
<table><tr><th>Sistema</th><th>Slot</th><th>Trama</th></tr><tr><td class="l">DMR</td><td class="l">2 × 30 ms</td><td class="l">60 ms</td></tr>
<tr><td class="l">TETRA</td><td class="l">4 × 14,17 ms</td><td class="l">56,67 ms</td></tr><tr><td class="l">GSM</td><td class="l">8 × 0,577 ms</td><td class="l">4,615 ms</td></tr></table></div><div>
<h3>Pregi e limiti</h3><ul class="small"><li>Un solo trasmettitore serve più utenti; i terminali trasmettono una frazione del tempo e risparmiano batteria.</li>
<li>Nel tempo libero il terminale può misurare altri canali (handover) o ricevere segnalazione.</li>
<li>Richiede sincronismo preciso e compensazione dei ritardi (timing advance nel GSM).</li>
<li>I burst producono disturbi pulsati: il "ronzio" a 217 Hz dei telefoni GSM negli altoparlanti è la frequenza delle trame (1 / 4,615 ms).</li></ul></div></div>''')
D.add("CDMA: tutti insieme, con un codice",f'''<div class="two" style="grid-template-columns:1.3fr 1fr"><div class="fig">{svg("cdma.svg")}</div><div><ul class="small">
<li>Ogni bit viene moltiplicato per un <b>codice</b> veloce (qui 8 "chip" per bit): il segnale si allarga in frequenza (<b>spread spectrum</b>).</li>
<li>Il ricevitore moltiplica per lo <b>stesso</b> codice e somma: il segnale voluto si ricompone, gli altri utenti (codici diversi) e il rumore restano sparsi.</li>
<li>Il guadagno di questa operazione è il <b>guadagno di processo</b>: 10·log(chip per bit). Con 8 chip: 9 dB; nel WCDMA anche oltre 20 dB.</li>
<li>Anche con molto rumore (ultima riga) il segno dei bit si legge bene.</li></ul></div></div>''')
D.add("CDMA: vantaggi e problemi",'''<div class="two"><div><h3>Vantaggi</h3><ul class="small">
<li>Tutte le celle possono usare la <b>stessa frequenza</b>: niente pianificazione dei canali.</li>
<li>Robusto contro disturbi a banda stretta e contro il multipath (ricevitore RAKE).</li>
<li><b>Soft handover</b>: un telefono può parlare con due celle insieme.</li>
<li>Il GPS usa lo stesso principio: tutti i satelliti sulla stessa frequenza, distinti dal codice.</li></ul></div><div>
<h3>Il problema "vicino-lontano"</h3><ul class="small"><li>Un utente vicino arriva molto più forte di uno lontano e lo "copre", anche con codici diversi.</li>
<li>Serve un <b>controllo di potenza</b> rapidissimo: nel WCDMA 1500 volte al secondo, in modo che tutti arrivino alla stazione base con la potenza giusta.</li>
<li>Più utenti significa più "rumore" per tutti: la capacità cala dolcemente invece di bloccarsi.</li></ul></div></div>''')
D.add("Duplex: FDD e TDD",'''<div class="two"><div><h3>FDD (duplex a divisione di frequenza)</h3><ul class="small">
<li>Trasmissione e ricezione su due frequenze diverse, separate dal <b>passo di duplex</b>.</li>
<li>Esempi: i ponti radio (−600 kHz in 2 m), GSM 900 (45 MHz), TETRA (10 MHz).</li>
<li>Per trasmettere e ricevere insieme con la stessa antenna serve un <b>duplexer</b>: filtri a cavità che isolano TX e RX (quelli che si tarano con il VNA o con tracking generator).</li></ul></div><div>
<h3>TDD (duplex a divisione di tempo)</h3><ul class="small"><li>Stessa frequenza, si alternano trasmissione e ricezione nel tempo.</li>
<li>Esempi: DECT, Wi-Fi, molte reti 5G, e in fondo anche FT8 con i cicli pari e dispari.</li>
<li>Niente duplexer, ma serve sincronismo e si perde un po' di tempo nei passaggi.</li></ul>
<p class="note">Il DMR in modalità diretta (senza ripetitore) usa una sola frequenza e alterna gli slot; con il ripetitore è FDD + TDMA.</p></div></div>''')
D.add("Accesso casuale e combinazioni",'''<div class="two"><div><h3>Accesso casuale</h3><ul class="small">
<li>Quando gli utenti trasmettono raramente, non conviene riservare un canale: si trasmette quando serve.</li>
<li><b>ALOHA</b>: trasmetti, e se c'è una collisione riprova dopo un tempo casuale. È usato per la richiesta iniziale di canale in GSM e TETRA.</li>
<li><b>CSMA</b>: prima ascolta, poi trasmetti se il canale è libero. È il packet radio, l'APRS, il Wi-Fi.</li></ul></div><div>
<h3>Nella realtà si combinano</h3><ul class="small"><li><b>GSM</b>: FDMA (portanti da 200 kHz) + TDMA (8 slot) + FDD.</li>
<li><b>WCDMA</b>: FDMA (portanti da 5 MHz) + CDMA + FDD.</li>
<li><b>LTE</b>: OFDMA, blocchi di 12 sottoportanti da 15 kHz per 0,5 ms.</li>
<li>Il prossimo capitolo li guarda da vicino.</li></ul></div></div>''')
rows=[("FDMA","un canale per utente; bande di guardia"),("TDMA","slot e trame; burst e sincronismo"),("CDMA","stesso spettro, codici diversi; guadagno 10·log(chip/bit)"),("OFDMA","blocchi tempo-frequenza assegnati dalla rete"),("Duplex","FDD con duplexer; TDD a turni")]
D.add("Riepilogo",'<table class="sum">'+"".join(f'<tr><td class="l" style="width:160px"><b>{a}</b></td><td class="l">{b}</td></tr>' for a,b in rows)+'</table>')
D.render(); pdf("ACC_FDMA_TDMA_CDMA_IV3HGA.pdf")
