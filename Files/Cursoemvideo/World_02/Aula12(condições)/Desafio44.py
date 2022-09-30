print("\033[1:34m     CONDIÇÕES DE PAGAMENTO POR VALOR DE PRODUTO\033[m")
print("=-="*18)
valorproduto=float(input("Digite o valor do pruduto: "))
print("\033[1:34m      CONDIÇÕES DE PAGAMENTO\033[m")
print("Digite 1 para pagar à vista no dinheiro/cheque com 10% de desconto!")
print("Digite 2 para pagar à vista no cartão com 5% de desconto!")
print("Digite 3 para pagar em até duas vezes no cartão")
print("Digite 4 para pagar em 3x ou mais com 20% juros.")
condicao=int(input("\033[1:34mQual a condição de pagamento escolhida?  \033[m"))

if condicao == 1:
    total= valorproduto - (valorproduto*0.1)
    print("Novo valor a ser pago com desconto é de R${:.2f}".format(total))
elif condicao ==2:
    total = valorproduto - (valorproduto*0.05)
    print("Novo valor a ser pago com desconto é de R${:.2f}".format(total))
elif condicao ==3:
    total = valorproduto*0.5
    print("Você pagará duas parcelas de R${:.2f}".format(total))
elif condicao ==4:
    total = (valorproduto*0.20)+valorproduto
    print("Você escolheu pagar em 3 parcelas ou mais. Esse é o novo valor com juros: R${:.2f}".format(total))