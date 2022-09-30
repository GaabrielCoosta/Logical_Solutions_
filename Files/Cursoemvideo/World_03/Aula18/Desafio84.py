print("CADASTRO DE PESSOAS E SEUS RESPECTIVOS PESOS")
print("=-="*15)
lista=[]
lt = []
pesados = 0
leves = 0

while True:
    lt.append(str(input("Digite um nome: ")))
    lt.append(float(input("Digite o peso: ")))
    if len(lista) == 0:
        pesados = leves = lt[1]
    else:
        if lt[1] > pesados:
            pesados = lt[1]
        if lt[1] < pesados:
            leves = lt[1]
    lista.append(lt[:])
    lt.clear()
    pa = str(input("Deseja continuar? [S|N]: ")).strip().upper()
    if pa == "N":
        break
print("=-="*15)
print(f"Ao todo foram cadastradas {len(lista)} pessoas.")
print(f"A(s) pessoa(s) mais pesada(s) tinha(m) {pesados} kg.")
print("\033[1:31mA lista do(s) mais pesado(s):\033[m", end="\n")

for p in lista:
    if p[1] == pesados:
        print(f"{p[0]}")
print("=-="*15)
print(f"A(s) pessoa(s) mais leve(s) tinha(m) {leves} kg.")
print("\033[1:34mA lista do(s) mais leves(s):\033[m", end="\n")
for p in lista:
    if p[1] == leves:
        print(f"{p[0]}")
print("=-="*15)
print(f"\033[1:31mFIM\033[m")
