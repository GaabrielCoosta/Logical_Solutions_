print("\033[1:34mVERIFICANDO SE UM NÚMERO É PRIMO!\033[m")
print("=-="*11)

n=int(input("Digite um número: "))
con = 0
for x in range(1,n+1):
    if n % x == 0:
        print("\033[1:34m{}\033[m".format(x),end=" ")
        con=con+1
    else:
        print("{}".format(x),end=" ")
if con == 2:
    print("\nO número {} tem {} divisores".format(n,con))
    print("\033[1:34mELE É UM NÚMERO PRIMO!\033[m")
else:
    print("\nO número {} tem {} dividores!".format(n,con))
    print("\033[1:31mELE NÃO É UM NÚMERO PRIMO!\033[m")