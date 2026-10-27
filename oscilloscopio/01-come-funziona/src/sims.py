import numpy as np
from deck import mpl_setup
plt=mpl_setup(); A="#0a1a2e"; B="#1593d1"; G="#9aa5b4"
# bandwidth vs square wave (10 MHz square through gaussian lowpass)
t=np.linspace(0,200e-9,8000); f0=10e6
sq=np.where((t*f0)%1<0.5,1.0,0.0)
def lp(x,bw):
    dt=t[1]-t[0]; tr=0.35/bw; sig=tr/2.563  # 10-90 of gaussian = 2.563 sigma
    k=np.arange(-int(5*sig/dt),int(5*sig/dt)+1)*dt; g=np.exp(-0.5*(k/sig)**2); g/=g.sum()
    return np.convolve(np.concatenate((x,x,x)),g,mode="same")[len(x):2*len(x)]
fig,ax=plt.subplots(figsize=(10,3.6))
for bw,col,lab in((20e6,"#9cc9e6","banda 20 MHz"),(50e6,B,"banda 50 MHz"),(200e6,A,"banda 200 MHz")):
    ax.plot(t*1e9,lp(sq,bw)+0,color=col,lw=2,label=f"{lab}: t_s ≈ {0.35/bw*1e9:.1f} ns".replace(".",","))
ax.set_xlabel("tempo (ns)"); ax.set_ylabel("ampiezza"); ax.legend(frameon=False,loc="upper center",bbox_to_anchor=(0.5,1.2),ncol=3,fontsize=10); ax.grid(alpha=.25); ax.set_xlim(0,200)
fig.tight_layout(); fig.savefig("bw.svg",transparent=True)
# aliasing
tt=np.linspace(0,2e-6,4000); fs=10e6; fsig=9e6
ts=np.arange(0,2e-6,1/fs)
fig,ax=plt.subplots(figsize=(6.4,3.6))
ax.plot(tt*1e6,np.sin(2*np.pi*fsig*tt),color=G,lw=1,label="segnale vero: 9 MHz")
ax.plot(ts*1e6,np.sin(2*np.pi*fsig*ts),"o",color=A,ms=5,label="campioni a 10 MS/s")
ax.plot(tt*1e6,np.sin(2*np.pi*(fsig-fs)*tt),color=B,lw=2.2,label="quello che vedi: 1 MHz")
ax.set_xlabel("tempo (µs)"); ax.set_ylim(-1.4,3.0); ax.legend(frameon=False,loc="upper center",ncol=1,fontsize=10); ax.grid(alpha=.25)
fig.tight_layout(); fig.savefig("alias.svg",transparent=True)
