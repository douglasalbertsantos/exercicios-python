from datetime import date
atual = date.today().year
nasc = int(input('Ano de nascimento: '))
idade = atual - nasc

if idade > 18:
    print(f'Sua idade é {idade} e vc se alistou no ano de {nasc + 18}')
elif idade < 18:
    print(f'Sua idade é {idade} e vc se alistará em {nasc+18}')
else:
    print(f'Sua idade é {idade} e vc vai se alistar esse ano')