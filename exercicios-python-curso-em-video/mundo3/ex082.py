numeros = list()
pares = list()
impares = list()
while True:
    numeros.append(int(input('Digite um valor: ')))
    while True:
        resp = str(input('Deseja continuar? [S / N] ')).strip().upper()
        if resp in 'SN':
            break
        print('Tecla inválida. Digite S ou N, tente novamente...')
    if resp == 'N':
        break
for valor in numeros:
    if valor % 2 == 0:
        pares.append(valor)
    else:
        impares.append(valor)
pares.sort()
impares.sort()
print(f'A lista completa é {numeros}')
print(f'A lista de pares é {pares}')
print(f'A lista de ímpares é {impares}')
