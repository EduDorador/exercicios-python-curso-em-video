num = int(input('Digite um número para visualizar sua tabuada: '))
print('=' * 14)
print(f"{f'TABUADA DO {num:^14}':^14}")
print('=' * 14)
for c in range(1, 11):
    print(f'{num} x {c:2} = {num * c}')
