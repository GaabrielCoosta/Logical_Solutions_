from random import randint
print("-"*20)
print("{:^20}".format("JOGO NA MEGA SENA"))
print("-"*20)
x = int(input("Quantos jogos você quer que eu sorteie? "))
print("-=-=-= SORTEANDO {} JOGOS -=-=-=".format(x))
lista=[]
lt = []

while True:
    while len(lista)<x:
        for c in range(0,7):
            lt.append(randint(1,61))
        lista.append(lt[:])
        lt.clear()

    if len(lista) == x:
        break
for z in range(0,x):
    print(f"Jogo {z+1}: {lista[z]}")
print("=-=-=-=-= < BOA SORTE! > -=-=-=-=-=")



