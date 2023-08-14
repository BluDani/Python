velocidade = float(input('Qual a velocidade do carro? '))
if velocidade <= 80:
    print('\033[32mVocê está dentro do limite de velocidade')
else:
    multa = (velocidade - 80) * 7
    print('\033[31mMULTADO! Você está acima do limite de velocidade')
    print('\033[33mVocê deve pagar uma multa de R${:.2f}'.format(multa))
