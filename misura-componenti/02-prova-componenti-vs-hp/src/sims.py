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
# errore di risoluzione del partitore con ADC a 10 bit
R=np.logspace(-1,8,500); Vcc=5; lsb=Vcc/1024
fig,ax=plt.subplots(figsize=(5.8,3.6))
for Rr,c,n in [(680,O,"partitore con 680 Ω"),(470e3,B,"partitore con 470 kΩ")]:
    Vx=Vcc*R/(R+Rr); err=lsb*Vcc/(Vx*(Vcc-Vx))*100
    ax.plot(R,err,color=c,lw=2.2,label=n)
ax.plot(R,np.minimum(lsb*Vcc/((Vcc*R/(R+680))*(Vcc-Vcc*R/(R+680))),lsb*Vcc/((Vcc*R/(R+470e3))*(Vcc-Vcc*R/(R+470e3))))*100,color=A,lw=1.2,ls="--",label="scegliendo il migliore")
ax.set_xscale("log"); ax.set_yscale("log"); ax.set_ylim(0.1,100); ax.set_xlim(0.1,1e8)
ax.set_xlabel("resistenza misurata (Ω)"); ax.set_ylabel("errore da 1 LSB (%)"); ax.grid(alpha=.25,which="both"); ax.legend(frameon=False,fontsize=9,loc="upper center")
fig.tight_layout(); fig.savefig("rerr.svg",transparent=True)
# ESR: gradino all'inizio dell'impulso
t=np.linspace(-2,20,600); I=0.005; C=100e-6; esr=2.0
v=np.where(t<0,0,I*esr+I*np.clip(t,0,None)*1e-6/C)
v=np.where(t>12,I*np.clip(12,0,None)*1e-6/C,v)
fig,ax=plt.subplots(figsize=(5.6,3.4))
ax.plot(t,v*1000,color=A,lw=2.4)
ax.annotate("",xy=(0.3,10),xytext=(0.3,0),arrowprops=dict(arrowstyle="<->",color=O)); ax.text(0.8,4.2,"salto = I·ESR",color=O,fontsize=10)
ax.annotate("",xy=(12.4,10+0.6),xytext=(12.4,0.6),arrowprops=dict(arrowstyle="<->",color=O)); ax.text(13,4,"stesso salto\nalla fine dell'impulso",color=O,fontsize=9)
ax.text(3,9.5+2.2,"carica: pendenza = I / C",color=B,fontsize=10)
ax.set_xlabel("tempo (µs)"); ax.set_ylabel("tensione sul condensatore (mV)"); ax.grid(alpha=.25); ax.set_ylim(-1,15)
fig.tight_layout(); fig.savefig("esrpulse.svg",transparent=True)
