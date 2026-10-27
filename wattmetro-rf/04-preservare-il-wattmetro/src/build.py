from deck import *
D=Deck("Preservare<br>il wattmetro","Come non rompere testine, strumenti e sensori: limiti di potenza e tensione, connettori, statica, trasporto, conservazione e verifiche periodiche","Il wattmetro RF: come preservarlo")
cards=[("Testine e sensori","il diodo, la termocoppia o il termistore: la parte più delicata"),("Strumento a lancetta","bobina mobile: urti, sovraccarichi, zero"),("Connettori","archi, usura, sporco, serraggio"),
("Attenuatori e carichi","scaldano: potenza e durata"),("Cavi","perdite, piegature, connettori allentati"),("La taratura","si perde senza accorgersene")]
D.add("Dove si rompe un wattmetro",'<div class="grid3">'+"".join(f'<div class="card"><h3>{a}</h3><p>{b}</p></div>' for a,b in cards)+'''</div>
<p class="note" style="margin-top:18px">Il guasto più insidioso non è quello che lo rompe del tutto, ma quello che lo fa <b>leggere sbagliato</b>: per questo alla fine del modulo ci sono le verifiche periodiche.</p>''')
D.add("Wattmetri passanti: potenza e tensione",'''<div class="two"><div><ul>
<li>La sezione di linea regge molta potenza, ma la <b>testina</b> è tarata per il suo fondo scala: oltre, la lancetta va a battuta e il diodo lavora fuori dai limiti.</li>
<li>Con un <b>SWR alto</b> la tensione di picco sulla linea cresce: con 1 kW e SWR 3 si superano i 500 V. Connettori e linea devono reggerli.</li>
<li>Considera la <b>PEP</b>, non solo la media: in SSB e AM i picchi sono molto più alti di quello che legge la lancetta.</li></ul></div><div>
<h3>Regole pratiche</h3><ol class="small"><li>Se non conosci la potenza, inizia con la testina di fondo scala più alto.</li>
<li>Non collegare né scollegare <b>mai</b> connettori con la RF presente: l'arco brucia i contatti (e le dita).</li>
<li>Non lasciare il wattmetro inserito sulla linea d'antenna durante i temporali.</li>
<li>Scarica cavi e antenne prima di collegarli.</li></ol></div></div>''')
D.add("Le testine: come trattarle",'''<div class="two"><div><ul>
<li>Dentro ci sono una spira, un diodo e componenti tarati: <b>non aprirle</b> e non smontarle.</li>
<li>Non farle cadere: un urto può spostare la taratura senza segni visibili.</li>
<li>Tienile nella loro custodia o in un contenitore imbottito, al riparo da umidità e polvere.</li>
<li>I <b>contatti</b> (sul fondo e sulla molla di contatto con lo strumento) devono essere puliti: alcool isopropilico e un bastoncino, mai abrasivi.</li></ul></div><div>
<h3>Segnali di testina malata</h3><ul class="small"><li>La lettura cambia ruotando leggermente la testina nella sua sede.</li>
<li>Due testine della stessa banda danno letture molto diverse sullo stesso segnale (oltre le tolleranze).</li>
<li>La lancetta non torna a zero o è "nervosa".</li>
<li>In questi casi confronta con un riferimento e, se serve, falla ritarare in un laboratorio.</li></ul></div></div>''')
D.add("Lo strumento a lancetta",'''<div class="two"><div><ul>
<li>È uno strumento a <b>bobina mobile</b>: sensibile agli urti e ai sovraccarichi, che piegano l'ago o danneggiano le molle.</li>
<li>Controlla sempre lo <b>zero meccanico</b> a riposo, con lo strumento nella posizione in cui lo userai (orizzontale o verticale).</li>
<li>Una lancetta che va spesso a fondo scala con forza perde precisione nel tempo.</li></ul></div><div>
<h3>Trasporto e conservazione</h3><ul class="small"><li>Trasportalo in una valigia imbottita, mai sciolto in auto con altri attrezzi.</li>
<li>Molti strumenti a bobina mobile si proteggono durante il trasporto <b>cortocircuitandone i morsetti</b>: la bobina diventa frenata e l'ago oscilla meno. Fallo solo se lo strumento ha i morsetti accessibili e sai come rimuovere il ponticello.</li>
<li>Tieni i connettori coperti con i tappi.</li>
<li>Evita il sole diretto e gli sbalzi di temperatura: il vetro e le scale si deformano, la taratura del diodo cambia.</li></ul></div></div>''')
D.add("Sensori terminali: i più delicati",'''<div class="two"><div><ul>
<li>Sono <b>molto più delicati</b> delle testine passanti: lavorano con milliwatt.</li>
<li>Leggi la targhetta: <b>potenza massima</b> (spesso intorno a +20 dBm, cioè 100 mW, per molti sensori) e <b>tensione continua massima</b>.</li>
<li>Pochi istanti oltre il limite bastano a bruciare il diodo o la termocoppia; per i bolometri il margine è ancora più piccolo.</li></ul></div><div>
<h3>Regole d'oro</h3><ol class="small"><li>Un <b>attenuatore</b> fisso davanti al sensore se non sei sicuro del livello.</li>
<li>Mai collegarlo a un punto con tensione continua (bias, uscite di amplificatori) senza DC block.</li>
<li>Scaricati a terra prima di toccare il connettore: la statica è il killer silenzioso dei sensori a diodo.</li>
<li>Serraggio corretto dei connettori N e SMA, senza far ruotare il corpo del sensore.</li>
<li>Non tirare il cavo del sensore e non piegarlo vicino al connettore.</li></ol></div></div>''')
D.add("Misurare un trasmettitore senza danni",'''<div class="two"><div><h3>La catena</h3><ol class="small">
<li>TX → wattmetro passante (opzionale) → <b>attenuatore di potenza</b> o carico con prelievo → altri attenuatori → sensore.</li>
<li>L'attenuatore di potenza deve reggere <b>tutta</b> la potenza del TX per tutta la durata della prova (FM e modi digitali: 100 % di duty cycle).</li>
<li>Calcola il livello finale sul sensore e tieni almeno 10 dB di margine.</li></ol>
<div class="eq">+50 dBm (100 W) − 30 dB − 20 dB = 0 dBm sul sensore</div></div><div>
<h3>Sequenza sicura</h3><ul class="small"><li>Collega tutto a TX spento, controlla i connettori.</li>
<li>Prima trasmissione breve e a bassa potenza: verifica che la lettura sia quella attesa.</li>
<li>Poi aumenta la potenza gradualmente.</li>
<li>Tocca gli attenuatori di potenza solo dopo che si sono raffreddati.</li>
<li>Per spegnere: prima la RF, poi scollega.</li></ul></div></div>''')
D.add("Verifiche periodiche",'''<div class="two"><div><ul>
<li><b>Riferimento interno</b>: molti power meter hanno un'uscita da <b>1 mW a 50 MHz</b> per controllare il sensore. Usala ogni volta.</li>
<li><b>Confronto incrociato</b>: due wattmetri passanti in serie sulla stessa linea, con carico buono, devono leggere uguale entro le tolleranze.</li>
<li><b>Confronto tra testine</b>: due testine della stessa banda sullo stesso segnale.</li></ul></div><div><ul>
<li><b>Carico calorimetrico</b> (vedi il modulo sulle misure inconsuete): un controllo indipendente della potenza assoluta.</li>
<li>Tieni un <b>registro</b>: data, segnale, letture. Una deriva lenta si vede solo confrontando nel tempo.</li>
<li>Per misure che devono valere "ufficialmente", la taratura in un laboratorio accreditato resta l'unico riferimento.</li></ul></div></div>''')
rows=["Testina della banda giusta e fondo scala con margine","Nessun collegamento o scollegamento con RF presente","Cavi e antenne scaricati, niente temporali in arrivo","Sensori terminali: attenuatore davanti, niente DC, niente statica",
"Attenuatori di potenza adatti a potenza e durata","Zero controllato, riferimento verificato","Strumenti e testine riposti in custodia, connettori tappati"]
D.add("Checklist",'<table class="sum">'+"".join(f'<tr><td class="l" style="width:46px;color:#22b8f0;font-weight:800">☐</td><td class="l">{r}</td></tr>' for r in rows)+'</table>')
D.render(); pdf("WM_Preservare_IV3HGA.pdf")
