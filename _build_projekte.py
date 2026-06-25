#!/usr/bin/env python3
# Generator für DESIGNJ Projekt-Detailseiten (nach Johnson-/Blue-Devils-Muster)
import os, time, urllib.request
from urllib.parse import urlparse

ROOT = os.path.dirname(os.path.abspath(__file__))
IMGDIR = os.path.join(ROOT, "images", "referenzen")
os.makedirs(IMGDIR, exist_ok=True)

# ---- Reihenfolge aller Projekte (für Vor/Zurück-Navigation) ----
ORDER = [
    "autoservice-johnson", "blue-devils", "dj-dollar-bill", "friedmann",
    "hofladen-weiden", "hohpe", "onz", "rupprecht-kappl", "sezayi-er",
    "spvgg-schirmitz", "spvgg-weiden", "us-army", "caraservice", "sei-sport",
    "djk-irchenrieth", "sparkasse-oberpfalz-nord", "bike-station",
    "zimmer-nr-zwei", "nele-und-hannes-ocik", "kurt-landauer-stiftung",
    "salzhaus-altenstadt", "ravenna-wernberg", "voit", "12ender",
]
def pfile(slug): return f"projekt-{slug}.html"

U = "https://www.designj.de/wp-content/uploads/2025/12/"

# ---- Projektdaten ----
P = {}
P["dj-dollar-bill"] = dict(
    name="DJ DOLLAR BILL", bc="DJ DOLLAR BILL",
    title="DJ DOLLAR BILL – Eventlayouts & Werbemittel | DESIGNJ",
    desc="Plakate, Flyer, Tickets und Banner für die Events von DJ DOLLAR BILL – ein einheitlicher, kreativer Look von DESIGNJ, Werbeagentur Weiden.",
    eyebrow="Projekt · Event & Print",
    h1="DJ DOLLAR BILL –<br>Eventlayouts & Werbemittel<br>für Hip-Hop-Veranstaltungen",
    lead="Plakate, Flyer, Tickets & Banner – ein einheitlicher Look für Events in ganz Bayern.",
    intro="Seit rund 20 Jahren gestalte ich für DJ DOLLAR BILL alle Layouts für seine Events in Clubs in Bayern und teilweise deutschlandweit. Dazu gehören Plakate, Flyer, Eintrittskarten und Bauzaunbanner, die einen einheitlichen, kreativen Look haben und die Events professionell präsentieren. Die Arbeit umfasst sowohl die grafische Gestaltung als auch die Umsetzung der Werbemittel, sodass die Marke DJ DOLLAR BILL bei Fans, Partnern und Veranstaltern einen hohen Wiedererkennungswert hat.",
    tags=["Eventlayout", "Print", "Plakate", "Flyer", "Werbetechnik"],
    main=[U+"designj_referenz_dj_dollar_bill_01.webp"],
    blocks=[dict(h="Hip Hop BBQ – Social Media & Drucksachen<br>für die eigene Eventreihe",
                 t="Für die Eventreihe „Hip Hop BBQ“ erstelle ich alle Layouts für Social Media und Drucksachen. Flyer, Plakate und Posts werden einheitlich gestaltet, um die Eventreihe modern, aufmerksamkeitsstark und professionell zu präsentieren – lokal, regional und deutschlandweit.",
                 imgs=[U+"designj_referenz_dj_dollar_bill_02.webp", U+"designj_referenz_dj_dollar_bill_03.webp", U+"designj_referenz_dj_dollar_bill_04.webp"])],
)
P["friedmann"] = dict(
    name="Ing. Carl Friedmann", bc="Friedmann",
    title="Carl Friedmann – Fahrzeugbeklebung & Werbeartikel | DESIGNJ",
    desc="Fahrzeugbeklebung, Bauzaunwerbung und Werbeartikel für die Ing. Carl Friedmann GmbH & Co KG in Weiden – konsistenter Markenauftritt von DESIGNJ.",
    eyebrow="Projekt · Werbetechnik & Print",
    h1="Ing. Carl Friedmann GmbH &amp; Co KG –<br>Visitenkarten, Fahrzeugbeklebung,<br>Bauzaunwerbung &amp; Werbeartikel",
    lead="Fahrzeugbeklebung, Bauzaunwerbung und Werbeartikel – ein konsistenter Auftritt aus einer Hand.",
    intro="Für die Ing. Carl Friedmann GmbH & Co KG, ein Unternehmen im gebäudetechnischen Anlagenbau und der Lüftungstechnik, betreue ich seit Jahren alle grafischen Projekte. Dazu gehören Layouts für Bauzaunwerbung, Fahrzeugbeklebungen und Stellenanzeigen, die den professionellen Auftritt des Unternehmens unterstreichen. Regelmäßig werden zudem Werbeartikel wie Lanyards, Zollstöcke, Gummibärchen, Kalender und weitere Giveaways gestaltet und umgesetzt. Durch die Kombination aus Grafik, Druck und Umsetzung entsteht ein konsistenter Markenauftritt, der das Unternehmen vor Kunden, Partnern und auf Veranstaltungen sichtbar macht.",
    tags=["Fahrzeugbeklebung", "Bauzaunwerbung", "Werbeartikel", "Print", "Visitenkarten"],
    main=[U+"designj_referenz_friedmann_weiden_01.webp", U+"designj_referenz_friedmann_weiden_02.webp"],
    blocks=[],
)
P["hofladen-weiden"] = dict(
    name="Hofladen Weiden", bc="Hofladen Weiden",
    title="Hofladen Weiden – Regionales Design & Packaging | DESIGNJ",
    desc="Etiketten, Flyer, Plakate und das Packaging-Design für Max Reger Kaffee – regionales Design für den Hofladen Weiden von DESIGNJ.",
    eyebrow="Projekt · Branding & Packaging",
    h1="Hofladen Weiden –<br>Regionales Design für<br>hochwertige Produkte",
    lead="Vom Etikett bis zum Packaging – ein Design, das Regionalität erlebbar macht.",
    intro="Der Hofladen Weiden steht für Regionalität, Qualität und echte Handwerkskunst – und genau das spiegelt sich auch in den vielen grafischen Projekten wider, die ich für das Team umsetzen durfte. Seit unserer Zusammenarbeit gestalte ich verschiedenste Layout- und Drucksachen rund um das Sortiment: von Produktetiketten und Flyern über Plakate bis hin zu Infomaterialien und saisonalen Werbemitteln. Mein Anspruch dabei: ein visuelles Erscheinungsbild, das den Charakter des Hofladens transportiert – natürlich, ehrlich und mit viel Liebe zum Detail. So entstehen Designs, die regionale Produkte nicht nur präsentieren, sondern erlebbar machen.",
    tags=["Branding", "Packaging", "Etiketten", "Print"],
    main=[U+"designj_referenz_hofladen_weiden_02.webp", U+"designj_referenz_hofladen_weiden_03.webp", U+"designj_referenz_hofladen_weiden_04.webp", U+"designj_referenz_hofladen_weiden_05.webp"],
    blocks=[dict(h="Max Reger Kaffee – Verpackungsdesign mit regionalem Charakter",
                 t="Ein besonderes Herzensprojekt war die grafische Umsetzung des Max Reger Kaffee – einer eigenen, hochwertigen Kaffeelinie mit starkem Bezug zur Stadt Weiden. Hier durfte ich das komplette Packaging-Design sowie das visuelle Konzept entwickeln: moderne Gestaltung, ein klarer lokaler Bezug und eine hochwertige Optik, die dem Premiumprodukt gerecht wird. Das Ziel: ein Design, das Tradition, Regionalität und moderne Produktgestaltung miteinander verbindet.",
                 imgs=[U+"designj_referenz_hofladen_weiden_01.webp"])],
)
P["hohpe"] = dict(
    name="HOHPE", bc="HOHPE",
    title="HOHPE – Drucksachen & Werbemittel für Gesundheit & Fitness | DESIGNJ",
    desc="Gutscheine, Banner, Werbemittel und Web für HOHPE aus den Bereichen Gesundheit, Wellness und Fitness in Weiden – von DESIGNJ.",
    eyebrow="Projekt · Print & Werbemittel",
    h1="HOHPE – Layouts, Drucksachen &amp; Werbemittel für Gesundheit, Wellness &amp; Fitness",
    lead="Drucksachen, Werbemittel und Web – ein stimmiger Auftritt für Gesundheit & Fitness.",
    intro="Für HOHPE, ein Unternehmen aus den Bereichen Gesundheit, Wellness und Fitness, gestalte ich vielfältige Layouts für Drucksachen wie Gutscheine, Weihnachtskarten, Banner und weitere Materialien. Außerdem betreue ich regelmäßig Werbemittel, darunter Event-Armbänder, Lippenpflege-Stifte, Kugelschreiber und andere Giveaways, die das Unternehmen professionell und einheitlich präsentieren. So entsteht ein stimmiger Markenauftritt, der HOHPE sowohl vor Ort als auch bei Kunden sichtbar macht.",
    tags=["Layout", "Print", "Werbemittel", "Web"],
    main=[U+"designj_referenz_hohpe_01.webp", U+"designj_referenz_hohpe_02.webp", U+"designj_referenz_hohpe_03.webp", U+"designj_referenz_hohpe_04.webp", U+"designj_referenz_hohpe_05.webp"],
    blocks=[dict(h="Physiopraxis Seeblick – Flyer & Website für das neue Projekt in Weiherhammer",
                 t="Für die neue Physiopraxis Seeblick, gelegen in Weiherhammer im BHS-Gebäude, übernehme ich die Gestaltung von Flyern und der gesamten Website. Ziel ist ein moderner, professioneller und einheitlicher Auftritt, der die Praxis optimal präsentiert und die Sichtbarkeit bei Patienten steigert.",
                 imgs=[U+"Bildschirmfoto-2025-12-11-um-15.39.48.png"])],
)
P["onz"] = dict(
    name="ONZ", bc="ONZ",
    title="ONZ – Dezente Fahrzeugbeklebung für Orthopädie & Chirurgie | DESIGNJ",
    desc="Dezente, stilvolle Fahrzeugbeklebung für das ONZ Fachzentrum für Orthopädie, Unfallchirurgie und Chirurgie in Weiden – von DESIGNJ.",
    eyebrow="Projekt · Fahrzeugbeklebung",
    h1="Oberpfalz Nord Zentrum –<br>Dezente Fahrzeugbeklebung für<br>Orthopädie &amp; Chirurgie in Weiden",
    lead="Dezente Fahrzeugbeklebung, die Seriosität<br>bewahrt und die Marke sichtbar macht.",
    intro="Für das ONZ Fachzentrum für Orthopädie, Unfallchirurgie und Chirurgie in Weiden wurden die Fahrzeuge dezent und stilvoll beklebt. Das Ziel bestand darin, den seriösen Charakter des Fachzentrums zu bewahren und gleichzeitig die Markenpräsenz unterwegs zu erhöhen. So entsteht ein professioneller, wiedererkennbarer Markenauftritt, der das Fachzentrum vor Ort und mobil sichtbar macht.",
    tags=["Fahrzeugbeklebung", "Werbetechnik"],
    main=[U+"designj_referenz_onz_weiden_01.webp", U+"designj_referenz_onz_weiden_02.webp", U+"designj_referenz_onz_weiden_03.webp"],
    blocks=[],
)
P["rupprecht-kappl"] = dict(
    name="Rupprecht & Kappl", bc="Rupprecht & Kappl",
    title="Rupprecht & Kappl – Logo, Drucksachen & Werbemittel | DESIGNJ",
    desc="Logos, Drucksachen und Werbetechnik für die Rupprecht & Kappl GmbH und den Club Hashtag in Weiden – konsistentes Branding von DESIGNJ.",
    eyebrow="Projekt · Branding & Werbetechnik",
    h1="Rupprecht &amp; Kappl GmbH – Logo, Drucksachen &amp; Werbemittel für Immobilien, Freizeit &amp; Gastronomie",
    lead="Logos, Drucksachen und Werbetechnik für mehrere Marken – konsistent über alle Bereiche.",
    intro="Seit über 10 Jahren betreue ich die Rupprecht & Kappl GmbH und ihre verschiedenen Marken. Logos wurden überarbeitet und ein einheitliches Design für unterschiedliche Geschäftsbereiche entwickelt. Ich gestalte alle Drucksachen und Layouts sowie diverse Werbemittel für RK Immobilienmakler und andere Firmenbereiche, sodass die unterschiedlichen Unternehmen professionell und konsistent auftreten.",
    tags=["Logo", "Branding", "Print", "Werbetechnik"],
    main=[U+f"designj_referenz_rupprecht_kappl_0{i}.webp" for i in range(1,7)],
    main_cols=3,
    blocks=[dict(h="Club Hashtag – Eventgrafiken & Werbetechnik für Weidener Club",
                 t="Nach der Übernahme und Wiedereröffnung betreue ich auch den Club Hashtag in Weiden. Ich erstelle alle Eventgrafiken, Drucksachen<br>und die Werbetechnik, sodass der Club visuell stark auftritt und Events aufmerksamkeitsstark beworben werden.",
                 imgs=[])],
)
P["sezayi-er"] = dict(
    name="SEZAYI ER", bc="SEZAYI ER",
    title="SEZAYI ER – Gestaltung für Telekom Shops & Tiny Houses | DESIGNJ",
    desc="Geschäftsausstattung, Drucksachen und Werbetechnik für die SE Center Telekom Shops und SEZI HOMES (Tiny Houses) in Weiden – von DESIGNJ.",
    eyebrow="Projekt · Branding & Print",
    h1="SEZAYI ER –<br>Gestaltung &amp; Drucksachen für<br>Telekom Shops und Tiny Houses",
    lead="Zwei Geschäftsbereiche, ein professioneller Auftritt – von Telekom Shops bis Tiny Houses.",
    intro="Seit 13 Jahren begleite ich SEZAYI ER in allen grafischen Belangen. Die langjährige Zusammenarbeit ermöglicht es, Projekte für die beiden Geschäftsbereiche individuell und professionell umzusetzen.",
    tags=["Branding", "Print", "Geschäftsausstattung", "Werbetechnik"],
    main=[],
    blocks=[
        dict(h="SE Center – Telekom Shops",
             t="Für die Telekom Shops SE Center gestalte ich Layouts für Banner, Roll-Ups, Flyer und Stempel sowie die Geschäftsausstattung wie Briefumschläge und Visitenkarten. So entsteht ein konsistenter und professioneller Auftritt, der die Shops vor Ort und bei Kunden sichtbar macht.",
             imgs=[U+f"designj_referenz_sezi_telekom_0{i}.webp" for i in range(1,4)]),
        dict(h="SEZI HOMES – Tiny Houses",
             t="Für SEZI HOMES, spezialisiert auf Tiny Houses, übernehme ich die Gestaltung aller Drucksachen, Banner, Roll-Ups sowie die komplette Geschäftsausstattung. Ziel ist ein moderner, ansprechender und einheitlicher Markenauftritt, der potenziellen Kunden die Qualität und Professionalität des Projekts vermittelt.",
             imgs=[U+f"designj_referenz_sezi_sezi_homes_0{i}.webp" for i in range(1,5)]),
    ],
    quote=dict(text="Sehr professionelle und kreative Zusammenarbeit! Dennis hat meine Vorstellungen perfekt umgesetzt und mit eigenen Ideen bereichert.",
               name="Sezayi Er", role="Unternehmer", logo="images/kunden/designj_kunde_sezihomes.webp", photo="images/kunden/designj_kundenstimme_sezayier.webp"),
)
P["spvgg-schirmitz"] = dict(
    name="SpVgg Schirmitz", bc="SpVgg Schirmitz",
    title="SpVgg Schirmitz – Drucksachen & Maskottchen „Drache Sigi“ | DESIGNJ",
    desc="Banner, Fahnen, Beklebungen und das Maskottchen „Drache Sigi“ für die SpVgg Schirmitz – Engagement und Design von DESIGNJ.",
    eyebrow="Projekt · Sport & Print",
    h1="SpVgg Schirmitz –<br>Drucksachen &amp; Engagement<br>für den Fußballverein",
    lead="Drucksachen, Werbetechnik und ein<br>eigenes Maskottchen für den Nachwuchs.",
    intro="Für die SpVgg Schirmitz, einen Fußballverein in der Bezirksliga Oberpfalz Nord, gestalte ich vielfältige Drucksachen wie Banner, Fahnen und Beklebungen. Darüber hinaus unterstütze ich den Verein durch Sponsoring in Form von Bandenwerbung und leiste soziales Engagement für den Jugendbereich, um den Nachwuchs aktiv zu fördern. So entsteht ein einheitlicher und professioneller Auftritt, der die Präsenz des Vereins vor Ort stärkt und gleichzeitig die Identifikation der Mitglieder und Fans unterstützt.",
    tags=["Print", "Werbetechnik", "Maskottchen", "Sponsoring"],
    main=[U+"designj_referenz_spvgg_schirmitz_01.webp", U+"designj_referenz_spvgg_schirmitz_02.webp"],
    blocks=[dict(h="„Drache Sigi“ – Maskottchen für die Jugendabteilung",
                 t="Ein besonderes Projekt war die Entwicklung des neuen Maskottchens „Drache Sigi“ in Zusammenarbeit mit der Jugendabteilung. Ich habe ein eigenes Logo und verschiedene Posen erstellt sowie Werbemittel wie Fahnen, Buntstifte und Banner gestaltet. Das Maskottchen macht die Jugendarbeit des Vereins sichtbar und schafft eine spielerische Identität für die jungen Mitglieder.",
                 imgs=[U+"designj_referenz_spvgg_schirmitz_03.webp", U+"designj_referenz_spvgg_schirmitz_04.webp", U+"designj_referenz_spvgg_schirmitz_05.webp"])],
)
P["spvgg-weiden"] = dict(
    name="SpVgg Weiden", bc="SpVgg Weiden",
    title="SpVgg Weiden – Spieltagsheft „Wasserwerk Echo“ | DESIGNJ",
    desc="Gestaltung des Spieltagshefts „Wasserwerk Echo“ für die SpVgg Weiden in der Bayernliga Nord – von DESIGNJ, Werbeagentur Weiden.",
    eyebrow="Projekt · Sport & Print",
    h1="SpVgg Weiden –<br>Spieltagsheft „Wasserwerk Echo“<br>in der Bayernliga Nord",
    lead="Alle zwei Wochen zum Heimspiel – mit Tabellen, Gegner-Infos, Spielberichten und Kader.",
    intro="Seit 2018 begleite ich die SpVgg Weiden, einen Fußballverein in der Bayernliga Nord, mit der Gestaltung des Spieltagshefts „Wasserwerk Echo“. Das Heft enthält aktuelle Statistiken, Infos zu den Heimspielen und Hintergrundinformationen zu den Gegnern und wird regelmäßig für die Fans erstellt. So entsteht ein professioneller, informativer und optisch ansprechender Auftritt, der die Vereinskommunikation unterstützt und den Fans einen hohen Mehrwert bietet.",
    tags=["Layout", "Print", "Spieltagsheft"],
    main=[U+f"designj_referenz_spvgg_weiden_0{i}.webp" for i in range(1,7)],
    main_cols=3,
    blocks=[],
)
P["us-army"] = dict(
    name="US ARMY Garrison Bavaria", bc="US ARMY",
    title="US ARMY Garrison Bavaria – Messe- & Eventausstattung | DESIGNJ",
    desc="Komplette Messe- und Eventausstattung, Werbetechnik und Drucksachen für die U.S. Army Garrison Bavaria in Hohenfels – von DESIGNJ.",
    eyebrow="Projekt · Messe & Werbetechnik",
    h1="US ARMY Garrison Bavaria – Messeausstattung, Werbetechnik &amp; Eventmaterial in Hohenfels",
    lead="Komplette Messe- und Eventausstattung<br>für einen hochwertigen, einheitlichen Auftritt.",
    intro="Für die U.S. Army Garrison Bavaria in Hohenfels, eine bedeutende US-Army-Garnison in Bayern, habe ich eine komplette Messe- und Eventausstattung umgesetzt. Dazu gehören Layouts und Drucksachen für Bauzaunbanner, Visitenkarten, Kugelschreiber, Pavillons, Tischhussen und Beachflags – alles abgestimmt auf die Anforderungen interner und externer Veranstaltungen.\n\nZiel war es, die professionelle Außenwirkung der Garnison zu stärken und sowohl bei offiziellen Events als auch bei internen Präsentationen ein einheitliches und hochwertiges Erscheinungsbild zu gewährleisten. So entsteht ein stimmiger und professioneller Markenauftritt – sichtbar, wiedererkennbar und effektiv bei allen Veranstaltungen.",
    tags=["Messeausstattung", "Werbetechnik", "Print", "Werbemittel"],
    main=[U+f"designj_referenz_us_army_0{i}.webp" for i in range(1,5)],
    blocks=[],
)
P["caraservice"] = dict(
    name="CaraService", bc="CaraService",
    title="CaraService – Messepaket, Drucksachen & Werbemittel | DESIGNJ",
    desc="Komplettes Messepaket aus Flyern, Gutscheinen, Roll-Ups und Square-Flags für die CaraService Holding GmbH an vier Standorten – von DESIGNJ.",
    eyebrow="Projekt · Messe & Print",
    h1="CaraService Holding GmbH – Messepaket, Drucksachen &amp; Werbemittel für Caravan Service",
    lead="Ein komplettes Messepaket für vier Standorte – durchgängig und professionell.",
    intro="Für die CaraService Holding GmbH, ein führendes Unternehmen im Caravan Service, startet eine Zusammenarbeit mit mehreren gemeinsamen Projekten. Dazu gehört ein komplettes Messe-Paket bestehend aus DIN-lang Produktflyern, Gutscheinen, Postkarten, verschiedenen Roll-Ups und Square-Flags für Messen und Events. Durch individuelle Layouts, hochwertige Druckproduktion und abgestimmte Werbetechnik entsteht ein einheitlicher Markenauftritt. Das Paket ermöglicht es den Standorten in Berlin, Düsseldorf, Weißenhorn und Rott am Inn, sich durchgängig und professionell bei Kunden und Branchenveranstaltungen zu repräsentieren.",
    tags=["Messepaket", "Print", "Werbetechnik", "Werbemittel"],
    main=[U+f"designj_referenz_carawerk_0{i}.webp" for i in range(1,8)],
    blocks=[],
)
P["sei-sport"] = dict(
    name="SEI SPORT", bc="SEI SPORT",
    title="SEI SPORT – Branding & Spielerinnen-Visuals | DESIGNJ",
    desc="Grafik, Branding und Spielerinnen-Visuals für die Frauenfußball-Agentur SEI SPORT sowie die Werbung fürs SEI SPORT Fußballcamp – von DESIGNJ.",
    eyebrow="Projekt · Branding & Social Media",
    h1="SEI SPORT – Grafik, Branding &amp; Spieler*innen-Visuals für eine moderne Frauenfußball-Agentur",
    lead="Ein professioneller Auftritt – für die Präsentation der Spielerinnen<br>und die Kommunikation mit Vereinen, Partnern und Sponsoren.",
    intro="Für SEI SPORT unterstütze ich Felix und sein Team seit der Saison 2023/24 in allen Bereichen rund um Grafikdesign und Marketing. Jedes Jahr entstehen individuell gestaltete Weihnachtsgeschenke, Postkarten und verschiedene Druckprodukte, die das Markenbild von SEI SPORT stärken und den persönlichen Kontakt zu Spielerinnen, Partnern und Vereinen unterstreichen.\n\nEin zentraler Teil unserer Zusammenarbeit sind die Spielerinnen-Visuals. Für alle Athletinnen, die SEI SPORT vertritt, entwickle ich ein einheitliches Layout, das sowohl auf der Homepage als auch in den Sozialen Medien eingesetzt wird. Die farblichen Akzente passen sich jeweils dem aktuellen Verein der Spielerin an – so entsteht ein stringentes, modernes und absolut wiedererkennbares Design.",
    tags=["Branding", "Social Media", "Print", "Sport-Visuals"],
    main=[U+f"designj_referenz_seisport_0{i}.webp" for i in range(1,5)],
    blocks=[dict(h="SEI SPORT Fußballcamp",
                 t="Seit zwei Jahren gestalte ich die komplette Vorab-Werbung – online wie offline – für das SEI SPORT Fußballcamp, das speziell für junge Mädchen organisiert wird. Dazu gehören Flyer, Social-Media-Visuals und diverse Werbetechnik vor Ort, wie Beachflags, Bauzaunbanner und weitere Elemente im typischen SEI SPORT Look.",
                 imgs=[U+f"designj_referenz_seisport_fussballcamp_0{i}.webp" for i in range(1,5)])],
    quote=dict(text="Super schnell, super zuverlässig, super persönlich! Dennis kümmert sich um jedes Produkt so, als wäre es sein eigenes. Weil ihm kleine Details wichtig sind, macht er den großen Unterschied.",
               name="Felix Seidel", role="SEI Sport", logo="images/kunden/designj_kunde_seisport.webp", photo="images/kunden/designj_kundenstimme_seisport.webp"),
)
P["djk-irchenrieth"] = dict(
    name="DJK Irchenrieth", bc="DJK Irchenrieth",
    title="DJK Irchenrieth – Vereinskommunikation & Maskottchen „Arni“ | DESIGNJ",
    desc="Social-Media-Vorlagen, Flyer, Banner und das Maskottchen „Arni“ für die DJK Irchenrieth – Vereinskommunikation und Design von DESIGNJ.",
    eyebrow="Projekt · Sport & Branding",
    h1="DJK Irchenrieth – Grafiken,<br>Vereinskommunikation &amp; ein eigenes<br>Maskottchen für den Nachwuchs",
    lead="Ein einheitlicher Look, den der Verein selbst weiterführt – inklusive „Arni“, dem eigenen Nachwuchs-Adler.",
    intro="Für die DJK Irchenrieth gestalte ich seit einiger Zeit einheitliche Layout-Vorlagen für Social Media, die der Verein flexibel für Infos, Spieltagsposts und Ergebnisse einsetzen kann. So entsteht ein klarer, moderner Look, den der Verein selbstständig weiterführen kann und der auf Instagram für mehr Wiedererkennung sorgt. Darüber hinaus setze ich regelmäßig Flyer, Plakate und Banner für Turniere, Feste und Vereinsaktionen um – für den Jugendbereich wie für die Herrenmannschaft. Ein besonderes Highlight war die gemeinsame Entwicklung des Vereinsmaskottchens „Arni“, dem Adler der „DJK Nachwuchsadler“. Zusammen mit der Jugendleitung habe ich Arni als Figur konzipiert, illustriert und digital umgesetzt – heute taucht er in verschiedenen Posen auf Bannern, Flyern, Social-Media-Posts und Werbematerialien auf.",
    tags=["Social Media", "Print", "Maskottchen", "Branding"],
    main=[U+f"designj_referenz_djk_irchenrieth_0{i}.webp" for i in range(1,5)],
    blocks=[],
    quote=dict(text="Suchst du einen kompetenten und kreativen Partner für dein Branding? Ich kann Dennis nur empfehlen! Er hat uns beim Entwickeln unseres Nachwuchsadlers unterstützt und alle Logos und Vorlagen erstellt. Alles lief schnell und kundenorientiert.",
               name="Silke Stader", role="DJK Irchenrieth", logo="images/kunden/designj_kunde_djkirchenrieth.webp", photo="images/kunden/designj_kundenstimme_djk_irchenrieth.webp"),
)
P["sparkasse-oberpfalz-nord"] = dict(
    name="Sparkasse Oberpfalz Nord", bc="Sparkasse Oberpfalz Nord",
    title="Sparkasse Oberpfalz Nord – Jubiläumslogo Private Banking | DESIGNJ",
    desc="Jubiläumslogo und hochwertige Präsentationsmedien zu 10 Jahren Private Banking der Sparkasse Oberpfalz Nord – von DESIGNJ.",
    eyebrow="Projekt · Logo & Branding",
    h1="Sparkasse Oberpfalz Nord – Jubiläumslogo &amp; Präsentationsmedien für 10 Jahre Private Banking",
    lead="Aus einem Jubiläumsprojekt wurde mehr – inzwischen auch Event-Visuals und NoFi-Lauf-Shirts.",
    intro="Für die Sparkasse Oberpfalz Nord wurde ein Jubiläumslogo zum 10-jährigen Bestehen des Private Banking entwickelt. Das Logo sollte Seriosität, Exklusivität und Wertigkeit widerspiegeln und sich als Jubiläumsmarke deutlich hervorheben. Das Design passt zur bestehenden Corporate Identity und fügt sich harmonisch in alle Kommunikationsmittel ein. Anschließend wurden Roll-Ups beauftragt, die das neue Jubiläumsbranding hochwertig präsentieren – verwendet bei internen Events, Kundenterminen und öffentlichen Veranstaltungen für einen professionellen, einheitlichen und festlichen Auftritt.",
    tags=["Logo", "Branding", "Print"],
    main=[U+f"designj_referenz_sparkasse_oberpfalz_nord_0{i}.webp" for i in range(1,5)],
    blocks=[],
    quote=dict(text="Mit Dennis Jähring zusammenzuarbeiten macht einfach Spaß: kreativ, schnell und auf den Punkt. Er versteht sofort, worum es geht, und liefert Lösungen, die überraschen und begeistern.",
               name="Sparkasse Oberpfalz Nord", role="Private Banking", logo="images/kunden/designj_kunde_sparkasse_oberpfalz_nord-1.webp"),
)
P["bike-station"] = dict(
    name="BIKE Station", bc="BIKE Station",
    title="BIKE Station – Markenauftritt für Fahrradhandel & E-Bikes | DESIGNJ",
    desc="Zeitungsbeilage, Flyer, Banner, Social-Media-Anzeigen und Beschilderung für die BIKE Station in Mitterteich – sichtbarer Markenauftritt von DESIGNJ.",
    eyebrow="Projekt · Print & Werbetechnik",
    h1="BIKE Station –<br>Markenauftritt für Fahrradhandel<br>und E-Bike-Spezialist in Mitterteich",
    lead="Zeitungsbeilage, Werbeanzeigen und Beschilderung – ein einheitlicher Look in allen Bereichen.",
    intro="Die BIKE Station in Mitterteich zählt zu den führenden Adressen für Fahrräder, E-Bikes und Zubehör in der Region – und genau diesen modernen, technisch orientierten Anspruch durfte ich im Design ihrer Werbemittel unterstützen.\n\nFür das Unternehmen habe ich eine 4-seitige Zeitungsbeilage gestaltet, die das Sortiment, aktuelle Angebote und saisonale Aktionen ansprechend und strukturiert präsentiert. Ergänzend dazu entstehen regelmäßig Flyer, Banner und Social-Media-Werbeanzeigen für Events, Aktionen und Sonderverkäufe. Auch die Beschilderung des Gebäudes wurde von mir neu gestaltet, damit der Standort schon von außen professionell, modern und eindeutig wahrnehmbar ist.",
    tags=["Print", "Werbeanzeigen", "Beschilderung", "Social Media"],
    main=[U+f"designj_referenz_bike_station_mitterteich_0{i}.webp" for i in range(1,5)],
    blocks=[],
)
P["zimmer-nr-zwei"] = dict(
    name="Zimmer Nr Zwei", bc="Zimmer Nr Zwei",
    title="Zimmer Nr Zwei – Markenauftritt für Café, Restaurant & Bar | DESIGNJ",
    desc="Website, Social Media, Drucksachen und Textil für das Zimmer Nr Zwei in Weiden – ein durchgängig stimmiger Markenauftritt von DESIGNJ.",
    eyebrow="Projekt · Branding & Web",
    h1="Zimmer Nr Zwei – Kreativer Markenauftritt für Café, Restaurant &amp; Bar in Weiden",
    lead="Website, Drucksachen aller Art, Textildruck<br>und Werbeartikel – alles aus einer Hand.",
    intro="Seit der Eröffnung im Jahr 2018 begleite ich das Zimmer Nr Zwei als festen Design- und Marketingpartner – und unterstütze das Team in wirklich allen Bereichen der Kommunikation.\n\nDazu gehören Website-Gestaltung, Social-Media-Grafiken und ein breites Spektrum an Drucksachen: von Speise- und Getränkekarten über Plakate, Aufkleber und Visitenkarten bis hin zu saisonalen Aktionsmaterialien. Auch bei der Textilausstattung für die Mitarbeiter setze ich das Branding um, mit hochwertigen Drucken des Logos für Shirts, Hoodies und weitere Arbeitskleidung. So entsteht ein durchgehend stimmiges Erscheinungsbild – vom ersten Online-Eindruck bis zum Erlebnis vor Ort.",
    tags=["Branding", "Web", "Print", "Textildruck"],
    main=[U+f"designj_referenz_zimmer_nr_zwei_0{i}.webp" for i in range(1,5)],
    blocks=[],
)
P["nele-und-hannes-ocik"] = dict(
    name="Nele und Hannes Ocik", bc="Nele und Hannes Ocik",
    title="Nele & Hannes Ocik – Persönliches Branding & Web | DESIGNJ",
    desc="Persönliches Branding, Geschäftsausstattung und Homepages für Sportmoderatorin Nele Ocik und Olympia-Ruderer Hannes Ocik – von DESIGNJ.",
    eyebrow="Projekt · Personal Branding & Web",
    h1="Nele und Hannes Ocik –<br>Personal Branding &amp; digitale Präsenz<br>für Spitzensportler und Moderatorin",
    lead="Von Geschäftsausstattung bis zur eigenen Homepage – für eine Sky-Moderatorin und einen Olympia-Ruderer.",
    intro="Seit 2018 unterstütze ich Nele Ocik, bekannte Sportmoderatorin bei Sky, mit persönlichem Branding einschließlich Briefpapier, Visitenkarten und Homepage-Gestaltung. Für Hannes Ocik, mehrfach ausgezeichneter Ruderer und Olympia-Silbermedaillengewinner, wurde 2024 eine neue Homepage konzipiert. Beide Projekte zeigen hochwertige Lösungen für Personenmarken – von klassischer Geschäftsausstattung bis zur digitalen Präsentation.",
    tags=["Personal Branding", "Web", "Geschäftsausstattung"],
    main=[U+"designj_referenz_ocik_nele_01.webp", U+"designj_referenz_ocik_nele_02.webp", U+"designj_referenz_ocik_hannes_01.webp", U+"designj_referenz_ocik_hannes_02.webp"],
    blocks=[],
    quote=dict(text="Dennis hat hervorragende Arbeit geleistet. Seine fundierte Beratung, kreative Gestaltung und vor allem sein Service sind hervorzuheben.",
               name="Nele Ocik", role="Sky Sportmoderatorin", logo="images/kunden/designj_kunde_neleocik.webp", photo="images/kunden/designj_kundenstimme_nele_ocik.webp"),
)
P["kurt-landauer-stiftung"] = dict(
    name="Kurt Landauer Stiftung", bc="Kurt Landauer Stiftung",
    title="Kurt Landauer Stiftung – Magazin „KURT!“ & Gedenkbuch | DESIGNJ",
    desc="Layouts für das Magazin „KURT!“ und das Gedenkbuch 2024 der Kurt Landauer Stiftung zur Geschichte jüdischer FC-Bayern-Mitglieder – von DESIGNJ.",
    eyebrow="Projekt · Editorial & Layout",
    h1="Kurt Landauer Stiftung – Layouts für Print &amp; Digital",
    lead="Layouts für das „KURT!“-Magazin, das Gedenkbuch 2024<br>und Social-Media-Beiträge.",
    intro="Die Kurt Landauer Stiftung in München widmet sich der Aufarbeitung der Geschichte jüdischer FC-Bayern-Mitglieder und erinnert an Persönlichkeiten wie Kurt Landauer, den ehemaligen Präsidenten von Bayern München, sowie an weitere Mitglieder, die während der NS-Zeit verfolgt wurden. Die Stiftung fördert damit Erinnerungskultur, Toleranz und Weltoffenheit im Fußball.\n\nFür die Stiftung wurden die gesamten Layouts für Ausgaben des offiziellen Magazins „KURT!“ erstellt und das Gedenkbuch 2024 umgesetzt. Das Buch dokumentiert auf über 265 Seiten das Schicksal verfolgter FC-Bayern-Mitglieder und wurde komplett gestaltet – vom Layout bis zur typografischen Umsetzung.",
    tags=["Editorial", "Layout", "Print", "Buchgestaltung", "Social Media"],
    main=[U+f"designj_referenz_kurt_landauer_stiftung_{i:02d}.webp" for i in range(1,9)],
    blocks=[],
)
P["salzhaus-altenstadt"] = dict(
    name="Salzhaus Altenstadt", bc="Salzhaus Altenstadt",
    title="Salzhaus Altenstadt – Logo & Branding für Physiotherapie | DESIGNJ",
    desc="Logo-Modernisierung, Drucksachen, Textilien und Werbetechnik für die Physiotherapiepraxis Salzhaus Altenstadt – von DESIGNJ.",
    eyebrow="Projekt · Branding & Print",
    h1="Salzhaus Altenstadt –<br>Logo, Drucksachen &amp; Branding<br>für Physiotherapiepraxis",
    lead="Vom modernisierten Logo bis zum Neonschild – ein frischer, professioneller Auftritt.",
    intro="Seit 2016 begleite ich das Salzhaus Altenstadt, eine moderne Physiotherapiepraxis in Altenstadt an der Waldnaab, in allen Belangen des Corporate Designs und Marketings. Ein besonderes Highlight war die Modernisierung und Neugestaltung des Logos im Jahr 2024, die dem Auftritt der Praxis einen frischen, zeitgemäßen Look verlieh. Darüber hinaus habe ich diverse Drucksachen und Werbemittel umgesetzt, darunter Textilien für die Mitarbeiter, Visitenkarten, Türbeklebungen und ein auffälliges Neonschild des Logos in den frisch renovierten Räumen. So entsteht ein durchgängig stimmiger, professioneller und moderner Auftritt.",
    tags=["Logo", "Branding", "Print", "Werbetechnik"],
    main=[U+f"designj_referenz_salzhaus_altenstadt_0{i}.webp" for i in range(1,5)],
    blocks=[],
)
P["ravenna-wernberg"] = dict(
    name="Ravenna Wernberg", bc="Ravenna Wernberg",
    title="Ravenna Wernberg – Branding für Restaurant & Pizzeria | DESIGNJ",
    desc="Speisekarten, Flyer, Werbung und Textil für die Pizzeria & Restaurant Ravenna in Wernberg-Köblitz – ein stimmiges Konzept von DESIGNJ.",
    eyebrow="Projekt · Branding & Print",
    h1="Ravenna Wernberg –<br>Grafiken, Drucksachen &amp; Branding<br>für Restaurant &amp; Pizzeria",
    lead="Speisekarten, Werbung und Textil – ein stimmiges Konzept für Restaurant & Lieferservice.",
    intro="Seit über 10 Jahren begleite ich das Ravenna Wernberg, eine beliebte Pizzeria und Restaurant in Wernberg-Köblitz, in allen Belangen des Corporate Designs und Marketings. Zu meinen Aufgaben gehören die Gestaltung von Speisekarten für das Restaurant, Flyer und Folder für den Lieferservice, Visitenkarten, Bannerwerbung und Plakate. Zusätzlich habe ich Textilien für die Mitarbeiter umgesetzt, darunter bedruckte Schürzen und Shirts mit dem Logo, um einen professionellen und einheitlichen Auftritt vor Ort zu gewährleisten.",
    tags=["Branding", "Print", "Speisekarten", "Textildruck"],
    main=[U+f"designj_referenz_ravanna_wernberg_0{i}.webp" for i in range(1,6)],
    main_cols=3,
    blocks=[],
    quote=dict(text="Über 10 Jahre unser bester Partner, wenn es rund ums Thema Werbung, Kreativität und Design geht.",
               name="Martin Sautter", role="Restaurant Ravenna", logo="images/kunden/designj_kunde_ravenna.webp"),
)

