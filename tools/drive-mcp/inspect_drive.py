import os
import json
from drive_mcp_server import get_drive_service

service = get_drive_service()
folders_to_check = ["15_aug", "15.08"]
all_items = {}

for folder_name in folders_to_check:
    fq = f"mimeType = 'application/vnd.google-apps.folder' and name = '{folder_name}' and trashed = false"
    f_res = service.files().list(q=fq, fields="files(id, name)").execute()
    folders = f_res.get('files', [])
    print(f"Folder search for '{folder_name}': Found {len(folders)} folders.")
    
    for f in folders:
        fid = f['id']
        # In Google Drive query, mimeType contains 'image/' or mimeType contains 'video/'
        # Or even simpler, query all non-trashed children in this parent:
        cq = f"'{fid}' in parents and trashed = false"
        # Let's request all useful fields: id, name, mimeType, description, webViewLink, webContentLink, thumbnailLink, createdTime, size, videoMediaMetadata, imageMediaMetadata
        fields = "nextPageToken, files(id, name, mimeType, description, webViewLink, webContentLink, thumbnailLink, createdTime, size)"
        
        children = []
        page_token = None
        while True:
            c_res = service.files().list(q=cq, fields=fields, pageToken=page_token, pageSize=100).execute()
            children.extend(c_res.get('files', []))
            page_token = c_res.get('nextPageToken')
            if not page_token:
                break
                
        all_items[f"{folder_name} ({fid})"] = children
        print(f"  -> Found {len(children)} files in {folder_name} (ID: {fid})")

with open("drive_contents.json", "w", encoding="utf-8") as out:
    json.dump(all_items, out, indent=2)

print("\nSaved full list to drive_contents.json")
