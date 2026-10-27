import numpy as np, math, json
from deck import mpl_setup
plt=mpl_setup(); A="#0a1a2e"; B="#1593d1"; O="#e0563b"; G="#9aa5b4"
f=145; d=50
fspl=32.45+20*math.log10(f)+20*math.log10(d)
steps=[("TX 100 W",50),("cavo 30 m\n−2,6 dB",-2.6),("connettori\n−0,3 dB",-0.3),("yagi\n+11 dBi",11),("spazio libero\n50 km",-fspl),("antenna RX\n+6 dBi",6),("cavo RX\n−2 dB",-2)]
lv=[];x=0;cur=0
for i,(n,v) in enumerate(steps):
    cur = v if i==0 else cur+v; lv.append(cur)
fig,ax=plt.subplots(figsize=(10.5,3.8))
xs=np.arange(len(lv)); ax.step(xs,lv,where="mid",color=B,lw=2.4); ax.plot(xs,lv,"o",color=A)
for i,(n,v) in enumerate(steps):
    ax.annotate(f"{lv[i]:.1f} dBm".replace(".",","),(i,lv[i]),xytext=(0,9),textcoords="offset points",ha="center",fontsize=10,color=A)
ax.set_xticks(xs); ax.set_xticklabels([s[0] for s in steps],fontsize=10)
ax.axhline(-121,color=O,ls="--"); ax.text(4.6,-116,"sensibilità RX −121 dBm",color=O,fontsize=10)
ax.set_ylabel("livello (dBm)"); ax.set_ylim(-130,72); ax.grid(alpha=.25,axis="y")
fig.tight_layout(); fig.savefig("budget.svg",transparent=True)
json.dump(dict(fspl=fspl,eirp=lv[3],pr=lv[-1]),open("vals.json","w")); print(fspl,lv)
