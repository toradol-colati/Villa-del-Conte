import json

with open("translations.js", "r", encoding="utf-8") as f:
    content = f.read()

# Replace Italian FAQ
content = content.replace('"Le spiagge di Santa Domenica di Ricadi, così come quelle di Tropea e Capo Vaticano, distano pochissimi minuti dalla struttura."', '"Ci troviamo sulla costa, circondati da tutte le spiagge principali della zona."')
content = content.replace('"Sì, la connessione WiFi è gratuita e copre per intero sia le abitazioni che le zone circostanti."', '"Sì, è gratuito e copre per intero le strutture."')
content = content.replace('"Certamente, il servizio biancheria è disponibile su richiesta per garantirvi il massimo comfort durante il vostro soggiorno."', '"Certamente, è disponibile su richiesta per garantirvi il massimo comfort."')
content = content.replace('"Gli animali non sono ammessi all\'interno delle nostre abitazioni per tutelare gli ospiti con eventuali allergie."', '"Solamente quelli di piccola taglia."')
content = content.replace('"All\'interno è severamente vietato fumare. Tuttavia, disponiamo di ampi spazi all\'aperto dotati di comfort."', '"No, è severamente vietato e punito con una multa."')

# Replace EN FAQ (just for thoroughness, assuming they are dynamically injected based on English defaults)
# Wait, let's just make sure we update translations.js. The user might switch languages and get the old long answers.
import re
content = re.sub(r'("en":\s*\{.*?)"faq_title"', r'\1"faq_a1": "We are on the coast, surrounded by all the main beaches of the area.", "faq_a2": "Yes, it is free and fully covers the facilities.", "faq_a3": "Certainly, it is available upon request to ensure maximum comfort.", "faq_a4": "Only small ones.", "faq_a5": "No, it is strictly forbidden and punishable by a fine.", "faq_title"', content, flags=re.DOTALL)
content = re.sub(r'("es":\s*\{.*?)"faq_title"', r'\1"faq_a1": "Estamos en la costa, rodeados de todas las playas principales de la zona.", "faq_a2": "Sí, es gratuito y cubre por completo las instalaciones.", "faq_a3": "Ciertamente, está disponible bajo petición para garantizar el máximo confort.", "faq_a4": "Solo los de tamaño pequeño.", "faq_a5": "No, está estrictamente prohibido y penalizado con una multa.", "faq_title"', content, flags=re.DOTALL)
content = re.sub(r'("ru":\s*\{.*?)"faq_title"', r'\1"faq_a1": "Мы находимся на побережье, в окружении всех главных пляжей района.", "faq_a2": "Да, он бесплатный и полностью покрывает объекты.", "faq_a3": "Конечно, предоставляется по запросу для обеспечения максимального комфорта.", "faq_a4": "Только маленькие.", "faq_a5": "Нет, это строго запрещено и наказывается штрафом.", "faq_title"', content, flags=re.DOTALL)
content = re.sub(r'("de":\s*\{.*?)"faq_title"', r'\1"faq_a1": "Wir befinden uns an der Küste, umgeben von allen Hauptstränden der Gegend.", "faq_a2": "Ja, es ist kostenlos und deckt die Einrichtungen vollständig ab.", "faq_a3": "Sicherlich, es ist auf Anfrage erhältlich, um maximalen Komfort zu gewährleisten.", "faq_a4": "Nur kleine.", "faq_a5": "Nein, es ist strengstens verboten und wird mit einem Bußgeld geahndet.", "faq_title"', content, flags=re.DOTALL)
content = re.sub(r'("zh":\s*\{.*?)"faq_title"', r'\1"faq_a1": "我们在海岸上，周围是该地区所有主要海滩。", "faq_a2": "是的，它是免费的，完全覆盖设施。", "faq_a3": "当然，可应要求提供，以确保最大的舒适度。", "faq_a4": "只有小型的。", "faq_a5": "不，严禁吸烟，违者将被罚款。", "faq_title"', content, flags=re.DOTALL)


with open("translations.js", "w", encoding="utf-8") as f:
    f.write(content)

print("Updated FAQ keys")
