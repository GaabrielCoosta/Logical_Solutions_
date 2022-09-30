cadastro={}
jogadores=[]
while True:

    cadastro.clear()
    cadastro['nome']=str(input('Nome: '))
    cadastro['partidas'] = int(input("Quantas partidas ele jogou? "))
    cadastro['gols']=[]

    for x in range(1,cadastro['partidas']+1):
        x = int(input(f'Quantos gols ele marcou na {x} partida? '))
        cadastro['gols'].append(x)

    cadastro['total']=sum(cadastro['gols'])
    jogadores.append(cadastro.copy())

    p = str(input("Deseja continuar cadastrando? [S|N]: ")).strip().upper()
    if p not in "sSnN":
        print("\033[1:31mErro de digitação... Tente novamente!\033[m")
        p = str(input("Deseja continuar cadastrando? [S|N]: ")).strip().upper()

    if p == "N":
        break
print("=-="*15)
print(f'cod ', end='')
for i in cadastro.keys():
    print(f'{i:<15}', end='')
print()
print('-------------------------------------------------------')
for k,v in enumerate(jogadores):
    print(f"{k:>3}", end=' ')
    for d in v.values():
        print(f"{str(d):<15}", end='')
    print()
print()
print('-------------------------------------------------------')

while True:
    p = int(input("Mostrar dados de qual jogador? (999 para parar):"))
    if p != 999:
        print(f' -- LEVANTAMENTO DO JOGADOR {jogadores[p]["nome"]}:')
        print(f'O jogador {jogadores[p]["nome"]} jogou {jogadores[p]["partidas"]} partidas.')
        for i in range(1, jogadores[p]['partidas'] + 1):
            print(f'    => Na partida {i}, fez {jogadores[p]["gols"][i - 1]}')
        print(f'Ele teve um aproveitamento de {jogadores[p]["total"]} gols.')
        print("=-=" * 15)

    if p==999:
        break




