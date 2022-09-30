print("{:^34}".format("****CADASTRANDO PRODUTOS****"))
print("\033[1:34m=-=\033[m"*12)

lista= ()
count = 0
nomes = ()
valores = ()
while True:
    pergunta = str(input("Deseja cadastrar produtos [S|N]: ")).strip().upper()
    if pergunta == "N":
        break
    elif pergunta != "S" and pergunta != "N":
        print("\033[1:31mErro de digitação!\033[m")

    if pergunta == "S":
        count += 1
        nome = str(input("Digite o nome do produto: "))
        nomes += (nome,)
        valor = float(input("Digite o valor do produto R$ "))
        valores += (valor,)
        lista += ((nome,valor),)
print("\033[1:34m=-=\033[m"*12)
for x in range(0,count):
    print("Você cadastrou o produto {} com o valor de R${:.2f}.".format(nomes[x],valores[x]))
print("\033[1:31m********* FIM **********\033[m")