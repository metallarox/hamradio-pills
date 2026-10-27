import numpy as np
from deck import mpl_setup
plt=mpl_setup(); A="#0a1a2e"; B="#1593d1"; O="#e0563b"
p=np.logspace(-6,3,400)  # W
fig,axs=plt.subplots(1,2,figsize=(10.5,3.5))
pts=[(1e-6,"1 µW"),(1e-3,"1 mW"),(1,"1 W"),(100,"100 W"),(1000,"1 kW")]
ax=axs[0]; ax.plot(p,p,color=O,lw=2.2); ax.set_title("scala lineare: tutto schiacciato a zero",color=A,fontsize=12); ax.set_xlabel("potenza (W)"); ax.set_ylabel("W"); ax.grid(alpha=.25)
ax=axs[1]; ax.semilogx(p,10*np.log10(p/1e-3),color=B,lw=2.2); ax.set_title("in dBm: ogni ×10 è un gradino uguale",color=A,fontsize=12)
for v,l in pts: ax.plot(v,10*np.log10(v/1e-3),"o",color=A); ax.annotate(l,(v,10*np.log10(v/1e-3)),xytext=(6,-14),textcoords="offset points",fontsize=10,color=A)
ax.set_xlabel("potenza (W)"); ax.set_ylabel("dBm"); ax.grid(alpha=.25,which="both")
fig.tight_layout(); fig.savefig("lin_log.svg",transparent=True)
