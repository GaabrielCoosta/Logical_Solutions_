lista=[]
pares=[]
impares =[]
p = int(input("Digite um valor: "))
lista.append(p)
if p % 2 == 0:
    pares.append(p)
else:
    impares.append(p)
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
        if p % 2 == 0:
            pares.append(p)
        else:
            impares.append(p)
    print("Valor adicionado...")
print("=-="*15)
print(f"Essa é a lista com os valores pares: {pares}")
print(f"Essa é a lista com os valores impares: {impares}")
print(f"Essas é a lista com todos os valores: {lista}")