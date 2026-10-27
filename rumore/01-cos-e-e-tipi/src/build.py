from deck import *
D=Deck("Il rumore · cos'è e da dove viene","Che cosa intendiamo per rumore, il rumore termico e il famoso −174 dBm/Hz, gli altri rumori dei componenti, bianco e rosa, gaussiano e impulsivo, il rumore che arriva dall'antenna","Capitolo 11 · il rumore · 1")
D.add("Che cosa intendiamo per rumore",'''<div class="two"><div><ul>
<li>Il <b>rumore</b> è un segnale <b>casuale</b>: non porta informazione e non si può prevedere istante per istante.</li>
<li>Non si descrive con un'ampiezza, ma con una <b>potenza media</b> in una certa banda, o con una <b>densità</b> (dBm/Hz).</li>
<li>Si somma a tutto quello che riceviamo: è il "pavimento" sotto il quale un segnale non si distingue più.</li></ul></div><div>
<h3>Quello che conta è il rapporto</h3><ul><li>Un segnale da −120 dBm è ottimo se il rumore è a −140 dBm, e inutile se il rumore è a −100 dBm.</li>
<li>Il parametro che decide se un collegamento funziona è il <b>rapporto segnale/rumore</b> (S/N, SNR, C/N, Eb/N0).</li></ul>
<div class="note">Due grandi famiglie: il rumore <b>interno</b>, generato dai componenti del ricevitore, e il rumore <b>esterno</b>, che entra dall'antenna insieme al segnale.</div></div></div>''')
rows="".join(f"<tr><td class='l'>{a}</td><td>{b}</td><td>{c}</td></tr>" for a,b,c in [("CW","500 Hz","−147,0 dBm"),("SSB","2,4 kHz","−140,2 dBm"),("FM a banda stretta","12,5 kHz","−133,0 dBm"),("Broadcast FM","200 kHz","−121,0 dBm"),("1 MHz","1 MHz","−114,0 dBm"),("LTE","20 MHz","−101,0 dBm")])
D.add("Il rumore termico: kTB",f'''<div class="two"><div><ul>
<li>Gli elettroni in un conduttore si muovono a caso per l'agitazione termica: ogni resistenza a temperatura T genera rumore.</li>
<li>La potenza disponibile su un carico adattato è:</li></ul>
{eq("P = k · T · B")}
<ul class="small"><li>k = 1,38·10⁻²³ J/K (Boltzmann), T in kelvin, B in hertz.</li>
<li>A T₀ = 290 K: kT = 4·10⁻²¹ W/Hz = <b>−174 dBm/Hz</b>. Il numero da ricordare.</li>
<li>Non dipende dalla frequenza (è "bianco") né dal valore della resistenza.</li></ul></div><div>
<h3>Il pavimento per ogni banda</h3><table><tr><th>Modo</th><th>Banda</th><th>−174 + 10·log B</th></tr>{rows}</table>
<p class="note">Banda 10 volte più stretta = 10 dB di rumore in meno. Per questo il CW e i modi digitali stretti arrivano dove la fonia non arriva.</p></div></div>''')
D.add("La tensione di rumore di una resistenza",f'''<div class="two"><div><ul>
<li>Vista come tensione a vuoto (formula di Johnson-Nyquist):</li></ul>
{eq("v<sub>n</sub> = √(4·k·T·R·B)")}
<h3>Esempio</h3><ul><li>R = 50 Ω, T = 290 K, B = 1 MHz:</li>
<li>v<sub>n</sub> = √(4 · 1,38·10⁻²³ · 290 · 50 · 10⁶) ≈ <b>0,89 µV</b> a vuoto.</li>
<li>Su un carico adattato da 50 Ω ne arriva la metà, 0,45 µV: (0,45 µV)² / 50 Ω = 4·10⁻¹⁵ W = <b>−114 dBm</b>. Torna con kTB.</li></ul></div><div>
<h3>Conseguenze pratiche</h3><ul><li>Il rumore dipende dalla <b>temperatura</b>: raffreddare il primo stadio (come nei radiotelescopi) lo riduce.</li>
<li>Una resistenza da 10 kΩ ha più tensione di rumore di una da 50 Ω, ma la stessa potenza disponibile: conta l'adattamento.</li>
<li>Un carico fittizio a temperatura ambiente è una sorgente di rumore "a 290 K": è il riferimento per misurare la cifra di rumore.</li></ul></div></div>''')
D.add("Gli altri rumori dei componenti",'''<div class="grid3"><div class="card"><h3>Rumore shot</h3><p>La corrente è fatta di cariche discrete che attraversano una giunzione in istanti casuali.</p>
<div class="eq">i<sub>n</sub> = √(2·q·I·B)</div><p>1 mA in 1 MHz: ≈ 18 nA. Bianco, come il termico.</p></div>
<div class="card"><h3>Rumore flicker (1/f)</h3><p>Domina alle basse frequenze in transistor, operazionali e resistenze a impasto. La densità cresce scendendo in frequenza.</p><p>Importante in audio, nei ricevitori a conversione diretta e negli oscillatori.</p></div>
<div class="card"><h3>Rumore a valanga</h3><p>Uno zener o una giunzione base-emettitore in breakdown generano molto rumore a larga banda.</p><p>È il cuore dei generatori di rumore autocostruiti.</p></div>
<div class="card"><h3>Rumore di fase</h3><p>Le piccole fluttuazioni di fase di un oscillatore allargano la sua riga in un "piedistallo".</p><p>Nel ricevitore causa il <b>reciprocal mixing</b>: un segnale forte vicino alza il fondo.</p></div>
<div class="card"><h3>Rumore di quantizzazione</h3><p>Un ADC arrotonda ogni campione al livello più vicino.</p><div class="eq">SNR = 6,02·N + 1,76 dB</div><p>14 bit: ≈ 86 dB; 16 bit: ≈ 98 dB.</p></div>
<div class="card"><h3>Rumore del ricevitore</h3><p>Tutti questi contributi insieme si riassumono in un solo numero: la <b>cifra di rumore</b> (lezione 2).</p></div></div>''')
D.add("Bianco e rosa",f'''<div class="two"><div class="fig">{svg("color.svg")}</div><div><ul>
<li><b>Bianco</b>: la stessa potenza in ogni hertz di banda. Termico e shot sono bianchi su tutte le frequenze che ci interessano.</li>
<li><b>Rosa</b>: la densità cala di 3 dB per ottava (1/f). Stessa potenza in ogni ottava: per questo si usa per tarare gli impianti audio.</li>
<li>Un amplificatore reale ha un fondo bianco più una parte 1/f sotto una frequenza d'angolo, da qualche hertz a qualche kilohertz.</li>
<li>Nei ricevitori a conversione diretta e negli SDR "zero-IF" il rumore 1/f finisce proprio vicino alla frequenza zero: per questo spesso si sintonizza leggermente fuori centro.</li></ul></div></div>''')
D.add("Gaussiano o impulsivo",f'''<div class="fig" style="width:86%">{svg("types.svg")}</div><div class="two" style="gap:30px"><div><ul class="small">
<li><b>Gaussiano</b>: ampiezze distribuite a campana, senza picchi isolati. È il rumore termico, il soffio che senti con l'antenna scollegata.</li></ul></div><div><ul class="small">
<li><b>Impulsivo</b>: brevi picchi molto più alti del fondo (fulmini, accensioni dei motori, alimentatori, recinti elettrici). Un noise blanker lo taglia; sul gaussiano non serve.</li></ul></div></div>''')
D.add("Il rumore che arriva dall'antenna",'''<div class="grid3"><div class="card"><h3>Atmosferico (QRN)</h3><p>Le scariche dei fulmini di tutto il mondo si propagano via ionosfera. Domina in onde lunghe, medie e nelle bande basse HF, soprattutto d'estate e di notte.</p></div>
<div class="card"><h3>Galattico</h3><p>Il rumore della Via Lattea. Arriva solo sopra la frequenza critica della ionosfera (≈ 10 MHz e oltre). È il limite delle stazioni VHF in luoghi tranquilli.</p></div>
<div class="card"><h3>Solare e del cielo</h3><p>Il Sole è una sorgente di rumore intensa, utile per tarare le antenne (lezione 2). Il terreno "caldo" a 290 K aggiunge rumore quando l'antenna lo vede.</p></div>
<div class="card"><h3>Artificiale (QRM)</h3><p>Alimentatori switching, LED, inverter fotovoltaici, PLC, VDSL, motori, caricabatterie. Oggi è quasi sempre il <b>limite principale</b> in HF.</p></div>
<div class="card"><h3>Del ricevitore</h3><p>Il rumore generato dentro la radio, sommato a quello esterno. In HF è quasi sempre trascurabile; in VHF/UHF può dominare.</p></div>
<div class="card"><h3>Da intermodulazione</h3><p>Prodotti dei segnali forti che si comportano come rumore di fondo (lezione sull'intermodulazione).</p></div></div>''')
D.add("Quanto rumore esterno c'è: ITU-R P.372",f'''<div class="two"><div class="fig">{svg("itu.svg")}</div><div><ul class="small">
<li>La raccomandazione ITU-R P.372 dà il rumore esterno medio come <b>fattore Fa</b>, in dB sopra kT₀B:</li></ul>
{eq("Fa = c − d · log f<sub>MHz</sub>")}
<table class="small"><tr><th>Ambiente</th><th>c</th><th>d</th></tr><tr><td class="l">Residenziale</td><td>72,5</td><td>27,7</td></tr><tr><td class="l">Rurale</td><td>67,2</td><td>27,7</td></tr><tr><td class="l">Rurale tranquillo</td><td>53,6</td><td>28,6</td></tr><tr><td class="l">Galattico</td><td>52,0</td><td>23,0</td></tr></table>
<p class="note">In 20 metri in zona residenziale: Fa ≈ 40,6 dB, il rumore esterno è oltre 10.000 volte quello di una resistenza a 290 K.</p></div></div>''')
rows="".join(f"<tr><td class='l'>{b}</td><td>{it(fa,1)} dB</td><td>{it(p,1).replace('-','−')} dBm</td><td>{s}</td></tr>" for b,fa,p,s in [("160 m (1,85 MHz)",65.1,-75.1,"≈ S9"),("80 m (3,6 MHz)",57.1,-83.1,"S7–S8"),("40 m (7,1 MHz)",48.9,-91.3,"S6"),("20 m (14,2 MHz)",40.6,-99.6,"S4–S5"),("10 m (28,5 MHz)",32.2,-108.0,"S3"),("2 m (145 MHz)",12.6,-127.6,"sotto S1")])
D.add("Che cosa leggi sull'S-meter",f'''<div class="two"><div><h3>Zona residenziale, banda SSB 2,4 kHz</h3><table><tr><th>Banda</th><th>Fa</th><th>Rumore</th><th>S-meter</th></tr>{rows}</table>
<p class="note">Rumore = −174 + 10·log 2400 + Fa = −140,2 dBm + Fa. S-meter HF con S9 = −73 dBm e 6 dB per unità S.</p></div><div><ul>
<li>In 80 e 160 metri il rumore di fondo in città può stare a S7–S9: nessun preamplificatore migliora la ricezione.</li>
<li>In 2 metri il rumore esterno è molto più basso e il ricevitore torna protagonista: lì la cifra di rumore conta davvero.</li>
<li>Sono valori medi: una sola lampadina LED o un inverter accanto all'antenna possono aggiungere 20–30 dB.</li>
<li>Prova semplice: scollega l'antenna. Se il fondo scende molto, è il rumore esterno a dominare.</li></ul></div></div>''')
r=[("Rumore","segnale casuale: conta il rapporto S/N"),("kTB","−174 dBm/Hz a 290 K; +10·log B"),("Johnson","50 Ω, 1 MHz: 0,89 µV a vuoto"),("Interni","shot, 1/f, valanga, fase, quantizzazione"),("Forma","bianco/rosa, gaussiano/impulsivo"),("Esterni","atmosferico, galattico, solare, artificiale"),("HF","domina il rumore esterno (ITU-R P.372)")]
D.add("Riepilogo",'<table class="sum">'+"".join(f'<tr><td class="l" style="width:160px"><b>{a}</b></td><td class="l">{b}</td></tr>' for a,b in r)+'</table>')
D.render(); pdf("Rumore_1_Cos_e_IV3HGA.pdf")
