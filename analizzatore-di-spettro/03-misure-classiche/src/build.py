import json
from deck import *
v=json.load(open("vals.json"))
D=Deck("Le misure classiche<br>con l'analizzatore","Potenza e frequenza, armoniche, intermodulazione, modulazione AM e FM, potenza di canale, zero span, tracking generator e rumore di fase: spiegate passo per passo","L'analizzatore di spettro: misure classiche")
cards=[("Potenza e frequenza","di una portante"),("Armoniche e spurie","di un trasmettitore"),("Intermodulazione","test a due toni, TOI"),("Modulazione AM","profondità dalle bande laterali"),
("Deviazione FM","metodo del nullo di Bessel"),("Potenza di canale","OBW, ACP, segnali digitali"),("Zero span","il segnale nel tempo"),("Tracking generator","filtri, duplexer, SWR"),("Rumore di fase","in dBc/Hz")]
D.add("Le misure di questo modulo",'<div class="grid3">'+"".join(f'<div class="card"><h3>{a}</h3><p>{b}</p></div>' for a,b in cards)+'</div><p class="note" style="margin-top:18px">Per ognuna: collegamento, impostazioni, come leggere il risultato e gli errori da evitare. Le protezioni e le impostazioni di base sono nel modulo precedente.</p>')
D.add("1 · Potenza e frequenza di una portante",'''<div class="two"><div><h3>Impostazioni</h3><ol class="small">
<li>Calcola i livelli e inserisci le attenuazioni esterne come <b>reference offset</b>.</li>
<li>Span largo per trovare il segnale, poi <b>peak search</b> e <b>marker → center</b>.</li>
<li>Restringi lo span (per esempio 100 kHz) e porta il segnale 5–10 dB sotto il reference level.</li>
<li>Per una portante non modulata la RBW non cambia l'ampiezza letta: scegli quella che rende la traccia stabile.</li>
<li>Usa il <b>frequency counter</b> sul marker per la frequenza esatta.</li></ol></div><div>
<h3>Quanto ci si può fidare</h3><ul class="small"><li>L'incertezza assoluta di un analizzatore è tipicamente intorno a ±0,5…±1,5 dB, a cui si aggiungono le incertezze di cavi e attenuatori.</li>
<li>Per una misura di potenza precisa, usa l'analizzatore per i livelli <b>relativi</b> (dBc) e un <b>power meter</b> per quello assoluto.</li>
<li>Su un segnale modulato (FM, digitale) il marker di picco non legge la potenza totale: usa la potenza di canale (misura 6).</li>
<li>La precisione in frequenza dipende dal riferimento interno: un riferimento esterno a 10 MHz (GPSDO) la migliora molto.</li></ul></div></div>''')
D.add("2 · Armoniche e spurie di un trasmettitore",f'''<div class="two"><div class="fig">{svg("harm.svg")}<p class="cap">TX a 145 MHz, simulazione: le ampiezze sono relative alla fondamentale.</p></div><div><ul class="small">
<li>TX su carico fittizio con campionatore, oppure attenuatore di potenza (vedi la catena di protezione).</li>
<li>Span da poco sopra zero a oltre la 3ª–5ª armonica, RBW automatica, rivelatore peak.</li>
<li>Marker sulla fondamentale, poi <b>delta marker</b> su ogni armonica: leggi direttamente i <b>dBc</b>.</li>
<li>Verifica che le armoniche non le crei l'analizzatore: aumenta l'attenuazione di 10 dB. Se il livello in dBc cambia, sono <b>interne</b>.</li>
<li>Per misurare armoniche molto basse, attenua la fondamentale con un <b>passa-alto o un notch</b> prima dell'analizzatore e correggi per la perdita del filtro alle armoniche.</li></ul>
<p class="note">Cerca anche le spurie non armoniche: prodotti dei sintetizzatori, oscillazioni parassite, rumore a larga banda.</p></div></div>''')
D.add("3 · Intermodulazione e punto di intercetta (TOI)",f'''<div class="two"><div class="fig">{svg("imd.svg")}</div><div><ul class="small">
<li>Due generatori a frequenze vicine (f1, f2), sommati con un <b>combinatore</b> ad alto isolamento e attenuatori, entrano nel DUT (amplificatore, mixer, ricevitore).</li>
<li>I prodotti del 3° ordine cadono a <b>2f1 − f2</b> e <b>2f2 − f1</b>, vicinissimi ai toni: nessun filtro li può togliere.</li></ul>
{eq("OIP3 = P<sub>tono</sub> + Δ / 2")}{eq("IIP3 = OIP3 − guadagno")}
<p class="note">Esempio: toni da 0 dBm in uscita, IM3 a −60 dBc → OIP3 = +{v["oip3"]:.0f} dBm. Verifica sempre che i generatori non si intermodulino tra loro e che l'IM3 non nasca nell'analizzatore (test dell'attenuazione: un IM3 interno cambia di 2 dB per ogni dB di attenuazione).</p></div></div>''')
D.add("4 · Profondità di modulazione AM",f'''<div class="two"><div class="fig">{svg("am.svg")}</div><div><ul class="small">
<li>Con un tono di modulazione fm, lo spettro AM è la portante più <b>due bande laterali</b> a ±fm, ciascuna di ampiezza m/2.</li>
<li>RBW abbastanza stretta da separare le righe (meno di fm/3).</li></ul>
{eq("m = 2 · 10<sup>−Δ/20</sup>")}
<table><tr><th>m</th><th>Δ portante − banda laterale</th></tr>
<tr><td class="l">100 %</td><td>6,0 dB</td></tr><tr><td class="l">50 %</td><td>12,0 dB</td></tr><tr><td class="l">30 %</td><td>16,5 dB</td></tr><tr><td class="l">10 %</td><td>26,0 dB</td></tr></table>
<p class="note">Bande laterali di livello diverso indicano modulazione di fase o di frequenza indesiderata insieme all'AM.</p></div></div>''')
D.add("5 · Deviazione FM con il nullo di Bessel",f'''<div class="two"><div class="fig">{svg("bessel.svg")}</div><div><ul class="small">
<li>In FM l'ampiezza della portante vale J0(β), con <b>β = Δf / fm</b>. Per β = <b>2,405</b> la portante <b>sparisce</b>.</li>
<li>Scegli fm in modo che il nullo cada alla deviazione voluta, poi alza il livello audio finché la portante scompare: in quel punto la deviazione è esatta.</li></ul>
{eq("Δf = 2,405 · fm")}
<table><tr><th>Deviazione voluta</th><th>Tono fm</th></tr>
<tr><td class="l">5 kHz (canali da 25 kHz)</td><td>2079 Hz</td></tr><tr><td class="l">2,5 kHz (canali da 12,5 kHz)</td><td>1040 Hz</td></tr></table>
<p class="note">RBW stretta (100–300 Hz) per vedere bene la portante. Banda occupata con la regola di Carson: B ≈ 2·(Δf + fm).</p></div></div>''')
D.add("6 · Potenza di canale, banda occupata, ACP",'''<div class="two"><div><ul>
<li>Un segnale modulato (FM, digitale, rumore) non ha una riga sola: la sua potenza è <b>distribuita</b> nella banda.</li>
<li>La misura di <b>potenza di canale</b> integra la traccia sulla larghezza del canale: rivelatore <b>RMS</b>, RBW pari all'1–5 % della banda, VBW ≥ 3·RBW, media su più sweep.</li>
<li><b>Banda occupata (OBW)</b>: la larghezza che contiene il 99 % della potenza.</li></ul></div><div>
<h3>ACP: potenza nel canale adiacente</h3><ul class="small"><li>Rapporto tra la potenza nel canale adiacente e quella nel canale principale, in dB.</li>
<li>Indica quanto il trasmettitore "sporca" i vicini: amplificatori in compressione e modulazione mal filtrata peggiorano l'ACP.</li>
<li>Molti analizzatori hanno funzioni automatiche: imposti larghezza e spaziatura dei canali e leggi i risultati.</li>
<li>Se non le hai, integra a mano: 10·log della somma delle potenze dei punti, corretta per RBW e passo dei punti.</li></ul></div></div>''')
D.add("7 · Zero span: il segnale nel tempo",f'''<div class="fig" style="width:94%">{svg("zerospan.svg")}</div><div class="two" style="align-items:start;gap:30px"><div><ul class="small">
<li>Span = 0: l'analizzatore resta fermo su una frequenza e mostra il livello <b>nel tempo</b>, come un ricevitore con oscilloscopio.</li>
<li>RBW ≥ banda del segnale, trigger <b>video</b> sul fronte di salita, sweep time pari a qualche trama.</li></ul></div><div><ul class="small">
<li>Usi: burst TDMA (TETRA, DMR: qui trama di 4 timeslot da 14,17 ms), impulsi, rapporto on/off, tempi di salita, inviluppo AM, intermittenze.</li>
<li>Con un segnale AM e scala lineare vedi direttamente la forma d'onda modulante.</li></ul></div></div>''')
D.add("8 · Risposta in frequenza con il tracking generator",'''<div class="two"><div><h3>Trasmissione (S21 scalare)</h3><ol class="small">
<li>Collega uscita del TG e ingresso dell'analizzatore con i cavi di misura e un thru.</li>
<li><b>Normalizza</b> (store reference / normalize): la traccia diventa 0 dB.</li>
<li>Inserisci il DUT: leggi direttamente perdita, banda e reiezione.</li></ol>
<p class="note">Ottimo per duplexer e filtri a cavità: la dinamica dell'analizzatore supera spesso quella di un VNA economico. Per notch profondi, riduci la RBW.</p></div><div>
<h3>Riflessione con un ponte (SWR)</h3><ol class="small"><li>TG → ponte di return loss → analizzatore, con la porta di prova del ponte aperta (o in corto).</li>
<li>Normalizza: è il riferimento di riflessione totale (0 dB).</li>
<li>Collega il DUT alla porta di prova: la traccia è il <b>return loss</b>.</li></ol>
<p class="note">La direttività del ponte limita il return loss misurabile, esattamente come nel VNA (modulo 1 del capitolo VNA).</p></div></div>''')
D.add("9 · Rumore di fase di un oscillatore",'''<div class="two"><div><ul>
<li>Il rumore di fase si esprime in <b>dBc/Hz</b> a una certa distanza (offset) dalla portante.</li>
<li>Misura la portante (P<sub>c</sub>), poi metti un <b>noise marker</b> all'offset voluto: legge direttamente dBm/Hz.</li></ul>
<div class="eq">L(f<sub>off</sub>) = P<sub>rumore</sub>(dBm/Hz) − P<sub>c</sub>(dBm)</div>
<p class="note">Esempio: portante −10 dBm, noise marker a 10 kHz −105 dBm/Hz → L(10 kHz) = −95 dBc/Hz.</p></div><div>
<h3>Attenzione</h3><ul class="small"><li>Non puoi misurare un oscillatore migliore dell'analizzatore: confronta il risultato con il rumore di fase dichiarato dello strumento.</li>
<li>RBW molto più stretta dell'offset, altrimenti leggi la "gonna" del filtro e non il rumore.</li>
<li>Rivelatore sample o RMS, media su più sweep. Se usi un marker normale, normalizza tu: −10·log(RBW) e +2,5 dB per la media logaritmica.</li>
<li>Il rumore di fase del VFO di un ricevitore peggiora il "reciprocal mixing": un segnale forte vicino alza il rumore di fondo.</li></ul></div></div>''')
rows=[("Potenza e frequenza","peak search, counter, offset esterni"),("Armoniche e spurie","delta marker in dBc, test dell'attenuazione"),("Intermodulazione","OIP3 = P + Δ/2"),("AM","m = 2·10^(−Δ/20)"),("FM","nullo della portante a β = 2,405"),
("Potenza di canale","RMS, RBW 1–5 % del canale"),("Zero span","il segnale nel tempo, trigger video"),("Tracking generator","normalizza, poi misura"),("Rumore di fase","noise marker − portante, in dBc/Hz")]
D.add("Riepilogo",'<table class="sum">'+"".join(f'<tr><td class="l" style="width:300px"><b>{a}</b></td><td class="l">{b}</td></tr>' for a,b in rows)+'</table>')
D.render(); pdf("SA_Misure_Classiche_IV3HGA.pdf")