P["voit"] = dict(
    name="VOIT", bc="VOIT",
    title="Partyservice & Eventcatering VOIT – Branding & Drucksachen | DESIGNJ",
    desc="Aufkleber, Fahrzeugbeklebung, Flyer, Social Media und Geschäftsausstattung für Partyservice & Eventcatering VOIT in Weiden – konsistentes Branding von DESIGNJ.",
    eyebrow="Projekt · Branding & Print",
    h1="Partyservice &amp; Eventcatering VOIT –<br>Grafiken, Drucksachen &amp; Branding<br>für Metzgerei, Imbiss und Catering",
    lead="Aufkleber, Fahrzeuge, Print und Social Media – ein konsistenter Auftritt aus einer Hand.",
    intro="Seit 2011 betreue ich den Partyservice & das Eventcatering VOIT umfassend in allen grafischen Belangen – für Metzgerei, Imbiss und Catering in Weiden. Dazu gehören die Gestaltung von Aufklebern, Fahrzeugbeklebungen, Flyern, Plakaten und Foldern ebenso wie Social-Media-Grafiken, Geschäftsausstattung und Präsentationen. So entsteht über alle Kanäle hinweg ein konsistenter, professioneller Markenauftritt.",
    tags=["Branding", "Print", "Fahrzeugbeklebung", "Social Media"],
    main=[U+f"designj_referenz_voit_0{i}.webp" for i in range(1,5)],
    blocks=[],
)
P["12ender"] = dict(
    name="12Ender", bc="12Ender",
    title="12Ender – Branding & Werbetechnik für Imbisse & Gastronomie | DESIGNJ",
    desc="Grafik und Beschilderung innen wie außen für die beiden „12Ender“-Imbisse in der Oberpfalz – stimmiges Design und Werbetechnik von DESIGNJ.",
    eyebrow="Projekt · Gastronomie & Werbetechnik",
    h1="12Ender –<br>Branding &amp; Werbetechnik<br>für Imbisse &amp; Gastronomie",
    lead="Grafik und Beschilderung innen wie außen – sichtbar und wiedererkennbar.",
    intro="Für die beiden „12Ender“-Imbisse unterstütze ich die Betriebe grafisch sowie bei der Beschilderung innen und außen. Die Imbisse bieten von Frühstück über wechselnde warme Mittagsgerichte frische, bayerische Mahlzeiten an – und werden durch ein stimmiges Design und die passende Werbetechnik optimal sichtbar und wiedererkennbar.",
    tags=["Branding", "Werbetechnik", "Beschilderung", "Print"],
    main=[U+f"designj_referenz_voit_12ender_0{i}.webp" for i in range(1,5)],
    blocks=[],
)

