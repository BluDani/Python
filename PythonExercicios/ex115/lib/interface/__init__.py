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


def linha(tam=30):
    print('=' * tam)


def cabecalho(txt):
    linha()
    print(txt.center(30))
    linha()


def menu(lista):
    cabecalho('MENU PRINCIPAL')

    c = 1

    for item in lista:
        print(f'\033[32m{c}\033[m - \033[34m{item}\033[m')

        c += 1

    linha()
    opcao = leiaInt('Sua Opção: ')

    return opcao