
def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return (f" Você tem somente {idade} anos! Ainda faltam {16 - idade} anos.\033[1:31m Voto negado!\033[m")
    if idade > 18:
        return (f"Você tem {idade} anos! VOTO OBRIGATÓRIO!")
    if 16 <= idade < 18:
        return (f'Você tem {idade} anos! Voto facultitivo!')


nasc = int(input("Digite o ano em que nasceu: "))
print(voto(nasc))



