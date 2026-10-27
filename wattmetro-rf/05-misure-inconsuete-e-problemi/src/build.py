import math
from deck import *
D=Deck("Misure inconsuete<br>e problemi di misura","Perché il wattmetro a volte sbaglia (armoniche, modulazione, burst, disadattamento, direttività) e cosa si può misurare oltre ai watt: perdita dei cavi, calorimetria, efficienza, SWR vero all'antenna","Il wattmetro RF: misure inconsuete e problemi")
D.add("In questo modulo",'''<div class="two"><div><h3>Problemi di misura</h3><div class="grid3" style="grid-template-columns:1fr 1fr">
<div class="card"><h3>Armoniche</h3><p>chi le conta e chi no</p></div><div class="card"><h3>Modulazione</h3><p>media, picco, PEP</p></div>
<div class="card"><h3>Burst TDMA</h3><p>DMR, TETRA, duty cycle</p></div><div class="card"><h3>Disadattamento</h3><p>posizione, direttività, cavi</p></div></div></div><div>
<h3>Misure inconsuete</h3><div class="grid3" style="grid-template-columns:1fr 1fr">
<div class="card"><h3>Perdita di un cavo</h3><p>con uno o due wattmetri</p></div><div class="card"><h3>Calorimetria</h3><p>la potenza con un termometro</p></div>
<div class="card"><h3>Efficienza</h3><p>di finali e amplificatori</p></div><div class="card"><h3>SWR all'antenna</h3><p>dalla stazione, togliendo il cavo</p></div></div></div></div>''')
D.add("Problema 1: armoniche e spurie",'''<div class="two"><div><ul>
<li>Un wattmetro <b>termico</b> (termocoppia, termistore, calorimetro) somma la potenza di <b>tutte</b> le componenti: fondamentale, armoniche, spurie.</li>
<li>Un'armonica a −20 dBc vale l'1 % della potenza: sulla lettura pesa solo 0,04 dB. Il problema non è la lettura, è che quella potenza va in antenna.</li>
<li>Un wattmetro a <b>diodo</b> che lavora come rivelatore di picco può sbagliare di più: le armoniche cambiano la forma d'onda e quindi il picco, anche di qualche %.</li></ul></div><div>
<h3>Il test del passa-basso</h3><ul class="small"><li>Misura con e senza un filtro passa-basso di buona qualità tra TX e wattmetro (tenendo conto della sua perdita).</li>
<li>Se la lettura cambia molto più della perdita del filtro, il TX ha armoniche importanti o il wattmetro reagisce alla forma d'onda.</li>
<li>Una testina di banda più alta (per esempio una A su un TX in HF) può "vedere" le armoniche meglio della fondamentale: usa sempre la testina della banda giusta.</li>
<li>Per sapere quanto valgono davvero le armoniche serve l'analizzatore di spettro.</li></ul></div></div>''')
D.add("Problema 2: modulazione, media e PEP",'''<div class="two"><div><ul>
<li>CW e FM hanno inviluppo costante: media = PEP, e qualsiasi wattmetro legge correttamente.</li>
<li>In <b>SSB</b> la media dipende da come parli: con la voce è spesso 7–13 dB sotto la PEP. Un wattmetro a lettura media "dice" 15 W su un TX da 100 W PEP.</li>
<li>In <b>AM</b> la media sale con la modulazione: 100 W di portante al 100 % diventano 150 W medi, con una PEP di 400 W.</li></ul></div><div>
<h3>Come misurare la PEP</h3><ul class="small"><li><b>Wattmetro di picco</b>: un circuito che trattiene il massimo dell'inviluppo.</li>
<li><b>Test a due toni</b> con wattmetro a lettura media: PEP = 2 × media.</li>
<li><b>Oscilloscopio</b> su un prelievo calibrato: PEP = (V<sub>picco</sub>/√2)² / R al massimo dell'inviluppo.</li>
<li>I conti completi sono nel modulo sulla potenza del segnale e dello spettro.</li></ul></div></div>''')
rows=""
for nome,d in (("CW / FM continuo",1.0),("DMR (1 slot su 2)",0.5),("TETRA (1 slot su 4)",0.25),("Impulsi radar 1 µs ogni 1 ms",0.001)):
    rows+=f'<tr><td class="l">{nome}</td><td>{it(d*100,1)} %</td><td>{it(10*math.log10(d),1)} dB</td></tr>'
