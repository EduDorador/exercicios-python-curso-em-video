from ex107 import moeda

p = float(input('Digite um preço: R$ '))
print(f'A metade do valor R$ {p} é R$ {moeda.metade(p)}')
print(f'O dobro do valor R$ {p} é R$ {moeda.dobro(p)}')
print(f'Aumentando em 10%, temos R$ {moeda.aumentar(p, 10)}')
print(f'Reduzindo em 13%, temos R$ {moeda.diminuir(p, 13)}')
