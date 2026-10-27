from deck import *
D=Deck("L'oscilloscopio:<br>come funziona","Dall'oscilloscopio analogico al digitale: schema a blocchi, banda e tempo di salita, campionamento e aliasing, memoria, trigger e modi di acquisizione","L'oscilloscopio: come funziona")
blk=f'''<svg viewBox="0 0 1120 300" font-family="DejaVu Sans">{ARW}
<circle cx="25" cy="80" r="9" fill="#fff" stroke="{N}" stroke-width="2"/><text x="25" y="50" text-anchor="middle" font-size="13" fill="{N}">CH1</text>
{ln(34,80,70,80)}{box(70,45,150,70,"Accoppiamento|DC/AC, 1 MΩ/50 Ω",L,13)}{ln(220,80,250,80)}{box(250,45,150,70,"Attenuatore +|amplificatore|(V/div)",L,13)}{ln(400,80,430,80)}
{box(430,45,140,70,"Filtro anti-|aliasing / banda",L,13)}{ln(570,80,600,80)}{box(600,45,130,70,"ADC|(campionamento)")}{ln(730,80,760,80)}{box(760,45,140,70,"Memoria|di acquisizione")}{ln(900,80,930,80)}
{box(930,35,180,90,"Elaborazione|e display|(misure, FFT, math)","#fff")}
{box(430,185,140,70,"Trigger|(livello, fronte)")}<path d="M500 115 V185" stroke="{N}" stroke-width="2" stroke-dasharray="5 4" fill="none"/>
{ln(570,220,830,220)}<path d="M830 220 V115" stroke="{N}" stroke-width="2" fill="none" marker-end="url(#ar)"/>
{box(600,240,130,50,"Base dei tempi|(clock)",L,13)}{ln(665,240,665,115)}
<text x="700" y="210" font-size="12" fill="#555">"da qui in poi salva e mostra"</text></svg>'''
D.add("Che cosa fa un oscilloscopio",'''<div class="two"><div><ul>
<li>Disegna la <b>tensione in funzione del tempo</b>: asse verticale = volt, asse orizzontale = tempo.</li>
<li>È lo strumento per vedere <b>forme d'onda</b>: impulsi, fronti, rumore, oscillazioni, inviluppi, ritardi tra segnali.</li>
<li>Complementare all'analizzatore di spettro: l'oscilloscopio guarda il <b>tempo</b>, l'analizzatore la <b>frequenza</b>.</li></ul></div><div>
<h3>Analogico e digitale</h3><ul class="small"><li><b>Analogico</b> (a tubo, CRT): il segnale devia direttamente il fascio di elettroni. Visione "dal vivo", nessun campionamento, ma niente memoria e misure solo a occhio.</li>
<li><b>Digitale</b> (DSO): il segnale viene campionato da un ADC e salvato in memoria. Misure automatiche, memoria, FFT, trigger evoluti, ma nuovi tranelli: campionamento, aliasing, memoria limitata.</li>
<li>Oggi quasi tutti sono digitali; gli analogici restano ottimi strumenti didattici e da banco.</li></ul></div></div>''')
D.add("Lo schema a blocchi di un oscilloscopio digitale",f'<div class="diag" style="width:96%">{blk}</div>'+'''<div class="grid3" style="margin-top:6px">
<div class="card"><h3>Ingresso e verticale</h3><p>Accoppiamento, impedenza d'ingresso, attenuatori e amplificatori che portano il segnale al livello giusto per l'ADC.</p></div>
<div class="card"><h3>ADC e memoria</h3><p>Il segnale diventa una sequenza di numeri: quanti al secondo (sample rate) e quanti in tutto (memoria).</p></div>
<div class="card"><h3>Trigger</h3><p>Decide <b>quando</b> salvare: senza trigger la traccia scorre e non si legge nulla.</p></div></div>''')
D.add("Banda e tempo di salita",f'''<div class="fig" style="width:92%">{svg("bw.svg")}</div><div class="two" style="align-items:start;gap:30px"><div>
{eq("t<sub>salita</sub> ≈ 0,35 / banda")}<ul class="small"><li>La <b>banda</b> è la frequenza a cui un sinusoide viene attenuato di 3 dB (cioè letto circa il 30 % più basso).</li></ul></div><div><ul class="small">
<li>Un'onda quadra da 10 MHz vista con 20 MHz di banda sembra quasi una sinusoide: le sue armoniche vengono tagliate.</li>
<li>Regola pratica: banda almeno <b>3–5 volte</b> la frequenza più alta che ti interessa, o un tempo di salita dello strumento 3–5 volte più veloce di quello da misurare.</li></ul></div></div>''')
D.add("Campionamento e aliasing",f'''<div class="two"><div class="fig">{svg("alias.svg")}</div><div><ul class="small">
<li>Il DSO preleva campioni a intervalli regolari: il <b>sample rate</b> (MS/s o GS/s).</li>
<li>Teorema del campionamento: servono più di <b>2 campioni per periodo</b> della componente più alta. Sotto questo limite compare l'<b>aliasing</b>: un segnale "finto" a frequenza più bassa.</li>
<li>Nell'esempio un 9 MHz campionato a 10 MS/s appare come un perfetto 1 MHz. Con il trigger stabile, l'inganno è totale.</li>
<li>In pratica: sample rate almeno <b>2,5 volte</b> la banda per ricostruire i sinusoidi, e <b>5–10 volte</b> per vedere bene i fronti.</li></ul>
<p class="note">Sospetto di aliasing? Cambia la base dei tempi: un segnale vero si "comprime" o si "allarga" come previsto, un alias cambia frequenza in modo strano.</p></div></div>''')
D.add("Memoria e sample rate",'''<div class="two"><div><ul>
<li>Il sample rate massimo vale solo se c'è abbastanza <b>memoria</b> per tutta la finestra visualizzata (di solito 10 divisioni):</li></ul>
<div class="eq">sample rate = memoria / (10 · tempo/div)</div>
<ul class="small"><li>Esempio: 10 000 punti di memoria, 1 ms/div → 10 000 / 10 ms = <b>1 MS/s</b>, anche se lo strumento sa fare 1 GS/s.</li>
<li>Con 10 milioni di punti alla stessa base dei tempi: 1 GS/s.</li></ul></div><div>
<h3>Cosa significa in pratica</h3><ul class="small"><li>Allargando la base dei tempi il sample rate <b>scende</b>, e con lui la capacità di vedere dettagli veloci.</li>
<li>Su finestre lunghe (ms o secondi) un glitch di pochi ns può cadere tra due campioni e sparire.</li>
<li>Il sample rate effettivo è quasi sempre scritto sullo schermo: guardalo.</li>
<li>Più memoria rende l'interfaccia più lenta: usala quando serve, non sempre al massimo.</li></ul></div></div>''')
D.add("Il trigger",'''<div class="two"><div><ul>
<li>Il trigger "aggancia" la forma d'onda: l'acquisizione parte quando il segnale attraversa un <b>livello</b> con una certa <b>pendenza</b> (fronte di salita o di discesa).</li>
<li>Così ogni traccia comincia nello stesso punto e l'immagine è ferma.</li></ul>
<table><tr><th>Modo</th><th>Cosa fa</th></tr>
<tr><td class="l"><b>Auto</b></td><td class="l">se non arriva il trigger, disegna comunque: utile per trovare il segnale</td></tr>
<tr><td class="l"><b>Normal</b></td><td class="l">disegna solo quando c'è il trigger: per eventi rari o irregolari</td></tr>
<tr><td class="l"><b>Single</b></td><td class="l">cattura un solo evento e si ferma</td></tr></table></div><div>
<h3>Trigger evoluti</h3><ul class="small"><li><b>Larghezza d'impulso</b>: impulsi più corti o più lunghi di un valore.</li>
<li><b>Runt</b>: impulsi che non raggiungono il livello logico pieno.</li>
<li><b>Video, bus seriali</b> (UART, I²C, SPI, CAN) sui modelli che li hanno.</li>
<li><b>Holdoff</b>: ignora nuovi trigger per un certo tempo, per agganciare treni d'impulsi complessi.</li>
<li><b>Accoppiamento del trigger</b>: HF reject, LF reject, noise reject per segnali disturbati.</li></ul></div></div>''')
D.add("Modi di acquisizione",'''<div class="two"><div><table><tr><th>Modo</th><th>A cosa serve</th></tr>
<tr><td class="l"><b>Normal / sample</b></td><td class="l">un campione per intervallo: il modo standard</td></tr>
<tr><td class="l"><b>Peak detect</b></td><td class="l">tiene massimo e minimo tra un campione e l'altro: non perde i glitch anche con sample rate basso</td></tr>
<tr><td class="l"><b>High resolution</b></td><td class="l">media i campioni vicini: meno rumore, più bit effettivi, banda ridotta</td></tr>
<tr><td class="l"><b>Average</b></td><td class="l">media su più acquisizioni: toglie il rumore casuale da segnali ripetitivi</td></tr>
<tr><td class="l"><b>Envelope / persistenza</b></td><td class="l">accumula più tracce: jitter, variazioni, eventi rari</td></tr></table></div><div><ul>
<li>Average e high resolution "puliscono" la traccia, ma nascondono il rumore vero e gli eventi singoli.</li>
<li>Peak detect è il modo giusto quando cerchi spike su finestre di tempo lunghe.</li>
<li>La <b>persistenza</b> riproduce il bello dell'analogico: vedi quanto spesso una forma d'onda passa da un punto.</li></ul></div></div>''')
D.add("Le specifiche che contano",'''<div class="two"><div><ul>
<li><b>Banda</b> analogica (e tempo di salita), per ogni canale.</li>
<li><b>Sample rate</b>: per canale o condiviso tra i canali? Spesso si dimezza usandone due.</li>
<li><b>Memoria</b>: quanti punti per canale.</li>
<li><b>Risoluzione verticale</b>: 8 bit sono 256 livelli; 10–12 bit servono per piccoli segnali su grandi offset.</li></ul></div><div><ul>
<li><b>Impedenza d'ingresso</b>: 1 MΩ (con sonde) e, sui modelli più veloci, anche 50 Ω.</li>
<li><b>Tensione massima</b> in ingresso e categoria di misura (CAT).</li>
<li><b>Velocità di aggiornamento</b> (forme d'onda al secondo): conta per vedere eventi rari.</li>
<li>Trigger, decodifiche seriali, FFT, generatore integrato, isolamento dei canali.</li></ul></div></div>''')
rows=[("Banda","t<sub>salita</sub> ≈ 0,35 / banda; 3–5 volte il segnale"),("Sample rate","> 2 campioni per periodo, meglio 5–10 per i fronti"),("Aliasing","segnale finto a bassa frequenza: cambia la base dei tempi"),
("Memoria","sample rate = memoria / (10 · tempo/div)"),("Trigger","livello e pendenza; auto, normal, single"),("Acquisizione","peak detect per i glitch, average per il rumore")]
D.add("Riepilogo",'<table class="sum">'+"".join(f'<tr><td class="l" style="width:220px"><b>{a}</b></td><td class="l">{b}</td></tr>' for a,b in rows)+'</table>')
D.render(); pdf("OSC_Come_Funziona_IV3HGA.pdf")
