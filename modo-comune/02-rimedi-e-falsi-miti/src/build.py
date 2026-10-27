from deck import *
O="#e0563b"; V="#2a9d5c"
def tx(x,y,t,c=N,fs=15,a="middle",b=""): return f'<text x="{x}" y="{y}" font-size="{fs}" fill="{c}" text-anchor="{a}" {"font-weight=\"bold\"" if b else ""}>{t}</text>'
def wire(x1,y1,x2,y2,c=N,w=3,d=""): return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{c}" stroke-width="{w}" {d}/>'
def gnd(x,y): return wire(x,y,x,y+14)+wire(x-14,y+14,x+14,y+14)+wire(x-9,y+20,x+9,y+20)+wire(x-4,y+26,x+4,y+26)
def cap(x,y): return wire(x,y,x,y+12)+wire(x-12,y+12,x+12,y+12)+wire(x-12,y+19,x+12,y+19)+wire(x,y+19,x,y+31)
def panel(ox,title,col,mode,lines):
    s=f'<g transform="translate({ox},0)">'+tx(170,26,title,col,17,b=1)
    s+=f'<rect x="10" y="50" width="70" height="60" rx="6" fill="{L}" stroke="{N}" stroke-width="2"/><rect x="260" y="50" width="70" height="60" rx="6" fill="{L}" stroke="{N}" stroke-width="2"/>'
    s+=tx(45,85,"A",N,15)+tx(295,85,"B",N,15)
    s+=wire(80,80,260,80,N,2)+f'<rect x="80" y="68" width="180" height="24" fill="none" stroke="#8a6d1f" stroke-width="2.5" stroke-dasharray="6 4"/>'
    s+=wire(45,110,45,140)+gnd(45,140)+wire(295,110,295,140)+gnd(295,140)
    s+=wire(86,92,86,125,"#8a6d1f",2.5)+wire(86,125,45,125,"#8a6d1f",2.5)
    if mode=="both": s+=wire(254,92,254,125,"#8a6d1f",2.5)+wire(254,125,295,125,"#8a6d1f",2.5)+wire(45,175,295,175,V,5)+tx(170,198,"conduttore di equipotenzialità",V,13)
    if mode=="cap": s+=wire(254,92,254,105,"#8a6d1f",2.5)+cap(254,105)+wire(254,136,295,136,"#8a6d1f",2.5)+tx(222,128,"10 nF",N,13,"end")
    if mode=="one": s+=tx(250,128,"aperta",O,13,"end")
    for i,(t,c) in enumerate(lines): s+=tx(170,230+i*22,t,c,14)
    return s+"</g>"
