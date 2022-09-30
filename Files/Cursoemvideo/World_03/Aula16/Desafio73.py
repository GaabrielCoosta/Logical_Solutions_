print("\033[1:34m{:^30}\033[m".format('CAMPEONATO BRASILEIRO'))
print("VEJA A SEGUIR OS RESULTADOS DA RODADA!")
print("=-="*13)
time = ("Bahia","Flamengo","Botafogo","Vasco","Palmeiras","Santos","Cruzeiro","Vitoria","Corinthias","São Paulao",
        "Atletico Mineiro","Atletico Paranaense","Fluminense","Gremio","Fortaleza","America","Bragantino","Coritiba",
        "Sport","Chapecoense")

cinco = time[0:5]
quatro = time[16:20]
ordem = sorted(time)
posicao = time.index("Chapecoense")
print("\033[1:34mOs cinco primeiros colocados são:\033[m")
for x in range(0,5):
        print(f"{(x+1)}-> {cinco[x]}")
print("\033[1:31mOs últimos quatro colocados são:\033[m")
for c in range (16,20):
        print(f"\033[1:31m{c+1}\033[m-> {time[c]}")
print("\033[1:34mNomes dos times em ordem alfabetica:\033[m")
for x in range(0,20):
        print(f"{ordem[x]}")
print("=-="*14)
print(f"O time da \033[1:34mChapecoense\033[m ficou na posição: {posicao+1}!")
print("\033[1:31mFim\033[m")




