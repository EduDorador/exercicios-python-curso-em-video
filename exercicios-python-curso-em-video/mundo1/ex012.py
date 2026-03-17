valor = float(input('Digite o valor do produto: '))
novo_valor = valor - (valor * 5 / 100)
print(f'O valor do produto é R$ {valor:.2f} com desconto de 5% ele sairá por: R$ {novo_valor:.2f}')
