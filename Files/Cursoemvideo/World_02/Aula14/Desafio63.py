print("\033[1:34mSEQUÊNCIA DE FIBONACCI\033[m")
print("Digite um número inteiro e veja a quantidade desejesada de números da Sequencia de Fibonacci!")
n=int(input("Digite quantos termos você quer mostrar: "))

n1 = 0
n2 = 1
print("{} -> {}".format(n1,n2), end="")
c = 3
while c <= n:
    n3 = n1 + n2
    print("-> {}".format(n3), end="")
    n1 = n2
    n2 = n3
    c = c +1
print("-> \033[1:34mFIM\033[m")