import re

with open("translations.js", "r") as f:
    content = f.read()

additions = {
    "it": """
        "blog_territorio_title": "Storia del Territorio",
        "blog_territorio_excerpt": "Il territorio che circonda Villa del Conte a Santa Domenica di Ricadi, sulla suggestiva Costa degli Dei in Calabria, è un mosaico vivo di epo...",
        "blog_romane_title": "Origini Romane",
        "blog_romane_excerpt": "Le origini romane del territorio intorno a Santa Domenica di Ricadi e Tropea, sulla Costa degli Dei in Calabria, riportano a un’epoca di co...",
        "blog_costa_title": "La Costa degli Dei",
        "blog_costa_excerpt": "La Costa degli Dei è uno dei tratti di litorale più spettacolari d’Italia, un paradiso calabrese che si snoda per circa 50 chilometri lu...",
        "blog_tropea_title": "Tropea: Il Borgo dei Borghi",
        "blog_tropea_excerpt": "Tropea, la “perla del Tirreno” e più volte eletta Borgo dei Borghi d’Italia, domina la Costa degli Dei in Calabria con un fascino irresist...",
        "blog_santadomenica_title": "Santa Domenica di Ricadi",
        "blog_santadomenica_excerpt": "Santa Domenica di Ricadi, frazione del comune di Ricadi sulla Costa degli Dei in Calabria – e non da confondere con l’omonima località...",
        "blog_cucina_title": "Tradizioni Culinarie",
        "blog_cucina_excerpt": "Le tradizioni culinarie della Costa degli Dei rappresentano l’anima autentica della Calabria, un’esplosione di sapori intensi e ingredienti..."
""",
    "en": """
        "blog_territorio_title": "History of the Territory",
        "blog_territorio_excerpt": "The territory surrounding Villa del Conte in Santa Domenica di Ricadi, on the charming Costa degli Dei in Calabria, is a living mosaic of epo...",
        "blog_romane_title": "Roman Origins",
        "blog_romane_excerpt": "The Roman origins of the territory around Santa Domenica di Ricadi and Tropea, on the Costa degli Dei in Calabria, date back to an era of co...",
        "blog_costa_title": "The Coast of the Gods",
        "blog_costa_excerpt": "The Costa degli Dei is one of the most spectacular stretches of coastline in Italy, a Calabrian paradise that winds for about 50 kilometers alo...",
        "blog_tropea_title": "Tropea: The Village of Villages",
        "blog_tropea_excerpt": "Tropea, the 'Pearl of the Tyrrhenian Sea' and repeatedly elected Village of Villages of Italy, dominates the Costa degli Dei in Calabria with an irresist...",
        "blog_santadomenica_title": "Santa Domenica di Ricadi",
        "blog_santadomenica_excerpt": "Santa Domenica di Ricadi, a hamlet of the municipality of Ricadi on the Costa degli Dei in Calabria - not to be confused with the town of the same name...",
        "blog_cucina_title": "Culinary Traditions",
        "blog_cucina_excerpt": "The culinary traditions of the Costa degli Dei represent the authentic soul of Calabria, an explosion of intense flavors and ingredients..."
""",
    "es": """
        "blog_territorio_title": "Historia del Territorio",
        "blog_territorio_excerpt": "El territorio que rodea Villa del Conte en Santa Domenica di Ricadi, en la sugerente Costa degli Dei en Calabria, es un mosaico vivo de épo...",
        "blog_romane_title": "Orígenes Romanos",
        "blog_romane_excerpt": "Los orígenes romanos del territorio alrededor de Santa Domenica di Ricadi y Tropea, en la Costa degli Dei en Calabria, se remontan a una época de co...",
        "blog_costa_title": "La Costa de los Dioses",
        "blog_costa_excerpt": "La Costa degli Dei es uno de los tramos de costa más espectaculares de Italia, un paraíso calabrés que serpentea a lo largo de unos 50 kilómetros a l...",
        "blog_tropea_title": "Tropea: El Pueblo de los Pueblos",
        "blog_tropea_excerpt": "Tropea, la 'Perla del Tirreno' y repetidamente elegida Pueblo de los Pueblos de Italia, domina la Costa degli Dei en Calabria con un encanto irresist...",
        "blog_santadomenica_title": "Santa Domenica di Ricadi",
        "blog_santadomenica_excerpt": "Santa Domenica di Ricadi, una aldea del municipio de Ricadi en la Costa degli Dei en Calabria - no confundir con la ciudad del mismo nombre...",
        "blog_cucina_title": "Tradiciones Culinarias",
        "blog_cucina_excerpt": "Las tradiciones culinarias de la Costa degli Dei representan el alma auténtica de Calabria, una explosión de sabores intensos e ingredientes..."
""",
    "ru": """
        "blog_territorio_title": "История Территории",
        "blog_territorio_excerpt": "Территория, окружающая Виллу дель Конте в Санта-Доменика-ди-Рикади, на очаровательном Побережье Богов в Калабрии, представляет собой живую мозаику эпо...",
        "blog_romane_title": "Римское Происхождение",
        "blog_romane_excerpt": "Римское происхождение территории вокруг Санта-Доменика-ди-Рикади и Тропеи, на Побережье Богов в Калабрии, восходит к эпохе ко...",
        "blog_costa_title": "Побережье Богов",
        "blog_costa_excerpt": "Побережье Богов - один из самых захватывающих участков побережья Италии, калабрийский рай, который извивается примерно на 50 километров вд...",
        "blog_tropea_title": "Тропея: Деревня Деревень",
        "blog_tropea_excerpt": "Тропея, 'Жемчужина Тирренского моря' и неоднократно избиравшаяся Деревней Деревень Италии, доминирует на Побережье Богов в Калабрии с неотразимым о...",
        "blog_santadomenica_title": "Санта-Доменика-ди-Рикади",
        "blog_santadomenica_excerpt": "Санта-Доменика-ди-Рикади, деревушка в муниципалитете Рикади на Побережье Богов в Калабрии - не путать с одноименным городом...",
        "blog_cucina_title": "Кулинарные Традиции",
        "blog_cucina_excerpt": "Кулинарные традиции Побережья Богов представляют собой подлинную душу Калабрии, взрыв интенсивных вкусов и ингредиентов..."
""",
    "de": """
        "blog_territorio_title": "Geschichte des Territoriums",
        "blog_territorio_excerpt": "Das Gebiet um die Villa del Conte in Santa Domenica di Ricadi an der bezaubernden Costa degli Dei in Kalabrien ist ein lebendiges Mosaik von Epo...",
        "blog_romane_title": "Römische Ursprünge",
        "blog_romane_excerpt": "Die römischen Ursprünge des Gebiets um Santa Domenica di Ricadi und Tropea an der Costa degli Dei in Kalabrien gehen auf eine Ära der Ko...",
        "blog_costa_title": "Die Küste der Götter",
        "blog_costa_excerpt": "Die Costa degli Dei ist einer der spektakulärsten Küstenabschnitte Italiens, ein kalabrisches Paradies, das sich über 50 Kilometer entla...",
        "blog_tropea_title": "Tropea: Dorf der Dörfer",
        "blog_tropea_excerpt": "Tropea, die 'Perle des Tyrrhenischen Meeres' und wiederholt zum Dorf der Dörfer Italiens gewählt, dominiert die Costa degli Dei in Kalabrien mit einem unwidersteh...",
        "blog_santadomenica_title": "Santa Domenica di Ricadi",
        "blog_santadomenica_excerpt": "Santa Domenica di Ricadi, ein Weiler der Gemeinde Ricadi an der Costa degli Dei in Kalabrien - nicht zu verwechseln mit der gleichnamigen Stadt...",
        "blog_cucina_title": "Kulinarische Traditionen",
        "blog_cucina_excerpt": "Die kulinarischen Traditionen der Costa degli Dei repräsentieren die authentische Seele Kalabriens, eine Explosion von intensiven Aromen und Zutaten..."
""",
    "zh": """
        "blog_territorio_title": "领土历史",
        "blog_territorio_excerpt": "卡拉布里亚众神海岸迷人的圣多梅尼卡迪里卡迪 (Santa Domenica di Ricadi) 的 Villa del Conte 周围的领土，是时代...",
        "blog_romane_title": "罗马起源",
        "blog_romane_excerpt": "位于卡拉布里亚众神海岸的圣多梅尼卡迪里卡迪和特罗佩亚周围领土的罗马起源可以追溯到...",
        "blog_costa_title": "众神海岸",
        "blog_costa_excerpt": "众神海岸是意大利最壮观的海岸线之一，这是一个绵延约 50 公里的卡拉布里亚天堂...",
        "blog_tropea_title": "特罗佩亚：村中之村",
        "blog_tropea_excerpt": "特罗佩亚被誉为“第勒尼安海的珍珠”，曾多次被选为意大利的村中之村，它以不可抗拒的魅力统治着卡拉布里亚的众神海岸...",
        "blog_santadomenica_title": "圣多梅尼卡迪里卡迪",
        "blog_santadomenica_excerpt": "圣多梅尼卡迪里卡迪（Santa Domenica di Ricadi）是卡拉布里亚众神海岸里卡迪市的一个小村庄——不要与同名城镇混淆...",
        "blog_cucina_title": "烹饪传统",
        "blog_cucina_excerpt": "众神海岸的烹饪传统代表了卡拉布里亚真实的灵魂，这是强烈风味和食材的爆发..."
"""
}

