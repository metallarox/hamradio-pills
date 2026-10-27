import numpy as np
from deck import mpl_setup
plt=mpl_setup(); A="#0a1a2e"; B="#1593d1"; G="#9aa5b4"
p=np.linspace(-65,20,400); P=10**(p/10)*1e-3; P0=10**(-15/10)*1e-3
v=50*P/(1+np.sqrt(P/P0))+20e-9   # V; offset = rumore/termico
fig,ax=plt.subplots(figsize=(6.6,4.1))
ax.semilogy(p,v*1e3,color=B,lw=2.4)
ax.axvspan(-65,-20,color="#e8f6fd"); ax.axvspan(0,20,color="#f3f5f8")
ax.text(-62,30,"zona quadratica\nV ∝ P\nvero valore efficace",color=A,fontsize=11)
ax.text(1,1e-3,"zona lineare\nV ∝ tensione\nrivelatore di picco",color=A,fontsize=11)
ax.text(-19,2e-4,"transizione",color="#555",fontsize=10)
ax.set_xlabel("potenza d'ingresso (dBm)"); ax.set_ylabel("tensione rivelata (mV)"); ax.grid(alpha=.25,which="both")
fig.tight_layout(); fig.savefig("diode.svg",transparent=True)
