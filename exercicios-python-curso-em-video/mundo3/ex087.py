matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
totPar = totTerceira = maiorValor = 0
for linha in range(0, 3): #Recebe os valores da matriz
    for coluna in range (0, 3):
        matriz[linha][coluna] = int(input('Digite um valor: '))
print('=-' * 30)
for linha in range(0, 3): #Realiza o print no modelo da matriz
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
        if matriz[linha][coluna] % 2 == 0: #Soma o total de pares
            totPar += matriz[linha][coluna]
    print()
for linha in range(0, 3): #Soma os valores da terceira coluna
    totTerceira += matriz[linha][2]
for coluna in range(0, 3): #Calcula o maior valor da segunda linha
    if coluna == 0:
        maiorValor = matriz[1][coluna]
    elif matriz[1][coluna] > maiorValor:
        maiorValor = matriz[1][coluna]
print('=-' * 30)
print(f'A soma dos valores pares é {totPar}')
print(f'A soma dos valores da terceira coluna {totTerceira}')
print(f'O maior valor da segunda linha é {maiorValor}')
