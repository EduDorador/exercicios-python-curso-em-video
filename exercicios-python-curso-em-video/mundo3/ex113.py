def leiaInt(msg):
    while True:
        try:
            num = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO! Número inteiro digitado inválido!\033[m')
            continue
        except (KeyboardInterrupt):
            print('\n\033[31mEntrada de dados interrompida pelo usuário!\033[m')
            return 0
        else:
            return num


def leiaFloat(msg):
    while True:
        try:
            num = float(input(msg))
        except (ValueError, TypeError):
            print('\033[31mErro! Número real digitado inválido!\033[m')
            continue
        except (KeyboardInterrupt):
            print('\n\033[31mEntrada de dados interrompida pelo usuário!\033[m')
            return 0
        else:
            return num


n1 = leiaInt('Digite um número Inteiro: ')
n2 = leiaFloat('Digite um número Real: ')
print(f'O número inteiro digitado foi {n1} e o número real digitado foi {n2}')
