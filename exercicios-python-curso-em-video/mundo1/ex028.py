from random import randint
from time import sleep
maq = randint(0, 5)
print('-=-' * 15)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 15)
num = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
sleep(2)
if num == maq:
    print(f'PARABÉNS! Você conseguiu me vencer!')
else:
    print(f'Você perdeu! Eu pensei no número {maq} e não no {num}')
