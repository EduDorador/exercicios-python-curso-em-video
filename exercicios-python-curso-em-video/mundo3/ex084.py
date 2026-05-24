principal = list()
temp = list()
maiorPeso = menorPeso = 0
while True:
    temp.append(str(input('Nome: ')).strip())
    temp.append(float(input('Peso: ')))
    if len(principal) == 0:
        maiorPeso = menorPeso = temp[1]
    else:
        if temp[1] > maiorPeso:
            maiorPeso = temp[1]
        if temp[1] < menorPeso:
            menorPeso = temp[1]
    principal.append(temp[:])
    temp.clear()
    resp = str(input('Deseja continuar? [S / N] ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'Foram cadastradas ao todo {len(principal)} pessoas.')
print(f'O maior peso foi {maiorPeso}KG. Peso de ', end='')
for p in principal:
    if p[1] == maiorPeso:
        print(f'[{p[0]}] ', end='')
print()
print(f'O menor peso foi {menorPeso}KG. Peso de ', end='')
for p in principal:
    if p[1] == menorPeso:
        print(f'[{p[0]}] ', end='')
