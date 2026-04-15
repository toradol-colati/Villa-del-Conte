import json

# 1. Update style.css
with open('style.css', 'a', encoding='utf-8') as f:
    f.write("""
/* Fixed Lang Selector */
.lang-selector-fixed {
  position: absolute;
  top: 20px;
  right: 20px;
  z-index: 1000;
}

/* Modal Styling */
.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  background: rgba(0, 0, 0, 0.7);
  z-index: 9999;
  display: flex;
  justify-content: center;
  align-items: center;
  opacity: 0;
  visibility: hidden;
  transition: opacity 0.3s ease, visibility 0.3s ease;
}
.modal-overlay.active {
  opacity: 1;
  visibility: visible;
}
.modal-content {
  background: #fff;
  width: 90%;
  max-width: 800px;
  max-height: 90vh;
  border-radius: 12px;
  overflow-y: auto;
  position: relative;
  transform: translateY(20px);
  transition: transform 0.3s ease;
  box-shadow: 0 25px 50px rgba(0,0,0,0.3);
}
.modal-overlay.active .modal-content {
  transform: translateY(0);
}
.modal-close {
  position: absolute;
  top: 15px;
  right: 20px;
  background: rgba(255, 255, 255, 0.8);
  border: none;
  font-size: 1.5em;
  font-weight: bold;
  cursor: pointer;
  border-radius: 50%;
  width: 40px;
  height: 40px;
  z-index: 10;
  transition: background 0.3s;
}
.modal-close:hover {
  background: #fff;
  color: #d14949;
}
.modal-header {
  height: 300px;
  background-size: cover;
  background-position: center;
  display: flex;
  align-items: flex-end;
  padding: 30px;
  position: relative;
}
.modal-header::before {
  content: '';
  position: absolute;
  top: 0; left: 0; width: 100%; height: 100%;
  background: linear-gradient(to top, rgba(0,0,0,0.8), transparent);
}
.modal-header h2 {
  position: relative;
  color: #fff;
  font-family: 'Cormorant Garamond', serif;
  font-size: 3em;
  text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
  margin: 0;
}
.modal-body {
  padding: 40px;
}
.modal-body h4 {
  font-family: 'Cormorant Garamond', serif;
  font-size: 1.8em;
  color: #4a9d5f;
  margin-top: 30px;
  margin-bottom: 15px;
}
.modal-body p {
  color: #444;
  font-size: 1.1em;
  line-height: 1.8;
  margin-bottom: 20px;
}
.blog-card {
  cursor: pointer;
}
""")

# 2. Add keys to translations.js
# Just reading and replacing manually is painful. I will rewrite the translations object structure, but since it's already there 
# I will use a simple regex approach or JSON parsing to append to `translations.js`

with open("translations.js", "r", encoding="utf-8") as f:
    js_content = f.read()

