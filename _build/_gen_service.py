#!/usr/bin/env python3
# Einmal-Generator fuer 4 Service-Seiten (Logik wie webdesign.html / Skelett marketing-auslagern.html)
import re, pathlib
ROOT = pathlib.Path(__file__).resolve().parent.parent
SKEL = (ROOT / "_build" / "_skeleton.html").read_text(encoding="utf-8")
CK = '<svg class="mk" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M5 13l4 4L19 7"/></svg>'
R = "images/referenzen/designj_referenz_"

def pack(name, tag, items, feat=False, delay=0):
    badge = '<span class="kmp-pack__badge">Beliebt</span>' if feat else ''
    cls = "kmp-pack kmp-pack--feat" if feat else "kmp-pack"
    d = f' data-delay="{delay}"' if delay else ''
    lis = "\n".join(f'          <li>{CK}{i}</li>' for i in items)
    return f'''      <div class="{cls} reveal"{d}>
        {badge}
        <div class="kmp-pack__name">{name}</div>
        <p class="kmp-pack__tag">{tag}</p>
        <ul class="kmp-pack__list">
{lis}
        </ul>
      </div>'''

def step(t, p, delay=0):
    d = f' data-delay="{delay}"' if delay else ''
    return f'      <div class="kmp-step reveal"{d}><div class="kmp-step__num"></div><h3>{t}</h3><p>{p}</p></div>'

def shot(img, alt, cap, delay=0):
    d = f' data-delay="{delay}"' if delay else ''
    return f'''      <figure class="kmp-shot reveal"{d}>
        <img class="kmp-shot__media" src="{R}{img}.webp" alt="{alt}" loading="lazy">
        <figcaption class="kmp-shot__cap"><span class="chev">»</span> {cap}</figcaption>
      </figure>'''

def faqitem(q, a):
    return f'      <details class="faq__item">\n        <summary>{q}</summary>\n        <p>{a}</p>\n      </details>'

def schema_q(q, a):
    a = a.replace('&amp;', 'und').replace('"', "'")
    return f'      {{ "@type": "Question", "name": "{q}", "acceptedAnswer": {{ "@type": "Answer", "text": "{a}" }} }}'

