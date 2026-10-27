import numpy as np, json
from deck import mpl_setup
plt=mpl_setup(); A="#0a1a2e"; B="#1593d1"; O="#e0563b"; G="#9aa5b4"
N=500; x=np.linspace(-1,1,N); X,Y=np.meshgrid(x,x); R=np.hypot(X,Y)+1e-3; TH=np.arctan2(Y,X)  # 0 = right
def pat(kind,th):
    if kind=="iso": return np.ones_like(th)
    if kind=="flat": return np.where(np.cos(th)>0,2.0,0.03)
    if kind=="curved":
        p=np.where(np.cos(th)>0,np.cos(th)**3,0.0)+0.01; return p
    if kind=="para":
        return np.exp(-(th/0.08)**2)+0.003
def norm(kind):
    t=np.linspace(-np.pi,np.pi,20001); p=pat(kind,t); return p/np.mean(p)  # 2D normalisation: mean = 1
gains={}
def panel(kind,fname,title):
    t=np.linspace(-np.pi,np.pi,20001); p=pat(kind,t); k=1/np.mean(p); gains[kind]=float(np.max(p)*k)
    I=pat(kind,TH)*k/(1+18*R**2)
    if kind=="para":  # parallel beam: brightness along a strip in front
        I=np.where((X>0.12)&(np.abs(Y)<0.12),1.0*gains["para"]/(1+0.5*X**2),0.0)+0.003*k/(1+18*R**2)
        I=np.maximum(I,np.where(R<0.25,pat(kind,TH)*k/(1+18*R**2)*0.0,0))
    fig,ax=plt.subplots(figsize=(4.6,4.6)); ax.set_facecolor("black")
    ax.imshow(np.log10(I+1e-4),extent=(-1,1,-1,1),origin="lower",cmap="inferno",vmin=-3.2,vmax=np.log10(40))
    if kind=="flat": ax.plot([-0.12,-0.12],[-0.45,0.45],color="#cfe8ff",lw=4)
    if kind=="curved":
        a=np.linspace(np.radians(120),np.radians(240),100); ax.plot(0.32*np.cos(a)+0.08,0.32*np.sin(a),color="#cfe8ff",lw=4)
    if kind=="para":
        yy=np.linspace(-0.4,0.4,100); ax.plot(yy**2/(4*0.12)-0.12,yy,color="#cfe8ff",lw=4)
    ax.plot(0,0,"o",color="#ffe9a8",ms=9); ax.set_xticks([]); ax.set_yticks([])
    for s in ax.spines.values(): s.set_color(A)
    ax.set_title(title,color=A,fontsize=13)
    fig.tight_layout(); fig.savefig(fname,transparent=True)
panel("iso","c1.svg","la candela da sola"); panel("flat","c2.svg","uno specchio piano")
panel("curved","c3.svg","uno specchio curvo"); panel("para","c4.svg","la parabola, candela nel fuoco")
print({k:(v,10*np.log10(v)) for k,v in gains.items()})
# polar patterns of the four (2D, normalized to isotropic, dBi-like clipped at -20)
fig,axs=plt.subplots(1,4,subplot_kw=dict(projection="polar"),figsize=(11,3.3))
t=np.linspace(-np.pi,np.pi,2001)
for ax,k,tt in zip(axs,("iso","flat","curved","para"),("candela","specchio piano","specchio curvo","parabola")):
    p=pat(k,t)/np.mean(pat(k,np.linspace(-np.pi,np.pi,20001))); d=np.clip(10*np.log10(p),-20,30)
    ax.plot(t,d+20,color=B,lw=2); ax.set_ylim(0,45); ax.set_yticks([20,30,40]); ax.set_yticklabels(["0","10","20 dB"],fontsize=8); ax.set_xticklabels([]); ax.set_title(tt,color=A,fontsize=12,pad=10)
fig.tight_layout(); fig.savefig("polar4.svg",transparent=True)
# real antenna patterns (E-plane)
th=np.linspace(1e-4,2*np.pi,4001)
dip=(np.cos(np.pi/2*np.cos(th))/np.sin(th))**2; dip=np.nan_to_num(dip); dip=dip/dip.max()*10**(2.15/10)
yag=((1+np.cos(th))/2)**18+0.01; Dy=10**(12/10); yag=yag/yag.max()*Dy
par=np.exp(-((np.angle(np.exp(1j*th)))/np.radians(2.1/2*1.2))**2*np.log(2)*0.7)+2e-4; par=par/par.max()*10**(37.8/10)
fig,axs=plt.subplots(1,3,subplot_kw=dict(projection="polar"),figsize=(10.5,3.6))
for ax,p,tt,lim in zip(axs,(dip,yag,par),("dipolo: 2,15 dBi","yagi: ~12 dBi","parabola 1 m a 10 GHz: ~38 dBi"),(5,15,40)):
    d=np.clip(10*np.log10(p+1e-9),lim-30,lim); ax.plot(th,d-(lim-30),color=B,lw=2); ax.set_ylim(0,30); ax.set_yticks([10,20,30]); ax.set_yticklabels([f"{lim-20}",f"{lim-10}",f"{lim} dBi"],fontsize=8); ax.set_xticklabels([]); ax.set_title(tt,color=A,fontsize=11,pad=10)
    if tt.startswith("dipolo"): ax.set_theta_zero_location("N")
fig.tight_layout(); fig.savefig("patterns.svg",transparent=True)
json.dump(gains,open("vals.json","w"))
