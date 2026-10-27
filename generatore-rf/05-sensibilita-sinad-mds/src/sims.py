import numpy as np
from deck import mpl_setup
plt=mpl_setup(); A="#0a1a2e"; B="#1593d1"; G="#9aa5b4"; O="#e0563b"
p=np.linspace(-135,-100,300); th=-121
sinad=np.clip(12+1.9*(p-th)*1.6,0,None); sinad=np.where(p<th-6, 3+ (p-(th-6))*0.3,sinad); sinad=np.clip(sinad,0,45)
# smooth model: FM threshold
x=p-th; s=12+ (30/(1+np.exp(-(x-4)/2.5))) -30/(1+np.exp(4/2.5))
s=np.clip(s+ (x<0)*x*1.2,0,45)
fig,ax=plt.subplots(figsize=(6.3,3.9)); ax.plot(p,s,color=B,lw=2.4)
ax.axhline(12,color=O,ls="--"); ax.axvline(th,color=O,ls="--"); ax.plot(th,12,"o",color=O)
ax.annotate("sensibilità: −121 dBm\n(0,2 µV PD) a SINAD 12 dB",(th,12),xytext=(-134.5,30),color=A,fontsize=11,arrowprops=dict(arrowstyle="->",color=A))
ax.text(-112,20,"oltre la soglia il\nrumore sparisce in fretta",color="#555",fontsize=10)
ax.set_xlabel("livello all'ingresso (dBm)"); ax.set_ylabel("SINAD (dB)"); ax.set_ylim(0,48); ax.grid(alpha=.25)
fig.tight_layout(); fig.savefig("sinad.svg",transparent=True)
