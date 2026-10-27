import numpy as np
from deck import mpl_setup
plt=mpl_setup(); A="#0a1a2e"; B="#1593d1"; O="#e0563b"; G="#9aa5b4"; V="#2a9d5c"
f=np.logspace(np.log10(1),np.log10(200),500)*1e6; w=2*np.pi*f
def Z(R,L,C): return 1/(1/R+1/(1j*w*L)+1j*w*C)
cur=[(Z(30e3,10e-6,5e-12),G,"8 spire di coassiale in aria"),(Z(5e3,60e-6,3e-12),O,"toroide mix 31, 7 spire RG-58"),(Z(4e3,22e-6,2e-12),B,"toroide mix 43, 7 spire RG-58"),(Z(1.2e3,6e-6,0.6e-12),V,"10 perline mix 31 (W2DU)")]
fig,ax=plt.subplots(figsize=(5.8,4.4))
for z,c,n in cur: ax.plot(f/1e6,np.abs(z),color=c,lw=2.2,label=n)
ax.axhspan(1000,5000,color=B,alpha=.07); ax.text(1.1,6000,"obiettivo: > 1 kΩ, meglio 5 kΩ",fontsize=9,color=A)
ax.set_xscale("log"); ax.set_yscale("log"); ax.set_ylim(30,4e4); ax.set_xlim(1,200)
ax.set_xticks([1,2,5,10,20,50,100,200]); ax.set_xticklabels(["1","2","5","10","20","50","100","200"])
ax.set_yticks([100,1000,10000]); ax.set_yticklabels(["100 Ω","1 kΩ","10 kΩ"])
ax.set_xlabel("frequenza (MHz)"); ax.set_ylabel("|Z| di modo comune"); ax.grid(alpha=.25,which="both"); ax.legend(frameon=False,fontsize=9,loc="upper center",bbox_to_anchor=(0.5,-0.2),ncol=2)
fig.tight_layout(); fig.savefig("chokes.svg",transparent=True)
# R vs X for coiled coax
z=cur[0][0]; z2=cur[1][0]
fig,ax=plt.subplots(figsize=(5.6,4.2))
ax.plot(f/1e6,z.real,color=G,lw=2.2,label="R, coassiale in aria"); ax.plot(f/1e6,np.abs(z.imag),color=G,lw=1.5,ls="--",label="|X|, coassiale in aria")
ax.plot(f/1e6,z2.real,color=O,lw=2.2,label="R, toroide mix 31"); ax.plot(f/1e6,np.abs(z2.imag),color=O,lw=1.5,ls="--",label="|X|, toroide mix 31")
ax.set_xscale("log"); ax.set_yscale("log"); ax.set_ylim(30,4e4); ax.set_xlim(1,200)
ax.set_xticks([1,2,5,10,20,50,100,200]); ax.set_xticklabels(["1","2","5","10","20","50","100","200"])
ax.set_yticks([100,1000,10000]); ax.set_yticklabels(["100 Ω","1 kΩ","10 kΩ"]); ax.set_xlabel("frequenza (MHz)"); ax.grid(alpha=.25,which="both"); ax.legend(frameon=False,fontsize=9,loc="upper center",bbox_to_anchor=(0.5,-0.2),ncol=2)
fig.tight_layout(); fig.savefig("rx.svg",transparent=True)
for z,c,n in cur:
  for fm in [3.6,7.1,14.2,28.5]:
    i=np.argmin(abs(f-fm*1e6)); print(n,fm,round(abs(z[i])),round(z[i].real))
