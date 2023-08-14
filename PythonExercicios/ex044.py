print('======LOJA GUANABARA======\n')

compras = float(input('Preço das compras: '))

print('\nFORMAS DE PAGAMENTO')
print('[ 1 ] À vista no dinheiro/cheque')
print('[ 2 ] À vista no cartão')
print('[ 3 ] 2x no cartão')
print('[ 4 ] 3x ou mais no cartão')

opcao = int(input('Qual é a opção? '))

if opcao == 1:
    total = compras - (compras * 10 / 100)
    print('Sua compra de R${:.2f} vai custar R${:.2f} com 10% de desconto'.format(compras, total))

elif opcao == 2:
    total = compras - (compras * 5 / 100)
    print('Sua compra de R${:.2f} vai custar R${:.2f} com 5% de desconto'.format(compras, total))

elif opcao == 3:
    total = compras / 2
    print('Sua compra será parcelada em {}x de R${:.2f}'.format(2, total))

elif opcao == 4:
    total = compras + (compras * 20 / 100)
    parcelas = int(input('Quantas vezes você gostaria de parcelar? '))
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS'.format(parcelas, total))

else:
    print('\033[31mForma de Pagamento Inválida!\033[m Escolha outra Forma de Pagamento')
