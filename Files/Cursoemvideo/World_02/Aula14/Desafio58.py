print("\033[1:34m==========TENTE ADIVINHAR O NÚMERO!==========\033[m")
print("\033[1:34m================ ( 0 a 10 ) =================\033[m")
print("=-="*15)
import random
n = random.randint(0,10)
c=1
tentativas = 0
while c != n:
    c = int(input("Qual número eu pensei? "))
    if n != c:
        tentativas += 1
        print("Você errou! Tente novamente!")
    else:
        print("\033[1:34mVocê acertou!\033[m")
        print("VOCÊ TENTOU {} VEZES!".format(tentativas))
