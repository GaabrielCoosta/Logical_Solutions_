soma=[]
for x in range(0,7):
    n=int(input("Digite um número inteiro: "))
    if n % 2 ==0:
        soma.append(n)

print("A soma dos números pares é {}.".format(sum(soma)))