import numpy as np
from deck import mpl_setup
plt=mpl_setup(); A="#0a1a2e"; B="#1593d1"; G="#9aa5b4"; O="#e0563b"
off=np.logspace(2,6,300)
def pn(L1k,floor,corner=1e4):
    return 10*np.log10(10**(L1k/10)*(1e3/off)**2*(1+(corner/off))+10**(floor/10))
fig,ax=plt.subplots(figsize=(6.6,4.0))
ax.semilogx(off,pn(-90,-150),color=A,lw=2.2,label="generatore buono")
ax.semilogx(off,pn(-70,-130),color=O,lw=2.2,label="generatore economico")
ax.semilogx(off,pn(-80,-145)+0.0,color=B,lw=2,ls="--",label="LO di un buon ricevitore")
ax.axvline(20e3,color=G,ls=":"); ax.text(22e3,-155,"20 kHz",color="#555")
ax.set_xlabel("distanza dalla portante (Hz)"); ax.set_ylabel("rumore di fase (dBc/Hz)"); ax.set_ylim(-160,-50); ax.legend(frameon=False,loc="lower left",fontsize=10); ax.grid(alpha=.25,which="both")
fig.tight_layout(); fig.savefig("pn.svg",transparent=True)
print(pn(-90,-150)[np.argmin(abs(off-20e3))],pn(-70,-130)[np.argmin(abs(off-20e3))])
