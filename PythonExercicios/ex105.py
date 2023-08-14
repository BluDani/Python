def notas(*nota, sit=False):
    """
    -> função para analisar notas e situações dos alunos
    :param nota: notas dos alunos
    :param sit: (opcional) mostrar ou não a situação do aluno
    :return: dicionário com todas as informações dos alunos
    """

    r = {}

    r['total'] = len(nota)
    r['maior'] = max(nota)
    r['menor'] = min(nota)
    r['media'] = sum(nota) / len(nota)

    if sit == True:
        if r['media'] < 4:
            r['situação'] = 'Reprovado'

        elif r['media'] < 6:
            r['situação'] = 'Recuperação'

        else:
            r['situação'] = 'Aprovado'


    return r

aluno = notas(6.5, 7.3, 5, sit=True)
print(aluno)
