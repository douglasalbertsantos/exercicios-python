num = [[], []]
n = 0
for c in range(1,8):
    n = int(input(f'Digie o {c}º número: '))
    if n % 2 == 0:
        num[0].append(n)
    else:
        num[1].append(n)
num[0].sort()
num[1].sort()
print(f'Os valores pares foram: {num[0]}')
print(f'Os valores ímpares foram: {num[1]}')
