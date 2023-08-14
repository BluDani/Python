salario = float(input('Digite o salário do funcionário: R$'))
if salario > 1250:
    aumento = (salario * 10 / 100) + salario
else:
    aumento = (salario * 15 / 100) + salario

print('O funcionário que antes ganhava \033[31mR${:.2f}\033[m agora ganha \033[32mR${:.2f}'.format(salario, aumento))