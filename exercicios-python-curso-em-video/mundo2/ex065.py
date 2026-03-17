resp = 'S'
media = maior = menor = cont = soma = 0
while resp in 'Ss':
    num = int(input('Digite um número: '))
    soma += num
    cont += 1
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input('Deseja continuar? [S/N] ')).strip().upper() [0]
media = soma / cont
print(f'A média entre os valores digitados é {media}')
print(f'O maior valor digitado foi {maior}')
print(f'O menor valor digitado foi {menor}')
