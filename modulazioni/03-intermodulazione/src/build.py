from deck import *
D=Deck("L'intermodulazione","Che cos'è, da dove nasce, perché i prodotti di 3° ordine sono i più fastidiosi, ricevitori, trasmettitori, siti con più ponti, intermodulazione passiva, come riconoscerla e come combatterla","Modulazioni · l'intermodulazione")
D.add("Che cos'è",'''<div class="two"><div><ul>
<li>Un circuito perfettamente <b>lineare</b> lascia passare due segnali senza mescolarli. Ogni circuito reale, se spinto abbastanza, è un po' <b>non lineare</b>.</li>
<li>Una non linearità si può descrivere così:</li></ul>
<div class="eq">y = a<sub>1</sub>·x + a<sub>2</sub>·x² + a<sub>3</sub>·x³ + …</div>
<ul class="small"><li>Con due segnali f1 e f2 in ingresso, i termini x², x³ … producono nuove frequenze che <b>non c'erano</b>: m·f1 ± n·f2.</li>
<li>L'<b>ordine</b> del prodotto è |m| + |n|.</li></ul></div><div>
<table><tr><th>Ordine</th><th>Prodotti</th></tr><tr><td class="l">2°</td><td class="l">2f1, 2f2, f1 + f2, f2 − f1</td></tr>
<tr><td class="l">3°</td><td class="l">3f1, 3f2, <b>2f1 − f2</b>, <b>2f2 − f1</b>, 2f1 + f2 …</td></tr>
<tr><td class="l">5°</td><td class="l"><b>3f1 − 2f2</b>, <b>3f2 − 2f1</b> …</td></tr></table>
<p class="note">È la stessa cosa che fa volutamente un mixer (prodotti di 2° ordine). L'intermodulazione è quando succede dove non la vuoi.</p></div></div>''')
D.add("Perché il 3° ordine è il peggiore",f'''<div class="fig" style="width:96%">{svg("prods.svg")}</div><div class="two" style="align-items:start;gap:30px"><div><ul class="small">
<li>Due ponti a 145,600 e 145,725 MHz. I prodotti di ordine dispari 2f1 − f2 e 2f2 − f1 cadono a <b>145,475 e 145,850 MHz</b>: nella stessa banda, accanto ai segnali originali.</li></ul></div><div><ul class="small">
<li>I prodotti di 2° ordine (f1 + f2 = 291,3 MHz, f2 − f1 = 125 kHz) cadono lontano e si filtrano facilmente. Quelli di 3° e 5° ordine no: nessun filtro di banda li separa dai segnali utili.</li></ul></div></div>''')
D.add("Le pendenze: 3 dB per dB",f'''<div class="two"><div class="fig">{svg("slopes.svg")}</div><div><ul class="small">
<li>Se i due segnali aumentano di 1 dB, i prodotti di 3° ordine aumentano di <b>3 dB</b>: crescono molto più in fretta.</li>
<li>Il punto in cui le due rette si incrocerebbero è il <b>punto di intercetta IP3</b>: più è alto, più il circuito è lineare.</li></ul>
<div class="eq">IM3 (dBc) = 2·(P<sub>tono</sub> − IP3)</div>
<ul class="small"><li>Con IP3 = +10 dBm: toni a −10 dBm danno IM3 a −40 dBc; toni a −20 dBm, IM3 a −60 dBc. 10 dB in meno di segnale = 20 dB di intermodulazione in meno.</li>
<li>Misure di IP3 e DR3 dei ricevitori: capitolo sul generatore.</li></ul></div></div>''')
D.add("Intermodulazione nel ricevitore",'''<div class="two"><div><ul>
<li>Due segnali forti (broadcast FM, ponti vicini, cercapersone, radar) entrano nel preamplificatore o nel mixer e producono un prodotto <b>sulla frequenza che stai ascoltando</b>.</li>
<li>Si sente un segnale "fantasma": spesso è la somma confusa di due modulazioni, che appare e sparisce quando uno dei due trasmettitori smette.</li></ul></div><div>
<h3>Come riconoscerla: il test dell'attenuatore</h3><ul><li>Inserisci un attenuatore da 10 dB sull'antenna.</li>
<li>Un segnale <b>vero</b> cala di 10 dB.</li><li>Un prodotto di 3° ordine cala di <b>30 dB</b>: sparisce quasi del tutto.</li>
<li>È lo stesso trucco della "riga vera" dell'analizzatore di spettro.</li></ul>
<h3>Rimedi</h3><ul><li>Filtri preselettori e passa-banda davanti al ricevitore, o filtri notch sulla frequenza del disturbo.</li>
<li>Meno guadagno: spegni il preamplificatore, usa l'attenuatore. In HF il rumore esterno è spesso più alto, quindi non perdi sensibilità.</li></ul></div></div>''')
D.add("Intermodulazione nel trasmettitore",'''<div class="two"><div><h3>Nel segnale che trasmetti</h3><ul>
<li>In SSB la voce contiene tante frequenze insieme: un finale non lineare le mescola e allarga il segnale (<b>splatter</b>).</li>
<li>Si misura con il test a due toni (capitolo sull'analizzatore, prelievi e accoppiatori): IMD tipiche di −30/−40 dB sotto la PEP per i ricetrasmettitori commerciali.</li>
<li>Cause: finale troppo spinto, ALC che entra in modo brusco, compressione esagerata, alimentazione che crolla sotto carico.</li></ul></div><div>
<h3>Intermodulazione "dall'esterno"</h3><ul><li>Il segnale di un altro trasmettitore vicino entra dall'antenna nel tuo finale; lì si mescola con il tuo e viene ritrasmesso a 2f1 − f2.</li>
<li>Succede nei siti con più stazioni e nei contest multi-operatore, anche tra apparati spenti in ricezione.</li>
<li>Rimedi: separazione tra antenne, filtri a cavità, <b>isolatori e circolatori</b> sull'uscita dei trasmettitori dei ponti.</li></ul></div></div>''')
D.add("Siti con più ponti radio",'''<div class="two"><div><ul>
<li>In un sito (traliccio, cima di un monte) convivono decine di trasmettitori e ricevitori: le combinazioni possibili sono migliaia.</li>
<li>Prima di installare un nuovo apparato si fa un <b>calcolo di intermodulazione</b>: si verifica che nessun prodotto di 3° e 5° ordine (e spesso 7°) delle frequenze presenti cada su un ricevitore del sito.</li></ul>
<h3>Esempio</h3><ul><li>TX a 145,600 e 145,725 MHz: il 3° ordine cade a 145,475 e 145,850; il 5° a 145,350 e 145,975 MHz.</li>
<li>Se un ricevitore del sito è su una di queste frequenze, va spostato o protetto.</li></ul></div><div>
<h3>Buone pratiche</h3><ul><li>Duplexer e filtri a cavità su ogni ripetitore; circolatori sulle uscite.</li>
<li>Separazione verticale tra le antenne (molto più efficace di quella orizzontale).</li>
<li>Cavi a doppia schermatura o rigidi, connettori di qualità serrati.</li>
<li>Registro delle frequenze del sito sempre aggiornato.</li></ul></div></div>''')
D.add("Intermodulazione passiva (PIM)",'''<div class="two"><div><ul>
<li>Non serve un transistor: qualsiasi giunzione metallica <b>non lineare</b> può generare intermodulazione quando è attraversata da correnti RF forti.</li>
<li>Il caso classico è il "<b>rusty bolt</b>": un bullone arrugginito, una giunzione ossidata, un contatto lento su un traliccio o una grondaia vicina all'antenna.</li></ul>
<h3>Cause tipiche</h3><ul><li>Connettori ossidati, serrati male o con contatti placcati in nichel.</li>
<li>Materiali ferromagnetici (acciaio) nel percorso della corrente RF.</li><li>Cavi danneggiati, calze allentate.</li></ul></div><div>
<h3>Come si manifesta</h3><ul><li>Disturbi che cambiano con il vento, la pioggia o la temperatura (la giunzione si muove o si bagna).</li>
<li>Rumore di fondo che sale quando i trasmettitori del sito sono attivi.</li>
<li>Si cerca con analizzatori PIM dedicati, oppure "a tentativi": scuotendo cavi e strutture mentre si ascolta.</li>
<li>Rimedi: connettori in buono stato e protetti dalle intemperie, giunzioni pulite e ben serrate, niente ferro vicino alle antenne.</li></ul></div></div>''')
rows=[("Origine","non linearità: prodotti m·f1 ± n·f2"),("3° ordine","2f1 − f2, 2f2 − f1: in banda, impossibili da filtrare"),("Pendenza","3 dB per dB; IP3 misura la linearità"),("Test","10 dB di attenuatore: il prodotto cala di 30 dB"),("Siti","calcolo dei prodotti, cavità, circolatori"),("PIM","bulloni arrugginiti e connettori ossidati")]
D.add("Riepilogo",'<table class="sum">'+"".join(f'<tr><td class="l" style="width:160px"><b>{a}</b></td><td class="l">{b}</td></tr>' for a,b in rows)+'</table>')
D.render(); pdf("MOD_Intermodulazione_IV3HGA.pdf")