KONTAKT = '''<section class="section" id="kontakt">
  <div class="container">
    <div class="section-head reveal">
      <span class="eyebrow">Lass uns sprechen</span>
      <h2>{k_h2}</h2>
      <p class="lead">{k_lead}</p>
    </div>
    <div class="contact-grid kmp-contact">
      <div class="reveal contact-aside">
        <h2 class="contact-h2">So erreichst du mich direkt:</h2>
        <a class="contact-map contact-map--link" href="https://www.google.com/maps/dir/?api=1&amp;destination=Hasenweg+34%2C+92699+Irchenrieth" target="_blank" rel="noopener" aria-label="Route zu DESIGNJ in Google Maps planen">
          <img class="contact-map__img" src="images/kontakt_karte.webp" alt="Standort DESIGNJ – Hasenweg 34, 92699 Irchenrieth (Luftbild)" loading="lazy">
          <span class="contact-map__cta">Route planen <span class="arrow">&#8594;</span></span>
        </a>
        <a class="contact-loc" href="https://www.google.com/maps/dir/?api=1&amp;destination=Hasenweg+34%2C+92699+Irchenrieth" target="_blank" rel="noopener">
          <svg class="ico" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M21 10c0 7-9 12-9 12s-9-5-9-12a9 9 0 0118 0z"/><circle cx="12" cy="10" r="3"/></svg>
          <div><span class="contact-loc__addr">Hasenweg 34, 92699 Irchenrieth</span><span class="contact-loc__note">Termine nach Vereinbarung – <br class="br--mobile">auch remote oder bei dir vor Ort</span></div>
        </a>
        <div class="contact-list">
          <a class="contact-row" href="tel:+491702918305"><svg class="ico" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 16.9v3a2 2 0 01-2.2 2 19.8 19.8 0 01-8.6-3 19.5 19.5 0 01-6-6 19.8 19.8 0 01-3-8.6A2 2 0 014.1 2h3a2 2 0 012 1.7c.1 1 .3 1.9.6 2.8a2 2 0 01-.5 2.1L8 9.6a16 16 0 006 6l1-1.2a2 2 0 012.1-.5c.9.3 1.8.5 2.8.6a2 2 0 011.7 2z"/></svg><span><span class="contact-row__label">Telefon</span><br><span class="contact-row__value">+49 170 291 83 05</span></span></a>
          <a class="contact-row" href="https://wa.me/491702918305" target="_blank" rel="noopener"><svg class="ico" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 21l1.6-4.5A8.4 8.4 0 1112 20.4a8.5 8.5 0 01-4.3-1.2z"/><path d="M8.5 8.5c-.3 1 .2 2.3 1.3 3.5s2.5 1.7 3.5 1.4c.5-.2.8-1 .6-1.4l-1.2-.9-.9.6c-.6-.2-1.2-.6-1.6-1.1-.4-.5-.7-.9-.7-1.1l.6-.9-.9-1.2c-.4-.2-1.1.1-1.3.6z"/></svg><span><span class="contact-row__label">WhatsApp</span><br><span class="contact-row__value">Nachricht schreiben</span></span></a>
          <a class="contact-row" href="mailto:info@designj.de"><svg class="ico" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="5" width="18" height="14" rx="2"/><path d="M3 7l9 6 9-6"/></svg><span><span class="contact-row__label">E-Mail</span><br><span class="contact-row__value">info@designj.de</span></span></a>
          <a class="contact-row" href="https://www.instagram.com/designj.de/" target="_blank" rel="noopener"><svg class="ico" viewBox="8 8 32 32" fill="currentColor" aria-hidden="true"><path d="M33.219,9.035H14.815c-3.197,0-5.797,2.6-5.797,5.797v6.125v12.281c0,3.197,2.6,5.797,5.797,5.797h18.404c3.197,0,5.799-2.6,5.799-5.797V20.957v-6.125C39.018,11.634,36.417,9.035,33.219,9.035z M34.883,12.494l0.662-0.004v0.662v4.422l-5.066,0.017l-0.018-5.084L34.883,12.494z M19.737,20.957c0.961-1.33,2.519-2.201,4.281-2.201s3.32,0.871,4.281,2.201c0.625,0.867,1,1.93,1,3.078c0,2.91-2.371,5.279-5.281,5.279c-2.912,0-5.281-2.369-5.281-5.279C18.737,22.886,19.112,21.824,19.737,20.957z M36.096,33.238c0,1.586-1.291,2.875-2.877,2.875H14.815c-1.586,0-2.875-1.289-2.875-2.875V20.957h4.478c-0.387,0.951-0.603,1.99-0.603,3.078c0,4.523,3.68,8.203,8.203,8.203c4.523,0,8.203-3.68,8.203-8.203c0-1.088-0.219-2.127-0.605-3.078h4.48V33.238z"/></svg><span><span class="contact-row__label">Instagram</span><br><span class="contact-row__value">@designj.de</span></span></a>
          <a class="contact-row" href="https://www.linkedin.com/in/dennisjaehring/" target="_blank" rel="noopener"><svg class="ico" viewBox="8 8 32 32" fill="currentColor" aria-hidden="true"><rect x="9.018" y="19.035" width="7" height="20"/><circle cx="12.518" cy="12.535" r="3.5"/><path d="M39.018,28.044c0-5.397-1.164-9.009-7.455-9.009c-3.023,0-5.053,1.123-5.883,2.699h-0.086v-2.699h-5.576v20h5.828v-9.913c0-2.614,0.494-5.145,3.728-5.145c3.186,0,3.443,2.989,3.443,5.314v9.745h6V28.044z"/></svg><span><span class="contact-row__label">LinkedIn</span><br><span class="contact-row__value">DESIGNJ</span></span></a>
          <a class="contact-row" href="https://www.facebook.com/designj.de" target="_blank" rel="noopener"><svg class="ico" viewBox="8 8 32 32" fill="currentColor" aria-hidden="true"><path d="M20.018,39.035h6c0,0,0-8.282,0-15h4.453l0.547-6H26.25v-2.399c0-1.169,0.779-1.441,1.326-1.441c0.547,0,3.366,0,3.366,0V9.053l-4.635-0.019c-5.145,0-6.314,3.834-6.314,6.288v2.712h-2.975v6h3C20.018,30.834,20.018,39.035,20.018,39.035z"/></svg><span><span class="contact-row__label">Facebook</span><br><span class="contact-row__value">DESIGNJ</span></span></a>
        </div>
      </div>
      <div class="reveal kmp-form-col">
        <h2 class="contact-h2">Oder schreib mir hier:</h2>
        <form class="form" style="margin-top:1.4rem" action="https://form.taxi/s/3g9tnrn5" method="POST">
          <input type="hidden" name="_subject" value="{k_subject}">
          <input type="hidden" name="_lang" value="de">
          <input type="hidden" name="_next" value="https://www.designj.de/danke">
          <input type="text" name="_gotcha" tabindex="-1" autocomplete="off" aria-hidden="true" style="position:absolute;left:-9999px;width:1px;height:1px;opacity:0" value="">
          <input type="hidden" name="Herkunft" value="{k_herkunft}">
          <div class="form__row"><label class="label" for="s-name">Dein Name <span class="req">*</span></label><input class="input" type="text" id="s-name" name="name" required></div>
          <div class="form__row"><label class="label" for="s-email">Deine E-Mail <span class="req">*</span></label><input class="input" type="email" id="s-email" name="email" required></div>
          <div class="form__row"><label class="label" for="s-phone">Deine Telefonnummer (optional, aber hilfreich)</label><input class="input" type="tel" id="s-phone" name="telefon"></div>
          <div class="form__row"><label class="label" for="s-plan">Woran denkst du? <span class="req">*</span></label>
            <select class="select" id="s-plan" name="thema" required><option value="" disabled selected>Bitte wählen&#8230;</option>{k_options}</select>
          </div>
          <div class="form__row"><label class="label" for="s-msg">Deine Nachricht <span class="req">*</span></label><textarea class="textarea" id="s-msg" name="nachricht" required></textarea></div>
          <div class="form__row"><label class="check"><input type="checkbox" name="dsgvo" required><span>Ich stimme zu, dass meine Angaben zur Beantwortung meiner Anfrage erhoben und verarbeitet werden. Die Daten werden nach Bearbeitung gelöscht. Details in der <a href="/datenschutz">Datenschutzerklärung</a>.</span></label></div>
          <button type="submit" class="btn btn--accent btn--block btn--lg">Nachricht absenden <span class="arrow">&#8594;</span></button>
          <p class="form-note">Ich melde mich in der Regel innerhalb von <br class="br--mobile">24 Stunden – meist deutlich schneller.</p>
        </form>
      </div>
    </div>
  </div>
</section>'''

