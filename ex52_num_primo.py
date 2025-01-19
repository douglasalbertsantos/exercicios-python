n1 = int(input('Digite um número: '))
t1 = 0

for c in range(1, n1 + 1):
    if n1 % c == 0:
        print('\033[33m', end = ' ')
        t1 += 1
    else:
        print('\033[31m', end = ' ')
    print(f'{c}', end = '')

print(f'\n\033[mO número {n1} foi divísivel {t1} vezes')
if t1 == 0:
    print(f'Por isso, {n1} NÃO é um número PRIMO')
else:
    print(f'Por isso, {n1} é um número PRIMO')