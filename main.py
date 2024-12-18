import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from time import sleep

def send_email_via_gmail(sender_email, app_password, recipient_email, subject, body):
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()  
        server.login(sender_email, app_password) 
        message = MIMEMultipart()
        message['From'] = sender_email
        message['To'] = recipient_email
        message['Subject'] = subject
        message.attach(MIMEText(body, 'plain'))

        text = message.as_string()
        server.sendmail(sender_email, recipient_email, text)
        print(f"Email sent successfully to {recipient_email}")
        server.quit()

    except Exception as e:
        print(f"Failed to send email: {e}")

def main():
    sender_email = input("Enter your Gmail email address: ")
    app_password = input("Enter your Gmail App Password (if 2FA enabled): ")  # Use App Password here
    recipient_email = input("Enter recipient's email address: ")
    subject = input("Enter the subject of the email: ")
    body = input("Enter the email body: ")

    send_count = int(input("How many emails would you like to send? "))
    delay = int(input("Enter the delay between emails in seconds: "))

    for i in range(send_count):
        print(f"Sending email {i + 1} of {send_count}...")
        send_email_via_gmail(sender_email, app_password, recipient_email, subject, body)
        if i < send_count - 1:
            sleep(delay)  

    print("All emails have been sent!")

if __name__ == '__main__':
    main()
