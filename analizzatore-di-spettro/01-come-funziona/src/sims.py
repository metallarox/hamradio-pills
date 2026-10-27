import numpy as np, json
from deck import sa_trace, mpl_setup
plt=mpl_setup(); A="#0a1a2e"; B="#1593d1"; G="#9aa5b4"; out={}
# RBW
f=np.linspace(99.95e6,100.06e6,4001); tones=[(100.000e6,-20),(100.010e6,-45)]
fig,ax=plt.subplots(figsize=(9.6,3.9))
for rbw,col,lab in((30e3,"#9cc9e6","RBW 30 kHz"),(10e3,B,"RBW 10 kHz"),(1e3,A,"RBW 1 kHz")):
    ax.plot((f-100e6)/1e3,sa_trace(f,tones,rbw,-150,seed=int(rbw)),color=col,lw=1.6,label=lab)
ax.set_xlabel("f − 100 MHz (kHz)"); ax.set_ylabel("livello (dBm)"); ax.set_ylim(-130,-10); ax.grid(alpha=.25)
ax.annotate("segnale a −45 dBm\na +10 kHz",(10,-45),xytext=(22,-75),color=A,fontsize=11,arrowprops=dict(arrowstyle="->",color=A))
ax.legend(frameon=False,loc="upper right")
fig.tight_layout(); fig.savefig("rbw.svg",transparent=True)
# dynamic range chart
pm=np.linspace(-80,0,200); DANL=-130; SHI=40; TOI=10
fig,ax=plt.subplots(figsize=(6.6,4.4))
ax.plot(pm,DANL-pm,color=G,lw=2.2,label="rumore (RBW 1 kHz)")
ax.plot(pm,pm-SHI,color=B,lw=2.2,label="2ª armonica interna")
ax.plot(pm,2*(pm-TOI),color=A,lw=2.2,label="intermodulazione 3° ordine")
p3=(2*TOI+DANL)/3; d3=2/3*(TOI-DANL); p2=(SHI+DANL)/2; d2=(SHI-DANL)/2
ax.plot(p3,-d3,"o",color=A); ax.annotate(f"max dinamica IM3\n≈ {d3:.0f} dB a {p3:.0f} dBm",(p3,-d3),xytext=(-79,-82),color=A,fontsize=11,arrowprops=dict(arrowstyle="->",color=A))
ax.plot(p2,-d2,"o",color=B)
ax.set_xlim(-80,0); ax.set_ylim(-130,-20); ax.set_xlabel("livello al mixer (dBm)"); ax.set_ylabel("livello relativo (dBc)")
ax.legend(frameon=False,loc="upper left",fontsize=10); ax.grid(alpha=.25)
fig.tight_layout(); fig.savefig("dynrange.svg",transparent=True)
out.update(p3=p3,d3=d3,p2=p2,d2=d2); print(out); json.dump(out,open("vals.json","w"))
