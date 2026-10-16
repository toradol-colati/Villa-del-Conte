# -*- coding: utf-8 -*-
"""Verifica che tutte le lingue di translations.js abbiano le stesse chiavi.

In questo progetto l'i18n e' scritta a mano: una chiave aggiunta in italiano e
dimenticata nelle altre lingue non da' nessun errore, produce una stringa vuota
sul sito pubblicato. Questo controllo lo intercetta prima del commit.
"""
import io
import re
import sys

path = sys.argv[1] if len(sys.argv) > 1 else 'translations.js'
src = io.open(path, encoding='utf-8').read()

parts = re.split(r'\n\s{4}(\w+):\s*\{', src)
langs = {}
for i in range(1, len(parts), 2):
    langs[parts[i]] = set(re.findall(r'"([a-zA-Z0-9_]+)"\s*:', parts[i + 1]))

if not langs:
    sys.exit(0)

reference = 'it' if 'it' in langs else sorted(langs)[0]
expected = langs[reference]
problems = []

for lang in sorted(langs):
    if lang == reference:
        continue
    missing = expected - langs[lang]
    extra = langs[lang] - expected
    if missing:
        problems.append('  %s: mancano %d chiavi -> %s'
                        % (lang, len(missing), ', '.join(sorted(missing))))
    if extra:
        problems.append('  %s: %d chiavi in piu rispetto a %s -> %s'
                        % (lang, len(extra), reference, ', '.join(sorted(extra))))

if problems:
    print('Traduzioni non allineate (riferimento: %s, %d chiavi):' % (reference, len(expected)))
    print('\n'.join(problems))
    sys.exit(1)

print('Traduzioni allineate: %d lingue x %d chiavi.' % (len(langs), len(expected)))
