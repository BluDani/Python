numero = int(input('\033[35mDigite qualquer número:\033[m '))
resultado = numero % 2
if resultado == 0:
    print('O número {} é \033[34mpar'.format(numero))
else:
    print('O número {} é \033[31mímpar'.format(numero))