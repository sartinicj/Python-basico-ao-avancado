'''
0123456789
Olá Mundo
-987654321
Fatiamento [1:f:p] [::]
len retona a qtd de caractere da str
'''

var = 'Olá Mundo'
print(var[4:8])
print(var[:8]) #o numero colocado para fatiamento é o indice -1, entao no cado de 8, pegará até a posiçao 7
print(len(var))
print(var[0:len(var):2])
print(var[::-1])

