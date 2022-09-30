print("\033[1:34m        CALCULANDO O ICM\033[m")
print("=-="*10  )
peso=(float(input("Digite seu peso: ")))
altura=float(input("Digite sua altura: "))
icm = peso / (altura**2)
print("\033[1:34mO seu ICM é: {}.\033[m".format(icm))

if icm < 18.5:
    print("\033[1:34mVOCÊ ESTÁ ABAIXO DO PESO!\033[m")
elif icm > 18.5 and icm < 25.0:
    print("\033[1:34mVOCÊ ESTÁ COM O PESO IDEAL!\033[m")
elif icm >= 25 and icm < 30:
    print("\033[1:33mVOCÊ ESTÁ COM SOBREPESO!\033[m")
elif icm >= 30 and icm <= 40:
    print("\033[1:31mVOCÊ ESTÁ COM OBESIDADE!\033[m")
elif icm > 40:
    print("\033[1:31mOBESIDADE MÓRBITA!\033[m")