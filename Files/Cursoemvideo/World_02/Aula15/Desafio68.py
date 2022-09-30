print("\033[1:34m************ VAMOS JOGAR PAR OU IMPAR! ************\033[m")
from random import randint
cont = 0
while True:
    jogador = str(input("VOCÊ É PAR OU IMPAR ? ")).strip().upper()
    print("\033[1:34m=*=\033[m"*17)
    if jogador != "PAR" and jogador != "IMPAR":
        print("\033[1:31mOPÇÃO NÃO EXISTENTE!\033[m")
        break

    q=int(input("Digite um número de 0 a 10: "))
    c=randint(0,10)
    soma= q + c

    if jogador == "IMPAR" and ( soma % 2 == 0 ):
        print(f"\033[1:31mVocê perdeu!\033[m A soma foi {soma}!")
        break
    if jogador == "PAR" and ( soma % 2 != 0):
        print(f"\033[1:31mVocê perdeu!\033[m\n A soma foi {soma}!")
        break
    else:
        cont = cont + 1
        print(f"\033[1:34mVOCÊ GANHOU!\033[m\nA soma foi {soma}! VAMOS DE NOVO!")
        print("\033[1:34m=*=\033[m"*17)
print("=-="*10)
print(f"\033[1:34mVOCÊ GANHOU {cont} PARTIDA(s)!\033[m")
print("=-="*10)

