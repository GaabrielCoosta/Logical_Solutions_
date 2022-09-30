class BombaDeCombustivel:
    def __init__(self,tipoCombustivel,valorLitro,quantidadeCombustivel):
        self.tipoCombustivel = tipoCombustivel
        self.valorLitro = float(valorLitro)
        self.quantidadeCombustivel = float(quantidadeCombustivel)

    def abastecerporvalor(self,valor):
        self.abastecerporvalor = float(valor)/self.valorLitro
        print(f"Pagando {valor} reais, o carro é abastecido com {self.abastecerporvalor:.2f} litros de {self.tipoCombustivel}.")

    def abastecerporlitro(self,litro):
        self.abastecerporlitro = float(litro)*self.valorLitro
        print(f"Abastecendo {litro} litros, você pagará R${self.abastecerporlitro:.2f}.")

    def alterarValor(self,valor):
        self.valorLitro = float(valor)
        print(f"Novo valor do combustivel é R$ {valor:.2f}")

    def alterarQuantidadeCombustivel(self,quantidade):
        self.quantidadeCombustivel = float(quantidade)
        print(f'Nova quantidade de combustivel: {quantidade} litros')

