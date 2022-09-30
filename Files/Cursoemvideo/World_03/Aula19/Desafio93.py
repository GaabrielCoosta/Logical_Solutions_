
cadastro = {}
cadastro['nome']=str(input('Nome do jodador: '))
partidas = int(input("Quantas partidas ele jogou? "))
cadastro['gols']=[]

for x in range(1,partidas+1):
    gols=int(input(f'Quantos gols na partida {x}? '))
    cadastro['gols'].append(gols)

cadastro['total']= sum(cadastro['gols'])
print("=-="*15)
print(f'O jogador {cadastro["nome"]} jogou {partidas} partidas.')
for x in range(1,partidas+1):
    print(f'    => Na partida {x}, fez {cadastro["gols"][x-1]}.')
print(f'Foi um total de {cadastro["total"]} gols.')