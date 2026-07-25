def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = n
            ok = True
        else:
            print(f'\33[0;31mErro! Digite um número inteiro válido!\33[m')
        if ok:
            break
    return valor

#Programa Principal
n = leiaInt('Digite um número inteiro: ')
print(f'Você digitou o número {n}')
