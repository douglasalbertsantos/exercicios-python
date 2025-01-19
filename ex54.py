from datetime import date
atual = date.today().year
maior = 0
menor = 0
n1 = 0

for c in range(1, 8):
    n1 = int(input(f"Em que ano a {c}ª pessoa nasceu: "))
    if n1 > atual - 18:
        menor += 1
    else:
        maior += 1

print(f'Ao todo tivemos {menor} pessoas menor de idade')
print(f'e {maior} pessoas maior de idade')     