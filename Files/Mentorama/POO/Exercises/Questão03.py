class Retangulo:
    def __init__(self):
        self.base = int(input("Digite o tamanho da base do local em metros: "))
        self.altura = int(input("digite o tamanho da altura do local em metros: "))
        print(f'O local tem base: {self.base}mt e altura: {self.altura}mt ')

    def mudarlados(self,base,altura):
        self.base = base
        self.altura = altura
        print(f'O retangulo mudou para base: {self.base}mt, e para a altura: {self.altura}mt ')

    def retornarlados(self):
        return print(f'A função retorna os valores da base e da altura respectivamnte: {self.base}mt , {self.altura}mt')

    def arearetangulo(self):
        print(f'A aréa do local é igual: {self.base*self.altura}mt².\n\033[1:34mEssa é a quantidade necessária de piso em mt² para preencher o local!\033[m')

    def perimetro(self):
        print(f'O perímetro do local é igual: {self.base * self.altura}mt.\n\033[1:34mEssa é a quantidade necessária em metros de roda pé!\033[m')


