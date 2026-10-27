import numpy as np, json, matplotlib
matplotlib.use("svg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.family":"DejaVu Sans","font.size":12,"axes.spines.top":False,"axes.spines.right":False})
A="#0a1a2e"; B="#1593d1"; out={}
# 1 ferrite: relaxation model
f=np.logspace(5,9,800); mui=800; fr=3e6
mu=mui/(1+1j*f/fr)**1  # Debye
fig,ax=plt.subplots(figsize=(6.4,4.0))
ax.semilogx(f/1e6,mu.real,color=A,lw=2,label="μ'  (induttiva)"); ax.semilogx(f/1e6,-mu.imag,color=B,lw=2,label="μ''  (perdite)")
ax.set_xlabel("f (MHz)"); ax.set_ylabel("permeabilità relativa"); ax.legend(frameon=False,loc="upper right"); ax.grid(alpha=.25,which="both")
ax.axvline(fr/1e6,color="#aaa",ls=":"); ax.text(fr/1e6*1.6,mui*0.55,"μ'' > μ' : zona\nresistiva (choke)",color="#555",fontsize=11)
fig.tight_layout(); fig.savefig("ferrite.svg",transparent=True)
# 2 SRF capacitor
C=100e-9; L=1e-9; R=0.02; f=np.logspace(5,9,2000); w=2*np.pi*f
Z=R+1j*w*L+1/(1j*w*C); srf=1/(2*np.pi*np.sqrt(L*C)); out["srf"]=srf
fig,ax=plt.subplots(figsize=(6.4,4.0))
ax.loglog(f/1e6,abs(Z),color=B,lw=2); ax.loglog(f/1e6,1/(w*C),color="#aaa",ls=":",lw=1); ax.loglog(f/1e6,w*L,color="#aaa",ls=":",lw=1)
ax.axvline(srf/1e6,color=A,ls="--",lw=1); ax.text(srf/1e6*1.15,3,f"SRF ≈ {srf/1e6:.1f} MHz\n|Z|min = ESR",color=A,fontsize=11)
ax.text(0.15,8,"capacitivo\n1/ωC",color="#666",fontsize=11); ax.text(150,0.25,"induttivo\nω·ESL",color="#666",fontsize=11)
ax.set_xlabel("f (MHz)"); ax.set_ylabel("|Z| (Ω)"); ax.grid(alpha=.25,which="both")
fig.tight_layout(); fig.savefig("srf.svg",transparent=True)
# 3 TDR: coax with crushed section and open end
c=299792458; VF=0.66; v=c*VF; Z0=50
N=2001; fmax=1e9; fr_=np.linspace(fmax/(N),fmax,N)  # 0.5 MHz step
segs=[(12.0,50),(0.3,62),(17.7,50)]  # length m, Z
def s11(f):
    Zl=np.full(f.shape,1e9,complex)  # open end
    for l,z in reversed(segs):
        b=2*np.pi*f/v*l; a=0.02*np.sqrt(f/1e8)*l/30  # small loss
        g=a+1j*b; Zl=z*(Zl+z*np.tanh(g))/(z+Zl*np.tanh(g))
    return (Zl-Z0)/(Zl+Z0)
S=s11(fr_); win=np.kaiser(2*N,6)[N:]
spec=np.concatenate(([ (S[0].real)],S*win))
nfft=16384; h=np.fft.irfft(spec,nfft)*nfft/ (N)  # impulse
dt=1/(2*fmax)* (2*N)/nfft
t=np.arange(nfft)*dt; d=v*t/2; m=d<40
step=np.cumsum(h)
fig,ax=plt.subplots(figsize=(10,3.1))
ax.plot(d[m],h[m]/abs(h[m]).max(),color=B,lw=1.8)
ax.set_xlabel("distanza (m), VF = 0,66"); ax.set_ylabel("riflessione (norm.)"); ax.grid(alpha=.25)
ax.annotate("cavo schiacciato\n(Z ≈ 62 Ω) a 12 m",(12.15,0.08),xytext=(4,0.5),color=A,fontsize=11,arrowprops=dict(arrowstyle="->",color=A))
ax.annotate("fine cavo aperta\na 30 m",(30,0.9),xytext=(20,0.6),color=A,fontsize=11,arrowprops=dict(arrowstyle="->",color=A))
out["dmax"]=v/(2*(fr_[1]-fr_[0]))
fig.tight_layout(); fig.savefig("tdr.svg",transparent=True)
# 4 coupled resonators
f=np.linspace(8e6,12e6,4000); f0=10e6; Lr=1e-6; Cr=1/((2*np.pi*f0)**2*Lr); Q=80; Rr=2*np.pi*f0*Lr/Q
fig,ax=plt.subplots(figsize=(6.4,4.0))
for k,col in((0.02,"#9cc9e6"),(0.05,B),(0.10,A)):
    w=2*np.pi*f; Zr=Rr+1j*w*Lr+1/(1j*w*Cr)+ 0  # series resonators, loosely coupled to 50Ω via M
    M=k*Lr; Rs=1  # source/load coupling resistance in loop
    Z1=Zr+Rs; I2=(1j*w*M)/(Z1*Z1+(w*M)**2)
    s21=2*Rs*abs(I2)
    ax.plot(f/1e6,20*np.log10(s21+1e-12),color=col,lw=2,label=f"k = {k}")
ax.set_ylim(-45,2); ax.set_xlabel("f (MHz)"); ax.set_ylabel("|S21| (dB)"); ax.legend(frameon=False,loc="lower right"); ax.grid(alpha=.25)
fig.tight_layout(); fig.savefig("coupling.svg",transparent=True)
# check k extraction for k=0.1
k=0.10; w=2*np.pi*f; M=k*Lr; Z1=Rr+1j*w*Lr+1/(1j*w*Cr)+1; s=abs((1j*w*M)/(Z1*Z1+(w*M)**2))
from scipy.signal import find_peaks
p,_=find_peaks(s); f1,f2=f[p[0]],f[p[-1]]; out["k_est"]=(f2**2-f1**2)/(f2**2+f1**2); out["f1"]=f1; out["f2"]=f2
print(out); json.dump(out,open("vals.json","w"))
