import math
from deck import *
D=Deck("Il Bird 43<br>e le sue testine","Come funziona il wattmetro passante più diffuso, come scegliere e usare le testine, come misurare potenza diretta, riflessa e SWR in modo corretto","Il wattmetro RF: il Bird 43")
thru=f'''<svg viewBox="0 0 900 300" font-family="DejaVu Sans">{ARW}
<rect x="120" y="150" width="660" height="70" rx="6" fill="{L}" stroke="{N}" stroke-width="2.5"/><line x1="120" y1="185" x2="780" y2="185" stroke="{N}" stroke-width="5"/>
<text x="450" y="245" text-anchor="middle" font-size="14" fill="#555">sezione di linea coassiale da 50 Ω (conduttore centrale)</text>
<rect x="380" y="40" width="140" height="110" rx="12" fill="#fff" stroke="{C}" stroke-width="2.5"/>
<path d="M425 150 V170 H475 V150" fill="none" stroke="{C}" stroke-width="3"/>
<text x="450" y="80" text-anchor="middle" font-size="15" font-weight="700" fill="{C}">testina</text><text x="450" y="100" text-anchor="middle" font-size="13" fill="{N}">spira + diodo</text>
<line x1="410" y1="125" x2="490" y2="125" stroke="{N}" stroke-width="2.5" marker-end="url(#ar)"/><text x="450" y="142" text-anchor="middle" font-size="12" fill="#555">freccia</text>
<line x1="520" y1="70" x2="640" y2="70" stroke="{N}" stroke-width="2"/>{box(640,40,150,60,"strumento|(µA → watt)","#fff",14)}
<circle cx="110" cy="185" r="9" fill="#fff" stroke="{N}" stroke-width="2"/><circle cx="790" cy="185" r="9" fill="#fff" stroke="{N}" stroke-width="2"/>
<text x="60" y="150" text-anchor="middle" font-size="14" fill="{N}">dal TX</text><text x="840" y="150" text-anchor="middle" font-size="14" fill="{N}">al carico</text>
<line x1="30" y1="275" x2="230" y2="275" stroke="{N}" stroke-width="2" marker-end="url(#ar)"/><text x="40" y="267" font-size="13" fill="{N}">onda diretta</text>
<line x1="870" y1="275" x2="670" y2="275" stroke="{C}" stroke-width="2" marker-end="url(#ac)"/><text x="700" y="267" font-size="13" fill="{C}">onda riflessa</text></svg>'''
D.add("Che cos'è il Bird 43",f'''<div class="diag" style="width:78%;margin:-6px auto 0">{thru}</div><div class="two" style="align-items:start;gap:30px"><div><ul class="small">
<li>Un wattmetro <b>passante</b> direzionale: una sezione di linea da 50 Ω con connettori intercambiabili, uno strumento a lancetta e una <b>testina</b> (elemento, "slug") che si infila nella linea.</li>
<li>La testina contiene la spira di accoppiamento e il diodo: decide <b>banda di frequenza</b> e <b>fondo scala</b>.</li></ul></div><div><ul class="small">
<li>La testina si può <b>ruotare</b> di 180°: la freccia verso il carico misura la potenza diretta, verso il trasmettitore quella riflessa.</li>
<li>Precisione dichiarata: <b>±5 % del fondo scala</b> (tra il 10 e il 100 % della scala). SWR d'inserzione molto basso.</li></ul></div></div>''')
D.add("Le testine: lettera = banda, numero = potenza",'''<div class="two"><div><table><tr><th>Lettera</th><th>Banda</th><th>Bande radioamatoriali</th></tr>
<tr><td class="l"><b>H</b></td><td class="l">2–30 MHz</td><td class="l">HF da 80 a 10 m (non i 160 m)</td></tr>
<tr><td class="l"><b>A</b></td><td class="l">25–60 MHz</td><td class="l">10 m, 6 m</td></tr>
<tr><td class="l"><b>B</b></td><td class="l">50–125 MHz</td><td class="l">6 m, 4 m</td></tr>
<tr><td class="l"><b>C</b></td><td class="l">100–250 MHz</td><td class="l">2 m (144 MHz)</td></tr>
<tr><td class="l"><b>D</b></td><td class="l">200–500 MHz</td><td class="l">70 cm (430 MHz)</td></tr>
<tr><td class="l"><b>E</b></td><td class="l">400–1000 MHz</td><td class="l">70 cm, UHF professionale</td></tr></table></div><div><ul>
<li>Il numero è il <b>fondo scala in watt</b>: 100C = 100 W tra 100 e 250 MHz; 10D = 10 W tra 200 e 500 MHz.</li>
<li>Esistono testine da pochi watt fino a migliaia di watt (in HF le standard partono da 50 W), e testine speciali per bande strette o potenze molto basse.</li>
<li>Lo strumento ha più scale (per esempio 25, 50, 100): leggi su quella che corrisponde alla testina, con il moltiplicatore giusto.</li></ul>
<p class="note">Fuori dalla sua banda la testina ha una sensibilità diversa: la lettura non è più affidabile.</p></div></div>''')
D.add("Misurare la potenza diretta, passo per passo",'''<div class="two"><div><ol>
<li>Con il TX spento, inserisci il Bird tra trasmettitore e carico (carico fittizio o antenna), con cavi corti e buoni.</li>
<li>Controlla lo <b>zero</b> della lancetta a riposo (vite di regolazione sul quadrante).</li>
<li>Scegli la testina: <b>banda giusta</b> e fondo scala poco sopra la potenza attesa.</li>
<li>Inseriscila con la <b>freccia verso il carico</b>.</li>
<li>Trasmetti in portante (CW o FM non modulata) e leggi sulla scala corrispondente.</li></ol></div><div>
<h3>Perché il fondo scala conta</h3>
<table><tr><th>Testina</th><th>Lettura</th><th>Errore possibile</th></tr>
<tr><td class="l">100 W</td><td>80 W</td><td>±5 W (±6 %)</td></tr>
<tr><td class="l">100 W</td><td>20 W</td><td>±5 W (±25 %)</td></tr>
<tr><td class="l">25 W</td><td>20 W</td><td>±1,25 W (±6 %)</td></tr></table>
<p class="note">L'errore è una frazione del fondo scala: tieni la lettura nella parte alta della scala. Ma non superare mai il fondo scala: se non sai che potenza aspettarti, parti con una testina più grande.</p></div></div>''')
def swr(pf,pr):
    g=math.sqrt(pr/pf); return (1+g)/(1-g)
