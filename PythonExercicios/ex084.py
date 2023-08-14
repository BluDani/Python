galera = []
dados = []

maior = menor = 0

while True:
    dados.append(str(input('Nome: ')).strip())
    dados.append(float(input('Peso: ')))

    if len(galera) == 0:
        maior = menor = dados[1]

    else:
        if dados[1] >= maior:
            maior = dados[1]

        elif dados[1] <= menor:
            menor = dados[1]

    galera.append(dados[:])
    dados.clear()

    continuar = str(input('Quer continuar [S/N]? ')).strip().upper()[0]

    if continuar == 'N':
        break

print('-=-=' * 10)

print(f'Ao todo, você cadastrou {len(galera)} pessoas')
print(f'O maior peso foi {maior}Kg. Peso de ', end='')

for p in galera:
    if p[1] == maior:
        print(f'[{p[0]}] ', end='')

print(f'\nO menor peso foi {menor}Kg. Peso de ', end='')

for p in galera:
    if p[1] == menor:
        print(f'[{p[0]}] ', end='')

