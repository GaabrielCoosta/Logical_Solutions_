f = 0
a = 0
lista = []
p = str(input("Digite uma expressão contendo parenteses: ")).strip()
lista = p
for x in lista:
    if x == ")":
        f += 1
    elif x == "(":
        a += 1
if ")" and "(" not in lista:
    print("\033[1:31mA expressão não possui parenteses!\033[m")
if (a+f) % 2 == 0 and lista[0]=="(" and lista[-1]==")":
    print("\033[1:34mSua expressão é válida!\033[m")
else:
    print("\033[1:31mSua expressão não é válida!\033[m")