import numpy as np
from deck import mpl_setup
plt=mpl_setup(); A="#0a1a2e"; B="#1593d1"; O="#e0563b"; G="#9aa5b4"
f=np.linspace(-4,4,2000)
fig,axs=plt.subplots(1,3,figsize=(11,3.0),sharey=True)
noise=-95*np.ones_like(f)
def rc(f,w,a=0.22):
    x=abs(f)/w; return np.where(x<=(1-a)/2,1,np.where(x<=(1+a)/2,0.5*(1+np.cos(np.pi/a*(x-(1-a)/2))),1e-6))
ax=axs[0]; ax.plot(f,np.where(abs(f)<0.02,-75,-160),color=O,lw=2); ax.plot(f,noise,color=G,ls="--"); ax.set_title("voce 12,2 kbit/s",color=A,fontsize=11)
ax=axs[1]; ax.plot(f,-75-25+10*np.log10(rc(f,3.84)),color=B,lw=2); ax.plot(f,noise,color=G,ls="--"); ax.set_title("allargata a 3,84 Mchip/s",color=A,fontsize=11)
ax.text(-3.8,-93,"rumore",color="#555",fontsize=9)
ax=axs[2]; ax.plot(f,np.where(abs(f)<0.02,-75,-160),color=O,lw=2); ax.plot(f,noise,color=G,ls="--"); ax.set_title("dopo il despreading",color=A,fontsize=11)
for a in axs: a.set_ylim(-140,-65); a.set_xlabel("MHz"); a.grid(alpha=.2)
axs[0].set_ylabel("dBm/Hz (indicativo)")
fig.tight_layout(); fig.savefig("spread.svg",transparent=True)
# RAKE
fig,ax=plt.subplots(figsize=(5.8,3.2))
d=[0,0.8,2.1]; a=[1,0.6,0.35]
ax.stem(d,a,linefmt=B,markerfmt="o",basefmt=" ")
for x,y,l in zip(d,a,["diretto","riflesso 1","riflesso 2"]): ax.text(x+0.05,y+0.04,l,fontsize=10,color=A)
ax.set_xlabel("ritardo (µs)"); ax.set_ylabel("ampiezza"); ax.set_xlim(-0.3,3); ax.set_ylim(0,1.25); ax.grid(alpha=.2)
ax.text(1.2,1.05,"1 chip = 0,26 µs",color=O,fontsize=10)
fig.tight_layout(); fig.savefig("rake.svg",transparent=True)
