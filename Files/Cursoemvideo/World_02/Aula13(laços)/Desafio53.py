print("\033[1:34m VAMOS ENCONTRAR ALGUNS POLÍNDROMOS ?\033[m")
print("\033[1:31m=-=\033[m"*13)

frase=str(input("Digite um frase: ")).strip().upper()
ra=frase.split()
rb="".join(ra)
rever="".join(reversed(rb))
if rb == rever:
    print("\033[1:34mA FRASE DIGITADA É UM POLÍNDROMO\033[m")
else:
    print("\033[1:32mDESCULPE, A FRASE DIGITADA NÃO É UM POLÍNDROMO!\033[m")

print("\033[1:31m=-=\033[m"*13)






