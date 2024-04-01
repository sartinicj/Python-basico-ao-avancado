entrada = input('Para iniciar escolha 1; sair, 0: ')
while entrada == '1':
    print('### Calculadora ###')
    num1 = int(input('Digite o primeiro valor: '))
    num2 = int(input('Digite o segundo valor: '))
    op = input('Qual a operação desejada? ')
    if op == '+':
        soma = num1 + num2
        print('A soma é ', soma)
    elif op == '-':
        sub = num1-num2
        print('O resultado é ', sub)
    elif op == '*':
        prd = num1*num2
        print('O produto é ', prd)
    elif op == '/':
        quo = num1/num2
        print('O quociente é ', quo)
    else:
        print('Entrada invalida!')
            
print('Fim de execução!')  

#    TODO: criar a lógica de forma que na segunda vez que passar pela calculadora, perguntar se quer digitar novos numeros ou outra operação
#    valor = input('Digitar novo valor?s/n ')
#    while valor = 'n':
