import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Define the HTML snippet for the reviews
reviews_html = """                <div class="reviews-section fade-in-up" style="margin-top: 60px; padding-top: 40px; border-top: 1px solid #eaeaea;">
                    <h3 class="property-title" style="text-align: center; margin-bottom: 40px;" data-i18n="reviews_title">Dicono di noi</h3>
                    <div class="reviews-grid">
                        
                        <!-- Google Maps Review -->
                        <div class="review-card google-card">
                            <div class="review-header">
                                <div class="review-avatar">L</div>
                                <div class="review-meta">
                                    <span class="review-author">Larisa Susi</span>
                                    <span class="review-source"><i class="fa-brands fa-google"></i> Google Maps · 6 mesi fa</span>
                                </div>
                                <div class="review-rating">5/5</div>
                            </div>
                            <div class="review-stars google-stars">
                                <i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i>
                            </div>
                            <div class="review-body">
                                <p>Se desiderate vera pace, tranquillità e comfort, pur trovandovi nelle immediate vicinanze di Tropea, questo appartamento... è perfetto per voi. Il giardino privato, con alberi di limoni e mandarini, offre una meravigliosa ombra, c'è un barbecue nel cortile e tutto è attrezzato per trascorrere una piacevole serata in compagnia. La splendida spiaggia autentica è vicinissima alla casa... 4 minuti di treno e siete nel cuore di Tropea. Ma il gioiello più importante di questo alloggio è Francesco. Un ragazzo adorabile, amichevole e gentile che risponde immediatamente alle vostre richieste...</p>
                            </div>
                        </div>

                        <!-- Booking Review 1 -->
                        <div class="review-card booking-card">
                            <div class="review-header">
                                <div class="review-avatar">G</div>
                                <div class="review-meta">
                                    <span class="review-author">Giacomo <span style="font-size: 0.8em; color: #888;">🇮🇹 Italia</span></span>
                                    <span class="review-source">Booking.com · 10 agosto 2024</span>
                                </div>
                                <div class="review-rating-box">10</div>
                            </div>
                            <h4 class="review-title">Soggiorno fantastico a Santa Domenica</h4>
                            <div class="review-body">
                                <p><span style="color: #28a745;"><i class="fa-regular fa-face-smile"></i></span> Francesco é un host fantastico. Ci mette passione e amore in quello che fa e lo si vede dalla disponibilità e della cura dell'abitazione. Fornisce ogni tipo di supporto e consiglio. Davvero unica ed completa la guida da lui prodotta... Comunicazione eccezionale e nessun problema riscontrato nonostante la prenotazione fatta all'ultimo momento... Davvero consigliatissimo!</p>
                            </div>
                        </div>

                        <!-- Airbnb Review -->
                        <div class="review-card airbnb-card">
                            <div class="review-header">
                                <div class="review-avatar" style="background-image: url('https://randomuser.me/api/portraits/men/32.jpg'); background-size: cover; text-indent: -9999px;">C</div>
                                <div class="review-meta">
                                    <span class="review-author">Claudio</span>
                                    <span class="review-source"><i class="fa-brands fa-airbnb"></i> Airbnb · September 2024</span>
                                </div>
                            </div>
                            <div class="review-stars airbnb-stars">
                                <i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i>
                            </div>
                            <div class="review-body">
                                <p>Cozy accommodation in a well-served location and close to the village. Completely as described. Friendly host and available for every request. Recommended!</p>
                            </div>
                        </div>

                        <!-- Booking Review 2 -->
                        <div class="review-card booking-card">
                            <div class="review-header">
                                <div class="review-avatar">A</div>
                                <div class="review-meta">
                                    <span class="review-author">Antonino <span style="font-size: 0.8em; color: #888;">🇮🇹 Italia</span></span>
                                    <span class="review-source">Booking.com · 15 luglio 2025</span>
                                </div>
                                <div class="review-rating-box">9,0</div>
                            </div>
                            <h4 class="review-title">Eccellente</h4>
                            <div class="review-body">
                                <p><span style="color: #28a745;"><i class="fa-regular fa-face-smile"></i></span> Ambiente spazioso, ideale per famiglie. Zanzariere, condizionatori ed uno spazioso giardino. Qualche svista qua e la, ma ritornerei certamente. Francesco è stato a disposizione per tutto il soggiorno, sempre reperibile e puntuale.</p>
                            </div>
                        </div>

                        <!-- Booking Review 3 -->
                        <div class="review-card booking-card">
                            <div class="review-header">
                                <div class="review-avatar">P</div>
                                <div class="review-meta">
                                    <span class="review-author">Panarit <span style="font-size: 0.8em; color: #888;">🇸🇪 Svezia</span></span>
                                    <span class="review-source">Booking.com · 27 luglio 2024</span>
                                </div>
                                <div class="review-rating-box">8,0</div>
                            </div>
                            <h4 class="review-title">Bästa Francesco</h4>
                            <div class="review-body">
                                <p><span style="color: #28a745;"><i class="fa-regular fa-face-smile"></i></span> Vår upplevelse i huset var jättebra, vår husvärd Francesco var en toppen värd. Allt som vi behövde han fixade...</p>
                                <p style="margin-top: 5px;"><span style="color: #dc3545;"><i class="fa-regular fa-face-frown"></i></span> Det som var inte så bra att man kunde ej dricka vattnet... Men det gjorde inget för att allt annat var toppen.</p>
                            </div>
                        </div>

                        <!-- Booking Review 4 -->
                        <div class="review-card booking-card">
                            <div class="review-header">
                                <div class="review-avatar">G</div>
                                <div class="review-meta">
                                    <span class="review-author">Giuliatt <span style="font-size: 0.8em; color: #888;">🇮🇹 Italia</span></span>
                                    <span class="review-source">Booking.com · 21 luglio 2025</span>
                                </div>
                                <div class="review-rating-box">9,0</div>
                            </div>
                            <h4 class="review-title">Eccellente</h4>
                            <div class="review-body">
                                <p style="color: #777; font-style: italic;">L'ospite non ha lasciato un commento</p>
                            </div>
                        </div>

                    </div>
                </div>
"""

