class Tv:
    def __init__(self,canal,volume):
        self.canal = int(canal)
        self.volume = int(volume)

    def aumentar(self,aumentar):
        self.volume = int(aumentar) + self.volume
        if self.volume > 100:
            print(f"Volume: {self.volume}")
            print("\033[1:31mLimite máximo ultrapassado!\033[m")

    def diminuir(self,diminuir):
        self.volume = self.volume - int(diminuir)
        if self.volume < 0:
            print(f"Volume: {self.volume}")
            print("\033[1:31mLimite minimo ultrapassado!\033[m")
