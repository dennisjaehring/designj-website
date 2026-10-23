# -*- coding: utf-8 -*-
# Inhaltsdaten fuer die 4 Service-Seiten (von _gen_service.py genutzt)
CK = '<svg class="mk" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M5 13l4 4L19 7"/></svg>'

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

def _cap(cap, client=""):
    cl = f'<span class="kmp-shot__client">{client}</span>' if client else ''
    return (f'<figcaption class="kmp-shot__cap">'
            f'<span class="kmp-shot__lbl"><span class="chev">»</span> {cap}</span>{cl}</figcaption>')

def shot(img, alt, cap, client="", delay=0, pos=""):
    d = f' data-delay="{delay}"' if delay else ''
    st = f' style="object-position:{pos}"' if pos else ''
    return f'''      <figure class="kmp-shot reveal"{d}>
        <img class="kmp-shot__media" src="images/referenzen/designj_referenz_{img}.webp" alt="{alt}" loading="lazy"{st}>
        {_cap(cap, client)}
      </figure>'''

def shot_src(src, alt, cap, client="", delay=0, logo=False):
    d = f' data-delay="{delay}"' if delay else ''
    mcls = "kmp-shot__media kmp-shot__media--logo" if logo else "kmp-shot__media"
    return f'''      <figure class="kmp-shot reveal"{d}>
        <img class="{mcls}" src="{src}" alt="{alt}" loading="lazy">
        {_cap(cap, client)}
      </figure>'''

def shot_logos(cap, items, client="", delay=0):
    d = f' data-delay="{delay}"' if delay else ''
    tiles = "\n".join(
        f'          <div class="kmp-logo"><img src="{src}" alt="{alt}" loading="lazy"></div>'
        for src, alt in items)
    return f'''      <figure class="kmp-shot kmp-shot--wide reveal"{d}>
        <div class="kmp-logos">
{tiles}
        </div>
        {_cap(cap, client)}
      </figure>'''

def shot_campaign(cap, client, posts, delay=0, zoom=False):
    d = f' data-delay="{delay}"' if delay else ''
    z = " kmp-feed--zoom" if zoom else ""
    tiles = "\n".join(
        f'          <span class="kmp-feed__cell"><img src="images/referenzen/designj_referenz_{p}.webp" alt="{alt}" loading="lazy"></span>'
        for p, alt in posts)
    return f'''      <figure class="kmp-shot kmp-shot--wide reveal"{d}>
        <div class="kmp-feed{z}">
{tiles}
        </div>
        {_cap(cap, client)}
      </figure>'''

def opts(lst):
    return "".join(f"<option>{o}</option>" for o in lst)

NOTE = 'Noch unsicher, was du brauchst?<br>Im Gespräch finde ich mit dir den passenden Umfang – du bekommst ein <strong>individuelles Angebot</strong>.'

PAGES = {}

