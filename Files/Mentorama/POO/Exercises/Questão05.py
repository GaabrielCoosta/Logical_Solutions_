class Carro:
    def __init__(self,marca,modelo,ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano


    def mostrardados(self):
        print(f'O carro é da marca: {self.marca}, modelo {self.modelo} e do ano: {self.ano}.')

    def valor(self):
        self.valor = float(input("Quanto custa? R$ "))
        print(f'O carro {self.marca} custa R${self.valor:.2f}')
    def vender(self=False):
        if self:
            print(f"O carro {self.marca} foi vendido!")


x = Carro("Honda", "SUV", 2015)
x2 = Carro("Fiat","Hatch",2020)
x3 = Carro("Ford","Sedan",2019)
x.mostrardados()
x2.mostrardados()
x3.mostrardados()

x3.valor()
x2.vender()


