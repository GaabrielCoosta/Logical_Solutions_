class Pessoa:
    def __init__(self,nome,idade,peso,altura):
        self.nome = nome
        self.idade = int(idade)
        self.peso = float(peso)
        self.altura = float(altura)

    def mostrarpessoa(self):
        print(f'Pessoa de nome {self.nome}, com idade de {self.idade} anos, pesando {self.peso}kg e com {self.altura}mt de altura')

    def envelhecer(self,maisidade):
        self.idade = ( int(maisidade) + self.idade)
        print(f'{self.nome} envelheceu {maisidade} anos, e agora tem {self.idade} anos')

    def engordar(self,maispeso):
        self.peso = (float(maispeso)+self.peso)
        print(f'{self.nome} engordou {maispeso}kg, e agora tem {self.peso}kg.')

    def emagrecer(self, menospeso):
        self.peso = (float(menospeso) + self.peso)
        print(f'{self.nome} emagreceu {menospeso}kg, e agora tem {self.peso}kg.')

    def crescer(self,maisaltura):
        self.altura = (float(maisaltura)+self.altura)
        print(f'{self.nome} cresceu {maisaltura}mt, e agora tem {self.peso}mt.')
