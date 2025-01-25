from random import randint

p1 = 0
p2 = ''
c1 = 0
c2 = ''
soma = 0
continuar = 'S'

while continuar not in ('nN'):
    p1 = int(input('Diga um valor: '))
    p2 = str(input('Par ou Ímpar? [P/I]')).strip().upper()

    c1 = randint(1,10)
    if p2 == "P": c2 = "I" 
    else: c2 = "I"

    soma = p1 + c1

    if soma % 2 == 0:
        print(f'Você jogou {p1}, o computador jogou {c1}. O total é {soma}, DEU PAR')
        if p2 == 'P':
            print(f'Parabéns, você venceu!!!')
        elif c2 == 'P':
            print(f'O Computador venceu...')

    elif soma % 2 != 0:
        print(f'Você jogou {p1}, o computador jogou {c1}. O total é {soma}, DEU ÍMPAR')
        if p2 == 'I':
            print(f'Parabéns, você venceu!!!')
        elif c2 == 'I':
            print(f'O Computador venceu...')

continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()

print('Jogo finalizado...')



