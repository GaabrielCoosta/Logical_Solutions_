lista=[]

while True:
    lt = []
    lt.append(str(input("Digite o nome do aluno: ")))
    lt.append(float(input("Digite a primeira nota: ")))
    lt.append(float(input("Digite a segunda nota: ")))
    lt.append((lt[1]+lt[2])/2)
    lista.append(lt[:])
    lt.clear()

    pa = str(input("Deseja continuar cadastrando? [S|N]: ")).strip().upper()
    if pa == "N":
        break
print("=-="*15)
print(f"{'No':<4}{'Nome':<10}{'Média':>10}")
print("------------------------------------------")
for x in range(0,len(lista)):
    print(f"{x:<4}{lista[x][0]:<10}{lista[x][3]:>8.1f}")

while True:

    p = int(input("Mostrar notas de qual aluno ? (999 interrompe): "))
    if p == x:
        print(f"Notas do aluno {lista[x][0]} são {[lista[x][1],lista[x][2]]}")
        print("-----------------------------------------")
    if p == 999:
        break