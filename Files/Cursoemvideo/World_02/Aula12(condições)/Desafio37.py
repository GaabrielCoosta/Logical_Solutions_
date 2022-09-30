#ESCREVA UM PROGRAMA QUE LEIA UM NÚMERO INTEIRO QUALQUER E PEÇA PARA O USÚARIO ESCOLHER QUAL SERÁ A BASE DE CONVERSÃO:
# - 1 PARA BINÁRIO
# - 2 PARA OCTAL
# - 3 PARA HEXADECIMAL

print("TRANSFORMANDO NÚMEROS INTEIROS PARA OUTRAS BASES")
print("\033[1:34m=-=\033[m"*16)
numero=int(input("Digite o número inteiro: "))
print("Qual conversão voce deseja escolher?\n[1]Converter para BINÁRIO\n[2]Converter para OCTAL\n[2]Converter para HEXADECIMAL")
escolha=(int(input("Sua opção: ")))
if escolha == 1:
    a=bin(numero)
    print(a)
elif escolha == 2:
    b=oct(numero)
    print(b)
elif escolha == 3:
    c=hex(numero)
    print(c)


