from deck import *
O="#e0563b"; V="#2a9d5c"; B="#1593d1"
def tx(x,y,t,c=N,fs=15,a="middle",b=""): return f'<text x="{x}" y="{y}" font-size="{fs}" fill="{c}" text-anchor="{a}" {"font-weight=\"bold\"" if b else ""}>{t}</text>'
def wire(x1,y1,x2,y2,c=N,w=2.5): return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{c}" stroke-width="{w}"/>'
D=Deck("L'LCR meter · come funziona e cosa fa","Impedenza, misura vettoriale di tensione e corrente, ponte auto-bilanciato, modelli serie e parallelo, D, Q ed ESR, frequenza e livello di prova, collegamenti a 4 terminali e compensazioni","Misurare i componenti · LCR meter")
D.add("Che cosa misura",f'''<div class="two"><div><ul>
<li>L'LCR meter applica una tensione <b>alternata sinusoidale</b> di frequenza e ampiezza note e misura l'<b>impedenza</b> complessa del componente:</li></ul>
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
D.add("Dal multimetro all'LCR meter",f"""<div class="two"><div><ul>
<li>Il multimetro misura la resistenza facendo passare una piccola corrente <b>continua</b>. Un condensatore in continua è un circuito aperto, un induttore è solo la resistenza del filo: il multimetro non vede né C né L.</li>
<li>In alternata invece condensatori e induttori hanno una <b>reattanza</b>, che dipende dalla frequenza:</li></ul>
{eq("X<sub>C</sub> = 1 / (2π·f·C)    X<sub>L</sub> = 2π·f·L")}
<ul><li>L'LCR meter usa proprio questo: applica una sinusoide di frequenza nota, misura la reattanza e ne ricava C o L.</li></ul></div><div>
<h3>Quanto valgono le reattanze</h3><table><tr><th>Frequenza</th><th>1 µF</th><th>100 µH</th></tr>
<tr><td>100 Hz</td><td>1592 Ω</td><td>0,063 Ω</td></tr><tr><td>1 kHz</td><td>159 Ω</td><td>0,63 Ω</td></tr><tr><td>100 kHz</td><td>1,59 Ω</td><td>62,8 Ω</td></tr></table>
<p class="note">Lo stesso induttore da 100 µH a 100 Hz ha una reattanza di 63 mΩ, più piccola della resistenza dei puntali: a quella frequenza non si misura. A 100 kHz diventa 63 Ω, facile. La scelta della frequenza è metà della misura.</p></div></div>""")
D.add("Tensione e corrente fuori fase",f"""<div class="fig" style="width:94%">{svg("phasor.svg")}</div><div class="two" style="gap:30px"><div><ul class="small">
<li>In una resistenza tensione e corrente salgono e scendono insieme. In un condensatore la corrente <b>anticipa</b> la tensione di un quarto di periodo (90°), in un induttore la <b>segue</b> con 90° di ritardo.</li></ul></div><div><ul class="small">
<li>Un componente reale sta in mezzo: un condensatore con perdite ha un angolo di poco meno di 90°. L'LCR meter misura proprio questo <b>angolo</b> insieme al rapporto delle ampiezze: è da lì che separa la parte resistiva da quella reattiva.</li></ul></div></div>""")
D.add("La demodulazione sincrona",f"""<div class="two"><div class="fig">{svg("demod.svg")}</div><div><ul class="small">
<li>Per sapere quanto del segnale misurato è "in fase" e quanto "in quadratura" con l'oscillatore, lo si moltiplica per due copie del riferimento: una in fase (I) e una sfasata di 90° (Q).</li>
<li>La <b>media</b> di ciascun prodotto è proporzionale alla componente corrispondente. Nell'esempio il segnale ha ampiezza 1 e fase −60°: le medie valgono 0,5·cos(−60°) = 0,25 e 0,5·sin(−60°) ≈ −0,43.</li>
<li>Lo stesso si fa sulla tensione e sulla corrente; dividendo i due numeri complessi si ottiene Z.</li>
<li>Il prodotto per il riferimento scarta quasi tutto ciò che non è alla frequenza di prova (rumore, ronzio): la misura resta stabile anche con segnali piccoli. Gli strumenti moderni fanno tutto in digitale dopo l'ADC.</li></ul></div></div>""")
D.add("Un esempio passo per passo",f"""<div class="two"><div><h3>Ceramico X7R da 1 µF a 1 kHz</h3><ul>
<li>Tensione applicata: <b>1 V</b>, presa come riferimento di fase (0°).</li>
<li>Corrente misurata: <b>6,282 mA</b>, in anticipo di <b>88,99°</b>.</li></ul>
{eq("Z = V / I = 1 / 0,006282 = 159,2 Ω  con θ = −88,99°")}
<ul><li>Parte reattiva: X = 159,2·sin(−88,99°) ≈ −159,15 Ω → C = 1 / (2π·1000·159,15) = <b>1,000 µF</b>.</li>
<li>Parte resistiva: R = 159,2·cos(−88,99°) ≈ <b>2,8 Ω</b> = ESR a 1 kHz.</li>
<li>D = R / |X| = 2,8 / 159,15 ≈ <b>0,018</b>.</li></ul></div><div>
<h3>Che cosa ci dice</h3><ul class="small"><li>Un grado di differenza dall'angolo ideale (−90°) basta a rivelare 2,8 Ω di perdite: per questo serve una misura di fase molto accurata.</li>
<li>D = 0,018 è un valore normale per un X7R; un film avrebbe D ≈ 0,001, cioè un angolo di −89,94°.</li>
<li>Lo strumento fa questi conti ad ogni lettura e mostra i parametri che scegli: Cs e D, oppure Cs e ESR, oppure |Z| e θ.</li></ul></div></div>""")
D.add("Serie o parallelo: un esempio",f"""<div class="two"><div><h3>Un condensatore da 10 pF</h3><ul class="small">
<li>A 1 kHz la sua reattanza vale 15,9 MΩ. Una resistenza di dispersione di 1 GΩ è in <b>parallelo</b> e pesa poco; una resistenza serie di qualche ohm è del tutto invisibile.</li>
<li>Il modello giusto è il parallelo (Cp, Rp o D). Il modello serie darebbe un'ESR di pochi kilohm senza alcun significato fisico.</li></ul>
<h3>Un elettrolitico da 1000 µF</h3><ul class="small"><li>A 120 Hz la reattanza vale 1,33 Ω, confrontabile con un'ESR di 0,05–0,1 Ω. Le perdite sono in <b>serie</b>: modello Cs ed ESR.</li></ul></div><div>
<h3>Lo stesso componente, due numeri</h3><ul class="small"><li>Con D piccolo Cs ≈ Cp e la scelta non cambia quasi nulla.</li>
<li>Con D = 0,3 (elettrolitico esaurito) Cs = Cp·1,09: il 9 % di differenza solo per aver scelto il modello sbagliato.</li>
<li>Un induttore 100 µH con Q = 126 a 100 kHz ha Rs = 0,5 Ω oppure Rp ≈ 7,9 kΩ: sono la stessa cosa, viste in due modi.</li></ul>
<p class="note">Regola: usa il modello in cui il "difetto" è fisicamente presente, e quando confronti con un datasheet usa lo stesso modello e la stessa frequenza.</p></div></div>""")
D.add("ESR e invecchiamento degli elettrolitici",f"""<div class="two"><div><ul>
<li>Negli elettrolitici l'elettrolita si asciuga col calore e col tempo: la <b>capacità cala</b> e soprattutto l'<b>ESR sale</b>.</li>
<li>Un'ESR alta scalda il condensatore (P = I²·ESR con la corrente di ripple), che invecchia ancora più in fretta: negli alimentatori switching è la causa di guasto più comune.</li>
<li>La capacità spesso è ancora "quasi giusta" quando l'ESR è già fuori: misurare solo C non basta.</li></ul></div><div>
<h3>Esempio indicativo, 1000 µF 25 V</h3><table><tr><th></th><th>Nuovo</th><th>Invecchiato</th></tr><tr><td class="l">Cs a 120 Hz</td><td>1000 µF</td><td>820 µF</td></tr><tr><td class="l">ESR a 100 kHz</td><td>0,03 Ω</td><td>0,6 Ω</td></tr><tr><td class="l">Calore con 1 A di ripple</td><td>30 mW</td><td>600 mW</td></tr></table>
<ul class="small"><li>Una regola pratica diffusa: sostituire quando l'ESR supera circa il doppio del valore di datasheet alla stessa frequenza.</li>
<li>L'ESR si misura a 100 kHz per i condensatori degli switching, a 120 Hz per i livellamenti a 50 Hz.</li></ul></div></div>""")
D.add("L'autorisonanza: calcolarla",f"""<div class="two"><div>{eq("f<sub>SRF</sub> = 1 / (2π·√(L·C))")}<ul>
<li>Per un condensatore L è l'induttanza parassita (ESL): pochi nH per un SMD piccolo, 10–20 nH per un elettrolitico con terminali.</li>
<li>Per un induttore C è la capacità tra le spire: da frazioni di pF a decine di pF.</li></ul>
<table><tr><th>Componente</th><th>Parassita</th><th>SRF</th></tr><tr><td class="l">ceramico 100 nF</td><td>1 nH</td><td>15,9 MHz</td></tr><tr><td class="l">elettrolitico 1000 µF</td><td>15 nH</td><td>41 kHz</td></tr><tr><td class="l">induttore 100 µH</td><td>5 pF</td><td>7,1 MHz</td></tr></table></div><div>
<h3>Conseguenze per chi fa radio</h3><ul class="small"><li>Un 100 nF di disaccoppiamento in 2 m (145 MHz) è già un induttore: per questo si mettono in parallelo valori diversi (100 nF + 1 nF + 100 pF), ognuno efficace nella sua banda.</li>
<li>Un'impedenza RF da 100 µH sopra 7 MHz lascia passare l'RF attraverso la sua capacità parassita: in 20 m non blocca più nulla.</li>
<li>Un elettrolitico in uscita a un alimentatore switching è un induttore sopra qualche decina di kHz: servono ceramici in parallelo.</li>
<li>L'LCR meter non vede nulla di tutto questo sotto 100 kHz: si misura col VNA.</li></ul></div></div>""")
D.add("Scegliere frequenza, livello e modello",'''<table><tr><th>Componente</th><th>Frequenza</th><th>Livello</th><th>Modello e parametri</th></tr>
<tr><td class="l">Elettrolitico, livellamento rete</td><td class="l">120 Hz (100 Hz)</td><td class="l">0,5–1 V</td><td class="l">Cs, D o ESR</td></tr>
<tr><td class="l">Elettrolitico per switching</td><td class="l">100 kHz</td><td class="l">0,5–1 V</td><td class="l">Cs, ESR</td></tr>
<tr><td class="l">Ceramico fino a 10 µF</td><td class="l">1 kHz</td><td class="l">1 V (0,5 V se grande)</td><td class="l">Cp o Cs, D</td></tr>
<tr><td class="l">Ceramico sotto 100 pF</td><td class="l">100 kHz (o 1 MHz se disponibile)</td><td class="l">1 V</td><td class="l">Cp, D</td></tr>
<tr><td class="l">Film</td><td class="l">1 kHz</td><td class="l">1 V</td><td class="l">Cs, D</td></tr>
<tr><td class="l">Induttore di potenza</td><td class="l">100 kHz</td><td class="l">basso; con DC bias se possibile</td><td class="l">Ls, Q, Rdc</td></tr>
<tr><td class="l">Induttore RF piccolo</td><td class="l">la più alta disponibile</td><td class="l">basso</td><td class="l">Ls, Q (poi VNA)</td></tr>
<tr><td class="l">Resistenza</td><td class="l">1 kHz o DC</td><td class="l">1 V</td><td class="l">R; con X si vede l'induttanza dei filo-avvolti</td></tr></table>
<p class="note">Per i confronti vale sempre la condizione del datasheet: stessa frequenza, stesso livello, stesso modello.</p>''')
D.add("Puntali e fixture",'''<div class="grid3"><div class="card"><h3>Pinze Kelvin</h3><p>Ogni ganascia ha due contatti isolati: uno porta la corrente, l'altro legge la tensione. Sono il modo pratico di fare la misura a 4 terminali su componenti con terminali.</p></div>
<div class="card"><h3>Fixture per componenti</h3><p>Zoccoli a molla o a vite collegati direttamente ai 4 terminali dello strumento: minimi residui, misure ripetibili su componenti a terminali assiali e radiali.</p></div>
<div class="card"><h3>Pinzette SMD</h3><p>Per componenti 0402–1206. Residui più alti: la compensazione open/short con le pinzette stesse è indispensabile.</p></div>
<div class="card"><h3>Cavi 4 terminal pair</h3><p>Quattro coassiali con le calze unite in fondo: la corrente di andata e ritorno corre nello stesso cavo e il campo si annulla. Si dichiara la lunghezza allo strumento.</p></div>
<div class="card"><h3>Coccodrilli comuni</h3><p>Vanno bene per resistenze e capacità medie. Per piccole impedenze (mΩ, nH) o grandi impedenze (pF) sono la prima fonte di errore.</p></div>
<div class="card"><h3>Mani e tavolo</h3><p>Un dito vicino a un condensatore da pochi pF aggiunge capacità; un piano metallico sotto un induttore ne cambia L e Q. Misura lontano da masse e fermo.</p></div></div>''')
D.add("La compensazione passo per passo",f"""<div class="two"><div><h3>Procedura</h3><ol>
<li>Imposta frequenza e livello che userai per la misura.</li>
<li>Collega puntali o fixture esattamente come per la misura.</li>
<li><b>Open</b>: puntali aperti, alla distanza dei terminali del componente. Avvia la correzione.</li>
<li><b>Short</b>: puntali chiusi con una barretta corta e spessa, o con le ganasce a contatto. Avvia la correzione.</li>
<li>Se lo strumento la prevede, <b>load</b>: misura un componente di riferimento noto, simile a quelli da misurare.</li>
<li>Misura. Se cambi frequenza, cavi o fixture, ripeti.</li></ol></div><div>
<h3>Che cosa fa lo strumento</h3><ul class="small"><li>Con l'open misura l'ammettenza parassita Yo (capacità e dispersione dei puntali); con lo short l'impedenza residua Zs (resistenza e induttanza dei collegamenti).</li>
<li>Poi corregge ogni misura con un modello semplice:</li></ul>
{eq("Z<sub>vera</sub> ≈ (Z<sub>mis</sub> − Zs) / (1 − (Z<sub>mis</sub> − Zs)·Yo)")}
<ul class="small"><li>È la stessa idea della calibrazione SOL del VNA, in forma più semplice.</li></ul></div></div>""")
D.add("Tre misure con i numeri",'''<div class="grid3"><div class="card"><h3>Toroide sconosciuto</h3><p>10 spire di filo, misura a 100 kHz: L = 40 µH.</p><p>AL = L / N² = 40 µH / 100 = <b>400 nH/spira²</b>. Un valore così alto indica una ferrite, non un ferro carbonile (che sta sotto i 100 nH/spira²).</p><p>Per 25 µH servono N = √(25000 / 400) ≈ 8 spire.</p></div>
<div class="card"><h3>Quanto è lungo questo cavo?</h3><p>Matassa di RG-58 aperta in fondo, a 1 kHz: Cp = 1,52 nF.</p><p>RG-58 ha circa 101 pF/m: 1520 / 101 ≈ <b>15 m</b>.</p><p>Con l'altro capo in corto si misura invece l'induttanza: circa 0,25 µH/m.</p></div>
<div class="card"><h3>Elettrolitico sospetto</h3><p>1000 µF dichiarati, a 120 Hz: Cs = 940 µF, D = 0,09.</p><p>ESR = D / (ω·C) = 0,09 / (2π·120·940·10⁻⁶) ≈ <b>0,13 Ω</b>.</p><p>Si confronta con il datasheet alla stessa frequenza prima di decidere.</p></div></div>''')
D.add("Errori comuni",'''<div class="two"><div><ul>
<li><b>Frequenza sbagliata</b>: piccole induttanze a 1 kHz, grandi capacità a 100 kHz. La |Z| finisce fuori dalla zona buona.</li>
<li><b>Niente compensazione</b>, o fatta a un'altra frequenza o con altri puntali.</li>
<li><b>Modello sbagliato</b>: Cs al posto di Cp su piccoli condensatori, o confronti con un datasheet che usa l'altro modello.</li>
<li><b>Componente in circuito</b>: tutto quello che è in parallelo entra nella misura.</li></ul></div><div><ul>
<li><b>Condensatori carichi</b>: possono danneggiare l'ingresso. Scaricali sempre; gli strumenti seri hanno protezioni, ma hanno un limite di energia.</li>
<li><b>Dimenticare il livello</b>: un X7R misurato a 0,1 V e a 1 V dà valori diversi, e senza DC bias non si vede la perdita in esercizio.</li>
<li><b>Fidarsi di più cifre</b>: cinque cifre sul display non significano cinque cifre di precisione.</li>
<li><b>Mani e metallo vicini</b> durante la misura di pF e nH.</li></ul></div></div>''')
ORDER=["Dal multimetro all'LCR meter","Che cosa misura","Tensione e corrente fuori fase","Il principio: tensione e corrente come vettori","La demodulazione sincrona","Un esempio passo per passo","Serie o parallelo?","Serie o parallelo: un esempio","D, Q ed ESR","ESR e invecchiamento degli elettrolitici","Perché la frequenza conta","L'autorisonanza: calcolarla","Livello di prova e polarizzazione","Scegliere frequenza, livello e modello","I collegamenti: 2, 3 o 4 terminali","Puntali e fixture","La compensazione passo per passo","Dove è preciso e dove no","Esempi pratici","Tre misure con i numeri","Errori comuni","Riepilogo"]
_d={t:b for t,b in D.S}; assert set(_d)==set(ORDER), set(_d)^set(ORDER)
D.S=[(t,_d[t]) for t in ORDER]
D.render(); pdf("LCR_1_Come_funziona_IV3HGA.pdf")
