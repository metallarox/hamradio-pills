<p align="center"><img src="logo.png" width="180" alt="IV3HGA"></p>

# Ham Radio Pills

Brevi presentazioni tecniche per radioamatori e appassionati di RF, a cura di **Elia, IV3HGA**.
Ogni "pillola" è un PDF pronto da leggere o proiettare, accompagnato dai sorgenti Python che lo generano (simulazioni, grafici e slide).

| # | Presentazione | Slide | Argomenti |
|---|---|---|---|
| 01 | [Misurare un quarzo con il VNA](01-quarzo-vna/Quarzo_VNA_IV3HGA.pdf) | 10 | Modello BVD, misura in S21 e in S11, estrazione di Rm, Lm, Cm, C0 e Q |
| 02 | [Misure inconsuete con il VNA](02-vna-misure-inconsuete/VNA_Misure_Inconsuete_IV3HGA.pdf) | 15 | Ferriti, SRF/ESR, choke, shunt-through, TDR, εr del PCB, umidità, grid-dip, k, isolamento, time-gating |
| 03 | [Come funziona un VNA](03-vna-come-funziona/VNA_Come_Funziona_IV3HGA.pdf) | 15 | Parametri S, architettura, ricevitori, direttività, modello d'errore, calibrazione SOL/SOLT/TRL |
| 04 | [La carta di Smith](04-carta-di-smith/Carta_di_Smith_IV3HGA.pdf) | 13 | Lettura, movimenti, dipolo, rete a L, stub, linee con perdite, λ/4, accordatore |

## Rigenerare un PDF

Servono Python 3 con `numpy`, `matplotlib`, `scipy`, `Pillow` e `playwright` (Chromium).

```bash
cd 04-carta-di-smith/src     # o un'altra cartella
python3 sims.py              # simulazioni e grafici (sim.py / sim11.py per la 01)
python3 build.py             # genera slides.html
python3 pdf.py               # stampa il PDF in src/
```

I grafici e gli esempi numerici derivano da simulazioni, non da misure reali.

---
73 de IV3HGA
