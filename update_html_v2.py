import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update Chi Siamo
chi_siamo_old = """                <div class="who-we-are-intro fade-in-up" style="margin-bottom: 50px; text-align: center; max-width: 800px; margin-left: auto; margin-right: auto;">
                    <h2 class="property-title" data-i18n="about_intro_title">La Nostra Accoglienza</h2>
                    <p class="property-description" style="font-size: 1.1em; line-height: 1.8;" data-i18n="about_intro_p1">Benvenuti a Villa del Conte. Da anni ci dedichiamo all'ospitalità, aprendo le porte di una delle zone più affascinanti della Costa degli Dei. Il nostro obiettivo è farvi sentire a casa, offrendovi ambienti curati in un contesto sereno e vicino al mare, per garantirvi una vacanza indimenticabile unendo modernità a tradizione.</p>
                </div>"""
chi_siamo_new = """                <div class="who-we-are-intro fade-in-up" style="margin-bottom: 50px; text-align: center; max-width: 800px; margin-left: auto; margin-right: auto;">
                    <p class="property-description" style="font-size: 1.1em; line-height: 1.8;" data-i18n="about_intro_p1">Ci dedichiamo all'ospitalità, aprendo le porte di una delle zone più affascinanti della Costa degli Dei. Il nostro obiettivo è farvi sentire a casa, offrendovi ambienti curati in un contesto sereno e vicino al mare, per garantirvi una vacanza indimenticabile unendo modernità a tradizione.</p>
                </div>"""
content = content.replace(chi_siamo_old, chi_siamo_new)

# 2. Update Form and Options
content = content.replace("Richiesta di Prenotazione", "Richiesta di informazioni")
content = content.replace("Richiesta di informazioni", "Richiesta di informazioni") # handled in code
content = content.replace('<h3 class="property-title" style="text-align: center; font-size: 2.5em;" data-i18n="form_title">Richiesta di Prenotazione</h3>', '<h3 class="property-title" style="text-align: center; font-size: 2.5em;" data-i18n="form_title">Richiesta di informazioni</h3>')
option_to_remove = '<option value="Solo Informazioni" data-i18n="form_opt_info">Solo Informazioni generiche</option>'
content = content.replace(option_to_remove, "")

# 3. Update discount banner
content = content.replace("— <em>contattaci</em> per prenotare ed ottenere uno <strong>SCONTO!</strong> —", "— <em>contattaci</em> per un'<strong>offerta riservata</strong> —")


# 4. Remove Carousel Emojis and add below Conte House
villa_services_old = """            <div class="services-col">
                <div class="service-item"><i class="fa-solid fa-wifi"></i> <span data-i18n="service_wifi">WiFi Gratuito</span></div>
                <div class="service-item"><i class="fa-solid fa-wheelchair-move"></i> <span data-i18n="service_disabled">Accesso Disabili</span></div>
                <div class="service-item"><i class="fa-solid fa-square-parking"></i> <span data-i18n="service_parking">Parcheggio</span></div>
            </div>"""
content = content.replace(villa_services_old, "")

conte_services_old = """            <div class="services-col">
                <div class="service-item"><i class="fa-solid fa-wifi"></i> <span data-i18n="service_wifi">WiFi Gratuito</span></div>
            </div>"""
content = content.replace(conte_services_old, "")

# We need to add the new horizontal row BELOW the .property-list (end of Conte House block, but inside .container of properties-section)
property_list_end = "</div>          </div> </section>"
new_horizontal_services = """</div>
                    <div class="services-bar fade-in-up" style="margin-top: 50px; border-top: 1px solid #eee; padding-top: 30px;">
                        <div class="service-item"><i class="fa-solid fa-wifi"></i><span data-i18n="service_wifi">WiFi Gratuito</span></div>
                        <div class="service-item"><i class="fa-solid fa-square-parking"></i><span data-i18n="service_parking">Parcheggio</span></div>
                        <div class="service-item"><i class="fa-solid fa-person-hiking"></i><span data-i18n="service_excursion">Escursioni</span></div>
                        <div class="service-item"><i class="fa-solid fa-fire-burner"></i><span data-i18n="service_bbq">Barbecue</span></div>
                    </div>
                </div> </section>"""