# Insert reviews right after the intro text inside "chi-siamo" section
target = """</div>
                <div class="map-section fade-in-up">"""
if target in content:
    content = content.replace(target, "</div>" + reviews_html + """                <div class="map-section fade-in-up">""")
else:
    print("Could not find the insertion point for reviews!")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

with open('style.css', 'a', encoding='utf-8') as f:
    f.write("""
/* REVIEWS GRID CSS */
.reviews-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 20px;
    margin-bottom: 40px;
}
.review-card {
    background: #fff;
    border-radius: 12px;
    padding: 24px;
    text-align: left;
    box-shadow: 0 4px 15px rgba(0,0,0,0.05);
    border: 1px solid #eee;
    display: flex;
    flex-direction: column;
}
.review-header {
    display: flex;
    align-items: center;
    margin-bottom: 15px;
}
.review-avatar {
    width: 45px;
    height: 45px;
    border-radius: 50%;
    background: #4a9d5f;
    color: white;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 1.2em;
    font-weight: bold;
    margin-right: 15px;
}
.review-meta {
    flex-grow: 1;
    display: flex;
    flex-direction: column;
}
.review-author {
    font-family: 'Poppins', sans-serif;
    font-weight: 600;
    color: #333;
}
.review-source {
    font-size: 0.8em;
    color: #666;
}
.review-body p {
    font-size: 0.95em;
    line-height: 1.6;
    color: #444;
}
.review-title {
    font-family: 'Poppins', sans-serif;
    font-size: 1.05em;
    font-weight: 600;
    margin: 5px 0 10px 0;
}
.review-rating {
    font-weight: bold;
    font-size: 1.2em;
}

/* Specific Styles */
.google-card { border-top: 4px solid #ea4335; }
.google-stars { color: #fbbc05; margin-bottom: 10px; font-size: 0.9em; }

.booking-card { border-top: 4px solid #003580; }
.review-rating-box {
    background: #003580;
    color: white;
    border-radius: 6px 6px 6px 0;
    padding: 5px 8px;
    font-weight: bold;
    display: flex;
    align-items: center;
    justify-content: center;
}

.airbnb-card { border-top: 4px solid #ff5a5f; }
.airbnb-stars { color: #ff5a5f; margin-bottom: 10px; font-size: 0.9em; }
""")

print("Updated reviews!")
