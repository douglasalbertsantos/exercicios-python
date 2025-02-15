numeros = list()
while True:
    n = int(input('Digite um valor: '))
    if n not in numeros: 
        numeros.append(n)
    else:
        print('Número repetido não adicionado...')

    r = str(input('Quer continuar? [S/N]: '))
    if r in 'Nn':
        break
numeros.sort()
print(f'Os números digitados foram: {numeros}')
