cont = 0
soma = 0

for impar in range(3, 501, 3):
    if impar % 2 != 0:
        cont += 1
        soma += impar
print('A soma dos {} valores solicitados é igual a {}'.format(cont, soma))
