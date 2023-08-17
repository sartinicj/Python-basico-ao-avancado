'''
#.......012345678910
nome = 'Luiz Otavio'
#......1110987654321
tamanho_nome = len(nome)
print(nome)
print(tamanho_nome)
print(nome[3])

nova_string += '*L*u*i*z* *O*t*a*v*i*o' 

###

0123456789
Olá Mundo
-987654321
Fatiamento [1:f:p] [::]
len retona a qtd de caractere da str


var = 'Olá Mundo'
print(var[4:8]) #imprime posição 4 a 8
print(var[:8]) #imprime atéposição 8 #o numero colocado para fatiamento é o indice -1, entao no cado de 8, pegará até a posiçao 7
print(len(var)) #imprime quantidade de posições
print(var[0:len(var):2]) #imprime pulando posições
print(var[::-1]) #imprime invertido

'''

name = input('Digite seu nome: ')
name_size = len(name)

while name_size == name_size:
    name_upd = (name[0:len(name):2])
print(name_upd)
print('Seu nome após a iteração será:', name_upd)