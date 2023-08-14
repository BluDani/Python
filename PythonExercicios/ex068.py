from random import randint

print('=-=-' * 6)
print('VAMOS JOGAR ÍMPAR/PAR')
print('=-=-' * 6)

cont = 0

while True:

    jogador = int(input('Digite um número: '))

    decisao = ' '

    while decisao not in 'PIÍ':
        decisao = str(input('Par ou Ímpar [P/I]? ')).strip().upper()[0]

    computador = randint(0, 10)

    soma = jogador + computador

    print('----' * 9)
    print(f'Você jogou {jogador} e o computador jogou {computador}')
    print(f'Total de {soma}', end='')

    if soma % 2 == 0:
        print(' DEU PAR')
    else:
        print(' DEU ÍMPAR')

    print('----' * 9)

    if decisao == 'P' and soma % 2 == 0:
        print('\033[32mVocê GANHOU!\033[m')
        cont += 1

        print('Vamos jogar novamente...')
        print('=-=-' * 9)

    elif decisao == 'IÍ' and soma % 2 == 1:
        print('\033[32mVocê GANHOU!\033[m')
        cont += 1

        print('Vamos jogar novamente...')
        print('=-=-' * 9)

    else:

        print('\033[31mVocê PERDEU!\033[m')
        print('=-=-' * 9)

        break

print(f'\033[7mGAME OVER!\033[m Você venceu {cont} vezes')
