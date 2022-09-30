from modulos import moeda

num = float(input('Digite um número: '))
print(f'O valor digitado foi R${num:.2f}')
print(f'Esse é o dobro do seu valor: R${moeda.dobro(num):.2f}')
print(f'Essa é a metade do valor: R${moeda.metade(num):.2f}')
print(f'Aumentando 10%, fica: R${moeda.maisporc(num,10):.2f}')

print(moeda.moeda(num))

