from random import randint
from time import sleep
números = list()

def sorteia(lista):
    print(f'Sorteando 5 valores para lista: ',end='')
    sleep(2)
    for cont in range(0, 5):
        n = randint(1, 10)
        lista.append(n)
        print(f'{n}, ', end='')
        sleep(0.4)
    print('PRONTO!')


def somaPar(lista):
    totPar = 0
    for valor in lista:
        if valor % 2 == 0:
            totPar += valor
    print(f'Somando os valores pares de {lista} temos, {totPar}')

#Programa Principal
sorteia(números)
somaPar(números)
