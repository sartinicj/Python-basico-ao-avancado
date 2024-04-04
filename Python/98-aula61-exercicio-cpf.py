'''
4devs.com.br/gerador_de_cpf
Exercicios: Calcule do primeiro digito do CPF

CPF: 746.824.890-70
Colete a soma dos 9 primeiros digitos do CPF multiplicando cada um dos valores por uma contagem regressiva começando do 10

Ex.: 746.824.890-70 (746824890)
...10...9...8...7...6...5...4...3...2 
*...7...4...6...8...2...4...8...9...0
...70..36..48...56..12..20..32..27..0

Somar todos os resultados:
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301*10 = 3010
Obter o resto da divisão anterior por 11
3010%11 = 7
Se o resultado anterior for maior que 9:
resultado é 0
contrario disso:
resultado é o valor da conta

O primeio digito do CPF é 7
'''