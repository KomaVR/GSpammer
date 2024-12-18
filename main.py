import os
import platform
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import time
from colorama import init, Fore, Style

init(autoreset=True)

def clear_screen():
    system = platform.system().lower()
    if system == 'windows':
        os.system('cls')  
    else:
        os.system('clear') 
def print_title():
    title = f"""
{Fore.CYAN}  __|   __|                                     
{Fore.CYAN} (_ | \\__ \\  _ \\   _` |   ` \\    ` \\    -_)   _|
{Fore.CYAN}\\___| ____/ .__/ \\__,_| _|_|_| _|_|_| \\___| _|  
{Fore.CYAN}           _|                                   
{Fore.GREEN}by Koma
    """
    print(title)

def send_email_via_outlook(sender_email, app_password, recipient_email, subject, body):
    try:
        server = smtplib.SMTP('smtp.office365.com', 587)
        server.starttls() 
        server.login(sender_email, app_password) 

        message = MIMEMultipart()
        message['From'] = sender_email
        message['To'] = recipient_email
        message['Subject'] = subject
        message.attach(MIMEText(body, 'plain'))

        text = message.as_string()
        server.sendmail(sender_email, recipient_email, text)
        print(f"{Fore.GREEN}Email sent successfully to {recipient_email}")

        server.quit()

    except smtplib.SMTPException as e:
        print(f"{Fore.RED}Failed to send email: {e}")
    except Exception as e:
        print(f"{Fore.RED}An unexpected error occurred: {e}")

def main():
    clear_screen()
    print_title()

    sender_email = input(f"{Fore.YELLOW}Enter your Outlook email address: ")
    app_password = input(f"{Fore.YELLOW}Enter your Outlook App Password (if 2FA enabled): ")
    recipient_email = input(f"{Fore.YELLOW}Enter recipient's email address: ")
    subject = input(f"{Fore.YELLOW}Enter the subject of the email: ")
    body = input(f"{Fore.YELLOW}Enter the email body: ")
    send_count = int(input(f"{Fore.YELLOW}How many emails would you like to send? "))
    delay = int(input(f"{Fore.YELLOW}Enter the delay between emails in seconds: "))

    for i in range(send_count):
        print(f"{Fore.CYAN}Sending email {i+1} of {send_count}...")
        send_email_via_outlook(sender_email, app_password, recipient_email, subject, body)
        time.sleep(delay)

if __name__ == '__main__':
    main()
