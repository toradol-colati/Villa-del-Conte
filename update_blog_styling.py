with open("style.css", "r", encoding="utf-8") as f:
    content = f.read()

# Fix the blog-grid
old_blog_grid = """/* Blog Section */
.blog-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 30px;
  margin-top: 40px;
}"""
new_blog_grid = """/* Blog Section */
.blog-grid {
  display: flex;
  justify-content: center;
  flex-wrap: wrap;
  gap: 30px;
  margin-top: 40px;
}
.blog-card {
  max-width: 400px;
  width: 100%;
}
"""
content = content.replace(old_blog_grid, new_blog_grid)

old_card = """.blog-card {
  background: #fff;"""
new_card = """.blog-card {
  background: #fff;"""
content = content.replace(old_card, new_card) # this is a no-op just validating I can overwrite if I wanted

with open("style.css", "w", encoding="utf-8") as f:
    f.write(content)

# Now rewrite blog-toraldo.html to be visually stunning
blog_html = """<!DOCTYPE html>
<html lang="it">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>I Toraldo a Tropea | Villa del Conte</title>
    <meta name="description" content="Scopri la storia della nobile famiglia Toraldo, il loro castello a Caria e le loro terre a Santa Domenica di Ricadi.">
    
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

    <div class="lang-selector-fixed fade-in-up reveal-visible">
        <select id="lang-switch" class="lang-select" aria-label="Seleziona la lingua">
            <option value="it">🇮🇹 IT</option>
            <option value="en">🇬🇧 EN</option>
            <option value="es">🇪🇸 ES</option>
            <option value="ru">🇷🇺 RU</option>
            <option value="de">🇩🇪 DE</option>
            <option value="zh">🇨🇳 ZH</option>
        </select>
    </div>

    <!-- Article Header -->
    <header class="blog-header" style="background-image: linear-gradient(to bottom, rgba(0, 0, 0, 0.4) 10%, rgba(253, 251, 247, 1) 100%), url('https://upload.wikimedia.org/wikipedia/commons/thumb/8/8f/Tropea2.jpg/960px-Tropea2.jpg'); background-size: cover; background-position: center; padding: 250px 0 100px 0; position: relative;">
      <div class="container" style="text-align: center;">
         <div class="logo-section" style="background: rgba(255,255,255,0.9); padding: 40px; border-radius: 12px; display: inline-block; box-shadow: 0 10px 30px rgba(0,0,0,0.1);">
             <div class="logo">
                <img src="http://www.nobili-napoletani.it/images/foto/T/Toraldo/Tropea,%20stemma%20Toraldo.png" alt="Stemma Toraldo" class="logo-image" style="max-width: 120px; margin: 0 auto 20px auto;">
             </div>
             <h1 class="site-title" style="font-size: 3em; margin: 0; color: #333;" data-i18n="blog_toraldo_title">I Toraldo a Tropea</h1>
             <p class="subtitle" style="margin: 20px 0 0 0; font-size: 1.1em;"><a href="index.html" style="color:#4a9d5f; text-decoration:none; font-weight:600;"><i class="fa-solid fa-arrow-left"></i> Torna alla Home</a></p>
         </div>
      </div>
    </header>

    <main class="article-container fade-in-up reveal-visible" style="max-width: 900px; margin: 0 auto; padding: 40px 20px; background: #fff; box-shadow: 0 0 40px rgba(0,0,0,0.03); border-radius: 16px; margin-top: -50px; position: relative; z-index: 10;">
        <article class="blog-article">
            
            <p class="property-description" style="font-size:1.3em; line-height: 1.8; color: #555; text-align: center; margin-bottom:50px; font-style: italic;" data-i18n="blog_toraldo_p1">La famiglia Toraldo è una delle più antiche e nobili casate del Regno di Napoli. Di origine germanica, la famiglia giunse in Italia al seguito dell'imperatore Federico II di Svevia e si stabilì in Calabria, venendo ascritta al patriziato di Tropea fin dal 1508.</p>
            
            <hr style="border: 0; border-top: 1px solid #eaeaea; margin: 40px auto; width: 50%;">

            <div style="display: flex; flex-wrap: wrap; align-items: center; gap: 40px; margin-top: 50px;">
                <div style="flex: 1; min-width: 300px;">
                    <h2 class="property-title" style="font-size: 2.2em; text-align:left; margin-top:0;" data-i18n="blog_toraldo_h1">Il Palazzo Toraldo e l'Archivio Storico</h2>
                    <p class="property-description" style="font-size: 1.15em; line-height: 1.8;" data-i18n="blog_toraldo_p2">Situato nel cuore del centro storico di Tropea, il maestoso Palazzo Toraldo ospita l'inestimabile archivio privato della famiglia, riconosciuto di grandissimo interesse storico, che conta pergamene risalenti dal XII al XVI secolo. Anche la scuola cittadina porta oggi il nome 'Toraldo'.</p>
                </div>
                <div style="flex: 1; min-width: 300px;">
                    <img src="https://images.unsplash.com/photo-1549884587-81765c9b7405?q=80&w=1200" alt="Palazzo Antico" style="width: 100%; border-radius: 12px; box-shadow: 0 10px 20px rgba(0,0,0,0.1);">
                </div>
            </div>
            
            <div style="display: flex; flex-wrap: wrap; flex-direction: row-reverse; align-items: center; gap: 40px; margin-top: 80px;">
                <div style="flex: 1; min-width: 300px;">
                    <h2 class="property-title" style="font-size: 2.2em; text-align:left; margin-top:0;" data-i18n="blog_toraldo_h2">Santa Domenica di Ricadi e le Terre di Famiglia</h2>
                    <p class="property-description" style="font-size: 1.15em; line-height: 1.8;" data-i18n="blog_toraldo_p3">La presenza dei Toraldo non si limitava al centro di Tropea. Le vastissime proprietà terriere includevano gran parte di Santa Domenica di Ricadi, dove i campi testimoniano l'importanza agricola ed economica della famiglia in tutta la Costa degli Dei.</p>
                </div>
                <div style="flex: 1; min-width: 300px;">
                    <img src="https://images.unsplash.com/photo-1502521995894-ae042e61917b?q=80&w=1200" alt="Campagne Ricadi" style="width: 100%; border-radius: 12px; box-shadow: 0 10px 20px rgba(0,0,0,0.1);">
                </div>
            </div>
            
            <div style="display: flex; flex-wrap: wrap; align-items: center; gap: 40px; margin-top: 80px; margin-bottom: 50px;">
                <div style="flex: 1; min-width: 300px;">
                    <h2 class="property-title" style="font-size: 2.2em; text-align:left; margin-top:0;" data-i18n="blog_toraldo_h3">Il Castello Galluppi-Toraldo a Caria</h2>
                    <p class="property-description" style="font-size: 1.15em; line-height: 1.8;" data-i18n="blog_toraldo_p4">A Caria di Drapia sorge l'affascinante Castello Galluppi-Toraldo. Un tempo residenza estiva della famiglia e salotto culturale di illustri intellettuali, la villa-castello è un esempio magnifico dell'architettura aristocratica calabrese dell'Ottocento.</p>
                </div>
                <div style="flex: 1; min-width: 300px;">
                    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/Castello_Normanno-Svevo_Vibo_Valentia_12.jpg/800px-Castello_Normanno-Svevo_Vibo_Valentia_12.jpg" alt="Castello" style="width: 100%; border-radius: 12px; box-shadow: 0 10px 20px rgba(0,0,0,0.1);">
                </div>
            </div>
            
        </article>
    </main>

    <section class="contact-section" style="margin-top: 50px; background: #fff; padding: 60px 0; text-align: center; border-top: 1px solid #eaeaea;">
        <div class="container">
            <h3 class="property-title" style="font-size: 1.8em; margin-bottom:30px;">Pronto per il tuo soggiorno?</h3>
            <a href="index.html" class="submit-btn" style="text-decoration:none; display:inline-block; max-width:300px;">Esplora le Strutture</a>
        </div>
    </section>

    <script src="translations.js"></script>
    <script src="script.js"></script>
</body>
</html>"""

with open("blog-toraldo.html", "w", encoding="utf-8") as f:
    f.write(blog_html)

print("Updated stylings and blog layout!")
