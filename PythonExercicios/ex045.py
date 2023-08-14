from random import randint
from time import sleep

itens = ('PEDRA', 'PAPEL', 'TESOURA')
print('Suas opções:')
print('[ 0 ] PEDRA')
print('[ 1 ] PAPEL')
print('[ 2 ] TESOURA')

jogador = int(input('Qual a sua jogada? '))

print('PEDRA')
sleep(1)
print('PAPEL')
sleep(1)
print('TESOURA')
sleep(1)

computador = randint(0, 2)

print('-=-=' * 7)
print('O computador jogou {}'.format(itens[computador]))
print('O jogador jogou {}'.format(itens[jogador]))
print('-=-=' * 7)

if computador == 0:
    if jogador == 0:
        print('\033[33mEMPATE')

    elif jogador == 1:
        print('\033[32mJOGADOR VENCE')

    elif jogador == 2:
        print('\033[31mCOMPUTADOR VENCE')

    else:
        print('\033[31mJOGADA INVÁLIDA!')

elif computador == 1:
    if jogador == 0:
        print('\033[31mCOMPUTADOR VENCE')

    elif jogador == 1:
        print('\033[33mEMPATE')

    elif jogador == 2:
        print('\033[32mJOGADOR VENCCE')

    else:
        print('\033[31mJOGADA INVÁLIDA!')

elif computador == 2:
    if jogador == 0:
        print('\033[32mJOGADOR VENCE')

    elif jogador == 1:
        print('\033[31mCOMPUTADOR VENCE')

    elif jogador == 2:
        print('\033[33mEMPATE')

    else:
        print('\033[31mJOGADA INVÁLIDA!')