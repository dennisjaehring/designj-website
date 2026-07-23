#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Baut eine Kampagnenseite (Menü) auf Macher-Basis (handwerk.html) mit voller Niche-Copy.
Aufruf: python3 _build/build_campaign.py   (baut kanzlei.html + praxis.html)
"""
import re, shutil, os, sys
FORCE = '--force' in sys.argv
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)

MK = '<svg class="mk" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M5 13l4 4L19 7"/></svg>'

# 4 generische Pain-Icons + 3 Modell-Icons (abstrakt, über Nischen wiederverwendet)
PAIN_ICONS = [
 '<svg class="ico" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c2.5 2.6 2.5 15.4 0 18M12 3c-2.5 2.6-2.5 15.4 0 18"/></svg>',
 '<svg class="ico" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><rect x="5" y="3" width="14" height="18" rx="2"/><path d="M9 8h6M9 12h6M9 16h3"/></svg>',
 '<svg class="ico" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><circle cx="8" cy="9" r="3"/><circle cx="17" cy="9" r="3"/><path d="M2 20c0-3 3-5 6-5s6 2 6 5M14 15c3 0 8 1 8 5"/></svg>',
 '<svg class="ico" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/></svg>',
]
MODEL_ICONS = [
 '<svg class="ico" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3 21 7.5 12 12 3 7.5Z"/><path d="M3 12 12 16.5 21 12"/><path d="M3 16 12 20.5 21 16"/></svg>',
 '<svg class="ico" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="M21 12a9 9 0 1 1-2.6-6.4M21 4v5h-5"/></svg>',
 '<svg class="ico" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><circle cx="8" cy="9" r="3"/><circle cx="17" cy="9" r="3"/><path d="M2 20c0-3 3-5 6-5s6 2 6 5M14 15c3 0 8 1 8 5"/></svg>',
]
C = {
 'HERO':"<!-- ============================ HERO ============================ -->",
 'PAIN':"<!-- ============================ PAIN ============================ -->",
 'MOD' :"<!-- ===================== BRÜCKE + LÖSUNGS-MODELLE ===================== -->",
 'NET' :"<!-- ===================== NETZWERK ===================== -->",
 'BEW' :"<!-- ============ BEWEIS/ANGEBOT-SLOT · VERGLEICHSTABELLE ============ -->",
 'LEI' :"<!-- ===================== LEISTUNGEN ===================== -->",
 'BSP' :"<!-- ===================== PRAXIS-BEISPIELE (Bild-Block, VARIABEL je Kampagne) ===================== -->",
 'STP' :"<!-- ===================== SO LÄUFT DIE ZUSAMMENARBEIT ===================== -->",
}
def swap(h, start, nxt, block):
    pat = re.escape(C[start]) + r'.*?(?=' + re.escape(C[nxt]) + r')'
    h2, n = re.subn(pat, lambda m: block, h, count=1, flags=re.DOTALL)
    assert n==1, f"FAIL {start}"
    return h2

def build(cfg):
    if os.path.exists(cfg['file']) and not FORCE:
        print(f"{cfg['file']} — existiert bereits, UEBERSPRUNGEN (handgepflegt; nur mit --force ueberschreiben)"); return
    shutil.copy("handwerk.html", cfg['file'])
    h = open(cfg['file'], encoding="utf-8").read()

    HERO = C['HERO'] + f'''
<section class="kmp-hero">
  <div class="container kmp-hero__grid">
    <div class="reveal">
      <span class="eyebrow">{cfg['eyebrow']}</span>
      <h1>{cfg['h1a']}<br><span class="accentword">{cfg['h1b']}</span><span class="kmp-hero__answer">{cfg['sub']}</span></h1>
      <p class="lead">{cfg['lead']}</p>
      <a href="#kontakt" class="btn btn--accent btn--lg"><span class="chev">»</span> Unverbindlich anfragen</a>
    </div>
    <div class="kmp-hero__media reveal" data-delay="120">
      <div class="placeholder-img ratio-1-1" data-label="Hero · {cfg['hero_label']} – Firefly folgt"></div>
    </div>
  </div>
</section>

'''
    pain_cards = ""
    for i,(t,p) in enumerate(cfg['pain']):
        d = f' data-delay="{i*80}"' if i else ''
        pain_cards += f'''      <div class="card reveal"{d}>
        {PAIN_ICONS[i]}
        <h3>{t}</h3>
        <p>{p}</p>
      </div>
'''
    PAIN = C['PAIN'] + f'''
<section class="section">
  <div class="container">
    <div class="section-head section-head--wide reveal">
      <span class="eyebrow">Erkennst du dich wieder?</span>
      <h2>{cfg['pain_h2']}</h2>
    </div>
    <div class="kmp-pain">
{pain_cards}    </div>
    <p class="kmp-painnote reveal">Genau hier setze ich an <span class="chev">»</span> {cfg['painnote']}</p>
  </div>
</section>

'''
    models = ""
    for i,(t,p) in enumerate(cfg['models']):
        d = f' data-delay="{i*100}"' if i else ''
        models += f'''      <div class="kmp-model reveal"{d}>
        {MODEL_ICONS[i]}
        <h3>{t}</h3>
        <p>{p}</p>
      </div>
'''
    MOD = C['MOD'] + f'''
<section class="section">
  <div class="container">
    <div class="section-head section-head--center section-head--wide reveal">
      <span class="eyebrow">So einfach geht&rsquo;s</span>
      <h2>{cfg['mod_h2']}</h2>
      <p class="lead">{cfg['mod_lead']}</p>
    </div>
    <div class="kmp-models">
{models}    </div>
  </div>
</section>

'''
    def pack(name, tag, bullets, feat=False):
        badge = '<span class="kmp-pack__badge">Empfehlung</span>\n        ' if feat else ''
        cls = ' kmp-pack--feat' if feat else ''
        dl = ' data-delay="100"' if feat else (' data-delay="200"' if name==cfg['packs'][2][0] else '')
        lis = "".join(f'          <li>{MK}{b}</li>\n' for b in bullets)
        return f'''      <div class="kmp-pack{cls} reveal"{dl}>
        {badge}<div class="kmp-pack__name">{name}</div>
        <p class="kmp-pack__tag">{tag}</p>
        <ul class="kmp-pack__list">
{lis}        </ul>
      </div>'''
    p0,p1,p2 = cfg['packs']
    BEW = C['BEW'].replace("VERGLEICHSTABELLE","PAKETE") + f'''
<section class="section">
  <div class="container">
    <div class="section-head section-head--center reveal">
      <span class="eyebrow">Drei Wege zu deinem Auftritt</span>
      <h2>Such dir aus,<br>wie viel du abgibst.</h2>
    </div>
    <div class="kmp-packages">
{pack(*p0)}
{pack(*p1, feat=True)}
{pack(*p2)}
    </div>
    <p class="kmp-pack-note reveal"><span class="chev">»</span> Nichts Passendes dabei? Die Pakete sind nur eine Empfehlung –<br>{cfg['pack_note']}</p>
  </div>
</section>

'''
    items=""
    for i,(t,p) in enumerate(cfg['leistungen']):
        d = f' data-delay="{(i%4)*60}"' if i else ''
        items += f'''      <details class="kmp-acc__item reveal"{d}>
        <summary><span class="kmp-acc__ico" aria-hidden="true">+</span><span class="kmp-acc__title">{t}</span></summary>
        <p>{p}</p>
      </details>
'''
    LEI = C['LEI'] + f'''
<section class="section" id="leistungen">
  <div class="container">
    <div class="section-head reveal">
      <span class="eyebrow">Wobei ich dich unterstützen kann</span>
      <h2>Alles aus einer Hand</h2>
    </div>
    <div class="kmp-acc">
{items}    </div>
  </div>
</section>

'''
    figs=""
    for i,c in enumerate(cfg['caps']):
        d=f' data-delay="{i*80}"' if i else ''
        figs += f'''      <figure class="kmp-shot reveal"{d}>
        <div class="placeholder-img" style="aspect-ratio:3/2" data-label="Best Case {i+1} · Firefly folgt"></div>
        <figcaption class="kmp-shot__cap"><span class="chev">»</span> {c}</figcaption>
      </figure>
'''
    BSP = C['BSP'] + f'''
<section class="section" id="beispiele">
  <div class="container">
    <div class="section-head section-head--wide reveal">
      <span class="eyebrow">Beispiele aus der Praxis</span>
      <h2>Sieh, was möglich ist.</h2>
      <p class="lead">Vier Beispiele, die zeigen, wohin es gehen kann – und das ist längst nicht alles. {cfg['bsp_line']}</p>
    </div>
    <div class="kmp-shots">
{figs}    </div>
  </div>
</section>

'''
    h = swap(h,'HERO','PAIN',HERO)
    h = swap(h,'PAIN','MOD',PAIN)
    h = swap(h,'MOD','NET',MOD)
    h = swap(h,'BEW','LEI',BEW)
    h = swap(h,'LEI','BSP',LEI)
    h = swap(h,'BSP','STP',BSP)

    # Meta / Body / Formular / Steps-Kontakt
    subs = [
     ('<body class="kampagne-macher">', f'<body class="{cfg["bodyclass"]}">'),
     ('<title>Marketing fürs Handwerk | mit DESIGNJ sichtbar werden</title>', f'<title>{cfg["title"]}</title>'),
     ('<meta property="og:title" content="Marketing fürs Handwerk | mit DESIGNJ sichtbar werden">', f'<meta property="og:title" content="{cfg["title"]}">'),
     ('content="Du machst top Arbeit – aber keiner sieht\'s? Ich übernehme Marketing fürs Handwerk: Logo, Fahrzeug, Schilder, Website &amp; Social. Damit dich die richtigen Kunden und Mitarbeiter finden. Aus Weiden."', f'content="{cfg["desc"]}"'),
     ('content="Gute Arbeit allein reicht nicht. Logo, Fahrzeug, Schilder, Website &amp; Social – ich mach dein Handwerk sichtbar."', f'content="{cfg["ogdesc"]}"'),
     ('value="Neue Anfrage über Kampagne: Macher (Handwerk)"', f'value="Neue Anfrage über Kampagne: {cfg["subj"]}"'),
     ('value="Macher – Marketing fürs Handwerk"', f'value="{cfg["kampagne"]}"'),
    ]
    warn=[]
    for a,b in subs:
        if a in h: h=h.replace(a,b)
        else: warn.append(a[:40])
    # Formular-Optionen (die 5 Handwerk-Optionen -> Nische)
    hopts = ['Kompletter Auftritt (Logo, Fahrzeug, Schilder, Web)','Website oder Landingpage','Social-Media-Betreuung','Einzelnes Projekt (Schild, Banner, Aktion)','Mitarbeiter finden (Recruiting)']
    for old,new in zip(hopts, cfg['opts']):
        h = h.replace(f'<option>{old}</option>', f'<option>{new}</option>')
    h = h.replace('https://www.designj.de/handwerk', f'https://www.designj.de/{cfg["slug"]}')
    open(cfg['file'],"w",encoding="utf-8").write(h)
    return warn

# ============================ KANZLEI (Violett) ============================
kanzlei = dict(
 file="kanzlei.html", bodyclass="kampagne-kanzlei", slug="kanzlei",
 title="Kanzleimarketing | DESIGNJ – Marketing für Anwälte, Notare &amp; Steuerberater",
 desc="Kanzleimarketing von DESIGNJ – seriöser Auftritt, moderne Website und Nachwuchsgewinnung für Anwälte, Notare und Steuerberater.",
 ogdesc="Fachlich top, kaum präsent? Website, Auftritt &amp; Recruiting – ich bring deine Kanzlei ins Heute.",
 eyebrow="Recht &amp; Steuer",
 h1a="Fachlich top,", h1b="kaum präsent?", sub='Ich bring dich <span class="kmp-emph">ins Heute</span>.',
 hero_label="Kanzlei-Motiv (Violett)",
 lead='Anwälte, Notare, Steuerberater:<br>Deine Arbeit überzeugt –<br>dein Auftritt sollte es auch.',
 pain_h2="Die Mandate laufen,<br>aber der Auftritt wirkt <br class=\"br--mobile\">von gestern.",
 pain=[("Website<br>wie 2010","Mandanten schauen zuerst online."),
       ("Kein einheitliches<br>Erscheinungsbild","Jedes Dokument sieht anders aus."),
       ("Nachwuchs<br>bleibt aus","Gute Leute gehen zur Konkurrenz."),
       ("Keine Zeit<br>fürs Marketing","Neben den Mandaten bleibt&rsquo;s liegen.")],
 painnote="damit deine Kanzlei so seriös wirkt, wie sie arbeitet.",
 mod_h2="Du willst professionell wirken,<br>ohne dich selbst zu kümmern?",
 mod_lead='Du sagst mir, was ansteht.<br><span class="kmp-fg">Ich mach den Rest:</span><br>vom neuen Logo bis zum <br class="br--mobile">kompletten Auftritt – <br class="br--desktop">so viel <br class="br--mobile">oder so wenig, wie du brauchst.',
 models=[("Einmal richtig aufstellen","Logo, Geschäftsausstattung, Website – ein seriöser Auftritt, der zu deiner Kanzlei passt. Einmal sauber gemacht, lange Ruhe."),
         ("Laufend betreut","Website-Pflege, Content und Social übers Jahr – ich halte deinen Auftritt aktuell, du berätst deine Mandanten."),
         ("Nachwuchs gewinnen","Karriereseite, Stellenanzeigen und eine Arbeitgebermarke, die junge Talente wirklich anspricht.")],
 packs=[("Start","Der seriöse Auftritt",["Logo neu oder aufgefrischt","Geschäftsausstattung &amp; Briefbogen","Kanzlei-Vorlagen (Word/PDF)","Einheitliches Erscheinungsbild","Beratung zu deinem Auftritt","Einmal sauber aufgestellt"]),
        ("Plus","Sichtbar &amp; auffindbar",["Alles aus Start","Moderne Kanzlei-Website","Google-Profil &amp; lokale Sichtbarkeit","Content zu Recht- &amp; Steuerthemen","Social-Media-Betreuung","Laufende Pflege &amp; Aktualität"]),
        ("Komplett","Deine Marketing-Abteilung",["Alles aus Plus","Karriereseite &amp; Recruiting","Foto- &amp; Content-Produktion","Kampagnen &amp; Aktionen","Mandanten-Newsletter","Fester Ansprechpartner übers Jahr"])],
 pack_note="für jede Kanzlei finden wir die passende Lösung. Auch ganz individuell.",
 leistungen=[
   ("Kanzlei-Auftritt &amp; Design","Logo, Geschäftsausstattung, Briefbogen und Vorlagen – ein einheitliches, seriöses Erscheinungsbild über alle Dokumente und Kanäle."),
   ("Website &amp; Auffindbarkeit","Moderne Kanzlei-Website mit sauberen SEO-Grundlagen, damit Mandanten dich finden – inkl. Texten, die Vertrauen schaffen statt Juristendeutsch."),
   ("Recruiting &amp; Karriere","Karriereseite, Stellenanzeigen und eine Arbeitgebermarke, die zu dir passt. Damit du nicht nur Mandate gewinnst, sondern auch den richtigen Nachwuchs."),
   ("Social Media &amp; LinkedIn","Redaktionsplan, Beiträge und Betreuung – gerade LinkedIn ist für Kanzleien Gold wert. Du musst nicht selbst posten, ich halte deinen Auftritt am Leben."),
   ("Content &amp; Fachthemen","Recht- und Steuerthemen verständlich aufbereitet – Ratgeber, Merkblätter, Beiträge. Positioniert dich als Experte und bringt dich bei Google nach vorn."),
   ("Print &amp; Kanzlei-Material","Broschüren, Mandantenmappen, Visitenkarten, Kanzleischilder – Druckdaten und Abwicklung koordiniert, du bekommst das fertige Ergebnis."),
   ("Beratung &amp; Struktur","Manchmal fehlt nicht die Umsetzung, sondern der Plan. Ich bring Struktur in dein Kanzlei-Marketing und sage ehrlich, was Sinn macht – und was nicht."),
   ("Foto &amp; Content","Echte Bilder von dir und deinem Team – seriös, aber nahbar. Statt Stockfotos, die jede Kanzlei hat."),
 ],
 caps=["Kanzlei-Website","Geschäftsausstattung","Karriere &amp; Stellenanzeige","Imagebroschüre"],
 bsp_line="Von Print über Website bis Social setze ich um, was zu deiner Kanzlei passt.",
 subj="Kanzlei", kampagne="Kanzlei (Recht &amp; Steuer)",
 opts=["Kompletter Auftritt (Logo, Website, Design)","Website oder Kanzlei-Auftritt","Recruiting &amp; Karriereseite","Social Media &amp; LinkedIn","Content &amp; Fachthemen"],
)

# ============================ GESUNDHEIT (Türkis) ============================
praxis = dict(
 file="praxis.html", bodyclass="kampagne-gesundheit", slug="praxis",
 title="Praxismarketing | DESIGNJ – Marketing für Praxen, Kliniken &amp; Pflege",
 desc="Praxismarketing von DESIGNJ – moderne Website, Patientenkommunikation und Personalgewinnung für Praxen, Kliniken und Pflegeeinrichtungen.",
 ogdesc="Patienten ja, Personal nein? Website, Auftritt &amp; Recruiting – für Praxen, Kliniken und Pflege.",
 eyebrow="Praxen &amp; Pflege",
 h1a="Patienten ja,", h1b="Personal nein?", sub='Ich bring dir die <span class="kmp-emph">Leute</span>.',
 hero_label="Gesundheit-Motiv (Türkis)",
 lead='Praxen, Kliniken, Pflege:<br>moderner Auftritt, neues Personal –<br>beides aus einer Hand.',
 pain_h2="Die Praxis läuft,<br>aber Auftritt und Team <br class=\"br--mobile\">brauchen Hilfe.",
 pain=[("Website<br>veraltet","Patienten suchen zuerst online."),
       ("Stellen bleiben<br>unbesetzt","Fachkräfte sind hart umkämpft."),
       ("Kein einheitlicher<br>Auftritt","Vom Schild bis zum Formular."),
       ("Keine Zeit<br>fürs Drumherum","Neben Patienten bleibt&rsquo;s liegen.")],
 painnote="damit deine Praxis Patienten UND Fachkräfte erreicht.",
 mod_h2="Du willst modern wirken,<br>ohne dich selbst zu kümmern?",
 mod_lead='Du sagst mir, was ansteht.<br><span class="kmp-fg">Ich mach den Rest:</span><br>von der Website bis zur <br class="br--mobile">Stellenanzeige – <br class="br--desktop">so viel <br class="br--mobile">oder so wenig, wie du brauchst.',
 models=[("Einmal richtig aufstellen","Logo, Praxis-Ausstattung, Website – ein moderner Auftritt, der Vertrauen schafft. Einmal sauber gemacht, lange Ruhe."),
         ("Laufend betreut","Website-Pflege, Social und Patienten-Infos übers Jahr – ich halte deinen Auftritt aktuell, du kümmerst dich um Patienten."),
         ("Personal gewinnen","Karriereseite, Stellenanzeigen und eine Arbeitgebermarke, die Fachkräfte anspricht – gerade in der Pflege entscheidend.")],
 packs=[("Start","Der moderne Auftritt",["Logo neu oder aufgefrischt","Praxis-Ausstattung &amp; Leitsystem","Formulare &amp; Vorlagen","Einheitliches Erscheinungsbild","Beratung zu deinem Auftritt","Einmal sauber aufgestellt"]),
        ("Plus","Gefunden werden",["Alles aus Start","Moderne Praxis-Website","Google-Profil &amp; lokale Sichtbarkeit","Social-Media-Betreuung","Patienten-Infos &amp; Content","Laufende Pflege &amp; Aktualität"]),
        ("Komplett","Auftritt &amp; Team",["Alles aus Plus","Karriereseite &amp; Recruiting","Foto- &amp; Content-Produktion","Kampagnen &amp; Aktionen","Patienten-Kommunikation","Fester Ansprechpartner übers Jahr"])],
 pack_note="für jede Praxis finden wir die passende Lösung. Auch ganz individuell.",
 leistungen=[
   ("Praxis-Website &amp; Auffindbarkeit","Moderne Website mit Online-Terminen, sauberen SEO-Grundlagen und verständlichen Texten. Damit Patienten dich finden – und nicht die Praxis nebenan."),
   ("Recruiting &amp; Karriere","Karriereseite, Stellenanzeigen und eine Arbeitgebermarke, die zu dir passt. Damit du die Fachkräfte findest, die du wirklich brauchst."),
   ("Praxis-Design &amp; Ausstattung","Logo, Praxisschilder, Leitsystem, Formulare und Ausstattung – ein einheitlicher, moderner Auftritt vom Empfang bis zum Wartezimmer."),
   ("Social Media &amp; Patienten-Infos","Redaktionsplan, Beiträge und Betreuung bei Instagram &amp; Facebook. Öffnungszeiten, Team, Leistungen – deine Praxis bleibt sichtbar und nahbar."),
   ("Content &amp; Aufklärung","Gesundheitsthemen verständlich aufbereitet – für Website, Social und Wartezimmer. Positioniert dich als kompetente Anlaufstelle."),
   ("Print &amp; Praxis-Material","Flyer, Terminkarten, Aufklärungsbögen, Praxisschilder – Druckdaten und Abwicklung koordiniert, du bekommst das fertige Ergebnis."),
   ("Beratung &amp; Struktur","Manchmal fehlt nicht die Umsetzung, sondern der Plan. Ich bring Struktur in dein Praxis-Marketing und sage ehrlich, was Sinn macht – und was nicht."),
   ("Foto &amp; Content","Echte Bilder von dir, deinem Team und deiner Praxis – vertrauensvoll und nahbar. Statt Stockfotos, die jede Praxis hat."),
 ],
 caps=["Praxis-Website","Praxis-Ausstattung &amp; Leitsystem","Karriere &amp; Stellenanzeige","Social Media &amp; Patienten-Info"],
 bsp_line="Von Website über Print bis Social setze ich um, was deine Praxis braucht.",
 subj="Gesundheit", kampagne="Gesundheit (Praxen &amp; Pflege)",
 opts=["Kompletter Auftritt (Logo, Website, Praxis)","Website oder Praxis-Auftritt","Recruiting &amp; Karriereseite","Social Media &amp; Patienten-Infos","Praxis-Ausstattung &amp; Leitsystem"],
)

for cfg in (kanzlei, praxis):
    w = build(cfg)
    print(f"{cfg['file']}: {'✅' if not w else '⚠️ '+str(w)}")
print("fertig.")
