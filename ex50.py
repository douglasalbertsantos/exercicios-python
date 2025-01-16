s = 0
n = 0
pares = 0
for c in range (1,7):
    s = int(input('Digite um número: '))
    if s % 2 == 0:
        n = n + s
        pares += 1

print (f"Vc informou {pares} números pares que somados dão {n}")