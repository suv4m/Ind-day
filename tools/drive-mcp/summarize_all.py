import json

with open("all_drive_media_recursive.json", "r", encoding="utf-8") as f:
    data = json.load(f)

for root_folder, files in data.items():
    print(f"\n=======================================================")
    print(f"=== {root_folder}: TOTAL {len(files)} FILES ===")
    print(f"=======================================================")
    
    # Group by subfolder
    by_folder = {}
    for item in files:
        p = item.get('folder_path', root_folder)
        by_folder.setdefault(p, []).append(item)
        
    for path, items in by_folder.items():
        print(f"\n--- Subfolder: {path} ({len(items)} items) ---")
        for i, item in enumerate(items, 1):
            name = item.get('name')
            mime = item.get('mimeType')
            size_mb = round(int(item.get('size', 0)) / (1024 * 1024), 2) if item.get('size') else "N/A"
            fid = item.get('id')
            print(f"  {i:02d}. [{mime}] {name} ({size_mb} MB) [ID: {fid}]")
