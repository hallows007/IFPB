# Check whether eight entered numbers are in strictly increasing order.

numeros = []
contador = 0
for i in range(8):
    numero = float(input('Digite um numero: '))
    numeros.append(numero)

primeiro = numeros[0]

for l in range(len(numeros) - 1):
    if numeros[l + 1] > numeros[l]:
        contador +=1
    else:
        break

if contador == 7:
    print('A lista está em ordem crescente!')
else:
    print('A lista não esta em ordem crescente')