"""Grafici per il "vezzo matematico" della pagina Fluke Hydra Monitor.
python3 tools/progetti/hydra_needle_plots.py  ->  progetti/fluke-hydra-monitor/img/math/*.svg"""
import os, math, numpy as np, matplotlib
matplotlib.use("Agg"); import matplotlib.pyplot as plt
OUT=os.path.join(os.path.dirname(__file__),"..","..","progetti","fluke-hydra-monitor","img","math"); os.makedirs(OUT,exist_ok=True)
plt.rcParams.update({"font.family":"DejaVu Sans","font.size":11,"axes.spines.top":False,"axes.spines.right":False,"svg.fonttype":"none","axes.formatter.use_locale":False})
A="#0a1a2e"; B="#1593d1"; O="#e0563b"; G="#9aa5b4"; V="#2a9d5c"; P="#8e5bd1"
wn,Z,dt,PEG=13.0,0.55,0.008,0.055
it=lambda x,d=2: f"{x:.{d}f}".replace(".",",")
def save(fig,n): fig.tight_layout(); fig.savefig(os.path.join(OUT,n),transparent=True); plt.close(fig)
def step(z,t):
    if z<1: wd=wn*math.sqrt(1-z*z); return 1-np.exp(-z*wn*t)/math.sqrt(1-z*z)*np.sin(wd*t+math.acos(z))
    if z==1: return 1-(1+wn*t)*np.exp(-wn*t)
    r=math.sqrt(z*z-1); s1,s2=-wn*(z-r),-wn*(z+r); return 1+(s2*np.exp(s1*t)-s1*np.exp(s2*t))/(s1-s2)
def sim(target,pos=0.0,vel=0.0,T=1.6,stops=True):
    out=[pos]
    for _ in range(int(T/dt)):
        acc=wn*wn*(target-pos)-2*Z*wn*vel; vel+=acc*dt; pos+=vel*dt
        hi,lo=1+PEG+0.01,-PEG-0.01
        if stops and (pos>hi or pos<lo): pos=min(max(pos,lo),hi); vel*=-0.25
        out.append(pos)
    return np.arange(len(out))*dt,np.array(out)
t=np.linspace(0,1.2,1200)
# 1) risposta al gradino per diversi smorzamenti
fig,ax=plt.subplots(figsize=(7,4.2))
ax.axhspan(0.98,1.02,color=V,alpha=.12); ax.text(1.12,1.035,"±2 %",color=V,fontsize=9)
for z,c,lw in [(0.2,G,1.4),(0.55,O,3),(0.707,B,1.8),(1.0,A,1.8),(2.0,P,1.6)]:
    ax.plot(t,step(z,t),color=c,lw=lw,label=f"ζ = {it(z,3) if z==0.707 else it(z,2)}"+("  (Hydra Monitor)" if z==0.55 else ""))
ax.plot([0.2894],[1.1263],"o",color=O); ax.annotate("sovraelongazione 12,6 %\na 0,29 s",xy=(0.2894,1.1263),xytext=(0.45,1.38),fontsize=9.5,color=O,arrowprops=dict(arrowstyle="->",color=O))
ax.set_xlabel("tempo (s)"); ax.set_ylabel("posizione dell'ago (frazione del gradino)"); ax.set_ylim(0,1.6); ax.set_xlim(0,1.2); ax.grid(alpha=.25)
ax.legend(frameon=False,fontsize=9.5,loc="lower right"); save(fig,"step.svg")
# 2) poli nel piano s
fig,ax=plt.subplots(figsize=(5.8,4.2))
th=np.linspace(math.pi/2,3*math.pi/2,200); ax.plot(wn*np.cos(th),wn*np.sin(th),color=G,lw=1,ls="--")
for z,c in [(0.2,G),(0.55,O),(0.707,B),(1.0,A)]:
    s=complex(-z*wn,wn*math.sqrt(max(0,1-z*z))); ax.plot([s.real,s.real],[s.imag,-s.imag],"x",color=c,ms=11,mew=2.4,label=f"ζ = {it(z,3) if z==0.707 else it(z,2)}")
