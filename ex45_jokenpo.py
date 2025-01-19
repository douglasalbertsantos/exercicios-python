from time import sleep
from random import randint
print('''Suas opções: 
      [ 1 ] PEDRA
      [ 2 ] PAPEL
      [ 3 ] TESOURA''')
p1 = int(input('Qual é a sua jogada? '))
pc = randint(1, 3)
sleep(0.5)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!!!')
sleep(1)

if p1 == 1: print("O Jogador escolheu PEDRA")
elif p1 == 2: print("O Jogador escolheu PAPEL")
elif p1 == 3: print("O Jogador escolheu TESOURA")
sleep(2)

if pc == 1: print("O Computador escolheu PEDRA")
elif pc == 2: print("O Computador escolheu PAPEL")
elif pc == 3: print("O Computador escolheu TESOURA")

sleep(1)

if (p1 == 1 and pc == 3) or (p1 == 2 and pc == 1) or (p1 == 3 and pc == 2):
    print("O JOGADOR venceu!!!")
elif (pc == 1 and p1 == 3) or (pc == 2 and p1 == 1) or (pc == 3 and p1 == 2):
    print("O COMPUTADOR venceu!!!")
elif (pc == 1 and p1 == 1) or (pc == 2 and p1 == 2) or (pc == 3 and p1 == 3):
    print("EMPATE")
else:
    print('O Jogador não escolheu uma opção válida!')