import re
# We insert new translations directly into the string before the closing brace of each language object.
additions = {
    "it": '''
        "blog_toraldo_title": "I Toraldo a Tropea",
        "blog_toraldo_excerpt": "Scopri il legame indissolubile tra l'antica famiglia nobiliare, arrivata con l'Imperatore Federico II, e i tesori architettonici e terrieri di Tropea e dintorni...",
        "read_more": "Leggi di più →",
        "blog_toraldo_p1": "La famiglia Toraldo è una delle più antiche e nobili casate del Regno di Napoli. Di origine germanica, la famiglia giunse in Italia al seguito dell'imperatore Federico II di Svevia e si stabilì in Calabria, venendo ascritta al patriziato di Tropea fin dal 1508.",
        "blog_toraldo_h1": "Il Palazzo Toraldo e l'Archivio Storico",
        "blog_toraldo_p2": "Situato nel cuore del centro storico di Tropea, il maestoso Palazzo Toraldo ospita l'inestimabile archivio privato della famiglia, con pergamene risalenti dal XII al XVI secolo. Anche la scuola cittadina porta oggi il nome 'Toraldo'.",
        "blog_toraldo_h2": "Santa Domenica di Ricadi e le Terre di Famiglia",
        "blog_toraldo_p3": "Le vastissime proprietà terriere includevano gran parte di Santa Domenica di Ricadi, testimoniando l'importanza agricola ed economica della famiglia in tutta la Costa degli Dei.",
        "blog_toraldo_h3": "Il Castello Galluppi-Toraldo",
        "blog_toraldo_p4": "A Caria di Drapia sorge l'affascinante Castello Galluppi-Toraldo. Un tempo residenza estiva della famiglia, è un magnifico esempio dell'architettura aristocratica calabrese dell'Ottocento.",
        "about_intro_title": "La Nostra Accoglienza",
        "about_intro_p1": "Benvenuti a Villa del Conte. Da anni ci dedichiamo all'ospitalità, aprendo le porte di una delle zone più affascinanti della Costa degli Dei. Il nostro obiettivo è farvi sentire a casa, garantendovi una vacanza indimenticabile."
''',
    "en": '''
        "blog_toraldo_title": "The Toraldos in Tropea",
        "blog_toraldo_excerpt": "Discover the unbreakable bond between the ancient noble family, who arrived with Emperor Frederick II, and the architectural and land treasures of Tropea and its surroundings...",
        "read_more": "Read more →",
        "blog_toraldo_p1": "The Toraldo family is one of the oldest and most noble houses of the Kingdom of Naples. Of Germanic origin, they arrived in Italy following Emperor Frederick II of Swabia and settled in Calabria, joining the patriciate of Tropea in 1508.",
        "blog_toraldo_h1": "Toraldo Palace and the Historical Archive",
        "blog_toraldo_p2": "Located in the heart of Tropea's historic center, the majestic Toraldo Palace houses the family's invaluable private archive, featuring scrolls dating from the 12th to the 16th century. Even the local school is named 'Toraldo' today.",
        "blog_toraldo_h2": "Santa Domenica di Ricadi and the Family Lands",
        "blog_toraldo_p3": "The vast land properties included much of Santa Domenica di Ricadi, a testament to the family's agricultural and economic importance throughout the Costa degli Dei.",
        "blog_toraldo_h3": "The Galluppi-Toraldo Castle",
        "blog_toraldo_p4": "In Caria di Drapia stands the fascinating Galluppi-Toraldo Castle. Once the family's summer residence, it is a magnificent example of 19th-century aristocratic Calabrian architecture.",
        "about_intro_title": "Our Hospitality",
        "about_intro_p1": "Welcome to Villa del Conte. For years we have been dedicated to hospitality, opening the doors to one of the most fascinating areas of the Costa degli Dei. Our goal is to make you feel at home, ensuring an unforgettable holiday."
''',
    "es": '''
        "blog_toraldo_title": "Los Toraldo en Tropea",
        "blog_toraldo_excerpt": "Descubre el vínculo inquebrantable entre la antigua familia noble, que llegó con el emperador Federico II, y los tesoros arquitectónicos de Tropea...",
        "read_more": "Leer más →",
        "blog_toraldo_p1": "La familia Toraldo es una de las casas más antiguas y nobles del Reino de Nápoles. De origen germánico, llegaron a Italia con el emperador Federico II de Suabia y se establecieron en Calabria.",
        "blog_toraldo_h1": "El Palacio Toraldo y el Archivo Histórico",
        "blog_toraldo_p2": "Ubicado en el corazón del centro histórico de Tropea, el majestuoso Palacio Toraldo alberga el invaluable archivo privado de la familia.",
        "blog_toraldo_h2": "Santa Domenica di Ricadi y las Tierras de la Familia",
        "blog_toraldo_p3": "Las vastas propiedades de tierras incluían gran parte de Santa Domenica di Ricadi, demostrando la importancia económica de la familia a lo largo de la Costa degli Dei.",
        "blog_toraldo_h3": "El Castillo Galluppi-Toraldo",
        "blog_toraldo_p4": "En Caria di Drapia se encuentra el fascinante Castillo Galluppi-Toraldo. Antaño residencia de verano de la familia, es un magnífico ejemplo de la arquitectura aristocrática del siglo XIX.",
        "about_intro_title": "Nuestra Hospitalidad",
        "about_intro_p1": "Bienvenidos a Villa del Conte. Durante años nos hemos dedicado a la hospitalidad, abriendo las puertas de una de las zonas más fascinantes de la costa."
''',
    "ru": '''
        "blog_toraldo_title": "Семья Торальдо в Тропее",
        "blog_toraldo_excerpt": "Узнайте о неразрывной связи между древней знатной семьей, прибывшей с императором Фридрихом II, и архитектурными сокровищами...",
        "read_more": "Читать далее →",
        "blog_toraldo_p1": "Семья Торальдо - один из старейших и знатнейших домов Неаполитанского королевства.",
        "blog_toraldo_h1": "Дворец Торальдо и исторический архив",
        "blog_toraldo_p2": "В самом сердце исторического центра Тропеи находится дворец Торальдо, в котором хранится бесценный частный архив семьи.",
        "blog_toraldo_h2": "Санта-Доменика-ди-Рикади и семейные земли",
        "blog_toraldo_p3": "Огромные земельные владения включали большую часть Санта-Доменика-ди-Рикади.",
        "blog_toraldo_h3": "Замок Галлуппи-Торальдо",
        "blog_toraldo_p4": "В Кария-ди-Драпия возвышается увлекательный замок Галлуппи-Торальдо.",
        "about_intro_title": "Наше гостеприимство",
        "about_intro_p1": "Добро пожаловать на Виллу дель Конте. В течение многих лет мы посвятили себя гостеприимству, открывая двери в одни из самых увлекательных районов побережья."
''',
    "de": '''
        "blog_toraldo_title": "Die Toraldos in Tropea",
        "blog_toraldo_excerpt": "Entdecken Sie die untrennbare Verbindung zwischen der alten Adelsfamilie, die mit Kaiser Friedrich II. ankam, und den architektonischen Schätzen...",
        "read_more": "Weiterlesen →",
        "blog_toraldo_p1": "Die Familie Toraldo ist eines der ältesten und edelsten Häuser des Königreichs Neapel.",
        "blog_toraldo_h1": "Toraldo-Palast und das Historische Archiv",
        "blog_toraldo_p2": "Im Herzen des historischen Zentrums von Tropea beherbergt der majestätische Toraldo-Palast das unschätzbare Privatarchiv der Familie.",
        "blog_toraldo_h2": "Santa Domenica di Ricadi und die Familienländereien",
        "blog_toraldo_p3": "Die ausgedehnten Ländereien umfassten einen großen Teil von Santa Domenica di Ricadi.",
        "blog_toraldo_h3": "Das Schloss Galluppi-Toraldo",
        "blog_toraldo_p4": "In Caria di Drapia steht das faszinierende Schloss Galluppi-Toraldo.",
        "about_intro_title": "Unsere Gastfreundschaft",
        "about_intro_p1": "Willkommen in der Villa del Conte. Seit Jahren widmen wir uns der Gastfreundschaft und öffnen die Türen zu einem der faszinierendsten Gebiete der Costa degli Dei."
''',
    "zh": '''
        "blog_toraldo_title": "特罗佩亚的托拉尔多家族",
        "blog_toraldo_excerpt": "探索跟随腓特烈二世皇帝抵达的古老贵族家庭与特罗佩亚建筑宝藏之间不可分割的联系...",
        "read_more": "阅读更多 →",
        "blog_toraldo_p1": "托拉尔多家族是那不勒斯王国最古老、最崇高的家族之一。",
        "blog_toraldo_h1": "托拉尔多宫与历史档案",
        "blog_toraldo_p2": "雄伟的托拉尔多宫位于特罗佩亚历史中心的心脏地带，收藏着该家族无价的私人档案。",
        "blog_toraldo_h2": "圣多梅尼卡迪里卡迪与家族土地",
        "blog_toraldo_p3": "广阔的土地财产包括圣多梅尼卡迪里卡迪的大部分地区。",
        "blog_toraldo_h3": "加卢皮-托拉尔多城堡",
        "blog_toraldo_p4": "在卡利亚迪德拉皮亚矗立着迷人的加卢皮-托拉尔多城堡。",
        "about_intro_title": "我们的热情好客",
        "about_intro_p1": "欢迎来到康特别墅。多年来，我们一直致力于酒店业，为您打开通往众神海岸最迷人地区之一的大门。"
'''
}

for lang, additions_str in additions.items():
    # Find the end of the language block: it's a "}" before either a "," or the end of the translations object.
    # regex matches exact language key 'it': { ... }
    pattern = rf'({lang}:\s*{{(.*?))(\n\s*}}\s*[,]?\s*(?:en:|es:|ru:|de:|zh:|</script>|\z|}}))'
    # We will just append before the closing brace of the language object by using a simple string operation
    
    parts = js_content.split(f'{lang}: {{')
    if len(parts) > 1:
        # inside parts[1], the first occurrence of '\n    },' or '\n    }' is the end of the block
        subparts = re.split(r'\n\s*}(?:,|$)', parts[1], 1)
        
        # reconstruct
        new_block = subparts[0] + ",\n" + additions_str + "\n    }" + ("," if len(parts[1]) > len(subparts[0]) + 10 else "")
        if "}," in parts[1][:len(subparts[0])+15]: # heuristic for commas
             pass # covered by standard JSON
        js_content = parts[0] + f'{lang}: {{' + subparts[0] + "," + additions_str + "\n    }" + ("" if lang=="zh" else ",") + subparts[1]

with open("translations.js", "w", encoding="utf-8") as f:
    f.write(js_content)
    
print("Updated CSS and Translations")
