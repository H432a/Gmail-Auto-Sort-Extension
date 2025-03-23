# fetch_emails.py - Retrieves emails from Gmail

from googleapiclient.discovery import build
from oauth import authenticate

def fetch_emails():
    creds = authenticate()
    service = build('gmail', 'v1', credentials=creds)
    results = service.users().messages().list(userId='me', labelIds=['INBOX']).execute()
    messages = results.get('messages', [])
    
    if not messages:
        print("No emails found.")
        return []
    
    email_list = []
    for message in messages[:10]:  # Fetch only 10 for testing
        msg = service.users().messages().get(userId='me', id=message['id']).execute()
        headers = msg.get("payload", {}).get("headers", [])
        sender = next((h['value'] for h in headers if h['name'] == 'From'), "Unknown")
        email_list.append((message['id'], sender))
    
    return email_list

if __name__ == "__main__":
    emails = fetch_emails()
    for email in emails:
        print(f"Email ID: {email[0]} | Sender: {email[1]}")
