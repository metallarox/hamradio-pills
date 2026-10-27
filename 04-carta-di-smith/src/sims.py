import numpy as np, json, matplotlib
matplotlib.use("svg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.family":"DejaVu Sans","font.size":12})
A="#0a1a2e"; B="#1593d1"; G="#9aa5b4"; LG="#d5dbe3"; O="#e0563b"; Z0=50; out={}
gam=lambda z:(z-1)/(z+1)  # normalized
def smith(size=5.0,labels=True,admit=False):
    fig,ax=plt.subplots(figsize=(size,size)); ax.set_aspect("equal"); ax.axis("off")
    t=np.linspace(0,2*np.pi,500)
    for r in [0,0.2,0.5,1,2,5]:
        c=r/(1+r); rad=1/(1+r); ax.plot(c+rad*np.cos(t),rad*np.sin(t),color=LG if r else G,lw=.9 if r else 1.4,zorder=0)
    for x in [0.2,0.5,1,2,5]:
        for s in(1,-1):
            zz=1j*s*x+np.concatenate((np.linspace(0,5,800),np.linspace(5,200,400))); g=gam(zz); ax.plot(g.real,g.imag,color=LG,lw=.9,zorder=0)
    if admit:
        for gg in [0.2,0.5,1,2,5]:
            c=-gg/(1+gg); rad=1/(1+gg); ax.plot(c+rad*np.cos(t),rad*np.sin(t),color="#f3c9bf",lw=.9,zorder=0)
    ax.plot([-1,1],[0,0],color=G,lw=1,zorder=0)
    if labels:
        for r in [0.2,0.5,1,2,5]:
            ax.text(gam(r).real,0.02,f"{r:g}",fontsize=8,color="#7a8696",ha="center",va="bottom",rotation=90)
        for x in [0.2,0.5,1,2,5]:
            for s in (1,-1):
                g=gam(1j*s*x); ax.text(g.real*1.07,g.imag*1.07,("+" if s>0 else "−")+f"{x:g}",fontsize=8,color="#7a8696",ha="center",va="center")
    ax.set_xlim(-1.15,1.15); ax.set_ylim(-1.15,1.15)
    return fig,ax
def pt(ax,z,lab,col=A,dx=8,dy=8,ha="left"):
    g=gam(z); ax.plot(g.real,g.imag,"o",color=col,ms=6,zorder=5)
    ax.annotate(lab,(g.real,g.imag),xytext=(dx,dy),textcoords="offset points",color=col,fontsize=11,ha=ha,zorder=6)
def swr_circle(ax,s,col=B,ls="--",lab=None):
    r=(s-1)/(s+1); t=np.linspace(0,2*np.pi,300); ax.plot(r*np.cos(t),r*np.sin(t),color=col,ls=ls,lw=1.4,label=lab)
# 1 anatomy
fig,ax=smith(5.4)
pt(ax,1,"50 Ω (centro)",A,8,-16)
ax.plot(-1,0,"o",color=A); ax.text(-1.04,0.06,"corto",ha="right",color=A,fontsize=11)
ax.plot(1,0,"o",color=A); ax.text(1.03,0.06,"aperto",color=A,fontsize=11)
ax.text(0,0.62,"INDUTTIVO (+jX)",ha="center",color=B,fontsize=12,fontweight="bold")
ax.text(0,-0.68,"CAPACITIVO (−jX)",ha="center",color=B,fontsize=12,fontweight="bold")
ax.text(-0.55,0.07,"R < 50 Ω",ha="center",color="#555",fontsize=10); ax.text(0.55,0.07,"R > 50 Ω",ha="center",color="#555",fontsize=10)
swr_circle(ax,2,lab="SWR 2:1")
pt(ax,(25+25j)/50,"25 + j25 Ω",O,8,6)
ax.legend(frameon=False,loc="lower right",fontsize=10)
fig.tight_layout(); fig.savefig("anatomy.svg",transparent=True)
z=(25+25j)/50; g=gam(z); out["ex_g"]=[abs(g),np.degrees(np.angle(g)),(1+abs(g))/(1-abs(g))]
# 2 movements
fig,ax=smith(5.4,admit=True)
def arc_r(ax,z0,x1,col,lab):
    xs=np.linspace(z0.imag,x1,60); g=gam(z0.real+1j*xs); ax.plot(g.real,g.imag,color=col,lw=2.6)
    ax.annotate("",xy=(g[-1].real,g[-1].imag),xytext=(g[-4].real,g[-4].imag),arrowprops=dict(arrowstyle="-|>",color=col,lw=2))
    ax.text(g[-1].real+0.03,g[-1].imag+(0.05 if x1>z0.imag else -0.1),lab,color=col,fontsize=11)
