ficha = list()
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    resp = str(input('Deseja continuar? [S / N] ')).strip().upper()[0]
    if resp in 'N':
        break
print('-=' * 30)
print(f'{"No.":<5}{"NOME":<10}{"MÉDIA":>8}')
for pos, aluno in enumerate(ficha):
    print(f'{pos:<5}{aluno[0]:<10}{aluno[2]:>8}')
print('-' * 30)
while True:
    opc = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    print('-' * 30)
    if opc == 999:
        print('FINALIZANDO...')
        break
    if opc <= len(ficha) -1:
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')
print('<<< VOLTE SEMPRE! >>>')
