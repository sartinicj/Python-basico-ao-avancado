string = 'ABCD'
lista = ['Maria', 'Helena', 1, 2, 3, 'Eduarda']
tupla = 'Pyhton', 'é', 'legal'

print('Dessa forma eu estou fazendo um print de lista comum: ') 
for nome in lista:
    print(nome)
    
print('\nAqui eu estou tirando a quebra de linha do print: ')
for nome in lista:
    print(nome, end=' ')
    
print('\nJa aqui é uma outra forma de trazer as informações da lista tambem sem quebra: ')
print(*lista)

print('\nJa aqui é uma outra forma de trazer as informações da lista tambem sem quebra: ')
print(*string)

print('\nJa aqui é uma outra forma de trazer as informações da lista tambem sem quebra: ')
print(*tupla)

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

print('\n\nImpressão de uma lista grande, de forma confusa: ')
print(*salas)

print('\nImpressão de uma lista grande, com separador: ')
print(*salas, sep='\n')