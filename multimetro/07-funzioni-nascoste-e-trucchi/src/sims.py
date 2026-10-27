import numpy as np
from deck import mpl_setup
plt=mpl_setup(); A="#0a1a2e"; B="#1593d1"; G="#9aa5b4"; O="#e0563b"
I=np.linspace(0,25,100); E=12.62; R=0.02
fig,ax=plt.subplots(figsize=(6.0,3.8)); ax.plot(I,E-R*I,color=B,lw=2.2)
for i,lab in((1,"carico leggero: 1 A → 12,60 V"),(21,"in trasmissione: 21 A → 12,20 V")):
    v=E-R*i; ax.plot(i,v,"o",color=A); ax.annotate(lab.replace(".",","),(i,v),xytext=(8 if i<10 else -200,8 if i<10 else -22),textcoords="offset points",color=A,fontsize=11)
ax.text(12,12.5,"pendenza = −R interna",color=O,fontsize=11)
ax.set_xlabel("corrente (A)"); ax.set_ylabel("tensione ai morsetti (V)"); ax.set_ylim(12.0,12.75); ax.grid(alpha=.25)
fig.tight_layout(); fig.savefig("rint.svg",transparent=True)
