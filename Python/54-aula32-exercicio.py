'''
Faça um algoritmo que peça ao usuario para digitar um numero inteiro.
informe se este é par ou impar. Caso não digite um numero 
inteiro, informe que não é um inteiro 
'''
'''
numb = int(input('Digite um número inteiro: '))

try:
    type(numb) == int:
        print('1')
    if numb % 2 == 0:
            print('o numero digitado é par')
    else:
            print('o numero digitado é ímpar')
except:
    print('4')
    print('o numero digitado não é inteiro')
'''

'''
Faça um programa que pergunte a hora ao usuario e, baseando-se 
no horario descrito, exiba a saudação apropriada. Ex.
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23
'''
'''
hour = int(input('Digite as horas: '))
if hour <= 11:
    print('Bom dia')
elif hour >= 12 and hour <= 17:
    print('Boa tarde')
else:
    print('Boa noite')    
'''

'''
Faça um programa que peça o primeiro nome do usuario. Se o nome tiver 4 letras
ou menos, escreva "seu nome é curto"; se tiver entre 5 e 6 letras, escreva
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande".
'''
'''
name = input('Digite seu nome: ')
print('0')
if len(name) == 4:
    print('1')
    print('Seu nome é curto')
elif len(name) > 4 and len(name) <= 6:
    print('2')
    print('Seu nome é normal')
elif len(name) >= 7:
    print('3')
    print('Seu nome é muito grande')
else:
    print('4')
    print('invalido')
'''         
 
