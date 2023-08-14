numero = 0

while True:
    numero = int(input('Quer ver a tabuada de qual valor? '))

    if numero <= 0:
        break

    print(f'----' * 6)
    for c in range(1, 11):
        tabuada = numero * c
        print(f'{numero} x {c:2} = {tabuada}')
    print(f'----' * 6)

print('\033[32mPrograma de Tabuada encerrado! Volte sempre')