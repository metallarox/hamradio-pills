import numpy as np
from deck import mpl_setup
plt=mpl_setup(); A="#0a1a2e"; B="#1593d1"; G="#9aa5b4"; O="#e0563b"
# rise time
t=np.linspace(-10e-9,30e-9,2000); tau=4e-9/2.197
y=np.where(t<0,0,1-np.exp(-t/tau))
fig,ax=plt.subplots(figsize=(6.2,3.8)); ax.plot(t*1e9,y,color=B,lw=2.4)
t10=-tau*np.log(0.9); t90=-tau*np.log(0.1)
for lv,tx in((0.1,t10),(0.9,t90)): ax.axhline(lv,color=G,ls=":"); ax.plot(tx*1e9,lv,"o",color=A)
ax.annotate("",xy=(t90*1e9,0.5),xytext=(t10*1e9,0.5),arrowprops=dict(arrowstyle="<->",color=A)); ax.text(t90*1e9+1,0.5,"t_s = 4 ns (10–90 %)",color=A,fontsize=11,va="center")
ax.text(18,0.12,"10 %",color="#555"); ax.text(18,0.84,"90 %",color="#555")
ax.set_xlabel("tempo (ns)"); ax.set_ylabel("ampiezza normalizzata"); ax.grid(alpha=.25)
fig.tight_layout(); fig.savefig("rise.svg",transparent=True)
# phase + lissajous
t=np.linspace(0,2e-6,2000); f=1e6; ph=np.radians(60)
fig,axs=plt.subplots(1,2,figsize=(10,3.6),gridspec_kw=dict(width_ratios=[1.6,1]))
ax=axs[0]; ax.plot(t*1e6,np.sin(2*np.pi*f*t),color=A,lw=2,label="CH1"); ax.plot(t*1e6,np.sin(2*np.pi*f*t-ph),color=B,lw=2,label="CH2")
dt=ph/(2*np.pi*f); ax.annotate("",xy=(0.25+dt*1e6,1.08),xytext=(0.25,1.08),arrowprops=dict(arrowstyle="<->",color=O)); ax.text(0.25+dt*0.5e6,1.18,"Δt",ha="center",color=O)
ax.set_xlabel("tempo (µs)"); ax.set_ylim(-1.3,1.45); ax.legend(frameon=False,loc="lower right",fontsize=10); ax.grid(alpha=.25)
ax=axs[1]; x=np.sin(2*np.pi*f*t); yy=np.sin(2*np.pi*f*t-ph); ax.plot(x,yy,color=B,lw=2.2); ax.set_aspect("equal")
ax.axhline(0,color=G,lw=.8); ax.axvline(0,color=G,lw=.8)
ax.annotate("",xy=(0.06,np.sin(ph)),xytext=(0.06,-np.sin(ph)),arrowprops=dict(arrowstyle="<->",color=O)); ax.text(0.1,0.05,"B",color=O,fontsize=12)
ax.annotate("",xy=(1.12,1),xytext=(1.12,-1),arrowprops=dict(arrowstyle="<->",color=A)); ax.text(1.17,0.05,"A",color=A,fontsize=12)
ax.set_xlim(-1.3,1.45); ax.set_ylim(-1.25,1.35); ax.set_title("XY: sin φ = B / A",color=A,fontsize=12,pad=8); ax.set_xticks([]); ax.set_yticks([])
fig.tight_layout(); fig.savefig("phase.svg",transparent=True)
# AM envelope & trapezoid
t=np.linspace(0,2e-3,20000); fm=1e3; fc=30e3; m=0.5
mod=1+m*np.cos(2*np.pi*fm*t); s=mod*np.cos(2*np.pi*fc*t)
fig,axs=plt.subplots(1,2,figsize=(10,3.4),gridspec_kw=dict(width_ratios=[1.6,1]))
ax=axs[0]; ax.plot(t*1e3,s,color=B,lw=.8); ax.plot(t*1e3,mod,color=A,lw=1.5); ax.plot(t*1e3,-mod,color=A,lw=1.5)
ax.text(0.02,1.62,"V_max",color=O); ax.text(0.47,0.62,"V_min",color=O); ax.set_xlabel("tempo (ms)"); ax.grid(alpha=.25); ax.set_ylim(-1.8,1.9)
ax=axs[1]
for xv in np.linspace(-1,1,41):
    h=1+m*xv; ax.plot([xv,xv],[-h,h],color=B,lw=1.2)
xe=np.linspace(-1,1,10); ax.plot(xe,1+m*xe,color=A,lw=2); ax.plot(xe,-(1+m*xe),color=A,lw=2)
ax.annotate("",xy=(1.12,1.5),xytext=(1.12,-1.5),arrowprops=dict(arrowstyle="<->",color="#e0563b")); ax.text(1.16,0,"lato lungo",color="#e0563b",fontsize=10,rotation=90,va="center")
ax.annotate("",xy=(-1.12,0.5),xytext=(-1.12,-0.5),arrowprops=dict(arrowstyle="<->",color="#e0563b")); ax.text(-1.45,0,"corto",color="#e0563b",fontsize=10,rotation=90,va="center")
ax.set_xlim(-1.6,1.4); ax.set_title("trapezio: audio su X, RF su Y",color=A,fontsize=11); ax.set_xticks([]); ax.set_yticks([])
fig.tight_layout(); fig.savefig("am.svg",transparent=True)
