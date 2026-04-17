import os

css_append = """
/* === LIGHTBOX MODAL === */
.lightbox {
    display: none; 
    position: fixed; 
    z-index: 9999; 
    left: 0; 
    top: 0; 
    width: 100%; 
    height: 100%; 
    background-color: rgba(0,0,0,0.9);
    backdrop-filter: blur(5px);
    opacity: 0;
    transition: opacity 0.3s ease;
}

.lightbox.show {
    display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: column;
    opacity: 1;
}

.lightbox-content {
    max-width: 90%;
    max-height: 90vh;
    object-fit: contain;
    border-radius: 8px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.5);
    transform: scale(0.9);
    transition: transform 0.3s ease;
}

.lightbox.show .lightbox-content {
    transform: scale(1);
}

.lightbox-close {
    position: absolute;
    top: 20px;
    right: 35px;
    color: #f1f1f1;
    font-size: 40px;
    font-weight: bold;
    cursor: pointer;
    transition: 0.3s;
    z-index: 10000;
}

.lightbox-close:hover,
.lightbox-close:focus {
    color: #bbb;
    text-decoration: none;
    cursor: pointer;
}

.property-image {
    cursor: zoom-in;
    transition: transform 0.3s ease;
}
.property-image:hover {
    transform: scale(1.02);
}
"""

with open('/Users/umbertotoraldo/petra-protocol/Villa-del-Conte/style.css', 'a', encoding='utf-8') as f:
    f.write(css_append)

js_append = """
    // === LIGHTBOX LOGIC ===
    const lightbox = document.createElement('div');
    lightbox.id = 'lightbox';
    lightbox.className = 'lightbox';
    
    const closeBtn = document.createElement('span');
    closeBtn.className = 'lightbox-close';
    closeBtn.innerHTML = '&times;';
    
    const maxImg = document.createElement('img');
    maxImg.className = 'lightbox-content';
    maxImg.id = 'lightbox-img';
    
    lightbox.appendChild(closeBtn);
    lightbox.appendChild(maxImg);
    document.body.appendChild(lightbox);
    
    const lbImages = document.querySelectorAll('.property-image');
    lbImages.forEach(img => {
        img.addEventListener('click', function(){
            lightbox.classList.add('show');
            maxImg.src = this.src;
            document.body.style.overflow = 'hidden';
        });
    });
    
    function closeLightbox() {
        lightbox.classList.remove('show');
        setTimeout(() => {
            lightbox.style.display = 'none';
            document.body.style.overflow = 'auto';
        }, 300); // match transition
    }

    // Fix display block issue by overriding default hide gracefully
    lbImages.forEach(img => {
        img.addEventListener('click', function(){
            lightbox.style.display = 'flex';
            setTimeout(() => lightbox.classList.add('show'), 10);
            maxImg.src = this.src;
            document.body.style.overflow = 'hidden';
        });
    });
    
    closeBtn.addEventListener('click', closeLightbox);
    
    lightbox.addEventListener('click', function(e) {
        if(e.target === lightbox) {
            closeLightbox();
        }
    });
"""

import re
script_path = '/Users/umbertotoraldo/petra-protocol/Villa-del-Conte/script.js'
with open(script_path, 'r', encoding='utf-8') as f:
    text = f.read()

# Append to DOMContentLoaded
text = text.replace('}); // Chiude il domcontentloaded', js_append + '\n}); // Chiude il domcontentloaded')

# Se il replace ha fallito (per formattazione diversa), provo a inserirlo alla fine, prima dell'ultima }
if "LIGHTBOX LOGIC" not in text:
    parts = text.rsplit('});', 1)
    if len(parts) == 2:
        text = parts[0] + js_append + "\n});"

with open(script_path, 'w', encoding='utf-8') as f:
    f.write(text)

# Cache-busting index.html
with open('/Users/umbertotoraldo/petra-protocol/Villa-del-Conte/index.html', 'r', encoding='utf-8') as f:
    index = f.read()
index = index.replace('style.css?v=5', 'style.css?v=6')
index = index.replace('script.js?v=5', 'script.js?v=6')
with open('/Users/umbertotoraldo/petra-protocol/Villa-del-Conte/index.html', 'w', encoding='utf-8') as f:
    f.write(index)

print("Lightbox CSS and JS injected successfully!")
