from random import randint
from time import sleep
lista = list()
jogos = list()
print('-'*30)
print('     Jogos da MEGA SENA     ')
print('-'*30)
quant = int(input('Quantos jogos vc quer sortear? '))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(1,60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1

print(f'Sorteando {quant} jogos...')
print()
sleep(2)
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    sleep(1)
print()
print('----------BOA SORTE!----------')
print()
print()