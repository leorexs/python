from VehiculoABC import (
    Vehiculo,
)


class Automovil(Vehiculo):

    def __init__(self, color, marca, modelo, oficio, motor=False, acelerador=False, freno=False):
        super().__init__(color, marca, modelo)
        self.__actividad = oficio
        self.__ruedas = 4
        self.__motor = motor
        self.__acelerador = acelerador
        self.__freno = freno

    @property
    def modelo(self):
        return self.__modelo

    @modelo.setter
    def modelo(self, modelo):
        self.__modelo = modelo

    @property
    def actividad(self):
        return self.__actividad

    @actividad.setter
    def actividad(self, actividad):
        self.__actividad = actividad

    @property
    def ruedas(self):
        return self.__ruedas

    @ruedas.setter
    def ruedas(self, ruedas):
        self.__ruedas = ruedas

    @property
    def motor(self):
        return self.__motor

    @motor.setter
    def motor(self, motor):
        self.__motor = motor

    @property
    def acelerador(self):
        return self.__acelerador

    @acelerador.setter
    def acelerador(self, acelerador):
        self.__acelerador = acelerador

    @property
    def freno(self):
        return self.__freno

    @freno.setter
    def freno(self, freno):
        self.__freno = freno

    def arrancar(self, value):
        if value:
            if not self.motor:
                self.motor = True
                if self.motor:
                    self.acelerador = True
                    self.freno = False
                return True
            return False
        return False

    def apagar(self, value):
        if value:
            if self.motor:
                self.acelerador = False
                self.freno = True
                self.motor = False
                if not self.motor:
                    self.freno = False
                return True
            else:
                return False
        return False

    def acelerar(self, value):
        if self.motor:
            if value:
                self.freno = False
                self.acelerador = True
                return True
            else:
                return False
        return False

    def frenar(self, value):
        if self.motor:
            if value:
                self.acelerador = False
                self.freno = True
                return True
            else:
                return False
        return False

    def __str__(self):
        return "Automovil: {}  {}".format(self.marca, self.color)


if __name__ == "__main__":
    taxi = Automovil("Rojo", "Chevrolet", "Bentayga", 'taxi')
    print('Object: ', taxi.__dict__)
    print('Arrancar: 0', taxi.arrancar(0))
    print(taxi.__dict__)
    print('Arrancar: 1', taxi.arrancar(1))
    print(taxi.__dict__)
    print('Apagar 1', taxi.apagar(1))
    print(taxi.__dict__)
    print('Acelerar: 1', taxi.acelerar(1))
    taxi.arrancar(1)
    print(taxi.acelerar(1))
    print('Acelerar: 1', taxi.__dict__)
    print('Frenar: 0', taxi.frenar(0))
    print('Frenar: 0', taxi.__dict__)
    print('Frenar: 1', taxi.frenar(1))
    print('Frenar: 1', taxi.__dict__)
    print('Apagar: 1', taxi.apagar(1))
    print('Apagar: 1', taxi.__dict__)




