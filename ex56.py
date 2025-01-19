soma_idade = 0
maior_idade = 0
maior_nome = ''
ms = ''
qtd_homem = 0
qtd_mulher = 0

for pess in range(1, 5):
    print(f'---{pess}ª pessoa---')
    nome = input("Nome: ")
    idade = int(input('Idade: '))
    sexo = input('Sexo [M/F]: ').strip().upper()
    soma_idade = idade + soma_idade
    if idade >= maior_idade:
        maior_idade = idade
        maior_nome = nome
        ms = sexo

    if sexo == 'F':
        qtd_mulher += 1
    elif sexo == 'M':
        qtd_homem += 1

print(f'A média de idade do grupo é de {soma_idade/pess}')
if ms == 'F':
    print(f'A mulher mais velha do grupo é a {maior_nome} que tem {maior_idade} anos')
elif ms =='M':
    print(f'O homem mais velho do grupo é o {maior_nome} que tem {maior_idade} anos')
print(f'A quantidade de mulheres é {qtd_mulher} e a de homens é {qtd_homem}')

