import numpy as np
from deck import mpl_setup
plt=mpl_setup(); A="#0a1a2e"; B="#1593d1"; O="#e0563b"; C2="#22b8f0"; G="#9aa5b4"
# burst structure
parts=[("3",3,G),("57 bit dati",57,B),("1",1,G),("26 training",26,O),("1",1,G),("57 bit dati",57,B),("3",3,G),("8,25 guardia",8.25,"#e5e8ec")]
fig,ax=plt.subplots(figsize=(10.5,1.9)); x=0
for n,w,c in parts:
    ax.barh(0,w,left=x,color=c,edgecolor="white",height=0.6); 
    if w>6: ax.text(x+w/2,0,n,ha="center",va="center",fontsize=10,color="white" if c in (B,O) else A)
    x+=w
ax.set_xlim(0,156.25); ax.set_yticks([]); ax.set_xlabel("bit (156,25 periodi = 577 µs)"); ax.text(0,0.45,"tail",fontsize=9,color="#555")
fig.tight_layout(); fig.savefig("burst.svg",transparent=True)
# GMSK frequency trajectory
rng=np.random.default_rng(1); bits=np.array([1,1,-1,1,-1,-1,-1,1,1,-1]); sps=32
nrz=np.repeat(bits,sps).astype(float)
BT=0.3; t=np.arange(-2*sps,2*sps+1)/sps; s=np.sqrt(np.log(2))/(2*np.pi*BT); g=np.exp(-t**2/(2*s**2)); g/=g.sum()
fg=np.convolve(nrz,g,mode="same")
fig,axs=plt.subplots(1,2,figsize=(10,3.2),gridspec_kw=dict(width_ratios=[1.7,1]))
ax=axs[0]; tt=np.arange(len(nrz))/sps
ax.plot(tt,nrz*67.7,color=G,lw=1.5,label="MSK (salti)"); ax.plot(tt,fg*67.7,color=B,lw=2.2,label="GMSK (BT = 0,3)")
ax.set_xlabel("bit"); ax.set_ylabel("deviazione (kHz)"); ax.legend(frameon=False,fontsize=9,loc="lower right"); ax.grid(alpha=.2)
ax=axs[1]; ph=np.cumsum(fg)*np.pi/2/sps; z=np.exp(1j*ph)
ax.plot(z.real,z.imag,color=B,lw=2); ax.set_aspect("equal"); ax.set_xticks([]); ax.set_yticks([]); ax.set_title("I/Q: sempre sul cerchio",color=A,fontsize=11)
ax.axhline(0,color=G,lw=.6); ax.axvline(0,color=G,lw=.6)
fig.tight_layout(); fig.savefig("gmsk.svg",transparent=True)
# frame
fig,ax=plt.subplots(figsize=(10.5,1.8)); cols=[B,O,C2,A,"#7fb3d5","#f5b041","#76d7c4","#bb8fce"]
for i in range(16): ax.barh(0,0.577*0.95,left=i*0.577,color=cols[i%8],height=0.6)
for i in range(8): ax.text(i*0.577+0.29,0.45,f"TS{i}",ha="center",fontsize=8,color=A)
ax.set_xlim(0,9.23); ax.set_yticks([]); ax.set_xlabel("tempo (ms): trama di 4,615 ms con 8 slot da 0,577 ms")
fig.tight_layout(); fig.savefig("frame.svg",transparent=True)
