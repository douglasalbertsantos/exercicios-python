a1 = int(input('Digite o primeiro termo da PA: '))
r1 = int(input('Digite a razão: '))

for c in range(a1, (a1+(9*r1))+1, r1):
    print(f'{c}', end = ' - ')

print('fim')
