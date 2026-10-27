import re,json,base64
v=json.load(open("vals.json"))
def svg(p):
    s=open(p).read(); s=re.sub(r'<\?xml.*?\?>','',s,flags=re.S); s=re.sub(r'<!DOCTYPE.*?>','',s,flags=re.S)
    return re.sub(r'(<svg[^>]*?)\swidth="[^"]*"\s+height="[^"]*"',r'\1 width="100%"',s,count=1)
logo='<img src="data:image/png;base64,'+base64.b64encode(open("logo.png","rb").read()).decode()+'">'
css=open("style.css").read()+".sm{width:510px;margin:-18px auto 0}.sm svg{width:100%;height:auto}.two.s{grid-template-columns:510px 1fr;gap:40px}table.sum td{font-size:22px!important;padding:12px 14px!important}td.l{font-family:inherit!important;text-align:left!important}"
def eq(x): return f'<div class="eq">{x}</div>'
def it(x,d=2): return f"{x:.{d}f}".replace(".",",")
S=[]
def add(t,b): S.append((t,b))
add("",f'''<div class="cover"><div class="clogo">{logo}</div><div>
<h1>La carta di Smith</h1>
<p class="sub">Come leggerla, come muoversi e perché è lo strumento più pratico per antenne, linee e adattatori: esempi dal mondo radioamatoriale</p>
<p class="by">Elia · IV3HGA</p></div></div>''')
add("Perché la carta di Smith",f'''<div class="two"><div><ul>
<li>È il piano del <b>coefficiente di riflessione Γ</b>, su cui sono disegnati i cerchi di resistenza e gli archi di reattanza costanti.</li>
<li>Tutte le impedenze passive, da 0 a ∞, stanno <b>dentro un cerchio</b>.</li>
<li>La distanza dal centro è |Γ|, quindi l'SWR si legge "a occhio".</li>
<li>Aggiungere un componente o un pezzo di linea è un <b>movimento</b> lungo un cerchio: l'adattamento diventa geometria.</li></ul></div><div>
<h3>Per il radioamatore</h3><ul><li>Ogni NanoVNA, LiteVNA e analizzatore d'antenna la mostra: imparare a leggerla vale più di cento letture di SWR.</li>
<li>Ti dice non solo <b>quanto</b> l'antenna è disadattata, ma <b>come</b>: troppo lunga, troppo corta, R troppo alta o bassa.</li>
<li>Progetti reti a L, stub e trasformatori in λ/4 senza calcoli complicati.</li>
<li>Capisci perché la stessa antenna "cambia SWR" cambiando il cavo… e perché in realtà non è così.</li></ul></div></div>''')
g=v["ex_g"]
add("Anatomia della carta",f'''<div class="two s"><div class="sm">{svg("anatomy.svg")}</div><div><ul class="small">
<li>Si lavora con impedenze <b>normalizzate</b>: z = Z / 50 Ω. Il centro (z = 1) è il <b>50 Ω perfetto</b>.</li>
<li>Asse orizzontale: impedenze resistive pure, dal <b>corto</b> a sinistra all'<b>aperto</b> a destra.</li>
<li>Metà superiore <b>induttiva</b> (+jX), metà inferiore <b>capacitiva</b> (−jX).</li>
<li>Cerchi: R costante. Archi: X costante. Il bordo esterno è |Γ| = 1 (riflessione totale).</li>
<li>I cerchi concentrici al centro hanno <b>SWR costante</b>; quello tratteggiato è il 2:1.</li></ul>
<p class="note">Esempio: 25 + j25 Ω → z = 0,5 + j0,5 → |Γ| = {it(g[0],3)} a {it(g[1],1)}°, SWR {it(g[2])}:1.</p></div></div>''')
add("Le formule che servono",f'''<div class="two"><div>
{eq("Γ = (Z − Z0) / (Z + Z0)")}{eq("Z = Z0 · (1 + Γ) / (1 − Γ)")}{eq("SWR = (1 + |Γ|) / (1 − |Γ|)")}{eq("RL = −20·log|Γ| &nbsp; P<sub>rifl</sub> = |Γ|²")}
<p class="note">Il raggio di un punto dal centro è |Γ|: tutti i punti alla stessa distanza hanno lo stesso SWR.</p></div><div>
<table><tr><th>SWR</th><th>|Γ|</th><th>Return loss</th><th>Potenza riflessa</th></tr>
<tr><td>1,2</td><td>0,091</td><td>20,8 dB</td><td>0,8 %</td></tr>
<tr><td>1,5</td><td>0,200</td><td>14,0 dB</td><td>4,0 %</td></tr>
<tr><td>2,0</td><td>0,333</td><td>9,5 dB</td><td>11,1 %</td></tr>
<tr><td>3,0</td><td>0,500</td><td>6,0 dB</td><td>25,0 %</td></tr>
<tr><td>5,0</td><td>0,667</td><td>3,5 dB</td><td>44,4 %</td></tr></table>
<p class="note">Un SWR di 2:1 "perde" solo l'11 % della potenza, se la linea ha poche perdite. Il problema vero sono spesso la protezione del finale e le perdite aggiuntive nel cavo.</p></div></div>''')
add("Muoversi sulla carta",f'''<div class="two s"><div class="sm">{svg("moves.svg")}</div><div>
<h3>Componenti</h3><ul class="small">
<li><b>L in serie</b>: su, lungo il cerchio di R costante (senso orario).</li>
<li><b>C in serie</b>: giù, lungo lo stesso cerchio.</li>
<li><b>C in parallelo</b>: lungo il cerchio di <b>G costante</b> (in rosso, carta delle ammettenze), in senso orario.</li>
<li><b>L in parallelo</b>: lungo il cerchio di G costante, in senso antiorario.</li></ul>
<h3>Linee di trasmissione</h3><ul class="small"><li>Allontanandosi dal carico verso il trasmettitore si <b>ruota in senso orario</b> attorno al centro, a SWR costante.</li>
<li>Un giro completo corrisponde a <b>λ/2</b> di linea: ogni mezza lunghezza d'onda l'impedenza si ripete.</li></ul></div></div>''')
lo,hi=v["dip_bw"]; z71=v["z71"]
add("Esempio 1: tarare un dipolo per i 40 m",f'''<div class="two s"><div class="sm">{svg("dipole.svg")}</div><div><ul class="small">
<li>Lo sweep di un dipolo disegna un arco che attraversa l'asse reale: quel punto è la <b>risonanza</b> (X = 0), qui a 7,03 MHz con R = 65 Ω.</li>
<li>A 7,10 MHz, dove vuoi lavorare, il punto sta <b>sopra</b> l'asse: Z = {z71[0]:.0f} + j{z71[1]:.0f} Ω, cioè induttivo, quindi il dipolo è <b>troppo lungo</b>.</li>
<li>Se fosse sotto l'asse (capacitivo) sarebbe troppo corto.</li>
<li>La frequenza si sposta circa in proporzione alla lunghezza: (7,10 − 7,03) / 7,10 ≈ 1 %, cioè una ventina di cm in tutto su circa 20 m di dipolo.</li>
<li>La parte di curva dentro il cerchio 2:1 è la banda utile: qui da {it(lo/1e6)} a {it(hi/1e6)} MHz.</li></ul>
<p class="note">Il punto di risonanza non sta al centro: R = 65 Ω dà comunque SWR 1,3. Tagliare per l'SWR minimo e tagliare per X = 0 non sono la stessa cosa.</p></div></div>''')
L=v["lnet"]
add("Esempio 2: rete a L per i 20 m",f'''<div class="two s"><div class="sm">{svg("lnet.svg")}</div><div><ul class="small">
<li>Carico a 14,2 MHz: <b>25 − j40 Ω</b>, per esempio una verticale corta. Sullo schermo è in basso a sinistra: R bassa e capacitiva.</li>
<li>① <b>L in serie</b> (lato antenna): risali il cerchio r = 0,5 fino a incontrare il cerchio rosso g = 1, a 25 + j25 Ω. Servono +j{L["Xs"]:.0f} Ω, cioè <b>L ≈ {it(L["Ls"]*1e6)} µH</b>.</li>
<li>② <b>C in parallelo</b> (lato trasmettitore): scendi lungo g = 1 fino al centro. Serve B = 1/50 S, cioè <b>C ≈ {L["Cp"]*1e12:.0f} pF</b>.</li>
<li>Risultato calcolato: Z<sub>in</sub> = {it(L["zin"][0],1)} + j{it(abs(L["zin"][1]),1)} Ω.</li></ul>
<p class="note">Bonus: L in serie e C in parallelo formano un passa-basso, che attenua anche le armoniche. L'altra soluzione possibile (L in serie piccola + L in parallelo) non filtra le armoniche.</p></div></div>''')
st=v["stub"]; lam=299.792458/145*0.66
add("Esempio 3: stub di adattamento a 145 MHz",f'''<div class="two s"><div class="sm">{svg("stub.svg")}</div><div><ul class="small">
<li>Antenna VHF con <b>Z = 100 + j50 Ω</b> (SWR {it((1+abs(((2+1j)-1)/((2+1j)+1)))/(1-abs(((2+1j)-1)/((2+1j)+1))))}:1).</li>
<li>① Percorri la linea verso il trasmettitore (senso orario) finché arrivi sul cerchio g = 1: succede dopo <b>{it(st["d"],3)} λ</b>, dove y = 1 + j1.</li>
<li>② Lì metti in parallelo uno <b>stub in corto</b> che vale −j1: la sua lunghezza è <b>λ/8</b> ({it(st["l"],3)} λ).</li>
<li>Con coassiale a VF 0,66 a 145 MHz (λ ≈ {it(lam*100,1)} cm): <b>stub a {it(st["d"]*lam*100,1)} cm</b> dall'antenna, lungo <b>{it(st["l"]*lam*100,1)} cm</b>.</li></ul>
<p class="note">Lo stub in corto è anche un corto in continua per l'antenna: scarica le cariche statiche. Taralo con il VNA, perché le lunghezze reali dipendono da connettori e T.</p></div></div>''')
le=v["lossy_end"]
add("Esempio 4: il cavo che \"migliora\" l'SWR",f'''<div class="two s"><div class="sm">{svg("lossy.svg")}</div><div><ul class="small">
<li>Antenna resistiva da <b>100 Ω</b>: SWR 2:1 al punto di alimentazione.</li>
<li>Con una linea <b>senza perdite</b> il punto ruota sul cerchio a SWR 2 (tratteggiato): l'impedenza vista in stazione cambia con la lunghezza, ma <b>l'SWR no</b>.</li>
<li>Con un cavo che perde <b>3 dB</b>, la riflessione torna indietro attenuata di 6 dB: il punto descrive una <b>spirale</b> verso il centro.</li>
<li>In stazione leggi |Γ| = {it(le[0],3)}, cioè SWR <b>{it(le[1])}:1</b>, ma l'antenna è sempre a 2:1 e metà della potenza scalda il cavo.</li></ul>
<p class="note">Regola pratica: un SWR "troppo bello" su un cavo lungo, soprattutto in VHF/UHF, è un campanello d'allarme. Misura all'antenna, o compensa il cavo con la calibrazione o con l'electrical delay del VNA.</p></div></div>''')
add("Esempio 5: λ/4 e stacking di due antenne",f'''<div class="two"><div><ul>
<li>Un tratto di linea lungo <b>λ/4</b> con impedenza Zt trasforma un carico Z<sub>L</sub> in:</li></ul>
{eq("Z<sub>in</sub> = Zt² / Z<sub>L</sub> &nbsp;→&nbsp; Zt = √(Z<sub>in</sub>·Z<sub>L</sub>)")}
<ul><li>Sulla carta normalizzata a Zt è <b>mezzo giro</b> attorno al centro: il punto va sul lato opposto.</li>
<li>Funziona solo per carichi resistivi, e la banda è limitata: si allarga se il rapporto di trasformazione è piccolo.</li></ul></div><div>
<h3>Due yagi in parallelo (stacking)</h3><ol class="small"><li>Ogni antenna da 50 Ω riceve un tratto λ/4 elettrico di coassiale da <b>75 Ω</b>.</li>
<li>Ogni ramo diventa 75² / 50 = <b>112,5 Ω</b>.</li><li>Due rami in parallelo: 112,5 / 2 = <b>56,25 Ω</b>, cioè SWR 1,13:1.</li></ol>
<p class="note">Ricorda il fattore di velocità: λ/4 elettrico in un cavo con VF 0,66 è più corto di λ/4 in aria. Il VNA ti dice subito se la lunghezza è giusta: un λ/4 aperto in fondo misura un corto all'ingresso.</p></div></div>''')
add("Esempio 6: cosa fa davvero l'accordatore",f'''<div class="two"><div><ul>
<li>Un accordatore (ATU) è una rete di adattamento variabile: L e C che "spostano" il punto dell'antenna al centro della carta.</li>
<li>Con una rete a L le strade sono due:</li></ul>
<table><tr><th>Se il carico ha…</th><th>Primo elemento sul carico</th></tr>
<tr><td class="l">R &lt; 50 Ω (fuori dal cerchio r = 1)</td><td class="l">in <b>serie</b></td></tr>
<tr><td class="l">G &lt; 1/50 S (fuori dal cerchio g = 1)</td><td class="l">in <b>parallelo</b></td></tr></table>
<p class="note">Ogni punto della carta soddisfa almeno una delle due condizioni: un accordatore che può commutare l'elemento in parallelo da un lato all'altro arriva ovunque, salvo limiti di valori.</p></div><div>
<h3>Ma attenzione</h3><ul class="small"><li>L'accordatore in stazione adatta il <b>trasmettitore</b>, non l'antenna: sul cavo l'onda stazionaria resta, con le sue perdite.</li>
<li>Le reti a T (C-L-C) arrivano quasi ovunque, ma con alcune combinazioni hanno Q altissimo e perdite forti: scegli la combinazione con le <b>capacità più alte</b> possibili e la minima L.</li>
<li>Con un VNA collegato al posto del TX vedi sulla carta la traiettoria mentre giri le manopole: è il modo migliore per capire il tuo accordatore.</li></ul></div></div>''')
add("Trucchi pratici con il NanoVNA",f'''<div class="two"><div><ul>
<li><b>Marker in R + jX</b> e in valore equivalente L o C: ti dicono subito quale componente serve per compensare.</li>
<li><b>Carta delle ammettenze</b> (G + jB) quando ragioni con elementi in parallelo.</li>
<li><b>Electrical delay / port extension</b>: "srotola" il cavo e ti riporta all'antenna. Regolalo finché la traccia di un aperto in fondo al cavo si raccoglie in un punto vicino al bordo destro.</li>
<li>Se il cavo è lungo un multiplo di <b>λ/2 elettrico</b>, vedi l'impedenza dell'antenna (a quella frequenza sola).</li></ul></div><div><ul>
<li>Un <b>anello</b> nella traccia indica due risonanze accoppiate: tipico di antenne con adattatore, trappole o choke risonanti.</li>
<li>Una traccia che <b>cambia toccando il cavo</b> indica correnti di modo comune sulla calza: serve un choke.</li>
<li>Calibra con gli standard <b>dove colleghi l'antenna</b>, non sullo strumento, se vuoi leggere i valori veri.</li>
<li>Guarda sempre la <b>forma</b> della curva, non solo il minimo dell'SWR.</li></ul></div></div>''')
rows=[("Centro","50 Ω, SWR 1"),("Sopra / sotto l'asse","induttivo / capacitivo"),("Distanza dal centro","|Γ|, cioè SWR"),("L serie / C serie","su / giù lungo R costante"),
("C parallelo / L parallelo","orario / antiorario lungo G costante"),("Linea verso il TX","rotazione oraria, giro = λ/2"),("Linea con perdite","spirale verso il centro"),("λ/4","mezzo giro: Zt² / Z<sub>L</sub>")]
add("Riepilogo: la carta in 8 regole",'<table class="sum">'+"".join(f'<tr><td class="l"><b>{a}</b></td><td class="l">{b}</td></tr>' for a,b in rows)+'</table><p class="note" style="margin-top:18px">Prossimo passo consigliato: prendi il tuo VNA, misura un\'antenna e prova a prevedere dove andrà la traccia aggiungendo un componente o un pezzo di cavo.</p>')
out=[f"<!DOCTYPE html><html><head><meta charset='utf-8'><style>{css}</style></head><body>"]
for i,(t,b) in enumerate(S):
    if not t: out.append(f'<section class="slide c">{b}</section>');continue
    out.append(f'<section class="slide"><div class="hdrlogo">{logo}</div><h2>{t}</h2>{b}<div class="foot"><span>La carta di Smith · IV3HGA</span><span>{i+1}/{len(S)}</span></div></section>')
out.append("</body></html>"); open("slides.html","w").write("".join(out))
