<p align="center"><img src="assets/logo.png" width="180" alt="IV3HGA"></p>

# Ham Radio Pills

🌐 **Sito del corso: https://metallarox.github.io/hamradio-pills/**

Un corso in pillole su strumentazione RF e misure per radioamatori, a cura di **Elia, IV3HGA**: 2 capitoli, 9 moduli, 116 slide.
Ogni modulo è un PDF pronto da leggere o proiettare, accompagnato dai sorgenti Python che lo generano (simulazioni, grafici e slide).

### Capitolo 1 · Il VNA (analizzatore di reti vettoriale)

| Modulo | Presentazione | Slide |
|---|---|---|
| 1 | [Come funziona un VNA](vna/01-vna-come-funziona/VNA_Come_Funziona_IV3HGA.pdf) | 15 |
| 2 | [Misure di base con il VNA](vna/02-vna-misure-di-base/VNA_Misure_di_Base_IV3HGA.pdf) | 13 |
| 3 | [La carta di Smith](vna/03-carta-di-smith/Carta_di_Smith_IV3HGA.pdf) | 13 |
| 4 | [Misurare un quarzo con il VNA](vna/04-quarzo-vna/Quarzo_VNA_IV3HGA.pdf) | 10 |
| 5 | [Misure inconsuete con il VNA](vna/05-vna-misure-inconsuete/VNA_Misure_Inconsuete_IV3HGA.pdf) | 15 |

### Capitolo 2 · L'analizzatore di spettro

| Modulo | Presentazione | Slide |
|---|---|---|
| 1 | [Come funziona l'analizzatore di spettro](analizzatore-di-spettro/01-come-funziona/SA_Come_Funziona_IV3HGA.pdf) | 13 |
| 2 | [Usare bene l'analizzatore: protezioni e impostazioni](analizzatore-di-spettro/02-uso-corretto-e-impostazioni/SA_Uso_Corretto_IV3HGA.pdf) | 12 |
| 3 | [Le misure classiche con l'analizzatore](analizzatore-di-spettro/03-misure-classiche/SA_Misure_Classiche_IV3HGA.pdf) | 12 |
| 4 | [Misure inconsuete e trucchi](analizzatore-di-spettro/04-misure-inconsuete-e-trucchi/SA_Misure_Inconsuete_Trucchi_IV3HGA.pdf) | 13 |

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
