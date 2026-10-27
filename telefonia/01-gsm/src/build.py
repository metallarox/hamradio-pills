from deck import *
D=Deck("La telefonia cellulare:<br>il GSM","Celle e riuso delle frequenze, FDMA e TDMA, modulazione GMSK, il burst con la sequenza di training, dalla voce ai bit, l'equalizzatore di Viterbi, timing advance e frequency hopping","Telefonia · il GSM")
D.add("L'idea della rete cellulare",'''<div class="two"><div><ul>
<li>Il territorio è diviso in <b>celle</b>, ciascuna servita da una stazione base (BTS) con potenza limitata.</li>
<li>Celle abbastanza lontane possono <b>riusare</b> le stesse frequenze: lo spettro "si moltiplica" con il numero di celle.</li>
<li>Il telefono passa da una cella all'altra mentre ti muovi (<b>handover</b>) senza interrompere la chiamata.</li></ul></div><div>
<h3>Il GSM in cifre (banda 900)</h3><table><tr><td class="l">Uplink / downlink</td><td class="l">890–915 / 935–960 MHz (duplex 45 MHz)</td></tr>
<tr><td class="l">Portanti</td><td class="l">200 kHz, 124 canali</td></tr><tr><td class="l">Accesso</td><td class="l">FDMA + TDMA a 8 slot + FDD</td></tr>
<tr><td class="l">Modulazione</td><td class="l">GMSK, 270,833 kbit/s</td></tr><tr><td class="l">Voce (full rate)</td><td class="l">13 kbit/s → 22,8 kbit/s codificati</td></tr>
<tr><td class="l">Potenza max del telefono</td><td class="l">2 W (33 dBm) a 900 MHz</td></tr></table></div></div>''')
D.add("FDMA + TDMA: 8 utenti per portante",f'''<div class="fig" style="width:96%">{svg("frame.svg")}</div><div class="two" style="align-items:start;gap:30px;margin-top:10px"><div><ul>
<li>Ogni portante da 200 kHz è divisa in <b>8 slot</b> da 577 µs: una trama dura 4,615 ms.</li>
<li>Ogni telefono trasmette in uno slot per trama, cioè circa 1/8 del tempo: un burst ogni 4,615 ms.</li></ul></div><div><ul>
<li>Uplink e downlink sono sfasati di 3 slot: il telefono non deve trasmettere e ricevere nello stesso istante.</li>
<li>La ripetizione delle trame a 217 Hz è il "ronzio" che i telefoni GSM producono negli altoparlanti vicini.</li></ul></div></div>''')
D.add("La modulazione GMSK",f'''<div class="fig" style="width:94%">{svg("gmsk.svg")}</div><div class="two" style="align-items:start;gap:30px"><div><ul class="small">
<li><b>MSK</b>: una FSK a 2 livelli con deviazione di ¼ del bit rate (circa ±67,7 kHz): la fase cambia di ±90° per bit, in modo continuo.</li>
<li>Il filtro <b>gaussiano</b> (BT = 0,3) smussa le transizioni: lo spettro sta nei 200 kHz del canale.</li></ul></div><div><ul class="small">
<li>Il segnale resta sempre sul cerchio: <b>ampiezza costante</b>. Il finale del telefono può lavorare saturo ed efficiente, e la batteria dura.</li>
<li>Il prezzo: il filtro fa "sbavare" ogni bit sui vicini (interferenza tra simboli voluta), che il ricevitore deve gestire.</li></ul></div></div>''')
D.add("Il burst normale",f'''<div class="fig" style="width:96%">{svg("burst.svg")}</div><div class="two" style="align-items:start;gap:30px;margin-top:10px"><div><ul>
<li>Ogni burst porta <b>114 bit</b> di dati in due metà da 57, separate dalla <b>sequenza di training</b> di 26 bit nota a priori.</li>
<li>I bit di coda e il tempo di guardia (8,25 bit, circa 30 µs) separano i burst e lasciano accendere e spegnere il trasmettitore.</li></ul></div><div><ul>
<li>La training sequence sta al <b>centro</b>: è il "campione noto" con cui il ricevitore misura come il canale ha deformato il segnale proprio in quel momento.</li>
<li>Due flag segnalano se il burst porta voce o segnalazione urgente ("stealing").</li></ul></div></div>''')
D.add("Dalla voce ai bit",'''<div class="two"><div><ol>
<li>Il <b>codec</b> vocale comprime 20 ms di voce in 260 bit: 13 kbit/s.</li>
<li>I bit più importanti vengono protetti con un <b>codice convoluzionale</b> a rapporto 1/2: diventano 456 bit ogni 20 ms, cioè 22,8 kbit/s.</li>
<li>L'<b>interleaving</b> sparpaglia i 456 bit su 8 burst consecutivi.</li>
<li>I burst vengono trasmessi nello slot assegnato.</li></ol></div><div>
<h3>Perché l'interleaving</h3><ul class="small"><li>Un'evanescenza o un disturbo rovina un intero burst. Senza interleaving perderesti un blocco di bit consecutivi, troppi da correggere.</li>
<li>Con l'interleaving gli errori di un burst finiscono sparsi in otto blocchi diversi: ogni blocco ha pochi errori, che il codice convoluzionale corregge.</li>
<li>Il decodificatore del codice convoluzionale è proprio l'<b>algoritmo di Viterbi</b> (capitolo bonus).</li></ul></div></div>''')
D.add("Multipath e l'equalizzatore",'''<div class="two"><div><ul>
<li>In città il segnale arriva per più strade (riflessioni su palazzi e colline) con ritardi di qualche microsecondo. Un bit dura 3,7 µs: le copie ritardate si sovrappongono ai bit vicini.</li>
<li>Il ricevitore confronta la <b>training sequence</b> ricevuta con quella nota e stima la "risposta del canale" in quell'istante.</li>
<li>Poi cerca la sequenza di bit che, passata attraverso quel canale, spiega meglio ciò che ha ricevuto.</li></ul></div><div>
<h3>Un equalizzatore di Viterbi</h3><ul class="small"><li>Provare tutte le sequenze possibili sarebbe impossibile; l'algoritmo di <b>Viterbi</b> trova la migliore tenendo solo i percorsi "sopravvissuti".</li>
<li>Gestisce ritardi fino a circa 4–5 bit (15–20 µs), sufficienti per la maggior parte degli ambienti.</li>
<li>Lo stesso algoritmo, nel GSM, lavora due volte: per l'equalizzazione e per la decodifica del codice convoluzionale.</li></ul></div></div>''')
D.add("Timing advance, potenza, hopping",'''<div class="two"><div><h3>Timing advance</h3><ul class="small">
<li>Un telefono lontano arriva in ritardo: il suo burst finirebbe nello slot successivo.</li>
<li>La stazione base gli chiede di <b>anticipare</b> la trasmissione, in passi di un bit (circa 550 m di distanza).</li>
<li>Con 63 passi il raggio massimo della cella è circa <b>35 km</b> (con estensioni speciali di più).</li></ul>
<h3>Controllo di potenza</h3><ul class="small"><li>Telefono e stazione base riducono la potenza al minimo necessario: meno interferenza, più batteria.</li></ul></div><div>
<h3>Frequency hopping</h3><ul class="small"><li>Opzionalmente, a ogni trama il collegamento salta su una portante diversa: 217 salti al secondo.</li>
<li>Un'evanescenza o un'interferenza su una frequenza colpisce solo alcuni burst, che l'interleaving e il codice correggono.</li></ul>
<h3>Handover</h3><ul class="small"><li>Nei tempi liberi della trama il telefono misura le celle vicine e lo comunica alla rete, che decide quando passarlo a un'altra cella.</li></ul></div></div>''')
rows=[("Accesso","FDMA 200 kHz + TDMA 8 slot + FDD 45 MHz"),("GMSK","BT 0,3, 270,833 kbit/s, ampiezza costante"),("Burst","2 × 57 bit + 26 di training al centro"),("Voce","13 kbit/s → convoluzionale 1/2 → 22,8 kbit/s, interleaving su 8 burst"),("Ricevitore","equalizzatore di Viterbi sulla training sequence"),("Rete","timing advance (35 km), potenza, hopping, handover")]
D.add("Riepilogo",'<table class="sum">'+"".join(f'<tr><td class="l" style="width:160px"><b>{a}</b></td><td class="l">{b}</td></tr>' for a,b in rows)+'</table>')
D.render(); pdf("TEL_GSM_IV3HGA.pdf")
