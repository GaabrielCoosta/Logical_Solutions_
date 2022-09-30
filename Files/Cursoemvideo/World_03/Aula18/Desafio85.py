lista = [[],[]]

while True:
    while (len(lista[1])+len(lista[0]))<7:
        for x in range(0,7):
            n = int(input(f"Digite {x+1}° número: "))
            if n % 2 == 0:
                lista[0].append(n)
            else:
                lista[1].append(n)
        print(f"Os valores em ordem crescente pares: {sorted(lista[0])}")
        print(f"Os valores em ordem crescente impares: {sorted(lista[1])}")
    if (len(lista[1])+len(lista[0])) == 7:
        break