def build_main(p):
    # Fuehrendes Leerzeichen ist PFLICHT: auf Desktop am Zeilenende verworfen,
    # auf Mobil (br ausgeblendet) bleibt es als Wort-Abstand -> keine zusammen-
    # geklebten Woerter. Immer Daten mit plain <br> schreiben, NIE br--desktop
    # hartcodieren, damit diese Umwandlung greift.
    BRD = ' <br class="br--desktop">'
    packs = "\n".join(c.replace("<br>", BRD) for c in p["packs"])
    note = f'    <p class="kmp-pack-note"><span class="chev">»</span> {p["pak_note"].replace("<br>", BRD)}</p>' if p.get("pak_note") else ''
    net = "\n".join(f'        <li>{i.replace("<br>", BRD)}</li>' for i in p["net_items"])
    steps = "\n".join(p["steps"])
    shots = "\n".join(p["shots"])
    faqs = "\n".join(faqitem(q, a) for q, a in p["faq"])
    paras = "\n".join(f'        <p>{x.replace("<br>", BRD)}</p>' for x in p["intro_paras"])
    kontakt = KONTAKT.format(k_h2=p["k_h2"].replace("<br>", BRD), k_lead=p["k_lead"], k_subject=p["k_subject"], k_herkunft=p["k_herkunft"], k_options=p["k_options"])
    has_shots = bool(p.get("shots"))
    btn_ref = '<a href="#referenzen" class="btn btn--ghost btn--lg">Beispiele ansehen</a>' if has_shots else ''
    ref_section = f'''<section class="section" id="referenzen">
  <div class="container">
    <div class="section-head reveal" style="max-width:none">
      <span class="eyebrow">Referenzen</span>
      <h2>{p["ref_h2"].replace("<br>", BRD)}</h2>
      <p class="lead" style="max-width:720px">{p["ref_lead"].replace("<br>", BRD)}</p>
    </div>
    <div class="kmp-shots">
{shots}
    </div>
  </div>
</section>''' if has_shots else ''
    return f'''<main class="kampagne">

<section class="kmp-hero">
  <div class="container kmp-hero__grid">
    <div class="reveal">
      <span class="eyebrow">{p["eyebrow"]}</span>
      <h1 class="seo-h1">{p["h1"].replace("<br>", BRD)}</h1>
      <p class="lead" style="max-width:none">{p["lead"].replace("<br>", BRD)}</p>
      <a href="#kontakt" class="btn btn--accent btn--lg"><span class="chev">»</span> Projekt starten</a>
      {btn_ref}
    </div>
    <div class="kmp-hero__media reveal" data-delay="120">
      <img src="{R}{p["hero_img"]}.webp" alt="{p["hero_alt"]}" style="border-radius:var(--radius)">
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section-head section-head--wide reveal" style="max-width:none">
      <span class="eyebrow">Warum DESIGNJ</span>
      <h2>{p["intro_h2"].replace("<br>", BRD)}</h2>
    </div>
    <div class="bio-block reveal">
      <div>
{paras}
      </div>
      <div class="bio-block__media"><img src="{R}{p["intro_img"]}.webp" alt="{p["intro_alt"]}" loading="lazy" style="border-radius:var(--radius)"></div>
    </div>
  </div>
</section>

<section class="section" id="pakete">
  <div class="container">
    <div class="section-head section-head--center reveal">
      <span class="eyebrow">{p["pak_eyebrow"]}</span>
      <h2>{p["pak_h2"].replace("<br>", BRD)}</h2>
    </div>
    <div class="kmp-packages">
{packs}
    </div>
{note}
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="kmp-net">
      <div class="reveal">
        <div class="section-head" style="max-width:none"><span class="eyebrow">Immer dabei</span><h2>{p["net_h2"].replace("<br>", BRD)}</h2></div>
        <p class="lead">{p["net_lead"].replace("<br>", BRD)}</p>
      </div>
      <ul class="kmp-net__list reveal" data-delay="120">
{net}
      </ul>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section-head section-head--center reveal" style="max-width:none">
      <span class="eyebrow">So läuft's ab</span>
      <h2>{p["abl_h2"].replace("<br>", BRD)}</h2>
      <p class="lead" style="max-width:820px;margin-inline:auto">{p["abl_lead"].replace("<br>", BRD)}</p>
    </div>
    <div class="kmp-steps">
{steps}
    </div>
  </div>
</section>

{ref_section}

<section class="section" id="faq">
  <div class="container">
    <div class="section-head section-head--center reveal">
      <span class="eyebrow">Häufige Fragen</span>
      <h2>{p["faq_h2"].replace("<br>", BRD)}</h2>
    </div>
    <div class="faq reveal">
{faqs}
    </div>
  </div>
</section>

{kontakt}

</main>'''