# ================= TEMPLATE =================
TPL = r"""<!DOCTYPE html>
<html lang="de">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>@@TITLE@@</title>
  <meta name="description" content="@@DESC@@">
  <meta name="robots" content="index, follow">
  <link rel="canonical" href="@@CANON@@">
  <meta property="og:type" content="article">
  <meta property="og:title" content="@@TITLE@@">
  <meta property="og:description" content="@@DESC@@">
  <meta property="og:image" content="@@OGIMAGE@@">
  <meta property="og:url" content="@@CANON@@">
  <link rel="icon" type="image/svg+xml" href="designj_icon.svg">
  <link rel="stylesheet" href="css/fonts.css">
  <link rel="stylesheet" href="css/style.css">
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "ProfessionalService",
    "@id": "https://www.designj.de/#designj",
    "name": "DESIGNJ – Dennis Jähring",
    "alternateName": "DESIGNJ Werbeagentur Weiden",
    "description": "Werbeagentur aus Weiden i.d.OPf. Design, Druck & Digital aus einer Hand – über 20 Jahre Erfahrung, ein Ansprechpartner.",
    "url": "https://www.designj.de/",
    "image": "https://www.designj.de/og-image.jpg",
    "telephone": "+49 170 291 83 05",
    "email": "info@designj.de",
    "priceRange": "€€",
    "slogan": "Design. Druck. Digital.",
    "foundingDate": "2003-05-02",
    "founder": { "@type": "Person", "name": "Dennis Jähring" },
    "address": { "@type": "PostalAddress", "streetAddress": "Hasenweg 34", "postalCode": "92699", "addressLocality": "Irchenrieth", "addressRegion": "Bayern", "addressCountry": "DE" },
    "areaServed": [ { "@type": "City", "name": "Weiden in der Oberpfalz" }, { "@type": "AdministrativeArea", "name": "Oberpfalz" }, { "@type": "Country", "name": "Deutschland" } ],
    "sameAs": [ "https://www.instagram.com/designj.de/", "https://www.facebook.com/designj.de" ]
  }
  </script>
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "BreadcrumbList",
    "itemListElement": [
      { "@type": "ListItem", "position": 1, "name": "Start", "item": "https://www.designj.de/" },
      { "@type": "ListItem", "position": 2, "name": "Projekte", "item": "https://www.designj.de/projekte.html" },
      { "@type": "ListItem", "position": 3, "name": "@@BCNAME@@", "item": "@@CANON@@" }
    ]
  }
  </script>
</head>
<body>
<svg width="0" height="0" style="position:absolute;overflow:hidden" aria-hidden="true"><defs><mask id="sgl-ig" maskUnits="userSpaceOnUse" x="0" y="0" width="48" height="48"><rect width="48" height="48" fill="#fff"/><path fill="#000" d="M33.219,9.035H14.815c-3.197,0-5.797,2.6-5.797,5.797v6.125v12.281c0,3.197,2.6,5.797,5.797,5.797h18.404c3.197,0,5.799-2.6,5.799-5.797V20.957v-6.125C39.018,11.634,36.417,9.035,33.219,9.035z M34.883,12.494l0.662-0.004v0.662v4.422l-5.066,0.017l-0.018-5.084L34.883,12.494z M19.737,20.957c0.961-1.33,2.519-2.201,4.281-2.201s3.32,0.871,4.281,2.201c0.625,0.867,1,1.93,1,3.078c0,2.91-2.371,5.279-5.281,5.279c-2.912,0-5.281-2.369-5.281-5.279C18.737,22.886,19.112,21.824,19.737,20.957z M36.096,33.238c0,1.586-1.291,2.875-2.877,2.875H14.815c-1.586,0-2.875-1.289-2.875-2.875V20.957h4.478c-0.387,0.951-0.603,1.99-0.603,3.078c0,4.523,3.68,8.203,8.203,8.203c4.523,0,8.203-3.68,8.203-8.203c0-1.088-0.219-2.127-0.605-3.078h4.48V33.238z"/></mask><mask id="sgl-fb" maskUnits="userSpaceOnUse" x="0" y="0" width="48" height="48"><rect width="48" height="48" fill="#fff"/><path fill="#000" d="M20.018,39.035h6c0,0,0-8.282,0-15h4.453l0.547-6H26.25v-2.399c0-1.169,0.779-1.441,1.326-1.441c0.547,0,3.366,0,3.366,0V9.053l-4.635-0.019c-5.145,0-6.314,3.834-6.314,6.288v2.712h-2.975v6h3C20.018,30.834,20.018,39.035,20.018,39.035z"/></mask><mask id="sgl-li" maskUnits="userSpaceOnUse" x="0" y="0" width="48" height="48"><rect width="48" height="48" fill="#fff"/><rect fill="#000" x="9.018" y="19.035" width="7" height="20"/><circle fill="#000" cx="12.518" cy="12.535" r="3.5"/><path fill="#000" d="M39.018,28.044c0-5.397-1.164-9.009-7.455-9.009c-3.023,0-5.053,1.123-5.883,2.699h-0.086v-2.699h-5.576v20h5.828v-9.913c0-2.614,0.494-5.145,3.728-5.145c3.186,0,3.443,2.989,3.443,5.314v9.745h6V28.044z"/></mask></defs></svg>

<header class="nav">
  <div class="container nav__inner">
    <a href="index.html" class="nav__logo" aria-label="DESIGNJ Startseite"><img src="designj_logo.svg" alt="DESIGNJ – Design Druck Digital"></a>
    <nav class="nav__menu" aria-label="Hauptnavigation">
      <a href="index.html">Start</a>
      <a href="leistungen.html">Leistungen</a>
      <a href="projekte.html">Projekte</a>
      <a href="kunden.html">Kunden</a>
      <a href="ueber-mich.html">Über mich</a>
      <a href="kontakt.html">Kontakt</a>
    </nav>
    <div class="nav__right">
      <a href="kontakt.html" class="btn btn--primary">Projekt starten</a>
      <button class="nav__toggle" aria-label="Menü öffnen" aria-expanded="false" aria-controls="mobileNav"><span></span></button>
    </div>
  </div>
</header>
<div class="nav__mobile" id="mobileNav">
  <div class="nav__mobile-head"><img src="designj_icon.svg" alt="DESIGNJ Icon"><span>Design | Druck | Digital</span></div>
  <a href="index.html" class="m-link">Start</a>
  <a href="leistungen.html" class="m-link">Leistungen</a>
  <a href="projekte.html" class="m-link">Projekte</a>
  <a href="kunden.html" class="m-link">Kunden</a>
  <a href="ueber-mich.html" class="m-link">Über mich</a>
  <a href="kontakt.html" class="m-link">Kontakt</a>
  <a href="kontakt.html" class="btn btn--primary btn--block">Projekt starten</a>
</div>

<main class="proj-page">

<section class="hero hero--text hero--project">
  <div class="container hero__content reveal">
    <a href="projekte.html" class="back-link"><span class="arrow">←</span> Alle Projekte</a>
    <span class="eyebrow">@@EYEBROW@@</span>
    <h1>@@H1@@</h1>
    <p class="lead">@@LEAD@@</p>
@@INTRO@@
    <div class="proj-tags">
@@TAGS@@
    </div>
  </div>
</section>
@@MAINGALLERY@@
@@BLOCKS@@
@@TESTIMONIAL@@
<section class="container section">
  <div class="cta-band reveal">
    <h2>Sollen wir auch dein Projekt angehen?</h2>
    <p class="lead">Vom ersten Entwurf bis zur fertigen Umsetzung – Design, Druck und Digital<br>aus einer Hand. Lass uns über dein Projekt sprechen.</p>
    <div class="cta-band__btns">
      <a href="kontakt.html" class="btn btn--primary btn--lg">Projekt starten <span class="arrow">→</span></a>
      <a href="projekte.html" class="btn btn--ghost btn--lg">Mehr Projekte ansehen</a>
    </div>
  </div>
</section>

<section class="container section--tight">
  <div class="proj-nav reveal">
    @@PREV@@
    <a href="projekte.html" class="center">Alle Projekte</a>
    @@NEXT@@
  </div>
</section>

</main>

<footer class="footer">
  <div class="container">
    <div class="footer__top">
      <div class="footer__brand">
        <img src="designj_logo.svg" alt="DESIGNJ – Design Druck Digital">
        <p class="footer__addr">DESIGNJ | Dennis Jähring<br>Hasenweg 34<br>92699 Irchenrieth<br><a href="tel:+491702918305">+49 170 291 83 05</a><br><a href="mailto:info@designj.de">info@designj.de</a></p>
      </div>
      <div class="footer__col">
        <h4>Navigation</h4>
        <a href="index.html">Start</a><a href="leistungen.html">Leistungen</a><a href="projekte.html">Projekte</a><a href="kunden.html">Kunden</a><a href="ueber-mich.html">Über mich</a><a href="kontakt.html">Kontakt</a>
      </div>
      <div class="footer__col">
        <h4>Social Media</h4>
        <div class="socials">
          <a class="social-btn" href="https://www.instagram.com/designj.de/" target="_blank" rel="noopener" aria-label="Instagram"><svg class="ico" viewBox="0 0 48 48" aria-hidden="true"><rect width="48" height="48" rx="11" fill="currentColor" mask="url(#sgl-ig)"/></svg></a>
          <a class="social-btn" href="https://www.facebook.com/designj.de" target="_blank" rel="noopener" aria-label="Facebook"><svg class="ico" viewBox="0 0 48 48" aria-hidden="true"><rect width="48" height="48" rx="11" fill="currentColor" mask="url(#sgl-fb)"/></svg></a>
          <a class="social-btn" href="https://www.linkedin.com/in/dennisjaehring/" target="_blank" rel="noopener" aria-label="LinkedIn"><svg class="ico" viewBox="0 0 48 48" aria-hidden="true"><rect width="48" height="48" rx="11" fill="currentColor" mask="url(#sgl-li)"/></svg></a>
        </div>
      </div>
    </div>
    <div class="footer__bottom">
      <span>© <span data-year>2026</span> DESIGNJ – Dennis Jähring. Alle Rechte vorbehalten.</span>
      <span class="footer__legal"><a href="impressum.html">Impressum</a><a href="datenschutz.html">Datenschutz</a></span>
    </div>
  </div>
</footer>

<script src="js/main.js"></script>
</body>
</html>
"""

