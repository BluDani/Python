from time import sleep

valor1 = int(input('Primeiro valor: '))
valor2 = int(input('Segundo valor: '))

opcao = 0

while opcao != 5:
    print('=-==-=' * 6)
    print('[ 1 ] Somar')
    print('[ 2 ] Multiplicar')
    print('[ 3 ] Maior')
    print('[ 4 ] Novos números')
    print('[ 5 ] Sair do programa')
    print('=-==-=' * 6)

    opcao = int(input('O que você quer fazer? '))

    if opcao == 1:
        soma = valor1 + valor2
        print('A soma {} + {} é igual a {}'.format(valor1, valor2, soma))

    elif opcao == 2:
        multiplicacao = valor1 * valor2
        print('A multiplicação {} x {} é igual a {}'.format(valor1, valor2, multiplicacao))

    elif opcao == 3:
        if valor1 > valor2:
            print('Entre {} e {} o maior é {}'.format(valor1, valor2, valor1))
        elif valor2 > valor1:
            print('Entre {} e {} o maior é {}'.format(valor1, valor2, valor2))
        else:
            print('Os dois números são iguais')

    elif opcao == 4:
        valor1 = int(input('Primeiro valor: '))
        valor2 = int(input('Segundo valor: '))

    elif opcao == 5:
        print('Finalizando...')

    else:
        print('\033[31mOpção Inválida! Tente novamente\033[m')

sleep(1)
print('Fim do programa')