distancia = float(input('Qual a distância de sua viagem em KM? '))
print(f'Você está prestes a começar uma viagem de {distancia:.1f}km')
if distancia <= 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45
print(f'O preço de sua passagem será de R$ {preco:.2f}')
