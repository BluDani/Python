color = ('\033[m',             # 0 = sem cor
         '\033[0;30;44m',      # 1 = azul
         '\033[0;30;41m',      # 2 = vermelho
         '\033[0;30;42m',      # 3 = verde
         '\033[0;30;45m'       # 4 = roxo
         )


def ajuda(objeto):
    titulo(f'Acessando o manual do comando \'{objeto}\'', 1)

    print(color[4])
    help(objeto)
    print(color[0])


def titulo(msg, cor=0):
    tamanho = len(msg) + 4

    print(color[cor], end='')
    print('~' * tamanho)
    print(f'  {msg}')
    print('~' * tamanho)
    print(color[0], end='')


while True:
    titulo('SISTEMA DE AJUDA PyHELP', 3)

    acao = str(input('Função ou Biblioteca > ')).strip().lower()

    if acao == 'fim':
        titulo('ATÉ LOGO', 2)

        break

    ajuda(acao)
