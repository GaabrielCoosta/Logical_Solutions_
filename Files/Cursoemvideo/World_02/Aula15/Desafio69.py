maisdedezoito=0
totalhomens=0
mulheresmenosdevinte=0
print("\033[1:34m*************** ANALISADOR DE CADASTRO ***************\033[m")
print("\033[1:34m=-=\033[m"*18)
while True:
    sexo=str(input("Você é do sexo Masculino ou Feminino: ")).strip().upper()
    if sexo != "FEMINIMO" and sexo != "MASCULINO":
        print("\033[1:31mSEXO NÃO EXISTENTE!\033[m")
        break
    idade=int(input("Qual a sua idade? "))
    if sexo == "MASCULINO":
        totalhomens += 1
    if idade > 18:
        maisdedezoito += 1
    if sexo == "FEMININO" and idade < 20:
        mulheresmenosdevinte += 1
    pergunta=str(input("Você gostaria de continuar cadastrando pessoas? [S|N]: ")).strip().upper()
    if pergunta == "N":
        break
print("\033[1:34m=*=\033[m"*18)
print(f"FORAM CADASTRADOS {totalhomens} HOMENS!")
print(f"A quantidade de pessoas maiores de 18 anos: {maisdedezoito}!")
print(f"O total de mulheres com menos de 20 anos: {mulheresmenosdevinte}!")
print("\033[1:34m*********************** FIM **************************\033[m")