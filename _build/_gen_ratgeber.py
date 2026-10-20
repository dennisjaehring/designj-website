#!/usr/bin/env python3
# Generator fuer den Ratgeber: /ratgeber (Uebersicht) + /ratgeber-<slug> (Artikel).
# Basis-Chrome (Head/Nav/Footer) aus marketing-auslagern.html geklont, <main> ersetzt.
import re, pathlib
ROOT = pathlib.Path(__file__).resolve().parent.parent
SKEL = (ROOT / "_build" / "_skeleton.html").read_text(encoding="utf-8")

BRD = ' <br class="br--desktop">'            # desktop-only Umbruch mit Leerzeichen
CK = ('<svg class="mk" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
      'stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round">'
      '<path d="M5 13l4 4L19 7"/></svg>')

def hb(s): return s.replace("<br>", BRD)

# Themenbild pro Kategorie (vorhandene Leistungs-Bilder) – Artikel-Hero.
CAT_IMG = {
    "Marketing": "leistung_marketing",
    "Branding": "leistung_branding",
    "Webdesign": "leistung_web",
    "Social Media": "leistung_social",
    "Print": "leistung_print",
}
def hero_img(a):
    return a.get("hero_img") or CAT_IMG.get(a["cat"], "dennis_spotlight")

SIM_CARDS = 0   # Vorschau: so viele Karten auf der Uebersicht zeigen (0 = nur published)

# Filter-Pills: Reihenfolge + kurze Pill-Labels (Karte zeigt die volle Kategorie)
CAT_ORDER = ["Branding", "Webdesign", "Print", "Social Media", "Marketing", "Sport & Vereine", "Handwerk"]
CAT_PILL = {"Social Media": "Social", "Sport & Vereine": "Sport", "Handwerk": "Handwerk"}

def display_name(a):
    return (a.get("h1","").replace("<br>", " ").strip() or a["title"])

# ---------- Artikel-Main ----------
def build_article_main(a):
    blocks = []
    for h2, paras in a["blocks"]:
        blocks.append(f'      <h2>{hb(h2)}</h2>')
        for p in paras:
            blocks.append(f'      <p>{hb(p)}</p>')
    body = "\n".join(blocks)
    keys = "\n".join(f'          <li>{CK}{k}</li>' for k in a["key"])
    return f'''<main class="kampagne">

<section class="kmp-hero">
  <div class="container kmp-hero__grid">
    <div class="reveal">
      <span class="eyebrow">{a["eyebrow"]}</span>
      <h1 class="seo-h1">{hb(a["h1"])}</h1>
      <p class="rg-meta">Lesezeit {a["read"]} <span class="rg-dot">·</span> <a href="{a["service_href"]}">{a["service_label"]}</a></p>
      <p class="lead" style="max-width:none">{hb(a["lead"])}</p>
    </div>
    <div class="kmp-hero__media reveal" data-delay="120">
      <img class="rg-hero__img" src="images/{hero_img(a)}.webp" alt="{a["service_label"]} – Beispiel von DESIGNJ" style="border-radius:var(--radius)">
    </div>
  </div>
</section>

<section class="section rg-section">
  <div class="container">
    <article class="rg-prose reveal">
{body}
      <aside class="rg-key">
        <h3>Kurz gesagt</h3>
        <ul>
{keys}
        </ul>
      </aside>
    </article>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="rg-cta reveal">
      <h2>{hb(a["cta_h2"])}</h2>
      <p class="lead">{hb(a["cta_lead"])}</p>
      <a href="{a["service_href"]}" class="btn btn--accent btn--lg"><span class="chev">»</span> Mehr zu {a["service_label"]}</a>
      <a href="/ratgeber" class="btn btn--ghost btn--lg">Zurück zum Ratgeber</a>
    </div>
  </div>
</section>

</main>'''

