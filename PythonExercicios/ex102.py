def fatorial(num, show=False):
    """
    -> função para calcular fatorial de um número
    :param num: valor a ser calculado
    :param show: (opcional) mostrar ou não a conta
    :return: valor do fatorial
    """

    print('----' * 10)

    resultado = 1

    for c in range(num, 0, -1):
        resultado *= c

        if show==True:

            print(f'{c}', end='')

            if c > 1:
                print(' x ', end='')

            else:
                print(' = ', end='')


    return resultado


print(fatorial(7, show=True))
