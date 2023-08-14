salario = float(input('Qual o salário do funcionário? R$'))
reajuste = salario + (salario * 15 / 100)

print('O salário do funcionário era R${:.2f}, ganhando um aumento de 15% ele passa a receber {:.2f}'.format(salario, reajuste))