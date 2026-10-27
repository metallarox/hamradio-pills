import numpy as np
from deck import mpl_setup
plt=mpl_setup(); A="#0a1a2e"; B="#1593d1"; G="#9aa5b4"; O="#e0563b"
# AC coupling tilt: 20 Hz square, AC coupling corner ~5 Hz
t=np.linspace(0,0.15,6000); f=20; sq=np.where((t*f)%1<0.5,1.0,0.0)
fc=5; tau=1/(2*np.pi*fc); dt=t[1]-t[0]; a=tau/(tau+dt)
y=np.zeros_like(sq)
# steady-state: run 3 cycles warmup
x=np.concatenate([np.where((np.arange(0,0.3,dt)*f)%1<0.5,1.0,0.0),sq]); yy=np.zeros_like(x)
for i in range(1,len(x)): yy[i]=a*(yy[i-1]+x[i]-x[i-1])
y=yy[-len(t):]
fig,ax=plt.subplots(figsize=(9.6,3.2))
ax.plot(t*1e3,sq+1.2,color=A,lw=2,label="accoppiamento DC: onda quadra 0–1 V")
ax.plot(t*1e3,y,color=O,lw=2,label="accoppiamento AC: livello perso e fianchi inclinati")
ax.set_xlabel("tempo (ms)"); ax.set_yticks([]); ax.legend(frameon=False,loc="upper center",bbox_to_anchor=(0.5,1.22),ncol=2,fontsize=10); ax.grid(alpha=.25)
fig.tight_layout(); fig.savefig("tilt.svg",transparent=True)
