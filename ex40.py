n1 =float(input('Primeira Nota: '))
n2 =float(input('Segunda Nota: '))
media = (n1+n2)/2

print(f'Vc ficou com {media} e passou de Ano!!!') if media >= 7 else print(f'Vc ficou com {media} e está reprovado!!!')