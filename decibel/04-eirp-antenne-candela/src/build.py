import json, math
from deck import *
D=Deck("EIRP e antenne:<br>la candela di IW3SMV","Che cosa vuol dire che un'antenna \"guadagna\": una candela, uno specchio e una parabola per capire diagramma di irradiazione, dBi, dBd, EIRP ed ERP, con qualche antenna vera e pochi conti","Milestone · EIRP e antenne")
D.add("Un'antenna non crea energia",'''<div class="two"><div><ul>
<li>Un'antenna è un componente <b>passivo</b>: non ha alimentazione, non può tirare fuori più potenza di quella che le dai.</li>
<li>Eppure diciamo che una yagi "guadagna 12 dB". Che cosa vuol dire?</li>
<li>Che <b>in una certa direzione</b> manda tanta energia quanta ne manderebbe un'antenna ideale che irradia ovunque allo stesso modo, alimentata con 16 volte la potenza.</li>
<li>Il prezzo: nelle altre direzioni ne manda di meno. Il totale è sempre lo stesso.</li></ul></div><div>
<h3>Un esempio di IW3SMV</h3><ul><li>Per capirlo senza formule c'è un esempio bellissimo, che dobbiamo a <b>IW3SMV</b>: una candela in una stanza buia.</li>
<li>Seguiamolo passo per passo: alla fine ogni passaggio corrisponderà a un'antenna vera e a un diagramma di irradiazione.</li></ul></div></div>''')
D.add("1 · La candela al centro della stanza",f'''<div class="two"><div class="fig" style="width:86%;margin:auto">{svg("c1.svg")}</div><div><ul>
<li>Accendiamo una candela al centro di una stanza buia. La sua luce si diffonde <b>in ogni direzione</b>, nello stesso modo.</li>
<li>Ogni parete riceve un po' di luce, debole. Più ti allontani, più è fioca: la stessa luce si distribuisce su una superficie sempre più grande.</li>
<li>Questa è l'<b>antenna isotropica</b>: un'antenna ideale, che non esiste davvero, che irradia uguale ovunque.</li>
<li>È il riferimento di tutti i guadagni: <b>0 dBi</b>, cioè "1 volta l'isotropica".</li></ul></div></div>''')
g=json.load(open("vals.json"))
D.add("2 · Uno specchio piano da un lato",f'''<div class="two"><div class="fig" style="width:86%;margin:auto">{svg("c2.svg")}</div><div><ul>
<li>Mettiamo uno specchio dietro la candela. La luce che andava verso il muro dietro viene rimandata in avanti.</li>
<li>Metà stanza resta al buio, ma l'altra metà riceve <b>il doppio</b> della luce: tutta la luce della candela, su metà dello spazio.</li>
<li>La candela non brucia più forte: abbiamo solo <b>ridistribuito</b> la stessa luce.</li>
<li>In avanti è come avere due candele: ×2, cioè <b>+3 dB</b>. Dietro, quasi nulla.</li>
<li>È l'idea dell'antenna con <b>riflettore</b> (o di un'antenna davanti a un piano metallico).</li></ul></div></div>''')
D.add("3 · Curviamo lo specchio",f'''<div class="two"><div class="fig" style="width:86%;margin:auto">{svg("c3.svg")}</div><div><ul>
<li>Ora pieghiamo lo specchio, avvolgendo un po' la candela. La luce viene raccolta da più direzioni e mandata in un <b>cono</b> davanti.</li>
<li>La zona illuminata è più piccola, ma molto più luminosa: in questo esempio circa <b>{it(g["curved"],1)} volte</b> la candela da sola (circa +{it(10*math.log10(g["curved"]),0)} dB) al centro del cono.</li>
<li>Ai lati la luce cala gradualmente: il cono ha un "bordo" sfumato.</li>
<li>È quello che fa un'antenna più direttiva: guadagno maggiore, fascio più stretto.</li></ul></div></div>''')
D.add("4 · La candela nel fuoco della parabola",f'''<div class="two"><div class="fig" style="width:86%;margin:auto">{svg("c4.svg")}</div><div><ul>
<li>Infine usiamo uno specchio <b>parabolico</b> e mettiamo la candela esattamente nel suo <b>fuoco</b>.</li>
<li>La parabola ha una proprietà speciale: tutti i raggi che partono dal fuoco vengono riflessi <b>paralleli</b>. Nasce un fascio, come quello di un faro o di una torcia.</li>
<li>Dove il fascio arriva c'è moltissima luce: decine, centinaia o migliaia di volte quella della candela nuda. Fuori dal fascio, buio.</li>
<li>Se la candela non è nel fuoco, il fascio si allarga e perde intensità: è la stessa cosa che succede con un illuminatore mal posizionato in una parabola per microonde.</li></ul></div></div>''')
D.add("Dalla stanza al diagramma di irradiazione",f'''<div class="fig" style="width:96%">{svg("polar4.svg")}</div><div class="two" style="align-items:start;gap:30px"><div><ul class="small">
<li>Il <b>diagramma di irradiazione</b> è il disegno di "quanta luce" va in ogni direzione, visto dall'alto. In questi grafici lo zero è la candela da sola.</li>
<li>Candela: un cerchio. Specchio piano: un semicerchio più grande. Specchio curvo: un lobo. Parabola: un lobo sottilissimo e lungo.</li></ul></div><div><ul class="small">
<li>L'area "sotto" i diagrammi è sempre la stessa luce: si allunga in una direzione e si accorcia nelle altre.</li>
<li>Nelle antenne reali gli specchi non sono perfetti: compaiono piccoli <b>lobi laterali</b> e un <b>lobo posteriore</b>, la luce che "scappa".</li></ul></div></div>''')
ants=f'''<svg viewBox="0 0 1100 260" font-family="DejaVu Sans" stroke="{N}" stroke-width="3" fill="none">
<g transform="translate(40,40)"><line x1="0" y1="80" x2="90" y2="80"/><line x1="110" y1="80" x2="200" y2="80"/><line x1="90" y1="80" x2="110" y2="80" stroke="{C}"/><line x1="100" y1="80" x2="100" y2="150" stroke="{C}" stroke-width="2"/>
<text x="100" y="185" text-anchor="middle" font-size="15" stroke="none" fill="{N}" font-weight="700">Dipolo</text><text x="100" y="205" text-anchor="middle" font-size="13" stroke="none" fill="#555">2,15 dBi (0 dBd)</text></g>
<g transform="translate(300,20)"><line x1="80" y1="10" x2="80" y2="110"/><line x1="80" y1="110" x2="20" y2="145"/><line x1="80" y1="110" x2="140" y2="145"/><line x1="80" y1="110" x2="40" y2="160"/><line x1="80" y1="110" x2="120" y2="160"/><line x1="80" y1="110" x2="80" y2="180" stroke="{C}" stroke-width="2"/>
<text x="80" y="205" text-anchor="middle" font-size="15" stroke="none" fill="{N}" font-weight="700">Ground plane / collineare</text><text x="80" y="225" text-anchor="middle" font-size="13" stroke="none" fill="#555">~2 dBi / 5–8 dBi</text></g>
<g transform="translate(560,30)"><line x1="0" y1="90" x2="230" y2="90"/><line x1="20" y1="20" x2="20" y2="160"/><line x1="70" y1="35" x2="70" y2="145" stroke="{C}"/><line x1="120" y1="40" x2="120" y2="140"/><line x1="165" y1="43" x2="165" y2="137"/><line x1="210" y1="46" x2="210" y2="134"/>
<text x="115" y="195" text-anchor="middle" font-size="15" stroke="none" fill="{N}" font-weight="700">Yagi</text><text x="115" y="215" text-anchor="middle" font-size="13" stroke="none" fill="#555">3 el. ~7–8 dBi · 10 el. ~13 dBi</text></g>
<g transform="translate(880,20)"><path d="M60 10 Q-20 100 60 190"/><line x1="40" y1="100" x2="120" y2="100" stroke-width="2"/><circle cx="120" cy="100" r="8" fill="{C}" stroke="{C}"/>
<text x="80" y="215" text-anchor="middle" font-size="15" stroke="none" fill="{N}" font-weight="700">Parabola</text><text x="80" y="235" text-anchor="middle" font-size="13" stroke="none" fill="#555">20–40 dBi e oltre</text></g></svg>'''
D.add("Le antenne vere",f'''<div class="diag" style="width:96%">{ants}</div><div class="grid3" style="grid-template-columns:repeat(4,1fr);gap:14px;margin-top:4px">
<div class="card"><h3>Dipolo</h3><p>Non è isotropico: niente luce lungo i fili, il massimo di lato. Già 2,15 dBi.</p></div>
<div class="card"><h3>Verticali</h3><p>Uguali in tutte le direzioni orizzontali: la luce viene "schiacciata" verso l'orizzonte.</p></div>
<div class="card"><h3>Yagi</h3><p>Riflettore e direttori: lo specchio curvo della candela, fatto di elementi.</p></div>
<div class="card"><h3>Parabola</h3><p>L'illuminatore è la candela nel fuoco: fascio strettissimo.</p></div></div>''')
D.add("Diagrammi di irradiazione reali",f'''<div class="fig" style="width:96%">{svg("patterns.svg")}</div><div class="two" style="align-items:start;gap:30px"><div><ul class="small">
<li><b>Dipolo</b> (verticale nel disegno): due lobi larghi di lato, nulla lungo l'asse. <b>Yagi</b>: un lobo in avanti e un piccolo lobo dietro (rapporto avanti/indietro).</li></ul></div><div><ul class="small">
<li><b>Parabola</b>: fascio di circa 2° a −3 dB. Puntarla bene diventa fondamentale: un grado di errore costa già qualche dB. Andamenti indicativi.</li></ul></div></div>''')
D.add("Fascio stretto, guadagno alto",'''<div class="two"><div><ul>
<li>Più stretto è il fascio, più la luce è concentrata, più alto è il guadagno. Una regola pratica lega le due cose:</li></ul>
<div class="eq">G ≈ 30 000 / (θ<sub>E</sub> · θ<sub>H</sub>) &nbsp; (gradi, a −3 dB)</div>
<ul class="small"><li>θ<sub>E</sub> e θ<sub>H</sub> sono le larghezze del fascio nei due piani.</li>
<li>Esempio: una yagi con 50° × 60° → G ≈ 10 → <b>10 dBi</b>.</li></ul></div><div>
<h3>La parabola</h3>
<div class="eq">G ≈ η · (π · D / λ)² &nbsp; θ ≈ 70 · λ / D (gradi)</div>
<ul class="small"><li>Parabola da 1 m a 10 GHz (λ = 3 cm) con efficienza 55 %: G ≈ 0,55 · (π · 1 / 0,03)² ≈ 6000 → <b>~38 dBi</b>; fascio ≈ 2°.</li>
<li>Raddoppiare il diametro: +6 dB. Raddoppiare la frequenza con la stessa parabola: +6 dB, ma fascio dimezzato.</li></ul></div></div>''')
D.add("EIRP ed ERP",'''<div class="two"><div><ul>
<li>L'<b>EIRP</b> (potenza isotropica equivalente irradiata) è la potenza che dovrebbe avere la candela nuda per illuminare quanto la tua antenna, nella direzione del massimo.</li></ul>
<div class="eq">EIRP (dBm) = P<sub>TX</sub> (dBm) − perdite (dB) + G (dBi)</div>
<div class="eq">ERP = EIRP − 2,15 dB &nbsp;(riferita al dipolo)</div>
<ul class="small"><li>È ciò che "vede" chi ti riceve: per lui non fa differenza se hai tanta potenza e un'antenna semplice, o poca potenza e un'antenna direttiva.</li>
<li>Le norme e le autorizzazioni spesso fissano limiti in EIRP o ERP.</li></ul></div><div>
<h3>Esempio: yagi in VHF</h3><ul class="small"><li>TX da 50 W = <b>47 dBm</b>; cavo e connettori −2 dB; yagi da 13 dBi.</li>
<li>EIRP = 47 − 2 + 13 = <b>58 dBm</b> = 631 W.</li>
<li>ERP = 58 − 2,15 = 55,85 dBm ≈ <b>385 W</b>.</li>
<li>In avanti è come avere una "candela" da 631 W; dietro, con 20 dB di rapporto avanti/indietro, circa 6 W.</li></ul></div></div>''')
D.add("Altri esempi di EIRP",'''<table><tr><th>Stazione</th><th>Potenza</th><th>Perdite</th><th>Antenna</th><th>EIRP</th></tr>
<tr><td class="l">Portatile con stilo</td><td class="l">5 W (37 dBm)</td><td class="l">0 dB</td><td class="l">~0 dBi</td><td class="l">37 dBm ≈ 5 W</td></tr>
<tr><td class="l">HF con dipolo</td><td class="l">100 W (50 dBm)</td><td class="l">1 dB</td><td class="l">2,15 dBi</td><td class="l">51 dBm ≈ 126 W</td></tr>
<tr><td class="l">Ponte con collineare</td><td class="l">25 W (44 dBm)</td><td class="l">3 dB (cavo + duplexer)</td><td class="l">6 dBi</td><td class="l">47 dBm ≈ 50 W</td></tr>
<tr><td class="l">EME a 144 MHz</td><td class="l">1 kW (60 dBm)</td><td class="l">1 dB</td><td class="l">4 yagi, ~20 dBi</td><td class="l">79 dBm ≈ 80 kW</td></tr>
<tr><td class="l">Link a 10 GHz</td><td class="l">1 W (30 dBm)</td><td class="l">1 dB</td><td class="l">parabola 1 m, 38 dBi</td><td class="l">67 dBm ≈ 5 kW</td></tr></table>
<p class="note" style="margin-top:14px">Un watt in una parabola "illumina" in quella direzione come 5 kW su un'antenna isotropica: la candela nel fuoco dello specchio.</p>''')
rows=[("Guadagno","ridistribuzione della stessa energia, non creazione"),("Candela","isotropica, 0 dBi"),("Specchio piano","metà spazio, ×2: +3 dB"),("Specchio curvo","cono: guadagno maggiore, fascio più stretto"),("Parabola","candela nel fuoco: fascio parallelo, guadagno altissimo"),("EIRP","P − perdite + G(dBi); ERP = EIRP − 2,15")]
D.add("Riepilogo",'<table class="sum">'+"".join(f'<tr><td class="l" style="width:200px"><b>{a}</b></td><td class="l">{b}</td></tr>' for a,b in rows)+'</table><p class="note" style="margin-top:16px">Grazie a IW3SMV per l\'esempio della candela.</p>')
D.render(); pdf("DB_EIRP_Antenne_Candela_IV3HGA.pdf")
