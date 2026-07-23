#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Baut eine SEO-Landingpage auf Basis von marketing-fuers-handwerk.html.
python3 _build/build_seo.py  -> immobilienmarketing / kanzleimarketing / praxismarketing"""
import re, shutil, os, json, sys
FORCE = '--force' in sys.argv
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__))); os.chdir(ROOT)
MASTER = "marketing-fuers-handwerk.html"
MK = '<svg class="mk" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M5 13l4 4L19 7"/></svg>'
def CM(x): return f"<!-- ============================ {x} ============================ -->"
ANCH = {'HERO':CM('HERO'),'INTRO':CM('INTRO / KEYWORD'),'LEI':CM('LEISTUNGEN'),'BSP':CM('BEISPIELE'),
        'PAK':CM('PAKETE'),'ABL':CM('ABLAUF'),'LOK':CM('LOKAL'),'FAQ':CM('FAQ'),
        'KON':"<!-- ===================== KONTAKT ===================== -->"}
def swap(h, a, b, block):
    pat = re.escape(ANCH[a]) + r'.*?(?=' + re.escape(ANCH[b]) + r')'
    h2,n = re.subn(pat, lambda m: block, h, count=1, flags=re.DOTALL); assert n==1, f"FAIL {a}"; return h2
PH = lambda label, ratio="4/3": f'<div class="placeholder-img" style="aspect-ratio:{ratio}" data-label="{label}"></div>'

def build(cfg):
    if os.path.exists(cfg['file']) and not FORCE:
        print(f"{cfg['file']} — existiert bereits, UEBERSPRUNGEN (handgepflegt; nur mit --force ueberschreiben)"); return
    shutil.copy(MASTER, cfg['file']); h = open(cfg['file'],encoding="utf-8").read()

    HERO = ANCH['HERO'] + f'''
<section class="kmp-hero">
  <div class="container kmp-hero__grid">
    <div class="reveal">
      <span class="eyebrow">{cfg['eyebrow']}</span>
      <h1 class="seo-h1">{cfg['h1a']}<br><span class="accentword">{cfg['h1b']}</span>.</h1>
      <p class="lead" style="max-width:none">{cfg['hero_lead']}</p>
      <a href="#kontakt" class="btn btn--accent btn--lg"><span class="chev">»</span> Unverbindlich anfragen</a>
    </div>
    <div class="kmp-hero__media reveal" data-delay="120">
      <div class="placeholder-img ratio-1-1" data-label="Hero · {cfg['hero_label']} – Firefly folgt"></div>
    </div>
  </div>
</section>

'''
    intro_ps = "\n        ".join(f"<p>{p}</p>" for p in cfg['intro_ps'])
    INTRO = ANCH['INTRO'] + f'''
<section class="section">
  <div class="container">
    <div class="section-head section-head--wide reveal">
      <span class="eyebrow">{cfg['intro_eyebrow']}</span>
      <h2>{cfg['intro_h2']}</h2>
    </div>
    <div class="bio-block reveal">
      <div>
        {intro_ps}
      </div>
      <div class="bio-block__media">{PH(cfg['intro_img'])}</div>
    </div>
  </div>
</section>

'''
    accs = ""
    for i,(t,p) in enumerate(cfg['leistungen']):
        d = f' data-delay="{(i%4)*60}"' if i else ''
        accs += f'''      <details class="kmp-acc__item reveal"{d}>
        <summary><span class="kmp-acc__ico" aria-hidden="true">+</span><span class="kmp-acc__title">{t}</span></summary>
        <p>{p}</p>
      </details>
'''
    LEI = ANCH['LEI'] + f'''
<section class="section" id="leistungen">
  <div class="container">
    <div class="section-head reveal">
      <span class="eyebrow">Wobei ich dich unterstütze</span>
      <h2>{cfg['leist_h2']}</h2>
    </div>
    <div class="kmp-acc">
{accs}    </div>
  </div>
</section>

'''
    figs=""
    for i,c in enumerate(cfg['beisp_caps']):
        d=f' data-delay="{i*100}"' if i else ''
        figs += f'''      <figure class="kmp-shot reveal"{d}>
        {PH("Best Case "+str(i+1)+" · Firefly folgt","3/2").replace('placeholder-img','placeholder-img kmp-ph')}
        <figcaption class="kmp-shot__cap"><span class="chev">»</span> {c}</figcaption>
      </figure>
'''
    BSP = ANCH['BSP'] + f'''
<section class="section">
  <div class="container">
    <div class="section-head reveal" style="max-width:none">
      <span class="eyebrow">Beispiele aus der Praxis</span>
      <h2>{cfg['beisp_h2']}</h2>
    </div>
    <div class="kmp-shots">
{figs}    </div>
  </div>
</section>

'''
    def pack(name,tag,bullets,feat=False,dl=''):
        badge='<span class="kmp-pack__badge">Empfehlung</span>\n        ' if feat else ''
        cls=' kmp-pack--feat' if feat else ''
        lis="".join(f'          <li>{MK}{b}</li>\n' for b in bullets)
        return f'''      <div class="kmp-pack{cls} reveal"{dl}>
        {badge}<div class="kmp-pack__name">{name}</div>
        <p class="kmp-pack__tag">{tag}</p>
        <ul class="kmp-pack__list">
{lis}        </ul>
      </div>'''
    p0,p1,p2 = cfg['packs']
    PAK = ANCH['PAK'] + f'''
<section class="section">
  <div class="container">
    <div class="section-head section-head--center reveal">
      <span class="eyebrow">Drei Wege zu deinem Auftritt</span>
      <h2>Such dir aus,<br>wie viel du abgibst.</h2>
    </div>
    <div class="kmp-packages">
{pack(*p0)}
{pack(*p1, feat=True, dl=' data-delay="100"')}
{pack(*p2, dl=' data-delay="200"')}
    </div>
    <p class="kmp-pack-note reveal"><span class="chev">»</span> Nichts Passendes dabei? Die Pakete sind nur eine Empfehlung –<br>{cfg['pack_note']}</p>
  </div>
</section>

'''
    steps=""
    for i,(t,p) in enumerate(cfg['steps']):
        d=f' data-delay="{i*100}"' if i else ''
        steps += f'      <div class="kmp-step reveal"{d}><div class="kmp-step__num"></div><h3>{t}</h3><p>{p}</p></div>\n'
    ABL = ANCH['ABL'] + f'''
<section class="section">
  <div class="container">
    <div class="section-head section-head--center reveal" style="max-width:none">
      <span class="eyebrow">So läuft die Zusammenarbeit</span>
      <h2>Einfach, direkt und ohne Chaos.</h2>
      <p class="lead" style="max-width:680px;margin-inline:auto">{cfg['ablauf_lead']}</p>
    </div>
    <div class="kmp-steps">
{steps}    </div>
  </div>
</section>

'''
    lok_ps = "\n        ".join(f"<p>{p}</p>" for p in cfg['lokal_ps'])
    LOK = ANCH['LOK'] + f'''
<section class="section">
  <div class="container">
    <div class="section-head section-head--wide reveal">
      <span class="eyebrow">Für die Region</span>
      <h2>{cfg['lokal_h2']}</h2>
    </div>
    <div class="bio-block bio-block--reverse reveal">
      <div>
        {lok_ps}
      </div>
      <div class="bio-block__media">{PH(cfg['lokal_img'])}</div>
    </div>
  </div>
</section>

'''
    faqitems=""
    for q,a in cfg['faq']:
        faqitems += f'''      <details class="faq__item">
        <summary>{q}</summary>
        <p>{a}</p>
      </details>
'''
    FAQ = ANCH['FAQ'] + f'''
<section class="section" id="faq">
  <div class="container">
    <div class="section-head section-head--center reveal">
      <span class="eyebrow">Häufige Fragen</span>
      <h2>{cfg['faq_h2']}</h2>
    </div>
    <div class="faq reveal">
{faqitems}    </div>
  </div>
</section>

'''
    h = swap(h,'HERO','INTRO',HERO); h = swap(h,'INTRO','LEI',INTRO); h = swap(h,'LEI','BSP',LEI)
    h = swap(h,'BSP','PAK',BSP); h = swap(h,'PAK','ABL',PAK); h = swap(h,'ABL','LOK',ABL)
    h = swap(h,'LOK','FAQ',LOK); h = swap(h,'FAQ','KON',FAQ)

    # FAQPage-Schema neu bauen (muss zur sichtbaren FAQ passen)
    qa = ",\n      ".join('{ "@type": "Question", "name": %s, "acceptedAnswer": { "@type": "Answer", "text": %s } }' %
                          (json.dumps(q, ensure_ascii=False), json.dumps(a, ensure_ascii=False)) for q,a in cfg['faq'])
    h = re.sub(r'(<script type="application/ld\+json">\s*\{\s*"@context": "https://schema.org",\s*"@type": "FAQPage",\s*"mainEntity": \[).*?(\]\s*\}\s*</script>)',
               lambda m: m.group(1) + "\n      " + qa + "\n    " + m.group(2), h, count=1, flags=re.DOTALL)

    # Head / Body / Kontakt
    subs = [
     ('<body class="kampagne-macher">', f'<body class="{cfg["bodyclass"]}">'),
     ('<title>Marketing fürs Handwerk Weiden | Werbeagentur DESIGNJ</title>', f'<title>{cfg["title"]}</title>'),
     ('<meta property="og:title" content="Marketing fürs Handwerk Weiden | Werbeagentur DESIGNJ">', f'<meta property="og:title" content="{cfg["title"]}">'),
     ('<meta name="description" content="Marketing fürs Handwerk aus Weiden: Website, Fahrzeug, Schilder &amp; Social Media aus einer Hand – damit dich die richtigen Kunden und Mitarbeiter finden.">', f'<meta name="description" content="{cfg["desc"]}">'),
     ('<meta property="og:description" content="Website, Fahrzeug, Schilder, Social Media &amp; Recruiting aus einer Hand – damit dein Handwerksbetrieb sichtbar wird.">', f'<meta property="og:description" content="{cfg["desc"]}">'),
     ('name="_subject" value="Neue Anfrage über SEO-Seite: Marketing fürs Handwerk"', f'name="_subject" value="Neue Anfrage über SEO-Seite: {cfg["seoname"]}"'),
     ('name="Herkunft" value="SEO-Seite: Marketing fürs Handwerk"', f'name="Herkunft" value="SEO-Seite: {cfg["seoname"]}"'),
     ('Herkunft = SEO-Seite Handwerk', f'Herkunft = SEO-Seite {cfg["seoname"]}'),
     ('Wir schauen gemeinsam, was zu deinem Handwerksbetrieb passt.', cfg['kontakt_sub']),
    ]
    for a,b in subs:
        h = h.replace(a,b)
    hopts = ['Kompletter Auftritt (Logo, Fahrzeug, Schilder, Web)','Website oder Landingpage','Social-Media-Betreuung','Einzelnes Projekt (Schild, Banner, Aktion)','Mitarbeiter finden (Recruiting)']
    for old,new in zip(hopts, cfg['opts']):
        h = h.replace(f'<option>{old}</option>', f'<option>{new}</option>')
    h = h.replace('https://www.designj.de/marketing-fuers-handwerk', f'https://www.designj.de/{cfg["slug"]}')
    open(cfg['file'],"w",encoding="utf-8").write(h)

# ---- gemeinsame Pakete je Nische aus Kampagnen (kurzgehalten) ----
PACK_IMMO = [("Start","Der saubere Auftritt",["Logo neu oder aufgefrischt","Geschäftsausstattung und Vorlagen","Exposé-Design als Vorlage","Einheitliches Erscheinungsbild","Beratung zu deinem Auftritt","Einmal sauber aufgestellt"]),
 ("Plus","Sichtbar bleiben",["Alles aus Start","Immobilien-Website","Objekt-Präsentation und Exposés","Social-Media-Betreuung","Google-Profil und lokale Sichtbarkeit","Laufende Pflege und Aktualität"]),
 ("Komplett","Dein Marketing-Partner",["Alles aus Plus","Foto-, Video- und Rundgang-Content","Großformat (Bautafel, Verkaufsschild)","Projekt- und Neubau-Kampagnen","Recruiting-Material fürs Team","Fester Ansprechpartner übers Jahr"])]
PACK_KANZ = [("Start","Der seriöse Auftritt",["Logo neu oder aufgefrischt","Geschäftsausstattung und Briefbogen","Kanzlei-Vorlagen (Word/PDF)","Einheitliches Erscheinungsbild","Beratung zu deinem Auftritt","Einmal sauber aufgestellt"]),
 ("Plus","Sichtbar und auffindbar",["Alles aus Start","Moderne Kanzlei-Website","Google-Profil und lokale Sichtbarkeit","Content zu Recht- und Steuerthemen","Social-Media-Betreuung","Laufende Pflege und Aktualität"]),
 ("Komplett","Deine Marketing-Abteilung",["Alles aus Plus","Karriereseite und Recruiting","Foto- und Content-Produktion","Kampagnen und Aktionen","Mandanten-Newsletter","Fester Ansprechpartner übers Jahr"])]
PACK_GES = [("Start","Der moderne Auftritt",["Logo neu oder aufgefrischt","Praxis-Ausstattung und Leitsystem","Formulare und Vorlagen","Einheitliches Erscheinungsbild","Beratung zu deinem Auftritt","Einmal sauber aufgestellt"]),
 ("Plus","Gefunden werden",["Alles aus Start","Moderne Praxis-Website","Google-Profil und lokale Sichtbarkeit","Social-Media-Betreuung","Patienten-Infos und Content","Laufende Pflege und Aktualität"]),
 ("Komplett","Auftritt und Team",["Alles aus Plus","Karriereseite und Recruiting","Foto- und Content-Produktion","Kampagnen und Aktionen","Patienten-Kommunikation","Fester Ansprechpartner übers Jahr"])]

STEPS_GEN = [("Kennenlernen","Du erzählst mir kurz, wo du stehst und wo der Schuh drückt – per Telefon, WhatsApp oder <a href=\"/kontakt\">Kontaktformular</a>. Unverbindlich und ohne Verkaufsgespräch."),
 ("Vorschlag","Ich schaue mir deinen bisherigen Auftritt an und sage dir ehrlich, was Sinn macht – vom einzelnen Baustein bis zum kompletten Auftritt. Eine klare Einschätzung, keine Standardlösung."),
 ("Umsetzung","Ich übernehme Gestaltung, Abstimmung mit Druckerei und Partnern und die komplette Koordination. Du bekommst das fertige Ergebnis – nicht den Stress dazwischen."),
 ("Dranbleiben","Auf Wunsch bleibe ich dein fester Ansprechpartner übers Jahr – für Website, Social Media und alles, was neu dazukommt. So läuft dein Marketing weiter, ohne Leerlauf.")]

immo = dict(file="immobilienmarketing.html", bodyclass="kampagne-immo", slug="immobilienmarketing",
 title="Immobilienmarketing Weiden | Werbeagentur DESIGNJ", seoname="Immobilienmarketing",
 desc="Immobilienmarketing aus Weiden: Exposés, Website, Social Media und Großformat aus einer Hand – für Makler, Architekten und Bauträger, die auffallen wollen.",
 eyebrow="Immobilienmarketing · Weiden &amp; Oberpfalz", h1a="Marketing für", h1b="Immobilien", hero_label="Immobilien-Motiv (Cyan)",
 hero_lead='Exposés, Website, Social Media &amp; Großformat –<br>alles mit einem Ansprechpartner.<br>Damit deine Objekte auffallen und du als Makler,<br>Architekt oder Bauträger professionell wirkst.',
 intro_eyebrow="Warum Immobilienmarketing?", intro_h2="Auffallen –<br>online wie am Objekt.",
 intro_img="Best Case · Website &amp; Portal (Cyan) – Firefly folgt",
 intro_ps=[
  'Gute Objekte verkaufen sich fast von allein – wenn die Präsentation stimmt. Handy-Fotos, Exposés von der Stange und eine lieblose Website lassen selbst Top-Immobilien kleiner wirken, als sie sind. Genau hier setzt <strong>Immobilienmarketing</strong> an: professionelle Exposés, eine überzeugende <a href="/leistungen#web">Website</a> und ein einheitlicher Auftritt, der Wert zeigt.',
  'Als deine Werbeagentur für Weiden und die Oberpfalz übernehme ich das komplett – von der <a href="/leistungen#branding">Marke</a> über Foto und Video bis zu <a href="/leistungen#social">Social Media</a>. Du bist Profi für Immobilien, nicht fürs Marketing. Ein Ansprechpartner, alles aus einer Hand, ohne Agentur-Overhead.',
  'Ob einzelnes Objekt, kompletter Büro-Auftritt oder die laufende Vermarktung deiner Projekte – du entscheidest, wie viel du abgibst. Ich sorge dafür, dass alles zusammenpasst: online, gedruckt und direkt am Objekt.'],
 leist_h2="Immobilienmarketing –<br>alles aus einer Hand.",
 leistungen=[
  ("Exposés &amp; Objekt-Präsentation",'Hochwertige Exposés, Objektbroschüren und Verkaufsunterlagen – so <a href="/leistungen#branding">gestaltet</a>, dass dein Objekt im besten Licht steht. Digital und gedruckt, aus einem Guss.'),
  ("Immobilien-Website &amp; Portale",'Eine überzeugende <a href="/leistungen#web">Website</a> mit Objektübersicht, Landingpages für Projekte und saubere Darstellung auf den Portalen – inkl. Texten und SEO-Grundlagen, damit du gefunden wirst.'),
  ("Foto, Video &amp; Rundgang",'Professionelle Objektfotos, Drohnenaufnahmen und Video-Rundgänge über mein Netzwerk – echte Bilder statt Handyknipse, die den wahren Wert zeigen.'),
  ("Social Media &amp; Reels",'Redaktionsplan, Objekt-Posts, Reels und laufende <a href="/leistungen#social">Betreuung</a> bei Instagram, Facebook &amp; LinkedIn. Neue Objekte und dein Büro bleiben sichtbar.'),
  ("Großformat &amp; Vor-Ort",'Bautafel, Verkaufsschild, Bauzaunbanner und Roll-up – <a href="/leistungen#print">Druck und Werbetechnik</a> koordiniert. Sichtbar direkt am Objekt, ohne Stress dazwischen.'),
  ("Projekt- &amp; Neubau-Vermarktung",'Für Neubau, Quartier oder Tag der offenen Tür: eine <a href="/leistungen#marketing">Kampagne</a>, die über Print, Social und vor Ort funktioniert – statt Einzelmaßnahmen ohne roten Faden.'),
  ("Beratung &amp; laufende Betreuung",'Manchmal fehlt nicht die Umsetzung, sondern der Plan. Ich bringe Struktur in dein Immobilienmarketing und bin der Ansprechpartner übers Jahr, der ehrlich sagt, was Sinn macht.')],
 beisp_h2="So sieht Immobilienmarketing aus.", beisp_caps=["Exposé &amp; Broschüre","Website &amp; Immobilienportal"],
 packs=PACK_IMMO, pack_note="für jedes Büro finden wir die passende Lösung. Auch ganz individuell.",
 ablauf_lead="Kein Angebots-Marathon, kein Fachchinesisch.<br>Du sagst mir, was ansteht – ich kümmere mich um den Rest.", steps=STEPS_GEN,
 lokal_h2="Deine Werbeagentur für Immobilien<br>in Weiden &amp; der Oberpfalz.",
 lokal_img="Best Case · Bautafel &amp; Verkaufsschild (Cyan) – Firefly folgt",
 lokal_ps=[
  'Ob Makler, Bauträger, Architekt oder Immobilienverwaltung – als Werbeagentur für Immobilien kümmere ich mich um deinen kompletten Auftritt. Von Exposé und Objektfotos über Website und Portale bis zu Bautafel und Social Media bekommst du Immobilienmarketing aus einer Hand.',
  'Ich sitze in Irchenrieth bei Weiden in der Oberpfalz und arbeite für Immobilienprofis in der ganzen Region – von Weiden über Neustadt und Tirschenreuth bis Amberg. Vieles läuft unkompliziert digital, auf Wunsch komme ich zum Objekt. Über 20 Jahre Erfahrung sorgen dafür, dass deine Immobilien auffallen.',
  'Wie das aussieht, siehst du bei meinen <a href="/projekte">Referenzen</a>. Egal ob einzelnes Objekt oder kompletter Auftritt – wir finden den Weg, der zu dir und deinem Budget passt.'],
 faq_h2="Immobilienmarketing –<br>kurz &amp; ehrlich erklärt.",
 faq=[
  ("Was bringt professionelles Immobilienmarketing überhaupt?","Eine gute Präsentation verkauft schneller und oft zu besseren Konditionen. Wer ein Objekt mit hochwertigen Fotos, einem klaren Exposé und einer überzeugenden Website zeigt, hebt sich vom Einheitsbrei ab und wird als Profi wahrgenommen."),
  ("Ich habe schon eine Website und Vorlagen – kannst du das auffrischen?","Klar – oft muss nichts komplett neu. Ich frische deinen Auftritt, deine Exposé-Vorlagen und deine Website behutsam auf und modernisiere sie, statt alles über den Haufen zu werfen. So bleibt der Wiedererkennungswert erhalten."),
  ("Machst du auch die Fotos und Video-Rundgänge?","Ja – über mein eingespieltes Netzwerk aus Fotografen und Videografen. Professionelle Objektfotos, Drohnenaufnahmen und Rundgänge zeigen den wahren Wert deiner Immobilie, statt sie klein wirken zu lassen."),
  ("Lohnt sich das auch für einzelne Objekte?","Absolut. Du musst nicht gleich den kompletten Auftritt buchen – ich mache auch Exposé, Fotos und Verkaufsunterlagen für ein konkretes Objekt. Schnell, hochwertig und verkaufsstark."),
  ("Übernimmst du auch Social Media für meine Objekte?","Auf Wunsch komplett. Ich plane, gestalte und betreue deine Kanäle – neue Objekte, dein Büro und deine Projekte bleiben sichtbar, ohne dass du täglich selbst posten musst."),
  ("Arbeitest du auch für Makler und Bauträger in der Oberpfalz?","Klar. Vom einzelnen Makler bis zum Bauträger mit mehreren Projekten – ich sitze in Weiden bzw. Irchenrieth und bin für die ganze Oberpfalz da, vor Ort oder digital.")],
 kontakt_sub="Wir schauen gemeinsam, was zu deinen Objekten passt.",
 subj="Immobilien", kampagne="Bau &amp; Immobilien",
 opts=["Kompletter Auftritt (Logo, Website, Exposés)","Website oder Landingpage","Objekt-Präsentation &amp; Exposés","Social-Media-Betreuung","Großformat (Bautafel, Schild, Banner)"])

kanz = dict(file="kanzleimarketing.html", bodyclass="kampagne-kanzlei", slug="kanzleimarketing",
 title="Kanzleimarketing Weiden | Werbeagentur DESIGNJ", seoname="Kanzleimarketing",
 desc="Kanzleimarketing aus Weiden: moderne Website, seriöser Auftritt und Recruiting aus einer Hand – für Anwälte, Notare und Steuerberater.",
 eyebrow="Kanzleimarketing · Weiden &amp; Oberpfalz", h1a="Marketing für", h1b="Kanzleien", hero_label="Kanzlei-Motiv (Violett)",
 hero_lead='Website, Auftritt, Content &amp; Recruiting –<br>alles mit einem Ansprechpartner.<br>Damit deine Kanzlei modern wirkt und die<br>richtigen Mandanten &amp; Mitarbeiter dich finden.',
 intro_eyebrow="Warum Kanzleimarketing?", intro_h2="Seriös auftreten –<br>online wie auf Papier.",
 intro_img="Best Case · Kanzlei-Website (Violett) – Firefly folgt",
 intro_ps=[
  'Fachlich ist deine Kanzlei top – nur sieht man das online oft nicht. Mandanten und Bewerber googeln zuerst; wer nur eine veraltete Seite findet, ist schnell bei der Konkurrenz. Genau hier setzt <strong>Kanzleimarketing</strong> an: ein seriöser, einheitlicher Auftritt und eine moderne <a href="/leistungen#web">Website</a>, die Vertrauen schafft.',
  'Als deine Werbeagentur für Weiden und die Oberpfalz übernehme ich das komplett – von der <a href="/leistungen#branding">Marke</a> über Content zu Fachthemen bis zu <a href="/leistungen#social">Social Media und LinkedIn</a>. Du berätst deine Mandanten, ich kümmere mich um deinen Auftritt. Ein Ansprechpartner, alles aus einer Hand.',
  'Ob neue Website, frisches Erscheinungsbild oder eine Karriereseite gegen den Fachkräftemangel – du entscheidest, wie viel du abgibst. Ich sorge dafür, dass deine Kanzlei so professionell wirkt, wie sie arbeitet.'],
 leist_h2="Kanzleimarketing –<br>alles aus einer Hand.",
 leistungen=[
  ("Kanzlei-Auftritt &amp; Design",'Logo, Geschäftsausstattung, Briefbogen und Vorlagen – ein einheitliches, <a href="/leistungen#branding">seriöses Erscheinungsbild</a> über alle Dokumente und Kanäle.'),
  ("Kanzlei-Website &amp; Auffindbarkeit",'Eine moderne <a href="/leistungen#web">Website</a> mit sauberen SEO-Grundlagen, damit Mandanten dich finden – inkl. Texten, die Vertrauen schaffen statt Juristendeutsch.'),
  ("Content &amp; Fachthemen",'Recht- und Steuerthemen verständlich aufbereitet – Ratgeber, Merkblätter, Beiträge. Positioniert dich als Experte und bringt dich bei Google nach vorn.'),
  ("Social Media &amp; LinkedIn",'Redaktionsplan, Beiträge und <a href="/leistungen#social">Betreuung</a> – gerade LinkedIn ist für Kanzleien Gold wert. Du musst nicht selbst posten, ich halte deinen Auftritt am Leben.'),
  ("Recruiting &amp; Karriere",'Karriereseite, Stellenanzeigen und eine Arbeitgebermarke, die zu dir passt. Damit du im Fachkräftemangel nicht nur Mandate, sondern auch den richtigen Nachwuchs gewinnst.'),
  ("Print &amp; Kanzlei-Material",'Broschüren, Mandantenmappen, Visitenkarten und Kanzleischilder – <a href="/leistungen#print">Druck und Abwicklung</a> koordiniert, du bekommst das fertige Ergebnis.'),
  ("Beratung &amp; laufende Betreuung",'Manchmal fehlt nicht die Umsetzung, sondern der Plan. Ich bringe Struktur in dein <a href="/leistungen#marketing">Kanzlei-Marketing</a> und bin der Ansprechpartner übers Jahr.')],
 beisp_h2="So sieht Kanzleimarketing aus.", beisp_caps=["Kanzlei-Website","Geschäftsausstattung"],
 packs=PACK_KANZ, pack_note="für jede Kanzlei finden wir die passende Lösung. Auch ganz individuell.",
 ablauf_lead="Kein Angebots-Marathon, kein Fachchinesisch.<br>Du sagst mir, was ansteht – ich kümmere mich um den Rest.", steps=STEPS_GEN,
 lokal_h2="Deine Werbeagentur für Kanzleien<br>in Weiden &amp; der Oberpfalz.",
 lokal_img="Best Case · Karriere &amp; Stellenanzeige (Violett) – Firefly folgt",
 lokal_ps=[
  'Ob Anwaltskanzlei, Notariat, Steuerberatung oder Wirtschaftsprüfung – als Werbeagentur für Kanzleien kümmere ich mich um deinen kompletten Auftritt. Von Logo und Geschäftsausstattung über Website und Content bis zu Recruiting bekommst du Kanzleimarketing aus einer Hand.',
  'Ich sitze in Irchenrieth bei Weiden in der Oberpfalz und arbeite für Kanzleien in der ganzen Region – von Weiden über Neustadt und Tirschenreuth bis Amberg. Vieles läuft unkompliziert digital, auf Wunsch bin ich vor Ort. Über 20 Jahre Erfahrung sorgen für einen Auftritt, der Vertrauen schafft.',
  'Wie das aussieht, siehst du bei meinen <a href="/projekte">Referenzen</a>. Egal ob kompletter Relaunch oder behutsame Auffrischung – wir finden den Weg, der zu deiner Kanzlei und deinem Budget passt.'],
 faq_h2="Kanzleimarketing –<br>kurz &amp; ehrlich erklärt.",
 faq=[
  ("Ist Marketing für eine Kanzlei nicht unseriös?","Im Gegenteil – seriös heißt nicht unsichtbar. Es geht nicht um reißerische Werbung, sondern um einen professionellen, zurückhaltenden Auftritt, der Kompetenz zeigt. Genau das erwarten Mandanten heute, wenn sie eine Kanzlei suchen."),
  ("Wir haben schon eine Website – reicht das nicht?","Kommt drauf an. Ist sie modern, schnell und wird sie gefunden? Viele Kanzlei-Seiten sind technisch veraltet und bei Google unsichtbar. Ich prüfe deinen Auftritt ehrlich und frische ihn auf, statt alles neu zu machen."),
  ("Hilft Marketing bei der Personalgewinnung?","Absolut – für viele Kanzleien ist das inzwischen das größere Problem als neue Mandate. Mit einer klaren Arbeitgebermarke, guten Stellenanzeigen und einer Karriereseite findest du eher den richtigen Nachwuchs."),
  ("Muss ich mich um LinkedIn und Social Media selbst kümmern?","Nein. Gerade LinkedIn ist für Kanzleien wertvoll, kostet aber Zeit. Auf Wunsch übernehme ich Planung, Gestaltung und Betreuung komplett – du gibst nur ab und zu Input."),
  ("Kannst du auch Content zu Recht- und Steuerthemen erstellen?","Ja. Verständlich aufbereitete Fachthemen – als Ratgeber, Merkblatt oder Beitrag – positionieren dich als Experte und bringen dich bei Google nach vorn. Fachlich stimmst du zu, den Rest mache ich."),
  ("Arbeitest du auch für kleine Kanzleien in der Oberpfalz?","Klar. Vom Einzelanwalt bis zur größeren Sozietät – gerade kleinere Kanzleien profitieren von einem professionellen Auftritt. Ich sitze in Weiden bzw. Irchenrieth und bin für die ganze Oberpfalz da.")],
 kontakt_sub="Wir schauen gemeinsam, was zu deiner Kanzlei passt.",
 subj="Kanzlei", kampagne="Kanzlei (Recht &amp; Steuer)",
 opts=["Kompletter Auftritt (Logo, Website, Design)","Website oder Kanzlei-Auftritt","Recruiting &amp; Karriereseite","Social Media &amp; LinkedIn","Content &amp; Fachthemen"])

ges = dict(file="praxismarketing.html", bodyclass="kampagne-gesundheit", slug="praxismarketing",
 title="Praxismarketing Weiden | Werbeagentur DESIGNJ", seoname="Praxismarketing",
 desc="Praxismarketing aus Weiden: moderne Website, Patientenkommunikation und Personalgewinnung aus einer Hand – für Praxen, Kliniken und Pflegeeinrichtungen.",
 eyebrow="Praxismarketing · Weiden &amp; Oberpfalz", h1a="Marketing für", h1b="Praxen", hero_label="Gesundheit-Motiv (Türkis)",
 hero_lead='Website, Auftritt, Social Media &amp; Recruiting –<br>alles mit einem Ansprechpartner.<br>Damit deine Praxis modern wirkt und du<br>Patienten &amp; Fachkräfte gleichermaßen erreichst.',
 intro_eyebrow="Warum Praxismarketing?", intro_h2="Modern wirken –<br>für Patienten und Team.",
 intro_img="Best Case · Praxis-Website (Türkis) – Firefly folgt",
 intro_ps=[
  'Deine Arbeit ist wichtig – dein Auftritt sollte es auch sein. Patienten suchen ihre Praxis heute zuerst online, und Fachkräfte schauen genau hin, für wen sie arbeiten wollen. Wer nur eine veraltete Seite hat, verliert beide. Genau hier setzt <strong>Praxismarketing</strong> an: eine moderne <a href="/leistungen#web">Website</a> und ein einheitlicher, vertrauensvoller Auftritt.',
  'Als deine Werbeagentur für Weiden und die Oberpfalz übernehme ich das komplett – von der <a href="/leistungen#branding">Praxis-Marke</a> über Patienten-Infos bis zu <a href="/leistungen#social">Social Media</a> und Recruiting. Du kümmerst dich um Patienten, ich um deinen Auftritt. Ein Ansprechpartner, alles aus einer Hand.',
  'Ob neue Website, Praxis-Leitsystem oder eine Karriereseite gegen den Fachkräftemangel – du entscheidest, wie viel du abgibst. Ich sorge dafür, dass deine Praxis modern und einladend wirkt: für Patienten genauso wie für neue Kolleg:innen.'],
 leist_h2="Praxismarketing –<br>alles aus einer Hand.",
 leistungen=[
  ("Praxis-Website &amp; Auffindbarkeit",'Eine moderne <a href="/leistungen#web">Website</a> mit Online-Terminen, sauberen SEO-Grundlagen und verständlichen Texten. Damit Patienten dich finden – und nicht die Praxis nebenan.'),
  ("Recruiting &amp; Karriere",'Karriereseite, Stellenanzeigen und eine Arbeitgebermarke, die zu dir passt. Damit du gerade in der Pflege die Fachkräfte findest, die du wirklich brauchst.'),
  ("Praxis-Design &amp; Ausstattung",'Logo, Praxisschilder, Leitsystem, Formulare und Ausstattung – ein einheitlicher, <a href="/leistungen#branding">moderner Auftritt</a> vom Empfang bis zum Wartezimmer.'),
  ("Social Media &amp; Patienten-Infos",'Redaktionsplan, Beiträge und <a href="/leistungen#social">Betreuung</a> bei Instagram &amp; Facebook. Öffnungszeiten, Team und Leistungen – deine Praxis bleibt sichtbar und nahbar.'),
  ("Content &amp; Aufklärung",'Gesundheitsthemen verständlich aufbereitet – für Website, Social und Wartezimmer. Positioniert dich als kompetente, vertrauensvolle Anlaufstelle.'),
  ("Print &amp; Praxis-Material",'Flyer, Terminkarten, Aufklärungsbögen und Praxisschilder – <a href="/leistungen#print">Druck und Abwicklung</a> koordiniert, du bekommst das fertige Ergebnis.'),
  ("Beratung &amp; laufende Betreuung",'Manchmal fehlt nicht die Umsetzung, sondern der Plan. Ich bringe Struktur in dein <a href="/leistungen#marketing">Praxis-Marketing</a> und bin der Ansprechpartner übers Jahr.')],
 beisp_h2="So sieht Praxismarketing aus.", beisp_caps=["Praxis-Website","Praxis-Ausstattung &amp; Leitsystem"],
 packs=PACK_GES, pack_note="für jede Praxis finden wir die passende Lösung. Auch ganz individuell.",
 ablauf_lead="Kein Angebots-Marathon, kein Fachchinesisch.<br>Du sagst mir, was ansteht – ich kümmere mich um den Rest.", steps=STEPS_GEN,
 lokal_h2="Deine Werbeagentur für Praxen<br>in Weiden &amp; der Oberpfalz.",
 lokal_img="Best Case · Karriere &amp; Stellenanzeige (Türkis) – Firefly folgt",
 lokal_ps=[
  'Ob Arztpraxis, Zahnarzt, Physio, Klinik oder Pflegeeinrichtung – als Werbeagentur für Praxen kümmere ich mich um deinen kompletten Auftritt. Von Logo und Leitsystem über Website und Social Media bis zu Recruiting bekommst du Praxismarketing aus einer Hand.',
  'Ich sitze in Irchenrieth bei Weiden in der Oberpfalz und arbeite für Praxen und Einrichtungen in der ganzen Region – von Weiden über Neustadt und Tirschenreuth bis Amberg. Vieles läuft unkompliziert digital, auf Wunsch bin ich vor Ort. Über 20 Jahre Erfahrung sorgen für einen Auftritt, der Vertrauen schafft.',
  'Wie das aussieht, siehst du bei meinen <a href="/projekte">Referenzen</a>. Egal ob kompletter Relaunch oder behutsame Auffrischung – wir finden den Weg, der zu deiner Praxis und deinem Budget passt.'],
 faq_h2="Praxismarketing –<br>kurz &amp; ehrlich erklärt.",
 faq=[
  ("Dürfen Praxen überhaupt Werbung machen?","Ja – sachliche Information ist erlaubt und erwünscht. Es geht nicht um marktschreierische Werbung, sondern um einen modernen, informativen Auftritt: Website, Öffnungszeiten, Team und Leistungen. Genau das erwarten Patienten heute."),
  ("Wir haben eine ältere Website – muss die komplett neu?","Nicht unbedingt. Oft reicht eine Auffrischung: modernes Design, schnelle Ladezeit, Online-Termine und saubere Auffindbarkeit bei Google. Ich prüfe deinen Auftritt ehrlich und modernisiere, statt alles über den Haufen zu werfen."),
  ("Hilft Marketing wirklich bei der Personalsuche?","Gerade in Pflege und Gesundheit ist das oft das größte Thema. Mit einer klaren Arbeitgebermarke, guten Stellenanzeigen und echten Einblicken in dein Team findest du eher die Fachkräfte, die zu dir passen."),
  ("Übernimmst du auch die Social-Media-Betreuung?","Auf Wunsch komplett. Du bist bei den Patienten, nicht am Handy – ich plane, gestalte und betreue deine Kanäle. Team, Leistungen und Infos bleiben sichtbar, ohne dass du täglich selbst posten musst."),
  ("Kümmerst du dich auch um Schilder, Leitsystem und Formulare?","Ja. Vom Praxisschild über das Leitsystem bis zu Formularen und Terminkarten – ein einheitlicher Auftritt vom Empfang bis zum Wartezimmer, alles koordiniert und aus einer Hand."),
  ("Arbeitest du auch für kleine Praxen in der Oberpfalz?","Klar. Von der Einzelpraxis bis zur größeren Einrichtung – gerade kleinere Praxen profitieren von einem professionellen Auftritt. Ich sitze in Weiden bzw. Irchenrieth und bin für die ganze Oberpfalz da.")],
 kontakt_sub="Wir schauen gemeinsam, was zu deiner Praxis passt.",
 subj="Gesundheit", kampagne="Gesundheit (Praxen &amp; Pflege)",
 opts=["Kompletter Auftritt (Logo, Website, Praxis)","Website oder Praxis-Auftritt","Recruiting &amp; Karriereseite","Social Media &amp; Patienten-Infos","Praxis-Ausstattung &amp; Leitsystem"])

for cfg in (immo, kanz, ges):
    build(cfg); print(f"{cfg['file']} ✅")
print("fertig.")
