matriz = []
dados = []

for c in range(0, 3):   # c = cont
    for d in range(0, 3):   # d = dados
        dados.append(int(input(f'Digite um valor para [{c},{d}]: ')))

    matriz.append(dados[:])
    dados.clear()

print('-=-=' * 10)

for n in matriz:    # n = numero
    print(f'[{n[0]:^3}]', end='')
    print(f'[{n[1]:^3}]', end='')
    print(f'[{n[2]:^3}]')