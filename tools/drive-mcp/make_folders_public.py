from drive_mcp_server import get_drive_service

service = get_drive_service()
new_perm = {
    'type': 'anyone',
    'role': 'reader'
}

for folder_id in ["1B89Qoj37ACF0ZBtOjpuQqvUzLf8Dhbv2", "16T1xb_Gd2fvCR8e3BdzY2HF3sGox257O"]:
    try:
        created = service.permissions().create(fileId=folder_id, body=new_perm).execute()
        print(f"Added public link permission to folder {folder_id}: {created.get('id')}")
    except Exception as e:
        print(f"Error updating {folder_id}: {e}")
