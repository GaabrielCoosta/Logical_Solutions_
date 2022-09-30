def leiaint(msg):
    while True:
        nu = str(input('Digite um número: '))
        if nu.isnumeric():
            nu = int(nu)
            break

        else:
            print('\033[1:31mErro! Digite um número inteiro!\033[m')
    return nu

n = leiaint('Digite um número: ')
print(f'Você acabou de digitar o número {n}.')