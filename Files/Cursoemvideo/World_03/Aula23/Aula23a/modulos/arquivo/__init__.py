from Cursoemvideo.Mundo03.Aula23.Aula23a.modulos import Interface

def arqExiste(nome):
    try:
        a = open(nome, 'rt' )
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Houve um erro na criação do arquivo!')
    else:
        print(f'Arquivo {nome} criado com sucesso!')

def leiaArq(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao ler arquivo!')
    else:
        Interface.cabecalho('PESSOAS CADASTRADAS')
        for linha in a:
            dado = linha.split(';')
            dado[1]=dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')

    finally:
        a.close()

def cadastrar(arq, nome='desconhecido', idade= 0):
    try:
        a = open(arq, 'at')
    except:
        print('Houve um erro na abertura do arquivo!')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Houve um Erro na hora de escrever os dados!')
        else:
            print(f'Novo registro de \033[1:34m{nome}\033[m adicionado.')
            a.close()