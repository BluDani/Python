numero = int(input('Digite um número inteiro: '))
print('Escolha uma das bases para conversão:')
print('[ 1 ] Converter para BINÁRIO')
print('[ 2 ] Converter para OCTAL')
print('[ 3 ] Converter para HEXADECIMAL')

opcao = int(input('Sua opção: '))

if opcao == 1:
    print('{} convertido para \033[32mBINÁRIO\033[m é igual a {}{}{}'.format(numero,'\033[32m', bin(numero)[2:], '\033[m'))

elif opcao == 2:
    print('{} convertido para \033[34mOCTAL\033[m é igual a {}{}{}'.format(numero, '\033[34m', oct(numero)[2:], '\033[m'))

elif opcao == 3:
    print('{} convertido para \033[35mHEXADECIMAL\033[m é igual a {}{}{}'.format(numero, '\033[35m', hex(numero)[2:], '\033[m'))

else:
    print('\033[31mOpção inválida! Tente novamente')


