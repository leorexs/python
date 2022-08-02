from examples.Automovil import Automovil

class Bus(Automovil):
    def __init__(self, marca, modelo, año):
        super().__init__(marca, modelo, año)
        self.carga = []

    def cargar(self, carga):
        self.carga.append(carga)
