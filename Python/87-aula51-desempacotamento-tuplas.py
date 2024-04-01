"""
Introdução ao desempacotamento + tuples
"""

names = ['Cecilia', 'Douglas', 'Sabrina']
name1, name2, name3 = names
print(name2)


name1, name2, name3 = ['Cecilia', 'Douglas', 'Sabrina']
print(name2)

"""
name1, name2 = ['Cecilia', 'Douglas', 'Sabrina']
print(name2)
UNPACK ERROR

name1, *_ = ['Cecilia', 'Douglas', 'Sabrina']
print(name1, _)
_, name2, *_ = ['Cecilia', 'Douglas', 'Sabrina']
*_ indica resto da lista a ser guardada
"""

