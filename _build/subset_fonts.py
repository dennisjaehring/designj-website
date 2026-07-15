#!/usr/bin/env python3
"""Subsettet die Inter-Latin-Schnitte auf die tatsaechlich genutzten Zeichen
(ASCII + Latin-1 + Typografie), behaelt Kerning/Ligaturen -> identisches Aussehen,
aber ~30% kleiner. Originale liegen in _build/fonts-orig/ (nicht deployt).

Aufruf:  python3 _build/subset_fonts.py
Voraussetzung:  pip3 install fonttools brotli
"""
import os, subprocess, glob, shutil

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ORIG = os.path.join(ROOT, "_build", "fonts-orig")
os.makedirs(ORIG, exist_ok=True)

UNI = ("U+0020-00FF,U+0152-0153,U+2013,U+2014,U+2018,U+2019,U+201A,U+201C,U+201D,"
       "U+201E,U+2020,U+2021,U+2022,U+2026,U+2030,U+2039,U+203A,U+20AC,U+2122,"
       "U+2190,U+2192,U+2212,U+25B4,U+25BE,U+25B8")
FEATURES = "kern,liga,clig,calt,ccmp,locl,mark,mkmk"

for w in (400, 500, 600, 700, 800, 900):
    live = os.path.join(ROOT, "fonts", f"inter-{w}-latin.woff2")
    backup = os.path.join(ORIG, f"inter-{w}-latin.woff2")
    if not os.path.exists(backup):        # Original einmalig sichern
        shutil.copy(live, backup)
    subprocess.run(["python3", "-m", "fontTools.subset", backup,
                    f"--unicodes={UNI}", f"--layout-features={FEATURES}",
                    "--flavor=woff2", f"--output-file={live}"], check=True)
    print(f"inter-{w}-latin: {os.path.getsize(live)/1024:.1f} KB")
print("fertig.")
