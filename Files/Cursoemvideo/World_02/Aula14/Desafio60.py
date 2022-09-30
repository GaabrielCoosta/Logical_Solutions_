#from math import factorial
#n = int(input("Digite o número: "))
#f = factorial(n)
#print (f)
print("\033[1:34mCALCULANDO O FATORIAL!\033[m")
print("=-="*8)
from math import factorial
n = int(input("Digite um número para calcular seu fatorial: "))
f=factorial(n)
c = n
while c > 0:

    print("{}".format(c),end="")
    print(" x " if c > 1 else " = ", end="")

    c -= 1
print("{}".format(f))

