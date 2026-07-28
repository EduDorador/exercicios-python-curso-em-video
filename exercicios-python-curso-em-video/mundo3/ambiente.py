try: #Tentativa
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except (ValueError, TypeError): #Retorno se der errado a tentativa.
    print('Tivemos um problema com os tipos de dados que você digitou.')
except ZeroDivisionError:
    print('Não é possível dividir um número por zero!')
except KeyboardInterrupt:
    print('O usuário preferiu não informar os dados!')
except Exception as erro:
    print(f'O erro encontrado foi {erro.__cause__}')
else: #Retorno se der tudo certo a tentativa.
    print(f'O resultado é {r}')
finally: #Acontecerá sempre independente do retorno.
    print('Volte sempre, muito obrigado!')