PAGES["branding"] = dict(
    title="Branding, Logo & Grafikdesign Weiden | DESIGNJ",
    desc="Branding aus Weiden: Logo, Corporate Design und Styleguide aus einer Hand – damit deine Marke klar, einheitlich und wiedererkennbar auftritt.",
    eyebrow="Branding · Weiden &amp; Oberpfalz",
    h1='Eine Marke,<br>die <span class="accentword">hängen bleibt</span>.',
    lead="Logo, Farben, Schriften, Styleguide –<br>ich entwickle Markenidentitäten,<br>die zu dir passen und wiedererkennbar sind.<br>Vom ersten Entwurf bis zum fertigen<br>Brand Manual, aus einer Hand.",
    hero_img="sparkasse_oberpfalz_nord_01", hero_alt="Branding &amp; Logo-Design von DESIGNJ – Jubiläumslogo Sparkasse Oberpfalz Nord",
    intro_h2='Deine Marke –<br>klar auf den Punkt.',
    intro_paras=[
        "Deine Marke ist mehr als ein Logo – sie ist der erste Eindruck.<br>Ich entwickle ein Erscheinungsbild, das zu dir passt, überall<br>funktioniert und im Kopf bleibt.",
        "Vom Logo über Farben und Schriften bis zur kompletten<br>Geschäftsausstattung: Du bekommst einen <strong>einheitlichen,<br>wiedererkennbaren Auftritt</strong> –<br>aus einer Hand, mit einem Ansprechpartner.",
        "Auf Wunsch halte ich alles in einem Styleguide fest, damit deine<br>Marke überall gleich wirkt – egal, wer später damit arbeitet.",
    ],
    intro_img="rupprecht_kappl_01", intro_alt="Markenauftritt &amp; Geschäftsausstattung von DESIGNJ",
    pak_eyebrow="Pakete", pak_h2='Vom Logo bis zur<br>ganzen Markenwelt.',
    packs=[
        pack("Logo", "Der klare Startpunkt für deine Marke.", ["Logoentwicklung &amp; -design", "Varianten für jeden Einsatz", "Dateien für Print &amp; Web"]),
        pack("Corporate Design", "Einheitlich auf allen Materialien.", ["Logo + Farb- &amp; Schriftkonzept", "Geschäftsausstattung<br>(Visitenkarte, Briefpapier, Mappe)", "Durchgängiges Erscheinungsbild"], feat=True, delay=120),
        pack("Komplett-Branding", "Die ganze Markenwelt, dokumentiert.", ["Corporate Design +<br>Styleguide / Brand Manual", "Icon-Design &amp; Bildsprache", "Konzepte auch für Start-ups"], delay=240),
    ],
    pak_note=NOTE,
    net_h2='Das steckt in jedem<br>Branding von mir.', net_lead="Egal welches Paket – diese Grundlagen<br>sind immer an Bord.",
    net_items=["Durchdachtes Konzept", "Varianten zur Auswahl", "Dateien für Print &amp; Web", "Einheitliche Vorlagen", "Persönliche Beratung", "Ein fester Ansprechpartner"],
    abl_h2="Von der Idee zur<br>fertigen Marke.", abl_lead="Klarer Ablauf, kein Fachchinesisch.<br>Du erzählst mir, wofür deine Marke steht – um den Rest kümmere ich mich.",
    steps=[
        step("Gespräch &amp; Zielsetzung", "Wofür steht deine Marke, wen willst du erreichen? Ich kläre mit dir Ziel, Werte und Stil – unverbindlich."),
        step("Konzept &amp; Entwürfe", "Ich entwickle mehrere Richtungen und zeige dir, wie deine Marke aussehen kann.", 100),
        step("Feinschliff &amp; Umsetzung", "Ich verfeinere mit dir, bis es sitzt – bis zum fertigen Erscheinungsbild.", 200),
        step("Übergabe", "Du bekommst alle Dateien für Print &amp; Web, auf Wunsch mit Styleguide.", 300),
    ],
    ref_h2="Marken, die ich<br>gestaltet habe.", ref_lead="Eine Auswahl von Logos, Corporate Designs<br>und Markenauftritten aus der Region.",
    shots=[
        shot("hofladen_weiden_01", "Branding &amp; Verpackung Max-Reger Kaffee von DESIGNJ", "Branding &amp; Packaging", "Max-Reger Kaffee vom Hofladen, Weiden"),
        shot_src("images/kunden/designj_kunde_salzhausaltenstadt.webp", "Logo-Refresh Salzhaus Altenstadt Physiotherapie von DESIGNJ", "Logo-Refresh", "Salzhaus Altenstadt, Physiotherapie", delay=100, logo=True),
        shot_logos("Markenauftritt", [
            ("images/referenzen/designj_referenz_rupprecht_kappl_06.webp", "Markenlogo Dein Gartenkoi von DESIGNJ"),
            ("images/referenzen/designj_referenz_rupprecht_kappl_05.webp", "Markenlogo Dein Urlaubsboot von DESIGNJ"),
            ("images/referenzen/designj_referenz_rupprecht_kappl_04.webp", "Markenlogo Deine Gartenpalme von DESIGNJ"),
        ], client="Dein Gartenkoi · Dein Urlaubsboot · Deine Gartenpalme"),
    ],
    faq_h2='Branding –<br>kurz &amp; ehrlich erklärt.',
    faq=[
        ("Was kostet ein Logo?", "Die Kosten für ein Logo hängen vom Umfang ab – vom einzelnen Logo bis zum kompletten Branding. Erzähl mir dein Vorhaben, du bekommst ein individuelles Angebot."),
        ("Wie viele Entwürfe bekomme ich?", "Du bekommst mehrere durchdachte Logo-Richtungen zur Auswahl – danach verfeinere ich den Favoriten mit dir, bis er sitzt."),
        ("Bekomme ich alle Dateien?", "Ja – dein Logo von DESIGNJ in allen gängigen Formaten für Print und Web, auf Wunsch mit einem Styleguide."),
        ("Kannst du mein bestehendes Logo auffrischen?", "Ein bestehendes Logo frische ich beim Rebranding auf: Ich baue auf dem Bestehenden auf und bringe es behutsam auf ein aktuelles, einheitliches Niveau."),
        ("Was bringt mir ein Styleguide?", "Ein Styleguide hält Farben, Schriften und Regeln fest, damit deine Marke überall gleich wirkt – egal, wer gestaltet."),
        ("Machst du auch die Drucksachen dazu?", "Ja – Visitenkarten, Briefpapier und Co. gestalte und produziere ich gleich mit. Mehr dazu auf meiner Print-Seite."),
    ],
    k_h2="Lass uns über<br>deine Marke sprechen.", k_lead="Erzähl mir kurz dein Vorhaben – du bekommst eine ehrliche Einschätzung und ein individuelles Angebot.",
    k_subject="Neue Anfrage über Seite: Branding", k_herkunft="Seite: Branding",
    k_options=opts(["Logo", "Corporate Design", "Komplett-Branding", "Rebranding", "Nur ein unverbindliches Gespräch", "Ich bin noch nicht sicher"]),
)

