from drive_mcp_server import get_drive_service
import json

service = get_drive_service()
for folder_name in ["15_aug", "15.08"]:
    fq = f"mimeType = 'application/vnd.google-apps.folder' and name = '{folder_name}' and trashed = false"
    f_res = service.files().list(q=fq, fields="files(id, name)").execute()
    for f in f_res.get('files', []):
        perms = service.permissions().list(fileId=f['id']).execute()
        print(f"Folder: {f['name']} (ID: {f['id']})")
        print("  Permissions:", json.dumps(perms, indent=2))
