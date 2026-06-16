def fatorial(num, show = False):
    """
    -> Função para calcular o fatorial de um número
    :param num: O número a ser calculado.
    :param show: (Opcional) Para mostrar ou não a conta.
    :return: O valor do fatorial de um número.
    """
    f = 1
    for cont in range(num, 0, -1):
        if show:
            print(cont, end='')
            if cont > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= cont
    return f


#Programa Principal
print(fatorial(5, show=True))
