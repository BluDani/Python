def area(larg, comp):
    resultado = larg * comp

    print(f'A Área de um terreno {larg}x{comp} é de {resultado}m²')


print('-=-=' * 6)
print('  Controle de Terrenos')
print('-=-=' * 6)

largura = float(input('Largura [m]: '))
comprimento = float(input('Comprimento [m]: '))

area(largura, comprimento)

