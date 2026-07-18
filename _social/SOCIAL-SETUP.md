# DESIGNJ – Social Render-Pipeline & Ablage (Setup)

> Wie die fertigen Social-Posts automatisch entstehen. Ergänzt `SOCIAL-SYSTEM.md` (Regeln) und den Content-Plan (Redaktionsplan).
> Stand: 2026-07-18. Diese Datei ist die **aktuelle** Fassung – ersetzt die ältere Version im Projekt-Wissen.

## Ordner

**Drive** (`… / DESIGNJ / Social Media /`):

- `_Social-Bilder/` = **Input**: Quell-/Firefly-Bilder, benannt `<ID>.webp` (z. B. `Handwerk_01.webp`).
- `_FERTIG/` = **Output**: fertige 1080×1350-PNGs.
- `_Contentplan/` = Redaktionsplan als `YYYY-MM-DD_Content-Plan.xlsx`; ältere Stände wandern nach `_Contentplan/alt/`.

**Repo** (`Projekte/designj-website/`):

- `_social/render_social.py` = **der Renderer** (diese Pipeline).
- `_social/SOCIAL-SETUP.md` = diese Doku.
- `_social-grundgeruest/` = 7 Grundgerüst-JPGs. Nische an Rahmenfarbe: Allgemein=`…_1`, Handwerk=`…_2`, Sport=`…_3`, Auslagern=`…_4`, Immobilien=`…_5`, Kanzlei=`…_6`, Praxis=`…_7`.
- `fonts/` = Inter (siehe Font-Hinweis unten).

`*.py` und `*.md` stehen in `.assetsignore` – nichts davon wird öffentlich ausgeliefert.

## Computer-Modus Pflicht für Drive

Aus der **Cloud** ist der Drive-Stream-Ordner nicht beschreibbar. Für direkte Ablage in `_FERTIG`: Cowork **„On your computer"**, Ordner **`Social Media`** + **`designj-website`** verbinden. Cloud-Fallback: Ausgabe als ZIP.

## Renderer

**PIL statt Headless-Chromium.** Die ursprüngliche Referenz-Implementierung rendert HTML per Headless-Chromium. Das lässt sich in der Cowork-Sandbox **nicht** ausführen (fehlende Systembibliotheken wie `libXdamage`, keine Root-Rechte zum Nachinstallieren). `render_social.py` baut das Layout deshalb direkt mit Pillow – identische Koordinaten, identische Schrift, identischer Zeilenumbruch.

Nachgebildete CSS-Details:

- **Baselines** über das Half-Leading-Modell: `baseline = box_top + (line_height − (asc+desc)) / 2 + asc`, mit Inter-Metriken `upem 2048 / asc 1984 / desc −494`. Ohne `line-height` gilt `normal` = `(asc+desc)/upem ≈ 1.21 × font-size`.
- **letter-spacing** durch zeichenweises Zeichnen (Kicker `+1`, Headline `−1`).
- **object-fit: cover** durch Scale-to-fill + Center-Crop.
- **border-radius 26** über eine 4× übersampelte Maske (saubere Kanten).

Aufruf:

```bash
# alle 24 Posts nach _FERTIG
DJ_BILDER="…/Social Media/_Social-Bilder" \
DJ_OUT="…/Social Media/_FERTIG" \
python3 _social/render_social.py

# nur ein Post
python3 _social/render_social.py Handwerk_01
```

Abhängigkeiten: `pillow`, `numpy`, `fonttools`, `brotli`.

## ⚠ Font-Hinweis (wichtig)

Alle zwölf Dateien in `fonts/` (`inter-400-latin.woff2` … `inter-900-latin.woff2`) sind **byte-identisch** – es ist in Wahrheit **eine Variable Font** mit Achse `wght 100–900`. Wer sie als statische Schnitte behandelt, bekommt überall **Regular**; genau daran ist die Headline zuerst nicht fett geworden.

`render_social.py` instanziiert die Schnitte deshalb selbst (`fontTools.varLib.instancer`) nach `/tmp/ttf/inter-<wght>.ttf`. Kontrolle: die Breite von „Macht dein Bauzaun" bei 70 px muss je Gewicht steigen (400 → 675,4 px · 800 → 704,7 px · 900 → 714,0 px). Sind alle Werte gleich, greift die Instanziierung nicht.

## Render-Regeln

- Canvas 1080×1350. Grundgerüst = Hintergrund. **Magenta `#FF00FF` → Bildfeld** automatisch erkennen (x 100–979 / y 240–830), Magenta auf Schwarz, Foto mit Radius 26 einsetzen (cover, 880×590 ab x100/y240).
- **Kicker** top 884, left 100: 30 px, Inter 400, UPPERCASE, letter-spacing 1, Farbe = Nischen-HEX.
- **Headline** top 930, left 100, width 900: 70 px, line-height 80, Inter **800**, weiß, letter-spacing −1. **Immer 2 Zeilen ausgewogen** (Wörter gleich verteilen; wenn Zeile > 24 Zeichen → 3 Zeilen).
- **CTA** top 1200, left 100: 30 px. `>>` Nischen-HEX/700 · „Mehr dazu:" Inter 400 · **„designj.de" Inter 700** (Stand 18.07.2026 von 500 hochgezogen – soll sich klar von „Mehr dazu:" absetzen).
- Rahmen/Bar/Icon kommen aus dem Grundgerüst.
- **Dateiname** `YYYY-MM-DD_Kategorie_NN.png` (Datum aus dem Content-Plan, Di+Do-Rhythmus ab 2026-07-21).

## Nischenfarben

Handwerk `#FF8A2B` · Sport `#3FBF6A` · Auslagern `#3D6BF0` · Immobilien `#28AEE6` · Kanzlei `#A3283F` · Praxis `#1FC4A8` · Allgemein Weiß.

## Qualitätskontrolle nach dem Batch

1. Anzahl + Maße: 24 Dateien, alle exakt 1080×1350.
2. **Textüberlauf**: keine Headline-Zeile breiter als 900 px, kein Kicker breiter als 880 px (das Skript kann das vorab durchrechnen).
3. **Magenta-Reste**: Restpixel im Bildfeld sind i. d. R. echte Bildinhalte (gedämpfte Rosatöne wie 172/104/148), kein Grundgerüst-Fehler. Nur kräftiges reines Magenta ist ein Alarmzeichen.
4. Stichprobe je Nische visuell prüfen.

## Status / offen

- Erledigt 18.07.2026: alle **24 Nischen-Posts** gerendert und in `_FERTIG` abgelegt.
- Offen: **9 Saison-/Anlass-Posts** (Motive fehlen noch) · 1:1- und 9:16-Ableitungen · 4 reservierte Farben zuordnen.
- Bekannter Textfehler: Kicker `Auslagern_03` endet mit geradem Zoll-Zeichen `MAL".` statt typografisch `MAL“.`
