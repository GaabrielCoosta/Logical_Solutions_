def leiaint(msg):
    while True:
        try:
            nu = int(input(msg))
        except (ValueError,TypeError):
            print(f'\033[1:31mTivemos um problema com os tipos de dados que voçê digitou.\033[m')
        else:
            return nu

def cabecalho(txt):
    print('-'*42)
    print(f'\033[1:34m{txt:^42}\033[m')
    print('-'*42)



def menu(lista):
    cabecalho('MENU PRINCIPAL')
    for x in range (1,len(lista)+1):
        print(f'{x} - {lista[x-1]}')
    b = leiaint('Sua opção: ')
    return b

