r1 = int(input('Primeiro segmento: '))
r2 = int(input('Segundo segmento: '))
r3 = int(input('Terceiro segmento: '))

if r1 == r2 == r3:
    print('Triângulo Equlátero')
elif r1 == r2 or r1 == r3 or r2 == r3:
    print('Triângulo Isóceles')
elif r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Triângulo Escaleno')
else:
    print('Não é triângulo')