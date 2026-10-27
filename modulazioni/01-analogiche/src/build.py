from deck import *
D=Deck("Le modulazioni<br>analogiche","Che cos'è una modulazione e perché serve, CW, AM, DSB e SSB (USB e LSB), FM e modulazione di fase: come si generano, come si ricevono e in che cosa differiscono","Modulazioni · analogiche")
D.add("Che cos'è una modulazione",'''<div class="two"><div><ul>
<li>L'informazione (voce, dati, il tasto del telegrafo) ha frequenze basse: da pochi Hz a qualche kHz. Non si può irradiare direttamente: servirebbero antenne lunghe chilometri.</li>
<li>Si usa una <b>portante</b>: un'onda sinusoidale a radiofrequenza, facile da irradiare. La si "deforma" seguendo l'informazione: è la <b>modulazione</b>.</li>
<li>Ogni stazione usa una portante diversa: così tante trasmissioni condividono lo spettro senza disturbarsi.</li></ul></div><div>
<div class="eq">v(t) = A · cos(2π·f·t + φ)</div>
<ul><li>Di un'onda si possono cambiare solo tre cose: l'<b>ampiezza</b> A, la <b>frequenza</b> f, la <b>fase</b> φ.</li>
<li>Tutte le modulazioni, analogiche e numeriche, sono combinazioni di questi tre "comandi".</li>
<li>Il ricevitore fa il lavoro inverso: la <b>demodulazione</b>.</li></ul></div></div>''')
D.add("Ampiezza, frequenza, fase",f'''<div class="fig" style="width:84%;margin:-10px auto 0">{svg("time.svg")}</div><div class="two" style="align-items:start;gap:30px"><div><ul class="small">
<li><b>AM</b>: l'inviluppo (tratteggiato) segue l'audio. <b>FM</b>: le oscillazioni si stringono e si allargano, l'ampiezza resta costante.</li></ul></div><div><ul class="small">
<li><b>PM</b>: simile all'FM, ma lo spostamento segue la <b>variazione</b> dell'audio. FM e PM sono parenti stretti: si chiamano insieme modulazioni d'angolo.</li></ul></div></div>''')
D.add("CW: la modulazione più semplice",f'''<div class="two"><div class="fig">{svg("cw.svg")}</div><div><ul>
<li>La portante viene accesa e spenta con il tasto: è una modulazione d'ampiezza on/off (OOK).</li>
<li>Occupa pochissima banda (qualche decina o centinaia di Hz): si ricevono con filtri stretti, quindi con pochissimo rumore. Per questo il CW "passa" dove la fonia non arriva.</li>
<li>In ricezione un oscillatore locale (BFO) batte con la portante e produce il tono che senti.</li></ul>
<p class="note">I fronti di accensione e spegnimento devono essere arrotondati (qualche ms): fronti troppo ripidi allargano lo spettro e producono i key click che disturbano le stazioni vicine.</p></div></div>''')
D.add("AM",'''<div class="two"><div><ul>
<li>L'ampiezza della portante segue l'audio. Lo spettro ha la <b>portante</b> al centro e due <b>bande laterali</b> speculari, larghe quanto l'audio.</li>
<li>Banda occupata: due volte la frequenza audio massima (per esempio 6 kHz per un audio fino a 3 kHz).</li>
<li>Demodulazione semplicissima: un diodo e un condensatore (rivelatore d'inviluppo). È il motivo del suo successo storico.</li></ul></div><div>
<h3>I limiti</h3><ul class="small"><li>Almeno due terzi della potenza vanno nella portante, che non porta informazione.</li>
<li>Le due bande laterali contengono la <b>stessa</b> informazione: metà banda è sprecata.</li>
<li>Il rumore e i disturbi impulsivi si sommano all'ampiezza e si sentono direttamente.</li>
<li>I conti di potenza (portante, bande laterali, PEP) sono nel modulo sulla potenza del segnale e dello spettro.</li></ul></div></div>''')
D.add("Dalla AM alla SSB: USB e LSB",f'''<div class="fig" style="width:96%">{svg("ssb.svg")}</div><div class="two" style="align-items:start;gap:30px"><div><ul class="small">
<li>Togliendo la portante si ottiene la <b>DSB</b>. Togliendo anche una banda laterale resta la <b>SSB</b>: la banda laterale superiore (<b>USB</b>) o inferiore (<b>LSB</b>).</li>
<li>Banda dimezzata (circa 2,4–2,7 kHz) e tutta la potenza nell'informazione: rispetto all'AM, a parità di potenza di picco, guadagni diversi dB in ricezione.</li></ul></div><div><ul class="small">
<li>Convenzione radioamatoriale: <b>LSB sotto i 10 MHz</b> (160, 80, 40 m), <b>USB sopra</b> (20 m e oltre, VHF e UHF). I modi digitali come FT8 usano USB su tutte le bande.</li>
<li>Senza voce la SSB non trasmette nulla: niente portante, niente potenza.</li></ul></div></div>''')
D.add("Come si genera e si riceve la SSB",'''<div class="two"><div><h3>Generazione</h3><ul class="small">
<li><b>Metodo a filtro</b>: un modulatore bilanciato produce la DSB (senza portante), poi un filtro a quarzo stretto lascia passare una sola banda laterale. È il metodo classico dei ricetrasmettitori analogici.</li>
<li><b>Metodo a sfasamento</b>: due modulatori bilanciati alimentati con audio e portante sfasati di 90°; sommando o sottraendo le uscite una banda laterale si cancella. È il principio degli SDR (segnali I e Q).</li></ul></div><div>
<h3>Ricezione</h3><ul class="small"><li>Un <b>rivelatore a prodotto</b> mescola il segnale con un oscillatore locale (BFO) che ricrea la portante mancante.</li>
<li>Se il BFO non è esattamente alla frequenza giusta, la voce si sposta in tono: è il classico effetto "paperino". Bastano poche decine di Hz per sentirlo.</li>
<li>Per questo la SSB richiede ricetrasmettitori stabili in frequenza.</li></ul></div></div>''')
D.add("FM e modulazione di fase",'''<div class="two"><div><ul>
<li>In <b>FM</b> la frequenza istantanea segue l'audio: la <b>deviazione</b> (per esempio ±5 kHz o ±2,5 kHz) dipende dal volume, non dalla frequenza del tono.</li>
<li>In <b>PM</b> è la fase a seguire l'audio: la deviazione di frequenza cresce con la frequenza del tono. Con un filtro sull'audio una diventa l'altra.</li>
<li>Molti trasmettitori "FM" per radioamatori sono in realtà PM, oppure FM con <b>preenfasi</b> (gli acuti vengono esaltati in trasmissione e riattenuati in ricezione, insieme al rumore).</li></ul></div><div>
<h3>Pregi e difetti</h3><ul class="small"><li>Ampiezza costante: gli amplificatori possono lavorare in classe C, efficienti; i disturbi d'ampiezza vengono tagliati dal limitatore.</li>
<li><b>Effetto cattura</b>: tra due segnali sulla stessa frequenza, il più forte "vince" e l'altro sparisce.</li>
<li><b>Soglia</b>: sotto un certo livello la qualità crolla in fretta (curva del SINAD, capitolo sul generatore).</li>
<li>Banda più larga della SSB (regola di Carson, capitolo sul wattmetro: modulo sulla potenza dello spettro).</li></ul></div></div>''')
D.add("Confronto",'''<table><tr><th>Modo</th><th>Banda tipica</th><th>Efficienza</th><th>Ricezione</th><th>Uso</th></tr>
<tr><td class="l"><b>CW</b></td><td class="l">50–500 Hz</td><td class="l">tutta la potenza in un segnale stretto</td><td class="l">BFO, filtri stretti</td><td class="l">DX, segnali deboli</td></tr>
<tr><td class="l"><b>AM</b></td><td class="l">6–9 kHz</td><td class="l">bassa (portante)</td><td class="l">diodo, semplicissima</td><td class="l">broadcast, aeronautica, storico</td></tr>
<tr><td class="l"><b>SSB</b></td><td class="l">2,4–2,7 kHz</td><td class="l">alta</td><td class="l">rivelatore a prodotto, stabilità</td><td class="l">fonia in HF, DX in VHF/UHF</td></tr>
<tr><td class="l"><b>FM</b></td><td class="l">11–16 kHz</td><td class="l">alta, amplificatori efficienti</td><td class="l">discriminatore, limitatore</td><td class="l">VHF/UHF, ponti, locale</td></tr></table>
<p class="note" style="margin-top:14px">Le modulazioni numeriche usano gli stessi tre "comandi" (ampiezza, frequenza, fase), ma per trasmettere numeri invece che una forma d'onda continua: è la lezione successiva.</p>''')
rows=[("Modulazione","variare ampiezza, frequenza o fase di una portante"),("CW","on/off, banda strettissima, fronti arrotondati"),("AM","portante + 2 bande laterali, demodulazione col diodo"),("SSB","una banda laterale; LSB sotto 10 MHz, USB sopra"),("FM / PM","ampiezza costante, effetto cattura, soglia")]
D.add("Riepilogo",'<table class="sum">'+"".join(f'<tr><td class="l" style="width:200px"><b>{a}</b></td><td class="l">{b}</td></tr>' for a,b in rows)+'</table>')
D.render(); pdf("MOD_Analogiche_IV3HGA.pdf")
