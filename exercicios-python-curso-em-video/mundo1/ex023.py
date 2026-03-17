numero = int(input('Informe um número: '))
print(f'Analisando o número {numero}...')

print(f'Unidade: {numero // 1  % 10}')
print(f'Dezena: {(numero // 10) % 10}')
print(f'Centena: {(numero // 100) % 10}')
print(f'Milhar: {(numero // 1000) % 10}')
