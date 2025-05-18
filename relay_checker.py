import smtplib
import argparse
from colorama import Fore, Style, init

init(autoreset=True)

def check_open_relay(smtp_server, port, sender_email, receiver_email):
    print(Fore.CYAN + f"[+] Testing SMTP Server: {smtp_server}:{port}")
    try:
        with smtplib.SMTP(smtp_server, port, timeout=10) as smtp:
            smtp.ehlo()
            print(Fore.YELLOW + "[*] Connected and EHLO sent.")

            msg = f"""\
From: {sender_email}
To: {receiver_email}
Subject: Open Relay Test

This is a test email to check for open SMTP relay.
"""
            smtp.sendmail(sender_email, receiver_email, msg)
            print(Fore.RED + "[!] SUCCESS: Server appears to be an OPEN RELAY (email sent without auth)")
    except smtplib.SMTPRecipientsRefused:
        print(Fore.GREEN + "[+] Server refused recipient. Likely not open relay.")
    except smtplib.SMTPSenderRefused:
        print(Fore.GREEN + "[+] Server refused sender. Likely not open relay.")
    except smtplib.SMTPException as e:
        print(Fore.YELLOW + f"[!] SMTP Exception: {e}")
    except Exception as e:
        print(Fore.RED + f"[!] Connection Error: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="SMTP Open Relay Checker")
    parser.add_argument("--server", required=True, help="SMTP server (e.g., smtp.example.com)")
    parser.add_argument("--port", type=int, default=25, help="SMTP port (default: 25)")
    parser.add_argument("--sender", required=True, help="Fake sender email address")
    parser.add_argument("--receiver", required=True, help="Receiver email address")

    args = parser.parse_args()
    check_open_relay(args.server, args.port, args.sender, args.receiver)
