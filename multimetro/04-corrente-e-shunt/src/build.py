from deck import *
O="#e0563b"
D=Deck("Misurare la corrente<br>e gli shunt","Il collegamento in serie, lo shunt interno e la tensione di carico, leggere una corrente in modalità tensione, shunt esterni, cavi e piste usati come shunt, pinze, nanoampere e correnti di riposo","Il multimetro: la corrente e gli shunt")
ser=f'''<svg viewBox="0 0 900 230" font-family="DejaVu Sans">{ARW}
{box(20,70,120,70,"Sorgente","#fff",16)}<path d="M140 90 H260" stroke="{N}" stroke-width="2.5"/>
{box(260,55,170,100,"","#fff")}<text x="345" y="85" text-anchor="middle" font-size="15" font-weight="700" fill="{N}">Multimetro (A)</text>
<rect x="290" y="100" width="110" height="26" rx="4" fill="#e8f6fd" stroke="{C}" stroke-width="2"/><text x="345" y="118" text-anchor="middle" font-size="13" fill="{C}" font-weight="700">shunt R<tspan font-size="10" dy="3">sh</tspan></text>
<path d="M430 90 H550" stroke="{N}" stroke-width="2.5"/>{box(550,70,130,70,"Carico","#fff",16)}<path d="M615 140 V185 H80 V140" stroke="{N}" stroke-width="2.5" fill="none"/>
<text x="345" y="212" text-anchor="middle" font-size="13" fill="#555">il circuito va aperto: la corrente deve passare nello strumento</text>
<text x="720" y="85" font-size="14" fill="{O}" font-weight="700">V<tspan font-size="11" dy="3">burden</tspan><tspan dy="-3"> = I · R</tspan><tspan font-size="11" dy="3">sh</tspan></text><text x="720" y="108" font-size="13" fill="{N}">tensione "rubata"</text><text x="720" y="126" font-size="13" fill="{N}">al circuito</text></svg>'''
D.add("Come si misura una corrente",f'''<div class="diag" style="width:88%;margin:-6px auto 0">{ser}</div><div class="two" style="align-items:start;gap:30px"><div><ul class="small">
<li>La corrente si misura <b>in serie</b>: si apre il circuito e lo strumento diventa parte del percorso.</li>
<li>Puntale rosso nella boccola <b>mA/µA</b> o <b>10 A</b>, selettore sulla funzione di corrente corretta (DC o AC).</li></ul></div><div><ul class="small">
<li>Se non conosci la corrente, parti dalla <b>portata più alta</b> (10 A) e scendi.</li>
<li>Mai mettere lo strumento in corrente <b>in parallelo</b> a una sorgente: è un cortocircuito, nel migliore dei casi salta il fusibile.</li></ul></div></div>''')
D.add("Lo shunt interno e la tensione di carico",'''<div class="two"><div><ul>
<li>Dentro lo strumento la corrente passa in una resistenza di precisione, lo <b>shunt</b>; il multimetro misura la tensione ai suoi capi.</li>
<li>Quella tensione si chiama <b>burden voltage</b> (tensione di carico): è tolta al circuito che misuri.</li>
<li>Lo shunt cambia con la portata: grande sulle portate piccole, piccolissimo sulla 10 A.</li></ul>
<table><tr><th>Portata</th><th>Shunt tipico (+ fusibile e puntali)</th></tr>
<tr><td class="l">µA</td><td class="l">100 Ω – 1 kΩ</td></tr><tr><td class="l">mA</td><td class="l">1 – 10 Ω</td></tr><tr><td class="l">10 A</td><td class="l">0,01 Ω (+ circa 0,02–0,05 Ω di fusibile e puntali)</td></tr></table>
<p class="note">Valori indicativi: il manuale li dà spesso come mV per unità di corrente (per esempio 1 mV/µA).</p></div><div>
<h3>Quando falsa la misura</h3><ul class="small"><li>Circuiti a <b>bassa tensione</b>: su 3,3 V anche 0,2 V di burden sono tanti.</li>
<li>Carichi a <b>bassa resistenza</b>: lo shunt si somma e la corrente cala.</li>
<li>Correnti che variano molto: un microcontrollore che dorme a pochi µA e si sveglia a decine di mA vede crollare la tensione sullo shunt dei µA e può <b>resettarsi</b>.</li>
<li>Sulla portata 10 A c'è spesso un <b>limite di tempo</b> (per esempio 30 s ogni qualche minuto): lo shunt scalda.</li></ul></div></div>''')
D.add("Esempio: quanto sbaglia la portata mA",'''<div class="two"><div><ul>
<li>LED su 5 V con una resistenza da 220 Ω e caduta del LED di 2 V: la corrente vera è (5 − 2) / 220 = <b>13,6 mA</b>.</li>
<li>Inserisci il multimetro sulla portata mA, con 10 Ω di shunt e circa 1 Ω tra fusibile e puntali.</li></ul>
<div class="eq">I = 3 V / (220 + 11) Ω = 13,0 mA</div>
<ul class="small"><li>Lo strumento mostra 13,0 mA, il 4,8 % in meno: non sbaglia lui, è il circuito che è cambiato.</li></ul></div><div>
<h3>Regola pratica</h3><ul class="small"><li>Confronta la resistenza dello shunt con la resistenza "vista" dal circuito: se è più dell'1 %, l'errore si vede.</li>
<li>Usa la portata più alta che dà ancora una buona risoluzione: lo shunt è più piccolo.</li>
<li>Oppure non aprire il circuito e misura la corrente <b>in tensione</b> su una resistenza che c'è già (slide successiva).</li></ul></div></div>''')
D.add("Leggere una corrente in modalità tensione",'''<div class="two"><div><ul>
<li>Se nel circuito c'è già una resistenza nota percorsa dalla corrente che ti interessa, basta misurare la tensione ai suoi capi:</li></ul>
<div class="eq">I = V / R</div>
<ul class="small"><li>Niente circuito da aprire, niente burden, niente fusibili: lo strumento resta in V ad alta impedenza.</li>
<li>Esempi: la resistenza di emettitore di un transistor, quella di source di un MOSFET, lo shunt di sensing di un alimentatore, la resistenza in serie a un LED.</li></ul></div><div>
<h3>Esempi numerici</h3><ul class="small"><li>Resistenza di emettitore da 10 Ω, leggi 0,150 V → <b>15 mA</b> di corrente di emettitore.</li>
<li>Resistenza da 0,1 Ω nel bias di un finale, leggi 25,0 mV → <b>250 mA</b> di corrente di riposo.</li>
<li>Resistenza del LED da 220 Ω, leggi 2,99 V → <b>13,6 mA</b>.</li></ul>
<p class="note">Il valore della resistenza va conosciuto con precisione: la tolleranza (1 %, 5 %) entra direttamente nella misura. Se puoi, misurala a circuito spento.</p></div></div>''')
D.add("Shunt esterni",'''<div class="two"><div><ul>
<li>Per correnti oltre i 10 A, o per misure lunghe, si usa uno <b>shunt esterno</b> e il multimetro sulla portata mV.</li>
<li>Gli shunt industriali sono specificati come "corrente / tensione": per esempio <b>50 A / 75 mV</b>, cioè 1,5 mΩ.</li>
<li>Hanno <b>quattro morsetti</b>: due grossi per la corrente, due piccoli per la misura (collegamento Kelvin). Così la resistenza dei contatti di potenza non entra nella lettura.</li></ul></div><div>
<h3>Scegliere o costruire uno shunt</h3><ul class="small"><li>Potenza dissipata: P = I²·R. Con 1,5 mΩ e 50 A: 3,75 W.</li>
<li>Lega a basso coefficiente di temperatura (manganina, costantana): il rame cambia di circa 0,4 % per °C.</li>
<li>Uno shunt piccolo dà tensioni piccole: con 1 mΩ e 1 A leggi 1 mV, serve la portata mV con buona risoluzione.</li>
<li>Mettilo sul <b>lato negativo</b> (verso massa) quando possibile: la misura è riferita a massa e più sicura.</li></ul></div></div>''')
D.add("Un cavo o una pista come shunt (stima)",'''<div class="two"><div><ul>
<li>Il rame ha resistività di circa 0,0172 Ω·mm²/m a 20 °C:</li></ul>
<div class="eq">R = 0,0172 · L(m) / S(mm²)</div>
<ul class="small"><li>Un conduttore da <b>4 mm²</b> lungo <b>2 m</b> vale circa 8,6 mΩ.</li>
<li>Con il ricetrasmettitore che assorbe 20 A, ai suoi capi leggi circa 172 mV.</li>
<li>Al contrario: leggendo 86 mV su quel conduttore, la corrente è circa 10 A.</li></ul></div><div>
<h3>Anche le piste</h3><ul class="small"><li>Una pista di rame da 35 µm, larga 1 mm, vale circa 0,5 mΩ per ogni mm di lunghezza.</li>
<li>Utile per capire quale ramo di un circuito assorbe corrente senza tagliare nulla.</li></ul>
<p class="note">È una <b>stima</b> (±20 % o peggio): temperatura, sezione reale e contatti cambiano il valore. Per una misura vera usa uno shunt o una pinza.</p></div></div>''')
D.add("Pinze amperometriche",'''<div class="two"><div><ul>
<li><b>A trasformatore</b>: solo correnti alternate. <b>A effetto Hall</b>: anche continue (le più utili in stazione).</li>
<li>Si abbraccia <b>un solo conduttore</b>: se abbracci tutto il cavo, andata e ritorno si annullano e leggi zero.</li>
<li>Le pinze DC vanno <b>azzerate</b> prima di ogni misura, lontano da campi magnetici.</li></ul></div><div>
<h3>Trucco: le spire</h3><ul class="small"><li>Per correnti piccole, fai passare il conduttore nella pinza <b>N volte</b>: la lettura si moltiplica per N.</li>
<li>Esempio: 10 spire e la pinza legge 3,0 A → la corrente vera è 0,30 A.</li>
<li>Per gli elettrodomestici esistono "separatori di linea": una prolunga con i conduttori separati, a volte con una sezione a 10 spire già pronta.</li></ul></div></div>''')
D.add("Correnti piccolissime: il multimetro come nanoamperometro",'''<div class="two"><div><ul>
<li>In V DC il multimetro è una resistenza da <b>10 MΩ</b>. Se una corrente lo attraversa, la tensione letta è proporzionale:</li></ul>
<div class="eq">I = V / 10 MΩ &nbsp; → &nbsp; 1 mV = 100 pA</div>
<ul class="small"><li>Collega sorgente → componente da provare → multimetro in V DC → ritorno alla sorgente.</li>
<li>Esempio: perdita di un condensatore elettrolitico a 12 V: leggi 0,50 V → 50 nA.</li></ul></div><div>
<h3>Attenzione</h3><ul class="small"><li>La resistenza d'ingresso va verificata sul manuale (10 MΩ è il valore più comune, alcuni hanno 1 MΩ o >1 GΩ in mV).</li>
<li>Sul componente cade la tensione della sorgente <b>meno</b> quella letta: tienila piccola rispetto alla sorgente.</li>
<li>Utile per perdite di condensatori, diodi in inversa, isolamento di circuiti stampati sporchi.</li></ul></div></div>''')
D.add("Correnti di riposo, spunto e trucchi",'''<div class="two"><div><h3>Corrente di un dispositivo che dorme</h3><ul class="small">
<li>All'accensione il dispositivo chiede molta corrente: sulla portata µA lo shunt fa cadere troppa tensione e il dispositivo si resetta.</li>
<li>Trucco: un <b>interruttore in parallelo</b> al multimetro. Chiuso durante l'accensione e il risveglio, aperto quando il dispositivo è in sleep: leggi i µA.</li>
<li>Con MIN/MAX vedi anche i picchi e il valore medio (lezione sulle funzioni nascoste).</li></ul></div><div>
<h3>Errori classici</h3><ul class="small"><li>Puntale lasciato nella boccola A dopo la misura (lezione sulla sicurezza).</li>
<li>Fusibile interrotto: lo strumento legge 0 A anche se la corrente c'è.</li>
<li>Portata 10 A usata troppo a lungo: lo shunt scalda e la lettura deriva.</li>
<li>Misurare la corrente di un ricetrasmettitore in trasmissione con i puntali sottili: i 20 A scaldano puntali e boccole. Meglio una pinza DC o uno shunt esterno.</li></ul></div></div>''')
rows=[("Serie","la corrente si misura aprendo il circuito"),("Burden","V = I·R<sub>sh</sub>: cambia il circuito che misuri"),("In tensione","I = V/R su una resistenza già presente"),("Shunt esterno","4 morsetti, es. 50 A / 75 mV = 1,5 mΩ"),
("Cavo come shunt","R ≈ 0,0172·L/S: solo una stima"),("Pinza","un solo conduttore; N spire = lettura × N"),("10 MΩ","in V DC: 1 mV = 100 pA")]
D.add("Riepilogo",'<table class="sum">'+"".join(f'<tr><td class="l" style="width:220px"><b>{a}</b></td><td class="l">{b}</td></tr>' for a,b in rows)+'</table>')
D.render(); pdf("MM_Corrente_Shunt_IV3HGA.pdf")