myth=f'''<svg viewBox="0 0 1080 320" width="100%">
{panel(0,"Calza a terra da un solo lato",O,"one",[("50 Hz: nessun anello di massa ✓",V),("RF: la calza aperta è un'antenna ✗",O),("nessuna schermatura magnetica ✗",O)])}
{panel(370,"Calza a terra dai due lati, a 360°",V,"both",[("schermatura elettrica e magnetica ✓",V),("la corrente a 50 Hz va sul conduttore",V),("di equipotenzialità, non sulla calza",V)])}
{panel(740,"Soluzione ibrida",C,"cap",[("50 Hz: aperto (10 nF ≈ 318 kΩ) ✓",V),("RF: chiuso (a 10 MHz ≈ 1,6 Ω) ✓",V),("quando non si può fare di meglio",N)])}</svg>'''
D=Deck("Le correnti di modo comune · rimedi e falsi miti","I choke e le ferriti, dove metterli e come misurarli, le masse e gli anelli a 50 Hz, il mito della calza collegata da un solo lato e le buone pratiche delle norme EMC","Capitolo 12 · modo comune · 2")
D.add("Il choke: un'impedenza solo per il modo comune",f'''<div class="two"><div class="fig">{svg("chokes.svg")}</div><div><ul class="small">
<li>Avvolgendo il coassiale su una ferrite (o in spire), la corrente utile I1/I2 non vede nulla: i suoi campi si annullano dentro il cavo.</li>
<li>La corrente sulla faccia esterna, invece, trova un'<b>impedenza in serie</b> alta: il modo comune viene bloccato.</li>
<li>Obiettivo pratico: almeno <b>1 kΩ</b>, meglio <b>5 kΩ</b> sulle bande dove serve; sotto qualche centinaio di ohm il choke serve a poco.</li>
<li>Le curve sono indicative: le impedenze reali dipendono da ferrite, numero di spire e disposizione.</li></ul></div></div>''')
D.add("Resistivo è meglio di reattivo",f'''<div class="two"><div class="fig">{svg("rx.svg")}</div><div><ul class="small">
<li>Il coassiale avvolto in aria è un circuito risonante: alla risonanza l'impedenza è altissima, ma lontano è quasi solo <b>reattanza</b> (induttiva sotto, capacitiva sopra).</li>
<li>Una reattanza può andare in <b>risonanza</b> con la reattanza della calza e aumentare la corrente di modo comune, invece di ridurla.</li>
<li>La ferrite mix 31 o 43 alle frequenze HF è soprattutto <b>resistiva</b>: assorbe la corrente di modo comune e la trasforma in calore, su una banda larga.</li>
<li>Per questo i choke su ferrite sono più affidabili delle spire in aria, che vanno bene su una sola banda.</li></ul></div></div>''')
D.add("Tipi di choke e ferriti",'''<div class="two"><div><table><tr><th>Tipo</th><th>Pregi</th><th>Limiti</th></tr>
<tr><td class="l">Spire di coassiale in aria</td><td class="l">economico, regge qualsiasi potenza</td><td class="l">stretto in banda, reattivo</td></tr>
<tr><td class="l">Perline sul coassiale (W2DU)</td><td class="l">compatto, resistivo</td><td class="l">impedenza bassa in HF basse</td></tr>
<tr><td class="l">Coassiale su toroide</td><td class="l">alta impedenza su più bande</td><td class="l">cavo con raggio di curvatura adatto</td></tr>
<tr><td class="l">Bifilare su toroide (balun 1:1 di corrente)</td><td class="l">compatto, alta impedenza</td><td class="l">dielettrico e riscaldamento da controllare</td></tr>
<tr><td class="l">Ferrite a scatto su cavi di servizio</td><td class="l">semplice</td><td class="l">poche spire: impedenza modesta</td></tr></table></div><div>
<h3>Quale ferrite</h3><table><tr><th>Mix</th><th>Uso indicativo</th></tr><tr><td class="l">31</td><td class="l">1–300 MHz, il migliore in HF basse</td></tr><tr><td class="l">43</td><td class="l">20–250 MHz, HF alte e VHF</td></tr><tr><td class="l">61</td><td class="l">200 MHz – 2 GHz, VHF/UHF</td></tr></table>
<p class="note">Più spire aumentano l'impedenza, ma anche la capacità tra le spire: oltre un certo numero la risonanza scende e l'impedenza alle frequenze alte cala.</p></div></div>''')
pl=f'''<svg viewBox="0 0 560 330" width="100%">
{wire(60,40,250,40,N,5)}{wire(290,40,480,40,N,5)}{wire(270,45,270,270,"#8a6d1f",6)}
<rect x="250" y="55" width="40" height="40" rx="6" fill="{O}"/>{tx(300,82,"1: al punto di alimentazione",O,14,"start")}
{wire(270,160,200,160,N,3)}{gnd(200,160)}{tx(185,140,"3: calza a terra",N,14,"end")}{tx(185,158,"all'ingresso",N,14,"end")}
<rect x="250" y="190" width="40" height="40" rx="6" fill="{O}"/>{tx(300,217,"2: choke dopo la terra",O,14,"start")}
<rect x="220" y="270" width="100" height="36" rx="6" fill="{L}" stroke="{N}" stroke-width="2"/>{tx(270,294,"radio",N,14)}
{tx(280,326,"4: ferriti su alimentazione, USB, audio, rete, rotore",N,14)}</svg>'''
D.add("Dove metterli",f'''<div class="two"><div>{pl}</div><div><ul>
<li><b>Al punto di alimentazione</b> dell'antenna: impedisce alla corrente di nascere sulla calza.</li>
<li><b>All'ingresso in stazione</b>, dopo il collegamento della calza a terra: blocca quello che il cavo ha raccolto lungo la strada e il rumore della casa diretto verso l'antenna.</li>
<li>Sui cavi lunghi può servire un terzo choke a circa λ/4 dal primo.</li>
<li><b>Su ogni cavo</b> che entra in stazione o sale sul palo: alimentazione, USB, audio, rete, rotore, preamplificatore.</li></ul></div></div>''')
D.add("Misurare un choke con il VNA",f'''<div class="two"><div><ul>
<li>Metodo <b>in serie</b>: il choke (centrale e calza cortocircuitati tra loro all'ingresso e all'uscita) si inserisce tra porta 1 e porta 2 come un'impedenza in serie.</li></ul>
{eq("Z = 2 · 50 · (1/S21 − 1)")}
<ul><li>Con S21 lineare. Valido per Z molto più grande di 50 Ω.</li>
<li>Il VNA dà anche la fase: separa la parte resistiva da quella reattiva.</li></ul></div><div>
<h3>Esempi</h3><table><tr><th>S21 misurato</th><th>|Z| circa</th></tr><tr><td>−20 dB</td><td>900 Ω</td></tr><tr><td>−30 dB</td><td>3,1 kΩ</td></tr><tr><td>−34 dB</td><td>4,9 kΩ</td></tr><tr><td>−40 dB</td><td>9,9 kΩ</td></tr></table>
<ul class="small"><li>Collegamenti cortissimi: pochi centimetri di filo hanno già una reattanza paragonabile.</li>
<li>Un choke che misura bene sul banco può cambiare quando è montato vicino a una struttura metallica.</li></ul></div></div>''')
D.add("Le masse e gli anelli a 50 Hz",'''<div class="two"><div><ul>
<li>Due apparati collegati a prese diverse hanno conduttori di protezione (PE) a potenziali leggermente diversi, per le correnti di dispersione e le cadute sui cavi.</li>
<li>Se li collega anche uno schermo, nasce un <b>anello di massa</b>: nello schermo scorre una corrente a 50 Hz e alle sue armoniche, che si somma al segnale.</li>
<li>Sintomi: ronzio nell'audio, interfacce audio e PC che "ronzano", errori nelle reti di sensori e nei bus di campo.</li></ul></div><div>
<h3>Rimedi a bassa frequenza</h3><ul class="small">
<li>Collegamenti di massa corti e a bassa impedenza tra gli apparati: una barra di massa comune in stazione.</li>
<li>Cavi raccolti insieme, per ridurre l'area dell'anello.</li>
<li>Trasformatori di isolamento audio, optoisolatori, fibra ottica tra edifici.</li>
<li>Segnali <b>differenziali</b> (RS-485, audio bilanciato): il disturbo comune viene ignorato dal ricevitore.</li>
<li>Un choke di ferrite serve poco a 50 Hz: è un rimedio per la RF.</li></ul>
<div class="warn">Mai togliere la terra di protezione da un apparato per eliminare il ronzio: è una protezione contro la folgorazione.</div></div></div>''')
D.add("Il falso mito della calza collegata da un solo lato",f'''{myth}<div class="two" style="gap:30px"><div><ul class="small">
<li>"Collega la calza a terra da un lato solo, per non fare anelli" nasce dall'audio e dalla strumentazione a bassa frequenza, dove serve solo uno schermo elettrostatico.</li></ul></div><div><ul class="small">
<li>In RF lo schermo funziona solo se la corrente indotta può scorrere sulla calza e richiudersi: con un lato aperto non c'è schermatura magnetica, e la calza è un'antenna risonante.</li></ul></div></div>''')
D.add("Perché in RF il lato aperto non funziona",'''<div class="grid3"><div class="card"><h3>La calza diventa un'antenna</h3><p>Un cavo di 10 m con un lato aperto è un'antenna a λ/4 a 7,5 MHz. Raccoglie il campo e lo porta dentro l'apparato a cui è collegato.</p></div>
<div class="card"><h3>Nessuna schermatura magnetica</h3><p>Contro i campi magnetici lo schermo funziona perché la corrente indotta crea un campo opposto. Se non può scorrere, i conduttori interni vedono il campo intero.</p></div>
<div class="card"><h3>Il "codino" (pigtail)</h3><p>Anche collegare la calza con un filo di qualche centimetro rovina lo schermo: 5 cm sono circa 50 nH, cioè 31 Ω a 100 MHz. Serve un collegamento a 360°.</p></div>
<div class="card"><h3>Il coassiale non ha scelta</h3><p>Nel coassiale la calza è il conduttore di ritorno del segnale: va collegata a entrambi i capi. Il problema da risolvere è la corrente sulla faccia esterna, non la calza.</p></div>
<div class="card"><h3>Le reti di sensori</h3><p>Bus di campo e sensori vicino a trasmettitori, inverter o motori ricevono proprio i disturbi RF che un lato aperto non ferma.</p></div>
<div class="card"><h3>Le norme EMC</h3><p>IEC 61000-5-2 raccomanda, dove possibile, la calza a entrambi i capi con terminazione a 360°, con un conduttore parallelo di equipotenzialità e una rete di masse magliata.</p></div></div>''')
D.add("Le buone pratiche",'''<div class="two"><div><h3>Nella stazione radio</h3><ul>
<li>Coassiale con la calza collegata ai due capi, sempre.</li>
<li>Choke al punto di alimentazione e all'ingresso in stazione.</li>
<li>Una sola barra di massa a cui collegare tutti gli apparati con conduttori corti e larghi, e la calza all'ingresso dei cavi.</li>
<li>Ferriti sui cavi di servizio; alimentatori lineari o switching di buona qualità.</li></ul></div><div><h3>Nelle reti di sensori e dati</h3><ul>
<li>Schermo collegato ai due capi a 360°, con <b>conduttore di equipotenzialità</b> in parallelo che porta la corrente a 50 Hz al posto della calza.</li>
<li>Segnali differenziali e cavi a coppie intrecciate.</li>
<li>Tra edifici o con potenziali di terra molto diversi: <b>isolamento galvanico</b> (fibra ottica, optoisolatori).</li>
<li>Solo quando nessuna di queste è possibile: un lato a terra diretto e l'altro tramite un condensatore (soluzione ibrida).</li></ul></div></div>''')
r=[("Choke","alta impedenza solo per il modo comune: > 1 kΩ, meglio 5 kΩ"),("Ferrite","resistiva è meglio: mix 31 in HF basse, 43 in HF alte"),("Posizione","antenna, ingresso stazione, cavi di servizio"),("Misura","VNA in serie: Z = 100·(1/S21 − 1)"),("50 Hz","barra di massa, cavi raccolti, differenziale, isolamento"),("Mito","un lato solo: niente anello, ma in RF niente schermo"),("Pratica","calza ai due capi a 360° + equipotenzialità")]
D.add("Riepilogo",'<table class="sum">'+"".join(f'<tr><td class="l" style="width:160px"><b>{a}</b></td><td class="l">{b}</td></tr>' for a,b in r)+'</table>')
D.render(); pdf("Modo_comune_2_Rimedi_e_miti_IV3HGA.pdf")
