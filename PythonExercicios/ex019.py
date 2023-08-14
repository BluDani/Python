from random import choice

primeiro = str(input('Primeiro aluno: '))
segundo = str(input('segundo aluno: '))
terceiro = str(input('terceiro aluno: '))
quarto = str(input('quarto aluno: '))
lista = [primeiro, segundo, terceiro, quarto]

sorteio = choice(lista)

print('O aluno escolhido foi {}'.format(sorteio))


