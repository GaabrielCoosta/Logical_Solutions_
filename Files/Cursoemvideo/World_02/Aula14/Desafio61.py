print("\033[1:34m PROGRESSÃO ARITMETRICA \033[m")
print("=-="*8)

n=int(input("Digite o primeiro termo: "))
r=int(input("Digite a razão: "))
c = 1
while c <= 10:
    n = n + r
    c = c+1
    print(n)
