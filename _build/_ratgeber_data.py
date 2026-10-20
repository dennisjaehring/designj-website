# -*- coding: utf-8 -*-
# Inhaltsdaten fuer den Ratgeber (genutzt von _gen_ratgeber.py)
# Umbruch-Regel: im Fliesstext/Headlines plain <br> schreiben -> Generator macht
# daraus desktop-only Umbrueche mit fuehrendem Leerzeichen.
# Reihenfolge der ARTICLES = Anzeige-Reihenfolge (neueste oben).

OVERVIEW = dict(
    title="Ratgeber | DESIGNJ – Design, Druck & Digital",
    desc="Ratgeber von DESIGNJ aus Weiden: verstaendliche Tipps zu Logo, Website, Druck, Social Media und Marketing – ohne Fachchinesisch, direkt aus der Praxis.",
    eyebrow="Gut zu wissen",
    h1='Ratgeber –<br>Klartext statt Fachchinesisch.',
    lead="Kurze, ehrliche Beiträge zu<br>Design, Druck und Marketing.<br>Damit du weißt, worauf es ankommt –<br>bevor du startest.",
)

ARTICLES = [
    # ---------- Branding ----------
    dict(
        slug="ratgeber-gutes-logo", cat="Branding", read="ca. 3 Min",
        title="Was macht ein gutes Logo aus? | DESIGNJ Ratgeber",
        desc="Was ein gutes Logo ausmacht: 4 Merkmale, an denen du ein starkes, zeitloses Logo erkennst – verständlich erklärt, ohne Fachchinesisch.",
        teaser="4 Merkmale, an denen du ein starkes Logo erkennst.",
        eyebrow="Ratgeber · Branding", service_href="/branding", service_label="Branding",
        h1="Was macht ein<br>gutes Logo aus?",
        lead="Ein gutes Logo muss nicht aufwändig sein –<br>es muss funktionieren: erkennbar, überall<br>einsetzbar und in ein paar Jahren noch gut.",
        blocks=[
            ("Erkennbar statt kompliziert", [
                "Die besten Logos sind einfach. Was man auf einen Blick erfasst, bleibt im Kopf – verschnörkelte Details verschwinden spätestens, wenn das Logo klein wird.",
                "Ein guter Test: Funktioniert es als winziges Icon genauso wie groß auf einem Schild? Wenn ja, bist du auf dem richtigen Weg.",
            ]),
            ("Es muss überall funktionieren", [
                "Dein Logo landet auf Website, Visitenkarte, Fahrzeug, Stempel und Social Media. Deshalb braucht es Varianten: farbig, einfarbig, hell auf dunkel und umgekehrt.",
                "Dazu die richtigen Dateien für Druck und Web – damit es überall sauber aussieht, nicht nur am Bildschirm.",
            ]),
            ("Zeitlos schlägt Trend", [
                "Trends sehen heute modern aus und morgen alt. Dein Logo soll dich aber viele Jahre begleiten. Lieber klar und reduziert als dem letzten Design-Hype hinterher.",
            ]),
            ("Es passt zu dir", [
                "Ein Logo aus der Vorlage sieht aus wie tausend andere. Gut ist es, wenn es zu deiner Branche und deinen Werten passt – und dich von anderen unterscheidet.",
            ]),
        ],
        key=[
            "Einfach und auf einen Blick erkennbar.",
            "Funktioniert einfarbig und in jeder Größe.",
            "Zeitlos statt trendy – hält viele Jahre.",
            "Passt zu dir, nicht aus der Vorlage.",
        ],
        cta_h2="Zeit für ein Logo, das bleibt?",
        cta_lead="Ich entwickle dir eine Marke, die erkennbar ist und zu dir passt.",
        published=True,
    ),
    # ---------- Webdesign ----------
    dict(
        slug="ratgeber-website-ablauf", cat="Webdesign", read="ca. 3 Min",
        title="Website erstellen lassen: der Ablauf in 5 Schritten | DESIGNJ",
        desc="Website erstellen lassen: So läuft der Ablauf von der Idee bis online – in 5 verständlichen Schritten erklärt.",
        teaser="Von der Idee bis online – was wann passiert.",
        eyebrow="Ratgeber · Webdesign", service_href="/webdesign", service_label="Webdesign",
        h1="Website erstellen lassen:<br>der Ablauf in 5 Schritten",
        lead="Eine Website entsteht nicht über Nacht –<br>aber der Weg dahin ist klar und planbar.<br>So läuft's von der Idee bis online.",
        blocks=[
            ("1. Gespräch & Ziel", [
                "Zuerst klären wir, was die Seite leisten soll: Kunden gewinnen, informieren, Termine bringen? Und wen du erreichen willst. Daraus ergibt sich alles Weitere.",
            ]),
            ("2. Struktur & Inhalte", [
                "Wir legen fest, welche Seiten es gibt und was wo steht. Gute Struktur heißt: Besucher finden sofort, was sie suchen – und Google versteht die Seite auch.",
                "Texte und Bilder sammeln wir gemeinsam; wo etwas fehlt, kümmere ich mich darum.",
            ]),
            ("3. Design & Umsetzung", [
                "Jetzt bekommt die Seite ihr Gesicht – passend zu deiner Marke, auf dem Handy genauso wie am Rechner. Anschließend wird alles sauber und schnell umgesetzt.",
            ]),
            ("4. Launch & danach", [
                "Vor dem Livegang prüfen wir alles: Technik, Mobildarstellung, Google-Grundlagen. Nach dem Start kann die Seite jederzeit wachsen – auf Wunsch pflege ich sie laufend.",
            ]),
        ],
        key=[
            "Erst Ziel klären, dann bauen.",
            "Struktur für Besucher UND Google.",
            "Responsiv: Handy wie Desktop.",
            "Nach dem Launch jederzeit erweiterbar.",
        ],
        cta_h2="Bereit für deine Website?",
        cta_lead="Von der Idee bis online – aus einer Hand, persönlich geplant.",
        published=True,
    ),
    # ---------- Print ----------
    dict(
        slug="ratgeber-flyer-drucken", cat="Print", read="ca. 3 Min",
        title="Flyer drucken lassen – worauf du achten solltest | DESIGNJ",
        desc="Flyer drucken lassen: Daten, Papier, Veredelung und Auflage – die wichtigsten Punkte, damit dein Flyer am Ende so aussieht wie geplant.",
        teaser="Die Checkliste für Daten, Material und Veredelung.",
        eyebrow="Ratgeber · Print", service_href="/print-produktion", service_label="Print & Produktion",
        h1="Flyer drucken lassen –<br>worauf du achten solltest",
        lead="Ein guter Flyer scheitert selten am Motiv,<br>sondern an Details im Druck. Die wichtigsten<br>Punkte, damit das Ergebnis stimmt.",
        blocks=[
            ("Daten richtig anlegen", [
                "Beschnitt, Auflösung und Farbraum (CMYK statt RGB) entscheiden, ob der Druck so aussieht wie am Bildschirm. Klingt technisch – das übernehme ich für dich, damit nichts schiefgeht.",
            ]),
            ("Das richtige Papier", [
                "Dünn und glänzend oder griffig und matt? Das Papier verändert die Wirkung enorm. Für einen hochwertigen Eindruck lohnt sich oft ein etwas stärkeres Material.",
            ]),
            ("Veredelung macht den Unterschied", [
                "Eine Lackierung, Prägung oder ein besonderer Falz heben deinen Flyer von der Masse ab – gezielt eingesetzt, nicht überladen.",
            ]),
            ("Menge & Timing", [
                "Größere Auflagen sind pro Stück günstiger, sollten aber nicht veralten. Und: Druck braucht Vorlauf – plane lieber ein paar Tage mehr ein.",
            ]),
        ],
        key=[
            "Daten in CMYK, mit Beschnitt und genug Auflösung.",
            "Papier bestimmt die Wertigkeit.",
            "Veredelung gezielt einsetzen.",
            "Auflage und Vorlauf einplanen.",
        ],
        cta_h2="Flyer, Karte oder Broschüre geplant?",
        cta_lead="Ich gestalte und produziere – du bekommst das fertige Ergebnis.",
        published=True,
    ),
    # ---------- Social Media ----------
    dict(
        slug="ratgeber-social-selbst-oder-auslagern", cat="Social Media", read="ca. 3 Min",
        title="Social Media selbst machen oder auslagern? | DESIGNJ Ratgeber",
        desc="Social Media selbst machen oder auslagern? Ehrliche Pro- und Contra-Abwägung – und warum ein Hybrid-Modell für viele am besten passt.",
        teaser="Ehrliche Pro- und Contra-Liste für beide Wege.",
        eyebrow="Ratgeber · Social Media", service_href="/social-media", service_label="Social Media",
        h1="Social Media selbst<br>machen oder auslagern?",
        lead="Beides geht – die Frage ist, was zu dir passt.<br>Ehrlich abgewogen, ohne Verkaufsmasche.",
        blocks=[
            ("Was selbst gut funktioniert", [
                "Du kennst dein Geschäft am besten. Schnelle Einblicke, eine Baustelle, ein zufriedener Kunde – solche echten Momente kannst du selbst am besten festhalten.",
            ]),
            ("Wo es oft hakt", [
                "Der Haken ist selten die Idee, sondern die Konsistenz: regelmäßig posten, ein einheitlicher Look, gute Grafiken. Genau da schläft Social Media bei vielen ein.",
            ]),
            ("Der Mittelweg: Vorlagen + du", [
                "Oft ist die beste Lösung ein Hybrid: Ich baue dir ein Vorlagen-Set und den Look, du füllst es mit deinen Inhalten. So bleibt es einheitlich und du bleibst flexibel.",
            ]),
            ("Wann ganz auslagern?", [
                "Wenn dir schlicht die Zeit fehlt, übernehme ich auch Planung und Umsetzung – dann läuft dein Auftritt, ohne dass du ständig dran denken musst.",
            ]),
        ],
        key=[
            "Echte Momente fängst du selbst am besten ein.",
            "Schwachstelle ist meist die Konsistenz.",
            "Hybrid: Vorlagen von mir, Inhalte von dir.",
            "Keine Zeit? Dann übernehme ich komplett.",
        ],
        cta_h2="Unsicher, welcher Weg zu dir passt?",
        cta_lead="Wir finden den Mix, der zu deiner Zeit und deinen Zielen passt.",
        published=True,
    ),
    # ---------- Branche: Sport & Vereine ----------
    dict(
        slug="ratgeber-sponsoring-vereinssport", cat="Sport & Vereine", read="ca. 4 Min",
        title="Sponsoring im Vereinssport – worauf es ankommt | DESIGNJ",
        desc="Sponsoring im Vereinssport: Was Sponsoren wirklich wollen, was Vereine bieten können und wie gutes Design beiden hilft.",
        teaser="Wie Vereine attraktiv werden – und Sponsoren wirklich profitieren.",
        eyebrow="Ratgeber · Sport & Vereine", service_href="/sport", service_label="Sport & Vereine",
        hero_img="sport_hero",
        h1="Sponsoring im Vereinssport –<br>worauf es ankommt",
        lead="Sponsoring ist mehr als ein Logo auf dem Trikot.<br>Wie Vereine attraktiv werden – und Sponsoren<br>wirklich etwas davon haben.",
        blocks=[
            ("Was Sponsoren wirklich wollen", [
                "Ein Sponsor will Sichtbarkeit und ein gutes Image – am liebsten lokal, dort wo seine Kunden sind. Der Verein bietet genau das: Reichweite in der Region, Woche für Woche.",
            ]),
            ("Was ein Verein zu bieten hat", [
                "Bande, Trikot, Stadionheft, Social Media, Events – es gibt viel mehr Flächen als nur das Trikot. Wichtig ist, sie als Paket zu denken statt einzeln zu verramschen.",
            ]),
            ("Attraktiv aufbereiten", [
                "Mit einer sauberen Sponsoren-Mappe und klaren Paketen wirkt ein Verein professionell – das erleichtert dem Sponsor die Entscheidung enorm.",
            ]),
            ("Gutes Design zahlt auf beide ein", [
                "Eine Bande oder ein Trikot-Druck, der gut aussieht, wertet den Verein <strong>und</strong> den Sponsor auf. Genau hier hole ich das Maximum raus.",
            ]),
        ],
        key=[
            "Sponsoren wollen lokale Sichtbarkeit + Image.",
            "Mehr Flächen als nur das Trikot – als Paket denken.",
            "Sponsoren-Mappe + klare Pakete wirken professionell.",
            "Gutes Design wertet Verein und Sponsor auf.",
        ],
        cta_h2="Mehr aus eurem Vereinsauftritt holen?",
        cta_lead="Von der Bande bis zum Sponsoren-Konzept – ich unterstütze Vereine.",
        published=True,
    ),
    # ---------- Branche: Handwerk ----------
    dict(
        slug="ratgeber-marketing-handwerk", cat="Handwerk", read="ca. 4 Min",
        title="Marketing fürs Handwerk: 5 Hebel, die sofort wirken | DESIGNJ",
        desc="Marketing fürs Handwerk: 5 einfache Hebel – von Fahrzeugbeschriftung bis Google-Profil – die zuverlässig für mehr Aufträge sorgen.",
        teaser="5 einfache Hebel, die zuverlässig Aufträge bringen.",
        eyebrow="Ratgeber · Handwerk", service_href="/handwerk", service_label="Handwerk & Bau",
        hero_img="handwerk_hero",
        h1="Marketing fürs Handwerk:<br>5 Hebel, die sofort wirken",
        lead="Als Handwerker brauchst du kein kompliziertes<br>Marketing – sondern ein paar Dinge, die<br>zuverlässig für Aufträge sorgen.",
        blocks=[
            ("1. Dein Fahrzeug als Werbefläche", [
                "Dein Transporter steht täglich bei Kunden und an der Straße. Eine saubere Beschriftung mit Logo, Leistung und Nummer ist Werbung, die 24/7 für dich fährt – einmal gemacht, dauerhaft sichtbar.",
            ]),
            ("2. Die Baustelle nutzen", [
                "Ein Bauzaunbanner oder ein Schild am Objekt zeigt der ganzen Nachbarschaft, wer hier arbeitet – genau dort, wo der nächste Auftrag entstehen kann.",
            ]),
            ("3. Bei Google auffindbar sein", [
                "Die meisten suchen den Handwerker online. Ein gepflegtes Google-Profil und eine einfache Website sorgen dafür, dass man dich findet – und direkt anrufen kann.",
            ]),
            ("4. Ein einheitlicher Auftritt", [
                "Logo, Arbeitskleidung, Visitenkarte, Rechnung – wenn alles zusammenpasst, wirkst du verlässlich. Das schafft Vertrauen, bevor du ein Wort gesagt hast.",
            ]),
            ("5. Bewertungen einsammeln", [
                "Zufriedene Kunden sind deine beste Werbung. Frag aktiv nach einer Google-Bewertung – ein paar gute Sterne überzeugen den nächsten Interessenten.",
            ]),
        ],
        key=[
            "Fahrzeugbeschriftung = Werbung, die 24/7 fährt.",
            "Bauzaun und Baustelle als Werbefläche nutzen.",
            "Google-Profil + einfache Website = auffindbar.",
            "Einheitlicher Auftritt schafft Vertrauen.",
        ],
        cta_h2="Mehr Aufträge aus deinem Auftritt?",
        cta_lead="Von Fahrzeug bis Website – ich bringe dein Handwerk sichtbar nach vorn.",
        published=True,
    ),
    # ---------- Marketing ----------
    dict(
        slug="ratgeber-marketing-auslagern-oder-einstellen", cat="Marketing", read="ca. 4 Min",
        title="Marketing auslagern oder einstellen? | DESIGNJ Ratgeber",
        desc="Lohnt sich eine feste Marketing-Stelle oder ein externer Partner? Wann Auslagern die bessere Wahl ist – ehrlich erklärt, ohne Verkaufsmasche.",
        teaser="Eine feste Stelle läuft das ganze Jahr – auch in ruhigen Monaten. Wann ein flexibler Partner die klügere Wahl ist.",
        eyebrow="Ratgeber · Marketing", service_href="/marketing-betreuung", service_label="Marketing & Betreuung",
        h1="Marketing auslagern<br>oder einstellen?",
        lead="Du musst niemanden einstellen, der ein oder zwei Themen beherrscht<br>und ganzjährig bezahlt wird – wenn dein Marketing übers Jahr aus<br>drei, vier Bereichen besteht und mal Monate ruhig sind.",
        blocks=[
            ("Das Problem mit der festen Stelle", [
                "Eine Marketing-Stelle klingt erstmal nach der sauberen Lösung: jemand kümmert sich, fertig. In der Praxis ist es selten so einfach.",
                "Gutes Marketing besteht heute aus vielen Disziplinen – Design, Social Media, Website, Druck, Texte, Anzeigen. <strong>Eine einzelne Person beherrscht fast nie alles</strong> auf gutem Niveau. Du bekommst entweder einen Allrounder, der in vielem okay ist, oder einen Spezialisten, dem die Hälfte fehlt.",
                "Dazu kommt: Die Stelle läuft das ganze Jahr – mit Gehalt, Nebenkosten, Urlaub und Krankheit. Auch in den Wochen, in denen gerade wenig ansteht.",
            ]),
            ("Wie viel Marketing brauchst du wirklich?", [
                "Die meisten kleinen und mittleren Betriebe haben über das Jahr verteilt drei bis vier Marketing-Themen: mal eine Kampagne, mal neue Drucksachen, mal der Social-Media-Auftritt, mal die Website.",
                "Zwischendrin gibt es ruhige Phasen – zwei, drei Monate, in denen kaum etwas liegen bleibt. Eine feste Stelle kostet in dieser Zeit trotzdem voll. <strong>Du bezahlst Kapazität, die du gerade nicht brauchst.</strong>",
            ]),
            ("Was ein externer Partner anders macht", [
                "Ein Partner kommt dann ins Spiel, wenn etwas ansteht – und ist weg, wenn gerade nichts zu tun ist. Keine Leerlauf-Kosten.",
                "Über ein eingespieltes Netzwerk deckst du mehrere Disziplinen mit <strong>einem Ansprechpartner</strong> ab: Design, Druck und Digital aus einer Hand, statt drei halbe Stellen. Und du kannst hoch- und runterfahren, je nachdem, was das Jahr gerade verlangt.",
            ]),
            ("Wann sich eine feste Stelle trotzdem lohnt", [
                "Ehrlich: Ab einer gewissen Größe kippt die Rechnung. Wenn bei dir das ganze Jahr durchgehend viel Marketing anfällt – täglich Content, laufende Kampagnen, ständig neue Projekte – dann kann eine eigene Kraft sinnvoll sein.",
                "Für die allermeisten kleineren Betriebe ist dieser Punkt aber noch weit weg. Bis dahin fährst du mit einem flexiblen Partner meist ruhiger und günstiger.",
            ]),
        ],
        key=[
            "Eine Stelle kostet ganzjährig – auch in ruhigen Monaten.",
            "Eine Person beherrscht selten alle Marketing-Disziplinen.",
            "Ein Partner skaliert mit deinem Bedarf – ohne Leerlauf-Kosten.",
            "Erst bei durchgehend hohem Volumen lohnt sich eine feste Stelle.",
        ],
        cta_h2="Klingt nach deiner Situation?",
        cta_lead="Genau dafür gibt es meine laufende Betreuung – flexibel, aus einer Hand, ohne feste Stelle.",
        published=True,
    ),

    # ---------- Branding: Begriffe ----------
    dict(
        slug="ratgeber-logo-cd-branding", cat="Branding", read="ca. 3 Min",
        title="Logo, Corporate Design, Branding – der Unterschied | DESIGNJ",
        desc="Logo, Corporate Design oder Branding – wo ist der Unterschied? Verständlich erklärt, mit einem Augenzwinkern und ohne Fachchinesisch.",
        teaser="Die drei Begriffe klar erklärt – und warum das wichtig ist.",
        eyebrow="Ratgeber · Branding", service_href="/branding", service_label="Branding",
        h1="Logo, Corporate Design,<br>Branding – der Unterschied",
        lead="Diese drei Begriffe werden ständig verwechselt.<br>Hier die schnelle Klarheit – ohne Vorlesung.",
        blocks=[
            ("Das Logo: dein Erkennungszeichen", [
                "Das Logo ist das eine Zeichen, an dem man dich erkennt. Wichtig – aber eben nur ein Baustein. Ein bisschen wie ein Gesicht: Man erkennt dich daran, aber es ist nicht die ganze Person.",
            ]),
            ("Corporate Design: der rote Faden", [
                "Corporate Design ist das ganze visuelle System drumherum: Logo plus Farben, Schriften, Layouts und Bildsprache. Die Regeln, die dafür sorgen, dass Visitenkarte, Website, Fahrzeug und Rechnung aussehen, als würden sie zusammengehören.",
                "Festgehalten wird das oft in einem Styleguide – damit alles einheitlich bleibt, egal wer gerade damit arbeitet.",
            ]),
            ("Branding: der Gesamteindruck", [
                "Branding ist der größte Begriff: wie deine Marke wirkt und wahrgenommen wird. Das Design ist ein großer Teil davon, aber auch dein Auftreten, deine Sprache und das, wofür du stehst, gehören dazu.",
            ]),
            ("Warum der Unterschied zählt", [
                "Ein Logo allein macht noch keine Marke – so wie ein schöner Türgriff noch kein Haus macht. Du brauchst selten alles auf einmal. Aber wenn du den Unterschied kennst, kannst du viel besser entscheiden, was du gerade wirklich brauchst.",
            ]),
        ],
        key=[
            "Logo = das Erkennungszeichen (ein Baustein).",
            "Corporate Design = das visuelle System drumherum.",
            "Branding = der Gesamteindruck deiner Marke.",
            "Ein Logo allein ist noch keine Marke.",
        ],
        cta_h2="Noch unsicher, was du brauchst?",
        cta_lead="Wir schauen gemeinsam, was für dich Sinn macht – vom Logo bis zur ganzen Markenwelt.",
        published=True,
    ),
    # ---------- Social: einheitlicher Look ----------
    dict(
        slug="ratgeber-einheitlicher-look", cat="Social Media", read="ca. 3 Min",
        title="Einheitlicher Look auf Social Media – so geht's | DESIGNJ",
        desc="Einheitlicher Look auf Social Media: Mit wenigen Farben, Schriften und Vorlagen baust du einen wiedererkennbaren Instagram- und Facebook-Auftritt.",
        teaser="So baust du einen wiedererkennbaren Auftritt – ohne Design-Studium.",
        eyebrow="Ratgeber · Social Media", service_href="/social-media", service_label="Social Media",
        h1="Einheitlicher Look<br>auf Social Media",
        lead="Wiedererkennung ist im Feed die halbe Miete.<br>Und das Gute: Das ist lernbar, keine Zauberei.",
        blocks=[
            ("Warum Wiedererkennung alles ist", [
                "Im Feed hast du einen Sekundenbruchteil. Ein einheitlicher Look sorgt dafür, dass man dich erkennt, <strong>bevor</strong> man den Namen liest. Und Wiedererkennung schafft Vertrauen.",
            ]),
            ("Die Zutaten für einen roten Faden", [
                "Viel braucht es nicht: ein paar feste Farben, ein bis zwei Schriften, ein gleichbleibender Bildstil und ein wiederkehrendes Layout. Nicht jeder Post muss identisch sein – es reicht die klare Familienähnlichkeit.",
            ]),
            ("Vorlagen sind dein bester Freund", [
                "Spontane Kreativität bei jedem einzelnen Post klingt romantisch, endet aber meist im Flickenteppich. Mit Vorlagen, die du nur noch befüllst, bleibt alles einheitlich – und geht nebenbei viel schneller.",
            ]),
            ("Weniger ist mehr", [
                "Nicht jede Schrift, jeden Filter und jede Farbe benutzen, nur weil es sie gibt. Gerade die Einschränkung macht dich wiedererkennbar.",
            ]),
        ],
        key=[
            "Im Feed entscheiden Sekundenbruchteile.",
            "Wenige Farben, 1–2 Schriften, ein Bildstil.",
            "Vorlagen halten alles einheitlich – und sparen Zeit.",
            "Einschränkung macht wiedererkennbar.",
        ],
        cta_h2="Auftritt, den man sofort erkennt?",
        cta_lead="Ich baue dir den Look und die Vorlagen – du bespielst sie ganz easy weiter.",
        published=True,
    ),
    # ---------- Print: Fahrzeugbeschriftung ----------
    dict(
        slug="ratgeber-fahrzeugbeschriftung", cat="Print", read="ca. 3 Min",
        title="Fahrzeugbeschriftung: Werbung, die 24/7 mitfährt | DESIGNJ",
        desc="Fahrzeugbeschriftung als Werbung: Warum dein Auto der günstigste Werbeträger ist, worauf es beim Motiv ankommt und was Teil- vs. Vollfolierung bringt.",
        teaser="Warum dein Auto der günstigste Werbeträger ist, den du hast.",
        eyebrow="Ratgeber · Print", service_href="/print-produktion", service_label="Print & Produktion",
        h1="Fahrzeugbeschriftung:<br>Werbung, die 24/7 mitfährt",
        lead="Dein Fahrzeug fährt eh jeden Tag durch die Gegend –<br>warum also nicht gleich für dich werben lassen?",
        blocks=[
            ("Der Werbeträger, den du schon hast", [
                "Dein Transporter steht täglich bei Kunden, an der Baustelle und an der Ampel. Eine Beschriftung ist Werbung, die ohne laufende Kosten arbeitet: einmal gemacht, jahrelang sichtbar.",
            ]),
            ("Weniger ist lesbar – mehr nicht", [
                "Bei Tempo 50 hat niemand Zeit, deine komplette Leistungsliste zu lesen. Drei Dinge reichen: Logo, was du machst, und wie man dich erreicht. Groß, klar und mit viel Kontrast – damit es in Sekunden hängen bleibt.",
            ]),
            ("Teil- oder Vollfolierung?", [
                "Eine Teilbeklebung (Schriftzüge und Logo) ist günstig, schnell und reicht in den meisten Fällen völlig. Eine Vollfolierung verwandelt das ganze Fahrzeug – maximale Wirkung, aber auch mehr Aufwand. Was sinnvoll ist, hängt von Ziel und Budget ab.",
            ]),
            ("Qualität zahlt sich aus", [
                "Gute Folie und eine saubere Montage halten jahrelang und sehen professionell aus. Billige Beklebung, die sich an den Ecken löst, wirkt dagegen schnell schlechter als gar keine. Hier lohnt es sich, es gleich richtig zu machen.",
            ]),
        ],
        key=[
            "Dein Fahrzeug ist ein Werbeträger, den du schon besitzt.",
            "Wenig Text, groß und kontrastreich – in Sekunden lesbar.",
            "Teil- oder Vollfolierung je nach Ziel und Budget.",
            "Gute Folie + saubere Montage halten jahrelang.",
        ],
        cta_h2="Soll dein Fahrzeug mitverdienen?",
        cta_lead="Von der Gestaltung bis zur Montage – ich mach dein Auto zur rollenden Werbefläche.",
        published=True,
    ),
    # ---------- Webdesign: bei Google gefunden ----------
    dict(
        slug="ratgeber-bei-google-gefunden", cat="Webdesign", read="ca. 4 Min",
        title="Bei Google gefunden werden – so klappt's lokal | DESIGNJ",
        desc="Bei Google gefunden werden: Mit Google-Unternehmensprofil, Bewertungen und einer sauberen Website verbessert ein lokaler Betrieb seine Sichtbarkeit.",
        teaser="Lokale Sichtbarkeit für kleine Betriebe – die ehrlichen Hebel.",
        eyebrow="Ratgeber · Webdesign", service_href="/webdesign", service_label="Webdesign",
        h1="Bei Google gefunden werden –<br>so klappt's lokal",
        lead="Die meisten Kunden googeln zuerst.<br>Gefunden zu werden schlägt dabei jeden<br>schicken Schriftzug – gerade lokal.",
        blocks=[
            ("Das Google-Unternehmensprofil zuerst", [
                "Der größte Hebel für lokale Sichtbarkeit ist kostenlos: das Google-Unternehmensprofil. Es zeigt dich in Maps und in dem Kasten rechts neben den Suchergebnissen – mit Öffnungszeiten, Telefonnummer und Bewertungen.",
                "Wichtig ist, dass es vollständig und aktuell ist: richtige Daten, ein paar gute Fotos, gepflegte Öffnungszeiten. Das klingt banal, macht aber einen riesigen Unterschied.",
            ]),
            ("Bewertungen sind Gold", [
                "Bewertungen wirken doppelt: Sie beeinflussen, wie weit oben du auftauchst – und sie schaffen Vertrauen beim nächsten Interessenten. Frag zufriedene Kunden aktiv danach. Ein paar ehrliche Sterne überzeugen mehr als jeder Werbespruch.",
            ]),
            ("Deine Website muss mitspielen", [
                "Google ist schlau, aber kein Hellseher – sag ihm, was du machst und wo. Eine klare, schnelle und mobil-taugliche Website, auf der dein Ort und deine Leistung im Text vorkommen, hilft Google, dich richtig einzuordnen.",
            ]),
            ("Geduld und dranbleiben", [
                "Lokale Sichtbarkeit ist kein Schalter, den man umlegt – sie wächst über Wochen. Dafür ist sie eine der ehrlichsten und langlebigsten Formen von Marketing: einmal gut aufgestellt, arbeitet sie dauerhaft für dich.",
            ]),
        ],
        key=[
            "Google-Unternehmensprofil ist der größte lokale Hebel.",
            "Bewertungen stärken Ranking und Vertrauen.",
            "Website: schnell, mobil, mit Ort + Leistung im Text.",
            "Lokale Sichtbarkeit wächst über Wochen – dranbleiben.",
        ],
        cta_h2="Online gefunden werden statt übersehen?",
        cta_lead="Ich baue dir eine Website, die Google – und deine Kunden – verstehen.",
        published=True,
    ),
    # ---------- Webdesign: Onepager oder Website ----------
    dict(
        slug="ratgeber-onepager-oder-website", cat="Webdesign", read="ca. 3 Min",
        title="Onepager oder große Website – was passt zu dir? | DESIGNJ",
        desc="Onepager oder große Website? Eine ehrliche Entscheidungshilfe, wann eine Onepage reicht und wann sich mehrere Seiten lohnen – auch fürs SEO.",
        teaser="Entscheidungshilfe je nach Ziel und Umfang.",
        eyebrow="Ratgeber · Webdesign", service_href="/webdesign", service_label="Webdesign",
        h1="Onepager oder große<br>Website – was passt zu dir?",
        lead="Mehr Seiten sind nicht automatisch besser.<br>Was zu dir passt, hängt von deinem Ziel ab –<br>hier die ehrliche Entscheidungshilfe.",
        blocks=[
            ("Was ein Onepager ist", [
                "Ein Onepager ist eine einzige, durchscrollbare Seite, die alles Wichtige in einem Fluss zeigt. Schnell, fokussiert und im Umfang überschaubar. Ideal für ein klares Angebot, als Web-Visitenkarte, für eine Kampagne oder einfach für den Start.",
            ]),
            ("Wann die große Website Sinn macht", [
                "Sobald du viele Leistungen, einen Ratgeber oder Blog, einen Shop oder einfach eine Menge Inhalte hast, helfen mehrere Seiten – den Besuchern und Google. Denn jede Seite kann für ihr eigenes Thema gefunden werden.",
            ]),
            ("Die ehrliche Entscheidungshilfe", [
                "Mehr Seiten füllen sich nicht von allein – lieber eine starke Seite als zehn halbleere. Fang lieber kompakt an und bau aus, wenn wirklich Inhalt dazukommt.",
            ]),
            ("Du musst dich nicht sofort festlegen", [
                "Wir nehmen das, was jetzt passt. Der Schritt vom Onepager zur großen Website ist später problemlos möglich – deine Seite darf mitwachsen.",
            ]),
        ],
        key=[
            "Onepager: eine Seite, fokussiert, schnell am Start.",
            "Große Website: bei vielen Themen + fürs SEO sinnvoll.",
            "Lieber eine starke Seite als zehn halbleere.",
            "Vom Onepager zur großen Website jederzeit möglich.",
        ],
        cta_h2="Unsicher, was für dich passt?",
        cta_lead="Wir finden den richtigen Umfang – und du kannst später jederzeit wachsen.",
        published=True,
    ),
]
