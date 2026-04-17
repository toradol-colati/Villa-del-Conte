import re
import os

blog_file = "/Users/umbertotoraldo/Downloads/Blog Villa del Conte.md"
with open(blog_file, 'r', encoding='utf-8') as f:
    content = f.read()

sections = re.split(r'\n# \*\*', '\n' + content)
articles = []
for sec in sections:
    if not sec.strip():
        continue
    parts = sec.split('**\n', 1)
    if len(parts) == 2:
        title = parts[0].strip()
        body = parts[1].strip()
        
        # RIMUOVE GLI ASTERISCHI (hashtags visivi) E I VERI HASHTAG
        body = body.replace('**', '')
        body = body.replace('#', '')
        
        # Rimuove segnaposto di immagini
        body = re.sub(r'!\[\]\[image\d+\]', '', body)
        body = re.sub(r'\[image\d+\]:.*', '', body)
        
        paragraphs = [p.strip() for p in body.split('\n\n') if p.strip()]
        articles.append({"title": title, "paragraphs": paragraphs})

mapping = [
    {"title": "Storia del Territorio", "slug": "territorio"},
    {"title": "Origini Romane", "slug": "romane"},
    {"title": "Toraldo e Federico II", "slug": "toraldo"},
    {"title": "La Costa degli Dei", "slug": "costa"},
    {"title": "Tropea: Il Borgo dei Borghi", "slug": "tropea"},
    {"title": "Santa Domenica di Ricadi", "slug": "santadomenica"},
    {"title": "Tradizioni Culinarie e Prodotti Tipici", "slug": "cucina"},
]

template = """<!DOCTYPE html>
<html lang="it">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} | Villa del Conte</title>
    <meta name="description" content="{desc}">
    <link rel="icon" type="image/png" href="images/ui/logo.png">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300..700;1,300..700&family=Lato:ital,wght@0,100;0,300;0,400;0,700;0,900;1,100;1,300;1,400;1,700;1,900&family=Poppins:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="style.css?v=5">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.2/css/all.min.css">
    <style>
        .blog-section-image {{ width: 100%; border-radius: 4px; border: 1px solid #dee2e6; box-shadow: 0 4px 15px rgba(0,0,0,0.05); }}
        .text-column p {{ margin-bottom: 25px; text-align: justify; font-family: 'Lato', sans-serif; font-size: 1.15em; line-height: 1.8; color: #555; }}
        .editorial-row {{ display: flex; flex-wrap: wrap; gap: 50px; align-items: start; margin-bottom: 40px; }}
        .text-column {{ flex: 1; min-width: 300px; }}
        .image-column {{ flex: 1; min-width: 300px; }}
    </style>
</head>
<body style="background-color: #fdfbf7; margin: 0; padding: 0;">

    <a href="index.html" id="sticky-logo" style="position: absolute; top: 20px; left: 20px; z-index:1000;">
        <img src="images/ui/logo.png" alt="Logo Villa del Conte" style="width: 60px;">
    </a>

    <header style="background-image: linear-gradient(to bottom, rgba(0, 0, 0, 0.4) 0%, rgba(0, 0, 0, 0.7) 100%), url('{img_url}'); background-size: cover; background-position: center center; padding: 180px 20px 100px 20px; text-align: center; color: white;">
        <div style="max-width: 800px; margin: 0 auto;">
             <h1 style="font-family: 'Cormorant Garamond', serif; font-size: 4em; margin: 0; text-shadow: 0 2px 4px rgba(0,0,0,0.8);">{title}</h1>
             <p style="font-family: 'Lato', sans-serif; font-size: 1.4em; letter-spacing: 1px; text-transform: uppercase; margin-top: 20px; opacity: 0.9;">Villa del Conte | Costa degli Dei</p>
        </div>
    </header>

    <main class="fade-in-up" style="max-width: 1000px; margin: -50px auto 100px auto; background: #fff; padding: 80px 60px; box-shadow: 0 20px 50px rgba(0,0,0,0.08); border-radius: 8px; position: relative;">
        
        {body_html}

    </main>

    <div style="text-align: center; margin-bottom: 80px;">
        <a href="index.html" class="submit-btn" style="text-decoration:none; display:inline-block; padding: 15px 40px; font-family: 'Poppins', sans-serif; background-color: #4a9d5f; color: white; border-radius: 6px; font-size: 1.1em; font-weight: 600; transition: transform 0.2s;">
            <i class="fa-solid fa-arrow-left"></i> Torna alla Struttura
        </a>
    </div>

    <footer style="background-color: #2b3034; color: #fff; padding: 40px 0; text-align: center; font-family: 'Poppins', sans-serif;">
        <p style="margin:0; font-size: 0.9em; color: #bbb;">&copy; 2024 Villa del Conte. Tutti i diritti riservati.</p>
    </footer>

    <script src="translations.js"></script>
    <script src="script.js?v=5"></script>
</body>
</html>"""

for i, m in enumerate(mapping):
    art = None
    for a in articles:
        if m['title'].lower() in a['title'].lower():
            art = a
            break
    if not art and i < len(articles):
        art = articles[i]
    
    if art:
        pars = art['paragraphs']
        intro = pars[0] if pars else ""
        
        img_url = f"images/blog/{m['slug']}.jpg"
        if not os.path.exists(img_url) or os.path.getsize(img_url) < 10000: # if it's 429 HTML it's small!
            img_url = "images/villa/giardino/26EA642B-36BE-4AB2-995D-C0369173014E_4_5005_c.jpeg"

        inner_img_str = f"images/blog/{m['slug']}_inner.jpg"
        if not os.path.exists(inner_img_str) or os.path.getsize(inner_img_str) < 10000:
            inner_img_str = img_url # Fallback to the header image
        
        body_html = ""
        for idx, p in enumerate(pars):
            if idx == 1:
                body_html += f"""
        <div class="editorial-row">
            <div class="text-column">
                <p>{p}</p>
            </div>
            <div class="image-column">
                <img src="{inner_img_str}" alt="{m['title']}" class="blog-section-image">
            </div>
        </div>
                """
            else:
                body_html += f"""
        <div class="text-column">
            <p>{p}</p>
        </div>"""
        
        html = template.format(
            title=art['title'],
            desc=intro[:150].replace('"', "'") + "...",
            img_url=img_url,
            body_html=body_html
        )
        
        with open(f"blog-{m['slug']}.html", "w", encoding='utf-8') as outf:
            outf.write(html)

print("Generated PERFECTED HTML pages with fixed fallbacks and sizes.")
