from deck import *
O="#e0563b"
MK=ARW+f'<defs><marker id="ao" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0L10 5L0 10z" fill="{O}"/></marker></defs>'
def ar(x1,y1,x2,y2,c=N,w=3):
    m={N:"ar",C:"ac",O:"ao"}[c]; return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{c}" stroke-width="{w}" marker-end="url(#{m})"/>'
def tx(x,y,t,c=N,fs=16,a="middle",b=""): return f'<text x="{x}" y="{y}" font-size="{fs}" fill="{c}" text-anchor="{a}" {"font-weight=\"bold\"" if b else ""}>{t}</text>'
def wire(x1,y1,x2,y2,c=N,w=3,d=""): return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{c}" stroke-width="{w}" {d}/>'
D=Deck("Le correnti di modo comune · queste sconosciute","Che cosa sono, perché scorrono sulla parte esterna della calza, da dove nascono, quali problemi causano in trasmissione e in ricezione, come si misurano","Modo comune · 1")
dm=f'''<svg viewBox="0 0 560 300" width="100%">{MK}
{tx(280,24,"Modo differenziale",C,18,b=1)}
<rect x="20" y="50" width="80" height="90" rx="8" fill="{L}" stroke="{N}" stroke-width="2"/>{tx(60,100,"TX")}
<rect x="460" y="50" width="80" height="90" rx="8" fill="{L}" stroke="{N}" stroke-width="2"/>{tx(500,100,"carico")}
{wire(100,70,460,70)}{wire(100,120,460,120)}{ar(220,70,330,70,C)}{ar(330,120,220,120,C)}
{tx(280,60,"I",C,16)}{tx(280,145,"−I",C,16)}{tx(280,170,"correnti uguali e opposte: i campi si annullano",N,14)}
{tx(280,205,"Modo comune",O,18,b=1)}
{wire(100,230,460,230)}{wire(100,260,460,260)}{ar(220,230,330,230,O)}{ar(220,260,330,260,O)}
{tx(280,290,"stessa direzione: torna attraverso la terra o le capacità parassite e irradia",N,14)}</svg>'''
D.add("Due modi di far scorrere una corrente",f'''<div class="two"><div>{dm}</div><div><ul>
<li>Su una coppia di conduttori qualsiasi corrente si può scomporre in due parti.</li>
<li><b>Differenziale</b>: va su un conduttore e torna sull'altro. È il segnale utile. I campi dei due conduttori, vicini e opposti, si cancellano: la linea non irradia.</li>
<li><b>Comune</b>: scorre nello stesso verso su entrambi i conduttori e si richiude da un'altra parte (terra, rete elettrica, il tuo corpo). La linea diventa un'<b>antenna</b>.</li>
<li>Bastano pochi milliampere di modo comune per irradiare quanto ampere di modo differenziale.</li></ul></div></div>''')
cx=f'''<svg viewBox="0 0 640 300" width="100%">{MK}
<rect x="40" y="70" width="500" height="160" rx="6" fill="#dfe6ee" stroke="{N}" stroke-width="2"/>
<rect x="40" y="95" width="500" height="110" fill="#fff" stroke="{N}" stroke-width="1"/>
<rect x="40" y="140" width="500" height="20" fill="#c9a24a" stroke="{N}" stroke-width="1"/>
{tx(560,154,"centrale",N,13,"start")}{tx(560,88,"calza",N,13,"start")}
{ar(150,150,330,150,C)}{tx(240,185,"I1 sul centrale",C,15)}
{ar(330,101,150,101,C)}{tx(240,122,"I2 = −I1 (interno calza)",C,15)}
{ar(150,62,330,62,O)}{tx(240,50,"I3: esterno della calza = modo comune",O,15)}
{tx(300,262,"Effetto pelle: in RF la calza ha due superfici indipendenti",N,14)}
{tx(300,284,"spessore di penetrazione nel rame a 14 MHz ≈ 18 µm",N,14)}</svg>'''
D.add("Il coassiale ha tre conduttori",f'''<div class="two"><div>{cx}</div><div><ul>
<li>In RF la corrente scorre solo sulla pelle dei conduttori. La calza ha <b>due facce</b>: quella interna e quella esterna, separate da uno spessore molto maggiore della profondità di penetrazione.</li>
<li>I1 e I2 sono uguali e opposte e restano chiuse dentro il cavo: è il segnale utile.</li>
<li>Sulla faccia esterna può scorrere una terza corrente <b>I3</b>, che non vede il dielettrico, non fa parte della linea e si comporta come un filo qualunque: irradia e riceve.</li>
<li>I3 è la corrente di modo comune del coassiale.</li></ul></div></div>''')
dp=f'''<svg viewBox="0 0 560 330" width="100%">{MK}
{wire(40,60,262,60,N,5)}{wire(298,60,520,60,N,5)}
<circle cx="262" cy="60" r="5" fill="{N}"/><circle cx="298" cy="60" r="5" fill="{N}"/>
{wire(268,70,268,300,"#555",10)}{wire(268,70,268,300,"#c9a24a",3)}
{wire(262,60,268,70,N,2)}{wire(298,60,274,70,N,2)}
{ar(240,46,120,46,C)}{tx(180,36,"I1",C,16)}
{ar(320,46,440,46,C)}{tx(380,36,"I2 − I3",C,16)}
{ar(285,110,285,240,O)}{tx(292,180,"I3 sulla calza",O,16,"start")}
{tx(140,110,"braccio collegato",N,13)}{tx(140,128,"al centrale",N,13)}{tx(430,110,"braccio collegato",N,13)}{tx(430,128,"alla calza",N,13)}
{tx(280,325,"verso la stazione",N,13)}</svg>'''
D.add("Da dove nasce: il dipolo alimentato in coassiale",f'''<div class="two"><div>{dp}</div><div><ul>
<li>Il dipolo è un'antenna <b>bilanciata</b>, il coassiale una linea <b>sbilanciata</b>.</li>
<li>Al punto di alimentazione la corrente I2 della faccia interna della calza trova due strade: il braccio destro del dipolo e la faccia esterna della calza.</li>
<li>Quanta ne va sulla calza dipende dall'impedenza di quel percorso: lunghezza del cavo, percorso verso terra, posizione.</li>
<li>I due bracci non hanno più correnti uguali: il diagramma si deforma e il cavo diventa il terzo braccio dell'antenna.</li></ul></div></div>''')
D.add("La lunghezza del cavo conta",f'''<div class="two"><div class="fig">{svg("length.svg")}</div><div><ul class="small">
<li>La faccia esterna della calza, tra antenna e terra (la stazione), è una linea con la sua impedenza: bassa quando è lunga circa λ/2, λ… e alta vicino a λ/4, 3λ/4.</li>
<li>Con un cavo "sfortunato" la corrente di modo comune è alta; cambiando la lunghezza di qualche metro si riduce di molti dB. Il grafico usa un modello semplificato, solo indicativo.</li>
<li>Per questo il ROS che cambia con la lunghezza del cavo, o toccando la radio, è un segnale di modo comune: in una linea adattata e senza correnti sulla calza il ROS non dipende dalla lunghezza.</li>
<li>Una lunghezza di cavo va bene su una banda e male su un'altra: il rimedio vero è il choke (lezione 2).</li></ul></div></div>''')
D.add("Altre sorgenti di modo comune",'''<div class="grid3"><div class="card"><h3>Antenne asimmetriche</h3><p>Dipoli fuori centro (OCF, Windom), end-fed, bracci di lunghezza diversa, dipoli vicini a un tetto da un lato solo.</p></div>
<div class="card"><h3>Verticali senza radiali</h3><p>Senza un contrappeso adeguato la corrente di ritorno cerca la calza: il cavo diventa un radiale, e la stazione fa parte dell'antenna.</p></div>
<div class="card"><h3>Accoppiamento col campo</h3><p>Un cavo che corre parallelo all'antenna o sotto di essa raccoglie corrente per induzione, anche con un balun perfetto al centro.</p></div>
<div class="card"><h3>Discesa non perpendicolare</h3><p>Se il coassiale non scende a 90° dal dipolo, un braccio si accoppia al cavo più dell'altro.</p></div>
<div class="card"><h3>Cavi di servizio</h3><p>Rotore, alimentazione del preamplificatore, cavi di rete o di controllo che salgono sul palo: ognuno porta il suo modo comune in stazione.</p></div>
<div class="card"><h3>Apparati in stazione</h3><p>Alimentatori switching, PC, monitor e caricabatterie generano correnti di modo comune sui loro cavi, che finiscono anche sulla calza dell'antenna.</p></div></div>''')
D.add("I sintomi: metà dei nostri problemi",'''<div class="two"><div><h3>In trasmissione</h3><ul>
<li>"RF in stazione": scosse leggere toccando la radio o il microfono, audio distorto o ronzante, il PC che si blocca, l'interfaccia USB che si scollega.</li>
<li>Il ROS cambia con la lunghezza del cavo, la posizione, toccando la radio o spostando un cavo.</li>
<li>Interferenze alla TV, all'impianto audio, ai citofoni, all'allarme dei vicini.</li>
<li>Diagramma d'irradiazione deformato: l'antenna non va dove dovrebbe.</li></ul></div><div><h3>In ricezione</h3><ul>
<li>La calza esterna del cavo porta fino all'antenna il rumore di tutti gli apparati della casa e della stazione.</li>
<li>Il cavo lo irradia vicino all'antenna, che lo riceve: il fondo di rumore sale di 10–20 dB senza che nessuno se ne accorga.</li>
<li>Prova: spegni l'alimentatore switching, il PC, il router. Se il rumore cala molto, probabilmente entra per modo comune.</li>
<li>Un buon choke in stazione e all'antenna spesso abbassa il fondo di qualche unità S.</li></ul></div></div>''')
pr=f'''<svg viewBox="0 0 560 260" width="100%">{MK}
{wire(20,130,540,130,"#555",12)}{wire(20,130,540,130,"#c9a24a",3)}
<ellipse cx="200" cy="130" rx="26" ry="70" fill="none" stroke="{N}" stroke-width="12"/>
{ar(330,110,430,110,O)}{tx(380,98,"I3",O,16)}
{wire(226,100,320,40,N,2)}<rect x="320" y="20" width="200" height="50" rx="8" fill="{L}" stroke="{N}" stroke-width="2"/>{tx(420,40,"50 Ω + diodo + strumento",N,13)}{tx(420,58,"oppure analizzatore",N,13)}
{tx(200,225,"toroide (es. FT-140-43, 10–20 spire)",N,14)}{tx(200,245,"il cavo passa una volta dentro",N,14)}</svg>'''
D.add("Come si misura",f'''<div class="two"><div>{pr}</div><div><ul>
<li>Una <b>sonda di corrente</b>: un toroide di ferrite con un avvolgimento chiuso su 50 Ω, che si infila attorno al cavo. Il cavo è il primario a una spira.</li>
<li>Misura solo la corrente <b>netta</b>: I1 e I2 si annullano, resta I3. Il centrale e la calza interna non disturbano la lettura.</li>
<li>Si fa scorrere lungo il cavo: la corrente varia, con massimi ogni mezza lunghezza d'onda.</li>
<li>Uno sguardo ai valori: con 100 W in un dipolo la corrente utile vale circa 1,2 A. Se ne misuri decine di milliampere sulla calza, c'è da intervenire.</li>
<li>Senza strumenti: aggiungi un choke e guarda se cambiano ROS, rumore e RF in stazione.</li></ul></div></div>''')
r=[("Due modi","differenziale (utile) e comune (irradia)"),("Coassiale","tre correnti: centrale, interno calza, esterno calza"),("Origine","carichi bilanciati in coassiale, asimmetrie, accoppiamento"),("Lunghezza","il modo comune dipende dalla lunghezza del cavo"),("Sintomi","RF in stazione, ROS instabile, TVI, rumore in RX"),("Misura","sonda di corrente su toroide, prova del choke")]
D.add("Riepilogo",'<table class="sum">'+"".join(f'<tr><td class="l" style="width:160px"><b>{a}</b></td><td class="l">{b}</td></tr>' for a,b in r)+'</table>')
D.render(); pdf("Modo_comune_1_Cosa_sono_IV3HGA.pdf")
