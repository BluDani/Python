numeros = []

for n in range(0, 5):
    num = int(input('Digite um valor: '))

    if n == 0:
        maior = menor = num

    if num > maior:
        maior = num
        numeros.insert(4, num)
        print('Adicionado ao final da lista')

    elif num < menor:
        menor = num
        numeros.insert(0, num)
        print('Adicionado na posição 0')

    else:
        numeros.insert(1, num)
        print('Adicionado na posição 1')

print('-=-=' * 10)
print(f'Os valores digitados em ordem foram: {numeros}')