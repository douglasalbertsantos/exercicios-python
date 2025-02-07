produto = ' '
valor = 0
total = 0
menor_produto = ' '
menor_valor = 0
mil = 0
resp = ' '
contador = 0
print('-'*30)
print('-----LOJA-----')
print('-'*30)
while True:
    produto = str(input('Nome do produto: '))
    valor = int(input('Preço: R$'))
    total += valor
    contador += 1

    
    if valor >= 1000:
        mil += 1
    if contador == 1:
        menor_valor = valor
        menor_produto = produto
    if valor < menor_valor:
        menor_valor = valor
        menor_produto = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('-----FIM DO PROGRAMA-----')
print(f'O total da compra foi R${total}')
print(f'Temos {mil} produtos custando mais de R$1000')
print(f'O produto mais barato foi {menor_produto} que custa R${menor_valor}!')


