p1 = float(input('Qual o valor da compra: R$'))

print('''FORMAS DE PAGAMENTO
      [ 1 ] à vista
      [ 2 ] à vista cartão
      [ 3 ] 2x no cartão
      [ 4 ] 3x ou mais no cartão''')
op1 = int(input('Qual a opção? '))

if op1 == 1:
    print(f'Sua compra de R${p1} sairá por R${p1-(p1*10/100)}')
elif op1 == 2:
    print(f'Sua compra de R${p1} sairá por R${p1-(p1*5/100)}')
elif op1 == 3:
    print(f'Sua compra ficará por R${p1}')
elif op1 == 4:
    par = int(input('Em quantas parcelas vai pagar? '))
    p2 = p1+(p1*20/100)
    print(f'Sua compra de R${p1} sairá por R${p2}')
    print(f'Cada parcela ficará no valor de {p2/par}')
else:
    print('Vc não digitou uma opção válida')