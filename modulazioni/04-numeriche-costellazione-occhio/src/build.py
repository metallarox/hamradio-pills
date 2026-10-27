from deck import *
D=Deck("Le modulazioni<br>numeriche","Bit, simboli e baud, ASK, FSK e PSK, il piano I/Q e il diagramma a costellazione, QPSK e QAM, filtri e coseno rialzato, il diagramma ad occhio e perché il numerico conviene","Modulazioni · numeriche")
D.add("Perché il numerico",'''<div class="two"><div><ul>
<li>Il segnale trasporta <b>numeri</b> (bit), non una forma d'onda. Il ricevitore non deve riprodurla fedelmente: deve solo <b>decidere</b> quale simbolo è stato trasmesso.</li>
<li>Finché le decisioni sono giuste, il risultato è <b>perfetto</b>: niente fruscio che cresce con la distanza, come in FM o SSB.</li></ul></div><div>
<h3>I vantaggi</h3><ul class="small"><li><b>Correzione degli errori</b>: bit di ridondanza permettono di riparare gli errori (capitolo bonus su Viterbi).</li>
<li><b>Compressione</b>: un codec vocale riduce la voce a 2–13 kbit/s.</li><li><b>Più utenti</b> sullo stesso canale (TDMA, capitolo sull'accesso multiplo).</li>
<li>Dati, messaggi, posizione, identificativo dell'utente, <b>crittografia</b>.</li>
<li>Segnali leggibili ben sotto il rumore, come FT8 (capitolo dedicato).</li></ul></div></div>''')
D.add("Bit, simboli e baud",'''<div class="two"><div><ul>
<li>Un <b>simbolo</b> è uno stato del segnale tenuto per un certo tempo: un'ampiezza, una frequenza, una fase, o una loro combinazione.</li>
<li>Con M simboli diversi, ogni simbolo porta log<sub>2</sub>M bit.</li></ul>
<div class="eq">bit rate = symbol rate × log<sub>2</sub>M</div>
<ul class="small"><li>Il <b>baud</b> è l'unità del symbol rate (simboli al secondo), non dei bit.</li></ul></div><div>
<table><tr><th>M</th><th>bit per simbolo</th><th>Esempio</th></tr>
<tr><td class="l">2</td><td>1</td><td class="l">BPSK, FSK a 2 toni</td></tr><tr><td class="l">4</td><td>2</td><td class="l">QPSK, 4FSK (DMR)</td></tr>
<tr><td class="l">8</td><td>3</td><td class="l">8PSK, 8 toni di FT8</td></tr><tr><td class="l">16</td><td>4</td><td class="l">16QAM</td></tr><tr><td class="l">64</td><td>6</td><td class="l">64QAM (Wi-Fi, LTE)</td></tr></table>
<p class="note">Esempio: DMR trasmette 4800 simboli/s con 4 livelli → 9600 bit/s.</p></div></div>''')
D.add("ASK, FSK, PSK",f'''<div class="fig" style="width:86%;margin:-8px auto 0">{svg("ask_fsk_psk.svg")}</div><div class="two" style="align-items:start;gap:30px"><div><ul class="small">
<li><b>ASK</b>: il bit cambia l'ampiezza (il CW è un ASK). <b>FSK</b>: il bit cambia la frequenza (RTTY, packet, DMR, FT8).</li></ul></div><div><ul class="small">
<li><b>PSK</b>: il bit cambia la fase (PSK31, satelliti, telefonia). Gli stessi tre "comandi" delle modulazioni analogiche.</li></ul></div></div>''')
D.add("Il piano I/Q",f'''<div class="two"><div class="fig" style="width:80%;margin:auto">{svg("iq.svg")}</div><div><ul>
<li>Ogni sinusoide a una data frequenza si può scrivere come somma di un coseno (<b>I</b>, in fase) e di un seno (<b>Q</b>, in quadratura):</li></ul>
<div class="eq">v(t) = I·cos(ωt) − Q·sin(ωt)</div>
<ul class="small"><li>La coppia (I, Q) è un <b>punto</b> su un piano: la distanza dal centro è l'ampiezza, l'angolo è la fase.</li>
<li>Un simbolo è un punto; l'insieme dei punti possibili è la <b>costellazione</b>.</li>
<li>Così ampiezza e fase si governano insieme: è il modo in cui lavorano tutti gli SDR e i modem moderni.</li></ul></div></div>''')
D.add("Il diagramma a costellazione",f'''<div class="fig" style="width:96%">{svg("const.svg")}</div><div class="two" style="align-items:start;gap:30px"><div><ul class="small">
<li>Più punti = più bit per simbolo = più velocità nella stessa banda.</li>
<li>Ma i punti sono più <b>vicini</b>: basta meno rumore per confonderli. Servono segnali più forti.</li></ul></div><div><ul class="small">
<li>La <b>codifica Gray</b> assegna i bit in modo che punti vicini differiscano di un solo bit: un errore di poco costa un bit, non tutto il simbolo.</li>
<li>I sistemi moderni scelgono la costellazione in base alla qualità del collegamento (modulazione adattiva).</li></ul></div></div>''')
D.add("La costellazione con il rumore",f'''<div class="fig" style="width:96%">{svg("noisy.svg")}</div><div class="two" style="align-items:start;gap:30px"><div><ul class="small">
<li>Il rumore trasforma ogni punto in una "nuvola". Il ricevitore assegna ogni campione al punto ideale più vicino.</li>
<li>Se le nuvole si sovrappongono, alcune decisioni sono sbagliate: errori di bit.</li></ul></div><div><ul class="small">
<li>QPSK a 10 dB è ancora leggibile, 16QAM a 14 dB comincia a confondersi.</li>
<li>L'<b>EVM</b> (errore di vettore) misura la distanza media dei punti ricevuti da quelli ideali: è il "SINAD" delle modulazioni numeriche.</li></ul></div></div>''')
D.add("Filtri e forma degli impulsi",f'''<div class="two"><div class="fig">{svg("rcspec.svg")}</div><div><ul class="small">
<li>Se i simboli cambiano di colpo, lo spettro ha "code" lunghissime che disturbano i canali vicini.</li>
<li>Si filtrano gli impulsi con un <b>coseno rialzato</b> (spesso diviso in due "radice di coseno rialzato", metà in TX e metà in RX).</li></ul>
<div class="eq">banda ≈ symbol rate × (1 + α)</div>
<ul class="small"><li>α (roll-off) tra 0 e 1: piccolo = spettro compatto ma più sensibile agli errori di temporizzazione.</li>
<li>Esempio: TETRA, 18 000 simboli/s, α = 0,35 → circa 24,3 kHz: sta nel canale da 25 kHz.</li>
<li>In FSK si fa lo stesso con un filtro gaussiano: GFSK, GMSK (GSM).</li></ul></div></div>''')
D.add("Il diagramma ad occhio",f'''<div class="fig" style="width:96%">{svg("eye.svg")}</div><div class="two" style="align-items:start;gap:30px"><div><ul class="small">
<li>Si sovrappongono tanti tratti del segnale demodulato, lunghi due simboli, sincronizzati sul clock: appare un "occhio".</li>
<li>L'<b>apertura verticale</b> è il margine contro il rumore; l'<b>apertura orizzontale</b> il margine sulla temporizzazione.</li></ul></div><div><ul class="small">
<li>Il campionamento va fatto al centro dell'occhio, dove è più aperto.</li>
<li>Un occhio che si chiude indica rumore, interferenza tra simboli (filtri sbagliati, multipath) o errore di temporizzazione. Con 4 livelli ci sono 3 occhi sovrapposti, più piccoli: serve più segnale.</li></ul></div></div>''')
D.add("Robustezza contro velocità",'''<div class="two"><div><table><tr><th>Modulazione</th><th>bit/simbolo</th><th>E<sub>b</sub>/N<sub>0</sub> per BER 10<sup>−5</sup></th></tr>
<tr><td class="l">BPSK, QPSK</td><td>1, 2</td><td>≈ 9,6 dB</td></tr><tr><td class="l">FSK a 2 toni (non coerente)</td><td>1</td><td>≈ 13,4 dB</td></tr>
<tr><td class="l">16QAM</td><td>4</td><td>≈ 13,4 dB</td></tr><tr><td class="l">64QAM</td><td>6</td><td>≈ 17,8 dB</td></tr></table>
<p class="note">Valori teorici senza codifica; con la correzione d'errore servono diversi dB in meno.</p></div><div>
<h3>Il limite di Shannon</h3><div class="eq">C = B · log<sub>2</sub>(1 + S/N)</div>
<ul class="small"><li>La capacità massima di un canale dipende dalla banda e dal rapporto segnale/rumore.</li>
<li>Con S/N molto basso si può comunicare lo stesso, ma lentamente: è la strada di FT8 e dei modi per segnali deboli.</li>
<li>Con S/N alto si possono usare costellazioni grandi: la strada di Wi-Fi e LTE.</li></ul></div></div>''')
rows=[("Simbolo","log<sub>2</sub>M bit; bit rate = baud × log<sub>2</sub>M"),("I/Q","un simbolo è un punto: ampiezza e fase"),("Costellazione","più punti, più velocità, più segnale necessario"),("Coseno rialzato","banda ≈ Rs·(1 + α)"),("Occhio","verticale: rumore; orizzontale: temporizzazione"),("Shannon","C = B·log<sub>2</sub>(1 + S/N)")]
D.add("Riepilogo",'<table class="sum">'+"".join(f'<tr><td class="l" style="width:200px"><b>{a}</b></td><td class="l">{b}</td></tr>' for a,b in rows)+'</table>')
D.render(); pdf("MOD_Numeriche_Costellazione_Occhio_IV3HGA.pdf")
