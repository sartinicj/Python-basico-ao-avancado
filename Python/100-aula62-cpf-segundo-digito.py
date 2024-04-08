'''
Calculo do segundo digito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros digitos MAIS O PRIMEIRO DIGITO, multiplicando cada um dos valores regressivamente do 11

Ex.: 746.824.890-70 (746824890)
...11..10...9...8...7...6...5...4...3...2 
*...7...4...6...8...2...4...8...9...0...7
...77..40..54...64..14..24..40..36..0...14

Somar todos os resultados:
77+40+54+64+14+24+40+36+0+14 = 363
Multiplicar o resultado anterior por 10
363*10 = 3630
Obter o resto da divisão anterior por 11
3630%11 = 0
Se o resultado anterior for maior que 9:
resultado é 0
contrario disso:
resultado é o valor da conta

O segundo digito do CPF é 0
'''

cpf = '36113696839'
novo_digitos = cpf[:9]
regresso = 11
onze = novo_digitos + novo_digitos[:1]
res = 0

for digito in onze:
    res += int(onze) * regresso
    regresso -= 1
    
    dez = res * 10
    mod = dez % 11

if mod > 9:
    final = 0
else:
    final = mod

print(f'O segundo digito do CPF é: {final}')


