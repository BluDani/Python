valor = float(input('Qual é o preço do produto? R$'))
desconto = valor - (valor * 5 / 100)

print('O produto custava R${:.2f}, mas com o desconto de 5% ele fica custando R${:.2f}'.format(valor, desconto))
