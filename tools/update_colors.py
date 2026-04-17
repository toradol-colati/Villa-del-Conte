import os

js_append = """
// === DYNAMIC CARD COLORING ===
window.addEventListener('load', () => {
    const cards = document.querySelectorAll('.blog-card');
    cards.forEach(card => {
        const bgDiv = card.querySelector('.blog-image');
        if(!bgDiv) return;
        
        let bgUrl = bgDiv.style.backgroundImage;
        if(bgUrl && bgUrl.includes('url(')) {
            bgUrl = bgUrl.replace(/^url\\(['"]?/, '').replace(/['"]?\\)$/, '');
            
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
"""

import re
script_path = '/Users/umbertotoraldo/petra-protocol/Villa-del-Conte/script.js'
with open(script_path, 'r', encoding='utf-8') as f:
    text = f.read()

if "DYNAMIC CARD COLORING" not in text:
    text += "\n" + js_append
    
with open(script_path, 'w', encoding='utf-8') as f:
    f.write(text)

# Also update cache-busting index.html
with open('/Users/umbertotoraldo/petra-protocol/Villa-del-Conte/index.html', 'r', encoding='utf-8') as f:
    idx = f.read()
idx = idx.replace('script.js?v=7', 'script.js?v=8')
with open('/Users/umbertotoraldo/petra-protocol/Villa-del-Conte/index.html', 'w', encoding='utf-8') as f:
    f.write(idx)

print("Dynamic Card Coloring added!")
