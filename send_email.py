import smtplib 
__author__ = "backup_python.dev"

remitente = "email@gmail.com"  
destinatario  = "email2@gmail.com"
asunto='E-mail con Python 3'
message ="""
mensaje enviado desde python
Sigueme para mas contenido... 
ENLACE:
https://www.instagram.com/backup_python.dev/
"""
# Datos
username = 'email@gmail.com'
password = '***************'

email = """From: %s 
To: %s 
MIME-Version: 1.0 
Content-type: text/html 
Subject: %s 
%s
""" % (remitente, destinatario, asunto, message) 

# Enviando el correo
try:
    server = smtplib.SMTP('smtp.gmail.com','587')
    server.starttls()
    server.login(username,password)
    server.sendmail(remitente, destinatario, email)
    server.quit()
except:
    print("Fallo en la conexion con Gmail")
