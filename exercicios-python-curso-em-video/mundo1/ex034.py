salario = float(input('Digite o seu salário atual: R$ '))
if salario <= 1250:
    novoSal = salario + (salario * 15 / 100)
else:
    novoSal = salario + (salario * 10 / 100)
print(f'Seu novo salário é de R$ {novoSal:.2f}')
