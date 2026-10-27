from deck import *
D=Deck("Esempi pratici<br>ed errori di misura","Come calcolare quanto ci si può fidare di una misura, quattro esempi numerici, gli errori subdoli, casi pratici di ricerca guasti in stazione e la manutenzione dello strumento","Il multimetro: esempi pratici ed errori")
D.add("Da dove vengono gli errori",'''<div class="two"><div><table><tr><th>Sorgente</th><th>Quando pesa</th></tr>
<tr><td class="l"><b>Precisione dello strumento</b></td><td class="l">sempre: ±(% lettura + digit)</td></tr>
<tr><td class="l"><b>Effetto di carico</b></td><td class="l">tensioni su sorgenti ad alta impedenza</td></tr>
<tr><td class="l"><b>Burden voltage</b></td><td class="l">correnti in circuiti a bassa tensione o bassa resistenza</td></tr>
<tr><td class="l"><b>Puntali e contatti</b></td><td class="l">resistenze basse, cadute in mV</td></tr>
<tr><td class="l"><b>Forma d'onda e frequenza</b></td><td class="l">AC non sinusoidale, frequenze fuori banda</td></tr>
<tr><td class="l"><b>Tensioni termoelettriche</b></td><td class="l">misure di pochi mV o µV</td></tr>
<tr><td class="l"><b>Ambiente</b></td><td class="l">temperatura, umidità, batteria scarica, RF</td></tr></table></div><div><ul>
<li>Nel caso peggiore gli errori si <b>sommano</b>; se sono indipendenti, una stima più realistica è la radice della somma dei quadrati.</li>
<li>Spesso un errore domina tutti gli altri: trovalo, e saprai quante cifre del display hanno senso.</li>
<li>Scrivi il risultato con l'incertezza: "13,80 ± 0,09 V" dice molto più di "13,80 V".</li></ul></div></div>''')
D.add("Esempio 1: la tensione dell'alimentatore",'''<div class="two"><div><ul>
<li>Multimetro da 6000 conteggi, ±(0,5 % + 2 digit) in V DC.</li>
<li>Lettura: <b>13,80 V</b> sulla portata 60,00 V (digit = 0,01 V).</li></ul>
<div class="eq">±(0,005 · 13,80 + 2 · 0,01) = ±0,089 V</div>
<ul class="small"><li>Il valore vero è tra 13,71 e 13,89 V.</li>
<li>L'alimentatore ha un'uscita a bassa impedenza: l'effetto di carico dei 10 MΩ è trascurabile.</li></ul></div><div>
<h3>Cosa significa in pratica</h3><ul class="small"><li>La seconda cifra decimale non è garantita: inutile regolare l'alimentatore "a 13,80 esatti" con questo strumento.</li>
<li>Per confronti (stessa portata, stesso strumento, poco tempo dopo) la ripetibilità è molto migliore della precisione: puoi vedere variazioni di 0,01 V anche se il valore assoluto è incerto di ±0,09 V.</li></ul></div></div>''')
D.add("Esempio 2: corrente di riposo di un finale",'''<div class="two"><div><ul>
<li>Shunt da 0,1 Ω all'1 % nel circuito di drain; misura in mV.</li>
<li>Lettura: <b>25,00 mV</b> sulla portata 60,00 mV, ±(0,5 % + 2 digit) (digit = 0,01 mV).</li></ul>
<div class="eq">errore strumento = ±(0,125 + 0,02) mV = ±0,58 %</div>
<div class="eq">I = 25,00 mV / 0,1 Ω = 250 mA</div></div><div>
<ul><li>Incertezza totale nel caso peggiore: 0,58 % (strumento) + 1 % (shunt) ≈ <b>±1,6 %</b>, cioè 250 ± 4 mA.</li>
<li>Su pochi mV le <b>tensioni termoelettriche</b> nei contatti possono aggiungere qualche µV: trascurabili qui, non con shunt da 1 mΩ.</li>
<li>Misurata così, la corrente di riposo si regola senza aprire il circuito e senza burden.</li></ul></div></div>''')
D.add("Esempio 3: una resistenza piccola",'''<div class="two"><div><ul>
<li>Resistenza da <b>0,47 Ω</b> (per esempio quella di emettitore di un finale).</li>
<li>Puntali senza REL: 0,20 Ω tra puntali e contatti. Lo strumento legge <b>0,67 Ω</b>: +43 %.</li>
<li>Con REL sui puntali in corto: legge 0,47 Ω.</li></ul>
<div class="eq">±(1 % · 0,47 + 3 · 0,01) = ±0,035 Ω ≈ ±7 %</div></div><div>
<h3>Lezione</h3><ul class="small"><li>Sui valori piccoli i digit dominano: 3 digit da 0,01 Ω pesano più dell'1 % della lettura.</li>
<li>Il metodo a 4 fili, o una misura V/I con una corrente nota di qualche ampere, fa molto meglio.</li>
<li>Pulisci i terminali e tieni i puntali premuti allo stesso modo: la resistenza di contatto cambia.</li></ul></div></div>''')
D.add("Esempio 4: AC non sinusoidale",'''<div class="two"><div><ul>
<li>Un inverter economico "ad onda modificata" dà un'uscita a gradini, non sinusoidale.</li>
<li>Per semplicità: un'onda quadra da <b>230 V efficaci</b>.</li>
<li>Un multimetro <b>a valore medio</b> legge 230 × 1,111 = <b>255 V</b>. Un true RMS legge 230 V.</li></ul></div><div>
<h3>Altri casi tipici</h3><ul class="small"><li>Corrente assorbita da un alimentatore switching o da un alimentatore con raddrizzatore e condensatore: impulsi stretti, il multimetro a valore medio legge decisamente <b>meno</b> del vero.</li>
<li>Uscite PWM di ventole e regolatori: in DC leggi il valore medio, in AC qualcosa che dipende dallo strumento; per capire la forma d'onda serve l'oscilloscopio.</li>
<li>Audio e toni: precisione buona solo dentro la banda AC dichiarata.</li></ul></div></div>''')
D.add("Errori subdoli",'''<div class="two"><div><ul class="small">
<li><b>Tensioni termoelettriche</b>: ogni giunzione tra metalli diversi (rame-stagno, rame-ottone) a temperature diverse genera microvolt. Su misure di pochi mV, inverti i puntali e fai la media.</li>
<li><b>Batteria scarica</b>: alcuni strumenti continuano a mostrare numeri, ma sbagliati.</li>
<li><b>Temperatura</b>: fuori dall'intervallo di riferimento (spesso 18–28 °C) si aggiunge un errore per grado: vale anche per lo strumento lasciato al sole in auto.</li></ul></div><div><ul class="small">
<li><b>RF</b>: vicino a un trasmettitore il multimetro può leggere valori assurdi; cavi lunghi dei puntali fanno da antenna.</li>
<li><b>Umidità e sporco</b> sui circuiti: resistenze alte e perdite che cambiano con il tempo.</li>
<li><b>REL o MIN/MAX</b> lasciati attivi: leggi differenze o valori memorizzati invece della misura attuale.</li>
<li><b>Autorange</b> che cambia portata durante la misura: valori che "saltano".</li></ul></div></div>''')
D.add("Ricerca guasti in stazione: tre casi",'''<div class="two"><div><h3>La radio si spegne in trasmissione</h3><ol class="small">
<li>MIN/MAX ai morsetti della radio mentre trasmetti: la tensione minima.</li>
<li>Caduta sotto carico su cavi, fusibile e connettori.</li>
<li>Resistenza interna di alimentatore o batteria.</li></ol>
<h3>Un'antenna che "non va più"</h3><ol class="small"><li>Scarica il cavo, poi continuità in DC: deve corrispondere a quella dell'antenna sana (corto o aperto).</li>
<li>Coassiale: corto all'altro capo, pochi decimi di ohm.</li>
<li>Capacità del cavo aperto per stimare dove è interrotto.</li></ol></div><div>
<h3>Ronzio nell'audio</h3><ol class="small"><li>mV AC tra le masse degli apparati: ground loop.</li>
<li>V AC sui condensatori di filtro dell'alimentatore: ripple.</li>
<li>Controlla che le letture non cambino trasmettendo: RF in stazione.</li></ol>
<p class="note">In tutti i casi: annota le letture. Una tabella di valori "sani" del tuo impianto è il miglior strumento di diagnosi.</p></div></div>''')
D.add("Manutenzione e verifica dello strumento",'''<div class="two"><div><ul>
<li><b>Riferimento di tensione</b>: un piccolo riferimento di precisione (per esempio un integrato da 2,5 V o 5 V allo 0,05–0,1 %) per controllare periodicamente la portata DC.</li>
<li><b>Confronto</b> tra due strumenti sulla stessa misura: se non concordano entro le tolleranze, uno dei due ha un problema.</li>
<li><b>Fusibili</b> controllati con il trucco della continuità; <b>puntali</b> verificati in Ω.</li></ul></div><div><ul>
<li>Batteria di buona qualità, tolta se lo strumento resta fermo a lungo (le perdite di elettrolita distruggono i circuiti).</li>
<li>Strumento riposto in custodia, lontano da umidità e calore.</li>
<li>Per misure che devono valere davvero, taratura in un laboratorio: almeno conosci lo scostamento del tuo strumento.</li></ul></div></div>''')
rows=[("Tensione","sorgente a bassa impedenza? altrimenti attenzione al carico"),("Corrente","shunt interno o resistenza già presente (I = V/R)"),("Ohm","circuito spento, REL, 4 fili per i milliohm"),("AC","true RMS e banda adeguata"),("Diodi e transistor","prova diodi, base comune, trucco del gate"),
("Picchi e cadute","MIN/MAX e peak"),("Connessioni","caduta di tensione sotto carico"),("Incertezza","±(% + digit), più carico, burden e puntali")]
D.add("Il prontuario del multimetro",'<table class="sum">'+"".join(f'<tr><td class="l" style="width:250px"><b>{a}</b></td><td class="l">{b}</td></tr>' for a,b in rows)+'</table>')
D.render(); pdf("MM_Esempi_Errori_IV3HGA.pdf")
