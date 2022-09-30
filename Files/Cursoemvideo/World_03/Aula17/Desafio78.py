lista=[]
p=0
maior = 0
while p < 5:
    l= int(input("Digite um valor: "))
    lista.append(l)
    p += 1
    if l > maior:
        maior = l
s = sorted(lista)
print(lista)
print(f"O menor valor digitado foi {s[0]}")
print(f"O maior valor digitado foi {maior}")
if maior in lista:
    print(f"A posição do maior número é a {lista.index(maior)}")
if s[0] in lista:
    print(f"A posição do menor número é a {lista.index(s[0])}")