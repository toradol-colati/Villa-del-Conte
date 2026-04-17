import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update Scripts
content = content.replace(
    '<script src="script.js"></script>',
    '<script src="translations.js"></script>\n<script src="script.js"></script>'
)

# 2. Nav Menu & Language Selector
nav_target = """<nav class="main-nav" aria-label="Navigazione principale">
        <div class="container" role="tablist">
            <button class="nav-btn active" role="tab" aria-selected="true" aria-controls="strutture" id="tab-strutture" data-target="strutture">Le Strutture</button>
            <button class="nav-btn" role="tab" aria-selected="false" aria-controls="chi-siamo" id="tab-chi-siamo" data-target="chi-siamo">Chi Siamo</button>
            <button class="nav-btn" role="tab" aria-selected="false" aria-controls="faq" id="tab-faq" data-target="faq">FAQ</button>
        </div>
    </nav>"""

nav_replacement = """<nav class="main-nav" aria-label="Navigazione principale">
        <div class="container" role="tablist" style="position: relative;">
            <div class="nav-tabs">
                <button class="nav-btn active" role="tab" aria-selected="true" aria-controls="strutture" id="tab-strutture" data-target="strutture" data-i18n="nav_structures">Le Strutture</button>
                <button class="nav-btn" role="tab" aria-selected="false" aria-controls="blog" id="tab-blog" data-target="blog" data-i18n="nav_blog">Notebook</button>
                <button class="nav-btn" role="tab" aria-selected="false" aria-controls="chi-siamo" id="tab-chi-siamo" data-target="chi-siamo" data-i18n="nav_about">Chi Siamo</button>
                <button class="nav-btn" role="tab" aria-selected="false" aria-controls="faq" id="tab-faq" data-target="faq" data-i18n="nav_faq">FAQ</button>
            </div>
            <div class="lang-selector">
                <select id="lang-switch" class="lang-select" aria-label="Seleziona la lingua">
                    <option value="it">🇮🇹 IT</option>
                    <option value="en">🇬🇧 EN</option>
                    <option value="es">🇪🇸 ES</option>
                    <option value="ru">🇷🇺 RU</option>
                    <option value="de">🇩🇪 DE</option>
                    <option value="zh">🇨🇳 ZH</option>
                </select>
            </div>
        </div>
    </nav>"""

if nav_target in content:
    content = content.replace(nav_target, nav_replacement)

# 3. Add Blog Section
faq_section_target = """        <section id="faq" class="content-section">
            <div class="container" style="padding: 60px 20px; text-align: center;">
                <h2 class="property-title">Domande Frequenti</h2>
                <p class="property-description">Le domande più comuni dei nostri ospiti.</p>
            </div>
        </section>"""

blog_section = """        <section id="faq" class="content-section">
            <div class="container fade-in-up" style="padding: 60px 20px; text-align: center;">
                <h2 class="property-title" data-i18n="faq_title">Domande Frequenti</h2>
                <p class="property-description" data-i18n="faq_subtitle">Le domande più comuni dei nostri ospiti.</p>
            </div>
        </section>

        <section id="blog" class="content-section">
            <div class="container fade-in-up">
                <div class="blog-grid">
                    <!-- Placeholder Blog post 1 -->
                    <article class="blog-card">
                        <div class="blog-image placeholder-img"></div>
                        <div class="blog-content">
                            <h3>Il fascino della Costa degli Dei</h3>
                            <p>Scopri le spiagge nascoste e i tramonti indimenticabili a pochi passi dalla nostra struttura...</p>
                            <a href="#" class="read-more">Leggi di più →</a>
                        </div>
                    </article>
                    <!-- Placeholder Blog post 2 -->
                    <article class="blog-card">
                        <div class="blog-image placeholder-img"></div>
                        <div class="blog-content">
                            <h3>I migliori ristoranti di Tropea</h3>
                            <p>Una selezione dei locali imperdibili dove gustare le migliori specialità del territorio fiero della Calabria...</p>
                            <a href="#" class="read-more">Leggi di più →</a>
                        </div>
                    </article>
                    <!-- Placeholder Blog post 3 -->
                    <article class="blog-card">
                        <div class="blog-image placeholder-img"></div>
                        <div class="blog-content">
                            <h3>Tropea: Il Borgo dei Borghi</h3>
                            <p>Un viaggio nella storia millenaria della nostra amata perla del Tirreno e le sue tradizioni...</p>
                            <a href="#" class="read-more">Leggi di più →</a>
                        </div>
                    </article>
                </div>
            </div>
        </section>"""

