print("\033[1:34mIMPRIMINDO UM NÚMERO POR EXTENSO\033[m")
print("=*="*10)
t = ("zero","um","dois","três","quatro","cinco","seis",
     "sete","oito","nove","dez","onze","doze","treze")
p =("S")
while True:
    while p == "S":
        num = int(input("Digite um número entre 0 e 13: "))
        if 0 <= num <= 13:
            print(f'Você digitou o número {t[num]}.')
            p = str(input("Você gostaria de continuar [S|N]? ")).strip().upper()
        else:
            print("\033[1:31mErro de digitação. Tente novamente!\033[m")
    if p == "N":
        print("\033[1:34mVOLTE SEMPRE!\033[mdd")
        break




