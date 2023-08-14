from datetime import date

nascimento = int(input('Ano de nascimento: '))
ano = date.today().year
idade = ano - nascimento

print('O atleta tem {} anos'.format(idade))
if idade <= 9:
    print('Classificação: \033[32mMIRIM')

elif idade <= 14:
    print('Classificação: \033[34mINFANTIL')

elif idade <= 19:
    print('Classificação: \033[35mJÚNIOR')

elif idade <= 25:
    print('Classificação: \033[36mSÊNIOR')

else:
    print('Classificação: \033[31mMASTER')
