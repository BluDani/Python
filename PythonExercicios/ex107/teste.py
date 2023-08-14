import moeda

valor = float(input('Digite o valor: '))

print(f'A metdade de R${valor} é R${moeda.metade(valor)}')
print(f'O dobro de R${valor} é R${moeda.dobrar(valor)}')
print(f'Aumentando 10% temos R${moeda.aumentar(valor, 10)}')
