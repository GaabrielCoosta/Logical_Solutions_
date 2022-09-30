print("\033[1:32m================VERIFICANDO!=================\033[m")
print("=-="*15)
c = 1
while c !="M" and c !="F":
    c = str(input("Informe seu sexo [M/F]: ")).strip()
    if c !="M" and c !="F":
        print("Erro de digitação!")
    else:
        print("MUITO OBRIGADO!")