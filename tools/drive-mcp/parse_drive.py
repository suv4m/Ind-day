import json

with open("drive_contents.json", "r", encoding="utf-8") as f:
    data = json.load(f)

for folder, files in data.items():
    print(f"\n==========================================")
    print(f"=== FOLDER: {folder} ({len(files)} files) ===")
    print(f"==========================================")
    for idx, item in enumerate(files, 1):
        name = item.get('name', 'Unknown')
        mime = item.get('mimeType', 'Unknown')
        fid = item.get('id', '')
        size = item.get('size', 'N/A')
        print(f"{idx:02d}. [{mime}] {name} (ID: {fid}, Size: {size} bytes)")
