print("\033[1:34m     ALISTAMENTO MILÍTAR!\033[m")
print("=-="*10)
idade=(int(input("Qual a sua idade? ")))
if idade < 18:
    tempo = 18 - idade
    print("Ainda não está na hora de se alistar, faltam ainda {} anos!".format(tempo))
elif idade > 18:
    tempo = idade - 18
    print("Já passou do tempo de se alistar, voce ultrapassou {} anos!".format(tempo))
elif idade == 18:
    print("ESTÁ NA HORA DE SE ALISTAR!")
