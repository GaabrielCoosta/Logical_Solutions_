print("\033[1:34:40mCOMPARANDO NÚMEROS!\033[m")
print("=-="*6)
n1=int(input("Digite o primeiro número: "))
n2=int(input("Digige o segundo número: "))
if n1 > n2:
    print("O número {} é maior que o número {} .".format(n1,n2))
elif n2 > n1:
    print("O número {} é maior que o número {} .".format(n2,n1))
elif n1 == n2:
    print("Não existe valor maior, os dois são iguais!")