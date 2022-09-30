def leiaint(msg):
    while True:
        try:
            nu = int(input(msg))
        except (ValueError,TypeError):
            print(f'\033[1:31mTivemos um problema com os tipos de dados que voçê digitou\033[m')
        else:
            print(f'Você digitou o número {nu}')
            break

def leiafloat(msg):
    while True:
        try:
            nu = float(input(msg))
        except (ValueError,TypeError):
            print(f'\033[1:31mTivemos um problema com os tipos de dados que voçê digitou\033[m')
        else:
            print(f'Você digitou o número {nu:.2f}')
            break

leiaint('Digite um valor inteiro: ')
leiafloat('Digite um valor Real: ')