matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
num = 0
par = 0
ter = 0
maior = 0
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Digite o valor para [{l}, {c}]: '))
        if matriz[l][c] % 2 == 0:
            par += matriz[l][c]
        if matriz[l][c] == matriz[0][2] or matriz[1][2] or matriz[2][2]:
            ter += matriz[l][c]
        if matriz[l][c] == matriz[1][0] or matriz[1][1] or matriz[1][2]:
            if matriz[l][c] == matriz[1][0]:
                ter = matriz[1][0]
            elif matriz[1][1] > matriz[1][0]:
                ter = matriz[1][1]
            elif matriz[1][2] > matriz[1][0] or matriz[1][2] > matriz[1][1]:
                ter = matriz[1][2]


for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()

print(f'A soma dos valores pares é: {par}')
print(f'A soma da terceira coluna é: {ter}')
print(f'O maior valor da segunda linha é: {maior}')