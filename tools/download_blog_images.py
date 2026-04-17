import urllib.request
import json
import os

topics = {
    "territorio": "Tropea",
    "romane": "Magna_Grecia",
    "toraldo": "Federico_II_di_Svevia",
    "costa": "Capo_Vaticano",
    "tropea": "Santuario_di_Santa_Maria_dell'Isola",
    "santadomenica": "Ricadi",
    "cucina": "'Nduja"
}

def get_wiki_image(title):
    url = f"https://it.wikipedia.org/w/api.php?action=query&titles={urllib.parse.quote(title)}&prop=pageimages&format=json&pithumbsize=1000"
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode())
            pages = data['query']['pages']
            for page_id in pages:
                if 'thumbnail' in pages[page_id]:
                    return pages[page_id]['thumbnail']['source']
    except Exception as e:
        print(f"Error fetching {title}: {e}")
    return None

os.makedirs('images/blog', exist_ok=True)
images_map = {}

for slug, title in topics.items():
    img_url = get_wiki_image(title)
    if img_url:
        print(f"Downloading {slug}.jpg from {img_url}")
        try:
            req = urllib.request.Request(img_url, headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(req) as resp, open(f'images/blog/{slug}.jpg', 'wb') as out:
                out.write(resp.read())
            images_map[slug] = f'images/blog/{slug}.jpg'
        except Exception as e:
            print(e)
            images_map[slug] = 'images/villa/giardino/26EA642B-36BE-4AB2-995D-C0369173014E_4_5005_c.jpeg' # Fallback
    else:
        images_map[slug] = 'images/villa/giardino/26EA642B-36BE-4AB2-995D-C0369173014E_4_5005_c.jpeg' # Fallback

with open('blog_images.json', 'w') as f:
    json.dump(images_map, f)
print("Done!")
