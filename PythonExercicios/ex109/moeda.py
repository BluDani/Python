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
