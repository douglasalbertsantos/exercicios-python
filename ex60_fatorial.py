n1 = int(input('Digite um número para calcular o seu Fatorial: '))
nf = n1
tot = n1
print(f'Calculando {n1}! = {n1} ',end = '')
while nf > 1:
    nf = nf -1
    print(f'x {nf} ',end = '')
    tot *= nf

print(f'= {tot}')