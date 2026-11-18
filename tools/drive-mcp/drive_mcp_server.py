import os
import io
import sys
import json  # Added missing import
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload

# Full drive access to allow downloads and file manipulation
SCOPES = ['https://www.googleapis.com/auth/drive']

def get_drive_service():
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    return build('drive', 'v3', credentials=creds)

def download_file(file_id, output_filename):
    """Downloads the full raw image or video binary file to your local workspace"""
    try:
        service = get_drive_service()
        request = service.files().get_media(fileId=file_id)
        fh = io.BytesIO()
        downloader = MediaIoBaseDownload(fh, request)
        
        done = False
        while done is False:
            status, done = downloader.next_chunk()
        
        # Save the downloaded binary locally for processing/editing
        with open(output_filename, 'wb') as f:
            f.write(fh.getvalue())
        return os.path.abspath(output_filename)
    except Exception as e:
        return f"Error downloading: {str(e)}"

def list_media_files(folder_name=None):
    """Queries both 'nomape' and '15.08' Google Drive folders and merges the results"""
    try:
        service = get_drive_service()
        
        # Hardcoded your two target folder names
        target_folders = ["15_aug", "15.08"] 
        all_files = []
        
        for folder in target_folders:
            # 1. Search for the folder ID by name
            folder_q = f"mimeType = 'application/vnd.google-apps.folder' and name = '{folder}' and trashed = false"
            folder_result = service.files().list(q=folder_q, fields="files(id)").execute()
            folders = folder_result.get('files', [])
            
            if not folders:
                print(f"Warning: Folder '{folder}' not found.", file=sys.stderr)
                continue # Skip to the next folder if one is missing
                
            folder_id = folders[0]['id']
            
            # 2. Get all images and videos inside this specific folder
            media_q = f"'{folder_id}' in parents and (mimeType startsWith 'image/' or mimeType startsWith 'video/') and trashed = false"
            fields = "files(id, name, mimeType, thumbnailLink, webContentLink)"
            
            results = service.files().list(q=media_q, fields=fields).execute()
            files_list = results.get('files', [])
            all_files.extend(files_list) # Combine results into a single list
            
        return {"status": "success", "files": all_files}
        
    except Exception as e:
        return {"status": "error", "message": str(e)} 

# === MCP JSON-RPC COMPLIANT COMMUNICATION ENGINE ===
if __name__ == "__main__":
    # Corrected argument slice indexing
    if len(sys.argv) > 1 and sys.argv[1] == "--auth-only":
        get_drive_service()
        print("Authenticated successfully!")
        sys.exit(0)
        
    # Main server loop: Antigravity sends JSON strings down stdin, script responds via stdout
    print("Google Drive MCP Server Active...", file=sys.stderr)
    
    for line in sys.stdin:
        try:
            request = json.loads(line)
            method = request.get("method")
            params = request.get("params", {})
            req_id = request.get("id")
            
            # Match tools called by the AI
            if method == "list_files":
                # TIP: You can replace "My Portfolio Assets" below with your actual default folder name
                folder = params.get("folder_name", "My Portfolio Assets")
                data = list_media_files(folder)
                response = {"jsonrpc": "2.0", "id": req_id, "result": data}
            
            elif method == "download_media":
                f_id = params.get("file_id")
                out_name = params.get("output_filename")
                saved_path = download_file(f_id, out_name)
                response = {"jsonrpc": "2.0", "id": req_id, "result": {"path": saved_path}}
                
            else:
                response = {"jsonrpc": "2.0", "id": req_id, "error": {"code": -32601, "message": "Method not found"}}
                
            # Send the data back up to Antigravity
            print(json.dumps(response))
            sys.stdout.flush()
            
        except Exception as e:
            err_resp = {"jsonrpc": "2.0", "error": {"code": -32603, "message": str(e)}}
            print(json.dumps(err_resp))
            sys.stdout.flush()
