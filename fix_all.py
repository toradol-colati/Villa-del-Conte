import re

# 1. FIX INDEX.HTML CARD
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

old_card_content = """                        <img src="http://www.nobili-napoletani.it/images/foto/T/Toraldo/Tropea,%20stemma%20Toraldo.png" alt="Card Image" class="card-image" style="object-fit: cover; height: 200px; cursor: pointer;" onclick="window.location.href='blog-toraldo.html'">
                        <div class="card-body">
                            <h3 class="property-title" style="margin-top:0;" data-i18n="blog_toraldo_title">I Toraldo a Tropea</h3>
                            <p class="property-description" data-i18n="blog_toraldo_desc">Scopri il legame indissolubile tra l'antica famiglia nobiliare, arrivata con l'Imperatore Federico II, e i tesori architettonici e terrieri di Tropea e dintorni...</p>
                            <a href="blog-toraldo.html" style="color: #4a9d5f; text-decoration: none; font-weight: 600;" data-i18n="blog_read_more">Leggi di più &rarr;</a>
                        </div>"""

new_card_content = """                        <img src="images/ui/stemma.png" alt="Stemma Toraldo" class="card-image" style="object-fit: contain; padding: 20px; height: 250px; cursor: pointer; background: #fff;" onclick="window.location.href='blog-toraldo.html'">
                        <div class="card-body" style="background-color: #fcf8f2; border-top: 1px solid #eee;">
                            <h3 class="property-title" style="margin-top:0; font-size: 1.6em; color: #222;" data-i18n="blog_toraldo_title">I Toraldo a Tropea</h3>
                            <p class="property-description" style="font-size: 0.95em; line-height: 1.6; text-align: justify; margin-bottom: 15px;">Dalle nebbie delle dinastie germaniche medievali giunsero nel sud Italia al seguito dell'Imperatore Federico II di Svevia. Ascritti al patriziato di Tropea dal 1508, la famiglia Toraldo non si limitò all'amministrazione politica ma plasmò l'architettura e l'economia dell'intera Costa degli Dei. Scoprili attraverso le antiche pietre di Palazzo Toraldo col suo preziosissimo archivio millenario, o passeggiando tra i fertili agrumeti e vigneti che costituivano i vasti latifondi della famiglia a Santa Domenica di Ricadi, e immergiti nell'atmosfera del loro romantico svago estivo al Castello Galluppi-Toraldo di Caria.</p>
                            <a href="blog-toraldo.html" style="display: inline-block; padding: 10px 20px; background-color: #4a9d5f; color: white; border-radius: 5px; text-decoration: none; font-weight: 600; text-align: center; width: 100%;" data-i18n="blog_read_more">Esplora la storia completa</a>
                        </div>"""

if old_card_content in content:
    content = content.replace(old_card_content, new_card_content)
else:
    # Aggressively force replace using regex if there was a slight mismatch
    content = re.sub(r'<img src="http://www\.nobili-napoletani\.it/.*?</div>', new_card_content, content, flags=re.DOTALL)

# Add explicit inline styles to .blog-card to defeat cache
content = content.replace('<div class="blog-card">', '<div class="blog-card" style="max-width: 450px; background-color: #fcf8f2; border: 1px solid #e5d8c5; border-radius: 12px; box-shadow: 0 10px 30px rgba(0,0,0,0.12); overflow: hidden; margin: 0 auto;">')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

