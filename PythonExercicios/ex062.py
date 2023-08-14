print('==' * 10)
print('Gerador de PA')
print('==' * 10)

termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))

resultado = termo

c = 1
total = 0
mais = 10

while mais != 0:

    total = total + mais
    while c <= total:
        print('{} '.format(resultado), end='')
        resultado += razao

        c += 1

    mais = int(input('\nQuantos termos você quer mostrar a mais? '))

print('Progreção finalizada com {} termos mostrados'.format(total))
