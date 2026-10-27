"""Genera index.html (pagina del corso) dai dati dei capitoli. Esegui dalla radice del repo: python3 tools/build_site.py"""
import os, html
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CHAPTERS=[
 dict(id="mm",num="Capitolo 1",title="Il multimetro",
  intro="Lo strumento di tutti i giorni, conosciuto davvero: sicurezza, tensione, corrente e shunt, ohm e diodi, funzioni secondarie, funzioni nascoste per esperti ed esempi pratici con i numeri.",
  mods=[
  dict(dir="multimetro/01-introduzione",pdf="MM_Introduzione_IV3HGA.pdf",img="mm-1.jpg",short="Introduzione",title="Il multimetro: introduzione",slides=10,meta="le basi · come leggerlo e sceglierlo",
   learn=['Che cosa misura, analogico e digitale', 'Boccole e selettore: dove va il puntale rosso', '<b>Cifre e conteggi</b>: 2000, 6000, 50 000', '<b>Risoluzione e precisione</b>: ±(% lettura + digit) con esempi', 'Valore medio e <b>true RMS</b>, autorange, come scegliere un multimetro'],
   tags=['conteggi', 'precisione', 'true RMS', 'boccole', 'autorange']),
  dict(dir="multimetro/02-sicurezza",pdf="MM_Sicurezza_IV3HGA.pdf",img="mm-2.jpg",short="Sicurezza",title="Il multimetro: sicurezza",slides=10,meta="non farsi male",
   learn=['Categorie <b>CAT</b> e sovratensioni transitorie', "L'errore più pericoloso: il puntale nella <b>boccola di corrente</b>", 'Fusibili HRC e il trucco per controllarli senza aprire', 'Puntali, metodo <b>live-dead-live</b>, tensioni fantasma e NCV', 'Le situazioni tipiche della stazione radio'],
   tags=['CAT', 'fusibili HRC', 'live-dead-live', 'LoZ', 'stazione radio']),
  dict(dir="multimetro/03-tensione",pdf="MM_Tensione_IV3HGA.pdf",img="mm-3.jpg",short="Tensione",title="Misurare la tensione",slides=10,meta="impedenza d'ingresso, true RMS, ripple",
   learn=['Il collegamento in parallelo e lo strumento flottante', "<b>Impedenza d'ingresso</b> ed effetto di carico, con numeri", 'Tensioni fantasma e <b>LoZ</b>', 'Valore medio contro <b>true RMS</b>: errori su quadra, triangolare, impulsi', 'Fattore di cresta, banda AC e il <b>ripple</b> letto con il multimetro'],
   tags=['10 MΩ', 'effetto di carico', 'LoZ', 'true RMS', 'ripple']),
  dict(dir="multimetro/04-corrente-e-shunt",pdf="MM_Corrente_Shunt_IV3HGA.pdf",img="mm-4.jpg",short="Corrente e shunt",title="Misurare la corrente e gli shunt",slides=11,meta="burden, shunt, corrente letta in tensione",
   learn=['Il collegamento in serie e lo <b>shunt interno</b>', '<b>Burden voltage</b>: quando la misura cambia il circuito', '<b>Leggere una corrente in modalità tensione</b> su una resistenza nota', 'Shunt esterni, cavi e piste usati come shunt, pinze amperometriche', 'Il multimetro come nanoamperometro e le correnti di sleep'],
   tags=['shunt', 'burden', 'I = V/R', 'pinze', 'nA']),
  dict(dir="multimetro/05-resistenza-continuita-diodi",pdf="MM_Resistenza_Diodi_IV3HGA.pdf",img="mm-5.jpg",short="Ohm e diodi",title="Resistenza, continuità e prova diodi",slides=11,meta="ohm, 4 fili, diodi, transistor e MOSFET",
   learn=['Come misura gli ohm, <b>REL</b> e misura a <b>4 fili</b>', 'Misure in circuito e resistenze alte', '<b>Continuità</b>: coassiali e antenne (il corto che è normale)', '<b>Prova diodi</b>: Si, Schottky, germanio, LED', 'Provare <b>transistor</b> e <b>MOSFET</b>, e altri componenti'],
   tags=['REL', '4 fili', 'continuità', 'prova diodi', 'BJT', 'MOSFET']),
  dict(dir="multimetro/06-capacita-frequenza-hfe-temperatura",pdf="MM_Capacita_Frequenza_hFE_Temperatura_IV3HGA.pdf",img="mm-6.jpg",short="Capacità, Hz, hFE, °C",title="Capacità, frequenza, hFE e temperatura",slides=9,meta="le funzioni secondarie, con usi pratici",
   learn=['Come misura la <b>capacità</b> e i suoi limiti (ESR!)', 'Trucco: la <b>lunghezza di un coassiale</b> dalla sua capacità', 'Frequenza e duty cycle: controllare un <b>CTCSS</b>', '<b>hFE</b> allo zoccolo e in condizioni reali', 'Temperatura con termocoppia e altre funzioni'],
   tags=['capacità', 'coassiale', 'CTCSS', 'hFE', 'termocoppia']),
  dict(dir="multimetro/07-funzioni-nascoste-e-trucchi",pdf="MM_Funzioni_Nascoste_Trucchi_IV3HGA.pdf",img="mm-7.jpg",short="Funzioni nascoste",title="Funzioni nascoste e trucchi da esperti",slides=11,meta="tips and tricks per esperti",
   learn=['<b>REL</b>, <b>MIN/MAX/AVG</b>, peak, hold, bargraph e logging', '<b>Resistenza interna</b> di batterie e alimentatori', '<b>Caduta di tensione sotto carico</b> su cavi e connettori', 'Controllare un <b>fusibile in circuito</b>', 'La <b>sonda RF a diodo</b> e altri trucchi da stazione'],
   tags=['MIN/MAX', 'R interna', 'caduta di tensione', 'sonda RF', 'ground loop']),
  dict(dir="multimetro/08-esempi-pratici-ed-errori",pdf="MM_Esempi_Errori_IV3HGA.pdf",img="mm-8.jpg",short="Esempi ed errori",title="Esempi pratici ed errori di misura",slides=10,meta="quanto fidarsi di una misura",
   learn=['Da dove vengono gli errori e come combinarli', 'Quattro <b>esempi numerici</b>: tensione, corrente di riposo, milliohm, AC', 'Errori subdoli: termocoppie parassite, batteria, RF', '<b>Ricerca guasti</b> in stazione: tre casi', 'Manutenzione dello strumento e prontuario finale'],
   tags=['incertezza', 'esempi', 'ricerca guasti', 'manutenzione']),
  ]),
 dict(id="osc",num="Capitolo 2",title="L'oscilloscopio",
  intro="Lo strumento da cui partire: come funziona, come usarlo senza farsi male né romperlo, le sonde, le misure classiche, gli errori da evitare e i trucchi da banco.",
  mods=[
  dict(dir="oscilloscopio/01-come-funziona",pdf="OSC_Come_Funziona_IV3HGA.pdf",img="osc-1.jpg",short="Come funziona",title="L'oscilloscopio: come funziona",slides=10,meta="le basi · analogico e digitale",
   learn=["Analogico e digitale, lo <b>schema a blocchi</b> di un DSO","<b>Banda</b> e tempo di salita: t<sub>s</sub> ≈ 0,35 / banda","<b>Campionamento</b>, aliasing e il legame tra memoria e sample rate","Il <b>trigger</b> e i modi di acquisizione (peak detect, average, persistenza)","Le specifiche che contano"],
   tags=["DSO","banda","sample rate","aliasing","trigger","memoria"]),
  dict(dir="oscilloscopio/02-sicurezza-e-protezione",pdf="OSC_Sicurezza_Protezione_IV3HGA.pdf",img="osc-2.jpg",short="Sicurezza",title="Oscilloscopio: sicurezza e protezione",slides=9,meta="non farsi male · non romperlo",
   learn=["La <b>clip di massa è collegata a terra</b>: il cortocircuito sulla rete","Perché non si toglie <b>mai</b> la terra, e cosa usare invece","Limiti degli ingressi a 1 MΩ e a 50 Ω, categorie CAT, derating delle sonde","Oscilloscopio e <b>trasmettitori</b>: tensioni su 50 Ω e attenuatori","Tensioni nascoste, condensatori carichi e regole d'oro"],
   tags=["massa a terra","sonda differenziale","CAT","50 Ω","alta tensione"]),
  dict(dir="oscilloscopio/03-sonde-e-impostazioni",pdf="OSC_Sonde_Impostazioni_IV3HGA.pdf",img="osc-3.jpg",short="Sonde e impostazioni",title="Sonde e impostazioni",slides=10,meta="la sonda giusta, impostata bene",
   learn=["La sonda passiva <b>10×</b> e la <b>compensazione</b>","Quanto la sonda <b>carica</b> il circuito: 159 Ω a 100 MHz","La <b>massa corta</b> e le oscillazioni finte del cavetto","Sonde attive, differenziali, di corrente e per alta tensione","Impostare verticale, base dei tempi e trigger con un metodo"],
   tags=["sonda 10×","compensazione","carico","molla di massa","trigger"]),
  dict(dir="oscilloscopio/04-misure-classiche",pdf="OSC_Misure_Classiche_IV3HGA.pdf",img="osc-4.jpg",short="Misure classiche",title="Le misure con l'oscilloscopio",slides=10,meta="come farle bene e quanto fidarsi",
   learn=["<b>Cursori</b> e misure automatiche: quando fidarsi","Ampiezza, frequenza, periodo e duty cycle","<b>Tempo di salita</b> e correzione per lo strumento","<b>Fase</b> tra due segnali e modalità <b>XY</b> (Lissajous)","Modulazione AM con <b>inviluppo e trapezio</b>, FFT, correnti e potenza"],
   tags=["cursori","rise time","fase","XY","trapezio AM","FFT"]),
  dict(dir="oscilloscopio/05-come-non-usarlo",pdf="OSC_Come_Non_Usarlo_IV3HGA.pdf",img="osc-5.jpg",short="Come non usarlo",title="Come NON usare l'oscilloscopio",slides=10,meta="nove errori classici e come evitarli",
   learn=["Immagini ingannevoli: <b>aliasing</b> e banda insufficiente","Fattore sonda sbagliato e sonde scompensate","<b>Masse</b> nel punto sbagliato e due masse su punti diversi","Accoppiamento <b>AC</b> dove serve DC; 1 MΩ al posto di 50 Ω","Autoset e misure automatiche alla cieca; lo strumento sbagliato"],
   tags=["errori","aliasing","masse","AC/DC","50 Ω","autoset"]),
  dict(dir="oscilloscopio/06-misure-inconsuete-e-trucchi",pdf="OSC_Misure_Inconsuete_Trucchi_IV3HGA.pdf",img="osc-6.jpg",short="Inconsuete e trucchi",title="Misure inconsuete e trucchi",slides=11,meta="tips and tricks da banco",
   learn=["Il <b>ripple</b> dei condensatori di filtro in accoppiamento AC, ESR e invecchiamento","Misure differenziali <b>A − B</b> e corrente di spunto con trigger single","<b>Prova componenti</b> in modalità XY","<b>TDR</b> con generatore, T e oscilloscopio","PTT, burst TDMA, inviluppo CW e altri trucchi (line trigger, sonda-spira)"],
   tags=["ripple","ESR","A − B","XY tester","TDR","key click"])]),
 dict(id="vna",num="Capitolo 3",title="Il VNA (analizzatore di reti vettoriale)",
  intro="Dallo strumento alle applicazioni: come funziona, come si usa e si calibra, la carta di Smith e le misure più particolari.",
  mods=[
  dict(dir="vna/01-vna-come-funziona",pdf="VNA_Come_Funziona_IV3HGA.pdf",img="vna-1.jpg",short="Come funziona un VNA",title="Come funziona un VNA",slides=15,meta="le basi · consigliato come punto di partenza",
   learn=["Cosa sono le onde incidenti e riflesse e i <b>parametri S</b>","Com'è fatto dentro: sorgente, ponte o accoppiatore, ricevitori R/A/B, LO e DSP","Perché la <b>direttività</b> limita quello che puoi misurare","Il modello d'errore a 3 e 12 termini e come la <b>calibrazione SOL</b> lo cancella","SOLT, TRL, port extension, buone pratiche e specifiche che contano"],
   tags=["parametri S","IF bandwidth","direttività","calibrazione","T/R vs 2 porte"]),
  dict(dir="vna/02-vna-misure-di-base",pdf="VNA_Misure_di_Base_IV3HGA.pdf",img="vna-2.jpg",short="Misure di base",title="Misure di base con il VNA",slides=13,meta="pratica sul banco · uso, calibrazione e misure corrette",
   learn=["Preparare cavi e connettori e <b>proteggere lo strumento</b> (statica, potenze, DC)","Impostare lo sweep: punti, IF bandwidth, potenza, media","<b>Calibrare</b> al piano giusto e <b>verificare</b> che la calibrazione sia buona","Misurare un'<b>antenna</b>, un <b>filtro</b>, un <b>cavo</b> (perdita, VF, Z0), un amplificatore e un componente","Gli errori più comuni e una checklist da usare prima di ogni misura"],
   tags=["calibrazione","verifica","antenne","filtri","cavi coassiali","amplificatori"]),
  dict(dir="vna/03-carta-di-smith",pdf="Carta_di_Smith_IV3HGA.pdf",img="vna-3.jpg",short="La carta di Smith",title="La carta di Smith",slides=13,meta="6 esempi radioamatoriali",
   learn=["Leggere impedenze, |Γ| e SWR a colpo d'occhio","Muoversi sulla carta con L e C in serie e in parallelo, e lungo le linee","Capire se un <b>dipolo</b> è troppo lungo o troppo corto","Progettare una <b>rete a L</b> e uno <b>stub</b> di adattamento","Perché un cavo con perdite \"migliora\" l'SWR, il λ/4 e cosa fa davvero l'accordatore"],
   tags=["SWR","dipolo 40 m","rete a L","stub 145 MHz","stacking","ATU"]),
  dict(dir="vna/04-quarzo-vna",pdf="Quarzo_VNA_IV3HGA.pdf",img="vna-4.jpg",short="Misurare un quarzo",title="Misurare un quarzo con il VNA",slides=10,meta="un'applicazione completa, passo per passo",
   learn=["Il modello equivalente <b>Butterworth–Van Dyke</b>: fs, fp, Rm, Lm, Cm, C0","Misura con il quarzo <b>in serie (S21)</b> e verso massa <b>(S11)</b>","Estrazione dei parametri dai punti di fase a <b>±45°</b> e calcolo del Q","Pi-network da 12,5 Ω, parassiti del fixture e frequenza con capacità di carico"],
   tags=["quarzi","modello BVD","Q a vuoto","S21 e S11","IEC 60444"]),
  dict(dir="vna/05-vna-misure-inconsuete",pdf="VNA_Misure_Inconsuete_IV3HGA.pdf",img="vna-5.jpg",short="Misure inconsuete",title="Misure inconsuete con il VNA",slides=15,meta="12 misure oltre SWR e filtri",
   learn=["<b>Ferriti</b> sconosciute, SRF/ESR dei componenti, choke in modo comune","<b>Shunt-through</b> per i milliohm e group delay di risonatori e cavità","<b>TDR</b> per trovare guasti nei cavi, εr e tan δ di un PCB, umidità dei materiali","Grid-dip moderno e NFC, accoppiamento k, isolamento tra antenne, schermatura, time-gating"],
   tags=["ferriti","TDR","choke","PCB εr","grid-dip","time-gating"])]),
 dict(id="sa",num="Capitolo 4",title="L'analizzatore di spettro",
  intro="Come funziona, come usarlo senza romperlo, le misure classiche fatte bene, carichi con prelievo, accoppiatori e ponti, e i trucchi che non trovi nei manuali.",
  mods=[
  dict(dir="analizzatore-di-spettro/01-come-funziona",pdf="SA_Come_Funziona_IV3HGA.pdf",img="sa-1.jpg",short="Come funziona",title="Come funziona l'analizzatore di spettro",slides=13,meta="le basi · supereterodina, RBW, rivelatori",
   learn=["Unità di misura: dBm, dBµV, dBc, dBm/Hz e livelli S9","L'architettura <b>supereterodina a scansione</b> e le frequenze immagine","<b>RBW</b> e VBW: risoluzione, rumore e tempo di sweep","Rivelatori, attenuatore d'ingresso e <b>livello al mixer</b> ottimale","Rumore di fondo, rumore di fase, dinamica, FFT/real-time e tracking generator"],
   tags=["supereterodina","RBW","VBW","rivelatori","DANL","dinamica"]),
  dict(dir="analizzatore-di-spettro/02-uso-corretto-e-impostazioni",pdf="SA_Uso_Corretto_IV3HGA.pdf",img="sa-2.jpg",short="Uso corretto e protezioni",title="Usare bene l'analizzatore: protezioni e impostazioni",slides=12,meta="non rompere lo strumento · impostare le misure",
   learn=["Perché gli analizzatori si rompono: <b>DC</b>, sovraccarichi, <b>spike</b>, statica","Leggere l'etichetta dell'ingresso e costruire la <b>catena di protezione</b>","Misurare un <b>trasmettitore</b> in sicurezza: budget di potenza e campionatori","Reference level, offset, RBW/VBW, tracce e marker scelti per l'obiettivo","Controllare la salute dello strumento e una checklist finale"],
   tags=["DC block","limitatore","attenuatori","reference offset","marker","checklist"]),
  dict(dir="analizzatore-di-spettro/03-misure-classiche",pdf="SA_Misure_Classiche_IV3HGA.pdf",img="sa-3.jpg",short="Misure classiche",title="Le misure classiche con l'analizzatore",slides=12,meta="9 misure spiegate passo per passo",
   learn=["Potenza e frequenza di una portante, <b>armoniche</b> e spurie di un TX","<b>Intermodulazione</b> a due toni e calcolo del TOI","Profondità <b>AM</b> dalle bande laterali e deviazione <b>FM</b> con il nullo di Bessel","Potenza di canale, OBW e ACP; <b>zero span</b> per i burst TDMA","Tracking generator per filtri e duplexer, rumore di fase in dBc/Hz"],
   tags=["armoniche","IM3 / TOI","AM","FM Bessel","zero span","rumore di fase"]),
  dict(dir="analizzatore-di-spettro/04-prelievi-accoppiatori-ponti",pdf="SA_Prelievi_Accoppiatori_Ponti_IV3HGA.pdf",img="sa-4.jpg",short="Prelievi, accoppiatori, ponti",title="Carico con prelievo, accoppiatore e ponte",slides=14,meta="misure sul trasmettitore e di adattamento",
   learn=["Il <b>carico con prelievo</b>: budget di potenza, durata e SWR del carico","Perché un prelievo capacitivo <b>sovrastima le armoniche</b> e come calibrarlo","L'<b>accoppiatore direzionale</b>: spettro in servizio, return loss sotto potenza, segnali dall'antenna","Il <b>ponte riflettometrico</b> con tracking generator: return loss, direttività e distanza delle discontinuità","Test a due toni su un TX SSB e cosa si vede: splatter, key click, ALC, autooscillazioni"],
   tags=["carico fittizio","prelievo","accoppiatore","direttività","ponte RL","two-tone"]),
  dict(dir="analizzatore-di-spettro/05-misure-inconsuete-e-trucchi",pdf="SA_Misure_Inconsuete_Trucchi_IV3HGA.pdf",img="sa-5.jpg",short="Inconsuete e trucchi",title="Misure inconsuete e trucchi",slides=13,meta="tips and tricks da banco",
   learn=["Capire se una riga è <b>vera</b>: test dell'attenuazione e altri tre controlli","Misurare vicino al rumore e la <b>cifra di rumore</b> con il metodo Y-factor","<b>Sonde near-field</b> per la caccia al QRM e misure di campo in dBµV/m","Ascoltare i segnali, <b>slope detection</b> della FM e il trucco della RBW","Più dinamica con notch e filtri, riferimento a 10 MHz e altri trucchi"],
   tags=["righe false","Y-factor","near-field","QRM","slope detection","dBµV/m"])]),
 dict(id="gen",num="Capitolo 5",title="Il generatore di segnali RF",
  intro="Il compagno dell'analizzatore: come funziona, livelli e attenuatori, modulazioni, purezza spettrale e i test di sensibilità, selettività e dinamica dei ricevitori.",
  mods=[
  dict(dir="generatore-rf/01-come-funziona",pdf="GEN_Come_Funziona_IV3HGA.pdf",img="gen-1.jpg",short="Come funziona",title="Il generatore RF: come funziona",slides=9,meta="le basi · architettura e specifiche",
   learn=["A cosa serve: il compagno dell'analizzatore", '<b>Architettura</b>: riferimento, PLL/DDS, modulatore, ALC, attenuatore', 'Il <b>riferimento a 10 MHz</b> e la precisione in frequenza', 'Protezione dalla potenza inversa, tipi di generatori e specifiche'],
   tags=['PLL', 'DDS', 'OCXO', 'ALC', 'attenuatore']),
  dict(dir="generatore-rf/02-livelli-e-attenuatori",pdf="GEN_Livelli_Attenuatori_IV3HGA.pdf",img="gen-2.jpg",short="Livelli e attenuatori",title="Livelli e attenuatori",slides=9,meta="dBm, µV, EMF e PD",
   learn=['Tabella <b>dBm, µV e dBµV</b> su 50 Ω', '<b>EMF e PD</b>: il fattore 2 nei datasheet', 'Attenuatori a π e T con le resistenze calcolate', 'Perdite, combinatori, <b>leakage</b> e livelli tipici dei test'],
   tags=['dBm', 'µV', 'EMF/PD', 'attenuatori', 'leakage']),
  dict(dir="generatore-rf/03-modulazioni",pdf="GEN_Modulazioni_IV3HGA.pdf",img="gen-3.jpg",short="Modulazioni",title="Le modulazioni del generatore",slides=8,meta="AM, FM, impulsi, esterna",
   learn=['Le <b>convenzioni dei test</b>: 1 kHz, 3 kHz di deviazione, 30 % AM', '<b>AM</b>: profondità, bande laterali, picchi', '<b>FM</b> e ΦM: deviazione e verifica con il nullo di Bessel', 'Impulsi, modulazione esterna e segnali per test speciali'],
   tags=['AM', 'FM', 'ΦM', 'impulsi', 'CTCSS']),
  dict(dir="generatore-rf/04-purezza-spettrale",pdf="GEN_Purezza_Spettrale_IV3HGA.pdf",img="gen-4.jpg",short="Purezza spettrale",title="La purezza spettrale",slides=9,meta="armoniche, spurie, rumore di fase",
   learn=['Perché il generatore deve essere <b>10 dB migliore</b> del ricevitore', '<b>Armoniche</b> e <b>spurie</b>: quando sono innocue e quando no', '<b>Rumore di fase</b>: quanto ne finisce nel canale del ricevitore', 'Come verificare e migliorare il tuo generatore'],
   tags=['armoniche', 'spurie', 'rumore di fase', 'filtri']),
  dict(dir="generatore-rf/05-sensibilita-sinad-mds",pdf="GEN_Sensibilita_SINAD_MDS_IV3HGA.pdf",img="gen-5.jpg",short="Sensibilità",title="Test di sensibilità: SINAD e MDS",slides=10,meta="passo per passo, con esempi",
   learn=['Che cosa vuol dire <b>sensibilità</b> e perché serve la condizione', '<b>SINAD 12 dB</b> in FM: setup, procedura ed esempio a 145 MHz', 'S/N 10 dB in <b>AM e SSB</b>', '<b>MDS</b> e cifra di rumore; errori tipici'],
   tags=['SINAD', '12 dB', 'S/N', 'MDS', 'NF']),
  dict(dir="generatore-rf/06-selettivita-e-dinamica",pdf="GEN_Selettivita_Dinamica_IV3HGA.pdf",img="gen-6.jpg",short="Selettività e dinamica",title="Selettività e dinamica del ricevitore",slides=9,meta="con due generatori",
   learn=['Il <b>setup con due generatori</b> e combinatore', '<b>Canale adiacente</b> in FM', '<b>Blocking</b> e <b>reciprocal mixing</b>', 'Intermodulazione: <b>DR3 e IP3</b> con esempio; frequenza immagine'],
   tags=['canale adiacente', 'blocking', 'reciprocal mixing', 'DR3', 'IP3']),
  dict(dir="generatore-rf/07-usi-pratici-e-trucchi",pdf="GEN_Usi_Pratici_Trucchi_IV3HGA.pdf",img="gen-7.jpg",short="Usi pratici",title="Usi pratici e trucchi",slides=9,meta="sul banco e in stazione",
   learn=["Tarare l'<b>S-meter</b> con la convenzione IARU", 'Allineare filtri e IF; <b>iniezione di segnale</b> per la ricerca guasti', '<b>Proteggere il generatore</b> nelle prove sui ricetrasmettitori', 'Generatore e analizzatore insieme, altri trucchi ed errori da evitare'],
   tags=['S-meter', 'allineamento', 'iniezione', 'protezione']),
  ]),
 dict(id="wm",num="Capitolo 6",title="Il wattmetro RF",
  intro="Come funziona e quali tipi esistono, il Bird 43 con le sue testine, bolometri e termistori, come preservarlo, i problemi di misura e la matematica della potenza.",
  mods=[
  dict(dir="wattmetro-rf/01-come-funziona",pdf="WM_Come_Funziona_IV3HGA.pdf",img="wm-1.jpg",short="Come funziona",title="Il wattmetro RF: come funziona",slides=10,meta="le basi · tipi di wattmetri e di sensori",
   learn=["Che cosa vuol dire misurare la <b>potenza</b> in RF: P = V²/R, dBm e tensioni","Wattmetri <b>passanti</b> (direzionali) e <b>terminali</b> (sensore + carico)","Sensori a <b>diodo</b>, termocoppia, <b>termistore</b>, <b>bolometro</b> e calorimetro a confronto","Potenza media, di picco e <b>PEP</b>, e le specifiche da leggere"],
   tags=["passante","terminale","diodo","termocoppia","termistore","PEP"]),
  dict(dir="wattmetro-rf/02-bird-43-e-testine",pdf="WM_Bird43_Testine_IV3HGA.pdf",img="wm-2.jpg",short="Il Bird 43",title="Il Bird 43 e le sue testine",slides=9,meta="esempio pratico · misure passo per passo",
   learn=["Come funziona un wattmetro passante con <b>testina</b> rotante","Le testine: <b>lettera = banda</b>, numero = fondo scala","Misurare potenza <b>diretta</b>, <b>riflessa</b>, SWR e potenza netta","Perché la precisione è in % del <b>fondo scala</b>; esempio a 145 MHz","Modulazioni, lettura di picco ed errori tipici"],
   tags=["Bird 43","testine","diretta/riflessa","SWR","fondo scala"]),
  dict(dir="wattmetro-rf/03-bolometri-e-termistori",pdf="WM_Bolometri_Termistori_IV3HGA.pdf",img="wm-3.jpg",short="Bolometri e termistori",title="Bolometri e termistori",slides=11,meta="sostituzione DC e misure di precisione",
   learn=["Il principio: la RF scalda, la <b>continua</b> la sostituisce","Il <b>ponte autobilanciato</b> e la formula con un esempio numerico","Compensazione, azzeramento e un classico: l'HP 432A","<b>Cal factor</b> e incertezza di <b>disadattamento</b>","Il bolometro (barretter) e perché oggi è raro"],
   tags=["termistore","bolometro","sostituzione DC","cal factor","HP 432A"]),
  dict(dir="wattmetro-rf/04-preservare-il-wattmetro",pdf="WM_Preservare_IV3HGA.pdf",img="wm-4.jpg",short="Preservarlo",title="Preservare il wattmetro",slides=9,meta="non romperlo · non farlo leggere sbagliato",
   learn=["Limiti di <b>potenza e tensione</b> dei wattmetri passanti","Come trattare <b>testine</b> e strumento a lancetta, trasporto e conservazione","<b>Sensori terminali</b>: attenuatori, DC, statica, connettori","Misurare un TX senza danni e <b>verifiche periodiche</b>"],
   tags=["protezione","testine","sensori","statica","verifiche"]),
  dict(dir="wattmetro-rf/05-misure-inconsuete-e-problemi",pdf="WM_Misure_Inconsuete_Problemi_IV3HGA.pdf",img="wm-5.jpg",short="Inconsuete e problemi",title="Misure inconsuete e problemi di misura",slides=11,meta="quando il wattmetro sbaglia · cosa misurare oltre ai watt",
   learn=["<b>Armoniche</b>, <b>modulazione</b> (media e PEP) e segnali a <b>burst</b> TDMA","Disadattamento, direttività, cavi e adattatori","Perdita di un cavo con uno o due wattmetri e <b>calorimetria</b>","Efficienza di un finale e <b>SWR vero all'antenna</b> dalla stazione"],
   tags=["PEP","TDMA","perdita cavi","calorimetria","efficienza"]),
  dict(dir="wattmetro-rf/06-potenza-segnale-spettro-bessel",pdf="Potenza_Segnale_Spettro_Bessel_IV3HGA.pdf",img="wm-6.jpg",short="Potenza e Bessel",title="Potenza del segnale e potenza dello spettro",slides=14,meta="approfondimento matematico con esempi concreti",
   learn=["Il teorema di <b>Parseval</b>: il ponte tra wattmetro e analizzatore","<b>AM</b>: portante, bande laterali, media e PEP con i numeri","<b>SSB</b> a due toni: PEP = 2 × media","<b>FM</b> e funzioni di <b>Bessel</b>: la potenza si ridistribuisce, non cambia","Regola di Carson, densità spettrale e RBW, somme in dB, fattore di cresta"],
   tags=["Parseval","AM","SSB","FM","Bessel","Carson","PAPR"])])]
