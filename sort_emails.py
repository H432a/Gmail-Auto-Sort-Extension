# sort_emails.py - Sort emails based on sender

from fetch_emails import fetch_emails

def sort_emails():
    emails = fetch_emails()
    categories = {
        "work": [],
        "personal": [],
        "spam": []
    }
    
    for email_id, sender in emails:
        if "@company.com" in sender:
            categories["work"].append(email_id)
        elif "@gmail.com" in sender:
            categories["personal"].append(email_id)
        else:
            categories["spam"].append(email_id)
    
    return categories

if __name__ == "__main__":
    sorted_emails = sort_emails()
    print("Sorted Emails:")
    for category, email_ids in sorted_emails.items():
        print(f"{category}: {email_ids}")
