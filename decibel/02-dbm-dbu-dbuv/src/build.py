from deck import *
D=Deck("dBm, dBW, dBu, dBµV<br>e tutti gli altri","Quando il decibel ha un riferimento diventa una misura: potenze, tensioni, rapporti rispetto alla portante, guadagni d'antenna e densità di rumore, con le conversioni e una tabella da tenere sul banco","Milestone · le unità in dB")
D.add("La lettera dopo il dB è il riferimento",'''<table><tr><th>Unità</th><th>Riferimento (0 dB = …)</th><th>Dove si usa</th></tr>
<tr><td class="l"><b>dBm</b></td><td class="l">1 milliwatt</td><td class="l">RF: livelli di segnale, potenze</td></tr>
<tr><td class="l"><b>dBW</b></td><td class="l">1 watt (dBW = dBm − 30)</td><td class="l">potenze di trasmettitori, EIRP</td></tr>
<tr><td class="l"><b>dBµV</b></td><td class="l">1 microvolt</td><td class="l">ricevitori, misure di campo, EMC</td></tr>
<tr><td class="l"><b>dBu</b></td><td class="l">0,775 V efficaci</td><td class="l">audio professionale</td></tr>
<tr><td class="l"><b>dBV</b></td><td class="l">1 V efficace</td><td class="l">audio, apparecchi consumer</td></tr>
<tr><td class="l"><b>dBc</b></td><td class="l">la portante (carrier)</td><td class="l">armoniche, spurie, rumore di fase</td></tr>
<tr><td class="l"><b>dBi / dBd</b></td><td class="l">antenna isotropica / dipolo</td><td class="l">guadagno d'antenna</td></tr>
<tr><td class="l"><b>dBm/Hz</b></td><td class="l">1 mW in 1 Hz di banda</td><td class="l">rumore, densità spettrale</td></tr>
<tr><td class="l"><b>dBµV/m</b></td><td class="l">1 µV/m di campo elettrico</td><td class="l">intensità di campo</td></tr></table>''')
D.add("dBm e dBW",'''<div class="two"><div>
<div class="eq">P(dBm) = 10 · log(P / 1 mW)</div><div class="eq">dBW = dBm − 30</div>
<table><tr><th>Potenza</th><th>dBm</th><th>dBW</th></tr>
<tr><td class="l">1 µW</td><td>−30</td><td>−60</td></tr><tr><td class="l">1 mW</td><td>0</td><td>−30</td></tr><tr><td class="l">10 mW</td><td>+10</td><td>−20</td></tr>
<tr><td class="l">1 W</td><td>+30</td><td>0</td></tr><tr><td class="l">5 W</td><td>+37</td><td>+7</td></tr><tr><td class="l">100 W</td><td>+50</td><td>+20</td></tr><tr><td class="l">1 kW</td><td>+60</td><td>+30</td></tr></table></div><div>
<ul class="small"><li>Con il trucco del 3 e del 10: 5 W = 1000 mW × 5 → 30 + 7 = <b>37 dBm</b>; 50 W = 47 dBm; 400 W = 56 dBm.</li>
<li>Al contrario: −100 dBm = 10<sup>−10</sup> mW = 0,1 pW.</li>
<li>I dBm sono la lingua comune di analizzatori, generatori e datasheet RF: vale la pena "sentirli" come si sentono i watt.</li></ul></div></div>''')
D.add("Le tensioni: dBµV, dBu, dBV",'''<div class="two"><div>
<div class="eq">dBµV = 20 · log(V / 1 µV)</div><div class="eq">dBu = 20 · log(V / 0,775 V)</div><div class="eq">dBV = 20 · log(V / 1 V) = dBu − 2,2</div>
<ul class="small"><li>Il curioso 0,775 V viene dalla telefonia: è la tensione che dà 1 mW su 600 Ω. Per questo, <b>solo su 600 Ω</b>, dBu e dBm coincidono.</li></ul></div><div>
<h3>Collegare tensioni e potenze su 50 Ω</h3>
<div class="eq">dBµV = dBm + 107</div>
<ul class="small"><li>0 dBm su 50 Ω sono 0,224 V = 107 dBµV.</li>
<li>S9 in HF: −73 dBm = 34 dBµV = 50 µV.</li>
<li>Su 50 Ω, 0 dBm = −10,8 dBu: in audio un livello "0 dBu" (0,775 V) su 50 Ω sarebbe 12 mW.</li>
<li>In audio le impedenze sono spesso alte (10 kΩ e oltre): lì si ragiona in tensione (dBu, dBV), non in potenza.</li></ul></div></div>''')
D.add("Rapporti: dBc, dBi, dBd",'''<div class="two"><div><h3>dBc</h3><ul class="small">
<li>"Rispetto alla portante": un'armonica a −50 dBc vale 1/100 000 della potenza della portante.</li>
<li>Comodo perché non dipende dalla potenza assoluta: un TX da 5 W o da 500 W con armoniche a −50 dBc è "pulito uguale".</li>
<li>Ma in assoluto: con 500 W, −50 dBc = 5 mW di armonica, che si sente lontano.</li></ul></div><div>
<h3>dBi e dBd</h3><ul class="small"><li><b>dBi</b>: guadagno rispetto a un'antenna isotropica ideale (che irradia uguale in tutte le direzioni).</li>
<li><b>dBd</b>: rispetto a un dipolo a mezz'onda.</li></ul>
<div class="eq">dBi = dBd + 2,15</div>
<ul class="small"><li>Attenzione ai depliant: "9 dB" senza lettera è spesso in dBi, che fa sembrare l'antenna migliore di 2,15 dB rispetto ai dBd.</li>
<li>Il significato fisico del guadagno d'antenna è spiegato con la candela di IW3SMV (lezione sull'EIRP).</li></ul></div></div>''')
D.add("Densità e rumore: dBm/Hz",'''<div class="two"><div><ul>
<li>Il rumore è distribuito in frequenza: si misura come potenza per hertz di banda.</li>
<li>Il rumore termico a temperatura ambiente vale:</li></ul>
<div class="eq">−174 dBm/Hz &nbsp;(kT a 290 K)</div>
<div class="eq">P<sub>rumore</sub> = −174 + 10·log(B) + NF</div></div><div>
<table><tr><th>Banda</th><th>10·log(B)</th><th>Rumore termico</th></tr>
<tr><td class="l">50 Hz (FT8)</td><td>17</td><td>−157 dBm</td></tr><tr><td class="l">500 Hz (CW)</td><td>27</td><td>−147 dBm</td></tr>
<tr><td class="l">2,4 kHz (SSB)</td><td>33,8</td><td>−140 dBm</td></tr><tr><td class="l">12,5 kHz (FM)</td><td>41</td><td>−133 dBm</td></tr>
<tr><td class="l">200 kHz (GSM)</td><td>53</td><td>−121 dBm</td></tr><tr><td class="l">5 MHz (WCDMA)</td><td>67</td><td>−107 dBm</td></tr></table>
<p class="note">Più stretta la banda, meno rumore: uno dei motivi per cui CW e FT8 arrivano dove la fonia non arriva.</p></div></div>''')
D.add("Tabella da banco",'''<table><tr><th>dBm</th><th>Potenza</th><th>V su 50 Ω</th><th>dBµV</th><th>Esempio</th></tr>
<tr><td class="l">+60</td><td class="l">1 kW</td><td class="l">224 V</td><td class="l">167</td><td class="l">lineare HF</td></tr>
<tr><td class="l">+50</td><td class="l">100 W</td><td class="l">70,7 V</td><td class="l">157</td><td class="l">ricetrasmettitore HF</td></tr>
<tr><td class="l">+37</td><td class="l">5 W</td><td class="l">15,8 V</td><td class="l">144</td><td class="l">portatile VHF</td></tr>
<tr><td class="l">+10</td><td class="l">10 mW</td><td class="l">0,71 V</td><td class="l">117</td><td class="l">uscita di un generatore</td></tr>
<tr><td class="l">0</td><td class="l">1 mW</td><td class="l">0,224 V</td><td class="l">107</td><td class="l">riferimento</td></tr>
<tr><td class="l">−73</td><td class="l">50 pW</td><td class="l">50 µV</td><td class="l">34</td><td class="l">S9 in HF</td></tr>
<tr><td class="l">−93</td><td class="l">0,5 pW</td><td class="l">5 µV</td><td class="l">14</td><td class="l">S9 in VHF/UHF</td></tr>
<tr><td class="l">−121</td><td class="l">≈ 0,8 fW</td><td class="l">0,2 µV</td><td class="l">−14</td><td class="l">sensibilità FM (SINAD 12 dB)</td></tr></table>''')
rows=[("dBm / dBW","1 mW / 1 W; dBW = dBm − 30"),("dBµV","dBm + 107 su 50 Ω"),("dBu / dBV","0,775 V / 1 V; dBV = dBu − 2,2"),("dBc","rispetto alla portante"),("dBi / dBd","dBi = dBd + 2,15"),("Rumore","−174 dBm/Hz + 10·log(B) + NF")]
D.add("Riepilogo",'<table class="sum">'+"".join(f'<tr><td class="l" style="width:200px"><b>{a}</b></td><td class="l">{b}</td></tr>' for a,b in rows)+'</table>')
D.render(); pdf("DB_Unita_dBm_dBu_IV3HGA.pdf")
