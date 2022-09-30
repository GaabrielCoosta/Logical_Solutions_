from datetime import datetime

temp={}
temp['nome']=str(input("Nome: "))
temp['idade']= datetime.now().year - (int(input("Nascimento: ")))
temp['ctps']=int(input("Carteira de Trabalho (o não tem): "))
if temp['ctps'] != 0:
    temp['ano']=int(input('Ano de Contratação: '))
    temp['salario']=float(input('Sálario R$: ' ))
    temp['aposentadoria']=(temp['ano'] + 35) - datetime.now().year
print("=-="*15)
for k,v in temp.items():
    print(f'    - {k} tem o valor {v}')