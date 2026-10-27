import numpy as np, json, matplotlib
matplotlib.use("svg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.family":"DejaVu Sans","font.size":11,"axes.spines.top":False,"axes.spines.right":False})
Z0=50; Rm=10; Lm=10e-3; fs0=10e6; Cm=1/((2*np.pi*fs0)**2*Lm); C0=5e-12
def Z(f):
    w=2*np.pi*f; Zm=Rm+1j*w*Lm+1/(1j*w*Cm); Zc=1/(1j*w*C0); return Zm*Zc/(Zm+Zc)
A="#0a1a2e"; B="#1593d1"
ff=np.linspace(fs0-1500,fs0+1500,600001); z=Z(ff); ph=np.degrees(np.angle(z))
i=np.argmin(abs(z.imag[:len(ff)//2+20000])) ; i=np.argmin(np.where(abs(ff-fs0)<500,abs(z.imag),1e9))
fs=ff[i]; Rx=z.real[i]
f1=ff[:i][np.argmin(abs(ph[:i]+45))]; f2=ff[i:][np.argmin(abs(ph[i:]-45))]
df=f2-f1; Lx=Rx/(2*np.pi*df); Cx=1/((2*np.pi*fs)**2*Lx); Q=fs/df
fw=np.linspace(fs0+20e3,fs0+30e3,200001); zw=Z(fw); fp=fw[np.argmax(abs(zw))]
C0x=Cx*fs/(2*(fp-fs)); G=(z-Z0)/(z+Z0)
d=dict(fs=fs,Rm=Rx,f1=f1,f2=f2,df=df,Lm=Lx,Cm=Cx,Q=Q,fp=fp,C0=C0x,G=float(abs(G[i])),Zfp=float(abs(Z(fp))))
print(d); json.dump({k:float(v) for k,v in d.items()},open("vals11.json","w"))
# Smith
fig,ax=plt.subplots(figsize=(4.4,4.4)); ax.set_aspect("equal"); ax.axis("off")
t=np.linspace(0,2*np.pi,400); ax.plot(np.cos(t),np.sin(t),color="#9aa5b4",lw=1.2)
for r in [0.2,0.5,1,2,5]:
    c=r/(1+r); rad=1/(1+r); ax.plot(c+rad*np.cos(t),rad*np.sin(t),color="#d5dbe3",lw=.8)
for x in [0.2,0.5,1,2,5]:
    for s in(1,-1):
        zz=1j*s*x+np.linspace(0,50,3000); g=(zz-1)/(zz+1); ax.plot(g.real,g.imag,color="#d5dbe3",lw=.8)
ax.plot([-1,1],[0,0],color="#9aa5b4",lw=1)
fa=np.linspace(fs0-3000,fs0+40e3,400001); Ga=(Z(fa)-Z0)/(Z(fa)+Z0)
ax.plot(Ga.real,Ga.imag,color=B,lw=2)
g=G[i]; ax.plot(g.real,g.imag,"o",color=A); ax.annotate("fs: X = 0\nZ ≈ Rm",(g.real,g.imag),xytext=(-70,22),textcoords="offset points",color=A,fontsize=14,arrowprops=dict(arrowstyle="-",color=A))
gp=(Z(fp)-Z0)/(Z(fp)+Z0); ax.plot(gp.real,gp.imag,"o",color=A); ax.annotate("fp: |Z| → ∞\n(Γ ≈ 1)",(gp.real,gp.imag),xytext=(-75,-40),textcoords="offset points",color=A,fontsize=14,arrowprops=dict(arrowstyle="-",color=A))
fig.tight_layout(); fig.savefig("smith.svg",transparent=True)
# phase of Z zoom
fig,ax=plt.subplots(figsize=(6.2,4.0)); x=ff-fs; m=abs(x)<600
ax.plot(x[m],ph[m],color=B,lw=2); ax.set_ylim(-90,90)
for v in(45,-45): ax.axhline(v,color="#aaa",ls=":",lw=1)
ax.axvline(f1-fs,color=A,ls="--",lw=1); ax.axvline(f2-fs,color=A,ls="--",lw=1)
ax.annotate("",xy=(f2-fs,70),xytext=(f1-fs,70),arrowprops=dict(arrowstyle="<->",color=A))
ax.text(0,76,f"Δf = {df:.0f} Hz",ha="center",color=A)
ax.text(f1-fs-20,-60,"f₁ (−45°)",ha="right",color=A); ax.text(f2-fs+20,-60,"f₂ (+45°)",color=A)
ax.set_xlabel("f − fs (Hz)"); ax.set_ylabel("fase di Z (°)"); ax.grid(alpha=.25)
fig.tight_layout(); fig.savefig("zph.svg",transparent=True)
