n1 = int(input("Primeiro termo: "))
ra = int(input("Razão da PA: "))
qt = int(input("Quantos termos terá a PA: "))
cont = 0

while cont != qt:
    print(f'{n1} → ',end = '')
    n1 += ra
    cont += 1

print('FIM')