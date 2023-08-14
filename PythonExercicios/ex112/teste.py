from utilidadesCeV import moeda, dado

valor = dado.leiaDinheiro('Digite o preço: R$')

"""
print(f'A metade de {moeda.formatado(valor)} é R${moeda.metade(valor, True)}')
print(f'O dobro de {moeda.formatado(valor)} é R${moeda.dobrar(valor, True)}')
print(f'Aumentando 10%, temos R${moeda.aumentar(valor, 10, True)}')
print(f'Reduzindo 13%, temos {moeda.diminuir(valor, 13, True)}')
"""

moeda.resumo(valor, 20, 12)
