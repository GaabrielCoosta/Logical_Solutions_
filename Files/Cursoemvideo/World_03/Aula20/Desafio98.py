from time import sleep
def titulo(txt):
    print('=-'*20)
    print(txt)


def contador(i,f,p):
    titulo(f'Contagem de {i} até {f} de {p} em {p}.')
    if i < f:
        c = i
        while c <= f:
            print(f'{c}',end=" ")
            sleep(0.5)
            c += p
        print("FIM!")
    else:
        c = i
        while c >= f:
            print(f'{c}',end=" ")
            sleep(0.5)
            c -= p
        print('FIM!')
contador(0,10,1)
contador(10,0,2)
titulo(f'Personalise sua contagem!')
i=int(input('Início: '))
f=int(input('Fim: '))
p=int(input('Passo: '))
contador(i,f,p)

