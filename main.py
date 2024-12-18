import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import time

sender_email = input("Enter your email: ")
sender_password = input("Enter your password: ")
recipient_email = input("Enter recipient's email: ")
subject = input("Enter subject: ")
body = input("Enter message: ")
send_count = int(input("How many emails to send: "))
delay = int(input("Delay between emails (in seconds): "))

message = MIMEMultipart()
message["From"] = sender_email
message["To"] = recipient_email
message["Subject"] = subject
message.attach(MIMEText(body, "plain"))

try:
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(sender_email, sender_password) 
    
    print("Starting email sending loop...")
    for i in range(send_count):
        server.send_message(message)
        print(f"Email {i + 1} sent successfully!")
        time.sleep(delay) 

    print("All emails sent successfully!")
except Exception as e:
    print(f"Failed to send email: {e}")
finally:
    server.quit()
