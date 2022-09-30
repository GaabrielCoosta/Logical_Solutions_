#Escreva um programa para aprovar o empréstimo bancário de uma casa. O programa vai perguntar o valor da casa,
# o salário do comprador e em quantos anos ele vai pagar.
#Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário, ou então empréstimo será negado.

print("\033[1:34:40m EMPRÉSTIMO BANCÁRIO!\033[m")
print("=-="*7)
casa=(float(input("Informe o valor do imóvel: ")))
salario=(float(input("Informe o valor do seu salário: ")))
anos=(int(input("Informe em quantos anos pretende quitar o empréstimo: ")))
prestacao=casa/(anos*12)
print("O valor mensal fixo é de R${:.2f}".format(prestacao))
if prestacao > (salario*0.3):
    print("\033[1:31:40mEMPRÉSTIMO NEGADO!\033[m")
else:
    print("\033[1:34:40mEMPRÉSTIMO APROVADO!\033[m")

