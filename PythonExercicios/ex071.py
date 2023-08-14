print('===' * 5)
print('BANCO NUBANK')
print('===' * 5)

valor = int(input('Qual valor você quer sacar? R$'))

total = valor
cedula = 50
totalCed = 0

while True:
    if total >= cedula:
        total -= cedula
        totalCed += 1
    else:
        if totalCed > 0:
            print(f'Total de {totalCed} cédulas de R${cedula}')

        if cedula == 50:
            cedula = 20

        elif cedula == 20:
            cedula = 10

        elif cedula == 10:
            cedula = 5

        elif cedula == 5:
            cedula = 1

        totalCed = 0

        if total == 0:
            break

print('Volte sempre ao Banco Nubank')