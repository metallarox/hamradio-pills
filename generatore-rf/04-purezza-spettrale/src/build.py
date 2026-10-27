from deck import *
D=Deck("La purezza<br>spettrale","Armoniche, spurie non armoniche, rumore di fase e rumore a larga banda del generatore: perché decidono quali misure sul ricevitore sono possibili, come verificarle e come migliorarle","Il generatore RF: purezza spettrale")
D.add("Perché la purezza conta",'''<div class="two"><div><ul>
<li>Il ricevitore non sa distinguere tra il segnale "voluto" e i difetti del generatore: li riceve tutti.</li>
<li>In un test di <b>sensibilità</b> il generatore deve essere pulito vicino alla frequenza di prova.</li>
<li>Nei test di <b>selettività e dinamica</b> il segnale forte del generatore cade lontano dalla frequenza di ascolto: il suo rumore di fase e le sue spurie, a quella distanza, arrivano direttamente nel canale del ricevitore.</li></ul></div><div>
<h3>Regola d'oro</h3><ul class="small"><li>Il generatore deve essere <b>almeno 10 dB migliore</b> del ricevitore nella caratteristica che stai misurando.</li>
<li>Se non lo è, stai misurando il generatore, non il ricevitore.</li>
<li>Un buon ricevitore HF moderno ha caratteristiche di dinamica che molti generatori, anche da laboratorio, non raggiungono: la misura va preparata con cura.</li></ul></div></div>''')
D.add("Armoniche",'''<div class="two"><div><ul>
<li>Righe a 2f, 3f, … prodotte dagli stadi d'uscita del generatore. Valori tipici da −25 a −40 dBc, migliori nei generatori con filtri d'uscita.</li>
<li>Nei moduli economici con uscita a onda quadra la 3ª armonica è a circa <b>−10 dBc</b>.</li></ul>
<h3>Quando danno fastidio</h3><ul class="small"><li>Provi un ricevitore a 7 MHz e il generatore ha un'armonica a 14 MHz: di solito non è un problema, il ricevitore non è sintonizzato lì.</li>
<li>Diventano un problema quando provi i <b>filtri</b> e le <b>risposte spurie</b> del ricevitore (immagini, frequenze intermedie), o quando usi il generatore per pilotare un mixer.</li></ul></div><div>
<h3>Come verificarle e ridurle</h3><ul class="small"><li>Generatore → attenuatore → analizzatore: misura le armoniche in dBc.</li>
<li>Un <b>passa-basso</b> o un passa-banda dopo il generatore le riduce di 40–60 dB.</li>
<li>Il livello delle armoniche dipende spesso dal livello d'uscita: più bassa la potenza dell'ultimo stadio, più pulito il segnale. Usa il generatore a livello medio e attenua all'esterno.</li></ul></div></div>''')
D.add("Spurie non armoniche",'''<div class="two"><div><ul>
<li>Righe a frequenze "strane", prodotte dal sintetizzatore: residui del riferimento, prodotti di miscelazione, immagini del DDS, divisori frazionari.</li>
<li>Possono essere vicine alla portante (pochi kHz) o lontane.</li>
<li>Livelli tipici da −50 a −80 dBc; alcune compaiono solo a certe frequenze di uscita.</li></ul></div><div>
<h3>Perché ingannano</h3><ul class="small"><li>In un test di sensibilità una spuria a −60 dBc è innocua; in un test di blocking con il segnale forte a 0 dBm, una spuria a −60 dBc finisce nel canale ricevuto a −60 dBm: un segnale fortissimo!</li>
<li>Test: sintonizza il ricevitore e sposta di poco la frequenza del generatore. Se nel ricevitore compare qualcosa che "cammina" in modo diverso dal previsto, è una spuria del generatore.</li>
<li>Controllale con l'analizzatore in uno span stretto e largo, alla frequenza di prova.</li></ul></div></div>''')
D.add("Il rumore di fase",f'''<div class="two"><div class="fig">{svg("pn.svg")}<p class="cap">Andamenti indicativi, non di modelli specifici.</p></div><div><ul class="small">
<li>Ogni oscillatore ha una "gonna" di rumore attorno alla portante: il <b>rumore di fase</b>, in dBc/Hz a una certa distanza.</li>
<li>Nel test di blocking o di reciprocal mixing, il rumore di fase del generatore alla distanza di prova entra nel canale del ricevitore.</li></ul>
{eq("P<sub>rumore nel canale</sub> = P<sub>gen</sub> + L(f) + 10·log(B)")}
<p class="note">Esempio: generatore a −20 dBm con −120 dBc/Hz a 20 kHz, ricevitore con filtro di 2,4 kHz: −20 − 120 + 33,8 = <b>−106 dBm</b> di rumore nel canale. Se il rumore proprio del ricevitore è −130 dBm, il generatore domina la misura di 24 dB.</p></div></div>''')
D.add("Rumore a larga banda e perdite",'''<div class="two"><div><h3>Rumore a larga banda</h3><ul class="small">
<li>Lontano dalla portante il rumore di fase si appiattisce in un "pavimento" (per esempio −145 dBc/Hz).</li>
<li>Ai livelli bassi conta anche il rumore termico dell'attenuatore e dell'uscita: in pratica, sotto −130 dBm il segnale del generatore è "pulito" quanto basta per i test di sensibilità.</li>
<li>Ai livelli alti il pavimento di rumore del generatore può alzare il rumore di un ricevitore anche a molti MHz di distanza: un passa-banda stretto sul generatore lo elimina.</li></ul></div><div>
<h3>Perdite (leakage)</h3><ul class="small"><li>Fanno parte della "purezza": un generatore che perde segnale dal contenitore rende impossibili le misure di sensibilità (lezione su livelli e attenuatori).</li>
<li>Verifica con il ricevitore stesso: generatore acceso alla frequenza di prova, livello minimo o uscita disattivata, cavo scollegato dal ricevitore. Non deve sentirsi nulla.</li></ul></div></div>''')
D.add("Come verificare il tuo generatore",'''<div class="two"><div><ol>
<li><b>Armoniche</b>: analizzatore, span fino a 5f, delta marker in dBc.</li>
<li><b>Spurie</b>: span di 1 MHz e di 100 kHz attorno alla portante, RBW stretta, cerca righe sopra il rumore.</li>
<li><b>Rumore di fase</b>: noise marker a 1, 10, 20, 100 kHz (capitolo sull'analizzatore, misure classiche).</li>
<li><b>Livello</b>: confronta con un power meter alla frequenza di prova, a +0 dBm e a −30 dBm.</li></ol></div><div>
<h3>Limiti della verifica</h3><ul class="small"><li>Un analizzatore ha anch'esso rumore di fase e spurie: misuri la somma dei due. Se il risultato è vicino alle specifiche dell'analizzatore, il generatore è "almeno così buono".</li>
<li>Un buon metodo per il rumore di fase vicino alla portante: usa il ricevitore stesso in CW con filtro stretto, e ascolta il rumore a varie distanze da un segnale forte (lezione sulla selettività).</li>
<li>Annota i risultati: ti diranno quali test sui ricevitori puoi fare con quel generatore.</li></ul></div></div>''')
D.add("Migliorare la purezza",'''<table><tr><th>Problema</th><th>Rimedio</th></tr>
<tr><td class="l"><b>Armoniche</b></td><td class="l">passa-basso o passa-banda dopo il generatore</td></tr>
<tr><td class="l"><b>Spurie lontane e pavimento di rumore</b></td><td class="l">passa-banda stretto (anche a cavità in VHF/UHF) sulla frequenza del generatore</td></tr>
<tr><td class="l"><b>Rumore di fase vicino</b></td><td class="l">nessun filtro lo toglie: serve un oscillatore migliore (un quarzo fisso è spesso eccellente)</td></tr>
<tr><td class="l"><b>Livelli alti sporchi</b></td><td class="l">usa il generatore a livello medio e attenua dopo</td></tr>
<tr><td class="l"><b>Intermodulazione tra due generatori</b></td><td class="l">attenuatori su ciascuno, combinatore ibrido, isolatori</td></tr>
<tr><td class="l"><b>Perdite</b></td><td class="l">cavi doppia calza, connettori serrati, attenuatori vicino al ricevitore</td></tr></table>
<p class="note" style="margin-top:12px">Trucco classico per i test di dinamica: un <b>oscillatore a quarzo</b> di buona qualità, seguito da un filtro, come sorgente del segnale forte. Il rumore di fase di un quarzo è spesso migliore di quello di un sintetizzatore.</p>''')
rows=[("Regola","generatore 10 dB migliore del ricevitore nella misura"),("Armoniche","−25…−40 dBc; filtra con un passa-basso"),("Spurie","innocue in sensibilità, critiche in blocking"),("Rumore di fase","P<sub>gen</sub> + L(f) + 10·log(B) nel canale"),("Rimedi","filtri per armoniche e spurie; quarzo per il rumore vicino")]
D.add("Riepilogo",'<table class="sum">'+"".join(f'<tr><td class="l" style="width:200px"><b>{a}</b></td><td class="l">{b}</td></tr>' for a,b in rows)+'</table>')
D.render(); pdf("GEN_Purezza_Spettrale_IV3HGA.pdf")
