lista=[]
print("ADICIONANDO ELEMENTOS EM UMA LISTA")
p = int(input("Digite um número para adicionar a lista: "))
lista.append(p)
while True:
    pa = str(input("Ainda deseja adicionar um novo número?[S|N]:  ")).strip().upper()
    if pa != "S" and pa != "N":
        print("\033[1:31mErro de Digitação!\033[m")
    if pa == "N":
        break
    while pa == "S":
        pa = int(input("Digite o próximo número: "))
        if pa in lista:
            print("\033[1:31mValor duplicado! Não vou adicionar...\033[m")
        if pa not in lista:
            lista.append(pa)
            print("Número adicionado com sucesso...")
print(f"Essa é a lista de números {lista}.")
print(f"Essa é a lista de números em ordem crescente {sorted(lista)}.")
