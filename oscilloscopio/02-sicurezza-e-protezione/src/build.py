from deck import *
D=Deck("Oscilloscopio:<br>sicurezza e protezione","Non farsi male e non rompere lo strumento: la massa della sonda collegata a terra, le misure sulla rete, i limiti d'ingresso, la RF e le tensioni nascoste","L'oscilloscopio: sicurezza e protezione")
O="#e0563b"
gnd=f'''<svg viewBox="0 0 900 320" font-family="DejaVu Sans">{ARW}
{box(20,40,190,90,"Oscilloscopio|(telaio metallico)","#fff",15)}
<line x1="115" y1="130" x2="115" y2="250" stroke="{N}" stroke-width="2.5"/><text x="125" y="200" font-size="13" fill="{N}">conduttore di terra</text><text x="125" y="216" font-size="13" fill="{N}">della spina</text>
<line x1="85" y1="250" x2="145" y2="250" stroke="{N}" stroke-width="2.5"/><line x1="95" y1="260" x2="135" y2="260" stroke="{N}" stroke-width="2.5"/><line x1="105" y1="270" x2="125" y2="270" stroke="{N}" stroke-width="2.5"/>
<text x="60" y="300" font-size="13" fill="#555">terra dell'impianto</text>
<path d="M210 70 H420" stroke="{N}" stroke-width="2"/><text x="300" y="60" font-size="13" fill="{N}">punta</text>
<path d="M210 105 H330 V160 H420" stroke="{O}" stroke-width="3" fill="none"/><text x="200" y="128" font-size="13" fill="{O}" font-weight="700">clip di massa = terra!</text>
{box(420,30,300,170,"","#fff")}<text x="570" y="60" text-anchor="middle" font-size="15" font-weight="700" fill="{N}">Circuito collegato alla rete</text>
<text x="570" y="85" text-anchor="middle" font-size="13" fill="#555">(primario di un alimentatore switching,</text><text x="570" y="102" text-anchor="middle" font-size="13" fill="#555">dimmer, raddrizzatore senza trasformatore)</text>
<circle cx="440" cy="160" r="6" fill="{O}"/><text x="455" y="165" font-size="13" fill="{O}">nodo a ~160–325 V rispetto a terra</text>
<path d="M720 120 H800 V250 H115" stroke="{O}" stroke-width="2.5" stroke-dasharray="7 5" fill="none" marker-end="url(#ar)"/>
<text x="250" y="240" font-size="14" fill="{O}" font-weight="700">corrente di cortocircuito attraverso la massa della sonda</text></svg>'''
D.add("Due pericoli",'''<div class="two"><div><h3>Per te</h3><ul>
<li>Il telaio dell'oscilloscopio e la clip di massa della sonda sono collegati alla <b>terra di sicurezza</b>.</li>
<li>Misure sulla rete, alimentatori, amplificatori a valvole e trasmettitori comportano tensioni che possono <b>uccidere</b>.</li>
<li>Molti incidenti nascono da gesti "normali": attaccare la clip di massa nel punto sbagliato, staccare la terra "per far sparire il ronzio".</li></ul></div><div>
<h3>Per lo strumento</h3><ul><li>Gli ingressi hanno limiti di tensione (a 1 MΩ) e di potenza (a 50 Ω).</li>
<li>Un cortocircuito attraverso la massa vaporizza il filo della sonda, brucia piste e connettori.</li>
<li>Scariche statiche e sovratensioni rovinano lo stadio d'ingresso, spesso in modo parziale: banda o precisione peggiorano senza che te ne accorga.</li></ul></div></div>''')
D.add("La clip di massa è collegata a terra",f'''<div class="diag" style="width:86%;margin:-8px auto 0">{gnd}</div><div class="two" style="align-items:start;gap:30px"><div><ul class="small">
<li>In un oscilloscopio da banco normale, <b>tutte le masse dei canali sono la stessa terra</b> della presa di corrente.</li>
<li>Se colleghi la clip di massa a un nodo che non è a potenziale di terra, crei un <b>cortocircuito</b> verso terra.</li></ul></div><div><ul class="small">
<li>Sul primario di un alimentatore switching, nei dimmer, nei circuiti senza trasformatore, nessun nodo è sicuro: anche il "meno" del ponte raddrizzatore è a centinaia di volt dalla terra.</li>
<li>Risultato: scintille, sonda e circuito bruciati, differenziale che scatta. Se va male, peggio.</li></ul></div></div>''')
D.add("Mai staccare la terra dell'oscilloscopio",'''<div class="two"><div><div class="warn">Togliere la terra all'oscilloscopio (adattatori, spine tagliate) per "farlo galleggiare" è <b>pericolosissimo</b>: il telaio, i connettori BNC e tutte le masse dei canali si portano alla tensione del punto misurato. Chi tocca lo strumento la riceve.</div>
<ul class="small"><li>Le norme vietano questa pratica e i costruttori la sconsigliano esplicitamente.</li>
<li>Anche il "ronzio" che sparisce staccando la terra è un problema di ground loop, che si risolve in altri modi.</li></ul></div><div>
<h3>Cosa usare invece</h3><table><tr><th>Soluzione</th><th>Note</th></tr>
<tr><td class="l"><b>Sonda differenziale</b> ad alta tensione</td><td class="l">la soluzione corretta: misura tra due punti qualsiasi, isolata</td></tr>
<tr><td class="l"><b>Oscilloscopio a canali isolati</b> (spesso a batteria)</td><td class="l">ogni canale ha la sua massa, con categoria di sicurezza dichiarata</td></tr>
<tr><td class="l"><b>Trasformatore d'isolamento</b> sul circuito in prova</td><td class="l">isola il DUT dalla terra, mai lo strumento; il DUT resta pericoloso al tatto</td></tr>
<tr><td class="l"><b>Misura A − B</b> con due canali</td><td class="l">solo per tensioni basse rispetto a terra (vedi lezione sui trucchi)</td></tr></table></div></div>''')
D.add("I limiti degli ingressi",'''<div class="two"><div><h3>Ingresso a 1 MΩ</h3><ul class="small">
<li>Sul pannello c'è scritta la tensione massima (per esempio 300 V CAT II o 400 V di picco): è il limite <b>dell'ingresso</b>.</li>
<li>Con una sonda 10× conta il limite <b>della sonda</b>, scritto sul suo corpo o sul connettore, e la sua categoria.</li>
<li>La tensione massima delle sonde <b>diminuisce con la frequenza</b> (curva di derating): 300 V a 50 Hz non significano 300 V a 30 MHz.</li></ul>
<h3>Categorie di misura</h3><ul class="small"><li><b>CAT I</b>: circuiti non collegati alla rete. <b>CAT II</b>: apparecchi collegati a una presa. <b>CAT III/IV</b>: impianto e quadri. Usa sempre strumento e sonde della categoria adatta.</li></ul></div><div>
<h3>Ingresso a 50 Ω</h3><ul class="small"><li>Pensato per segnali veloci da sorgenti a 50 Ω. È un <b>carico</b>: dissipa potenza.</li>
<li>Il limite tipico è intorno a <b>5 V efficaci</b>, cioè mezzo watt: leggilo sul pannello.</li>
<li>Niente tensione continua elevata, niente trasmettitori, niente misure di alimentatori su questo ingresso.</li>
<li>Molti strumenti staccano il 50 Ω in caso di sovraccarico, ma non sempre in tempo.</li></ul></div></div>''')
D.add("Oscilloscopio e trasmettitori",'''<div class="two"><div><ul>
<li>Su 50 Ω, <b>100 W</b> sono 70,7 V efficaci e <b>100 V di picco</b>; con SWR alto anche il doppio. 5 W sono già 22 V efficaci.</li>
<li>Collegare un TX all'ingresso a 50 Ω significa bruciarlo. Anche a 1 MΩ, con una sonda, la tensione e la frequenza vanno confrontate con il derating della sonda.</li></ul>
<h3>Il modo corretto</h3><ol class="small"><li>TX su <b>carico fittizio</b> con prelievo, o attenuatore di potenza.</li>
<li>Attenuatori fino a un livello di pochi volt.</li><li>Ingresso a 50 Ω (o 1 MΩ con terminazione passante da 50 Ω).</li></ol></div><div>
<div class="eq">V<sub>pp</sub> = 2·√2·√(P·50 Ω)</div>
<table><tr><th>Potenza su 50 Ω</th><th>V<sub>eff</sub></th><th>V<sub>pp</sub></th></tr>
<tr><td class="l">10 mW (+10 dBm)</td><td>0,71 V</td><td>2,0 V</td></tr><tr><td class="l">0,5 W (+27 dBm)</td><td>5,0 V</td><td>14,1 V</td></tr>
<tr><td class="l">5 W</td><td>15,8 V</td><td>44,7 V</td></tr><tr><td class="l">100 W</td><td>70,7 V</td><td>200 V</td></tr></table>
<p class="note">Con 40 dB di attenuazione, 100 W diventano 10 mW: 2 V picco-picco, perfetti per l'oscilloscopio.</p></div></div>''')
D.add("Tensioni nascoste e lavoro in sicurezza",'''<div class="two"><div><ul>
<li>I <b>condensatori di filtro</b> degli alimentatori restano carichi a lungo dopo lo spegnimento, soprattutto se la resistenza di scarica è guasta.</li>
<li>Negli <b>amplificatori a valvole</b> l'anodica è di centinaia di volt o di kilovolt, con condensatori che possono uccidere anche a spina staccata.</li>
<li>Gli oscilloscopi a tubo stessi hanno tensioni di kilovolt all'interno.</li></ul></div><div>
<h3>Regole d'oro</h3><ol class="small"><li>Scarica i condensatori con una resistenza di potenza adeguata (non con un cacciavite) e <b>verifica</b> con il multimetro.</li>
<li>Collega le sonde a circuito spento, poi accendi.</li>
<li>Una mano sola vicino al circuito in tensione, l'altra lontana (non appoggiata al telaio).</li>
<li>Niente anelli, braccialetti, orologi metallici. Tappetino isolante sul banco.</li>
<li>Mai lavorare da soli sull'alta tensione; un interruttore d'emergenza a portata di mano.</li></ol></div></div>''')
D.add("Proteggere lo strumento",'''<div class="two"><div><ul>
<li><b>Statica</b>: scaricati prima di toccare i BNC; la punta di una sonda è una porta diretta verso l'amplificatore d'ingresso.</li>
<li>Non collegare sonde a punti ad alta tensione con il circuito acceso: l'arco e il transitorio possono superare i limiti.</li>
<li>Controlla il selettore 1×/10× della sonda: a 1× l'ingresso vede tutta la tensione.</li>
<li>Usa un <b>DC block</b> prima dell'ingresso a 50 Ω quando c'è continua.</li></ul></div><div><ul>
<li>BNC e punte delle sonde si consumano: non torcerli e non tirare i cavi.</li>
<li>Lascia libere le prese d'aria: l'elettronica interna scalda.</li>
<li>Trasporto in custodia imbottita; schermo protetto.</li>
<li>Ogni sonda va compensata sul suo canale (vedi la lezione sulle sonde) e tenuta con il suo strumento.</li></ul></div></div>''')
rows=["La clip di massa va solo su un punto a potenziale di terra","Mai togliere la terra all'oscilloscopio","Sonda differenziale o canali isolati per misure sulla rete","Limiti di ingresso e di sonda (con il derating in frequenza) rispettati",
"Niente RF di potenza all'ingresso: carico, attenuatori, 50 Ω","Condensatori scaricati e verificati, una mano sola","Selettore 1×/10× e DC block controllati"]
D.add("Checklist di sicurezza",'<table class="sum">'+"".join(f'<tr><td class="l" style="width:46px;color:#22b8f0;font-weight:800">☐</td><td class="l">{r}</td></tr>' for r in rows)+'</table>')
D.render(); pdf("OSC_Sicurezza_Protezione_IV3HGA.pdf")
