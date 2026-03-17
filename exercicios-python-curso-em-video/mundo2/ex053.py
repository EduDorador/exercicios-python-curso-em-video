frase = str(input('Digite uma frase: ')).strip().upper().split()
junto = ''.join(frase)
inverso = ''
#inverso = junto[::-1]
for letra in range(len(junto) - 1, -1 , -1):
    inverso += junto[letra]
print(f'O inverso de {junto} é {inverso}')
if junto == inverso:
    print('A frase digitada É UM PALÍNDROMO!')
else:
    print('A frase digitada NÃO É UM PALÍNDROMO!')
