num = int(input('Digite um número para calcular seu fatorial: '))
c = num
f = 1
print(f'Fatorial de {num}!')
while c > 0:
    if c > 1:
        print(f'{c} x', end=' ')
    else:
        print(f'{c} =', end=' ')
    f *= c
    c -= 1
print(f)
