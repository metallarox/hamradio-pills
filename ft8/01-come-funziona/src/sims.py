import numpy as np
from deck import mpl_setup
plt=mpl_setup(); A="#0a1a2e"; B="#1593d1"; O="#e0563b"; G="#9aa5b4"
rng=np.random.default_rng(11)
costas=[3,1,4,0,6,5,2]
def tones():
    d=list(rng.integers(0,8,58)); return costas+d[:29]+costas+d[29:]+costas
# single signal tone map
tn=tones()
fig,ax=plt.subplots(figsize=(10.5,3.3))
for i,t in enumerate(tn):
    c=O if (i<7 or 36<=i<43 or i>=72) else B
    ax.add_patch(plt.Rectangle((i*0.16,t*6.25),0.16,6.25,color=c))
ax.set_xlim(0,79*0.16); ax.set_ylim(0,50); ax.set_xlabel("tempo (s)"); ax.set_ylabel("tono (Hz sopra la base)")
ax.set_yticks(np.arange(0,51,6.25)); ax.set_yticklabels([f"{x:g}".replace(".",",") for x in np.arange(0,51,6.25)],fontsize=8)
ax.text(0.1,52,"Costas",color=O,fontsize=10); ax.text(36*0.16,52,"Costas",color=O,fontsize=10); ax.text(72*0.16,52,"Costas",color=O,fontsize=10)
ax.text(12*0.16,52,"29 simboli di dati",color=B,fontsize=10); ax.text(48*0.16,52,"29 simboli di dati",color=B,fontsize=10)
ax.grid(alpha=.15); fig.tight_layout(); fig.savefig("tonemap.svg",transparent=True)
# waterfall simulation
T=15; fs_t=0.04; tt=np.arange(0,T,fs_t); ff=np.arange(200,3000,6.25)
W=rng.normal(0,1,(len(tt),len(ff)))**2*0.5
for _ in range(14):
    f0=rng.uniform(250,2900); st=rng.uniform(0.2,0.8); a=10**(rng.uniform(0.2,1.8)); tn=tones()
    for i,t in enumerate(tn):
        ts=st+i*0.16; idx=(tt>=ts)&(tt<ts+0.16); fi=np.argmin(abs(ff-(f0+t*6.25))); W[idx,fi]+=a
fig,ax=plt.subplots(figsize=(10.5,3.4)); ax.imshow(np.log10(W+0.05).T,aspect="auto",origin="lower",extent=(0,T,200,3000),cmap="viridis",vmin=-0.6,vmax=1.4)
ax.axvline(12.64+0.5,color="w",ls=":",lw=1); ax.set_xlabel("tempo (s)"); ax.set_ylabel("audio (Hz)")
fig.tight_layout(); fig.savefig("waterfall.svg",transparent=True,dpi=130)
# bandwidth comparison
fig,ax=plt.subplots(figsize=(6.2,3.3))
ax.barh(["SSB","CW","FT8"],[2400,500,50],color=[G,B,O])
for y,v in zip(range(3),[2400,500,50]): ax.text(v+40,y,f"{v} Hz",va="center",color=A,fontsize=11)
ax.set_xlim(0,3000); ax.set_xlabel("banda occupata (Hz)"); ax.grid(alpha=.2,axis="x")
fig.tight_layout(); fig.savefig("bw.svg",transparent=True)
