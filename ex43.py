peso = float(input('Qual o peso: Kg '))
alt = float(input('Qual a altura: m '))
imc = peso / (alt ** 2)

print(f'O IMC é: ')

if imc < 18.5:
    print('Abaixo do peso')
elif imc < 25:
    print('Peso ideal')
elif imc < 30:
    print('Sobrepeso')
elif imc < 40:
    print('Obesidade')
else: 
    print('Obesidade Mórbida')