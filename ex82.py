numeros = list()
pares = list()
impares = list()
while True:
    numeros.append(int(input('Digite um valor: ')))
    r = str(input('Quer continuar? [S/N]: '))
    if r in 'Nn':
        break
for i, v in enumerate(numeros):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        impares.append(v)

numeros.sort()
pares.sort()
impares.sort()
print(f'A lista completa é: {numeros}')
print(f'A lista de números pares é: {pares}')
print(f'A lista de números ímpares é: {impares}')