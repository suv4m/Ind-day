import urllib.request
import json

with open("all_drive_media_recursive.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Find a sample image
sample_img = None
for root, items in data.items():
    for it in items:
        if it.get('mimeType', '').startswith('image/'):
            sample_img = it
            break
    if sample_img:
        break

fid = sample_img['id']
name = sample_img['name']
thumb_orig = sample_img.get('thumbnailLink')
print(f"Sample: {name} (ID: {fid})")
print(f"Orig thumbnail: {thumb_orig}")

test_urls = [
    ("thumbnailLink orig", thumb_orig),
    ("thumbnailLink sz=s1920", thumb_orig.replace("=s220", "=s1920") if thumb_orig else ""),
    ("drive.google.com/thumbnail?id=...&sz=w1600", f"https://drive.google.com/thumbnail?id={fid}&sz=w1600"),
    ("drive.google.com/uc?export=view&id=...", f"https://drive.google.com/uc?export=view&id={fid}"),
]

for label, u in test_urls:
    if not u: continue
    req = urllib.request.Request(u, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            print(f"[{label}] -> {resp.status}, Content-Type: {resp.headers.get('Content-Type')}, Length: {resp.headers.get('Content-Length')}")
    except Exception as e:
        print(f"[{label}] -> ERROR: {e}")
