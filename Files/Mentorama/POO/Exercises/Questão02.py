class Quadrado:
    def __init__(self,lado):
        self.lado = lado

    def mudarlado(self,novolado):
        self.lado = novolado
        print(f'O novo lado do quadrado é {novolado}')
    def retornarlado(self):
        return print(f'O lado do quadrado é: {self.lado}')

    def area(self):
        print(f'A aréa do quadrado é: {self.lado * self.lado}mt²')

