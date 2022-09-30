def escreva():
    txt = str(input("Digite algo: "))
    print("~"*(len(txt)+6))
    print(f'  {txt}')
    print("~" * (len(txt) + 6))


escreva()