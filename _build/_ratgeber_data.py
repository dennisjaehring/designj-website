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
        slug="ratgeber-gutes-logo", cat="Branding", read="ca. 4 Min",
        title="Was macht ein gutes Logo aus? | DESIGNJ Ratgeber",
        desc="Was ein gutes Logo ausmacht: 4 Merkmale, an denen du ein starkes, zeitloses Logo erkennst – verständlich erklärt, ohne Fachchinesisch.",
        teaser="4 Merkmale, an denen du ein starkes Logo erkennst.",
        eyebrow="Ratgeber · Branding", service_href="/branding", service_label="Branding",
        hero_img="ratgeber_logo",
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
            ("Logo ist noch keine Marke", [
                "Das Logo ist der Anfang, nicht das Ganze. Erst mit festen Farben, Schriften und ein paar Regeln (einem Styleguide) wird daraus eine Marke, die überall gleich wirkt.",
                "Das Logo allein macht dich noch nicht wiedererkennbar – das Zusammenspiel von allem tut es.",
            ]),
            ("Woran du ein schwaches Logo erkennst", [
                "Warnzeichen sind: zu viele Details, Effekte oder Farbverläufe, schlechte Lesbarkeit in klein, Abhängigkeit von einem bunten Hintergrund – oder dass es verwechselbar mit anderen ist.",
                "Ein guter Gegentest: Funktioniert dein Logo auch in Graustufen und in Briefmarkengröße? Wenn ja, bist du auf der sicheren Seite.",
            ]),
        ],
        key=[
            "Einfach und auf einen Blick erkennbar.",
            "Funktioniert einfarbig und in jeder Größe.",
            "Zeitlos statt trendy – hält viele Jahre.",
            "Passt zu dir, nicht aus der Vorlage.",
            "Logo + Farben + Schrift = erst dann eine Marke.",
        ],
        faq=[
            ("Was kostet ein Logo?",
             "Die Kosten für ein Logo hängen vom Umfang ab – vom einzelnen Logo bis zum kompletten Branding. Erzähl mir dein Vorhaben, du bekommst ein individuelles Angebot."),
            ("Wie viele Entwürfe bekomme ich?",
             "Du bekommst mehrere durchdachte Richtungen zur Auswahl – danach verfeinere ich den Favoriten mit dir, bis er sitzt."),
            ("In welchen Dateien bekomme ich mein Logo?",
             "Dein Logo bekommst du in allen gängigen Formaten für Druck und Web – inklusive einfarbiger Varianten und der Dateien, die Druckereien brauchen. Auf Wunsch mit kurzem Styleguide."),
            ("Kann ich mein bestehendes Logo auffrischen lassen?",
             "Ein bestehendes Logo lässt sich beim Rebranding behutsam modernisieren: Ich baue auf dem Bestehenden auf und bringe es auf ein aktuelles, einheitliches Niveau – ohne dass dich deine Kunden plötzlich nicht mehr erkennen."),
        ],
        cta_h2="Zeit für ein Logo, das bleibt?",
        cta_lead="Ich entwickle dir eine Marke, die erkennbar ist und zu dir passt.",
        published=True,
    ),
    # ---------- Webdesign ----------
    dict(
        slug="ratgeber-website-ablauf", cat="Webdesign", read="ca. 4 Min",
        title="Website erstellen lassen: der Ablauf in 5 Schritten | DESIGNJ",
        desc="Website erstellen lassen: So läuft der Ablauf von der Idee bis online – in 5 verständlichen Schritten erklärt.",
        teaser="Von der Idee bis online – was wann passiert.",
        eyebrow="Ratgeber · Webdesign", service_href="/webdesign", service_label="Webdesign",
        h1="Website erstellen lassen:<br>der Ablauf in 5 Schritten",
        lead="Eine Website entsteht nicht über Nacht –<br>aber der Weg dahin ist klar und planbar.<br>So läuft's von der Idee bis online.",
        blocks=[
            ("1. Gespräch & Ziel", [
                "Zuerst finde ich mit dir heraus, was die Seite leisten soll: Kunden gewinnen, informieren, Termine bringen? Und wen du erreichen willst. Daraus ergibt sich alles Weitere – Umfang, Aufbau und Ton.",
                "Je klarer das Ziel, desto zielgerichteter wird die Seite. Dieser erste Schritt spart dir später am meisten Zeit.",
            ]),
            ("2. Struktur & Inhalte", [
                "Ich lege mit dir fest, welche Seiten es gibt und was wo steht. Gute Struktur heißt: Besucher finden sofort, was sie suchen – und Google versteht die Seite auch.",
                "Texte und Bilder trägst du zusammen; wo etwas fehlt, kümmere ich mich darum – von der Formulierung bis zum passenden Foto.",
            ]),
            ("3. Design & Entwurf", [
                "Jetzt bekommt die Seite ihr Gesicht – passend zu deiner Marke, mit klaren Farben und Schriften. Du siehst einen Entwurf, und wir feilen gemeinsam, bis es sitzt.",
                "So gibt es beim Umsetzen keine Überraschungen: Du weißt vorher, wie deine Seite aussieht.",
            ]),
            ("4. Umsetzung & Technik", [
                "Aus dem Entwurf wird die fertige Seite: sauber umgesetzt, schnell ladend, auf dem Handy genauso wie am Rechner. Domain, SSL und Hosting richte ich auf Wunsch gleich mit ein.",
                "Du musst dich um nichts Technisches kümmern – das läuft im Hintergrund.",
            ]),
            ("5. Launch & danach", [
                "Vor dem Livegang prüfe ich alles: Technik, Mobildarstellung, Google-Grundlagen. Nach dem Start kann die Seite jederzeit wachsen – auf Wunsch pflege ich sie laufend.",
                "So bleibt deine Seite aktuell, ohne dass du ständig daran denken musst.",
            ]),
        ],
        key=[
            "Erst Ziel klären, dann bauen.",
            "Struktur für Besucher UND Google.",
            "Entwurf vorab – keine Überraschungen.",
            "Responsiv & schnell: Handy wie Desktop.",
            "Nach dem Launch jederzeit erweiterbar.",
        ],
        faq=[
            ("Was kostet eine Website?",
             "Die Kosten für eine Website hängen vom Umfang ab – von der kompakten Web-Visitenkarte bis zur großen Seite. Erzähl mir dein Vorhaben, du bekommst ein individuelles Angebot."),
            ("Wie lange dauert es, bis meine Website online ist?",
             "Eine Website ist je nach Umfang in wenigen Tagen bis zu einigen Wochen online. Den genauen Zeitrahmen lege ich mit dir im ersten Gespräch fest."),
            ("Muss ich die Texte und Bilder selbst liefern?",
             "Vorhandene Texte und Bilder baust du gern ein – wo etwas fehlt, kümmere ich mich darum, von der Formulierung bis zum passenden Foto. Du musst nicht alles fertig liefern."),
            ("Kann ich die Website später erweitern?",
             "Deine Website lässt sich jederzeit erweitern. Auf Wunsch übernehme ich die laufende Pflege, oder ich richte sie so ein, dass du Inhalte selbst aktualisieren kannst."),
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
        slug="ratgeber-social-selbst-oder-auslagern", cat="Social Media", read="ca. 4 Min",
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
            ("Woran du merkst, dass du Hilfe brauchst", [
                "Wenn dein letzter Post Wochen her ist, der Look von Mal zu Mal anders aussieht oder dich das Posten eher stresst als Spaß macht – dann ist es Zeit, dir einen Teil abnehmen zu lassen.",
                "Das ist kein Scheitern, sondern Arbeitsteilung: Du machst, was dir liegt, den Rest übernehme ich.",
            ]),
            ("Was am Ende wirklich zählt", [
                "Nicht wer am meisten postet gewinnt, sondern wer verlässlich und wiedererkennbar auftritt. Lieber einmal pro Woche einheitlich als täglich zusammengewürfelt.",
                "Der einheitliche Look macht aus einzelnen Posts einen Auftritt, der im Kopf bleibt.",
            ]),
        ],
        key=[
            "Echte Momente fängst du selbst am besten ein.",
            "Schwachstelle ist meist die Konsistenz.",
            "Hybrid: Vorlagen von mir, Inhalte von dir.",
            "Keine Zeit? Dann übernehme ich komplett.",
            "Verlässlich & einheitlich schlägt viel & planlos.",
        ],
        faq=[
            ("Was kostet es, Social Media auszulagern?",
             "Die Kosten hängen vom Umfang ab – von einzelnen Vorlagen bis zur kompletten Betreuung. Du bekommst ein individuelles Angebot, passend zu dem, was du wirklich brauchst."),
            ("Wie viel Zeit kostet mich Social Media, wenn ich es selbst mache?",
             "Selbst gemacht brauchst du vor allem Regelmäßigkeit – mit einem fertigen Vorlagen-Set sind das oft nur ein paar Minuten pro Post. Ohne Vorlagen frisst vor allem das Gestalten die Zeit."),
            ("Welche Plattform ist die richtige für mich?",
             "Die richtige Plattform hängt davon ab, wo deine Kunden sind – für die meisten lokalen Betriebe sind das Instagram und Facebook. Lieber ein, zwei Kanäle richtig als fünf halbherzig."),
            ("Muss ich selbst vor die Kamera?",
             "Vor die Kamera musst du nicht. Oft wirken Fotos von deiner Arbeit, den Ergebnissen oder dem Team sogar besser – und die lassen sich ganz nebenbei einsammeln."),
        ],
        cta_h2="Unsicher, welcher Weg zu dir passt?",
        cta_lead="Ich finde mit dir den Mix, der zu deiner Zeit und deinen Zielen passt.",
        published=True,
    ),
    # ---------- Branche: Sport & Vereine ----------
    dict(
        slug="ratgeber-sponsoring-vereinssport", cat="Sport & Vereine", read="ca. 4 Min",
        title="Sponsoring im Vereinssport – worauf es ankommt | DESIGNJ",
        desc="Sponsoring im Vereinssport: Was Sponsoren wirklich wollen, was Vereine bieten können und wie gutes Design beiden hilft.",
        teaser="Wie Vereine attraktiv werden – und Sponsoren wirklich profitieren.",
        eyebrow="Ratgeber · Sport & Vereine", service_href="/sportmarketing", service_label="Sport & Vereine",
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
        slug="ratgeber-marketing-handwerk", cat="Handwerk", read="ca. 5 Min",
        title="Marketing fürs Handwerk: 5 Hebel, die sofort wirken | DESIGNJ",
        desc="Marketing fürs Handwerk: 5 einfache Hebel – von Fahrzeugbeschriftung bis Google-Profil – die zuverlässig für mehr Aufträge sorgen.",
        teaser="5 einfache Hebel, die zuverlässig Aufträge bringen.",
        eyebrow="Ratgeber · Handwerk", service_href="/marketing-fuers-handwerk", service_label="Handwerk & Bau",
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
            ("Womit du anfängst", [
                "Du musst nicht alles auf einmal machen. Fang mit dem an, was dich am sichtbarsten macht: meist das Fahrzeug und das Google-Profil. Der Rest kommt Schritt für Schritt dazu.",
                "Lieber zwei Dinge richtig als zehn halb – so bleibt es bezahlbar und wirkt trotzdem.",
            ]),
        ],
        key=[
            "Fahrzeugbeschriftung = Werbung, die 24/7 fährt.",
            "Bauzaun und Baustelle als Werbefläche nutzen.",
            "Google-Profil + einfache Website = auffindbar.",
            "Einheitlicher Auftritt schafft Vertrauen.",
            "Schritt für Schritt statt alles auf einmal.",
        ],
        faq=[
            ("Was bringt Marketing im Handwerk überhaupt?",
             "Marketing fürs Handwerk sorgt dafür, dass dich die richtigen Kunden und Mitarbeiter finden – auch wenn deine Arbeit top ist. Gute Arbeit allein spricht sich heute nicht mehr von selbst herum."),
            ("Womit sollte ich als Handwerksbetrieb anfangen?",
             "Am meisten bringt dir zuerst ein sauber beschriftetes Fahrzeug und ein gepflegtes Google-Profil – beides macht dich sofort sichtbar und auffindbar. Den Rest baust du Schritt für Schritt aus."),
            ("Brauche ich als Handwerker wirklich eine Website?",
             "Eine einfache, gute Website hilft im Handwerk vor allem bei zwei Dingen: gefunden werden und Vertrauen schaffen. Für den Anfang reicht oft eine kompakte Seite, die später mitwächst."),
            ("Hilft Marketing auch bei der Mitarbeitersuche?",
             "Ein sichtbarer, sympathischer Auftritt zieht nicht nur Kunden, sondern auch Bewerber an. Wer dich vom Fahrzeug, von Social oder der Website kennt, bewirbt sich leichter."),
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
        cta_lead="Ich schaue mit dir, was für dich Sinn macht – vom Logo bis zur ganzen Markenwelt.",
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
        hero_img="referenzen/designj_referenz_rupprecht_kappl_02",
        h1="Werbung an<br>deinem Fahrzeug,<br>die 24/7 mitfährt",
        lead="Dein Auto fährt eh jeden Tag durch die Gegend –<br>warum also nicht gleich für dich werben lassen?",
        blocks=[
            ("Der Werbeträger, den du schon hast", [
                "Dein Transporter steht täglich bei Kunden, an der Baustelle und an der Ampel. Eine Fahrzeugbeschriftung ist Werbung, die ohne laufende Kosten arbeitet: einmal gemacht, jahrelang sichtbar.",
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
                "Ich nehme das, was jetzt passt. Der Schritt vom Onepager zur großen Website ist später problemlos möglich – deine Seite darf mitwachsen.",
            ]),
        ],
        key=[
            "Onepager: eine Seite, fokussiert, schnell am Start.",
            "Große Website: bei vielen Themen + fürs SEO sinnvoll.",
            "Lieber eine starke Seite als zehn halbleere.",
            "Vom Onepager zur großen Website jederzeit möglich.",
        ],
        cta_h2="Unsicher, was für dich passt?",
        cta_lead="Ich finde mit dir den richtigen Umfang – und du kannst später jederzeit wachsen.",
        published=True,
    ),
    # ---------- Social Media ----------
    dict(
        slug="ratgeber-social-media-ideen", cat="Social Media", read="ca. 3 Min",
        title="Social-Media-Ideen: was posten, wenn dir nichts einfällt? | DESIGNJ",
        desc="Social-Media-Ideen für Unternehmen: einfache Content-Formate und ein Mini-Plan, damit dir nie wieder die Themen ausgehen – verständlich erklärt.",
        teaser="Content-Formate und ein Mini-Plan gegen den leeren Kopf.",
        eyebrow="Ratgeber · Social Media", service_href="/social-media", service_label="Social Media",
        h1="Was posten, wenn dir<br>nichts einfällt?",
        lead="Dir fehlt nicht die Zeit – dir fehlen die Ideen.<br>Mit ein paar festen Formaten postest du<br>regelmäßig, ohne jedes Mal neu zu grübeln.",
        blocks=[
            ("Denk in Formaten, nicht in Einzelposts", [
                "Der häufigste Fehler: jedes Mal bei null anfangen. Leichter wird's mit wiederkehrenden Formaten – „Schubladen“, die du immer wieder neu füllst.",
                "Ein paar, die bei fast jedem Betrieb funktionieren: Vorher/Nachher, „So entsteht …“, häufige Kundenfragen, ein Blick hinter die Kulissen, fertige Projekte.",
            ]),
            ("Zeig, was du sowieso machst", [
                "Du musst nichts inszenieren. Das echte Tagesgeschäft ist der beste Content: die Baustelle, der frisch beklebte Transporter, das fertige Logo auf dem Schreibtisch.",
                "Mach dir zur Gewohnheit, nebenbei ein, zwei Fotos zu knipsen – dann hast du Material, wenn du es brauchst.",
            ]),
            ("Ein Mini-Plan reicht", [
                "Du brauchst keinen ausgefeilten Redaktionsplan. Leg dir 3–4 Formate fest und einen festen Tag pro Woche. Das schlägt „viel auf einmal und dann wochenlang nichts“.",
                "Regelmäßig und ruhig ist besser als sporadisch und hektisch – für dich und für den Algorithmus.",
            ]),
        ],
        key=[
            "In Formaten denken statt in Einzelposts.",
            "Das echte Tagesgeschäft ist dein bester Content.",
            "3–4 Formate + fester Tag = genug.",
            "Regelmäßig schlägt viel-auf-einmal.",
        ],
        cta_h2="Keine Lust, selbst zu grübeln?",
        cta_lead="Ich entwickle dir Vorlagen und einen Plan, mit dem Posten leicht von der Hand geht.",
        published=True,
    ),
    dict(
        slug="ratgeber-reel-post-story", cat="Social Media", read="ca. 3 Min",
        title="Reel, Post oder Story – was bringt was? | DESIGNJ Ratgeber",
        desc="Reel, Post oder Story: Was die drei Formate können und wann du welches nimmst – einfach erklärt, damit sich dein Social-Media-Aufwand lohnt.",
        teaser="Welches Format wofür – und wann sich was lohnt.",
        eyebrow="Ratgeber · Social Media", service_href="/social-media", service_label="Social Media",
        h1="Reel, Post oder Story –<br>was bringt was?",
        lead="Drei Formate, drei Jobs. Wer sie auseinanderhält,<br>spart Aufwand und erreicht die richtigen Leute<br>zur richtigen Zeit.",
        blocks=[
            ("Reels: für neue Leute", [
                "Kurze Videos werden am breitesten ausgespielt – auch an Menschen, die dir noch nicht folgen. Reels sind dein Werkzeug für Reichweite und neue Kontakte.",
                "Es muss kein Hochglanz sein. Ein ehrlicher Clip vom Arbeiten funktioniert oft besser als perfekt Produziertes.",
            ]),
            ("Posts: fürs Schaufenster", [
                "Der normale Feed-Post bleibt auf deinem Profil und baut dein „Schaufenster“ auf. Hierhin gehören deine besten Ergebnisse, Referenzen und Kernbotschaften.",
                "Wer dich prüft, bevor er anfragt, schaut genau hierhin.",
            ]),
            ("Stories: für die Stammgäste", [
                "Stories verschwinden nach 24 Stunden und erreichen vor allem, wer dir eh folgt. Perfekt für Alltag, Schnelles, Persönliches – und um in Erinnerung zu bleiben.",
                "Merksatz: Reel für Reichweite, Post fürs Schaufenster, Story für die Bindung.",
            ]),
        ],
        key=[
            "Reel = Reichweite und neue Leute.",
            "Post = dein dauerhaftes Schaufenster.",
            "Story = Bindung zu bestehenden Followern.",
            "Der Mix macht's – nicht nur ein Format.",
        ],
        cta_h2="Content, der zu dir passt?",
        cta_lead="Ich gestalte dir Vorlagen für Reels, Posts und Stories in einem einheitlichen Look.",
        published=True,
    ),
    # ---------- Sport & Vereine ----------
    dict(
        slug="ratgeber-trikot-banden-sponsoring", cat="Sport & Vereine", read="ca. 3 Min",
        title="Trikot- & Bandenwerbung: Was bringt Sponsoring? | DESIGNJ",
        desc="Trikot- und Bandenwerbung: Was Sponsoring deinem Unternehmen wirklich bringt, worauf es beim Logo ankommt und wie du mehr herausholst.",
        teaser="Was Trikot & Bande dem Sponsor wirklich bringen.",
        eyebrow="Ratgeber · Sport & Vereine", service_href="/sportmarketing", service_label="Sportmarketing",
        hero_img="sport_beispiel_01",
        h1="Trikot & Bande:<br>was bringt dir das als Sponsor?",
        lead="Sponsoring ist mehr als ein Logo auf Stoff.<br>Richtig gemacht, bringt es Sichtbarkeit,<br>Sympathie und lokale Kundschaft.",
        blocks=[
            ("Sichtbarkeit, Woche für Woche", [
                "Ein Logo auf Trikot oder Bande läuft jedes Spiel mit – vor Zuschauern, auf Fotos, in Vereins-Posts. Das ist dauerhafte lokale Präsenz mit wenig Streuverlust.",
                "Wichtig: Dein Logo muss auch klein und aus der Distanz funktionieren. Verschnörkeltes verschwindet auf dem Trikot.",
            ]),
            ("Sympathie, die auf dich abfärbt", [
                "Wer den Verein vor Ort unterstützt, gilt als bodenständig und verbunden. Diese Sympathie überträgt sich – gerade im Handwerk und bei lokalen Betrieben ein echter Pluspunkt.",
                "Menschen kaufen lieber bei Firmen, die „auch was für die Gegend tun“.",
            ]),
            ("Mehr rausholen als nur das Logo", [
                "Das Maximum holst du, wenn du das Sponsoring sichtbar machst: ein Post „Wir unterstützen …“, ein Foto mit der Mannschaft, eine Erwähnung auf deiner Seite.",
                "So wird aus einem stillen Logo eine Geschichte, die Leute sehen und teilen.",
            ]),
        ],
        key=[
            "Dauerhafte lokale Sichtbarkeit, wenig Streuverlust.",
            "Logo muss klein und aus Distanz funktionieren.",
            "Die Sympathie des Vereins färbt auf dich ab.",
            "Sichtbar machen (Posts/Fotos) holt das Maximum raus.",
        ],
        cta_h2="Sponsoring, das man sieht?",
        cta_lead="Ich sorge dafür, dass dein Logo auf Trikot, Bande & Co. wirklich wirkt.",
        published=True,
    ),
    dict(
        slug="ratgeber-vereinsauftritt", cat="Sport & Vereine", read="ca. 3 Min",
        title="Vereinsauftritt aus einem Guss: Logo, Trikot, Social | DESIGNJ",
        desc="Vereinsauftritt aus einem Guss: Wie Logo, Trikot, Banden und Social Media zusammen ein starkes Vereinsbild ergeben – und mehr Sponsoren anziehen.",
        teaser="Logo, Trikot, Banden & Social als ein starkes Bild.",
        eyebrow="Ratgeber · Sport & Vereine", service_href="/sportmarketing", service_label="Sportmarketing",
        hero_img="sport_beispiel_02",
        h1="Vereinsauftritt,<br>der zusammenpasst",
        lead="Ein Verein wirkt stark, wenn alles zusammenspielt –<br>vom Logo übers Trikot bis zum Instagram-Kanal.<br>Aus einem Guss statt zusammengewürfelt.",
        blocks=[
            ("Ein Logo als Anker", [
                "Alles beginnt beim Vereinslogo. Es muss auf Trikot, Bande, Urkunde und Handy gleichermaßen funktionieren – also klar, einfarbig-tauglich und in jeder Größe lesbar.",
                "Ein aufgeräumtes Logo macht alles danach leichter.",
            ]),
            ("Überall derselbe Look", [
                "Trikot, Banden, Aushänge, Social-Grafiken, Urkunden – wenn alles dieselben Farben, Schriften und das gleiche Logo nutzt, wirkt der Verein professionell und wiedererkennbar.",
                "Das ist kein Luxus: Ein einheitlicher Auftritt macht Vereine auch für Sponsoren attraktiver.",
            ]),
            ("Social hält den Verein lebendig", [
                "Ein gepflegter Instagram- oder Facebook-Kanal mit einheitlichen Vorlagen (Spieltag, Ergebnis, Neuzugang) hält Mitglieder, Fans und Sponsoren bei der Stange.",
                "Mit fertigen Vorlagen füllt das auch ein ehrenamtliches Team locker.",
            ]),
        ],
        key=[
            "Logo als Anker: klar, einfarbig-tauglich, skalierbar.",
            "Überall gleiche Farben/Schriften = professionell.",
            "Einheitlicher Auftritt zieht Sponsoren an.",
            "Social mit Vorlagen hält den Verein lebendig.",
        ],
        cta_h2="Zeit für einen runden Vereinsauftritt?",
        cta_lead="Ich bringe Logo, Trikot, Banden und Social in einen einheitlichen Look.",
        published=True,
    ),
    # ---------- Handwerk ----------
    dict(
        slug="ratgeber-mitarbeiter-finden", cat="Handwerk", read="ca. 3 Min",
        title="Mitarbeiter finden übers eigene Marketing | DESIGNJ Ratgeber",
        desc="Mitarbeiter finden im Handwerk: Wie du mit Website, Social Media und Fahrzeug die richtigen Leute anziehst – ohne teure Stellenportale.",
        teaser="Wie dein eigener Auftritt die richtigen Leute anzieht.",
        eyebrow="Ratgeber · Handwerk", service_href="/marketing-fuers-handwerk", service_label="Marketing fürs Handwerk",
        hero_img="handwerk_hero",
        h1="Mitarbeiter finden –<br>mit deinem eigenen Auftritt",
        lead="Gute Leute suchen sich ihren Arbeitgeber aus.<br>Wer sichtbar und sympathisch auftritt,<br>bekommt die besseren Bewerbungen.",
        blocks=[
            ("Deine Website ist das erste Bewerbungsgespräch", [
                "Wer bei dir anfangen will, schaut dich vorher an – Website und Social. Finden sie dort echte Bilder, ein eingespieltes Team und klare Infos, bewerben sie sich eher.",
                "Eine kurze „Jobs/Team“-Seite mit ehrlichen Fotos wirkt oft mehr als die zehnte Stellenanzeige.",
            ]),
            ("Zeig das Team, nicht nur die Maschinen", [
                "Menschen bewerben sich bei Menschen. Gesichter, Alltag, Zusammenhalt – das zieht mehr als Hochglanz-Technik. Zeig, wie es bei euch wirklich zugeht.",
                "Ein zufriedenes Team im Bild ist das beste Recruiting-Argument.",
            ]),
            ("Sichtbar sein, bevor du suchst", [
                "Wer dich schon kennt – vom beklebten Transporter, von Social, vom Schild an der Baustelle – bewirbt sich leichter. Recruiting fängt lange vor der Stellenanzeige an.",
                "Ein starker, sichtbarer Auftritt arbeitet im Hintergrund für dich, auch bei der Personalsuche.",
            ]),
        ],
        key=[
            "Website/Social = das erste Bewerbungsgespräch.",
            "Team zeigen schlägt Maschinen zeigen.",
            "Sichtbarkeit (Fahrzeug, Schild, Social) bringt Bewerbungen.",
            "Recruiting beginnt vor der Stellenanzeige.",
        ],
        cta_h2="Die richtigen Leute anziehen?",
        cta_lead="Ich mach deinen Betrieb so sichtbar, dass gute Bewerbungen von selbst kommen.",
        published=True,
    ),
    # ---------- Print ----------
    dict(
        slug="ratgeber-grossformat", cat="Print", read="ca. 3 Min",
        title="Banner, Rollup oder Plakat – wann was? | DESIGNJ Ratgeber",
        desc="Großformat-Werbung erklärt: Banner, Rollup oder Plakat – welches Format wofür und worauf du bei Material und Gestaltung achten musst.",
        teaser="Welches Großformat sich wofür wirklich eignet.",
        eyebrow="Ratgeber · Print", service_href="/print-produktion", service_label="Print & Produktion",
        hero_img="handwerk_beispiel_01",
        h1="Banner, Rollup oder Plakat –<br>wann was?",
        lead="Großformat wirkt – wenn Format und Botschaft<br>zum Ort passen. Ein kurzer Überblick,<br>was wofür gemacht ist.",
        blocks=[
            ("Banner: für draußen & dauerhaft", [
                "Das Banner (meist PVC-Plane mit Ösen) ist der Allrounder für außen: Bauzaun, Fassade, Sportplatz-Bande. Robust, wetterfest und auf großer Fläche günstig.",
                "Faustregel: je größer die Distanz zum Betrachter, desto größer Logo und Schrift – und desto weniger Text.",
            ]),
            ("Rollup: für drinnen & mobil", [
                "Das Rollup steht in Sekunden: Messe, Empfang, Veranstaltung, Ladenlokal. Du ziehst es aus der Kassette, fertig. Ideal, wenn du flexibel bleiben willst.",
                "Das Wichtigste gehört ins obere Drittel – unten verdecken es oft Köpfe und Tische.",
            ]),
            ("Plakat: für den Blick im Vorbeigehen", [
                "Plakate (A1, A0 …) leben von einer einzigen klaren Botschaft. Wer im Vorbeigehen nur zwei Sekunden hat, braucht eine Aussage, nicht fünf.",
                "Ein Gedanke, ein großes Bild, ein klarer Aufruf – der Rest lenkt nur ab.",
            ]),
        ],
        key=[
            "Banner = außen, robust, große Fläche.",
            "Rollup = drinnen, mobil, schnell aufgebaut.",
            "Plakat = eine klare Botschaft fürs Vorbeigehen.",
            "Je weiter weg der Betrachter, desto weniger Text.",
        ],
        cta_h2="Großformat, das sitzt?",
        cta_lead="Ich gestalte und produziere Banner, Rollups und Plakate, die aus der Distanz wirken.",
        published=True,
    ),
    dict(
        slug="ratgeber-visitenkarte", cat="Print", read="ca. 3 Min",
        title="Die Visitenkarte, die hängenbleibt | DESIGNJ Ratgeber",
        desc="Visitenkarte gestalten lassen: Was eine Karte wirklich gut macht – Material, Veredelung und die Infos, die draufgehören (und die nicht).",
        teaser="Was eine Visitenkarte wirklich gut macht.",
        eyebrow="Ratgeber · Print", service_href="/print-produktion", service_label="Print & Produktion",
        hero_img="kontakt_setup",
        h1="Die Visitenkarte,<br>die hängenbleibt",
        lead="Die Visitenkarte ist oft dein erster Eindruck<br>zum Anfassen. Ein bisschen Sorgfalt macht<br>aus Papier einen bleibenden Eindruck.",
        blocks=[
            ("Weniger drauf ist mehr", [
                "Name, was du machst, ein Weg dich zu erreichen, das Logo – mehr braucht's meist nicht. Eine überfüllte Karte wirkt hektisch und wird eher weggelegt.",
                "Lieber eine klare Info gut lesbar als acht kleine, die niemand entziffert.",
            ]),
            ("Das Material fühlt man", [
                "Eine Karte wird angefasst – und gutes Papier spürt man sofort. Etwas dickerer Karton oder eine dezente Veredelung (matt, Prägung, Spotlack) hebt dich vom 08/15-Stapel ab.",
                "Dieser kurze Moment „oh, die ist ja wertig“ bleibt hängen.",
            ]),
            ("Teil deines großen Ganzen", [
                "Die Visitenkarte steht nie allein: Farben, Schrift und Logo sollten zu Website, Fahrzeug und Schild passen. So wirkt alles wie aus einer Hand.",
                "Eine Karte, die zum Rest passt, verstärkt deine Marke bei jedem Handschlag.",
            ]),
        ],
        key=[
            "Nur das Nötige drauf – klar lesbar.",
            "Gutes Papier/Veredelung fühlt man sofort.",
            "Muss zu Website, Fahrzeug & Logo passen.",
            "Erster Eindruck zum Anfassen – nutz ihn.",
        ],
        cta_h2="Eine Karte, die man behält?",
        cta_lead="Ich gestalte und drucke dir Visitenkarten, die zu deiner Marke passen und wertig wirken.",
        published=True,
    ),
    # ---------- Marketing / Lokal ----------
    dict(
        slug="ratgeber-lokal-gefunden-werden", cat="Marketing", read="ca. 5 Min",
        title="Lokal gefunden werden: dein Google-Unternehmensprofil | DESIGNJ",
        desc="Lokal gefunden werden: Wie du mit dem Google-Unternehmensprofil, Bewertungen und einheitlichen Daten in deiner Region ganz oben auftauchst.",
        teaser="Wie du in deiner Region ganz oben auftauchst.",
        eyebrow="Ratgeber · Marketing", service_href="/marketing-betreuung", service_label="Marketing & Betreuung",
        hero_img="ratgeber_lokal",
        h1="Lokal gefunden werden",
        lead="Wenn jemand in deiner Nähe sucht,<br>willst du oben stehen.<br>Ein paar Grundlagen entscheiden,<br>ob Google dich deiner Region zuordnet.",
        blocks=[
            ("Das Google-Unternehmensprofil ist fast Pflicht", [
                "Der <a href=\"https://www.google.com/business/\" target=\"_blank\" rel=\"noopener\">kostenlose Eintrag</a> (früher „Google My Business“) ist für lokale Suchen der größte Hebel – er füllt die Karte und den Kasten rechts in der Google-Suche.",
                "Vollständig ausgefüllt, mit Kategorie, Öffnungszeiten, Leistungen und echten Fotos, schlägt er in der lokalen Suche fast jede Website.",
            ]),
            ("Die richtige Kategorie entscheidet", [
                "Die wichtigste Stellschraube ist deine Hauptkategorie – sie sagt Google, wofür du überhaupt infrage kommst. „Werbeagentur“ bringt dich bei anderen Suchen nach vorn als „Grafikdesigner“. Wähl die, die dein Kerngeschäft am besten trifft.",
                "Dazu passende Nebenkategorien und deine einzelnen Leistungen eintragen – so tauchst du bei mehr passenden Suchen auf, ohne zu verwässern.",
            ]),
            ("Überall dieselben Daten (NAP)", [
                "Name, Adresse und Telefon (im Marketing „NAP“ genannt) müssen überall zeichengenau gleich sein – Website, Google-Profil, Branchenbücher. Google wertet diese Übereinstimmung als Vertrauensbeweis.",
                "Schon unterschiedliche Schreibweisen der Telefonnummer oder „Str.“ statt „Straße“ können das Signal verwässern. Einmal sauber festlegen, überall gleich verwenden.",
            ]),
            ("Bewertungen sind lokale Währung", [
                "Echte Bewertungen gehören zu den stärksten Faktoren dafür, wer lokal oben steht – und sie schaffen Vertrauen bei neuen Kunden. Frag zufriedene Kunden aktiv (aber kauf dir nie welche).",
                "Schon ein, zwei neue Bewertungen pro Monat bringen dich über die Zeit spürbar nach vorn.",
            ]),
            ("Halt das Profil lebendig", [
                "Ein gepflegtes Profil rankt besser als eine Karteileiche. Lad regelmäßig echte Fotos hoch, schreib ab und zu einen kurzen Google-Beitrag (Angebot, Projekt, Neuigkeit) und beantworte Fragen, die dort auftauchen.",
                "Diese Aktivität signalisiert Google: Hier ist ein lebendiges Unternehmen – und genau das will die lokale Suche nach vorn stellen.",
            ]),
            ("Nicht nur Google: Bing, Apple & Verzeichnisse", [
                "Google ist der größte Hebel, aber nicht der einzige. Ein Eintrag bei Bing Places (ChatGPT & Copilot ziehen aus Bing) und bei Apple („Karten“/Siri) bringt dich auch dort auf die Landkarte.",
                "Dazu ein paar seriöse Branchenverzeichnisse – überall mit denselben Daten. Je mehr verlässliche Quellen dasselbe über dich sagen, desto sicherer ordnet dich auch die KI-Suche richtig ein.",
            ]),
        ],
        key=[
            "Hauptkategorie sorgfältig wählen – sie entscheidet, wofür du erscheinst.",
            "Google-Unternehmensprofil vollständig ausfüllen und pflegen.",
            "Name/Adresse/Telefon (NAP) überall zeichengleich.",
            "Echte Bewertungen aktiv einsammeln (nie kaufen).",
            "Auch Bing, Apple & Verzeichnisse mitnehmen – für Google UND KI-Suche.",
        ],
        faq=[
            ("Kostet ein Google-Unternehmensprofil etwas?",
             "Das Google-Unternehmensprofil ist komplett kostenlos – du brauchst nur ein Google-Konto und etwas Zeit fürs Einrichten. Wer keine Zeit hat, gibt es ab; ich richte es ein und pflege es."),
            ("Wie lange dauert es, bis ich lokal oben stehe?",
             "Lokale Sichtbarkeit baut sich über Wochen auf: Profil vollständig ausfüllen, Daten überall gleich halten und Schritt für Schritt Bewertungen sammeln. Es ist kein Schalter, sondern ein stetiger Prozess – der sich aber lohnt."),
            ("Brauche ich dafür eine eigene Website?",
             "Für die lokale Suche bringt dich schon ein gepflegtes Google-Unternehmensprofil weit – eine Website ist kein Muss. Sie verstärkt dein lokales Ranking aber deutlich, wenn Website und Profil dieselben Daten und denselben Auftritt zeigen."),
            ("Darf ich Kunden um Bewertungen bitten?",
             "Zufriedene Kunden aktiv um eine Google-Bewertung zu bitten ist erlaubt und sinnvoll. Nicht erlaubt ist, Bewertungen zu kaufen oder mit Rabatten zu belohnen – das verstößt gegen die Google-Richtlinien."),
        ],
        cta_h2="In deiner Region nach vorn?",
        cta_lead="Ich bringe deinen lokalen Auftritt auf Vordermann – von der Website bis zum Google-Profil.",
        published=True,
    ),
]
