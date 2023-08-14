print('-=-=' * 6)
print('Analizador de Triângulos')
print('-=-=' * 6)

s1 = float(input('Primeiro segmento: '))
s2 = float(input('Segundo segmento: '))
s3 = float(input('Terceiro segmento: '))

if s1 < s2 + s3 and s2 < s1 + s3 and s3 < s1 + s2:
    print('Os segmentos acima \033[32mPODEM FORMAR\033[m um triângulo', end='')
    if s1 == s2 == s3:
        print(' \033[34mEQUILÁTERO')
    elif s1 == s2 or s1 == s3 or s2 == s3:
        print(' \033[35mISÓCELES')
    else:
        print(' \033[36mESCALENO')
else:
    print('Os segmentos acima \033[31mNÃO PODEM\033[m formar um triângulo')
