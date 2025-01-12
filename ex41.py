from datetime import date
atual = date.today().year
nasc = int(input('Data de nascimento do atleta: '))
idade = atual - nasc

if idade <= 9:
    print('Mirim')
elif idade <= 14:
    print("Infantil")
elif idade <= 19:
    print("Junior")
elif idade <= 25:
    print('Sênior')
else: 
    print('Master')