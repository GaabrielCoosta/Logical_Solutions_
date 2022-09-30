from random import randint
from time import sleep
numeros = []
def sorteia():
    print(f'Sorteando 5 valores da lista: ',end=' ')
    for x in range(0,5):
        n = randint(0,100)
        numeros.append(n)
        print(f'{n}',end=" ")
        sleep(0.3)
    print('PRONTO!')


def somapar():

    par = []
    for x in numeros:
        if x % 2 == 0:
            par.append(x)
    print(f'Somando dos valores pares de {numeros}, temos ', end='')
    print(sum(par))


sorteia()
somapar()