print("\033[1:34m    *=GERADOR DE PA=* \033[m")
print("=-="*8)

termo=int(input("Digite o primeiro termo: "))
razao=int(input("Digite a razão: "))
total = 0
mais=int(input("Digite quantos termos você deseja visualizar: "))
c = 1
ttermo = 1


while mais != 0:
    total = total + mais

    while c <= total:
        print("{}->".format(termo), end=" ")
        termo = termo + razao
        c = c + 1
    print("\033[1:31mPausa\033[m")
    mais= int(input("Digite quantos termos você deseja visualizar a mais: "))

print("\033[1:34m===*==\033[m O total de termos mostrados foi: {} \033[1:34m===*==\033[m"
      "".format(total+1))
print("\033[1:34mFIM\033[m")
