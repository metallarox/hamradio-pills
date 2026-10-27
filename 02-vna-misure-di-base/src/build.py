import re,json,base64
v=json.load(open("vals.json"))
def svg(p):
    s=open(p).read(); s=re.sub(r'<\?xml.*?\?>','',s,flags=re.S); s=re.sub(r'<!DOCTYPE.*?>','',s,flags=re.S)
    return re.sub(r'(<svg[^>]*?)\swidth="[^"]*"\s+height="[^"]*"',r'\1 width="100%"',s,count=1)
logo='<img src="data:image/png;base64,'+base64.b64encode(open("logo.png","rb").read()).decode()+'">'
css=open("style.css").read()+"td.l{font-family:inherit!important;text-align:left!important}.flow{display:grid;grid-template-columns:repeat(5,1fr);gap:14px}.flow .card{position:relative}.flow .card b{display:block;font-size:34px;color:#22b8f0;line-height:1}.flow .card h3{margin-top:8px}table.sum td{font-size:22px!important;padding:13px 14px!important}"
def eq(x): return f'<div class="eq">{x}</div>'
def it(x,d=2): return f"{x:.{d}f}".replace(".",",")
S=[]
def add(t,b): S.append((t,b))
add("",f'''<div class="cover"><div class="clogo">{logo}</div><div>
<h1>Misure di base<br>con il VNA</h1>
<p class="sub">Come impostarlo, calibrarlo, verificare la calibrazione e fare le misure fondamentali nel modo corretto: antenne, filtri, cavi, amplificatori e componenti</p>
<p class="by">Elia · IV3HGA</p></div></div>''')
steps=[("Prepara","cavi, connettori, adattatori, statica"),("Imposta","span, punti, IF BW, potenza"),("Calibra","SOL o SOLT al piano giusto"),("Verifica","misura gli standard e un DUT noto"),("Misura","e leggi nel formato giusto")]
add("Il flusso di lavoro",'<div class="flow">'+"".join(f'<div class="card"><b>{i+1}</b><h3>{a}</h3><p>{b}</p></div>' for i,(a,b) in enumerate(steps))+'''</div>
<div class="two" style="margin-top:34px;align-items:start"><div><ul><li>L'ordine conta: ogni passo dà per scontato il precedente. Una calibrazione fatta prima di cambiare le impostazioni, o con un cavo che poi si muove, non vale più.</li></ul></div><div><ul>
<li>Le misure di questo modulo valgono per qualsiasi VNA, da un NanoVNA a uno strumento da laboratorio: cambiano solo i menu.</li></ul></div></div>''')
add("1 · Preparazione",f'''<div class="two"><div><h3>Cavi e connettori</h3><ul class="small">
<li>Usa cavi corti e di buona qualità, possibilmente <b>stabili in fase</b> (semirigidi o flessibili per misura): ogni movimento dopo la calibrazione è un errore.</li>
<li>Connettori <b>puliti</b> e serrati alla coppia giusta: per gli SMA circa 0,9 N·m (8 in-lb) se in acciaio, meno per l'ottone. Non stringere mai "a sensazione" con la pinza.</li>
<li>Gli adattatori vanno messi <b>prima</b> della calibrazione, così finiscono dentro la correzione.</li>
<li>Il kit di calibrazione deve avere lo stesso connettore del DUT, oppure va calibrato dopo l'adattatore.</li></ul></div><div>
<h3>Proteggere lo strumento</h3><ul class="small"><li><b>Mai</b> collegare un trasmettitore: anche pochi watt distruggono il ricevitore.</li>
<li>Prima di collegare un'antenna, <b>scarica il cavo</b> cortocircuitando centrale e calza: le cariche statiche accumulate dal vento sono un killer classico di VNA.</li>
<li>Rispetta la potenza massima in ingresso, soprattutto sulla porta 2 (spesso pochi dBm: controlla il manuale). Con amplificatori metti un attenuatore.</li>
<li>Se il DUT ha tensione continua (bias-tee, preamplificatori alimentati via cavo) usa un <b>DC block</b>.</li>
<li>Accendi il VNA qualche minuto prima, per stabilizzarne la temperatura.</li></ul></div></div>''')
add("2 · Impostare lo sweep",f'''<div class="two"><div><table>
<tr><th>Parametro</th><th>Consiglio</th></tr>
<tr><td class="l"><b>Start / stop</b></td><td class="l">copri la banda d'interesse con un po' di margine</td></tr>
<tr><td class="l"><b>Punti</b></td><td class="l">abbastanza da non perdere risonanze strette</td></tr>
<tr><td class="l"><b>IF bandwidth</b></td><td class="l">stretta per misure di attenuazione alta, larga per tarare dal vivo</td></tr>
<tr><td class="l"><b>Potenza</b></td><td class="l">bassa per amplificatori e quarzi, alta per la massima dinamica</td></tr>
<tr><td class="l"><b>Media</b></td><td class="l">riduce il rumore della traccia, a scapito della velocità</td></tr></table></div><div>
{eq("Δf = span / (N − 1)")}
<ul class="small"><li>Esempio: 1 MHz di span con 101 punti dà un passo di 10 kHz. Un risonatore con banda di 2 kHz può sparire tra due punti.</li>
<li>Imposta tutto <b>prima</b> di calibrare. Se poi cambi span o punti, molti VNA <b>interpolano</b> la calibrazione: funziona, ma è meno precisa. Quando possibile, ricalibra.</li>
<li>Per misure molto lunghe o larghe, usa i segmenti o il software sul PC con migliaia di punti.</li></ul></div></div>''')
add("3 · Calibrare",f'''<div class="two"><div><h3>Dove</h3><ul class="small">
<li>Il <b>piano di riferimento</b> è dove colleghi gli standard: tutto ciò che sta prima (VNA, cavi, adattatori) viene tolto dalla misura.</li>
<li>Calibra esattamente dove collegherai il DUT, cioè in fondo ai cavi di misura.</li>
<li>Se non puoi arrivare al punto giusto (antenna sul traliccio), calibra in fondo al cavo di misura e usa <b>port extension</b> o <b>de-embedding</b>.</li></ul>
<h3>Quale calibrazione</h3><table><tr><th>Misura</th><th>Standard</th></tr>
<tr><td class="l">solo S11 (antenne, impedenze)</td><td class="l">Open, Short, Load sulla porta 1</td></tr>
<tr><td class="l">S11 e S21 (filtri, cavi, amplificatori)</td><td class="l">OSL + Isolation + Through</td></tr></table></div><div>
<h3>Sequenza tipica</h3><ol class="small"><li><b>Open</b> sulla porta 1</li><li><b>Short</b> sulla porta 1</li><li><b>Load</b> 50 Ω sulla porta 1</li>
<li><b>Isolation</b>: carichi su entrambe le porte (misura il crosstalk interno)</li><li><b>Through</b>: porta 1 collegata alla porta 2</li><li><b>Salva</b> la calibrazione in uno slot con un nome che ricordi le impostazioni</li></ol>
<p class="note">Seleziona nello strumento il kit che usi davvero (o inserisci i suoi coefficienti): un open "ideale" a 1 GHz non è ideale.</p></div></div>''')
add("4 · Verificare la calibrazione",f'''<div class="two"><div><table>
<tr><th>Collega</th><th>Devi vedere</th></tr>
<tr><td class="l"><b>Load</b></td><td class="l">|S11| molto basso (−35…−40 dB o meglio), punto al centro della carta di Smith</td></tr>
<tr><td class="l"><b>Open</b></td><td class="l">|S11| ≈ 0 dB, fase ≈ 0°, punto sul bordo destro</td></tr>
<tr><td class="l"><b>Short</b></td><td class="l">|S11| ≈ 0 dB, fase ≈ 180°, punto sul bordo sinistro</td></tr>
<tr><td class="l"><b>Through</b></td><td class="l">|S21| ≈ 0 dB (±0,1 dB), fase ≈ 0°</td></tr>
<tr><td class="l"><b>Attenuatore noto</b></td><td class="l">il suo valore (per esempio 20 dB), piatto in frequenza</td></tr></table></div><div><ul>
<li>Gli stessi standard usati per calibrare danno sempre un risultato "perfetto": è più onesta una verifica con un <b>secondo carico</b> o un attenuatore che non hai usato nella calibrazione.</li>
<li>Muovi un po' i cavi e guarda quanto cambia la traccia: è l'incertezza reale del tuo setup.</li>
<li>Ripeti la verifica a fine sessione: se è cambiato qualcosa, sai quali misure rifare.</li></ul></div></div>''')
add("5 · Misurare un'antenna (S11)",f'''<div class="two"><div><h3>Come</h3><ul class="small">
<li>Calibrazione OSL <b>in fondo al cavo</b> che collegherai all'antenna. Ideale: misurare direttamente al punto di alimentazione.</li>
<li>Se misuri dalla stazione, il cavo trasforma l'impedenza e le sue perdite fanno sembrare migliore l'SWR.</li>
<li>Formati utili: <b>SWR</b> per la banda, <b>R + jX</b> per sapere cosa correggere, <b>carta di Smith</b> per vedere tutto insieme.</li>
<li>Usa un marker sul minimo e due marker ai bordi della banda: leggi frequenza di risonanza e banda 2:1.</li></ul></div><div>
<h3>Trappole</h3><ul class="small"><li><b>Tocca il cavo</b>: se la traccia cambia, c'è corrente di modo comune sulla calza. Serve un choke.</li>
<li>Stai lontano dall'antenna: il tuo corpo e gli oggetti vicini la spostano, soprattutto in VHF/UHF.</li>
<li>Stazioni broadcast o ripetitori vicini possono entrare nel ricevitore: se la traccia è rumorosa, stringi l'IF BW.</li>
<li>Ricorda di <b>scaricare il cavo</b> prima di collegarlo.</li>
<li>Per leggere i risultati sulla carta di Smith, vedi il modulo dedicato.</li></ul></div></div>''')
lo,hi=v["bw3"]
add("6 · Misurare un filtro (S21)",f'''<div class="two"><div class="fig">{svg("filter.svg")}<p class="cap">Passa-banda simulato a 145 MHz (Chebyshev del 3° ordine).</p></div><div><ul class="small">
<li>Calibrazione completa (OSL + Isolation + Through), poi il filtro tra le due porte.</li>
<li><b>Insertion loss</b> = −|S21| al centro banda: qui {it(v["il"],1)} dB.</li>
<li><b>Banda a −3 dB</b>: due marker a 3 dB sotto il massimo, qui da {it(lo/1e6,1)} a {it(hi/1e6,1)} MHz.</li>
<li><b>Reiezione</b> alle frequenze da attenuare, qui {-v["rej"]:.0f} dB a 130 MHz.</li>
<li>Guarda anche <b>S11</b> in banda: un filtro tarato male ha IL accettabile ma adattamento pessimo.</li>
<li>Se la reiezione tocca il rumore di fondo, il filtro è "almeno" quel valore: stringi l'IF BW o alza la potenza per avere più dinamica.</li></ul></div></div>''')
fq=v["fq"]
add("7 · Misurare un cavo coassiale",f'''<div class="two"><div class="fig">{svg("cable.svg")}<p class="cap">10 m di cavo con VF 0,66, aperto in fondo (simulazione).</p></div><div>
<ul class="small"><li><b>Perdita</b> (due porte): IL = −|S21|. <b>Con una porta sola</b>: lascia il cavo aperto (o in corto) in fondo, e il segnale fa andata e ritorno:</li></ul>
{eq("perdita (dB) ≈ |S11|<sub>dB</sub> / 2")}
<ul class="small"><li><b>Fattore di velocità</b>: un cavo aperto lungo λ/4 si comporta da corto. Dalla prima frequenza f<sub>λ/4</sub> in cui |Z| è minimo:</li></ul>
{eq("VF = 4·L·f<sub>λ/4</sub> / c")}
<ul class="small"><li><b>Impedenza caratteristica</b>, a una frequenza lontana dai multipli di λ/4:</li></ul>
{eq("Z0 = √(Z<sub>aperto</sub> · Z<sub>corto</sub>)")}
<p class="note">Esempi: |S11| = −3,2 dB con il cavo aperto → 1,6 dB di perdita. Primo minimo a {it(fq/1e6)} MHz con 10 m → VF = {it(4*10*fq/299792458)}. Z<sub>aperto</sub> = −j40 Ω e Z<sub>corto</sub> = +j62,5 Ω → Z0 = 50 Ω.</p></div></div>''')
add("8 · Amplificatori e preamplificatori",f'''<div class="two"><div><ul>
<li><b>Abbassa la potenza</b> del VNA prima di collegare: in ingresso all'amplificatore deve stare ben sotto il punto di compressione.</li>
<li>All'uscita metti un <b>attenuatore</b> se il segnale amplificato supera il limite della porta 2. Calibra con l'attenuatore già inserito, così il guadagno si legge direttamente.</li>
<li>Alimenta l'amplificatore <b>prima</b> di collegarlo, e usa un DC block se l'uscita porta tensione.</li></ul></div><div>
<h3>Cosa misurare</h3><ul class="small"><li><b>Guadagno</b> = |S21| in dB, e la sua piattezza in banda.</li>
<li><b>Adattamento d'ingresso e d'uscita</b> = S11 e S22 (con un VNA T/R giri l'amplificatore).</li>
<li><b>Isolamento inverso</b> = S12: importante per la stabilità.</li>
<li><b>Compressione a 1 dB</b>: aumenta la potenza a frequenza fissa finché il guadagno cala di 1 dB (se il VNA permette lo sweep di potenza).</li>
<li>Picchi strani fuori banda o una traccia instabile possono indicare un'<b>autooscillazione</b>: controlla con un analizzatore di spettro.</li></ul></div></div>''')
add("9 · Componenti: L, C e R a una frequenza",f'''<div class="two"><div><ul>
<li>Componente sul piano di calibrazione (meglio su un piccolo fixture con collegamenti cortissimi), misura <b>S11</b> e leggi Z = R + jX.</li></ul>
{eq("L = X / (2π·f) &nbsp;&nbsp;(X > 0)")}{eq("C = −1 / (2π·f·X) &nbsp;&nbsp;(X &lt; 0)")}{eq("Q = |X| / R")}
<p class="note">Quasi tutti i VNA mostrano direttamente L o C equivalenti sul marker.</p></div><div>
<h3>Limiti</h3><ul class="small"><li>S11 è preciso quando |Z| è nell'ordine di 5–500 Ω. Molto lontano da 50 Ω il punto finisce sul bordo della carta e la precisione crolla.</li>
<li>Per impedenze molto basse (mΩ) usa lo <b>shunt-through</b>, per quelle alte la misura <b>in serie</b> in S21: entrambe nel modulo "Misure inconsuete".</li>
<li>Un componente ha senso solo sotto la sua <b>SRF</b>: fai sempre uno sweep largo prima di fidarti del valore a una frequenza.</li></ul></div></div>''')
add("Errori comuni",f'''<div class="two"><div><ul class="small">
<li>Calibrare in un punto e misurare in un altro (per esempio aggiungere un adattatore dopo).</li>
<li>Cambiare span o punti dopo la calibrazione senza accorgersene.</li>
<li>Piegare o spostare i cavi tra calibrazione e misura.</li>
<li>Connettori sporchi, allentati o danneggiati, che danno valori che "ballano".</li>
<li>Kit di calibrazione sbagliato selezionato nello strumento.</li></ul></div><div><ul class="small">
<li>Troppi pochi punti: la risonanza vera cade tra due campioni.</li>
<li>Potenza troppo alta su amplificatori, quarzi o componenti non lineari.</li>
<li>Antenna misurata dalla stazione con un cavo lungo e con perdite.</li>
<li>Confondere i segni: |S11| = −20 dB corrisponde a un return loss di +20 dB.</li>
<li>Dimenticare di scaricare l'antenna, o collegare per errore un TX.</li></ul></div></div>''')
rows=["Connettori puliti, coppia corretta, cavi fermi","VNA acceso da qualche minuto","Span, punti, IF BW e potenza impostati","Calibrazione al piano del DUT, kit corretto","Verifica con load, open/short, thru e un DUT noto","Cavo d'antenna scaricato, potenze in ingresso rispettate","Misura nel formato giusto e marker sui punti chiave","Verifica finale e salvataggio di dati e calibrazione"]
add("Checklist prima di ogni misura",'<table class="sum">'+"".join(f'<tr><td class="l" style="width:46px;color:#22b8f0;font-weight:800">☐</td><td class="l">{r}</td></tr>' for r in rows)+'</table>')
out=[f"<!DOCTYPE html><html><head><meta charset='utf-8'><style>{css}</style></head><body>"]
for i,(t,b) in enumerate(S):
    if not t: out.append(f'<section class="slide c">{b}</section>');continue
    out.append(f'<section class="slide"><div class="hdrlogo">{logo}</div><h2>{t}</h2>{b}<div class="foot"><span>Misure di base con il VNA · IV3HGA</span><span>{i+1}/{len(S)}</span></div></section>')
out.append("</body></html>"); open("slides.html","w").write("".join(out))
