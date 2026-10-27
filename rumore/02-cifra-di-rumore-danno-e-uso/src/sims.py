import numpy as np
from deck import mpl_setup
plt=mpl_setup(); A="#0a1a2e"; B="#1593d1"; O="#e0563b"; G="#9aa5b4"; V="#2a9d5c"
f=np.logspace(np.log10(1.5),np.log10(450),300)
fig,ax=plt.subplots(figsize=(5.8,3.9))
ax.plot(f,72.5-27.7*np.log10(f),color=O,lw=2.2,label="esterno, residenziale")
ax.plot(f,53.6-28.6*np.log10(f),color=V,lw=2.2,label="esterno, rurale tranquillo")
fg=f[f>=10]; ax.plot(fg,52-23*np.log10(fg),color=A,lw=1.8,ls="--",label="galattico")
for nf,c in [(15,B),(1,G)]:
    ax.axhline(nf,color=c,lw=1.8,ls="-."); ax.text(1.6,nf+1.5,f"NF ricevitore {nf} dB",color=c,fontsize=9)
ax.set_xscale("log"); ax.set_ylim(-5,70); ax.set_xticks([2,5,10,30,100,300]); ax.set_xticklabels(["2","5","10","30","100","300"])
ax.set_xlabel("frequenza (MHz)"); ax.set_ylabel("dB sopra kT₀B"); ax.grid(alpha=.25,which="both"); ax.legend(frameon=False,fontsize=8.5,loc="upper right")
fig.tight_layout(); fig.savefig("who.svg",transparent=True)
# Tsys bars
lab=["nessun\npreamp","preamp\nin stazione","preamp\nin cima al palo"]; ta=201; trx=[2014,423,79]
fig,ax=plt.subplots(figsize=(5.4,3.6))
ax.bar(lab,[ta]*3,color=V,label="cielo (T_a ≈ 200 K)"); ax.bar(lab,trx,bottom=[ta]*3,color=O,label="ricevitore + cavo")
for i,v in enumerate(trx): ax.text(i,ta+v+50,f"{ta+v} K",ha="center",fontsize=10,color=A)
ax.set_ylabel("temperatura di sistema (K)"); ax.set_ylim(0,2600); ax.legend(frameon=False,fontsize=9); ax.grid(alpha=.25,axis="y")
fig.tight_layout(); fig.savefig("tsys.svg",transparent=True)
# dither
fs=48000; n=8192; nb=24; f0=48000/8192*80
rng=np.random.default_rng(2); w=np.hanning(n); fr=np.fft.rfftfreq(n,1/fs)/1000
def spec(dith):
    acc=0
    for b in range(nb):
        t=(np.arange(n)+b*n)/fs; x=1.3*np.sin(2*np.pi*f0*t)
        if dith: x=x+rng.uniform(-.5,.5,n)+rng.uniform(-.5,.5,n)
        acc=acc+np.abs(np.fft.rfft(np.round(x)*w))**2
    return acc
s0=spec(False); s1=spec(True); ref=max(s0.max(),s1.max())
fig,axs=plt.subplots(1,2,figsize=(10,3.2),sharey=True)
for a,s_,ti,c in [(axs[0],s0,"senza dither: armoniche di quantizzazione",O),(axs[1],s1,"con dither: fondo un po' più alto, niente armoniche",B)]:
    a.plot(fr,10*np.log10(s_/ref+1e-14),color=c,lw=.8); a.set_title(ti,fontsize=10,loc="left"); a.set_xlim(0,12); a.set_ylim(-120,5); a.grid(alpha=.25); a.set_xlabel("frequenza (kHz)")
axs[0].set_ylabel("dB"); fig.tight_layout(); fig.savefig("dither.svg",transparent=True)
# noise + SA filter response
ff=np.linspace(6.5,7.7,600); f0=7.1; bw=0.12
H=10*np.log10(1/(1+((ff-f0)/(bw/2))**8)+1e-6)
noise=lambda k: 10*np.log10(np.mean(rng.exponential(1,(k,ff.size)),axis=0))
fig,ax=plt.subplots(figsize=(5.8,3.6))
ax.plot(ff,-30+H+noise(1),color=G,lw=.7,label="una spazzata")
ax.plot(ff,-30+H+noise(50),color=B,lw=1.8,label="media di 50 spazzate")
ax.set_ylim(-100,-20); ax.set_xlabel("frequenza (MHz)"); ax.set_ylabel("dBm (RBW 10 kHz)"); ax.grid(alpha=.25); ax.legend(frameon=False,fontsize=9,loc="upper right")
ax.text(6.52,-26,"limite: rumore del generatore − DANL",fontsize=8.5,color="#555")
fig.tight_layout(); fig.savefig("filt.svg",transparent=True)
