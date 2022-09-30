print("\033[1:34m DIGITE DOIS NÚMEROS E INFORME A OPERAÇÃO QUE DESEJA REALIZAR!\033[m")
print("\033[1:34m=-=\033[m"*21)
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
print("\033[1:34m=-=\033[m"*21)
c=1
while c != 5:
    print("[1]SOMAR")
    print("[2]MULTIPLICAR")
    print("[3]MAIOR")
    print("[4]NOVOS NÚMEROS")
    print("[5]SAIR")
    c = int(input("\033[1:31mQUAL OPERAÇÃO VOCE DESEJA REALIZAR:\033[m "))
    if c == 1:
        somar= n1+n2
        print("\033[1:34mA soma dos números é {}.\033[m".format(somar))
    if c == 2:
        multiplicar = n1*n2
        print("\033[1:34mO total da multiplicação é {}.\033[m".format(multiplicar))
    if c == 3:
        maior = [n1,n2]
        maior.sort()
        print("\033[1:34mO maior número digitado foi o {}.\033[m".format(maior[1]))
    if c == 4:
        n1 = int(input("Digite o novo primeiro número: "))
        n2 = int(input("Digite o novo segundo número: "))
print("=-="*12)
print("\033[1:34mVOCÊ ESCOLHEU SAIR DO PROGRAMA!\033[m")
