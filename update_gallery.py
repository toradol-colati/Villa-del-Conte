import os
import json
import re

base_dir = '/Users/umbertotoraldo/petra-protocol/Villa-del-Conte/'
images_dir = os.path.join(base_dir, 'images')

def scan_dir(prop_folder, expected_order):
    path = os.path.join(images_dir, prop_folder)
    data = {}
    
    # Pre-populate with expected order to enforce sorting
    for cat in expected_order:
        data[cat] = []
        
    for root, dirs, files in os.walk(path):
        cat = os.path.basename(root)
        
        # Skip the parent folder itself or hidden folders
        if root == path or cat.startswith('.'):
            continue
            
        if cat not in data:
            data[cat] = []
            
        for f in files:
            if f.endswith('.jpg') or f.endswith('.jpeg') or f.endswith('.JPG') or f.endswith('.JPEG') or f.endswith('.png'):
                # relative path from the root of the site
                rel_path = f"images/{prop_folder}/{cat}/{f}"
                data[cat].append(rel_path)
    
    # Remove empty categories and sort files inside categories
    final_data = {}
    all_files = []
    
    # Process explicitly ordered categories first
    for cat in expected_order:
        if cat in data and len(data[cat]) > 0:
            s_files = sorted(data[cat])
            final_data[cat] = s_files
            all_files.extend(s_files)
            
    # Process any leftover categories not in expected order
    for cat, files in data.items():
        if cat not in expected_order and len(files) > 0:
            s_files = sorted(files)
            final_data[cat] = s_files
            all_files.extend(s_files)
            
    final_data["Tutte"] = all_files
    return final_data

villa_order = ["giardino", "salone&cucina", "stanza 1", "stanza 2", "stanza 3"]
conte_order = ["salone&cucina", "stanza", "bagno", "esterno"]

galleryData = {
    "villa": scan_dir("villa", villa_order),
    "conte": scan_dir("house", conte_order)
}

# Now rewrite script.js
script_path = os.path.join(base_dir, 'script.js')
with open(script_path, 'r', encoding='utf-8') as f:
    text = f.read()

# Replace galleryData block
# It starts with: const galleryData = {
# It ends with:   }
# };
pattern = r'const galleryData = \{.*?\n\};'
new_data_str = "const galleryData = " + json.dumps(galleryData, indent=4) + ";"
text = re.sub(pattern, new_data_str, text, flags=re.DOTALL)

with open(script_path, 'w', encoding='utf-8') as f:
    f.write(text)

print("galleryData updated successfully!")
