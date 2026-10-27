import numpy as np, json
from deck import mpl_setup
plt=mpl_setup(); A="#0a1a2e"; B="#1593d1"; O="#e0563b"; G="#9aa5b4"
def step(state,u):
    s1,s0=state>>1,state&1
    out=(u^s1^s0, u^s0); ns=(u<<1)|s1; return out,ns
msg=[1,0,1,1,0,0]
st=0; enc=[]
for u in msg: o,st=step(st,u); enc.append(o)
rx=[list(p) for p in enc]; rx[2][0]^=1   # one bit error at time 2
# viterbi
INF=99; pm=[0,INF,INF,INF]; hist=[]; pms=[pm[:]]
for r in rx:
    new=[INF]*4; prev=[None]*4
    for s in range(4):
        if pm[s]>=INF: continue
        for u in (0,1):
            o,ns=step(s,u); d=(o[0]!=r[0])+(o[1]!=r[1]); m=pm[s]+d
            if m<new[ns]: new[ns]=m; prev[ns]=(s,u)
    hist.append(prev); pm=new; pms.append(pm[:])
# traceback from state 0
s=0; path=[0]; dec=[]
for t in range(len(rx)-1,-1,-1):
    ps,u=hist[t][s]; dec.append(u); s=ps; path.append(s)
dec=dec[::-1]; path=path[::-1]
json.dump(dict(enc=enc,rx=rx,dec=dec,pms=pms,path=path),open("vals.json","w")); print(enc,rx,dec,pms,path)
# trellis figure
names=["00","01","10","11"]  # state index -> label (s1 s0)
ypos={0:3,2:2,1:1,3:0}
fig,ax=plt.subplots(figsize=(10.8,4.0))
T=len(rx)
for t in range(T):
    for s in range(4):
        if pms[t][s]>=INF: continue
        for u in (0,1):
            o,ns=step(s,u)
            ax.plot([t,t+1],[ypos[s],ypos[ns]],color=G,lw=1,ls="-" if u==0 else "--",zorder=1)
for t in range(T):
    ax.plot([t,t+1],[ypos[path[t]],ypos[path[t+1]]],color=O,lw=3.5,zorder=2)
for t in range(T+1):
    for s in range(4):
        m=pms[t][s]
        if m>=INF: continue
        ax.plot(t,ypos[s],"o",color=B,ms=16,zorder=3); ax.text(t,ypos[s],str(m),ha="center",va="center",color="white",fontsize=10,zorder=4,fontweight="bold")
for t,r in enumerate(rx):
    err = (t==2)
    ax.text(t+0.5,3.55,f"{r[0]}{r[1]}",ha="center",fontsize=12,color=O if err else A,fontweight="bold" if err else "normal")
ax.text(-0.45,3.55,"ricevuto:",ha="right",fontsize=11,color=A)
ax.set_yticks([ypos[s] for s in range(4)]); ax.set_yticklabels([f"stato {names[s]}" for s in range(4)],fontsize=10)
ax.set_xticks(range(T+1)); ax.set_xlabel("tempo (passi)"); ax.set_xlim(-0.6,T+0.4); ax.set_ylim(-0.5,3.9)
for sp in ("top","right","left"): ax.spines[sp].set_visible(False)
fig.tight_layout(); fig.savefig("trellis.svg",transparent=True)