def basename(url): return os.path.basename(urlparse(url).path)
def local(url): return "images/referenzen/" + basename(url)

def gallery(imgs, name, block=False, cols=None):
    # Einheitliches 4-Spalten-Raster (.proj-gallery). cols=N überschreibt pro
    # Galerie die Spaltenzahl (z. B. damit gleichartige Logos in einer Reihe stehen).
    if not imgs: return ""
    parts = []
    if block: parts.append("margin-top:1.8rem")
    if cols:  parts.append(f"grid-template-columns:repeat({cols},1fr)")
    style = f' style="{";".join(parts)}"' if parts else ""
    items = "\n".join(
        f'    <a href="{local(u)}"><img src="{local(u)}" alt="{name} – Referenz von DESIGNJ" loading="lazy"></a>'
        for u in imgs)
    return f'  <div class="proj-gallery reveal"{style}>\n{items}\n  </div>'

def navlink(slug, label, arrow_before):
    if slug is None:
        if arrow_before:
            return '<a class="is-disabled" aria-disabled="true"><span class="arrow">←</span> Vorheriges</a>'
        return '<a class="is-disabled" aria-disabled="true">Nächstes <span class="arrow">→</span></a>'
    if arrow_before:
        return f'<a href="{pfile(slug)}"><span class="arrow">←</span> Vorheriges</a>'
    return f'<a href="{pfile(slug)}">Nächstes <span class="arrow">→</span></a>'

