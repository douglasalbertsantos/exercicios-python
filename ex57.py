s1 = str(input('Digite o sexo [M/F]: ')).strip().upper()
while s1 not in 'MmFf':
    s1 = str(input('Registro inválido, tente de novo [M/F]: ')).strip().upper()


print('Regsitro feito com sucesso!')
print('Processo finalizado')
