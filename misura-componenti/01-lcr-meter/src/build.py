from deck import *
O="#e0563b"; V="#2a9d5c"; B="#1593d1"
def tx(x,y,t,c=N,fs=15,a="middle",b=""): return f'<text x="{x}" y="{y}" font-size="{fs}" fill="{c}" text-anchor="{a}" {"font-weight=\"bold\"" if b else ""}>{t}</text>'
def wire(x1,y1,x2,y2,c=N,w=2.5): return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{c}" stroke-width="{w}"/>'
D=Deck("L'LCR meter · come funziona e cosa fa","Impedenza, misura vettoriale di tensione e corrente, ponte auto-bilanciato, modelli serie e parallelo, D, Q ed ESR, frequenza e livello di prova, collegamenti a 4 terminali e compensazioni","Misurare i componenti · LCR meter")
D.add("Che cosa misura",f'''<div class="two"><div><ul>
<li>Un multimetro misura la resistenza in <b>continua</b>. Un LCR meter applica una tensione <b>alternata sinusoidale</b> di frequenza e ampiezza note e misura l'<b>impedenza</b>:</li></ul>
{eq("Z = R + jX = |Z|·e<sup>jθ</sup>")}
<ul><li>Dalle due componenti, resistiva e reattiva, ricava tutto il resto:</li></ul>
<table><tr><th>Se X &gt; 0 (induttivo)</th><th>Se X &lt; 0 (capacitivo)</th></tr><tr><td class="l">L = X / ω</td><td class="l">C = −1 / (ω·X)</td></tr><tr><td class="l">Q = X / R</td><td class="l">D = R / |X| = ESR·ω·C</td></tr></table></div><div>
<h3>Parametri tipici sul display</h3><ul class="small"><li><b>|Z|, θ</b>: modulo e fase dell'impedenza.</li><li><b>R, X</b> oppure <b>G, B</b> (ammettenza Y = 1/Z).</li>
<li><b>Ls, Lp, Cs, Cp</b>: induttanza o capacità nel modello serie o parallelo.</li><li><b>D</b> (fattore di dissipazione), <b>Q</b> (fattore di merito), <b>ESR</b>.</li></ul>
<p class="note">Il valore che leggi vale <b>a quella frequenza e a quel livello</b>. Un componente reale non ha "una" capacità o "una" induttanza: cambiano con frequenza, tensione, corrente e temperatura.</p></div></div>''')
br=f'''<svg viewBox="0 0 600 300" width="100%">{ARW}
<circle cx="60" cy="150" r="26" fill="{L}" stroke="{N}" stroke-width="2"/>{tx(60,156,"~",N,26)}{tx(60,200,"oscillatore",N,13)}
{wire(86,150,150,150)}<rect x="150" y="125" width="110" height="50" rx="6" fill="#fde8e3" stroke="{N}" stroke-width="2"/>{tx(205,156,"componente",N,14)}
{wire(260,150,330,150)}<circle cx="330" cy="150" r="4" fill="{N}"/>{tx(330,112,"massa virtuale",N,12)}
{wire(330,150,330,230)}<polygon points="320,230 380,255 320,280" fill="{L}" stroke="{N}" stroke-width="2"/>{wire(300,268,320,268)}{wire(300,268,300,290)}{wire(290,290,310,290)}
{wire(380,255,470,255)}{wire(470,255,470,150)}<rect x="360" y="135" width="90" height="30" rx="4" fill="{L}" stroke="{N}" stroke-width="2"/>{tx(405,155,"R rif.",N,13)}
{wire(330,150,360,150)}{wire(450,150,470,150)}
{wire(205,125,205,70)}{wire(205,70,520,70)}<rect x="520" y="50" width="70" height="40" rx="6" fill="{L}" stroke="{N}" stroke-width="2"/>{tx(555,75,"V",N,15,b=1)}
{wire(470,150,520,150)}<rect x="520" y="130" width="70" height="40" rx="6" fill="{L}" stroke="{N}" stroke-width="2"/>{tx(555,155,"I·R",N,15,b=1)}
</svg>'''
D.add("Il principio: tensione e corrente come vettori",f'''<div class="two"><div>{br}</div><div><ul class="small">
<li>Un oscillatore applica una sinusoide al componente. Si misurano <b>la tensione ai suoi capi</b> e <b>la corrente</b> che lo attraversa, come caduta su una resistenza di riferimento nota.</li>
<li>Nel <b>ponte auto-bilanciato</b> un amplificatore tiene a 0 V l'estremo "basso" del componente (massa virtuale): la corrente passa tutta nella resistenza di riferimento, senza disperdersi verso massa.</li>
<li>Un <b>demodulatore sincrono</b> (o un ADC con calcolo digitale) separa per ciascuna la parte in fase e quella in quadratura rispetto all'oscillatore.</li></ul>
{eq("Z = V / I   (numeri complessi)")}
<ul class="small"><li>Il rapporto dà modulo e fase, quindi R e X. È lo stesso principio della misura vettoriale del VNA, alle basse frequenze.</li></ul></div></div>''')
D.add("Serie o parallelo?",f'''<div class="two"><div><ul>
<li>Lo strumento misura una sola Z. Per esprimerla come L o C deve scegliere un <b>modello</b>: componente ideale con una resistenza <b>in serie</b> (Cs, Ls, Rs) oppure <b>in parallelo</b> (Cp, Lp, Rp).</li>
<li>I due modelli descrivono la stessa Z e sono legati da:</li></ul>
{eq("Rp = Rs·(1 + Q²)   Cs = Cp·(1 + D²)")}
<ul class="small"><li>Con D piccolo Cs e Cp quasi coincidono (D = 0,05: differenza dello 0,25 %). Con D grande (elettrolitico vecchio, induttore con perdite) la differenza è grande.</li></ul></div><div>
<h3>Regola pratica</h3><table><tr><th>|Z| alla frequenza di prova</th><th>Modello</th><th>Perché</th></tr>
<tr><td class="l">sotto ~10 Ω</td><td class="l">serie</td><td class="l">conta la resistenza dei collegamenti e l'ESR</td></tr>
<tr><td class="l">sopra ~10 kΩ</td><td class="l">parallelo</td><td class="l">conta la resistenza di dispersione</td></tr>
<tr><td class="l">in mezzo</td><td class="l">quello del datasheet</td><td class="l">per confrontare i numeri</td></tr></table>
<ul class="small"><li>Grandi capacità e piccole induttanze: serie. Piccole capacità e grandi induttanze: parallelo.</li>
<li>Esempio: induttore 100 µH con Rs = 0,5 Ω a 100 kHz. Q = 2π·10⁵·10⁻⁴/0,5 ≈ 126; nel modello parallelo Rp ≈ 7,9 kΩ.</li></ul></div></div>''')
D.add("D, Q ed ESR",'''<div class="grid3"><div class="card"><h3>ESR</h3><p>Resistenza serie equivalente: tutte le perdite del condensatore (armature, terminali, dielettrico) riassunte in una resistenza.</p><p>Negli elettrolitici cresce con l'invecchiamento: è il primo indizio di un condensatore da sostituire.</p></div>
<div class="card"><h3>D (tan δ)</h3><p>Rapporto tra potenza persa e potenza scambiata: D = ESR·ω·C.</p><p>Elettrolitico 1000 µF con ESR = 0,05 Ω a 100 Hz: D = 0,05 · 2π · 100 · 10⁻³ ≈ 0,031. I datasheet lo danno di solito a 120 Hz.</p></div>
<div class="card"><h3>Q</h3><p>Il contrario di D: Q = X / R. Si usa per induttori e circuiti risonanti.</p><p>Un induttore con Q alto fa filtri stretti e con poche perdite; in RF interessa il Q alla frequenza di lavoro, non a 1 kHz.</p></div>
<div class="card"><h3>Angolo θ</h3><p>−90° condensatore ideale, +90° induttore ideale, 0° resistenza. Tra −89° e −90° un buon condensatore film o C0G.</p></div>
<div class="card"><h3>DCR</h3><p>Alcuni strumenti misurano anche la resistenza in continua degli avvolgimenti: diversa dalla Rs in alternata per effetto pelle e perdite del nucleo.</p></div>
<div class="card"><h3>Valori di confronto</h3><p>Ceramico C0G: D ≈ 0,001. Film: 0,001–0,01. X7R: ≈ 0,01–0,025. Elettrolitico: 0,05–0,3. Valori indicativi, il datasheet fa fede.</p></div></div>''')
D.add("Perché la frequenza conta",f'''<div class="two"><div class="fig">{svg("zf.svg")}</div><div><ul class="small">
<li>Un condensatore reale ha anche un'induttanza serie (ESL) dovuta a terminali e costruzione. Alla <b>frequenza di autorisonanza</b> (SRF) l'impedenza è minima e vale l'ESR; sopra, si comporta da induttore.</li>
<li>Un induttore ha una capacità parassita tra le spire: sopra la SRF si comporta da condensatore.</li>
<li>Esempi (ESL e capacità parassite tipiche): ceramico 100 nF con 1 nH, SRF ≈ 15,9 MHz; elettrolitico 1000 µF con 15 nH, SRF ≈ 41 kHz; induttore 100 µH con 5 pF, SRF ≈ 7,1 MHz.</li>
<li>Un LCR meter fino a 100 kHz misura bene il valore "di bassa frequenza". Per sapere come si comporta un componente in RF serve il <b>VNA</b>, o un LCR meter RF.</li></ul></div></div>''')
D.add("Livello di prova e polarizzazione",f'''<div class="two"><div class="fig">{svg("bias.svg")}</div><div><ul class="small">
<li>I ceramici ad alta costante dielettrica (X7R, X5R, Y5V) <b>perdono capacità</b> con la tensione continua applicata, ed è tanto peggio quanto più il condensatore è piccolo rispetto alla sua capacità. Un 10 µF in 0805 a 16 V può valere meno di metà.</li>
<li>Cambiano anche col <b>livello AC</b> di prova: per questo i datasheet indicano 1 kHz e 1 Vrms (0,5 V per i valori grandi).</li>
<li>Gli induttori con nucleo di ferrite cambiano con la corrente: la saturazione si vede solo con una polarizzazione in corrente continua.</li>
<li>Gli LCR meter seri regolano il livello (es. 20 mV–1 Vrms) e hanno una sorgente di <b>DC bias</b> per misurare i componenti nelle condizioni d'uso.</li></ul></div></div>''')
k4=f'''<svg viewBox="0 0 560 230" width="100%">
<rect x="20" y="40" width="130" height="150" rx="8" fill="{L}" stroke="{N}" stroke-width="2"/>{tx(85,30,"strumento",N,14,b=1)}
{"".join(tx(110,y+5,t,N,14,"end") for y,t in [(70,"Hc"),(100,"Hp"),(140,"Lp"),(170,"Lc")])}
{wire(150,70,330,70,O,3)}{wire(150,100,300,100,B,2)}{wire(150,140,300,140,B,2)}{wire(150,170,330,170,O,3)}
{wire(330,70,330,95,O,3)}{wire(330,145,330,170,O,3)}{wire(300,100,320,100,B,2)}{wire(300,140,320,140,B,2)}
<rect x="310" y="95" width="40" height="50" rx="4" fill="#fde8e3" stroke="{N}" stroke-width="2"/>{tx(380,125,"componente",N,13,"start")}
{tx(240,60,"corrente (Hc, Lc)",O,12)}{tx(240,215,"tensione (Hp, Lp): nessuna corrente, nessuna caduta",B,12)}</svg>'''
D.add("I collegamenti: 2, 3 o 4 terminali",f'''<div class="two"><div>{k4}<ul class="small">
<li>Con <b>4 terminali</b> (Kelvin) la corrente passa da due fili e la tensione si legge con altri due, attaccati direttamente al componente: la resistenza dei cavi non entra nella misura.</li>
<li>I cavi schermati (4 terminal pair) riducono anche le capacità verso l'esterno.</li></ul></div><div>
<h3>Compensazione open e short</h3><ul class="small"><li><b>Open</b>: puntali aperti, alla stessa distanza della misura. Toglie la capacità parassita (tipicamente qualche pF), che pesa sulle piccole capacità.</li>
<li><b>Short</b>: puntali in cortocircuito. Toglie resistenza e induttanza dei collegamenti (decine di mΩ, decine di nH), che pesano sulle piccole impedenze.</li>
<li>Va rifatta quando cambi frequenza, cavi o fixture.</li></ul>
<h3>Esempio</h3><ul class="small"><li>Induttore da 10 µH a 100 kHz: X = 6,28 Ω. Senza compensazione, 50 nH di collegamenti valgono 0,031 Ω: 0,5 % di errore.</li>
<li>Induttore da 1 µH a 1 kHz: X = 6,3 mΩ, meno dei soli collegamenti. Misura impossibile: serve una frequenza più alta.</li></ul></div></div>''')
D.add("Dove è preciso e dove no",f'''<div class="two"><div class="fig">{svg("acc.svg")}</div><div><ul class="small">
<li>L'accuratezza dichiarata (per esempio 0,1 %) vale in un intervallo di impedenze, di solito da qualche decina di ohm a qualche centinaio di kilohm, alla frequenza e al livello di riferimento.</li>
<li>Agli estremi l'errore cresce: con piccole impedenze contano i residui di collegamento, con grandi impedenze le capacità parassite e il rumore.</li>
<li>Trucco: scegli la frequenza in modo che il componente abbia una |Z| nella zona buona. Grandi capacità a bassa frequenza, piccole capacità e piccole induttanze ad alta frequenza.</li>
<li>Il grafico è indicativo: la curva esatta è nel datasheet dello strumento, spesso come diagramma di accuratezza in funzione di |Z| e frequenza.</li></ul></div></div>''')
D.add("Esempi pratici",'''<div class="grid3"><div class="card"><h3>Elettrolitico</h3><p>120 Hz, modello serie: Cs, D ed ESR. Confronta ESR con il datasheet; a 100 kHz leggi l'ESR che conta negli alimentatori switching.</p></div>
<div class="card"><h3>Ceramici piccoli</h3><p>1 kHz o meglio 100 kHz, modello parallelo, compensazione open accurata: pochi pF di cavi sono un errore grande su un 10 pF.</p></div>
<div class="card"><h3>Induttore di filtro</h3><p>Alla frequenza più alta disponibile, Ls e Q. Per avere il Q alla frequenza RF di lavoro serve il VNA.</p></div>
<div class="card"><h3>Toroide e AL</h3><p>Avvolgi 10 spire, misura L e ricava il fattore AL = L / N². Serve per riconoscere ferriti e ferri carbonili senza marcatura.</p></div>
<div class="card"><h3>Cavo coassiale</h3><p>Cavo aperto in fondo, misura C a 1 kHz. RG-58 ha circa 101 pF/m: 1,5 nF corrispondono a circa 15 m.</p></div>
<div class="card"><h3>Trasformatori</h3><p>Induttanza del primario a secondario aperto, induttanza di dispersione a secondario in corto: due misure, molte informazioni.</p></div></div>''')
r=[("Misura","Z complessa con tensione AC nota: V/I vettoriale"),("Modelli","serie per piccole Z, parallelo per grandi Z"),("Perdite","ESR, D = ESR·ω·C, Q = X/R"),("Frequenza","il valore vale a quella frequenza; per l'RF serve il VNA"),("Livello","ceramici X7R e ferriti cambiano con tensione e corrente"),("Collegamenti","4 terminali e compensazione open/short"),("Precisione","massima a |Z| medie: scegli la frequenza giusta")]
D.add("Riepilogo",'<table class="sum">'+"".join(f'<tr><td class="l" style="width:160px"><b>{a}</b></td><td class="l">{b}</td></tr>' for a,b in r)+'</table>')
D.render(); pdf("LCR_1_Come_funziona_IV3HGA.pdf")
