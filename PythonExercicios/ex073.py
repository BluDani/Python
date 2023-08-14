times = ('Palmeiras', 'Santos', 'Vasco da Gama', 'Grêmio', 'Flamengo', 'Corinthians',
         'Internacional', 'Cruzeiro', 'São Paulo', 'Atlético Mineiro', 'Botafogo',
         'Fluminense', 'Coritiba', 'Bahia', 'Goiás', 'Guarani', 'Sport', 'Portuguesa',
         'Atlético Paranaense', 'Vitória')

print('-=-=' * 10)
print(f'Lista de times do Brasileirão 2013: {times}')
print('-=-=' * 10)
print(f'Os 5 primeiros são {times[:5]}')
print('-=-=' * 10)
print(f'Os 4 últimos são {times[-4:]}')
print('-=-=' * 10)
print(f'Times em ordem alfabética: {sorted(times)}')
print('-=-=' * 10)
print(f'O Botafogo está na posição {times.index("Botafogo")}')
