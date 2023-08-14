print('==' * 10)
print('10 TERMOS DE UMA PA')
print('==' * 10)

termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))

resultado = termo

c = 1
while c <= 10:
    print('{} '.format(resultado), end='')
    resultado += razao

    c += 1
