document.addEventListener('DOMContentLoaded', () => {

    // === CAROUSEL LOGIC ===
    // Helper: build image object from base path (produced by optimize_images.py)
    function img(base, alt) {
        return {
            webp: {
                "480":  base + "-480w.webp",
                "960":  base + "-960w.webp",
                "1600": base + "-1600w.webp"
            },
            fallback: base + ".jpg",
            alt: alt
        };
    }
    // Helper: images not yet through optimize_images.py (e.g. WhatsApp photos)
    function imgRaw(path, alt) {
        return { webp: {"480": path, "960": path, "1600": path}, fallback: path, alt: alt };
    }

    const galleryData = {
        "villa": {
            "giardino": [
                img("images/villa/giardino/giardino-01", "Giardino - La Villa"),
                img("images/villa/giardino/giardino-02", "Giardino - La Villa"),
                img("images/villa/giardino/giardino-03", "Giardino - La Villa"),
                img("images/villa/giardino/giardino-04", "Giardino - La Villa"),
                img("images/villa/giardino/giardino-05", "Giardino - La Villa"),
                img("images/villa/giardino/giardino-06", "Giardino - La Villa"),
                img("images/villa/giardino/giardino-07", "Giardino - La Villa"),
                img("images/villa/giardino/giardino-08", "Giardino - La Villa")
            ],
            "salone&cucina": [
                img("images/villa/salone&cucina/salone_cucina-01", "Salotto / Cucina - La Villa"),
                img("images/villa/salone&cucina/salone_cucina-02", "Salotto / Cucina - La Villa"),
                img("images/villa/salone&cucina/salone_cucina-03", "Salotto / Cucina - La Villa"),
                img("images/villa/salone&cucina/salone_cucina-04", "Salotto / Cucina - La Villa"),
                img("images/villa/salone&cucina/salone_cucina-05", "Salotto / Cucina - La Villa")
            ],
            "stanza 1": [
                img("images/villa/stanza 1/stanza 1-01", "Stanza 1 - La Villa"),
                img("images/villa/stanza 1/stanza 1-02", "Stanza 1 - La Villa"),
                img("images/villa/stanza 1/stanza 1-03", "Stanza 1 - La Villa"),
                img("images/villa/stanza 1/stanza 1-04", "Stanza 1 - La Villa"),
                img("images/villa/stanza 1/stanza 1-05", "Stanza 1 - La Villa")
            ],
            "stanza 2": [
                img("images/villa/stanza 2/stanza 2-01", "Stanza 2 - La Villa"),
                img("images/villa/stanza 2/stanza 2-02", "Stanza 2 - La Villa"),
                img("images/villa/stanza 2/stanza 2-03", "Stanza 2 - La Villa")
            ],
            "stanza 3": [
                img("images/villa/stanza 3/stanza 3-01", "Stanza 3 - La Villa"),
                img("images/villa/stanza 3/stanza 3-02", "Stanza 3 - La Villa")
            ],
            "bagno 1": [
                img("images/villa/bagno 1/bagno 1-01", "Bagno 1 - La Villa")
            ]
        },
        "conte": {
            "salone&cucina": [
                img("images/house/salone&cucina/salone_cucina-01", "Salotto / Cucina - La Conte House"),
                img("images/house/salone&cucina/salone_cucina-02", "Salotto / Cucina - La Conte House"),
                img("images/house/salone&cucina/salone_cucina-03", "Salotto / Cucina - La Conte House"),
                img("images/house/salone&cucina/salone_cucina-04", "Salotto / Cucina - La Conte House"),
                img("images/house/salone&cucina/salone_cucina-05", "Salotto / Cucina - La Conte House"),
                img("images/house/salone&cucina/salone_cucina-06", "Salotto / Cucina - La Conte House")
            ],
            "stanza": [
                img("images/house/stanza/stanza-01", "Stanza - La Conte House"),
                img("images/house/stanza/stanza-02", "Stanza - La Conte House"),
                img("images/house/stanza/stanza-03", "Stanza - La Conte House"),
                img("images/house/stanza/stanza-04", "Stanza - La Conte House"),
                img("images/house/stanza/stanza-05", "Stanza - La Conte House")
            ],
            "bagno": [
                img("images/house/bagno/bagno-01", "Bagno - La Conte House"),
                img("images/house/bagno/bagno-02", "Bagno - La Conte House"),
                img("images/house/bagno/bagno-03", "Bagno - La Conte House"),
                img("images/house/bagno/bagno-04", "Bagno - La Conte House"),
                // Foto WhatsApp non ancora ottimizzate — aggiungi dopo aver eseguito optimize_images.py
                imgRaw("images/house/bagno/WhatsApp Image 2026-04-15 at 22.10.13.jpeg", "Bagno - La Conte House"),
                imgRaw("images/house/bagno/WhatsApp Image 2026-04-15 at 22.10.39.jpeg", "Bagno - La Conte House"),
                imgRaw("images/house/bagno/WhatsApp Image 2026-04-15 at 22.10.49.jpeg", "Bagno - La Conte House")
            ],
            "esterno": [
                img("images/house/esterno/esterno-01", "Esterno - La Conte House"),
                img("images/house/esterno/esterno-02", "Esterno - La Conte House"),
                img("images/house/esterno/esterno-03", "Esterno - La Conte House"),
                img("images/house/esterno/esterno-04", "Esterno - La Conte House")
            ]
        }
    };

    // Auto-popola gli array "Tutte" in base alle categorie per evitare array duplicati da gestire manualmente
    galleryData.villa["Tutte"] = [
        ...galleryData.villa["giardino"],
        ...galleryData.villa["salone&cucina"],
        ...galleryData.villa["stanza 1"],
        ...galleryData.villa["stanza 2"],
        ...galleryData.villa["stanza 3"],
        ...galleryData.villa["bagno 1"]
    ];

    galleryData.conte["Tutte"] = [
        ...galleryData.conte["salone&cucina"],
        ...galleryData.conte["stanza"],
        ...galleryData.conte["bagno"],
        ...galleryData.conte["esterno"]
    ];

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
    
    const lbLabel = document.createElement('div');
    lbLabel.className = 'carousel-label fade-in';
    lbLabel.style.zIndex = '10002';
    lbLabel.style.bottom = '30px';
    lbLabel.style.right = '30px';
    lbLabel.style.position = 'fixed';
    
    const lbPrev = document.createElement('span');
    lbPrev.className = 'lightbox-nav lightbox-prev';
    lbPrev.innerHTML = '&#10094;';

    const lbNext = document.createElement('span');
    lbNext.className = 'lightbox-nav lightbox-next';
    lbNext.innerHTML = '&#10095;';

    lightbox.appendChild(closeBtn);
    lightbox.appendChild(lbLabel);
    lightbox.appendChild(lbPrev);
    lightbox.appendChild(lbNext);
    lightbox.appendChild(maxImg);
    document.body.appendChild(lightbox);
    
    window.lbCurrentArray = [];
    window.lbCurrentIndex = 0;
    window.lbSyncCarousel = null;

    window.openLightboxWithArray = function() {
        lightbox.style.display = 'flex';
        setTimeout(() => lightbox.classList.add('show'), 10);
        updateLightboxImg();
        document.body.style.overflow = 'hidden';
    };

    function updateLightboxImg() {
        if(window.lbCurrentArray && window.lbCurrentArray.length > 0) {
            const imgObj = window.lbCurrentArray[window.lbCurrentIndex];
            maxImg.srcset = `${imgObj.webp["480"]} 480w, ${imgObj.webp["960"]} 960w, ${imgObj.webp["1600"]} 1600w`;
            maxImg.sizes = "100vw";
            maxImg.src = imgObj.fallback;
            maxImg.alt = imgObj.alt;
            
            lbLabel.textContent = imgObj.alt.split(' - ')[0];
            
            if(window.lbSyncCarousel) {
                window.lbSyncCarousel(window.lbCurrentIndex);
            }
        }
    }

    lbPrev.addEventListener('click', (e) => {
        e.preventDefault();
        e.stopPropagation();
        window.lbCurrentIndex = (window.lbCurrentIndex - 1 + window.lbCurrentArray.length) % window.lbCurrentArray.length;
        updateLightboxImg();
    });

    lbNext.addEventListener('click', (e) => {
        e.preventDefault();
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


    function initializeCarousel(galleryId, catsId, propertyKey) {
        const gallery = document.getElementById(galleryId);
        const catsContainer = document.getElementById(catsId);
        if (!gallery || !galleryData[propertyKey]) return;

        if (catsContainer) catsContainer.style.display = 'none';

        const imageElement = gallery.querySelector('.property-image');
        const prevBtn = gallery.querySelector('.prev-btn');
        const nextBtn = gallery.querySelector('.next-btn');

        let currentIndex = 0;

        function updateImage() {
            const imgs = galleryData[propertyKey]['Tutte'];
            if (imgs && imgs.length > 0) {
                const imgObj = imgs[currentIndex];
                imageElement.srcset = `${imgObj.webp["480"]} 480w, ${imgObj.webp["960"]} 960w, ${imgObj.webp["1600"]} 1600w`;
                imageElement.sizes = "(max-width: 768px) 100vw, 45vw";
                imageElement.src = imgObj.fallback;
                imageElement.alt = imgObj.alt;
                
                // Preload adjacent images
                const preloadNext = new Image();
                preloadNext.src = imgs[(currentIndex + 1) % imgs.length].fallback;
                const preloadPrev = new Image();
                preloadPrev.src = imgs[(currentIndex - 1 + imgs.length) % imgs.length].fallback;
                
                let label = gallery.querySelector('.carousel-label');
                if (!label) {
                    label = document.createElement('div');
                    label.className = 'carousel-label fade-in';
                    const imgContainer = imageElement.parentElement;
                    imgContainer.style.position = 'relative'; 
                    imgContainer.appendChild(label);
                }
                
                label.textContent = imgObj.alt.split(' - ')[0];
            }
        }

        nextBtn.addEventListener('click', (e) => {
            e.preventDefault();
            e.stopPropagation();
            const len = galleryData[propertyKey]['Tutte'].length;
            currentIndex = (currentIndex + 1) % len;
            updateImage();
        });

        prevBtn.addEventListener('click', (e) => {
            e.preventDefault();
            e.stopPropagation();
            const len = galleryData[propertyKey]['Tutte'].length;
            currentIndex = (currentIndex - 1 + len) % len;
            updateImage();
        });
        
        imageElement.addEventListener('click', function(e) {
            window.lbCurrentArray = galleryData[propertyKey]['Tutte'];
            window.lbCurrentIndex = currentIndex;
            window.lbSyncCarousel = function(index) {
                currentIndex = index;
                updateImage();
            };
            window.openLightboxWithArray();
        });

        updateImage();
    }

    initializeCarousel('gallery-villa', 'cats-villa', 'villa');
    initializeCarousel('gallery-conte', 'cats-conte', 'conte');

    // === TABS NAVIGATION ===
    const navBtns = document.querySelectorAll('.nav-btn');
    const sections = document.querySelectorAll('.content-section');

    navBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            navBtns.forEach(b => {
                b.classList.remove('active');
                b.setAttribute('aria-selected', 'false');
            });
            sections.forEach(s => {
                s.classList.remove('active');
            });

            btn.classList.add('active');
            btn.setAttribute('aria-selected', 'true');
            // Check if element exists before adding class
            const target = document.getElementById(btn.getAttribute('data-target'));
            if (target) target.classList.add('active');
        });
    });

    // === I18N SYSTEM ===
    const langSwitch = document.getElementById('lang-switch');
    // Default to Italian or user's previously saved lang
    let currentLang = localStorage.getItem('preferredLang') || 'it';

    // Set selector value
    if (langSwitch) {
        langSwitch.value = currentLang;

        langSwitch.addEventListener('change', (e) => {
            currentLang = e.target.value;
            localStorage.setItem('preferredLang', currentLang);
            applyLanguage();
        });
    }

    function sanitizeHtml(str) {
        return str.replace(/&/g, '&amp;')
                  .replace(/</g, '&lt;')
                  .replace(/>/g, '&gt;')
                  .replace(/"/g, '&quot;')
                  .replace(/'/g, '&#39;')
                  .replace(/&lt;em&gt;/g, '<em>')
                  .replace(/&lt;\/em&gt;/g, '</em>')
                  .replace(/&lt;strong&gt;/g, '<strong>')
                  .replace(/&lt;\/strong&gt;/g, '</strong>');
    }

    function applyLanguage() {
        if (!window.translations) return;
        const dict = window.translations[currentLang];
        if (!dict) return;

        const elementsToTranslate = document.querySelectorAll('[data-i18n]');
        elementsToTranslate.forEach(el => {
            const key = el.getAttribute('data-i18n');
            if (dict[key]) {
                // if data-html is true, insert as HTML (useful for strong/em tags)
                if (el.getAttribute('data-html') === 'true') {
                    el.innerHTML = sanitizeHtml(dict[key]);
                } else {
                    el.textContent = dict[key];
                }
            }
        });
    }

    // Apply immediately
    applyLanguage();

    // === INTERSECTION OBSERVER FOR SMART SCROLLING ===
    const observerOptions = {
        threshold: 0.1, // Trigger when 10% is visible
        rootMargin: "0px 0px -50px 0px"
    };

    const scrollObserver = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('reveal-visible');
                // Optional: stop observing once revealed
                // observer.unobserve(entry.target); 
            }
        });
    }, observerOptions);


    // === FAQ ACCORDION ===
    const faqQuestions = document.querySelectorAll('.faq-question');
    faqQuestions.forEach(q => {
        q.addEventListener('click', () => {
            // Toggle current
            q.classList.toggle('active');
            const answer = q.nextElementSibling;
            if (q.classList.contains('active')) {
                answer.style.maxHeight = answer.scrollHeight + "px";
            } else {
                answer.style.maxHeight = 0;
            }
        });
    });

    const fadeElements = document.querySelectorAll('.fade-in-up');
    fadeElements.forEach(el => scrollObserver.observe(el));

    // === LOADING LOGIC ===
    const body = document.body;
    body.classList.add('loading');
    const loaderStart = performance.now();

    window.addEventListener('load', () => {
        const loader = document.getElementById('loader-wrapper');
        const elapsed = performance.now() - loaderStart;
        const remaining = Math.max(0, 2000 - elapsed);
        setTimeout(() => {
            if (loader) loader.classList.add('loader-hidden');
            body.classList.remove('loading');
        }, remaining);
    });

});

