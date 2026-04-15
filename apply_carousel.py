import re
import os
import json

def get_images(base_dir):
    result = {}
    if not os.path.exists(base_dir): return result
    for root, dirs, files in os.walk(base_dir):
        category = os.path.basename(root)
        if category == os.path.basename(base_dir): continue
        imgs = [f for f in files if f.lower().endswith(('.jpg', '.jpeg', '.png', '.webp'))]
        if imgs:
            result[category] = [os.path.join(root, img).replace('/Users/umbertotoraldo/petra-protocol/Villa-del-Conte/', '') for img in sorted(imgs)]
    
    all_imgs = []
    cats = sorted(list(result.keys()))
    if 'esterno' in cats: cats.remove('esterno'); cats.insert(0, 'esterno')
    if 'giardino' in cats: cats.remove('giardino'); cats.insert(0, 'giardino')
    if 'salone&cucina' in cats: cats.remove('salone&cucina'); cats.insert(1, 'salone&cucina')
    for c in cats:
        all_imgs.extend(result[c])
    result['Tutte'] = all_imgs
    return result

data = {'villa': get_images('images/villa'), 'conte': get_images('images/house')}

with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

new_css = """
/* Carousel Categories */
.carousel-categories {
    display: flex;
    gap: 10px;
    margin-top: 15px;
    overflow-x: auto;
    padding-bottom: 5px;
    scrollbar-width: thin;
}
.carousel-categories::-webkit-scrollbar { height: 6px; }
.carousel-categories::-webkit-scrollbar-thumb { background-color: #ccc; border-radius: 10px; }
.carousel-cat-btn {
    background: #f0f0f0;
    border: none;
    border-radius: 20px;
    padding: 6px 15px;
    font-size: 0.85em;
    font-weight: 500;
    color: #555;
    cursor: pointer;
    white-space: nowrap;
    transition: all 0.3s ease;
    font-family: 'Poppins', sans-serif;
}
.carousel-cat-btn:hover { background: #e0e0e0; }
.carousel-cat-btn.active { background: #4a9d5f; color: white; }
"""
if "carousel-categories" not in css:
    with open('style.css', 'w', encoding='utf-8') as f:
        f.write(css + new_css)

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

html = re.sub(r'(<div class="image-gallery" id="gallery-villa">.*?</div>)', r'\1\n                                    <div class="carousel-categories" id="cats-villa"></div>', html, flags=re.DOTALL)
html = re.sub(r'(<div class="image-gallery" id="gallery-conte">.*?</div>)', r'\1\n                                    <div class="carousel-categories" id="cats-conte"></div>', html, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

with open('script.js', 'r', encoding='utf-8') as f:
    js = f.read()

js_replacement = """
    // === CAROUSEL LOGIC ===
    const galleryData = __INSERT_JSON_DATA__;

    function initializeCarousel(galleryId, catsId, propertyKey) {
      const gallery = document.getElementById(galleryId);
      const catsContainer = document.getElementById(catsId);
      if (!gallery || !galleryData[propertyKey]) return;
      
      const imageElement = gallery.querySelector('.property-image');
      const prevBtn = gallery.querySelector('.prev-btn');
      const nextBtn = gallery.querySelector('.next-btn');
      
      let currentCategory = 'Tutte';
      let currentIndex = 0;
      
      function updateImage() { 
          const imgs = galleryData[propertyKey][currentCategory];
          if(imgs && imgs.length > 0) {
              imageElement.src = imgs[currentIndex]; 
          }
      }
      
      nextBtn.addEventListener('click', () => { 
          const len = galleryData[propertyKey][currentCategory].length;
          currentIndex = (currentIndex + 1) % len; 
          updateImage(); 
      });
      
      prevBtn.addEventListener('click', () => { 
          const len = galleryData[propertyKey][currentCategory].length;
          currentIndex = (currentIndex - 1 + len) % len; 
          updateImage(); 
      });
      
      if (catsContainer) {
          catsContainer.innerHTML = '';
          const catsObj = galleryData[propertyKey];
          const cats = ['Tutte', ...Object.keys(catsObj).filter(c => c !== 'Tutte')];
          
          cats.forEach(cat => {
              const btn = document.createElement('button');
              btn.className = 'carousel-cat-btn' + (cat === 'Tutte' ? ' active' : '');
              btn.textContent = cat;
              
              btn.addEventListener('click', () => {
                  catsContainer.querySelectorAll('.carousel-cat-btn').forEach(b => b.classList.remove('active'));
                  btn.classList.add('active');
                  
                  currentCategory = cat;
                  currentIndex = 0;
                  updateImage();
              });
              
              catsContainer.appendChild(btn);
          });
      }
      
      updateImage();
    }
    
    initializeCarousel('gallery-villa', 'cats-villa', 'villa');
    initializeCarousel('gallery-conte', 'cats-conte', 'conte');
"""
js_replacement = js_replacement.replace("__INSERT_JSON_DATA__", json.dumps(data, indent=4))

js = re.sub(r'// === CAROUSEL LOGIC ===.*?// === TABS NAVIGATION ===', js_replacement + "\n    // === TABS NAVIGATION ===", js, flags=re.DOTALL)

with open('script.js', 'w', encoding='utf-8') as f:
    f.write(js)

print("Carousels integrated successfully!")
