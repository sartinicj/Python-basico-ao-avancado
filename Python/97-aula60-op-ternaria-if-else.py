'''
Operação Ternária (condição de uma linha)
<valor> if <condição> else <outro valor>
'''

print('Exemplo de operação ternaria com True: ')
print('Valor' if True else 'Outro valor')
print('\nExemplo de operação ternária com False: ')
print('Valor' if False else 'Outro valor')

10 == 10
print('\nExemplo de uma operação ternaria em variavel: ')
var = 'Valor' if True else 'Outro valor'
print(var)

10 == 11
print('\nExemplo de uma operação ternaria em variavel com False: ')
var = 'Valor' if False else 'Outro valor'
print(var)

digito = 9 # > 9 = 0
novo_digito = digito if digito <= 9 else 0
print(f'\nExemplo de if com numeros: {novo_digito}')
novo_invertido = 0 if digito > 9 else digito
print(f'\nExemplo de if com logica inversa: {novo_invertido})
