import math
from deck import *
D=Deck("Le misure<br>con l'oscilloscopio","Ampiezza, frequenza, tempo di salita, fase, modalità XY, modulazione AM con inviluppo e trapezio, FFT e correnti: come farle bene e quanto fidarsi","L'oscilloscopio: le misure")
D.add("Cursori e misure automatiche",'''<div class="two"><div><h3>Misure automatiche</h3><ul class="small">
<li>Veloci e comode: Vpp, Vrms, frequenza, tempo di salita, duty cycle, fase…</li>
<li>Lavorano sui <b>dati in memoria</b>, non sui pixel: sono più precise dell'occhio, se il segnale occupa bene lo schermo.</li>
<li>Su segnali rumorosi, con più fronti o tagliati dallo schermo possono dare numeri assurdi.</li>
<li>Usa le <b>statistiche</b> (media, minimo, massimo, deviazione) e il <b>gating</b> (misura solo tra due cursori).</li></ul></div><div>
<h3>Cursori</h3><ul class="small"><li>Due linee verticali (tempo) o orizzontali (tensione) che metti tu: ΔV, Δt e 1/Δt.</li>
<li>Indispensabili quando il punto da misurare lo scegli tu: un gradino, un'oscillazione, un ritardo tra eventi.</li>
<li>Regola d'oro: controlla <b>sempre</b> una misura automatica con un'occhiata ai cursori o al reticolo, almeno la prima volta.</li></ul></div></div>''')
D.add("Ampiezza",'''<div class="two"><div><table><tr><th>Misura</th><th>Che cos'è</th></tr>
<tr><td class="l"><b>Vpp</b></td><td class="l">dal minimo al massimo assoluto (rumore e spike compresi)</td></tr>
<tr><td class="l"><b>Vampiezza</b></td><td class="l">tra i livelli "alto" e "basso" stabili (top − base)</td></tr>
<tr><td class="l"><b>Vrms</b></td><td class="l">valore efficace vero, da calcolare su un numero intero di periodi</td></tr>
<tr><td class="l"><b>Vmedia</b></td><td class="l">componente continua del segnale</td></tr></table></div><div>
<div class="eq">sinusoide: V<sub>rms</sub> = V<sub>p</sub> / √2 = V<sub>pp</sub> / (2√2)</div>
<ul class="small"><li>Fai occupare al segnale <b>almeno metà schermo</b> in verticale: con un ADC a 8 bit, un segnale di una sola divisione usa circa 30 livelli.</li>
<li>Precisione tipica in DC di un oscilloscopio: qualche % del fondo scala. Per tensioni precise usa un multimetro.</li>
<li>Vrms con una sonda 10× scompensata o con banda insufficiente è sbagliato anche se il numero sembra stabile.</li></ul></div></div>''')
D.add("Frequenza, periodo, duty cycle",'''<div class="two"><div><ul>
<li><b>Periodo</b>: tempo tra due fronti uguali; f = 1/T.</li>
<li>Misura su <b>più periodi</b> e dividi: l'errore di lettura si riduce in proporzione.</li>
<li>Molti strumenti hanno un <b>contatore</b> sul trigger, molto più preciso della misura sulla traccia.</li>
<li><b>Duty cycle</b> = tempo alto / periodo, misurato a metà ampiezza.</li></ul></div><div>
<h3>Attenzione</h3><ul class="small"><li>La precisione dipende dalla base dei tempi dello strumento (tipicamente qualche decina di ppm): per tarare un oscillatore usa un frequenzimetro con riferimento buono.</li>
<li>Su segnali rumorosi il trigger "salta": usa il filtro sul trigger o il limite di banda.</li>
<li>Con segnali modulati o burst misura dentro il burst, con il gating.</li></ul></div></div>''')
D.add("Tempo di salita",f'''<div class="two"><div class="fig">{svg("rise.svg")}</div><div>
<ul class="small"><li>Si misura tra il <b>10 % e il 90 %</b> dell'ampiezza (a volte tra 20 e 80 %).</li>
<li>Quello che vedi è la combinazione del fronte vero con i tempi di salita di oscilloscopio e sonda:</li></ul>
{eq("t<sub>misurato</sub> ≈ √(t<sub>vero</sub>² + t<sub>osc</sub>² + t<sub>sonda</sub>²)")}
<p class="note">Esempio: misuri 4 ns con un sistema oscilloscopio + sonda da 2 ns → t<sub>vero</sub> ≈ √(16 − 4) = {it(math.sqrt(12),2)} ns. Se t<sub>misurato</sub> è vicino a quello dello strumento, stai misurando lo strumento, non il segnale.</p>
<ul class="small"><li>Usa la molla di massa corta: il cavetto lungo aggiunge oscillazioni e falsa il 90 %.</li></ul></div></div>''')
D.add("Fase tra due segnali e modalità XY",f'''<div class="fig" style="width:94%">{svg("phase.svg")}</div><div class="two" style="align-items:start;gap:30px"><div>
{eq("φ = 360° · Δt / T")}<p class="note" style="margin-top:2px">Due canali, stesso trigger, Δt tra due passaggi per lo zero nello stesso verso. Esempio: 1 MHz (T = 1 µs) e Δt = 167 ns → 60°.</p></div><div>
{eq("XY: sin φ = B / A")}<p class="note" style="margin-top:2px">Un canale sull'asse X e uno sull'asse Y: due sinusoidi della stessa frequenza disegnano un'ellisse (Lissajous). B è l'intersezione con l'asse verticale, A l'altezza totale. Con frequenze diverse, il rapporto si legge contando i "lobi" sui lati.</p></div></div>''')
D.add("Modulazione AM: inviluppo e trapezio",f'''<div class="fig" style="width:94%">{svg("am.svg")}</div><div class="two" style="align-items:start;gap:30px"><div>
{eq("m = (V<sub>max</sub> − V<sub>min</sub>) / (V<sub>max</sub> + V<sub>min</sub>)")}<p class="note" style="margin-top:2px">Dall'inviluppo (picco-picco massimo e minimo) o dal trapezio (lato lungo e lato corto). Nell'esempio V<sub>max</sub> = 1,5, V<sub>min</sub> = 0,5 → m = 50 %.</p></div><div><ul class="small">
<li>Il <b>trapezio</b> (audio su X, RF su Y) mostra anche la <b>linearità</b>: lati dritti = modulatore lineare; lati curvi = distorsione; una punta che tocca lo zero = sovramodulazione in arrivo.</li>
<li>La RF va presa da un prelievo o attenuatore, mai dall'uscita del TX diretta.</li></ul></div></div>''')
D.add("La FFT dell'oscilloscopio",'''<div class="two"><div><ul>
<li>La funzione FFT trasforma la traccia in uno spettro: utile per vedere armoniche, rumore di commutazione, disturbi a frequenze note.</li>
<li><b>Risoluzione</b> in frequenza = sample rate / numero di punti: più lunga la finestra di tempo, più fine la risoluzione.</li>
<li><b>Finestra</b>: Hann/Hanning per uso generale, flat-top per leggere bene le ampiezze, rettangolare solo per transitori.</li></ul></div><div>
<h3>Limiti rispetto a un analizzatore</h3><ul class="small"><li>Con un ADC a 8 bit la dinamica è di circa <b>50–60 dB</b>: le armoniche a −60 dBc di un TX non si vedono.</li>
<li>Niente preselezione: segnali forti fuori dalla banda d'interesse creano aliasing nello spettro.</li>
<li>Ottima per una prima occhiata o per segnali audio e di bassa frequenza; per misure RF serie usa l'analizzatore di spettro.</li></ul></div></div>''')
D.add("Correnti e potenza",'''<div class="two"><div><ul>
<li><b>Resistenza di shunt</b>: una piccola resistenza in serie, misuri la tensione ai suoi capi: I = V / R. Meglio se lo shunt è sul lato massa, così la misura è riferita a terra.</li>
<li><b>Sonda di corrente</b>: pinza a trasformatore (solo AC) o a effetto Hall (anche DC). Va azzerata (degauss) prima dell'uso.</li></ul></div><div>
<h3>Potenza istantanea</h3><ul class="small"><li>Con tensione su un canale e corrente sull'altro, la funzione <b>math</b> calcola V × I punto per punto.</li>
<li>Utile per vedere le perdite di commutazione di un MOSFET o la corrente di spunto di un alimentatore.</li>
<li>Attenzione al <b>ritardo</b> diverso tra sonde (deskew): pochi ns di differenza falsano la potenza sui fronti veloci.</li></ul></div></div>''')
rows=[("Misure automatiche","comode, ma da verificare con cursori"),("Ampiezza","almeno metà schermo; Vrms = Vp/√2 per i sinusoidi"),("Tempo di salita","t<sub>mis</sub>² = t<sub>vero</sub>² + t<sub>sistema</sub>²"),("Fase","φ = 360°·Δt/T; in XY sin φ = B/A"),
("AM","m = (Vmax − Vmin)/(Vmax + Vmin)"),("FFT","~50–60 dB di dinamica: prima occhiata, non analizzatore")]
D.add("Riepilogo",'<table class="sum">'+"".join(f'<tr><td class="l" style="width:250px"><b>{a}</b></td><td class="l">{b}</td></tr>' for a,b in rows)+'</table>')
D.render(); pdf("OSC_Misure_Classiche_IV3HGA.pdf")
