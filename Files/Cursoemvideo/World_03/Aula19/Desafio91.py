from random import randint
import time
from operator import itemgetter
jogadores={}
ranking =[]

print("Valores Sorteados:")
for x in range(1,5):

    jogadores[f"jodador{x}"]=randint(1,6)
    jogadores.copy()

for k, v in jogadores.items():
    print(f"{k} tirou {v} no dado.")
    time.sleep(1)
print("=-=0"*15)
print(f"{'== RANKING DOS JOGADORES ==':^45}")
ranking = sorted(jogadores.items(),key=itemgetter(1),reverse=True)

for i, v in enumerate(ranking):
    print(f"{i+1:>6}° lugar: {v[0]} tirou {v[1]} no dado.")
    time.sleep(1)
