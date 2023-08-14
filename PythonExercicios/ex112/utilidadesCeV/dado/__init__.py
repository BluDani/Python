def leiaDinheiro(msg):
    """
    -> função para validar mensagem
    :param msg: mensagaem digitada
    :return: o valor da mensagem convertida em float
    """

    valido = False

    while not valido:

        entrada = str(input(msg)).replace(',', '.').strip()

        if entrada.isalpha() or entrada == '':
            print(f'\033[31m[ERRO] \"{entrada}" é um preço inválido\033[m')

        else:
            valido = True
            return float(entrada)
