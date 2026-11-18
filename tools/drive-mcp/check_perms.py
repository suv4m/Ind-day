from drive_mcp_server import get_drive_service
import json

service = get_drive_service()
sample_id = "1p7SV6z8gJJ9ADpQKld3DVxFvCqlGSwAf"
perms = service.permissions().list(fileId=sample_id).execute()
print("Permissions:", json.dumps(perms, indent=2))