# 2. FIX BLOG-TORALDO.HTML FULL PAGE
blog_html = """<!DOCTYPE html>
<html lang="it">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>I Toraldo a Tropea | Villa del Conte</title>
    <meta name="description" content="Scopri la storia millenaria della nobile famiglia Toraldo, il castello a Caria d'epoca sveva e le splendide terre a Santa Domenica di Ricadi in Calabria.">
    <link rel="icon" type="image/png" href="images/ui/logo.png">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300..700;1,300..700&family=Lato:ital,wght@0,100;0,300;0,400;0,700;0,900;1,100;1,300;1,400;1,700;1,900&family=Poppins:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="style.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.2/css/all.min.css">
    <style>
        .blog-section-image { width: 100%; border-radius: 4px; border: 1px solid #dee2e6; box-shadow: 0 4px 15px rgba(0,0,0,0.05); }
        .text-column p { margin-bottom: 25px; text-align: justify; }
        .editorial-row { display: flex; flex-wrap: wrap; gap: 50px; align-items: start; margin-bottom: 80px; }
        .text-column { flex: 1; min-width: 300px; }
        .image-column { flex: 1; min-width: 300px; }
    </style>
</head>
<body style="background-color: #fdfbf7; margin: 0; padding: 0;">

    <a href="index.html" id="sticky-logo" style="position: absolute; top: 20px; left: 20px; z-index:1000;">
        <img src="images/ui/logo.png" alt="Logo Villa del Conte" style="width: 60px;">
    </a>

    <!-- Flat header, no padding bubble -->
    <header style="background-image: linear-gradient(to bottom, rgba(0, 0, 0, 0.4) 0%, rgba(0, 0, 0, 0.7) 100%), url('https://upload.wikimedia.org/wikipedia/commons/thumb/8/8f/Tropea2.jpg/1920px-Tropea2.jpg'); background-size: cover; background-position: center bottom; padding: 180px 20px 100px 20px; text-align: center; color: white;">
        <div style="max-width: 800px; margin: 0 auto;">
             <img src="images/ui/stemma.png" alt="Stemma Toraldo" style="max-width: 140px; margin: 0 auto 30px auto; display: block; filter: drop-shadow(0 4px 8px rgba(0,0,0,0.5));">
             <h1 style="font-family: 'Cormorant Garamond', serif; font-size: 4em; margin: 0; text-shadow: 0 2px 4px rgba(0,0,0,0.8);">I Toraldo a Tropea</h1>
             <p style="font-family: 'Lato', sans-serif; font-size: 1.4em; letter-spacing: 1px; text-transform: uppercase; margin-top: 20px; opacity: 0.9;">Storia, Nobiltà e Paesaggi della Costa degli Dei</p>
        </div>
    </header>

    <main class="fade-in-up" style="max-width: 1000px; margin: -50px auto 100px auto; background: #fff; padding: 80px 60px; box-shadow: 0 20px 50px rgba(0,0,0,0.08); border-radius: 8px; position: relative;">
        
        <p style="font-family: 'Cormorant Garamond', serif; font-size: 1.8em; line-height: 1.6; color: #333; text-align: center; margin-bottom: 60px; padding: 0 40px;">
            Dalle origini germaniche al cuore del Regno di Napoli: l'ascesa secolare della famiglia che ha scolpito la Costa degli Dei.
        </p>
        
        <div class="editorial-row">
            <div class="text-column" style="font-family: 'Lato', sans-serif; font-size: 1.15em; line-height: 1.8; color: #555;">
                <p>La <strong>famiglia Toraldo</strong> rappresenta una delle più antiche, venerabili e influenti casate aristocratiche dell'intero <em>Regno di Napoli</em>. Con origini che si perdono nelle nebbie delle dinastie germaniche medievali, le prime testimonianze li vedono giungere in Italia al prestigioso seguito dell'Imperatore Federico II di Svevia.</p>
                <p>Scesi nella penisola con compiti militari ed amministrativi, si ritagliarono un ruolo centrale nel governo delle province meridionali. Intorno alla fine del XV secolo, un importante ramo della casata trovò la sua culla eletta lungo il versante tirrenico della Calabria, venendo ufficialmente ascritti al ristrettissimo ed esclusivo patriziato della città di Tropea dal lontano 1508.</p>
            </div>
            <div class="image-column">
                <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/ca/Tropea_Palazzi.jpg/800px-Tropea_Palazzi.jpg" alt="Centro Storico di Tropea" class="blog-section-image">
                <p style="font-size: 0.85em; color: #888; text-align: right; margin-top: 10px;"><em>Scorci degli antichi palazzi patrizi nel centro storico di Tropea.</em></p>
            </div>
        </div>

        <hr style="border:0; border-top: 1px solid #eaeaea; margin: 80px 0;">

        <div class="editorial-row" style="flex-direction: row-reverse;">
            <div class="text-column" style="font-family: 'Lato', sans-serif; font-size: 1.15em; line-height: 1.8; color: #555;">
                <h2 style="font-family: 'Cormorant Garamond', serif; font-size: 2.2em; color: #222; margin-top: 0;">Palazzo Toraldo e il suo inestimabile Archivio</h2>
                <p>Passeggiando lungo le intricate viuzze basolate del cuore antico di Tropea, ci si imbatte quasi d'improvviso nella sontuosità austera ma elegante del <strong>Palazzo Toraldo</strong> (anticamente d'Aquino-Toraldo). Costruito sull'impronta di antichi manieri difensivi e impreziosito nei secoli con lussuosi cortili e stemmi gentilizi incisi nella pietra, divenne la dimora fissa e il simbolo del potere locale della famiglia.</p>
                <p>Ancora oggi, il prestigio dell'edificio si irradia culturalmente su tutto il territorio grazie al tesoro in esso custodito: l'<em>Archivio Storico privato dei Toraldo</em>. Dichiarato bene di eccezionale interesse da parte dello Stato italiano, tramanda ai posteri un'infinita collezione di pergamene pontificie, registri notarili, atti imperiali e manoscritti diplomatici, il cui nucleo più antico risale direttamente al <strong>XII secolo</strong>.</p>
            </div>
            <div class="image-column">
                <img src="images/ui/stemma.png" alt="Archivio e Stemma" class="blog-section-image" style="background:#fff; object-fit: contain; padding: 40px; box-sizing:border-box;">
                <p style="font-size: 0.85em; color: #888; text-align: right; margin-top: 10px;"><em>L'originale stemma nobiliare Toraldo di Tropea.</em></p>
            </div>
        </div>

        <hr style="border:0; border-top: 1px solid #eaeaea; margin: 80px 0;">

        <div class="editorial-row">
            <div class="text-column" style="font-family: 'Lato', sans-serif; font-size: 1.15em; line-height: 1.8; color: #555;">
                <h2 style="font-family: 'Cormorant Garamond', serif; font-size: 2.2em; color: #222; margin-top: 0;">Terre Marine e Agrumeti a Santa Domenica</h2>
                <p>Il polmone economico su cui si reggeva l'influenza della casata batteva forte nei latifondi circostanti. Prima dello sviluppo del turismo balneare, le distese collinari digradanti verso il blu cobalto della <em>Costa degli Dei</em> erano la cassaforte produttiva locale.</p>
                <p>Le sterminate proprietà del casato abbracciavano quasi integralmente i terreni che oggi costituiscono <strong>Santa Domenica di Ricadi</strong>. Furono i nobili Toraldo a spingere sull'innovazione organica dei campi, commissionando i curatissimi muretti a secco utili per i terrazzamenti vista mare. Terre arse dal sole che regalavano agrumeti lussureggianti, mandorli generosi, pesanti vigneti e storiche distese di cipolle rosse la cui genetica andava formandosi nei secoli.</p>
            </div>
            <div class="image-column">
                <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/d/d3/Golfo_di_Gioia_Tauro.jpg/800px-Golfo_di_Gioia_Tauro.jpg" alt="Coste a terrazzamento" class="blog-section-image">
                <p style="font-size: 0.85em; color: #888; text-align: right; margin-top: 10px;"><em>Panorama tipico delle scogliere e delle campagne lungo la Costa degli Dei.</em></p>
            </div>
        </div>

        <hr style="border:0; border-top: 1px solid #eaeaea; margin: 80px 0;">

        <div class="editorial-row" style="flex-direction: row-reverse; margin-bottom: 0;">
            <div class="text-column" style="font-family: 'Lato', sans-serif; font-size: 1.15em; line-height: 1.8; color: #555;">
                <h2 style="font-family: 'Cormorant Garamond', serif; font-size: 2.2em; color: #222; margin-top: 0;">Il romanticismo del Castello Galluppi</h2>
                <p>Mentre l'inverno scorreva tra le mura urbane, l'avvento della canicola estiva spingeva la famiglia verso le colline di <strong>Caria (frazione di Drapia)</strong>, dove sorgeva lo scenografico <em>Castello Galluppi-Toraldo</em>.</p>
                <p>Nata come dimora estiva prima che come baluardo bellicoso, fu cornice di ritiri umanistici, convegni storici in giardino, simposi serali e cenacoli letterari. I Toraldo amavano accogliere illustri accademici del meridione in questo rifugio spirituale, la cui magnifica eleganza cerca ancora oggi di esser tutelata integralmente dagli sforzi comunitari di preservazione architettonica e memoria feudale.</p>
            </div>
            <div class="image-column">
                <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/91/Castello_galluppi.jpg/800px-Castello_galluppi.jpg" alt="Castello Galluppi" class="blog-section-image">
                <p style="font-size: 0.85em; color: #888; text-align: right; margin-top: 10px;"><em>Antica rappresentazione o rudere signorile nel comune limitrofo.</em></p>
            </div>
        </div>

    </main>

    <div style="text-align: center; margin-bottom: 80px;">
        <a href="index.html" class="submit-btn" style="text-decoration:none; display:inline-block; padding: 15px 40px; font-family: 'Poppins', sans-serif; background-color: #4a9d5f; color: white; border-radius: 6px; font-size: 1.1em; font-weight: 600; transition: transform 0.2s;">
            <i class="fa-solid fa-arrow-left"></i> Torna alla Struttura
        </a>
    </div>

    <!-- Footer base -->
    <footer style="background-color: #2b3034; color: #fff; padding: 40px 0; text-align: center; font-family: 'Poppins', sans-serif;">
        <p style="margin:0; font-size: 0.9em; color: #bbb;">&copy; 2024 Villa del Conte. Tutti i diritti riservati.</p>
    </footer>

    <script src="translations.js"></script>
    <script src="script.js"></script>
</body>
</html>"""

with open('blog-toraldo.html', 'w', encoding='utf-8') as f:
    f.write(blog_html)

print("Card properly styled inline in index.html, blog explicitly flat fixed.")
