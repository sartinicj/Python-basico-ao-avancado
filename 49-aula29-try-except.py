num_str = input('Vou dobrar o numero que voce digitar: ')

try:
    num_flt = float(num_str)
    print('FLOAhT: ', num_flt)
    print(f'O dobro de {num_str} é: {num_flt*2}')
except:
    print('Isso não é um número!')
    
    
    #if num_str.isdigit():
    #   num_flt = float(num_str)
    #    print(f'O dobro de {num_str} é: {num_flt*2}')
    #else:
    #    print('Isso não é um número!')