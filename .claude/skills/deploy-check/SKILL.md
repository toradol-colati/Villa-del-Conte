---
name: deploy-check
description: Controlla il sito prima di pubblicarlo su villa-del-conte.com. Usalo prima di ogni push su main, perche' su questo progetto un push e' una pubblicazione immediata.
disable-model-invocation: true
---

# Controllo prima della pubblicazione

Su questo progetto **non esiste CI e non esiste staging**: Vercel pubblica ogni
push su `main` direttamente su villa-del-conte.com. Questo e' l'unico cancello
prima della produzione, quindi vale la pena eseguirlo per intero.

Esegui lo script e poi interpreta i risultati:

```bash
python3 -I .claude/skills/deploy-check/check.py
```

Lo script verifica, in ordine:

1. sintassi di `script.js` e `translations.js` con `node --check`
2. parita' delle chiavi tra le sei lingue di `translations.js`
3. struttura di ogni pagina HTML: tag bilanciati, un solo `h1`, title, meta
   description, canonical, alt sulle immagini, JSON-LD valido, nessun code fence
   markdown rimasto
4. esistenza su disco di ogni immagine, foglio di stile e script referenziato
   (in passato due immagini di apertura davano 404 in produzione)
5. allineamento tra `sitemap.xml` e i file HTML indicizzabili presenti
6. validita' di `vercel.json`, `blog_images.json` e `gallery_data.json`
7. presenza dei file di contorno: `robots.txt`, `llms.txt`, `404.html`,
   `privacy.html`

## Dopo lo script

- Se qualcosa fallisce, **correggi prima di pubblicare**: non c'e' modo di
  accorgersene dopo se non visitando il sito.
- Se tutto passa, riepiloga in due righe cosa cambia questo deploy e chiedi
  conferma prima di fare `git push`.
- Per un controllo visivo: avvia l'anteprima con la configurazione
  `villa-del-conte` in `.claude/launch.json` e guarda la home, una pagina blog e
  il form.
- Dopo la pubblicazione, verifica che il sito risponda:
  `curl -s -o /dev/null -w "%{http_code}" https://villa-del-conte.com/`

Non eseguire `git push` da solo: proponilo e aspetta il via libera.
