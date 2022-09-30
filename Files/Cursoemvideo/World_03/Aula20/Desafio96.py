def titulo(txt):
    print('-'*30)
    print(txt)
    print('-'*30)


titulo(f'{"CONTROLE DE TERRENOS":^30}')
def area():
    l = float(input("LARGURA  (m)? "))
    c = float(input('COMPRIMENTO (m)? '))
    a = (l*c)
    print(f'O terreno de {l} x {c} tem {a:.2f} m².')


area()

