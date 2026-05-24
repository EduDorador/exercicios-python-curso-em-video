valores = list()
while True:
    valores.append(int(input('Digite um valor: ')))
    while True:
        resp = str(input('Deseja continuar? [S / N] ')).strip().upper()
        if resp in 'SN':
            break
        print('Tecla inválida, tente novamente. Digite S ou N!')
    if resp == 'N':
        break
print(f'Foram digitados {len(valores)} elementos.')
valores.sort(reverse=True)
print(f'Os valores em ordem decrescente é: {valores}')
if 5 in valores:
    print('O número 5 está na lista!')
else:
    print('O número 5 não foi encontrado!')
