lista = ()
cont = 0
pares = ()
for x in range(0,4):
    n = int(input("Digite um número qualquer: "))
    lista += (n,)
    if n == 9:
        cont += 1
    if n % 2 == 0:
        pares += (n,)
if 3 in lista:
    print(f"O número três se encontra na posição {lista.index(3)}")
print(f"Essa foi a lista de número digitados -> {lista}")
print(f"O número de ocorrências em que o número 9 foi digitado: {cont}")
print(f"Esses foram os números pares digitados: {pares}")