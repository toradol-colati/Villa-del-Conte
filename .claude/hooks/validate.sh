#!/bin/bash
# Validazione post-edit per un sito statico senza build step.
# Qui non c'e' ne' bundler ne' type checker: se un file e' rotto, lo e' in produzione.
# Riceve il payload dell'hook su stdin.

set -uo pipefail

payload=$(cat)
file=$(printf '%s' "$payload" | python3 -I -c 'import sys,json; print(json.load(sys.stdin).get("tool_input",{}).get("file_path",""))' 2>/dev/null)

[ -z "$file" ] && exit 0
[ -f "$file" ] || exit 0

root="$(cd "$(dirname "$0")/../.." && pwd)"
errors=""

case "$file" in
  *.js)
    if ! out=$(node --check "$file" 2>&1); then
      errors="Errore di sintassi JavaScript:\n$out"
    fi
    # translations.js: tutte le lingue devono avere le stesse chiavi
    if [ "$(basename "$file")" = "translations.js" ]; then
      if ! out=$(python3 -I "$root/.claude/hooks/check_translations.py" "$file" 2>&1); then
        errors="$errors\n$out"
      fi
    fi
    ;;
  *.json)
    if ! out=$(python3 -I -c 'import json,sys; json.load(open(sys.argv[1]))' "$file" 2>&1); then
      errors="JSON non valido:\n$out"
    fi
    ;;
  *.html)
    if ! out=$(python3 -I "$root/.claude/hooks/check_html.py" "$file" 2>&1); then
      errors="$out"
    fi
    ;;
  *.xml)
    if ! out=$(python3 -I -c 'import xml.etree.ElementTree as ET,sys; ET.parse(sys.argv[1])' "$file" 2>&1); then
      errors="XML non valido:\n$out"
    fi
    ;;
esac

if [ -n "$errors" ]; then
  printf 'Validazione fallita su %s\n' "$file" >&2
  printf '%b\n' "$errors" >&2
  exit 2   # exit 2 = blocca e mostra l'errore al modello
fi

exit 0
