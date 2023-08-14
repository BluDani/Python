av1 = float(input('Digite a nota da av1: '))
av2 = float(input('Digite a nota da av2: '))
media = (av1 + av2) / 2

print('Tirando {:.1f} e {:.1f}, a média do aluno é {:.1f}'.format(av1, av2, media))
if media < 5:
    print('\033[31mO aluno está REPROVADO')

elif media < 7:
    print('\033[33mO aluno está de RECUPERAÇÃO')

else:
    print('\033[32mO aluno está APROVADO')