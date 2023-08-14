def aumentar(preco=0, taxa=0, format=False):
    resultado = preco + (preco * taxa / 100)

    if format is False:
        return resultado

    else:
        return formatado(resultado)


def diminuir(preco=0, taxa=0, format=False):
    resultado = preco + (preco * taxa / 100)

    if format is False:
        return resultado

    else:
        return formatado(resultado)


def dobrar(preco=0, format=False):
    resultado = preco * 2

    if format is False:
        return resultado

    else:
        return formatado(resultado)


def metade(preco=0, format=False):
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
