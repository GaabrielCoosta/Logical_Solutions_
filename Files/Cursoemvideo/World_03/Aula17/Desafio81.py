lista=[]
p = int(input("Digite um valor: "))
lista.append(p)
print("Valor adicionado...")
while True:
    pa = str(input("Ainda deseja adicionar algum valor? [S|N]: ")).strip().upper()
    if pa != 'S' and pa != "N":
        print("\033[1:31mErro de digitação...\033[m")
    if pa == "N":
        break
    if pa == "S":
        p = int(input("Digite o outro valor: "))
        lista.append(p)
        print("Valor adicionado...")
b = sorted(lista)
b.reverse()
print(f"Foram adicionado {len(lista)} números!")
print(f"Essa é a lista em ordem decrescente {b}")
if 5 in lista:
    print("O valor 5 está contido na lista!")
else:
    print("O valor 5 não foi digitado, e por isso não se encontra na lista!")