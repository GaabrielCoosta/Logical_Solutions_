class Bola:
    def __init__(self, cor, circunferencia, material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material

    def trocacor(self, novacor):
        self.cor = novacor

    def mostracor(self):
        print(self.cor)

    def imprimabola(self):
        print(self.cor, self.circunferencia, self.material)