from random import shuffle
n1 = input('Nome do primeiro aluno(a): ')
n2 = input('Nome do segundo aluno(a): ')
n3 = input('Nome do terceiro aluno(a): ')
n4 = input('Nome do quarto aluno(a): ')
lista = [n1, n2, n3, n4]
shuffle(lista)
print(f'A ordem de apresentação dos alunos será: {lista}')
