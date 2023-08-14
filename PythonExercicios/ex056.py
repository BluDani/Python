idadeGeral = 0
maisVelho = 0
cont = 0

for c in range(1, 5):
    print('----- {}° PESSOA -----'.format(c))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()

    idadeGeral += idade

    if sexo == 'M' and idade > maisVelho:
        maisVelho = idade
        nomeVelho = nome

    if sexo == 'F' and idade < 20:
        cont += 1

mediaIdade = idadeGeral / 4

print('A média de idade do grupo é de {} anos'.format(mediaIdade))
print('O homem mais velho tem {} anos e se chama {}'.format(maisVelho, nomeVelho))
print('Ao todo são {} mulheres com menos de 20 anos'.format(cont))
