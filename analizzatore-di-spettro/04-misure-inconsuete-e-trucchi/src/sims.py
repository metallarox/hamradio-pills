import numpy as np, json
from deck import sa_trace, mpl_setup
plt=mpl_setup(); A="#0a1a2e"; B="#1593d1"; G="#9aa5b4"; out={}
# attenuation test: fundamental 50 MHz -5 dBm; external harmonic 2nd -60 dBm (real); internal 3rd at 150 MHz -70 dBm with att 10 -> -80 with att 20
f=np.linspace(10e6,180e6,5000)
t10=sa_trace(f,[(50e6,-5),(100e6,-70),(150e6,-60)],300e3,-150,seed=1)
t20=sa_trace(f,[(50e6,-5),(100e6,-80),(150e6,-60)],300e3,-140,seed=2)
fig,ax=plt.subplots(figsize=(10,3.3))
ax.plot(f/1e6,t10,color=G,lw=1.3,label="attenuazione 10 dB"); ax.plot(f/1e6,t20,color=B,lw=1.3,label="attenuazione 20 dB")
ax.set_ylim(-100,5); ax.set_xlabel("f (MHz)"); ax.set_ylabel("livello (dBm)"); ax.grid(alpha=.25); ax.legend(frameon=False,loc="upper left")
ax.annotate("150 MHz: non cambia\n→ segnale VERO",(150,-60),xytext=(140,-30),color=A,fontsize=11,arrowprops=dict(arrowstyle="->",color=A))
ax.annotate("100 MHz (2ª armonica): cala di 10 dB\n→ generata DENTRO l'analizzatore",(100,-75),xytext=(62,-28),color=A,fontsize=11,arrowprops=dict(arrowstyle="->",color=A))
ax.annotate("il rumore sale di 10 dB",(30,-80),xytext=(14,-62),color="#555",fontsize=10)
fig.tight_layout(); fig.savefig("atttest.svg",transparent=True)
# noise correction curve
d=np.linspace(0.5,20,300); corr=-10*np.log10(1-10**(-d/10))
fig,ax=plt.subplots(figsize=(6.2,3.9)); ax.plot(d,corr,color=B,lw=2.2)
for x in (3,6,10):
    y=-10*np.log10(1-10**(-x/10)); ax.plot(x,y,"o",color=A); ax.annotate(f"{x} dB → −{y:.2f} dB".replace(".",","),(x,y),xytext=(8,8),textcoords="offset points",color=A,fontsize=11)
ax.set_yscale("log"); ax.set_xlabel("Δ = (segnale + rumore) − rumore (dB)"); ax.set_ylabel("correzione da sottrarre (dB)"); ax.grid(alpha=.25,which="both")
fig.tight_layout(); fig.savefig("noisecorr.svg",transparent=True)
print("ok")
