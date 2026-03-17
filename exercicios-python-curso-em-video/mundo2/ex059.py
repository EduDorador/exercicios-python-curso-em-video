from time import sleep
num1 = int(input('Digite o primeiro valor: '))
num2 = int(input('Digite o segundo valor: '))
rodando = True
while rodando:
    print('''[1] SOMAR
[2] MULTIPLICAR
[3] MAIOR
[4] NOVOS NÚMEROS
[5] SAIR DO PROGRAMA''')
    opcao = int(input('>>>>> Qual é a sua opção? '))
    if opcao == 1:
        soma = num1 + num2
        print(f'O resultado de {num1} + {num2} é {soma}')
    elif opcao == 2:
        produto = num1 * num2
        print(f'O resultado de {num1} x {num2} é {produto}')
    elif opcao == 3:
        if num1 == num2:
            print(f'Os números são iguais')
        elif num1 > num2:
            print(f'O maior número é {num1}')
        else:
            print(f'O maior número é {num2}')
    elif opcao == 4:
        num1 = int(input('Digite novamente o primeiro valor: '))
        num2 = int(input('Digite novamente o segundo valor: '))
    elif opcao == 5:
        print('Fim do programa, volte sempre!')
        rodando = False
    else:
        print('Opção inválida, tente novamente!')
    print('=-=' * 10)
    sleep(2)
