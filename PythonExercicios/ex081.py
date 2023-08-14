numeros = []

cont = 0

while True:
    numeros.append(int(input('Digite um número: ')))

    continuar = str(input('Quer continuar [S/N]? ')).strip().upper()[0]

    if continuar == 'N':
        break

print('-=-=' * 10)
print(f'Você digitou {len(numeros)} elementos')
numeros.sort(reverse=True)
print(f'Os valores em ordem decrescente são {numeros}')

if 5 in numeros:
    print('O número 5 faz parte da lista!')

else:
    print('O valor 5 não foi encontrado na lista!')


