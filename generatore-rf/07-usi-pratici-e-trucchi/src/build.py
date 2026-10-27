from deck import *
O="#e0563b"
D=Deck("Usi pratici<br>e trucchi","Tarare l'S-meter, allineare filtri e medie frequenze, iniezione di segnale stadio per stadio, prove su ricetrasmettitori senza distruggere il generatore, il generatore con l'analizzatore e altri trucchi da banco","Il generatore RF: usi pratici e trucchi")
trx=f'''<svg viewBox="0 0 980 230" font-family="DejaVu Sans">{ARW}
{box(10,70,170,70,"Ricetrasmettitore|in prova","#fff",14)}<path d="M180 105 H230" stroke="{N}" stroke-width="2.5"/>
{box(230,55,190,100,"Attenuatore di potenza|40 dB, 100 W|(o carico con prelievo)",L,13)}<path d="M420 105 H470" stroke="{N}" stroke-width="2.5"/>
{box(470,70,130,70,"Attenuatore|20–30 dB",L,13)}<path d="M600 105 H650" stroke="{N}" stroke-width="2.5"/>
{box(650,70,150,70,"Generatore RF",L,14)}
<text x="10" y="190" font-size="13" fill="{O}" font-weight="700">Se per errore trasmetti: 100 W − 40 dB − 30 dB = 10 µW al generatore.</text>
<text x="10" y="212" font-size="13" fill="#555">Il livello al RX è quello del generatore meno 60–70 dB: ok per la sensibilità, troppo poco per i test con segnali forti.</text></svg>'''
D.add("Tarare l'S-meter",'''<div class="two"><div><ul>
<li>Convenzione IARU: <b>S9 = −73 dBm</b> (50 µV) sotto i 30 MHz, <b>S9 = −93 dBm</b> (5 µV) sopra; <b>6 dB</b> per punto S.</li>
<li>Con il generatore leggi lo S-meter a vari livelli e costruisci una tabella "S letto → dBm vero".</li></ul>
<table><tr><th>Punto S</th><th>HF (dBm)</th><th>VHF/UHF (dBm)</th></tr>
<tr><td class="l">S9 + 20 dB</td><td>−53</td><td>−73</td></tr><tr><td class="l">S9</td><td>−73</td><td>−93</td></tr>
<tr><td class="l">S7</td><td>−85</td><td>−105</td></tr><tr><td class="l">S5</td><td>−97</td><td>−117</td></tr><tr><td class="l">S1</td><td>−121</td><td>−141</td></tr></table></div><div>
<h3>Cosa scopri</h3><ul class="small"><li>Pochi S-meter rispettano i 6 dB per punto: spesso sono compressi in basso e più larghi in alto.</li>
<li>Con il preamplificatore o l'attenuatore inseriti la lettura cambia: è un buon modo per misurarne il guadagno reale.</li>
<li>Con la tabella puoi dare rapporti di segnale "veri" e confrontare antenne con misure ripetibili.</li></ul></div></div>''')
D.add("Allineare filtri e medie frequenze",'''<div class="two"><div><ul>
<li>Il generatore inietta un segnale non modulato (o AM) alla frequenza di lavoro del filtro o della IF.</li>
<li>Come indicatore: lo S-meter, la tensione AGC (con un multimetro o un analogico), o l'audio con un voltmetro AC.</li>
<li>Regola i nuclei o i trimmer per il <b>massimo</b>, riducendo il livello del generatore man mano che il segnale cresce: l'AGC non deve intervenire, altrimenti "appiattisce" il massimo.</li></ul></div><div>
<h3>Trucchi</h3><ul class="small"><li>Per i filtri passa-banda a più stadi, regola alternando: prima per il massimo, poi spostando il generatore ai bordi per una risposta piatta.</li>
<li>Con un generatore con sweep e un rivelatore (o l'analizzatore con il tracking generator) vedi tutta la forma del filtro mentre lo tari.</li>
<li>Usa un cacciavite di taratura isolante: quelli metallici sintonizzano anch'essi.</li>
<li>Annota la posizione iniziale dei nuclei: se le cose peggiorano puoi tornare indietro.</li></ul></div></div>''')
D.add("Iniezione di segnale: ricerca guasti",'''<div class="two"><div><ul>
<li>Un ricevitore muto si ripara procedendo all'indietro: dall'altoparlante verso l'antenna.</li></ul><ol class="small">
<li>Audio: un tono a 1 kHz sull'ingresso dell'amplificatore audio.</li>
<li>Rivelatore: la IF modulata AM sull'ingresso del rivelatore.</li>
<li>Stadi IF: la IF sull'ingresso di ciascuno stadio, a livello via via più basso.</li>
<li>Mixer: la frequenza di ricezione sull'ingresso del mixer.</li>
<li>Ingresso RF: la frequenza di ricezione sul connettore d'antenna.</li></ol>
<p class="note">Dove il segnale smette di passare, hai trovato lo stadio guasto.</p></div><div>
<h3>Accorgimenti</h3><ul class="small"><li>Inietta tramite un condensatore da qualche nF: niente continua verso il generatore.</li>
<li>Livelli moderati (−60…−30 dBm): troppo segnale satura gli stadi e maschera i guasti.</li>
<li>Il generatore può anche <b>sostituire un oscillatore locale</b> guasto: se il ricevitore riprende a funzionare iniettando il LO dall'esterno, il guasto è nell'oscillatore.</li>
<li>Attenzione alla massa: collega la massa del generatore vicino al punto di iniezione.</li></ul></div></div>''')
D.add("Ricetrasmettitori: proteggere il generatore",f'''<div class="diag" style="width:92%;margin:-6px auto 0">{trx}</div><div class="two" style="align-items:start;gap:30px"><div><ul class="small">
<li>Il pericolo è un <b>PTT premuto per errore</b>: decine o centinaia di watt finiscono nell'uscita del generatore.</li>
<li>Soluzione: un attenuatore di <b>potenza</b> (o carico con prelievo) tra radio e generatore, dimensionato per tutta la potenza del TX.</li></ul></div><div><ul class="small">
<li>In alternativa un <b>commutatore</b> o un relè che isola il generatore quando il TX trasmette, o un accoppiatore direzionale con il generatore sulla porta accoppiata.</li>
<li>Abbassa la potenza del TX al minimo e, se possibile, disabilita la trasmissione durante le prove.</li></ul></div></div>''')
D.add("Generatore e analizzatore insieme",'''<div class="two"><div><ul>
<li><b>Risposta di un filtro</b> senza tracking generator: generatore in sweep lento, analizzatore in max hold. La traccia accumulata è la risposta del filtro.</li>
<li><b>Guadagno e compressione</b> di un amplificatore: generatore all'ingresso, analizzatore all'uscita (con attenuatori), livello d'ingresso crescente fino a 1 dB di compressione.</li>
<li><b>Test a due toni</b> su un amplificatore o un mixer: due generatori, combinatore, analizzatore all'uscita.</li></ul></div><div><ul>
<li><b>Verificare l'analizzatore</b> con il generatore (e viceversa): livello e frequenza a confronto, a più valori.</li>
<li><b>Riferimento comune a 10 MHz</b>: aggancia i due strumenti, così le frequenze coincidono esattamente e puoi usare RBW strettissime.</li>
<li>Misura di <b>perdite di cavi e attenuatori</b> a una frequenza: generatore → cavo → analizzatore, confronto con il collegamento diretto.</li></ul></div></div>''')
D.add("Altri trucchi da banco",'''<div class="two"><div><ul class="small">
<li><b>Prova di un'antenna in ricezione</b>: generatore con una piccola antenna a distanza fissa, confronta lo S-meter con due antenne diverse (solo indicativo, attento alle riflessioni dell'ambiente).</li>
<li><b>Battimento zero</b>: il generatore come riferimento per tarare la frequenza di un VFO o di un oscillatore a quarzo, ascoltando il battimento in un ricevitore.</li>
<li><b>Soglia dello squelch</b> e del CTCSS: livello minimo che apre lo squelch, tono che apre la radio.</li></ul></div><div><ul class="small">
<li><b>AGC</b>: S-meter e audio con il livello che sale da −120 a −20 dBm. Un buon AGC mantiene l'audio entro pochi dB per 100 dB d'ingresso.</li>
<li><b>Generatore come oscillatore</b> per un mixer o un convertitore autocostruito: verifica il livello giusto per il mixer (+7, +13, +17 dBm).</li>
<li><b>Fonte di marcatori</b>: in AM a impulsi stretti o con un'onda quadra produce un "pettine" di righe, utile per tarare la scala di vecchi ricevitori.</li></ul></div></div>''')
D.add("Errori da evitare",'''<div class="two"><div><ul>
<li>Trasmettere dentro il generatore (sempre attenuatore di potenza o commutatore).</li>
<li>Livelli alti senza filtrare armoniche e spurie nei test di selettività.</li>
<li>Dimenticare le perdite di cavi, attenuatori e combinatori.</li>
<li>Confondere EMF e PD nelle sensibilità.</li></ul></div><div><ul>
<li>Non verificare il leakage nei test di sensibilità.</li>
<li>AGC acceso mentre si tara "al massimo".</li>
<li>Generatore non scaldato: frequenza e livello derivano nei primi minuti.</li>
<li>Usare un modulo a onda quadra come se fosse un generatore sinusoidale tarato.</li></ul></div></div>''')
rows=[("S-meter","S9 = −73 dBm HF, −93 dBm VHF; 6 dB per punto"),("Allineamento","massimo con AGC fuori gioco, livello che scende"),("Iniezione","dall'audio verso l'antenna: dove si ferma, lì è il guasto"),("Ricetrasmettitori","attenuatore di potenza tra TX e generatore"),("Con l'analizzatore","sweep + max hold, compressione, 10 MHz comune")]
D.add("Riepilogo",'<table class="sum">'+"".join(f'<tr><td class="l" style="width:220px"><b>{a}</b></td><td class="l">{b}</td></tr>' for a,b in rows)+'</table>')
D.render(); pdf("GEN_Usi_Pratici_Trucchi_IV3HGA.pdf")
