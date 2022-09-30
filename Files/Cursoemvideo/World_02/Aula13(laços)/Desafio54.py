print("\033[1:34mQUANTOS JA ATINGIRAM A MAIOR IDADE ?\033[m")
print("=-="*12)

m=0
n=0
for x in range(0,7):

    p=int(input("Em qual ano você nasceu: "))
    if (2022 - p) >= 18:
        m = m+1
    else:
        n = n+1
print(n)
print("=-="*14)
print("\033[1:34mSomente {} pessoas, atingiram a maior idade!\033[m".format(m))
print("\033[1:31m{} pessoas são de menores!\033[m".format(n))
print("=-="*14)

