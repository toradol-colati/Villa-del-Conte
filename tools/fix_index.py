import sys

with open("index.html", "r") as f:
    content = f.read()

replacements = [
    ('<h3>Storia del Territorio</h3>', '<h3 data-i18n="blog_territorio_title">Storia del Territorio</h3>'),
    ('<p>Il territorio che circonda Villa del Conte a Santa Domenica di Ricadi, sulla suggestiva\n                                Costa degli Dei in Calabria, è un mosaico vivo di epo...</p>', '<p data-i18n="blog_territorio_excerpt">Il territorio che circonda Villa del Conte a Santa Domenica di Ricadi, sulla suggestiva\n                                Costa degli Dei in Calabria, è un mosaico vivo di epo...</p>'),
    ('<h3>Origini Romane</h3>', '<h3 data-i18n="blog_romane_title">Origini Romane</h3>'),
    ('<p>Le origini romane del territorio intorno a Santa Domenica di Ricadi e Tropea, sulla Costa\n                                degli Dei in Calabria, riportano a un’epoca di co...</p>', '<p data-i18n="blog_romane_excerpt">Le origini romane del territorio intorno a Santa Domenica di Ricadi e Tropea, sulla Costa\n                                degli Dei in Calabria, riportano a un’epoca di co...</p>'),
    ('<h3>La Costa degli Dei</h3>', '<h3 data-i18n="blog_costa_title">La Costa degli Dei</h3>'),
    ('<p>La Costa degli Dei è uno dei tratti di litorale più spettacolari d’Italia, un paradiso\n                                calabrese che si snoda per circa 50 chilometri lu...</p>', '<p data-i18n="blog_costa_excerpt">La Costa degli Dei è uno dei tratti di litorale più spettacolari d’Italia, un paradiso\n                                calabrese che si snoda per circa 50 chilometri lu...</p>'),
    ('<h3>Tropea: Il Borgo dei Borghi</h3>', '<h3 data-i18n="blog_tropea_title">Tropea: Il Borgo dei Borghi</h3>'),
    ('<p>Tropea, la “perla del Tirreno” e più volte eletta Borgo dei Borghi d’Italia, domina la\n                                Costa degli Dei in Calabria con un fascino irresist...</p>', '<p data-i18n="blog_tropea_excerpt">Tropea, la “perla del Tirreno” e più volte eletta Borgo dei Borghi d’Italia, domina la\n                                Costa degli Dei in Calabria con un fascino irresist...</p>'),
    ('<h3>Santa Domenica di Ricadi</h3>', '<h3 data-i18n="blog_santadomenica_title">Santa Domenica di Ricadi</h3>'),
    ('<p>Santa Domenica di Ricadi, frazione del comune di Ricadi sulla Costa degli Dei in Calabria\n                                – e non da confondere con l’omonima località...</p>', '<p data-i18n="blog_santadomenica_excerpt">Santa Domenica di Ricadi, frazione del comune di Ricadi sulla Costa degli Dei in Calabria\n                                – e non da confondere con l’omonima località...</p>'),
    ('<h3>Tradizioni Culinarie</h3>', '<h3 data-i18n="blog_cucina_title">Tradizioni Culinarie</h3>'),
    ('<p>Le tradizioni culinarie della Costa degli Dei rappresentano l’anima autentica della\n                                Calabria, un’esplosione di sapori intensi e ingredienti...</p>', '<p data-i18n="blog_cucina_excerpt">Le tradizioni culinarie della Costa degli Dei rappresentano l’anima autentica della\n                                Calabria, un’esplosione di sapori intensi e ingredienti...</p>')
]

for a, b in replacements:
    if a not in content:
        print(f"Error: could not find {a!r}")
    content = content.replace(a, b)

with open("index.html", "w") as f:
    f.write(content)
