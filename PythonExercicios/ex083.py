expressao = str(input('Digite a expressão: '))

pilha = []

for simb in expressao:
    if simb == '(':
        pilha.append('(')

    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()

        else:
            pilha.append(')')
            break

if len(pilha) == 0:
    print('\033[32mSua expressão está válida!\033[m')

else:
    print('\033[31mSua expressão está errada\033[m')