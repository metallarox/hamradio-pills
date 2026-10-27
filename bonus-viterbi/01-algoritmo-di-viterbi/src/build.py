import json
from deck import *
v=json.load(open("vals.json"))
D=Deck("Bonus: l'algoritmo<br>di Viterbi","Come un ricevitore ricostruisce i bit giusti anche quando ne arrivano di sbagliati: codifica convoluzionale, stati e traliccio, percorsi sopravvissuti, un esempio passo per passo e dove si usa","Bonus · l'algoritmo di Viterbi")
reg=f'''<svg viewBox="0 0 760 270" font-family="DejaVu Sans">{ARW}
<text x="10" y="140" font-size="15" fill="{N}">bit u</text>{ln(60,135,110,135)}
<rect x="110" y="110" width="80" height="50" rx="6" fill="#fff" stroke="{N}" stroke-width="2"/><text x="150" y="141" text-anchor="middle" font-size="16" fill="{N}">u</text>
{ln(190,135,250,135)}<rect x="250" y="110" width="80" height="50" rx="6" fill="{L}" stroke="{N}" stroke-width="2"/><text x="290" y="141" text-anchor="middle" font-size="16" fill="{N}">s1</text>
{ln(330,135,390,135)}<rect x="390" y="110" width="80" height="50" rx="6" fill="{L}" stroke="{N}" stroke-width="2"/><text x="430" y="141" text-anchor="middle" font-size="16" fill="{N}">s0</text>
<circle cx="600" cy="50" r="22" fill="#fff" stroke="{C}" stroke-width="2.5"/><text x="600" y="57" text-anchor="middle" font-size="20" fill="{C}">⊕</text>
<circle cx="600" cy="220" r="22" fill="#fff" stroke="{O if False else C}" stroke-width="2.5"/><text x="600" y="227" text-anchor="middle" font-size="20" fill="{C}">⊕</text>
<g stroke="{C}" stroke-width="2" fill="none"><path d="M150 110 V50 H578"/><path d="M290 110 V50"/><path d="M430 110 V50"/><path d="M150 160 V220 H578"/><path d="M430 160 V220"/></g>
{ln(622,50,690,50,C)}{ln(622,220,690,220,C)}<text x="695" y="55" font-size="15" fill="{N}">c1</text><text x="695" y="225" font-size="15" fill="{N}">c2</text>
<text x="250" y="200" font-size="13" fill="#555">memoria: gli ultimi 2 bit = 4 stati</text></svg>'''
D.add("Il problema",'''<div class="two"><div><ul>
<li>Lungo il percorso radio qualche bit si rovina: rumore, evanescenze, interferenze.</li>
<li>Se trasmettiamo bit "nudi", un errore è irrimediabile. Se invece aggiungiamo <b>ridondanza</b> in modo intelligente, il ricevitore può capire qual era il messaggio più probabile.</li>
<li>È come il correttore del telefono: da "cssa" capisce "casa", perché sa quali parole esistono e quali sono "vicine".</li></ul></div><div>
<h3>L'idea di Viterbi</h3><ul class="small"><li>Andrew Viterbi, nel 1967, trova un modo efficiente di fare questa "correzione" per i codici convoluzionali.</li>
<li>Invece di confrontare il segnale con <b>tutti</b> i messaggi possibili (che crescono in modo esplosivo), a ogni passo tiene solo i candidati migliori.</li>
<li>Lo troviamo nel GSM, nei satelliti, nel Wi-Fi, nei modem, nei ricevitori GPS e in molti altri posti.</li></ul></div></div>''')
D.add("La codifica convoluzionale",f'''<div class="two" style="grid-template-columns:1.3fr 1fr"><div class="diag">{reg}</div><div><ul class="small">
<li>Un piccolo registro ricorda gli ultimi 2 bit (s1, s0). Per ogni nuovo bit u escono <b>due</b> bit:</li></ul>
<div class="eq">c1 = u ⊕ s1 ⊕ s0 &nbsp;&nbsp; c2 = u ⊕ s0</div>
<ul class="small"><li>⊕ è lo XOR: 1 se gli ingressi sono diversi.</li><li>Rapporto 1/2: un bit entra, due escono. Il doppio dei bit, ma ogni bit trasmesso "porta traccia" anche dei due bit precedenti.</li>
<li>Esempio: il messaggio <b>1 0 1 1</b> (più due zeri finali per svuotare il registro) diventa <b>11 10 00 01 01 11</b>.</li></ul></div></div>''')
D.add("Gli stati e il traliccio",'''<div class="two"><div><ul>
<li>Il contenuto del registro (s1 s0) è lo <b>stato</b>: con 2 bit di memoria ci sono 4 stati (00, 10, 01, 11).</li>
<li>Da ogni stato si può andare solo in <b>due</b> stati successivi, a seconda che il nuovo bit sia 0 o 1, e ogni passaggio produce una coppia di bit nota.</li>
<li>Disegnando stati e passaggi nel tempo si ottiene il <b>traliccio</b> (trellis): ogni messaggio possibile è un percorso da sinistra a destra.</li></ul></div><div>
<h3>Il trucco</h3><ul class="small"><li>Non tutte le sequenze di coppie sono possibili: il codice ne permette solo alcune.</li>
<li>Se ricevi una sequenza "impossibile", sai che c'è un errore. Il decodificatore cerca il percorso nel traliccio che produce la sequenza <b>più simile</b> a quella ricevuta.</li>
<li>La somiglianza si misura con la <b>distanza di Hamming</b>: quanti bit sono diversi.</li></ul></div></div>''')
D.add("Il cuore dell'algoritmo",'''<div class="two"><div><ol>
<li>Per ogni stato teniamo un numero: la <b>metrica</b>, cioè quanti bit di differenza ha accumulato il percorso migliore che arriva lì.</li>
<li>A ogni passo, per ogni ramo: metrica dello stato di partenza + differenza tra la coppia del ramo e quella ricevuta (<b>somma</b>).</li>
<li>In ogni stato arrivano due rami: teniamo quello con la metrica più bassa (<b>confronta e scegli</b>). L'altro viene scartato per sempre.</li>
<li>Alla fine si parte dallo stato finale e si ripercorre all'indietro il percorso sopravvissuto: sono i bit decodificati.</li></ol></div><div>
<h3>Perché funziona</h3><ul class="small"><li>Se due percorsi arrivano nello stesso stato, da lì in poi il loro futuro è identico: quello che oggi è peggiore resterà peggiore. Si può scartare subito.</li>
<li>Così il lavoro cresce in modo <b>lineare</b> con la lunghezza del messaggio, non esponenziale.</li>
<li>Si chiama "add-compare-select": somma, confronta, scegli. È talmente regolare che si costruisce facilmente in hardware.</li></ul></div></div>''')
D.add("Un esempio passo per passo",f'''<div class="fig" style="width:96%">{svg("trellis.svg")}</div><div class="two" style="align-items:start;gap:30px"><div><ul class="small">
<li>Trasmesso: <b>11 10 00 01 01 11</b>. Ricevuto: 11 10 <b>10</b> 01 01 11, con un bit sbagliato al terzo passo (in rosso).</li>
<li>Nei cerchi: la metrica di ogni stato. Linee continue: bit 0; tratteggiate: bit 1.</li></ul></div><div><ul class="small">
<li>Il percorso arancione, ripercorso all'indietro dallo stato 00, dà <b>1 0 1 1 0 0</b>: il messaggio giusto. La metrica finale (1) dice che è stato corretto un bit.</li></ul></div></div>''')
D.add("Decisioni dure e morbide",'''<div class="two"><div><ul>
<li>Nell'esempio il ricevitore decide prima "0 o 1" per ogni bit e poi Viterbi conta le differenze: <b>decisioni dure</b>.</li>
<li>Meglio ancora: passare a Viterbi <b>quanto</b> il ricevitore è sicuro (per esempio +0,9 è "quasi certamente 1", +0,1 è "forse 1"). Sono le <b>decisioni morbide</b>.</li>
<li>Le decisioni morbide valgono circa <b>2 dB</b> di guadagno: come raddoppiare quasi la potenza.</li></ul></div><div>
<h3>Quanto si guadagna</h3><ul class="small"><li>Un codice convoluzionale con rapporto 1/2 e memoria più lunga (per esempio 6 bit, 64 stati, quello dei satelliti) con decisioni morbide guadagna circa <b>5 dB</b> rispetto ai bit nudi, a BER 10<sup>−5</sup>.</li>
<li>Il prezzo: il doppio dei bit da trasmettere e più calcoli nel ricevitore.</li>
<li>I codici più moderni (turbo, LDPC come in FT8 e nel 5G) si avvicinano ancora di più al limite di Shannon, ma l'idea di fondo è la stessa: ridondanza + ricerca del messaggio più probabile.</li></ul></div></div>''')
D.add("Dove si usa",'''<table><tr><th>Sistema</th><th>Uso di Viterbi</th></tr>
<tr><td class="l"><b>GSM</b></td><td class="l">decodifica del codice convoluzionale (16 stati) <b>e</b> equalizzatore sulla training sequence</td></tr>
<tr><td class="l"><b>Sonde spaziali e satelliti</b></td><td class="l">codice convoluzionale a 64 stati, rapporto 1/2, molto diffuso dalle missioni degli anni '70 in poi</td></tr>
<tr><td class="l"><b>Wi-Fi (802.11a/g)</b></td><td class="l">codice convoluzionale a 64 stati con rapporti 1/2, 2/3, 3/4</td></tr>
<tr><td class="l"><b>DMR</b></td><td class="l">codice a traliccio a rapporto 3/4 per i dati</td></tr>
<tr><td class="l"><b>Modem e dischi</b></td><td class="l">modulazione codificata a traliccio, lettura dei dischi magnetici</td></tr>
<tr><td class="l"><b>Oltre la radio</b></td><td class="l">riconoscimento vocale, analisi del DNA: ovunque si cerchi la sequenza nascosta più probabile</td></tr></table>''')
rows=[("Codice convoluzionale","ogni bit trasmesso dipende dagli ultimi bit"),("Stati","2<sup>memoria</sup>; traliccio = tutti i percorsi"),("Metrica","distanza (Hamming o morbida) dal ricevuto"),("Add-compare-select","in ogni stato sopravvive un solo percorso"),("Traceback","all'indietro dallo stato finale: i bit corretti"),("Guadagno","qualche dB: come avere più potenza")]
D.add("Riepilogo",'<table class="sum">'+"".join(f'<tr><td class="l" style="width:250px"><b>{a}</b></td><td class="l">{b}</td></tr>' for a,b in rows)+'</table>')
D.render(); pdf("BONUS_Viterbi_IV3HGA.pdf")
