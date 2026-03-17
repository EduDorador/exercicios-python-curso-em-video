from datetime import date
ano_atual = date.today().year
sexo = str(input('Qual é o seu gênero? [M] ou [F]' )).strip().upper()
if sexo == 'F':
    print('Você não precisa fazer alistamento militar obrigatório!')
elif sexo == 'M':
    ano_nasc = int(input('Digite o seu ano de nascimento: '))
    idade = ano_atual - ano_nasc
    print(f'Quem nasceu em {ano_nasc} tem {idade} anos em {ano_atual}')
    if idade == 18:
        print('Você tem que se alistar IMEDIATAMENTE!')
    elif idade < 18:
        saldo = 18 - idade
        ano = ano_atual + saldo
        print(f'Ainda faltam {saldo} anos para o alistamento')
        print(f'Seu alistamento será em {ano}')
    else:
        saldo = idade - 18
        ano = ano_atual - saldo
        print(f'Você já deveria ter se alistado há {saldo} anos')
        print(f'Seu alistamento foi em {ano}')
else:
    print('Dígito inválido, tente novamente...')
