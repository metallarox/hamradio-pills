import numpy as np
from deck import mpl_setup
plt=mpl_setup(); A="#0a1a2e"; B="#1593d1"; G="#9aa5b4"; O="#e0563b"
# ripple: full-wave 100 Hz, 1 A, 10000 uF -> ~1 Vpp sawtooth around 16 V
t=np.linspace(0,40e-3,8000); T=10e-3; I=1; C=10000e-6; Vpk=16.5
dv=I*T/C
ph=(t%T)/T; charge=0.15  # fraction of period charging
v=np.where(ph<1-charge, Vpk-dv*ph/(1-charge), Vpk-dv+dv*(ph-(1-charge))/charge)
rng=np.random.default_rng(1); v=v+0.004*rng.standard_normal(t.shape)
fig,axs=plt.subplots(1,2,figsize=(11,3.4))
ax=axs[0]; ax.plot(t*1e3,v,color=A,lw=1.6); ax.set_ylim(0,20); ax.set_title("DC, 5 V/div: sembra una linea piatta",color=A,fontsize=12)
ax.set_xlabel("tempo (ms)"); ax.set_ylabel("V"); ax.grid(alpha=.25)
ax=axs[1]; ax.plot(t*1e3,(v-v.mean())*1e3,color=B,lw=1.6); ax.set_title("AC, 200 mV/div: il ripple a 100 Hz",color=A,fontsize=12)
ax.annotate("",xy=(31,(Vpk-v.mean())*1e3),xytext=(31,(Vpk-dv-v.mean())*1e3),arrowprops=dict(arrowstyle="<->",color=O)); ax.text(31.8,620,f"≈ {dv:.1f} V pp".replace(".",","),color=O,fontsize=11)
ax.set_xlabel("tempo (ms)"); ax.set_ylabel("mV"); ax.set_ylim(-800,800); ax.grid(alpha=.25)
fig.tight_layout(); fig.savefig("ripple.svg",transparent=True)
# component tester XY
th=np.linspace(0,2*np.pi,600); vs=np.sin(th)  # source, through R
fig,axs=plt.subplots(1,4,figsize=(11,2.9))
def setup(ax,tt): ax.set_title(tt,color=A,fontsize=12); ax.axhline(0,color=G,lw=.6); ax.axvline(0,color=G,lw=.6); ax.set_xticks([]); ax.set_yticks([]); ax.set_xlim(-1.2,1.2); ax.set_ylim(-1.2,1.2); ax.set_aspect("equal")
# resistor: V=0.5 vs, I=0.5 vs
setup(axs[0],"resistenza"); axs[0].plot(0.6*vs,0.6*vs,color=B,lw=2.4)
setup(axs[1],"condensatore"); axs[1].plot(0.8*np.cos(th),0.8*np.sin(th),color=B,lw=2.4)
# diode: V clamps at 0.65 forward
vd=np.where(vs>0,np.minimum(vs,0.6+0.05*vs),vs); i=np.where(vs>0,(vs-vd)/0.5,0)
setup(axs[2],"diodo"); axs[2].plot(vd,np.clip(i,0,1.1),color=B,lw=2.4)
vz=np.where(vs>0,np.minimum(vs,0.6+0.05*vs),np.maximum(vs,-0.8+0.05*vs)); iz=np.where(vs>0,(vs-vz)/0.5,(vs-vz)/0.5)
setup(axs[3],"zener"); axs[3].plot(vz,np.clip(iz,-1.1,1.1),color=B,lw=2.4)
for ax in axs: ax.text(1.12,-0.18,"V",fontsize=10,color="#555"); ax.text(0.06,1.05,"I",fontsize=10,color="#555")
fig.tight_layout(); fig.savefig("xy.svg",transparent=True)
# TDR traces
t=np.linspace(-20,220,2000); td=101  # ns round trip for 10 m VF .66
def tr(r):
    return np.where(t<0,0,0.5)+np.where(t<td,0,0.5*r)
fig,ax=plt.subplots(figsize=(6.4,3.6))
for r,c,lab in((1,O,"fine aperta"),(0,B,"chiusa su 50 Ω"),(-1,A,"fine in corto")):
    ax.plot(t,tr(r),color=c,lw=2.2,label=lab)
ax.annotate("",xy=(td,1.12),xytext=(0,1.12),arrowprops=dict(arrowstyle="<->",color="#555")); ax.text(td/2,1.17,"2·d / v ≈ 101 ns (10 m, VF 0,66)",ha="center",color="#555",fontsize=10)
ax.set_ylim(-0.1,1.3); ax.set_xlabel("tempo (ns)"); ax.set_ylabel("tensione all'ingresso del cavo"); ax.legend(frameon=False,loc="upper left",bbox_to_anchor=(0.0,0.92),fontsize=10); ax.grid(alpha=.25)
fig.tight_layout(); fig.savefig("tdr.svg",transparent=True)
print("dv",dv, "td", 2*10/(0.66*0.299792458))
