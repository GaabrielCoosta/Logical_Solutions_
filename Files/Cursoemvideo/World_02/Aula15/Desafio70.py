print("\033[1:34mESTATISTICAS DOS PRODUTOS\033[m")
totalgasto=0
cont=0
nome=[]
produto=str(input("Nome do Produto: ")).strip().upper()
preco=int(input("Qual o preço do produto? "))
menorpreco = preco
while True:
    pergunta = str(input("Você gostaria de continuar cadastrando produtos [S|N] ?")).strip().upper()
    if pergunta != "S":
        break
    produto=str(input("Nome do Produto: ")).strip().upper()
    preco=int(input("Qual o preço do produto? "))
    totalgasto = totalgasto + preco



    if preco < menorpreco:
        menorpreco = preco
        nome.append(produto)

    if preco > 1000:
        cont = cont + 1



print(f"O total gasto foi R${totalgasto:.2f}.")
print(f"O total de produtos que custam menos de R$ 1000,00: {cont}")
print(f"O nome do produto mais barato é {nome} e ele custa R${menorpreco:.2f}.")
