casa = float(input('Valor da casa: R$'))
salario = float(input('Salário do  comprador: R$'))
ano = int(input('Quantos anos de financiamento? '))

prestacao = casa / (ano * 12)
porcento = salario * 30 / 100    # 30% do salario

if prestacao > porcento:
    print('Para pagar uma casa de R${} em {} anos, a prestação será de R${}'.format(casa, ano, prestacao))
    print('\033[31mEmpréstimo NEGADO!\033[m')
else:
    print('Para pagar uma casa de R${:.2f} em {} anos, a prestação será de R${:.2f}'.format(casa, ano, prestacao))
    print('\033[32mEmpréstimo pode ser CONCEDIDO!')