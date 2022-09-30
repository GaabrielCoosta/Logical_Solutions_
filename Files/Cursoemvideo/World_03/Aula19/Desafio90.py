escola = {}
escola['nome']=str(input("Nome do aluno: "))
escola['Média']=float(input("Digite a média: "))
if escola['Média'] >= 7:
    escola['Situação']='Aprovado'
else:
    escola['Situação']='Reprovado'
print("=-="*20)
print(f"  - nome é igual a {escola['nome']}")
print(f"  - média é igual a {escola['Média']}")
print(f"  - situação é igual a {escola['Situação']}")

