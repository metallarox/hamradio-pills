import numpy as np
from deck import mpl_setup
plt=mpl_setup(); A="#0a1a2e"; B="#1593d1"; O="#e0563b"; G="#9aa5b4"
t=np.linspace(0,2e-3,8000); fm=1e3; fc=12e3; m=np.sin(2*np.pi*fm*t)
fig,axs=plt.subplots(4,1,figsize=(10,4.2),sharex=True)
axs[0].plot(t*1e3,m,color=O,lw=2); axs[0].set_ylabel("audio",fontsize=10)
axs[1].plot(t*1e3,(1+0.7*m)*np.cos(2*np.pi*fc*t),color=B,lw=1); axs[1].plot(t*1e3,1+0.7*m,color=A,lw=1,ls="--"); axs[1].set_ylabel("AM",fontsize=10)
ph=2*np.pi*fc*t+ (5e3/fm)*(-np.cos(2*np.pi*fm*t))
axs[2].plot(t*1e3,np.cos(2*np.pi*fc*t+ 2.5*(-np.cos(2*np.pi*fm*t))*1),color=B,lw=1); axs[2].set_ylabel("FM",fontsize=10)
axs[3].plot(t*1e3,np.cos(2*np.pi*fc*t+2.5*m),color=B,lw=1); axs[3].set_ylabel("PM",fontsize=10)
for a in axs: a.set_yticks([]); a.grid(alpha=.2)
axs[3].set_xlabel("tempo (ms)")
fig.tight_layout(); fig.savefig("time.svg",transparent=True)
# spectra AM / DSB / USB / LSB
fig,axs=plt.subplots(1,4,figsize=(11,2.9),sharey=True)
def bars(ax,items,title):
    for f,a,c in items: ax.bar(f,a,width=0.25,color=c)
    ax.set_title(title,color=A,fontsize=12); ax.set_xlim(-4,4); ax.set_xticks([-3,0,3]); ax.set_xticklabels(["fc−3k","fc","fc+3k"],fontsize=9); ax.set_yticks([])
    ax.axvline(0,color=G,ls=":",lw=1)
band=np.linspace(0.3,3,10)
bars(axs[0],[(0,1,A)]+[(f,0.35,B) for f in band]+[(-f,0.35,B) for f in band],"AM")
bars(axs[1],[(f,0.35,B) for f in band]+[(-f,0.35,B) for f in band],"DSB (senza portante)")
bars(axs[2],[(f,0.35,B) for f in band],"USB")
bars(axs[3],[(-f,0.35,B) for f in band],"LSB")
fig.tight_layout(); fig.savefig("ssb.svg",transparent=True)
# CW keying envelope
t=np.linspace(0,0.25,5000); key=((t>0.03)&(t<0.09))|((t>0.13)&(t<0.22))
def env(rt):
    k=key.astype(float)
    if rt==0: return k
    n=int(rt/(t[1]-t[0])); w=np.hanning(2*n); w/=w.sum(); return np.convolve(k,w,mode="same")
fig,ax=plt.subplots(figsize=(6.4,3.2))
ax.plot(t*1e3,env(0)+1.3,color=O,lw=2,label="fronti ripidi: key click")
ax.plot(t*1e3,env(0.005),color=B,lw=2,label="fronti di ~5 ms: pulito")
ax.set_yticks([]); ax.set_xlabel("tempo (ms)"); ax.legend(frameon=False,loc="upper right",fontsize=10); ax.set_ylim(-0.2,2.9); ax.grid(alpha=.2)
fig.tight_layout(); fig.savefig("cw.svg",transparent=True)
