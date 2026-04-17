with open("style.css", "r", encoding="utf-8") as f:
    content = f.read()

# Make the card a distinct entity
old_card = """.blog-card {
  background: #fff;
  border-radius: 8px;
  box-shadow: 0 5px 15px rgba(0,0,0,0.05);"""
new_card = """.blog-card {
  background: #ffffff;
  border: 1px solid #e8e0d5;
  border-radius: 12px;
  box-shadow: 0 8px 30px rgba(0,0,0,0.08);"""
content = content.replace(old_card, new_card)

with open("style.css", "w", encoding="utf-8") as f:
    f.write(content)

# Now severely expand blog-toraldo.html and fix images!
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
</head>
<body style="background-color: #fdfbf7;">

    <a href="index.html" id="sticky-logo" style="position: absolute; top: 20px; left: 20px; z-index:1000;">
        <img src="images/ui/logo.png" alt="Logo Villa del Conte" style="width: 60px;">
    </a>

    <!-- Article Header -->
    <header class="blog-header" style="background-image: linear-gradient(to bottom, rgba(0, 0, 0, 0.6) 10%, rgba(253, 251, 247, 1) 100%), url('https://images.unsplash.com/photo-1549884587-81765c9b7405?q=80&w=2000'); background-size: cover; background-position: center; padding: 220px 0 100px 0; position: relative;">
      <div class="container" style="text-align: center;">
         <div class="logo-section" style="background: rgba(255,255,255,0.95); padding: 50px; border-radius: 16px; display: inline-block; box-shadow: 0 15px 40px rgba(0,0,0,0.15); max-width: 800px;">
             <!-- FALLBACK HTTPS ICON INSTEAD OF HTTP HTTP-MIXED CONTENT BROKEN IMAGE! -->
             <div class="logo">
                <i class="fa-solid fa-shield-halved" style="font-size: 5em; color: #4a9d5f; margin-bottom: 20px;"></i>
             </div>
             <h1 class="site-title" style="font-size: 3.5em; margin: 0; color: #222; font-family: 'Cormorant Garamond', serif;" data-i18n="blog_toraldo_title">I Toraldo a Tropea</h1>
             <p style="font-size: 1.2em; color: #555; margin-top: 15px;">Storia, Nobiltà e Paesaggi della Costa degli Dei</p>
             <p class="subtitle" style="margin: 30px 0 0 0; font-size: 1.1em;"><a href="index.html" style="color:#4a9d5f; text-decoration:none; font-weight:600; border: 1px solid #4a9d5f; padding: 10px 20px; border-radius: 30px; transition: 0.3s;"><i class="fa-solid fa-arrow-left"></i> Torna alla Home</a></p>
         </div>
      </div>
    </header>

    <main class="article-container fade-in-up reveal-visible" style="max-width: 900px; margin: 0 auto; padding: 60px 40px; background: #fff; box-shadow: 0 0 40px rgba(0,0,0,0.03); border-radius: 16px; margin-top: -50px; position: relative; z-index: 10; font-family: 'Lato', sans-serif;">
        <article class="blog-article">
            
            <p style="font-size:1.3em; line-height: 1.8; color: #444; text-align: justify; margin-bottom: 40px;">
                La <strong style="color: #4a9d5f;">famiglia Toraldo</strong> rappresenta una delle più antiche, venerabili e influenti casate aristocratiche dell'intero <em>Regno di Napoli</em>. Con origini che si perdono nelle nebbie delle dinastie germaniche medievali, le prime testimonianze li vedono giungere in Italia al prestigioso seguito dell'<strong>Imperatore Federico II di Svevia</strong>. Scesi nella penisola con compiti militari ed amministrativi, si ritagliarono un ruolo centrale nel governo delle province meridionali.
            </p>

            <img src="https://images.unsplash.com/photo-1599839619722-39751411ea63?q=80&w=1200" alt="Scorci Antichi" style="width: 100%; border-radius: 12px; box-shadow: 0 10px 20px rgba(0,0,0,0.1); margin-bottom: 40px; border: 1px solid #eee;">
            
            <p style="font-size:1.15em; line-height: 1.8; color: #555; text-align: justify; margin-bottom:50px;">
                Intorno alla fine del XV secolo, un importante ramo della casata trovò la sua culla eletta lungo il versante tirrenico della Calabria. Vennero ufficialmente ascritti al ristrettissimo ed esclusivo **patriziato della città di Tropea** sin dal dal lontano 1508. Da quel momento, le sorti storiche e architettoniche del comprensorio s'intrecciarono indissolubilmente con il loro stemma: l'iconico scudetto fogliato verde caricato dal leone rampante. La famiglia non si limitò all'amministrazione, ma produsse intellettuali, ecclesiastici, e noti militari. 
            </p>
            
            <hr style="border: 0; border-top: 1px solid #eaeaea; margin: 60px auto; width: 30%;">

            <h2 class="property-title" style="font-size: 2.2em; text-align:center; margin-bottom: 40px; color: #333;" data-i18n="blog_toraldo_h1">Il Palazzo Toraldo e l'Archivio Storico in Tropea</h2>

            <p style="font-size: 1.15em; line-height: 1.8; color: #555; text-align: justify; margin-bottom: 30px;">
                Passeggiando lungo le intricate viuzze basolate del cuore antico di Tropea, ci si imbatte quasi d'improvviso nella sontuosità austera ma elegante del <strong>Palazzo Toraldo</strong> (anticamente d'Aquino-Toraldo). Costruito sull'impronta di antichi manieri difensivi aragonesi e impreziosito nei secoli successivi con lussuosi cortili, loggiati e stemmi gentilizi incisi nella pietra, divenne la dimora fissa e il simbolo del potere locale della famiglia.
            </p>

            <img src="https://images.unsplash.com/photo-1555020108-7a5611dd1fc3?q=80&w=1200" alt="Centro Storico" style="width: 100%; border-radius: 12px; box-shadow: 0 10px 20px rgba(0,0,0,0.1); margin-bottom: 40px; border: 1px solid #eee;">

            <p style="font-size: 1.15em; line-height: 1.8; color: #555; text-align: justify; margin-bottom: 80px;">
                Ancora oggi, il prestigio dell'edificio si irradia culturalmente su tutto il territorio grazie al tesoro in esso custodito: l'<em>Archivio Storico privato dei Toraldo</em>. Dichiarato bene di eccezionale interesse da parte dello Stato italiano, tramanda ai posteri un'infinita collezione di pergamene pontificie, registri notarili, atti imperiali e manoscritti diplomatici, il cui nucleo più antico risale direttamente al <strong>XII secolo</strong>. All'interno del palazzo si apprezza inoltre una collezione insostituibile di reperti archeologici e un'antichissima raccolta di epigrafi romane e cristiane rinvenute lungo il litorale. A riprova dell'impatto dei Toraldo sulla sociologia tropeana, anche il principale liceo statale porta fieramente il loro nome.
            </p>

            <hr style="border: 0; border-top: 1px solid #eaeaea; margin: 60px auto; width: 30%;">
            
            <h2 class="property-title" style="font-size: 2.2em; text-align:center; margin-bottom: 40px; color: #333;" data-i18n="blog_toraldo_h2">Santa Domenica di Ricadi, Viti, Aranci e Terre Marine</h2>

            <div style="display: flex; flex-wrap: wrap; align-items: start; gap: 40px; margin-bottom: 80px;">
                <div style="flex: 1; min-width: 300px;">
                    <p style="font-size: 1.15em; line-height: 1.8; color: #555; text-align: justify;">
                        Tuttavia, il polmone economico ed agricolo su cui si reggeva l'influenza tropeana della casata batteva forte nei latifondi circostanti. Prima ancora dello sviluppo del turismo balneare di massa ai giorni nostri, le distese collinari digradanti verso il blu cobalto della <em>Costa degli Dei</em> erano la cassaforte produttiva locale. 
                    </p>
                    <p style="font-size: 1.15em; line-height: 1.8; color: #555; text-align: justify; margin-top: 20px;">
                        Le sterminate proprietà del casato abbracciavano quasi integralmente i terreni che oggi costituiscono <strong>Santa Domenica di Ricadi</strong> e le sue contrade marinare limitrofe. Furono proprio i nobili Toraldo a spingere sull'innovazione organica dei campi, commissionando i curatissimi muretti a secco (le "Armacere") utili per i terrazzamenti vista mare. Quelle terre, arse dal sole ma dolci, regalavano agrumeti lussureggianti (tra limoni e bergamotti inebrianti), mandorli generosi, immensi vigneti da cui si pestava un vino corposo e distese di cipolle rosse la cui genetica andava formandosi nei secoli in modo del tutto naturale. Una fertilità che permise l'edificazione di antiche dimore padronali e masserie che oggi punteggiano discretamente il paesaggio costiero.
                    </p>
                </div>
                <div style="flex: 1; min-width: 300px;">
                    <img src="https://images.unsplash.com/photo-1543781295-8ee7741f0bba?q=80&w=1200" alt="Terreni Santa Domenica" style="width: 100%; border-radius: 12px; box-shadow: 0 10px 20px rgba(0,0,0,0.1); border: 1px solid #eee;">
                    <p style="text-align: center; font-size: 0.9em; color: #999; margin-top: 10px;"><em>Antichi terrazzamenti e alberi da frutto</em></p>
                </div>
            </div>

            <hr style="border: 0; border-top: 1px solid #eaeaea; margin: 60px auto; width: 30%;">

            <h2 class="property-title" style="font-size: 2.2em; text-align:center; margin-bottom: 40px; color: #333;" data-i18n="blog_toraldo_h3">Il romantico ritiro del Castello Galluppi-Toraldo</h2>

            <img src="https://images.unsplash.com/photo-1533154823295-8d54c86e00ea?q=80&w=1200" alt="Castello Caria" style="width: 100%; border-radius: 12px; box-shadow: 0 10px 20px rgba(0,0,0,0.1); margin-bottom: 40px; border: 1px solid #eee;">

            <p style="font-size: 1.15em; line-height: 1.8; color: #555; text-align: justify; margin-bottom: 40px;">
                Mentre l'inverno scorreva tra le mura del palazzo urbano ed i contadini badavano alla potatura a valle, l'avvento della canicola estiva spingeva la famiglia verso le colline interne. Situato a nord di Tropea salendo sul crinale, l'abitato di <strong>Caria (una frazione collinare di Drapia)</strong> offriva refrigerio e ritmi più pacati. 
            </p>
            <p style="font-size: 1.15em; line-height: 1.8; color: #555; text-align: justify; margin-bottom: 50px;">
                Qui, circondato dai boschi di faggi e ulivi, la famiglia si rigenerava all'interno dello scenografico <em>Castello Galluppi-Toraldo</em>. Nata prettamente come sfarzosa residenza estiva che come opera fortificata bellicosa, sebbene dotata della tipica estetica austera del mastio padronale calabrese, fu negli anni cornice di ritiri umanistici, convegni storici in giardino, simposi serali illuminati a fiamma e cenacoli culturali dedicati a poeti ed accademici dell'Ottocento. I Toraldo amavano accogliere illustri esponenti del sud in questo rifugio spirituale e culturale. Ad oggi la struttura versa in un profondo bisogno di restauro tutelativo, acquisita dalle autorità comunali, nel vivo tentativo di non disperdere la preziosissima essenza e testimonianza architettonica di un'antica armonia feudale perduta.
            </p>
            
        </article>
    </main>

    <section class="contact-section" style="margin-top: 50px; background: transparent; padding: 60px 0; text-align: center;">
        <div class="container">
            <h3 class="property-title" style="font-size: 1.8em; margin-bottom:30px; color: #333;">Pronto per l'esperienza?</h3>
            <p style="max-width: 600px; margin: 0 auto 30px auto; color: #555;">La Costa degli Dei aspetta di essere vissuta tra le medesime insenature e scorci panoramici che secoli fa conquistarono i nobili Toraldo.</p>
            <a href="index.html" class="submit-btn" style="text-decoration:none; display:inline-block; max-width:300px; padding: 15px 40px;">Ritorna alla Home</a>
        </div>
    </section>

    <!-- Footer base -->
    <footer style="background-color: #2b3034; color: #fff; padding: 40px 0; text-align: center; font-family: 'Poppins', sans-serif;">
        <p style="margin:0; font-size: 0.9em; color: #bbb;">&copy; 2024 Villa del Conte. Tutti i diritti riservati.</p>
    </footer>

    <script src="translations.js"></script>
    <script src="script.js"></script>
</body>
</html>"""

with open("blog-toraldo.html", "w", encoding="utf-8") as f:
    f.write(blog_html)

print("Card styled as entity. Article aggressively expanded.")
