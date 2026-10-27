import numpy as np
from deck import mpl_setup
plt=mpl_setup(); A="#0a1a2e"; B="#1593d1"; G="#9aa5b4"; O="#e0563b"
pin=np.linspace(-140,10,300); mds=-130; ip3=1.5*(-43)+0.5*130
fig,ax=plt.subplots(figsize=(6.4,4.1))
ax.plot(pin,pin,color=B,lw=2.2,label="fondamentale (1 dB/dB)")
ax.plot(pin,3*pin-2*ip3,color=O,lw=2.2,label="prodotto IM3 (3 dB/dB)")
ax.axhline(mds,color=G,ls="--"); ax.text(-138,mds+2,"MDS −130 dBm",color="#555",fontsize=10)
ax.plot(ip3,ip3,"o",color=A); ax.annotate(f"IP3 = {ip3:.1f} dBm".replace(".",","),(ip3,ip3),xytext=(-110,10),textcoords="offset points",color=A,fontsize=11)
ax.plot(-43,mds,"o",color=O); ax.annotate("toni a −43 dBm:\nIM3 = MDS → DR3 = 87 dB",(-43,mds),xytext=(-128,-55),color=A,fontsize=11,arrowprops=dict(arrowstyle="->",color=A))
ax.set_xlim(-140,10); ax.set_ylim(-150,10); ax.set_xlabel("livello di ciascun tono all'ingresso (dBm)"); ax.set_ylabel("livello riferito all'ingresso (dBm)")
ax.legend(frameon=False,loc="upper left",fontsize=10); ax.grid(alpha=.25)
fig.tight_layout(); fig.savefig("ip3.svg",transparent=True)
