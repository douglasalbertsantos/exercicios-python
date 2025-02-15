numeros = [int(input('Digite um valor na posição 0: ')), int(input('Digite um valor na posição 1: ')), int(input('Digite um valor na posição 2: ')), int(input('Digite um valor na posição 3: ')), int(input('Digite um valor na posição 4: '))]

print(f'Você digitou os valores: {numeros}')

print(f'O maior valor digitado foi {max(numeros)} na posição {numeros.index(max(numeros))}')
print(f'O menor valor digitado foi {min(numeros)} na posição {numeros.index(min(numeros))}')