PAGES["print-produktion"] = dict(
    title="Flyer, Schilder & Textildruck Weiden | DESIGNJ",
    desc="Print & Produktion aus Weiden: Flyer, Broschüren, Großformat, Fahrzeugbeschriftung, Textildruck & Werbemittel – gestaltet und produziert aus einer Hand.",
    eyebrow="Print &amp; Produktion · Weiden &amp; Oberpfalz",
    h1='Gestaltet, gedruckt, <span class="accentword">geliefert</span>.',
    lead="Von der Visitenkarte bis zur Fahrzeugflotte –<br>ich gestalte nicht nur, sondern kümmere mich<br>um die komplette Produktion.<br>Über mein Netzwerk an Druckereien und<br>Werbetechnik-Partnern, alles aus einer Hand.",
    hero_img="kurt_landauer_stiftung_01", hero_alt="Printprodukt von DESIGNJ – Magazin KURT!",
    intro_h2='Du bekommst das<br>Ergebnis, nicht<br>den Aufwand.',
    intro_paras=[
        "Gestaltung, Abstimmung mit Druckerei und<br>Werbetechnik, Koordination bis zur Lieferung –<br>ein Ansprechpartner für fast alles, was sich<br>bedrucken, bekleben oder beschriften lässt.",
        "Von der kleinen Drucksache über Großformat<br>und Werbetechnik bis zum Textildruck und<br>Werbemitteln: Ich bringe dein Design<br><strong>sauber auf das richtige Material</strong>.",
        "Dank meines Netzwerks an Partnern realisiere<br>ich auch besondere Wünsche – von Sonderfarben<br>bis zur fertigen Montage.",
    ],
    intro_img="spvgg_weiden_06", intro_alt="Printprodukt von DESIGNJ – SpVgg Weiden",
    pak_eyebrow="Was ich für dich produziere", pak_h2='Fast alles, was sich<br>bedrucken lässt.',
    packs=[
        pack("Drucksachen", "Alles für Papier &amp; Print.", ["Flyer, Broschüren, Folder, Kataloge", "Visitenkarten, Briefpapier, Blöcke, Mappen"]),
        pack("Großformat &amp; Außenwerbung", "Weithin sichtbar.", ["Plakate &amp; Großformatdruck", "Banner, Roll-Ups, Messesysteme", "Bauzaunwerbung"], delay=100),
        pack("Werbetechnik", "Bekleben &amp; beschriften.", ["Aufkleber &amp; Schilder", "Fahrzeugbeschriftung", "Schaufensterbeklebung"], delay=200),
        pack("Textildruck", "Deine Marke zum Anziehen.", ["T-Shirts, Hoodies, Trikots", "Team- &amp; Vereinskleidung"], delay=100),
        pack("Werbemittel &amp; Veredelung", "Das gewisse Extra.", ["Kugelschreiber, Tassen, Notizbücher", "Sonderfarben, Lackierungen, Prägungen"], delay=200),
    ],
    pak_note="Du brauchst etwas, das nicht dabei ist?<br><strong>Frag einfach</strong> – fast alles ist machbar.",
    net_h2='Das ist bei jedem<br>Print-Auftrag dabei.', net_lead="Gestaltung und Produktion laufen bei mir<br>zusammen – du hast nur einen Ansprechpartner.",
    net_items=["Gestaltung + Produktion<br>aus einer Hand", "Abstimmung mit<br>Druckerei &amp; Partnern", "Komplette Koordination", "Druckfertige Daten", "Starkes Partner-Netzwerk", "Ein fester Ansprechpartner"],
    abl_h2="Von der Idee<br>bis zur Lieferung.", abl_lead="Kein Aufwand für dich.<br>Du sagst mir, was du brauchst – ich kümmere mich um den Rest.",
    steps=[
        step("Gespräch &amp; Idee", "Du sagst mir, was du brauchst – von der einzelnen Drucksache bis zur Komplett-Ausstattung."),
        step("Gestaltung", "Ich gestalte dein Produkt passend zu deiner Marke und bereite es druckfertig auf.", 100),
        step("Produktion &amp; Koordination", "Ich stimme mit Druckerei und Werbetechnik ab und koordiniere die ganze Produktion.", 200),
        step("Lieferung / Montage", "Du bekommst das fertige Ergebnis geliefert – auf Wunsch inklusive Montage.", 300),
    ],
    ref_h2="Gedruckt &amp; produziert.", ref_lead="Eine Auswahl aus Drucksachen, Großformat,<br>Werbetechnik und Werbemitteln.",
    shots=[
        shot("autoservice_johnson_01", "Flyer von DESIGNJ – Autoservice Johnson", "Flyer &amp; Drucksachen", "Autoservice Johnson, Luhe"),
        shot("ravanna_wernberg_01", "Speisekarte von DESIGNJ – Ravenna Wernberg", "Speise- und Bestellkarten", "Restaurante Ravenna, Wernberg-Köblitz", delay=100),
        shot("friedmann_weiden_01", "Werbemittel von DESIGNJ – Friedmann", "Werbemittel", "Ing. Friedmann GmbH, Weiden"),
        shot("us_army_01", "Bauzaunbanner von DESIGNJ – U.S. Army Garrison", "Großformat &amp; Banner", "U.S. Army, Stützpunkt Hohenfels", delay=100),
    ],
    faq_h2='Print &amp; Produktion –<br>kurz &amp; ehrlich erklärt.',
    faq=[
        ("Was kostet ein Druckauftrag?", "Die Kosten für einen Druckauftrag hängen von Produkt, Menge und Veredelung ab. Sag mir, was du brauchst, du bekommst ein individuelles Angebot."),
        ("Kann ich auch Einzelstücke oder kleine Auflagen drucken lassen?", "Einzelstücke und kleine Auflagen sind kein Problem – ob ein einzelnes Schild oder 10.000 Flyer, beides geht."),
        ("Übernimmst du auch die Druckabwicklung?", "Die komplette Druckabwicklung übernehme ich: druckfertige Daten, Abstimmung mit der Druckerei und die ganze Koordination."),
        ("Machst du auch Fahrzeugbeschriftung inklusive Montage?", "Fahrzeugbeschriftung inklusive Montage läuft über mein Werbetechnik-Netzwerk in der Oberpfalz – Gestaltung, Produktion und Montage aus einer Hand."),
        ("Lieferst du auch Werbemittel?", "Werbemittel liefere ich ebenfalls – von Kugelschreibern über Tassen bis zu Textilien, bedruckt mit deinem Design."),
        ("Sind Veredelungen möglich?", "Veredelungen sind möglich – Sonderfarben, Lackierungen oder Prägungen geben deinen Drucksachen das gewisse Extra."),
    ],
    k_h2="Lass uns über dein<br>Druckprojekt sprechen.", k_lead="Sag mir, was du brauchst – du bekommst eine ehrliche Einschätzung und ein individuelles Angebot.",
    k_subject="Neue Anfrage über Seite: Print & Produktion", k_herkunft="Seite: Print & Produktion",
    k_options=opts(["Drucksachen", "Großformat &amp; Außenwerbung", "Werbetechnik", "Fahrzeugbeschriftung", "Textildruck", "Werbemittel", "Nur ein unverbindliches Gespräch", "Ich bin noch nicht sicher"]),
)

