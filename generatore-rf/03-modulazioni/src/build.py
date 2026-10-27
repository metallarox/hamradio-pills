from deck import *
D=Deck("Le modulazioni<br>del generatore","AM, FM e modulazione di fase, impulsi, modulazione esterna e I/Q: come impostarle, verificarle con l'analizzatore e usarle nei test dei ricevitori","Il generatore RF: le modulazioni")
D.add("Perché modulare",'''<div class="two"><div><ul>
<li>Un ricevitore si prova come si usa: con un segnale <b>modulato</b> e la misura sull'audio in uscita.</li>
<li>Il generatore modula con un tono interno (di solito <b>1 kHz</b>, a volte 400 Hz) o con un segnale esterno.</li>
<li>La modulazione deve essere <b>nota</b> e <b>pulita</b>: deviazione o profondità precise, distorsione bassa.</li></ul></div><div>
<h3>Convenzioni dei test</h3><table><tr><th>Modo</th><th>Modulazione di prova tipica</th></tr>
<tr><td class="l">FM a 25 kHz di canalizzazione</td><td class="l">1 kHz, deviazione 3 kHz (60 % del massimo)</td></tr>
<tr><td class="l">FM a 12,5 kHz</td><td class="l">1 kHz, deviazione 1,5 kHz</td></tr>
<tr><td class="l">AM</td><td class="l">1 kHz (o 400 Hz), profondità 30 %</td></tr>
<tr><td class="l">SSB / CW</td><td class="l">portante non modulata, battimento a ~1 kHz</td></tr></table>
<p class="note">Sono le convenzioni più diffuse nelle norme e nei datasheet: usa le stesse per confrontare i tuoi risultati.</p></div></div>''')
D.add("AM",'''<div class="two"><div><ul>
<li>L'ampiezza della portante segue il segnale modulante; la <b>profondità</b> m indica quanto varia.</li></ul>
<div class="eq">m = (V<sub>max</sub> − V<sub>min</sub>) / (V<sub>max</sub> + V<sub>min</sub>)</div>
<div class="eq">bande laterali: 20·log(m/2) dBc</div>
<ul class="small"><li>Con m = 30 % le bande laterali sono a −16,5 dBc; con m = 100 % a −6 dBc.</li></ul></div><div>
<h3>Attenzione</h3><ul class="small"><li>In AM la <b>potenza di picco</b> sale: con m = 100 % il picco è 4 volte (+6 dB) la portante. Il livello indicato dal generatore è di solito quello della <b>portante</b>.</li>
<li>Ai livelli d'uscita più alti il generatore può non avere margine per i picchi: controlla i limiti di livello con AM attiva.</li>
<li>Verifica la profondità con l'analizzatore (bande laterali) o con l'oscilloscopio (inviluppo o trapezio).</li>
<li>Con ALC attivo e modulazione esterna lenta, l'ALC può "correggere" la modulazione: usa la modalità prevista per l'AM.</li></ul></div></div>''')
D.add("FM e modulazione di fase",'''<div class="two"><div><ul>
<li>In FM la <b>frequenza</b> segue il segnale modulante; la <b>deviazione</b> Δf è lo spostamento massimo.</li>
<li>In ΦM varia la <b>fase</b>: la deviazione di frequenza cresce con la frequenza del tono. I trasmettitori "FM" per radioamatori usano spesso la ΦM con pre-enfasi.</li></ul>
<div class="eq">β = Δf / f<sub>m</sub> &nbsp; B ≈ 2·(Δf + f<sub>m</sub>)</div></div><div>
<h3>Verificare la deviazione</h3><ul class="small"><li><b>Nullo di Bessel</b>: con f<sub>m</sub> = Δf / 2,405 la portante si annulla sull'analizzatore. Per 3 kHz di deviazione: tono da 1247 Hz.</li>
<li>Con un ricevitore di misura o un analizzatore con demodulazione FM si legge direttamente.</li>
<li><b>FM residua</b>: deviazione "spontanea" del generatore senza modulazione. Deve essere molto più piccola di quella che usi (pochi Hz).</li>
<li>In FM l'ampiezza resta costante: il livello indicato vale anche con la modulazione attiva.</li></ul></div></div>''')
D.add("Impulsi e modulazione esterna",'''<div class="two"><div><h3>Impulsi</h3><ul class="small">
<li>La portante viene accesa e spenta con impulsi di durata e periodo impostabili.</li>
<li>Usi: simulare segnali TDMA (burst di DMR o TETRA), radar, telecomandi; provare AGC e squelch con segnali intermittenti.</li>
<li>Parametri: <b>on/off ratio</b> (quanto si spegne davvero, in dB) e tempi di salita.</li>
<li>Su un wattmetro termico la potenza media si riduce del duty cycle (capitolo sul wattmetro).</li></ul></div><div>
<h3>Modulazione esterna</h3><ul class="small"><li><b>AM/FM esterna</b>: ingresso audio con sensibilità indicata (per esempio 1 V picco = deviazione impostata). Accoppiamento AC o DC: con DC puoi spostare la frequenza con una tensione (sweep lento, VCO).</li>
<li><b>I/Q</b> nei generatori vettoriali: qualsiasi modulazione digitale da un file o da un SDR.</li>
<li>Per test di intelligibilità puoi modulare con voce registrata, ma per misure ripetibili usa i toni.</li></ul></div></div>''')
D.add("Segnali per test speciali",'''<table><tr><th>Segnale</th><th>Come ottenerlo</th><th>A cosa serve</th></tr>
<tr><td class="l"><b>Due toni RF</b></td><td class="l">due generatori + combinatore</td><td class="l">intermodulazione, IP3 del ricevitore</td></tr>
<tr><td class="l"><b>Tono subaudio</b></td><td class="l">modulazione esterna o interna a bassa frequenza</td><td class="l">verificare CTCSS di ripetitori e radio</td></tr>
<tr><td class="l"><b>DTMF / 1750 Hz</b></td><td class="l">modulazione esterna da un generatore audio</td><td class="l">apertura di ripetitori, telecomandi</td></tr>
<tr><td class="l"><b>Rumore</b></td><td class="l">alcuni generatori hanno una sorgente interna</td><td class="l">AGC, filtri, prove di riduzione del rumore</td></tr>
<tr><td class="l"><b>Sweep di frequenza</b></td><td class="l">funzione sweep o modulazione esterna DC</td><td class="l">risposta di filtri (con un rivelatore o l'analizzatore)</td></tr>
<tr><td class="l"><b>Segnali digitali</b></td><td class="l">generatore vettoriale o SDR</td><td class="l">BER e sensibilità dei modi digitali</td></tr></table>''')
D.add("Verificare la modulazione con l'analizzatore",'''<div class="two"><div><ul>
<li><b>AM</b>: portante e due righe a ±f<sub>m</sub>; dalla differenza in dB ricavi m (m = 2·10<sup>−Δ/20</sup>).</li>
<li><b>FM</b>: righe a ±n·f<sub>m</sub> con ampiezze J<sub>n</sub>(β); il nullo della portante a β = 2,405 tara la deviazione.</li>
<li><b>Impulsi</b>: in zero span vedi l'inviluppo, i tempi di salita e l'on/off ratio.</li></ul></div><div>
<h3>Cosa cercare</h3><ul class="small"><li>Bande laterali AM <b>asimmetriche</b>: c'è anche una modulazione di fase o di frequenza indesiderata.</li>
<li>Righe in più (2·f<sub>m</sub>, 3·f<sub>m</sub>) in AM: distorsione del modulatore.</li>
<li>FM che "sporca" il canale adiacente: deviazione eccessiva o tono di modulazione distorto.</li>
<li>Tutti i dettagli matematici di AM e FM sono nel modulo sulla potenza del segnale e dello spettro.</li></ul></div></div>''')
rows=[("Toni di prova","1 kHz; FM 3 kHz (25 kHz) o 1,5 kHz (12,5 kHz); AM 30 %"),("AM","bande laterali a 20·log(m/2) dBc; picco +6 dB a m = 100 %"),("FM","β = Δf/f<sub>m</sub>; nullo di Bessel a 2,405"),("Impulsi","TDMA, AGC, squelch; on/off ratio"),("Esterna","audio, DC per sweep, I/Q per il digitale")]
D.add("Riepilogo",'<table class="sum">'+"".join(f'<tr><td class="l" style="width:200px"><b>{a}</b></td><td class="l">{b}</td></tr>' for a,b in rows)+'</table>')
D.render(); pdf("GEN_Modulazioni_IV3HGA.pdf")
