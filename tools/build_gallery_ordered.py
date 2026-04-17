import os
import json
import re

VILLA_DIR = '/Users/umbertotoraldo/petra-protocol/Villa-del-Conte/images/villa'
HOUSE_DIR = '/Users/umbertotoraldo/petra-protocol/Villa-del-Conte/images/house'

ALLOWED_EXTENSIONS = ('.jpg', '.jpeg', '.png', '.webp', '.jpg'.upper(), '.jpeg'.upper(), '.png'.upper())

VILLA_ORDER = ["giardino", "salone&cucina", "stanza 1", "stanza 2", "stanza 3", "bagno 1"]
HOUSE_ORDER = ["salone&cucina", "stanza", "bagno", "esterno"]

def build_dict(base_dir, prefix, desired_order):
    data = {}
    tutte = []
    
    try:
        actual_subdirs = [d for d in os.listdir(base_dir) if os.path.isdir(os.path.join(base_dir, d))]
    except:
        return {}
        
    # Process only directories that exist, following the desired order
    ordered_subdirs = [d for d in desired_order if d in actual_subdirs]
    # Keep any extra subdirectories just in case
    for d in actual_subdirs:
        if d not in ordered_subdirs:
            ordered_subdirs.append(d)
            
    for d in ordered_subdirs:
        d_path = os.path.join(base_dir, d)
        files = [f for f in os.listdir(d_path) if f.endswith(ALLOWED_EXTENSIONS) and not f.startswith('.')]
        files.sort() # sort images within same folder alphabetically
        
        arr = []
        for f in files:
            p = f"images/{prefix}/{d}/{f}"
            arr.append(p)
            tutte.append(p)
            
        data[d] = arr
    
    data['Tutte'] = tutte
    return data

gallery_data = {
    "villa": build_dict(VILLA_DIR, 'villa', VILLA_ORDER),
    "conte": build_dict(HOUSE_DIR, 'house', HOUSE_ORDER)
}

js_str = "    const galleryData = " + json.dumps(gallery_data, indent=4) + ";"

script_path = '/Users/umbertotoraldo/petra-protocol/Villa-del-Conte/script.js'
with open(script_path, 'r', encoding='utf-8') as f:
    content = f.read()
    
pattern = r'const galleryData = \{.*?\n    \};\n'
content = re.sub(pattern, js_str + '\n', content, flags=re.DOTALL)

with open(script_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("galleryData fully rebuilt with CUSTOM ORDER logic!")

# Bump cache version in index.html to force reload of script.js
index_path = '/Users/umbertotoraldo/petra-protocol/Villa-del-Conte/index.html'
with open(index_path, 'r', encoding='utf-8') as f:
    idx = f.read()
    
# We will just do a generic regex bump to handle ?v=X easily
idx = re.sub(r'script\.js\?v=\d+', 'script.js?v=20', idx)
idx = re.sub(r'style\.css\?v=\d+(\.\d+)?', 'style.css?v=20', idx)

with open(index_path, 'w', encoding='utf-8') as f:
    f.write(idx)
    
print("Cache version bumped to 20.")