if faq_section_target in content:
    content = content.replace(faq_section_target, blog_section)

# 4. Insert data-i18n attributes
# The texts have to be mapped.
replacements = [
    ('<h2 class="property-title" style="text-align: left;">La Villa</h2>', '<h2 class="property-title" style="text-align: left;" data-i18n="villa_title">La Villa</h2>'),
    ('<h2 class="property-title" style="text-align: right;">La Conte House</h2>', '<h2 class="property-title" style="text-align: right;" data-i18n="conte_title">La Conte House</h2>'),
    ('<span>WiFi Gratuito</span>', '<span data-i18n="service_wifi">WiFi Gratuito</span>'),
    ('<span>Accesso Disabili</span>', '<span data-i18n="service_disabled">Accesso Disabili</span>'),
    ('<span>Parcheggio</span>', '<span data-i18n="service_parking">Parcheggio</span>'),
    ('<p class="property-description">È la soluzione ideale per famiglie numerose o gruppi di amici che desiderano condividere una vacanza indimenticabile.</p>', '<p class="property-description" data-i18n="villa_desc_1">È la soluzione ideale per famiglie numerose o gruppi di amici che desiderano condividere una vacanza indimenticabile.</p>'),
    ('<p class="property-description">Dispone di tre camere da letto, un grande soggiorno, una cucina perfettamente attrezzata e due bagni, il tutto circondato da un meraviglioso giardino privato.</p>', '<p class="property-description" data-i18n="villa_desc_2">Dispone di tre camere da letto, un grande soggiorno, una cucina perfettamente attrezzata e due bagni, il tutto circondato da un meraviglioso giardino privato.</p>'),
    ('<p class="property-description">Godetevi la comodità di spazi pensati per il relax e il divertimento di tutti, a soli 500m dalla spiaggia.</p>', '<p class="property-description" data-i18n="villa_desc_3">Godetevi la comodità di spazi pensati per il relax e il divertimento di tutti, a soli 500m dalla spiaggia.</p>'),
    ('<p class="property-description">Una dependance accogliente e riservata, perfetta per coppie o piccole famiglie.</p>', '<p class="property-description" data-i18n="conte_desc_1">Una dependance accogliente e riservata, perfetta per coppie o piccole famiglie.</p>'),
    ('<p class="property-description">Questa suite indipendente è composta da una camera da letto con TV, un bagno privato e un soggiorno con una moderna cucina a vista.</p>', '<p class="property-description" data-i18n="conte_desc_2">Questa suite indipendente è composta da una camera da letto con TV, un bagno privato e un soggiorno con una moderna cucina a vista.</p>'),
    ('<p class="contact-subtitle" style="margin: 0;">— <em>contattaci</em> per prenotare ed ottenere uno <strong>SCONTO!</strong> —</p>', '<p class="contact-subtitle" style="margin: 0;" data-i18n="contact_banner" data-html="true">— <em>contattaci</em> per prenotare ed ottenere uno <strong>SCONTO!</strong> —</p>'),
    ('<h3 class="property-title" style="text-align: center; font-size: 2.5em;">Richiesta di Prenotazione</h3>', '<h3 class="property-title" style="text-align: center; font-size: 2.5em;" data-i18n="form_title">Richiesta di Prenotazione</h3>'),
    ('<p style="text-align: center; color: #555; margin-bottom: 30px;">Compila il modulo, ti risponderemo tempestivamente.</p>', '<p style="text-align: center; color: #555; margin-bottom: 30px;" data-i18n="form_subtitle">Compila il modulo, ti risponderemo tempestivamente.</p>'),
    ('<label for="email">Email *</label>', '<label for="email" data-i18n="form_email">Email *</label>'),
    ('<label for="phone">Telefono *</label>', '<label for="phone" data-i18n="form_phone">Telefono *</label>'),
    ('<label for="checkin">Check-in</label>', '<label for="checkin" data-i18n="form_checkin">Check-in</label>'),
    ('<label for="checkout">Check-out</label>', '<label for="checkout" data-i18n="form_checkout">Check-out</label>'),
    ('<label for="structure">Struttura di interesse</label>', '<label for="structure" data-i18n="form_structure">Struttura di interesse</label>'),
    ('<option value="La Villa">La Villa</option>', '<option value="La Villa" data-i18n="form_opt_villa">La Villa</option>'),
    ('<option value="La Conte House">La Conte House</option>', '<option value="La Conte House" data-i18n="form_opt_conte">La Conte House</option>'),
    ('<option value="Entrambe">Entrambe (Intera Proprietà)</option>', '<option value="Entrambe" data-i18n="form_opt_both">Entrambe (Intera Proprietà)</option>'),
    ('<option value="Solo Informazioni">Solo Informazioni generiche</option>', '<option value="Solo Informazioni" data-i18n="form_opt_info">Solo Informazioni generiche</option>'),
    ('<label for="message">Messaggio / Richieste speciali *</label>', '<label for="message" data-i18n="form_msg">Messaggio / Richieste speciali *</label>'),
    ('<button type="submit" class="submit-btn">Invia Richiesta</button>', '<button type="submit" class="submit-btn" data-i18n="form_submit">Invia Richiesta</button>'),
    ('<p>Ci troviamo a 4.4km da Tropea, precisamente a Santa Domenica di Ricadi e sulla Costa degli Dei, nota per le spiagge mozzafiato ed il mare cristallino.</p>', '<p data-i18n="about_desc_1">Ci troviamo a 4.4km da Tropea, precisamente a Santa Domenica di Ricadi e sulla Costa degli Dei, nota per le spiagge mozzafiato ed il mare cristallino.</p>'),
    ('<p>La zona offre ristoranti, bar, negozi e tutti i comfort per una vacanza rilassante ed in pochi minuti è possibile raggiungere Capo Vaticano e Tropea.</p>', '<p data-i18n="about_desc_2">La zona offre ristoranti, bar, negozi e tutti i comfort per una vacanza rilassante ed in pochi minuti è possibile raggiungere Capo Vaticano e Tropea.</p>'),
    ('<p style="font-size: 1.1em;">Per rendere il vostro soggiorno ancora più sereno e personalizzato, siamo felici di offrire una serie di <strong>servizi esclusivi su richiesta</strong>:</p>', '<p style="font-size: 1.1em;" data-i18n="about_subtitle" data-html="true">Per rendere il vostro soggiorno ancora più sereno e personalizzato, siamo felici di offrire una serie di <strong>servizi esclusivi su richiesta</strong>:</p>'),
    ('<span>Servizio Biancheria</span>', '<span data-i18n="service_laundry">Servizio Biancheria</span>'),
    ('<span>Noleggio Auto</span>', '<span data-i18n="service_car">Noleggio Auto</span>'),
    ('<span>Noleggio Bici</span>', '<span data-i18n="service_bike">Noleggio Bici</span>'),
    ('<span>Navetta Aeroportuale</span>', '<span data-i18n="service_transfer">Navetta Aeroportuale</span>'),
    ('class="property-block"', 'class="property-block fade-in-up"'),
    ('class="booking-form-container"', 'class="booking-form-container fade-in-up"'),
    ('class="map-section"', 'class="map-section fade-in-up"'),
    ('class="location-info"', 'class="location-info fade-in-up"'),
    ('class="services-bar"', 'class="services-bar fade-in-up"'),
    ('class="contact-info"', 'class="contact-info fade-in-up"'),
]

for old, new in replacements:
    content = content.replace(old, new)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated index.html")
