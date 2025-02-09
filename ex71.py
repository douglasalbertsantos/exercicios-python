valor = int(input("Qual o valor vc quer sacar? R$"))
cont50 = 0
cont20 = 0
cont10 = 0
cont01 = 0

while valor >= 50:
    cont50 += 1
    valor = valor - 50

while valor >= 20:
    cont20 += 1
    valor = valor - 20

while valor >= 10:
    cont10 += 1
    valor = valor - 10

while valor >= 1:
    cont01 += 1
    valor = valor - 1

print(f"Vc usou {cont50} cédulas de R$50,{cont20} cédulas de R$20, {cont10} cédulas de R$10, {cont01} cédulas de R$1")