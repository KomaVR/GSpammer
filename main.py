import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from time import sleep

def send_email_via_outlook(sender_email, sender_password, recipient_email, subject, body):
    try:
        # Set up the Outlook server
        server = smtplib.SMTP('smtp.office365.com', 587)
        server.starttls()  # Encrypts the connection
        server.login(sender_email, sender_password)

        # Compose the email
        message = MIMEMultipart()
        message['From'] = sender_email
        message['To'] = recipient_email
        message['Subject'] = subject
        message.attach(MIMEText(body, 'plain'))

        # Send the email
        text = message.as_string()
        server.sendmail(sender_email, recipient_email, text)
        print(f"Email sent successfully to {recipient_email}")
        server.quit()

    except Exception as e:
        print(f"Failed to send email: {e}")

def main():
    sender_email = input("Enter your Gmail address: ")
    sender_password = input("Enter your Gmail password (App Password if 2FA is enabled): ")
    recipient_email = input("Enter recipient's email address: ")
    subject = input("Enter the subject of the email: ")
    body = input("Enter the email body: ")

    # Input the number of emails to send and the delay in between
    send_count = int(input("How many emails would you like to send? "))
    delay = int(input("Enter the delay between emails in seconds: "))

    for i in range(send_count):
        print(f"Sending email {i + 1} of {send_count}...")
        send_email_via_outlook(sender_email, sender_password, recipient_email, subject, body)
        if i < send_count - 1:
            sleep(delay)  # Delay between sends

    print("All emails have been sent!")

if __name__ == '__main__':
    main()
