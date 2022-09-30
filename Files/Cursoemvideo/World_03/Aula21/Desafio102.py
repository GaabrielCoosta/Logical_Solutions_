def fatorial(n=0, show=False):
    """
    -> Calcule o fatorial de um número.
    :para (n), o número a ser calculado.
    :para (show), mostrar ou não a conta.
    : return, retorna o valor total do fatorial de n.
    """
    f = 1
    for c in range(n,0,-1):
        if show:
            if c > 1:
                print(f'{c} x ',end="")
            if c == 1:
                print(f'{c} = ',end="")

        f = f*c
    return f


print(fatorial(5,True))

help(fatorial)