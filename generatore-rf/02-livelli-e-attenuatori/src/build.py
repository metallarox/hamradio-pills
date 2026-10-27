import math
from deck import *
D=Deck("Livelli<br>e attenuatori","dBm e µV, tensione a vuoto (EMF) e su carico (PD), conversioni, attenuatori fissi e pad di adattamento, perdite dei cavi, combinatori e livelli tipici dei test radioamatoriali","Il generatore RF: livelli e attenuatori")
def dbm_uv(d): return math.sqrt(10**(d/10)*1e-3*50)*1e6
def fmt(v):
    if v>=1e5: return it(v/1e6,3)+" V"
    if v>=1e3: return it(v/1e3,2)+" mV"
    if v>=10: return it(v,1)+" µV"
    if v>=1: return it(v,2)+" µV"
    return it(v,3)+" µV"
rows="".join(f'<tr><td class="l">{d} dBm</td><td>{fmt(dbm_uv(d))}</td><td>{it(d+107,0)} dBµV</td></tr>' for d in (0,-47,-73,-93,-107,-120,-127,-137))
D.add("dBm, µV e dBµV",f'''<div class="two"><div>
{eq("P(dBm) = 10·log(V² / (50 Ω · 1 mW))")}{eq("dBµV = dBm + 107 &nbsp;(su 50 Ω)")}
<ul class="small"><li>I generatori indicano il livello in dBm, in µV o in dBµV: sono la stessa cosa, purché sia chiaro su quale impedenza e se la tensione è su carico o a vuoto (slide successiva).</li>
<li>−73 dBm (50 µV) è l'S9 in HF; −93 dBm (5 µV) l'S9 in VHF/UHF.</li></ul></div><div>
<table><tr><th>dBm</th><th>V su 50 Ω (PD)</th><th>dBµV</th></tr>{rows}</table></div></div>''')
D.add("EMF e PD: il fattore 2 che inganna",'''<div class="two"><div><ul>
<li>Un generatore ha una resistenza interna di 50 Ω. Con un carico da 50 Ω la tensione si divide a metà.</li>
<li><b>PD</b> (potential difference): la tensione <b>sul carico</b> da 50 Ω. È la convenzione più usata oggi.</li>
<li><b>EMF</b> (forza elettromotrice): la tensione <b>a vuoto</b>, doppia rispetto alla PD (+6 dB).</li></ul>
<div class="eq">V<sub>EMF</sub> = 2 · V<sub>PD</sub> &nbsp; (+6 dB)</div></div><div>
<h3>Perché conta</h3><ul class="small"><li>Molti datasheet di ricevitori, soprattutto vecchi, danno la sensibilità in µV <b>EMF</b>: "0,25 µV EMF" equivale a 0,125 µV PD, cioè circa −125 dBm.</li>
<li>Alcuni generatori permettono di scegliere la visualizzazione EMF o PD: controlla l'impostazione prima di confrontare con un datasheet.</li>
<li>Se colleghi il generatore a un ingresso da 1 MΩ (un oscilloscopio) vedi la tensione EMF, cioè il doppio del valore impostato in PD.</li></ul></div></div>''')
D.add("Attenuatori fissi",f'''<div class="two"><div><ul>
<li>Un attenuatore resistivo a <b>π</b> o a <b>T</b> riduce il livello di un valore preciso e mantiene 50 Ω da entrambi i lati.</li>
<li>Migliora anche l'<b>adattamento</b>: un carico disadattato visto attraverso un attenuatore da N dB ha un return loss migliorato di 2N dB.</li></ul>
<div class="eq">K = 10<sup>A/20</sup>; &nbsp; π: R<sub>shunt</sub> = Z0·(K+1)/(K−1), &nbsp; R<sub>serie</sub> = Z0·(K²−1)/(2K)</div></div><div>
<table><tr><th>Attenuazione</th><th>R shunt (π)</th><th>R serie (π)</th></tr>
<tr><td class="l">3 dB</td><td>292,4 Ω</td><td>17,6 Ω</td></tr><tr><td class="l">6 dB</td><td>150,5 Ω</td><td>37,4 Ω</td></tr>
<tr><td class="l">10 dB</td><td>96,2 Ω</td><td>71,2 Ω</td></tr><tr><td class="l">20 dB</td><td>61,1 Ω</td><td>247,5 Ω</td></tr></table>
<p class="note">Gli attenuatori in serie si sommano in dB. Per livelli molto bassi una catena di attenuatori schermati (o l'attenuatore interno) è meglio di uno solo da 100 dB: la perdita attraverso i contenitori limita l'attenuazione reale.</p></div></div>''')
D.add("Perdite dei cavi e degli accessori",'''<div class="two"><div><ul>
<li>Tra generatore e ricevitore ci sono cavi, adattatori, attenuatori, magari un combinatore: ognuno toglie qualcosa.</li>
<li>Il livello vero all'ingresso del ricevitore è:</li></ul>
<div class="eq">P<sub>RX</sub> = P<sub>generatore</sub> − perdite (dB)</div>
<ul class="small"><li>Misura le perdite una volta con un VNA, o con il generatore e l'analizzatore (normalizzazione), alla frequenza di prova.</li>
<li>Annotale sul cavo o in un file: a 430 MHz un metro di RG-58 toglie circa 0,3–0,4 dB, un combinatore resistivo 6 dB.</li></ul></div><div>
<h3>Adattamento e incertezza</h3><ul class="small"><li>L'ingresso di un ricevitore spesso <b>non</b> è 50 Ω: le riflessioni rendono incerto il livello che arriva davvero.</li>
<li>Un attenuatore da 6–10 dB direttamente sull'ingresso del ricevitore riduce molto questo errore (il generatore deve scendere di altrettanto, e di solito ha margine).</li>
<li>L'incertezza di disadattamento si calcola come per i wattmetri: (1 ± |Γ<sub>g</sub>||Γ<sub>rx</sub>|)².</li></ul></div></div>''')
D.add("Combinatori e due generatori",'''<div class="two"><div><ul>
<li>Per i test di selettività e di intermodulazione servono <b>due segnali</b> (o tre) all'ingresso del ricevitore.</li>
<li><b>Combinatore resistivo</b> (3 resistenze da 16,7 Ω): banda larghissima, 6 dB di perdita per porta, isolamento tra le porte di soli 6 dB.</li>
<li><b>Combinatore ibrido</b> (trasformatore, splitter Wilkinson): circa 3,5 dB di perdita e 20–30 dB di isolamento, ma banda limitata.</li></ul></div><div>
<h3>Isolamento tra i generatori</h3><ul class="small"><li>Se i generatori "si vedono" troppo, i loro stadi d'uscita producono <b>intermodulazione</b> che sembra del ricevitore.</li>
<li>Rimedio: attenuatori da 10 dB o più su ogni generatore prima del combinatore, o un ibrido con buon isolamento.</li>
<li>Verifica: guarda l'uscita del combinatore con l'analizzatore di spettro. I prodotti di intermodulazione devono essere molto sotto quelli che vuoi misurare nel ricevitore.</li></ul></div></div>''')
D.add("Perdite (leakage): il nemico dei livelli bassi",'''<div class="two"><div><ul>
<li>A −120 dBm il segnale è un decimiliardesimo di milliwatt. Basta pochissimo segnale "sfuggito" dal generatore, dai cavi o dagli adattatori per falsare la misura.</li>
<li>Test: imposta il livello, poi <b>scollega il cavo</b> dall'ingresso del ricevitore (lasciandolo vicino). Se il ricevitore sente ancora il segnale, la misura di sensibilità non è valida.</li></ul></div><div>
<h3>Rimedi</h3><ul class="small"><li>Cavi a doppia schermatura o semirigidi, connettori N o SMA serrati, niente BNC allentati.</li>
<li>Gli attenuatori esterni vicino al ricevitore, non vicino al generatore: lungo il cavo il livello resta alto rispetto alle perdite.</li>
<li>Distanza tra generatore e ricevitore; spegni le antenne e scollega gli altri apparati.</li>
<li>Nei vecchi generatori controlla le guarnizioni e le viti del contenitore: un coperchio allentato perde.</li></ul></div></div>''')
D.add("Livelli tipici dei test radioamatoriali",'''<table><tr><th>Test</th><th>Livello tipico all'ingresso del ricevitore</th></tr>
<tr><td class="l">Sensibilità FM (SINAD 12 dB), VHF/UHF</td><td class="l">−120 … −125 dBm (0,2–0,3 µV PD)</td></tr>
<tr><td class="l">MDS in SSB/CW (banda 500 Hz)</td><td class="l">−130 … −140 dBm</td></tr>
<tr><td class="l">Taratura S-meter: S9</td><td class="l">−73 dBm (HF), −93 dBm (VHF/UHF)</td></tr>
<tr><td class="l">Prove di blocking e intermodulazione</td><td class="l">da −60 a 0 dBm (segnali forti)</td></tr>
<tr><td class="l">Iniezione di segnale in un'IF</td><td class="l">−60 … −30 dBm</td></tr>
<tr><td class="l">Pilotaggio di un mixer (LO)</td><td class="l">+7 … +17 dBm, a seconda del mixer</td></tr></table>
<p class="note" style="margin-top:12px">I livelli bassi richiedono attenuatori precisi e nessuna perdita; quelli alti richiedono un generatore pulito (lezione sulla purezza spettrale).</p>''')
rows=[("dBµV","dBm + 107 su 50 Ω"),("EMF / PD","EMF = 2·PD: +6 dB"),("Attenuatori","π o T, si sommano in dB, migliorano l'adattamento"),("Perdite","P<sub>RX</sub> = P<sub>gen</sub> − cavi − accessori"),("Combinatori","resistivo 6 dB, ibrido ~3,5 dB con più isolamento"),("Leakage","scollega il cavo: il RX non deve sentire nulla")]
D.add("Riepilogo",'<table class="sum">'+"".join(f'<tr><td class="l" style="width:200px"><b>{a}</b></td><td class="l">{b}</td></tr>' for a,b in rows)+'</table>')
D.render(); pdf("GEN_Livelli_Attenuatori_IV3HGA.pdf")
