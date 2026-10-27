import json
from deck import *
v=json.load(open("vals.json"))
D=Deck("Bolometri<br>e termistori","Il principio della sostituzione in continua, il ponte autobilanciato, come si fa una misura passo per passo, cal factor e incertezze","Il wattmetro RF: bolometri e termistori")
def R(x1,y1,x2,y2,lab,lx,ly,fill="#fff",col=N): return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{N}" stroke-width="2.2"/><rect x="{(x1+x2)/2-22}" y="{(y1+y2)/2-9}" width="44" height="18" rx="3" fill="{fill}" stroke="{col}" stroke-width="2" transform="rotate({45 if (x2-x1)*(y2-y1)>0 else -45} {(x1+x2)/2} {(y1+y2)/2})"/><text x="{lx}" y="{ly}" font-size="14" fill="{col}" font-weight="{700 if col!=N else 400}">{lab}</text>'
bridge=f'''<svg viewBox="0 -5 620 365" font-family="DejaVu Sans">{ARW}
{R(220,50,100,170,"R",120,105)}{R(220,50,340,170,"R",310,105)}{R(100,170,220,290,"R",120,245)}{R(340,170,220,290,"R<tspan font-size='10' dy='3'>T</tspan>",300,268,"#e8f6fd",C)}
<g fill="{N}"><circle cx="220" cy="50" r="5"/><circle cx="100" cy="170" r="5"/><circle cx="340" cy="170" r="5"/><circle cx="220" cy="290" r="5"/></g>
<line x1="220" y1="290" x2="220" y2="305" stroke="{N}" stroke-width="2"/><line x1="205" y1="305" x2="235" y2="305" stroke="{N}" stroke-width="2"/><line x1="211" y1="311" x2="229" y2="311" stroke="{N}" stroke-width="2"/>
<path d="M100 170 H60 V335 H460 V235" fill="none" stroke="{N}" stroke-width="2"/><path d="M340 170 H460 V205" fill="none" stroke="{N}" stroke-width="2"/>
<polygon points="460,190 515,220 460,250" fill="#fff" stroke="{N}" stroke-width="2"/><text x="470" y="275" font-size="12" fill="#555">amplificatore</text>
<path d="M515 220 H570 V20 H220 V50" fill="none" stroke="{N}" stroke-width="2"/>
<text x="580" y="110" font-size="15" font-weight="700" fill="{N}">V</text><text x="300" y="13" font-size="12" fill="#555">tensione di alimentazione del ponte</text>
{ln(400,290,300,240,C)}<text x="405" y="300" font-size="14" fill="{C}" font-weight="700">RF in</text>
<text x="370" y="355" font-size="12" fill="#555">R<tspan font-size="9" dy="3">T</tspan><tspan dy="-3"> = termistore</tspan></text></svg>'''
D.add("Il principio",'''<div class="two"><div><ul>
<li>Un piccolo elemento resistivo assorbe la potenza RF e si scalda. La sua <b>resistenza cambia con la temperatura</b>.</li>
<li><b>Termistore</b>: una perlina di semiconduttore con coefficiente <b>negativo</b> (scaldandosi la resistenza scende). Robusto e stabile, ma lento.</li>
<li><b>Bolometro</b> (barretter): un filo sottilissimo di platino con coefficiente <b>positivo</b>. Veloce, ma delicatissimo.</li></ul></div><div>
<h3>Perché sono importanti</h3><ul class="small"><li>La misura si riconduce a una <b>potenza in continua</b>, cioè a tensioni e resistenze misurabili con grande precisione.</li>
<li>Rispondono al <b>vero valore efficace</b>: armoniche e modulazione non falsano la lettura, conta solo il calore.</li>
<li>Per decenni le testine a termistore sono state lo standard per tarare gli altri wattmetri, e lo sono ancora come standard di trasferimento.</li></ul></div></div>''')
D.add("Il ponte autobilanciato",f'''<div class="two"><div class="diag">{bridge}</div><div><ul class="small">
<li>Il termistore è un lato di un ponte di Wheatstone. Un amplificatore fornisce al ponte la tensione necessaria a tenerlo <b>sempre bilanciato</b>.</li>
<li>In equilibrio il termistore ha esattamente la resistenza R (per esempio 200 Ω): la corrente continua lo scalda fino a quel punto.</li>
<li>Quando arriva la RF, il termistore si scalda di più: l'amplificatore <b>riduce la continua</b> quanto basta per riportarlo a R.</li>
<li>La diminuzione di potenza continua è esattamente uguale alla potenza RF assorbita.</li></ul>
<p class="note">Il termistore resta sempre alla stessa temperatura e resistenza: per questo resta adattato a 50 Ω e la misura non dipende dalla sua curva.</p></div></div>''')
D.add("La sostituzione in continua, con i numeri",f'''<div class="two"><div class="fig">{svg("dcsub.svg")}</div><div>
{eq("P<sub>DC</sub> = V² / (4·R)")}{eq("P<sub>RF</sub> = (V<sub>0</sub>² − V<sub>1</sub>²) / (4·R)")}
<ul class="small"><li>Con il termistore in un ponte a lati uguali, ai suoi capi c'è metà della tensione V: da qui il fattore 4.</li>
<li>Esempio con R = 200 Ω: senza RF V<sub>0</sub> = 4,000 V → {it(v["P0"])} mW. Con RF V<sub>1</sub> = 3,899 V → {it(v["P1"])} mW.</li>
<li>P<sub>RF</sub> = {it(v["Prf"],3)} mW, cioè circa <b>0 dBm</b>.</li></ul>
<p class="note">Una variazione di appena 0,1 V corrisponde a 1 mW: il voltmetro deve essere preciso e stabile, e la temperatura ambiente non deve cambiare durante la misura.</p></div></div>''')
D.add("Compensazione e azzeramento",'''<div class="two"><div><ul>
<li>Anche la temperatura ambiente scalda o raffredda il termistore, e il ponte la scambierebbe per RF.</li>
<li>Le testine coassiali hanno un <b>secondo termistore</b>, nello stesso blocco metallico ma senza RF, in un secondo ponte: misura solo la "deriva termica" e lo strumento la sottrae.</li>
<li>Resta comunque necessario <b>azzerare</b> lo strumento senza RF prima di ogni serie di misure.</li></ul></div><div>
<h3>In pratica</h3><ul class="small"><li>Accendi strumento e testina e aspetta che il blocco sia in equilibrio termico (anche mezz'ora per misure precise).</li>
<li>Non toccare la testina con le mani durante la misura e tienila lontana da correnti d'aria e fonti di calore.</li>
<li>Azzera sulla portata più sensibile che userai, con la testina collegata al circuito ma senza RF.</li>
<li>Se la lettura "cammina" a RF spenta, rifai lo zero: la deriva limita la misura di potenze molto basse.</li></ul></div></div>''')
D.add("Un classico: l'HP 432A con testina a termistore",'''<div class="two"><div><ul>
<li>Il 432A è il power meter a termistore più diffuso nei laboratori e nel surplus. Si usa con testine coassiali come la <b>478A</b> o la <b>8478B</b>.</li>
<li>Portate da pochi µW a 10 mW fondo scala, lettura su strumento analogico in mW e dBm.</li>
<li>Ha una regolazione per la <b>resistenza della testina</b> (100 o 200 Ω) e una manopola per il <b>cal factor</b>.</li>
<li>Porta fuori le tensioni del ponte: con un buon voltmetro si applica la formula della sostituzione DC e si ottiene una precisione molto migliore della lancetta.</li></ul></div><div>
<h3>Cosa controllare se lo compri usato</h3><ul class="small"><li>La testina è la parte delicata: verifica la sua resistenza di lavoro e che lo zero sia stabile.</li>
<li>Prova la lettura con un riferimento noto (per esempio un'uscita da 1 mW a 50 MHz di un altro power meter).</li>
<li>Controlla la tabella dei cal factor sull'etichetta della testina.</li>
<li>Connettori N in buono stato: un connettore rovinato introduce disadattamento e errori.</li></ul></div></div>''')
D.add("Fare una misura, passo per passo",'''<div class="two"><div><ol>
<li>Accendi e lascia stabilizzare strumento e testina.</li>
<li>Imposta la resistenza della testina e la portata più alta.</li>
<li>Collega la testina al circuito con la RF spenta e <b>azzera</b>.</li>
<li>Imposta il <b>cal factor</b> per la frequenza di misura.</li>
<li>Accendi la RF e scendi di portata finché la lettura è nella parte alta della scala.</li>
<li>Leggi, poi spegni la RF e ricontrolla lo zero.</li></ol></div><div>
<h3>Livelli</h3><ul class="small"><li>Le testine a termistore lavorano fino a circa <b>10 mW (+10 dBm)</b>: per potenze più alte servono attenuatori o accoppiatori calibrati davanti.</li>
<li>Esempio: TX da 100 W (+50 dBm) → attenuatore di potenza da 30 dB + attenuatore da 20 dB → 0 dBm sulla testina.</li>
<li>L'incertezza degli attenuatori si somma a quella del power meter: usa attenuatori di cui conosci il valore alla frequenza di misura.</li></ul></div></div>''')
D.add("Cal factor ed efficienza",'''<div class="two"><div><ul>
<li>Non tutta la potenza che arriva alla testina finisce nel termistore: un po' viene riflessa, un po' si perde nella testina.</li></ul>
<div class="eq">K = η<sub>e</sub> · (1 − |Γ|²)</div><div class="eq">P<sub>incidente</sub> = P<sub>letta</sub> / K</div>
<ul class="small"><li>η<sub>e</sub> è l'<b>efficienza effettiva</b> (potenza misurata / potenza assorbita), |Γ| il coefficiente di riflessione della testina.</li>
<li>Il cal factor è scritto sulla testina per varie frequenze; impostandolo, lo strumento corregge da solo.</li></ul></div><div>
<h3>Esempio</h3><ul class="small"><li>A 1 GHz la testina ha K = 0,95. Lo strumento, senza correzione, legge 0,90 mW.</li>
<li>Potenza incidente: 0,90 / 0,95 = <b>0,947 mW</b>.</li>
<li>Con la manopola del cal factor su 95 % lo strumento mostra direttamente questo valore.</li></ul>
<p class="note">Il cal factor varia con la frequenza: usa il valore più vicino, o interpola, e annota quale hai usato.</p></div></div>''')
g=0.2*0.0909
up=((1+g)**2-1)*100; dn=(1-(1-g)**2)*100
D.add("L'incertezza di disadattamento",f'''<div class="two"><div><ul>
<li>Se né la sorgente né la testina sono perfettamente a 50 Ω, le riflessioni multiple tra le due cambiano la potenza che arriva alla testina, di una quantità che <b>non si conosce</b> (dipende dalle fasi).</li></ul>
<div class="eq">limiti = (1 ± |Γ<sub>s</sub>|·|Γ<sub>t</sub>|)² − 1</div>
<p class="note">Esempio: sorgente con SWR 1,5 (|Γ| = 0,2) e testina con SWR 1,2 (|Γ| = 0,091): ±{it(up,1)} %, cioè circa ±0,16 dB.</p></div><div>
<h3>Come ridurla</h3><ul class="small"><li>Spesso è la <b>componente d'incertezza più grande</b>, più dell'errore dello strumento.</li>
<li>Migliora l'adattamento della sorgente con un attenuatore da 6–10 dB davanti alla testina (se il livello lo permette).</li>
<li>Usa adattatori e cavi di buona qualità ed evita lunghe catene di adattatori.</li>
<li>Misura gli SWR con un VNA, così conosci |Γ<sub>s</sub>| e |Γ<sub>t</sub>| invece di stimarli.</li></ul></div></div>''')
D.add("Il bolometro (barretter)",'''<div class="two"><div><ul>
<li>Un filo di platino di pochi micron, in un supporto coassiale o in guida d'onda: si scalda in millisecondi.</li>
<li>Usato nello stesso tipo di ponte, ma soprattutto nelle misure di <b>SWR con linea fessurata</b>: la RF è modulata a 1 kHz e il bolometro, abbastanza veloce, restituisce un segnale a 1 kHz letto da un voltmetro selettivo.</li>
<li>Lavora a potenze di pochi mW o meno.</li></ul></div><div>
<h3>Perché oggi è raro</h3><ul class="small"><li>È <b>delicatissimo</b>: pochi volte la potenza nominale, anche per un attimo, bastano a fondere il filo.</li>
<li>Termistori, termocoppie e diodi moderni lo hanno sostituito quasi ovunque.</li>
<li>Se ne trovi uno nel surplus, trattalo come un fusibile di precisione: attenuatori davanti sempre, e niente scariche statiche.</li></ul></div></div>''')
rows=[("Principio","la RF scalda, il ponte sostituisce con la continua"),("Formula","P<sub>RF</sub> = (V<sub>0</sub>² − V<sub>1</sub>²) / (4R)"),("Termistore","robusto, lento, fino a ~10 mW"),("Bolometro","veloce, delicatissimo, SWR a 1 kHz"),
("Zero","sempre, a RF spenta e testina in equilibrio termico"),("Cal factor","P<sub>inc</sub> = P<sub>letta</sub> / K"),("Disadattamento","(1 ± |Γs||Γt|)² − 1: spesso l'incertezza maggiore")]
D.add("Riepilogo",'<table class="sum">'+"".join(f'<tr><td class="l" style="width:240px"><b>{a}</b></td><td class="l">{b}</td></tr>' for a,b in rows)+'</table>')
D.render(); pdf("WM_Bolometri_Termistori_IV3HGA.pdf")