CSS=open(os.path.join(ROOT,"tools/site.css")).read()
nmod=sum(len(c["mods"]) for c in CHAPTERS); nsl=sum(m["slides"] for c in CHAPTERS for m in c["mods"])
def mod_html(c,i,m):
    href=f'{m["dir"]}/{m["pdf"]}'
    return f'''<article class="mod" id="{c["id"]}{i}">
      <a class="shot" href="{href}"><img src="assets/{m["img"]}" alt="Anteprima: {html.escape(m["title"])}" loading="lazy"></a>
      <div><div class="num">{c["num"]} · Modulo {i}</div><h3>{m["title"]}</h3><div class="meta">{m["slides"]} slide · {m["meta"]}</div>
        <ul>{"".join(f"<li>{x}</li>" for x in m["learn"])}</ul>
        <div class="tags">{"".join(f"<span>{t}</span>" for t in m["tags"])}</div>
        <div class="btns"><a class="btn primary" href="{href}" download>⬇ Scarica PDF</a><a class="btn ghost" href="{href}" target="_blank" rel="noopener">Apri nel browser</a></div></div>
    </article>'''
chap=""
for c in CHAPTERS:
    n=len(c["mods"])
    steps="".join(f'<a class="step" href="#{c["id"]}{i+1}"><small>Modulo {i+1}</small><div>{m["short"]}</div></a>' for i,m in enumerate(c["mods"]))
    chap+=f'''<section class="chapter" id="{c["id"]}"><div class="wrap">
  <div class="chap-head"><span class="chap-num">{c["num"]}</span><h2>{c["title"]}</h2></div>
  <p class="sub">{c["intro"]} {n} moduli, {sum(m["slides"] for m in c["mods"])} slide.</p>
  <div class="path p{n}">{steps}</div>
  {"".join(mod_html(c,i+1,m) for i,m in enumerate(c["mods"]))}
</div></section>'''
toc="".join(f'<a href="#{c["id"]}"><small>{c["num"]}</small><h3>{c["title"]}</h3><p>{c["intro"]}</p></a>' for c in CHAPTERS)
page=f'''<!DOCTYPE html>
<html lang="it"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Ham Radio Pills · Corso su multimetro, oscilloscopio, VNA, analizzatore di spettro, wattmetro RF · IV3HGA</title>
<meta name="description" content="Corso gratuito per radioamatori: multimetro, oscilloscopio, VNA, carta di Smith, analizzatore di spettro, wattmetro RF e misure. {len(CHAPTERS)} capitoli, {nmod} moduli in PDF. A cura di IV3HGA.">
<link rel="icon" href="assets/logo.png"><style>{CSS}</style></head><body>
<header class="hero"><div class="wrap"><div>
  <span class="kicker">Corso · RF e strumentazione per radioamatori</span>
  <h1>Ham Radio <span>Pills</span></h1>
  <p class="lead">Un corso in pillole per capire davvero gli strumenti da banco e usarli sull'antenna e sul trasmettitore: il multimetro, l'oscilloscopio, il VNA e la carta di Smith, l'analizzatore di spettro, il generatore RF e il wattmetro RF, dalle basi ai trucchi del mestiere.</p>
  <div class="btns"><a class="btn primary" href="#capitoli">Inizia il corso ↓</a><a class="btn ghost" href="https://github.com/metallarox/hamradio-pills">Sorgenti su GitHub</a></div>
  <div class="stats"><div><b>{len(CHAPTERS)}</b>capitoli</div><div><b>{nmod}</b>moduli</div><div><b>{nsl}</b>slide</div><div><b>PDF</b>gratuiti</div></div>
</div><img src="assets/logo.png" alt="Logo IV3HGA"></div></header>
<section id="capitoli" style="padding-bottom:20px"><div class="wrap"><h2>I capitoli</h2>
<p class="sub">Ogni capitolo parte da come funziona lo strumento, passa all'uso corretto e arriva alle misure avanzate. I moduli si possono leggere anche da soli.</p>
<div class="toc">{toc}</div></div></section>
{chap}
<section class="info"><div class="wrap"><h2>Come seguire il corso</h2>
<p class="sub">Non serve un laboratorio: bastano strumenti economici e la voglia di provare sul banco quello che leggi.</p>
<div class="grid3">
<div class="card"><h4>📡 Cosa serve</h4><p>Un buon multimetro true RMS, un oscilloscopio con sonde 10×, un VNA anche economico (NanoVNA, LiteVNA o simili) con kit SOL, un analizzatore di spettro (anche un tinySA), un generatore RF, un wattmetro passante, un carico fittizio, attenuatori, un DC block e qualche cavo.</p></div>
<div class="card"><h4>🧭 Come procedere</h4><p>Leggi un modulo, poi rifai la misura sul banco. Ogni presentazione ha formule pronte, esempi numerici e checklist finali.</p></div>
<div class="card"><h4>🧪 Esempi e sorgenti</h4><p>Grafici ed esempi vengono da simulazioni verificate. Gli script Python che generano slide e grafici sono nel repository: modificali per i tuoi casi.</p></div>
</div></div></section>
<footer><div class="wrap"><div><b>Ham Radio Pills</b> · a cura di Elia, IV3HGA · 73!</div><div><a href="https://github.com/metallarox/hamradio-pills">github.com/metallarox/hamradio-pills</a></div></div></footer>
</body></html>'''
open(os.path.join(ROOT,"index.html"),"w").write(page)
# README
rows=""
for c in CHAPTERS:
    rows+=f"\n### {c['num']} · {c['title']}\n\n| Modulo | Presentazione | Slide |\n|---|---|---|\n"
    for i,m in enumerate(c["mods"]):
        rows+=f"| {i+1} | [{m['title']}]({m['dir']}/{m['pdf']}) | {m['slides']} |\n"
