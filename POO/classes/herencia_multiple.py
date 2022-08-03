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


class ClaseB:
    def __init__(self, valor2):
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
        return f'"Valor B:", {self.valor_b}'


class ClaseC(ClaseA, ClaseB):
    def __init__(self, valor, valor2):
        ClaseA.__init__(self, valor)
        ClaseB.__init__(self, valor2)

    def display_values(self):
        return f'''
        {f'"Valor A:", {self.valor_a}'.center(50, '-')}
        {f'"Valor B:", {self.valor_b}'.center(50, '_')}
        '''


if __name__ == '__main__':
    clase_c = ClaseC('hola', 'mundo')

    print(clase_c.display_values())
