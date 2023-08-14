peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
imc = peso / altura ** 2

print('Seu IMC é de {:.1f}'.format(imc))
print('Você está ', end='')

if imc < 18.5:
    print('\033[33mABAIXO DO PESO')

elif imc < 25:
    print('no \033[32mPESO IDEAL')

elif imc < 30:
    print('em \033[33mSOBREPESO')

elif imc < 40:
    print('em \033[31mOBESIDADE')

else:
    print('em \033[30;41mOBESIDADE MÓRBIDA, CUIDADO!\033[m')