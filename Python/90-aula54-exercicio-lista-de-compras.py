"""
Crie um menu de opções para a criação de uma lista de compras
O usuario deve ter a possibilidade de inserir, editar e apagar valores
Não permita que o prigrama quebre com erros de indices inexistentes
"""

lista = []
entrada = True
while entrada == False:
    print('Lista de compras!')
    print('1 para inserir um item')
    print('2 para editar um item existente')
    print('3 para apagar um item')
    print('4 para visualizar sua item')
    print('5 para sair')
    escolha = int(input('Qual a opão desejada: '))
    
    if escolha == '1':
        inserir = input('O que deseja incluir? ')
        lista.append(inserir)
    
    if escolha == '2':
        lista = tuple(lista)
        for item in enumerate:
            print('Sua lista atua atual está assim: ', item)
            editar = input('Qual item deseja alterar? ')
            for editar in lista:
                adicionar = input('Informe o novo item: ')
                lista = list(lista)
                lista.append 