numero = int(input('Digite um número para calcular seu fatorial: '))
fatorial = 1
'''while numero > 0:
    print('{} '.format(numero), end='')
    print('x ' if numero > 1 else '=', end='')
    fatorial *= numero
    numero -= 1'''

for c in range(numero, 0, -1):
    print('{} '.format(c), end='')
    print('x ' if c > 1 else '=', end='')
    fatorial *= c

print(' {}'.format(fatorial))
