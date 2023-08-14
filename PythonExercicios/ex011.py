largura = float(input('Qual a largura da parede? '))
altura = float(input('Qual a altura da parede? '))
area = largura * altura
tinta = area / 2

print('A área dessa parede é {:.1f}m²'.format(area))
print('a quantidade de tinta necessária para pintar essa área é {:.1f}L'.format(tinta))