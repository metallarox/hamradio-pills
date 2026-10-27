from deck import *
D=Deck("Il multimetro:<br>introduzione","Che cosa misura, analogico e digitale, boccole e selettore, cifre e conteggi, risoluzione e precisione, valore medio e true RMS, come sceglierne uno","Il multimetro: introduzione")
panel=f'''<svg viewBox="0 0 420 330" font-family="DejaVu Sans">
<rect x="20" y="10" width="380" height="310" rx="26" fill="#f6f9fc" stroke="{N}" stroke-width="2.5"/>
<rect x="60" y="30" width="300" height="70" rx="8" fill="#dfe9e3" stroke="{N}" stroke-width="2"/><text x="210" y="80" text-anchor="middle" font-family="DejaVu Sans Mono" font-size="40" fill="{N}">12.03</text><text x="345" y="92" font-size="13" fill="{N}">V</text>
<circle cx="210" cy="175" r="48" fill="#fff" stroke="{N}" stroke-width="2.5"/><line x1="210" y1="175" x2="240" y2="140" stroke="{N}" stroke-width="5"/>
<g font-size="12" fill="{N}"><text x="140" y="130">OFF</text><text x="243" y="128">V⎓</text><text x="268" y="160">V~</text><text x="268" y="200">Ω ⟶|</text><text x="243" y="234">A</text><text x="135" y="232">Hz</text><text x="120" y="198">CAP</text><text x="125" y="160">mV</text></g>
<g font-size="13" font-weight="700" text-anchor="middle">
<circle cx="80" cy="280" r="15" fill="#fff" stroke="{C}" stroke-width="3"/><text x="80" y="310" fill="{N}">10 A</text>
<circle cx="160" cy="280" r="15" fill="#fff" stroke="{C}" stroke-width="3"/><text x="160" y="310" fill="{N}">mA µA</text>
<circle cx="250" cy="280" r="15" fill="#222" stroke="{N}" stroke-width="3"/><text x="250" y="310" fill="{N}">COM</text>
<circle cx="335" cy="280" r="15" fill="#e0563b" stroke="{N}" stroke-width="3"/><text x="335" y="310" fill="{N}">V Ω ⟶|</text></g></svg>'''
cards=[("Tensione DC e AC","da mV a centinaia di volt"),("Corrente","da µA a 10–20 A"),("Resistenza","da 0,1 Ω a decine di MΩ"),("Continuità","il cicalino"),("Prova diodi","tensione di giunzione"),
("Capacità","da nF a mF"),("Frequenza e duty","da Hz a qualche MHz"),("hFE","guadagno dei transistor"),("Temperatura","con termocoppia")]
D.add("Che cosa misura",'<div class="grid3">'+"".join(f'<div class="card"><h3>{a}</h3><p>{b}</p></div>' for a,b in cards)+'</div><p class="note" style="margin-top:16px">È lo strumento più usato in assoluto: per questo vale la pena conoscerne bene limiti e funzioni meno ovvie. Non tutti i modelli hanno tutte le funzioni.</p>')
D.add("Analogico e digitale",'''<div class="two"><div><h3>Analogico (a lancetta)</h3><ul class="small">
<li>Uno strumento a bobina mobile con resistenze e shunt commutati.</li>
<li>In tensione ha una resistenza che dipende dalla portata: tipicamente <b>20 kΩ/V</b> (sulla portata 10 V: 200 kΩ). <b>Carica</b> i circuiti ad alta impedenza.</li>
<li>Ottimo per vedere <b>tendenze</b>: un massimo durante una taratura, una tensione che oscilla, la carica di un condensatore.</li>
<li>In ohm la batteria interna fornisce corrente: la polarità sui puntali è spesso invertita rispetto ai colori.</li></ul></div><div>
<h3>Digitale</h3><ul class="small"><li>Un convertitore analogico-digitale (spesso a doppia rampa) e un display.</li>
<li>In tensione ha un'impedenza alta e costante: tipicamente <b>10 MΩ</b>.</li>
<li>Più preciso, più robusto, con molte funzioni in più.</li>
<li>Il <b>bargraph</b> veloce dei modelli migliori recupera parte del vantaggio della lancetta nel seguire le variazioni.</li></ul>
<p class="note">Nel laboratorio di un radioamatore servono entrambi: il digitale per misurare, l'analogico (o il bargraph) per tarare "al massimo" o "al minimo".</p></div></div>''')
D.add("Boccole e selettore",f'''<div class="two"><div class="diag" style="width:92%">{panel}</div><div><ul>
<li><b>COM</b> (nera): il riferimento, sempre usata.</li>
<li><b>V Ω</b> (rossa): tensione, resistenza, diodi, capacità, frequenza. Ingresso ad alta impedenza.</li>
<li><b>mA µA</b>: correnti piccole, con il suo shunt e un fusibile.</li>
<li><b>10 A</b> (o 20 A): correnti forti, shunt da pochi milliohm e fusibile di potenza.</li></ul>
<div class="warn">Le boccole di corrente sono <b>quasi un cortocircuito</b> tra i puntali. Il puntale nella boccola A con il selettore in tensione è la causa principale di incidenti (vedi la lezione sulla sicurezza).</div></div></div>''')
D.add("Cifre e conteggi",'''<div class="two"><div><ul>
<li>Il display si descrive con il numero massimo che può mostrare: i <b>conteggi</b>.</li>
<li>"3½ cifre" significa che la prima cifra può essere solo 0 o 1: massimo <b>1999</b> conteggi.</li>
<li>Modelli migliori: 4000, 6000, 20 000, 50 000 conteggi e oltre.</li></ul>
<table><tr><th>Conteggi</th><th>Portate tipiche in V</th></tr>
<tr><td class="l">2000</td><td class="l">1,999 / 19,99 / 199,9</td></tr><tr><td class="l">6000</td><td class="l">6,000 / 60,00 / 600,0</td></tr><tr><td class="l">50 000</td><td class="l">5,0000 / 50,000 / 500,00</td></tr></table></div><div>
<h3>Perché conta</h3><ul class="small"><li>Con 2000 conteggi, 13,8 V si leggono sulla portata 199,9 V: <b>13,8</b>. Con 6000 conteggi, sulla portata 60,00 V: <b>13,80</b>, una cifra in più.</li>
<li>Una tensione di 2,1 V su un 2000 conteggi passa alla portata superiore e perde risoluzione; su un 6000 conteggi resta 2,100.</li>
<li>Più conteggi = più <b>risoluzione</b>, ma non per forza più <b>precisione</b>: lo dice la specifica di accuratezza.</li></ul></div></div>''')
D.add("Risoluzione e precisione",'''<div class="two"><div>
<div class="eq">errore = ±(x % della lettura + n digit)</div>
<ul class="small"><li>La specifica è scritta così nel manuale, per ogni funzione e portata. "Digit" (o "counts") sono unità dell'ultima cifra.</li></ul>
<h3>Esempio</h3><ul class="small"><li>Multimetro da 6000 conteggi, ±(0,5 % + 2) in DC.</li>
<li>Leggi <b>12,00 V</b> sulla portata 60,00 V: 0,5 % di 12,00 = 0,06 V, più 2 digit da 0,01 V = 0,02 V.</li>
<li>Il valore vero è tra <b>11,92 e 12,08 V</b>.</li></ul></div><div><ul class="small">
<li>Leggi <b>0,500 V</b> sulla portata 6,000 V: 0,0025 + 0,002 = ±0,0045 V, cioè quasi ±1 %: i digit pesano di più sulle letture piccole.</li>
<li>Usa la portata più bassa che contiene il valore: stesso numero di digit, ma più piccoli.</li>
<li>In AC, in corrente e in capacità la precisione è di solito <b>peggiore</b> che in tensione DC.</li>
<li>Le specifiche valgono in un intervallo di temperatura (spesso 18–28 °C) e per un certo tempo dalla taratura.</li></ul>
<p class="note">Un display con tante cifre "stabili" non garantisce che siano giuste: è la differenza tra risoluzione e precisione.</p></div></div>''')
D.add("Valore medio e true RMS",'''<div class="two"><div><ul>
<li>In AC il multimetro deve dare il <b>valore efficace</b> (RMS): quello che produce lo stesso calore di una continua.</li>
<li>I modelli economici misurano il <b>valore medio raddrizzato</b> e lo moltiplicano per 1,11, il rapporto giusto solo per una <b>sinusoide pura</b>.</li>
<li>I modelli <b>true RMS</b> calcolano il valore efficace vero, entro un certo fattore di cresta e una certa banda.</li></ul></div><div>
<h3>Quando fa differenza</h3><ul class="small"><li>Onde quadre, triangolari, impulsi, uscite di inverter e dimmer, correnti di alimentatori switching.</li>
<li>Su questi segnali un multimetro a valore medio può sbagliare di decine di % (i numeri sono nella lezione sulla tensione).</li>
<li>Sulla rete pulita, o su un trasformatore senza carico distorto, i due tipi danno lo stesso risultato.</li></ul></div></div>''')
D.add("Autorange, portata manuale e velocità",'''<div class="two"><div><ul>
<li>In <b>autorange</b> lo strumento sceglie da solo la portata: comodo, ma impiega qualche decimo di secondo a decidere.</li>
<li>Con un valore che cambia vicino al limite di una portata, l'autorange "salta" avanti e indietro.</li>
<li>La portata <b>manuale</b> (tasto RANGE) blocca la scala: misura più veloce e stabile, utile per tarature e confronti.</li></ul></div><div>
<h3>Velocità di lettura</h3><ul class="small"><li>Le cifre si aggiornano tipicamente 2–4 volte al secondo; il bargraph, quando c'è, molto più spesso.</li>
<li>Per regolare un trimmer "al massimo" guarda il bargraph o usa un analogico.</li>
<li>Su segnali che cambiano rapidamente (correnti di spunto, picchi) servono le funzioni MIN/MAX e peak, viste più avanti.</li></ul></div></div>''')
D.add("Come scegliere un multimetro",'''<div class="two"><div><ul>
<li><b>Categoria di sicurezza reale</b> (CAT III 600 V o meglio per chi lavora sulla rete), certificata da un ente indipendente.</li>
<li><b>Fusibili ad alto potere di interruzione</b> (HRC) sulle boccole di corrente, non fusibili di vetro da pochi euro.</li>
<li><b>True RMS</b>, con la banda AC dichiarata.</li>
<li>Almeno <b>6000 conteggi</b> e un bargraph.</li></ul></div><div><ul>
<li><b>LoZ</b> (bassa impedenza) per non farsi ingannare dalle tensioni fantasma.</li>
<li>Puntali di qualità con la stessa categoria dello strumento.</li>
<li>Per il banco: MIN/MAX, REL, misura di µA, capacità, frequenza.</li>
<li>Diffida delle categorie "1000 V CAT IV" stampate su strumenti economici che dentro hanno fusibili di vetro: l'etichetta non è una garanzia.</li></ul></div></div>''')
rows=[("Boccole","COM sempre; V Ω per tensione e ohm; A solo per corrente"),("Conteggi","risoluzione: 2000, 6000, 50 000"),("Precisione","±(% lettura + digit): fai il conto"),("True RMS","indispensabile con forme d'onda non sinusoidali"),("Portata","la più bassa che contiene il valore; manuale per tarare")]
D.add("Riepilogo",'<table class="sum">'+"".join(f'<tr><td class="l" style="width:200px"><b>{a}</b></td><td class="l">{b}</td></tr>' for a,b in rows)+'</table>')
D.render(); pdf("MM_Introduzione_IV3HGA.pdf")
