n1 = int(input("Primeiro termo: "))
ra = int(input("Razão da PA: "))
qt = n1
cont = 1
total = 0
mais = 10

while mais != 0:
    total += mais
    while cont <= total:
        print(f'{qt} → ',end = '')
        qt += ra
        cont += 1
    print('PAUSA')
    mais = int(input("Quantos termos vc quer mostrar a mais? "))

print('FIM')