content = content.replace(property_list_end, new_horizontal_services)


# 5. Notebook Section rebuild + Modal removal
content = re.sub(r'<!-- Modal I Toraldo -->.*</div>\s*</div>\s*</div>', '', content, flags=re.DOTALL)
content = content.replace("onclick=\"document.getElementById('toraldo-modal').classList.add('active')\"", "onclick=\"window.location.href='blog-toraldo.html'\"")


# 6. Add FAQ Accordions
old_faq = """        <section id="faq" class="content-section">
            <div class="container fade-in-up" style="padding: 60px 20px; text-align: center;">
                <h2 class="property-title" data-i18n="faq_title">Domande Frequenti</h2>
                <p class="property-description" data-i18n="faq_subtitle">Le domande più comuni dei nostri ospiti.</p>
            </div>
        </section>"""
new_faq = """        <section id="faq" class="content-section">
            <div class="container fade-in-up" style="padding: 60px 20px; max-width: 800px; margin: 0 auto;">
                <h2 class="property-title" style="text-align: center;" data-i18n="faq_title">Domande Frequenti</h2>
                <p class="property-description" style="text-align: center; margin-bottom: 40px;" data-i18n="faq_subtitle">Le domande più comuni dei nostri ospiti.</p>
                <div class="faq-accordion">
                    <div class="faq-item">
                        <button class="faq-question" aria-expanded="false"><span data-i18n="faq_q1">A che distanza si trovano le spiagge principali?</span><i class="fa-solid fa-chevron-down"></i></button>
                        <div class="faq-answer"><p data-i18n="faq_a1">Le spiagge di Santa Domenica di Ricadi, così come quelle di Tropea e Capo Vaticano, distano pochissimi minuti dalla struttura.</p></div>
                    </div>
                    <div class="faq-item">
                        <button class="faq-question" aria-expanded="false"><span data-i18n="faq_q2">Il WiFi è disponibile in tutta la struttura?</span><i class="fa-solid fa-chevron-down"></i></button>
                        <div class="faq-answer"><p data-i18n="faq_a2">Sì, la connessione WiFi è gratuita e copre per intero sia le abitazioni che le zone circostanti.</p></div>
                    </div>
                    <div class="faq-item">
                        <button class="faq-question" aria-expanded="false"><span data-i18n="faq_q3">Viene fornita la biancheria da letto e da bagno?</span><i class="fa-solid fa-chevron-down"></i></button>
                        <div class="faq-answer"><p data-i18n="faq_a3">Certamente, il servizio biancheria è disponibile su richiesta per garantirvi il massimo comfort durante il vostro soggiorno.</p></div>
                    </div>
                    <div class="faq-item">
                        <button class="faq-question" aria-expanded="false"><span data-i18n="faq_q4">Gli animali domestici sono ammessi?</span><i class="fa-solid fa-chevron-down"></i></button>
                        <div class="faq-answer"><p data-i18n="faq_a4">Gli animali non sono ammessi all'interno delle nostre abitazioni per tutelare gli ospiti con eventuali allergie.</p></div>
                    </div>
                    <div class="faq-item">
                        <button class="faq-question" aria-expanded="false"><span data-i18n="faq_q5">È consentito fumare all'interno?</span><i class="fa-solid fa-chevron-down"></i></button>
                        <div class="faq-answer"><p data-i18n="faq_a5">All'interno è severamente vietato fumare. Tuttavia, disponiamo di ampi spazi all'aperto dotati di comfort.</p></div>
                    </div>
                </div>
            </div>
        </section>"""
content = content.replace(old_faq, new_faq)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated index.html elements")
