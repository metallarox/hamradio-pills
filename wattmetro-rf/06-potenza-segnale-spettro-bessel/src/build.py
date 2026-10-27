import json, math
from deck import *
v=json.load(open("vals.json"))
def dbm(w): return 10*math.log10(w*1000)
D=Deck("Potenza del segnale<br>e potenza dello spettro","AM, SSB, FM e funzioni di Bessel, densità spettrale e RBW, somme in dB e fattore di cresta: la matematica che lega il wattmetro all'analizzatore di spettro, con esempi numerici","Potenza del segnale e dello spettro")
D.add("Due modi di guardare la stessa potenza",'''<div class="two"><div><h3>Il wattmetro</h3><ul>
<li>Guarda il segnale <b>nel tempo</b> e ne misura la potenza totale: media (o picco).</li>
<li>Non sa come la potenza è distribuita in frequenza: portante, bande laterali, armoniche, tutto insieme.</li></ul>
<h3>L'analizzatore di spettro</h3><ul><li>Scompone il segnale <b>in frequenza</b> e mostra la potenza di ogni componente (riga) o la densità per unità di banda.</li></ul></div><div>
<h3>Il ponte tra i due: Parseval</h3>
<div class="eq">P<sub>totale</sub> = Σ P<sub>righe</sub> = ∫ PSD(f) df</div>
<ul class="small"><li>La potenza totale è la <b>somma delle potenze</b> delle righe (in watt, non in dB!), o l'integrale della densità spettrale per i segnali a spettro continuo.</li>
<li>Quindi, sommando le righe viste sull'analizzatore, devi ritrovare quello che legge il wattmetro, a meno degli errori degli strumenti.</li>
<li>In questo modulo lo verifichiamo per AM, SSB e FM.</li></ul></div></div>''')
D.add("Potenza istantanea, media e di inviluppo",'''<div class="two"><div>
<div class="eq">v(t) = V<sub>p</sub> · cos(ωt)</div><div class="eq">P = V<sub>p</sub>² / (2R) = V<sub>eff</sub>² / R</div>
<ul class="small"><li>La potenza istantanea v²/R oscilla al doppio della frequenza; la sua media su un ciclo è V<sub>p</sub>²/(2R).</li>
<li>Se l'ampiezza cambia lentamente (modulazione), si scrive v(t) = a(t)·cos(ωt): a(t) è l'<b>inviluppo</b>.</li></ul>
<div class="eq">P<sub>inv</sub>(t) = a(t)² / (2R)</div></div><div>
<ul><li><b>PEP</b> = valore massimo di P<sub>inv</sub>(t): la potenza media di un ciclo RF quando l'inviluppo è al massimo.</li>
<li><b>Potenza media</b> = media di P<sub>inv</sub>(t) su un tempo lungo: quella che scalda il carico.</li>
<li><b>Fattore di cresta</b> (o PAPR) = PEP / media, spesso in dB.</li></ul>
<p class="note">Esempio: su 50 Ω, un'onda con V<sub>p</sub> = 100 V dà P = 100² / 100 = 100 W, e V<sub>eff</sub> = 70,7 V.</p></div></div>''')
D.add("AM: la portante e le bande laterali",f'''<div class="two"><div>
<div class="eq">v(t) = V<sub>c</sub>·[1 + m·cos(ω<sub>m</sub>t)]·cos(ω<sub>c</sub>t)</div>
<p class="note">Con la formula di prodotto dei coseni diventa:</p>
<div class="eq">= V<sub>c</sub>cos(ω<sub>c</sub>t) + (mV<sub>c</sub>/2)·cos((ω<sub>c</sub> ± ω<sub>m</sub>)t)</div>
<ul class="small"><li>Tre righe: la portante di ampiezza V<sub>c</sub> e due bande laterali di ampiezza mV<sub>c</sub>/2.</li></ul>
{eq("P<sub>BL</sub> = P<sub>c</sub>·m²/4 &nbsp;(ciascuna)")}{eq("P<sub>tot</sub> = P<sub>c</sub>·(1 + m²/2) &nbsp;&nbsp; PEP = P<sub>c</sub>·(1 + m)²")}</div><div class="fig">{svg("am.svg")}
<p class="cap">Portante da 100 W: con m = 100 % le bande laterali valgono 25 W ciascuna, totale 150 W, PEP 400 W.</p></div></div>''')
D.add("AM: cosa leggono gli strumenti",f'''<div class="two"><div><h3>Portante 100 W, m = 100 %</h3><table>
<tr><th>Grandezza</th><th>Valore</th></tr><tr><td class="l">Portante</td><td>100 W ({it(dbm(100),1)} dBm)</td></tr>
<tr><td class="l">Ogni banda laterale</td><td>25 W ({it(dbm(25),1)} dBm)</td></tr><tr><td class="l">Totale (media)</td><td>150 W</td></tr>
<tr><td class="l">PEP</td><td>400 W</td></tr><tr><td class="l">PEP / media</td><td>2,67 ({it(10*math.log10(400/150),2)} dB)</td></tr></table></div><div><ul>
<li><b>Wattmetro termico</b>: 150 W. Senza modulazione legge 100 W: la lancetta "sale" del 50 % quando moduli.</li>
<li><b>Analizzatore</b>: tre righe, la portante a +50 dBm e le bande laterali 6 dB sotto. Sommandole in watt: 100 + 25 + 25 = 150 W.</li>
<li>La potenza "utile" che porta l'informazione è solo quella delle bande laterali: un terzo del totale nel caso migliore.</li></ul>
<p class="note">Da qui l'idea della SSB: togliere la portante e una banda laterale, che non portano informazione in più.</p></div></div>''')
D.add("SSB e il test a due toni",f'''<div class="two"><div><ul>
<li>Con un solo tono, la SSB è una sola riga: media = PEP.</li>
<li>Con due toni di uguale ampiezza A le due righe "battono": l'inviluppo va da 0 a 2A.</li></ul>
{eq("P<sub>media</sub> = 2·P<sub>tono</sub>")}{eq("PEP = (2A)²/(2R) = 4·P<sub>tono</sub>")}
{eq("PEP = 2·P<sub>media</sub> &nbsp;(+3 dB)")}</div><div>
<h3>Esempio: 100 W PEP</h3><ul class="small"><li>Ogni tono: 25 W → sull'analizzatore due righe a {it(dbm(25),1)} dBm, cioè <b>6 dB sotto la PEP</b>.</li>
<li>Wattmetro a lettura media: <b>50 W</b>.</li>
<li>Wattmetro di picco: 100 W.</li>
<li>Somma delle righe sull'analizzatore: 25 + 25 = 50 W = lettura media. Parseval funziona.</li></ul>
<p class="note">Per questo l'IMD di un TX si esprime rispetto alla PEP aggiungendo 6 dB alla distanza tono–prodotto (modulo sui prelievi e accoppiatori).</p></div></div>''')
D.add("FM: lo spettro e le funzioni di Bessel",'''<div class="two"><div>
<div class="eq">v(t) = V·cos(ω<sub>c</sub>t + β·sin ω<sub>m</sub>t)</div><div class="eq">β = Δf / f<sub>m</sub></div>
<p class="note">Lo sviluppo di Jacobi–Anger trasforma la fase sinusoidale in una somma di righe:</p>
<div class="eq">v(t) = V · Σ<sub>n</sub> J<sub>n</sub>(β) · cos((ω<sub>c</sub> + n·ω<sub>m</sub>)t)</div>
<ul class="small"><li>Le righe sono a f<sub>c</sub> ± n·f<sub>m</sub>: infinite in teoria, ma quelle lontane sono trascurabili.</li>
<li>L'ampiezza di ogni riga è V·J<sub>n</sub>(β), la sua potenza P·J<sub>n</sub>²(β).</li>
<li>J<sub>−n</sub> = (−1)<sup>n</sup>·J<sub>n</sub>: le righe simmetriche hanno la stessa ampiezza (con segno alternato per n dispari).</li></ul></div><div>
<h3>Cosa sono le J<sub>n</sub>(β)</h3><ul class="small"><li>Sono le funzioni di Bessel di prima specie: oscillano e si smorzano al crescere di β, come onde che si allargano.</li>
<li>Per β piccolo (FM a banda stretta) J<sub>0</sub> ≈ 1 e J<sub>1</sub> ≈ β/2: una portante e due bande laterali, come l'AM ma con fase diversa.</li>
<li>Quando una J<sub>n</sub>(β) passa per zero, quella riga sparisce: il caso più famoso è J<sub>0</sub>(2,405) = 0, la portante si annulla (metodo del nullo di Bessel per tarare la deviazione).</li></ul></div></div>''')
D.add("FM: la potenza totale non cambia",f'''<div class="fig" style="width:96%">{svg("bessel_bars.svg")}</div><div class="two" style="align-items:start;gap:30px"><div>
{eq("Σ<sub>n=−∞</sub><sup>+∞</sup> J<sub>n</sub>²(β) = 1 &nbsp;→&nbsp; P<sub>tot</sub> = P per ogni β")}</div><div>
<p class="note" style="margin-top:2px">L'FM ha inviluppo costante: la modulazione non aggiunge potenza, la <b>ridistribuisce</b> dalla portante alle bande laterali. Con β = 2,405 la portante è vuota e tutta la potenza è nelle bande laterali. Il wattmetro legge sempre lo stesso valore, modulato o no.</p></div></div>''')
r=v["t2405"]
rows="".join(f'<tr><td class="l">{"portante" if k==0 else "± "+str(k)+"·fm"}</td><td>{it(abs(j) if abs(j)<1e-3 else j,3)}</td><td>{it(p,2)} W{" × 2" if k else ""}</td></tr>' for k,j,p in r)
tot=r[0][2]+2*sum(p for k,j,p in r[1:])
D.add("Esempio: FM da 50 W con β = 2,405",f'''<div class="two"><div><table><tr><th>Riga</th><th>J<sub>n</sub>(2,405)</th><th>Potenza</th></tr>{rows}</table></div><div>
<ul><li>Deviazione 5 kHz con un tono di 2079 Hz: β = 5000 / 2079 = 2,405.</li>
<li>Somma: 0 + 2·(13,47 + 9,32 + 1,98 + 0,21 + 0,01) = <b>{it(tot,1)} W</b>: tutta la potenza c'è, solo spostata.</li>
<li>Sull'analizzatore la prima coppia di righe è a {it(dbm(13.47),1)} dBm, cioè {it(10*math.log10(13.47/50),1)} dB sotto la portante non modulata.</li></ul>
<p class="note">Con β = 1 la portante tiene il {it(v["t1"][0][2]/50*100,0)} % ({it(v["t1"][0][2],1)} W) e la prima coppia {it(v["t1"][1][2],2)} W ciascuna.</p></div></div>''')
c1=v["carson_1.0"]; c2=v["carson_2.405"]; c5=v["carson_5.0"]
D.add("La banda occupata: la regola di Carson",f'''<div class="two"><div>
{eq("B ≈ 2·(Δf + f<sub>m</sub>) = 2·f<sub>m</sub>·(β + 1)")}
<ul><li>Dice quante righe contare: fino a n = β + 1 per lato.</li>
<li>Sommando la potenza di queste righe si ottiene almeno il <b>98 %</b> del totale (spesso il 99 %).</li></ul>
<table><tr><th>β</th><th>Righe per lato</th><th>Potenza contenuta</th></tr>
<tr><td class="l">1</td><td>{c1[0]}</td><td>{it(c1[1]*100,1)} %</td></tr><tr><td class="l">2,405</td><td>{c2[0]}</td><td>{it(c2[1]*100,1)} %</td></tr><tr><td class="l">5</td><td>{c5[0]}</td><td>{it(c5[1]*100,1)} %</td></tr></table></div><div>
<h3>Esempio pratico</h3><ul class="small"><li>FM per radioamatori con Δf = 5 kHz e audio fino a 3 kHz: B ≈ 2·(5 + 3) = <b>16 kHz</b>. Ecco perché questo segnale sta (stretto) in un canale da 25 kHz e non in uno da 12,5 kHz, dove si usa Δf = 2,5 kHz.</li>
<li>Con lo stesso conto si capisce perché "spingere la deviazione" allarga lo spettro e disturba il canale adiacente.</li></ul></div></div>''')
D.add("Densità spettrale e RBW",'''<div class="two"><div><ul>
<li>Per righe isolate (CW, AM, FM a tono) l'analizzatore legge la potenza di ogni riga, qualunque sia la RBW.</li>
<li>Per segnali a <b>spettro continuo</b> (rumore, modi digitali, voce) legge la potenza che cade nel filtro RBW:</li></ul>
<div class="eq">P<sub>letta</sub> = PSD (dBm/Hz) + 10·log(RBW)</div><div class="eq">P<sub>canale</sub> = PSD + 10·log(B<sub>canale</sub>)</div></div><div>
<h3>Esempio</h3><ul class="small"><li>Segnale digitale con densità piatta −100 dBm/Hz su 10 kHz.</li>
<li>Potenza totale: −100 + 10·log(10 000) = <b>−60 dBm</b>, quella che legge un wattmetro.</li>
<li>Con RBW 1 kHz l'analizzatore mostra un "tetto" a −70 dBm: <b>10 dB sotto</b> la potenza vera. Con RBW 100 Hz, a −80 dBm.</li></ul>
<p class="note">Un segnale largo sembra sempre più debole della sua potenza totale: per confrontarlo con il wattmetro serve la misura di potenza di canale (integrazione), non il marker.</p></div></div>''')
D.add("Sommare potenze in dB",f'''<div class="two"><div>
<div class="eq">P<sub>tot</sub> = 10·log( Σ 10<sup>P<sub>i</sub>/10</sup> )</div>
<table><tr><th>Due segnali</th><th>Totale</th></tr>
<tr><td class="l">uguali</td><td>+3,0 dB</td></tr><tr><td class="l">uno 6 dB sotto</td><td>+{it(10*math.log10(1+10**-0.6),2)} dB</td></tr>
<tr><td class="l">uno 10 dB sotto</td><td>+{it(10*math.log10(1.1),2)} dB</td></tr><tr><td class="l">uno 20 dB sotto</td><td>+{it(10*math.log10(1.01),2)} dB</td></tr></table></div><div><ul>
<li>I dB <b>non si sommano</b>: si convertono in watt (o mW), si sommano, si riconvertono.</li>
<li>Vale per segnali a frequenze diverse o scorrelati (righe diverse, rumore).</li>
<li>Due segnali <b>coerenti</b> alla stessa frequenza sommano le <b>tensioni</b>: da +6 dB (in fase) a −∞ (in opposizione). È il caso delle onde stazionarie e degli array di antenne.</li></ul>
<p class="note">Esempio: portante AM a +50 dBm e due bande laterali a +44 dBm → 100 + 25 + 25 = 150 W = +51,8 dBm.</p></div></div>''')
D.add("Fattore di cresta: perché conta",f'''<div class="two"><div><table><tr><th>Segnale</th><th>PEP / media</th></tr>
<tr><td class="l">CW, FM, FSK a inviluppo costante</td><td>0 dB</td></tr><tr><td class="l">SSB a due toni</td><td>3,0 dB</td></tr>
<tr><td class="l">AM al 100 %</td><td>{it(10*math.log10(4/1.5),2)} dB</td></tr><tr><td class="l">SSB con voce (senza compressione)</td><td>~10 dB e oltre</td></tr>
<tr><td class="l">Rumore gaussiano, OFDM</td><td>~10–12 dB (statistico)</td></tr></table></div><div><ul>
<li><b>Amplificatori</b>: devono reggere la PEP senza comprimere. Un finale da 100 W "di media" in FM non fa 100 W di media in SSB pulita.</li>
<li><b>Wattmetri a diodo</b> e rivelatori di picco: la lettura dipende dal fattore di cresta, mentre i termici leggono la media corretta.</li>
<li><b>Analizzatori</b>: con segnali ad alto fattore di cresta il rivelatore peak legge più della potenza media; per la potenza vera serve RMS.</li>
<li><b>Carichi e attenuatori</b>: scaldano con la media, ma l'isolamento deve reggere la tensione di picco.</li></ul></div></div>''')
rows=[("Parseval","potenza totale = somma delle righe (in W)"),("AM","P<sub>tot</sub> = P<sub>c</sub>(1 + m²/2), PEP = P<sub>c</sub>(1 + m)²"),("SSB due toni","PEP = 2·media = 4·P<sub>tono</sub>"),("FM","righe J<sub>n</sub>(β), Σ J<sub>n</sub>² = 1: potenza costante"),
("Carson","B ≈ 2(Δf + f<sub>m</sub>), ~98 % della potenza"),("RBW","P<sub>letta</sub> = PSD + 10·log(RBW)"),("Somme","in watt, mai in dB")]
D.add("Riepilogo",'<table class="sum">'+"".join(f'<tr><td class="l" style="width:200px"><b>{a}</b></td><td class="l">{b}</td></tr>' for a,b in rows)+'</table>')
D.render(); pdf("Potenza_Segnale_Spettro_Bessel_IV3HGA.pdf")
