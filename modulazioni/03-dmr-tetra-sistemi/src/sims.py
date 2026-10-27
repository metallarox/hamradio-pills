import numpy as np
from deck import mpl_setup
plt=mpl_setup(); A="#0a1a2e"; B="#1593d1"; O="#e0563b"; G="#9aa5b4"
rng=np.random.default_rng(5)
# DMR 4FSK deviation over time
dib=["01","00","10","11","00","01","11","10","00","11"]; dev={"01":1944,"00":648,"10":-648,"11":-1944}
sps=40; f=np.repeat([dev[d] for d in dib],sps).astype(float)
k=np.exp(-0.5*(np.arange(-40,41)/6)**2); k/=k.sum(); fs=np.convolve(f,k,mode="same")
t=np.arange(len(f))/sps/4.8
fig,ax=plt.subplots(figsize=(7.2,3.4)); ax.plot(t,fs,color=B,lw=2.2)
for i,d in enumerate(dib): ax.text((i+0.5)/4.8,2250,d,ha="center",fontsize=10,color=A)
for v in (1944,648,-648,-1944): ax.axhline(v,color=G,ls=":",lw=1)
ax.set_yticks([-1944,-648,648,1944]); ax.set_xlabel("tempo (ms)"); ax.set_ylabel("deviazione (Hz)"); ax.set_ylim(-2500,2600); ax.grid(alpha=.15)
fig.tight_layout(); fig.savefig("dmr4fsk.svg",transparent=True)
# TDMA timelines
fig,axs=plt.subplots(2,1,figsize=(10.5,3.4))
ax=axs[0]
for i in range(4):
    ax.barh(0,27.5,left=i*60,height=0.6,color=B); ax.barh(0,27.5,left=i*60+30,height=0.6,color=O)
ax.text(5,0.45,"slot 1",color=B,fontsize=10); ax.text(35,0.45,"slot 2",color=O,fontsize=10)
ax.set_xlim(0,240); ax.set_yticks([]); ax.set_title("DMR: 2 slot da 30 ms (burst 27,5 ms), trama 60 ms, canale 12,5 kHz",color=A,fontsize=11)
ax=axs[1]; cols=[B,O,"#22b8f0",A]
for i in range(4):
    for s in range(4): ax.barh(0,14.167*0.95,left=i*56.67+s*14.167,height=0.6,color=cols[s])
for s in range(4): ax.text(s*14.167+1,0.45,f"TS{s+1}",color=cols[s],fontsize=9)
ax.set_xlim(0,240); ax.set_yticks([]); ax.set_xlabel("tempo (ms)"); ax.set_title("TETRA: 4 slot da 14,17 ms, trama 56,67 ms, canale 25 kHz",color=A,fontsize=11)
fig.tight_layout(); fig.savefig("tdma.svg",transparent=True)
# pi/4 DQPSK
fig,axs=plt.subplots(1,2,figsize=(8.6,4.6))
ax=axs[0]; a=np.exp(1j*np.pi/4*np.arange(8))
ax.plot(a[0::2].real,a[0::2].imag,"o",color=B,ms=11,label="simboli pari"); ax.plot(a[1::2].real,a[1::2].imag,"s",color=O,ms=9,label="simboli dispari")
ax.set_aspect("equal"); ax.set_xlim(-1.4,1.4); ax.set_ylim(-1.4,1.4); ax.axhline(0,color=G,lw=.6); ax.axvline(0,color=G,lw=.6); ax.set_xticks([]); ax.set_yticks([]); ax.set_title("8 posizioni: ● e ■ si alternano",color=A,fontsize=11)
ax=axs[1]; ph=0; pts=[1+0j]; ch={0:np.pi/4,1:3*np.pi/4,2:-np.pi/4,3:-3*np.pi/4}
for _ in range(60): ph+=ch[rng.integers(4)]; pts.append(np.exp(1j*ph))
pts=np.array(pts)
for i in range(len(pts)-1):
    seg=np.linspace(pts[i],pts[i+1],30); ax.plot(seg.real,seg.imag,color=B,lw=.8,alpha=.6)
ax.plot(0,0,"x",color=O,ms=12,mew=3); ax.text(-1.35,-1.35,"le transizioni non passano per lo zero (×)",color=O,fontsize=9)
ax.set_aspect("equal"); ax.set_xlim(-1.4,1.4); ax.set_ylim(-1.4,1.4); ax.set_xticks([]); ax.set_yticks([]); ax.set_title("transizioni ±45° e ±135°",color=A,fontsize=11)
fig.tight_layout(); fig.savefig("pi4.svg",transparent=True)
