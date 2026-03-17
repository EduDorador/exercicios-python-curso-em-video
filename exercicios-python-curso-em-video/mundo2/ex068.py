from random import randint
print('=-' * 14)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-' * 14)
vitoria = 0
while True:
    jogador = int(input('Digite um número: '))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar? [P/I]')).strip().upper()[0]
    print('=-' * 14)
    print(f'Você jogou o número {jogador} e o computador jogou o número {computador}. Total de {total}. ', end='')
    print('DEU PAR!' if total % 2 == 0 else 'DEU ÍMPAR!')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você VENCEU!')
            vitoria += 1
        else:
            print('Você PERDEU!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você VENCEU!')
            vitoria += 1
        else:
            print('Você PERDEU!')
            break
    print('Vamos jogar novamente...')
    print('=-' * 14)
print('=-' * 14)
print(f'GAME OVER! Você ganhou {vitoria} vezes. ')
