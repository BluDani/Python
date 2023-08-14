produtos = ('Pão', 3,
            'Presunto', 5.50,
            'Queijo', 6.30,
            'Peito de Peru', 6.70,
            'Pão de Alho', 9.70,
            'Refrigerante', 8,)

print('----' * 10)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('----' * 10)

for item in range(0, len(produtos)):
    if item % 2 == 0:
        print(f'{produtos[item]:.<30}', end='')
    if item % 2 == 1:
        print(f'R$ {produtos[item]:.2f}')

print('----' * 10)

