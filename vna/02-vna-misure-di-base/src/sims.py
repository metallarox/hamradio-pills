import numpy as np, json, matplotlib
from scipy import signal
matplotlib.use("svg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.family":"DejaVu Sans","font.size":12,"axes.spines.top":False,"axes.spines.right":False})
A="#0a1a2e"; B="#1593d1"; G="#9aa5b4"; out={}
# 1 bandpass filter 145 MHz, 3rd order Chebyshev 0.5 dB, BW 8 MHz, IL 1.2 dB
f0=145e6; bw=8e6
b,a=signal.cheby1(3,0.5,[2*np.pi*(f0-bw/2),2*np.pi*(f0+bw/2)],btype="bandpass",analog=True)
f=np.linspace(110e6,180e6,4001); _,h=signal.freqs(b,a,2*np.pi*f)
s21=20*np.log10(abs(h))-1.2
pk=s21.max(); ins=f[s21>=pk-3]; out.update(il=-pk,bw3=[ins.min(),ins.max()],rej=float(np.interp(130e6,f,s21)))
fig,ax=plt.subplots(figsize=(6.6,4.1))
ax.plot(f/1e6,s21,color=B,lw=2.2); ax.set_ylim(-70,3)
ax.axhline(pk-3,color=G,ls=":",lw=1)
ax.annotate(f"insertion loss\n{-pk:.1f} dB",(f0/1e6,pk),xytext=(160,-16),color=A,fontsize=11,arrowprops=dict(arrowstyle="->",color=A))
ax.annotate("",xy=(ins.max()/1e6,pk-3),xytext=(ins.min()/1e6,pk-3),arrowprops=dict(arrowstyle="<->",color=A))
ax.text(ins.min()/1e6-1,pk-3,f"−3 dB: {(ins.max()-ins.min())/1e6:.1f} MHz ↔",ha="right",va="center",color=A,fontsize=11)
r=out["rej"]; ax.plot(130,r,"o",color=A); ax.annotate(f"reiezione a 130 MHz\n{-r:.0f} dB",(130,r),xytext=(112,-30),color=A,fontsize=11,arrowprops=dict(arrowstyle="->",color=A))
ax.set_xlabel("f (MHz)"); ax.set_ylabel("|S21| (dB)"); ax.grid(alpha=.25)
fig.tight_layout(); fig.savefig("filter.svg",transparent=True)
# 2 open-ended cable 10 m VF .66, |Zin|
c=299792458; VF=0.66; Lc=10; Z0=50
f=np.linspace(0.5e6,30e6,6000); beta=2*np.pi*f/(c*VF); alpha=0.0015*np.sqrt(f/1e6)  # Np/m
g=alpha+1j*beta; Zin=Z0/np.tanh(g*Lc)
fq=c*VF/(4*Lc); out["fq"]=fq
fig,ax=plt.subplots(figsize=(6.6,4.1))
ax.semilogy(f/1e6,abs(Zin),color=B,lw=2)
ax.axvline(fq/1e6,color=A,ls="--",lw=1); ax.text(fq/1e6+0.6,150,f"λ/4: {fq/1e6:.2f} MHz\n(aperto → corto)",color=A,fontsize=11)
ax.set_xlabel("f (MHz)"); ax.set_ylabel("|Z| all'ingresso (Ω)"); ax.grid(alpha=.25,which="both")
fig.tight_layout(); fig.savefig("cable.svg",transparent=True)
print(out); json.dump(out,open("vals.json","w"))
