
def maisporc(preço=0 ,p=0 , format=False):
    n = ((preço * p)/100) + preço
    return n if format is False else moeda(n)

def menosporc(preço=0,p=0,format=False):
    n = preço - ((preço* p)/100)
    return n if format is False else moeda(n)


def dobro(preço=0,format=False):
    n = preço*2
    return n if format is False else moeda(n)



def metade(preço=0,format=False):
    n = preço/2
    return n if format is False else moeda(n)


def moeda(preço = 0,moeda = 'R$'):
    return(f'{moeda}{preço:.2f}'.replace('.',','))

def resumo(preço=0,a = 0, d = 0):

    print('-'*30)
    print(f'Resumo de Valores'.center(30))
    print('-'*30)
    print(f'Analisando o valor: \t{moeda(preço)}')
    print(f'O dobro do valor: \t\t{dobro(preço,True)}')
    print(f'A metade do valor: \t\t{metade(preço,True)}')
    print(f'O valor com mais {a}%: \t{maisporc(preço,a,True)}')
    print(f'O valor com menos {d}%: \t{menosporc(preço,d,True)}')
    print(f'{"*** FIM ***"}'.center(30))
