# Villa del Conte

Sito di due case vacanze (La Villa e La Conte House) a Santa Domenica di Ricadi,
sulla Costa degli Dei. Pubblicato su https://villa-del-conte.com.

## Come e' fatto

Sito **statico vanilla**: HTML, CSS e JavaScript scritti a mano. Nessun bundler,
nessun framework, nessun `package.json`, nessuno step di build.

- `index.html` — pagina unica con quattro sezioni mostrate via tab JavaScript
  (Strutture, Notebook, Chi Siamo, FAQ)
- `blog-*.html` — sette pagine del Notebook, indipendenti
- `privacy.html`, `404.html` — pagine di servizio
- `script.js` — caroselli, lightbox, tab, accordion FAQ, cambio lingua, mappa
- `translations.js` — i18n in sei lingue (it, en, es, ru, de, zh) applicata lato
  client tramite attributi `data-i18n`
- `style.css` — tutto il CSS del sito
- `images/` — immagini servite, con varianti webp a 480/960/1600px;
  `images/_originals/` contiene i sorgenti ad alta risoluzione ed e' ignorata da git
- `tools/` — script Python di manutenzione, in gran parte **obsoleti**; l'unico che
  serve ancora regolarmente e' `optimize_images.py`

## Pubblicazione

Vercel pubblica automaticamente ogni push su `main`. **Non esiste CI e non esiste
staging: un push e' una pubblicazione immediata in produzione.** Prima di pushare,
esegui `/deploy-check`.

## Regole di lavoro

- **Una sola URL per tutte le lingue.** I testi cambiano lato client, quindi
  `hreflang` non va aggiunto finche' non esisteranno URL separate per lingua.
- **Le chiavi di traduzione vanno aggiunte in tutte e sei le lingue.** Una chiave
  presente solo in italiano produce uno spazio vuoto sul sito, senza nessun errore.
- **Le traduzioni passano da `sanitizeHtml`**, che ammette solo `<em>` e `<strong>`.
  Serve un link dentro un testo tradotto? Spezzalo in piu' chiavi e metti il tag
  `<a>` nell'HTML, non nella stringa.
- **Controlla che le immagini referenziate esistano.** Due immagini di apertura
  hanno dato 404 in produzione per mesi senza che nessuno se ne accorgesse.
- **Niente contenuti finti**: nessun avatar stock su recensioni reali, nessun
  dettaglio storico inventato nelle pagine del Notebook.
- Quando aggiungi una pagina del Notebook usa `/new-blog-post`, che aggancia anche
  home, sitemap, traduzioni e `llms.txt`.

## Strumenti configurati

- **Hook** (`.claude/hooks/validate.sh`): a ogni Edit o Write valida sintassi JS,
  parita' delle traduzioni, struttura HTML, JSON e XML. Blocca se trova errori.
- **Subagent**: `seo-auditor` (SEO tecnica e AIO), `a11y-reviewer` (WCAG 2.2 AA).
- **Skill**: `/deploy-check` prima di pubblicare, `/new-blog-post` per il Notebook.
- **Anteprima locale**: configurazione `villa-del-conte` in `.claude/launch.json`
  (`python3 -m http.server` sulla porta 4173).
- **MCP** (`.mcp.json`): `chrome-devtools` per Lighthouse e debug nel browser,
  `vercel` per i log di deploy. Richiedono approvazione al primo avvio.

## Cose ancora aperte

- Nessun sistema di analytics. Se ne aggiungi uno, scegline uno senza cookie
  (Plausible, PostHog) per non dover introdurre un banner di consenso.
- La mappa Google si carica solo al click dell'utente: e' la ragione per cui il
  sito non ha un cookie banner. Non reintrodurre embed di terze parti che partono
  da soli.
- `privacy.html` e' una bozza tecnicamente accurata ma non verificata da un legale.
