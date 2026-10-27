from deck import *
D=Deck("Selettività e dinamica<br>del ricevitore","Canale adiacente, blocking e desensibilizzazione, reciprocal mixing, intermodulazione con DR3 e IP3, frequenza immagine e reiezione IF: come misurarli con uno o due generatori","Il generatore RF: selettività e dinamica")
two=f'''<svg viewBox="0 0 960 230" font-family="DejaVu Sans">{ARW}
{box(10,20,150,60,"Generatore A|(segnale utile)","#fff",13)}{box(10,130,150,60,"Generatore B|(interferente)","#fff",13)}
{ln(160,50,200,50)}{ln(160,160,200,160)}{box(200,25,110,50,"Att. 10 dB",L,13)}{box(200,135,110,50,"Att. 10 dB",L,13)}
<path d="M310 50 H360 V95" stroke="{N}" stroke-width="2" fill="none"/><path d="M310 160 H360 V115" stroke="{N}" stroke-width="2" fill="none"/>
{box(330,85,140,40,"Combinatore",L,13)}{ln(470,105,510,105)}{box(510,80,140,50,"Att. variabile",L,13)}{ln(650,105,690,105)}
{box(690,70,130,70,"Ricevitore|in prova","#fff",14)}{ln(820,105,860,105)}{box(860,80,90,50,"Misura|audio",L,12)}
<text x="330" y="215" font-size="12" fill="#555">gli attenuatori isolano i generatori tra loro (niente IMD dei generatori)</text></svg>'''
D.add("Che cosa si misura",'''<div class="two"><div><ul>
<li>La <b>sensibilità</b> dice quanto il ricevitore sente segnali deboli da soli.</li>
<li>La <b>selettività</b> e la <b>dinamica</b> dicono come si comporta quando accanto al segnale debole ci sono segnali forti: la situazione reale di un contest, di un sito con più ripetitori o di una banda affollata.</li></ul></div><div>
<table><tr><th>Misura</th><th>Che cosa rivela</th></tr>
<tr><td class="l">Canale adiacente</td><td class="l">la qualità dei filtri</td></tr>
<tr><td class="l">Blocking</td><td class="l">la saturazione degli stadi d'ingresso</td></tr>
<tr><td class="l">Reciprocal mixing</td><td class="l">il rumore di fase dell'oscillatore locale</td></tr>
<tr><td class="l">Intermodulazione (DR3, IP3)</td><td class="l">la linearità di preamplificatore e mixer</td></tr>
<tr><td class="l">Immagine e IF</td><td class="l">la preselezione e i filtri della supereterodina</td></tr></table></div></div>''')
D.add("Il setup con due generatori",f'''<div class="diag" style="width:90%;margin:-6px auto 0">{two}</div><div class="two" style="align-items:start;gap:30px"><div><ul class="small">
<li>Generatore A sulla frequenza del ricevitore, a un livello di riferimento (per esempio 3 dB sopra il MDS, o per SINAD 12 dB in FM).</li>
<li>Generatore B a una certa distanza (per esempio 20 kHz in HF, 25 kHz nel canale adiacente FM), a un livello alto.</li></ul></div><div><ul class="small">
<li>Prima di misurare il ricevitore, guarda l'uscita del combinatore con l'analizzatore: niente IMD tra i generatori, rumore di fase del generatore B sotto controllo.</li>
<li>Ricorda le perdite del combinatore (6 dB per il resistivo).</li></ul></div></div>''')
D.add("Selettività sul canale adiacente (FM)",'''<div class="two"><div><ol class="small">
<li>Generatore A sul canale, modulato come per la sensibilità, al livello che dà SINAD 12 dB; poi alzalo di 3 dB.</li>
<li>Generatore B sul canale adiacente (±12,5 o ±25 kHz), modulato con 400 Hz e deviazione standard.</li>
<li>Alza B finché il SINAD torna a 12 dB.</li>
<li>La selettività è la differenza tra il livello di B e quello di riferimento del segnale utile.</li></ol>
<div class="eq">selettività (dB) = P<sub>B</sub> − P<sub>A, 12 dB SINAD</sub></div></div><div>
<h3>Valori e interpretazione</h3><ul class="small"><li>Valori tipici: 60–70 dB per buone radio professionali a 25 kHz, meno per apparati portatili economici e a 12,5 kHz.</li>
<li>Se il risultato peggiora molto a 12,5 kHz rispetto a 25 kHz, il filtro IF è largo.</li>
<li>Il risultato dipende anche dal rumore di fase del generatore B: deve essere molto più pulito del ricevitore (lezione sulla purezza).</li></ul></div></div>''')
D.add("Blocking e desensibilizzazione",'''<div class="two"><div><ul>
<li>Un segnale fortissimo, anche lontano dalla frequenza ascoltata, satura gli stadi d'ingresso: il segnale utile <b>cala</b> (desensibilizzazione).</li></ul>
<h3>Procedura (SSB/CW)</h3><ol class="small"><li>Segnale utile A a un livello moderato (per esempio −110 dBm), letto in uscita audio con AGC spento.</li>
<li>Interferente B non modulato a una distanza fissata (20 kHz, poi 50 e 100 kHz).</li>
<li>Alza B finché l'uscita di A cala di <b>1 dB</b>.</li></ol>
<div class="eq">BDR = P<sub>B</sub> (1 dB di compressione) − MDS</div></div><div>
<h3>Cosa ingannare e cosa no</h3><ul class="small"><li>Spesso, prima del blocking vero, il ricevitore diventa rumoroso a causa del <b>reciprocal mixing</b> (slide successiva): il risultato è limitato dal rumore, non dalla compressione. Annota quale dei due limiti hai incontrato.</li>
<li>Valori tipici di un buon ricevitore HF: BDR oltre 120–130 dB a 20 kHz; ricevitori economici molto meno.</li>
<li>Il generatore B deve avere un rumore di fase eccellente a quella distanza.</li></ul></div></div>''')
D.add("Reciprocal mixing",'''<div class="two"><div><ul>
<li>Il rumore di fase dell'<b>oscillatore locale</b> del ricevitore si mescola con il segnale forte e produce rumore nel canale ricevuto.</li>
<li>Effetto pratico: un segnale forte a qualche kHz alza il "fondo" del ricevitore; i segnali deboli spariscono nel rumore senza che si veda una riga.</li></ul>
<div class="eq">L(f) ≈ MDS − P<sub>B</sub> − 10·log(B<sub>filtro</sub>)</div></div><div>
<h3>Misura</h3><ol class="small"><li>Solo il generatore B, non modulato, a una distanza nota dalla frequenza di ascolto.</li>
<li>Alza B finché il rumore in uscita aumenta di <b>3 dB</b> (come aggiungere un segnale al MDS).</li>
<li>Dalla formula ricavi il rumore di fase del LO del ricevitore a quella distanza.</li></ol>
<p class="note">Esempio: MDS −130 dBm, rumore +3 dB con B a −30 dBm, filtro 2,4 kHz → L ≈ −130 + 30 − 33,8 ≈ <b>−134 dBc/Hz</b>. Il generatore deve essere migliore di così, altrimenti misuri il suo rumore.</p></div></div>''')
D.add("Intermodulazione: DR3 e IP3",f'''<div class="two"><div class="fig">{svg("ip3.svg")}</div><div><ol class="small">
<li>Due toni uguali a f1 e f2 (per esempio 14,020 e 14,040 MHz), il ricevitore sintonizzato sul prodotto 2f1 − f2 (14,000 MHz).</li>
<li>Alza entrambi i toni finché il prodotto IM3 è uguale al MDS (3 dB sopra il rumore).</li></ol>
{eq("DR3 = P<sub>tono</sub> − MDS")}{eq("IP3 = (3·P<sub>tono</sub> − MDS) / 2")}
<ul class="small"><li>Esempio: MDS −130 dBm, toni a −43 dBm → DR3 = <b>87 dB</b>, IP3 = <b>+0,5 dBm</b>.</li>
<li>IP3 si estrapola: vale solo se il prodotto cresce davvero di 3 dB per dB (verificalo con due livelli).</li></ul></div></div>''')
D.add("Frequenza immagine e reiezione IF",'''<div class="two"><div><h3>Immagine</h3><ul>
<li>In una supereterodina, oltre al segnale voluto, entra anche quello a <b>f<sub>immagine</sub> = f<sub>RX</sub> ± 2·f<sub>IF</sub></b> (segno a seconda che il LO sia sopra o sotto).</li>
<li>Esempio: ricezione a 145,000 MHz con IF a 21,4 MHz e LO sopra: immagine a 187,8 MHz.</li>
<li>Misura: livello del generatore all'immagine per ottenere lo stesso effetto (SINAD 12 dB o MDS) del segnale sulla frequenza giusta. La differenza in dB è la <b>reiezione d'immagine</b>.</li></ul></div><div>
<h3>Reiezione IF e altre risposte spurie</h3><ul><li>Un segnale alla frequenza intermedia stessa (21,4 MHz nell'esempio) può passare direttamente: stessa procedura.</li>
<li>Altre risposte nascono da armoniche del LO e del segnale: si trovano spazzolando il generatore a livello alto e cercando dove il ricevitore "sente".</li>
<li>Valori tipici: 60–80 dB o più per apparati di qualità.</li>
<li>Per queste prove il generatore deve essere privo di armoniche: un passa-basso dopo il generatore evita falsi positivi.</li></ul></div></div>''')
rows=[("Canale adiacente","P<sub>B</sub> che riporta il SINAD a 12 dB, meno il riferimento"),("Blocking","1 dB di compressione: BDR = P<sub>B</sub> − MDS"),("Reciprocal mixing","+3 dB di rumore: L ≈ MDS − P<sub>B</sub> − 10·log(B)"),("IMD","DR3 = P − MDS; IP3 = (3P − MDS)/2"),("Immagine","f ± 2·f<sub>IF</sub>, reiezione in dB")]
D.add("Riepilogo",'<table class="sum">'+"".join(f'<tr><td class="l" style="width:220px"><b>{a}</b></td><td class="l">{b}</td></tr>' for a,b in rows)+'</table>')
D.render(); pdf("GEN_Selettivita_Dinamica_IV3HGA.pdf")
