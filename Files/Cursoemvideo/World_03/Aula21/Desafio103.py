def ficha(nome="<desconhecido>",gol=0):
    print(f'O jogador {nome} fez {gol} gols.')
n = str(input("Nome do Jogador: "))
g = str(input("Número de gol(s): "))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == "":
    ficha(gol=g)
else:
    ficha(n,g)