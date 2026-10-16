# -*- coding: utf-8 -*-
"""Controlli rapidi sulle pagine HTML di un sito statico senza build step.

Intercetta la classe di errori che in questo progetto e' gia' finita in
produzione: code fence markdown rimasti nell'HTML, tag non bilanciati,
attributi essenziali mancanti.
"""
import io
import re
import sys
from html.parser import HTMLParser

VOID = {'area', 'base', 'br', 'col', 'embed', 'hr', 'img', 'input', 'link',
        'meta', 'param', 'source', 'track', 'wbr'}


class Checker(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.stack = []
        self.errors = []
        self.imgs_without_alt = []
        self.h1 = 0

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == 'img' and 'alt' not in a:
            self.imgs_without_alt.append(a.get('src', '?'))
        if tag == 'h1':
            self.h1 += 1
        if tag not in VOID:
            self.stack.append((tag, self.getpos()[0]))

    def handle_endtag(self, tag):
        if tag in VOID:
            return
        if not self.stack:
            self.errors.append('riga %d: </%s> senza tag di apertura' % (self.getpos()[0], tag))
            return
        if self.stack[-1][0] == tag:
            self.stack.pop()
        else:
            for i in range(len(self.stack) - 1, -1, -1):
                if self.stack[i][0] == tag:
                    unclosed = [t for t, _ in self.stack[i + 1:]]
                    self.errors.append('riga %d: </%s> chiude mentre sono aperti %s'
                                       % (self.getpos()[0], tag, ', '.join(unclosed)))
                    del self.stack[i:]
                    break


def main():
    path = sys.argv[1]
    src = io.open(path, encoding='utf-8').read()
    problems = []

    fences = [i + 1 for i, line in enumerate(src.splitlines()) if line.strip() == '```']
    if fences:
        problems.append('code fence markdown nell\'HTML alle righe: %s'
                        % ', '.join(str(n) for n in fences))

    c = Checker()
    c.feed(src)
    problems.extend(c.errors)
    if c.stack:
        problems.append('tag mai chiusi: %s'
                        % ', '.join('<%s> (riga %d)' % (t, n) for t, n in c.stack))
    if c.imgs_without_alt:
        problems.append('immagini senza alt: %s' % ', '.join(c.imgs_without_alt))

    # controlli SEO solo sulle pagine pubbliche indicizzabili
    name = path.rsplit('/', 1)[-1]
    if name not in ('404.html',):
        if c.h1 == 0:
            problems.append('nessun <h1> nella pagina')
        elif c.h1 > 1:
            problems.append('%d tag <h1>: deve essercene uno solo' % c.h1)
        for tag, label in (('<title>', 'title'),
                           ('name="description"', 'meta description'),
                           ('rel="canonical"', 'canonical')):
            if tag not in src:
                problems.append('manca %s' % label)

    for m in re.finditer(r'<script type="application/ld\+json">(.*?)</script>', src, re.S):
        import json
        try:
            json.loads(m.group(1))
        except ValueError as e:
            problems.append('JSON-LD non valido: %s' % e)

    if problems:
        print('Problemi in %s:' % path)
        for p in problems:
            print('  - %s' % p)
        sys.exit(1)


if __name__ == '__main__':
    main()
