import numpy as np, json
from scipy.special import jv
from deck import sa_trace, mpl_setup
plt=mpl_setup(); A="#0a1a2e"; B="#1593d1"; G="#9aa5b4"; out={}
def ann(ax,x,y,t,dx,dy):
    ax.annotate(t,(x,y),xytext=(dx,dy),textcoords="offset points",color=A,fontsize=11,arrowprops=dict(arrowstyle="->",color=A))
# harmonics
f=np.linspace(1e6,500e6,6000); tones=[(145e6,0),(290e6,-52),(435e6,-63)]
fig,ax=plt.subplots(figsize=(6.6,4.0)); tr=sa_trace(f,tones,1e6,-160,seed=3)
ax.plot(f/1e6,tr,color=B,lw=1.4); ax.set_ylim(-100,10)
ann(ax,145,0,"fondamentale\n0 dBm",25,-30); ann(ax,290,-52,"2ª: −52 dBc",-55,30); ann(ax,435,-63,"3ª: −63 dBc",-30,45)
ax.set_xlabel("f (MHz)"); ax.set_ylabel("livello (dBm)"); ax.grid(alpha=.25)
fig.tight_layout(); fig.savefig("harm.svg",transparent=True)
# IMD
f=np.linspace(14.17e6,14.23e6,4001); f1=14.195e6; f2=14.205e6; P=0; d=60
tones=[(f1,P),(f2,P),(2*f1-f2,P-d),(2*f2-f1,P-d)]
fig,ax=plt.subplots(figsize=(6.6,4.0)); ax.plot((f-14.2e6)/1e3,sa_trace(f,tones,300,-160,seed=5),color=B,lw=1.4)
ax.set_ylim(-100,10); ann(ax,-5,0,"f1",-30,-5); ann(ax,5,0,"f2",18,-5); ann(ax,15,-60,"2f2 − f1",10,25); ann(ax,-15,-60,"2f1 − f2",-70,25)
ax.annotate("",xy=(9,-60),xytext=(9,0),arrowprops=dict(arrowstyle="<->",color=A)); ax.text(10,-33,"Δ = 60 dB",color=A,fontsize=11)
ax.set_xlabel("f − 14,200 MHz (kHz)"); ax.set_ylabel("livello (dBm)"); ax.grid(alpha=.25)
fig.tight_layout(); fig.savefig("imd.svg",transparent=True)
out["oip3"]=P+d/2
# AM m=0.3 fm=1 kHz
f=np.linspace(7.095e6,7.105e6,4001); m=0.3; sb=20*np.log10(m/2)
fig,ax=plt.subplots(figsize=(6.6,4.0)); ax.plot((f-7.1e6)/1e3,sa_trace(f,[(7.1e6,-10),(7.099e6,-10+sb),(7.101e6,-10+sb)],100,-160,seed=7),color=B,lw=1.4)
ax.set_ylim(-110,0); ax.annotate("",xy=(1.6,-10+sb),xytext=(1.6,-10),arrowprops=dict(arrowstyle="<->",color=A)); ax.text(1.8,-20,f"Δ = {-sb:.1f} dB\n→ m = 30 %",color=A,fontsize=11)
ax.set_xlabel("f − 7,100 MHz (kHz)"); ax.set_ylabel("livello (dBm)"); ax.grid(alpha=.25)
fig.tight_layout(); fig.savefig("am.svg",transparent=True); out["am_sb"]=sb
# Bessel
b=np.linspace(0,6,600)
fig,ax=plt.subplots(figsize=(6.6,4.0))
ax.plot(b,jv(0,b),color=A,lw=2.2,label="J0: portante"); ax.plot(b,jv(1,b),color=B,lw=2,label="J1: 1ª coppia di bande laterali"); ax.plot(b,jv(2,b),color=G,lw=2,label="J2: 2ª coppia")
ax.axhline(0,color="#bbb",lw=.8); ax.axvline(2.405,color=A,ls="--",lw=1); ax.text(2.48,0.75,"β = 2,405\nprimo nullo\ndella portante",color=A,fontsize=11)
ax.set_xlabel("indice di modulazione β = Δf / fm"); ax.set_ylabel("ampiezza relativa"); ax.legend(frameon=False,loc="lower left",fontsize=10); ax.grid(alpha=.25)
fig.tight_layout(); fig.savefig("bessel.svg",transparent=True)
# zero span TETRA-like burst: slot 14.167 ms, frame 56.67 ms, one active slot
t=np.linspace(0,120e-3,6000); slot=170/12*1e-3/ (1) ; slot=14.1667e-3; frame=4*slot
env=np.where(((t%frame)>1e-3)&((t%frame)<slot-0.2e-3),1.0,0.0)
rng=np.random.default_rng(2); p=10**(-0/10)*env+10**(-75/10)*rng.exponential(1,t.shape)
from scipy.ndimage import uniform_filter1d
p=uniform_filter1d(p,8)
fig,ax=plt.subplots(figsize=(9.5,3.2)); ax.plot(t*1e3,10*np.log10(p),color=B,lw=1.3)
ax.set_ylim(-90,10); ax.set_xlabel("tempo (ms) — zero span, frequenza fissa"); ax.set_ylabel("livello (dBm)"); ax.grid(alpha=.25)
ax.annotate("",xy=(frame*1e3,3),xytext=(0,3),arrowprops=dict(arrowstyle="<->",color=A)); ax.text(frame*1e3/2,5,f"trama {frame*1e3:.2f} ms",ha="center",color=A,fontsize=11)
ax.text(slot*1e3+2,-30,"un timeslot attivo su 4\n(burst TDMA)",color=A,fontsize=11)
fig.tight_layout(); fig.savefig("zerospan.svg",transparent=True)
print(out); json.dump(out,open("vals.json","w"))
