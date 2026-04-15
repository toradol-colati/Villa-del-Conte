import re

# 1. Update translations.js
trans_path = '/Users/umbertotoraldo/petra-protocol/Villa-del-Conte/translations.js'
with open(trans_path, 'r', encoding='utf-8') as f:
    text = f.read()

# Italian
text = text.replace('"Benvenuti a Villa del Conte. Da anni ci dedichiamo', '"Ci dedichiamo')
# English
text = text.replace('"Welcome to Villa del Conte. For years we have been dedicated', '"We are dedicated')
# Spanish
text = text.replace('"Bienvenidos a Villa del Conte. Durante años nos hemos dedicado', '"Nos dedicamos')
# Russian
text = text.replace('"Добро пожаловать на Виллу дель Конте. В течение многих лет мы посвятили', '"Мы посвятили')
# German
text = text.replace('"Willkommen in der Villa del Conte. Seit Jahren widmen wir uns', '"Wir widmen uns')
# Chinese
text = text.replace('"欢迎来到康特别墅。多年来，我们一直致力', '"我们致力')

with open(trans_path, 'w', encoding='utf-8') as f:
    f.write(text)

# 2. Update index.html
index_path = '/Users/umbertotoraldo/petra-protocol/Villa-del-Conte/index.html'
with open(index_path, 'r', encoding='utf-8') as f:
    idx = f.read()

# Delete "Dicono di noi" h3 element
# <h3 class="property-title" style="text-align: center; margin-bottom: 40px;"
#    data-i18n="reviews_title">Dicono di noi</h3>
idx = re.sub(r'<h3[^>]*data-i18n="reviews_title"[^>]*>.*?</h3>', '', idx, flags=re.DOTALL)

# Also remove the border and padding-top from reviews-section that was meant for "Dicono di noi"
# <div class="reviews-section fade-in-up"
#     style="margin-top: 60px; padding-top: 40px; border-top: 1px solid #eaeaea;">
old_review_style = 'style="margin-top: 60px; padding-top: 40px; border-top: 1px solid #eaeaea;"'
new_review_style = 'style="margin-top: 30px;"'
idx = idx.replace(old_review_style, new_review_style)

# Add margin to map-section
idx = idx.replace('<div class="map-section fade-in-up">', '<div class="map-section fade-in-up" style="margin-top: 80px;">')

# Cache-busting
idx = idx.replace('script.js?v=6', 'script.js?v=7')
idx = idx.replace('style.css?v=6', 'style.css?v=7')

with open(index_path, 'w', encoding='utf-8') as f:
    f.write(idx)

print("UI fixes applied successfully!")
