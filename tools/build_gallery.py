import os
import json
import re

VILLA_DIR = '/Users/umbertotoraldo/petra-protocol/Villa-del-Conte/images/villa'
HOUSE_DIR = '/Users/umbertotoraldo/petra-protocol/Villa-del-Conte/images/house'

ALLOWED_EXTENSIONS = ('.jpg', '.jpeg', '.png', '.webp', '.jpg'.upper(), '.jpeg'.upper(), '.png'.upper())

def build_dict(base_dir, prefix):
    data = {}
    tutte = []
    
    # Sort subdirectories to ensure consistent order if needed
    try:
        subdirs = sorted([d for d in os.listdir(base_dir) if os.path.isdir(os.path.join(base_dir, d))])
    except:
        return {}
        
    for d in subdirs:
        d_path = os.path.join(base_dir, d)
        files = [f for f in os.listdir(d_path) if f.endswith(ALLOWED_EXTENSIONS) and not f.startswith('.')]
        files.sort()
        
        arr = []
        for f in files:
            p = f"images/{prefix}/{d}/{f}"
            arr.append(p)
            tutte.append(p)
            
        data[d] = arr
    
    data['Tutte'] = tutte
    return data

gallery_data = {
    "villa": build_dict(VILLA_DIR, 'villa'),
    "conte": build_dict(HOUSE_DIR, 'house')
}

js_str = "    const galleryData = " + json.dumps(gallery_data, indent=4) + ";"

script_path = '/Users/umbertotoraldo/petra-protocol/Villa-del-Conte/script.js'
with open(script_path, 'r', encoding='utf-8') as f:
    content = f.read()
    
# Replace the galleryData block
# It starts at: const galleryData = {
# And ends before: function initializeCarousel(galleryId, catsId, propertyKey) {
pattern = r'const galleryData = \{.*?\n    \};\n'
content = re.sub(pattern, js_str + '\n', content, flags=re.DOTALL)

with open(script_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("galleryData fully rebuilt based on file system!")

# Bump cache version in index.html to force reload of script.js
index_path = '/Users/umbertotoraldo/petra-protocol/Villa-del-Conte/index.html'
with open(index_path, 'r', encoding='utf-8') as f:
    idx = f.read()
    
idx = idx.replace('script.js?v=11', 'script.js?v=12')
idx = idx.replace('script.js?v=12', 'script.js?v=13')

with open(index_path, 'w', encoding='utf-8') as f:
    f.write(idx)
    
print("Cache version bumped.")
