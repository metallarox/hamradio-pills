import numpy as np
from deck import mpl_setup
plt=mpl_setup(); A="#0a1a2e"; B="#1593d1"; G="#9aa5b4"; O="#e0563b"
rs=np.logspace(2,7,300)
fig,ax=plt.subplots(figsize=(6.4,3.9))
for rin,c,lab in((10e6,B,"digitale 10 MΩ"),(200e3,O,"analogico 20 kΩ/V, portata 10 V (200 kΩ)"),(1e9,A,"elettrometrico / >1 GΩ")):
    ax.semilogx(rs,100*rs/(rs+rin),color=c,lw=2.2,label=lab)
ax.axhline(1,color=G,ls=":"); ax.text(120,3,"1 %",color="#555")
ax.set_xlabel("resistenza della sorgente (Ω)"); ax.set_ylabel("lettura più bassa del vero (%)"); ax.set_ylim(0,100); ax.legend(frameon=False,loc="upper left",fontsize=10); ax.grid(alpha=.25,which="both")
fig.tight_layout(); fig.savefig("loading.svg",transparent=True)
labs=["sinusoide","onda quadra","triangolare","impulsi 10 %\n(accoppiati AC)"]; err=[0,11.1,-3.8,-33.4]
fig,ax=plt.subplots(figsize=(6.2,3.8)); bars=ax.bar(labs,err,color=[B if e>=0 else O for e in err],width=0.55)
for b,e in zip(bars,err): ax.text(b.get_x()+b.get_width()/2,e+(1.5 if e>=0 else -4.5),f"{e:+.1f} %".replace(".",",").replace("+0,0","0"),ha="center",color=A,fontsize=11)
ax.axhline(0,color=A,lw=1); ax.set_ylabel("errore del multimetro a valore medio"); ax.set_ylim(-40,18); ax.grid(alpha=.25,axis="y")
fig.tight_layout(); fig.savefig("rms.svg",transparent=True)