# ---------- Uebersicht-Main ----------
def build_overview_main(ov, articles):
    show = articles[:SIM_CARDS] if SIM_CARDS else [a for a in articles if a.get("published")]
    cards = []
    for a in show:
        cards.append(
f'''      <a class="rg-card reveal" href="/{a["slug"]}" data-cat="{a["cat"]}">
        <span class="rg-card__cat">{a["cat"]}</span>
        <h2 class="rg-card__title">{display_name(a)}</h2>
        <p class="rg-card__teaser">{a["teaser"]}</p>
        <span class="rg-card__more"><span class="chev">»</span> Weiterlesen</span>
      </a>''')
    cards_html = "\n".join(cards)
    soon = [a for a in articles if a not in show]
    soon_html = ""
    if soon:
        items = " · ".join(a["title"] for a in soon)
        soon_html = f'''
    <p class="rg-soon reveal"><span class="rg-soon__label">In Vorbereitung:</span> {items}</p>'''
    present = [c for c in CAT_ORDER if any(a["cat"] == c for a in show)]
    pills = ['      <button class="is-active" data-filter="all">Alle</button>']
    pills += [f'      <button data-filter="{c}">{CAT_PILL.get(c, c)}</button>' for c in present]
    pills_html = "\n".join(pills)
    return f'''<main class="kampagne">

<section class="kmp-hero">
  <div class="container kmp-hero__grid">
    <div class="reveal">
      <span class="eyebrow">{ov["eyebrow"]}</span>
      <h1 class="seo-h1">{hb(ov["h1"])}</h1>
      <p class="lead" style="max-width:none">{hb(ov["lead"])}</p>
    </div>
    <div class="kmp-hero__media reveal" data-delay="120">
      <img src="images/dennis_spotlight.webp" alt="Dennis Jähring – DESIGNJ, dein Ansprechpartner" style="border-radius:var(--radius)">
    </div>
  </div>
</section>

<section class="section rg-section">
  <div class="container">
    <div class="rg-filter reveal" role="tablist" aria-label="Nach Thema filtern">
{pills_html}
    </div>
    <div class="rg-cards">
{cards_html}
    </div>{soon_html}
  </div>
</section>

<script>
(function(){{
  var pills = document.querySelectorAll('.rg-filter button');
  var cards = document.querySelectorAll('.rg-card');
  pills.forEach(function(b){{
    b.addEventListener('click', function(){{
      var f = b.getAttribute('data-filter');
      pills.forEach(function(p){{ p.classList.toggle('is-active', p === b); }});
      cards.forEach(function(c){{
        c.style.display = (f === 'all' || c.getAttribute('data-cat') === f) ? '' : 'none';
      }});
    }});
  }});
}})();
</script>

</main>'''

# ---------- Seite schreiben (Chrome klonen + ersetzen) ----------
def write_page(slug, title, desc, main_html, schema_json):
    s = SKEL
    s = s.replace("<title>Marketing auslagern Weiden | Werbeagentur DESIGNJ</title>", f"<title>{title}</title>")
    s = re.sub(r'<meta name="description" content="[^"]*">', f'<meta name="description" content="{desc}">', s, count=1)
    s = s.replace('<link rel="canonical" href="https://www.designj.de/marketing-auslagern">', f'<link rel="canonical" href="https://www.designj.de/{slug}">')
    s = s.replace('<meta property="og:title" content="Marketing auslagern Weiden | Werbeagentur DESIGNJ">', f'<meta property="og:title" content="{title}">')
    s = re.sub(r'<meta property="og:description" content="[^"]*">', f'<meta property="og:description" content="{desc}">', s, count=1)
    s = s.replace('<meta property="og:url" content="https://www.designj.de/marketing-auslagern">', f'<meta property="og:url" content="https://www.designj.de/{slug}">')
    # FAQ-Schema-Block durch unser Schema (oder leer) ersetzen
    repl = ('<!-- Schema -->\n  <script type="application/ld+json">\n  ' + schema_json + '\n  </script>') if schema_json else '<!-- Schema -->'
    s = re.sub(r'<!-- FAQ-Schema \(Rich Results\) -->\s*<script type="application/ld\+json">.*?</script>', lambda m: repl, s, count=1, flags=re.S)
    s = s.replace('<body class="kampagne-bedarf">', '<body class="kampagne">')
    s = re.sub(r'<main class="kampagne">.*?</main>', lambda m: main_html, s, count=1, flags=re.S)
    (ROOT / f"{slug}.html").write_text(s, encoding="utf-8")

def article_schema(a):
    name = display_name(a).replace('"', "'")
    desc = a["desc"].replace('"', "'")
    return ('{\n'
            '    "@context": "https://schema.org",\n'
            '    "@type": "BlogPosting",\n'
            f'    "headline": "{name}",\n'
            f'    "description": "{desc}",\n'
            '    "author": {"@type": "Person", "name": "Dennis Jähring"},\n'
            '    "publisher": {"@type": "Organization", "name": "DESIGNJ", "logo": {"@type": "ImageObject", "url": "https://www.designj.de/designj_logo.svg"}},\n'
            f'    "mainEntityOfPage": "https://www.designj.de/{a["slug"]}"\n'
            '  }')

# ---------------- DATEN ----------------
from _ratgeber_data import OVERVIEW, ARTICLES  # noqa

# Artikel
for a in ARTICLES:
    if not a.get("published"):
        continue
    write_page(a["slug"], a["title"], a["desc"], build_article_main(a), article_schema(a))
    print("gebaut:", a["slug"] + ".html")

# Uebersicht
write_page("ratgeber", OVERVIEW["title"], OVERVIEW["desc"], build_overview_main(OVERVIEW, ARTICLES), "")
print("gebaut: ratgeber.html")
