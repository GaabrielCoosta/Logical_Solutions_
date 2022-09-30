matriz=[[],[],[]]
while True:
    while (len(matriz[0])+len(matriz[1])+len(matriz[2]))<9:
        for x in range(0,3):
            n=(int(input(f"Digite um valor para [0,{x}]: ")))
            matriz[0].append(n)

        for x in range(0,3):
            n=(int(input(f"Digite um valor para [1,{x}]: ")))
            matriz[1].append(n)

        for x in range(0,3):
            n=(int(input(f"Digite um valor para [2,{x}]: ")))
            matriz[2].append(n)
    if (len(matriz[0]) + len(matriz[1]) + len(matriz[2])) == 9:
        break
print("=-="*20)
print("[{:^5}][{:^5}][{:^5}]\n".format(matriz[0][0],matriz[0][1],matriz[0][2]),end="")
print("[{:^5}][{:^5}][{:^5}]\n".format(matriz[1][0],matriz[1][1],matriz[1][2]),end="")
print("[{:^5}][{:^5}][{:^5}]\n".format(matriz[2][0],matriz[2][1],matriz[2][2]))