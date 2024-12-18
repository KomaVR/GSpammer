from __future__ import print_function
import os
import base64
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from email.mime.text import MIMEText
from time import sleep

# If modifying these SCOPES, delete the token.json file
SCOPES = ['https://www.googleapis.com/auth/gmail.send']

def authenticate():
    """Authenticate the user and return a service object for Gmail API."""
    creds = None
    # The token.json file stores the user's access and refresh tokens.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no valid credentials available, request login.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    return build('gmail', 'v1', credentials=creds)

def create_message(sender, recipient, subject, body):
    """Create a MIMEText email."""
    message = MIMEText(body)
    message['to'] = recipient
    message['from'] = sender
    message['subject'] = subject
    raw = base64.urlsafe_b64encode(message.as_bytes()).decode()
    return {'raw': raw}

def send_email(service, sender, recipient, subject, body):
    """Send an email using the Gmail API."""
    try:
        message = create_message(sender, recipient, subject, body)
        send_message = service.users().messages().send(userId="me", body=message).execute()
        print(f"Email sent successfully! Message ID: {send_message['id']}")
    except HttpError as error:
        print(f"An error occurred: {error}")

def main():
    service = authenticate()
    sender_email = input("Enter your Gmail address: ")
    recipient_email = input("Enter recipient's email: ")
    subject = input("Enter the subject of the email: ")
    body = input("Enter the email body: ")
    send_count = int(input("How many emails to send: "))
    delay = int(input("Delay between emails (in seconds): "))

    for i in range(send_count):
        print(f"Sending email {i + 1} of {send_count}...")
        send_email(service, sender_email, recipient_email, subject, body)
        if i < send_count - 1:
            sleep(delay)
    print("All emails sent!")

if __name__ == '__main__':
    main()