def arc_g(ax,y0,b1,col,lab,off=(0.03,0.03)):
    bs=np.linspace(y0.imag,b1,60); g=gam(1/(y0.real+1j*bs)); ax.plot(g.real,g.imag,color=col,lw=2.6)
    ax.annotate("",xy=(g[-1].real,g[-1].imag),xytext=(g[-4].real,g[-4].imag),arrowprops=dict(arrowstyle="-|>",color=col,lw=2))
    ax.text(g[-1].real+off[0],g[-1].imag+off[1],lab,color=col,fontsize=11)
arc_r(ax,1+0j,1.2,B,"L serie")
arc_r(ax,1+0j,-1.2,B,"C serie")
arc_g(ax,1+0j,1.2,O,"C parallelo",(-0.42,-0.1))
arc_g(ax,1+0j,-1.2,O,"L parallelo",(-0.45,0.05))
fig.tight_layout(); fig.savefig("moves.svg",transparent=True)
# 3 dipole sweep (series RLC model) 40 m, resonant 7.03 MHz, R 65
f=np.linspace(6.7e6,7.4e6,701); fr=7.03e6; R=65; Qa=12; L=Qa*R/(2*np.pi*fr); C=1/((2*np.pi*fr)**2*L)
Zd=R+1j*2*np.pi*f*L+1/(1j*2*np.pi*f*C); Gd=(Zd-Z0)/(Zd+Z0); swr=(1+abs(Gd))/(1-abs(Gd))
ok=f[swr<=2]; out["dip_bw"]=[ok.min(),ok.max()]
fig,ax=smith(5.0)
ax.plot(Gd.real,Gd.imag,color=B,lw=2.4); swr_circle(ax,2,col=G,lab="SWR 2:1")
for ff,lab,dx,dy in((6.8e6,"6,80",-40,-4),(7.03e6,"7,03 (risonanza)",8,-16),(7.1e6,"7,10",8,4),(7.3e6,"7,30 MHz",8,0)):
    zz=np.interp(ff,f,Zd.real)+1j*np.interp(ff,f,Zd.imag); pt(ax,zz/50,lab,A,dx,dy)
