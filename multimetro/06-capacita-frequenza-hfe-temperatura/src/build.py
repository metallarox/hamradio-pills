from deck import *
D=Deck("Capacità, frequenza,<br>hFE e temperatura","Come lavorano le funzioni \"secondarie\" del multimetro, i loro limiti e gli usi pratici: misurare la lunghezza di un coassiale, controllare un CTCSS, appaiare transistor, la temperatura di un finale","Il multimetro: capacità, frequenza, hFE, temperatura")
D.add("Capacità: come la misura",'''<div class="two"><div><ul>
<li>Lo strumento carica il condensatore con una <b>corrente nota</b> e misura il tempo per raggiungere una certa tensione: C = I·t / V.</li>
<li>Per questo le misure di condensatori grandi (centinaia di µF o mF) richiedono <b>secondi</b>.</li>
<li>La tensione di prova è bassa (pochi decimi di volt o qualche volt).</li></ul>
<div class="warn">Scarica sempre il condensatore prima: un elettrolitico carico può danneggiare lo strumento.</div></div><div>
<h3>Limiti</h3><ul class="small"><li>Non misura l'<b>ESR</b> né la perdita: un elettrolitico "secco" può avere la capacità giusta e un ESR altissimo. Per quello serve un misuratore di ESR.</li>
<li>Sui pF piccoli pesa la capacità dei puntali: accorciali, tienili fermi e usa <b>REL</b> con i puntali aperti.</li>
<li>In circuito le letture sono inaffidabili (componenti in parallelo).</li>
<li>Precisione tipica di qualche %: sufficiente per riconoscere e verificare, non per selezionare condensatori di precisione.</li></ul></div></div>''')
D.add("Trucco: la lunghezza di un cavo coassiale",'''<div class="two"><div><ul>
<li>Un coassiale è un condensatore distribuito: la capacità per metro è nota dal datasheet.</li>
<li>Con il cavo aperto all'altro capo, misura la capacità tra centrale e calza:</li></ul>
<div class="eq">lunghezza ≈ C<sub>misurata</sub> / C<sub>per metro</sub></div>
<table><tr><th>Tipo di cavo da 50 Ω</th><th>Capacità tipica</th></tr>
<tr><td class="l">dielettrico in polietilene pieno (RG-58, RG-213)</td><td class="l">circa 100 pF/m</td></tr>
<tr><td class="l">dielettrico espanso (schiuma)</td><td class="l">circa 75–85 pF/m</td></tr></table></div><div>
<h3>Esempio</h3><ul class="small"><li>Una matassa di RG-58 misura 2,0 nF: circa <b>20 m</b>.</li>
<li>Utile per sapere quanto cavo resta nella bobina senza srotolarla, o la lunghezza di un cavo già posato.</li>
<li>Se lo stesso cavo misura molto meno del previsto, potrebbe essere interrotto a metà: la capacità ti dice anche <b>dove</b>.</li></ul>
<p class="note">Usa il valore del datasheet del tuo cavo: le capacità variano da marca a marca.</p></div></div>''')
D.add("Frequenza e duty cycle",'''<div class="two"><div><ul>
<li>La funzione Hz conta i passaggi del segnale per una soglia: serve un'ampiezza minima (spesso qualche centinaio di mV) e una forma d'onda pulita.</li>
<li>Frequenza massima tipica: da decine di kHz a qualche MHz, a seconda del modello.</li>
<li>Con segnali rumorosi o con armoniche il contatore può contare il doppio: usa la funzione Hz sulla portata V AC più alta, che fa da filtro.</li>
<li><b>Duty cycle</b>: percentuale del tempo in cui il segnale è alto.</li></ul></div><div>
<h3>Usi in stazione</h3><ul class="small"><li>Controllare il tono <b>CTCSS</b> di una radio sull'uscita audio o sul segnale demodulato: 88,5 Hz deve leggere 88,5.</li>
<li>Verificare la frequenza di un oscillatore audio o di un generatore di toni.</li>
<li>Controllare PWM di ventole e regolatori.</li>
<li>Misurare la frequenza di rete (50 Hz) su un gruppo elettrogeno in portatile.</li>
<li>Non è un frequenzimetro RF: per la frequenza di un TX serve un frequenzimetro dedicato o l'analizzatore.</li></ul></div></div>''')
D.add("hFE: il guadagno dei transistor",'''<div class="two"><div><ul>
<li>Lo zoccolino hFE alimenta il transistor con una <b>corrente di base fissa</b> (tipicamente intorno a 10 µA) e qualche volt sul collettore, e misura la corrente di collettore.</li>
<li>Il display mostra hFE = I<sub>C</sub> / I<sub>B</sub>.</li>
<li>Attenzione al tipo (NPN o PNP) e all'ordine dei piedini (E, B, C) dello zoccolo.</li></ul></div><div>
<h3>Quanto vale il numero</h3><ul class="small"><li>L'hFE dipende molto da corrente di collettore e temperatura: il valore letto vale in quelle condizioni, non nel tuo circuito a 100 mA.</li>
<li>È ottimo per <b>confrontare</b> transistor dello stesso tipo: appaiare coppie per stadi push-pull o differenziali, scartare esemplari anomali.</li>
<li>Scalda il transistor con le dita: l'hFE sale, una prova rapida della sensibilità alla temperatura.</li>
<li>I Darlington vanno spesso fuori scala; i transistor di potenza lavorano lontano dal loro punto tipico.</li></ul></div></div>''')
D.add("hFE senza zoccolo, in condizioni reali",'''<div class="two"><div><ul>
<li>Per conoscere l'hFE alla corrente che userai davvero, monta un circuito di prova: una resistenza di base da un'alimentazione e una resistenza di collettore.</li></ul>
<div class="eq">I<sub>B</sub> = (V<sub>alim</sub> − V<sub>BE</sub>) / R<sub>B</sub> &nbsp;&nbsp; I<sub>C</sub> = V<sub>RC</sub> / R<sub>C</sub></div><div class="eq">hFE = I<sub>C</sub> / I<sub>B</sub></div></div><div>
<h3>Esempio</h3><ul class="small"><li>12 V, R<sub>B</sub> = 220 kΩ, V<sub>BE</sub> ≈ 0,65 V → I<sub>B</sub> ≈ 51,6 µA.</li>
<li>R<sub>C</sub> = 470 Ω, ai suoi capi leggi 4,70 V → I<sub>C</sub> = 10 mA.</li>
<li>hFE ≈ 10 mA / 51,6 µA ≈ <b>194</b>.</li>
<li>Tutte misure di <b>tensione</b> su resistenze note: l'idea della lezione sulla corrente.</li>
<li>Controlla che il transistor non sia saturo: la tensione collettore-emettitore deve restare sopra 1 V circa.</li></ul></div></div>''')
D.add("Temperatura con termocoppia",'''<div class="two"><div><ul>
<li>Le sonde sono quasi sempre <b>termocoppie tipo K</b>: due metalli diversi che generano circa 41 µV/°C.</li>
<li>Il multimetro compensa la temperatura dei suoi morsetti (giunzione fredda) con un sensore interno: per questo, appena collegato o spostato da un ambiente all'altro, va lasciato stabilizzare.</li>
<li>La sonda a perlina in dotazione regge in genere qualche centinaio di gradi; l'isolamento dei fili ha limiti più bassi.</li></ul></div><div>
<h3>Usi in stazione</h3><ul class="small"><li>Temperatura del <b>dissipatore</b> di un finale durante una trasmissione lunga (FM, modi digitali).</li>
<li>Carico fittizio e attenuatori di potenza: quanto scaldano davvero.</li>
<li>Trasformatori e alimentatori sotto carico.</li>
<li>Verifica della temperatura della punta del saldatore (con sonde adatte).</li>
<li>Il contatto termico conta: fissa la perlina con nastro di alluminio o pasta termica, altrimenti misuri l'aria.</li></ul></div></div>''')
D.add("Altre funzioni da conoscere",'''<table><tr><th>Funzione</th><th>A cosa serve</th></tr>
<tr><td class="l"><b>4–20 mA (%)</b></td><td class="l">mostra la corrente dei loop industriali in percentuale della scala</td></tr>
<tr><td class="l"><b>dBm / dBV</b></td><td class="l">tensioni AC in decibel, con impedenza di riferimento impostabile (spesso 600 Ω): utile in audio</td></tr>
<tr><td class="l"><b>Test batterie</b></td><td class="l">misura la tensione con un piccolo carico inserito: più significativo della tensione a vuoto</td></tr>
<tr><td class="l"><b>NCV</b></td><td class="l">rilevatore di tensione senza contatto: solo come indizio, mai come prova di assenza di tensione</td></tr>
<tr><td class="l"><b>Filtro passa-basso / VFD</b></td><td class="l">misure corrette sulle uscite degli inverter per motori</td></tr>
<tr><td class="l"><b>Prova diodi ad alta tensione</b></td><td class="l">alcuni modelli superano i 3 V: provano LED bianchi e stringhe di LED</td></tr></table>
<p class="note" style="margin-top:12px">Le funzioni "da esperti" (REL, MIN/MAX, peak, logging) hanno una lezione dedicata.</p>''')
rows=[("Capacità","scarica prima; non misura ESR; REL per i pF"),("Coassiale","lunghezza ≈ C / (pF/m)"),("Frequenza","ampiezza minima, segnali puliti; CTCSS e audio, non RF"),("hFE","per confrontare; I<sub>C</sub>/I<sub>B</sub> in condizioni reali"),("Temperatura","termocoppia K, contatto termico, giunzione fredda")]
D.add("Riepilogo",'<table class="sum">'+"".join(f'<tr><td class="l" style="width:180px"><b>{a}</b></td><td class="l">{b}</td></tr>' for a,b in rows)+'</table>')
D.render(); pdf("MM_Capacita_Frequenza_hFE_Temperatura_IV3HGA.pdf")
