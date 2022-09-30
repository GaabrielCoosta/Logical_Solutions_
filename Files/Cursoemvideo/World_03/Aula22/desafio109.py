from modulos import moeda


num = float(input('Digite um número: '))
print(f'O valor digitado foi {moeda.moeda(num)}')
print(f'Esse é o dobro do seu valor:{(moeda.dobro(num, True))}')
print(f'Essa é a metade do valor: {(moeda.metade(num, True))}')
print(f'Aumentando 10%, fica: {(moeda.maisporc(num,10 , True))}')
print(f'Diminuindo 10% fica: {moeda.menosporc(num,10, True)}')
