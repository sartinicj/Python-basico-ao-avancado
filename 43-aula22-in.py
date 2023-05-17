name = input('Digite o nome: ')
found = input('Digite o que deseja encontrar: ')

if found in name:
    print(f'{found} está em {name}')
else:
        print(f'{found} não está em {name}')