class contacorrente:
    def __init__(self,numerodaconta,nomedocorrentista,saldo=0):
        self.numerodaconta = numerodaconta
        self.nomedocorrentista = nomedocorrentista
        self.saldo = saldo

    def mudarnome(self,nome):
        self.nomedocorrentista = nome

    def deposito(self,deposito):
        self.saldo = self.saldo + int(deposito)
        
    def saque(self,saque):
        self.saldo = self.saldo - int(saque)