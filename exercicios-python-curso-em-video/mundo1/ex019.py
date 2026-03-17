from random import choice
aluno1 = input('Digite o nome do primeiro aluno(a): ')
aluno2 = input('Digite o nome do segundo aluno(a): ')
aluno3 = input('Digite o nome do terceiro aluno(a): ')
aluno4 = input('Digite o nome do quarto aluno(a): ')
lista = [aluno1, aluno2, aluno3, aluno4]
escolhido = choice(lista)
print(f'O aluno sorteado para apagar a lousa foi: {escolhido}')
