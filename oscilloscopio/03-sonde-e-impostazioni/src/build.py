import math
from deck import *
D=Deck("Sonde<br>e impostazioni","La sonda passiva 10×, la compensazione, il carico sul circuito, la massa corta, le sonde speciali e come impostare verticale, base dei tempi e trigger","L'oscilloscopio: sonde e impostazioni")
D.add("La sonda passiva 10×",'''<div class="two"><div><ul>
<li>Dentro la punta c'è una resistenza da <b>9 MΩ</b> in parallelo a un piccolo condensatore; con l'ingresso da 1 MΩ forma un partitore <b>10:1</b>.</li>
<li>Il circuito vede circa <b>10 MΩ in parallelo a 10–15 pF</b>: molto meno carico di una sonda 1×.</li>
<li>Un condensatore regolabile (vite sul connettore o sulla punta) bilancia il partitore anche in frequenza: è la <b>compensazione</b>.</li></ul></div><div>
<h3>1× o 10×?</h3><table><tr><th></th><th>1×</th><th>10×</th></tr>
<tr><td class="l">Impedenza vista</td><td class="l">1 MΩ ∥ ~50–100 pF</td><td class="l">10 MΩ ∥ ~10–15 pF</td></tr>
<tr><td class="l">Banda tipica</td><td class="l">pochi MHz</td><td class="l">quella dello strumento</td></tr>
<tr><td class="l">Sensibilità</td><td class="l">massima</td><td class="l">10 volte meno</td></tr></table>
<p class="note">Usa il 10× quasi sempre. Il 1× serve solo per segnali molto piccoli e lenti (ripple di pochi mV, audio).</p></div></div>''')
D.add("La compensazione",f'''<div class="fig" style="width:96%">{svg("comp.svg")}</div><div class="two" style="align-items:start;gap:30px"><div><ol class="small">
<li>Collega la sonda all'uscita di <b>calibrazione</b> dello strumento (un'onda quadra, di solito 1 kHz).</li>
<li>Regola la vite di compensazione finché gli spigoli sono <b>piatti e squadrati</b>.</li></ol></div><div><ul class="small">
<li>Una sonda scompensata sbaglia l'ampiezza alle frequenze medie e alte e deforma tutti i segnali non sinusoidali.</li>
<li>Ricompensa ogni volta che cambi canale o strumento: ogni ingresso ha una capacità leggermente diversa.</li></ul></div></div>''')
rows="".join(f'<tr><td class="l">{lab}</td><td>{x}</td></tr>' for lab,x in (("1 MHz","15,9 kΩ"),("10 MHz","1,59 kΩ"),("30 MHz","531 Ω"),("100 MHz","159 Ω")))
D.add("La sonda carica il circuito",f'''<div class="two"><div><ul>
<li>La capacità della punta è piccola, ma alle alte frequenze diventa un'impedenza bassa in parallelo al punto misurato:</li></ul>
{eq("X<sub>C</sub> = 1 / (2π·f·C)")}
<table><tr><th>Con 10 pF a</th><th>X<sub>C</sub></th></tr>{rows}</table></div><div>
<h3>Conseguenze pratiche</h3><ul class="small"><li>Su un nodo ad alta impedenza (oscillatori, circuiti accordati, gate) la sonda <b>cambia</b> quello che misuri.</li>
<li>Toccando il circuito accordato di un VFO con la sonda, la frequenza si sposta o l'oscillatore si spegne.</li>
<li>Misura dove l'impedenza è bassa (uscita di un buffer, di un emitter follower) o usa una sonda attiva a bassa capacità.</li>
<li>Per segnali RF su 50 Ω usa l'ingresso a 50 Ω o una sonda a bassa impedenza, non la sonda 10× appoggiata su una linea.</li></ul></div></div>''')
D.add("La massa corta",f'''<div class="two"><div class="fig">{svg("ground.svg")}<p class="cap">Fronte veloce visto con 200 MHz di banda: il cavetto lungo crea una risonanza con la capacità della punta.</p></div><div><ul class="small">
<li>Il cavetto di massa a coccodrillo è un'<b>induttanza</b>: circa 1 nH per mm, cioè ~150 nH per 15 cm.</li>
<li>Con i ~10 pF della punta forma un circuito risonante: con 150 nH risuona a circa <b>130 MHz</b> e sui fronti veloci compaiono oscillazioni che nel circuito <b>non esistono</b>.</li>
<li>Il cavetto è anche una spira che raccoglie campi magnetici: vicino a uno switching vedi disturbi "dal nulla".</li>
<li>Soluzione: la <b>molla di massa</b> corta sulla punta, o un adattatore da circuito stampato.</li></ul>
<p class="note">Test rapido: tocca con la punta la sua stessa clip di massa vicino al circuito. Quello che vedi è il disturbo raccolto dal cavetto.</p></div></div>''')
D.add("Le altre sonde",'''<table><tr><th>Sonda</th><th>Come funziona</th><th>Quando usarla</th></tr>
<tr><td class="l"><b>Passiva 50 Ω (Z0)</b></td><td class="l">resistenza da 450 o 950 Ω in punta verso l'ingresso a 50 Ω: 10× o 20×</td><td class="l">segnali veloci su circuiti a bassa impedenza; capacità bassissima ma carico resistivo</td></tr>
<tr><td class="l"><b>Attiva (FET)</b></td><td class="l">amplificatore nella punta, capacità di circa 1 pF</td><td class="l">nodi ad alta impedenza ad alta frequenza, oscillatori</td></tr>
<tr><td class="l"><b>Differenziale</b></td><td class="l">misura la differenza tra due punti, isolata dalla terra</td><td class="l">misure sulla rete, ponti, gate driver, bus differenziali</td></tr>
<tr><td class="l"><b>Di corrente</b></td><td class="l">pinza a trasformatore (solo AC) o a effetto Hall (anche DC)</td><td class="l">correnti di alimentatori, motori, finali, senza interrompere il circuito</td></tr>
<tr><td class="l"><b>Alta tensione</b></td><td class="l">partitori 100× o 1000× isolati</td><td class="l">anodiche, alimentatori ad alta tensione, sempre con massa a terra</td></tr></table>
<p class="note" style="margin-top:12px">Ogni sonda ha la sua banda, il suo limite di tensione e il suo fattore di attenuazione da impostare nello strumento.</p>''')
D.add("Impostare il canale verticale",'''<div class="two"><div><table>
<tr><td class="l"><b>Fattore sonda</b></td><td class="l">1×, 10×, 100×: deve corrispondere alla sonda, o tutte le tensioni sono sbagliate</td></tr>
<tr><td class="l"><b>V/div</b></td><td class="l">il segnale deve occupare buona parte dello schermo: più bit dell'ADC usati</td></tr>
<tr><td class="l"><b>Posizione / offset</b></td><td class="l">sposta la traccia; l'offset permette di "zoomare" su una parte del segnale</td></tr>
<tr><td class="l"><b>Accoppiamento</b></td><td class="l">DC vede tutto, AC toglie la continua (passa-alto), GND mostra lo zero</td></tr>
<tr><td class="l"><b>Limite di banda</b></td><td class="l">tipicamente 20 MHz: toglie il rumore ad alta frequenza</td></tr>
<tr><td class="l"><b>Impedenza</b></td><td class="l">1 MΩ con le sonde, 50 Ω con cavi coassiali da sorgenti a 50 Ω</td></tr></table></div><div><ul>
<li>Se la traccia esce dallo schermo in verticale, l'ADC va in saturazione: le misure automatiche diventano false anche sulla parte visibile.</li>
<li>Usa l'accoppiamento DC come default: AC solo quando devi guardare piccole variazioni sopra una continua (vedi il trucco del ripple).</li>
<li>L'inversione di canale e la funzione math servono per misure differenziali e somme.</li></ul></div></div>''')
D.add("Base dei tempi e trigger",'''<div class="two"><div><h3>Orizzontale</h3><ul class="small">
<li><b>Tempo/div</b> per vedere 2–5 periodi del segnale: abbastanza per capirlo, non troppi per perdere i dettagli.</li>
<li><b>Posizione / ritardo</b>: sposta il punto di trigger sullo schermo, anche per vedere cosa è successo <b>prima</b> dell'evento (pre-trigger).</li>
<li><b>Zoom</b>: una seconda finestra ingrandita su una parte dell'acquisizione.</li>
<li>Ricorda: allargando il tempo/div il sample rate può scendere.</li></ul></div><div>
<h3>Trigger</h3><ul class="small"><li><b>Sorgente</b>: il canale più "pulito" e stabile.</li>
<li><b>Livello</b> a metà dell'escursione del segnale; <b>pendenza</b> sul fronte che ti interessa.</li>
<li><b>Modo</b> auto per trovare il segnale, normal per eventi irregolari, single per catturare un evento.</li>
<li>Con segnali rumorosi: accoppiamento del trigger HF reject o noise reject.</li>
<li>Con treni d'impulsi: <b>holdoff</b> pari alla durata del treno.</li></ul></div></div>''')
D.add("Un metodo che funziona sempre",'''<div class="flow">'''+"".join(f'<div class="card"><b>{i+1}</b><h3>{a}</h3><p>{b}</p></div>' for i,(a,b) in enumerate([("Default","richiama le impostazioni di fabbrica"),("Sonda","10×, compensata, fattore impostato"),("Verticale","DC, V/div adatto, zero noto"),("Tempo e trigger","2–5 periodi, livello a metà"),("Misura","cursori o misure automatiche, controllate")]))+'''</div>
<div class="two" style="margin-top:28px;align-items:start"><div><ul class="small"><li>L'<b>autoset</b> è comodo per trovare un segnale sconosciuto, ma sceglie da solo accoppiamento, trigger e scale: poi controlla e correggi a mano.</li></ul></div><div><ul class="small">
<li>Se qualcosa non torna, torna al passo 1: un'impostazione dimenticata (offset, media, limite di banda) è la causa più comune di misure strane.</li></ul></div></div>''')
rows=[("Sonda 10×","10 MΩ ∥ ~10–15 pF, banda piena"),("Compensazione","onda quadra di calibrazione, spigoli piatti"),("Carico","X<sub>C</sub> = 1/(2πfC): 159 Ω a 100 MHz con 10 pF"),("Massa","molla corta: il cavetto crea risonanze finte"),
("Verticale","fattore sonda, V/div, DC, limite di banda"),("Trigger","livello a metà, pendenza, modo giusto")]
D.add("Riepilogo",'<table class="sum">'+"".join(f'<tr><td class="l" style="width:220px"><b>{a}</b></td><td class="l">{b}</td></tr>' for a,b in rows)+'</table>')
D.render(); pdf("OSC_Sonde_Impostazioni_IV3HGA.pdf")
