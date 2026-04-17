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
        
    ordered_subdirs = [d for d in desired_order if d in actual_subdirs]
    for d in actual_subdirs:
        if d not in ordered_subdirs:
            ordered_subdirs.append(d)
            
    for d in ordered_subdirs:
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
    "villa": build_dict(VILLA_DIR, 'villa', VILLA_ORDER),
    "conte": build_dict(HOUSE_DIR, 'house', HOUSE_ORDER)
}

js_str = "    const galleryData = " + json.dumps(gallery_data, indent=4) + ";\n\n"

script_path = '/Users/umbertotoraldo/petra-protocol/Villa-del-Conte/script.js'
with open(script_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Safe replacement using exactly identified markers
start_marker = "// === CAROUSEL LOGIC ==="
end_marker = "    function initializeCarousel(galleryId, catsId, propertyKey) {"

start_idx = content.find(start_marker)
end_idx = content.find(end_marker)

if start_idx != -1 and end_idx != -1:
    new_content = content[:start_idx + len(start_marker)] + "\n" + js_str + content[end_idx:]
    with open(script_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Successfully replaced galleryData securely!")
else:
    print("Could not find markers securely.")
