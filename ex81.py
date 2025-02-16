numeros = list()
cont = 0
cont5 = 0
while True:
    n = int(input('Digite um valor: '))
    numeros.append(n)
    cont += 1
    r = str(input('Quer continuar? [S/N]: '))
    if r in 'Nn':
        break
numeros.sort(reverse=True)


print(f'Você digitou {cont} elementos')
print(f'Os valores em ordem reversa são: {numeros}')
if 5 in numeros:
    print('O valor 5 está na lista')
else:
    print('O valor 5 não está na lista')
