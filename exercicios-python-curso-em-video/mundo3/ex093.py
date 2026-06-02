jogador = dict()
gols = list()
jogador['nome'] = str(input('Nome do Jogador: '))
qtdPartidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for cont in range(0, qtdPartidas):
    gols.append(int(input(f'   Quantos gols na partida {cont + 1}? ')))
jogador['gols'] = gols[:]
jogador['total'] = sum(gols)
print('-=' * 30)
print(jogador)
print('-=' * 30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-=' * 30)
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas.')
for i, v in enumerate(jogador['gols'], start = 1):
    print(f'   => na partida {i}, fez {v} gols.')
print(f'Foi um total de {jogador["total"]} gols.')
