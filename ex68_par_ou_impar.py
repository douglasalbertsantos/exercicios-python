from random import randint
v = 0
while True:
    p1 = int(input('Digite um número: '))
    c1 = randint(0,10)
    tot = p1 + c1
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
    print(f'Você jogou {p1} e o computador jogou {c1}. O total é {tot}')
    if tipo == 'P':
        if tot % 2 == 0:
            print('Você Venceu!!!')
            v +=1
        else:
            print('Você Perdeu...')
            break

    if tipo == 'I':
        if tot % 2 == 1:
            print('Você Venceu!!!')
            v +=1
        else:
            print('Você Perdeu...')
            break
    print ('vamos jogar novamente...')

print(f'Game Over! Você venceu {v} vezes')
            
