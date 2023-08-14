def aumentar(preco=0, taxa=0, format=False):
    """
    -> função para aumentar o valor fornecido
    :param preco: preço fornecido pelo usúario
    :param taxa: taxa em % de aumento
    :param format: decide se terá formatação ou não
    :return: valor aumentado
    """

    resultado = preco + (preco * taxa / 100)

    if format is False:
        return resultado

    else:
        return formatado(resultado)


def diminuir(preco=0, taxa=0, format=False):
    """
    -> função para diminuir o valor fornecido
    :param preco: preço fornecido pelo usúario
    :param taxa: taxa em % de redução
    :param format: decide se terá formatação ou não
    :return: valor reduzido
    """

    resultado = preco + (preco * taxa / 100)

    if format is False:
        return resultado

    else:
        return formatado(resultado)


def dobrar(preco=0, format=False):
    """

    :param preco: preço fornecido pelo usúario
    :param format: decide se terá formatação ou não
    :return: retorna o preço dobrado
    """

    resultado = preco * 2

    if format is False:
        return resultado

    else:
        return formatado(resultado)


def metade(preco=0, format=False):
    """

    :param preco: preço fornecido pelo usúario
    :param format: decide se terá formatação ou não
    :return: retorna o valor dividido pela metade
    """

    resultado = preco / 2

    if format is False:
        return resultado

    else:
        return formatado(resultado)


def formatado(preco=0, moeda='R$'):
    return f'{moeda}{preco:.2f}'.replace('.', ',')


def resumo(preco=0, aumento=10, reducao=5):
    print('---' * 10)
    print('RESUMO DE PREÇO'.center(30))
    print('---' * 10)

    print(f'Preço analisado: \t{formatado(preco)}')
    print(f'Dobro do preço: \t{dobrar(preco, True)}')
    print(f'Metade do preço: \t{metade(preco, True)}')
    print(f'{aumento}% de aumento: \t{aumentar(preco, aumento, True)}')
    print(f'{reducao}% de redução: \t{diminuir(preco, reducao, True)}')

    print('---' * 10)
