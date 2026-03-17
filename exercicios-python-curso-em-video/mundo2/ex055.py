maior_peso = 0
menor_peso = 0
for cont in range(1, 6):
    peso = float(input(f'Qual o peso da {cont}º pessoa? '))
    if cont == 1:
        maior_peso = peso
        menor_peso = peso
    else:
        if peso > maior_peso:
            maior_peso = peso
        if peso < menor_peso:
            menor_peso = peso
    
print(f'O maior peso informado foi {maior_peso}kg')
print(f'O menor peso informado foi {menor_peso}kg')
