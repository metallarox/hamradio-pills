import json
from deck import *
v=json.load(open("vals.json"))
D=Deck("La catena di trasmissione<br>in decibel","Dal trasmettitore all'antenna e dall'antenna al ricevitore: perdite dei cavi, guadagni, attenuazione di spazio libero e bilancio del collegamento, tutto con somme e sottrazioni","Milestone · la catena in dB")
D.add("Una catena è una somma",f'''<div class="fig" style="width:96%">{svg("budget.svg")}</div><div class="two" style="align-items:start;gap:30px"><div><ul class="small">
<li>Collegamento a 145 MHz su 50 km in spazio libero: ogni blocco aggiunge o toglie dB, e il livello si segue come una scala.</li></ul></div><div><ul class="small">
<li>Arrivano circa <b>{it(v["pr"],0)} dBm</b>: oltre 70 dB sopra la sensibilità. Nella realtà ostacoli, terreno e curvatura terrestre si mangiano gran parte di questo margine.</li></ul></div></div>''')
D.add("Le perdite della linea",'''<div class="two"><div><ul>
<li>I cavi coassiali sono specificati in <b>dB per 100 m</b> a una certa frequenza: la perdita cresce con la frequenza e con la lunghezza.</li></ul>
<div class="eq">perdita = (dB/100 m) × lunghezza / 100</div>
<table><tr><th>Cavo (valori indicativi)</th><th>145 MHz</th><th>435 MHz</th></tr>
<tr><td class="l">RG-58</td><td class="l">~ 17 dB/100 m</td><td class="l">~ 32 dB/100 m</td></tr>
<tr><td class="l">RG-213</td><td class="l">~ 8,5 dB/100 m</td><td class="l">~ 15 dB/100 m</td></tr>
<tr><td class="l">Cavi a basse perdite da ~10 mm</td><td class="l">~ 5 dB/100 m</td><td class="l">~ 9 dB/100 m</td></tr></table>
<p class="note">Valori tipici: usa il datasheet del tuo cavo.</p></div><div>
<h3>Esempio: 30 m a 435 MHz</h3><ul class="small"><li>RG-58: 0,3 × 32 = <b>9,6 dB</b> → di 50 W arrivano circa 5,5 W all'antenna.</li>
<li>Cavo da 10 mm a basse perdite: 0,3 × 9 = <b>2,7 dB</b> → arrivano circa 27 W.</li>
<li>Cambiare cavo vale quanto un lineare da 5 volte la potenza (~7 dB), e funziona anche in ricezione.</li>
<li>Ogni connettore aggiunge 0,1–0,2 dB (più se ossidato), ogni adattatore lo stesso.</li></ul></div></div>''')
D.add("Disadattamento: quanto costa davvero",'''<div class="two"><div><ul>
<li>Con un SWR diverso da 1, una parte della potenza torna indietro. La perdita "di disadattamento" vale:</li></ul>
<div class="eq">ML = −10·log(1 − |Γ|²)</div>
<table><tr><th>SWR</th><th>Mismatch loss</th></tr><tr><td class="l">1,5</td><td>0,18 dB</td></tr><tr><td class="l">2</td><td>0,51 dB</td></tr><tr><td class="l">3</td><td>1,25 dB</td></tr><tr><td class="l">5</td><td>2,55 dB</td></tr></table></div><div>
<ul class="small"><li>Un SWR 2:1 "costa" mezzo dB: meno di un decimo di punto S. Molto meno di quello che si teme.</li>
<li>Il problema vero dell'SWR alto è altrove: il finale che riduce la potenza per protezione, e le perdite del cavo che aumentano con l'onda stazionaria.</li>
<li>Un cavo con molte perdite <b>maschera</b> l'SWR: in stazione sembra buono, all'antenna non lo è (capitolo sul VNA, carta di Smith).</li></ul></div></div>''')
D.add("Lo spazio libero",f'''<div class="two"><div><ul>
<li>Anche nel vuoto il segnale si "diluisce": la stessa energia si distribuisce su una sfera sempre più grande. È l'attenuazione di <b>spazio libero</b>:</li></ul>
<div class="eq">FSPL (dB) = 32,45 + 20·log(f<sub>MHz</sub>) + 20·log(d<sub>km</sub>)</div>
<ul class="small"><li>Raddoppiare la distanza costa <b>6 dB</b> (un punto S); decuplicarla 20 dB.</li>
<li>Esempio: 145 MHz e 50 km → {it(v["fspl"],1)} dB.</li></ul></div><div>
<h3>Perché dipende dalla frequenza?</h3><ul class="small"><li>Non è l'aria che "assorbe" di più: la formula è scritta per due antenne <b>isotropiche</b>, e un'antenna isotropica a frequenza più alta è più piccola e raccoglie meno energia.</li>
<li>Con antenne di uguale <b>dimensione fisica</b> (per esempio due parabole) a frequenza alta il guadagno cresce e compensa: per questo le microonde usano parabole.</li>
<li>Nella realtà si aggiungono ostacoli, assorbimento della vegetazione, riflessioni, propagazione ionosferica in HF.</li></ul></div></div>''')
D.add("Il bilancio del collegamento",'''<div class="two"><div>
<div class="eq">P<sub>RX</sub> = P<sub>TX</sub> − L<sub>cavo TX</sub> + G<sub>TX</sub> − FSPL + G<sub>RX</sub> − L<sub>cavo RX</sub></div>
<div class="eq">margine = P<sub>RX</sub> − sensibilità</div>
<ul class="small"><li>Il margine è la "riserva" contro ostacoli, evanescenze, antenne non perfettamente puntate.</li>
<li>Per i ponti radio si progetta con margini di 20–30 dB o più.</li></ul></div><div>
<h3>Cosa conviene migliorare</h3><ul class="small"><li>Ogni dB vale uguale ovunque nella catena: un dB guadagnato nel cavo o nell'antenna vale quanto un dB di potenza.</li>
<li>Ma i miglioramenti in <b>antenna e cavo</b> valgono in <b>trasmissione e in ricezione</b>; la potenza solo in trasmissione.</li>
<li>In ricezione, dove il rumore esterno è basso (VHF e oltre), il cavo prima del preamplificatore pesa doppio: aggiunge perdita <b>e</b> rumore. Per questo i preamplificatori si montano in cima al palo.</li></ul></div></div>''')
D.add("Esercizio guidato: un ponte radio",'''<div class="two"><div><h3>Dati</h3><ul class="small">
<li>Portatile: 5 W (37 dBm), antenna a stilo 0 dBi.</li><li>Ponte a 20 km, 435 MHz: antenna collineare 6 dBi, 25 m di cavo da ~9 dB/100 m (−2,3 dB), duplexer −1,5 dB.</li>
<li>Sensibilità del ricevitore del ponte: −120 dBm.</li></ul>
<h3>Conti</h3><ul class="small"><li>FSPL = 32,45 + 52,8 + 26,0 = <b>111,2 dB</b>.</li>
<li>P<sub>RX</sub> = 37 + 0 − 111,2 + 6 − 2,3 − 1,5 = <b>−72 dBm</b>.</li><li>Margine: −72 − (−120) = <b>48 dB</b>.</li></ul></div><div>
<h3>Cosa ci dice</h3><ul class="small"><li>In spazio libero il collegamento è abbondante: anche con 30–40 dB di perdite per ostacoli e il corpo dell'operatore, si passa ancora.</li>
<li>Se dal portatile non si apre il ponte, il problema è nel percorso (ostacoli, schermature di edifici) o in un elemento della catena (antenna, cavo, duplexer).</li>
<li>Con i dB lo vedi in un minuto, senza calcolatrice.</li></ul></div></div>''')
rows=[("Catena","si sommano guadagni e si sottraggono perdite"),("Cavi","dB/100 m × lunghezza; crescono con la frequenza"),("SWR","2:1 costa solo 0,5 dB"),("Spazio libero","32,45 + 20·log f + 20·log d; ×2 distanza = −6 dB"),("Margine","P<sub>RX</sub> − sensibilità")]
D.add("Riepilogo",'<table class="sum">'+"".join(f'<tr><td class="l" style="width:200px"><b>{a}</b></td><td class="l">{b}</td></tr>' for a,b in rows)+'</table>')
D.render(); pdf("DB_Catena_Trasmissione_IV3HGA.pdf")
