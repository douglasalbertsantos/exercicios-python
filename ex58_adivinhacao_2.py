from random import randint

npc = randint(1,10)
print("Pensei em um número de 0 a 10...")
n1 = int(input("Tente adivinhar que número é esse: "))
cont = 1

while n1 != npc:
    cont += 1
    if n1 > npc:
        n1 = int(input('Menos... Tente novo: '))
    elif n1 < npc:
        n1 = int(input('Mais... Tente novo: '))

print(f'Acertou miserávi.... o número que eu pensei foi {n1}')
if cont == 1: 
    print(f'Você acertou em {cont} tentativa') 
else: 
    print(f'Você acertou em {cont} tentativas')


