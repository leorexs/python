from POO.examples.Automovil import Automovil


class Deportivo(Automovil):
    def __init__(self, color, marca, modelo, oficio, motor=False, acelerador=False, freno=False):
        super().__init__(color, marca, modelo, oficio, motor, acelerador, freno)
        self.__turbo = False

    @property
    def turbo(self):
        return self.__turbo

    @turbo.setter
    def turbo(self, turbo):
        self.__turbo = turbo

    def activar_turbo(self):
        self.__turbo = True
        return self.__turbo

    def desactivar_turbo(self):
        self.__turbo = False
        return self.__turbo


if __name__ == '__main__':
    deportivo = Deportivo('rojo', 'Ferrari', 'F12', 'correr', True, True, True)
    print('Object', deportivo.__dict__)
    print(deportivo.turbo)
    print(deportivo.activar_turbo())
    print('Object', deportivo.__dict__)
    print(deportivo.turbo)
    print(deportivo.desactivar_turbo())
    print('Object', deportivo.__dict__)
    print(deportivo.__class__.mro())