PAGES["social-media"] = dict(
    title="Social-Media-Design Weiden | DESIGNJ",
    desc="Social-Media-Design aus Weiden: Feed- & Story-Vorlagen, Content-Pakete und Anzeigen-Grafiken für einen einheitlichen Auftritt auf Instagram & Facebook.",
    eyebrow="Social Media · Weiden &amp; Oberpfalz",
    h1='Auf allen Kanälen<br><span class="accentword">wiedererkennbar</span>.',
    lead="Von der einzelnen Grafik bis zum kompletten<br>Content-Paket – ich sorge für einen<br>professionellen, einheitlichen Auftritt auf<br>Instagram, Facebook, LinkedIn &amp; Co.",
    hero_img="seisport_01", hero_alt="Social-Media-Visuals von DESIGNJ – SEI SPORT",
    intro_h2='Ein Look, der deine Marke<br>sofort erkennbar macht.',
    intro_paras=[
        "Ein konsistenter Look macht deine Marke auf<br>einen Blick erkennbar. Ich gestalte Vorlagen<br>und Content, die du leicht selbst nutzt –<br>oder fertig von mir bekommst.",
        "Feed- und Story-Vorlagen, Profilbilder,<br>Werbeanzeigen-Grafiken: Dein Auftritt wirkt auf<br><strong>jedem Kanal einheitlich und professionell</strong>.",
        "Du willst nicht nur Vorlagen, sondern laufende<br>Betreuung und Planung? Das übernehme ich über<br>mein Angebot <a href=\"/marketing-betreuung\">Marketing &amp; Betreuung</a>.",
    ],
    intro_img="blue_devils_weiden_04", intro_alt="Social-Media-Design von DESIGNJ – Blue Devils Weiden",
    pak_eyebrow="Pakete", pak_h2='Von der Vorlage bis<br>zur fertigen Kampagne.',
    packs=[
        pack("Vorlagen-Set", "Einheitlicher Look, den du selbst bespielst.", ["Feed- &amp; Story-Templates", "Profil- &amp; Headerbilder", "Leicht selbst befüllbar"]),
        pack("Content-Paket", "Fertiger Content, bereit zum Posten.", ["Fertige Grafiken &amp; Posts im Set", "Auf deine Themen abgestimmt", "Einheitlich über alle Kanäle"], feat=True, delay=120),
        pack("Ads &amp; Kampagnen", "Auffällige Grafiken für deine Kampagnen.", ["Werbeanzeigen (Meta, Instagram, LinkedIn)", "Google-Ads-Banner", "Digitale Flyer &amp; PDF-Flyer"], delay=240),
    ],
    pak_note=NOTE,
    net_h2='Das steckt in jedem<br>Social-Media-Auftritt.', net_lead="Egal welches Paket – diese Grundlagen<br>sind immer dabei.",
    net_items=["Einheitlicher Marken-Look", "Formate für alle Kanäle", "Leicht selbst nutzbar", "Profil- &amp; Headerbilder", "Auf Wunsch Newsletter-/Signatur-Vorlagen", "Ein fester Ansprechpartner"],
    abl_h2="Von der Idee zum<br>fertigen Feed.", abl_lead="Klarer Ablauf, kein Fachchinesisch.<br>Du sagst mir, wo du hin willst – ich gestalte den Look.",
    steps=[
        step("Gespräch &amp; Zielsetzung", "Welche Kanäle, welche Themen, welcher Look? Ich kläre mit dir, was zu dir passt – unverbindlich."),
        step("Look &amp; Konzept", "Ich entwickle einen einheitlichen Stil für deinen Auftritt auf allen Kanälen.", 100),
        step("Umsetzung", "Ich gestalte Vorlagen und Content – fertig zum Posten oder zum Selbstbefüllen.", 200),
        step("Übergabe", "Du bekommst alles sauber aufbereitet – auf Wunsch kümmere ich mich laufend weiter.", 300),
    ],
    ref_h2="Social Media, das auffällt.", ref_lead="Ein Blick in Social-Media-Auftritte,<br>die ich laufend mit Content bespiele.",
    shots=[
        shot_campaign("Social-Media-Kampagne", "Automobile Höcht, Mitterteich", [
            ("automobile_hoecht_social_01", "Social-Media-Posting von DESIGNJ – Automobile Höcht"),
            ("automobile_hoecht_social_02", "Social-Media-Posting von DESIGNJ – Automobile Höcht"),
            ("automobile_hoecht_social_03", "Social-Media-Posting von DESIGNJ – Automobile Höcht"),
            ("automobile_hoecht_social_04", "Social-Media-Posting von DESIGNJ – Automobile Höcht"),
        ]),
        shot_campaign("Event-Postings", "Club #Hashtag, Weiden", [
            ("club_hashtag_social_01", "Event-Posting von DESIGNJ – Club Hashtag Weiden"),
            ("club_hashtag_social_02", "Event-Posting von DESIGNJ – Club Hashtag Weiden"),
            ("club_hashtag_social_03", "Event-Posting von DESIGNJ – Club Hashtag Weiden"),
            ("club_hashtag_social_04", "Event-Posting von DESIGNJ – Club Hashtag Weiden"),
        ], delay=100, zoom=True),
        shot_campaign("DESIGNJ – mein eigener Social-Auftritt", "", [
            ("designj_social_01", "Social-Media-Posting von DESIGNJ – Marketing fürs Handwerk"),
            ("designj_social_02", "Social-Media-Posting von DESIGNJ – Marketing für den Sport"),
            ("designj_social_03", "Social-Media-Posting von DESIGNJ – Marketing für Immobilien"),
            ("designj_social_04", "Social-Media-Posting von DESIGNJ – Marketing für Kanzleien"),
            ("designj_social_05", "Social-Media-Posting von DESIGNJ – Marketing für Praxen"),
            ("designj_social_06", "Social-Media-Posting von DESIGNJ – Marketing auslagern"),
            ("designj_social_07", "Social-Media-Posting von DESIGNJ – Design, Druck, Digital"),
            ("designj_social_08", "Social-Media-Posting von DESIGNJ – Saison-Motiv"),
        ], delay=200),
    ],
    faq_h2='Social Media –<br>kurz &amp; ehrlich erklärt.',
    faq=[
        ("Was kostet Social-Media-Design?", "Die Kosten für Social-Media-Design hängen vom Umfang ab – von einzelnen Vorlagen bis zum kompletten Content-Paket. Du bekommst ein individuelles Angebot."),
        ("Kann ich die Vorlagen selbst bearbeiten?", "Die Vorlagen kannst du selbst bearbeiten – ganz ohne Designprogramm leicht befüllen und immer wieder nutzen."),
        ("Übernimmst du auch das Posten und die laufende Betreuung?", "Das Posten und die laufende Betreuung übernehme ich auf Wunsch – über mein Angebot Marketing und Betreuung."),
        ("Für welche Plattformen gestaltest du?", "Bei DESIGNJ gestalte ich für Instagram, Facebook, LinkedIn und Co. – in den passenden Formaten für jeden Kanal."),
        ("Machst du auch Werbeanzeigen-Grafiken?", "Werbeanzeigen-Grafiken mache ich auch – für Meta-, Instagram- und LinkedIn-Ads sowie Google-Ads-Banner."),
        ("Bekomme ich ein einheitliches Design über alle Kanäle?", "Ein einheitliches Design über alle Kanäle ist genau das Ziel: ein konsistenter Look, der deine Marke überall wiedererkennbar macht."),
    ],
    k_h2="Lass uns über<br>deinen Social-Auftritt sprechen.", k_lead="Erzähl mir kurz dein Vorhaben – du bekommst eine ehrliche Einschätzung und ein individuelles Angebot.",
    k_subject="Neue Anfrage über Seite: Social Media", k_herkunft="Seite: Social Media",
    k_options=opts(["Vorlagen-Set", "Content-Paket", "Werbeanzeigen-Grafiken", "Komplettes Social-Media-Design", "Nur ein unverbindliches Gespräch", "Ich bin noch nicht sicher"]),
)

