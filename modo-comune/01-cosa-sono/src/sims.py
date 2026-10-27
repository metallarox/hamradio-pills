import numpy as np
from deck import mpl_setup
plt=mpl_setup(); A="#0a1a2e"; B="#1593d1"; O="#e0563b"; G="#9aa5b4"
L=np.linspace(0.02,1.25,800)  # lunghezza esterna della calza in lunghezze d'onda
Z0=300; loss=0.06
Zin=np.abs(Z0*np.tanh((loss+1j*2*np.pi)*L))
Zarm=73/2
Icm=np.abs(Zarm/(Zarm+Zin))  # quota di corrente che "sceglie" la calza (modello indicativo)
fig,ax=plt.subplots(figsize=(6,3.8))
ax.plot(L,20*np.log10(Icm),color=O,lw=2.2)
for x,t in [(0.5,"λ/2"),(1.0,"λ")]: ax.axvline(x,color=G,ls=":",lw=1); ax.text(x+0.01,-3,t,color="#555",fontsize=10)
for x,t in [(0.25,"λ/4"),(0.75,"3λ/4")]: ax.axvline(x,color=G,ls=":",lw=1); ax.text(x+0.01,-36,t,color="#555",fontsize=10)
ax.set_xlabel("lunghezza della calza fino a terra (in λ)"); ax.set_ylabel("corrente di modo comune (dB rel.)")
ax.set_ylim(-42,2); ax.grid(alpha=.25)
fig.tight_layout(); fig.savefig("length.svg",transparent=True)
