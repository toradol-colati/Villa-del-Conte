import re

grid_html = """                <div class="blog-grid">
                    <article class="blog-card" onclick="window.location.href='blog-territorio.html'">
                        <div class="blog-image" style="background-image: url('images/blog/territorio.jpg');"></div>
                        <div class="blog-content">
                            <h3>Storia del Territorio</h3>
                            <p>Il territorio che circonda Villa del Conte a Santa Domenica di Ricadi, sulla suggestiva Costa degli Dei in Calabria, è un mosaico vivo di epo...</p>
                            <span class="read-more" data-i18n="read_more">Leggi di più →</span>
                        </div>
                    </article>
                    <article class="blog-card" onclick="window.location.href='blog-romane.html'">
                        <div class="blog-image" style="background-image: url('images/blog/romane.jpg');"></div>
                        <div class="blog-content">
                            <h3>Origini Romane</h3>
                            <p>Le origini romane del territorio intorno a Santa Domenica di Ricadi e Tropea, sulla Costa degli Dei in Calabria, riportano a un’epoca di co...</p>
                            <span class="read-more" data-i18n="read_more">Leggi di più →</span>
                        </div>
                    </article>
                    <article class="blog-card" onclick="window.location.href='blog-toraldo.html'">
                        <div class="blog-image" style="background-image: url('images/blog/toraldo.jpg'); background-position: top center;"></div>
                        <div class="blog-content">
                            <h3>Toraldo e Federico II</h3>
                            <p>Nel cuore della Costa degli Dei, tra le scogliere di Tropea e le spiagge cristalline di Santa Domenica di Ricadi, la figura dell’imperato...</p>
                            <span class="read-more" data-i18n="read_more">Leggi di più →</span>
                        </div>
                    </article>
                    <article class="blog-card" onclick="window.location.href='blog-costa.html'">
                        <div class="blog-image" style="background-image: url('images/blog/costa.jpg');"></div>
                        <div class="blog-content">
                            <h3>La Costa degli Dei</h3>
                            <p>La Costa degli Dei è uno dei tratti di litorale più spettacolari d’Italia, un paradiso calabrese che si snoda per circa 50 chilometri lu...</p>
                            <span class="read-more" data-i18n="read_more">Leggi di più →</span>
                        </div>
                    </article>
                    <article class="blog-card" onclick="window.location.href='blog-tropea.html'">
                        <div class="blog-image" style="background-image: url('images/blog/tropea.jpg');"></div>
                        <div class="blog-content">
                            <h3>Tropea: Il Borgo dei Borghi</h3>
                            <p>Tropea, la “perla del Tirreno” e più volte eletta Borgo dei Borghi d’Italia, domina la Costa degli Dei in Calabria con un fascino irresist...</p>
                            <span class="read-more" data-i18n="read_more">Leggi di più →</span>
                        </div>
                    </article>
                    <article class="blog-card" onclick="window.location.href='blog-santadomenica.html'">
                        <div class="blog-image" style="background-image: url('images/blog/santadomenica.jpg');"></div>
                        <div class="blog-content">
                            <h3>Santa Domenica di Ricadi</h3>
                            <p>Santa Domenica di Ricadi, frazione del comune di Ricadi sulla Costa degli Dei in Calabria – e non da confondere con l’omonima località...</p>
                            <span class="read-more" data-i18n="read_more">Leggi di più →</span>
                        </div>
                    </article>
                    <article class="blog-card" onclick="window.location.href='blog-cucina.html'">
                        <div class="blog-image" style="background-image: url('images/blog/cucina.jpg');"></div>
                        <div class="blog-content">
                            <h3>Tradizioni Culinarie</h3>
                            <p>Le tradizioni culinarie della Costa degli Dei rappresentano l’anima autentica della Calabria, un’esplosione di sapori intensi e ingredienti...</p>
                            <span class="read-more" data-i18n="read_more">Leggi di più →</span>
                        </div>
                    </article>
                </div>"""

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Replace block
pattern = r'<div class="blog-grid">.*?</div>\s*</div>\s*</section>'
replacement = grid_html + '\n            </div>\n        </section>'
text = re.sub(pattern, replacement, text, flags=re.DOTALL)

# Add cache busting to CSS
css_cache = """<meta http-equiv="Cache-Control" content="no-cache, no-store, must-revalidate" />
    <meta http-equiv="Pragma" content="no-cache" />
    <meta http-equiv="Expires" content="0" />
    <link rel="stylesheet" href="style.css?v=2.0">"""
text = text.replace('<link rel="stylesheet" href="style.css">', css_cache)

# Add cache busting to JS
text = text.replace('<script src="translations.js"></script>', '<script src="translations.js?v=2.0"></script>')
text = text.replace('<script src="script.js"></script>', '<script src="script.js?v=2.0"></script>')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("index.html updated successfully!")
