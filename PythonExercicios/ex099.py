from time import sleep


def maior(*num):

    enorme = 0
    sleep(2)

    print('-=-=' * 10)
    print('Analisando os valores passados...')

    for n in num:
        print(f'{n} ', end='')
        sleep(0.5)

        if n >= enorme:
            enorme = n

    print(f'\nForam informados {len(num)} valores ao todo')
    print(f'O maior valor foi {enorme}')


maior(9, 3, 5, 6)
maior(4, 2, 5, 6)
maior(9, 5, 7, 2, 0, 10)
maior()