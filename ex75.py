n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))
n4 = int(input('Digite o quarto número: '))
numeros = (n1, n2, n3, n4)

print(f'Os números digitados são:')
for num in numeros:
    print(f'{num}, ', end='')

print(f'\nO número 9 aparece {numeros.count(9)} vezes')
if 3 in numeros:
    print(f'O valor 3 apareceu primeiro na {numeros.index(3)+1}ª posição')
else:
    print('O número 3 não foi digitado')
print('Os valores pares digitados são: ', end='')
for n in numeros:
    if n % 2 == 0:
        print(n, end=' ')