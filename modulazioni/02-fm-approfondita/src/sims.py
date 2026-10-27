import numpy as np
from scipy.special import jv
from deck import mpl_setup
plt=mpl_setup(); A="#0a1a2e"; B="#1593d1"; O="#e0563b"; G="#9aa5b4"
# Bessel spectra beta 0.5, 1.67, 5
fig,axs=plt.subplots(1,3,figsize=(11,3.0),sharey=True)
for ax,(b,tt) in zip(axs,((0.5,"β = 0,5 (banda stretta)"),(1.67,"β = 1,67 (5 kHz / 3 kHz)"),(5,"β = 5 (broadcast, 75/15 kHz)"))):
    n=np.arange(-10,11); p=jv(n,b)**2
    ax.bar(n,10*np.log10(p+1e-9)+40,bottom=-40,color=B,width=0.6); ax.set_ylim(-40,2); ax.set_title(tt,color=A,fontsize=11); ax.set_xlabel("riga n (fc + n·fm)"); ax.grid(alpha=.2,axis="y")
axs[0].set_ylabel("dB rispetto alla portante")
fig.tight_layout(); fig.savefig("bessel.svg",transparent=True)
# FM noise triangle & deemphasis
f=np.linspace(50,15000,500); tau=50e-6
noise=20*np.log10(f/1000); de=-10*np.log10(1+(2*np.pi*f*tau)**2)
fig,ax=plt.subplots(figsize=(6.2,3.7))
ax.semilogx(f,noise,color=O,lw=2.2,label="rumore FM in uscita (+6 dB/ottava)")
ax.semilogx(f,noise+de,color=B,lw=2.2,label="dopo la deenfasi (50 µs)")
ax.semilogx(f,de,color=G,lw=1.5,ls="--",label="curva di deenfasi")
ax.axvline(1/(2*np.pi*tau),color=G,ls=":"); ax.text(3400,-25,"3,18 kHz",color="#555",fontsize=10)
ax.set_xlabel("frequenza audio (Hz)"); ax.set_ylabel("dB (relativo)"); ax.legend(frameon=False,fontsize=9,loc="upper left"); ax.grid(alpha=.25,which="both"); ax.set_ylim(-30,25)
fig.tight_layout(); fig.savefig("emph.svg",transparent=True)
# threshold
cnr=np.linspace(0,30,300)
def fm_out(c,beta):
    gain=10*np.log10(3*beta**2*(beta+1))
    above=c+gain
    thr=10
    return np.where(c>thr,above, above-np.clip(thr-c,0,None)**1.6)
fig,ax=plt.subplots(figsize=(6.2,3.7))
ax.plot(cnr,cnr,color=G,lw=2,ls="--",label="AM / SSB (lineare)")
ax.plot(cnr,fm_out(cnr,5),color=A,lw=2.2,label="FM β = 5")
ax.plot(cnr,fm_out(cnr,1.67),color=B,lw=2.2,label="FM β = 1,67")
ax.axvline(10,color=O,ls=":"); ax.text(10.5,2,"soglia ≈ 10 dB",color=O,fontsize=10)
ax.set_xlabel("C/N in ingresso (dB)"); ax.set_ylabel("S/N audio (dB)"); ax.set_ylim(0,60); ax.legend(frameon=False,fontsize=9,loc="upper left"); ax.grid(alpha=.25)
fig.tight_layout(); fig.savefig("threshold.svg",transparent=True)
print(10*np.log10(3*5**2*6),10*np.log10(3*1.67**2*2.67))
