galera = list()
dado = list()
mai = men = cont = 0
while True:
    dado.append(str(input('Nome: ')))
    dado.append(float(input('Peso: ')))
    if len(galera) == 0:
        mai = men = dado[1]
    else:
        if dado [1] > mai:
            mai = dado[1]
        if dado [1] < men:
            men = dado[1]
    galera.append(dado[:])
    dado.clear()
    cont += 1
    r = str(input('Quer continuar? [S/N]: '))
    if r in 'Nn':
        break

print(f'Ao todo você cadastrou {len(galera)} pessoas')
print(f'O maior peso foi de {mai}, das pessoas: ')
for p in galera:
    if p[1] == mai:
        print(f'{p[0]}, ', end='')
print(f'\nO menor peso foi de {men}, das pessoas: ')
for p in galera:
    if p[1] == men:
        print(f'{p[0]}, ', end='')




