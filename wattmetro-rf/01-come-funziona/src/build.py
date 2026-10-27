from deck import *
D=Deck("Il wattmetro RF:<br>come funziona","Che cosa vuol dire misurare la potenza a radiofrequenza, wattmetri passanti e terminali, e i sensori: diodo, termocoppia, termistore, bolometro e calorimetro","Il wattmetro RF: come funziona")
D.add("Che cosa misura un wattmetro",'''<div class="two"><div><ul>
<li>In RF non si misura bene "la tensione": cambia lungo la linea se c'è onda stazionaria. Si misura la <b>potenza</b>, che è l'energia trasferita al carico in un secondo.</li></ul>
<div class="eq">P = V<sub>eff</sub>² / R &nbsp;&nbsp; P(dBm) = 10·log(P / 1 mW)</div>
<ul><li>Quasi tutti i wattmetri misurano la <b>potenza media</b>. Alcuni misurano anche il <b>picco</b> o la <b>PEP</b> (potenza di picco dell'inviluppo), importante in SSB.</li></ul></div><div>
<table><tr><th>Potenza</th><th>dBm</th><th>V<sub>eff</sub> su 50 Ω</th></tr>
<tr><td class="l">1 mW</td><td>0</td><td>0,224 V</td></tr><tr><td class="l">1 W</td><td>+30</td><td>7,07 V</td></tr><tr><td class="l">10 W</td><td>+40</td><td>22,4 V</td></tr>
<tr><td class="l">100 W</td><td>+50</td><td>70,7 V</td></tr><tr><td class="l">1 kW</td><td>+60</td><td>224 V</td></tr></table>
<p class="note">Con 100 W su 50 Ω il picco di tensione è 100 V; con un SWR alto, sulla linea si superano facilmente i 200 V.</p></div></div>''')
D.add("Due famiglie: passanti e terminali",'''<div class="two"><div><h3>Wattmetro passante (direzionale)</h3><ul class="small">
<li>Si inserisce <b>tra</b> trasmettitore e carico: la potenza passa e una piccola parte viene campionata.</li>
<li>Misura separatamente la potenza <b>diretta</b> e quella <b>riflessa</b>: da qui si ricava l'SWR.</li>
<li>Regge potenze alte (da pochi watt a kilowatt), precisione tipica qualche % del fondo scala.</li>
<li>Esempi: Bird 43 e simili, wattmetri/rosmetri da stazione.</li></ul></div><div>
<h3>Wattmetro terminale (sensore + carico)</h3><ul class="small"><li>Il sensore <b>è</b> il carico: tutta la potenza viene assorbita e misurata.</li>
<li>Potenze basse (da nW a qualche mW o W), ma precisione molto migliore e banda larghissima.</li>
<li>Per potenze alte si usa con un attenuatore o un accoppiatore calibrato davanti.</li>
<li>Esempi: power meter con sensori a diodo, a termocoppia, a termistore; carichi calorimetrici.</li></ul></div></div>''')
D.add("Il sensore a diodo",f'''<div class="two"><div class="fig">{svg("diode.svg")}</div><div><ul class="small">
<li>Un diodo Schottky raddrizza l'RF e dà una tensione continua.</li>
<li>Sotto circa −20 dBm lavora in <b>zona quadratica</b>: la tensione è proporzionale alla potenza, qualunque sia la forma d'onda. È un vero misuratore di valore efficace.</li>
<li>Sopra circa 0 dBm diventa un <b>rivelatore di picco</b>: la lettura dipende dalla forma d'onda, e con segnali modulati o con armoniche sbaglia.</li>
<li>Pregi: velocissimo, sensibile (fino a −70 dBm), economico.</li>
<li>Difetti: dipende dalla temperatura, va corretto con tabelle; sensibile ai segnali multipli.</li></ul>
<p class="note">Anche le testine dei wattmetri passanti come il Bird 43 usano un diodo, a livello alto: la scala è tarata per una portante sinusoidale.</p></div></div>''')
D.add("Termocoppia, termistore, bolometro",'''<div class="two"><div><h3>Termocoppia</h3><ul class="small">
<li>Un resistore assorbe l'RF e si scalda; una termocoppia genera una tensione proporzionale al calore.</li>
<li><b>Vero valore efficace</b> su tutta la sua gamma: indipendente da modulazione e armoniche.</li>
<li>Gamma tipica da circa −30 a +20 dBm, risposta in frazioni di secondo.</li></ul>
<h3>Calorimetro</h3><ul class="small"><li>Misura il calore prodotto in un carico (acqua, olio, aria). È il metodo più "assoluto", usato per potenze alte e come riferimento.</li></ul></div><div>
<h3>Termistore e bolometro</h3><ul class="small"><li>Un elemento la cui <b>resistenza cambia con la temperatura</b>: termistore (perlina di semiconduttore, coefficiente negativo) o bolometro/barretter (filo sottilissimo, coefficiente positivo).</li>
<li>Un ponte lo mantiene a resistenza costante sostituendo la potenza RF con potenza in <b>continua</b>, che si misura con precisione: è la <b>sostituzione DC</b>.</li>
<li>Lenti e limitati a pochi mW, ma tracciabili alle grandezze elettriche in continua: per decenni sono stati gli standard di laboratorio.</li>
<li>Li vediamo in dettaglio nel modulo dedicato.</li></ul></div></div>''')
D.add("Confronto tra i sensori",'''<table><tr><th>Sensore</th><th>Principio</th><th>Gamma tipica</th><th>Vero RMS</th><th>Velocità</th><th>Uso tipico</th></tr>
<tr><td class="l"><b>Diodo</b></td><td class="l">raddrizzamento</td><td class="l">−70…+20 dBm</td><td class="l">solo in zona quadratica</td><td class="l">molto alta</td><td class="l">power meter moderni, misure di picco</td></tr>
<tr><td class="l"><b>Diodo (testina passante)</b></td><td class="l">campione della linea</td><td class="l">watt…kW</td><td class="l">no, tarato su CW</td><td class="l">alta</td><td class="l">wattmetri da stazione, Bird 43</td></tr>
<tr><td class="l"><b>Termocoppia</b></td><td class="l">calore → tensione</td><td class="l">−30…+20 dBm</td><td class="l">sì</td><td class="l">media</td><td class="l">segnali modulati e complessi</td></tr>
<tr><td class="l"><b>Termistore</b></td><td class="l">sostituzione DC</td><td class="l">µW…10 mW</td><td class="l">sì</td><td class="l">bassa</td><td class="l">riferimenti, trasferimento di taratura</td></tr>
<tr><td class="l"><b>Bolometro</b></td><td class="l">sostituzione DC</td><td class="l">µW…mW</td><td class="l">sì</td><td class="l">media</td><td class="l">storico, laboratorio, SWR a 1 kHz</td></tr>
<tr><td class="l"><b>Calorimetro</b></td><td class="l">calore nel carico</td><td class="l">mW…kW</td><td class="l">sì</td><td class="l">molto bassa</td><td class="l">alta potenza, riferimento assoluto</td></tr></table>
<p class="note" style="margin-top:12px">Valori indicativi: ogni modello ha i suoi limiti, scritti sulla targhetta o nel manuale.</p>''')
D.add("Media, picco e PEP",'''<div class="two"><div><ul>
<li><b>Potenza media</b>: quella che scalda il carico. È ciò che leggono termocoppie, termistori, calorimetri e la maggior parte dei wattmetri.</li>
<li><b>Potenza di picco</b>: il massimo istantaneo, importante per impulsi e radar.</li>
<li><b>PEP</b> (Peak Envelope Power): la potenza media su un ciclo RF nel momento in cui l'inviluppo è al massimo. È la potenza "di targa" dei trasmettitori SSB.</li></ul></div><div>
<table><tr><th>Segnale</th><th>PEP / media</th></tr>
<tr><td class="l">CW, FM (inviluppo costante)</td><td class="l">1 (0 dB)</td></tr>
<tr><td class="l">SSB a due toni</td><td class="l">2 (3 dB)</td></tr>
<tr><td class="l">AM al 100 %</td><td class="l">2,67 (4,3 dB)</td></tr>
<tr><td class="l">SSB con voce</td><td class="l">tipicamente 5–20 (7–13 dB)</td></tr></table>
<p class="note">Un wattmetro a lettura media, in SSB, legge molto meno della PEP: non è un TX "debole". Le formule sono nel modulo sulla potenza del segnale e dello spettro.</p></div></div>''')
D.add("Passanti: come separano diretta e riflessa",'''<div class="two"><div><ul>
<li>Una piccola spira vicino al conduttore centrale raccoglie un segnale <b>magnetico</b> (proporzionale alla corrente) e uno <b>elettrico</b> (proporzionale alla tensione).</li>
<li>Per l'onda diretta i due contributi si sommano, per la riflessa si sottraggono (o viceversa, girando la spira): così la testina "vede" una sola direzione.</li>
<li>Il diodo rivela il segnale e lo strumento è tarato direttamente in watt.</li></ul></div><div>
<h3>Cosa conta in un wattmetro passante</h3><ul class="small"><li><b>Inserzione</b>: SWR e perdita introdotti nella linea, devono essere trascurabili.</li>
<li><b>Direttività</b>: quanto la lettura della riflessa è "pulita" dalla diretta. Limita la misura di SWR molto bassi.</li>
<li><b>Precisione</b>: spesso espressa in % del <b>fondo scala</b>, non della lettura.</li>
<li><b>Banda</b>: la sensibilità della spira cambia con la frequenza; per questo esistono testine diverse per bande diverse.</li></ul></div></div>''')
D.add("Le specifiche da leggere",'''<div class="two"><div><ul>
<li><b>Gamma di frequenza</b> e di potenza (per testina o per sensore).</li>
<li><b>Precisione</b>: in % del fondo scala o della lettura? ±5 % FS a un decimo della scala diventa ±50 % della lettura.</li>
<li><b>Potenza massima</b> continua e di picco, e per quanto tempo.</li>
<li><b>Tipo di rivelazione</b>: media, valore efficace vero, picco, PEP.</li></ul></div><div><ul>
<li><b>SWR e perdita di inserzione</b> (passanti) o SWR del sensore (terminali).</li>
<li><b>Direttività</b> (passanti): decide il minimo SWR misurabile.</li>
<li><b>Cal factor</b> in funzione della frequenza (sensori).</li>
<li><b>Connettori</b>: N, UHF, SMA… e gli adattatori necessari, che aggiungono incertezza.</li></ul></div></div>''')
rows=[("Potenza media","quella che scalda il carico: P = V²/R"),("Passante","diretta e riflessa, alta potenza, % del fondo scala"),("Terminale","il sensore è il carico, bassa potenza, alta precisione"),
("Diodo","quadratico sotto −20 dBm, di picco sopra"),("Termocoppia","vero valore efficace, −30…+20 dBm"),("Termistore e bolometro","sostituzione DC, riferimenti di laboratorio"),("PEP","potenza di inviluppo massima: SSB")]
D.add("Riepilogo",'<table class="sum">'+"".join(f'<tr><td class="l" style="width:300px"><b>{a}</b></td><td class="l">{b}</td></tr>' for a,b in rows)+'</table>')
D.render(); pdf("WM_Come_Funziona_IV3HGA.pdf")
