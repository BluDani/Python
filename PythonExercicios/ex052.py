numero = int(input('Digite um número: '))
cont = 0

for c in range(1, numero + 1):
    if numero % c == 0:
        print('\033[31m', end='')
        cont += 1
    else:
        print('\033[34m', end='')

    print('{} '.format(c), end='')

print('\n\033[mO número {} foi divisivel {} vezes'.format(numero, cont))
if cont <= 2:
    print('E por isso \033[32mele É PRIMO')
else:
    print('E por isso ele \033[31mNÃO É PRIMO')