z71=np.interp(7.1e6,f,Zd.real)+1j*np.interp(7.1e6,f,Zd.imag); out["z71"]=[z71.real,z71.imag]
ax.legend(frameon=False,loc="lower right",fontsize=10)
fig.tight_layout(); fig.savefig("dipole.svg",transparent=True)
# 4 L-network 25-j40 @14.2 MHz: series L then shunt C (low-pass)
fq=14.2e6; w=2*np.pi*fq; zl=(25-40j)/50
x_target=0.5; Xs=(x_target-zl.imag)*50; Ls=Xs/w
z1=zl+1j*(x_target-zl.imag); y1=1/z1; Bp=-y1.imag; Cp=Bp/50/w
zin=1/(y1+1j*Bp)*50
out["lnet"]=dict(Xs=Xs,Ls=Ls,Bp=Bp,Cp=Cp,zin=[zin.real,zin.imag])
fig,ax=smith(5.0,admit=True)
xs=np.linspace(zl.imag,x_target,60); g=gam(zl.real+1j*xs); ax.plot(g.real,g.imag,color=B,lw=2.6)
ax.annotate("",xy=(g[-1].real,g[-1].imag),xytext=(g[-4].real,g[-4].imag),arrowprops=dict(arrowstyle="-|>",color=B,lw=2))
bs=np.linspace(y1.imag,0,60); g=gam(1/(y1.real+1j*bs)); ax.plot(g.real,g.imag,color=O,lw=2.6)
ax.annotate("",xy=(g[-1].real,g[-1].imag),xytext=(g[-4].real,g[-4].imag),arrowprops=dict(arrowstyle="-|>",color=O,lw=2))
pt(ax,zl,"carico 25 − j40 Ω",A,8,-14); pt(ax,z1,"25 + j25 Ω",A,-10,8,"right"); pt(ax,1,"50 Ω",A,8,-16)
ax.text(-0.85,-0.3,"① L serie",color=B,fontsize=11); ax.text(0.04,0.3,"② C parallelo",color=O,fontsize=11)
fig.tight_layout(); fig.savefig("lnet.svg",transparent=True)
# 5 single shunt stub, 145 MHz, ZL=100+j50
zl=(100+50j)/50; gl=gam(zl)
d=np.linspace(0,0.5,200001); gd=gl*np.exp(-1j*4*np.pi*d); yd=(1-gd)/(1+gd)
i=np.where(np.diff(np.sign(yd.real-1)))[0][0]; d1=d[i]; y_at=yd[i]; bstub=-y_at.imag
# short stub: y = -j cot(beta l)  -> need -cot(bl)=bstub
ls=np.arctan(1/(-bstub))/(2*np.pi) if bstub!=0 else 0.25
ls=ls%0.5
out["stub"]=dict(d=d1,y=[y_at.real,y_at.imag],b=bstub,l=ls)
yc=y_at+1j*bstub; out["stub"]["check"]=[yc.real,yc.imag]
fig,ax=smith(5.0,admit=True)
gg=gd[:i+1]; ax.plot(gg.real,gg.imag,color=B,lw=2.6)
ax.annotate("",xy=(gg[-1].real,gg[-1].imag),xytext=(gg[-200].real,gg[-200].imag),arrowprops=dict(arrowstyle="-|>",color=B,lw=2))
bs=np.linspace(y_at.imag,0,60); g=gam(1/(y_at.real+1j*bs)); ax.plot(g.real,g.imag,color=O,lw=2.6)
ax.annotate("",xy=(g[-1].real,g[-1].imag),xytext=(g[-4].real,g[-4].imag),arrowprops=dict(arrowstyle="-|>",color=O,lw=2))
pt(ax,zl,"antenna 100 + j50 Ω",A,8,6); zat=1/y_at; pt(ax,zat,f"dopo {d1:.3f} λ",A,8,8); pt(ax,1,"50 Ω",A,-8,-16,"right")
swr_circle(ax,(1+abs(gl))/(1-abs(gl)),col=G,ls=":")
ax.text(0.05,-0.62,"① linea (senso orario)",color=B,fontsize=11); ax.text(-0.15,0.62,"② stub in parallelo",color=O,fontsize=11)
fig.tight_layout(); fig.savefig("stub.svg",transparent=True)
# 6 lossy line spiral: ZL 100 ohm, total one-way loss 3 dB, 1.25 wavelengths
zl=2.0; gl=gam(zl); L1=np.linspace(0,1.25,2000); a=3/8.686/1.25  # nepers per wavelength
gin=gl*np.exp(-2*a*L1)*np.exp(-1j*4*np.pi*L1)
fig,ax=smith(5.0)
ax.plot(gin.real,gin.imag,color=B,lw=2.2,label="linea con 3 dB di perdita")
swr_circle(ax,2,col=G,ls="--",lab="linea senza perdite (SWR 2)")
pt(ax,zl,"antenna 100 Ω",A,6,12); ge=gin[-1]; ax.plot(ge.real,ge.imag,"o",color=O); ax.annotate("in stazione",(ge.real,ge.imag),xytext=(8,-14),textcoords="offset points",color=O,fontsize=11)
ax.legend(frameon=False,loc="lower center",bbox_to_anchor=(0.5,-0.06),fontsize=10)
fig.tight_layout(); fig.savefig("lossy.svg",transparent=True)
out["lossy_end"]=[abs(ge),(1+abs(ge))/(1-abs(ge))]
print(json.dumps(out,indent=1,default=float)); json.dump(out,open("vals.json","w"),default=float)
