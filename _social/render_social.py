#!/usr/bin/env python3
# DESIGNJ Social Render-Pipeline (PIL-Port des HTML-Renderers aus SOCIAL-SETUP.md)
import os, sys
import numpy as np
from PIL import Image, ImageDraw, ImageFont

# Repo-Wurzel = Elternordner dieser Datei (_social/)
WEB  = os.environ.get('DJ_WEB',  os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
GDIR = os.path.join(WEB, '_social-grundgeruest') + '/'
# Quellbilder: Drive `Social Media/_Social-Bilder`, Fallback = lokale Kopie im Repo
PDIR = os.environ.get('DJ_BILDER', os.path.join(WEB, '_social-bilder')) + '/'
OUT  = os.environ.get('DJ_OUT', '/tmp/out')          # Ziel: Drive `Social Media/_FERTIG`
TTF  = '/tmp/ttf/inter-%d.ttf'
os.makedirs(OUT, exist_ok=True)

UPEM, ASC, DESC = 2048, 1984, -494

# Inter in fonts/ ist eine Variable Font (wght 100-900); alle inter-*.woff2 sind
# byte-identisch. Statische Schnitte deshalb selbst instanziieren.
def build_fonts():
    from fontTools.ttLib import TTFont
    from fontTools.varLib import instancer
    src = f'{WEB}/fonts/inter-400-latin.woff2'
    os.makedirs('/tmp/ttf', exist_ok=True)
    for w in (400, 500, 700, 800, 900):
        out = TTF % w
        if os.path.exists(out): continue
        inst = instancer.instantiateVariableFont(TTFont(src), {'wght': w}, inplace=False)
        inst.flavor = None
        inst.save(out)

def font(w, size): return ImageFont.truetype(TTF % w, size)
def ascent(size):  return ASC / UPEM * size
def content_h(size): return (ASC - DESC) / UPEM * size

def baseline(box_top, size, line_height=None):
    """CSS-Boxtop -> PIL-Baseline (half-leading Modell)."""
    lh = content_h(size) if line_height is None else line_height
    return box_top + (lh - content_h(size)) / 2 + ascent(size)

def draw_ls(d, x, y_base, text, fnt, fill, ls=0.0):
    """Zeichnet Text zeichenweise mit letter-spacing. y_base = Baseline."""
    for ch in text:
        d.text((x, y_base), ch, font=fnt, fill=fill, anchor='ls')
        x += fnt.getlength(ch) + ls
    return x

def text_w(text, fnt, ls=0.0):
    return sum(fnt.getlength(c) for c in text) + ls * len(text)

# --- Headline-Umbruch (identisch zu SOCIAL-SETUP.md) ---
def split_even(words, n):
    best, bestscore, L = None, 1e9, len(words)
    if n == 2:
        for i in range(1, L):
            lines = [' '.join(words[:i]), ' '.join(words[i:])]
            sc = abs(len(lines[0]) - len(lines[1]))
            if sc < bestscore: bestscore, best = sc, lines
    elif n == 3:
        for i in range(1, L - 1):
            for j in range(i + 1, L):
                lines = [' '.join(words[:i]), ' '.join(words[i:j]), ' '.join(words[j:])]
                sc = max(len(x) for x in lines) - min(len(x) for x in lines)
                if sc < bestscore: bestscore, best = sc, lines
    return best

def balanced(text, charmax=24):
    w = text.split()
    if len(w) <= 1: return [text]
    two = split_even(w, 2)
    if two and max(len(l) for l in two) <= charmax: return two
    three = split_even(w, 3)
    return three if three else two

# --- Nischen: Farbe + Grundgeruest ---
NICHE = {
    'Handwerk':    ('#FF8A2B', '2026-07_SocialMedia_2.jpg'),
    'Sport':       ('#3FBF6A', '2026-07_SocialMedia_3.jpg'),
    'Auslagern':   ('#3D6BF0', '2026-07_SocialMedia_4.jpg'),
    'Immobilien':  ('#28AEE6', '2026-07_SocialMedia_5.jpg'),
    'Kanzlei':     ('#A3283F', '2026-07_SocialMedia_6.jpg'),
    'Praxis':      ('#1FC4A8', '2026-07_SocialMedia_7.jpg'),
}

# ID, Datum, Kicker, Headline  (aus SOCIAL-CONTENTPLAN.md + SOCIAL-SETUP.md)
POSTS = [
 ('Handwerk_01',   '2026-07-21', 'STEHT MONATELANG. SIEHT JEDER.',    'Macht dein Bauzaun schon Werbung?'),
 ('Handwerk_02',   '2026-08-11', 'DAS ERSTE, WAS MAN AM BAU SIEHT.',  'Wer baut hier eigentlich?'),
 ('Handwerk_03',   '2026-09-01', 'FÄHRT TÄGLICH. WIRBT TÄGLICH.',     'Wirbt dein Auto schon für dich?'),
 ('Handwerk_04',   '2026-09-22', 'DEIN TEAM IST DEINE VISITENKARTE.', 'Trägt dein Team schon deinen Namen?'),
 ('Sport_01',      '2026-07-23', 'JEDES SPIEL. JEDES AUGE. DRAUF.',   'Wer wirbt an eurer Bande?'),
 ('Sport_02',      '2026-08-13', 'EIN TEAM. EIN AUFTRITT.',           'Sieht euer Team schon nach Team aus?'),
 ('Sport_03',      '2026-09-03', 'DER VEREIN LEBT AUCH ONLINE.',      'Wie aktiv ist euer Verein online?'),
 ('Sport_04',      '2026-09-24', 'GROSS. LAUT. NICHT ZU ÜBERSEHEN.',  'Fällt euer Event schon auf?'),
 ('Auslagern_01',  '2026-07-28', 'MARKETING-STELLE OFFEN?',           'Muss es gleich eine feste Stelle sein?'),
 ('Auslagern_02',  '2026-08-18', 'KEINE ZEIT. KEIN TEAM.',            'Wer kümmert sich um deine Website?'),
 ('Auslagern_03',  '2026-09-08', 'JEDER SAGT „MACHEN WIR MAL".',      'Wer macht euer Social Media wirklich?'),
 ('Auslagern_04',  '2026-09-29', 'VON KLEIN BIS RIESENGROSS.',        'Und wer macht den Rest auch noch?'),
 ('Immobilien_01', '2026-07-30', 'DER ERSTE EINDRUCK VERKAUFT MIT.',  'Verkauft dein Exposé schon mit?'),
 ('Immobilien_02', '2026-08-20', 'KÄUFER SUCHEN ZUERST ONLINE.',      'Findet man deine Objekte im Netz?'),
 ('Immobilien_03', '2026-09-10', 'OBJEKTE VERKAUFEN ÜBER BILDER.',    'Zeigst du Objekte schon als Reel?'),
 ('Immobilien_04', '2026-10-01', 'DAS SCHILD VERKAUFT VOR ORT.',      'Weiß die Straße, dass du verkaufst?'),
 ('Kanzlei_01',    '2026-08-04', 'MANDANTEN PRÜFEN DICH ONLINE.',     'Wirkt deine Kanzlei online seriös?'),
 ('Kanzlei_02',    '2026-08-25', 'SERIOSITÄT STECKT IM DETAIL.',      'Passt deine Ausstattung zur Kanzlei?'),
 ('Kanzlei_03',    '2026-09-15', 'GUTE LEUTE SIND RAR.',              'Findet dein Nachwuchs zu dir?'),
 ('Kanzlei_04',    '2026-10-06', 'MANCHE MANDATE BRAUCHEN MEHR.',     'Erzählt deine Kanzlei ihre Geschichte?'),
 ('Praxis_01',     '2026-08-06', 'PATIENTEN GOOGELN ZUERST.',         'Finden Patienten deine Praxis online?'),
 ('Praxis_02',     '2026-08-27', 'DER WEG IST TEIL DES EINDRUCKS.',   'Findet sich jeder in deiner Praxis zurecht?'),
 ('Praxis_03',     '2026-09-17', 'DER EINGANG EMPFÄNGT ZUERST.',      'Lädt dein Eingang zum Reinkommen ein?'),
 ('Praxis_04',     '2026-10-08', 'AUFKLÄRUNG SCHAFFT VERTRAUEN.',     'Bleibt deine Praxis mit Patienten in Kontakt?'),
]

# --- Grundgeruest-Cache: Magenta -> Schwarz ---
_bases = {}
def base_for(niche):
    if niche not in _bases:
        a = np.array(Image.open(GDIR + NICHE[niche][1]).convert('RGB'))
        R, G, B = a[:, :, 0].astype(int), a[:, :, 1].astype(int), a[:, :, 2].astype(int)
        a[(R > 140) & (G < 115) & (B > 140)] = (0, 0, 0)
        _bases[niche] = Image.fromarray(a)
    return _bases[niche].copy()

# --- Foto: object-fit cover auf 880x590, radius 26 ---
def photo(pid, w=880, h=590, r=26):
    im = Image.open(PDIR + pid + '.webp').convert('RGB')
    sw, sh = im.size
    scale = max(w / sw, h / sh)
    nw, nh = int(round(sw * scale)), int(round(sh * scale))
    im = im.resize((nw, nh), Image.LANCZOS)
    im = im.crop(((nw - w) // 2, (nh - h) // 2, (nw - w) // 2 + w, (nh - h) // 2 + h))
    S = 4
    mask = Image.new('L', (w * S, h * S), 0)
    ImageDraw.Draw(mask).rounded_rectangle([0, 0, w * S - 1, h * S - 1], radius=r * S, fill=255)
    return im, mask.resize((w, h), Image.LANCZOS)

def render(pid, datum, kicker, headline):
    niche = pid.rsplit('_', 1)[0]
    acc = NICHE[niche][0]
    img = base_for(niche)
    ph, mask = photo(pid)
    img.paste(ph, (100, 240), mask)

    d = ImageDraw.Draw(img)
    # Kicker: top 884, 30px/400, uppercase, ls +1, Nischenfarbe
    fk = font(400, 30)
    draw_ls(d, 100, baseline(884, 30), kicker.upper(), fk, acc, ls=1.0)

    # Headline: top 930, 70px/lh 80, 800, weiss, ls -1
    fh = font(800, 70)
    lines = balanced(headline)
    for i, ln in enumerate(lines):
        draw_ls(d, 100, baseline(930, 70, 80) + i * 80, ln, fh, '#FFFFFF', ls=-1.0)

    # CTA: top 1200, 30px -> ">>" acc/700, "Mehr dazu: " 400, "designj.de" 500
    yb = baseline(1200, 30)
    x = draw_ls(d, 100, yb, '>>', font(700, 30), acc)
    x += 6
    x = draw_ls(d, x, yb, 'Mehr dazu: ', font(400, 30), '#FFFFFF')
    draw_ls(d, x, yb, 'designj.de', font(700, 30), '#FFFFFF')

    name = f'{datum}_{pid}.png'
    img.save(os.path.join(OUT, name))
    return name, ' / '.join(lines)

if __name__ == '__main__':
    build_fonts()
    only = sys.argv[1] if len(sys.argv) > 1 else None
    for pid, datum, kicker, headline in POSTS:
        if only and pid != only: continue
        n, h = render(pid, datum, kicker, headline)
        print(n, '::', h)
