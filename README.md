# Gmail-Auto-Sort-Extension

This script automatically sorts Gmail emails into categories based on the sender's email ID using the **Gmail API** and **OAuth 2.0**.

## Features
- Uses Gmail API to fetch and label emails.
- OAuth 2.0 authentication for secure access.
- Custom sorting logic based on sender email.

## Tech Stack
- Python
- Gmail API
- OAuth 2.0

## Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/gmail-auto-sort.git
   ```
2. Install dependencies:
   ```sh
   pip install --upgrade google-auth google-auth-oauthlib google-auth-httplib2 googleapiclient
   ```
3. Set up OAuth:
   - Go to the [Google Cloud Console](https://console.cloud.google.com/)
   - Create a new project and enable the **Gmail API**
   - Create **OAuth Client ID** and download `credentials.json`
   - Place `credentials.json` in the project folder

## Running the Script
1. Authenticate with Google:
   ```sh
   python oauth.py
   ```
2. Fetch and sort emails:
   ```sh
   python fetch_emails.py
   ```

## How It Works
- **oauth.py**: Handles OAuth authentication.
- **fetch_emails.py**: Retrieves emails.
- **sort_emails.py**: Sorts emails based on sender.
- **apply_label.py**: Applies labels to emails.
