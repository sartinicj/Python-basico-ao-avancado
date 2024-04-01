"""
Crie um menu de opções para a criação de uma lista de compras
O usuario deve ter a possibilidade de inserir, editar e apagar valores
Não permita que o prigrama quebre com erros de indices inexistentes
"""

lista = []
while lista == True:
    print('\nLista de compras!\n')
    print('Digite [1] para inserir um item')
    print('Digite [2] para editar um item existente')
    print('Digite [3] para apagar um item')
    print('Digite [4] para visualizar seu item')
    print('Digite [5] para sair')
    escolha = int(input('\nQual a opção desejada: '))
    
    if escolha == '1':
        inserir = input('O que deseja incluir? ')
        lista.append(inserir)
    
    elif escolha == '2':
        lista = tuple(lista)
        for item in enumerate:
            print('Sua lista atua atual está assim: ', item)
            editar = input('Qual item deseja alterar? ')
            for editar in lista:
                editar = input('Informe o novo item: ')
                lista = list(lista)
                lista.append(editar)
                
    elif escolha == '3':
        adicionar = input('Informe o novo item: ')
        lista = list(lista)
        lista.append(adicionar)
        
    elif escolha == '4':
        for item in enumerate:
            print('Sua lista atua atual está assim: ', item)
    
    elif escolha == '5':
        print('Lista encerrada')
        
    else:
        print('Entrada invalida!')
