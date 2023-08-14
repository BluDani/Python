aluno = {}

aluno['nome'] = str(input('Nome: ')).strip()
aluno['media'] = float(input(f'Média do aluno {aluno["nome"]}: '))

print('-=-=' * 10)
print(f'- Nome do aluno: {aluno["nome"]}')
print(f'- A media é {aluno["media"]}')
print('- Situação: ', end='')

if aluno['media'] < 4:
    print('\033[31mREPROVADO\033[m')

elif aluno['media'] < 6:
    print('\033[33mRECUPERAÇÃO\033[m')

else:
    print('\033[32mAPROVADO\033[m')
