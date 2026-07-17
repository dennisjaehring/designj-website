# DESIGNJ Website – Arbeitsanweisungen für Claude

Diese Website ist **LIVE** unter https://www.designj.de (Static Site, Cloudflare Pages).
**Nur Dennis** arbeitet daran – es gibt genau **einen** Klon: `~/Projekte/designj-website`.

## Goldene Regel bei JEDER Änderung (verbindlich)

1. **ZUERST immer `git pull`** (aktuellen Stand von `main` holen) – noch BEVOR
   Dateien gelesen oder geändert werden. Selbst ausführen, ohne Aufforderung.
   Das verhindert Divergenz/„alter Stand"-Probleme.
2. Änderung umsetzen und **lokal prüfen** (`python3 -m http.server` + Browser).
3. **`git commit` + `git push` auf `main`.** Der Push löst automatisch den
   Cloudflare-Deploy aus → in ~1 Minute live. Kein manueller Upload nötig.

> Ursache früherer „Konflikte": Es wurde lokal weitergearbeitet, ohne vorher
> `git pull` zu machen (Commits auf altem Stand, während GitHub schon weiter war).
> Mit Schritt 1 kann das nicht mehr passieren.

## Ein Ort für Änderungen

- **Immer hier in Claude Code**, im lokalen Repo. **Nicht** parallel über eine
  zweite/Cloud-Kopie editieren – sonst entstehen wieder zwei Stände.
- Wird ausnahmsweise doch woanders gearbeitet: dort ebenfalls strikt
  pull-first / push-after.

## Deploy / Hosting

- **Cloudflare Pages**, Deploy automatisch bei Push auf `main`.
- **Clean URLs:** Seiten laufen **ohne** `.html` (z. B. `/kanzlei`). Ein Aufruf
  mit `.html` gibt einen 307-Redirect auf die saubere URL – das ist normal.
- **Nicht öffentlich ausgeliefert** (via `.assetsignore`): `*.md`, `*.py`, `_build/`.
- **Nicht deployt** (via `.gitignore`): `_neu-kanzlei-praxis/`, `_seo/`, `_real/`,
  `_neue-fotos/`, `_bilder-optimieren/` u. a. Arbeitsordner.
- Nach dem Push kurz per `curl` gegen die **Clean-URLs** prüfen (200).

## Bilder / Kampagnen

- Zentrales Regelwerk für alle Nischen-/Kampagnen-Bilder: **`_briefing/BILD-SYSTEM.md`**
  (Stil, Farben je Nische, Maße, Dateinamen, Formate). Vor Bild-Arbeiten dort nachsehen.
- Roh-Firefly-Bilder in `_neu-kanzlei-praxis/` (nicht deployt), live in `images/`.
