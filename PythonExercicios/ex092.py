from datetime import date
dados = {}

anoAtual = date.today().year

dados['Nome'] = str(input('Nome: ')).strip()

nascimento = int(input('Ano de nascimento: '))
idade = anoAtual - nascimento

dados['idade'] = idade

dados['CTPS'] = int(input('Carteira de trabalho [0 não tem]: '))

if dados['CTPS'] != 0:
    dados['contratação'] = int(input('Ano de contratação: '))
    dados['salario'] = float(input('Salário: R$'))
    dados['aposentadoria'] = idade + ((dados['contratação'] + 40) - anoAtual)

print('-=-=' * 10)
for k, v in dados.items():
    print(f' - {k} tem o valor {v}')