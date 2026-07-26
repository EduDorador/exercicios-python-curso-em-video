from ex109 import moeda

p = float(input('Digite um preço: R$ '))
print(f'A metade do valor {moeda.moeda(p)} é {moeda.metade(p, True)}')
print(f'O dobro do valor {moeda.moeda(p)} é {moeda.dobro(p, True)}')
print(f'Aumentando em 10%, temos {moeda.aumentar(p, 10, True)}')
print(f'Reduzindo em 13%, temos {moeda.diminuir(p, 13, True)}')
