from lib import interface, arquivo
from time import sleep

arq = 'CursoEmVideo.txt'

if not arquivo.arquivoExiste(arq):
    arquivo.criarArquivo(arq)

while True:
    resposta = interface.menu(['Ver pessoas cadastradas', 'Cadastrar nova Pessoa', 'Sair do Sistema'])

    if resposta == 1:
        arquivo.lerArquivo(arq)

    elif resposta == 2:
        interface.cabecalho('Novo Cadastro')
        nome = str(input('Nome: ')).strip()
        idade = interface.leiaInt('Idade: ')
        arquivo.cadastrar(arq, nome, idade)

    elif resposta == 3:
        interface.cabecalho('Saindo do Programa...')
        break

    else:
        print('\033[31m[ERRO] Digite uma opção válida\033[m')

    sleep(1)