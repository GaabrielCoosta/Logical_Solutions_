from random import randint
lista = ()
d = ()
for x in range(0,5):
    c=randint(0,100)
    lista += (c,)
crescente= sorted(lista)
for x in range(0,5):
    d += (crescente[x],)


print(lista)
print(crescente)
print(d)
print(f"O menor número sorteado foi o {d[0]}, e o maior número sorteado foi o {d[-1]}.")