num = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão:
[ 1 ] Converter para BINÁRIO
[ 2 ] Converter para OCTAL
[ 3 ] Converter para HEXADECIMAL''')
opcao = int(input('Sua opção: '))
if opcao == 1:
    print(f'O número inteiro {num} em BINÁRIO é: {bin(num)[2:]}')
elif opcao == 2:
    print(f'O número inteiro {num} em OCTAL é: {oct(num)[2:]}')
elif opcao ==3:
    print(f'O número inteiro {num} em HEXADECIMAL é: {hex(num)[2:]}')
else:
    print('Opção inválida, tente novamente!...')
