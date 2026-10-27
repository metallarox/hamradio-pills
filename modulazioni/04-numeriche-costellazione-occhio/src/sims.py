import numpy as np
from deck import mpl_setup
plt=mpl_setup(); A="#0a1a2e"; B="#1593d1"; O="#e0563b"; G="#9aa5b4"
rng=np.random.default_rng(3)
bits=np.array([1,0,1,1,0,0,1,0]); sps=200; fc=3
t=np.arange(len(bits)*sps)/sps; b=np.repeat(bits,sps)
fig,axs=plt.subplots(4,1,figsize=(10,4.4),sharex=True)
axs[0].step(np.arange(len(bits)+1),np.r_[bits,bits[-1]],where="post",color=O,lw=2); axs[0].set_ylabel("bit",fontsize=10)
for i,bb in enumerate(bits): axs[0].text(i+0.5,1.15,str(bb),ha="center",fontsize=10,color=A)
axs[0].set_ylim(-0.2,1.5)
axs[1].plot(t,b*np.sin(2*np.pi*fc*t),color=B,lw=1.2); axs[1].set_ylabel("ASK",fontsize=10)
f=np.where(b==1,fc*1.6,fc*0.8); ph=2*np.pi*np.cumsum(f)/sps; axs[2].plot(t,np.sin(ph),color=B,lw=1.2); axs[2].set_ylabel("FSK",fontsize=10)
axs[3].plot(t,np.sin(2*np.pi*fc*t+np.pi*(1-b)),color=B,lw=1.2); axs[3].set_ylabel("PSK",fontsize=10)
for a in axs: a.set_yticks([]); a.grid(alpha=.2)
axs[3].set_xlabel("tempo (in simboli)")
fig.tight_layout(); fig.savefig("ask_fsk_psk.svg",transparent=True)
def qam(M):
    m=int(np.sqrt(M)); x=np.arange(-m+1,m,2); X,Y=np.meshgrid(x,x); c=(X+1j*Y).ravel(); return c/np.sqrt(np.mean(abs(c)**2))
def psk(M,off=0): k=np.arange(M); return np.exp(1j*(2*np.pi*k/M+off))
fig,axs=plt.subplots(1,5,figsize=(11.5,2.8))
for ax,(c,tt) in zip(axs,((psk(2),"BPSK · 1 bit"),(psk(4,np.pi/4),"QPSK · 2 bit"),(psk(8),"8PSK · 3 bit"),(qam(16),"16QAM · 4 bit"),(qam(64),"64QAM · 6 bit"))):
    ax.plot(c.real,c.imag,"o",color=B,ms=6 if len(c)<20 else 3.5); ax.axhline(0,color=G,lw=.6); ax.axvline(0,color=G,lw=.6)
    ax.set_xlim(-1.5,1.5); ax.set_ylim(-1.5,1.5); ax.set_aspect("equal"); ax.set_xticks([]); ax.set_yticks([]); ax.set_title(tt,color=A,fontsize=11)
