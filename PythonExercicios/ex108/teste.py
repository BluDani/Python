import moeda

valor = float(input('Digite o valor: '))

print(f'A metade de {moeda.formatado(valor)} é R${moeda.formatado(moeda.metade(valor))}')
print(f'O dobro de {moeda.formatado(valor)} é R${moeda.formatado(moeda.dobrar(valor))}')
print(f'Aumentando 10% temos R${moeda.formatado(moeda.aumentar(valor, 10))}')
