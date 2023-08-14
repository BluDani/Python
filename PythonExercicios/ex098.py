from time import sleep

def contador(i, f, p):

    if p < 0:
        p *= -1

    if p == 0:
        p = 1

    print('-=-=' * 10)
    print(f'Contagem de {i} até {f} de {p} em {p}')

    cont = i

    if i < f:
        while cont <= f:
            print(f'{cont} ', end='')
            cont += p

    else:
        while cont >= f:
            print(f'{cont} ', end='')
            cont -= p

    print('Fim')

    print('-=-=' * 10)


contador(1, 10, 1)
contador(10, 0, 2)

print('Agora é sua vez de personalizar a contagem!')
inicio = int(input('Ínicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))

contador(inicio, fim, passo)
