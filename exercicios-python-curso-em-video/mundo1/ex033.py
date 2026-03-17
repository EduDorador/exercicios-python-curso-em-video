a = int(input('Digite o primeiro valor: '))
b = int(input('Digite o segundo valor: '))
c = int(input('Digite o terceiro valor: '))
#Verificando qual número é menor:
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c

#Verificando qual número é maior:
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print(f'O menor número digitado foi: {menor}')
print(f'O maior número digitado foi: {maior}')
