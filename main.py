import smtplib

from email.message import EmailMessage

with open(archivo_texto) as lector:
    mensaje = EmailMessage()
    mensaje.set_content(lector.read())

