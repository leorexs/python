import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from os.path import basename

from dotenv import load_dotenv

load_dotenv()


class SenderEmail:
    def __init__(self, mensaje=''):
        self.__email = os.getenv("REPORT_EMAIL_ADDRESS")
        self.__password = os.getenv("REPORT_EMAIL_PASSWORD")
        self.__smtp_server = os.getenv("SMTP_SERVER")
        self.__smtp_port = os.getenv("SMTP_PORT")
        self.__mensaje = mensaje

    @property
    def email(self):
        return self.__email

    @property
    def password(self):
        return self.__password

    @property
    def smtp_server(self):
        return self.__smtp_server

    @property
    def smtp_port(self):
        return self.__smtp_port

    @property
    def mensaje(self):
        return self.__mensaje

    @mensaje.setter
    def mensaje(self, value):
        self.__mensaje = value

    def construir_mensaje_email(self, filename=None):
        msg = MIMEMultipart()
        msg["From"] = f'{self.email}'
        msg["To"] = f'{self.email}'
        msg["Subject"] = "Reporte de Logg de usuario Infectado"
        html = f"<p>{self.mensaje}</p>"
        text_part = MIMEText(self.mensaje, "plain")
        html_part = MIMEText(html, "html")
        msg.attach(text_part)
        msg.attach(html_part)
        if filename:

            with open(file=f'./Log/{filename}', mode='r') as f:
                part = MIMEApplication(f.read(), Name=basename(filename))

            part['Content-Disposition'] = 'attachment; filename="{}"'.format(basename(filename))
            msg.attach(part)

        return msg.as_string()

    def enviar_email(self, message):
        servidor = smtplib.SMTP(host=f'{self.smtp_server}', port=int(self.smtp_port))
        servidor.login(self.email, self.password)
        servidor.sendmail(self.email, self.email, message)
        servidor.quit()


if __name__ == '__main__':
    email = SenderEmail("Hola mundo")
    msg = email.construir_mensaje_email()
    print(msg)
    email.enviar_email()

