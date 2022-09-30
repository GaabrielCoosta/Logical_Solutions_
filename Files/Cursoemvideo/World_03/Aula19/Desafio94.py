cadastro=[]
mulheres = []
total = 0
tidade = 0
while True:
    temp = {}
    temp['nome']=str(input('Nome: '))
    temp['sexo']=str(input('Sexo [F|M]: ')).strip().upper()
    if temp['sexo'] not in "fFmM":
        print("\033[1:31mErro de digitação... Tente novamente!\033[m")
        temp['sexo']=str(input('Sexo [F|M]: ')).strip().upper()
    if temp["sexo"] == "F":
        mulheres.append(temp['nome'])
    temp['idade']=int(input('Idade: '))

    cadastro.append(temp.copy())
    temp.clear()
    total += 1

    p = str(input('Deseja continuar cadastrando? [S|N]: ')).strip().upper()
    if p not in "fFmM":
        print("\033[1:31mErro de digitação... Tente novamente!")
    if p == "N":
        break
print('=-='*15)
print(f"A) Ao todo, {total} pessoas foram cadastradas.")
for x in range(0,total):
    tidade += cadastro[x]['idade']
print('B) A média de idade é de {:.2f} anos.'.format(tidade/total))
print('C) As mulheres cadastradas foram: ',end="")
for x in mulheres:
    print(f'{x}',end=" ")

print(f'\nD) Lista de pessoas que estão acima da média:')

for x in cadastro:
    if x['idade'] > (tidade/total):
        print(f'\033[1:31m    nome = {x["nome"]}; sexo = {x["sexo"]}; idade = {x["idade"]};\033[m')
print('\033[1:34mENCERRADO\033[m >>')