ax.plot([0,-Z*wn],[0,wn*math.sqrt(1-Z*Z)],color=O,lw=1); ax.text(-3.6,4.0,"ωn = 13",color=O,fontsize=9.5)
ax.annotate("",xy=(-7.15,0),xytext=(0,0),arrowprops=dict(arrowstyle="<->",color=A)); ax.text(-6.8,-1.4,"ζ·ωn = 7,15",fontsize=9)
ax.text(-14.6,13.2,"ωd = 10,86",fontsize=9,color=O)
ax.axhline(0,color=A,lw=.8); ax.axvline(0,color=A,lw=.8); ax.set_xlim(-15,3); ax.set_ylim(-15,15); ax.set_aspect("equal")
ax.set_xlabel("parte reale (1/s)"); ax.set_ylabel("parte immaginaria (rad/s)"); ax.legend(frameon=False,fontsize=9,loc="center left",bbox_to_anchor=(1.02,0.5)); ax.grid(alpha=.2); save(fig,"poles.svg")
# 3) risposta in frequenza
f=np.logspace(-1,1.3,500); w=2*np.pi*f
fig,ax=plt.subplots(figsize=(6,3.8))
for z,c,lw in [(0.2,G,1.4),(0.55,O,3),(0.707,B,1.8),(1.0,A,1.6)]:
    H=wn**2/np.sqrt((wn**2-w**2)**2+(2*z*wn*w)**2); ax.plot(f,20*np.log10(H),color=c,lw=lw,label=f"ζ = {it(z,3) if z==0.707 else it(z,2)}")
ax.axhline(-3,color=G,ls=":",lw=1); ax.text(0.11,-2.6,"−3 dB",fontsize=9,color="#555")
ax.plot([1.30],[0.74],"o",color=O); ax.annotate("+0,74 dB a 1,3 Hz",xy=(1.30,0.74),xytext=(0.15,6),fontsize=9.5,color=O,arrowprops=dict(arrowstyle="->",color=O))
ax.set_xscale("log"); ax.set_ylim(-30,10); ax.set_xlabel("frequenza con cui varia la lettura (Hz)"); ax.set_ylabel("ampiezza dell'ago (dB)"); ax.grid(alpha=.25,which="both"); ax.legend(frameon=False,fontsize=9,loc="lower left")
ax.set_xticks([0.1,0.3,1,3,10]); ax.set_xticklabels(["0,1","0,3","1","3","10"]); save(fig,"freq.svg")
# 4) fondo scala e rimbalzo (stesso algoritmo del programma)
fig,ax=plt.subplots(figsize=(6.4,3.9))
ts,ps=sim(1+PEG); ax.plot(ts,ps,color=O,lw=2.4,label="overload: obiettivo 105,5 %")
ts,ps=sim(0.8); ax.plot(ts,ps,color=B,lw=2,label="lettura all'80 %")
ts,ps=sim(1+PEG,stops=False); ax.plot(ts,ps,color=G,lw=1.2,ls="--",label="senza fermo meccanico")
ax.axhline(1+PEG+0.01,color=A,lw=2); ax.text(0.75,1.09,"fermo meccanico (106,5 %)",fontsize=9)
ax.axhline(1.0,color=G,lw=.8,ls=":"); ax.text(1.3,0.965,"fondo scala",fontsize=9,color="#555")
ax.set_xlim(0,1.6); ax.set_ylim(0,1.25); ax.set_xlabel("tempo (s)"); ax.set_ylabel("posizione (frazione del fondo scala)"); ax.grid(alpha=.25); ax.legend(frameon=False,fontsize=9,loc="lower right"); save(fig,"stop.svg")
# 5) integratore: continuo contro discreto
fig,ax=plt.subplots(figsize=(5.6,3.6))
ax.plot(t,step(Z,t),color=A,lw=2,label="soluzione esatta (ζ = 0,55)")
ts,ps=sim(1.0,stops=False); ax.plot(ts,ps,".",color=O,ms=4,label="Euler semi-implicito, passo 8 ms")
ax.set_xlim(0,0.8); ax.set_ylim(0,1.25); ax.set_xlabel("tempo (s)"); ax.set_ylabel("posizione"); ax.grid(alpha=.25); ax.legend(frameon=False,fontsize=9,loc="lower right"); save(fig,"euler.svg")
print("ok")
