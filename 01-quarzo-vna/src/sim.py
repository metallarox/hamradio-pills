import numpy as np, matplotlib
matplotlib.use("svg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.family":"DejaVu Sans","font.size":11,"axes.spines.top":False,"axes.spines.right":False})
Z0=50; Rm=10; Lm=10e-3; fs0=10e6
Cm=1/((2*np.pi*fs0)**2*Lm); C0=5e-12
def Z(f):
    w=2*np.pi*f
    Zm=Rm+1j*w*Lm+1/(1j*w*Cm); Zc=1/(1j*w*C0)
    return Zm*Zc/(Zm+Zc)
def S21(f): return 2*Z0/(2*Z0+Z(f))
# wide
f=np.linspace(9.995e6,10.040e6,40001); s=S21(f)
mag=20*np.log10(abs(s)); ph=np.degrees(np.angle(s))
fs=f[np.argmax(abs(s))]; fp=f[np.argmin(abs(s))]
# fine around fs
ff=np.linspace(fs-3000,fs+3000,600001); ss=S21(ff); pp=np.degrees(np.angle(ss))
fs=ff[np.argmax(abs(ss))]; s_pk=abs(ss).max()
i=np.argmax(abs(ss))
fm=ff[:i][np.argmin(abs(pp[:i]-45))]; fpl=ff[i:][np.argmin(abs(pp[i:]+45))]
Rx=2*Z0*(1/s_pk-1); df=fpl-fm; Lx=(Rx+2*Z0)/(2*np.pi*df); Cx=1/((2*np.pi*fs)**2*Lx)
C0x=Cx*fs/(2*(fp-fs)); Q=2*np.pi*fs*Lx/Rx
print(f"fs={fs:.1f} fp={fp:.1f} |S21|pk={s_pk:.4f} ({20*np.log10(s_pk):.2f} dB) f-45={fm:.1f} f+45={fpl:.1f} df={df:.1f}")
print(f"Rm={Rx:.2f} Lm={Lx*1e3:.3f}mH Cm={Cx*1e15:.2f}fF C0={C0x*1e12:.2f}pF Q={Q:.0f} true Cm={Cm*1e15:.2f}")
import json; open("vals.txt","w").write(json.dumps({k:float(x) for k,x in dict(fs=fs,fp=fp,spk=s_pk,spkdb=20*np.log10(s_pk),fm=fm,fpl=fpl,df=df,Rm=Rx,Lm=Lx,Cm=Cx,C0=C0x,Q=Q).items()}))
A="#0a1a2e"; B="#1593d1"
fig,ax=plt.subplots(2,1,figsize=(9,4.6),sharex=True)
x=(f-10e6)/1e3
ax[0].plot(x,mag,color=A,lw=1.8); ax[0].set_ylabel("|S21| (dB)")
ax[0].axvline((fs-10e6)/1e3,color="#888",ls="--",lw=1); ax[0].axvline((fp-10e6)/1e3,color="#888",ls="--",lw=1)
ax[0].annotate("fs  (picco)",((fs-10e6)/1e3,mag.max()),xytext=(6,-14),textcoords="offset points",color=A)
ax[0].annotate("fp  (notch)",((fp-10e6)/1e3,mag.min()),xytext=(6,4),textcoords="offset points",color=A)
ax[1].plot(x,ph,color=B,lw=1.8); ax[1].set_ylabel("fase S21 (°)"); ax[1].set_xlabel("f − 10 MHz (kHz)")
ax[1].axhline(0,color="#bbb",lw=.8)
for a in ax: a.grid(alpha=.25)
fig.tight_layout(); fig.savefig("wide.svg",transparent=True)
fig,ax=plt.subplots(figsize=(6.2,4.2))
xx=(ff-fs); m=abs(xx)<2500
ax.plot(xx[m],pp[m],color=B,lw=2)
for v,l in((45,"+45°"),(-45,"−45°")): ax.axhline(v,color="#aaa",ls=":",lw=1)
ax.axvline(fm-fs,color=A,ls="--",lw=1); ax.axvline(fpl-fs,color=A,ls="--",lw=1)
ax.annotate("",xy=(fpl-fs,-75),xytext=(fm-fs,-75),arrowprops=dict(arrowstyle="<->",color=A))
ax.text(0,-70,f"Δf = {df:.0f} Hz",ha="center",color=A)
ax.text(fm-fs-80,50,"f₁ (+45°)",ha="right",color=A); ax.text(fpl-fs+80,50,"f₂ (−45°)",color=A)
ax.set_xlabel("f − fs (Hz)"); ax.set_ylabel("fase S21 (°)"); ax.set_ylim(-90,90); ax.grid(alpha=.25)
fig.tight_layout(); fig.savefig("zoom.svg",transparent=True)
