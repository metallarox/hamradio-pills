import numpy as np, json
from deck import sa_trace, mpl_setup
plt=mpl_setup(); A="#0a1a2e"; B="#1593d1"; G="#9aa5b4"; out={}
# 1 coupling vs frequency
f=np.logspace(np.log10(1.8e6),np.log10(200e6),400)
cap=-50+20*np.log10(f/3.5e6)  # capacitive pick-off: +6 dB/octave
res=-40-10*np.log10(1+(f/300e6)**2)
fig,ax=plt.subplots(figsize=(6.6,4.0))
ax.semilogx(f/1e6,res,color=A,lw=2.2,label="prelievo resistivo (piatto)")
ax.semilogx(f/1e6,cap,color=B,lw=2.2,label="prelievo capacitivo (+6 dB/ottava)")
for fx in (14,28,42):
    y=-50+20*np.log10(fx/3.5); ax.plot(fx,y,"o",color=B)
ax.annotate("14 MHz: −38 dB\n28 MHz: −32 dB\n42 MHz: −28,5 dB",(28,-32),xytext=(2.0,-17),color=B,fontsize=11,arrowprops=dict(arrowstyle="->",color=B))
ax.set_xlabel("f (MHz)"); ax.set_ylabel("accoppiamento della presa (dB)"); ax.set_ylim(-60,-10); ax.grid(alpha=.25,which="both"); ax.legend(frameon=False,loc="lower right",fontsize=10)
fig.tight_layout(); fig.savefig("coupling.svg",transparent=True)
out["cap14"]=-50+20*np.log10(14/3.5); out["cap28"]=-50+20*np.log10(28/3.5); out["cap42"]=-50+20*np.log10(42/3.5)
# 2 cable ripple with bridge + TG
c=299792458; VF=0.66; l=20; Z0=50
f=np.linspace(1e6,100e6,4000); beta=2*np.pi*f/(c*VF); alpha=0.01*np.sqrt(f/1e8)*l/20/8.686*20  # small loss
gl=(100-50)/(100+50); g0=0.05
gam=g0+gl*np.exp(-2*(alpha/l*l)-2j*beta*l)
rl=-20*np.log10(abs(gam))
fig,ax=plt.subplots(figsize=(10,3.1)); ax.plot(f/1e6,rl,color=B,lw=1.8); ax.set_ylim(13.5,7)
p=c*VF/(2*l); out["ripple"]=p
ax.annotate("",xy=(30+p/1e6,7.6),xytext=(30,7.6),arrowprops=dict(arrowstyle="<->",color=A)); ax.text(30+p/2e6,7.4,f"Δf = {p/1e6:.2f} MHz",ha="center",color=A,fontsize=11)
ax.set_xlabel("f (MHz)"); ax.set_ylabel("return loss (dB)"); ax.grid(alpha=.25)
fig.tight_layout(); fig.savefig("ripple.svg",transparent=True)
# 3 two-tone SSB test
fc=14.2e6; t1=fc+700; t2=fc+1900; tone=-6
im3=tone-30; im5=tone-42
tones=[(t1,tone),(t2,tone),(2*t1-t2,im3),(2*t2-t1,im3),(3*t1-2*t2,im5),(3*t2-2*t1,im5)]
f=np.linspace(fc-3000,fc+6000,6000)
fig,ax=plt.subplots(figsize=(6.6,4.0)); ax.plot((f-fc),sa_trace(f,tones,30,-150,seed=4),color=B,lw=1.4)
ax.axhline(0,color=G,ls=":",lw=1); ax.text(-2900,1.5,"PEP (0 dB)",color="#555",fontsize=10)
ax.annotate("IM3",(2*t2-t1-fc,im3),xytext=(10,15),textcoords="offset points",color=A,fontsize=11)
ax.annotate("IM3",(2*t1-t2-fc,im3),xytext=(-35,15),textcoords="offset points",color=A,fontsize=11)
ax.annotate("IM5",(3*t2-2*t1-fc,im5),xytext=(5,15),textcoords="offset points",color=A,fontsize=11)
ax.set_ylim(-80,6); ax.set_xlabel("f − portante soppressa (Hz)"); ax.set_ylabel("livello rispetto alla PEP (dB)"); ax.grid(alpha=.25)
fig.tight_layout(); fig.savefig("twotone.svg",transparent=True)
print(out); json.dump(out,open("vals.json","w"))
