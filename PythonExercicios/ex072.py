extenso = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis',
           'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze',
           'Catorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito',
           'Dezenove', 'Vinte')

numero = ' '

while True:
    while True:
        numero = int(input('Digite um número entre 0 e 20: '))

        if 0 <= numero <= 20:
            break

        print('\033[31mTente novamente!\033[m', end=' ')

    print(f'Você digitou o número \033[32m{extenso[numero]}\033[m')

    print('====' * 7)
    continuar = str(input('Quer continuar [S/N]? ')).strip().upper()[0]
    print('====' * 7)

    if continuar == 'N':
        break

