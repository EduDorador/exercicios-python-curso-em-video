alt = float(input('Qual a altura da parede? '))
larg = float(input('Qual a largura da parede? '))
area = alt * larg
tinta = area / 2
print(f'A dimensões da parede são: Altura {alt:.2f} x Largura {larg:.2f} ... Totalizando {area}m².')
print(f'Será necessário {tinta} litros de tinta, para pintar toda área.')
