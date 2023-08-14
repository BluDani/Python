lista = []
pares = []
impares = []

while True:
    lista.append(int(input('Digite um valor: ')))

    continuar = str(input('Quer continuar [S/N]? ')).strip().upper()[0]

    if continuar == 'N':
        break

for n in lista:
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)

print('-=-=' * 10)
print(f'A lista completa é {lista}')
print(f'A lista de pares é {pares}')
print(f'A lista de ímpares é {impares}')
