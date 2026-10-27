from deck import *
D=Deck("Misurare<br>la tensione","Il collegamento in parallelo, l'impedenza d'ingresso e l'effetto di carico, tensioni fantasma e LoZ, valore medio e true RMS, fattore di cresta e banda, ripple con il multimetro ed esempi pratici","Il multimetro: la tensione")
D.add("Come si misura una tensione",'''<div class="two"><div><ul>
<li>La tensione si misura <b>in parallelo</b>: i puntali sui due punti tra cui vuoi conoscere la differenza di potenziale.</li>
<li>Puntale nero in COM, rosso in V Ω. In DC un segno meno indica solo che hai invertito i puntali.</li>
<li>Il multimetro a batteria è <b>flottante</b>: a differenza dell'oscilloscopio da banco puoi misurare tra due punti qualsiasi, entro la sua categoria di sicurezza.</li></ul></div><div>
<h3>DC, AC e mV</h3><ul class="small"><li><b>V DC</b>: tensioni continue, batterie, alimentatori, polarizzazioni.</li>
<li><b>V AC</b>: tensioni alternate a bassa frequenza (rete, trasformatori, audio).</li>
<li><b>mV</b>: portata separata per tensioni piccole (shunt, termocoppie, cadute su contatti), spesso con risoluzione di 0,01–0,1 mV.</li></ul></div></div>''')
D.add("L'impedenza d'ingresso e l'effetto di carico",f'''<div class="two"><div class="fig">{svg("loading.svg")}</div><div>
{eq("V<sub>letta</sub> = V · R<sub>in</sub> / (R<sub>in</sub> + R<sub>sorgente</sub>)")}
<ul class="small"><li>Il multimetro è una resistenza (10 MΩ per i digitali) in parallelo al punto misurato: assorbe un po' di corrente e abbassa la tensione.</li>
<li>Se la resistenza della sorgente è meno di 1/100 di R<sub>in</sub>, l'errore è sotto l'1 %.</li></ul>
<h3>Esempio: partitore da 2 × 1 MΩ su 10 V</h3><ul class="small"><li>Valore vero al centro: 5,00 V (sorgente equivalente: 500 kΩ).</li>
<li>Digitale da 10 MΩ: <b>4,76 V</b>. Analogico 20 kΩ/V sulla portata 10 V (200 kΩ): <b>1,43 V</b>!</li></ul></div></div>''')
D.add("Dove l'effetto di carico ti inganna",'''<div class="two"><div><ul class="small">
<li><b>Polarizzazioni</b> di base o di gate attraverso resistenze da centinaia di kΩ.</li>
<li><b>Tensioni di sintonia</b> dei varicap nei VFO e nei PLL: spesso arrivano da resistenze alte, e la frequenza si sposta mentre misuri.</li>
<li>Linee <b>AGC</b> e uscite di rivelatori ad alta impedenza.</li>
<li><b>Partitori ad alta tensione</b> con resistenze da molti MΩ.</li>
<li>Ingressi CMOS lasciati flottanti.</li></ul></div><div>
<h3>Come difendersi</h3><ul class="small"><li>Misura dal lato a bassa impedenza (all'uscita del buffer, non sulla resistenza di polarizzazione).</li>
<li>Se la lettura cambia sensibilmente passando da un multimetro all'altro, o aggiungendo in parallelo un secondo strumento, c'è effetto di carico.</li>
<li>Con una misura nota (per esempio aggiungendo in parallelo 10 MΩ) puoi stimare la resistenza della sorgente e correggere.</li>
<li>Per misure veramente ad alta impedenza servono strumenti elettrometrici (oltre 1 GΩ).</li></ul></div></div>''')
D.add("Tensioni fantasma e LoZ",'''<div class="two"><div><ul>
<li>Un conduttore scollegato, ma che corre accanto a cavi in tensione, prende tensione per accoppiamento capacitivo: con 10 MΩ ne leggi decine di volt.</li>
<li>La funzione <b>LoZ</b> mette in parallelo all'ingresso qualche kΩ: la tensione "fantasma" crolla a zero, una tensione vera resta.</li>
<li>È lo strumento giusto per decidere se un conduttore è davvero alimentato.</li></ul></div><div>
<h3>Quando NON usarla</h3><ul class="small"><li>Su circuiti elettronici delicati: qualche kΩ in parallelo è un carico pesante, può disturbare o danneggiare.</li>
<li>Su sorgenti ad alta impedenza dove vuoi la tensione a vuoto.</li>
<li>Su circuiti protetti da differenziale: la corrente di LoZ verso terra, in alcuni casi, può farlo scattare.</li></ul></div></div>''')
D.add("AC: valore medio contro true RMS",f'''<div class="two"><div class="fig">{svg("rms.svg")}</div><div><ul class="small">
<li>Un multimetro "a valore medio" misura il valore medio della tensione raddrizzata e lo moltiplica per 1,111 (π / 2√2), il rapporto RMS/medio di una <b>sinusoide</b>.</li>
<li>Con forme d'onda diverse il rapporto cambia: <b>+11 %</b> su un'onda quadra, <b>−4 %</b> su una triangolare, fino a <b>−33 %</b> su un treno di impulsi stretti.</li>
<li>Correnti di raddrizzatori con condensatore, alimentatori switching, inverter, dimmer, PWM: tutti casi in cui serve il <b>true RMS</b>.</li></ul>
<p class="note">Il true RMS calcola √(media di v²): è il valore che scalda davvero un carico resistivo, qualunque sia la forma d'onda.</p></div></div>''')
D.add("Fattore di cresta e banda in AC",'''<div class="two"><div><h3>Fattore di cresta</h3><ul class="small">
<li>È il rapporto picco / RMS: 1,41 per la sinusoide, 1 per l'onda quadra, 3 o più per gli impulsi.</li>
<li>Anche un true RMS ha un limite (per esempio 3 a fondo scala): oltre, i picchi saturano il convertitore e la lettura è bassa.</li>
<li>Con segnali impulsivi usa una portata più alta, così i picchi restano nel campo.</li></ul></div><div>
<h3>Banda</h3><ul class="small"><li>La precisione AC vale solo in una gamma di frequenze: nei modelli economici spesso fino a qualche centinaio di Hz o 1 kHz, nei migliori fino a decine o centinaia di kHz.</li>
<li>L'audio di un trasmettitore si misura (con il modello adatto), la <b>RF no</b>: per la RF serve una sonda a diodo (lezione sui trucchi).</li>
<li>Sotto qualche decina di Hz la lettura AC diventa instabile o sbagliata.</li></ul></div></div>''')
D.add("Il ripple con il multimetro",'''<div class="two"><div><ul>
<li>Nella maggior parte dei multimetri la funzione <b>V AC</b> ha un condensatore in serie: blocca la continua e misura solo la parte alternata (verifica sul manuale: alcuni modelli hanno una funzione AC+DC separata).</li>
<li>Puntali sui capi del condensatore di filtro, funzione V AC: leggi il <b>valore efficace del ripple</b>.</li></ul>
<div class="eq">dente di sega: V<sub>RMS</sub> = V<sub>pp</sub> / (2·√3) ≈ 0,29 · V<sub>pp</sub></div></div><div>
<h3>Esempio</h3><ul class="small"><li>Alimentatore lineare, 1 V picco-picco di ripple a 100 Hz (vedi la lezione sul ripple con l'oscilloscopio).</li>
<li>Un true RMS legge circa <b>0,29 V</b> AC.</li>
<li>Non vedi la forma d'onda, ma è un ottimo controllo rapido: confronta con un alimentatore sano o con il valore di progetto. Un ripple che cresce indica condensatori che invecchiano.</li>
<li>Su ripple a centinaia di kHz (switching) il multimetro non ha banda sufficiente: lì serve l'oscilloscopio.</li></ul></div></div>''')
D.add("Esempi pratici dalla stazione",'''<div class="two"><div><h3>Alimentatore da 13,8 V</h3><ul class="small">
<li>Misura la tensione a vuoto e poi <b>sotto carico</b> (in trasmissione): un alimentatore sano perde pochi decimi di volt.</li>
<li>Misura anche ai morsetti del ricetrasmettitore: la differenza è la caduta sui cavi e sui connettori (dettagli nella lezione sui trucchi).</li></ul>
<h3>Polarizzazione di un finale</h3><ul class="small"><li>Tensione di gate o di base a riposo: misura sul punto a bassa impedenza (uscita del regolatore di bias), non sulla resistenza alta.</li></ul></div><div>
<h3>Tensione di sintonia di un VFO o PLL</h3><ul class="small"><li>Se la frequenza si sposta quando appoggi il puntale, stai caricando il circuito: misura a valle di un buffer o accetta l'errore sapendo che c'è.</li></ul>
<h3>Batterie</h3><ul class="small"><li>La tensione a vuoto di una batteria dice poco sulla sua salute: misurala sotto carico (o calcola la resistenza interna, lezione sui trucchi).</li></ul></div></div>''')
rows=[("Parallelo","la tensione si misura ai capi, con lo strumento flottante"),("Carico","V<sub>letta</sub> = V·R<sub>in</sub>/(R<sub>in</sub>+R<sub>s</sub>): attenzione oltre ~100 kΩ"),("LoZ","elimina le tensioni fantasma, ma carica il circuito"),("True RMS","necessario con forme non sinusoidali"),("Banda AC","solo bassa frequenza: niente RF"),("Ripple","V AC sul condensatore: ~0,29·V<sub>pp</sub> per il dente di sega")]
D.add("Riepilogo",'<table class="sum">'+"".join(f'<tr><td class="l" style="width:160px"><b>{a}</b></td><td class="l">{b}</td></tr>' for a,b in rows)+'</table>')
D.render(); pdf("MM_Tensione_IV3HGA.pdf")
