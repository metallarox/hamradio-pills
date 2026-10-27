from deck import *
D=Deck("Sistemi numerici:<br>DMR, TETRA e gli altri","Dalla teoria ai sistemi veri: 4FSK e TDMA a due slot del DMR, π/4-DQPSK e quattro slot del TETRA, D-STAR, C4FM e gli altri, con vantaggi e limiti del digitale nella pratica","Modulazioni · DMR, TETRA e gli altri")
D.add("I sistemi numerici in VHF/UHF",'''<table><tr><th>Sistema</th><th>Modulazione</th><th>Simboli/s</th><th>Bit/s</th><th>Canale</th><th>Accesso</th></tr>
<tr><td class="l"><b>DMR</b> (ETSI)</td><td class="l">4FSK</td><td class="l">4800</td><td class="l">9600</td><td class="l">12,5 kHz</td><td class="l">TDMA, 2 slot</td></tr>
<tr><td class="l"><b>TETRA</b> (ETSI)</td><td class="l">π/4-DQPSK</td><td class="l">18 000</td><td class="l">36 000</td><td class="l">25 kHz</td><td class="l">TDMA, 4 slot</td></tr>
<tr><td class="l"><b>D-STAR</b> (JARL)</td><td class="l">GMSK</td><td class="l">4800</td><td class="l">4800</td><td class="l">6,25 kHz</td><td class="l">FDMA</td></tr>
<tr><td class="l"><b>C4FM / System Fusion</b></td><td class="l">4FSK</td><td class="l">4800</td><td class="l">9600</td><td class="l">12,5 kHz</td><td class="l">FDMA</td></tr>
<tr><td class="l"><b>P25 fase 1</b></td><td class="l">C4FM (4FSK)</td><td class="l">4800</td><td class="l">9600</td><td class="l">12,5 kHz</td><td class="l">FDMA</td></tr></table>
<p class="note" style="margin-top:14px">Stessi mattoni della lezione precedente: FSK o PSK, pochi simboli, filtri per contenere lo spettro. Cambiano i dettagli, la trama e il codec vocale.</p>''')
D.add("DMR: la modulazione 4FSK",f'''<div class="two"><div class="fig">{svg("dmr4fsk.svg")}</div><div><ul>
<li>Ogni simbolo porta <b>2 bit</b> (un "dibit") e corrisponde a una di 4 deviazioni di frequenza:</li></ul>
<table><tr><th>Dibit</th><th>Simbolo</th><th>Deviazione</th></tr><tr><td class="l">01</td><td>+3</td><td>+1944 Hz</td></tr><tr><td class="l">00</td><td>+1</td><td>+648 Hz</td></tr><tr><td class="l">10</td><td>−1</td><td>−648 Hz</td></tr><tr><td class="l">11</td><td>−3</td><td>−1944 Hz</td></tr></table>
<ul class="small"><li>4800 simboli/s × 2 bit = <b>9600 bit/s</b>, in 12,5 kHz.</li>
<li>Ampiezza costante: i finali possono essere quelli efficienti degli apparati FM.</li></ul></div></div>''')
D.add("DMR e TETRA: il TDMA",f'''<div class="fig" style="width:96%">{svg("tdma.svg")}</div><div class="two" style="align-items:start;gap:30px"><div><ul class="small">
<li>Nel <b>DMR</b> il canale è diviso in due intervalli di tempo: due conversazioni indipendenti sullo stesso canale da 12,5 kHz, cioè <b>6,25 kHz equivalenti</b> per conversazione.</li>
<li>Ogni radio trasmette solo 27,5 ms ogni 60: la batteria dura di più.</li></ul></div><div><ul class="small">
<li>Il <b>TETRA</b> usa 4 slot in 25 kHz: ancora 6,25 kHz equivalenti per utente, con più velocità per i dati.</li>
<li>È la "trama" che si vede in zero span con l'analizzatore o l'oscilloscopio (capitoli precedenti). FDMA e TDMA hanno un capitolo dedicato.</li></ul></div></div>''')
D.add("Dentro un burst DMR",'''<div class="two"><div><ul>
<li>Ogni burst dura 27,5 ms e contiene <b>264 bit</b>:</li></ul>
<table><tr><th>Parte</th><th>Bit</th><th>Contenuto</th></tr><tr><td class="l">carico utile</td><td>108</td><td class="l">voce o dati</td></tr>
<tr><td class="l">centro</td><td>48</td><td class="l">sincronismo o segnalazione</td></tr><tr><td class="l">carico utile</td><td>108</td><td class="l">voce o dati</td></tr></table>
<ul class="small"><li>Il sincronismo al centro serve al ricevitore per agganciarsi alla trama e riconoscere voce o dati.</li></ul></div><div>
<h3>Voce e identificativi</h3><ul class="small"><li>Codec vocale <b>AMBE+2</b>: 2450 bit/s di voce più 1150 bit/s di correzione d'errore, 3600 bit/s per slot.</li>
<li><b>Color code</b>: un numero da 0 a 15 che distingue i ripetitori sulla stessa frequenza, come un "tono" digitale.</li>
<li><b>Talkgroup</b> e ID dell'utente: chi parla e a chi, dentro il segnale stesso.</li>
<li>Una parte della capacità va in segnalazione: per questo 9600 bit/s non sono tutti "voce".</li></ul></div></div>''')
D.add("TETRA: la π/4-DQPSK",f'''<div class="two" style="grid-template-columns:1.25fr 1fr"><div class="fig">{svg("pi4.svg")}</div><div><ul class="small">
<li>QPSK <b>differenziale</b>: i 2 bit di ogni simbolo non sono una fase assoluta, ma un <b>salto di fase</b> rispetto al simbolo precedente: +45°, +135°, −45°, −135°.</li>
<li>Il ricevitore non deve ricostruire la fase esatta della portante: confronta un simbolo con il precedente. Più semplice e robusto in mobilità.</li>
<li>Il salto non è mai 0° né 180°: le transizioni non passano per il centro, l'inviluppo non si annulla e i finali soffrono meno (amplificatori lineari ma meno critici).</li>
<li>18 000 simboli/s, filtro a radice di coseno rialzato con α = 0,35: circa 24,3 kHz nel canale da 25 kHz.</li></ul></div></div>''')
D.add("TETRA: trama e servizi",'''<div class="two"><div><ul>
<li>4 slot da 14,17 ms formano una trama da 56,67 ms; 18 trame formano una multitrama di circa 1,02 s. La 18ª trama è dedicata al controllo.</li>
<li>Ogni slot porta 510 bit lordi. Il codec vocale ACELP usa circa 4,6 kbit/s, più la protezione.</li></ul></div><div>
<h3>Perché lo usano i servizi di emergenza</h3><ul class="small"><li>Chiamate di gruppo con accesso immediato, priorità, chiamate di emergenza.</li>
<li>Dati, messaggi di stato, posizione, crittografia.</li>
<li>Modalità diretta tra terminali (DMO) quando la rete non c'è.</li>
<li>Rete cellulare: i terminali passano da una stazione base all'altra in movimento.</li>
<li>Molte di queste cose sono possibili proprio perché il segnale è numerico e organizzato in trame.</li></ul></div></div>''')
D.add("D-STAR, C4FM e gli altri",'''<div class="two"><div><h3>D-STAR</h3><ul class="small">
<li>GMSK a 4800 bit/s in 6,25 kHz: una FSK a due livelli con filtro gaussiano, ampiezza costante.</li>
<li>Codec AMBE, dati lenti in parallelo alla voce (testo, posizione), modalità dati veloce in 23 cm.</li></ul>
<h3>C4FM (System Fusion)</h3><ul class="small"><li>4FSK come il DMR, ma in FDMA (una conversazione per canale): modalità "voce piena" a qualità più alta o voce + dati.</li></ul></div><div>
<h3>Lo stesso schema per tutti</h3><ul class="small"><li>Modulazione semplice a inviluppo costante (o quasi), adatta ai finali FM.</li>
<li>Codec vocale a bassa velocità e correzione d'errore.</li>
<li>Trama con sincronismo, identificativi e segnalazione.</li>
<li>I sistemi non sono compatibili tra loro: servono ripetitori o ponti che convertono (gateway).</li></ul></div></div>''')
D.add("Il digitale nella pratica",'''<div class="two"><div><h3>Vantaggi</h3><ul class="small">
<li>Audio <b>pulito</b> fino al limite: niente fruscio crescente.</li><li>Più conversazioni per MHz (TDMA, canali stretti).</li>
<li>Identificativi, messaggi, posizione, gruppi, crittografia.</li><li>Batterie che durano di più (TDMA).</li></ul></div><div>
<h3>Limiti</h3><ul class="small"><li><b>Effetto soglia</b> ("cliff effect"): sopra la soglia è perfetto, sotto sparisce di colpo. Con l'FM il segnale debole si sente male ma si sente.</li>
<li>Voce "metallica" con i codec a bassa velocità; latenza di decine o centinaia di ms.</li>
<li>Sistemi incompatibili tra loro e configurazione più complessa (codeplug, talkgroup, color code).</li>
<li>Misurarli richiede strumenti adatti: costellazioni, BER, errori di modulazione.</li></ul></div></div>''')
rows=[("DMR","4FSK ±648/±1944 Hz, 9600 bit/s, 2 slot in 12,5 kHz"),("TETRA","π/4-DQPSK, 36 kbit/s, 4 slot in 25 kHz"),("D-STAR","GMSK 4800 bit/s, 6,25 kHz"),("C4FM","4FSK 9600 bit/s, FDMA"),("Pratica","audio pulito fino alla soglia, poi nulla")]
D.add("Riepilogo",'<table class="sum">'+"".join(f'<tr><td class="l" style="width:160px"><b>{a}</b></td><td class="l">{b}</td></tr>' for a,b in rows)+'</table>')
D.render(); pdf("MOD_DMR_TETRA_Sistemi_IV3HGA.pdf")
