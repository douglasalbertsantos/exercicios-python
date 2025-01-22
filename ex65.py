n1 = 0
maior = 0
menor = 0
cont = 0
soma = 0
sn = ''

while sn != "N":
    n1 = int(input('Digite um numero: '))
    cont += 1
    soma += n1
    if cont == 1:
        maior = n1
        menor = n1
    elif n1 > maior:
        maior = n1
    elif n1 < menor:
        menor = n1
    sn = str(input('Deseja continuar? [S/N] ')).strip().upper()

print(f'Você digitou {cont} números e a média deles é: {soma/cont}')
print(f'O maior valor foi {maior} e o menor valor foi {menor}')
