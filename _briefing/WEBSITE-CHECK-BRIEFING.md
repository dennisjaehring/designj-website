# Briefing: DESIGNJ Website-Checks (für Interessenten/Kunden)

> **Dieses Dokument in einen neuen Chat ziehen** – dann kennt Claude sofort den
> Rahmen und wir können direkt mit dem ersten Kunden-Check starten.
> Pro Kunde einfach die URL nennen, der Rest läuft nach diesem Schema.

---

## Wer ich bin (Kontext)

- **Dennis Jähring – DESIGNJ**, „(k)eine Werbeagentur", Einzelunternehmer aus
  Weiden/Oberpfalz. Design · Druck · Digital.
- Anlass dieser Checks: der Ratgeber **„PHP-Sicherheitslücke / PHP2Shell"**
  (`designj.de/php`). Leute schicken mir jetzt ihre Website-Adresse und fragen:
  *„Bin ich betroffen? Reicht ein Update oder lohnt ein Neuaufbau?"*
- Meine eigene Seite läuft **statisch auf Cloudflare, komplett ohne PHP** –
  das ist mein Verkaufsargument, aber **nie überheblich** rüberbringen.

---

## Harte Regeln (immer einhalten)

1. **Anrede:** immer **„du"/„ich"** (Einzelunternehmer). Nie „ihr/wir".
2. **Keine Preise** – nirgends. Nur Umfang beschreiben + „individuelles Angebot".
3. **Ehrlich bleiben:** Ein Check **von außen** ist eine **Einschätzung**, kein
   garantiertes Security-Audit. Für die Tiefe (Plugin-Versionen im Backend,
   Patch-Stand, Backups) braucht man Zugang. Das immer klar sagen.
4. **Keine erfundenen Zahlen / CVEs.** Nur nennen, was wirklich belegbar ist.
5. **Nicht angreifbar machen / nichts Aggressives:** nur **passive, öffentliche**
   Betrachtung der Seite (normale `GET`-Aufrufe, wie jeder Besucher).
   **KEINE** aktiven Schwachstellen-Scanner, **kein** Port-Scan, **keine**
   Login-Versuche, **kein** Brute-Force, **kein** Ausnutzen von Lücken.
   Alles, was über „anschauen, was öffentlich da ist" hinausgeht, braucht die
   **schriftliche Erlaubnis des Seiten-Inhabers**. Im Zweifel: nachfragen.
6. **Datenschutz:** keine Kundendaten/URLs an fremde Online-Dienste schicken, die
   der Kunde nicht kennt. Öffentliche Tools (z. B. Googles PageSpeed) sind ok,
   aber transparent benennen.

---

## Was ich von AUSSEN (nur URL, ohne Login) verlässlich sehen kann

| Bereich | Woran erkennbar |
|---|---|
| **Läuft PHP?** | HTTP-Header `X-Powered-By: PHP`, Cookie `PHPSESSID` |
| **WordPress?** | `/wp-login.php`, `/wp-admin/`, `/wp-content/`, `/wp-json/`, `readme.html`, `<meta name="generator" content="WordPress …">` |
| **WP-/Theme-Version** | `generator`-Meta, `?ver=` an CSS/JS, `readme.html`, Theme-Pfad in `/wp-content/themes/…` |
| **Offene Angriffsflächen** | erreichbares `xmlrpc.php`, Directory-Listing, `/wp-content/debug.log`, exponierte Login-Seite |
| **Verschlüsselung** | gültiges SSL-Zertifikat, erzwingt die Seite HTTPS?, `Strict-Transport-Security`-Header |
| **Security-Header** | `Content-Security-Policy`, `X-Frame-Options`, `X-Content-Type-Options`, `Referrer-Policy` vorhanden? |
| **Hoster/Setup** | `Server`-Header (Apache/nginx/IONOS/…), `cf-ray` (Cloudflare), IP/Reverse-DNS |
| **Pflege-Zustand** | veraltete WP-Version, alte Jahreszahl im Footer, tote Links, Mixed-Content |
| **Performance** | PageSpeed/Lighthouse-Score, Ladezeit, Bildgewicht |
| **Basis-SEO** | `<title>`, Meta-Description, `robots.txt`, `sitemap.xml`, saubere H-Struktur |
| **Mobil** | responsives Verhalten, Viewport-Meta |

## Was ich OHNE Zugang NICHT sicher sagen kann (ehrlich benennen)

