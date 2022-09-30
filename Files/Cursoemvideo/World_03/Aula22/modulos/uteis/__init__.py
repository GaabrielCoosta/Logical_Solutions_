def leiaint(msg):
    while True:
        try:
            nu = int(input(msg))
        except (ValueError,TypeError):
            print(f'Tivemos um problema com os tipos de dados que voçê digitou.')
        else:
            print(f'Você digitou o número {nu}')
            break



def cabecalho(txt):
    print('-'*30)
    print(f'{txt:^30}')
    print('-'*30)

cabecalho('Programa')


