print("\033[1:34m       VAMOS DE TABUADA?\033[m")
print("=-="*12)
n=int(input("Digite um número e veja sua tabuada: "))
for x in range(1,11):

    print("{} X {} = {}".format(n,x,(n*x)))

print("\033[1:34m=========FIM==========\033[m")