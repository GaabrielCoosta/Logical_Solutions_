print("****** CONTANDO VOGAIS ******")
print("\033[1:34m=-=\033[m"*10)

tupla= ()
while True:
    p = str(input("Deseja adicionar uma palava a tupla [S|N] ?")).strip().upper()
    if p == "N":
        break
    if p == "S":
        palavra = str(input("Qual palavra deseja adicionar? "))
        tupla += (palavra,)

b = len(tupla)
p = 0

for x in range(0,b):
    print(f"As vogais contidas na palavra {tupla[x]} são:")
    vogais = ()
    for p in tupla[x]:

        if p == "a" or p == "e" or p == "i" or p == "o" or p == "u":
            vogais += (p,)
    print(vogais)
print("\033[1:34m=-=\033[m"*10)
print("\033[1:31m*** FIM ***\033[m")


