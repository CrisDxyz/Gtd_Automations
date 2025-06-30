#This script was used in a real company production use case, internal monitoring and alerts.
#*it was heavily redacted for obvious reasons, so this is mostly a showcase of the general idea.

#Check the generic boilerplatey version if you want to implement it, since this one won't work
#(i erased too much but added some humor to compensate, so the world is in balance again).

import ssl, smtplib
from email.message import EmailMessage
import os 
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

#env vars
email_sender =
email_password =
email_receiver =
email_cc =
#https://learn.microsoft.com/en-us/exchange/clients-and-mobile-in-exchange-online/authenticated-client-smtp-submission

'''
para: 

cc:

asunto: 
'''

subject = 'beep boop'

body = '''


'''


####Email plain text simple
em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['Cc'] = email_cc
em['Subject'] = subject
em.set_content(body)

####Email HTML pulento

message = MIMEMultipart("alternative")
message['From'] = email_sender 
message['To'] = email_receiver
message['Cc'] = email_cc
message['Subject'] = subject

#Placeholders reemplazados por contenido y variables del otro script
s_name = 'branch_name'
ip_s = 'branch_ip'
dir_name = 'addr'
CS = 'service_code'

####Plain text
text = ("""\
Beep boop beep!

Mis antenas pichulonas han detectado una anomalía en la sucursal:

Nombre identificador de sucursal: {branch_var}
IP: {ip_var}

#Plain text por terminar

""".format(sucursal_name, sucursal_name))


# HTML part
html = """\
<html>
 <head>
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <style>
   img {
   display: block,
   margin-left: auto,
   margin-right: auto,
   }
  </style>
  <style>
   text {
   display: block;
   margin-left: auto;
   margin-right: auto;
   }
  </style>
  <style>
   p.dashed {border-style: dotted;
             style="white-space: pre-line";
             border-color: gray;
             style="text-align:center";
             width: "200";
             height: 190px;
             border-width: 2px;}
  </style>
 </head>
 <body>
  <p style="text-align:center;"><em> Beep boop beep!</em><br><br><br>

   <img src="data:image/jpg;base64,/9j/4AAQSkZJRgABAQEASABIAAD/4QAiRXhpZgAATU0AKgAAAAgAAQESAAMAAAABAAEAAAAAAAD/2wBDAAIBAQIBAQICAgICAgICAwUDAwMDAwYEBAMFBwYH
BwcGBwcICQsJCAgKCAcHCg0KCgsMDAwMBwkODw0MDgsMDAz/2wBDAQICAgMDAwYDAwYMCAcIDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwM
DAwMDAwMDAwMDAwMDAz/wAARCAC+AJYDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQID
AAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWG
h4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAA
AAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5
OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk
5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwD9/KKKKACiiigAooooAKKKKAPy5/4L+f8ABYLxV+yBq2l/CT4V30ej+Nta08arrWveWk0ujWbuyQw26uGQ
Ty7JGZ3BMcYUqC0ivH+Pugf8FBPj14Z8Wrr1j8bPiwmrJIJPPm8VXtyshGOHjlkaOReB8jqynpg9K+uf+Dm34C658Pf2/wC18c3EE0nhz4iaHaiyu9p8pLqz
XyJ7bPZgghlx3Epxna2PzoJzXZTiuU4aspcx/SP/AMEO/wDgqDf/APBRr4B6xbeLIbOH4j/D+W3tNbltI/Lg1WCcOba+WMcRtJ5MyPGvyh4WZQiuqL9v1+OP
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
KOwVQAB6CrtFFcx1hRRRQAUUUUAFFFFAH//Z">
  
   <h2 style="text-align:center;color:#cc0418">Mis antenas pichulonas han detectado una anomalía una sucursal de REDACTED BRAND:</p></h2>
   <h4 style="text-align:center;">Favor de revisar, equipo no IP caido. *Recomendación para el humano revisando el TK: reiniciar la marmota primero.</h4>

   <p style="text-align:center;">Contactos: </p>
   <p style="text-align:center;"><strong>REDACTED BRAND S.A.</strong></p>

   <p align="center">01110111 01101111 01110010 01101011 01000000 01101111 01101110 01100100 01100001 01100011 01101001 01100010 00101110 01110011 01101001 01101101 01110000 01101100 01100101 01101100 01101111 01100111 01101001 01101110 00101110 01100011 01101111 01101101</p>

   <p class="dashed"; style="text-align:center";> <br>Nombre identificador de sucursal: <strong>"""+str(sucursal_name)+"""</strong><br><br>
   Código de Servicio o BPI: <strong>"""+str(CS)+"""</strong><br><br>
   Dirección: <strong>"""+str(dir_name)+"""</strong><br><br>
   IP: <strong>"""+str(ip_sucursal)+"""</strong><br></p><br>

   <p style="text-align:center;"><strong> Registro de cmd> show ip interface brief: </strong></p>
   
   <p style="text-align:center;">Aux_siib</p>

   <p style="text-align:center;">Saludos <em>boop</em>diales</p>

  </body>
</html>

"""

contexto = ssl.create_default_context()

#"smtp-mail.outlook.com", port=587
#em.as_string()

def datos_sucursal_a_html(sn: str, ips: str, direc: str, CS: str):
    sucursal_name = sn
    ip_sucursal = ips
    dir_name = direc
    CS = CS

    html = up
    return html

def send_mail():
    with smtplib.SMTP("smtp.gmail.com", port=587) as server:
        server.starttls(context=contexto)
        server.login(email_sender, email_password)
        server.sendmail(email_sender, email_receiver, message.as_string())
        print("Correo enviado exitosamente.")
    return 0

#por adaptar
def main():
    sucursal_name="Funcion"
    ip_sucursal="pyCharm"
    dir_name="Dir_placefun"
    CS="CS_placefun"
    html=datos_sucursal_a_html(sucursal_name, ip_sucursal, dir_name, CS)
    part1 = MIMEText(text, "plain")
    part2 = MIMEText(html, "html")
    message.attach(part1)
    message.attach(part2)
    send_mail()

main()