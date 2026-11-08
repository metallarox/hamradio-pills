"""Modelli 3D per il visualizzatore della pagina Fluke Hydra Monitor.

python3 tools/progetti/hydra_plate_3d.py /percorso/fluke_hydra_monitor   (serve: pip install cadquery)

Usa il modello parametrico hardware/gpib_plate/hydra_wemos_plate.FCMacro del repository del progetto
e scrive in progetti/fluke-hydra-monitor/3d/ un STL per ogni parte, nelle coordinate di montaggio:
origine al centro della feritoia GPIB sulla superficie del pannello, +Z verso l'esterno."""
import os, sys, json
SRC = sys.argv[1] if len(sys.argv) > 1 else os.path.expanduser("~/fluke_hydra_monitor")
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "progetti", "fluke-hydra-monitor", "3d")
os.makedirs(OUT, exist_ok=True)
m = {}
macro = os.path.join(SRC, "hardware", "gpib_plate", "hydra_wemos_plate.FCMacro")
exec(compile(open(macro).read(), "plate", "exec"), m)
import cadquery as cq
P = dict(m["P"]); d = m["derived"](P)
B, R, U = m["box"], m["crect"], m["union"]
plate, cover = m["make_plate"](P), m["make_cover"](P)
zb = d["zb"]
# segnaposto di Wemos e MAX3232, come in preview/make_previews.py del progetto
wemos = U([R(0, 0, P["wemos_l"], P["wemos_w"], zb, zb + 1.0, 0.5),
           B(P["wemos_l"] / 2 - 24, -8, zb + 1, P["wemos_l"] / 2, 8, zb + 4.2)])
z0 = -P["tongue_depth"] + P["tongue_end"] + 0.2
module = U([B(-P["module_l"] / 2, 0.2, z0, P["module_l"] / 2, 1.2, z0 + P["module_w"]),
            B(-5, -1.55, z0 + 3.5, 5, 0.2, z0 + 9.5)])
# un pezzo di pannello posteriore con la feritoia GPIB e i due fori
pan = B(-48, -30, -P["panel_t"], 48, 30, 0)
pan = m["cut"](pan, [R(0, 0, P["slot_len"], P["slot_w"], -P["panel_t"] - 1, 1, P["slot_r"]),
                     m["cyl"](-d["hx"], 0, -P["panel_t"] - 1, 1, 3.2), m["cyl"](d["hx"], 0, -P["panel_t"] - 1, 1, 3.2)])
parts = {"panel": pan, "plate": plate, "max3232": module, "wemos": wemos, "cover": cover}
info = {}
for name, shape in parts.items():
    path = os.path.join(OUT, name + ".stl")
    shape.exportStl(path, tolerance=0.05 if name in ("plate", "cover") else 0.1, angularTolerance=0.3)
    info[name] = os.path.getsize(path)
json.dump({"z_cover_top": round(d["z_cover_top"], 2), "sizes": info}, open(os.path.join(OUT, "info.json"), "w"), indent=1)
print(info, "spessore fuori dal pannello: %.1f mm" % d["z_cover_top"])
