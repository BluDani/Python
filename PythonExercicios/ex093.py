jogador = {}
gols = []


jogador['nome'] = str(input('Nome: ')).strip()
partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))

for p in range(1, partidas + 1):
    gols.append(int(input(f'\tQuantos gols na partida {p}? ')))

jogador['gols'] = gols[:]
jogador['total'] = sum(gols)

print('-=-=' * 15)
print(jogador)
print('-=-=' * 15)

for k, v in jogador.items():
    print(f'{k} tem o valor {v}')

print('-=-=' * 15)
print(f'O jogador {jogador["nome"]} jogou {partidas} partidas')

for g in range(1, partidas + 1):
    print(f'\t->Na partida {g}, fez {jogador["gols"][g - 1]} gols')

print(f'Foi um total de {jogador["total"]} gols')



