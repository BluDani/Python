from time import sleep
from random import randint


def sorteio(lista):

    print('Sorteando 5 valores da lista: ', end='')

    for cont in range(0, 5):
        n = randint(1, 10)
        lista.append(n)
        print(f'{n} ', end='')

    print('Pronto')


def somaPar(lista):

    soma = 0

    for n in lista:
        if n % 2 == 0:
            soma += n

    print(f'Somando os valores pares de {lista}, temos {soma}')
    

numeros = []

sorteio(numeros)
somaPar(numeros)


