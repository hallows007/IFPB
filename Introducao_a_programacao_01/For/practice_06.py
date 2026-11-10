# Read three numbers and find the largest and smallest values.

lista = []


for i in range(3):
    num = int(input("Digite o numero: "))
    lista.append(num)
    maior = num
    menor = num

for numeros in lista:
    if numeros > maior:
        maior = numeros
    elif numeros < menor:
        menor = numeros

print(f'O maior numero é o {maior} e o menor é o {menor}')