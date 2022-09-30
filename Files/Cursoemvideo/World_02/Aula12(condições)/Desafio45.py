#– Pedra ganha da tesoura (amassando-a ou quebrando-a).
#– Tesoura ganha do papel (cortando-o).
#– Papel ganha da pedra (embrulhando-a).
import time
import random
print("\033[1:34m====================JOQUEPÔ======================\033[m")
lista=["PEDRA","PAPEL","TESOURA"]
pc=random.choice(lista)
usuario=str(input("Escolha Pedra, Papel ou Tesoura: ")).upper().strip()
print("\033[1:34mQUAL É A SUA JOGADA?\033[m")
print("JO")
time.sleep(1)
print("KEN")
time.sleep(1)
print("PO!!!!")
print("=-="*15)
print("Computador jogou {}".format(pc))
print("Jogador jogou {}".format(usuario))
print("=-="*15)
if pc == usuario:
    print("\033[1:37mEMPATAMOS!\033[m")
elif pc == 'PEDRA' and usuario == 'TESOURA':
    print("\033[1:31mEU GANHEI! Pedra quedra Tesoura!\033[m")
elif pc == 'TESOURA' and usuario == 'PAPEL':
    print("\033[1:31mEU GANHEI! Tesoura corta Papel!\033[m")
elif pc == 'PAPEL' and usuario == 'PEDRA':
    print("\033[1:31m EU GANHEI! Papel embrulha Pedra!\033[m")

elif usuario == 'PEDRA' and pc == 'TESOURA':
    print("\033[1:34mVOCÊ GANHOU!! Pedra quedra Tesoura!\033[m")
elif usuario == 'TESOURA' and pc == 'PAPEL':
    print("\033[1:34mVOCÊ GANHOU! Tesoura corta Papel!\033[m")
elif usuario == 'PAPEL' and pc == 'PEDRA':
    print("\033[1:34mVOCÊ GANHOU! Papel embrulha Pedra!\033[m")



