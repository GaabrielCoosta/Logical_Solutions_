def ajuda():
    while True:
        print('~'*25)
        print(f"\033[1:34m{'SISTEMA DE AJUDA PyHel':^25}\033[m")
        print('~'*25)
        print(f'\033[1:32mFunção ou Biblioteca>>\033[m ',end="")
        resp = str(input(""))
        help(resp)
        if resp == "FIM":
            break
ajuda()