time = list()
jogador = dict()
gols = list()
while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do Jogador: '))
    qtdPartidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    gols.clear()
    for cont in range(0, qtdPartidas):
        gols.append(int(input(f'   Quantos gols na partida {cont + 1}? ')))
    jogador['gols'] = gols[:]
    jogador['total'] = sum(gols)
    time.append(jogador.copy())
    while True:
        resp = str(input('Deseja continuar? [S / N] ')).strip().upper()[0]
        if resp in 'SN':
            break
        print('Erro! Digite S ou N.')
    if resp == 'N':
        break
print('-=' * 30)
print('cod', end='')
for k in jogador.keys():
    print(f' {str(k):<15}', end='')
print()
print('-' * 40)
for i, j in enumerate(time):
    print(f' {str(i):<3}', end='')
    for v in j.values():
        print(f'{str(v):<15}', end='')
    print()
print('-' * 40)
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar): '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'Erro! Não existe jogador com o código {busca}!')
    else:
        print(f'__ LEVANTAMENTO DO JOGADOR {time[busca]["nome"]} __')
        for k, v in enumerate(time[busca]['gols']):
            print(f'   No jogo {k+1} fez {v} gols.')
    print('-' * 40)
print('<<< ENCERRANDO! >>>')
