numeros = []
posicaoMaior = []
posicaoMenor = []

cont = 0

for c in range(0, 5):
    numeros.append(int(input(f'Digite um número para a Posição {c}: ')))

    if c == 0:
        maior = menor = numeros[c]

    else:
        if numeros[c] >= maior:
            maior = numeros[c]

        if numeros[c] <= menor:
            menor = numeros[c]

print('====' * 11)
print(f'Você digitou os valores: {numeros}')
print(f'O maior valor digitado foi {maior} na posição ', end='')

for pos, n in enumerate(numeros):
    if n == maior:
        print(f' {pos}...', end='')

print(f'\nO menor valor digitado foi {menor} na posição ',end='')

for pos, n in enumerate(numeros):
    if n == menor:
        print(f' {pos}...', end='')

