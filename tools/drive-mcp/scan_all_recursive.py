import os
import json
from drive_mcp_server import get_drive_service

service = get_drive_service()

def list_folder_recursive(folder_id, folder_name, path_str=""):
    current_path = f"{path_str}/{folder_name}" if path_str else folder_name
    print(f"Scanning folder: {current_path} (ID: {folder_id})")
    
    cq = f"'{folder_id}' in parents and trashed = false"
    fields = "nextPageToken, files(id, name, mimeType, description, webViewLink, webContentLink, thumbnailLink, createdTime, size)"
    
    items = []
    page_token = None
    while True:
        res = service.files().list(q=cq, fields=fields, pageToken=page_token, pageSize=100).execute()
        items.extend(res.get('files', []))
        page_token = res.get('nextPageToken')
        if not page_token:
            break
            
    files = []
    subfolders = []
    for item in items:
        if item.get('mimeType') == 'application/vnd.google-apps.folder':
            subfolders.append(item)
        else:
            item['folder_path'] = current_path
            files.append(item)
            
    for sf in subfolders:
        sub_files = list_folder_recursive(sf['id'], sf['name'], current_path)
        files.extend(sub_files)
        
    return files

all_data = {}
for root_name in ["15_aug", "15.08"]:
    fq = f"mimeType = 'application/vnd.google-apps.folder' and name = '{root_name}' and trashed = false"
    f_res = service.files().list(q=fq, fields="files(id, name)").execute()
    folders = f_res.get('files', [])
    for f in folders:
        all_data[root_name] = list_folder_recursive(f['id'], root_name)

with open("all_drive_media_recursive.json", "w", encoding="utf-8") as out:
    json.dump(all_data, out, indent=2)

print("\n--- Summary ---")
for k, v in all_data.items():
    print(f"Total files in {k}: {len(v)}")
