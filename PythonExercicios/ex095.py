jogadores = []
gols = []
dados = {}

while True:
    print('-=-=' * 10)
    dados['nome'] = str(input('Nome do jogador: '))
    partidas = int(input(f'Quantas partidas {dados["nome"]} jogou? '))

    for g in range(1, partidas + 1):
        gols.append(int(input(f'  Quantos gols na partida {g}: ')))

    dados['gols'] = gols[:]
    dados['total'] = sum(gols)
    jogadores.append(dados.copy())

    gols.clear()

    while True:
        continuar = str(input('Quer continuar [S/N]? ')).strip().upper()[0]

        if continuar in 'SN':
            break

        else:
            print('\033[31m[ERRO]\033[m Digite apenas S ou N')

    if continuar == 'N':
        break

print('-=-=' * 11)

print('Cod\tNome\t\tGols\t\t\t\tTotal')

print('----' * 11)

for k, v in enumerate(jogadores):
    print(f'{k}\t{v["nome"]}\t\t{v["gols"]}\t\t{v["total"]:<10}')

print('----' * 11)

while True:
    busca = int(input('Mostrar dados de qual jogador [999 para parar]? '))

    if busca == 999:
        break

    if busca > len(jogadores):
        print(f'\033[31m[ERRO]\033[m Não existe jogador com código {busca}')

    else:
        print(f'Levantamento do Jogador {jogadores[busca]["nome"]}')

        for i, g in enumerate(jogadores[busca]['gols']):
            print(f'  No jogo {i + 1} fez {g} gols')

    print('----' * 11)

print('<<<< VOLTE SEMPRE >>>>')