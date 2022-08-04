import keyboard


class KeyBoardListener:
    def __init__(self):
        self.__observer = keyboard

    @property
    def observer(self):
        return self.__observer

    def teclear(self, key):
        self.observer.send(key)

    def es_tecleado(self, key):
        return self.observer.is_pressed(f'{key}')

    def leer_tecleado_antes_de(self, key):
        return self.observer.record(f'{key}')

    def ejecutar_elementos_tecleados(self, events):
        return self.observer.play(events=events)

    def obtener_elementos_tecleados(self, events):
        return ' '.join(self.observer.get_typed_strings(events=events))

    def ejecutar_funcion_callback(self, funcion_callback):
        self.observer.on_release(callback=funcion_callback)


if __name__ == '__main__':
    import logging
    logging.basicConfig(level=logging.DEBUG)
    logging.info('Iniciando...')
    observador = KeyBoardListener()
    eventos = observador.leer_tecleado_antes_de('enter')
    observador.teclear('enter')
    lista_tecleada = observador.obtener_elementos_tecleados(eventos)
    print('\n', f'Usted escribio : {lista_tecleada}')
    logging.info('Finalizando...')
