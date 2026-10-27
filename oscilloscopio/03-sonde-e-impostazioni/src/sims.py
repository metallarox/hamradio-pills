import numpy as np
from deck import mpl_setup
plt=mpl_setup(); A="#0a1a2e"; B="#1593d1"; G="#9aa5b4"; O="#e0563b"
# compensation: 1 kHz square
t=np.linspace(0,2.5e-3,5000); T=1e-3; tau=0.12e-3
def comp(k):
    y=np.zeros_like(t); 
    for i,ti in enumerate(t):
        ph=(ti%T); lev=1 if ph<T/2 else 0; tt=ph%(T/2)
        y[i]=(lev-0.5)*2*(1+(k-1)*np.exp(-tt/tau))/2+0.5
    return y
fig,axs=plt.subplots(1,3,figsize=(11,3.0),sharey=True)
for ax,k,tt,c in zip(axs,(0.7,1.0,1.3),("sottocompensata","corretta","sovracompensata"),(G,B,O)):
    ax.plot(t*1e3,comp(k),color=c,lw=2.2); ax.set_title(tt,color=A,fontsize=13); ax.set_xlabel("ms"); ax.grid(alpha=.25); ax.set_yticks([])
fig.tight_layout(); fig.savefig("comp.svg",transparent=True)
# ground lead ringing: step through series L, shunt C, with R damping
from scipy import signal
def resp(L,C=10e-12,R=25):
    # source R into L then C (second order)
    num=[1]; den=[L*C,R*C,1]; sys=signal.lti(num,den); tt=np.linspace(0,30e-9,3000); _,y=signal.step(sys,T=tt); return tt,y
# apply scope bandwidth 200 MHz (1st order) 
def bwlim(tt,y,bw=200e6):
    a=np.exp(-2*np.pi*bw*(tt[1]-tt[0])); z=np.zeros_like(y); 
    for i in range(1,len(y)): z[i]=a*z[i-1]+(1-a)*y[i]
    return z
fig,ax=plt.subplots(figsize=(6.4,3.8))
tt,y=resp(150e-9); ax.plot(tt*1e9,bwlim(tt,y),color=O,lw=2,label="cavetto di massa 15 cm (~150 nH)")
tt,y=resp(10e-9); ax.plot(tt*1e9,bwlim(tt,y),color=B,lw=2.2,label="molla di massa corta (~10 nH)")
ax.set_xlabel("tempo (ns)"); ax.set_ylabel("ampiezza"); ax.legend(frameon=False,loc="lower right",fontsize=10); ax.grid(alpha=.25)
fig.tight_layout(); fig.savefig("ground.svg",transparent=True)
