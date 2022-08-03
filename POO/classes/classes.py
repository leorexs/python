
class MiClaseDefinida:
    pass


class MiClaseDefinida2:
    atributo_de_clase = "valor1"

    def obtener_atributo(self):
        return self.atributo_de_clase

    def cambiar_atributo(self, valor):
        self.atributo_de_clase = valor




class MiClaseDefinida3:
    __atributo_de_clase = "clase"

    def __init__(self, valor):
        self._atributo_de_instancia = valor

    def obtener_atributo_clase(self):
        return self.__atributo_de_clase

    def cambiar_atributo_clase(self, valor):
        self.__atributo_de_clase = valor

    @property
    def atributo_de_instancia(self):
        return self._atributo_de_instancia

    @atributo_de_instancia.setter
    def atributo_de_instancia(self, valor):
        self._atributo_de_instancia = valor


    def obtener_atributo_instancia(self):
        return self._atributo_de_instancia

    def cambiar_atributo_instancia(self, valor):
        self._atributo_de_instancia = valor

