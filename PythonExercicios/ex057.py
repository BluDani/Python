sexo = str(input('Informe seu sexo [M/F]: ')).strip().upper()[0]

while sexo not in 'MF':

    sexo = str(input('\033[31mDados Inválidos!\033[m Por favor, informe seu sexo: ')).strip().upper() [0]

print('\033[32mSexo {} registrado com sucesso'.format(sexo))