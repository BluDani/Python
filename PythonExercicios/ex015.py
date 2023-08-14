alugado = int(input('Quantos dias o carro foi alugado? '))
km = float(input('Quantos Km o carro pecorreu? '))
preco = (alugado * 60) + (km * 0.15)

print('O carro foi alugado por {} dias e pecorreu {}Km'.format(alugado, km))
print('O preço a ser pago é R${:.2f}'.format(preco))
