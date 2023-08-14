print('----' * 6)
print('LOJA SUPER BARATÃO')
print('----' * 6)

total = caro = 0
menor = 9999999

while True:
    nome = str(input('Nome do Produto: ')).strip()
    preco = float(input('Preço: R$'))

    total += preco

    if preco >= 1000:
        caro += 1

    if preco < menor:
        produtoBarato = nome
        menor = preco

    continuar = ' '
    print('----' * 6)

    while continuar not in 'SN':
        continuar = str(input('Quer continuar [S/N]? ')).strip().upper()[0]

    if continuar == 'S':
        print('----' * 6)

    if continuar == 'N':
        break

print('{:-^40}'.format('FIM DO PROGRAMA'))

print(f'O total da compra foi R${total:.2f}')
print(f'Temos {caro} produtos custando mais que R$1000.00')
print(f'O produto mais barato foi {produtoBarato} custando R${menor:.2f}')

