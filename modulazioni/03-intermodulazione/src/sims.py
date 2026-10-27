import numpy as np
from deck import mpl_setup
plt=mpl_setup(); A="#0a1a2e"; B="#1593d1"; O="#e0563b"; G="#9aa5b4"
f1,f2=145.600,145.725; d=f2-f1
prods=[(f1,0,"f1"),(f2,0,"f2"),(2*f1-f2,-40,"2f1−f2"),(2*f2-f1,-40,"2f2−f1"),(3*f1-2*f2,-60,"3f1−2f2"),(3*f2-2*f1,-60,"3f2−2f1"),(4*f1-3*f2,-75,"7°"),(4*f2-3*f1,-75,"7°")]
fig,ax=plt.subplots(figsize=(10,3.4))
for f,l,n in prods:
    c=A if l==0 else (O if "2f" in n and "3" not in n else B)
    ax.vlines(f,-90,l,color=c,lw=3); ax.text(f,l+3,n,ha="center",fontsize=10,color=c)
for f,l,n in prods[:6]: ax.text(f,-97,f"{f:.3f}".replace(".",","),ha="center",fontsize=8,color="#555")
ax.set_ylim(-100,10); ax.set_xlim(145.2,146.15); ax.set_xticks([]); ax.set_ylabel("dBc (indicativo)"); ax.set_xlabel("frequenza (MHz)"); ax.grid(alpha=.2,axis="y")
fig.tight_layout(); fig.savefig("prods.svg",transparent=True)
pin=np.linspace(-60,10,200); ip3=10
fig,ax=plt.subplots(figsize=(5.9,3.8))
ax.plot(pin,pin,color=B,lw=2.2,label="segnale (1 dB/dB)"); ax.plot(pin,3*pin-2*ip3,color=O,lw=2.2,label="IM3 (3 dB/dB)")
ax.plot(ip3,ip3,"o",color=A); ax.text(ip3-26,ip3+3,"IP3 (punto di intercetta)",color=A,fontsize=10)
ax.annotate("",xy=(-20,-20),xytext=(-20,-80),arrowprops=dict(arrowstyle="<->",color=A)); ax.text(-19,-55,"60 dB",color=A,fontsize=10)
ax.annotate("",xy=(-10,-10),xytext=(-10,-50),arrowprops=dict(arrowstyle="<->",color=G)); ax.text(-9,-35,"40 dB",color="#555",fontsize=10)
ax.set_xlim(-60,15); ax.set_ylim(-110,20); ax.set_xlabel("livello di ciascun tono (dBm)"); ax.set_ylabel("uscita (dBm)"); ax.legend(frameon=False,fontsize=9,loc="upper left"); ax.grid(alpha=.25)
fig.tight_layout(); fig.savefig("slopes.svg",transparent=True)
