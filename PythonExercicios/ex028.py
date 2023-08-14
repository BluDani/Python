from random import randint
from time import sleep

print('-=--=' * 11)
print('Vou pensar em número entre 0 e 5, tente adivinhar....')
print('-=--=' * 11)

computador = randint(0, 5)  # o computador vai escolher um número de 0 a 5

resposta = int(input('Em que número eu pensei? '))
print('\033[34mProcessando...')
sleep(3)

if resposta == computador:
    print('\033[32mPARABÉNS! Você ganhou')
else:
    print('\033[31mGANHEI! Eu pensei no número {} e não no {}!'.format(computador, resposta))