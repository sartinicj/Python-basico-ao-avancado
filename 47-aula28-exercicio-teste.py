'''
Peça ao usuario para digitar seu nome e idade
Se nome e idade forem digitados:
    Exiba:
        Seu nome é (nome)
        Seu nome invertido é (invertido)
        Seu nome contem ou nao espaços
        Seu nome tem n letras
        A primeira letra do seu nome é (letra)
        A ultima letra do seu nome é (letra)
Se nada for digitado em nome ou idade
    Exiba
        desculpe, voce deixou campos vazios
'''

name = input('Digite um nome: ')
age = input('Digite uma idade: ')


if name and age:
    print(f'Seu nome é {name}')
    print(f'Seu nome invertido é {name[::-1]}')

    if ' ' in name:
        print(f'Seu nome tem espaços')
    else:
        print(f'Seu nome não tem espaços')
    
    size = (len(name))
    print(f'Seu nome tem {size} letras')

    fst = (name[0])
    print(f'A primeira letra do seu nome é: {fst}')

    lst = (name[-1])
    print(f'A última letra do seu nome é {lst}')
else:
    print('Desculpe, você dedixou campos vazios!')

