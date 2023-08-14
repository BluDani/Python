print('==' * 10)
print('10 TERMOS DE UMA PA')
print('==' * 10)

termo = int(input('Primeiro Termo: '))
razao = int(input('Razão: '))

resultado = termo

for c in range(1, 11):
    print('{}'.format(resultado), end=' ')
    resultado += razao

