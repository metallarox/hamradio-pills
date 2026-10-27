import numpy as np
from deck import mpl_setup
plt=mpl_setup(); A="#0a1a2e"; B="#1593d1"; O="#e0563b"; G="#9aa5b4"; V="#2a9d5c"
f=np.logspace(np.log10(0.3),np.log10(300),300)
fig,ax=plt.subplots(figsize=(5.6,4.0))
for (c,d,n,col,ls) in [(72.5,27.7,"residenziale",O,"-"),(67.2,27.7,"rurale",B,"-"),(53.6,28.6,"rurale tranquillo",V,"-")]:
    ax.plot(f,c-d*np.log10(f),color=col,lw=2.2,ls=ls,label=n)
fg=f[f>=10]; ax.plot(fg,52-23*np.log10(fg),color=A,lw=2,ls="--",label="galattico")
ax.axhline(0,color=G,lw=1); ax.text(40,2,"kT₀B (290 K)",color="#555",fontsize=9)
for b,fb in [("160 m",1.85),("40 m",7.1),("20 m",14.2),("10 m",28.5),("2 m",145)]:
    ax.axvline(fb,color=G,lw=.6,ls=":"); ax.text(fb*1.04,84,b,fontsize=9,color="#555")
ax.set_xscale("log"); ax.set_xlim(0.3,300); ax.set_ylim(-5,90)
ax.set_xticks([0.3,1,3,10,30,100,300]); ax.set_xticklabels(["0,3","1","3","10","30","100","300"])
ax.set_xlabel("frequenza (MHz)"); ax.set_ylabel("Fa (dB sopra kT₀B)"); ax.grid(alpha=.25,which="both"); ax.legend(frameon=False,fontsize=8.5,loc="lower left")
fig.tight_layout(); fig.savefig("itu.svg",transparent=True)
rng=np.random.default_rng(3); n=600; t=np.arange(n)
g=rng.normal(0,1,n); imp=0.3*rng.normal(0,1,n)
for k in rng.choice(n,8,replace=False): imp[k:k+3]+=rng.choice([-1,1])*rng.uniform(4,7)*np.array([1,.5,.2])[:len(imp[k:k+3])]
fig,axs=plt.subplots(2,2,figsize=(9.6,3.9),gridspec_kw=dict(width_ratios=[3,1]))
for r,(x,col,nm) in enumerate([(g,B,"gaussiano (termico)"),(imp,O,"impulsivo (scariche, motori, PLC)")]):
    axs[r,0].plot(t,x,color=col,lw=.9); axs[r,0].set_ylim(-8,8); axs[r,0].set_yticks([]); axs[r,0].set_title(nm,fontsize=10,loc="left")
    axs[r,1].hist(x,bins=40,range=(-8,8),orientation="horizontal",color=col,alpha=.8); axs[r,1].set_yticks([]); axs[r,1].set_xticks([])
axs[1,0].set_xlabel("tempo"); axs[1,1].set_xlabel("istogramma")
axs[0,0].set_xticks([]); fig.tight_layout(); fig.savefig("types.svg",transparent=True)
ff=np.logspace(1,5,200)
fig,ax=plt.subplots(figsize=(5.6,3.6))
ax.plot(ff,0*ff,color=B,lw=2.2,label="bianco: stessa densità ovunque")
ax.plot(ff,-10*np.log10(ff/10),color=O,lw=2.2,label="rosa (1/f): −3 dB per ottava")
ax.plot(ff,10*np.log10(1+1000/ff),color=A,lw=1.6,ls="--",label="amplificatore reale: 1/f + bianco")
ax.set_xscale("log"); ax.set_ylim(-45,25); ax.set_xlabel("frequenza (Hz)"); ax.set_ylabel("densità (dB, relativa)")
ax.grid(alpha=.25,which="both"); ax.legend(frameon=False,fontsize=9,loc="lower left"); ax.text(1000,12,"corner ≈ 1 kHz",fontsize=9,color=A)
fig.tight_layout(); fig.savefig("color.svg",transparent=True)
