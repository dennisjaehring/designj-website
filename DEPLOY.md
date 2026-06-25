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

## Livegang-Checkliste (designj.de)

- [ ] `noindex` entfernen → `index, follow`
- [ ] **FormSubmit aktivieren:** erstes echtes Absenden vom Live-Formular → Bestätigungsmail an info@designj.de anklicken
- [ ] FormSubmit: auf **verschlüsselten Endpoint** umstellen (statt offener E-Mail im Code) – optional eigene „Danke"-Seite (`_next`)
- [ ] Host: **gzip/brotli** aktiv (meist Standard), HTTPS aktiv
- [ ] **Google PageSpeed/Lighthouse** prüfen, ggf. nachschärfen
- [ ] Sitemap.xml + robots.txt ergänzen (optional, SEO)
- [ ] Datenschutz/Impressum final gegenlesen (juristisch)
- [ ] Offene Bilder eingebaut (Porträts, Container, Projektbilder)
