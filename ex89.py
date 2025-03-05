ficha = list()
while True:
    nome = str(input("Nome: "))
    nota1 = float(input("Nota1: "))
    nota2 = float(input("Nota2: "))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    resp = str(input('Desja continuar? [S/N] '))
    if resp in 'nN':
        break

print('-='*30)
print(f'{"Nº":<4}{"NOME":<10}{"MÉDIA":>8}')
print()
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:8.1f}')

print()
while True:
    print('--'*30)
    opc = int(input('Mostrar nota de qual aluno? [999 interrompe]'))
    if opc == 999:
        print('Finalizando...')
        break
    if opc <= len(ficha) - 1:
        print(f'As notas de {ficha[opc][0]} são {ficha[opc][1]}')

print()
print('-='*30)