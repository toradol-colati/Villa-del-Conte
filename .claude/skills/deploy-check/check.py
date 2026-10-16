# -*- coding: utf-8 -*-
"""Controlli prima della pubblicazione di villa-del-conte.com.

Il sito e' statico e senza build: un push su main pubblica. Questo script
raccoglie tutti i controlli che altrimenti nessuno farebbe.
"""
from __future__ import print_function

import glob
import io
import json
import os
import re
import subprocess
import sys
import xml.etree.ElementTree as ET

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
ROOT = os.path.dirname(ROOT) if os.path.basename(ROOT) == '.claude' else ROOT
os.chdir(ROOT)
sys.path.insert(0, os.path.join(ROOT, '.claude', 'hooks'))

problems = []
notes = []


def fail(msg):
    problems.append(msg)


def section(title):
    print('\n== %s' % title)


# ---------------------------------------------------------------- 1. JavaScript
section('Sintassi JavaScript')
for js in ('script.js', 'translations.js', 'modify_translations.js'):
    if not os.path.exists(js):
        continue
    p = subprocess.Popen(['node', '--check', js], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    out = p.communicate()[0].decode('utf-8', 'replace')
    if p.returncode:
        fail('%s: errore di sintassi\n%s' % (js, out.strip()))
        print('  FAIL %s' % js)
    else:
        print('  ok   %s' % js)

# ------------------------------------------------------------- 2. Traduzioni
section('Parita delle traduzioni')
src = io.open('translations.js', encoding='utf-8').read()
parts = re.split(r'\n\s{4}(\w+):\s*\{', src)
langs = {}
for i in range(1, len(parts), 2):
    langs[parts[i]] = set(re.findall(r'"([a-zA-Z0-9_]+)"\s*:', parts[i + 1]))
ref = 'it' if 'it' in langs else sorted(langs)[0]
for lang in sorted(langs):
    missing = langs[ref] - langs[lang]
    extra = langs[lang] - langs[ref]
    if missing or extra:
        fail('translations.js, %s: %d mancanti %s, %d in piu %s'
             % (lang, len(missing), sorted(missing), len(extra), sorted(extra)))
        print('  FAIL %s' % lang)
    else:
        print('  ok   %s (%d chiavi)' % (lang, len(langs[lang])))

# ------------------------------------------------------------------ 3. HTML
section('Struttura delle pagine HTML')
try:
    import check_html
except ImportError:
    check_html = None

html_files = sorted(glob.glob('*.html'))
for f in html_files:
    p = subprocess.Popen([sys.executable, '-I', '.claude/hooks/check_html.py', f],
                         stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    out = p.communicate()[0].decode('utf-8', 'replace')
    if p.returncode:
        fail(out.strip())
        print('  FAIL %s' % f)
    else:
        print('  ok   %s' % f)

# ------------------------------------------------------- 4. Risorse referenziate
section('Risorse referenziate')
missing_assets = []
for f in html_files:
    s = io.open(f, encoding='utf-8').read()
    refs = re.findall(r'(?:src|href)="(?!https?:|mailto:|tel:|#|data:)([^"]+)"', s)
    refs += [u.strip() for part in re.findall(r'srcset="([^"]+)"', s)
             for u in re.findall(r'([^\s,]+)\s+\d+w', part)]
    refs += re.findall(r"url\('([^']+)'\)", s)
    for ref in refs:
        path = ref.split('?')[0].split('#')[0].lstrip('/')
        if not path:
            continue
        if not os.path.exists(path):
            missing_assets.append('%s -> %s' % (f, ref))
if missing_assets:
    for m in missing_assets:
        fail('risorsa inesistente: %s' % m)
    print('  FAIL %d risorse mancanti' % len(missing_assets))
else:
    print('  ok   tutte le risorse referenziate esistono')

# --------------------------------------------------------------- 5. Sitemap
section('Sitemap')
root = ET.parse('sitemap.xml').getroot()
ns = '{http://www.sitemaps.org/schemas/sitemap/0.9}'
locs = [e.text.strip() for e in root.iter(ns + 'loc')]
in_sitemap = set()
for loc in locs:
    tail = loc.replace('https://villa-del-conte.com/', '')
    in_sitemap.add(tail if tail else 'index.html')
indexable = set()
for f in html_files:
    s = io.open(f, encoding='utf-8').read()
    if 'noindex' in s:
        continue
    indexable.add(f)
only_disk = indexable - in_sitemap
only_map = in_sitemap - indexable
for f in sorted(only_disk):
    fail('sitemap.xml: manca %s' % f)
for f in sorted(only_map):
    fail('sitemap.xml: elencata %s ma il file non esiste o e noindex' % f)
if not only_disk and not only_map:
    print('  ok   %d URL allineate ai file' % len(locs))

# ------------------------------------------------------------------ 6. JSON
section('File JSON e configurazione')
for j in ('vercel.json', 'blog_images.json', 'gallery_data.json'):
    if not os.path.exists(j):
        notes.append('%s non presente' % j)
        continue
    try:
        json.load(io.open(j, encoding='utf-8'))
        print('  ok   %s' % j)
    except ValueError as e:
        fail('%s non valido: %s' % (j, e))
        print('  FAIL %s' % j)

# ------------------------------------------------------- 7. File di contorno
section('File di contorno')
for f in ('robots.txt', 'llms.txt', '404.html', 'privacy.html', 'sitemap.xml'):
    if os.path.exists(f):
        print('  ok   %s' % f)
    else:
        fail('manca %s' % f)

# ----------------------------------------------------------------- Riepilogo
print('\n' + '=' * 60)
if problems:
    print('%d PROBLEMI DA RISOLVERE PRIMA DI PUBBLICARE:\n' % len(problems))
    for p in problems:
        print('  - %s' % p)
if notes:
    print('\nNote:')
    for n in notes:
        print('  - %s' % n)
if not problems:
    print('Tutti i controlli superati: si puo pubblicare.')
print('=' * 60)
sys.exit(1 if problems else 0)
