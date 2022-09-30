print("{:^30}".format("BANCO DO GABRIEL"))
print("\033[1:34m=*=\033[m"*12)
valor=int(input('INFORME O VALOR QUE DESEJA SACAR: '))

total = valor
ced = 50
totced = 0
while True:
    if total >= ced:
        total-= ced
        totced += 1
    else:
        if totced>0:
            print(f"O total de {totced} cédulas de R${ced}")
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if total == 0:
            break
print("\033[1:34m=*=\033[m"*12)
print("Volte sempre!")








