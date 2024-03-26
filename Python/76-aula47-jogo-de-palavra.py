'''
Faça um jogo para o usuario adivinhar qual a palavra secreta.
- Você vai propor uma palavra secreta qualquer e vai dar a possibilidade
para o usuario digitar apenas uma letra.
- Quando o usuario digitar uma letra, você vai conferir se a letra digitada 
está na palavra secreta.
    - Se a letra digitada está na palavra secreta; exiba a letra;
    - Se a letra digitada não está na palavra secreta; exiba *;
- Faça a contagem de tentativas do seu usuário.     
'''

code = 'muito'
i = 0
user = True
print('Boa sorte ao tentar desvendar a a palvra!')
for user in code:
    tries = input('Digite uma letra: ')
    if tries in code:
        print(tries)
        i += 1
    else:
        print('*')
    
    