fig.tight_layout(); fig.savefig("const.svg",transparent=True)
# QPSK labeled
fig,ax=plt.subplots(figsize=(4.2,4.2)); c=psk(4,np.pi/4); labs=["00","01","11","10"]
ax.plot(c.real,c.imag,"o",color=B,ms=12)
for p,l in zip(c,labs): ax.annotate(l,(p.real,p.imag),xytext=(10,8),textcoords="offset points",fontsize=12,color=A)
ax.annotate("",xy=(c[0].real,c[0].imag),xytext=(0,0),arrowprops=dict(arrowstyle="->",color=O,lw=2)); ax.text(0.25,0.1,"ampiezza\ne fase",color=O,fontsize=10)
ax.axhline(0,color=G,lw=.8); ax.axvline(0,color=G,lw=.8); ax.set_xlabel("I (in fase)"); ax.set_ylabel("Q (in quadratura)")
ax.set_xlim(-1.4,1.4); ax.set_ylim(-1.4,1.4); ax.set_aspect("equal"); ax.set_xticks([]); ax.set_yticks([])
fig.tight_layout(); fig.savefig("iq.svg",transparent=True)
# noisy constellations
fig,axs=plt.subplots(1,4,figsize=(11,2.9))
for ax,(c,snr,tt) in zip(axs,((psk(4,np.pi/4),20,"QPSK, SNR 20 dB"),(psk(4,np.pi/4),10,"QPSK, SNR 10 dB"),(qam(16),25,"16QAM, SNR 25 dB"),(qam(16),14,"16QAM, SNR 14 dB"))):
    s=rng.choice(c,3000); n=(rng.standard_normal(3000)+1j*rng.standard_normal(3000))*np.sqrt(10**(-snr/10)/2)
    r=s+n; ax.plot(r.real,r.imag,".",color=B,ms=1.5,alpha=.5,rasterized=True); ax.plot(c.real,c.imag,"+",color=O,ms=8)
    ax.set_xlim(-1.6,1.6); ax.set_ylim(-1.6,1.6); ax.set_aspect("equal"); ax.set_xticks([]); ax.set_yticks([]); ax.set_title(tt,color=A,fontsize=11)
fig.tight_layout(); fig.savefig("noisy.svg",transparent=True,dpi=150)
# eye diagrams with raised cosine
def rc(beta,sps,span=8):
    tt=np.arange(-span*sps,span*sps+1)/sps
    h=np.sinc(tt)*np.cos(np.pi*beta*tt)/(1-(2*beta*tt)**2+1e-12); h[np.isinf(h)]=0; return h
def eye(ax,beta,snr,title,M=2):
    sps=32; sym=rng.choice(np.linspace(-1,1,M),600); x=np.zeros(len(sym)*sps); x[::sps]=sym
    y=np.convolve(x,rc(beta,sps),mode="same"); y=y+rng.standard_normal(len(y))*np.sqrt(10**(-snr/10)*0.5) if snr else y
    for k in range(20,560): seg=y[k*sps-sps:k*sps+sps+1]; ax.plot(np.linspace(-1,1,len(seg)),seg,color=B,lw=.6,alpha=.25,rasterized=True)
    ax.set_title(title,color=A,fontsize=11); ax.set_xticks([-1,0,1]); ax.set_xticklabels(["−T","istante di\ncampionamento","+T"],fontsize=8); ax.set_yticks([]); ax.set_ylim(-1.9,1.9)
fig,axs=plt.subplots(1,3,figsize=(11,3.2))
eye(axs[0],0.5,None,"2 livelli, pulito"); eye(axs[1],0.5,14,"2 livelli, con rumore"); eye(axs[2],0.5,None,"4 livelli (come 4FSK/4PAM)",M=4)
fig.tight_layout(); fig.savefig("eye.svg",transparent=True,dpi=150)
# pulse spectrum
f=np.linspace(-3,3,3000)
def rcs(f,b):
    a=abs(f); return np.where(a<=(1-b)/2,1,np.where(a<=(1+b)/2,0.5*(1+np.cos(np.pi/b*(a-(1-b)/2))),0))
fig,ax=plt.subplots(figsize=(5.8,3.4)); 
ax.plot(f,10*np.log10(np.sinc(f)**2+1e-9),color=G,lw=1.8,label="impulsi rettangolari")
for b,c in((0.35,B),(1.0,A)): ax.plot(f,10*np.log10(rcs(f,b)+1e-9),color=c,lw=2,label=f"coseno rialzato α = {b}".replace(".",","))
ax.set_xlabel("frequenza / symbol rate"); ax.set_ylabel("dB"); ax.legend(frameon=False,fontsize=9,loc="lower center"); ax.grid(alpha=.2); ax.set_ylim(-50,5)
fig.tight_layout(); fig.savefig("rcspec.svg",transparent=True)
