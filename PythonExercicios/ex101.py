
def votar(ano):
    """
        ->
        :param anos: Idade do usúario
        :return: A situação do voto
        """

    from datetime import date

    anoAtual = date.today().year

    idade = anoAtual - ano

    if idade <= 15:
        return f'Com {idade} anos: NÃO VOTA'

    elif idade < 18 or idade >= 60:
        return f'Com {idade} anos: VOTO OPCIONAL'

    else:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO'


print('----' * 10)
nascimento = int(input('Ano de nascimento: '))

print(votar(nascimento))
