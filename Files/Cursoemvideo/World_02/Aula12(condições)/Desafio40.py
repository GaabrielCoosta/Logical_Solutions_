print("\033[1:34m     APROVAÇÃO ESCOLAR!\033[m")
print("=-="*10)
n1=float(input("Qual foi sua primeira nota? "))
n2=float(input("Qual foi a sua segunda nota? "))
media= (n1+n2)/2
print("Sua média é {}".format(media))

if media < 5.0:
    print("\033[1:31mREPROVADO!\033[m")
elif media >= 5.0 and media < 7.0:
    print("\033[1:33mVOCÊ ESTÁ DE RECUPERAÇÃO!\033[m")
elif media >= 7.0:
    print("\033[1:32mVOCÊ FOI APROVADO!\033[m")
