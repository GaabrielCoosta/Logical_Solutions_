def leiaint(msg):
    while True:
        try:
            nu = int(input(msg))
        except (ValueError,TypeError):
            print(f'Tivemos um problema com os tipos de dados que voçê digitou.')
        else:
            print(f'Você digitou o número {nu}')
            break