readme=f'''<p align="center"><img src="assets/logo.png" width="180" alt="IV3HGA"></p>

# Ham Radio Pills

🌐 **Sito del corso: https://metallarox.github.io/hamradio-pills/**

Un corso in pillole su strumentazione RF e misure per radioamatori, a cura di **Elia, IV3HGA**: {len(CHAPTERS)} capitoli, {nmod} moduli, {nsl} slide.
Ogni modulo è un PDF pronto da leggere o proiettare, accompagnato dai sorgenti Python che lo generano (simulazioni, grafici e slide).
{rows}
## Rigenerare un PDF

Servono Python 3 con `numpy`, `matplotlib`, `scipy`, `Pillow` e `playwright` (Chromium).

```bash
cd analizzatore-di-spettro/01-come-funziona/src   # o un'altra cartella src
python3 sims.py      # simulazioni e grafici, se presente (sim.py / sim11.py per il quarzo)
python3 build.py     # genera slides.html (e nei moduli dell'analizzatore anche il PDF)
python3 pdf.py       # stampa il PDF, nei moduli che hanno questo script
```

La pagina del corso si rigenera con `python3 tools/build_site.py`.

I grafici e gli esempi numerici derivano da simulazioni, non da misure reali.

---
73 de IV3HGA
'''
open(os.path.join(ROOT,"README.md"),"w").write(readme)
print(nmod,nsl)
