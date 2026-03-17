from random import randint
from time import sleep
lista = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''Escolha uma Opção:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Qual é sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
if jogador < 0 or jogador > 2:
    print('JOGADA INVÁLIDA!')
else:
    print('-=-' * 10)
    print(f'O computador jogou: {lista[computador]}')
    print(f'O jogador jogou: {lista[jogador]}')
    print('-=-' * 10)
    if computador == 0:
        if jogador == 0:
            print('EMPATE!')
        elif jogador == 1:
            print('JOGADOR VENCEU!')
        elif jogador == 2:
            print('COMPUTADOR VENCEU!')
    elif computador == 1:
        if jogador == 0:
            print('COMPUTADOR VENCEU!')
        elif jogador == 1:
            print('EMPATE!')
        elif jogador == 2:
            print('JOGADOR VENCEU!')
    elif computador == 2:
        if jogador == 0:
            print('JOGADOR VENCEU!')
        elif jogador == 1:
            print('COMPUTADOR VENCEU!')
        elif jogador == 2:
            print('EMPATE!')
