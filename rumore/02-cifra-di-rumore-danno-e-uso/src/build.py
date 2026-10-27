from deck import *
D=Deck("Il rumore · quando fa male e quando ci serve","Cifra di rumore e temperatura, la formula di Friis, il preamplificatore sul palo, perché in HF il ricevitore non conta quasi mai, e il rumore come strumento di misura","Il rumore · 2")
rows="".join(f"<tr><td style='white-space:nowrap'>{it(a,1)} dB</td><td style='white-space:nowrap'>{b} K</td><td class='l'>{c}</td></tr>" for a,b,c in [(0.5,35,"preamplificatore VHF/UHF di buona qualità"),(1,75,"preamplificatore da palo"),(3,289,"ricevitore VHF/UHF moderno"),(6,865,"ricevitore senza preamplificatore"),(10,"2610","ricevitore HF tipico"),(15,"8880","ricevitore HF con attenuatore inserito")])
D.add("La cifra di rumore",f'''<div class="two"><div><ul>
<li>Ogni stadio aggiunge il suo rumore e quindi <b>peggiora il rapporto S/N</b>. Il fattore di rumore F dice di quanto:</li></ul>
{eq("F = (S/N)<sub>ingresso</sub> / (S/N)<sub>uscita</sub>   NF = 10·log F")}
<ul><li>Un ricevitore ideale ha NF = 0 dB. Uno con NF = 6 dB fa perdere 6 dB di S/N.</li>
<li>In alternativa si usa la <b>temperatura di rumore</b>, più comoda per valori piccoli:</li></ul>
{eq("T = 290 · (F − 1)")}</div><div>
<table><tr><th>NF</th><th>T</th><th>Esempio</th></tr>{rows}</table>
<h3>Sensibilità (MDS)</h3><ul class="small"><li>Il segnale minimo che emerge dal rumore: MDS = −174 + 10·log B + NF.</li>
<li>NF 6 dB, B = 500 Hz: −174 + 27 + 6 = <b>−141 dBm</b>.</li></ul></div></div>''')
D.add("La formula di Friis",f'''<svg viewBox="0 0 1160 160" width="100%" style="max-height:180px">{ARW}
{box(20,45,170,70,"antenna")}{box(270,45,200,70,"stadio 1|F1, G1",fill="#fde8e3")}{box(550,45,200,70,"stadio 2|F2, G2")}{box(830,45,200,70,"stadio 3|F3, G3")}
{ln(190,80,270,80)}{ln(470,80,550,80)}{ln(750,80,830,80)}{ln(1030,80,1110,80)}</svg>
{eq("F<sub>tot</sub> = F1 + (F2 − 1)/G1 + (F3 − 1)/(G1·G2) + …")}
<div class="two"><div><ul><li>Il rumore di ogni stadio viene <b>diviso per il guadagno</b> di tutti quelli che lo precedono.</li>
<li>Conclusione: il primo stadio decide quasi tutto. Basso rumore e guadagno sufficiente, all'inizio della catena.</li></ul></div><div><ul>
<li>Un cavo o un filtro con perdita L è uno stadio con <b>F = L e G = 1/L</b>: 3 dB di cavo prima del ricevitore sono 3 dB di cifra di rumore in più.</li>
<li>Per questo il preamplificatore va messo <b>prima</b> del cavo, non dopo.</li></ul></div></div>''')
D.add("Esempio: il preamplificatore sul palo in 2 metri",f'''<div class="two"><div class="fig">{svg("tsys.svg")}</div><div><ul class="small">
<li>Cavo con 3 dB di perdita, ricevitore con NF 6 dB, preamplificatore con NF 0,8 dB e 20 dB di guadagno.</li></ul>
<table class="small"><tr><th>Configurazione</th><th>NF sistema</th><th>T</th></tr>
<tr><td class="l">nessun preamplificatore</td><td>9,0 dB</td><td>2014 K</td></tr><tr><td class="l">preamplificatore in stazione</td><td>3,9 dB</td><td>423 K</td></tr><tr><td class="l">preamplificatore sul palo</td><td>1,0 dB</td><td>79 K</td></tr></table>
<ul class="small"><li>Il cielo a 145 MHz vale circa 200 K (galattico, ITU-R P.372). Il rapporto S/N migliora di (201 + 2014) / (201 + 79) ≈ <b>9 dB</b> con il preamplificatore sul palo, e solo 5,5 dB con quello in stazione.</li>
<li>9 dB equivalgono a passare da 100 W a quasi 800 W dall'altra parte.</li></ul></div></div>''')
D.add("In HF il ricevitore quasi non conta",f'''<div class="two"><div class="fig">{svg("who.svg")}</div><div><ul class="small">
<li>Il rumore totale in ingresso è la somma, in lineare, di quello esterno e di quello del ricevitore:</li></ul>
{eq("N<sub>tot</sub> ∝ Fa + F − 1")}
<ul class="small"><li>In 20 metri, zona residenziale: Fa = 40,6 dB. Un ricevitore con NF 9 dB peggiora il fondo di <b>0,003 dB</b>.</li>
<li>Il preamplificatore in HF serve solo a far salire il rumore insieme al segnale, e peggiora l'intermodulazione. Spesso conviene usare l'<b>attenuatore</b>.</li>
<li>Sopra i 21–28 MHz, in località tranquille, e soprattutto in VHF/UHF, la curva esterna scende sotto la NF del ricevitore: lì il preamplificatore e la cifra di rumore tornano a contare.</li></ul></div></div>''')
D.add("Quando il rumore è dannoso",'''<div class="grid3"><div class="card"><h3>Limita la sensibilità</h3><p>Sotto il fondo di rumore un segnale non si decodifica. In HF quasi sempre è il rumore esterno, in VHF/UHF anche quello del ricevitore.</p></div>
<div class="card"><h3>QRM locale</h3><p>Alimentatori switching, LED, inverter: alzano il fondo di 10–30 dB. Si cercano con una radio portatile e un'antenna a loop, e si curano alla fonte (ferriti, filtri, sostituzione).</p></div>
<div class="card"><h3>Reciprocal mixing</h3><p>Il rumore di fase dell'oscillatore locale trasferisce sul canale ascoltato il rumore attorno a un segnale forte vicino: il fondo sale quando il vicino trasmette.</p></div>
<div class="card"><h3>Rumore del trasmettitore</h3><p>Anche un trasmettitore emette rumore a larga banda attorno alla portante. Nei field day e nei siti condivisi può coprire le stazioni vicine.</p></div>
<div class="card"><h3>Rumore negli strumenti</h3><p>Il DANL dell'analizzatore di spettro e il rumore del generatore limitano le misure di filtri e prodotti spuri.</p></div>
<div class="card"><h3>Rumore nei modi digitali</h3><p>Ogni modo ha un S/N minimo (FT8 circa −21 dB in 2,5 kHz): sotto quello la decodifica fallisce di colpo.</p></div></div>''')
D.add("Quando lo usiamo",'''<div class="grid3"><div class="card"><h3>Misurare la cifra di rumore</h3><p>Una sorgente di rumore calibrata acceso/spento: metodo del fattore Y.</p></div>
<div class="card"><h3>Generatore di spazzata "povero"</h3><p>Un generatore di rumore a larga banda e un analizzatore di spettro: la risposta di un filtro in un colpo solo.</p></div>
<div class="card"><h3>Ponte di rumore</h3><p>Il noise bridge misura l'impedenza dell'antenna col ricevitore: si cerca il minimo di rumore in cuffia.</p></div>
<div class="card"><h3>Il Sole come sorgente</h3><p>Il rumore solare verifica puntamento e sensibilità delle antenne VHF/UHF e microonde, soprattutto in EME.</p></div>
<div class="card"><h3>Dither</h3><p>Un po' di rumore aggiunto prima dell'ADC elimina le armoniche di quantizzazione negli SDR.</p></div>
<div class="card"><h3>Test di vita del ricevitore</h3><p>Colleghi l'antenna e il fondo sale: la catena riceve e il rumore esterno domina. Se non cambia nulla, c'è un problema.</p></div></div>''')
D.add("Il metodo del fattore Y",f'''<div class="two"><div><ul>
<li>Una sorgente di rumore (diodo a valanga calibrato) ha un <b>ENR</b> noto: di quanti dB il suo rumore acceso supera kT₀B.</li>
<li>Si collega al ricevitore e si legge il rumore in uscita con la sorgente <b>spenta</b> e <b>accesa</b>. Il rapporto è il fattore Y:</li></ul>
{eq("NF = ENR − 10·log(Y − 1)")}</div><div>
<h3>Esempio</h3><ul><li>Sorgente con ENR = 15 dB.</li><li>Il rumore in uscita sale di 6 dB quando la si accende: Y = 3,98.</li>
<li>NF = 15 − 10·log(2,98) = 15 − 4,7 = <b>10,3 dB</b>.</li></ul>
<h3>Consigli</h3><ul class="small"><li>Il rivelatore deve essere a vero valore efficace o in potenza, con molte medie: lo S-meter di una radio non va bene.</li>
<li>Usa una banda di misura nota e stabile e un AGC spento.</li>
<li>Per NF molto basse serve un ENR basso (5–6 dB), altrimenti Y è grande e l'errore cresce.</li></ul></div></div>''')
D.add("Il rumore come generatore di spazzata",f'''<div class="two"><div class="fig">{svg("filt.svg")}</div><div><ul>
<li>Un generatore di rumore a larga banda (anche autocostruito con uno zener) contiene <b>tutte le frequenze</b> nello stesso momento.</li>
<li>Rumore → filtro → analizzatore di spettro: la traccia mostra direttamente la risposta del filtro.</li>
<li>Una sola spazzata è "sporca": la media su molte spazzate (o la banda video ridotta) la rende leggibile.</li>
<li>La dinamica è limitata dalla differenza tra il livello del rumore e il DANL dell'analizzatore: qui circa 60 dB.</li>
<li>Utile per allineare filtri di banda, trappole, cavità, duplexer quando non si ha un tracking generator.</li></ul></div></div>''')
D.add("Il dither: rumore aggiunto apposta",f'''<div class="fig" style="width:92%">{svg("dither.svg")}</div><div class="two" style="gap:30px"><div><ul class="small">
<li>Un segnale di appena 1,3 LSB, quantizzato direttamente, diventa un'onda quadra a gradini: compaiono <b>armoniche</b> che non esistono nel segnale reale.</li></ul></div><div><ul class="small">
<li>Aggiungendo un rumore casuale di circa 1 LSB l'errore di quantizzazione diventa rumore: il fondo sale un po', le righe spurie spariscono. Molti SDR lo fanno con un'opzione "dither".</li></ul></div></div>''')
D.add("Il Sole, il ponte di rumore e il test dell'antenna",'''<div class="grid3"><div class="card"><h3>Rumore solare</h3><p>Puntando un'antenna direttiva sul Sole il rumore in uscita sale di qualche dB rispetto al cielo freddo.</p><p>Più è alto questo salto, migliori sono guadagno e cifra di rumore del sistema. Le stazioni EME lo usano come verifica periodica, confrontandolo con il flusso solare del giorno.</p></div>
<div class="card"><h3>Ponte di rumore</h3><p>Un generatore di rumore alimenta un ponte con l'antenna su un ramo e un condensatore e una resistenza variabili sull'altro.</p><p>Quando il rumore in cuffia è minimo, i comandi indicano la parte resistiva e reattiva dell'impedenza. Funziona col solo ricevitore, senza trasmettere.</p></div>
<div class="card"><h3>Il test più semplice</h3><p>Ricevitore acceso, antenna scollegata: ascolta il fondo. Collega l'antenna: il fondo deve salire.</p><p>Se sale molto, il sistema è limitato dal rumore esterno (bene in HF). Se non sale, controlla cavo, connettori, preamplificatore e antenna.</p></div></div>''')
r=[("NF","di quanto il ricevitore peggiora S/N; T = 290·(F − 1)"),("MDS","−174 + 10·log B + NF"),("Friis","il primo stadio decide; il cavo prima del preamp costa caro"),("2 m","preamp sul palo: +9 dB di S/N nell'esempio"),("HF","domina il rumore esterno: meglio attenuatore che preamp"),("Dannoso","sensibilità, QRM, reciprocal mixing, rumore TX"),("Utile","fattore Y, spazzata con rumore, ponte, Sole, dither")]
D.add("Riepilogo",'<table class="sum">'+"".join(f'<tr><td class="l" style="width:160px"><b>{a}</b></td><td class="l">{b}</td></tr>' for a,b in r)+'</table>')
D.render(); pdf("Rumore_2_Cifra_di_rumore_IV3HGA.pdf")
