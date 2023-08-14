from math import sin, cos, tan, radians

angulo = int(input('Digite o ângulo que você deseja: '))
sen = sin(radians(angulo))
cos = cos(radians(angulo))
tan = tan(radians(angulo))

print('O ângulo de {} graus tem o seno {:.2f}'.format(angulo, sen))
print('O ângulo de {} graus tem o cosseno {:.2f}'.format(angulo, cos))
print('O ângulo de {} graus tem o tangente {:.2f}'.format(angulo, tan))

