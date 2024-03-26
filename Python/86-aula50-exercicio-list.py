"""
Exercicio
Exiba os indices da lista
0 nome 1
1 nome 2
2 nome 3
"""

lista = ['Maria', 'Madalena', 'Luiz']
indices = range(len(lista))

for indice in indices:
    print(indice, lista[indice], type(lista[indice]))
    