numeros = []

while True:
    num = (int(input('Digite um número: ')))

    if num not in numeros:
        numeros.append(num)
        print('\033[32mNúmero adicionado com sucesso\033[m')
    else:
        print('\033[31mNúmero duplicado! Não vou adicionar\033[m')

    continuar = str(input('Quer continuar [S/N]? ')).strip().upper()[0]

    if continuar == 'N':
        break

print('-=-=' * 10)
numeros.sort()
print(f'Você digitou os valores: {numeros}')