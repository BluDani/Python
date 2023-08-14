dados = {}
cadastro = []

soma = 0

while True:
    dados['nome'] = str(input('Nome: '))

    while True:
        dados['sexo'] = str(input('Sexo [M/F]: ')).strip().upper()[0]
        if dados['sexo'] in 'MF':
            break
        else:
            print('\033[31m[ERRO]\033[m Digite apenass M ou F')

    dados['idade'] = int(input('Idade: '))

    cadastro.append(dados.copy())

    soma += dados['idade']

    while True:
        continuar = str(input('Quer continuar [S/N]: ')).strip().upper()[0]

        if continuar in 'SN':
            break

        else:
            print('\033[31m[ERRO]\033[m Responda apenas S ou N')

    if continuar == 'N':
        break

media = soma / len(cadastro)

print(cadastro)

print('-=-=' * 10)

print(f'Ao todo foram {len(cadastro)} pessoas cadastradas')
print(f'A média de idade é de {media:.2f}')
print(f'As mulheres cadastradas foram ', end='')

for p in cadastro:
    if p['sexo'] == 'F':
        print(f'{p["nome"]} ', end='')

print(f'\nLista das pessoas que estão acima da média: ', end='')

for p in cadastro:
    if p['idade'] > media:
        print('\t')

        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print('<<<< ENCERRADO >>>>')