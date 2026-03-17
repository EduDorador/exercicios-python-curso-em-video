from math import cos, sin, tan, radians
angulo = float(input('Digite um ângulo: '))
print(f'O Ângulo digitado foi: {angulo:.0f}')
print(f'O seu Seno é: {sin(radians(angulo)):.2f}')
print(f'O seu Cosseno é: {cos(radians(angulo)):.2f}')
print(f'Tangente: {tan(radians(angulo)):.2f}')
