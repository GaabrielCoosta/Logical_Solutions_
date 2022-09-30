print("=-="*15)
print("ANALISADOR DE TRIÃNGULOS")
print("ANALISAREMOS SE O TRIÂNGULO É EQUILÁTEO, ISÓSCELES OU ESCALENO")
print("=-="*15)

r1 = float(input("Digite o primeiro seguimento de reta: "))
r2 = float(input("Digite o segundo seguimento de reta: "))
r3 = float(input("Digite o terceiro seguimemnto de reta: "))
if r1 < r2+r3 and r2 < r1+r3 and r3 < r1+r2:
    print("\033[1:34mÉ POSSÍVEL FORMAR UM TRIÃNGULO")
    if r1 == r2 == r3:
        print("\033[1:34mO TRIÂNGULO FORMADO É EQUILÁTERO!\033[m")
    elif r1 == r2 and r1 != r3:
        print("\033[1:34mO TRIÃNGULO FORMADO É ISÓSCELES!\033[m")
    elif r1 == r3 and r1 != r2:
        print("\033[1:34mO TRIÃNGULO FORMADO É ISÓSCELES!\033[m")
    elif r2 == r3 and r2 != r1:
        print("\033[1:34mO TRIÃNGULO FORMADO É ISÓSCELES!\033[m")
    elif r1 != r2 and r1 != r3 and r2 != r3:
        print("\033[1:34mO TRIÃNGULO FORMADO É ESCALENO!\033[m")

else:
    print("\033[1:31mNÃO É POSSÍVEL FORMAR UM TRIÃNGULO")