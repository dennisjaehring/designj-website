#!/usr/bin/env python3
"""Bettet css/fonts.css + css/style.css als EIN inline <style> in jede HTML-Seite ein
und entfernt die render-blockierenden <link rel="stylesheet">.

css/style.css bleibt die EDITIERBARE Quelle. Nach jeder CSS-Aenderung dieses Script
erneut laufen lassen:  python3 _build/inline_css.py

Idempotent: erkennt einen bereits eingebetteten Block (<style id="inline-css">) und
ersetzt dessen Inhalt statt zu duplizieren.
"""
import re, glob, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def read(p):
    with open(os.path.join(ROOT, p), encoding="utf-8") as f:
        return f.read()

fonts = read("css/fonts.css").replace("../fonts/", "/fonts/")
style = read("css/style.css")

inlined = f"/* fonts.css (inline) */\n{fonts}\n/* style.css (inline) */\n{style}"
block = ('  <!-- CSS inline eingebettet – kein Render-Blocking (Quelle: css/style.css, '
         'Build: _build/inline_css.py) -->\n'
         '  <style id="inline-css">\n' + inlined + '\n  </style>')

# Kampagnen-CSS (nur auf 6 Kampagnen-/SEO-Seiten) ebenfalls inline
kmp = read("css/kampagnen.css")
kmp_block = ('  <!-- Kampagnen-CSS inline (Quelle: css/kampagnen.css) -->\n'
             '  <style id="inline-css-kmp">\n/* kampagnen.css (inline) */\n' + kmp + '\n  </style>')

existing = re.compile(r'  <!-- CSS inline eingebettet.*?-->\n  <style id="inline-css">.*?</style>', re.DOTALL)
existing_kmp = re.compile(r'  <!-- Kampagnen-CSS inline.*?-->\n  <style id="inline-css-kmp">.*?</style>', re.DOTALL)

changed = 0
for path in sorted(glob.glob(os.path.join(ROOT, "*.html"))):
    html = open(path, encoding="utf-8").read()
    orig = html
    if 'id="inline-css"' in html:
        # Re-Inline: bestehenden Block ersetzen
        html = existing.sub(lambda m: block, html)
    else:
        # Erst-Inline: fonts-Link -> Block, style-Link (+ vorangestellter Zeilenumbruch) raus
        html = html.replace('  <link rel="stylesheet" href="css/fonts.css">', block)
        html = html.replace('\n\n  <link rel="stylesheet" href="css/style.css">', '')
        html = html.replace('\n  <link rel="stylesheet" href="css/style.css">', '')
    # Kampagnen-CSS (falls die Seite es referenziert)
    if 'id="inline-css-kmp"' in html:
        html = existing_kmp.sub(lambda m: kmp_block, html)
    elif 'css/kampagnen.css' in html:
        html = html.replace('  <link rel="stylesheet" href="css/kampagnen.css">', kmp_block)
    if html != orig:
        open(path, "w", encoding="utf-8").write(html)
        changed += 1

print(f"{changed} Seiten aktualisiert (CSS: {len(inlined)/1024:.1f} KB inline).")
