num = int(input('Digite um número para calcular o seu Fatorial: '))
f = 1
for c in range(num, 0, -1):
    print(f'{c}', end=' ')
    print(f'x' if c > 1 else '=', end=' ')
    f *= c
print(f)
