from deck import *
D=Deck("FT8: come funziona","Il modo digitale che ha cambiato le bande: cicli di 15 secondi, modulazione 8-GFSK, sincronismo Costas, correzione d'errore LDPC, il waterfall e perché si decodifica sotto il rumore","FT8")
D.add("Che cos'è FT8",'''<div class="two"><div><ul>
<li>Un modo digitale per collegamenti con <b>segnali deboli</b>, sviluppato nel 2017 da K1JT e K9AN all'interno del programma WSJT-X.</li>
<li>Scambi brevi e standard: nominativi, locatore, rapporto in dB, conferma. Niente conversazione libera.</li>
<li>Ogni trasmissione dura <b>12,64 s</b> dentro cicli fissi di <b>15 s</b>.</li>
<li>Si usa in <b>USB</b>: il ricetrasmettitore trasmette l'audio generato dal computer (per esempio 14,074 MHz in 20 m).</li></ul></div><div>
<h3>Le cifre</h3><table><tr><td class="l">Modulazione</td><td class="l">8-GFSK, 8 toni</td></tr><tr><td class="l">Spaziatura dei toni</td><td class="l">6,25 Hz</td></tr>
<tr><td class="l">Durata del simbolo</td><td class="l">0,16 s (6,25 baud)</td></tr><tr><td class="l">Simboli per messaggio</td><td class="l">79 (58 dati + 21 sincronismo)</td></tr>
<tr><td class="l">Banda occupata</td><td class="l">50 Hz</td></tr><tr><td class="l">Messaggio</td><td class="l">77 bit + 14 di CRC, codice LDPC (174, 91)</td></tr>
<tr><td class="l">Soglia di decodifica</td><td class="l">circa −20 / −21 dB in 2500 Hz</td></tr></table></div></div>''')
D.add("Il ciclo di 15 secondi",'''<div class="two"><div><ul>
<li>Il tempo è diviso in intervalli di 15 s che iniziano a :00, :15, :30, :45 di ogni minuto.</li>
<li>Una stazione trasmette negli intervalli <b>pari</b>, l'altra nei <b>dispari</b>: si alternano come in un dialogo a turni.</li>
<li>Restano circa 2 s a fine ciclo per decodificare e decidere la risposta.</li></ul></div><div>
<h3>L'orologio conta</h3><ul class="small"><li>Il decodificatore cerca i segnali solo intorno all'inizio previsto: l'orologio del computer deve essere preciso entro circa <b>1 secondo</b>.</li>
<li>Sincronizzalo con un server di tempo (NTP) o con un ricevitore GPS. È l'errore più comune di chi inizia: "non decodifico niente".</li>
<li>Il valore DT mostrato dal programma è lo scarto di tempo di ogni segnale: se tutti hanno DT simile e lontano da zero, è il tuo orologio.</li></ul></div></div>''')
D.add("La modulazione: 8 toni",f'''<div class="fig" style="width:96%">{svg("tonemap.svg")}</div><div class="two" style="align-items:start;gap:30px"><div><ul class="small">
<li>Ogni simbolo è uno di <b>8 toni</b> distanti 6,25 Hz: porta 3 bit. 58 simboli di dati × 3 = <b>174 bit</b>.</li>
<li>Il tono dura 0,16 s: 6,25 Hz × 0,16 s = 1, i toni sono "ortogonali" e non si confondono tra loro.</li></ul></div><div><ul class="small">
<li>La <b>G</b> di GFSK: i passaggi tra i toni sono smussati da un filtro gaussiano, così lo spettro resta compatto.</li>
<li>Ampiezza costante: il trasmettitore non deve essere lineare, ma l'audio non deve saturare (ALC a zero).</li></ul></div></div>''')
D.add("Il sincronismo: gli array di Costas",'''<div class="two"><div><ul>
<li>All'inizio, a metà e alla fine di ogni messaggio c'è una sequenza fissa di 7 toni: <b>3, 1, 4, 0, 6, 5, 2</b>.</li>
<li>È un <b>array di Costas</b>: una sequenza con una proprietà speciale. Se la confronti con se stessa spostata nel tempo o in frequenza, combacia solo nella posizione giusta.</li>
<li>Il ricevitore la cerca in tutto il waterfall: dove la trova, sa esattamente <b>dove</b> (frequenza) e <b>quando</b> (tempo) inizia un segnale, anche se è sotto il rumore.</li></ul></div><div>
<h3>Perché tre volte</h3><ul class="small"><li>21 simboli su 79 servono solo a trovare i segnali: un "investimento" del 27 %.</li>
<li>Tre copie distribuite nel messaggio rendono la ricerca robusta anche se una parte del segnale è disturbata o in evanescenza.</li>
<li>Una volta agganciati tempo e frequenza, il decodificatore misura l'energia di ciascuno degli 8 toni in ogni simbolo di dati.</li></ul></div></div>''')
D.add("Dal messaggio ai bit",'''<div class="two"><div><ol>
<li>Il messaggio (per esempio "CQ IV3HGA JN66") viene compresso in <b>77 bit</b>: i nominativi e il locatore hanno formati standard e occupano pochi bit.</li>
<li>Si aggiungono <b>14 bit di CRC</b>: un controllo che dice se la decodifica è giusta. Totale 91 bit.</li>
<li>Un codice <b>LDPC (174, 91)</b> aggiunge 83 bit di ridondanza: 174 bit.</li>
<li>I 174 bit diventano 58 simboli da 3 bit, con codifica <b>Gray</b> (toni vicini differiscono di un bit).</li></ol></div><div>
<h3>La correzione d'errore</h3><ul class="small"><li>Il codice LDPC permette di ricostruire il messaggio anche se molti simboli sono stati letti male.</li>
<li>Il decodificatore usa informazioni "morbide": non solo quale tono sembra più forte, ma <b>quanto</b> è più forte degli altri.</li>
<li>Il CRC evita i falsi messaggi: se dopo la correzione il controllo non torna, il messaggio viene scartato.</li>
<li>Il principio è lo stesso della correzione d'errore della telefonia e del capitolo bonus su Viterbi, con un codice più moderno.</li></ul></div></div>''')
D.add("Il waterfall: tanti QSO in 3 kHz",f'''<div class="fig" style="width:96%">{svg("waterfall.svg")}</div><div class="two" style="align-items:start;gap:30px"><div><ul class="small">
<li>Nella banda audio di un ricevitore SSB (circa 200–3000 Hz) stanno decine di segnali FT8 da 50 Hz: è un'<b>FDMA</b> spontanea.</li>
<li>Il programma li decodifica tutti insieme, anche quelli che a occhio non si vedono.</li></ul></div><div><ul class="small">
<li>Le trasmissioni iniziano tutte allo stesso istante: è anche una forma di <b>TDMA</b> (pari/dispari).</li>
<li>Scegli per trasmettere una frequenza libera: due segnali sovrapposti si disturbano.</li></ul></div></div>''')
D.add("Perché funziona sotto il rumore",f'''<div class="two"><div class="fig">{svg("bw.svg")}</div><div><ul class="small">
<li>Il rapporto S/N di FT8 è riferito a <b>2500 Hz</b> di banda, come per un ascolto in SSB. Ma il segnale occupa 50 Hz: rispetto a 2500 Hz, 17 dB di rumore in meno.</li>
<li>Ogni tono dura 0,16 s in un "cassetto" di 6,25 Hz: a −21 dB in 2500 Hz corrisponde circa <b>+5 dB</b> nel cassetto del tono.</li>
<li>La correzione d'errore lavora sull'intero messaggio di 12,64 s: integra l'energia di tutti i simboli.</li>
<li>Il prezzo è la <b>velocità</b>: circa 6 bit/s di informazione utile. È il limite di Shannon in pratica: poco segnale, poca velocità.</li></ul></div></div>''')
D.add("Un QSO tipico",'''<div class="two"><div><table><tr><th>Ciclo</th><th>Messaggio</th></tr>
<tr><td class="l">pari</td><td class="l">CQ IV3HGA JN66</td></tr><tr><td class="l">dispari</td><td class="l">IV3HGA DL1ABC JO62</td></tr>
<tr><td class="l">pari</td><td class="l">DL1ABC IV3HGA −12</td></tr><tr><td class="l">dispari</td><td class="l">IV3HGA DL1ABC R−08</td></tr>
<tr><td class="l">pari</td><td class="l">DL1ABC IV3HGA RR73</td></tr><tr><td class="l">dispari</td><td class="l">IV3HGA DL1ABC 73</td></tr></table>
<p class="note">Nominativo di esempio. Un QSO completo in circa un minuto e mezzo.</p></div><div>
<ul class="small"><li>Il rapporto (−12) è il S/N con cui ricevi l'altro, in dB riferiti a 2500 Hz.</li>
<li>"R" davanti al rapporto conferma di aver ricevuto il tuo; "RR73" chiude il QSO.</li>
<li>Potenze di pochi watt bastano spesso per collegamenti intercontinentali in HF: l'efficienza del modo compensa.</li>
<li>Livelli audio: niente saturazione e ALC a zero, altrimenti il segnale si allarga e disturba le stazioni vicine.</li></ul></div></div>''')
D.add("Cosa insegna FT8 sul numerico",'''<div class="two"><div><h3>I vantaggi in un esempio</h3><ul class="small">
<li><b>Banda stretta</b> e lunga integrazione: segnali leggibili 20 dB sotto il rumore in SSB.</li>
<li><b>Correzione d'errore</b>: messaggi perfetti anche con molti simboli sbagliati.</li><li><b>CRC</b>: o il messaggio è giusto, o non c'è.</li>
<li><b>Sincronismo</b> e decodifica automatica di decine di segnali.</li></ul></div><div>
<h3>E i limiti</h3><ul class="small"><li>Pochissima informazione: niente conversazioni, solo lo scambio essenziale.</li>
<li>Dipende dalla precisione del tempo e del computer.</li><li>Effetto soglia: sotto −21 dB il messaggio semplicemente non c'è.</li>
<li>È la stessa scelta di fondo di tutti i sistemi numerici: robustezza contro velocità, decisa dalla quantità di segnale disponibile.</li></ul></div></div>''')
rows=[("Tempo","cicli di 15 s, orologio entro ~1 s"),("Modulazione","8-GFSK, 6,25 Hz, 0,16 s, 50 Hz di banda"),("Sincronismo","3 array di Costas 3-1-4-0-6-5-2"),("Codifica","77 bit + CRC 14 → LDPC (174, 91) → 58 simboli"),("Soglia","circa −21 dB in 2500 Hz"),("Lezione","poco segnale, poca velocità: Shannon in pratica")]
D.add("Riepilogo",'<table class="sum">'+"".join(f'<tr><td class="l" style="width:200px"><b>{a}</b></td><td class="l">{b}</td></tr>' for a,b in rows)+'</table>')
D.render(); pdf("FT8_Come_Funziona_IV3HGA.pdf")
