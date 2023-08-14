alunos = []

while True:
    nome = str(input('Nome: ')).strip()
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2

    alunos.append([nome, [nota1, nota2], media])

    continuar = str(input('Quer continuar [S/SN]? ')).strip().upper()[0]

    if continuar == 'N':
        break

print('-=-=' * 8)

print('N°\tNome\t\tMédia')

print('----' * 8)

for p, n in enumerate(alunos):
    print(f'{p}\t{n[0]}\t\t{n[2]}')

while True:

    print('----' * 11)

    nota = int(input('Mostrar notas de qual aluno [999 interrompe]? '))

    if nota == 999:
        print('FINALIZANDO...')
        break

    if nota <= len(alunos) - 1:
        print(f'Notas de {alunos[nota][0]} são {alunos[nota][1]}')

print('<<<< VOLTE SEMPRE >>>>')