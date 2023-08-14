matriz = []
dados = []

somaPar = somaTer = maior = 0

for c in range(0, 3):   # c = cont
    for d in range(0, 3):   # d = dados
        dados.append(int(input(f'Digite o valor para [{c},{d}]: ')))

        if dados[d] % 2 == 0:
            somaPar += dados[d]

        if d == 2:
            somaTer += dados[d]

        if c == 1 and dados[d] > maior:
            maior = dados[d]

    matriz.append(dados[:])
    dados.clear()

print('-=-=' * 10)

for n in matriz:    # n = número
    print(f'[{n[0]:^3}]', end='')
    print(f'[{n[1]:^3}]', end='')
    print(f'[{n[2]:^3}]')

print('-=-=' * 10)

print(f'A soma dos números pares é {somaPar}')
print(f'A soma dos valores da terceira coluna é {somaTer}')
print(f'O maior valor da segunda coluna é {maior}')