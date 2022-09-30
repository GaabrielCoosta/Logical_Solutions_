print("           VERIFICANDO PESOS")
print("\033[1:34m=-=\033[m"*14)

p = []
for x in range(0,5):
    peso=float(input("Digite aqui o seu peso: "))
    p.append(peso)
p.sort()
print("A pessoa com menor peso tem {}kg".format(p[0]))
print("A pessoa com maior peso tem {}kg".format(p[-1]))
print("\033[1:34m=-=\033[m"*14)