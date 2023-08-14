def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))

        except (ValueError, TypeError):
            print('\033[31m[ERRO] Por favor digite um número válido\033[m')
            continue

        except KeyboardInterrupt:
            print('\n\033[31mUsúario preferiu não digitar eesse número\033[m')
            return 0

        else:
            return n


def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))

        except (ValueError, TypeError):
            print('\033[31m[ERRO] Por favor digite um número válido\033[m')
            continue

        except KeyboardInterrupt:
            print('\n\033[31mUsúario preferiu não digitar eesse número\033[m')
            return 0

        else:
            return n