PAGES["marketing-betreuung"] = dict(
    title="Marketing & Betreuung Weiden | DESIGNJ",
    desc="Marketing & laufende Betreuung aus Weiden: Kampagnenplanung, Social-Media-Betreuung, Content-Planung und Websitepflege – ein fester Ansprechpartner übers Jahr.",
    eyebrow="Marketing &amp; Betreuung · Weiden &amp; Oberpfalz",
    h1='Marketing,<br>das <span class="accentword">dranbleibt</span>.',
    lead="Gutes Marketing hört nicht nach dem ersten<br>Entwurf auf. Ich plane voraus, setze um<br>und bleibe dran – von der Kampagne bis zur<br>laufenden Betreuung deiner Kanäle.",
    hero_img="blue_devils_weiden_01", hero_alt="Marketing &amp; Betreuung von DESIGNJ – Blue Devils Weiden",
    intro_h2='Ein Ansprechpartner,<br>der mitdenkt.',
    intro_paras=[
        "Ein fester Ansprechpartner, der vorausdenkt:<br>Kampagnen, Content-Planung, laufende Betreuung –<br>damit dein Auftritt kontinuierlich läuft, ohne<br>dass du selbst ständig dran denken musst.",
        "Du entscheidest, wie viel du abgibst – von einzelnen<br>Aufgaben bis zur kompletten Betreuung über das Jahr.<br><strong>Flexibel statt starrem Vertrag.</strong>",
        "Die Erstellung von Design und Grafiken findest<br>du auf meinen Seiten <a href=\"/social-media\">Social Media</a> und<br><a href=\"/branding\">Branding</a> – hier geht es ums <strong>Dranbleiben</strong>.",
    ],
    intro_img="seisport_fussballcamp_02", intro_alt="Laufende Marketing-Betreuung von DESIGNJ – SEI SPORT",
    pak_eyebrow="Pakete", pak_h2='Vom Einzelprojekt<br>bis Rundum-Betreuung.',
    packs=[
        pack("Einzelprojekt", "Eine Idee, sauber umgesetzt.", ["Kampagnenplanung &amp; Umsetzung", "Für einen konkreten Anlass", "Klarer Rahmen, klares Ergebnis"]),
        pack("Laufende Betreuung", "Dein Auftritt läuft, ohne Leerlauf.", ["Social-Media-Betreuung", "Content- &amp; Redaktionsplan", "Websitepflege &amp; Updates"], feat=True, delay=120),
        pack("Rundum-Paket", "Marketing komplett ausgelagert.", ["Alles aus laufender Betreuung", "Newsletter &amp; Infografiken", "Performance-Optimierung"], delay=240),
    ],
    pak_note=NOTE,
    net_h2='Das hast du bei<br>laufender Betreuung.', net_lead="Ein fester Partner, der plant,<br>umsetzt und dranbleibt.",
    net_items=["Fester Ansprechpartner", "Vorausschauende Planung", "Redaktionsplan", "Ehrliche Einschätzung", "Flexibel statt starrem Vertrag", "Abstimmung über alle Kanäle"],
    abl_h2="Planen. Umsetzen.<br>Dranbleiben.", abl_lead="Kein Chaos, kein Hinterherlaufen.<br>Du sagst mir, wo es hingeht – ich halte deinen Auftritt am Laufen.",
    steps=[
        step("Kennenlernen", "Du erzählst mir, wo du stehst und wo Marketing liegen bleibt – unverbindlich."),
        step("Plan &amp; Strategie", "Ich plane voraus: Kampagnen, Content und einen klaren Fahrplan übers Jahr.", 100),
        step("Umsetzung", "Ich setze um – Grafiken, Posts, Kampagnen, Pflege – alles aus einer Hand.", 200),
        step("Dranbleiben", "Auf Wunsch bleibe ich dein fester Ansprechpartner und halte deinen Auftritt am Laufen.", 300),
    ],
    ref_h2="Langfristig betreut.", ref_lead="Eine Auswahl an Kunden, die ich<br>über das Jahr begleite.",
    shots=[
        shot("hofladen_weiden_02", "Laufende Betreuung von DESIGNJ – Hofladen Weiden", "Laufende Betreuung", "Hofladen, Weiden"),
        shot("seisport_02", "Content &amp; Kampagnen von DESIGNJ – SEI SPORT", "Content &amp; Kampagnen", "SEI SPORT, Tegernsee", delay=100, pos="top"),
        shot("hohpe_03", "Content &amp; Werbung von DESIGNJ – Hohpe Weiden", "Content &amp; Werbung", "Hohpe, Weiden"),
        shot("bike_station_mitterteich_04", "Online &amp; Offline von DESIGNJ – Bike Station Mitterteich", "Online &amp; Offline", "Bike Station, Mitterteich", delay=100),
    ],
    faq_h2='Marketing &amp; Betreuung –<br>kurz &amp; ehrlich erklärt.',
    faq=[
        ("Was kostet laufende Betreuung?", "Die Kosten für die laufende Betreuung bei DESIGNJ hängen vom Umfang ab – vom Einzelprojekt bis zum Rundum-Paket. Du bekommst ein individuelles Angebot."),
        ("Bin ich an einen langen Vertrag gebunden?", "Kein Zwang, flexibel projektweise oder laufend. Für die meisten ist eine laufende Pauschale am Ende die ruhigere und günstigere Lösung – Planung und Umsetzung laufen in einem festen Rahmen, statt in Einzelaufträgen."),
        ("Übernimmst du komplett oder nur einzelne Aufgaben?", "Komplett oder einzelne Aufgaben – beides geht. Du entscheidest, wie viel du abgibst, von einzelnen Aufgaben bis zur kompletten Betreuung."),
        ("Postest du auch selbst auf meinen Kanälen?", "Das Posten übernehme ich auf Wunsch selbst – inklusive laufender Pflege deiner Kanäle."),
        ("Pflegst du auch meine Website?", "Die Pflege deiner Website gehört dazu – Content-Updates und Aktualisierungen übernehme ich in der laufenden Betreuung."),
        ("Wie schnell kannst du loslegen?", "Loslegen kann ich in der Regel sofort – nach einem kurzen Gespräch geht es direkt los."),
    ],
    k_h2="Lass uns über dein<br>Marketing sprechen.", k_lead="Erzähl mir kurz, wo du stehst – du bekommst eine ehrliche Einschätzung und ein individuelles Angebot.",
    k_subject="Neue Anfrage über Seite: Marketing & Betreuung", k_herkunft="Seite: Marketing & Betreuung",
    k_options=opts(["Einzelprojekt", "Laufende Betreuung", "Rundum-Paket", "Nur ein unverbindliches Gespräch", "Ich bin noch nicht sicher"]),
)
