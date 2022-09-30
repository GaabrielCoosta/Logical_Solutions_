from modulos import moeda


num = float(input('Digite um número: '))
print(f'O valor digitado foi {moeda.moeda(num)}')
print(f'Esse é o dobro do seu valor:{moeda.moeda(moeda.dobro(num))}')
print(f'Essa é a metade do valor: {moeda.moeda(moeda.metade(num))}')
print(f'Aumentando 10%, fica: {moeda.moeda(moeda.maisporc(num,10))}')

