numeros = [[], []]

for c in range(1, 8):
    valor = int(input(f'Digite o {c}° valor: '))

    if valor % 2 == 0:
        numeros[0].append(valor)

    elif valor % 2 == 1:
        numeros[1].append(valor)

print('-=-=' * 10)

numeros[0].sort()
numeros[1].sort()

print(f'Os números pares digitados foram {numeros[0]}')
print(f'Os números ímpares digitados foram {numeros[1]}')