'''
split e join com list e str
split divide uma string
join une uma string
'''

frase = '    Olha só que, coisa interessante    '
print(frase)
lista_palavra = frase.split()
print(f'Para tirar os espaços desnecessarios de uma frase usa-se o split: {lista_palavra}')
lista_palavra = frase.split(', ')
print(f'Para separar uma frase sempre que tiver uma virgula e espaço, coloca-se tal argumento como parametro do aplit: {lista_palavra}')

lista_frases_corretas = []
for i, frases in enumerate(lista_palavra):
    lista_frases_corretas.append(lista_palavra[i].strip())
    
print(f'Assim era a saída inicial: {lista_palavra}')
print(f'Assim ficou a saída splitada: {lista_frases_corretas}')

frases_unidas = '-'.join('abc')
print(f'O join une uma string com o separador fornecido, no caso o hifen: {frases_unidas}')
frases_unidas = '-'.join(lista_frases_corretas)
print(frases_unidas)