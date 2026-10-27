from deck import *
D=Deck("Test di sensibilità:<br>SINAD e MDS","Che cosa vuol dire sensibilità, SINAD 12 dB in FM passo per passo, S/N 10 dB in AM e SSB, MDS e cifra di rumore, strumenti necessari, errori tipici ed esempi numerici","Il generatore RF: test di sensibilità")
setup=f'''<svg viewBox="0 0 1000 220" font-family="DejaVu Sans">{ARW}
{box(10,60,150,70,"Generatore RF|(modulato)","#fff",14)}{ln(160,95,200,95)}{box(200,65,130,60,"Attenuatore|6–10 dB",L,13)}{ln(330,95,370,95)}
{box(370,55,160,80,"Ricevitore|in prova","#fff",15)}{ln(530,95,570,95)}{box(570,60,160,70,"Carico audio|(R altoparlante)",L,13)}{ln(730,95,770,95)}
{box(770,55,210,80,"SINAD-metro|o analizzatore audio|(filtro notch 1 kHz)","#fff",13)}
<text x="370" y="170" font-size="12" fill="#555">squelch aperto, volume a una potenza audio nota (es. metà della nominale)</text>
<text x="10" y="200" font-size="12" fill="#555">livello all'ingresso = livello del generatore − cavi − attenuatore</text></svg>'''
D.add("Che cosa vuol dire sensibilità",'''<div class="two"><div><ul>
<li>La sensibilità è il <b>livello minimo</b> di segnale con cui il ricevitore dà un'uscita di una qualità stabilita.</li>
<li>Un numero di sensibilità senza la <b>condizione</b> (SINAD 12 dB, S/N 10 dB, banda, modulazione) non significa nulla.</li>
<li>Si esprime in µV (attenzione PD o EMF!) o in dBm.</li></ul></div><div>
<table><tr><th>Modo</th><th>Criterio più usato</th></tr>
<tr><td class="l">FM</td><td class="l">SINAD 12 dB (o 20 dB di quieting)</td></tr>
<tr><td class="l">AM</td><td class="l">(S+N)/N 10 dB con modulazione 30 %</td></tr>
<tr><td class="l">SSB / CW</td><td class="l">(S+N)/N 10 dB, oppure MDS (3 dB)</td></tr>
<tr><td class="l">Modi digitali</td><td class="l">tasso di errore (BER) a un valore dato</td></tr></table></div></div>''')
D.add("SINAD: che cos'è",'''<div class="two"><div>
<div class="eq">SINAD = 20·log( (S + N + D) / (N + D) )</div>
<ul class="small"><li>S = segnale (il tono demodulato), N = rumore, D = distorsione: tutte tensioni efficaci all'uscita audio.</li>
<li>Il SINAD-metro misura l'audio totale, poi lo ripete con un <b>filtro notch</b> che toglie il tono a 1 kHz: resta solo rumore + distorsione.</li>
<li>12 dB di SINAD significa che rumore e distorsione valgono circa il <b>25 %</b> dell'audio totale: un segnale comprensibile ma rumoroso.</li></ul></div><div>
<h3>Perché proprio 12 dB</h3><ul class="small"><li>È un punto in cui il parlato è intelligibile e la misura è riproducibile.</li>
<li>Tutti i costruttori di radio FM usano questa convenzione: puoi confrontare il tuo apparato con il datasheet.</li>
<li>Alcuni usano 20 dB SINAD o "20 dB quieting" (riduzione del rumore di 20 dB senza modulazione): numeri più alti, ma non direttamente confrontabili.</li></ul></div></div>''')
D.add("Il setup per la misura in FM",f'''<div class="diag" style="width:90%;margin:-6px auto 0">{setup}</div><div class="two" style="align-items:start;gap:30px"><div><ul class="small">
<li>Generatore: frequenza del canale, modulazione 1 kHz, deviazione <b>3 kHz</b> (25 kHz) o <b>1,5 kHz</b> (12,5 kHz).</li>
<li>Ricevitore: squelch aperto, filtri e funzioni speciali (riduzione rumore, CTCSS) disattivati.</li></ul></div><div><ul class="small">
<li>Uscita audio su un carico resistivo uguale all'altoparlante (o sull'altoparlante, se non disturba).</li>
<li>Il SINAD-metro può essere uno strumento dedicato, un analizzatore audio o un programma sul PC con la scheda audio (con un partitore e isolamento).</li></ul></div></div>''')
D.add("La procedura passo per passo",f'''<div class="two"><div><ol>
<li>Livello alto (per esempio −60 dBm): regola il volume per la potenza audio di riferimento.</li>
<li>Scendi di livello finché il SINAD-metro legge <b>12 dB</b>.</li>
<li>Leggi il livello del generatore e sottrai le perdite di cavi e attenuatori.</li>
<li>Ripeti 2–3 volte e fai la media: il SINAD vicino alla soglia oscilla.</li>
<li>Verifica le perdite (leakage): scollegando il cavo, il SINAD deve crollare.</li></ol></div><div class="fig">{svg("sinad.svg")}
<p class="cap">Andamento tipico di un ricevitore FM: dopo la soglia il SINAD cresce rapidamente.</p></div></div>''')
D.add("Esempio di misura in FM",'''<div class="two"><div><ul>
<li>Ricetrasmettitore VHF, 145,500 MHz, deviazione 3 kHz a 1 kHz.</li>
<li>Generatore: SINAD 12 dB ottenuto con il generatore a <b>−114,6 dBm</b>.</li>
<li>Perdite: cavo 0,4 dB + attenuatore 6,0 dB = 6,4 dB.</li></ul>
<div class="eq">−114,6 − 6,4 = −121,0 dBm</div>
<div class="eq">= 0,20 µV PD (0,40 µV EMF)</div></div><div>
<h3>Come leggere il risultato</h3><ul class="small"><li>I ricevitori VHF/UHF FM moderni dichiarano di solito 0,15–0,25 µV per SINAD 12 dB: il nostro è nella norma.</li>
<li>Se il valore misurato è molto peggiore (per esempio 1 µV), cerca: preamplificatore guasto, filtro d'ingresso starato, antenna/commutatore d'antenna danneggiato.</li>
<li>Ripeti a inizio e fine banda: la sensibilità spesso varia di 1–2 dB.</li></ul></div></div>''')
D.add("AM e SSB: S/N 10 dB",'''<div class="two"><div><h3>AM</h3><ul class="small">
<li>Segnale modulato al 30 % con 1 kHz. Misura l'audio con modulazione (S+N) e senza (N): il livello per cui il rapporto vale 10 dB è la sensibilità.</li>
<li>Valori tipici in HF: qualche µV.</li></ul>
<h3>SSB e CW</h3><ul class="small"><li>Portante <b>non modulata</b>, sintonizzata in modo da ottenere un tono di battimento di circa 1 kHz.</li>
<li>Misura l'audio con il segnale (S+N) e togliendolo (N, uscita del generatore spenta o frequenza spostata fuori banda): livello per cui (S+N)/N = 10 dB.</li>
<li>AGC spento (o lento) e guadagno RF al massimo, altrimenti l'AGC "comprime" il risultato.</li></ul></div><div>
<h3>Strumento minimo</h3><ul class="small"><li>Un voltmetro audio true RMS (anche un buon multimetro, se la banda basta) sull'uscita, oppure un programma di analisi audio sul PC.</li>
<li>10 dB di rapporto in tensione corrispondono a un fattore 3,16.</li>
<li>Valori tipici per un buon ricevitore HF in SSB: 0,1–0,2 µV (circa −127…−121 dBm) per 10 dB S/N, dipende da preamplificatore e banda del filtro.</li></ul></div></div>''')
D.add("MDS e cifra di rumore",'''<div class="two"><div><ul>
<li>Il <b>MDS</b> (Minimum Discernible Signal) è il livello che produce un'uscita <b>3 dB</b> sopra il rumore: il segnale è uguale al rumore nel filtro del ricevitore.</li>
<li>Si misura come la S/N, ma con 3 dB al posto di 10 dB; va dichiarata la banda del filtro (spesso 500 Hz in CW).</li></ul>
<div class="eq">MDS ≈ −174 dBm + 10·log(B) + NF</div></div><div>
<h3>Esempi</h3><ul class="small"><li>Filtro 500 Hz, NF 6 dB: −174 + 27 + 6 = <b>−141 dBm</b>.</li>
<li>Filtro 2,4 kHz, NF 8 dB: −174 + 33,8 + 8 = <b>−132 dBm</b>.</li>
<li>Dal MDS misurato ricavi la <b>cifra di rumore</b> del ricevitore: NF = MDS + 174 − 10·log(B).</li>
<li>In HF sotto 14 MHz il rumore dell'antenna è quasi sempre molto più alto di quello del ricevitore: un MDS migliore di −130 dBm serve a poco. In VHF/UHF ogni dB conta.</li></ul></div></div>''')
D.add("Errori tipici nei test di sensibilità",'''<div class="two"><div><ul class="small">
<li><b>Perdite</b> del generatore o dei cavi: il ricevitore riceve per irradiazione, il risultato sembra migliore del vero.</li>
<li>Confondere <b>EMF e PD</b>: 6 dB di differenza.</li>
<li>Non sottrarre <b>cavi e attenuatori</b>.</li>
<li>Livello d'uscita del generatore non verificato ai livelli bassi: l'attenuatore interno può essere fuori di qualche dB.</li></ul></div><div><ul class="small">
<li>Deviazione o modulazione diverse da quelle della norma: risultati non confrontabili.</li>
<li>Squelch, riduzione rumore, CTCSS o AGC attivi.</li>
<li>Rumore ambientale e RF in laboratorio (computer, alimentatori switching): alzano il rumore del ricevitore. Prova con tutto spento e confronta.</li>
<li>Una sola misura vicino alla soglia: ripeti e fai la media.</li></ul></div></div>''')
rows=[("Sensibilità","sempre con la condizione: SINAD 12 dB, S/N 10 dB, banda"),("SINAD","(S+N+D)/(N+D); 12 dB ≈ 25 % di rumore+distorsione"),("FM","1 kHz, 3 kHz di deviazione; tipico 0,15–0,25 µV PD"),("SSB/CW","portante, battimento 1 kHz, AGC spento"),
("MDS","−174 + 10·log(B) + NF"),("Errori","leakage, EMF/PD, perdite non sottratte")]
D.add("Riepilogo",'<table class="sum">'+"".join(f'<tr><td class="l" style="width:200px"><b>{a}</b></td><td class="l">{b}</td></tr>' for a,b in rows)+'</table>')
D.render(); pdf("GEN_Sensibilita_SINAD_MDS_IV3HGA.pdf")
