times = ('Botafogo', 'Palmeiras', 'Flamengo', 'Fortaleza', 'Internacional', 'São Paulo', 'Corinthians', 'Bahia', 'Cruzeiro', 'Vasco da Gama', 'EC Vitória', 'Atlético-MG', 'Fluminense', 'Grêmio', 'Juventude', 'Bragantino', 'Athletico-PR', 'Criciuma', 'Atletico-GO', 'Cuiabá')

print('-='*15)
print(f'Lista dos times no fianl do Brasileirão de 2024: {times}')
print('-='*15)
print(f'Lista dos 5 primeiros colocados: {times[0:5]}')
print('-='*15)
print(f'Lista dos 4 últimos colocados: {times[-4:]}')
print('-='*15)
print(f'Lista dos times em ordem alfabética: {sorted(times)}')
print('-='*15)
print(f'O São Paulo ficou na {times.index("São Paulo")+1}ª posição')
print('-='*15)