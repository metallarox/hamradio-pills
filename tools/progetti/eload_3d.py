"""Modelli 3D per il visualizzatore della pagina eload-60v.

1) Scheda: esportata dal progetto KiCad con kicad-cli (KiCad 10) e compressa con gltf-transform:
   kicad-cli pcb export glb --subst-models --include-tracks --include-pads --include-zones \
       --include-silkscreen --include-soldermask --user-origin 135x102.5mm -o eload.glb eload_4ch.kicad_pcb
   gltf-transform optimize eload.glb board.glb --compress meshopt --simplify true --simplify-ratio 0.5 \
       --simplify-error 0.0005 --flatten true --join true
   (il modello del pacchetto TO-247 orizzontale e dello shunt WSK2512 non sono nella libreria 3D di KiCad:
   lo shunt e' sostituito da un 2512 normale, i MOSFET sono disegnati qui sotto)
2) Parte meccanica (questo script, serve trimesh): MOSFET TO-247 sotto la scheda, spreader di rame 80x70x6 mm,
   pad isolante, dissipatore e ventola. Spreader e pad dal README del progetto; dissipatore e ventola indicativi.
Coordinate glTF (metri, Y in alto): x = (X_pcb - 135) mm, z = (Y_pcb - 102,5) mm, y = altezza dal lato inferiore della scheda."""
import os, sys, numpy as np, trimesh
OUT = sys.argv[1] if len(sys.argv) > 1 else "."
mm = 1e-3
def box(x0, x1, y0, y1, h0, h1):     # coordinate della scheda in mm, altezza in mm
    b = trimesh.creation.box(extents=[(x1 - x0) * mm, (h1 - h0) * mm, (y1 - y0) * mm])
    b.apply_translation([((x0 + x1) / 2 - 135) * mm, (h0 + h1) / 2 * mm, ((y0 + y1) / 2 - 102.5) * mm]); return b
def cyl(X, Y, r, h0, h1, sections=48):
    c = trimesh.creation.cylinder(radius=r * mm, height=(h1 - h0) * mm, sections=sections)
    c.apply_transform(trimesh.transformations.rotation_matrix(np.pi / 2, [1, 0, 0]))
    c.apply_translation([(X - 135) * mm, (h0 + h1) / 2 * mm, (Y - 102.5) * mm]); return c
def save(name, meshes): trimesh.util.concatenate(meshes).export(os.path.join(OUT, name + ".glb"))
# MOSFET: corpo del footprint TO-247 orizzontale (x -2,5..13,4, y -5,08..-26,03 locali), Q3/Q4 a 0°, Q1/Q2 a 180°
Q = [(94.55, 130, 0), (118.55, 130, 0), (105.45, 74, 180), (129.45, 74, 180)]
body, tabs, leads = [], [], []
for X, Y, r in Q:
    s = 1 if r == 0 else -1
    x0, x1 = sorted([X + s * -2.5, X + s * 13.4]); y0, y1 = sorted([Y + s * -5.08, Y + s * -26.03])
    body.append(box(x0, x1, y0, y1, -7.6, -2.8)); tabs.append(box(x0 + 0.3, x1 - 0.3, y0 + 0.2, y1 - 0.2, -8.4, -7.6))
    for k in range(3):
        px = X + s * 5.45 * k; ya, yb = sorted([Y, Y + s * -5.08])
        leads.append(box(px - 0.6, px + 0.6, ya, yb, -5.6, -5.0)); leads.append(box(px - 0.6, px + 0.6, Y - 0.3, Y + 0.3, -5.6, 1.6))
save("mosfet", body); save("mosfet_tab", tabs + leads)
save("spreader", [box(72, 152, 67, 137, -14.4, -8.4)])
save("pad", [box(72, 152, 67, 137, -14.9, -14.4)])
fins = [box(70, 154, 60 + i * 4.2, 60 + i * 4.2 + 1.2, -50.9, -20.9) for i in range(21)]
save("cooler", [box(70, 154, 60, 144, -20.9, -14.9)] + fins)
fan = [box(66, 158, 56, 148, -76, -73), box(66, 158, 56, 148, -54, -51)]
for cx, cy in [(68.5, 58.5), (155.5, 58.5), (68.5, 145.5), (155.5, 145.5)]: fan.append(box(cx - 2.5, cx + 2.5, cy - 2.5, cy + 2.5, -76, -51))
fan.append(cyl(112, 102, 19, -74, -53))
for a in np.linspace(0, 2 * np.pi, 7)[:-1]:
    b = trimesh.creation.box(extents=[24 * mm, 2 * mm, 9 * mm]); b.apply_transform(trimesh.transformations.rotation_matrix(a, [0, 1, 0]))
    b.apply_translation([(112 - 135 + 31 * np.cos(a)) * mm, -63.5 * mm, (102 - 102.5 - 31 * np.sin(a)) * mm]); fan.append(b)
save("fan", fan)
print("ok", sorted(os.listdir(OUT)))
