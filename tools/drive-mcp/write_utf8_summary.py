import json

with open("all_drive_media_recursive.json", "r", encoding="utf-8") as f:
    data = json.load(f)

with open("summary_utf8.txt", "w", encoding="utf-8") as out:
    for root_folder, files in data.items():
        out.write(f"\n=======================================================\n")
        out.write(f"=== {root_folder}: TOTAL {len(files)} FILES ===\n")
        out.write(f"=======================================================\n")
        
        # Group by subfolder
        by_folder = {}
        for item in files:
            p = item.get('folder_path', root_folder)
            by_folder.setdefault(p, []).append(item)
            
        for path, items in by_folder.items():
            out.write(f"\n--- Subfolder: {path} ({len(items)} items) ---\n")
            for i, item in enumerate(items, 1):
                name = item.get('name')
                mime = item.get('mimeType')
                size_mb = round(int(item.get('size', 0)) / (1024 * 1024), 2) if item.get('size') else "N/A"
                fid = item.get('id')
                out.write(f"  {i:02d}. [{mime}] {name} ({size_mb} MB) [ID: {fid}]\n")

print("summary_utf8.txt written successfully.")
