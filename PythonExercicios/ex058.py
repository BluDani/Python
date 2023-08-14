from random import randint

print('-=--=' * 11)
print('Vou pensar em número entre 0 e 10, tente adivinhar....')
print('-=--=' * 11)

computador = randint(0, 10)

jogador = int(input('Qual o seu palpite? '))
tentativas = 1

while jogador != computador:
    if jogador < computador:
        print('Mais... Tente mais uma vez')
        jogador = int(input('Qual o seu palpite? '))
        tentativas += 1

    else:
        print('Menos... Tente mais uma vez')
        jogador = int(input('Qual o seu palpite? '))
        tentativas += 1

print('\033[32mParabéns! Você acertou com {} tentativas'.format(tentativas))