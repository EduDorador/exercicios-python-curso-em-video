print('=' * 40)
print(f"{'BANCO CEV':^40}")
print('=' * 40)
valor = int(input('Qual valor você quer sacar? R$ '))
total = valor
ced = 50
totCed = 0
while True:
    if total >= ced:
        total -= ced
        totCed += 1
    else:
        if totCed > 0:
            print(f'Total de {totCed} cédulas de R$ {ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totCed = 0
        if total == 0:
            break
print('=' * 40)
print('volte sempre ao banco CEV! Tenha um bom dia!!')
