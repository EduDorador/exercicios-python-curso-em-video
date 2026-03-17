peso = float(input('Digite o seu peso: (Kg) '))
altura = float(input('Digite a sua altura: (M) '))
imc = peso / (pow(altura, 2))
print(f'O seu IMC é de {imc:.1f}')
if imc < 18.5:
    print('Você está abaixo do peso!')
elif imc >= 18.5 and imc < 25:
    print('Parabéns, você está no peso ideal!')
elif imc >= 25 and imc < 30:
    print('Você está com Sobrepeso!')
elif imc >= 30 and imc < 40:
    print('Você está com Obesidade, cuidado!')
else:
    print('Você está com Obesidade Mórbida, procure ajuda urgente!')
