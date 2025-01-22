n1 = cont = 0

while True:
    n1 = int(input("Quer ver a tabuada de qual valor? "))
    print('_'*30)
    print('')
    cont = 1
    if n1 < 0:
        break
    while cont < 11:
        print(f'{n1} x {cont} = {n1 * cont}')
        cont +=1
    print('_'*30)
    print('')
print('PRAGRAMA FINALIZADO')