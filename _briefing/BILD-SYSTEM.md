# DESIGNJ – Bild-System (Vorlage & Regeln)

> Verbindliches Regelwerk für alle Nischen-/Kampagnen-Bilder (Firefly) – Homepage **und** Social.
> Zweck: gesicherte Basis, damit jede neue Bild-Anfrage sofort stil- und formatkonform umgesetzt werden kann.
> Keine konkreten Einzel-Prompts hier – nur **Stil, Farben, Art & Weise, Formate**.
> Zuletzt aktualisiert: 2026-07-17.

---

## 1. Stil (gilt für ALLE Bilder)

- Helle, natürliche, **premium** Mockup-Fotografie; weiches Tageslicht; geringe Tiefenschärfe; leichter Winkel.
- Ausnahme Hero → siehe Formate (schwarzer Tisch, siehe unten).
- **Kein lesbarer Text** – Inhalte nur als angedeutete **graue Platzhalter-Linien** + Icons.
  Erlaubt ist **gezielt eine kurze, korrekt geschriebene Headline**, wo bewusst gewünscht
  (z. B. „Willkommen in unserer Praxis", „KARRIERE", „KANZLEI", „ZU VERKAUFEN").
- **Kein Englisch, kein Kauderwelsch, keine erfundenen Wörter.**
- Druckstücke (Flyer/Broschüre/Ausstattung): **Flat-Lay direkt von oben**, flach auf dem Tisch liegend
  (nicht aufgestellt/angelehnt).
- Zurückhaltender Farbeinsatz: **schlanke Akzente**, viel Weißraum – keine großen Farbflächen,
  außer bewusst gewünscht.
- **Pro Seite jedes Motiv nur einmal** – niemals dasselbe Bild doppelt auf einer Seite
  (v. a. SEO-Seiten: bio-Block oben + kmp-shots dürfen sich nicht wiederholen).

## 2. Farben je Nische (Hex aus CSS)

| Nische | Akzent (Klammer) | Hex |
|---|---|---|
| Immobilien | Cyan / Azurblau | `#28AEE6` |
| Kanzlei | Bordeaux / Weinrot | `#A3283F` |
| Praxis | Mint-Grün / Petrol | `#1FC4A8` |

Akzentfarbe immer als **Hex im Prompt** nennen (Firefly trifft den Ton sonst nicht zuverlässig).

## 3. Logo / Icon

- Generisch & **abstrakt**, **kräftig** (keine feinen dünnen Linien), keine Buchstaben.
- **Verboten:** Waage, medizinisches Kreuz/Plus, sowie **alles, was auch nur grob** an ein
  Hakenkreuz oder eine eckige hakenförmige Vierarm-/Pinwheel-Form erinnert.
- Im Zweifel: **runde/weiche** Marke (Kreis, sanfte geometrische Form).
- Auf Druckstücken/Flyern oft **ganz weglassen**, wenn es nichts hinzufügt.

## 4. Formate & Maße

| Format | Verwendung | Verhältnis | Pixel | Szene |
|---|---|---|---|---|
| **Quadratisch – Hero** | Nischen-Hero oben | **1:1** | **1024 × 1024** | Objekt-Stillleben auf **schwarzem, glattem Tisch**, nischentypische Requisiten + Akzentfarbe als Detail |
| **Quer – Beispiele** | Best-Case-Mockups | **3:2** | **1264 × 848** | helle, natürliche Premium-Mockups (Website, Print, Social, Schild …) auf hellem Tisch |
| **Hochformat – Social** *(geplant)* | Social-Media-Posts | **4:5** | z. B. **1080 × 1350** | wird definiert, sobald die Social-Vorlage steht |

**Hero-Regel:** dunkel, edel, ruhig – Requisiten (z. B. Laptop, Notizbuch, nischentypische Objekte)
auf einer **schwarzen, glatten Tischplatte**, dezent die Akzentfarbe der Nische. Bewusst anderer
Look als die hellen Beispiel-Mockups.

Alle Bilder als **WebP, Qualität ~82**.

## 5. Dateinamen

- Hero: `{nische}_hero.webp` (1024²)
- Beispiele: `{nische}_beispiel_01–04.webp` (1264×848)
- Social (geplant): `{nische}_social_XX.webp` (4:5) – Schema final, wenn Vorlage steht
- `{nische}` = `immobilien` | `kanzlei` | `praxis` | …

## 6. Prompt-Regeln (Art & Weise)

- **Ein** einzelner, kompletter **Fließtext-Prompt** – keine Zusatz-/Avoid-Felder.
- **Maximal ~900 Zeichen** (Firefly schneidet länger ab).
- Immer enthalten: Stil (bright/natural/premium), **Format** (`3:2` / `1:1` / `4:5`),
  **Akzent-Hex**, Text-Regel (nur graue Platzhalter, evtl. eine definierte Headline),
  Logo-Regel (oder „no logo"), Requisiten/Setting.
- Bei „liegt nicht flach": „**flat-lay shot directly from above … lying completely flat … not standing, not propped, not leaning**".
- Marken-/Gerätelogos vermeiden: „**plain laptop with no visible brand name**".

## 7. Ablauf (Pipeline)

1. Anfrage → passender Prompt nach diesen Regeln (Farbe-Hex + Format der Nische).
2. In Firefly generieren, roh (richtiges Seitenverhältnis) in `_neu-kanzlei-praxis/` ablegen mit Ziel-Dateiname.
3. Claude: auf Zielmaß skalieren, nach `images/` legen, in Seiten verdrahten, Alt-Texte setzen.
4. Lokal prüfen (Desktop + Mobil) → committen/pushen + **Cache-Busting** (bei gleichem Dateinamen).
