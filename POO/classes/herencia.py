class ClaseA:
    def __init__(self, valor):
        self._valor_a = valor

    @property
    def valor_a(self):
        return self._valor_a

    @valor_a.setter
    def valor_a(self, valor):
        self._valor_a = valor

    def imprimir_a(self):
        return f'"Valor A:", {self.valor_a}'

    def display_values(self):
        return f'"Valor A:", {self.valor_a}'


class ClaseB(ClaseA):
    def __init__(self, valor, valor2):
        super().__init__(valor)
        self._valor_b = valor2

    @property
    def valor_b(self):
        return self._valor_b

    @valor_b.setter
    def valor_b(self, valor):
        self._valor_b = valor

    def imprimir_b(self):
        return f'"Valor A:", {self.valor_b}'

    def display_values(self):
        return f'''"
        Valor A:", {self.valor_a}
        Valor B:", {self.valor_b}
        '''


if __name__ == '__main__':
    instancia_a = ClaseA(10)
    print("Valor A:", instancia_a.valor_a)
    print(instancia_a.display_values())

    instancia_b = ClaseB('hola', 'mundo')
    print(instancia_b.imprimir_a())
    print(instancia_b.display_values())
    print(instancia_b.__class__.__subclasses__())
