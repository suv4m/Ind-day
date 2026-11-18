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
        thumb = item.get('thumbnailLink', 'N/A')
        web_content = item.get('webContentLink', 'N/A')
        web_view = item.get('webViewLink', 'N/A')
        print(f"[{idx:02d}] {name} ({mime})")
        print(f"     ID: {fid} | Size: {size}")
        print(f"     View URL: https://drive.google.com/file/d/{fid}/view")
        print(f"     Preview / Embed: https://drive.google.com/file/d/{fid}/preview")
        print(f"     Direct/Stream URL: https://lh3.googleusercontent.com/d/{fid}")
        if thumb != 'N/A':
            print(f"     Thumbnail: {thumb}")
