from random import randint
from time import sleep
lista = list()
jogos = list()
print('-' * 30)
print('     JOGA NA MEGA SENA     ')
print('-' * 30)
quant = int(input('Quantos jogos deseja que eu sorteie? '))
tot = 0
while True:
    cont = 1
    while cont <= 6:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
    if tot == quant:
        break
print('-=' * 5, f'SORTEANDO {quant} JOGOS', '-=' * 5)
for pos, num in enumerate(jogos, start=1):
    print(f'Jogo {pos}: {num}')
    sleep(1)
print('-=' * 5, '< BOA SORTE! >', '-=' * 5)
