"""
Faça uma lista de compras com listas
O usuario deve ter a possibilidade de inserir e apagar valores
Não permita que o prigrama quebre com erros de indices inexistentes
"""

compras_mercado = ['Vinagre', 'Pasta de dente']

for item in enumerate(compras_mercado):
    print('Itens da lista: ', item)
    
for tupla_enumerada in enumerate(compras_mercado):
    for valor in tupla_enumerada:
        print('Item da lista: ',valor)