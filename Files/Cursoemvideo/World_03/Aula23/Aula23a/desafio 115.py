from Cursoemvideo.Mundo03.Aula23.Aula23a.modulos import Interface
from Cursoemvideo.Mundo03.Aula23.Aula23a.modulos import arquivo

arq = 'Cursoemvideo.txt'
if not arquivo.arqExiste(arq):
    arquivo.criarArquivo(arq)

while True:
    resposta = Interface.menu(['Ver Pessoas', 'Cadastrar Pessoas', 'Sair do Sistema'])
    if resposta == 1:
        arquivo.leiaArq(arq)
    elif resposta == 2:
        Interface.cabecalho('CADASTRAR PESSOAS')
        nome = str(input("Nome: "))
        idade = Interface.leiaint('Idade: ')
        arquivo.cadastrar(arq,nome,idade)
    elif resposta == 3:
        Interface.cabecalho('\033[1:31mSair do Sistema\033[m')
        break
    else:
        print("\033[1:31mErro! Digite uma opção válida!\033[m")
