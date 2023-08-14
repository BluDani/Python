soma = 0
cont = 0

for c in range(1, 7):
    numero = int(input('Digite o {}° número: '.format(c)))
    if numero % 2 == 0:
        soma += numero
        cont += 1

print('Você informou {} números \033[32mPARES\033[m e a soma deles é igual a {}'.format(cont, soma))
