def area(larg, comp):
    a = larg * comp
    print(f'A área de um terreno {larg:.1f} x {comp:.1f} é de {a:.1f}m².')


#Programa Principal
print('Controle de Terrenos!')
print('-' * 20)
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
area(l, c)
