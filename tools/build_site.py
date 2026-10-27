"""Genera index.html (pagina del corso) dai dati dei capitoli. Esegui dalla radice del repo: python3 tools/build_site.py"""
import os, html
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CHAPTERS=[
 dict(id="vna",num="Capitolo 1",title="Il VNA (analizzatore di reti vettoriale)",
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
 dict(id="sa",num="Capitolo 2",title="L'analizzatore di spettro",
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
   tags=["righe false","Y-factor","near-field","QRM","slope detection","dBµV/m"])])]
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
<title>Ham Radio Pills · Corso su VNA, analizzatore di spettro e misure RF · IV3HGA</title>
<meta name="description" content="Corso gratuito per radioamatori: VNA, carta di Smith, analizzatore di spettro e misure RF. {len(CHAPTERS)} capitoli, {nmod} moduli in PDF. A cura di IV3HGA.">
<link rel="icon" href="assets/logo.png"><style>{CSS}</style></head><body>
<header class="hero"><div class="wrap"><div>
  <span class="kicker">Corso · RF e strumentazione per radioamatori</span>
  <h1>Ham Radio <span>Pills</span></h1>
  <p class="lead">Un corso in pillole per capire davvero gli strumenti da banco e usarli sull'antenna e sul trasmettitore: il VNA e la carta di Smith, l'analizzatore di spettro, dalle basi ai trucchi del mestiere.</p>
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
<div class="card"><h4>📡 Cosa serve</h4><p>Un VNA anche economico (NanoVNA, LiteVNA o simili) con kit SOL, un analizzatore di spettro (anche un tinySA), attenuatori, un DC block e qualche cavo SMA.</p></div>
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
