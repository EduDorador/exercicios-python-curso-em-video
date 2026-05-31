from datetime import date
dados = dict()
dados['nome'] = str(input('Nome: '))
anoNascimento = int(input('Ano de nascimento: '))
dados['idade'] = date.today().year - anoNascimento
dados['ctps'] = int(input('Carteira de trabalho (0 Não tem): '))
if dados['ctps'] != 0:
    dados['contratação'] = int(input('Ano de contratação: '))
    dados['salário'] = float(input('Salário: R$ '))
    dados['aposentadoria'] = dados['idade'] + ((dados['contratação'] + 35) - date.today().year)
print('-=' * 25)
for k, v in dados.items():
    print(f'   -> {k} tem o valor {v}')
