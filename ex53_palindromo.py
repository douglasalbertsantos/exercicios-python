frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''

for c in range(len(junto) - 1, -1, -1):
    inverso += junto[c]

if inverso == junto:
    print(f'O inverso de {junto} é: {inverso}')
    print('Temos um PALÍNDROMO')
else:
    print(f'O inverso de {junto} é: {inverso}')





