times = ('Palmeiras', 'São Paulo', 'Fluminense', 'Bahia',
         'Flamengo', 'Coritiba', 'Gremio', 'Athletico-PR',
         'Corinthians', 'Vasco', 'Atletico-MG', 'Bragantino',
         'EC Vitoria', 'Chapecoense', 'Botafogo', 'Mirasol',
         'Santos', 'Internacional', 'Cruzeiro', 'Remo')
print('-=' * 50)
print(f'Lista de times do Brasileirão: {times}')
print('-=' * 50)
print(f'Os 5 primeiros times são: {times[:5]}')
print('-=' * 50)
print(f'Os 4 últimos times são: {times[-4:]}')
print('-=' * 50)
print(f'Times em ordem alfabética: {sorted(times)}')
print('-=' * 50)
print(f'O Chapecoense está na {times.index("Chapecoense") + 1}ª posição')
