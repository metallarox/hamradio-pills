import numpy as np
from deck import mpl_setup
plt=mpl_setup(); A="#0a1a2e"; B="#1593d1"; O="#e0563b"; G="#9aa5b4"; V="#2a9d5c"
t=np.linspace(0,0.2,500); Vcc=5
fig,ax=plt.subplots(figsize=(5.6,3.5))
for tau,c,n in [(0.047,B,"100 nF con 470 kΩ: τ = 47 ms"),(0.0068,O,"10 µF con 680 Ω: τ = 6,8 ms")]:
    ax.plot(t*1000,Vcc*(1-np.exp(-t/tau)),color=c,lw=2.2,label=n)
    ax.plot(tau*1000,Vcc*(1-np.exp(-1)),"o",color=c)
ax.axhline(Vcc*(1-np.exp(-1)),color=G,ls="--",lw=1); ax.text(120,3.3,"63 % di Vcc dopo τ",fontsize=9,color="#555")
ax.set_xlabel("tempo (ms)"); ax.set_ylabel("tensione sul condensatore (V)"); ax.set_ylim(0,5.4); ax.grid(alpha=.25); ax.legend(frameon=False,fontsize=9,loc="lower right")
fig.tight_layout(); fig.savefig("charge.svg",transparent=True)
t=np.linspace(0,6e-6,500); R=680
fig,ax=plt.subplots(figsize=(5.6,3.5))
for L,c,n in [(1e-3,B,"1 mH: τ = L/R ≈ 1,5 µs"),(100e-6,O,"100 µH: τ ≈ 0,15 µs"),(10e-6,V,"10 µH: τ ≈ 15 ns")]:
    ax.plot(t*1e6,1-np.exp(-t/(L/R)),color=c,lw=2.2,label=n)
ax.axvline(0.125,color=G,ls=":",lw=1.2); ax.text(0.2,0.08,"un ciclo di clock a 8 MHz",fontsize=9,color="#555")
ax.set_xlabel("tempo (µs)"); ax.set_ylabel("corrente (rispetto al valore finale)"); ax.grid(alpha=.25); ax.legend(frameon=False,fontsize=9,loc="lower right"); ax.set_ylim(0,1.05)
fig.tight_layout(); fig.savefig("lrise.svg",transparent=True)
f=np.logspace(1.5,6,300); C=470e-6
esr=0.04+0.02/(2*np.pi*f*C)
fig,ax=plt.subplots(figsize=(5.8,3.6))
ax.plot(f,esr*1000,color=A,lw=2.4,label="ESR del condensatore (modello)")
fh=np.array([100,120,1e3,1e4,1e5]); ax.plot(fh,(0.04+0.02/(2*np.pi*fh*C))*1000,"o",color=B,ms=8,label="punti di misura dell'LCR meter HP")
ax.text(40,8,"il tester a impulsi dà una sola lettura,\nsenza una frequenza di prova dichiarata",fontsize=9,color=O)
ax.set_xscale("log"); ax.set_ylim(0,110); ax.set_xlabel("frequenza (Hz)"); ax.set_ylabel("ESR (mΩ)"); ax.grid(alpha=.25,which="both"); ax.legend(frameon=False,fontsize=9,loc="upper right",bbox_to_anchor=(1,0.75))
fig.tight_layout(); fig.savefig("esrf.svg",transparent=True)
for x in [100,120,1e3,1e4,1e5]: print(x,round((0.04+0.02/(2*np.pi*x*C))*1000,1))
