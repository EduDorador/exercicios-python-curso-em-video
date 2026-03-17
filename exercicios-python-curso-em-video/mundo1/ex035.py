print('-=-' * 9)
print('Analisador de Triângulos')
print('-=-' * 9)
a = float(input('Primeiro Segmento: '))
b = float(input('Segundo Segmento: '))
c = float(input('Terceiro Segmento: '))
if a + b > c and a + c > b and b + c > a:
    print('O segmento acima podem formar um TRIÂNGULO!')
else:
    print('O segmento acima NÃO podem formar um TRIâNGULO!')