D.add("Problema 3: segnali a burst (TDMA)",f'''<div class="two"><div>
{eq("P<sub>media</sub> = P<sub>burst</sub> · duty cycle")}
<table><tr><th>Segnale</th><th>Duty cycle</th><th>Media rispetto al burst</th></tr>{rows}</table></div><div><ul class="small">
<li>Un wattmetro <b>termico</b> legge la media: per un terminale TETRA da 10 W di burst, circa 2,5 W.</li>
<li>Un wattmetro a <b>diodo lento</b> (come una testina passante con strumento a lancetta) legge qualcosa tra media e picco, in modo poco prevedibile.</li>
<li>Un wattmetro di <b>picco</b> o un power meter con sensore veloce legge la potenza del burst.</li>
<li>Prima di confrontare due misure, chiediti sempre: "media o burst?".</li></ul>
<p class="note">Per tarare la potenza di un apparato TDMA si usa di solito un analizzatore o un power meter con funzioni per segnali a burst; in alternativa si mette l'apparato in modalità di test a portante continua, se disponibile.</p></div></div>''')
D.add("Problema 4: disadattamento, direttività e cavi",'''<div class="two"><div><ul class="small">
<li>Con un wattmetro passante direzionale, su una linea senza perdite, <b>P<sub>f</sub> − P<sub>r</sub></b> non dipende da dove lo metti. Se cambia molto spostandolo, il wattmetro ha poca direttività o la linea ha perdite.</li>
<li>La <b>direttività finita</b> fa apparire una riflessa anche con un carico perfetto: SWR sotto circa 1,1–1,2 non sono affidabili con i wattmetri passanti comuni.</li>
<li>Anche il wattmetro ha il suo SWR d'inserzione: aggiunge una piccola riflessione.</li></ul></div><div><ul class="small">
<li><b>Cavi e adattatori</b> tra wattmetro e carico non sono "gratis": 1 dB di perdita è il <b>21 %</b> della potenza. A 430 MHz bastano pochi metri di cavo sottile.</li>
<li>Con sensori terminali, l'incertezza di disadattamento (1 ± |Γ<sub>s</sub>||Γ<sub>t</sub>|)² − 1 è spesso la voce più grande.</li>
<li>La <b>frequenza</b> fuori banda e la <b>temperatura</b> (diodi caldi, testine al sole) spostano le letture di qualche %.</li></ul>
<p class="note">Regola: scrivi sempre dove hai misurato, con quale testina o sensore e con quali cavi in mezzo.</p></div></div>''')
D.add("Misura inconsueta 1: la perdita di un cavo",'''<div class="two"><div><h3>Con due letture (cavo sotto carico)</h3><ul class="small">
<li>Wattmetro all'ingresso del cavo e all'uscita, chiuso sul carico fittizio. Con la stessa testina e lo stesso segnale:</li></ul>
<div class="eq">perdita (dB) = 10·log(P<sub>ingresso</sub> / P<sub>uscita</sub>)</div>
<p class="note">Con due wattmetri contemporaneamente, o spostandone uno; l'incertezza delle testine pesa molto se la perdita è piccola.</p></div><div>
<h3>Con un solo wattmetro (cavo aperto in fondo)</h3><ul class="small"><li>Lascia il cavo <b>aperto</b> (o in corto) all'altra estremità: tutta la potenza torna indietro, attenuata due volte.</li></ul>
<div class="eq">perdita (dB) = ½ · 10·log(P<sub>f</sub> / P<sub>r</sub>)</div>
<ul class="small"><li>Esempio: P<sub>f</sub> = 50 W, P<sub>r</sub> = 20 W → return loss 3,98 dB → perdita del cavo ≈ <b>2,0 dB</b>.</li>
<li>Usa bassa potenza e un TX che tolleri l'SWR infinito (o meglio un generatore e un power meter): la tensione su un cavo aperto è alta.</li></ul></div></div>''')
D.add("Misura inconsueta 2: la calorimetria",'''<div class="two"><div><ul>
<li>Il modo più "fisico" di misurare la potenza: la si trasforma in calore e si misura di quanto si scalda una massa nota.</li></ul>
<div class="eq">P = m · c · ΔT / t</div>
<ul class="small"><li>m massa del liquido (kg), c calore specifico (acqua 4186 J/kg·K, olio ≈ 1900), ΔT aumento di temperatura, t durata in secondi.</li></ul>
<p class="note">Esempio: 1 kg d'acqua che si scalda di 1,43 °C in 60 s → P = 4186 · 1,43 / 60 ≈ 100 W.</p></div><div>
<h3>Come farla bene</h3><ul class="small"><li>Carico fittizio immerso in un contenitore isolato, con il liquido <b>mescolato</b> e un termometro preciso (0,1 °C).</li>
<li>Misura anche la "deriva" a RF spenta: le perdite di calore verso l'ambiente vanno sottratte.</li>
<li>Trasmissioni brevi rispetto alla capacità termica, e ΔT piccoli (pochi gradi).</li>
<li>Precisione realistica: qualche %, ottima come controllo indipendente del wattmetro.</li></ul></div></div>''')
D.add("Misura inconsueta 3: efficienza di un finale",'''<div class="two"><div><ul>
<li>Misuri la potenza RF d'uscita con il wattmetro e la potenza DC d'ingresso con voltmetro e amperometro:</li></ul>
<div class="eq">η = P<sub>RF</sub> / (V<sub>DC</sub> · I<sub>DC</sub>)</div><div class="eq">G (dB) = 10·log(P<sub>out</sub> / P<sub>in</sub>)</div>
<p class="note">Esempio: 100 W RF con 13,8 V e 18 A → 248 W assorbiti → η ≈ 40 %. Il resto, circa 150 W, è calore da smaltire.</p></div><div>
<h3>Usi pratici</h3><ul class="small"><li>Confrontare finali diversi o lo stesso finale su bande diverse.</li>
<li>Scoprire un finale che si sta degradando: a parità di potenza assorbe più corrente.</li>
<li>Dimensionare alimentatore e dissipatore.</li>
<li>Con un carico disadattato l'efficienza cambia: è un buon modo di vedere quanto il finale "soffre" un SWR alto.</li>
<li>Misura la corrente vicino al finale, con cavi corti: la caduta sui cavi falsa V<sub>DC</sub>.</li></ul></div></div>''')
g=(1.5-1)/2.5; rl=-20*math.log10(g); ra=rl-4; ga=10**(-ra/20); sa=(1+ga)/(1-ga)
D.add("Misura inconsueta 4: l'SWR vero all'antenna",f'''<div class="two"><div><ul>
<li>Il cavo attenua anche l'onda riflessa, due volte: in stazione l'SWR sembra <b>migliore</b> di quello all'antenna.</li>
<li>Se conosci la perdita L del cavo (in dB), puoi risalire al valore all'antenna:</li></ul>
<div class="eq">RL<sub>antenna</sub> = RL<sub>stazione</sub> − 2·L</div><div class="eq">RL = 10·log(P<sub>f</sub> / P<sub>r</sub>)</div></div><div>
<h3>Esempio</h3><ul class="small"><li>In stazione: SWR 1,5, cioè RL = {it(rl,1)} dB.</li>
<li>Cavo con 2 dB di perdita (misurata come nella misura 1).</li>
<li>All'antenna: RL = {it(rl,1)} − 4 = {it(ra,1)} dB → <b>SWR ≈ {it(sa,2)}</b>.</li></ul>
<p class="note">Funziona bene finché RL in stazione è ben misurabile (con riflesse non troppo vicine al limite di direttività del wattmetro). Per cavi molto lunghi o con perdite alte, misura direttamente all'antenna.</p></div></div>''')
rows=[("Armoniche","i termici le sommano; i diodi di picco sbagliano di più"),("SSB e AM","media ≠ PEP: due toni → PEP = 2 × media"),("Burst TDMA","media = burst × duty cycle"),("Direttività","SWR sotto ~1,1–1,2 poco affidabili"),
("Perdita cavo","½·10·log(Pf/Pr) con il cavo aperto"),("Calorimetria","P = m·c·ΔT/t"),("SWR all'antenna","RL<sub>ant</sub> = RL<sub>stazione</sub> − 2L")]
D.add("Riepilogo",'<table class="sum">'+"".join(f'<tr><td class="l" style="width:250px"><b>{a}</b></td><td class="l">{b}</td></tr>' for a,b in rows)+'</table>')
D.render(); pdf("WM_Misure_Inconsuete_Problemi_IV3HGA.pdf")
