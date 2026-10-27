import numpy as np, json
from deck import mpl_setup
plt=mpl_setup(); A="#0a1a2e"; B="#1593d1"
R=200; V0=4.000; V1=3.899; P0=V0**2/(4*R)*1e3; P1=V1**2/(4*R)*1e3; Prf=P0-P1
json.dump(dict(P0=P0,P1=P1,Prf=Prf),open("vals.json","w")); print(P0,P1,Prf)
fig,ax=plt.subplots(figsize=(5.6,4.0))
ax.bar([0],[P0],color=B,width=0.5,label="potenza DC dal ponte"); ax.bar([1],[P1],color=B,width=0.5); ax.bar([1],[Prf],bottom=[P1],color=A,width=0.5,label="potenza RF")
ax.set_xticks([0,1]); ax.set_xticklabels(["senza RF","con RF"]); ax.set_ylabel("potenza nel termistore (mW)"); ax.set_ylim(0,24)
ax.text(0,P0+0.4,f"{P0:.2f} mW".replace(".",","),ha="center",color=A); ax.text(1,P0+0.4,"stessa temperatura,\nstessa resistenza",ha="center",color=A,fontsize=10)
ax.text(1.3,P1+Prf/2,f"RF = {Prf:.2f} mW".replace(".",","),va="center",color=A,fontsize=11)
ax.legend(frameon=False,loc="lower center",fontsize=10); ax.set_xlim(-0.5,1.9)
fig.tight_layout(); fig.savefig("dcsub.svg",transparent=True)
