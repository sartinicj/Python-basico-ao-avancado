"""
enumerate - enumera iteraveis (indices)
"""

names = ['Cecilia', 'Douglas', 'Sabrina']
names.append('Salem')

# O problema dessa forma, que coloca o enumerator em uma variavel, é que uma vez usado, ele é consumido. 
summary_names = enumerate(names)
print('Aqui print de enumerate na memoria: ', summary_names) #Assim mostrará a posição na memória
print('Aqui print de enumerate com valores: ',next(summary_names)) #Assim mostrará a posição do índice e o valor registrado

for item in summary_names:
    print('Aqui print do primeiro for: ',item)

# Por ter sido consumido, ele não repete a informação pedida
for item in summary_names:
    print('Aqui print do segundo for,com valor esgotado: ',item)
    
# Como solução, usa-se o enumerate direto, sem criar variavel: 

for item in enumerate(names):
    print('Aqui print do novo for: ',item)

"""
NÃO FUNCIONANDO:    
for item in enumerate(names):
    print('Aqui print do segundo for: ',item)
    
for tupla_enumerada in enumerate(names):
    for valor in tupla_enumerada:
        print('Aqui print do desempacotamento: ',item)
"""

for tupla_enumerada in enumerate(names):
    print('FOR DA TUPLA:')
    for valor in tupla_enumerada:
            print(f'\t{valor}')
