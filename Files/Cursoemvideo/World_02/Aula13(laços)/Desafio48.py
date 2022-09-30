pares=[]
i=[]
for x in range(1,500):
    if x % 2 == 0:
        pares.append(x)
    else:
        if x % 3 == 0:
            i.append(x)

print("A soma dos números impares multiplos de 3 é: {}".format(sum(i)))

