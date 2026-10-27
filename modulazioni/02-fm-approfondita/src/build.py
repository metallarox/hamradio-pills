from deck import *
D=Deck("La modulazione FM<br>in profondità","Deviazione e indice di modulazione, spettro e potenza costante, banda di Carson, preenfasi e deenfasi, soglia e guadagno FM, effetto cattura, limitatore e demodulatori, sovradeviazione e toni subaudio","Modulazioni · la FM in profondità")
D.add("L'idea",'''<div class="two"><div><ul>
<li>In FM l'audio sposta la <b>frequenza istantanea</b> della portante: più forte è l'audio, più grande lo spostamento. La rapidità con cui avviene lo spostamento segue la frequenza dell'audio.</li>
<li>L'ampiezza resta <b>costante</b>: l'informazione non sta nell'ampiezza, quindi tutto ciò che disturba l'ampiezza (rumore impulsivo, evanescenze moderate) si può tagliare.</li></ul></div><div>
<h3>Le due grandezze chiave</h3>
<div class="eq">Δf = deviazione di picco (Hz)</div><div class="eq">β = Δf / f<sub>m</sub> &nbsp;(indice di modulazione)</div>
<ul class="small"><li>Δf dipende dal <b>volume</b> dell'audio; f<sub>m</sub> è la frequenza del tono.</li>
<li>Esempi: radioamatori su canali da 25 kHz Δf ≈ 5 kHz; canali da 12,5 kHz Δf ≈ 2,5 kHz; broadcast Δf = 75 kHz.</li></ul></div></div>''')
D.add("Lo spettro: tante righe, potenza costante",f'''<div class="fig" style="width:96%">{svg("bessel.svg")}</div><div class="two" style="align-items:start;gap:30px"><div><ul class="small">
<li>Un tono di modulazione produce righe a f<sub>c</sub> ± n·f<sub>m</sub> con ampiezze date dalle funzioni di Bessel J<sub>n</sub>(β).</li>
<li>Con β piccolo la FM somiglia all'AM (portante + 2 righe); con β grande lo spettro si allarga molto.</li></ul></div><div><ul class="small">
<li>La somma delle potenze delle righe è <b>sempre</b> uguale alla potenza della portante non modulata: modulare non aggiunge potenza, la sposta (modulo sulla potenza dello spettro).</li></ul></div></div>''')
D.add("Potenza e trasmettitore",'''<div class="two"><div><ul>
<li>Inviluppo costante: <b>PEP = potenza media</b>. Un wattmetro legge sempre la stessa potenza, con o senza modulazione.</li>
<li>Il finale può lavorare in <b>classe C</b> o saturato: alta efficienza, meno calore, batterie che durano.</li>
<li>Non serve un amplificatore lineare: è il motivo per cui l'FM ha dominato i portatili e i mobili VHF/UHF.</li></ul></div><div>
<h3>Attenzione però</h3><ul><li>La trasmissione è continua al 100 %: carichi fittizi, attenuatori e finali devono reggere la potenza piena per tutto il tempo (ciclo di lavoro).</li>
<li>Un finale saturo genera armoniche forti: il filtro passa-basso d'uscita è indispensabile.</li>
<li>Il "punch" in FM non viene dalla potenza, ma dalla <b>deviazione</b>: un TX poco deviato si sente debole anche con tanti watt.</li></ul></div></div>''')
D.add("Banda occupata e sovradeviazione",'''<div class="two"><div>
<div class="eq">B ≈ 2·(Δf + f<sub>m,max</sub>) &nbsp;(Carson)</div>
<table><tr><th>Uso</th><th>Δf</th><th>Audio max</th><th>Carson</th></tr>
<tr><td class="l">canale 12,5 kHz</td><td>2,5 kHz</td><td>3 kHz</td><td>11 kHz</td></tr>
<tr><td class="l">canale 25 kHz</td><td>5 kHz</td><td>3 kHz</td><td>16 kHz</td></tr>
<tr><td class="l">broadcast</td><td>75 kHz</td><td>15 kHz</td><td>180 kHz</td></tr></table></div><div>
<h3>Sovradeviazione</h3><ul class="small"><li>Parlare troppo vicino al microfono, o un guadagno microfonico eccessivo, aumentano Δf: il segnale esce dal canale e disturba quelli adiacenti.</li>
<li>Per questo i trasmettitori hanno un <b>limitatore di deviazione</b> (clipper) seguito da un filtro passa-basso audio.</li>
<li>Un segnale sovradeviato ricevuto con un filtro stretto (12,5 kHz) suona distorto e "a tratti".</li>
<li>Si verifica con il nullo di Bessel o con un analizzatore con demodulazione (capitoli sul generatore e sull'analizzatore).</li></ul></div></div>''')
D.add("Preenfasi e deenfasi",f'''<div class="two"><div class="fig">{svg("emph.svg")}</div><div><ul class="small">
<li>Nel demodulatore FM il rumore non è piatto: la sua ampiezza cresce con la frequenza audio (+6 dB/ottava). Gli acuti sono i più rumorosi.</li>
<li>Soluzione: in trasmissione si <b>esaltano gli acuti</b> (preenfasi), in ricezione si attenuano allo stesso modo (deenfasi). La voce torna piatta, il rumore acuto scende.</li>
<li>Broadcast in Europa: costante di tempo <b>50 µs</b> (75 µs in America), angolo a 3,18 kHz.</li>
<li>Nei sistemi radiomobili si usa una preenfasi di 6 dB/ottava su tutta la banda vocale (300–3000 Hz): in pratica è una <b>modulazione di fase</b>.</li>
<li>Preenfasi e deenfasi devono corrispondere: altrimenti la voce suona "cupa" o "stridula".</li></ul></div></div>''')
D.add("FM e PM: due facce della stessa medaglia",'''<div class="two"><div><ul>
<li>In <b>PM</b> l'audio sposta la fase; la deviazione di frequenza risultante cresce con la frequenza del tono.</li>
<li>PM = preenfasi a 6 dB/ottava + FM. FM = filtro integratore + PM.</li>
<li>Molti trasmettitori "FM" storici erano modulatori di fase (più facili da costruire con oscillatori a quarzo stabili); il ricevitore FM con deenfasi li riceve correttamente.</li></ul></div><div>
<h3>Conseguenze pratiche</h3><ul><li>La deviazione misurata dipende dalla frequenza del tono di prova: per questo i test si fanno a 1 kHz.</li>
<li>Un tono acuto modulato "troppo forte" devia molto più di uno grave: il limitatore di deviazione serve proprio per gli acuti.</li>
<li>I toni subaudio <b>CTCSS</b> (67–254,1 Hz) si sommano all'audio con piccola deviazione e vengono filtrati in ricezione.</li></ul></div></div>''')
D.add("Soglia e guadagno FM",f'''<div class="two"><div class="fig">{svg("threshold.svg")}</div><div><ul class="small">
<li>Sopra la <b>soglia</b> (C/N di circa 10 dB) l'FM dà in uscita un S/N migliore di quello in ingresso: è il <b>guadagno FM</b>, che cresce con β (circa 3·β²·(β+1)).</li>
<li>Broadcast (β = 5): circa +26 dB. Radioamatori a banda stretta (β ≈ 1,7): circa +13 dB. Curve indicative.</li>
<li>Sotto la soglia la qualità <b>crolla</b>: compaiono scrosci e "click", il segnale sparisce. È l'effetto che si sente al limite della copertura di un ponte.</li>
<li>La SSB invece degrada in modo graduale: per i segnali deboli è migliore, per quelli forti l'FM è più pulita.</li></ul></div></div>''')
D.add("Effetto cattura, limitatore e demodulatori",'''<div class="two"><div><h3>Effetto cattura</h3><ul>
<li>Se due segnali FM sono sulla stessa frequenza, il ricevitore "si aggancia" al più forte e l'altro sparisce, anche con pochi dB di differenza (tipicamente 1–3 dB).</li>
<li>Utile (un ponte lontano non disturba quello vicino), ma ingannevole: chi è debole non si sente affatto, nemmeno come disturbo.</li>
<li>Quando i due segnali sono quasi uguali si alternano: il classico "picchiettio" tra due stazioni.</li></ul></div><div>
<h3>Ricevitore</h3><ul><li><b>Limitatore</b>: amplifica e taglia l'ampiezza, così restano solo le variazioni di frequenza.</li>
<li><b>Demodulatori</b>: discriminatore, rivelatore a quadratura, PLL; negli SDR si calcola direttamente la variazione della fase I/Q.</li>
<li><b>Squelch</b>: misura il rumore ad alta frequenza all'uscita del demodulatore; quando il segnale arriva il rumore scende e l'audio si apre.</li></ul></div></div>''')
rows=[("Deviazione","Δf dal volume; β = Δf/f<sub>m</sub>"),("Potenza","costante: PEP = media, classe C"),("Banda","Carson 2(Δf + f<sub>m</sub>): 11 / 16 / 180 kHz"),("Enfasi","preenfasi in TX, deenfasi in RX; 50 µs in Europa"),("Soglia","~10 dB di C/N: sopra guadagno, sotto crollo"),("Cattura","vince il più forte di pochi dB")]
D.add("Riepilogo",'<table class="sum">'+"".join(f'<tr><td class="l" style="width:180px"><b>{a}</b></td><td class="l">{b}</td></tr>' for a,b in rows)+'</table>')
D.render(); pdf("MOD_FM_Approfondita_IV3HGA.pdf")
