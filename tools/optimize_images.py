import os
import glob
import shutil
import json
from PIL import Image, ImageOps

# Need to install Pillow: python3 -m pip install Pillow

directories = [
    'images/villa',
    'images/house',
    'images/blog',
    'images/ui'
]

breakpoints = [480, 960, 1600]

def sanitize_name(base, idx=None):
    if idx is not None:
        idx_str = f"{idx:02d}"
        return f"{base}-{idx_str}"
    return base

# First, collect files per folder (to ensure stable order)
folders_to_files = {}

for root_dir in directories:
    for root, dirs, files in os.walk(root_dir):
        if '_originals' in root:
            continue
        valid_files = [f for f in files if f.lower().endswith(('.jpg', '.jpeg', '.png', '.heic'))]
        if not valid_files:
            continue
        # sort valid files
        valid_files.sort()
        folders_to_files[root] = valid_files

# Process
new_gallery_data = {
    'villa': {},
    'conte': {}
}

import collections
prop_map = {'images/villa': 'villa', 'images/house': 'conte'}

for root, files in folders_to_files.items():
    print(f"Processing folder: {root}")
    
    # create original dir
    orig_dir = os.path.join('images/_originals', root.replace('images/', ''))
    os.makedirs(orig_dir, exist_ok=True)
    
    is_gallery = root.startswith('images/villa') or root.startswith('images/house')
    prop_key = 'villa' if root.startswith('images/villa') else ('conte' if root.startswith('images/house') else None)
    cat_key = os.path.basename(root)
    
    pop_key = prop_key
    if is_gallery and pop_key:
        if cat_key not in new_gallery_data[pop_key]:
            new_gallery_data[pop_key][cat_key] = []
    
    for idx, f in enumerate(files, start=1):
        src_path = os.path.join(root, f)
        
        # skip if already optimized file format
        if '-480w.webp' in f or 'fallback' in f:
            continue

        base_name = os.path.splitext(f)[0]
        if is_gallery:
            new_base = sanitize_name(cat_key.replace('&', '_'), idx)
        else:
            new_base = base_name

        try:
            img = Image.open(src_path)
            img = ImageOps.exif_transpose(img)
            
            webp_dict = {}
            for w in breakpoints:
                # Calculate height
                ratio = w / float(img.width)
                if ratio >= 1: 
                    # image smaller than breakpoint, just use original size
                    new_w = img.width
                    new_h = img.height
                else:
                    new_w = w
                    new_h = int(float(img.height) * ratio)
                
                new_img = img.resize((new_w, new_h), Image.Resampling.LANCZOS)
                out_path = os.path.join(root, f"{new_base}-{w}w.webp")
                new_img.save(out_path, 'WEBP', quality=80)
                webp_dict[str(w)] = out_path

            # Fallback jpg
            fallback_img = img.resize((min(960, img.width), int(float(img.height) * (min(960, img.width) / float(img.width)))), Image.Resampling.LANCZOS)
            fallback_path = os.path.join(root, f"{new_base}.jpg")
            # If the original was RGBA, convert to RGB
            if fallback_img.mode in ("RGBA", "P"):
                fallback_img = fallback_img.convert("RGB")
            fallback_img.save(fallback_path, 'JPEG', quality=80)

            # Move original
            dest_orig = os.path.join(orig_dir, f)
            shutil.move(src_path, dest_orig)
            print(f"  Moved original to {dest_orig} and generated sizes for {new_base}")

            if is_gallery:
                cat_display = cat_key.replace('salone&cucina', 'Salotto / Cucina').replace('giardino', 'Giardino').replace('esterno', 'Esterno').replace('bagno', 'Bagno').replace('stanza', 'Stanza').capitalize()
                alt_prop = "La Villa" if prop_key == 'villa' else "La Conte House"
                alt_text = f"{cat_display} - {alt_prop}"
                
                new_gallery_data[pop_key][cat_key].append({
                    "webp": webp_dict,
                    "fallback": fallback_path,
                    "alt": alt_text
                })

        except Exception as e:
            print(f"  Failed processing {src_path}: {e}")

# Pre-populate Tutte
for p in ['villa', 'conte']:
    tutte = []
    for c, items in new_gallery_data[p].items():
        tutte.extend(items)
    new_gallery_data[p]['Tutte'] = tutte

with open('gallery_data.json', 'w') as f:
    json.dump(new_gallery_data, f, indent=4)
print("Saved gallery_data.json!")
