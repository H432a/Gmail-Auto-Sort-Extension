# apply_label.py - Apply labels to sorted emails

from googleapiclient.discovery import build
from oauth import authenticate
from sort_emails import sort_emails

def apply_labels():
    creds = authenticate()
    service = build('gmail', 'v1', credentials=creds)
    sorted_emails = sort_emails()
    
    label_map = {
        "work": "Work",
        "personal": "Personal",
        "spam": "Spam"
    }
    
    for category, email_ids in sorted_emails.items():
        label_name = label_map.get(category)
        if not label_name:
            continue
        
        for email_id in email_ids:
            service.users().messages().modify(
                userId='me', 
                id=email_id, 
                body={'addLabelIds': [label_name]}
            ).execute()
            print(f"Applied label '{label_name}' to email {email_id}")

if __name__ == "__main__":
    apply_labels()
