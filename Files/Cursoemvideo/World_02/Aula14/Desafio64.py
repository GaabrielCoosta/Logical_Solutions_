n=0
soma=0
quantidade=0
while n != 999:
    n=int(input("Digite um número: "))
    soma = soma +  n
    quantidade = quantidade + 1
print("A soma dos números digitados é {}.".format(soma))
print("A quantidade dos números digitados é {}.".format(quantidade))