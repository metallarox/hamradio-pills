from deck import *
D=Deck("Misure inconsuete<br>e trucchi","Riconoscere le righe false, misurare vicino al rumore, cifra di rumore, sonde di campo vicino, misure di campo, ascoltare i segnali e altri trucchi da banco","L'analizzatore di spettro: misure inconsuete e trucchi")
cards=[("La riga è vera?","quattro test rapidi"),("Vicino al rumore","correggere la lettura"),("Cifra di rumore","metodo Y-factor"),("Sonde near-field","caccia al QRM"),
("Misure di campo","dBµV/m con un'antenna"),("Ascoltare","demodulare e riconoscere"),("Slope detection","vedere la FM in zero span"),("Il trucco della RBW","CW, rumore o impulsi?"),("Più dinamica","notch, filtri, preamplificatori")]
D.add("Cosa c'è in questo modulo",'<div class="grid3">'+"".join(f'<div class="card"><h3>{a}</h3><p>{b}</p></div>' for a,b in cards)+'</div>')
D.add("La riga è vera? Il test dell'attenuazione",f'''<div class="fig" style="width:88%;margin:-10px auto 0">{svg("atttest.svg")}</div><div class="two" style="align-items:start;gap:30px"><div><ul class="small">
<li>Aumenta l'attenuazione interna di 10 dB: i segnali veri <b>restano fermi</b> (lo strumento compensa), il rumore sale di 10 dB.</li>
<li>Una 2ª armonica generata nel mixer cala di 10 dB, una 3ª o un IM3 interni di 20 dB.</li></ul></div><div><ul class="small">
<li>Se il livello cambia, la riga (o una sua parte) è <b>prodotta dall'analizzatore</b>: lavora con più attenuazione o con un filtro esterno.</li></ul></div></div>''')
D.add("Altri tre test per le righe sospette",'''<div class="two"><div><h3>Sposta la frequenza centrale</h3><ul class="small">
<li>Un segnale vero resta alla sua frequenza. Un'<b>immagine</b> o una risposta su un'armonica del LO si sposta in modo "strano" o sparisce.</li></ul>
<h3>Cambia la RBW</h3><ul class="small"><li>Una portante resta allo stesso livello. Se si sposta o cambia forma in modo anomalo, può essere una spuria del sintetizzatore interno.</li></ul></div><div>
<h3>Togli il segnale</h3><ul class="small"><li>Chiudi l'ingresso su 50 Ω con le stesse impostazioni: le righe che restano sono <b>spurie interne</b> (o arrivano dall'alimentazione e dai cavi). Annotale: sono la "firma" del tuo strumento.</li></ul>
<h3>Filtra l'ingresso</h3><ul class="small"><li>Un forte segnale fuori span (broadcast FM, un ripetitore vicino) può creare prodotti ovunque. Un filtro passa-banda sulla banda d'interesse fa sparire i prodotti, ma non i segnali veri.</li></ul></div></div>''')
D.add("Misurare vicino al rumore di fondo",f'''<div class="two"><div class="fig">{svg("noisecorr.svg")}</div><div>
<ul class="small"><li>Quando un segnale è vicino al rumore, l'analizzatore mostra la <b>somma</b> delle due potenze: il segnale sembra più forte di quanto sia.</li>
<li>Misura il rumore da solo (Δ è la differenza tra lettura con segnale e senza) e correggi:</li></ul>
{eq("correzione = −10·log(1 − 10<sup>−Δ/10</sup>)")}
<table><tr><th>Δ</th><th>Da sottrarre</th></tr><tr><td class="l">3 dB</td><td>3,0 dB</td></tr><tr><td class="l">6 dB</td><td>1,3 dB</td></tr><tr><td class="l">10 dB</td><td>0,46 dB</td></tr><tr><td class="l">20 dB</td><td>0,04 dB</td></tr></table>
<p class="note">Per abbassare il rumore: RBW più stretta, attenuazione minima (con prudenza), preamplificatore, media su più sweep con rivelatore sample o RMS.</p></div></div>''')
D.add("Cifra di rumore con il metodo Y-factor",'''<div class="two"><div><ul>
<li>Serve una <b>sorgente di rumore</b> calibrata, con un suo <b>ENR</b> (excess noise ratio) in dB.</li>
<li>Sorgente → DUT (preamplificatore, LNA) → analizzatore con preamplificatore. Misura la potenza di rumore con la sorgente accesa e spenta: il rapporto lineare è <b>Y</b>.</li></ul>
<div class="eq">NF = ENR − 10·log(Y − 1)</div>
<p class="note">Esempio: ENR 15 dB e Y = 10 dB (cioè 10 volte) → NF = 15 − 10·log(9) = 5,5 dB. È la cifra dell'intera catena: DUT + analizzatore.</p></div><div>
<h3>Togliere il contributo dell'analizzatore</h3>
<div class="eq">F<sub>DUT</sub> = F<sub>tot</sub> − (F<sub>SA</sub> − 1) / G<sub>DUT</sub></div>
<ul class="small"><li>F e G lineari: misura prima l'analizzatore da solo (stessa procedura senza DUT) per avere F<sub>SA</sub>.</li>
<li>Funziona bene se il guadagno del DUT è alto e il preamplificatore dell'analizzatore abbassa F<sub>SA</sub>.</li>
<li>Rivelatore RMS, RBW larga (centinaia di kHz–MHz), molta media: si misura rumore, non righe.</li>
<li>Senza sorgente di rumore: con un DUT ad alto guadagno, NF ≈ N<sub>out</sub>(dBm/Hz) + 174 − G (dB).</li></ul></div></div>''')
D.add("Sonde di campo vicino: caccia al QRM",'''<div class="two"><div><ul>
<li>Una <b>sonda magnetica</b> è una spira di semirigido da 1–2 cm, con la calza interrotta al centro della spira. Una <b>sonda elettrica</b> è un breve spezzone di centrale scoperto.</li>
<li>Collegata all'analizzatore (meglio con un preamplificatore), "annusa" i campi a pochi millimetri dai circuiti.</li>
<li>Muovendola trovi il punto da cui nasce il disturbo: induttore di uno switching, pista di clock, cavo che irradia.</li></ul></div><div>
<h3>Per il radioamatore</h3><ul class="small"><li>Trovare quale alimentatore, caricabatterie, LED o router disturba la ricezione in HF.</li>
<li>Usa <b>max hold</b> mentre muovi la sonda e confronta prima e dopo ferriti e filtri.</li>
<li>In zero span, con la demodulazione audio, spesso <b>senti</b> il "ronzio" caratteristico e confermi la sorgente.</li>
<li>La sonda non misura valori assoluti di campo, ma confronti: perfetta per prima e dopo.</li></ul></div></div>''')
D.add("Misure di campo con un'antenna",'''<div class="two"><div><ul>
<li>Con un'antenna dal <b>fattore d'antenna</b> (AF) noto, l'analizzatore diventa un misuratore di campo.</li></ul>
<div class="eq">E (dBµV/m) = V (dBµV) + AF (dB/m) + L<sub>cavo</sub> (dB)</div><div class="eq">V (dBµV) = P (dBm) + 107 &nbsp;(su 50 Ω)</div>
<p class="note">Esempio: −60 dBm letti, AF 20 dB/m, cavo 2 dB → 47 + 20 + 2 = 69 dBµV/m.</p></div><div>
<h3>Usi pratici</h3><ul class="small"><li>Verifica della copertura di un ripetitore o di un ponte radio.</li>
<li><b>Occupazione di banda</b>: max hold per ore, o una visualizzazione a cascata (waterfall), per vedere chi trasmette e quando.</li>
<li>Ricerca di interferenze: con un'antenna direttiva e il marker trovi la direzione del segnale.</li>
<li>Ricorda le protezioni: antenne esterne = scariche statiche e segnali forti fuori banda.</li></ul></div></div>''')
D.add("Ascoltare e riconoscere i segnali",'''<div class="two"><div><ul>
<li>Molti analizzatori hanno una <b>demodulazione audio</b> AM/FM: metti il marker sul segnale, vai in zero span e ascolta.</li>
<li>È il modo più rapido per identificare un disturbo: broadcast, ponte radio, dati digitali, ronzio di uno switching o arco elettrico.</li>
<li>In zero span con scala lineare vedi anche la forma dell'inviluppo, per esempio impulsi a 100 Hz legati alla rete.</li></ul></div><div>
<h3>Firme tipiche</h3><table><tr><th>Cosa vedi</th><th>Probabile sorgente</th></tr>
<tr><td class="l">righe a passo fisso di decine di kHz</td><td class="l">alimentatore switching</td></tr>
<tr><td class="l">"gobbe" larghe che si spostano</td><td class="l">switching a frequenza variabile, LED</td></tr>
<tr><td class="l">righe stabili a multipli esatti</td><td class="l">clock digitali, quarzi</td></tr>
<tr><td class="l">rumore a larga banda a impulsi</td><td class="l">archi, motori a spazzole, linee elettriche</td></tr></table></div></div>''')
D.add("Slope detection: vedere la FM in zero span",'''<div class="two"><div><ul>
<li>In zero span l'analizzatore rivela solo l'ampiezza: una FM sintonizzata al centro dà una linea piatta.</li>
<li><b>Il trucco</b>: sposta la frequenza di un po' (circa mezza RBW) da un lato del segnale. Ora sei sul fianco del filtro RBW, che trasforma le variazioni di frequenza in variazioni di ampiezza.</li>
<li>In zero span vedi la forma della modulazione FM, la deviazione relativa, i transitori di aggancio di un sintetizzatore o la deriva di un oscillatore.</li></ul></div><div>
<h3>Consigli</h3><ul class="small"><li>Scala lineare o 1–2 dB/div, RBW confrontabile con la deviazione da osservare.</li>
<li>È una misura qualitativa: per la deviazione esatta usa il nullo di Bessel (modulo precedente).</li>
<li>Ottimo per vedere quanto tempo impiega un TX a stabilizzarsi dopo il PTT: trigger video sul fronte del burst.</li></ul></div></div>''')
D.add("Il trucco della RBW: CW, rumore o impulsi?",'''<div class="two"><div><ul>
<li>Cambia la RBW di un fattore 10 e guarda come cambia il livello visualizzato:</li></ul>
<table><tr><th>Variazione</th><th>Il segnale è…</th></tr>
<tr><td class="l"><b>0 dB</b></td><td class="l">una portante (CW, riga stretta)</td></tr>
<tr><td class="l"><b>10 dB</b> (10·log)</td><td class="l">rumore o modulazione a larga banda</td></tr>
<tr><td class="l"><b>20 dB</b> (20·log)</td><td class="l">impulsivo (impulsi coerenti, archi)</td></tr></table></div><div><ul class="small">
<li>Funziona perché una riga ha tutta la potenza in un punto, il rumore distribuisce la potenza (proporzionale alla banda), gli impulsi la distribuiscono in modo coerente (tensione proporzionale alla banda).</li>
<li>Usalo per classificare un disturbo prima di cercarne la sorgente.</li>
<li>Per gli stessi motivi, il livello di un segnale digitale "letto con il marker" dipende dalla RBW: misuralo come potenza di canale.</li></ul></div></div>''')
D.add("Più dinamica e altri trucchi",'''<div class="two"><div><h3>Dinamica</h3><ul class="small">
<li><b>Notch o passa-alto</b> sulla fondamentale: le armoniche si misurano 30–40 dB più in basso.</li>
<li><b>Preamplificatore</b> esterno a basso rumore per segnali deboli, ma attenzione alla sua linearità.</li>
<li><b>Convertitore o mixer esterno</b> per frequenze oltre la gamma dello strumento.</li>
<li>Con tracking generator e ponte di return loss: SWR di antenne e filtri anche senza VNA.</li></ul></div><div>
<h3>Trucchi da banco</h3><ul class="small"><li><b>Riferimento esterno a 10 MHz</b> (GPSDO): frequenze precise e stabili per tutte le misure.</li>
<li><b>Linee limite</b> (limit lines) per controlli rapidi "passa/non passa" su filtri e armoniche.</li>
<li>Alimentazione a batteria (strumenti portatili) per eliminare ground loop e disturbi della rete dalla misura.</li>
<li>Salva tracce e schermate con impostazioni e offset: tra un mese non te li ricorderai.</li>
<li><b>Max hold notturno</b> sulla banda per catturare disturbi intermittenti.</li></ul></div></div>''')
rows=[("Test dell'attenuazione","una riga vera non cambia"),("Vicino al rumore","sottrai la correzione: 3 dB → −3 dB"),("Y-factor","NF = ENR − 10·log(Y − 1)"),("Sonde near-field","trovano la sorgente, confronti prima/dopo"),("Misure di campo","E = V + AF + cavo"),("Slope detection","fianco della RBW = discriminatore FM"),("Trucco della RBW","0 dB CW, 10 dB rumore, 20 dB impulsi")]
D.add("Riepilogo",'<table class="sum">'+"".join(f'<tr><td class="l" style="width:300px"><b>{a}</b></td><td class="l">{b}</td></tr>' for a,b in rows)+'</table>')
D.render(); pdf("SA_Misure_Inconsuete_Trucchi_IV3HGA.pdf")
