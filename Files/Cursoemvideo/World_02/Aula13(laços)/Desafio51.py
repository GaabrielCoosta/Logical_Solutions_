print("\033[1:34m PROGRESSÃO ARITMETRICA\033[m")
print("=-="*8)

n=int(input("Digite o primeiro termo: "))
r=int(input("Digite a razão: "))
decimo=n+(11-1)*r
for x in range(n,decimo,r):
    print('{} '.format(x), end="-> ")
print("ACABOU")

