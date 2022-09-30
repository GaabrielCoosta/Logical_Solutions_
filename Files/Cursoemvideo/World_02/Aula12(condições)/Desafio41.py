print("\033[1:34m    CLASSIFICAÇÃO DE CATEGORIA POR IDADE!\033[m")
print("=-="*15)
ano = int(input("Digite aqui o seu ano de nascimento: "))
idade = 2022 - ano
print("VOCÊ TEM {} ANOS".format(idade))
if idade <= 9:
    print("\033[1:34mSUA CATEGORIA É A MIRIM!\033[m")
elif idade > 9 and idade < 15:
    print("\033[1:34mSUA CATEGORIA É A INFANTIL!\033[m")
elif idade > 14 and idade < 20:
    print("\033[1:34mSUA CATEGORIA É A JUNIOR!\033[m")
elif idade > 19 and idade < 21:
    print("\033[1:34mSUA CATEGORIA É A SÊNIOR!\033[m")
elif idade > 20:
    print("\033[1:34mSUA CATEGORIA É A MASTER!\033[m")
print("=-="*15)
print("\033[1:34mBOA SORTE!\033[m")
print("=-="*15)
