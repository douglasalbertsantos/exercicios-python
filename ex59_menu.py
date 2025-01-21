n1 = int(input("Primeiro valor: "))
n2 = int(input("Segundo valor: "))
np = 0

while np != 5:
    print('''
[ 1 ] Somar
[ 2 ] Multiplicar
[ 3 ] Maior
[ 4 ] Novos números
[ 5 ] Sair do Programa''')
    np = int(input('>>> Qual a sua opção? '))

    if np == 1:
        print(f'{n1} + {n2} = {n1+n2}')
    
    elif np == 2:
        print(f'{n1} x {n2} = {n1*n2}')

    elif np == 3:
        if n1 > n2:
            print(f'Entre {n1} e {n2} o maior número é: {n1}')
        elif n2 > n1:
            print(f'Entre {n1} e {n2} o maior número é: {n2}')
        else:
            print("Os números digitados são iguais")
    
    elif np == 4:
        print('Informe os números novamente:')
        n1 = int(input("Primeiro valor: "))
        n2 = int(input("Segundo valor: "))

    elif np == 5:
        print('Saindo do Menu')

    else:
        print('Opção inválida, tente novamente')
        


    print('=-='*10)

print("Programa Finalizado...")