---
name: new-blog-post
description: Crea una nuova pagina del Notebook (blog-*.html) con la struttura, i meta tag, il JSON-LD e i collegamenti gia' a posto, e la aggancia alla home, alla sitemap e alle traduzioni.
disable-model-invocation: true
---

# Nuova pagina del Notebook

Le sette pagine blog esistenti sono state clonate a mano, e ogni clonazione ha
portato con se' i suoi errori: code fence markdown rimasti nell'HTML, JSON-LD
mancante, meta tag dimenticati. Questa skill rifa' il percorso per intero.

## Cosa chiedere prima di iniziare

1. **Argomento e titolo** della pagina (il titolo diventa l'`h1`).
2. **Slug**: il nome file sara' `blog-<slug>.html`, tutto minuscolo, senza accenti.
3. **Immagini**: servono una immagine di testata e una secondaria. Se l'utente le
   fornisce come file originali, mettile in `images/_originals/blog/` (cartella
   ignorata da git) e genera le varianti ottimizzate con
   `python3 tools/optimize_images.py`, che produce `-480w`, `-960w` e `-1600w` in
   webp dentro `images/blog/`.
4. **Testo**: se l'utente non lo fornisce, scrivilo, ma solo su fatti che puoi
   verificare sul territorio. Niente dettagli storici inventati.

## Come costruire la pagina

Parti da `blog-tropea.html` come riferimento di struttura, ma copia il markup, non
gli errori: controlla che nel file nuovo non finiscano code fence, tag non chiusi o
meta tag vuoti.

La pagina deve avere:

- `<html lang="it">`, charset, viewport
- `<title>` di 50–60 caratteri, nella forma `Titolo | Villa del Conte`
- `meta description` sotto i 160 caratteri, specifica per la pagina
- `<link rel="canonical" href="https://villa-del-conte.com/blog-<slug>.html">`
- `<link rel="icon" type="image/svg+xml" href="/images/ui/logo.svg">`
- Open Graph completo (`og:type` article, title, description, url, image assoluta)
  e `twitter:card`
- due blocchi JSON-LD: `Article` (headline, description, image, datePublished,
  dateModified, author e publisher Villa del Conte, mainEntityOfPage) e
  `BreadcrumbList` (Home, Notebook, pagina corrente)
- **un solo** `<h1>`, nella testata
- `alt` descrittivo e `loading="lazy"` su ogni immagine del corpo
- link di ritorno alla home

## Cosa agganciare dopo

1. **Home**: aggiungi la card nella sezione `blog` di `index.html`, seguendo le
   altre (immagine di sfondo, `h3`, descrizione, link "Leggi di piu'").
2. **Traduzioni**: la card sulla home usa `data-i18n`, quindi aggiungi le chiavi
   `blog_<slug>_title` e `blog_<slug>_desc` **in tutte e sei le lingue** di
   `translations.js` (it, en, es, ru, de, zh). Se ne dimentichi una, sul sito
   compare uno spazio vuoto.
3. **Sitemap**: aggiungi la URL in `sitemap.xml` con `lastmod` di oggi,
   `changefreq` monthly e `priority` 0.8.
4. **llms.txt**: aggiungi la pagina all'elenco del Notebook.
5. **blog_images.json**: aggiorna se usi quel file per le immagini.

## Prima di chiudere

Esegui il controllo completo:

```bash
python3 -I .claude/skills/deploy-check/check.py
```

Poi apri l'anteprima locale (configurazione `villa-del-conte` in
`.claude/launch.json`) e guarda la pagina nuova e la card sulla home, in italiano e
in almeno un'altra lingua.
