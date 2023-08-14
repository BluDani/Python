mais18 = homem = mulher = 0

while True:
    print('----' * 6)
    print('CADASTRE UMA PESSOA')
    print('----' * 6)

    idade = int(input('Idade: '))
    sexo = ' '

    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]

    if idade >= 18:
        mais18 += 1

    if sexo == 'M':
        homem += 1

    if idade < 20 and sexo == 'F':
        mulher += 1

    print('----' * 6)
    continuar = str(input('Quer continuar [S/N]? ')).strip().upper()[0]

    if continuar in 'N':
        break

print(f'Total de pessoas com mais de 18 anos: {mais18}')
print(f'Ao todo temos {homem} homens cadastrados')
print(f'E temos {mulher} mulheres com menos de 20 anos')