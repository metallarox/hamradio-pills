import json
from deck import *
v=json.load(open("vals.json"))
D=Deck("Come funziona<br>l'analizzatore di spettro","Supereterodina a scansione, RBW e VBW, rivelatori, attenuatore, rumore e dinamica: cosa c'è dentro e perché conta","L'analizzatore di spettro: come funziona")
mix=f'<circle cx="420" cy="90" r="26" fill="#fff" stroke="{N}" stroke-width="2"/><path d="M402 72 L438 108 M438 72 L402 108" stroke="{N}" stroke-width="2"/>'
blk=f'''<svg viewBox="0 0 1000 380" font-family="DejaVu Sans">{ARW}
<circle cx="25" cy="90" r="9" fill="#fff" stroke="{N}" stroke-width="2"/><text x="25" y="55" text-anchor="middle" font-size="13" fill="{N}">RF in</text>
{ln(34,90,60,90)}{box(60,60,130,60,"Attenuatore|d'ingresso")}{ln(190,90,220,90)}{box(220,60,140,60,"Passa-basso /|preselettore")}{ln(360,90,394,90)}{mix}
{ln(446,90,480,90)}{box(480,60,150,60,"Filtro IF|(RBW)")}{ln(630,90,660,90)}{box(660,60,140,60,"Amplificatore|logaritmico")}{ln(800,90,830,90)}{box(830,60,150,60,"Rivelatore|d'inviluppo")}
{ln(905,120,905,255)}{box(830,255,150,60,"Filtro video|(VBW)")}{ln(830,285,790,285)}{box(620,255,170,60,"Rivelatore di|display + ADC")}{ln(620,285,570,285)}{box(380,240,190,90,"Display|(ampiezza vs f)",L,16)}
{box(355,160,130,55,"Oscillatore|locale (LO)")}{ln(420,160,420,118)}
{box(60,160,210,55,"Generatore di sweep|(rampa)")}{ln(270,187,355,187)}
<path d="M165 215 V285 H380" stroke="{N}" stroke-width="1.8" stroke-dasharray="5 4" fill="none" marker-end="url(#ar)"/>
<text x="185" y="305" font-size="12" fill="#666">asse orizzontale = frequenza</text>
<text x="555" y="150" font-size="13" fill="{C}" font-weight="700">f<tspan font-size="10" dy="3">IF</tspan><tspan dy="-3"> = f</tspan><tspan font-size="10" dy="3">LO</tspan><tspan dy="-3"> − f</tspan><tspan font-size="10" dy="3">in</tspan></text>
</svg>'''
D.add("Cos'è un analizzatore di spettro",'''<div class="two"><div><ul>
<li>Mostra la <b>potenza in funzione della frequenza</b>: ogni segnale presente all'ingresso diventa una "riga" alla sua frequenza.</li>
<li>L'oscilloscopio guarda il segnale nel <b>tempo</b>, l'analizzatore nella <b>frequenza</b>: armoniche, spurie e prodotti di intermodulazione nel tempo sono invisibili.</li>
<li>Misura solo l'<b>ampiezza</b> (è uno strumento scalare), ma con una dinamica enorme: segnali di +10 dBm e di −120 dBm sulla stessa schermata.</li></ul></div><div>
<h3>A cosa serve al radioamatore</h3><ul class="small"><li>Armoniche e spurie del trasmettitore</li><li>Intermodulazione di amplificatori e ricevitori</li>
<li>Deviazione FM e profondità di modulazione AM</li><li>Caccia ai disturbi (QRM) di alimentatori e LED</li>
<li>Con un tracking generator: risposta di filtri, duplexer e cavità</li><li>Occupazione di banda e potenza di canale</li></ul></div></div>''')
D.add("Le unità di misura",f'''<div class="two"><div><table><tr><th>Unità</th><th>Significato</th></tr>
<tr><td class="l"><b>dBm</b></td><td class="l">potenza rispetto a 1 mW: 0 dBm = 1 mW, +30 dBm = 1 W, +50 dBm = 100 W</td></tr>
<tr><td class="l"><b>dBµV</b></td><td class="l">tensione rispetto a 1 µV; su 50 Ω vale dBµV = dBm + 107</td></tr>
<tr><td class="l"><b>dBc</b></td><td class="l">livello rispetto alla portante (armoniche, spurie, bande laterali)</td></tr>
<tr><td class="l"><b>dBm/Hz</b></td><td class="l">densità di rumore, cioè potenza in 1 Hz di banda</td></tr></table></div><div>
<h3>Riferimenti utili</h3><table><tr><th>Livello</th><th>Equivale a</th></tr>
<tr><td class="l">0 dBm</td><td class="l">0,224 V efficaci su 50 Ω</td></tr><tr><td class="l">−107 dBm</td><td class="l">1 µV su 50 Ω</td></tr>
<tr><td class="l">−73 dBm</td><td class="l">S9 in HF (50 µV)</td></tr><tr><td class="l">−93 dBm</td><td class="l">S9 in VHF/UHF (5 µV)</td></tr>
<tr><td class="l">−174 dBm/Hz</td><td class="l">rumore termico a 290 K</td></tr></table>
<p class="note">Ogni 3 dB la potenza raddoppia, ogni 10 dB si moltiplica per 10, ogni 6 dB raddoppia la tensione.</p></div></div>''')
D.add("Architettura: la supereterodina a scansione",f'<div class="diag" style="width:94%;margin:auto">{blk}</div>'+'''<div class="grid3" style="margin-top:0">
<div class="card"><h3>Mixer + LO</h3><p>L'oscillatore locale spazzola la frequenza: a ogni istante solo il segnale che cade a f<sub>IF</sub> passa.</p></div>
<div class="card"><h3>Filtro IF = RBW</h3><p>La sua larghezza è la "risoluzione": decide quanto vicini possono stare due segnali per essere distinti.</p></div>
<div class="card"><h3>Log + rivelatori</h3><p>Il logaritmico comprime la dinamica in dB, i rivelatori trasformano l'IF in un punto sul display.</p></div></div>''')
D.add("Conversione e frequenze immagine",'''<div class="two"><div><ul>
<li>Il mixer produce f<sub>LO</sub> − f<sub>in</sub> e f<sub>LO</sub> + f<sub>in</sub>. Con f<sub>IF</sub> = f<sub>LO</sub> − f<sub>in</sub>, anche un segnale a <b>f<sub>LO</sub> + f<sub>IF</sub></b> cade nell'IF: è la <b>frequenza immagine</b>.</li>
<li>Gli analizzatori classici usano una <b>prima IF molto alta</b>, sopra la massima frequenza d'ingresso: l'immagine finisce lontanissimo e un semplice passa-basso all'ingresso la elimina.</li>
<li>Per salire in frequenza si usano le <b>armoniche del LO</b>: servono un <b>preselettore</b> (filtro passa-banda che segue lo sweep) o la soppressione software delle immagini.</li></ul></div><div>
<h3>Cosa significa in pratica</h3><ul class="small"><li>Negli analizzatori economici o a bassa IF possono comparire <b>righe fantasma</b>: immagini, risposte su armoniche del LO, spurie interne.</li>
<li>Un segnale vero non cambia frequenza se sposti un po' la frequenza centrale; un'immagine sì, oppure scompare.</li>
<li>Anche segnali <b>fuori dallo span</b> che stai guardando arrivano al mixer: un forte broadcast FM può creare spurie o saturare, anche se non è sullo schermo.</li></ul>
<p class="note">Questi controlli sono spiegati in dettaglio nel modulo "Misure inconsuete e trucchi".</p></div></div>''')
D.add("RBW: la risoluzione",f'''<div class="fig" style="width:92%">{svg("rbw.svg")}</div><div class="two" style="align-items:start;gap:30px"><div>
{eq("rumore visualizzato ∝ 10·log(RBW)")}{eq("tempo di sweep ≈ k · span / RBW²")}</div><div><p class="note" style="margin-top:2px">Con RBW 30 kHz il segnale a −45 dBm, 10 kHz accanto alla portante, è nascosto nella sua "gonna". Con 1 kHz è ben separato e il rumore scende di 15 dB (10·log 30). Il prezzo è il tempo: dividere RBW per 10 rende lo sweep circa 100 volte più lento (k ≈ 2–3 per filtri analogici).</p></div></div>''')
D.add("VBW e rivelatori",'''<div class="two"><div><h3>Filtro video (VBW)</h3><ul class="small">
<li>È un passa-basso dopo il rivelatore: <b>media</b> le fluttuazioni del rumore e rende la traccia più liscia.</li>
<li>Non cambia la risoluzione né l'ampiezza dei segnali continui, ma rallenta lo sweep se più stretto della RBW.</li>
<li>Regola pratica: VBW = RBW per uso generale, VBW ≤ RBW/10 per leggere segnali vicini al rumore.</li></ul></div><div>
<h3>Rivelatori di display</h3><table><tr><th>Rivelatore</th><th>Uso tipico</th></tr>
<tr><td class="l"><b>Peak</b></td><td class="l">segnali continui, nessun segnale perso tra i punti</td></tr>
<tr><td class="l"><b>Sample</b></td><td class="l">rumore e misure statistiche</td></tr>
<tr><td class="l"><b>Neg. peak</b></td><td class="l">vedere segnali dentro il rumore impulsivo</td></tr>
<tr><td class="l"><b>RMS / average</b></td><td class="l">potenza di canale, segnali digitali, rumore</td></tr></table>
<p class="note">Attenzione: il rumore mediato in scala logaritmica si legge circa <b>2,5 dB più basso</b> del vero. I marker di rumore degli strumenti moderni correggono già questo errore.</p></div></div>''')
D.add("Attenuatore d'ingresso e livello al mixer",f'''<div class="two"><div class="fig">{svg("dynrange.svg")}</div><div><ul class="small">
<li>L'attenuatore protegge il mixer e decide il <b>livello al mixer</b> = livello d'ingresso − attenuazione.</li>
<li>Più attenuazione: il rumore visualizzato sale 1 dB per dB, ma le distorsioni interne calano (2ª armonica 1 dB per dB, intermodulazione del 3° ordine 2 dB per dB, in dBc).</li>
<li>Il punto ottimo è all'incrocio: con TOI +10 dBm e rumore −130 dBm (RBW 1 kHz) la dinamica libera da IM3 è circa <b>{v["d3"]:.0f} dB</b> con {v["p3"]:.0f} dBm al mixer.</li>
<li>Lo strumento mantiene costante il livello di riferimento: cambiando attenuazione i segnali veri restano fermi, si muove solo il rumore.</li></ul>
<p class="note">Valori di esempio, non di uno strumento specifico: usa quelli del tuo manuale (DANL, TOI, SHI).</p></div></div>''')
D.add("Rumore, rumore di fase e dinamica",'''<div class="two"><div><h3>DANL</h3><ul class="small">
<li>Il <b>Displayed Average Noise Level</b> è il rumore proprio dello strumento, di solito dato a RBW 1 Hz o normalizzato in dBm/Hz.</li>
<li>Lo abbassano una RBW più stretta, meno attenuazione e un <b>preamplificatore</b> interno (che però peggiora la distorsione).</li></ul>
<h3>Rumore di fase</h3><ul class="small"><li>Il LO non è perfetto: la sua "gonna" di rumore si sovrappone a ogni segnale forte.</li>
<li>Limita la misura di segnali deboli <b>vicini</b> a uno forte, e il rumore di fase dei tuoi oscillatori: non puoi misurare meglio di quello dell'analizzatore.</li></ul></div><div>
<h3>Le "dinamiche"</h3><table><tr><th>Limitata da</th><th>Conta per</th></tr>
<tr><td class="l">DANL e compressione</td><td class="l">segnali lontani tra loro in frequenza</td></tr>
<tr><td class="l">DANL e distorsione (SHI, TOI)</td><td class="l">armoniche e intermodulazione</td></tr>
<tr><td class="l">Rumore di fase</td><td class="l">segnali vicini alla portante</td></tr>
<tr><td class="l">Spurie interne</td><td class="l">ricerca di segnali molto deboli</td></tr></table>
<p class="note">Il numero "dinamica 100 dB" sul depliant vale in condizioni precise: chiediti sempre "limitata da cosa?".</p></div></div>''')
D.add("Analizzatori FFT, real-time e SDR",'''<div class="two"><div><ul>
<li>Gli strumenti moderni <b>campionano l'IF con un ADC</b> e calcolano lo spettro con la FFT. Per RBW strette sono molto più veloci dello sweep analogico.</li>
<li>Gli analizzatori <b>real-time</b> elaborano senza buchi: catturano anche impulsi brevissimi. Le visualizzazioni a <b>persistenza</b> mostrano quanto spesso compare un segnale.</li>
<li>Gli analizzatori economici e gli SDR usano gli stessi principi, con compromessi su dinamica, immagini e spurie.</li></ul></div><div>
<h3>Cosa cambia per te</h3><ul class="small"><li>Con la FFT la RBW stretta non è più "proibitiva": usala.</li>
<li>Segnali intermittenti (burst TDMA, telecomandi, disturbi impulsivi) si vedono bene con max hold, persistenza o real-time; con uno sweep lento possono sfuggire.</li>
<li>Su strumenti economici controlla sempre se una riga è vera (vedi il modulo sui trucchi).</li></ul></div></div>''')
D.add("Tracking generator",'''<div class="two"><div><ul>
<li>È un generatore che segue esattamente la frequenza su cui l'analizzatore è sintonizzato in quel momento.</li>
<li>Collegandolo all'ingresso di un DUT e l'uscita del DUT all'analizzatore ottieni la <b>risposta in frequenza</b> (|S21|): filtri, amplificatori, cavi, duplexer.</li>
<li>Con un ponte di return loss misuri anche |S11|, cioè l'SWR.</li></ul></div><div>
<h3>Rispetto a un VNA</h3><ul class="small"><li>È <b>scalare</b>: niente fase, quindi niente carta di Smith e correzione degli errori limitata (normalizzazione).</li>
<li>Ha spesso <b>più dinamica</b> di un VNA economico: utile per la reiezione di duplexer e filtri a cavità.</li>
<li>La normalizzazione (thru di riferimento) toglie la risposta di cavi e strumento.</li></ul></div></div>''')
D.add("Le specifiche che contano",'''<div class="two"><div><ul>
<li><b>Gamma di frequenza</b>, e se sopra una certa soglia passa a mixing armonico.</li>
<li><b>DANL</b> (con e senza preamplificatore) e RBW minima.</li>
<li><b>Rumore di fase</b> a 10 kHz e 100 kHz dalla portante.</li>
<li><b>TOI e SHI</b>: quanto distorce lo strumento stesso.</li></ul></div><div><ul>
<li><b>Massima potenza d'ingresso</b> e <b>massima tensione continua</b>: le specifiche che salvano lo strumento.</li>
<li><b>Precisione di ampiezza</b> e piattezza.</li>
<li><b>Rivelatori</b> disponibili (RMS!), marker di rumore e potenza di canale.</li>
<li>Tracking generator, zero span, demodulazione audio, persistenza.</li></ul></div></div>''')
rows=[("Supereterodina","il LO spazzola, il filtro IF seleziona"),("RBW","risoluzione e rumore: 10× più stretta = −10 dB di rumore, 100× più lenta"),("VBW","liscia la traccia, non cambia la risoluzione"),
("Rivelatore","peak per CW, RMS per potenza di canale e rumore"),("Attenuatore","+10 dB: rumore +10 dB, distorsione interna giù"),("Immagini","righe fantasma: verifica sempre"),("Rumore di fase","limita le misure vicine alla portante")]
D.add("Riepilogo",'<table class="sum">'+"".join(f'<tr><td class="l" style="width:240px"><b>{a}</b></td><td class="l">{b}</td></tr>' for a,b in rows)+'</table>')
D.render(); pdf("SA_Come_Funziona_IV3HGA.pdf")
