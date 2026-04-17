import re

with open("script.js", "r") as f:
    text = f.read()

# Fix 1: Add preloading to updateImage
updateImage_str = """        function updateImage() {
            const imgs = galleryData[propertyKey]['Tutte'];
            if (imgs && imgs.length > 0) {
                imageElement.src = imgs[currentIndex];
                
                // Preload adjacent images to fix loading delays
                const preloadNext = new Image();
                preloadNext.src = imgs[(currentIndex + 1) % imgs.length];
                const preloadPrev = new Image();
                preloadPrev.src = imgs[(currentIndex - 1 + imgs.length) % imgs.length];"""

text = text.replace("""        function updateImage() {
            const imgs = galleryData[propertyKey]['Tutte'];
            if (imgs && imgs.length > 0) {
                imageElement.src = imgs[currentIndex];""", updateImage_str)

# Fix 2: Add e.preventDefault() and e.stopPropagation() to inline carousel buttons
nextBtn_str = """        nextBtn.addEventListener('click', (e) => {
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
        });"""

text = re.sub(r"        nextBtn\.addEventListener\('click', \(\) => \{.+?updateImage\(\);\n        \}\);", nextBtn_str, text, flags=re.DOTALL)

# Fix 3: Also ensure Lightbox buttons have preventDefault
lbPrev_str = """    lbPrev.addEventListener('click', (e) => {
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
    });"""

text = re.sub(r"    lbPrev\.addEventListener\('click', \(e\) => \{.+?updateLightboxImg\(\);\n    \}\);", lbPrev_str, text, flags=re.DOTALL)

with open("script.js", "w") as f:
    f.write(text)

