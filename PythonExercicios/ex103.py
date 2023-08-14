def ficha(jogador='<desconhecido>', gols=0):
    """
    ->
    :param jogador: Nome do jogador
    :param gols: númerros de gols feito pelo jogador
    :return: sem retorno
    """
    print(f'O jogador {jogador} fez {gols} gol(s) no campeonato')


nome = str(input('Nome do Jogador: ')).strip()
numGols = str(input('Número de gols: '))

if numGols.isnumeric():
    numGols = int(numGols)

else:
    numGols = 0

if nome.strip() == '':
    ficha(gols = numGols)

else:

    ficha(nome, numGols)