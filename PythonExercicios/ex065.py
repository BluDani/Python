continuar = 'S'

soma = 0
cont = 0

maior = 0
menor = 99999

while continuar not in 'Nn':
    numero = int(input('Digite um número: '))

    cont += 1
    soma += numero

    if numero > maior:
        maior = numero
    elif numero < menor:
        menor = numero

    continuar = str(input('Quer continuar [S/N]? ')).strip()[0]


media = soma / cont

print('Você digitou {} números e a média foi {:.2f}'.format(cont, media))
print('O \033[34mmaior número foi {}\033[m e o \033[35mmenor foi {}'.format(maior, menor))