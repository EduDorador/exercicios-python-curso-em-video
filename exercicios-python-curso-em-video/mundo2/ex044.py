preco = float(input('Preço das compras - R$: '))
opcao = int(input('''FORMAS DE PAGAMENTO:
[ 1 ] à vista Dinheiro / Cheque
[ 2 ] à vista no cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão
Qual será a opção de pagamento? '''))
if opcao == 1:
    novo_preco = preco - (preco * 10 / 100)
elif opcao == 2:
    novo_preco = preco - (preco * 5 / 100)
elif opcao == 3:
    novo_preco = preco
    parcela = preco / 2
    print(f'Sua compra será parcelada em 2x de R$ {parcela:.2f} sem juros.')
elif opcao == 4:
    novo_preco = preco + (preco * 20 / 100)
    qnt_parcelas = int(input('Quantas parcelas? '))
    valor_parcelas = novo_preco / qnt_parcelas
    print(f'Sua compra será parcelada em {qnt_parcelas}x de R$ {valor_parcelas:.2F} COM JUROS')
else:
    novo_preco = preco
    print('\033[41mOpção INVÁLIDA, tente novamente!...\033[m')
print(f'Sua compra de R$ {preco:.2f} vai custar R$ {novo_preco:.2f} no final.')
