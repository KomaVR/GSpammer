import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from time import sleep
import os
from colorama import init, Fore, Style

init(autoreset=True)

title_art = '''
  __|   __|                                     
 (_ | \__ \  _ \   _` |   ` \    ` \    -_)   _|
\___| ____/ .__/ \__,_| _|_|_| _|_|_| \___| _|  
           _|                                   
               by Koma
'''

def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

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
        print(Fore.GREEN + f"Email sent successfully to {recipient_email}")
        server.quit()

    except Exception as e:
        print(Fore.RED + f"Failed to send email: {e}")

def main():
    clear_screen()
    print(Style.BRIGHT + Fore.MAGENTA + title_art)

    sender_email = input(Fore.CYAN + "Enter your Gmail email address: ")
    app_password = input(Fore.CYAN + "Enter your Gmail App Password (if 2FA enabled): ")
    recipient_email = input(Fore.CYAN + "Enter recipient's email address: ")
    subject = input(Fore.CYAN + "Enter the subject of the email: ")
    body = input(Fore.CYAN + "Enter the email body: ")

    send_count = int(input(Fore.YELLOW + "How many emails would you like to send? "))
    delay = int(input(Fore.YELLOW + "Enter the delay between emails in seconds: "))

    for i in range(send_count):
        print(Fore.YELLOW + f"Sending email {i + 1} of {send_count}...")
        send_email_via_gmail(sender_email, app_password, recipient_email, subject, body)
        if i < send_count - 1:
            sleep(delay)

    print(Fore.GREEN + "All emails have been sent!")

if __name__ == '__main__':
    main()
