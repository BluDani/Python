print('-=-=' * 6)
print('Analizador de Triângulos')
print('-=-=' * 6)

s1 = float(input('Primeiro segmento: '))
s2 = float(input('Segundo segmento: '))
s3 = float(input('Terceiro segmento: '))

if s1 < s2 + s3 and s2 < s1 + s3 and s3 < s1 + s2:
    print('Os segmentos acima \033[32mPODEM\033[m formar triângulo')
else:
    print('Os segmentos acima \033[31mNÃO PODEM\033[m formar triângulo')