rows="".join(f'<tr><td class="l">{pf} W</td><td>{it(pr,1)} W</td><td>{it(math.sqrt(pr/pf),3)}</td><td>{it(swr(pf,pr),2)}</td><td>{it(pf-pr,1)} W</td></tr>' for pf,pr in((100,1),(100,4),(100,11.1),(50,0.5)))
D.add("Riflessa, SWR e potenza netta",f'''<div class="two"><div><ol class="small">
<li>Misura la potenza diretta P<sub>f</sub>.</li>
<li>Ruota la testina con la <b>freccia verso il trasmettitore</b>: misuri la riflessa P<sub>r</sub>.</li>
<li>Per una riflessa piccola usa una testina di fondo scala più basso (stessa banda): la lettura diventa molto più precisa.</li></ol>
{eq("|Γ| = √(P<sub>r</sub> / P<sub>f</sub>)")}{eq("SWR = (1 + |Γ|) / (1 − |Γ|)")}{eq("P<sub>netta</sub> = P<sub>f</sub> − P<sub>r</sub>")}</div><div>
<table><tr><th>P<sub>f</sub></th><th>P<sub>r</sub></th><th>|Γ|</th><th>SWR</th><th>Netta</th></tr>{rows}</table>
<p class="note">La potenza netta è quella che arriva davvero al carico (in un punto della linea senza perdite). La riflessa non "torna nel TX a bruciarlo": viene ri-riflessa e, se il TX tollera il disadattamento, finisce comunque nel carico, meno le perdite del cavo.</p></div></div>''')
D.add("Esempio: TX FM da 50 W a 145 MHz",'''<div class="two"><div><h3>Scelta delle testine</h3><ul class="small">
<li>Banda: 145 MHz → testine <b>C</b> (100–250 MHz).</li>
<li>Diretta: <b>100C</b>. La 50C avrebbe la lettura a fondo scala (più precisa) ma nessun margine se il TX eroga qualcosa in più.</li>
<li>Riflessa: <b>10C</b> o <b>5C</b>: con 1 W riflesso la 100C leggerebbe all'1 % della scala, cioè nulla di affidabile.</li></ul>
<h3>Letture</h3><ul class="small"><li>Diretta con la 100C: 48 W (±5 W).</li><li>Riflessa con la 10C: 0,8 W (±0,5 W).</li></ul></div><div>
<h3>Risultato</h3>
<div class="eq">|Γ| = √(0,8 / 48) = 0,13 → SWR ≈ 1,3</div>
<ul class="small"><li>Considerando le tolleranze, la riflessa può stare tra 0,3 e 1,3 W: con anche la tolleranza della diretta l'SWR è tra circa 1,16 e 1,42.</li>
<li>Per SWR molto bassi il Bird indica bene "è buono", ma non distingue 1,05 da 1,15: lì serve un VNA o un ponte.</li>
<li>Annota testine usate, frequenza e posizione del Bird nella linea: misurare in stazione o all'antenna dà numeri diversi se il cavo ha perdite.</li></ul></div></div>''')
D.add("Modulazioni e lettura di picco",'''<div class="two"><div><ul>
<li>La testina è tarata con una <b>portante continua</b> (CW, FM). Su questi segnali la lettura è corretta.</li>
<li>In <b>SSB</b> la lancetta segue l'inviluppo in modo lento e impreciso: legge molto meno della PEP.</li>
<li>In <b>AM</b> la potenza media aumenta con la modulazione: la lancetta "sale" quando moduli (vedi il modulo sulla potenza dello spettro).</li>
<li>Con segnali a <b>burst</b> (DMR, TETRA) legge una media che dipende dal duty cycle.</li></ul></div><div>
<h3>Misurare la PEP</h3><ul class="small"><li>Esistono versioni e accessori a <b>lettura di picco</b> (per esempio il modello 43P) che mantengono il picco dell'inviluppo.</li>
<li>In alternativa: test a due toni con lettura media. Con due toni uguali la <b>PEP è il doppio della media</b>.</li>
<li>Oppure misura la PEP in modo indiretto con l'analizzatore di spettro e un carico con prelievo.</li></ul></div></div>''')
D.add("Errori tipici con il Bird",'''<div class="two"><div><ul>
<li>Testina della <b>banda sbagliata</b>: per esempio una H (2–30 MHz) a 145 MHz. La lettura può essere molto diversa dal vero.</li>
<li>Letture a <b>fondo scala troppo basso</b>: il ±5 % del fondo scala diventa un errore enorme sulla lettura.</li>
<li><b>Freccia</b> nel verso sbagliato: diretta e riflessa scambiate.</li>
<li>Misurare dove la linea ha forte onda stazionaria con un wattmetro <b>non direzionale</b> o mal adattato.</li></ul></div><div><ul>
<li><b>Armoniche</b> e spurie: la testina somma ciò che rientra nella sua risposta; una testina di banda più alta può "vedere" le armoniche.</li>
<li><b>Connettori UHF</b> e adattatori a 145–430 MHz: introducono disadattamento e perdita.</li>
<li>Zero non controllato: un ago fuori zero sposta tutte le letture basse.</li>
<li>Testine cadute o con contatti ossidati: letture instabili (vedi il modulo su come preservarlo).</li></ul></div></div>''')
rows=[("Testina","lettera = banda, numero = fondo scala in W"),("Freccia","verso il carico: diretta; verso il TX: riflessa"),("Precisione","±5 % del fondo scala: leggi nella parte alta"),("Riflessa","usa una testina più piccola della stessa banda"),
("SWR","|Γ| = √(Pr/Pf), SWR = (1 + |Γ|)/(1 − |Γ|)"),("Modulazioni","tarato su CW/FM; per la PEP serve il picco")]
D.add("Riepilogo",'<table class="sum">'+"".join(f'<tr><td class="l" style="width:220px"><b>{a}</b></td><td class="l">{b}</td></tr>' for a,b in rows)+'</table>')
D.render(); pdf("WM_Bird43_Testine_IV3HGA.pdf")
