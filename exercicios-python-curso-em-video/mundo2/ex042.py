a = int(input('Primeiro segmento: '))
b = int(input('Segundo segmento: '))
c = int(input('Terceiro segmento: '))

if a + b > c and a + c > b and b + c > a:
    print('Os segmentos podem formar um triângulo', end=' ')
    if a == b and b == c:
        print('EQUILÁTERO!')
    elif a != b and a != c and b != c:
        print('ESCALENO!')
    else:
        print('ISÓSCELES!')
else:
    print('Não é possível formar um triângulo!')
