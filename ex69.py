qm = 0
qf = 0
id = 0
continuar = ' '

while True:
    print('-'*30)
    print('CADATRE UMA PESSOA')
    print('-'*30)
    idade = int(input('Idade: '))
    s1 = ' '
    while s1 not in 'MF':
        s1 = str(input('Sexo: [M/F] ')).strip().upper()[0]

    if idade >= 18:
        id += 1
    if s1 == 'M':
            qm += 1
    if s1 == 'F' and idade < 20:
            qf += 1

    while continuar not in 'SN':
        continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break

print(f'Total de pessoas com mais de 18 anos: {id}')
print(f'Total de homens cadastrados: {qm}')
print(f'Total de mulheres com menos de 20 anos cadastradas: {qf}')
