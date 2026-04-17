import re

script_path = '/Users/umbertotoraldo/petra-protocol/Villa-del-Conte/script.js'

with open(script_path, 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Update initializeCarousel to remove buttons and add overlay label
init_func_pattern = r'function initializeCarousel.*?updateImage\(\);\n\s*\}'

new_init_func = """function initializeCarousel(galleryId, catsId, propertyKey) {
        const gallery = document.getElementById(galleryId);
        const catsContainer = document.getElementById(catsId);
        if (!gallery || !galleryData[propertyKey]) return;

        // Hide the category container permanently
        if (catsContainer) catsContainer.style.display = 'none';

        const imageElement = gallery.querySelector('.property-image');
        const prevBtn = gallery.querySelector('.prev-btn');
        const nextBtn = gallery.querySelector('.next-btn');

        let currentIndex = 0;

        function updateImage() {
            const imgs = galleryData[propertyKey]['Tutte'];
            if (imgs && imgs.length > 0) {
                imageElement.src = imgs[currentIndex];
                
                let label = gallery.querySelector('.carousel-label');
                if (!label) {
                    label = document.createElement('div');
                    label.className = 'carousel-label fade-in';
                    const imgContainer = imageElement.parentElement;
                    imgContainer.style.position = 'relative'; 
                    imgContainer.appendChild(label);
                }
                
                const parts = imgs[currentIndex].split('/');
                let catText = parts.length > 2 ? parts[2] : "";
                
                catText = catText.replace('salone&cucina', 'Salotto / Cucina')
                                 .replace('giardino', 'Piscina & Giardino')
                                 .replace('esterno', 'Esterno')
                                 .replace('bagno', 'Bagno')
                                 .replace('stanza ', 'Stanza ')
                                 .replace('stanza', 'Stanza');
                                 
                catText = catText.charAt(0).toUpperCase() + catText.slice(1);
                label.textContent = catText;
            }
        }

        nextBtn.addEventListener('click', () => {
            const len = galleryData[propertyKey]['Tutte'].length;
            currentIndex = (currentIndex + 1) % len;
            updateImage();
        });

        prevBtn.addEventListener('click', () => {
            const len = galleryData[propertyKey]['Tutte'].length;
            currentIndex = (currentIndex - 1 + len) % len;
            updateImage();
        });
        
        // Open lightbox bridging logic
        imageElement.addEventListener('click', function(e) {
            window.lbCurrentArray = galleryData[propertyKey]['Tutte'];
            window.lbCurrentIndex = currentIndex;
            window.openLightboxWithArray();
        });

        updateImage();
    }"""

text = re.sub(init_func_pattern, new_init_func, text, flags=re.DOTALL)


# 2. Update Lightbox Logic to allow array navigation
lightbox_pattern = r'// === LIGHTBOX LOGIC ===.*?\}\);\n\n\}\);'
new_lightbox = """// === LIGHTBOX LOGIC ===
    const lightbox = document.createElement('div');
    lightbox.id = 'lightbox';
    lightbox.className = 'lightbox';

    const closeBtn = document.createElement('span');
    closeBtn.className = 'lightbox-close';
    closeBtn.innerHTML = '&times;';

    const maxImg = document.createElement('img');
    maxImg.className = 'lightbox-content';
    maxImg.id = 'lightbox-img';
    
    const lbPrev = document.createElement('span');
    lbPrev.className = 'lightbox-nav lightbox-prev';
    lbPrev.innerHTML = '&#10094;';

    const lbNext = document.createElement('span');
    lbNext.className = 'lightbox-nav lightbox-next';
    lbNext.innerHTML = '&#10095;';

    lightbox.appendChild(closeBtn);
    lightbox.appendChild(lbPrev);
    lightbox.appendChild(lbNext);
    lightbox.appendChild(maxImg);
    document.body.appendChild(lightbox);
    
    window.lbCurrentArray = [];
    window.lbCurrentIndex = 0;

    window.openLightboxWithArray = function() {
        lightbox.style.display = 'flex';
        setTimeout(() => lightbox.classList.add('show'), 10);
        maxImg.src = window.lbCurrentArray[window.lbCurrentIndex];
        document.body.style.overflow = 'hidden';
    };

    function updateLightboxImg() {
        if(window.lbCurrentArray && window.lbCurrentArray.length > 0) {
            maxImg.src = window.lbCurrentArray[window.lbCurrentIndex];
        }
    }

    lbPrev.addEventListener('click', (e) => {
        e.stopPropagation();
        window.lbCurrentIndex = (window.lbCurrentIndex - 1 + window.lbCurrentArray.length) % window.lbCurrentArray.length;
        updateLightboxImg();
    });

    lbNext.addEventListener('click', (e) => {
        e.stopPropagation();
        window.lbCurrentIndex = (window.lbCurrentIndex + 1) % window.lbCurrentArray.length;
        updateLightboxImg();
    });

    function closeLightbox() {
        lightbox.classList.remove('show');
        setTimeout(() => {
            lightbox.style.display = 'none';
            document.body.style.overflow = 'auto';
        }, 300);
    }

    closeBtn.addEventListener('click', closeLightbox);
    
    // Support left/right arrow keys
    document.addEventListener('keydown', (e) => {
        if(lightbox.classList.contains('show')) {
            if(e.key === 'ArrowLeft') lbPrev.click();
            if(e.key === 'ArrowRight') lbNext.click();
            if(e.key === 'Escape') closeLightbox();
        }
    });

    lightbox.addEventListener('click', function (e) {
        if (e.target === lightbox) {
            closeLightbox();
        }
    });

});"""

text = re.sub(lightbox_pattern, new_lightbox, text, flags=re.DOTALL)

with open(script_path, 'w', encoding='utf-8') as f:
    f.write(text)


# 3. Add CSS classes to style.css
css_append = """
/* === NEW CAROUSEL & LIGHTBOX CONTROLS === */
.carousel-label {
    position: absolute;
    bottom: 20px;
    right: 20px;
    background: rgba(43, 48, 52, 0.7);
    backdrop-filter: blur(4px);
    color: white;
    padding: 6px 16px;
    border-radius: 30px;
    font-size: 0.9rem;
    font-weight: 500;
    font-family: 'Poppins', sans-serif;
    pointer-events: none;
    letter-spacing: 0.5px;
    box-shadow: 0 4px 10px rgba(0,0,0,0.2);
    border: 1px solid rgba(255,255,255,0.1);
}

.lightbox-nav {
    position: absolute;
    top: 50%;
    transform: translateY(-50%);
    color: rgba(255,255,255,0.7);
    font-size: 3rem;
    cursor: pointer;
    padding: 30px 20px;
    user-select: none;
    z-index: 10001;
    transition: all 0.3s ease;
}

.lightbox-nav:hover {
    color: #fff;
    transform: translateY(-50%) scale(1.1);
}

.lightbox-prev { left: 20px; }
.lightbox-next { right: 20px; }

@media (max-width: 768px) {
    .lightbox-nav { font-size: 2rem; padding: 15px 10px; }
    .lightbox-prev { left: 5px; }
    .lightbox-next { right: 5px; }
}
"""

with open('/Users/umbertotoraldo/petra-protocol/Villa-del-Conte/style.css', 'a', encoding='utf-8') as f:
    f.write(css_append)

# Cache-busting
index_path = '/Users/umbertotoraldo/petra-protocol/Villa-del-Conte/index.html'
with open(index_path, 'r', encoding='utf-8') as f:
    idx = f.read()
idx = idx.replace('script.js?v=10', 'script.js?v=11')
idx = idx.replace('style.css?v=10', 'style.css?v=11')
with open(index_path, 'w', encoding='utf-8') as f:
    f.write(idx)

print("Advanced Carousel + Lightbox features successfully applied!")
