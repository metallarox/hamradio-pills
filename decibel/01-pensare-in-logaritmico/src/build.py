from deck import *
D=Deck("Il decibel:<br>pensare in logaritmico","Che cos'è il decibel, perché lo usano tutti i radiotecnici, potenze e tensioni, i trucchi per fare i conti a mente e come smettere di avere paura dei logaritmi","Milestone · il decibel")
D.add("Perché i decibel",f'''<div class="fig" style="width:94%">{svg("lin_log.svg")}</div><div class="two" style="align-items:start;gap:30px"><div><ul class="small">
<li>In radio conviviamo con numeri lontanissimi: un trasmettitore da 100 W e un segnale ricevuto da 0,000 000 000 000 01 W (−110 dBm). Con i numeri "normali" non si riesce a ragionare.</li></ul></div><div><ul class="small">
<li>Il decibel trasforma le <b>moltiplicazioni in somme</b>: guadagni e perdite di una catena si sommano e si sottraggono, a mente.</li>
<li>Anche l'orecchio e l'occhio funzionano "in logaritmico": per questo l'S-meter, il volume e la luminosità sono naturali in dB.</li></ul></div></div>''')
D.add("La definizione",'''<div class="two"><div><ul><li>Il decibel è un <b>rapporto</b> tra due potenze, scritto in scala logaritmica:</li></ul>
<div class="eq">dB = 10 · log<sub>10</sub>(P<sub>2</sub> / P<sub>1</sub>)</div>
<ul class="small"><li>Positivo se P<sub>2</sub> è più grande (guadagno), negativo se è più piccolo (perdita, attenuazione).</li>
<li>0 dB significa "uguale": rapporto 1.</li>
<li>Da solo il dB <b>non è un'unità di potenza</b>: dice "quante volte", non "quanto". Per dire "quanto" serve un riferimento, ed ecco dBm, dBW, dBµV… (lezione successiva).</li></ul></div><div>
<h3>Al contrario</h3>
<div class="eq">rapporto = 10<sup>dB / 10</sup></div>
<ul class="small"><li>Sulla calcolatrice: 10, tasto x<sup>y</sup>, il valore in dB diviso 10.</li>
<li>Esempio: 13 dB → 10<sup>1,3</sup> = 20 volte.</li>
<li>Ma con i trucchi delle prossime slide la calcolatrice serve raramente.</li></ul></div></div>''')
D.add("Potenze e tensioni: 10 o 20?",'''<div class="two"><div><ul>
<li>La potenza è proporzionale al <b>quadrato</b> della tensione (P = V²/R). Per questo, quando il rapporto è tra tensioni (o correnti), si usa 20:</li></ul>
<div class="eq">dB = 20 · log<sub>10</sub>(V<sub>2</sub> / V<sub>1</sub>)</div>
<ul class="small"><li>Così lo stesso fenomeno dà lo stesso numero di dB, che tu misuri tensioni o potenze.</li>
<li>Esempio: raddoppi la tensione su 50 Ω → la potenza diventa 4 volte → +6 dB in entrambi i casi.</li></ul></div><div>
<table><tr><th>dB</th><th>× potenza</th><th>× tensione</th></tr>
<tr><td class="l">0</td><td>1</td><td>1</td></tr><tr><td class="l">1</td><td>1,26</td><td>1,12</td></tr><tr><td class="l">3</td><td>2</td><td>1,41</td></tr>
<tr><td class="l">6</td><td>4</td><td>2</td></tr><tr><td class="l">10</td><td>10</td><td>3,16</td></tr><tr><td class="l">20</td><td>100</td><td>10</td></tr>
<tr><td class="l">30</td><td>1000</td><td>31,6</td></tr><tr><td class="l">−3</td><td>0,5</td><td>0,71</td></tr><tr><td class="l">−10</td><td>0,1</td><td>0,32</td></tr></table>
<p class="note">Il 20·log vale solo se le due tensioni sono sulla stessa impedenza.</p></div></div>''')
D.add("Il trucco: bastano il 3 e il 10",'''<div class="two"><div><ul>
<li>Ricorda solo due cose: <b>+3 dB = ×2</b> e <b>+10 dB = ×10</b>. Tutto il resto si costruisce sommando e sottraendo.</li></ul>
<table><tr><th>dB</th><th>Costruzione</th><th>× potenza</th></tr>
<tr><td class="l">6</td><td class="l">3 + 3</td><td>2 × 2 = 4</td></tr><tr><td class="l">7</td><td class="l">10 − 3</td><td>10 / 2 = 5</td></tr>
<tr><td class="l">4</td><td class="l">10 − 3 − 3</td><td>10 / 4 = 2,5</td></tr><tr><td class="l">9</td><td class="l">3 + 3 + 3</td><td>8</td></tr>
<tr><td class="l">13</td><td class="l">10 + 3</td><td>20</td></tr><tr><td class="l">17</td><td class="l">20 − 3</td><td>50</td></tr>
<tr><td class="l">1</td><td class="l">10 − 9</td><td>10 / 8 ≈ 1,25</td></tr><tr><td class="l">2</td><td class="l">1 + 1</td><td>≈ 1,6</td></tr></table></div><div>
<h3>Al contrario: da "volte" a dB</h3><ul class="small"><li>×200 = ×100 × 2 → 20 + 3 = <b>23 dB</b>.</li>
<li>×0,25 = /4 → <b>−6 dB</b>.</li><li>×5000 = ×10 000 / 2 → 40 − 3 = <b>37 dB</b>.</li>
<li>×1/1000 = <b>−30 dB</b>.</li></ul>
<p class="note">Con questa tabella in testa fai a mente il 90 % dei conti di una stazione radio, con un errore di pochi percento.</p></div></div>''')
D.add("Esempi da stazione",'''<div class="two"><div><ul class="small">
<li><b>Lineare da 100 W a 400 W</b>: ×4 = +6 dB. All'altro capo del QSO è <b>un punto S</b> in più (6 dB). Utile, ma non miracoloso.</li>
<li><b>Da 5 W a 100 W</b>: ×20 = +13 dB, poco più di due punti S.</li>
<li><b>Da 100 W a 1 kW</b>: ×10 = +10 dB, meno di due punti S.</li>
<li><b>Cavo che perde 3 dB</b>: metà della potenza scalda il cavo. Dei 100 W del trasmettitore, all'antenna ne arrivano 50.</li></ul></div><div><ul class="small">
<li><b>Yagi da 10 dBd invece di un dipolo</b>: in quella direzione, come moltiplicare per 10 la potenza.</li>
<li><b>Preamplificatore da 20 dB</b>: il segnale e il rumore crescono entrambi di 100 volte; serve davvero solo se il ricevitore è il limite (capitolo sul generatore).</li>
<li><b>Attenuatore da 40 dB</b>: 100 W diventano 10 mW.</li>
<li>Morale: i dB rendono evidente cosa conviene. Spesso migliorare l'antenna o il cavo vale più di un lineare.</li></ul></div></div>''')
D.add("Sommare, sottrarre… e cosa non si fa",'''<div class="two"><div><h3>Si può</h3><ul class="small">
<li>dB + dB = dB: guadagni e perdite in serie si sommano. 20 dB di amplificatore − 3 dB di cavo = 17 dB.</li>
<li>dBm + dB = dBm: un livello più un guadagno è un nuovo livello. 0 dBm + 17 dB = +17 dBm.</li>
<li>dBm − dBm = dB: la differenza tra due livelli è un rapporto. −60 dBm e −80 dBm differiscono di 20 dB.</li></ul></div><div>
<h3>Non si può</h3><ul class="small"><li><b>dBm + dBm</b>: due segnali da 0 dBm insieme non fanno "0 dBm", né "0+0": in watt 1 mW + 1 mW = 2 mW = <b>+3 dBm</b>.</li>
<li>Per sommare potenze converti in watt, somma, riconverti (capitolo sul wattmetro, potenza dello spettro).</li>
<li>Non mescolare 10·log e 20·log sullo stesso rapporto.</li>
<li>Non confondere "dB" (rapporto) con "dBm" (livello): "l'amplificatore dà 20 dBm" è un livello d'uscita, "guadagna 20 dB" è un rapporto.</li></ul></div></div>''')
D.add("Per non scoraggiarsi",'''<div class="two"><div><ul>
<li>Pensa ai dB come a <b>gradini</b>: ogni 10 dB è uno zero in più o in meno. Non serve "vedere" il logaritmo, basta contare gli zeri.</li>
<li>Abituati a tradurre le misure di tutti i giorni: l'S-meter (6 dB per punto), i guadagni d'antenna, le perdite dei cavi.</li>
<li>Usa i numeri rotondi: 3, 6, 10, 20, 30. Il resto è una piccola correzione.</li></ul></div><div>
<h3>Esercizi da fare a mente</h3><ol class="small"><li>Un cavo perde 1,5 dB ogni 10 m. Quanto perdono 30 m? (4,5 dB: poco meno di 3 volte)</li>
<li>Da 50 W, con 6 dB di perdita: quanti watt arrivano? (12,5 W)</li>
<li>Un segnale passa da S5 a S9: quanti dB? (24 dB, cioè ×250 in potenza)</li>
<li>0 dBm passano in un attenuatore da 20 dB e in un amplificatore da 30 dB: livello finale? (+10 dBm = 10 mW)</li></ol></div></div>''')
rows=[("Definizione","dB = 10·log(P<sub>2</sub>/P<sub>1</sub>) = 20·log(V<sub>2</sub>/V<sub>1</sub>)"),("Trucco","+3 dB = ×2, +10 dB = ×10: il resto si costruisce"),("Somme","dB + dB, dBm + dB ok; dBm + dBm no"),("Punto S","6 dB = ×4 in potenza"),("Abitudine","conta gli zeri: 10 dB a gradino")]
D.add("Riepilogo",'<table class="sum">'+"".join(f'<tr><td class="l" style="width:200px"><b>{a}</b></td><td class="l">{b}</td></tr>' for a,b in rows)+'</table>')
D.render(); pdf("DB_Pensare_Logaritmico_IV3HGA.pdf")
