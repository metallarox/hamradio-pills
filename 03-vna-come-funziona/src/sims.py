import numpy as np, json, matplotlib
matplotlib.use("svg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.family":"DejaVu Sans","font.size":12,"axes.spines.top":False,"axes.spines.right":False})
A="#0a1a2e"; B="#1593d1"; G="#9aa5b4"; out={}
f=np.linspace(100e6,200e6,801); w=2*np.pi*f; Z0=50
# DUT: series RLC "antenna" resonant at 145 MHz, R=40
f0=145e6; R=40; L=300e-9; C=1/((2*np.pi*f0)**2*L)
Zd=R+1j*w*L+1/(1j*w*C); Ga=(Zd-Z0)/(Zd+Z0)
# error terms (cable 1 m VF .66 plus imperfect bridge)
tau=1/(0.66*3e8)
Ed=0.06*np.exp(-1j*w*0.4e-9)+0.02
Es=0.12*np.exp(-1j*w*0.9e-9)
Er=0.85*np.exp(-1j*2*w*tau)
meas=lambda G: Ed+Er*G/(1-Es*G)
Gm=meas(Ga)
# SOL with ideal standards
mL=meas(0*Ga); mS=meas(-1+0*Ga); mO=meas(1+0*Ga)
ed=mL; s=mS-ed; o=mO-ed; es=(o+s)/(o-s); er=o*(1-es)
Gc=(Gm-ed)/(er+es*(Gm-ed))
out["maxerr"]=float(abs(Gc-Ga).max())
fig,ax=plt.subplots(figsize=(6.4,4.0))
ax.plot(f/1e6,20*np.log10(abs(Gm)),color=G,lw=2,label="non calibrato")
ax.plot(f/1e6,20*np.log10(abs(Gc)),color=B,lw=2.2,label="dopo SOL")
ax.set_xlabel("f (MHz)"); ax.set_ylabel("|S11| (dB)"); ax.legend(frameon=False,loc="lower left"); ax.grid(alpha=.25)
fig.tight_layout(); fig.savefig("cal_mag.svg",transparent=True)
fig,ax=plt.subplots(figsize=(4.3,4.3)); ax.set_aspect("equal"); ax.axis("off")
t=np.linspace(0,2*np.pi,400); ax.plot(np.cos(t),np.sin(t),color="#9aa5b4",lw=1.2)
for r in [0.2,0.5,1,2,5]:
    c=r/(1+r); rad=1/(1+r); ax.plot(c+rad*np.cos(t),rad*np.sin(t),color="#d5dbe3",lw=.8)
for x in [0.2,0.5,1,2,5]:
    for sg in(1,-1):
        zz=1j*sg*x+np.linspace(0,50,3000); g=(zz-1)/(zz+1); ax.plot(g.real,g.imag,color="#d5dbe3",lw=.8)
ax.plot([-1,1],[0,0],color="#9aa5b4",lw=1)
ax.plot(Gm.real,Gm.imag,color=G,lw=1.8,label="non calibrato"); ax.plot(Gc.real,Gc.imag,color=B,lw=2.2,label="dopo SOL")
ax.legend(frameon=False,loc="lower center",bbox_to_anchor=(0.5,-0.12),ncol=2,fontsize=11)
fig.tight_layout(); fig.savefig("cal_smith.svg",transparent=True)
# directivity uncertainty
rl=np.linspace(0,40,400); g=10**(-rl/20)
fig,ax=plt.subplots(figsize=(6.4,4.0))
ax.plot(rl,rl,color=A,lw=1.5,label="ideale")
for D,col in((20,"#9cc9e6"),(30,B),(40,A)):
    e=10**(-D/20); lo=-20*np.log10(g+e); hi=-20*np.log10(np.maximum(g-e,1e-6))
    ax.fill_between(rl,lo,np.minimum(hi,60),color=col,alpha=.35,label=f"direttività {D} dB")
ax.set_ylim(0,50); ax.set_xlabel("return loss vero (dB)"); ax.set_ylabel("return loss misurato (dB)")
ax.legend(frameon=False,loc="upper left"); ax.grid(alpha=.25)
fig.tight_layout(); fig.savefig("directivity.svg",transparent=True)
# example numbers: true RL 20 dB, D 30 dB
g=0.1; e=10**(-30/20); out["rl20_d30"]=[-20*np.log10(g+e),-20*np.log10(g-e)]
print(out); json.dump(out,open("vals.json","w"))
