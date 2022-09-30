somaidade=0
mediaidade=0
maioridadehomem=0
nomevelho=''
menoresdeidade=0
print("\033[1:33m-=-=-= ANALISADOR DE PESSOAS =-=-=-\033[m")
print("=="*18)
for x in range(1,5):
    print("\033[1:34m============ {} Pessoa =============\033[m".format(x))
    nome=str(input("Nome: ")).strip()
    idade=int(input("Idade: "))
    sexo=str(input("Digite seu sexo [M/F]: ")).strip().upper()
    somaidade = somaidade + idade
    if x == 1 and sexo == "M":
        maioridadehomem = idade
        nomevelho = nome
    if sexo == "M" and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo == "F" and idade < 20:
        menoresdeidade=menoresdeidade + 1


mediaidade=somaidade/4
print("\033[1:34m=-=\033[m"*12)
print("A média das idade é: {} anos.".format(mediaidade))
print("O homem mais velho se chama {}, e ele tem {} anos de idade.".format(nomevelho,maioridadehomem))
print("São {} mulheres com menos de 20 anos.".format(menoresdeidade))