num = int(input('Digite um número: '))
print('''Escolha uma das opções: 
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')
op = int(input('QUal sua opção: '))

if op == 1:
    print(f'{num} convertido para binário fica: {bin(num)}')
elif op == 2:
    print(f'{num} convertido para binário fica: {oct(num)}')
elif op == 3:
    print(f'{num} convertido para binário fica: {hex(num)}')
else:
    print('Vc não digitou uma opção válida')