num_ext = ('zero', 'um','dois', 'três', 'quatro', 
           'cinco', 'seis', 'sete', 'oito',
           'nove', 'dez', 'onze', 'doze', 'treze', 
           'quatorze', 'quinze', 'dezesseis', 'dezessete',
           'dezoito', 'dezenove', 'vinte')
while True:
    num = int(input('Digite um número entre 0 e 20: '))
    if 0 <= num <= 20:
       print(f'Você digitou o número {num_ext[num]}')
       print('=' * 30)
       resp = str(input('Deseja continuar? [S / N]: ')).strip().upper()[0]
       print('=' * 30)
       if resp == 'N':
           print('Finalizando o programa...')
           break
    else:
        print('Número inválido, tente novamente! ', end='')
