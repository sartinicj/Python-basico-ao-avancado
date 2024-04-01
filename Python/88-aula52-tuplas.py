"""
Tipo tupla: uma lista imutavel
"""

# Uma lista pode-se alterar o valor:
names = ['Cecilia', 'Douglas', 'Sabrina']
names[1] = 'outro'
_, _, name, *others = names
print(names)
print(name)

# Uma tupla é usada quando nao se tem alterações de dados:
names = 'Cecilia', 'Douglas', 'Sabrina'
print(names[-1])
print(names)

# É possível se converter lista em tupla e vice versa:
names = ['Cecilia', 'Douglas', 'Sabrina']
names = tuple(names)
names = list(names)
print(names[-1])
print(names)
