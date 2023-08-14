from random import randint
from time import sleep

palpite = []
dados = []

print('-=-=' * 10)
print(f'\t\t\tJOGO NA MEGA SENA')
print('-=-=' * 10)

jogos = int(input('Quantos jogos você quer que eu sorteie? '))

print('-=' * 4, f'SORTEANDO {jogos} JOGOS', '-=' * 4)

for j in range(1, jogos + 1):

    cont = 0
    while True:
        num = randint(1, 60)
        if num not in dados:
            dados.append(num)
            cont += 1
        if cont >= 6:
            break

    dados.sort()
    palpite.append(dados[:])
    dados.clear()

for i, l in enumerate(palpite):

    sleep(1)
    print(f'Jogo {i + 1}: {l}')

print('-=' * 6, 'BOA SORTE', '-=' * 6)
