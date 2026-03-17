soma_idade = 0
media_idade = 0
idade_homemvelho = 0
nome_homemvelho = ''
mulher_menor20 = 0
for c in range(1, 5):
    print(f"{f' {c}º PESSOA ':-^20}")
    nome = str(input('Qual é o seu nome? ')).strip()
    idade = int(input('Qual é a sua idade? '))
    sexo = str(input('Qual é o seu sexo? [M / F] ')).strip().upper()
    soma_idade += idade
    if c == 1 and sexo =='M':
        idade_homemvelho = idade
        nome_homemvelho = nome
    if sexo == 'M' and idade > idade_homemvelho:
        idade_homemvelho = idade
        nome_homemvelho = nome
    if sexo == 'F' and idade < 20:
        mulher_menor20 += 1
media_idade = soma_idade / 4
print(f'A média de idade do grupo é de {media_idade:.2f}')
print(f'O homem mais velho tem {idade_homemvelho} anos e se chama {nome_homemvelho}')
print(f'Ao todo são {mulher_menor20} mulheres com menos de 20 anos de idade')
