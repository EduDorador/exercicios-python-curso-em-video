from datetime import date
ano_atual = date.today().year
maior_idade = 0
menor_idade = 0
for c in range(1, 8):
    ano_nascimento = int(input(f'Em que ano a {c}º pessoa nasceu? '))
    idade = ano_atual- ano_nascimento
    if idade >= 21:
        maior_idade += 1
    else:
        menor_idade += 1
print(f'Ao todo {maior_idade} são maiores de idade. \nE {menor_idade} são menores de idade.')
