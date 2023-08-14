from datetime import date

ano = date.today().year
maior = 0
menor = 0

for c in range(1, 8):
    nascimento = int(input('Em que ano a {}° pessoa nasceu? '.format(c)))

    idade = ano - nascimento

    if idade < 18:
        menor += 1
    else:
        maior += 1

print('Ao todo tivemos {} pessoas maiores de idade'.format(maior))
print('E também tivemos {} pessoas menores de idade'.format(menor))