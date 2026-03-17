totCompra = totMil = cont = menorPreco = 0
produtoBarato = ''
print('-' * 40)
print(f"{'LOJA SUPER BARATÃO':^40}")
print('-' * 40)
while True:
    produto = str(input('Nome do Produto: ')).strip().capitalize()
    preco = float(input('Preço: R$ '))
    totCompra += preco
    cont += 1
    if preco > 1000:
        totMil += 1
    if cont == 1 or preco < menorPreco:
        produtoBarato = produto
        menorPreco = preco
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('-' * 40)
print(f'O total da compra foi R$ {totCompra:.2f}')
print(f'Temos {totMil} produtos custando mais de R$ 1.000,00')
print(f'O produtos mais barato foi {produtoBarato} que custa {menorPreco:.2f}')
