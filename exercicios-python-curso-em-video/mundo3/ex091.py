from random import randint
from operator import itemgetter
from time import sleep
jogadores = dict()
ranking = list()
for cont in range(1, 5):
    jogadores[f'jogador{cont}'] = randint(1 , 6)
print('Os valores sorteados são:')
for k, v in jogadores.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)
print('-=' * 30)
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
print(' === RANKING DOS JOGADORES === ')
for i, v in enumerate(ranking, start=1):
    print(f'   {i}º Lugar: {v[0]} com {v[1]}')
    sleep(1)
