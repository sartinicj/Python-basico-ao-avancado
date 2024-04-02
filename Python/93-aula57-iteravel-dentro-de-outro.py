'''
Lista de listas e seus índices
'''

salas = [
    #0.........1
    ['Maria', 'Helena', ], #0
    #0
    ['Elaine',], #1
    #0.......1.......2
    ['Luiza', 'João', 'Eduarda', ], #2
    #0.......1.......2........3
    ['Nome1', 'Nome2', 'nome3', (0, 10, 20, 30)], #3
]

print(f'\n\nCom um print da variavel, ter-a-se a impressão dos valores contidos nas listas: {salas}')
print(f'\nColocando-se indices para impressão, o primeiro é sobre a lista externa e segundo sobre a lista interna: {salas[1][0]}')
print(f'\nDessa forma, para encontrar o segundo valor da primeira lista, faz-se [0][1]: {salas[0][1]}!')
print(f'\nTambem, para encontrar o terceiro valor da terceira lista, faz-se [2][2]: {salas[2][2]}!')
print(f'\nNo caso de uma tupla, para encontrar o valor em uma lista, segue-se a mesma logica: {salas[3][3][2]}!')

print(f'\n\nNo for tambem funciona. Em um for simples, imprime-se todas as listas: ')
for sala in salas:
    print(sala)

print(f'\nPara tirar da lista, e trazer somente os itens, faaz-se um for encadeado: ')   
for sala in salas:
    print(f'A sala é: {sala}')
    for aluno in sala:
        print(aluno)