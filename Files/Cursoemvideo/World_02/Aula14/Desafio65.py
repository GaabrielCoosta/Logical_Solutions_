print("\033[1:31mMENOR VALOR - MAIOR VALOR - MÉDIA\033[m")

lista=[]
numero=int(input("Digite um número inteiro: "))
lista.append(numero)
soma=numero
c = 1
p = str(input("Deseja continuar a digitar números [S|N]: ")).strip().upper()
while p == "S":
    while p == "S":
        numero = int(input("Digite o próximo número: "))
        lista.append(numero)
        soma = soma + numero
        c = c +1
        p = str(input("Deseja continuar a digitar números [S|N]: ")).strip().upper()
lista.sort()
print("O menor valor digitado: {}".format(lista[0]))
print("O maior valor digitado: {}".format(lista[-1]))
media=(soma/c)
#print("A média dos números digitados é {}.".format(media))
print(f"A média dos números digitados é {media}.")