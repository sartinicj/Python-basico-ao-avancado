import decimal
#Função decimal serve para fazer contas exatas, sem aproximação

num1 = 0.1
num2 = 0.7
num3 = num1 + num2
num4 = decimal.Decimal('0.1')
num5 = decimal.Decimal('0.7')
print(f'Saída sem formatação será: {num3}')
print(f'Saída com formatação será: {num3:.1f}')
print('A função round tambem funciona: ')
print(round(num3, 2))