// === DYNAMIC CARD COLORING ===
window.addEventListener('load', () => {
    const cards = document.querySelectorAll('.blog-card');
    cards.forEach(card => {
        const bgDiv = card.querySelector('.blog-image');
        if (!bgDiv) return;

        let bgUrl = bgDiv.style.backgroundImage;
        if (bgUrl && bgUrl.includes('url(')) {
            bgUrl = bgUrl.replace(/^url\(['"]?/, '').replace(/['"]?\)$/, '');

            if (!bgUrl.startsWith('/') && !bgUrl.startsWith(window.location.origin)) {
                return;
            }

            const img = new Image();
            img.crossOrigin = "Anonymous";
            img.src = bgUrl;
            img.onload = function () {
                const canvas = document.createElement('canvas');
                const ctx = canvas.getContext('2d');
                canvas.width = img.width;
                canvas.height = img.height;
                ctx.drawImage(img, 0, 0);

                try {
                    const data = ctx.getImageData(0, 0, canvas.width, canvas.height).data;
                    let r = 0, g = 0, b = 0, count = 0;
                    // sample every 20th pixel to be fast
                    for (let i = 0; i < data.length; i += 4 * 20) {
                        r += data[i];
                        g += data[i + 1];
                        b += data[i + 2];
                        count++;
                    }
                    r = Math.floor(r / count);
                    g = Math.floor(g / count);
                    b = Math.floor(b / count);

                    // Apply a soft tint of the dominant color to the card background
                    card.style.backgroundColor = `rgba(${r}, ${g}, ${b}, 0.3)`;

                    // Apply a slightly stronger tint to the border
                    card.style.borderColor = `rgba(${r}, ${g}, ${b}, 0.8)`;
                    card.style.boxShadow = `0 10px 30px rgba(${r}, ${g}, ${b}, 0.2)`;

                    // Darken the color for title text
                    const darkened = `rgb(${Math.max(0, r - 80)}, ${Math.max(0, g - 80)}, ${Math.max(0, b - 80)})`;
                    const h3 = card.querySelector('h3');
                    if (h3) h3.style.color = darkened;

                } catch (e) {
                    console.log("Could not extract color from " + bgUrl, e);
                    return;
                }
            };
        }
    });
});
