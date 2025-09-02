from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import frappe

SCOPES = ['https://www.googleapis.com/auth/drive.file']

def get_drive_service():
    creds = None

    # Token file stores the user's access and refresh tokens
    token_file = 'token.json'

    try:
        creds = Credentials.from_authorized_user_file(token_file, SCOPES)
    except Exception:
        pass

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open(token_file, 'w') as token:
            token.write(creds.to_json())

    service = build('drive', 'v3', credentials=creds)
    return service

def upload_file_to_drive(filepath, filename):
    service = get_drive_service()

    file_metadata = {'name': filename}
    media = MediaFileUpload(filepath, mimetype='application/octet-stream')
    file = service.files().create(body=file_metadata, media_body=media, fields='id').execute()
    frappe.msgprint(f'File uploaded with ID: {file.get("id")}')
    return file.get('id')
