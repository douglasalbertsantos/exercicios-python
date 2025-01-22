qtd = int(input('Quantos termos vc quer mostrar? '))
cont = 1
f1 = 0
f2 = 1
f3 = 0
print('0 → ', end = '')
while cont <= qtd:
    f3 = f1 + f2
    print(f'{f3} → ', end = '')
    f1 = f2
    f2 = f3
    cont += 1

print('FIM')