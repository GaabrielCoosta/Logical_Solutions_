while True:
    n = int(input("Digite um número e veja sua tabuada: "))
    if n < 0:
        break
    for x in range(1,11):
        t = n*x
        print(f"{n} x {x} = {t}")
print("Você digitou um número negativo!")
print("\033[1:34m===FIM===\033[m")