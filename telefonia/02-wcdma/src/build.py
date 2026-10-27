from deck import *
D=Deck("La telefonia cellulare:<br>WCDMA (UMTS)","Dal TDMA al CDMA: chip rate, codici di spreading e di scrambling, guadagno di processo, QPSK, ricevitore RAKE, controllo di potenza veloce, soft handover e uno sguardo a LTE","Telefonia · il WCDMA")
ovsf=f'''<svg viewBox="0 0 560 300" font-family="DejaVu Sans Mono" font-size="17">
<g stroke="{G}" stroke-width="2" fill="none"><path d="M70 150 L210 80"/><path d="M70 150 L210 220"/><path d="M290 80 L400 45"/><path d="M290 80 L400 115"/><path d="M290 220 L400 185"/><path d="M290 220 L400 255"/></g>
<g fill="{N}"><text x="20" y="155">(1)</text><text x="215" y="85">(1,1)</text><text x="215" y="225">(1,−1)</text>
<text x="405" y="50">(1,1,1,1)</text><text x="405" y="120">(1,1,−1,−1)</text><text x="405" y="190">(1,−1,1,−1)</text><text x="405" y="260">(1,−1,−1,1)</text></g>
<g font-family="DejaVu Sans" font-size="13" fill="#555"><text x="20" y="290">SF = 1</text><text x="215" y="290">SF = 2</text><text x="405" y="290">SF = 4 …</text></g></svg>'''
D.add("Dal GSM all'UMTS",'''<div class="two"><div><ul>
<li>Il GSM nasce per la voce. Per i dati veloci servivano più banda e più flessibilità: la terza generazione (UMTS) sceglie il <b>CDMA a banda larga</b>, il WCDMA.</li>
<li>Tutti gli utenti di una cella, e anche le celle vicine, usano la <b>stessa portante da 5 MHz</b>, distinti dai codici.</li></ul></div><div>
<h3>Le cifre (FDD, banda I)</h3><table><tr><td class="l">Uplink / downlink</td><td class="l">1920–1980 / 2110–2170 MHz</td></tr><tr><td class="l">Portanti</td><td class="l">5 MHz</td></tr>
<tr><td class="l">Chip rate</td><td class="l">3,84 Mchip/s</td></tr><tr><td class="l">Trama</td><td class="l">10 ms, 15 slot da 2560 chip</td></tr>
<tr><td class="l">Modulazione</td><td class="l">QPSK, coseno rialzato α = 0,22</td></tr><tr><td class="l">Voce</td><td class="l">codec AMR, 12,2 kbit/s massimo</td></tr></table></div></div>''')
D.add("Chip, spreading e scrambling",f'''<div class="two"><div class="diag" style="width:94%">{ovsf}</div><div><ul class="small">
<li>Ogni bit (o simbolo) viene moltiplicato per un codice di <b>spreading</b> di SF chip (spreading factor). I codici <b>OVSF</b> si costruiscono con l'albero a sinistra: codici dello stesso livello sono <b>ortogonali</b>, la loro somma "prodotto per prodotto" vale zero.</li>
<li>SF piccolo = pochi chip per bit = <b>più velocità</b>; SF grande = più robustezza (da 4 a 512).</li>
<li>Poi si applica un codice di <b>scrambling</b> (pseudo-casuale, lunghissimo): in downlink identifica la <b>cella</b>, in uplink il <b>telefono</b>.</li>
<li>Lo spettro occupato dipende solo dal chip rate: 3,84 × 1,22 ≈ 4,7 MHz, dentro il canale da 5 MHz.</li></ul></div></div>''')
D.add("Il guadagno di processo",f'''<div class="fig" style="width:96%">{svg("spread.svg")}</div><div class="two" style="align-items:start;gap:30px"><div>
{eq("G<sub>p</sub> = 10·log(chip rate / bit rate)")}<ul class="small"><li>Voce a 12,2 kbit/s: 10·log(3,84 M / 12,2 k) ≈ <b>25 dB</b>.</li></ul></div><div><ul class="small">
<li>Il segnale allargato può stare <b>sotto il rumore</b> e sotto gli altri utenti: dopo il despreading torna in alto, mentre rumore e interferenze restano sparsi. Grafico indicativo.</li></ul></div></div>''')
D.add("Il ricevitore RAKE",f'''<div class="two"><div class="fig">{svg("rake.svg")}</div><div><ul class="small">
<li>Un chip dura <b>0,26 µs</b>, circa 78 m di percorso: le copie del segnale che arrivano con ritardi diversi (multipath) si distinguono una dall'altra.</li>
<li>Il ricevitore RAKE ha più "dita" (finger): ognuna si sincronizza su una copia, ne corregge fase e ritardo, poi il ricevitore le somma.</li>
<li>Il multipath, che nel GSM era un problema da equalizzare, qui diventa una <b>risorsa</b>: più copie = più energia raccolta.</li>
<li>Il nome viene dal rastrello (rake), che raccoglie da più punti.</li></ul></div></div>''')
D.add("Controllo di potenza e soft handover",'''<div class="two"><div><h3>Controllo di potenza veloce</h3><ul class="small">
<li>Il problema vicino-lontano (capitolo sull'accesso multiplo) richiede che tutti arrivino alla stazione base con la potenza giusta.</li>
<li>La stazione base manda un comando "su" o "giù" (1 dB tipico) <b>1500 volte al secondo</b>, uno per slot.</li>
<li>Il telefono segue anche le evanescenze rapide: usa sempre la potenza minima indispensabile.</li></ul></div><div>
<h3>Soft handover</h3><ul class="small"><li>Le celle vicine usano la stessa frequenza: il telefono può essere collegato a <b>due o tre celle insieme</b>.</li>
<li>Il RAKE combina i segnali delle diverse celle come se fossero copie di multipath.</li>
<li>Il passaggio da una cella all'altra è graduale: niente interruzioni, niente "buchi" nella chiamata.</li>
<li>La capacità cala dolcemente con il traffico: più utenti alzano il "rumore" per tutti (respirazione della cella).</li></ul></div></div>''')
D.add("GSM, UMTS, LTE a confronto",'''<table><tr><th></th><th>GSM (2G)</th><th>UMTS / WCDMA (3G)</th><th>LTE (4G)</th></tr>
<tr><td class="l"><b>Accesso</b></td><td class="l">FDMA + TDMA</td><td class="l">CDMA</td><td class="l">OFDMA (downlink), SC-FDMA (uplink)</td></tr>
<tr><td class="l"><b>Larghezza del canale</b></td><td class="l">200 kHz</td><td class="l">5 MHz</td><td class="l">da 1,4 a 20 MHz</td></tr>
<tr><td class="l"><b>Modulazione</b></td><td class="l">GMSK</td><td class="l">QPSK (poi anche 16/64QAM)</td><td class="l">QPSK, 16QAM, 64QAM, 256QAM adattiva</td></tr>
<tr><td class="l"><b>Correzione d'errore</b></td><td class="l">convoluzionale (Viterbi)</td><td class="l">convoluzionale e turbo</td><td class="l">turbo (poi LDPC e polar nel 5G)</td></tr>
<tr><td class="l"><b>Contro il multipath</b></td><td class="l">equalizzatore</td><td class="l">ricevitore RAKE</td><td class="l">sottoportanti lente + prefisso ciclico</td></tr></table>
<p class="note" style="margin-top:14px">Ogni generazione usa gli stessi mattoni visti nel corso (costellazioni, filtri, accesso multiplo, correzione d'errore) combinati per avere più bit per hertz.</p>''')
rows=[("Portante","5 MHz, 3,84 Mchip/s, trama 10 ms"),("Codici","OVSF per i canali, scrambling per celle e telefoni"),("Guadagno","10·log(chip/bit): 25 dB per la voce"),("RAKE","il multipath diventa una risorsa"),("Potenza","1500 comandi al secondo"),("Handover","soft, con più celle insieme")]
D.add("Riepilogo",'<table class="sum">'+"".join(f'<tr><td class="l" style="width:160px"><b>{a}</b></td><td class="l">{b}</td></tr>' for a,b in rows)+'</table>')
D.render(); pdf("TEL_WCDMA_IV3HGA.pdf")