- Exakter Patch-Stand von Core/Plugins im Backend.
- Ob die Seite **intern** schon kompromittiert ist.
- Ob Backups existieren / wie der Server konkret konfiguriert ist.
- Genaue PHP-Version des Servers (nur grob aus Headern ableitbar).

→ Darum ist das Ergebnis immer eine **Einschätzung + Empfehlung für den
nächsten Schritt**, kein abschließendes Gutachten.

---

## Ablauf pro Kunde (Schema)

1. **URL vom Kunden** entgegennehmen (ggf. mit/ohne `www`, beide prüfen).
2. **Passiv checken** (siehe Toolkit unten): Technik, PHP/WP?, Version, Header,
   SSL, offensichtliche Altlasten, PageSpeed.
3. **Einordnen** in eine von drei Stufen:
   - 🟢 **Ok / gepflegt** – läuft sauber, nur Kleinigkeiten.
   - 🟡 **Update/Wartung nötig** – veraltet, aber Substanz brauchbar.
   - 🔴 **Neuaufbau lohnt** – alt, verwundbar, träge; Modernisierung > Flicken.
4. **Ehrliche Empfehlung** formulieren: *„Update reicht"* vs. *„Neuaufbau ohne
   PHP lohnt sich"* – als **Einschätzung**, mit Begründung.
5. **Kundenantwort** im DESIGNJ-Ton (du/ich, keine Preise) nach Template unten.
6. Optional: kurze interne Notiz je Kunde (Datum, URL, Stufe, Empfehlung),
   damit wir hier den Überblick behalten.

---

## Toolkit (passive Checks per Terminal)

```bash
# 1) Grund-Header + läuft PHP?
curl -sI https://BEISPIEL.de | grep -iE 'server|x-powered-by|set-cookie|cf-ray|strict-transport|content-security|x-frame'

# 2) WordPress? (Statuscodes; 200/302 = existiert)
for p in wp-login.php wp-admin/ wp-json/ xmlrpc.php readme.html wp-content/debug.log; do
  printf "%-22s " "$p"; curl -s -o /dev/null -w "%{http_code}\n" "https://BEISPIEL.de/$p"
done

# 3) Generator-/Version-Meta
curl -s https://BEISPIEL.de | grep -iE 'generator|wp-content|\\?ver=' | head

# 4) HTTPS-Erzwingung (leitet http -> https um?)
curl -sI http://BEISPIEL.de | grep -iE 'location|http/'

# 5) SSL-Zertifikat (Gültigkeit/Aussteller)
echo | openssl s_client -connect BEISPIEL.de:443 -servername BEISPIEL.de 2>/dev/null | openssl x509 -noout -issuer -dates
```

> `BEISPIEL.de` jeweils durch die echte Kundendomain ersetzen.
> Performance separat über **PageSpeed Insights** (pagespeed.web.dev) prüfen.

---

## Antwort-Template an den Kunden (du-Form, keine Preise)

> Hi [Name],
>
> hab mir **[deine-seite.de]** mal von außen angeschaut – hier meine ehrliche
> Einschätzung:
>
> **Kurz gesagt:** [1 Satz – 🟢/🟡/🔴 + Kernaussage]
>
> **Was ich sehe:**
> - Technik: [z. B. WordPress x.y auf PHP] 
> - Zustand: [aktuell / veraltet / verwundbar – mit konkretem Punkt]
> - [ggf. Sicherheits-/Performance-Hinweis]
>
> **Wichtig & ehrlich:** Das ist eine Einschätzung **von außen** – für den
> genauen Patch-Stand im Backend bräuchte ich kurz Zugang. Aber für die Richtung
> reicht das.
>
> **Meine Empfehlung:** [Update/Wartung reicht] ODER [ein Neuaufbau ohne PHP
> lohnt sich, weil …].
>
> Wenn du magst, schauen wir gemeinsam drauf – ich mach dir dann ein
> individuelles Angebot. Meld dich einfach.
>
> Viele Grüße, Dennis

---

## So nutzen wir diesen Chat

- **Ein Chat = alle Website-Checks.** Pro Anfrage einfach: *„Neuer Check: URL = …"*
- Claude arbeitet das Schema oben ab, hält sich an die harten Regeln, und liefert
  am Ende **(a)** eine interne Kurz-Einordnung und **(b)** den fertigen
  Kunden-Text zum Rauskopieren.
- Bei „aktiveren" Wünschen (echter Vuln-Scan o. Ä.): erst Erlaubnis des Inhabers
  klären.
