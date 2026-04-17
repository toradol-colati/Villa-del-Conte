import re
import os

# 1. Update translations.js
trans_path = '/Users/umbertotoraldo/petra-protocol/Villa-del-Conte/translations.js'
with open(trans_path, 'r', encoding='utf-8') as f:
    text = f.read()

# form_title
text = text.replace('"form_title": "Richiesta di Prenotazione"', '"form_title": "Richiesta di informazioni"')
# form_subtitle
text = text.replace('"form_subtitle": "Compila il modulo, ti risponderemo tempestivamente."', '"form_subtitle": "Ti risponderemo tempestivamente."')

# Also for contact_banner if they changed it? They highlighted "contattaci..."
# The user's screenshot had: "— contattaci per prenotare ed ottenere uno SCONTO! —"
# Wait, they didn't modify it in the diff. But "Richiesta di informazioni" is there.

with open(trans_path, 'w', encoding='utf-8') as f:
    f.write(text)

# 2. Update script.js for vibrant colors
script_path = '/Users/umbertotoraldo/petra-protocol/Villa-del-Conte/script.js'
with open(script_path, 'r', encoding='utf-8') as f:
    stext = f.read()

# In script.js, I have:
# card.style.backgroundColor = `rgba(${r}, ${g}, ${b}, 0.15)`;
# card.style.borderColor = `rgba(${r}, ${g}, ${b}, 0.4)`;
# const darkened = `rgb(${Math.max(0, r - 80)}, ${Math.max(0, g - 80)}, ${Math.max(0, b - 80)})`;

new_bg = "card.style.backgroundColor = `rgba(${r}, ${g}, ${b}, 0.3)`;"
new_border = "card.style.borderColor = `rgba(${r}, ${g}, ${b}, 0.8)`;\n                    card.style.boxShadow = `0 10px 30px rgba(${r}, ${g}, ${b}, 0.2)`;"

stext = stext.replace("card.style.backgroundColor = `rgba(${r}, ${g}, ${b}, 0.15)`;", new_bg)
stext = stext.replace("card.style.borderColor = `rgba(${r}, ${g}, ${b}, 0.4)`;", new_border)

with open(script_path, 'w', encoding='utf-8') as f:
    f.write(stext)

# Cache-busting
index_path = '/Users/umbertotoraldo/petra-protocol/Villa-del-Conte/index.html'
with open(index_path, 'r', encoding='utf-8') as f:
    idx = f.read()
idx = idx.replace('script.js?v=9', 'script.js?v=10')
idx = idx.replace('translations.js?v=2.0', 'translations.js?v=3.0')
idx = idx.replace('style.css?v=9', 'style.css?v=10')
with open(index_path, 'w', encoding='utf-8') as f:
    f.write(idx)

print("Translations and vibrant colors applied!")
