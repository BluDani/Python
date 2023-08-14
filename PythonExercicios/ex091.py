from random import randint
from time import sleep
from operator import itemgetter

resultado = {'Jogador1': randint(1, 6),
             'Jogador2': randint(1, 6),
             'Jogador3': randint(1, 6),
             'Jogador4': randint(1, 6),
             }

ranking = []

print('Valores Sorteados: ')

for k, v in resultado.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)

ranking = sorted(resultado.items(), key=itemgetter(1), reverse=True)

print('-=-=' * 8)
print('===RANKING DOS JOGADORES === ')
for i, v in enumerate(ranking):
    print(f'  {i+1}° lugar: {v[0]} com {v[1]}.')

