import numpy as np
from deck import mpl_setup
plt=mpl_setup(); A="#0a1a2e"; B="#1593d1"; O="#e0563b"; C2="#22b8f0"; G="#9aa5b4"
cols=[B,O,C2,A,"#7fb3d5","#f5b041"]
fig,axs=plt.subplots(1,4,figsize=(11.5,3.2))
ax=axs[0]
for i in range(4): ax.add_patch(plt.Rectangle((0,i*1.0+0.1),10,0.8,color=cols[i]))
ax.set_title("FDMA",color=A,fontsize=13)
ax=axs[1]
for i in range(8): ax.add_patch(plt.Rectangle((i*1.25+0.05,0.1),1.15,3.8,color=cols[i%4]))
ax.set_title("TDMA",color=A,fontsize=13)
ax=axs[2]
for i in range(4): ax.add_patch(plt.Rectangle((0,0.1),10,3.8,color=cols[i],alpha=0.35))
ax.text(5,2,"tutti insieme,\ncodici diversi",ha="center",va="center",color=A,fontsize=11)
ax.set_title("CDMA",color=A,fontsize=13)
ax=axs[3]; rng=np.random.default_rng(2)
for ti in range(10):
    for fi in range(8): ax.add_patch(plt.Rectangle((ti+0.05,fi*0.5+0.03),0.9,0.44,color=cols[rng.integers(4)]))
ax.set_title("OFDMA",color=A,fontsize=13)
for ax in axs: ax.set_xlim(0,10); ax.set_ylim(0,4); ax.set_xticks([]); ax.set_yticks([]); ax.set_xlabel("tempo"); ax.set_ylabel("frequenza")
fig.tight_layout(); fig.savefig("grids.svg",transparent=True)
# CDMA spreading
rng=np.random.default_rng(4); bits=np.array([1,-1,1]); N=8; code=np.array([1,-1,1,1,-1,-1,1,-1])
tx=np.repeat(bits,N)*np.tile(code,len(bits))
fig,axs=plt.subplots(4,1,figsize=(9.6,4.2),sharex=True)
x=np.arange(len(tx)+1)
axs[0].step(x,np.r_[np.repeat(bits,N),bits[-1]],where="post",color=O,lw=2); axs[0].set_ylabel("dati",fontsize=10)
axs[1].step(x,np.r_[np.tile(code,3),code[-1]],where="post",color=A,lw=1.6); axs[1].set_ylabel("codice",fontsize=10)
axs[2].step(x,np.r_[tx,tx[-1]],where="post",color=B,lw=1.6); axs[2].set_ylabel("trasmesso",fontsize=10)
rx=tx+rng.normal(0,1.0,len(tx)); de=(rx*np.tile(code,3)).reshape(3,N).sum(1)/N
axs[3].step(x,np.r_[np.repeat(de,N),de[-1]],where="post",color=O,lw=2); axs[3].set_ylabel("ricostruito",fontsize=10)
for a in axs: a.set_yticks([]); a.grid(alpha=.2); a.set_ylim(-1.8,1.8)
axs[3].set_xlabel("chip (8 chip per bit)")
fig.tight_layout(); fig.savefig("cdma.svg",transparent=True)
