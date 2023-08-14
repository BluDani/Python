valor = int(input('Digite um número: '))
'''
m = valor // 1000
resto = valor % 1000
c = resto // 100
resto = resto % 100
d = resto // 10
resto = valor % 10
u = resto // 1
'''
m = valor // 1000 % 10
c = valor // 100 % 10
d = valor // 10 % 10
u = valor // 1 % 10

print('Milhar: {}'.format(m))
print('Centena: {}'.format(c))
print('Dezena: {}'.format(d))
print('Unidade: {}'.format(u))
