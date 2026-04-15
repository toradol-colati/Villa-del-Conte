document.addEventListener('DOMContentLoaded', () => {
    
    // === CAROUSEL LOGIC ===
    const galleryData = {
    "villa": {
        "giardino": [
            "images/villa/giardino/26EA642B-36BE-4AB2-995D-C0369173014E_4_5005_c.jpeg",
            "images/villa/giardino/4268B1BD-1472-4D5E-9817-43D37EA16A31_4_5005_c.jpeg",
            "images/villa/giardino/4EDED8F3-742B-4346-8A1B-1D50343EE903_1_105_c.jpeg",
            "images/villa/giardino/8276F5D8-1BC1-4B2D-89D9-8C62F60E755C_4_5005_c.jpeg",
            "images/villa/giardino/8EEC52B7-1160-4CC4-AA87-8B63F929DD3D_1_105_c.jpeg",
            "images/villa/giardino/9A504C58-C365-4B6E-A001-A5F8963D3B91_1_105_c.jpeg",
            "images/villa/giardino/E35C3DB7-9DA4-45FC-8C37-E52FE5D2E582_4_5005_c.jpeg",
            "images/villa/giardino/FC48C6C8-2DD0-4ACC-B66E-6DC6BD20549E_1_105_c.jpeg"
        ],
        "salone&cucina": [
            "images/villa/salone&cucina/DSC_0085.JPG",
            "images/villa/salone&cucina/DSC_0090.JPG",
            "images/villa/salone&cucina/DSC_0099.JPG",
            "images/villa/salone&cucina/DSC_0104.JPG",
            "images/villa/salone&cucina/DSC_0111.JPG"
        ],
        "stanza 1": [
            "images/villa/stanza 1/1AF6C193-C0ED-4977-9D61-02CE8AFBAE62_4_5005_c.jpeg",
            "images/villa/stanza 1/2A4D06F3-4731-4027-8429-52C259E2C0AE_4_5005_c.jpeg",
            "images/villa/stanza 1/2AAD7C51-DD85-4CFE-9B71-F4F08838A756_4_5005_c.jpeg",
            "images/villa/stanza 1/6A87A1E1-CFE5-4B9B-82BB-B7855E1C01B2_4_5005_c.jpeg",
            "images/villa/stanza 1/95531917-55C8-4B29-B6EB-F934DAF3F566_4_5005_c.jpeg"
        ],
        "stanza 2": [
            "images/villa/stanza 2/04FD21C3-8C04-440F-B27E-E28CD0FCE02D_4_5005_c.jpeg",
            "images/villa/stanza 2/167AB6BE-CA0E-4D07-898C-514027A0280B_4_5005_c.jpeg",
            "images/villa/stanza 2/66E2FC4D-C8C3-4081-95B0-DA076704FA44_4_5005_c.jpeg"
        ],
        "stanza 3": [
            "images/villa/stanza 3/8037F6AB-B5A0-4EB9-9FA1-97F843835080_4_5005_c.jpeg",
            "images/villa/stanza 3/F4CBF9BB-20B1-4B40-8C10-CBE878BF99D0_4_5005_c.jpeg"
        ],
        "Tutte": [
            "images/villa/giardino/26EA642B-36BE-4AB2-995D-C0369173014E_4_5005_c.jpeg",
            "images/villa/giardino/4268B1BD-1472-4D5E-9817-43D37EA16A31_4_5005_c.jpeg",
            "images/villa/giardino/4EDED8F3-742B-4346-8A1B-1D50343EE903_1_105_c.jpeg",
            "images/villa/giardino/8276F5D8-1BC1-4B2D-89D9-8C62F60E755C_4_5005_c.jpeg",
            "images/villa/giardino/8EEC52B7-1160-4CC4-AA87-8B63F929DD3D_1_105_c.jpeg",
            "images/villa/giardino/9A504C58-C365-4B6E-A001-A5F8963D3B91_1_105_c.jpeg",
            "images/villa/giardino/E35C3DB7-9DA4-45FC-8C37-E52FE5D2E582_4_5005_c.jpeg",
            "images/villa/giardino/FC48C6C8-2DD0-4ACC-B66E-6DC6BD20549E_1_105_c.jpeg",
            "images/villa/salone&cucina/DSC_0085.JPG",
            "images/villa/salone&cucina/DSC_0090.JPG",
            "images/villa/salone&cucina/DSC_0099.JPG",
            "images/villa/salone&cucina/DSC_0104.JPG",
            "images/villa/salone&cucina/DSC_0111.JPG",
            "images/villa/stanza 1/1AF6C193-C0ED-4977-9D61-02CE8AFBAE62_4_5005_c.jpeg",
            "images/villa/stanza 1/2A4D06F3-4731-4027-8429-52C259E2C0AE_4_5005_c.jpeg",
            "images/villa/stanza 1/2AAD7C51-DD85-4CFE-9B71-F4F08838A756_4_5005_c.jpeg",
            "images/villa/stanza 1/6A87A1E1-CFE5-4B9B-82BB-B7855E1C01B2_4_5005_c.jpeg",
            "images/villa/stanza 1/95531917-55C8-4B29-B6EB-F934DAF3F566_4_5005_c.jpeg",
            "images/villa/stanza 2/04FD21C3-8C04-440F-B27E-E28CD0FCE02D_4_5005_c.jpeg",
            "images/villa/stanza 2/167AB6BE-CA0E-4D07-898C-514027A0280B_4_5005_c.jpeg",
            "images/villa/stanza 2/66E2FC4D-C8C3-4081-95B0-DA076704FA44_4_5005_c.jpeg",
            "images/villa/stanza 3/8037F6AB-B5A0-4EB9-9FA1-97F843835080_4_5005_c.jpeg",
            "images/villa/stanza 3/F4CBF9BB-20B1-4B40-8C10-CBE878BF99D0_4_5005_c.jpeg"
        ]
    },
    "conte": {
        "salone&cucina": [
            "images/house/salone&cucina/DSC_0025.JPG",
            "images/house/salone&cucina/DSC_0028.JPG",
            "images/house/salone&cucina/DSC_0032.JPG",
            "images/house/salone&cucina/DSC_0061.JPG",
            "images/house/salone&cucina/DSC_0066.JPG",
            "images/house/salone&cucina/DSC_0071.JPG"
        ],
        "stanza": [
            "images/house/stanza/DSC_0968.JPG",
            "images/house/stanza/DSC_0984.JPG",
            "images/house/stanza/DSC_0987.JPG",
            "images/house/stanza/DSC_0997.JPG",
            "images/house/stanza/DSC_1007.JPG"
        ],
        "bagno": [
            "images/house/bagno/DSC_0079.JPG",
            "images/house/bagno/DSC_0130.JPG"
        ],
        "esterno": [
            "images/house/esterno/3B4895AD-286E-4081-A3A8-80E2FFE69987_1_105_c.jpeg",
            "images/house/esterno/6070F5FC-C36D-4CB8-9E8B-348F4A1FC35D_1_105_c.jpeg",
            "images/house/esterno/6853A0C5-7E98-4629-B29B-F68321A7F71D_1_105_c.jpeg",
            "images/house/esterno/FFBF2795-CFCB-431C-A979-0E5AAC0CA78C.jpeg"
        ],
        "Tutte": [
            "images/house/salone&cucina/DSC_0025.JPG",
            "images/house/salone&cucina/DSC_0028.JPG",
            "images/house/salone&cucina/DSC_0032.JPG",
            "images/house/salone&cucina/DSC_0061.JPG",
            "images/house/salone&cucina/DSC_0066.JPG",
            "images/house/salone&cucina/DSC_0071.JPG",
            "images/house/stanza/DSC_0968.JPG",
            "images/house/stanza/DSC_0984.JPG",
            "images/house/stanza/DSC_0987.JPG",
            "images/house/stanza/DSC_0997.JPG",
            "images/house/stanza/DSC_1007.JPG",
            "images/house/bagno/DSC_0079.JPG",
            "images/house/bagno/DSC_0130.JPG",
            "images/house/esterno/3B4895AD-286E-4081-A3A8-80E2FFE69987_1_105_c.jpeg",
            "images/house/esterno/6070F5FC-C36D-4CB8-9E8B-348F4A1FC35D_1_105_c.jpeg",
            "images/house/esterno/6853A0C5-7E98-4629-B29B-F68321A7F71D_1_105_c.jpeg",
            "images/house/esterno/FFBF2795-CFCB-431C-A979-0E5AAC0CA78C.jpeg"
        ]
    }
};

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
            if(target) target.classList.add('active');
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

    function applyLanguage() {
        if(!window.translations) return;
        const dict = window.translations[currentLang];
        if(!dict) return;

        const elementsToTranslate = document.querySelectorAll('[data-i18n]');
        elementsToTranslate.forEach(el => {
            const key = el.getAttribute('data-i18n');
            if(dict[key]) {
                // if data-html is true, insert as HTML (useful for strong/em tags)
                if(el.getAttribute('data-html') === 'true') {
                    el.innerHTML = dict[key];
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
});
  
// === LOADING LOGIC ===
document.addEventListener('DOMContentLoaded', () => {
    const body = document.body;
    body.classList.add('loading');
  
    window.addEventListener('load', () => {
        const loader = document.getElementById('loader-wrapper');
        setTimeout(() => {
            if(loader) loader.classList.add('loader-hidden');
            body.classList.remove('loading');
        }, 3000); 
    });

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

});

// === DYNAMIC CARD COLORING ===
window.addEventListener('load', () => {
    const cards = document.querySelectorAll('.blog-card');
    cards.forEach(card => {
        const bgDiv = card.querySelector('.blog-image');
        if(!bgDiv) return;
        
        let bgUrl = bgDiv.style.backgroundImage;
        if(bgUrl && bgUrl.includes('url(')) {
            bgUrl = bgUrl.replace(/^url\(['"]?/, '').replace(/['"]?\)$/, '');
            
            const img = new Image();
            img.crossOrigin = "Anonymous";
            img.src = bgUrl;
            img.onload = function() {
                const canvas = document.createElement('canvas');
                const ctx = canvas.getContext('2d');
                canvas.width = img.width;
                canvas.height = img.height;
                ctx.drawImage(img, 0, 0);
                
                try {
                    const data = ctx.getImageData(0, 0, canvas.width, canvas.height).data;
                    let r = 0, g = 0, b = 0, count = 0;
                    // sample every 20th pixel to be fast
                    for(let i = 0; i < data.length; i += 4 * 20) {
                        r += data[i];
                        g += data[i+1];
                        b += data[i+2];
                        count++;
                    }
                    r = Math.floor(r / count);
                    g = Math.floor(g / count);
                    b = Math.floor(b / count);
                    
                    // Apply a soft tint of the dominant color to the card background
                    card.style.backgroundColor = `rgba(${r}, ${g}, ${b}, 0.15)`;
                    
                    // Apply a slightly stronger tint to the border
                    card.style.borderColor = `rgba(${r}, ${g}, ${b}, 0.4)`;
                    
                    // Darken the color for title text
                    const darkened = `rgb(${Math.max(0, r-80)}, ${Math.max(0, g-80)}, ${Math.max(0, b-80)})`;
                    const h3 = card.querySelector('h3');
                    if(h3) h3.style.color = darkened;
                    
                } catch(e) {
                    console.log("Could not extract color from " + bgUrl, e);
                }
            };
        }
    });
});
