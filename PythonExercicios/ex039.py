from datetime import date

nascimento = int(input('Ano de nascimento: '))
anoAtual = date.today().year
idade = anoAtual - nascimento

convocacao = nascimento + 18

print('Quem nasceu em {} tem {} anos em {}'.format(nascimento, idade, anoAtual))

if idade < 18:
    alistamento = 18 - idade
    print('\033[32mAinda faltam {} anos para o alistamento'.format(alistamento))
    print('Seu alistamento será em {}'.format(convocacao))

elif idade > 18:
    alistamento = idade - 18
    print('\033[33mVocê já deveria ter se alistado há {} anos'.format(alistamento))
    print('Seu alistamento foi em {}'.format(convocacao))

else:
    print('\033[31mVocê deve se alistar esse ano')


