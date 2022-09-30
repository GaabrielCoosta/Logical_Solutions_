from time import sleep
def maior(*n):
    cont = maior = 0
    print('=-='*20)
    print('Analisando valores...')
    for x in n:
        print(f'{x}',end=" ")
        sleep(0.3)
        if cont == 0:
            maior = x
        else:
            if x > maior:
                maior = x
        cont += 1
    print(f'Foram informados {cont} valores ao todo.')
    print(f'O maior valor passado foi o {maior}.')


maior(2,9,4,5,7,1)
maior(4,7,0)
maior()