all_imgs = []
def brk(s):
    # Überschrift „schöner aufteilen": Umbruch nach dem ersten Gedankenstrich „ – ".
    # Wenn schon ein manueller <br> drin ist, nichts ändern (Override pro Projekt möglich).
    if "<br>" in s:
        return s
    return s.replace(" – ", " –<br>", 1)

def build(slug, d):
    canon = f"https://www.designj.de/{pfile(slug)}"
    # og image = erstes Bild
    first = (d["main"] or (d["blocks"][0]["imgs"] if d["blocks"] and d["blocks"][0]["imgs"] else []))
    ogimg = f"https://www.designj.de/{local(first[0])}" if first else "https://www.designj.de/og-image.jpg"
    intro = "\n".join(f'    <p class="proj-intro">{p.strip()}</p>' for p in d["intro"].split("\n\n"))
    tags = "\n".join(f'      <span class="proj-tag">{t}</span>' for t in d["tags"])
    # main gallery
    mg = ""
    if d["main"]:
        mg = f'\n<section class="container section--tight">\n{gallery(d["main"], d["name"], cols=d.get("main_cols"))}\n</section>\n'
        all_imgs.extend(d["main"])
    # blocks
    blk = ""
    for b in d["blocks"]:
        g = gallery(b["imgs"], d["name"], block=True, cols=b.get("cols")) if b["imgs"] else ""
        all_imgs.extend(b["imgs"])
        blk += (f'\n<section class="container section">\n'
                f'  <div class="proj-body reveal">\n    <h2>{brk(b["h"])}</h2>\n    <p>{b["t"]}</p>\n  </div>\n'
                f'{g}\n</section>\n')
    # testimonial
    tst = ""
    q = d.get("quote")
    if q:
        if q.get("photo"):
            media = f'    <div class="proj-quote__media proj-quote__media--photo"><img src="{q["photo"]}" alt="{q["name"]}"></div>\n'
        else:
            media = f'    <div class="proj-quote__media"><img src="{q["logo"]}" alt="Logo {q["name"]}"></div>\n'
        tst = (f'\n<section class="container section">\n'
               f'  <figure class="proj-quote reveal">\n'
               f'{media}'
               f'    <div>\n'
               f'      <blockquote>„{q["text"]}“</blockquote>\n'
               f'      <div class="proj-quote__name">{q["name"]}</div>\n'
               f'      <div class="proj-quote__role">{q["role"]}</div>\n'
               f'    </div>\n  </figure>\n</section>\n')
    i = ORDER.index(slug)
    prev = ORDER[i-1] if i > 0 else None
    nxt = ORDER[i+1] if i < len(ORDER)-1 else None
    html = (TPL
        .replace("@@TITLE@@", d["title"])
        .replace("@@DESC@@", d["desc"])
        .replace("@@CANON@@", canon)
        .replace("@@OGIMAGE@@", ogimg)
        .replace("@@BCNAME@@", d["bc"])
        .replace("@@EYEBROW@@", d["eyebrow"])
        .replace("@@H1@@", brk(d["h1"]))
        .replace("@@LEAD@@", brk(d["lead"]))
        .replace("@@INTRO@@", intro)
        .replace("@@TAGS@@", tags)
        .replace("@@MAINGALLERY@@", mg)
        .replace("@@BLOCKS@@", blk)
        .replace("@@TESTIMONIAL@@", tst)
        .replace("@@PREV@@", navlink(prev, "Vorheriges", True))
        .replace("@@NEXT@@", navlink(nxt, "Nächstes", False)))
    with open(os.path.join(ROOT, pfile(slug)), "w", encoding="utf-8") as f:
        f.write(html)
    return len(d["main"]) + sum(len(b["imgs"]) for b in d["blocks"])

built = 0
for slug, d in P.items():
    n = build(slug, d)
    built += 1
    print(f"  ✓ {pfile(slug):42s} ({n} Bilder)")

# ---- Bilder herunterladen ----
print("\nLade Bilder ...")
opener = urllib.request.build_opener()
opener.addheaders = [("User-Agent", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)")]
urllib.request.install_opener(opener)
dl = ok = skip = fail = 0
seen = set()
for u in all_imgs:
    if u in seen: continue
    seen.add(u)
    dest = os.path.join(ROOT, local(u))
    if os.path.exists(dest) and os.path.getsize(dest) > 1500:
        skip += 1; continue
    for attempt in range(3):
        try:
            urllib.request.urlretrieve(u, dest)
            if os.path.getsize(dest) > 500:
                ok += 1
            else:
                fail += 1; print("    ! leer:", u)
            break
        except Exception as e:
            if attempt == 2:
                fail += 1; print("    ! FEHLER:", basename(u), e)
            else:
                time.sleep(1.5)
    time.sleep(0.25)
print(f"\nFertig: {built} Seiten gebaut | Bilder neu: {ok}, vorhanden: {skip}, Fehler: {fail}")
