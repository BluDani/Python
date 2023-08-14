numero = int(input('Digite um número [999 para parar]: '))

soma = 0
cont = 0

while numero != 999:
    cont += 1

    soma += numero
    numero = int(input('Digite um número [999 para parar]: '))

print('Você digitou {} números e a soma entre eles é {}'.format(cont, soma))