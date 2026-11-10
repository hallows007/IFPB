# Calculate the average of the even numbers among four entered integers.

lista = []
soma = 0
contador = 0

for i in range(4):
    num = int(input('Digite os numeros: '))
    lista.append(num)

for numeros in lista:
    if numeros % 2 == 0:
        contador = contador + 1
        soma = soma + numeros

media = soma / contador

print(f'a media é de {media}')