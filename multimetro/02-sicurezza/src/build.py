from deck import *
O="#e0563b"
D=Deck("Il multimetro:<br>sicurezza","Categorie CAT e sovratensioni, l'errore della boccola di corrente, fusibili e puntali, il metodo live-dead-live, tensioni fantasma e le situazioni tipiche della stazione radio","Il multimetro: sicurezza")
short=f'''<svg viewBox="0 0 770 250" font-family="DejaVu Sans">{ARW}
{box(20,60,170,90,"Presa di rete|230 V","#fff",16)}
<path d="M190 85 H300" stroke="{O}" stroke-width="3"/><path d="M190 125 H300" stroke="{N}" stroke-width="3"/>
{box(300,40,230,130,"","#fff")}<text x="415" y="70" text-anchor="middle" font-size="15" font-weight="700" fill="{N}">Multimetro</text>
<text x="415" y="95" text-anchor="middle" font-size="13" fill="#555">puntale rosso nella boccola A</text>
<rect x="360" y="110" width="110" height="26" rx="4" fill="#fde4de" stroke="{O}" stroke-width="2"/><text x="415" y="128" text-anchor="middle" font-size="13" fill="{O}" font-weight="700">shunt 0,01 Ω</text>
<text x="415" y="160" text-anchor="middle" font-size="13" fill="#555">+ fusibile</text>
<text x="560" y="80" font-size="14" fill="{O}" font-weight="700">I = 230 V / ~0,1 Ω</text><text x="560" y="100" font-size="14" fill="{O}" font-weight="700">= migliaia di ampere</text>
<text x="560" y="130" font-size="13" fill="{N}">per pochi millisecondi:</text><text x="560" y="148" font-size="13" fill="{N}">arco, fiammata,</text><text x="560" y="166" font-size="13" fill="{N}">ustioni</text>
<text x="20" y="215" font-size="13" fill="#555">Solo un fusibile HRC adatto interrompe una corrente così prima che l'arco si sostenga.</text></svg>'''
D.add("Perché parlarne",'''<div class="two"><div><ul>
<li>Il multimetro si usa <b>in mano</b>, a pochi centimetri dal circuito: è lo strumento con cui ci si fa male più spesso.</li>
<li>I pericoli non sono solo la tensione: un cortocircuito su una batteria o un alimentatore da 30 A produce scintille, metallo fuso e ustioni.</li>
<li>Uno strumento inadatto può <b>esplodere</b> se arriva una sovratensione o se sbagli boccola.</li></ul></div><div>
<h3>Tre regole di base</h3><ol><li>Strumento e puntali con categoria adatta a dove misuri.</li><li>Boccole e funzione controllate <b>prima</b> di toccare il circuito.</li><li>Verifica che lo strumento funzioni prima e dopo (live-dead-live).</li></ol></div></div>''')
D.add("Le categorie di misura (CAT)",'''<div class="two"><div><table><tr><th>Categoria</th><th>Dove</th></tr>
<tr><td class="l"><b>CAT I</b></td><td class="l">circuiti non collegati alla rete: elettronica a batteria, secondari isolati</td></tr>
<tr><td class="l"><b>CAT II</b></td><td class="l">apparecchi collegati a una presa: elettrodomestici, alimentatori, strumenti</td></tr>
<tr><td class="l"><b>CAT III</b></td><td class="l">impianto dell'edificio: quadri, prese, linee fisse</td></tr>
<tr><td class="l"><b>CAT IV</b></td><td class="l">origine dell'impianto: contatore, linea di arrivo</td></tr></table></div><div>
<h3>Perché non basta il numero di volt</h3><ul class="small"><li>La categoria indica la capacità di resistere ai <b>transitori</b> (fulmini lontani, commutazioni), molto più alti della tensione nominale.</li>
<li>Per esempio, secondo la norma IEC 61010 un CAT III 600 V deve reggere impulsi di 6 kV, un CAT IV 600 V di 8 kV.</li>
<li>Uno strumento CAT II usato sul quadro elettrico può cedere proprio durante un transitorio.</li>
<li>La categoria valida è la più bassa tra strumento, puntali e accessori.</li></ul></div></div>''')
D.add("L'errore più pericoloso: la boccola di corrente",f'''<div class="diag" style="width:84%;margin:-6px auto 0">{short}</div><div class="two" style="align-items:start;gap:30px"><div><ul class="small">
<li>Dopo una misura di corrente il puntale rosso resta nella boccola <b>A</b>; giri il selettore su V e misuri una presa. Tra i puntali c'è uno shunt da pochi milliohm.</li></ul></div><div><ul class="small">
<li>Prevenzione: dopo ogni misura di corrente <b>riporta subito</b> il puntale in V Ω. Molti strumenti hanno un allarme o otturatori sulle boccole: non disattivarli.</li></ul></div></div>''')
D.add("I fusibili",'''<div class="two"><div><ul>
<li>Le boccole di corrente sono protette da fusibili <b>HRC</b> (alto potere di interruzione): ceramici, riempiti di sabbia, con tensione nominale alta (per esempio 1000 V) e potere di interruzione di migliaia di ampere.</li>
<li>Un fusibile di vetro da 250 V ha un potere di interruzione di poche decine di ampere: con una corrente di guasto di migliaia di ampere può <b>non interrompere</b> l'arco o esplodere.</li>
<li>Sostituiscili solo con lo <b>stesso identico tipo</b> indicato dal costruttore.</li></ul></div><div>
<h3>Trucco: controllare il fusibile senza aprire</h3><ol class="small"><li>Selettore su Ω, puntale nero in COM.</li><li>Infila il puntale rosso nella boccola V Ω e tocca con la sua punta l'interno della boccola A (o 10 A).</li>
<li>Fusibile buono: pochi decimi di ohm sulla boccola 10 A, qualche ohm sulla mA. <b>OL</b>: fusibile interrotto.</li></ol>
<p class="note">Il valore esatto dipende dallo strumento: misuralo una volta quando è nuovo e annotalo.</p></div></div>''')
D.add("Puntali e accessori",'''<div class="two"><div><ul>
<li>I puntali hanno la loro categoria (CAT e tensione): deve essere almeno quella dell'uso.</li>
<li>Per CAT III e IV si usano puntali con la parte metallica scoperta <b>corta</b> (pochi mm) o cappucci isolanti: riducono il rischio di cortocircuito tra due conduttori vicini.</li>
<li>Connettori a banana <b>schermati</b> sul lato strumento.</li>
<li>Le dita restano sempre dietro le protezioni dei puntali.</li></ul></div><div>
<h3>Controlli frequenti</h3><ul class="small"><li>Isolamento integro: niente tagli, schiacciature, parti fuse.</li>
<li>Continuità: puntali in cortocircuito in Ω devono leggere pochi decimi di ohm. Un puntale interrotto dà letture assurde, o "0 V" su un circuito in tensione.</li>
<li>Coccodrilli e adattatori: anche loro hanno una categoria, spesso solo CAT I o II.</li></ul></div></div>''')
D.add("Il metodo: live-dead-live",'''<div class="two"><div><ol>
<li>Verifica lo strumento su una sorgente <b>nota</b> in tensione (una presa sicura, un verificatore).</li>
<li>Misura il circuito: risulta senza tensione?</li>
<li>Verifica di nuovo sulla sorgente nota: lo strumento funziona ancora?</li></ol>
<p class="note">Solo così sai che "0 V" significa davvero zero, e non un fusibile o un puntale interrotto, o una batteria scarica.</p></div><div>
<h3>Altre regole d'oro</h3><ul class="small"><li>Collega per primo il puntale <b>COM</b> (al riferimento), poi il rosso. Scollega per primo il <b>rosso</b>.</li>
<li>Non cambiare funzione con i puntali sul circuito.</li>
<li>Una mano sola vicino a parti in tensione; l'altra lontana dal telaio.</li>
<li>Con la <b>batteria scarica</b> molti strumenti leggono valori sbagliati, anche bassi: sostituiscila al primo avviso.</li>
<li>Mai misure su circuiti oltre i limiti dello strumento, nemmeno "un attimo".</li></ul></div></div>''')
D.add("Tensioni fantasma e rilevatori senza contatto",'''<div class="two"><div><h3>Tensioni fantasma</h3><ul class="small">
<li>Un conduttore scollegato ma vicino a cavi in tensione si carica per accoppiamento capacitivo: con 10 MΩ d'ingresso il multimetro legge decine di volt.</li>
<li>Sono innocue ma ingannano: non sai se il conduttore è davvero collegato.</li>
<li>La funzione <b>LoZ</b> (bassa impedenza, qualche kΩ) le fa sparire: una tensione vera resta.</li></ul></div><div>
<h3>Rilevatori NCV (senza contatto)</h3><ul class="small"><li>Comodi per una prima verifica, ma possono dare <b>falsi negativi</b>: cavi schermati, batterie scariche, conduttori lontani dalla punta.</li>
<li>Non sostituiscono mai una misura con i puntali secondo il metodo live-dead-live.</li></ul></div></div>''')
D.add("Situazioni tipiche della stazione radio",'''<div class="two"><div><ul class="small">
<li><b>Alimentatori da 13,8 V</b>: la tensione è innocua, ma un puntale che scivola tra due morsetti fa un cortocircuito da decine di ampere. Usa puntali sottili e cappucci, misura con calma.</li>
<li><b>Batterie</b> al piombo e al litio: correnti di cortocircuito enormi. Niente anelli e orologi.</li>
<li><b>Amplificatori a valvole</b>: anodiche di centinaia o migliaia di volt, condensatori che restano carichi. Sonde e strumenti adatti, scarica e verifica sempre.</li></ul></div><div><ul class="small">
<li><b>Antenne e cavi</b>: possono essere carichi di elettricità statica; scaricali prima di misurarli in Ω, o il multimetro ne risente.</li>
<li><b>Mai</b> misurare su un'antenna o una linea mentre si trasmette: la RF brucia lo strumento e le dita.</li>
<li><b>Alimentatori switching aperti</b>: il lato primario è collegato alla rete; condensatori di ingresso carichi a oltre 300 V.</li></ul></div></div>''')
rows=["Strumento e puntali con categoria adatta, integri","Fusibili HRC originali, verificati","Puntale nella boccola giusta per la funzione scelta","Live-dead-live sulle misure di assenza di tensione","Batteria dello strumento carica","COM per primo, rosso per ultimo; mai cambiare funzione sul circuito","Niente misure su antenne e linee durante la trasmissione"]
D.add("Checklist di sicurezza",'<table class="sum">'+"".join(f'<tr><td class="l" style="width:46px;color:#22b8f0;font-weight:800">☐</td><td class="l">{r}</td></tr>' for r in rows)+'</table>')
D.render(); pdf("MM_Sicurezza_IV3HGA.pdf")
