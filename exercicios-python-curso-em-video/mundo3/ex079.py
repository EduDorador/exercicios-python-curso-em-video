valores = []
while True:
    num = int(input('Digite um valor para incluir na lista: '))
    if num not in valores:
        valores.append(num)
        print('Valor adicionado com sucesso...')
    else:
        print(f'O valor {num} já consta na lista, não vou adicionar!...')
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar? [S / N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('-=' * 20)
valores.sort()
print(f'Os valores digitados foram {valores}')
