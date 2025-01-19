maior = 0
menor = 0
peso = 0

for pess in range(1, 6):
    peso = float(input(f'Peso da {pess}ª pessoa: '))
    if pess == 1:
        maior = peso
        menor = peso
    elif peso >= maior:
        maior = peso
    elif peso <= menor:
        menor = peso

print(f'O maior peso foi: {maior}')
print(f'O menor peso foi: {menor}')


    