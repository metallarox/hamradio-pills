import numpy as np, json
from scipy.special import jv
from deck import mpl_setup
plt=mpl_setup(); A="#0a1a2e"; B="#1593d1"; G="#9aa5b4"; out={}
# AM bars
fig,ax=plt.subplots(figsize=(6.0,3.8))
for m,col,off in((0.5,G,-0.12),(1.0,B,0.12)):
    p=[100*m*m/4,100,100*m*m/4]; ax.bar(np.array([-1,0,1])+off,p,width=0.22,color=col,label=f"m = {int(m*100)} %")
    for i,(x,y) in enumerate(zip(np.array([-1,0,1])+off,p)):
        if i==1 and m<1: continue
        ax.text(x if i!=1 else 0,y+2,f"{y:g} W".replace(".",","),ha="center",fontsize=10,color=A)
ax.set_xticks([-1,0,1]); ax.set_xticklabels(["fc − fm","portante fc","fc + fm"]); ax.set_ylabel("potenza della riga (W)"); ax.set_ylim(0,118)
ax.legend(frameon=False,loc="upper right"); ax.grid(alpha=.25,axis="y")
fig.tight_layout(); fig.savefig("am.svg",transparent=True)
# Bessel bars
betas=[0.5,2.405,5.0]
fig,axs=plt.subplots(1,3,figsize=(11,3.4),sharey=True)
for ax,b in zip(axs,betas):
    n=np.arange(-9,10); p=jv(n,b)**2*100
    ax.bar(n,p,color=B,width=0.6); ax.set_title(f"β = {b:g}".replace(".",","),fontsize=13,color=A)
    ax.set_xlabel("n (riga a fc + n·fm)"); ax.grid(alpha=.25,axis="y"); ax.set_xlim(-9.5,9.5)
    ax.text(0.02,0.92,f"portante: {jv(0,b)**2*100:.1f} %".replace(".",","),transform=ax.transAxes,fontsize=10,color=A)
axs[0].set_ylabel("% della potenza totale")
fig.tight_layout(); fig.savefig("bessel_bars.svg",transparent=True)
# tables
def tab(b,P,nmax=6):
    rows=[]
    for k in range(0,nmax+1):
        j=jv(k,b); rows.append((k,float(j),float(j*j*P)))
    return rows
out["t1"]=tab(1.0,50,4); out["t2405"]=tab(2.405,50,5)
for b in (1.0,2.405,5.0):
    s=sum(jv(k,b)**2 for k in range(-60,61)); nc=int(np.floor(b+1)); sc=sum(jv(k,b)**2 for k in range(-nc,nc+1))
    out[f"sum_{b}"]=float(s); out[f"carson_{b}"]=[nc,float(sc)]
print(json.dumps(out,indent=0)); json.dump(out,open("vals.json","w"))