def build_page(slug, p):
    s = SKEL
    s = s.replace("<title>Marketing auslagern Weiden | Werbeagentur DESIGNJ</title>", f"<title>{p['title']}</title>")
    s = re.sub(r'<meta name="description" content="[^"]*">', f'<meta name="description" content="{p["desc"]}">', s, count=1)
    s = s.replace('<link rel="canonical" href="https://www.designj.de/marketing-auslagern">', f'<link rel="canonical" href="https://www.designj.de/{slug}">')
    s = s.replace('<meta property="og:title" content="Marketing auslagern Weiden | Werbeagentur DESIGNJ">', f'<meta property="og:title" content="{p["title"]}">')
    s = re.sub(r'<meta property="og:description" content="[^"]*">', f'<meta property="og:description" content="{p["desc"]}">', s, count=1)
    s = s.replace('<meta property="og:url" content="https://www.designj.de/marketing-auslagern">', f'<meta property="og:url" content="https://www.designj.de/{slug}">')
    # FAQ-Schema ersetzen
    schema = ',\n'.join(schema_q(q, a) for q, a in p["faq"])
    faq_block = f'''<!-- FAQ-Schema (Rich Results) -->
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
{schema}
    ]
  }}
  </script>'''
    s = re.sub(r'<!-- FAQ-Schema \(Rich Results\) -->\s*<script type="application/ld\+json">.*?</script>', lambda m: faq_block, s, count=1, flags=re.S)
    # weiss-auf-schwarz
    s = s.replace('<body class="kampagne-bedarf">', '<body class="kampagne">')
    # main ersetzen
    s = re.sub(r'<main class="kampagne">.*?</main>', lambda m: build_main(p), s, count=1, flags=re.S)
    (ROOT / f"{slug}.html").write_text(s, encoding="utf-8")
    return slug

# ---------------- DATEN ----------------
from _service_data import PAGES   # noqa
for slug, p in PAGES.items():
    build_page(slug, p)
    print("gebaut:", slug + ".html")
