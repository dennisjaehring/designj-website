# DESIGNJ – Deploy & Workflow

Statische Website (HTML/CSS/JS). Kein Build nötig – die Dateien werden 1:1 ausgeliefert.

## Der Ablauf in Kurzform

1. **Ändern** – lokal in `~/designj-website` (mit Claude: „ändere X", Claude setzt um).
2. **Lokal ansehen** – Vorschau-Server starten:
   ```
   cd ~/designj-website
   python3 -m http.server 8770
   ```
   → im Browser `http://localhost:8770` öffnen. Hier siehst du alles **zuerst**, bevor es live geht.
3. **Live bringen** – Änderungen committen & pushen:
   ```
   git add -A
   git commit -m "Kurze Beschreibung der Änderung"
   git push
   ```
   → der Host (Cloudflare Pages) deployt **automatisch** → in ~1 Minute live.
4. **Rückgängig** – alte Version jederzeit wiederherstellbar (Commit zurücksetzen oder im Cloudflare-Dashboard einen früheren Deploy „rollback").

## Einmalige Einrichtung

### A) GitHub (Versionen)
1. Account auf github.com (kostenlos).
2. Neues, **leeres** Repository anlegen, z. B. `designj-website` (privat ist ok).
3. Lokal verbinden & hochladen (Auth einmalig nötig, z. B. via `brew install gh && gh auth login`):
   ```
   git remote add origin https://github.com/<DEIN-USER>/designj-website.git
   git branch -M main
   git push -u origin main
   ```

### B) Hosting mit Auto-Deploy – Empfehlung: Cloudflare Pages (kostenlos)
1. Account auf cloudflare.com → **Workers & Pages** → **Pages** → **Connect to Git** → das GitHub-Repo wählen.
2. Build-Einstellungen: **Framework = None**, Build command **leer**, Output directory **`/`** (Root). → Deploy.
3. **Custom Domain** hinzufügen: `www.dennisj.de` (Test) → Cloudflare zeigt die nötigen DNS-Einträge.
4. Bei **IONOS** (Domain dennisj.de): DNS entsprechend setzen (CNAME/Nameserver wie von Cloudflare angegeben).

> Alternativen: **IONOS Deploy Now** (bleibt bei IONOS, auch Git-basiert) oder klassisch **FTP-Upload** der Dateien auf IONOS-Webspace.

## Test (dennisj.de) → Produktion (designj.de)

- **Test-Phase auf dennisj.de:** Suchmaschinen aussperren, damit der Test **nicht** bei Google landet:
  - Cloudflare/Netlify: Header `X-Robots-Tag: noindex` für die Test-Domain setzen, **oder**
  - in allen Seiten `<meta name="robots" content="index, follow">` → `noindex, nofollow` (Claude macht das per Skript, einmal hin, einmal zurück).
- **Umzug auf designj.de:** Dieselben Dateien deployen. Es muss **nichts** im Code geändert werden:
  - interne Links sind **relativ** → laufen auf jeder Domain,
  - Canonical/OG/JSON-LD zeigen **bereits auf designj.de**.
  - Dann: `noindex` **raus** (auf index) und **FormSubmit aktivieren** (siehe unten).

## ⚠️ Domain-Umzug zu Cloudflare – MAIL-SICHER & OHNE AUSFALL

> Gilt für **designj.de** (dort läuft die Geschäfts-Mail `info@designj.de`) **und** für `dennisj.de` (private Mail). Ein Nameserver-Umzug **verschiebt die Postfächer NICHT** – die Mails bleiben physisch bei IONOS. Wir ändern nur, **wo die DNS gehostet wird**, und kopieren jeden Eintrag **1:1**. Solange die **MX-Einträge identisch** bleiben, merkt die E-Mail vom Umzug nichts.

**Vorbereitung (Tage vorher):**
- [ ] In IONOS **alle** DNS-Einträge von designj.de auflisten + sichern (Screenshot **und** Textdatei). Kritisch:
  - [ ] **MX** (Maileingang) – Werte + Prioritäten notieren
  - [ ] **TXT/SPF** (`v=spf1 …`)
  - [ ] **TXT/DKIM** (`<selector>._domainkey…`)
  - [ ] **TXT/DMARC** (`_dmarc…`)
  - [ ] Mail-CNAMEs: `imap`, `smtp`, `mail`, `autoconfig`, `autodiscover`, ggf. `webmail`
  - [ ] Website-Einträge (A/AAAA/CNAME) – damit die ALTE Seite während des Umzugs online bleibt
  - [ ] sonstige (z. B. Verifizierungs-TXT)
- [ ] **TTL** der Einträge bei IONOS auf niedrig stellen (z. B. 300 s / 5 Min), 1 Tag vorher → Änderungen greifen dann schnell.

**Umzug Schritt für Schritt:**
1. [ ] designj.de in Cloudflare einhängen (Add a domain, Free-Plan). Cloudflare scannt vorhandene Einträge.
2. [ ] **Jeden** Eintrag gegen die IONOS-Liste abgleichen – besonders MX + alle Mail-TXT. Fehlende **manuell nachtragen**. Website-A/CNAME zunächst auf den **bisherigen** Host zeigen lassen (alte Seite bleibt live), Proxy für Mail-Einträge **aus** (grau).
3. [ ] Erst wenn **kein** Mail-Eintrag fehlt: bei IONOS Nameserver auf die 2 Cloudflare-Nameserver umstellen.
4. [ ] Auf Cloudflare-Status **„Active"** warten (Min. bis Std.). → Von außen ändert sich nichts.
5. [ ] **Mail-Test:** Test-Mail an `info@designj.de` senden + von dort eine raus → Ein-/Ausgang bestätigt. Alte Website weiterhin erreichbar prüfen.
6. [ ] **Erst jetzt** Website-Cutover: Worker `designj-website` → Domains `www.designj.de` + `designj.de` hinzufügen (Cloudflare setzt A/CNAME auf den Worker, SSL automatisch). Wirkt in Sekunden (NS liegen schon auf CF).
7. [ ] Neue Seite auf beiden URLs prüfen (inkl. http→https, www↔nackt-Redirect).

**Sicherheitsnetze:**
- **Rollback Website:** Worker-Domain entfernen / A-CNAME zurück auf alten Host → alte Seite sofort wieder da. Mail ist davon nie betroffen.
- **Timing:** abends / ruhige Zeit, nicht Freitagnachmittag.
- Postfächer + IONOS-Mailhosting bleiben unangetastet – nur die DNS-Verwaltung wandert.

## Livegang-Checkliste (designj.de)

- [ ] `noindex` entfernen → `index, follow`
- [ ] **FormSubmit aktivieren:** erstes echtes Absenden vom Live-Formular → Bestätigungsmail an info@designj.de anklicken
- [ ] FormSubmit: auf **verschlüsselten Endpoint** umstellen (statt offener E-Mail im Code) – optional eigene „Danke"-Seite (`_next`)
- [ ] Host: **gzip/brotli** aktiv (meist Standard), HTTPS aktiv
- [ ] **Google PageSpeed/Lighthouse** prüfen, ggf. nachschärfen
- [ ] Sitemap.xml + robots.txt ergänzen (optional, SEO)
- [ ] Datenschutz/Impressum final gegenlesen (juristisch)
- [ ] Offene Bilder eingebaut (Porträts, Container, Projektbilder)
