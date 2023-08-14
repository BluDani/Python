distancia = float(input('Digite a distância da viagem: '))
print('Você está prestes a começar uma viagem de {}Km'.format(distancia))

if distancia <= 200:
    preco = distancia * 0.50
    print('O preço da sua passagem será de \033[31mR${:.2f}'.format(preco))
else:
    preco = distancia * 0.45
    print('O preço da sua passagem será de \033[31mR${:.2f}'.format(preco))
