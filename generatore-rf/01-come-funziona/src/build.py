from deck import *
D=Deck("Il generatore di segnali RF:<br>come funziona","A cosa serve, l'architettura a blocchi, sintetizzatori PLL e DDS, riferimento di frequenza, ALC, attenuatore d'uscita e protezione, tipi di generatori e specifiche","Il generatore RF: come funziona")
blk=f'''<svg viewBox="0 0 1150 300" font-family="DejaVu Sans">{ARW}
{box(10,40,150,70,"Riferimento|TCXO / OCXO",L,14)}<text x="20" y="135" font-size="12" fill="#555">ingresso/uscita 10 MHz</text>
{ln(160,75,195,75)}{box(195,40,170,70,"Sintetizzatore|PLL / DDS",L,14)}{ln(365,75,400,75)}{box(400,40,140,70,"Modulatore|AM / FM / ΦM",L,14)}{ln(540,75,575,75)}
{box(575,40,150,70,"Amplificatore|di uscita",L,14)}{ln(725,75,760,75)}{box(760,40,160,70,"Attenuatore|a scatti (0–130 dB)",L,14)}{ln(920,75,955,75)}{box(955,40,150,70,"Protezione|potenza inversa",L,14)}
<circle cx="1125" cy="75" r="9" fill="#fff" stroke="{N}" stroke-width="2"/><text x="1112" y="30" text-anchor="middle" font-size="12" fill="{N}">RF out</text>
{box(575,180,150,60,"Rivelatore|e ALC",L,14)}<path d="M690 110 V180" stroke="{C}" stroke-width="2" fill="none" marker-end="url(#ac)"/><path d="M610 180 V110" stroke="{C}" stroke-width="2" fill="none" marker-end="url(#ac)"/>
<text x="740" y="215" font-size="12" fill="{C}">anello di controllo del livello</text>
{box(400,180,140,60,"Sorgente|di modulazione",L,13)}{ln(470,180,470,110)}<text x="300" y="275" font-size="12" fill="#555">interna (1 kHz, rumore…) o esterna (audio, I/Q)</text></svg>'''
cards=[("Sensibilità dei ricevitori","SINAD, MDS, S/N"),("Selettività e dinamica","canale adiacente, blocking, IMD"),("Taratura","filtri, medie frequenze, S-meter"),("Iniezione di segnale","ricerca guasti stadio per stadio"),
("Prova di amplificatori","guadagno, compressione, con l'analizzatore"),("Sostituto di oscillatori","LO, BFO, clock"),("Con l'analizzatore","risposta di filtri, sweep"),("Ripetitori e ponti","verifica della catena RX"),("Modulazioni","AM, FM, impulsi, segnali digitali")]
D.add("A cosa serve",'<div class="grid3">'+"".join(f'<div class="card"><h3>{a}</h3><p>{b}</p></div>' for a,b in cards)+'</div><p class="note" style="margin-top:16px">È il "contrario" dell\'analizzatore di spettro: invece di misurare un segnale, ne crea uno <b>noto</b> per frequenza, livello e modulazione.</p>')
D.add("Architettura a blocchi",f'<div class="diag" style="width:96%">{blk}</div>'+'''<div class="grid3" style="margin-top:6px">
<div class="card"><h3>Frequenza</h3><p>Il riferimento dà la precisione, il sintetizzatore genera la frequenza voluta con passi fini.</p></div>
<div class="card"><h3>Livello</h3><p>Amplificatore con ALC per un livello stabile, poi un attenuatore di precisione per scendere fino a −130 dBm e oltre.</p></div>
<div class="card"><h3>Modulazione</h3><p>Interna o esterna, applicata alla frequenza (FM, ΦM) o all'ampiezza (AM, impulsi).</p></div></div>''')
D.add("Sintetizzatori: PLL e DDS",'''<div class="two"><div><h3>PLL</h3><ul class="small">
<li>Un oscillatore controllato in tensione (VCO) viene agganciato al riferimento tramite divisori e un comparatore di fase.</li>
<li>Copre gamme ampie (fino a GHz) con un buon rumore di fase lontano dalla portante.</li>
<li>Il rumore vicino alla portante e le spurie dipendono dal progetto dell'anello; i cambi di frequenza richiedono qualche ms.</li></ul>
<h3>DDS (sintesi digitale diretta)</h3><ul class="small"><li>Un convertitore digitale-analogico ricostruisce una sinusoide da una tabella, con risoluzione di frazioni di Hz e cambi di frequenza istantanei.</li>
<li>Frequenza massima utile intorno al 40 % del clock; produce <b>immagini</b> e spurie che vanno filtrate.</li></ul></div><div>
<h3>Nella pratica</h3><ul class="small"><li>I generatori moderni combinano le due tecniche: DDS per la risoluzione fine, PLL per salire in frequenza.</li>
<li>I vecchi generatori a cavità e a LC (con la manopola) hanno spesso un rumore di fase eccellente ma frequenza meno stabile: per la stabilità si agganciano a un contatore o a un riferimento.</li>
<li>I moduli economici (sintetizzatori PLL su schedina, generatori di clock) producono spesso un'<b>onda quadra</b>: ricca di armoniche, va filtrata prima di usarla per test seri.</li></ul></div></div>''')
D.add("Il riferimento di frequenza",'''<div class="two"><div><ul>
<li>La precisione della frequenza è quella del <b>riferimento</b>: un quarzo compensato in temperatura (TCXO) o in forno (OCXO).</li></ul>
<div class="eq">errore (Hz) = errore (ppm) × frequenza (MHz)</div>
<ul class="small"><li>Esempio: 1 ppm a 432 MHz = <b>432 Hz</b>; in SSB o nei modi digitali stretti si sente e si vede.</li>
<li>Gli oscillatori invecchiano: dopo anni un OCXO può essere fuori di qualche decimo di ppm.</li></ul></div><div>
<h3>Ingresso e uscita a 10 MHz</h3><ul class="small"><li>Quasi tutti i generatori hanno un ingresso <b>REF IN</b>: collegandolo a un riferimento migliore (GPSDO) la precisione diventa quella del GPS.</li>
<li>L'uscita <b>REF OUT</b> permette di agganciare tra loro generatore, analizzatore e frequenzimetro: tutto il banco "parla" con lo stesso orologio e le misure relative diventano esatte.</li>
<li>Lascia scaldare l'OCXO (anche mezz'ora) prima delle misure di frequenza.</li></ul></div></div>''')
D.add("ALC, attenuatore e protezione",'''<div class="two"><div><h3>ALC</h3><ul class="small">
<li>Un rivelatore misura il livello in uscita dall'amplificatore e un anello lo corregge: il livello resta piatto in frequenza e nel tempo.</li>
<li>Con modulazioni d'ampiezza veloci o impulsi l'ALC va spesso disattivato o messo in modalità "hold", altrimenti cerca di correggere la modulazione stessa.</li></ul>
<h3>Attenuatore d'uscita</h3><ul class="small"><li>Una catena di attenuatori di precisione (meccanici o elettronici) porta il livello fino a −130 dBm e oltre.</li>
<li>Quelli meccanici "scattano" cambiando livello: durante il cambio l'uscita può avere un breve transitorio.</li></ul></div><div>
<h3>Protezione dalla potenza inversa</h3><ul class="small"><li>Molti generatori hanno una protezione (relè o fusibile) che scatta se all'uscita arriva potenza dall'esterno, tipicamente fino a qualche decina di watt.</li>
<li>È una protezione d'emergenza, non un permesso: trasmettere dentro il generatore lo danneggia comunque se la potenza supera il limite o la protezione è lenta.</li>
<li>Nei test su ricetrasmettitori usa sempre un attenuatore di potenza o un commutatore che isoli il generatore durante la trasmissione (lezione sugli usi pratici).</li></ul></div></div>''')
D.add("Tipi di generatori",'''<table><tr><th>Tipo</th><th>Pregi</th><th>Limiti</th></tr>
<tr><td class="l"><b>Analogici a cavità / LC</b> (classici da laboratorio, molto diffusi nel surplus)</td><td class="l">rumore di fase spesso eccellente, modulazioni pulite</td><td class="l">deriva di frequenza, regolazione meno comoda</td></tr>
<tr><td class="l"><b>Sintetizzati</b> (PLL)</td><td class="l">frequenza precisa, livelli tarati, memorie, controllo remoto</td><td class="l">rumore di fase variabile da modello a modello, spurie</td></tr>
<tr><td class="l"><b>Vettoriali</b> (I/Q)</td><td class="l">qualsiasi modulazione digitale, anche standard professionali</td><td class="l">costo, complessità</td></tr>
<tr><td class="l"><b>Moduli economici</b> (schedine PLL, generatori di clock)</td><td class="l">costo bassissimo, gamma ampia</td><td class="l">onda quadra, livello poco preciso, niente attenuatore tarato, perdite</td></tr>
<tr><td class="l"><b>SDR in trasmissione</b></td><td class="l">flessibilità totale</td><td class="l">livello e purezza da verificare con l'analizzatore</td></tr></table>''')
D.add("Le specifiche che contano",'''<div class="two"><div><ul>
<li><b>Gamma di frequenza</b> e risoluzione.</li>
<li><b>Gamma di livello</b> (per esempio da −137 a +13 dBm) e <b>precisione</b> del livello, specialmente ai livelli bassi.</li>
<li><b>Rumore di fase</b> a 10–20 kHz dalla portante: decide se puoi misurare la selettività e la dinamica di un buon ricevitore.</li>
<li><b>Armoniche</b> e <b>spurie</b> non armoniche, in dBc.</li></ul></div><div><ul>
<li><b>Perdite (leakage)</b>: quanto segnale esce dal contenitore e dai cavi, fondamentale per i test di sensibilità.</li>
<li><b>Modulazioni</b>: tipi, deviazione massima, distorsione, FM residua.</li>
<li><b>SWR d'uscita</b> e protezione dalla potenza inversa.</li>
<li>Riferimento interno e ingresso 10 MHz, controllo remoto (GPIB, LAN, USB).</li></ul></div></div>''')
rows=[("Architettura","riferimento → sintetizzatore → modulatore → ALC → attenuatore"),("PLL e DDS","gamma e rumore contro risoluzione e velocità"),("Riferimento","errore in Hz = ppm × MHz; aggancia tutto a 10 MHz"),("ALC","livello stabile; attenzione con AM e impulsi"),("Protezione","d'emergenza: mai trasmettere nel generatore")]
D.add("Riepilogo",'<table class="sum">'+"".join(f'<tr><td class="l" style="width:200px"><b>{a}</b></td><td class="l">{b}</td></tr>' for a,b in rows)+'</table>')
D.render(); pdf("GEN_Come_Funziona_IV3HGA.pdf")
