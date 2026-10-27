from deck import *
D=Deck("Resistenza, continuità<br>e prova diodi","Come il multimetro misura gli ohm, puntali e REL, misura a 4 fili, misure in circuito, continuità, prova diodi, transistor e MOSFET, ed esempi dalla stazione radio","Il multimetro: resistenza, continuità e diodi")
kel=f'''<svg viewBox="0 0 760 260" font-family="DejaVu Sans">{ARW}
<rect x="290" y="100" width="180" height="50" rx="6" fill="#e8f6fd" stroke="{C}" stroke-width="2.5"/><text x="380" y="131" text-anchor="middle" font-size="15" font-weight="700" fill="{C}">R da misurare</text>
<circle cx="290" cy="125" r="5" fill="{N}"/><circle cx="470" cy="125" r="5" fill="{N}"/>
<path d="M290 125 H190 V40 H60" stroke="{N}" stroke-width="3" fill="none"/><path d="M470 125 H570 V40 H700" stroke="{N}" stroke-width="3" fill="none"/>
<path d="M295 125 V210 H60" stroke="{C}" stroke-width="2" fill="none"/><path d="M465 125 V210 H700" stroke="{C}" stroke-width="2" fill="none"/>
<text x="60" y="30" font-size="14" fill="{N}" font-weight="700">corrente I →</text><text x="610" y="30" font-size="14" fill="{N}" font-weight="700">← ritorno</text>
<text x="60" y="230" font-size="14" fill="{C}" font-weight="700">misura V (nessuna corrente)</text>
<text x="380" y="255" text-anchor="middle" font-size="13" fill="#555">R = V / I: la resistenza dei cavi di corrente e dei contatti non entra nella misura</text></svg>'''
D.add("Come il multimetro misura gli ohm",'''<div class="two"><div><ul>
<li>Lo strumento fa passare una <b>corrente nota</b> nel componente e misura la tensione ai suoi capi: R = V / I.</li>
<li>La corrente di prova cambia con la portata: circa 1 mA sulle portate basse, pochi µA o meno sulle portate da MΩ.</li>
<li>La tensione a vuoto tra i puntali va da qualche decimo di volt a circa 3 V, a seconda del modello e della funzione.</li></ul></div><div>
<h3>Regole</h3><ol class="small"><li>Circuito <b>spento</b> e condensatori <b>scaricati</b>: una tensione presente falsa la misura o danneggia lo strumento.</li>
<li>Non toccare i terminali con le dita sulle resistenze alte.</li>
<li>Per resistenze basse azzera i puntali (REL) o usa il metodo a 4 fili.</li>
<li>In autorange la lettura su valori alti impiega qualche secondo a stabilizzarsi: aspetta.</li></ol></div></div>''')
D.add("Puntali, REL e misura a 4 fili",f'''<div class="diag" style="width:80%;margin:-6px auto 0">{kel}</div><div class="two" style="align-items:start;gap:30px"><div><ul class="small">
<li>I puntali hanno 0,1–0,3 Ω in tutto. Mettili in corto, premi <b>REL</b> (o Δ): lo strumento sottrae quel valore dalle misure successive.</li>
<li>Su resistenze di pochi ohm, l'errore dei puntali e dei contatti è dello stesso ordine della misura.</li></ul></div><div><ul class="small">
<li>Il <b>metodo a 4 fili</b> (Kelvin) usa una coppia di cavi per la corrente e un'altra per la tensione. Lo fanno alcuni multimetri da banco; con due strumenti (alimentatore + amperometro e un voltmetro) lo puoi fare a mano.</li>
<li>Indispensabile per shunt, contatti di relè, cavi, connettori: milliohm che contano.</li></ul></div></div>''')
D.add("Misurare in circuito",'''<div class="two"><div><ul>
<li>In circuito il componente ha in parallelo il resto del circuito: la lettura è sempre <b>uguale o più bassa</b> del valore vero.</li>
<li>Se la tensione di prova supera 0,5 V circa, le giunzioni dei semiconduttori conducono e la lettura crolla.</li>
<li>Alcuni multimetri hanno una funzione <b>ohm a bassa tensione</b> (low-power ohms) che resta sotto la soglia dei diodi.</li></ul></div><div>
<h3>Trucchi</h3><ul class="small"><li>Misura nei due versi (scambia i puntali): se cambia, c'è una giunzione in parallelo.</li>
<li>Se la lettura è più bassa del valore nominale, prima di sostituire il componente <b>stacca un terminale</b> e rimisura.</li>
<li>Una lettura più <b>alta</b> del nominale, in circuito, indica quasi sicuramente un componente interrotto o alterato.</li></ul></div></div>''')
D.add("Resistenze alte e il corpo umano",'''<div class="two"><div><ul>
<li>Tenendo i due terminali di una resistenza tra le dita, il tuo corpo è in parallelo: tra le due mani ci sono tipicamente da 100 kΩ a qualche MΩ, a seconda della pelle.</li>
<li>Su una resistenza da 10 kΩ l'errore è piccolo; su una da 1 MΩ puoi leggere la metà del valore.</li></ul></div><div>
<h3>Altre cause di errore sopra 1 MΩ</h3><ul class="small"><li>Umidità e sporco sul circuito stampato (residui di flussante).</li>
<li>Cavi dei puntali mossi durante la misura: la lettura "balla".</li>
<li>Il multimetro non misura l'<b>isolamento</b>: con pochi volt di prova un cavo può sembrare perfetto e scaricare a 500 V. Per quello serve un megaohmmetro.</li></ul></div></div>''')
D.add("Continuità: cavi, coassiali e antenne",'''<div class="two"><div><ul>
<li>Il cicalino suona sotto una certa soglia, di solito tra 20 e 50 Ω: "c'è collegamento" non significa "collegamento buono".</li>
<li>Utile per cavi, fusibili, interruttori, piste, connettori.</li></ul>
<h3>Cavo coassiale</h3><ul class="small"><li>Estremi liberi: tra centrale e calza deve leggere <b>OL</b>.</li>
<li>Metti in corto centrale e calza all'altro capo: devi leggere pochi decimi di ohm (centrale + calza). Così controlli entrambi i conduttori senza un secondo strumento.</li></ul></div><div>
<h3>Antenne: il corto che è normale</h3><ul class="small"><li>Dipoli ripiegati, adattamenti gamma, hairpin, alcuni balun e molte verticali con adattamento a "shunt feed" sono un <b>cortocircuito in continua</b> tra centrale e calza. È corretto, e scarica anche le cariche statiche.</li>
<li>Un dipolo semplice, invece, deve leggere aperto (OL) tra i due rami.</li>
<li>Conosci il comportamento in DC della tua antenna quando è sana: diventa un test rapido dopo un temporale o una tempesta di vento.</li>
<li>Prima della misura scarica sempre l'antenna: le cariche statiche possono danneggiare lo strumento.</li></ul></div></div>''')
D.add("Prova diodi",'''<div class="two"><div><ul>
<li>Lo strumento fa passare circa 1 mA e mostra la <b>tensione diretta</b> della giunzione, in volt (non in ohm).</li>
<li>Rosso sull'anodo, nero sul catodo (la fascia): conduce. Invertendo i puntali: <b>OL</b>.</li>
<li>OL nei due versi: diodo interrotto. Valore quasi zero nei due versi: in corto.</li></ul></div><div>
<table><tr><th>Componente</th><th>Tensione diretta tipica</th></tr>
<tr><td class="l">Diodo al silicio</td><td class="l">0,5 – 0,7 V</td></tr><tr><td class="l">Schottky</td><td class="l">0,15 – 0,45 V</td></tr>
<tr><td class="l">Germanio</td><td class="l">0,2 – 0,35 V</td></tr><tr><td class="l">LED rosso</td><td class="l">1,6 – 2,0 V</td></tr>
<tr><td class="l">LED verde, blu, bianco</td><td class="l">2,5 – 3,3 V</td></tr></table>
<p class="note">Se la tensione a vuoto dello strumento è più bassa della soglia del LED (alcuni hanno circa 2,5 V), il LED blu o bianco sembra aperto. Uno zener si verifica solo in diretta, a meno che la sua tensione sia sotto quella di prova.</p></div></div>''')
D.add("Provare un transistor bipolare",'''<div class="two"><div><ul>
<li>Un transistor bipolare, per la prova diodi, è come <b>due diodi</b> con la base in comune.</li>
<li>Cerca la base: è il terminale che conduce verso entrambi gli altri con lo stesso puntale.</li></ul>
<table><tr><th>Puntale sulla base</th><th>Verso C ed E</th><th>Tipo</th></tr>
<tr><td class="l">rosso</td><td class="l">~0,6 V verso entrambi</td><td class="l">NPN</td></tr>
<tr><td class="l">nero</td><td class="l">~0,6 V verso entrambi</td><td class="l">PNP</td></tr></table></div><div>
<h3>Distinguere collettore ed emettitore</h3><ul class="small"><li>La giunzione base-emettitore ha di solito una tensione diretta <b>leggermente più alta</b> di quella base-collettore (qualche decina di mV).</li>
<li>Tra collettore ed emettitore: OL nei due versi. Un valore basso indica un transistor in corto o con perdite.</li>
<li>I Darlington mostrano circa il doppio (due giunzioni); molti transistor di potenza hanno un diodo o resistenze interne che cambiano le letture: guarda il datasheet.</li></ul></div></div>''')
D.add("Provare un MOSFET",'''<div class="two"><div><h3>Il diodo di corpo</h3><ul class="small">
<li>Un MOSFET a canale N ha un diodo tra source e drain: rosso sul <b>source</b>, nero sul <b>drain</b> → circa 0,5 V; al contrario OL.</li>
<li>Tra gate e gli altri terminali: OL in tutti i versi (il gate è isolato).</li></ul>
<h3>Il trucco della carica del gate</h3><ol class="small"><li>Nero sul source, rosso sul gate per un attimo: carichi il gate con la tensione di prova.</li>
<li>Ora misura drain-source (rosso sul drain): il MOSFET <b>conduce</b> (lettura bassa) e resta acceso, perché il gate trattiene la carica.</li>
<li>Cortocircuita gate e source con un dito o un filo: si spegne, torna OL.</li></ol></div><div>
<h3>Limiti</h3><ul class="small"><li>Funziona solo se la tensione di prova dello strumento supera la soglia del gate: con MOSFET "logic level" quasi sempre, con quelli standard (soglia 2–4 V) non sempre.</li>
<li>Per i canale P: polarità invertite.</li>
<li>Attenzione all'elettricità statica: il gate è delicato.</li>
<li>È una prova "va/non va": non dice nulla su resistenza di conduzione o prestazioni dinamiche.</li></ul></div></div>''')
D.add("Altri componenti da provare",'''<table><tr><th>Componente</th><th>Cosa aspettarsi</th></tr>
<tr><td class="l"><b>Altoparlante da 8 Ω</b></td><td class="l">circa 6–7 Ω in continua (la bobina mobile)</td></tr>
<tr><td class="l"><b>Trasformatore di rete</b></td><td class="l">primario da decine a centinaia di Ω, secondari di pochi Ω; nessuna continuità tra avvolgimenti e verso il nucleo</td></tr>
<tr><td class="l"><b>Bobina di relè</b></td><td class="l">il valore di targa (da decine a migliaia di Ω); contatti: pochi mΩ quando chiusi</td></tr>
<tr><td class="l"><b>Potenziometro</b></td><td class="l">resistenza totale tra gli estremi; ruotando, il cursore deve variare senza salti (guarda il bargraph)</td></tr>
<tr><td class="l"><b>NTC / PTC</b></td><td class="l">il valore a 25 °C; scaldandoli con le dita il valore deve scendere (NTC) o salire (PTC)</td></tr>
<tr><td class="l"><b>Fusibile</b></td><td class="l">pochi decimi di ohm o meno; OL = interrotto</td></tr>
<tr><td class="l"><b>Trappola di un dipolo</b></td><td class="l">la bobina deve dare continuità tra i due tronchi; OL indica bobina interrotta</td></tr></table>''')
rows=[("Ohm","corrente nota, circuito spento e scarico"),("REL","sottrae i puntali; 4 fili per i milliohm"),("In circuito","letture più basse: stacca un terminale"),("Continuità","coassiale: OL a vuoto, pochi decimi con il corto in fondo"),
("Diodi","Si 0,5–0,7 V; Schottky 0,15–0,45 V; LED 1,6–3,3 V"),("BJT","base comune: NPN con rosso sulla base"),("MOSFET","diodo di corpo e trucco della carica del gate")]
D.add("Riepilogo",'<table class="sum">'+"".join(f'<tr><td class="l" style="width:160px"><b>{a}</b></td><td class="l">{b}</td></tr>' for a,b in rows)+'</table>')
D.render(); pdf("MM_Resistenza_Diodi_IV3HGA.pdf")
