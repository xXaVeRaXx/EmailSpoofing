# Import smtplib for the actual sending function
import smtplib

# Import the email modules
from email.message import Message

def prompt(prompt):
    return input(prompt).strip()

#Attacker's email
email = input("Introduce un email que quiera simular: ")
print()

#Attacker's name
atacante = input("Introduce el nombre del atacante: ")
print()

#Victim
victima = prompt("Introduce una víctima a quién enviarle un email: ").split()
print()

#Subject
subject = input("Introduce un asunto: ")
print()

#Message
text = input("Introduce un texto: ")
print()

#Email Priority
print("Puedes escoger entre las siguientes prioridades:")
print("1. Muy alta")
print("2. Media alta")
print("3. Media")
print("4. Media baja")
print("5. Muy baja")
prioridad = input("Introduce un número de la prioridad que desea que tenga el e-mail: ")
print()

#Email X-Mailer
print("Puedes escoger diferentes X-Mailers, donde indicas de qué tipo de servidor proviene el email.")
print("Ejemplos de X-Mailer: Apple Mail, ColdFusion MX Application Server, E-Messenger, iPhone Mail, KMail, Lotus Notes, Microsoft Office Outlook, Microsoft Outlook Express, Microsoft Outlook IMO, Microsoft Windows Live Mail, Microsoft Windows Mail, Mozilla Thunderbird, Mozilla/5.0, Novell GroupWise, Novell GroupWise Internet Agent, PHP, PHPMailer, QUALCOMM Windows Eudora Version, The Bat!, Unknown (No Version), YahooMailWebService y Zimbra")
print("También puede inventarse uno a su elección, no necesariamente tiene que estar en la lista.")
XMAILER = input("Introduce un X-Mailer que desea que tenga el e-mail: ")

#Start SMTP server
server = smtplib.SMTP('localhost')
server.set_debuglevel(1)
server.ehlo()
server.starttls()

#Create email
m = Message()
m['From'] = "{}".format(atacante) + " <{}>".format(email)
m['To'] = ', '.join(victima)
m['X-Priority'] = prioridad
m['X-Mailer'] = XMAILER
m['Subject'] = subject
m.set_payload(text)

#Send email
server.sendmail(email, victima, m.as_string())

#Close SMTP server
server.quit()
