maior = 0
menor = 1000
for c in range(1, 4):
    peso = float(input('Peso da {}° pessoa: '.format(c)))

    if peso > maior:
        maior = peso
    if peso < menor:
        menor = peso

print('O maior peso lido foi {}{}Kg{}'.format('\033[31m', maior, '\033[m'))
print('O menor peso lido foi {}{}Kg{}'.format('\033[36m', menor, '\033[m'))