# The files look like this:
# "blog_toraldo_p4": "A Caria di Drapia sorge l'affascinante Castello Galluppi-Toraldo..."
#     },

def replace_for_lang(lang_match):
    text = lang_match.group(0)
    for lang, added_text in additions.items():
        # A simple heuristic: check the language block content
        if lang == "it" and "Ottocento" in text:
            return text.replace('\n    }', ',\n' + added_text + '\n    }')
        elif lang == "en" and "19th-century" in text:
            return text.replace('\n    }', ',\n' + added_text + '\n    }')
        elif lang == "es" and "ejemplo arquitectónico" in text:
            return text.replace('\n    }', ',\n' + added_text + '\n    }')
        elif lang == "ru" and "Галлуппи-Торальдо" in text:
            return text.replace('\n    }', ',\n' + added_text + '\n    }')
        elif lang == "de" and "faszinierende Schloss" in text:
            return text.replace('\n    }', ',\n' + added_text + '\n    }')
        elif lang == "zh" and "托拉尔多城堡" in text:
            return text.replace('\n    }', ',\n' + added_text + '\n    }')
            
    return text

new_content = re.sub(r'("blog_toraldo_p4".*?\n\s*\})', replace_for_lang, content, flags=re.DOTALL)

if new_content != content:
    with open("translations.js", "w") as f:
        f.write(new_content)
    print("translations.js successfully updated.")
else:
    print("Could not update translations.js.")

