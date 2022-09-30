def leiadinheiro(txt):
    while True:
        a = str(input(f'{txt}')).replace(',', '.')

        if a.isalpha():
            print(f'\033[1:31mERRO: "{a}" é um preço inválido!\033[m')
        elif a.strip() == "":
            print(f'\033[1:31mERRO: "{a}" é um preço inválido!\033[m')


        else:
            return float(a)
